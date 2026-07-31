---
title: "Nuclear-emulsion material-trace lineage gate — run receipt"
status: completed
doc_type: governed_run_receipt
created: 2026-07-30
run_id: RUN-20260731-014344-nuclear-emulsion-lineage-gate
work_id: NUCLEAR-EMULSION-MATERIAL-PROVENANCE-REOPENER-AUDIT
action_id: NUCLEAR-EMULSION-MATERIAL-PROVENANCE-REOPENER-AUDIT
program_id: CCR-MINIMAL-PHYSICAL-ANTECEDENT-TO-FINITE-REMAINDER
owner_repo: dynamic-unity
---

# Nuclear-emulsion material-trace lineage gate

## Disposition

```text
MATERIAL_SPATIAL_TRACE_FOUND
+ FINITE_LATENT_ARCHIVE_FOUND
+ LOCAL_FORMATION_PROVENANCE_FOUND
+ CAUSAL_LINEAGE_NOT_INTRINSIC
+ UNIQUE_PATH_COVER_CONDITIONAL
+ EVENT_TIME_AND_DIRECTION_UNSELECTED
+ SOURCE_CLASSIFICATION_CONDITIONAL
+ STANDARD_TRACKING_ABSORPTION
+ RESPONSE_ORDER_GATE_UNMET
+ NO_READY_SUCCESSOR
```

## What was learned

Nuclear emulsion is a stronger material provenance carrier than one bubble.
Ionizing histories alter silver-halide grains along spatial traces, and the
latent pattern persists before development or electronic readout.

The material does not generally carry explicit same-source edges, temporal
order, or event timestamps. The audited neutron-emulsion source constructs
tracks by connecting grains under distance and angle tolerances and selecting
a longest chain. It obtains particle energy only after calibration,
kinematics, and an independently known incident direction are supplied.

The exact finite control finds two admissible path covers for the same
four-site material trace. Edge/order tags repair the record; a physically
justified unique path-cover class repairs the completion space. These are
different operations.

## Campaign effect

The wave advances the first HC-DU-178 reopener from:

```text
detector-event formation and retention
```

to:

```text
local material formation plus retained spatial provenance.
```

Global path membership, temporal direction, event identity, source class,
and selected readout remain open. No unabsorbed response-order discriminator
was found, so no later campaign wave or successor activates.

## Grade and boundaries

- scoped Grade 4 lineage/orientation nonselection and exact repair;
- conditional Grade 3 unique-path-cover reconstruction;
- Grade 2 source-pinned detector reconstruction;
- complete absorption by emulsion physics, tracking, data association, and
  source-classification theory;
- no new physics, paper, provider action, external hardware, or detector
  simulation.

## Validation

- `du_material_trace_lineage_probe.py`: PASS, `9/9`;
- `du_agent_orientation_contract_probe.py`: PASS, `37/37`; schema parsed with
  the documented semantic fallback because `jsonschema` is unavailable;
- `du_minimal_antecedent_campaign_probe.py`: PASS, all `21` seeds and `10`
  cards retained;
- `du_stage_resource_persistence_separation_probe.py`: PASS, `10/10`;
- counter-assumptive register: `335` unique rows, including `NI-DU-222`;
- cold-start surface: `5,824/6,000` words after compacting repeated authority
  prose; and
- `git diff --check`: PASS.
