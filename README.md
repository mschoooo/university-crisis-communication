## 최신 발표자료: deck_v20

- [슬라이드 보기](versions/deck_v20/index.html)
- [PDF 다운로드](versions/deck_v20/deck_v20.pdf)
- [출처 목록](versions/deck_v20/sources.html)
- [발표자 노트](versions/deck_v20/deck_v20_발표자노트.md)

# 변화의 결단은 왜 위기가 되는가

부산대학교 미디어커뮤니케이션학과 **위기관리(029) 중간고사 대체 과제** 발표용 HTML 슬라이드 덱이다(발표자: **조민성**, 학번 **202206251**). 최신 `deck_v19`는 Cameron 정황적 수용 이론을 중심으로 부산대–부산교대 통합과 동덕여대 남녀공학 전환을 비교한다. Benoit의 이미지 회복 전략은 한 장에서 보조적으로 평가한다.

- **최신 발표(deck_v19)**: [`versions/deck_v19/index.html`](versions/deck_v19/index.html)
- **최신 인쇄용 PDF(deck_v19)**: [`versions/deck_v19/deck_v19.pdf`](versions/deck_v19/deck_v19.pdf)
- **발표자 노트·출처 색인·시각자료 크레딧**: [`versions/deck_v19/README.md`](versions/deck_v19/README.md)
- **구성·시간 계획**: [`PLAN_v19.md`](PLAN_v19.md)
- **이전 발표본(deck_v5)**: [`versions/deck_v5/index.html`](versions/deck_v5/index.html)
- **이전 발표본(deck_v4)**: [`versions/deck_v4/index.html`](versions/deck_v4/index.html)
- **이전 사실관계 검증본(v4)**: [`versions/v4/index.html`](versions/v4/index.html)
- **v4 원문 검증·변경 로그**: [`versions/v4/검증_변경로그.md`](versions/v4/검증_변경로그.md)
- **버전 기록**: [`VERSION_HISTORY.md`](VERSION_HISTORY.md)

이전 버전은 불변(immutable) 아카이브 원칙에 따라 그대로 보존한다:
- **v3 보존본**: [HTML](versions/v3/index.html) · [PDF](versions/v3/deck_v3.pdf) · [출처](versions/v3/sources.html)
- **v2 보존본**: [HTML](versions/v2/index.html) · [PDF](versions/v2/deck_v2.pdf) · [출처](versions/v2/sources.html)
- **v1 보존본**: [HTML](versions/v1/index.html) · [PDF](versions/v1/deck_v1.pdf) · [출처](versions/v1/sources.html)

## 발표 조작 및 단축키 (deck_v4)

- `←` / `→`, `PageUp` / `PageDown`, `Home` / `End`: 슬라이드 이동
- `M` 또는 하단 `목차(M)` 버튼: 15장 전체 슬라이드 목차 점프 모달
- `N` 또는 하단 `발표노트(N)` 버튼: 슬라이드별 발표 대본 및 교수님 예상 질문(Q&A) 방어 논리 드로어
- `D` 또는 하단 `수치검증(D)` 버튼: 1차 원자료 핵심 수치(강원대 회의록·동덕여대 가중/무가중 통계) 요약 모달
- `F` 또는 하단 `전체화면(F)` 버튼: 전체화면 전환

## 검증 및 재생성

Windows에서 다음 순서로 실행하면 `deck_v4`의 15장 화면을 렌더링하고 16:9 PDF를 생성·검증한다. 자료 ID와 원문 링크는 `versions/deck_v4/sources.html`에서 확인할 수 있다:

```powershell
python scripts/render_editorial_deck.py --pdf
python scripts/verify_editorial_pdf.py
```
