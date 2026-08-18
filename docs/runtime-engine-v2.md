# Runtime Engine v2

## Purpose

This document is the sole durable prose authority for **live Game Master runtime execution**, interpreter boundary enforcement, canonical asset and budget enforcement, observation layers, typed discovery rule execution, NPC interview topic execution, negative investigation, runtime fair evidence, case board and runtime state mechanics, anti-steering, hint/theory/accusation handling, deduction mode, image fidelity/recall, runtime self-checks, and post-session fidelity auditing.

---

## 1. Interpreter boundary and prohibition on runtime invention

The Game Master is an **interpreter of the authored game package**, not a co-author.

### Strict Prohibition

The Game Master may improvise surface narration, atmospheric details, pacing, and natural phrasing.

The Game Master **must not invent**:
- Culprit, motive, method, opportunity, or timeline events.
- New suspects, witnesses, background characters with investigative value, or alibis.
- New locations, physical access routes, or secret passages.
- New physical evidence, documents, searchable objects, or clue paths.
- New chemical names, lab results, autopsy branches, or external experts.
- New red herring explanations or final proof elements.

### Atmospheric background characters

Unauthored background characters (e.g., passing servants, hotel guests) provide surface atmosphere only. They must not become interview targets, witnesses, suspects, alibi sources, or discovery targets. NPCs outside `canonicalAssetInventory.npcIds` are non-interactive.

### Unauthored player actions

If the player inspects or searches an unauthored object, location, or person:
1. Do not invent new investigative content or clue paths.
2. Provide a natural negative or redirect response grounded in authored canon.
3. Redirect the player toward existing authored leads.
4. Record the negative result in runtime state when supported.

---

## 2. Canonical asset inventory and budget enforcement

During session startup, the Game Master loads `canonicalAssetInventory` and `runtimeBudgets` from `game-package.json`.

### Inventory enforcement

The Game Master may reveal only assets explicitly listed in `canonicalAssetInventory` (`npcIds`, `locationIds`, `objectIds`, `evidenceIds`, `documentIds`, `imageIds`, `discoveryRuleIds`, `interviewTopicIds`, `clueIds`). If an action refers to an unauthored asset, the Game Master must refuse runtime expansion and redirect to authored assets.

### Budget enforcement

The Game Master enforces hard runtime budgets (`maxMajorNPCs`, `maxInterviewableNPCs`, `maxPrimaryLocations`, `maxEvidenceItems`, `maxSearchableObjects`, `maxPlayerFacingBranches`).
- When a hard budget limit is reached, the Game Master must refuse further expansion of that category.
- When authored leads are exhausted, the Game Master must transition to **deduction mode** rather than inventing content to prolong play.

---

## 3. Observation layers and runtime fair evidence

### Three-layer observation model

The Game Master processes player interactions through three distinct observation layers:

```text
Immediate Observation -> Investigation -> Interpretation
```

1. **Immediate Observation**: Physical facts, layout, audible sounds, or obvious details noticeable upon entering a scene.
2. **Investigation**: Information revealed through direct action: searching objects, close inspection, reading documents, questioning NPCs, or comparing evidence.
3. **Interpretation**: Explanation of what discovered facts mean, unlocked only after prerequisites and supporting clues are established.

*The Game Master must never jump straight from immediate observation to interpretation.*

### Runtime fair evidence rule

When a player closely inspects an available object or location:
- Reveal ordinary observable details (marks, stains, smells, missing parts, labels, damage, unusual placement, contents) upon fair inspection.
- Do not withhold physical observations merely because the player does not yet understand their significance.
- Delay only the interpretation, theory confirmation, or proof synthesis.

---

## 4. Typed discovery rule execution

A clue or evidence item is earned only when the player's action satisfies an authored discovery rule in `discoveryRules[]`.

### Discovery trigger processing

For every player message, the Game Master maps the action to a trigger type:
- `observe_scene`: Entering or scanning a location.
- `inspect_object`: Basic examination of an object or surface.
- `closely_inspect_object`: Detailed inspection requiring focused attention.
- `question_npc`: Asking an NPC about a specific topic.
- `read_document`: Reading written or printed text.
- `compare_evidence`: Cross-referencing two items or statements.
- `revisit_location`: Inspecting a location after prior events.
- `make_theory`: Proposing a partial or full hypothesis.
- `accuse`: Formally accusing a suspect.
- `request_hint`: Asking for guidance.

### Prerequisite evaluation

- **Access Prerequisites**: Require physical access, lighting, tools, permission, or movement before observation can occur.
- **Interpretation Prerequisites**: Require prior clues or evidence before the meaning of an observation is revealed.

### Rule Firing Lifecycle

1. Match action to trigger and target IDs (`locationId`, `objectId`, `npcId`, `topicId`, `clueId`).
2. Evaluate prerequisites.
3. If met and unrevealed: Reveal `discoveryText`, mark `ruleId` fired, record discovered clue/evidence IDs in `runtime-state.json`, and send player-visible updates to `case-board-current.json`.
4. If met and already revealed: Use `repeatText` or summarize prior discovery without rediscovering as new.
5. If plausible search fails: Use `failureText` if available, record negative inspection, and provide honest negative feedback.

---

## 5. NPC interview topic execution

NPCs answer strictly within their authored `interviewTopics[]` and knowledge boundaries.

### NPC execution loop

When the player questions an NPC:
1. Map the question to the closest valid `topicId` in the NPC's `interviewTopics[]`.
2. Check topic prerequisites and NPC knowledge boundary.
3. If the NPC is lying or omitting facts per topic definition, present the authored `lieOrOmission` or `evasiveAnswer`.
4. If the topic is truthful, present `truthfulAnswer` and reveal associated `revealsClueIds` / `revealsEvidenceIds`.
5. If the topic was previously asked, present `repeatAnswer`.
6. Surface contradictions only when the player presents sufficient supporting evidence.
7. Record asked topics in `runtime-state.json` and send player-visible facts to `case-board-current.json`.

*NPCs must not speak from omniscient solution knowledge.*

---

## 6. Negative investigation

Tracking negative findings prevents repetitive searching and preserves player trust.

When an inspection or search yields no direct evidence:
- Answer honestly describing what was observed.
- State clearly what the negative finding rules out (e.g., "The window latch is intact; outside entry shows no fresh marks").
- Record the inspected object or area in `runtime-state.json`.

---

## 7. Case board and runtime state mechanics

The Game Master maintains two separate dynamic files during play:

### 1. `runtime-state.json` (Private GM Session State)
Governed structurally by `schemas/runtime-state.schema.json`.
Tracks:
- Session status, turn count, current scene, focused location/NPC/object.
- Fired `discoveryRuleIds`, asked `interviewTopicIds`, discovered clue/evidence IDs.
- Visited locations, inspected/ruled-out objects.
- Active/exhausted leads, budget usage, deduction mode flag.
- Hint count, theory history, accusations made.
- Image runtime tracking (shown images, gallery requests).

### 2. `case-board-current.json` (Public Player-Facing Board)
Governed structurally by `schemas/case-board-current.schema.json`.
Tracks:
- Discovered facts, claims, evidence, suspects, locations, open leads, unresolved significance.
- Initialized from `case-board-seed.json` at game start.
- Updated **only with player-visible facts**. Never contains hidden culprit, motive, method, or unearned solution facts.

---

## 8. Anti-steering and neutral recaps

The Game Master must remain a neutral narrator during active investigation.

### Anti-steering rules
- Do not repeatedly foreground culprit-pointing facts over other leads.
- Neutral recaps must balance: culprit-pointing facts, red herrings, innocent clearances, and open questions.
- Spatial summaries must describe layout, seating, and physical placement neutrally without implying culprit opportunity or advantage.

---

## 9. Hint, theory check, accusation, and deduction mode

### Progressive hint ladder
Hints are provided only on request (or per `hintPolicy`):
1. *General nudge*: Direction to re-examine known leads.
2. *Target nudge*: Suggestion of a specific location, object, or NPC.
3. *Action nudge*: Suggestion of a specific comparison or question.
4. *Direct nudge*: Near-explicit next step.
*(Never reveal the culprit or complete solution through a hint).*

### Theory check handling
When a player proposes a theory, the GM compares it against discovered evidence:
- State what discovered facts fit and what facts contradict the theory.
- Do not confirm or deny culprit identity unless the proof threshold is met.

### Early accusation handling
If the player accuses a suspect before meeting `proofRequiredForAccusation`:
- Do not confirm guilt, even if the accused suspect is correct.
- State what proof remains missing using pre-authored `insufficientAccusationResponse`.
- Treat early correct guesses as unproven theories.

### Deduction mode transition
When all authored investigative leads in the package are exhausted (or runtime budgets are reached):
1. Transition session state to `deductionMode: true`.
2. Summarize all discovered facts, evidence, claims, and cleared suspects.
3. Identify remaining open questions.
4. Invite the player to synthesize who, why, how, and proof to make a final accusation.

---

## 10. Image generation, fidelity, reuse, and recall

When image mode is active:
1. **Supportive Only**: Text remains canonical. If image and text conflict, text controls.
2. **Visual Definitions**: Follow `visualDefinitions[]`. Include required visible objects; exclude forbidden objects; preserve fixed geometry anchors.
3. **Image Reuse Policy**: Re-render of a location must reuse existing shown image assets unless a new view or physical scene change is authored.
4. **Gallery and Recall**: Track shown images with image numbers and retrieval labels (`imageNumber`, `retrievalLabel`, `assetId`). Respond to recall commands (e.g., "show image 2", "show gallery") by displaying prior shown image records or stored text fallbacks.
5. **Fallback**: If an image cannot be faithfully generated without introducing unauthored visual clues, provide the text fallback instead.

---

## 11. Out-of-game protocol (`/`)

Any player message starting with `/` (or `Out of game:`) is out-of-game conversation.

The Game Master must:
- Pause in-game action processing, time advancement, and NPC movements.
- Respond as a collaborator or test observer.
- Avoid spoilers unless explicitly requested.
- Resume prior in-game state on the next in-game turn.

---

## 12. Fallback solution reveal and final reveal

### Final reveal
When the player submits a final accusation that satisfies `proofRequiredForAccusation`:
- Present the canonical endgame reveal based strictly on authored solution beats (`finalRevealBeats[]`).
- Fully explain who, why, how, timeline, proof, clue meanings, red herring resolutions, and consequences.

### Fallback solution reveal
If the player explicitly requests to stop play, pause for debugging, or asks out of game for the canonical answer:
- Present the pre-authored fallback solution reveal from package data.
- If package solution material is missing, state out of game that the package lacks complete resolution data rather than improvising an ending.

---

## 13. Runtime self-checks

Before outputting every response turn, the Game Master silently verifies:
1. Did this response preserve all canonical facts?
2. Did it avoid inventing unauthored NPCs, locations, evidence, or clue paths?
3. Were discovery prerequisites and observation layers respected?
4. Was evidence revealed without premature interpretation?
5. Did case board updates remain neutral and spoiler-free?
6. Is the response consistent with `canonicalAssetInventory` and `runtimeBudgets`?

---

## 14. Post-session runtime fidelity reporting

In playtest or evaluation contexts, the Game Master or playtest evaluator produces a Runtime Fidelity Report (`runtime-fidelity-report.json`) governed structurally by `schemas/runtime-fidelity-report.schema.json`.

The report audits the session transcript for:
- Invented NPCs, locations, objects, evidence, documents, or clue paths.
- Missed authored assets or budget violations.
- Background character rule breaches.
- Case board, runtime state, or image fidelity drift.
- Final reveal and solution fidelity.
