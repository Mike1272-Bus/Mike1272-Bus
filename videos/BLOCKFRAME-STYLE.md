# Blockframe Motion — style guide (Michaelson Digital Academy / DigitalMikaelson)

Reference notes for every new HyperFrames video project in this repo. Read this
before authoring a new composition's CSS so generated motion-design elements
stay consistent and legible across episodes.

## Brand

- Name: **DigitalMikaelson** (one word).
- Series: Michaelson Digital Academy, pilier "Produits Digitaux".
- Framework introduced Épisode 2: **VENDRE** — Visibilité, Engagement,
  Notoriété, Distribution, Relance, Évolution. One episode per letter,
  starting with "V" (Épisode 2).

## Palette & type

- `--yellow: #F7CB46` `--ink: #0A0A05` `--cream: #FFFDF5`
- Display: "Archivo Black" (headlines, badges). Body/labels: "Work Sans".
- Real footage: `.shot-card.landscape` (1000×563, 7px ink border, hard
  12px offset shadow, no blur) or `.shot-card.portrait-fit` for
  portrait-native images (poster/cover graphics) — never force-crop a
  portrait source into the landscape box.

## Sizing — generated motion-design elements (2026-09-16 correction)

**User feedback: generated icons/shapes read too small on a phone screen in
academy-00/01. Scale up every hand-built motion-design element in new
builds** (not just text) — target roughly 30-40% larger than the
academy-00/01 baseline:

| Element | Old baseline | New target |
|---|---|---|
| `.fx-title` | 68px | 84-96px |
| `.fx-eyebrow` | 24px / 10×24 padding | 30-32px / 14×28 padding |
| `.fx-bulb .glass` | 190px | 250-260px |
| `.fx-box` (package) | 210px | 270-280px |
| `.fx-phone` | 160×300 | 210×390 |
| `.fx-bill` | 190×108 | 250-260×140-150 |
| `.fx-coin` | 54px | 72-74px |
| `.fx-notif-card` icon | 74px | 92-96px |
| `.fx-notif-card` text | 32px | 36-38px |
| `.fx-step` circle | 92px | 116-120px |
| `.fx-day` (calendar) | 108×132 | 138-140×168-170 |
| `.cta-badge` / subscribe button text | 76px / 54px | 88-96px |

Keep `.pd-grid` mosaic tiles close to the existing 490×560 (a 2×2 grid
already fills the frame; growing it risks overlap) — legibility there comes
from the photo itself, not the frame size.

Apply this sizing from Épisode 2 onward. Episode 1 / academy-01-partie2 are
not being retroactively re-rendered for this — ask before touching finished,
already-shared episodes.

## Real logos over generic badges (2026-09-16)

User confirmed: use real, official brand logos (own brand + third-party
platforms named on screen) instead of generic icon/text badges, wherever a
named brand appears in the script. Source real logo files from the user's
asset dropbox (`main` branch) or ask the user to send them directly — do not
hand-redraw a trademarked mark. `.fx-logo-badge` (168px, 30px radius, 6px ink
border, 8px offset shadow) is the standard frame for a third-party platform
logo; `.fx-identity-badge` (260px circle) is the standard frame for the
DigitalMikaelson mark.

## Script angle — contrarian, not consensus (2026-09-17)

**Standing direction for every future script, starting Épisode 3:** don't
restate classic digital-marketing advice everyone already knows (e.g. "crée
un bon produit, fais du contenu, construis une audience, et vends"). Instead,
name that classic belief explicitly, then go against it — show why the
common order/assumption is wrong or incomplete, using a concrete case
(Oncle David) as proof, not another generic tip list. Each script should
pick one specific belief tied to that episode's VENDRE letter and flip it,
rather than layering three "leviers" that read like a checklist. This is a
durable editorial rule — apply it by default, no need to re-ask each time.

## CTA "Abonne-toi" — standard, permanent pattern (2026-09-16)

**Do not ask again — use this on every future episode by default:**
a pill-shaped yellow button reading "ABONNE-TOI" pops in
(`elastic.out(1,0.6)`), then a hand/pointer emoji cursor (`.fx-cursor-hand`)
slides in from the bottom-right corner of the button and "clicks" it (a quick
scale-bounce on the cursor + a `.fx-click-ring` burst expanding from the
click point + the button itself does a small squash-bounce), timed with the
synthesized click SFX (`audio/sfx/click.wav`). Reuse the exact mechanism from
academy-01-partie2 / academy-02's beat 10 (`.fx-subscribe-btn`,
`.fx-cursor-hand`, `.fx-click-ring`) verbatim — only the surrounding text/
timing changes per episode.
