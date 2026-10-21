# -*- coding: utf-8 -*-
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DECK = ROOT / "versions" / "deck_v7"
html_path = DECK / "index.html"
html = html_path.read_text(encoding="utf-8")

old_cover_pattern = r'<section class="slide cover active" data-slide="1">.*?</section>'

new_cover = """  <!-- 01 · 표지 -->
  <section class="slide cover active" data-slide="1">
    <div class="cover-photo cover-photo-a"></div><div class="cover-photo cover-photo-b"></div><div class="cover-wash"></div>
    <div class="cover-top"><b>CRISIS MANAGEMENT</b><i>|</i><span>위기관리(029) · 중간고사 대체 과제</span></div>
    <div class="cover-copy">
      <h1>변화의 결단은<br><em>왜 위기가 되는가</em></h1>
      <p class="cover-sub">공식 결정의 진전과 내부 공중 수용의 괴리</p>
      <div class="cover-seal">
        <span>CASE A<br><b>강원대–강릉원주대 통합</b><small>2025.04 · 평의원회 8:12 부결 → 15:6 가결</small></span>
        <span>CASE B<br><b>동덕여대 남녀공학 전환</b><small>2024.11 · 본관 점거·래커 시위 및 공론화 갈등</small></span>
      </div>
      <div class="cover-author-card">
        <span class="author-badge">RESEARCH &amp; PRESENTATION</span>
        <div class="author-details">
          <span class="author-name">조민성</span>
          <span class="author-id">202206251</span>
          <span class="author-dept">부산대학교 미디어커뮤니케이션학과</span>
        </div>
      </div>
    </div>
    <div class="cover-archive" aria-label="실제 기사 스크랩 및 문서 아카이브">
      <div class="archive-backdoc backdoc-a" aria-hidden="true"></div>
      <div class="archive-backdoc backdoc-b" aria-hidden="true"></div>
      <article class="paper-slip paper-slip-a">
        <header class="news-masthead masthead-gw">
          <div class="masthead-brand">
            <span class="masthead-title">江原日報</span>
            <span class="masthead-sub">GANGWON ILBO</span>
          </div>
          <div class="masthead-meta">
            <span>2025년 4월 1일 화요일</span>
            <span>제24158호 · 종합 1면</span>
          </div>
        </header>
        <div class="news-body">
          <h3 class="news-headline">강원대-강릉원주대 통합 추진 제동…<br>평의원회 부결로 혼란 불가피</h3>
          <p class="news-subhead">글로컬대학 지정 취소·사업비 50% 삭감 기로… 본부-평의원회 충돌</p>
          <p class="news-lead"><b>【춘천】</b> 강원대 대학평의원회가 1일 강원대-강릉원주대 통폐합신청서 승인 안건을 표결 끝에 부결시켰다. 2,150억 원 규모의 글로컬대학30 사업 무산 위기 속에서 사전 협의 부족과 캠퍼스 위상 축소를 둘러싼 갈등이 수면 위로 떠올랐다.</p>
        </div>
        <div class="news-cite">사료 대조: 제47차 대학평의원회 속기록 (찬성 8 : 반대 12 부결)</div>
      </article>
      <article class="paper-slip paper-slip-b">
        <header class="news-masthead masthead-yn">
          <div class="masthead-brand">
            <span class="masthead-title">YONHAP NEWS</span>
            <span class="masthead-sub">연합뉴스</span>
          </div>
          <div class="masthead-meta">
            <span>2025.12.09 16:35 송고</span>
            <span>사회면 속보 · 대학행정</span>
          </div>
        </header>
        <div class="news-body">
          <h3 class="news-headline">동덕여대 갈등 또 불붙나…<br>“공학반대 투표결과” vs “절차 문제”</h3>
          <p class="news-subhead">공론화위 권고 직후 학생 총투표 85.7% 반대… 본부 "2029년 추진" 공식화</p>
          <p class="news-lead"><b>(서울=연합뉴스)</b> 동덕여대 총학생회가 남녀공학 전환에 반대하는 전교생 총투표 결과를 발표하며 본부의 전환 방침 철회를 촉구했다. 반면 본부는 공론화위원회의 숙의 권고안에 따라 학칙 개정 절차를 밟겠다고 밝혀 학내 충돌이 재점화되고 있다.</p>
        </div>
        <div class="news-cite slip-split">
          <span><b>2025.12.02.</b> 공론화위원회 권고안 (9:2:1) <i>|</i> <b>12.03.~07.</b> 학생 총투표 (반대 85.7%)</span>
        </div>
      </article>
    </div>
    <div class="cover-meta">
      <p class="cover-credit">보도사진 출처: 연합뉴스(2024.11.21.) · 아주경제(2024.11.13., 한준구 기자)</p>
    </div>
  </section>"""

html = re.sub(old_cover_pattern, new_cover, html, flags=re.DOTALL)
html_path.write_text(html, encoding="utf-8")
print("Cover slide successfully replaced!")
