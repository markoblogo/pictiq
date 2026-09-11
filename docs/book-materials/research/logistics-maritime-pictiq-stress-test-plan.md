# Logistics / Maritime Pictiq Stress Test Plan

> Status: future stress-test plan
> Source event: Pictiq Research Foundations — Batch 02
> Rule: corpus candidates are not accepted Pictiq translations.

## Premise

Maritime, port, warehouse, and logistics communication already relies on layered standardization: controlled maritime English, fixed radio phrases, signal flags, hand signals, hazard placards, packaging marks, safety signage, cargo documents, and operational procedures.

The main lesson is that standardization works especially well for recurring, bounded, high-frequency operational messages.

## Scope boundary

Pictograms are relatively good at:

- classifying visible things;
- showing immediate condition;
- directing immediate action;
- movement/location;
- simple handling constraints.

They are weak at independently establishing:

- exact identity;
- authority;
- legal release;
- measurement basis;
- procedural history;
- customs status;
- dangerous-goods particulars;
- navigation control;
- complex lift engineering.

Pictiq should supplement authoritative systems, not replace them.

## Candidate corpus families

Preserve the supplied logistics cases as a future research corpus. Rebuild every case later using the then-current registry.

| Family | Examples to test | What to discover |
| --- | --- | --- |
| Cargo identity, type, and quantity | container, pallet, fragile, cold chain, weight/volume. | Numeric notation, units, linked data, exact identity gaps. |
| Direction, place, and movement | load, unload, move here/there, warehouse zones, ship/port/gate. | Relation and location pressure. |
| Hazard, weather, and condition | flammable, damaged, wet, hot, unstable, PPE required. | Existing composition vs safety authority boundary. |
| Equipment, PPE, and readiness | forklift, crane, truck, helmet, gloves, ready/blocked. | Context Pack candidates and status vocabulary pressure. |
| Procedural sequencing and handoff | inspect, confirm, hold, release, supervisor, customs. | Professional/system-only cases and workflow-state pressure. |

## Test dimensions

Object resolution, action prediction, role clarity, direction/location, quantity/units, negation/scope, state lifecycle, hazard response, conditional procedure, recognition versus compliance, cultural variance, noise/visibility resilience, machine parse, and escalation behavior.
