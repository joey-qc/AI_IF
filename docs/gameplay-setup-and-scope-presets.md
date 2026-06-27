# Gameplay Setup and Scope Presets

## Purpose

This document defines the player-facing setup choices that must be collected before game authorship begins, plus the scope presets that constrain game size, complexity, and validation expectations.

The first playtest asked the player questions about genre, tone, length, setting, and images immediately before gameplay. That was useful, but in the new architecture those choices must happen earlier.

A generated game should be authored, validated, AI-playtested, and revised against the player's setup choices before the human player begins.

## Core rule

Player setup decisions are inputs to authorship, not runtime preferences.

Once a case is authored and validated, these settings should be considered locked for that game package:

- genre;
- tone;
- setting;
- era;
- length preset;
- difficulty;
- image mode;
- player role;
- voice/text preference;
- hint policy;
- content boundaries.

If the player changes one of these foundational settings after validation, the case should usually be regenerated or revalidated.

## Why setup must happen before authorship

Setup choices affect the actual structure of the mystery.

Examples:

- A one-room quick mystery needs a different clue design than a multi-location case.
- A hard mystery can support ambiguity that an easy mystery should not.
- A voice-first game should avoid large tables and long document-heavy clue dumps.
- An image-heavy game needs a richer asset manifest.
- A no-image game must ensure all artifacts are fully represented in text.
- A lighthearted tone should avoid motives or crimes that create tonal mismatch.

The Story Author, Validator, AI Playtester, and Game Master must all know these constraints.

## Recommended setup workflow

Before story authorship, collect or assign values for:

1. Game length preset.
2. Difficulty preset.
3. Genre.
4. Tone.
5. Setting and era.
6. Player role.
7. Image mode.
8. Interaction mode.
9. Hint policy.
10. Content boundaries.

These values should be stored in the game package under:

```json
{
  "playerConfig": {},
  "scopeBudget": {}
}
```

## Player configuration fields

### lengthPreset

Controls the scale of the game.

Allowed values:

- `quick_mystery`
- `one_sitting`
- `standard_case`
- `extended_case`

### difficulty

Controls clue clarity, number of red herrings, deduction burden, and hint aggressiveness.

Allowed values:

- `easy`
- `medium`
- `hard`

### genre

Examples:

- classic detective;
- noir;
- cozy mystery;
- gothic;
- science fiction;
- historical mystery;
- espionage;
- supernatural mystery.

### tone

Examples:

- lighthearted;
- serious;
- noir;
- eerie;
- comedic;
- cerebral;
- melancholy;
- adventurous.

### setting

Should define location and era clearly enough for authorship.

Examples:

- 1947 New York City;
- present-day Savannah;
- Victorian London;
- near-future Mars colony;
- 1930s ocean liner.

### playerRole

Examples:

- private detective;
- police detective;
- journalist;
- amateur sleuth;
- insurance investigator;
- archivist;
- passenger or guest;
- family member.

### imageMode

Allowed values:

- `none`
- `player_requested_only`
- `occasional_suggested`
- `asset_rich`

Default recommendation: `player_requested_only`.

Images should support narration and evidence, not replace it.

### interactionMode

Allowed values:

- `text_first`
- `voice_friendly`
- `mixed`

### hintPolicy

Allowed values:

- `none`
- `on_request_only`
- `gentle_when_stuck`
- `proactive_for_easy_mode`

### contentBoundaries

Optional limits on violence, horror, sexual content, cruelty, or other topics.

## Scope presets

### Quick Mystery

A compact mystery designed for a short, focused play session.

#### Intended experience

The entire mystery unfolds in one location or room. The player can solve the case through close observation, questioning, and deduction without traveling between locations.

#### Recommended use

Use this when the player wants a short mystery that can be completed quickly, especially in a single conversation or voice session.

#### Hard constraints

- Primary locations: exactly 1.
- Characters/NPCs: no more than 3 major NPCs.
- Essential clues: no more than 10.
- Red herrings: no more than 1.
- Central mystery: exactly 1.
- Nested secrets: 0.
- Major scene transitions: 0 to 1.
- Asset count: 0 to 4.
- Expected play time: 10 to 25 minutes.

#### Structural expectations

A Quick Mystery should usually include:

- one confined setting;
- one immediate problem;
- three or fewer people with relevant knowledge;
- a small number of inspectable objects;
- one contradiction or decisive clue chain;
- a concise final accusation;
- a brief but complete final reveal.

#### Suitable examples

- A forged letter in a locked study.
- A stolen necklace during a dinner party.
- A poisoned glass at a card table.
- A missing will in a solicitor's office.
- A swapped photograph in an archive room.

#### Unsuitable examples

- A citywide conspiracy.
- Multi-day missing-person cases.
- Four or more suspects with complex alibis.
- Multiple crime scenes.
- Nested historical secrets requiring many documents.

### One Sitting

A fuller mystery designed for one substantial session.

#### Hard constraints

- Primary locations: 4 to 6.
- Major NPCs/suspects: 3 to 5.
- Essential clues: 6 to 12.
- Red herrings: 1 to 3.
- Central mystery: 1.
- Nested secrets: 0 to 1.
- Expected play time: 30 to 60 minutes.

### Standard Case

A longer case intended for multiple sessions or a longer single session.

#### Recommended constraints

- Primary locations: 6 to 10.
- Major NPCs/suspects: 5 to 8.
- Essential clues: 10 to 18.
- Red herrings: 2 to 5.
- Central mystery: 1 to 2 related mysteries.
- Nested secrets: 1 to 2.
- Expected play time: 1 to 3 hours.

### Extended Case

A campaign-style mystery with multiple phases.

#### Recommended constraints

- Primary locations: 10 or more.
- Major NPCs/suspects: 8 or more.
- Essential clues: 18 or more.
- Red herrings: 4 or more.
- Multiple acts or chapters.
- Expected play time: multiple sessions.

Extended cases require stronger state management and should not be attempted until Quick Mystery and One Sitting cases validate successfully.

## Difficulty presets

### Easy

Designed to be solvable with moderate attention.

Rules:

- Clues should be fairly direct.
- Red herrings should be limited and clearable.
- The Game Master may gently redirect when stuck.
- The final proof threshold should be explicit.
- NPC lies should be simple and discoverable.

### Medium

Designed for normal detective play.

Rules:

- Clues may require comparison or inference.
- Red herrings may persist longer.
- The player may need to reconstruct timeline or motive.
- Hints should be on request or after clear stagnation.

### Hard

Designed for careful deduction.

Rules:

- Clues may be indirect.
- Alibis and timeline details may require close attention.
- Red herrings may be more persuasive.
- The player may need to build a complete theory before accusation.
- The case must still be fair and solvable.

## Setup lock

Once the game package is generated, store the setup settings in:

```json
{
  "caseMetadata": {
    "status": "draft"
  },
  "playerConfig": {
    "lengthPreset": "quick_mystery",
    "difficulty": "easy",
    "genre": "classic detective",
    "tone": "lighthearted",
    "setting": "1947 New York City",
    "imageMode": "player_requested_only"
  },
  "scopeBudget": {
    "maxPrimaryLocations": 1,
    "maxMajorNpcCount": 3,
    "maxEssentialClueCount": 10,
    "maxRedHerringCount": 1
  }
}
```

The Validator must compare the authored case against these values.

The AI Playtester must test whether the case feels like the selected preset.

The Game Master must not expand beyond these values during play.

## Design implication

The old startup questions should not disappear. They should move earlier in the pipeline.

Old model:

```text
Player setup -> immediate gameplay
```

New model:

```text
Player setup -> authorship -> validation -> AI playtest -> revision -> human gameplay
```

This is one of the key architectural changes from the first playtest.
