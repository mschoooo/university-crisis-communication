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
    "title": "대학 구조개편 갈등에서 위기 메시지는 어떻게 작동했나",
    "script": "두 사례를 메시지·행동·반응의 순서로 봅니다. 표지 제목은 관찰 질문으로 제시합니다.",
    "qa": "수치의 분모와 발화의 범위를 원문에 맞춰 설명합니다."
  },
  {
    "title": "무엇을 말했고, 상대는 어떻게 반응했나",
    "script": "발표의 분석 단위는 대학의 발화와 후속 행동, 공중의 반응입니다. 공식 결정은 반응 지표 중 하나입니다.",
    "qa": "수치의 분모와 발화의 범위를 원문에 맞춰 설명합니다."
  },
  {
    "title": "외부·내부 조건으로 대응 범위를 읽는다",
    "script": "교재의 외부 24·내부 57개 변수 가운데 원문으로 논의할 수 있는 E24·E21·I56을 고릅니다. 코드 자체는 교재가 아닌 이 분석의 순번입니다.",
    "qa": "수치의 분모와 발화의 범위를 원문에 맞춰 설명합니다."
  },
  {
    "title": "두 사안 모두 결정 과정이 쟁점이 됐다",
    "script": "강원대는 통합 일정과 사전 자료 제공이, 동덕여대는 공학 논의의 사전 협의와 대표성이 초기 쟁점입니다. 배경 설명은 대학의 주장으로 표시합니다.",
    "qa": "수치의 분모와 발화의 범위를 원문에 맞춰 설명합니다."
  },
  {
    "title": "사과가 있었지만 심의는 보류됐다",
    "script": "자료 전달 지연에 관한 제한적 사과입니다. 발언의 범위만 베노이트로 분류하고, 카메론은 일정·심의 조건을 읽는 데 씁니다.",
    "qa": "수치의 분모와 발화의 범위를 원문에 맞춰 설명합니다."
  },
  {
    "title": "보안·기한 해명 뒤 8:12로 부결됐다",
    "script": "평의원회 공식 부결은 공중의 상대적 힘을 보여줍니다. 표결 자체가 다음 수정의 단일 원인이라는 뜻은 아닙니다.",
    "qa": "수치의 분모와 발화의 범위를 원문에 맞춰 설명합니다."
  },
  {
    "title": "인력 구성은 바뀌었지만 수용은 갈렸다",
    "script": "인력안의 일부 수정과 공식 가결은 확인됩니다. 직원협의회 이의가 이어졌다는 점도 함께 설명합니다.",
    "qa": "수치의 분모와 발화의 범위를 원문에 맞춰 설명합니다."
  },
  {
    "title": "본부의 설명과 학생 요구가 엇갈렸다",
    "script": "대학의 '결정 전 논의' 설명과 학생 요구를 나란히 봅니다. 제한적 부인 분류는 이 실제 발언에만 붙입니다.",
    "qa": "수치의 분모와 발화의 범위를 원문에 맞춰 설명합니다."
  },
  {
    "title": "면담 뒤 논의가 잠정 중단됐다",
    "script": "면담 뒤 잠정 중단과 수업 재개가 합의됐습니다. 여대 유지 요구가 수용된 것은 아닙니다.",
    "qa": "수치의 분모와 발화의 범위를 원문에 맞춰 설명합니다."
  },
  {
    "title": "집계 규칙이 결과 해석을 갈랐다",
    "script": "51.8%와 71.3%는 분모와 가중치가 다릅니다. 집계 규칙과 대표성 논쟁을 읽습니다.",
    "qa": "수치의 분모와 발화의 범위를 원문에 맞춰 설명합니다."
  },
  {
    "title": "우려를 인정한 발표 뒤에도 반대가 이어졌다",
    "script": "2029년 전환 시점은 기존 계획입니다. 학생 반대가 이후 총투표로 확인됐고 신뢰 회복은 측정되지 않았습니다.",
    "qa": "수치의 분모와 발화의 범위를 원문에 맞춰 설명합니다."
  },
  {
    "title": "조정 가능한 범위가 대응을 갈랐다",
    "script": "카메론의 대응 조건과 실제 메시지·행동을 직접 비교합니다. 공식 결정과 구성원 반응을 별도 열로 읽습니다.",
    "qa": "수치의 분모와 발화의 범위를 원문에 맞춰 설명합니다."
  },
  {
    "title": "공식 통과와 구성원 수용은 다르다",
    "script": "확인된 행동 변화와 남은 이견을 구분합니다. 시간적 선후로 인과관계를 확정할 수 없습니다.",
    "qa": "수치의 분모와 발화의 범위를 원문에 맞춰 설명합니다."
  },
  {
    "title": "결정 전에 참여 규칙을 공개하라",
    "script": "사전 이슈관리와 절차적 공정성의 관점에서 초기 정보, 협의, 대표성, 집계, 후속 조치를 제안합니다.",
    "qa": "수치의 분모와 발화의 범위를 원문에 맞춰 설명합니다."
  },
  {
    "title": "참고문헌 · 사건 원문",
    "script": "서지와 사건 원문의 증거 수준을 구분했습니다. 자세한 원문은 자료 ID로 확인할 수 있습니다.",
    "qa": "수치의 분모와 발화의 범위를 원문에 맞춰 설명합니다."
  }
];

function fitStage() {
  const scale = Math.min(window.innerWidth / 1600, window.innerHeight / 900);
  stage.style.transform = `translate(-50%, -50%) scale(${scale})`;
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
