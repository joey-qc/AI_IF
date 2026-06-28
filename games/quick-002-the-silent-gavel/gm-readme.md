# GM Readme: The Silent Gavel

## Startup

Read these files before play:

- `game-package.json`
- `case-board-seed.json`
- `asset-manifest.json`
- `human-play-handoff.md`

Use image mode off by default. Do not generate images during ordinary play.

## Runtime Board

If resuming an active session, read `case-board-current.json` first. If it does not exist, initialize the visible board from `case-board-seed.json`.

Update the current case board only with player-visible discoveries. Do not place hidden solution facts, clue meanings, undiscovered motives, or unrevealed timeline information on the current board.

## Spoiler Boundary

`game-package.json` contains the complete solution and GM-only truth. Keep those facts out of player-facing narration until the appropriate discovery rule, interview topic, comparison, or accusation condition reveals them.

## Fair Play

The case is solvable without guesswork if the player discovers the essential clues, compares the physical evidence, and tests NPC statements against the reception timeline. Do not invent new suspects, hidden rooms, or off-page evidence.
