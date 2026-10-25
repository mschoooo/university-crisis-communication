"""Render and check every HTML slide in deck_v20."""
from pathlib import Path
import json
from PIL import Image, ImageOps, ImageDraw
from playwright.sync_api import sync_playwright

repo=Path(__file__).resolve().parents[1]
deck=repo/'versions'/'deck_v20'
out=repo/'qa'/'deck_v20'
out.mkdir(parents=True,exist_ok=True)
failures=[]
with sync_playwright() as pw:
    browser=pw.chromium.launch(headless=True)
    page=browser.new_page(viewport={'width':1600,'height':900},device_scale_factor=1)
    page.emulate_media(reduced_motion='reduce')
    page.goto((deck/'index.html').as_uri(),wait_until='load')
    page.evaluate('document.fonts.ready')
    count=page.locator('.slide').count()
    for number in range(1,count+1):
        page.evaluate('(n)=>show(n-1)',number)
        page.wait_for_timeout(40)
        page.locator('#stage').screenshot(path=str(out/f'slide_{number:02}.png'))
        result=page.evaluate('''() => {
          const slide=document.querySelector('.slide.active'),s=slide.getBoundingClientRect();
          const bad=[];
          for(const el of slide.querySelectorAll('h1,h2,h3,p,blockquote,figure,figcaption,.timeline,.theory-rows,.comparison,.assessment,.bibliography,.message-compare,.recommendations')){
            const r=el.getBoundingClientRect();
            if(!el.matches('.cover-bg')&&(r.right>s.right+4||r.bottom>s.bottom-50||r.left<s.left-4)) bad.push(`${el.tagName}.${el.className}: ${Math.round(r.left-s.left)},${Math.round(r.top-s.top)},${Math.round(r.right-s.right)},${Math.round(r.bottom-s.bottom)}`);
            if(el.scrollWidth>el.clientWidth+5&&el.clientWidth>0)bad.push(`scroll:${el.tagName}.${el.className}`);
          }
          const missing=[...slide.querySelectorAll('img')].filter(i=>!i.complete||i.naturalWidth===0).map(i=>i.getAttribute('src'));
          return {bad,missing};
        }''')
        if result['bad'] or result['missing']: failures.append((number,result))
    # Print layout has all slides visible via @media print.
    page.pdf(path=str(deck/'deck_v20.pdf'),width='1600px',height='900px',print_background=True,prefer_css_page_size=True)
    browser.close()

thumbs=[]
for n in range(1,count+1):
    im=Image.open(out/f'slide_{n:02}.png').convert('RGB')
    thumb=ImageOps.fit(im,(400,225))
    d=ImageDraw.Draw(thumb)
    d.rectangle((0,0,39,25),fill='#202426')
    d.text((8,5),str(n).zfill(2),fill='#ffffff')
    thumbs.append(thumb)
sheet=Image.new('RGB',(1600,900),'white')
for i,im in enumerate(thumbs):sheet.paste(im,((i%4)*400,(i//4)*225))
sheet.save(out/'contact_sheet.png')
(out/'validation.json').write_text(json.dumps({'slides':count,'failures':failures},ensure_ascii=False,indent=2),encoding='utf-8')
print('slides',count,'failures',len(failures))
for f in failures:print(f)
