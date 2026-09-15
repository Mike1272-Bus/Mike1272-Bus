# Disney's 12 Principles, adapted for motion/UI design

The 1981 Thomas & Johnston principles, written for hand-drawn character animation, translate almost unchanged to interface and product motion. Each entry: the original principle, its UI/motion-design equivalent, and a concrete before/after.

## 1. Squash and Stretch
**Original:** deforming a shape along its motion to sell weight and flexibility.
**Translated:** scale distortion on impact/release — a button squashes slightly on press (scaleY 0.94) and overshoots slightly on release (scaleY 1.04 → 1). A card landing after a drop compresses on impact.
**Before/after:** a button that just changes color on press vs. one that also scales down 4% for 80ms — the second reads as physically pressed, the first reads as a color swap.

## 2. Anticipation
**Original:** a small counter-movement before the main action, so the eye knows something is about to happen.
**Translated:** a tiny pre-move before the real move. A card about to fly off-screen first nudges 4px in the opposite direction. A button about to expand first compresses slightly.
**Before/after:** a modal that instantly appears at full size vs. one that first scales to 96% for 60ms before expanding to 100% — the second feels intentional, the first feels like a glitch.

## 3. Staging
**Original:** present one idea per moment; don't let competing action fight for attention.
**Translated:** only animate what the viewer needs to be looking at *right now*. If five elements move simultaneously with equal weight, nothing reads. Stagger and hierarchy (see `choreography.md`) exist to enforce this.
**Before/after:** a dashboard where every widget animates in at once vs. one where the primary metric arrives first, secondary widgets follow 80ms later, staggered.

## 4. Straight Ahead vs. Pose to Pose
**Original:** two animation workflows — draw frame by frame forward (organic, unpredictable) vs. key poses first then fill between (controlled, precise).
**Translated:** procedural/physics-driven motion (spring simulations, drag-follow, particle systems) vs. keyframed/timeline motion (GSAP tweens, CSS transitions with fixed easing). Pick based on whether the motion needs to *respond* to continuous input (straight-ahead/physics: dragging, momentum scroll) or *deliver* a fixed, repeatable beat (pose-to-pose/keyframed: an entrance animation, a brand sting).

## 5. Follow Through and Overlapping Action
**Original:** parts of a body don't stop at the same instant — trailing elements (hair, cloth, a tail) continue past the main stop and settle after.
**Translated:** when a parent element moves or stops, its children/decorations shouldn't move in perfect lockstep. A dragged card's drop shadow lags a few px and eases in slightly after the card itself stops. A dismissed toast's icon can finish its own micro-animation a beat after the toast body has started fading.
**Before/after:** a card and its shadow moving as one rigid unit vs. the shadow trailing by ~40ms and settling after — the second has weight, the first looks like a flat sticker.

## 6. Slow In, Slow Out
**Original:** most frames cluster near the start and end poses; few frames in the fast middle. i.e., easing.
**Translated:** never use linear easing for anything meant to feel natural (reserve linear for mechanical/robotic/deliberately-artificial motion, like a progress bar or a hard-wipe transition). Entrances: ease-out (fast start, slow settle). Exits: ease-in (slow start, fast departure). See `reference/timing-easing-tables.md` for curve values.

## 7. Arcs
**Original:** natural motion travels in curves, not straight lines, because organic movement pivots around joints.
**Translated:** anything meant to feel alive (a character, a mascot, a celebratory element) should move along a curved path, not a straight tween of `x`/`y`. Straight-line motion is fine and often *correct* for mechanical/UI elements (a panel sliding in, a menu opening) — arcs are for things that should feel like they have agency, not for things that should feel like machinery.

## 8. Secondary Action
**Original:** a smaller supporting action that reinforces the main action without competing with it (a character scratching their head while thinking).
**Translated:** a subtle supporting detail on the primary motion — a confetti burst accompanying (not replacing) a "success" state's main checkmark animation; a subtle icon wiggle alongside a primary button's color change. Must be strictly smaller/quieter than the main action or it becomes competing staging (principle 3), not support.

## 9. Timing
**Original:** the number of frames (i.e. duration) an action takes determines its weight and mood — same action, different duration, completely different feel.
**Translated:** duration is a communication choice, not an afterthought. The exact same scale-pop animation at 100ms reads as "snappy/efficient"; at 400ms it reads as "deliberate/weighty." Pick duration from the emotion you're targeting (`emotion-mapping.md`), not from what "felt okay" in isolation.

## 10. Exaggeration
**Original:** push a motion slightly beyond strict realism to make it read clearly and feel more alive.
**Translated:** a *slight* overshoot past the final resting state, then settle, reads as more alive than landing exactly on target. This is why `back.out` / spring-with-overshoot easings feel better than a plain ease-out for anything with a Playful or Bold personality — but exaggeration has a ceiling; past a point it reads as cartoonish or buggy instead of alive. Calibrate against the personality archetype (Precise/Elegant want near-zero overshoot; Playful/Bold can carry more).

## 11. Solid Drawing
**Original:** maintain volume and consistent perspective through a deformation, don't let a shape twist and lose spatial coherence.
**Translated:** transforms should stay visually coherent — a card rotating in 3D should keep consistent perspective/anchor point through the whole rotation, not pop between projection modes. Avoid animating properties whose interpolation looks wrong at intermediate frames (e.g. animating `border-radius` between very different shapes can look broken mid-transition; test the middle frame, not just start/end).

## 12. Appeal
**Original:** even a "plain" character design should be pleasant and clear to look at — appeal isn't about being cute, it's about being well-composed.
**Translated:** an animation should be pleasant to watch even paused mid-frame. If freezing the animation at 40%, 60%, 80% produces awkward, ugly, or confusing intermediate compositions, the motion needs redesigning even if the start and end states are both fine.

## How to use this list

When an animation "feels off" and you can't articulate why, walk this list top to bottom against the specific motion. It's almost always one of: missing anticipation (#2), no follow-through (#5), linear easing (#6), wrong timing for the intended weight (#9), or a duration mismatched to personality's exaggeration tolerance (#10). See `reference/troubleshooting.md` for this same diagnosis organized by symptom instead of by principle.
