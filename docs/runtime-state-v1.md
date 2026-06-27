# Runtime State v1

## Purpose

Runtime State v1 defines how the Game Master records changing player-session state during gameplay.

The canonical game package answers what is true in the authored mystery.

Runtime state answers what this player has seen, inspected, learned, ruled out, asked, theorized, requested, or resolved during this play session.

## Core rule

Do not write player progress back into `game-package.json`.

Use:

```text
games/<caseId>-<slug>/runtime-state.json
```

for live gameplay state.

Use:

```text
schemas/runtime-state.schema.json
```

as the machine-readable contract for that file.

## Relationship to canon

Runtime state is not canon.

Runtime state must never change:

- culprit;
- motive;
- method;
- true timeline;
- clue meanings;
- evidence provenance;
- witness knowledge;
- red herring explanations;
- final proof.

Those facts belong in the canonical game package.

Runtime state may record that the player has discovered, misunderstood, partially interpreted, or failed to discover those facts.

## Required responsibilities

Runtime state should help the Game Master answer these questions before responding:

```text
Has the player seen this?
Has the player inspected it?
Has the player closely inspected it?
Has the player recovered it as evidence?
Has the player ruled it out?
Has this NPC already been questioned on this topic?
Was a contradiction already discovered?
Was a hint already given?
Has this image already been shown?
Is this clue visible, discovered, interpreted, or still hidden?
```

## Top-level sections

Runtime State v1 uses these top-level sections:

```text
metadata
session
currentPosition
discoveredState
objectState
npcState
leadState
hintState
accusationState
imageState
caseBoardSummary
outOfGameNotes
```

## metadata

Identifies the case and state file.

Should include:

- case ID;
- case title;
- game package version;
- runtime schema version;
- last updated turn;
- last updated timestamp or label.

## session

Tracks the play session itself.

Should include:

- session status;
- turn count;
- interaction mode;
- image mode;
- hint policy;
- whether gameplay has started;
- whether the case has been solved.

Allowed session status values:

```text
not_started
in_progress
paused
solved
abandoned
postgame
```

## currentPosition

Tracks where the player currently is.

Should include:

- current scene ID;
- current location ID;
- current NPC conversation, if any;
- current focus object, if any;
- active mode, such as observing, investigating, interviewing, reviewing, accusing, or out-of-game.

## discoveredState

Tracks what the player knows.

Should include arrays for:

- known fact IDs or labels;
- discovered clue IDs;
- interpreted clue IDs;
- discovered evidence IDs;
- recovered evidence IDs;
- known character IDs;
- known suspect IDs;
- cleared or deprioritized suspect IDs;
- known location IDs;
- visited location IDs;
- discovered contradiction IDs or labels.

A clue may be discovered without being interpreted.

That distinction is important.

## objectState

Tracks visible and inspected objects.

Each object entry should record:

- object ID or label;
- location ID;
- current state;
- inspection depth;
- last result shown to the player;
- associated clue IDs;
- whether the object has been ruled out;
- whether closer inspection remains possible;
- turn first seen;
- turn last inspected.

Allowed object states:

```text
unseen
visible
mentioned
inspected
closely_inspected
evidence_recovered
ruled_out
revisited
```

## npcState

Tracks NPC interaction history.

Each NPC entry should record:

- character ID;
- whether the player has met them;
- whether they have been questioned;
- topics already asked;
- claims the player has heard;
- lies or omissions revealed to the player;
- contradictions known to the player;
- current attitude, if relevant;
- turn last questioned.

The Game Master should use this to avoid making NPCs repeat, contradict, or reveal knowledge they do not have.

## leadState

Tracks investigation leads.

Should include:

- open leads;
- pending leads;
- closed leads;
- blocked leads;
- lead source;
- reason a lead was opened or closed;
- related clue, evidence, NPC, location, or object IDs.

Negative investigations should often become closed leads or ruled-out areas.

## hintState

Tracks hint usage.

Should include:

- hints requested count;
- proactive hints offered count;
- highest hint level used;
- hint history;
- whether the player appears stuck.

Allowed hint levels:

```text
none
general_nudge
relevant_area_or_npc
relevant_object_or_comparison
near_explicit_next_action
```

The Game Master should not repeat the same hint level without adding value.

## accusationState

Tracks player theories and accusations.

Should include:

- theories proposed;
- accusations made;
- culprit guessed;
- motive guessed;
- method guessed;
- proof offered;
- missing proof explained;
- whether the accusation met the proof threshold.

This allows partial accusations without prematurely ending the case.

## imageState

Tracks player-facing image activity.

Should include:

- seen asset IDs;
- requested asset IDs;
- denied or deferred image requests;
- reason for denial or deferral;
- generated image labels;
- text fallback used.

Images remain supportive only.

The text fallback and game package control if an image conflicts with canon.

## caseBoardSummary

Stores a compact copy of player-facing investigation state.

This is not a replacement for `case-board-current.json` if that file exists.

It is a minimum runtime summary that lets the Game Master preserve continuity even when no separate case-board file has been written.

Should include:

- known facts;
- evidence;
- suspects;
- inspected objects;
- ruled-out areas;
- open questions;
- pending leads;
- closed leads;
- contradictions;
- working theories.

## outOfGameNotes

Tracks playtest or design feedback submitted during gameplay.

Messages beginning with `/`, `Out of game:`, or `Note to ChatGPT:` may be summarized here when the player wants the issue preserved.

Out-of-game notes must not advance gameplay state.

## Update timing

The Game Master should update runtime state when:

- gameplay starts;
- the player changes location or scene;
- a clue is discovered;
- a clue is interpreted;
- evidence is observed or recovered;
- an object is inspected or ruled out;
- an NPC is questioned;
- a contradiction is discovered;
- a lead opens, closes, or becomes blocked;
- a hint is requested or offered;
- an image is shown, requested, denied, or deferred;
- a theory or accusation is made;
- the case is solved, paused, abandoned, or moved to postgame.

## Minimal Quick Mystery usage

Quick Mysteries may use a lightweight runtime state file.

At minimum, they should track:

```text
session
currentPosition
discoveredState
objectState
npcState
leadState
hintState
accusationState
imageState
caseBoardSummary
```

The purpose is not bureaucracy.

The purpose is to prevent the Game Master from forgetting what the player has already done.

## Failure conditions

Runtime state fails if the Game Master:

- loses discovered clues;
- forgets inspected objects;
- reopens ruled-out areas without reason;
- repeats hints without tracking prior hints;
- lets NPCs contradict earlier player-facing answers;
- treats visible objects as interpreted clues;
- treats image details as independent evidence;
- stores player progress in `game-package.json`;
- changes canonical truth during play.

## Relationship to future phases

Runtime State v1 supports future work on:

- Case Board Current Schema;
- stronger discovery rule typing;
- NPC interview models;
- save/resume behavior;
- campaign support;
- coded application state management.
