# Repository Workflow

## Purpose

This document defines how repository files should be managed across the AI Interactive Fiction project.

The project uses GitHub as persistent shared storage for architecture documents, prompt modules, schemas, generated game packages, validation reports, playtest reports, revision notes, and postgame findings.

The goal is to prevent the repository from becoming disorganized as multiple AI roles create and update files over time.

## Core rule

Separate project-level knowledge from case-level knowledge.

```text
Project-level lesson -> docs/
Case-specific issue  -> games/<case-id>/
```

The master documents in `docs/` should evolve slowly and intentionally.

Per-game files under `games/<case-id>/` should capture the details, failures, revisions, and outcomes for individual cases.

## Repository layers

## 1. Project-level documents

Project-level documents describe the whole system.

Examples:

```text
README.md
docs/project-architecture.md
docs/design-principles.md
docs/playtest-findings.md
docs/gameplay-setup-and-scope-presets.md
docs/repository-workflow.md
docs/roadmap.md
```

These files should be updated only when a durable project-level decision, lesson, or architecture change is made.

They should not be used as live logs.

## 2. Prompt modules

Prompt modules define reusable AI roles.

Examples:

```text
prompts/00-player-setup.md
prompts/01-template-designer.md
prompts/02-story-author.md
prompts/03-validator.md
prompts/04-ai-playtester.md
prompts/05-revision-engine.md
prompts/06-game-master.md
```

These files should change when the workflow changes, not every time a game is generated.

## 3. Schemas

Schemas define the structure of game packages and related files.

Examples:

```text
schemas/game-package-schema.md
schemas/game-package.schema.json
schemas/character.schema.json
schemas/clue.schema.json
schemas/location.schema.json
schemas/timeline.schema.json
schemas/asset.schema.json
```

Schemas should be treated as shared contracts between AI roles.

Changing a schema may require updating prompts, validators, and existing game packages.

## 4. Game packages

Each generated game should have its own folder.

Example:

```text
games/quick-001/
  game-package.json
  solution.md
  case-board-seed.json
  asset-manifest.json
  validation-report.md
  playtest-report.md
  revision-notes.md
  postgame-report.md
  assets/
```

These files are case-specific.

Problems found in one case should usually be recorded in that case's reports first, not immediately promoted to master project documents.

## 5. Archive

Historical or obsolete prompt files should be preserved under `archive/` when useful.

Example:

```text
archive/v1-playtest-prompts/
```

Archived files are reference material. They are not active instructions unless explicitly reactivated.

## File ownership by AI role

## Player Setup role

### Reads

```text
README.md
docs/gameplay-setup-and-scope-presets.md
docs/design-principles.md
```

### Writes

```text
games/<case-id>/setup.md
games/<case-id>/player-config.json
```

### May recommend updates to

```text
docs/gameplay-setup-and-scope-presets.md
```

### Should not directly update

```text
docs/playtest-findings.md
schemas/
prompts/
```

Unless explicitly instructed.

## Template Designer role

### Reads

```text
README.md
docs/project-architecture.md
docs/design-principles.md
docs/playtest-findings.md
docs/gameplay-setup-and-scope-presets.md
```

### Writes or updates

```text
schemas/game-package-schema.md
schemas/game-package.schema.json
```

### May recommend updates to

```text
prompts/01-template-designer.md
docs/project-architecture.md
```

### Should not write

```text
games/<case-id>/game-package.json
```

The Template Designer defines structure; it does not author cases.

## Story Author role

### Reads

```text
README.md
docs/design-principles.md
docs/playtest-findings.md
docs/gameplay-setup-and-scope-presets.md
schemas/game-package-schema.md
schemas/game-package.schema.json
prompts/02-story-author.md
games/<case-id>/player-config.json
```

### Writes

```text
games/<case-id>/game-package.json
games/<case-id>/solution.md
games/<case-id>/case-board-seed.json
games/<case-id>/asset-manifest.json
games/<case-id>/author-notes.md
```

### Should not update

```text
docs/playtest-findings.md
prompts/
schemas/
```

Unless explicitly instructed.

The Story Author may identify possible project-level lessons, but they should be written first to `author-notes.md` or surfaced to the user for approval.

## Validator role

### Reads

```text
README.md
docs/design-principles.md
docs/playtest-findings.md
docs/gameplay-setup-and-scope-presets.md
schemas/game-package-schema.md
schemas/game-package.schema.json
prompts/03-validator.md
games/<case-id>/game-package.json
games/<case-id>/solution.md
games/<case-id>/case-board-seed.json
games/<case-id>/asset-manifest.json
```

### Writes

```text
games/<case-id>/validation-report.md
```

### May recommend updates to

```text
docs/playtest-findings.md
docs/design-principles.md
schemas/game-package-schema.md
prompts/03-validator.md
```

### Should not directly update

```text
games/<case-id>/game-package.json
```

The Validator diagnoses. The Revision Engine repairs.

## AI Playtester role

### Reads

```text
README.md
docs/design-principles.md
docs/playtest-findings.md
prompts/04-ai-playtester.md
games/<case-id>/game-package.json
games/<case-id>/solution.md
games/<case-id>/validation-report.md
```

### Writes

```text
games/<case-id>/playtest-report.md
```

### May recommend updates to

```text
docs/playtest-findings.md
docs/design-principles.md
prompts/04-ai-playtester.md
```

### Should not directly update

```text
games/<case-id>/game-package.json
docs/playtest-findings.md
```

unless explicitly instructed.

## Revision Engine role

### Reads

```text
README.md
docs/design-principles.md
docs/playtest-findings.md
prompts/05-revision-engine.md
games/<case-id>/game-package.json
games/<case-id>/solution.md
games/<case-id>/validation-report.md
games/<case-id>/playtest-report.md
```

### Writes or updates

```text
games/<case-id>/game-package.json
games/<case-id>/solution.md
games/<case-id>/case-board-seed.json
games/<case-id>/asset-manifest.json
games/<case-id>/revision-notes.md
```

### May recommend updates to

```text
docs/playtest-findings.md
docs/design-principles.md
schemas/
prompts/
```

### Should not mark a case as approved

Approval requires validation and, ideally, AI playtesting after revision.

## Game Master role

### Reads

```text
README.md
docs/design-principles.md
prompts/06-game-master.md
games/<case-id>/game-package.json
games/<case-id>/solution.md
games/<case-id>/case-board-seed.json
games/<case-id>/asset-manifest.json
games/<case-id>/validation-report.md
games/<case-id>/playtest-report.md
```

### Writes during active gameplay

Prefer writing active play state to files such as:

```text
games/<case-id>/runtime-state.json
games/<case-id>/case-board-current.json
games/<case-id>/session-log.md
games/<case-id>/postgame-report.md
```

### May update

```text
games/<case-id>/asset-manifest.json
```

only when a new player-facing asset is generated or recorded.

### Should not directly update

```text
docs/playtest-findings.md
docs/design-principles.md
schemas/
prompts/
```

unless the user explicitly says to record a project-level finding.

## Managing `docs/playtest-findings.md`

`docs/playtest-findings.md` is a master project-level lessons document.

It should contain durable findings that affect the design of the engine, not every defect from every case.

### Appropriate entries

Add to `docs/playtest-findings.md` when a finding is broadly applicable.

Examples:

- Final reveals must answer who, why, how, and proof.
- Images must not contain hidden clues absent from text.
- Player setup must occur before authorship.
- Quick Mystery needs hard scope limits.
- Evidence provenance must be validated.
- Game Master must not invent the solution during play.

### Inappropriate entries

Do not add narrow case-specific defects.

Examples:

- `clue-004 in quick-001 was too hard to find.`
- `NPC Alice gave an inconsistent answer in scene-003.`
- `The library map asset should be renamed.`
- `The red glove clue in case-002 was confusing.`

Those belong in the case's reports.

## Promotion workflow

A case-specific issue may be promoted to a project-level finding only when one of these is true:

1. The issue appears in multiple cases.
2. The issue reveals a missing schema requirement.
3. The issue reveals a missing prompt instruction.
4. The issue affects the Game Master architecture.
5. The user explicitly marks it as a project-level lesson.
6. The issue would likely recur unless the system is changed.

### Promotion path

Use this path:

```text
Case issue found
  -> games/<case-id>/playtest-report.md or validation-report.md
  -> games/<case-id>/revision-notes.md if repaired
  -> user reviews whether it is broader
  -> docs/playtest-findings.md if promoted
  -> docs/design-principles.md, schemas/, or prompts/ if it changes rules
```

## Case-level reports

Each case should maintain its own reports.

### validation-report.md

Created by the Validator.

Purpose:

- formal consistency review;
- clue closure matrix;
- timeline review;
- motive review;
- solvability review;
- pass/fail decision.

### playtest-report.md

Created by the AI Playtester.

Purpose:

- simulated player behavior;
- discoverability problems;
- dead ends;
- premature solution risks;
- Game Master stress points.

### revision-notes.md

Created by the Revision Engine.

Purpose:

- what changed;
- why it changed;
- which defects were fixed;
- remaining risks;
- files affected.

### postgame-report.md

Created after human gameplay.

Purpose:

- what happened during actual play;
- what confused the player;
- what worked;
- where the Game Master struggled;
- proposed case-level and project-level lessons.

## Asset management workflow

Each case should maintain an asset manifest.

```text
games/<case-id>/asset-manifest.json
```

The manifest should track:

- asset ID;
- title;
- type;
- associated clue, character, or location;
- discovery condition;
- text fallback;
- retrieval label;
- whether the player has seen it;
- whether it contains hidden clues.

The Game Master may add to this file during play if a new generated image or document is created.

The Game Master must not use images as the only source of essential clues.

## Runtime state workflow

The canonical game package should remain stable during play.

Use separate runtime files for changing state:

```text
games/<case-id>/runtime-state.json
games/<case-id>/case-board-current.json
games/<case-id>/session-log.md
```

Do not write discovered clues or visited locations back into `game-package.json` unless deliberately producing a revised package.

## Suggested case status workflow

Use this lifecycle:

```text
draft
  -> validation_failed
  -> validated
  -> playtest_failed
  -> playtested
  -> approved_for_human_play
  -> in_play
  -> completed
  -> archived
```

Status should be stored in `game-package.json` under `caseMetadata.status`.

## Commit discipline

When using the GitHub connector, prefer small commits with clear messages.

Examples:

```text
Add Quick Mystery setup preset
Add game package schema draft
Add validator report for quick-001
Revise quick-001 timeline and clue closure
Promote image handling finding to design principles
```

Avoid vague commit messages such as:

```text
updates
changes
fix stuff
```

## Safe update rules

Before updating an existing file:

1. Fetch the current file.
2. Preserve existing useful content.
3. Make the smallest coherent update.
4. Commit with a descriptive message.
5. Report what changed to the user.

Do not overwrite large files casually.

If a requested change is ambiguous, prefer adding a new report or notes file rather than rewriting a master document.

## Current recommended next files

The next missing files are likely:

```text
prompts/00-player-setup.md
docs/roadmap.md
```

The next missing case structure is likely:

```text
games/quick-001/
  player-config.json
  game-package.json
  solution.md
  case-board-seed.json
  asset-manifest.json
```

## Summary

Use `docs/` for durable project-level knowledge.

Use `prompts/` for reusable AI role instructions.

Use `schemas/` for shared data contracts.

Use `games/<case-id>/` for case-specific generated content, validation, playtesting, revision, runtime state, and postgame reports.

Promote lessons upward only when they change the system, not merely because one case had a defect.
