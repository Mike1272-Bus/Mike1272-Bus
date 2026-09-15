# Context Adaptation — platform, accessibility, performance

Everything in `core-philosophy.md`, `motion-personality.md`, and `emotion-mapping.md` describes the *ideal* motion for a purpose. This document describes the constraints that can override that ideal — and they always win when they conflict.

## Accessibility: `prefers-reduced-motion`

Some viewers have vestibular disorders or motion sensitivity where parallax, large-scale movement, or continuous ambient motion causes real physical discomfort (dizziness, nausea), not just annoyance. This is a hard requirement, not a nice-to-have.

- **Detect and respect** the OS-level `prefers-reduced-motion: reduce` media query in any web/app context. When set:
  - Replace large-scale movement (slides, parallax, scale transforms crossing significant screen distance) with **cross-fades**. The state change still communicates (Pillar 1, purpose is preserved) without the vestibular trigger.
  - Kill purely ambient/decorative continuous motion entirely (background parallax, idle breathing loops, auto-playing carousels) — these have the lowest purpose-to-risk ratio.
  - Keep functionally necessary motion (a loading spinner communicating "still working") but ideally swap it for a lower-amplitude or opacity-pulse variant instead of a spatial one.
- **This does not apply to pre-rendered video content** (the video files this repo produces) the same way — a viewer choosing to press play on a video has different expectations than passively encountering ambient UI motion. But it fully applies to anything in a companion web app, landing page, or interactive deck this skill might also be used for.

## Platform conventions

Motion that feels natural on one platform can feel foreign on another, because viewers carry platform-specific expectations:

- **Short-form vertical video (TikTok/Reels/Shorts)** — Bold-archetype energy is the norm, fast cuts, high information density, motion needs to read clearly even when the viewer is half-attentive with sound off; captions/text motion must be legible in <1s.
- **Native mobile app UI** — platform easing conventions exist for a reason (iOS's springs, Android's Material motion) and departing from them without a strong reason makes an app feel subtly "off" even to viewers who can't articulate why.
- **Desktop web** — generally more tolerant of longer/subtler motion since attention spans and viewing distance differ from mobile; Elegant-archetype pacing that would feel slow on mobile can feel appropriately considered on desktop.
- **Print-adjacent / static export contexts** — no motion at all is the constraint; design the single best frame instead (see `disney-principles.md` #12, Appeal — the freeze-frame test matters literally here).

## Performance budget

A beautifully choreographed sequence that drops frames is worse than a simpler one that doesn't — jank itself communicates "cheap" and "broken," overriding whatever the motion was designed to say (this can invalidate all three pillars at once).

- **Animate compositor-friendly properties** — `transform` (translate/scale/rotate) and `opacity` run on the GPU compositor in most modern engines and are close to free. Animating `top`/`left`/`width`/`height`/`margin` forces layout recalculation on every frame and is the most common cause of janky "smooth in theory, choppy in practice" motion. Full detail in `reference/property-selection.md`.
- **Budget for the slowest target device**, not the development machine. A sequence with 15 simultaneously-animating elements that's smooth on a dev laptop may drop frames on a mid-range phone — reduce simultaneous animating element count, or stagger them so fewer are active at any single frame, rather than reducing quality of each individual tween.
- **Video export contexts** (this repo's HyperFrames pipeline) don't have live-performance jank risk since frames are pre-rendered deterministically — but render time itself is a budget (complex per-frame compositing multiplies render duration), and it's still worth avoiding unnecessarily expensive per-frame CSS (heavy blur/filter stacks, huge DOM counts) purely for render-pipeline efficiency.

## Resolving conflicts

When the ideal motion (from purpose/personality/emotion) conflicts with a constraint in this document, the constraint wins, but look for a version of the original intent that survives the constraint rather than just deleting the motion: reduced-motion → cross-fade instead of slide (purpose intact, vestibular risk removed); performance-constrained → fewer simultaneously-animating elements with the same stagger *shape*, not zero choreography.
