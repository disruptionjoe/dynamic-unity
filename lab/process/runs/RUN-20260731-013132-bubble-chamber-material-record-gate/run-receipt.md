---
title: "Bubble-chamber material-record reopener audit — run receipt"
status: completed
doc_type: governed_run_receipt
created: 2026-07-30
run_id: RUN-20260731-013132-bubble-chamber-material-record-gate
work_id: BUBBLE-CHAMBER-MATERIAL-RECORD-REOPENER-AUDIT
action_id: BUBBLE-CHAMBER-MATERIAL-RECORD-REOPENER-AUDIT
program_id: CCR-MINIMAL-PHYSICAL-ANTECEDENT-TO-FINITE-REMAINDER
owner_repo: dynamic-unity
---

# Bubble-chamber material-record reopener audit

## Disposition

```text
MATERIAL_FORMATION_AND_FINITE_RETENTION_FOUND
+ PHYSICALLY_SELECTED_SOURCE_RESPONSE_CONTRACT
+ DETECTOR_EVENT_RECORD_NOT_UPSTREAM_SOURCE_CERTIFICATE
+ ACCESS_AND_DIGITAL_ARCHIVE_SUPPLIED
+ STANDARD_DETECTOR_PHYSICS_ABSORPTION
+ RESPONSE_ORDER_GATE_UNMET
+ NO_READY_SUCCESSOR
```

## What was learned

A PICO-style bubble chamber provides the strongest material record in the
bounded detector comparison. Localized deposited energy can turn a
superheated metastable liquid into a growing bubble. The bubble remains a
material distinction until hydraulic recompression resets the chamber. Its
existence does not depend on the camera being the carrier that preserves it.

The retained bubble factors the detector target “nucleation occurred.” It does
not factor every upstream source target. Detection efficiency is not one, and
alpha, recoil, wall, and interface histories can overlap in optical or acoustic
record space. Camera and acoustic channels improve source classification but
add their own calibration, trigger, retention, and access contracts.

The correct result is:

> physical record of a detector event, probabilistic evidence about its
> upstream cause.

## Campaign effect

The candidate clears the first half of the reopener more strongly than the
prior abstract metastability survey:

- source-pinned apparatus;
- formed one-run material occurrence;
- finite material retention;
- physical reset; and
- nontrivial source-response law.

It does not expose an invariant, unabsorbed response-order question with a
finite held-out consequence. No later causal-response wave activates, and no
successor is selected.

## Grade and boundaries

- scoped Grade 4 target-factorization and stochastic-support boundary;
- Grade 2 primary-source detector reconstruction;
- full absorption by standard detector and nucleation science;
- no new physics, ontology verdict, paper, local simulation, provider action,
  or hardware run.

## Validation

- `du_agent_orientation_contract_probe.py`: PASS, `37/37`; schema parsed with
  the documented semantic fallback because `jsonschema` is unavailable;
- `du_minimal_antecedent_campaign_probe.py`: PASS, all `21` seeds and `10`
  cards retained;
- `du_stage_resource_persistence_separation_probe.py`: PASS, `10/10`;
- counter-assumptive register: `334` unique rows, including `NI-DU-221`;
- cold-start surface: `5,823/6,000` words; and
- `git diff --check`: PASS.
