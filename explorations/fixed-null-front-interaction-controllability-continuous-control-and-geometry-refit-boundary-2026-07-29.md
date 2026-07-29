---
title: "Fixed null-front interaction controllability, continuous control, and geometry-refit boundary"
date: 2026-07-29
status: banked_scoped_result
claim_id: HC-DU-109
work_id: CCR-FIXED-NULL-FRONT-INTERACTION-FORMATION-GATE
run_id: RUN-20260729-075132-fixed-null-front-interaction-formation-gate
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
maximum_grade: "Conditional Grade 3 fixed-architecture event-formation controllability in a supplied flat 3+1 arena plus scoped Grade 4 channel-rank, finite-control, latency, and no-refit necessity boundaries; no Grade-5 physical remainder or prediction"
---

# Fixed null-front interaction controllability, continuous control, and geometry-refit boundary

## Executive result

The swing returned:

```text
ONE_FIXED_FOUR_NULL_FRONT_ARCHITECTURE_CONTROLS_EVERY_FLAT_EVENT
+ FOUR_CONTINUOUS_PHASE_CONTROLS_ARE_BIJECTIVE_WITH_EVENT_COORDINATES
+ THREE_SCALAR_PHASE_CHANNELS_LEAVE_A_ONE_DIMENSIONAL_INTERSECTION_FIBRE
+ PHASE_TO_EVENT_MAP_HAS_AN_EXACT_POSITIVE_CONDITIONING_MARGIN
+ FINITE_EXACT_CONTROL_CODEBOOK_COVERS_ONLY_FINITELY_MANY_EVENTS
+ FINITE_BITS_SUPPORT_ONLY_FINITE_RESOLUTION
+ UNKNOWN_SOURCE_LATENCY_CONFUNDS_EVENT_LOCATION
+ FRONT_INTERSECTION_DOES_NOT_BY_ITSELF_PROVE_NONLINEAR_SIGNAL_FORMATION
+ UNKNOWN_CURVED_GEOMETRY_REQUIRES_EIKONAL_OR_GEODESIC_CONTROL_NOT_PROVIDED_HERE
+ CONTINUOUS_PREDECLARED_CONTROLS_ARE_NOT_ARCHITECTURE_REFIT
+ TARGET_GEOMETRY_CODED_CONTROL_DESIGN_IS_INTERFACE_REFIT
+ NONLINEAR_INVERSE_THEORY_ABSORBS_ARTIFICIAL_POINT_SOURCE_CONCEPT
+ FORMATION_PROVENANCE_ACQUISITION_AND_REGIONAL_NO_REFIT_TRANSFER_REMAIN_OPEN
+ NO_READY_SUCCESSOR
```

The source-formation problem is not blocked at the level of flat-space
kinematics. One fixed set of four null fronts can be translated in phase so
that all four meet at any chosen event in \(3+1\)-dimensional Minkowski space.
The directions do not change between events.

Let

\[
L=
\begin{pmatrix}
1&1&0&0\\
1&-1&0&0\\
1&0&1&0\\
1&0&0&1
\end{pmatrix},
\qquad
\phi_i(p)=\ell_i p-c_i.
\]

Every row \(\ell_i\) is null for the \((-+++)\) metric and

\[
\det L=-2.
\]

The four phase settings \(c\) therefore determine exactly one intersection
event:

\[
t=\frac{c_1+c_2}{2},\quad
x=\frac{c_1-c_2}{2},\quad
y=c_3-t,\quad
z=c_4-t.
\tag{1}
\]

Conversely, every event \(p\) is addressed by \(c=Lp\). This is a useful
constructive correction to an overly strong worry that nonlinear interaction
experiments must redesign their source architecture around every held-out
event.

It does **not** yet form the physical event Dynamic Unity needs. Equation (1)
only proves that four ideal null hypersurfaces meet. A nonlinear wave equation
must still generate a nonzero, stable, outgoing mixed response at that
intersection; the inputs and output must be associated and completely
acquired; and the same control and decoder must transfer to an unknown
regional geometry without encoding that geometry in the controls.

The clean resource split is:

```text
fixed architecture
  = four null directions and one coupling law

trial control
  = four continuously variable phase/timing values

physical formation
  = a nondegenerate nonlinear mixed response at their intersection

formed record
  = retained joint source identity, realized controls, and outgoing response

regional reconstruction
  = one frozen map from those records to a held-out geometric target.
```

## 1. Exact flat-space theorem

### Definition

Use Minkowski coordinates \(p=(t,x,y,z)\) with metric

\[
\eta=\operatorname{diag}(-1,1,1,1).
\]

Freeze four phase covectors

\[
\begin{aligned}
\ell_1&=(1,1,0,0),\\
\ell_2&=(1,-1,0,0),\\
\ell_3&=(1,0,1,0),\\
\ell_4&=(1,0,0,1).
\end{aligned}
\]

Each satisfies

\[
\eta^{-1}(\ell_i,\ell_i)=0.
\]

For a control vector \(c\in\mathbb R^4\), define four null hyperplanes

\[
H_i(c_i)=\{p:\ell_i p=c_i\}.
\]

### Theorem: fixed-architecture event addressing

For every \(c\in\mathbb R^4\),

\[
\bigcap_{i=1}^{4}H_i(c_i)
\]

contains exactly one event \(p=L^{-1}c\). For every event
\(p_\star\in\mathbb R^{1,3}\), the fixed architecture reaches it using
\(c=Lp_\star\).

### Proof

Direct row reduction gives

\[
\det L=-2\ne0.
\]

Thus \(L\) is bijective. Its inverse is

\[
L^{-1}=
\begin{pmatrix}
\frac12&\frac12&0&0\\
\frac12&-\frac12&0&0\\
-\frac12&-\frac12&1&0\\
-\frac12&-\frac12&0&1
\end{pmatrix},
\]

which is exactly equation (1). No source direction changes with \(c\).
\(\square\)

### What the theorem earns

- one fixed architecture covers every event algebraically;
- four real controls are enough;
- no event-specific change of propagation direction is needed in the supplied
  flat arena;
- the phase-to-event decoder is exact and fixed; and
- the target event and the control settings are in one-to-one correspondence.

### What it does not earn

- realization of infinite null hyperplanes by finite physical sources;
- a nonlinear interaction term of the required order;
- a nonzero outgoing principal symbol or detectable amplitude;
- suppression of pairwise and lower-order responses;
- absence of finite-width, caustic, boundary, or multiple-interaction effects;
- source timing truth or latency calibration;
- retained provenance or complete acquisition;
- unknown-geometry controllability;
- geometry reconstruction; or
- a physical record-selection theorem.

## 2. Exact conditioning

The Gram matrix is

\[
L^\mathsf{T}L=
\begin{pmatrix}
4&0&1&1\\
0&2&0&0\\
1&0&1&0\\
1&0&0&1
\end{pmatrix}.
\]

Its eigenvalues are

\[
\left\{
\frac{5-\sqrt{17}}2,\ 1,\ 2,\ \frac{5+\sqrt{17}}2
\right\}.
\]

Therefore

\[
\sigma_{\min}(L)
=
\sqrt{\frac{5-\sqrt{17}}2}
\approx0.662153.
\tag{2}
\]

For phase error \(\Delta c\),

\[
\|\Delta p\|_2
\le
\frac{\|\Delta c\|_2}{\sigma_{\min}(L)}.
\tag{3}
\]

If each of the four phase channels has absolute error at most \(\epsilon\),
then \(\|\Delta c\|_2\le2\epsilon\), so

\[
\|\Delta p\|_2
\le
\frac{2\epsilon}{\sigma_{\min}(L)}
\approx3.02045\epsilon.
\tag{4}
\]

This is a real positive finite-resolution certificate in the flat control. It
does not supply a physical noise distribution or prove that the commanded
phase is the realized phase.

## 3. Why four channels are the exact local minimum

The first three rows of \(L\) annihilate

\[
v=(0,0,0,1).
\]

Three fixed scalar phase constraints therefore leave the line

\[
p+\alpha v
\]

indistinguishable. More generally, a continuous map from an open
four-dimensional event region into fewer than four smooth scalar coordinates
cannot be a local smooth embedding.

The fourth independent phase closes this specific fibre. This agrees with
`HC-DU-107`'s four-scalar lower bound on event localization, but the direction
of the map is reversed:

```text
HC-DU-107:
  unknown event -> four retained arrival readings

HC-DU-109:
  four commanded phases -> intended interaction event.
```

The shared number four comes from event dimension, not from a new physical
constant.

## 4. Continuous control is not a finite packet

The positive theorem uses a fixed architecture but a continuum of phase
settings. Those are different resources.

Because \(L\) is bijective, a codebook with \(M\) distinct exact settings
forms at most \(M\) exact intersection events. No finite codebook exactly
covers a compact region with nonempty four-dimensional interior.

At finite target resolution \(\delta\), the situation is constructive. A
finite \(\delta\)-net of the event region maps through \(L\) to a finite phase
codebook. Equation (4) says that coordinatewise phase resolution

\[
\epsilon\le\frac{\delta\,\sigma_{\min}(L)}2
\]

is sufficient for event error at most \(\delta\). The number of codewords must
still grow at least like the packing number of the target region; for an
ordinary four-dimensional region this is asymptotically proportional to
\(\delta^{-4}\).

Thus:

- exact continuum addressing requires continuum-valued controls;
- finite bits support only finite resolution;
- a target-independent finite codebook is legitimate for a declared finite
  target resolution; and
- the source-control budget must be charged separately from the number of
  physical source channels.

## 5. Exact source-latency gauge

Suppose the retained command is \(c\), but the physically realized phase is

\[
c+\lambda,
\]

where \(\lambda\) contains unknown per-channel emission or transduction
latency. The formed event is

\[
p=L^{-1}(c+\lambda).
\]

For any alternative event \(p'\), the same retained command is compatible
with

\[
\lambda'
=
\lambda+L(p'-p),
\]

whenever both latency vectors remain physically admitted.

The regression contains a positive-latency witness. The command

\[
c=(1,1,1,1)
\]

with latency

\[
\lambda=(1,1,1,1)
\]

forms \(p=(2,0,0,0)\), while the same command with

\[
\lambda'=(1.2,1.0,1.1,1.1)
\]

forms \(p'=(2.1,0.1,0,0)\).

Therefore a command transcript is not a physical phase record. `HC-DU-108`
self-calibrates the **detector** scaffold under reciprocal crosslinks; it does
not calibrate the four **source** emission chains.

This boundary can be narrowed by independent source monitoring, reciprocal
loopback, bounded differential latency, or direct phase readout. Each repair
adds a formed interface and must preserve trial association. Cryptographic
authentication can protect the command's origin and integrity but cannot prove
that the source physically realized it at the claimed phase.

## 6. Front intersection versus nonlinear event formation

The elementary theorem proves a unique joint intersection of ideal fronts. It
does not prove a nonlinear outgoing event.

That distinction is already visible in the primary literature:

- Kurylev, Lassas, and Uhlmann use the nonlinearity of a hyperbolic equation
  to create artificial point-source behavior and reconstruct conformal
  spacetime structure from a supplied source-to-solution operator
  ([arXiv:1405.3386](https://arxiv.org/abs/1405.3386)).
- Lassas, Uhlmann, and Wang reconstruct the conformal class from the
  source-to-solution map for semilinear waves in four-dimensional Lorentzian
  spacetime
  ([arXiv:1606.06261](https://arxiv.org/abs/1606.06261)).
- Lassas, Liimatainen, Pohjola, and Tyni develop an explicit calculus for
  nonlinear Gaussian-beam interactions and recover coefficients and a source
  under stated gauge and geometric assumptions
  ([arXiv:2510.11494](https://arxiv.org/abs/2510.11494)).

These results make physical nonlinear event formation a serious route. They
also absorb any novelty claim for the broad idea. Their positive theorems use
rich source-to-solution data, supplied observation regions, a supplied
Lorentzian PDE class, and waves or beams chosen through the relevant geometry.

The remaining DU question is not whether nonlinear interactions *can* act as
point sources in a theorem. It is whether a finite, physically formed,
target-independent source and record packet supplies enough of that interface
without importing the held-out geometry.

## 7. The curved-geometry boundary

In a curved spacetime, a high-frequency phase \(S\) obeys the eikonal equation

\[
g^{\mu\nu}\partial_\mu S\,\partial_\nu S=0.
\]

The constant covectors in \(L\) are null only relative to the supplied
Minkowski metric. Unknown curvature changes the null fronts, their meeting
sets, their caustics, and their amplitudes. Equation (1) is therefore not a
curved-spacetime decoder.

Two practices must be distinguished:

1. **Legitimate predeclared control.** Freeze a physical source architecture,
   a finite-resolution control codebook, and a retained command/response
   packet before observing the held-out geometry. Apply them unchanged and
   infer what the actual interactions reveal.
2. **Interface refit.** Use the unknown or held-out metric to calculate
   geodesics, Gaussian beams, phase settings, source supports, or a decoder
   that ensures a desired intersection, then count the resulting event as
   evidence reconstructing that metric.

The first is an experiment. The second can be a valid existence proof inside a
known geometry, but it is circular as record-first reconstruction.

Continuous controls themselves are not refit. Experimental control parameters
may vary. Refit occurs when their selection rule uses the held-out target or
changes the interface after seeing target-specific data.

## 8. Composition with the current event packet

The current constructive chain is:

```text
HC-DU-109
fixed null-front architecture + phase controls
  -> intended flat-space joint intersection

nonlinear PDE premise
  -> outgoing mixed response

HC-DU-105
all required on/off contexts
  -> joint-source Möbius provenance coefficient

HC-DU-108
reciprocal detector crosslinks
  -> detector geometry + relative clocks up to gauge

HC-DU-107
four associated arrivals
  -> event localization up to spatial isometry and time origin.
```

This is more than a loose analogy. Each arrow now has a typed mathematical
contract. It is still not one complete physical reconstruction theorem.

The missing arrows are:

- physical realization of the four fronts by finite source supports;
- a specified nonlinear law with a nonzero and detectable four-way response;
- direct or bounded source-phase latency;
- joined command, source, mixed-response, and detector-arrival lineage;
- complete attempt-level acquisition;
- separation from caustics, multiple intersections, and ordinary backgrounds;
- a target-independent finite-resolution control packet in the unknown arena;
- and no-refit transfer from multiple localized formed events to a held-out
  regional causal or conformal relation.

## 9. What changed

Before this swing, “form an interaction event” was one undivided open burden.
It now separates into three claims:

1. **Kinematic controllability — closed in the supplied flat arena.** One
   fixed four-front architecture algebraically addresses every event with
   continuous phases.
2. **Physical nonlinear formation — open but backed by serious theory.** A
   particular PDE, finite source implementation, nonzero interaction symbol,
   and detectable output remain to be fixed.
3. **Record-first regional transfer — still open.** Unknown geometry,
   finite-resolution controls, source calibration, complete lineage, and
   unchanged held-out transfer remain the North-Star burden.

This is genuine progress because future work should not redesign source
directions merely to solve a flat linear-algebra problem. It should spend its
effort on the physical nonlinear and no-refit interfaces that actually remain.

## 10. Strongest absorber and cheapest kills

### Strongest absorber

Ordinary wavefront/phased control absorbs the fixed-matrix event-addressing
mathematics. Nonlinear Lorentzian inverse theory absorbs the artificial
point-source concept and provides much stronger conditional reconstruction
results from supplied source-to-solution maps.

### Cheapest kills

- three phase channels leave an exact one-dimensional event fibre;
- a finite exact codebook reaches only finitely many events;
- unknown per-channel source latency gives a same-command/different-event
  witness;
- a front intersection without a nonzero nonlinear response is not a formed
  outgoing event;
- controls computed from the held-out geometry are interface refit; and
- a flat fixed matrix is not a uniform controller for an unknown curved
  metric class.

## 11. Claim ledger

| Claim | Status | Grade |
|---|---|---:|
| Four fixed null hyperplanes can be phase-shifted to meet uniquely at every Minkowski event | proved in the frozen model / standard | 3 |
| The architecture need not change event by event | proved in the frozen model | 3 |
| The phase-to-event map has smallest singular value \(\sqrt{(5-\sqrt{17})/2}\) | proved | 3 |
| Three scalar phase channels suffice for local event uniqueness in 3+1 dimensions | false | 4 |
| A finite exact control codebook covers a continuum event region | false | 4 |
| Finite phase precision gives a finite event-resolution bound | proved conditionally | 3 |
| A command record identifies the formed event with unknown source latency | false | 4 |
| Ideal front intersection proves nonlinear outgoing-event formation | false | 4 |
| The flat control transfers unchanged to unknown curved geometry | not shown | 0 |
| Continuous control variation is automatically interface refit | false | — |
| Target-geometry-coded source or decoder design is no-refit reconstruction | false | 4 |
| The source architecture, nonlinearity, latency, provenance, and acquisition are physically selected | not shown | 0 |
| Regional causal or conformal geometry transfers without refit | open | 0 |
| A novel physical prediction or finite remainder survives standard physics | not shown | 0 |

## 12. Highest-information reopener

The next dependency-changing question is:

> For one frozen semilinear Lorentzian PDE and one finite boundary source
> region, can a predeclared finite-resolution four-input control codebook
> produce at least one clean, associable, detectable higher-order interaction
> packet throughout a declared compact metric class, with source latency
> bounded independently and without using the held-out metric to refit the
> beams or decoder?

A positive would connect the flat formation control to a genuine finite
physical record interface. A negative should identify the smallest exact
failure:

- no uniform transverse interaction;
- caustic or multiple-intersection ambiguity;
- vanishing interaction symbol;
- source-latency confounding;
- insufficient finite codebook;
- incomplete context or attempt acquisition; or
- geometry-dependent control/decoder refit.

Only after that gate should the packet be composed with `HC-DU-107/108` and
tested against a held-out regional causal or conformal relation.

## 13. Repository disposition

- Bank `HC-DU-109` as a conditional Grade-3 fixed-architecture event-control
  result and scoped Grade-4 channel-rank, finite-control, latency, PDE, and
  no-refit necessity boundary.
- Preserve the exact nullness, determinant, spectrum, event recovery,
  three-channel fibre, finite-codebook count, and positive-latency witness in
  one proportional regression.
- Narrow the candidate class to a source-formed nonlinear interaction event
  from one fixed null-front architecture with a predeclared finite-resolution
  control codebook, independently bounded source timing, reciprocal
  self-calibrating detector crosslinks, complete provenance/acquisition, and
  no-refit regional geometry transfer.
- Keep Dynamic Unity quiescent with no selected successor.
- Do not create a paper, prediction, experiment, hardware path, or external
  action.

## Boundary

This is a scoped exact flat-space controllability and nonidentifiability
result. It is not a nonlinear PDE formation theorem, unknown-geometry
controllability theorem, physically selected source, formed record theorem,
full Lorentzian reconstruction, new law, empirical anomaly, prediction, or
ontological promotion.
