# Revision Notes: The Silent Gavel

## Revision Goal

Address the first validation pass for `quick-002` while preserving the case ID, title, culprit, quick-mystery scope, one-location structure, NPC count, image mode, typed discovery rules, and structured NPC interview topics.

## Inputs Reviewed

- `README.md`
- `prompts/05-revision-engine.md`
- `docs/design-principles.md`
- `docs/discovery-rules-v1.md`
- `docs/npc-interview-model-v1.md`
- `docs/validator-diagnostics-v1.md`
- `schemas/game-package.schema.json`
- `schemas/validation-report.schema.json`
- `games/quick-002-the-silent-gavel/game-package.json`
- `games/quick-002-the-silent-gavel/case-board-seed.json`
- `games/quick-002-the-silent-gavel/asset-manifest.json`
- `games/quick-002-the-silent-gavel/gm-readme.md`
- `games/quick-002-the-silent-gavel/human-play-handoff.md`
- `games/quick-002-the-silent-gavel/validation-report.md`
- `games/quick-002-the-silent-gavel/validation-report.json`

## Summary of Changes

- Fixed schema type mismatches in clue closure fields.
- Fixed schema type mismatches in evidence provenance fields.
- Added a distinct recovered-target evidence item.
- Added a typed discovery rule for recovering that evidence before accusation.
- Updated final accusation gating so recovered evidence is required before successful accusation handling.
- Removed unused contradiction IDs from NPC interview topics and kept contradiction handling on existing physical clue and comparison rules.

## Validator Diagnostics Addressed

- Blocker findings addressed: 1
- Major findings addressed: 1
- Minor findings addressed: 1
- Advisory findings preserved: 1

## Remaining Risks

- The case should be revalidated before AI playtesting or human play.
- Runtime state and current case board files should still be created only when active play begins.

## Revalidation Recommendation

Run the Validator again for `quick-002`.
