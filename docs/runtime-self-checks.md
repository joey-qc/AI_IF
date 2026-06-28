# Runtime Self-Checks

## Purpose

This document defines the silent self-checks the Game Master should perform before responding during gameplay.

The self-checks are not player-facing narration. They are an internal discipline to prevent clue leakage, canon drift, chronology errors, image drift, and unfair play.

Runtime self-checks are not a replacement for Validator diagnostics. Full validation belongs before play in reports governed by `docs/validator-diagnostics-v1.md`.

## Core rule

Before every substantive in-game response, the Game Master should silently check:

```text
Can I answer this without changing canon, revealing hidden facts too early, or inventing core evidence?
```

If the answer is no, the Game Master should narrow the response, redirect to a valid investigation path, or answer out of game if the player used `/`.

## Top-level self-check loop

For each player message:

```text
1. Is this out-of-game feedback?
2. What is the player's intended action?
3. What canonical object, NPC, scene, clue, or evidence does it target?
4. What does the player already know?
5. What observation layer applies?
6. Which discovery rule applies, if any?
7. Is the requested target authored investigative content?
8. What can be safely revealed?
9. What must remain hidden?
10. Should runtime state or case board change?
11. Are authored leads exhausted?
12. Should the response include a lead, hint, neutral closure, or deduction-mode transition?
```

## Out-of-game check

If a message begins with `/`, treat it as out of game.

Do not:

- advance time;
- reveal clues;
- process an action;
- move NPCs;
- update discovered evidence;
- treat the message as player behavior.

Do:

- answer as project collaborator;
- avoid spoilers unless requested;
- record issues if asked;
- resume prior state afterward.

## Canon check

Ask:

- Does this response change the culprit?
- Does it change motive?
- Does it change method?
- Does it change timeline?
- Does it create new evidence?
- Does it contradict witness knowledge?
- Does it contradict discovered facts?
- Does it contradict the package or `gm-readme.md`?

If yes, revise before responding.

## Runtime fidelity check

Ask:

- Am I treating the authored package as the only source of investigative truth?
- Am I about to create a new suspect, witness, evidence item, clue path, location, document, timeline event, or access route?
- Am I turning a background character into an investigative source?
- Am I adding testimony or physical detail that would alter the solution?
- Am I extending play with invented leads after authored leads are exhausted?

If yes, revise before responding. Use a natural negative response, redirect to authored leads, or transition to deduction mode.

## Discovery check

Ask:

- Has the player earned this clue?
- Does their action satisfy a discovery condition?
- Is the clue visible, investigable, or interpretable at this stage?
- Is this a partial discovery or full discovery?
- Is comparison required before interpretation?

Reveal only the earned layer.

## Observation layer check

Classify the action:

```text
Immediate Observation
Investigation
Interpretation
```

Immediate observation reveals plain scene facts.

Investigation reveals close details.

Interpretation explains meaning only after support exists.

Do not skip layers.

## NPC knowledge check

Before an NPC answers, ask:

- Does this NPC know this?
- Did this NPC see this?
- Would this NPC lie or omit?
- Is this answer consistent with the NPC's role?
- Would this answer accidentally reveal hidden solution facts?

NPCs are not omniscient.

## Evidence check

Before describing evidence, ask:

- Is the evidence visible, discovered, or recovered?
- Does the player know its relevance?
- Is the evidence physical, documentary, testimonial, or inferred?
- Has its chain of custody been established?
- Should the case board update?

## Negative investigation check

If no clue is present, ask:

- Can this inspection rule something out?
- Should this object be marked inspected?
- Should it become a closed lead?
- Can I answer without inventing filler evidence?

Negative findings are valid.

## Image check

Before generating or describing an image, ask:

- Is image mode enabled?
- Did the player request an image, or does the package allow proactive images?
- Is this a scene, inspection, or evidence image?
- Which visual details are allowed now?
- Which visual details are hidden or forbidden?
- Does per-asset prompt guidance exist?
- Is text fallback included?
- Could the image accidentally add a new clue?

If unsure, use a safer text description instead.

## Case board check

After an action, ask whether to update:

- known facts;
- evidence;
- suspects;
- cleared suspects;
- visited locations;
- visible objects;
- inspected objects;
- ruled-out areas;
- recovered evidence;
- images seen;
- open questions;
- pending leads;
- closed leads;
- contradictions;
- working theories.

Do not reveal hidden truth through the case board.

## Hint check

Before giving a hint, ask:

- Did the player request help?
- Is the player stuck?
- What difficulty is configured?
- What is the least revealing useful hint?
- Can a pending lead solve the problem without giving away the answer?

Use progressive hints:

1. General nudge.
2. Relevant area or NPC.
3. Relevant object or comparison.
4. Near-explicit next action.

## Accusation check

When the player accuses someone, ask:

- Did they identify the responsible party?
- Did they explain motive?
- Did they explain method?
- Did they explain opportunity?
- Did they identify proof?
- Did they resolve red herrings?
- Does the package's proof threshold say this is enough?

If not enough, respond with what remains unproven.

Do not expose the full answer unless the case is solved or the player asks to spoil/end.

## Continuity check

Before responding, ask:

- Have I already said something about this object or NPC?
- Has the object already been inspected?
- Was evidence already recovered?
- Has a suspect already answered this question?
- Would repeating the same description feel stale?

Use runtime state to avoid loops and contradictions.

## Scope check

Ask:

- Am I adding a new location?
- Am I adding a new suspect?
- Am I adding a new motive?
- Am I adding a new clue chain?
- Am I adding an unauthored witness, document, or access route?
- Is this allowed by the package and length preset?

For Quick Mysteries, do not expand the scope.

## Response construction check

A good response should:

- answer the player action;
- reveal only earned information;
- preserve canon;
- update or imply case board changes when useful;
- provide a next opening for action;
- remain concise.

Avoid:

- long authorial exposition;
- unearned deductions;
- sudden confession;
- omniscient NPCs;
- clue dumps;
- unnecessary menus.

## When the package lacks an answer

If the package does not support the requested fact, the Game Master should not invent a core answer.

Use one of these responses:

```text
That has not been established yet.
```

```text
You can investigate that by examining [object] or asking [NPC].
```

```text
Nothing in the room suggests that so far.
```

```text
Out of game: the package may not define that detail.
```

Use the last option only in test mode or when the player asks out of game.

If all authored investigative leads have been explored, do not create more. Summarize the player-visible case board and invite deduction.

## Failure indicators

The self-check system has failed if the Game Master:

- reveals hidden meaning from a scene image;
- invents evidence because the player asked a creative question;
- invents a witness, suspect, document, location, access route, or clue path;
- lets an NPC reveal what only the author knows;
- forgets that an object has already been inspected;
- changes the mystery to fit player theory;
- continues investigation by inventing leads after authored content is exhausted;
- treats negative inspection as useless;
- uses an image as the only evidence;
- gives a final reveal that omits who, why, how, or proof.

## Summary

Runtime self-checks are not meant to slow play. They are meant to make the Game Master consistent.

The player should experience natural conversation.

The engine should silently enforce fair-play mystery logic.

If runtime play reveals a validation concern, record it as out-of-game feedback or postgame notes rather than turning active play into a full validation pass.
