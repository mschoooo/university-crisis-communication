"""Render every final PDF page for visual review and check basic print integrity."""
from pathlib import Path
from PIL import Image, ImageOps, ImageDraw
import pymupdf

ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / 'versions' / 'deck_v4' / 'deck_v4.pdf'
QA = ROOT / 'qa' / 'deck_v4'
doc = pymupdf.open(PDF)
assert len(doc) == 15, f'Expected 15 pages, got {len(doc)}'
thumbs = []
for number, page in enumerate(doc, start=1):
    assert abs(page.rect.width / page.rect.height - 16/9) < .01, page.rect
    text = page.get_text()
    assert len(text.strip()) > 40, f'Page {number} appears blank'
    out = QA / f'pdf_page_{number:02d}.png'
    page.get_pixmap(matrix=pymupdf.Matrix(1.5, 1.5), alpha=False).save(out)
    image = Image.open(out).convert('RGB')
    thumb = ImageOps.fit(image, (400, 225))
    draw = ImageDraw.Draw(thumb)
    draw.rectangle((0, 0, 42, 25), fill=(25, 28, 26))
    draw.text((8, 5), f'{number:02d}', fill=(255, 255, 255))
    thumbs.append(thumb)
sheet = Image.new('RGB', (1600, 900), '#ddd')
for i, thumb in enumerate(thumbs):
    sheet.paste(thumb, ((i % 4) * 400, (i // 4) * 225))
sheet.save(QA / 'pdf_contact_sheet.png')
print('PDF pages:', len(doc), 'size:', PDF.stat().st_size, 'bytes')
print('Rendered:', QA / 'pdf_contact_sheet.png')
