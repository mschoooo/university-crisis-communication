# -*- coding: utf-8 -*-
"""Verify v18 content, links, viewport centering, rendered slides and PDF."""
from pathlib import Path
import re
import sys
from bs4 import BeautifulSoup
from PIL import Image, ImageOps, ImageDraw
import pymupdf
from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
DECK = ROOT / "versions" / "deck_v18"
QA = ROOT / "qa" / "deck_v18"
QA.mkdir(parents=True, exist_ok=True)
PDF = DECK / "deck_v18.pdf"
issues = []
html = (DECK / "index.html").read_text(encoding="utf-8")
source_html = (DECK / "sources.html").read_text(encoding="utf-8")
soup = BeautifulSoup(html, "html.parser")
slides = soup.select("section.slide")
if len(slides) != 15: issues.append(f"Expected 15 slides, got {len(slides)}")
if len(slides[0].select('.v17-cover-right img')) != 2: issues.append("Cover must show both field photographs")
if not slides[1].select_one('.v17-dual-timeline'): issues.append("Slide 2 lacks the two-case timeline")
if not slides[2].select_one('.v17-rq'): issues.append("Slide 3 lacks the research question layout")
if 'v17-closing' not in slides[13].get('class', []): issues.append("Slide 14 is not the navy conclusion")
if "카메룬" in html or "전수 적용" in html: issues.append("Uncorrected theory name or unsupported blanket application claim")
if "사의 보류" in html: issues.append("Typo remains")
if "조정 가능한 범위가 대응을 갈랐다" in html: issues.append("Causal slide 12 headline remains")
if slides[14].find("h2"): issues.append("References slide retains a large title")
requirements = {
    1: ['변화의 결단은', '강원대–강릉원주대', '동덕여대'],
    2: ['강원대–강릉원주대', '동덕여대', '심의 보류', '잠정 중단'],
    3: ['발화', '행동', '반응', '신뢰 회복'],
    4: ['외부 변수', '내부 변수', 'E24', 'E21', 'I56'],
    5: ['사과', '심의 보류', '카메론'],
    6: ['8', '12', 'E24'],
    7: ['24명', '11명', 'E21'],
    8: ['제한적 부인', 'I56', '측정되지'],
    9: ['잠정 중단', 'E24'],
    10: ['51.8%', '71.3%', 'E24'],
    11: ['85.7%', '2029', '2026.1.12', 'D14', 'D22'],
    12: ['무엇을 조정하고', 'D14', 'D22', '공식 절차'],
    13: ['효과적이었던 대응', '미흡했던 대응', '확인되지 않은 성과', '2.26', '3.1', '신뢰'],
    14: ['강원대', '동덕여대', '공통', '요구 반영 결과'],
    15: ['Heath', 'Leventhal', 'D14', 'D22'],
}
for n, terms in requirements.items():
    text = slides[n - 1].get_text(" ", strip=True)
    for term in terms:
        if term not in text: issues.append(f"Slide {n} lacks {term}")
for i, (button, slide) in enumerate(zip(soup.select(".toc-item"), slides), 1):
    title = slide.find(["h1", "h2"]).get_text(" ", strip=True) if slide.find(["h1", "h2"]) else "참고문헌 · 출처"
    if title not in button.get_text(" ", strip=True): issues.append(f"TOC mismatch on slide {i}")
available = set(re.findall(r'id="([A-Z][A-Z0-9]*)"', source_html))
targets = set(re.findall(r'href="sources\.html#([A-Z][A-Z0-9]*)"', html))
if targets - available: issues.append(f"Missing source anchors: {targets-available}")
for a in soup.select("a[href]"):
    href = a["href"].split("#", 1)[0]
    if href and not href.startswith(("http://", "https://", "mailto:")) and not (DECK / href).exists() and href != "deck_v18.pdf":
        issues.append(f"Broken local link: {href}")
for n in range(5, 12):
    text = slides[n - 1].get_text(" ", strip=True)
    if not any(term in text for term in ("발화", "설명", "입장문", "면담", "공론화", "수정안")):
        issues.append(f"Slide {n} lacks a message or dialogue reference")
if "D07_final_survey_clip.png" not in html or "D07_student_clip.png" in html:
    issues.append("Slide 10 must show the final online survey table, not the deliberative panel")

if '2.26 개정 학칙 시행' in html or '2.26 개정 학칙 시행' in source_html: issues.append('Incorrect 2.26 effective date remains')
if '집단별 가중치가 달라' in html: issues.append('Incorrect weighting description remains')
source_d23 = list(ROOT.parent.parent.rglob('D23.txt'))
if not source_d23 or '2026년 3월 1일부터 시행' not in source_d23[0].read_text(encoding='utf-8'):
    issues.append('D23 effective date cannot be verified')
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
          const nodes=[...slide.querySelectorAll('h1,h2,h3,p,blockquote,figure,img,.v18-body>div,.source-footer')];
          const bad=nodes.filter(x=>{const r=x.getBoundingClientRect(); return r.width && r.height && (r.left<sr.left-3 || r.right>sr.right+3 || r.top<sr.top-3 || r.bottom>sr.bottom+3)}).map(x=>x.tagName+'.'+x.className);
          const images=[...slide.querySelectorAll('img')].filter(x=>!x.complete||x.naturalWidth===0).map(x=>x.src);
          const body=slide.querySelector('.v15-body');
          return {bad,images,bodyBottom:body?.getBoundingClientRect().bottom,footerTop:slide.querySelector('.source-footer')?.getBoundingClientRect().top,scrollW:slide.scrollWidth,scrollH:slide.scrollHeight,bg:getComputedStyle(slide).backgroundColor};
        }""", n)
        if result["bad"] or result["images"] or result["scrollW"] > 1602 or result["scrollH"] > 902:
            issues.append(f"Slide {n} visual boundary: {result}")
        if result["bg"] != ("rgb(23, 44, 70)" if n == 14 else "rgb(255, 255, 255)"): issues.append(f"Slide {n} background is {result['bg']}")
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
print("All v18 checks PASSED")




