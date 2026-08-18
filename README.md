# AI Interactive Fiction

Welcome to the **AI Interactive Fiction (AI_IF)** repository.

This repository contains the durable architecture specifications, machine JSON schemas, operational role prompts, and case package data for a repository-backed interactive mystery system.

`README.md` is the authoritative bootstrap router for the project. When starting a session without an assigned role prompt, start here to navigate to your role. Once an AI role is explicitly invoked with its operational prompt, it loads only its designated startup contract and does not reread `README.md`.

---

## Core Idea

AI_IF decouples authoring, validation, playtesting, revision, and gameplay into separate role phases:

1. **Author the mystery**: Define complete canonical truth before play.
2. **Validate the mystery**: Verify solvability, clue closure, timeline coherence, and proof thresholds before play.
3. **AI Playtest & Revise**: Simulate interactive play, surface defects, and repair the package.
4. **Run the mystery**: A conversational Game Master interprets the prebuilt, validated package without inventing investigative facts during play.

---

## System Architecture: Four Conceptual Layers

The repository's prose rules live in **exactly four authoritative contracts**. Machine structural constraints are governed by JSON schemas.

### 1. Authoritative Specifications (`docs/`)
- **`README.md`**: System bootstrap router and entry point.
- **`docs/repository-workflow.md`**: Sole prose authority for repository governance, case folder naming (`games/<caseId>-<slug>/`), catalog index (`games/index.json`), file ownership, canonical lifecycle states, readiness rules, and commit discipline.
- **`docs/design-principles.md`**: Sole prose authority for pre-runtime mystery design, reverse authoring, solvability, motive mechanisms, scope budgets, suspect deception, red herrings, contained whodunits, specialized test boundaries, authored player agency, and pre-runtime image definitions.
- **`docs/runtime-engine-v2.md`**: Sole prose authority for live Game Master execution, interpreter boundary (no unauthored asset invention), observation layers, typed discovery rules, NPC interview topics, negative investigation, case board & runtime state mechanics, anti-steering, deduction mode, image fidelity & recall, runtime self-checks, and post-session fidelity auditing.

### 2. Machine Structural Schemas (`schemas/`)
Sole structural authority for JSON validation:
- **`schemas/game-package.schema.json`**: Structural authority for `game-package.json`.
- **`schemas/runtime-state.schema.json`**: Structural authority for `runtime-state.json`.
- **`schemas/case-board-current.schema.json`**: Structural authority for `case-board-current.json`.
- **`schemas/validation-report.schema.json`**: Structural authority for `validation-report.json`.
- **`schemas/runtime-fidelity-report.schema.json`**: Structural authority for `runtime-fidelity-report.json`.

### 3. Operational Prompts (`prompts/`)
Instructions for AI execution of specific roles:
- `prompts/00-player-setup.md` - Player Setup role.
- `prompts/01-repository-engineer.md` - Repository Engineer (local Codex implementation).
- `prompts/02-story-author.md` - Story Author role.
- `prompts/03-validator.md` - Validator role.
- `prompts/04-ai-playtester.md` - AI Playtester role.
- `prompts/05-revision-engine.md` - Revision Engine role.
- `prompts/06-game-master.md` - Game Master role.
- `prompts/07-if-engine-manager.md` - IF Engine Manager / project architecture and pass-fail review role.

### 4. Case Data (`games/<caseId>-<slug>/`)
Case packages and session state:
- `games/index.json` - Master catalog of all cases.
- `games/<caseId>-<slug>/game-package.json` - Canonical case truth.
- `games/<caseId>-<slug>/gm-readme.md` - Case readiness handoff.
- `games/<caseId>-<slug>/runtime-state.json` - Session state during active play.
- `games/<caseId>-<slug>/case-board-current.json` - Player-facing investigation board during active play.

---

## Deterministic Validation Tooling

Structural JSON validation is performed mechanically by `tools/validate.py`:

```bash
# Install development dependency
python -m pip install -r requirements-dev.txt

# Validate all supported artifacts in games/ and check repository index consistency
python tools/validate.py --all

# Validate a single supported JSON file
python tools/validate.py games/<case>/game-package.json
```

- **JSON Schemas** define machine-readable structural constraints.
- **`tools/validate.py`** mechanically checks JSON syntax, schema conformance, and catalog index consistency.
- **AI Roles** evaluate semantic mystery quality, story solvability, and player engagement.

---

## Minimal Role Startup Routing

Roles operate under a **minimum necessary context** model. Once invoked with an operational prompt, a role loads only its designated startup contract:

### IF Engine Manager
- **Conversational Reads**: `prompts/07-if-engine-manager.md`
- **Conditional**: `docs/repository-workflow.md` (repository governance, lifecycle, file ownership, handoffs, or implementation workflow), `docs/design-principles.md` (mystery-design architecture), `docs/runtime-engine-v2.md` (runtime or Game Master architecture), applicable role prompts, schemas, repository files, diffs, commits, reports, or case artifacts only when directly relevant to the current task.

### Player Setup
- **Conversational Reads**: `prompts/00-player-setup.md`, `docs/repository-workflow.md`, `docs/design-principles.md`
- **Conditional**: `games/index.json` (when assigning/verifying case identity or working with the catalog)

### Repository Engineer / Local Developer
- **Conversational Reads**: `prompts/01-repository-engineer.md`, `docs/repository-workflow.md`, files explicitly involved in the requested task
- **Conditional**: `docs/design-principles.md` (design-authority changes), `docs/runtime-engine-v2.md` (runtime-authority changes), applicable `schemas/*.schema.json` (schema/tooling work)

### Story Author
- **Conversational Reads**: `prompts/02-story-author.md`, `docs/repository-workflow.md`, `docs/design-principles.md`, case setup / user constraints
- **Deterministic Check**: `python tools/validate.py games/<case>/game-package.json`
- **Raw Schema Fallback**: Read `schemas/game-package.schema.json` directly only if deterministic tooling cannot execute.

### Validator
- **Conversational Reads**: `prompts/03-validator.md`, `docs/repository-workflow.md`, `docs/design-principles.md`, target case files
- **Deterministic Check**: `python tools/validate.py` on `game-package.json` and `validation-report.json`
- **Raw Schema Fallback**: Read raw schemas directly only if deterministic tooling cannot execute.

### AI Playtester
- **Conversational Reads**: `prompts/04-ai-playtester.md`, `docs/repository-workflow.md`, `docs/runtime-engine-v2.md`, target case package and validation report
- **Deterministic Check**: `python tools/validate.py` on `runtime-fidelity-report.json` when produced
- **Raw Schema Fallback**: Read `schemas/runtime-fidelity-report.schema.json` directly only if deterministic tooling cannot execute.

### Revision Engine
- **Conversational Reads**: `prompts/05-revision-engine.md`, `docs/repository-workflow.md`, `docs/design-principles.md`, target package and defect reports
- **Conditional**: `docs/runtime-engine-v2.md` (when repairing runtime/GM behavior)
- **Deterministic Check**: `python tools/validate.py games/<case>/game-package.json`
- **Raw Schema Fallback**: Read `schemas/game-package.schema.json` directly only if deterministic tooling cannot execute.

### Game Master
- **Conversational Reads**: 4-file normal runtime startup: `prompts/06-game-master.md`, `docs/runtime-engine-v2.md`, `games/<caseId>-<slug>/gm-readme.md`, `games/<caseId>-<slug>/game-package.json`
- **Conditional**: `runtime-state.json` and `case-board-current.json` (when resuming active play)
- **Deterministic Check**: None during normal gameplay.
