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
4. workflow-and-case-readiness-v1.md
5. runtime-engine-v2.md
6. runtime-fidelity-engine-v1.md
7. reverse-mystery-authoring-and-resolution-v1.md
8. human-engagement-and-playability-v1.md
9. human-playtest-review-template-v1.md
10. player-agency-and-fair-evidence-v1.md
11. canonical-assets-and-runtime-budgets-v1.md
12. image-fidelity-contract-v1.md
13. discovery-rules-v1.md
14. npc-interview-model-v1.md
15. validator-diagnostics-v1.md
16. runtime-fidelity-report-v1.md
17. investigation-model.md
18. image-system-v2.md
19. case-board-v2.md
20. runtime-state-v1.md
21. case-board-current-v1.md
22. runtime-self-checks.md

## Case Readiness

AI_IF separates case existence from play readiness. A game package may be implemented under `games/` but still remain draft, unvalidated, or unplaytested.

A case becomes ready for human play only after validation, revision, AI playthrough, final validation, and metadata confirmation.

The engine treats validation, AI playtest, runtime fidelity, and human playtest reports as working artifacts that must feed Revision Engine work.

Case readiness and blessed package discipline are governed by:

```text
docs/workflow-and-case-readiness-v1.md
```

Human playtest review is governed by:

```text
docs/human-playtest-review-template-v1.md
```

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

## Runtime Fidelity Contract

Runtime fidelity is governed by:

```text
docs/runtime-fidelity-engine-v1.md
```

The Game Master is an interpreter of the authored package, not a co-author during play.

The Game Master may improvise surface narration, ordinary atmosphere, and natural phrasing. It must not invent suspects, witnesses, evidence, clue paths, locations, documents, solution mechanics, timeline events, physical access routes, motives, alibis, or final proof.

If the player asks about unauthored content, the Game Master should answer with a natural negative or redirect response, update runtime state or case-board state only with player-visible negative investigation when appropriate, and return to authored leads.

When authored investigative content is exhausted, the Game Master should transition to deduction mode rather than inventing additional leads.

## Reverse Authoring and Final Resolution Contract

Reverse mystery authoring and final resolution completeness are governed by:

```text
docs/reverse-mystery-authoring-and-resolution-v1.md
```

Canonical truth and a complete final resolution must exist before runtime. The Story Author works from what actually happened, proof, timeline, and suspect clearance outward into scenes, NPC dialogue, images, red herrings, and gameplay flow.

The Game Master must be able to explain the full canonical solution from authored package data. Missing culprit, motive, method, opportunity, timeline, proof chain, red herring explanation, suspect clearance, endgame explanation, or fallback solution reveal is an authoring and validation failure, not a runtime problem to improvise around.

## Human Engagement and Playability Contract

Human engagement and playability are governed by:

```text
docs/human-engagement-and-playability-v1.md
```

Logical solvability is not enough. Cases must also pass engagement and playability expectations: concrete human conflict, emotionally legible stakes, non-generic motive mechanics, plain-language handling of specialized mechanisms, neutral recaps, and voice-safe clarification when player input is ambiguous.

## Player Agency and Fair Evidence Contract

Player agency and fair evidence are governed by:

```text
docs/player-agency-and-fair-evidence-v1.md
```

Fair play requires stable observable evidence and player inference protection. When the player fairly inspects available evidence, ordinary observable details should appear then, not retroactively after the explanatory fact is known.

The Game Master should distinguish observation, witness claim, document statement, possible meaning, and final proof synthesis. Case-board updates, recaps, spatial summaries, and images must not smuggle interpretation or culprit-pointing analysis into neutral investigation mode.

## Canonical Asset and Budget Contract

Canonical asset and runtime budget enforcement is governed by:

```text
docs/canonical-assets-and-runtime-budgets-v1.md
schemas/game-package.schema.json
```

`game-package.json` defines what exists in the mystery.

`canonicalAssetInventory` lists investigative assets the runtime may expose, including authored NPCs, locations, objects, evidence, documents, images, discovery rules, interview topics, scenes, clues, and red herrings.

`runtimeBudgets` define maximum runtime scope. The Game Master cannot exceed those budgets or invent investigative assets during play.

Background atmosphere is allowed only when it remains non-investigative. Background characters, descriptive objects, incidental writing, and flavor props cannot become witnesses, clues, documents, evidence, or branches unless authored in the package.

## Image Fidelity Contract

Image fidelity is governed by:

```text
docs/image-fidelity-contract-v1.md
schemas/game-package.schema.json
schemas/runtime-state.schema.json
schemas/runtime-fidelity-report.schema.json
```

Images are optional support for authored content. Generated or reused images must preserve canonical visual definitions, required and forbidden visible objects, physical geometry, continuity anchors, hidden-element rules, and text fallback.

Image output must not invent suspects, witnesses, evidence, clue paths, locations, objects, access routes, documents, hidden mechanisms, or solution facts. If a faithful image cannot be produced, the runtime should use text fallback rather than creating visual drift.

## Case Board Current Contract

Player-facing case board state is governed by:

```text
docs/case-board-current-v1.md
schemas/case-board-current.schema.json
```

The canonical `game-package.json` remains the source of authored mystery truth.

`case-board-seed.json` is the initial visible board at the start of play.

`case-board-current.json` is the evolving player-facing board during runtime.

`runtime-state.json` tracks broader gameplay and session state, such as turn count, current position, hints, accusation state, and compact continuity.

Do not write the current case board back into `game-package.json`.

## Discovery Rules Contract

Typed discovery rules are governed by:

```text
docs/discovery-rules-v1.md
schemas/game-package.schema.json
```

The canonical `game-package.json` remains the source of clue truth.

Discovery rules define how canonical clues, evidence, and related player-visible information become available.

`runtime-state.json` tracks which discovery rules have fired and which clue or evidence IDs the player has discovered.

`case-board-current.json` records only the player-visible results of fired rules, failed searches, theories, contradictions, and ruled-out paths.

## NPC Interview Model Contract

NPC interview data is governed by:

```text
docs/npc-interview-model-v1.md
schemas/game-package.schema.json
```

NPC interview topics are canonical authoring data inside `game-package.json`.

`runtime-state.json` tracks which NPC topics have been asked and what player-visible claims, lies, omissions, or contradictions have surfaced.

`case-board-current.json` records only player-visible NPC answers, witness statements, contradictions, and follow-up leads.

## Validator Diagnostics Contract

Validation reports are structured diagnostic artifacts governed by:

```text
docs/validator-diagnostics-v1.md
schemas/validation-report.schema.json
```

Validation reports are not canonical game truth.

They cite affected canonical IDs, summarize schema and mystery-quality checks, and inform Revision Engine work.

## Runtime Fidelity Report Contract

Runtime Fidelity Reports are post-playtest or post-session QA artifacts governed by:

```text
docs/runtime-fidelity-report-v1.md
schemas/runtime-fidelity-report.schema.json
```

They compare the authored package against actual runtime behavior, including introduced NPCs, locations, objects, evidence, documents, clues, discovery rules, NPC topics, case-board updates, runtime-state updates, images, budget use, and final reveal fidelity.

Runtime Fidelity Reports are not canonical game truth. They may contain spoilers and should feed Revision Engine repairs when runtime drift, invented assets, missed authored content, budget violations, or solution mismatches are found.

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
- Runtime Fidelity Engine v1
- Reverse Mystery Authoring and Resolution v1
- Human Engagement and Playability v1
- Workflow and Case Readiness v1
- Human Playtest Review Template v1
- Player Agency and Fair Evidence v1
- Canonical Asset and Runtime Budget Enforcement v1
- Image Fidelity Contract v1
- Runtime Fidelity Report v1
- Discovery Rules v1
- NPC Interview Model v1
- Validator Diagnostics v1
- Game Master v2
- Runtime State v1 specification and schema

Next milestone:

Review and harden the engine architecture before generating additional cases.
