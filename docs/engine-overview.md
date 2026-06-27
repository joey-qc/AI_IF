# AI_IF Engine Overview

## Purpose

`README.md` is the authoritative bootstrap entry point for the AI_IF repository. New AI conversations and new contributors should begin there, then use this document for the compact engine overview.

## Vision

AI_IF is a repository-backed interactive fiction engine that separates engine behavior from story content. Stories are authored, validated, playtested, and then run by a Game Master using canonical game packages.

## Repository Structure

- `docs/` — Permanent engine specifications.
- `prompts/` — Operational AI role prompts.
- `schemas/` — Machine-readable schemas.
- `games/` — Individual mystery packages and reports.

## Workflow

1. Player setup
2. Story authorship
3. Validation
4. AI playtest
5. Revision
6. Human play
7. Postgame review
8. Engine improvements

## Role Boundary

Engine roles create, validate, revise, test, and run mysteries:

- Story Author
- Validator
- AI Playtester
- Revision Engine
- Game Master

The Repository Engineer / Codex is a development role. It manages local source files, implements approved repository changes, runs available checks, creates focused commits, and pushes only when instructed.

The Repository Engineer is not an engine role and should not generate mystery content unless explicitly instructed.

## Core Specifications

Read in this order:

1. project-architecture.md
2. design-principles.md
3. repository-workflow.md
4. runtime-engine-v2.md
5. investigation-model.md
6. image-system-v2.md
7. case-board-v2.md
8. runtime-state-v1.md
9. runtime-self-checks.md

## Runtime State Contract

Runtime player-session state is governed by:

```text
docs/runtime-state-v1.md
schemas/runtime-state.schema.json
```

The canonical game package records what is true in the mystery.

Runtime state records what the player has seen, inspected, learned, ruled out, asked, theorized, requested, or resolved during a specific play session.

Runtime state should be stored in:

```text
games/<case-folder>/runtime-state.json
```

Do not store player progress in `game-package.json`.

## Operational Prompts

Operational prompts implement the specifications. They should reference the documents above rather than duplicate them.

Key runtime prompt:

- prompts/06-game-master.md

## Canonical Content

Each mystery lives in its own folder under `games/`.

The case's `gm-readme.md` identifies the canonical source (normally `game-package.json`). The Game Master must preserve canon and never invent core solution elements during play.

## Current Project Status

Completed:

- Repository architecture
- Story package architecture
- Authoring workflow
- Validation workflow
- AI playtesting workflow
- First successful human playthrough
- Runtime Engine v2 specifications
- Game Master v2
- Runtime State v1 specification and schema

Next milestone:

Review and harden the engine architecture before generating `quick-002`.
