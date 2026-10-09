"""The patch 5.0 skill trees: prerequisite links and the cheapest route to each skill.

Usage, from the repository root:

    python3 scripts/skill_tree.py            # every skill, all four trees
    python3 scripts/skill_tree.py Signs      # one tree

For each skill it prints the fewest points needed to own rank 1 from an empty
tree (the "Points to reach" column in chapter 21), the skills it unlocks and
every cheapest route. check_plans.py imports the data from here.

Prerequisites were transcribed from WitcherDB's Remastered planner
(https://witcherdb.com/build-planner), read twice with identical results. A
skill unlocks when you own one point in any one of its listed prerequisites;
an empty list marks a starting skill. General links run both ways. The tier
numbers are the row positions from Hack the Minotaur's skill tables and are
only used to sanity-check that Combat, Signs and Alchemy links point upward.
"""
import sys
from collections import deque

# skill: (tier, [prerequisites]); [] = starting skill
COMBAT = {
    "Muscle Memory": (1, []),
    "Arrow Deflection": (1, []),
    "Strength Training": (2, ["Muscle Memory"]),
    "Cold Blood": (2, ["Arrow Deflection"]),
    "Three Strikes": (3, ["Muscle Memory", "Strength Training"]),
    "Resolve": (3, ["Arrow Deflection", "Cold Blood"]),
    "Undying": (4, ["Three Strikes", "Resolve"]),
    "Crushing Blow": (5, ["Strength Training"]),
    "Razor Focus": (5, ["Three Strikes"]),
    "Fleet-Footed": (5, ["Undying"]),
    "Lightning Reflexes": (5, ["Resolve"]),
    "Anatomical Knowledge": (5, ["Cold Blood"]),
    "Whirl": (6, ["Fleet-Footed"]),
    "Rend": (7, ["Razor Focus", "Crushing Blow", "Whirl"]),
    "Counterattack": (7, ["Lightning Reflexes", "Anatomical Knowledge", "Whirl"]),
    "Sunder Armor": (8, ["Crushing Blow"]),
    "Crippling Strike": (8, ["Whirl"]),
    "Maiming Shot": (8, ["Anatomical Knowledge"]),
    "Deadly Precision": (9, ["Rend", "Crippling Strike"]),
    "Flood of Anger": (9, ["Crippling Strike", "Counterattack"]),
}
SIGNS = {
    "Far-Reaching Aard": (1, []),
    "Melt Armor": (1, []),
    "Sustained Glyphs": (1, []),
    "Exploding Shield": (1, []),
    "Delusion": (1, []),
    "Aard Sweep": (2, ["Far-Reaching Aard"]),
    "Firestream": (2, ["Melt Armor"]),
    "Magic Trap": (2, ["Sustained Glyphs"]),
    "Active Shield": (2, ["Exploding Shield"]),
    "Puppetmaster": (2, ["Delusion"]),
    "Supercharged Glyphs": (3, ["Firestream", "Magic Trap", "Active Shield"]),
    "Shockwave": (4, ["Aard Sweep", "Firestream", "Magic Trap"]),
    "Domination": (4, ["Magic Trap", "Active Shield", "Puppetmaster"]),
    "Catalyst": (5, ["Supercharged Glyphs", "Shockwave"]),
    "Fortify Signs": (5, ["Supercharged Glyphs", "Domination"]),
    "Chain Reaction": (6, ["Catalyst", "Fortify Signs"]),
    "Focus": (7, ["Catalyst"]),
    "Sidestep": (7, ["Fortify Signs"]),
    "Aftershock": (8, ["Chain Reaction", "Focus", "Sidestep"]),
    "Resonance": (9, ["Aftershock"]),
}
ALCHEMY = {
    "Refreshment": (1, []),
    "Efficiency": (1, []),
    "Frenzy": (1, []),
    "Adaptability": (2, ["Refreshment"]),
    "Endure Pain": (2, ["Frenzy"]),
    "Pyrotechnics": (3, ["Refreshment", "Efficiency", "Adaptability"]),
    "Hunter Instinct": (3, ["Refreshment", "Efficiency", "Frenzy"]),
    "Poisoned Blades": (3, ["Efficiency", "Frenzy", "Endure Pain"]),
    "Protective Coating": (4, ["Pyrotechnics"]),
    "Acquired Tolerance": (4, ["Hunter Instinct"]),
    "Toxic Shock": (4, ["Poisoned Blades"]),
    "Tissue Transmutation": (5, ["Protective Coating", "Acquired Tolerance", "Toxic Shock"]),
    "Delayed Recovery": (6, ["Tissue Transmutation"]),
    "High Tolerance": (6, ["Tissue Transmutation"]),
    "Volatile Compound": (7, ["Delayed Recovery", "Protective Coating"]),
    "Debilitating Poison": (7, ["Toxic Shock", "High Tolerance"]),
    "Fast Metabolism": (8, ["Delayed Recovery", "High Tolerance"]),
    "Cluster Bombs": (9, ["Volatile Compound"]),
    "Side Effects": (9, ["Fast Metabolism"]),
    "Potent Sting": (9, ["Debilitating Poison"]),
}
GENERAL = {
    "Cat School Techniques": (1, []),
    "Battle Frenzy": (2, ["Cat School Techniques", "Strong Back"]),
    "Wolf School Techniques": (2, []),
    "Adrenaline Burst": (2, ["Cat School Techniques", "Survival Instinct"]),
    "Attack Is the Best Defense": (3, ["Cat School Techniques", "Bear School Techniques", "Wolf School Techniques", "Strong Back"]),
    "Sun and Stars": (3, ["Cat School Techniques", "Bear School Techniques", "Wolf School Techniques", "Survival Instinct"]),
    "Strong Back": (4, ["Attack Is the Best Defense", "Battle Frenzy", "Gourmand"]),
    "Bear School Techniques": (4, []),
    "Survival Instinct": (4, ["Anger Management", "Sun and Stars", "Adrenaline Burst"]),
    "Gourmand": (5, ["Griffin School Techniques", "Bear School Techniques", "Strong Back", "Elemental Attunement"]),
    "Anger Management": (5, ["Griffin School Techniques", "Bear School Techniques", "Survival Instinct", "Synergy"]),
    "Elemental Attunement": (6, ["Advanced Pyrotechnics", "Gourmand", "Element of Surprise"]),
    "Griffin School Techniques": (6, []),
    "Synergy": (6, ["Metabolic Boost", "Metabolic Control", "Anger Management"]),
    "Element of Surprise": (7, ["Griffin School Techniques", "Manticore School Techniques", "Viper School Techniques", "Elemental Attunement"]),
    "Metabolic Control": (7, ["Griffin School Techniques", "Manticore School Techniques", "Viper School Techniques", "Synergy"]),
    "Advanced Pyrotechnics": (8, ["Viper School Techniques", "Elemental Attunement"]),
    "Manticore School Techniques": (8, []),
    "Metabolic Boost": (8, ["Viper School Techniques", "Synergy"]),
    "Viper School Techniques": (9, []),
}

TREES = {"Combat": COMBAT, "Signs": SIGNS, "Alchemy": ALCHEMY, "General": GENERAL}
TWO_WAY = {"General"}


def tree_of(skill):
    """Name of the tree that contains `skill`; KeyError if it's not a 5.0 skill."""
    for name, tree in TREES.items():
        if skill in tree:
            return name
    raise KeyError(skill)


def links(tree_name):
    """skill -> set of skills that owning it unlocks."""
    tree = TREES[tree_name]
    out = {s: set() for s in tree}
    for skill, (_, prereqs) in tree.items():
        for p in prereqs:
            out[p].add(skill)
            if tree_name in TWO_WAY:
                out[skill].add(p)
    return out


def neighbours(skill):
    """Every skill whose ownership unlocks `skill` (both directions in General)."""
    name = tree_of(skill)
    prereqs = set(TREES[name][skill][1])
    if name in TWO_WAY:
        prereqs |= {s for s, (_, pre) in TREES[name].items() if skill in pre}
    return prereqs


def is_start(skill):
    return not TREES[tree_of(skill)][skill][1]


def is_unlocked(skill, owned):
    """True if `skill` can take its first point given the skills in `owned`."""
    return is_start(skill) or bool(neighbours(skill) & set(owned))


def cheapest(tree_name):
    """(cost, parents): fewest points to own rank 1 of each skill, and the
    predecessors on every cheapest route."""
    tree = TREES[tree_name]
    unlocks = links(tree_name)
    starts = [s for s, (_, pre) in tree.items() if not pre]
    cost = {s: 1 for s in starts}
    parents = {s: [] for s in starts}
    queue = deque(starts)
    while queue:
        u = queue.popleft()
        for v in sorted(unlocks[u]):
            if v in starts:
                continue
            if v not in cost:
                cost[v] = cost[u] + 1
                parents[v] = [u]
                queue.append(v)
            elif cost[v] == cost[u] + 1 and u not in parents[v]:
                parents[v].append(u)
    missing = set(tree) - set(cost)
    assert not missing, f"unreachable skills in {tree_name}: {missing}"
    return cost, parents


def points_to_reach():
    """skill -> fewest points to own rank 1, across all four trees."""
    out = {}
    for name in TREES:
        out.update(cheapest(name)[0])
    return out


def sanity_check():
    """Every prerequisite exists in its tree, one-way links point to a lower
    tier, and two-way General links are listed on both sides."""
    problems = []
    for name, tree in TREES.items():
        for skill, (tier, prereqs) in tree.items():
            for p in prereqs:
                if p not in tree:
                    problems.append(f"{name}: {skill} lists unknown prerequisite {p}")
                elif name in TWO_WAY:
                    if tree[p][1] and skill not in tree[p][1]:
                        problems.append(f"{name}: {skill} lists {p}, but {p} doesn't list {skill}")
                elif tree[p][0] >= tier:
                    problems.append(f"{name}: {p} (tier {tree[p][0]}) unlocks {skill} (tier {tier})")
    return problems


def report(tree_name):
    cost, parents = cheapest(tree_name)
    unlocks = links(tree_name)

    def routes(v):
        if not parents[v]:
            return [[v]]
        return [r + [v] for p in parents[v] for r in routes(p)]

    print(f"== {tree_name}")
    for skill in TREES[tree_name]:
        print(f"  {skill}: {cost[skill]} point(s) to reach; unlocks {', '.join(sorted(unlocks[skill])) or 'nothing'}")
        print(f"      cheapest: {' | '.join(' > '.join(r) for r in routes(skill))}")


if __name__ == "__main__":
    for problem in sanity_check():
        print("!!", problem)
    for name in (sys.argv[1:] or TREES):
        report(name)
