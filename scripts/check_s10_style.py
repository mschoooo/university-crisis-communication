# -*- coding: utf-8 -*-
from playwright.sync_api import sync_playwright
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DECK = ROOT / "versions" / "deck_v7"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1600, "height": 900})
    page.goto((DECK / "index.html").resolve().as_uri(), wait_until="load")
    page.evaluate("show(9)")
    page.wait_for_timeout(300)
    
    style_info = page.evaluate("""() => {
        const slide = document.querySelector('.slide[data-slide="10"]');
        const grid = slide.querySelector('.parallel-grid');
        const thesis = slide.querySelector('.thesis-line');
        const footer = slide.querySelector('.source-footer');
        return {
            grid: { top: grid.getBoundingClientRect().top, bottom: grid.getBoundingClientRect().bottom },
            thesis: { top: thesis.getBoundingClientRect().top, bottom: thesis.getBoundingClientRect().bottom },
            footer: { top: footer.getBoundingClientRect().top, bottom: footer.getBoundingClientRect().bottom },
            gridStyle: window.getComputedStyle(grid).marginBottom,
            thesisMarginTop: window.getComputedStyle(thesis).marginTop
        };
    }""")
    print("Slide 10 details:", style_info)
    browser.close()
