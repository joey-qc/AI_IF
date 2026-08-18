# Validation Report: The Third Knock (`quick-005`)

**Report ID**: `valrep-quick-005-2026-08-18`  
**Case ID**: `quick-005`  
**Validation Date**: 2026-08-18  
**Validator Role Version**: `v2.0-simplified`  
**Overall Verdict**: **FAIL** (`fail`)  

---

## Executive Summary

Independent revalidation of case `quick-005-the-third-knock` under the simplified AI_IF Validator workflow (`prompts/03-validator.md`).

The case package:
1. **Passes deterministic structural schema validation** via `tools/validate.py` against `schemas/game-package.schema.json`.
2. **Fails semantic validation against `docs/design-principles.md` Section 5** due to 1 Major scope-budget finding (`find-001-red-herring-count-exceeds-quick-preset-limit`):
   - The package contains 3 red herrings under the `quick_mystery` preset, which specifies Max 1 red herring (`docs/design-principles.md` Section 5).
   - Under `prompts/03-validator.md`, exceeding a hard preset maximum is a Major pacing/scope issue requiring overall verdict **FAIL**.

Handoff recommended to `revision_engine`.

---

## Verification Checks Summary

| Check ID | Category | Status | Summary |
| :--- | :--- | :--- | :--- |
| `chk-schema-validity` | `schema_validity` | **PASS** | `game-package.json` passes deterministic structural validation via `tools/validate.py`. |
| `chk-solvability-contract` | `missing_clue_path` | **PASS** | Final Resolution Contract proof clues are complete and reachable via typed discovery rules. |
| `chk-motive-proportionality` | `weak_motive` | **PASS** | Culprit Lydia Harrow has a clear, proportional motive supported by discoverable evidence. |
| `chk-red-herring-discipline` | `unfair_discovery_path` | **PASS** | All three red herrings are bounded and clearable via questioning and evidence. |
| `chk-scope-budget` | `scope_pacing_issue` | **FAIL** | Quick mystery scope budget contains 3 red herrings, exceeding the `quick_mystery` preset maximum of 1 (`docs/design-principles.md` Section 5). |
| `chk-metadata-consistency` | `runtime_state_issue` | **PASS** | Case metadata status values are valid current enum values in `schemas/game-package.schema.json`. |

---

## Findings

### Major Findings

- **`find-001-red-herring-count-exceeds-quick-preset-limit`**: Red herring count exceeds `quick_mystery` preset maximum.
  - **Severity**: `major`
  - **Category**: `scope_pacing_issue`
  - **Description**: `scopeBudget` and case package author 3 red herrings (`rh-clara-fraud`, `rh-edmund-heir`, `rh-supernatural`). Under `docs/design-principles.md` Section 5, `quick_mystery` preset specifies Max 1 red herring. This is a Major scope/pacing contract violation.
  - **Affected File**: `games/quick-005-the-third-knock/game-package.json` (`/scopeBudget/maxRedHerringCount`)

### Advisory Findings

- **`find-002-play-time-range-exceeds-quick-preset-max`**: Max expected play time exceeds `quick_mystery` upper bound.
  - **Severity**: `advisory`
  - **Category**: `scope_pacing_issue`
  - **Description**: `expectedPlayTimeMinutesMax` is set to 30 minutes, whereas `docs/design-principles.md` Section 5 specifies 10-25 minutes for `quick_mystery` preset.
  - **Affected File**: `games/quick-005-the-third-knock/game-package.json` (`/scopeBudget/expectedPlayTimeMinutesMax`)

---

## Coverage Section Breakdown

- **Clues**: 7 essential clues verified; 0 missing.
- **Discovery Rules**: 10 rules verified using schema-valid triggerTypes (`observe_scene`, `inspect_object`, `read_document`, `question_npc`, `accuse`).
- **NPC Interviews**: 3 suspects (Clara Vane, Edmund Hallow, Lydia Harrow) verified with bounded knowledge, topics, and alibis.
- **Timeline**: 10 event beats verified with coherent chronological sequence.
- **Evidence Provenance**: 6 physical/documentary evidence items tied to valid discovery nodes.
- **Image Safety**: 1 visual definition verified with complete text fallback (`vis-seance-parlor`).
- **Runtime Readiness**: Full canonical data present for GM execution.
- **Case Board Safety**: Initial board seed uses neutral labels without solution spoilers.

---

## Recommendation & Next Steps

- **Recommended Next Role**: `revision_engine` (Revision Engine)
- **Revision Priority**: High (1 Major scope defect must be resolved before progression to AI Playtester).
