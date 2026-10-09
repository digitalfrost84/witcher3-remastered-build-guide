"""Apply a batch of exact text replacements to the book, all or nothing.

Usage, from the repository root:

    python3 scripts/apply_edits.py my_edits.py

my_edits.py defines a list named EDITS of (file, old, new) tuples, with file
paths relative to the repository root:

    EDITS = [
        ("chapters/04-alchemy.md",
         "| **Blizzard** | ... | 25 |",
         "| **Blizzard** | ... | 20 |"),
    ]

Every `old` string must occur exactly once in its file, after the earlier
edits to that file have been applied. If any of them doesn't, nothing is
written and the script lists the failures, so a stale or ambiguous edit can't
half-apply. Keep edit files outside the repository; they're one-off data.
"""
import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def load(edit_file):
    spec = importlib.util.spec_from_file_location("edits", edit_file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.EDITS


def main(args):
    if len(args) != 1:
        print(__doc__)
        return 2
    edits = load(args[0])
    texts, failures = {}, []
    for number, (name, old, new) in enumerate(edits, 1):
        path = ROOT / name
        if name not in texts:
            if not path.exists():
                failures.append(f"edit {number}: {name} doesn't exist")
                continue
            texts[name] = path.read_text(encoding="utf-8")
        count = texts[name].count(old)
        if count != 1:
            failures.append(f"edit {number}: {name}: expected 1 match, found {count}: {old[:70]!r}")
            continue
        texts[name] = texts[name].replace(old, new)
    if failures:
        print("\n".join(failures))
        print(f"nothing written: {len(failures)} of {len(edits)} edits failed")
        return 1
    for name, text in texts.items():
        (ROOT / name).write_text(text, encoding="utf-8")
    print(f"applied {len(edits)} edits to {len(texts)} file(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
