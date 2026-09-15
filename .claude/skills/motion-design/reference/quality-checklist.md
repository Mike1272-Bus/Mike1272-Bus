# Quality Checklist

Run before calling any animation done. Organized by the three pillars, plus a structure and a technical pass.

## Purpose
- [ ] Can you state what this motion communicates in one sentence?
- [ ] If this animation were removed entirely (instant cut), would something meaningful be lost? (If not, it's decoration — cut it or find its real purpose.)
- [ ] Does the motion's intensity match how much the moment actually matters? (A routine action shouldn't get hero-moment treatment, and vice versa.)

## Physics
- [ ] Does anything start or stop instantly with no easing? (Should be near-zero exceptions, and only for deliberately mechanical/artificial moments.)
- [ ] Do connected/grouped elements move as one coherent object, with any follow-through reading as *lag*, not as *disconnection*?
- [ ] If there's overshoot, does it look like energy dissipating (settling down from the overshoot), not energy appearing from nowhere (overshoot bigger than the arrival)?
- [ ] Freeze the animation at 25%, 50%, 75% — does every intermediate frame look coherent, or does something visually break/twist mid-transition?

## Personality
- [ ] Does this motion's easing/overshoot/duration texture match the project's established archetype (Precise/Playful/Elegant/Bold)?
- [ ] If you played this next to another animation from the same project with content hidden, would they clearly belong to the same family?
- [ ] Is the personality consistent, or did this component just get "whatever felt good in isolation"?

## Structure
- [ ] Is there an actual payoff — a real hold at the end — or does the motion just stop?
- [ ] For multi-element sequences: is there a clear leader, and does everything else relate to it clearly (follower, ambient, grouped)?
- [ ] For a sequence of beats/scenes: does intensity vary (some quiet, some loud), or is everything the same energy level throughout?

## Technical
- [ ] Are the animated properties compositor-cheap (`transform`, `opacity`) wherever possible, or is there a specific reason to pay for a layout-triggering property?
- [ ] Does this respect `prefers-reduced-motion` where applicable (web/app contexts)?
- [ ] Does it hold up on the slowest target device/render path, not just the fastest?
- [ ] For looping content: is the loop point genuinely seamless across 3+ consecutive cycles?

## The freeze-frame test (Disney #12, Appeal)
Pause the animation at several random points. Each frame should look like a plausible, well-composed still image on its own. If any frozen frame looks awkward, unbalanced, or confusing, the motion needs redesigning even if start and end states are both fine — viewers on slower devices, screen recordings, or simply glancing mid-animation will see exactly these "bad" frames.

## The five-second gut check
Show the finished motion to someone (or watch it yourself) without any other context. Ask: what just happened, and how did that feel? If the honest answer to "what happened" doesn't match the intended purpose, or the honest answer to "how did that feel" doesn't match the intended emotion, go back to `director/decision-framework.md` step 1 before touching any easing curve.

## When it still feels wrong after all of the above passes
See `reference/troubleshooting.md` — it catalogs specific named "smells" (linear-everywhere, uniform-duration, motion-for-motion's-sake, competing-leaders) that this checklist can miss because each individual item passes while the combination still feels off.
