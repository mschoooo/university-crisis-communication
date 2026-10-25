# -*- coding: utf-8 -*-
"""Build v15 from v14 while retaining its documentary layouts."""
from pathlib import Path
from bs4 import BeautifulSoup
import json
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "versions/deck_v14"
DST = ROOT / "versions/deck_v15"
shutil.copytree(SRC, DST, dirs_exist_ok=True)
(DST / "deck_v14.pdf").unlink(missing_ok=True)
(DST / "deck_v14_참고문헌.md").unlink(missing_ok=True)
soup = BeautifulSoup((SRC / "index.html").read_text(encoding="utf-8"), "html.parser")
slides = soup.select("section.slide")
assert len(slides) == 15


def refs(*ids):
    return " · ".join(f'<a href="sources.html#{x}">{x}</a>' for x in ids)


def replace_slide(n, section, kicker, title, body, ids):
    slide = slides[n - 1]
    slide.attrs = {"class": ["slide", "paper-slide", "v14-slide", "v15-slide"], "data-slide": str(n)}
    slide.clear()
    html = f'''<header class="folio"><span>{section}</span><span>CAMERON · MESSAGE · ACTION · RESPONSE</span></header>
<p class="deck-kicker">{kicker}</p><h2>{title}</h2><div class="v15-body">{body}</div>
<footer class="source-footer"><span>원자료 {refs(*ids)} · 관찰과 해석 구분</span><span>{n:02d} / 15</span></footer>'''
    slide.extend(BeautifulSoup(html, "html.parser").contents)


replace_slide(3, "02 / THEORY & METHOD", "카메론의 정황적 수용 이론", "외부·내부 조건으로 대응 범위를 읽는다", '''
<div class="v15-taxonomy"><div><b>외부 변수 <em>24</em></b><p>위협 5 · 업계 현황 3 · 정치·사회 환경 2<br><strong>외부 공중 14</strong></p></div><div><b>내부 변수 <em>57</em></b><p>조직 15 · PR부서 13 · 의사결정체 8<br>내부 위협 3 · 개인 16 · <strong>관계성 2</strong></p></div></div>
<p class="v15-method">81개 전체를 사건에 적용한 것은 아니다. 공개 기록에서 <strong>공중의 영향력·요구 조정 범위·기존 관계</strong>와 연결되는 세 항목을 선별했다.</p>
<div class="v15-vars"><div><span>E24 · 외부 공중 14</span><b>공중의 상대적인 힘</b><p>평의원회 부결과 학생 집단행동·총투표가 대응의 맥락을 형성했다.</p></div><div><span>E21 · 외부 공중 11</span><b>공중의 양보할 수 있는 수준</b><p>인력안은 수정됐으나, 여대 유지 요구와 공학 전환은 충돌했다.</p></div><div><span>I56 · 관계성 1</span><b>공중과 조직 사이의 신뢰감 정도</b><p>사전 설명·자료 공개를 둘러싼 이의가 있었다. 신뢰 수준 자체는 측정하지 않았다.</p></div></div>
<p class="v15-caveat">E·I 코드는 교재 원문 표기가 아니라 81개 목록의 분석용 순번이다. <a href="카메론 위기 상황변수 목록.md">교재 표 2-5 전사</a>의 ‘기업·외부 공중’ 변수를 대학 구성원 사례에 맞춰 제한적으로 읽었다.</p>
''', ["P99", "P01", "A03P", "D26"])

replace_slide(4, "03 / CASE BACKGROUND", "구조개편 배경과 초기 위험 징후", "두 사안 모두 결정 과정이 쟁점이 됐다", '''
<div class="v15-parallel"><article><span class="v15-case">강원대–강릉원주대 통합</span><strong>통합 신청·심의 일정</strong><p>대학은 통합과 재정지원·신청 기한을 설명했다. 인력 배치 등 실행안은 평의원회 심의 대상이었다.</p><div class="v15-early"><b>초기 징후</b><p><em>2.20</em> 신청서 선제출 → <em>2.26</em> 257쪽 자료 전달 → <em>2.28</em> 사의 보류. 심의 시간과 권한을 둘러싼 이의가 기록됐다.</p></div></article>
<article><span class="v15-case">동덕여대 공학 전환</span><strong>학령인구·대학 운영 논의</strong><p>대학은 전환 검토의 배경으로 운영 환경 변화를 제시했다. 경제적 생존 위기 자체는 이 자료만으로 판정하지 않는다.</p><div class="v15-early"><b>초기 징후</b><p><em>2024.11</em> 공학 논의가 알려지고 학생들이 사전 협의와 결정권을 문제 삼았다. 11.11 면담 취소를 둘러싼 설명도 엇갈렸다.</p></div></article></div>
<p class="v15-read">공통 질문: <strong>검토 단계에서 누가 무엇을 언제 알았고, 어떤 요구를 결정 전에 반영할 수 있었나?</strong></p>
''', ["A03P", "A04", "D26", "D01"])

# Keep v14's enlarged quotes, images, document excerpts and data charts. Add one short
# Cameron condition inside each existing analysis area, never as a competing card.
context = {
    5: "카메론 조건: 짧은 심의 일정과 자료 접근에 대한 이의가 사과 뒤의 설명 범위를 제한했다.",
    6: "카메론 E24: 평의원회의 공식 부결은 수정안 제시를 요구할 수 있는 힘을 드러냈다.",
    7: "카메론 E21: 수정 가능한 인력 구성은 조정됐지만 직원협의회의 요구가 모두 수용된 것은 아니다.",
    8: "카메론 I56: 사전 협의에 관한 이의가 ‘결정 전 논의’라는 해명의 수용 조건이었다.",
    9: "카메론 E24·E21: 학생의 집단행동 뒤 논의가 멈췄다. 여대 유지 요구 수용은 확인되지 않는다.",
    10: "카메론 E24: 집단별 가중치가 달라 대표성과 공중의 상대적 힘을 둘러싼 쟁점이 남았다.",
    11: "카메론 E21·I56: 2029년은 기존 전환 일정이며, 학생의 여대 유지 요구 수용이나 신뢰 회복의 근거가 아니다.",
}
for n, statement in context.items():
    slide = slides[n - 1]
    slide["class"] = list(slide.get("class", [])) + ["v15-context-slide"]
    # Existing takeaway/caption already occupies the bottom. Use a compact fixed
    # strip between the body and source footer, leaving the documentary layout intact.
    footer = slide.select_one(".source-footer")
    footer.insert_before(BeautifulSoup(f'<p class="v15-context">{statement}</p>', "html.parser"))

replace_slide(12, "11 / DIRECT COMPARISON", "카메론: 대응 선택의 조건", "조정 가능한 범위가 대응을 갈랐다", '''
<div class="v15-comparison"><div class="head"><b>비교 질문</b><b>강원대 통합</b><b>동덕여대 전환</b></div>
<div><b>대응 조건</b><p>심의권을 가진 평의원회 부결(E24)<br>인력안 수정 여지(E21)</p><p>학생 집단행동·대표성 논쟁(E24)<br>여대 유지와 전환 추진 충돌(E21)</p></div>
<div><b>메시지·행동</b><p>자료 지연 사과·기한 해명 → 인력 구성 수정 후 재상정</p><p>결정 전 논의 해명 → 면담·잠정 중단·공론화·전환 발표</p></div>
<div><b>요구 반영</b><p><strong>인력 구성 일부 수정</strong><br>직원협의회는 수정 폭 비판</p><p><strong>논의 중단·수업 재개 합의</strong><br>여대 유지 요구 수용은 확인되지 않음</p></div>
<div><b>공식 결정 ≠ 구성원 반응</b><p>평의원회 <strong>15:6 가결</strong> / 직원협의회 이의 지속</p><p>전환 추진 발표 / 학생 총투표 <strong>85.7% 반대</strong></p></div></div>
''', ["A03P", "A01P", "A02P", "A07", "D02", "D07", "D09", "D10"])

replace_slide(13, "12 / EVIDENCE LIMITS", "확인된 변화와 남은 간극", "공식 통과와 구성원 수용은 다르다", '''
<div class="v15-results"><div><span>강원대</span><b>공식 결정</b><p>수정안 재상정 뒤 평의원회 15:6 가결</p><b>구성원 반응</b><p>직원협의회는 수정 범위에 이의를 제기</p></div><div><span>동덕여대</span><b>확인된 조치</b><p>논의 잠정 중단·수업 재개 합의, 이후 전환 추진 발표</p><b>구성원 반응</b><p>발표 뒤 학생 총투표 85.7% 반대</p></div></div>
<div class="v15-limit"><strong>판정 유보</strong><p>같은 공중의 신뢰를 전후로 측정한 자료가 없다. 결정·발표·표결의 시간 순서만으로 메시지의 독립적 효과나 신뢰 회복을 단정할 수 없다.</p></div>
''', ["A02P", "A07", "D02", "D09", "D10"])

replace_slide(14, "13 / CONCLUSION & PRACTICE", "사전 이슈관리 · 절차적 공정성", "결정 전에 참여 규칙을 공개하라", '''
<p class="v15-conclusion">카메론은 <strong>왜 대응 범위가 달랐는지</strong>, 실제 발언에 한정한 베노이트는 <strong>어떻게 설명했는지</strong>를 읽게 한다. 두 사례의 실무 과제는 결정 이전의 정보와 참여 절차에 있다.</p>
<div class="v15-actions"><div><b>01</b><strong>초기 정보공개</strong><p>검토안·일정·원문·수정 가능한 항목을 심의 전에 공개</p></div><div><b>02</b><strong>사전 협의</strong><p>결정 이전에 공중별 요구를 받고 응답 기한을 명시</p></div><div><b>03</b><strong>대표성 합의</strong><p>누가 참여·대표하는지, 결정권이 어디에 있는지 사전 합의</p></div><div><b>04</b><strong>집계 규칙 공개</strong><p>집단별 비율·가중치·이견 기록·이의 절차를 투표 전에 제시</p></div><div><b>05</b><strong>후속 조치 추적</strong><p>요구별 반영·미반영 이유와 시행 결과를 같은 공중에 보고</p></div></div>
<p class="v15-caveat">이는 관찰된 자료 지연·합의 범위·대표성 논쟁에 근거한 제언이다. 효과가 입증된 처방이라는 뜻은 아니다.</p>
''', ["A03P", "A07", "D02", "D07", "D10"])

# Bibliography receives usable vertical space; retain the v14 source list.
last = slides[14]
last["class"] = list(last.get("class", [])) + ["v15-references"]
last.select_one(".deck-kicker").decompose()
last.select_one("h2").string = "참고문헌 · 사건 원문"
last.select_one(".source-footer span").string = "전체 서지·원문: deck_v15_참고문헌.md · sources.html"
bib = last.select_one(".v9-bibliography")
anchor = bib.select_one(".v9-bib-title.evidence")
for html in [
    '<div class="v9-bib-row"><b>Heath (1997)</b><span><i>Strategic Issues Management: Organizations and Public Policy Challenges.</i> Sage.</span></div>',
    '<div class="v9-bib-row"><b>Leventhal (1980)</b><span>“What Should Be Done with Equity Theory?” In <i>Social Exchange: Advances in Theory and Research</i>, 27–55.</span></div>',
]:
    anchor.insert_before(BeautifulSoup(html, "html.parser"))

titles = [s.find(["h1", "h2"]).get_text(" ", strip=True) for s in slides]
for n, button in enumerate(soup.select(".toc-item"), 1):
    button.string = f"{n:02d} · {titles[n-1]}"
for a in soup.select("#controls a[href]"):
    a["href"] = a["href"].replace("deck_v14.pdf", "deck_v15.pdf")
soup.title.string = "대학 구조개편 갈등의 위기 커뮤니케이션 | deck_v15"
(DST / "index.html").write_text(str(soup).replace("deck_v14", "deck_v15"), encoding="utf-8")

css = (SRC / "style.css").read_text(encoding="utf-8")
css += '''
/* v15: compact analytical context on the v14 documentary canvas */
.v15-slide .folio{border-bottom:0}.v15-slide .deck-kicker{margin-top:23px;font-size:19px}.v15-slide h2{font-size:46px;line-height:1.2}.v15-body{margin:29px 72px 0}.v15-slide .source-footer{font-size:15px}
.v15-taxonomy{display:grid;grid-template-columns:1fr 1fr;gap:28px}.v15-taxonomy>div{background:#e7ece6;padding:18px 24px}.v15-taxonomy>div:last-child{background:#eeeae1}.v15-taxonomy b{font:800 25px var(--serif);color:var(--teal)}.v15-taxonomy em{font-style:normal;color:var(--brick)}.v15-taxonomy p{font-size:19px;line-height:1.44;margin:8px 0 0}.v15-method{font-size:20px;margin:20px 0}.v15-vars{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}.v15-vars>div{border-top:4px solid var(--teal);padding-top:10px}.v15-vars>div:nth-child(2){border-color:var(--brick)}.v15-vars>div:nth-child(3){border-color:#59635b}.v15-vars span{font-size:16px;color:var(--teal);font-weight:800}.v15-vars b{display:block;font:800 23px var(--serif);margin:5px 0}.v15-vars p{font-size:19px;line-height:1.36;margin:0}.v15-caveat{font-size:16px;color:#52605a;margin:18px 0 0;line-height:1.35}
.v15-parallel{display:grid;grid-template-columns:1fr 1fr;gap:36px}.v15-parallel article{background:#f2f1e9;padding:25px 29px;min-height:423px}.v15-parallel article:last-child{background:#e6ece8}.v15-case{display:block;color:var(--teal);font-size:19px;font-weight:800}.v15-parallel strong{display:block;font:800 29px var(--serif);margin:12px 0}.v15-parallel p{font-size:21px;line-height:1.43;margin:0}.v15-early{border-top:3px solid var(--brick);margin-top:26px;padding-top:14px}.v15-early b{font-size:19px;color:var(--brick)}.v15-early p{margin-top:8px}.v15-early em{font-style:normal;font-weight:800;color:var(--teal)}.v15-read{font-size:22px;margin-top:19px}
.v15-context-slide .v14-body{margin-top:26px}.v15-context-slide .v14-split{height:515px}.v15-context-slide[data-slide="7"] .v14-evidence-bottom{margin-top:22px}.v15-context-slide[data-slide="10"] .v14-wide-clip img{height:207px}.v15-context{position:absolute;left:72px;right:72px;bottom:66px;margin:0;padding:8px 12px;background:#e7ece7;color:#284b49;font-size:17px;line-height:1.3;font-weight:700}.v15-context-slide[data-slide="7"] .v15-context,.v15-context-slide[data-slide="10"] .v15-context{bottom:62px}
.v15-comparison{border-top:3px solid var(--teal)}.v15-comparison>div{display:grid;grid-template-columns:230px 1fr 1fr;gap:25px;padding:12px 10px;border-bottom:1px solid #bdc4ba}.v15-comparison .head{background:#e0e9e4;padding:13px 10px}.v15-comparison b{font-size:20px;color:var(--teal)}.v15-comparison p{font-size:20px;line-height:1.37;margin:0}.v15-comparison strong{color:var(--brick)}
.v15-results{display:grid;grid-template-columns:1fr 1fr;gap:35px}.v15-results>div{background:#e7ece7;padding:28px 34px;min-height:372px}.v15-results>div:last-child{background:#eeeae2}.v15-results span{font:800 28px var(--serif);display:block;margin-bottom:22px}.v15-results b{font-size:18px;color:var(--teal)}.v15-results p{font-size:23px;line-height:1.4;margin:6px 0 22px}.v15-limit{display:grid;grid-template-columns:175px 1fr;gap:25px;align-items:start;margin-top:24px;background:#f0eee7;padding:18px 24px}.v15-limit strong{font:800 25px var(--serif);color:var(--brick)}.v15-limit p{font-size:21px;line-height:1.44;margin:0}
.v15-conclusion{font-size:24px;line-height:1.44;background:#e7ece7;padding:20px 26px;margin:0 0 20px}.v15-actions{display:grid;grid-template-columns:repeat(5,1fr);gap:16px}.v15-actions>div{border-top:4px solid var(--teal);padding-top:12px}.v15-actions>div:nth-child(even){border-color:var(--brick)}.v15-actions b{display:block;font:800 28px var(--serif);color:var(--brick)}.v15-actions strong{display:block;font-size:21px;margin:7px 0}.v15-actions p{font-size:19px;line-height:1.38;margin:0}
.v15-references .deck-kicker{display:none}.v15-references h2{font-size:29px;margin-top:24px}.v15-references .v9-bibliography{margin-top:12px}.v15-references .v9-bib-row{padding-top:7px;padding-bottom:7px}.v15-references .v9-bib-title{margin-top:8px}
'''
(DST / "style.css").write_text(css, encoding="utf-8")

js = (SRC / "slides.js").read_text(encoding="utf-8")
notes = [
    "교재의 외부 24·내부 57개 변수 가운데 원문으로 논의할 수 있는 E24·E21·I56을 고릅니다. 코드 자체는 교재가 아닌 이 분석의 순번입니다.",
    "강원대는 통합 일정과 사전 자료 제공이, 동덕여대는 공학 논의의 사전 협의와 대표성이 초기 쟁점입니다. 배경 설명은 대학의 주장으로 표시합니다.",
    "자료 전달 지연에 관한 제한적 사과입니다. 발언의 범위만 베노이트로 분류하고, 카메론은 일정·심의 조건을 읽는 데 씁니다.",
    "평의원회 공식 부결은 공중의 상대적 힘을 보여줍니다. 표결 자체가 다음 수정의 단일 원인이라는 뜻은 아닙니다.",
    "인력안의 일부 수정과 공식 가결은 확인됩니다. 직원협의회 이의가 이어졌다는 점도 함께 설명합니다.",
    "대학의 '결정 전 논의' 설명과 학생 요구를 나란히 봅니다. 제한적 부인 분류는 이 실제 발언에만 붙입니다.",
    "면담 뒤 잠정 중단과 수업 재개가 합의됐습니다. 여대 유지 요구가 수용된 것은 아닙니다.",
    "51.8%와 71.3%는 분모와 가중치가 다릅니다. 집계 규칙과 대표성 논쟁을 읽습니다.",
    "2029년 전환 시점은 기존 계획입니다. 학생 반대가 이후 총투표로 확인됐고 신뢰 회복은 측정되지 않았습니다.",
    "카메론의 대응 조건과 실제 메시지·행동을 직접 비교합니다. 공식 결정과 구성원 반응을 별도 열로 읽습니다.",
    "확인된 행동 변화와 남은 이견을 구분합니다. 시간적 선후로 인과관계를 확정할 수 없습니다.",
    "사전 이슈관리와 절차적 공정성의 관점에서 초기 정보, 협의, 대표성, 집계, 후속 조치를 제안합니다.",
    "서지와 사건 원문의 증거 수준을 구분했습니다. 자세한 원문은 자료 ID로 확인할 수 있습니다.",
]
speaker = json.loads(re.search(r"const SPEAKER_NOTES = (\[.*?\]);\s*function fitStage", js, re.S).group(1))
for n, note in enumerate(notes, 3):
    speaker[n-1]["title"] = titles[n-1]
    speaker[n-1]["script"] = note
js = re.sub(r"const SPEAKER_NOTES = \[.*?(?=function fitStage\(\))", "const SPEAKER_NOTES = " + json.dumps(speaker, ensure_ascii=False, indent=2) + ";\n\n", js, flags=re.S)
(DST / "slides.js").write_text(js, encoding="utf-8")

for filename in ["README.md", "asset_sources.md", "sources.html", "deck_v14_참고문헌.md"]:
    source = SRC / filename
    if source.exists():
        dest = DST / filename.replace("deck_v14", "deck_v15")
        dest.write_text(source.read_text(encoding="utf-8").replace("deck_v14", "deck_v15"), encoding="utf-8")
ref = DST / "deck_v15_참고문헌.md"
if ref.exists():
    content = ref.read_text(encoding="utf-8")
    content = content.replace("14장 발화 전략 분류에만 사용", "실제 발언이 확인되는 5·8·11장의 발화 전략 분류에만 사용")
    content += "\n## 추가로 복원한 기존 관점\n\n- Heath, R. L. (1997). *Strategic Issues Management: Organizations and Public Policy Challenges*. Sage.\n- Leventhal, G. S. (1980). What Should Be Done with Equity Theory? In *Social Exchange: Advances in Theory and Research* (pp. 27–55). Plenum.\n- E21·E24·I56은 교재 표에 인쇄된 코드가 아니라 제공된 81개 목록의 순차적 분석 코드다.\n"
    ref.write_text(content, encoding="utf-8")
(DST / "README.md").write_text("# deck_v15\n\n`deck_v14`의 원문·사진·수치 레이아웃에 `deck_v9`의 카메론 변수 체계, 사례 배경 비교, 사전 이슈관리와 절차적 공정성 관점을 결합한 15장 발표 자료.\n\n- [발표 보기](index.html) · [PDF](deck_v15.pdf) · [원문 색인](sources.html)\n- E21·E24·I56 코드는 교재 원문이 아닌 분석용 순번이다.\n", encoding="utf-8")
print(f"Built {len(slides)} slides at {DST}")
