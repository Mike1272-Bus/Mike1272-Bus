---
format: 1080x1920
duration: 28.437s
message: "Toutes ces lecons disent la meme chose : il est temps de transformer ta boutique WhatsApp en vraie boutique en ligne."
arc: Accroche -> Site+outils -> Pub+reponse -> Apprentissage+confiance -> Transformation -> CTA
audience: petits commercants qui vendent en ligne
mode: autonomous
music: none
---

## Video direction

- **Palette system** (from `frame.md`, BlockFrame): offwhite resting canvas, one pastel wash per frame — blue (accroche), green (site+outils), pink (pub+reponse), yellow (confiance), cream (transformation), pink/yellow split (CTA).
- **Standing rule: 3 sequential images per scene, hard cut.** Each narrative scene (all except CTA) shows exactly one image at a time, full-hero, timed to a clause of the voiceover. Image start times come from the Kokoro word-timing (character-weighted estimate).
- **Single-image frame** (CTA): held for the whole line, standard spring-pop + particle-burst treatment.
- **Captions — mandatory**: every voiceover line captioned, word-grouped, synced via the shared BlockFrame caption skin.
- **Tone**: recap + transformation, direct, second person ("tu"), never "je".
- All images are **reused real assets from videos 02-08** (no new generation) per the user's explicit request.

## Assets

- Accroche: `accroche-1-erreurs.jpg` / `accroche-2-clients.jpg` / `accroche-3-jourapresjour.jpg`
- Site+outils: `siteoutils-1-statut.jpg` / `siteoutils-2-vraisite.jpg` / `siteoutils-3-outils.jpg`
- Pub+reponse: `pubreponse-1-preparation.jpg` / `pubreponse-2-ciblage.jpg` / `pubreponse-3-reponse.jpg`
- Confiance: `confiance-1-tropto.png` / `confiance-2-prix.png` / `confiance-3-confiance.png`
- Transformation: `transformation-1-lecons.jpg` / `transformation-2-transformer.jpg` / `transformation-3-vraieboutique.jpg`
- CTA: `cta-lienenbio.png`

## Audio

Kokoro TTS (`ff_siwis`, French) per-line, staged at `audio/lines/NN.wav` with word timing at `audio/lines/NN.words.json`.

---

## Frame 1 — Accroche

- duration: 4.967s
- transition_in: zoom-through
- status: animated
- type: hook
- src: compositions/frames/01-accroche.html
- voiceover: "Cette semaine, tu as vu plusieurs erreurs qui te coutent des clients, jour apres jour."
- words: audio/lines/01.words.json (duration 4.267s)

Scene 1 (0.0-0.3s): blue wash zoom-through-cuts in.
Scene 2 (0.3-2.35s): `accroche-1-erreurs.jpg` cuts in, holds through "Cette semaine, tu as vu plusieurs erreurs".
Scene 3 (2.35-3.73s): cut to `accroche-2-clients.jpg`, holds through "qui te coutent des clients,".
Scene 4 (3.73-4.967s): cut to `accroche-3-jourapresjour.jpg`, holds through "jour apres jour." to the end.

## Frame 2 — Site+outils (lundi/mardi)

- duration: 5.756s
- transition_in: push-slide
- status: animated
- type: recap
- src: compositions/frames/02-siteoutils.html
- voiceover: "Un statut WhatsApp s'oublie, un vrai site reste, avec les bons outils pour vendre."
- words: audio/lines/02.words.json (duration 5.056s)

Scene 1 (0.0-0.3s): green wash push-slides in.
Scene 2 (0.3-2.03s): `siteoutils-1-statut.jpg` cuts in, holds through "Un statut WhatsApp s'oublie,".
Scene 3 (2.03-3.27s): cut to `siteoutils-2-vraisite.jpg`, holds through "un vrai site reste,".
Scene 4 (3.27-5.756s): cut to `siteoutils-3-outils.jpg`, holds through "avec les bons outils pour vendre." to the end.

## Frame 3 — Pub+reponse (mercredi/jeudi)

- duration: 5.671s
- transition_in: zoom-through
- status: animated
- type: recap
- src: compositions/frames/03-pubreponse.html
- voiceover: "La preparation compte plus que le ciblage, et un client n'attend jamais longtemps une reponse."
- words: audio/lines/03.words.json (duration 4.971s)

Scene 1 (0.0-0.3s): pink wash zoom-through-cuts in.
Scene 2 (0.3-1.08s): `pubreponse-1-preparation.jpg` cuts in, holds through "La preparation".
Scene 3 (1.08-2.58s): cut to `pubreponse-2-ciblage.jpg`, holds through "compte plus que le ciblage,".
Scene 4 (2.58-5.671s): cut to `pubreponse-3-reponse.jpg`, holds through "et un client n'attend jamais longtemps une reponse." to the end.

## Frame 4 — Apprentissage+confiance (vendredi/samedi)

- duration: 5.927s
- transition_in: push-slide
- status: animated
- type: recap
- src: compositions/frames/04-confiance.html
- voiceover: "Casser une pub trop tot fait exploser son prix, et la confiance compte plus que la concurrence."
- words: audio/lines/04.words.json (duration 5.227s)

Scene 1 (0.0-0.3s): yellow wash push-slides in.
Scene 2 (0.3-1.6s): `confiance-1-tropto.png` cuts in, holds through "Casser une pub trop tot".
Scene 3 (1.6-2.92s): cut to `confiance-2-prix.png`, holds through "fait exploser son prix,".
Scene 4 (2.92-5.927s): cut to `confiance-3-confiance.png`, holds through "et la confiance compte plus que la concurrence." to the end.

## Frame 5 — Transformation

- duration: 6.716s
- transition_in: zoom-through
- status: animated
- type: conclusion
- src: compositions/frames/05-transformation.html
- voiceover: "Toutes ces lecons disent la meme chose : il est temps de transformer ta boutique WhatsApp en vraie boutique en ligne."
- words: audio/lines/05.words.json (duration 6.016s)

Scene 1 (0.0-0.3s): cream wash zoom-through-cuts in.
Scene 2 (0.3-2.44s): `transformation-1-lecons.jpg` cuts in, holds through "Toutes ces lecons disent la meme chose :".
Scene 3 (2.44-3.85s): cut to `transformation-2-transformer.jpg`, holds through "il est temps de transformer".
Scene 4 (3.85-6.716s): cut to `transformation-3-vraieboutique.jpg`, holds through "ta boutique WhatsApp en vraie boutique en ligne." to the end.

## Frame 6 — CTA

- duration: 2.9s
- transition_in: zoom-through
- status: animated
- type: cta
- focal: cta-lienenbio.png
- src: compositions/frames/06-cta.html
- voiceover: "Le lien est en bio."
- words: audio/lines/06.words.json (duration 1.173s)

Scene 1 (0.0-0.3s): pink/yellow split wash zoom-through-cuts in.
Scene 2 (0.3-0.8s): `cta-lienenbio.png` spring-pops to center; a particle-burst fires on landing.
Scene 3 (0.8-2.9s): held final read, subtle sine-wave-loop micro-bob only; video ends on this frame.
