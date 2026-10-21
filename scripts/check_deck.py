# -*- coding: utf-8 -*-
"""Script to inspect and generate updated index.html, style.css, slides.js."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DECK = ROOT / "versions" / "deck_v7"
html = (DECK / "index.html").read_text(encoding="utf-8")
print(f"Read index.html: {len(html)} chars")
