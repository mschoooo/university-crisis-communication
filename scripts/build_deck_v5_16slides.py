from pathlib import Path

deck_dir = Path("대학통합_위기커뮤니케이션_연구/07_HTML_발표덱/versions/deck_v5")

html_content = """<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>변화의 결단은 왜 위기가 되는가 | Editorial Archive (v5)</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
<main id="stage" aria-label="위기관리 연구 발표 슬라이드">

  <section class="slide cover active" data-slide="1">
    <div class="cover-photo cover-photo-a"></div><div class="cover-photo cover-photo-b"></div><div class="cover-wash"></div>
    <div class="cover-top"><b>CRISIS MANAGEMENT</b><i>|</i><span>위기관리(029) · 중간고사 대체 과제</span></div>
    <div class="cover-copy">
      <h1>변화의 결단은<br><em>왜 위기가 되는가</em></h1>
      <p class="cover-sub">공식 결정의 진전과 내부 공중 수용의 괴리</p>
      <div class="cover-seal"><span>CASE A<br><b>강원대–강릉원주대 통합</b><small>2025.04 · 평의원회 8:12 부결 → 15:6 가결</small></span><span>CASE B<br><b>동덕여대 남녀공학 전환</b><small>2024.11 · 본관 점거·래커 시위 및 공론화 갈등</small></span></div>
    </div>
    <div class="cover-archive" aria-label="실제 기사 제목과 공식 문서의 발췌">
      <div class="archive-backdoc backdoc-a" aria-hidden="true"><small>A02P · 제48차 대학평의원회 회의록</small><img src="assets/A02_staff_clip.png" alt=""></div>
      <div class="archive-backdoc backdoc-b" aria-hidden="true"><small>D08 · 공론화위원회 진행과정 및 의결 절차</small><img src="assets/D08_rule_clip.png" alt=""></div>
      <article class="paper-slip paper-slip-a">
        <div class="paper-kicker"><span>강원일보 · 2025.04.01 · 기사 제목 인용</span><span>A01P · 공식 회의록</span></div>
        <h3>강원대-강릉원주대 통합 추진 제동…<br>평의원회 부결로 혼란 불가피</h3>
        <div class="paper-image"><img src="assets/A01_title_clip.png" alt="강원대학교 제47차 대학평의원회 회의록 첫 페이지 제목 부분"></div>
        <p><b>제47차 대학평의원회 회의록 발췌</b> · 2025.04.01. 1·40쪽 (찬성 8 : 반대 12 부결)</p>
      </article>
      <article class="paper-slip paper-slip-b">
        <div class="paper-kicker"><span>연합뉴스 · 2025.12.09 · 기사 제목 인용</span><span>D06 · 공식 권고안</span></div>
        <h3>동덕여대 갈등 또 불붙나…<br>“공학반대 투표결과” vs “절차 문제”</h3>
        <div class="paper-image"><img src="assets/D06_title_clip.png" alt="동덕여자대학교 공학전환공론화 권고안 첫 페이지 제목 부분"></div>
        <p><b>동덕여대 공학전환공론화 권고안 발췌</b> · 2025.12.02. 2쪽 (학생 총투표 85.7% 반대)</p>
      </article>
    </div>
    <div class="cover-meta">
      <p>배경·보도사진 출처: 연합뉴스(2024.11.21.) · 아주경제(2024.11.13., 한준구 기자) · 강원대·동덕여대 공식 문서</p>
      <p class="cover-author">조민성(202206251) · 부산대학교 미디어커뮤니케이션학과</p>
    </div>
  </section>

  <section class="slide paper-slide" data-slide="2">
    <header class="folio"><span>01 / RESEARCH QUESTION</span><span>CASE FILE · 2024—2026</span></header>
    <p class="deck-kicker">문제제기 및 연구 설계</p>
    <h2>결정의 속도,<br><em>수용의 거리</em></h2>
    <div class="two-case-grid">
      <article class="case-plate">
        <figure class="case-photo"><img src="assets/campus_gangneung.jpg" alt="2024년 강릉원주대학교 전경 기록사진"><figcaption>국립강릉원주대 전경 · 김호진2, 2024 · CC BY 4.0</figcaption></figure>
        <div><span class="case-index teal">A / 통합</span><h3>강원대–강릉원주대</h3><p>4월 1일 <b>8:12 부결</b> → 4월 28일 수정안 <b>15:6 가결</b></p><small>서로 다른 회의의 표결 · 출석 20명 / 21명</small></div>
      </article>
      <article class="case-plate red-border">
        <figure class="case-doc"><img src="assets/D06_recommendation_clip.png" alt="동덕여대 공론화위원회의 공학전환 권고안 2쪽 발췌"><figcaption>공론화위원회 권고안 · D06, 2025.12.02, 2쪽</figcaption></figure>
        <div><span class="case-index brick">B / 공학 전환</span><h3>동덕여대</h3><p>권고·학칙 개정 뒤에도 학생 총투표 <b>85.7% 반대</b></p><small>입시 지원자 감소는 인과 미확인 참고 지표</small></div>
      </article>
    </div>
    <div class="thesis-line"><b>연구 질문</b><span>같은 구조개편 압박 아래, 어떤 조건의 조합이 제도적 진전과 내부 공중의 수용을 갈라놓았는가?</span></div>
    <footer class="source-footer"><span>A01P 40쪽 · A02P 44쪽 · D06 2쪽 · D10 · D15 · R1 · R2</span><span>02 / 16</span></footer>
  </section>

  <section class="slide paper-slide" data-slide="3">
    <header class="folio"><span>02 / THEORY</span><span>CAMERON · CONTINGENCY THEORY</span></header>
    <p class="deck-kicker">분석 틀 ①: 정황적 수용 이론</p>
    <h2>81개 변수의 체계,<br><em>움직이는 연속선</em></h2>
    <div class="theory-columns">
      <div class="theory-panel"><span>01 / 기저 입장</span><h3>사전성향적 변수</h3><p>거버넌스 구조 · 리더십 · 소통 문화가 갈등 이전 baseline을 설정한다.<br><small>(교재 표 2-5 내부 변수군)</small></p></div>
      <div class="theory-arrow">→</div>
      <div class="theory-panel"><span>02 / 동태적 압력</span><h3>상황적 변수</h3><p>외적 위협 · 긴급성 · 공중의 권력 · 가분적 쟁점이 입장을 이동시킨다.<br><small>(Cancel et al. 1999 핵심 5대 변수)</small></p></div>
      <div class="theory-arrow">→</div>
      <div class="theory-panel"><span>03 / 타협의 한계</span><h3>수용 제한 요인</h3><p>상충하는 복수 공중(교원 vs 학생)과 창학 정체성이 수용의 벽을 형성한다.<br><small>(Cameron et al. 2001)</small></p></div>
    </div>
    <div class="continuum">
      <div class="continuum-labels"><span>순수 옹호 <small>ADVOCACY (1)</small></span><span>정황적 선택의 동태적 연속선</span><span>순수 수용 <small>ACCOMMODATION (7)</small></span></div>
      <div class="continuum-track"><i></i><i></i><i></i><i></i><i></i><i></i><i></i></div>
      <div class="continuum-note"><b>개념적 전용의 한계</b>: 기업의 외부 공중과 달리 대학 구성원은 법정 거부권(평의원회)과 불이탈성(학생)을 지님.</div>
    </div>
    <footer class="source-footer"><span>Cancel et al. (1999) P99 · Cameron et al. (2001) P01 · 황성욱 (2014) H14 · 교재 표 2-5 (80–82쪽)</span><span>03 / 16</span></footer>
  </section>

  <section class="slide paper-slide" data-slide="4">
    <header class="folio"><span>02 / THEORY</span><span>CONFLICT LIFE CYCLE</span></header>
    <p class="deck-kicker">분석 틀 ②: 갈등관리 생애주기</p>
    <h2>결정 전부터 결정 후까지,<br><em>위기의 긴 시간</em></h2>
    <div class="life-grid">
      <article><span>01</span><h3>전조</h3><p>이슈 스캐닝<br>지형 정찰 (Heath)</p><small>H97</small></article>
      <article><span>02</span><h3>발생</h3><p>의견 고착화 전<br>초기 정보 (Sturges)</p><small>S94</small></article>
      <article><span>03</span><h3>대응</h3><p>행동적 수용 vs<br>수사 수용 (Cameron)</p><small>P01 · H14</small></article>
      <article><span>04</span><h3>회복</h3><p>결정 후 소통 문화<br>신뢰 복원 (Marra/Ham)</p><small>M04 · H11</small></article>
    </div>
    <div class="assessment-ribbon"><b>이 연구의 세 평가 축</b><span>① 제도적 결정 진전</span><i>+</i><span>② 핵심 요구의 실질 반영 (행동 수용도)</span><i>+</i><span>③ 내부 수용 및 외부 평판</span></div>
    <footer class="source-footer"><span>W05 · H11 · H97 · S94 · M04 · H22 · 세 평가 축은 발표자의 분석 틀</span><span>04 / 16</span></footer>
  </section>

  <section class="slide paper-slide" data-slide="5">
    <header class="folio"><span>03 / CASE A · KANGWON</span><span>THE FIRST VOTE · 2025.04.01</span></header>
    <p class="deck-kicker">강원대 사전 조건과 부결</p>
    <h2>2,150억 사업비 압박,<br><em>선제출과 8:12 부결</em></h2>
    <div class="timeline-layout">
      <div class="timeline">
        <div><time>2024.07.24</time><b>50% 삭감 경고</b><span>통합 지연 시 글로컬 사업비 위험</span></div>
        <div><time>2025.02.20</time><b>통합 신청서 선제출</b><span>평의원회 심의보다 먼저 교육부 제출</span></div>
        <div><time>02.28 → 03.18</time><b>257쪽 당일 배부 · 회의 무산</b><span>검토 시간 부족과 삼척 지역 반발</span></div>
        <div class="last"><time>04.01</time><b>제47차 평의원회 부결</b><span>찬성 8 · 반대 12 / 투표 20명</span></div>
      </div>
      <figure class="archive-card tall"><div class="archive-label">PRIMARY DOCUMENT / A01P</div><img src="assets/A01_vote_clip.png" alt="제47차 평의원회 회의록 40쪽의 8:12 부결 기록"><figcaption>제47차 대학평의원회 회의록 · 2025.04.01 · 40쪽</figcaption><p>신청서 본문의 '공무원 35명 차출' 미수정으로 인해 Sturges의 의견 고착화 발생.</p></figure>
    </div>
    <footer class="source-footer"><span>A03P 6쪽 · A01P 2–3, 40쪽 · A12 · A04 · S94</span><span>05 / 16</span></footer>
  </section>

  <section class="slide paper-slide" data-slide="6">
    <header class="folio"><span>03 / CASE A · KANGWON</span><span>REVISION &amp; SECOND VOTE · 2025.04.28</span></header>
    <p class="deck-kicker">강원대 27일간의 대응</p>
    <h2>두 번의 표결,<br><em>인력 조정과 가결</em></h2>
    <div class="vote-layout">
      <div class="vote-block">
        <p class="micro-title">대학평의원회 표결 · 서로 다른 출석 모수</p>
        <div class="vote-row"><span>04.01<small>20명 투표</small></span><div class="vote-track"><i class="yes" style="width:40%"></i><i class="no" style="width:60%"></i></div><b>8 : 12<small>부결</small></b></div>
        <div class="vote-row"><span>04.28<small>21명 투표</small></span><div class="vote-track"><i class="yes" style="width:71.43%"></i><i class="no" style="width:28.57%"></i></div><b>15 : 6<small>가결</small></b></div>
        <div class="legend"><span><i class="yes"></i> 찬성</span><span><i class="no"></i> 반대</span></div>
        <div class="staff-change"><span>원안<br><strong>공무원 35명</strong></span><i>→</i><span>수정안<br><strong>공무원 24명 + 외부 전문가 11명</strong></span></div>
      </div>
      <figure class="archive-card"><div class="archive-label">PRIMARY DOCUMENT / A02P</div><img src="assets/A02_staff_clip.png" alt="제48차 평의원회 회의록 7쪽의 공무원 24명·외부 전문가 11명 조정 설명"><figcaption>제48차 평의원회 회의록 · 2025.04.28 · 7쪽</figcaption><p>인력 조정(부분적 행동 수용)과 동시에 의장의 당일 수정안 제한이 병존함 (A02P 3-4쪽).</p></figure>
    </div>
    <footer class="source-footer"><span>A01P 40쪽 · A02P 3–4, 7–9, 44쪽 · A04 · A07 · 출석 모수(20→21명) 주의</span><span>06 / 16</span></footer>
  </section>

  <section class="slide paper-slide" data-slide="7">
    <header class="folio"><span>03 / CASE A · INTERPRETATION</span><span>CONTINGENT STANCE</span></header>
    <p class="deck-kicker">강원대 이론 분석</p>
    <h2>다중 조건의 결합,<br><em>부분적 행동 수용</em></h2>
    <div class="mechanism-grid">
      <div class="mechanism"><span>외적 긴급성</span><h3>재정 위협 &amp; 입시 시한</h3><p>2,150억 사업비 · 50% 삭감 경고 · 5월 말 대교협 대입전형 제출 기한</p></div>
      <div class="mechanism-arrow">+</div>
      <div class="mechanism"><span>공중의 권력</span><h3>평의원회 법정 거부권</h3><p>4/1 실제 8:12 부결로 본부 일방 옹호를 저지하고 협상 강제</p></div>
      <div class="mechanism-arrow">+</div>
      <div class="mechanism"><span>요구의 특성</span><h3>가분적 실리 쟁점</h3><p>공무원 정원(35→24명)이라는 수치 조절 가능한 협상 매개체</p></div>
    </div>
    <div class="interpretation-note"><b>이론적 결론</b><span>세 조건의 결합이 '부분적 행동 수용(24+11명)'을 낳아 15:6 가결을 이끌었으나, 당일 수정 제한과 명칭 불일치로 직원 불신 잔존.</span></div>
    <footer class="source-footer"><span>A02P 7–9, 44쪽 · A04 · A07 · A08 · A17 · P99 · H14</span><span>07 / 16</span></footer>
  </section>

  <section class="slide paper-slide" data-slide="8">
    <header class="folio"><span>04 / CASE B · DONGDUK</span><span>EARLY SIGNALS · 2024.09—2025.06</span></header>
    <p class="deck-kicker brick-text">동덕여대 전조 실패와 공론화</p>
    <h2>공론화보다 먼저<br><em>도착한 소문</em></h2>
    <div class="dongduk-timeline">
      <div><time>09.27 / 11.05</time><b>대학비전혁신추진단 논의</b><span>공학 전환 방안이 내부에서 동의됨</span></div>
      <div><time>11.07</time><b>학내 소문 유출</b><span>학생대표의 사실 확인 요청</span></div>
      <div class="crisis"><time>11.11</time><b>면담 취소 통지 · 본관 점거</b><span>Sturges의 밀실 규범 급속 고착화</span></div>
      <div><time>2024.11.21 → 2025.05</time><b>잠정 중단 합의 · 공론화위 출범</b><span>교원·학생·직원·동문 4단위 절차 개설</span></div>
    </div>
    <div class="document-band"><figure><img src="assets/D06_title_clip.png" alt="동덕여대 공학전환공론화 권고안 첫 페이지 제목 부분"><figcaption>사후에 구성된 공론화의 공식 기록 · D06, 2025.12.02, 1쪽</figcaption></figure><p class="analysis-quote">학생은 사전 협의의 부재를 문제 삼았고,<br>본부는 정식 의제 이전의 논의였다고 설명했다.</p></div>
    <footer class="source-footer"><span>D26 · D01 · D02 · D05 · D06 1쪽 · S94 · 2024년 현장 사진은 재사용 조건 미확인으로 미수록</span><span>08 / 16</span></footer>
  </section>

  <section class="slide paper-slide" data-slide="9">
    <header class="folio"><span>04 / CASE B · DELIBERATION</span><span>DIFFERENT QUESTIONS · DIFFERENT BASES</span></header>
    <p class="deck-kicker brick-text">동덕여대 공론화 분석</p>
    <h2>숙의의 숫자,<br><em>서로 다른 모수</em></h2>
    <div class="survey-grid">
      <div class="survey-major"><span class="micro-title">숙의기구 학생단 · ‘여대 유지’ 공표 비율</span><div class="before-after"><div><small>숙의 전</small><strong>80%</strong></div><i>→</i><div><small>숙의 후</small><strong>50%</strong></div></div><p>학생단 <b>구성원 12명</b>. 회차별 유효 응답 모수와 동일인 응답 여부는 공개되지 않았다.</p><figure class="document-crop"><img src="assets/D07_student_clip.png" alt="D07 3쪽 숙의기구 학생단의 전후 공표 비율 원표"><figcaption>D07 · 공론화 결과 참고자료, 3쪽 · 원표 발췌</figcaption></figure></div>
      <div class="survey-side"><div><span>최종 온라인 설문 · N=3,176</span><strong class="teal-text">51.8%</strong><p>교원·학생·직원 <b>1:1:1 가중</b> 시 공학 전환 선택</p></div><div><span>학생 응답 · n=2,889</span><strong class="brick-text">71.3%</strong><p>학생 응답에서 <b>여대 유지</b> 선택</p></div><div><span>무가중 단순합산 · N=3,176</span><strong>66.1%</strong><p>전체 응답을 인원수대로 합산한 <b>여대 유지</b> 비율</p></div></div>
    </div>
    <footer class="source-footer"><span>D07 1, 3–4, 17쪽 · D08 4, 8–9, 19쪽 · 가중·무가중 집계 방식의 정면 충돌</span><span>09 / 16</span></footer>
  </section>

  <section class="slide paper-slide" data-slide="10">
    <header class="folio"><span>04 / CASE B · AFTER THE DECISION</span><span>DECEMBER 2025—JANUARY 2026</span></header>
    <p class="deck-kicker brick-text">동덕여대 후속 결정</p>
    <h2>조기 발표와 가결,<br><em>재점화된 불신</em></h2>
    <div class="aftermath-grid">
      <div class="aftermath-card red-accent"><span>12.03 / 학생 총투표</span><strong>85.7<small>% 반대</small></strong><p>투표 3,470명 중 반대 2,975표 (첫날 총장 조기 발표 충돌)</p></div>
      <div class="aftermath-card teal-accent"><span>2026.01.12 / 대학평의원회</span><strong>8 <small>:</small> 2</strong><p>학칙 개정안 가결 · 학생위원 2명 서명 거부 및 공문 논란</p></div>
      <div class="aftermath-card muted-accent"><span>2026학년도 / 지원 동향</span><strong>−32.9<small>%</small></strong><p>전년 대비 수시·정시 합계 감소. 원인 미확인 참고 지표.</p></div>
    </div>
    <div class="after-note"><b>시간 순서 검증</b><span>수시 접수는 <strong>2025년 9월 8–12일</strong>이었다. 12월 3일 발표는 수시 감소의 원인이 될 수 없다. 정시 감소의 원인도 확인되지 않았다.</span></div>
    <footer class="source-footer"><span>D09 · D10 · D14 · D15 · AD26S · AD26R · D22 · D23</span><span>10 / 16</span></footer>
  </section>

  <section class="slide paper-slide" data-slide="11">
    <header class="folio"><span>04 / CASE B · INTERPRETATION</span><span>MULTIPLE PUBLICS &amp; LEGITIMACY</span></header>
    <p class="deck-kicker brick-text">동덕여대 이론 분석</p>
    <h2>상충하는 공중,<br><em>수사 혼합적 수용</em></h2>
    <div class="publics-grid">
      <article><span>학교 본부 &amp; 교원·직원</span><h3>제도적 대표성</h3><p>교원(76.0%)·직원(68.5%) 찬성, 1:1:1 가중 강조, 2029년 유예 배려</p><small>D06 · D09 · D11</small></article>
      <div class="publics-vs">↔</div>
      <article><span>학생 공중</span><h3>당사자 수와 창학 정체성</h3><p>학생 응답 71.3% 유지, 총투표 85.7% 반대, 1/23 가치 절하 비판</p><small>D07 · D10</small></article>
    </div>
    <div class="theory-diagnosis"><span>CONTINGENCY THEORY / 수용 제한 요인 (Cameron et al. 2001)</span><p>상충하는 복수 공중 + 비가분적 정체성 + 학생 단독 거부권 부재. 공론화 개설과 2029년 유예라는 <b>수사·절차적 수용</b>을 취하되, 전환 결론과 가중 규칙은 일방 옹호 강행.</p></div>
    <figure class="mini-document"><img src="assets/D08_rule_clip.png" alt="공론화위원회 제4차 회의 의결방식 원문 발췌"><figcaption>D08 · 제4차 공론화위원회 의결방식, 19쪽</figcaption></figure>
    <footer class="source-footer"><span>P01 · H14 · D06 · D07 4쪽 · D08 19쪽 · D09 · D10 · D11</span><span>11 / 16</span></footer>
  </section>

  <section class="slide paper-slide" data-slide="12">
    <header class="folio"><span>05 / COMPARATIVE ANALYSIS</span><span>ADVOCACY ↔ ACCOMMODATION</span></header>
    <p class="deck-kicker">두 대학 직접 비교</p>
    <h2>5대 쟁점 매트릭스,<br><em>수용의 질적 분화</em></h2>
    <div class="compare-rows">
      <div><span>강원대</span><div class="compare-line teal-line"><i></i><b>조직·인력안 수정</b></div><p>공무원 35→24명 · 외부 전문가 11명. 부분적 <b>행동 수용</b> 해석 가능.</p></div>
      <div><span>동덕여대</span><div class="compare-line red-line"><i></i><b>공론화 절차·전환 시점 유예</b></div><p>숙의와 권고 절차는 열었으나 가중 규칙·결론은 고수. <b>수사 혼합적 수용</b> 해석.</p></div>
    </div>
    <div class="compare-caveats"><div><b>제도적 결정</b><span>두 사례 모두 공식 절차가 진전 (15:6 가결 vs 8:2 가결)</span></div><div><b>내부 공중 수용</b><span>두 사례 모두 미흡 (직원 시위 잔존 vs 학생 85.7% 반대)</span></div><div><b>타협의 매개체</b><span>강원대는 가분적 정원 수치, 동덕여대는 비가분 정체성 대신 3년 유예</span></div></div>
    <footer class="source-footer"><span>A01P 40쪽 · A02P 7–9, 44쪽 · D06 · D07 · D10 · D15 · H14 · 단순 이분법 극복</span><span>12 / 16</span></footer>
  </section>

  <section class="slide paper-slide" data-slide="13">
    <header class="folio"><span>06 / EARLY CRISIS MANAGEMENT</span><span>FROM WARNING TO RESPONSE</span></header>
    <p class="deck-kicker">사전 위기관리 진단</p>
    <h2>위기 이전의 선택,<br><em>징후와 타이밍</em></h2>
    <div class="prevention-flow">
      <article><b>01 · 징후 포착</b><h3>Heath</h3><p>인력 이동·정체성 손실을 고영향 이슈로 사전 스캐닝 실패</p><small>H97</small></article>
      <i>→</i>
      <article><b>02 · 초기 타이밍</b><h3>Sturges</h3><p>선제출·소문 유출로 비공식 루머에 의한 의견 고착화 초래</p><small>S94</small></article>
      <i>→</i>
      <article><b>03 · 비선형 예방</b><h3>Jaques</h3><p>사전 위험 예방 실패가 사후 대응 및 심의 비용을 증폭</p><small>R5</small></article>
      <i>→</i>
      <article><b>04 · 소통 문화</b><h3>Marra / Hwang</h3><p>형식적 절차보다 정보 공유 문화와 PR 자율성이 결정적</p><small>M04 · H22</small></article>
    </div>
    <div class="prevention-bottom"><span>사례 A 처방 · 신청서 제출 최소 30일 전 인력영향평가 공개 및 신구대비표 의무 사전 배부</span><span>사례 B 처방 · 공론화 착수 전 가중치·단순합산 이원화 병기 합의 및 총투표 결과 존중</span></div>
    <footer class="source-footer"><span>W05 · H11 · H97 · S94 · P01 · M04 · H22 · R5 · 처방은 발표자의 제언</span><span>13 / 16</span></footer>
  </section>

  <section class="slide paper-slide" data-slide="14">
    <header class="folio"><span>07 / PROCEDURAL JUSTICE</span><span>RULES &amp; LEGITIMACY</span></header>
    <p class="deck-kicker">절차적 공정성 평가</p>
    <h2>규칙의 정당성,<br><em>발언권과 결정권</em></h2>
    <div class="two-case-grid" style="margin-bottom:14px;">
      <article class="case-plate" style="padding:16px 20px;">
        <span class="micro-title" style="color:var(--teal); font-weight:800; margin-bottom:8px; display:block;">Leventhal (1980) 6대 절차 규칙 대조</span>
        <ul style="margin:0; padding-left:18px; font-size:15px; line-height:1.6; color:var(--ink);">
          <li><b>일관성·대표성 위반:</b> 동덕 1:1:1 가중치로 학생(91%) 표 가치를 1/23로 희석. 평의원회 10석 중 2석 과소 반영.</li>
          <li><b>직권 행사 논란:</b> 강원 4/28 의장이 28일 지연을 이유로 당일 수정동의안 접수를 원천 차단.</li>
          <li><b>수정 가능성:</b> 강원 4/1 8:12 부결 후 재상정 작동 vs 동덕 2/3 다결 규칙으로 학생 이의 차단.</li>
        </ul>
      </article>
      <article class="case-plate red-border" style="padding:16px 20px;">
        <span class="micro-title" style="color:var(--red); font-weight:800; margin-bottom:8px; display:block;">Tyler (1988) &amp; Główczewski (2023) 모델</span>
        <p style="font-size:15px; line-height:1.6; margin:0 0 8px; color:var(--ink);">
          <b>Voice(발언권) ≠ Decision Control(결정 통제권):</b><br>
          공론화로 말할 기회는 주었으나 결정권을 박탈당했을 때 구성원은 제도를 기만으로 인식하고 냉소를 표출함.
        </p>
        <div style="background:var(--card); padding:8px 12px; border-left:3px solid var(--red); font-size:13.5px; color:var(--muted);">
          <b>최신 고등교육 실증(R4):</b> 대학생의 대학 당국 신뢰는 결과보다 '절차적 공정성'에 의해 가장 강력하게 결정됨.
        </div>
      </article>
    </div>
    <div class="thesis-line" style="margin-top:0;"><b>절차 정당성 결론</b><span>합법적 관문 통과(Legality)와 주관적 절차 공정성(Fairness)의 괴리가 공식 결정 후에도 불복종을 낳는다.</span></div>
    <footer class="source-footer"><span>Leventhal (1980) LEV · Tyler (1988) TYL · Główczewski &amp; Burdziej (2023) R4 · D08 19쪽 · D14</span><span>14 / 16</span></footer>
  </section>

  <section class="slide final-slide" data-slide="15">
    <header class="folio"><span>08 / CONCLUSION</span><span>THREE CONDITIONS &amp; ACTIONABLE STEPS</span></header>
    <p class="deck-kicker">결론 및 실무 제언</p>
    <h2>수용으로 가는<br><em>세 가지 조건</em></h2>
    <div class="conclusion-list">
      <div><span>01</span><h3>시점</h3><p>소문이 의견을 굳히기 전에<br>핵심 쟁점 대안을 선공개한다.</p></div>
      <div><span>02</span><h3>규칙</h3><p>표본 비대칭 시 가중·무가중을<br>병기하고 절차 전 합의한다.</p></div>
      <div><span>03</span><h3>행동</h3><p>수사적 공감을 넘어 확인 가능한<br>자원·인력 수정을 남긴다.</p></div>
    </div>
    <div class="prevention-bottom" style="margin-top:16px;">
      <span><b>사례 A 실행 대안</b> · 사전 인력영향평가제(30일 전) · 신구대비표 의무화 · 노사 동수 옴부즈퍼슨</span>
      <span><b>사례 B 실행 대안</b> · 가중·단순합산 이원화 병기제 · 부분적 자율전공 모델 · 총투표 후 발표 유예</span>
    </div>
    <blockquote class="final-quote" style="margin-top:14px;">“절차의 개설과<br>결정의 가결은<br>구성원의 수용과<br>같은 지표가 아니다.”</blockquote>
    <div class="final-small">연구 한계: 공개 사료로 인과·개인별 태도 변화를 입증할 수 없음. AI 도구·지원 범위·연구자 기여의 상세 고지는 발표자 노트에 수록.</div>
    <footer class="source-footer"><span>S94 · D07 3–4쪽 · A02P 7–9쪽 · P01 · H14 · 처방은 연구자의 제언</span><span>15 / 16</span></footer>
  </section>

  <section class="slide paper-slide references-slide" data-slide="16">
    <header class="folio"><span>09 / REFERENCES</span><span>ACADEMIC WORKS &amp; PRIMARY RECORDS</span></header>
    <p class="deck-kicker">참고문헌 및 인용 자료</p>
    <h2>분석을 지탱한<br><em>문헌과 사건 기록</em></h2>
    <div class="reference-columns">
      <section class="reference-column">
        <div class="reference-head"><span>THEORY / 핵심 문헌</span><b>정황적 수용 및 절차 공정성</b></div>
        <p><b>Cancel et al. (1999); Cameron et al. (2001); 황성욱 (2014).</b> 정황적 수용 이론 및 행동적/수사적 수용 구분. <small>P99 · P01 · H14</small></p>
        <p><b>Leventhal (1980); Tyler (1988); Główczewski &amp; Burdziej (2023).</b> 절차적 공정성 6대 규칙과 대학 당국 신뢰. <small>LEV · TYL · R4</small></p>
        <p><b>Heath (1997); Sturges (1994); Marra (2004); Jaques (2007).</b> 이슈 스캐닝·의견 고착화·소통 문화·비선형 위기관리. <small>H97 · S94 · M04 · R5</small></p>
        <p><b>김동우 외 (2025); 김택형 (2025); 김보엽 (2024); Erjansola et al. (2026).</b> 대학 통합 시 행정직원 체감 및 거버넌스. <small>R1 · R2 · R3 · R6</small></p>
      </section>
      <section class="reference-column primary-column">
        <div class="reference-head"><span>EVIDENCE / 사건 기록</span><b>대학 공식 문서와 검증 자료</b></div>
        <p><b>강원대학교 (2025.04.01 / 04.28).</b> 제47차(8:12 부결)·제48차(15:6 가결) 대학평의원회 회의록. <small>A01P · A02P</small></p>
        <p><b>동덕여대 공론화위 (2025.12.02 / 12.08).</b> 권고안(9:2:1) 및 설문 상세자료, 제4차 회의 의결 규칙. <small>D06 · D07 · D08</small></p>
        <p><b>동덕여대 후속 기록 (2025–2026).</b> 학생 총투표(85.7% 반대)·평의원회(8:2)·입시 지원 통계. <small>D10 · D14 · D15 · AD26S · AD26R</small></p>
        <p><b>공식 공고 및 입장문 (2024–2026).</b> 학부모 서신(D01)·합의문(D02)·학칙 개정(D22, D23)·소통 일지(D26). <small>D01 · D02 · D22 · D26</small></p>
      </section>
    </div>
    <footer class="source-footer"><span>전체 문헌·원문 URL: <a href="sources.html">원자료·수업 문헌 검증 인덱스 ↗</a> · 사진·문서 이미지: <a href="asset_sources.md">이미지 출처 목록 ↗</a></span><span>16 / 16</span></footer>
  </section>

</main>

<aside id="notes-drawer" class="overlay-panel" aria-label="발표자 노트와 상세 논증"><div class="modal-header"><h3 id="notes-title">발표자 노트</h3><button class="close-btn" type="button">닫기 (Esc)</button></div><p id="notes-body"></p><p id="notes-qa"></p><h4>v5 상세 분석 근거</h4><p id="notes-detail"></p></aside>
<aside id="toc-modal" class="overlay-panel" aria-label="슬라이드 목차"><div class="modal-header"><h3>목차 · M</h3><button class="close-btn" type="button">닫기 (Esc)</button></div><div class="toc-grid">
  <button class="toc-item" data-slide="1">01 · 표지 / 연구 질문</button><button class="toc-item" data-slide="2">02 · 두 사례의 대조</button><button class="toc-item" data-slide="3">03 · 정황적 수용 이론</button><button class="toc-item" data-slide="4">04 · 갈등관리 생애주기</button><button class="toc-item" data-slide="5">05 · 강원대 / 위기의 발생</button><button class="toc-item" data-slide="6">06 · 강원대 / 수정과 표결</button><button class="toc-item" data-slide="7">07 · 강원대 / 이론 분석</button><button class="toc-item" data-slide="8">08 · 동덕여대 / 초기 갈등</button><button class="toc-item" data-slide="9">09 · 동덕여대 / 공론화</button><button class="toc-item" data-slide="10">10 · 동덕여대 / 후속 결정</button><button class="toc-item" data-slide="11">11 · 동덕여대 / 이론 분석</button><button class="toc-item" data-slide="12">12 · 두 대학 직접 비교</button><button class="toc-item" data-slide="13">13 · 사전 위기관리</button><button class="toc-item" data-slide="14">14 · 절차적 공정성</button><button class="toc-item" data-slide="15">15 · 결론 / 실무 제언</button><button class="toc-item" data-slide="16">16 · 참고문헌·사건 기록</button>
</div></aside>
<aside id="data-modal" class="overlay-panel" aria-label="수치 검증"><div class="modal-header"><h3>핵심 수치 검증 · D</h3><button class="close-btn" type="button">닫기 (Esc)</button></div><div class="data-grid"><article><h4>강원대</h4><p>4/1 표결 8:12 (20명) · A01P 40쪽<br>4/28 표결 15:6 (21명) · A02P 44쪽<br>공무원 35→24명, 외부 전문가 11명 · A02P 7–9쪽<br><b>다중 조건: 긴급성 × 거부권 × 가분적 쟁점.</b></p></article><article><h4>동덕여대</h4><p>학생단 구성 12명, 공표 비율 80→50%, 유효 응답 모수 미공개 · D07 1, 3쪽<br>1:1:1 가중 공학 51.8%, 학생 응답 유지 71.3%, 무가중 유지 66.1% · D07 4쪽<br>총투표 반대 85.7% · D10 / 지원자 −32.9% · D15<br><b>수용 제한: 상충 공중 × 비가분 정체성 × 거부권 부재.</b></p></article></div></aside>
<nav id="controls" aria-label="슬라이드 조작"><button id="prev" type="button">← 이전</button><span id="count">1 / 16</span><button id="next" type="button">다음 →</button><button id="btn-toc" type="button">목차 M</button><button id="btn-notes" type="button">노트 N</button><button id="btn-data" type="button">수치 D</button><button id="btn-fs" type="button">전체 F</button><a href="sources.html">원자료</a><a href="asset_sources.md">이미지 출처</a><a href="deck_v5.pdf">PDF</a></nav>
<script src="archive_details.js"></script><script src="slides.js"></script>
</body>
</html>
"""

(deck_dir / "index.html").write_text(html_content, encoding="utf-8")
print("index.html for deck_v5 (16 slides) written successfully.")
