# Design Principles

## Purpose

This document is the sole durable prose authority for **pre-runtime mystery design**, reverse mystery authoring, fair-play solvability, clue closure, motive strength, human engagement, scope matching, suspect deception, red herrings, whodunit patterns, specialized test boundaries, authored player agency, and pre-runtime image definitions for the AI Interactive Fiction project.

---

## 1. Conversational human interactive fiction

Interactive mysteries are human stories first and puzzles second.

The player interacts with an AI Game Master in natural language. The mystery must offer emotionally legible stakes: people want, fear, betray, protect, envy, resent, or regret something concrete. 

A case that is technically solvable can still fail if it feels like a procedural checklist of logs, devices, and abstract business numbers rather than an engaging human story.

---

## 2. Canonical solution before play and reverse authoring

The complete solution must exist in `game-package.json` before gameplay begins.

The culprit, victim, motive, method, opportunity, timeline, clue chain, evidence provenance, red herring explanations, and proof threshold must be fixed before play. The Game Master must never invent or alter facts during gameplay.

### Reverse mystery authoring

All mysteries must be authored **backward from canonical truth**:

1. Define what actually happened (the hidden timeline and central crime).
2. Define who is responsible (the culprit) and their concrete motive mechanism.
3. Define how the crime was executed (method and physical opportunity).
4. Define what mistakes were made and what evidence was created.
5. Define how the truth can be discovered and proved.
6. Author scenes, NPC dialogue, images, red herrings, and discovery rules that derive from this canonical truth model.

### Final Resolution Contract

Every authored package must satisfy the Final Resolution Contract. The package must contain enough canonical data for the Game Master to explain:
- Culprit or responsible party.
- Motive and motive mechanism.
- Method and opportunity.
- Exact chronological timeline.
- Required clues and supporting evidence.
- Red herring explanations and false leads.
- Innocent suspect clearance.
- Proof chain and accusation prerequisites.
- Canonical endgame explanation.
- Authoritative fallback solution reveal.

---

## 3. Motive strength and concrete motive mechanism

The motive must be proportional to the crime.

For major crimes (such as murder, arson, major theft, or blackmail), the culprit must face severe, life-altering consequences if they fail, such as:
- Financial ruin or inheritance loss.
- Exposure of fraud or criminal liability.
- Institutional collapse or loss of life's work.
- Blackmail, ruinous scandal, or destruction of family name.
- Protection of a prior major crime.

### Concrete motive mechanism requirement

Generic motive labels (e.g., "jealousy", "financial trouble", "career pressure") are insufficient. Every authored case must define the culprit's concrete action plan:
1. What specific benefit the culprit expected.
2. Why they acted *now* (triggering event).
3. How the crime solved their specific problem.
4. What would happen if they failed.
5. Why they chose this specific method over lesser actions.

---

## 4. Fair-play solvability, clue closure, and evidence provenance

Every mystery must be solvable by a careful player through observation, investigation, and deduction without guessing or luck.

### Clue closure matrix

Every significant clue introduced in the story must have explicit closure:
- Connected to the culprit's actions (essential or supporting clue); or
- Connected to an innocent suspect's secret (red herring with innocent explanation); or
- Clearly marked as atmospheric background.

Unexplained or dangling major clues are blocker-level authoring failures.

### Proof chain and proof threshold

The case author must define `proofRequiredForAccusation`:
- Minimum essential clues required before an accusation succeeds.
- Deductions the player must articulate.
- Pre-authored insufficient-proof response to handle early correct guesses without confirming or denying guilt.

### Evidence provenance

Evidence must not appear spontaneously to suit plot convenience. Every piece of physical or documentary evidence must specify:
- Who created it and when (timeline event).
- Where it was stored and who had access.
- How it reached its discovery location.
- Why it was not destroyed, hidden, or previously discovered.

---

## 5. Scope matching and budget presets

A mystery package must strictly fit its chosen length and difficulty preset.

### Presets and limits

- **`quick_mystery`** (10-25 min play time):
  - Primary locations: **Exactly 1**.
  - Major NPCs/suspects: **Max 3**.
  - Essential clues: **Max 10**.
  - Red herrings: **Max 1**.
  - Nested secrets: **0**.
  - *Must not sprawl into multi-location investigations.*

- **`one_sitting`** (30-60 min play time):
  - Primary locations: 4-6.
  - Major NPCs/suspects: 3-5.
  - Essential clues: 6-12.
  - Red herrings: 1-3.
  - Nested secrets: 0-1.

- **`standard_case`** & **`extended_case`**:
  - Expanded scope permitted only with explicit runtime budget declarations.

### Canonical asset inventory & runtime budgets

Every authored package must declare:
- `canonicalAssetInventory`: Explicit list of allowed NPC IDs, location IDs, object IDs, evidence IDs, document IDs, image IDs, discovery rule IDs, and interview topic IDs.
- `runtimeBudgets`: Hard and soft limits on major NPCs, interviewable NPCs, searchable objects, evidence items, documents, images, hints, and player-facing branches.

---

## 6. Suspect deception and red herring discipline

### Suspect deception requirements

For every major suspect, the package must author:
- Alibi claim vs. alibi truth.
- Truthful statements vs. lies or omissions.
- Concrete reason for lying (e.g., shame, lesser secret, protecting another person).
- Discoverable evidence or contradiction that exposes the lie.
- What clears or implicates the suspect.

*Do not author a lie unless the player can discover, challenge, or resolve it.*

### Red herring discipline

Red herrings must mislead fairly:
- Must have a grounded innocent explanation.
- Must be clearable through discoverable evidence.
- Must not block the canonical solution or force the player into absurd assumptions.

---

## 7. Contained whodunit patterns

For contained whodunits (e.g., locked room, isolated house, private gathering):
- The crime must occur within a closed environment with a fixed suspect pool.
- Physical entry and exit routes must be accounted for in the true timeline.
- Suspect alibis and opportunity windows must be physically testable.
- Atmospheric elements (weather, house creaks, closed curtains) are encouraged, but supernatural or unauthored external factors are strictly forbidden as solutions.

---

## 8. Specialized technical, forensic, and medical test boundaries

If a mystery involves specialized mechanisms (forensic analysis, toxicology, computer logs, financial ledgers, mechanical devices, medical records):
- The case must define what the player can inspect/test and what is out of scope.
- Plain-language explanations must be authored for all technical concepts.
- Safe refusal responses must be pre-authored for dangerous or out-of-scope actions (e.g., tasting unknown poison, requesting off-site lab work).
- The solution **must be solvable through authored clues** within the play area, without depending on unauthored external lab results, police experts, or specialized domain knowledge.

---

## 9. Player agency and fair evidence (Authoring Rules)

### Stable observable evidence

Ordinary observable evidence must remain physically stable.

An observable mark, stain, smell, missing part, label, damage, unusual placement, ordinary content, or physical oddity present in a scene must be authored as observable upon fair close inspection. Do not hide physical observations behind interpretation prerequisites.

### Observation vs. Interpretation boundary

Authoring must separate:
1. **Observation**: Physical facts visible or discoverable on inspection.
2. **Witness Claim**: Testimony given by NPCs.
3. **Document Fact**: Text written in discovered documents.
4. **Interpretation**: Meaning, theory, or clue synthesis (gated by prerequisites).

### Neutral case board seeding

`caseBoardSeed` entries must use neutral language (e.g., `Known fact`, `Known claim`, `Known evidence`, `Unresolved significance`). Authors must not seed the case board with leading language that performs deductions for the player.

---

## 10. Image and visual asset authoring rules

### Supportive, not canonical

Images enrich the visual experience, but text remains canonical.
- No essential clue may exist exclusively in an image without text fallback.
- Images must not replace descriptive text narration.

### Visual definitions (`visualDefinitions`)

When image mode is enabled or optional, the package must author visual definitions for major scenes, close-ups, evidence photos, maps, and portraits:
- `requiredVisibleObjectIds`: Objects that must be depicted.
- `forbiddenObjectIds`: Objects that must not appear (prevents unauthored clue visual drift).
- `fixedGeometryNotes` & `continuityAnchor`: Fixed physical layout for repeated scene renders.
- `hiddenElementRules`: Concealed mechanisms, compartments, or internal details must not be rendered before discovery.
- `textFallback`: Full textual description for every visual asset.
