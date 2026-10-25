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
    "title": "입장은 상황에 따라 이동한다",
    "script": "교재 81개 변수 목록 가운데 세 조건을 집중적으로 검토합니다. 모든 변수의 작용을 입증했다는 뜻은 아닙니다.",
    "qa": "수치의 분모와 발화의 범위를 원문에 맞춰 설명합니다."
  },
  {
    "title": "두 위기에서 같은 순서를 본다",
    "script": "두 대학의 자료 유형을 구분합니다. 본부 발화는 공식문서로, 공중 반응은 회의록과 학생·직원 기록 및 보도로 확인합니다.",
    "qa": "수치의 분모와 발화의 범위를 원문에 맞춰 설명합니다."
  },
  {
    "title": "사과가 있었지만 심의는 보류됐다",
    "script": "제46차 회의록의 사과는 자료 송부 지연에 한정됩니다. 기한 설명과 요약본에도 심의는 보류됐습니다.",
    "qa": "수치의 분모와 발화의 범위를 원문에 맞춰 설명합니다."
  },
  {
    "title": "보안·기한 해명 뒤 8:12로 부결됐다",
    "script": "제47차에서는 총장이 보안과 기한을 설명했습니다. 출석 20명 가운데 찬성 8명, 반대 12명으로 부결됐습니다.",
    "qa": "수치의 분모와 발화의 범위를 원문에 맞춰 설명합니다."
  },
  {
    "title": "인력 구성은 바뀌었지만 수용은 갈렸다",
    "script": "본부는 공무원 35명 구상을 공무원 24명과 외부 전문가 11명으로 수정했습니다. 직원협의회는 그 폭에 이의를 제기했습니다.",
    "qa": "수치의 분모와 발화의 범위를 원문에 맞춰 설명합니다."
  },
  {
    "title": "본부의 설명과 학생 요구가 엇갈렸다",
    "script": "학부모 대상 글은 수업 차질에 집중했고, 구성원 대상 글은 아직 결정 전이라는 절차 설명을 했습니다. 학생은 논의 중단을 요구했습니다.",
    "qa": "수치의 분모와 발화의 범위를 원문에 맞춰 설명합니다."
  },
  {
    "title": "면담 뒤 논의가 잠정 중단됐다",
    "script": "11월 21일 약 3시간 면담 뒤 논의를 잠정 중단하고 수업 재개에 합의했습니다. 영구 철회로 볼 수 없습니다.",
    "qa": "수치의 분모와 발화의 범위를 원문에 맞춰 설명합니다."
  },
  {
    "title": "집계 규칙이 결과 해석을 갈랐다",
    "script": "51.8%는 교원·학생·직원 집단별 동일 가중을 적용한 공학 전환 선택률입니다. 학생 응답자 중 71.3%는 여대 유지를 선택했습니다.",
    "qa": "수치의 분모와 발화의 범위를 원문에 맞춰 설명합니다."
  },
  {
    "title": "우려를 인정한 발표 뒤에도 반대가 이어졌다",
    "script": "총장 입장문은 우려를 인정하고 2029년 계획을 밝혔습니다. 학생은 12월 9일 총투표 반대 결과를 발표했고 대학이 재응답했습니다.",
    "qa": "수치의 분모와 발화의 범위를 원문에 맞춰 설명합니다."
  },
  {
    "title": "공중의 힘은 서로 다른 양보를 이끌었다",
    "script": "강원대의 평의원회 부결과 동덕여대의 집단행동은 서로 다른 권력 형태입니다. 두 사례의 양보 범위도 달랐습니다.",
    "qa": "수치의 분모와 발화의 범위를 원문에 맞춰 설명합니다."
  },
  {
    "title": "대화는 움직였고, 신뢰 회복은 미확인이다",
    "script": "확인 가능한 행동 변화와 남은 반대를 구분합니다. 동일 공중의 신뢰 변화를 측정한 자료는 없습니다.",
    "qa": "수치의 분모와 발화의 범위를 원문에 맞춰 설명합니다."
  },
  {
    "title": "설명 뒤에 바뀔 것까지 말해야 한다",
    "script": "실무 제언은 두 사례에서 관찰된 문제로부터 도출했습니다. 효과가 검증된 보편적 처방으로 제시하지 않습니다.",
    "qa": "수치의 분모와 발화의 범위를 원문에 맞춰 설명합니다."
  },
  {
    "title": "근거와 추가 검토 자료",
    "script": "핵심 원문과 이론 문헌을 연결했습니다. 변수 검토표는 별도 파일입니다.",
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
