# 대학의 구조적 변화와 위기 커뮤니케이션

강원대–강릉원주대의 2025년 4월 통합안 재심의와 동덕여대의 공학 전환 공론화·후속 의사결정을 비교하는 15분 발표용 HTML 슬라이드 덱이다. 중심 명제는 **공식 결정의 진전과 이해관계자의 수용은 별개의 성과**라는 것이다. 최신 v2는 연구 배경, 사건별 타임라인, 실제 조치, Cameron 상황이론 적용과 반론, 사전 위기관리 평가를 13장으로 구성했다.

- 최신 발표: [`versions/v2/index.html`](versions/v2/index.html)
- 최신 PDF: [`versions/v2/deck_v2.pdf`](versions/v2/deck_v2.pdf)
- 최신 출처 목록: [`versions/v2/sources.html`](versions/v2/sources.html)
- v2 제작 계획: [`PLAN_v2.md`](PLAN_v2.md)
- 버전 기록: [`VERSION_HISTORY.md`](VERSION_HISTORY.md)

v1은 [HTML](versions/v1/index.html)과 [PDF](versions/v1/deck_v1.pdf)로 보존한다.

화살표 키, Page Up/Down, Home/End 또는 화면 오른쪽 위 버튼으로 이동한다. PDF는 슬라이드의 `PDF` 버튼에서 내려받을 수 있다.

## 근거와 재생성

차트는 앞서 수집한 원자료의 수치만 사용한다. 원자료 ID와 발행 정보는 출처 목록에 표시했다. 대학평의원회 두 표결의 차이는 개인별 입장 변경으로 해석하지 않는다. 공론화 설문의 전체 비율은 집단에 동일한 가중치를 준 값이며, 학생 총투표와는 질문·시점·모집단이 다르다.

Windows에서 `python scripts/generate_sources_v2.py`, `python scripts/verify_deck_v2.py` 순서로 실행하면 v2 출처 목록과 PDF를 재생성하고 13장 화면 검사를 수행한다. v2 차트는 v1의 원자료 수치로 만든 SVG를 보존해 사용했다. v1은 `python scripts/generate_charts.py`, `python scripts/generate_sources.py`, `python scripts/verify_deck.py` 순서로 재생성한다. 스크립트는 원래의 로컬 연구 폴더 및 설치된 Chrome과 Python 패키지(Matplotlib, Playwright, Pillow, PyMuPDF)를 사용한다. 공개 저장소에는 원자료의 로컬 경로나 전문을 포함하지 않았다.

## 범위

이 발표의 ‘성공’은 강원대의 수정안 재심의 가결과 동덕여대의 공식 의사결정 절차 진전을 가리킨다. ‘실패’ 또는 한계는 각각 가결 직후 직원 반발의 지속과 학생대표의 수용 미확보 범위에서만 논한다. 강원대 본부가 설명한 전략실 인력 변경은 실제 배치 완료와 구별한다. 전체 구성원의 장기 수용이나 2029년 공학 전환 시행 결과를 판정하지 않는다.
