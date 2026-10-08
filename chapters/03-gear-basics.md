# 3. Gear basics

Gear does two jobs in a build. Each armor piece's **weight class** feeds your School Technique, and at the very end of the game the **Grandmaster set bonuses** add the effects that define each school. Everything in between is stats. Once you know that, gear decisions get simple.

## Weight classes and School Techniques

Every armor piece is **light, medium or heavy**. In 5.0 all six School Techniques are starting skills in the General tree, and each one only counts armor pieces of one weight class (chest, gloves, trousers and boots, so four pieces at most).

| School Technique | Counts | Bonus per matching piece at rank 1 | At rank 3 | Four pieces at rank 3 |
| --- | --- | --- | --- | --- |
| **Cat** | Light | +2% fast attack damage, +8% crit damage* | +6% fast attack damage, +24% crit damage* | +24% fast attack damage, +96% crit damage* |
| **Wolf** | Medium | +2% weapon damage, +2% Sign intensity | +6% each | +24% each |
| **Griffin** | Medium | +2% Sign intensity, +0.2 Stamina per second | +6% Sign intensity, +0.6 Stamina per second | +24% Sign intensity, +2.4 Stamina per second |
| **Bear** | Heavy | +2% max Vitality, +2% strong attack damage | +6% each | +24% each |
| **Manticore** | Medium | +2% sword damage, +2% bomb damage | +6% each | +24% each |
| **Viper** | Medium | +2% max Vitality, +2% poison damage | +6% each | +24% each |

Sources: [WitcherDB planner](https://witcherdb.com/build-planner) (rank 1), [witcherhour.com](https://witcherhour.com/skills/) (all ranks), and the installed 5.0 game files, which confirm every value in the table except the starred crit damage ([chapter 19](19-the-maths.md#2-school-techniques-what-can-be-compared)). \*Cat's crit-damage bonus is stored as a multiplier, and how the game combines it with Geralt's base crit bonus is unresolved, so treat +96% as the published figure, not a measured one. Witcherhour lists Cat's fast attack bonus at rank 1 as +1%; the files say +2%. Griffin's Stamina figures are 0.2% of maximum Stamina per second for each rank and piece, so 0.2 / 0.4 / 0.6 points per second per piece at the base 100 Stamina, before armor modifiers ([chapter 19](19-the-maths.md#13-stamina-in-combat)); the nukesdragons database's +0.2 at rank 1 agrees, witcherhour's +1 per piece at rank 3 (+4 for four) does not.

Two things follow from this table:

- **A school's style is available long before its set.** Wolf, Griffin, Manticore and Viper Techniques all count *any* medium armor. You can play a Manticore alchemist at level 10 in medium armor from a merchant; the Manticore set itself only matters at level 40.
- **You can change an armor's weight class.** Three Hearts of Stone glyphwords make all your armor count as one weight: Levity (light), Balance (medium) and Heft (heavy). That's how players wear heavy armor and still use Cat School Techniques (chapter 6).

Heavier armor protects more but slows Stamina regeneration ([Fextralife: Chest armor](https://thewitcher3.wiki.fextralife.com/Chest+Armor)).

## The witcher sets

Each school's gear comes in up to five tiers: **Basic, Enhanced, Superior, Mastercrafted and Grandmaster**. You find the crafting diagrams in the world, usually through a "Scavenger Hunt" quest, and a craftsman makes the piece. Each tier's recipe uses up the piece from the tier below.

| Set | Weight | Level by tier (B / E / S / M / G) | Where the diagrams are |
| --- | --- | --- | --- |
| **Griffin** | Medium | 11 / 18 / 26 / 34 / 40 | Velen and Novigrad, then Skellige, then Toussaint |
| **Wolven** | Medium | 14 / 21 / 29 / 34 / 40 | Kaer Morhen, Velen and Skellige, then Toussaint |
| **Feline** | Light | 17 / 23 / 29 / 34 / 40 | Novigrad and Velen, then Skellige, then Toussaint |
| **Forgotten Wolven** | Medium | 20 / – / – / 34 / 40 | Velen (quest), then Kaer Morhen notes |
| **Ursine** | Heavy | 20 / 25 / 30 / 34 / 40 | Skellige, then Velen, then Toussaint |
| **Viper** | Medium | Swords 1–2; armor and Venomous swords 39 | White Orchard; Hearts of Stone (missable) |
| **Manticore** | Medium | Grandmaster only, 40 | Toussaint |

Levels come from pre-5.0 sources (Console Pulse, Gamestegy) and match a 5.0 KeenGamer article; no source reports a 5.0 change. Chapter 15 draws all of them on one timeline, and each school chapter links a location guide for its diagrams.

**About Manticore's weight.** One Remastered guide calls the Manticore set light. Every other source, including the 5.0 Manticore School Technique (which rewards medium armor), says medium. The "light" reading most likely came from a chest piece enchanted with the Levity glyphword. This book treats Manticore as medium.

## Set bonuses: only at Grandmaster

**Only Grandmaster gear has set bonuses.** Basic through Mastercrafted give stats and nothing else ([Vulkk](https://vulkk.com/2023/11/04/the-witcher-3-gear-sets-catalog/); [Console Pulse](https://www.consolepulse.com/multiplatform/the-witcher/guides/witcher-3-griffin-gear-guide)). Each Grandmaster set has a **3-piece** and a **6-piece** bonus; the six pieces are the four armor pieces plus the steel and silver swords. The crossbow doesn't count.

| Set | 3 pieces | 6 pieces |
| --- | --- | --- |
| **Feline** | A strong attack raises fast attack damage by 10% per set piece worn, for 5 seconds | Attacks from behind deal +50% damage and stun, at the cost of 1 Adrenaline point |
| **Griffin** | After you cast a normal Sign using Stamina, your next normal Sign within 3 seconds is free | Yrden traps are 40% larger; inside one you get +5 Stamina per second, +100% Sign intensity and take 20% less damage |
| **Ursine** | When Quen breaks, a 5% chance per set piece to recast it for free | Quen-based abilities deal +200% damage |
| **Wolven** | Each Bleeding effect you apply raises sword damage by 1% per set piece | Each Adrenaline point raises how many Bleeding effects one enemy can carry |
| **Forgotten Wolven** | Potion duration +7% per set piece | Aard deals extra damage to enemies affected by Yrden |
| **Manticore** | Crit chance and crit damage also apply to bombs, and bombs throw without delay | Every alchemy item gets +1 maximum charge |
| **Viper** | No set bonus | No set bonus |

These descriptions come from pre-5.0 sources; no 5.0 patch note mentions set bonuses. Two are disputed. Some wiki pages show the Wolven bleed bonus on Forgotten Wolven pieces. One Remastered guide describes an Ursine bonus based on strong attacks and Adrenaline instead of Quen. Check the tooltip in game. Sources: [Witcher wiki: Cat School Gear](https://witcher.fandom.com/wiki/Cat_School_Gear), [Witcher wiki: Griffin School Gear](https://witcher.fandom.com/wiki/Griffin_School_Gear), [Fextralife: Grandmaster Ursine Armor](https://thewitcher3.wiki.fextralife.com/Grandmaster+Ursine+Armor), [Witcher wiki: Wolf School Gear](https://witcher.fandom.com/wiki/Wolf_School_Gear), [Gamestegy: Grandmaster Forgotten Wolven](https://gamestegy.com/witcher-3/wiki/1383/grandmaster-forgotten-wolven-armor), [Witcher wiki: Manticore School Gear](https://witcher.fandom.com/wiki/Manticore_School_Gear).

## Who crafts what

| Craftsman level | Can make | Where |
| --- | --- | --- |
| Amateur | No witcher gear (one source says Basic Wolven armor) | Most early villages |
| Journeyman | Up to Superior | Most towns |
| **Master** | Up to Mastercrafted | **Yoana**, armorer at Crow's Perch, after the quest *Master Armorers* (level 24). **Hattori**, blacksmith in Novigrad, after *Of Swords and Dumplings* (level 24) |
| **Grandmaster** | Everything | **Lazare Lafargue** in Hauteville, Beauclair (Toussaint), the only Grandmaster craftsman, for both armor and swords |

Lafargue's quest *Master Master Master Master!* starts from the "Contract: Grandmaster Armorer" notice in Beauclair (suggested level 40). Asking him about the five vanished witchers opens the Grandmaster scavenger hunts for Feline, Griffin, Manticore, Ursine and Wolven. Every Grandmaster recipe except Manticore's needs the matching **Mastercrafted** piece (patch 4.0 restored this requirement for Wolven), so don't sell those ([Gamertagmythras: Crafting](https://gamertagmythras.com/blog/the-witcher-3/witcher-3-crafting-guide); [GameBanshee](https://gamebanshee.com/thewitcher3/walkthrough/mastermastermastermaster.php); [Witcher wiki: Wolf School Gear](https://witcher.fandom.com/wiki/Wolf_School_Gear)).

## Reforge: wear the stats, keep the look

New in 5.0, **Reforge** changes an item's appearance and nothing else. Yoana offers it after *Master Armorers*, Hattori after *Of Swords and Dumplings*. A look unlocks as soon as the item or its diagram is in your inventory, and Blood and Wine dyes carry over ([KeenGamer: Patch notes](https://www.keengamer.com/articles/guides/witcher-3-remastered-patch-notes-skill-reset-reforge-and-major-changes/)). You never have to pick between the armor that looks right and the armor that plays right.

## Rules of thumb

These follow from the rules above. They're this book's recommendations, not game mechanics:

1. **Weight class first, set second.** Before Grandmaster, sets give no bonus, so mixing pieces from different sets costs you nothing as long as every piece has the weight your Technique wants.
2. **Craft Basic as soon as you can wear it.** It gets the set's stats on you early, and every later tier is crafted from it.
3. **You can't skip a tier, but you can wait.** Each recipe uses up the piece below it, so reaching Mastercrafted means crafting every tier in order. You don't have to craft each one the day you find the diagram: if your current pieces are holding up, craft two tiers back to back later. Never sell or dismantle a piece you'll upgrade, the Mastercrafted ones above all.
4. **Socket single runestones and glyphs freely; save runewords and glyphwords for your final tier.** Upgrading keeps single stones but destroys words (chapter 6).
5. **Count your swords as set pieces.** The 6-piece bonus needs both swords from the same set, which competes with relic swords (chapter 17).

## Sources

- [WitcherDB: Remastered build planner](https://witcherdb.com/build-planner)
- [witcherhour.com: Witcher 3 skills](https://witcherhour.com/skills/)
- [Console Pulse: Grandmaster gear sets compared](https://consolepulse.com/multiplatform/the-witcher/guides/witcher-3-grandmaster-gear-sets-bonuses-compared)
- [Vulkk: Witcher 3 gear sets catalog](https://vulkk.com/2023/11/04/the-witcher-3-gear-sets-catalog/)
- [Witcher wiki: The Witcher 3 witcher gear](https://witcher.fandom.com/wiki/The_Witcher_3_witcher_gear)
- [Gamertagmythras: Crafting guide](https://gamertagmythras.com/blog/the-witcher-3/witcher-3-crafting-guide)
- [GameBanshee: Master Master Master Master!](https://gamebanshee.com/thewitcher3/walkthrough/mastermastermastermaster.php)
- [KeenGamer: Remastered patch notes, skill reset and Reforge](https://www.keengamer.com/articles/guides/witcher-3-remastered-patch-notes-skill-reset-reforge-and-major-changes/)
- [KeenGamer: New armor and weapons](https://www.keengamer.com/articles/guides/the-witcher-3-remastered-all-new-armor-weapons-locations/)

<!-- nav -->

---

[← 2. The 5.0 skill system](02-the-skill-system.md) · [Contents](../README.md) · [4. Alchemy basics →](04-alchemy.md)
