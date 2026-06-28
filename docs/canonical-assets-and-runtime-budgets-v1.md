# Canonical Assets and Runtime Budgets v1

## Purpose

This specification defines how AI_IF packages declare what investigative assets exist and how far the Game Master may expand runtime interaction.

It strengthens Runtime Fidelity Engine v1 by making authored scope explicit.

## Core Rule

The Game Master may expose only authored investigative assets and may not exceed the package's runtime budgets.

If an asset is not in the canonical inventory, it cannot become investigative content during play.

If a runtime budget is exhausted, the Game Master must redirect to existing authored leads, summarize the case board, or transition toward deduction mode rather than expanding the case.

## Canonical Asset Inventory

`canonicalAssetInventory` is an optional game-package section that lists the canonical IDs the runtime may expose as investigative content.

Recommended fields:

- `npcIds`
- `locationIds`
- `objectIds`
- `evidenceIds`
- `documentIds`
- `imageIds`
- `discoveryRuleIds`
- `interviewTopicIds`
- `sceneIds`
- `clueIds`
- `redHerringIds`

The inventory does not replace canonical sections such as `characters`, `locations`, `evidence`, `scenes`, or `discoveryRules`. It is an explicit runtime allowlist derived from them.

Image assets and visual definitions are part of canonical asset enforcement. The Game Master may not generate visual content that exceeds authored image inventory, visual definitions, image reuse policy, or image budget.

## Authored Investigative Assets

An authored investigative asset is any package-defined item that can affect investigation, deduction, accusation, or proof.

Examples:

- a suspect or interviewable NPC;
- an investigative location;
- a searchable object;
- a clue-bearing prop;
- an evidence item;
- a document with case relevance;
- an image or visual asset with canonical text fallback;
- a discovery rule;
- an NPC interview topic;
- a scene branch or player-facing lead.

## Permitted Atmosphere

Permitted atmosphere is descriptive content that does not create investigative affordances.

Examples:

- crowd murmur;
- weather;
- room texture;
- ordinary furniture that is not searchable evidence;
- nameless staff movement;
- harmless sensory detail.

Atmosphere must remain non-decisive. It cannot become a clue, witness, document, evidence item, access route, or suspect source.

## Runtime Budgets

`runtimeBudgets` is an optional game-package section that defines maximum runtime scope.

Recommended fields:

- `maxMajorNPCs`
- `maxInterviewableNPCs`
- `maxBackgroundCharacters`
- `maxPrimaryLocations`
- `maxSecondaryLocations`
- `maxSearchableObjects`
- `maxEvidenceItems`
- `maxDocuments`
- `maxImages`
- `maxDiscoveryRules`
- `maxRedHerrings`
- `maxInterviewTopics`
- `maxHints`
- `maxPlayerFacingBranches`
- `hardBudgetFields`
- `softBudgetFields`

Budgets should be derived from the selected length preset, difficulty, and case design.

## Hard and Soft Budgets

Hard budgets cannot be exceeded during play.

Use hard budgets for:

- primary locations;
- major NPCs;
- interviewable NPCs;
- evidence items;
- documents;
- discovery rules;
- red herrings;
- player-facing branches.

Soft budgets guide pacing and can be exceeded only when the authored package explicitly permits it.

Use soft budgets for:

- background characters;
- hints;
- atmospheric references;
- optional images.

For Quick Mysteries, primary locations, major NPCs, interviewable NPCs, essential clues, red herrings, and player-facing branches should be treated as hard budgets.

## Length and Difficulty Defaults

For `quick_mystery` packages:

- one primary location;
- no more than 3 major NPCs;
- no more than 3 interviewable NPCs unless explicitly allowed;
- no more than 10 essential clues;
- no more than 1 red herring;
- tightly limited searchable objects, evidence, documents, images, and player-facing branches.

Larger presets may allow more secondary locations, documents, images, and player-facing branches, but the package must still declare the budget.

Difficulty should affect clue subtlety and hint policy before it expands scope.

## Exceeding a Budget

When a player attempts to exceed a budget, the Game Master should:

1. Check whether the requested asset is in `canonicalAssetInventory`.
2. Check whether the relevant runtime budget has remaining capacity.
3. If either check fails, give a natural negative or redirect response.
4. Optionally record a ruled-out area, closed lead, denied image request, or exhausted lead in runtime state.
5. Return to existing authored leads, case-board review, or deduction mode.

Do not add an investigative asset to satisfy the request.

Budget violations discovered during play should be captured in a Runtime Fidelity Report:

```text
docs/runtime-fidelity-report-v1.md
schemas/runtime-fidelity-report.schema.json
```

## Background Characters

Background characters count only as atmosphere unless the package authors them as NPCs.

They may:

- create scene texture;
- answer that they do not know;
- point back to authored staff, suspects, or locations.

They may not:

- become interview targets;
- provide alibis;
- provide witness testimony;
- reveal clues;
- create new leads;
- supply evidence or documents.

If a background character would logically have case knowledge, the Story Author should make that character an authored NPC or the Validator should flag the gap.

## Authored NPCs vs Background Characters

Authored NPCs have stable IDs, roles, knowledge boundaries, and interview topics.

Background characters have no investigative ID, no topic inventory, and no authority over clues or timeline facts.

The Game Master must not convert a background character into an authored NPC during play.

## Searchable Objects vs Descriptive Objects

Searchable objects can trigger investigation, discovery rules, evidence recovery, negative investigation, or case-board updates.

Descriptive objects are atmosphere. They may be described, but they cannot become clue-bearing unless authored.

If the player searches a descriptive object, the Game Master should provide a natural negative result and redirect to authored searchable objects.

## Evidence vs Flavor Props

Evidence items have stable IDs, provenance, access history, discovery conditions, and clue relationships.

Flavor props add texture but do not affect proof.

Flavor props must not become evidence during play.

## Documents vs Incidental Writing

Investigative documents have stable IDs or evidence IDs and can support clue discovery, evidence provenance, timeline, motive, or proof.

Incidental writing may exist as atmosphere but cannot introduce new names, dates, alibis, maps, codes, or proof.

## Images and Visual Assets

Images and visual assets are part of the canonical inventory when they have stable asset IDs.

Images must not introduce hidden clues, objects, routes, documents, suspects, or scene details absent from text.

If the player requests an unauthored image or the image budget is exhausted, the Game Master should use a text description or decline naturally according to image mode and runtime fidelity rules.

## Validator Responsibilities

The Validator should check:

- inventory completeness against package IDs;
- budget consistency with length preset and difficulty;
- every discovery rule references authored assets;
- every NPC interview topic belongs to an authored NPC;
- case-board seed entries do not expose unauthored or hidden assets;
- Quick Mystery packages do not exceed scope;
- unsupported player requests can be handled without runtime invention.

## AI Playtester Responsibilities

The AI Playtester should attempt:

- questioning background characters;
- searching beyond authored objects;
- requesting extra witnesses, evidence, locations, documents, and images;
- exhausting authored leads;
- asking for additional branches after the case should enter deduction mode.

The playtest should report whether the Game Master refuses or redirects without inventing content.

## Revision Engine Responsibilities

The Revision Engine should repair:

- missing inventory IDs;
- budget mismatches;
- overbroad runtime affordances;
- unauthored investigative paths;
- package scope violations.

Repairs should either add authored support within scope or remove misleading affordances.

## Runtime State Tracking

Runtime state may track budget usage through compact ID lists, such as:

- `usedNpcIds`
- `usedLocationIds`
- `usedObjectIds`
- `usedEvidenceIds`
- `usedDocumentIds`
- `usedDiscoveryRuleIds`
- `exhaustedLeadIds`
- `deductionModeEntered`

Runtime state should not duplicate the full case board or the full canonical inventory.
