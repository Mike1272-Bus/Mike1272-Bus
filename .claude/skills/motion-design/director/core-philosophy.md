# Core Philosophy — The Three Pillars

Every piece of motion, from a 150ms button press to a 40-second brand video, should be interrogated against three pillars, in order. Skipping the order is the most common cause of motion that "looks fine but feels wrong."

## Pillar 1 — Purpose

**Motion is not decoration. It is communication with a frame rate.**

Before choosing a single easing curve, answer: *what is this movement telling the viewer that a static frame could not?* Valid answers:

- **Causality** — this happened because of that (a button press causes a card to expand)
- **Continuity** — this new thing is the same thing as that old thing, transformed (a thumbnail growing into a detail view)
- **Hierarchy** — this matters more, so it arrives first / moves more / holds longer
- **State change** — something became true (a form field became invalid, a task became complete)
- **Invitation** — this is interactive, come touch it (a subtle idle hover cue)
- **Emotion** — this moment should feel like X (delight on success, urgency on a countdown)

If the honest answer is "because motion is more impressive than a static frame," that is not a purpose — it's decoration, and decoration is where motion design goes to feel cheap. Cut it, or find the real purpose first.

**Test:** try to write the motion's job in one sentence, in the form "This animation tells the viewer that ___." If you can't finish the sentence, you don't have a design yet, you have a special effect.

## Pillar 2 — Physics

**Motion must obey an internal logic the eye already trusts, even when nothing on screen is a real physical object.**

Viewers have decades of embodied intuition about how mass, momentum, friction, and elasticity behave. Motion that respects this intuition reads as "real" and "considered" even at 100ms; motion that ignores it reads as "cheap" even with a huge production budget. Concretely:

- **Nothing starts or stops instantly.** Real mass has inertia. A linear tween that snaps from 0 to full velocity at frame 1 is the single most common tell of unconsidered motion. Ease in, ease out — always, unless you are deliberately signaling something is *not* physical (a hard glitch cut, a UI hard-wipe).
- **Heavier / larger things move slower and settle with more overshoot-damping; lighter / smaller things move faster and snap more.** A full-screen panel and a small icon badge should not share an easing curve if they're meant to feel like they belong to the same physical world.
- **Things that were connected stay connected while moving** (see Disney's "follow through and overlapping action" — full detail in `disney-principles.md`). A dragged card's shadow doesn't teleport with it; it lags very slightly and catches up.
- **Energy doesn't appear from nowhere.** If something arrives with a bounce, the bounce should be smaller than the arrival (energy dissipates), never bigger.

**Test:** if you removed all color and just watched two grey blobs move, would the motion still make physical sense?

## Pillar 3 — Personality

**Motion carries brand and emotional character the same way typography and color do — and it's the pillar most often skipped entirely, which is why most products' motion is interchangeable.**

Two products can animate the exact same button-press interaction with completely different feel: one snappy-and-precise (100ms, minimal overshoot, sharp ease-out), one warm-and-bouncy (220ms, visible elastic overshoot, softer ease). Neither is "more correct" — they encode different personalities. See `motion-personality.md` for the four-archetype framework used across this skill (Precise / Playful / Elegant / Bold).

The failure mode here isn't usually "no personality" — it's **inconsistent** personality: one screen bounces, the next screen is stiff and linear, a third overshoots wildly. That inconsistency reads as a team of people who never talked to each other, even if every individual animation is well-crafted.

**Test:** if you played five different animated moments from the same product back to back with the content hidden, would they clearly belong to the same family?

## Why the order matters

Purpose → Physics → Personality is not arbitrary. Fixing physics without a clear purpose optimizes a movement nobody needed. Adding personality before physics is solid just polishes something that already feels wrong. Always establish *why*, then make it *believable*, then make it *yours*.
