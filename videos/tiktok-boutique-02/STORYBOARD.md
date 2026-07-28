---
format: 1080x1920
duration: 30s
message: "Un statut WhatsApp s'oublie vite. Un vrai site reste - et fait plus serieux."
arc: Hook -> Raison 1 -> Raison 2 -> Raison 3 -> Pivot/Preuve -> CTA doux
audience: petits commercants qui vendent via WhatsApp ou un site peu professionnel
mode: autonomous
music: none
---

## Video direction

- **Palette system** (from `frame.md`, BlockFrame): offwhite (`#FFFDF5`) resting canvas throughout. One pastel accent per frame: blue for the WhatsApp-photo frames, pink for the transition/contrast beat, green for the real-site reveal (credibility signal), yellow bookend on hook + CTA.
- **Motion grammar + reveal model**: long-tail `power3`/`expo` eases. This cut (v2) upgrades to a punchier, more "viral short-form" motion register than the first pass: real photos enter on a **motion-blur-streak** push (peak blur at speed, resolves to 0 on settle), accent chips/labels land with **spring-pop-entrance** (`back.out` overshoot), and one **particle-burst** accent per frame marks its key beat. Between-frame cuts use the registry's punchier options (`zoom-through`, `blur-crossfade`, `push-slide`) instead of plain crossfades — see each frame's `transition_in`. Beat-paced reveal still applies: nothing appears before its line is "spoken."
- **Rhythm / held-frame allocation**: Frame 5 (pivot/reveal with the real site proof) stays the calmest, most-held beat — the real screenshots need to breathe even as the rest of the video is punchier. Frame 1 (hook) and Frame 6 (CTA) carry the most energy.
- **Negative list**: no invented UI mockups anymore in Frames 2-4 (replaced by real photos/screenshots below) — never crop a real photo so hard it loses its subject; no more than 2 accent pastels per frame; no slideshow/screensaver failure modes.

## Real assets (this revision)

- `whatsapp-open-photo.jpg` — real stock photo, hand opening WhatsApp on a phone. Hook backdrop.
- `whatsapp-status-crowded.jpg` — real WhatsApp Status-tab screenshot, crowded with product-photo statuses. Raison 1 hero.
- `whatsapp-status-viewer.jpg` — real WhatsApp screenshot, a status being viewed with others floating alongside. Raison 2 hero.
- `saudagar-site.jpg` — real e-commerce catalog screenshot (generic reference site, not the user's own build). Raison 3's "site" side.
- `nyara-site.jpg` / `aura-site.jpg` — the user's own real site builds. Pivot/Preuve proof (unchanged from the prior cut).

---

## Frame 1 — Hook

- scene: A real photo of someone opening WhatsApp punches in behind the question
- duration: 4s
- transition_in: cut
- status: animated
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

## Frame 2 — Raison 1

- scene: The real crowded WhatsApp status screen IS the shot — the newest entry is visibly lost in the pile
- duration: 5s
- transition_in: zoom-through
- status: animated
- type: pain_point
- persuasion: naming a familiar frustration, backed by a real screenshot
- blueprint: device-surface-showcase (Reproduce) + motion-blur-streak entrance
- focal: whatsapp-status-crowded.jpg
- roles: whatsapp-status-crowded.jpg = cutout (hero, framed as a phone-card, contain-fit so no status entry is cropped away)
- asset_candidates: assets/whatsapp-status-crowded.jpg — real WhatsApp status list screenshot, crowded with product statuses
- src: compositions/frames/02-raison1.html
- voiceover: "Il y a trop de statuts. Le tien passe inapercu."

Reproduce: the held-device-surface signature, now with a REAL screenshot instead of an invented list — the zoom-through cut from Frame 1 lands directly on it at speed.

Scene 1 (0.0-0.5s): `whatsapp-status-crowded.jpg` lands via the zoom-through cut's incoming half (scale 0.75->1.0, blur 10px->0px, opacity 0.15->1.0, expo.out) inside a bordered card, ~78% of frame, centered.
Scene 2 (0.5-3.4s): a thin coral annotation ring/arrow spring-pops onto the bottom status entry (the "newest" one) as the line lands, then a soft pulse (opacity 0.6<->1) repeats twice, unanswered.
Scene 3 (3.4-5.0s): held on the crowded, real screen - no further motion, the ring's pulse fades to a steady faint state.

## Frame 3 — Raison 2

- scene: A second real screenshot shows a status being viewed while other statuses float alongside — visual overload, not just invisibility
- duration: 5s
- transition_in: blur-crossfade
- status: animated
- type: pain_point
- persuasion: naming a second, related frustration, backed by a real screenshot
- blueprint: device-surface-showcase (Reproduce)
- focal: whatsapp-status-viewer.jpg
- roles: whatsapp-status-viewer.jpg = cutout (hero, framed as a phone-card, contain-fit)
- asset_candidates: assets/whatsapp-status-viewer.jpg — real WhatsApp screenshot, a status being viewed with others floating
- src: compositions/frames/03-raison2.html
- voiceover: "Si tu postes trop, les gens se lassent - meme ceux qui aiment ce que tu vends."

Scene 1 (0.0-1.6s): `whatsapp-status-viewer.jpg` blur-crossfades in (continuity feel from Frame 2's phone-card, softer entrance than the zoom-through cuts), ~78% of frame, centered.
Scene 2 (1.6-3.6s): a small grey "muted" bell-badge spring-pops onto the card's corner as the line's first half lands; a second badge pops on as "meme ceux qui aiment ce que tu vends" lands.
Scene 3 (3.6-5.0s): held - the screen reads as quietly ignored, no further motion.

## Frame 4 — Raison 3 (transition)

- scene: A split beat contrasts the fading WhatsApp status against a real site sliding in and simply staying put
- duration: 6s
- transition_in: zoom-through
- status: animated
- type: reveal
- persuasion: contrast / setup for the pivot, now with a real site preview instead of an empty mock browser
- blueprint: comparison-split (Adapt)
- focal: saudagar-site.jpg
- roles: whatsapp-status-crowded.jpg = supporting (small, left pane, reused/cropped tighter) · saudagar-site.jpg = cutout (right pane, real site preview)
- asset_candidates: assets/whatsapp-status-crowded.jpg — reused small on the left (statut side); assets/saudagar-site.jpg — real site screenshot, right pane preview of "un site"
- src: compositions/frames/04-raison3.html
- voiceover: "Un statut, ca dure 24h. Un site, on peut le voir quand on veut."

Adapt: the right pane is now a REAL site screenshot (`saudagar-site.jpg`) sliding in with a motion-blur-streak push, not an empty mock browser.

Scene 1 (0.0-2.2s): canvas splits pink/offwhite down the center as the line's first half lands; left pane holds a small crop of `whatsapp-status-crowded.jpg` (docked left, ~35% of frame width), a circular countdown ring drains around it (24 -> 0), fading to 20% opacity as the ring completes.
Scene 2 (2.2-4.6s): right pane's `saudagar-site.jpg` push-enters (motion-blur-streak, scale 1.1->1.0, blur 12px->0px) as the line's second half lands, mirrored tilt to the left pane for book-open symmetry. Split-screen, ~50/50.
Scene 3 (4.6-6.0s): held - left side fully faded (24h up), right site sits steady and un-faded, holding the contrast for the read.

## Frame 5 — Pivot + Preuve

- scene: The real site from Frame 4 hands off to the user's OWN real sites as the actual proof
- duration: 6s
- transition_in: push-slide
- status: animated
- type: proof
- persuasion: the pivot statement, backed by real evidence (the user's own work, not a generic reference)
- blueprint: device-surface-showcase (Reproduce)
- focal: nyara-site.jpg
- roles: nyara-site.jpg = cutout (hero, first proof) · aura-site.jpg = supporting (second proof, arrives just after)
- asset_candidates: assets/nyara-site.jpg — real screenshot of the NYARA fashion site, hero proof; assets/aura-site.jpg — real screenshot of the AURA skincare site, supporting proof
- src: compositions/frames/05-pivot-preuve.html
- voiceover: "Un site, c'est toujours la. Et ca fait plus serieux."

Reproduce: stays the calmest beat of the video by design — the push-slide cut lands, then the two real screenshots hold with minimal added motion so they can breathe.

Scene 1 (0.0-1.6s): `nyara-site.jpg` push-slides in from the Frame 4 cut (continuing the same rightward push, decelerating to a stop - cut-the-curve velocity match), settling centered, ~70% of frame, subtle drop shadow only.
Scene 2 (1.6-3.4s): the nyara window settles fully; the green label-pill "TOUJOURS LA" spring-pops gently top-of-frame, one small particle-burst marks the landing (the video's confirming "yes" beat).
Scene 3 (3.4-5.2s): `aura-site.jpg` slides/fades in from the right edge, docking as a smaller supporting card overlapping the nyara window's bottom-right corner (asymmetric 70/30, 2 depth layers) as "et ca fait plus serieux" lands.
Scene 4 (5.2-6.0s): held read on both real screenshots together - no further motion.

## Frame 6 — CTA (doux)

- scene: A calm closing line offers to show what the viewer's own site could look like - an invitation, delivered with a confident spring-pop landing
- duration: 5s
- transition_in: cut
- status: animated
- type: cta
- persuasion: soft single next step, punchier visual close
- blueprint: kinetic-type-beats (Adapt) + spring-pop-entrance + particle-burst
- assets: none — typographic only
- src: compositions/frames/06-cta.html
- voiceover: "Envie de voir a quoi ressemblerait le tien ? Ecris SITE en message."

Adapt: same yellow bookend as Frame 1; the button now lands with a confident spring-pop (back.out overshoot) + a small particle-burst, more energy than the first pass while the copy itself stays an invitation, not a hard sell.

Scene 1 (0.0-1.6s): yellow canvas wash; the line "ENVIE DE VOIR A QUOI RESSEMBLERAIT LE TIEN ?" fades up (2 lines, soft drift), centered top-half.
Scene 2 (1.6-3.4s): a button-primary spring-pops to center (scale 0.7->1.0, back.out(1.6)): "ECRIS 'SITE' EN MESSAGE"; a small particle-burst (6-8 dots) fires from the button on landing.
Scene 3 (3.4-5.0s): held final read - button and question sit still; video ends on this frame.
