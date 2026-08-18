# Validation Report: The Third Knock (`quick-005`)

**Report ID**: `valrep-quick-005-2026-08-18`  
**Case ID**: `quick-005`  
**Validation Date**: 2026-08-18  
**Validator Role Version**: `v2.0-simplified`  
**Overall Verdict**: **PASS WITH WARNINGS** (`pass_with_warnings`)  

---

## Executive Summary

Independent revalidation of case `quick-005-the-third-knock` under the simplified AI_IF Validator workflow (`prompts/03-validator.md`).

The case package:
1. **Passes deterministic structural schema validation** via `tools/validate.py` against `schemas/game-package.schema.json`.
2. **Satisfies pre-runtime mystery design principles** in `docs/design-principles.md`:
   - Complete Final Resolution Contract (culprit Lydia Harrow, motive, method, opportunity, means, culprit mistake, proof chain).
   - Solvability and fair evidence provenance across all essential clues, including discoverable motive evidence (`clue-beatrice-note`, `ev-beatrice-note`).
   - Proportional motive involving correspondence manipulation and imminent exposure.
   - Bounded red herrings (`rh-clara-fraud`, `rh-edmund-heir`, `rh-supernatural`) clearable via discovery rules and NPC questioning.
3. **Scope Budget Evaluation**:
   - Primary locations: 1 (meets `quick_mystery` budget).
   - Major NPCs / suspects: 3 (meets `quick_mystery` budget).
   - Essential clues: 7 (meets `quick_mystery` budget).
   - Red herrings: 3 (exceeds `quick_mystery` preset limit of 1 - recorded as Minor finding).
   - Expected play time: 20-30 min (max 30 min slightly exceeds `quick_mystery` 25 min limit - recorded as Advisory finding).

Zero Blocker or Major defects exist.

---

## Verification Checks Summary

| Check ID | Category | Status | Summary |
| :--- | :--- | :--- | :--- |
| `chk-schema-validity` | `schema_validity` | **PASS** | `game-package.json` passes deterministic structural validation via `tools/validate.py`. |
| `chk-solvability-contract` | `missing_clue_path` | **PASS** | Final Resolution Contract proof clues are complete and reachable via typed discovery rules. |
| `chk-motive-proportionality` | `weak_motive` | **PASS** | Culprit Lydia Harrow has a clear, proportional motive supported by discoverable evidence. |
| `chk-red-herring-discipline` | `unfair_discovery_path` | **PASS** | All three red herrings are bounded and clearable via questioning and evidence. |
| `chk-scope-budget` | `scope_pacing_issue` | **PASS WITH WARNINGS** | Quick mystery scope budget observed for locations and suspects, but contains 3 red herrings (preset max 1) and 30 min max play time (preset max 25 min). |
| `chk-metadata-consistency` | `runtime_state_issue` | **PASS** | Case metadata status values are valid current enum values in `schemas/game-package.schema.json`. |

---

## Findings

### Minor Findings

- **`find-001-red-herring-count-exceeds-quick-preset-limit`**: Red herring count exceeds `quick_mystery` preset maximum.
  - **Category**: `scope_pacing_issue`
  - **Description**: `scopeBudget` and case package author 3 red herrings (`rh-clara-fraud`, `rh-edmund-heir`, `rh-supernatural`). Under `docs/design-principles.md` Section 5, `quick_mystery` preset specifies Max 1 red herring. All 3 red herrings are fully bounded and clearable, so this does not block playability or solvability.
  - **Affected File**: `games/quick-005-the-third-knock/game-package.json` (`/scopeBudget/maxRedHerringCount`)

### Advisory Findings

- **`find-002-play-time-range-exceeds-quick-preset-max`**: Max expected play time exceeds `quick_mystery` upper bound.
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

- **Recommended Next Role**: `ai_playtester` (AI Playtester)
- **Revision Priority**: Low (No Blocker or Major defects; case is clearable and fully solvable).
