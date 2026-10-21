# -*- coding: utf-8 -*-
from playwright.sync_api import sync_playwright
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DECK = ROOT / "versions" / "deck_v7"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1600, "height": 900})
    page.goto((DECK / "index.html").resolve().as_uri(), wait_until="load")
    page.evaluate("show(9)") # Slide 10 is 0-indexed 9
    page.wait_for_timeout(300)
    
    info = page.evaluate("""() => {
        const slide = document.querySelector('.slide[data-slide="10"]');
        const plates = Array.from(slide.querySelectorAll('.parallel-plate')).map(el => el.getBoundingClientRect());
        const thesis = slide.querySelector('.thesis-line')?.getBoundingClientRect();
        const footer = slide.querySelector('.source-footer')?.getBoundingClientRect();
        const caveats = Array.from(slide.querySelectorAll('.caveat-text')).map(el => el.getBoundingClientRect());
        return {
            plates: plates.map(p => ({top: p.top, bottom: p.bottom, height: p.height})),
            caveats: caveats.map(c => ({top: c.top, bottom: c.bottom, height: c.height})),
            thesis: thesis ? {top: thesis.top, bottom: thesis.bottom, height: thesis.height} : null,
            footer: footer ? {top: footer.top, bottom: footer.bottom, height: footer.height} : null
        };
    }""")
    print("Slide 10 bounding boxes:")
    for k, v in info.items():
        print(f"  {k}: {v}")
    browser.close()
