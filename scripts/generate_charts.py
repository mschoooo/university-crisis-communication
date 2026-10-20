"""Produce the three evidence charts for the v1 HTML deck.

Data are copied only from the pre-collected source files:
A01P p.40, A02P p.44, D07 pp.1,4, and D10 (2025-12-09).
"""

from pathlib import Path
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager


OUT = Path(__file__).resolve().parents[1] / "versions" / "v1" / "assets"
OUT.mkdir(parents=True, exist_ok=True)

font_path = Path(r"C:\Windows\Fonts\NotoSansKR-VF.ttf")
font_manager.fontManager.addfont(str(font_path))
font_name = font_manager.FontProperties(fname=str(font_path)).get_name()
plt.rcParams.update(
    {
        "font.family": font_name,
        "font.size": 18,
        "svg.fonttype": "none",
        "axes.unicode_minus": False,
    }
)

INK = "#17313d"
TEAL = "#1d807e"
RED = "#be4b45"
MUTED = "#8f9694"
BG = "#f7f5ef"


def basic_axis(width=12.8, height=4.0):
    fig, ax = plt.subplots(figsize=(width, height), dpi=144)
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.tick_params(axis="both", length=0, colors=INK)
    return fig, ax


# A01P p.40 and A02P p.44: two different roll calls (n=20 and n=21).
fig, ax = basic_axis(height=3.8)
rows = [("4월 1일 · 부결", 8, 12, 20), ("4월 28일 · 가결", 15, 6, 21)]
for y, (label, yes, no, total) in zip([1, 0], rows):
    ax.barh(y, yes, height=0.46, color=TEAL)
    ax.barh(y, no, left=yes, height=0.46, color=RED)
    ax.text(yes / 2, y, f"찬성 {yes}", ha="center", va="center", color="white", weight="bold", fontsize=17)
    ax.text(yes + no / 2, y, f"반대 {no}", ha="center", va="center", color="white", weight="bold", fontsize=17)
    ax.text(total + 0.4, y, f"투표 {total}명", ha="left", va="center", color=INK, fontsize=17)
ax.set_yticks([1, 0], [r[0] for r in rows], fontsize=18, color=INK)
ax.set_xticks([])
ax.set_xlim(0, 26)
ax.set_ylim(-0.6, 1.6)
fig.subplots_adjust(left=0.20, right=0.99, top=0.97, bottom=0.1)
fig.savefig(OUT / "kangwon_votes.svg", facecolor=BG)
plt.close(fig)


# D07 pp.1,4: final online survey, 2029–2030 condition.
# The overall result uses equal weights for faculty, student and staff groups.
fig, ax = basic_axis(height=3.9)
survey = [
    ("집단 동일 가중 전체", 51.8, 33.2, 15.0),
    ("학생 응답", 10.8, 71.3, 17.9),
]
for y, (label, coed, women, defer) in zip([1, 0], survey):
    parts = [(coed, TEAL, "공학"), (women, RED, "여대 유지"), (defer, MUTED, "유보")]
    left = 0
    for value, color, name in parts:
        ax.barh(y, value, left=left, height=0.46, color=color)
        ax.text(left + value / 2, y, f"{value:.1f}%", ha="center", va="center", color="white", weight="bold", fontsize=15)
        left += value
ax.set_yticks([1, 0], [r[0] for r in survey], fontsize=18, color=INK)
ax.set_xticks([])
ax.set_xlim(0, 100)
ax.set_ylim(-0.6, 1.6)
fig.subplots_adjust(left=0.22, right=0.99, top=0.97, bottom=0.1)
fig.savefig(OUT / "dongduk_survey.svg", facecolor=BG)
plt.close(fig)


# D10: student referendum, 3,470 votes (not directly comparable to D07).
fig, ax = basic_axis(height=4.6)
votes = [
    ("반대", 2975, "85.7%", RED),
    ("찬성", 280, "8.1%", TEAL),
    ("기권", 147, "4.2%", MUTED),
    ("무효", 68, "2.0%", "#bfc3bd"),
]
for y, (label, count, pct, color) in zip([3, 2, 1, 0], votes):
    ax.barh(y, count, height=0.5, color=color)
    ax.text(count + 45, y, f"{count:,}표  ·  {pct}", ha="left", va="center", color=INK, fontsize=17)
ax.set_yticks([3, 2, 1, 0], [r[0] for r in votes], fontsize=18, color=INK)
ax.set_xticks([])
ax.set_xlim(0, 3700)
ax.set_ylim(-0.6, 3.6)
fig.subplots_adjust(left=0.12, right=0.99, top=0.97, bottom=0.1)
fig.savefig(OUT / "dongduk_student_vote.svg", facecolor=BG)
plt.close(fig)

print(f"Created 3 charts in {OUT}")
