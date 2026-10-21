const slides=[...document.querySelectorAll('.slide')];
const count=document.querySelector('#count');
let current=0;
function setZoom(){document.documentElement.style.setProperty('--zoom',Math.min(innerWidth/1600,innerHeight/900).toString());}
function show(index){
  current=Math.max(0,Math.min(slides.length-1,index));
  slides.forEach((slide,i)=>slide.classList.toggle('active',i===current));
  count.textContent=`${current+1} / ${slides.length}`;
  history.replaceState(null,'',`#${current+1}`);
}
document.querySelector('#prev').addEventListener('click',()=>show(current-1));
document.querySelector('#next').addEventListener('click',()=>show(current+1));
window.addEventListener('keydown',event=>{
  if(['ArrowRight','PageDown',' '].includes(event.key)){event.preventDefault();show(current+1);}
  if(['ArrowLeft','PageUp'].includes(event.key)){event.preventDefault();show(current-1);}
  if(event.key==='Home')show(0);
  if(event.key==='End')show(slides.length-1);
});
window.addEventListener('resize',setZoom);
window.addEventListener('hashchange',()=>{
  const target=Number(location.hash.replace('#',''));
  if(Number.isInteger(target)&&target>=1&&target<=slides.length&&target-1!==current)show(target-1);
});
setZoom();
const hash=Number(location.hash.replace('#',''));
show(Number.isInteger(hash)&&hash>=1&&hash<=slides.length?hash-1:0);
