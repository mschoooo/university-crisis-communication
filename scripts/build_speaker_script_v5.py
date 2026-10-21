import sys
import re
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
deck = ROOT / "versions" / "deck_v5"
proposal_path = ROOT.parent / "발표_v5_내용개선안.md"

proposal_text = proposal_path.read_text(encoding="utf-8")

# Extract slides 01 to 15 from proposal
pattern = r'### (Slide \d+ [^\n]+)([\s\S]*?)(?=(?:### Slide \d+|## 3\.))'
matches = re.findall(pattern, proposal_text)

# Also load slides.js for speaker notes and Q&A
import json
slides_js = (deck / "slides.js").read_text(encoding="utf-8")

# Extract SPEAKER_NOTES array using regex
notes_match = re.search(r'const SPEAKER_NOTES = (\[[\s\S]*?\]);', slides_js)
speaker_notes = []
if notes_match:
    try:
        speaker_notes = json.loads(notes_match.group(1))
    except Exception as e:
        print("JSON parse error on SPEAKER_NOTES:", e)

# Also load ARCHIVE_DETAILS
archive_js = (deck / "archive_details.js").read_text(encoding="utf-8")
archive_match = re.search(r'window\.ARCHIVE_DETAILS = (\[[\s\S]*?\]);', archive_js)
archive_details = []
if archive_match:
    try:
        archive_details = json.loads(archive_match.group(1))
    except Exception as e:
        print("JSON parse error on ARCHIVE_DETAILS:", e)

md_lines = [
    "# 위기관리(029) 중간고사 대체 과제 · Editorial Archive 발표자 대본 (v5)",
    "",
    "발표자: 조민성 · 학번 202206251 (미디어커뮤니케이션학과)",
    "",
    "> **발표 개요**: 정황적 수용 이론(81개 변수·3분법)과 절차적 공정성(Leventhal; Tyler)을 접목한 대학 구조개혁 위기관리 심층 비교 연구 (16슬라이드, 15분 구성).",
    "",
    "---",
    ""
]

for idx in range(16):
    slide_num = idx + 1
    note = speaker_notes[idx] if idx < len(speaker_notes) else {}
    title = note.get("title", f"Slide {slide_num:02d}")
    script = note.get("script", "")
    qa = note.get("qa", "")
    archive = archive_details[idx] if idx < len(archive_details) else ""
    
    md_lines.append(f"## {slide_num:02d}. {title}")
    md_lines.append("")
    md_lines.append(f"**[발표자 스크립트]** (약 55~60초)")
    md_lines.append(f"> \"{script}\"")
    md_lines.append("")
    if qa:
        md_lines.append(f"**{qa}**")
        md_lines.append("")
    md_lines.append("### v5 화면 및 아카이브 상세 근거")
    md_lines.append("```text")
    md_lines.append(archive.strip())
    md_lines.append("```")
    md_lines.append("")
    md_lines.append("---")
    md_lines.append("")

out_file = deck / "speaker_script.md"
out_file.write_text("\n".join(md_lines), encoding="utf-8")
print(f"speaker_script.md written successfully to {out_file} ({len(md_lines)} lines).")
