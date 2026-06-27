# Playtest Findings

## Context

This document captures findings from the first full interactive mystery playtest.

The playtest began with a set of Markdown prompt files intended to make ChatGPT act as an interactive mystery Game Master. The selected game was a lighthearted classic detective mystery set in 1947 New York City.

The experience was engaging during investigation. The player could question NPCs, inspect evidence, request visual artifacts, revisit locations, and reason through clues conversationally. However, the mystery failed at resolution: the final reveal did not identify a coherent culprit, motive, method, proof structure, or complete explanation of the clues.

The purpose of this document is not to preserve the failed story as canon. Its purpose is to preserve the design lessons.

## High-level result

The playtest succeeded as a test of conversational investigation.

The playtest failed as a fair-play mystery.

This distinction is important. The conversational interface was valuable, but the underlying mystery-generation architecture was insufficient.

## What worked

### Conversational Game Master interface

The player enjoyed being able to interact with the Game Master naturally.

Useful interactions included:

- asking follow-up questions about evidence;
- interviewing NPCs;
- revisiting locations;
- requesting summaries;
- asking for images of discovered artifacts;
- testing theories;
- pursuing unexpected lines of inquiry.

This supports keeping an AI chatbot as the player-facing interface.

### Text-first gameplay

The game remained playable as text. Images were helpful when they showed artifacts, locations, photographs, or documents, but the player did not want images to contain hidden clues or replace narration.

### Artifact-style images

The strongest image opportunities were:

- photographs;
- maps;
- letters;
- diagrams;
- location visualizations;
- suspect portraits.

Images should support the case file rather than become the case file.

### Investigative structure

The player enjoyed following leads through:

- suspects;
- locations;
- physical evidence;
- documents;
- timeline reconstruction;
- contradictions in testimony.

This confirms that mystery investigation is a good fit for conversational AI.

## What failed

### 1. No coherent final culprit

By the end of the game, the story had not established who killed the victim.

Several suspects had partial suspicion attached to them, but the evidence did not converge on one provable culprit. The Game Master could not honestly reveal a culprit without inventing an answer after the fact.

### 2. Weak or collapsed motive

The hidden object at the center of the mystery was built up as the reason people were threatened, kidnapped, and killed.

When revealed, the document only showed that a famous composer had adapted or copied earlier music. That fact was academically interesting but not proportional to murder.

A murder mystery requires a motive with consequences. The secret must plausibly threaten someone with financial loss, exposure, ruin, prosecution, blackmail, institutional collapse, inheritance loss, or another serious consequence.

### 3. No complete who / why / how / proof structure

A satisfying detective solution must answer:

1. Who did it?
2. Why did they do it?
3. How did they do it?
4. How can the detective prove it?

The playtest did not answer these questions.

### 4. Clues lacked closure

Many clues were introduced but not resolved.

Examples included:

- anonymous threat letter;
- typewriter match;
- missing file page;
- orchestra button;
- red wool fiber;
- cryptic notebook warnings;
- visitor pass chronology;
- storage room access;
- unexplained suspect behavior;
- the origin of the manuscript;
- the identity of the person pursuing the client.

The system needs a clue closure matrix. Every significant clue should be explained by the final solution or explicitly identified as a red herring with a grounded explanation.

### 5. Chronology contradictions

The story introduced timeline details that did not reconcile.

Examples included:

- messages referring to "tomorrow" when the implied date no longer matched;
- events that required characters to know information before they plausibly could;
- object movements that did not match known access windows;
- meeting references that conflicted with discovered evidence.

A timeline validator is required.

### 6. Physical plausibility failures

Some dramatic events did not make physical sense.

Examples included:

- a missing man being found in a locked crate without a plausible method of entry, exit, air, or concealment;
- a letter supposedly left by a third party being found inside the missing man's jacket;
- a character attempting to burn a document using an electric lamp before an ignition source had been established.

The system needs physical action precondition checks.

### 7. Evidence provenance failures

Some evidence appeared without a credible chain of custody or access history.

Future cases must answer:

- Who created this evidence?
- When was it created?
- Where was it stored?
- Who had access to it?
- How did the player find it?
- Why was it not found earlier?
- How does it fit the known timeline?

### 8. Excessive scope growth

The requested game length was one sitting, roughly 30 to 60 minutes. The investigation expanded to too many locations, suspects, and open leads.

The system needs a story scope budget tied to difficulty and desired duration.

For a short case, the engine should limit:

- number of suspects;
- number of major locations;
- number of clue chains;
- number of nested secrets;
- number of red herrings;
- number of late-game reveals.

### 9. Game Master over-improvisation

The Game Master generated compelling scenes but did not reliably preserve a fixed hidden solution.

This suggests that the Game Master should not be the primary mystery author during gameplay. It should run a pre-authored, validated game package.

### 10. No solution file

There was no external `solution.md` equivalent that the Game Master could consult at the end.

If a future Game Master cannot answer all major questions by reading the solution file, the game package is not ready for play.

### 11. No validation gate before play

The original workflow moved directly from prompt instructions to gameplay.

A future workflow needs explicit gates:

1. Generate draft case.
2. Validate internally.
3. AI-playtest externally.
4. Revise.
5. Revalidate.
6. Approve for play.

### 12. Image library was missing

Images created during play became difficult to reference later.

Future cases should maintain an asset library with labels, descriptions, discovery status, and retrieval commands.

### 13. Case board was missing

The player would benefit from an explicit case board tracking:

- suspects;
- known facts;
- evidence;
- locations;
- visited/unvisited leads;
- contradictions;
- theories;
- open questions.

The case board should be maintained separately from prose narration.

## Requirements derived from the playtest

| Finding | Required design response |
| --- | --- |
| No culprit resolution | Solution file must name culprit before play. |
| Weak motive | Motive must be validated for proportionality. |
| Unresolved clues | Clue closure matrix required. |
| Timeline problems | Chronology validator required. |
| Physical impossibilities | Physical plausibility checks required. |
| Evidence appeared arbitrarily | Evidence provenance fields required. |
| Scope creep | Difficulty and length budgets required. |
| Over-improvisation | Separate authoring from Game Master runtime. |
| No QA cycle | Validator and AI playtester tiers required. |
| Lost images | Asset repository required. |
| Player state unclear | Case board manager required. |

## Design implications

The project should move from a single prompt to a repository-backed workflow.

The minimum viable workflow should include:

1. Game package schema.
2. Story author prompt.
3. Validator prompt.
4. AI playtester prompt.
5. Revision prompt.
6. Game Master prompt.
7. Case board file.
8. Asset manifest.
9. Solution file.

## Success criteria for the next playtest

The next playtest should be considered successful only if:

- the culprit is known before gameplay starts;
- the motive is strong enough to justify the crime;
- every major clue is explained;
- the final reveal answers who, why, how, and proof;
- the player can request a case-board summary at any time;
- images are retrievable by label;
- the game stays within the requested scope;
- the Game Master can answer endgame questions without inventing new facts.

## Conclusion

The first playtest showed that the project concept is promising but that prompt-only improvisation is not sufficient for fair-play detective fiction.

The next version should treat mystery generation more like compiling and validating a structured game package than improvising a story in real time.
