"""Combine v13's message analysis with v9's documentary visual language."""
from pathlib import Path
from bs4 import BeautifulSoup
import json
import re
import shutil
import pymupdf

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "versions" / "deck_v13"
TARGET = ROOT / "versions" / "deck_v14"
TARGET.mkdir(exist_ok=True)
for name in ("assets", "sources.html", "sources.csv", "동덕여대_sources.csv", "asset_sources.md", "deck_v13_참고문헌.md"):
    src = SOURCE / name
    dst = TARGET / ("deck_v14_참고문헌.md" if name == "deck_v13_참고문헌.md" else name)
    shutil.copytree(src, dst, dirs_exist_ok=True) if src.is_dir() else shutil.copy2(src, dst)
for name in ("카메룬_81개_변수_전수분석.md", "카메룬 위기 상황변수 목록.md"):
    text = (SOURCE / name).read_text(encoding="utf-8").replace("카메룬", "카메론")
    (TARGET / name.replace("카메룬", "카메론")).write_text(text, encoding="utf-8")
d07_candidates = list(ROOT.parents[1].rglob("D07.pdf"))
if d07_candidates:
    with pymupdf.open(d07_candidates[0]) as d07:
        d07[3].get_pixmap(matrix=pymupdf.Matrix(3, 3), clip=pymupdf.Rect(40, 48, 800, 191), alpha=False).save(TARGET / "assets" / "D07_final_survey_clip.png")
elif not (TARGET / "assets" / "D07_final_survey_clip.png").exists():
    raise FileNotFoundError("D07.pdf or the verified D07 final survey excerpt is required")
ref = TARGET / "deck_v14_참고문헌.md"
ref.write_text(ref.read_text(encoding="utf-8").replace("deck_v13", "deck_v14").replace("카메룬", "카메론"), encoding="utf-8")

soup = BeautifulSoup((SOURCE / "index.html").read_text(encoding="utf-8"), "html.parser")
slides = soup.select("section.slide")
assert len(slides) == 15

def links(ids):
    return " · ".join(f'<a href="sources.html#{x}">{x}</a>' for x in ids)

def put(n, section, kicker, title, content, ids, kind=""):
    el = slides[n - 1]
    el.attrs = {"class": ["slide", "paper-slide", "v14-slide"] + ([kind] if kind else []), "data-slide": str(n)}
    el.clear()
    fragment = BeautifulSoup(f'''<header class="folio"><span>{section}</span><span>위기 메시지 · 행동 · 공중 반응</span></header>
<p class="deck-kicker">{kicker}</p><h2>{title}</h2>
<div class="v14-body">{content}</div>
<footer class="source-footer"><span>원자료 {links(ids)} · 자료와 해석을 구분</span><span>{n:02d} / 15</span></footer>''', "html.parser")
    el.extend(list(fragment.contents))

cover = slides[0]
cover.select_one("h1").replace_with(BeautifulSoup('<h1>대학 구조개편 갈등에서<br><em>위기 메시지는 어떻게 작동했나</em></h1>', "html.parser"))
cover.select_one(".cover-sub").string = "강원대 통합과 동덕여대 공학 전환의 발화·행동·반응"

# Preserve v13's research logic and soften the claim about all 81 variables.
s3 = slides[2]
lead = s3.select_one(".cc-lead")
lead.string = "교재의 81개 상황변수 목록을 검토했다. 공개 원문에서 실제 메시지 선택과 연결되는 근거를 확인할 수 있는 세 조건에 분석을 집중한다."
s3.select_one(".deck-kicker").string = "카메론의 정황적 수용 이론"
s3.select_one(".cc-bottom").string = "변수의 독립적인 인과 효과는 측정하지 않았다. ‘요구의 조정 가능성’은 E21을 관찰하기 위해 만든 분석 지표다."

put(5, "04 / 강원대 · 제46차", "2025.02.28 · 첫 설명", "사과가 있었지만 심의는 보류됐다", '''
<div class="v14-split v14-doc-left">
 <div class="v14-document"><span class="v14-eyebrow">회의록 원문 · 기획처장 발언</span><blockquote>“실무부처의 장으로서<br><em>분명히 사과를 드립니다.</em>”</blockquote><span class="v14-tag">베노이트 · 제한적 사과</span><p>자료 송부 지연에 대한 사과다. 통합안 전반의 책임 인정으로 확대하지 않는다.</p><a href="sources.html#A03P">제46차 대학평의원회 회의록 · A03P ↗</a></div>
 <div class="v14-side-flow"><div><b>2월 20일</b><p>본부가 통합 신청서를 교육부에 먼저 제출</p></div><div><b>2월 26일</b><p>257쪽 심의자료 송부. 평의원은 검토 시간이 부족하다고 지적</p></div><div><b>2월 28일</b><p>사과와 7쪽 요약 설명 뒤에도 <strong>심의 보류</strong></p></div><small>카메론: 일정 압박과 평의원회의 검토 권한이 충돌했다.</small></div>
</div>''', ["A03P"])

put(6, "05 / 강원대 · 제47차", "2025.04.01 · 재설명", "보안·기한 해명 뒤 8:12로 부결됐다", '''
<div class="v14-split v14-photo-left"><figure class="v14-photo"><img src="assets/protest_kangwon.jpg" alt="강원대 통합 반대 현수막"/><figcaption>통합 반대 현수막 · 2025.02.25 현장, 강원도민일보 02.26 보도 · <a href="asset_sources.md">사진 출처</a></figcaption></figure>
 <div class="v14-vote"><p class="v14-quote">“협상안의 보안 유지”와 “신청서 제출기한” 때문에 사전 심의가 어려웠다는 총장 설명</p><div class="v14-big-vote"><strong>8 <small>찬성</small></strong><span>:</span><strong>12 <small>반대</small></strong></div><figure class="v14-clip"><img src="assets/A01_vote_clip.png" alt="제47차 평의원회 회의록의 찬성 8표, 반대 12표, 부결 기록"/><figcaption>제47차 대학평의원회 회의록 40쪽 · A01P</figcaption></figure><p class="v14-take">평의원회는 사후 수정 약속에 동의하지 않았다. 출석 20명 표결.</p></div>
</div>''', ["A01P"])

put(7, "06 / 강원대 · 제48차", "2025.04.28 · 수정안", "인력 구성은 바뀌었지만 수용은 갈렸다", '''
<div class="v14-before-after"><div><span>이전 구상</span><strong>35명</strong><p>전원 공무원 배치</p></div><div class="v14-after"><span>수정안</span><strong>24명 <i>+</i> 11명</strong><p>공무원 · 외부 전문가</p></div></div>
<div class="v14-evidence-bottom"><figure class="v14-clip"><img src="assets/A02_staff_clip.png" alt="제48차 평의원회 회의록의 공무원 24명과 외부 전문가 11명 설명"/><figcaption>제48차 대학평의원회 회의록 · A02P</figcaption></figure><div class="v14-evidence-note"><b>15 : 6 가결</b><p>통합 절차는 진행됐다. 직원협의회는 실질적 변경 폭이 작다고 비판했다.</p><small>총원은 35명으로 유지. 인력 수정의 독립 효과와 직원 신뢰 회복은 미확인.</small></div></div>''', ["A02P", "A04", "A07"])

put(8, "07 / 동덕여대 · 초기 메시지", "2024.11.15~18 · 두 수신자", "본부의 설명과 학생 요구가 엇갈렸다", '''
<div class="v14-split v14-photo-left"><figure class="v14-photo"><img src="assets/protest_dongduk_wall.jpg" alt="동덕여대 공학 전환 반대 글씨가 남은 캠퍼스 현장"/><figcaption>동덕여대 시위 현장 · 연합뉴스 · <a href="asset_sources.md">사진 출처</a></figcaption></figure>
 <div class="v14-statement"><div><span>11월 15일 · 학부모에게</span><p>대학은 사과하며 점거와 수업 차질을 강조했다.</p></div><div><span>11월 18일 · 구성원에게</span><blockquote>“교무위원회 보고도 이루어지지 않은 의제설정 이전의 상황”</blockquote><small class="v14-tag">베노이트 · ‘이미 결정’ 주장에 대한 제한적 부인</small></div><div><span>학생의 요구</span><p>공학 전환 논의 중단과 사과. 본부의 절차 해명만으로 핵심 요구는 충족되지 않았다.</p></div></div>
</div>''', ["D01", "D26"], "v14-dongduk")

put(9, "08 / 동덕여대 · 대면 협의", "2024.11.21 · 처장단과 학생대표", "면담 뒤 논의가 잠정 중단됐다", '''
<div class="v14-split v14-photo-left"><figure class="v14-photo"><img src="assets/protest_dongduk_stairs.jpg" alt="동덕여대 본관 앞 과잠 시위 현장"/><figcaption>본관 앞 과잠 시위 · 2024.11.12 촬영, 연합뉴스 11.13 보도 · <a href="asset_sources.md">사진 출처</a></figcaption></figure>
 <div class="v14-milestones"><div><time>면담 전</time><p>학생은 공학 전환 반대 의사를 전달했다.</p></div><div><time>약 3시간 면담</time><p>본부와 학생대표가 직접 협의했다.</p></div><div><time>합의</time><p><strong>논의 잠정 중단</strong> · 재개 시 학생 협의 · 수업 재개</p></div><p class="v14-take">학생의 집단행동은 본부의 즉각적 입장 이동과 연결된다. 영구 철회로 해석하지 않는다.</p></div>
</div>''', ["D02", "D26"], "v14-dongduk")

put(10, "09 / 동덕여대 · 공론화", "2025.06~12 · 대표성 논쟁", "집계 규칙이 결과 해석을 갈랐다", '''
<div class="v14-number-pair"><div><b>51.8%</b><span>공학 전환 선택</span><small>교원·학생·직원 집단별 응답 비율 동일 가중</small></div><div><b>71.3%</b><span>여대 유지 선택</span><small>학생 응답자 안에서의 비율</small></div></div>
<figure class="v14-wide-clip"><img src="assets/D07_final_survey_clip.png" alt="동덕여대 최종 온라인 조사에서 동일 가중 공학 전환 51.8%와 학생 응답자 여대 유지 71.3%가 나타난 원문 표"/><figcaption>공론화 최종 온라인 조사 원문 표 · D07 4쪽. 서로 다른 집단의 비율이므로 두 수치를 같은 모집단의 찬반으로 읽지 않는다.</figcaption></figure>
<p class="v14-take">본부는 동일 가중을 구성단위의 동등한 참여로 설명했다. 학생은 인원 규모와 실제 의사가 축소 반영됐다고 비판했다.</p>''', ["D06", "D07", "D08", "D10"], "v14-dongduk")

put(11, "10 / 동덕여대 · 전환 발표", "2025.12.03~09 · 발표와 재반발", "우려를 인정한 발표 뒤에도 반대가 이어졌다", '''
<div class="v14-split v14-statement-left"><div class="v14-document"><span class="v14-eyebrow">12월 3일 · 총장 공식 입장문</span><blockquote>“재학생들의 반대와 우려가<br><em>여전히 존재한다는 사실을</em><br>무겁게 받아들이고 있습니다.”</blockquote><p>2029년 시행을 계획하며 재학생의 학업 환경 보장을 설명했다.</p><div class="v14-miniquote">“여성교육 발전과 여성 사회참여 확대에 큰 성과” <span class="v14-tag">베노이트 · 긍정적 이미지 강조</span></div><a href="sources.html#D09">동덕여대 공식 입장문 · D09 ↗</a></div>
<div class="v14-reaction"><strong>85.7%</strong><b>학생 총투표 반대</b><p>12월 9일 발표. 총학생회는 공론화위 대표성과 가중 방식을 비판하며 전환 중단을 요구했다.</p><p>대학은 학생 반대를 인정하면서 다른 구성원의 의견과 공론화 합의도 존중해야 한다고 재응답했다.</p><small>재학생 졸업 후 시행 계획은 여대 유지 요구의 수용과 다르다.</small></div></div>''', ["D09", "D10", "D11"], "v14-dongduk")

put(12, "11 / DIRECT COMPARISON", "두 대학의 대응 이동", "공중의 힘은 서로 다른 양보를 이끌었다", '''
<div class="v14-matrix"><div class="v14-matrix-head"><b>비교 질문</b><b>강원대 통합</b><b>동덕여대 전환</b></div>
<div><b>처음 설명</b><p>자료 지연 사과 → 보안·기한 해명</p><p>‘결정 전 논의’ 해명 → 학생 요구와 충돌</p></div>
<div><b>공중의 힘</b><p>평의원회 8:12 부결</p><p>집단행동과 대면 면담</p></div>
<div><b>확인된 양보</b><p>인력 구성 변경 후 재상정</p><p>논의 잠정 중단 후 공론화</p></div>
<div><b>남은 이견</b><p>직원협의회가 수정 폭 비판</p><p>총투표 85.7% 반대와 대표성 문제</p></div></div>
<p class="v14-take">카메론의 공중의 힘(E24)·양보 수준(E21)·기존 신뢰(I56)가 발화와 행동의 이동을 설명하는 조건으로 관찰됐다.</p>''', ["A01P", "A02P", "A07", "D02", "D09", "D10"])

put(13, "12 / WHAT WE CAN CONCLUDE", "확인된 성과와 한계", "대화는 움직였고, 신뢰 회복은 미확인이다", '''
<div class="v14-outcomes"><div><span>확인된 행동 변화</span><strong>강원대</strong><p>수정안 재상정과 공식 가결</p><strong>동덕여대</strong><p>논의 잠정 중단과 수업 재개 합의</p></div><div><span>확인된 반대</span><strong>강원대</strong><p>직원협의회의 수정 폭 비판</p><strong>동덕여대</strong><p>전환 발표 뒤 학생 총투표 반대</p></div><div><span>판정 유보</span><strong>공통</strong><p>동일 공중의 신뢰를 전후로 측정한 자료가 없다.</p><p>표결과 발표만으로 평판·신뢰 회복을 입증할 수 없다.</p></div></div>
<p class="v14-take">사례 기록은 메시지 이후의 행동과 반응을 보여준다. 각 메시지의 독립적 인과 효과는 분리할 수 없다.</p>''', ["A02P", "A07", "D02", "D10"])

put(14, "13 / CONCLUSION & PRACTICE", "종합 결론과 실무 제언", "설명 뒤에 바뀔 것까지 말해야 한다", '''
<div class="v14-conclusion"><div class="v14-conclusion-main"><span>종합 결론</span><p>두 사례 모두 공식 설명 뒤에도 반발이 이어졌다. <em>후속 행동</em>과 요구 반영 범위가 갈등의 다음 국면을 만들었다.</p><small>강원대는 조정 가능한 인력안을 수정했다. 동덕여대는 논의를 멈췄다가 전환 추진을 재개했고, 대표성 갈등이 남았다.</small></div><div class="v14-practice"><div><b>01</b><p>심의 전에 검토 가능한 원문과 수정 범위를 공개한다.</p></div><div><b>02</b><p>면담 뒤 합의한 내용, 미합의 쟁점, 다음 결정권자를 함께 공지한다.</p></div><div><b>03</b><p>공론화 전 집계 기준을 공개하고, 집단별 결과와 전체 결과를 나눠 제시한다.</p></div></div></div>
<p class="v14-take">실무 제언은 두 사례에서 관찰된 자료 지연, 합의 범위, 대표성 논쟁에서 도출했다. 효과가 검증된 처방으로 단정하지 않는다.</p>''', ["A03P", "A07", "D02", "D07", "D10"])

slides[14].select_one(".deck-kicker").string = "이론 문헌과 사건 원문"
slides[14].select_one("h2").string = "근거와 추가 검토 자료"
slides[14].select_one(".source-footer span").string = "전체 서지와 원문: deck_v14_참고문헌.md · sources.html"

for n, node in enumerate(slides, 1): node["data-slide"] = str(n)
titles = [s.find(["h1", "h2"]).get_text(" ", strip=True) for s in slides]
for n, button in enumerate(soup.select(".toc-item"), 1): button.string = f"{n:02d} · {titles[n-1]}"
for a in soup.select("#controls a[href]"):
    a["href"] = (a["href"].replace("deck_v13.pdf", "deck_v14.pdf")
                  .replace("카메룬_81개_변수_전수분석.md", "카메론_81개_변수_전수분석.md"))
    if "81개 변수" in a.get_text(): a.string = "81개 변수 검토표"
soup.title.string = "대학 구조개편 갈등에서 위기 메시지는 어떻게 작동했나 | deck_v14"
(TARGET / "index.html").write_text(str(soup).replace("카메룬", "카메론").replace("deck_v13", "deck_v14"), encoding="utf-8")

css = (SOURCE / "style.css").read_text(encoding="utf-8")
css += '''
/* v14: documentary visual hierarchy and guaranteed viewport centering */
body{display:block}
#stage{position:fixed;left:50%;top:50%;margin:0}
@media print{#stage{position:relative;left:auto;top:auto;transform:none!important}}
.v14-slide .folio{border-bottom:0}.v14-slide .deck-kicker{margin-top:24px;font-size:19px}.v14-slide h2{font-size:49px;line-height:1.23}.v14-body{margin:34px 72px 0 72px}.v14-slide .source-footer{font-size:15px}.v14-slide .source-footer a{text-decoration:underline;text-underline-offset:3px}
.v14-split{display:grid;grid-template-columns:1fr 1fr;gap:38px;height:565px}.v14-doc-left{grid-template-columns:1.08fr .92fr}.v14-photo-left{grid-template-columns:.95fr 1.05fr}.v14-statement-left{grid-template-columns:1.1fr .9fr}
.v14-document{background:#fbf9f2;padding:36px 42px;border-left:7px solid var(--teal);display:flex;flex-direction:column}.v14-eyebrow{font-size:18px;font-weight:800;color:var(--teal)}.v14-document blockquote{font:800 36px/1.48 var(--serif);margin:28px 0 18px}.v14-document blockquote em{font-style:normal;color:var(--brick)}.v14-document p{font-size:21px;margin:18px 0}.v14-document a{font-size:17px;color:var(--teal);margin-top:auto}.v14-tag{display:inline-block;color:var(--brick);font-size:17px;font-weight:800}
.v14-side-flow>div{display:grid;grid-template-columns:145px 1fr;gap:20px;padding:18px 0;border-bottom:1px solid #c6c8bd}.v14-side-flow b{font-size:22px;color:var(--teal)}.v14-side-flow p{font-size:23px;line-height:1.4;margin:0}.v14-side-flow strong{color:var(--brick)}.v14-side-flow small{display:block;margin-top:33px;font-size:19px;color:#4b5852}
.v14-photo{margin:0;position:relative;overflow:hidden;background:#d8d8cf}.v14-photo img{width:100%;height:100%;object-fit:cover;filter:grayscale(.45) contrast(1.05)}.v14-photo figcaption{position:absolute;bottom:0;left:0;right:0;padding:11px 18px;background:rgba(18,23,21,.84);color:white;font-size:15px}.v14-photo figcaption a{color:white}
.v14-vote{display:flex;flex-direction:column}.v14-quote{font-size:23px;line-height:1.4;margin:0 0 10px}.v14-big-vote{display:flex;align-items:baseline;justify-content:center;gap:22px;font:800 88px var(--serif);color:var(--teal);line-height:1.1}.v14-big-vote strong:last-child{color:var(--brick)}.v14-big-vote span{font-size:54px;color:#686c63}.v14-big-vote small{font:700 19px var(--sans)}.v14-clip{margin:14px 0 0}.v14-clip img{display:block;width:100%;height:auto;object-fit:contain;background:white}.v14-clip figcaption,.v14-wide-clip figcaption{font-size:16px;line-height:1.35;color:#505d57;margin-top:8px}.v14-take{font-size:21px;line-height:1.42;color:#263934;margin:21px 0 0;border-left:5px solid var(--brick);padding-left:18px}
.v14-before-after{display:grid;grid-template-columns:1fr 1.18fr;gap:38px}.v14-before-after>div{padding:16px 20px;background:#e6e8e0}.v14-before-after .v14-after{background:#e0eae6}.v14-before-after span{font-size:19px;font-weight:800;color:var(--teal)}.v14-before-after strong{display:block;font:800 61px var(--serif);line-height:1.12;color:#294f53;margin:4px 0}.v14-before-after i{font-size:39px;color:var(--brick);font-style:normal}.v14-before-after p{font-size:22px;margin:0}.v14-evidence-bottom{display:grid;grid-template-columns:1.25fr .75fr;gap:34px;margin-top:24px}.v14-evidence-bottom .v14-clip img{height:200px;object-fit:contain}.v14-evidence-note{padding:16px 0}.v14-evidence-note b{display:block;font:800 52px var(--serif);color:var(--brick)}.v14-evidence-note p{font-size:21px;line-height:1.4}.v14-evidence-note small{font-size:17px;color:#52605a}
.v14-statement>div{padding:8px 0 19px;border-bottom:1px solid #b6beb7}.v14-statement span{font-size:19px;font-weight:800;color:var(--brick)}.v14-statement p{font-size:22px;line-height:1.4;margin:8px 0}.v14-statement blockquote{font:800 27px/1.38 var(--serif);margin:10px 0}.v14-statement .v14-tag{font-size:16px}
.v14-milestones{display:flex;flex-direction:column}.v14-milestones>div{display:grid;grid-template-columns:160px 1fr;gap:18px;border-bottom:1px solid #bac2b9;padding:16px 0}.v14-milestones time{font-size:21px;font-weight:800;color:var(--brick)}.v14-milestones p{font-size:23px;line-height:1.37;margin:0}.v14-milestones strong{color:var(--teal)}
.v14-number-pair{display:grid;grid-template-columns:1fr 1fr;gap:36px}.v14-number-pair>div{border-top:4px solid var(--teal);padding-top:8px}.v14-number-pair>div:last-child{border-color:var(--brick)}.v14-number-pair b{font:800 68px var(--serif);color:var(--teal);display:block;line-height:1.12}.v14-number-pair>div:last-child b{color:var(--brick)}.v14-number-pair span{font-size:24px;font-weight:800}.v14-number-pair small{display:block;font-size:17px;color:#5a635c;margin-top:6px}.v14-wide-clip{margin:23px 0 0}.v14-wide-clip img{width:100%;height:224px;object-fit:contain;background:#fff;display:block}.v14-wide-clip figcaption{margin-top:5px}.v14-number-pair~.v14-take{margin-top:17px}
.v14-miniquote{font:700 19px var(--serif);margin-top:auto}.v14-miniquote .v14-tag{font:800 15px var(--sans);margin-left:8px}.v14-reaction{display:flex;flex-direction:column;padding:17px 0 0}.v14-reaction strong{font:800 95px var(--serif);line-height:1.1;color:var(--brick)}.v14-reaction b{font-size:27px;margin-bottom:20px}.v14-reaction p{font-size:22px;line-height:1.43;margin:0 0 20px}.v14-reaction small{font-size:18px;color:#56635d;margin-top:auto}
.v14-matrix{border-top:3px solid var(--teal)}.v14-matrix>div{display:grid;grid-template-columns:230px 1fr 1fr;gap:25px;padding:17px 10px;border-bottom:1px solid #bac3ba}.v14-matrix-head{background:#e0e7e1}.v14-matrix b{font-size:22px;color:#263d39}.v14-matrix p{font-size:21px;line-height:1.4;margin:0}.v14-matrix-head b{font-size:21px;color:var(--teal)}
.v14-outcomes{display:grid;grid-template-columns:repeat(3,1fr);gap:32px}.v14-outcomes>div{padding-top:18px;border-top:4px solid var(--teal)}.v14-outcomes>div:nth-child(2){border-color:var(--brick)}.v14-outcomes>div:nth-child(3){border-color:#4c5550}.v14-outcomes span{font:800 29px var(--serif);display:block;margin-bottom:26px}.v14-outcomes strong{font-size:18px;color:var(--teal)}.v14-outcomes p{font-size:23px;line-height:1.42;margin:7px 0 29px}
.v14-conclusion{display:grid;grid-template-columns:1.05fr .95fr;gap:55px}.v14-conclusion-main{background:#e5eae4;padding:28px 34px}.v14-conclusion-main span{font-size:20px;font-weight:800;color:var(--teal)}.v14-conclusion-main p{font:800 33px/1.48 var(--serif);margin:20px 0 35px}.v14-conclusion-main em{font-style:normal;color:var(--brick)}.v14-conclusion-main small{font-size:19px;line-height:1.5}.v14-practice>div{display:grid;grid-template-columns:70px 1fr;gap:20px;padding:13px 0;border-bottom:1px solid #b8c0b7}.v14-practice b{font:800 38px var(--serif);color:var(--brick)}.v14-practice p{font-size:23px;line-height:1.42;margin:0}
.v14-slide[data-slide="7"] .v14-evidence-bottom{margin-top:32px}.v14-slide[data-slide="7"] .v14-evidence-bottom .v14-clip img{height:232px}
.v14-slide[data-slide="12"] .v14-matrix>div{padding-top:23px;padding-bottom:23px}
.v14-slide[data-slide="13"] .v14-outcomes{min-height:392px}.v14-slide[data-slide="13"] .v14-outcomes>div{padding-top:22px}
.v14-slide[data-slide="14"] .v14-conclusion{min-height:420px}.v14-slide[data-slide="14"] .v14-practice>div{min-height:133px;align-items:start;padding-top:20px}
'''
(TARGET / "style.css").write_text(css, encoding="utf-8")

(TARGET / "asset_sources.md").write_text("""# deck_v14 시각자료 출처

| 슬라이드 | 자산 | 출처와 사용 범위 |
|---|---|---|
| 1, 8 | `protest_dongduk_wall.jpg` | 연합뉴스 사진(2024.11.14 장면), [The Korea Times 보도](https://www.koreatimes.co.kr/southkorea/society/20241118/protests-at-dongduk-womens-university-trigger-anti-feminist-backlash). 표지에서는 어두운 배경으로 사용. |
| 6 | `protest_kangwon.jpg` | 강원대 통합 반대 현수막, [강원도민일보 2025.02.26 보도](https://www.kado.net/news/articleView.html?idxno=1295481). 4월 1일 표결 현장 사진은 아니다. |
| 6 | `A01_vote_clip.png` | 강원대학교 제47차 대학평의원회 회의록 40쪽, 2025.04.01, [A01P 원문](https://www.kangwon.ac.kr/ko/cmmn/download.do?dn=20250423140105131G8v.pdf&path=/DATA/bbs/394&fn=%EF%BC%88%EC%B5%9C%EC%A2%85%EF%BC%89%EC%A0%9C47%EC%B0%A8%20%EB%8C%80%ED%95%99%ED%8F%89%EC%9D%98%EC%9B%90%ED%9A%8C%20%ED%9A%8C%EC%9D%98%EB%A1%9D.pdf)의 8:12 부결 대목 발췌. |
| 7 | `A02_staff_clip.png` | 강원대학교 제48차 대학평의원회 회의록 7쪽, 2025.04.28, [A02P 원문](https://www.kangwon.ac.kr/ko/cmmn/download.do?dn=20250523100535708tt3.pdf&path=/DATA/bbs/394&fn=%EF%BC%88%EC%B5%9C%EC%A2%85%EF%BC%89%EC%A0%9C48%EC%B0%A8%20%EB%8C%80%ED%95%99%ED%8F%89%EC%9D%98%EC%9B%90%ED%9A%8C%20%ED%9A%8C%EC%9D%98%EB%A1%9D.pdf)의 인력 변경 발언 발췌. |
| 9 | `protest_dongduk_stairs.jpg` | 동덕여대 본관 앞 과잠 시위, 연합뉴스 2024.11.12 촬영, [연합뉴스 2024.11.13 보도](https://www.yna.co.kr/view/AKR20241113138900004). 11월 21일 면담 장면은 아니다. |
| 10 | `D07_final_survey_clip.png` | 동덕여대 공학전환공론화 설문 상세자료 4쪽, 2025.12.02, [D07 원문](https://portal.dongduk.ac.kr/ctt/bb/bulletin?a=fd&b=1&fs=1&p=56963)의 최종 온라인 조사 표 발췌. 51.8%와 71.3%는 서로 다른 분모를 가진다. |

사진 촬영일과 발화·표결일이 다르면 슬라이드 본문에서 구분했다. Noto Serif KR·Noto Sans KR 글꼴의 라이선스 전문은 assets에 동봉했다.
""", encoding="utf-8")

js = (SOURCE / "slides.js").read_text(encoding="utf-8")
js = js.replace("stage.style.transform = `scale(${scale})`;", "stage.style.transform = `translate(-50%, -50%) scale(${scale})`;")
notes = [
"두 사례를 메시지·행동·반응의 순서로 봅니다. 표지 제목은 관찰 질문으로 제시합니다.",
"발표의 분석 단위는 대학의 발화와 후속 행동, 공중의 반응입니다. 공식 결정은 반응 지표 중 하나입니다.",
"교재 81개 변수 목록 가운데 세 조건을 집중적으로 검토합니다. 모든 변수의 작용을 입증했다는 뜻은 아닙니다.",
"두 대학의 자료 유형을 구분합니다. 본부 발화는 공식문서로, 공중 반응은 회의록과 학생·직원 기록 및 보도로 확인합니다.",
"제46차 회의록의 사과는 자료 송부 지연에 한정됩니다. 기한 설명과 요약본에도 심의는 보류됐습니다.",
"제47차에서는 총장이 보안과 기한을 설명했습니다. 출석 20명 가운데 찬성 8명, 반대 12명으로 부결됐습니다.",
"본부는 공무원 35명 구상을 공무원 24명과 외부 전문가 11명으로 수정했습니다. 직원협의회는 그 폭에 이의를 제기했습니다.",
"학부모 대상 글은 수업 차질에 집중했고, 구성원 대상 글은 아직 결정 전이라는 절차 설명을 했습니다. 학생은 논의 중단을 요구했습니다.",
"11월 21일 약 3시간 면담 뒤 논의를 잠정 중단하고 수업 재개에 합의했습니다. 영구 철회로 볼 수 없습니다.",
"51.8%는 교원·학생·직원 집단별 동일 가중을 적용한 공학 전환 선택률입니다. 학생 응답자 중 71.3%는 여대 유지를 선택했습니다.",
"총장 입장문은 우려를 인정하고 2029년 계획을 밝혔습니다. 학생은 12월 9일 총투표 반대 결과를 발표했고 대학이 재응답했습니다.",
"강원대의 평의원회 부결과 동덕여대의 집단행동은 서로 다른 권력 형태입니다. 두 사례의 양보 범위도 달랐습니다.",
"확인 가능한 행동 변화와 남은 반대를 구분합니다. 동일 공중의 신뢰 변화를 측정한 자료는 없습니다.",
"실무 제언은 두 사례에서 관찰된 문제로부터 도출했습니다. 효과가 검증된 보편적 처방으로 제시하지 않습니다.",
"핵심 원문과 이론 문헌을 연결했습니다. 변수 검토표는 별도 파일입니다."
]
new_array = "const SPEAKER_NOTES = " + json.dumps([{"title": titles[i], "script": note, "qa": "수치의 분모와 발화의 범위를 원문에 맞춰 설명합니다."} for i, note in enumerate(notes)], ensure_ascii=False, indent=2) + ";\n\n"
js = re.sub(r"const SPEAKER_NOTES = \[.*?(?=function fitStage\(\))", new_array, js, flags=re.S)
(TARGET / "slides.js").write_text(js, encoding="utf-8")

sources = (TARGET / "sources.html").read_text(encoding="utf-8").replace("v13", "v14").replace("카메룬", "카메론")
(TARGET / "sources.html").write_text(sources, encoding="utf-8")
(TARGET / "README.md").write_text("""# 발표덱 v14\n\n`deck_v13`의 위기 메시지 분석을 유지하면서 `deck_v9`에서 사용한 현장사진·회의록 확대 발췌·수치 대비를 결합한 15장 발표자료다.\n\n- [발표 열기](index.html) · [PDF](deck_v14.pdf)\n- [원자료 인덱스](sources.html) · [81개 변수 검토표](카메론_81개_변수_전수분석.md)\n\n공식 가결, 반대 공중의 수용, 신뢰 회복은 구분한다. 베노이트 전략명은 원문 발언 옆에 표시했다.\n""", encoding="utf-8")
print(f"Built {len(slides)} slides in {TARGET}")
