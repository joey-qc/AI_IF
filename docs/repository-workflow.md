# Repository Workflow

## Purpose

This document defines how repository files should be managed across the AI Interactive Fiction project.

The project uses GitHub as persistent shared storage for architecture documents, prompt modules, schemas, generated game packages, validation reports, playtest reports, revision notes, runtime state, assets, and postgame findings.

The goal is to prevent the repository from becoming disorganized as multiple AI roles create and update files over time.

## Core rule

Separate project-level knowledge from case-level knowledge.

```text
Project-level lesson -> docs/
Case-specific issue  -> games/<caseId>-<slug>/
```

The master documents in `docs/` should evolve slowly and intentionally.

Per-game files under `games/<caseId>-<slug>/` should capture the setup, authored package, hidden solution, validation, playtesting, revisions, runtime state, assets, and postgame findings for one specific story.

## Case identity and naming

Every authored game/story must have three identity fields.

### caseId

A stable machine-friendly identifier.

Examples:

```text
quick-001
one-001
standard-001
extended-001
```

Rules:

- must be unique in the repository;
- should not change after creation;
- should not depend on the final title;
- should be used for references, reports, commits, and internal IDs.

### title

A human-friendly story title.

Examples:

```text
The Case of the Missing Melody
The Clock in the Locked Study
The Vanishing Guest at Table Three
```

Rules:

- should be memorable;
- may be changed before final approval;
- should be shown in game menus, setup summaries, and postgame reports;
- should be stored in `caseMetadata.title`.

### slug

A URL/file-safe version of the title.

Examples:

```text
the-missing-melody
the-clock-in-the-locked-study
the-vanishing-guest-at-table-three
```

Rules:

- lowercase;
- words separated by hyphens;
- no spaces;
- no punctuation except hyphens;
- should be stored in `caseMetadata.slug`.

## Game folder naming convention

Each game folder should use this format:

```text
games/<caseId>-<slug>/
```

Example:

```text
games/quick-001-the-clock-in-the-locked-study/
```

Rationale:

- `caseId` keeps references stable.
- `slug` makes the folder readable.
- The folder remains manageable even when many games exist.

If the title changes after folder creation, do not automatically rename the folder unless the user requests it. Prefer stable paths over cosmetic renames.

## Game library index

The repository should maintain a game library index:

```text
games/index.json
```

Purpose:

- list all authored games;
- make games browsable by title;
- track status, difficulty, length, and folder path;
- help future ChatGPT conversations locate available games quickly.

Recommended structure:

```json
[
  {
    "caseId": "quick-001",
    "title": "The Clock in the Locked Study",
    "slug": "the-clock-in-the-locked-study",
    "folder": "games/quick-001-the-clock-in-the-locked-study",
    "lengthPreset": "quick_mystery",
    "difficulty": "easy",
    "genre": "classic detective",
    "tone": "lighthearted",
    "status": "draft",
    "validationStatus": "not_validated",
    "playtestStatus": "not_playtested",
    "lastUpdatedAt": "",
    "notes": ""
  }
]
```

Update `games/index.json` when a new case is created, renamed, approved, completed, archived, or materially revised.

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
prompts/01-repository-engineer.md
prompts/01-template-designer.md
prompts/02-story-author.md
prompts/03-validator.md
prompts/04-ai-playtester.md
prompts/05-revision-engine.md
prompts/06-game-master.md
```

These files should change when the workflow changes, not every time a game is generated.

### Repository Engineer implementation conventions

`prompts/01-repository-engineer.md` defines the local Codex implementation workflow.

The Repository Engineer is a development role, not an engine role. It reads the local repository, implements approved changes, edits files, runs available checks, shows diffs before commits, creates focused commits after approval, and pushes only when instructed.

Engine roles create, validate, revise, test, and run mysteries. The Repository Engineer manages source files and should not generate mystery content unless explicitly instructed.

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

Each authored game should have its own folder.

Example:

```text
games/quick-001-the-clock-in-the-locked-study/
  setup.md
  player-config.json
  game-package.json
  solution.md
  case-board-seed.json
  asset-manifest.json
  validation-report.md
  playtest-report.md
  revision-notes.md
  runtime-state.json
  case-board-current.json
  session-log.md
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
docs/repository-workflow.md
games/index.json
```

### Writes

```text
games/<caseId>-<slug>/setup.md
games/<caseId>-<slug>/player-config.json
games/index.json
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
docs/repository-workflow.md
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
games/<caseId>-<slug>/game-package.json
```

The Template Designer defines structure; it does not author cases.

## Story Author role

### Reads

```text
README.md
docs/design-principles.md
docs/playtest-findings.md
docs/gameplay-setup-and-scope-presets.md
docs/repository-workflow.md
schemas/game-package-schema.md
schemas/game-package.schema.json
prompts/02-story-author.md
games/<caseId>-<slug>/player-config.json
```

### Writes

```text
games/<caseId>-<slug>/game-package.json
games/<caseId>-<slug>/solution.md
games/<caseId>-<slug>/case-board-seed.json
games/<caseId>-<slug>/asset-manifest.json
games/<caseId>-<slug>/author-notes.md
games/index.json
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
docs/repository-workflow.md
schemas/game-package-schema.md
schemas/game-package.schema.json
prompts/03-validator.md
games/<caseId>-<slug>/game-package.json
games/<caseId>-<slug>/solution.md
games/<caseId>-<slug>/case-board-seed.json
games/<caseId>-<slug>/asset-manifest.json
```

### Writes

```text
games/<caseId>-<slug>/validation-report.md
games/index.json
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
games/<caseId>-<slug>/game-package.json
```

The Validator diagnoses. The Revision Engine repairs.

## AI Playtester role

### Reads

```text
README.md
docs/design-principles.md
docs/playtest-findings.md
docs/repository-workflow.md
prompts/04-ai-playtester.md
games/<caseId>-<slug>/game-package.json
games/<caseId>-<slug>/solution.md
games/<caseId>-<slug>/validation-report.md
```

### Writes

```text
games/<caseId>-<slug>/playtest-report.md
games/index.json
```

### May recommend updates to

```text
docs/playtest-findings.md
docs/design-principles.md
prompts/04-ai-playtester.md
```

### Should not directly update

```text
games/<caseId>-<slug>/game-package.json
docs/playtest-findings.md
```

unless explicitly instructed.

## Revision Engine role

### Reads

```text
README.md
docs/design-principles.md
docs/playtest-findings.md
docs/repository-workflow.md
prompts/05-revision-engine.md
games/<caseId>-<slug>/game-package.json
games/<caseId>-<slug>/solution.md
games/<caseId>-<slug>/validation-report.md
games/<caseId>-<slug>/playtest-report.md
```

### Writes or updates

```text
games/<caseId>-<slug>/game-package.json
games/<caseId>-<slug>/solution.md
games/<caseId>-<slug>/case-board-seed.json
games/<caseId>-<slug>/asset-manifest.json
games/<caseId>-<slug>/revision-notes.md
games/index.json
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
docs/repository-workflow.md
prompts/06-game-master.md
games/index.json
games/<caseId>-<slug>/game-package.json
games/<caseId>-<slug>/solution.md
games/<caseId>-<slug>/case-board-seed.json
games/<caseId>-<slug>/asset-manifest.json
games/<caseId>-<slug>/validation-report.md
games/<caseId>-<slug>/playtest-report.md
```

### Writes during active gameplay

Prefer writing active play state to files such as:

```text
games/<caseId>-<slug>/runtime-state.json
games/<caseId>-<slug>/case-board-current.json
games/<caseId>-<slug>/session-log.md
games/<caseId>-<slug>/postgame-report.md
games/index.json
```

### May update

```text
games/<caseId>-<slug>/asset-manifest.json
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
- Each authored game needs a stable `caseId`, human-friendly title, slug, and folder.

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
  -> games/<caseId>-<slug>/playtest-report.md or validation-report.md
  -> games/<caseId>-<slug>/revision-notes.md if repaired
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
games/<caseId>-<slug>/asset-manifest.json
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
games/<caseId>-<slug>/runtime-state.json
games/<caseId>-<slug>/case-board-current.json
games/<caseId>-<slug>/session-log.md
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

Status should be stored in `game-package.json` under `caseMetadata.status` and mirrored in `games/index.json`.

## Commit discipline

When using the GitHub connector, prefer small commits with clear messages.

Examples:

```text
Add Quick Mystery setup preset
Add game package schema draft
Add validator report for quick-001
Revise quick-001 timeline and clue closure
Add game library index
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

The next missing project file is likely:

```text
docs/roadmap.md
```

The next missing game library file is:

```text
games/index.json
```

The next missing case structure is likely:

```text
games/quick-001-the-clock-in-the-locked-study/
  setup.md
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

Use `games/index.json` for the human-friendly game library.

Use `games/<caseId>-<slug>/` for one complete authored story, including setup, game package, validation, playtesting, revision, runtime state, assets, and postgame reports.

Promote lessons upward only when they change the system, not merely because one case had a defect.
