---
format: 1080x1920
duration: 34s
message: "Ta boutique en ligne pro, livree vite avec l'IA, a prix imbattable"
arc: Hook -> Agitation -> Solution -> Offre -> Garantie -> CTA
audience: petits commercants qui vendent via WhatsApp ou un site peu professionnel
mode: autonomous
music: none
---

## Video direction

- **Palette system** (from `frame.md`, BlockFrame): offwhite (`#FFFDF5`) as the resting canvas, black ink for type/borders, one pastel accent rationed per frame (yellow for the hook's alarm energy, pink for agitation, blue for the solution reveal, green for the offer/money beat, cream for the guarantee breather, yellow again for the CTA to bookend the video). Never more than two pastels live on screen at once.
- **Motion grammar + reveal model**: long-tail `power3` eases everywhere (smooth deceleration, no bounce). Beat-paced reveal — since this cut carries no voiceover, each Scene's text/card enters on its own beat window exactly like a VO-paced reveal would; nothing appears before its window, and the canvas never gets dumped at t=0. Idle content may carry, at most, a subtle 1-2px jitter or slow scale breathe — no drift, no lazy pan.
- **Rhythm / held-frame allocation**: Frames 1, 3 and 6 are fast punches (hook, reveal, CTA). Frame 5 (the guarantee) is the deliberate held breather — content resolves early in its window and then just sits, calm, before the CTA's final punch.
- **Negative list**: no stock photography, no generic floating gradient blobs / fake "AI" bokeh, no browser chrome or fake cursors, no more than 2 accent pastels per frame, no slideshow (front-load-then-freeze) and no screensaver (independent floating elements) failure modes. Every frame is typographic/graphic only — no captured or external image assets exist in this project.

---

## Frame 1 — Hook

- scene: A blunt question slams onto a yellow-cracked canvas, daring the viewer to keep scrolling
- duration: 4s
- transition_in: cut
- status: outline
- type: hook
- persuasion: pattern interrupt
- blueprint: kinetic-type-beats (Reproduce)
- assets: none — typographic only
- src: compositions/frames/01-hook.html
- voiceover: "Ton business tourne encore sur un statut WhatsApp ?"

Open cold, no logo, no preamble — the question IS the thesis.

Scene 1 (0.0-1.4s): bare offwhite canvas; a thick black label-pill top-third reading "STOP." scale-pops in from 0 on power3, star-burst decoration (yellow) punches into the top-right corner half a beat later. Centered template, ~30% of frame.
Scene 2 (1.4-3.0s): the line "TU VENDS ENCORE SUR WHATSAPP ?" types/slams in word-by-word (heading-xl, black on offwhite), each word landing with a hard 4px-border card-pop, no bounce. Centered, stacked 2-3 lines, ~55% of frame.
Scene 3 (3.0-4.0s): everything holds still — a single yellow stripe-block ticks in diagonally behind the type as the only added motion, reading as tension, not clutter. Held read.

## Frame 2 — Agitation

- scene: Three pain-cards slam down one after another, stacking the cost of staying invisible
- duration: 6s
- transition_in: crossfade
- status: outline
- type: pain_point
- persuasion: pain agitation
- blueprint: kinetic-type-beats (Adapt)
- assets: none — typographic only
- src: compositions/frames/02-agitation.html
- voiceover: "Un lien qui inspire pas confiance. Des clients qui hesitent. Des ventes qui partent chez le concurrent qui, lui, a une vraie boutique."

Adapt: keep the escalating-card signature move; three sequential pain cards instead of a single statement, each heavier than the last.

Scene 1 (0.0-1.8s): pink stripe-block wipes in from the left edge as ground; first card-small ("PAS DE VRAIE BOUTIQUE") pops top-left as the line names it. Asymmetric 70/30, layered depth building.
Scene 2 (1.8-3.8s): second card-elevated slams in mid-frame, slightly larger and rotated -3deg ("CLIENTS QUI DOUTENT"), overlapping the first card's corner (depth: overlap + shadow-stack). Reveals exactly as its phrase lands.
Scene 3 (3.8-5.4s): third, heaviest card ("VENTES PERDUES") drops bottom-right, biggest of the three (hierarchy via size 3:1), pink-accented border-glow pulses once on landing.
Scene 4 (5.4-6.0s): brief hold — all three cards sit stacked, reading as a pile of accumulated cost. No further motion.

## Frame 3 — Solution reveal

- scene: The pile of pain collapses and one clean statement takes over the whole canvas
- duration: 6s
- transition_in: crossfade
- status: outline
- type: reveal
- persuasion: relief / turn
- blueprint: typewriter-reveal (Adapt)
- assets: none — typographic only
- src: compositions/frames/03-solution.html
- voiceover: "Et si ta boutique en ligne, pro et credible, etait prete en quelques jours ?"

Adapt: keep the type-then-collapse-then-pop signature; instead of popping a logo/product-UI at the end, pop one bold blue statement card — this project has no brand mark yet.

Scene 1 (0.0-2.2s): on blue canvas wash, the line "ET SI TA BOUTIQUE ETAIT PRETE... EN QUELQUES JOURS ?" types in live, monospace-cursor blink visible (label/counter type), left-aligned, ~60% of frame.
Scene 2 (2.2-3.4s): the typed line collapses (scale-down + fade) toward center — the "here's the everyday pain, now here's us" pivot.
Scene 3 (3.4-6.0s): a single oversized card-elevated pops from the collapse point: "BOUTIQUE PRO. CREEE AVEC L'IA." (heading-xl, black on white card, blue border-glow). Centered, hero, ~50% of frame, then holds still for the read.

## Frame 4 — The offer

- scene: Three offer bullets assemble into a grid, then a price-anchor comparison lands the value gap
- duration: 7s
- transition_in: crossfade
- status: outline
- type: offer
- persuasion: value equation (Hormozi) + price anchor
- blueprint: grid-card-assemble (Adapt)
- assets: none — typographic only
- src: compositions/frames/04-offer.html
- voiceover: "Design professionnel. Livraison en quelques jours. Le tout a un prix qu'une agence classique ne pratique jamais."

Adapt: keep the self-assembling tile-grid signature for the three offer bullets; extend with one extra beat — a struck-through "agence" price versus the real offer price — instead of stopping at the grid.

Scene 1 (0.0-2.0s): green canvas wash; label-pill "L'OFFRE" scale-pops top-center. Three empty card-small outlines fade in as skeleton slots in a row, ~70% width.
Scene 2 (2.0-4.4s): the three cards self-assemble one at a time as each benefit is named — "DESIGN PRO", "LIVRAISON RAPIDE", "PRIX IMBATTABLE" — each snapping into its slot with a hard-shadow pop, staggered left to right. Grid, ~75% of frame.
Scene 3 (4.4-6.0s): below the grid, a card-elevated drops in showing a struck-through higher price label ("AGENCE : DES MOIS, DES MILLIERS D'EUROS") in muted grey, crossed out with a hard black line-draw animation.
Scene 4 (6.0-7.0s): beside it, the real offer price-anchor card pops in bold black-on-yellow ("NOUS : QUELQUES JOURS, UN PRIX JUSTE"), bigger than the struck one (hierarchy via size). Hold on the contrast.

## Frame 5 — Guarantee (breather)

- scene: One calm, held title card states the guarantee — the video's deliberate quiet beat
- duration: 5s
- transition_in: crossfade
- status: outline
- type: proof
- persuasion: risk reversal (Hormozi guarantee)
- blueprint: titlecard-reveal (Adapt)
- assets: none — typographic only
- src: compositions/frames/05-guarantee.html
- voiceover: "Et si le rendu ne te plait pas, on retravaille jusqu'a ce que ce soit parfait."

Adapt: single calm two-line card instead of the three-beat prelude chain — this is the video's breather, content resolves fast then just sits.

Scene 1 (0.0-1.6s): cream canvas; a label-pill "GARANTIE" scale-pops center-top, immediately followed by a card-elevated centered beneath it.
Scene 2 (1.6-2.6s): the card's line resolves in one clean motion (no letter-by-letter): "PAS SATISFAIT ? ON CORRIGE JUSQU'A CE QUE CA TE PLAISE." Centered, ~50% of frame.
Scene 3 (2.6-5.0s): held read — content already resolved, canvas stays still (only a barely-there 1-2px card jitter), deliberately quiet before the CTA's final punch.

## Frame 6 — CTA

- scene: A bold closing card locks in the single next action, punctuated by a hard landing
- duration: 6s
- transition_in: cut
- status: outline
- type: cta
- persuasion: single clear next step
- blueprint: kinetic-type-beats (Adapt)
- assets: none — typographic only
- src: compositions/frames/06-cta.html
- voiceover: "Ecris-moi BOUTIQUE en message et on demarre ta boutique des aujourd'hui."

Adapt: keep the beat-by-beat kinetic landing but resolve on a CTA action-card instead of a logo — bookend the video's opening yellow energy.

Scene 1 (0.0-1.6s): yellow canvas wash (bookends Frame 1); label-pill "PRET A DEMARRER ?" scale-pops top-third.
Scene 2 (1.6-3.6s): button-primary sized up to hero scale slams to center: "ECRIS 'BOUTIQUE' EN MESSAGE" (Inter 700, black on yellow, hard shadow), landing with one decisive card-pop on power3 — no bounce.
Scene 3 (3.6-5.0s): a star-burst decoration punches into one corner as the only added motion; button gets a single hard-shadow pulse (press-and-release) to read as clickable.
Scene 4 (5.0-6.0s): final hold — button + label sit still, full read, video ends on this frame (no exit motion needed; it's the last frame).
