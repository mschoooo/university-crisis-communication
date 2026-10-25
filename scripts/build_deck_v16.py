# -*- coding: utf-8 -*-
"""Rebuild the v15 deck on a white academic presentation canvas."""
from pathlib import Path
from bs4 import BeautifulSoup
import json
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "versions/deck_v15"
DST = ROOT / "versions/deck_v16"
shutil.copytree(SRC, DST, dirs_exist_ok=True)
for old in ("deck_v15.pdf", "deck_v15_참고문헌.md"):
    (DST / old).unlink(missing_ok=True)
soup = BeautifulSoup((SRC / "index.html").read_text(encoding="utf-8"), "html.parser")
slides = soup.select("section.slide")
assert len(slides) == 15


def fragment(html):
    return BeautifulSoup(html, "html.parser")


def set_body(n, html):
    body = slides[n-1].select_one(".v15-body")
    body.clear()
    body.extend(fragment(html).contents)


def add_ids(n, *ids):
    span = slides[n-1].select_one(".source-footer span")
    for ident in ids:
        if not span.find("a", href=f"sources.html#{ident}"):
            span.append(fragment(f' · <a href="sources.html#{ident}">{ident}</a>'))


# White cover, two modest documentary photographs, no dark wash or archive motif.
cover = slides[0]
cover.clear()
cover.extend(fragment('''
<div class="v16-cover-label">위기관리(029) · 중간고사 대체 과제</div>
<h1>변화의 결단은<br/>왜 위기가 되는가</h1>
<p class="v16-cover-sub">강원대–강릉원주대 통합과 동덕여대 남녀공학 전환의<br/>위기 커뮤니케이션 비교 분석</p>
<div class="v16-cover-photos"><figure><img src="assets/protest_kangwon.jpg" alt="강원대 통합 반대 현수막"/><figcaption>강원대 통합 반대 현장 · <a href="asset_sources.md">사진 출처</a></figcaption></figure><figure><img src="assets/protest_dongduk_wall.jpg" alt="동덕여대 공학 전환 반대 시위 현장"/><figcaption>동덕여대 공학 전환 반대 현장 · <a href="asset_sources.md">사진 출처</a></figcaption></figure></div>
<div class="v16-cover-byline">조민성 <span>부산대학교 미디어커뮤니케이션학과</span></div>
''').contents)

s2 = slides[1]
s2.select_one(".cc-bottom").clear()
s2.select_one(".cc-bottom").extend(fragment("분석 단위는 <b>발화 → 후속 행동 → 공중의 반응</b>이다. 공식 의결과 구성원 반응은 별도로 기록한다.").contents)

# Accurate use of the I56 name and a bounded case interpretation.
s3 = slides[2]
s3.select_one(".v15-method").replace_with(fragment('<p class="v15-method">81개 전체를 사건에 적용하지 않았다. 공개 기록에서 공중의 영향력(E24), 요구의 조정 여지(E21), 사전 협의·정보공개를 둘러싼 관계 문제(I56)를 선별해 읽는다.</p>'))
s3.select_one(".v15-vars>div:nth-child(3) p").string = "사전 협의와 자료 제공을 둘러싼 이의가 확인된다. 이를 신뢰도 측정 결과로 읽지 않는다."

s4 = slides[3]
s4_html = s4.decode_contents().replace("사의 보류", "심의 보류")
s4.clear(); s4.extend(fragment(s4_html).contents)

s8 = slides[7]
s8.select_one(".v15-context").string = "카메론 I56: 사전 협의를 둘러싼 이의는 확인된다. 기존 신뢰 수준이나 해명의 수용 효과는 측정되지 않았다."

s11 = slides[10]
s11.select_one(".v15-context").string = "카메론 E21·I56: 2029년은 기존 일정이다. 사전 협의 갈등은 확인되지만 신뢰 수준과 회복 여부는 측정되지 않았다."
s11.select_one(".v14-reaction small").string = "2026.1.12 평의원회 8:2 심의(취재 보도) → 2.26 개정 학칙 시행(대학 공고). 2025.12 학생 반대와 별개의 공식 절차다."
add_ids(11, "D14", "D22", "D23")

s12 = slides[11]
s12.select_one("h2").string = "무엇을 조정하고, 무엇을 유지했나"
set_body(12, '''
<div class="v16-compare"><div class="v16-compare-head"><b></b><b>강원대–강릉원주대 통합</b><b>동덕여대 공학 전환</b></div>
<div><b>대응 조건</b><p>평의원회 심의·부결(E24)<br/>인력 구성 수정 여지(E21)</p><p>학생 집단행동과 대표성 논쟁(E24)<br/>여대 유지 요구와 전환 추진의 충돌(E21)</p></div>
<div><b>메시지 → 행동</b><p>자료 지연 사과·기한 해명<br/>→ 인력안 수정·재상정</p><p>결정 전 논의 해명<br/>→ 면담·잠정 중단·공론화</p></div>
<div><b>조정한 것</b><p>공무원 35명 구상 → 공무원 24명·외부 전문가 11명</p><p>논의 일시 중단·수업 재개 합의</p></div>
<div><b>유지한 것</b><p>통합 추진. 평의원회 15:6 가결 뒤 직원협의회 이의 지속</p><p>공학 전환 추진. 2026.1.12 평의원회 8:2 심의(보도), 2.26 개정 학칙 시행(공고)</p></div></div>
<p class="v16-under-compare">공식 절차의 진전과 구성원의 수용을 같은 결과로 보지 않는다.</p>
''')
add_ids(12, "D14", "D22", "D23")

s13 = slides[12]
s13.select_one("h2").string = "공식 결정 뒤에도 이견은 남았다"
set_body(13, '''
<div class="v16-outcome-cols"><div><span>강원대</span><b>공식 결정</b><p>수정안 재상정 뒤 평의원회 <strong>15:6 가결</strong></p><b>구성원 반응</b><p>직원협의회는 수정 폭에 이의를 제기했다.</p></div><div><span>동덕여대</span><b>공식 경과</b><p>2026.1.12 평의원회 <strong>8:2 심의·가결</strong>(취재 보도)<br/>2.26 <strong>개정 학칙 시행</strong>(대학 공고)</p><b>구성원 반응</b><p>2025.12 학생 총투표 <strong>85.7% 반대</strong>. 평의원회 학생위원의 반대도 보도됐다.</p></div></div>
<div class="v16-limit"><b>판정 범위</b><p>의결·학칙 시행은 공식 절차의 진전이다. 같은 공중의 신뢰를 전후로 측정한 자료가 없으므로 수용·신뢰 회복과 메시지의 독립적 효과는 판정하지 않는다.</p></div>
''')
add_ids(13, "D14", "D22", "D23")

s14 = slides[13]
s14.select_one("h2").string = "결정 전에 절차를 합의하라"
set_body(14, '''
<p class="v16-theory-close">카메론은 대응 선택의 조건을, 실제 발언에 한정한 베노이트는 설명 방식을 보여준다. 두 사례에서 드러난 실무 과제는 결정 전 정보와 참여 규칙이다.</p>
<div class="v16-three-actions"><div><span>01</span><h3>사전 정보공개와 협의</h3><p>검토안·일정·원문·수정 가능 범위를 공개하고, 결정 전에 구성원별 요구를 듣는다.</p></div><div><span>02</span><h3>대표성·의사결정 규칙</h3><p>참여자, 대표 방식, 결정권, 집단별 가중치와 이의 절차를 사전에 합의한다.</p></div><div><span>03</span><h3>후속 조치와 관계관리</h3><p>요구별 반영·미반영 이유와 시행 결과를 기록해 같은 구성원에게 다시 보고한다.</p></div></div>
<p class="v16-note">관찰된 자료 지연·합의 범위·대표성 논쟁에서 도출한 제언이며 효과가 검증된 처방이라는 뜻은 아니다.</p>
''')

s15 = slides[14]
for node in s15.select(".folio,.deck-kicker,h2"):
    node.decompose()
s15["class"] = list(s15.get("class", [])) + ["v16-ref-slide"]
last_bib_row = s15.select(".v9-bib-row.evidence")[-1]
last_bib_row.insert_after(fragment('<div class="v9-bib-row evidence"><b>동덕여대 (2026)</b><span>1.12 평의원회 심의 취재 보도 · 2.26 개정 학칙과 대학 공고 <small>D14 · D22 · D23</small></span></div>'))
add_ids(15, "D14", "D22", "D23")

# Remove redundant English section furniture from the actual document structure.
for slide in slides[1:14]:
    folio = slide.select_one(".folio")
    if folio: folio.decompose()
for n, slide in enumerate(slides, 1):
    slide["data-slide"] = str(n)
    slide["class"] = list(slide.get("class", [])) + ["v16-slide"]
    footer = slide.select_one(".source-footer")
    if footer:
        footer.select("span")[-1].string = f"{n:02d} / 15"
        footer.select("span")[0].replace_with(fragment('<span>' + str(footer.select("span")[0]).replace('<span>', '').replace('</span>', '').replace(' · 관찰과 해석 구분','').replace(' · 자료와 해석을 구분','').replace(' · 해석은 원문과 구분','') + '</span>'))

titles = [x.find(["h1", "h2"]).get_text(" ", strip=True) if x.find(["h1", "h2"]) else "참고문헌 · 출처" for x in slides]
for n, button in enumerate(soup.select(".toc-item"), 1):
    button.string = f"{n:02d} · {titles[n-1]}"
for a in soup.select("#controls a[href]"):
    a["href"] = a["href"].replace("deck_v15.pdf", "deck_v16.pdf")
soup.title.string = "변화의 결단은 왜 위기가 되는가 | deck_v16"
(DST / "index.html").write_text(str(soup).replace("deck_v15", "deck_v16"), encoding="utf-8")

# Carry over the control panel rules and overwrite every on-slide visual rule.
css = (SRC / "style.css").read_text(encoding="utf-8")
css += "\n" + (ROOT / "scripts/deck_v16_theme.css").read_text(encoding="utf-8")
(DST / "style.css").write_text(css, encoding="utf-8")
js = (SRC / "slides.js").read_text(encoding="utf-8")
speaker = json.loads(re.search(r"const SPEAKER_NOTES = (\[.*?\]);\s*function fitStage", js, re.S).group(1))
speaker[0]["title"] = titles[0]
speaker[0]["script"] = "두 대학의 구조개편에서 공식 결정과 구성원 반응을 구분해 위기 커뮤니케이션을 비교합니다."
speaker[2]["script"] = "E24·E21·I56은 교재 표를 전사해 붙인 분석용 순번입니다. I56의 신뢰도는 측정하지 않았고 사전 협의·정보공개 갈등을 제한적으로 읽습니다."
speaker[3]["script"] = "2월 28일에는 심의가 보류됐습니다. 신청서 선제출과 늦은 자료 전달이 초기 절차 쟁점이었습니다."
speaker[7]["script"] = "결정 전 논의라는 대학의 발언과 학생의 사전 협의 요구를 나란히 읽습니다. I56의 신뢰 수준은 측정되지 않았습니다."
speaker[10]["script"] = "2025년 12월 발표와 학생 총투표 이후, 2026년 1월 12일 평의원회 심의와 2월 26일 개정 학칙 시행으로 공식 절차가 진전했습니다. 8 대 2 수치는 회의록 원본이 아닌 취재 보도 근거입니다."
speaker[11]["title"] = titles[11]
speaker[11]["script"] = "무엇을 조정하고 유지했는지 비교합니다. 공식 절차의 진전과 구성원의 수용은 별도로 읽습니다."
speaker[12]["title"] = titles[12]
speaker[12]["script"] = "동덕여대 1월 12일 8 대 2 심의는 취재 보도, 2월 26일 학칙 시행은 대학 공고로 확인합니다. 학생 반대와 신뢰 수준은 별개입니다."
speaker[13]["title"] = titles[13]
speaker[13]["script"] = "제언은 사전 정보공개와 협의, 대표성과 의사결정 규칙, 후속 조치와 관계관리의 세 범주입니다."
speaker[14]["title"] = titles[14]
js = re.sub(r"const SPEAKER_NOTES = \[.*?(?=function fitStage\(\))", "const SPEAKER_NOTES = " + json.dumps(speaker, ensure_ascii=False, indent=2) + ";\n\n", js, flags=re.S)
(DST / "slides.js").write_text(js, encoding="utf-8")

for name in ("README.md", "asset_sources.md", "sources.html"):
    content = (SRC / name).read_text(encoding="utf-8").replace("deck_v15", "deck_v16")
    if name == "asset_sources.md":
        content = content.replace("표지에서는 어두운 배경으로 사용.", "표지에서는 원래 색감의 사진으로 사용.")
        content = content.replace("| 6 | `protest_kangwon.jpg`", "| 1, 6 | `protest_kangwon.jpg`")
    (DST / name).write_text(content, encoding="utf-8")
refs = (SRC / "deck_v15_참고문헌.md").read_text(encoding="utf-8").replace("deck_v15", "deck_v16")
(DST / "deck_v16_참고문헌.md").write_text(refs, encoding="utf-8")
(DST / "README.md").write_text("# deck_v16\n\n흰 배경의 15장 대학 위기 커뮤니케이션 비교 발표자료.\n\n- [웹 덱](index.html) · [PDF](deck_v16.pdf) · [출처 색인](sources.html) · [사진 출처](asset_sources.md)\n- 2026.1.12 평의원회 8:2는 D14 취재 보도, 2.26 학칙 시행은 D22·D23 대학 공고에 따른다.\n", encoding="utf-8")
print(f"Built {len(slides)} slides in {DST}")
