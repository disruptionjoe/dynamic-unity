---
run_id: RUN-20260729-065106-tetrahedral-interaction-arrival-localization-gate
status: completed
started_at: 2026-07-29T06:51:06-05:00
completed_at: 2026-07-29T06:56:13-05:00
repository: dynamic-unity
authority: "Joe direct chat: Go"
work_id: CCR-TETRAHEDRAL-INTERACTION-ARRIVAL-LOCALIZATION-GATE
claim_id: HC-DU-107
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
maximum_grade: "Conditional Grade 3 fixed-scaffold event reconstruction plus scoped Grade 4 calibration and formation necessity boundary; no Grade-5 physical remainder or prediction"
external_action_authorization: "Primary-source research plus repository-local proof, evidence, authority, register, regression, explicit-path commit, and non-force push only; no publication, submission, hardware, provider, contact, or other external action."
---

# Tetrahedral interaction-arrival localization gate

## Cold-start contract

Dynamic Unity's purpose is to make physical reality intelligible as one
coherent, evidence-accountable whole. Its North Star is to determine whether
independently selected, observer-indexed certified causal records reconstruct
all observer-accessible time, geometry, fields, and capability, or expose a
finite physical remainder.

The repository begins quiescent at revision 57. `HC-DU-105` gives a finite
counterfactual packet for one nonlinear source-provenance coefficient, and
`HC-DU-106` proves that a compact four-dimensional event target can in
principle admit an exact finite response embedding. Neither result exhibits
one unchanged physically meaningful response family.

This swing freezes the simplest serious specialization:

> A nonlinear interaction forms one outgoing point singularity in a compact
> \(3+1\)-dimensional Minkowski event region; four stationary detectors at
> regular-tetrahedron sites retain its first-arrival times.

The question is whether those same four channels are point- and
tangent-complete with a uniform margin throughout the region, and which
calibration or source-formation assumptions are logically necessary.

The evidence boundary is an exact arrival-map theorem, exact calibration
counterexamples, collision with relativistic emission-coordinate and
nonlinear Lorentzian inverse literature, and a proportional local regression.
The nonlinear formation premise is imported conditionally; no PDE simulation
or external hardware is warranted.

Keep independent:

- **interaction formation:** whether admitted sources physically create a
  detectable outgoing singularity;
- **event association:** whether all four arrivals came from that one event;
- **event localization:** whether the four readings identify its spacetime
  coordinates relative to the frozen scaffold;
- **calibration:** detector positions, clock offsets, propagation law, and
  detector latency;
- **retention:** whether joined arrival readings form an acquired record;
- **geometry reconstruction:** whether the scaffold itself is inferred rather
  than supplied; and
- **regional composition:** whether many localized events transfer without
  refit to a held-out causal or conformal target.

## Frozen typed objects

Use units with propagation speed \(c=1\). Let

\[
v_1=(1,1,1)/\sqrt 3,\quad
v_2=(1,-1,-1)/\sqrt 3,
\]

\[
v_3=(-1,1,-1)/\sqrt 3,\quad
v_4=(-1,-1,1)/\sqrt 3,
\]

and fix detector positions \(s_i=-Rv_i\). The admitted event region is

\[
\Theta=[-T,T]\times\overline{B_\rho(0)}
\]

with \(R>0\) and \(\rho=R/20\). For an event \(p=(t,x)\), define the arrival
packet

\[
A(p)=\bigl(t+\|x-s_i\|\bigr)_{i=1}^{4}.
\]

The held-out target is the event \(p\), relative to this declared Minkowski
frame and detector scaffold.

## Exact questions

1. Is \(A\) globally injective on \(\Theta\)?
2. Does \(A\) have a positive uniform inverse-Lipschitz margin?
3. Do four scalar readings saturate the local target-dimension lower bound?
4. How does coordinate error bound event-localization error?
5. Which result is standard positioning mathematics rather than a Dynamic
   Unity contribution?
6. Does nonlinear interaction select the outgoing occurrence, its association,
   or the detector interface?
7. What happens when detector clock offsets, sites, propagation law, latency,
   or event association are not independently fixed?
8. Does this reconstruct geometry from records, or only localize an event
   inside supplied geometry?
9. What exact reopener remains for a source-formed, calibrated, no-refit
   regional reconstruction?

## Pre-registered return states

```text
FIXED_TETRAHEDRAL_ARRIVAL_PACKET_LOCALIZES_COMPACT_EVENT_REGION
FOUR_CHANNELS_SATURATE_LOCAL_EVENT_DIMENSION_LOWER_BOUND
UNIFORM_INVERSE_MARGIN_GIVES_EXPLICIT_NOISE_BOUND
RELATIVISTIC_POSITIONING_ABSORBS_LOCALIZATION_MATHEMATICS
NONLINEAR_INTERACTION_SUPPLIES_A_FORMATION_CANDIDATE_NOT_THE_INTERFACE
UNKNOWN_COMMON_OFFSET_CONFOUNDS_ABSOLUTE_EVENT_TIME
UNKNOWN_INDIVIDUAL_OFFSETS_DESTROY_EVENT_IDENTIFIABILITY
UNKNOWN_SCAFFOLD_OR_MULTIPLE_EVENTS_REQUIRE_MORE_RECORD_STRUCTURE
FIXED_GEOMETRY_LOCALIZATION_IS_NOT_RECORD_FIRST_GEOMETRY
SOURCE_FORMATION_CALIBRATION_AND_COMPOSITION_REMAIN_OPEN
NO_READY_SUCCESSOR
```

## Assumption and warrant discipline

- `STANDARD`: Minkowski null propagation, Euclidean norm estimates,
  singular-value perturbation, multilateration, emission coordinates, and
  elementary inverse-function stability.
- `IMPORTED`: nonlinear wave interactions can create artificial point-source
  singularities whose earliest light observations support Lorentzian inverse
  reconstruction.
- `PROJECT_NATIVE`: source/event/readout provenance typing, fixed versus
  selected scaffold, no-refit transfer, complete acquisition, target-relative
  reconstruction, and regional record composition.
- `CONDITIONAL_POSIT`: one detectable outgoing event is formed in the declared
  region; arrivals are correctly associated; clocks, detector sites,
  propagation speed, response latency, and coordinate frame are calibrated
  independently; the four readings are joined and retained.

## Cheapest constructive positive

At \(x=0\), the Jacobian rows are \((1,v_i^\top)\), and

\[
DA(0)^\top DA(0)
=
\operatorname{diag}(4,4/3,4/3,4/3).
\]

Thus \(\sigma_{\min}(DA(0))=2/\sqrt 3\). On
\(\|x\|\le\rho<R\), the spatial row direction changes by at most
\(2\rho/(R-\rho)\). The four-row operator perturbation is at most
\(4\rho/(R-\rho)\). Integrating the Jacobian along the segment between any
two events gives

\[
\|A(p)-A(q)\|
\ge
\left(
\frac{2}{\sqrt3}-\frac{4\rho}{R-\rho}
\right)\|p-q\|.
\]

At \(\rho=R/20\), the margin is

\[
\gamma=\frac{2}{\sqrt3}-\frac4{19}>0.94.
\]

## Cheapest exact kills

1. **Individual clock-offset kill.** With
   \(Y_i=A_i(p)+b_i\), any alternative event \(p'\) reproduces the same packet
   by choosing \(b_i'=b_i+A_i(p)-A_i(p')\).
2. **Common-offset kill.** One unknown common offset is exactly confounded
   with absolute event time.
3. **Scaffold kill.** Unknown detector positions, propagation speed, or
   metric add target degrees of freedom not identified by four readings.
4. **Association kill.** With multiple interaction sites, four first arrivals
   need not share one provenance.
5. **Threshold kill.** Source formation below detector threshold, or
   source-dependent detection latency, changes the response map.
6. **Selection kill.** The theorem uses a supplied tetrahedral scaffold and
   Minkowski geometry. It does not derive or physically select either.

## Stops

- do not report a new positioning, multilateration, or nonlinear inverse-wave
  theorem;
- do not treat four exact real coordinates as a finite-bit physical record;
- do not infer a formed interaction from an assumed point event;
- do not infer event association from four unlabeled first arrivals;
- do not treat synchronized clocks or known detector locations as free;
- do not call localization inside known geometry reconstruction of geometry;
- do not import geometry-informed Gaussian-beam design as target-independent
  source formation;
- do not infer regional causal or conformal geometry from one localized event;
- do not activate a successor without a source-formation and calibration
  result that survives no-refit transfer;
- do not build a PDE model when direct analysis decides the present gate; and
- do not create a paper, prediction, experiment, hardware path, or external
  action.

## Local-model disposition

`DESK_RESEARCH_FIRST`. Elementary geometry and primary literature decide the
scientific boundary. One deterministic numerical regression preserves the
margin and calibration witnesses; it earns no independent learning claim.

## Durable outputs

- one uniform tetrahedral arrival-time localization theorem;
- one explicit finite-error localization corollary;
- one exact clock-offset nonidentifiability theorem;
- one selected-versus-supplied scaffold audit;
- one source-formation versus event-localization separation;
- one corrected physical reopener;
- proportional regression controls;
- the minimum authority, concept, orientation, counter-assumptive, and
  regression updates; and
- one governed closeout receipt.

## Completion

This run is complete only when the result is banked, regression controls pass,
current routing remains honest, explicit paths are committed and pushed, and
the repository session closes cleanly.
