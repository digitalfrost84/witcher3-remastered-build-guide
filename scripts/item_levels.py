"""Compute the required level of every armor piece and sword from the definitions.

Usage:

    python3 scripts/item_levels.py <extracted-root> [name-filter ...]

The game doesn't store an item's level. `CInventoryComponent.GetItemLevel`
(game/components/inventoryComponent.ws) and `W3GameParams.GetItemLevel`
(game/gameParams.ws) derive it from one stat:

- chest: floor(1 + (armor - 25) / 5); boots and trousers: floor(1 + (armor - 5) / 2);
  gloves: floor(1 + (armor - 1) / 2);
- steel sword: ceil(1 + (1 + sum(damage - 1) - 25) / 8) over its seven damage types;
  silver sword: ceil(1 + (1 + sum(damage - 1) - 90) / 10) over its six;
- then -1 for every item, -2 more for witcher gear (quality 5), -1 more for
  relics (quality 4) and a further -1 for Hearts of Stone witcher or relic gear
  (tag EP1), minimum 1.

`armor` and the damage values are the summed `base` entries of the item's base
abilities. Prints category, level, quality and name, tab-separated, for every
item whose name contains one of the filters (all items if none are given).
New Game+ copies (the abilities_plus and items_plus folders) are skipped; New
Game+ items inside the normal files carry an NGP prefix or a `newgame`
localisation key (Manticore's tier 2).
"""
import math
import os
import re
import sys

root = sys.argv[1]
filters = sys.argv[2:]

abilities = {}
items = []
item_re = re.compile(r'<item\s+(.*?)>(.*?)</item>', re.S)
abil_re = re.compile(r'<ability\s+name="([^"]+)"[^>]*>(.*?)</ability>', re.S)
attr_re = re.compile(r'<(\w+)\s+([^>]*?)/?>')

for dp, _, fs in os.walk(root):
    if '_plus' in dp:
        continue
    for f in fs:
        if not f.endswith('.xml'):
            continue
        text = open(os.path.join(dp, f), encoding='utf-8', errors='replace').read()
        text = re.sub(r'<!--.*?-->', '', text, flags=re.S)
        for m in abil_re.finditer(text):
            stats = {}
            for a in attr_re.finditer(m.group(2)):
                t = re.search(r'type="(\w+)"', a.group(2))
                v = re.search(r'min="([-\d.]+)"', a.group(2))
                if t and v:
                    stats.setdefault(a.group(1), {}).setdefault(t.group(1), 0.0)
                    stats[a.group(1)][t.group(1)] += float(v.group(1))
            abilities.setdefault(m.group(1), stats)
        for m in item_re.finditer(text):
            head = m.group(1)
            name = re.search(r'\bname\s*=\s*"([^"]+)"', head)
            cat = re.search(r'\bcategory\s*=\s*"([^"]+)"', head)
            if not name or not cat:
                continue
            base = re.search(r'<base_abilities>(.*?)</base_abilities>', m.group(2), re.S)
            abs_ = re.findall(r'<a>([^<]+)</a>', base.group(1)) if base else []
            tags = re.search(r'<tags>(.*?)</tags>', m.group(2), re.S)
            items.append((name.group(1), cat.group(1), abs_, tags.group(1) if tags else ''))


def stat(abs_, attr, kind):
    return sum(abilities.get(a, {}).get(attr, {}).get(kind, 0.0) for a in abs_)


STEEL = ['SlashingDamage', 'BludgeoningDamage', 'RendingDamage', 'ElementalDamage', 'FireDamage', 'SilverDamage', 'PiercingDamage']
SILVER = ['SilverDamage', 'BludgeoningDamage', 'RendingDamage', 'ElementalDamage', 'FireDamage', 'PiercingDamage']

seen = set()
for name, cat, abs_, tags in items:
    if filters and not any(x.lower() in name.lower() for x in filters):
        continue
    if (name, cat) in seen:
        continue
    seen.add((name, cat))
    armor = stat(abs_, 'armor', 'base')
    if cat == 'armor':
        level = math.floor(1 + (armor - 25) / 5)
    elif cat in ('boots', 'pants'):
        level = math.floor(1 + (armor - 5) / 2)
    elif cat == 'gloves':
        level = math.floor(1 + (armor - 1) / 2)
    elif cat == 'steelsword':
        s = sum(stat(abs_, d, 'base') - 1 for d in STEEL)
        level = math.ceil(1 + (1 + s - 25) / 8)
    elif cat == 'silversword':
        s = sum(stat(abs_, d, 'base') - 1 for d in SILVER)
        level = math.ceil(1 + (1 + s - 90) / 10)
    else:
        continue
    level = max(level - 1, 1)
    quality = round(stat(abs_, 'quality', 'add') + stat(abs_, 'quality', 'base'))
    if quality == 5:
        level -= 2
    elif quality == 4:
        level -= 1
    level = max(level, 1)
    if quality in (4, 5) and re.search(r'\bEP1\b', tags):
        level -= 1
    print(f'{cat}\t{level}\tq{quality}\t{name}')
