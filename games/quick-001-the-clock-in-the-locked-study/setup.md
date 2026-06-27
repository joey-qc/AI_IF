# Setup: The Clock in the Locked Study

## Case Identity

- Case ID: `quick-001`
- Title: `The Clock in the Locked Study`
- Slug: `the-clock-in-the-locked-study`
- Folder: `games/quick-001-the-clock-in-the-locked-study`

## Player-Facing Setup Summary

A compact classic-detective mystery set entirely inside one private study in a mid-century townhouse. A valuable heirloom pocket watch vanishes during a small family gathering, even though the room was closed, the display case was locked, and only three people were present.

The player is a private detective asked to determine who took the watch, how they did it, and where the watch is now.

## Configuration

- Length preset: `quick_mystery`
- Difficulty: `easy`
- Genre: `classic detective`
- Tone: `lighthearted`
- Setting: A single locked study in a mid-century private townhouse
- Era: Mid-20th century, approximately late 1940s
- Player role: Private detective
- Image mode: `player_requested_only`
- Interaction mode: `text_first`
- Hint policy: `gentle_when_stuck`
- Content boundaries: No graphic violence; no horror; no sexual content

## Scope Budget

- Primary locations: 1
- Major NPCs: 3
- Essential clues: 8
- Red herrings: 1
- Nested secrets: 0
- Expected play time: 10 to 25 minutes

## Special Requests

- Designed as the first end-to-end engine test case.
- Keep all gameplay inside one room.
- Make the final reveal answer who, why, how, and proof.
- Keep images optional and supportive only.

## Assumptions

- The mystery is theft rather than murder to keep the first test compact and easier to validate.
- The story should prioritize clean clue logic over dramatic complexity.
- The title is provisional but suitable for human-friendly library browsing.

## Next Recommended Role

Run `prompts/02-story-author.md` using this setup as input.
