# -*- coding: utf-8 -*-
from playwright.sync_api import sync_playwright
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DECK = ROOT / "versions" / "deck_v7"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1600, "height": 900})
    page.goto((DECK / "index.html").resolve().as_uri(), wait_until="load")
    page.evaluate("show(4)") # Slide 5 is index 4
    page.wait_for_timeout(300)
    
    info = page.evaluate("""() => {
        const slide = document.querySelector('.slide[data-slide="5"]');
        const plates = Array.from(slide.querySelectorAll('.parallel-plate')).map(el => el.getBoundingClientRect());
        const imgs = Array.from(slide.querySelectorAll('.parallel-photo img')).map(img => ({
            src: img.getAttribute('src'),
            complete: img.complete,
            naturalWidth: img.naturalWidth,
            naturalHeight: img.naturalHeight
        }));
        const thesis = slide.querySelector('.thesis-line')?.getBoundingClientRect();
        const footer = slide.querySelector('.source-footer')?.getBoundingClientRect();
        return {
            plates: plates.map(p => ({top: p.top, bottom: p.bottom, height: p.height})),
            imgs: imgs,
            thesis: thesis ? {top: thesis.top, bottom: thesis.bottom} : null,
            footer: footer ? {top: footer.top, bottom: footer.bottom} : null
        };
    }""")
    print("Slide 5 details:", info)
    page.screenshot(path=str(ROOT / "qa" / "deck_v7" / "slide_05.png"))
    print("Screenshot saved to qa/deck_v7/slide_05.png")
    browser.close()
