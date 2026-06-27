# Case Library and Identity Schema

## Purpose

This document defines the case identity and game library index conventions for the AI Interactive Fiction project.

It supplements `schemas/game-package-schema.md` and `schemas/game-package.schema.json`.

## Core rule

Every authored game/story must have:

- a stable `caseId`;
- a human-friendly `title`;
- a file-safe `slug`;
- a stable folder path using `games/<caseId>-<slug>/`.

## caseId

The `caseId` is the stable machine-friendly identifier.

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
- should not depend on the title;
- should be used in references, reports, commits, and internal IDs.

## title

The `title` is the human-friendly story name.

Examples:

```text
The Case of the Missing Melody
The Clock in the Locked Study
The Vanishing Guest at Table Three
```

Rules:

- should be memorable;
- should be suitable for menus and story selection;
- may be refined before final approval;
- should be stored in `caseMetadata.title`.

## slug

The `slug` is the file-safe version of the title.

Examples:

```text
the-missing-melody
the-clock-in-the-locked-study
the-vanishing-guest-at-table-three
```

Rules:

- lowercase;
- hyphen-separated;
- no spaces;
- no punctuation except hyphens;
- should be stored in `caseMetadata.slug`.

## folder

The `folder` is the repository path for the case.

Format:

```text
games/<caseId>-<slug>/
```

Example:

```text
games/quick-001-the-clock-in-the-locked-study/
```

Rules:

- should be created during Player Setup;
- should remain stable after creation;
- should not be renamed automatically if the title changes;
- should be stored in `caseMetadata.repositoryPath` and in `games/index.json`.

## Required game package metadata

Each `game-package.json` should include these identity fields in `caseMetadata`:

```json
{
  "caseMetadata": {
    "caseId": "quick-001",
    "title": "The Clock in the Locked Study",
    "slug": "the-clock-in-the-locked-study",
    "version": "0.1.0",
    "status": "draft",
    "validationStatus": "not_validated",
    "playtestStatus": "not_playtested",
    "repositoryPath": "games/quick-001-the-clock-in-the-locked-study"
  }
}
```

## Game library index

The repository should maintain:

```text
games/index.json
```

This is the human-friendly catalog of available stories.

## games/index.json structure

The index is an array of case entries.

Example:

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

## Required index fields

Each index entry should include:

- `caseId`
- `title`
- `slug`
- `folder`
- `lengthPreset`
- `difficulty`
- `genre`
- `tone`
- `status`
- `validationStatus`
- `playtestStatus`

Recommended fields:

- `lastUpdatedAt`
- `notes`
- `estimatedPlayTimeMinutes`
- `imageMode`
- `interactionMode`

## Update rules

Update `games/index.json` when:

- a new case setup is created;
- a case title changes;
- a case status changes;
- validation status changes;
- playtest status changes;
- a case is approved for human play;
- a case is completed or archived;
- a folder path changes by explicit user request.

## Role responsibility

The Player Setup role creates the initial index entry.

The Story Author may update the title, status, notes, or package metadata.

The Validator updates validation status.

The AI Playtester updates playtest status.

The Revision Engine updates status and notes after revision.

The Game Master may update runtime or completion status.

## Design rationale

A stable ID plus readable title makes the game library manageable.

The user should be able to say things like:

- "Open The Missing Melody."
- "Resume quick-001."
- "Show me all completed quick mysteries."
- "Find the story set in a 1940s townhouse."

The index makes those workflows possible without manually browsing folders.
