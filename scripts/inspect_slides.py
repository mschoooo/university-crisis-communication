import re

html = open('대학통합_위기커뮤니케이션_연구/07_HTML_발표덱/versions/deck_v4/index.html', encoding='utf-8').read()
slides = re.findall(r'(<section class="slide[^"]*".*?</section>)', html, re.DOTALL)
print(f'Total slides: {len(slides)}')

for idx in [2, 6, 10, 11, 12, 13]:
    print(f'=== SLIDE {idx+1} ===')
    print(slides[idx])
    print()
