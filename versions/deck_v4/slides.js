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
  ['.timeline > div, .dongduk-timeline > div, .vote-row, .before-after > div, .survey-side > div, .aftermath-card, .compare-rows > div, .reference-column p', 'row']
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
    title: "Slide 01 · 표지 및 핵심 연구 질문",
    script: "안녕하십니까. 위기관리(029) 중간고사 대체 과제를 발표하는 미디어커뮤니케이션학과 조민성(202206251)입니다. 본 발표는 학령인구 감소와 구조개편 압박 속에서 대학 본부의 변화 결단이 왜 학내 위기로 비화하는지, 강원대–강릉원주대 통합과 동덕여대 공학 전환 사례를 비교 분석합니다.",
    qa: "[교수님 예상 질문 포인트] 연구의 독창성: 단순 사건 나열이 아니라 정황적 수용 이론(Cancel et al., 1999; Cameron et al., 2001; 황성욱, 2014)과 수업의 갈등관리 생애주기 문헌(2~7주차)을 결합해 '공식 결정의 진전'과 '내부 공중의 수용'을 분리 평가한 점이 핵심입니다."
  },
  {
    title: "Slide 02 · 문제제기 및 비교 연구 설계",
    script: "강원대–강릉원주대 통합과 동덕여대 공학 전환은 모두 생존을 위한 구조개편이었지만, 제도적 경로와 수용 결과는 판이했습니다. 강원대는 4월 1일 평의원회 부결(8:12) 뒤 27일 만에 수정안이 가결(15:6)되어 통합 출범에 이르렀고, 동덕여대는 6개월간의 숙의 공론화와 학칙 개정을 관철했으나 학생 총투표에서 85.7% 반대가 확인됐습니다. 입시 지원은 전년보다 32.9% 줄었으나 원인은 확인되지 않았습니다.",
    qa: "[교수님 예상 질문 포인트] 두 사례 비교 가능성: 국립대 통합과 사립 여대 공학 전환이라는 구조적 차이 자체가 정황적 수용 이론의 '사전성향적 변인(Predisposing Variables)' 차이를 검증하는 최적의 비교 조건이 됩니다."
  },
  {
    title: "Slide 03 · 이론적 분석 틀 ①: 정황적 수용 이론",
    script: "본 연구의 핵심 이론틀은 카메론 연구진의 정황적 수용 이론과 황성욱 교수님(2014)의 종합 모형입니다. 첫째, 조직의 초기 입장은 거버넌스 구조와 리더십 같은 '사전성향적 변인'이 설정하고, 이후 외적 위협·긴급성·공중의 상대적 권력 같은 '상황적 변인'이 입장을 이동시킵니다. 둘째, 수용의 양태는 실질적 양보를 수반하는 '행동적 수용(Action-based)'과 절차·담화적 제스처에 머무는 '수사 혼합적 수용(Qualified-rhetoric-mixed)'으로 구분됩니다.",
    qa: "[교수님 예상 질문 포인트] 입장(Stance)과 결과(Outcome)의 분리: 수용적 입장으로 이동했다고 해서 곧바로 갈등 완전 해소를 뜻하지 않으며, 쟁점별·공중별로 입장이 동시에 다르게 포지셔닝될 수 있음을 명확히 반영했습니다."
  },
  {
    title: "Slide 04 · 이론적 분석 틀 ②: 갈등관리 생애주기와 3대 평가 축",
    script: "2~6주차 수업 문헌인 Wilcox & Cameron(2005), Ham, Hwang, & Cameron(2011)의 갈등관리 생애주기 4단계와 Heath(1997), Sturges(1994), Marra(2004)를 결합했습니다. 또한 본 발표는 위기관리 성패를 단일 단어로 재단하지 않고, ① 공식 의사결정의 제도적 진전, ② 내부 공중 핵심 요구의 실질적 반영(행동적 수용), ③ 결정 이후 내부 공중의 수용과 외부 평판이라는 3대 축으로 입체 평가합니다.",
    qa: "[교수님 예상 질문 포인트] 왜 3대 평가 축인가? 대학 본부 입장에서는 안건 가결이 성공이지만, 갈등관리 관점에서는 공중의 수용과 평판 회복까지 보아야 반응적(Reactive)·회복(Recovery) 단계의 성패를 온전히 진단할 수 있기 때문입니다."
  },
  {
    title: "Slide 05 · 사례 A (강원대) 사전성향 변인과 위기의 누적",
    script: "강원대 사례의 초기 조건을 보면, 글로컬대학30 사업비 2,150억 원과 2024년 7월 글로컬위원회의 '사업비 50% 삭감 경고'라는 막대한 외적 압박이 존재했습니다. 본부는 협상 보안을 우선시하여 2월 20일 교육부에 신청서를 먼저 제출한 뒤, 2월 28일 회의 당일에야 257쪽 분량의 문서를 배부했습니다. 결국 3월 18일 삼척 항의로 회의가 무산되고, 4월 1일 제47차 평의원회에서 40쪽 요약표와 조건부 가결 제안에도 불구하고 8:12로 부결되었습니다.",
    qa: "[교수님 예상 질문 포인트] Sturges(1994) 적용: 공식 심의 전 '선제출 후통보'가 이루어지면서 내부 공중의 불신이 먼저 고착화되었고, 4월 1일의 구두 약속(조건부 가결 제안)만으로는 이미 굳어진 반대 여론을 돌릴 수 없었습니다."
  },
  {
    title: "Slide 06 · 사례 A (강원대) 본부의 대응과 입장 이동",
    script: "4월 1일 부결 직후 대학 본부는 4월 22일 통폐합심사위원회의 전문성 강화 의견과 내부 직원의 인력 유출 우려가 제기된 뒤 4월 28일 수정안을 상정했습니다. 부분적 행동적 수용으로 해석할 수 있는 수정은 핵심 쟁점이었던 대학혁신전략실 인력 35명 중 공무원을 24명으로 줄이고 외부 전문가 11명을 영입해 춘천 기존 인력 11명을 잔류시킨 점입니다. 반면 평의원회 의장은 28일 추가 지연을 막기 위해 당일 수정안 상정을 제한했고, 신청서 본문 명칭을 둘러싼 절차 논쟁은 남았습니다.",
    qa: "[교수님 예상 질문 포인트] 표결 모수 주의: 4월 1일은 20명 투표(8:12), 4월 28일은 21명 투표(15:6)로 출석 모수가 다르며, 무기명 표결이므로 개별 위원의 표 이동이 아닌 '회의체 전체 표결 결과의 변화'로 해석합니다."
  },
  {
    title: "Slide 07 · 사례 A (강원대) 정황 변인 분석과 위기관리 평가",
    script: "강원대가 27일 만에 인력안을 조정한 배경에는 여러 정황이 있습니다. ① 글로컬 2,150억 원 상실 위험과 5월 말 대교협 입시전형 제출 기한이라는 극도의 긴급성, ② 통합 신청서 심의권을 쥔 대학평의원회의 법정 권력, ③ 정원·조직 수치로 협상 가능했던 요구의 특성이 결합해 '부분적 행동 수용'을 함께 나타났습니다. 수정안 가결 뒤 통합 승인과 연차평가 유일 A등급을 달성했으나, 가결 당일 직원 시위 등 사후 회복 과제가 남았습니다.",
    qa: "[교수님 예상 질문 포인트] 쟁점별 입장 분리: 거버넌스·정원 쟁점에서는 행동적 수용으로 이동했으나, 회의 절차와 문서 명칭에서는 옹호(Advocacy)가 유지되어 직원 수용이 지연되었다는 점이 정황 이론의 정교한 설명력을 보여줍니다."
  },
  {
    title: "Slide 08 · 사례 B (동덕여대) 위기의 발생과 공론화 이행",
    script: "동덕여대 사례는 2024년 11월 전조 단계 소통 실패에서 출발합니다. 본부 일지(D26)를 보면 11월 5일 비전혁신추진단에서 단과대 공학전환 동의가 이뤄졌고 11월 12일 교무위 보고 후 의견수렴을 할 예정이었으나, 11월 7일 교내 소문으로 먼저 유출되고 11월 11일 처장단 면담이 취소되면서 본관 점거로 폭발했습니다. 이후 2025년 5월 상생협력 합의서를 통해 4단위 동수 공론화위원회라는 절차적 수용으로 이행했습니다.",
    qa: "[교수님 예상 질문 포인트] 본부와 학생의 프레임 충돌: 본부는 '교무위 의제화 이전 단계'라 보았으나(D26), 학생들은 '사전 협의 없는 밀실 결정'으로 받아들여 Sturges(1994)가 말한 의견 고착화가 초기 4일 만에 완결되었습니다."
  },
  {
    title: "Slide 09 · 사례 B (동덕여대) 공론화 설계와 입장의 이중성",
    script: "48명 숙의기구의 학생단은 12명으로 구성됐습니다. D07에 공표된 '여대 유지' 비율은 숙의 전 80%, 후 50%입니다. 다만 유효 응답자 수와 동일인 응답 여부가 공개되지 않아 개인의 태도 변화는 확인할 수 없습니다. 숙의기구 전체의 결과 수용 의향은 83.2%였습니다. 일반 구성원 온라인 설문(N=3,176)에서는 교원·학생·직원 1:1:1 동일 가중 시 공학전환이 51.8%인 반면, 학생 응답(2,889명)은 여대 유지가 71.3%, 무가중 단순합산 시에도 여대 유지가 66.1%였습니다. 이 집계 방식의 간극은 절차 정당성 논쟁의 한 요인이 됐습니다.",
    qa: "[교수님 예상 질문 포인트] 11월 26일 표결 보류의 이유(D08 19쪽): 파행이 아니라 제4차 회의(8/29)에서 합의한 '한 단위 전원 반대 시 차기 회의 보류 및 2/3 가결' 규칙이 작동한 결과였으며, 이에 따라 12월 2일 9:2:1(75%)로 권고안이 의결되었습니다."
  },
  {
    title: "Slide 10 · 사례 B (동덕여대) 권고 이후의 후속 결정과 위기 재점화",
    script: "권고안 제출 직후인 12월 3일은 학생 총투표가 시작된 첫날이었습니다. 이날 총장이 권고안 수용과 2029년 전환 방침을 조기 발표하자, 학생 총투표(3,470명)에서는 85.7% 반대가 표출되었습니다. 나아가 2026년 1월 12일 대학평의원회에서 학칙 개정안이 8:2로 가결된 뒤 학생위원 2명이 서명을 거부했고, 본부가 '비밀유지 엄중 관리 요청' 공문을 발송한 사실이 보도되며 불신이 재점화되었습니다. 2026학년도 입시 지원은 전년 대비 32.9% 감소했습니다. 수시는 2025년 9월에 접수되어 12월 발표의 영향으로 볼 수 없고, 감소 원인은 검증되지 않았습니다.",
    qa: "[교수님 예상 질문 포인트] 입시 지원자 32.9% 감소의 해석: 학령인구 변화나 입시 구조 요인을 통제하지 않은 기술통계이므로 공학전환 갈등의 '단일 인과 결과'로 단정하지 않고, 외부 지원 동향을 살펴볼 참고 지표로만 제시합니다. 모집인원·전형 변화 등 다른 요인도 남아 있습니다."
  },
  {
    title: "Slide 11 · 사례 B (동덕여대) 정황 변인 분석과 위기관리 평가",
    script: "Cameron et al.(2001)과 황성욱(2014)의 틀로 보면, 동덕여대는 교원·직원·동문(전환 찬성 우세)과 재학생(반대 우세)이라는 '상충하는 복수 공중(Multiple Publics)' 및 '창학 정체성(도덕적·정체성 비타협 사안)'에 직면했습니다. 본부는 공론화 기구 설치라는 절차적 수용을 취하고 재학생 졸업 시점인 2029년으로 이행을 유예했으나, 1:1:1 가중 규칙과 전환 결론 자체는 끝까지 옹호하는 '수사 혼합적 수용'에 머물렀고, 그 결과 학칙 개정은 관철했으나 내부 수용에는 실패했습니다.",
    qa: "[교수님 예상 질문 포인트] 학교 측 반론의 균형 반영(D11): 고등교육법상 대학평의원회도 특정 단위 과반을 금지하므로 1:1:1 가중이 법 취지에 부합한다는 학교 측 논리와, 재학생 졸업 시점(2029년) 유예가 학생 보호 조치였다는 설명도 함께 제시했습니다."
  },
  {
    title: "Slide 12 · 종합 비교: 무엇이 결정과 수용의 경로를 갈랐는가?",
    script: "두 사례를 정황적 수용 이론 연속선과 5대 비교 차원으로 종합했습니다. 강원대는 '단일 법정 관문(평의원회) + 수치 조정 가능한 실리 쟁점 + 극도의 재정·일정 압박'이 결합해 인력안의 부분적 행동적 수용으로 해석할 만한 수정이 확인됩니다. 4월 28일 가결에는 일정 압박, 수정안 제한, 회의체 구성 차이도 영향을 미쳤을 수 있습니다. 반면 동덕여대는 '복수 공중의 정면충돌 + 비타협적 정체성 쟁점' 속에서 소규모 숙의의 공표 비율과 대규모 설문 간 간극을 해소하지 못하고 1:1:1 가중 규칙과 조기 방침 발표로 회귀하면서 제도적 결정과 구성원 수용이 극단적으로 분리되었습니다.",
    qa: "[교수님 예상 질문 포인트] 핵심 테제 요약: '절차의 개설(Procedural Opening)'만으로는 수용이 완성되지 않으며, 핵심 쟁점의 실제 수정과 집계·표결 규칙에 대한 합의가 구성원 수용과 어떻게 연결되는지는 추가 검증이 필요합니다."
  },
  {
    title: "Slide 13 · 선제적·전략적 위기관리 진단 (수업 핵심 이론 통합)",
    script: "만약 두 대학이 Wilcox & Cameron(2005)의 사전대응적·전략적 단계에서 수업 이론을 적용했다면 무엇이 달라졌을까요? 첫째, Heath(1997)의 이슈 스캐닝을 통해 신청서 선제출이나 비전혁신추진단 회의 전에 직무·정체성 위협을 조기 진단했어야 합니다. 둘째, Sturges(1994)의 의견 고착화 시점 이론처럼 소문이나 당일 257쪽 배부로 여론이 굳어지기 전에 쟁점별 옵션을 선제 공개했어야 합니다. 셋째, Marra(2004)와 Hwang et al.(2022)이 강조하듯 비밀유지 공문이나 형식적 위원회보다 상시 정보 공유 문화와 집계 규칙(가중/무가중 병기) 사전 합의가 필수적입니다.",
    qa: "[교수님 예상 질문 포인트] 2~6주차 수업 이론의 실천적 연결: 각 이론이 단순 장식이 아니라 두 대학의 실제 실패 지점(2/20 선제출, 11/7 소문 유출, 1:1:1 가중 충돌, 1/12 비밀유지 공문)을 정확히 타격하는 처방전임을 보여줍니다."
  },
  {
    title: "Slide 14 · 결론, 연구의 한계 및 AI 활용 투명성 고지",
    script: "결론적으로 이 비교에서 주목할 지점은 ① 의견 고착화 이전의 정보 공유, ② 집계·의결 규칙에 대한 사전 합의, ③ 핵심 요구를 반영한 실제 수정입니다. 강원대의 인력안 수정은 확인되지만, 그것이 표결 변화를 일으켰다고 단정할 수는 없습니다. 아울러 비공개 협상 기록 접근 제한 등 연구의 방법론적 한계를 명시하고, 강의계획서 지침에 따라 본 연구 및 발표덱 제작 과정에서의 AI 도구 활용 목적과 범위, 그리고 연구자의 독자적 기여를 투명하게 고지합니다. 경청해 주셔서 감사합니다.",
    qa: "[교수님 예상 질문 포인트] 강의계획서 AI 고지 준수: 사용한 AI 도구, 활용 목적, 지원 범위 및 연구자의 원자료 전수 대조·이론 재해석 책임을 명확히 구분해 기재했습니다."
  },
  {
    title: "Slide 15 · 참고문헌과 사건 기록",
    script: "마지막 장에는 분석의 핵심 이론 문헌과 두 대학의 공개 원자료를 나누어 제시했습니다. 슬라이드의 자료 ID는 원자료·수업 문헌 검증 인덱스에서 원문 URL과 쪽수로 이어집니다. 보도사진은 이용 허가가 확인되지 않아 공개 파일에 복제하지 않았고, 표지의 링크에서 원문 보도사진을 직접 확인할 수 있습니다.",
    qa: "[자료 확인] P99·P01·H14는 정황적 수용 이론의 핵심 문헌입니다. A01P·A02P의 회의일과 표결, D06–D08의 공론화 조사·의결 규칙, D10·D14·D15·AD26S·AD26R의 후속 결과는 출처 인덱스에서 개별 확인할 수 있습니다."
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
