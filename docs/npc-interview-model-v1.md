# NPC Interview Model v1

## Purpose

NPC Interview Model v1 defines how AI_IF game packages describe what each NPC knows, withholds, lies about, evades, reveals, and can be contradicted on during gameplay.

The interview model is canonical authoring data inside:

```text
games/<case-folder>/game-package.json
```

The machine-readable structure is defined in:

```text
schemas/game-package.schema.json
```

Runtime asked-topic state is tracked in:

```text
games/<case-folder>/runtime-state.json
```

## Core rule

NPCs are not omniscient.

An NPC may answer only from:

- what they personally know;
- what they saw or heard;
- what they believe;
- what they are willing to say;
- what they are trying to hide;
- what the package defines for the topic being asked.

The Game Master may improvise tone and phrasing, but not new canonical facts.

## Interview topics

Important NPCs should define structured interview topics.

Interviewable NPCs must be authored. Background characters cannot become interview topics unless they are promoted into the canonical package before play.

Each topic may include:

```text
topicId
topicLabel
topicType
npcId
playerQuestionExamples
truthfulAnswer
lieOrOmission
evasiveAnswer
knowledgeBoundary
emotionalState
revealsClueIds
revealsEvidenceIds
prerequisiteClueIds
prerequisiteEvidenceIds
contradictionIds
followUpTopicIds
repeatAnswer
validationNotes
```

Use only the fields that apply. The goal is consistency, not bureaucracy.

## Knowledge boundaries

`knowledgeBoundary` explains what the NPC cannot know or should not reveal.

Examples of boundaries:

- the NPC was not present for the event;
- the NPC knows only a rumor;
- the NPC saw an object but not its meaning;
- the NPC knows the truth but will omit it until contradicted;
- the NPC can identify a contradiction only after the player has discovered another clue.

The Game Master should use this field to avoid accidental omniscience.

## Truth, lies, omissions, evasion, and ignorance

`truthfulAnswer` is what the NPC says when answering honestly.

`lieOrOmission` is a deliberate falsehood, half-truth, or withheld fact.

`evasiveAnswer` is a safe response when the NPC avoids the topic without providing the hidden answer.

Ignorance means the NPC genuinely does not know. The Game Master should say so or answer from limited perception.

A lie or omission should be discoverable through clues, contradictions, follow-up questions, or comparison with evidence.

## Relationship to discovery rules

NPC interview topics connect to typed discovery rules through `question_npc`.

A `question_npc` rule should reference the relevant:

```text
npcId
topicId
revealsClueIds
revealsEvidenceIds
prerequisiteClueIds
prerequisiteEvidenceIds
updatesCaseBoardSections
```

The interview topic defines the NPC's answer model. The discovery rule defines when that answer reveals clue or evidence IDs.

Topic expansion must stay within the package's canonical topic inventory when `canonicalAssetInventory.interviewTopicIds` is present.

NPC portraits and other character images must preserve the authored NPC's identity and appearance across generated or recalled images. They must not introduce unauthored NPC identity details or make background characters appear investigative.

## Revealing clues and evidence

An interview topic may reveal clues or evidence when:

- the topic is asked;
- prerequisites are satisfied;
- the NPC has reason to answer;
- the package permits the information to become player-visible.

Do not reveal hidden solution facts simply because the player asks a broad question.

If prerequisites are missing, use `evasiveAnswer`, a limited truthful answer, or a safe prompt toward further investigation.

## Contradictions

`contradictionIds` identify contradictions that may become player-visible when an NPC answer conflicts with:

- physical evidence;
- another NPC statement;
- a discovered timeline note;
- an object state;
- the NPC's prior answer.

Contradictions should have fair discovery paths. A contradiction should not require the player to guess the exact wording of a question.

## Follow-up topics

`followUpTopicIds` identify topics unlocked by an answer.

Follow-ups may become available after:

- a clue is discovered;
- an NPC lies or evades;
- a contradiction is noticed;
- the player compares evidence;
- the player makes a theory.

Follow-ups should help the Game Master keep questioning natural without inventing new branches.

## Repeat answers

Use `repeatAnswer` when the player asks the same topic again.

The repeat answer should:

- preserve prior facts;
- avoid revealing the same clue as new;
- remind the player of the relevant answer;
- stay consistent with any lie or omission already established.

Runtime state should track asked topics so repeats can be handled cleanly.

## Emotional state and motive pressure

`emotionalState` describes how the NPC behaves around the topic.

It may include fear, anger, guilt, grief, pride, confusion, protectiveness, or irritation.

Emotional state should affect tone, hesitation, and evasiveness. It should not let the Game Master invent hidden facts.

Motive pressure may affect whether an NPC lies, omits, or answers defensively.

## Game Master responsibilities

The Game Master should:

1. Map the player's natural-language question to the closest valid topic.
2. Check the NPC's knowledge boundary.
3. Check prerequisites and discovery rules.
4. Answer with truthful, lying, evasive, or ignorant behavior as defined.
5. Reveal only eligible clues or evidence.
6. Use repeat answers for already-asked topics.
7. Surface contradictions only when the player has enough visible support.
8. Record asked topics in runtime state.
9. Update `case-board-current.json` only with player-visible results.

The Game Master must not make NPCs omniscient or overhelpful.

## Validator responsibilities

The Validator should check that:

- important NPCs have enough interview topics for expected questioning;
- NPCs do not know facts they should not know;
- answers are consistent with the timeline and motive;
- lies and omissions are marked;
- lies and omissions can be discovered fairly;
- contradictions have fair discovery paths;
- `question_npc` discovery rules reference valid `npcId` and `topicId` values;
- every interview topic belongs to an authored NPC;
- background characters are not treated as interviewable sources;
- topic IDs stay within the canonical inventory when present;
- solution-critical NPC disclosures are not hidden behind unreasonable phrasing;
- repeat answers remain consistent.

## Story Author responsibilities

The Story Author should define:

- interview topics for important NPCs;
- knowledge boundaries;
- truthful answers;
- lies or omissions;
- evasive answers;
- clue and evidence reveals;
- contradictions;
- follow-up topics;
- repeat answers.

The Story Author should not leave important NPC behavior for the Game Master to invent during play.

## Examples

### Alibi topic

```json
{
  "topicId": "topic-alibi",
  "topicLabel": "Alibi during the bell",
  "topicType": "alibi",
  "npcId": "npc-clerk",
  "playerQuestionExamples": ["Where were you when the bell rang?", "Did anyone see you then?"],
  "truthfulAnswer": "The clerk says he was in the hall and heard the bell from there.",
  "knowledgeBoundary": "The clerk did not see inside the study.",
  "emotionalState": "nervous but cooperative",
  "revealsClueIds": ["clue-bell-heard-from-hall"],
  "followUpTopicIds": ["topic-delivery-time"],
  "repeatAnswer": "He repeats that he was in the hall when the bell rang.",
  "validationNotes": "Supports timeline without revealing the culprit."
}
```

### Lie or omission topic

```json
{
  "topicId": "topic-delivery-time",
  "topicLabel": "Delivery time",
  "topicType": "timeline",
  "npcId": "npc-clerk",
  "playerQuestionExamples": ["When did the parcel arrive?", "Was the parcel there before the bell?"],
  "truthfulAnswer": "The parcel arrived before the bell.",
  "lieOrOmission": "At first, the clerk avoids saying the parcel arrived early.",
  "evasiveAnswer": "He says only that the parcel was already being handled that evening.",
  "prerequisiteClueIds": ["clue-parcel-label"],
  "contradictionIds": ["contradiction-parcel-before-bell"],
  "repeatAnswer": "He sticks to the corrected timing: the parcel arrived before the bell.",
  "validationNotes": "Contradiction is available only after the parcel label is found."
}
```

## Suspect Lies and Omissions

NPC interview design must distinguish:

- truthful answer;
- lie or omission;
- evasive answer;
- alibi claim;
- alibi truth;
- knowledge boundary;
- evidence that challenges the statement;
- response when confronted.

A suspect may lie in-character. The GM must not invent unauthored lies or change the truth at runtime.

## Confrontation Behavior

When confronted with contradictory evidence, an NPC should respond according to authored guidance:

- admit a minor truth;
- double down;
- explain innocent deception;
- reveal shameful but non-culprit motive;
- become evasive;
- refuse to answer;
- confess only if final proof threshold allows it.
