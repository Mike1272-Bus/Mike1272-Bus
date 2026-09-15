# Ambient / Continuous Patterns — loops, breathing, parallax

Motion that runs without user input, often indefinitely. The design problem is different from discrete entrance/exit/feedback motion: it has to be sustainable to look at for an unbounded amount of time, which means lower amplitude and stricter loop-seamlessness than almost any other category.

## Core rule: subtlety scales inversely with duration-on-screen

A one-shot 400ms animation can be bold. An ambient loop the viewer might look at for 30 seconds needs to be dramatically more restrained than intuition suggests — what looks "too subtle to bother with" in an isolated preview is usually correct once it's actually looping in context. If an ambient effect is noticeable enough to *name* after a few seconds of looking at it, it's very likely too strong.

## Breathing / idle pulse
**What:** a slow, low-amplitude scale or opacity oscillation (e.g. scale 1.0 ↔ 1.02, or opacity 0.9 ↔ 1.0), signaling "this is alive/active/waiting" without demanding attention.
**Use when:** indicating an idle-but-active state (a waiting call-to-action, a live indicator, an element inviting interaction without being urgent about it).
**Parameters:** long period (2-4s per full cycle), smooth sine-like easing (`ease-in-out`, never a sharp curve — sharp easing on a loop reads as mechanical ticking rather than breathing), never full-stop at either extreme (should feel continuous, not like two snapped poses).
**Watch out:** never breathe more than one element in a given view unless they're explicitly meant to feel connected — multiple independent breathing elements at different phases reads as visual static.

## Looping micro-animation
**What:** a short (1-3s) animation that repeats seamlessly — a subtle icon animation, a looping illustration detail.
**Parameters:** the hard requirement is a **seamless loop point** — the last frame's velocity/position must match the first frame's, or the seam reads as a stutter every cycle, which is far more distracting over a loop than a single hard cut would be once. Test by watching 3+ consecutive loops, not one.
**Watch out:** looping motion placed anywhere near a focused task (a text input, a reading area) actively competes for attention and measurably hurts task completion — see `context-adaptation.md`'s focus/concentration row. Ambient motion belongs in peripheral, decorative, or explicitly-idle contexts only.

## Parallax
**What:** background/foreground layers moving at different rates relative to a scroll or pointer position, creating a sense of depth.
**Parameters:** keep the rate differential moderate (background at 30-60% of foreground's rate is usually enough to read as depth; larger differentials start to feel like a gimmick or, worse, nauseating). Background layers should generally move *slower* than foreground, matching real-world depth-of-field intuition (Pillar 2, physics).
**Watch out:** this is one of the two ambient patterns (with autoplay carousels) most likely to trigger vestibular discomfort — always provide the reduced-motion fallback from `context-adaptation.md`, and never make parallax the *only* way information is conveyed (it should be a texture, never load-bearing for comprehension).

## Auto-advancing / autoplay content (carousels, rotating banners)
**What:** content that changes on a timer without user input.
**Parameters:** if used at all, the transition itself should follow the relevant entrance/exit pattern (`entrance-exit.md`) — but seriously reconsider the pattern itself first: autoplaying rotation is one of the most consistently disliked ambient patterns in usability research, because it removes viewer control over reading pace and frequently changes content exactly when the viewer was about to read it.
**Watch out:** if autoplay is genuinely required (a lot of business contexts demand it), always pause on hover/focus and provide manual controls — non-negotiable both for accessibility and for basic respect of reading speed.

## For pre-rendered video (this repo's context)

"Ambient" in a fixed-duration video (not a live loop) usually means: does the background have any subtle drift, or does a decorative element idle-pulse behind the main content while VO plays over it? Same amplitude rule applies — a background element that's more active than the foreground content it's supporting is a staging failure (Disney #3), not an ambient enhancement. When this repo's compositions include persistent background layers (grids, gradients), the default should be near-static — reserve any drift for a specific reason, not as a default "make it feel alive" reflex, which more often just competes with the actual content.
