const slides=[...document.querySelectorAll('.slide')];
const stage=document.getElementById('stage');
const count=document.getElementById('count');
const panel=document.getElementById('panel');
let index=Math.max(0,Math.min(slides.length-1,(parseInt(location.hash.slice(1),10)||1)-1));
const notes=[
 '25초. 두 대학의 변화 방향은 다르지만, 발표의 대상은 공식 결정 이후까지 이어진 위기 대응이다.',
 '40초. 2023년 교육부가 선정한 글로컬대학 본지정 과제는 10개다. 이 중 4개가 대학 간 통합 제안을 포함한다. 동덕여대는 이 사업 밖의 비교 사례다. 전국 모든 구조개편을 세는 통계가 아니다.',
 '55초. 부산은 서로 다른 두 학생 공중이 있다. 부산대 사범대는 공간·교육 여건, 부산교대는 정체성·자격·절차를 문제 삼았다. 부산교대 51.27%는 투표자 중 반대이며 참여율은 7.18%다. 동덕여대의 85.7%는 2025년 학생 총투표 참여자 중 반대다.',
 '35초. 상황변수로 대학의 선택을 해석하고 발언, 후속 행동, 공중 반응을 분리한다. 결정의 진전과 구성원 수용을 동일시하지 않는다.',
 '60초. 외부 변수 24개, 내부 변수 57개 중 원문 대조가 가능한 E24, E21, I56을 택했다. E21과 I56은 실제 양보 의사나 신뢰도 조사값이 아니다. 코드는 교재 목록에 붙인 분석용 순번이다.',
 '65초. 부산교대 학생은 공동 지원 결정과 절차에, 부산대 사범대 학생은 이전 시 교육 환경에 이의를 냈다. 두 공중을 한 집단으로 묶으면 이후 계획 수정의 대상이 흐려진다.',
 '65초. 부산대는 9월 설명회에서 사범대 일부 이전 구상을 철회했고 2024년 공개 계획에도 이를 제외했다. 그럼에도 직후 부산대 학부 투표 참여자의 63.5%가 통합에 반대했다. 계획 수정과 전체 수용은 다른 결과다.',
 '65초. 교육부의 2025년 2월 심사 요약에는 사범대 물리적 이전 방안 재검토 요청이 기록된다. 대학은 연구센터와 문구 수정안을 제시했지만 학생들은 범위와 정보공개에 이의를 냈다. 2023년 철회가 곧 파기됐다고 단정할 수 없다.',
 '55초. 대학은 결정 전 논의라고 해명했지만 학생은 애초 논의 전에 협의했어야 한다고 요구했다. I56은 이 절차 갈등의 단서일 뿐 신뢰 측정값은 아니다.',
 '55초. 11월 21일 직접 면담과 잠정 중단은 실제 조치다. 다만 잠정 중단과 여대 유지 요구의 수용은 다르다.',
 '70초. 공론화 최종 온라인 조사는 교원·학생·직원 응답값을 1대1대1 동일 비중으로 집계했다. 51.8%, 71.3%, 85.7%는 서로 다른 분모와 질문의 결과다. 2026년 공식 절차와 학생 반대도 분리한다.',
 '60초. 부산은 사범대 이전과 일부 문구를 조정하며 통합 목표를 유지했다. 동덕여대는 협의 시점은 바꾸었으나 전환 방침을 유지했다. 변수는 선택의 조건을 해석하는 데 쓰며 단일 원인으로 단정하지 않는다.',
 '60초. 두 대학을 통째로 성공·실패로 평가하지 않는다. 조치별 효과와 미흡함을 구분하고 신뢰 회복은 미확인으로 둔다.',
 '60초. 베노이트는 실제 발언의 범위에서만 보조적으로 쓴다. 부산대는 연구센터와 단과대학 이전을 구분했고, 동덕여대는 이미 결정됐다는 인식을 부인했다. 핵심 요구에 얼마나 답했는지가 평가의 중심이다.',
 '60초. 당시 실행 가능했던 대안을 앞서 확인된 공백에 일대일로 연결했다. 두 대학 모두 학생 요구별 반영 결과를 공개할 필요가 있었다.',
 '25초. 공식 문서와 대학 언론, 이론 문헌을 분리해 정리했다. 상세 URL과 원문 ID는 출처 색인에서 확인할 수 있다.'
];
function fit(){const scale=Math.min(innerWidth/1600,innerHeight/900);stage.style.transform=`translate(-50%,-50%) scale(${scale})`}
function show(n){index=(n+slides.length)%slides.length;slides.forEach((s,i)=>s.classList.toggle('active',i===index));count.textContent=`${index+1} / ${slides.length}`;history.replaceState(null,'',`#${index+1}`);if(!panel.hidden)updatePanel()}
function updatePanel(){const h=slides[index].querySelector('h1,h2');document.getElementById('panel-title').textContent=`${index+1}장 · ${h?.textContent.trim().replace(/\s+/g,' ')||'참고문헌'}`;document.getElementById('panel-body').textContent=notes[index]}
document.getElementById('prev').onclick=()=>show(index-1);document.getElementById('next').onclick=()=>show(index+1);document.getElementById('notes').onclick=()=>{panel.hidden=false;updatePanel()};document.getElementById('close').onclick=()=>panel.hidden=true;
document.getElementById('toc').onclick=()=>{panel.hidden=false;document.getElementById('panel-title').textContent='목차';document.getElementById('panel-body').textContent=slides.map((s,i)=>`${i+1}. ${s.querySelector('h1,h2')?.textContent.trim().replace(/\s+/g,' ')||'참고문헌'}`).join('\n')};
addEventListener('keydown',e=>{if(e.key==='ArrowRight'||e.key==='PageDown'){show(index+1)}else if(e.key==='ArrowLeft'||e.key==='PageUp'){show(index-1)}else if(e.key==='Home'){show(0)}else if(e.key==='End'){show(slides.length-1)}else if(e.key==='Escape'){panel.hidden=true}else if(e.key.toLowerCase()==='n'){panel.hidden=false;updatePanel()}});
addEventListener('resize',fit);fit();show(index);
