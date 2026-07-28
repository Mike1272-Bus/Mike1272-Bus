---
format: 1080x1920
duration: 45.5s
message: "Mon avis sur les nouvelles regles de pub Facebook/Meta: la difference se joue sur la preparation."
arc: Accroche -> Suite -> Explication 1 -> Explication 2 -> Consequence 1 -> Consequence 2 -> Avis final -> CTA
audience: petits commercants / entrepreneurs qui font ou envisagent de faire de la pub Facebook/Meta
mode: autonomous
music: none
---

## Video direction

- **Palette system** (from `frame.md`, BlockFrame): offwhite (`#FFFDF5`) resting canvas, one pastel wash per frame for pacing — blue (accroche), cream (suite/perte), pink (explication 1), green (explication 2), yellow (consequence 1), blue (consequence 2), cream (avis final), pink/yellow (CTA).
- **Single-image frames** (Accroche, Suite, Explication 1, Consequence 1, Consequence 2, CTA): one real image presented as a large tilted card (spring-pop or motion-blur-streak entrance), continuous sine-wave-loop idle drift for the rest of the hold — same grammar as videos 2/3.
- **Two-image frames** (Explication 2, Avis final) — **explicit new rule, replaces the tilted-overlap collage from videos 2/3**: the two real images stack **vertically, one directly above the other**, both full-size cards, both fully visible at all times, never overlapping or occluding each other. Top card lands first (spring-pop from above), bottom card lands second (spring-pop from below), then both hold with independent-phase sine-wave-loop idle drift (small, so they never visually collide across the seam).
- **Captions — mandatory on this and every future video** (standing rule): every voiceover line is captioned on screen, word-grouped (3-4 words/group), synced to `audio/lines/NN.words.json` timestamps. Style: BlockFrame `card-elevated` pill (white, 4px black border, 8px black shadow) holding black Inter 800 uppercase text, positioned lower-third (~650px from bottom on the 1920 canvas), one group visible at a time, spring-pop in / hard-kill out per the caption authoring contract. Never covers the frame's real image.
- **Hook and CTA get the video's best motion design** (series-consistent, per videos 1/3): Frame 1 opens with a confident zoom-through card land; Frame 8 closes with a spring-pop sticker landing plus a particle-burst.
- **Tone**: plain, simple French sentences (no figurative/"AI-sounding" language — constraint validated on video 2). This is an opinion piece, not a product pitch: no ADG mention, no product CTA, only "Abonne-toi."
- **Negative list**: no image stretched to fill the canvas alone; no more than 2 accent pastels per frame; no slideshow (front-load-then-freeze); two-image scenes must never overlap/occlude (hard rule, checked visually before render).

## Real assets

See `capture/extracted/asset-descriptions.md` for full descriptions. File map:

- `meta-apps-phone.jpg` — Accroche
- `money-bag-loss.jpg` — Suite
- `targeting-manual.jpg` — Explication 1
- `advantage-plus.jpg` (top) / `meta-logo-reactions.png` (bottom) — Explication 2
- `rethink-planning.jpg` — Consequence 1
- `dashboard-earnings.jpg` — Consequence 2
- `meta-reading-book.jpg` (top) / `megaphone-target.jpg` (bottom) — Avis final
- `abonne-toi-sticker.jpg` — CTA

## Audio

Kokoro TTS (`ff_siwis`, French) per-line, staged at `audio/lines/NN.wav` with word timing at `audio/lines/NN.words.json` (deterministic character-weighted estimate — no network ASR available in this environment; re-run `audio/estimate-words.mjs` against the real duration once the user's own recorded voice replaces a line, captions re-sync automatically from the same word list shape).

---

## Frame 1 — Accroche

- scene: A real photo of a phone showing the Meta ecosystem lands with confident motion, opening the video's opinion
- duration: 4s
- transition_in: zoom-through
- status: animated
- type: hook
- persuasion: naming the familiar starting point (wanting to advertise on Facebook)
- blueprint: kinetic-type-beats (Adapt) + spring-pop-entrance
- focal: meta-apps-phone.jpg
- asset_candidates: assets/meta-apps-phone.jpg — real photo, phone + Meta/FB/IG/WhatsApp icons floating
- src: compositions/frames/01-accroche.html
- voiceover: "Tu veux faire de la pub pour ton produit sur Facebook."
- words: audio/lines/01.words.json (duration 3.307s)

Scene 1 (0.0-0.5s): blue canvas wash zoom-through-cuts in.
Scene 2 (0.3-1.0s): `meta-apps-phone.jpg` spring-pops in large, tilted -2deg, ~75% of frame, centered (back.out overshoot).
Scene 3 (1.0-4.0s): continuous sine-wave-loop idle drift (small y-bob + -+1deg rotation) for the rest of the hold. Captions: 3 groups synced to words.json.

## Frame 2 — Suite (le risque)

- scene: A money-bag-with-a-hole illustration lands, spilling coins and bills, landing the stakes
- duration: 5s
- transition_in: push-slide
- status: animated
- type: pain_point
- persuasion: naming the risk (losing money) if you don't know the new rules
- blueprint: kinetic-type-beats (Compose) + spring-pop-entrance
- focal: money-bag-loss.jpg
- asset_candidates: assets/money-bag-loss.jpg — illustration, money bag with hole losing coins/cash
- src: compositions/frames/02-suite.html
- voiceover: "Mais si tu ne connais pas les nouvelles regles, tu risques de perdre de l'argent pour rien."
- words: audio/lines/02.words.json (duration 4.565s)

Scene 1 (0.0-0.5s): cream canvas wash push-slides in from the right (cut-the-curve velocity match).
Scene 2 (0.3-1.0s): `money-bag-loss.jpg` spring-pops in, tilted +3deg, ~70% of frame, centered.
Scene 3 (1.0-5.0s): continuous sine-wave-loop idle drift for the rest of the hold. Captions: 4 groups synced to words.json.

## Frame 3 — Explication 1 (avant)

- scene: A real Meta Ads Manager screenshot of manual targeting settings lands as proof of "how it used to work"
- duration: 5s
- transition_in: zoom-through
- status: animated
- type: pain_point
- persuasion: grounding the "before" claim in a real screenshot
- blueprint: kinetic-type-beats (Compose) + spring-pop-entrance
- focal: targeting-manual.jpg
- asset_candidates: assets/targeting-manual.jpg — real screenshot, manual age/gender/language/interest targeting panel
- src: compositions/frames/03-explication1.html
- voiceover: "Avant, tu choisissais toi-meme qui voit ta pub: l'age, la ville, les centres d'interet."
- words: audio/lines/03.words.json (duration 4.587s)

Scene 1 (0.0-0.5s): pink canvas wash zoom-through-cuts in.
Scene 2 (0.3-1.0s): `targeting-manual.jpg` spring-pops in, tilted -3deg, ~72% of frame, centered.
Scene 3 (1.0-5.0s): continuous sine-wave-loop idle drift for the rest of the hold. Captions: 4 groups synced to words.json.

## Frame 4 — Explication 2 (aujourd'hui)

- scene: Two real/illustrated images stack vertically — the Advantage+ auto-targeting proof on top, the Meta-decides illustration below — both fully visible, never overlapping
- duration: 7s
- transition_in: push-slide
- status: animated
- type: pain_point
- persuasion: grounding the "AI decides now" claim in a real screenshot, paired with a supporting illustration
- blueprint: comparison-split (Adapt — vertical stack instead of side-by-side, per explicit no-occlusion rule) + spring-pop-entrance
- roles: advantage-plus.jpg = top card (hero, real screenshot) · meta-logo-reactions.png = bottom card (support, illustration)
- asset_candidates: assets/advantage-plus.jpg — real screenshot, "Advantage+ on" auto-targeting audience collage; assets/meta-logo-reactions.png — illustration, person + Meta logo + reaction emojis
- src: compositions/frames/04-explication2.html
- voiceover: "Aujourd'hui, Facebook prefere decider lui-meme qui voit ta pub, grace a son intelligence artificielle."
- words: audio/lines/04.words.json (duration 6.549s)

Scene 1 (0.0-0.5s): green canvas wash push-slides in from the right.
Scene 2 (0.3-1.0s): `advantage-plus.jpg` spring-pops in from above, settling in the TOP half of the frame (~44% height, full width margin, tilted -2deg).
Scene 3 (1.0-1.7s): `meta-logo-reactions.png` spring-pops in from below, settling in the BOTTOM half of the frame (~44% height, tilted +2deg) — a clear vertical gap separates the two cards; neither ever crosses into the other's half.
Scene 4 (1.7-7.0s): both cards keep independent-phase sine-wave-loop idle drift (small amplitude, so they never approach the gap) for the rest of the hold. Captions: 5 groups synced to words.json.

## Frame 5 — Consequence 1 (mal preparee)

- scene: A real photo of a person overwhelmed by scattered, disorganized thought-icons lands, symbolizing a poorly prepared campaign
- duration: 6.5s
- transition_in: zoom-through
- status: animated
- type: pain_point
- persuasion: visualizing "unprepared = costly/scattered"
- blueprint: kinetic-type-beats (Compose) + spring-pop-entrance
- focal: rethink-planning.jpg
- asset_candidates: assets/rethink-planning.jpg — real photo, man thinking surrounded by scattered doodle icons
- src: compositions/frames/05-consequence1.html
- voiceover: "Resultat: une pub mal preparee coute plus cher, et touche des gens qui ne sont pas vraiment interesses."
- words: audio/lines/05.words.json (duration 5.995s)

Scene 1 (0.0-0.5s): yellow canvas wash zoom-through-cuts in.
Scene 2 (0.3-1.0s): `rethink-planning.jpg` spring-pops in, tilted -2deg, ~72% of frame, centered.
Scene 3 (1.0-6.5s): continuous sine-wave-loop idle drift for the rest of the hold. Captions: 5 groups synced to words.json.

## Frame 6 — Consequence 2 (bien pensee)

- scene: A real Facebook professional dashboard screenshot lands, showing real earnings growth as proof of a well-prepared campaign paying off
- duration: 6.5s
- transition_in: push-slide
- status: animated
- type: benefit_highlight
- persuasion: grounding "well-prepared = profitable" in real proof (rising earnings/insights)
- blueprint: dataviz-countup (Adapt — held real dashboard rather than an animated counter) + spring-pop-entrance
- focal: dashboard-earnings.jpg
- asset_candidates: assets/dashboard-earnings.jpg — real screenshot, Facebook professional dashboard with rising earnings/insights
- src: compositions/frames/06-consequence2.html
- voiceover: "Mais une pub bien pensee, avec un bon message et de bonnes images, devient beaucoup plus rentable."
- words: audio/lines/06.words.json (duration 6.016s)

Scene 1 (0.0-0.5s): blue canvas wash push-slides in from the right.
Scene 2 (0.3-1.0s): `dashboard-earnings.jpg` spring-pops in, tilted +2deg, ~72% of frame, centered.
Scene 3 (1.0-6.5s): continuous sine-wave-loop idle drift for the rest of the hold. Captions: 5 groups synced to words.json.

## Frame 7 — Avis final

- scene: Two illustrated images stack vertically — a person reading/studying (understanding) on top, a megaphone with a bullseye-target (aiming well) below — both fully visible, never overlapping
- duration: 6.5s
- transition_in: zoom-through
- status: animated
- type: benefit_highlight
- persuasion: landing the video's opinion — preparation (understanding + aim) is what makes the difference now
- blueprint: comparison-split (Adapt — vertical stack, no-occlusion rule) + spring-pop-entrance
- roles: meta-reading-book.jpg = top card (hero, understanding) · megaphone-target.jpg = bottom card (support, aiming well)
- asset_candidates: assets/meta-reading-book.jpg — illustration, Meta-headed figure reading a book; assets/megaphone-target.jpg — illustration, megaphone + phone + bullseye with dart
- src: compositions/frames/07-avis.html
- voiceover: "Mon avis: aujourd'hui, la difference ne se joue plus sur le ciblage. Elle se joue sur la preparation."
- words: audio/lines/07.words.json (duration 5.653s)

Scene 1 (0.0-0.5s): cream canvas wash zoom-through-cuts in.
Scene 2 (0.3-1.0s): `meta-reading-book.jpg` spring-pops in from above, settling in the TOP half (~44% height, tilted -2deg).
Scene 3 (1.0-1.7s): `megaphone-target.jpg` spring-pops in from below, settling in the BOTTOM half (~44% height, tilted +2deg) — clear vertical gap preserved.
Scene 4 (1.7-6.5s): both cards keep independent-phase sine-wave-loop idle drift for the rest of the hold. Captions: 5 groups synced to words.json.

## Frame 8 — CTA

- scene: The "Abonne-toi" sticker lands with the video's second most energetic beat, a particle-burst marking its landing
- duration: 3.5s
- transition_in: zoom-through
- status: animated
- type: cta
- persuasion: single soft next step — no product ask, subscribe only
- blueprint: cta-morph-press (Adapt) + spring-pop-entrance + particle-burst
- focal: abonne-toi-sticker.jpg
- asset_candidates: assets/abonne-toi-sticker.jpg — real sticker graphic, "Abonne toi !" red arrow
- src: compositions/frames/08-cta.html
- voiceover: "Abonne-toi pour en apprendre plus a ce sujet."
- words: audio/lines/08.words.json (duration 2.304s)

Scene 1 (0.0-0.5s): pink/yellow split canvas wash zoom-through-cuts in.
Scene 2 (0.3-1.0s): `abonne-toi-sticker.jpg` spring-pops to center (scale 0.7->1.0, back.out(1.8) overshoot), tilted -3deg; a particle-burst (7-8 dots) fires on landing.
Scene 3 (1.0-3.5s): held final read — sticker keeps a very subtle sine-wave-loop micro-bob only; video ends on this frame. Captions: 2 groups synced to words.json.
