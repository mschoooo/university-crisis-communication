# -*- coding: utf-8 -*-
"""Verify v14 content, links, viewport centering, rendered slides and PDF."""
from pathlib import Path
import re
import sys
from bs4 import BeautifulSoup
from PIL import Image, ImageOps, ImageDraw
import pymupdf
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
DECK = ROOT / "versions" / "deck_v14"
QA = ROOT / "qa" / "deck_v14"
QA.mkdir(parents=True, exist_ok=True)
PDF = DECK / "deck_v14.pdf"
issues = []
html = (DECK / "index.html").read_text(encoding="utf-8")
source_html = (DECK / "sources.html").read_text(encoding="utf-8")
soup = BeautifulSoup(html, "html.parser")
slides = soup.select("section.slide")
if len(slides) != 15: issues.append(f"Expected 15 slides, got {len(slides)}")
if "카메룬" in html or "전수 적용" in html: issues.append("Uncorrected theory name or unsupported blanket application claim")
if "왜 갈등을 멈추지 못했나" in slides[0].get_text(" ", strip=True): issues.append("Cover still states an unqualified result")
requirements = {
    5: ["사과", "심의 보류", "A03P"],
    6: ["8", "12", "A01P"],
    7: ["24명", "11명", "15 : 6", "A07"],
    8: ["의제설정 이전", "제한적 부인", "D26"],
    9: ["잠정 중단", "수업 재개", "D02"],
    10: ["51.8%", "71.3%", "D07"],
    11: ["85.7%", "2029", "D09"],
    12: ["강원대", "동덕여대", "기존 신뢰"],
    13: ["확인된 행동 변화", "판정 유보", "신뢰"],
    14: ["종합 결론", "실무 제언", "01", "02", "03"],
}
for n, terms in requirements.items():
    text = slides[n - 1].get_text(" ", strip=True)
    for term in terms:
        if term not in text: issues.append(f"Slide {n} lacks {term}")
for i, (button, slide) in enumerate(zip(soup.select(".toc-item"), slides), 1):
    title = slide.find(["h1", "h2"]).get_text(" ", strip=True)
    if title not in button.get_text(" ", strip=True): issues.append(f"TOC mismatch on slide {i}")
available = set(re.findall(r'id="([A-Z][A-Z0-9]*)"', source_html))
targets = set(re.findall(r'href="sources\.html#([A-Z][A-Z0-9]*)"', html))
if targets - available: issues.append(f"Missing source anchors: {targets-available}")
for a in soup.select("a[href]"):
    href = a["href"].split("#", 1)[0]
    if href and not href.startswith(("http://", "https://", "mailto:")) and not (DECK / href).exists() and href != "deck_v14.pdf":
        issues.append(f"Broken local link: {href}")
for n in range(5, 12):
    text = slides[n - 1].get_text(" ", strip=True)
    if not any(term in text for term in ("발화", "설명", "입장문", "면담", "공론화", "수정안")):
        issues.append(f"Slide {n} lacks a message or dialogue reference")
if "D07_final_survey_clip.png" not in html or "D07_student_clip.png" in html:
    issues.append("Slide 10 must show the final online survey table, not the deliberative panel")

with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1600, "height": 900}, device_scale_factor=1)
    page.emulate_media(reduced_motion="reduce")
    page.on("pageerror", lambda error: issues.append(f"JavaScript error: {error}"))
    url = (DECK / "index.html").resolve().as_uri()
    page.goto(url, wait_until="load")
    page.evaluate("document.fonts.ready")
    if page.locator(".slide").count() != 15: issues.append("Browser slide count mismatch")
    for n in range(1, 16):
        page.goto(url + f"#{n}", wait_until="load")
        page.evaluate("document.fonts.ready")
        page.screenshot(path=str(QA / f"slide_{n:02d}.png"))
        result = page.evaluate("""n => {
          const slide=document.querySelectorAll('.slide')[n-1];
          const sr=slide.getBoundingClientRect();
          const nodes=[...slide.querySelectorAll('h1,h2,h3,p,blockquote,figure,img,.v14-body>div,.source-footer')];
          const bad=nodes.filter(x=>{const r=x.getBoundingClientRect(); return r.width && r.height && (r.left<sr.left-3 || r.right>sr.right+3 || r.top<sr.top-3 || r.bottom>sr.bottom+3)}).map(x=>x.tagName+'.'+x.className);
          const images=[...slide.querySelectorAll('img')].filter(x=>!x.complete||x.naturalWidth===0).map(x=>x.src);
          const body=slide.querySelector('.v14-body');
          return {bad,images,bodyBottom:body?.getBoundingClientRect().bottom,footerTop:slide.querySelector('.source-footer')?.getBoundingClientRect().top,scrollW:slide.scrollWidth,scrollH:slide.scrollHeight};
        }""", n)
        if result["bad"] or result["images"] or result["scrollW"] > 1602 or result["scrollH"] > 902:
            issues.append(f"Slide {n} visual boundary: {result}")
        if result["bodyBottom"] and result["footerTop"] and result["bodyBottom"] > result["footerTop"] - 10:
            issues.append(f"Slide {n} body overlaps footer")
    # FitStage: at 100% and at a smaller viewport, the visible slide must be centered.
    for width, height in ((1600, 900), (1920, 1080), (1366, 768)):
        page.set_viewport_size({"width": width, "height": height})
        page.wait_for_timeout(150)
        box = page.locator("#stage").bounding_box()
        if abs(box["x"] + box["width"] / 2 - width / 2) > 2 or abs(box["y"] + box["height"] / 2 - height / 2) > 2:
            issues.append(f"Stage off center at {width}x{height}: {box}")
    page.set_viewport_size({"width": 1600, "height": 900})
    page.goto(url, wait_until="load")
    page.pdf(path=str(PDF), width="1600px", height="900px", print_background=True, prefer_css_page_size=True, display_header_footer=False)
    page.keyboard.press("Home")
    page.keyboard.press("ArrowRight")
    if page.locator("#count").inner_text() != "2 / 15": issues.append("Keyboard navigation failed")
    browser.close()

thumbs = []
for n in range(1, 16):
    img = Image.open(QA / f"slide_{n:02d}.png").convert("RGB")
    thumb = ImageOps.fit(img, (400, 225))
    draw = ImageDraw.Draw(thumb)
    draw.rectangle((0, 0, 38, 24), fill=(24, 29, 26))
    draw.text((8, 4), f"{n:02d}", fill="white")
    thumbs.append(thumb)
sheet = Image.new("RGB", (1600, 900), "#ddd")
for i, thumb in enumerate(thumbs): sheet.paste(thumb, ((i % 4) * 400, (i // 4) * 225))
sheet.save(QA / "contact_sheet.png")

doc = pymupdf.open(PDF)
if len(doc) != 15: issues.append(f"Expected 15 PDF pages, got {len(doc)}")
for n, page in enumerate(doc, 1):
    if not page.get_text().strip(): issues.append(f"PDF page {n} lacks selectable text")
    if abs(page.rect.width / page.rect.height - 16 / 9) > .005: issues.append(f"PDF page {n} aspect ratio mismatch")

print(f"Slides rendered: 15 · PDF pages: {len(doc)} · source anchors: {len(targets)}")
print(f"Contact sheet: {QA / 'contact_sheet.png'}")
if issues:
    print("FAILURES:", *issues, sep="\n- ")
    sys.exit(1)
print("All v14 checks PASSED")
