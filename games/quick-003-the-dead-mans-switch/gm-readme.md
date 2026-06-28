# Game Master README: The Dead Man's Switch

## Case

- Case ID: `quick-003`
- Title: `The Dead Man's Switch`
- Status: draft
- Validation status: not validated
- Playtest status: not playtested

## Canonical Source

The canonical source for this case is:

```text
games/quick-003-the-dead-mans-switch/game-package.json
```

Use `case-board-seed.json` for the starting player-facing board and `asset-manifest.json` for optional image/text-fallback assets.

Do not rely on external notes or memory as canonical truth.

## Runtime Constraints

- Quick Mystery.
- One primary location.
- Three major NPCs.
- Images are off by default and optional on request.
- Text is canonical.
- Hints are available only on request.
- Do not add additional investigative locations, witnesses, suspects, documents, evidence, or clue paths.

Allowed background atmosphere:

- unnamed executives waiting outside;
- hallway noise;
- investor call countdown;
- general office tension.

Forbidden runtime expansion:

- no new interviewable executives;
- no outside hacker suspect as a real branch;
- no new IT employee;
- no new creditor NPC;
- no additional rooms;
- no new surveillance footage unless represented by authored logs;
- no new decisive clue outside the inventory.

## Runtime Guidance

Follow:

```text
docs/runtime-engine-v2.md
docs/runtime-fidelity-engine-v1.md
docs/reverse-mystery-authoring-and-resolution-v1.md
docs/discovery-rules-v1.md
docs/npc-interview-model-v1.md
docs/image-fidelity-contract-v1.md
```

When authored leads are exhausted, transition to deduction mode:

```text
You have examined the available evidence and questioned the three people in the room. The remaining task is deduction: reconcile the alert timing, the export log, cable access, and motive.
```

Do not reveal hidden solution facts until the player solves the case, asks to end the case, or explicitly asks out of game for the canonical answer.
