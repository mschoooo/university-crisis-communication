# -*- coding: utf-8 -*-
"""Update style.css and slides.js for deck_v7."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DECK = ROOT / "versions" / "deck_v7"
css_path = DECK / "style.css"
js_path = DECK / "slides.js"

css = css_path.read_text(encoding="utf-8")
js = js_path.read_text(encoding="utf-8")

# 1. Update style.css:
# Add global word-break: keep-all;
if "word-break: keep-all" not in css:
    css = "*, *:before, *:after { word-break: keep-all; box-sizing: border-box; }\n" + css

# Replace .cover-author-card, .cover-archive, .paper-slip, .news-masthead, numbers, animations
cover_and_news_css = """
/* ===== Cover Slide: Presenter Card & Cleaned Meta ===== */
.cover-author-card {
  margin-top: 26px;
  display: inline-flex;
  flex-direction: column;
  gap: 5px;
  padding: 12px 20px 14px;
  background: rgba(18, 22, 19, 0.82);
  border: 1px solid rgba(228, 220, 205, 0.32);
  border-left: 5px solid var(--brick);
  box-shadow: 0 6px 20px rgba(0,0,0,0.35);
  border-radius: 2px;
}
.cover-author-card .author-badge {
  font: 800 11px var(--sans);
  letter-spacing: 0.16em;
  color: #dba08e;
  text-transform: uppercase;
}
.cover-author-card .author-details {
  display: flex;
  align-items: baseline;
  gap: 14px;
}
.cover-author-card .author-name {
  font: 900 24px var(--sans);
  color: #ffffff;
  letter-spacing: -0.02em;
}
.cover-author-card .author-id {
  font: 700 16px var(--sans);
  color: #e2c0b5;
}
.cover-author-card .author-dept {
  font: 600 15px var(--sans);
  color: #d6d0c4;
}
.cover-meta {
  position: absolute;
  left: 80px;
  bottom: 45px;
  z-index: 4;
}
.cover-meta .cover-credit {
  font: 500 12px var(--sans);
  color: #8c867a;
  margin: 0;
  letter-spacing: 0.01em;
}

/* ===== Cover Archive: 85% Sized Authentic Newspaper Clippings ===== */
.cover-archive {
  position: absolute;
  left: 815px;
  top: 70px;
  width: 715px;
  height: 750px;
  z-index: 2;
}
.archive-backdoc {
  position: absolute;
  border: 1px solid #bfb39f;
  box-shadow: 4px 10px 24px rgba(0,0,0,0.28);
  z-index: 1;
  border-radius: 2px;
  pointer-events: none;
}
.backdoc-a {
  width: 485px;
  height: 255px;
  top: 18px;
  left: 110px;
  transform: rotate(2.8deg);
  background: linear-gradient(135deg, #eee7d8 0%, #e2d9c5 100%);
}
.backdoc-b {
  width: 485px;
  height: 255px;
  top: 425px;
  left: 75px;
  transform: rotate(-2.4deg);
  background: linear-gradient(135deg, #e4dcce 0%, #dcd1be 100%);
}

.paper-slip {
  position: absolute;
  width: 510px;
  height: 305px;
  padding: 14px 18px 12px;
  background: #faf6ed;
  border: 1px solid #d4c8b2;
  outline: 1px dashed #c0b299;
  outline-offset: -7px;
  box-shadow: 6px 14px 28px rgba(0,0,0,0.35), 0 1px 3px rgba(0,0,0,0.18);
  z-index: 2;
  display: flex;
  flex-direction: column;
  box-sizing: border-box;
}
.paper-slip:after {
  content: "";
  position: absolute;
  top: -8px;
  left: 42%;
  width: 82px;
  height: 19px;
  background: rgba(220, 210, 185, 0.65);
  box-shadow: 0 1px 2px rgba(0,0,0,0.1);
  transform: rotate(-1.5deg);
}
.paper-slip-a {
  top: 30px;
  left: 95px;
  transform: rotate(-1.8deg);
}
.paper-slip-b {
  top: 365px;
  left: 115px;
  transform: rotate(1.4deg);
}

.news-masthead {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  border-bottom: 2px solid #222520;
  padding-bottom: 5px;
  margin-bottom: 8px;
}
.masthead-gw .masthead-title {
  font-family: var(--serif);
  font-size: 20px;
  font-weight: 900;
  letter-spacing: 0.08em;
  color: #161815;
}
.masthead-gw .masthead-sub {
  font-family: var(--sans);
  font-size: 9.5px;
  font-weight: 800;
  letter-spacing: 0.12em;
  color: var(--brick);
  margin-left: 6px;
}
.masthead-yn .masthead-title {
  font-family: var(--sans);
  font-size: 17px;
  font-weight: 900;
  letter-spacing: 0.04em;
  color: #0b4578;
}
.masthead-yn .masthead-sub {
  font-family: var(--sans);
  font-size: 11px;
  font-weight: 800;
  color: #222;
  margin-left: 5px;
}
.masthead-meta {
  font: 700 11px var(--sans);
  color: #58544d;
  text-align: right;
  line-height: 1.25;
}
.news-headline {
  font-family: var(--serif);
  font-size: 18px;
  line-height: 1.26;
  margin: 0 0 5px;
  letter-spacing: -0.04em;
  color: #151813;
  font-weight: 900;
}
.news-subhead {
  font: 700 11.5px var(--sans);
  line-height: 1.35;
  color: #43403a;
  margin: 0 0 6px;
  padding-left: 6px;
  border-left: 2.5px solid var(--brick);
}
.news-lead {
  font-family: var(--serif);
  font-size: 11.5px;
  line-height: 1.45;
  color: #262823;
  margin: 0 0 6px;
  background: rgba(255,255,255,0.7);
  padding: 5px 8px;
  border: 1px solid #dfd7c6;
  text-align: justify;
  flex-grow: 1;
}
.news-lead b {
  color: #1a1c18;
  font-family: var(--sans);
}
.news-cite {
  font: 600 10.5px var(--sans);
  color: #666258;
  margin: auto 0 0;
  border-top: 1px dashed #cfc5b3;
  padding-top: 4px;
}
.news-cite.slip-split {
  display: flex;
  justify-content: space-between;
}

/* ===== Typography: All Numbers in Gothic (Sans-Serif) with Clear Hierarchy ===== */
.num, time, .pct, .stat-num, .stat-major, .vote-block, .vote-badge,
.timeline-step time, .timeline-step b, .case-plate p b, .case-plate h3,
.delib-stat-item b, .vote-card b, .fact-list li b, .clean-list li b,
.cover-top, .cover-seal small, .cover-seal b, .author-id, .masthead-meta,
.step-num, .crit-label, .case-index, .big-stat, .stat-primary, .stat-secondary,
.stat-tertiary, .criteria article b {
  font-family: var(--sans) !important;
  font-feature-settings: "tnum" 1;
}

/* 1급 위계: 핵심 의사결정 및 대형 핵심 수치 */
.stat-primary, .survey-major b, .big-vote b, .vote-card.highlight b, .num-hero {
  font-family: var(--sans) !important;
  font-size: 46px !important;
  font-weight: 900 !important;
  line-height: 1.05;
  letter-spacing: -0.04em;
  display: inline-block;
}
.stat-primary.teal, .vote-teal { color: var(--teal) !important; }
.stat-primary.brick, .vote-brick { color: var(--brick) !important; }

/* 2급 위계: 중간 규모 분석 수치 (정원 감축, 설문 세부 비율, 사업비) */
.stat-secondary, .timeline-step b, .delib-stat-item b, .staff-change b, .case-plate p b {
  font-family: var(--sans) !important;
  font-size: 20px;
  font-weight: 800;
  line-height: 1.25;
  color: var(--ink);
}

/* 3급 위계: 날짜, 순번, 모수, 페이지 번호 */
.stat-tertiary, time, .timeline-step time, .folio span, .step-num, .source-footer span {
  font-family: var(--sans) !important;
  font-size: 13.5px;
  font-weight: 700;
  letter-spacing: 0.02em;
}

/* ===== Smooth Animations for Tables, Numbers, and Bars ===== */
.slide.motion-in [data-motion="number"] {
  animation: numReveal 0.6s cubic-bezier(0.16, 1, 0.3, 1) both;
  animation-delay: var(--motion-delay, 0ms);
}
.slide.motion-in [data-motion="bar"] {
  animation: barExpand 0.75s cubic-bezier(0.16, 1, 0.3, 1) both;
  animation-delay: var(--motion-delay, 0ms);
  transform-origin: left center;
}
.slide.motion-in [data-motion="row"] {
  animation: cardFadeUp 0.52s cubic-bezier(0.16, 1, 0.3, 1) both;
  animation-delay: var(--motion-delay, 0ms);
}

@keyframes numReveal {
  0% { opacity: 0; transform: translateY(10px) scale(0.92); }
  100% { opacity: 1; transform: translateY(0) scale(1); }
}
@keyframes barExpand {
  0% { transform: scaleX(0); opacity: 0.2; }
  100% { transform: scaleX(1); opacity: 1; }
}
@keyframes cardFadeUp {
  0% { opacity: 0; transform: translateY(14px); }
  100% { opacity: 1; transform: translateY(0); }
}
"""

# Append or replace rules in style.css
css += "\n" + cover_and_news_css
css_path.write_text(css, encoding="utf-8")
print("Appended cover, typography, number hierarchy, and animation CSS rules to style.css")

# 2. Update slides.js motionPlan to attach animation triggers to tables, stats, and numbers
new_motion_plan = """const motionPlan = [
  ['.stat-primary, .survey-major b, .vote-block b, .timeline-step b, .case-plate p b, .staff-change b, .analysis-box b, .big-stat, .delib-stat-item b, .vote-card b', 'number'],
  ['.vote-track i, .delib-bar i, .progress-bar i, .continuum-track i, .survey-bar i, .bar-fill', 'bar'],
  ['.timeline-step > div, .parallel-plate, .deep-left, .archive-plate, .criteria article, .var-panel, .reference-column, .aftermath-card, .vote-card', 'row']
];"""

old_plan_pattern = r'const motionPlan = \[.*?\];'
js = re.sub(old_plan_pattern, new_motion_plan, js, flags=re.DOTALL)
js_path.write_text(js, encoding="utf-8")
print("Updated motionPlan in slides.js successfully!")
