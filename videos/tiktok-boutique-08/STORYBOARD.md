---
format: 1080x1920
duration: 45.1s
message: "Le vrai probleme n'est pas la concurrence, c'est le manque de confiance que ton profil inspire."
arc: Accroche -> Developpement -> Probleme -> Exemple -> Avis final -> CTA
audience: petits commercants qui vendent en ligne
mode: autonomous
music: none
---

## Video direction

- **Palette system** (from `frame.md`, BlockFrame): offwhite resting canvas, one pastel wash per frame — blue (accroche), green (developpement), pink (probleme), yellow (exemple), cream (avis final), pink/yellow split (CTA).
- **NEW standing rule: 3 sequential images per scene, hard cut.** Each narrative scene (all except CTA) shows exactly one image at a time, full-hero, timed to a clause of the voiceover. When the next clause begins, the current image is replaced (fast fade/scale-out then the next image spring-pops/cuts in) — never two images visible together. Image start times below come directly from the Kokoro word-timing (character-weighted estimate), not arbitrary guesses.
- **Single-image frame** (CTA): held for the whole line, standard spring-pop + particle-burst treatment.
- **Captions — mandatory standing rule since video 4**: every voiceover line captioned, word-grouped, synced via the shared BlockFrame caption skin (root-level captions track). Keep all content above y=1600px.
- **Tone**: opinion piece, direct, second person ("tu"), never "je".
- **Negative list**: no two of the 3 sequential images ever overlap on screen at once; no slideshow-style front-loading (each image genuinely lands on its own clause).

## Real assets

Agent-generated BlockFrame illustrations (see `capture/extracted/asset-descriptions.md`). File map per scene, in image order:

- Accroche: `accroche-1-concurrence.png` / `accroche-2-envrai.png` / `accroche-3-pasleprobleme.png`
- Developpement: `developpement-1-milliers.png` / `developpement-2-vendfacile.png` / `developpement-3-memenombre.png`
- Probleme: `probleme-1-confiance.png` / `probleme-2-jamais.png` / `probleme-3-inspirerien.png`
- Exemple: `exemple-1-memeprix.png` / `exemple-2-deuxprofils.png` / `exemple-3-lechoix.png`
- Avis final: `avis-1-stop.png` / `avis-2-demandetoi.png` / `avis-3-toimeme.png`
- CTA: `cta-confiance.png`

## Audio

Kokoro TTS (`ff_siwis`, French) per-line, staged at `audio/lines/NN.wav` with word timing at `audio/lines/NN.words.json`.

---

## Frame 1 — Accroche

- duration: 5.5s
- transition_in: zoom-through
- status: animated
- type: hook
- src: compositions/frames/01-accroche.html
- voiceover: "Tu penses que c'est la concurrence qui t'empeche de vendre ? En vrai, c'est pas ca le probleme."
- words: audio/lines/01.words.json (duration 4.8s)

Scene 1 (0.0-0.3s): blue wash zoom-through-cuts in.
Scene 2 (0.3-3.06s): `accroche-1-concurrence.png` cuts in (spring-pop), holds through "Tu penses que c'est la concurrence qui t'empeche de vendre ?".
Scene 3 (3.06-3.54s): `accroche-1-concurrence.png` cuts OUT, `accroche-2-envrai.png` cuts in, holds through "En vrai,".
Scene 4 (3.54-5.5s): `accroche-2-envrai.png` cuts OUT, `accroche-3-pasleprobleme.png` cuts in, holds through "c'est pas ca le probleme." to the end.

## Frame 2 — Developpement

- duration: 8.2s
- transition_in: push-slide
- status: animated
- type: pain_point
- src: compositions/frames/02-developpement.html
- voiceover: "Il y a des milliers de vendeurs sur le meme produit que toi. Et pourtant, certains vendent facilement, sans avoir moins de concurrents que toi."
- words: audio/lines/02.words.json (duration 7.509s)

Scene 1 (0.0-0.3s): green wash push-slides in from the right.
Scene 2 (0.3-3.22s): `developpement-1-milliers.png` cuts in, holds through "Il y a des milliers de vendeurs sur le meme produit que toi.".
Scene 3 (3.22-5.40s): cut to `developpement-2-vendfacile.png`, holds through "Et pourtant, certains vendent facilement,".
Scene 4 (5.40-8.2s): cut to `developpement-3-memenombre.png`, holds through "sans avoir moins de concurrents que toi." to the end.

## Frame 3 — Probleme

- duration: 6.1s
- transition_in: zoom-through
- status: animated
- type: pain_point
- src: compositions/frames/03-probleme.html
- voiceover: "Le vrai probleme, c'est la confiance. Un client n'achete jamais chez quelqu'un qui ne lui inspire rien."
- words: audio/lines/03.words.json (duration 5.419s)

Scene 1 (0.0-0.3s): pink wash zoom-through-cuts in.
Scene 2 (0.3-2.04s): `probleme-1-confiance.png` cuts in, holds through "Le vrai probleme, c'est la confiance.".
Scene 3 (2.04-3.35s): cut to `probleme-2-jamais.png`, holds through "Un client n'achete jamais".
Scene 4 (3.35-6.1s): cut to `probleme-3-inspirerien.png`, holds through "chez quelqu'un qui ne lui inspire rien." to the end.

## Frame 4 — Exemple

- duration: 13.5s
- transition_in: push-slide
- status: animated
- type: pain_point
- src: compositions/frames/04-exemple.html
- voiceover: "Deux vendeurs, meme produit, meme prix. L'un a un profil pro, des vraies photos, des avis. L'autre a juste un statut WhatsApp flou. Le client va choisir celui qui lui donne confiance, pas celui qui est deux dollars moins cher."
- words: audio/lines/04.words.json (duration 12.693s)

Scene 1 (0.0-0.3s): yellow wash push-slides in from the right.
Scene 2 (0.3-2.31s): `exemple-1-memeprix.png` cuts in, holds through "Deux vendeurs, meme produit, meme prix.".
Scene 3 (2.31-7.45s): cut to `exemple-2-deuxprofils.png`, holds through "L'un a un profil pro, des vraies photos, des avis. L'autre a juste un statut WhatsApp flou." (longest hold of the video, matches the longest clause).
Scene 4 (7.45-13.5s): cut to `exemple-3-lechoix.png`, holds through "Le client va choisir celui qui lui donne confiance, pas celui qui est deux dollars moins cher." to the end.

## Frame 5 — Avis final

- duration: 7.0s
- transition_in: zoom-through
- status: animated
- type: benefit_highlight
- src: compositions/frames/05-avis.html
- voiceover: "Avant de te plaindre de la concurrence, demande-toi une chose: toi-meme, tu ferais confiance a ta propre boutique ?"
- words: audio/lines/05.words.json (duration 6.293s)

Scene 1 (0.0-0.3s): cream wash zoom-through-cuts in.
Scene 2 (0.3-2.18s): `avis-1-stop.png` cuts in, holds through "Avant de te plaindre de la concurrence,".
Scene 3 (2.18-3.39s): cut to `avis-2-demandetoi.png`, holds through "demande-toi une chose:".
Scene 4 (3.39-7.0s): cut to `avis-3-toimeme.png`, holds through "toi-meme, tu ferais confiance a ta propre boutique ?" to the end.

## Frame 6 — CTA

- duration: 4.8s
- transition_in: zoom-through
- status: animated
- type: cta
- focal: cta-confiance.png
- src: compositions/frames/06-cta.html
- voiceover: "Le lien est en bio si tu veux inspirer plus confiance a tes clients."
- words: audio/lines/06.words.json (duration 3.776s)

Scene 1 (0.0-0.5s): pink/yellow split wash zoom-through-cuts in.
Scene 2 (0.3-1.0s): `cta-confiance.png` spring-pops to center (back.out overshoot); a particle-burst fires on landing.
Scene 3 (1.0-4.8s): held final read, subtle sine-wave-loop micro-bob only; video ends on this frame.
