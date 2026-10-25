# -*- coding: utf-8 -*-
"""Adapt deck_v16 to the supplied Jeju presentation's visual grammar."""
from pathlib import Path
from bs4 import BeautifulSoup
import json
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "versions/deck_v16"
DST = ROOT / "versions/deck_v17"
shutil.copytree(SRC, DST, dirs_exist_ok=True)
for stale in ("deck_v16.pdf", "deck_v16_참고문헌.md"):
    (DST / stale).unlink(missing_ok=True)
soup = BeautifulSoup((SRC / "index.html").read_text(encoding="utf-8"), "html.parser")
original = soup.select("section.slide")
assert len(original) == 15
slides = [original[i] for i in [0, 3, 1, 2, *range(4, 15)]]
stage = soup.select_one("#stage")
for node in original:
    node.extract()
for node in slides:
    stage.append(node)


def frag(html):
    return BeautifulSoup(html, "html.parser")


def replace_node(node, html):
    node.replace_with(frag(html))


def links(*ids):
    return " · ".join(f'<a href="sources.html#{x}">{x}</a>' for x in ids)


def set_footer(slide, n, ids):
    old = slide.select_one(".source-footer")
    new = frag(f'<footer class="source-footer"><span>자료 {links(*ids)}</span><span>{n:02d} / 15</span></footer>')
    if old:
        old.replace_with(new)
    else:
        slide.append(new)


# Reference cover: large sans headline on the left, documentary imagery on the right.
cover = slides[0]
cover.clear()
cover.extend(frag('''
<div class="v17-cover-left"><p class="v17-overline">위기 커뮤니케이션 · 비교 분석</p>
<h1>변화의 결단은<br/>왜 위기가 되는가</h1>
<p class="v17-cover-sub">강원대–강릉원주대 통합과 동덕여대<br/>남녀공학 전환의 위기 커뮤니케이션 비교 분석</p>
<p class="v17-cover-byline">조민성 · 부산대학교 미디어커뮤니케이션학과</p>
<p class="v17-cover-question">공식 결정은 진전됐지만, 구성원의 반대는 왜 남았는가?</p>
<p class="v17-cover-source">사진: 강원도민일보 · 연합뉴스 · <a href="asset_sources.md">시각자료 출처</a></p></div>
<div class="v17-cover-right"><figure><img src="assets/protest_kangwon.jpg" alt="강원대 통합 반대 현수막"/><figcaption>강원대 통합 반대 현장</figcaption></figure><figure><img src="assets/protest_dongduk_wall.jpg" alt="동덕여대 공학 전환 반대 시위"/><figcaption>동덕여대 공학 전환 반대 현장</figcaption></figure></div>
''').contents)
set_footer(cover, 1, ["A01P", "D26"])

# Opening follows the reference: event context, analytical question, theory.
s2 = slides[1]
s2.select_one("h2").string = "두 구조개편에서 절차가 쟁점이 됐다"
s2.select_one(".deck-kicker").string = "초기 위험 징후 · 강원대와 동덕여대"
s2.select_one(".v15-body").clear()
s2.select_one(".v15-body").extend(frag('''
<div class="v17-context-top"><figure><img src="assets/protest_dongduk_stairs.jpg" alt="동덕여대 본관 앞 공학 전환 반대 시위"/><figcaption>동덕여대 본관 앞 시위 · 2024.11.12 촬영 · <a href="asset_sources.md">사진 출처</a></figcaption></figure>
<div class="v17-context-text"><div><b>강원대–강릉원주대</b><p>통합 신청과 심의 일정이 추진됐다. 신청서 선제출과 늦은 심의자료 전달에 이의가 나왔다.</p></div><div><b>동덕여대</b><p>남녀공학 논의가 알려진 뒤 학생들이 사전 협의와 결정권을 문제 삼았다.</p></div></div></div>
<div class="v17-dual-timeline"><div><strong>강원대</strong><span>2.20 신청서 선제출</span><span>2.26 257쪽 자료 전달</span><span>2.28 심의 보류</span></div><div><strong>동덕여대</strong><span>2024.11 논의 공개</span><span>11.11 면담 취소 논쟁</span><span>11.21 논의 잠정 중단</span></div></div>
<p class="v17-takeaway">같은 ‘구조개편’이라도 사전 정보와 참여 절차를 둘러싼 이의의 형태가 달랐다.</p>
''').contents)
set_footer(s2, 2, ["A03P", "A04", "D26", "D02"])

s3 = slides[2]
s3.select_one("h2").string = "무엇을 말했고, 무엇이 달라졌나?"
s3.select_one(".deck-kicker").string = "분석 질문 · 발화에서 공중 반응까지"
s3.select_one(".cc-body").clear()
s3.select_one(".cc-body").extend(frag('''
<div class="v17-rq"><div class="v17-rq-left"><span>연구 질문</span><p>대학본부는 갈등 속에서 어떤 설명과 대화를 선택했는가?<br/>그 뒤 확인 가능한 조치와 구성원 반응은 무엇이었는가?</p></div><div class="v17-rq-right"><span>같은 순서로 두 사례를 읽는다</span><div><b>01 · 발화</b><p>시점 · 주장 · 책임 인정 범위</p></div><div><b>02 · 행동</b><p>면담 · 논의 중단 · 수정안</p></div><div><b>03 · 반응</b><p>표결 · 합의 · 재반발</p></div></div></div>
<p class="v17-takeaway">공식 의결과 구성원 반응을 나누어 기록한다. 신뢰 회복은 별도 자료가 필요하다.</p>
''').contents)
set_footer(s3, 3, ["A01P", "A02P", "D02", "D09", "D10"])

s4 = slides[3]
s4.select_one("h2").string = "카메론의 변수로 대응 조건을 읽는다"
s4.select_one(".deck-kicker").string = "이론과 방법 · 외부 24개, 내부 57개"
set_footer(s4, 4, ["P99", "P01", "A03P", "D26"])

section_labels = [
    "", "01 / 사건 맥락", "02 / 분석 질문", "03 / 이론과 방법",
    "04 / 강원대 · 첫 설명", "05 / 강원대 · 재설명", "06 / 강원대 · 수정안",
    "07 / 동덕여대 · 초기 입장", "08 / 동덕여대 · 면담", "09 / 동덕여대 · 공론화",
    "10 / 동덕여대 · 전환 발표", "11 / 직접 비교", "12 / 공식 경과와 반응", "13 / 실무 제언", "14 / 참고문헌"
]
for n, slide in enumerate(slides, 1):
    slide["data-slide"] = str(n)
    slide["class"] = list(slide.get("class", [])) + ["v17-slide"]
    if n > 1:
        header = frag(f'<div class="v17-top"><span>{section_labels[n-1]}</span><span>대학 구조개편 · 위기 커뮤니케이션</span></div>')
        slide.insert(0, header)
    footer = slide.select_one(".source-footer")
    if footer:
        footer.select("span")[-1].string = f"{n:02d} / 15"

# The reference closes in navy. Keep the three v16 recommendations and the limits.
slides[13]["class"] += ["v17-closing"]
slides[13].select_one(".deck-kicker").string = "관찰 결과에서 도출한 실무 제언"
slides[13].select_one("h2").string = "결정 전에 절차를 합의하라"

titles = [slide.find(["h1", "h2"]).get_text(" ", strip=True) if slide.find(["h1", "h2"]) else "참고문헌 · 출처" for slide in slides]
for n, item in enumerate(soup.select(".toc-item"), 1):
    item.string = f"{n:02d} · {titles[n-1]}"
for a in soup.select("#controls a[href]"):
    a["href"] = a["href"].replace("deck_v16.pdf", "deck_v17.pdf")
soup.title.string = "변화의 결단은 왜 위기가 되는가 | deck_v17"
(DST / "index.html").write_text(str(soup).replace("deck_v16", "deck_v17"), encoding="utf-8")

css = (SRC / "style.css").read_text(encoding="utf-8")
css += "\n" + (ROOT / "scripts/deck_v17_theme.css").read_text(encoding="utf-8")
(DST / "style.css").write_text(css, encoding="utf-8")
js = (SRC / "slides.js").read_text(encoding="utf-8")
speaker = json.loads(re.search(r"const SPEAKER_NOTES = (\[.*?\]);\s*function fitStage", js, re.S).group(1))
speaker = [speaker[i] for i in [0, 3, 1, 2, *range(4, 15)]]
for i, note in enumerate(speaker):
    note["title"] = titles[i]
speaker[1]["script"] = "두 대학의 갈등을 초기 위험 징후로 나란히 제시합니다. 사진 촬영일과 사건일을 구분합니다."
speaker[2]["script"] = "발화, 후속 행동, 공중 반응을 같은 순서로 분석합니다. 공식 의결과 구성원 반응은 별도로 봅니다."
speaker[3]["script"] = "카메론의 외부·내부 변수 가운데 E24·E21·I56을 선별합니다. I56은 신뢰도 측정값이 아닙니다."
js = re.sub(r"const SPEAKER_NOTES = \[.*?(?=function fitStage\(\))", "const SPEAKER_NOTES = " + json.dumps(speaker, ensure_ascii=False, indent=2) + ";\n\n", js, flags=re.S)
(DST / "slides.js").write_text(js, encoding="utf-8")

for name in ("asset_sources.md", "sources.html"):
    content = (SRC / name).read_text(encoding="utf-8").replace("deck_v16", "deck_v17")
    if name == "asset_sources.md":
        content = content.replace("| 9 | `protest_dongduk_stairs.jpg`", "| 2, 9 | `protest_dongduk_stairs.jpg`")
    (DST / name).write_text(content, encoding="utf-8")
refs = (SRC / "deck_v16_참고문헌.md").read_text(encoding="utf-8").replace("deck_v16", "deck_v17")
(DST / "deck_v17_참고문헌.md").write_text(refs, encoding="utf-8")
(DST / "README.md").write_text("# deck_v17\n\n제공된 제주 해군기지 발제 PDF의 시각 체계와 구성 흐름을 참고해 `deck_v16`을 재디자인한 15장 발표자료. 사건 근거와 분석 범위는 유지했다.\n\n- [웹 덱](index.html) · [PDF](deck_v17.pdf) · [출처 색인](sources.html) · [사진 출처](asset_sources.md)\n", encoding="utf-8")
print(f"Built {len(slides)} slides in {DST}")
