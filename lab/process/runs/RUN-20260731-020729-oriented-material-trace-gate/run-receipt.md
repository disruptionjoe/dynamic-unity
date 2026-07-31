---
title: "Oriented material-trace and head-tail gate — run receipt"
status: completed
doc_type: governed_run_receipt
created: 2026-07-30
run_id: RUN-20260731-020729-oriented-material-trace-gate
work_id: ORIENTED-MATERIAL-TRACE-HEAD-TAIL-GATE
action_id: ORIENTED-MATERIAL-TRACE-HEAD-TAIL-GATE
program_id: CCR-MINIMAL-PHYSICAL-ANTECEDENT-TO-FINITE-REMAINDER
owner_repo: dynamic-unity
---

# Oriented material-trace and head-tail gate

## Disposition

```text
PHYSICAL_ORIENTATION_INFORMATION_FOUND
+ EXACT_ORIENTATION_ONLY_IN_FROZEN_NOISELESS_REGIME
+ BOUNDED_ERROR_HEAD_TAIL_CERTIFICATE
+ ZERO_ERROR_EVENT_CERTIFICATE_NOT_EARNED
+ TRANSIENT_SIGNAL_NOT_RETAINED_MATERIAL_ARCHIVE
+ KNOWN_SOURCE_AND_CALIBRATION_SEPARATELY_TYPED
+ DETERMINISTIC_READOUT_CANNOT_CREATE_ORIENTATION_INFORMATION
+ STANDARD_DETECTOR_AND_STATISTICS_ABSORPTION
+ RESPONSE_ORDER_GATE_UNMET
+ NO_READY_SUCCESSOR
```

## What was learned

A discrete timestamp or explicit graph edge is not the only possible physical
orientation tag. Stopping and ionization dynamics can make the two ends of a
recoil track physically different. A gaseous TPC can therefore contain real
head-tail information even though its unweighted geometry is only an axis.

The information remains statistical and apparatus-relative. DRIFT validates
mean charge asymmetry with known neutron-source directions. MIMAC
deconvolves a transient induced-current signal to estimate the primary
electron-time profile. Primary-track recovery compares two flipped Bragg
hypotheses under a simulated and calibrated detector model. None of those
operations demotes the physical asymmetry to belief, but none makes every
event a zero-error source certificate.

For equal priors, the exact boundary is:

\[
P_{\rm err}^{\star}
=
\frac{1-\operatorname{TV}(\mu_+,\mu_-)}{2}.
\]

The finite fixture has \(\operatorname{TV}=3/5\) and optimal error \(1/5\).
A noisy readout contracts the total variation to \(3/10\), giving error
\(7/20\). A known source label can repair a joint packet while remaining
side information rather than detector-internal provenance.

## Campaign effect

The material-record ladder now distinguishes:

```text
spatial axis
< reflection-asymmetric physical profile
< bounded-error orientation certificate
< zero-error orientation certificate
< event/path membership
< event time
< source identity.
```

The detector positives remain split:

- nuclear emulsion supplies retained material spatial provenance but weak or
  ambiguous orientation; and
- gaseous TPCs supply stronger orientation information in a transient carrier
  whose durable acquisition is separately specified.

No source joins retained carrier, path association, orientation,
access/archive selection, and an unabsorbed higher-response consequence.
Wave 3 remains ineligible and no successor is selected.

## Grade and boundaries

- scoped Grade 4 for deterministic factorization, stochastic
  certification, and total-variation contraction;
- conditional Grade 3 for bounded-error orientation reconstruction in a
  frozen detector class;
- Grade 2 primary-source detector audit;
- full absorption by standard stopping-power, TPC, directional-reconstruction,
  binary-testing, calibration, and deconvolution theory; and
- no new physics, ontology verdict, paper, provider, or hardware action.

## Durable outputs

- `explorations/gaseous-tpc-oriented-trace-head-tail-information-and-zero-error-boundary-2026-07-30.md`;
- `tests/du_oriented_trace_head_tail_probe.py`;
- `tests/artifacts/du_oriented_trace_head_tail_result.json`;
- additive concept and counter-assumptive entries; and
- `CURRENT-RESEARCH.yaml` revision 135.

## Validation

- `du_oriented_trace_head_tail_probe.py`: **PASS**, `9/9`;
- `du_agent_orientation_contract_probe.py`: **PASS**, `37/37`;
- `du_minimal_antecedent_campaign_probe.py`: **PASS**, all `21` seeds and
  `10` cards retained;
- `du_stage_resource_persistence_separation_probe.py`: **PASS**, `10/10`;
- counter-assumptive register: `336` unique rows, including `NI-DU-223`;
- cold-start surface: `5,837/6,000` words;
- Python compilation: **PASS**; and
- `git diff --check`: **PASS**.
