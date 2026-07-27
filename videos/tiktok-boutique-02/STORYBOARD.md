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

- **Palette system** (from `frame.md`, BlockFrame): offwhite (`#FFFDF5`) resting canvas throughout for a calmer, more consistent feel than video 1 (which rotated a pastel per frame). One pastel accent per frame, softer usage: blue for the WhatsApp-mockup frames (screen-glow, neutral/tech), pink for the transition/contrast beat, green for the real-site reveal (money/credibility signal), yellow bookend on hook + CTA only (kept from video 1 for series continuity).
- **Motion grammar + reveal model**: long-tail `power3` eases; entrances are gentler than video 1 - fades and modest scale-ins (0.9->1) rather than hard "slam" card-pops, matching the softer, less confrontational script. Beat-paced reveal still applies: nothing appears before its line is "spoken" (its beat window).
- **Rhythm / held-frame allocation**: Frame 5 (pivot/reveal with the real site proof) is the held climax - let the two real screenshots breathe, minimal added motion once they land. Frame 1 (hook) and Frame 6 (CTA) are the only frames with slightly more energy, to bookend the calmer middle.
- **Negative list**: no stock photography beyond the two real site screenshots (which ARE the point - genuine proof, not decoration), no invented logos, no more than 2 accent pastels per frame, no slideshow/screensaver failure modes, no aggressive "slam" motion (reserve that register for video 1's harder sell, not this softer educational piece).

---

## Frame 1 — Hook

- scene: A calm numbered intro states the video's premise as a plain question, not a confrontation
- duration: 4s
- transition_in: cut
- status: animated
- type: hook
- persuasion: curiosity / pattern-naming (soft)
- blueprint: kinetic-type-beats (Reproduce)
- assets: none — typographic only
- src: compositions/frames/01-hook.html
- voiceover: "3 raisons pour lesquelles on ne te prend pas au serieux sur WhatsApp."

Calmer register than video 1's "STOP." hook - a number card, not an alarm.

Scene 1 (0.0-1.3s): offwhite canvas; a black number-pill "3 RAISONS" fades/scales in gently (0.9->1, power3) top-third, no star-burst/alarm decoration this time. Centered, ~30% of frame.
Scene 2 (1.3-3.2s): the line "POUR LESQUELLES ON NE TE PREND PAS AU SERIEUX SUR WHATSAPP" fades in line by line (2 lines), soft upward drift (12px), no hard card-pop. Centered, ~55% of frame.
Scene 3 (3.2-4.0s): held read, only a faint yellow underline-tick draws under "SERIEUX" as the sole added motion.

## Frame 2 — Raison 1

- scene: A phone screen mockup shows a WhatsApp-style status feed crammed with entries; the newest one gets lost in the pile
- duration: 5s
- transition_in: crossfade
- status: animated
- type: pain_point
- persuasion: naming a familiar frustration, plainly
- blueprint: device-surface-showcase (Adapt)
- assets: none — invented UI mockup (illustrates a generic problem, not a real account)
- src: compositions/frames/02-raison1.html
- voiceover: "Il y a trop de statuts. Le tien passe inapercu."

Adapt: keep the held-device-surface signature (a phone screen as the hero), but instead of a task flow, the "content" is a static status list that visually crowds itself as the line lands.

Scene 1 (0.0-1.2s): blue canvas wash; a phone-frame device mockup fades/scales up center (0.92->1), screen showing a chat-app status list header only ("Statuts"). Centered, phone ~55% of frame height.
Scene 2 (1.2-3.4s): as the line is "said", status entries stack in one by one (5-6 generic rows: circle avatar + name-bar + time-bar, no real content), each a quick fade+8px drop, filling the screen densely. Same centered phone frame.
Scene 3 (3.4-5.0s): the most recent (bottom) entry gets a faint highlight ring that fades out unanswered — visually "lost in the pile". Held on the crowded, static screen.

## Frame 3 — Raison 2

- scene: The same crowded status feed now shows a small "muted" indicator appearing on it, naming fatigue rather than invisibility
- duration: 5s
- transition_in: crossfade
- status: animated
- type: pain_point
- persuasion: naming a second, related frustration
- blueprint: device-surface-showcase (Adapt)
- assets: none — invented UI mockup
- src: compositions/frames/03-raison2.html
- voiceover: "Si tu postes trop, les gens se lassent - meme ceux qui aiment ce que tu vends."

Adapt: continue the exact same phone/status visual from Frame 2 (continuity, not a reset) - the delta is one small "muted" badge appearing, not a new busy build.

Scene 1 (0.0-1.6s): same crowded status screen holds (carried look from Frame 2, no rebuild). A small grey "muted" bell-badge fades in on one status ring, top-right of the list.
Scene 2 (1.6-3.6s): two more "muted" badges fade in on other rows, one at a time, paced to the line's two halves ("les gens se lassent" / "meme ceux qui aiment ce que tu vends").
Scene 3 (3.6-5.0s): held - the screen now reads as quietly ignored (several muted badges), no further motion.

## Frame 4 — Raison 3 (transition)

- scene: A split beat contrasts a fading, disappearing status against a steady browser window that simply stays put
- duration: 6s
- transition_in: crossfade
- status: animated
- type: reveal
- persuasion: contrast / setup for the pivot
- blueprint: comparison-split (Reproduce)
- assets: none — invented UI mockup (left side); a plain generic browser frame, no site content yet (right side)
- src: compositions/frames/04-raison3.html
- voiceover: "Un statut, ca dure 24h. Un site, on peut le voir quand on veut."

Scene 1 (0.0-2.2s): canvas splits pink/offwhite down the center as the line's first half lands; left pane holds the Frame 2-3 phone mockup (now shrunk, docked left), a circular countdown ring drains around it (24 -> 0), the phone fades to 20% opacity as the ring completes.
Scene 2 (2.2-4.6s): right pane fades/scales in a plain browser-chrome window (empty offwhite content area, no site yet) as the line's second half lands, mirrored tilt to the phone for book-open symmetry. Split-screen, ~50/50.
Scene 3 (4.6-6.0s): held - left phone fully faded (24h up), right browser window sits steady and un-faded, holding the contrast for the read.

## Frame 5 — Pivot + Preuve

- scene: The browser window from Frame 4 fills the canvas and becomes real - the two actual sites the user built land as proof
- duration: 6s
- transition_in: crossfade
- status: animated
- type: proof
- persuasion: the pivot statement, backed by real evidence (not a mockup)
- blueprint: device-surface-showcase (Reproduce)
- focal: nyara-site.jpg
- roles: nyara-site.jpg = cutout (hero, first proof) · aura-site.jpg = supporting (second proof, arrives just after)
- asset_candidates: assets/nyara-site.jpg — real screenshot of the NYARA fashion site, hero proof; assets/aura-site.jpg — real screenshot of the AURA skincare site, supporting proof
- src: compositions/frames/05-pivot-preuve.html
- voiceover: "Un site, c'est toujours la. Et ca fait plus serieux."

Reproduce: the empty browser window from Frame 4 is this shot's opening state (continuity), then fills with the real screenshot - the "held device, real content" signature.

Scene 1 (0.0-1.6s): the plain browser window (carried from Frame 4, now centered and enlarged, ~70% of frame) crossfades its empty content area into the real `nyara-site.jpg` screenshot as the line's first half ("un site, c'est toujours la") lands. Centered, hero, layered-depth (subtle drop shadow only, image already contains its own browser-chrome framing).
Scene 2 (1.6-3.4s): the nyara window settles fully; the green label-pill "TOUJOURS LA" scale-pops gently top-of-frame as a confirming beat.
Scene 3 (3.4-5.2s): `aura-site.jpg` slides/fades in from the right edge, docking as a smaller supporting card overlapping the nyara window's bottom-right corner (asymmetric 70/30, 2 depth layers) as "et ca fait plus serieux" lands.
Scene 4 (5.2-6.0s): held read on both real screenshots together - no further motion.

## Frame 6 — CTA (doux)

- scene: A calm closing line offers to show what the viewer's own site could look like - an invitation, not a demand
- duration: 5s
- transition_in: cut
- status: animated
- type: cta
- persuasion: soft single next step
- blueprint: kinetic-type-beats (Adapt)
- assets: none — typographic only
- src: compositions/frames/06-cta.html
- voiceover: "Envie de voir a quoi ressemblerait le tien ? Ecris SITE en message."

Adapt: same yellow bookend register as Frame 1 (series continuity with video 1's CTA color), but the button/action reads as an invitation, not a hard sell - smaller scale-in, no "hard shadow slam".

Scene 1 (0.0-1.6s): yellow canvas wash; the line "ENVIE DE VOIR A QUOI RESSEMBLERAIT LE TIEN ?" fades up (2 lines, soft drift), centered top-half.
Scene 2 (1.6-3.4s): a button-primary fades/scale-settles to center (0.94->1, power3, no bounce): "ECRIS 'SITE' EN MESSAGE".
Scene 3 (3.4-5.0s): held final read - button and question sit still; video ends on this frame.
