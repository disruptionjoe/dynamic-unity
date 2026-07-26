---
title: "Public physical evidence four-table screen"
date: 2026-07-25
status: completed_bounded_screen
doc_type: exploration
claim_grade: "PUBLIC-EVIDENCE ROUTING AUDIT / NO PHYSICAL SUFFICIENCY OR NEW-PHYSICS VERDICT"
candidate_ids:
  - HC-DU-036C
paper_id: DU-PAPER-007
lanes:
  - lane_3
  - lane_7
channels:
  - CH-EMPIRICAL
  - CH-COLLIDE
probe_ref: tests/du_public_physical_evidence_screen_probe.py
artifact_ref: tests/artifacts/du_public_physical_evidence_screen_result.json
---

# Public physical evidence four-table screen

## Verdict

`NO_INGESTIBLE_PUBLIC_PACKET_FOUND`.

A bounded screen of four strong experimental/process-tensor candidates found
one materially better reopening route, but none passes Dynamic Unity's full
four-table ingestion contract.

The best candidate is Xiang et al.,
[Learning and forecasting open quantum dynamics with correlated noise](https://www.nature.com/articles/s42005-025-01944-2)
(2025), with its public
[data and reconstruction repository](https://github.com/guochu/pt_recovery).
Unlike the previously screened figure-source packet, it provides experimental
randomized-benchmarking data, explicit train/test partitions, reconstructed
process tensors, and reconstruction code. The public preprocessing code,
however, reduces each experimental item to:

```text
Clifford-operation sequence + aggregate p0
```

That is enough to learn and test a predictive open-quantum-evolution model.
It is not yet enough to run the Dynamic Unity sufficiency contract, because
the inspected schema does not carry per-shot outcomes, invalid/rejected
trials, calibration-block joins, controller/decoder versions, complete
selective instrument outcomes, or explicit reset/causal-break rows.

The correct next physical verdict is therefore not factorization or
remainder. It remains `INCOMPLETE_CONTRACT`, now with a much narrower missing-
data diagnosis.

The deterministic screen passes `9/9` checks. Its artifact SHA-256 is
`93fc5b766242d93a1f69d854e4b26b5f5e525f53f8048bddb82bd6e5b516da65`.

## Frozen ingestion rule

A public candidate is ingestible only if all four tables are explicit:

| table | minimum fields |
|---|---|
| trial | trial/order, preparation, intermediate instrument outcome, output setting/result, validity or rejection, calibration block |
| calibration | preparation model, readout-confusion model, joint uncertainty object, controller and decoder version |
| process schema | selective-map convention, normalization, physicality projection, raw-row-to-map rule |
| multitime | repeat index, reset or causal break, held-out continuation |

`PARTIAL`, `UNVERIFIED`, and `UNAVAILABLE` are not treated as passes. A paper's
method section cannot substitute for its public rows. A reconstructed tensor
cannot manufacture missing shot or provenance fields. An aggregate probability
cannot be expanded into fictional trials.

## Screen results

| candidate | trial | calibration | process schema | multitime | routing verdict |
|---|---|---|---|---|---|
| Xiang et al. 2025 OQE/RB | partial | unverified | partial | partial | **strongest public reopener; not ingestible** |
| White et al. 2022 process-tensor tomography | unverified | unverified | method-level pass | partial | method reference; no ingestible packet located |
| White et al. 2020 restricted process tensor | unavailable | unavailable | partial | partial | author request required; not public |
| Stricker et al. 2022 trapped-ion instrument | fail | fail | partial | fail | figure-source packet; not ingestible |

This is an evidence-readiness screen, not a ranking of the papers' scientific
quality.

## Candidate receipts

### Xiang et al. 2025 — promising partial

The [paper](https://www.nature.com/articles/s42005-025-01944-2) explicitly
links the GitHub repository as the experimental-data and code source. It uses
randomized benchmarking on coupled superconducting system/environment qubits,
learns an open quantum evolution model, reconstructs process tensors, and
tests predictions on held-out and longer future sequences.

The inspected public sources were:

- repository `README.md`, blob
  `08acfaae30ca332a60f5b6fdc1b1cb1262482546`;
- `split_rb_data.jl`, blob
  `63875ce93997ce23fc7dc334e8754df2d994c5c3`; and
- `two_qubit_model_rb_unitary.jl`, blob
  `dd40e6b7e1ac4e1291578684afaa85de5f523f5a`.

The splitter reads each original item as `cl_ops` and `p0`, groups by sequence
length, shuffles within length, and writes flattened training and testing
pairs. The reconstruction consumes those pairs. This establishes genuinely
public multitime predictive data, but also establishes the precise loss of
record granularity: the learner sees an aggregate terminal probability, not
the full trial and intermediate record history required here.

**Cheap reopening check:** inspect only for a public sidecar joining the
aggregate rows to shot outcomes, calibration epochs, reset events, and
controller versions. If no such sidecar exists, stop. Do not reverse-engineer
those fields from \(p_0\).

### White et al. 2022 — method reference, not current data premise

[Non-Markovian Quantum Process Tomography](https://arxiv.org/abs/2106.11722)
provides the most relevant method-level template: informationally complete
multi-time characterization, maximum-likelihood reconstruction, and positive
causal projection, with IBM-device validation.

The bounded screen did not locate a linked row-level experimental,
calibration, and reset packet. The paper remains valuable for specifying the
process table, likelihood, physicality constraints, and uncertainty workflow.
It does not presently supply the other three public tables needed for a DU
verdict.

### White et al. 2020 — good experiment, nonpublic packet

[Demonstration of non-Markovian process characterisation and control on a quantum processor](https://www.nature.com/articles/s41467-020-20113-3)
reconstructs four-time restricted process tensors and validates predictions
outside the reconstruction basis. The experiment is directly relevant.

Two stops are explicit in the primary paper:

1. available controls span a restricted unitary subspace rather than the full
   space of trace-nonincreasing CP maps; and
2. data and code are available from the corresponding author on reasonable
   request, not through a public packet.

Contacting an author is an external action and was not taken.

### Stricker et al. 2022 — prior failure retained

The [published trapped-ion instrument](https://doi.org/10.1103/PRXQuantum.3.030318)
is physically relevant, but its linked
[Zenodo record](https://doi.org/10.5281/zenodo.6901982) contains figure-source
data rather than the four linked tables. This candidate remains a useful
instrument and calibration design reference, not an ingestible premise.

## What the screen actually teaches

The bottleneck is no longer “find any real quantum instrument” or “find any
process-tensor code.” Those exist.

The bottleneck is a mismatch between two evidence products:

- current public process-characterization packets often preserve enough
  aggregate data to reconstruct or predict dynamics; while
- Dynamic Unity's North-Star test needs the formation, access, provenance,
  selective outcomes, invalid trials, calibrations, resets, and held-out
  continuations to remain joined.

That mismatch is scientifically relevant. It means the flagship cannot be
closed by attaching a record interpretation after a conventional tomography
pipeline has already discarded the record lineage. The assay likely needs
either:

1. a still-unlocated public sidecar with those joins; or
2. a deliberately co-designed experiment whose acquisition schema preserves
   them from the beginning.

This does not show that conventional process tensors are physically
insufficient. It shows that the inspected **public evidence packets** are
insufficient to test the stronger record-sufficiency claim.

## Next physical action

Perform one bounded sidecar audit of the Xiang repository and supplementary
data for:

```text
shot or count rows
readout/preparation calibration epoch
invalid/discard reason
reset or causal-break marker
controller/decoder version
row-to-selective-map convention
```

If the join is absent, close the public-reuse route without further model
fitting and write the minimal prospective acquisition schema for a new
experiment. Do not run the new reconstruction trichotomy against aggregates.
