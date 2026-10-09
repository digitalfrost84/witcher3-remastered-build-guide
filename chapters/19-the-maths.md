# 19. The maths behind the choices

This chapter collects every calculation in the book in one place, with the assumptions spelled out. The school chapters use these results; here you can check the working.

## Ground rules

- **Separate file evidence from published descriptions.** Local file audits on October 9, 2026 used the installed executable version `5.0.0.1048522`. The values marked **file-verified** below come from that build's definitions and scripts. They are not in-game timing or damage measurements.
- **Other values still come from community sources.** [witcherhour.com](https://witcherhour.com/skills/), [WitcherDB](https://witcherdb.com/build-planner) and [Hack the Minotaur](https://hacktheminotaur.com/the-witcher-3/the-witcher-3-remastered-new-skill-trees-guide/) supply the remaining skill descriptions. Older item and potion values remain provisional where the audits did not check them.
- **Follow the calculation, not just the percentage label.** A bonus to an attack-power multiplier is not necessarily a separate multiplier on final damage. Armor reduction is not the same as extra damage.
- **Treat disagreements as questions to test.** A tooltip describes intended behavior; scripts show the implemented path. Check the game build and use a controlled test when they disagree.

## File-verified base values

These are unmodified baseline attributes and rates, before equipment, skills, potions and other conditional modifiers.

| Property | Value | Qualification |
| --- | --- | --- |
| Critical-hit chance | **5%** | Conditional guarantees and bonuses are additional |
| Critical-damage bonus | **+0.25 to the attack-power multiplier** | Not a universal final-damage multiplier of 1.25; see section 3 |
| Maximum Toxicity | **100 points** | Normal-game and NG+ definitions agree |
| Potion Toxicity drain, in combat | **0.25 points/s** | Excludes Toxicity locked by active decoctions |
| Potion Toxicity drain, outside combat | **0.275 points/s** | The combat rate is multiplied by 1.1 |
| Toxicity damage | **0.5% of maximum Vitality/s above 50% Toxicity** | Decoctions count toward the 50%; no damage while meditating |
| Decoction Toxicity | **50 locked for 30 minutes** | Basilisk locks 40; locked Toxicity doesn't drain |
| Potion Toxicity per dose | **Thunderbolt and Petri's Philter 25, Swallow and Tawny Owl 20, Cat 15** | The same at every recipe tier |
| Stamina regeneration, in combat | **10% of maximum Stamina/s** | Normally 10 points/s; armor weight multiplies it; see section 13 |
| Stamina regeneration, outside combat | **100% of maximum Stamina/s** | Normally 100 points/s; only while regeneration is active |

The base crit attributes, Toxicity maximum and Stamina attributes also agree between normal-game and NG+ definitions. The installed Brothers In Arms override retains the same baseline Toxicity drain. Action-related pauses can delay Stamina recovery, so neither regeneration rate equals casts per second. See [file evidence](#file-evidence-and-reproducibility) for paths and functions.

## 1. A basic combo: which skills actually activate

The Wolven sequence is a dodge, three fast attacks and a strong finisher. Muscle Memory covers more of those fast attacks as its rank rises, Strength Training supports the finisher, and Toxic Shock needs poison already on the target. Their rank descriptions explain the sequence; the damage pipeline below decides what it's worth.

**Strong and fast attacks follow different paths (file-verified).** A strong attack adds +0.15 (the heavy-attack definition) and +0.333 (the core strong-attack skill) to the attack-power multiplier, loses 0.433 in damage processing, carries **1,000 flat armor penetration**, and is multiplied by **1.833 after defenses**. With identical weapon damage, no armor, no crit and a shared multiplier `M`:

```math
\frac{D_{\mathrm{strong}}}{D_{\mathrm{fast}}} = \frac{1.833\,(M + 0.05)}{M}
```

That is 1.925 at `M = 1` and drifts toward 1.833 as other bonuses grow (1.879 at `M = 2`). Against armor the gap widens, because a fast hit loses the target's flat armor and a strong hit usually doesn't (section 11). This is damage per hit, not per second: attack animation timings haven't been measured, so the book makes no damage-per-second claim.

The earlier **+23% at rank 1 / +89% at rank 3** illustration stays withdrawn. It applied Wolf School Techniques as a separate multiplier on the completed combo and ignored Toxic Shock's 5-second cooldown.

**Three Strikes does not activate in this repeating three-fast/one-strong sequence.** Its implementation checks the fourth consecutive matching attack; switching between fast and strong resets the other counter. Keep rank 1 to unlock Razor Focus and Undying, but prioritize another useful rank or slot if this is your usual rotation. Section 10 gives the boost for a sequence that does activate it.

**Toxic Shock is conditional.** It fires only on a target that already carries poison, uses that poison up, and then waits out a 5-second cooldown. A strong hit that poisons a clean target can't consume the poison on the same hit. Count it once per cooldown on a target you've re-poisoned, not once per combo (section 7).

**Melt Armor mostly helps the three fast hits.** The strong finisher already carries 1,000 flat penetration, more than any enemy's armor in the game's definitions (section 11). Its armor reduction is not a damage percentage either way.

## 2. School Techniques: what can be compared

**File-verified:** each Technique counts the chest, gloves, trousers and boots of its weight and multiplies that count by its rank. Its main bonuses are **0.02 per rank per piece**, so rank 3 with four pieces gives 0.24:

| Technique | Rank 3, four pieces |
| --- | --- |
| **Wolf** | +24% attack power and +24% Sign intensity |
| **Manticore** | +24% fast-attack and strong-attack power, +24% bomb damage |
| **Cat** | +24% fast-attack power; its crit-damage part adds nothing in combat (below) |
| **Bear** | +24% strong-attack power and +24% maximum Vitality |
| **Griffin** | +24% Sign intensity and +2.4 Stamina/s at 100 maximum Stamina (section 13) |
| **Viper** | +24% poison damage, Toxic Shock's included, and +24% maximum Vitality |

**Cat's crit damage adds nothing to real attacks (file-verified).** The damage code resolves the crit bonus as `base × multiplier + addition`. Cat stores its 0.08 per rank and piece as a *multiplier*, and the game applies it once for every light piece times rank. But no definition in the base game, either expansion or New Game+ gives crit damage a *base* value: Geralt's +0.25 and every weapon, skill and oil bonus are *additions*. The multiplier therefore multiplies zero:

```math
C = 0 \times (0.08\,r\,n) + (0.25 + \text{other additions}) = 0.25 + \text{other additions}
```

The "+96%" comes from the character panel, which uses a different formula: it multiplies your whole crit-damage total by rank × light pieces, so rank 3 with four pieces shows 0.25 × 12 = +300% on top of the base. Real hits don't use that formula. Cat's established value is its fast-attack bonus. The same zero base also neutralizes Doppler's back-attack crit bonus (`damageIncrease`, also a multiplier).

Matching labels still don't prove equal final damage once crits, armor, skill activation and attack timing enter the calculation. Choose the Technique that supports the build's actions. These findings do not establish a new ordering of the schools.

## 3. Crits: what chance is worth

![Published bonus crit chance by Adrenaline held: 10% from Katakan, up to 37% at three points with rank-3 Battle Frenzy; excludes the file-verified 5% base chance](../images/crit-stack.png)

**File-verified:** Geralt's baseline crit chance is 5%, and his baseline critical-damage attribute contributes 0.25 to the attack-power multiplier. The damage code adds the resolved crit bonus to that multiplier after applying the victim's crit-damage reduction.

For a simplified hit before armor and other later processing, let:

- `W` be the damage term multiplied by attack power;
- `M` be the non-critical attack-power multiplier;
- `A` be damage added after that multiplication;
- `C` be the resolved extra multiplier on a crit, after the target's crit-damage reduction;
- `c` be the actual crit probability.

Then:

```math
D_{\mathrm{normal}} = WM + A,\qquad
D_{\mathrm{crit}} = W(M+C) + A
```

```math
\mathbb{E}[D] = W(M+cC) + A,\qquad
\Delta\mathbb{E}[D] = W\,\Delta c\,C
```

Relative to the non-critical hit, that marginal benefit is:

```math
\frac{\Delta\mathbb{E}[D]}{D_{\mathrm{normal}}}
= \frac{W\,\Delta c\,C}{WM+A}
```

When `A = 0`, this reduces to `Δc × C / M`. It is not the percentage gain over an already critting build; that comparison uses its current expected damage as the denominator.

This corrects the former claim that the Feline crit package guarantees **0.35**, or **0.57** against an oiled target, additional normal hits per swing. Those lower bounds did not account for the existing attack-power multiplier or the complete critical-bonus calculation. Do not replace them with a new bound that includes Cat's published percentage; section 2 shows that part contributes nothing.

Crit chance and the resolved crit bonus still work together. The size of the benefit needs the actual weapon, skills, other damage bonuses and target. Feline remains a coherent crit build, but this audit does not prove its superiority to another sword build.

## 4. Adrenaline: the Undying floor

**File-verified:** when a hit would kill you, Undying sets your Vitality to:

```math
\text{Vitality} = \text{max Vitality} \times \bigl(0.1 \times \text{Adrenaline held} + 0.33334 \times (\text{rank} - 1)\bigr)
```

It needs at least one whole Adrenaline point, uses up the entire bar and then waits out a 30-second cooldown at every rank. Once you have a whole point, fractions count too. It doesn't trigger on quest, trap or falling deaths.

| Adrenaline held | Rank 1 | Rank 2 | Rank 3 |
| --- | --- | --- | --- |
| 1 (fight start, with Razor Focus) | 10% | 43% | 77% |
| 2 | 20% | 53% | 87% |
| 3 (full bar) | 30% | 63% | 97% |

So the "33% / 67% bonus" in the rank descriptions is a flat share of maximum Vitality, and it dwarfs the per-point part: rank 2 with one point restores more than rank 1 with a full bar. Razor Focus still matters, because Undying does nothing with an empty bar, which is why the plans buy Razor Focus before Undying or alongside it.

## 5. Effective health: Ursine with Mutated Skin

How long you last scales with Vitality divided by the share of each hit that reaches it. With Bear School Techniques rank 3 on four heavy pieces (+24%) and Survival Instinct rank 3 (+24%):

```math
\text{effective health} = \frac{1 + 0.24 + 0.24}{1 - 0.15 \times \text{Adrenaline held}}
```

| Adrenaline held | Damage taken | Effective health vs no bonuses |
| --- | --- | --- |
| 0 | 100% | 1.48× |
| 1 | 85% | 1.74× |
| 2 | 70% | 2.11× |
| 3 | 55% | 2.69× |

A full bar nearly doubles how long you last compared with an empty one (2.69 against 1.48), which is the trade-off against spending the same three points on a rank-3 Rend. **Mutated Skin (file-verified):** the damage that reaches your Vitality is multiplied by `1 − 0.15 × whole Adrenaline points`. Fractions don't count, unlike Undying: 2.9 points still give −30%. It does nothing while any Quen shield is active and doesn't reduce damage over time such as poison, burning or bleeding. Chapter 10.

## 6. The Toxicity budget and Euphoria

![How many decoctions fit at different maximum Toxicity levels: one with no skills or with Acquired Tolerance alone, two with Metabolic Control and Manticore armor added, and four only with about 150 of the game's 173 eligible recipes learned](../images/toxicity-budget.png)

Each decoction locks 50 Toxicity until it ends, so:

```math
\text{decoctions} = \left\lfloor \frac{\text{max Toxicity} - \text{room for potions}}{50} \right\rfloor
```

```math
\text{max Toxicity} = 100 + 0.5\,E + 10\,k + 5\,m
```

where `E` is the number of eligible recipes you've learned, `k` is Metabolic Control's rank and `m` is the number of Manticore armor pieces worn (chest, gloves, trousers, boots). All four terms are **file-verified**.

**Acquired Tolerance adds 0.5 per eligible recipe, not 1/2/3.** Its rank decides which recipes count: those of level 1 at rank 1, up to level 2 at rank 2, all three levels at rank 3. Bolt and dye recipes never count. With 40 eligible recipes at rank 3, rank-3 Metabolic Control and four Manticore pieces, the total is 100 + 20 + 30 + 20 = **170**: two decoctions with 70 left for potions, or three with 20 left, which isn't enough for a Thunderbolt.

The game defines **173 eligible alchemy recipes** across the base game and both expansions (109 of level 1, 141 up to level 2). Learning every one would add 86.5, for a ceiling of 236.5 and four decoctions with 36.5 to spare. Four decoctions plus room for a Thunderbolt need at least 150 of them. How many a real playthrough can learn hasn't been counted, so treat 236.5 as an upper bound.

**Toxicity damage (file-verified):** above 50% of your maximum, decoctions included, you lose **0.5% of your maximum Vitality per second**, except while meditating. Two decoctions stay below that line only with a maximum of 200 or more, so at the 170 example they mean a constant drain for Refreshment, Endure Pain and healing effects to cover.

**Euphoria (file-verified):** in combat, it adds **0.75 percentage points per point of current Toxicity, decoctions included**, to the same multiplier that attack power and Sign intensity already use. There's no separate cap in the calculation; the tooltip's maximum is simply 0.75% of your maximum Toxicity.

| Toxicity held | Added to the power multiplier |
| --- | --- |
| 50 | +0.375 |
| 100 | +0.75 |
| 150 | +1.125 |
| 170 (the example maximum above) | +1.275 |

Because it joins the multiplier your other bonuses already raised, its share of the final hit depends on what's there: on a multiplier of 1.5, +0.75 is a 50% increase, not 75%.

**Delayed Recovery (file-verified, normal game):** a drink qualifies only if your potion Toxicity, not counting decoctions, is above **70% / 65% / 55%** of your maximum at ranks 1/2/3. Each qualifying drink then adds 5 seconds to every active potion and decoction effect, never beyond its original duration. Because decoctions take room that potions can't use, it can only qualify when:

```math
\text{decoction Toxicity} < (1 - \text{threshold}) \times \text{max Toxicity}
```

At the 170 maximum above, rank 3 needs more than 93.5 points of potion Toxicity, so it can't trigger with two or more decoctions running, and rank 1 needs more than 119, which a single decoction already makes nearly impossible. It rewards the opposite of a decoction build.

**In New Game+ it probably triggers on almost every drink.** The code asks for three rank thresholds, but the NG+ definition only carries the old single `toxicity_threshold`. A missing attribute resolves to 0, so any potion Toxicity above zero qualifies, decoctions or not. That rests on two standard engine behaviors, NG+ loading its own definitions and a missing attribute reading as 0, which haven't been confirmed in-game.

**Potion Toxicity recovery (file-verified):** without modifiers, clearing `T` points takes `T / 0.25` seconds in combat or `T / 0.275` outside it, if the combat state stays unchanged; 20 points take 80 seconds in combat. **Fast Metabolism** adds 1 point per second per rank to that drain, so the same 20 points clear in 16 s at rank 1 and about 6 s at rank 3. That is five times the base speed at rank 1, which strips a Euphoria build of potion Toxicity quickly; decoction Toxicity doesn't drain either way.

**Volatile Compound (file-verified):** bomb damage is multiplied by `1 + 0.001 × rank × current Toxicity`, decoctions included: +45% at rank 3 with 150 Toxicity. It turns a decoction stack into bomb damage with or without Euphoria. Chapter 12.

## 7. Poison: how many hits it takes

![Chance the target is poisoned after a number of hits with a matching oil, at 5%, 15%, 35% and 44.75% per hit](../images/poison-odds.png)

**File-verified:** Poisoned Blades rolls only when your blade carries an oil that matches the target's monster type. Its chance is:

```math
p_{\mathrm{PB}} = 0.05 \times \text{rank} + 0.10 \times (\text{oil tier} - 1)
```

so 5/10/15% with a basic oil, 10 points more with an enhanced oil and 20 more with a superior one: **35% at rank 3 with a superior oil**. A sword with its own poison chance, like the Viper swords' 15%, rolls separately:

```math
p = 1 - (1 - p_{\mathrm{PB}})(1 - p_{\mathrm{sword}}),\qquad
P_{\text{poisoned}}(n) = 1 - (1 - p)^n
```

| Chance per hit | After 3 hits | After 6 hits | Hits for even odds |
| --- | --- | --- | --- |
| 5% (rank 1, basic oil) | 14% | 26% | 14 |
| 15% (rank 3 with a basic oil, or a Viper sword alone) | 39% | 62% | 5 |
| 35% (rank 3, superior oil) | 73% | 92% | 2 |
| 44.75% (rank 3, superior oil and a Viper sword) | 83% | 97% | 2 |

The table assumes independent rolls and a target that can be poisoned. Multiple oils and repeated runes aren't covered.

**Who can't be poisoned (file-verified).** Poison lasts `5 s × attack power × (1 − poison resistance)`, so a target with 100% poison resistance gets a 0-second poison that expires on the next update: no damage, nothing for Toxic Shock to consume. These monster definitions carry 100%:

- **Insectoids and draconids:** arachas, endregas, all spiders (Hearts of Stone and Blood and Wine), kikimores, scolopendromorphs, forktails, wyverns and basilisks.
- **Necrophages:** drowners, grave hags, water hags and foglets.
- **Specters and cursed ones:** wraiths, noonwraiths, nightwraiths, the Crones and the Baron's transformed wife.
- **Elementa and constructs:** earth, fire and ice elementals, golems, gargoyles and the djinn.
- **Blood and Wine and others:** archespores, the wight, the Spoon Collector, Dettlaff, the toad prince and fairy-tale enemies.
- **Any enemy 20 or more levels above you**, human or monster: the "deadly" level bonus sets poison resistance to 100%.

Viper and Toxic Shock builds need another plan for these fights, which include several major bosses.

**Template immunity is a different, shorter list (file-verified).** Potent Sting's doubled bonus checks `IsImmuneToBuff`, which reads immunity flags from the creature templates (`.w2ent`), not the resistance value. Flagged immune to poison: earth, fire and ice elementals and golems, both expansions' spiders, kikimores, archespores, scolopendromorphs, the toad prince, Iris's nightwraith, the banshees and their summons, Dettlaff, Regis and the Caretaker. Arachas, drowners, wraiths, hags and the rest are only fully resistant, so poison fails on them but Potent Sting deals its normal bonus.

**What poison does (file-verified):** a standard poison lasts 5 seconds, scaled by the attack's power multiplier and shortened by the target's poison resistance, and deals 1.6% of the target's maximum health per second before damage processing. An equal-strength poison from the same source refreshes the duration instead of stacking.

**Toxic Shock (file-verified):** a strong melee attack against a target that already has poison adds poison damage equal to **25% / 50% / 75% of that attack's raw damage**, removes the poison and starts a 5-second cooldown. The burst then goes through normal damage processing, so it isn't a guaranteed +25/50/75% of the final hit; Viper School Techniques' poison bonus applies to it. The check runs before Poisoned Blades rolls, so a strong hit can't poison a clean target and consume that poison at once.

**The rest of the poison line (file-verified):** Potent Sting needs a matching oil, not a poisoned target, and multiplies raw melee damage by `1 + 0.05 × rank`, or `1 + 0.10 × rank` against poison-immune enemies. Debilitating Poison adds `0.05 × rank` resistance against attacks from enemies carrying your poison. Ordinary poison you apply also triggers Metamorphosis. Chapter 13.

## 8. Sign intensity

![Sign intensity added by each source, fully upgraded: Griffin set inside Yrden +100%, Catalyst +90%, Focus +90%, Chain Reaction +75%, Petri's Philter +25%, Griffin Techniques +24%, Grandmaster chest +22%, Grandmaster steel sword +21%](../images/sign-intensity.png)

The two largest bonuses need Yrden: Catalyst only counts against enemies inside it, and the Griffin set bonus only while you stand in your own trap. Focus needs a full bar, and Chain Reaction five casts in a row, each a different Sign from the one before. The flat sources (potion, Technique, armor, sword) are what you have in every fight. Chapter 9.

**File-verified:** the Grandmaster Griffin set's Yrden bonus (+100% Sign intensity, +5% of maximum Stamina per second, 20% less damage taken, a 40% larger trap), Griffin School Techniques' Sign intensity and Petri's Philter's +15/20/25%. Catalyst, Focus and Chain Reaction come from witcherhour; their per-rank coefficients in the files match it.

**Grandmaster item values (file-verified).** The chest is the game's tier 4, the other pieces tier 5:

| Set | Chest | Gloves, trousers, boots (each) | Steel and silver swords |
| --- | --- | --- | --- |
| **Feline** | +22% attack power | +11% attack power | +10% crit chance, +15% Aard intensity, 15% bleeding |
| **Griffin** | +22% Sign intensity | +11% Sign intensity | +5% crit chance, +0.25 crit damage, +21% Sign intensity |
| **Ursine** | +0.22 Adrenaline gain | +0.11 Adrenaline gain | +5% crit chance, +0.75 crit damage, +0.21 Adrenaline gain |
| **Wolven** | +0.22 Adrenaline gain | gloves +11% Sign intensity; trousers +11% attack power and Sign intensity; boots +11% attack power | +11% crit chance, +11% Sign intensity, +0.11 Adrenaline gain, 11% bleeding |
| **Manticore** | +0.25 crit damage | gloves and trousers +5% crit chance; boots +0.25 crit damage | +5% crit chance, +0.50 crit damage, 250 armor piercing, 10% bleeding |

Base sword damage is 372 steel and 524 silver for every set. Every Manticore armor piece also adds +5 maximum Toxicity. The files hold a second, stronger Manticore tier (`Red Wolf … 2`, level 70); its localisation key marks it as the New Game+ version, so it isn't the set you craft in a first playthrough. Light and heavy pieces also carry their Stamina regeneration modifier (section 13).

## 9. Branch passives

**File-verified:** each tree's passive counts the ranks of your **equipped** skills from that tree, leaving out the core skills. Points in unslotted skills give nothing, not even the passive.

| Tree | Per equipped rank |
| --- | --- |
| Combat | +0.01 Adrenaline gain (`focus_gain`) |
| Signs | +0.5% of maximum Stamina per second in combat, normally +0.5/s |
| Alchemy | +2% potion duration, which also multiplies bomb damage by the same 2% |
| General | +1% maximum Vitality |

This settles both disputes in chapter 21: witcherhour was right that only equipped skills count, and the two descriptions of the Signs passive are the same number at 100 Stamina. Hack the Minotaur's "+2% potion duration and bomb damage" is right too: thrown bombs are multiplied by one plus your potion-duration bonus.

## 10. Three Strikes: a bonus to the fourth matching hit

**File-verified:** the skill uses the internal name `sword_s24` (legacy “Precise Blows”). The prerequisite links and implementation identify it as Three Strikes.

| Rank | Chance on the fourth matching hit | Raw-damage boost if it activates |
| --- | --- | --- |
| 1 | 20% | Random +40–70% |
| 2 | 40% | Random +40–70% |
| 3 | 60% | Random +40–70% |

The counter advances on qualifying hits. On count four, the game rolls the chance, rolls the damage increase on success, applies it to that hit, and resets the counters. Changing attack style resets the other style's count. The damage code does not establish a persistent boost to every following attack.

**Recommendation:** keep the prerequisite point where the plan needs Razor Focus or Undying. Further ranks and a slot are conditional on regularly reaching four same-style hits. The Wolven three-fast/strong-finisher loop does not meet that condition.

## 11. Melt Armor: intensity-dependent armor reduction

**File-verified:** `magic_s8` defines a coefficient of 0.25 per rank, and each applied stack subtracts 0.01 from the target's armor multiplier. For the inspected Igni projectile path:

```math
N = \operatorname{round}_{\mathrm{half\ up}}(12.5\,r\,I_{\mathrm{Igni}})
```

Here `r` is skill rank and `I_Igni` is the total internal Igni power multiplier: 1.0 means no increase over the base multiplier, and 2.0 means +100%. Each of the `N` stacks subtracts one percentage point from the armor multiplier.

| Igni power multiplier | Rank 1 | Rank 2 | Rank 3 |
| --- | --- | --- | --- |
| 1.0 | 13 points | 25 points | 38 points |
| 2.0 | 25 points | 50 points | 75 points |

The cast adds only the stacks missing from this target amount; repeated equal-strength casts do not add the full reduction again. There is no explicit cap in this application formula. Effective armor limits and other Igni delivery paths need separate verification before extrapolating to very high intensity.

**How defenses are applied (file-verified).** With `A` the target's flat armor, `P` your flat penetration, `R` its percentage resistance and `Q` your percentage penetration:

```math
r = R - Q,\qquad
D_{\mathrm{after}} = \max\bigl(0,\ D - \max(0,\,(A - P)(1 + \min(r, 0)))\bigr) \times \bigl(1 - \max(0, r)\bigr)
```

Elemental damage skips the flat part. Strong attacks and Rend carry `P = 1000`, while the armor values in the game's enemy definitions, flat bonuses included, add up to a few hundred at most, so a strong hit usually clears flat armor on its own. Melt Armor and other flat reductions therefore mostly help fast attacks. Sunder Armor works on resistance instead, and only your strong attacks use it, including the hit that adds the stack.

**Recommendation:** Igni before melee remains useful against armored enemies for builds that land fast attacks. A 25-point armor-multiplier reduction is not a 25% damage increase; target armor and mitigation determine the benefit.

## 12. Aftershock: the coefficient and the damage pipeline

**File-verified:** `magic_s40` (legacy “Overload”) has an elemental-damage coefficient of 15. Its prerequisites and cast behavior identify it as Aftershock. It searches within **3 game units** of the Sign entity, with a line-of-sight test.

The initial damage payload is:

```math
R = 15\,r\,I_{\mathrm{global}}/2
```

The action then enters normal damage processing, which obtains the power of the Sign that caused it. With zero additive/base power contributions and no other damage modifiers, the pre-resistance expression is:

```math
D = 7.5\,r\,I_{\mathrm{global}}\,I_{\mathrm{cast\ Sign}}
```

This is why **15/30/45 is not a final-damage table**. Both global power and the cast Sign's power can matter; target mitigation and other processing still follow. Normal casts trigger it every time; alternate casts are limited to once every **2 seconds**.

**Recommendation:** treat Aftershock as close-range damage on the route to Resonance, not a proven reason to replace another core skill. Its practical value needs measured damage, target coverage and activation frequency.

**The two Sign mutations (file-verified).** Only one can be active, so they're alternatives:

- **Conductors of Magic:** with a sword of quality 3 or higher (magic, relic or witcher gear) in hand, every Sign action, Aftershock included, adds **half of that sword's base damage stat** (steel: slashing; silver: silver damage) to each raw damage component before Sign intensity applies. It uses the listed damage, not your fully boosted sword damage.
- **Magic Sensibilities:** Sign crit chance = **20% + 10% × the cast Sign's power multiplier**: 30% with no bonus, 40% at +100%, certain at a multiplier of 8. A crit adds the Sign's power multiplier to itself after the target's crit reduction, doubling it in the simple case. Sign burning compresses multipliers above 2.5 logarithmically, so "double damage" isn't universal.

## 13. Stamina in combat

**File-verified:** while regeneration is running and you aren't guarding:

```math
\text{Stamina per second} = (F + S \times M) \times (1 + \text{armor})
```

`S` is maximum Stamina (normally 100), `M` the sum of proportional bonuses and `F` the flat ones.

| Source | Adds, at 100 maximum Stamina |
| --- | --- |
| Base | 10/s |
| Signs branch passive | +0.5/s per equipped Signs rank |
| Griffin School Techniques | +0.2/s per rank per medium piece: 2.4/s at rank 3 with four |
| Tawny Owl, basic / enhanced / superior | +5 / +8 / +10/s |
| Grandmaster Griffin set, inside Yrden | +5/s |
| Ancient Leshen decoction | +2/s flat for each Sign cast in combat, stacking until the fight ends |
| Sun and Stars, at night | +1/s per rank (1% of maximum Stamina per rank) |

Armor multiplies the total: chest and trousers ±10% each, boots ±3%, gloves ±2%, plus for light pieces and minus for heavy ones. Full light armor gives ×1.25, medium ×1 and heavy ×0.75. The weight glyphwords (chapter 6) set this modifier along with the weight class.

Example: medium armor, Griffin School Techniques rank 3 on four pieces, 18 equipped Signs ranks, superior Tawny Owl, standing in a Grandmaster Griffin Yrden:

```math
10 + 9 + 2.4 + 10 + 5 = 36.4\ \text{points/s},\ \text{plus 2 per Ancient Leshen stack}
```

Superior Tawny Owl alone doubles the base rate. Guarding switches to a separate rate (10% of maximum per second) that ignores these bonuses, and casts and other actions pause regeneration briefly (0.5 s for a Sign), so this is the rate while regenerating, not casts per second.

## 14. Combat skills with file values

| Skill | File-verified behavior |
| --- | --- |
| **Whirl** | 75 / 50 / 37.5 Stamina per second at ranks 1/2/3; once Stamina is empty, 1 / 0.67 / 0.5 Adrenaline per second. Stamina doesn't regenerate while you spin. |
| **Rend** | 50 Stamina per second while charging, so about 2 s from a full bar. A full charge multiplies damage by 2.5; Adrenaline adds a separate ×(1 + 0.1 × rank × points used), and those points are spent: ×3.25 / ×4 / ×4.75 in all at full charge with three points. 1,000 flat armor penetration, like a strong attack. |
| **Deadly Precision** | Any attack opens a 3-second window; a strong attack inside it has a 5% / 10% / 15% instant-kill chance. Successful instant kills share a 15-second cooldown. Immune enemies give 0.05 / 0.1 / 0.15 Adrenaline, half what the description says. |
| **Attack Is the Best Defense** | Per rank: 0.03 Adrenaline per parry, 0.2 per counterattack, 0.1 per dodged attack. It counts attacks that actually miss because you dodged, not dodge presses. |
| **Undying** | Section 4. |

Rend's multipliers apply at their stage of the damage pipeline, not to the final hit compared with a fast attack.

## 15. Skill points

**File-verified:** each level from 2 to 100 gives one point (99 at most), each Place of Power gives one the first time you use it, the Magic Acorn gives two when used and Blood and Wine's Golden Egg gives one. **The Moreau lab gives no point in a first playthrough:** *Turn and Face the Strange* is the only quest in the game that grants skill points, and both of its +1 grants sit behind the check "were mutations already enabled (NG+)". The other branch enables the mutation system instead. New Game+ keeps your level and points rather than handing out another 99. A full-playthrough total still needs the number of reachable Places of Power, so the plans keep assuming about one point per level.

## 16. Other skills with file values

| Skill | File-verified behavior |
| --- | --- |
| **High Tolerance** | At 80% Toxicity or more, adds `0.2 × rank × current ÷ maximum Toxicity` to the crit bonus: +0.16 to +0.2 per rank. The same check multiplies the damage enemies deal you by 1.5. Its 0.3334-per-rank crit multiplier only feeds the tooltip; like Cat's (section 2), it would multiply a base of zero. |
| **Exploding Shield** | When the shield breaks, it hits hostile and neutral targets within 3 game units in line of sight. Rank 1: a stagger roll of `Quen power multiplier ÷ 2 − target resistance`, 50% with no Sign bonus against an unresisting target. Rank 2: also a random 3–12 physical and silver damage, the same at rank 3. Rank 3: also a knockdown roll of 0.15 times the same chance, 7.5% in that case. Superior Petri's Philter makes both rolls certain. While the shield holds, it returns **10% × rank** of absorbed melee damage as shock damage to attackers within about 3.6 units. The Ursine 6-piece bonus raises both damages. |
| **Sun and Stars** | By day: +10 Vitality per second per rank, **outside combat only**; combat uses a separate regeneration attribute. With the base 1/s that's 11/21/31. At night: +1% of maximum Stamina per second per rank, **in combat only**, multiplied by the armor modifier (section 13). |
| **Mutated Skin** | Section 5. |

## 17. Gear levels, skill slots and decoctions

**Item levels (file-verified).** The game computes an item's required level from one stat. A chest needs `⌊1 + (armor − 25) / 5⌋`, trousers and boots `⌊1 + (armor − 5) / 2⌋`, gloves `⌊1 + (armor − 1) / 2⌋`; swords use their summed damage. Every item then loses 1 level, witcher gear 2 more, relics 1 more, and Hearts of Stone witcher and relic gear a further 1. Every set and sword level the book quotes matches this calculation.

**Skill slots and unlocks (file-verified).** Regular slots open at **0, 2, 4, 6, 8, 10, 12, 15, 18, 22, 26 and 30 Ability Points earned**, counting spent, unspent and mutation points, not character level. A skill can be bought once any one of its linked prerequisites has a rank; equipping that prerequisite isn't required.

**Decoctions (file-verified):**

| Decoction | Value in the files | Condition |
| --- | --- | --- |
| Katakan | +10% crit chance | Always |
| Water Hag | +0.5 to the attack-power multiplier | Vitality full |
| Forktail | +0.5 attack power and Sign intensity | After three different action types |
| Chort | +0.25 Sign intensity | Always; knockdowns become staggers, staggers are blocked |
| Ekimmara | 10% of damage dealt returned as Vitality | Always |
| Ekhidna | 10% of maximum Vitality healed | Each one-off Stamina cost, except Rend |
| Archgriffin | All Stamina spent, then 5% of the target's Vitality removed | Strong attacks |
| Ancient Leshen | +2 Stamina per second per Sign cast | In combat, until it ends |
| Griffin | +1% to every resistance per hit taken | Up to 25 stacks |
| Troll | +20 Vitality/s in combat, +100 outside | Always |
| Nightwraith | +50 maximum Vitality per kill | Until meditation |
| Succubus | +1% attack power per stack | Up to 30 stacks |
| Doppler | +0.5 multiplier on a zero crit-damage base | Rear attacks; adds nothing (section 2) |

## What this changes in the build advice

- **Manticore:** the realistic budget is two decoctions with room to drink, three at the edge; four need about 150 recipes. Acquired Tolerance adds about as much as Metabolic Control (20 at 40 recipes, against 30), not the 120 the old figure promised. Euphoria has no fixed cap and counts decoctions, so a full budget still pays. Two decoctions under a 200 maximum also mean a constant Vitality drain. Delayed Recovery can't trigger with two decoctions running unless the maximum tops 222, so the plan now takes Volatile Compound instead, and Fast Metabolism's fivefold drain at rank 1 keeps it on the skip list.
- **Viper:** poison is far more reliable than the skill's 5–15% suggests once the oil matches: 35% per hit at rank 3 with a superior oil, about 45% with a Viper sword. Poison also feeds Metamorphosis. But a long list of monster families, and every enemy 20 or more levels above you, has 100% poison resistance and can't be poisoned at all (section 7).
- **Wolven:** keep Three Strikes 1 as a prerequisite and spend the former extra rank on Wolf School Techniques. Toxic Shock pays once per cooldown on a re-poisoned target, and Melt Armor helps the three fast hits more than the finisher.
- **Griffin:** combat Stamina is resolved: 10/s base in medium armor, superior Tawny Owl the largest single bonus, and only equipped Signs ranks feed the passive. Aftershock's formula alone does not establish a ranking change.
- **Feline:** retain the crit-and-Adrenaline concept, but withdraw the guaranteed 0.35/0.57-normal-hit benefit; Cat School Techniques' crit-damage part and Doppler's back-attack bonus add nothing in combat, so Cat is a +24% fast-attack Technique and crit damage has to come from weapons, Hunter Instinct, High Tolerance and the sword-tree skills. Light armor adds 25% Stamina regeneration.
- **Ursine:** Undying's rank-ups are worth far more than the per-point text suggests; heavy armor costs 25% Stamina regeneration; Melt Armor does little for strong attacks and Rend. Mutated Skin counts only whole Adrenaline points and switches off while Quen is up.
- **Everyone:** an unslotted skill gives nothing, not even its tree's passive.
- **Overall:** these findings correct mechanics and priorities, but do not justify reordering the school verdicts. Those remain playstyle judgments, not benchmark results.

## The remaining numbers worth finding

Prioritize questions by whether the answer could change a build choice:

1. **Attack timing:** fast and strong animation timings, without which damage per hit can't become damage per second. They live in binary animation files.
2. **Recipes:** how many of the 173 eligible recipes a playthrough can learn, which sets the real Toxicity ceiling. This needs the loot, shop and quest-reward tables cross-checked.
3. **Skill-point total:** how many Places of Power are reachable, which needs the world layer files. Quest grants are settled (section 15).
4. **Poison stacking:** how multiple oils and repeated runes interact.
5. **In-game confirmation:** the New Game+ Delayed Recovery reading (section 6) and the zero-base crit multipliers (section 2) follow directly from the files but haven't been tested in play.

**Settled since the previous edition:** Cat School Techniques' and High Tolerance's crit multipliers (they multiply a zero base), New Game+ Delayed Recovery, the poison-resistance list and the creature templates' immunity flags, the Moreau lab grants, Sun and Stars, Exploding Shield, Mutated Skin, the Grandmaster item values and set bonuses, every gear level, and when skill slots open.

## File evidence and reproducibility

The audits read the local game files on **October 9, 2026**. The DX12 executable reported **`5.0.0.1048522`**. These findings apply to that installed build; they do not establish that every 5.0/5.01 build has identical data.

Definitions below are paths **inside `content/content0/bundles/xml.bundle`**, or inside the expansion bundles where marked (Hearts of Stone: `dlc/ep1/data/`; Blood and Wine: `dlc/bob/data/`). They were extracted to a separate directory, and their uncompressed sizes and CRC32 checksums were verified. Script paths are relative to **`content/content0/scripts/`**. No runtime measurements were made. The extraction and search tools are in the repository's [`scripts/`](../scripts/README.md) folder, with steps for repeating the audits on your own install.

| Finding | Definition | Implemented calculation |
| --- | --- | --- |
| Base crit attributes | `gameplay/abilities/geralt_stats.xml`, lines 173–175 | `game/player/r4Player.ws`, `GetCriticalHitChance`; `game/actor.ws`, `GetCriticalHitDamageBonus`; `game/gameplay/damage/damageManagerProcessor.ws`, lines 2510–2515 |
| Toxicity maximum | `gameplay/abilities/geralt_stats.xml`, `ConGeralt`, line 81 | Base attribute; the common player ability supplies a multiplier of 1 |
| Toxicity drain, Toxicity damage and Fast Metabolism | `gameplay/abilities/effects.xml`, `ToxicityEffect`, lines 405–406; `geralt_skills.xml`, `alchemy_s15` | `game/gameplay/effects/effects/drain/toxicity.ws`, lines 63–64, 156–178, 194–200 and 290–306; threshold 0.50001 in `game/gameParams.ws`, line 405 |
| Decoctions and potion costs | `gameplay/items/def_item_alchemy_mutagens.xml`; `gameplay/items/def_item_alchemy_potion.xml` | — |
| Acquired Tolerance | `gameplay/abilities/geralt_skills.xml`, `alchemy_s18`, lines 593–595 | `game/gameplay/ability/PlayerAbilityManager.ws`, lines 2915–2925 and 3582–3603; `game/player/playerWitcher.ws`, lines 4890–4893 |
| Recipe count | `gameplay/items/def_item_alchemy_recipes_*.xml`; the expansions' recipe files | `game/gameplay/alchemy/alchemyTypes.ws`, lines 52–67 |
| Metabolic Control and Manticore armor | `geralt_skills.xml`, `perk_33`, lines 989–991; Blood and Wine `gameplay/items/def_item_crafting_{armor,gloves,pants,boots}.xml`, line 67 | `PlayerAbilityManager.ws`, lines 2861–2868 |
| Euphoria | Blood and Wine `gameplay/abilities/effects_ep2.xml`, `Mutation10Effect`, lines 60–62 | `playerWitcher.ws`, `ApplyMutation10StatBoost` (lines 4754–4767) and `GetPowerStatValue` (lines 8286–8294) |
| Delayed Recovery | `geralt_skills.xml`, `alchemy_s3`, lines 496–501 | `playerWitcher.ws`, lines 7686–7693 and 12837–12856 |
| Volatile Compound | `geralt_skills.xml`, `alchemy_s25` | `damageManagerProcessor.ws`, lines 1899–1905 |
| Poisoned Blades and sword poison | `geralt_skills.xml`, `alchemy_s12`, lines 554–558; `gameplay/items/def_item_alchemy_oils.xml`; Hearts of Stone `gameplay/items/def_item_crafting_weapons.xml`, lines 48–74 | `damageManagerProcessor.ws`, lines 751–774; `game/components/inventoryComponent.ws`, lines 2167–2213; `game/gameplay/effects/effectManager.ws`, lines 1470–1490 |
| Poison effect and Toxic Shock | `gameplay/abilities/effects.xml`, `PoisonEffect`, lines 277–281; `geralt_skills.xml`, `alchemy_s23`, lines 884–888 | `game/gameplay/effects/effects/dotEffect.ws`, lines 137–186; `damageManagerProcessor.ws`, lines 1629–1660 |
| Viper Techniques, Potent Sting, Debilitating Poison, Metamorphosis | `geralt_skills.xml`, `perk_28`, `alchemy_s26`, `alchemy_s22` | `damageManagerProcessor.ws`, lines 1992–2041 and 2550–2563; `dotEffect.ws`, lines 101–108 |
| School Techniques | `geralt_skills.xml`, `perk_23` to `perk_28`, lines 921–958 | `PlayerAbilityManager.ws`, `SetPerkArmorBonus` |
| Combat Stamina | `geralt_stats.xml`, lines 77–93; `geralt_skills.xml`, lines 251–254 and 927–931; `gameplay/abilities/effects_potions.xml`, lines 144–155; Blood and Wine `effects_ep2.xml`, lines 25–31; `gameplay/abilities/effects_mutagens.xml`, lines 95–99; the armor `def_item_crafting_*.xml` files | `game/gameplay/effects/effects/regen/regenEffect.ws`, lines 39–45; `game/gameplay/effects/effects/auto/staminaRegen.ws`, lines 37–56; `playerWitcher.ws`, `CalculatedArmorStaminaRegenBonus` (lines 8678–8728) |
| Outside-combat Stamina | `gameplay/abilities/geralt_stats.xml`, lines 77 and 92–93 | `staminaRegen.ws`, lines 37–45; `regenEffect.ws`, lines 39–59 |
| Branch passives | `geralt_skills.xml`, `sword_adrenalinegain`, `magic_staminaregen`, `alchemy_potionduration`, `survival_vitality` | `PlayerAbilityManager.ws`, `AddSkillPassiveBonusesForEquipped`, lines 147–180; bombs in `damageManagerProcessor.ws`, lines 1869–1875 |
| Strong attacks and defenses | `gameplay/abilities/basic_attacks.xml`, line 12; `geralt_skills.xml`, `sword_2`, lines 99–102; enemy armor in `gameplay/abilities/monster_base_abl.xml` and `opp_base_abl.xml` | `damageManagerProcessor.ws`, lines 2427, 2533–2644 and 2888 |
| Undying | `geralt_skills.xml`, `sword_s18`, lines 222–227 | `playerWitcher.ws`, lines 2551–2571 |
| Whirl, Rend, Deadly Precision, Attack Is the Best Defense | `geralt_skills.xml`, `sword_s35`, `sword_s2`, `sword_s30`, `perk_31` | `playerWitcher.ws`, lines 3518–3623 and 10809–10828; `damageManagerProcessor.ws`, lines 634–732 and 1724–1746 |
| Three Strikes | `gameplay/abilities/geralt_skills.xml`, `sword_s24`, lines 686–691 | `game/gameplay/damage/damageManagerProcessor.ws`, lines 1126–1178 and 1428–1443 |
| Melt Armor | `gameplay/abilities/geralt_skills.xml`, `magic_s8`, lines 389–395 | `game/gameplay/projectile/signs/signProjectiles.ws`, lines 525–534; denominator 2 in `game/gameParams.ws`, line 445 |
| Aftershock | `gameplay/abilities/geralt_skills.xml`, `magic_s40`, lines 855–858 | `game/player/playerWitcher.ws`, lines 9491–9533; `game/gameplay/effects/effects/skill/overloadCooldown.ws`; `game/gameplay/actions/baseAction.ws`, lines 576–584; `damageManagerProcessor.ws`, line 2693 |
| Conductors of Magic, Magic Sensibilities | Blood and Wine `gameplay/abilities/geralt_mutations.xml`, lines 6–14 | `damageManagerProcessor.ws`, lines 805–822, 1916–1944 and 2684–2693; `playerWitcher.ws`, lines 4461–4490 |
| Skill points | `gameplay/abilities/geralt_levelups.xml`; Blood and Wine quest graph `quests/minor_quests/quest_files/mq7023_mutations.w2phase` (in `bob.bundle`), the only quest graph that calls `AddSkillPoints` | `game/gameplay/leveling/levelManager.ws`; `game/gameplay/interactive/placeOfPowerEntity.ws`, lines 241–248; `playerWitcher.ws`, lines 5504–5536; `game/quests/quest_function.ws`, `AddSkillPoints` |
| Crit-damage aggregation (Cat, High Tolerance, Doppler) | `geralt_stats.xml`, line 175 (`add` 0.25); `geralt_skills.xml`, `perk_23` line 923 and `alchemy_s24` line 897 (`mult`); `effects_mutagens.xml`, `Mutagen11Effect`, line 44 (`mult`); no `base` crit-damage entry in any definition file | `game/types.ws`, `CalculateAttributeValue`, line 605; `damageManagerProcessor.ws`, lines 2483–2516; `PlayerAbilityManager.ws`, `SetPerkArmorBonus` and `UpdatePerkArmorBonus`, lines 3372–3470; `playerWitcher.ws`, lines 2768–2797 and 8732–8748; panel formula at line 8782 |
| High Tolerance damage taken | `geralt_skills.xml`, `alchemy_s24`, lines 893–898 | `damageManagerProcessor.ws`, lines 2003–2014 |
| Poison resistance | `poison_resistance_perc` in `gameplay/abilities/monster_base_abl.xml`, `monster_base_abl_new.xml` (`MonsterLevelBonusDeadly`) and `opp_base_abl.xml` (`NPCLevelBonusDeadly`), and the expansions' `monster_base_abl.xml` / `monster_bob_base_abl.xml` | `game/gameplay/effects/effects/baseEffect.ws`, `CalculateDuration`, lines 297–323; `dotEffect.ws`, lines 208–218; level bonus in `game/npc/npc.ws`, line 1414, with `LEVEL_DIFF_DEADLY = 20` in `gameParams.ws`, line 457 |
| Mutated Skin | Blood and Wine `gameplay/abilities/geralt_mutations.xml`, `Mutation5`, line 24 | `playerWitcher.ws`, lines 2487–2512 |
| Exploding Shield | `geralt_skills.xml`, `magic_s13`, lines 425–433 | `playerWitcher.ws`, `QuenImpulse`, lines 9359–9440; `game/gameplay/items/spells/quenEntity.ws`, lines 96–107, 601–612 and 629–641; `effectManager.ws`, `GetSignApplyBuffTest`, lines 1540–1628 |
| Sun and Stars | `geralt_skills.xml`, `perk_38`, lines 1028–1043 | `PlayerAbilityManager.ws`, `SetPerk38Abilities`, lines 3510–3540; `game/gameplay/effects/effects/auto/vitalityRegen.ws` and `staminaRegen.ws` |
| Item levels | Every `def_item_crafting_*.xml`, the free-DLC files in `dlc0.bundle` (`dlc/dlc*/data/gameplay/items/`) | `game/components/inventoryComponent.ws`, `GetItemLevel`, lines 305–400; `game/gameParams.ws`, `GetItemLevel`, lines 917–1021; reproduced by `scripts/item_levels.py` |
| Skill slots and unlocks | `geralt_skills.xml`, `<skill_slots>`, lines 2162–2179; the `required_skills` and `isAlternative` attributes of each skill | `PlayerAbilityManager.ws`, lines 337–349 and 2590–2606 (slots), `CanLearnSkill`, lines 2042–2103 |
| Creature immunities | `CBuffImmunityParam` objects in the creature templates, `characters/npc_entities/monsters/*.w2ent` in `blob.bundle`, `bob.bundle`, `ep1.bundle` and `dlc0.bundle` | `game/actor.ws`, `IsImmuneToBuff`, lines 4032–4087; reproduced by `scripts/buff_immunities.py` |
| Set bonuses | Blood and Wine `gameplay/abilities/geralt_skills_ep2.xml`, lines 29–60; `effects_ep2.xml`, lines 20–38 | `damageManagerProcessor.ws`, lines 1783–1866; `effectManager.ws`, line 863; `quenEntity.ws`, lines 96–107 and 320–345; `playerWitcher.ws`, lines 3065, 7443 and 9359–9440; `inventoryComponent.ws`, lines 3780–3810; `petard.ws`, line 319 |
| Decoctions | `gameplay/abilities/effects_mutagens.xml`; `gameplay/items/def_item_alchemy_mutagens.xml` | `game/gameplay/effects/effects/mutagens/`; `effectManager.ws`, lines 821–833 (Chort); `PlayerAbilityManager.ws`, lines 2385–2389 (Ekhidna); `damageManagerProcessor.ws`, lines 2483–2526 (Water Hag, Doppler) |
| New Game+ | `gameplay/abilities_plus/` and `gameplay/items_plus/` | `playerWitcher.ws`, `NewGamePlusInitialize`, lines 1089–1260; `game/npc/npc.ws`, lines 613–628 and 1260–1263; `gameParams.ws`, lines 313–318 and 1024–1040 |
| Grandmaster items | Blood and Wine `gameplay/items/def_item_crafting_{armor,gloves,pants,boots,weapons}.xml` (`… 4 _Stats` chests and swords, `… 5 _Stats` other pieces; Manticore is `Red Wolf … 1`, and `Red Wolf … 2` is its New Game+ version) | — |

The normal-game and NG+ base definitions agree for the reported crit attributes, maximum Toxicity and regeneration rates. The exception is Delayed Recovery: `gameplay/abilities_plus/geralt_skills.xml`, lines 497–500, defines only an obsolete single threshold, while `playerWitcher.ws`, `GetAlchemyS03Threshold` (lines 12837–12856), reads three rank-specific attributes that are missing there. The installed Brothers In Arms `effects.xml` override retains the same `ToxicityEffect` rate. A second, independent read of the same files re-checked the definitions above and the main script paths for Acquired Tolerance, Delayed Recovery, Euphoria, Poisoned Blades, combat Stamina, strong attacks, Undying, Toxic Shock and the two Sign mutations, and added the branch passives, Toxicity damage, Fast Metabolism, Volatile Compound, potion costs and the recipe count. This is a baseline mechanics audit, not a claim that every installed mod or every conditional build interaction has been validated.

## Sources

- [witcherhour.com: Witcher 3 skills](https://witcherhour.com/skills/)
- [WitcherDB: Remastered build planner](https://witcherdb.com/build-planner)
- [Hack the Minotaur: New skill trees](https://hacktheminotaur.com/the-witcher-3/the-witcher-3-remastered-new-skill-trees-guide/)
- [KeenGamer: All mutations](https://www.keengamer.com/articles/guides/the-witcher-3-remastered-all-mutations-how-to-unlock-them/)
- [Fextralife: Decoctions](https://thewitcher3.wiki.fextralife.com/Decoctions), [Katakan Decoction](https://thewitcher3.wiki.fextralife.com/Katakan+Decoction), [Potions](https://thewitcher3.wiki.fextralife.com/Potions)
- [Console Pulse: Toxicity, overdose and Delayed Recovery](https://consolepulse.com/multiplatform/the-witcher/guides/witcher-3-toxicity-overdose-delayed-recovery-guide)
- [Gamestegy: Grandmaster Griffin armor](https://gamestegy.com/witcher-3/wiki/1335/grandmaster-griffin-armor)

<!-- nav -->

---

[← 18. Missables: one-time gear](18-missables.md) · [Contents](../README.md) · [20. Common mistakes, and how to respec →](20-mistakes-and-respec.md)
