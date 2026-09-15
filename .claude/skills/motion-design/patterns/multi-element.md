# Multi-Element Patterns — stagger + choreography recipes

Concrete recipes implementing `director/choreography.md`'s principles. Numbers are starting points, adjust with the timing table (`reference/timing-easing-tables.md`) and the project's archetype.

## Linear stagger (list, one dimension)
**Shape:** N similar elements, one implied reading order (top-to-bottom or left-to-right).
**Recipe:** each item runs its own entrance pattern (`entrance-exit.md`) at `start_time = i * stagger_delay`, where `stagger_delay` is 40-80ms for compact lists (≤8 items) and compresses toward 25-40ms for longer lists to keep total spread reasonable.
**Cap:** total stagger spread should rarely exceed ~600-800ms even for long lists — past that, compress delay further or switch to batched-group stagger (below) rather than letting one linear stagger run for seconds.
**Direction:** should match the list's natural reading order; reversing it (bottom-to-top for a top-anchored list) needs a specific reason (e.g. content pushing up from a compose box) or it reads as a bug.

## Radial / outward stagger (grid or cluster reveal)
**Shape:** elements arranged around a center point or origin (a grid revealing from a triggering click point, a radial menu).
**Recipe:** stagger delay based on each element's distance from the origin rather than index order — `delay = distance_from_origin / wave_speed`. Produces a "ripple" read that feels physically motivated (Pillar 2) rather than arbitrary.
**Fits:** especially strong for Bold/Playful; feels like a deliberate physical wave. Use sparingly in Precise/Elegant contexts (it's an inherently expressive pattern).

## Batched-group stagger
**Shape:** many elements (12+), where item-by-item stagger would take too long in aggregate.
**Recipe:** split into groups of 3-5, stagger delay between groups (60-100ms), items within a group animate simultaneously or with a very tight inner stagger (15-20ms). Reads as "waves arriving" rather than "one item at a time," compresses total duration while still avoiding the flatness of everything appearing at once.

## Leader-follower
**Shape:** one element's motion causes or is closely coupled to another's (see `choreography.md`'s leader/follower concept).
**Recipe:** follower's animation starts at `leader_start + small_offset` (typically 15-30% of the leader's own duration) and often runs slightly longer than the leader so it visibly "catches up and settles after" (Disney #5, follow-through). Never start the follower before the leader, or the causal read inverts.

## Parent-child rigid group
**Shape:** elements that must read as one compound object (an icon+label pill, a card+shadow).
**Recipe:** animate the group's own wrapper transform as the single source of truth; children either inherit it directly (no separate animation) or get only a very small follow-through offset (a shadow lagging 30-50ms and easing slightly softer than the parent). Do NOT give children fully independent easing curves — that's what breaks the "one object" read.

## Crossfade handoff (A replaced by B in place)
**Shape:** one element is replaced by a different element in the same screen position (a play button becoming a pause button, a thumbnail becoming a full view).
**Recipe:** overlap the exit of A with the entrance of B rather than sequencing them (A fully exits, THEN B enters) — sequential handoffs at the same screen position create an empty-state flash that reads as a glitch. Overlap window: B starts at roughly 40-60% into A's exit.

## Scene-to-scene (full composition change)
**Shape:** an entire scene/frame is replaced by the next (relevant to this repo's HyperFrames video beats).
**Recipe:** outgoing scene's exit and incoming scene's entrance should either (a) overlap significantly via crossfade for a smooth/Elegant feel, or (b) use a hard, near-zero-overlap wipe/cut for Bold/kinetic pacing — the failure mode is landing in between, a slow sequential cut-then-fade that's too slow to feel punchy and too abrupt to feel smooth. Pick one register deliberately (ties back to `motion-personality.md`'s archetype) rather than drifting into the gap between them.

## Checklist before shipping a multi-element sequence

1. Stagger delay and direction chosen deliberately, not left at a framework default.
2. Total sequence duration checked against how long a viewer will actually tolerate watching it arrive.
3. Grouped elements share transform logic; independent elements don't fake being grouped.
4. Any causal (leader-follower) relationship reads as causal in the timing, not simultaneous or inverted.
