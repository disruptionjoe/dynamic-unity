---
title: "Time-resolved TPC record-packet gate — run receipt"
status: completed
doc_type: governed_run_receipt
created: 2026-07-30
run_id: RUN-20260731-023936-time-resolved-tpc-record-packet-gate
work_id: TIME-RESOLVED-TPC-RECORD-PACKET-GATE
action_id: TIME-RESOLVED-TPC-RECORD-PACKET-GATE
program_id: CCR-MINIMAL-PHYSICAL-ANTECEDENT-TO-FINITE-REMAINDER
owner_repo: dynamic-unity
---

# Time-resolved TPC record-packet gate

## Disposition

```text
JOINED_ACQUIRED_DETECTOR_PACKET_FOUND
+ ONE_CARRIER_CLOCK_DEPTH_NONIDENTIFIABILITY
+ DISTINCT_TWO_CARRIER_ABSOLUTE_DEPTH_REPAIR
+ CONDITIONAL_CLOCK_DEPTH_RANK_THEOREM
+ EVENT_BUILDING_REMAINS_SEPARATELY_TYPED
+ MINORITY_PEAK_EFFICIENCY_PREVENTS_UNIVERSAL_COMPLETE_PACKET
+ HEAD_TAIL_NOT_JOINED_IN_THE_SOURCE-PINNED_ARCHITECTURE
+ SOURCE_IDENTITY_NOT_CERTIFIED
+ NO_CROSS-PLATFORM_STITCHING
+ STANDARD_ABSORPTION
+ RESPONSE_ORDER_GATE_UNMET
+ NO_READY_SUCCESSOR
```

## What was learned

One real negative-ion micro-TPC joins material formation, self-triggered
electronic acquisition, transverse coordinates, waveforms, charge/energy,
and absolute drift-depth reconstruction. This closes the false possibility
that these record duties exist only as a conceptual composite.

The repair is exact and typed. One carrier measures only
\(t_0+z/v\). Two correctly associated carriers with distinct calibrated
velocities give a full-rank system and reconstruct \(z\); with a declared
common clock they also conditionally reconstruct the clock-relative \(t_0\).
The source directly earns absolute depth, not a universal time observable.

The complete packet still fails. The reported minority peak is detected with
overall efficiency \(70\pm5\%\) in the admitted recoil sample. Trigger,
selection, peak association, event building, calibration, and archive/access
remain engineered interfaces. The source-pinned architecture does not also
demonstrate per-event head-tail sense or exact source identity.

Timepix3 and MIMAC show that richer hit packets and physical polarity are
separately realizable. They are adjacent platforms, not components of the
audited negative-ion detector. No cross-platform stitching is credited.

## Exact regression

The finite probe passes `10/10`:

- one-carrier event-time and depth targets both fail to factor;
- distinct carrier velocities give nonzero determinant and exact
  time/depth recovery;
- duplicate velocity fails to repair rank;
- raw hits fail to factor event membership;
- a retained event tag repairs the finite partition;
- deterministic clustering does not create occurrence provenance;
- a lossless archive cannot repair a missing minority peak; and
- the joined acquisition packet need not factor source identity.

## Campaign effect

The material-record ladder now contains a real joined acquisition and
absolute-depth stage. The first leaks are minority-peak availability and
association, event membership, track polarity, source provenance, selected
archive/access, and the absent unabsorbed response-order discriminator.

Wave 3 remains ineligible and no successor is selected.

## Grade and absorption

- scoped Grade 4 exact rank, fibre, and event-partition boundary;
- conditional Grade 3 common-clock two-carrier reconstruction;
- Grade 2 primary-source detector audit;
- complete absorption by TPC transport, negative-ion drift, inverse
  problems, DAQ, event building, calibration, and classification; and
- no new physics, paper, prediction, hardware action, or ontology promotion.

## Durable outputs

- `explorations/time-resolved-tpc-acquired-packet-clock-depth-rank-and-event-building-boundary-2026-07-30.md`;
- `tests/du_time_resolved_tpc_record_packet_probe.py`;
- `tests/artifacts/du_time_resolved_tpc_record_packet_result.json`;
- additive concept and counter-assumptive entries; and
- `CURRENT-RESEARCH.yaml` revision 137.

## Validation

- time-resolved TPC packet probe: **PASS**, `10/10`;
- governance/orientation probe: **PASS**, `37/37`, with `338` unique
  counter-assumptive rows and `5,960/6,000` cold-start words;
- minimal-antecedent campaign retention: **PASS**, all `21` seeds and `10`
  cards retained;
- stage/resource/persistence regression: **PASS**, `10/10`;
- Python compilation: **PASS**; and
- `git diff --check`: **PASS**.
