# Classic Whodunit Pattern v1

## Purpose

This document defines AI_IF support for classic contained whodunit mysteries, including murder mysteries in the Agatha Christie and Sherlock Holmes tradition.

A whodunit is a human-centered fair-play mystery. The player should solve through motive, method, opportunity, alibi, contradiction, and physical or testimonial clues.

## Supported Structure

A classic whodunit package should define:

- victim or target;
- culprit;
- motive;
- method;
- opportunity;
- means;
- alibi claims;
- alibi truths;
- suspect relationships;
- required clues;
- supporting clues;
- red herrings;
- innocent suspect clearances;
- final proof chain;
- final reconstruction;
- fallback solution reveal.

## Contained Mystery Principle

A whodunit works best when tightly scoped:

- limited location count;
- limited suspect count;
- no surprise outsider;
- no late-added witness;
- no external clue required for the solution;
- no hidden information that cannot be discovered through authored play.

One-room and single-location designs are strongly supported.

## Human Motive Requirement

The culprit's motive must be concrete and emotionally legible.

Acceptable motive types include:

- inheritance;
- shame;
- revenge;
- fear of exposure;
- jealousy;
- protection of another person;
- greed;
- loss of status;
- blackmail;
- betrayal;
- desperation.

A motive is not sufficient if it is merely abstract.

Weak:

> Julian had financial pressure.

Strong:

> Eleanor was about to sign a document removing Julian from estate control and exposing withdrawals he had forged.

## Method Requirement

The method must be understandable from discovered clues.

Avoid methods that depend on:

- obscure chemistry;
- obscure medical knowledge;
- hidden forensic results;
- unexplained technology;
- surprise legal technicalities;
- supernatural or impossible mechanics unless the genre explicitly supports them.

If specialized knowledge is necessary, the package must explain it plainly and provide fair player-facing discovery paths.

## Opportunity Requirement

The package must define:

- who had access;
- who lacked access;
- when the method could happen;
- what sequence matters;
- which alibi claims are true, false, mistaken, or incomplete.

Opportunity should be testable through room layout, witness statements, object placement, timing, or documents.

## Alibi Structure

Each suspect should have:

- alibi claim;
- alibi truth;
- suspicious behavior;
- pressure or motive;
- clearance or implication path.

A whodunit should not depend only on motive. Motive without method or opportunity is not enough.

## Red Herring Structure

Each red herring should have:

- why it looks suspicious;
- why it is false;
- what clue clears it;
- whether the suspect lied for an innocent reason;
- how the final reveal explains it.

## Cause of Death / Harm Boundary

Murder mysteries are allowed, but:

- no gore;
- no graphic death description;
- no prolonged suffering for shock value;
- no obscure autopsy dependency;
- no solution by lab result alone;
- no unsafe player action such as tasting suspected poison.

The playable proof should come from authored clues, not from external forensic branches.

## Final Reconstruction

The final reveal should reconstruct:

1. what happened;
2. why it happened;
3. when the decisive act occurred;
4. how the culprit attempted concealment;
5. what mistake or contradiction exposed them;
6. why the innocent suspects are not responsible.

## Validation Requirements

Validator must check:

- motive is concrete;
- method is understandable;
- opportunity is testable;
- each innocent suspect can be cleared;
- red herrings are bounded;
- final proof chain does not rely on hidden forensic knowledge;
- final reconstruction explains both guilt and innocence;
- the case remains contained within the authored scope.

## AI Playtest Requirements

AI playtester must test:

- motive-only accusation;
- opportunity-only accusation;
- wrong suspect accusation;
- correct suspect with missing method;
- correct suspect with missing physical proof;
- full proof accusation;
- red herring resolution.
