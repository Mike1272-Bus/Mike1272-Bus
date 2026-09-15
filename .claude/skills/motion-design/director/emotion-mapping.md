# Emotion Mapping — target feeling to motion parameters

A lookup from the emotion a moment should evoke to concrete motion parameters. Cross-reference with the project's archetype (`motion-personality.md`): the emotion sets direction, the archetype sets how far and how it's textured.

| Emotion | Duration | Easing | Overshoot | Secondary motion | Notes |
|---|---|---|---|---|---|
| **Trust / reliability** | 150-250ms | smooth ease-out, no elastic | none | none | Consistency matters more than any single instance — same parameters every time this state occurs. |
| **Urgency** | 80-150ms | sharp ease-out or linear-ish | none, or a single hard flash | a pulse/flash accent color | Speed itself communicates urgency; a slow "urgent" animation is a contradiction the viewer will feel even if they can't name it. |
| **Delight / celebration** | 300-600ms total sequence | elastic or back.out with visible overshoot | yes, generous | confetti/particles, secondary bounce | This is the one place to spend your biggest motion budget — reserve elasticity for genuine wins so it stays special. |
| **Calm / reassurance** | 300-500ms | very soft ease (expo-out family) | none | gentle fade paired with movement | Pair movement with opacity fade, not movement alone — a fade softens arrival. |
| **Confidence** | 150-250ms | firm ease-out, decisive | small (5-10%), not elastic | none | Arrives and plants — no wobble, no hesitation, no overshoot correction. |
| **Playfulness** | 200-350ms | back.out with moderate overshoot | yes, moderate | small wiggle/rotation | Fine for routine interactions in a Playful-archetype product; reserve for emphasis-only in other archetypes. |
| **Surprise** | very fast onset (<100ms), then hold | sharp in, soft out | can be large | flash or scale-punch | The suddenness IS the surprise — anticipation (Disney principle #2) should be minimal or absent here, on purpose. |
| **Anticipation / buildup** | 200-400ms lead-in before the payoff | ease-in (slow start, building) | none during buildup | a small counter-move (Disney #2) | The buildup itself should NOT resolve the tension — save the release for the payoff beat. |
| **Sadness / error / failure** | 200-350ms | soft ease, slightly heavier/slower than neutral | none, or a small "sink" (slight downward settle) | muted color shift, no bright flash | Avoid bounce or elastic here entirely — it reads as mocking rather than sympathetic. |
| **Focus / concentration** | minimal — near-instant or no motion at all | — | — | — | The correct motion for "help the user focus" is often *the absence of motion*. Ambient/looping motion near a focused task is a bug, not a feature (see `context-adaptation.md`). |

## Compound and transitional emotions

Real moments are rarely one pure emotion. A "success after a long wait" moment is both **relief** (calm parameters: soft ease, fade) and **delight** (celebration parameters: overshoot, secondary motion) — sequence them: relief beat first (the tension releases), delight beat second (the reward lands), rather than trying to blend both parameter sets into one confused tween. This sequencing is exactly the micro-story shape in `narrative-structure.md`.

## Using this table

1. Name the emotion (or compound emotion) from `core-philosophy.md` Pillar 1's purpose statement.
2. Pull the row's parameters as a *starting point*, not gospel.
3. Adjust intensity to the project's archetype — a Precise-archetype product's "delight" still won't overshoot as much as a Playful-archetype product's "delight," but it should still overshoot *more than its own baseline* to register as the special emotion.
4. If two adjacent moments in the same flow map to very different rows, that's a signal there needs to be a transitional beat between them (see `narrative-structure.md`) rather than an instant emotional whiplash.
