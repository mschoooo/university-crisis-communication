"""Render cited document facsimiles and fetch reusable campus record photos."""
from pathlib import Path
from urllib.parse import quote
import requests
import pymupdf

DECK = Path(__file__).resolve().parents[1] / 'versions' / 'deck_v4'
ASSETS = DECK / 'assets'
SOURCE = Path(__file__).resolve().parents[2] / '원문'
ASSETS.mkdir(parents=True, exist_ok=True)

# Every clipping below is an unaltered rectangular excerpt of the cited page.
clips = {
    'A01_title_clip': (SOURCE / 'A01_attachment.pdf', 1, (35, 15, 560, 250)),
    'A01_vote_clip': (SOURCE / 'A01_attachment.pdf', 40, (42, 515, 555, 650)),
    'A02_staff_clip': (SOURCE / 'A02_attachment.pdf', 7, (43, 125, 550, 280)),
    'D06_title_clip': (SOURCE / '동덕여대/D06.pdf', 1, (58, 38, 550, 260)),
    'D06_recommendation_clip': (SOURCE / '동덕여대/D06.pdf', 2, (53, 32, 555, 308)),
    'D07_student_clip': (SOURCE / '동덕여대/D07.pdf', 3, (32, 42, 803, 191)),
    'D08_rule_clip': (SOURCE / '동덕여대/D08.pdf', 19, (72, 106, 555, 320)),
}
for name, (source, number, bounds) in clips.items():
    doc = pymupdf.open(source)
    page = doc[number - 1]
    out = ASSETS / f'{name}.png'
    page.get_pixmap(matrix=pymupdf.Matrix(2.2, 2.2), clip=pymupdf.Rect(bounds), alpha=False).save(out)
    print(out.name, out.stat().st_size)

photos = {
    'campus_kangwon.jpg': '강원대학교 60주년 기념관.jpg',
    'campus_gangneung.jpg': '국립강릉원주대학교1.jpg',
}
session = requests.Session()
session.headers.update({'User-Agent': 'Mozilla/5.0 (academic research slide attribution)'})
for out_name, file_name in photos.items():
    url = 'https://commons.wikimedia.org/wiki/Special:Redirect/file/' + quote(file_name) + '?width=1280'
    response = session.get(url, timeout=40)
    response.raise_for_status()
    if not response.headers.get('content-type', '').startswith('image/'):
        raise RuntimeError(f'Unexpected response for {file_name}: {response.headers.get("content-type")}')
    out = ASSETS / out_name
    out.write_bytes(response.content)
    print(out.name, out.stat().st_size, response.url)

# Drop earlier full-page previews and unused clips from the distributable deck.
for stale in [
    'A01_p01.png', 'A01_p40.png', 'A02_p01.png', 'A02_p07.png', 'A02_p09.png',
    'A02_p44.png', 'D06_p01.png', 'D06_p02.png', 'D07_p01.png', 'D07_p03.png',
    'D07_p04.png', 'D07_p17.png', 'D08_p19.png', 'A02_vote_clip.png',
    'D07_survey_clip.png', 'D07_accept_clip.png',
]:
    (ASSETS / stale).unlink(missing_ok=True)
