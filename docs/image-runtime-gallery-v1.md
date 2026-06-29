# Image Runtime Gallery v1

## Purpose

This document defines how AI_IF tracks, recalls, and reuses images during runtime.

Images are optional visualizations. Text remains canonical. No required clue may exist only in an image.

## Core Rule

Every generated or shown image must become a tracked runtime image asset.

The Game Master must not treat images as disposable. If the player asks to see a prior image, the GM should recall or describe the existing image rather than generating a different one.

## Runtime Image Record

Each shown image should be tracked with:

- imageNumber;
- assetId, if connected to a package asset;
- title or retrieval label;
- scene or location;
- associated evidence, if any;
- associated clue IDs, if any;
- image type: full-room, close-up, symbolic, empty-room, mood-only;
- player request that caused the image;
- shownAt or approximate sequence position;
- text fallback;
- canon fidelity notes;
- whether the image contains people;
- required visible people, if any;
- required absent people, if any;
- required visible objects;
- forbidden objects;
- spoiler level;
- whether the image has already been shown.

## Supported Recall Commands

The GM should support player requests such as:

- show image 1;
- show image 2;
- show last image;
- show the previous image;
- list images;
- show gallery;
- describe image 3 again;
- remind me what was in the cigar case image;
- show the room image again.

## Reuse Rule

When the player asks to see a prior image:

1. Reuse the existing image if the platform supports it.
2. Do not generate a new image unless the player explicitly asks for a new visualization.
3. If exact reuse is unavailable, provide the stored text fallback.
4. Make clear that the fallback is a description of the prior visualization, not new evidence.

## No Regeneration Drift

Do not regenerate an old image merely because the player asked to see it again.

Regenerated images can drift from canon and may add or remove details. Reuse or describe the existing image instead.

## Image Gallery Rule

If the player asks for the gallery, list tracked images by:

- image number;
- short label;
- type;
- scene or evidence association;
- whether it was full-room, close-up, symbolic, or empty-room.

Do not include hidden solution facts in the gallery list.

## Text Is Canonical

Images are visual aids only.

The GM must not require the player to notice a clue in an image unless that same clue is available in text.

If an image conflicts with text, text wins.

The GM should correct the contradiction as a visualization issue rather than making it part of the mystery.

## Image Recall and Spoilers

When recalling an image, do not add interpretation that was not available when the image was first shown.

The GM may repeat the original text fallback or describe visible content, but must not add hidden solution facts.

## Validation Requirements

Validator must check:

- image assets include text fallbacks;
- full-room images specify required present people when relevant;
- image prompts do not add hidden clues;
- image prompts do not omit canonically present major NPCs unless the image is explicitly empty-room, symbolic, close-up, or mood-only;
- runtime instructions support image recall;
- no required clue depends only on image inspection.

## AI Playtest Requirements

AI playtester must test:

- requesting an image;
- asking to show the same image again;
- asking for image 1 or image 2;
- asking for the gallery;
- asking whether an image detail is evidence;
- checking that image recall does not create new clues or contradictions.
