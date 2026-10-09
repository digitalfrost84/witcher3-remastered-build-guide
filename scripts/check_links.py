"""Check the book's internal links, section anchors, tables and images.

Usage, from the repository root:

    python3 scripts/check_links.py

It checks both READMEs and every chapter for:

- relative links whose file doesn't exist;
- links to a #section that no heading in the target file produces (GitHub's
  anchor rules: lowercase, punctuation dropped, spaces become hyphens);
- table rows whose cell count differs from their header row;
- images in images/ that nothing references, and references to images that
  don't exist.

Web links aren't fetched. Exit status is 1 if anything fails.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def slug(heading):
    heading = heading.strip().lower()
    heading = re.sub(r"[^\w\- ]", "", heading)
    return heading.replace(" ", "-")


def main():
    files = [ROOT / "README.md", ROOT / "scripts" / "README.md"] + sorted((ROOT / "chapters").glob("*.md"))
    anchors = {}
    for f in files:
        text = f.read_text(encoding="utf-8")
        anchors[f.resolve()] = {slug(m.group(2)) for m in re.finditer(r"^(#{1,6}) (.+)$", text, re.M)}

    problems = []
    used_images = set()
    for f in files:
        text = f.read_text(encoding="utf-8")
        name = f.relative_to(ROOT)
        for m in re.finditer(r"\]\(([^)\s]+)\)", text):
            url = m.group(1)
            if url.startswith(("http://", "https://", "mailto:")):
                continue
            path, _, fragment = url.partition("#")
            target = (f.parent / path).resolve() if path else f.resolve()
            if not target.exists():
                problems.append(f"{name}: link to missing file {url}")
                continue
            if fragment and target.suffix == ".md" and fragment not in anchors.get(target, set()):
                problems.append(f"{name}: link to missing section {url}")
        used_images |= set(re.findall(r"images/([\w\-]+\.png)", text))

        lines = text.split("\n")
        i = 0
        while i < len(lines):
            if lines[i].startswith("|") and i + 1 < len(lines) and re.match(r"^\|[\s\-:|]+\|$", lines[i + 1]):
                width = lines[i].count("|") - lines[i].count("\\|")
                j = i + 2
                while j < len(lines) and lines[j].startswith("|"):
                    cells = lines[j].count("|") - lines[j].count("\\|")
                    if cells != width:
                        problems.append(f"{name}, line {j + 1}: table row has {cells - 1} cells, the header has {width - 1}")
                    j += 1
                i = j
            else:
                i += 1

    images = {p.name for p in (ROOT / "images").glob("*.png")}
    for missing in sorted(used_images - images):
        problems.append(f"referenced image doesn't exist: images/{missing}")
    for unused in sorted(images - used_images):
        problems.append(f"image isn't referenced anywhere: images/{unused}")

    for p in problems:
        print("!!", p)
    print(f"{len(files)} files checked: " + ("OK" if not problems else f"{len(problems)} problem(s)"))
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
