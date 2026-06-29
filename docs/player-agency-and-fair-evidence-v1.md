# Player Agency and Fair Evidence v1

## Purpose

Player Agency and Fair Evidence v1 defines how AI_IF protects fair-play investigation during runtime.

The Game Master must reveal stable observable evidence when the player fairly examines available objects, while leaving interpretation and final synthesis to the player until the correct mode or request.

This contract works with:

```text
docs/runtime-fidelity-engine-v1.md
docs/discovery-rules-v1.md
docs/human-engagement-and-playability-v1.md
docs/image-fidelity-contract-v1.md
docs/case-board-current-v1.md
```

## Stable Evidence Rule

When the player closely examines an available object, location feature, document, or piece of evidence, the Game Master should reveal all ordinary observable sensory details available at that time.

Ordinary observable details include:

- marks;
- stains;
- smells;
- missing parts;
- unusual placement;
- texture;
- damage;
- labels;
- ordinary contents;
- immediate physical oddities.

The Game Master must not hide observable physical evidence merely because the player has not yet discovered the explanatory fact.

The meaning of an observation may change later. The observation itself should not appear retroactively as if it was invisible during fair inspection.

New details may appear later only when the player gains a fair new basis for observing them, such as:

- opening the object;
- changing lighting;
- using a tool;
- gaining permission or physical access;
- moving the object;
- inspecting a specific subpart;
- learning from another clue where to look.

## Observation vs Interpretation

The engine separates:

- observation;
- witness claim;
- document statement;
- possible meaning;
- final proof synthesis.

Observations, witness claims, and document statements should be revealed when the player discovers them.

Interpretation should wait until:

- the player proposes it;
- the player asks for a hint;
- the player requests a theory check;
- deduction mode begins;
- the package explicitly permits the interpretation at that point.

Final proof synthesis belongs to final accusation handling, deduction support, or the authored final reveal.

## Discovery Prerequisite vs Interpretation Prerequisite

Discovery prerequisites may restrict when evidence is visible only when they change:

- physical access;
- permission;
- available tools;
- lighting;
- inspection method;
- available testimony.

Do not use a prerequisite merely to suppress an observable fact.

If an object is physically available and the player closely inspects it, ordinary observable details should be revealed even when their significance remains unclear.

Use later prerequisites for interpretation, comparison, theory checks, or proof synthesis rather than making stable evidence appear late without a physical reason.

## Neutral Case Board

Case-board updates summarize directly discovered facts. They must not convert facts into implied theories or lead the player toward a specific method, motive, culprit, or investigative direction unless the player requested a hint, theory check, or deduction support.

Avoid leading language such as:

```text
Was something added?
Who tampered with it?
Did the killer use this?
This suggests...
This points to...
The likely explanation is...
```

Prefer neutral labels and wording:

```text
Known fact
Known claim
Known evidence
Unresolved significance
```

Use `Unresolved significance` instead of `Open question` when question wording would imply a theory the player has not raised.

## Player Inference Protection

The Game Master may identify that something is:

- unusual;
- inconsistent;
- unexplained;
- unresolved.

The Game Master must not explain the deduction category or investigative implication unless the player asks for interpretation, a hint, a theory check, or deduction help.

Let the player ask the deductive question.

## No Inference in Spatial Summaries

Spatial summaries should describe seating, layout, movement, object placement, and physical relationships neutrally.

Do not imply access, opportunity, tampering, or culprit advantage unless:

- the player asks for analysis;
- the connection has already been established through discovered facts;
- deduction mode has begun.

Good:

```text
Julian's seat was nearest the path to the sideboard.
```

Too leading:

```text
Julian was best positioned to tamper with the glass.
```

## Runtime Mode Distinction

### Investigation Mode

Reveal player-visible facts only. Do not add interpretation, covert hints, or leading case-board summaries.

### Hint Mode

Use only when requested or when the case's hint policy allows an offered hint. Hints should be gradual, bounded, and tied to authored content.

### Theory-Check Mode

Activate when the player proposes a theory. The Game Master may say what fits, what is missing, and what contradicts the theory based only on discovered player-visible facts and authored proof rules.

### Deduction Mode

Use when authored leads are exhausted or the player asks to solve. Organize known facts without revealing hidden solution facts. Invite the player to form or refine suspect, motive, method, opportunity, and proof.

### Final Solution Mode

Use only when the proof threshold is met, the player asks to end, or the player asks out of game for the canonical answer. The final solution must come from authored package data.

## Image Fidelity Addendum

Scene images should preserve canonically present people, objects, and spatial relationships unless the player explicitly requests an allowed empty-room, symbolic, close-up, or mood-only image.

Images must not:

- omit canonically present major NPCs from full-room scene images without an authored or requested reason;
- add extra people;
- add hidden clues;
- add noncanonical objects;
- show culprit action;
- reveal hidden facts;
- contradict text canon.

Future packages should specify image-participant and visibility metadata where images are enabled:

- required visible people;
- required absent people;
- required objects;
- forbidden objects;
- image type, such as `full_room`, `close_up`, `symbolic`, or `empty_room`;
- whether people are included.

Text remains authoritative if an image conflicts with the canonical package or player-visible runtime state.

## Role Responsibilities

### Story Author

Author clue text so observations, claims, document facts, interpretations, and final synthesis are clearly distinguishable. Ensure ordinary observable evidence is stable on fair inspection.

### Validator

Check that discovery rules do not hide observable facts behind interpretation prerequisites, that case-board language is neutral, and that image definitions preserve canonically present people and objects.

### AI Playtester

Stress-test whether gameplay delays physical evidence unfairly, steers through summaries or open questions, or implies deductions through spatial descriptions.

### Revision Engine

Repair packages that hide observable evidence without a physical reason, blur observation and interpretation, or use leading summaries that imply method, motive, culprit, or direction.

### Game Master

Reveal stable observations on fair inspection, keep interpretation mode-bound, use neutral case-board language, avoid covert hints, and let the player make deductions.
