# Narrative Structure — the micro-story framework

Every piece of motion that lasts more than a single instantaneous cut, whether it's a 200ms button press or a 40-second brand video, works better when it has a **setup → build → payoff** shape rather than being one continuous undifferentiated motion. This is a fractal structure: it applies at the scale of a single micro-interaction and at the scale of an entire video's pacing.

## The three beats

**Setup** — establishes the starting state and, ideally, plants a small piece of anticipation (Disney principle #2). Brief. Its job is to make sure the viewer's eye is in the right place and knows *something* is about to happen, without giving away what.

**Build** — the motion itself moves through its main transformation. This is where most of the duration budget goes, and where the emotion-mapped parameters (`emotion-mapping.md`) do their work: speed, easing, overshoot trajectory.

**Payoff** — the settle, the moment the viewer's eye is told "this is the result, look at it." Must include a genuine hold — even 100-150ms of stillness — or the payoff never registers as a payoff, it just reads as motion that happened to stop. This is the most commonly skipped beat: designers spend all their effort on the build and let the payoff be an instant, silent stop.

## At micro-interaction scale (100-400ms total)

A button press: setup = tiny anticipatory compress (20-30ms), build = the color/scale transition (60-150ms), payoff = settle with a beat of stillness before it's interactive again. Skipping setup is usually fine at this scale (not every micro-interaction needs anticipation), but skipping the payoff hold is not — an interaction that immediately allows the next action with zero settle time feels twitchy.

## At scene scale (2-8 seconds)

A card expanding into a detail view: setup = the card getting a subtle pre-expansion cue, build = the expansion + content reveal (often choreographed, see `choreography.md`), payoff = the final layout holding still long enough to actually be read before anything else can happen. The payoff hold duration should scale with how much the viewer needs to process — a payoff with new text to read needs longer stillness than a payoff that's purely visual.

## At full-video scale (this repo's use case: 20-60s vertical video)

The same three beats operate at the level of the whole piece, and *also* recursively within each scene:
- **Setup** = the hook (first 1-3s) — plant the question or tension, minimal resolution yet.
- **Build** = the body — each beat itself often has its own mini setup/build/payoff, and the beats should escalate (see "escalation," below) rather than repeat the same energy level throughout.
- **Payoff** = the CTA or resolution — and it needs its own hold. A CTA card that flashes for 0.3s and cuts to black is a payoff with no beat to land; give it real screen time.

## Escalation across beats

A sequence of scenes that are all "build" energy with no differentiation flattens into monotony — even if each individual scene is well-crafted. Deliberately vary intensity: a quiet/held beat (payoff of the previous idea, or a breath) followed by a punchier beat (a new idea's setup+build) reads as *pacing*; uniform intensity throughout reads as *noise*, regardless of quality. This is the same principle as Bold archetype's "quiet beats make loud beats land" (`motion-personality.md`), generalized to structure.

## Cliffhangers and multi-part content

For content deliberately split across parts (e.g., "part 1 of a series"), the payoff of part 1 is intentionally incomplete — it resolves the immediate tension of part 1's own build, but deliberately leaves the larger question open. This still needs a real hold (don't cut mid-motion), it just holds on an *unresolved* state rather than a resolved one — the stillness communicates "this is the note we're ending on," even when that note is a question.

## Diagnostic use

If a piece of motion "feels flat" or "doesn't land" despite good individual tweens, check: is there an actual payoff hold, or does it just stop? Is there any setup/anticipation, or does it start cold? Is the build the only beat present, stretched to fill the whole duration? Missing payoff-hold is the single most common structural defect in otherwise well-executed motion.
