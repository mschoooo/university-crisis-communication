"""Carry corrected v4 speaker notes and on-screen evidence into the redesign."""
from pathlib import Path
import json
import re
from bs4 import BeautifulSoup

DECK_ROOT = Path(__file__).resolve().parents[1]
SOURCE = DECK_ROOT / 'versions' / 'v4'
DEST = DECK_ROOT / 'versions' / 'deck_v4'

html = BeautifulSoup((SOURCE / 'index.html').read_text(encoding='utf-8'), 'html.parser')
details = []
for slide in html.select('section.slide[data-slide]'):
    for tag in slide.select('footer, .topline'):
        tag.decompose()
    text = slide.get_text(' ', strip=True)
    details.append(' '.join(text.split()))
assert len(details) == 14
(DEST / 'archive_details.js').write_text(
    'window.ARCHIVE_DETAILS = ' + json.dumps(details, ensure_ascii=False, indent=2) + ';\n',
    encoding='utf-8',
)

js = (SOURCE / 'slides.js').read_text(encoding='utf-8')
js = js.replace('  if (notesQa) notesQa.textContent = item.qa;',
                '  if (notesQa) notesQa.textContent = item.qa;\n'
                '  const detail = document.getElementById("notes-detail");\n'
                '  if (detail) detail.textContent = (window.ARCHIVE_DETAILS || [])[index] || "";')
(DEST / 'slides.js').write_text(js, encoding='utf-8')

notes_block = (SOURCE / 'slides.js').read_text(encoding='utf-8').split('const SPEAKER_NOTES = [', 1)[1].split('];', 1)[0]
fields = re.findall(r'title: ("(?:\\.|[^"\\])*")\s*,\s*script: ("(?:\\.|[^"\\])*")\s*,\s*qa: ("(?:\\.|[^"\\])*")', notes_block)
assert len(fields) == 14, len(fields)
out = ['# Editorial Archive 발표자 대본', '', '수정 사실관계는 `versions/v4`를 기준으로 보존했다. 화면에서 축약한 세부 논증은 각 슬라이드의 노트에도 포함된다.', '']
for i, triple in enumerate(fields, start=1):
    title, script, qa = (json.loads(x) for x in triple)
    out.extend([f'## {i:02d}. {title}', '', script, '', qa, '', '### v4 화면의 상세 근거', '', details[i-1], ''])
(DEST / 'speaker_script.md').write_text('\n'.join(out), encoding='utf-8')

sources = (SOURCE / 'sources.html').read_text(encoding='utf-8')
sources = sources.replace('versions/v4', 'versions/deck_v4').replace('deck_v4.pdf', 'deck_v4.pdf')
(DEST / 'sources.html').write_text(sources, encoding='utf-8')
print('notes:', len(fields), 'slides; source anchors:', sources.count(' id="'))
