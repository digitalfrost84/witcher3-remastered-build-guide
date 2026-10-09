# Scripts

The code used to build the book. Run everything from the repository root; each script's docstring has the details.

| Script | What it does |
| --- | --- |
| `charts.py` | Rebuilds every chart in `images/`. Needs matplotlib and, for matching output, the Inter font. |
| `unbundle.py` | Extracts files from the game's `.bundle` archives and checks each one's size and CRC32. |
| `attr_table.py` | Lists every ability in the extracted XML that defines a given attribute, with its type, value and line. |
| `cr2w_calls.py` | Shows the script calls in a quest graph (`.w2phase`), with their comments and properties. |

## Reproducing the file audits

The audits in [chapter 19](../chapters/19-the-maths.md#file-evidence-and-reproducibility) read build `5.0.0.1048522`. To repeat them against your own install (`<game>` is the game folder):

```bash
python3 -I scripts/unbundle.py "<game>/content/content0/bundles/xml.bundle" extracted/xml
python3 -I scripts/unbundle.py "<game>/content/content0/bundles/ep1.bundle" extracted/ep1 .xml
python3 -I scripts/unbundle.py "<game>/content/content0/bundles/bob.bundle" extracted/bob .xml
python3 -I scripts/attr_table.py extracted poison_resistance_perc
```

The game scripts need no extraction: they ship as plain `.ws` files in `<game>/content/content0/scripts/`. Mods installed in `<game>/mods` can override both definitions and scripts, so the audits read only the vanilla bundles.
