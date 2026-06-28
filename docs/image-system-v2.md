# Image System v2

## Purpose

This document defines Image System v2 for the AI Interactive Fiction project.

Images are optional, supportive visualizations. They are not the canonical source of essential evidence.

The system exists to make images useful without allowing them to reveal hidden clues, add non-canonical details, or drift away from the authored setting.

Image fidelity is governed by the stricter runtime layer:

```text
docs/image-fidelity-contract-v1.md
```

Image System v2 defines image classes and general image safety. Image Fidelity Contract v1 defines whether a generated or shown image remains faithful to canonical scene geometry, required visible objects, forbidden objects, continuity anchors, reuse policy, and text fallback.

## Core rules

1. Images must follow the same observation layers as text.
2. Images must not contain essential clues absent from text.
3. Images must not introduce new suspects, locations, props, exits, labels, maps, symbols, or mechanisms not supported by the package.
4. Images must obey the package's era, setting, tone, and asset guidance.
5. Every generated image must have a text fallback.
6. The Game Master must remain able to run the case without images.
7. Every image must derive from canonical package data.
8. Repeated images of a location must preserve canonical scene geometry.
9. Evidence photos and cutaways must follow their own visual definitions and cannot use scene-image rules.

## Image classes

Image System v2 defines three primary classes:

```text
Scene Image
Inspection Image
Evidence Image
```

## Scene Image

A scene image shows the immediate observable environment.

A scene image may show:

- room layout;
- obvious furniture;
- visible people;
- visible objects;
- lighting;
- weather through windows;
- general atmosphere.

A scene image must not show:

- hidden compartments;
- close forensic traces;
- secret markings;
- undiscovered documents in readable detail;
- labels or diagrams;
- clue-highlight arrows;
- objects not in the package.

Repeated scene images must preserve the same canonical layout, required visible objects, major furniture positions, and continuity anchors unless the package defines a player-visible change.

## Inspection Image

An inspection image is generated only after the player inspects a specific object, area, or person.

It may show:

- close-up object details;
- scratches;
- dust patterns;
- disturbed surfaces;
- visible residues;
- object condition;
- readable document portions already revealed in text.

It must not show:

- the final interpretation of the clue;
- undiscovered related evidence;
- hidden solution facts;
- details that require a later comparison.

## Evidence Image

An evidence image is generated only after evidence has been recovered, exposed, or identified in text.

It may show:

- recovered objects;
- documents the player has read;
- close-up evidence already discovered;
- comparison exhibits when both compared items are known.

It must not show:

- secret conclusions;
- undiscovered inscriptions;
- clue text not already available to the player;
- future discoveries.

Evidence photos differ from scene illustrations. They should focus on the discovered evidence and must not add unauthored markings, props, labels, or contextual clues.

## Technical cutaways

Technical cutaways are allowed only when the player has discovered the relevant hidden structure or mechanism and the package permits the cutaway.

A cutaway must preserve physical geometry. It must not reveal concealed mechanisms, rear access, internal compartments, or hidden routes before discovery.

## Visibility vs discovery

An object may appear in a scene image before it is investigated.

That is allowed.

Example:

A mantle with objects on it may appear in a room image if the mantle is plainly visible.

However, the image must not reveal that one object on the mantle is significant unless that significance has already been earned in text.

The image may show the object. It must not reveal its hidden meaning.

## Asset generation guidance

Each game package may include top-level `assetGenerationGuidance`.

This should include:

- image mode;
- style constraints;
- canonical room or era constraints;
- prohibited additions;
- text fallback requirement.

Example fields:

```json
{
  "assetGenerationGuidance": {
    "imageMode": "player_requested_only",
    "styleConstraints": [
      "Late 1940s mid-century private townhouse study.",
      "Do not add non-canonical props.",
      "Images are supportive only."
    ],
    "textFallbackRequired": true
  }
}
```

## Per-asset guidance

Each asset may include `imagePromptGuidance`.

This narrows the generated image to the specific asset.

Examples:

```text
Depict the canonical display case only after text discovery. Do not imply a broken front lock or add extra mechanisms.
```

```text
Depict the recovered pocket watch only after text discovery. No hidden inscriptions or additional clues.
```

## Image prompt construction

When generating an image, the Game Master should build the prompt from:

```text
1. Asset class: scene, inspection, or evidence.
2. Canonical setting and era.
3. Player's current observation layer.
4. Visible objects already established.
5. Discovered inspection details, if any.
6. Per-asset guidance.
7. Prohibited additions.
8. Text fallback.
```

Do not generate from free association.

Do not let the image model invent evidence.

Generated images must not create unauthored objects, unauthored exits, unauthored suspects, unauthored clues, or unauthored geometry.

## Player request handling

When the player requests an image, the Game Master should silently ask:

1. Is image mode enabled?
2. What asset or scene is being requested?
3. Has the player discovered enough to see this asset?
4. Is this scene, inspection, or evidence image?
5. What details are allowed at this stage?
6. What details must remain hidden?
7. What text fallback should accompany the image?

If the requested image would reveal hidden information, provide a safer image or explain that a closer inspection is needed first.

If the requested image would violate canonical visual definitions or continuity, provide text fallback instead.

## Text fallback

Every image response must include or be paired with a text fallback.

The text fallback is canonical.

The image is illustrative.

If image and text conflict, the text and game package control.

If an image omits a required visible object or adds a forbidden object, treat the image as non-canonical and record the issue in runtime notes or a Runtime Fidelity Report when in evaluation mode.

## Preventing style drift

Postgame review from `quick-001` showed that image generation can drift into the wrong historical style.

To prevent drift:

- include era in every image prompt;
- include prohibited eras if relevant;
- specify only canonical objects;
- forbid extra props or decorations that look clue-like;
- keep prompts concrete.

Example:

```text
Late 1940s mid-century private townhouse study, not Victorian or Edwardian.
```

## No hidden visual-only clues

Essential clues must exist in text.

Images may depict an already discovered clue, but they must not be required to solve the case.

If a player uses voice-only mode or disables images, the mystery must remain solvable.

## Asset manifest implications

The asset manifest should track:

- asset ID;
- title;
- type;
- image class;
- associated location;
- associated clues;
- discovery conditions;
- spoiler level;
- text fallback;
- whether shown;
- prompt guidance.

Recommended future fields:

```text
imageClass
observationLayer
imagePromptGuidance
allowedVisibleElements
forbiddenVisibleElements
```

Current packages may also use optional `visualDefinitions`, `imageGalleryPolicy`, `imageReusePolicy`, `evidencePhotoDefinitions`, and `cutawayDefinitions` in `game-package.json`.

## Validator implications

The Validator should check:

- no asset has hidden clue-only content;
- every asset has text fallback;
- scene images contain only immediate-observation details;
- inspection images require inspection triggers;
- evidence images require discovery triggers;
- image guidance does not contradict setting or canon.
- visual definitions include required objects for central scene images when images are enabled or optional;
- cutaway and evidence photo definitions do not reveal hidden mechanisms prematurely.

## Game Master implications

The Game Master should:

- ask permission or follow player-requested image mode;
- avoid automatic images unless configured;
- never use an image to advance the case without a text clue;
- record seen assets in runtime state;
- make generated images retrievable by label;
- treat images as supportive, not canonical.

Image fidelity issues should be captured in a Runtime Fidelity Report when an image adds non-canonical details, reveals hidden information early, exceeds image budgets, contradicts text, or is not recorded consistently.

## Failure conditions

The image system fails if:

- an image reveals a hidden clue before text does;
- an image adds a new clue not in the package;
- an image adds a new suspect, exit, or object that affects play;
- an image contradicts the era or setting;
- the Game Master relies on an image to convey essential evidence;
- the case becomes unsolvable when images are disabled.
