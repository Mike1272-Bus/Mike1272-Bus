# Timing & Easing Tables

Concrete numbers. Pull from here once purpose/personality/emotion are decided (`director/decision-framework.md` steps 1-3); don't start here.

## Duration bands by category

| Category | Duration | Notes |
|---|---|---|
| Micro-feedback (hover, press) | 80-150ms | Fires constantly — must never fatigue. See `patterns/state-feedback.md`. |
| Standard UI transition (tab switch, dropdown, tooltip) | 150-250ms | The default band for "something changed, no big deal." |
| Entrance / exit of a discrete element (card, modal, toast) | 200-350ms | Slightly longer than standard UI since there's more to visually resolve. |
| Emphasis / hero moment (success celebration, brand reveal) | 300-600ms | The one place to deliberately spend more time — but see Narrative Structure's payoff-hold, which is separate from and additional to this build duration. |
| Full-scene transition (video beat change, page transition) | 150-400ms for the cut/wipe itself | The *content* of the new scene holds far longer than this — this number is just the transition mechanism. |
| Ambient loop period | 2-4s per cycle | Longer than intuition suggests; see `patterns/ambient-continuous.md` on why ambient wants to be slow. |
| Payoff hold (stillness after motion resolves) | 100-150ms minimum, 400ms+ for anything meaningful | Not optional — see `director/narrative-structure.md`. |

Adjust up for: larger/heavier-feeling elements, longer travel distance, Elegant archetype, higher emotional weight. Adjust down for: high-frequency interactions, Precise archetype, urgency-mapped moments.

## Easing curves by intent

| Intent | Curve (cubic-bezier or named) | GSAP equivalent |
|---|---|---|
| Entrance (arriving) | ease-out: `cubic-bezier(0.16, 1, 0.3, 1)` (soft) or `cubic-bezier(0.4, 0, 0.2, 1)` (standard/Precise) | `power2.out` / `power3.out` |
| Exit (leaving) | ease-in: `cubic-bezier(0.7, 0, 0.84, 0)` | `power2.in` |
| Standard bidirectional transition | ease-in-out: `cubic-bezier(0.65, 0, 0.35, 1)` | `power2.inOut` |
| Playful / Bold overshoot | back-out with tunable overshoot | `back.out(1.4)` (subtle) to `back.out(2.4)` (strong) |
| Delight / celebration | elastic, sparingly | `elastic.out(1, 0.5)` — the second param controls how "springy" vs. "damped" |
| Mechanical / deliberately artificial (progress bars, hard wipes) | linear, or a near-linear curve | `none` / `linear` |
| Elegant / premium slow settle | expo-out family, very soft | `expo.out` or `cubic-bezier(0.19, 1, 0.22, 1)` |
| Ambient / breathing loops | sine-based, smooth both directions | `sine.inOut` |
| Anticipation (small counter-move before main action) | ease-in, short | `power1.in`, very short duration (60-100ms) |

## Overshoot amount by archetype

| Archetype | Overshoot | Practical value |
|---|---|---|
| Precise | none | scale/position lands exactly at target, no back-ease |
| Elegant | none to barely perceptible | if any, <2% scale deviation, immediately settling |
| Playful | moderate | `back.out(1.7)`-ish; 3-8% scale overshoot |
| Bold | moderate to strong for emphasis moments, restrained for routine ones | `back.out(2)-back.out(2.6)` on hero moments; closer to Precise on routine UI within a Bold product |

## Stagger delay by list length

| List length | Per-item delay |
|---|---|
| 2-5 items | 60-100ms |
| 6-10 items | 40-70ms |
| 11-20 items | 25-40ms, or switch to batched-group stagger (`patterns/multi-element.md`) |
| 20+ items | batched-group stagger; linear per-item stagger stops working past this point |

## Quick lookup shortcut

Purpose is functional/routine (Precise-leaning, high frequency) → short duration band, ease-out standard, zero overshoot.
Purpose is emphasis/celebration → longer duration band + payoff hold, back/elastic easing, real overshoot.
Purpose is ambient → long period, sine easing, minimal amplitude — no overshoot concept applies.
