---
title: "Dual-phase xenon S1/S2 event-pairing gate — run receipt"
status: completed
doc_type: governed_run_receipt
created: 2026-07-30
run_id: RUN-20260731-025212-dual-phase-xenon-s1-s2-pairing-gate
work_id: DUAL-PHASE-XENON-S1-S2-EVENT-PAIRING-GATE
action_id: DUAL-PHASE-XENON-S1-S2-EVENT-PAIRING-GATE
program_id: CCR-MINIMAL-PHYSICAL-ANTECEDENT-TO-FINITE-REMAINDER
owner_repo: dynamic-unity
---

# Dual-phase xenon S1/S2 event-pairing gate

## Disposition

```text
PROMPT_DELAYED_ACQUIRED_PACKET_FOUND
+ S1_PHYSICALLY_ANCHORS_DETECTOR_RELATIVE_EVENT_TIME
+ CORRECTLY_PAIRED_S1_S2_DELAY_RECONSTRUCTS_DEPTH
+ S2_PATTERN_AND_S2_S1_RATIO_ADD_POSITION_AND_STATISTICAL_RESPONSE
+ TRIGGERLESS_STREAM_HAS_NO_PREDETERMINED_EVENT
+ ACCIDENTAL_COINCIDENCE_IS_A_PHYSICAL_PAIRING_REMAINDER
+ UNIQUE_ADMISSIBLE_MATCHING_IS_THE_EXACT_EVENT-PAIRING_GATE
+ EVENT_TAG_REFINEMENT_AND_SINGLE-EVENT_NARROWING_ARE_DISTINCT_REPAIRS
+ LOSSLESS_ACQUISITION_DOES_NOT_CREATE_EVENT_IDENTITY
+ SOURCE_IDENTITY_AND_PATH_POLARITY_NOT_CERTIFIED
+ STANDARD_ABSORPTION
+ RESPONSE_ORDER_GATE_UNMET
+ NO_READY_SUCCESSOR
```

## What was learned

A dual-phase xenon TPC physically joins prompt S1, delayed S2, a
detector-relative timing anchor, conditional three-dimensional
localization, statistical response discrimination, and digital acquisition
in one real architecture. This is a stronger joined material packet than
the previous negative-ion example.

The first leak is the relation between the records. A triggerless acquired
peak stream need not say which S1 and S2 came from the same occurrence.
PandaX-II's accidental-coincidence background is the physical witness:
unrelated isolated S1 and S2 signals can fall inside the same drift window.

The exact finite result is that pairing-dependent targets factor through a
raw packet only when they are constant across every admissible matching.
Unique admissible matching is a sufficient special case. A retained common
event tag repairs by record refinement; a justified single-event or
unique-topology regime repairs by completion narrowing.

## Exact regression

The finite probe passes `10/10`:

- one drift window admits two exact perfect matchings;
- raw peaks fail to factor event pairing and paired depths;
- a common retained event tag repairs both targets;
- a uniquely matchable compatibility graph repairs conditionally;
- correctly paired S1/S2 delay reconstructs depth;
- S2 alone does not reconstruct event time or depth;
- lossless triggerless acquisition does not add pairing truth;
- overlapping S2/S1-style response laws do not yield zero-error class
  certification; and
- a complete detector packet need not identify the upstream source.

## Campaign effect

Dynamic Unity can now point to one real apparatus joining prompt event time,
delayed depth, transverse position, response-class information, and retained
acquisition. The missing duty is sharper: certify common occurrence across
formed record channels rather than merely collecting more coordinates.

Path polarity, source identity, selected archive/access, and the unabsorbed
response-order discriminator remain absent. Wave 3 remains ineligible and no
successor is selected.

## Grade and absorption

- scoped Grade 4 exact matching and factorization boundary;
- conditional Grade 3 correctly-paired depth reconstruction;
- Grade 2 source-pinned detector audit;
- complete absorption by detector response, triggerless DAQ, event building,
  accidental-coincidence analysis, matching, data association, calibration,
  and classification; and
- no new physics, paper, prediction, hardware action, or ontology promotion.

## Durable outputs

- `explorations/dual-phase-xenon-prompt-delayed-event-pairing-and-accidental-coincidence-boundary-2026-07-30.md`;
- `tests/du_dual_phase_s1_s2_pairing_probe.py`;
- `tests/artifacts/du_dual_phase_s1_s2_pairing_result.json`;
- additive concept and counter-assumptive entries; and
- `CURRENT-RESEARCH.yaml` revision 138.

## Validation

- dual-phase S1/S2 pairing probe: **PASS**, `10/10`;
- governance/orientation probe: **PASS**, `37/37`, with `339` unique
  counter-assumptive rows;
- minimal-antecedent campaign retention: **PASS**;
- stage/resource/persistence regression: **PASS**;
- Python compilation: **PASS**; and
- `git diff --check`: **PASS**.
