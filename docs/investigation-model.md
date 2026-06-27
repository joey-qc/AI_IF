# Investigation Model v2

## Purpose

This document defines the investigation model used by Game Master Runtime Engine v2.

The model exists to keep play fair, natural, and consistent. It prevents the Game Master from revealing hidden meanings too early while still allowing the player to observe the world normally.

## Core idea

Every object, room, person, sound, document, and image can be understood through three layers:

```text
Immediate Observation
  -> Investigation
  -> Interpretation
```

The Game Master should not jump directly from immediate observation to interpretation.

## Layer 1: Immediate Observation

Immediate observation is what the player can plainly perceive without special effort.

Examples:

- a fireplace exists;
- a mantle has objects on it;
- a desk stands near the window;
- a tallcase clock is in the room;
- a suspect is nervous;
- a document envelope is visible;
- rain taps against the window.

Immediate observations may appear in opening narration and scene images.

Immediate observation may raise questions, but it should not reveal forensic meaning.

## Layer 2: Investigation

Investigation is what the player learns by interacting with or closely examining something.

Examples:

- inspecting the mantle;
- opening a drawer;
- checking dust patterns;
- comparing fabric;
- asking a suspect about a statement;
- reading a visible document;
- listening closely to a clock;
- smelling an oily residue.

Investigation can reveal clues if discovery conditions are met.

Investigation may also produce negative findings.

## Layer 3: Interpretation

Interpretation is what the evidence means.

Examples:

- the scratch suggests recent movement;
- the oil matches the clock mechanism;
- the handwriting matches a prior note;
- the suspect's answer contradicts the timeline;
- the envelope is a red herring;
- the hidden object explains a mechanical disturbance.

Interpretation usually requires at least one of these:

- multiple clues;
- comparison;
- player theory;
- NPC contradiction;
- final accusation;
- explicit request for analysis.

## Application to images

Images must follow the same layers.

A scene image may show immediate observation details, such as a mantle with objects on it.

It should not show close forensic details unless those are already earned.

An inspection image may show close detail after the player inspects that object or area.

An evidence image may show a recovered or exposed object after discovery.

Images should not reveal interpretation. Interpretation belongs in text, deduction, or final reveal.

## Visible does not mean solved

A visible object can be shown without revealing its importance.

For example, an opening scene may show a mantle with decorative objects. If the mantle has no relevant clue, inspecting it should safely rule it out. If the mantle has a clue, the clue should be revealed only through investigation.

Visibility is not the same as clue discovery.

## Negative investigation

Negative investigation is a valid result.

When the player investigates an object or area with no direct clue, the Game Master should:

- say what is observed;
- avoid inventing new facts;
- explain what the inspection rules out when appropriate;
- mark the object as inspected in runtime state if useful.

Example:

```text
You inspect the mantle. The objects appear decorative and undisturbed. Nothing there explains the missing watch, but the inspection rules out the mantle as an obvious hiding place.
```

Negative findings help players feel systematic rather than stuck.

## Object state

Objects may move through investigation states:

```text
unseen
visible
mentioned
inspected
closely_inspected
evidence_recovered
ruled_out
revisited
```

Not every object needs every state. Quick Mysteries may use a lightweight state model.

## Discovery condition mapping

The Story Author and Validator should ensure each clue has a clear discovery condition.

The Game Master should map player actions to these conditions.

Examples:

```text
Player: I look around the room.
Layer: Immediate Observation.
Reveal: visible objects only.

Player: I inspect the display case.
Layer: Investigation.
Reveal: case-level clues if conditions are satisfied.

Player: Does the oil match anything?
Layer: Interpretation through comparison.
Reveal: matching relationship if the relevant source has been observed.
```

## Progressive reveal pattern

When possible, reveal clues progressively.

Example:

```text
Initial: The display case is locked.
Inspection: The rear panel is loose.
Close inspection: A trace is present.
Comparison: The trace matches a suspect or object.
Interpretation: This supports a method or accusation.
```

This makes deduction feel earned.

## NPC investigation

NPC answers also follow the three layers.

Immediate observation:

- posture;
- tone;
- visible nerves;
- where they are standing.

Investigation:

- direct questions;
- contradictions;
- alibi details;
- explanations of visible behavior.

Interpretation:

- lie detection;
- motive inference;
- timeline conflict;
- connection to physical evidence.

The Game Master must not make NPCs reveal interpretation unless earned.

## Case board integration

The case board should track:

- visible but uninspected objects;
- inspected objects;
- recovered evidence;
- ruled-out areas;
- interpreted clues;
- unresolved observations.

This prevents the player from repeatedly inspecting the same irrelevant areas without feedback.

## Validator implications

The Validator should check that:

- every essential clue has a fair discovery path;
- important visible objects are not omitted from scene descriptions;
- images cannot reveal hidden clues prematurely;
- negative investigations do not block progress;
- interpretation requires sufficient supporting clues.

## Game Master implications

The Game Master should respond to player actions by determining the requested layer.

If the player asks a broad observation question, answer at Layer 1.

If the player inspects an object, answer at Layer 2.

If the player asks what something means, answer at Layer 3 only if enough evidence has been discovered. Otherwise, provide a fair partial answer and suggest how to investigate further.
