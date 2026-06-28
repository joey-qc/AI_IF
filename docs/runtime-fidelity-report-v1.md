# Runtime Fidelity Report v1

## Purpose

Runtime Fidelity Report v1 defines a standardized post-playtest or post-session audit report for AI_IF cases.

The report compares what happened during runtime against the authored game package so runtime drift can be detected, diagnosed, and repaired.

Runtime Fidelity Reports are QA artifacts. They are not canonical game truth.

## Report Location

Runtime fidelity reports belong in the relevant case folder:

```text
games/<case-folder>/runtime-fidelity-report.md
games/<case-folder>/runtime-fidelity-report.json
```

Versioned equivalents may be used when multiple sessions are audited:

```text
games/<case-folder>/runtime-fidelity-report-v2.md
games/<case-folder>/runtime-fidelity-report-v2.json
```

The structured JSON report should follow:

```text
schemas/runtime-fidelity-report.schema.json
```

## Spoiler Status

Runtime Fidelity Reports may contain spoilers.

They may reference culprit, method, motive, clue meanings, final proof, missed clues, invented content, and final reveal behavior.

Players who want a spoiler-free experience should not read these reports before play.

## Inputs

A Runtime Fidelity Report should compare:

- authored `game-package.json`;
- `canonicalAssetInventory`;
- `runtimeBudgets`;
- `case-board-seed.json`;
- `asset-manifest.json`;
- validation and playtest reports when relevant;
- session log or transcript;
- `runtime-state.json`;
- `case-board-current.json`;
- postgame report, if present.

The report should cite canonical IDs rather than duplicating large story content.

## Required Comparisons

The report should compare authored package contents against actual runtime investigation, including:

- NPCs introduced during play;
- locations introduced during play;
- objects introduced during play;
- evidence and documents introduced during play;
- clues revealed during play;
- discovery rules fired;
- NPC interview topics used;
- case-board-current updates;
- runtime-state updates;
- images generated or shown;
- final accusation and final reveal behavior;
- canonical asset inventory compliance;
- runtime budget usage;
- background character handling;
- final solution fidelity.

## Fidelity Status

Use these overall statuses:

```text
pass
pass_with_warnings
fail
not_evaluated
```

Use `pass` only when no runtime drift affected play.

Use `pass_with_warnings` when small issues occurred but did not change the mystery, proof, or player-facing canon.

Use `fail` when the Game Master invented investigative content, changed the solution, exceeded hard budgets, exposed hidden facts prematurely, or relied on unauthored content.

## Finding Severity

Use these severity levels:

```text
blocker
major
minor
advisory
```

### blocker

Runtime drift made the session untrustworthy or replay-blocking.

Examples:

- invented culprit, method, motive, or proof;
- invented decisive evidence;
- final reveal contradicted the package;
- background character became a decisive witness;
- hard runtime budget was exceeded in a way that changed the investigation.

### major

Runtime drift damaged fairness or continuity but may not invalidate the entire session.

Examples:

- invented non-decisive clue path;
- missed essential authored content;
- NPC gave unauthored testimony;
- case board treated theory as fact;
- image added a clue-like object.

### minor

Runtime issue should be corrected but did not threaten the solution.

Examples:

- runtime state missed a repeated action;
- case-board wording was ambiguous;
- optional authored asset was not tracked.

### advisory

Useful observation or preventive recommendation.

## Finding Categories

Recommended categories:

```text
invented_npc
invented_location
invented_object
invented_evidence
invented_document
invented_clue
invented_discovery_path
missed_canonical_content
discovery_rule_mismatch
npc_interview_mismatch
case_board_drift
runtime_state_drift
image_fidelity_issue
budget_violation
canonical_inventory_violation
background_character_violation
final_solution_mismatch
premature_reveal
other
```

## Canonical Asset Checks

The report should identify whether runtime introduced or used assets outside `canonicalAssetInventory`.

Check:

- NPC IDs;
- location IDs;
- object IDs;
- evidence IDs;
- document IDs;
- image IDs;
- discovery rule IDs;
- interview topic IDs;
- scene IDs;
- clue IDs.

If an asset appeared only as non-investigative atmosphere, record that distinction.

## Runtime Budget Checks

The report should compare runtime usage against `runtimeBudgets`.

Check:

- major NPCs;
- interviewable NPCs;
- background characters;
- primary and secondary locations;
- searchable objects;
- evidence items;
- documents;
- images;
- discovery rules;
- red herrings;
- interview topics;
- hints;
- player-facing branches.

Hard-budget violations should normally be major or blocker findings.

## Invented Content Findings

Invented content findings should identify runtime elements that were not authored and affected investigation.

Examples:

- a new witness;
- a new searchable object;
- a new document;
- a new evidence item;
- an unauthored clue interpretation;
- an unauthored physical access route;
- an invented branch or lead.

## Missed Canonical Content Findings

Missed canonical content findings identify authored assets that should have appeared or been tracked but did not.

Examples:

- a discovery rule should have fired but did not;
- an NPC interview topic was skipped or answered from improvisation instead;
- recovered evidence was not recorded in runtime state;
- case-board-current omitted a key player-visible discovery.

## Final Solution Fidelity

The report should check whether the final accusation and reveal stayed faithful to:

- culprit;
- motive;
- method;
- timeline;
- clue meanings;
- evidence provenance;
- red herring explanation;
- final proof threshold.

The final reveal must not introduce new decisive facts absent from the authored package.

## Recommended Repairs

Recommended repairs should distinguish:

- package gaps that encouraged improvisation;
- Game Master instruction failures;
- runtime-state tracking gaps;
- case-board update defects;
- image prompt/generation defects;
- validation or playtest coverage gaps.

Repairs should feed the Revision Engine or prompt/schema updates as appropriate.

## Role Responsibilities

### Game Master

During normal play, maintain enough session, runtime-state, case-board, and image-state detail to support later reporting. Do not reveal spoiler report contents to the player.

In a playtest or evaluation context, produce or support a Runtime Fidelity Report after the session when requested.

### AI Playtester

After playtesting, produce or request a Runtime Fidelity Report that covers runtime drift, invented content, missed authored content, budget violations, image fidelity, and final solution fidelity.

### Validator

Before play, check whether the package has stable IDs, canonical inventory, runtime budgets, typed discovery rules, NPC interview topics, and case-board structure sufficient to support future Runtime Fidelity Reports.

### Revision Engine

Consume Runtime Fidelity Reports and prioritize repairs to runtime drift, invented assets, package gaps that encouraged improvisation, and Game Master instruction failures.

## Relationship to Other Reports

Validation reports diagnose whether the authored package is ready before play.

Playtest reports diagnose whether the case works in simulated interaction.

Runtime Fidelity Reports diagnose whether the runtime session stayed faithful to the authored package.

These reports may reference each other, but they should remain separate artifacts.
