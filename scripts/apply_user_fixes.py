# -*- coding: utf-8 -*-
"""Apply user fixes:
1. Cover: Remove newspaper & paper elements, write name/dept/id as plain typography without box.
2. Slide 5: Kangwon photo -> protest_kangwon.jpg (anti-integration protest).
3. Slide 10: Fix bottom box (thesis-line) touching/overlapping footer.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DECK = ROOT / "versions" / "deck_v7"
html_path = DECK / "index.html"
css_path = DECK / "style.css"

html = html_path.read_text(encoding="utf-8")
css = css_path.read_text(encoding="utf-8")

# =========================================================================
# 1. Slide 1: Cover Page
# =========================================================================
# Replace Cover slide
new_cover_html = """  <!-- 01 · 표지 -->
  <section class="slide cover active" data-slide="1">
    <div class="cover-photo cover-photo-a"></div><div class="cover-photo cover-photo-b"></div><div class="cover-wash"></div>
    <div class="cover-top"><b>CRISIS MANAGEMENT</b><i>|</i><span>위기관리(029) · 중간고사 대체 과제</span></div>
    <div class="cover-copy full-cover">
      <h1>변화의 결단은<br><em>왜 위기가 되는가</em></h1>
      <p class="cover-sub">공식 결정의 진전과 내부 공중 수용의 괴리</p>
      
      <div class="cover-seal">
        <span>CASE A<br><b>강원대–강릉원주대 통합</b><small>2025.04 · 평의원회 8:12 부결 → 15:6 가결</small></span>
        <span>CASE B<br><b>동덕여대 남녀공학 전환</b><small>2024.11 · 본관 점거·래커 시위 및 공론화 갈등</small></span>
      </div>

      <div class="cover-byline">
        <span class="byline-label">발표자</span>
        <b class="byline-name">조민성</b>
        <span class="byline-dot">·</span>
        <span class="byline-dept">부산대학교 미디어커뮤니케이션학과</span>
        <span class="byline-dot">·</span>
        <span class="byline-id">학번 202206251</span>
      </div>
    </div>
    <div class="cover-meta">
      <p class="cover-credit">배경 사진: 국립강릉원주대 및 동덕여자대학교 캠퍼스 기록사진</p>
    </div>
  </section>"""

old_cover_pattern = r'<section class="slide cover active" data-slide="1">.*?</section>'
html = re.sub(old_cover_pattern, new_cover_html, html, flags=re.DOTALL)
print("Updated Slide 1 (Cover)")

# =========================================================================
# 2. Slide 5: Kangwon photo -> protest_kangwon.jpg
# =========================================================================
old_s5_kangwon = r'<figure class="parallel-photo tall"><img src="assets/campus_kangwon\.jpg"[^>]*><figcaption>[^<]*</figcaption></figure>'
new_s5_kangwon = '<figure class="parallel-photo tall"><img src="assets/protest_kangwon.jpg" alt="강원대·강릉원주대 통합 반대 현수막 시위"><figcaption>통합 반대 시위 현수막 · 강원도민일보 2025.02.25</figcaption></figure>'

if re.search(old_s5_kangwon, html):
    html = re.sub(old_s5_kangwon, new_s5_kangwon, html)
    print("Updated Slide 5 Kangwon image to protest_kangwon.jpg")
else:
    print("Warning: Slide 5 Kangwon photo pattern not found")

# Update Slide 5 footer citation to include Kangwon Ilbo/Kado news
s5_footer_old = r'(<section class="slide[^"]*" data-slide="5">.*?<footer class="source-footer"><span>)(.*?)(</span>)'
s5_footer_new = r'\g<1>기사: 강원도민일보 (2025.02.25.) · 아주경제 (2024.11.13.) · Sturges (1994) 사전 커뮤니케이션\g<3>'
html = re.sub(s5_footer_old, s5_footer_new, html, flags=re.DOTALL)

# =========================================================================
# 3. Slide 10: Compact plate & timeline steps to give plenty of breathing room
# =========================================================================
# In Slide 10, remove the long duplicate caveat or shorten it, and add slide-10-grid class
old_s10_pattern = r'(<section class="slide paper-slide" data-slide="10">.*?<div class="parallel-grid">)'
new_s10_start = r'\g<1>' # we can style .slide[data-slide="10"] in CSS

html_path.write_text(html, encoding="utf-8")
print("HTML updated successfully!")

# =========================================================================
# 4. CSS Updates
# =========================================================================
cover_byline_and_slide10_css = """
/* ===== Cover Full Layout (No Box, Elegant Typography) ===== */
.cover-copy.full-cover {
  width: 1060px;
  top: 175px;
}
.cover-copy.full-cover h1 {
  font-size: 84px;
  line-height: 1.18;
  margin-bottom: 20px;
}
.cover-copy.full-cover .cover-sub {
  font-size: 32px;
  color: #f5efe3;
  margin-bottom: 0;
}
.cover-copy.full-cover .cover-seal {
  width: 820px;
  margin-top: 56px;
}
.cover-byline {
  display: flex;
  align-items: baseline;
  gap: 12px;
  margin-top: 42px;
  font-family: var(--sans);
  color: #d8d2c4;
}
.byline-label {
  font-size: 13px;
  font-weight: 800;
  letter-spacing: 0.12em;
  color: #dba08e;
  text-transform: uppercase;
  margin-right: 2px;
}
.byline-name {
  font-size: 26px;
  font-weight: 900;
  color: #ffffff;
  letter-spacing: -0.02em;
}
.byline-dot {
  font-size: 15px;
  color: #8c8577;
  font-weight: 300;
}
.byline-dept {
  font-size: 18px;
  font-weight: 600;
  color: #f0eae0;
}
.byline-id {
  font-size: 17px;
  font-weight: 700;
  color: #dba08e;
}

/* ===== Slide 10 Layout Fix: Prevent Bottom Box Touching Footer ===== */
.slide[data-slide="10"] .parallel-grid {
  margin-top: 16px;
  gap: 22px;
}
.slide[data-slide="10"] .parallel-plate {
  grid-template-rows: 1fr;
  box-shadow: 0 4px 12px rgba(0,0,0,.05);
}
.slide[data-slide="10"] .parallel-content.full {
  padding: 14px 22px 12px;
}
.slide[data-slide="10"] .parallel-content h3 {
  font-size: 22px;
  margin: 3px 0 8px;
}
.slide[data-slide="10"] .timeline-step {
  gap: 5px;
  margin-top: 6px;
  padding-left: 14px;
}
.slide[data-slide="10"] .timeline-step > div {
  padding: 2px 0 2px 8px;
}
.slide[data-slide="10"] .timeline-step time {
  font-size: 13px;
  margin-right: 6px;
}
.slide[data-slide="10"] .timeline-step b {
  font-size: 16px;
}
.slide[data-slide="10"] .timeline-step span {
  font-size: 13px;
  line-height: 1.28;
  margin-top: 1px;
}
.slide[data-slide="10"] .caveat-text {
  margin-top: 8px;
  font-size: 11.5px;
  line-height: 1.32;
  padding-top: 5px;
  border-top: 1px dashed var(--line);
}
.slide[data-slide="10"] .thesis-line {
  margin-top: 12px;
  padding: 10px 18px;
  font-size: 15px;
  line-height: 1.4;
}
"""

css += "\n" + cover_byline_and_slide10_css
css_path.write_text(css, encoding="utf-8")
print("CSS updated successfully!")
