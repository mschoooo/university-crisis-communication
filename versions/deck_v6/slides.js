const slides = Array.from(document.querySelectorAll('.slide'));
const stage = document.getElementById('stage');
const count = document.getElementById('count');
const notesDrawer = document.getElementById('notes-drawer');
const notesTitle = document.getElementById('notes-title');
const notesBody = document.getElementById('notes-body');
const notesQa = document.getElementById('notes-qa');
const tocModal = document.getElementById('toc-modal');
const dataModal = document.getElementById('data-modal');
let index = 0;

const motionPlan = [
  ['.case-plate p b, .vote-row > b, .staff-change strong, .before-after strong, .survey-side strong, .aftermath-card strong', 'number'],
  ['.vote-track i, .compare-line i', 'bar'],
  ['.timeline > div, .dongduk-timeline > div, .vote-row, .before-after > div, .survey-side > div, .aftermath-card, .compare-rows > div, .reference-column p, .conclusion-list > div', 'row']
];
slides.forEach(slide => {
  motionPlan.forEach(([selector, type]) => {
    slide.querySelectorAll(selector).forEach(element => element.dataset.motion = type);
  });
  slide.querySelectorAll('[data-motion]').forEach((element, order) => {
    element.style.setProperty('--motion-delay', `${Math.min(order * 85, 510)}ms`);
  });
});

const SPEAKER_NOTES = [
  {
    "title": "Slide 01 · 표지 및 문제의식",
    "script": "안녕하십니까. 위기관리(029) 중간고사 대체 과제 발표를 맡은 부산대학교 미디어커뮤니케이션학과 조민성(202206251)입니다. 오늘날 대학 구조개혁은 학령인구 급감 속에서 불가피한 결단이지만, 내부 구성원에게는 정체성과 직무를 위협하는 심각한 갈등을 초래합니다. 본 연구는 강원대–강릉원주대 국립대 통합과 동덕여대 남녀공학 전환 추진 사례를 분석합니다. 두 대학 모두 공식 심의와 학칙 개정이라는 제도적 진전을 이루었으나, 구성원의 수용 양상은 크게 달랐습니다. 왜 공식 결정의 통과가 곧바로 내부 공중의 수용으로 이어지지 못하는가? 정황적 수용 이론(Contingency Theory)과 절차적 공정성 논의를 바탕으로, 조직의 전략적 선택을 설명하는 조건들의 조합과 그 한계를 검토하겠습니다.",
    "qa": "[핵심 문제의식] 본 발표의 목적은 단순한 성공·실패 이분법이 아니라, 공식 의사결정의 진전과 내부 공중의 수용이라는 두 차원을 분리하여 조직의 전략적 선택과 그 한계를 객관적으로 평가하는 데 있습니다."
  },
  {
    "title": "Slide 02 · 연구 질문 및 평가 기준",
    "script": "연구 질문과 분석 기준을 말씀드리겠습니다. 본 연구는 두 가지 핵심 질문을 탐구합니다. 첫째, RQ1: 두 대학은 구조개편 갈등에 어떻게 대응했으며, 그 전략적 선택과 관련된 내·외부 변수는 무엇인가? 둘째, RQ2: 그러한 대응은 공식 의사결정과 반대 공중의 수용이라는 측면에서 어떤 성과와 한계를 보였는가? 이를 체계적으로 평가하기 위해 발표자는 세 가지 분석 기준을 설정했습니다. 첫째, 공식 의사결정의 진전입니다. 둘째, 핵심 요구의 실질적 반영입니다. 셋째, 결정 이후의 수용입니다. 양 대학의 공식 회의록, 권고안, 설문 원자료 등 1차 사료를 바탕으로 이 세 기준을 검토하겠습니다.",
    "qa": "[분석 기준의 성격] 세 평가 기준은 단일한 성공·실패 판정을 넘어, 정책 추진의 제도적 진전과 구성원의 사후 수용 사이의 괴리를 포착하기 위해 발표자가 설정한 분석 틀입니다."
  },
  {
    "title": "Slide 03 · 정황적 수용 이론 (외부 변수와 내부 변수)",
    "script": "본 연구의 핵심 이론인 정황적 수용 이론을 검토하겠습니다. 교재 『PR커뮤니케이션』 제2장 표 2-5는 조직을 둘러싼 다양한 상황변수를 외부 변수와 내부 변수로 대별합니다. 외부 변수에는 위협, 업계 환경, 일반적인 정치·사회·문화 환경, 외부 공중의 특성이 포함되며, 내부 변수에는 조직의 특성, PR커뮤니케이션 부서의 특성, 최고 의사결정자의 특성, 내부적 위협, 개인적 특성, 관계의 성격이 포함됩니다. 조직은 이러한 조건들의 결합에 따라 순수 옹호(Pure Advocacy)에서 순수 수용(Pure Accommodation)에 이르는 연속선 상에서 입장을 동태적으로 이동합니다. 다만, 원전이 상정한 기업의 외부 공중과 달리, 대학의 구성원은 법정 심의기구 참여 권한이나 소속성을 지니므로 기계적 대입에는 개념적 주의가 필요합니다.",
    "qa": "[이론적 유의점] 이론의 발전 과정에서 초기 매트릭스 제시 이후 사전성향적 변수, 상황변수, 수용 제한 요인에 대한 구분이 심화되었습니다. 교재의 공식 한국어 번역 변수명을 존중하되, 대학 내부 구성원에게 적용할 때의 거버넌스 맥락을 고려해야 합니다."
  },
  {
    "title": "Slide 04 · 사례 A (강원대) 위기 발생과 초기 대응 분석",
    "script": "강원대의 위기 발생 국면입니다. 2024년 7월 글로컬위원회는 통합 지연 시 사업비 50% 삭감을 경고했고, 본부는 2,150억 원 규모의 사업 추진 압박 속에서 2025년 2월 20일 교육부에 신청서를 먼저 제출했습니다. 이어 2월 28일 평의원회 당일에야 257쪽 문서를 배부했고, 삼척 지역 반발로 회의가 무산되었습니다. 결국 4월 1일 제47차 평의원회에서 본부의 설명에도 불구하고 8 대 12로 부결되었습니다. 이 국면에서는 외부의 재정·사업비 위협 및 추진 일정과 내부의 대학 의사결정 구조, 직역·캠퍼스별 이해관계, 자료 공개 절차 문제가 복합적으로 작용했습니다. 즉, 외부 압박과 내부 심의 절차의 충돌 속에서 절차적 갈등이 심화된 것입니다.",
    "qa": "[인과관계 해석 주의] 특정 단일 변수가 부결의 유일한 원인으로 입증된 것은 아니며, 재정적 마감 압박과 심의 절차의 불일치가 결합하여 심의 교착을 초래한 상황으로 해석합니다."
  },
  {
    "title": "Slide 05 · 사례 A (강원대) 대응의 변화 분석: 설명 약속에서 실제 조정으로",
    "script": "4월 1일 부결 이후 강원대 본부의 대응 변화를 살펴보겠습니다. 4월 1일 이전 본부는 조건부 가결을 요청하고 사후 수정 가능성을 설명하는 구두 설득 중심이었습니다. 반면 4월 28일 이전에는 핵심 쟁점이었던 대학혁신전략실 공무원 차출을 35명에서 24명으로 줄이고 외부 전문가 11명을 충원하여 춘천 인력 11명을 잔류시키는 실제 조직안 조정을 단행했습니다. 이에 따라 제48차 평의원회에서 15:6으로 가결되었습니다. 이는 설명 중심 대응에서 부분적인 행동적 수용으로 전환한 사례로 해석할 수 있습니다. 다만, 두 회의의 출석 인원이 20명과 21명으로 다르고, 무기명 표결이므로 개인별 태도 변화를 단정할 수 없으며, 당일 추가 수정 제안을 제한하는 옹호적 대응도 공존했습니다.",
    "qa": "[표결 해석의 한계] 8:12에서 15:6으로의 변화는 개인 위원의 태도 전향을 직접 증명하지 않으며, 조직안 수정 외에도 마감 시한 임박 등 복합 요인이 작용했을 가능성을 함께 명시합니다."
  },
  {
    "title": "Slide 06 · 사례 A (강원대) 강원대 종합 평가",
    "script": "강원대 사례의 종합 평가입니다. 세 평가 축으로 정리하면 다음과 같습니다. 첫째, 성과 측면에서 대학본부는 통합이라는 핵심 정책 목표를 옹호 유지하면서도, 조직·인력 구성의 일부를 실제로 수정하여 공식 심의의 교착 상태를 해소하고 15:6 가결을 이끌어냈습니다. 둘째, 한계 측면에서는 신청서 선제출, 검토 시간 부족, 당일 추가 수정 제안 제한 등 의사결정 절차를 둘러싼 갈등이 여전히 남았습니다. 셋째, 공식 가결과 통합 출범이라는 제도적 진전은 명확하지만, 직원들의 불신 해소나 구성원 전체의 정서적 수용까지 완결되었다고 보기는 어렵습니다. 부결 이후의 실질적 조정에는 성과가 있었으나, 사전 협의와 절차적 갈등 관리에는 한계가 있었습니다.",
    "qa": "[종합 평가 논리] 성공·실패의 이분법 대신, 제도적 진전 달성이라는 성과와 절차적 정당성 미흡이라는 한계를 병렬적으로 평가하여 학술적 균형을 유지했습니다."
  },
  {
    "title": "Slide 07 · 사례 B (동덕여대) 초기 위기와 논의 잠정 중단",
    "script": "동덕여대의 초기 갈등 국면입니다. 2024년 9월과 11월 대학비전혁신추진단에서 공학 전환 방안이 논의되었으나, 11월 7일 학내 커뮤니티로 소문이 확산되었습니다. 학생 대표단의 사전 협의 요구와 11월 11일 면담 취소 통지가 이어지며 본관 점거와 시위가 폭발했습니다. 대학본부는 11월 21일 총학생회와의 면담을 통해 남녀공학 논의 잠정 중단과 수업 재개에 합의했습니다. 이 국면은 대학의 115년 여성교육 정체성, 추진단 중심의 의사결정 방식, 학생 집단행동과 사전 정보공개 시점이 맞물린 상황이었습니다. 특히 본부가 11월 21일 논의 잠정 중단을 수용한 것은 실제 대응 조정에 해당하므로, 초기부터 최종 결정까지 일관된 옹호만 유지했다고 보아서는 안 됩니다.",
    "qa": "[모니터링 평가 주의] 정보공개 시점과 징후 관리의 적절성은 검토 대상이지만, 대학 내부에 이슈 모니터링 자체가 전혀 없었다고 단정하지는 않습니다."
  },
  {
    "title": "Slide 08 · 사례 B (동덕여대) 공론화 절차와 의견 충돌",
    "script": "2025년 동덕여대 공론화 과정입니다. 교원·학생·직원·동문 각 3인씩 12인으로 구성된 공론화위원회와 48인 숙의기구가 운영되었습니다. 12인 학생단의 여대 유지 공표 비율은 숙의 전 80%에서 숙의 후 50%로 완화되었으나, 유효 응답 모수가 미공개되어 개인별 태도 변화로 단정할 수는 없습니다. 한편 3,176명이 참여한 대규모 설문에서는 극단적인 의견 충돌이 확인되었습니다. 교원(76%)과 직원(68.5%)은 공학 전환을 지지한 반면, 학생 응답(2,889명)은 71.3%가 여대 유지를 지지했습니다. 1:1:1 동일 가중 시 공학 전환 51.8%였으나, 무가중 단순합산 시 여대 유지가 66.1%였습니다. 상충하는 복수 공중의 존재와 집계 규칙을 둘러싼 정당성 논쟁이 지속된 것입니다.",
    "qa": "[가중 방식 평가] 가중 방식이 통계적으로 잘못되었다거나 절차를 위반했다고 단정하지 않으며, 집단 간 선호가 정면 대립하는 상황에서 집계 규칙 합의가 얼마나 중요한 쟁점인지를 분석합니다."
  },
  {
    "title": "Slide 09 · 사례 B (동덕여대) 공식 결정과 후속 갈등",
    "script": "공론화 권고 이후의 공식 결정과 갈등입니다. 2025년 12월 2일 공론화위원회는 9:2:1로 공학 전환 권고안을 가결했고, 본부는 12월 3일 권고안 수용과 2029년 전환 방침을 발표했습니다. 이에 반발한 학생 총투표(12/3~7)에서는 85.7%라는 압도적인 반대가 표출되었습니다. 2026년 1월 12일 대학평의원회에서 학칙 개정안이 8:2로 가결되었으나 학생위원 2명은 서명을 거부했고, 2월 26일 학칙이 개정 공포되었습니다. 본부는 공학 전환이라는 핵심 정책을 옹호 관철했고 절차적 관문을 밟았으나, 학생 공중의 핵심 요구는 수용되지 못했습니다. 한편 2029년 전환은 설문 원안에 포함된 안이었으며, 수시 접수는 9월이었으므로 입시 지원자 감소를 12월 발표의 직접 결과로 볼 수는 없습니다.",
    "qa": "[시간 순서와 인과관계] 2029년 유예는 사후 양보가 아니라 사전 제시된 설문 선택지였으며, 수시 감소 역시 12월 발표 이전의 사건이므로 직접적 인과 귀속을 배제했습니다."
  },
  {
    "title": "Slide 10 · 사례 B (동덕여대) 동덕여대 종합 평가",
    "script": "동덕여대 사례의 종합 평가입니다. 본 연구는 동덕여대의 대응을 단일한 유형으로 고정하지 않고 세 국면으로 구분합니다. ① 2024년 초기에는 논의 잠정 중단이라는 실제 행동 조정을 실행했습니다. ② 2025년 중반에는 4단위 공론화위원회와 숙의 절차를 개설하여 절차적 수용을 보였습니다. ③ 그러나 2025년 말부터 2026년 초까지는 1:1:1 가중 규칙과 남녀공학 전환 방침, 학칙 개정을 일관되게 옹호 관철했습니다. 결론적으로 대학본부는 국면과 쟁점에 따라 유연한 절차적 조정을 시도했으나, 최종적으로 학생들의 핵심 요구인 여대 정체성 유지에는 수용적인 입장을 취하지 않았습니다. 즉, 절차적 수용과 핵심 정책 옹호가 공존한 것입니다.",
    "qa": "[수용 유형화의 정교화] 단일한 수사 수용이라는 평가 대신, 국면별·쟁점별로 행동 조정, 절차적 수용, 정책 옹호가 다르게 나타났음을 입체적으로 논증했습니다."
  },
  {
    "title": "Slide 11 · 두 대학 직접 비교 (조건 → 대응 → 결과)",
    "script": "두 대학의 비교 분석입니다. 두 대학 모두 통합과 공학 전환이라는 조직의 핵심 정책 목표를 끝까지 유지했습니다. 그러나 조정한 사항과 수용의 범위는 현저히 달랐습니다. 강원대는 조직·인력 배치라는 가분적 쟁점을 수정안의 매개체로 삼았고, 평의원회의 법정 거부권이라는 내부 조건 속에서 15:6 가결을 이끌어냈습니다. 반면 동덕여대는 여대 정체성이라는 비가분적 쟁점과 교원·직원 대 학생이라는 상충하는 복수 공중 속에서 공론화 절차를 개설했으나, 집계 규칙과 정책 결론을 옹호했습니다. 비교 결론은 두 가지입니다. 첫째, 반대 공중의 영향력, 요구의 성격, 의사결정 구조에 따라 수용의 대상과 범위가 달랐습니다. 둘째, 공식 절차 통과가 곧 반대 집단의 수용이나 관계 회복을 의미하지는 않습니다.",
    "qa": "[비교의 핵심 시사점] 두 대학 모두 공식 결정은 통과시켰으나, 강원대는 직원 관계 회복 과제를, 동덕여대는 학생 불신과 대표성 논쟁을 남겼다는 점에서 괴리의 구조를 확인했습니다."
  },
  {
    "title": "Slide 12 · 사전 위기관리 (Heath & Sturges)",
    "script": "사전 위기관리 관점에서의 검토입니다. Heath의 이슈관리와 Sturges의 위기 이전 커뮤니케이션에 비추어 볼 때, 강원대에서는 조직·인력 배치와 심의 절차에 대한 문제 제기가 조기 위험 징후로 관찰되었습니다. 본부는 선제출 후 심의 및 수정안을 제시했으나, 신청 전 핵심 이해관계와 수정 가능 범위를 선제 공개했다면 갈등을 완화할 수 있었을 것입니다. 동덕여대에서는 공학 전환 논의에 대한 사전 협의 요구가 조기 징후였으나, 소문 확산 이후에야 대응이 이루어졌습니다. 공식 논의 초기부터 대안과 절차를 투명하게 공개하는 조기 협의가 유효했을 것입니다. 단, 위기가 발생했다는 사실만으로 조직에 사전 모니터링이 없었다고 단정해서는 안 되며, 대응 시점의 적절성을 비교 평가해야 합니다.",
    "qa": "[사전 모니터링 단정 배제] 모니터링의 부재를 단정하는 대신, 확인된 조기 징후와 실제 조직 대응 시점 사이의 시간적 간극을 객관적으로 대조했습니다."
  },
  {
    "title": "Slide 13 · 절차적 공정성 (대표성 · 정보 충분성 · 수정 가능성)",
    "script": "절차적 공정성 관점에서의 분석입니다. Leventhal의 절차 규칙과 Tyler의 관계적 모델에 기초하여 발표자는 세 가지 검토 기준을 적용했습니다. 첫째, 대표성 기준에서 강원대는 직역·캠퍼스별 요구가 평의원회 심의에 반영되는 방식이 문제되었고, 동덕여대는 집단별 1:1:1 가중 규칙을 둘러싼 대표성 논쟁이 격화되었습니다. 둘째, 정보의 충분성 기준에서 강원대는 선제출 및 257쪽 당일 배부가, 동덕여대는 공학 논의의 사전 공개 지연이 쟁점이 되었습니다. 셋째, 수정 가능성 기준에서 강원대는 부결 후 수정안 재상정이 작동했으나 당일 추가 수정은 제한되었고, 동덕여대는 학생 반대 의견이 최종 결정에 반영되지 못했습니다. 합법적 절차 통과와 이해관계자의 주관적 공정성 인식은 엄격히 구분되어야 합니다.",
    "qa": "[법적 위반 단정 배제] 규정 위반이나 위법성을 단정하는 것이 아니라, 절차의 합법성과 구성원이 체감하는 절차적 정당성 사이의 괴리를 평가 기준으로 삼았습니다."
  },
  {
    "title": "Slide 14 · 결론 및 실무 제언 (시점 · 규칙 · 행동)",
    "script": "결론 및 실무 제언을 말씀드리겠습니다. 본 연구는 대학 구조개편 갈등 관리를 위해 시점, 규칙, 행동이라는 세 가지 원칙을 제언합니다. 첫째, 시점의 원칙입니다. 반발 이후의 설명보다 결정 이전의 협의가 선행되어야 합니다. 정책 확정 전에 핵심 우려와 수정 가능 범위를 공개해야 합니다. 둘째, 규칙의 원칙입니다. 참여 기회뿐 아니라 의사결정 방식을 사전에 합의해야 합니다. 공론화의 대표성, 가중 방식, 최종 결정권과 이의제기 절차를 사전에 명확히 해야 합니다. 셋째, 행동의 원칙입니다. 수용의 의사 표명보다 수용의 결과를 문서화하여 공개해야 합니다. 마지막으로 강조하고 싶은 테제는, 절차의 개설과 공식 결정의 가결은 구성원의 수용과 같은 지표가 아니라는 점입니다.",
    "qa": "[실무 제언의 도출] 본 제언은 검증되지 않은 가상의 제도 신설이 아니라, 두 대학 사례에서 관찰된 절차적 병목과 갈등 지점을 해결하기 위한 실무적 커뮤니케이션 원칙으로 정립했습니다."
  },
  {
    "title": "Slide 15 · 참고문헌 및 출처",
    "script": "마지막으로 분석에 활용한 참고문헌과 사건 기록입니다. 핵심 이론 문헌으로는 Cancel et al.(1997, 1999), Cameron et al.(2001), 황성욱(2014)의 정황적 수용 이론 및 교재 표 2-5, Heath(1997), Sturges(1994), Wilcox & Cameron(2005)의 갈등 생애주기 문헌, Leventhal(1980)과 Tyler(1988)의 절차적 공정성 연구를 인용했습니다. 사건 기록으로는 강원대학교 평의원회 회의록(A01P, A02P, A03P)과 공식 보도자료, 동덕여대 소통 일지(D26), 합의문(D02), 공론화위원회 권고안(D06), 설문 상세자료(D07), 회의록(D08), 총투표 보도(D10), 학칙 개정 공고(D22) 등 1차 사료를 엄밀하게 대조했습니다. 이상으로 발표를 마치겠습니다. 경청해 주셔서 감사합니다.",
    "qa": "[사료 비판 준수] 모든 서지는 실제 확보된 원자료와 수업 문헌에 기초하며, 미확인된 출처나 임의의 데이터는 일절 배제했습니다."
  }
];

function fitStage() {
  const scale = Math.min(window.innerWidth / 1600, window.innerHeight / 900);
  stage.style.transform = `scale(${scale})`;
  stage.style.transformOrigin = 'center center';
}

function updateNotes() {
  const item = SPEAKER_NOTES[index] || { title: "", script: "", qa: "" };
  const heading = slides[index].querySelector('h1, h2');
  if (notesTitle) notesTitle.textContent = `Slide ${String(index + 1).padStart(2, '0')} · ${heading ? heading.textContent.trim().replace(/\s+/g, ' ') : item.title}`;
  if (notesBody) notesBody.textContent = item.script;
  if (notesQa) notesQa.textContent = item.qa;
  const detail = document.getElementById("notes-detail");
  if (detail) detail.textContent = (window.ARCHIVE_DETAILS || [])[index] || "";
}

function show(next) {
  index = (next + slides.length) % slides.length;
  slides.forEach((slide, i) => slide.classList.toggle('active', i === index));
  const current = slides[index];
  current.classList.remove('motion-in');
  void current.offsetWidth;
  if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) current.classList.add('motion-in');
  count.textContent = `${index + 1} / ${slides.length}`;
  history.replaceState(null, '', `#${index + 1}`);
  updateNotes();
}

function togglePanel(panel) {
  const isOpen = panel.classList.contains('open');
  [notesDrawer, tocModal, dataModal].forEach(p => p && p.classList.remove('open'));
  if (!isOpen && panel) panel.classList.add('open');
}

document.getElementById('prev').addEventListener('click', () => show(index - 1));
document.getElementById('next').addEventListener('click', () => show(index + 1));
document.getElementById('btn-notes').addEventListener('click', () => togglePanel(notesDrawer));
document.getElementById('btn-toc').addEventListener('click', () => togglePanel(tocModal));
document.getElementById('btn-data').addEventListener('click', () => togglePanel(dataModal));
document.getElementById('btn-fs').addEventListener('click', () => {
  if (!document.fullscreenElement) document.documentElement.requestFullscreen().catch(() => {});
  else document.exitFullscreen().catch(() => {});
});

document.querySelectorAll('.close-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    [notesDrawer, tocModal, dataModal].forEach(p => p && p.classList.remove('open'));
  });
});

document.querySelectorAll('.toc-item').forEach(btn => {
  btn.addEventListener('click', () => {
    const target = Number(btn.getAttribute('data-slide') || '1') - 1;
    show(target);
    tocModal.classList.remove('open');
  });
});

window.addEventListener('keydown', (event) => {
  if (['ArrowRight', 'PageDown', ' '].includes(event.key)) {
    event.preventDefault();
    show(index + 1);
  } else if (['ArrowLeft', 'PageUp'].includes(event.key)) {
    event.preventDefault();
    show(index - 1);
  } else if (event.key === 'Home') {
    event.preventDefault();
    show(0);
  } else if (event.key === 'End') {
    event.preventDefault();
    show(slides.length - 1);
  } else if (event.key === 'n' || event.key === 'N') {
    event.preventDefault();
    togglePanel(notesDrawer);
  } else if (event.key === 'm' || event.key === 'M') {
    event.preventDefault();
    togglePanel(tocModal);
  } else if (event.key === 'd' || event.key === 'D') {
    event.preventDefault();
    togglePanel(dataModal);
  } else if (event.key === 'f' || event.key === 'F') {
    event.preventDefault();
    document.getElementById('btn-fs').click();
  } else if (event.key === 'Escape') {
    [notesDrawer, tocModal, dataModal].forEach(p => p && p.classList.remove('open'));
  }
});

window.addEventListener('resize', fitStage);
window.addEventListener('hashchange', () => {
  const target = Number(location.hash.replace('#', ''));
  if (Number.isInteger(target) && target >= 1 && target <= slides.length && target - 1 !== index) {
    show(target - 1);
  }
});
fitStage();
const initial = Number(location.hash.replace('#', ''));
show(Number.isFinite(initial) && initial >= 1 && initial <= slides.length ? initial - 1 : 0);
