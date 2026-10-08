# 19. The maths behind the choices

This chapter collects every calculation in the book in one place, with the assumptions spelled out. The school chapters use these results; here you can check the working.

## Ground rules

- **Separate file evidence from published descriptions.** A local file audit on October 9, 2026 used the installed executable version `5.0.0.1048522`. The values marked **file-verified** below come from that build's definitions and scripts. They are not in-game timing or damage measurements.
- **Other values still come from community sources.** [witcherhour.com](https://witcherhour.com/skills/), [WitcherDB](https://witcherdb.com/build-planner) and [Hack the Minotaur](https://hacktheminotaur.com/the-witcher-3/the-witcher-3-remastered-new-skill-trees-guide/) supply the remaining skill descriptions. Older item and potion values remain provisional where this audit did not check them.
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
| Stamina regeneration, outside combat | **100% of maximum Stamina/s** | Normally 100 points/s; only while regeneration is active |

The base crit attributes, Toxicity maximum and Stamina attributes also agree between normal-game and NG+ definitions. The installed Brothers In Arms override retains the same baseline Toxicity drain. Action-related pauses can delay Stamina recovery; the outside-combat rate does not establish combat casting frequency. See [file evidence](#file-evidence-and-reproducibility) for paths and functions.

## 1. A basic combo: which skills actually activate

The Wolven sequence is a dodge, three fast attacks and a strong finisher. Muscle Memory covers more of those fast attacks as its rank rises. Strength Training supports the finisher, and Toxic Shock needs poison on the target. Their published rank descriptions still explain the sequence, but they do not by themselves establish its total damage.

The earlier **+23% at rank 1 / +89% at rank 3** illustration is withdrawn as a build comparison. It assumed that a strong hit is twice a fast hit and applied Wolf School Techniques as a separate multiplier on the completed combo. The audit has not established the attack ratio or all interactions, so neither those totals nor the associated chart should be treated as measured gains.

**Three Strikes does not activate in this repeating three-fast/one-strong sequence.** Its implementation checks the fourth consecutive matching attack; switching between fast and strong resets the other counter. Keep rank 1 to unlock Razor Focus and Undying, but prioritize another useful rank or slot if this is your usual rotation. Section 10 gives the boost for a sequence that does activate it.

Melt Armor can support the melee follow-up against armored targets. Its armor reduction cannot be added to the combo as an equivalent damage percentage without knowing the target's armor and the mitigation calculation.

## 2. School Techniques: what can be compared

The published rank-3 descriptions for four matching armor pieces remain useful as a list of effects. They are not a verified ranking of final damage:

| Technique | Published benefit relevant to this comparison |
| --- | --- |
| **Wolf** | +24% weapon damage and +24% Sign intensity |
| **Manticore** | +24% sword damage and +24% bomb damage |
| **Cat** | +24% fast-attack damage and +96% critical-damage bonus |
| **Bear** | +24% strong-attack damage and +24% maximum Vitality |
| **Griffin** | +24% Sign intensity; the combat Stamina benefit needs a separate audit |
| **Viper** | +24% poison damage and +24% maximum Vitality |

The earlier “units added” comparison depended on the withdrawn combo model. Matching weapon-damage labels do not prove equal final damage once crits, armor, skill activation and attack timing enter the calculation. In particular, Cat's critical-damage attribute must be traced through its own calculation before its displayed bonus is inserted into a damage model.

Choose the Technique that supports the build's actions. These findings do not establish a new ordering of the schools.

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

This corrects the former claim that the Feline crit package guarantees **0.35**, or **0.57** against an oiled target, additional normal hits per swing. Those lower bounds did not account for the existing attack-power multiplier or the complete critical-bonus calculation. Do not replace them with a new bound by simply adding 0.25 to Cat's published percentage.

Crit chance and the resolved crit bonus still work together. The size of the benefit needs the actual weapon, skills, other damage bonuses and target. Feline remains a coherent crit build, but this audit does not prove its superiority to another sword build.

## 4. Adrenaline: the Undying floor

Undying restores 10% Vitality per Adrenaline point when you'd die. Razor Focus guarantees one point at the start of every fight, so Undying has at least that much to work with when a fight opens (hits, Rend and Whirl can still empty the bar later):

| Adrenaline held | Vitality restored by Undying |
| --- | --- |
| 1 (fight start, with Razor Focus) | 10% |
| 2 | 20% |
| 3 (full bar) | 30% |

Without Razor Focus, the first big hit of a fight can kill you with Undying sitting empty, which is why the plans buy Razor Focus before Undying or alongside it. The rank 2 and 3 values carry an extra "33% / 67% bonus" that no source explains.

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

A full bar nearly doubles how long you last compared with an empty one (2.69 against 1.48), which is the trade-off against spending the same three points on a rank-3 Rend (+90% on one strike). Chapter 10.

## 6. The Toxicity budget and Euphoria

![How many decoctions fit at different maximum Toxicity levels, from one with no skills to four with Acquired Tolerance rank 3 plus Metabolic Control and Manticore armor](../images/toxicity-budget.png)

Each decoction locks 50 Toxicity until it ends, so:

```math
\text{decoctions} = \left\lfloor \frac{\text{max Toxicity} - \text{room for potions}}{50} \right\rfloor
```

```math
\text{max Toxicity} = 100 + a \times \text{recipes known} + 10\,k + 5 \times \text{Manticore pieces}
```

where `a` is Acquired Tolerance's rank (+1/2/3 per recipe) and `k` is Metabolic Control's rank (+10/20/30). The **base of 100 is now file-verified** for build `5.0.0.1048522`. Manticore's +5 per piece remains an older value not checked in this audit. At 40 recipes, rank-3 Acquired Tolerance alone adds 120, more than any other source.

**Euphoria** adds 0.75% sword damage and Sign intensity per Toxicity point, so each decoction held is worth +37.5% (+75% for two, +150% for four). Sources disagree on the cap (a flat 75%, or rising with your maximum), and two guides report that 5.0 weakened it, so treat those as upper bounds. Chapter 12.

**Potion Toxicity recovery is now known.** Without modifiers, clearing `T` points takes `T / 0.25` seconds in combat or `T / 0.275` outside combat, if the combat state stays unchanged. For example, 20 points take **80 seconds** in combat or about **72.7 seconds** outside it. This describes potion Toxicity, not the amount reserved by active decoctions. Fast Metabolism and other modifiers change the rate; the Euphoria cap and Delayed Recovery's disputed behavior still need their own checks.

## 7. Poison: how many hits it takes

![Chance the target is poisoned after a number of oiled hits, at 5%, 15% and 30% per hit](../images/poison-odds.png)

```math
P_{\text{poisoned}}(n) = 1 - (1 - p)^n
```

| Chance per hit | After 3 hits | After 6 hits | Hits for even odds |
| --- | --- | --- | --- |
| 5% (Poisoned Blades rank 1) | 14% | 26% | 14 |
| 15% (rank 3, or the Viper steel sword alone) | 39% | 62% | 5 |
| 30% (rank 3 plus a Venomous sword, if they add) | 66% | 88% | 2 |

If the sword's roll and the skill's roll are separate, the combined chance is 1 − 0.85 × 0.85 ≈ 28% rather than 30%; no source confirms which. Toxic Shock fires at most every 5 seconds, so poison chance beyond what you need to have the target poisoned each cooldown only adds damage over time. Chapter 13.

## 8. Sign intensity

![Sign intensity added by each source, fully upgraded: Griffin set inside Yrden +100%, Catalyst +90%, Focus +90%, Chain Reaction +75%, Petri's Philter +25%, Griffin Techniques +24%, Grandmaster chest +22%, Grandmaster steel sword +21%](../images/sign-intensity.png)

The two largest bonuses need Yrden: Catalyst only counts against enemies inside it, and the Griffin set bonus only while you stand in your own trap. Focus needs a full bar, and Chain Reaction five casts in a row, each a different Sign from the one before. The flat sources (potion, Technique, armor, sword) are what you have in every fight. Chapter 9.

## 9. Branch passives

Every point you spend earns its tree a small passive: Combat +1% Adrenaline gain, Signs +0.5% combat Stamina regeneration, Alchemy +2% potion duration and bomb damage, General +1% Vitality ([Hack the Minotaur](https://hacktheminotaur.com/the-witcher-3/the-witcher-3-remastered-new-skill-trees-guide/)). They're small per point but they make stepping-stone skills worth something.

Sources disagree on two details: witcherhour gives the Signs bonus as +0.5 Stamina per second rather than +0.5%, and says only equipped skills count toward the passives, while Hack the Minotaur counts every point (chapter 21).

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

**Recommendation:** Igni before melee remains useful against armored enemies. A 25-point armor-multiplier reduction is not a 25% damage increase; target armor and mitigation determine the benefit.

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

This is why **15/30/45 is not a final-damage table**. Both global power and the cast Sign's power can matter; target mitigation and other processing still follow. Alternate casts also have cooldown gating in the inspected invocation path.

**Recommendation:** treat Aftershock as close-range damage on the route to Resonance, not a proven reason to replace another core skill. Its practical value needs measured damage, target coverage and activation frequency.

## What this changes in the build advice

- **Wolven:** keep Three Strikes 1 as a prerequisite; for the stated three-fast/strong loop, spend the former extra rank on Wolf School Techniques and use the active slot for a skill that can activate.
- **Feline:** retain the crit-and-Adrenaline concept, but withdraw the guaranteed 0.35/0.57-normal-hit benefit and comparisons that relied on it.
- **Manticore:** the 100-point starting Toxicity budget is confirmed. This does not settle Euphoria's cap or prove the highest damage ceiling.
- **Griffin:** the outside-combat Stamina result does not determine combat casting speed. Aftershock's formula alone does not establish a ranking change.
- **Overall:** these findings correct mechanics and priorities, but do not justify reordering the school verdicts. Those remain playstyle judgments, not benchmark results.

## The remaining numbers worth finding

Prioritize questions by whether the answer could change a build choice:

1. **Euphoria and Delayed Recovery:** actual conversion, cap, which Toxicity pool counts, and the disputed potion-extension behavior. These directly affect Manticore's claimed ceiling.
2. **Combat Stamina:** base rate, armor-weight effects, Griffin Techniques, and whether the Signs passive uses flat points or a percentage and counts spent or equipped ranks. The installed `perk_24` coefficient is `staminaRegen mult = 0.002` per rank/piece, implying 2.4 points/s for rank 3, four medium pieces and 100 maximum Stamina before armor modifiers, rather than the community description's +4/s. The total rate needs a complete combat-regeneration check.
3. **Sword damage:** fast/strong damage and attack times; the full modifier order, including Cat's crit bonus; armor piercing and mitigation. Damage per hit alone cannot establish damage per second.
4. **Poison and Toxic Shock:** combined poison rolls, duration, immunity/resistance, consumption and cooldown. These determine Viper's consistency and the Wolven finisher's expected return.
5. **Sign damage and mutations:** practical Aftershock activation and scaling; Conductors of Magic and Magic Sensibilities interactions.
6. **Skill-point budget:** attainable points, mutually exclusive rewards, expansion content and NG+ scope. Define the playthrough before giving one total.

Other unresolved entries in the skill reference include Whirl's base cost, Rend's Stamina scaling, Deadly Precision's kill chance, Undying's rank scaling, and the Adrenaline generated by Attack Is the Best Defense.

## File evidence and reproducibility

The audit read the local game files on **October 9, 2026**. The DX12 executable reported **`5.0.0.1048522`**. These findings apply to that installed build; they do not establish that every 5.0/5.01 build has identical data.

Definitions below are paths **inside `content/content0/bundles/xml.bundle`**. They were extracted to a separate directory, and their uncompressed sizes and CRC32 checksums were verified. Script paths are relative to **`content/content0/scripts/`**. No runtime measurements were made.

| Finding | Definition | Implemented calculation |
| --- | --- | --- |
| Base crit attributes | `gameplay/abilities/geralt_stats.xml`, lines 173–175 | `game/player/r4Player.ws`, `GetCriticalHitChance`; `game/actor.ws`, `GetCriticalHitDamageBonus`; `game/gameplay/damage/damageManagerProcessor.ws`, lines 2510–2515 |
| Toxicity maximum | `gameplay/abilities/geralt_stats.xml`, `ConGeralt`, line 81 | Base attribute; the common player ability supplies a multiplier of 1 |
| Toxicity drain | `gameplay/abilities/effects.xml`, `ToxicityEffect`, line 405 | `game/gameplay/effects/effects/drain/toxicity.ws`, lines 194–200 |
| Outside-combat Stamina | `gameplay/abilities/geralt_stats.xml`, lines 77 and 92–93 | `game/gameplay/effects/effects/auto/staminaRegen.ws`, lines 37–45; `game/gameplay/effects/effects/regen/regenEffect.ws`, lines 39–59 |
| Griffin Stamina coefficient | `gameplay/abilities/geralt_skills.xml`, `perk_24`, lines 927–931 | `game/gameplay/ability/PlayerAbilityManager.ws`, `SetPerkArmorBonus`; `game/gameplay/effects/effects/regen/regenEffect.ws`, lines 39–45 |
| Three Strikes | `gameplay/abilities/geralt_skills.xml`, `sword_s24`, lines 686–691 | `game/gameplay/damage/damageManagerProcessor.ws`, lines 1126–1178 and 1428–1443 |
| Melt Armor | `gameplay/abilities/geralt_skills.xml`, `magic_s8`, lines 389–395 | `game/gameplay/projectile/signs/signProjectiles.ws`, lines 525–534; denominator 2 in `game/gameParams.ws`, line 445 |
| Aftershock | `gameplay/abilities/geralt_skills.xml`, `magic_s40`, lines 855–858 | `game/player/playerWitcher.ws`, lines 9491–9533; `game/gameplay/actions/baseAction.ws`, lines 576–584; `game/gameplay/damage/damageManagerProcessor.ws`, line 2693 |

The normal-game and NG+ base definitions agree for the reported crit attributes, maximum Toxicity and regeneration rates. The installed Brothers In Arms `effects.xml` override retains the same `ToxicityEffect` rate. This is a baseline mechanics audit, not a claim that every installed mod or every conditional build interaction has been validated.

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
