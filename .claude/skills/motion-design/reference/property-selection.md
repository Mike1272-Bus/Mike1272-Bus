# Property Selection — what to animate, and why

Two separate questions live here: which property best *communicates* the intended change, and which properties are cheap vs. expensive to animate at runtime. Both matter; performance never justifies communicating the wrong thing, but among properties that communicate equally well, always pick the cheap one.

## Performance tier (web/app runtime contexts)

**Cheap (compositor-only, animate freely):**
- `transform` (translateX/Y/Z, scale, rotate) — does not trigger layout or paint in most modern browser engines, runs on the GPU compositor thread.
- `opacity` — same, compositor-only.
- `filter` in moderation (blur, brightness) — GPU-accelerated in most engines but heavier than transform/opacity; fine for occasional use, avoid animating heavy blur radii on many simultaneous elements.

**Expensive (triggers layout and/or paint — avoid animating every frame):**
- `top` / `left` / `right` / `bottom` (with `position: absolute/relative`) — triggers layout recalculation. Use `transform: translate()` instead for the same visual result at a fraction of the cost.
- `width` / `height` — triggers layout. If the end goal is a size change, prefer `transform: scale()` when the content doesn't need to reflow, or accept the layout cost deliberately when it does (e.g. an accordion that must actually reflow surrounding content).
- `margin` / `padding` — triggers layout, same guidance as width/height.
- `box-shadow` (animating its spread/blur directly) — triggers paint on every frame; if a shadow needs to animate, consider animating a pseudo-element's opacity instead (fade between a fixed set of pre-defined shadow states) rather than interpolating the shadow values themselves.
- `background-position` on large images — paint-heavy; fine for small elements, avoid on full-viewport backgrounds animated continuously.

**Rule of thumb:** if it's not `transform`, `opacity`, or (sparingly) `filter`, ask whether the same visual result is achievable with one of those three before reaching for a layout-triggering property, especially for anything looping or running on every frame (ambient motion, drag-follow, scroll-linked effects).

## Property selection for communication (independent of runtime)

| Communicating... | Prefer animating |
|---|---|
| Presence / absence | `opacity` |
| Position change, arrival, departure | `transform: translate` |
| Emphasis, weight, impact | `transform: scale` (with squash/stretch asymmetry per Disney #1) |
| Direction, orientation, playful energy | `transform: rotate` |
| Depth, layering | `transform: translateZ` / scale + opacity combined (things "further away" are smaller, dimmer) |
| State/identity change (this became that) | shape/color morph, or a well-timed crossfade between two fixed representations |
| Urgency, alert | color plus a fast, sharp transform — never color alone, since color-only changes are easy to miss peripherally |
| Continuous "alive" signal | slow opacity or scale pulse (`patterns/ambient-continuous.md`) |

## Color

Color transitions (background-color, color, border-color, fill) are relatively cheap to animate but easy to overuse as the *only* signal — color-blind viewers and anyone not looking directly at the element can miss a color-only change entirely. Pair meaningful color changes with a shape/transform/icon change wherever the color is communicating something the viewer needs to act on (errors, required fields, alerts) — color alone is acceptable for low-stakes cosmetic state (hover tint) but not for anything functionally important.

## HyperFrames / pre-rendered video context

Since this repo's video output is pre-rendered frame-by-frame rather than running live in a browser, the GPU-compositor-cost argument above matters less for the *final* video (every frame renders regardless of cost). It still matters for **render time** during iteration (a composition full of layout-triggering animated properties on many elements renders slower per frame) and it still matters for **correctness** — `transform`-based animation composes predictably with GSAP timelines and seek-to-any-frame determinism (required by this repo's rendering pipeline) in ways that some layout-triggering properties can behave inconsistently with when the timeline is scrubbed rather than played forward continuously. Default to transform/opacity here for both reasons.
