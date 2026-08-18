# Game Master README: The Third Knock (`quick-005`)

## 1. Case Identity

- **Case ID**: `quick-005`
- **Title**: The Third Knock
- **Length Preset**: `quick_mystery`
- **Genre**: Classic contained whodunit / rational seance mystery
- **Tone**: Tense, intimate, rational, fair-play
- **Player Role**: Detective.

## 2. Canonical Package Path

The sole canonical authority for this case is:

```text
games/quick-005-the-third-knock/game-package.json
```

Treat `game-package.json` as the single source of truth for all case facts, setting, NPCs, clues, evidence, discovery rules, initial case board seed, asset manifest, and solution logic. Do not rely on external notes or companion reports for canonical case truth.

## 3. Readiness State

- **Overall Status**: `ready_for_human_play`
- **Validation Status**: `passed`
- **Playtest Status**: `passed`
- **Human Play Status**: `not_played`
- **Notes**: Classic contained rational seance whodunit in a locked parlor. Validation and AI playthrough passed. Ready for human play.

## 4. Case-Specific Runtime Restrictions

Derived directly from `game-package.json`:

- **Configuration**:
  - `imageMode`: `player_requested_only`
  - `hintPolicy`: `on_request_only`
  - `interactionMode`: `voice_friendly`
- **Location Boundaries**:
  - Exactly 1 primary location (`loc-seance-parlor` - locked seance parlor).
  - All playable investigation occurs in the locked seance parlor. No other playable locations exist.
- **Suspect Scope**:
  - Exactly 3 major NPCs / suspects present in the room (`npc-clara-vane`, `npc-edmund-hallow`, `npc-lydia-harrow`).
- **Forbidden Case Expansions**:
  - No off-screen witnesses, police lab branch, medical/autopsy branch, servants, doctors, neighbors, relatives, or outsiders.
  - No secret passages.
  - No supernatural solution (supernatural elements are atmosphere and theatrical seance stagecraft only).

## 5. Session Initialization Notes

- Initialize player-facing state using `caseBoardSeed` embedded in `game-package.json`.
- Opening scene is `scene-opening` in `loc-seance-parlor` immediately following the third knock and collapse.
