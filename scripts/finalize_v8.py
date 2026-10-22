"""Align v8 supplementary text with the checked primary records."""
from pathlib import Path

root = Path(__file__).resolve().parents[1] / "versions" / "deck_v8"

def replace(name, old, new):
    path = root / name
    text = path.read_text(encoding="utf-8")
    if old not in text:
        raise ValueError(f"Missing text in {name}: {old}")
    path.write_text(text.replace(old, new), encoding="utf-8")

replace("index.html", "심의 전 교육부 선제출과 당일 배부", "심의 전 교육부 선제출과 검토 시간 부족")
replace("slides.js", "257쪽 당일 배부", "257쪽 이틀 전 송부")
replace("slides.js", "동덕여대 소통 일지(D26), 합의문(D02)", "동덕여대 소통 일지(D26), 잠정 중단 합의 보도(D02)")
replace("slides.js", "등 1차 사료를 엄밀하게 대조했습니다", "등 공식 사료와 보도를 구분하여 대조했습니다")
replace("archive_details.js", "257쪽 당일 배부", "257쪽 이틀 전 송부")
replace("archive_details.js", "deck_v7_참고문헌.md", "deck_v8_참고문헌.md")
replace("archive_details.js", "- Cancel et al. (1997) P97", "- Benoit (1997) BEN · Cancel et al. (1997) P97")
replace("deck_v8_참고문헌.md", "# deck_v7 참고문헌", "# deck_v8 참고문헌")
replace("deck_v8_참고문헌.md", "제46차 대학평의원회 회의록 (당일 배부 문제제기)", "제46차 대학평의원회 회의록 (이틀 전 자료 송부 문제제기)")
replace("deck_v8_참고문헌.md", "남녀공학 전환 논의 잠정 중단 및 수업 재개 합의서 | 동덕여자대학교 처장단 - 총학생회", "남녀공학 전환 논의 잠정 중단 및 수업 재개 합의 보도 | 연합뉴스")
print("Supplementary text aligned")
