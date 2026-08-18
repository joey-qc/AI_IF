# AI Interactive Fiction

Welcome to the **AI Interactive Fiction (AI_IF)** repository.

This repository contains the durable architecture specifications, machine JSON schemas, operational role prompts, and case package data for a repository-backed interactive mystery system.

`README.md` is the authoritative bootstrap router for the project. When starting a session without an assigned role prompt, start here to navigate to your role. Once an AI role is explicitly invoked with its operational prompt, it loads only its minimal startup contract and does not reread `README.md`.

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

> Note: Machine schemas are validated via tooling and are not loaded as conversational prose reading during role startup.

### 3. Operational Prompts (`prompts/`)
Instructions for AI execution of specific roles:
- `prompts/00-player-setup.md` - Player Setup role.
- `prompts/01-repository-engineer.md` - Repository Engineer (local Codex implementation).
- `prompts/02-story-author.md` - Story Author role.
- `prompts/03-validator.md` - Validator role.
- `prompts/04-ai-playtester.md` - AI Playtester role.
- `prompts/05-revision-engine.md` - Revision Engine role.
- `prompts/06-game-master.md` - Game Master role.

> Note: `prompts/01-template-designer.md` is deprecated and non-operational.

### 4. Case Data (`games/<caseId>-<slug>/`)
Case packages and session state:
- `games/index.json` - Master catalog of all cases.
- `games/<caseId>-<slug>/game-package.json` - Canonical case truth.
- `games/<caseId>-<slug>/gm-readme.md` - Case readiness handoff.
- `games/<caseId>-<slug>/runtime-state.json` - Session state during active play.
- `games/<caseId>-<slug>/case-board-current.json` - Player-facing investigation board during active play.

---

## Minimal Role Startup Routing

Roles operate under a **minimum necessary context** model. Once invoked with an operational prompt, a role loads only its designated minimal startup contract:

### Repository Engineer / Local Developer
- **Operational Prompt**: `prompts/01-repository-engineer.md`
- **Always Required Spec**: `docs/repository-workflow.md`
- **Conditionally Required**: `docs/design-principles.md` (authoring rules), `docs/runtime-engine-v2.md` (runtime rules)
- **Machine Checks**: `schemas/*.schema.json` (when maintaining schemas/tooling)

### Player Setup
- **Operational Prompt**: `prompts/00-player-setup.md`
- **Always Required Spec**: `docs/design-principles.md`
- **Conditionally Required**: `games/index.json` (to verify case ID uniqueness or select case)
- **Machine Checks**: `schemas/game-package.schema.json`

### Story Author
- **Operational Prompt**: `prompts/02-story-author.md`
- **Always Required Spec**: `docs/design-principles.md`
- **Case-Specific Inputs**: `games/<case>/player-config.json` or setup constraints
- **Machine Checks**: `schemas/game-package.schema.json`

### Validator
- **Operational Prompt**: `prompts/03-validator.md`
- **Always Required Spec**: `docs/design-principles.md`
- **Conditionally Required**: `docs/repository-workflow.md` (catalog/readiness metadata)
- **Case-Specific Inputs**: Target draft case files (`game-package.json`, `solution.md`, etc.)
- **Machine Checks**: `schemas/game-package.schema.json`, `schemas/validation-report.schema.json`

### AI Playtester
- **Operational Prompt**: `prompts/04-ai-playtester.md`
- **Always Required Spec**: `docs/runtime-engine-v2.md`
- **Case-Specific Inputs**: Target case package (`game-package.json`), validation report if available
- **Machine Checks**: `schemas/runtime-fidelity-report.schema.json`

### Revision Engine
- **Operational Prompt**: `prompts/05-revision-engine.md`
- **Always Required Spec**: `docs/design-principles.md`
- **Conditionally Required**: `docs/runtime-engine-v2.md` (if repairing GM execution flaws)
- **Case-Specific Inputs**: Target case package (`game-package.json`), defect report (`validation-report.md`, `playtest-report.md`)
- **Machine Checks**: `schemas/game-package.schema.json`

### Game Master
- **Operational Prompt**: `prompts/06-game-master.md`
- **Always Required Spec**: `docs/runtime-engine-v2.md`
- **Case-Specific Inputs**: `games/<caseId>-<slug>/gm-readme.md`, `game-package.json`
- **Conditionally Required**: `runtime-state.json`, `case-board-current.json` (when resuming active play)
- **Machine Checks**: None (interprets authored case package)
