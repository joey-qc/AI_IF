# Workflow and Case Readiness v1

## Purpose

This document defines the required AI_IF case lifecycle. A case is not ready for human play merely because it exists in GitHub. Readiness requires validation, revision, AI playthrough, final validation, and explicit status confirmation.

## Case Lifecycle States

Use these conceptual states even if exact metadata field names differ:

1. authored_draft
2. implementation_draft
3. package_created
4. validation_pending
5. validation_failed
6. revised_after_validation
7. validation_passed
8. ai_playtest_pending
9. ai_playtest_failed
10. revised_after_ai_playtest
11. final_validation_passed
12. ready_for_human_play
13. human_played
14. postgame_reviewed

## GitHub Package Is Not Automatically Playable

A case may exist under `games/` and still be unready. The Game Master must check case metadata, GM README status, and any readiness fields before treating a package as playable.

If a case says `draft`, `not_validated`, or `not_playtested`, it should not be presented as ready for human play unless the user explicitly requests testing an unfinished package.

## Local Working Draft Rule

Story design, validation findings, AI playthrough findings, and revision planning may be managed outside GitHub during development.

Codex should generally update GitHub only after a consolidated revision package is ready.

Avoid repeated GitHub patch cycles for intermediate findings unless:

- the repository itself is the only working source;
- a blocker prevents further analysis;
- the user explicitly authorizes a partial patch;
- the change is metadata-only and approved.

## Validation Before AI Playthrough

Do not AI-playtest a known-flawed package unless the explicit purpose is to reproduce the flaw.

If validation finds a material issue:

1. revise the working draft;
2. re-validate;
3. only then run AI playthrough.

## Reports Must Be Consumed

Validation and AI playthrough reports are working artifacts. They should not merely be handed to the user and left unused.

The Revision Engine must consume reports and apply or propose revisions before the user is asked to proceed.

User-facing summaries should be spoiler-free unless the user requests details.

## Blessed Package Definition

A package is ready for human play only when:

1. the package exists in GitHub or a final implementation handoff exists;
2. package validation has passed;
3. AI playthrough has passed;
4. validation/playthrough findings have been resolved;
5. final re-validation has passed;
6. case metadata reflects readiness;
7. GM README reflects readiness;
8. no known blockers or major findings remain.

## Consolidated Codex Handoff Standard

Codex should be treated as repository I/O, not the primary reasoning engine.

A Codex handoff must specify:

- exact allowed files;
- forbidden files;
- whether game files may be changed;
- whether engine docs may be changed;
- whether story content may be generated;
- required checks;
- final report format only.

Codex should not be asked to reason broadly, invent story material, or perform exploratory design unless the user explicitly approves.

## Final Report Standard

Codex final reports should include:

- files changed;
- checks run;
- commit hash;
- final git status;
- confirmation that forbidden files were not changed;
- confirmation that no unintended game/case was created.
