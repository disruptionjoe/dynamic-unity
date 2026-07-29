---
title: "Reciprocal-crosslink self-calibration, distance and clock gauge, and asymmetric delay"
date: 2026-07-29
status: banked_scoped_result
claim_id: HC-DU-108
work_id: CCR-RECIPROCAL-CROSSLINK-SELF-CALIBRATION-GATE
run_id: RUN-20260729-072609-reciprocal-crosslink-self-calibration-gate
lanes:
  - lane_1
  - lane_3
  - lane_4
  - lane_5
  - lane_6
  - lane_7
channels:
  - CH-FORMAL
  - CH-COLLIDE
  - CH-SYN
  - CH-MODEL
maximum_grade: "Conditional Grade 3 self-calibrated event reconstruction up to declared gauge plus scoped Grade 4 reciprocity, latency, and scale necessity boundaries; no Grade-5 physical remainder or prediction"
---

# Reciprocal-crosslink self-calibration, distance and clock gauge, and asymmetric delay

## Executive result

The swing returned:

```text
RECIPROCAL_BIDIRECTIONAL_TIMESTAMPS_RECOVER_RANGE_AND_OFFSET_DIFFERENCE
+ AFFINELY_INDEPENDENT_COMPLETE_K4_RECOVERS_CONSTELLATION_UP_TO_EUCLIDEAN_ISOMETRY
+ CONNECTED_CROSSLINKS_RECOVER_CLOCK_OFFSETS_UP_TO_COMMON_SHIFT
+ HC_DU_107_COMPOSES_TO_SELF_CALIBRATED_EVENT_LOCALIZATION_UP_TO_GAUGE
+ AUTONOMOUS_POSITIONING_AND_CLOCK_RIGIDITY_ABSORB_THE_MATHEMATICS
+ UNKNOWN_ASYMMETRIC_DELAY_CONFUNDS_CLOCK_OFFSET
+ UNKNOWN_HARDWARE_LATENCY_CONFUNDS_RANGE_AND_OFFSET
+ UNKNOWN_COMMON_CLOCK_RATE_CONFUNDS_SPATIAL_SCALE
+ AUTHENTICATION_CERTIFIES_ORIGIN_NOT_TIMESTAMP_TRUTH_OR_DELAY
+ SELF_CALIBRATION_DOES_NOT_SELECT_A_FOLIATION
+ SOURCE_FORMATION_ASSOCIATION_AND_REGIONAL_TRANSFER_REMAIN_OPEN
+ NO_READY_SUCCESSOR
```

`HC-DU-107`'s numerical detector positions and relative clock offsets need
not be supplied from outside. In a stationary flat-spacetime control, the
detectors can reconstruct them from their own reciprocal crosslink records.

Let four honest nodes at affinely independent sites \(s_i\in\mathbb R^3\)
have clocks

\[
C_i(t)=t+b_i
\]

and reciprocal unit-speed propagation

\[
d_{ij}=d_{ji}=\|s_i-s_j\|.
\]

When a timestamped message travels from \(i\) to \(j\), the retained
pseudorange is

\[
p_{ij}=d_{ij}+b_j-b_i.
\tag{1}
\]

The two directions immediately give

\[
d_{ij}=\frac{p_{ij}+p_{ji}}2,
\qquad
b_j-b_i=\frac{p_{ij}-p_{ji}}2.
\tag{2}
\]

The six pairwise distances reconstruct the tetrahedral constellation up to a
Euclidean isometry. The clock differences reconstruct all four offsets up to
one common time-origin shift. Once those natural gauges are fixed,
`HC-DU-107` localizes the held-out event. The common clock-origin ambiguity
simply shifts the event's time coordinate by the opposite amount.

This is a real constructive improvement:

```text
reciprocal crosslink transcript
  -> relative detector geometry + relative clock calibration

self-calibrated detector scaffold
  + four event-arrival readings
  -> event localization up to spatial-isometry and time-origin gauge.
```

It is not new positioning or synchronization mathematics. Autolocated
relativistic positioning, two-way time transfer, sensor self-calibration, and
joint position-clock rigidity absorb it.

The important result is the exact boundary. If propagation delays are allowed
to be directed and independently unknown, then

\[
p_{ij}=a_{ij}+b_j-b_i
\]

is invariant under

\[
b_i'=b_i+c_i,
\qquad
a_{ij}'=a_{ij}+c_i-c_j.
\tag{3}
\]

No amount of the same timestamp data separates clock offset from path
asymmetry. Unknown transmit/receive latency similarly contaminates both range
and offset. An unknown common clock rate is confounded with spatial scale.
Cryptographic authentication can protect node identity and message integrity,
but cannot prove that a timestamp is truthful or prevent an undetected delay.

Thus the supplied-scaffold objection is partly closed, not moved by
definition:

- the numerical sites and relative offsets can be reconstructed;
- the reciprocal propagation law, stable clock-rate unit, hardware latency,
  honest timestamping, identities, stationarity, and acquisition contract
  remain supplied or independently formed.

No preferred foliation follows. The protocol defines an operational
synchronization and coordinate gauge inside the frozen stationary model. It
does not establish an observer-independent global simultaneity structure.

The live wall narrows again: source formation and event association, physical
warrant for reciprocity/latency/rate, complete acquisition, and no-refit
regional transfer.

## 1. Frozen transcript

Each node \(i\) has:

- a stable identity;
- a stationary spatial site \(s_i\);
- an affine unit-rate clock \(C_i(t)=t+b_i\); and
- a transmitter and receiver whose internal latencies are negligible or
  independently known.

For a message sent at global coordinate time \(\tau\):

\[
S_{ij}=C_i(\tau)=\tau+b_i
\]

is included in the message, while the receiver retains

\[
R_{ij}=C_j(\tau+d_{ij})
=
\tau+d_{ij}+b_j.
\]

The formed crosslink value is

\[
p_{ij}=R_{ij}-S_{ij}
=
d_{ij}+b_j-b_i.
\tag{4}
\]

The minimal transcript contains:

- authenticated sender and receiver identities;
- the send and receive timestamp values;
- a message/attempt identifier joining the pair;
- success, failure, censoring, and retry status;
- the declared hardware-latency treatment; and
- enough bidirectional edges for spatial and clock rigidity.

A signature or message authentication code can make the retained identity and
payload tamper-evident. It cannot certify that an honest physical clock was
read at the claimed boundary or that the path was reciprocal.

## 2. Pairwise range-and-offset theorem

### Theorem 1

Under the frozen transcript and reciprocal propagation, one directed
timestamp exchange in each direction along edge \(\{i,j\}\) determines both
the range \(d_{ij}\) and offset difference \(b_j-b_i\) by (2).

### Proof

Equation (4) gives

\[
p_{ij}=d_{ij}+b_j-b_i,
\]

and reciprocity gives

\[
p_{ji}=d_{ij}+b_i-b_j.
\]

Adding and subtracting yield (2).

This does not determine:

- a common offset added to every \(b_i\);
- any coordinate origin or orientation for the sites; or
- an absolute spatial scale when the common clock rate or propagation speed
  is not independently fixed.

Those are typed gauges or missing calibrations, not failures of the algebra.

## 3. Distance-geometry reconstruction

### Theorem 2

Let the complete graph on four sites have recovered pairwise distances
\(d_{ij}\), and assume the sites are affinely independent. Then their
configuration is determined up to translation and an orthogonal
transformation.

### Proof

Choose node zero as coordinate origin. For \(i,j=1,2,3\), form

\[
G_{ij}
=
\frac{d_{0i}^2+d_{0j}^2-d_{ij}^2}{2}.
\tag{5}
\]

This is the Gram matrix of the three displacement vectors
\((s_i-s_0)\). Affine independence makes \(G\) positive definite. Any
coordinate matrix \(X\) satisfying \(X^\top X=G\) differs from another by an
orthogonal transformation. Restoring \(s_0\) adds a translation.

For the regular-tetrahedron control with sites

\[
(1,1,1),\ (1,-1,-1),\ (-1,1,-1),\ (-1,-1,1),
\]

every squared edge length is eight, and

\[
G=
\begin{pmatrix}
8&4&4\\
4&8&4\\
4&4&8
\end{pmatrix}.
\tag{6}
\]

Its eigenvalues are \(16,4,4\), so the configuration has full rank with a
nonzero conditioning margin.

Reflection is part of the orthogonal gauge. It is not a physical distinction
unless the target includes an independently oriented parity reference.

## 4. Clock reconstruction

### Theorem 3

On a connected crosslink graph, the recovered edge differences \(b_j-b_i\)
determine every clock offset up to one common additive constant.

### Proof

Choose an anchor node and set its representative offset to zero. Sum edge
differences along any path from the anchor to another node. Exact consistent
data give the same value on every path because cycle sums vanish. Any two
solutions differ by a vector constant on every connected component; for a
connected graph that is one common shift.

The common shift is exactly the time-origin gauge:

\[
b_i\mapsto b_i+\beta,
\qquad
t_{\mathrm{event}}\mapsto t_{\mathrm{event}}-\beta.
\tag{7}
\]

Every observable arrival timestamp remains unchanged.

## 5. Composition with event localization

Suppose a held-out outgoing occurrence at \((t,x)\) produces detector
arrivals

\[
y_i=t+\|x-s_i\|+b_i.
\tag{8}
\]

The crosslink transcript reconstructs:

- a coordinate representative of \(s_i\), up to Euclidean isometry; and
- representative offsets \(\widehat b_i=b_i-b_0\).

Correcting the event packet gives

\[
y_i-\widehat b_i
=
(t+b_0)+\|x-s_i\|.
\tag{9}
\]

This is exactly the `HC-DU-107` arrival map with event time represented in
the anchor-clock gauge. The uniform localization margin therefore applies
unchanged after self-calibration.

The reconstruction target is:

\[
\frac{
\{\text{detector sites, clock offsets, event}\}
}{
\text{Euclidean spatial isometry}
\times
\text{common time-origin shift}
}.
\]

It is not an absolute frame, preferred foliation, or full spacetime metric.

## 6. Exact failure under asymmetric delay

Drop reciprocity and write

\[
p_{ij}=a_{ij}+b_j-b_i
\tag{10}
\]

for positive directed delay \(a_{ij}\).

For any sufficiently small node potentials \(c_i\), define (3). Then

\[
a_{ij}'+b_j'-b_i'
=
a_{ij}+c_i-c_j+b_j+c_j-b_i-c_i
=
p_{ij}.
\]

The full directed timestamp transcript is unchanged while the clock offsets
and directed delays differ. This is an exact same-record/different-calibration
witness.

For one pair,

\[
\frac{p_{ij}-p_{ji}}2
=
b_j-b_i+\frac{a_{ij}-a_{ji}}2.
\tag{11}
\]

If only

\[
|a_{ij}-a_{ji}|\le\eta
\]

is known, then the pairwise offset retains uncertainty up to \(\eta/2\).
More samples do not remove a fixed unknown asymmetry unless the physical path
class or intervention family supplies new constraints.

This is the clock-synchronization version of a Dynamic Unity fibre:

```text
same authenticated timestamp record
  -> multiple clock-offset/path-delay completions
  -> different event-time calibration.
```

## 7. Hardware latency and scale

With transmit and receive hardware delays,

\[
p_{ij}
=
d_{ij}
+\ell_i^{\mathrm{tx}}
+\ell_j^{\mathrm{rx}}
+b_j-b_i.
\tag{12}
\]

Adding the two directions no longer isolates range:

\[
\frac{p_{ij}+p_{ji}}2
=
d_{ij}
+
\frac{
\ell_i^{\mathrm{tx}}+\ell_i^{\mathrm{rx}}
+\ell_j^{\mathrm{tx}}+\ell_j^{\mathrm{rx}}
}{2}.
\tag{13}
\]

Subtracting no longer isolates offset either. Independent hardware
calibration, an exact symmetry, or a richer identifiable protocol is needed.
A pair-specific latency can absorb a changed distance exactly.

If instead clocks share an unknown rate \(\alpha\),

\[
C_i(t)=\alpha t+b_i,
\qquad
p_{ij}=\alpha d_{ij}+b_j-b_i.
\tag{14}
\]

For any \(\lambda>0\),

\[
\alpha'=\lambda\alpha,
\qquad
s_i'=s_i/\lambda
\tag{15}
\]

preserves every pseudorange. The crosslinks determine spatial shape but not
absolute scale until a physical rate or propagation-speed unit is fixed.

Clock drift, detector motion, curvature, dispersion, and stochastic latency
require richer time-indexed process models. They are not licensed by the
static theorem.

## 8. Literature collision

### Strongest absorbers

1. [Pascual-Sánchez, *The Relativistic framework of Positioning systems*](https://arxiv.org/abs/0710.1282)
   describes autolocated relativistic positioning: emitters cross-broadcast
   received proper times so users can recover emitter trajectories and metric
   information on the constellation.
2. [Wen et al., *Clock Rigidity and Joint Position-Clock Estimation in Ultra-Wideband Sensor Networks*](https://arxiv.org/abs/2106.02199)
   proves joint position-clock identifiability under bidirectional TOA
   assumptions up to position, offset, and scale gauges.
3. [Ferranti et al., *Sensor Networks TDOA Self-Calibration*](https://arxiv.org/abs/2005.10298)
   treats simultaneous receiver/transmitter position recovery and makes the
   Euclidean gauge and clock-offset burden explicit.
4. [NIST, *Time and Frequency Transfer using the Two Way Method*](https://tf.nist.gov/time/twoway.htm)
   documents the cancellation enabled by symmetric two-way paths and the
   residual transmit/receive, propagation, transponder, and Sagnac
   corrections.
5. [RFC 8915, Network Time Security](https://datatracker.ietf.org/doc/rfc8915/)
   records the asymmetric-delay attack: authenticated messages can be delayed
   without modification, and cryptography does not remove the resulting
   synchronization error.

### Earned Dynamic Unity contribution

Dynamic Unity does not claim new positioning, clock-rigidity, synchronization,
or distance-geometry mathematics. It banks:

- the exact composition from formed reciprocal crosslink records to the
  `HC-DU-107` event packet;
- numerical detector calibration versus law/protocol selection as separate
  obligations;
- spatial isometry, time origin, and scale as separately typed gauges;
- asymmetric delay as a concrete same-record/different-calibration fibre;
- hardware latency as a non-gauge physical remainder unless independently
  calibrated;
- authentication/provenance versus timestamp truth and delay; and
- the correction that operational synchronization does not select a
  fundamental foliation.

## 9. What changed for the North Star

Before this swing, `HC-DU-107` used known detector sites and relative clock
offsets. That could look like the geometry target had been imported whole.
Now the distinction is sharper:

### Closed conditionally

- detector-to-detector ranges;
- constellation shape up to rigid isometry;
- relative clock offsets;
- held-out event localization in the reconstructed scaffold; and
- an explicit finite self-calibration transcript.

### Still supplied or unearned

- why these systems, identities, clocks, and crosslink protocol exist;
- honest timestamp capture at the physical boundary;
- reciprocal propagation or a bound on asymmetry;
- hardware latency and clock-rate calibration;
- stationarity and flat-spacetime applicability;
- formation and association of the nonlinear interaction event;
- complete attempt-level acquisition; and
- no-refit composition into a regional causal/conformal target outside the
  constellation.

The strongest next reopener becomes:

> Form one associable nonlinear interaction event using a target-independent
> finite source family, and show that a reciprocal, clock-rigid crosslink
> network with physically bounded latency/asymmetry completely acquires the
> event packets and transfers them unchanged to a held-out regional causal or
> conformal relation.

This result favors neither record fundamentality nor a hidden global clock.
It shows that a finite network can operationally reconstruct part of its own
scaffold from causal records, while identifying the physical law and
acquisition assumptions that records alone do not select.

## 10. Claim ledger

| Claim | Status | Grade |
|---|---|---:|
| Reciprocal bidirectional pseudoranges recover pairwise range and offset difference | proved in the frozen model | 3 |
| Complete affinely independent \(K_4\) ranges recover the spatial constellation up to Euclidean isometry | proved / standard | 3 |
| Connected edge differences recover offsets up to a common shift | proved / standard | 3 |
| The self-calibrated packet composes with `HC-DU-107` up to natural gauge | proved conditionally | 3 |
| Directed unknown delays make clock offsets nonidentifiable | proved | 4 |
| Hardware latency contaminates both range and offset | proved | 4 |
| Unknown common clock rate is confounded with spatial scale | proved | 4 |
| Cryptographic authentication proves timestamp truth or path reciprocity | false | — |
| The protocol derives a preferred foliation | false | — |
| The crosslink law, nodes, clocks, and hardware are physically selected | not shown | 0 |
| A nonlinear source event is formed and associated | not shown | 0 |
| Regional causal/conformal geometry transfers without refit | open | 0 |
| A novel physical prediction or finite remainder survives standard physics | not shown | 0 |

## 11. Repository disposition

- Bank `HC-DU-108` as a conditional Grade-3 self-calibrated event
  reconstruction and scoped Grade-4 reciprocity/latency/scale necessity
  boundary.
- Add the reciprocal-versus-asymmetric calibration correction to the
  counter-assumptive register.
- Preserve the regular-tetrahedron Gram rank, reciprocal recovery, event
  composition, and hostile gauges in one proportional regression.
- Narrow the candidate class to a source-formed nonlinear interaction event
  with a reciprocal clock-rigid self-calibrating crosslink network, complete
  provenance/acquisition, bounded latency/asymmetry, and no-refit regional
  geometry transfer.
- Keep Dynamic Unity quiescent with no selected successor.
- Do not create a paper, prediction, experiment, hardware path, or external
  action.

## Boundary

This is a scoped exact reconstruction and nonidentifiability result. It is not
a selected physical record law, preferred foliation, nonlinear
source-formation theorem, full Lorentzian reconstruction, new law, empirical
anomaly, prediction, or ontological promotion.
