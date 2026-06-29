# Discovery Rules v1

## Purpose

Discovery Rules v1 defines the typed structure used to describe how canonical clues, evidence, locations, assets, and case-board updates become visible to the player.

Discovery rules live in:

```text
games/<case-folder>/game-package.json
```

The machine-readable contract is:

```text
schemas/game-package.schema.json
```

## Core idea

The canonical game package records what is true.

Discovery rules record how the player can fairly discover player-visible parts of that truth.

When `canonicalAssetInventory` exists in the game package, discovery rules may reveal only IDs listed in that inventory.

The Game Master should not reveal a clue merely because it exists in the package. A clue should become visible when the player's action satisfies a typed discovery rule and any listed prerequisites.

Discovery rules must also preserve player agency and fair evidence as defined in:

```text
docs/player-agency-and-fair-evidence-v1.md
```

If a player closely inspects an available object, ordinary observable details should be revealed then. A discovery prerequisite should not be used merely to suppress an observable mark, stain, smell, missing part, label, damage, unusual placement, ordinary content, or immediate physical oddity.

## Why typed rules exist

Loose prose discovery notes are hard for the Story Author, Validator, AI Playtester, Revision Engine, and Game Master to apply consistently.

Typed discovery rules make clue gating:

- easier to validate;
- easier to playtest;
- easier to repair;
- easier for the Game Master to map from player action to eligible reveal;
- safer against premature hidden-solution leakage.

## Standard trigger types

Use these trigger types:

```text
observe_scene
inspect_object
closely_inspect_object
question_npc
compare_evidence
read_document
revisit_location
make_theory
accuse
request_hint
```

### observe_scene

Use for information visible through ordinary scene observation.

This should reveal only immediate observations, not hidden meaning.

### inspect_object

Use when the player examines a visible or known object.

### closely_inspect_object

Use when an ordinary inspection can lead to a deeper or more precise inspection.

### question_npc

Use when the player asks an NPC about a topic.

The rule should identify the NPC and topic when possible.

NPC topics should be defined by `docs/npc-interview-model-v1.md`.

The discovery rule decides when a topic reveals clue or evidence IDs. The interview topic defines what the NPC knows, withholds, lies about, evades, or repeats.

### compare_evidence

Use when the player compares two or more clues, evidence items, documents, statements, or object states.

### read_document

Use when the player reads a visible or recovered document.

### revisit_location

Use when returning to a known location can reveal a new observation because prerequisites have changed.

### make_theory

Use when a player proposes an interpretation that can unlock a fair partial confirmation, contradiction, or next lead.

### accuse

Use when accusation handling reveals whether the proof threshold is met or what remains unproven.

Final accusation rules must not confirm the canonical solution before the package proof threshold is met.

### request_hint

Use when hint policy allows the Game Master to reveal a nudge or next investigative direction.

Hints should not reveal solution facts unless the player explicitly asks to spoil or end the case.

## Recommended fields

Each discovery rule should include:

```text
ruleId
triggerType
description
revealsClueIds
revealsEvidenceIds
updatesCaseBoardSections
discoveryText
isOptional
isRedHerring
validationNotes
```

Use these fields when they apply:

```text
locationId
objectId
npcId
topicId
clueId
evidenceId
documentId
prerequisiteClueIds
prerequisiteEvidenceIds
prerequisiteLocationIds
prerequisiteObjectIds
failureText
repeatText
```

Not every trigger type needs every field. The structure should be enforceable without making authoring brittle.

## Discovery Prerequisites vs Interpretation Prerequisites

Discovery prerequisites may restrict visibility only when they change:

- physical access;
- permission;
- available tools;
- lighting;
- inspection method;
- available testimony.

Interpretation prerequisites may restrict when the Game Master can explain what an observation means, confirm a theory, compare evidence, or synthesize proof.

Do not use a clue, evidence, or theory prerequisite to make stable physical evidence appear late unless the prerequisite also changes how the player can observe the evidence.

If evidence is physically available and closely inspected, reveal the ordinary observation and withhold only the meaning.

## Relationship to package entities

Discovery rules may reference canonical IDs from:

- clues;
- evidence;
- locations;
- objects or object-like package entries;
- NPCs;
- documents;
- assets;
- scenes.

References should point to canonical IDs, but the player-facing text in `discoveryText`, `failureText`, and `repeatText` must remain spoiler-safe.

Discovery rules must not create assets by implication. A rule that reveals an NPC, location, object, evidence item, document, image, or clue path should reference an authored ID from the package and, when present, `canonicalAssetInventory`.

Images may support discovery text, but they must not be the sole source of a clue unless an equivalent text discovery exists. Image-only clues fail runtime fidelity.

## Case-board updates

`updatesCaseBoardSections` identifies which player-facing board sections may change when the rule fires.

Allowed sections include:

```text
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

A discovery rule may update the current case board only with information available to the player.

## Failed searches and negative investigation

A failed search is still useful when it rules something out.

Use `failureText` for fair negative feedback when the trigger is plausible but does not reveal a clue.

Examples of negative investigation:

- the window shows no sign of forced entry;
- the desk contains no hidden compartment;
- an NPC cannot know the answer to a question;
- a document does not mention the expected name.

Negative results may update:

```text
inspectedObjects
ruledOutAreas
closedLeads
pendingLeads
openQuestions
```

Do not invent new clues merely to reward a failed search.

## Repeat interactions

Use `repeatText` when the player repeats an action that already fired a rule.

Repeat text should summarize prior discovery or remind the player what was already ruled out.

The Game Master should avoid re-revealing the same clue as if it were new.

## Optional clues and red herrings

Use `isOptional` for clues that enrich the mystery but are not required for a fair solution.

Use `isRedHerring` for misleading but explainable discoveries.

Red herring rules must not make the real solution impossible to infer. They should include validation notes explaining how the player can eventually clear or reinterpret the misleading path.

## Final Accusation Discovery Rules

Final accusation discovery rules must include all required proof prerequisites.

If the player accuses before prerequisites are met, the rule should return an insufficient-proof response.

Final accusation discovery text must not reveal hidden facts that were not earned through discovered clues.

If the player names the correct culprit without required proof, the Game Master should treat it as a theory check, not a solved case.

The accusation rule should align with the package's required proof list, final accusation threshold, and final reveal beats.

## Preventing hidden unfair clues

Every solution-critical clue should have at least one fair discovery rule.

A clue is unfair if it is:

- required for the final accusation but has no discovery rule;
- locked behind an invisible or unreasonable action;
- available only through an image without text support;
- revealed only after the final accusation;
- hidden behind a prerequisite that itself has no fair discovery path;
- phrased so vaguely that the Game Master must invent how to reveal it.

## Game Master processing

For each player action, the Game Master should:

1. Identify whether the action is in game or out of game.
2. Map the action to a trigger type.
3. Identify relevant location, object, NPC, topic, clue, evidence, or document IDs.
4. Check whether prerequisites are satisfied in runtime state.
5. Check whether the rule has already fired.
6. Reveal eligible clues or evidence using `discoveryText`.
7. Use `failureText` for plausible failed searches.
8. Use `repeatText` or a concise reminder for repeated discoveries.
9. Update `runtime-state.json` with fired rule and discovered IDs.
10. Update `case-board-current.json` only with player-visible results.

## Validator responsibilities

The Validator should check that:

- every required clue has at least one fair discovery rule;
- every rule uses a standard trigger type;
- rule references point to valid canonical IDs;
- rule references point to canonical inventory IDs when the package declares `canonicalAssetInventory`;
- prerequisites do not create impossible chains;
- solution-critical clues are not locked behind unreasonable actions;
- optional clues and red herrings are marked appropriately;
- `discoveryText` does not reveal hidden solution facts prematurely;
- `failureText` supports negative investigation without inventing clues;
- case-board updates are player-visible and safe.

## Revision responsibilities

The Revision Engine should repair discovery rules when validation or playtesting finds that they are:

- missing;
- too vague;
- too brittle;
- too generous;
- unfairly hidden;
- contradictory;
- disconnected from case-board or runtime-state updates.

## Examples

### Object inspection

```json
{
  "ruleId": "rule-inspect-clock-face",
  "triggerType": "inspect_object",
  "locationId": "loc-study",
  "objectId": "obj-clock",
  "revealsClueIds": ["clue-stopped-clock"],
  "updatesCaseBoardSections": ["evidence", "inspectedObjects", "openQuestions"],
  "discoveryText": "The clock face is stopped at 8:17, and the minute hand sits slightly loose.",
  "failureText": "A casual glance shows only that the clock is stopped.",
  "repeatText": "You already noted the stopped time and loose minute hand.",
  "isOptional": false,
  "isRedHerring": false,
  "validationNotes": "Essential clue; discoverable by inspecting the visible clock."
}
```

### NPC question

```json
{
  "ruleId": "rule-question-clerk-about-delivery",
  "triggerType": "question_npc",
  "npcId": "npc-clerk",
  "topicId": "topic-delivery",
  "revealsClueIds": ["clue-delivery-time"],
  "updatesCaseBoardSections": ["knownNPCs", "timelineNotes", "contradictions"],
  "discoveryText": "The clerk says the parcel arrived before the bell rang, not after.",
  "repeatText": "The clerk repeats that the parcel arrived before the bell.",
  "isOptional": false,
  "isRedHerring": false
}
```

### Negative investigation

```json
{
  "ruleId": "rule-check-window",
  "triggerType": "inspect_object",
  "locationId": "loc-study",
  "objectId": "obj-window",
  "updatesCaseBoardSections": ["inspectedObjects", "ruledOutAreas", "closedLeads"],
  "discoveryText": "The window is latched from inside and the sill shows no fresh marks.",
  "failureText": "There is no sign of outside entry here.",
  "repeatText": "The window remains latched, with no sign of forced entry.",
  "isOptional": true,
  "isRedHerring": false,
  "validationNotes": "Negative clue closes an obvious but false entry path."
}
```

## Deception Discovery Rules

Discovery rules should expose contradictions fairly.

A rule may reveal:

- a lie;
- an omission;
- a timeline contradiction;
- an alibi failure;
- an innocent explanation;
- a clearance clue.

Do not mark a suspect as lying in player-facing text until the player has discovered the contradiction.

## Red Herring Resolution Rules

Red herrings should have discovery and clearance conditions.

A red herring is incomplete if it creates suspicion but provides no way for the player to resolve whether it matters.
