---
title: "Bounded KMS response: factorial tail, thermodynamic scaling, and record-interface boundary"
date: 2026-07-28
status: banked_scoped_result
claim_id: HC-DU-101
work_id: CCR-BOUNDED-KMS-LOCAL-RESPONSE-TAIL-GATE
run_id: RUN-20260728-220339-bounded-kms-local-response-tail-gate
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
maximum_grade: "Grade 4 scoped bounded-response theorem and scale/typing boundary; conditional Grade 3 finite-resolution local-response reconstruction"
---

# Bounded KMS response: factorial tail, thermodynamic scaling, and record-interface boundary

## Executive result

The swing returned:

```text
BOUNDED_FINITE_TIME_DYNAMICS_SUPPLIES_FACTORIAL_RESPONSE_TAIL
+ KMS_RELATES_COEFFICIENTS_BUT_DOES_NOT_CREATE_THE_TAIL
+ LOCAL_BOUNDED_LATTICE_LIMIT_PRESERVES_THE_CONTROL
+ EXTENSIVE_SOURCE_HAS_NO_VOLUME_UNIFORM_FIXED_ORDER
+ CONTINUUM_FIELD_HANDOFF_REQUIRES_NEW_UNBOUNDED_CONTROL
+ THEORETICAL_KMS_HIERARCHY_IS_NOT_A_PASSIVE_FORMED_RECORD
+ BOUNDED_RESPONSE_DOES_NOT_YET_TRANSFER_GEOMETRY
+ PHYSICAL_INTERFACE_AND_ACQUISITION_STILL_SUPPLIED
+ NO_READY_SUCCESSOR
```

The strongest result is a real constructive advance over `HC-DU-100`.

For any state on a quantum dynamical system, any bounded readout \(A\), any
bounded perturbation \(B\), and any finite source profile \(f\in L^1[0,T]\),
the complete nonlinear response has a factorial Taylor tail. If

\[
x=2|\lambda|\,\lVert B\rVert\,\lVert f\rVert_1,
\]

then the response truncated after order \(N\) obeys

\[
|F(\lambda)-F_N(\lambda)|
\leq
\lVert A\rVert
\sum_{n=N+1}^{\infty}\frac{x^n}{n!}
\leq
\lVert A\rVert e^x\frac{x^{N+1}}{(N+1)!}.
\tag{1}
\]

This is stronger than the generic geometric analytic-tail premise in
`HC-DU-100`. It is also more revealing:

> KMS equilibrium is not what creates the finite response tail. Bounded
> finite-time quantum dynamics creates it. KMS supplies relations among
> thermal orderings and response coefficients.

The theorem is not restricted to a finite Hilbert space. The same proof holds
for a \(C^\ast\)-dynamical system with a bounded integrable perturbation
cocycle. It can therefore survive a thermodynamic limit for a fixed local
bounded source and readout when the infinite-volume dynamics exists.

The positive has two sharp boundaries.

First, it is a **source-budget-relative** theorem. When the perturbation norm
grows with system size or source support, no fixed Taylor order is uniformly
sufficient. The exact thermal two-level family

\[
F_m(\lambda)=q\cos(2m\lambda),
\qquad 0<q<1,
\tag{2}
\]

has perturbation norm \(m\). For every fixed \(N\), its order-\(N\) Taylor
polynomial fails uniformly on any fixed interval containing \([0,1]\) as
\(m\to\infty\).

Second, the theorem controls a **counterfactual controlled response**, not a
passive formed observer record. KMS thermal functions can be expressed in a
causal basis of nested commutators, but noncommuting multi-time orderings are
not one classical sample path. Existing protocols use controlled
perturbations, echoes, interferometry, randomized measurements, weak
measurements, or a declared process-tensor instrument.

The net result is:

> Dynamic Unity now has a physically standard, volume-uniform analytic tail
> for bounded local finite-time response. The remaining high-ceiling
> obstruction has moved to source-class transfer and operational record
> formation: the Lorentzian geometry theorem uses an unbounded continuum
> source-to-solution capability surface, while the bounded quantum theorem
> neither selects nor passively records its higher response hierarchy.

No scientific successor is ready.

## 1. Frozen typed contract

Let \((\mathcal A,\tau_t)\) be a unital \(C^\ast\)-dynamical system. The
finite-dimensional case has

\[
\mathcal A=\mathcal B(\mathcal H),
\qquad
\tau_t(X)=e^{itH_0}Xe^{-itH_0}.
\]

Fix:

- a state \(\omega\) on \(\mathcal A\);
- a bounded readout \(A\in\mathcal A\);
- a bounded self-adjoint perturbation \(B\in\mathcal A\);
- a real source profile \(f\in L^1([0,T])\); and
- a scalar source amplitude \(\lambda\).

In the thermal case,

\[
\omega=\omega_\beta,
\qquad
\rho_\beta=\frac{e^{-\beta H_0}}{\operatorname{Tr}e^{-\beta H_0}}
\]

in finite dimension. Write

\[
B(t)=\tau_t(B),
\qquad
A_T=\tau_T(A),
\]

and let \(U_\lambda\) solve

\[
\frac{dU_\lambda(t)}{dt}
=-i\lambda f(t)B(t)U_\lambda(t),
\qquad
U_\lambda(0)=1.
\tag{3}
\]

The controlled response is

\[
F(\lambda)
=
\omega\!\left(U_\lambda(T)^\ast A_TU_\lambda(T)\right).
\tag{4}
\]

The relevant types are:

```text
state satisfying the KMS condition
!= algebraic thermal n-point function
!= nested-commutator response coefficient
!= controlled source-to-readout response
!= sequential instrument distribution
!= retained observer record
!= geometric target.
```

The task is response reconstruction under a fixed physical law. It is not
source issuance.

## 2. The factorial response theorem

### Proposition 1 — bounded finite-time response has an explicit entire tail

For the contract above, \(F\) is entire in \(\lambda\). If \(F_N\) is its
Taylor expansion through order \(N\), then (1) holds.

### Proof

Iterating (3), or equivalently using the Duhamel expansion for the conjugated
observable, gives

\[
\begin{aligned}
F(\lambda)
=
\sum_{n=0}^{\infty}(i\lambda)^n
\int_{0\leq t_n\leq\cdots\leq t_1\leq T}
&f(t_1)\cdots f(t_n)\\
&\omega\!\left(
[B(t_n),[\cdots,[B(t_1),A_T]\cdots]]
\right)
\,dt_1\cdots dt_n.
\end{aligned}
\tag{5}
\]

Every state has norm one, automorphisms preserve operator norm, and

\[
\lVert[C,D]\rVert
\leq
2\lVert C\rVert\lVert D\rVert.
\tag{6}
\]

Therefore the magnitude of the \(n\)-fold nested commutator in (5) is at most

\[
2^n\lVert B\rVert^n\lVert A\rVert.
\tag{7}
\]

The ordered-simplex integral of the absolute source product is

\[
\int_{0\leq t_n\leq\cdots\leq t_1\leq T}
|f(t_1)\cdots f(t_n)|
\,dt_1\cdots dt_n
=
\frac{\lVert f\rVert_1^n}{n!}.
\tag{8}
\]

Thus the \(n\)-th term is bounded by

\[
\lVert A\rVert
\frac{(2|\lambda|\lVert B\rVert\lVert f\rVert_1)^n}{n!}.
\tag{9}
\]

The majorant is an exponential series, which proves entire convergence and
the first inequality in (1). Taylor's remainder formula for \(e^x\) gives

\[
\sum_{n=N+1}^{\infty}\frac{x^n}{n!}
\leq
e^x\frac{x^{N+1}}{(N+1)!},
\tag{10}
\]

which proves the second. \(\square\)

### What is load-bearing

The proof uses:

- finite duration through \(\lVert f\rVert_1<\infty\);
- bounded source coupling;
- bounded readout;
- norm-preserving dynamics; and
- a normalized state.

It does **not** use:

- the KMS condition;
- stationarity;
- finite dimension;
- a spectral gap;
- mixing;
- a thermal bath;
- a measurement protocol; or
- geometry.

This corrects the initial framing of the swing. The physical source of the
tail is bounded unitary response, not equilibrium.

### Relation to the literature

Kubo's original response theory gives the first-order equilibrium relation
([Kubo 1957](https://doi.org/10.1143/JPSJ.12.570)). Nonlinear response uses
higher nested commutators. Bradlyn and Abbamonte write the second-order
response explicitly as an expectation of a double commutator and note that
the unsymmetrized response function is not itself the directly measured
quantity
([primary source](https://doi.org/10.1103/PhysRevB.110.245132)).

The bound above is the elementary all-order norm consequence of that Duhamel
structure. Dynamic Unity does not claim the component mathematics as novel.
Its new program result is that the abstract tail premise in `HC-DU-100` is
automatically discharged for a precisely typed bounded finite-time source
class.

## 3. KMS supplies organization, not selection

For fixed \((\mathcal A,\tau,\beta,\omega_\beta)\), the KMS condition relates
thermal functions under imaginary-time shifts and cyclic permutations.
Haehl and collaborators show that thermal \(n\)-point functions admit a
natural causal basis in fully nested commutators, with KMS relations spanning
different time orderings
([primary source](https://arxiv.org/abs/1706.08956)).

This matters because the response coefficients in (5) are precisely nested
commutator expectations. In a fully specified algebraic model, KMS structure
can reduce redundancy among the theoretical correlators needed to calculate
response.

It does not select the model.

### Finite dimension

Once \(H_0\) and \(\beta\) are given, the Gibbs density matrix is unique. But
the following remain supplied:

- the Hamiltonian and its parameters;
- inverse temperature;
- the chosen readout \(A\);
- the conjugate perturbation \(B\);
- source profile and amplitude budget;
- subsystem and algebra;
- detector and instrument; and
- target class.

### Infinite volume

The KMS condition need not select one phase. High-temperature uniqueness is a
theorem under additional interaction and temperature conditions, not a
property of the word "KMS"
([Fröhlich--Ueltschi](https://arxiv.org/abs/1412.2534)). Quantum systems can
have multiple equilibrium phases; multiplicity of global equilibrium states
is itself the mathematical signal of a phase transition
([Kozitsky](https://arxiv.org/abs/1806.08264)).

Hence:

```text
KMS-admissible
!= uniquely phase-selected
!= observer-interface-selected.
```

Work extending KMS perturbation theory to some unbounded operators requires
additional noncommutative \(L_p\) domain hypotheses and proves corresponding
multi-time analyticity only within that controlled class
([Correa da Silva](https://arxiv.org/abs/1811.04514)). This supports, rather
than removes, the bounded-to-field boundary below.

## 4. The local lattice positive

### Proposition 2 — the tail survives a bounded local thermodynamic limit

Suppose finite-volume lattice dynamics \(\tau_t^\Lambda\) converge on local
observables to an infinite-volume dynamics \(\tau_t\). Let \(A\) and \(B\)
have fixed finite support and fixed norm as \(\Lambda\) grows. Then (1) is
uniform in every sufficiently large \(\Lambda\), and the same bound holds for
the limiting response.

### Reason

The proof of Proposition 1 depends on \(A\), \(B\), \(f\), and \(T\), not on
the Hilbert-space dimension or ambient lattice volume. For fixed local
operators,

\[
x=2|\lambda|\lVert B\rVert\lVert f\rVert_1
\]

is volume independent.

Lieb--Robinson and quasi-locality methods rigorously construct
infinite-volume dynamics for broad classes of local interactions and control
their finite-volume convergence. Nachtergaele, Sims, and Young give a
systematic treatment including bounded time-dependent interactions and
thermodynamic-limit dynamics
([primary source](https://arxiv.org/abs/1810.02428)).

### What this earns

This is more than a finite-matrix toy:

> A fixed bounded local source in a quantum lattice arena has a
> thermodynamic-limit-uniform finite response order at every declared source
> budget and tolerance.

It still does not say that all spatially extended sources, continuum fields,
or geometry-reconstructing source families have that property.

## 5. The exact source-scale boundary

### Proposition 3 — no fixed order is uniform over unbounded coupling norm

Let \(0<q<1\). On a two-level system choose

\[
H_0=-hX,
\qquad
\tanh(\beta h)=q,
\qquad
B_m=mZ,
\qquad
A=X,
\qquad
U_{m,\lambda}=e^{-i\lambda B_m}.
\]

The Gibbs state is

\[
\rho_\beta=\frac{I+qX}{2},
\]

and

\[
F_m(\lambda)
=
\operatorname{Tr}
\left(
\rho_\beta U_{m,\lambda}^\ast XU_{m,\lambda}
\right)
=q\cos(2m\lambda).
\tag{11}
\]

For every fixed \(N\), the Taylor polynomial \(P_{N,m}\) at zero fails to
approximate \(F_m\) uniformly over \(m\) and \(\lambda\in[0,1]\).

### Proof

For \(N=0\) or \(1\), choose

\[
\lambda_m=\frac{\pi}{2m}\leq1
\]

for sufficiently large \(m\). Then

\[
F_m(\lambda_m)=-q,
\qquad
P_{N,m}(\lambda_m)=q,
\]

so the error is \(2q\).

For \(N\geq2\),

\[
P_{N,m}(1)
=q\sum_{j=0}^{\lfloor N/2\rfloor}
(-1)^j\frac{(2m)^{2j}}{(2j)!}.
\tag{12}
\]

Apart from the harmless factor \(q\), this is a nonconstant polynomial in
\(m\) whose leading coefficient is nonzero. Its magnitude diverges as
\(m\to\infty\), while

\[
|F_m(1)|\leq q.
\]

Therefore the approximation error diverges along the family. \(\square\)

### Interpretation

The parameter \(m\) is an effective extensive coupling scale. The same
\(mZ\) action occurs on the two-dimensional extremal sector of a collective
spin operator. The result does not claim that every extensive source is
poorly behaved. It proves the exact limitation:

> No theorem depending only on boundedness at each finite size can provide a
> fixed response order uniform over a family whose admitted source norm is
> unbounded.

The correct resource is not "number of particles" by itself. It is the
integrated operator-norm source budget

\[
\mathfrak s
=
|\lambda|\int_0^T\lVert V(t)\rVert\,dt.
\tag{13}
\]

Proposition 1 gives a finite order for every fixed \(\mathfrak s\). It gives
no fixed order over \(\mathfrak s\to\infty\).

## 6. Why the continuum-field handoff is not automatic

The bounded theorem applies cleanly to:

- finite quantum systems;
- bounded observables in a \(C^\ast\)-algebra;
- fixed local bounded perturbations in lattice systems; and
- bounded time-dependent cocycles.

The Lorentzian inverse theorem audited in `HC-DU-100` uses a different source
class: local source functions for nonlinear hyperbolic fields, with a rich
continuum source-to-solution map.

Quantum fields are operator-valued distributions; test-function smearing is
part of defining them
([primary source](https://arxiv.org/abs/math-ph/0612011)). Smeared fields are
generally unbounded operators. The inequality

\[
\lVert B\rVert<\infty
\]

that drives Proposition 1 is then unavailable.

There are three possible repairs, none earned here:

1. **Bounded functional repair.** Replace fields by bounded Weyl operators or
   other bounded local-algebra elements, then prove that their response class
   retains the geometric inverse information.
2. **Energy-constrained repair.** Replace operator norm by an independently
   selected energy-constrained or relatively bounded norm and derive a
   uniform factorial or other quantitative tail.
3. **Cutoff repair.** Use a lattice/UV cutoff and prove that the response
   certificate and geometric target transfer uniformly as the cutoff is
   removed.

Each repair is a theorem obligation. A regulator that changes with the target
would be interface refit.

Operational realizability is also narrower than algebraic causality. Recent
work in free scalar QFT proves that some causal channels cannot be
approximated by the admitted local measurement schemes, while identifying a
large realizable class of random field displacements
([Mandrysch--Simmons--Navascués](https://arxiv.org/abs/2607.12976)).
Therefore a bounded local-algebra source family still needs a realizability
proof before it becomes observer capability.

## 7. Why a KMS hierarchy is not one passive record

The theoretical coefficient in (5) is an ordered nested commutator. Expanded
algebraically, it is a signed sum of differently ordered products.

In classical stationary dynamics, one realized path can conditionally supply
many multi-time correlations because the measured variables possess one
joint stochastic history. In quantum mechanics, noncommuting observables do
not generally possess one positive joint distribution with all those
marginals.

The measurement route is instrument relative:

- an echo protocol can estimate an out-of-time-order correlator by reversing
  a Hamiltonian
  ([Swingle et al.](https://arxiv.org/abs/1602.06271));
- interferometry can estimate selected OTO orderings with additional local
  control
  ([Yao et al.](https://arxiv.org/abs/1607.01801));
- weak-measurement protocols estimate an associated quasiprobability
  ([Yunger Halpern--Swingle--Dressel](https://arxiv.org/abs/1704.01971)); and
- process tensors define a complete multi-time operational object only
  relative to a declared family of interventions
  ([Pollock et al.](https://arxiv.org/abs/1512.00589)).

Even at second order, the response kernel need not be the direct measured
object: symmetric applied fields expose a symmetrized combination of
frequency arguments in the Bradlyn--Abbamonte analysis.

Thus:

```text
thermal algebra determines a formal correlator
  -/->
one passive detector produces a joined record of that correlator.
```

An instrument may solve the problem. It must be fixed or physically selected,
and its disturbance, repetitions, source controls, attempt lineage, memory,
precision, and cost must be charged.

## 8. The exact advance toward the North Star

### Before `HC-DU-101`

The nonlinear passive route required:

```text
physically warranted analytic class
+ common coefficient tail
+ response-complete higher correlations
+ instrument
+ finite acquisition
+ geometric transfer.
```

The first two items were both open.

### After `HC-DU-101`

For bounded finite-time source coupling, the analytic class and tail are
automatic:

```text
fixed bounded A and B
+ finite integrated source budget
-> entire response
+ explicit factorial tail.
```

The remaining obligations are now narrower:

```text
source class used by the geometric inverse theorem
+ volume/cutoff-uniform bound for that class
+ operationally response-complete instrument
+ physical state/phase/interface selection
+ finite estimation and acquisition
+ no-refit geometric transfer.
```

This is real progress. It removes a generic analytic uncertainty and reveals
that the live scientific risk is physical typing, not convergence of a
finite matrix expansion.

## 9. Grade, absorption, and disposition

### Earned

- **Scoped Grade 4:** bounded finite-time quantum response is entire and has
  the explicit factorial tail (1).
- **Scoped Grade 4:** KMS is not required for that tail; it organizes thermal
  response coefficients relative to a supplied dynamical system.
- **Scoped Grade 4:** the bound is volume uniform for a fixed local bounded
  source/readout whenever the infinite-volume local dynamics exists.
- **Scoped Grade 4:** no fixed response order is uniform over an unbounded
  perturbation-norm family, by (11)--(12).
- **Scoped Grade 4 typing boundary:** an algebraic KMS hierarchy is not one
  passive formed record without an operational instrument.
- **Conditional Grade 3:** at any fixed integrated bounded-source budget and
  target tolerance, a finite response order is certified explicitly.

### Imported and absorbed

The component mathematics is absorbed by:

- Duhamel/Dyson perturbation theory;
- Kubo nonlinear response and nested commutators;
- KMS thermal ordering relations;
- \(C^\ast\)-dynamical systems and bounded perturbation cocycles;
- Lieb--Robinson and quasi-local thermodynamic-limit results;
- process tensors and operational correlator protocols; and
- algebraic QFT measurement-realizability work.

Dynamic Unity claims the typed composition, dependency closure, exact
source-scale boundary, and corrected location of the remaining North-Star
obligation. It does not claim a new theorem in operator algebras or response
theory.

### Not earned

- a physically selected Hamiltonian, temperature, or KMS phase;
- a selected readout or conjugate perturbation;
- an endogenous passive nonlinear source;
- a passive response-complete multi-time instrument;
- finite-sample estimation and mixing at every retained order;
- a volume-uniform result for extensive sources;
- an unbounded continuum-field response tail;
- a bounded-source inverse Lorentzian geometry theorem;
- complete acquisition;
- no-refit transfer;
- a Grade-5 physical remainder or prediction;
- paper promotion; or
- a ready successor.

### Exact reopener

Reopen the high-ceiling nonlinear passive geometry route when one serious
physical arena supplies, before held-out evaluation:

1. a physically selected state or phase and local source/readout algebra;
2. a bounded, energy-constrained, or cutoff-uniform source class that is rich
   enough for a stated geometric inverse theorem;
3. a response-complete operational instrument for every required ordering;
4. a finite estimation bound, including disturbance and process memory;
5. a target-separation or inverse-stability margin;
6. bounded duration, bandwidth, energy, precision, repetitions, memory, and
   complete attempt acquisition; and
7. no-refit transfer to a held-out causal or conformal target.

The nearest constructive question is whether a physically realizable bounded
local-QFT displacement/instrument family retains enough of the nonlinear
source-to-solution map to support any geometric inverse theorem. That is a
candidate class, not an activated successor.

## 10. Regression scope

`tests/du_bounded_kms_local_response_tail_probe.py` preserves:

- thirteen exact Pauli nested-commutator norm controls;
- thirty-six factorial-tail numerical regressions;
- two finite-order certificate controls; and
- thirteen exact rational scale-family counterexamples.

The scale controls use only the bound

\[
|\cos(2m)|\leq1.
\]

For each retained order \(2\leq N\leq14\), the exact rational Taylor
polynomial at \(\lambda=1\) is made larger than two in magnitude, so its error
against \(q\cos(2m)\) exceeds \(q\) without evaluating the cosine.

The probe is a regression artifact after the proof. It supplies no physical
state, instrument, field limit, geometry, or evidence grade.
