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
  ['.stat-primary, .survey-major b, .vote-block b, .timeline-step b, .case-plate p b, .staff-change b, .analysis-box b, .big-stat, .delib-stat-item b, .vote-card b', 'number'],
  ['.vote-track i, .delib-bar i, .progress-bar i, .continuum-track i, .survey-bar i, .bar-fill', 'bar'],
  ['.timeline-step > div, .parallel-plate, .deep-left, .archive-plate, .criteria article, .var-panel, .reference-column, .aftermath-card, .vote-card', 'row']
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
    "title": "Slide 02 · 결정과 수용",
    "script": "연구 질문과 분석 기준을 말씀드리겠습니다. 본 연구는 두 가지 핵심 질문을 탐구합니다. 첫째, RQ1: 두 대학은 구조개편 갈등에 어떻게 대응했으며, 그 전략적 선택과 관련된 내·외부 변수는 무엇인가? 둘째, RQ2: 그러한 대응은 공식 의사결정과 반대 공중의 수용이라는 측면에서 어떤 성과와 한계를 보였는가? 이를 체계적으로 평가하기 위해 발표자는 세 가지 분석 기준을 설정했습니다. 첫째, 공식 의사결정의 진전입니다. 둘째, 핵심 요구의 실질적 반영입니다. 셋째, 결정 이후의 수용입니다. 양 대학의 공식 회의록, 권고안, 설문 원자료 등 1차 사료를 바탕으로 이 세 기준을 검토하겠습니다. 특히 동덕여대의 경우 학생 총투표(12/3~7)가 학칙 개정(1/12, 2/26)보다 앞서 진행되었음을 시간 순서상 명확히 확인했습니다.",
    "qa": "[시간 순서 교정] 동덕여대 학생 총투표(12/3~7)는 공론화위 권고 직후 총장 발표에 반발해 실시된 것으로, 이듬해 1월 평의원회 심의 및 2월 학칙 개정보다 앞선 사건임을 엄밀히 대조했습니다."
  },
  {
    "title": "Slide 03 · 대응을 바꾸는 조건",
    "script": "본 연구의 이론적 기둥인 정황적 수용 이론을 검토하겠습니다. 교재 『PR커뮤니케이션』 제2장 표 2-5는 조직을 둘러싼 다양한 상황변수를 외부 변수와 내부 변수로 대별합니다. 외부 변수에는 위협, 업계 환경, 일반적인 정치·사회·문화 환경, 외부 공중의 특성이 포함되며, 내부 변수에는 조직의 특성, PR 부서의 특성, 최고 의사결정자의 특성, 내부적 위협, 개인적 특성, 관계의 성격이 포함됩니다. 조직은 이러한 조건들의 결합에 따라 순수 옹호(Pure Advocacy)에서 순수 수용(Pure Accommodation)에 이르는 연속선 상에서 입장을 동태적으로 이동합니다. 다만 기업의 외부 공중과 달리, 대학의 교수·직원·학생은 법정 심의기구 참여권과 소속성을 지닌 내부 주권자이므로 기계적 대입에는 개념적 주의가 필요합니다.",
    "qa": "[이론적 유의점] 이론의 발전 과정에서 초기 매트릭스 제시 이후 사전성향적 변수, 상황변수, 수용 제한 요인에 대한 구분이 심화되었습니다. 교재의 변수 분류를 존중하되 대학 거버넌스의 특수성을 고려했습니다."
  },
  {
    "title": "Slide 04 · 구조개편의 배경",
    "script": "두 대학의 구조개편 추진 배경입니다. 두 대학 모두 학령인구 급감 속에서 생존을 위한 대규모 변화를 결단했습니다. 좌측의 강원대–강릉원주대는 정부의 '글로컬대학30' 사업에 선정되어 5년간 2,150억 원의 국비·지방비 지원을 연계하고, 춘천·삼척·강릉·원주를 잇는 '1도 1국립대' 통합 모델을 추진했습니다. 우측의 동덕여대는 사립 여대의 중장기 발전계획인 'VISION 2040'의 일환으로 디자인·IT 첨단 분야 융합을 위한 남녀공학 개편 방안을 검토했습니다. 그러나 한 대학은 재정 지원 연계 통합이었고, 다른 대학은 115년 여성교육 정체성의 전환이라는 점에서 근본적 차이가 존재했습니다.",
    "qa": "[사례 배경의 비교 가능성] 대규모 구조개편이라는 공통 외적 압박 아래, 국립대 재정 통합 모델과 사립 여대의 정체성 전환 모델이라는 대조적 조건이 정황 이론의 최적의 분석 환경을 제공합니다."
  },
  {
    "title": "Slide 05 · 위기의 발생",
    "script": "위기의 발생 과정입니다. 두 대학 모두 사전 협의와 공식 설명이 부족한 상태에서 절차가 진행되어 위기가 촉발되었습니다. 강원대는 2024년 7월 글로컬위의 '50% 삭감 경고' 속에서 평의원회 심의 전 교육부에 통합신청서를 먼저 제출했습니다. 그리고 2월 28일 평의원회 당일에야 257쪽 문서를 배부했고, 삼척 지역 반발로 회의가 무산되었습니다. 동덕여대는 11월 5일 비전추진단에서 공학 전환 방안이 동의되었으나 11월 7일 소문이 학내로 유출되었고, 11일 면담 취소 통보 직후 본관 점거와 래커 시위로 폭발했습니다. 공식 정보 제공 이전에 '선제출'과 '소문'이 앞서며 밀실 추진 인식이 급속히 고착화된 것입니다.",
    "qa": "[Sturges(1994) 적용] 공식 설명 이전에 비공식 소문이나 일방적 선제출이 발생하면 '밀실 규범'이 즉각 고착화되어 사후 설명만으로는 여론을 되돌리기 어렵다는 점을 보여줍니다."
  },
  {
    "title": "Slide 06 · 선제출과 부결",
    "script": "강원대 1차 표결 국면입니다. 2025년 4월 1일 제47차 평의원회에서 본부는 2,150억 사업비 무산 위기를 강조하며 40쪽 요약표를 배부하고 조건부 가결을 요청했습니다. 그러나 핵심 쟁점이었던 '대학혁신전략실 공무원 35명 강릉 차출' 원안이 수정되지 않았다는 점에 대해 평의원들이 거세게 반발했습니다. 우측의 공식 회의록 40쪽을 보시면, 무기명 투표 결과 찬성 8표, 반대 12표로 최종 부결되었습니다. 외부의 막대한 재정 위협에도 불구하고 내부 심의기구인 평의원회가 법정 거부권을 실제로 행사하여 본부의 일방적 옹호 입장을 저지한 것입니다.",
    "qa": "[법정 거부권의 작동] 대학평의원회의 법정 심의 권한이 단순 자문이 아닌 실질적 거부권(Veto Point)으로 작동하여 대학본부의 강경 옹호에 제동을 걸었습니다."
  },
  {
    "title": "Slide 07 · 약속에서 수정으로",
    "script": "부결 이후 27일간 강원대 본부의 대응 변화입니다. 4월 1일 이전 본부는 조건부 가결을 요청하는 구두 설득 중심이었습니다. 그러나 4월 28일 제48차 평의원회를 앞두고 본부는 핵심 쟁점이었던 대학혁신전략실 공무원을 35명에서 24명으로 줄이고 외부 전문가 11명을 충원하여 춘천 인력 11명을 잔류시키는 실질적인 조직안 수정을 단행했습니다. 우측 7쪽 회의록이 이를 증명합니다. 그 결과 4월 28일 표결에서 15 대 6으로 가결되었습니다. 이는 설명 중심에서 부분적인 행동적 수용으로 전환한 성과입니다. 다만 출석 인원이 20명과 21명으로 다르고, 당일 추가 수정 제안을 차단하는 옹호적 대응도 공존했습니다.",
    "qa": "[표결 해석의 한계] 8:12에서 15:6으로의 변화는 무기명 투표이므로 개인별 전향을 단정할 수 없으며, 조직안 수정과 마감 시한 압박이 복합 작용한 결과로 해석합니다."
  },
  {
    "title": "Slide 08 · 소문과 갈등",
    "script": "동덕여대의 초기 갈등과 대응 조정입니다. 2024년 11월 11일 본관 점거와 계단 시위 등 물리적 충돌이 격화되자, 대학본부는 11월 21일 총학생회와 3시간 면담 끝에 '남녀공학 논의 잠정 중단'과 수업 재개에 전격 합의했습니다. 우측 D02 연합뉴스 보도에 명시되었듯, 향후 논의 재개 시 학생들과 협의하겠다는 입장문 발표를 전제로 합의가 이루어졌습니다. 이는 대학본부가 초기 위기 국면에서 대치를 풀기 위해 실제 대응 조정을 취했음을 입증합니다. 따라서 동덕여대 본부가 초기부터 최종 결정까지 일관된 옹호만 유지했다고 보아서는 안 됩니다.",
    "qa": "[11/21 잠정 중단의 의미] 극단적 충돌 속에서 본부가 취한 실제 행동 조정이었으며, 이후 2025년 4단위 공론화위원회 출범으로 이어지는 징검다리 역할을 했습니다."
  },
  {
    "title": "Slide 09 · 공론화의 딜레마",
    "script": "2025년 동덕여대 공론화 과정의 핵심 딜레마입니다. 숙의기구 학생단(12명)에서는 여대 유지 공표 비율이 80%에서 50%로 완화되었으나, 유효 모수가 미공개되어 개인 태도 변화로 단정할 수는 없습니다. 한편 3,176명이 참여한 대규모 설문에서는 극단적 규칙 충돌이 확인되었습니다. 교원(76%)과 직원(68.5%)은 공학 전환을 지지한 반면, 전체 응답의 91%를 차지한 학생(2,889명)은 71.3%가 여대 유지를 지지했습니다. 교직원과 학생을 1:1:1로 동일 가중하면 공학 찬성이 51.8%였으나, 무가중 단순합산을 하면 여대 유지가 66.1%였습니다. 결국 공론화위는 12월 2일 9:2:1로 공학 전환 권고안을 가결했습니다.",
    "qa": "[가중 방식 평가] 가중 방식의 위법성을 단정하는 것이 아니라, 집단 간 이해관계가 정면 대립하는 상황에서 집계 규칙 합의가 얼마나 결정적인 정당성 쟁점인지를 분석합니다."
  },
  {
    "title": "Slide 10 · 결정 이후의 반발",
    "script": "공식 결정 이후 양 대학의 갈등 양상입니다. 동덕여대에서는 12월 2일 권고 직후 총장이 2029년 전환 방침을 발표하자, 12월 3일부터 7일까지 진행된 학생 총투표에서 85.7%라는 압도적 반대가 표출되었습니다. 이어 2026년 1월 평의원회에서 8:2로 학칙 개정이 가결되었으나 학생위원 2인은 서명을 거부했습니다. 강원대 역시 4월 28일 15:6 가결과 6월 교육부 승인을 얻었으나, 가결 당일 직원협의회가 본문 왜곡을 규탄하며 피켓 시위를 벌였습니다. 두 대학 모두 공식 절차의 통과라는 제도적 진전을 이루었으나, 반대 공중의 수용과 신뢰 회복은 미완으로 남았습니다.",
    "qa": "[입시 지원율 보조 지표 처리] 2026학년도 동덕여대 지원자 32.9% 감소는 수시 접수가 9월에 완료되었으므로 12월 발표의 직접적 결과로 단정하지 않고 보조 지표로만 제시했습니다."
  },
  {
    "title": "Slide 11 · 같은 옹호, 다른 수용",
    "script": "두 대학의 직접 비교입니다. 두 대학 모두 통합과 공학 전환이라는 핵심 정책 목표를 끝까지 옹호했습니다. 그러나 수용의 범위와 매개체는 달랐습니다. 강원대는 조직·인력 배치라는 가분적 쟁점을 수정안의 매개체로 삼아 부분적 행동 수용을 택했고 15:6 가결을 이끌어냈습니다. 반면 동덕여대는 여대 정체성이라는 비가분적 쟁점 속에서 공론화 절차와 2029년 유예를 제공했으나 결론을 옹호 관철했습니다. 비교 결론은 두 가지입니다. 첫째, 반대 공중의 영향력, 요구의 성격, 의사결정 구조에 따라 수용의 대상과 범위가 달랐습니다. 둘째, 공식 절차 통과가 곧 반대 집단의 수용이나 관계 회복을 의미하지는 않습니다.",
    "qa": "[비교 결론의 엄밀성] 변수들이 결과를 기계적으로 결정했다고 단정하지 않고, 각 조직이 처한 상황적 조건의 결합 속에서 서로 다른 수용 궤적을 설명했습니다."
  },
  {
    "title": "Slide 12 · 위기의 전조",
    "script": "사전 위기관리 관점에서의 검토입니다. Heath의 이슈관리와 Sturges의 사전 커뮤니케이션 관점에서 볼 때, 강원대에서는 인력 배치와 심의 절차에 대한 문제 제기가, 동덕여대에서는 공학 전환 논의에 대한 사전 협의 요구가 조기 징후로 관찰되었습니다. 그러나 두 대학 모두 비공식 소문이나 선제출 이후에야 사후 대응에 나섰습니다. 신청 전 핵심 이해관계와 수정 가능한 범위를 선제 공개하고, 공식 논의 초기부터 대안과 절차를 투명하게 공개했다면 갈등 비용을 크게 줄일 수 있었을 것입니다. 다만 위기가 발생했다는 사실만으로 조직에 사전 모니터링이 없었다고 단정해서는 안 됩니다.",
    "qa": "[모니터링 단정 배제] 모니터링의 부재를 단정하는 대신, 확인된 조기 징후와 실제 조직 대응 시점 사이의 시간적 간극을 객관적으로 비교했습니다."
  },
  {
    "title": "Slide 13 · 참여와 결정권",
    "script": "절차적 공정성 관점에서의 분석입니다. Leventhal의 절차 규칙과 Tyler의 관계적 모델에 기초하여 발표자는 세 가지 검토 기준을 적용했습니다. 첫째, 대표성 기준에서 강원대는 직역별 심의 반영이, 동덕여대는 1:1:1 가중 방식이 쟁점이 되었습니다. 우측 D08 19쪽을 보시면 공론화위의 2/3 다결 규칙이 명시되어 있습니다. 둘째, 정보 공개 기준에서 강원대는 257쪽 당일 배부가, 동덕여대는 소문 확산이 문제되었습니다. 셋째, 수정 가능성 기준에서 강원대는 수정안 재상정이 작동했으나 당일 수정은 제한되었고, 동덕여대는 학생 의견이 최종 결론에 반영되지 못했습니다. 공식 의결 절차를 통과했다는 사실과 이해관계자가 절차를 공정하게 받아들였는지는 구분해서 평가해야 합니다.",
    "qa": "[표현 교정 반영] '적법한 절차'라는 단정 대신 '공식 의결 절차를 통과했다는 사실'로 문구를 교정하여 절차적 합법성과 주관적 공정성 인식의 괴리를 명확히 규명했습니다."
  },
  {
    "title": "Slide 14 · 시점·규칙·행동",
    "script": "결론 및 실무 제언입니다. 본 연구는 대학 구조개편 갈등 관리를 위해 세 가지 원칙을 제언합니다. 첫째, 시점의 원칙입니다. 반발 이후의 설명보다 결정 이전의 협의가 선행되어야 합니다. 정책 확정 전에 핵심 우려와 수정 가능 범위를 공개해야 합니다. 둘째, 규칙의 원칙입니다. 참여 기회뿐 아니라 의사결정 방식을 사전에 합의해야 합니다. 공론화의 대표성, 가중 방식, 최종 결정권과 이의제기 절차를 사전에 명확히 해야 합니다. 셋째, 행동의 원칙입니다. 수용의 의사 표명보다 수용의 결과를 문서화하여 공개해야 합니다. 마지막으로 강조하고 싶은 테제는, 절차의 개설과 공식 결정의 가결은 구성원의 수용과 같은 지표가 아니라는 점입니다.",
    "qa": "[실무 제언의 도출] 검증되지 않은 제도 신설 대신, 두 대학 사례에서 관찰된 절차적 병목과 갈등 지점을 해결하기 위한 실무적 커뮤니케이션 원칙으로 정립했습니다."
  },
  {
    "title": "Slide 15 · (제목 없음) 참고문헌",
    "script": "마지막으로 분석에 활용한 참고문헌과 1차 사건 기록입니다. 핵심 이론 문헌으로는 Cancel et al.(1997, 1999), Cameron et al.(2001), 황성욱(2014)의 정황적 수용 이론 및 교재 표 2-5, Heath(1997), Sturges(1994), Wilcox & Cameron(2005)의 갈등 생애주기 문헌, Leventhal(1980)과 Tyler(1988)의 절차적 공정성 연구를 인용했습니다. 사건 기록으로는 강원대학교 평의원회 회의록(A01P, A02P, A03P), 동덕여대 소통 일지(D26), 합의문(D02), 공론화위원회 권고안(D06), 설문 상세자료(D07), 회의록(D08), 총투표 보도(D10), 학칙 개정 공고(D22) 등 1차 사료를 엄밀하게 대조했습니다. 이상으로 발표를 마치겠습니다. 경청해 주셔서 감사합니다.",
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
