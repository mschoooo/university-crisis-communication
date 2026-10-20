"""Build a public citation page from the local, previously collected manifests.

Only publication metadata and original URLs are exported. Local paths, article
texts, hashes and private workspace information stay outside the public deck.
"""

import csv
from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parents[1] / "versions" / "v1" / "sources.html"
A_IDS = ["A01P", "A02P", "A04", "A07", "A10", "A14", "A15"]
D_IDS = ["D02", "D06", "D07", "D08", "D09", "D10", "D14", "D22"]


def load(path, id_field):
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return {row[id_field]: row for row in csv.DictReader(stream)}


a = load(ROOT / "데이터" / "sources.csv", "문서_ID")
d = load(ROOT / "데이터" / "동덕여대_sources.csv", "문서ID")


def row(item_id, row_data, title_field, date_field, url_field):
    title = escape(row_data[title_field])
    date = escape(row_data[date_field] or "날짜 미기재")
    publisher = escape(row_data["발행기관"])
    url = escape(row_data[url_field], quote=True)
    return f'<li id="{escape(item_id)}"><b>{escape(item_id)}</b> · {title} · {publisher} · {date}<br><a href="{url}" target="_blank" rel="noopener noreferrer">원문 열기</a></li>'


rows_a = "\n".join(row(item_id, a[item_id], "문서_제목", "발행일", "원문_URL") for item_id in A_IDS)
rows_d = "\n".join(row(item_id, d[item_id], "제목", "발행일", "URL") for item_id in D_IDS)

html = f'''<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>자료와 문헌 | 대학 위기 커뮤니케이션</title>
<style>body{{margin:0;background:#f7f5ef;color:#17313d;font:19px/1.7 "Noto Sans KR","Malgun Gothic",sans-serif}}main{{max-width:1000px;margin:0 auto;padding:65px 28px 100px}}h1{{font-size:46px;line-height:1.25}}h2{{margin-top:55px;border-top:1px solid #adb9b7;padding-top:25px}}li{{padding:18px 0;border-bottom:1px solid #d6dbd7}}a{{color:#0e7473;text-underline-offset:3px}}.back{{font-weight:700}}.note{{color:#536369}}</style></head>
<body><main><a class="back" href="index.html">← 발표로 돌아가기</a><h1>자료와 문헌</h1>
<p class="note">슬라이드의 자료 ID에서 이 페이지로 이동한다. 사건일과 발행일은 다를 수 있다. 기사에 실린 당사자 발언은 취재 인용이며 성명 원문과 구분한다. 이 페이지는 제목·발행기관·날짜·원문 링크만 싣는다.</p>
<h2>강원대 · 강릉원주대</h2><ul>{rows_a}</ul>
<h2>동덕여대</h2><ul>{rows_d}</ul>
<h2>이론과 수업자료</h2><ul>
<li id="P99"><b>P99</b> · Cancel, A. E., Mitrook, M. A., &amp; Cameron, G. T. (1999). “Testing the Contingency Theory of Accommodation in Public Relations.” <i>Public Relations Review, 25</i>(2), 171–197. <a href="https://doi.org/10.1016/S0363-8111(99)80161-1" target="_blank" rel="noopener noreferrer">DOI</a>. 개념 172–173쪽, 상황변수 184–189쪽.</li>
<li id="P01"><b>P01</b> · Cameron, G. T., Cropp, F., &amp; Reber, B. H. (2001). “Getting Past Platitudes: Factors Limiting Accommodation in Public Relations.” <i>Journal of Communication Management, 5</i>(3), 242–261. <a href="https://doi.org/10.1108/13632540110806802" target="_blank" rel="noopener noreferrer">DOI</a>.</li>
</ul><p class="note">자료 기준일 2026-10-21. 원자료·추출본은 발표자의 별도 연구 폴더에 보관한다.</p></main></body></html>'''
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(html, encoding="utf-8")
print(f"Created {OUT}")
