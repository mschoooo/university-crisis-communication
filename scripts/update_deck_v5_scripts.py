import json
from pathlib import Path

deck_dir = Path("대학통합_위기커뮤니케이션_연구/07_HTML_발표덱/versions/deck_v5")

speaker_notes = [
  {
    "title": "Slide 01 · 표지 및 핵심 문제의식",
    "script": "안녕하십니까. 위기관리(029) 중간고사 대체 과제를 발표하는 미디어커뮤니케이션학과 조민성(202206251)입니다. 오늘날 학령인구 급감 속에서 대학 본부의 구조개혁 결단은 생존을 위한 필수 전략이지만, 내부 구성원들에게는 직무와 정체성을 뒤흔드는 파괴적 위기로 작동합니다. 본 발표는 강원대–강릉원주대의 국립대 통합과 동덕여대의 남녀공학 전환 추진 사례를 비교합니다. 두 대학 모두 대학평의원회 의결과 학칙 개정이라는 ‘공식 결정의 진전’을 이뤄냈지만, 한 대학은 부분적 인력 조정을 통해 제도적 출범을 안착시킨 반면, 다른 대학은 학생들의 85.7% 총투표 반대와 극단적 불신에 직면했습니다. 왜 공식 결정의 통과가 곧바로 구성원의 수용으로 이어지지 못하는가? 카메론 연구진의 정황적 수용 이론(Contingency Theory)과 절차적 공정성 이론을 통해 조직의 전략적 선택을 결정한 상황변수의 조합을 심층 논증하겠습니다.",
    "qa": "[교수님 예상 질문 포인트] 연구의 독창성: 단순 사건 나열이 아니라 정황적 수용 이론(Cancel et al., 1999; Cameron et al., 2001; 황성욱, 2014)과 절차적 공정성(Leventhal; Tyler; Główczewski & Burdziej, 2023)을 결합해 '공식 결정의 진전'과 '내부 공중의 수용'을 분리 평가한 점이 핵심입니다."
  },
  {
    "title": "Slide 02 · 문제제기 및 비교 연구 설계",
    "script": "연구 설계를 말씀드리겠습니다. 강원대는 5년간 국비·지방비 2,150억 원이 연계된 글로컬대학30 사업의 일환으로 통합을 추진했습니다. 2월 20일 교육부 선제출 논란 속에 4월 1일 평의원회에서 8:12로 부결되었으나, 27일 만에 수정안이 15:6으로 가결되었습니다. 동덕여대는 학령인구 감소에 대응한 VISION 2040의 일환으로 공학 전환을 검토하다 2024년 11월 소문 유출과 본관 점거로 폭발했습니다. 11월 21일 잠정 중단 합의 후, 2025년 6개월간 4단위 공론화위원회를 거쳐 2026년 평의원회에서 학칙을 개정했으나, 학생 총투표에서 85.7% 반대가 확인되었습니다. 본 연구는 양 대학의 공식 회의록, 공론화 설문 원자료, 개정 학칙 및 대학언론 보도 등 전수 확보된 1차 사료를 바탕으로 과정 추적(Process Tracing)을 수행했습니다.",
    "qa": "[교수님 예상 질문 포인트] 두 사례 비교 가능성: 국립대 통합과 사립 여대 공학 전환이라는 구조적 차이 자체가 정황적 수용 이론의 '사전성향적 변인(Predisposing Variables)' 차이와 가분적 실리 vs 비가분적 정체성 쟁점의 차이를 검증하는 최적의 준실험적 비교 조건을 제공합니다."
  },
  {
    "title": "Slide 03 · 이론적 분석 틀 ①: 정황적 수용 이론 (81개 변수와 3분법)",
    "script": "본 연구의 이론적 기둥인 정황적 수용 이론을 재검토하겠습니다. 교재에는 외부 24개, 내부 57개로 총 81개의 변수가 제시되어 있습니다. 그러나 카메론 연구진의 1999년 실증 연구에 따르면, 모든 변수가 동일하게 작동하는 것은 아닙니다. 본 연구는 이를 세 가지 기능적 층위로 범주화했습니다. 첫째, 갈등 이전의 기저 입장을 좌우하는 '사전성향적 변수', 둘째, 위기 국면에서 입장을 실제로 밀고 당기는 '상황변수(긴급성·위협·공중의 권력)', 셋째, 타협하고 싶어도 타협할 수 없게 만드는 '수용 제한 요인(상충하는 공중·도덕적 정체성)'입니다. 특히 주의할 점은, 원전이 상정한 기업의 외부 공중과 달리, 대학의 교수·직원·학생은 고등교육법상 대학평의원회의 법정 의결권을 지닌 내부 주권자라는 점입니다. 따라서 원전의 변수를 기계적으로 적용하지 않고, 대학의 특수한 거버넌스 맥락을 반영해 분석을 진행했습니다.",
    "qa": "[교수님 예상 질문 포인트] 개념적 한계 검토: 기업의 외부 공중 모델을 대학 내부 구성원에게 적용할 때의 한계(평의원회의 법정 거부권, 학생의 불이탈성 및 창학정신 수호 의식)를 명확히 고지하여 학술적 엄밀성을 확보했습니다."
  },
  {
    "title": "Slide 04 · 이론적 분석 틀 ②: 갈등관리 생애주기와 3대 평가 축",
    "script": "갈등관리 생애주기 관점에서 위기관리는 위기 폭발 이후의 대응에만 머물지 않습니다. Heath가 강조한 사전 지형 정찰, Sturges가 규명한 의견 고착화 이전의 선제 정보 제공, 그리고 Marra가 지적한 조직 소통 문화가 유기적으로 작동해야 합니다. 나아가 본 발표는 위기관리 성패를 단일한 성공·실패로 재단하지 않습니다. 대학 본부가 안건을 통과시켰다고 해서 갈등관리가 성공한 것은 아닙니다. ① 공식 결정의 제도적 진전, ② 구성원 핵심 요구의 실질적 반영, ③ 결정 이후 구성원의 사후 수용과 대외 평판이라는 3대 평가 축을 통해 두 대학의 대응을 입체적으로 해부하겠습니다.",
    "qa": "[교수님 예상 질문 포인트] 왜 3대 평가 축인가? 대학 본부 관점(안건 가결)과 PR/갈등관리 관점(공중의 수용과 신뢰 회복)의 괴리를 포착하여 반응적(Reactive) 단계와 회복(Recovery) 단계를 독립적으로 진단하기 위함입니다."
  },
  {
    "title": "Slide 05 · 사례 A (강원대) 2,150억 사업비 압박 속 ‘선제출·후통보’와 8:12 부결",
    "script": "강원대 사례를 살펴보겠습니다. 2024년 7월 글로컬위원회는 통합이 지연될 경우 사업비 50% 삭감과 협약 해지를 공식 경고했습니다. 2,150억 원이라는 막대한 재정 위협 속에서 본부는 극단적인 옹호 입장을 취하며 대외 협상 보안을 이유로 2월 20일 교육부에 신청서를 먼저 제출했습니다. 그리고 2월 28일 평의원회 당일에야 257쪽 문서를 배부했습니다. 이 '선제출·후통보'는 Sturges가 경고한 치명적인 전조 단계 실패였습니다. 평의원들에게 '패싱' 인식이 확고히 고착화된 것입니다. 결국 4월 1일 제47차 평의원회에서 본부가 40쪽 요약표를 내밀며 조건부 가결을 읍소했으나, 공무원 35명 차출이라는 원안이 수정되지 않았다는 이유로 8 대 12로 전격 부결되었습니다.",
    "qa": "[교수님 예상 질문 포인트] Sturges(1994) 적용: 공식 심의 전 '선제출 후통보'로 밀실 프레임이 고착화되어, 본문 수정 없는 구두 약속만으로는 이미 굳어진 반대 여론을 돌릴 수 없었습니다."
  },
  {
    "title": "Slide 06 · 사례 A (강원대) 인력안 조정(35→24명)과 당일 수정안 제한 (15:6 가결)",
    "script": "4월 1일 부결 이후 27일간 강원대 본부는 무엇을 바꿨고 무엇을 밀어붙였을까요? 본부는 핵심 쟁점이었던 대학혁신전략실 공무원 차출을 35명에서 24명으로 줄이고, 부족한 11명은 외부 계약직 전문가로 채워 춘천 인력 11명을 잔류시키는 실질적인 수정안을 성안했습니다. 이는 분명한 ‘행동적 수용’의 조치였습니다. 하지만 동시에 강력한 옹호가 유지되었습니다. 4월 28일 제48차 회의에서 한 평의원이 추가 수정을 제안하려 하자, 의장은 ‘추가 수정 시 28일 이상 지연되어 사업이 무산된다’며 당일 수정안 상정을 전격 불허했습니다. 결국 15:6으로 가결되었으나, 직원들은 본문 명칭 왜곡을 규탄하며 회의장 밖에서 피켓 시위를 벌였습니다.",
    "qa": "[교수님 예상 질문 포인트] 표결 모수 주의: 4월 1일은 20명 투표(8:12), 4월 28일은 21명 투표(15:6)로 출석 모수가 다르며, 무기명 표결이므로 개별 위원의 표 이동이 아닌 '회의체 전체 표결 결과의 변화'로 해석합니다."
  },
  {
    "title": "Slide 07 · 사례 A (강원대) 다중 조건의 결합과 ‘부분적 행동 수용’",
    "script": "강원대의 대응을 이론적으로 해부하면, 세 가지 조건의 결합이 드러납니다. 첫째, 글로컬 2,150억 원과 5월 말 대교협 대입전형 마감이라는 '극도의 외적 긴급성'이 존재했습니다. 둘째, 상대 공중인 대학평의원회가 법정 의결 거부권을 실제로 행사해 안건을 부결시켰습니다. 셋째, 가장 결정적인 것은 갈등의 쟁점이 '공무원 35명 차출'이라는 쪼갤 수 있는(Divisible) 가분적 수치 쟁점이었다는 점입니다. 즉, 외적 위협과 법정 권력이 본부를 압박했을 때, 가분적 쟁점이 존재했기에 본부는 35명을 24명으로 깎아주는 부분적 행동 수용을 통해 15:6 가결이라는 제도적 돌파구를 열 수 있었습니다. 그러나 당일 수정 차단과 본문 왜곡 논란으로 인해 직원들의 수복이라는 회복 단계 과제는 미완으로 남았습니다.",
    "qa": "[교수님 예상 질문 포인트] 다중 조건의 조합(Configural causality): 단일 변수가 아니라 [긴급성] × [법정 거부권] × [가분적 쟁점]의 결합이 부분적 행동 수용을 촉발한 동력이었음을 증명합니다."
  },
  {
    "title": "Slide 08 · 사례 B (동덕여대) 전조 단계 ‘의견 고착화’와 공론화 이행 (2024~2025)",
    "script": "동덕여대 사례로 넘어가겠습니다. 동덕여대의 위기는 전조 단계의 완벽한 실패에서 촉발되었습니다. 대학본부 일지(D26)에 따르면, 11월 5일 비전혁신추진단에서 단과대 공학 전환이 동의되었고 본부는 12일 교무위 보고 후 설명하려 했습니다. 그러나 7일 학내 커뮤니티로 소문이 유출되었고, 11일 면담이 전격 취소되면서 본관 점거로 폭발했습니다. 단 4일 만에 학생들에게 '밀실 추진' 프레임이 고착화된 것입니다. 본부는 11월 21일 총학 면담 끝에 '공학 논의 잠정 중단'을 합의하며 일시 후퇴했습니다. 이후 겨울철 법적 공방을 거쳐, 2025년 5월 비대위와 상생협약을 맺고 교원·학생·직원·동문 각 3인씩 4단위 동수로 구성된 공론화위원회를 출범시키며 제도적 숙의 국면으로 전환했습니다.",
    "qa": "[교수님 예상 질문 포인트] 11/21 잠정 중단 합의(D02)의 의미: 사태 초기 극단적 폭력 충돌 속에서 일시적인 전술적 후퇴를 취한 것이며, 2025년 공론화위 출범으로 이어지는 징검다리 역할을 했습니다."
  },
  {
    "title": "Slide 09 · 사례 B (동덕여대) 공론화 분석: 숙의의 숫자와 집계 방식의 충돌",
    "script": "동덕여대 공론화 과정에서는 매우 흥미로운 두 가지 발견이 나타납니다. 첫째, 48명이 참여한 소규모 숙의기구에서는 학생단의 여대 유지 응답이 80%에서 50%로 완화되었고, 수용 의향도 83.2%에 달했습니다. 숙의의 가능성을 보여준 대목입니다. 그러나 둘째, 3,176명이 참여한 대규모 설문 집계에서 치명적인 규칙 충돌이 발생했습니다. 교원·직원·학생을 1:1:1로 동일 가중하면 공학 찬성이 51.8%로 과반이지만, 무가중 단순합산을 하면 여대 유지가 66.1%로 압도적이었습니다. 전체 응답자의 91%를 차지하는 학생의 표가 1/23로 축소된 것입니다. 공론화위는 8월에 합의한 2/3 다결 규칙에 따라 학생위원의 반대에도 불구하고 12월 2일 9 대 2 대 1로 공학 전환 권고안을 가결했습니다.",
    "qa": "[교수님 예상 질문 포인트] 4차 회의 의결 규칙 작동: 11월 26일 보류는 파행이 아니라, '한 단위 전원 반대 시 차기 회의로 보류하고 2/3 찬성으로 가결'한다는 사전 합의 규칙이 작동한 결과였습니다(D08 19쪽)."
  },
  {
    "title": "Slide 10 · 사례 B (동덕여대) 조기 발표와 학칙 관철, 그리고 재점화된 불신",
    "script": "권고안이 나오자마자 위기는 다시 폭발했습니다. 학생 총투표가 시작된 바로 그 첫날인 12월 3일, 총장이 권고안 수용과 2029년 공학 전환 방침을 전격 발표했습니다. 이에 반발한 학생 총투표에서는 85.7%라는 압도적 반대가 표출되었습니다. 이어 2026년 1월 12일 대학평의원회에서 학칙 개정안이 8 대 2로 가결되었으나, 학생위원 2명은 서명을 거부했고, 본부가 비밀유지 공문을 보낸 사실이 알려지며 불신은 극에 달했습니다. 결국 2월 26일 학칙이 공포되어 제도적으로는 공학 전환이 관철되었습니다. 한편 2026학년도 입시 지원자가 32.9% 급감했으나, 수시는 9월에 접수되었으므로 12월 발표와의 직접적 인과관계는 확인할 수 없습니다.",
    "qa": "[교수님 예상 질문 포인트] 입시 지원자 32.9% 감소의 해석: 학령인구 변화나 입시 구조 요인을 통제하지 않은 기술통계이므로 공학전환 갈등의 '단일 인과 결과'로 단정하지 않고, 외부 지원 동향을 살펴볼 참고 지표로만 제시합니다."
  },
  {
    "title": "Slide 11 · 사례 B (동덕여대) 수용 제한 요인과 ‘수사 혼합적 수용’의 한계",
    "script": "동덕여대 본부의 선택을 이론적으로 규명하면 세 가지 수용 제한 요인이 드러납니다. 첫째, 교원·직원(찬성 70%대)과 학생(반대 71%)이 정면 대립하는 '상충하는 복수 공중'에 갇혀 있었습니다. 한쪽을 들어주면 다른 쪽을 배제해야 했습니다. 둘째, 강원대의 정원 문제와 달리 '여대 유지냐 공학 전환이냐'는 쪼갤 수 없는 비가분적 정체성 쟁점이었습니다. 셋째, 평의원회 10석 중 2석에 불과해 학생에게는 법정 거부권이 없었습니다. 결국 본부는 4단위 공론화위원회와 2029년 이행 유예라는 '수사적·절차적 수용'을 제공하는 대신, 1:1:1 가중치와 8:2 표결로 실질적 전환 결론을 옹호 관철했습니다. 제도는 통과시켰으나 학내 신뢰를 영구적으로 잃어버린 수사 혼합적 수용의 한계를 보여줍니다.",
    "qa": "[교수님 예상 질문 포인트] 학교 측 반론의 균형 반영: 고등교육법상 대학평의원회도 특정 단위 과반을 금지하므로 1:1:1 가중이 법 취지에 부합한다는 본부 입장과, 재학생 졸업 시점(2029년) 유예가 실질적 배려였다는 점도 함께 명시했습니다."
  },
  {
    "title": "Slide 12 · 종합 비교: 5대 쟁점별·시점별 옹호–수용 매트릭스",
    "script": "두 사례의 직접 비교입니다. 본 연구는 '강원대=행동 수용, 동덕여대=수사 수용'이라는 단순 이분법을 기각합니다. 5대 쟁점 매트릭스를 보시면, 두 대학 모두 ‘통합 승인’과 ‘공학 전환’이라는 핵심 정책 목표는 1.0의 순수 옹호로 끝까지 밀어붙였습니다. 차이는 무엇을 양보 매개체로 삼았는가입니다. 강원대는 조직·인력 쟁점에서 공무원 정원을 35명에서 24명으로 줄이는 '행동적 수용'을 택했고, 동덕여대는 정체성 자체는 양보하지 못하는 대신 시행 시기를 재학생 졸업 후인 2029년으로 3년 늦추는 '시간적 수용'을 제공했습니다. 즉, 조직의 입장은 단일하지 않으며, 상황변수가 허용하는 타협의 여지에 따라 쟁점별로 다르게 분화된다는 것이 정황 이론의 정교한 설명력입니다.",
    "qa": "[교수님 예상 질문 포인트] 이분법 기각 논리: 강원대 역시 통합 목표 100% 옹호 및 당일 수정안 배제가 존재했고, 동덕여대 역시 2029년 유예라는 실질적 시간 양보가 존재했음을 5대 쟁점으로 실증했습니다."
  },
  {
    "title": "Slide 13 · 사전 위기관리 진단: 징후 탐지와 커뮤니케이션 타이밍",
    "script": "그렇다면 두 대학은 왜 사전에 위기를 막지 못했을까요? Heath의 관점에서 보면, 두 대학 모두 외부 환경 스캐닝에는 능했으나 내부 지형 정찰(Scouting the terrain)에 실패했습니다. 강원대는 춘천 직원의 인력 유출 공포를, 동덕여대는 학생들의 정체성 상실감을 사전 위험 이슈로 분류하지 않았습니다. 더 치명적인 것은 Sturges가 강조한 '커뮤니케이션 타이밍'이었습니다. 강원대는 교육부 선제출 후에 문서를 줬고, 동덕여대는 비공식 소문이 학내에 퍼진 뒤 면담을 취소했습니다. 공식 정보가 늦어지면 비공식 루머가 진실의 자리를 차지하며 반대 의견이 단단하게 굳어집니다. 의견이 고착화된 이후의 사후 해명은 천문학적인 갈등 비용을 초래함을 보여줍니다.",
    "qa": "[교수님 예상 질문 포인트] 2~6주차 수업 이론의 실천적 연결: Heath(1997) 지형 정찰, Sturges(1994) 의견 고착화 시점, Jaques(2007) 비선형 모델을 두 대학의 실제 실패 지점에 정밀 타격했습니다."
  },
  {
    "title": "Slide 14 · 절차적 공정성 평가: 규칙의 일관성과 정당성",
    "script": "절차적 공정성 이론으로 두 대학의 회의와 투표 규칙을 평가해 보겠습니다. Tyler의 관계적 모델에 따르면, 사람들은 단순히 말할 기회인 발언권(Voice)만으로는 만족하지 않으며, 자신의 발언이 결정에 반영된다는 결정 통제권(Decision Control)을 느낄 때 정당성을 인정합니다. 동덕여대는 공론화라는 방대한 발언의 장을 열었으나, 1:1:1 가중치 규칙과 8:2 평의원회 표결로 학생의 결정을 무력화했습니다. Główczewski & Burdziej(2023)의 최신 연구가 실증하듯, 절차가 불공정하다고 인식될 때 학생들의 대학에 대한 동일시는 무너집니다. 강원대 역시 4월 28일 회의에서 의장이 28일 지연을 이유로 당일 수정동의안을 원천 차단하고 명칭 불일치를 낳음으로써 절차적 일관성의 흠결을 남겼습니다.",
    "qa": "[교수님 예상 질문 포인트] 절차 공정성과 합법성의 구분: 법률상 요건을 채웠다고 해서(합법성) 구성원이 그 결정을 공정하다고 인정(정당성)하는 것은 아니며, Voice와 Decision Control의 괴리가 불복종을 낳습니다."
  },
  {
    "title": "Slide 15 · 결론: 공식 결정을 구성원의 수용으로 잇는 3대 조건",
    "script": "결론을 맺겠습니다. 본 연구는 대학 구조개혁 위기관리에서 공식 결정을 구성원의 수용으로 잇기 위한 세 가지 원칙을 제시합니다. 첫째, 시점의 법칙입니다. 소문이 퍼지기 전 복수 대안을 선공개해야 합니다. 둘째, 규칙의 법칙입니다. 집단 간 표본 크기가 다를 때는 가중치 단일 발표가 아니라 무가중 단순합산을 동등하게 병기하여 절차적 공정성을 확보해야 합니다. 셋째, 행동의 법칙입니다. 수사적 위원회 개설을 넘어, 강원대처럼 실제 자원과 인력을 조정하는 행동적 양보가 수반되어야 합니다. 거버넌스 위기관리의 진정한 성패는 회의실 안에서의 표결 가결이 아니라, 회의실 밖 구성원들의 신뢰를 얻는 데 있습니다. 경청해 주셔서 감사합니다.",
    "qa": "[자료 확인] P99·P01·H14·LEV·TYL·R4는 정황적 수용 및 절차 공정성의 핵심 문헌입니다. A01P·A02P, D06–D08, D10·D14·D15는 출처 인덱스에서 개별 확인할 수 있습니다."
  }
]

# Write slides.js
slides_js_content = f"""const slides = Array.from(document.querySelectorAll('.slide'));
const stage = document.getElementById('stage');
const count = document.getElementById('count');
const notesDrawer = document.getElementById('notes-drawer');
const notesTitle = document.getElementById('notes-title');
const notesBody = document.getElementById('notes-body');
const notesQa = document.getElementById('notes-qa');
const tocModal = document.getElementById('toc-modal');
const dataModal = document.getElementById('data-modal');
let index = 0;

const motionPlan = [
  ['.case-plate p b, .vote-row > b, .staff-change strong, .before-after strong, .survey-side strong, .aftermath-card strong', 'number'],
  ['.vote-track i, .compare-line i', 'bar'],
  ['.timeline > div, .dongduk-timeline > div, .vote-row, .before-after > div, .survey-side > div, .aftermath-card, .compare-rows > div, .reference-column p, .conclusion-list > div', 'row']
];
slides.forEach(slide => {{
  motionPlan.forEach(([selector, type]) => {{
    slide.querySelectorAll(selector).forEach(element => element.dataset.motion = type);
  }});
  slide.querySelectorAll('[data-motion]').forEach((element, order) => {{
    element.style.setProperty('--motion-delay', `${{Math.min(order * 85, 510)}}ms`);
  }});
}});

const SPEAKER_NOTES = {json.dumps(speaker_notes, ensure_ascii=False, indent=2)};

function fitStage() {{
  const scale = Math.min(window.innerWidth / 1600, window.innerHeight / 900);
  stage.style.transform = `scale(${{scale}})`;
  stage.style.transformOrigin = 'center center';
}}

function updateNotes() {{
  const item = SPEAKER_NOTES[index] || {{ title: "", script: "", qa: "" }};
  const heading = slides[index].querySelector('h1, h2');
  if (notesTitle) notesTitle.textContent = `Slide ${{String(index + 1).padStart(2, '0')}} · ${{heading ? heading.textContent.trim().replace(/\\s+/g, ' ') : item.title}}`;
  if (notesBody) notesBody.textContent = item.script;
  if (notesQa) notesQa.textContent = item.qa;
  const detail = document.getElementById("notes-detail");
  if (detail) detail.textContent = (window.ARCHIVE_DETAILS || [])[index] || "";
}}

function show(next) {{
  index = (next + slides.length) % slides.length;
  slides.forEach((slide, i) => slide.classList.toggle('active', i === index));
  const current = slides[index];
  current.classList.remove('motion-in');
  void current.offsetWidth;
  if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) current.classList.add('motion-in');
  count.textContent = `${{index + 1}} / ${{slides.length}}`;
  history.replaceState(null, '', `#${{index + 1}}`);
  updateNotes();
}}

function togglePanel(panel) {{
  const isOpen = panel.classList.contains('open');
  [notesDrawer, tocModal, dataModal].forEach(p => p && p.classList.remove('open'));
  if (!isOpen && panel) panel.classList.add('open');
}}

document.getElementById('prev').addEventListener('click', () => show(index - 1));
document.getElementById('next').addEventListener('click', () => show(index + 1));
document.getElementById('btn-notes').addEventListener('click', () => togglePanel(notesDrawer));
document.getElementById('btn-toc').addEventListener('click', () => togglePanel(tocModal));
document.getElementById('btn-data').addEventListener('click', () => togglePanel(dataModal));
document.getElementById('btn-fs').addEventListener('click', () => {{
  if (!document.fullscreenElement) document.documentElement.requestFullscreen().catch(() => {{}});
  else document.exitFullscreen().catch(() => {{}});
}});

document.querySelectorAll('.close-btn').forEach(btn => {{
  btn.addEventListener('click', () => {{
    [notesDrawer, tocModal, dataModal].forEach(p => p && p.classList.remove('open'));
  }});
}});

document.querySelectorAll('.toc-item').forEach(btn => {{
  btn.addEventListener('click', () => {{
    const target = Number(btn.getAttribute('data-slide') || '1') - 1;
    show(target);
    tocModal.classList.remove('open');
  }});
}});

window.addEventListener('keydown', (event) => {{
  if (['ArrowRight', 'PageDown', ' '].includes(event.key)) {{
    event.preventDefault();
    show(index + 1);
  }} else if (['ArrowLeft', 'PageUp'].includes(event.key)) {{
    event.preventDefault();
    show(index - 1);
  }} else if (event.key === 'Home') {{
    event.preventDefault();
    show(0);
  }} else if (event.key === 'End') {{
    event.preventDefault();
    show(slides.length - 1);
  }} else if (event.key === 'n' || event.key === 'N') {{
    event.preventDefault();
    togglePanel(notesDrawer);
  }} else if (event.key === 'm' || event.key === 'M') {{
    event.preventDefault();
    togglePanel(tocModal);
  }} else if (event.key === 'd' || event.key === 'D') {{
    event.preventDefault();
    togglePanel(dataModal);
  }} else if (event.key === 'f' || event.key === 'F') {{
    event.preventDefault();
    document.getElementById('btn-fs').click();
  }} else if (event.key === 'Escape') {{
    [notesDrawer, tocModal, dataModal].forEach(p => p && p.classList.remove('open'));
  }}
}});

window.addEventListener('resize', fitStage);
window.addEventListener('hashchange', () => {{
  const target = Number(location.hash.replace('#', ''));
  if (Number.isInteger(target) && target >= 1 && target <= slides.length && target - 1 !== index) {{
    show(target - 1);
  }}
}});
fitStage();
const initial = Number(location.hash.replace('#', ''));
show(Number.isFinite(initial) && initial >= 1 && initial <= slides.length ? initial - 1 : 0);
"""

(deck_dir / "slides.js").write_text(slides_js_content, encoding="utf-8")
print("slides.js written successfully.")
