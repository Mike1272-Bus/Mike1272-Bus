---
format: 1080x1920
duration: 30s
message: "4 outils simples pour vendre en ligne, meme si tu debutes."
arc: Hook -> Outil 1 -> Outil 2 -> Outil 3 -> Outil 4 -> CTA
audience: petits commercants qui vendent via WhatsApp ou un site peu professionnel
mode: autonomous
music: none
---

## Video direction

- **Palette system** (from `frame.md`, BlockFrame): offwhite (`#FFFDF5`) resting canvas, one pastel wash per tool frame for visual pacing: blue (outil 1), pink (outil 2), green (outil 3), cream (outil 4), yellow bookend on hook + CTA.
- **Motion grammar + reveal model**: long-tail `power3`/`expo`/`back.out` eases. Real images are ALWAYS presented as a layered collage (2 cards per tool frame, offset + tilted, depth via size/shadow) — never full-bleed, since none of the source photos cover a 9:16 canvas alone. Each card enters via spring-pop or motion-blur-streak, then — this is the explicit ask — never goes fully static: every card keeps a continuous **sine-wave-loop** idle drift/rotation (small amplitude, ~2-3 finite cycles) for the rest of its scene, so the whole video reads as alive, not a slideshow.
- **Hook and CTA get the video's best motion design** (explicit ask): Frame 1 opens with a fast zoom-through flash-preview of all 4 tool visuals before the headline lands; Frame 6 closes with a spring-pop button landing plus a particle-burst, reusing the `shop-now-button.jpg` cursor-click graphic as a literal visual echo of "click here."
- **Rhythm**: tool frames (2-5) are the steadier midsection — collage lands, drifts, holds. Frame 1 and Frame 6 carry the most energy and the most cuts-per-second.
- **Negative list**: no image ever stretched to fill the full canvas alone (all are real photos with their own margins/whitespace — respect that, collage instead of crop-to-fill); no more than 2 accent pastels per frame; no slideshow (front-load-then-freeze) or screensaver (independent unrelated drifting) failure modes — the idle drift must read as ONE coherent floating collage, not scattered elements.

## Real assets

- `ecommerce-icons.jpg` / `oliverbirch-site.jpg` / `shop-now-button.jpg` — Outil 1 (boutique en ligne pro).
- `canva-adjust.jpg` / `canva-magicstudio.jpg` — Outil 2 (Canva).
- `meta-ads-collage.png` / `meta-reels-ads-examples.png` — Outil 3 (Meta Business Suite).
- `capcut-editor-1.png` / `capcut-editor-2.png` — Outil 4 (CapCut).

---

## Frame 1 — Hook

- scene: A fast flash-preview of all 4 tools' visuals cuts through before the headline lands — the video's most energetic beat
- duration: 4s
- transition_in: cut
- status: animated
- type: hook
- persuasion: curiosity / value-preview
- blueprint: kinetic-type-beats (Adapt) + zoom-through flash-preview
- assets: none in this frame directly (the flash-preview reuses tiny crops as abstract color/shape flashes, not full images — the real images land properly in their own frames)
- src: compositions/frames/01-hook.html
- voiceover: "4 outils simples pour vendre en ligne, meme si tu debutes."

Adapt: this is the video's showcase beat for motion design. Four rapid zoom-through flashes (one per tool's accent color: blue/pink/green/cream) cut through at speed before the number-pill lands — a taste of what's coming, not the real reveal.

Scene 1 (0.0-0.8s): four quick zoom-through color flashes cut in sequence (0.2s each: blue, pink, green, cream full-bleed washes), each with peak motion-blur (18-20px) at the cut, establishing pace before any text.
Scene 2 (0.8-1.8s): a black number-pill "4 OUTILS" spring-pops in (back.out overshoot) top-third on the settled offwhite canvas; one particle-burst (6-7 dots, mixed palette) marks its landing.
Scene 3 (1.8-3.3s): the line "SIMPLES POUR VENDRE EN LIGNE, MEME SI TU DEBUTES" fades in line by line (2 lines), soft upward drift. Centered, ~55% of frame.
Scene 4 (3.3-4.0s): held read, a yellow underline-tick draws under "DEBUTES" as the sole added motion.

## Frame 2 — Outil 1 : boutique en ligne professionnelle

- scene: A real online store screenshot and a generic e-commerce icon graphic land as a floating collage, drifting continuously
- duration: 5s
- transition_in: zoom-through
- status: animated
- type: value
- persuasion: naming the foundational tool, backed by a real site example
- blueprint: compose (layered collage) + sine-wave-loop idle
- focal: oliverbirch-site.jpg
- roles: oliverbirch-site.jpg = cutout (hero card, larger, front layer) · ecommerce-icons.jpg = supporting (smaller card, back layer, offset top-left) · shop-now-button.jpg = accent (small, bottom-right corner, arrives last)
- asset_candidates: assets/oliverbirch-site.jpg — real professional e-commerce site screenshot, hero card; assets/ecommerce-icons.jpg — generic e-commerce icon illustration, supporting card; assets/shop-now-button.jpg — 3D shop-now button graphic, accent
- src: compositions/frames/02-outil1.html
- voiceover: "Avoir une boutique en ligne professionnelle: la base pour vendre serieusement, sans dependre d'un simple statut ou d'un profil Instagram."

Scene 1 (0.0-0.5s): `oliverbirch-site.jpg` lands via the zoom-through cut's incoming half (scale 0.75->1.0, blur 10px->0px, opacity 0.15->1.0, expo.out), tilted -3deg, ~70% of frame, centered-right.
Scene 2 (0.5-1.3s): `ecommerce-icons.jpg` spring-pops in behind/left of it (smaller card, tilted +4deg, offset top-left, back.out), establishing the layered collage.
Scene 3 (1.3-2.0s): `shop-now-button.jpg` spring-pops in small, bottom-right corner, slight overlap onto the hero card's corner.
Scene 4 (2.0-5.0s): all three cards keep a continuous sine-wave-loop idle drift (small y-bob + +-1deg rotation, offset phase per card so they don't move in unison, 3 finite cycles) for the rest of the hold — nothing goes fully static.

## Frame 3 — Outil 2 : Canva

- scene: Two real Canva screenshots land as a floating collage, drifting continuously
- duration: 5s
- transition_in: push-slide
- status: animated
- type: value
- persuasion: naming a genuinely useful design tool, backed by real screenshots
- blueprint: compose (layered collage) + sine-wave-loop idle
- focal: canva-magicstudio.jpg
- roles: canva-magicstudio.jpg = cutout (hero card, logo visible, front layer) · canva-adjust.jpg = supporting (smaller card, back layer, offset)
- asset_candidates: assets/canva-magicstudio.jpg — real Canva Magic Studio screenshot with logo, hero card; assets/canva-adjust.jpg — real Canva adjust-panel screenshot, supporting card
- src: compositions/frames/03-outil2.html
- voiceover: "Canva: cree des visuels pro en quelques minutes, sans designer."

Scene 1 (0.0-2.2s): pink canvas wash settles (carried from the push-slide cut); `canva-magicstudio.jpg` push-slides in from the right (cut-the-curve velocity match, decelerating to rest), tilted -2deg, ~72% of frame, centered.
Scene 2 (2.2-3.0s): `canva-adjust.jpg` spring-pops in behind/below it (smaller card, tilted +5deg, offset bottom-left, back.out).
Scene 3 (3.0-5.0s): both cards keep a continuous sine-wave-loop idle drift (offset phase, 3 finite cycles) for the rest of the hold.

## Frame 4 — Outil 3 : Meta Business Suite

- scene: A Meta Ads illustration and real Reels ad examples land as a floating collage, drifting continuously
- duration: 5s
- transition_in: zoom-through
- status: animated
- type: value
- persuasion: naming the ads-management tool, backed by real ad examples
- blueprint: compose (layered collage) + sine-wave-loop idle
- focal: meta-ads-collage.png
- roles: meta-ads-collage.png = cutout (hero card, front layer) · meta-reels-ads-examples.png = supporting (smaller card, back layer, offset)
- asset_candidates: assets/meta-ads-collage.png — Meta Ads illustration (megaphone/logo), hero card; assets/meta-reels-ads-examples.png — real Reels sponsored-ad examples, supporting card
- src: compositions/frames/04-outil3.html
- voiceover: "Meta Business Suite: gere ta page et tes pubs au meme endroit."

Scene 1 (0.0-0.5s): `meta-ads-collage.png` lands via the zoom-through cut's incoming half (scale 0.75->1.0, blur 10px->0px, opacity 0.15->1.0, expo.out), tilted -2deg, ~70% of frame, centered.
Scene 2 (0.5-1.4s): `meta-reels-ads-examples.png` spring-pops in behind/right of it (smaller card, tilted +4deg, offset, back.out).
Scene 3 (1.4-5.0s): both cards keep a continuous sine-wave-loop idle drift (offset phase, 3 finite cycles) for the rest of the hold.

## Frame 5 — Outil 4 : CapCut

- scene: Two real CapCut screenshots land as a floating collage, drifting continuously
- duration: 5s
- transition_in: push-slide
- status: animated
- type: value
- persuasion: naming a self-serve video tool, backed by real screenshots (including the CapCut logo)
- blueprint: compose (layered collage) + sine-wave-loop idle
- focal: capcut-editor-1.png
- roles: capcut-editor-1.png = cutout (hero card, front layer) · capcut-editor-2.png = supporting (smaller card showing the CapCut logo, back layer, offset)
- asset_candidates: assets/capcut-editor-1.png — real CapCut editor screenshot, hero card; assets/capcut-editor-2.png — real CapCut screenshot with logo visible, supporting card
- src: compositions/frames/05-outil4.html
- voiceover: "CapCut: monte tes propres videos de promo, directement depuis ton telephone."

Scene 1 (0.0-2.2s): cream canvas wash settles (carried from the push-slide cut); `capcut-editor-1.png` push-slides in from the right (cut-the-curve velocity match), tilted -3deg, ~72% of frame, centered.
Scene 2 (2.2-3.0s): `capcut-editor-2.png` spring-pops in behind/above it (smaller card, tilted +3deg, offset, back.out) — its CapCut logo stays clearly visible, not occluded by the hero card.
Scene 3 (3.0-5.0s): both cards keep a continuous sine-wave-loop idle drift (offset phase, 3 finite cycles) for the rest of the hold.

## Frame 6 — CTA

- scene: A confident closing invitation lands with the video's best motion design, echoing "click here" with the shop-now cursor graphic
- duration: 6s
- transition_in: zoom-through
- status: animated
- type: cta
- persuasion: soft single next step, most elevated motion in the video alongside the hook
- blueprint: kinetic-type-beats (Adapt) + spring-pop-entrance + particle-burst
- focal: shop-now-button.jpg
- roles: shop-now-button.jpg = supporting (small accent, arrives late, echoes the button's own click cursor onto the real CTA button)
- asset_candidates: assets/shop-now-button.jpg — 3D shop-now button graphic with click cursor, CTA accent
- src: compositions/frames/06-cta.html
- voiceover: "Besoin d'aide pour tout connecter ensemble ? Ecris OUTILS en message."

Adapt: same yellow bookend as Frame 1 for series continuity. This is the video's second-most-energetic beat: a confident spring-pop button landing, a particle-burst, and the shop-now cursor graphic sliding in to visually "click" the real CTA button a beat after it lands.

Scene 1 (0.0-1.6s): yellow canvas wash zoom-through-cuts in; the line "BESOIN D'AIDE POUR TOUT CONNECTER ENSEMBLE ?" fades up (2 lines, soft drift), centered top-half.
Scene 2 (1.6-2.3s): the button-primary spring-pops to center (scale 0.7->1.0, back.out(1.6) overshoot): "ECRIS 'OUTILS' EN MESSAGE"; a particle-burst (7-8 dots) fires from the button on landing.
Scene 3 (2.3-3.1s): `shop-now-button.jpg`'s cursor graphic (cropped to just the hand/cursor) slides in from bottom-right and settles pointing at the real CTA button, as if about to click it — a literal, playful echo of the reference image.
Scene 4 (3.1-6.0s): held final read - button, cursor accent, and question sit still (cursor keeps a very subtle sine-wave-loop micro-bob only); video ends on this frame.
