# Troubleshooting — animation smells and fixes

Named symptoms, mapped to root cause and fix. Use this when the quality checklist technically passes but something still feels wrong and you can't articulate why.

## "Linear-everywhere"
**Symptom:** motion feels robotic, cheap, or slightly nauseating even though nothing is technically broken.
**Cause:** linear easing used on motion meant to feel natural (see `director/disney-principles.md` #6, Slow In Slow Out).
**Fix:** apply ease-out to entrances, ease-in to exits, ease-in-out to bidirectional transitions (`reference/timing-easing-tables.md`). Reserve linear exclusively for deliberately mechanical moments (progress bars, hard wipes).

## "Uniform-duration"
**Symptom:** a sequence of different-sized/different-importance elements all animate in exactly the same time, and the whole thing feels flat despite each individual motion being fine.
**Cause:** duration wasn't varied by size/weight/importance (Pillar 2, physics + Pillar 1, purpose/hierarchy).
**Fix:** scale duration slightly with size/mass and with narrative importance — the hero element gets more time than a routine sibling, per `director/core-philosophy.md`.

## "Motion for motion's sake"
**Symptom:** the animation is polished but pointless; removing it changes nothing meaningful.
**Cause:** skipped `director/decision-framework.md` step 1 — no real purpose was ever named.
**Fix:** name the purpose honestly. If there isn't one, cut the animation. Decoration dressed as motion design is the fastest way to make a product feel try-hard.

## "Competing leaders"
**Symptom:** a multi-element scene feels chaotic even though each element's individual tween is well-crafted.
**Cause:** no single leader was designated (`director/choreography.md`) — multiple elements move with equal visual weight/timing, and the eye doesn't know where to look first.
**Fix:** pick one leader per beat. Demote everything else to follower or ambient. If two things genuinely both need to lead, split into two beats instead (`director/narrative-structure.md`).

## "No payoff"
**Symptom:** motion resolves but doesn't feel *finished* — viewer isn't sure it's over, or the next thing happens too fast to register the last thing landed.
**Cause:** missing hold at the end (`director/narrative-structure.md`'s payoff beat).
**Fix:** add a genuine stillness period after the motion resolves — minimum 100-150ms for micro-interactions, 400ms+ for anything meaningful, before allowing the next action or cutting away.

## "Everything bounces"
**Symptom:** a Playful/Bold product feels exhausting or unserious even in low-stakes routine interactions.
**Cause:** overshoot/elasticity applied uniformly regardless of how much a given moment actually matters (`director/emotion-mapping.md`, `director/motion-personality.md`'s per-archetype risk notes).
**Fix:** reserve strong overshoot for genuine emphasis/delight moments; keep routine, high-frequency interactions (hover, tab switch) closer to zero-overshoot even within a bouncy archetype.

## "Dead on arrival" / no anticipation
**Symptom:** the motion is technically smooth but feels abrupt or unearned, especially on larger/more dramatic movements.
**Cause:** missing anticipation beat (`director/disney-principles.md` #2) before a large action.
**Fix:** add a small (60-100ms), opposite-direction counter-move immediately before the main action, especially for anything with real visual weight or narrative importance.

## "Rigid group" / disconnected parts
**Symptom:** an element and its supporting decoration (shadow, icon, label) look like they're glued together rather than belonging together — or worse, look like two unrelated things that happen to overlap.
**Cause:** children animated with fully independent easing/timing instead of a shared transform + small follow-through offset (`director/disney-principles.md` #5, `patterns/multi-element.md`'s parent-child recipe).
**Fix:** drive the group from one transform source; give supporting elements only a small timing lag (30-50ms) and slightly softer easing, never a fully independent curve.

## "Jank" / dropped frames
**Symptom:** motion that looks smooth in isolated preview stutters in the real product, especially with multiple elements or on lower-end devices.
**Cause:** animating layout-triggering properties (`top`/`left`/`width`/`height`/`margin`) instead of compositor-cheap ones.
**Fix:** switch to `transform`/`opacity` per `reference/property-selection.md`; reduce the count of simultaneously-animating elements if the budget is still tight.

## "Broken mid-transition"
**Symptom:** an otherwise fine entrance/exit or morph looks glitchy or visually wrong specifically in the middle of the transition, even though start and end frames both look correct.
**Cause:** failed the freeze-frame test (`director/disney-principles.md` #11 and #12) — the interpolation path between two states isn't visually coherent.
**Fix:** check the actual midpoint frame. Either choose a shape/property pair that interpolates cleanly, or mask the ugly middle with a timed opacity cross-fade so the viewer never actually sees the bad intermediate frame at full visibility.

## "Same energy throughout"
**Symptom:** a longer sequence (a video, a multi-step flow) feels monotonous even though no individual beat is bad.
**Cause:** no escalation or variation in intensity across beats (`director/narrative-structure.md`'s escalation section).
**Fix:** deliberately alternate quieter/held beats with punchier ones; audit the whole sequence's intensity curve, not just each beat in isolation.
