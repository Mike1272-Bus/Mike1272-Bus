---
name: blockframe-motion-fx
description: Use this skill when building or enriching motion-design beats (no real footage available) in a Michaelson Digital Academy / DigitalMikaelson HyperFrames episode. It adapts a curated set of Magic UI visual effects (sparkle text, shiny sweep, shimmer border, ripple click, ambient particles, marquee, staggered text reveal) into deterministic GSAP/CSS recipes that match the Blockframe palette and fit the shared root timeline. Load it whenever a beat has no real clip/image and the instruction is to prioritize moving illustration over static text.
metadata:
  short-description: Blockframe-flavored motion recipes adapted from Magic UI
---

# Blockframe motion FX (adapted from Magic UI)

A curated translation of selected Magic UI component effects into
deterministic GSAP timeline recipes for this project's HyperFrames
compositions. Source: `magicuidesign/magicui` (cloned read-only at
`/home/user/magicuidesign/magicui` for reference — do not `npx shadcn add`
anything from it, it is a React/Tailwind/shadcn registry and none of that
stack applies here).

## Why this exists, and the one rule that matters

Magic UI components animate on the **wall clock**: Framer Motion
`animate={{...}}` loops, CSS `@keyframes ... infinite`, `setInterval`,
`Math.random()`, `Date.now()`. None of that is usable as-is.

HyperFrames renders by **seeking** a single paused GSAP timeline
(`window.__timelines["main"]`) to an exact timestamp per frame — see
`CLAUDE.md`'s Key Rules and the project's standing constraint: *"Only
deterministic logic — no `Date.now()`, no `Math.random()`, no network
fetches."* A wall-clock CSS animation or a `Math.random()`-seeded sparkle
field will not reproduce the same frame on every seek, which breaks
rendering. Every effect below is re-expressed as `tl.fromTo`/`tl.to`/
`tl.set` calls with fixed values and fixed positions, added to the shared
`tl`, exactly like every other beat in these compositions.

Before using this skill, you should already know the project's baseline
patterns: `.fx-scene`, `.fx-title`, `.fx-eyebrow`, `.fx-numbadge`,
`.fx-roadmap`/`.fx-node`, the CTA `.fx-subscribe-btn` mechanism, and the
palette (`--yellow: #F7CB46`, `--ink: #0A0A05`, `--cream: #FFFDF5`,
Archivo Black for display, Work Sans for labels) — see
`videos/BLOCKFRAME-STYLE.md`. These recipes extend that system; they
don't replace it.

## When to reach for this

Only for beats where **no real clip/image exists** for the clause, and
the brief says to prefer a moving illustration over centered static text
(this has been an explicit, recurring instruction across episodes 3-4).
Don't reach for a flashy effect just because it exists — one core motion
idea per beat, same discipline Magic UI's own skill recommends ("start
with 1 core component + 1 supporting effect").

## Recipes

### 1. Sparkle burst — emphasis on a reveal moment

Good for: a "gratuit" tag, a number hitting its final value, a VENDRE
letter landing, any "this is the important word" beat.

Magic UI's `sparkles-text` spawns random stars on an interval. Deterministic
version: a fixed ring of sparkle glyphs placed by hand in the HTML,
staggered once via GSAP.

```html
<div class="fx-sparkle-wrap">
  <span id="sp1" class="fx-sparkle" style="left:-30px; top:-20px;">&#10022;</span>
  <span id="sp2" class="fx-sparkle" style="right:-24px; top:-10px;">&#10022;</span>
  <span id="sp3" class="fx-sparkle" style="left:10%; bottom:-26px;">&#10022;</span>
  <span id="sp4" class="fx-sparkle" style="right:14%; bottom:-18px;">&#10022;</span>
  <strong id="sp-word" class="fx-title">GRATUIT</strong>
</div>
```

```css
.fx-sparkle-wrap { position: relative; display: inline-block; }
.fx-sparkle { position: absolute; font-size: 34px; color: var(--yellow); opacity: 0; }
```

```js
const sparkles = ["#sp1", "#sp2", "#sp3", "#sp4"];
tl.fromTo("#sp-word", { opacity: 0, scale: 0.7 }, { opacity: 1, scale: 1, duration: 0.22, ease: "back.out(2.6)" }, t);
sparkles.forEach((sel, i) => {
  tl.fromTo(sel, { opacity: 0, scale: 0, rotation: 0 },
    { opacity: 1, scale: 1, rotation: 90, duration: 0.18, ease: "back.out(3)" }, t + 0.1 + i * 0.05);
  tl.to(sel, { opacity: 0, scale: 0.4, duration: 0.2, ease: "power1.in" }, t + 0.45 + i * 0.05);
});
```

### 2. Shiny sweep — a highlight that crosses the CTA once

Magic UI's `shiny-button` loops a diagonal gradient via CSS `--x` custom
property forever. Here: one deterministic pass, timed to land right when
the CTA pops in.

```css
.fx-sweep-mask {
  position: absolute; inset: 0; border-radius: inherit; overflow: hidden; pointer-events: none;
}
.fx-sweep-mask::before {
  content: ""; position: absolute; top: -20%; bottom: -20%; width: 60px;
  background: linear-gradient(75deg, transparent, rgba(255,255,255,0.55), transparent);
  transform: translateX(-140px); /* start position, GSAP drives x */
}
```

Add `<div class="fx-sweep-mask"><div id="sweep-bar"></div></div>` inside
`.fx-subscribe-btn` (give the inner bar its own id instead of relying on
`::before`, since GSAP can't tween pseudo-elements — copy the gradient
bar's look onto a real absolutely-positioned div):

```js
tl.fromTo("#sweep-bar", { x: -140 }, { x: 900, duration: 0.5, ease: "power1.inOut" }, t + 0.3);
```

### 3. Shimmer border — a pulsing ring on a "hot" badge

Good for the currently-highlighted VENDRE roadmap node, or a numbered
badge that should read as "look here." Magic UI's `shimmer-button` spins
a conic gradient border forever; here, a single ring that expands and
fades, repeated a fixed number of times (not `Infinity`).

```css
.fx-shimmer-ring {
  position: absolute; inset: -10px; border-radius: 50%; border: 3px solid var(--yellow);
  opacity: 0;
}
```

```js
tl.set("#node-ring", { opacity: 0.8, scale: 1 }, t);
tl.to("#node-ring", { opacity: 0, scale: 1.4, duration: 0.6, ease: "power1.out", repeat: 2 }, t);
tl.set("#node-ring", { opacity: 0 }, t + 1.9); // hard kill — see BLOCKFRAME lint rule below
```

**Reminder**: any tween that fades an element to 0 needs a `tl.set(...,
{opacity:0}, exitTime)` hard kill at the beat's exit boundary, and the
very first tween touching an element must animate *from* `opacity: 0`
(the CSS default), never *from* `opacity: 1` — see the postmortem in
`videos/PROJECT-CONTEXT.md` ("Bug GSAP à connaître"). This bit us once
already (academy-04's guide-unlock lock icon stayed visible for the
entire video because its first `fromTo` started from `opacity: 1`).

### 4. Ripple click — reuse, don't reinvent

The project's CTA already has this exact effect
(`.fx-click-ring`/`#p7-ring` pattern, permanent per
`BLOCKFRAME-STYLE.md`). Magic UI's `ripple-button` is the same idea
(expanding circle from the click point, fading out) — no new recipe
needed, just reuse the existing `.fx-click-ring` class anywhere a "tap"
needs to register (e.g. a phone-mockup beat showing someone tapping
follow/like).

### 5. Ambient particles — subtle background texture for a long static beat

Good for beats that run 5s+ with no real footage (long definition/lecture
beats can feel static). Magic UI's `particles` scatters and drifts dots
randomly forever. Deterministic version: a fixed small grid of dots,
gently drifting via a few `tl.to` calls with different offsets so they
don't look mechanically synchronized.

```css
.fx-dot { position: absolute; width: 8px; height: 8px; border-radius: 50%; background: var(--yellow); opacity: 0; }
```

```js
const dots = [
  { sel: "#d1", x: 120, y: 200 }, { sel: "#d2", x: 860, y: 340 },
  { sel: "#d3", x: 200, y: 1400 }, { sel: "#d4", x: 900, y: 1500 },
];
dots.forEach(({ sel, x, y }, i) => {
  tl.set(sel, { left: x, top: y, opacity: 0.25 }, t);
  tl.to(sel, { y: y - 40, duration: 2.4 + i * 0.3, ease: "sine.inOut", yoyo: true, repeat: 1 }, t);
});
tl.set(dots.map(d => d.sel), { opacity: 0 }, exitTime);
```

Keep it to 3-5 dots at low opacity (0.15-0.3) — it's texture, not content.
Never stack this under a beat that already has a real video/image; it's
for motion-design-only beats.

### 6. Staggered word reveal — alternative to a flat fade-in

Magic UI's `text-animate` / `blur-fade` reveal text word-by-word or
letter-by-letter. Useful for a punchy kinetic-text beat instead of the
whole line fading in at once (already used for the hook typewriter — this
is the same idea applied to a short phrase mid-video).

```html
<div class="p1-text"><span id="wrap"><span class="fx-word">ARRÊTE</span> <span class="fx-word">DE</span> <span class="fx-word">COURIR</span></span></div>
```

```js
const words = ["one selector per .fx-word span, in order"];
words.forEach((sel, i) => {
  tl.fromTo(sel, { opacity: 0, y: 16 }, { opacity: 1, y: 0, duration: 0.16, ease: "power2.out" }, t + i * 0.09);
});
```

Reserve this for a short punchline (3-5 words); on a full sentence it
reads as slow, not punchy.

### 7. Marquee — a scrolling row (platform logos, VENDRE letters preview, etc.)

Magic UI's `marquee` loops a flex row via CSS animation forever.
Deterministic version: a single GSAP `xPercent` tween across the beat's
duration, no loop needed since the beat itself is short.

```css
.fx-marquee-track { display: flex; gap: 40px; position: absolute; left: 0; white-space: nowrap; }
```

```js
tl.fromTo("#marquee-track", { xPercent: 0 }, { xPercent: -35, duration: beatDuration, ease: "none" }, t);
```

Duplicate the row's content once (`A B C A B C`) if you need it to look
continuous rather than sliding off-frame.

## Effects deliberately left out

- `globe`, `warp-background`, `retro-grid`, `animated-grid-pattern`:
  heavy WebGL/canvas or large SVG effects, overkill for a 2-4s beat and
  this render pipeline runs with `browserGpuMode: software` (confirmed in
  every `npm run check` log) — anything GPU-shader-heavy will be slow or
  render incorrectly.
- `avatar-circles`, `bento-grid`: layout components for web pages, not a
  motion pattern; not applicable to a single full-bleed video frame.

## Quick index by intent

- Emphasize a word/number/tag → **Sparkle burst**
- Make the CTA feel extra polished → **Shiny sweep**
- Draw the eye to one roadmap node/badge → **Shimmer border**
- Confirm a tap/click → reuse **`.fx-click-ring`** (already in the project)
- A long static lecture beat feels dead → **Ambient particles** (sparingly)
- A short punchline needs rhythm → **Staggered word reveal**
- Show a row of things moving (logos, letters) → **Marquee**
