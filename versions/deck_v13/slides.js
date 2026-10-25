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
    "title": "대학의 설명은 왜 갈등을 멈추지 못했나",
    "script": "두 사례의 공식 결정은 진전됐지만, 메시지의 효과는 발화 후 공중 반응에서 따로 살핍니다.",
    "qa": "근거와 해석을 구분하고, 신뢰 회복은 측정 자료가 있을 때만 판정합니다."
  },
  {
    "title": "무엇을 말했고, 상대는 어떻게 반응했나",
    "script": "연구 질문은 메시지, 조치, 반응의 순서를 묻습니다. 의결만으로 위기 커뮤니케이션 성공을 판단하지 않습니다.",
    "qa": "근거와 해석을 구분하고, 신뢰 회복은 측정 자료가 있을 때만 판정합니다."
  },
  {
    "title": "입장은 상황에 따라 이동한다",
    "script": "81개 변수는 전수분석 보고서에 보존했습니다. 발표에서는 공중의 힘, 양보 수준, 기존 신뢰가 입장 이동을 설명하는지 확인합니다.",
    "qa": "근거와 해석을 구분하고, 신뢰 회복은 측정 자료가 있을 때만 판정합니다."
  },
  {
    "title": "두 위기에서 같은 순서를 본다",
    "script": "회의록과 공식 입장은 본부 발화의 근거입니다. 반대 공중의 반응은 별도 기록과 보도에서 대조했습니다.",
    "qa": "근거와 해석을 구분하고, 신뢰 회복은 측정 자료가 있을 때만 판정합니다."
  },
  {
    "title": "사과의 범위는 ‘자료 전달 지연’이었다",
    "script": "제46차 회의록에서 257쪽 자료가 이틀 전 전달됐다는 지적과 기획처장의 사과, 심의 보류를 확인할 수 있습니다.",
    "qa": "근거와 해석을 구분하고, 신뢰 회복은 측정 자료가 있을 때만 판정합니다."
  },
  {
    "title": "보안과 기한 설명 뒤에도 8:12로 부결됐다",
    "script": "제47차에서 총장은 협상 보안과 제출 기한을 설명했습니다. 발언과 약속 뒤에도 표결은 8대12 부결이었습니다.",
    "qa": "근거와 해석을 구분하고, 신뢰 회복은 측정 자료가 있을 때만 판정합니다."
  },
  {
    "title": "인력안은 바뀌었고, 수정의 의미는 다퉈졌다",
    "script": "공무원 35명 구상을 공무원 24명과 외부 전문가 11명으로 바꿨습니다. 직원협의회는 실제 수정 폭이 작다고 보았습니다.",
    "qa": "근거와 해석을 구분하고, 신뢰 회복은 측정 자료가 있을 때만 판정합니다."
  },
  {
    "title": "본부는 ‘결정 전 논의’라고 설명했다",
    "script": "11월 15일 학부모 대상 글과 18일 구성원 대상 설명은 수신자와 강조점이 다릅니다. 총학생회는 논의 중단과 사과를 요구했습니다.",
    "qa": "근거와 해석을 구분하고, 신뢰 회복은 측정 자료가 있을 때만 판정합니다."
  },
  {
    "title": "대면 협의가 잠정 중단 합의를 만들었다",
    "script": "11월 21일 대면 면담 뒤 본부가 논의를 잠정 중단했고 수업 재개에 합의했습니다. 영구 철회와는 구분합니다.",
    "qa": "근거와 해석을 구분하고, 신뢰 회복은 측정 자료가 있을 때만 판정합니다."
  },
  {
    "title": "공론화는 진행됐지만 대표성에 이견이 남았다",
    "script": "공론화위는 집단별 동일 가중을 적용했습니다. 학생 응답자 다수의 여대 유지 선택과 위원회 권고를 동시에 보여줍니다.",
    "qa": "근거와 해석을 구분하고, 신뢰 회복은 측정 자료가 있을 때만 판정합니다."
  },
  {
    "title": "우려를 인정한 전환 발표에 학생은 반대했다",
    "script": "12월 3일 총장 입장문은 우려를 인정하면서 전환 추진을 발표했습니다. 12월 9일 학생은 총투표 반대와 대표성 비판을 제기했습니다.",
    "qa": "근거와 해석을 구분하고, 신뢰 회복은 측정 자료가 있을 때만 판정합니다."
  },
  {
    "title": "두 대학은 공중의 힘에 다르게 반응했다",
    "script": "강원대의 공식 심의권과 동덕여대 학생의 동원력은 다른 힘입니다. 두 대학 모두 후속 설명에 대한 이의가 남았습니다.",
    "qa": "근거와 해석을 구분하고, 신뢰 회복은 측정 자료가 있을 때만 판정합니다."
  },
  {
    "title": "정책 진전과 신뢰 회복은 다른 결과다",
    "script": "관찰 가능한 합의와 반대는 확인되지만, 동일 공중의 신뢰 전후 측정은 없습니다. 정책 진전을 평판 회복으로 대체하지 않습니다.",
    "qa": "근거와 해석을 구분하고, 신뢰 회복은 측정 자료가 있을 때만 판정합니다."
  },
  {
    "title": "발화의 전략과 회복 성과를 분리한다",
    "script": "베노이트는 한 장에서 발화 전략만 분류합니다. 조건은 카메룬으로, 결과는 실제 조치와 공중 반응으로 판정합니다.",
    "qa": "근거와 해석을 구분하고, 신뢰 회복은 측정 자료가 있을 때만 판정합니다."
  },
  {
    "title": "참고문헌과 전수분석",
    "script": "모든 핵심 수치는 원문 인덱스에 연결했습니다. 81개 변수별 중요도는 별도 전수분석 보고서에 있습니다.",
    "qa": "근거와 해석을 구분하고, 신뢰 회복은 측정 자료가 있을 때만 판정합니다."
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
