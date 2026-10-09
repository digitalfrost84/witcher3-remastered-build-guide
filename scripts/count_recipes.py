"""Count the alchemy recipes that Acquired Tolerance can use.

Usage:

    python3 scripts/count_recipes.py <extracted folder> [more folders or files]

Give it the folders you extracted with scripts/unbundle.py (the base game's
xml.bundle and both expansions'). It finds every def_item_alchemy_recipes_*.xml
below them, skips the New Game+ copies (folders ending in _plus) and
commented-out entries, and prints how many recipes each Acquired Tolerance
rank counts.

The rule it applies comes from the 5.0 scripts (chapter 19): Acquired
Tolerance adds 0.5 maximum Toxicity per learned recipe whose level is at most
its rank, and it skips bolts, dyes and any type the game doesn't recognize.
The result is the number of recipe definitions, an upper bound on what a
playthrough can learn. For build 5.0.0.1048522 it prints 109 / 141 / 173.
"""
import collections
import re
import sys
from pathlib import Path

# cookedItemType strings the game maps to a real type (alchemyTypes.ws); bolt and
# dye are real types that Acquired Tolerance skips, anything else is "Undefined"
ELIGIBLE = {"potion", "petard", "oil", "Substance", "mutagen_potion", "alcohol", "quest"}


def recipe_files(args):
    for arg in args:
        path = Path(arg)
        if path.is_dir():
            yield from sorted(p for p in path.rglob("def_item_alchemy_recipes_*.xml")
                              if not any(part.endswith("_plus") for part in p.parts))
        else:
            yield path


def recipes(path):
    text = path.read_text(encoding="utf-8-sig", errors="replace")
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    for section in re.findall(r"<alchemy_recipes>(.*?)</alchemy_recipes>", text, flags=re.S):
        for tag in re.findall(r"<recipe\b(.*?)>", section, flags=re.S):
            yield dict(re.findall(r'(\w+)\s*=\s*"([^"]*)"', tag))


def main(args):
    if not args:
        print(__doc__)
        return 2
    found, by_kind = [], collections.Counter()
    for path in recipe_files(args):
        rows = list(recipes(path))
        print(f"{path}: {len(rows)} recipes")
        found += rows
    names = collections.Counter(r.get("name_name") for r in found)
    duplicates = sorted(n for n, c in names.items() if c > 1)
    for r in found:
        by_kind[(r.get("cookedItemType"), r.get("level"))] += 1

    print("\nBy type and level:")
    for (kind, level), count in sorted(by_kind.items(), key=lambda kv: (str(kv[0][0]), str(kv[0][1]))):
        flag = "" if kind in ELIGIBLE else "  (not counted)"
        print(f"  {kind:15s} level {level}: {count}{flag}")

    unique = {}
    for r in found:
        unique.setdefault(r.get("name_name"), r)  # the player learns a recipe name once
    print("\nAcquired Tolerance:")
    for rank in (1, 2, 3):
        n = sum(1 for r in unique.values() if r.get("cookedItemType") in ELIGIBLE and int(r.get("level", 99)) <= rank)
        print(f"  rank {rank}: {n} eligible recipes, at most +{n * 0.5:g} maximum Toxicity")
    if duplicates:
        print("\nRecipe names defined more than once (counted once):", ", ".join(duplicates))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
