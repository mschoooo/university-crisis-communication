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
    "title": "Slide 01 · 표지",
    "script": "두 사례 모두 공식 결정은 진전됐지만 반대 집단의 수용은 별도로 평가해야 합니다. 발표는 카메룬의 상황변수로 대응의 조건을 설명하고 마지막에 베노이트를 한 장으로 다룹니다.",
    "qa": "공식 의결과 실제 수용을 혼동하지 않습니다."
  },
  {
    "title": "Slide 02 · 결정과 수용",
    "script": "평가 축은 공식 결정, 핵심 요구 반영, 결정 이후 수용입니다. 회의록과 공론화 원자료를 중심으로 두 사례를 같은 질문에 대입합니다.",
    "qa": "수용도에 관한 동일 질문의 사후 반복조사는 확보되지 않았습니다."
  },
  {
    "title": "Slide 03 · 81개 변수와 세 조건",
    "script": "외부 24개·내부 57개를 모두 검토했습니다. 발표는 두 사례 모두에서 대응 차이를 설명할 자료가 있는 공중의 힘, 양보 수준에 연결한 요구의 조정 가능성, 기존 신뢰를 중심으로 합니다. 요구의 조정 가능성은 교재 변수명이 아니라 연구자의 관찰 지표입니다. 학생·직원은 기업의 외부 공중과 다른 내부 구성원입니다.",
    "qa": "평의원회의 공식 심의권과 학생의 여론 영향력을 같은 권력으로 취급하지 않습니다."
  },
  {
    "title": "Slide 04 · 서로 다른 구조개편 압력",
    "script": "강원대는 정부 지원을 연계한 통합을 추진했습니다. 동덕여대 본부는 경쟁력과 지속가능성을 전환 검토 이유로 제시했습니다. 공개 자료만으로 재무적 존립 위기를 확정할 수는 없습니다.",
    "qa": "본부의 주장과 독립적으로 검증된 재무 사실을 구분합니다."
  },
  {
    "title": "Slide 05 · 신뢰가 약해진 출발점",
    "script": "강원대 제46차 회의록에는 257쪽 자료가 이틀 전 송부됐다는 발언이 있습니다. 동덕여대는 사전 설명 전에 논의가 알려져 학생이 반발했습니다. 신뢰 저하의 크기는 독립 조사로 측정되지 않았습니다.",
    "qa": "이틀 전 송부는 A03P 원문에 근거합니다. 밀실 추진을 확정된 동기로 단정하지 않습니다."
  },
  {
    "title": "Slide 06 · 제도적 힘",
    "script": "강원대는 지원 축소 우려로 통합을 서둘렀지만 평의원회가 8대12로 부결했습니다. 외부 자원 압력과 내부 공중의 제도적 힘이 동시에 작용했습니다.",
    "qa": "부결을 곧바로 법적 최종 거부권 전체로 확대하지 않습니다."
  },
  {
    "title": "Slide 07 · 조정 가능한 인력 문제",
    "script": "본부는 전략실 공무원 35명 제안을 24명과 외부 전문가 11명으로 바꿨습니다. 총원 35명 감축이 아닌 구성 변경입니다. 인력 수정, 정부 일정 압박, 다른 조직안 조정이 함께 작용했을 수 있습니다. 15대6 가결만으로 각 원인의 독립 효과는 알 수 없습니다.",
    "qa": "실제 전문가 채용과 직원 수용은 별도 확인이 필요합니다."
  },
  {
    "title": "Slide 08 · 학생의 두 종류의 영향력",
    "script": "학생의 높은 관련성과 집단행동은 2024년 논의 잠정 중단에 압력을 주었습니다. 이후 공론화위의 학생위원은 12명 중 3명이었고, 동원력과 공식 의결권은 다른 변수입니다.",
    "qa": "잠정 중단은 공학 전환 방침의 영구 철회가 아닙니다."
  },
  {
    "title": "Slide 09 · 같은 응답, 다른 집계 규칙",
    "script": "2025년 최종 온라인 조사는 재학생이 모두 졸업한 뒤인 2029~2030년 예상 시점의 전환을 물었습니다. 전체 응답자는 3,176명입니다. 51.8%는 집단별 동일 가중으로 계산된 공학 전환 찬성이고, 66.1%는 인원수 기준 재계산의 여대 유지 선택입니다. 학생 2,889명 중 71.3%가 여대 유지를 택했습니다.",
    "qa": "두 수치를 전체 응답자의 단순 찬반으로 소개하면 틀립니다. 가중 규칙의 정당성은 의견이 갈립니다."
  },
  {
    "title": "Slide 10 · 사건일과 발표일 구분",
    "script": "동덕여대 학생 총투표 반대 85.7%는 12월 9일 발표됐습니다. 투표 종료일은 보도마다 차이가 있어 특정하지 않습니다. 2029년 조건은 그보다 앞선 공론화 질문에도 있었습니다. 강원대 입학식은 2026년 2월 26~27일, 통합 출범은 3월 1일입니다. 동덕여대 평의원회 8대2는 회의록을 취재한 보도이며 원본은 확보되지 않았습니다.",
    "qa": "2029년 실제 남학생 입학과 강원대 수정안 실제 인사 배치는 아직 확인된 결과가 아닙니다."
  },
  {
    "title": "Slide 11 · 세 조건과 세 결과",
    "script": "강원대에서는 평의원회 부결, 조정 가능한 인력 배치, 선제출에 따른 불신이 함께 작용했습니다. 동덕여대에서는 강한 학생 동원력, 여대 유지 요구의 성격, 집계 규칙에 대한 불신이 결합했습니다. 공식 결정은 양교 모두 진전됐지만 요구 반영 범위는 달랐고 사후 수용은 별개입니다.",
    "qa": "변수의 결합은 사례 해석이지 통제된 인과효과 추정이 아닙니다."
  },
  {
    "title": "Slide 12 · 변수 선정과 등급",
    "script": "81개 항목 모두에 질적 중요도를 판정했습니다. 동덕여대는 상 28, 중 25, 하 4, 미확인 24개이고 강원대는 상 30, 중 22, 하 4, 미확인 25개입니다. 발표 중심 변수는 양쪽에서 중요하고 대응 차이를 설명할 원문 자료가 있는 세 조건입니다.",
    "qa": "등급 건수는 통계적 효과 크기가 아닙니다. 미확인은 비작용을 뜻하지 않습니다."
  },
  {
    "title": "Slide 13 · 확인과 한계",
    "script": "원문으로 확인되는 변화와 공개 기록으로는 판정할 수 없는 속성을 구분했습니다. 조직의 행동으로 담당자 개인의 윤리관이나 성별 효과를 추측하지 않습니다.",
    "qa": "실제 인력 배치와 2029년 전환 시행, 신뢰의 정량 변화가 남은 검증 과제입니다."
  },
  {
    "title": "Slide 14 · 베노이트 이미지 회복 전략",
    "script": "마지막으로 공식 발화를 분류합니다. 강원대 사과는 자료 송부 지연에 한정됩니다. 인력 수정안은 시정조치 제시와 후속 안의 변경으로 확인됩니다. 동덕여대는 이미 단독 결정했다는 주장에 제한적으로 반박하고 여성교육의 성과를 강조했습니다. 발화, 실제 조치, 신뢰 회복 성과를 각기 구분합니다.",
    "qa": "15대6 가결이나 메시지 발표만으로 이미지 회복을 입증할 수 없습니다."
  },
  {
    "title": "Slide 15 · 참고문헌",
    "script": "교재의 81개 변수와 Cancel·Cameron의 이론, 사건별 원문을 대조했습니다. 전수분석 보고서와 문서 ID는 덱 하단에서 열 수 있습니다.",
    "qa": "언론 보도와 공식 문서를 증거 수준에 따라 구분합니다."
  }
];
SPEAKER_NOTES[2].script += " 보조 분석으로 베노이트의 이미지 회복 전략을 사용합니다. Cameron은 대응의 이동 조건, Benoit은 실제 메시지의 기능을 설명합니다. 전략명은 원문 발화로 확인될 때만 붙입니다.";
SPEAKER_NOTES[5].script += " 제46차 회의에서 기획처장이 늦은 자료 제공을 사과한 것은 그 절차 문제에 한정된 사과입니다. 제47차에서 총장은 협상 보안과 제출 기한을 해명했고 사후 수정을 약속했으나, 그날의 표결은 부결이었습니다.";
SPEAKER_NOTES[6].script += " 제48차 회의록과 대학 공식 보도문은 35명 전원 공무원 구상에서 공무원 24명과 외부 전문가 11명 구성으로 바꾼 안을 설명합니다. 이를 제한적 시정조치로 분류합니다. 실제 인사 배치 결과는 별도 확인되지 않았습니다.";
SPEAKER_NOTES[7].script += " 11월 18일 공식 글은 교무위원회 의제화 전이었다며 이미 독단적으로 결정했다는 주장을 부인합니다. 부인의 대상은 그 주장에 한정됩니다. 11월 21일의 논의 잠정 중단은 실제 행동 조정으로 봅니다.";
SPEAKER_NOTES[8].script += " 12월 8일 본부 자료는 동일 가중을 동등한 참여권으로 설명합니다. 이는 본부의 절차 해명이며, 해당 규칙에 학생 측이 동의했다는 근거는 아닙니다.";
SPEAKER_NOTES[9].script += " 12월 3일 입장문은 여성교육의 성과와 미래의 사명을 강조합니다. 베노이트의 긍정적 이미지 강조와 초월로 읽을 수 있습니다. 후속 문서에서는 학칙 개정이 확인되지만 학생들의 여대 유지 요구가 수용된 것은 아닙니다.";
SPEAKER_NOTES[10].script += " 두 사례 모두 설명과 행동을 구분했습니다. 강원대는 지연 사과와 인력안 수정, 동덕여대는 제한적 부인과 논의 중단·전환 일정 조정이 확인됩니다. 사후 수용도와 실제 인사 배치 등은 자료 밖에 있습니다.";

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
