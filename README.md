# AI Interactive Fiction

This repository contains the design documents, prompt modules, schemas, and game packages for an AI-assisted interactive fiction system.

`README.md` is the authoritative bootstrap document for the repository. New AI conversations, human contributors, and Codex/local repository sessions should start here, choose the relevant role path below, and then continue into the role prompt or case files named by that path.

## Core idea

The system separates three jobs that were previously combined in one conversation:

1. Author the mystery.
2. Validate the mystery.
3. Run the mystery for the player.

The player-facing Game Master should not invent the mystery during gameplay. It should reveal and manage a prebuilt, validated game package.

## Current status

This repository is in early engine-hardening stage.

Completed foundations include:

- repository architecture;
- design principles and playtest findings;
- gameplay setup and scope presets;
- game package schemas;
- Discovery Rules v1;
- Validator Diagnostics v1;
- Repository Engineer workflow for local implementation;
- role prompts for authoring, validation, playtesting, revision, and gameplay;
- Runtime Engine v2;
- Runtime Fidelity Engine v1;
- Canonical Asset and Runtime Budget Enforcement v1;
- Runtime State v1 specification and schema;
- Game Master v2.

Next work should harden the existing engine architecture and repository workflow before generating additional cases.

## Repository structure

```text
AI_IF/
  README.md

  docs/
    engine-overview.md
    project-architecture.md
    playtest-findings.md
    design-principles.md
    gameplay-setup-and-scope-presets.md
    repository-workflow.md
    runtime-engine-v2.md
    runtime-fidelity-engine-v1.md
    reverse-mystery-authoring-and-resolution-v1.md
    human-engagement-and-playability-v1.md
    canonical-assets-and-runtime-budgets-v1.md
    image-fidelity-contract-v1.md
    discovery-rules-v1.md
    npc-interview-model-v1.md
    validator-diagnostics-v1.md
    runtime-fidelity-report-v1.md
    runtime-state-v1.md
    case-board-current-v1.md

  prompts/
    00-player-setup.md
    01-repository-engineer.md
    01-template-designer.md
    02-story-author.md
    03-validator.md
    04-ai-playtester.md
    05-revision-engine.md
    06-game-master.md

  schemas/
    game-package-schema.md
    game-package.schema.json
    runtime-state.schema.json
    case-board-current.schema.json
    validation-report.schema.json
    runtime-fidelity-report.schema.json

  games/
    index.json
    <caseId>-<slug>/
      gm-readme.md
      game-package.json
      case-board-seed.json
      asset-manifest.json
      validation-report.md
      playtest-report.md
      runtime-state.json
      case-board-current.json
```

This structure may change as the design matures.

## General startup path

All roles should begin with this file, then follow the role-specific startup path below.

Core project documents:

1. `docs/project-architecture.md`
2. `docs/design-principles.md`
3. `docs/playtest-findings.md`
4. `docs/repository-workflow.md`
5. `docs/engine-overview.md`

Use `docs/repository-workflow.md` for file ownership, case naming, report locations, runtime state handling, and commit discipline.

## Role layers

AI_IF separates engine roles from the development role that manages repository implementation.

Engine roles create, validate, revise, test, and run mysteries:

- Story Author
- Validator
- AI Playtester
- Revision Engine
- Game Master

Development role:

- Repository Engineer / Codex

Codex should read `README.md` first. Before making repository changes, Codex should then read `prompts/01-repository-engineer.md` and follow its local implementation workflow.

## Role startup paths

### Repository Engineer / Codex

Use this path when implementing approved changes in the local repository.

Read:

1. `README.md`
2. `prompts/01-repository-engineer.md`
3. `docs/repository-workflow.md`
4. Any files directly named by the user
5. Any nearby docs, prompts, schemas, or case files needed to understand the requested change

The Repository Engineer manages source files and implementation. It does not act as Story Author, Validator, AI Playtester, Revision Engine, or Game Master unless explicitly instructed.

### Engine Architect

Use this path when changing durable project architecture, engine behavior, schemas, workflow rules, or role responsibilities.

Read:

1. `README.md`
2. `docs/engine-overview.md`
3. `docs/project-architecture.md`
4. `docs/design-principles.md`
5. `docs/playtest-findings.md`
6. `docs/repository-workflow.md`
7. `docs/runtime-engine-v2.md`
8. `docs/runtime-fidelity-engine-v1.md`
9. `docs/reverse-mystery-authoring-and-resolution-v1.md`
10. `docs/human-engagement-and-playability-v1.md`
11. `docs/canonical-assets-and-runtime-budgets-v1.md`
12. `docs/image-fidelity-contract-v1.md`
13. `docs/discovery-rules-v1.md`
14. `docs/npc-interview-model-v1.md`
15. `docs/validator-diagnostics-v1.md`
16. `docs/runtime-fidelity-report-v1.md`
17. `docs/runtime-state-v1.md`
18. `docs/case-board-current-v1.md`
19. `schemas/game-package.schema.json`
20. `schemas/runtime-state.schema.json`
21. `schemas/case-board-current.schema.json`
22. `schemas/validation-report.schema.json`
23. `schemas/runtime-fidelity-report.schema.json`

Then inspect whichever prompt, schema, or case files are directly affected by the requested architecture change.

### Story Author

Use this path when creating or revising authored mystery content from setup constraints.

Read:

1. `README.md`
2. `docs/design-principles.md`
3. `docs/playtest-findings.md`
4. `docs/gameplay-setup-and-scope-presets.md`
5. `docs/repository-workflow.md`
6. `docs/discovery-rules-v1.md`
7. `docs/npc-interview-model-v1.md`
8. `docs/reverse-mystery-authoring-and-resolution-v1.md`
9. `docs/human-engagement-and-playability-v1.md`
10. `docs/canonical-assets-and-runtime-budgets-v1.md`
11. `docs/image-fidelity-contract-v1.md`
12. `schemas/game-package-schema.md`
13. `schemas/game-package.schema.json`
14. `prompts/02-story-author.md`
15. `games/<caseId>-<slug>/player-config.json`, if continuing an existing setup

The Story Author writes case content but does not approve it for play.

### Validator

Use this path when checking whether a mystery package is coherent, fair, complete, and ready for playtesting or human play.

Read:

1. `README.md`
2. `docs/design-principles.md`
3. `docs/playtest-findings.md`
4. `docs/gameplay-setup-and-scope-presets.md`
5. `docs/repository-workflow.md`
6. `docs/discovery-rules-v1.md`
7. `docs/npc-interview-model-v1.md`
8. `docs/runtime-fidelity-engine-v1.md`
9. `docs/reverse-mystery-authoring-and-resolution-v1.md`
10. `docs/human-engagement-and-playability-v1.md`
11. `docs/canonical-assets-and-runtime-budgets-v1.md`
12. `docs/image-fidelity-contract-v1.md`
13. `docs/validator-diagnostics-v1.md`
14. `docs/runtime-fidelity-report-v1.md`
15. `schemas/game-package-schema.md`
16. `schemas/game-package.schema.json`
17. `schemas/validation-report.schema.json`
18. `schemas/runtime-fidelity-report.schema.json`
19. `prompts/03-validator.md`
20. `docs/case-board-current-v1.md`
21. `schemas/case-board-current.schema.json`
22. `games/<caseId>-<slug>/game-package.json`
23. `games/<caseId>-<slug>/solution.md`, if canonical or required by the case handoff
24. `games/<caseId>-<slug>/case-board-seed.json`
25. `games/<caseId>-<slug>/asset-manifest.json`

The Validator diagnoses. The Revision Engine repairs.

### AI Playtester

Use this path when simulating player investigation against a drafted or validated case.

Read:

1. `README.md`
2. `docs/design-principles.md`
3. `docs/playtest-findings.md`
4. `docs/repository-workflow.md`
5. `docs/runtime-fidelity-engine-v1.md`
6. `docs/reverse-mystery-authoring-and-resolution-v1.md`
7. `docs/human-engagement-and-playability-v1.md`
8. `docs/canonical-assets-and-runtime-budgets-v1.md`
9. `docs/image-fidelity-contract-v1.md`
10. `docs/discovery-rules-v1.md`
11. `docs/npc-interview-model-v1.md`
12. `docs/validator-diagnostics-v1.md`
13. `docs/runtime-fidelity-report-v1.md`
14. `docs/case-board-current-v1.md`
15. `schemas/case-board-current.schema.json`
16. `schemas/runtime-fidelity-report.schema.json`
17. `prompts/04-ai-playtester.md`
18. `games/<caseId>-<slug>/game-package.json`
19. `games/<caseId>-<slug>/solution.md`, if canonical or required by the case handoff
20. `games/<caseId>-<slug>/validation-report*.md`, if available

The AI Playtester tests how the case behaves in practice and reports defects.

### Revision Engine

Use this path when repairing a case based on validation, AI playtest, or human feedback.

Read:

1. `README.md`
2. `docs/design-principles.md`
3. `docs/playtest-findings.md`
4. `docs/repository-workflow.md`
5. `docs/discovery-rules-v1.md`
6. `docs/npc-interview-model-v1.md`
7. `docs/runtime-fidelity-engine-v1.md`
8. `docs/reverse-mystery-authoring-and-resolution-v1.md`
9. `docs/human-engagement-and-playability-v1.md`
10. `docs/canonical-assets-and-runtime-budgets-v1.md`
11. `docs/image-fidelity-contract-v1.md`
12. `docs/validator-diagnostics-v1.md`
13. `docs/runtime-fidelity-report-v1.md`
14. `schemas/validation-report.schema.json`
15. `schemas/runtime-fidelity-report.schema.json`
16. `docs/case-board-current-v1.md`
17. `schemas/case-board-current.schema.json`
18. `prompts/05-revision-engine.md`
19. `games/<caseId>-<slug>/game-package.json`
20. `games/<caseId>-<slug>/solution.md`, if canonical or required by the case handoff
21. `games/<caseId>-<slug>/validation-report*.md`, if available
22. `games/<caseId>-<slug>/validation-report.json`, if available
23. `games/<caseId>-<slug>/runtime-fidelity-report*.md`, if available
24. `games/<caseId>-<slug>/runtime-fidelity-report*.json`, if available
25. `games/<caseId>-<slug>/playtest-report.md`, if available
26. Any human feedback or postgame report supplied by the user

The Revision Engine should preserve intended experience while fixing defects.

### Game Master

Use this path when running a validated, repository-backed mystery for a human player.

Read:

1. `README.md`
2. `docs/design-principles.md`
3. `docs/playtest-findings.md`
4. `docs/repository-workflow.md`
5. `docs/runtime-engine-v2.md`
6. `docs/runtime-fidelity-engine-v1.md`
7. `docs/reverse-mystery-authoring-and-resolution-v1.md`
8. `docs/human-engagement-and-playability-v1.md`
9. `docs/canonical-assets-and-runtime-budgets-v1.md`
10. `docs/image-fidelity-contract-v1.md`
11. `docs/investigation-model.md`
12. `docs/discovery-rules-v1.md`
13. `docs/npc-interview-model-v1.md`
14. `docs/validator-diagnostics-v1.md`, if reviewing validation or postgame report context
15. `docs/runtime-fidelity-report-v1.md`, if reviewing or producing post-session QA
16. `docs/image-system-v2.md`
17. `docs/case-board-v2.md`
18. `docs/runtime-state-v1.md`
19. `docs/case-board-current-v1.md`
20. `docs/runtime-self-checks.md`
21. `schemas/runtime-state.schema.json`
22. `schemas/case-board-current.schema.json`
23. `schemas/runtime-fidelity-report.schema.json`, if producing post-session QA
24. `prompts/06-game-master.md`
25. `games/index.json`
26. `games/<caseId>-<slug>/gm-readme.md`
27. `games/<caseId>-<slug>/game-package.json`
28. `games/<caseId>-<slug>/case-board-seed.json`
29. `games/<caseId>-<slug>/case-board-current.json`, if resuming active play
30. `games/<caseId>-<slug>/asset-manifest.json`
31. `games/<caseId>-<slug>/validation-report*.md`, if available
32. `games/<caseId>-<slug>/playtest-report.md`, if available
33. `games/<caseId>-<slug>/runtime-fidelity-report*.md`, if available
34. `games/<caseId>-<slug>/runtime-state.json`, if resuming active play

If `gm-readme.md` identifies a canonical source, follow it. Do not rely on stale companion files unless the case handoff says they are canonical.

Runtime player-session state is governed by:

```text
docs/runtime-state-v1.md
schemas/runtime-state.schema.json
```

Runtime state belongs in:

```text
games/<caseId>-<slug>/runtime-state.json
```

Current player-facing case board state is governed by:

```text
docs/case-board-current-v1.md
schemas/case-board-current.schema.json
```

The current case board belongs in:

```text
games/<caseId>-<slug>/case-board-current.json
```

Do not write player progress back into `game-package.json`.

## Intended workflow

A future game should move through these phases:

1. Define or select the game package structure.
2. Capture player setup and scope constraints.
3. Author a complete mystery from that structure.
4. Validate the mystery for chronology, motive, clues, causality, and solvability.
5. Simulate playthroughs with one or more AI playtesters.
6. Feed failures back into revision.
7. Approve a game package for play.
8. Run the validated package through an AI Game Master.
9. Maintain player-facing state through runtime state, case board, session log, and asset library files.

## Design stance

This project may eventually become either:

- a prompt-driven workflow using Markdown files and structured JSON; or
- a coded application that uses AI models through an API and stores game packages in this repository.

The architecture should support both paths until implementation decisions are made.
