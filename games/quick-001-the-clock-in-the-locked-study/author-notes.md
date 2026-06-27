# Author Notes: The Clock in the Locked Study

## Purpose

This is the first full test case for the repository-backed Interactive Mystery Engine workflow.

It is intentionally small, constrained, and low-stakes so the schema, validation prompt, AI playtester, revision engine, and Game Master workflow can be tested without the complexity of a larger story.

## Design Choices

### Format

- Length preset: Quick Mystery
- One room only
- Three major NPCs
- Eight essential clues
- One red herring
- Theft instead of murder

### Reason for theft instead of murder

The first engine test should prioritize clean logic, scope control, clue closure, and validation. A theft case reduces motive and plausibility burden while still testing the core mystery structure:

- culprit;
- motive;
- method;
- opportunity;
- clue chain;
- red herring;
- final proof.

### Title

`The Clock in the Locked Study` was chosen because it is human-friendly, genre-appropriate, and names both the location and the key hiding mechanism.

### Culprit

Thomas Greer is the culprit.

The clue chain points to him through:

- access to the study;
- clock duties;
- oil transfer;
- livery thread;
- premature clock comment;
- hidden watch in the clock.

### Red herring

Celia's pawnshop envelope is the only red herring. It is intentionally simple and clearable.

The red herring should not overpower the physical evidence against Thomas.

## Known Risk Areas for Validation

1. Check whether Thomas's physical opportunity is sufficiently established.
2. Check whether the hinge method is physically plausible.
3. Check whether the watch hiding place inside the clock is believable.
4. Check whether Celia's pawnshop envelope is fair and clearable.
5. Check whether eight essential clues is too many for a Quick Mystery.
6. Check whether the Game Master can avoid revealing the clock solution too early.
7. Check whether schema compatibility is clean, especially around `slug` and case identity fields.

## Self-Check

- Culprit fixed: yes.
- Motive proportional: yes, for theft.
- Method defined: yes.
- Opportunity defined: yes.
- Timeline defined: yes.
- Evidence provenance defined: yes.
- Clue closure defined: yes.
- Red herring clearable: yes.
- Scope within Quick Mystery constraints: yes.
- Images optional and non-canonical: yes.

## Status

Draft complete.

Ready for Validator as step 2.
