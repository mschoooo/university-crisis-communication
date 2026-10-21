import re
from pathlib import Path

deck_dir = Path("대학통합_위기커뮤니케이션_연구/07_HTML_발표덱/versions/deck_v4")
html_text = (deck_dir / "index.html").read_text(encoding="utf-8")
slides = re.findall(r'<article class="slide[^"]*"', html_text)
print("Number of slides in deck_v4:", len(slides))

# Check ids or data-slide
slide_ids = re.findall(r'<article class="slide[^"]*"\s+id="([^"]+)"', html_text)
print("Slide IDs:", slide_ids)
