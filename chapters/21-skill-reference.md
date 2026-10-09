# 21. Skill reference: all 80 skills

Every skill in the four 5.0 trees, with what unlocks it, how many points it takes to reach from an empty tree, and its values at each rank. Use it to plan a build or a respec: pick your destination skills, then trace the cheapest route back.

## How to read the tables

- **Requires (any one):** owning **one point in any one** of the listed skills unlocks the skill. "Start" marks the 16 starting skills.
- **Points to reach:** the fewest skill points needed to own rank 1 of the skill from an empty tree, counting every skill on the route and the skill itself.
- **General links run both ways.** Owning any General skill unlocks every skill connected to it, above or below; the School Techniques are the six entry points.
- **Values** are the 5.0 launch values. Patch 5.01 changed Exploding Shield (it now reflects damage) and fixed how Synergy is displayed; no other skill values changed in its notes ([CD PROJEKT RED: Patch 5.01](https://www.thewitcher.com/us/en/news/52085/patch-5-01-for-the-witcher-3-wild-hunt-remastered-is-live)).

**Sources.** Ranks 1 to 3 come from [witcherhour.com](https://witcherhour.com/skills/), the only source that publishes all three; rank-1 values agree with [WitcherDB](https://witcherdb.com/build-planner) and [Hack the Minotaur](https://hacktheminotaur.com/the-witcher-3/the-witcher-3-remastered-new-skill-trees-guide/) except where noted. The prerequisite links come from WitcherDB's Remastered planner, the only source that lists them per skill; they were read in full twice with identical results, and every link agrees with the tree layout Hack the Minotaur and witcherhour describe. A few long links are worth confirming in game (see the end of the chapter). Effect wording is summarized. Where a row says **file-verified**, the file audits of build `5.0.0.1048522` supersede the published description; see [chapter 19's file audit](19-the-maths.md#file-evidence-and-reproducibility).

## Combat (red)

**How the tree is built.** Two mirrored wings joined by a center spine. The **Muscle Memory** wing covers fast and strong attacks: Strength Training, Three Strikes, Crushing Blow, Razor Focus, Sunder Armor, Rend and Deadly Precision. The **Arrow Deflection** wing covers defense and the crossbow: Cold Blood, Resolve, Lightning Reflexes, Anatomical Knowledge, Maiming Shot, Counterattack and Flood of Anger. The **spine** runs Undying → Fleet-Footed → Whirl → Crippling Strike, and can be entered from Three Strikes or Resolve. Rend, Counterattack, Deadly Precision and Flood of Anger can all be reached without Whirl. Dead ends (they unlock nothing): Sunder Armor, Maiming Shot, Deadly Precision, Flood of Anger.

| Skill | Requires (any one) | Points to reach | Effect, rank 1 / 2 / 3 |
| --- | --- | --- | --- |
| **Muscle Memory** | — (start) | 1 | After a successful dodge or roll, your next fast attacks deal +30% damage. Ranks 1/2/3: applies to the next 1 / 2 / 3 fast attacks. |
| **Arrow Deflection** | — (start) | 1 | Parry arrows; a perfect parry deflects them back with a chance to instantly kill. Ranks 1/2/3: kill chance 15% / 30% / 45%; deflected-arrow damage: none listed / +50% / +100%. |
| **Strength Training** | Muscle Memory | 2 | Fast attacks raise the next strong attack's damage. Ranks 1/2/3: +15% / +30% / +45%. |
| **Cold Blood** | Arrow Deflection | 2 | Each crossbow bolt that hits generates Adrenaline. Ranks 1/2/3: 0.3 / 0.6 / 1 Adrenaline point. |
| **Three Strikes** | Muscle Memory or Strength Training | 2 | **File-verified:** the fourth consecutive same-style hit has a 20% / 40% / 60% chance to gain a random +40–70% raw damage. Switching style resets the other counter. See [chapter 19](19-the-maths.md#10-three-strikes-a-bonus-to-the-fourth-matching-hit). |
| **Resolve** | Arrow Deflection or Cold Blood | 2 | Less Adrenaline lost when you take damage. Ranks 1/2/3: −33% / −67% / −100%. |
| **Undying** | Three Strikes or Resolve | 3 | At 0 Vitality, uses up all your Adrenaline (at least one point) to restore Vitality; once per 30 s at every rank. **File-verified:** 10% of max Vitality per point held, plus a flat 33% at rank 2 or 67% at rank 3: one point restores 10% / 43% / 77%, a full bar 30% / 63% / 97%. |
| **Crushing Blow** | Strength Training | 3 | A strong attack has a chance to raise the damage of the next 2 strong attacks by 50%. Ranks 1/2/3: 20% / 40% / 60% chance. |
| **Razor Focus** | Three Strikes | 3 | Gain 1 Adrenaline on entering combat; weapon hits generate more Adrenaline. Ranks 1/2/3: +10% / +20% / +30%. |
| **Fleet-Footed** | Undying | 4 | Less damage taken while dodging. Ranks 1/2/3: −33% / −67% / −100%. |
| **Lightning Reflexes** | Resolve | 3 | Extra slow-motion while aiming the crossbow; headshots deal +250% damage and can instantly kill. Ranks 1/2/3: extra slow 30% / 60% / 90%; kill chance 5% / 10% / 15%. |
| **Anatomical Knowledge** | Cold Blood | 3 | Crossbow damage gains a share of current silver-sword damage. Ranks 1/2/3: 10% / 20% / 30%. |
| **Whirl** | Fleet-Footed | 5 | Spinning attack that hits all nearby enemies; keeping it going costs Stamina, then Adrenaline. **File-verified:** 75 / 50 / 37.5 Stamina per second, then 1 / 0.67 / 0.5 Adrenaline per second once Stamina is empty; no Stamina regeneration while spinning. |
| **Rend** | Razor Focus, Crushing Blow or Whirl | 4 | Charged strike; damage grows with charge and with Adrenaline. **File-verified:** 50 Stamina per second while charging; a full charge multiplies damage by 2.5; each Adrenaline point spent adds a separate +10% / +20% / +30%; 1,000 flat armor penetration. |
| **Counterattack** | Lightning Reflexes, Anatomical Knowledge or Whirl | 4 | After a successful counterattack or dodge, the next attack deals bonus damage (the crossbow bonus is doubled). Ranks 1/2/3: +33% / +67% / +100%. |
| **Sunder Armor** | Crushing Blow | 4 | Strong attacks reduce the target's damage resistance by 10% per stack. Ranks 1/2/3: max 1 / 2 / 3 stacks. In the files, only your strong attacks use the reduction, starting with the hit that adds the stack. |
| **Crippling Strike** | Whirl | 6 | Critical fast attacks cripple the target so it takes more damage. Ranks 1/2/3: +10% / +20% / +30%. |
| **Maiming Shot** | Anatomical Knowledge | 4 | After a critical hit, the next crossbow shot disables monster special abilities. Ranks 1/2/3: 4 / 8 / 12 s. |
| **Deadly Precision** | Rend or Crippling Strike | 5 | All attacks can make the next strong attack an instant kill; immune enemies give Adrenaline instead. **File-verified:** any attack opens a 3-second window in which a strong attack has a 5% / 10% / 15% kill chance; successful kills share a 15-second cooldown; immune enemies give 0.05 / 0.1 / 0.15 Adrenaline, half the 0.1 / 0.2 / 0.3 in the description. |
| **Flood of Anger** | Crippling Strike or Counterattack | 5 | Casting a Sign consumes 3 Adrenaline to cast it at its highest level with extra intensity. Ranks 1/2/3: +50% / +100% / +150% Sign intensity. |

## Signs (blue)

**How the tree is built.** Each starting skill unlocks only its own Sign's alternate mode, from left to right Aard (Aard Sweep), Igni (Firestream), Yrden (Magic Trap), Quen (Active Shield) and Axii (Puppetmaster). The alternate modes feed a middle layer (Shockwave, Supercharged Glyphs, Domination), which feeds Catalyst and Fortify Signs, then Chain Reaction, Focus and Sidestep, then Aftershock and Resonance. **Every start reaches Resonance in 7 points.** Two lines are limited: from the Aard side you can never reach Supercharged Glyphs, Domination, Fortify Signs or Sidestep, and from the Axii side never Supercharged Glyphs, Shockwave, Catalyst or Focus. Magic Trap is the only alternate mode that reaches all three middle skills.

| Skill | Requires (any one) | Points to reach | Effect, rank 1 / 2 / 3 |
| --- | --- | --- | --- |
| **Far-Reaching Aard** | — (start) | 1 | Longer Aard range. Ranks 1/2/3: +1 / +2 / +3 yards. |
| **Melt Armor** | — (start) | 1 | Igni reduces armor. **File-verified projectile path:** applies round(12.5 × rank × total Igni power multiplier) stacks, each subtracting one percentage point from the armor multiplier; tops up rather than repeatedly adding the full amount. Published burn chance: +10% / +20% / +30%. See [chapter 19](19-the-maths.md#11-melt-armor-intensity-dependent-armor-reduction). |
| **Sustained Glyphs** | — (start) | 1 | Yrden lasts longer and covers more area, with more alternate-mode charges and standard-mode traps. Ranks 1/2/3: duration +5 / +10 / +15 s; area +10% / +20% / +30%; charges +2 / +4 / +6; traps +1 / +2 / +3. |
| **Exploding Shield** | — (start) | 1 | When Quen breaks, it pushes nearby enemies back. Ranks 1/2/3: not published. witcherhour says only "stronger pushback at each rank"; WitcherDB says "Push-back strength increases with skill level". **File-verified:** the break hits enemies within 3 units. Rank 1 rolls a stagger (50% with no Sign bonus); rank 2 adds 3–12 physical and silver damage; rank 3 adds a knockdown roll at 0.15 times the stagger chance. While the shield holds, it returns 10% × rank of absorbed melee damage as shock damage (chapter 19, section 16). |
| **Delusion** | — (start) | 1 | Target doesn't move toward Geralt while Axii is being cast; improves Axii in dialogue. Ranks 1/2/3: witcherhour (5.0) says "same effect at every rank", and Hack the Minotaur says the dialogue options are available from rank 1; before 5.0, some needed rank 2 ([Witcher wiki](https://witcher.fandom.com/wiki/Delusion)). Keep it slotted for dialogue. |
| **Aard Sweep** | Far-Reaching Aard | 2 | Alternate Aard: a blast that hits all enemies around you, with a reduced knockdown chance. Ranks 1/2/3: knockdown chance −21% / −17% / not reduced. |
| **Firestream** | Melt Armor | 2 | Alternate Igni: a continuous stream of fire. Ranks 1/2/3: Stamina cost −0% / −25% / −50%. |
| **Magic Trap** | Sustained Glyphs | 2 | Alternate Yrden: a discharge that damages and slows enemies within a 14-yard radius. Ranks 1/2/3: damage +0% / +25% / +50%. |
| **Active Shield** | Exploding Shield | 2 | Alternate Quen: a maintained shield that drains Stamina while held or blocking; absorbed damage restores Vitality. Ranks 1/2/3: Stamina drain normal (100%) / half / none. |
| **Puppetmaster** | Delusion | 2 | Alternate Axii: the target briefly fights for you and deals extra damage. Ranks 1/2/3: +20% / +40% / +60%. |
| **Supercharged Glyphs** | Firestream, Magic Trap or Active Shield | 3 | Enemies inside Yrden lose Vitality or Essence each second. Ranks 1/2/3: 10 / 20 / 30 per second. |
| **Shockwave** | Aard Sweep, Firestream or Magic Trap | 3 | Aard deals bonus damage equal to a share of your current Vitality. Ranks 1/2/3: 1% / 2% / 3%. |
| **Domination** | Magic Trap, Active Shield or Puppetmaster | 3 | Axii affects two targets at once. Ranks 1/2/3: effect 50% weaker / 25% weaker / full strength. |
| **Catalyst** | Supercharged Glyphs or Shockwave | 4 | Higher Aard and Igni intensity against enemies inside Yrden. Ranks 1/2/3: +30% / +60% / +90%. |
| **Fortify Signs** | Supercharged Glyphs or Domination | 4 | Yrden, Quen and Axii last longer. Ranks 1/2/3: +20% / +40% / +60% duration. |
| **Chain Reaction** | Catalyst or Fortify Signs | 5 | Casting a Sign raises the intensity of the next *different* Sign, stacking up to 5 times. Ranks 1/2/3: +5% / +10% / +15% per stack. |
| **Focus** | Catalyst | 5 | Sign intensity per Adrenaline point. Ranks 1/2/3: +10% / +20% / +30% per point. |
| **Sidestep** | Fortify Signs | 5 | After a dodge or roll, the next Sign costs less Stamina. Ranks 1/2/3: −20% / −40% / −60%. |
| **Aftershock** | Chain Reaction, Focus or Sidestep | 6 | **File-verified:** initial elemental payload = 15 × rank × global spell-power multiplier / 2, radius 3 game units. Normal processing then applies the cast Sign's power; alternate casts have cooldown gating. See [chapter 19](19-the-maths.md#12-aftershock-the-coefficient-and-the-damage-pipeline). |
| **Resonance** | Aftershock | 7 | After casting a Sign, your next 3 melee attacks deal bonus damage based on Sign intensity. Ranks 1/2/3: 10% / 20% / 30% of Sign intensity. |

## Alchemy (green)

**How the tree is built.** Three columns meet at Tissue Transmutation. **Bombs and oils** on the left (Pyrotechnics → Protective Coating → Volatile Compound → Cluster Bombs), **potions and decoctions** in the center (Hunter Instinct → Acquired Tolerance → Tissue Transmutation → Delayed Recovery, High Tolerance → Fast Metabolism → Side Effects), and **poison** on the right (Poisoned Blades → Toxic Shock → Debilitating Poison → Potent Sting). Two shortcuts skip the hub: Protective Coating → Volatile Compound and Toxic Shock → Debilitating Poison, which is why Cluster Bombs and Potent Sting cost 5 points but Side Effects costs 7. Adaptability and Endure Pain are never required for anything. From Refreshment alone you can't reach Endure Pain, Poisoned Blades or Toxic Shock; from Frenzy alone, not Adaptability, Pyrotechnics or Protective Coating; from Efficiency alone, not Adaptability or Endure Pain.

| Skill | Requires (any one) | Points to reach | Effect, rank 1 / 2 / 3 |
| --- | --- | --- | --- |
| **Refreshment** | — (start) | 1 | Each potion dose heals Vitality. Ranks 1/2/3: 10% / 20% / 30%. |
| **Efficiency** | — (start) | 1 | More bombs per slot. Ranks 1/2/3: +1 / +2 / +3. |
| **Frenzy** | — (start) | 1 | While Toxicity is above 1, time slows when an enemy is about to counterattack. Ranks 1/2/3: 5% / 10% / 15% slow. |
| **Adaptability** | Refreshment | 2 | Longer mutagen decoction duration. Ranks 1/2/3: +33% / +67% / +100%. |
| **Endure Pain** | Frenzy | 2 | Higher max Vitality while Toxicity is above the safe threshold. Ranks 1/2/3: +10% / +20% / +30%. |
| **Pyrotechnics** | Refreshment, Efficiency or Adaptability | 2 | All bombs deal extra damage, including bombs that normally deal none. Ranks 1/2/3: +50 / +100 / +150. |
| **Hunter Instinct** | Refreshment, Efficiency or Frenzy | 2 | At max Adrenaline, higher crit damage against the monster type your oil targets. Ranks 1/2/3: +20% / +40% / +60%. |
| **Poisoned Blades** | Efficiency, Frenzy or Endure Pain | 2 | Oiled blades can poison the target. Ranks 1/2/3: 5% / 10% / 15% chance. **File-verified:** only with an oil matching the target's monster type, and +10 points per oil tier above basic: 35% at rank 3 with a superior oil. A poison sword rolls separately. |
| **Protective Coating** | Pyrotechnics | 3 | Extra protection against the monster type your oil targets. Ranks 1/2/3: +5% / +10% / +15%. |
| **Acquired Tolerance** | Hunter Instinct | 3 | Each learned alchemy recipe raises max Toxicity. **File-verified:** +0.5 per recipe at every rank; the rank decides which recipes count: basic ones at rank 1, up to enhanced at rank 2, all at rank 3. Bolt and dye recipes never count. The published +1 / +2 / +3 per recipe is wrong. |
| **Toxic Shock** | Poisoned Blades | 3 | A strong attack on a poisoned enemy consumes the poison for a damage burst; once every 5 s. **File-verified:** burst = 25% / 50% / 75% of the attack's raw damage, as poison damage that still goes through resistances. The poison must already be on the target. |
| **Tissue Transmutation** | Protective Coating, Acquired Tolerance or Toxic Shock | 4 | Decoctions raise max Vitality while active. Ranks 1/2/3: +300 / +600 / +900. |
| **Delayed Recovery** | Tissue Transmutation | 5 | **File-verified:** if your potion Toxicity alone, decoctions excluded, is above 70% / 65% / 55% of your maximum when you drink, every active potion and decoction effect gains 5 s, never beyond its original duration. Two decoctions usually make the threshold unreachable. In New Game+ the definition lacks the three rank thresholds, so it probably qualifies on almost every drink (chapter 19). |
| **High Tolerance** | Tissue Transmutation | 5 | At 80% Toxicity or more you take 150% damage, but gain crit damage equal to a share of current Toxicity. Ranks 1/2/3: 33% / 67% / 100% of current Toxicity. In the files, decoctions count toward the 80%, and the script adds 0.2 × rank × (current ÷ max Toxicity) to the crit bonus; the separate 0.3334-per-rank multiplier only feeds the tooltip and adds nothing (chapter 19, section 16). |
| **Volatile Compound** | Delayed Recovery or Protective Coating | 4 | More bomb damage per point of Toxicity. Ranks 1/2/3: +0.1% / +0.2% / +0.3% per point. **File-verified:** counts current Toxicity including decoctions, as a separate multiplier on bomb damage: +45% at rank 3 with 150 Toxicity. |
| **Debilitating Poison** | Toxic Shock or High Tolerance | 4 | Poisoned enemies deal less damage. Ranks 1/2/3: −5% / −10% / −15%, applied in the files as extra resistance against attacks from enemies carrying your poison. |
| **Fast Metabolism** | Delayed Recovery or High Tolerance | 6 | Toxicity drops faster. Ranks 1/2/3: +1 / +2 / +3 points per second. **File-verified:** on a base drain of 0.25 per second, so potion Toxicity clears 5 / 9 / 13 times as fast. Decoction Toxicity doesn't drain. |
| **Cluster Bombs** | Volatile Compound | 5 | Bombs split into fragments, each dealing 40% of the bomb's damage. Ranks 1/2/3: 2 / 3 / 4 fragments. |
| **Side Effects** | Fast Metabolism | 7 | Drinking a potion can trigger another random potion's effect without adding Toxicity. Ranks 1/2/3: 33% / 67% / 100% chance. |
| **Potent Sting** | Debilitating Poison | 5 | Oiled weapons deal extra damage, doubled against poison-immune targets. Ranks 1/2/3: +5% / +10% / +15% (vs poison-immune: +10% / +20% / +30%). **File-verified:** needs an oil matching the target, not a poisoned target; it multiplies raw melee damage. "Poison-immune" means the creature template's immunity flag (golems, elementals, spiders, kikimores and a few others), not the much longer list of enemies with 100% poison resistance (chapter 19). |

## General

**How the tree is built.** A two-way lattice with the six School Techniques as entry points: Cat at the top, Viper at the bottom, the other four in the middle. A **left rail** runs Battle Frenzy – Strong Back – Gourmand – Elemental Attunement – Advanced Pyrotechnics, a **right rail** runs Adrenaline Burst – Survival Instinct – Anger Management – Synergy – Metabolic Boost, and four cross links tie them together (Attack Is the Best Defense – Strong Back, Sun and Stars – Survival Instinct, Element of Surprise – Elemental Attunement, Metabolic Control – Synergy). **No General skill is more than 3 points away**, counting the School Technique you enter through. Synergy, for example, costs 3 points through Bear or Griffin → Anger Management, through Griffin, Manticore or Viper → Metabolic Control, or through Viper → Metabolic Boost.

| Skill | Requires (any one) | Points to reach | Effect, rank 1 / 2 / 3 |
| --- | --- | --- | --- |
| **Cat School Techniques** | — (start; links to Battle Frenzy, Adrenaline Burst, Attack Is the Best Defense, Sun and Stars) | 1 | Per piece of **light** armor: crit damage and fast-attack damage. Ranks 1/2/3: crit damage +8% / +16% / +24% (published); fast-attack damage +2% / +4% / +6%. **File-verified:** the fast-attack values. The crit-damage part is a multiplier on a zero base and adds nothing in real attacks; the panel's figure uses a different formula (chapter 19). |
| **Battle Frenzy** | Cat School Techniques or Strong Back | 2 | Crit chance per available Adrenaline point. Ranks 1/2/3: +3% / +6% / +9% per point. |
| **Wolf School Techniques** | — (start; links to Attack Is the Best Defense, Sun and Stars) | 1 | Per piece of **medium** armor: weapon damage and Sign intensity. Ranks 1/2/3: +2% / +4% / +6% each. |
| **Adrenaline Burst** | Cat School Techniques or Survival Instinct | 2 | Faster Adrenaline generation; Signs also generate Adrenaline. Ranks 1/2/3: +2% / +4% / +6%. |
| **Attack Is the Best Defense** | Cat, Wolf or Bear School Techniques, or Strong Back | 2 | Successful defensive actions generate Adrenaline. **File-verified:** per rank, 0.03 Adrenaline per parry, 0.2 per counterattack and 0.1 per enemy attack you actually dodge. |
| **Sun and Stars** | Cat, Wolf or Bear School Techniques, or Survival Instinct | 2 | By day: extra Vitality regeneration out of combat. By night: extra Stamina regeneration in combat. Ranks 1/2/3: day +10 / +20 / +30 Vitality/s; night +1 / +2 / +3 Stamina/s (witcherhour, flat). WitcherDB gives night rank 1 as 1% of max Stamina per second (= 1/s at 100 max Stamina). **File-verified:** +10 Vitality/s per rank by day, outside combat only; +1% of max Stamina/s per rank at night, in combat only, scaled by armor weight. |
| **Strong Back** | Attack Is the Best Defense, Battle Frenzy or Gourmand | 3 | Higher carry weight. Ranks 1/2/3: +20 / +40 / +60. |
| **Bear School Techniques** | — (start; links to Attack Is the Best Defense, Sun and Stars, Gourmand, Anger Management) | 1 | Per piece of **heavy** armor: max Vitality and strong-attack damage. Ranks 1/2/3: +2% / +4% / +6% each. |
| **Survival Instinct** | Adrenaline Burst, Sun and Stars or Anger Management | 3 | Higher max Vitality. Ranks 1/2/3: +8% / +16% / +24%. |
| **Gourmand** | Bear or Griffin School Techniques, Strong Back or Elemental Attunement | 2 | Food regenerates Vitality for longer. Ranks 1/2/3: 5 / 10 / 15 minutes. |
| **Anger Management** | Bear or Griffin School Techniques, Survival Instinct or Synergy | 2 | With no Stamina left, Signs can be cast with Adrenaline. Ranks 1/2/3: 2 / 1.5 / 1 Adrenaline per cast. |
| **Elemental Attunement** | Gourmand, Element of Surprise or Advanced Pyrotechnics | 3 | More fire, frost, force, magic and poison damage. Ranks 1/2/3: +3% / +6% / +9%. |
| **Griffin School Techniques** | — (start; links to Gourmand, Anger Management, Element of Surprise, Metabolic Control) | 1 | Per piece of **medium** armor: Sign intensity and combat Stamina regeneration. **File-verified:** +2% / +4% / +6% Sign intensity and +0.2 / +0.4 / +0.6 Stamina per second (at 100 max Stamina) per piece: +2.4/s with four at rank 3, not the community's +4/s. |
| **Synergy** | Anger Management, Metabolic Control or Metabolic Boost | 3 | Bigger bonuses from mutagens in mutagen slots. Ranks 1/2/3: +10% / +20% / +30%. |
| **Element of Surprise** | Griffin, Manticore or Viper School Techniques, or Elemental Attunement | 2 | Hitting an enemy with a bomb raises melee damage for 10 s. Ranks 1/2/3: +10% / +20% / +30%. |
| **Metabolic Control** | Griffin, Manticore or Viper School Techniques, or Synergy | 2 | Higher max Toxicity. Ranks 1/2/3: +10 / +20 / +30. |
| **Advanced Pyrotechnics** | Viper School Techniques or Elemental Attunement | 2 | Thrown bombs may not be used up, and your own thrown bombs can't damage you. Ranks 1/2/3: 10% / 20% / 30% chance. |
| **Manticore School Techniques** | — (start; links to Element of Surprise, Metabolic Control) | 1 | Per piece of **medium** armor: sword and bomb damage. Ranks 1/2/3: +2% / +4% / +6% each. |
| **Metabolic Boost** | Viper School Techniques or Synergy | 2 | Consumes Adrenaline to cut the Toxicity cost of potions (mutagen decoctions excluded). Ranks 1/2/3: −10% / −20% / −30% per Adrenaline point. |
| **Viper School Techniques** | — (start; links to Element of Surprise, Metabolic Control, Advanced Pyrotechnics, Metabolic Boost) | 1 | Per piece of **medium** armor: max Vitality and poison damage. Ranks 1/2/3: +2% / +4% / +6% each; the poison bonus also applies to Toxic Shock's burst. |

## Where the sources disagree

1. **Legacy names.** The installed files call Three Strikes `sword_s24` / "Precise Blows", Aftershock `magic_s40` / "Overload", High Tolerance `HeightenedTolerance`, Potent Sting `WyvernSting` and Volatile Compound `VolatileConcoction`. Their links and implemented behavior establish those mappings.

**Settled by the game files:** Cat School Techniques' rank-1 fast-attack bonus is +2% (witcherhour's +1% was a typo); Delayed Recovery works as described in its row; and the branch passives count only equipped skills, with the Signs passive worth 0.5% of maximum Stamina per second, which is +0.5 per second at 100 Stamina (chapter 2). Sun and Stars' night bonus is 1% of maximum Stamina per rank, so witcherhour and WitcherDB agree at 100 Stamina. Exploding Shield, Mutated Skin and High Tolerance now have file values in their rows, and Cat School Techniques' crit-damage part adds nothing.

**Still requiring verification:** in-game tests of the file readings. Chapter 19 lists the open questions in order of how much they could change a build.

**Links worth checking in game.** Because the per-skill links come from one source, the long ones that skip several rows are worth a glance before you plan around them: Crushing Blow → Sunder Armor, Anatomical Knowledge → Maiming Shot, Protective Coating → Volatile Compound, Toxic Shock → Debilitating Poison, Battle Frenzy ↔ Strong Back, and Adrenaline Burst ↔ Survival Instinct.

## Sources

- [witcherhour.com: Witcher 3 skills](https://witcherhour.com/skills/) and [skill calculator](https://witcherhour.com/witcher-3-skill-calculator/)
- [WitcherDB: Remastered build planner](https://witcherdb.com/build-planner)
- [Hack the Minotaur: New skill trees guide](https://hacktheminotaur.com/the-witcher-3/the-witcher-3-remastered-new-skill-trees-guide/)
- [Mobalytics: New skill tree](https://mobalytics.gg/gamebase/guides/witcher-3-new-skill-tree)
- [CD PROJEKT RED: Patch 5.01 notes](https://www.thewitcher.com/us/en/news/52085/patch-5-01-for-the-witcher-3-wild-hunt-remastered-is-live)

<!-- nav -->

---

[← 20. Common mistakes, and how to respec](20-mistakes-and-respec.md) · [Contents](../README.md) · [22. Sources →](22-sources.md)
