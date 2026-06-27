# Case Board v2

## Purpose

This document defines Case Board v2 for the AI Interactive Fiction project.

The case board is the player's structured memory of the investigation. It helps the Game Master track what the player knows, what has been inspected, what has been ruled out, and what remains open.

The case board should support play without becoming a spoiler device.

## Core principle

The case board records discovered or reasonably inferred information. It must not reveal hidden solution facts before the player earns them.

## Case board categories

Case Board v2 should support these categories:

```text
Known Facts
Evidence
Known NPCs
Suspects
Cleared Suspects
Locations
Visited Locations
Visible Objects
Inspected Objects
Ruled-Out Areas
Recovered Evidence
Images Seen
Open Questions
Working Theories
Timeline Notes
Pending Leads
Closed Leads
Contradictions
```

Quick Mysteries may use a smaller subset, but the structure should support these categories.

## Known facts

Known facts are established truths available to the player.

Examples:

- The object is missing.
- Only certain characters were present.
- A door was closed.
- A clock is visibly stopped.

Known facts may come from opening narration, NPC testimony, physical inspection, or discovered documents.

## Evidence

Evidence means discovered physical or documentary items.

Evidence entries should track:

- evidence ID;
- title;
- where it was found;
- whether it has been inspected;
- associated clues discovered so far;
- whether it is recovered or merely observed.

## Known NPCs

Known NPCs are characters the player has met or learned about.

Each entry may track:

- name;
- role;
- current location;
- attitude;
- known claims;
- known contradictions;
- whether questioned.

## Suspects

Suspects are NPCs or entities that remain possible responsible parties.

A suspect entry may include:

- apparent motive;
- apparent opportunity;
- evidence for;
- evidence against;
- alibi claim;
- unresolved questions.

## Cleared suspects

A cleared suspect is someone the player has enough evidence to deprioritize.

Clearing may be partial.

Example:

```text
Celia appears less likely because her suspicious envelope has an innocent explanation, but she remains present until the final proof chain is complete.
```

The Game Master should avoid over-clearing too early.

## Locations and visited locations

The case board should distinguish:

- known locations;
- visited locations;
- unavailable locations;
- ruled-out locations.

For a Quick Mystery, there may be only one location, but that location can contain multiple visible areas and objects.

## Visible objects

Visible objects are plainly observable but not yet inspected.

Examples:

- desk;
- mantle;
- window;
- fireplace;
- clock;
- display case;
- tea trolley.

Visible object tracking lets the Game Master answer:

```text
What have I not examined yet?
```

## Inspected objects

Inspected objects are things the player has examined closely.

The case board should record:

- object name;
- inspection depth;
- result;
- clues found;
- whether nothing significant was found;
- whether a closer inspection remains possible.

Example:

```text
Desk — inspected. No direct evidence found. Ruled out as obvious hiding place.
```

## Ruled-out areas

Negative findings belong here.

Examples:

- window shows no entry signs;
- fireplace contains no hidden object;
- mantel items appear undisturbed;
- door shows no forced entry.

Ruled-out areas are useful because they prevent repetition and support player confidence.

## Recovered evidence

Recovered evidence means the player now possesses or has exposed the evidence.

This differs from observed evidence.

Example:

```text
Observed: a closed envelope.
Recovered/Read: the contents of the envelope.
```

## Images seen

Track image assets shown to the player.

Fields may include:

- asset ID;
- label;
- image class;
- when shown;
- whether it was scene, inspection, or evidence;
- text fallback used.

Images seen should not create new clues unless those clues are also in text.

## Open questions

Open questions are unresolved investigative questions.

Examples:

- How was the object removed?
- Who had motive?
- Which clue is misleading?
- Why did an object behave unusually?

Open questions should update as the player discovers information.

## Working theories

Working theories are player-proposed explanations.

The Game Master may track them but should not confirm or deny hidden truth prematurely.

A theory may be:

- unsupported;
- partially supported;
- contradicted;
- near-correct;
- solved.

## Timeline notes

Timeline notes organize chronology as discovered by the player.

They should include:

- player-known times;
- claimed movements;
- contradictions;
- established sequence.

They should not expose hidden true timeline events until earned.

## Pending leads

Pending leads are suggested next investigative actions.

Examples:

- inspect the case more closely;
- question a suspect about a contradiction;
- compare two traces;
- review the clock;
- ask for a case board summary.

Hints can draw from pending leads.

## Closed leads

Closed leads are examined paths with no further immediate value.

Examples:

```text
Window checked: no sign of entry.
Mantle checked: no direct evidence.
Envelope explained: red herring resolved.
```

Closed leads should not disappear from memory.

## Contradictions

Contradictions are mismatches between:

- testimony and physical evidence;
- one NPC statement and another;
- claimed timeline and discovered chronology;
- object state and explanation.

Contradictions should be preserved because they often drive deduction.

## Case board update triggers

The Game Master should update the case board when:

- a clue is discovered;
- evidence is recovered;
- an object is inspected;
- an area is ruled out;
- an NPC is questioned;
- a contradiction emerges;
- a theory is proposed;
- an image is shown;
- a lead is closed;
- a final accusation is made.

## Summary modes

The Game Master should provide case board summaries in several depths.

### Brief summary

Use during active play.

```text
Known facts, current suspects, open leads.
```

### Full summary

Use when requested.

```text
Facts, evidence, suspects, inspected objects, open questions, pending leads.
```

### Accusation readiness summary

Use before or during final accusation.

```text
What you can prove, what you suspect, what remains unproven.
```

## Spoiler safety

The case board must never list hidden solution facts as if known.

If the player has not discovered a clue, it should not appear as discovered.

If the player has seen an object but not understood it, record it as observed, not interpreted.

## Runtime state relationship

The case board is part of runtime state, not canonical truth.

Canonical truth is stored in the game package.

The case board stores the player's known state.

## Validator implications

The Validator should check that the package provides enough data to support case board updates:

- opening facts;
- known characters;
- known locations;
- discovery rules;
- evidence IDs;
- clue IDs;
- asset IDs;
- validation targets.

## Game Master implications

The Game Master should not wait for the player to request every update.

Major discoveries should trigger concise case board updates or offer them.

For short mysteries, case board summaries can be lightweight.

For larger mysteries, case board discipline becomes essential.

## Failure conditions

The case board fails if it:

- reveals hidden facts;
- loses discovered clues;
- forgets inspected objects;
- omits negative findings;
- marks a suspect cleared too early;
- treats seen images as independent evidence;
- contradicts the canonical package.
