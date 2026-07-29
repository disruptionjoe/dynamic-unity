---
title: "Physical regularity-gap compactness and the geometric target-topology boundary"
status: completed_scoped_compactness_selection_boundary_and_conditional_finite_certificate_bridge
doc_type: physical_compactness_reduction_theorem_counterexamples_and_selection_boundary
created: 2026-07-28
work_id: CCR-PHYSICAL-REGULARITY-COMPACTNESS-GATE
claim_id: HC-DU-096
run_id: RUN-20260728-201348-physical-regularity-compactness-gate
lanes:
  - lane_1
  - lane_4
  - lane_6
  - lane_7
channels:
  - CH-FORMAL
  - CH-COLLIDE
  - CH-SYN
claim_grade: "GRADE 4 SCOPED SAME-TOPOLOGY ENERGY-BOUNDEDNESS/COMPACTNESS NONIMPLICATION, GEOMETRIC TARGET-DERIVATIVE BOUNDARY, AND REVERSIBLE-EVOLUTION TRANSPORT-NOT-SELECTION THEOREM; CONDITIONAL GRADE 3 COMPOSITION FROM PHYSICALLY WARRANTED HIGHER-REGULARITY/NONCOLLAPSE BOUNDS THROUGH WEAKER-TARGET COMPACTNESS TO HC-DU-095 FINITE CERTIFICATION; RELLICH, SOBOLEV, HYPERBOLIC PDE, AND LORENTZIAN COMPACTNESS THEORY ABSORB THE COMPONENTS; NO PHYSICALLY SELECTED CLASS, GAUGE, TOPOLOGY, TIME ANCHOR, PROBE PACKET, COMPLETE ACQUISITION, NEW PHYSICS, GRADE-5 REMAINDER, PREDICTION, OR PAPER PROMOTION"
decision: PHYSICAL_BOUNDS_CAN_CONDITIONALLY_SUPPLY_THE_COMPACTNESS_TOPOLOGY_BUT_REVERSIBLE_DYNAMICS_DOES_NOT_SELECT_THE_CLASS
---

# Physical regularity-gap compactness gate

## Executive result

`HC-DU-095` left one premise conspicuously open: a compact physical
completion class. This swing determines exactly how ordinary field-theory
regularity can and cannot supply it.

The positive route is real but conditional:

> On a fixed compact domain and in a fixed gauge, a uniformly bounded
> \(H^s\) class is precompact in every weaker \(H^{s'}\) topology with
> \(s'<s\), and it is precompact in \(C^k\) when
> \(s>k+d/2\). If physical admissibility is closed in that weaker topology
> and the held-out target and readouts are continuous there, the resulting
> compact class can be passed unchanged into `HC-DU-095`.

The composition then gives a finite robust target-resolution certificate,
provided a physically realizable target-separating probe family and complete
joint acquisition also exist.

The negative boundary is equally exact:

- a bounded ball is not compact in its own infinite-dimensional energy norm;
- weak or lower-regularity convergence does not control a target requiring
  derivatives discarded by that topology;
- causal or conformal structure can remain fixed while curvature oscillates;
- compact causal diamonds inside each spacetime do not make a family of
  spacetimes compact; and
- reversible hyperbolic evolution transports compactness of an initial-data
  class but does not create or select it.

This means the active-wave route is not blocked by an impossible compactness
requirement. It is blocked by a more physical and more discriminating packet:

```text
independently warranted domain / topology / gauge
  + uniform higher-regularity and noncollapse bounds
  + closure in the target topology
  -> compact physical completion class

compact class
  + target-continuous, physically realizable separating probes
  + joint complete acquisition below the separation margin
  -> finite robust target-resolution certificate.
```

No audited arena currently selects that whole packet. The result therefore
refines the reopener without selecting a successor.

Returned states:

```text
REGULARITY_GAP_PRECOMPACTNESS
+ SAME_NORM_ENERGY_BALL_NONCOMPACT
+ TARGET_DERIVATIVE_TOPOLOGY_LADDER
+ CAUSAL_STRUCTURE_WITHOUT_CURVATURE_CONTROL
+ EVOLUTION_TRANSPORTS_NOT_SELECTS_COMPACTNESS
+ NONCOLLAPSE_AND_GAUGE_CONTROLS_REQUIRED
+ FINITE_CERTIFICATE_CONDITIONAL
+ PHYSICAL_CLASS_SELECTION_STILL_OPEN
+ NO_READY_SUCCESSOR
```

## 1. Frozen contract

Let \(D\) be a compact \(d\)-dimensional smooth domain or finite causal slab
on a fixed manifold. After fixing a bundle trivialization or gauge, let

\[
\Theta\subset H^s(D;E)
\]

be a class of metric and matter fields in a fixed finite-rank bundle \(E\).
Let \(T\) be a held-out physical target and let \(\mathcal M\) be the frozen
physical measurement family from `HC-DU-095`.

There are four distinct topologies:

1. the **control topology**, such as \(H^s\), in which an energy estimate is
   available;
2. the **compactness topology**, such as \(H^{s'}\) or \(C^k\), in which a
   bounded sequence has a convergent subsequence;
3. the **target topology**, the weakest topology in which \(T\) is
   continuous; and
4. the **measurement topology**, in which each admitted readout is
   continuous.

The compactness topology is useful only if it is at least as strong as both
the target and measurement topologies.

The following are also different:

- one causal diamond being compact;
- one spacetime region having compact closure;
- a set of fields on a fixed region being compact;
- a moduli class of spacetimes being compact after diffeomorphism quotient;
- and a physical law selecting which class is admissible.

Conflating any pair silently supplies the premise that must be proved.

## 2. The regularity-gap theorem

### Theorem

Let \(D\) be compact and let \(\Theta\subset H^s(D;E)\) be uniformly bounded.
Then:

1. for every \(s'<s\), \(\Theta\) is relatively compact in \(H^{s'}\);
2. if \(s>k+d/2\), \(\Theta\) is relatively compact in \(C^k\); and
3. if \(\Theta\) is closed in the chosen weaker topology—or if physical
   admissibility and all targets/readouts extend to its closure—then its
   closure in that topology is a valid compact class for the theorem in
   `HC-DU-095`.

### Proof

Rellich compactness gives a compact inclusion

\[
H^s(D;E)\hookrightarrow H^{s'}(D;E)
\qquad(s'<s).
\]

Hence every uniformly \(H^s\)-bounded sequence has an
\(H^{s'}\)-convergent subsequence.

If \(s>k+d/2\), choose \(t\) with

\[
k+\frac d2<t<s.
\]

Rellich gives compact inclusion \(H^s\hookrightarrow H^t\), while Sobolev
embedding gives continuous inclusion \(H^t\hookrightarrow C^k\). Their
composition is compact. The final statement is the definition of compactness
of the weaker closure. \(\square\)

### Closure is not clerical

A class can be closed in \(H^s\) but not in \(H^{s'}\). Its weaker closure
may introduce limits that lose:

- Lorentzian signature;
- constraint satisfaction;
- a positive volume radius;
- boundary conditions;
- source support;
- matter positivity;
- global hyperbolicity; or
- the declared observer/access interface.

The physical class must therefore be shown closed under the convergence being
used, or the target and measurements must be defined on a larger,
independently justified completion. Otherwise “take the compact closure” is
completion enlargement, not physical selection.

## 3. Geometric target derivative ladder

For fields on a four-dimensional compact domain, a uniform \(H^s\) bound
gives the following clean sufficient ladder:

| Held-out object | Local coefficient dependence | Sufficient regularity for \(C^k\)-precompactness in \(d=4\) |
|---|---|---|
| metric coefficients and pointwise cone field | \(g\) | \(s>2\) for \(C^0\) |
| connection coefficients and finite-time geodesic ODE | \(g,\partial g\) | \(s>3\) for \(C^1\) |
| Riemann/Ricci/scalar curvature | \(g,\partial g,\partial^2g\) | \(s>4\) for \(C^2\) |

This is a sufficient Sobolev route, not a claim of sharpness. Global causal
order needs additional causal stability, boundary, and nondegeneracy
conditions. A uniform cone margin is needed because the set of Lorentzian
metrics is open, not closed, inside all symmetric tensors.

The ladder matters because Dynamic Unity's target cannot be named merely as
“geometry.” A completion class can be compact enough for causal or conformal
targets and too weak for curvature or full metric targets.

## 4. Exact counterexample I — energy boundedness is not compactness

On the circle, let

\[
u_n(x)
=
(1+n^2)^{-s/2}e^{inx}.
\]

Then

\[
\|u_n\|_{H^s}=1.
\]

For distinct \(m,n\), orthogonality gives

\[
\|u_n-u_m\|_{H^s}=\sqrt2.
\]

Thus the bounded sequence has no strongly convergent \(H^s\) subsequence.
However, for every \(s'<s\),

\[
\|u_n\|_{H^{s'}}
=
(1+n^2)^{(s'-s)/2}
\longrightarrow0.
\]

The same sequence is therefore:

```text
bounded but noncompact in the energy topology
precompact in every strictly weaker Sobolev topology.
```

This is the smallest exact reason an energy estimate alone does not discharge
`HC-DU-095`.

## 5. Exact counterexample II — causal agreement without curvature control

Let \(\eta\) be a flat Lorentzian metric on a compact coordinate slab and let
\(x\) be one periodic spatial coordinate. Define

\[
\phi_n(x)=n^{-2}\sin(nx),
\qquad
g_n=e^{2\phi_n}\eta.
\]

Then:

1. \(\{\phi_n\}\) is uniformly bounded in \(H^2\);
2. \(\phi_n\to0\) in \(C^1\), so \(g_n\to\eta\) in \(C^1\);
3. every \(g_n\) has exactly the same pointwise causal cones as \(\eta\),
   because a positive conformal factor does not change null directions; but
4. \(\partial_x^2\phi_n=-\sin(nx)\) has no strongly convergent \(L^2\)
   subsequence.

In dimension \(d\geq3\), conformal scalar curvature obeys

\[
R(e^{2\phi}\eta)
=
e^{-2\phi}
\left[
-2(d-1)\Box_\eta\phi
-(d-1)(d-2)|\nabla\phi|_\eta^2
\right].
\]

The curvature of \(g_n\) therefore retains an order-one oscillatory term even
though the metrics converge in \(C^1\) and their causal cones agree exactly.

This proves a sharp target warning:

> Compactness sufficient for causal or connection-level targets need not be
> sufficient for curvature. The omitted derivatives can carry the entire
> remainder.

The example does not show that causal records fail to reconstruct causal
geometry; all members deliberately share it. It shows that such a success
cannot be promoted to full physical geometry.

## 6. Reversible evolution transports compactness; it does not create it

### Proposition

Let \(X\) be a topological state space and let

\[
\Phi_t:U_t\rightarrow V_t
\]

be a homeomorphism supplied by a reversible, well-posed evolution at fixed
time \(t\). For every \(K\subset U_t\),

\[
K\text{ is compact}
\quad\Longleftrightarrow\quad
\Phi_t(K)\text{ is compact}.
\]

### Proof

A continuous image of a compact set is compact. The reverse implication
follows by applying the continuous inverse \(\Phi_t^{-1}\). \(\square\)

For an entire finite trajectory interval, suppose

\[
\Psi:K\rightarrow C([0,T],X)
\]

is continuous and evaluation at \(t=0\) returns the initial datum. Then
compactness of \(K\) implies compactness of the trajectory family
\(\Psi(K)\); conversely, compactness of the trajectory family implies
compactness of \(K\) by continuous evaluation at zero.

Therefore a reversible hyperbolic law can:

- propagate a regularity bound;
- give a uniform existence interval;
- continuously transport a compact initial-data class; and
- preserve constraints.

It does not by those facts:

- make a bounded infinite-dimensional energy ball compact;
- choose the initial-data class;
- choose topology, gauge, boundary or sources;
- choose the target topology; or
- choose the measurement/archive interface.

Dissipative or parabolic dynamics can compactify bounded sets for positive
time. That is a genuine alternate route, but it requires a physically
selected smoothing semigroup and does not describe ordinary reversible
Lorentzian hyperbolic evolution. It must be tested as new structure, not
silently attributed to “dynamics.”

## 7. Primary-source collision

The physical literature supports the boundary rather than closing it.

### Einstein energy estimates

Klainerman, Rodnianski, and Szeftel prove that the existence time of a
classical vacuum Einstein solution can be controlled by an \(L^2\) curvature
bound **and a lower volume-radius bound**. Their result also ties the
\(L^2\) curvature threshold to causal-boundary injectivity
([primary source](https://arxiv.org/abs/1204.1767)).

Czimek's localized theorem makes the supplied packet even more explicit:
on a compact spacelike hypersurface with boundary, the existence interval
depends on Ricci-curvature, boundary second-fundamental-form,
second-fundamental-form \(H^1\), and lower volume-radius bounds
([primary source](https://arxiv.org/abs/1807.08306)).

These are powerful physical regularity results. They establish a controlled
existence interval. They do not say that the admitted initial-data class is
compact in the topology of every desired target, nor that Einstein dynamics
selects that class.

### Lorentzian convergence needs typed anchors

Noldus constructs a Lorentzian Gromov--Hausdorff distance on isometry classes
of compact globally hyperbolic spacetimes with boundary
([primary source](https://arxiv.org/abs/gr-qc/0308074)). A metric on a moduli
space is not a theorem that the whole moduli space is compact.

Sormani and Vega show that null distance is built from a supplied time
function; definiteness requires an anti-Lipschitz condition, and recovery of
causal structure uses both the null distance and time function
([primary source](https://arxiv.org/abs/1508.00531)).

Burgos, Flores, and Sánchez explain why Lorentzian Cheeger--Gromov
convergence must be anchored by a timelike direction and use Cauchy temporal
functions to bring Riemannian compactness machinery into the globally
hyperbolic setting
([primary source](https://arxiv.org/abs/2508.15441)).

This is not a flaw in those theories. It is exactly the typing DU needs:
Lorentzian compactness is not a free coordinate-independent ball. Temporal
anchors, causal nondegeneracy, gauge/isometry handling, and geometric bounds
are part of the convergence contract.

## 8. Composition with `HC-DU-095`

Let \(\overline\Theta^\tau\) be the closure of the physically admitted class
in a compactness topology \(\tau\). Assume:

1. a physical theory independently warrants the domain, topology, gauge,
   boundary/source class, regularity bound, noncollapse bound, and finite
   evolution interval;
2. \(\overline\Theta^\tau\) contains only admitted physical completions;
3. the held-out target \(T\) is continuous in \(\tau\);
4. every admitted measurement is continuous in \(\tau\);
5. the full physically realizable family separates all completion pairs
   whose target distance is at least \(\delta\); and
6. the selected finite subfamily is jointly executable and completely
   acquired with error below half its uniform margin.

Then `HC-DU-095` gives a finite robust record whose completion fibre has
target diameter below \(\delta\).

The scientific burden has therefore moved from vague continuum pessimism to
six explicit interfaces. The first two are now mathematically tractable; the
last four remain arena-specific physical work.

## 9. Grade, implications, and reopener

### Earned

- **Scoped Grade 4:** boundedness in an infinite-dimensional energy topology
  does not imply compactness there; reversible well-posed evolution preserves
  rather than creates compactness; and target continuity determines how much
  of a regularity gap is usable.
- **Scoped Grade 4:** exact conformal metrics can share causal structure and
  converge in \(C^1\) while their curvature fails to converge.
- **Conditional Grade 3:** independently warranted uniform higher regularity
  on a fixed compact, noncollapsed, gauge-controlled class can supply the
  compact target topology needed by `HC-DU-095`.

### Absorbed

The mathematical components are standard Rellich/Sobolev compactness,
geometric convergence, hyperbolic well-posedness, and experimental-design
logic. The result is valuable to Dynamic Unity as a typed composition and
scope theorem, not as new analysis or new physics.

### Not earned

- a physical law that selects the required class;
- compactness of a natural Lorentzian moduli class;
- a canonical gauge or temporal anchor;
- a physically formed finite source/response packet;
- complete attempted-process acquisition;
- no-refit held-out transfer;
- a physical remainder, prediction, or new law; or
- a ready successor.

### Exact reopener

Reopen the active-wave route only when one physical arena supplies, before
target revelation:

1. a fixed observer region and physical completion class;
2. gauge/quotient, Lorentzian margin, noncollapse, and target-topology
   controls;
3. a proved compactness or total-boundedness theorem in that target topology;
4. a bounded jointly realizable target-separating probe family;
5. a constructive positive margin and resource bound; and
6. complete joined acquisition with no-refit held-out transfer.

Absent that packet, another local Fourier model or another generic energy
estimate repeats this result.
