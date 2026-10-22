"""Apply the narrowly evidenced Benoit analysis to the archived v7 deck."""
from pathlib import Path
import json

root = Path(__file__).resolve().parents[1]
deck = root / "versions" / "deck_v8"

def edit(name, pairs):
    path = deck / name
    data = path.read_text(encoding="utf-8")
    for before, after in pairs:
        count = data.count(before)
        if count != 1:
            raise ValueError(f"{name}: expected one match, got {count}: {before[:70]}")
        data = data.replace(before, after)
    path.write_text(data, encoding="utf-8")

if "베노이트 · 사과의 범위" not in (deck / "index.html").read_text(encoding="utf-8"):
 edit("index.html", [
    ("deck_v7_참고문헌.md", "deck_v8_참고문헌.md"),
    ("deck_v7.pdf", "deck_v8.pdf"),
    ("<div class=\"continuum-note\"><b>적용상의 한계</b>: 교재 표 2-5는 기업의 외부 공중을 기준으로 한 변수 목록이다. 대학 내부 구성원과 평의원회 등 법정 심의기구를 원전의 외부 공중과 기계적으로 동일시하지 않는다.</div>",
     "<div class=\"continuum-note\"><b>분석 순서</b>: Cameron으로 대응의 이동 조건을 설명하고, Benoit으로 실제 발화의 이미지 회복 전략을 판독한다. 발화와 후속 행동은 따로 대조하며, 내부 구성원을 기업의 외부 공중과 동일시하지 않는다.</div>"),
    ("<li><b>설명 중심 대응:</b> 40쪽 의견수렴 요약표를 제시하며 사후 수정 가능성을 구두로 설명함.</li>",
     "<li><b>본부의 해명:</b> 총장은 협상 보안과 촉박한 제출 기한을 들어 사전 협의가 어려웠다고 설명하고, 사후 수정·보완을 약속함 (A01P 4–5쪽).</li>"),
    ("<p>외부의 재정적 마감 압박과 내부 평의원회의 법정 심의 권한이 충돌한 국면으로, 구두 약속만으로는 이미 고착화된 절차적 불신을 넘어서지 못했다.</p>",
     "<p><b>베노이트 · 사과의 범위:</b> 2월 28일 기획처장은 자료 지연을 사과했다 (A03P 5쪽). 통합안 전체에 대한 사과로 확대할 수 없다. 4월 1일의 사후 수정 약속은 당시 실행 결과가 아니었고, 안은 8:12로 부결됐다.</p>"),
    ("<li>수정 가능성 설명 중심 대응</li>", "<li>보안·기한을 들어 사전 협의 지연 해명 (A01P)</li>"),
    ("<li>실제 조직·인력 구성안 조정</li>", "<li><b>베노이트 · 시정조치:</b> 조직·인력 구성안 조정</li>"),
    ("<li>춘천 인력 11명 잔류 확정</li>", "<li>본부 설명상 공무원 11명 춘천 잔류 (A02P)</li>"),
    ("<div><b>대응 범위</b> 수정안 제시와 함께 당일 추가 수정 제한도 남았다 (A02P 3–4쪽).</div>",
     "<div><b>검증 범위</b> 수정안 설명은 확인되나 실제 인사 배치는 미확인. 당일 추가 수정도 제한됐다 (A02P 3–4쪽).</div>"),
    ("<li><b>합의 조건:</b> 향후 논의 재개 시 학생들과 협의를 거치겠다는 취지의 입장문 발표 전제 (D02, D26).</li>",
     "<li><b>본부의 해명:</b> 11월 18일 공식 글은 당시 안이 교무위원회 의제화 전이었다며 ‘단독 결정’ 주장을 부인하고 향후 의견수렴을 예고함 (D26).</li>"),
    ("<p>대학본부는 초기 위기 국면에서 극단적 대치를 해소하기 위해 논의 잠정 중단이라는 실제 대응 조정을 단행했다. 따라서 <em>초기부터 최종 결정까지 일관된 옹호만 유지했다고 분류해서는 안 된다.</em></p>",
     "<p><b>베노이트 · 제한적 부인 → 시정조치:</b> D26의 부인은 ‘이미 단독 결정했다’는 주장에 한정된다. 11월 21일 논의 잠정 중단은 실제 행동 변화다. 공학 전환 방침 자체의 철회는 아니다.</p>"),
    ("<div class=\"thesis-line\"><b>공론화 갈등</b><span>공론화 절차가 마련되었지만, 집단 간 선호가 정면 대립하는 상황에서 집계 규칙(동일 가중 vs 단순합산)을 둘러싼 정당성 논쟁은 해소되지 않았다.</span></div>",
     "<div class=\"thesis-line\"><b>본부의 절차 해명</b><span>본부는 동일 가중을 ‘동등한 참여권’으로 정당화했다 (D08 1–3쪽). 그러나 학생 응답 다수와 최종 권고의 방향은 달랐고, 대표성 논쟁은 계속됐다.</span></div>"),
    ("<div><time>2025.12.03</time><b>본부 방침 발표</b><span>총장: 권고 수용 및 2029년 전환 발표 (D09)</span></div>",
     "<div><time>2025.12.03</time><b>입장문 · 가치 강조</b><span>여성교육의 성과를 강조하며 2029년 전환을 계획 (D09)</span></div>"),
    ("<div class=\"thesis-line\"><b>결정 이후의 평가</b><span>두 대학 모두 공식 의결 절차를 통과하여 제도적 진전을 이루었으나, 반대 공중의 핵심 요구 불일치와 절차적 불신은 공식 결정 이후에도 지속되었다.</span></div>",
     "<div class=\"thesis-line\"><b>메시지와 행동</b><span>동덕여대 입장문의 전통·미래 강조는 베노이트의 긍정적 이미지 강조·초월로 읽힌다 (D09). 2029년 계획과 학칙 개정은 확인되지만 여대 유지 요구의 수용은 아니다.</span></div>"),
    ("<div class=\"cf-head\">대응 <small>조정한 사항</small></div>", "<div class=\"cf-head\">메시지와 행동 <small>베노이트 전략 · 확인된 조정</small></div>"),
    ("<div class=\"cf-cell\"><b>조직·인력 구성안 조정</b><br><small>공무원 35→24명 + 외부 전문가 11명</small></div>",
     "<div class=\"cf-cell\"><b>지연 사과 → 시정조치</b><br><small>공무원 35→24명 + 외부 전문가 11명 제시</small></div>"),
    ("<div class=\"cf-cell\"><b>논의 중단, 공론화 절차</b><br><small>2024 잠정 중단 + 2029 전환 유예</small></div>",
     "<div class=\"cf-cell\"><b>제한적 부인 → 잠정 중단</b><br><small>전통·미래 강조, 2029 전환 계획</small></div>"),
    ("<div><b>비교 결과</b><span>두 대학 모두 핵심 정책을 옹호했지만, 반대 공중의 영향력, 요구의 성격, 의사결정 구조에 따라 수용의 대상과 범위가 달랐다.</span></div>",
     "<div><b>비교 결과</b><span>Cameron의 조건 분석에 메시지 분석을 더하면, 두 대학 모두 정책 목표를 지키면서 해명 뒤 일부 행동을 조정했음을 확인할 수 있다.</span></div>"),
    ("<footer class=\"source-footer\"><span>Cancel et al. (1997) · Cameron et al. (2001) · 황성욱 (2014)</span><span>11 / 15</span></footer>",
     "<footer class=\"source-footer\"><span>Cancel et al. (1997) · Cameron et al. (2001) · Benoit (1997) · A01P–A03P · D09 · D26</span><span>11 / 15</span></footer>"),
])

path = deck / "slides.js"
data = path.read_text(encoding="utf-8")
needle = "\n];"
pos = data.find(needle, data.index("const SPEAKER_NOTES = ["))
if pos < 0:
    raise ValueError("Speaker notes array end not found")
additions = {
    3: "보조 분석으로 베노이트의 이미지 회복 전략을 사용합니다. Cameron은 대응의 이동 조건, Benoit은 실제 메시지의 기능을 설명합니다. 전략명은 원문 발화로 확인될 때만 붙입니다.",
    6: "제46차 회의에서 기획처장이 늦은 자료 제공을 사과한 것은 그 절차 문제에 한정된 사과입니다. 제47차에서 총장은 협상 보안과 제출 기한을 해명했고 사후 수정을 약속했으나, 그날의 표결은 부결이었습니다.",
    7: "제48차 회의록과 대학 공식 보도문은 35명 전원 공무원 구상에서 공무원 24명과 외부 전문가 11명 구성으로 바꾼 안을 설명합니다. 이를 제한적 시정조치로 분류합니다. 실제 인사 배치 결과는 별도 확인되지 않았습니다.",
    8: "11월 18일 공식 글은 교무위원회 의제화 전이었다며 이미 독단적으로 결정했다는 주장을 부인합니다. 부인의 대상은 그 주장에 한정됩니다. 11월 21일의 논의 잠정 중단은 실제 행동 조정으로 봅니다.",
    9: "12월 8일 본부 자료는 동일 가중을 동등한 참여권으로 설명합니다. 이는 본부의 절차 해명이며, 해당 규칙에 학생 측이 동의했다는 근거는 아닙니다.",
    10: "12월 3일 입장문은 여성교육의 성과와 미래의 사명을 강조합니다. 베노이트의 긍정적 이미지 강조와 초월로 읽을 수 있습니다. 후속 문서에서는 학칙 개정이 확인되지만 학생들의 여대 유지 요구가 수용된 것은 아닙니다.",
    11: "두 사례 모두 설명과 행동을 구분했습니다. 강원대는 지연 사과와 인력안 수정, 동덕여대는 제한적 부인과 논의 중단·전환 일정 조정이 확인됩니다. 사후 수용도와 실제 인사 배치 등은 자료 밖에 있습니다.",
}
patch = "\n".join(f"SPEAKER_NOTES[{i-1}].script += {json.dumps(' ' + note, ensure_ascii=False)};" for i, note in additions.items())
data = data[:pos+3] + "\n" + patch + data[pos+3:]
path.write_text(data, encoding="utf-8")

for name in ["README.md", "deck_v7_참고문헌.md", "deck_v7_수정내역.md", "speaker_script.md"]:
    pass
print("v8 slide content and speaker notes updated")
