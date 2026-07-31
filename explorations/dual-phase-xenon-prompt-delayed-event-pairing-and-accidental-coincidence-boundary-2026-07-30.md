---
title: "Dual-phase xenon prompt-delayed event pairing and accidental-coincidence boundary"
status: banked_scoped_result
doc_type: exploration
created: 2026-07-30
claim_id: HC-DU-183
run_id: RUN-20260731-025212-dual-phase-xenon-s1-s2-pairing-gate
work_id: DUAL-PHASE-XENON-S1-S2-EVENT-PAIRING-GATE
action_id: DUAL-PHASE-XENON-S1-S2-EVENT-PAIRING-GATE
program_id: CCR-MINIMAL-PHYSICAL-ANTECEDENT-TO-FINITE-REMAINDER
owner_repo: dynamic-unity
primary_lane: lane_3
supporting_lanes:
  - lane_1
  - lane_4
  - lane_7
channels:
  - CH-EMPIRICAL
  - CH-FORMAL
  - CH-MODEL
  - CH-COLLIDE
evidence_grade: 4
maximum_grade: 4
---

# Dual-phase xenon prompt-delayed event pairing and accidental-coincidence boundary

## Executive return

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
+ STANDARD_DETECTOR_DAQ_DATA-ASSOCIATION_ABSORPTION
+ RESPONSE_ORDER_GATE_UNMET
+ NO_READY_SUCCESSOR
```

`HC-DU-182` found a source-pinned acquired TPC packet whose two carrier
speeds can remove clock-depth ambiguity, but only when two minority/majority
peaks are available and already associated with one occurrence. This swing
tests a distinct architecture that physically forms a prompt timing channel
and a delayed position channel in the same medium.

A dual-phase liquid-xenon TPC really does join more of the material-record
ladder in one apparatus:

- an interaction produces prompt scintillation, S1;
- the same interaction produces ionization electrons;
- the electrons drift and generate delayed proportional scintillation, S2;
- the S1--S2 delay gives depth once the two signals are correctly paired;
- the S2 pattern gives transverse position;
- S2/S1 and scatter multiplicity provide statistical response
  discrimination; and
- triggerless acquisition can retain the underlying above-threshold signal
  stream.

This closes a real gap. Prompt event time, delayed depth, transverse
position, response class, and digital acquisition need not be stitched
across different detector platforms.

It does not close event identity. XENONnT's DAQ retains signals without a
global hardware trigger and software later reconstructs events. PandaX-II
reports accidental coincidences of unrelated isolated S1 and S2 signals
inside the admissible drift window as a real detector background. A
time-compatible pair is therefore not automatically a physically certified
common occurrence.

The exact boundary is graph-theoretic:

> A raw S1/S2 packet determines event pairing exactly only when all
> physically admissible matchings give the same pairing-dependent target.
> Unique admissible matching is a sufficient special case.

The smallest counterexample has two S1 peaks at times \(0,1\), two S2 peaks
at \(3,4\), and an allowed delay interval \([2,4]\). Both perfect matchings
are admissible:

\[
(0\mapsto3,\ 1\mapsto4)
\quad\text{and}\quad
(0\mapsto4,\ 1\mapsto3).
\]

The acquired peaks are identical, but the event partitions and reconstructed
depths differ. Lossless acquisition preserves the ambiguity exactly.

## 1. Frozen question

> Does one source-pinned dual-phase detector physically join event time,
> depth, transverse position, response class, and retained acquisition; and
> does that joined packet certify which prompt and delayed signals belong to
> the same occurrence?

The target is detector-event membership, not a metaphysical global event.
The analysis keeps four objects distinct:

1. physical S1 and S2 formation;
2. retained peak acquisition;
3. inferred or certified S1/S2 pairing; and
4. upstream particle/source identity.

## 2. What the detector physically selects

The XENON Collaboration's
[XENON1T detector paper](https://link.springer.com/article/10.1140/epjc/s10052-017-5326-3)
describes the dual-phase chain directly. Prompt S1 scintillation is detected
in the liquid; ionization electrons drift to the gas and produce delayed S2.
The top-PMT S2 pattern supplies lateral position, and the S1--S2 time
difference supplies depth. S2/S1 and the number of S2 signals support
background rejection and scatter-multiplicity reconstruction.

The physical packet can be typed as

\[
q_{\rm LXe}
=
(\{S1_i\},\{S2_j\},\text{PMT patterns},\text{areas},
  \text{waveforms},\text{clock},\text{calibration context}).
\]

This is stronger than an S2-only TPC timestamp. S1 supplies the prompt
detector-relative origin, so a correctly associated pair gives

\[
z=v_d(t_{S2}-t_{S1}),
\]

with calibrated electron drift velocity \(v_d\). The source earns a
detector-relative event time and depth coordinate for the admitted
interaction class. It does not earn observer-independent global time.

The
[XENON1T DAQ paper](https://arxiv.org/abs/1906.00819)
also makes clear that acquisition and event identification are separate:
the detector signals are digitized and stored, while the global trigger is
deferred to software and event identification is performed later.

XENONnT sharpens the distinction. Its
[triggerless DAQ paper](https://arxiv.org/abs/2212.11032)
states that the system reads and stores every signal above digitization
thresholds and uses software to process the acquired data. Its
[signal-reconstruction and event-selection paper](https://arxiv.org/abs/2409.08778)
then documents the separately implemented reconstruction, calibration, and
event-selection layer.

The detector dynamics selects S1/S2 formation. The electronics and
threshold contract select which signals are acquired. Neither fact alone
selects a unique event partition of a multi-peak stream.

## 3. Exact pairing theorem

Let \(A=\{a_i\}\) be acquired S1 peaks and \(B=\{b_j\}\) acquired S2 peaks.
Let \(G_q\subseteq A\times B\) be the compatibility graph defined by the
frozen physical contract: drift-time limits, detector region, quality
constraints, and any other target-blind admissibility conditions. Let
\(\mathcal M(q)\) be its set of admissible matchings.

For a pairing-dependent target \(T(M)\), an exact decoder from the raw packet
exists if and only if

\[
M,M'\in\mathcal M(q)
\quad\Longrightarrow\quad
T(M)=T(M').
\tag{1}
\]

This is the ordinary fibre criterion applied to event building. If the
matching itself is the target, (1) becomes uniqueness of the admissible
matching. If only reconstructed depth is the target, multiple matchings are
allowed only when they accidentally induce the same depth result.

### 3.1 Smallest ambiguous fixture

With

\[
A=(0,1),\qquad B=(3,4),\qquad
2\le b-a\le4,
\]

the compatibility graph is complete bipartite. It has two perfect
matchings. For drift velocity \(v_d=2\), the direct matching gives depths
\((6,6)\), while the cross matching gives \((8,4)\). Same peaks; different
pairing and depths.

This is not a claim about the frequency of ambiguity in XENONnT. It proves
that a drift window by itself is not a physical event certificate.

### 3.2 Repairs

There are three typed repairs:

- **Record refinement:** a physical tag common to the S1 and S2 channels is
  retained with both signals.
- **Completion narrowing:** a justified low-rate, topology, veto, or
  single-scatter regime leaves one admissible matching.
- **Inference:** an event builder ranks or selects a matching under a
  calibrated stochastic model.

Only the first two can make the finite target exact. The third is often the
right experimental method, but its error model must remain visible.

## 4. Accidental coincidence is the real physical witness

The PandaX-II Collaboration's
[accidental-coincidence study](https://csnsdoc.ihep.ac.cn/article/doi/10.1088/1674-1137/ac7cd8)
states the physical issue directly: a good event uses one correlated S1/S2
pair within the maximum drift-time window, while unrelated isolated S1 and
S2 signals inside that window create accidental-coincidence background.

This source matters more than the finite fixture. It shows the pairing
remainder is not manufactured by Dynamic Unity's formalism. The apparatus
really can acquire prompt and delayed signals whose temporal compatibility
does not imply common causal lineage.

The correct conclusion is not that event building is arbitrary. Detector
geometry, pulse shape, S2 position, vetoes, multiplicity, and response models
can make a pairing highly reliable. The conclusion is that reliability,
exact event identity, and raw acquisition are different objects.

## 5. What each channel earns

| Channel | Earned | Not earned |
|---|---|---|
| S1 | prompt detector-relative timestamp and scintillation response | depth, source identity, global time |
| S2 | delayed charge response, transverse pattern, multiplicity | absolute depth without paired S1 |
| S1--S2 pair | conditional depth and joint light/charge response | common occurrence unless pairing is certified or uniquely admissible |
| S2/S1 | statistical ER/NR discrimination | zero-error source or particle certificate |
| triggerless archive | retained above-threshold signal stream | predetermined event partition |
| event builder | calibrated pairing estimate | physical provenance by algorithm alone |

This architecture therefore closes more duties than the negative-ion packet,
but reveals a sharper first leak: the prompt and delayed channels may both be
physical records while their common-event relation is not itself recorded.

## 6. Absorbers, novelty, and grade

The detector facts and matching result are absorbed by:

- dual-phase xenon detector physics;
- TPC drift and position reconstruction;
- triggerless DAQ and software event building;
- accidental-coincidence estimation;
- bipartite matching, unique matchability, and data association;
- detector calibration and statistical classification; and
- inverse problems and sufficient-statistic theory.

The Dynamic Unity contribution at current grade is the typed physical
composition:

> Two channels may each be real formed and acquired records while the
> relation asserting that they came from the same event remains a separate
> physical or inferential record duty.

Grades:

- **Grade 4:** exact finite event-pairing/depth factorization boundary;
- **conditional Grade 3:** depth reconstruction in a correctly paired,
  calibrated dual-phase event class;
- **Grade 2:** source-pinned detector and accidental-coincidence audit;
- **not earned:** a novel detector theorem, new physics, source certificate,
  response-order discriminator, paper seed, or scientific successor.

## 7. Campaign consequence

The material-record ladder now has a stronger single-platform positive:

```text
physical prompt S1 formation
+ physical delayed S2 formation
+ detector-relative event-time anchor
+ conditional 3D localization
+ response-class information
+ retained triggerless acquisition.
```

The next missing duty is no longer merely “get a prompt clock.” It is:

> Physically certify the common-occurrence relation across prompt and
> delayed record channels, or state the exact event class and error under
> which the relation is inferred.

This refines the North-Star search, but it does not reopen Wave 3. Source
identity, path polarity, selected archive/access semantics, and the
unabsorbed higher-response discriminator remain absent.

## 8. Exact regression

Run:

```bash
python3 tests/du_dual_phase_s1_s2_pairing_probe.py --write-artifact
```

The artifact is
`tests/artifacts/du_dual_phase_s1_s2_pairing_result.json`.

Passing establishes:

- one drift window can admit two exact S1/S2 matchings;
- raw triggerless peaks fail to factor pairing and paired depth;
- a retained common event tag repairs the fixture;
- a uniquely matchable completion class conditionally repairs it;
- correctly paired S1/S2 delay reconstructs depth;
- S2 alone does not reconstruct event time and depth;
- lossless acquisition does not create event identity;
- overlapping response laws are not zero-error event-class certificates; and
- a rich detector packet need not factor upstream source identity.

It does not simulate xenon response or promote a scientific successor.
