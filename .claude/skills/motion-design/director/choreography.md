# Choreography — coordinating multiple elements

A single element animating is a tween. Multiple elements animating together is choreography, and it fails or succeeds on structure, not on how good any individual tween looks.

## Establish a leader

Every multi-element sequence needs exactly one element the eye is told to follow first. Everything else is either a **follower** (moves in response to / after the leader) or **ambient** (moves independently, at low visual weight, never competing for primary attention). If nothing is designated the leader, the viewer's eye has to guess, and guessing reads as chaos even if every individual motion is well-crafted (this is Disney principle #3, Staging, applied to groups).

Practical tie-breaker for "who's the leader": whichever element the user's action was most directly about, or whichever element carries the content that matters most to the current purpose (`core-philosophy.md` Pillar 1).

## Stagger

The default tool for "multiple similar elements, one implied order." Rules of thumb:

- **Stagger delay: 40-100ms** between siblings for UI-scale lists (cards, list rows, nav items). Below ~40ms it reads as simultaneous; above ~100ms per item it starts to feel slow for anything more than ~6 items.
- **Direction should match reading/visual order** — top-to-bottom for a vertical list, left-to-right for a horizontal row, outward-from-center for a radial/grid reveal tied to a central action. A stagger direction that fights the eye's natural scan path reads as arbitrary.
- **Total sequence duration matters more than per-item duration** — for long lists (12+), cap the total stagger spread (e.g., don't stagger 30 items at 80ms each, that's 2.4s just for the stagger; compress the per-item delay or batch them) and see `patterns/multi-element.md` for concrete recipes.

## Group as a single camera move

For elements that must feel like *one thing* moving, not several things moving in coordination (e.g., a card and its shadow, an icon and its label, a multi-layer illustration), treat the group's transform as a single authored move and let members deviate only slightly via `follow through` timing offsets (Disney #5), not via independent easing curves. If two "grouped" elements use noticeably different easing functions, they will read as two things that happen to be near each other, not one object.

## Overlap vs. sequence

Two structural choices for how elements relate in time:

- **Sequential** (A finishes, then B starts) — used when B's motion is *caused by* A completing (a confirmation appearing after a submit animation lands). Creates a clear causal read but costs total time.
- **Overlapping** (B starts before A finishes, typically at 60-80% of A's duration) — used when A and B are part of the same beat and don't need a causal read between them (a card scaling in while its label fades in). Faster, feels more like one cohesive moment. This is the default for most "elements belonging to the same reveal" scenarios — pure sequential chains for unrelated elements feel sluggish.

Avoid the common mistake of overlapping elements that DO have a causal relationship (making B start before A visually "finishes causing" it) — that reads as B happening for no reason, since A hasn't visibly resolved yet.

## Competing motion

If two elements both want to be the leader in the same beat, that's a purpose problem (`core-philosophy.md` Pillar 1), not a choreography problem — go back and decide which one actually matters more right now, or split them into two beats (see `narrative-structure.md`). Choreography can sequence and stagger, but it cannot fix a scene that fundamentally doesn't know what it's about.

## Practical checklist for any multi-element scene

1. Who's the leader? (if unclear, that's the first thing to fix)
2. What's the stagger direction, and does it match how the eye already wants to scan this layout?
3. Which elements are grouped (must move as one) vs. independent?
4. Sequential or overlapping, per relationship — and does that choice match whether there's a causal link?
5. Total sequence duration — does it still feel like "one moment," or has it sprawled into a long slideshow?
