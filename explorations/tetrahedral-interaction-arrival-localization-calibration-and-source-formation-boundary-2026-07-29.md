---
title: "Tetrahedral interaction-arrival localization, calibration, and source formation"
date: 2026-07-29
status: banked_scoped_result
claim_id: HC-DU-107
work_id: CCR-TETRAHEDRAL-INTERACTION-ARRIVAL-LOCALIZATION-GATE
run_id: RUN-20260729-065106-tetrahedral-interaction-arrival-localization-gate
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
---

# Tetrahedral interaction-arrival localization, calibration, and source formation

## Executive result

The swing returned:

```text
FIXED_TETRAHEDRAL_ARRIVAL_PACKET_LOCALIZES_COMPACT_EVENT_REGION
+ FOUR_CHANNELS_SATURATE_LOCAL_EVENT_DIMENSION_LOWER_BOUND
+ UNIFORM_INVERSE_MARGIN_GIVES_EXPLICIT_NOISE_BOUND
+ RELATIVISTIC_POSITIONING_ABSORBS_LOCALIZATION_MATHEMATICS
+ NONLINEAR_INTERACTION_SUPPLIES_A_FORMATION_CANDIDATE_NOT_THE_INTERFACE
+ UNKNOWN_COMMON_OFFSET_CONFOUNDS_ABSOLUTE_EVENT_TIME
+ UNKNOWN_INDIVIDUAL_OFFSETS_DESTROY_EVENT_IDENTIFIABILITY
+ UNKNOWN_SCAFFOLD_OR_MULTIPLE_EVENTS_REQUIRE_MORE_RECORD_STRUCTURE
+ FIXED_GEOMETRY_LOCALIZATION_IS_NOT_RECORD_FIRST_GEOMETRY
+ SOURCE_FORMATION_CALIBRATION_AND_COMPOSITION_REMAIN_OPEN
+ NO_READY_SUCCESSOR
```

There is now a concrete physical specialization of `HC-DU-106`'s finite
event-packet theorem.

In \(3+1\)-dimensional Minkowski spacetime, place four stationary detectors at
the vertices of a regular tetrahedron surrounding a compact event region.
For an event \(p=(t,x)\), retain the four arrival times of one outgoing null
signal:

\[
A_i(t,x)=t+\|x-s_i\|.
\]

The same four detector channels localize every event in the declared region.
For detector radius \(R\), event-region radius \(\rho=R/20\), and the
tetrahedral arrangement below,

\[
\|A(p)-A(q)\|
\ge
\gamma\|p-q\|,
\qquad
\gamma=\frac{2}{\sqrt3}-\frac4{19}>0.94.
\tag{1}
\]

Thus the packet is globally point-complete, tangent-complete, and robust on
the whole frozen region. Four scalar response coordinates also saturate the
`HC-DU-106` local lower bound for a four-dimensional event target.

This is an exact positive, but not new physics. Relativistic positioning and
emission-coordinate theory already use four null timing coordinates.
Nonlinear Lorentzian inverse theory already shows that wave interactions can
produce artificial point sources whose outgoing singularities expose light
observation sets. Dynamic Unity's gain is the typed composition and boundary:

```text
nonlinear interaction
  -> candidate formed outgoing occurrence

four calibrated arrival channels
  -> exact fixed-scaffold event localization

formed event + retained joined readings + independent calibration
  -> candidate finite certified event packet

many such packets + provenance-preserving composition
  -> still-open regional causal/conformal reconstruction
```

The localization step is not the present wall. **Formation, association,
calibration, acquisition, and no-refit composition are.**

The result does not reconstruct geometry from records. It localizes an event
relative to a geometry, propagation law, coordinate frame, detector
constellation, and clock calibration supplied beforehand. If individual
detector offsets can vary, every alternative event can reproduce the same
four readings. Even one common unknown offset destroys absolute event time.

No external hardware or PDE simulation is needed for this decision. Dynamic
Unity remains quiescent because the physically selected source and calibration
bridge is still absent.

## 1. Frozen physical and operational contract

Use units in which the null propagation speed is one. Let

\[
v_1=\frac{(1,1,1)}{\sqrt3},\quad
v_2=\frac{(1,-1,-1)}{\sqrt3},
\]

\[
v_3=\frac{(-1,1,-1)}{\sqrt3},\quad
v_4=\frac{(-1,-1,1)}{\sqrt3}.
\]

These satisfy

\[
\sum_{i=1}^{4}v_i=0,
\qquad
\sum_{i=1}^{4}v_iv_i^\top=\frac43I_3.
\tag{2}
\]

Fix four stationary detector sites

\[
s_i=-Rv_i
\]

and the convex compact event region

\[
\Theta=[-T,T]\times\overline{B_\rho(0)},
\qquad
0<\rho<R.
\]

For one point event \(p=(t,x)\) that emits an outgoing null singularity, the
ideal arrival map is

\[
A:\Theta\longrightarrow\mathbb R^4,
\qquad
A_i(t,x)=t+\|x+Rv_i\|.
\tag{3}
\]

The target is the four-coordinate event \(p\) **relative to this frozen
Minkowski scaffold**. The packet is four exact scalar values. It becomes a
finite-bit record only after a precision, range, quantizer, retention, and
error contract is supplied.

The physical interpretation is conditional:

- nonlinear source interaction forms one detectable outgoing singularity;
- all four arrivals are associated with that same occurrence;
- propagation is null at the calibrated speed;
- detector sites, clock offsets, and response latencies are known;
- the readings are joined by event provenance and retained; and
- the detector design is frozen before the held-out event.

## 2. Uniform tetrahedral localization theorem

### Theorem 1

For the arrival map in (3), define

\[
\gamma(R,\rho)
=
\frac{2}{\sqrt3}-\frac{4\rho}{R-\rho}.
\tag{4}
\]

If \(\gamma(R,\rho)>0\), then for every \(p,q\in\Theta\),

\[
\|A(p)-A(q)\|
\ge
\gamma(R,\rho)\|p-q\|.
\tag{5}
\]

Consequently, \(A\) is injective, its differential has full rank everywhere,
and its inverse on \(A(\Theta)\) is \(1/\gamma\)-Lipschitz.

### Proof

Write

\[
n_i(x)=\frac{x+Rv_i}{\|x+Rv_i\|}.
\]

The \(i\)-th row of the Jacobian is

\[
DA_i(t,x)=(1,n_i(x)^\top).
\tag{6}
\]

At the center \(x=0\), (2) gives

\[
DA(0)^\top DA(0)
=
\begin{pmatrix}
4&0\\
0&\frac43I_3
\end{pmatrix}.
\tag{7}
\]

Therefore

\[
\sigma_{\min}(DA(0))=\frac2{\sqrt3}.
\tag{8}
\]

For \(\|x\|\le\rho<R\), normalize \(Rv_i+x\). The elementary estimate

\[
\left\|
\frac{Rv_i+x}{\|Rv_i+x\|}-v_i
\right\|
\le
\frac{2\|x\|}{R-\|x\|}
\le
\frac{2\rho}{R-\rho}
\tag{9}
\]

bounds each spatial row perturbation. With four rows, the Frobenius bound
therefore gives

\[
\|DA(t,x)-DA(0)\|_{\mathrm{op}}
\le
\frac{4\rho}{R-\rho}.
\tag{10}
\]

For \(h=p-q\), the line segment from \(q\) to \(p\) lies in \(\Theta\).
Integrating the Jacobian along it,

\[
A(p)-A(q)
=
DA(0)h
+
\int_0^1
\bigl(DA(q+sh)-DA(0)\bigr)h\,ds.
\tag{11}
\]

Equations (8)--(10) and the reverse triangle inequality give (5). This proves
the theorem.

### Fixed numerical specialization

Choose

\[
\rho=\frac R{20}.
\]

Then

\[
\gamma
=
\frac2{\sqrt3}-\frac4{19}
\approx0.944174>0.
\tag{12}
\]

This one array is therefore fixed for the entire compact target class. It is
not reoriented or redesigned for the held-out event.

## 3. Noise and scalar-resource corollaries

Suppose every retained arrival coordinate has error at most \(\epsilon\).
If two events \(p,q\) are both compatible with the same observed packet,
then each pair of ideal arrival coordinates differs by at most \(2\epsilon\).
Hence

\[
\|A(p)-A(q)\|\le 2\epsilon\sqrt4=4\epsilon.
\]

Combining this with (5),

\[
\|p-q\|
\le
\frac{4\epsilon}{\gamma}.
\tag{13}
\]

This is a deterministic finite-error bound, not a statistical confidence
claim.

The event region contains a four-dimensional open set. By the dimension
lower bound in `HC-DU-106`, no continuous exact packet into
\(\mathbb R^N\) can localize it when \(N<4\). The four detector readings
therefore meet the minimal scalar count in this local model.

They are not automatically four finite records:

- exact arrival times are real-valued;
- a physical implementation needs clock resolution and bounded dynamic range;
- joined provenance must associate the readings;
- missed, censored, or thresholded attempts must be accounted for; and
- detector latency enters the response unless independently calibrated.

## 4. Calibration nonidentifiability

### Theorem 2: individual-offset failure

Let the observed readings be

\[
Y_i=A_i(p)+b_i
\tag{14}
\]

with unknown detector clock offsets \(b_i\). For every alternative event
\(p'\in\Theta\), define

\[
b_i'=b_i+A_i(p)-A_i(p').
\tag{15}
\]

Then

\[
A_i(p')+b_i'=A_i(p)+b_i
\]

for all four detectors. Thus the event is completely nonidentifiable when
four independent offsets may refit.

### Corollary: common-offset failure

If all detectors share one unknown offset \(b\), then

\[
(t,x,b)
\quad\text{and}\quad
(t+\delta,x,b-\delta)
\]

produce the same packet. Relative spatial position and relative timing may
remain inferable, but absolute event time is not.

### Further target enlargement

Unknown detector sites, propagation speed, metric, or response latency
enlarge the target beyond four event coordinates. The existing four-channel
map cannot identify arbitrary added parameters. This is not a numerical
shortcoming; it is an exact dimension and gauge issue.

The proper repair is to:

1. independently form and certify the calibration;
2. add calibrating records and charge their resources;
3. quotient only a declared genuine gauge; or
4. weaken the held-out target.

Fitting detector parameters after seeing the event is interface refit.

## 5. What the nonlinear interaction contributes

Kurylev, Lassas, and Uhlmann use nonlinear distorted-wave interactions to
construct artificial point sources and recover earliest light observation
sets. In \(3+1\) dimensions, their rich source-to-solution data determine
topological, differentiable, and conformal spacetime structure under their
stated hypotheses. Lassas, Uhlmann, and Wang extend this semilinear inverse
program.

Those results make a nonlinear interaction a serious physical **formation
candidate**. They do not make the present four-detector packet automatic.
The published inverse constructions retain:

- a supplied Lorentzian manifold or observer region;
- a supplied nonlinear wave law;
- a rich controllable source family;
- source and observation support;
- geometry-informed wave construction and intersection control; and
- a source-to-solution operator or light-observation set richer than four
  untyped scalar readings.

The present theorem closes only this conditional handoff:

```text
one correctly associated outgoing point singularity
  + one fixed calibrated tetrahedral readout
  -> exact event localization in the compact scaffold.
```

It does not prove:

```text
target-independent finite sources
  -> exactly one formed point singularity everywhere in the region
  -> complete joined detector acquisition
  -> calibration selected by the same physics
  -> regional causal/conformal reconstruction without refit.
```

That second chain is the remaining research object.

## 6. Literature collision and novelty

### Strongest absorbers

1. [Coll and Pozo, *Relativistic Positioning Systems: The Emission Coordinates*](https://arxiv.org/abs/gr-qc/0606044)
   develops four null timing coordinates in four-dimensional spacetime. The
   direction of signalling differs from the present receiver arrangement,
   but the coordinate principle absorbs the localization idea.
2. [Kurylev, Lassas, and Uhlmann, *Inverse problems for Lorentzian manifolds and non-linear hyperbolic equations*](https://arxiv.org/abs/1405.3386)
   develops artificial point sources from nonlinear wave interactions and
   reconstructs conformal spacetime from rich light-observation data.
3. [Lassas, Uhlmann, and Wang, *Inverse problems for semilinear wave equations on Lorentzian manifolds*](https://arxiv.org/abs/1606.06261)
   extends the nonlinear source-to-solution reconstruction framework.
4. Standard multilateration, inverse-function stability, and frame geometry
   absorb the tetrahedral conditioning calculation.

### Earned Dynamic Unity contribution

Dynamic Unity does **not** claim new positioning or inverse-wave mathematics.
It banks:

- the exact composition of `HC-DU-105` source-formation provenance with
  `HC-DU-106` finite event localization;
- a uniform no-refit margin for one explicit fixed response packet;
- the exact separation of event formation, association, localization,
  calibration, retention, and geometry reconstruction;
- clock calibration as a necessary record dependency rather than a harmless
  implementation detail; and
- the corrected conclusion that localization is not the decisive remaining
  barrier.

## 7. Implications for the North Star

This result advances the North Star because it turns an abstract possibility
into a clean positive control:

> If physics forms a point occurrence and supplies a fixed calibrated
> four-channel null readout, one finite event packet can reconstruct that
> occurrence robustly.

It also identifies what the result cannot support:

> The packet does not reconstruct the detector scaffold, Minkowski metric,
> propagation law, clock offsets, or source mechanism used to define it.

The next valuable reopener is therefore no longer “find enough event
coordinates.” It is:

> Exhibit a target-independent finite source family that forms one
> associable outgoing interaction singularity throughout a frozen compact
> region, together with independently formed detector calibration and
> complete acquisition, and transfer the unchanged event packets into a
> held-out regional causal or conformal relation.

This is narrower than full continuum reconstruction and stronger than
mathematical localization. It has three informative returns:

1. **positive:** formation plus calibration is physically selected and the
   regional transfer works;
2. **mixed:** physics selects the occurrence but not its access/calibration
   interface; or
3. **negative:** geometry-informed source design or refittable calibration is
   unavoidable.

No branch is ready for activation on the present evidence. The repository
should remain quiescent.

## 8. Claim ledger

| Claim | Status | Grade |
|---|---|---:|
| The tetrahedral arrival map is globally bi-Lipschitz on the declared compact event region | proved in this scoped model | 3 |
| Four scalar channels saturate the local dimension lower bound | proved in this scoped model | 4 |
| Coordinate error gives the bound \(4\epsilon/\gamma\) | proved conditionally | 3 |
| Unknown individual detector offsets destroy event identifiability | proved | 4 |
| One common unknown offset destroys absolute event time | proved | 4 |
| Four null timing coordinates are novel | false; absorbed by positioning theory | — |
| Nonlinear interactions can create useful artificial point sources | imported from nonlinear Lorentzian inverse theory | external |
| The fixed detector scaffold is physically selected | not shown | 0 |
| The outgoing event is formed, uniquely associated, and completely acquired by this theorem | not shown | 0 |
| The packet reconstructs geometry rather than coordinates inside supplied geometry | false | — |
| Many packets reconstruct held-out regional causal/conformal geometry without refit | open | 0 |
| A novel physical prediction or finite remainder survives | not shown | 0 |

## 9. Repository disposition

- Bank `HC-DU-107` as a conditional Grade-3 fixed-scaffold event
  reconstruction and scoped Grade-4 calibration/formation necessity
  boundary.
- Add the calibration and geometry-supply correction to the
  counter-assumptive register.
- Preserve the tetrahedral geometry, margin, and offset witnesses in one
  proportional regression.
- Narrow the candidate class to source-formed nonlinear interaction events
  with fixed calibrated arrival readout, complete provenance/acquisition, and
  no-refit regional transfer.
- Keep Dynamic Unity quiescent with no selected successor.
- Do not create a paper, prediction, experiment, hardware path, or external
  action.

## Boundary

This is a scoped exact theorem and absorber audit. It is not a selected
physical record theory, nonlinear source-formation theorem, geometry
reconstruction, new law, empirical anomaly, prediction, or ontological
promotion.
