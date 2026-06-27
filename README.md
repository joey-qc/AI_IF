# AI Interactive Fiction

This repository contains the design documents, prompt modules, schemas, and future game packages for an AI-assisted interactive fiction system.

The project began as a prompt-only experiment: a user uploaded Markdown prompt files, then interacted with ChatGPT as a game master for a detective mystery. The playtest demonstrated that conversational AI can create an engaging investigative experience, but it also revealed that prompt-only improvisation is not enough to guarantee a fair, coherent mystery with a satisfying solution.

The goal of this repository is to evolve the project from a single monolithic game-master prompt into a structured, multi-phase system for generating, validating, revising, storing, and playing interactive mysteries.

## Core idea

The system should separate three jobs that were previously combined in one conversation:

1. Author the mystery.
2. Validate the mystery.
3. Run the mystery for the player.

The player-facing Game Master should not invent the mystery during gameplay. It should reveal and manage a prebuilt, validated game package.

## Current status

This repository is in early architecture/design stage.

Current foundational documents:

- `docs/project-architecture.md` - system tiers, AI roles, repositories, and workflow.
- `docs/playtest-findings.md` - lessons from the first full gameplay test.
- `docs/design-principles.md` - non-negotiable design rules for future versions.

A test file, `connector-test.md`, was created to verify ChatGPT GitHub connector write access.

## Planned repository structure

```text
AI_IF/
  README.md

  docs/
    project-architecture.md
    playtest-findings.md
    design-principles.md
    roadmap.md

  prompts/
    01-template-designer.md
    02-story-author.md
    03-validator.md
    04-ai-playtester.md
    05-revision-engine.md
    06-game-master.md

  schemas/
    game-package-schema.md
    game-package.schema.json
    character.schema.json
    clue.schema.json
    location.schema.json
    timeline.schema.json
    asset.schema.json

  games/
    case-001/
      game-package.json
      solution.md
      case-board.json
      assets/

  archive/
    v1-playtest-prompts/
      README.md
```

This structure may change as the design matures.

## Intended workflow

A future game should move through these phases:

1. Define the game package structure.
2. Author a complete mystery from that structure.
3. Validate the mystery for chronology, motive, clues, causality, and solvability.
4. Simulate playthroughs with one or more AI playtesters.
5. Feed failures back into revision.
6. Approve a game package for play.
7. Run the validated package through an AI Game Master.
8. Maintain player-facing state through a case board and asset library.

## How to use this repository in a new ChatGPT conversation

Start by asking ChatGPT to read this `README.md`, then read:

1. `docs/project-architecture.md`
2. `docs/playtest-findings.md`
3. `docs/design-principles.md`

After those files are loaded, continue work on the next required phase.

## Design stance

This project may eventually become either:

- a prompt-driven workflow using Markdown files and structured JSON; or
- a coded application that uses AI models through an API and stores game packages in this repository.

The architecture should support both paths until implementation decisions are made.
