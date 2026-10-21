"""Render and verify the 14-slide v3 HTML deck and save its PDF.

Requires local Chrome, Playwright, Pillow and PyMuPDF. QA images stay outside
the public git repository; the PDF is stored with the immutable v3 HTML files.
"""

import re
from pathlib import Path

import pymupdf
from PIL import Image
from playwright.sync_api import sync_playwright


ROOT = Path(__file__).resolve().parents[1]
DECK = ROOT / "versions" / "deck_v3_수정본"
QA = ROOT / "qa" / "deck_v3_수정본"
QA.mkdir(parents=True, exist_ok=True)
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
PDF = DECK / "deck_v3_수정본.pdf"
problems = []

html = (DECK / "index.html").read_text(encoding="utf-8")
sources = (DECK / "sources.html").read_text(encoding="utf-8")
targets = set(re.findall(r'href="sources\.html#([A-Z][A-Z0-9]*)"', html))
available = set(re.findall(r'id="([A-Z][A-Z0-9]*)"', sources))
missing = targets - available
if missing:
    problems.append(f"Source anchors missing: {sorted(missing)}")

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(executable_path=CHROME, headless=True)
    page = browser.new_page(viewport={"width": 1600, "height": 900}, device_scale_factor=1)
    page.on("pageerror", lambda error: problems.append(f"JavaScript: {error}"))
    page.goto((DECK / "index.html").resolve().as_uri(), wait_until="load")
    count = page.locator(".slide").count()
    if count != 14:
        problems.append(f"Expected 14 slides, found {count}")
    for number in range(1, count + 1):
        page.evaluate("index => show(index)", number - 1)
        page.wait_for_timeout(60)
        check = page.evaluate("""() => {
          const slide = document.querySelector('.slide.active');
          const footer = slide.querySelector('footer').getBoundingClientRect();
          const boxes = [...slide.querySelectorAll('*')]
            .filter(el => el.tagName !== 'FOOTER' && !el.closest('footer'))
            .map(el => ({tag:el.tagName, cls:el.className?.baseVal || el.className || '',
              bottom:el.getBoundingClientRect().bottom,
              right:el.getBoundingClientRect().right,
              top:el.getBoundingClientRect().top}));
          const imgs = [...slide.querySelectorAll('img')]
            .map(el => ({src:el.getAttribute('src'), loaded:el.complete && el.naturalWidth>0}));
          return {footerTop:footer.top, boxes, imgs};
        }""")
        for item in check["imgs"]:
            if not item["loaded"]:
                problems.append(f"Slide {number} image failed: {item['src']}")
        for box in check["boxes"]:
            if box["bottom"] > check["footerTop"] - 2:
                problems.append(
                    f"Slide {number} {box['tag']}.{box['cls']} overlaps footer "
                    f"by {box['bottom'] - check['footerTop']:.1f}px"
                )
            if box["right"] > 1599 or box["top"] < -1:
                problems.append(f"Slide {number} {box['tag']}.{box['cls']} outside canvas")
        page.screenshot(path=str(QA / f"slide_{number:02d}.png"), full_page=False)

    page.keyboard.press("Home")
    page.keyboard.press("ArrowRight")
    if page.locator("#count").inner_text() != f"2 / {count}":
        problems.append("Keyboard navigation failed")
    page.goto((DECK / "index.html").resolve().as_uri() + "#9", wait_until="load")
    if page.locator("#count").inner_text() != f"9 / {count}":
        problems.append("URL hash navigation failed")
    page.emulate_media(media="print")
    page.pdf(path=str(PDF), print_background=True, prefer_css_page_size=True, display_header_footer=False)
    browser.close()


def contact_sheet(paths, output, cols=2, cell=(480, 270)):
    rows = (len(paths) + cols - 1) // cols
    board = Image.new("RGB", (cols * cell[0], rows * cell[1]), "#dddeda")
    for i, path in enumerate(paths):
        with Image.open(path) as source:
            image = source.convert("RGB").resize(cell, Image.Resampling.LANCZOS)
            board.paste(image, ((i % cols) * cell[0], (i // cols) * cell[1]))
    board.save(output)


contact_sheet([QA / f"slide_{i:02d}.png" for i in range(1, count + 1)], QA / "contact_sheet.png")

document = pymupdf.open(PDF)
if len(document) != 14:
    problems.append(f"Expected 14 PDF pages, found {len(document)}")
pdf_images = []
for number, pdf_page in enumerate(document, 1):
    if not pdf_page.get_text().strip():
        problems.append(f"PDF page {number} has no extractable text")
    if abs(pdf_page.rect.width / pdf_page.rect.height - 16 / 9) > 0.002:
        problems.append(f"PDF page {number} aspect ratio is not 16:9")
    pix = pdf_page.get_pixmap(matrix=pymupdf.Matrix(0.4, 0.4), alpha=False)
    png = QA / f"pdf_{number:02d}.png"
    pix.save(png)
    pdf_images.append(png)
document.close()
contact_sheet(pdf_images, QA / "pdf_contact_sheet.png")

print(f"Slides: {count}; PDF pages: {len(pdf_images)}; source anchors: {len(targets)}")
print(f"PDF: {PDF}; QA: {QA / 'contact_sheet.png'}")
print("Problems:", problems)
if problems:
    raise SystemExit(1)

