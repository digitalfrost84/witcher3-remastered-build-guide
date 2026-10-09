"""List every ability that defines one attribute, across extracted XML.

Usage:

    python3 scripts/attr_table.py <extracted-root> <attribute> [--include-plus]

Prints one tab-separated row per definition: ability name, type (base, mult
or add), value and file:line. New Game+ copies (abilities_plus, items_plus)
are skipped unless --include-plus is given. Chapter 19 used it for the
poison-resistance list (poison_resistance_perc) and to show that no
definition gives critical_hit_damage_bonus a base value.
"""
import os, re, sys

root, attr = sys.argv[1], sys.argv[2]
plus = '--include-plus' in sys.argv
abil_re = re.compile(r'<ability\s+name="([^"]+)"')
attr_re = re.compile(r'<%s\b([^>]*)>' % re.escape(attr))
for dp, _, fs in os.walk(root):
    if not plus and '_plus' in dp:
        continue
    for f in fs:
        if not f.endswith('.xml'):
            continue
        p = os.path.join(dp, f)
        cur = None
        for ln, line in enumerate(open(p, encoding='utf-8', errors='replace'), 1):
            m = abil_re.search(line)
            if m:
                cur = m.group(1)
            for a in attr_re.finditer(line):
                t = re.search(r'type="(\w+)"', a.group(1))
                v = re.search(r'min="([-\d.]+)"', a.group(1))
                print('%s\t%s\t%s\t%s:%d' % (cur, t.group(1) if t else '?', v.group(1) if v else '?',
                                            os.path.relpath(p, root).replace('\\', '/'), ln))
