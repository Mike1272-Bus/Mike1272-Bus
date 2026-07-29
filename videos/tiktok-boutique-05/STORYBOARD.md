---
format: 1080x1920
duration: 54.3s
message: "Le vrai probleme quand tu vends sur WhatsApp: le temps de reponse, pas ton produit."
arc: Accroche -> Situation -> Probleme -> Consequence -> Declic -> Solution -> Benefice -> CTA
audience: petits commercants qui vendent via WhatsApp
mode: autonomous
music: none
---

## Video direction

- **Palette system** (from `frame.md`, BlockFrame): offwhite (`#FFFDF5`) resting canvas, one pastel wash per frame for pacing — blue (accroche), pink (situation), cream (probleme), yellow (consequence), green (declic), blue (solution), pink (benefice), yellow/pink split (CTA).
- **Single-image frames** (Accroche, Probleme, Declic, Solution, CTA): one real image/illustration presented as a large tilted card (spring-pop or motion-blur-streak entrance), continuous sine-wave-loop idle drift for the rest of the hold — same grammar as videos 2-4.
- **Two-image frames** (Situation, Consequence, Benefice) — **standing rule since video 4**: the two real images stack vertically, one directly above the other, both full-size cards, both fully visible at all times, never overlapping or occluding each other. Top card lands first (spring-pop from above), bottom card lands second (spring-pop from below), then both hold with independent-phase sine-wave-loop idle drift.
- **Captions — mandatory standing rule since video 4**: every voiceover line is captioned on screen, word-grouped, synced to `audio/lines/NN.words.json` timestamps via the shared BlockFrame caption skin (root-level captions track, built by `captions.mjs`, not authored inside individual frames). Frame workers must respect the caption keep-out zone (nothing below y=1600px on the 1920-tall canvas).
- **Tone**: testimonial/"vecu" — second person ("tu"), never "je". Plain, simple, spoken French (natural contractions like "t'etais", "c'est pas") — no figurative/"AI-sounding" language.
- **Hook and CTA get elevated motion** (series-consistent): Frame 1 opens with a confident zoom-through card land; Frame 8 closes with a spring-pop "link in bio" landing plus a particle-burst and a subtle upward-pointing cursor animation echoing "look up at your bio".
- **Negative list**: no image stretched to fill the canvas alone; no more than 2 accent pastels per frame; no slideshow (front-load-then-freeze); two-image scenes must never overlap/occlude (hard rule, checked visually before render).

## Real assets

See `capture/extracted/asset-descriptions.md` for full descriptions. File map:

- `accroche-whatsapp-phone.jpg` (hero) / `accroche-business-doodle.jpg` (small accent) — Accroche
- `situation-client-demande.png` (top) / `situation-client-parti.png` (bottom) — Situation
- `probleme-occupee-dm.jpg` — Probleme
- `consequence-notif-badge.jpg` (top) / `consequence-femme-bureau.jpg` (bottom) — Consequence
- `declic-sablier.png` — Declic
- `solution-boutique-illustration.jpg` — Solution
- `benefice-email-confirmation.png` (top) / `benefice-achat-mobile.jpg` (bottom) — Benefice
- `cta-link-in-bio.png` — CTA

## Audio

Kokoro TTS (`ff_siwis`, French) per-line, staged at `audio/lines/NN.wav` with word timing at `audio/lines/NN.words.json` (deterministic character-weighted estimate — no network ASR available in this environment; re-run `audio/estimate-words.mjs` against the real duration once the user's own recorded voice replaces a line).

---

## Frame 1 — Accroche

- scene: A real photo of someone happily checking WhatsApp lands, setting up the "you've been there" hook
- duration: 7s
- transition_in: zoom-through
- status: animated
- type: hook
- persuasion: universal relatable opener, naming the everyday tool (WhatsApp) before the twist
- blueprint: kinetic-type-beats (Adapt) + spring-pop-entrance
- focal: accroche-whatsapp-phone.jpg
- roles: accroche-whatsapp-phone.jpg = hero (large card) · accroche-business-doodle.jpg = small accent (corner, arrives after hero)
- asset_candidates: assets/accroche-whatsapp-phone.jpg — real photo, phone + WhatsApp; assets/accroche-business-doodle.jpg — hand-drawn business/social doodle
- src: compositions/frames/01-accroche.html
- voiceover: "Si tu fais du business en ligne avec WhatsApp, tu t'es sans doute deja retrouve dans la situation ou..."
- words: audio/lines/01.words.json (duration 6.571s)

Scene 1 (0.0-0.5s): blue canvas wash zoom-through-cuts in.
Scene 2 (0.3-1.0s): `accroche-whatsapp-phone.jpg` spring-pops in large, tilted -2deg, ~75% of frame, centered.
Scene 3 (1.0-1.7s): `accroche-business-doodle.jpg` spring-pops in small, corner accent, tilted +5deg.
Scene 4 (1.7-7.0s): continuous sine-wave-loop idle drift on both for the rest of the hold.

## Frame 2 — Situation

- scene: Two real staged WhatsApp screenshots stack vertically — the client's question on top, the too-late reply and lost sale on bottom — both fully visible, never overlapping
- duration: 6.8s
- transition_in: push-slide
- status: animated
- type: pain_point
- persuasion: the concrete, relatable proof of the hook's setup — a real (staged) conversation showing exactly how a sale is lost
- blueprint: comparison-split (Adapt — vertical stack, no-occlusion rule) + spring-pop-entrance
- roles: situation-client-demande.png = top card (the question) · situation-client-parti.png = bottom card (the loss)
- asset_candidates: assets/situation-client-demande.png — WhatsApp mockup, client asks about a sofa in stock; assets/situation-client-parti.png — WhatsApp mockup, late reply + client already bought elsewhere
- src: compositions/frames/02-situation.html
- voiceover: "...un client te demande le prix. Le temps que tu reponds, deux heures apres, il a disparu. Plus jamais de nouvelles."
- words: audio/lines/02.words.json (duration 6.293s)

Scene 1 (0.0-0.5s): pink canvas wash push-slides in from the right.
Scene 2 (0.3-1.0s): `situation-client-demande.png` spring-pops in from above, settling in the TOP half (~44% height, tilted -2deg).
Scene 3 (1.0-1.7s): `situation-client-parti.png` spring-pops in from below, settling in the BOTTOM half (~44% height, tilted +2deg) — clear vertical gap preserved, neither card ever crosses into the other's half.
Scene 4 (1.7-6.8s): both cards keep independent-phase sine-wave-loop idle drift for the rest of the hold.

## Frame 3 — Probleme

- scene: A real photo of someone happily distracted by other messages lands, showing why the reply came late
- duration: 7.4s
- transition_in: zoom-through
- status: animated
- type: pain_point
- persuasion: humanizing the lapse — not malice, just an ordinary busy moment
- blueprint: kinetic-type-beats (Compose) + spring-pop-entrance
- focal: probleme-occupee-dm.jpg
- asset_candidates: assets/probleme-occupee-dm.jpg — real photo, woman on phone with casual chat bubbles, distracted
- src: compositions/frames/03-probleme.html
- voiceover: "Pourtant t'as rien fait de mal. T'etais juste occupe, comme tous les jours. Mais pour lui, t'as mis trop de temps, et il est alle voir ailleurs."
- words: audio/lines/03.words.json (duration 6.891s)

Scene 1 (0.0-0.5s): cream canvas wash zoom-through-cuts in.
Scene 2 (0.3-1.0s): `probleme-occupee-dm.jpg` spring-pops in, tilted +3deg, ~72% of frame, centered.
Scene 3 (1.0-7.4s): continuous sine-wave-loop idle drift for the rest of the hold.

## Frame 4 — Consequence

- scene: Two images stack vertically — a WhatsApp icon buried under 79 unread messages on top, an ordinary workday photo below — both fully visible, never overlapping
- duration: 9s
- transition_in: push-slide
- status: animated
- type: pain_point
- persuasion: quantifying the invisible cost — sales lost quietly, every week, without the seller ever noticing
- blueprint: comparison-split (Adapt — vertical stack, no-occlusion rule) + spring-pop-entrance
- roles: consequence-notif-badge.jpg = top card (the accumulating cost) · consequence-femme-bureau.jpg = bottom card (ordinary business-as-usual)
- asset_candidates: assets/consequence-notif-badge.jpg — WhatsApp icon with 79 unread badge; assets/consequence-femme-bureau.jpg — real photo, businesswoman working at her desk
- src: compositions/frames/04-consequence.html
- voiceover: "Et ca, ca t'arrive plus souvent que tu crois. Tu perds des ventes chaque semaine, sans meme t'en rendre compte. Tu te dis juste que les gens ne sont pas interesses."
- words: audio/lines/04.words.json (duration 8.576s)

Scene 1 (0.0-0.5s): yellow canvas wash push-slides in from the right.
Scene 2 (0.3-1.0s): `consequence-notif-badge.jpg` spring-pops in from above, settling in the TOP half (~44% height, tilted -2deg).
Scene 3 (1.0-1.7s): `consequence-femme-bureau.jpg` spring-pops in from below, settling in the BOTTOM half (~44% height, tilted +2deg) — clear vertical gap preserved.
Scene 4 (1.7-9.0s): both cards keep independent-phase sine-wave-loop idle drift for the rest of the hold.

## Frame 5 — Declic

- scene: An hourglass icon circled by turning arrows lands, marking the video's turning point
- duration: 5.2s
- transition_in: zoom-through
- status: animated
- type: pain_point
- persuasion: the reveal beat — reframing the whole problem in one line
- blueprint: kinetic-type-beats (Compose) + spring-pop-entrance
- focal: declic-sablier.png
- asset_candidates: assets/declic-sablier.png — hourglass icon with circular time-turning arrows
- src: compositions/frames/05-declic.html
- voiceover: "Mais en vrai, le probleme c'est pas ton produit. C'est le temps que ca prend pour repondre."
- words: audio/lines/05.words.json (duration 4.715s)

Scene 1 (0.0-0.5s): green canvas wash zoom-through-cuts in.
Scene 2 (0.3-1.0s): `declic-sablier.png` spring-pops in, centered, tilted -2deg, ~68% of frame — this is a reveal beat, so keep it clean/centered rather than collaged.
Scene 3 (1.0-5.2s): continuous sine-wave-loop idle drift (small, steady) for the rest of the hold.

## Frame 6 — Solution

- scene: A real e-commerce storefront illustration lands, showing the answer to the problem
- duration: 8.8s
- transition_in: push-slide
- status: animated
- type: benefit_highlight
- persuasion: naming the solution with a concrete visual of prices/photos/stock available instantly
- blueprint: kinetic-type-beats (Compose) + spring-pop-entrance
- focal: solution-boutique-illustration.jpg
- asset_candidates: assets/solution-boutique-illustration.jpg — illustration, online storefront with buy buttons and shoppers
- src: compositions/frames/06-solution.html
- voiceover: "Avec une vraie boutique en ligne, le client voit direct le prix, les photos, si c'est en stock. Il n'a plus besoin d'attendre apres toi pour se decider."
- words: audio/lines/06.words.json (duration 8.384s)

Scene 1 (0.0-0.5s): blue canvas wash push-slides in from the right.
Scene 2 (0.3-1.0s): `solution-boutique-illustration.jpg` spring-pops in, tilted -3deg, ~72% of frame, centered.
Scene 3 (1.0-8.8s): continuous sine-wave-loop idle drift for the rest of the hold.

## Frame 7 — Benefice

- scene: Two images stack vertically — a real order-confirmation email on top, an easy mobile-checkout illustration below — both fully visible, never overlapping
- duration: 6.9s
- transition_in: zoom-through
- status: animated
- type: benefit_highlight
- persuasion: proving the "sells even while you sleep" claim with a real unattended-purchase artifact
- blueprint: comparison-split (Adapt — vertical stack, no-occlusion rule) + spring-pop-entrance
- roles: benefice-email-confirmation.png = top card (real proof, a completed order) · benefice-achat-mobile.jpg = bottom card (the easy mobile purchase experience)
- asset_candidates: assets/benefice-email-confirmation.png — real order confirmation email; assets/benefice-achat-mobile.jpg — illustration, mobile storefront with buy button and card
- src: compositions/frames/07-benefice.html
- voiceover: "Il peut commander a n'importe quelle heure. Meme la nuit, meme quand tu dors, ta boutique continue de vendre a ta place."
- words: audio/lines/07.words.json (duration 6.4s)

Scene 1 (0.0-0.5s): pink canvas wash zoom-through-cuts in.
Scene 2 (0.3-1.0s): `benefice-email-confirmation.png` spring-pops in from above, settling in the TOP half (~44% height, tilted -2deg).
Scene 3 (1.0-1.7s): `benefice-achat-mobile.jpg` spring-pops in from below, settling in the BOTTOM half (~44% height, tilted +2deg) — clear vertical gap preserved.
Scene 4 (1.7-6.9s): both cards keep independent-phase sine-wave-loop idle drift for the rest of the hold.

## Frame 8 — CTA

- scene: The "link in bio" graphic lands with the video's second most energetic beat, a particle-burst marking its landing
- duration: 3.2s
- transition_in: zoom-through
- status: animated
- type: cta
- persuasion: single soft next step — link in bio, no "message me" ask
- blueprint: cta-morph-press (Adapt) + spring-pop-entrance + particle-burst
- focal: cta-link-in-bio.png
- asset_candidates: assets/cta-link-in-bio.png — illustration, "LINK IN BIO" button with clicking cursor
- src: compositions/frames/08-cta.html
- voiceover: "Le lien est en bio si tu veux la tienne."
- words: audio/lines/08.words.json (duration 2.069s)

Scene 1 (0.0-0.5s): pink/yellow split canvas wash zoom-through-cuts in.
Scene 2 (0.3-1.0s): `cta-link-in-bio.png` spring-pops to center (scale 0.7->1.0, back.out(1.8) overshoot), tilted -2deg; a particle-burst (7-8 dots) fires on landing.
Scene 3 (1.0-3.2s): held final read — graphic keeps a very subtle sine-wave-loop micro-bob only; video ends on this frame.
