"""Build the Cameron-led v11 revision from the preserved v10 HTML deck."""
from pathlib import Path
import json
import re
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
DECK = ROOT / "versions" / "deck_v11"
html = (DECK / "index.html").read_text(encoding="utf-8")
soup = BeautifulSoup(html, "html.parser")
slides = soup.select("section.slide")
assert len(slides) == 15

def set_inner(node, markup):
    node.clear()
    fragment = BeautifulSoup(markup, "html.parser")
    for child in list(fragment.contents):
        node.append(child)

def replace_once(old, new):
    global html
    if old not in html:
        raise ValueError(f"Text not found: {old[:90]}")
    html = html.replace(old, new, 1)

# The last analytic pages use the original typography and color vocabulary.
set_inner(slides[11], '''
<header class="folio"><span>08 / VARIABLE PRIORITIES</span><span>CAMERON · 81 VARIABLES</span></header>
<p class="deck-kicker">전수 평가에서 설명력이 큰 조건</p>
<h2>81개 변수의 중요도</h2>
<div class="v11-matrix">
 <div class="v11-matrix-head"><span>변수군</span><span>강원대</span><span>동덕여대</span></div>
 <div><b>외부 압력과 자원</b><p>정부 지원·일정 압박 <strong>상</strong><br>통합 목표를 유지하는 제약</p><p>대학 경쟁·재정 우려 <strong>중</strong><br>전환 명분, 위험 규모는 미측정</p></div>
 <div><b>공중의 상대적 힘</b><p>평의원회 8:12 부결 <strong>상</strong><br>수정안을 요구한 제도적 관문</p><p>학생 동원력 <strong>상</strong><br>공론화위 3/12석, 제도적 저지력은 제한</p></div>
 <div><b>요구의 조정 가능성</b><p>공무원 배치 변경 <strong>상</strong><br>35명 제안을 24명과 외부 전문가 11명으로 조정</p><p>여대 유지 요구 <strong>상</strong><br>시점 조정만으로 핵심 요구를 충족하기 어려움</p></div>
 <div><b>기존 관계와 신뢰</b><p>선제출·자료 공유 논란 <strong>상</strong><br>가결 뒤에도 직원 이의 지속</p><p>사전 설명·가중치 논란 <strong>상</strong><br>절차 참여 뒤에도 학생 반대 지속</p></div>
</div>
<p class="v11-note">상·중은 효과 크기가 아닌 사례 설명의 중요도다. PR부서 인력·예산, 개인 성향 등은 공개 기록으로 판정하기 어렵다.</p>
<footer class="source-footer"><span>81개 변수 전수분석 · A01P · A02P · A07 · D07 · D08 · D10</span><span>12 / 15</span></footer>''')

set_inner(slides[12], '''
<header class="folio"><span>09 / EVIDENCE AND LIMITS</span><span>CAMERON · INFERENCE BOUNDARIES</span></header>
<p class="deck-kicker">변수 적용의 근거와 한계</p>
<h2>무엇이 확인되고 남았나</h2>
<div class="v11-evidence">
 <article><span>확인 01</span><h3>조직의 입장 이동</h3><p>강원대는 부결 뒤 인력 구성안을 고쳐 재상정했다. 동덕여대는 논의를 잠정 중단하고 공론화했지만 공학 전환 방향을 유지했다.</p><small>A01P · A02P · D02 · D08 · D09</small></article>
 <article><span>확인 02</span><h3>공식 결정과 수용</h3><p>강원대 수정안은 15:6으로 가결됐다. 동덕여대 학칙 개정도 진행됐다. 직원의 이의와 학생 총투표 반대는 별도의 결과다.</p><small>A02P · A07 · D10 · D14 · D22</small></article>
 <article><span>판정 유보</span><h3>사람과 부서의 속성</h3><p>PR 담당자의 인원·자율성·예산, 의사결정자의 성격·윤리관·성별은 공개 기록만으로 중요도를 판단할 수 없다.</p><small>81개 변수 중 공개 근거가 없는 항목</small></article>
</div>
<div class="v11-limit"><b>분석의 경계</b><span>무기명 표결의 개인별 전향, 강원대 수정안의 실제 인사 배치, 동덕여대 2029년 전환 시행 및 사후 신뢰 변화는 확인되지 않았다. 내부 구성원을 기업의 외부 공중과 동일시하지 않는다.</span></div>
<footer class="source-footer"><span>전수분석 보고서 · 강원대 제47·48차 회의록 · 동덕여대 공론화 자료 및 학칙 공고</span><span>13 / 15</span></footer>''')

set_inner(slides[13], '''
<header class="folio"><span>10 / FINAL MESSAGE ANALYSIS</span><span>BENOIT · ONE-PAGE CHECK</span></header>
<p class="deck-kicker">최종 단계: 베노이트의 이미지 회복 전략</p>
<h2>발화와 행동의 차이</h2>
<div class="v11-benoit">
 <div class="v11-benoit-head"><span>사례</span><span>확인된 공식 발화</span><span>전략 판독과 행동 대조</span></div>
 <div><b>강원대</b><p>2월 28일 기획처장이 자료 공유 지연을 사과했다. 이후 본부는 조직·인력 수정안을 설명했다.</p><p><strong>제한된 사과와 시정조치</strong><br>사과 대상은 자료 지연이다. 수정안은 제시됐지만 실제 인사 배치와 직원 수용은 미확인이다. [A03P·A02P·A07]</p></div>
 <div><b>동덕여대</b><p>대학은 ‘이미 단독 결정’ 주장을 부인했고, 총장은 여성교육의 성과와 향후 전환 방향을 함께 말했다.</p><p><strong>제한적 부인·긍정적 이미지 강조</strong><br>2024년 논의 잠정 중단은 확인된다. 2029년 시행 계획은 여대 유지 요구의 수용과 다르다. [D26·D02·D09]</p></div>
</div>
<blockquote class="v11-benoit-quote">이미지 회복 전략은 <b>무슨 말을 했는가</b>를 분류한다.<br>카메룬의 상황변수는 <b>왜 그 입장을 택했는가</b>를 설명한다.</blockquote>
<footer class="source-footer"><span>Benoit (1997) · A03P · A02P · A07 · D26 · D02 · D09</span><span>14 / 15</span></footer>''')

# Update captions and theory references on the unchanged evidence-rich pages.
html = str(soup)
replacements = [
 ('<b>분석 순서</b>: Cameron으로 대응의 이동 조건을 설명하고, Benoit으로 실제 발화의 이미지 회복 전략을 판독한다. 발화와 후속 행동은 따로 대조하며, 내부 구성원을 기업의 외부 공중과 동일시하지 않는다.',
  '<b>판정 기준</b>: 교재의 외부 24개·내부 57개 변수를 모두 검토하고 중요도를 상·중·하·미확인으로 구분했다. 본문에는 의결·대응 변화를 설명하는 조건을 제시한다.'),
 ('<b>베노이트 · 사과의 범위:</b> 2월 28일 기획처장은 자료 지연을 사과했다 (A03P 5쪽). 통합안 전체에 대한 사과로 확대할 수 없다. 4월 1일의 사후 수정 약속은 당시 실행 결과가 아니었고, 안은 8:12로 부결됐다.',
  '<b>카메룬 · 외부 압력과 공중의 힘:</b> 정부 지원 축소 우려는 통합 추진을 재촉했다. 그러나 평의원회는 실제로 8:12 부결을 만들어 본부의 안을 제약했다 (A01P).'),
 ('<b>베노이트 · 시정조치:</b> 조직·인력 구성안 조정',
  '<b>카메룬 · 요구의 조정 가능성:</b> 조직·인력 구성안 변경'),
 ('<b>베노이트 · 제한적 부인 → 시정조치:</b> D26의 부인은 ‘이미 단독 결정했다’는 주장에 한정된다. 11월 21일 논의 잠정 중단은 실제 행동 변화다. 공학 전환 방침 자체의 철회는 아니다.',
  '<b>카메룬 · 학생의 압력과 수용 범위:</b> 높은 관련성과 집단행동이 11월 21일 논의 잠정 중단을 이끌었다. 공학 전환 방향까지 철회된 것은 아니다 (D02·D26).'),
 (' · Benoit (1997)</span><span>08 / 15', '</span><span>08 / 15'),
 ('<b>메시지와 행동</b><span>동덕여대 입장문의 전통·미래 강조는 베노이트의 긍정적 이미지 강조·초월로 읽힌다 (D09). 2029년 계획과 학칙 개정은 확인되지만 여대 유지 요구의 수용은 아니다.</span>',
  '<b>카메룬 변수</b><span>조직의 공식 결정권과 학생의 동원력은 동시에 작용했다. 2029년 계획과 학칙 개정은 확인되지만 여대 유지 요구의 수용은 아니다.</span>'),
 ('<b>해명 → 수정안 제시</b>', '<b>부분적 행동 수용</b>'),
 ('<b>제한적 부인 → 잠정 중단</b>', '<b>절차적 수용과 핵심 옹호</b>'),
 ('Cameron: 대응 조건의 차이 · Benoit: 공식 발화의 전략 · 원문 대조: 실제 행동과 결정 이후 반응',
  'Cameron: 공중의 힘 · 요구의 조정 가능성 · 자원 압력 · 기존 신뢰를 함께 비교'),
 ('Cancel et al. (1997) · Cameron et al. (2001) · Benoit (1997) · A01P–A03P · D09 · D26',
  'Cancel et al. (1997, 1999) · Cameron et al. (2001) · A01P–A03P · D07–D10'),
 ('<h2>구조개편의 배경</h2>', '<h2>서로 다른 구조개편 압력</h2>'),
 ('<h2>위기의 발생</h2>', '<h2>신뢰가 약해진 출발점</h2>'),
 ('<h2>선제출과 부결</h2>', '<h2>부결을 만든 제도적 힘</h2>'),
 ('<h2>약속에서 수정으로</h2>', '<h2>조정 가능한 인력 문제</h2>'),
 ('<h2>소문과 갈등</h2>', '<h2>동덕여대 학생의 동원력</h2>'),
 ('<h2>공론화의 딜레마</h2>', '<h2>대표성을 둘러싼 집계 규칙</h2>'),
 ('<h2>결정 이후의 반발</h2>', '<h2>결정 이후에도 남은 반대</h2>'),
 ('<h2>같은 옹호, 다른 수용</h2>', '<h2>핵심 변수의 결합</h2>'),
 ('2025.05.08</time><b>대교협 제출</b><span>2026학년도 대입전형 시행계획 수정 제출 마감 준수',
  '2025.05</time><b>입시 계획 후속 절차</b><span>통합 승인에 앞서 입시 계획 조정'),
 ('2025.06.05</time><b>교육부 최종 승인</b>', '2025.05.28</time><b>교육부 통합 승인</b>'),
 ('2026.03.03</time><b>통합 대학교 출범</b>', '2026.03.01</time><b>통합 대학교 출범</b>'),
 ('기사: 강원도민일보 (2025.02.25.) · 아주경제 (2024.11.13.) · Sturges (1994) 사전 커뮤니케이션',
  '강원대 평의원회 회의록 A03P · 동덕여대 공식 소통 경과 D26 · Cameron 상황변수 I1·I56'),
]
for old, new in replacements:
    replace_once(old, new)

# Refresh table of contents and link to the full audit.
for old, new in {
    '04 · 구조개편의 배경':'04 · 구조개편 압력', '05 · 위기의 발생':'05 · 신뢰의 출발점',
    '06 · 선제출과 부결':'06 · 제도적 힘', '07 · 약속에서 수정으로':'07 · 인력 문제',
    '08 · 소문과 갈등':'08 · 학생의 동원력', '09 · 공론화의 딜레마':'09 · 집계 규칙',
    '10 · 결정 이후의 반발':'10 · 남은 반대', '11 · 같은 옹호, 다른 수용':'11 · 변수의 결합',
    '12 · 위기의 전조':'12 · 81개 변수의 중요도', '13 · 참여와 결정권':'13 · 확인과 한계',
    '14 · 시점·규칙·행동':'14 · 베노이트 한 장',
}.items():
    replace_once(old, new)
replace_once('<a href="sources.html">원자료</a>', '<a href="카메룬_81개_변수_전수분석.md">81개 변수 보고서</a><a href="sources.html">원자료</a>')
replace_once('deck_v10.pdf', 'deck_v11.pdf')
(DECK / "index.html").write_text(html, encoding="utf-8")

notes = [
  ("표지", "두 사례 모두 공식 결정은 진전됐지만 반대 집단의 수용은 별도로 평가해야 합니다. 발표는 카메룬의 상황변수로 대응의 조건을 설명하고 마지막에 베노이트를 한 장으로 다룹니다.", "공식 의결과 실제 수용을 혼동하지 않습니다."),
  ("결정과 수용", "평가 축은 공식 결정, 핵심 요구 반영, 결정 이후 수용입니다. 회의록과 공론화 원자료를 중심으로 두 사례를 같은 질문에 대입합니다.", "수용도에 관한 동일 질문의 사후 반복조사는 확보되지 않았습니다."),
  ("대응을 바꾸는 조건", "교재에는 외부 24개와 내부 57개, 총 81개 변수가 있습니다. 전수분석에서는 상·중·하·미확인으로 평가했습니다. 이 발표는 그중 실제 입장 이동을 설명하는 변수를 선택해 보여줍니다.", "기업의 외부 공중 모델을 대학 내부 구성원에게 적용하는 한계를 명시합니다."),
  ("구조개편 압력", "강원대에는 정부 지원과 네 캠퍼스의 배분 문제가, 동덕여대에는 여성교육 정체성과 대학 경쟁력 주장이 있었습니다. 후자의 재정 위험 규모는 독립 검증되지 않았습니다.", "동덕여대의 존립 위기를 확정된 재무 사실로 표현하지 않습니다."),
  ("신뢰의 출발점", "강원대는 선제출과 자료 공유 방식이, 동덕여대는 공식 설명 전 논의가 알려진 경위가 불신의 출발점이었습니다. 이는 조직문화·기존 신뢰 변수와 연결됩니다.", "초기 소통 부족을 개인의 동기나 인성으로 단정하지 않습니다."),
  ("제도적 힘", "강원대는 지원 축소 우려로 통합을 서둘렀지만 평의원회가 8대12로 부결했습니다. 외부 자원 압력과 내부 공중의 제도적 힘이 동시에 작용했습니다.", "부결을 곧바로 법적 최종 거부권 전체로 확대하지 않습니다."),
  ("인력 문제", "4월 28일 본부는 전략실의 공무원 35명 제안을 공무원 24명과 외부 전문가 11명으로 바꾸어 설명했습니다. 총원 35명 축소가 아니라 구성 변경입니다. 표결은 15대6으로 가결됐습니다.", "실제 채용·배치는 확인되지 않았고 무기명 투표라 개인별 전향도 알 수 없습니다."),
  ("학생의 동원력", "동덕여대 학생의 높은 관련성과 자체 여론 형성이 2024년 논의 잠정 중단에 압력을 가했습니다. 본부는 수업 재개와 협의에 합의했지만 공학 전환을 영구 철회한 것은 아닙니다.", "학생의 동원력과 제도적 의결권은 구별해야 합니다."),
  ("집계 규칙", "2025년 최종 온라인 조사의 51.8%는 교원·학생·직원 집단별 동일 가중치입니다. 학생 2,889명 중 71.3%는 여대 유지였습니다. 어떤 집계 규칙이 정당한지 합의가 없었기에 결과 해석이 충돌했습니다.", "51.8%를 응답자 전체 단순 찬성 비율로 말하지 않습니다."),
  ("남은 반대", "두 조직 모두 공식 절차가 진행됐지만 직원협의회의 이의와 학생 총투표 반대가 남았습니다. 동덕여대 2029년 시행은 계획이며 현재 완료된 결과가 아닙니다.", "총투표 85.7%와 공론화 조사 51.8%는 서로 다른 질문·집계 방식입니다."),
  ("변수의 결합", "강원대는 정부 압력, 평의원회 부결, 조정 가능한 인력 요구가 함께 작용했습니다. 동덕여대는 정체성 요구, 학생 동원력, 집단별 가중 규칙과 제한된 의결 영향력이 결합했습니다.", "단일 변수가 결과를 기계적으로 결정했다는 인과 주장은 하지 않습니다."),
  ("81개 변수의 중요도", "전수분석에서 중요도가 높은 변수군을 네 줄로 비교했습니다. 강원대에는 정부 지원과 평의원회의 부결, 동덕여대에는 정체성과 대표성 논란이 두드러집니다. 개인·PR부서 변수의 많은 항목은 미확인입니다.", "미확인은 작용하지 않았다는 판정이 아닙니다."),
  ("확인과 한계", "원문으로 확인되는 변화와 공개 기록으로는 판정할 수 없는 속성을 구분했습니다. 조직의 행동으로 담당자 개인의 윤리관이나 성별 효과를 추측하지 않습니다.", "실제 인력 배치와 2029년 전환 시행, 신뢰의 정량 변화가 남은 검증 과제입니다."),
  ("베노이트 한 장", "마지막으로 공식 발화를 이미지 회복 전략으로 분류합니다. 강원대의 사과는 자료 지연에 한정되고, 인력 수정안은 시정조치에 해당합니다. 동덕여대는 이미 단독 결정했다는 주장을 제한적으로 부인했고 여성교육 성과를 강조했습니다. 발화와 후속 행동은 구분합니다.", "전략 분류가 실제 신뢰 회복의 성과를 입증하지는 않습니다."),
  ("참고문헌", "교재의 81개 변수와 Cancel·Cameron의 이론, 사건별 원문을 대조했습니다. 전수분석 보고서와 문서 ID는 덱 하단에서 열 수 있습니다.", "언론 보도와 공식 문서를 증거 수준에 따라 구분합니다."),
]
js = (DECK / "slides.js").read_text(encoding="utf-8")
entries = [{"title": f"Slide {i:02d} · {title}", "script": script, "qa": qa} for i, (title, script, qa) in enumerate(notes, 1)]
js = re.sub(r"const SPEAKER_NOTES = \[.*?\n\];", "const SPEAKER_NOTES = " + json.dumps(entries, ensure_ascii=False, indent=2) + ";", js, count=1, flags=re.S)
(DECK / "slides.js").write_text(js, encoding="utf-8")
details = [f"{title}\n{script}\n검증 메모: {qa}" for title, script, qa in notes]
(DECK / "archive_details.js").write_text("window.ARCHIVE_DETAILS = " + json.dumps(details, ensure_ascii=False, indent=2) + ";\n", encoding="utf-8")

css = '''
/* v11 Cameron-led analysis pages */
.v11-matrix,.v11-benoit{margin:28px 72px 0;border-top:2px solid #173e45;font-family:inherit}
.v11-matrix-head,.v11-benoit-head,.v11-matrix>div:not(:first-child),.v11-benoit>div:not(:first-child){display:grid;grid-template-columns:23% 38.5% 38.5%;gap:0;border-bottom:1px solid rgba(20,48,52,.24)}
.v11-matrix-head,.v11-benoit-head{font-size:17px;font-weight:800;color:#25555a;background:#e5e9e5;padding:12px 15px}
.v11-matrix>div:not(:first-child),.v11-benoit>div:not(:first-child){padding:14px 15px;align-items:start}
.v11-matrix b,.v11-benoit b{font-size:23px;color:#173e45}
.v11-matrix p,.v11-benoit p{font-size:19px;line-height:1.38;margin:0 12px 0 0}
.v11-matrix strong,.v11-benoit strong{color:#9d493f}
.v11-note{margin:18px 74px 0;font-size:18px;line-height:1.4}
.v11-evidence{display:grid;grid-template-columns:repeat(3,1fr);gap:25px;margin:42px 70px 0}
.v11-evidence article{border-top:3px solid #24575c;padding:20px 5px 0}
.v11-evidence article:nth-child(3){border-color:#a34e42}
.v11-evidence span{font-size:17px;color:#9d493f;font-weight:800}
.v11-evidence h3{font-size:29px;margin:14px 0}
.v11-evidence p{font-size:21px;line-height:1.46;margin:0 0 18px}
.v11-evidence small{font-size:16px;color:#555}
.v11-limit{margin:43px 70px 0;border-top:1px solid #9da7a3;padding-top:20px;display:grid;grid-template-columns:180px 1fr;gap:12px;font-size:20px;line-height:1.42}
.v11-limit b{color:#25555a}
.v11-benoit{margin-top:44px}
.v11-benoit>div:not(:first-child){padding-top:23px;padding-bottom:23px}
.v11-benoit p{font-size:21px;line-height:1.46}
.v11-benoit-quote{margin:54px 75px 0;font-family:inherit;font-size:29px;line-height:1.4;border-left:5px solid #9d493f;padding-left:25px}
.v11-benoit-quote b{color:#9d493f}
'''
(DECK / "style.css").write_text((DECK / "style.css").read_text(encoding="utf-8") + css, encoding="utf-8")
print("Built", DECK)
