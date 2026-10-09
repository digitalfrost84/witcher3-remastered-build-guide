# 2. The 5.0 skill system

Patch 5.0 threw out the old skill grid. Skills now sit in **four trees of 20 skills each**, every skill has **three ranks**, and a skill unlocks once you own a skill connected to it, not after you've spent a set number of points in that tree ([CD PROJEKT RED: What's new](https://www.thewitcher.com/us/en/news/52041/see-whats-new-in-the-witcher-3-wild-hunt-remastered); [witcherhour.com](https://witcherhour.com/skills/)). If you load an old save, all your skill points come back to spend again.

Two consequences matter most:

- **Paths are cheap.** Rank 1 of a skill is enough to open the next one, so you can reach deep skills quickly. Whirl, for example, costs five points: Muscle Memory, Three Strikes, Undying, Fleet-Footed, Whirl ([witcherhour.com calculator](https://witcherhour.com/witcher-3-skill-calculator/)).
- **Old build guides don't translate.** Skills were renamed, moved, rebalanced or removed. Keep an old build's idea, not its shopping list.

## The four trees

| Tree | Color | What it covers | Starting skills (no prerequisite) |
| --- | --- | --- | --- |
| **Combat** | Red | Fast and strong attacks, Adrenaline, Whirl and Rend, the crossbow | Muscle Memory, Arrow Deflection |
| **Signs** | Blue | All five Signs, their alternate modes, and new skills that mix Signs with swords | Far-Reaching Aard, Melt Armor, Sustained Glyphs, Exploding Shield, Delusion |
| **Alchemy** | Green | Potions, decoctions, bombs, oils and a new poison line | Refreshment, Efficiency, Frenzy |
| **General** | None | School Techniques, Vitality, Adrenaline helpers, Synergy, Toxicity limits | All six School Techniques: Cat, Wolf, Bear, Griffin, Manticore, Viper |

Every rank you **equip** also earns its tree a small **branch passive**. Only skills in your slots count, and the always-on core skills don't, so a point in an unslotted skill gives nothing at all:

| Tree | Per equipped rank |
| --- | --- |
| Combat | +0.01 Adrenaline gain (published as +1%) |
| Signs | +0.5 Stamina per second in combat (0.5% of maximum Stamina) |
| Alchemy | +2% potion duration and +2% bomb damage |
| General | +1% maximum Vitality |

Source: the installed 5.0 game files ([chapter 19](19-the-maths.md#9-branch-passives)). [Hack the Minotaur](https://hacktheminotaur.com/the-witcher-3/the-witcher-3-remastered-new-skill-trees-guide/) published the same values but counted every point you spend; witcherhour was right that only equipped skills count.

## What changed from older guides

| Change | Details |
| --- | --- |
| **Removed** | The per-Sign intensity skills, Quen Discharge, Killing Spree, Fixative and Steady Aim |
| **Moved to General** | Synergy, Metabolic Control and Metabolic Boost |
| **Renamed** | Heightened Tolerance became High Tolerance, and it no longer protects you from overdose |
| **New in Alchemy** | A poison line: Poisoned Blades, Toxic Shock, Debilitating Poison, Potent Sting |
| **New in Signs** | Six hybrid skills: Catalyst, Chain Reaction, Focus, Sidestep, Aftershock, Resonance |
| **Reworked** | Deadly Precision now only works with strong attacks; crossbow skills got stronger; Signs, especially Yrden, were buffed |
| **Patch 5.01** | Exploding Shield now also reflects damage; the Synergy value shown in the menu was fixed |

Sources: [witcherhour.com](https://witcherhour.com/skills/), [CD PROJEKT RED: Patch 5.01](https://www.thewitcher.com/us/en/news/52085/patch-5-01-for-the-witcher-3-wild-hunt-remastered-is-live).

## Skill slots and mutagens

Owning a skill isn't enough: **most skills only work while they sit in one of your skill slots**. You get up to **12 slots**, arranged in four groups of three, and each group has a **mutagen slot** beside it.

- **When slots open (file-verified).** By **Ability Points earned**, not by level: one slot from the start, then at 2, 4, 6, 8, 10, 12, 15, 18, 22, 26 and 30 points. The game counts points you've spent, points still unspent and points spent on mutations, so Places of Power, the Magic Acorn and the Golden Egg open slots early. Hack the Minotaur had this right; witcherhour lists the same thresholds as character levels ([Hack the Minotaur](https://hacktheminotaur.com/the-witcher-3/the-witcher-3-remastered-signs-build/); [witcherhour.com](https://witcherhour.com/skills/)).
- **Mutagens.** Red mutagens add attack power, blue add Sign intensity and green add Vitality. Each skill of the matching color in the mutagen's group adds another 100% of its bonus, so a full matching group quadruples it ([Fextralife: Mutagens](https://thewitcher3.wiki.fextralife.com/Mutagens), pre-5.0). Red goes with Combat skills, blue with Signs, green with Alchemy; General skills aren't one of the three colors, so they never boost a mutagen ([Hack the Minotaur](https://hacktheminotaur.com/the-witcher-3/the-witcher-3-remastered-new-skill-trees-guide/)). The General skill Synergy raises every mutagen bonus by 10/20/30%.
- **Mutations** (Blood and Wine) add four more slots that only take skills of the active mutation's color. See chapter 5.

Skills you buy only to unlock something deeper (Sustained Glyphs on the way to Magic Trap, say) don't need a slot. **File-verified:** a skill can be bought once you *own* at least one rank in one of its linked prerequisites; whether that prerequisite is equipped doesn't matter, and the 5.0 skills have no points-spent requirement. Most builds own more skills than they can equip, and that's fine.

**A note on Delusion:** if you want Axii's extra dialogue options, keep Delusion slotted. In 5.0, Hack the Minotaur says the dialogue options are available from rank 1, and witcherhour lists the same effect at every rank ([Hack the Minotaur: Signs](https://hacktheminotaur.com/the-witcher-3/the-witcher-3-signs-and-upgrades-guide/); [witcherhour.com](https://witcherhour.com/skills/)). Before 5.0, most Axii conversations needed level 1 or 2, and level 3 only added experience ([Witcher wiki: Delusion](https://witcher.fandom.com/wiki/Delusion)). Rank 1 is very likely enough now; a second point is cheap insurance if you want to be sure.

## How to plan a build in 5.0

1. **Pick a destination.** Choose the two or three skills that define the build, such as Battle Frenzy for crits or Catalyst for Signs.
2. **Trace the prerequisites back.** Count the stepping stones. Some are good in their own right; some you'll never equip.
3. **Rank the skills your rotation uses.** Additional ranks can strengthen a core skill, but compare them with the new abilities and prerequisites another point could unlock. Chapter 19 explains why the former fixed combo-percentage comparison is not reliable, and why Three Strikes is a poor rank-up for a three-fast/strong loop.
4. **Match your armor.** Your School Technique only counts armor pieces of its weight class (chapter 3).

The diagram shows one finished route, the Wolven hybrid from chapter 11. Arrows run from a prerequisite to the skill it unlocks; darker boxes are bought earlier.

![Prerequisite map of the Wolven hybrid build across all four trees](../images/skill-route.png)

Chapter 21 lists all 80 skills with their prerequisites.

## Respec

- **Potion of Clearance** refunds every skill point. Keira Metz sells it, and it usually costs about 1,000 crowns ([KeenGamer](https://www.keengamer.com/articles/guides/the-witcher-3-remastered-best-builds-for-every-playstyle/); [FinalBoss](https://finalboss.io/the-witcher-3-wild-hunt-how-to-rebuild-the-5-0-skill-tree)).
- **Potion of Restoration** does the same for mutation research (chapter 5).

Because paths are cheap now, a respec around level 30 to pick up a new school, or when you reach Blood and Wine, costs you nothing but crowns.

## Sources

- [CD PROJEKT RED: See what's new in Remastered](https://www.thewitcher.com/us/en/news/52041/see-whats-new-in-the-witcher-3-wild-hunt-remastered)
- [CD PROJEKT RED: Patch 5.01 notes](https://www.thewitcher.com/us/en/news/52085/patch-5-01-for-the-witcher-3-wild-hunt-remastered-is-live)
- [witcherhour.com: Witcher 3 skills](https://witcherhour.com/skills/) and [skill calculator](https://witcherhour.com/witcher-3-skill-calculator/)
- [WitcherDB: Remastered build planner](https://witcherdb.com/build-planner)
- [Hack the Minotaur: New skill trees](https://hacktheminotaur.com/the-witcher-3/the-witcher-3-remastered-new-skill-trees-guide/)
- [KeenGamer: Best builds for every playstyle](https://www.keengamer.com/articles/guides/the-witcher-3-remastered-best-builds-for-every-playstyle/)
- [FinalBoss: How to rebuild the 5.0 skill tree](https://finalboss.io/the-witcher-3-wild-hunt-how-to-rebuild-the-5-0-skill-tree)
- [Witcher wiki: Delusion](https://witcher.fandom.com/wiki/Delusion)

<!-- nav -->

---

[← 1. The resources every build trades](01-the-resources.md) · [Contents](../README.md) · [3. Gear basics →](03-gear-basics.md)
