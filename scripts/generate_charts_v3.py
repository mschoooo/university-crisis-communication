"""Produce the four evidence and theoretical charts for the v3 HTML deck.

All numbers are verified from local primary sources:
- A03P (2025-02-28), A01P p.40 (2025-04-01), A02P pp.6-10, 44 (2025-04-28), A04
- D07 pp.1, 3, 4, 17; D08 pp.8, 19, 22
- D10 (2025-12-09), D14 (2026-01-27), D15 (2026-01-13)
"""

from pathlib import Path
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyBboxPatch


OUT = Path(__file__).resolve().parents[1] / "versions" / "v3" / "assets"
OUT.mkdir(parents=True, exist_ok=True)

font_path = Path(r"C:\Windows\Fonts\NotoSansKR-VF.ttf")
font_manager.fontManager.addfont(str(font_path))
font_name = font_manager.FontProperties(fname=str(font_path)).get_name()
plt.rcParams.update(
    {
        "font.family": font_name,
        "font.size": 15,
        "svg.fonttype": "none",
        "axes.unicode_minus": False,
    }
)

INK = "#132934"
TEAL = "#136f6d"
TEAL_LIGHT = "#3a9694"
RED = "#b8443e"
AMBER = "#c47d2b"
SLATE = "#5c6d75"
MUTED = "#8e9a9d"
BG = "#f7f5ef"
CARD_BG = "#efeae0"
BORDER = "#c9c3b8"


def new_canvas(width=12.6, height=4.2):
    fig, ax = plt.subplots(figsize=(width, height), dpi=144)
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.tick_params(axis="both", length=0, colors=INK)
    return fig, ax


# ---------------------------------------------------------------------------
# 1. kangwon_votes.svg: Senate Roll Calls (4/1 vs 4/28) + Staff Reallocation
# ---------------------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(
    1, 2, figsize=(13.2, 3.6), dpi=144, gridspec_kw={"width_ratios": [1.35, 1.0], "wspace": 0.28}
)
fig.patch.set_facecolor(BG)
for ax in (ax1, ax2):
    ax.set_facecolor(BG)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.tick_params(axis="both", length=0, colors=INK)

ax1.set_title("① 대학평의원회 표결 변화 (A01P·A02P)", loc="left", fontsize=16, fontweight="bold", color=INK, pad=12)
rows = [
    ("4월 1일 제47차 (부결)", 8, 12, 20, "찬성 40.0%"),
    ("4월 28일 제48차 (가결)", 15, 6, 21, "찬성 71.4%"),
]
for y, (label, yes, no, total, pct_txt) in zip([1, 0], rows):
    ax1.barh(y, yes, height=0.46, color=TEAL)
    ax1.barh(y, no, left=yes, height=0.46, color=RED)
    ax1.text(yes / 2, y, f"찬성 {yes}표", ha="center", va="center", color="white", weight="bold", fontsize=14.5)
    ax1.text(yes + no / 2, y, f"반대 {no}표", ha="center", va="center", color="white", weight="bold", fontsize=14.5)
    ax1.text(total + 0.4, y, f"총 {total}명 ({pct_txt})", ha="left", va="center", color=INK, weight="bold", fontsize=13.5)

ax1.set_yticks([1, 0], [r[0] for r in rows], fontsize=14.5, fontweight="bold", color=INK)
ax1.set_xticks([])
ax1.set_xlim(0, 29.5)
ax1.set_ylim(-0.55, 1.55)

ax2.set_title("② 핵심 쟁점: 대학혁신전략실 35명 구성 조정 (A02P·A04)", loc="left", fontsize=16, fontweight="bold", color=INK, pad=12)
staff_rows = [
    ("4월 1일 원안", 35, 0, "전원 공무원 35명 차출"),
    ("4월 28일 수정안", 24, 11, "춘천 기존 인력 11명 잔류"),
]
for y, (label, civil, ext, note) in zip([1, 0], staff_rows):
    ax2.barh(y, civil, height=0.46, color=SLATE if y == 1 else TEAL)
    if ext > 0:
        ax2.barh(y, ext, left=civil, height=0.46, color=AMBER)
        ax2.text(civil / 2, y, f"공무원 {civil}명", ha="center", va="center", color="white", weight="bold", fontsize=13.5)
        ax2.text(civil + ext / 2, y, f"외부 {ext}명", ha="center", va="center", color="white", weight="bold", fontsize=13.5)
    else:
        ax2.text(civil / 2, y, f"공무원 {civil}명 (춘천·강릉 차출)", ha="center", va="center", color="white", weight="bold", fontsize=13.5)
    ax2.text(35.8, y, note, ha="left", va="center", color=INK, fontsize=13)

ax2.set_yticks([1, 0], [r[0] for r in staff_rows], fontsize=14.5, fontweight="bold", color=INK)
ax2.set_xticks([])
ax2.set_xlim(0, 56)
ax2.set_ylim(-0.55, 1.55)

fig.subplots_adjust(left=0.16, right=0.98, top=0.84, bottom=0.08)
fig.savefig(OUT / "kangwon_votes.svg", facecolor=BG)
plt.close(fig)


# ---------------------------------------------------------------------------
# 2. dongduk_survey.svg: Multi-layered Comparison (Deliberation vs 1:1:1 vs Raw)
# ---------------------------------------------------------------------------
fig, ax = new_canvas(width=13.2, height=4.1)
survey_rows = [
    ("숙의기구 학생단 1차 (숙의 전, n=12)", 10.0, 80.0, 10.0, "소규모 숙의 전"),
    ("숙의기구 학생단 2차 (숙의 후, n=12)", 20.0, 50.0, 30.0, "여대유지 -30%p 이동"),
    ("최종 설문 · 집단 동일 가중 (1:1:1)", 51.8, 33.2, 15.0, "권고안 채택 기준"),
    ("최종 설문 · 학생 응답 (n=2,889)", 10.8, 71.3, 17.9, "전체 응답자의 91.0%"),
    ("최종 설문 · 무가중 단순합산 (N=3,176)", 16.4, 66.1, 17.5, "학생 측 '가중치 왜곡' 근거"),
]
y_positions = [4, 3, 2, 1, 0]
for y, (label, coed, women, defer, note) in zip(y_positions, survey_rows):
    parts = [(coed, TEAL, "공학 전환"), (women, RED, "여대 유지"), (defer, MUTED, "유보")]
    left = 0.0
    for val, col, _ in parts:
        ax.barh(y, val, left=left, height=0.54, color=col)
        if val >= 10.0:
            ax.text(left + val / 2, y, f"{val:.1f}%", ha="center", va="center", color="white", weight="bold", fontsize=13)
        left += val
    ax.text(101.5, y, note, ha="left", va="center", color=INK, fontsize=13, weight="bold" if y in (2, 4) else "normal")

ax.set_yticks(y_positions, [r[0] for r in survey_rows], fontsize=13.5, fontweight="bold", color=INK)
ax.set_xticks([])
ax.set_xlim(0, 128)
ax.set_ylim(-0.6, 4.75)

# Legend on top
ax.text(0, 4.62, "■ 공학 전환(2029~2030)", color=TEAL, fontsize=13.5, fontweight="bold")
ax.text(26, 4.62, "■ 여대 유지", color=RED, fontsize=13.5, fontweight="bold")
ax.text(43, 4.62, "■ 유보(현안 해결 후 검토)", color=MUTED, fontsize=13.5, fontweight="bold")
ax.text(74, 4.62, "출처: D07(1·3·4쪽), D08(8·22쪽)", color=SLATE, fontsize=12.5)

fig.subplots_adjust(left=0.27, right=0.99, top=0.92, bottom=0.05)
fig.savefig(OUT / "dongduk_survey.svg", facecolor=BG)
plt.close(fig)


# ---------------------------------------------------------------------------
# 3. dongduk_aftermath.svg: Post-Recommendation Backlash & Admissions Drop
# ---------------------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(
    1, 2, figsize=(13.2, 3.6), dpi=144, gridspec_kw={"width_ratios": [1.35, 1.0], "wspace": 0.28}
)
fig.patch.set_facecolor(BG)
for ax in (ax1, ax2):
    ax.set_facecolor(BG)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.tick_params(axis="both", length=0, colors=INK)

ax1.set_title("① 권고안 이후 학생 반발 및 평의원회 표결 (D10·D14·D15)", loc="left", fontsize=15.5, fontweight="bold", color=INK, pad=12)
post_rows = [
    ("12월 학생 총투표 (n=3,470)", 8.1, 85.7, 6.2, "반대 2,975표"),
    ("1월 학칙개정 학생설문 (n=615)", 12.5, 87.5, 0.0, "개정 반대 87.5%"),
    ("1월 평의원회 표결 (n=10)", 80.0, 20.0, 0.0, "8:2 가결(학생 2명 서명거부)"),
]
for y, (label, pro, con, etc, note) in zip([2, 1, 0], post_rows):
    ax1.barh(y, pro, height=0.48, color=TEAL)
    ax1.barh(y, con, left=pro, height=0.48, color=RED)
    if etc > 0:
        ax1.barh(y, etc, left=pro + con, height=0.48, color=MUTED)
    if pro >= 12:
        ax1.text(pro / 2, y, f"찬성/기타 {pro:.1f}%" if y == 1 else f"찬성 {pro:.1f}%", ha="center", va="center", color="white", weight="bold", fontsize=12.5)
    if con >= 15:
        ax1.text(pro + con / 2, y, f"반대 {con:.1f}%", ha="center", va="center", color="white", weight="bold", fontsize=12.5)
    ax1.text(101.8, y, note, ha="left", va="center", color=INK, fontsize=13, weight="bold")

ax1.set_yticks([2, 1, 0], [r[0] for r in post_rows], fontsize=13.5, fontweight="bold", color=INK)
ax1.set_xticks([])
ax1.set_xlim(0, 142)
ax1.set_ylim(-0.55, 2.55)

ax2.set_title("② 2026학년도 입시 지원자 증감률 (전년 대비, D15)", loc="left", fontsize=15.5, fontweight="bold", color=INK, pad=12)
adm_rows = [
    ("수시 모집", -35.6, "24,092명 → 15,519명"),
    ("정시 모집", -25.4, "6,366명 → 4,923명"),
    ("수시+정시 합계", -32.9, "30,458명 → 20,442명 (-1만 명)"),
]
for y, (label, drop, detail) in zip([2, 1, 0], adm_rows):
    col = RED if y == 0 else "#cf655f"
    ax2.barh(y, abs(drop), height=0.48, color=col)
    ax2.text(abs(drop) / 2, y, f"{drop:.1f}%", ha="center", va="center", color="white", weight="bold", fontsize=13.5)
    ax2.text(abs(drop) + 1.2, y, detail, ha="left", va="center", color=INK, fontsize=12.5, weight="bold" if y == 0 else "normal")

ax2.set_yticks([2, 1, 0], [r[0] for r in adm_rows], fontsize=13.5, fontweight="bold", color=INK)
ax2.set_xticks([])
ax2.set_xlim(0, 68)
ax2.set_ylim(-0.55, 2.55)

fig.subplots_adjust(left=0.20, right=0.98, top=0.84, bottom=0.08)
fig.savefig(OUT / "dongduk_aftermath.svg", facecolor=BG)
plt.close(fig)


# ---------------------------------------------------------------------------
# 4. stance_continuum.svg: Contingency Theory Trajectory (Advocacy <-> Accommodation)
# ---------------------------------------------------------------------------
fig, ax = new_canvas(width=13.2, height=3.6)
ax.set_xlim(0, 100)
ax.set_ylim(0, 10)
ax.set_xticks([])
ax.set_yticks([])

# Continuum header bar
bar = FancyBboxPatch((4, 8.1), 92, 1.15, boxstyle="round,pad=0.1,rounding_size=0.3", facecolor=CARD_BG, edgecolor=BORDER, linewidth=1.5)
ax.add_patch(bar)
ax.text(6, 8.68, "순수 옹호 (Pure Advocacy · 1)", ha="left", va="center", fontsize=14.5, fontweight="bold", color=RED)
ax.text(50, 8.68, "정황적 수용 이론 연속선 (Cancel et al., 1999; 황성욱, 2014)", ha="center", va="center", fontsize=13.5, fontweight="bold", color=INK)
ax.text(94, 8.68, "순수 수용 (Pure Accommodation · 7)", ha="right", va="center", fontsize=14.5, fontweight="bold", color=TEAL)

# Track 1: Kangwon Univ
ax.text(4, 6.6, "사례 A · 강원대", ha="left", va="center", fontsize=15, fontweight="bold", color=TEAL)
ax.text(4, 5.7, "(행동적 수용 이동)", ha="left", va="center", fontsize=12.5, color=SLATE)

# Nodes for Kangwon
ax.plot([24, 68], [6.2, 6.2], color=TEAL, linewidth=3.5, zorder=2)
ax.annotate("", xy=(68, 6.2), xytext=(24, 6.2), arrowprops=dict(arrowstyle="->", color=TEAL, lw=3))
ax.scatter([24], [6.2], s=180, color=RED, zorder=3)
ax.scatter([68], [6.2], s=220, color=TEAL, zorder=3)
ax.text(24, 7.05, "초기 (2/20~4/1): 비공개 추진·원안 고수 → 8:12 부결", ha="center", va="center", fontsize=12.5, fontweight="bold", color=INK)
ax.text(68, 7.05, "4/28 수정안: 거버넌스·정원 실질 조정(35→24명) → 15:6 가결", ha="center", va="center", fontsize=12.5, fontweight="bold", color=TEAL)

# Sub-track for Kangwon procedural advocacy
ax.scatter([31], [4.9], s=130, color=AMBER, zorder=3)
ax.text(31, 4.9, "  ※ 단, 의장의 당일 수정안 제한·신청서 명칭 변경은 옹호(Advocacy) 유지 → 직원 시위 잔존", ha="left", va="center", fontsize=12, color=INK)

# Divider
ax.plot([4, 96], [4.0, 4.0], color=BORDER, linestyle="--", linewidth=1.2)

# Track 2: Dongduk Women's Univ
ax.text(4, 2.3, "사례 B · 동덕여대", ha="left", va="center", fontsize=15, fontweight="bold", color=RED)
ax.text(4, 1.4, "(수사 혼합적 수용)", ha="left", va="center", fontsize=12.5, color=SLATE)

ax.plot([18, 58, 28], [2.1, 2.1, 0.9], color=RED, linewidth=2.5, linestyle="-", zorder=2)
ax.annotate("", xy=(57, 2.1), xytext=(19, 2.1), arrowprops=dict(arrowstyle="->", color=TEAL_LIGHT, lw=2.8))
ax.annotate("", xy=(29, 0.95), xytext=(57, 2.0), arrowprops=dict(arrowstyle="->", color=RED, lw=2.8))

ax.scatter([18], [2.1], s=170, color=RED, zorder=3)
ax.scatter([58], [2.1], s=190, color=TEAL_LIGHT, zorder=3)
ax.scatter([28], [0.9], s=210, color=RED, zorder=3)

ax.text(18, 2.95, "초기 (2024.11): 사전협의 부재·점거 충돌", ha="center", va="center", fontsize=12.5, fontweight="bold", color=INK)
ax.text(62, 2.95, "절차적 수용 (2025.05~11): 4단위 공론화위·숙의기구 가동", ha="center", va="center", fontsize=12.5, fontweight="bold", color=TEAL)
ax.text(30, 0.35, "결론·후속 (2025.12~2026.02): 1:1:1 가중 고수·총투표 중 총장 발표·8:2 학칙 개정 강행 (옹호 복귀)", ha="left", va="center", fontsize=12.2, fontweight="bold", color=RED)

fig.subplots_adjust(left=0.01, right=0.99, top=0.98, bottom=0.02)
fig.savefig(OUT / "stance_continuum.svg", facecolor=BG)
plt.close(fig)

print(f"Created 4 charts in {OUT}")
