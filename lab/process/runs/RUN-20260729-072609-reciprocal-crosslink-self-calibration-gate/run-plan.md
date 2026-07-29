---
run_id: RUN-20260729-072609-reciprocal-crosslink-self-calibration-gate
status: completed
started_at: 2026-07-29T07:26:09-05:00
completed_at: 2026-07-29T07:31:25-05:00
repository: dynamic-unity
authority: "Joe direct chat: Go"
work_id: CCR-RECIPROCAL-CROSSLINK-SELF-CALIBRATION-GATE
claim_id: HC-DU-108
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
external_action_authorization: "Primary-source research plus repository-local proof, evidence, authority, register, regression, explicit-path commit, and non-force push only; no publication, submission, hardware, provider, contact, or other external action."
---

# Reciprocal-crosslink self-calibration gate

## Cold-start contract

Dynamic Unity's purpose is to make physical reality intelligible as one
coherent, evidence-accountable whole. Its North Star is to determine whether
independently selected, observer-indexed certified causal records reconstruct
all observer-accessible time, geometry, fields, and capability, or expose a
finite physical remainder.

The repository begins quiescent at revision 58. `HC-DU-107` proves that four
fixed tetrahedral arrival channels robustly localize one event inside a known
Minkowski detector scaffold. It also proves that free clock offsets destroy
absolute event identification.

The unspent obligation is:

> Can the detector network form a finite reciprocal crosslink transcript that
> reconstructs its own positions and relative clock offsets up to natural
> gauge, so event localization no longer imports those numerical calibration
> values?

The evidence boundary is an exact stationary flat-spacetime theorem, exact
asymmetric-delay/hardware-latency/clock-scale counterexamples, collision with
autolocated relativistic positioning, time transfer, sensor self-calibration,
and clock rigidity, plus a proportional local regression. No external
hardware is needed.

Keep independent:

- **crosslink identity and provenance:** which node sent and received;
- **timestamp honesty:** whether the included values equal local clock
  readings;
- **clock model:** rate, offset, drift, and stability;
- **propagation law:** reciprocal or directed, stationary or changing;
- **hardware latency:** transmit, receive, processing, and turnaround delays;
- **distance geometry:** the node configuration modulo rigid motion;
- **time gauge:** common clock-origin translation;
- **scale gauge:** common clock-rate/spatial-scale ambiguity;
- **event formation and association:** which outgoing occurrence produced the
  held-out arrival packet; and
- **regional reconstruction:** transfer beyond the detector constellation.

## Frozen typed objects

Let four honest stationary nodes have affinely independent positions
\(s_i\in\mathbb R^3\) and affine clocks

\[
C_i(t)=t+b_i.
\]

Propagation is reciprocal at unit speed:

\[
d_{ij}=d_{ji}=\|s_i-s_j\|.
\]

For a message sent by \(i\) at global time \(\tau\), the packet contains the
send timestamp \(C_i(\tau)\), and \(j\) retains the receive timestamp
\(C_j(\tau+d_{ij})\). The directed pseudorange is

\[
p_{ij}=d_{ij}+b_j-b_i.
\]

All twelve directed crosslinks are joined by authenticated node identity.
Authentication establishes origin and transcript integrity only; timestamp
truth is part of the honest-node posit.

## Exact questions

1. Do reciprocal directed pseudoranges recover every pairwise distance and
   relative clock offset?
2. Does a complete affinely independent four-node distance graph recover the
   constellation up to Euclidean isometry?
3. Does a connected crosslink graph recover offsets up to one common time
   origin?
4. Does the recovered scaffold compose with `HC-DU-107` to localize events up
   to spatial-isometry and time-origin gauge?
5. Which content is already absorbed by autonomous positioning, two-way time
   transfer, distance geometry, sensor self-calibration, and clock rigidity?
6. What fails when directed propagation delay is asymmetric?
7. What fails when transmit/receive/processing latency is uncalibrated?
8. What fails when the common clock rate or propagation scale is unknown?
9. Does the protocol select a preferred foliation or only define one
   operational coordinate gauge?
10. Which source-formation and regional-transfer obligations remain?

## Pre-registered return states

```text
RECIPROCAL_BIDIRECTIONAL_TIMESTAMPS_RECOVER_RANGE_AND_OFFSET_DIFFERENCE
AFFINELY_INDEPENDENT_COMPLETE_K4_RECOVERS_CONSTELLATION_UP_TO_EUCLIDEAN_ISOMETRY
CONNECTED_CROSSLINKS_RECOVER_CLOCK_OFFSETS_UP_TO_COMMON_SHIFT
HC_DU_107_COMPOSES_TO_SELF_CALIBRATED_EVENT_LOCALIZATION_UP_TO_GAUGE
AUTONOMOUS_POSITIONING_AND_CLOCK_RIGIDITY_ABSORB_THE_MATHEMATICS
UNKNOWN_ASYMMETRIC_DELAY_CONFUNDS_CLOCK_OFFSET
UNKNOWN_HARDWARE_LATENCY_CONFUNDS_RANGE_AND_OFFSET
UNKNOWN_COMMON_CLOCK_RATE_CONFUNDS_SPATIAL_SCALE
AUTHENTICATION_CERTIFIES_ORIGIN_NOT_TIMESTAMP_TRUTH_OR_DELAY
SELF_CALIBRATION_DOES_NOT_SELECT_A_FOLIATION
SOURCE_FORMATION_ASSOCIATION_AND_REGIONAL_TRANSFER_REMAIN_OPEN
NO_READY_SUCCESSOR
```

## Assumption and warrant discipline

- `STANDARD`: bidirectional time transfer, distance geometry, graph
  connectivity, Euclidean rigidity, affine clocks, and gauge quotienting.
- `IMPORTED`: autolocated relativistic positioning, TOA/TDOA
  self-calibration, joint position-clock rigidity, NIST two-way transfer, and
  the standard asymmetric-delay limit.
- `PROJECT_NATIVE`: formed record versus transcript, honest provenance versus
  truth, calibration as a reconstructible target, no-refit composition into
  `HC-DU-107`, and source/event/regional separation.
- `CONDITIONAL_POSIT`: stationary honest nodes, unit and stable clock rates,
  reciprocal unit-speed propagation, accurately captured send/receive
  timestamps, negligible or independently known hardware latency, complete
  crosslink acquisition, and affine independence.

## Cheapest constructive positive

For each unordered pair,

\[
\frac{p_{ij}+p_{ji}}2=d_{ij},
\qquad
\frac{p_{ij}-p_{ji}}2=b_j-b_i.
\]

The complete distance matrix reconstructs four affinely independent spatial
sites up to Euclidean isometry. Relative clock offsets on a connected graph
reconstruct all \(b_i\) up to a common shift. Choose one spatial frame and one
clock origin, correct the held-out arrival readings, and apply `HC-DU-107`.

## Cheapest exact kills

1. **Directed-delay gauge.** If
   \(p_{ij}=a_{ij}+b_j-b_i\) with free directed delay \(a_{ij}\), then
   \[
   b_i'=b_i+c_i,\qquad
   a_{ij}'=a_{ij}+c_i-c_j
   \]
   leaves every timestamp unchanged.
2. **Asymmetry uncertainty.** The nominal offset estimator contains
   \((a_{ij}-a_{ji})/2\); an asymmetry bound \(\eta\) leaves at least
   \(\eta/2\) pairwise offset uncertainty.
3. **Hardware-latency gauge.** Unknown transmit/receive delays enter both the
   symmetric range estimate and antisymmetric offset estimate. Pairwise
   latency can absorb a changed distance exactly.
4. **Clock-scale gauge.** With \(C_i(t)=\alpha t+b_i\), pseudorange contains
   \(\alpha d_{ij}\). The transformation
   \(\alpha'=\lambda\alpha,\ s_i'=s_i/\lambda\) leaves it unchanged.
5. **Truth kill.** A signature proves who signed a timestamp, not that the
   timestamp, latency, or claimed clock state is physically correct.
6. **Dynamics kill.** Motion, curvature, dispersion, or time-varying paths
   invalidate the static Euclidean reduction unless modeled and acquired.

## Stops

- do not report a new time-transfer, positioning, rigidity, or distance-
  geometry theorem;
- do not call the recovered coordinate representative an observer-independent
  absolute frame;
- do not treat a common time-origin or spatial isometry gauge as a physical
  remainder;
- do not infer a preferred foliation from an operational synchronization
  convention;
- do not treat authentication as truth, reciprocity, or latency calibration;
- do not silently set hardware delays or clock rates to known values;
- do not extend the flat stationary theorem to curved or dynamic spacetime;
- do not infer source formation, event association, or complete acquisition
  from calibration;
- do not infer regional geometry from the detector constellation alone;
- do not activate a successor without a target-independent formed source and
  unchanged regional transfer;
- do not build a simulation when exact algebra decides the gate; and
- do not create a paper, prediction, experiment, hardware path, or external
  action.

## Local-model disposition

`DESK_RESEARCH_FIRST`. Exact algebra and existing primary literature decide
the scientific boundary. One exact/numerical regression preserves the
regular-tetrahedron Gram rank, reciprocal recovery, event-packet composition,
and hostile gauges; it earns no independent learning claim.

## Durable outputs

- one reciprocal crosslink self-calibration theorem;
- one distance-geometry and clock-gauge composition;
- one self-calibrated `HC-DU-107` event-localization corollary;
- exact directed-delay, latency, and clock-scale counterexamples;
- one cryptographic provenance/truth boundary;
- one flat-operational-gauge versus preferred-foliation correction;
- one corrected physical reopener and candidate class;
- proportional regression controls;
- the minimum authority, concept, orientation, counter-assumptive, and
  regression updates; and
- one governed closeout receipt.

## Completion

This run is complete only when the result is banked, regression controls pass,
current routing remains honest, explicit paths are committed and pushed, and
the repository session closes cleanly.
