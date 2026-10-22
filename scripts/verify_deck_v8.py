# -*- coding: utf-8 -*-
"""Render and verify the 15-slide v8 HTML deck and save its PDF.

Requires local Playwright, Chromium, Pillow and PyMuPDF.
"""

import re
import sys
from pathlib import Path
from PIL import Image, ImageOps, ImageDraw
import pymupdf
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
DECK = ROOT / "versions" / "deck_v8"
QA = ROOT / "qa" / "deck_v8"
QA.mkdir(parents=True, exist_ok=True)
PDF = DECK / "deck_v8.pdf"
problems = []

html = (DECK / "index.html").read_text(encoding="utf-8")
sources = (DECK / "sources.html").read_text(encoding="utf-8")
targets = set(re.findall(r'href="sources\.html#([A-Z][A-Z0-9]*)"', html))
available = set(re.findall(r'id="([A-Z][A-Z0-9]*)"', sources))
missing = targets - available
if missing:
    problems.append(f"Source anchors missing in sources.html: {sorted(missing)}")
else:
    print(f"All {len(targets)} source anchors verified.")

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1600, "height": 900}, device_scale_factor=1)
    page.emulate_media(reduced_motion="reduce")
    page.on("pageerror", lambda error: problems.append(f"JavaScript: {error}"))
    page.goto((DECK / "index.html").resolve().as_uri(), wait_until="load")
    page.evaluate("document.fonts.ready")
    count = page.locator(".slide").count()
    if count != 15:
        problems.append(f"Expected 15 slides, found {count}")
    print(f"Found {count} slides in deck_v8.")

    failures = []
    for number in range(1, count + 1):
        page.evaluate("(n) => show(n - 1)", number)
        page.wait_for_timeout(100)
        out = QA / f"slide_{number:02d}.png"
        page.locator("#stage").screenshot(path=str(out))

        result = page.evaluate("""() => {
          const slide = document.querySelector('.slide.active');
          const footer = slide.querySelector('footer')?.getBoundingClientRect();
          const footerTop = footer ? footer.top : 900;
          const bad = [];
          for (const el of slide.querySelectorAll('h1,h2,h3,p,figcaption,.source-footer,.paper-slip,.headline-strip,.vote-block,.survey-major,.aftermath-card,.publics-grid,.conclusion-list,.two-case-grid,.var-columns,.parallel-grid,.deep-grid,.compare-votes-grid,.deliberation-layout,.v7-flow,.v7-foresight,.v7-pj,.v6-conclusion,.reference-columns')) {
            const r = el.getBoundingClientRect();
            const s = slide.getBoundingClientRect();
            const intended = el.closest('.cover-archive') || el.classList.contains('final-quote');
            if (!intended && (r.right > s.right + 6 || r.bottom > s.bottom + 6 || r.left < s.left - 6)) {
              bad.push(el.tagName + '.' + el.className + ':bottom_overflow=' + Math.round(r.bottom - s.bottom));
            }
            if (footer && !el.closest('footer') && el.tagName !== 'FOOTER' && r.bottom > footerTop + 4) {
              bad.push(el.tagName + '.' + el.className + ':overlaps_footer=' + Math.round(r.bottom - footerTop));
            }
          }
          const missing = [...slide.querySelectorAll('img')].filter(i => !i.complete || i.naturalWidth === 0).map(i => i.getAttribute('src'));
          return {bad, missing};
        }""")
        if result["bad"] or result["missing"]:
            failures.append((number, result))

    # Keyboard test
    page.keyboard.press("Home")
    page.keyboard.press("ArrowRight")
    if page.locator("#count").inner_text() != f"2 / {count}":
        problems.append(f"Keyboard navigation failed: got {page.locator('#count').inner_text()}")
    page.goto((DECK / "index.html").resolve().as_uri() + "#9", wait_until="load")
    if page.locator("#count").inner_text() != f"9 / {count}":
        problems.append(f"URL hash navigation failed: got {page.locator('#count').inner_text()}")

    # Generate PDF
    page.pdf(path=str(PDF), width="1600px", height="900px", print_background=True,
             prefer_css_page_size=True, display_header_footer=False)
    browser.close()

# Create contact sheet
thumbs = []
for number in range(1, count + 1):
    image = Image.open(QA / f"slide_{number:02d}.png").convert("RGB")
    thumb = ImageOps.fit(image, (400, 225))
    draw = ImageDraw.Draw(thumb)
    draw.rectangle((0, 0, 42, 25), fill=(25, 28, 26))
    draw.text((8, 5), f"{number:02d}", fill=(255, 255, 255))
    thumbs.append(thumb)

sheet = Image.new("RGB", (1600, 900), "#ddd")
for i, thumb in enumerate(thumbs):
    sheet.paste(thumb, ((i % 4) * 400, (i // 4) * 225))
sheet.save(QA / "contact_sheet.png")

# Verify PDF
doc = pymupdf.open(PDF)
if len(doc) != 15:
    problems.append(f"Expected 15 PDF pages, found {len(doc)}")
for number, pdf_page in enumerate(doc, 1):
    if not pdf_page.get_text().strip():
        problems.append(f"PDF page {number} has no extractable text")
    ratio = pdf_page.rect.width / pdf_page.rect.height
    if abs(ratio - 16 / 9) > 0.005:
        problems.append(f"PDF page {number} aspect ratio is {ratio:.3f}, not 16:9")

print("=== VERIFICATION SUMMARY ===")
print(f"Rendered {count} slides to {QA}")
print(f"Contact sheet saved to {QA / 'contact_sheet.png'}")
print(f"PDF exported to {PDF} ({len(doc)} pages)")
if failures:
    print("Layout issues:", failures)
else:
    print("Layout checks: PASSED (no boundary overflows or missing images)")

if problems:
    print("Problems found:", problems)
    sys.exit(1)
else:
    print("All verification checks PASSED!")

