"""Check the skill plans in the school chapters against the 5.0 skill trees.

Usage, from the repository root:

    python3 scripts/check_plans.py

It reads the "Skills by phase" tables in chapters 8 to 13 straight from the
Markdown, so it always checks what the book says. For every row it checks
that:

- the skill exists and sits in the tree the row names;
- a first point is only bought once a prerequisite is owned, and the
  Requires column names a real link ("start" for starting skills, "—" for a
  rank-up of a skill already owned);
- ranks only go up and never past 3;
- the running point total matches the phase heading ("the first 12 points",
  "to 28 points").

It also checks a "| Phase | Combat | Signs | Alchemy | General | Total |"
table when a chapter has one, and the "Points to reach" column of the
chapter 21 skill reference. Late-game bullet lists are free text and aren't
checked. Exit status is 1 if anything fails.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import skill_tree  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
SCHOOLS = ["08-feline.md", "09-griffin.md", "10-ursine.md", "11-wolven.md", "12-manticore.md", "13-viper.md"]
DASHES = {"—", "-", "–"}


def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def tables_after_headings(text, section):
    """Yield (heading, rows) for every ### heading inside `## section` that is
    followed by a skill table."""
    body = text.split(f"## {section}", 1)[1]
    body = re.split(r"\n## ", body, maxsplit=1)[0]
    for block in re.split(r"\n(?=### )", body):
        lines = block.strip().splitlines()
        if not lines or not lines[0].startswith("### "):
            continue
        heading = lines[0][4:].strip()
        rows, in_table = [], False
        for line in lines[1:]:
            if line.startswith("| Skill | Tree | Rank | Requires"):
                in_table = True
                continue
            if in_table:
                if not line.startswith("|"):
                    break
                if set(line.replace("|", "").strip()) <= set("-: "):
                    continue
                rows.append(cells(line))
        if rows:
            yield heading, rows


def check_school(path):
    text = path.read_text(encoding="utf-8")
    problems = []
    owned = {}
    per_tree = {t: 0 for t in skill_tree.TREES}
    phase_totals = []
    for heading, rows in tables_after_headings(text, "Skills by phase"):
        for skill, tree, rank, requires, *_ in rows:
            where = f"{path.name}, {heading}, {skill} {rank}"
            try:
                actual_tree = skill_tree.tree_of(skill)
            except KeyError:
                problems.append(f"{where}: not a 5.0 skill name")
                continue
            if tree != actual_tree:
                problems.append(f"{where}: listed under {tree}, but it's a {actual_tree} skill")
            rank = int(rank)
            current = owned.get(skill, 0)
            if rank <= current:
                problems.append(f"{where}: already at rank {current}")
                continue
            if rank > 3:
                problems.append(f"{where}: ranks stop at 3")
            if current == 0:
                if not skill_tree.is_unlocked(skill, owned):
                    problems.append(f"{where}: bought before any prerequisite ({', '.join(sorted(skill_tree.neighbours(skill)))})")
                if requires == "start" and not skill_tree.is_start(skill):
                    problems.append(f"{where}: marked as a starting skill, but it isn't one")
                elif requires in DASHES:
                    problems.append(f"{where}: Requires says rank-up, but it's the first point")
                elif requires not in ("start",) and not skill_tree.is_start(skill):
                    named = {r.strip() for r in re.split(r",| or ", requires) if r.strip()}
                    unknown = named - skill_tree.neighbours(skill)
                    if unknown:
                        problems.append(f"{where}: Requires names {', '.join(sorted(unknown))}, which doesn't link to it")
                    elif not named & set(owned):
                        problems.append(f"{where}: Requires names {requires}, which isn't owned yet")
            elif requires not in DASHES:
                problems.append(f"{where}: a rank-up should say — in Requires")
            per_tree[actual_tree] += rank - current
            owned[skill] = rank
        total = sum(per_tree.values())
        phase_totals.append((heading, dict(per_tree), total))
        target = re.search(r"(?:first|to) (\d+) points", heading)
        if target and int(target.group(1)) != total:
            problems.append(f"{path.name}, {heading}: the tables add up to {total} points, the heading says {target.group(1)}")

    # an optional cumulative table: | Phase | Combat | Signs | Alchemy | General | Total |
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("| Phase | Combat | Signs | Alchemy | General | Total |"):
            for row, (heading, trees, total) in zip(
                    (cells(l) for l in lines[i + 2:] if l.startswith("|")), phase_totals):
                expected = [trees["Combat"], trees["Signs"], trees["Alchemy"], trees["General"], total]
                if [int(x) for x in row[1:6]] != expected:
                    problems.append(f"{path.name}: cumulative table row '{row[0]}' says {row[1:6]}, the plan gives {expected} ({heading})")
            break
    return problems, phase_totals


def check_reference():
    """Chapter 21's 'Points to reach' column against the computed cheapest routes."""
    path = ROOT / "chapters" / "21-skill-reference.md"
    expected = skill_tree.points_to_reach()
    problems, seen = [], set()
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"\| \*\*(.+?)\*\* \| (.+?) \| (\d+) \|", line)
        if not m:
            continue
        skill, points = m.group(1), int(m.group(3))
        seen.add(skill)
        if skill not in expected:
            problems.append(f"21-skill-reference.md: {skill} is not in the skill-tree data")
        elif expected[skill] != points:
            problems.append(f"21-skill-reference.md: {skill} says {points} points to reach, the tree gives {expected[skill]}")
    missing = set(expected) - seen
    if missing:
        problems.append(f"21-skill-reference.md: no row for {', '.join(sorted(missing))}")
    return problems


def main():
    problems = skill_tree.sanity_check()
    for name in SCHOOLS:
        found, totals = check_school(ROOT / "chapters" / name)
        problems += found
        summary = "; ".join(f"{h.split(':')[0]} {t}" for h, _, t in totals)
        print(f"{name}: {summary}")
    problems += check_reference()
    for p in problems:
        print("!!", p)
    print("OK" if not problems else f"{len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
