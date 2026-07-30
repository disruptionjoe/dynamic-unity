---
title: "Sequential-readout complete-record-packet boundary — run plan"
status: completed
doc_type: governed_run_plan
created: 2026-07-30
run_id: RUN-20260730-115843-sequential-readout-complete-packet
work_id: MPA-04-COMPLETE-PHYSICAL-RECORD-PACKET
action_id: MPA-04-COMPLETE-PHYSICAL-RECORD-PACKET
program_id: CCR-MINIMAL-PHYSICAL-ANTECEDENT-TO-FINITE-REMAINDER
authority: "Joe direct chat: Go"
owner_repo: dynamic-unity
---

# Sequential-readout complete-record-packet boundary

## Cold-start contract

- **Purpose:** make physical reality intelligible as one coherent,
  evidence-accountable whole.
- **North Star:** determine which target-blind physical antecedents select
  material, provenance-bearing, observer-indexed record interfaces, then test
  reconstruction and finite remainder.
- **Earned input:** `HC-DU-161` source-pins the coupling-response coordinate
  on the Peronnin sequential superconducting-qubit readout platform. It
  identifies the coupling in a calibrated multi-response packet but does not
  establish one joined formed record.
- **Action:** Joe's `Go` activates only Swing 4,
  `MPA-04-COMPLETE-PHYSICAL-RECORD-PACKET`.

## Frozen platform and source

Use only the apparatus and protocol specified by Peronnin, Marković, Ficheux,
and Huard,
["Sequential dispersive measurement of a superconducting
qubit"](https://arxiv.org/abs/1904.04635), *Physical Review Letters* 124,
180502 (2020), including its supplemental material.

No other experimental platform may fill a missing packet field. Other
literature may serve only as an absorber or definition check.

## Seven-field packet

Treat `SEED-DU-MPA-15` as one conjunction:

1. a physical blank-to-written transition;
2. one run's realized operational outcome;
3. retained material archive through a declared horizon;
4. causal provenance joining preparation, interaction, release, detection,
   and stored result;
5. a declared observer/read-access boundary;
6. reset semantics for both probe and record memory, with an error contract;
7. one held-out future action or response whose law depends on the retained
   record.

`COMPLETE_RECORD_PACKET` requires all seven arrows in one unchanged physical
packet. Otherwise return `PARTIAL_PHYSICAL_TYPING`.

## Frozen source maps

The one-run detector path is:

```text
prepared qubit + coherent readout probe
  -> dispersive interaction
  -> pump-controlled release through the buffer
  -> amplified and digitized voltage trace V(t)
  -> calibrated linear statistic beta = integral V(t)w(t)dt
  -> binary label z from beta in Z_g or its complement
```

The weight \(w\) is constructed from state-labelled average traces. The
decision region

\[
Z_g=\{\beta:P_g(\beta)>P_e(\beta)\}
\]

is constructed from measured state-conditioned distributions. Treat those
choices as supplied calibration unless a source-level naturality or selection
argument says otherwise.

The residual readout population, release efficiency, fidelity, and QND
figures remain typed as separate calibration or validation arms unless the
source explicitly joins them shot by shot.

## Pre-registered returns

```text
RAW_TRACE_FORMATION
CALIBRATION_CONDITIONAL_ONE_RUN_OUTCOME
PARTIAL_PHYSICAL_TYPING
COMPLETE_RECORD_PACKET
PROVENANCE_NONIDENTIFICATION
ARCHIVE_POLICY_NONSELECTION
RESET_LAYER_SPLIT
NO_HELD_OUT_ACTION
KNOWN_RESULT_ABSORPTION
```

## Controls

- **History twin:** positive cross-classification probabilities permit the
  same binary label under distinct prepared histories.
- **Compression twin:** distinct voltage traces differing by a component in
  \(\ker\ell_w\) have the same \(\beta\) and binary label.
- **Archive twin:** one acquisition pipeline retains trial ID, controls, raw
  trace, statistic, and label; another updates the same sufficient aggregate
  and discards raw lineage. They reproduce the declared summary statistics.
- **Erase/rewrite:** test whether the reported interface distinguishes a
  retained original trace from a recomputed or overwritten statistic.
- **Reset:** keep cavity emptying, qubit QND stability, detector readiness,
  and archive-memory erasure as separate maps.
- **Source intervention:** ask whether changing preparation or inserting a
  declared control is joined to each retained attempt rather than merely
  known at ensemble level.
- **Finite access:** track the reported 11% total detection efficiency,
  91% release efficiency, and unmonitored modes without treating absence from
  the detected trace as absence from the process.
- **Held-out action:** repeated-readout correlation or postselection is not
  physical feedback unless the record controls a later operation in the
  source packet.

## Grade, absorber, and stops

- Maximum Grade 4 for an exact complete-packet theorem or an exact
  formation/provenance/access nonselection boundary.
- No Grade 5: no held-out reconstruction target or anomalous physical
  remainder is tested in this swing.
- Strongest absorbers: standard single-shot circuit-QED readout,
  matched-filter/sufficient-statistic theory, quantum instruments,
  measurement-based feedback, classical data acquisition, and database
  provenance.
- Cheapest kill: any one of retention, provenance, access, reset, or
  held-out action is only externally supplied or absent.
- Stop before Swing 5. Do not define the action-relative quotient here.
- No hardware or numerical simulation. Use the primary source and only an
  exact finite counterexample if it fixes a proof boundary.

## Durable output

`explorations/sequential-readout-formed-trace-complete-packet-and-provenance-boundary-2026-07-30.md`
