# -*- coding: utf-8 -*-
import sys
import re
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
HTML_PATH = ROOT / "versions" / "deck_v7" / "index.html"
content = HTML_PATH.read_text(encoding="utf-8")

sections = re.findall(r'<section class="slide[^"]*" data-slide="(\d+)">(.*?)</section>', content, re.DOTALL)
for num, sec in sections:
    footer = re.search(r'<footer class="source-footer">(.*?)</footer>', sec, re.DOTALL)
    f_text = re.sub(r'<[^>]+>', ' ', footer.group(1)).strip() if footer else "None"
    f_text = re.sub(r'\s+', ' ', f_text)
    print(f"Slide {num}: {f_text}")
