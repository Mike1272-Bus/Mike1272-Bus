# Decision Framework — the full pipeline

Run new motion decisions through these six steps, in order. Each step's output feeds the next. For a component you're iterating on repeatedly, steps 1-3 usually stay fixed and you're only re-running 4-6.

## 1. Name the purpose

One sentence: "This animation tells the viewer that ___." See `core-philosophy.md` Pillar 1 for the valid categories (causality, continuity, hierarchy, state change, invitation, emotion). Write it down even if it feels obvious — half the time, writing it down reveals there isn't one yet.

No purpose → stop. Either find the real purpose or don't animate this element.

## 2. Pick (or confirm) the personality archetype

Every project should have ONE dominant archetype, decided once, applied everywhere: **Precise / Playful / Elegant / Bold** (full definitions in `motion-personality.md`). If this is a new element in an existing project, don't pick — inherit whatever the project already uses. If this is the first motion decision in a new project, pick deliberately based on the brand, not by default.

## 3. Map the emotion to motion parameters

Given the purpose (step 1) and the archetype (step 2), what should the viewer *feel* at this moment? Look it up in `emotion-mapping.md` for a starting set of parameters (speed, easing family, overshoot amount, secondary motion). The archetype colors how that emotion is expressed; the emotion decides which direction to push within the archetype.

## 4. Choose timing and easing

Pull concrete numbers from `reference/timing-easing-tables.md`, adjusted by:
- **Size/mass** — bigger or more visually "heavy" elements get slightly longer duration and softer easing (Pillar 2, physics).
- **Distance traveled** — further = longer, but not linearly; use the duration bands in the table, don't compute a literal px/ms constant.
- **Frequency** — anything the user triggers repeatedly (hover, tab switch) must be fast (100-200ms) or it becomes an obstacle, regardless of how nice it looks the first time.

## 5. Choreograph if more than one element is involved

Single element → skip to step 6. Multiple elements moving together (a list appearing, a dashboard loading, a multi-layer scene transition) → read `director/choreography.md` and `patterns/multi-element.md`. Decide: is there a leader and followers? A stagger direction that matches reading order or visual hierarchy? Does anything need to look like a single "camera move" rather than N independent tweens?

## 6. Validate against the quality checklist

Before calling it done, run `reference/quality-checklist.md`. If it fails on "feels janky" or "feels generic," the fix is almost always back in step 1 (purpose too vague) or step 2 (personality not actually applied — just default easing with the archetype's name attached). If it fails on performance, see `reference/property-selection.md`.

## Fast-path shortcut

Once an archetype and its emotion-to-parameter mappings are established for a project, steps 2-3 collapse into "look up the existing pattern." Most day-to-day motion work is really just steps 1, 4 (grab numbers from the table), and 6 (sanity check). The full six-step pipeline matters most at the *start* of a project (establishing the system) and when something feels off and you need to diagnose which pillar broke.

## Common shortcuts that cause problems later

- **Skipping step 1 and going straight to "what does GSAP's `back.out` look like"** — produces technically smooth motion with no reason to exist, which reads as noise once there's more than one of it on screen.
- **Skipping step 2 per-component** — every component picks its own easing "because it looked good," and the product ends up with a dozen incompatible motion languages.
- **Skipping step 5 on a scene with 4+ elements** — each element individually looks fine in isolation, but together they read as chaotic because nothing establishes an order of attention.
