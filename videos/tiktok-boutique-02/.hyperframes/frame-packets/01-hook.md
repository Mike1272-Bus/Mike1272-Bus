# Frame packet: 01-hook

## Project inputs

- Project: /home/user/Mike1272-Bus/videos/tiktok-boutique-02
- Design tokens: /home/user/Mike1272-Bus/videos/tiktok-boutique-02/frame.md
- RULES_DIR: /root/.claude/skills/hyperframes-animation/rules

## Assigned storyboard block

## Frame 1 — Hook

- scene: A real photo of someone opening WhatsApp punches in behind the question
- duration: 4s
- transition_in: cut
- status: outline
- type: hook
- persuasion: curiosity / pattern-naming (soft copy, punchier visual)
- blueprint: kinetic-type-beats (Adapt) + motion-blur-streak entrance
- focal: whatsapp-open-photo.jpg
- roles: whatsapp-open-photo.jpg = background (dimmed ~35%, full-bleed, cover-fit centered on the phone/hand)
- asset_candidates: assets/whatsapp-open-photo.jpg — real photo, hand opening WhatsApp, hook backdrop
- src: compositions/frames/01-hook.html
- voiceover: "3 raisons pour lesquelles on ne te prend pas au serieux sur WhatsApp."

Adapt: the photo replaces the bare offwhite canvas — it enters with a motion-blur-streak push (peak blur ~18-20px full-frame per Blur Logic, resolves by 0.5s), everything else keeps the calm register.

Scene 1 (0.0-0.5s): `whatsapp-open-photo.jpg` push-enters full-bleed (scale 1.08->1.0, motion-blur-streak: 0->20px->0px), dims to ~35% opacity under a dark overlay as it settles so text reads clean on top.
Scene 2 (0.5-1.6s): a black number-pill "3 RAISONS" spring-pops in (back.out overshoot) top-third; one small particle-burst (5-6 dots) marks its landing.
Scene 3 (1.6-3.2s): the line "POUR LESQUELLES ON NE TE PREND PAS AU SERIEUX SUR WHATSAPP" fades in line by line (2 lines), soft upward drift (12px). Centered, ~55% of frame, over the dimmed photo.
Scene 4 (3.2-4.0s): held read, a faint yellow underline-tick draws under "SERIEUX" as the sole added motion.

## Selected motion rule: motion-blur-streak

---
name: motion-blur-streak
description: Fake directional velocity blur on a fast entrance or camera push-through — blur peaks at max speed and resolves to 0 at the settle, so the element streaks in then snaps sharp. Two paths — SVG feGaussianBlur on the motion axis, or an echo/ghost trail that collapses into the lead.
metadata:
  tags: motion-blur, velocity, streak, entrance, fly-in, ghost, echo, svg-filter, kinetic, camera, snap
---

# Motion-Blur Streak

Real motion blur isn't available to a seeked renderer (it integrates over shutter time), so this rule **fakes** it for a fast fly-in or hard camera push-through. The whole point is the _coupling_: the blur envelope rides the **same ease and window** as the position tween, so peak blur lands exactly on peak speed and the element is razor-sharp the instant it stops. Two paths:

- **(A) Directional SVG blur** — inline `<feGaussianBlur stdDeviation="X 0">` (X on the motion axis, 0 across it), tweened via a proxy. Cleanest; a true directional smear.
- **(B) Echo / ghost trail** — 2–4 duplicates at decreasing opacity, offset backward along the motion vector, collapsing into the lead as it settles. No filter cost; a stylized "speed-line" trail.

**Entrances and mid-shot moves only — never a mid-composition exit.** A blurred element fleeing off-frame mid-composition reads as a glitch; a hard exit between scenes is the transition's job (`../../transitions/overview.md`). One sanctioned scope extension: the envelope may ride the **camera wrapper** during a travel leg — see the Camera-Travel Carve-Out.

## How It Works

A fast `out`-eased move front-loads velocity — fastest off the start, bleeding to zero at the settle. Map the blur/echo envelope onto that same curve: position travels from an off-frame / pushed-back start to rest over `MOVE_DUR`; in lockstep on the same window and ease the smear goes `PEAK_BLUR → 0` (A) or the ghosts collapse onto the lead (B). By the settle the element is fully crisp and dwells ≥1 s — the contrast between violent streak and still, sharp settle IS the effect. GSAP can't tween an SVG attribute directly: tween a plain `{ v }` proxy and write `setAttribute("stdDeviation", …)` in `onUpdate`, seeding it once at setup so a seek to t=0 shows the streaked start.

## Recipe

```html
<!-- inside a standard scene clip; overflow: hidden on the scene (the smear extends past rest) -->
<svg width="0" height="0" aria-hidden="true" style="position: absolute">
  <filter id="streak" x="-50%" y="-50%" width="200%" height="200%">
    <feGaussianBlur id="streak-blur" in="SourceGraphic" stdDeviation="0 0" />
  </filter>
</svg>
<div class="streak-el" id="streak-el" style="filter: url(#streak)">{phrase}</div>
<!-- Path B instead: N-1 aria-hidden .streak-ghost duplicates BEHIND the lead, no filter -->
```

```js
// Path A — proxy-tweened directional blur.
const blurNode = document.getElementById("streak-blur");
const blurProxy = { v: PEAK_BLUR };
const writeBlur = () => blurNode.setAttribute("stdDeviation", `${blurProxy.v} 0`); // X axis only
writeBlur(); // seed frame 0 — a seek to t=0 must show the streaked start, not a sharp pre-frame

tl.fromTo(
  "#streak-el",
  { x: ENTER_FROM_X, opacity: 0 },
  { x: 0, opacity: 1, duration: MOVE_DUR, ease: MOVE_EASE },
  MOVE_START,
);
tl.to(blurProxy, { v: 0, duration: MOVE_DUR, ease: MOVE_EASE, onUpdate: writeBlur }, MOVE_START);

// Path B — ghosts on the SAME window/ease; per-ghost variation by index.
gsap.utils.toArray(".streak-ghost").forEach((g) => {
  const i = Number(g.dataset.i); // 1..N-1, set in HTML
  tl.fromTo(
    g,
    { x: ENTER_FROM_X - i * ECHO_STEP_PX, opacity: GHOST_BASE_OPACITY / i },
    { x: 0, opacity: 0, duration: MOVE_DUR, ease: MOVE_EASE },
    MOVE_START,
  );
});
```

## Variations

- **Vertical streak** — swap axes: `y`, `stdDeviation="0 Y"`, vertical echo offsets.
- **Camera push-through** — `scale: SCALE_FROM → 1` with a symmetric `"B B"` envelope (depth-wise smear, not directional): the wordmark punches out of soft focus and snaps crisp at the lock.
- **Staggered grid streak-in** — each card streaks into its slot at `MOVE_START + i * CARD_STAGGER` with its own blur proxy / ghosts; sharp the instant it lands.
- **Hold-the-streak** — blur on a marginally slower curve than position (position `expo.out`, blur `power3.out`) so the last wisp resolves just after arrival. Sparingly; default is locked envelopes.

## Camera-Travel Carve-Out

The envelope is also sanctioned at **wrapper level**: on the `.world` / camera wrapper of a virtual-camera scene ([viewport-change.md](viewport-change.md), [multi-phase-camera.md](multi-phase-camera.md), [3d-camera-flight.md](3d-camera-flight.md)) during a **travel leg** — a dive, a whip sweep, a violent final push. This does **not** violate "never a mid-composition exit": the world never leaves frame — the camera travels _through_ it, and every leg ends with the world at rest, sharp, inside the frame. Each leg is an **arrival** at the next pose, so the entrance doctrine applies leg by leg. Three deltas from the element-level recipe:

- **Envelope follows the leg's ease.** An `out` leg (dive, final push) uses the base recipe unchanged. An `inOut` repositioning leg peaks mid-leg: split the envelope at the velocity peak — `0 → PEAK` on the in-half ease over the first half, `PEAK → 0` on the out-half over the second. Seed the proxy at **0** for these (the streaked state lives mid-leg, not at t=0; seed-at-`PEAK_BLUR` belongs to the entrance shape, where the first frame IS the fastest).
- **Filter placement.** 2D camera: `filter: url(#streak)` on the `.world` wrapper. 3D flight: on the **perspective stage** above the 3D context — a `filter` on a `preserve-3d` element flattens it and collapses every `translateZ`. Never per-element inside the world: one frame-wide envelope, not N desynced ones.
- **Full-frame blur is heavy** — cap `PEAK_BLUR` ~18–20 at wrapper level (vs 30 for one element); a brief whip may touch ~24. Axis rule as usual: `"X 0"` for a lateral whip/pan, `"B B"` for a dive/push.

### Whip sweep (named composition)

The heavily-blurred lateral whip that resolves into the next region — two rules on one window:

1. **Position** — [nudge-curve.md](nudge-curve.md)'s three-phase chain on the camera state, tuned burst-dominant (tail still ≥3× ramp-in in time).
2. **Blur** — `0 → PEAK` across the ramp-in, held at `PEAK` through the linear burst (constant velocity = constant smear), `PEAK → 0` across the tail.

Swap or reveal the next region's content DURING the burst — the smear masks the change; the `power4.out` tail lands it sharp. Reveal during the burst, read after the tail.

```js
tl.to(cam, { x: WHIP_X * 0.1, duration: 0.12, ease: "power3.in", onUpdate: applyCamera }, WHIP_AT);
tl.to(
  cam,
  { x: WHIP_X * 0.75, duration: 0.1, ease: "none", onUpdate: applyCamera },
  WHIP_AT + 0.12,
);
tl.to(
  cam,
  { x: WHIP_X, duration: 0.35, ease: "power4.out", onUpdate: applyCamera },
  WHIP_AT + 0.22,
);

tl.to(blurProxy, { v: PEAK_BLUR, duration: 0.12, ease: "power3.in", onUpdate: writeBlur }, WHIP_AT);
// blur holds at PEAK through the linear burst (no tween needed — value rests at PEAK)
tl.to(blurProxy, { v: 0, duration: 0.35, ease: "power4.out", onUpdate: writeBlur }, WHIP_AT + 0.22);
```

## Values

| token              | range                                              | notes                                                                                           |
| ------------------ | -------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| MOVE_EASE          | `expo.out` / `power4.out` (default) / `power3.out` | `out`-family ONLY — `in`/`inOut` puts peak speed in the wrong place; position and blur share it |
| MOVE_DUR           | 0.25–0.6s                                          | over ~0.7s reads as a focus pull, not velocity                                                  |
| ENTER_FROM_X/Y     | 40–120% of the element's own dimension             | enough runway for the streak to read                                                            |
| PEAK_BLUR          | 8–30 (default 18)                                  | >30 erases the glyph at the start; ~18–20 cap at wrapper level                                  |
| SCALE_FROM         | 1.3–2.5                                            | push-through variation                                                                          |
| N (ghosts)         | 2–4                                                | >4 reads as strobe, not streak                                                                  |
| ECHO_STEP_PX       | 12–40px                                            | `N × step ≲ ENTER_FROM` so the furthest ghost starts inside the runway                          |
| GHOST_BASE_OPACITY | 0.3–0.6                                            | opaque ghosts read as duplicate elements                                                        |
| CARD_STAGGER       | 0.05–0.12s                                         | one assembling wave, not separate arrivals                                                      |

## Critical Constraints

- Blur peaks at peak speed and resolves to 0 at the settle — share the ease and window between position and envelope. A blur that lingers after the stop reads as a focus pull.
- Entrances / mid-shot arrivals only — never a mid-composition exit; wrapper-level use only per the carve-out.
- Seed `stdDeviation` at setup: at `PEAK_BLUR` for the entrance shape, at 0 for a whip / `inOut` leg.
- Generous filter region (`x="-50%" y="-50%" width="200%" height="200%"`) or the smear clips at the element's box edge.
- Directional axis: `"X 0"` horizontal, `"0 Y"` vertical, `"B B"` only for a depth/scale move — symmetric blur on a sideways move looks like defocus.
- Dwell ≥1 s sharp after the snap; a streak landing at the last beat reads as "flashed and gone".
- Heavy element on a solid field — thin type (< ~120px / 800 weight) or a busy backdrop swallows the smear.
- `overflow: hidden` on the scene — the smear / furthest ghost extends past the resting position during travel.

## See also

`kinetic-beat-slam` (streak as one beat's entrance) · `center-outward-expansion` (grid streak-in) · `scale-swap-transition` (same-footprint morph — not an arrival) · `nudge-curve` (the whip sweep's position half) · `3d-camera-flight` / `viewport-change` (the carve-out's wrappers).

## Selected motion rule: particle-burst

---
name: particle-burst
description: Deterministic particle / confetti events — a confetti pop that bursts up and drifts down (optionally instant-shrinking away), a dot burst from behind text, or a glyph dissolving to particles. Every particle's state is a pure ballistic function of timeline time from index-seeded values, so a scrub to any t shows the correct mid-flight frame.
metadata:
  tags: particles, confetti, burst, dissolve, celebration, ballistic, deterministic, punctuation
---

# Particle Burst

Discrete flying particles as a one-shot event: a **confetti pop** that erupts upward and drifts back down on gravity, a **dot burst** radiating from behind a landing word, or a **glyph dissolve** where text breaks into particles that scatter and die. Particles are ephemeral garnish — born from a beat, fly, gone; they never become layout.

Boundaries: [css-marker-patterns.md](css-marker-patterns.md)'s burst mode is radiating **drawn lines** — a static accent, no flight. [press-release-spring.md](press-release-spring.md)'s release burst is **one blurred radial layer** faking an explosion — enough when a single glow pop will do. [center-outward-expansion.md](center-outward-expansion.md) moves **real layout elements** to final resting slots; particles have no destination, only physics and a death.

## How It Works

The whole event is **one driver tween and one formula**:

1. **Seeded setup** — a fixed pool of `PARTICLE_COUNT` small divs is created once at composition setup (a deterministic loop — setup-time generation is fine; per-frame DOM creation is not). Each particle `i` derives everything from a pure hash:

   ```js
   // angle, speed, size, spin, color (palette[i % palette.length]) — all from prand(i * k)
   const prand = (n) => {
     const x = Math.sin(n * 127.1 + 311.7) * 43758.5453;
     return x - Math.floor(x); // 0..1, pure function of n
   };
   ```

2. **Ballistic formula** — a proxy tween advances `T: 0 → 1` over `FLIGHT_DUR` with `ease: "none"`; `onUpdate` positions every particle as a **pure function of T**:

   ```
   x(T) = vx · T·FLIGHT_DUR
   y(T) = vy · T·FLIGHT_DUR + ½ · G · (T·FLIGHT_DUR)²
   rot(T) = spin · T·FLIGHT_DUR
   ```

   Gravity `G` supplies the rise-decelerate-fall arc for free. Because position is computed from `T` (never accumulated per frame), a seek to any moment renders the exact mid-flight state — this is what makes DOM particles seek-safe. The driver's `ease: "none"` is load-bearing: the physics lives in the formula; an eased driver warps gravity and the arc stops reading as thrown objects.

3. **Death** — an opacity tail inside the same formula (fade over the last `FADE_FRAC` of flight), or the confetti signature: a separate **instant-shrink** tween scaling the pool to 0 in a blink at flight end. Either way the particles end invisible and stay invisible.

## Recipe

```html
<!-- inside a standard scene clip (hyperframes-core) -->
<div class="burst-stage">
  <div class="particle-field" id="particle-field"></div>
  <div class="burst-hero" id="burst-hero">{heroWord}</div>
</div>
```

```css
/* .burst-stage: position: relative; display: grid; place-items: center.
   .burst-hero: z-index: 2 — particles fly BEHIND the word. */
.particle-field {
  position: absolute;
  z-index: 1;
  left: 50%;
  top: 50%; /* the launch origin — offset to taste (e.g. the word's baseline) */
  width: 0;
  height: 0;
}
.particle {
  position: absolute;
  left: 0;
  top: 0;
  border-radius: 2px; /* confetti chip; 50% for dots */
  opacity: 0; /* invisible until the event fires */
  will-change: transform, opacity;
}
```

```js
// Setup: deterministic pool, generated ONCE.
const field = document.getElementById("particle-field");
const palette = ["{accentA}", "{accentB}", "{accentC}"]; // 3-5 brand tokens
const parts = [];
for (let i = 0; i < PARTICLE_COUNT; i++) {
  const el = document.createElement("div");
  el.className = "particle";
  const size = SIZE_MIN + prand(i * 3 + 1) * (SIZE_MAX - SIZE_MIN);
  el.style.width = `${size}px`;
  el.style.height = `${size * 0.7}px`; // slightly oblong = confetti chip
  el.style.background = palette[i % palette.length];
  field.appendChild(el);
  // Index-seeded launch parameters — the particle's whole life, fixed here.
  const angle = -Math.PI / 2 + (prand(i * 5 + 2) * 2 - 1) * CONE; // upward cone
  const speed = SPEED_MIN + prand(i * 7 + 3) * (SPEED_MAX - SPEED_MIN);
  parts.push({
    el,
    vx: Math.cos(angle) * speed,
    vy: Math.sin(angle) * speed, // negative = up
    spin: (prand(i * 11 + 4) * 2 - 1) * SPIN_MAX,
  });
}

// Confetti pop — one driver, pure ballistic formula.
const drive = { T: 0 };
tl.fromTo(
  drive,
  { T: 0 },
  {
    T: 1,
    duration: FLIGHT_DUR,
    ease: "none", // physics lives in the formula, not the ease
    onUpdate: () => {
      const t = drive.T * FLIGHT_DUR; // seconds of flight — pure function of T
      const fade = Math.min(1, (1 - drive.T) / FADE_FRAC); // opacity tail
      parts.forEach((p) => {
        const x = p.vx * t;
        const y = p.vy * t + 0.5 * G * t * t; // rise, stall, drift down
        p.el.style.transform = `translate(${x}px, ${y}px) rotate(${p.spin * t}deg)`;
        p.el.style.opacity = String(drive.T === 0 ? 0 : fade); // T===0 guard covers seeks before the event
      });
    },
  },
  BURST_AT,
);
```

## Variations

- **Confetti pop, then instant-shrink** — the playful signature: full burst, gravity drift, then every chip scales to 0 in a blink: `FADE_FRAC` near 0, plus `tl.to(".particle", { scale: 0, duration: SHRINK_DUR, ease: "power2.in" }, BURST_AT + FLIGHT_DUR - SHRINK_DUR)` with `SHRINK_DUR` 0.15–0.25s. Keep the whole event tiny relative to the subject — a garnish measured in a few dozen pixels, not a screen-filling cannon.
- **Dot burst behind a landing word** — radial instead of a cone: `angle = prand(i) * Math.PI * 2`, `G` near 0, short flight (0.4–0.7s), round dots (`border-radius: 50%`), pool z-indexed behind the word. Fire at the word's settle frame.
- **Glyph dissolve** — seed each particle's **origin** across the glyph block's box (`ox = (prand(i*13) - 0.5) * BLOCK_W`, same for `oy`, added inside the transform), gentle outward drift with low `G`; text fades out over the first ~30% of flight while particles fade in from its silhouette. Color every particle `{textColor}` so the swarm reads as the text's own material. (True per-pixel dissolves are Canvas-2D territory — `techniques.md`; this DOM version sells it up to ~40 particles.)
- **Two-stage burst (pop + stragglers)** — split the pool: 70% on the main driver, 30% on a second driver ~0.12s later with lower speeds; the split is index-derived (`i % 10 < 3`). Same formula, two windows.

## Values

| token                 | range                                        | notes                                                                           |
| --------------------- | -------------------------------------------- | ------------------------------------------------------------------------------- | --- | ----------------------- |
| PARTICLE_COUNT        | 10–18 pop/dots; 24–40 dissolve               | **cap ~40** — per-frame style writes; past that, seek perf and register degrade |
| G                     | 900–1600 px/s² confetti; 0–200 dots/dissolve | natural fall vs drift                                                           |
| SPEED_MIN / SPEED_MAX | 250–700 px/s                                 | per-particle via `prand`, never uniform                                         |
| CONE                  | 0.35–0.8 rad (~20–45°)                       | wider = splash, narrower = fountain                                             |
| FLIGHT_DUR            | 0.7–1.4s                                     | arc should peak ~35–45% of flight: check `                                      | vy  | / G ≈ 0.4 × FLIGHT_DUR` |
| SIZE_MIN / SIZE_MAX   | 5–14px chips; 4–8px dots                     | on a 1080p frame                                                                |
| SPIN_MAX              | 180–720 deg/s confetti; 0 dots               | tumble                                                                          |
| FADE_FRAC             | 0.2–0.35                                     | near 0 when using instant-shrink                                                |
| BURST_AT              | on a cause                                   | the word's settle, a click, a lockup completing — an uncaused burst is noise    |

## Critical Constraints

- **Position is a pure function of time, driver ease `"none"`** — `x(T)`, `y(T)`, `rot(T)` computed from the driver value every frame, never accumulated (`+=`) per tick (accumulation breaks the moment the renderer seeks); gravity is the ease — an eased driver bends the parabola.
- **Fixed pool, no per-frame DOM** — all particles exist after setup with `opacity: 0`; the event only writes `transform` / `opacity`. **`PARTICLE_COUNT ≤ ~40`** — per-frame style writes scale linearly; keep the event cheap.
- **Particles start AND end at `opacity: 0`** — the `drive.T === 0` guard covers seeks to before the event; the tail/shrink covers after. A chip frozen mid-air at driver end is a bug every subsequent frame.
- **Particles are punctuation** — one event per beat, fired on a cause, small relative to the subject, dead before the next beat; z-ordered behind or around the word it celebrates, never over it. A persistent particle system is a background, and that's not this rule.

## See also

`spring-pop-entrance` (confetti fires on the hero's settle frame) · `kinetic-beat-slam` (one beat earns the confetti payoff) · `press-release-spring` (single-layer glow alternative, or compose both) · `css-marker-patterns` (drawn-line burst when the accent should feel hand-annotated) · `scale-swap-transition` (glyph dissolve covers the exit).
