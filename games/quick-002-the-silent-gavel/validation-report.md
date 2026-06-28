# Validation Report: The Silent Gavel

## Verdict

FAIL

## Executive Summary

The case has a complete authored solution, a coherent suspect set, bounded quick-mystery scope, no image-canon dependency, safe starting case-board state, and mostly fair clue/discovery coverage.

It does not pass validation yet. The canonical package is schema-invalid, and the final proof path needs an explicit recovered-target evidence step before the Game Master can run the accusation path cleanly.

## Structured Diagnostics Summary

| Severity | Count |
| --- | ---: |
| Blocker | 1 |
| Major | 1 |
| Minor | 1 |
| Advisory | 1 |

## Blockers

### finding-schema-type-mismatch

- Severity: blocker
- Category: schema_validity
- Affected file: `games/quick-002-the-silent-gavel/game-package.json`
- Affected IDs: all clue IDs; `evidence-display-niche`, `evidence-tea-urn`, `evidence-appeal-note`, `evidence-call-slip`

Several fields in `game-package.json` parse as JSON but do not match `schemas/game-package.schema.json`.

- Each clue uses `resolvedInFinalReveal` as a boolean, while the schema expects a string.
- Evidence items use `chainOfCustody` and `accessHistory` as strings, while the schema expects arrays of strings.

This blocks repository validation and should be repaired before playtesting.

## Major Issues

### finding-missing-recovered-target-evidence

- Severity: major
- Category: final_accusation_issue
- Affected file: `games/quick-002-the-silent-gavel/game-package.json`
- Affected IDs: `clue-tea-urn-base`, `clue-green-baize-fibers`, `evidence-tea-urn`, `rule-inspect-tea-urn`, `rule-compare-urn-baize`, `rule-accuse`

The solution depends on the missing target and hiding place, but the package models the hiding-place clue rather than the recovered target as a distinct evidence item. No typed rule currently reveals a target evidence ID or updates `recoveredEvidence` when the player opens or searches the hiding place.

Recommended repair: add a canonical evidence item for the recovered target and a typed discovery rule that reveals it when the player performs the appropriate search. The rule should update `recoveredEvidence` and preserve the existing final accusation requirements.

## Minor Issues

### finding-undefined-contradiction-ids

- Severity: minor
- Category: npc_interview_issue
- Affected file: `games/quick-002-the-silent-gavel/game-package.json`
- Affected IDs: `topic-miriam-alibi`, `topic-miriam-keys`

Some NPC interview topics cite contradiction IDs, but the package has no explicit contradiction objects, `make_theory` rules, comparison rules, or case-board guidance defining when those contradictions become player-visible. Physical clue rules cover the same logic well enough that this is not a blocker.

Recommended repair: either remove unused contradiction IDs or add explicit rules that surface those contradictions after the relevant clues are discovered.

## Advisory Recommendations

### finding-runtime-artifacts-not-started

- Severity: advisory
- Category: runtime_state_issue
- Affected files: `gm-readme.md`, `case-board-seed.json`

No `runtime-state.json` or `case-board-current.json` exists yet. This is acceptable before active play. The GM readme correctly instructs the GM to initialize from the seed board and keep hidden solution facts out of player-facing current state.

## Category-by-Category Review

| Category | Status | Notes |
| --- | --- | --- |
| Schema/structure | Fail | JSON parses, but schema type mismatches block validation. |
| Fair-play solvability | Fail | Core chain is fair, but final recovered-target proof needs explicit evidence modeling. |
| Clue coverage | Pass with warnings | Essential clues exist and have discovery paths; one recovery/proof step needs strengthening. |
| Typed discovery rules | Pass with warnings | Standard trigger types are used; final recovery should be a typed rule. |
| NPC interview consistency | Pass with warnings | Topics and boundaries exist; contradiction IDs need clearer operational handling. |
| Timeline consistency | Pass | No causal contradiction detected. |
| Motive proportionality | Pass | Motive is proportionate to the nonviolent theft/disruption. |
| Evidence provenance | Fail | Narrative provenance exists, but schema field types are invalid and target recovery is under-modeled. |
| Image/canon safety | Pass | Image mode is none and asset manifest is empty. |
| Case-board seed safety | Pass | Seed board contains only player-visible starting facts and leads. |
| Game Master readiness | Fail | GM can run most interactions, but package approval is blocked by schema and final proof modeling. |
| Final accusation path | Fail | The proof chain needs an explicit recovered-target evidence step. |

## Clue Closure Matrix

| Clue | Role | True meaning | Resolved? | Issue |
| --- | --- | --- | --- | --- |
| `clue-intact-front-lock` | essential | Explains the false locked-front assumption. | Yes | Schema type mismatch on `resolvedInFinalReveal`. |
| `clue-loose-backing` | essential | Establishes the hidden access route. | Yes | Schema type mismatch on `resolvedInFinalReveal`. |
| `clue-tea-urn-base` | essential | Establishes the hiding-place lead. | Partial | Needs recovered-target evidence/rule. |
| `clue-green-baize-fibers` | essential | Connects hiding place and display area. | Yes | Schema type mismatch on `resolvedInFinalReveal`. |
| `clue-miriam-key-mark` | essential | Links key access to the hidden access route. | Yes | Schema type mismatch on `resolvedInFinalReveal`. |
| `clue-reception-interval` | essential | Establishes the relevant opportunity window. | Yes | Schema type mismatch on `resolvedInFinalReveal`. |
| `clue-appeal-file-note` | essential | Establishes motive context. | Yes | Schema type mismatch on `resolvedInFinalReveal`. |
| `clue-roland-phone-call` | essential | Establishes timing and clears one misleading theory. | Yes | Schema type mismatch on `resolvedInFinalReveal`. |
| `clue-ink-smudge` | red herring | Misleading suspect pressure with a grounded explanation. | Yes | Schema type mismatch on `resolvedInFinalReveal`. |
| `clue-ledger-dust` | supporting | Supports an innocent movement claim. | Yes | Schema type mismatch on `resolvedInFinalReveal`. |

## Timeline Review

The true sequence is coherent: preparation occurs before the reception, the reception establishes the object as present, a brief interruption creates an opportunity window, the theft occurs within the single primary location, and the missing object is discovered moments later.

No impossible travel, access, or knowledge contradiction was detected.

## Motive Review

The motive is proportionate to the central act because the case is a nonviolent symbolic theft/disruption rather than a severe violent crime. The emotional and institutional stakes are enough for a medium quick mystery.

## Solvability Review

A careful player has a fair path through physical inspection, comparison, document reading, and NPC questioning. The proof threshold is mostly clear through `solution.proofRequiredForAccusation`.

The solvability defect is not the deduction logic itself, but the missing canonical recovery/proof step for the target. Without that evidence item and typed reveal, the GM may have to improvise a decisive proof moment.

## Game Master Readiness

The GM has good startup guidance, a safe opening board, structured NPC topics, bounded locations, and safe image instructions. The GM should not need to invent suspects, locations, or motive.

However, approval is blocked until schema mismatches are fixed and the final recovery/proof step is modeled.

## Discovery Rule Review

Discovery rules use the standard trigger vocabulary and cover the essential clue IDs. Prerequisite chains are short and fair.

The main discovery-rule gap is the lack of a typed rule that explicitly reveals the recovered target evidence and updates `recoveredEvidence`.

## NPC Interview Review

Each major NPC has structured topics, knowledge boundaries, repeat answers, and plausible omissions. `question_npc` rules reference valid NPC/topic IDs for the most important testimony.

Contradiction IDs should either be operationalized through explicit rules or removed to avoid making the GM infer case-board contradiction handling.

## Runtime Readiness Review

No runtime-state artifact exists yet, which is acceptable before gameplay. `gm-readme.md` correctly instructs the GM to initialize from `case-board-seed.json` and to use `case-board-current.json` when resuming.

## Case Board Safety Review

`case-board-seed.json` is spoiler-safe. It does not expose hidden culprit, hidden motive, hidden method, clue meanings, undiscovered evidence provenance, secret timeline events, red herring explanation, or final proof.

## Revision Inputs

Priority finding IDs:

- `finding-schema-type-mismatch`
- `finding-missing-recovered-target-evidence`

Recommended files to review:

- `games/quick-002-the-silent-gavel/game-package.json`
- `schemas/game-package.schema.json`
- `docs/discovery-rules-v1.md`
- `docs/npc-interview-model-v1.md`

## Required Revisions

1. Fix schema type mismatches in `game-package.json`.
2. Add explicit recovered-target evidence and a typed discovery rule for the recovery/proof step.

## Recommended Next Step

Run the Revision Engine next. Do not proceed to AI playtesting until the blocker and major finding are repaired.
