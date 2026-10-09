# Scripts

The code used to build and check the book. Run everything from the repository root with Python 3.9 or later; each script's docstring has the details. Only `charts.py` needs a package (matplotlib); the rest use the standard library.

## Editing the book

| Script | What it does | When to run it |
| --- | --- | --- |
| [`check_links.py`](check_links.py) | Checks internal links, section anchors, table cell counts and image references in both READMEs and every chapter | After any edit |
| [`check_plans.py`](check_plans.py) | Reads the skill plans in chapters 8 to 13 and checks prerequisites, ranks and point totals against the 5.0 skill trees; also checks chapter 21's "Points to reach" column | After changing a skill plan or the skill reference |
| [`skill_tree.py`](skill_tree.py) | The 5.0 prerequisite links and the cheapest route to every skill | When planning a build or a new phase table |
| [`apply_edits.py`](apply_edits.py) | Applies a batch of exact text replacements across chapters, all or nothing | For corrections that touch many chapters at once |
| [`charts.py`](charts.py) | Rebuilds every chart in `images/` from the numbers in its source, each with its source noted | After changing a number that a chart shows |

```sh
python3 scripts/check_links.py
python3 scripts/check_plans.py
python3 scripts/skill_tree.py Alchemy
python3 scripts/apply_edits.py ~/my_edits.py
python3 scripts/charts.py                  # rewrites images/
```

`check_links.py` and `check_plans.py` print `OK` and exit with status 0 when everything passes, so they can run before every commit.

**Charts.** `charts.py` writes into `images/`, or into a folder you pass it. It uses the Inter font when it's installed and falls back to DejaVu Sans, which changes text widths. Different matplotlib versions also write slightly different bytes, so a rebuild can mark PNGs as changed even when they look the same: look at them before committing.

## Reproducing the file audits

| Script | What it does |
| --- | --- |
| [`unbundle.py`](unbundle.py) | Extracts files from the game's `.bundle` archives and checks each one's size and CRC32. |
| [`attr_table.py`](attr_table.py) | Lists every ability in the extracted XML that defines a given attribute, with its type, value and line. |
| [`cr2w_calls.py`](cr2w_calls.py) | Shows the script calls in a quest graph (`.w2phase`), with their comments and properties. |
| [`count_recipes.py`](count_recipes.py) | Counts the alchemy recipes Acquired Tolerance can use, per rank. |
| [`item_levels.py`](item_levels.py) | Computes every armor piece's and sword's required level from its stats, the way the game does. |
| [`buff_immunities.py`](buff_immunities.py) | Lists the effect immunities in creature templates (`.w2ent`), such as which monsters are immune to poison or burning. |

The audits in [chapter 19](../chapters/19-the-maths.md#file-evidence-and-reproducibility) read build `5.0.0.1048522`. To repeat them against your own install (`<game>` is the game folder):

```bash
python3 -I scripts/unbundle.py "<game>/content/content0/bundles/xml.bundle" extracted/xml
python3 -I scripts/unbundle.py "<game>/content/content0/bundles/ep1.bundle" extracted/ep1 .xml
python3 -I scripts/unbundle.py "<game>/content/content0/bundles/bob.bundle" extracted/bob .xml
python3 -I scripts/attr_table.py extracted poison_resistance_perc
python3 -I scripts/count_recipes.py extracted
python3 -I scripts/item_levels.py extracted Gryphon Lynx
python3 -I scripts/unbundle.py "<game>/content/content0/bundles/blob.bundle" extracted/ent npc_entities/monsters
python3 -I scripts/buff_immunities.py extracted/ent "<game>/content/content0/scripts" EET_Poison
```

Free-DLC gear (the Wolven tiers, the Temerian, Nilfgaardian and Undvik sets) lives in `dlc0.bundle`; extract its `.xml` files too before running `item_levels.py`. For `buff_immunities.py`, repeat the template extraction for `bob.bundle`, `ep1.bundle` and `dlc0.bundle`.

The game scripts need no extraction: they ship as plain `.ws` files in `<game>/content/content0/scripts/`. Mods installed in `<game>/mods` can override both definitions and scripts, so the audits read only the vanilla bundles.
