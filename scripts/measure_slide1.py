# -*- coding: utf-8 -*-
from playwright.sync_api import sync_playwright
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DECK = ROOT / "versions" / "deck_v7"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1600, "height": 900})
    page.goto((DECK / "index.html").resolve().as_uri(), wait_until="load")
    page.evaluate("show(0)") # Slide 1 is index 0
    page.wait_for_timeout(300)
    
    info = page.evaluate("""() => {
        const slide = document.querySelector('.slide[data-slide="1"]');
        const h1 = slide.querySelector('h1').getBoundingClientRect();
        const seal = slide.querySelector('.cover-seal').getBoundingClientRect();
        const byline = slide.querySelector('.cover-byline').getBoundingClientRect();
        const credit = slide.querySelector('.cover-credit').getBoundingClientRect();
        return {
            h1: {top: h1.top, bottom: h1.bottom},
            seal: {top: seal.top, bottom: seal.bottom},
            byline: {top: byline.top, bottom: byline.bottom},
            credit: {top: credit.top, bottom: credit.bottom}
        };
    }""")
    print("Slide 1 elements:", info)
    page.screenshot(path=str(ROOT / "qa" / "deck_v7" / "slide_01.png"))
    print("Screenshot saved to qa/deck_v7/slide_01.png")
    browser.close()
