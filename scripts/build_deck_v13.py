"""Reframe v12 around observable crisis messages, actions and audience responses."""
from pathlib import Path
from bs4 import BeautifulSoup
import json
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "versions" / "deck_v12"
TARGET = ROOT / "versions" / "deck_v13"
TARGET.mkdir(exist_ok=True)
for name in ["assets", "sources.html", "sources.csv", "동덕여대_sources.csv", "asset_sources.md", "카메룬_81개_변수_전수분석.md", "카메룬 위기 상황변수 목록.md", "deck_v12_참고문헌.md"]:
    src = SOURCE / name
    dst = TARGET / ("deck_v13_참고문헌.md" if name == "deck_v12_참고문헌.md" else name)
    if src.is_dir():
        shutil.copytree(src, dst, dirs_exist_ok=True)
    else:
        shutil.copy2(src, dst)
ref_path = TARGET / "deck_v13_참고문헌.md"
ref_path.write_text(ref_path.read_text(encoding="utf-8").replace("# deck_v12 참고문헌과 사건 자료", "# deck_v13 참고문헌과 사건 자료"), encoding="utf-8")

soup = BeautifulSoup((SOURCE / "index.html").read_text(encoding="utf-8"), "html.parser")
slides = soup.select("section.slide")
assert len(slides) == 15

def source_links(ids):
    return " · ".join(f'<a href="sources.html#{x}">{x}</a>' for x in ids)

def make_slide(n, section, kicker, title, body, ids, tone=""):
    node = slides[n - 1]
    node.attrs = {"class": ["slide", "paper-slide", "cc-slide"] + ([tone] if tone else []), "data-slide": str(n)}
    node.clear()
    markup = f'''<header class="folio"><span>{section}</span><span>CRISIS COMMUNICATION · 2024—2026</span></header>
<p class="deck-kicker">{kicker}</p><h2>{title}</h2>
<div class="cc-body">{body}</div>
<footer class="source-footer"><span>근거: {source_links(ids)} · 해석은 원문과 구분</span><span>{n:02d} / 15</span></footer>'''
    frag = BeautifulSoup(markup, "html.parser")
    node.extend(list(frag.contents))

slides[0].select_one("h1").replace_with(BeautifulSoup('<h1>대학의 설명은<br><em>왜 갈등을 멈추지 못했나</em></h1>', 'html.parser'))
slides[0].select_one(".cover-sub").string = "위기 메시지와 이해관계자 반응의 비교 분석"

make_slide(2, "01 / RESEARCH QUESTION", "분석 초점", "무엇을 말했고, 상대는 어떻게 반응했나", '''
<div class="cc-rq"><b>연구 질문</b><p>대학본부는 갈등이 커질 때 어떤 메시지와 대화 방식을 선택했는가? 그 뒤 공중의 요구와 반응은 어떻게 달라졌는가?</p></div>
<div class="cc-three"><article><strong>메시지</strong><p>발표 시점, 주장, 책임 인정 범위, 설명 대상</p></article><article><strong>행동</strong><p>면담, 논의 중단, 계획 수정처럼 확인 가능한 후속 조치</p></article><article><strong>반응</strong><p>표결·합의·재반발 등 관찰 가능한 반응. 신뢰 회복은 별도 입증</p></article></div>
<p class="cc-bottom">분석 단위는 ‘정책 결정’이 아니라 <b>발화 → 후속 행동 → 공중의 반응</b>이다. 공식 의결은 반응 지표 중 하나로만 사용한다.</p>''', ["A01P", "A02P", "D26", "D02", "D09", "D10"])

make_slide(3, "02 / THEORY & METHOD", "카메룬의 정황적 수용 이론", "입장은 상황에 따라 이동한다", '''
<p class="cc-lead">교재의 81개 변수(외부 24·내부 57)를 두 사례에 전수 적용했다. 본문은 실제 메시지 선택을 설명할 자료가 있는 세 조건을 추적한다.</p>
<div class="cc-rows"><div><b>공중의 상대적 힘 <small>E24</small></b><p>평의원회는 부결로 재협상을 요구했다. 학생은 집단행동과 총투표로 본부의 설명에 도전했다.</p></div><div><b>양보 가능한 수준 <small>E21</small></b><p>강원대의 인력 구성은 수정됐다. 동덕여대의 ‘여대 유지’ 요구와 전환 추진은 양립하기 어려웠다.</p></div><div><b>조직과 공중의 신뢰 <small>I56</small></b><p>늦은 자료 제공과 사전 설명 부족은 뒤늦은 해명의 수용 가능성을 낮추는 조건이었다.</p></div></div>
<p class="cc-bottom">‘요구의 조정 가능성’은 E21을 관찰하기 위해 만든 분석 지표다. 변수의 독립적인 인과 효과는 측정하지 않았다.</p>''', ["P99", "P01", "A03P", "D26"])

make_slide(4, "03 / EVIDENCE DESIGN", "사례와 자료의 범위", "두 위기에서 같은 순서를 본다", '''
<div class="cc-two"><article><h3>강원대–강릉원주대 통합</h3><p><b>발단</b> 신청서 선제출과 늦은 자료 전달</p><p><b>본부 대응</b> 사과·기한 설명·수정안 제시</p><p><b>공중 반응</b> 8:12 부결, 15:6 가결, 직원협의회 이의</p></article><article><h3>동덕여대 공학 전환</h3><p><b>발단</b> 공학 논의가 알려진 뒤 학생 반발</p><p><b>본부 대응</b> 단독 결정 부인·잠정 중단·공론화·전환 발표</p><p><b>공중 반응</b> 수업 재개 합의, 학생 총투표 85.7% 반대</p></article></div>
<p class="cc-bottom">대학 발표문·회의록은 본부의 발화와 조치를, 학생·직원 기록과 취재 보도는 반대 공중의 반응을 확인하는 데 사용했다.</p>''', ["A03P", "A01P", "A02P", "A07", "D26", "D02", "D09", "D10"])

make_slide(5, "04 / KANGWON · FIRST RESPONSE", "2025년 2월 28일 제46차 평의원회", "사과의 범위는 ‘자료 전달 지연’이었다", '''
<div class="cc-sequence"><div><span>상황</span><p>통합 신청서를 교육부에 먼저 냈다. 평의원은 257쪽 자료를 회의 이틀 전에 받아 충분히 검토하기 어렵다고 지적했다.</p></div><div><span>본부 발화</span><p>기획처장은 늦게 전달한 책임을 인정하며 사과했다. 이어 제출 기한의 긴급성을 설명하고 7쪽 요약본을 제시했다.</p></div><div><span>관찰된 반응</span><p>평의원회는 안건 심의를 보류했다. 사과와 요약 설명만으로 당일 심의 동의를 얻지 못했다.</p></div></div>
<div class="cc-reading"><b>카메룬 해석</b><p>기한 압박이 본부의 조기 제출을 이끌었고, 공중의 검토 권한이 설명 방식에 제약을 가했다. 신뢰의 정량 변화는 확인되지 않는다.</p></div>''', ["A03P"])

make_slide(6, "05 / KANGWON · SECOND RESPONSE", "2025년 4월 1일 제47차 평의원회", "보안과 기한 설명 뒤에도 8:12로 부결됐다", '''
<div class="cc-sequence"><div><span>본부 발화</span><p>총장은 협상 보안과 촉박한 제출 기한 때문에 사전 협의가 어려웠다고 해명하고, 구성원 의견을 충분히 받지 못한 데 양해를 구했다.</p></div><div><span>제시한 행동</span><p>수정 가능 항목은 뒤에 보완하겠다고 설명하며 조건부 가결을 요청했다.</p></div><div><span>공중의 응답</span><p>평의원은 신청서 내용과 의견 반영의 불확실성을 문제 삼았다. 출석 20명 중 찬성 8명·반대 12명으로 부결했다.</p></div></div>
<div class="cc-reading"><b>카메룬 해석</b><p>정부 사업 일정은 본부의 입장을 압박했지만, 평의원회의 제도적 힘은 ‘향후 수정’이라는 약속만으로 넘어가지 않았다.</p></div>''', ["A01P"])

make_slide(7, "06 / KANGWON · CORRECTIVE ACTION", "2025년 4월 28일 제48차 평의원회", "인력안은 바뀌었고, 수정의 의미는 다퉈졌다", '''
<div class="cc-sequence"><div><span>본부의 수정</span><p>대학혁신전략실 공무원 35명 구상을 공무원 24명·외부 전문가 11명으로 바꿔 설명했다. 총원 35명은 유지됐다.</p></div><div><span>공식 반응</span><p>평의원회는 수정안을 15:6으로 가결했다. 통합 절차는 진행됐다.</p></div><div><span>반대 공중의 반응</span><p>직원협의회는 실제 변경 폭이 작다고 비판했다. 본부의 ‘수정’과 직원의 ‘실질 변화’ 평가가 갈렸다.</p></div></div>
<div class="cc-reading"><b>카메룬 해석</b><p>조정 가능한 인력 구성에서 부분 수용이 있었다. 가결에 대한 인력 수정의 독립 효과나 직원 신뢰 회복은 단정할 수 없다.</p></div>''', ["A02P", "A04", "A07"])

make_slide(8, "07 / DONGDUK · INITIAL MESSAGE", "2024년 11월 15~18일", "본부는 ‘결정 전 논의’라고 설명했다", '''
<div class="cc-sequence"><div><span>첫 대상</span><p>11월 15일 대학은 학부모에게 사과하면서 점거·수업 차질을 강조했다. 학생에게 먼저 제기된 ‘사전 설명 부족’에는 직접 답하지 않았다.</p></div><div><span>11월 18일 발화</span><p>대학은 공학 전환이 교무위원회 의제화 전이었다며 ‘이미 단독 결정했다’는 학생 측 주장을 부인하고 소통 경과를 공개했다.</p></div><div><span>학생 요구</span><p>총학생회는 논의 자체의 중단과 사과를 요구했다. 본부의 절차 설명과 학생의 핵심 요구가 어긋났다.</p></div></div>
<div class="cc-reading"><b>카메룬 해석</b><p>높은 관련성과 집단행동이 있었지만 초기 메시지는 사실관계 해명과 질서 회복에 집중했다. 발화만으로 불신이 해소됐다는 근거는 없다.</p></div>''', ["D01", "D26"] , "cc-dongduk")

make_slide(9, "08 / DONGDUK · DIRECT DIALOGUE", "2024년 11월 21일 면담", "대면 협의가 잠정 중단 합의를 만들었다", '''
<div class="cc-sequence"><div><span>학생의 발화</span><p>총학생회는 남녀공학 전환 반대 의사를 면담에서 전달했다. 전날 학생총회에서도 압도적 반대가 표출됐다.</p></div><div><span>상호 조정</span><p>처장단과 학생대표가 약 3시간 면담했다. 본부는 공학 논의를 잠정 중단하고, 재개할 때 학생과 협의하겠다고 밝혔다.</p></div><div><span>관찰된 결과</span><p>본관을 제외한 강의실 봉쇄 해제와 수업 재개에 합의했다. 잠정 중단은 전환 계획의 영구 철회를 뜻하지 않는다.</p></div></div>
<div class="cc-reading"><b>카메룬 해석</b><p>학생의 동원력은 즉각적인 수업 정상화가 필요한 상황과 맞물려 본부의 입장을 잠시 수용 쪽으로 옮겼다.</p></div>''', ["D02", "D26"], "cc-dongduk")

make_slide(10, "09 / DONGDUK · DELIBERATION", "2025년 6~12월 공론화", "공론화는 진행됐지만 대표성에 이견이 남았다", '''
<div class="cc-sequence"><div><span>본부가 마련한 채널</span><p>교원·학생·직원·동문 대표로 공론화위를 꾸리고 숙의, 타운홀미팅, 온라인 조사를 진행했다.</p></div><div><span>대학의 해석</span><p>위원회는 공학 전환을 권고했다. 최종 조사에서는 교원·학생·직원 집단별 응답 비율을 같은 비중으로 합산해 공학 전환 51.8%를 제시했다.</p></div><div><span>쟁점</span><p>학생 응답자 다수는 여대 유지를 선택했다. 집단별 동일 가중을 둘러싸고 대학과 학생의 대표성 기준이 달랐다.</p></div></div>
<div class="cc-reading"><b>카메룬 해석</b><p>본부는 대화 채널을 넓혔지만, 누가 얼마나 대표되는지에 대한 불일치는 설명의 신뢰성을 계속 제약했다.</p></div>''', ["D05", "D06", "D07", "D08"], "cc-dongduk")

make_slide(11, "10 / DONGDUK · ANNOUNCEMENT & REPLY", "2025년 12월 3~9일", "우려를 인정한 전환 발표에 학생은 반대했다", '''
<div class="cc-sequence"><div><span>12월 3일 총장 입장문</span><p>권고를 존중한다며 공학 전환 추진을 밝혔다. 재학생의 우려를 인정하고 2029년 시행을 계획했으며 추가 설명을 약속했다.</p></div><div><span>12월 9일 학생 반응</span><p>총학생회는 총투표에서 반대 85.7%를 발표하고 공론화위의 구성·가중 방식을 비판했다. 전환 추진 중단을 요구했다.</p></div><div><span>대학의 재응답</span><p>대학은 학생 반대를 가볍게 여기지 않는다면서도, 다른 구성원 의견과 합의한 공론화 절차를 함께 존중해야 한다고 주장했다.</p></div></div>
<div class="cc-reading"><b>카메룬 해석</b><p>시행 시점 조정은 현재 재학생의 학업 환경에 대한 대응이다. 학생의 핵심 요구인 여대 유지는 수용하지 않았다.</p></div>''', ["D09", "D10", "D11"], "cc-dongduk")

make_slide(12, "11 / COMPARATIVE ANALYSIS", "발화와 행동의 이동", "두 대학은 공중의 힘에 다르게 반응했다", '''
<div class="cc-comparison"><div class="cc-comparison-head"><b>관찰 지점</b><b>강원대</b><b>동덕여대</b></div><div><b>초기 메시지</b><p>자료 지연 사과 뒤 보안·기한 해명</p><p>단독 결정 부인, 절차 경과 공개</p></div><div><b>압력이 작동한 순간</b><p>평의원회 8:12 부결</p><p>집단행동 뒤 대면 면담</p></div><div><b>실제 입장 이동</b><p>인력 구성 수정 후 재상정</p><p>논의 잠정 중단 후 공론화 재개</p></div><div><b>남은 충돌</b><p>직원협의회의 수정 폭 비판</p><p>학생의 대표성·여대 유지 요구</p></div></div>
<p class="cc-bottom">공중의 힘(E24), 양보 수준(E21), 기존 신뢰(I56)가 메시지 선택과 후속 행동을 제약했다는 사례 해석이다. 동일한 조건의 비교 실험은 아니다.</p>''', ["A01P", "A02P", "A07", "D02", "D09", "D10"])

make_slide(13, "12 / OUTCOMES & LIMITS", "위기 커뮤니케이션 성과 판정", "정책 진전과 신뢰 회복은 다른 결과다", '''
<div class="cc-three"><article><strong>확인: 대화의 결과</strong><p>강원대는 수정안을 재상정했다. 동덕여대는 면담 뒤 논의를 잠정 중단하고 수업 재개에 합의했다.</p></article><article><strong>확인: 남은 이견</strong><p>강원대 직원협의회는 수정 폭을 비판했다. 동덕여대 학생은 전환 발표 뒤 총투표로 반대했다.</p></article><article><strong>미확인: 회복 성과</strong><p>두 대학 모두 동일 공중의 신뢰를 전후로 측정한 자료가 없다. 공식 가결만으로 평판 회복을 말할 수 없다.</p></article></div>
<div class="cc-reading"><b>연구 결론</b><p>상황변수는 조직이 얼마나 양보할 수 있는지 설명한다. 위기 메시지의 효과는 발화 후 행동과 공중 반응을 함께 봐야 한다.</p></div>
<p class="cc-bottom">81개 변수의 항목별 판정과 근거는 연결된 전수분석 보고서에 보존했다.</p>''', ["A02P", "A07", "D02", "D10", "P99", "P01"])

make_slide(14, "13 / FINAL CHECK", "베노이트 이미지 회복 전략 · 최종 한 페이지", "발화의 전략과 회복 성과를 분리한다", '''
<div class="cc-comparison cc-benoit"><div class="cc-comparison-head"><b>사례</b><b>발화의 전략</b><b>조치와 관찰 결과</b></div><div><b>강원대</b><p>자료 전달 지연에 <b>제한적 사과</b>. 이후 인력 구성 변경을 제시해 <b>시정조치</b>를 약속했다.</p><p>수정안 15:6 가결. 직원협의회는 수정 폭을 비판했다. 신뢰 회복은 미확인.</p></div><div><b>동덕여대</b><p>‘이미 단독 결정’ 주장에 <b>제한적 부인</b>. 여성교육 성과를 강조하며 전환의 의미를 재해석했다.</p><p>논의 잠정 중단과 공론화를 시행했다. 이후 학생 총투표 85.7% 반대. 신뢰 회복은 미확인.</p></div></div>
<p class="cc-bottom">베노이트는 최종 단계에서 메시지의 수사 전략을 분류한다. 입장 이동의 조건과 공중 반응 분석은 카메룬의 상황변수에 근거한다.</p>''', ["BEN", "A03P", "A02P", "A07", "D26", "D09", "D10"])

# Keep the verified bibliography, with updated framing and local links.
slides[14].select_one(".deck-kicker").string = "이론 문헌과 핵심 원문"
slides[14].select_one("h2").string = "참고문헌과 전수분석"
slides[14].select_one(".source-footer span").string = "전체 서지·원문 링크: deck_v13_참고문헌.md 및 sources.html"
evidence_rows = slides[14].select(".v9-bib-row.evidence")
evidence_rows[0].span.clear()
evidence_rows[0].span.append(BeautifulSoup("제46·47·48차 평의원회 회의록 · 통합안 공식 설명 · 직원협의회 반응 <small>A03P · A01P · A02P · A04 · A07</small>", "html.parser"))
evidence_rows[1].span.clear()
evidence_rows[1].span.append(BeautifulSoup("학부모 대상 글 · 본부 소통 일지 · 논의 잠정 중단 합의 <small>D01 · D26 · D02</small>", "html.parser"))
evidence_rows[2].span.clear()
evidence_rows[2].span.append(BeautifulSoup("공론화 권고 · 결과 자료 · 총장 입장문 · 학생 총투표와 대학 재응답 <small>D06 · D07 · D09 · D10 · D11</small>", "html.parser"))
evidence_rows[3].decompose()

for i, node in enumerate(slides, 1):
    node["data-slide"] = str(i)

titles = [x.find(["h1", "h2"]).get_text(" ", strip=True) for x in slides]
for i, button in enumerate(soup.select(".toc-item"), 1):
    button.string = f"{i:02d} · {titles[i-1]}"

for a in soup.select("#controls a[href]"):
    a["href"] = a["href"].replace("deck_v12.pdf", "deck_v13.pdf")
soup.title.string = "위기 메시지와 공중 반응 | 발표 덱 v13"

# Obsolete number modal content and archive details are replaced with the new evidence focus.
modal = soup.select_one("#data-modal")
if modal:
    body = modal.find(["div"], class_="data-grid")
    if body: body.decompose()
    modal.append(BeautifulSoup('<div class="cc-modal-copy"><p>수치의 분모와 의미: 강원대 8:12는 제47차 평의원회 출석 20명, 15:6은 제48차 출석 21명의 표결이다. 동덕여대 51.8%는 교원·학생·직원 집단별 동일 가중을 적용한 공학 전환 선택률이다. 학생 총투표의 85.7% 반대는 별도 조사 결과다.</p><p>각 수치의 원문은 원자료 링크에서 확인할 수 있다.</p></div>', 'html.parser'))

(TARGET / "index.html").write_text(str(soup).replace("deck_v12.pdf", "deck_v13.pdf"), encoding="utf-8")

css = (SOURCE / "style.css").read_text(encoding="utf-8")
css += '''
/* v13: flat, readable evidence layouts */
.cc-slide .cc-body{margin:38px 84px 0 84px;color:#172c30}
.cc-slide .source-footer{font-size:16px}
.cc-slide .source-footer a{text-decoration:underline;text-underline-offset:3px}
.cc-slide h2{font-size:48px;line-height:1.23;max-width:1360px}
.cc-lead{font-size:23px;line-height:1.5;max-width:1320px;margin:0 0 28px}
.cc-rq{display:grid;grid-template-columns:175px 1fr;gap:30px;padding:23px 0;border-top:3px solid #24575c;border-bottom:1px solid #9aaca9;font-size:28px;line-height:1.5}
.cc-rq b{font-size:22px;color:#24575c}.cc-rq p{margin:0}
.cc-three{display:grid;grid-template-columns:repeat(3,1fr);gap:34px;margin-top:39px}
.cc-three article{border-top:3px solid #9d493f;padding-top:14px;min-height:170px}.cc-three strong{font:800 27px var(--serif)}.cc-three p{font-size:21px;line-height:1.42;margin:15px 0 0}
.cc-bottom{border-top:1px solid #a5aca5;margin:33px 0 0;padding-top:15px;font-size:20px;line-height:1.45;color:#4a5553}
.cc-rows{border-top:3px solid #24575c}.cc-rows>div{display:grid;grid-template-columns:340px 1fr;gap:30px;border-bottom:1px solid #a5aca5;padding:22px 0}.cc-rows b{font:800 26px var(--serif)}.cc-rows small{font:800 17px var(--sans);color:#9d493f}.cc-rows p{font-size:22px;margin:0}
.cc-two{display:grid;grid-template-columns:1fr 1fr;gap:54px}.cc-two article{border-top:4px solid #24575c;padding-top:15px}.cc-two article:nth-child(2){border-color:#9d493f}.cc-two h3{font-size:32px;margin:0 0 26px}.cc-two p{font-size:22px;border-bottom:1px solid #b4b9b0;padding:14px 0;margin:0}.cc-two b{display:inline-block;width:120px;color:#24575c}
.cc-sequence{border-top:3px solid #24575c}.cc-sequence>div{display:grid;grid-template-columns:210px 1fr;gap:27px;align-items:start;border-bottom:1px solid #aeb7b1;padding:20px 0}.cc-sequence span{font:800 24px var(--serif);color:#24575c}.cc-sequence p{font-size:23px;line-height:1.46;margin:0}
.cc-reading{display:grid;grid-template-columns:190px 1fr;gap:26px;background:#e6e6dc;padding:18px 24px;margin-top:30px;border-left:5px solid #9d493f}.cc-reading b{font-size:21px;color:#9d493f}.cc-reading p{font-size:20px;line-height:1.42;margin:0}
.cc-dongduk .cc-sequence{border-color:#9d493f}.cc-dongduk .cc-sequence span{color:#9d493f}
.cc-comparison{border-top:3px solid #24575c}.cc-comparison>div{display:grid;grid-template-columns:240px 1fr 1fr;gap:24px;border-bottom:1px solid #aeb7b1;padding:17px 0;align-items:start}.cc-comparison>div>b{font-size:22px}.cc-comparison p{font-size:21px;line-height:1.4;margin:0}.cc-comparison-head{background:#dfe6e0;padding:12px 16px!important}.cc-comparison-head b{font-size:19px!important;color:#24575c}.cc-benoit>div{grid-template-columns:165px 1fr 1fr}.cc-benoit>div:not(:first-child){padding:28px 0}.cc-benoit p{font-size:23px}.cc-modal-copy{font-size:19px;line-height:1.6;padding:24px}
'''
(TARGET / "style.css").write_text(css, encoding="utf-8")

notes = [
"두 사례의 공식 결정은 진전됐지만, 메시지의 효과는 발화 후 공중 반응에서 따로 살핍니다.",
"연구 질문은 메시지, 조치, 반응의 순서를 묻습니다. 의결만으로 위기 커뮤니케이션 성공을 판단하지 않습니다.",
"81개 변수는 전수분석 보고서에 보존했습니다. 발표에서는 공중의 힘, 양보 수준, 기존 신뢰가 입장 이동을 설명하는지 확인합니다.",
"회의록과 공식 입장은 본부 발화의 근거입니다. 반대 공중의 반응은 별도 기록과 보도에서 대조했습니다.",
"제46차 회의록에서 257쪽 자료가 이틀 전 전달됐다는 지적과 기획처장의 사과, 심의 보류를 확인할 수 있습니다.",
"제47차에서 총장은 협상 보안과 제출 기한을 설명했습니다. 발언과 약속 뒤에도 표결은 8대12 부결이었습니다.",
"공무원 35명 구상을 공무원 24명과 외부 전문가 11명으로 바꿨습니다. 직원협의회는 실제 수정 폭이 작다고 보았습니다.",
"11월 15일 학부모 대상 글과 18일 구성원 대상 설명은 수신자와 강조점이 다릅니다. 총학생회는 논의 중단과 사과를 요구했습니다.",
"11월 21일 대면 면담 뒤 본부가 논의를 잠정 중단했고 수업 재개에 합의했습니다. 영구 철회와는 구분합니다.",
"공론화위는 집단별 동일 가중을 적용했습니다. 학생 응답자 다수의 여대 유지 선택과 위원회 권고를 동시에 보여줍니다.",
"12월 3일 총장 입장문은 우려를 인정하면서 전환 추진을 발표했습니다. 12월 9일 학생은 총투표 반대와 대표성 비판을 제기했습니다.",
"강원대의 공식 심의권과 동덕여대 학생의 동원력은 다른 힘입니다. 두 대학 모두 후속 설명에 대한 이의가 남았습니다.",
"관찰 가능한 합의와 반대는 확인되지만, 동일 공중의 신뢰 전후 측정은 없습니다. 정책 진전을 평판 회복으로 대체하지 않습니다.",
"베노이트는 한 장에서 발화 전략만 분류합니다. 조건은 카메룬으로, 결과는 실제 조치와 공중 반응으로 판정합니다.",
"모든 핵심 수치는 원문 인덱스에 연결했습니다. 81개 변수별 중요도는 별도 전수분석 보고서에 있습니다."
]
js = (SOURCE / "slides.js").read_text(encoding="utf-8")
array = "const SPEAKER_NOTES = " + json.dumps([{"title": titles[i], "script": note, "qa": "근거와 해석을 구분하고, 신뢰 회복은 측정 자료가 있을 때만 판정합니다."} for i, note in enumerate(notes)], ensure_ascii=False, indent=2) + ";\n\n"
js = re.sub(r"const SPEAKER_NOTES = \[.*?(?=function fitStage\(\))", array, js, flags=re.S)
js = re.sub(r"window\.ARCHIVE_DETAILS\s*=\s*\[.*?\];", "window.ARCHIVE_DETAILS = [];", js, flags=re.S)
(TARGET / "slides.js").write_text(js, encoding="utf-8")

sources = (TARGET / "sources.html").read_text(encoding="utf-8").replace("발표 v12", "발표 v13").replace("(v12)", "(v13)").replace("슬라이드(v5)", "슬라이드(v13)")
(TARGET / "sources.html").write_text(sources, encoding="utf-8")
(TARGET / "README.md").write_text("""# 발표덱 v13\n\n강원대 통합과 동덕여대 공학 전환에서 대학본부의 실제 메시지, 후속 행동, 공중의 반응을 비교한 15장 HTML 덱이다. 카메룬의 상황변수로 전개하고 베노이트는 14장 한 페이지에서만 다룬다.\n\n- [발표 열기](index.html) · [PDF](deck_v13.pdf)\n- [81개 변수 전수분석](카메룬_81개_변수_전수분석.md) · [원문 인덱스](sources.html)\n\n공식 가결과 정책 진전은 신뢰 회복 지표로 해석하지 않는다. 전체 사례의 평판 변화나 메시지의 독립 효과는 측정되지 않았다.\n""", encoding="utf-8")
print(f"Built {len(slides)} slides in {TARGET}")
