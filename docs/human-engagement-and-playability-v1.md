# Human Engagement and Playability v1

## Purpose

This specification defines the engine rule that a mystery must be engaging as interactive fiction, not merely logically solvable.

Validation, playtesting, and revision should treat boredom, over-technical presentation, vague motive, and over-steering as real design failures.

## Human Engagement Gate

A mystery should not pass authoring merely because its facts connect. It must give the player a reason to care about what happened.

A draft should include:

- central human conflict;
- emotionally legible stakes;
- concrete culprit motive;
- minimal dependence on jargon;
- at least two plausible pressures among suspects;
- a final reveal that feels like human betrayal, desperation, fear, greed, pride, jealousy, protection, revenge, or shame;
- a reason the player wants to know what happened.

Flag or fail cases where:

- the experience feels like technical procedure;
- the player is pushed through logs, devices, or checklists;
- the mystery depends on abstract business stakes;
- the culprit's motive is vague;
- the player is likely to feel steered rather than clever.

## Motive Mechanism Requirement

The culprit motive must answer:

- What does the culprit want?
- Why now?
- What specific benefit do they expect?
- How does the crime solve their problem?
- What happens if they fail?
- Why did they choose this method?

Generic motives such as "financial pressure," "jealousy," "career trouble," or "revenge" are insufficient unless the package explains the concrete action plan.

## Technical Mystery Constraint

If a mystery uses technical, forensic, medical, mechanical, financial, or specialized mechanisms, the package must define:

- what the player can test;
- what the player cannot test;
- why not;
- what each test proves;
- what each test cannot prove;
- how to explain the mechanism in plain language;
- obvious real-world challenges the player may raise.

The Game Master must not block a rational technical test merely because the package failed to support it.

If a test is out of scope, the package must provide an authored safe response that preserves runtime fidelity without inventing new evidence.

## Anti-Steering Rule

The Game Master must not repeatedly foreground culprit-pointing facts unless the player asks for a hint, recap, theory check, or deduction help.

Neutral recaps must balance:

- facts pointing toward the culprit;
- facts pointing toward red herrings;
- facts clearing innocents;
- open questions.

The Game Master may say a theory is plausible, but must not make the player feel pushed toward a solution.

## Player Agency and Fair Evidence

Player agency depends on letting the player form deductions from stable evidence.

The Game Master should reveal ordinary observable details when the player fairly inspects available evidence, then let the player decide what those details might mean.

The Game Master must not ask leading deductive questions on the player's behalf, convert neutral facts into implied culprit paths, or use case-board summaries to suggest method, motive, opportunity, or proof unless the player requests a hint, theory check, or deduction help.

Neutral support may identify facts as unusual, inconsistent, unexplained, or unresolved. It should not explain the deduction category before the player asks for interpretation.

## Voice Ambiguity Handling

In voice-friendly play, if the player names an unknown NPC, location, or object, the Game Master must not guess when the mapping is uncertain.

Use clarification before answering:

```text
There is no Ellen in the room. Did you mean Lena, Owen, or Priya?
```

Unknown or misheard names should be clarified before the Game Master maps the request to an authored entity.

## Opening Consistency Check

Validator and playtester should check for inconsistent opening-state language:

- event scheduled vs. already happened;
- setup interrupted vs. call aborted;
- victim discovered vs. victim still missing;
- countdown language;
- player-facing facts vs. hidden timeline.

Opening language should make the player-facing state clear without revealing hidden chronology.

## Role Responsibilities

Story Author:

- pass the Human Engagement Gate before presenting a package as ready for validation;
- define concrete motive mechanics;
- author safe responses for likely technical tests.

Validator:

- treat weak engagement, vague motive mechanics, unsupported technical tests, and inconsistent opening state as findings.

AI Playtester:

- test whether play feels clever, human, and fair rather than procedural, steered, or jargon-heavy.

Revision Engine:

- repair dull, over-technical, vague, or over-steered cases before cosmetic polish.

Game Master:

- preserve neutrality, clarify ambiguous voice input, reveal stable observable evidence on fair inspection, and avoid steering except when the player asks for help.

## Human Deception and Emotional Legibility

Suspect deception should arise from human motives, not arbitrary puzzle needs.

Good deception comes from:

- fear;
- shame;
- grief;
- loyalty;
- greed;
- protection;
- embarrassment;
- revenge;
- fear of exposure.

The player should understand why an innocent person lied or behaved suspiciously.
