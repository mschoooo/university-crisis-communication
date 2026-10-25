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
    "title": "Slide 03 · 대응을 바꾸는 조건",
    "script": "교재에는 외부 24개와 내부 57개, 총 81개 변수가 있습니다. 전수분석에서는 상·중·하·미확인으로 평가했습니다. 이 발표는 그중 실제 입장 이동을 설명하는 변수를 선택해 보여줍니다.",
    "qa": "기업의 외부 공중 모델을 대학 내부 구성원에게 적용하는 한계를 명시합니다."
  },
  {
    "title": "Slide 04 · 구조개편 압력",
    "script": "강원대에는 정부 지원과 네 캠퍼스의 배분 문제가, 동덕여대에는 여성교육 정체성과 대학 경쟁력 주장이 있었습니다. 후자의 재정 위험 규모는 독립 검증되지 않았습니다.",
    "qa": "동덕여대의 존립 위기를 확정된 재무 사실로 표현하지 않습니다."
  },
  {
    "title": "Slide 05 · 신뢰의 출발점",
    "script": "강원대는 선제출과 자료 공유 방식이, 동덕여대는 공식 설명 전 논의가 알려진 경위가 불신의 출발점이었습니다. 이는 조직문화·기존 신뢰 변수와 연결됩니다.",
    "qa": "초기 소통 부족을 개인의 동기나 인성으로 단정하지 않습니다."
  },
  {
    "title": "Slide 06 · 제도적 힘",
    "script": "강원대는 지원 축소 우려로 통합을 서둘렀지만 평의원회가 8대12로 부결했습니다. 외부 자원 압력과 내부 공중의 제도적 힘이 동시에 작용했습니다.",
    "qa": "부결을 곧바로 법적 최종 거부권 전체로 확대하지 않습니다."
  },
  {
    "title": "Slide 07 · 인력 문제",
    "script": "4월 28일 본부는 전략실의 공무원 35명 제안을 공무원 24명과 외부 전문가 11명으로 바꾸어 설명했습니다. 총원 35명 축소가 아니라 구성 변경입니다. 표결은 15대6으로 가결됐습니다.",
    "qa": "실제 채용·배치는 확인되지 않았고 무기명 투표라 개인별 전향도 알 수 없습니다."
  },
  {
    "title": "Slide 08 · 학생의 동원력",
    "script": "동덕여대 학생의 높은 관련성과 자체 여론 형성이 2024년 논의 잠정 중단에 압력을 가했습니다. 본부는 수업 재개와 협의에 합의했지만 공학 전환을 영구 철회한 것은 아닙니다.",
    "qa": "학생의 동원력과 제도적 의결권은 구별해야 합니다."
  },
  {
    "title": "Slide 09 · 집계 규칙",
    "script": "2025년 최종 온라인 조사의 51.8%는 교원·학생·직원 집단별 동일 가중치입니다. 학생 2,889명 중 71.3%는 여대 유지였습니다. 어떤 집계 규칙이 정당한지 합의가 없었기에 결과 해석이 충돌했습니다.",
    "qa": "51.8%를 응답자 전체 단순 찬성 비율로 말하지 않습니다."
  },
  {
    "title": "Slide 10 · 남은 반대",
    "script": "두 조직 모두 공식 절차가 진행됐지만 직원협의회의 이의와 학생 총투표 반대가 남았습니다. 동덕여대 2029년 시행은 계획이며 현재 완료된 결과가 아닙니다.",
    "qa": "총투표 85.7%와 공론화 조사 51.8%는 서로 다른 질문·집계 방식입니다."
  },
  {
    "title": "Slide 11 · 변수의 결합",
    "script": "강원대는 정부 압력, 평의원회 부결, 조정 가능한 인력 요구가 함께 작용했습니다. 동덕여대는 정체성 요구, 학생 동원력, 집단별 가중 규칙과 제한된 의결 영향력이 결합했습니다.",
    "qa": "단일 변수가 결과를 기계적으로 결정했다는 인과 주장은 하지 않습니다."
  },
  {
    "title": "Slide 12 · 81개 변수의 중요도",
    "script": "전수분석에서 중요도가 높은 변수군을 네 줄로 비교했습니다. 강원대에는 정부 지원과 평의원회의 부결, 동덕여대에는 정체성과 대표성 논란이 두드러집니다. 개인·PR부서 변수의 많은 항목은 미확인입니다.",
    "qa": "미확인은 작용하지 않았다는 판정이 아닙니다."
  },
  {
    "title": "Slide 13 · 확인과 한계",
    "script": "원문으로 확인되는 변화와 공개 기록으로는 판정할 수 없는 속성을 구분했습니다. 조직의 행동으로 담당자 개인의 윤리관이나 성별 효과를 추측하지 않습니다.",
    "qa": "실제 인력 배치와 2029년 전환 시행, 신뢰의 정량 변화가 남은 검증 과제입니다."
  },
  {
    "title": "Slide 14 · 베노이트 한 장",
    "script": "마지막으로 공식 발화를 이미지 회복 전략으로 분류합니다. 강원대의 사과는 자료 지연에 한정되고, 인력 수정안은 시정조치에 해당합니다. 동덕여대는 이미 단독 결정했다는 주장을 제한적으로 부인했고 여성교육 성과를 강조했습니다. 발화와 후속 행동은 구분합니다.",
    "qa": "전략 분류가 실제 신뢰 회복의 성과를 입증하지는 않습니다."
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
