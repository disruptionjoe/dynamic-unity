---
title: "Time-resolved TPC acquired packet, clock-depth rank, and event-building boundary"
status: banked_scoped_result
doc_type: exploration
created: 2026-07-30
claim_id: HC-DU-182
run_id: RUN-20260731-023936-time-resolved-tpc-record-packet-gate
work_id: TIME-RESOLVED-TPC-RECORD-PACKET-GATE
action_id: TIME-RESOLVED-TPC-RECORD-PACKET-GATE
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

# Time-resolved TPC acquired packet, clock-depth rank, and event-building boundary

## Executive return

```text
JOINED_ACQUIRED_DETECTOR_PACKET_FOUND
+ ONE_CARRIER_CLOCK_DEPTH_NONIDENTIFIABILITY
+ DISTINCT_TWO_CARRIER_ABSOLUTE_DEPTH_REPAIR
+ CONDITIONAL_CLOCK_DEPTH_RANK_THEOREM
+ EVENT_BUILDING_REMAINS_A_SEPARATE_PHYSICAL_OR_INFERENTIAL_INTERFACE
+ MINORITY_PEAK_EFFICIENCY_PREVENTS_UNIVERSAL_COMPLETE_PACKET
+ HEAD_TAIL_NOT_JOINED_IN_THE_SOURCE-PINNED_ARCHITECTURE
+ SOURCE_IDENTITY_NOT_CERTIFIED
+ NO_CROSS-PLATFORM_STITCHING
+ STANDARD_TPC_DAQ_EVENT-BUILDING_AND_INVERSE-PROBLEM_ABSORPTION
+ RESPONSE_ORDER_GATE_UNMET
+ NO_READY_SUCCESSOR
```

`HC-DU-178--180` found detector formation, retained spatial traces, and
physical head-tail information in different systems. This wave asks whether
one real apparatus—not a composite assembled from convenient papers—already
joins enough of those duties to count as a complete acquired record packet.

The strongest source-pinned candidate is Higashino et al.'s negative-ion
micro-TPC:

- a recoil creates ionization in one prepared gas volume;
- strip readout supplies transverse coordinates;
- self-triggered electronics acquire waveforms;
- majority and minority negative-ion species reach the readout at different
  speeds;
- the arrival-time difference supplies absolute drift depth; and
- calibrated energy, track length, and reconstructed three-dimensional
  positions are retained for analysis.

This is materially stronger than a transient orientation signal or a
time-insensitive emulsion trace. It joins formation, three-dimensional
localization, acquisition, and an electronic packet in one detector.

It is not yet the complete Dynamic Unity packet. The published minority peak
was detected with overall efficiency \(70\pm5\%\) in the admitted nuclear
recoil sample. Event selection, peak association, calibration, trigger
semantics, and track reconstruction remain specified interfaces. The paper
does not also establish per-event head-tail sense or exact source identity.
Adjacent Timepix3 and MIMAC results show that richer per-hit packets and
physical polarity are individually realizable, but combining their duties
with the negative-ion result would be an unbuilt detector proposal, not
evidence about one existing architecture.

The exact new boundary is a rank statement. For one carrier,

\[
t_{\rm arr}=t_0+\frac{z}{v},
\tag{1}
\]

so event time \(t_0\) and drift depth \(z\) are not separately identifiable.
For two correctly associated carriers with distinct calibrated velocities,

\[
\begin{pmatrix}t_1\\t_2\end{pmatrix}
=
\begin{pmatrix}
1 & 1/v_1\\
1 & 1/v_2
\end{pmatrix}
\begin{pmatrix}t_0\\z\end{pmatrix},
\tag{2}
\]

whose determinant is \(1/v_2-1/v_1\). Distinct velocities give an exact
conditional reconstruction. Equal velocities, a missing minority peak, or
ambiguous peak association restore the one-carrier ambiguity.

That theorem explains the negative-ion absolute-\(z\) repair. It does not
make the electronics clock an observer-independent physical time. The
experiment directly earns absolute depth inside a calibrated detector
contract. Recovering an event-time coordinate as well additionally requires
a declared common clock, timestamp origin, latency model, and peak
association.

## 1. Frozen question

> Does one existing source-pinned detector physically join retained spatial
> provenance, timing, polarity or charge, event association, and accessible
> acquisition strongly enough to close Dynamic Unity's material-record
> packet; and if not, what is the first exact leak?

The wave forbids a common but subtle form of overbuilding:

```text
Timepix3 hit packet
+ MIMAC head-tail response
+ negative-ion absolute z
!= one demonstrated physical instrument.
```

Each source is audited on its own apparatus. Adjacent platforms may identify
a realizable duty, but duties are not credited as joined until one physical
architecture joins them.

## 2. The source-pinned negative-ion micro-TPC

Higashino et al.,
[“First reconstruction of absolute three-dimensional position of nuclear
recoils using a negative ion \(\mu\)-TPC for dark matter search
experiments”](https://arxiv.org/abs/2302.10725),
describe an SF\(_6\) negative-ion micro-TPC with a micro-pixel chamber,
dedicated readout electronics, and a self-triggering back end.

Ionization electrons attach predominantly to SF\(_6^-\), with a minority
SF\(_5^-\) population. The two carrier species drift at different speeds and
therefore produce two separated pulses from one admitted recoil. The paper
uses

\[
z=
\frac{v_5v_6}{v_5-v_6}\Delta t
\tag{3}
\]

to reconstruct absolute drift depth from the inter-peak delay. It reports
three-dimensional nuclear-recoil position reconstruction throughout the
drift volume and an overall SF\(_5^-\)-peak detection efficiency of
\(70\pm5\%\).

The physically joined packet is therefore at least:

\[
q_{\rm NI\mu TPC}
=
(\text{strip hits},\text{waveforms},t_5,t_6,
  \text{charge/energy},\text{trigger context},\text{calibration context}).
\tag{4}
\]

This packet is not a cognitive metaphor. It is a physical acquisition
produced by gas transport, amplification, electronics, and retained data.
But every field in (4) has a scope:

| Duty | Source-pinned status |
|---|---|
| local material formation | physically realized by ionization and carrier formation |
| transverse position | acquired by the micro-pixel/strip readout |
| drift depth | reconstructed when two carrier peaks are detected and associated |
| event time | not directly established as an observer-independent or global time |
| event membership | defined by trigger, waveform, selections, and reconstruction contract |
| track sense | not demonstrated as a joined per-event head-tail certificate |
| source identity | classified statistically under source/background models |
| archive/access | electronics and analysis retain data, while retention policy and access boundary remain engineered |

The detector selects a concrete instrument because it was physically built.
The fundamental particle law does not uniquely select that instrument,
trigger, threshold, gas mixture, or analysis contract.

## 3. Exact clock-depth rank boundary

### 3.1 One carrier

With one measured arrival coordinate and known velocity \(v\), the map

\[
(t_0,z)\longmapsto t_0+z/v
\tag{5}
\]

has a one-dimensional kernel. For example, with \(v=2\),

\[
(t_0,z)=(0,6)
\quad\text{and}\quad
(1,4)
\tag{6}
\]

both give \(t_{\rm arr}=3\). A lossless archive of that timestamp does not
repair the ambiguity.

This corrects an overreading of ordinary TPC language. Multiplying drift
time by a calibrated velocity gives a depth only when the time origin is
known or otherwise eliminated. A time-of-arrival field is not by itself
both event time and depth.

### 3.2 Two carriers

For two velocities \(v_1\ne v_2\), the measurement matrix in (2) has full
rank. Equivalently,

\[
z
=
\frac{t_1-t_2}{1/v_1-1/v_2},
\qquad
t_0=t_1-\frac{z}{v_1}.
\tag{7}
\]

Equation (3) is the depth part of this repair. It removes the unknown event
time by differencing the two peaks. If the apparatus also retains the two
arrival times in one declared clock, (7) conditionally reconstructs the
clock-relative event-time coordinate.

The result has four explicit antecedents:

1. both peaks came from the same physical occurrence;
2. the carrier species are correctly identified;
3. their velocities are distinct and calibrated for the admitted gas,
   field, pressure, and temperature; and
4. the arrival times share one controlled clock and latency model.

The rank theorem is exact. Whether its antecedents hold for a realized event
is an empirical certification question.

## 4. Event membership is not a timestamp

A hit packet can contain \((x,y,t,q)\) for every acquired hit while failing
to determine which hits arose from the same occurrence. A finite control
uses one raw four-hit packet compatible with either:

```text
one occurrence containing four hits
```

or:

```text
two occurrences containing two hits each.
```

The raw acquired values are identical; the event partition differs.
Therefore event membership does not factor through the raw packet.

A physically retained trigger/event tag can repair the fixture. A justified
single-event operating regime can instead narrow the completion class.
Those are different moves. Applying a deterministic clustering algorithm to
the same ambiguous packet produces one partition, but cannot prove that the
partition is the occurrence truth in both compatible histories.

This is not a criticism of event building. Timepix3 work makes the boundary
especially visible:

- Roberts et al.,
  [“First demonstration of 3D optical readout of a TPC using a single photon
  sensitive Timepix3 based camera”](https://arxiv.org/abs/1810.09955),
  report per-hit packets containing pixel \(x,y\), time of arrival, and time
  over threshold; they obtain \(z\) through calibrated drift velocity and
  cluster hits by declared spatial and temporal proximity.
- Meduna et al.,
  [“Real-time Timepix3 data clustering, visualization and classification
  with a new Clusterer framework”](https://arxiv.org/abs/1910.13356),
  report simultaneous ToA/ToT, data-driven readout, online acquisition,
  clustering, filtering, and data saving. They explicitly reconstruct
  clusters from a stream of pixel packets by an algorithm.

These sources establish that a rich acquired and retained packet is a real
physical-engineering object. They also show why “hit,” “cluster,” and
“occurrence” must remain separately typed.

## 5. Why adjacent detector positives cannot be stitched

The MIMAC result audited in `HC-DU-180` demonstrates that stopping and
ionization response can carry head-tail information. But that result uses a
different gas, amplification/readout path, deconvolution, source geometry,
and reconstruction contract. The negative-ion \(\mu\)-TPC paper establishes
absolute three-dimensional position, not the same per-event head-tail
certificate.

The honest cross-platform conclusion is:

```text
rich retained hit packet: physically realizable;
absolute self-triggered depth: physically realizable;
head-tail information: physically realizable;
all duties joined in one source-pinned complete packet: not yet shown.
```

This is a construction target, not a factual contradiction. It also remains
insufficient by itself for the causal-response campaign: even a detector
joining all three duties would still need an invariant, unabsorbed
higher-response distinction with a finite held-out consequence.

## 6. Updated material-record ladder

The detector ladder is now:

```text
formed local material change
< retained spatial marks
< acquired per-hit (position, arrival, intensity) packet
< calibrated 3D localization
< two-carrier absolute-depth certificate
< physically certified event membership
< bounded- or zero-error path polarity
< retained source provenance
< selected observer access/finality quotient.
```

These are not stages every detector must implement. They are separately
typed duties that prevent one positive coordinate from silently standing for
the whole packet.

## 7. Absorbers, novelty, and grade

The source results and the exact rank boundary are absorbed by:

- time-projection-chamber transport and readout;
- multi-species negative-ion drift;
- linear inverse problems and observability rank;
- triggering, data acquisition, data association, and event building;
- detector calibration, timewalk correction, diffusion, efficiency, and
  selection effects; and
- binary classification and source inference.

The Dynamic Unity contribution at current grade is the typed composition:

> A physical acquisition may join several record coordinates without
> selecting event identity, causal polarity, source provenance, or access;
> and a second propagation speed repairs a specific clock-depth fibre only
> under a same-event, calibrated-clock contract.

Grades:

- **Grade 4:** exact finite factorization, rank, event-partition, and
  lossless-archive boundaries;
- **conditional Grade 3:** two-carrier time/depth reconstruction within the
  frozen calibrated common-clock class;
- **Grade 2:** primary-source detector audit;
- **not earned:** a novel detector theorem, new physics, universal record
  ontology, source certificate, empirical remainder, or paper seed.

## 8. Campaign consequence

One meaningful gap has closed: Dynamic Unity no longer needs to speak as if
physical acquisition, retained digital data, three-dimensional localization,
and an absolute-depth repair are only hypothetical. A real negative-ion
micro-TPC joins them.

The first exact leaks are now better located:

1. minority-carrier detection/association does not hold on every event;
2. event membership is trigger- and model-relative unless physically tagged
   or guaranteed by a frozen regime;
3. track sense is not joined in the source-pinned architecture;
4. source identity remains statistical; and
5. the response-order discriminator required to reopen Wave 3 is absent.

No successor is ready. Reopen only for one source-pinned architecture that
both closes at least one of these remaining duties and exposes an invariant,
unabsorbed response-order question with a finite held-out consequence.

## 9. Exact regression

Run:

```bash
python3 tests/du_time_resolved_tpc_record_packet_probe.py --write-artifact
```

The artifact is
`tests/artifacts/du_time_resolved_tpc_record_packet_result.json`.

Passing establishes:

- one-carrier clock-depth nonidentifiability;
- full-rank reconstruction for two distinct calibrated velocities;
- failure of duplicate carrier speed to repair the fibre;
- raw-hit/event-partition nonfactorization;
- repair by a retained event tag;
- inability of deterministic clustering to create missing provenance;
- inability of lossless storage to recreate an absent minority peak; and
- failure of even a rich packet to identify a source in general.

It does not simulate detector physics or promote a scientific successor.
