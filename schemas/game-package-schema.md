# Game Package Schema

## Purpose

This document defines the human-readable structure of a game package for the AI Interactive Fiction project.

A game package is the durable, validated source of truth for a playable mystery. It should contain everything the Story Author, Validator, AI Playtester, Revision Engine, and Game Master need to generate, test, revise, and run the case.

## Core principle

The game package must contain the complete hidden truth before gameplay begins.

The Game Master may improvise prose, transitions, and minor environmental details, but it must not invent:

- culprit;
- motive;
- method;
- timeline;
- clue meanings;
- evidence provenance;
- final proof.

## Package lifecycle

A game package should move through these statuses:

1. `draft`
2. `validation_failed`
3. `validated`
4. `playtest_failed`
5. `playtested`
6. `approved_for_human_play`
7. `in_play`
8. `completed`
9. `archived`

## Recommended file structure

```text
games/<case-id>/
  game-package.json
  solution.md
  case-board-seed.json
  asset-manifest.json
  validation-report.md
  playtest-report.md
  revision-notes.md
  assets/
```

Early versions may use one consolidated `game-package.json`, but the schema should support later file separation.

## Top-level structure

A complete `game-package.json` should include:

```json
{
  "caseMetadata": {},
  "playerConfig": {},
  "scopeBudget": {},
  "setting": {},
  "centralMystery": {},
  "solution": {},
  "characters": [],
  "locations": [],
  "timeline": [],
  "clues": [],
  "redHerrings": [],
  "evidence": [],
  "scenes": [],
  "discoveryRules": [],
  "caseBoardSeed": {},
  "assetManifest": [],
  "validationTargets": {},
  "runtimeState": {}
}
```

`runtimeState` should be empty or omitted before gameplay. It may be populated when the package is copied into an active play session.

## 1. caseMetadata

Identifies the game package.

Required fields:

- `caseId`
- `title`
- `version`
- `status`
- `createdAt`
- `lastUpdatedAt`
- `authorRole`
- `validationStatus`
- `playtestStatus`

Recommended fields:

- `shortDescription`
- `estimatedPlayTimeMinutes`
- `repositoryPath`
- `notes`

Example:

```json
{
  "caseId": "case-001",
  "title": "The Clock in the Locked Study",
  "version": "0.1.0",
  "status": "draft",
  "validationStatus": "not_validated",
  "playtestStatus": "not_playtested"
}
```

## 2. playerConfig

Stores the setup decisions made before authorship.

These values constrain the entire case.

Required fields:

- `lengthPreset`
- `difficulty`
- `genre`
- `tone`
- `settingSummary`
- `playerRole`
- `imageMode`
- `interactionMode`
- `hintPolicy`

Allowed `lengthPreset` values:

- `quick_mystery`
- `one_sitting`
- `standard_case`
- `extended_case`

Allowed `difficulty` values:

- `easy`
- `medium`
- `hard`

Allowed `imageMode` values:

- `none`
- `player_requested_only`
- `occasional_suggested`
- `asset_rich`

Allowed `interactionMode` values:

- `text_first`
- `voice_friendly`
- `mixed`

Allowed `hintPolicy` values:

- `none`
- `on_request_only`
- `gentle_when_stuck`
- `proactive_for_easy_mode`

Design rule:

If the player changes major configuration after validation, the case should be regenerated or revalidated.

## 3. scopeBudget

Defines hard or soft limits for the case.

Required fields:

- `maxPrimaryLocations`
- `maxMajorNpcCount`
- `maxEssentialClueCount`
- `maxRedHerringCount`
- `maxNestedSecrets`
- `expectedPlayTimeMinutesMin`
- `expectedPlayTimeMinutesMax`

### Quick Mystery budget

For `quick_mystery`, enforce:

- `maxPrimaryLocations`: 1
- `maxMajorNpcCount`: 3
- `maxEssentialClueCount`: 10
- `maxRedHerringCount`: 1
- `maxNestedSecrets`: 0
- expected play time: 10 to 25 minutes

The Validator must fail a Quick Mystery that exceeds these hard constraints.

## 4. setting

Defines the world context.

Required fields:

- `place`
- `era`
- `dateOrSeason`
- `socialContext`
- `technologyLevel`
- `toneNotes`

Recommended fields:

- `sensoryStyle`
- `historicalConstraints`
- `languageStyle`

The setting must support the selected genre and tone.

## 5. centralMystery

Defines the problem the player is asked to solve.

Required fields:

- `mysteryType`
- `openingProblem`
- `victimOrTarget`
- `stakes`
- `playerObjective`
- `successCondition`

Examples of `mysteryType`:

- murder;
- theft;
- disappearance;
- fraud;
- blackmail;
- sabotage;
- identity deception;
- locked room puzzle.

## 6. solution

Defines the hidden truth.

This is the most important section of the package.

Required fields:

- `culpritCharacterId`
- `victimCharacterId` or `targetId`
- `motive`
- `motiveProportionality`
- `method`
- `opportunity`
- `means`
- `concealmentPlan`
- `culpritMistake`
- `proofRequiredForAccusation`
- `essentialClueIds`
- `supportingClueIds`
- `redHerringIds`
- `trueTimelineEventIds`
- `finalRevealBeats`
- `postResolutionAnswers`

### motiveProportionality

Must explain why the culprit's action is plausible in context.

Weak secrets should not support major crimes unless the emotional or practical consequence is strong.

### proofRequiredForAccusation

Must define the minimum evidence needed for the player to fairly accuse the culprit.

Example:

```json
{
  "requiredClueIds": ["clue-003", "clue-006", "clue-009"],
  "deductionRequired": "The player must connect the torn telegram to the false alibi and the missing key.",
  "insufficientAccusationResponse": "The theory is plausible, but Ames cannot yet prove how the suspect entered the room."
}
```

## 7. characters

Defines NPCs and suspects.

Required fields for each character:

- `characterId`
- `name`
- `role`
- `isMajorNpc`
- `isSuspect`
- `relationshipToMystery`
- `apparentMotive`
- `trueMotiveOrInnocentExplanation`
- `alibiClaim`
- `alibiTruth`
- `knowledge`
- `secrets`
- `liesOrOmissions`
- `cluesPointingToward`
- `cluesClearingOrImplicating`
- `interrogationGuidance`

NPCs should have bounded knowledge. The Game Master should know what each person can and cannot truthfully answer.

## 8. locations

Defines places the player can investigate.

Required fields for each location:

- `locationId`
- `name`
- `isPrimaryLocation`
- `description`
- `purpose`
- `availableFromStart`
- `entryConditions`
- `charactersPresent`
- `clueIds`
- `evidenceIds`
- `exitLeads`
- `assetIds`

For a Quick Mystery, only one location may be primary.

## 9. timeline

Defines the true chronology.

Required fields for each event:

- `eventId`
- `sequenceOrder`
- `dateTimeLabel`
- `locationId`
- `participantCharacterIds`
- `summary`
- `cause`
- `effect`
- `evidenceCreatedIds`
- `evidenceMovedIds`
- `clueIdsGenerated`
- `witnessKnowledgeCreated`
- `visibilityToPlayer`

Timeline events must support object movement, witness claims, and clue provenance.

## 10. clues

Defines all discoverable clues.

Required fields for each clue:

- `clueId`
- `title`
- `playerFacingDescription`
- `trueMeaning`
- `importance`
- `discoveryLocationId`
- `discoveryConditions`
- `sourceOrProvenance`
- `associatedTimelineEventId`
- `associatedCharacterIds`
- `associatedEvidenceIds`
- `pointsTowardCharacterIds`
- `clearsCharacterIds`
- `supportsSolution`
- `resolvedInFinalReveal`
- `assetIds`
- `textFallback`

Allowed `importance` values:

- `essential`
- `supporting`
- `optional`
- `red_herring`
- `atmosphere`

A clue marked `essential` must appear in `solution.essentialClueIds`.

## 11. redHerrings

Defines misleading but explainable elements.

Required fields:

- `redHerringId`
- `title`
- `appearsToSuggest`
- `innocentExplanation`
- `discoveryConditions`
- `clearanceConditions`
- `relatedClueIds`
- `fairnessNotes`

A red herring must be clearable or explainable by the final reveal.

## 12. evidence

Defines physical or documentary objects.

Required fields:

- `evidenceId`
- `title`
- `type`
- `description`
- `currentLocationId`
- `createdByCharacterId`
- `createdDuringTimelineEventId`
- `chainOfCustody`
- `accessHistory`
- `discoveryConditions`
- `associatedClueIds`
- `assetIds`

Evidence provenance is required. The Validator should flag evidence without creation and access history.

## 13. scenes

Defines playable scene frames.

Required fields:

- `sceneId`
- `locationId`
- `entryConditions`
- `openingNarration`
- `availableCharacterIds`
- `availableClueIds`
- `availableEvidenceIds`
- `likelyPlayerQuestions`
- `safeAnswers`
- `hiddenFactsNotYetRevealed`
- `exitLeads`

Scenes are not rigid branches. They are structured support for conversational play.

## 14. discoveryRules

Defines when clues, scenes, assets, and information become available.

Required fields:

- `ruleId`
- `triggerType`
- `triggerDescription`
- `revealsClueIds`
- `revealsEvidenceIds`
- `revealsLocationIds`
- `revealsAssetIds`
- `caseBoardUpdates`

Examples of `triggerType`:

- inspect object;
- ask NPC;
- compare clues;
- revisit location;
- accuse suspect;
- request case board;
- time/event progression.

## 15. caseBoardSeed

Defines the starting state for the player's case board.

Required fields:

- `knownFacts`
- `knownCharacters`
- `knownLocations`
- `openQuestions`
- `activeLeads`
- `discoveredClueIds`
- `discoveredEvidenceIds`
- `seenAssetIds`
- `playerTheories`

At game start, most discovered arrays should be empty or limited to opening facts.

## 16. assetManifest

Defines images, maps, portraits, documents, and other player-facing assets.

Required fields for each asset:

- `assetId`
- `title`
- `assetType`
- `associatedLocationId`
- `associatedCharacterIds`
- `associatedClueIds`
- `discoveryConditions`
- `textFallback`
- `retrievalLabel`
- `spoilerLevel`
- `isCanonicalEvidence`
- `containsHiddenClues`

Rules:

- `containsHiddenClues` should normally be `false`.
- If an asset depicts evidence, the clue must also be described in text.
- Assets should be retrievable by label after discovery.

## 17. validationTargets

Defines what the Validator must check.

Required fields:

- `mustResolveClueIds`
- `mustExplainRedHerringIds`
- `mustValidateTimelineEventIds`
- `mustValidateEvidenceIds`
- `mustSupportAccusationWithClueIds`
- `knownRiskAreas`

## 18. runtimeState

Used only during active play.

Possible fields:

- `currentSceneId`
- `visitedLocationIds`
- `discoveredClueIds`
- `discoveredEvidenceIds`
- `knownCharacterIds`
- `seenAssetIds`
- `openLeads`
- `closedLeads`
- `playerTheories`
- `accusationsMade`
- `gameStatus`

Runtime state should not replace the canonical solution.

## Quick Mystery example skeleton

```json
{
  "caseMetadata": {
    "caseId": "case-quick-001",
    "title": "Untitled Quick Mystery",
    "status": "draft"
  },
  "playerConfig": {
    "lengthPreset": "quick_mystery",
    "difficulty": "easy",
    "genre": "classic detective",
    "tone": "lighthearted",
    "settingSummary": "A single drawing room in a 1940s townhouse",
    "playerRole": "private detective",
    "imageMode": "player_requested_only",
    "interactionMode": "text_first",
    "hintPolicy": "gentle_when_stuck"
  },
  "scopeBudget": {
    "maxPrimaryLocations": 1,
    "maxMajorNpcCount": 3,
    "maxEssentialClueCount": 10,
    "maxRedHerringCount": 1,
    "maxNestedSecrets": 0,
    "expectedPlayTimeMinutesMin": 10,
    "expectedPlayTimeMinutesMax": 25
  }
}
```

## Validation implications

The Validator must fail a package if:

- player setup is missing;
- scope budget is missing;
- the authored game exceeds hard scope limits;
- solution fields are incomplete;
- essential clues are not discoverable;
- major clues lack closure;
- evidence lacks provenance;
- the Game Master would need to invent core facts.

## Authorship implications

The Story Author must not begin with an open-ended mystery idea alone.

It must first know the player's configuration and scope budget.

For example, if `lengthPreset` is `quick_mystery`, the Story Author must design a compact one-room mystery rather than a citywide investigation.

## Game Master implications

The Game Master must respect the package constraints during play.

For a Quick Mystery, the Game Master should not add new rooms, new suspects, or a second layer of conspiracy during play. It should deepen the investigation within the defined room.
