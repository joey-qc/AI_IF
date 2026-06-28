# Case Board Current v1

## Purpose

Case Board Current v1 defines the structured format for:

```text
games/<case-folder>/case-board-current.json
```

This file is the player's current visible investigation board during active play.

It is runtime, player-facing state. It is not canonical mystery truth.

The machine-readable contract is:

```text
schemas/case-board-current.schema.json
```

## Core rule

The case board must contain only information available to the player.

It must never reveal undiscovered solution facts, hidden culprit knowledge, true motive, undiscovered clue meanings, secret timeline events, or final proof before the player earns them.

## Relationship to canonical truth

`game-package.json` records what is true in the authored mystery.

`case-board-current.json` records what the player currently knows, has seen, has recovered, has questioned, has ruled out, or is theorizing.

The case board may reference canonical IDs from the package, including:

```text
clueId
npcId
locationId
objectId
evidenceId
imageId
```

Those references are internal anchors only. The board text must still be player-safe.

When the package defines `canonicalAssetInventory`, board entries may reference only player-visible information derived from canonical assets, authored discovery rules, permitted negative investigation, or player theories.

Do not copy hidden solution explanations from `game-package.json` into the current case board unless the player has discovered them.

## Relationship to runtime-state.json

`runtime-state.json` tracks broader gameplay and session state:

- session status;
- current scene or location;
- turn count;
- NPC conversation state;
- hints;
- accusation state;
- image requests;
- out-of-game notes;
- compact case-board continuity.

`case-board-current.json` is the player-facing investigation board. It is more structured and readable than the compact `caseBoardSummary` inside runtime state.

The two files may overlap, but they have different jobs. Runtime state helps the Game Master operate. The current case board helps the player resume and reason.

## Relationship to case-board-seed.json

`case-board-seed.json` is the initial visible board at the start of play.

It may include opening facts, initially known NPCs, known locations, visible objects, and starting questions or leads.

`case-board-current.json` begins from the seed and evolves during runtime.

If no current board exists when gameplay starts, the Game Master should initialize one from `case-board-seed.json` or from the package's embedded `caseBoardSeed`.

If a current board exists when resuming play, the Game Master should read it before responding.

## Required sections

Case Board Current v1 supports these top-level sections:

```text
metadata
knownFacts
evidence
knownNPCs
suspects
clearedSuspects
locations
visitedLocations
visibleObjects
inspectedObjects
ruledOutAreas
recoveredEvidence
imagesSeen
openQuestions
workingTheories
timelineNotes
pendingLeads
closedLeads
contradictions
```

Each section should use structured objects with stable board IDs and canonical references where useful.

Loose strings are acceptable only inside fields such as summaries, notes, or player-visible evidence lists.

## Evidence and interpretation

The board should distinguish discovered evidence from interpreted theory.

Example distinction:

```text
Evidence: "A torn receipt was found in the desk."
Theory: "The receipt may connect the desk to the missing object."
```

Do not mark evidence as interpreted until the player has enough support to understand what it means.

## Leads and ruled-out paths

The board should distinguish:

- pending leads;
- closed leads;
- ruled-out areas;
- cleared or deprioritized suspects.

Negative investigation results belong on the board when they help continuity.

Examples:

```text
Window checked: no visible sign of forced entry.
Fireplace inspected: no hidden object found.
```

These entries should not invent new clues. They record what the player has reasonably ruled out.

The board must not add invented investigative assets. A background character, descriptive object, incidental document, flavor prop, or image request may appear only as a negative or atmospheric note unless it maps to an authored canonical ID.

## Uncertainty and theories

Uncertainty should be explicit.

Working theories may be marked as:

```text
unsupported
partially_supported
contradicted
near_correct
resolved
abandoned
```

The Game Master should not confirm hidden truth through theory status. A theory can be described as supported by known evidence without saying whether it is secretly correct.

## Contradictions

Contradictions record mismatches the player has discovered, such as:

- testimony versus physical evidence;
- one NPC statement versus another;
- a claimed timeline versus a discovered timeline note;
- an object state versus an explanation.

Contradictions should include only the player-visible mismatch and the current status:

```text
noticed
investigating
explained
unresolved
```

Do not include the hidden explanation until the player earns it.

## NPC answers and witness statements

NPC answers may update the current case board when they become player-visible.

Use relevant sections such as:

```text
knownNPCs
knownFacts
timelineNotes
openQuestions
pendingLeads
contradictions
```

The board should record what the NPC said or what contradiction the player noticed. It should not record hidden author knowledge, undiscovered lies, or private motive truth until the player discovers them.

## Images

Images seen should record player-facing image activity.

An image entry may include:

- image ID;
- label;
- image class;
- turn shown;
- text fallback used;
- related clue, evidence, object, NPC, or location IDs.

Images must not introduce essential evidence that is absent from text.

If an image conflicts with text or the game package, the package and text control.

## Update timing

The Game Master should update `case-board-current.json` when:

- gameplay starts and the board is initialized;
- a typed discovery rule produces player-visible information;
- a known fact is established;
- evidence is observed, inspected, interpreted, or recovered;
- an NPC becomes known, met, or questioned;
- a suspect is added, deprioritized, or cleared by player-visible evidence;
- a location becomes known or visited;
- an object becomes visible or inspected;
- an area or lead is ruled out;
- an image is shown;
- an open question is added or answered;
- a theory is proposed, revised, contradicted, or abandoned;
- a timeline note becomes known;
- a pending lead opens;
- a lead closes;
- a contradiction is discovered or explained.

The Game Master should update only with information available to the player.

## Discovery rule relationship

Typed discovery rules define when canonical clues and evidence become player-visible.

When a discovery rule fires, it may update the case board sections named in the rule's `updatesCaseBoardSections`.

The current board should record the player-visible result, not the hidden rule logic.

For example, a rule may reference a hidden clue ID internally, but the board entry should say only what the player has actually observed, inspected, read, compared, or inferred.

If a discovery rule fails or produces negative investigation, the board may update `inspectedObjects`, `ruledOutAreas`, `closedLeads`, `pendingLeads`, or `openQuestions` with safe player-visible results.

## Resume support

The current case board supports resuming a game by giving the player and Game Master a shared visible memory of the investigation.

On resume, the Game Master should read:

```text
games/<case-folder>/runtime-state.json
games/<case-folder>/case-board-current.json
```

Runtime state restores session mechanics. The current case board restores the visible investigation summary.

## What must never be placed on the board

Do not place these on `case-board-current.json` unless already discovered by the player:

- the true culprit;
- hidden motive;
- hidden method;
- undiscovered clue meanings;
- undiscovered evidence provenance;
- secret witness knowledge;
- hidden true timeline events;
- red herring explanations;
- final proof;
- author notes;
- validator-only analysis;
- Game Master private reasoning.

## Failure conditions

The current case board fails if it:

- reveals hidden solution facts;
- treats visible objects as interpreted clues;
- treats player theories as confirmed truth too early;
- loses inspected objects;
- omits useful negative findings;
- merges pending leads with closed or ruled-out leads;
- treats image-only details as evidence;
- records unauthored NPCs, objects, documents, evidence, images, locations, or branches as investigative assets;
- writes player-facing state back into `game-package.json`;
- contradicts `runtime-state.json` or the canonical package.
