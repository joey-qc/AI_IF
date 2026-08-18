# Repository Workflow

## Purpose

This document is the sole prose authority for repository governance, case identity, file ownership, game catalog indexing (`games/index.json`), case lifecycle vocabulary, readiness progression, handoff standards, and commit discipline for the AI Interactive Fiction project.

## Core rule

Separate project-level knowledge from case-level knowledge.

```text
Project-level lesson -> docs/
Case-specific data    -> games/<caseId>-<slug>/
```

The master documents in `docs/` evolve slowly and intentionally.

Per-game folders under `games/<caseId>-<slug>/` capture the setup, authored package, hidden solution, validation, playtesting, revisions, runtime state, assets, and postgame findings for a single mystery.

## Four-layer authority model

The project operates under four conceptual layers:

1. **`README.md`**: System bootstrap and router. Sends roles to operational prompts and authoritative specifications.
2. **`docs/repository-workflow.md`**: Sole prose authority for repository governance, lifecycle states, handoffs, and file management.
3. **`docs/design-principles.md`**: Sole prose authority for pre-runtime mystery design, reverse authoring, solvability, and fair-play rules.
4. **`docs/runtime-engine-v2.md`**: Sole prose authority for live Game Master runtime execution, interpreter boundary, and runtime fidelity.

Machine structural authority remains exclusively with JSON schemas (`schemas/*.schema.json`).

---

## Case identity and naming

Every authored game/story must maintain three stable identity fields:

### caseId

A stable, machine-friendly identifier.

Examples: `quick-001`, `quick-002`, `one-001`, `standard-001`.

Rules:
- Must be unique across the repository.
- Must not change after creation.
- Should not depend on the final story title.
- Must be used in internal references, schemas, reports, and commits.

### title

A human-friendly story title.

Examples: *The Clock in the Locked Study*, *The Second Toast*, *The Third Knock*.

Rules:
- Should be human-readable and memorable.
- May be refined during authoring or revision before final approval.
- Stored in `caseMetadata.title`.

### slug

A URL- and file-safe version of the title.

Examples: `the-clock-in-the-locked-study`, `the-second-toast`, `the-third-knock`.

Rules:
- Lowercase, words separated by hyphens, no spaces or special characters.
- Stored in `caseMetadata.slug`.

### Game folder naming convention

Each game folder uses the standard format:

```text
games/<caseId>-<slug>/
```

Example: `games/quick-001-the-clock-in-the-locked-study/`

Do not rename the folder after creation if the title changes cosmetically unless explicitly instructed by the user. Prefer path stability over cosmetic folder renames.

---

## Game library index (`games/index.json`)

The repository maintains a master catalog index of all cases at `games/index.json`.

### Purpose

- List all authored cases in the repository.
- Allow AI roles and human users to discover and inspect available cases.
- Track case metadata, length preset, difficulty, image mode, and lifecycle status.

### Authoritative index schema structure

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
    "status": "ready_for_human_play",
    "validationStatus": "passed_with_minor_issues",
    "playtestStatus": "passed_with_issues",
    "humanPlayStatus": "not_played",
    "lastUpdatedAt": "2026-06-27",
    "estimatedPlayTimeMinutes": 20,
    "imageMode": "player_requested_only",
    "interactionMode": "text_first",
    "notes": "Ready for GM."
  }
]
```

### Mandatory update triggers

Update `games/index.json` whenever:
- A new case setup is created.
- A case package title or configuration changes.
- Validation status changes.
- Playtest status changes.
- A case is marked `ready_for_human_play`.
- Active human play begins or completes.
- A case is archived or materially revised.

---

## Single canonical lifecycle vocabulary

Every case package progresses through a single, canonical lifecycle state sequence:

```text
draft -> validation_failed / validated -> playtest_failed / playtested -> ready_for_human_play -> in_play -> completed -> archived
```

### Canonical status values

- **`draft`**: Case setup or package authoring is in progress; not yet ready for validation.
- **`validation_failed`**: Package was validated and found to contain blocker or major defects requiring revision.
- **`validated`**: Package passed validation checks (or passed with minor issues); ready for AI playtest.
- **`playtest_failed`**: Package underwent AI playtest and encountered gameplay, solvability, or runtime defects requiring revision.
- **`playtested`**: Package passed AI playtest; ready for final review and approval.
- **`ready_for_human_play`**: Blessed package; all validation and playtest requirements are met. Approved for human play.
- **`in_play`**: Human gameplay session is currently active.
- **`completed`**: Human play session finished; postgame findings recorded.
- **`archived`**: Case retired or superseded by a newer version.

### Standardized metadata status fields

`schemas/game-package.schema.json` is the sole structural authority for exact allowed enum values across all case metadata fields. Every `game-package.json` (`caseMetadata`) and `games/index.json` entry uses these standardized fields:

- **`status`**: Overall lifecycle state. Governed structurally by `schemas/game-package.schema.json` (`draft`, `validation_failed`, `validated`, `playtest_failed`, `playtested`, `ready_for_human_play`, `in_play`, `completed`, `archived`).
- **`validationStatus`**: Diagnostic verdict representing validation progress. Structurally governed by `schemas/game-package.schema.json`.
- **`playtestStatus`**: Playtest verdict representing AI playthrough progress. Structurally governed by `schemas/game-package.schema.json`.
- **`humanPlayStatus`**: Human session state representing human play progress. Structurally governed by `schemas/game-package.schema.json`.

---

## Readiness progression and blessed package rules

### GitHub package is not automatically playable

A case existing under `games/` is **not** automatically ready for human play. The Game Master must inspect case metadata and `gm-readme.md` before starting play.

If a case has `status: draft`, `validationStatus: not_validated`, or `playtestStatus: not_playtested`, the Game Master must refuse to present it as ready for human play unless the user explicitly requests playing an unvalidated package.

### Blessed package definition

A case package is considered **blessed** and ready for human play only when all of the following criteria are satisfied:

1. The package files exist in the repository under `games/<caseId>-<slug>/`.
2. Package validation has passed (`validationStatus`: `passed`, `passed_with_minor_issues`, or `passed_with_minor_repository_issue`).
3. AI playthrough has passed (`playtestStatus`: `passed`, `passed_with_issues`, or `passed_with_minor_runtime_guidance`).
4. All blocker and major findings from validation and playtesting have been resolved.
5. Case metadata (`caseMetadata.status`) explicitly states `ready_for_human_play`.
6. Case `gm-readme.md` explicitly reflects readiness and identifies `game-package.json` as canonical truth.
7. No unresolved blocker or major findings remain.

### Validation before AI playthrough

Do not run an AI playtest on a known-flawed package unless the explicit purpose is to reproduce a specific reported defect.

If validation identifies material defects:
1. Revise the working package.
2. Re-validate.
3. Only then execute AI playtesting.

### Reports must be consumed

Validation reports and AI playtest reports are working artifacts. The Revision Engine must consume reports and apply repairs before asking the user to proceed. Reports must not be left unaddressed in the repository.

### Local working draft rule

Story design, validation analysis, and revision planning may be managed in temporary working state during step execution. Code/file changes should be committed to GitHub when a coherent iteration or consolidated package is ready, preventing noisy partial-patch commit logs.

---

## Case Handoff Contract (`gm-readme.md`)

Each case folder must maintain a concise handoff file at `games/<caseId>-<slug>/gm-readme.md`. It provides the Game Master with case-level readiness facts, eliminating the need for the GM to load repository-wide governance context.

### Standard `gm-readme.md` Structure
1. **Case Identity**: Case ID, Title, Slug.
2. **Canonical Package Path**: Pointer to `games/<caseId>-<slug>/game-package.json`.
3. **Readiness State**: Explicit confirmation of `status: ready_for_human_play`, validation verdict, and playtest verdict.
4. **Case-Specific Runtime Restrictions**: Specific spatial, witness, forensic, atmospheric, or topic boundaries unique to the case.
5. **Session Initialization Notes**: Specific opening narration notes or initial board setup instructions if required.

`gm-readme.md` must NOT contain general engine rules, schema definitions, or duplicated repository governance prose.

---

## File ownership by AI role

### Player Setup role (`prompts/00-player-setup.md`)
- **Reads**: `prompts/00-player-setup.md`, `docs/repository-workflow.md`, `docs/design-principles.md`; `games/index.json` (conditionally).
- **Writes**: `games/<caseId>-<slug>/setup.md`, `games/<caseId>-<slug>/player-config.json`, updates `games/index.json`.

### Story Author role (`prompts/02-story-author.md`)
- **Reads**: `prompts/02-story-author.md`, `docs/repository-workflow.md`, `docs/design-principles.md`, `schemas/game-package.schema.json`, case setup / user constraints (`games/<caseId>-<slug>/player-config.json`).
- **Writes**: `games/<caseId>-<slug>/game-package.json`, `games/<caseId>-<slug>/case-board-seed.json`, `games/<caseId>-<slug>/asset-manifest.json`, `games/<caseId>-<slug>/author-notes.md`, updates `games/index.json`.

### Validator role (`prompts/03-validator.md`)
- **Reads**: `prompts/03-validator.md`, `docs/repository-workflow.md`, `docs/design-principles.md`, `schemas/game-package.schema.json`, `schemas/validation-report.schema.json`, target case files (`game-package.json`, etc.).
- **Writes**: `games/<caseId>-<slug>/validation-report.json`, `games/<caseId>-<slug>/validation-report.md`, updates `games/index.json`.

### AI Playtester role (`prompts/04-ai-playtester.md`)
- **Reads**: `prompts/04-ai-playtester.md`, `docs/repository-workflow.md`, `docs/runtime-engine-v2.md`, target case package and validation report; `schemas/runtime-fidelity-report.schema.json` (conditionally when producing fidelity report).
- **Writes**: `games/<caseId>-<slug>/playtest-report.md`, `games/<caseId>-<slug>/runtime-fidelity-report.json`, updates `games/index.json`.

### Revision Engine role (`prompts/05-revision-engine.md`)
- **Reads**: `prompts/05-revision-engine.md`, `docs/repository-workflow.md`, `docs/design-principles.md`, `schemas/game-package.schema.json`, target package and defect reports; `docs/runtime-engine-v2.md` (conditionally).
- **Writes**: `games/<caseId>-<slug>/game-package.json`, `games/<caseId>-<slug>/case-board-seed.json`, `games/<caseId>-<slug>/asset-manifest.json`, `games/<caseId>-<slug>/revision-notes.md`, updates `games/index.json`.

### Game Master role (`prompts/06-game-master.md`)
- **Reads**: `prompts/06-game-master.md`, `docs/runtime-engine-v2.md`, `games/<caseId>-<slug>/gm-readme.md`, `games/<caseId>-<slug>/game-package.json`; active session files if resuming (`runtime-state.json`, `case-board-current.json`); state schemas conditionally if creating/persisting structured state without a validator; `docs/repository-workflow.md` conditionally if performing repo maintenance.
- **Writes**: `games/<caseId>-<slug>/runtime-state.json`, `games/<caseId>-<slug>/case-board-current.json`, `games/<caseId>-<slug>/session-log.md`, `games/<caseId>-<slug>/postgame-report.md`, updates `games/index.json`.

---

## Repository Engineer / Codex handoff standards

The Repository Engineer (`prompts/01-repository-engineer.md`) is a development role responsible for local repository file edits, checks, diff reviews, and git commits.

### Consolidated Handoff Standard

A task instruction to the Repository Engineer must specify:
- Target files allowed to be created or modified.
- Forbidden files or paths (e.g., do not touch case files during engine updates).
- Whether story content generation is allowed (default: forbidden).
- Verification commands or checks to run.
- Required report format.

### Final Report Standard

After completing repository work, the Repository Engineer must report:
- Changed files.
- Commit hash and message.
- Git working tree status (clean / dirty).
- Remote branch status (ahead / up to date).
- Confirmation that forbidden paths were not altered.

---

## Case-level report conventions

Each case folder maintains its diagnostic and QA artifacts locally:

- **`validation-report.json` / `validation-report.md`**: Pre-play formal consistency, solvability, and structural report created by the Validator.
- **`playtest-report.md`**: Interactive playtest log, simulated player path, and stress test report created by the AI Playtester.
- **`revision-notes.md`**: Changelog of repairs, defect finding IDs addressed, and re-validation notes created by the Revision Engine.
- **`runtime-fidelity-report.json` / `runtime-fidelity-report.md`**: Post-session audit comparing runtime transcript behavior against canonical package data to detect GM drift.
- **`postgame-report.md`**: Human playtest observations, player friction points, and recommendations created after active human play.

---

## Managing project-level lessons (`docs/playtest-findings.md`)

`docs/playtest-findings.md` is a master project-level lessons log. It records durable architectural findings derived from playtests that apply across all cases.

### Promotion workflow

A case-specific defect is promoted to `docs/playtest-findings.md` only when:
1. The issue recurs across multiple cases.
2. The issue reveals a gap in system design principles or runtime engine specifications.
3. The issue requires a schema or prompt update.
4. The user explicitly requests promoting the lesson.

Do not record narrow case-specific bugs (e.g., "Clue 4 in case 1 was hard to find") in `docs/playtest-findings.md`.

---

## Commit discipline

When executing repository commits:
- Use small, focused, coherent commits with descriptive messages.
- Format commit messages clearly (e.g., `Consolidate AI_IF authoritative contracts`, `Update game library index for quick-005`).
- Never use vague messages like `update`, `fix`, or `changes`.
- Verify `git status` and diffs before committing.
- Do not push commits unless explicitly instructed by the user or task workflow.
