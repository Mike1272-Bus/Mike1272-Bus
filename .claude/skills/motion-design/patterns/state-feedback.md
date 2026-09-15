# State Feedback Patterns — success, error, loading, hover/press

Motion whose entire purpose (Pillar 1) is communicating a state change. These are high-frequency, high-purpose-clarity moments — get them right and the whole product feels responsive; get them generic and the product feels dead even if the "hero" animations are great.

## Success
**Shape:** setup (brief) → build (the confirming action, e.g. checkmark draw-on) → payoff (a real hold, often with secondary delight motion). Map to `emotion-mapping.md`'s delight/celebration row for anything user-meaningful (completed a purchase, finished onboarding); map to the calmer confidence row for routine/frequent success states (a form field validated, an autosave confirmed) — not every success deserves confetti, and treating routine success like a big win makes the big wins feel smaller.
**Recipe:** icon draws on or scale-pops in (200-350ms, moderate overshoot for meaningful success / none for routine success) → optional secondary motion (particles, a color wash) strictly smaller than the primary icon's motion → hold 400ms+ before allowing dismissal or next action.
**Watch out:** never use bounce/elastic on success states the user will see dozens of times a day (e.g. "message sent") — it reads as try-hard after the third time. Save elasticity for genuinely infrequent wins.

## Error
**Shape:** should feel apologetic/clear, never mocking. Map to `emotion-mapping.md`'s sadness/error row: no bounce, no bright flash, a small "sink" or a restrained horizontal shake is the ceiling of intensity.
**Recipe:** a brief shake (2-3 cycles, small amplitude — 4-8px, ~300ms total) for "this input is wrong, try again," OR a soft color-shift + icon swap with no spatial motion at all for less urgent errors (a background sync failure vs. an invalid form field). Match intensity to how blocking the error is for the user.
**Watch out:** shake is overused for every error regardless of severity — reserve it for actionable, in-the-moment input errors; for passive/background errors (notification-style), a calm fade-in of an error state reads better than shaking something the user wasn't actively interacting with.

## Loading
**Shape:** this is the one category where motion runs for an *unknown* duration, which changes the design problem — it needs to read as "still working, not stuck" without becoming visual noise over a potentially long wait.
**Recipe:** for genuinely short waits (<1s), consider no loading state at all — a spinner that flashes for 200ms and disappears is worse than nothing (it's Disney principle #12, Appeal, failing at every freeze-frame). For longer waits, prefer a **determinate** progress indication whenever the actual progress is knowable (real percentage), reserving indeterminate spinners/pulses for genuinely unknown-duration waits. Indeterminate motion should be smooth, continuous, low-amplitude, and genuinely loopable with no visible seam (see `ambient-continuous.md`).
**Watch out:** a loading animation with high-energy Bold-archetype intensity becomes exhausting over more than a couple seconds — loading states should generally sit calmer than the archetype's baseline, regardless of what archetype the rest of the product uses, simply because the viewer is staring at it involuntarily for an unknown length of time.

## Hover / press (micro-feedback)
**Shape:** the highest-frequency motion in most interactive products — a user may trigger a given hover/press state hundreds of times in a session. Must be fast and must never fatigue.
**Recipe:** hover: 100-150ms, subtle (scale 1.0→1.02-1.03, or a color/elevation shift, rarely both at full intensity simultaneously). Press: even faster (80-120ms), a compress (Disney #1, squash) reading as "received the input." Release: quick settle, no overshoot for Precise/Elegant, small overshoot acceptable for Playful/Bold but must stay tiny given the repetition frequency.
**Watch out:** this is the category most sensitive to Disney principle #9 (Timing = weight/mood) — even 50ms of extra duration across a hover state that fires constantly changes the product's felt responsiveness disproportionately to how small the number looks on paper. When in doubt, err faster here specifically.

## General rule across all four

State-feedback motion is functional first, expressive second — the personality archetype (`motion-personality.md`) should still be recognizable, but never at the cost of the state being immediately, unambiguously clear. If a viewer has to watch the full animation to understand whether something succeeded or failed, the state communication has failed regardless of how polished the motion is.
