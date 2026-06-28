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
  "canonicalAssetInventory": {},
  "runtimeBudgets": {},
  "caseBoardSeed": {},
  "assetManifest": [],
  "visualDefinitions": [],
  "imageGalleryPolicy": {},
  "imageReusePolicy": {},
  "evidencePhotoDefinitions": [],
  "cutawayDefinitions": [],
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
- `interviewTopics`
- `cluesPointingToward`
- `cluesClearingOrImplicating`
- `interrogationGuidance`

NPCs should have bounded knowledge. The Game Master should know what each person can and cannot truthfully answer.

Important NPCs should include structured `interviewTopics` following:

```text
docs/npc-interview-model-v1.md
```

Recommended interview topic fields:

- `topicId`
- `topicLabel`
- `topicType`
- `npcId`
- `playerQuestionExamples`
- `truthfulAnswer`
- `lieOrOmission`
- `evasiveAnswer`
- `knowledgeBoundary`
- `emotionalState`
- `revealsClueIds`
- `revealsEvidenceIds`
- `prerequisiteClueIds`
- `prerequisiteEvidenceIds`
- `contradictionIds`
- `followUpTopicIds`
- `repeatAnswer`
- `validationNotes`

Interview topics define what the NPC can say. `question_npc` discovery rules define when a topic reveals clue or evidence IDs.

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

Defines when clues, evidence, scenes, assets, and information become available.

Discovery rules should follow:

```text
docs/discovery-rules-v1.md
```

Discovery rules replace loose discovery-condition prose with typed, machine-checkable triggers.

Required fields:

- `ruleId`
- `triggerType`

Recommended fields:

- `description`
- `locationId`
- `objectId`
- `npcId`
- `topicId`
- `clueId`
- `evidenceId`
- `documentId`
- `prerequisiteClueIds`
- `prerequisiteEvidenceIds`
- `prerequisiteLocationIds`
- `prerequisiteObjectIds`
- `revealsClueIds`
- `revealsEvidenceIds`
- `revealsLocationIds`
- `revealsAssetIds`
- `updatesCaseBoardSections`
- `discoveryText`
- `failureText`
- `repeatText`
- `isOptional`
- `isRedHerring`
- `validationNotes`

Allowed `triggerType` values:

- `observe_scene`
- `inspect_object`
- `closely_inspect_object`
- `question_npc`
- `compare_evidence`
- `read_document`
- `revisit_location`
- `make_theory`
- `accuse`
- `request_hint`

Design rule:

Every essential clue should have at least one fair discovery rule. Optional clues and red herrings should be marked so the Validator, AI Playtester, Revision Engine, and Game Master can distinguish critical path information from enrichment or misdirection.

Discovery rules may reveal only canonical assets. When `canonicalAssetInventory` exists, rule references should point to IDs listed there.

## 15. canonicalAssetInventory

Defines the authored investigative asset allowlist the runtime may expose.

Recommended fields:

- `npcIds`
- `locationIds`
- `objectIds`
- `evidenceIds`
- `documentIds`
- `imageIds`
- `discoveryRuleIds`
- `interviewTopicIds`
- `sceneIds`
- `clueIds`
- `redHerringIds`
- `notes`

This section is optional for backward compatibility, but new packages should include it. It should be derived from the canonical package sections, not invented separately.

## 16. runtimeBudgets

Defines maximum runtime scope for the package.

Recommended fields:

- `maxMajorNPCs`
- `maxInterviewableNPCs`
- `maxBackgroundCharacters`
- `maxPrimaryLocations`
- `maxSecondaryLocations`
- `maxSearchableObjects`
- `maxEvidenceItems`
- `maxDocuments`
- `maxImages`
- `maxDiscoveryRules`
- `maxRedHerrings`
- `maxInterviewTopics`
- `maxHints`
- `maxPlayerFacingBranches`
- `hardBudgetFields`
- `softBudgetFields`
- `notes`

Runtime budgets reinforce the scope budget and are enforced by the Game Master. Hard budgets cannot be exceeded during play; soft budgets guide pacing and atmosphere.

## 17. caseBoardSeed

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

## 18. assetManifest

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

## 19. visualDefinitions

Defines canonical visual rules for generated or shown images.

Recommended fields for each visual definition:

- `visualDefinitionId`
- `locationId`
- `assetId`
- `imageType`
- `canonicalDescription`
- `requiredVisibleObjectIds`
- `optionalVisibleObjectIds`
- `forbiddenObjectIds`
- `fixedGeometryNotes`
- `cameraAllowedViews`
- `hiddenElementRules`
- `continuityAnchor`
- `textFallback`
- `validationNotes`

Allowed `imageType` values include:

- `scene`
- `inspection_closeup`
- `evidence_photo`
- `technical_cutaway`
- `map`
- `memory_recall`
- `portrait`
- `other`

Visual definitions are optional for backward compatibility but should be included when image mode is enabled or optional.

## 20. imageGalleryPolicy and imageReusePolicy

`imageGalleryPolicy` defines whether the runtime supports image recall commands and gallery labels.

`imageReusePolicy` defines when prior images must be reused instead of regenerated.

Repeated canonical scene images should normally be reused unless the player requests a new allowed view or the package defines a player-visible scene change.

## 21. evidencePhotoDefinitions and cutawayDefinitions

Evidence photo definitions govern images of discovered or recovered evidence.

Cutaway definitions govern internal geometry and hidden mechanisms. They must not reveal hidden compartments, rear panels, concealed access, or internal structures before the player has discovered them in text.

## 22. validationTargets

Defines what the Validator must check.

Required fields:

- `mustResolveClueIds`
- `mustExplainRedHerringIds`
- `mustValidateTimelineEventIds`
- `mustValidateEvidenceIds`
- `mustSupportAccusationWithClueIds`
- `knownRiskAreas`

## 23. runtimeState

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
- `budgetUsage`, for compact tracking of used IDs, exhausted leads, and whether deduction mode has begun
- image runtime tracking, such as generated image IDs, shown image IDs, reused image IDs, image request history, shown visual definition IDs, and image mismatch flags

Runtime state should not replace the canonical solution.

## Validation report schema

Validation reports are separate diagnostic artifacts, not part of `game-package.json`.

Structured reports should follow:

```text
docs/validator-diagnostics-v1.md
schemas/validation-report.schema.json
```

Validation reports should cite canonical IDs instead of duplicating canonical content.

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
  },
  "canonicalAssetInventory": {
    "npcIds": [],
    "locationIds": [],
    "objectIds": [],
    "evidenceIds": [],
    "documentIds": [],
    "imageIds": [],
    "discoveryRuleIds": [],
    "interviewTopicIds": [],
    "sceneIds": [],
    "clueIds": []
  },
  "runtimeBudgets": {
    "maxMajorNPCs": 3,
    "maxInterviewableNPCs": 3,
    "maxPrimaryLocations": 1,
    "maxSecondaryLocations": 0,
    "maxEvidenceItems": 10,
    "maxRedHerrings": 1,
    "maxPlayerFacingBranches": 6,
    "hardBudgetFields": [
      "maxMajorNPCs",
      "maxInterviewableNPCs",
      "maxPrimaryLocations",
      "maxRedHerrings"
    ]
  }
}
```

## Validation implications

The Validator must fail a package if:

- player setup is missing;
- scope budget is missing;
- canonical inventory or runtime budgets are missing from a new package;
- the authored game exceeds hard scope limits;
- solution fields are incomplete;
- essential clues are not discoverable;
- major clues lack closure;
- evidence lacks provenance;
- the Game Master would need to invent core facts or exceed runtime budgets.

## Authorship implications

The Story Author must not begin with an open-ended mystery idea alone.

It must first know the player's configuration and scope budget.

For example, if `lengthPreset` is `quick_mystery`, the Story Author must design a compact one-room mystery rather than a citywide investigation.

## Game Master implications

The Game Master must respect the package constraints during play.

For a Quick Mystery, the Game Master should not add new rooms, new suspects, or a second layer of conspiracy during play. It should deepen the investigation within the defined room.

It should also refuse or redirect attempts to exceed `canonicalAssetInventory` or `runtimeBudgets`, then return to authored leads, case-board review, or deduction mode.
