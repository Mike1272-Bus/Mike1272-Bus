# Entrance / Exit Patterns

Recipes for how elements should appear and disappear. Each recipe names: when to use it, the parameter shape, and the archetype it fits best. Numbers are starting points — pull exact values from `reference/timing-easing-tables.md` and adjust per `emotion-mapping.md`.

## Fade
**What:** opacity 0 → 1 (in) or 1 → 0 (out), nothing else moves.
**Use when:** the element's position is already "correct" and doesn't need to travel — it's just becoming present/absent. Also the default reduced-motion substitute for anything spatial (`context-adaptation.md`).
**Fits:** all archetypes; the most neutral, lowest-commitment entrance.
**Watch out:** fade alone on something that visually "should" have arrived from somewhere (an off-canvas panel) feels incomplete — pair with a small translate (see Slide-fade below) unless deliberately going for the calmest possible treatment (Elegant).

## Slide (translate) + fade
**What:** translate from an offset position to resting position (typically 16-40px offset, never further unless it's a deliberate large-scale entrance) combined with a fade.
**Use when:** the element has an implied origin (slides up from below its trigger, slides in from the edge it's associated with).
**Fits:** all archetypes — Precise keeps the offset small and fast, Playful/Bold can offset further and add overshoot, Elegant keeps it slow and soft.
**Watch out:** exit should not be the exact time-reverse of entrance — exits are typically faster (viewer's attention has already moved on) and ease-in rather than ease-out (see `reference/timing-easing-tables.md`).

## Scale-pop
**What:** scale from ~0.7-0.9 to 1.0, usually combined with fade, often with overshoot (scale briefly to 1.03-1.08 before settling to 1.0).
**Use when:** the element "arrives" rather than "slides in" — modals, badges, popovers, anything that should feel like it materializes at its own location rather than traveling from elsewhere.
**Fits:** Playful and Bold love the overshoot version; Precise uses scale-pop with zero overshoot (settles exactly at 1.0); Elegant rarely uses scale-pop at all, preferring fade or slow slide.
**Watch out:** scaling from too small a starting value (below ~0.6) reads as "popping into existence" rather than "growing into place," which can feel jarring — reserve very small starting scales for deliberately dramatic reveals.

## Wipe reveal
**What:** a hard-edged shape (usually a solid color bar) covers the element, then the bar moves away revealing the content underneath, OR a clip-path/mask reveals the content edge-to-edge.
**Use when:** a punchy, graphic, non-physics-feeling transition is wanted — this is the one entrance pattern that deliberately breaks Pillar 2 (physics) by design, in service of Bold personality and hard-cut energy.
**Fits:** Bold almost exclusively; wrong for Elegant (too hard), usually wrong for Precise (too showy for utility contexts) unless it's a very fast, minimal version.
**Watch out:** the wipe itself should be genuinely fast (80-150ms) — a slow wipe loses the "hard cut" energy that's the entire point of the pattern and just becomes a slow slide with extra steps.

## Morph / shape transform
**What:** one shape's geometry (border-radius, path, size) animates into a different shape rather than the element disappearing and a new one appearing.
**Use when:** communicating continuity (Pillar 1) — this used-to-be-that-thing, transformed. A thumbnail becoming a full detail view; an icon becoming a different icon representing a state change.
**Fits:** all archetypes, but the easing/duration texture changes a lot — Precise morphs fast and directly, Elegant morphs slow and smooth, Bold morphs fast with hard, high-contrast intermediate shapes.
**Watch out:** test the midpoint frame (Disney #11, Solid Drawing) — some shape interpolations look broken or meaningless halfway through; if so, either pick a different pair of shapes or hide the transition with an opacity cross-fade timed to the least-legible part of the morph.

## Staggered reveal (list/grid entrance)
**What:** multiple similar elements each running one of the above patterns, offset in time. See `multi-element.md` for the stagger mechanics; this entry is about which base pattern to stagger.
**Use when:** a list, grid, or gallery of similar items is appearing together.
**Fits:** scale-pop and slide-fade stagger well across all archetypes; wipe-reveal staggered across many items usually reads as chaotic past 3-4 items (too many hard edges competing) — reserve wipe for single hero elements.

## General exit guidance

Exits deserve deliberately less design attention than entrances (the viewer's focus has already moved on, or is about to), but they still need SOME shape — an instant `display: none` with zero transition reads as broken/buggy, not intentional. Minimum viable exit: a fast fade (100-150ms) even when nothing else about the exit is elaborate.
