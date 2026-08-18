# Revision Notes: The Third Knock (`quick-005`)

**Date**: 2026-08-18  
**Role**: Revision Engine (`prompts/05-revision-engine.md`)  
**Target Package**: `games/quick-005-the-third-knock/game-package.json`  

---

## Executive Summary

Executed the Step 6D Revision Engine repair for `quick-005-the-third-knock` to align the case package with `quick_mystery` preset scope and pacing budgets specified in `docs/design-principles.md` Section 5.

All authored story facts, suspects, clues, evidence, NPC interview topics, deception/alibis, discovery rules, timeline events, and final solution logic remain **100% intact**.

---

## Repairs Performed

### 1. Formal Red-Herring Budget Realignment
- **Problem**: `scopeBudget.maxRedHerringCount` and case package declared 3 formal red herrings, whereas `docs/design-principles.md` Section 5 specifies Max 1 red herring for the `quick_mystery` preset.
- **Repair**:
  - Retained `rh-clara-fraud` (Clara Vane as fraudulent medium) as the single formal red herring (`redHerrings` array length 1).
  - Reclassified the metadata fields (`solution.redHerringIds`, `validationTargets.mustExplainRedHerringIds`, `canonicalAssetInventory.redHerringIds`, `scopeBudget.maxRedHerringCount`, `runtimeBudgets.maxRedHerrings`) to `1` / `["rh-clara-fraud"]`.
  - Set `isRedHerring: false` on `dr-inspect-cabinet`, retaining its discovery function while preserving Edmund's lesser secret under NPC interview topics (`topic-edmund-cabinet`).
  - Preserved all 3 suspects, 7 essential clues, 6 physical evidence items, 10 discovery rules, and 10 timeline events without deleting any story material or clue paths.

### 2. Maximum Expected Play-Time Realignment
- **Problem**: `scopeBudget.expectedPlayTimeMinutesMax` was set to 30 minutes, exceeding the `quick_mystery` preset upper limit of 25 minutes (`docs/design-principles.md` Section 5).
- **Repair**:
  - Updated `scopeBudget.expectedPlayTimeMinutesMax` from 30 to 25.
  - Kept `scopeBudget.expectedPlayTimeMinutesMin` at 20.
  - Preserved `caseMetadata.estimatedPlayTimeMinutes` at 25.

---

## Verification
- `python tools/validate.py games/quick-005-the-third-knock/game-package.json` $\rightarrow$ **PASS**
- All 7 clues, 3 suspects, 6 evidence items, 10 discovery rules, 10 timeline events, and canonical solution are verified intact.
