---
name: motion-design
description: "Creative direction for motion design — the judgment layer that decides WHY and HOW something should move, before any runtime writes code. Use when a motion/animation decision is being made: choosing what should animate, picking a personality/feel, mapping an emotion to a motion treatment, choreographing multiple elements together, sequencing an entrance/exit, diagnosing why an animation feels 'off' or 'static' or 'cheap', or reviewing a finished animation against a quality bar. Framework-agnostic (CSS, GSAP, Lottie, native, HyperFrames, anything) — pairs with a runtime-specific skill (e.g. hyperframes-animation) for the actual implementation API once the creative decision is made."
---

# Motion Design

This is the **director**, not the **animator**. It decides what a piece of motion is for, what personality it should carry, how it should be timed and choreographed, and how to tell if it worked — before a single line of animation code gets written. Once the decision is made, hand off to a runtime-specific skill (GSAP, CSS, Lottie, HyperFrames…) for implementation syntax.

Load this skill when the ask is fuzzy ("make it feel more alive", "this transition is boring", "how should this error state behave") rather than when the ask is already a concrete spec ("fade this in over 300ms").

## The Three Pillars

Every motion decision routes through three questions, in this order. Full depth in `director/core-philosophy.md`.

1. **Purpose** — what is this motion communicating? If you can't name it in one sentence, don't animate it yet.
2. **Physics** — does it obey a believable internal logic (weight, momentum, resistance)? Motion that ignores physics reads as cheap regardless of polish.
3. **Personality** — does it carry the brand's/product's character, or is it generic easing-curve wallpaper?

Purpose without physics feels janky. Physics without personality feels generic. Personality without purpose feels like noise. All three, together, is what separates motion design from "things fading in."

## Where to go

**Starting from zero on a scene or component?** Read `director/decision-framework.md` — it's the full pipeline: identify purpose → pick a personality → map the emotion → choose timing/easing → choreograph if multiple elements → validate. Follow it top to bottom the first few times; internalize it after that.

**Need the grounding theory?**
- `director/disney-principles.md` — the 12 classical animation principles, each translated into a UI/motion-design equivalent with a concrete before/after. This is the single most load-bearing reference in the skill; when an animation feels wrong and you can't say why, it's almost always a violated principle from this list.
- `director/motion-personality.md` — four motion archetypes (Precise, Playful, Elegant, Bold) and how to pick one and stay consistent with it across a whole product or video series.
- `director/emotion-mapping.md` — a lookup from target emotion (trust, urgency, delight, calm, confidence…) to concrete motion parameters.
- `director/narrative-structure.md` — the micro-story shape (setup → build → payoff) that even a 200ms micro-interaction should have.
- `director/choreography.md` — when more than one element moves: leaders/followers, stagger, groups-as-camera-shots.
- `director/context-adaptation.md` — platform constraints, `prefers-reduced-motion`, and performance budgets that override everything above.

**Need a recipe, not a theory?** `patterns/` has ready-to-adapt treatments:
- `patterns/entrance-exit.md` — how things should appear/disappear.
- `patterns/state-feedback.md` — success, error, loading, hover/press feedback.
- `patterns/ambient-continuous.md` — idle loops, breathing, parallax, anything that runs without user input.
- `patterns/multi-element.md` — stagger and group-choreography recipes.

**Need a number or a gut-check?** `reference/`:
- `reference/timing-easing-tables.md` — duration and easing lookup by motion category.
- `reference/property-selection.md` — which property to animate (and why some are GPU-cheap and some tank frame rate).
- `reference/quality-checklist.md` — run before calling any animation done.
- `reference/troubleshooting.md` — named "animation smells" (linear-everywhere, uniform-duration, motion-for-motion's-sake…) mapped to fixes.

## How to use this with an implementation skill

This skill never writes runtime code. The handoff is: settle purpose + personality + timing + choreography here, then carry those decisions into whichever runtime skill applies (e.g., `hyperframes-animation` for a HyperFrames/GSAP composition) to actually author the tween. If no project-specific runtime skill is loaded, the reference tables here (timing, easing, properties) are enough to hand a developer or write plain CSS/GSAP directly.

## Fast path (already know the drill)

Purpose in one sentence → personality archetype → emotion → timing/easing off the table → single element or choreographed group → quality checklist. Skip straight to `reference/` if you just need numbers.
