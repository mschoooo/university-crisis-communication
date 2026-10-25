# -*- coding: utf-8 -*-
"""Render and verify the 15-slide v10 HTML deck and save its PDF.

Requires local Playwright, Chromium, Pillow and PyMuPDF.
"""

import re
import sys
from pathlib import Path
from bs4 import BeautifulSoup
from PIL import Image, ImageOps, ImageDraw
import pymupdf
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
DECK = ROOT / "versions" / "deck_v13"
QA = ROOT / "qa" / "deck_v13"
QA.mkdir(parents=True, exist_ok=True)
PDF = DECK / "deck_v13.pdf"
problems = []

html = (DECK / "index.html").read_text(encoding="utf-8")
sources = (DECK / "sources.html").read_text(encoding="utf-8")
references = (DECK / "deck_v13_참고문헌.md").read_text(encoding="utf-8")
if "평의원회 회의록 원본은 미확보" not in references or "이사회 결의서가 아니다" not in references:
    problems.append("Reference types for D14 or D22 are not properly qualified")
if "2025-12-03~07 학생 총투표" in sources:
    problems.append("The source index still asserts an unverified vote end date")
slide_nodes = BeautifulSoup(html, "html.parser").select("section.slide")
if len(slide_nodes) != 15:
    problems.append(f"Expected 15 HTML slides, found {len(slide_nodes)}")
for number, slide in enumerate(slide_nodes[:13], 1):
    if "베노이트" in slide.get_text(" ", strip=True) or "Benoit" in slide.get_text(" ", strip=True):
        problems.append(f"Benoit analysis found before final page: slide {number}")
if "베노이트" not in slide_nodes[13].get_text(" ", strip=True):
    problems.append("Slide 14 is missing the Benoit analysis")
slide_text = [node.get_text(" ", strip=True) for node in slide_nodes]
for number, required in {2:["메시지", "행동", "반응"], 5:["사과", "심의"], 6:["8:12", "해명"], 7:["24명", "11명", "직원협의회"], 8:["단독 결정", "학생 요구"], 9:["잠정 중단", "수업 재개"], 10:["공론화", "51.8%", "대표성"], 11:["85.7%", "학생 반응"], 13:["신뢰 회복", "미확인"], 14:["베노이트", "발화의 전략", "조치와 관찰 결과"]}.items():
    for term in required:
        if term not in slide_text[number-1]:
            problems.append(f"Slide {number} missing required fact: {term}")
if any(term in html for term in ["12.03~07", "12/3~7", "2025.12.03.~07.", "2026.03.03", "생존 위기:"]):
    problems.append("An unverified date or claim remains in the deck")
toc = BeautifulSoup(html, "html.parser").select(".toc-item")
for i, (button, slide) in enumerate(zip(toc, slide_nodes), 1):
    title = (slide.find(["h1", "h2"]) or slide).get_text(" ", strip=True)
    if title not in button.get_text(" ", strip=True):
        problems.append(f"Table of contents mismatch on slide {i}")
report = (DECK / "카메룬_81개_변수_전수분석.md").read_text(encoding="utf-8")
if len(re.findall(r"^\| [EI]\d+ ", report, re.M)) != 81:
    problems.append("The linked report does not contain all 81 variable rows")
for local_name in ["deck_v13.pdf", "카메룬_81개_변수_전수분석.md", "sources.html", "asset_sources.md"]:
    if f'href="{local_name}"' not in html:
        problems.append(f"Missing deck link to {local_name}")
for link in BeautifulSoup(html, "html.parser").select("a[href]"):
    href = link["href"].split("#", 1)[0]
    if href and not href.startswith(("https://", "http://", "mailto:")) and not (DECK / href).exists() and href != "deck_v13.pdf":
        problems.append(f"Broken local link: {href}")
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
    print(f"Found {count} slides in deck_v13.")

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







