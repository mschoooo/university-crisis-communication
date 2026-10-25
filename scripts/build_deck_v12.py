"""Build the reviewed v12 HTML, notes and styles from the preserved v11 deck."""
from pathlib import Path
import json
import re
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "versions" / "deck_v11"
TARGET = ROOT / "versions" / "deck_v12"
soup = BeautifulSoup((SOURCE / "index.html").read_text(encoding="utf-8"), "html.parser")
slides = soup.select("section.slide")
assert len(slides) == 15

def set_inner(index, markup):
    node = slides[index - 1]
    node.clear()
    fragment = BeautifulSoup(markup, "html.parser")
    for child in list(fragment.contents):
        node.append(child)

set_inner(3, '''
<header class="folio"><span>02 / CONTINGENCY THEORY</span><span>CAMERON · STUDY DESIGN</span></header>
<p class="deck-kicker">분석 틀과 적용 범위</p>
<h2>81개 변수에서 세 갈등 조건으로</h2>
<div class="v12-theory-intro"><b>교재의 변수 목록</b><span>외부 24개 · 내부 57개</span><p>모든 항목을 두 사례에서 평가했다. 본 발표에서는 입장 이동에 직접 연결된 조건을 중심으로 설명한다.</p></div>
<div class="v12-three-axis">
 <article><span>01</span><h3>공중의 힘</h3><p>평의원회의 부결권과 학생의 동원력은 서로 다른 방식으로 본부를 압박했다.</p><small>교재: 공중의 상대적인 힘 · E24</small></article>
 <article><span>02</span><h3>요구의 조정 범위</h3><p>인력 구성은 바뀌었고, 여대 유지 요구는 시행 시점 조정으로 충족되지 않았다.</p><small>교재: 공중의 양보할 수 있는 수준 · E21<br>‘조정 가능성’은 연구자의 관찰 지표</small></article>
 <article><span>03</span><h3>기존 신뢰</h3><p>선제출·사전 설명·집계 규칙 논란이 절차에 대한 판단에 영향을 주었다.</p><small>교재: 공중과 조직 사이의 신뢰감 · I56</small></article>
</div>
<div class="v12-theory-caveat"><b>적용 한계</b><span>이 목록은 기업과 외부 공중을 전제로 한다. 대학의 학생·직원은 내부 구성원이며, 평의원회의 공식 심의권과 여론을 통한 압력을 구분한다.</span></div>
<footer class="source-footer"><span>『PR커뮤니케이션』 제2장 표 2-5, 80–82쪽 · Cancel et al. (1997, 1999) · Cameron et al. (2001)</span><span>03 / 15</span></footer>''')

set_inner(9, '''
<header class="folio"><span>05 / CASE B · DONGDUK (2)</span><span>ONE QUESTION · TWO WEIGHTING RULES</span></header>
<p class="deck-kicker brick-text">동덕여대 2025년 최종 온라인 조사</p>
<h2>같은 응답, 다른 집계 규칙</h2>
<div class="v12-question"><b>질문 조건</b><span>현재 재학생이 모두 졸업한 뒤인 <strong>2029~2030년 예상 시점</strong>에 공학으로 전환할지 물었다.</span><small>교원 163명 · 학생 2,889명 · 직원 124명, 총 3,176명 (D07 4쪽)</small></div>
<div class="v12-weight-grid">
 <article><span>집단별 동일 가중</span><strong>51.8%</strong><b>공학 전환</b><p>교원·학생·직원 집단의 응답 비율을 각각 같은 비중으로 합산한 공론화 발표 수치다.</p></article>
 <article><span>인원수 단순합산</span><strong>66.1%</strong><b>여대 유지</b><p>응답자 수를 기준으로 다시 합산한 연구자 계산이다. 학생 응답자의 71.3%는 여대 유지를 택했다.</p></article>
</div>
<div class="v12-weight-note"><b>해석</b><span>어느 집계 규칙을 쓰는지가 결론을 바꾼다. 집단별 동일 가중의 정당성에 대한 이견은 남았으며, 두 비율을 전체 응답자의 단순 찬반으로 말할 수 없다.</span></div>
<footer class="source-footer"><span>D07 최종 온라인 조사 4쪽 · D06 권고안 · 단순합산은 D07 공개 수치를 이용한 재계산</span><span>09 / 15</span></footer>''')

set_inner(10, '''
<header class="folio"><span>06 / AFTERMATH</span><span>DECISION · RESPONSE · TIME</span></header>
<p class="deck-kicker">공식 절차와 반대 공중의 반응</p>
<h2>결정 이후에도 남은 반대</h2>
<div class="v12-after-grid">
 <article><h3>강원대</h3>
  <div><time>2025.04.28</time><p>제48차 평의원회 <b>15:6 가결</b>. 같은 날 직원협의회는 안의 내용에 이의를 제기했다. <small>A02P·A07</small></p></div>
  <div><time>2025.05.28</time><p>교육부의 양교 통합 승인. <small>A10·A11</small></p></div>
  <div><time>2026.02.26~27</time><p>네 캠퍼스에서 신입생 입학식 개최. <small>A17</small></p></div>
  <div><time>2026.03.01</time><p>통합 강원대학교 출범. <small>A10·A17</small></p></div>
 </article>
 <article><h3>동덕여대</h3>
  <div><time>2025.12.02~03</time><p>공론화위 <b>9:2:1 권고</b> 뒤 총장이 2029년 전환 추진을 발표했다. 시점 조건은 발표 전 설문에도 있었다. <small>D06·D07·D09</small></p></div>
  <div><time>2025.12.09</time><p>총학생회가 총투표 <b>85.7% 반대</b> 결과를 발표했다. 투표 종료일은 자료마다 달라 확정하지 않는다. <small>D10·D11</small></p></div>
  <div><time>2026.01.12</time><p>평의원회 학칙 개정안 <b>8:2 가결</b>은 회의록 취재 보도에 근거한다. 원본 회의록은 미확보다. <small>D14</small></p></div>
  <div><time>2026.02.26~27</time><p>2월 26일 개정 학칙 시행, 27일 대학이 이를 공고했다. 2029년 남학생 입학은 향후 계획이다. <small>D22·D23</small></p></div>
 </article>
</div>
<div class="v12-after-take"><b>판정</b><span>양교의 공식 절차는 진전됐다. 직원의 이의와 학생의 반대는 구성원 수용을 별도로 확인해야 함을 보여준다.</span></div>
<footer class="source-footer"><span>강원대 회의록·통합 승인·입학식 A02P·A07·A10·A17 · 동덕여대 D06·D07·D09·D10·D14·D22·D23</span><span>10 / 15</span></footer>''')

set_inner(11, '''
<header class="folio"><span>07 / COMPARATIVE SYNTHESIS</span><span>THREE CONDITIONS · THREE OUTCOMES</span></header>
<p class="deck-kicker">카메룬 변수의 결합과 결과</p>
<h2>어떤 조건이 입장을 바꿨나</h2>
<div class="v12-compare-head"><span>핵심 조건</span><span>강원대 통합</span><span>동덕여대 공학 전환</span></div>
<div class="v12-compare-row"><b>공중의 힘</b><p>평의원회가 8:12로 부결해 재상정이 필요했다.</p><p>학생의 반대·동원력은 컸지만 공식 의결 영향력은 제한됐다.</p></div>
<div class="v12-compare-row"><b>요구의 조정 범위</b><p>공무원 배치안을 바꾸는 부분 수용이 가능했다.</p><p>여대 유지라는 핵심 요구는 시점 조정과 맞바꿀 수 없었다.</p></div>
<div class="v12-compare-row"><b>기존 신뢰</b><p>선제출과 자료 공유 문제가 가결 뒤에도 이의를 남겼다.</p><p>사전 설명과 집계 규칙을 둘러싼 불신이 공론화 뒤에도 남았다.</p></div>
<div class="v12-outcome"><div><b>공식 결정</b><span>양교 모두 진전</span></div><div><b>요구 반영</b><span>강원대 인력 구성 변경<br>동덕여대 핵심 요구 미반영</span></div><div><b>사후 수용</b><span>직원 이의·학생 반대 확인<br>전체 구성원 수용도 미측정</span></div></div>
<footer class="source-footer"><span>카메룬 변수 E21·E24·I56 · A01P·A02P·A07 · D02·D07·D08·D10</span><span>11 / 15</span></footer>''')

set_inner(12, '''
<header class="folio"><span>08 / VARIABLE SCREENING</span><span>81 ITEMS · TWO CASES</span></header>
<p class="deck-kicker">전수분석의 선정 규칙</p>
<h2>왜 세 변수를 중심에 놓았나</h2>
<div class="v12-criteria">
 <div><b>상</b><span>공식 결정 또는 관찰된 입장 이동과 직접 연결된 근거</span></div>
 <div><b>중</b><span>배경·증폭·제약을 설명하지만 독립 효과는 확인되지 않음</span></div>
 <div><b>하</b><span>부차적 연결만 관찰됨</span></div>
 <div><b>미확인</b><span>공개 기록으로 존재나 작용을 판단하기 어려움</span></div>
</div>
<div class="v12-counts"><div><b>동덕여대</b><span>상 28</span><span>중 25</span><span>하 4</span><span>미확인 24</span></div><div><b>강원대</b><span>상 30</span><span>중 22</span><span>하 4</span><span>미확인 25</span></div></div>
<div class="v12-selection"><b>발표에서 고른 세 조건</b><span>공중의 힘(E24) · 공중의 양보 수준(E21)에 연결한 요구의 조정 가능성 · 조직과 공중의 신뢰(I56). 두 사례에서 모두 중요도가 높고, 대응 차이를 설명할 관찰 자료가 있다.</span></div>
<p class="v12-count-caveat">건수는 질적 중요도 판정의 분포이며 통계적 효과 크기가 아니다. ‘미확인’은 변수가 작용하지 않았다는 뜻이 아니다.</p>
<footer class="source-footer"><span>81개 변수 전수분석 보고서 · 교재 『PR커뮤니케이션』 표 2-5 · A01P·A02P·D07·D08</span><span>12 / 15</span></footer>''')

set_inner(14, '''
<header class="folio"><span>10 / FINAL MESSAGE ANALYSIS</span><span>BENOIT · ONE PAGE</span></header>
<p class="deck-kicker">최종 단계: 베노이트의 이미지 회복 전략</p>
<h2>메시지, 실제 조치, 성과</h2>
<div class="v12-benoit-head"><span>사례</span><span>공식 발화와 전략 분류</span><span>확인된 조치</span><span>회복 성과</span></div>
<div class="v12-benoit-row"><b>강원대</b><p>기획처장은 자료 송부 지연을 사과했다. 본부는 수정안을 설명했다.<br><strong>제한된 사과 · 시정조치 제시</strong></p><p>공무원 35명 제안을 24명과 외부 전문가 11명으로 변경해 재상정했다. <small>A03P·A02P</small></p><p>15:6 가결은 확인된다. 직원 수용과 실제 인사 배치는 미확인이다. <small>A07</small></p></div>
<div class="v12-benoit-row"><b>동덕여대</b><p>대학은 ‘이미 단독 결정’ 주장을 부인하고 여성교육의 성과를 강조했다.<br><strong>제한적 부인 · 긍정적 이미지 강조</strong></p><p>2024년 논의를 잠정 중단했고, 2025년 공론화를 운영했다. <small>D26·D02·D08</small></p><p>학생 총투표에서 반대 85.7%가 발표됐다. 이미지·신뢰 회복은 입증되지 않았다. <small>D10</small></p></div>
<div class="v12-benoit-note"><b>분석의 역할</b><span>베노이트는 발화의 전략을 분류한다. 대응을 낳은 조건은 카메룬으로 설명한다. 발화의 분류만으로 평판 회복을 판정하지 않는다.</span></div>
<footer class="source-footer"><span>Benoit (1997) · 강원대 A03P·A02P·A07 · 동덕여대 D26·D02·D08·D10</span><span>14 / 15</span></footer>''')
slides[13]["class"] = ["slide", "paper-slide"]

html = str(soup)
changes = [
    ("총투표 <b>85.7% 반대</b>(12/3~7)", "총투표 <b>85.7% 반대</b>(12/9 결과 발표)"),
    ("<b>생존 위기:</b> 학령인구 급감 속 사립 여대의 경쟁력 약화 및 정원 확보 불안 대응.",
     "<b>본부의 문제 인식:</b> 학령인구 감소와 경쟁력·모집 우려를 전환 검토의 이유로 제시. 위험 규모의 독립 재무분석은 미확보."),
    ("공식적 설명과 사전 협의가 이루어지기 전에 '선제출'과 '소문 유출'이 선행되면서, 내부 구성원 사이에 밀실 추진 인식이 고착화되었다.",
     "선제출과 소문 확산에 대해 구성원들이 사전 협의 부족을 제기했다. 이후 신뢰의 변화는 별도로 측정되지 않았다."),
    ("<b>카메룬 · 요구의 조정 가능성:</b> 조직·인력 구성안 변경",
     "<b>카메룬 · 부분 수용:</b> 조정 가능한 인력 구성안 변경"),
    ("<b>복합 요인</b> 조직안 수정만으로 가결 이유를 설명할 수 없다.",
     "<b>복합 요인</b> 인력 수정, 정부 일정 압박, 다른 조직안 조정이 함께 작용했다. 각각의 독립 효과는 미확인이다."),
    ("<b>검증 범위</b> 수정안 설명은 확인되나 실제 인사 배치는 미확인. 당일 추가 수정도 제한됐다 (A02P 3–4쪽).",
     "<b>검증 범위</b> 총원 35명의 구성 변경이다. 실제 인사 배치는 미확인이고 당일 추가 수정도 제한됐다 (A02P 3–4쪽)."),
    ("<b>카메룬 · 학생의 압력과 수용 범위:</b> 높은 관련성과 집단행동이 11월 21일 논의 잠정 중단을 이끌었다. 공학 전환 방향까지 철회된 것은 아니다 (D02·D26).",
     "<b>카메룬 · 영향력의 두 형태:</b> 높은 관련성과 집단행동은 11월 21일 논의 잠정 중단을 압박했다. 학생의 공식 의결권은 이후 절차에서 제한적이었다 (D02·D05)."),
    ("학생 총투표(2025.12.03.~07.) 반대 85.7% · D10 / 평의원회 8:2 · D14",
     "학생 총투표 결과 발표(2025.12.09.) 반대 85.7% · D10 / 평의원회 8:2는 취재 보도 · D14"),
    ("지원자 −32.9% · D15 (원인 미확인 참고 지표)",
     "2029~2030년 조건부 문항 · D07 4쪽 / 실제 전환 시행은 미래 계획"),
    ("<div class=\"v9-bib-row\"><b>Heath (1997)</b><span><i>Strategic Issues Management</i>. Sage.</span></div>", ""),
    ("<div class=\"v9-bib-row\"><b>Sturges (1994)</b><span>“Communicating through crisis.” <i>Management Communication Quarterly, 7</i>(3), 297–316.</span></div>", ""),
    ("<div class=\"v9-bib-row\"><b>Wilcox &amp; Cameron (2005)</b><span><i>Public Relations: Strategies and Tactics</i>, 8th ed.</span></div>", ""),
    ("<div class=\"v9-bib-row\"><b>Leventhal (1980)</b><span>“What should be done with equity theory?” In <i>Social Exchange</i>, 27–55.</span></div>", ""),
    ("<div class=\"v9-bib-row\"><b>Tyler (1988)</b><span>“What is procedural justice?” <i>Law &amp; Society Review, 22</i>(1), 103–135.</span></div>", ""),
    ("Cameron의 정황적 수용 이론을 중심으로 메시지·절차 분석 문헌을 함께 사용", "카메룬의 상황변수와 베노이트의 발화 전략을 구분해 사용"),
    ("전체 서지·원문 링크: deck_v11_참고문헌.md 및 sources.html", "전체 서지·원문 링크: deck_v12_참고문헌.md 및 sources.html"),
    ("deck_v11.pdf", "deck_v12.pdf"),
]
for old, new in changes:
    if old not in html:
        raise ValueError(f"Missing expected HTML text: {old[:70]}")
    html = html.replace(old, new, 1)
for old, new in {
    "03 · 대응을 바꾸는 조건": "03 · 분석 틀",
    "09 · 집계 규칙": "09 · 집계 규칙",
    "11 · 변수의 결합": "11 · 조건과 결과",
    "12 · 81개 변수의 중요도": "12 · 변수 선정 규칙",
    "14 · 베노이트 한 장": "14 · 메시지와 성과",
}.items():
    if old != new:
        html = html.replace(old, new, 1)
parsed = BeautifulSoup(html, "html.parser")
for i, (button, slide) in enumerate(zip(parsed.select(".toc-item"), parsed.select("section.slide")), 1):
    title = (slide.find(["h1", "h2"]) or slide).get_text(" ", strip=True)
    button.string = f"{i:02d} · {title}"
html = str(parsed)
(TARGET / "index.html").write_text(html, encoding="utf-8")

js = (SOURCE / "slides.js").read_text(encoding="utf-8")
match = re.search(r"const SPEAKER_NOTES = (\[.*?\]);", js, re.S)
assert match
notes = json.loads(match.group(1))
updates = {
  3: ("81개 변수와 세 조건", "외부 24개·내부 57개를 모두 검토했습니다. 발표는 두 사례 모두에서 대응 차이를 설명할 자료가 있는 공중의 힘, 양보 수준에 연결한 요구의 조정 가능성, 기존 신뢰를 중심으로 합니다. 요구의 조정 가능성은 교재 변수명이 아니라 연구자의 관찰 지표입니다. 학생·직원은 기업의 외부 공중과 다른 내부 구성원입니다.", "평의원회의 공식 심의권과 학생의 여론 영향력을 같은 권력으로 취급하지 않습니다."),
  4: ("서로 다른 구조개편 압력", "강원대는 정부 지원을 연계한 통합을 추진했습니다. 동덕여대 본부는 경쟁력과 지속가능성을 전환 검토 이유로 제시했습니다. 공개 자료만으로 재무적 존립 위기를 확정할 수는 없습니다.", "본부의 주장과 독립적으로 검증된 재무 사실을 구분합니다."),
  5: ("신뢰가 약해진 출발점", "강원대 제46차 회의록에는 257쪽 자료가 이틀 전 송부됐다는 발언이 있습니다. 동덕여대는 사전 설명 전에 논의가 알려져 학생이 반발했습니다. 신뢰 저하의 크기는 독립 조사로 측정되지 않았습니다.", "이틀 전 송부는 A03P 원문에 근거합니다. 밀실 추진을 확정된 동기로 단정하지 않습니다."),
  7: ("조정 가능한 인력 문제", "본부는 전략실 공무원 35명 제안을 24명과 외부 전문가 11명으로 바꿨습니다. 총원 35명 감축이 아닌 구성 변경입니다. 인력 수정, 정부 일정 압박, 다른 조직안 조정이 함께 작용했을 수 있습니다. 15대6 가결만으로 각 원인의 독립 효과는 알 수 없습니다.", "실제 전문가 채용과 직원 수용은 별도 확인이 필요합니다."),
  8: ("학생의 두 종류의 영향력", "학생의 높은 관련성과 집단행동은 2024년 논의 잠정 중단에 압력을 주었습니다. 이후 공론화위의 학생위원은 12명 중 3명이었고, 동원력과 공식 의결권은 다른 변수입니다.", "잠정 중단은 공학 전환 방침의 영구 철회가 아닙니다."),
  9: ("같은 응답, 다른 집계 규칙", "2025년 최종 온라인 조사는 재학생이 모두 졸업한 뒤인 2029~2030년 예상 시점의 전환을 물었습니다. 전체 응답자는 3,176명입니다. 51.8%는 집단별 동일 가중으로 계산된 공학 전환 찬성이고, 66.1%는 인원수 기준 재계산의 여대 유지 선택입니다. 학생 2,889명 중 71.3%가 여대 유지를 택했습니다.", "두 수치를 전체 응답자의 단순 찬반으로 소개하면 틀립니다. 가중 규칙의 정당성은 의견이 갈립니다."),
  10: ("사건일과 발표일 구분", "동덕여대 학생 총투표 반대 85.7%는 12월 9일 발표됐습니다. 투표 종료일은 보도마다 차이가 있어 특정하지 않습니다. 2029년 조건은 그보다 앞선 공론화 질문에도 있었습니다. 강원대 입학식은 2026년 2월 26~27일, 통합 출범은 3월 1일입니다. 동덕여대 평의원회 8대2는 회의록을 취재한 보도이며 원본은 확보되지 않았습니다.", "2029년 실제 남학생 입학과 강원대 수정안 실제 인사 배치는 아직 확인된 결과가 아닙니다."),
  11: ("세 조건과 세 결과", "강원대에서는 평의원회 부결, 조정 가능한 인력 배치, 선제출에 따른 불신이 함께 작용했습니다. 동덕여대에서는 강한 학생 동원력, 여대 유지 요구의 성격, 집계 규칙에 대한 불신이 결합했습니다. 공식 결정은 양교 모두 진전됐지만 요구 반영 범위는 달랐고 사후 수용은 별개입니다.", "변수의 결합은 사례 해석이지 통제된 인과효과 추정이 아닙니다."),
  12: ("변수 선정과 등급", "81개 항목 모두에 질적 중요도를 판정했습니다. 동덕여대는 상 28, 중 25, 하 4, 미확인 24개이고 강원대는 상 30, 중 22, 하 4, 미확인 25개입니다. 발표 중심 변수는 양쪽에서 중요하고 대응 차이를 설명할 원문 자료가 있는 세 조건입니다.", "등급 건수는 통계적 효과 크기가 아닙니다. 미확인은 비작용을 뜻하지 않습니다."),
  14: ("베노이트 이미지 회복 전략", "마지막으로 공식 발화를 분류합니다. 강원대 사과는 자료 송부 지연에 한정됩니다. 인력 수정안은 시정조치 제시와 후속 안의 변경으로 확인됩니다. 동덕여대는 이미 단독 결정했다는 주장에 제한적으로 반박하고 여성교육의 성과를 강조했습니다. 발화, 실제 조치, 신뢰 회복 성과를 각기 구분합니다.", "15대6 가결이나 메시지 발표만으로 이미지 회복을 입증할 수 없습니다."),
}
for slide_number, (title, script, qa) in updates.items():
    notes[slide_number - 1] = {"title": f"Slide {slide_number:02d} · {title}", "script": script, "qa": qa}
js = js[:match.start(1)] + json.dumps(notes, ensure_ascii=False, indent=2) + js[match.end(1):]
(TARGET / "slides.js").write_text(js, encoding="utf-8")
details = [f"{item['title']}\n{item['script']}\n검증 메모: {item['qa']}" for item in notes]
(TARGET / "archive_details.js").write_text("window.ARCHIVE_DETAILS = " + json.dumps(details, ensure_ascii=False, indent=2) + ";\n", encoding="utf-8")

css = '''
/* v12 content-first layouts with larger internal margins */
.v12-theory-intro,.v12-theory-caveat,.v12-question,.v12-weight-note,.v12-after-take,.v12-selection,.v12-benoit-note{margin-left:82px;margin-right:82px;display:grid;grid-template-columns:180px 1fr;gap:18px;border-top:1px solid #9aa7a1;padding:15px 0;font-size:21px;line-height:1.4}
.v12-theory-intro{margin-top:32px;grid-template-columns:240px 220px 1fr;border-top:2px solid #24575c;align-items:start}
.v12-theory-intro b,.v12-theory-caveat b,.v12-question b,.v12-weight-note b,.v12-after-take b,.v12-selection b,.v12-benoit-note b{color:#24575c}
.v12-theory-intro p{margin:0}
.v12-three-axis{display:grid;grid-template-columns:repeat(3,1fr);gap:34px;margin:27px 82px 23px}
.v12-three-axis article{border-top:3px solid #9d493f;padding:12px 0}
.v12-three-axis article>span{color:#9d493f;font-weight:800;font-size:18px}
.v12-three-axis h3{font-size:29px;margin:10px 0 11px}
.v12-three-axis p{font-size:21px;line-height:1.4;margin:0 0 13px}
.v12-three-axis small{font-size:17px;line-height:1.35;color:#565e59}
.v12-theory-caveat{margin-top:12px;font-size:19px}
.v12-question{grid-template-columns:150px 1fr;margin-top:35px;border-top:2px solid #24575c;row-gap:4px}
.v12-question small{grid-column:2;font-size:17px;color:#5a615c}
.v12-question strong{color:#9d493f}
.v12-weight-grid{display:grid;grid-template-columns:1fr 1fr;gap:36px;margin:32px 82px 22px}
.v12-weight-grid article{border-top:3px solid #24575c;padding-top:15px}
.v12-weight-grid article:nth-child(2){border-color:#9d493f}
.v12-weight-grid span{display:block;font-size:18px;font-weight:700}
.v12-weight-grid strong{font-size:75px;line-height:1.07;color:#24575c;display:block;margin-top:11px}
.v12-weight-grid article:nth-child(2) strong{color:#9d493f}
.v12-weight-grid b{font-size:23px}
.v12-weight-grid p{font-size:20px;line-height:1.4;margin:17px 0 0}
.v12-weight-note{font-size:20px}
.v12-after-grid{display:grid;grid-template-columns:1fr 1fr;gap:35px;margin:28px 76px 15px}
.v12-after-grid article{border-top:3px solid #24575c;padding-top:8px}
.v12-after-grid article:nth-child(2){border-color:#9d493f}
.v12-after-grid h3{font-size:27px;margin:7px 0 12px}
.v12-after-grid article>div{display:grid;grid-template-columns:135px 1fr;gap:10px;border-top:1px solid #c1c9c3;padding:11px 0}
.v12-after-grid time{font-size:17px;font-weight:800;color:#24575c}
.v12-after-grid p{margin:0;font-size:18px;line-height:1.34}
.v12-after-grid small{color:#636966;font-size:15px;white-space:nowrap}
.v12-after-take{font-size:19px;margin-top:0}
.v12-compare-head,.v12-compare-row{display:grid;grid-template-columns:23% 38.5% 38.5%;margin:0 80px;border-bottom:1px solid #b8c0ba;gap:0;padding:12px 0}
.v12-compare-head{margin-top:30px;background:#e5e9e5;font-size:18px;font-weight:800;color:#24575c;border-top:2px solid #24575c;padding:13px 10px}
.v12-compare-row{padding:20px 10px}
.v12-compare-row b{font-size:22px}
.v12-compare-row p{font-size:20px;line-height:1.4;margin:0 22px 0 0}
.v12-outcome{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin:35px 80px 0}
.v12-outcome div{border-top:3px solid #9d493f;padding-top:12px}
.v12-outcome b{display:block;font-size:21px;color:#9d493f;margin-bottom:9px}
.v12-outcome span{font-size:19px;line-height:1.37}
.v12-criteria{display:grid;grid-template-columns:1fr 1fr;gap:0 32px;margin:32px 83px 0}
.v12-criteria div{display:grid;grid-template-columns:95px 1fr;gap:10px;border-top:1px solid #aab4ad;padding:12px 0;font-size:19px;line-height:1.33}
.v12-criteria b{color:#24575c}
.v12-counts{margin:33px 83px 0;border-top:2px solid #24575c}
.v12-counts div{display:grid;grid-template-columns:210px repeat(4,1fr);padding:15px 5px;border-bottom:1px solid #bdc5bf;font-size:22px}
.v12-counts b{font-size:24px}
.v12-counts span:last-child{color:#9d493f}
.v12-selection{margin-top:28px;font-size:20px;grid-template-columns:245px 1fr}
.v12-count-caveat{font-size:18px;margin:11px 84px 0;color:#454d48}
.v12-benoit-head,.v12-benoit-row{display:grid;grid-template-columns:15% 32% 27% 26%;margin:0 74px;padding:13px 10px;border-bottom:1px solid #b8c0ba}
.v12-benoit-head{margin-top:33px;border-top:2px solid #24575c;background:#e5e9e5;font-size:17px;font-weight:800;color:#24575c}
.v12-benoit-row{padding-top:24px;padding-bottom:24px}
.v12-benoit-row b{font-size:23px}
.v12-benoit-row p{font-size:19px;line-height:1.41;margin:0 18px 0 0}
.v12-benoit-row strong{display:block;margin-top:9px;color:#9d493f}
.v12-benoit-row small{display:block;color:#626964;font-size:16px;margin-top:6px}
.v12-benoit-note{margin-top:39px;font-size:20px}
'''
(TARGET / "style.css").write_text((SOURCE / "style.css").read_text(encoding="utf-8") + css, encoding="utf-8")
print("Built", TARGET)
