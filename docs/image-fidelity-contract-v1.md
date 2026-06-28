# Image Fidelity Contract v1

## Purpose

Image Fidelity Contract v1 defines strict runtime rules for generated or shown images in AI_IF.

Images are optional, supportive runtime outputs. They must remain faithful to canonical game-package content, preserve scene continuity, and never introduce or omit important story objects.

## Image System vs Image Fidelity

`docs/image-system-v2.md` defines image classes, text fallback, and general image safety.

This contract is stricter. It governs whether a specific image is faithful to the authored package and runtime state.

The Image System answers:

- what kinds of images exist;
- when images are allowed;
- how images support text.

Image Fidelity answers:

- whether the image matches canon;
- whether required objects are present;
- whether forbidden objects are absent;
- whether geometry and continuity are preserved;
- whether an existing image must be reused;
- whether hidden elements are shown only when earned.

## Core Rule

Every image must derive from canonical package data and current player-visible runtime state.

An image must not:

- add unauthored objects;
- add unauthored exits;
- add unauthored suspects or background characters that look investigative;
- add unauthored clues;
- omit required visible story objects;
- change scene layout across repeated images;
- violate physical geometry;
- reveal hidden mechanisms before discovery;
- contradict text fallback or the canonical package.

If image fidelity cannot be maintained, the Game Master should provide text fallback instead.

## Canonical Visual Definitions

Packages may define `visualDefinitions` in `game-package.json`.

Each visual definition may include:

- `visualDefinitionId`;
- `locationId`;
- `imageType`;
- `canonicalDescription`;
- `requiredVisibleObjectIds`;
- `optionalVisibleObjectIds`;
- `forbiddenObjectIds`;
- `fixedGeometryNotes`;
- `cameraAllowedViews`;
- `hiddenElementRules`;
- `continuityAnchor`;
- `textFallback`;
- `validationNotes`.

Visual definitions are the source of truth for image prompts. They do not replace `assetManifest`; they constrain how assets and scenes may be shown.

## Scene Visual Continuity

Repeated images of the same location must preserve canonical scene geometry.

Continuity includes:

- room shape;
- doors, windows, and exits;
- major furniture positions;
- display cases, cabinets, desks, and other story-bearing objects;
- relative positions of required visible objects;
- lighting or weather details when they affect investigation.

The Game Master must not regenerate a canonical scene image from scratch when a prior image should be reused.

Use a new image only when:

- the player requests a new allowed view;
- a visual definition permits a different camera angle;
- the scene has changed in a player-visible, authored way;
- an inspection close-up, evidence photo, map, or cutaway is requested and permitted.

## Required Visible Objects

Required visible objects are authored objects that must appear in a scene or asset image because their absence would misrepresent the case.

Examples:

- central plot objects visible at scene start;
- major furniture required for geometry;
- visible evidence containers;
- known doors or access points;
- scene-defining objects named in opening narration.

If a required object cannot be reliably shown, use text fallback instead of a misleading image.

## Forbidden Visible Objects

Forbidden visible objects are objects that must not appear in an image.

Examples:

- unauthored props that look clue-like;
- extra doors, windows, compartments, or tools;
- suspects or witnesses not present in the package;
- hidden mechanisms before discovery;
- labels, arrows, diagrams, or readable text not available in text;
- anachronistic or off-tone elements.

## Permitted Image Types

Permitted image types include:

- `scene`;
- `inspection_closeup`;
- `evidence_photo`;
- `technical_cutaway`;
- `map`;
- `memory_recall`;
- `portrait`;
- `other`, when explicitly justified by the package.

Each type has different fidelity rules.

## Scene Images

Scene images show immediate observation only.

They may show authored visible layout and objects. They must not show hidden interiors, rear panels, concealed mechanisms, clue-highlight marks, or undiscovered evidence.

## Inspection Close-Ups

Close-ups require player action and an authored inspection target.

They may show player-visible surface detail that the player has earned. They must not show interpretation or undiscovered related evidence.

## Evidence Photos

Evidence photos require the evidence to be discovered or recovered in text first.

They should show the evidence as described in text and should not add new markings, labels, inscriptions, or associations.

## Technical Cutaways

Cutaways may show internal geometry only when:

- the player has discovered the relevant mechanism or hidden structure;
- the package or visual definition permits the cutaway;
- the cutaway does not reveal later proof early;
- text fallback states the same information.

Cutaways must preserve physical plausibility. Rear panels, hidden compartments, hinges, routes, and access points must appear in positions compatible with the authored location.

## Maps

Maps may show authored spatial relationships only.

They must not add exits, rooms, corridors, routes, labels, or objects absent from the package.

## Memory and Recall Images

Image recall should reuse previously shown images whenever possible.

Supported commands may include:

- "show scene";
- "show image 2";
- "show evidence photo";
- "show close-up";
- "show the previous room image".

Recall must not regenerate an inconsistent replacement. If the original image is unavailable, provide the recorded text fallback and explain that the visual cannot be safely recreated.

## Hidden Compartments and Internal Geometry

Hidden compartments, rear panels, concealed mechanisms, and internal geometry must not appear in scene images before discovery.

After discovery, they may appear only in:

- inspection close-ups;
- evidence photos;
- technical cutaways;
- maps or diagrams explicitly allowed by the package.

The image must match the authored physical mechanism. If the model cannot represent it faithfully, use text fallback.

## Physical Impossibilities

Images must not:

- place rear access on the wrong side of an object;
- move doors or windows between views;
- make objects too large or too small for their function;
- change room layout between repeated images;
- imply impossible lines of sight;
- add impossible hiding spaces;
- contradict the timeline or object movement.

Physical impossibility is runtime drift.

## Text Fallback

Every image must have text fallback.

The text fallback is authoritative. If image and text conflict, text and the canonical package control.

If an image omits required objects or adds forbidden objects, the Game Master should correct the record in text and prefer fallback over reuse.

## Image Failure or Mismatch

If an image is missing required objects, contains forbidden objects, changes geometry, reveals hidden content, or contradicts canon:

1. Do not treat the visual detail as canonical.
2. State the canonical text fallback.
3. Record the mismatch in runtime state or session notes when in playtest/evaluation mode.
4. Prefer reusing a faithful prior image if one exists.
5. Capture the issue in a Runtime Fidelity Report.

## Runtime Fidelity Reporting

Image issues should be captured in Runtime Fidelity Reports when they include:

- missing required objects;
- unauthored objects introduced by images;
- visual continuity drift;
- physical geometry violations;
- image-only clue risks;
- regenerated scene inconsistencies;
- image reuse failures;
- mismatched evidence photos or cutaways.

Runtime Fidelity Reports are governed by:

```text
docs/runtime-fidelity-report-v1.md
schemas/runtime-fidelity-report.schema.json
```

## Role Responsibilities

### Story Author

Define canonical visual data when images are enabled or optional, especially required visible objects, forbidden visual elements, continuity anchors, evidence photo rules, cutaway rules, and text fallbacks.

### Validator

Check that visual definitions and asset manifests align with the package, contain no image-only clues, and do not allow premature hidden mechanism reveals.

### AI Playtester

Test initial scene images, repeated scene images, close-ups, cutaways, gallery recall, text fallback, and image continuity.

### Game Master

Check image mode, player permission, visual definition, required objects, forbidden objects, continuity anchors, and reuse policy before generating or showing images.

### Revision Engine

Repair missing required visual objects, inconsistent geometry, unauthored visual elements, image-only clues, mismatched evidence photos, unsafe cutaways, and overly broad image prompts.
