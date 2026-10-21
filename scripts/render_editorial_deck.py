"""Render all editable HTML slides and optionally export their print PDF."""
from pathlib import Path
import argparse
from PIL import Image, ImageOps, ImageDraw
from playwright.sync_api import sync_playwright

DECK = Path(__file__).resolve().parents[1] / 'versions' / 'deck_v4'
QA = Path(__file__).resolve().parents[1] / 'qa' / 'deck_v4'
QA.mkdir(parents=True, exist_ok=True)

parser = argparse.ArgumentParser()
parser.add_argument('--pdf', action='store_true')
args = parser.parse_args()

with sync_playwright() as pw:
    browser = pw.chromium.launch(headless=True)
    page = browser.new_page(viewport={'width': 1600, 'height': 900}, device_scale_factor=1)
    page.emulate_media(reduced_motion='reduce')
    page.goto((DECK / 'index.html').as_uri(), wait_until='load')
    page.evaluate('document.fonts.ready')
    total = page.locator('.slide').count()
    failures = []
    for number in range(1, total + 1):
        page.evaluate('(n) => show(n-1)', number)
        page.wait_for_timeout(100)
        out = QA / f'slide_{number:02d}.png'
        page.locator('#stage').screenshot(path=str(out))
        result = page.evaluate('''() => {
          const slide = document.querySelector('.slide.active');
          const bad = [];
          for (const el of slide.querySelectorAll('h1,h2,h3,p,figcaption,.source-footer,.paper-slip,.headline-strip,.vote-block,.survey-major,.aftermath-card,.publics-grid,.conclusion-list')) {
            const r = el.getBoundingClientRect();
            const s = slide.getBoundingClientRect();
            const intended = el.closest('.cover-archive') || el.classList.contains('final-quote');
            if (!intended && (r.right > s.right + 2 || r.bottom > s.bottom + 2 || r.left < s.left - 2)) bad.push(el.tagName + '.' + el.className + ':' + Math.round(r.bottom-s.bottom));
            if (el.scrollWidth > el.clientWidth + 4 && el.clientWidth > 0) bad.push('horizontal text overflow:' + el.tagName + '.' + el.className);
          }
          const missing = [...slide.querySelectorAll('img')].filter(i=>!i.complete || i.naturalWidth===0).map(i=>i.getAttribute('src'));
          return {bad,missing};
        }''')
        if result['bad'] or result['missing']:
            failures.append((number, result))
    thumbs = []
    for number in range(1, total + 1):
        image = Image.open(QA / f'slide_{number:02d}.png').convert('RGB')
        thumb = ImageOps.fit(image, (400, 225))
        draw = ImageDraw.Draw(thumb)
        draw.rectangle((0, 0, 42, 25), fill=(25, 28, 26))
        draw.text((8, 5), f'{number:02d}', fill=(255, 255, 255))
        thumbs.append(thumb)
    sheet = Image.new('RGB', (1600, 900), '#ddd')
    for i, thumb in enumerate(thumbs):
        sheet.paste(thumb, ((i % 4) * 400, (i // 4) * 225))
    sheet.save(QA / 'contact_sheet.png')
    if args.pdf:
        page.pdf(path=str(DECK / 'deck_v4.pdf'), width='1600px', height='900px', print_background=True,
                 prefer_css_page_size=True, display_header_footer=False)
    browser.close()

print(f'Rendered {total} slides to', QA)
print('Layout checks:', failures if failures else 'no boundary or missing-image failures')
if args.pdf:
    print('PDF:', DECK / 'deck_v4.pdf')
