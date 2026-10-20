"""Render every slide, inspect geometry, and save the versioned PDF.

Requires local Chrome, Playwright, Pillow and PyMuPDF. Screenshots and a contact
sheet stay in qa/; the PDF is stored with the corresponding HTML version.
"""

from pathlib import Path
from PIL import Image, ImageOps, ImageDraw
from playwright.sync_api import sync_playwright
import fitz


ROOT = Path(__file__).resolve().parents[1]
DECK = ROOT / "versions" / "v1"
QA = ROOT / "qa" / "v1"
QA.mkdir(parents=True, exist_ok=True)
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
HTML = (DECK / "index.html").resolve().as_uri()
PDF = DECK / "deck_v1.pdf"
problems = []

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(executable_path=CHROME, headless=True)
    page = browser.new_page(viewport={"width": 1600, "height": 900}, device_scale_factor=1)
    page.on("pageerror", lambda error: problems.append(f"JavaScript: {error}"))
    page.goto(HTML, wait_until="load")
    count = page.locator(".slide").count()
    if count != 10:
        problems.append(f"Expected 10 slides, found {count}")
    for slide_number in range(1, count + 1):
        page.evaluate("index => show(index)", slide_number - 1)
        page.wait_for_timeout(50)
        if not page.locator(f".slide:nth-child({slide_number})").evaluate("element => element.classList.contains('active')"):
            problems.append(f"Slide {slide_number} did not activate")
        check = page.evaluate("""() => {
          const slide=document.querySelector('.slide.active');
          const footer=slide.querySelector('footer').getBoundingClientRect();
          const boxes=[...slide.children].filter(el=>el.tagName!=='FOOTER').map(el=>({
            tag:el.tagName, cls:el.className, bottom:el.getBoundingClientRect().bottom,
            right:el.getBoundingClientRect().right,
            top:el.getBoundingClientRect().top,
          }));
          const imgs=[...slide.querySelectorAll('img')].map(el=>({src:el.getAttribute('src'),loaded:el.complete&&el.naturalWidth>0}));
          return {footerTop:footer.top, boxes, imgs};
        }""")
        for image in check["imgs"]:
            if not image["loaded"]:
                problems.append(f"Slide {slide_number} image failed: {image['src']}")
        for box in check["boxes"]:
            if box["bottom"] > check["footerTop"] - 4:
                problems.append(f"Slide {slide_number} {box['tag']}.{box['cls']} overlaps footer by {box['bottom']-check['footerTop']:.1f}px")
            if box["right"] > 1599 or box["top"] < -1:
                problems.append(f"Slide {slide_number} {box['tag']}.{box['cls']} outside canvas")
        page.screenshot(path=str(QA / f"slide_{slide_number:02d}.png"), full_page=False)

    # Printing shows all sections through @media print, independent of current slide.
    page.emulate_media(media="print")
    page.pdf(path=str(PDF), print_background=True, prefer_css_page_size=True, display_header_footer=False)
    browser.close()

contact = Image.new("RGB", (960, 1350), "#dddeda")
for slide_number in range(1, 11):
    with Image.open(QA / f"slide_{slide_number:02d}.png") as image:
        small = image.resize((480, 270), Image.Resampling.LANCZOS)
        x = ((slide_number - 1) % 2) * 480
        y = ((slide_number - 1) // 2) * 270
        contact.paste(small, (x, y))
contact.save(QA / "contact_sheet.png")

document = fitz.open(PDF)
if len(document) != 10:
    problems.append(f"Expected 10 PDF pages, found {len(document)}")
for number, pdf_page in enumerate(document, 1):
    if not pdf_page.get_text().strip():
        problems.append(f"PDF page {number} has no extractable text")
    if abs(pdf_page.rect.width / pdf_page.rect.height - 16 / 9) > 0.002:
        problems.append(f"PDF page {number} aspect ratio is not 16:9")
document.close()

print(f"Slides: {count}; PDF pages: {len(fitz.open(PDF))}; PDF: {PDF}")
print(f"Contact sheet: {QA / 'contact_sheet.png'}")
print("Problems:", problems)
if problems:
    raise SystemExit(1)
