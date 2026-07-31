---
title: "DRIFT joined depth/head-tail gate — run receipt"
status: completed
doc_type: governed_run_receipt
created: 2026-07-30
run_id: RUN-20260731-031215-drift-joined-depth-head-tail-gate
work_id: DRIFT-JOINED-DEPTH-HEAD-TAIL-GATE
action_id: DRIFT-JOINED-DEPTH-HEAD-TAIL-GATE
program_id: CCR-MINIMAL-PHYSICAL-ANTECEDENT-TO-FINITE-REMAINDER
owner_repo: dynamic-unity
---

# DRIFT joined depth/head-tail gate

## Disposition

```text
SINGLE-CONFIGURATION_DEPTH_AND_HEAD-TAIL_PACKET_FOUND
+ NO_CROSS-PLATFORM_STITCHING_REQUIRED
+ MULTI-CARRIER_ABSOLUTE_Z_AND_HEAD-TAIL_RESPONSE_JOINED
+ PHYSICAL_PATH-POLARITY_INFORMATION_JOINED
+ ENSEMBLE_DIRECTIONAL_SENSITIVITY_ESTABLISHED
+ ENSEMBLE_ASYMMETRY_DOES_NOT_IMPLY PER-EVENT CERTIFICATION
+ KNOWN_NEUTRON-SOURCE_GEOMETRY_IS IMPORTED SIDE INFORMATION
+ LOW-Z_PEAK-OVERLAP_AND HIGH-Z_TRIGGER/DIFFUSION_RESTRICT THE EVENT CLASS
+ RECOIL_SPECIES_AND UPSTREAM_SOURCE_NOT CERTIFIED
+ STANDARD_ABSORPTION
+ RESPONSE-ORDER_GATE_UNMET
+ NO_READY_SUCCESSOR
```

## What was learned

The prior non-stitching assessment was too narrow. One real DRIFT-IId
configuration joins oxygen-induced minority-carrier absolute depth,
triggered waveform acquisition, and a physical ionization-asymmetry
head-tail response. No cross-platform composite is needed for those duties.

The positive is ensemble-scoped. Known neutron-source positions label
opposite and transverse runs, and the mean asymmetry reverses as expected.
That establishes physical path-polarity information. It does not provide a
zero-error head-tail label for every individual unknown event.

The exact finite result gives opposite mean asymmetries with total variation
\(1/4\) and minimum equal-prior one-event error \(3/8\). Four independent
events reduce the ensemble error to \(81/512\) without changing the
one-event certificate. Disjoint event laws are the exact zero-error positive
control.

## Campaign effect

The search for a single packet joining depth and physical polarity
information is closed positively on a restricted event class. The next
detector duty is to obtain orientation-conditioned event laws and declare
per-event error or support separation in the same source-pinned
configuration.

Low-\(z\) carrier overlap, high-\(z\)/low-energy diffusion and trigger
effects, source geometry, recoil-species ambiguity, and reported systematic
differences remain visible. Source identity, selected access, and the
response-order discriminator remain absent. No successor is selected.

## Grade and absorption

- scoped Grade 4 exact ensemble/event-certification boundary;
- conditional Grade 3 joined depth/head-tail reconstruction;
- Grade 2 primary-source detector audit;
- complete absorption by negative-ion/directional TPC physics, detector
  calibration, binary testing, total variation, efficiency, and systematic
  analysis; and
- no new physics, paper, prediction, hardware action, or ontology promotion.

## Exact regression

The finite probe passes `10/10`:

- one packet joins two carrier times and an orientation statistic;
- distinct carrier velocities retain full depth rank;
- a missing minority peak restores depth ambiguity;
- ensemble means reverse;
- event laws overlap with nonzero optimal error;
- replication strengthens ensemble detection only;
- disjoint laws give the zero-error control;
- a known source tag repairs an ambiguous statistic by side information;
- the joined packet need not factor recoil species; and
- a trigger does not force event orientation.

## Durable outputs

- `explorations/drift-iid-joined-absolute-depth-head-tail-packet-and-event-certification-boundary-2026-07-30.md`;
- `tests/du_drift_joined_depth_head_tail_probe.py`;
- `tests/artifacts/du_drift_joined_depth_head_tail_result.json`;
- additive concept and counter-assumptive entries; and
- `CURRENT-RESEARCH.yaml` revision 139.

## Validation

- joined depth/head-tail probe: **PASS**, `10/10`;
- governance/orientation probe: **PASS**, `37/37`, with `340` unique
  counter-assumptive rows;
- minimal-antecedent campaign retention: **PASS**;
- stage/resource/persistence regression: **PASS**;
- Python compilation: **PASS**; and
- `git diff --check`: **PASS**.
