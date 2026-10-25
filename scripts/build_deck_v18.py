# -*- coding: utf-8 -*-
"""Apply the final evidence-bounded evaluation to deck_v17."""
from pathlib import Path
from bs4 import BeautifulSoup
import json, re, shutil

ROOT = Path(__file__).resolve().parents[1]
SRC, DST = ROOT / "versions/deck_v17", ROOT / "versions/deck_v18"
shutil.copytree(SRC, DST, dirs_exist_ok=True)
for name in ("deck_v17.pdf", "deck_v17_참고문헌.md"):
    (DST / name).unlink(missing_ok=True)
soup = BeautifulSoup((SRC / "index.html").read_text(encoding="utf-8"), "html.parser")
slides = soup.select("section.slide")
assert len(slides) == 15

def put(node, html):
    node.clear()
    node.extend(BeautifulSoup(html, "html.parser").contents)

s4, s10, s11, s12, s13, s14 = [slides[i-1] for i in (4, 10, 11, 12, 13, 14)]
put(s4.select_one(".v15-method"), "선정 기준: ① 두 사례 기록에서 관찰 가능 ② 대응 선택·수정·반응과 관련 ③ 원문과 대조 가능. 81개 중 E24·E21·I56을 분석의 초점으로 삼았다.")
put(s4.select_one(".v15-vars"), '''
<div><span>E24 · 외부 공중 14</span><b>공중의 상대적인 힘</b><p>평의원회 부결과 학생 집단행동·총투표 등 기록으로 확인되는 영향력에 한정한다.</p></div>
<div><span>E21 · 외부 공중 11</span><b>공중의 양보할 수 있는 수준</b><p>원문은 ‘양보 수준’이다. 인력안 수정과 여대 유지 요구의 충돌을 협상 여지로 개념적으로 읽는다. 수준 자체를 측정한 값은 없다.</p></div>
<div><span>I56 · 관계성 1</span><b>공중과 조직 사이의 신뢰감 정도</b><p>사전 협의·자료 제공 이의는 관계 갈등의 단서다. 신뢰 수준이나 전후 변화의 측정치는 아니다.</p></div>''')
put(s4.select_one(".v15-caveat"), 'E·I는 교재 원문 코드가 아닌 분석용 순번이다. <a href="카메론 위기 상황변수 목록.md">교재 표 2-5 전사</a>와 대조했다. 선정 변수는 대응을 읽는 조건이며, 결과의 원인으로 단정하지 않는다.')

s10.select_one(".v14-number-pair div:first-child small").string = "교원·학생·직원 응답값을 1:1:1 동일 비중 적용"
put(s10.select_one(".v14-take"), "공론화위는 집단별 동일 비중을 적용해 공학 전환 51.8%를 제시했다. 학생 측은 응답자 수와 대표성이 결과에 반영되는 방식에 이의를 제기했다.")
put(s10.select_one(".v15-context"), "카메론 E24: 최종조사는 교원·학생·직원 응답값을 1:1:1로 집계했다. 쟁점은 집단 간 비중 차이가 아니라, 동일 비중 규칙의 대표성이었다.")

put(s11.select_one(".v14-reaction small"), "2026.1.12 평의원회 8:2 심의·가결(취재 보도) → 2.26 학칙 개정 → 2.27 시행 공고 → 3.1 시행(대학 원문). 학생 반대와는 별개인 공식 절차다.")
put(s12.select(".v16-compare>div")[-1].select("p")[-1], "공학 전환 추진. 2026.1.12 평의원회 8:2 심의·가결(보도), 2.26 학칙 개정·2.27 공고·3.1 시행(대학 원문)")

s13.select_one(".deck-kicker").string = "연구자의 평가 · 조치별 판정"
s13.select_one(".v17-top span").string = "12 / 대응별 평가"
s13.select_one("h2").string = "효과와 한계를 조치별로 평가한다"
put(s13.select_one(".v15-body"), '''
<div class="v18-evaluation">
 <div class="v18-eval-head"><b>평가</b><b>강원대–강릉원주대 통합</b><b>동덕여대 공학 전환</b></div>
 <div><b>효과적이었던 대응</b><p>평의원회 부결 뒤 인력 구성을 35명 구상에서 공무원 24명·외부 전문가 11명으로 수정했고, 재상정안이 15:6으로 가결됐다.</p><p>대면 협의와 논의 잠정 중단으로 즉각적인 대화·수업 재개 합의가 이뤄졌다.</p></div>
 <div><b>미흡했던 대응</b><p>신청서 선제출과 257쪽 심의자료의 늦은 전달은 사전 설명·심의 기회를 둘러싼 이의를 남겼다. 수정 폭에도 직원협의회가 이의를 제기했다.</p><p>공론화의 집단별 1:1:1 동일 비중과 대표성에 학생 측이 이의를 제기했다. 85.7% 반대 총투표 뒤에도 전환 절차가 진행됐다.</p></div>
 <div><b>확인되지 않은 성과</b><p>가결이 직원 요구의 충분한 반영이나 신뢰 회복을 뜻하는지는 확인되지 않는다.</p><p>1.12 평의원회 심의·가결(보도), 2.26 학칙 개정·2.27 공고·3.1 시행은 공식 경과다. 학생 수용·신뢰 회복은 확인되지 않는다.</p></div>
</div><p class="v18-eval-note">평가는 확인된 조치와 반응에 한정한다. 대학 전체의 성공·실패나 메시지의 독립적 효과는 판정하지 않는다.</p>''')

s14.select_one(".deck-kicker").string = "당시의 대응 대안 · 사례별 적용"
s14.select_one("h2").string = "결정 전에 정보와 규칙을 합의하라"
put(s14.select_one(".v16-theory-close"), "효과가 확인된 조치는 살리고, 절차에 이의가 제기된 지점은 결정 전에 다뤘어야 한다. 카메론은 조건을, 베노이트는 실제 발언의 설명 방식을 읽는 도구다.")
put(s14.select_one(".v16-three-actions"), '''
<div><span>01 · 강원대</span><h3>신청 전에 자료와 인력안을 협의</h3><p>통합 신청 전 자료·일정을 공개하고 평의원회가 심의할 시간을 확보한다. 인력 구성은 직원협의회와 수정 가능 범위를 먼저 논의한다.</p></div>
<div><span>02 · 동덕여대</span><h3>논의 초기에 참여 규칙을 합의</h3><p>공학 전환 검토안·일정을 일찍 공개한다. 학생 등 참여 주체의 대표성, 집단별 동일 비중의 이유와 이의 절차를 조사 전에 합의한다.</p></div>
<div><span>03 · 공통</span><h3>요구 반영 결과를 다시 공개</h3><p>어떤 요구를 반영·보류·거절했는지, 그 이유와 후속 일정은 무엇인지 같은 구성원에게 문서로 보고한다.</p></div>''')
put(s14.select_one(".v16-note"), "두 사례에서 관찰된 이의에 대응하는 실무 대안이다. 제시한 절차를 밟았을 때의 효과까지 검증된 것은 아니다.")

for slide in slides:
    slide["class"] = list(slide.get("class", [])) + ["v18-slide"]
titles = [x.find(["h1", "h2"]).get_text(" ", strip=True) if x.find(["h1", "h2"]) else "참고문헌 · 출처" for x in slides]
for n, item in enumerate(soup.select(".toc-item"), 1):
    item.string = f"{n:02d} · {titles[n-1]}"
for a in soup.select("#controls a[href]"):
    a["href"] = a["href"].replace("deck_v17.pdf", "deck_v18.pdf")
soup.title.string = "변화의 결단은 왜 위기가 되는가 | deck_v18"
(DST / "index.html").write_text(str(soup).replace("deck_v17", "deck_v18"), encoding="utf-8")
(DST / "style.css").write_text((SRC / "style.css").read_text(encoding="utf-8") + "\n" + (ROOT / "scripts/deck_v18_theme.css").read_text(encoding="utf-8"), encoding="utf-8")

js = (SRC / "slides.js").read_text(encoding="utf-8")
speaker = json.loads(re.search(r"const SPEAKER_NOTES = (\[.*?\]);\s*function fitStage", js, re.S).group(1))
for i, note in enumerate(speaker): note["title"] = titles[i]
speaker[3]["script"] = "E24는 공중의 상대적인 힘, E21은 공중의 양보할 수 있는 수준, I56은 신뢰감 정도다. 기록으로 관찰 가능한 조건을 골랐으며 양보 수준과 신뢰를 직접 측정한 것은 아니다. 인과관계로 단정하지 않는다."
speaker[9]["script"] = "최종조사는 교원, 학생, 직원 응답값을 1대1대1 동일 비중으로 적용했다. 실제 응답자 수가 서로 달라 대표성에 이의가 제기됐다."
speaker[10]["script"] = "2025년 12월 발표 뒤 학생 반대가 이어졌습니다. 2026년 1월 12일 평의원회 심의·가결의 8 대 2 수치는 취재 보도 근거입니다. 학칙은 2월 26일 개정, 27일 공고, 3월 1일 시행입니다. 공식 절차와 학생 수용을 구분합니다."
speaker[12]["script"] = "대학 단위의 성공 실패가 아니라 대응별 평가다. 강원대 조직안 수정과 동덕여대 대면 협의·잠정 중단은 확인된 조치다. 사전 소통과 공론화 대표성에는 이의가 남았다. 양측의 신뢰 회복은 확인되지 않았다."
speaker[13]["script"] = "당시 강원대는 신청 전 자료 공개, 충분한 심의, 인력 협의를 했어야 한다. 동덕여대는 논의 초기에 정보 공개와 대표성, 동일 비중 규칙을 합의했어야 한다. 두 대학 모두 요구 반영 결과를 다시 공개하는 절차가 필요하다."
js = re.sub(r"const SPEAKER_NOTES = \[.*?(?=function fitStage\(\))", "const SPEAKER_NOTES = " + json.dumps(speaker, ensure_ascii=False, indent=2) + ";\n\n", js, flags=re.S)
(DST / "slides.js").write_text(js, encoding="utf-8")
for name in ("asset_sources.md", "sources.html"):
    content = (SRC / name).read_text(encoding="utf-8").replace("deck_v17", "deck_v18")
    if name == "sources.html":
        content = content.replace("2026-02-26 개정 학칙 공포·시행 공고(02-27 게시)", "2026-02-26 개정 학칙의 시행 공고(02-27 게시); 부칙상 시행일은 03-01")
    (DST / name).write_text(content, encoding="utf-8")
refs = (SRC / "deck_v17_참고문헌.md").read_text(encoding="utf-8").replace("deck_v17", "deck_v18")
refs = refs.replace("개정 학칙의 2026-02-26 시행과 27일 공고", "학칙의 2026-02-26 개정, 27일 공고와 부칙상 03-01 시행")
(DST / "deck_v18_참고문헌.md").write_text(refs, encoding="utf-8")
(DST / "README.md").write_text("# deck_v18\n\n15장 최종 발표자료. `deck_v17`의 디자인과 사건 자료를 유지하며 대응별 평가, 당시의 대응 대안, 변수 해석 한계, 집계 규칙 및 학칙 날짜를 교정했다.\n\n- [웹 덱](index.html) · [PDF](deck_v18.pdf) · [출처 색인](sources.html) · [사진 출처](asset_sources.md)\n", encoding="utf-8")
print(f"Built {len(slides)} slides in {DST}")
