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
    "title": "두 구조개편에서 절차가 쟁점이 됐다",
    "script": "두 대학의 갈등을 초기 위험 징후로 나란히 제시합니다. 사진 촬영일과 사건일을 구분합니다.",
    "qa": "수치의 분모와 발화의 범위를 원문에 맞춰 설명합니다."
  },
  {
    "title": "무엇을 말했고, 무엇이 달라졌나?",
    "script": "발화, 후속 행동, 공중 반응을 같은 순서로 분석합니다. 공식 의결과 구성원 반응은 별도로 봅니다.",
    "qa": "수치의 분모와 발화의 범위를 원문에 맞춰 설명합니다."
  },
  {
    "title": "카메론의 변수로 대응 조건을 읽는다",
    "script": "E24는 공중의 상대적인 힘, E21은 공중의 양보할 수 있는 수준, I56은 신뢰감 정도다. 기록으로 관찰 가능한 조건을 골랐으며 양보 수준과 신뢰를 직접 측정한 것은 아니다. 인과관계로 단정하지 않는다.",
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
    "script": "최종조사는 교원, 학생, 직원 응답값을 1대1대1 동일 비중으로 적용했다. 실제 응답자 수가 서로 달라 대표성에 이의가 제기됐다.",
    "qa": "수치의 분모와 발화의 범위를 원문에 맞춰 설명합니다."
  },
  {
    "title": "우려를 인정한 발표 뒤에도 반대가 이어졌다",
    "script": "2025년 12월 발표 뒤 학생 반대가 이어졌습니다. 2026년 1월 12일 평의원회 심의·가결의 8 대 2 수치는 취재 보도 근거입니다. 학칙은 2월 26일 개정, 27일 공고, 3월 1일 시행입니다. 공식 절차와 학생 수용을 구분합니다.",
    "qa": "수치의 분모와 발화의 범위를 원문에 맞춰 설명합니다."
  },
  {
    "title": "무엇을 조정하고, 무엇을 유지했나",
    "script": "무엇을 조정하고 유지했는지 비교합니다. 공식 절차의 진전과 구성원의 수용은 별도로 읽습니다.",
    "qa": "수치의 분모와 발화의 범위를 원문에 맞춰 설명합니다."
  },
  {
    "title": "효과와 한계를 조치별로 평가한다",
    "script": "대학 단위의 성공 실패가 아니라 대응별 평가다. 강원대 조직안 수정과 동덕여대 대면 협의·잠정 중단은 확인된 조치다. 사전 소통과 공론화 대표성에는 이의가 남았다. 양측의 신뢰 회복은 확인되지 않았다.",
    "qa": "수치의 분모와 발화의 범위를 원문에 맞춰 설명합니다."
  },
  {
    "title": "결정 전에 정보와 규칙을 합의하라",
    "script": "당시 강원대는 신청 전 자료 공개, 충분한 심의, 인력 협의를 했어야 한다. 동덕여대는 논의 초기에 정보 공개와 대표성, 동일 비중 규칙을 합의했어야 한다. 두 대학 모두 요구 반영 결과를 다시 공개하는 절차가 필요하다.",
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
