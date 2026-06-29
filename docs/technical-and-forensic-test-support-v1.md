# Technical and Forensic Test Support v1

## Purpose

This document defines how AI_IF handles player requests for technical, forensic, medical, financial, mechanical, legal, or specialized tests.

Players often ask rational real-world questions. The engine should support those questions without creating uncontrolled external branches or unsafe actions.

## Core Rule

If a case uses specialized mechanisms, the package must define what the player can test, what cannot be tested during play, and how the GM should respond.

The GM must not block a rational test merely because the package forgot to support it. The case should either provide an authored result, an authored limitation, or a safe redirection to available proof.

## Required Test Boundary Fields

For any specialized mechanism, the package should define:

- what the player can inspect now;
- what the player can safely test now;
- what cannot be tested during play;
- why it cannot be tested during play;
- what each available test would prove;
- what each available test would not prove;
- what unsafe actions must be refused;
- what external branches are out of scope;
- how to explain the mechanism in plain language;
- what authored evidence substitutes for unavailable lab or expert results.

## Safe Refusal Rule

If the player requests an unsafe action, the GM must refuse safely and redirect to authored evidence.

Examples of unsafe actions:

- tasting suspected poison;
- touching hazardous residue;
- dismantling dangerous equipment;
- ingesting or applying unknown substances;
- bypassing security systems;
- destroying evidence;
- performing real-world harmful procedures.

The GM should say what can be done safely instead.

## No External Rabbit Hole Rule

The GM must not create new expert witnesses, police labs, off-screen technicians, hospitals, agencies, or forensic branches unless they are authored.

If the case says no police lab branch, the GM may explain that formal testing will follow later, but the playable proof depends on authored clues available now.

## Plain-Language Mechanism Rule

Specialized mechanisms must be explainable in ordinary language.

Avoid requiring the player to know:

- obscure chemistry;
- obscure medicine;
- advanced cybersecurity;
- specialized finance;
- technical law;
- mechanical engineering;
- forensic pathology.

If specialized knowledge is unavoidable, it must be surfaced through an authored clue, document, object, or suspect statement.

## Test Result Discipline

A test result must not become a surprise solution shortcut unless authored.

Test responses should clarify:

- what the test shows;
- what it does not show;
- whether it is conclusive;
- whether it only supports another clue;
- whether more proof is needed.

## Current-Scene Proof Preference

For quick mysteries, prefer playable proof available in the authored scene.

External lab results, future police analysis, court records, hospital reports, and expert testimony should not be required for the solution unless they are explicitly part of the authored package.

## Technical Mystery Constraint

If a case uses technical or cyber-adjacent mechanics, it must define obvious real-world challenges the player may raise.

Examples:

- Can I inspect the device?
- Can I test the cable?
- Can I check logs?
- Can I verify whether files left the room?
- Can I isolate the system?
- Can I call an expert?

The package must provide safe, bounded answers.

## Forensic Mystery Constraint

If a case uses poison, medicine, injury, blood, fingerprints, handwriting, or other forensic elements, it must define:

- what is observable without expert analysis;
- what is not safely inspectable;
- what formal testing would happen later;
- what the player can infer now;
- what cannot be inferred without outside testing;
- what authored proof is sufficient for gameplay.

## Validation Requirements

Validator must check:

- all specialized mechanisms have test boundaries;
- unsafe player actions have safe refusal responses;
- out-of-scope tests have authored explanations;
- the solution does not require an unauthored lab result;
- rational player challenges are anticipated;
- mechanisms are explained plainly;
- the GM is not forced to invent expert results.

## AI Playtest Requirements

AI playtester must test:

- asking for a rational technical or forensic test;
- asking for an unsafe test;
- asking for external expert help;
- asking what a test proves;
- asking what a test cannot prove;
- trying to solve through lab results alone;
- checking that authored proof remains sufficient.
