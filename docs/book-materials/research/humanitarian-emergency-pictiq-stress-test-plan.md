# Humanitarian / Emergency Pictiq Stress Test Plan

> Status: future stress-test plan / safety-boundary note
> Source event: Pictiq Research Foundations — Batch 02
> Rule: not a field protocol, medical/legal guide, or accepted humanitarian vocabulary.

## Premise

Pictographic communication can be useful for immediate, concrete, repeatable, low-inference messages: basic needs, locations, simple actions, hazards, queues, routes, and visible status.

It becomes unsafe when a message determines legal rights, clinical decisions, informed consent, safeguarding, family separation, individualized treatment, or official records. In these cases Pictiq may support first contact or orientation, but trained interpreters, qualified professionals, and authoritative records remain required.

## Suitable message properties

A safer humanitarian/emergency candidate message should be:

- concrete;
- immediate;
- low-inference;
- reversible or repairable;
- testable through demonstrated understanding.

## Professional boundary

Use `PROFESSIONAL_ONLY` as an orthogonal safety/authority annotation when a Pictiq sequence may communicate a gist but cannot be authoritative for the task.

This is not a seventh semantic-compression category. It answers a different question: whether the visual representation is allowed to carry authority.

## Candidate corpus strata

| Stratum | Candidate cases | Boundary |
| --- | --- | --- |
| Wayfinding and basic services | water, food, toilet, shelter, information, queue, exit, family point. | Likely useful with local context and staff support. |
| Immediate safety and public health | danger, fire, hot/cold, no entry, wash, mask, wait, call help. | Requires testing under stress and low-literacy conditions. |
| Basic self-report and triage prompts | pain, hungry, thirsty, child, lost, medicine, allergy. | Triage-adjacent only; not diagnosis. |
| Protection, family, and escalation | interpreter, private help, missing family, unsafe person/place. | High risk; must route to qualified humans. |

## Outcome measures

First interpretation, action accuracy, false-action rate, clarification rate, time to comprehension, recall after delay, cultural variance, accessibility performance, confidence calibration, staff interpretability, honest loss classification, and escalation success.
