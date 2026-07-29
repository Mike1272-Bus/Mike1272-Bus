---
format: 1080x1920
duration: 50.3s
message: "L'erreur qui fait exploser le prix de tes pubs Facebook: y toucher pendant la phase d'apprentissage."
arc: Accroche -> Explication -> Erreur -> Consequence -> Solution -> CTA
audience: petits commercants qui font ou envisagent de faire de la pub Facebook/Meta
mode: autonomous
music: none
---

## Video direction

- **Palette system** (from `frame.md`, BlockFrame): offwhite (`#FFFDF5`) resting canvas, one pastel wash per frame for pacing — blue (accroche), green (explication), cream (erreur), yellow (consequence), blue (solution), pink/yellow split (CTA).
- **Two-image frames** (Accroche, Explication, Erreur, Consequence, Solution) — **standing rule since video 4**: the two real images/illustrations stack vertically, one directly above the other, both full-size cards, both fully visible at all times, never overlapping or occluding each other. Top card lands first (spring-pop from above), bottom card lands second (spring-pop from below), then both hold with independent-phase sine-wave-loop idle drift.
- **Single-image frame** (CTA): the agent-generated "S'abonner" illustration presented as one large hero card.
- **Captions — mandatory standing rule since video 4**: every voiceover line captioned, word-grouped, synced to `audio/lines/NN.words.json` via the shared BlockFrame caption skin (root-level captions track, not authored inside individual frames). Frame workers respect the caption keep-out zone (nothing below y=1600px).
- **Tone**: sharp, non-obvious insight — NOT a beginner's generic guide (explicit user rejection of an earlier generic-steps draft: "tout le monde sait tout ca"). Direct, plain, spoken French, second person ("tu").
- **Hook and CTA get elevated motion** (series-consistent): Frame 1 opens with a confident zoom-through card land; Frame 6 (CTA) closes with a spring-pop bell/subscribe landing plus a particle-burst.
- **Negative list**: no image stretched to fill the canvas alone; no more than 2 accent pastels per frame; no slideshow (front-load-then-freeze); two-image scenes must never overlap/occlude (hard rule, checked visually before render).

## Real assets

See `capture/extracted/asset-descriptions.md` for full descriptions. File map:

- `accroche-pub-explose.png` (top) / `accroche-erreur-alerte.jpg` (bottom) — Accroche
- `explication-lancement.png` (top) / `explication-apprentissage.png` (bottom) — Explication
- `erreur-impatience.jpg` (top) / `erreur-reflexion.jpg` (bottom) — Erreur
- `consequence-restart.jpg` (top) / `consequence-adsmanager.webp` (bottom) — Consequence
- `solution-multiplateforme.jpg` (top) / `solution-pub-reussie.webp` (bottom) — Solution
- `cta-sabonner.png` (single hero) — CTA

## Audio

Kokoro TTS (`ff_siwis`, French) per-line, staged at `audio/lines/NN.wav` with word timing at `audio/lines/NN.words.json` (deterministic character-weighted estimate — no network ASR available in this environment; re-run `audio/estimate-words.mjs` against the real duration once the user's own recorded voice replaces a line).

---

## Frame 1 — Accroche

- scene: Two illustrations stack vertically — a pub/money graphic on top, a document-review alert below — both fully visible, never overlapping
- duration: 7.9s
- transition_in: zoom-through
- status: animated
- type: hook
- persuasion: naming a costly, invisible mistake most advertisers make without realizing
- blueprint: comparison-split (Adapt — vertical stack, no-occlusion rule) + spring-pop-entrance
- roles: accroche-pub-explose.png = top card (running a Facebook ad) · accroche-erreur-alerte.jpg = bottom card (something's wrong, unnoticed)
- asset_candidates: assets/accroche-pub-explose.png — illustration, laptop with ad banners, money, thumbs up; assets/accroche-erreur-alerte.jpg — illustration, magnifying glass over documents with warning triangle
- src: compositions/frames/01-accroche.html
- voiceover: "Il y a une erreur que presque tout le monde fait sur ses pubs Facebook, et qui fait exploser le prix sans qu'on comprenne pourquoi."
- words: audio/lines/01.words.json (duration 7.36s)

Scene 1 (0.0-0.5s): blue canvas wash zoom-through-cuts in.
Scene 2 (0.3-1.0s): `accroche-pub-explose.png` spring-pops in from above, settling in the TOP half (~44% height, tilted -2deg).
Scene 3 (1.0-1.7s): `accroche-erreur-alerte.jpg` spring-pops in from below, settling in the BOTTOM half (~44% height, tilted +2deg) — clear vertical gap preserved.
Scene 4 (1.7-7.9s): both cards keep independent-phase sine-wave-loop idle drift for the rest of the hold.

## Frame 2 — Explication

- scene: Two illustrations stack vertically — a rocket launch on top, the "60% learning phase" ring below — both fully visible, never overlapping
- duration: 8.2s
- transition_in: push-slide
- status: animated
- type: pain_point
- persuasion: teaching the mechanism (the learning phase exists) before revealing the mistake
- blueprint: comparison-split (Adapt — vertical stack, no-occlusion rule) + spring-pop-entrance
- roles: explication-lancement.png = top card (launching a new ad) · explication-apprentissage.png = bottom card (the learning-phase concept, already-validated agent illustration)
- asset_candidates: assets/explication-lancement.png — illustration, rocket launching; assets/explication-apprentissage.png — agent-generated illustration, "60% Apprentissage" progress ring
- src: compositions/frames/02-explication.html
- voiceover: "Quand tu lances une pub, Facebook a besoin de quelques jours pour comprendre a qui la montrer. Ca s'appelle la phase d'apprentissage."
- words: audio/lines/02.words.json (duration 7.659s)

Scene 1 (0.0-0.5s): green canvas wash push-slides in from the right.
Scene 2 (0.3-1.0s): `explication-lancement.png` spring-pops in from above, settling in the TOP half (~44% height, tilted -2deg).
Scene 3 (1.0-1.7s): `explication-apprentissage.png` spring-pops in from below, settling in the BOTTOM half (~44% height, tilted +2deg) — clear vertical gap preserved.
Scene 4 (1.7-8.2s): both cards keep independent-phase sine-wave-loop idle drift for the rest of the hold.

## Frame 3 — Erreur

- scene: Two images stack vertically — a real photo of an impatient man checking his watch on top, a pensive figure making a decision below — both fully visible, never overlapping
- duration: 9.2s
- transition_in: zoom-through
- status: animated
- type: pain_point
- persuasion: naming the exact human behavior that causes the mistake — not waiting
- blueprint: comparison-split (Adapt — vertical stack, no-occlusion rule) + spring-pop-entrance
- roles: erreur-impatience.jpg = top card (the impatience) · erreur-reflexion.jpg = bottom card (the impulsive decision to edit)
- asset_candidates: assets/erreur-impatience.jpg — real photo, businessman checking his watch impatiently; assets/erreur-reflexion.jpg — illustration, pensive figure on the phone with an idea bulb
- src: compositions/frames/03-erreur.html
- voiceover: "Le probleme, c'est que la plupart des gens n'attendent pas. Ils voient que ca marche pas encore, et ils changent le texte, l'image, ou le budget tout de suite."
- words: audio/lines/03.words.json (duration 8.619s)

Scene 1 (0.0-0.5s): cream canvas wash zoom-through-cuts in.
Scene 2 (0.3-1.0s): `erreur-impatience.jpg` spring-pops in from above, settling in the TOP half (~44% height, tilted -2deg).
Scene 3 (1.0-1.7s): `erreur-reflexion.jpg` spring-pops in from below, settling in the BOTTOM half (~44% height, tilted +2deg) — clear vertical gap preserved.
Scene 4 (1.7-9.2s): both cards keep independent-phase sine-wave-loop idle drift for the rest of the hold.

## Frame 4 — Consequence

- scene: Two images stack vertically — a "RESTART" icon on top, the Ads Manager dashboard below — both fully visible, never overlapping
- duration: 9.2s
- transition_in: push-slide
- status: animated
- type: pain_point
- persuasion: making the invisible cost visible and literal — everything resets, the price climbs back up
- blueprint: comparison-split (Adapt — vertical stack, no-occlusion rule) + spring-pop-entrance
- roles: consequence-restart.jpg = top card (the reset, the core consequence) · consequence-adsmanager.webp = bottom card (where it happens, the tool context)
- asset_candidates: assets/consequence-restart.jpg — icon illustration, RESTART with circular arrows; assets/consequence-adsmanager.webp — illustration, Ads Manager dashboard with charts
- src: compositions/frames/04-consequence.html
- voiceover: "Sauf que des que tu modifies quelque chose, Facebook recommence a zero. Toute l'avance qu'il avait prise est perdue, et ta pub redevient chere pour rien."
- words: audio/lines/04.words.json (duration 8.661s)

Scene 1 (0.0-0.5s): yellow canvas wash push-slides in from the right.
Scene 2 (0.3-1.0s): `consequence-restart.jpg` spring-pops in from above, settling in the TOP half (~44% height, tilted -2deg).
Scene 3 (1.0-1.7s): `consequence-adsmanager.webp` spring-pops in from below, settling in the BOTTOM half (~44% height, tilted +2deg) — clear vertical gap preserved.
Scene 4 (1.7-9.2s): both cards keep independent-phase sine-wave-loop idle drift for the rest of the hold.

## Frame 5 — Solution

- scene: Two images stack vertically — a multi-platform ad mockup on top, a real successful ad example below — both fully visible, never overlapping
- duration: 11s
- transition_in: zoom-through
- status: animated
- type: benefit_highlight
- persuasion: landing the fix with concrete proof of what a well-run ad looks like
- blueprint: comparison-split (Adapt — vertical stack, no-occlusion rule) + spring-pop-entrance
- roles: solution-multiplateforme.jpg = top card (professional multi-channel presence) · solution-pub-reussie.webp = bottom card (real proof, a working ad)
- asset_candidates: assets/solution-multiplateforme.jpg — illustration, ad mockups across Facebook/Messenger/Instagram/WhatsApp; assets/solution-pub-reussie.webp — real screenshot, a successful Instagram/Facebook ad example
- src: compositions/frames/05-solution.html
- voiceover: "La bonne methode: tu laisses la pub tourner au moins 3 a 4 jours sans y toucher, meme si les premiers resultats semblent faibles. C'est apres ca que tu regardes vraiment si ca marche."
- words: audio/lines/05.words.json (duration 10.368s)

Scene 1 (0.0-0.5s): blue canvas wash zoom-through-cuts in.
Scene 2 (0.3-1.0s): `solution-multiplateforme.jpg` spring-pops in from above, settling in the TOP half (~44% height, tilted -2deg).
Scene 3 (1.0-1.7s): `solution-pub-reussie.webp` spring-pops in from below, settling in the BOTTOM half (~44% height, tilted +2deg) — clear vertical gap preserved.
Scene 4 (1.7-11.0s): both cards keep independent-phase sine-wave-loop idle drift for the rest of the hold.

## Frame 6 — CTA

- scene: The agent-generated "S'abonner" bell illustration lands with the video's second most energetic beat, a particle-burst marking its landing
- duration: 4.8s
- transition_in: zoom-through
- status: animated
- type: cta
- persuasion: single soft next step — subscribe to learn to manage ads correctly, no product ask
- blueprint: cta-morph-press (Adapt) + spring-pop-entrance + particle-burst
- focal: cta-sabonner.png
- asset_candidates: assets/cta-sabonner.png — agent-generated illustration, notification bell + "S'ABONNER" button
- src: compositions/frames/06-cta.html
- voiceover: "Abonne-toi si tu veux en apprendre plus sur comment gerer ta publicite."
- words: audio/lines/06.words.json (duration 3.989s)

Scene 1 (0.0-0.5s): pink/yellow split canvas wash zoom-through-cuts in.
Scene 2 (0.3-1.0s): `cta-sabonner.png` spring-pops to center (scale 0.7->1.0, back.out(1.8) overshoot), tilted -2deg; a particle-burst (7-8 dots) fires on landing.
Scene 3 (1.0-4.8s): held final read — graphic keeps a very subtle sine-wave-loop micro-bob only; video ends on this frame.
