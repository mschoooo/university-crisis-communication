# Editorial Archive Deck v7 (학술 보고서 최종본)

본 디렉터리는 연구자의 **「deck_v6 → deck_v7 최종 수정 지시서」**를 100% 반영하여 완성된 15슬라이드 학술 발표자료 최종 패키지입니다.

---

## 1. 개요 및 사양

- **슬라이드 총수**: 15장
- **권장 발표 시간**: 약 15분 (슬라이드당 55~60초)
- **화면 규격**: 16:9 와이드스크린 (1600x900 반응형 뷰포트)
- **디자인 테마**: Editorial Archive (학술 아카이브 테마 - 와인/틸/아이보리 팔레트, 명조·고딕 타이포그래피)
- **시각 사료 강화**:
  - 실제 표결 공표 문서 크롭 (`A01_vote_clip.png`, `A02_vote_clip.png`)
  - 실제 조직안 수정 조문 (`A02_staff_clip.png`) 및 학칙 개정 신구조문대비표 (`D25_clip.png`)
  - 실제 공론화 권고문 (`D06_recommendation_clip.png`), 숙의단 문서 (`D07_student_clip.png`), 운영규정 (`D08_rule_clip.png`)
  - 현장 고해상도 사진 (`campus_gangneung.jpg`, `campus_dongduk.jpg`, `protest_dongduk_wall.jpg`, `protest_dongduk_stairs.jpg`)
  - 2024.11.21 잠정 중단 합의서 (`D02`) 전문 인용

---

## 2. 파일 구성

```
versions/deck_v7/
├── index.html              # 15슬라이드 독립 실행형 메인 HTML
├── style.css               # Editorial Archive 고유 스타일시트
├── slides.js               # 슬라이드별 발표자 대본 및 예상 Q&A 데이터
├── archive_details.js      # 슬라이드별 아카이브 상세 해설 데이터
├── sources.html            # 1차 사료 앵커 및 서지 상세 페이지
├── deck_v7.pdf             # 고해상도 벡터 15페이지 발표 PDF
├── speaker_script.md       # 슬라이드별 발표 대본 마크다운
└── assets/                 # 사료 캡처 크롭 및 캠퍼스 현장 사진 이미지
```

---

## 3. 키보드 단축키 안내

- `→` / `Space` / `PageDown`: 다음 슬라이드
- `←` / `PageUp`: 이전 슬라이드
- `Home`: 첫 슬라이드 (표지)
- `End`: 마지막 슬라이드 (참고문헌)
- `N`: 발표자 대본 / Q&A 패널 토글
- `D`: 아카이브 상세 사료 해설 패널 토글
- `F`: 전체 화면(Fullscreen) 모드 전환
- `P`: 고해상도 인쇄 및 PDF 저장 모드
