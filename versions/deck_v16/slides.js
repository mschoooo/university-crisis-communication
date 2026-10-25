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
    "title": "변화의 결단은 왜 위기가 되는가",
    "script": "두 대학의 구조개편에서 공식 결정과 구성원 반응을 구분해 위기 커뮤니케이션을 비교합니다.",
    "qa": "수치의 분모와 발화의 범위를 원문에 맞춰 설명합니다."
  },
  {
    "title": "무엇을 말했고, 상대는 어떻게 반응했나",
    "script": "발표의 분석 단위는 대학의 발화와 후속 행동, 공중의 반응입니다. 공식 결정은 반응 지표 중 하나입니다.",
    "qa": "수치의 분모와 발화의 범위를 원문에 맞춰 설명합니다."
  },
  {
    "title": "외부·내부 조건으로 대응 범위를 읽는다",
    "script": "E24·E21·I56은 교재 표를 전사해 붙인 분석용 순번입니다. I56의 신뢰도는 측정하지 않았고 사전 협의·정보공개 갈등을 제한적으로 읽습니다.",
    "qa": "수치의 분모와 발화의 범위를 원문에 맞춰 설명합니다."
  },
  {
    "title": "두 사안 모두 결정 과정이 쟁점이 됐다",
    "script": "2월 28일에는 심의가 보류됐습니다. 신청서 선제출과 늦은 자료 전달이 초기 절차 쟁점이었습니다.",
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
    "script": "결정 전 논의라는 대학의 발언과 학생의 사전 협의 요구를 나란히 읽습니다. I56의 신뢰 수준은 측정되지 않았습니다.",
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
    "script": "2025년 12월 발표와 학생 총투표 이후, 2026년 1월 12일 평의원회 심의와 2월 26일 개정 학칙 시행으로 공식 절차가 진전했습니다. 8 대 2 수치는 회의록 원본이 아닌 취재 보도 근거입니다.",
    "qa": "수치의 분모와 발화의 범위를 원문에 맞춰 설명합니다."
  },
  {
    "title": "무엇을 조정하고, 무엇을 유지했나",
    "script": "무엇을 조정하고 유지했는지 비교합니다. 공식 절차의 진전과 구성원의 수용은 별도로 읽습니다.",
    "qa": "수치의 분모와 발화의 범위를 원문에 맞춰 설명합니다."
  },
  {
    "title": "공식 결정 뒤에도 이견은 남았다",
    "script": "동덕여대 1월 12일 8 대 2 심의는 취재 보도, 2월 26일 학칙 시행은 대학 공고로 확인합니다. 학생 반대와 신뢰 수준은 별개입니다.",
    "qa": "수치의 분모와 발화의 범위를 원문에 맞춰 설명합니다."
  },
  {
    "title": "결정 전에 절차를 합의하라",
    "script": "제언은 사전 정보공개와 협의, 대표성과 의사결정 규칙, 후속 조치와 관계관리의 세 범주입니다.",
    "qa": "수치의 분모와 발화의 범위를 원문에 맞춰 설명합니다."
  },
  {
    "title": "참고문헌 · 출처",
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
