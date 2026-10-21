"""Export public source metadata for the v3 deck from existing local manifests.

Includes all primary sources for Kangwon Univ (A01-A17) and Dongduk Women's Univ (D01-D27),
as well as all course readings (Weeks 2-7, 14) from Prof. Sungwook Hwang's Strategic Conflict Management course.
"""

import csv
from html import escape
from pathlib import Path


RESEARCH = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parents[1] / "versions" / "v3" / "sources.html"

A_IDS = [
    "A16", "A03", "A03P", "A01", "A01P", "A12", "A13", "A14",
    "A02", "A02P", "A04", "A15", "A06", "A07", "A11", "A08", "A10", "A09", "A17"
]
D_IDS = [
    "D01", "D26", "D02", "D03", "D04", "D05", "D06", "D07", "D08",
    "D09", "D12", "D18", "D10", "D11", "D19", "D21", "D13", "D25",
    "D15", "D14", "D22", "D23", "D20", "D16", "D17", "D27"
]
EVENT_DATES = {
    "A16": "2025-02-16 총장 합의 보도",
    "A03": "회의일 2025-02-28 (제46차 평의원회)",
    "A03P": "회의일 2025-02-28 (제46차 평의원회 회의록 원문)",
    "A01": "회의일 2025-04-01 (제47차 평의원회)",
    "A01P": "회의일 2025-04-01 (제47차 평의원회 회의록 원문, 8:12 부결)",
    "A02": "회의일 2025-04-28 (제48차 평의원회)",
    "A02P": "회의일 2025-04-28 (제48차 평의원회 회의록 원문, 15:6 가결)",
    "A04": "2025-04-28 가결 당일 대학 공식 설명 (2,150억 사업비·혁신전략실 24+11명)",
    "A06": "2025-05-09 작성·05-12 발행 정재연 총장 인터뷰",
    "A07": "2025-05-12 강대신문 직원협의회 반응 보도",
    "A08": "2025-06-13 통합 강원대 출범 확정·연차평가 A등급 보도",
    "A09": "2026-01-30 출범 직전 학사 재구조화·전부개정 학칙안 보도",
    "A17": "2026-03-03 통합 강원대 4개 캠퍼스 첫 입학식 보도",
    "D01": "2024-11-15 비상대책위원장 명의 학부모 서신",
    "D26": "2024-11-18 비전혁신추진단(9/27·11/5) 및 총학 소통 일지 공개",
    "D06": "2025-12-02 공론화위원회 최종 권고안 PDF",
    "D07": "2025-12-02 공론화 설문·숙의기구·타운홀 상세 통계 PDF",
    "D08": "2025-11-26(6차)·12-02(7차) 회의록 및 4차 회의 의결 규칙 수록 PDF",
    "D09": "2025-12-03 공론화위 권고안 수용 및 2029년 이행 총장 입장문",
    "D10": "2025-12-03~07 학생 총투표(3,470표 중 반대 2,975표) 결과 보도",
    "D11": "2025-12-09 총투표 결과와 고등교육법 비율에 관한 학교 반론 보도",
    "D14": "2026-01-12 대학평의원회 8:2 가결·학생위원 서명 거부·비밀유지 공문 보도(01-27)",
    "D15": "2026-01-13 학생회 학칙개정 반대 설문(87.5%) 및 입시 지원자 32.9% 감소 보도",
    "D22": "2026-02-26 개정 학칙 공포·시행 공고(02-27 게시)",
}


def load(path, id_field):
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return {item[id_field]: item for item in csv.DictReader(stream)}


a = load(RESEARCH / "데이터" / "sources.csv", "문서_ID")
d = load(RESEARCH / "데이터" / "동덕여대_sources.csv", "문서ID")


def row(source_id, item, title_field, date_field, url_field):
    detail = f" · <span class='ev'>{escape(EVENT_DATES[source_id])}</span>" if source_id in EVENT_DATES else ""
    return (
        f'<li id="{escape(source_id)}"><div class="id-badge">{escape(source_id)}</div>'
        f'<div class="src-body"><b>{escape(item[title_field])}</b> · {escape(item["발행기관"])} · '
        f'발행 {escape(item[date_field] or "날짜 미기재")}{detail}<br>'
        f'<a href="{escape(item[url_field], quote=True)}" target="_blank" '
        f'rel="noopener noreferrer">공개 원문 열기 ↗</a></div></li>'
    )


rows_a = "\n".join(row(k, a[k], "문서_제목", "발행일", "원문_URL") for k in A_IDS if k in a)
rows_d = "\n".join(row(k, d[k], "제목", "발행일", "URL") for k in D_IDS if k in d)

html = f'''<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>원자료 및 수업 이론 문헌 검증 인덱스 | 발표 v3</title>
<style>
  :root {{ --bg:#f7f5ef; --ink:#132934; --teal:#136f6d; --red:#b8443e; --muted:#5a6b73; --line:#d5d1c8; --card:#efeae0; }}
  body {{ margin:0; background:var(--bg); color:var(--ink); font:17px/1.68 "Noto Sans KR","Malgun Gothic",sans-serif; }}
  main {{ max-width:1080px; margin:0 auto; padding:56px 28px 96px; }}
  .top-bar {{ display:flex; justify-content:space-between; align-items:center; border-bottom:2px solid var(--ink); padding-bottom:18px; margin-bottom:28px; }}
  .back {{ font-weight:700; color:var(--teal); text-decoration:none; font-size:18px; }}
  h1 {{ font-size:38px; line-height:1.22; margin:0 0 12px; letter-spacing:-0.02em; }}
  h2 {{ margin-top:48px; border-top:2px solid var(--ink); padding-top:20px; font-size:24px; color:var(--ink); }}
  p.note {{ color:var(--muted); margin:8px 0 24px; font-size:16px; background:var(--card); padding:14px 18px; border-left:4px solid var(--teal); }}
  ul {{ list-style:none; padding:0; margin:0; }}
  li {{ display:flex; gap:16px; align-items:flex-start; padding:14px 0; border-bottom:1px solid var(--line); }}
  .id-badge {{ min-width:58px; text-align:center; font-weight:800; font-size:14px; background:var(--ink); color:#fff; padding:4px 8px; border-radius:4px; margin-top:3px; }}
  .src-body {{ flex:1; }}
  .ev {{ color:var(--red); font-weight:700; }}
  a {{ color:var(--teal); text-underline-offset:3px; font-weight:600; }}
</style></head>
<body><main>
<div class="top-bar">
  <a class="back" href="index.html">← 발표 슬라이드(v3)로 돌아가기</a>
  <span>전략적 갈등관리 · 조민성 (부산대학교 미디어커뮤니케이션학과)</span>
</div>
<h1>원자료 및 수업 이론 문헌 검증 인덱스 (v3)</h1>
<p class="note">
  <b>사료 비판 원칙:</b> ① 사건 발생일(회의일·표결일)과 문서 게시일(보도일·공고일)을 엄격히 구분한다. ② 대학 공식 회의록·설문 통계 원문(1차 자료)과 언론 취재 보도(2차 인용)의 증거 위계를 구분한다. ③ 슬라이드 내 모든 출처 배지(예: <code>A01P</code>, <code>D07</code>, <code>P99</code>)는 본 페이지의 고유 앵커와 1:1로 연결된다.
</p>

<h2>1. 전략적 갈등관리 수업 핵심 이론 문헌 (Weeks 2–7, 14)</h2>
<ul>
  <li id="P99"><div class="id-badge">P99</div><div class="src-body"><b>Cancel, A. E., Mitrook, M. A., &amp; Cameron, G. T. (1999).</b> “Testing the Contingency Theory of Accommodation in Public Relations.” <i>Public Relations Review, 25</i>(2), 171–197. <a href="https://doi.org/10.1016/S0363-8111(99)80161-1" target="_blank">DOI ↗</a> · <span class="ev">4주차 수업 문헌</span> (순수 옹호 1 ↔ 순수 수용 7 연속선, 사전성향적 변인[조직 문화·리더십·구조]과 상황적 변인[외적 위협·긴급성·공중의 상대적 권력·잠재적 비용]의 상호작용 검증, pp. 172–176, 184–189).</div></li>
  <li id="P01"><div class="id-badge">P01</div><div class="src-body"><b>Cameron, G. T., Cropp, F., &amp; Reber, B. H. (2001).</b> “Getting Past Platitudes: Factors Limiting Accommodation in Public Relations.” <i>Journal of Communication Management, 5</i>(3), 242–261. <a href="https://doi.org/10.1108/13632540110806802" target="_blank">DOI ↗</a> · <span class="ev">4주차 수업 문헌</span> (수용을 제약하는 6대 요인: 도덕적 확신·정체성, 상충하는 복수 공중의 요구[Multiple Publics], 법적·규제적 제약, 최고경영진의 입장과 관할권 등, pp. 245–253).</div></li>
  <li id="H14"><div class="id-badge">H14</div><div class="src-body"><b>황성욱 (2014).</b> 「정황적 수용 이론: 과거, 현재, 그리고 미래에 대한 전망」. <i>홍보학연구, 18</i>(1), 248–280. · <span class="ev">14주차 수업 문헌 (교수님 저술)</span> (정황적 수용 이론의 종합 고찰: 사전성향적 변인과 상황적 변인의 구분, 갈등 포지셔닝, 그리고 Jin &amp; Cameron(2006)의 <b>행동적 수용[action-based accommodation]</b> 대 <b>수사 혼합적 수용[qualified-rhetoric-mixed accommodation]</b> 척도 구분).</div></li>
  <li id="W05"><div class="id-badge">W05</div><div class="src-body"><b>Wilcox, D. L., &amp; Cameron, G. T. (2005).</b> “Conflict Management: Dealing with Issues, Risks, and Crises.” In <i>Public Relations: Strategies and Tactics</i> (8th ed., Chap. 10). Pearson. · <span class="ev">2주차 수업 문헌</span> (전략적 갈등관리 생애주기 4단계: <b>사전대응적[Proactive] → 전략적[Strategic] → 반응적[Reactive] → 회복[Recovery]</b> 단계).</div></li>
  <li id="H11"><div class="id-badge">H11</div><div class="src-body"><b>Ham, C.-D., Hwang, S., &amp; Cameron, G. T. (2011).</b> “Contingency Crisis Management in South Korea: Preparation and Rebound Strategy.” · <span class="ev">3주차 수업 문헌</span> (갈등관리 생애주기에서의 사전 대비와 사후 회복 전략의 연속적 작동).</div></li>
  <li id="H97"><div class="id-badge">H97</div><div class="src-body"><b>Heath, R. L. (1997).</b> <i>Strategic Issues Management: Organizations and Public Policy Challenges</i>. Sage. · <span class="ev">3주차 수업 문헌</span> (이슈 스캐닝과 지형 정찰[scouting the terrain], 쟁점의 <b>영향력[impact] × 발생 가능성[probability]</b> 우선순위 매트릭스).</div></li>
  <li id="S94"><div class="id-badge">S94</div><div class="src-body"><b>Sturges, D. L. (1994).</b> “Communicating through Crisis: A Strategy for Organizational Survival.” <i>Management Communication Quarterly, 7</i>(3), 297–316. <a href="https://doi.org/10.1177/0893318994007003004" target="_blank">DOI ↗</a> · <span class="ev">5주차 수업 문헌</span> (위기 생애주기[전조–돌발–만성–해결]와 <b>공중 의견 고착화[opinion solidification] 시점</b>: 의견이 사회적 규범으로 굳어진 뒤에는 사후 정보 제공으로 태도를 역전시키기 어렵다는 이론).</div></li>
  <li id="M04"><div class="id-badge">M04</div><div class="src-body"><b>Marra, F. J. (2004).</b> “Crisis Communication Plans: Poor Predictors of Excellent Crisis Public Relations.” · <span class="ev">5주차 수업 문헌</span> (문서화된 절차나 형식적 위원회보다 조직의 <b>위기 커뮤니케이션 문화[투명성·소통 의지]와 PR 기능의 자율성</b>이 실제 위기 대응 성과를 좌우함).</div></li>
  <li id="H22"><div class="id-badge">H22</div><div class="src-body"><b>Hwang, S., Cho, S., &amp; Lee, S. (2022).</b> “Crisis Preparedness of Organizations: Perceived Importance and Actual Execution.” · <span class="ev">6주차 수업 문헌 (교수님 저술)</span> (위기대비태세 구성요소 중 상시 쟁점관리와 조직 내부 정보 공유·임파워먼트의 중요도–실행도 격차 규명).</div></li>
</ul>

<h2>2. 사례 A · 강원대–강릉원주대 통합 관련 1차 원자료 및 보도</h2>
<ul>{rows_a}</ul>

<h2>3. 사례 B · 동덕여대 공학 전환 관련 1차 원자료 및 보도</h2>
<ul>{rows_d}</ul>

<h2>4. 고등교육 배경·보조 문헌</h2>
<ul>
  <li id="R1"><div class="id-badge">R1</div><div class="src-body"><b>김택형 (2025).</b> 「대학 통폐합 연구의 필요성과 미래 방향」. 한국교육행정학회 뉴스레터 제162호(10월호) 시론. <a href="https://keas1967.com/board/news/article/268628" target="_blank">학회 원문 ↗</a> (통합 이후 구성원 갈등·거버넌스 연구의 필요성 제기).</div></li>
  <li id="R2"><div class="id-badge">R2</div><div class="src-body"><b>김동우·김희주·김태성 (2025).</b> 「대학통합을 겪은 행정직원의 경험에 대한 현상학적 연구」. <i>고등교육, 8</i>(2), 131–159. <a href="https://doi.org/10.22838/jher.2025.8.2.131" target="_blank">DOI ↗</a> (대학 통합 시 행정직원이 겪는 직무 재편·순환근무 불안과 의사결정 소외 메커니즘).</div></li>
  <li id="R4"><div class="id-badge">R4</div><div class="src-body"><b>Główczewski, M., &amp; Burdziej, S. (2023).</b> “(In)justice in academia: Procedural fairness, students’ academic identification, and perceived legitimacy of university authorities.” <i>Higher Education, 86</i>, 163–184. <a href="https://doi.org/10.1007/s10734-022-00907-8" target="_blank">DOI ↗</a> (대학 당국의 절차적 공정성 인식이 학생의 정당성 수용에 미치는 영향).</div></li>
  <li id="R5"><div class="id-badge">R5</div><div class="src-body"><b>Jaques, T. (2007).</b> “Issue management and crisis management: An integrated, non-linear, relational construct.” <i>Public Relations Review, 33</i>(2), 147–157. <a href="https://doi.org/10.1016/j.pubrev.2007.02.001" target="_blank">DOI ↗</a> (이슈관리와 위기관리의 비선형적 연계 모형).</div></li>
</ul>
</main></body></html>'''

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(html, encoding="utf-8")
print(f"Created {OUT}")
