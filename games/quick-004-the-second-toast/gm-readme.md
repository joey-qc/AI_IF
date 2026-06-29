# Game Master README: The Second Toast

## Case

- Case ID: `quick-004`
- Title: `The Second Toast`
- Status: approved_for_human_play
- Validation status: passed
- Playtest status: passed
- Human play status: not_played
- Notes: Proof-gating finalized; package validation and AI playthrough passed.

## Canonical Source

The canonical source for this case is:

```text
games/quick-004-the-second-toast/game-package.json
```

Use `case-board-seed.json` for the starting player-facing board and `asset-manifest.json` for optional image/text-fallback assets.

Do not rely on external notes or memory as canonical truth.

## Runtime Constraints

- Quick Mystery.
- One primary location.
- Four major NPCs.
- Images are off by default and optional on request.
- Text is canonical.
- Hints are available only on request.
- Do not add additional investigative locations, witnesses, suspects, documents, evidence, or clue paths.
- Do not repeatedly steer toward a single suspect unless the player asks for a hint or theory check.
- If the player accuses early, distinguish plausible theory from proven accusation.
- If the player uses an unknown or ambiguous name in voice play, clarify instead of guessing. Example: "There is no Ellen in the room. Did you mean Eleanor, Mara, Beatrice, Julian, or Felix?"

Allowed background atmosphere:

- rain at the windows;
- old house sounds;
- distant household staff already dismissed and not interviewable;
- family tension.

Forbidden runtime expansion:

- no new servants as witnesses;
- no police lab branch;
- no autopsy rabbit hole;
- no secret passage;
- no hidden outsider;
- no additional poison mechanism beyond the authored cordial glass.

## Poison and Test Boundaries

If the player asks for toxicology, lab testing, police forensics, or a precise chemical name, explain that police and medical testing will follow, but the playable fair-proof question is motive, access, timing, and physical evidence at the dinner table.

Do not invent a named poison, lab result, autopsy branch, or external expert.

If the player asks to taste the cordial, refuse safely. Evidence should be isolated. The GM may describe odor, residue, placement, and witness timing because those are authored.

## Runtime Guidance

Follow:

```text
docs/runtime-engine-v2.md
docs/runtime-fidelity-engine-v1.md
docs/reverse-mystery-authoring-and-resolution-v1.md
docs/human-engagement-and-playability-v1.md
docs/discovery-rules-v1.md
docs/npc-interview-model-v1.md
docs/image-fidelity-contract-v1.md
```

When authored leads are exhausted, transition to deduction mode. Recaps must remain balanced across suspects unless the player asks for a hint or theory check.

Do not reveal hidden solution facts until the player solves the case, asks to end the case, or explicitly asks out of game for the canonical answer.
