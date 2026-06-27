# Schema Cleanup Report — 2026-06-27

## Context

This cleanup was performed after the first human play-through of:

```text
quick-001 / The Clock in the Locked Study
```

The human player completed the case successfully. The postgame handoff identified schema/repository drift that should be resolved before generating `quick-002`.

## Files Compared

```text
schemas/game-package.schema.json
games/quick-001-the-clock-in-the-locked-study/game-package.json
```

## Issue Found

The completed `game-package.json` contained fields that reflected real workflow needs but were not yet supported by the machine-readable schema.

These included:

```text
caseMetadata.slug
caseMetadata.humanPlayStatus
caseMetadata.validationStatus = passed_with_minor_repository_issue
caseMetadata.playtestStatus = passed_with_minor_runtime_guidance
assetGenerationGuidance
assetManifest[].imagePromptGuidance
```

## Fix Applied

Updated:

```text
schemas/game-package.schema.json
```

The schema now supports:

1. `caseMetadata.slug`
2. `caseMetadata.humanPlayStatus`
3. expanded validation status values
4. expanded playtest status values
5. top-level `assetGenerationGuidance`
6. per-asset `imagePromptGuidance`
7. optional per-asset `hasBeenShownToPlayer`

## Rationale

### slug

The repository now uses human-friendly case folders:

```text
games/<caseId>-<slug>/
```

The slug must therefore be part of canonical metadata.

### humanPlayStatus

The project now distinguishes AI playtest status from actual human play-through status.

Current allowed values:

```text
not_played
in_progress
completed_once
completed_multiple
abandoned
blocked
```

### assetGenerationGuidance

The first human play-through showed that image generation can drift from canonical setting and style. The package now needs a structured place for image constraints.

### imagePromptGuidance

Individual assets may need asset-specific instructions to prevent:

- anachronistic styling;
- non-canonical props;
- hidden clue leakage;
- premature visual reveals.

## Result

The known schema drift from the first human play-through has been addressed.

## Remaining Notes

This cleanup did not generate `quick-002`.

Recommended next steps:

1. Optionally update `schemas/game-package-schema.md` with a fuller prose explanation of the new fields.
2. Optionally improve `prompts/06-game-master.md` using postgame lessons.
3. Then generate `quick-002` using the hardened schema.
