# Motion Personality — four archetypes + brand identity

Pick ONE archetype per project/brand, once, and apply it everywhere. Mixing archetypes within one product is the single most common cause of motion feeling "off-brand" even when no individual animation is bad.

## The four archetypes

### Precise
**Feel:** efficient, trustworthy, engineered, fast.
**Parameters:** short durations (100-200ms), minimal or zero overshoot, easing skews toward `ease-out`/`cubic-bezier(0.4, 0, 0.2, 1)`, straight-line motion over arcs, sharp not soft.
**Fits:** productivity tools, fintech, developer tools, utilities, dashboards.
**Signature move:** a settle with no bounce at all — it arrives and stops, like a well-made mechanism.
**Risk if overused:** can read as cold or robotic if never softened anywhere (e.g., a success state with zero warmth).

### Playful
**Feel:** friendly, energetic, approachable, a little silly.
**Parameters:** medium durations (200-350ms), visible overshoot (`back.out(1.7)`-ish, elastic on emphasis moments), arcs over straight lines for anything with "character," secondary bounce/wiggle details.
**Fits:** consumer social apps, kids' products, games, casual/youth-oriented brands.
**Signature move:** overshoot-and-settle — it goes past the target, then eases back, like it's a little excited.
**Risk if overused:** everything bouncing all the time reads as chaotic or unserious; reserve the biggest bounces for genuine delight moments (success, reward), keep routine interactions (tab switches, hovers) more restrained even within a Playful system.

### Elegant
**Feel:** premium, calm, considered, unhurried.
**Parameters:** longer durations (350-600ms) but ONLY for hero/emphasis moments — routine UI stays fast; very smooth easing (`cubic-bezier(0.16, 1, 0.3, 1)` "expo-out" family), near-zero overshoot but soft settling, generous use of fade alongside movement rather than movement alone.
**Fits:** luxury, editorial, portfolio, high-end hospitality/real estate, premium subscription products.
**Signature move:** a slow, silky ease with a fade — never a hard snap, never a bounce.
**Risk if overused:** slow durations on frequent/repeated interactions (hover, list scroll) make the product feel sluggish rather than premium — Elegant must still be fast where speed is functionally required.

### Bold
**Feel:** confident, loud, kinetic, attention-commanding.
**Parameters:** fast entrances with hard, high-contrast easing (`power4.out`, sharp wipes), strong exaggeration (principle #10), frequent use of scale/rotation for emphasis, hard-cut transitions (wipes, flashes) alongside eased ones, big typography moves.
**Fits:** short-form video/social content, sports, streetwear, hype-driven marketing, kinetic-typography brand systems (this is the register the Blockframe visual system in this repo's academy videos uses).
**Signature move:** a fast hard-wipe or snap-pop with a flash frame, immediately followed by a hold — energy up front, stillness to let it land.
**Risk if overused:** if EVERY beat is maximum intensity, nothing reads as the emphasis moment; Bold still needs quiet beats to make the loud beats land (see `narrative-structure.md`).

## Choosing an archetype

Ask: if this brand's motion were a person's body language, how would they move through a room? Precise = walks a direct line, no wasted motion. Playful = bounces a little with each step. Elegant = glides, unhurried. Bold = strides in fast and plants themselves.

If the product already has a visual identity (typography weight, color saturation, brand voice), the archetype should usually match: heavy display type + saturated color + punchy copy → Bold, not Elegant. Thin type + generous whitespace + restrained copy → Elegant, not Bold. A mismatch between visual identity and motion archetype is as jarring as a mismatch between logo and brand voice.

## Staying consistent without being monotonous

One archetype does not mean one animation. Within Bold, a routine tab-switch and a hero brand-reveal are both "Bold" but the hero moment pushes every parameter further (longer hold, harder wipe, bigger scale) while the routine interaction stays quick and restrained. The archetype sets the *character* of the easing/overshoot/hardness; the emotion and hierarchy (see `emotion-mapping.md`, `core-philosophy.md` Pillar 1) set how far to push it for a given moment.
