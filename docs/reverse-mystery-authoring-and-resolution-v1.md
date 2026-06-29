# Reverse Mystery Authoring and Resolution v1

## Purpose

This specification defines the authoring and validation rule that every AI_IF mystery must be built from canonical truth outward and must contain a complete final resolution before validation, playtesting, or human play.

The Game Master runs an authored mystery. It does not discover, decide, or complete the mystery during play.

## Reverse Mystery Authoring

Mysteries must be authored from canonical truth outward.

Before writing player-facing scenes, NPC dialogue, images, red herrings, or gameplay flow, the Story Author must define:

- what actually happened;
- who is responsible;
- why they did it;
- how they did it;
- when each key event occurred;
- what evidence the act created;
- how the player can discover and prove the truth.

Scenes, NPC answers, discovery rules, image opportunities, red herrings, case-board seed entries, and endgame flow must derive from that truth model.

The authoring sequence is:

1. Define the canonical truth.
2. Define the final resolution.
3. Define proof and accusation requirements.
4. Define clue creation and evidence provenance.
5. Define timeline and suspect clearance.
6. Define discovery paths and NPC knowledge.
7. Define scenes, images, red herrings, and gameplay flow.

Do not author a mystery forward from an intriguing scene and leave the solution to be completed later.

## Final Resolution Contract

Every mystery package must contain enough canonical material for the Game Master to explain the full solution without inventing anything.

The Final Resolution Contract must answer:

- culprit or responsible party;
- motive;
- method;
- opportunity;
- exact chronological timeline;
- required clues;
- supporting clues;
- red herrings and why they are false;
- innocent suspect clearance;
- proof chain;
- final accusation requirements;
- canonical endgame explanation;
- fallback solution reveal if gameplay stops early.

This material may live in `game-package.json`, a canonical `solution.md`, or another case handoff file only if `gm-readme.md` identifies that file as canonical.

## Fallback Solution Reveal

If the player stops a game early, pauses for debugging, asks to end the case, or asks out of game for the canonical answer, the Game Master must be able to provide the authored solution from package data.

The fallback reveal may contain spoilers, but it must not be improvised.

The fallback reveal should explain:

- what happened;
- who was responsible;
- why they acted;
- how they acted;
- what evidence proved it;
- what the key clues meant;
- why red herrings were false;
- how innocent suspects are cleared.

If the package does not contain this material, the Game Master should state out of game that the package is incomplete rather than inventing an ending.

## Validation Gate

Missing final-resolution material is a blocker.

## Required Final Proof Alignment

Reverse authoring must define:

- culprit;
- motive;
- method;
- opportunity;
- required proof;
- final accusation threshold;
- final reveal beats.

The required proof list must align with the final accusation discovery rule and Game Master reveal guidance.

A solution is not fair if the player can be declared correct before discovering the proof that the final reveal depends on.

Early correct guesses should remain theory checks until the authored proof threshold is met, the player asks to stop, or the player explicitly asks out of game for the canonical answer.

A case must fail validation if:

- the culprit or responsible party is undefined;
- motive is vague or insufficient;
- method is incomplete;
- opportunity is unsupported;
- timeline is missing or contradictory;
- proof chain is incomplete;
- red herrings are not explained;
- innocent suspects cannot be cleared;
- the Game Master cannot produce a canonical endgame explanation;
- no fallback solution reveal exists.

The Validator should confirm that the Game Master can explain the full canonical solution from package data alone.

## Runtime Rule

At runtime, the Game Master may reveal only the authored final resolution.

The Game Master must not invent missing solution material, final proof, clue meanings, red herring explanations, suspect clearance, or fallback reveal content.

If the player reaches the final accusation, the Game Master should evaluate the accusation against the authored proof threshold and then reveal the canonical endgame explanation when the threshold is met.

If the player asks out of game for the answer or asks to stop early, the Game Master should provide the authored fallback solution reveal.

## Relationship to Other Specifications

This contract works with:

- `docs/design-principles.md`, which defines fair-play mystery principles;
- `docs/runtime-engine-v2.md`, which governs Game Master behavior;
- `docs/runtime-fidelity-engine-v1.md`, which prevents runtime invention;
- `docs/discovery-rules-v1.md`, which defines how clues become player-visible;
- `docs/npc-interview-model-v1.md`, which bounds NPC knowledge;
- `docs/validator-diagnostics-v1.md`, which structures validation findings.

Runtime fidelity depends on authoring completeness. If the package lacks a complete final resolution, runtime cannot repair it.

## Suspect Deception in Reverse Authoring

Reverse authoring must define which suspect statements are true, false, incomplete, mistaken, or misleading before gameplay starts.

For each major suspect, define:

- what they claim;
- what actually happened;
- what they know;
- what they hide;
- why they hide it;
- how the player can expose or resolve the deception.

## Classic Whodunit Reverse Structure

For whodunits, reverse authoring must define:

- culprit;
- victim;
- motive;
- method;
- opportunity;
- alibi claims;
- alibi truths;
- physical proof;
- testimonial proof;
- red herrings;
- innocent clearances;
- final reconstruction.
