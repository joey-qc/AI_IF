# Validator Diagnostics v1

## Purpose

Validator Diagnostics v1 defines the standard validation report model for AI_IF cases.

Validation diagnostics make reports consistent, comparable, and useful for the Revision Engine.

The report schema is:

```text
schemas/validation-report.schema.json
```

Case-specific validation reports belong under:

```text
games/<case-folder>/validation-report.md
games/<case-folder>/validation-report.json
games/<case-folder>/validation-report-v*.md
```

Use the repository's existing case naming when a case already has a report convention.

## Core distinction

Schema validation checks whether files match machine-readable structure.

Mystery-quality validation checks whether the authored case is fair, coherent, playable, and solvable.

A case can pass schema validation and still fail mystery-quality validation.

A validation report should identify both kinds of issue when relevant.

## Overall status

Use one of these statuses:

```text
pass
pass_with_warnings
fail
not_evaluated
```

Use `pass` only when the case is ready for the next workflow phase.

Use `pass_with_warnings` only when remaining issues do not threaten playability, solvability, or canon safety.

Use `fail` when any blocker remains or when major issues make play unfair or incoherent.

## Severity levels

Use these severity levels:

```text
blocker
major
minor
advisory
```

### blocker

The case should not proceed. The defect breaks the mystery, blocks validation, or would force the Game Master to invent core facts.

### major

The case may be repairable but is not yet safe for approval.

### minor

The issue should be fixed, but it does not block the core mystery.

### advisory

Useful guidance, polish, or risk note that does not block validation.

## Required diagnostic categories

Reports should classify findings with stable categories, including:

```text
schema_validity
factual_contradiction
missing_clue_path
unfair_discovery_path
premature_reveal
weak_motive
timeline_issue
npc_knowledge_violation
image_canon_violation
evidence_provenance_issue
runtime_state_issue
case_board_exposure_issue
discovery_rule_issue
npc_interview_issue
final_accusation_issue
scope_pacing_issue
```

Additional categories may be used when necessary, but prefer the standard vocabulary for comparable reports.

## Finding structure

Each finding should include:

```text
findingId
severity
category
title
description
affectedFiles
affectedIds
playerImpact
recommendedFix
blocksGameplay
blocksValidation
relatedFindingIds
```

`affectedIds` should cite canonical IDs rather than copying canonical content.

Useful ID references include:

- clue IDs;
- NPC IDs;
- topic IDs;
- discovery rule IDs;
- evidence IDs;
- image IDs;
- location IDs;
- object IDs;
- runtime-state fields;
- case-board fields;
- timeline event IDs.

## Coverage sections

A structured report should summarize coverage for:

- clue coverage;
- discovery rule coverage;
- NPC interview coverage;
- timeline coverage;
- evidence provenance coverage;
- image safety coverage;
- runtime readiness coverage;
- case-board safety coverage.

Coverage sections should identify what was checked, what passed, what failed, and which findings cover the failure.

## Common issue distinctions

### Factual contradiction

Two canonical facts cannot both be true.

### Missing clue path

A required clue exists, but no fair player action can discover it.

### Unfair discovery path

A clue is technically discoverable but only through unreasonable, invisible, or overly exact player phrasing.

### Premature reveal

The package, asset, case board, or Game Master guidance exposes hidden solution facts before the player earns them.

### Weak motive

The motive does not plausibly support the culprit's action.

### Timeline issue

Events, witness knowledge, object movement, or evidence creation do not fit chronologically.

### NPC knowledge violation

An NPC knows, says, hides, or contradicts something inconsistent with their role, location, motive, or timeline.

### Image/canon violation

An image contains essential evidence not present in text, contradicts the package, or reveals hidden information.

### Runtime-state issue

The Game Master would not have enough structured state to track play safely.

### Case-board exposure issue

Player-facing board state exposes hidden truth or treats theory as confirmed fact.

## Revision handoff

Validation diagnostics feed the Revision Engine.

Each blocker or major finding should include a recommended fix and enough affected IDs for targeted repair.

Reports should not rewrite the whole story unless explicitly asked.

The Validator diagnoses. The Revision Engine repairs.

## Report discipline

Reports should:

- cite affected files and IDs;
- avoid duplicating large canonical sections;
- distinguish player-visible impact from author-only issues;
- identify blocking status clearly;
- preserve case-specific defects in the case folder;
- promote project-level lessons only when they affect the broader engine.
