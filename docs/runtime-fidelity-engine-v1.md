# Runtime Fidelity Engine v1

## Purpose

Runtime Fidelity Engine v1 defines the strict boundary between authored mystery content and runtime narration.

The Game Master executes an authored, validated game package. It is an interpreter, not a co-author.

The player should experience natural conversation, but the mystery itself must remain the mystery that was authored before play began.

## Core Rule

The Game Master may improvise surface narration only.

The Game Master must not invent investigative content during play.

Investigative content includes:

- suspects;
- witnesses;
- evidence;
- clues;
- clue paths;
- locations;
- objects;
- documents;
- solution mechanics;
- timeline events;
- physical access routes;
- motives;
- alibis;
- red herring explanations;
- final proof.

If it affects who did what, why, how, when, where, with what evidence, or how the player can prove it, it must come from the authored package.

## Canonical Package Content

Canonical investigative content lives in the case package, normally:

```text
games/<case-folder>/game-package.json
games/<case-folder>/gm-readme.md
games/<case-folder>/case-board-seed.json
games/<case-folder>/asset-manifest.json
```

If a case handoff identifies another canonical source, the Game Master should follow that source.

Canonical content includes:

- central mystery;
- solution;
- timeline;
- locations;
- characters and NPC knowledge boundaries;
- clues and true meanings;
- evidence and provenance;
- typed discovery rules;
- red herrings and explanations;
- case-board seed;
- asset manifest and text fallbacks.

## Runtime Narration

Runtime narration is the Game Master's conversational presentation of authored content.

Allowed runtime narration includes:

- concise atmospheric description;
- pacing and transitions;
- tone, body language, and ordinary speech style;
- restating already-authored facts in natural language;
- safe negative investigation responses;
- summaries of player-visible discoveries;
- reminders of open authored leads;
- ordinary environmental filler that does not create a lead.

Runtime narration must not create new investigative affordances unless the package already supports them.

## Allowed Improvisation

The Game Master may improvise:

- sensory texture for an authored scene;
- natural phrasing for an authored NPC answer;
- neutral transitions between player actions;
- mundane physical handling of authored objects;
- safe summaries of known player-visible facts;
- non-canonical atmosphere from background characters;
- negative responses to unsupported searches;
- redirects toward existing authored leads.

Allowed improvisation must be reversible and non-decisive. It should not change what can be solved, proved, searched, questioned, accused, or discovered.

## Forbidden Improvisation

The Game Master must not improvise:

- a new suspect;
- a new witness;
- a new clue;
- a new clue interpretation;
- a new piece of evidence;
- a new document;
- a new location or secret room;
- a new access route;
- a new timeline event;
- a new motive or alibi;
- a new contradiction;
- a new hidden object;
- a new forensic result;
- a new confession condition;
- a new final proof;
- a new branch that can alter the solution.

The Game Master must not reward a creative but unsupported player action by adding canon.

## Unauthored NPCs and Witnesses

Unauthored NPCs may exist only as background atmosphere.

They may:

- create crowd texture;
- point the player back to authored NPCs or locations;
- say they do not know;
- provide ordinary logistical help that does not affect the mystery.

They may not:

- become suspects;
- become witnesses;
- provide testimony;
- reveal clues;
- introduce new rumors;
- confirm or deny alibis;
- identify objects;
- supply documents;
- alter the timeline.

If the player tries to interview an unauthored background character, the Game Master should respond naturally and redirect to authored investigative sources.

## Unauthored Evidence, Clues, Objects, Documents, and Locations

If an object, document, location, or evidence item is not authored as investigative content, the Game Master must not promote it into a clue path.

The Game Master may say:

- the object is ordinary;
- the search reveals nothing relevant;
- the document is routine and unrelated;
- the door or area is not part of the investigation;
- nothing there changes the known facts;
- the package-supported leads remain elsewhere.

The response should be natural in-world language when possible. It should not sound like a system limitation unless the player asks out of game or the session is explicitly in test mode.

## Responding to Unauthored Content Requests

When a player asks about unauthored content, the Game Master should:

1. Check whether the request maps to an authored scene, object, NPC, evidence item, clue, document, or discovery rule.
2. If yes, process it through the normal runtime loop.
3. If no, give a natural negative or neutral response.
4. Optionally mark the area or object as inspected or ruled out if runtime state supports it.
5. Redirect to an existing authored lead when useful.

Example patterns:

```text
You check the corridor, but nothing there adds to the case. The useful leads remain inside the chambers.
```

```text
The clerk remembers the general commotion, but not anything that identifies a new witness. The three named staff members are the people with meaningful access.
```

```text
The drawer contains ordinary office supplies. Nothing in it changes the evidence you have so far.
```

Do not add new facts merely to make the response feel rewarding.

## Background Characters

Background characters are scenery, not investigative authorities.

They may help the room feel alive, but they cannot become a route to hidden truth unless the authored package defines them as an NPC, witness, evidence source, or discovery-rule target.

If a background character would logically know something important, that is a package defect for validation or revision. The Game Master should not repair it during play by inventing testimony.

## Authored Content Exhaustion

Authored investigative content may be exhausted when:

- all available discovery rules have fired or are blocked by already-known prerequisites;
- all authored NPC topics have been asked or fairly repeated;
- all authored locations and objects have been inspected at the relevant observation layers;
- all authored evidence has been discovered or ruled out;
- no pending authored leads remain on the current case board;
- further player searches target unsupported content.

The Game Master should not respond to exhaustion by inventing more leads.

Instead, it should transition toward deduction mode.

## Deduction Mode

Deduction mode is the phase where the player has enough player-visible material to form or test a theory.

When authored leads are exhausted, the Game Master should:

- summarize discovered facts;
- distinguish evidence from theory;
- list open questions that can still be answered from discovered facts;
- invite the player to propose a theory;
- ask what suspect, method, motive, and proof the player believes fit;
- offer a non-spoiler hint only if the hint policy allows it;
- evaluate accusations against the authored proof threshold.

Deduction mode should not reveal hidden solution facts unless the player has solved the case, requests a spoiler, or asks to end the case.

## Negative Investigation

Negative investigation is allowed when it closes an unsupported path without creating new canon.

A negative response may:

- confirm nothing relevant is present;
- state that a search finds no sign of tampering;
- mark an area as inspected;
- close a lead;
- redirect to authored leads.

A negative response must not add a new mystery fact, clue, document, witness, or object of interest.

## Post-Play Fidelity Check

After play, runtime fidelity should be checked by comparing the session log, runtime state, current case board, and postgame report against the canonical package.

Check for:

- invented suspects;
- invented witnesses;
- invented evidence or clue paths;
- invented locations, objects, or documents;
- invented solution mechanics;
- changed timeline or motive;
- NPCs revealing knowledge outside their authored boundaries;
- background characters becoming investigative sources;
- case-board entries that treat unauthored theory as fact;
- final reveal facts not present in the package;
- images or descriptions that added canonical details.

Any fidelity breach should be recorded as a Game Master runtime defect. If the package lacked necessary authored content, that should become a Validator or Revision Engine finding rather than an in-play invention.

## Role Responsibilities

### Game Master

Interpret the authored package. Preserve canon. Use negative responses and deduction mode instead of inventing content.

### Validator

Check whether the package gives the Game Master enough authored content to run the case without invention. Flag likely fidelity gaps before play.

### AI Playtester

Stress-test runtime fidelity by asking natural and unusual questions that could tempt the Game Master to invent content.

### Revision Engine

Repair package gaps discovered by validation or playtesting. Do not rely on the Game Master to improvise missing investigative content during play.

## Failure Conditions

Runtime fidelity fails if the Game Master:

- creates a new investigative source;
- creates a new clue path;
- creates new evidence;
- creates a new location or access route;
- lets a background character become a witness;
- changes authored facts to satisfy a player theory;
- extends play after all authored leads are exhausted by inventing leads;
- resolves the case using facts not present in the authored package.
