# Game Master Readme

## Canonical Source

Use this file as the canonical game source:

```text
game-package.json
```

## Companion Files

The companion files are useful for context, but `game-package.json` controls the current approved human-play version.

## Important

Do not rely on `solution.md` for the current version. It was created during the first draft and was superseded by the canonical `solution` section inside `game-package.json` during revision.

## Current Status

```text
Approved for human play.
Validated: pass with minor repository issue.
AI playtested: pass with minor runtime guidance.
Human playtest: completed once; see postgame-report.md.
```

## Runtime Notes

- Treat `game-package.json` as canonical for culprit, motive, method, timeline, clue meanings, evidence provenance, and final proof.
- Use `case-board-seed.json` and the embedded `caseBoardSeed` only to initialize player-facing state.
- Use `asset-manifest.json` and embedded asset data only for optional visual support.
- Images must not contain hidden clues that are absent from text.
- Opening narration should identify the stopped clock as the **tallcase clock in the study**, not the missing pocket watch.
