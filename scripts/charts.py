"""Rebuild every chart in the book.

Usage, from the repository root:

    python3 scripts/charts.py            # writes into images/
    python3 scripts/charts.py some/dir   # writes somewhere else

Needs matplotlib (the committed images were made with 3.11.2). The charts use
the Inter font when it's installed and fall back to DejaVu Sans otherwise, which
changes text widths slightly. With Inter and that matplotlib version the output
matches the committed PNGs byte for byte.

Every number sits in a DATA block inside its function, with its source noted,
and every total, share or curve is computed from those numbers. The charts and
the chapters that show them:

    resources        resources.png        chapter 1
    school_map       school-map.png       README, chapter 7
    gear_timeline    gear-timeline.png    chapter 15
    toxicity_budget  toxicity-budget.png  chapters 4, 12 and 19
    sign_intensity   sign-intensity.png   chapters 9 and 19
    crit_stack       crit-stack.png       chapters 8 and 19
    poison_odds      poison-odds.png      chapters 13 and 19
    skill_route      skill-route.png      chapters 2 and 11
    ursine_ehp       ursine-effective-health.png  chapter 10

Values marked as game-file values come from the audit in chapter 19.
"""
import math
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from matplotlib import font_manager

OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent / "images"
OUT.mkdir(parents=True, exist_ok=True)

# ---- palette (dataviz reference palette, light mode) ----
SURFACE = "#fcfcfb"
INK = "#0b0b0b"
INK2 = "#52514e"
MUTED = "#898781"
GRID = "#e1e0d9"
AXIS = "#c3c2b7"
GREY_DATA = "#b9b7ae"
BLUE, ORANGE, AQUA, YELLOW = "#2a78d6", "#eb6834", "#1baf7a", "#eda100"
GOOD, CRIT = "#0ca30c", "#d03b3b"
BLUE_RAMP = ["#86b6ef", "#3987e5", "#1c5cab", "#0d366b"]  # ordinal steps 250 / 400 / 550 / 700
WEIGHT = {"Light": BLUE, "Medium": ORANGE, "Heavy": AQUA}

fams = {f.name for f in font_manager.fontManager.ttflist}
FONT = "Inter" if "Inter" in fams else "DejaVu Sans"
plt.rcParams.update({
    "font.family": FONT,
    "font.size": 11,
    "axes.edgecolor": AXIS,
    "axes.labelcolor": INK2,
    "xtick.color": INK2,
    "ytick.color": INK2,
    "figure.facecolor": SURFACE,
    "axes.facecolor": SURFACE,
    "savefig.facecolor": SURFACE,
})


def titled(fig, title, subtitle=None, top=0.93):
    fig.text(0.04, top, title, fontsize=16, fontweight="bold", color=INK, ha="left", va="top")
    if subtitle:
        fig.text(0.04, top - 0.055, subtitle, fontsize=11, color=INK2, ha="left", va="top")


def clean(ax, grid_axis="x"):
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color(AXIS)
    ax.tick_params(length=0)
    if grid_axis:
        ax.grid(axis=grid_axis, color=GRID, linewidth=0.8)
        ax.set_axisbelow(True)


def save(fig, name):
    fig.savefig(OUT / name, dpi=200)
    plt.close(fig)
    print("wrote", OUT / name)


# =====================================================================
# 1. Resource diagram
# =====================================================================
def resources():
    fig = plt.figure(figsize=(12, 7.2))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 120)
    ax.set_ylim(0, 72)
    ax.axis("off")
    titled(fig, "Every build trades four resources",
           "What fills and drains them, and what each one pays for. + adds to the resource, − takes from it.", top=0.965)

    def box(x, y, w, h, head, body, edge=AXIS, fill=SURFACE, lw=1.2, headw="bold"):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.25,rounding_size=1.2",
                                    linewidth=lw, edgecolor=edge, facecolor=fill))
        if body:
            ax.text(x + w / 2, y + h - 2.1, head, ha="center", va="top", fontsize=11.5, fontweight=headw, color=INK)
            ax.text(x + w / 2, y + h - 5.1, body, ha="center", va="top", fontsize=9.6, color=INK2, linespacing=1.35)
        else:
            ax.text(x + w / 2, y + h / 2, head, ha="center", va="center", fontsize=11.5, fontweight=headw, color=INK)
        return (x, y, w, h)

    # columns
    ax.text(12, 61.4, "WHAT YOU DO", ha="center", fontsize=9.5, color=MUTED, fontweight="bold")
    ax.text(55, 61.4, "RESOURCE", ha="center", fontsize=9.5, color=MUTED, fontweight="bold")
    ax.text(97, 61.4, "WHAT IT PAYS FOR", ha="center", fontsize=9.5, color=MUTED, fontweight="bold")

    L = {}
    L["hits"] = box(2, 50, 20, 7, "Sword hits", None)
    L["signs"] = box(2, 36, 20, 7, "Casting Signs", None)
    L["hurt"] = box(2, 22, 20, 7, "Getting hit", None)
    L["drink"] = box(2, 6, 20, 9, "Potions and", None)
    ax.text(12, 8.7, "decoctions", ha="center", va="center", fontsize=11.5, fontweight="bold", color=INK)

    M = {}
    M["adr"] = box(44, 47.5, 22, 10, "Adrenaline", "0 to 3 points", edge=BLUE, lw=2)
    M["sta"] = box(44, 34.5, 22, 10, "Stamina", "refills over time", edge=BLUE, lw=2)
    M["vit"] = box(44, 20.5, 22, 10, "Vitality", "your health", edge=BLUE, lw=2)
    M["tox"] = box(44, 5.5, 22, 10, "Toxicity", "decoctions lock 50 each", edge=BLUE, lw=2)

    R = {}
    R["held"] = box(80, 50.5, 34, 8.5, "Held: makes you stronger", "Battle Frenzy, Focus, Mutated Skin")
    R["spent"] = box(80, 40.5, 34, 8.5, "Spent: big moves", "Rend, Whirl, Undying, Flood of Anger")
    R["sta"] = box(80, 30, 34, 8.5, "Pays for", "Signs, Whirl, Rend, Active Shield, sprint")
    R["vit"] = box(80, 19, 34, 8.5, "At zero you die, unless", "Undying or Second Life saves you")
    R["tox"] = box(80, 3.5, 34, 11.5, "Unlocks, then limits",
                   "Frenzy, Endure Pain, Euphoria.\nIt also caps how many\npotions you can drink")

    def right_mid(b):
        x, y, w, h = b
        return (x + w + 0.6, y + h / 2)

    def left_mid(b, dy=0.0):
        x, y, w, h = b
        return (x - 0.6, y + h / 2 + dy)

    def arrow(p0, p1, color, label=None, rad=0.0, lx=None, ly=None):
        a = FancyArrowPatch(p0, p1, arrowstyle="-|>", mutation_scale=13, linewidth=1.6,
                            color=color, connectionstyle=f"arc3,rad={rad}", shrinkA=0, shrinkB=0)
        ax.add_patch(a)
        if label:
            mx = lx if lx is not None else (p0[0] + p1[0]) / 2
            my = ly if ly is not None else (p0[1] + p1[1]) / 2
            ax.text(mx, my, label, ha="center", va="center", fontsize=10, color=INK,
                    bbox=dict(boxstyle="round,pad=0.25", fc=SURFACE, ec=color, lw=1))

    # left -> middle
    arrow(right_mid(L["hits"]), left_mid(M["adr"], 1.5), GOOD, "+", lx=33, ly=55.0)
    arrow(right_mid(L["signs"]), left_mid(M["sta"], 1.0), CRIT, "−", lx=33, ly=40.0)
    arrow(right_mid(L["signs"]), left_mid(M["adr"], -2.0), GOOD, "+ with Adrenaline Burst", rad=-0.18, lx=31.5, ly=46.6)
    arrow(right_mid(L["hurt"]), left_mid(M["vit"], 0.5), CRIT, "−", lx=33, ly=25.8)
    arrow(right_mid(L["hurt"]), left_mid(M["adr"], -3.8), CRIT, "−", rad=0.28, lx=36.5, ly=37.0)
    arrow(right_mid(L["drink"]), left_mid(M["tox"], 0.0), GOOD, "+", lx=33, ly=10.5)
    arrow(right_mid(L["drink"]), left_mid(M["vit"], -2.8), GOOD, "+ heals", rad=0.2, lx=30.5, ly=17.0)

    # middle -> right
    def plain(p0, p1, rad=0.0):
        ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle="-|>", mutation_scale=12, linewidth=1.2,
                                     color=MUTED, connectionstyle=f"arc3,rad={rad}", shrinkA=0, shrinkB=0))
    plain(right_mid(M["adr"]), left_mid(R["held"]))
    plain(right_mid(M["adr"]), left_mid(R["spent"]))
    plain(right_mid(M["sta"]), left_mid(R["sta"]))
    plain(right_mid(M["vit"]), left_mid(R["vit"]))
    plain(right_mid(M["tox"]), left_mid(R["tox"]))

    fig.text(0.04, 0.012, "Sources: witcherhour.com skill values (5.0), hacktheminotaur.com Adrenaline guide, Fextralife decoction rules (pre-5.0).",
             fontsize=8.5, color=MUTED)
    save(fig, "resources.png")


# =====================================================================
# 2. School playstyle map
# =====================================================================
def school_map():
    # DATA: placement is the author's judgment from each school's technique and set bonuses.
    schools = [
        # name, x (0 swords .. 1 Signs), y (0 react .. 1 prepare), weight, note
        ("Feline", 0.12, 0.24, "Light", "fast attacks, crits"),
        ("Ursine", 0.30, 0.12, "Heavy", "strong attacks, Quen"),
        ("Wolven", 0.52, 0.42, "Medium", "sword and Sign hybrid"),
        ("Griffin", 0.86, 0.36, "Medium", "Yrden, Igni, Aard"),
        ("Viper", 0.20, 0.66, "Medium", "poisoned blades"),
        ("Manticore", 0.36, 0.86, "Medium", "decoctions, bombs, crits"),
    ]
    fig = plt.figure(figsize=(11, 8.2))
    ax = fig.add_axes([0.09, 0.10, 0.84, 0.70])
    titled(fig, "Six schools, two questions",
           "What deals your damage, and how much you prepare before a fight. Dot color = armor weight the school wants.", top=0.965)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axhline(0.5, color=GRID, lw=1.2)
    ax.axvline(0.5, color=GRID, lw=1.2)
    for s in ax.spines.values():
        s.set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.text(0.0, -0.045, "Swords do the work", ha="left", va="top", color=INK2, fontsize=11, transform=ax.transAxes)
    ax.text(1.0, -0.045, "Signs do the work", ha="right", va="top", color=INK2, fontsize=11, transform=ax.transAxes)
    ax.text(-0.02, 0.0, "React in the moment", ha="right", va="bottom", rotation=90, color=INK2, fontsize=11, transform=ax.transAxes)
    ax.text(-0.02, 1.0, "Prepare before the fight", ha="right", va="top", rotation=90, color=INK2, fontsize=11, transform=ax.transAxes)
    for name, x, y, w, note in schools:
        ax.scatter([x], [y], s=260, color=WEIGHT[w], edgecolor=SURFACE, linewidth=2, zorder=3)
        ax.text(x + 0.035, y + 0.012, name, fontsize=13, fontweight="bold", color=INK, va="bottom")
        ax.text(x + 0.035, y - 0.005, note, fontsize=10, color=INK2, va="top")
    # legend
    lx = 0.66
    for i, (w, c) in enumerate(WEIGHT.items()):
        ax.scatter([lx + i * 0.11], [0.955], s=110, color=c, zorder=3)
        ax.text(lx + i * 0.11 + 0.02, 0.955, w, va="center", fontsize=10.5, color=INK2)
    fig.text(0.04, 0.02, "Placement is the author's judgment, based on each school's 5.0 technique, its Grandmaster set bonuses and the builds guides recommend.",
             fontsize=8.5, color=MUTED)
    save(fig, "school-map.png")


# =====================================================================
# 3. Gear timeline
# =====================================================================
def gear_timeline():
    # DATA: tier levels, computed from the 5.0 game files by scripts/item_levels.py
    # (they match the older Console Pulse, Gamestegy and KeenGamer figures)
    witcher = [
        ("Viper swords", "Medium", [(1, "")], "levels 1 and 2, White Orchard"),
        ("Griffin", "Medium", [(11, "B"), (18, "E"), (26, "S"), (34, "M"), (40, "G")], ""),
        ("Wolven", "Medium", [(14, "B"), (21, "E"), (29, "S"), (34, "M"), (40, "G")], ""),
        ("Feline", "Light", [(17, "B"), (23, "E"), (29, "S"), (34, "M"), (40, "G")], ""),
        ("Forgotten Wolven", "Medium", [(20, "B"), (34, "M"), (40, "G")], ""),
        ("Ursine", "Heavy", [(20, "B"), (25, "E"), (30, "S"), (34, "M"), (40, "G")], ""),
        ("Viper set + Venomous swords", "Medium", [(39, "")], "Hearts of Stone, missable"),
        ("Manticore", "Medium", [(40, "G")], "Toussaint only"),
    ]
    bridge = [
        ("Temerian (free DLC)", "Light", [(4, "")]),
        ("Thousand Flowers (reward)", "Medium", [(7, "")]),
        ("Nilfgaardian (free DLC)", "Medium", [(10, "")]),
        ("White Tiger of the West (reward)", "Medium", [(11, "")]),
        ("Undvik (free DLC)", "Heavy", [(16, "")]),
    ]
    rows = [(n, w, t, note) for n, w, t, note in witcher] + [None] + [(n, w, t, "") for n, w, t in bridge]
    fig = plt.figure(figsize=(12, 9.4))
    ax = fig.add_axes([0.30, 0.09, 0.66, 0.72])
    titled(fig, "The first witcher set fits at level 11; every school meets at Grandmaster, level 40",
           "Required level for each tier (B Basic, E Enhanced, S Superior, M Mastercrafted, G Grandmaster) and for the best bridge armor.", top=0.965)
    n = len(rows)
    ax.set_xlim(0, 44)
    ax.set_ylim(-0.6, n - 0.4)
    ax.invert_yaxis()
    clean(ax, grid_axis="x")
    ax.set_xticks(range(0, 45, 5))
    ax.set_xlabel("Character level", color=INK2)
    ax.set_yticks([])
    for lvl, text in ((24, "Master crafters\n(Yoana, Hattori)"), (40, "Grandmaster crafter\n(Lazare Lafargue)")):
        ax.axvline(lvl, color=AXIS, lw=1.2, ls=(0, (4, 3)), zorder=1)
        ax.text(lvl, -0.75, text, ha="center", va="bottom", fontsize=9, color=INK2)
    for i, row in enumerate(rows):
        if row is None:
            ax.text(-0.015, i, "BRIDGE ARMOR", transform=ax.get_yaxis_transform(), ha="right", va="center",
                    fontsize=9.5, color=MUTED, fontweight="bold")
            continue
        name, w, tiers, note = row
        c = WEIGHT[w]
        xs = [t[0] for t in tiers]
        if len(xs) > 1:
            ax.plot(xs, [i] * len(xs), color=c, lw=2, alpha=0.45, zorder=2)
        ax.scatter(xs, [i] * len(xs), s=70, color=c, edgecolor=SURFACE, linewidth=1.5, zorder=3)
        for x, lab in tiers:
            if lab:
                ax.text(x, i + 0.24, f"{lab} {x}", ha="center", va="top", fontsize=8.5, color=INK2)
            elif not note:
                ax.text(x + 0.8, i, str(x), ha="left", va="center", fontsize=9, color=INK2)
        if note:
            right = max(xs)
            if right >= 39:
                ax.text(right - 1.0, i, f"{note}  {right}" if not tiers[0][1] else note, ha="right", va="center", fontsize=9, color=INK2)
            else:
                ax.text(right + 0.8, i, note, ha="left", va="center", fontsize=9, color=INK2)
        ax.text(-0.015, i, name, transform=ax.get_yaxis_transform(), ha="right", va="center", fontsize=10.5, color=INK)
    # legend
    for k, (w, c) in enumerate(WEIGHT.items()):
        fig.text(0.30 + k * 0.1, 0.845, "●", color=c, fontsize=12, va="center")
        fig.text(0.315 + k * 0.1, 0.845, w, color=INK2, fontsize=10, va="center")
    fig.text(0.04, 0.02, "Levels computed from the game files, build 5.0.0.1048522 (scripts/item_levels.py). Reward sets need a linked CD PROJEKT RED account.",
             fontsize=8.5, color=MUTED)
    save(fig, "gear-timeline.png")


# =====================================================================
# 4. Toxicity budget
# =====================================================================
def toxicity_budget():
    # DATA: every value from the game files, build 5.0.0.1048522 (chapter 19)
    BASE = 100          # max Toxicity (geralt_stats.xml)
    DECOCTION = 50      # toxicity_offset of standard decoctions (def_item_alchemy_mutagens.xml); Basilisk 40
    AT_PER_RECIPE = 0.5 # Acquired Tolerance: +0.5 per eligible learned recipe with level <= rank (alchemy_s18)
    RECIPES = 40        # example count of eligible recipes learned (an assumption, labelled)
    ALL_RECIPES = 173   # eligible recipe definitions in base game + both expansions (no bolts, no dyes, no commented-out entries)
    MC_R3 = 30          # Metabolic Control rank 3: +10 per rank (perk_33)
    MANTICORE = 5 * 4   # +5 per Manticore armor piece (Blood and Wine def_item_crafting_*.xml)
    POTION_ROOM = 25    # one Thunderbolt or Petri's Philter (def_item_alchemy_potion.xml)
    steps = [
        ("No Toxicity skills", BASE),
        (f"+ Acquired Tolerance rank 3\n({RECIPES} eligible recipes learned)", BASE + AT_PER_RECIPE * RECIPES),
        ("+ Metabolic Control rank 3", BASE + AT_PER_RECIPE * RECIPES + MC_R3),
        ("+ Manticore armor, 4 pieces", BASE + AT_PER_RECIPE * RECIPES + MC_R3 + MANTICORE),
        (f"Every eligible recipe in the game\n({ALL_RECIPES}) instead of {RECIPES}", BASE + AT_PER_RECIPE * ALL_RECIPES + MC_R3 + MANTICORE),
    ]
    need_for_4 = math.ceil((4 * DECOCTION + POTION_ROOM - (BASE + MC_R3 + MANTICORE)) / AT_PER_RECIPE)
    fig = plt.figure(figsize=(12, 6.6))
    ax = fig.add_axes([0.27, 0.14, 0.68, 0.64])
    titled(fig, f"Four decoctions need {need_for_4} of the game's {ALL_RECIPES} recipes",
           f"Maximum Toxicity as each bonus is added, top to bottom, and the decoctions that fit while keeping {POTION_ROOM} free for a Thunderbolt.", top=0.965)
    clean(ax, grid_axis=None)
    xmax = steps[-1][1] + 30
    ax.set_xlim(0, xmax)
    ax.set_ylim(-0.6, len(steps) - 0.4)
    ax.invert_yaxis()
    ax.set_yticks([])
    ax.set_xticks([])
    for i, (label, cap) in enumerate(steps):
        nd = int((cap - POTION_ROOM) // DECOCTION)
        for d in range(nd):
            ax.barh(i, DECOCTION - 1.5, left=d * DECOCTION, height=0.56, color=BLUE, zorder=3)
            ax.text(d * DECOCTION + DECOCTION / 2, i, "decoction", ha="center", va="center", fontsize=9, color="white", zorder=4)
        rest = cap - nd * DECOCTION
        ax.barh(i, rest, left=nd * DECOCTION, height=0.56, color=GREY_DATA, zorder=3)
        ax.text(nd * DECOCTION + rest / 2, i, f"{rest:g} for potions", ha="center", va="center", fontsize=8.5, color=INK, zorder=4)
        ax.text(cap + 3, i, f"max {cap:g}", ha="left", va="center", fontsize=10.5, color=INK, fontweight="bold")
        ax.text(-3, i, label, ha="right", va="center", fontsize=10.5, color=INK)
    fig.text(0.04, 0.045, f"All values from the game files, build 5.0.0.1048522. Acquired Tolerance adds 0.5 per eligible learned recipe; {RECIPES} is an example.",
             fontsize=8.5, color=MUTED)
    fig.text(0.04, 0.018, f"{ALL_RECIPES} = recipes defined in the base game and both expansions, bolts and dyes excluded; how many a playthrough can learn is unverified.",
             fontsize=8.5, color=MUTED)
    save(fig, "toxicity-budget.png")


# =====================================================================
# 5. Griffin Sign intensity sources
# =====================================================================
def sign_intensity():
    # DATA: label, value %, needs Yrden?, source
    rows = [
        ("Griffin set, 6 pieces, inside Yrden", 100, True),        # game files: GryphonSetBonusYrdenEffect spell_power 1.0
        ("Catalyst rank 3 (Aard and Igni in Yrden)", 90, True),    # witcherhour 5.0
        ("Focus rank 3, 3 Adrenaline held", 90, False),            # witcherhour 5.0
        ("Chain Reaction rank 3, 5 stacks", 75, False),            # witcherhour 5.0 (15% x 5)
        ("Superior Petri's Philter", 25, False),                  # Fextralife potions
        ("Griffin School Techniques rank 3, 4 pieces", 24, False), # witcherhour 5.0 (6% x 4)
        ("Grandmaster Griffin chest piece", 22, False),            # game files (chapter 19, Grandmaster items)
        ("Grandmaster Griffin steel sword", 21, False),            # game files (chapter 19, Grandmaster items)
    ]
    fig = plt.figure(figsize=(12, 6.4))
    ax = fig.add_axes([0.35, 0.10, 0.60, 0.68])
    titled(fig, "A Griffin standing in Yrden stacks two of the biggest Sign bonuses",
           "Sign intensity added by each source, fully upgraded. Blue = only works inside Yrden (Catalyst: enemies in it; set: you in it).", top=0.965)
    clean(ax, grid_axis=None)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(0, 112)
    ax.set_ylim(-0.6, len(rows) - 0.4)
    ax.invert_yaxis()
    for i, (lab, v, yrden) in enumerate(rows):
        ax.barh(i, v, height=0.6, color=BLUE if yrden else GREY_DATA, zorder=3)
        ax.text(v + 1.5, i, f"+{v}%", va="center", fontsize=10.5, color=INK, fontweight="bold" if yrden else "normal")
        ax.text(-2, i, lab, ha="right", va="center", fontsize=10.5, color=INK)
    fig.text(0.04, 0.03, "Game files (build 5.0.0.1048522): Griffin set, Griffin Techniques, Petri's Philter, Grandmaster items. witcherhour.com (5.0): Catalyst, Focus, Chain Reaction.",
             fontsize=8.5, color=MUTED)
    save(fig, "sign-intensity.png")


# =====================================================================
# 6. Crit chance stack (Feline)
# =====================================================================
def crit_stack():
    # DATA
    BF_R1, BF_R3 = 3, 9   # Battle Frenzy % per Adrenaline point held (witcherhour 5.0)
    KATAKAN = 10          # Katakan decoction (Fextralife)
    levels = [0, 1, 2, 3]
    fig = plt.figure(figsize=(11, 6.0))
    ax = fig.add_axes([0.08, 0.16, 0.88, 0.60])
    full = KATAKAN + BF_R3 * 3
    titled(fig, f"At full Adrenaline, rank-3 Battle Frenzy plus Katakan add +{full}% crit chance",
           "Bonus crit chance by Adrenaline points held. The 5% base crit chance and gear come on top.", top=0.965)
    clean(ax, grid_axis=None)
    ax.set_yticks([])
    ax.set_ylim(0, 44)
    ax.set_xlim(-0.6, 3.6)
    ax.set_xticks(levels)
    ax.set_xticklabels([f"{a} Adrenaline" for a in levels], fontsize=11)
    w = 0.5
    for a in levels:
        ax.bar(a, KATAKAN, width=w, color=AQUA, zorder=3)
        bf = BF_R3 * a
        if bf:
            ax.bar(a, bf - 0.4, bottom=KATAKAN + 0.4, width=w, color=YELLOW, zorder=3)
        ax.text(a, KATAKAN + bf + 1.0, f"+{KATAKAN + bf}%", ha="center", va="bottom", fontsize=12, fontweight="bold", color=INK)
        r1 = KATAKAN + BF_R1 * a
        ax.plot([a - w / 2 - 0.06, a + w / 2 + 0.06], [r1, r1], color=INK, lw=1.4, ls=(0, (3, 2)), zorder=5)
    ax.text(3 + w / 2 + 0.1, KATAKAN + BF_R1 * 3, f"rank 1:\n+{KATAKAN + BF_R1 * 3}%", va="center", fontsize=9, color=INK2)
    fig.text(0.08, 0.80, "■", color=AQUA, fontsize=13, va="center")
    fig.text(0.097, 0.80, f"Katakan Decoction (+{KATAKAN}%)", color=INK2, fontsize=10, va="center")
    fig.text(0.33, 0.80, "■", color=YELLOW, fontsize=13, va="center")
    fig.text(0.347, 0.80, f"Battle Frenzy rank 3 (+{BF_R3}% per point)", color=INK2, fontsize=10, va="center")
    fig.text(0.63, 0.80, "- - -", color=INK, fontsize=10, va="center")
    fig.text(0.665, 0.80, f"same with Battle Frenzy rank 1 (+{BF_R1}%)", color=INK2, fontsize=10, va="center")
    fig.text(0.04, 0.03, "Battle Frenzy values: witcherhour.com (5.0). Katakan +10%: Fextralife (pre-5.0 value, no reported change). Base 5%: game files, build 5.0.0.1048522.", fontsize=8.5, color=MUTED)
    save(fig, "crit-stack.png")


# =====================================================================
# 7. Poison odds
# =====================================================================
def poison_odds():
    # DATA: Poisoned Blades chance = 0.05*rank + 0.10*(oil tier - 1), needs an oil matching the target;
    # a poison sword rolls separately (game files, build 5.0.0.1048522; chapter 19)
    viper = 1 - (1 - 0.35) * (1 - 0.15)
    chances = [(0.05, "5% per hit", "Poisoned Blades rank 1, basic oil"),
               (0.15, "15% per hit", "rank 3 with a basic oil,\nor a Viper sword on its own"),
               (0.35, "35% per hit", "rank 3 with a superior oil"),
               (viper, f"{viper:.2%} per hit", "rank 3, superior oil\nand a Viper sword")]
    hits = list(range(1, 21))
    fig = plt.figure(figsize=(11.5, 6.6))
    ax = fig.add_axes([0.08, 0.13, 0.55, 0.64])
    p3s = [1 - (1 - p) ** 3 for p, _, _ in chances]
    titled(fig, f"With a superior oil, one three-hit combo poisons the target {p3s[2]:.0%} of the time",
           "Chance the target is poisoned after n hits with a matching oil: 1 − (1 − p)^n.", top=0.965)
    clean(ax, grid_axis="y")
    ax.set_xlim(1, 20)
    ax.set_ylim(0, 1.0)
    ax.set_yticks([0, 0.25, 0.5, 0.75, 1.0])
    ax.set_yticklabels(["0%", "25%", "50%", "75%", "100%"])
    ax.set_xticks([1, 3, 5, 10, 15, 20])
    ax.set_xlabel("Hits landed with a matching oil", color=INK2)
    ax.axhline(0.5, color=AXIS, lw=1.2, ls=(0, (4, 3)))
    ax.axvline(3, color=AXIS, lw=1.0, ls=(0, (2, 3)))
    ax.text(3.15, 0.04, "one combo\n(3 fast hits)", va="bottom", fontsize=9, color=INK2)
    legend_y = [0.18, 0.37, 0.56, 0.74]  # figure-relative rows for the side legend, bottom to top
    for (p, lab, src), col, ly, p3 in zip(chances, BLUE_RAMP, legend_y, p3s):
        ys = [1 - (1 - p) ** n for n in hits]
        ax.plot(hits, ys, color=col, lw=2.2)
        ax.scatter([3], [p3], s=40, color=col, zorder=4, edgecolors="#fcfcfb", linewidths=1.5)
        half = math.ceil(math.log(0.5) / math.log(1 - p))
        fig.lines.append(plt.Line2D([0.665, 0.705], [ly + 0.012, ly + 0.012], transform=fig.transFigure, color=col, lw=2.6))
        fig.text(0.715, ly + 0.012, lab, fontsize=10.5, fontweight="bold", color=INK, va="center")
        fig.text(0.715, ly - 0.020, src, fontsize=9.3, color=INK2, va="top")
        fig.text(0.715, ly - (0.083 if "\n" in src else 0.052), f"one combo: {p3:.0%} · even odds after {half} hit{'s' if half > 1 else ''}", fontsize=9.3, color=INK2, va="top")
    fig.text(0.04, 0.03, "Game files, build 5.0.0.1048522: Poisoned Blades 5% per rank, +10% per oil tier above basic; Viper swords 15%, rolled separately. Assumes a target below 100% poison resistance.",
             fontsize=8.5, color=MUTED)
    save(fig, "poison-odds.png")


# =====================================================================
# 8. Skill route (Wolven hybrid), phases shaded
# =====================================================================
def skill_route():
    # DATA: the Wolven plan in chapter 11; links from witcherdb (5.0)
    PH = ["Opening (first 6 points)", "Phase 1 (to 13)", "Phase 2 (to 20)", "Phase 3 (to 28)", "Phase 4 (30+)"]
    SHADE = ["#1c5cab", "#3987e5", "#86b6ef", "#c4dbf7", "#eef4fc"]
    TXT = ["white", "white", INK, INK, INK]
    cols = {
        "Combat": [("Muscle Memory", 0), ("Strength Training", 0), ("Three Strikes", 1), ("Razor Focus", 1), ("Undying", 2)],
        "Signs": [("Exploding Shield", 0), ("Active Shield", 2), ("Melt Armor", 0), ("Sustained Glyphs", 1), ("Magic Trap", 1),
                  ("Supercharged Glyphs", 2), ("Catalyst", 3), ("Focus", 4), ("Chain Reaction", 4), ("Aftershock", 4), ("Resonance", 4)],
        "Alchemy": [("Refreshment", 0), ("Hunter Instinct", 3), ("Acquired Tolerance", 3), ("Tissue Transmutation", 4),
                    ("Frenzy", 1), ("Poisoned Blades", 2), ("Toxic Shock", 2)],
        "General": [("Wolf School Techniques", 1), ("Sun and Stars", 3), ("Survival Instinct", 3), ("Adrenaline Burst", 3),
                    ("Anger Management", 4), ("Synergy", 4)],
    }
    edges = {
        "Combat": [(0, 1), (0, 2), (2, 3), (2, 4)],
        "Signs": [(0, 1), (3, 4), (4, 5), (5, 6), (6, 7), (6, 8), (8, 9), (9, 10)],
        "Alchemy": [(0, 1), (1, 2), (2, 3), (4, 5), (5, 6)],
        "General": [(0, 1), (1, 2), (2, 3), (2, 4), (4, 5)],
    }
    fig = plt.figure(figsize=(11, 9.2))
    ax = fig.add_axes([0.03, 0.10, 0.94, 0.74])
    ax.set_xlim(0, 13.2)
    ax.set_ylim(11.4, -0.9)
    ax.axis("off")
    titled(fig, "Signs is the long climb: Resonance sits six skills past its starting skill",
           "The Wolven hybrid route. Arrows run from a prerequisite to the skill it unlocks; darker boxes are bought earlier.", top=0.965)
    W, H, STEP = 2.7, 0.62, 1.0
    for ci, (tree, items) in enumerate(cols.items()):
        x0 = 0.45 + ci * 3.25
        ax.text(x0 + W / 2, -0.55, tree, ha="center", va="center", fontsize=13, fontweight="bold", color=INK)
        for ri, (name, ph) in enumerate(items):
            y = ri * STEP
            ax.add_patch(FancyBboxPatch((x0, y - H / 2), W, H, boxstyle="round,pad=0.02,rounding_size=0.12",
                                        fc=SHADE[ph], ec=AXIS if ph >= 3 else SHADE[ph], lw=1.0, zorder=3))
            ax.text(x0 + W / 2, y, name, ha="center", va="center", fontsize=10.5, color=TXT[ph], zorder=4,
                    fontweight="bold" if name == "Resonance" else "normal")
        for a, b in edges[tree]:
            ya, yb = a * STEP, b * STEP
            if b == a + 1:
                ax.add_patch(FancyArrowPatch((x0 + W / 2, ya + H / 2), (x0 + W / 2, yb - H / 2), arrowstyle="-|>",
                                             mutation_scale=9, color=MUTED, lw=1.1, zorder=2))
            else:
                xl = x0 - 0.22
                ax.plot([x0, xl, xl], [ya, ya, yb], color=MUTED, lw=1.1, zorder=2)
                ax.add_patch(FancyArrowPatch((xl, yb), (x0, yb), arrowstyle="-|>", mutation_scale=9, color=MUTED, lw=1.1, zorder=2))
    for k, lab in enumerate(PH):
        x = 0.04 + k * 0.19
        fig.patches.append(FancyBboxPatch((x, 0.052), 0.018, 0.022, boxstyle="round,pad=0.002", transform=fig.transFigure,
                                          fc=SHADE[k], ec=AXIS, lw=0.8))
        fig.text(x + 0.026, 0.063, lab, fontsize=10, color=INK2, va="center")
    fig.text(0.04, 0.018, "Prerequisite links: witcherdb.com Remastered planner (5.0). Phases follow chapter 11's plan.", fontsize=8.5, color=MUTED)
    save(fig, "skill-route.png")


# =====================================================================
# 9. Ursine effective health (Mutated Skin)
# =====================================================================
def ursine_ehp():
    # DATA: game files, build 5.0.0.1048522 (chapter 19)
    BEAR = 0.02 * 3 * 4      # Bear School Techniques: 0.02 per rank per heavy piece, rank 3, four pieces
    SURVIVAL = 0.08 * 3      # Survival Instinct rank 3 (+8% per rank, witcherhour 5.0)
    SKIN = 0.15              # Mutated Skin: -15% Vitality damage per whole Adrenaline point (Mutation5)
    levels = [0, 1, 2, 3]
    base = 1 + BEAR + SURVIVAL
    with_skin = [base / (1 - SKIN * a) for a in levels]
    fig = plt.figure(figsize=(11, 6.0))
    ax = fig.add_axes([0.08, 0.16, 0.88, 0.60])
    titled(fig, f"With Mutated Skin and a full bar, an Ursine lasts {with_skin[-1]:.1f} times as long as an unbuffed Geralt",
           "Effective health by whole Adrenaline points held, between Quen shields (Mutated Skin is off while a shield is up).", top=0.965)
    clean(ax, grid_axis=None)
    ax.set_yticks([])
    ax.set_ylim(0, 3.2)
    ax.set_xlim(-0.6, 3.6)
    ax.set_xticks(levels)
    ax.set_xticklabels([f"{a} Adrenaline" for a in levels], fontsize=11)
    w = 0.34
    for a, v in zip(levels, with_skin):
        ax.bar(a - w / 2 - 0.02, base, width=w, color=GREY_DATA, zorder=3)
        ax.text(a - w / 2 - 0.02, base + 0.05, f"{base:.2f}×", ha="center", va="bottom", fontsize=10, color=INK2)
        ax.bar(a + w / 2 + 0.02, v, width=w, color=AQUA, zorder=3)
        ax.text(a + w / 2 + 0.02, v + 0.05, f"{v:.2f}×", ha="center", va="bottom", fontsize=12, fontweight="bold", color=INK)
    fig.text(0.08, 0.80, "■", color=GREY_DATA, fontsize=13, va="center")
    fig.text(0.097, 0.80, "Bear School Techniques and Survival Instinct only", color=INK2, fontsize=10, va="center")
    fig.text(0.45, 0.80, "■", color=AQUA, fontsize=13, va="center")
    fig.text(0.467, 0.80, "with Mutated Skin (−15% damage per whole point)", color=INK2, fontsize=10, va="center")
    fig.text(0.04, 0.045, "Game files, build 5.0.0.1048522: Bear School Techniques rank 3 on four heavy pieces (+24%), Mutated Skin 0.15 per whole point.",
             fontsize=8.5, color=MUTED)
    fig.text(0.04, 0.018, "Survival Instinct rank 3 (+24%): witcherhour.com (5.0). Assumes the two Vitality bonuses add.", fontsize=8.5, color=MUTED)
    save(fig, "ursine-effective-health.png")


if __name__ == "__main__":
    resources()
    school_map()
    gear_timeline()
    toxicity_budget()
    sign_intensity()
    crit_stack()
    poison_odds()
    skill_route()
    ursine_ehp()
