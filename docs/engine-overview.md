# AI_IF Engine Overview

## Purpose

This is the primary entry point for the AI_IF repository. New AI conversations and new contributors should begin here.

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

## Core Specifications

Read in this order:

1. project-architecture.md
2. design-principles.md
3. repository-workflow.md
4. runtime-engine-v2.md
5. investigation-model.md
6. image-system-v2.md
7. case-board-v2.md
8. runtime-self-checks.md

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

Next milestone:

Review the engine architecture before generating `quick-002`.
