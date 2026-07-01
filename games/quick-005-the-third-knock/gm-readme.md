# Game Master README: The Third Knock

## Case

- Case ID: `quick-005`
- Title: `The Third Knock`
- Status: ready_for_human_play
- Validation status: passed
- Playtest status: passed
- Human play status: not_played
- Notes: Classic contained rational seance mystery; validation and AI playthrough passed; images not required.

## Canonical Source

The canonical source for this case is:

```text
games/quick-005-the-third-knock/game-package.json
```

Use `case-board-seed.json` for the starting player-facing board and `asset-manifest.json` for optional image/text-fallback assets.

Do not rely on external notes or memory as canonical truth.

## Runtime Constraints

- Quick Mystery.
- One primary location.
- Three major NPCs.
- Images are off by default and optional only if the runtime supports visualization.
- Text is canonical.
- Hints are available only on request.
- No supernatural solution.
- No technical or forensic dependency.
- Do not add additional investigative locations, witnesses, suspects, documents, evidence, or clue paths.
- Do not add off-screen witnesses, police, servants, doctors, neighbors, relatives, or outsiders.
- Do not repeatedly steer toward a single suspect unless the player asks for a hint or theory check.
- If the player accuses early, distinguish plausible theory from proven accusation.
- If the player uses an unknown or ambiguous name in voice play, clarify instead of guessing.

Allowed atmosphere:

- candlelight;
- old house sounds;
- closed curtains;
- ordinary room creaks;
- seance tension.

Forbidden runtime expansion:

- no new servants as witnesses;
- no police lab branch;
- no doctor or autopsy branch;
- no secret passage;
- no hidden outsider;
- no additional supernatural mechanism beyond atmosphere and authored trick effects.

## Test Boundaries

This case has no required technical, forensic, medical, financial, mechanical, legal, or specialized test dependency.

If the player asks for external experts, medical testing, police forensics, or later formal reports, explain that formal processes may follow after the scene, but the playable fair-proof question is motive, access, timing, physical evidence, and contradicted statements available inside the parlor.

Do not invent lab results, medical conclusions, external witnesses, or off-screen investigative branches.

## Runtime Guidance

Follow:

```text
docs/runtime-engine-v2.md
docs/runtime-fidelity-engine-v1.md
docs/reverse-mystery-authoring-and-resolution-v1.md
docs/human-engagement-and-playability-v1.md
docs/player-agency-and-fair-evidence-v1.md
docs/suspect-deception-and-red-herring-discipline-v1.md
docs/classic-whodunit-pattern-v1.md
docs/discovery-rules-v1.md
docs/npc-interview-model-v1.md
docs/image-fidelity-contract-v1.md
docs/image-runtime-gallery-v1.md
```

When authored leads are exhausted, transition to deduction mode. Recaps must remain balanced across suspects unless the player asks for a hint or theory check.

Do not reveal hidden solution facts until the player solves the case, asks to end the case, or explicitly asks out of game for the canonical answer.
