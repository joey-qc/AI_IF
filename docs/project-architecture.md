# Project Architecture

## Purpose

This document describes the proposed architecture for the AI Interactive Fiction project.

The project began as a prompt-only interactive mystery experiment. The first full playtest showed that conversational AI can provide a compelling detective-game interface, but it also showed that a single Game Master prompt cannot reliably generate, validate, remember, and resolve a complex mystery in one continuous conversation.

The architecture therefore separates the system into distinct tiers and AI roles.

## Architectural principle

Separate these responsibilities:

1. Story structure design.
2. Story authorship.
3. Validation and QA.
4. Revision.
5. Gameplay presentation.
6. Persistent storage of game files and assets.

The Game Master should not improvise the core mystery while the player is investigating. The Game Master should operate from a validated game package whose solution already exists.

## Tier 1: Template and Schema Designer

### Role

Defines the structure of a playable mystery.

### Responsibilities

- Define required components of a game package.
- Define required fields for suspects, clues, locations, timeline events, evidence, images, and solution data.
- Define difficulty presets.
- Define scope limits for one-sitting games versus longer campaigns.
- Define validation requirements.
- Define what must be known before gameplay begins.

### Outputs

- Human-readable schema documentation.
- JSON Schema or similar machine-readable schema files.
- Template files for generated games.

### Non-responsibilities

- Does not write the actual story.
- Does not act as Game Master.
- Does not revise individual cases except by improving the template.

## Tier 2: Story Author

### Role

Creates a complete mystery using the approved template.

### Responsibilities

- Generate the setting, premise, central crime, suspects, locations, clues, red herrings, and final resolution.
- Work backward from the culprit, motive, method, and proof.
- Create a complete hidden solution before gameplay begins.
- Ensure that every major clue has a reason to exist.
- Ensure that every suspect has a plausible apparent relationship to the case.
- Keep the story within the requested difficulty and length budget.

### Outputs

- Draft game package.
- Draft solution file.
- Draft timeline.
- Draft clue matrix.
- Draft NPC and location files.
- Draft asset manifest.

### Non-responsibilities

- Does not approve its own work as playable.
- Does not run the final player-facing game.

## Tier 3: Game Package Builder

### Role

Converts authored story material into a structured game package that can be validated and played.

### Responsibilities

- Assemble all story elements into the required file structure.
- Normalize IDs for suspects, clues, locations, evidence, scenes, and assets.
- Ensure references between files are valid.
- Package canonical story facts separately from player-facing narration.
- Preserve hidden information that the Game Master may access but the player may not see until earned.

### Outputs

- `game-package.json`
- `solution.md`
- `case-board-seed.json`
- `asset-manifest.json`
- Optional maps, images, handouts, and documents.

## Tier 4: Validator

### Role

Performs formal consistency checks before play.

### Responsibilities

- Check that the culprit, motive, method, opportunity, and proof are explicit.
- Check that the final solution is supported by discoverable clues.
- Check that every clue has closure.
- Check that every red herring is explainable.
- Check chronology for contradictions.
- Check physical plausibility.
- Check evidence provenance.
- Check witness statements against the true timeline.
- Check that the solution can be reached without guessing.
- Check that difficulty and length match the requested preset.

### Outputs

- Validation report.
- Pass/fail status.
- Required revisions.
- Optional severity ranking.

### Non-responsibilities

- Does not rewrite the story directly unless acting under the Revision Engine role.
- Does not run the player-facing game.

## Tier 5: AI Playtester

### Role

Simulates one or more player investigations to test whether the mystery actually works in play.

### Responsibilities

- Play the case as a skeptical detective.
- Ask questions a real player might ask.
- Attempt likely and unlikely investigation paths.
- Look for missing information, dead ends, premature reveals, and unsupported conclusions.
- Test whether the mystery can be solved from available evidence.
- Identify whether the final reveal feels earned.

### Outputs

- Playtest transcript or summary.
- List of uncovered defects.
- Solvability assessment.
- Pacing and scope assessment.
- Recommendations for revision.

## Tier 6: Feedback Loop and Revision Engine

### Role

Uses validator and playtester findings to revise the game package.

### Responsibilities

- Interpret validation failures.
- Repair plot holes, chronology issues, clue gaps, weak motives, and unsupported deductions.
- Preserve the intended tone, genre, difficulty, and player experience.
- Avoid patching one issue by creating new contradictions.
- Re-run validation after revisions.

### Outputs

- Revised game package.
- Revision notes.
- Updated validation report.
- Updated playtest report.

## Tier 7: Game Library Repository

### Role

Stores complete generated games and their versions.

### Responsibilities

- Maintain validated game packages.
- Preserve historical versions.
- Track play status.
- Store metadata such as genre, difficulty, estimated length, setting, and validation status.
- Allow future conversations or applications to load a specific case.

### Example structure

```text
games/
  case-001/
    game-package.json
    solution.md
    case-board-seed.json
    validation-report.md
    playtest-report.md
    assets/
```

## Tier 8: Asset Library

### Role

Stores and indexes player-facing visual and documentary assets.

### Responsibilities

- Track images, maps, portraits, letters, diagrams, and evidence handouts.
- Ensure assets support the written game rather than replacing canonical clues.
- Maintain labels and descriptions so the player can request previously seen assets.
- Record when each asset becomes available to the player.
- Prevent images from containing hidden clues not also described in text.

### Example player requests

- Show me the family photo again.
- Show me the map from Pier 9.
- Show me all documents I found in the hotel.
- Show me portraits of the current suspects.

## Tier 9: Game Master

### Role

Runs the validated game package for the human player through conversational interaction.

### Responsibilities

- Present scenes and NPC interactions.
- Answer player questions from canonical game data.
- Reveal clues only when earned.
- Maintain tone and pacing.
- Track discovered evidence, visited locations, known suspects, and open questions.
- Generate or retrieve assets only when requested or when allowed by startup settings.
- Avoid inventing contradictions.
- Avoid revealing hidden solution data prematurely.
- Guide the game toward resolution when the player has enough information.

### Non-responsibilities

- Does not choose the culprit during play.
- Does not rewrite the solution during play.
- Does not create hidden clues that were absent from the game package.

## Tier 10: Case Board Manager

### Role

Maintains player-facing investigation state.

### Responsibilities

- Track discovered clues.
- Track open leads.
- Track suspects and known facts.
- Track visited and unvisited locations.
- Track contradictions and unresolved questions.
- Track current theories.
- Provide summaries on request.

### Example commands

- Show my case board.
- What evidence points to Mallory?
- What questions are still unanswered?
- Which locations have I not visited?
- Summarize the timeline so far.

## Tier 11: Start-Here / Handoff Layer

### Role

Allows future ChatGPT conversations to resume work without losing context.

### Responsibilities

- Explain the repository structure.
- Identify which documents to read first.
- Record current project status.
- Identify next recommended work.
- Preserve architectural decisions.

### Current implementation

The repository `README.md` currently serves this role.

## Prompt-only versus coded implementation

The architecture should support two possible futures.

### Prompt-driven workflow

The project may continue as a collection of Markdown prompts, schema documents, generated JSON files, and validation reports managed through GitHub.

Advantages:

- Fast to iterate.
- No custom UI required.
- Works well inside ChatGPT conversations.
- Good for experimentation.

Limitations:

- Less automation.
- More manual file orchestration.
- More risk of context loss if files are not carefully maintained.

### Coded application

The project may eventually become a web or desktop application that uses LLM APIs, structured storage, and a custom UI.

Advantages:

- Better state management.
- Automated validation loops.
- Persistent game library.
- Asset retrieval and case board can be first-class features.
- Easier to run repeatable QA.

Limitations:

- Requires software development.
- Requires API integration and hosting decisions.
- Requires schema and data model stability.

## Near-term recommendation

Continue with a repository-backed prompt workflow until the core schemas and phase-specific prompts stabilize. Do not build a full application until the project has at least one validated game package that can be generated, tested, revised, and played successfully using the file-based workflow.
