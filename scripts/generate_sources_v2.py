"""Export public source metadata for the v2 deck from existing local manifests.

Only titles, publishers, publication dates, event-date notes and original URLs go
to GitHub Pages. Full local source documents and private workspace paths remain
in the research folder.
"""

import csv
from html import escape
from pathlib import Path


RESEARCH = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parents[1] / "versions" / "v2" / "sources.html"
A_IDS = ["A16", "A03P", "A01P", "A14", "A02P", "A04", "A07", "A15", "A10"]
D_IDS = ["D01", "D02", "D03", "D04", "D05", "D06", "D07", "D08", "D09", "D10", "D11", "D14", "D22", "D25", "D27"]
EVENT_DATES = {
    "A03P": "회의일 2025-02-28",
    "A01P": "회의일 2025-04-01",
    "A02P": "회의일 2025-04-28",
    "D08": "2025-11-26·12-02 회의 수록",
    "D14": "2026-01-12 회의에 대한 01-27 보도",
    "D22": "02-26 개정 학칙 시행 공고",
}


def load(path, id_field):
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return {item[id_field]: item for item in csv.DictReader(stream)}


a = load(RESEARCH / "데이터" / "sources.csv", "문서_ID")
d = load(RESEARCH / "데이터" / "동덕여대_sources.csv", "문서ID")


def row(source_id, item, title_field, date_field, url_field):
    detail = f" · {EVENT_DATES[source_id]}" if source_id in EVENT_DATES else ""
    return (
        f'<li id="{escape(source_id)}"><b>{escape(source_id)}</b> · '
        f'{escape(item[title_field])} · {escape(item["발행기관"])} · '
        f'발행 {escape(item[date_field] or "날짜 미기재")}{escape(detail)}<br>'
        f'<a href="{escape(item[url_field], quote=True)}" target="_blank" '
        f'rel="noopener noreferrer">원문 열기</a></li>'
    )


rows_a = "\n".join(row(k, a[k], "문서_제목", "발행일", "원문_URL") for k in A_IDS)
rows_d = "\n".join(row(k, d[k], "제목", "발행일", "URL") for k in D_IDS)

html = f'''<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>자료와 문헌 | 발표 v2</title>
<style>body{{margin:0;background:#f7f5ef;color:#17313d;font:19px/1.7 "Noto Sans KR","Malgun Gothic",sans-serif}}main{{max-width:1000px;margin:0 auto;padding:65px 28px 100px}}h1{{font-size:46px;line-height:1.25}}h2{{margin-top:55px;border-top:1px solid #adb9b7;padding-top:25px}}li{{padding:18px 0;border-bottom:1px solid #d6dbd7}}a{{color:#0e7473;text-underline-offset:3px}}.back{{font-weight:700}}.note{{color:#536369}}</style></head>
<body><main><a class="back" href="index.html">← 발표로 돌아가기</a><h1>자료와 문헌 · v2</h1>
<p class="note">사건일과 자료 발행일을 구별한다. 기사 속 발언은 취재 인용이며 원문 성명과 구별한다. 이 페이지에는 서지 정보와 공개 원문 주소만 싣는다.</p>
<h2>강원대 · 강릉원주대</h2><ul>{rows_a}</ul>
<h2>동덕여대</h2><ul>{rows_d}</ul>
<h2>주 이론과 수업 논문</h2><ul>
<li id="P99"><b>P99</b> · Cancel, A. E., Mitrook, M. A., &amp; Cameron, G. T. (1999). “Testing the Contingency Theory of Accommodation in Public Relations.” <i>Public Relations Review, 25</i>(2), 171–197. <a href="https://doi.org/10.1016/S0363-8111(99)80161-1">DOI</a>. 본 발표: 172–173·184–189쪽. 수업 원문 PDF에서 확인.</li>
<li id="P01"><b>P01</b> · Cameron, G. T., Cropp, F., &amp; Reber, B. H. (2001). “Getting Past Platitudes: Factors Limiting Accommodation in Public Relations.” <i>Journal of Communication Management, 5</i>(3), 242–261. <a href="https://doi.org/10.1108/13632540110806802">DOI</a>. 본 발표: 246·251쪽. 수업 원문 PDF에서 확인.</li>
</ul>
<h2>연구 배경·보조 문헌</h2><ul>
<li id="R1"><b>R1</b> · 김택형(2025). 「대학 통폐합 연구의 필요성과 미래 방향」. 한국교육행정학회 뉴스레터 제162호(10월호) 시론. <a href="https://keas1967.com/board/news/article/268628">학회 게시 원문</a> (게시 2025-11-14). 학술지 실증논문은 아님.</li>
<li id="R2"><b>R2</b> · 김동우·김희주·김태성(2025). 「대학통합을 겪은 행정직원의 경험에 대한 현상학적 연구」. <i>고등교육, 8</i>(2), 131–159. <a href="https://doi.org/10.22838/jher.2025.8.2.131">DOI</a>. 로컬 원문 131·141–142·150·152쪽 확인. 강원대 직접 연구는 아님.</li>
<li id="R4"><b>R4</b> · Główczewski, M., &amp; Burdziej, S. (2023). “(In)justice in academia: Procedural fairness, students’ academic identification, and perceived legitimacy of university authorities.” <i>Higher Education, 86</i>, 163–184. <a href="https://doi.org/10.1007/s10734-022-00907-8">DOI</a>. 공개 원문 PDF 1·8·16·18쪽 확인. 동덕여대 직접 연구는 아님.</li>
<li id="R5"><b>R5</b> · Jaques, T. (2007). “Issue management and crisis management: An integrated, non-linear, relational construct.” <i>Public Relations Review, 33</i>(2), 147–157. <a href="https://doi.org/10.1016/j.pubrev.2007.02.001">DOI</a>. 본 발표: 150–153쪽.</li>
</ul><p class="note">자료 기준일 2026-10-21. 각 사건의 원자료·추출본과 문헌 PDF는 발표자의 로컬 연구 폴더에 보관한다. 발표의 세 평가 기준과 사전 대응 제안은 발표자의 분석이다.</p></main></body></html>'''
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(html, encoding="utf-8")
print(f"Created {OUT}")
