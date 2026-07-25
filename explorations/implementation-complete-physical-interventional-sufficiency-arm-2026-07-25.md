---
title: "Implementation-complete physical interventional sufficiency: first public-data gate"
status: completed_incomplete_contract
doc_type: physical_evidence_gate_and_reproducible_ingestion_protocol
created: 2026-07-25
run_id: RUN-20260725-150819-three-paper-advance
claim_grade: "PUBLISHED PHYSICAL PLATFORM AND FIGURE-SOURCE DATA / IMPLEMENTATION-COMPLETE CONTRACT NOT AVAILABLE / NO FACTORIZATION, REMAINDER, OR NEW-PHYSICS VERDICT"
probe: "../tests/du_physical_interventional_sufficiency_probe.py"
artifact: "../tests/artifacts/du_physical_interventional_sufficiency_result.json"
---

# Implementation-Complete Physical Interventional Sufficiency

## Result

The first physical arm for `DU-PAPER-007` reached a useful hard boundary:

> **`INCOMPLETE_CONTRACT`.** The selected source is a real, published
> laboratory characterization of a complete quantum instrument. Its public
> data record is figure-source data, however, not the calibration-linked,
> trial-resolved instrument record required for an uncertainty-aware
> factorization or finite-witness verdict.

This is not a criticism of the experiment. Stricker et al. set out to
characterize a trapped-ion loss-detection instrument, and the article reports
the classical outcomes and postmeasurement dynamics that ordinary
channel-only tomography misses. The result is exactly the right physical
kind for Dynamic Unity.

The narrower issue is evidentiary. The linked Zenodo record describes its
contents as:

> “Source data underlying the graphical representations used in the figures.”

It contains 22 named CSV figure-source files. The record does not expose, as
such, the raw trial table, invalid/discarded trials, calibration linkage and
joint uncertainty, controller/environment provenance, or ordered repeat and
causal-break controls needed by the frozen DU contract. Figure values cannot
legitimately be promoted into those missing fields.

The executable gate passes all checks and returns no sufficiency, remainder,
or new-physics verdict.

## Physical source

- Roman Stricker et al.,
  [“Characterizing Quantum Instruments: From Nondemolition Measurements to
  Quantum Error Correction”](https://doi.org/10.1103/PRXQuantum.3.030318),
  *PRX Quantum* **3**, 030318 (2022).
- Stricker et al.,
  [open figure-source dataset](https://doi.org/10.5281/zenodo.6901982),
  version 1, CC-BY-4.0.

The article supplies a genuine physical premise: a \(^{40}\mathrm{Ca}^{+}\)
trapped-ion loss-detection unit characterized as a quantum instrument with
classical loss/no-loss outputs and outcome-conditioned postmeasurement
dynamics. The paper and dataset remain primary sources. No synthetic model is
described here as laboratory evidence.

## Contract frozen before verdict

### Candidate certified record

The archived classical loss/no-loss outcome, its declared preparation and
intervention labels, and the published outcome-conditioned process estimate.
No hidden run metadata is silently included.

### Observer and access boundary

An external experimenter may:

1. prepare the data ion;
2. invoke the fixed loss-detection unit;
3. read its reported classical outcome;
4. apply an outcome-conditioned single-qubit continuation; and
5. perform tomographically complete output measurements.

The trap environment, controller internals, raw fluorescence stream,
discarded trials, and calibration registers remain outside the boundary
unless the source record explicitly supplies them.

### Admitted interventions

- tomographically complete input preparations;
- one invocation of the fixed instrument;
- outcome-conditioned single-qubit rotations;
- tomographically complete output measurements; and
- a repeat-instrument continuation for a declared memory test.

### Physical refinement class

Only independently formed implementation fields are admitted:

- detector and invalid-trial records;
- preparation and readout calibration blocks;
- controller and pulse-program version;
- implementation route and available environment telemetry;
- trial order, timestamp, and drift block; and
- retained ancilla, leakage, or loss syndromes.

A target-derived behavioral quotient is not an admitted physical refinement.

### Target

All outcome probabilities and outcome-conditioned future responses under the
admitted interventions, with a finite-shot confidence statement.

### Strongest implementation-complete null

Every CPTNI selective instrument—including admitted SPAM, leakage, detector
confusion, drift, temporal memory, invalid-trial selection, and
controller/environment correlations—compatible with the frozen raw record
and independently calibrated uncertainty model.

## Exact evidence audit

| Required field | Public status |
|---|---|
| Physical platform and intended loss-detection instrument | Available in the article |
| Public figure-source files, DOI, license, and file checksums | Available in Zenodo |
| Raw trial-resolved preparation/instrument/output counts | Not exposed by the public record |
| Invalid, abort, herald, and discarded-trial rows | Not exposed |
| Calibration-block linkage and joint uncertainty or bootstrap draws | Not exposed |
| Complete selective-map machine representation with conventions and joint uncertainty | Not established by the dataset description |
| Controller, route, environment, detector, decoder, and resource passport | Not exposed |
| Ordered repeats, causal breaks, and held-out continuations | Not exposed |

The exact missing source package is:

> A calibration-block-linked, trial-resolved instrument-tomography table
> containing preparation, instrument outcome, output tomography
> setting/result, invalid/discard reason, trial order or timestamp, and
> controller/decoder version; plus joint calibration uncertainty or bootstrap
> draws and an explicit mapping from those rows to every selective map.

For the multi-time claim, the packet additionally needs repeat index, prior
outcome, reset or causal-break status, and held-out continuation result.

## What was executed

Two exact information-loss controls show why the gate is substantive.

### Point estimates do not fix finite-shot evidence

The records \(3/4\) and \(300/400\) have the same plotted probability,
\(p=0.75\). Their binomial standard errors differ by a factor of ten. A
figure-level point estimate therefore cannot determine a calibrated shot
gate.

### Marginals do not fix temporal memory

Two 100-trial records can both contain 50 zeros and 50 ones while one
alternates on every trial and the other contains two long blocks. They have
identical marginals but sharply different transition and lag-one statistics.
An aggregate figure therefore cannot certify absence of controller,
environment, or drift memory.

These are constructive nonidentifiability results about the available
evidence packet. They are not claims about what happened in the Innsbruck
experiment.

## What was not executed

Because the likelihood and calibration model are unavailable, this swing did
not:

- reconstruct selective Choi maps from raw counts;
- run uncertainty-aware record factorization;
- search for a minimum physical refinement;
- return a separating physical intervention; or
- calibrate a finite-shot witness.

Doing any of those from the figure CSVs would silently fit missing
experimental structure and violate the frozen comparison contract.

## Reproducible reopening gate

The probe records a machine-readable minimum packet with four linked tables:

1. **Trial table:** trial ID/order, preparation, instrument outcome, output
   setting/result, validity flag, rejection reason, calibration block.
2. **Calibration table:** preparation model, readout confusion matrix, joint
   covariance or bootstrap draws, controller and decoder versions.
3. **Process schema:** selective-map convention, outcome normalization,
   physicality projection, and row-to-map transformation.
4. **Multi-time extension:** repeat index, causal-break/reset flag, and
   held-out conditional continuation.

If this packet becomes available, the next run can freeze uncertainty
regions, reconstruct all selective maps, compare the candidate record against
the implementation-complete null, and return factorization, a minimum formed
refinement, or a finite calibrated separator.

If it is unavailable, the scientifically honest next move is to seek a
different published instrument whose public record passes this gate—not to
replace the missing experiment with another synthetic selector.

## Scientific disposition

- **Physical premise:** published laboratory quantum instrument.
- **Public evidence grade:** figure-source data with article-level method
  description.
- **DU-PAPER-007 advance:** the physical input contract and exact ingestion
  boundary are now executable.
- **North-Star verdict:** none.
- **Paper claim:** none from this arm alone.
- **Reopen condition:** the minimum source packet passes the predeclared
  ingestion gate.
