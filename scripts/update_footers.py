# -*- coding: utf-8 -*-
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DECK = ROOT / "versions" / "deck_v7"
html_path = DECK / "index.html"
html = html_path.read_text(encoding="utf-8")

# Define cleaned footers (strictly keeping papers, news, and academic notes, removing internal IDs)
cleaned_footers = {
    2: "<span>평가 기준은 발표자의 분석 틀 · 공식 심의 기록 및 학생 총투표 결과 바탕</span><span>02 / 15</span>",
    3: "<span>『PR커뮤니케이션』 제2장 표 2-5 (80–82쪽) · Cancel et al. (1997, 1999) · Cameron et al. (2001) · 황성욱 (2014)</span><span>03 / 15</span>",
    4: "<span>강원대학교·강릉원주대 글로컬대학30 통합계획서 · 동덕여자대학교 VISION 2040 중장기 발전계획</span><span>04 / 15</span>",
    5: "<span>기사: 아주경제 (2024.11.13.) · 대학저널 (2024.07.24.) · Sturges (1994) 사전 커뮤니케이션</span><span>05 / 15</span>",
    6: "<span>기사: 강원일보 (2025.04.01.) · 강원대학교 제47차 대학평의원회 회의록 (2025.04.01.)</span><span>06 / 15</span>",
    7: "<span>강원대학교 제48차 대학평의원회 회의록 (2025.04.28.) · 황성욱 (2014) · 출석 모수(20→21명) 차이 주의</span><span>07 / 15</span>",
    8: "<span>기사: 연합뉴스 (2024.11.21.) · 동덕여자대학교 처장단-총학생회 합의문 (2024.11.21.) · 황성욱 (2014)</span><span>08 / 15</span>",
    9: "<span>동덕여자대학교 공학전환 공론화위원회 권고안 및 설문 결과 (2025.12.02.) · 가중 규칙 분석</span><span>09 / 15</span>",
    10: "<span>기사: 연합뉴스 (2025.12.09.) · 동덕여자대학교 학칙 일부개정 공포 (2026.02.26.) · 학생 총투표 공고</span><span>10 / 15</span>",
    11: "<span>Cancel et al. (1997) · Cameron et al. (2001) · 황성욱 (2014) · 변수는 상황적 조건이며 단일 인과 요인으로 단정하지 않음</span><span>11 / 15</span>",
    12: "<span>Heath (1997) 전략적 이슈관리 · Sturges (1994) 사전 위기 커뮤니케이션 · Wilcox & Cameron (2005)</span><span>12 / 15</span>",
    13: "<span>Leventhal (1980) 절차적 정의 6대 규칙 · Tyler (1988) 발언권과 결정 통제권 · 세 기준은 발표자의 분석 틀</span><span>13 / 15</span>",
    14: "<span>Sturges (1994) · Heath (1997) · Leventhal (1980) · Cameron et al. (2001) · 황성욱 (2014) · 실무 원칙 제언</span><span>14 / 15</span>",
    15: "<span>전체 문헌 원문 서지 목록: deck_v7_참고문헌.md · 이미지 출처: asset_sources.md</span><span>15 / 15</span>"
}

for slide_num, new_f in cleaned_footers.items():
    # Find section with data-slide="X"
    pattern = rf'(<section class="slide[^"]*" data-slide="{slide_num}".*?<footer class="source-footer">)(.*?)(</footer>)'
    match = re.search(pattern, html, re.DOTALL)
    if match:
        html = html[:match.start(2)] + new_f + html[match.end(2):]
        print(f"Updated footer for Slide {slide_num}")
    else:
        print(f"Warning: Slide {slide_num} footer not found")

# Also on Slide 15 references: clean internal codes in tags: <small>P97</small>, etc.
# Replace <small>[A-Z0-9· ]+</small> inside Slide 15
sec15_match = re.search(r'(<section class="slide[^"]*" data-slide="15">.*?</section>)', html, re.DOTALL)
if sec15_match:
    sec15 = sec15_match.group(1)
    # Remove cryptic tags like <small>P97</small>, <small>A01P · A02P</small>
    sec15_clean = re.sub(r'\s*<small>[A-Z0-9·,–\s/]+</small>', '', sec15)
    # Replace in html
    html = html[:sec15_match.start(1)] + sec15_clean + html[sec15_match.end(1):]
    print("Cleaned internal codes from Slide 15 references")

html_path.write_text(html, encoding="utf-8")
print("Footers successfully updated!")
