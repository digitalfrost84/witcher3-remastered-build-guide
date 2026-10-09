"""List the buff immunities in creature templates (.w2ent, CR2W format).

Usage:

    python3 scripts/buff_immunities.py <extracted-root> <game-scripts-dir> [EffectType]

<game-scripts-dir> is <game>/content/content0/scripts; the effect types are
stored as numbers, and the script reads their names from the EEffectType enum
in game/gameplay/effects/effectTypes.ws.

Creature immunities don't live in the XML. `CActor.IsImmuneToBuff`
(game/actor.ws) asks `theGame.GetBuffImmunitiesForActor`, which reads the
CBuffImmunityParam objects in the creature's entity template: an `immunityTo`
list of effect types plus flags for whole groups (potion, positive, neutral,
negative, immobilize, confuse, damage). This prints one line per template:
the template path, the group flags that are set and the listed effect types.
With an effect type such as EET_Poison it prints only the templates immune to
it, either by name or through a group flag. The poison effect is a "damage"
and "negative" effect, so those two flags count for it.

Extract the templates first, for example:

    python3 -I scripts/unbundle.py "<game>/content/content0/bundles/blob.bundle" extracted/ent npc_entities/monsters

and the same for bob.bundle, ep1.bundle and dlc0.bundle.
"""
import os
import re
import struct
import sys

GROUP_FLAGS = ('potion', 'positive', 'neutral', 'negative', 'immobilize', 'confuse', 'damage')
# effect type -> group flags that also make an actor immune to it (effectTypes.ws, GetEffectTypeFlags)
FLAGS_FOR = {'EET_Poison': ('negative', 'damage'), 'EET_PoisonCritical': ('negative', 'damage')}


def effect_names(scripts_dir):
    text = open(os.path.join(scripts_dir, 'game', 'gameplay', 'effects', 'effectTypes.ws'),
                encoding='utf-8', errors='replace').read()
    body = re.sub(r'//.*', '', re.search(r'enum EEffectType\s*\{(.*?)\}', text, re.S).group(1))
    names, value = {}, -1
    for item in (x.strip() for x in body.split(',')):
        if not item:
            continue
        if '=' in item:
            item, v = (y.strip() for y in item.split('='))
            value = int(v, 0)
        else:
            value += 1
        names[value] = item
    return names


def read(path, eet):
    d = open(path, 'rb').read()
    if d[:4] != b'CR2W':
        return []
    tables = [struct.unpack_from('<III', d, 0x28 + 12 * i) for i in range(10)]
    s_off, s_size, _ = tables[0]
    strings = d[s_off:s_off + s_size]
    n_off, n_cnt, _ = tables[1]
    names = []
    for i in range(n_cnt):
        o = struct.unpack_from('<I', d, n_off + 8 * i)[0]
        names.append(strings[o:strings.index(b'\0', o)].decode('latin1'))
    e_off, e_cnt, _ = tables[4]
    found = []
    for i in range(e_cnt):
        cls, _, _, size, off, _, _ = struct.unpack_from('<HHIIIII', d, e_off + 24 * i)
        if names[cls] != 'CBuffImmunityParam':
            continue
        buf, p = d[off:off + size], 1
        flags, effects = [], []
        while p + 8 <= len(buf):
            ni, ti, sz = struct.unpack_from('<HHI', buf, p)
            if ni == 0 or ni >= len(names):
                break
            val = buf[p + 8:p + 4 + sz]
            prop = names[ni]
            if prop == 'immunityTo' and len(val) >= 4:
                count = struct.unpack_from('<I', val, 0)[0]
                for k in range(count):
                    v = struct.unpack_from('<i', val, 4 + 4 * k)[0]
                    effects.append(eet.get(v, str(v)))
            elif prop in GROUP_FLAGS and val[:1] == b'\x01':
                flags.append(prop)
            p += 4 + sz
        found.append((flags, effects))
    return found


def main(root, scripts_dir, effect=None):
    eet = effect_names(scripts_dir)
    for dp, _, fs in os.walk(root):
        for f in sorted(fs):
            if not f.endswith('.w2ent'):
                continue
            path = os.path.join(dp, f)
            flags, effects = set(), set()
            for fl, ef in read(path, eet):
                flags.update(fl)
                effects.update(ef)
            if not flags and not effects:
                continue
            if effect and effect not in effects and not flags & set(FLAGS_FOR.get(effect, ())):
                continue
            rel = os.path.relpath(path, root).replace('\\', '/')
            print(f"{rel}\t{','.join(sorted(flags))}\t{','.join(sorted(effects))}")


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
