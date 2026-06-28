# Runtime Engine v2

## Purpose

This document defines Game Master Runtime Engine v2 for the AI Interactive Fiction project.

Version 1 proved that a repository-backed mystery can be authored, validated, AI-playtested, revised, handed off, and completed by a human player.

Version 2 turns the Game Master from a broad prompt into a more deterministic runtime engine with explicit internal behaviors.

The player should still experience a natural conversational mystery. Internally, the Game Master should follow a structured loop.

## Repository architecture distinction

The project now uses two parallel layers:

```text
docs/      Durable engine specifications and design rules.
prompts/   Operational role instructions for AI execution.
```

Specification documents define how the system should behave.

Prompt documents tell a specific AI role how to operate.

Prompts should reference specs instead of duplicating all logic.

## Runtime goals

The Game Master should:

- preserve canon;
- reveal information only when earned;
- apply discovery rules consistently;
- distinguish immediate observation, investigation, and interpretation;
- respect NPC knowledge boundaries;
- maintain a structured case board;
- manage image generation safely;
- track negative inspections;
- maintain structured runtime state;
- handle out-of-game feedback;
- support fair final accusation;
- record postgame findings.

## Runtime lifecycle

A Game Master session has these phases:

1. Load project and case files.
2. Confirm canonical source.
3. Initialize runtime state.
4. Present opening scene.
5. Process player actions through the runtime loop.
6. Update case board and runtime state.
7. Evaluate theories and accusations.
8. Resolve the case when sufficient proof is supplied.
9. Record postgame findings if requested.

## Required files

Before gameplay, the Game Master should read:

```text
README.md
docs/project-architecture.md
docs/design-principles.md
docs/playtest-findings.md
docs/repository-workflow.md
docs/runtime-engine-v2.md
docs/runtime-fidelity-engine-v1.md
docs/canonical-assets-and-runtime-budgets-v1.md
docs/discovery-rules-v1.md
docs/npc-interview-model-v1.md
docs/investigation-model.md
docs/image-system-v2.md
docs/case-board-v2.md
docs/case-board-current-v1.md
docs/runtime-state-v1.md
docs/runtime-self-checks.md
schemas/runtime-state.schema.json
schemas/case-board-current.schema.json
prompts/06-game-master.md
games/index.json
games/<case-folder>/gm-readme.md
games/<case-folder>/game-package.json
games/<case-folder>/case-board-seed.json
games/<case-folder>/case-board-current.json
games/<case-folder>/asset-manifest.json
games/<case-folder>/validation-report*.md
games/<case-folder>/playtest-report.md
```

If `gm-readme.md` identifies a canonical source, follow it.

If an existing runtime state file exists, the Game Master should read it before resuming play:

```text
games/<case-folder>/runtime-state.json
```

If an existing current case board exists, the Game Master should read it before resuming play:

```text
games/<case-folder>/case-board-current.json
```

If no current case board exists, initialize it from `case-board-seed.json` or the package's embedded `caseBoardSeed`.

During startup, load `canonicalAssetInventory` and `runtimeBudgets` from `game-package.json` when present. Treat them as runtime constraints.

## Canon preservation

The Game Master must not change:

- culprit;
- motive;
- method;
- timeline;
- clue meanings;
- evidence provenance;
- witness knowledge;
- final proof;
- red herring explanation.

Surface narration may be flexible. Core facts may not.

## Runtime fidelity

Runtime fidelity is governed by:

```text
docs/runtime-fidelity-engine-v1.md
```

The Game Master is an interpreter of the authored package, not a co-author.

It may improvise surface narration, ordinary atmosphere, pacing, and natural phrasing. It must not invent new suspects, witnesses, evidence, clues, clue paths, locations, documents, solution mechanics, timeline events, physical access routes, motives, alibis, contradictions, red herring explanations, or final proof.

Background characters may provide atmosphere only. They cannot become investigative sources unless the package authors them as NPCs, witnesses, evidence sources, or discovery-rule targets.

If the player asks about unauthored content, the Game Master should give a natural negative or redirect response without adding new facts. It may record a fair negative investigation result when runtime state or the current case board supports it.

When authored leads are exhausted, the Game Master should summarize player-visible facts and transition to deduction mode instead of creating more leads.

Before revealing or accepting an investigative branch, check `canonicalAssetInventory`. Before introducing any NPC, location, object, evidence, document, image, discovery rule, or branch, check both the inventory and `runtimeBudgets`.

## Runtime loop

For each player message, the Game Master should silently process:

```text
1. Is this in-game or out-of-game?
2. What is the player trying to do?
3. What scene, object, NPC, or evidence does it concern?
4. What has the player already discovered?
5. What typed discovery trigger does the action map to?
6. Is the target authored investigative content or unsupported content?
7. Is the target listed in `canonicalAssetInventory` when an inventory exists?
8. Would this exceed a runtime budget?
9. Which discovery rule, if any, applies?
10. Are rule prerequisites satisfied?
11. Has this rule already fired?
12. What observation layer is being requested?
13. What can be revealed now?
14. What remains hidden?
15. Are authored leads exhausted, requiring deduction mode?
16. Does the case board change?
17. Does runtime state change?
18. What concise response preserves canon and moves play forward?
```

The player should not see this checklist unless they ask for process notes out of game.

## Observation layers

Use the investigation model:

```text
Immediate observation -> Investigation -> Interpretation
```

Immediate observation describes what a person can plainly see, hear, or notice on entering a scene.

Investigation reveals details through close inspection, questioning, comparison, or interaction.

Interpretation explains what details mean after the player has enough supporting information.

The Game Master must not skip from immediate observation directly to interpretation.

## Discovery gating

A clue is earned when the player's action satisfies a relevant typed discovery rule.

Typed discovery rules are governed by:

```text
docs/discovery-rules-v1.md
```

The Game Master should not reveal a clue unless the proper discovery trigger is satisfied and listed prerequisites are met.

If an action partially satisfies a condition, reveal partial information.

Example pattern:

```text
Player inspects an object.
GM reveals visible condition.
Player inspects more closely or compares evidence.
GM reveals forensic detail.
Player connects detail to another clue.
GM permits interpretation.
```

Do not reveal a clue's true meaning too early.

When a rule fires, record its `ruleId` in runtime state and record any discovered clue or evidence IDs. If the rule has already fired, use `repeatText` or summarize the prior discovery.

If a plausible action does not reveal a clue, use `failureText` when available and treat the result as negative investigation rather than inventing evidence.

`case-board-current.json` should receive only player-visible updates from the fired rule.

If no authored clue path, evidence item, NPC topic, object, document, or location supports the action, do not create one. Give a natural negative or redirect response and return to authored leads.

Discovery rules may reveal only authored assets. If a rule references an asset outside the inventory, treat that as a package defect and do not expose the asset during play.

## Negative investigation

Negative investigation is valuable and should be tracked.

If the player inspects an object or area that contains no direct evidence, the GM should:

- answer honestly;
- say what the inspection rules out;
- avoid inventing new clues;
- update inspected-object state when useful.

Example:

```text
You examine the window. It is latched from inside, and the sill shows no fresh marks. That does not explain the theft, but it makes outside entry less likely.
```

## NPC interactions

NPCs should answer only from:

- their own knowledge;
- their own observations;
- their own motives;
- their own lies or omissions;
- their defined personality.

NPCs must not speak from omniscient solution knowledge.

If a player asks an NPC something the NPC cannot know, the NPC should say so or answer from limited perception.

NPC interview topics are governed by:

```text
docs/npc-interview-model-v1.md
```

For NPC questions, the Game Master should:

1. Map the natural-language question to the closest valid NPC topic.
2. Respect the NPC's knowledge boundary.
3. Check topic prerequisites and `question_npc` discovery rules.
4. Reveal only eligible clue or evidence IDs.
5. Use lie, omission, evasion, ignorance, or truthful answer behavior as defined.
6. Use repeat answers when the topic was already asked.
7. Record asked topics in `runtime-state.json`.
8. Update `case-board-current.json` only with player-visible answers, contradictions, or leads.

NPCs must not become omniscient or overhelpful because the player asks a broad question.

Unauthored background characters may add atmosphere only. They must not become witnesses, suspects, or clue sources during play.

## Hint progression

Hints should progress gradually.

Use this ladder:

1. General nudge.
2. Relevant object, NPC, or area.
3. Relevant comparison or question.
4. Near-explicit next action.

Do not jump directly to solution facts unless the player explicitly asks to end or spoil the case.

## Image runtime

Images follow the same observation layers as text.

A scene image may show immediately visible room elements.

An inspection image may show close details only after the player inspects that object or area.

An evidence image may show recovered or exposed evidence only after it is discovered in text.

Images must not be the only place where an essential clue appears.

## Final accusation

When the player accuses someone, evaluate:

- culprit;
- motive;
- method;
- opportunity;
- proof;
- red herring explanation.

Allow partial theories. Do not declare full success until the required proof threshold is met.

If the accusation is close but incomplete, explain what remains unproven without revealing the full answer.

## Deduction mode

When all authored investigative leads available to the player are exhausted, transition to deduction mode.

In deduction mode, the Game Master should:

- summarize discovered facts;
- separate evidence from theory;
- identify remaining open questions answerable from discovered facts;
- ask the player to propose who, why, how, and proof;
- offer only policy-allowed non-spoiler hints;
- evaluate theories and accusations against the authored proof threshold.

Do not invent more leads to prolong investigation.

## Out-of-game feedback

A player message beginning with `/` is out of game.

The Game Master should:

- pause in-game action processing;
- answer as project collaborator or test observer;
- avoid spoilers unless explicitly requested;
- not reveal clues or advance gameplay;
- resume from prior state afterward.

## Runtime state

The GM should track runtime state separately from the canonical package.

Canonical package answers what is true.

Runtime state answers what the player has discovered, inspected, seen, theorized, requested, ruled out, or resolved.

Runtime state is governed by:

```text
docs/runtime-state-v1.md
schemas/runtime-state.schema.json
```

Runtime state should be stored during play as:

```text
games/<case-folder>/runtime-state.json
```

The Game Master should use runtime state to track at minimum:

- session status and turn count;
- current scene, location, NPC conversation, and focus object;
- fired discovery rule IDs;
- discovered and interpreted clues;
- observed and recovered evidence;
- visible, inspected, closely inspected, recovered, and ruled-out objects;
- NPCs met, questioned, topics asked, claims heard, and contradictions known;
- open, pending, closed, and blocked leads;
- hints requested or offered;
- theories and accusations;
- compact runtime budget usage, such as used NPC, location, object, evidence, document, image, and discovery rule IDs;
- exhausted leads and whether deduction mode has begun;
- images shown, requested, denied, or deferred;
- compact case-board continuity;
- preserved out-of-game notes when relevant.

Do not write player progress, discovered clues, visited locations, or object inspection state into `game-package.json` unless deliberately producing a revised package.

## Current case board

The GM should maintain the current player-facing case board separately from both canonical truth and broader runtime state.

The current case board is governed by:

```text
docs/case-board-current-v1.md
schemas/case-board-current.schema.json
```

It should be stored during active play as:

```text
games/<case-folder>/case-board-current.json
```

`case-board-seed.json` is the initial visible board.

`case-board-current.json` is the evolving player-facing board.

Only information available to the player belongs on the current board. Hidden culprit, motive, method, clue meaning, timeline, red herring explanation, or final proof data must remain in the canonical package until discovered.

## Failure conditions

The Game Master fails if it:

- changes canon;
- invents decisive clues;
- invents suspects, witnesses, evidence, clue paths, locations, documents, timeline events, or physical access routes;
- reveals hidden facts prematurely;
- treats images as secret evidence;
- loses track of what the player has seen;
- forgets inspected objects or ruled-out areas;
- repeats hints without tracking prior hints;
- makes NPCs omniscient;
- lets background characters become investigative sources;
- fails to transition to deduction mode when authored leads are exhausted;
- ignores `/` feedback protocol;
- ends without answering who, why, how, and proof.

## Relationship to Prompt 06

`prompts/06-game-master.md` is the operational prompt.

This document is the durable specification.

Future versions of Prompt 06 should remain concise and reference this document rather than reimplementing every detail inline.
