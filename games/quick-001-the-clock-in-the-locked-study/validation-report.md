# Validation Report: The Clock in the Locked Study

## Verdict

FAIL

## Executive Summary

`The Clock in the Locked Study` is a strong first Quick Mystery draft. It has a fixed culprit, a contained one-room setting, a clear stolen object, a defined method, a recoverable piece of final proof, a limited suspect pool, and a single clearable red herring.

However, it should not proceed to AI playtesting yet. The case has one blocker and several major issues.

The blocker is motive discoverability: Thomas Greer's gambling-debt motive exists in the hidden solution but is not supported by a discoverable clue before the final reveal. That means the final explanation would introduce a key answer, "why," rather than confirming something the player could infer.

The case is repairable. The recommended next role is `prompts/05-revision-engine.md`.

## Blockers

### B1. Motive is not discoverable before the final reveal

**Severity:** Blocker

**Problem:**

The solution states that Thomas Greer stole the watch because he needed money to settle a gambling debt. The timeline includes `event-debt-threat`, but its `visibilityToPlayer` says this is hidden background motive discoverable only through Thomas's behavior or confession after proof.

No actual clue, evidence item, discovery rule, or NPC testimony gives the player a fair way to learn or infer the gambling debt before the final reveal.

**Why it matters:**

The final reveal must answer who, why, how, and proof. The package currently supports who, how, and proof well, but the why is not fairly discoverable.

If the Game Master reveals the debt only after Thomas is caught, the motive becomes newly introduced explanation rather than confirmed deduction.

**Recommended repair:**

Add or revise one discoverable motive clue. Keep it simple to preserve Quick Mystery scope.

Possible fixes:

1. Add a folded creditor note or betting slip in Thomas's waistcoat pocket, dropped near the tea trolley.
2. Add a small ledger tucked behind the clock-oil cloth showing Thomas's debt.
3. Let Celia mention that Thomas recently asked whether pawnshops buy watches.
4. Let Rowan mention that Thomas requested an advance and was refused.

Recommended simplest fix:

Add one supporting clue:

```text
clue-thomas-debt-note
```

This should not increase essential-clue count unless needed. It can be a supporting motive clue, keeping the essential clue chain focused on method and proof.

**Affected files or sections:**

- `game-package.json`
- `solution.md`
- `case-board-seed.json`, optional
- `author-notes.md`, optional

## Major Issues

### M1. Thomas's opportunity needs a more explicit distraction window

**Severity:** Major

**Problem:**

The package says Thomas removed the watch while moving normally through the room serving tea and adjusting the fire. This is plausible in broad terms, but the exact distraction or blind spot is not defined.

**Why it matters:**

The case occurs in one room with only three NPCs. If Thomas removes a watch from a display case while everyone is present, the package needs a clear reason no one sees him do it.

**Recommended repair:**

Add one precise opportunity beat to the timeline.

Example:

```text
At 8:10, Rowan turns to the desk to find the museum receipt while Celia bends to retrieve the pawn envelope she dropped. Thomas uses that moment, while setting down the tea tray beside the display case, to lift the loosened rear hinge and remove the watch.
```

This repair should appear in:

- `event-watch-stolen`
- Thomas's opportunity text
- Celia or Rowan witness knowledge, if needed

### M2. The Thomas clock contradiction clue has an unstable trigger

**Severity:** Major

**Problem:**

`clue-thomas-contradiction` says Thomas mentions the stopped clock too early. But the discovery condition says the clue can trigger when the player questions Thomas about the clock.

If the player asks about the clock, then Thomas mentioning the clock is not premature.

**Why it matters:**

The clue's incriminating value depends on Thomas volunteering clock knowledge before being prompted.

**Recommended repair:**

Revise the discovery condition so it triggers when the player asks Thomas about his movements, not when the player asks directly about the clock.

Possible revised trigger:

```text
Player asks Thomas to account for his movements after serving tea. Thomas volunteers that he wound the clock properly and it should not have stopped, even if the player has not yet mentioned the clock.
```

### M3. The hinge method needs one physical detail

**Severity:** Major

**Problem:**

The case says Thomas lifted the loosened rear edge of the display case enough to remove the watch. This is plausible, but the display case design is underspecified.

**Why it matters:**

A player may ask how a pocket watch can be removed through a rear hinge without opening the front lock or making obvious damage.

**Recommended repair:**

Add one concrete design detail:

```text
The case has a hinged rear service panel used for cleaning the velvet lining. Thomas loosened that rear service panel, not the front display door.
```

This makes the method cleaner and more physically plausible.

### M4. Schema compatibility issue: `slug` is not allowed by current machine schema

**Severity:** Major

**Problem:**

The game package includes `caseMetadata.slug`, which is correct according to the later case-library convention. However, the current machine-readable `schemas/game-package.schema.json` has `additionalProperties: false` for `caseMetadata` and does not list `slug` as an allowed property.

**Why it matters:**

Strict JSON Schema validation would fail even though the field is now part of the intended repository workflow.

**Recommended repair:**

Update `schemas/game-package.schema.json` so `caseMetadata` permits and preferably requires `slug`.

Also consider adding:

```json
"slug": { "type": "string", "pattern": "^[a-z0-9]+(?:-[a-z0-9]+)*$" }
```

## Minor Issues

### m1. Evidence `createdByCharacterId` is imprecise for inherited or manufactured objects

Some evidence entries use `createdByCharacterId` where `ownedByCharacterId` or `handledByCharacterId` would be more accurate.

Example:

- `evidence-pocket-watch` says it was created by Rowan Vale, but Rowan is the owner, not the maker.

This does not break the case, but the schema may eventually need clearer evidence provenance fields.

### m2. Title may imply a stronger locked-room puzzle than the package actually presents

The title says `Locked Study`, but the setup says the study door was closed, not necessarily locked. This is not a blocker, but if the intended player expectation is a locked-room puzzle, the package should clarify whether the door was locked or merely closed.

### m3. The red herring is fair, but slightly obvious once inspected

Celia's pawnshop envelope is clearable by reading the ticket. This is appropriate for Easy difficulty, but AI playtesting should verify that it is not dismissed too quickly.

## Notes

The draft does several things well:

- It stays within Quick Mystery scope.
- It has exactly one primary location.
- It uses three major NPCs.
- It keeps red herrings limited.
- It gives the Game Master a clear final proof object: the watch inside the clock.
- It avoids hidden image-only clues.
- It separates case-board seed data from runtime state.

## Category-by-Category Review

### 1. Solution completeness

**Status:** Mostly pass.

The package identifies:

- culprit: Thomas Greer;
- target: Breguet pocket watch;
- method: loosened rear hinge;
- opportunity: movement during service duties;
- concealment: hidden inside clock;
- proof: watch in clock plus thread/oil/hinge evidence.

Weakness: motive exists but is not discoverable before reveal.

### 2. Motive proportionality

**Status:** Pass in concept, fail in discoverability.

The motive is proportional for theft. A gambling debt is sufficient for stealing a valuable watch.

But the motive must be supported by a clue or inference path.

### 3. Timeline coherence

**Status:** Pass with revisions recommended.

The sequence is coherent:

1. Thomas is threatened by debt.
2. Thomas loosens the hinge in the afternoon.
3. The watch is shown at 7:55.
4. Thomas steals it around 8:10.
5. Thomas hides it in the clock at 8:13.
6. Rowan discovers the theft at 8:20.

Weakness: the 8:10 theft moment needs a more explicit distraction or sightline explanation.

### 4. Clue closure

**Status:** Pass with one major gap.

Most clues resolve cleanly. The physical clue chain works.

The motive clue is missing.

### 5. Evidence provenance

**Status:** Pass with minor schema concerns.

Evidence chain-of-custody is generally defined.

Minor concern: the evidence model conflates creation, ownership, and handling in a few places.

### 6. Physical plausibility

**Status:** Pass with major clarification needed.

The clock hiding place works.

The hinge method can work, but the case needs a more specific rear service panel or hinge design.

### 7. Suspect fairness

**Status:** Pass.

- Rowan has a possible insurance/donation motive but weak physical connection.
- Celia has an apparent money motive but clearable evidence.
- Thomas has the strongest physical evidence path.

### 8. Red herring fairness

**Status:** Pass.

Celia's pawnshop envelope is fair and clearable.

### 9. Solvability

**Status:** Fail pending motive repair.

The player can probably solve who and how. The player cannot fairly solve why without new information.

### 10. Scope and pacing

**Status:** Pass.

The case fits Quick Mystery limits:

- one room;
- three NPCs;
- one red herring;
- no nested secrets;
- fewer than ten essential clues.

### 11. Asset safety

**Status:** Pass.

Assets have text fallback and do not contain hidden image-only clues.

### 12. Game Master readiness

**Status:** Not ready.

The Game Master can run much of the case, but would have to invent or reveal the debt motive late unless the package is revised.

## Clue Closure Matrix

| Clue | Role | True meaning | Resolved? | Issue |
| --- | --- | --- | --- | --- |
| `clue-loose-hinge` | Essential | Watch left through rear hinge | Yes | Needs service-panel detail |
| `clue-brass-dust` | Essential | Hinge recently disturbed | Yes | None |
| `clue-black-thread` | Essential | Thomas's livery snagged on hinge | Yes | None |
| `clue-clock-oil` | Essential | Hinge handler also handled clock oil | Yes | None |
| `clue-stopped-clock` | Essential | Hidden watch stopped clock | Yes | None |
| `clue-scraped-clock-latch` | Essential | Clock compartment opened recently | Yes | None |
| `clue-watch-in-clock` | Essential | Watch hidden in clock | Yes | None |
| `clue-thomas-contradiction` | Essential | Thomas knows too much about clock | Partial | Trigger condition needs revision |
| `clue-celia-pawn-envelope` | Red herring | Celia pawned her bracelet | Yes | None |
| Missing motive clue | Supporting | Thomas has gambling debt | No | Blocker |

## Timeline Review

The timeline is logically ordered and mostly usable. The key repair is to define the exact distraction or blind spot during `event-watch-stolen`.

Current issue:

```text
Thomas removes the watch while everyone is in the same room, but the package does not define why nobody sees him do it.
```

Recommended repair:

```text
Give Rowan and Celia simultaneous attention breaks while Thomas is beside the display case with the tea tray.
```

## Motive Review

The motive works as an author-level explanation but fails as player-facing fair-play evidence.

Repair required before playtesting.

## Solvability Review

The physical solution is solvable.

The full solution is not yet solvable because the motive is not discoverable.

## Game Master Readiness

Not ready for Game Master use.

The Game Master would have to either:

1. reveal a new gambling-debt motive at the end; or
2. improvise a motive clue during play.

Both violate the project design principles.

## Required Revisions

1. Add a discoverable motive clue for Thomas's gambling debt.
2. Clarify Thomas's opportunity/distraction window during the theft.
3. Revise the Thomas clock contradiction trigger.
4. Clarify the physical design of the rear service panel or hinge.
5. Update `schemas/game-package.schema.json` to allow `caseMetadata.slug`.

## Recommended Next Step

Run `prompts/05-revision-engine.md`.

Do not proceed to AI Playtester yet.

## Final Validator Summary

- Verdict: FAIL.
- Top three required fixes:
  1. Add discoverable motive evidence.
  2. Clarify Thomas's exact opportunity to steal unseen.
  3. Repair the premature clock-comment clue trigger.
- Proceed to AI playtesting: No.
- Run Revision Engine next: Yes.
