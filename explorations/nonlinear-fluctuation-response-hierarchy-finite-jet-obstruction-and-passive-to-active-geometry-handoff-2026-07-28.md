---
title: "Nonlinear fluctuation-response hierarchy, finite-jet obstruction, and passive-to-active geometry handoff"
date: 2026-07-28
status: banked_scoped_result
claim_id: HC-DU-100
work_id: CCR-NONLINEAR-PASSIVE-RESPONSE-HIERARCHY-GATE
run_id: RUN-20260728-214629-nonlinear-passive-response-hierarchy-gate
lanes:
  - lane_1
  - lane_3
  - lane_4
  - lane_6
  - lane_7
channels:
  - CH-FORMAL
  - CH-COLLIDE
  - CH-SYN
maximum_grade: "Grade 4 scoped finite-response-jet nonidentifiability; conditional Grade 3 finite-resolution reconstruction under a physically warranted analytic-tail and record contract"
---

# Nonlinear fluctuation-response hierarchy, finite-jet obstruction, and passive-to-active geometry handoff

## Executive result

The swing returned:

```text
PASSIVE_LINEAR_IMAGING_RECOVERS_ONLY_ITS_TYPED_GEOMETRY
+ NONLINEAR_RESPONSE_REQUIRES_A_HIGHER_CORRELATION_HIERARCHY
+ FINITE_RESPONSE_JET_DOES_NOT_IDENTIFY_NONLINEAR_RESPONSE
+ UNIFORM_ANALYTIC_TAIL_GIVES_A_FINITE_RESOLUTION_BRIDGE
+ THEORETICAL_CORRELATION_IS_NOT_A_FORMED_RECORD
+ PHYSICAL_INTERFACE_AND_ACQUISITION_STILL_SUPPLIED
+ NO_READY_SUCCESSOR
```

The most important correction is that Dynamic Unity's active and passive
reconstruction routes do not yet meet at one response object.

The strongest passive-imaging theorem audited here is already substantial:
one realization of a stipulated white-noise-driven **linear** wave field,
observed for unbounded time on an open region, determines a time-independent
**Riemannian** manifold up to isometry under the theorem's hypotheses.

The strongest Lorentzian result used by Dynamic Unity is different. It
reconstructs the conformal structure of spacetime from a local
source-to-solution map for a **nonlinear** hyperbolic equation. The nonlinear
interaction of waves is load-bearing. Even the single-timelike-curve version
still requires sources arranged in an open tubular neighborhood.

Linear FDT therefore does not hand the passive branch the response operator
used by the Lorentzian theorem. A nonlinear fluctuation-response hierarchy is
needed.

That hierarchy has an exact finite ceiling:

> No fixed finite response jet determines a general analytic nonlinear
> response map.

For any retained order \(N\),

\[
L_0(s)=s,
\qquad
L_c(s)=s+c\,s^{N+1}
\]

have identical derivatives through order \(N\) at zero and different
responses at every nonzero held-out source amplitude. Both maps are entire.
Analyticity alone does not repair the failure.

There is also an exact constructive bridge. If physics supplies a common
analytic radius \(R\) and coefficient bound

\[
\|A_n\|\leq M R^{-n}
\]

for the response maps, then on sources of norm at most \(r<R\), the omitted
tail after order \(N\) is at most

\[
\varepsilon_N
\leq
M\frac{(r/R)^{N+1}}{1-r/R}.
\]

A held-out target margin larger than twice the response-estimation error plus
twice this tail makes a finite hierarchy sufficient at that declared
resolution.

This is the clean answer:

> Passive nonlinear reconstruction is mathematically coherent, but a finite
> passive record becomes sufficient only after a physical arena supplies a
> response-complete correlation hierarchy, a common analytic tail bound, a
> measurement instrument, mixing, calibration, and complete acquisition.

No audited arena presently supplies that entire packet. Dynamic Unity remains
quiescent.

## 1. Frozen typed contract

Let:

- \(F\) be a Banach space of local source functions;
- \(Y\) be a Banach readout space;
- \(B_R(0)\subset F\) be a source ball;
- \(L:B_R(0)\to Y\) be the local source-to-solution map;
- \(D^nL(0)\) be its \(n\)-th Fréchet derivative;
- \(\mathcal C_n\) be a declared equilibrium \(n\)-time correlation object;
- \(\mathcal I_n\) be the physical instrument used to estimate that object;
- \(J_N(L)=(L(0),DL(0),\ldots,D^NL(0))\) be the response jet through
  order \(N\);
- \(R_N\) be the retained record from which that jet is claimed to be
  reconstructed;
- \(T(L)\) be a held-out causal or conformal target; and
- \(\mathfrak B\) be the resource contract: duration, bandwidth, source and
  force calibration, detector precision, repetitions, retained memory,
  attempt lineage, and target tolerance.

These are different types:

```text
equilibrium operator correlation
!= sequential measurement distribution
!= retained observer record
!= response tensor
!= complete source-to-solution operator
!= geometric target.
```

The task is a disclosure/reconstruction task under a frozen dynamics. It
does not test source issuance.

## 2. Four response objects that had been compressed into one

The previous route used the word "response" across four distinct theorem
contracts.

| Object | What it contains | What it can conditionally recover | What remains supplied |
|---|---|---|---|
| Linear equilibrium susceptibility | First derivative of a response at zero forcing | Linear response or a Green function after FDT/KMS and calibration | State, temperature, observable, conjugate force, detector |
| Passive white-noise covariance | Correlations of a linear stochastic wave driven by a specified source law | A local linear source-to-solution map and Riemannian metric in the imported theorem | White-noise statistics, source envelope, observation open set, infinite-time limit |
| Nonlinear response hierarchy | Higher derivatives of the response map | A local analytic response operator when the entire hierarchy and convergence control are known | Perturbation fields, correlation ordering, analytic radius, measurement protocol |
| Nonlinear Lorentzian source-to-solution map | Counterfactual output for a rich family of local sources | Topological/differentiable/conformal spacetime structure in the theorem's causal domain | Field equation, source neighborhood, continuum source family, ideal readout, regularity |

The active/passive handoff is valid only after typed maps connect all four
rows.

## 3. Primary-source collision

### 3.1 Linear passive imaging is a real positive

Helin, Lassas, Oksanen, and Saksala study

\[
\partial_t^2u-\Delta_gu=\chi W
\]

on \(\mathbb R^{1+n}\), where \(W\) is Gaussian spacetime white noise and
\(\chi\) is a smooth source envelope. Their empirical correlations are

\[
C_T(t_1,x_1,t_2,x_2)
=
\frac1T\int_0^T
u(t_1+s,x_1)u(t_2+s,x_2)\,ds.
\]

Under nontrapping and asymptotically Euclidean hypotheses, the
\(T\to\infty\) correlation data from one noise realization determine the
Riemannian manifold up to isometry
([primary source](https://arxiv.org/abs/1609.08022)).

The proof matters to Dynamic Unity because the correlations recover a local
linear source-to-solution operator. Random excitation multiplexes a continuum
of linear probes into one stochastic field realization.

The theorem does **not** say:

- that the white-noise law is selected by the medium;
- that white noise has finite energy or bandwidth;
- that a bounded observer has the \(T\to\infty\) distribution-valued record;
- that the observation open set is selected;
- that a detector and complete attempt lineage are formed;
- that Lorentzian causal order is reconstructed; or
- that the source law is an equilibrium fluctuation law.

It is a strong imported reconstruction theorem inside a heavily typed ideal
arena, not a physical record-interface selector.

### 3.2 Lorentzian conformal reconstruction uses nonlinearity

Kurylev, Lassas, and Uhlmann distinguish a passive light-observation-set
problem from an active nonlinear-wave inverse problem. For the active problem,
a local source-to-solution operator for a semilinear wave equation determines
the topological, differentiable, and conformal structure of the causally
accessible spacetime region in four dimensions
([primary source](https://arxiv.org/abs/1405.3386)).

Lassas, Uhlmann, and Wang extend this semilinear program and recover
coefficients of the nonlinearity within their theorem class
([primary source](https://arxiv.org/abs/1606.06261)).

Nursultanov, Oksanen, and Tzou reduce the observation locus to one timelike
curve, but explicitly retain sources in an open tubular neighborhood and use
microlocal nonlinear-wave interaction
([primary source](https://arxiv.org/abs/2310.06925)).

Therefore:

```text
one observation curve
!= one source
!= one response coefficient
!= one finite record.
```

The known Lorentzian positive cannot be inherited from a two-point linear
FDT alone.

### 3.3 Nonlinear fluctuation-response theory supplies a possible bridge

Lucarini and Colangeli formulate response at each nonlinear order for systems
with a smooth invariant measure. Near equilibrium, the \(n\)-th order
susceptibility is related to suitably constructed correlations of \(n+1\)
observables, with variable changes, algebraic combinations, and multiple
convolutions
([primary source](https://arxiv.org/abs/1202.1073)).

This establishes a serious conditional bridge:

```text
selected invariant state and perturbation field
+ correctly ordered correlation hierarchy
+ nonlinear fluctuation-response identities
-> nonlinear response tensors.
```

It does not select the invariant state, perturbation field, observable,
instrument, or finite record.

The quantum case makes the typing stricter. Tsuji, Shitara, and Ueda derive a
generalized FDT for a particular class of bipartite out-of-time-order
correlators and show that the difference from physical OTOCs is measured by
Wigner--Yanase skew information
([primary source](https://arxiv.org/abs/1612.08781)).

The lesson is not that OTOCs solve the interface. It is that "the higher
correlation" is not one untyped object. Ordering, statistical average,
time-reversal operation, and measurement protocol matter.

### 3.4 Multi-time operator data are not automatically one passive record

A theoretical Kubo response tensor contains step functions and nested
commutators. Algebraically, a complete family of the required ordered
operator correlations can determine those nested commutators.

A classical output time series does not automatically provide those
noncommuting orderings. Sequential quantum outcome probabilities are
generated by instruments; the interventions alter the later state.

Process-tensor work treats multi-time processes operationally through the
interventions placed at the time slots rather than by identifying one
reduced-state history with the process
([primary source](https://arxiv.org/abs/1801.09811)).

Recent work on sequential statistics makes the same boundary explicit:
multi-time memory can be intrinsically protocol dependent even when lower
order statistics remain compatible with a quantum-regression description
([primary source](https://arxiv.org/abs/2605.06427)).

Thus:

```text
theoretical n-point function
+ a claim that it is measurable
```

is not yet:

```text
formed instrument
+ joined attempt-level outcomes
+ retained certified record.
```

## 4. Exact finite-response-jet obstruction

### Proposition 1 — finite response jets do not identify analytic maps

Let \(N\geq1\), let \(c\neq0\), and define entire scalar response maps

\[
L_0(s)=s,
\qquad
L_c(s)=s+c\,s^{N+1}.
\tag{1}
\]

Then:

\[
L_0^{(j)}(0)=L_c^{(j)}(0)
\quad
\text{for every }0\leq j\leq N,
\tag{2}
\]

while

\[
L_c(s_\star)-L_0(s_\star)
=c\,s_\star^{N+1}\neq0
\tag{3}
\]

for every nonzero \(s_\star\).

#### Proof

The added monomial has a zero of order \(N+1\) at the origin, so all its
derivatives through order \(N\) vanish there. At a nonzero source it does not
vanish. Both maps are polynomials and therefore entire. \(\square\)

### Banach-space form

Let \(F,Y\) be Banach spaces, choose nonzero
\(\lambda\in F^\ast\) and \(y\in Y\), and add

\[
\Delta L(f)=\lambda(f)^{N+1}y.
\tag{4}
\]

Every Fréchet derivative of \(\Delta L\) through order \(N\) vanishes at
zero, while \(\Delta L(f_\star)\neq0\) whenever
\(\lambda(f_\star)\neq0\).

The obstruction is not a one-dimensional artifact.

### Corollary 1 — any finite hierarchy needs a tail premise

Suppose a retained passive record \(R_N\) determines at most the response jet
\(J_N(L)\). If the held-out target varies between (1)'s two maps, then

\[
T\not\!\!\downarrow R_N.
\]

No reconstruction rule from that fixed finite hierarchy can be correct on
both completions.

The conclusion survives the assumption "the response is analytic." A common
radius and quantitative tail control are additional premises.

### Executable exact control

`tests/du_nonlinear_passive_response_hierarchy_probe.py` checks eight
finite-jet pairs with exact rational arithmetic. In every case:

- all retained derivatives agree;
- the first omitted derivative differs; and
- the held-out response at \(s=1/2\) differs.

No stochastic simulation is used.

## 5. Conditional finite analytic bridge

### Proposition 2 — uniform analytic tail certificate

Let

\[
L(f)=\sum_{n=0}^{\infty}A_n[f^{\otimes n}]
\tag{5}
\]

be analytic on \(B_R(0)\), and assume the common bound

\[
\|A_n\|\leq M R^{-n}.
\tag{6}
\]

For \(\|f\|\leq r<R\), let

\[
L_N(f)=\sum_{n=0}^{N}A_n[f^{\otimes n}].
\tag{7}
\]

Then

\[
\begin{aligned}
\|L(f)-L_N(f)\|
&\leq
\sum_{n=N+1}^{\infty}\|A_n\|\,\|f\|^n\\
&\leq
M\sum_{n=N+1}^{\infty}(r/R)^n\\
&=
M\frac{(r/R)^{N+1}}{1-r/R}.
\end{aligned}
\tag{8}
\]

This is sharp for the scalar geometric series with
\(A_n=MR^{-n}\).

The executable control checks the sharp bound through order eight. With

\[
M=1,\qquad R=2,\qquad r=1,\qquad \delta=10^{-2},
\]

order seven is the first to make the tail at most \(\delta\):

\[
\varepsilon_6=\frac1{64}>10^{-2},
\qquad
\varepsilon_7=\frac1{128}<10^{-2}.
\]

### Corollary 2 — target-relative finite response order

Let different target classes have a response separation margin
\(\Delta>0\) on the declared source set. Let \(\eta_N\) bound the error in
estimating the retained response jet from the finite passive record, and let
\(\varepsilon_N\) be (8).

If

\[
\Delta>2(\eta_N+\varepsilon_N),
\tag{9}
\]

then the retained hierarchy distinguishes the target classes at that
resolution.

This is the nonlinear-response analogue of the compactness and finite-packet
results in `HC-DU-095--098`.

It is conditional on:

- a common physical response class;
- a common \(R\) and \(M\);
- a record that estimates every required response tensor through order \(N\);
- a uniform finite-time error \(\eta_N\);
- a target margin \(\Delta\) proved before evaluation; and
- no refit of the state, source law, instrument, or analytic class.

### What the theorem does not do

It does not derive:

- analyticity of a relativistic interacting field response;
- a radius uniform across physical completions;
- a useful coefficient bound;
- response completeness of passive correlations;
- a nondisturbing quantum measurement hierarchy;
- mixing at all required orders;
- finite detector bandwidth;
- a source/force calibration;
- a geometric inverse-stability margin; or
- complete acquisition.

The bound is the exact mathematical seam, not the missing physical engine.

## 6. Why the two existing positives do not compose unchanged

### Passive linear Riemannian branch

```text
specified Gaussian white-noise source
+ linear wave equation on a time-independent medium
+ open observation region
+ one infinite-duration distribution-valued realization
-> empirical covariance
-> local linear source-to-solution map
-> Riemannian metric up to isometry.
```

This branch already works mathematically. Its principal Dynamic Unity debts
are physical source/interface selection and bounded acquisition. Its target
is spatial Riemannian geometry, not Lorentzian causal/conformal spacetime.

### Nonlinear active Lorentzian branch

```text
specified semilinear hyperbolic equation
+ rich local source family
+ ideal source-to-solution map
+ nonlinear wave interaction
-> light observation structure
-> Lorentzian conformal geometry in the accessible domain.
```

This branch already works mathematically. Its principal Dynamic Unity debts
are the active continuum capability surface, finite packet, interface
formation, and acquisition.

### Proposed nonlinear passive bridge

```text
physically selected stationary interacting arena
+ response-complete multi-time correlation hierarchy
+ nonlinear fluctuation-response identities
+ selected instrument and calibration
+ uniform finite-time mixing
-> finite estimates of a response jet

uniform analytic radius and coefficient bound
+ held-out target margin
-> finite-resolution nonlinear response operator

inverse-geometric stability theorem
-> causal or conformal target.
```

Every arrow is mathematically intelligible. Several are not physically
selected or proved in one arena.

## 7. The smallest remaining mismatch

The first mismatch is not "infinite data" in the abstract. It is:

> The Lorentzian inverse theorem needs a nonlinear counterfactual capability
> surface, while the physically endogenous passive route has so far earned
> only a calibrated linear response relation.

A higher passive hierarchy can close that mismatch only if it is:

1. response-complete for the perturbation actually used by the inverse
   theorem;
2. operationally measurable by a frozen instrument family;
3. finite at the target resolution through a uniform analytic tail;
4. uniformly estimable in finite time;
5. physically realizable at bounded bandwidth and energy; and
6. retained with complete attempt lineage.

This is narrower and more actionable than looking for "a physical
covariance."

## 8. Arena comparison after the gate

| Arena | Strongest earned positive | Missing load-bearing piece | Disposition |
|---|---|---|---|
| White-noise passive spatial imaging | One ideal stochastic realization determines a Riemannian manifold | Physical source law, finite-energy/bandwidth, finite duration, selected detector | Keep as exact positive control |
| Equilibrium linear FDT/KMS | Correlation determines calibrated retarded linear response | State/phase, interface, thermal gauge, nonlinear response | Keep as first rung |
| Classical nonlinear fluctuation-response | \(n+1\)-point correlations can encode \(n\)-th response under smooth invariant-measure assumptions | Physical arena, finite hierarchy, analytic tail, measurement/acquisition | Best mathematical bridge |
| Quantum nonlinear/OTO response | Selected ordered correlators constrain selected nonlinear responses | Ordering-specific instrument, disturbance, process memory, state/interface | High-value hostile case |
| Active semilinear Lorentzian waves | Rich local response operator reconstructs conformal spacetime | Physical/finite capability surface and formed record | Keep as target theorem |

No row by itself satisfies Dynamic Unity's full typed ladder.

## 9. What changed

### Before

The active and passive options appeared to differ mainly in who supplied the
source:

```text
designed stochastic source
versus
endogenous equilibrium fluctuation.
```

### After

There are two independent differences:

```text
source provenance
and
response order.
```

Replacing an active source with passive equilibrium noise may remove source
design at linear order while still failing to supply the nonlinear response
information that the Lorentzian geometry theorem uses.

This changes the successor contract from:

```text
physically selected covariance + finite response gap
```

to:

```text
physically selected response-complete hierarchy
+ uniform analytic tail
+ finite target margin
+ formed instrument and complete acquisition.
```

It also separates two legitimate research branches:

- **lower ceiling / closer:** finite passive reconstruction of a spatial
  Riemannian medium under a physically improved noise and acquisition model;
- **higher ceiling / farther:** nonlinear passive reconstruction of
  Lorentzian causal or conformal structure.

## 10. Grade, absorption, and disposition

### Earned

- **Scoped Grade 4:** no finite response jet identifies a general analytic
  nonlinear response map.
- **Scoped Grade 4:** a two-point linear FDT does not supply the nonlinear
  source-to-solution operator used by the audited Lorentzian inverse theorem.
- **Scoped Grade 4 typing boundary:** a theoretical higher-order correlation
  object is not automatically one passive formed observer record.
- **Conditional Grade 3:** a physically warranted common analytic radius and
  coefficient bound turn a finite response jet into an explicit
  finite-resolution response certificate.
- **Conditional Grade 3:** composing that bound with a target margin gives a
  finite response order sufficient for the declared target resolution.

### Imported positives

- one-realization white-noise passive reconstruction of a Riemannian metric
  in the Helin--Lassas--Oksanen--Saksala arena;
- nonlinear Lorentzian conformal reconstruction from local
  source-to-solution maps;
- nonlinear fluctuation-response relations under declared invariant-measure
  and perturbation assumptions; and
- operational multi-time instrument/process typing.

### Absorbed

The component mathematics is absorbed by:

- analytic Taylor jets and Cauchy/geometric tail estimates;
- Kubo/Ruelle nonlinear response;
- generalized fluctuation-dissipation relations;
- stochastic passive imaging;
- nonlinear hyperbolic inverse problems; and
- process tensors and sequential quantum measurement.

Dynamic Unity's contribution is the typed composition, exact finite-jet
obstruction, and the new response-order dependency in the physical
reconstruction ladder. No new theorem in those source fields is claimed.

### Not earned

- a physically selected stationary interacting field arena;
- a response-complete passive correlation hierarchy;
- a selected multi-time quantum instrument;
- a uniform physical analytic radius or coefficient bound;
- finite-time high-order mixing and concentration;
- finite Lorentzian geometric reconstruction;
- complete attempted-process acquisition;
- no-refit second-arena transfer;
- a Grade-5 physical remainder or prediction;
- paper promotion; or
- a ready scientific successor.

### Exact reopener

Reopen the high-ceiling nonlinear passive route only when one serious physical
arena supplies, before held-out evaluation:

1. a selected stationary or equilibrium completion class;
2. a physically justified source/perturbation and state law;
3. a response-complete correlation hierarchy through a declared order \(N\);
4. an operational instrument that estimates the required correlation
   orderings;
5. a common analytic radius and coefficient bound;
6. a target-distinct inverse-geometric margin;
7. uniform finite-time mixing/concentration for every retained order;
8. bounded duration, bandwidth, energy, precision, quantization, memory, and
   complete attempt acquisition; and
9. no-refit transfer to a held-out causal or conformal target.

The lower-ceiling Riemannian passive branch may reopen earlier if a physical
finite-energy source and finite-duration stability theorem replace the ideal
white-noise/infinite-time contract. That would be useful calibration work but
would not by itself reach the Lorentzian North-Star target.

## Resource disposition

The exact polynomial counterexample, analytic bound, and primary-source
theorem collision decide this gate locally. No external hardware is relevant.
A stochastic or PDE simulation would merely illustrate already proved
relations and would not close the physical selection, high-order instrument,
analytic-tail, or acquisition gaps.
