---
title: "Stochastic multiplexing, pairwise versus uniform observability, and the finite-energy record boundary"
status: completed_scoped_gaussian_small_ball_bridge_quantifier_counterexample_and_white_noise_inverse_problem_boundary
doc_type: stochastic_observability_theorem_counterexamples_and_physical_record_gate
created: 2026-07-28
work_id: CCR-STOCHASTIC-MULTIPLEXING-OBSERVABILITY-GATE
claim_id: HC-DU-098
run_id: RUN-20260728-210517-stochastic-multiplexing-observability-gate
lanes:
  - lane_1
  - lane_4
  - lane_6
  - lane_7
channels:
  - CH-FORMAL
  - CH-COLLIDE
  - CH-SYN
claim_grade: "GRADE 4 SCOPED PAIRWISE-ALMOST-SURE VERSUS UNIFORM-RECONSTRUCTION, INFINITE-DIMENSIONAL ISOTROPIC-FINITE-ENERGY, AND SINGLE-WHITE-NOISE VERSUS FINITE-RECORD BOUNDARIES; CONDITIONAL GRADE 3 GAUSSIAN BILINEAR SMALL-BALL CONSTRUCTION UNDER A PHYSICALLY SELECTED TRACE-CLASS SOURCE/READOUT LAW, UNIFORM NOISE-WEIGHTED HILBERT-SCHMIDT RESPONSE GAP, BOUNDED RESOURCE CONDITIONING, JOINT REALIZABILITY, AND CALIBRATED ACQUISITION; STOCHASTIC INVERSE PROBLEMS, GAUSSIAN MOMENTS, PALEY-ZYGMUND, FINITE-MEASUREMENT INVERSE PROBLEMS, AND LOW-DIMENSIONAL MODEL THEORY ABSORB THE COMPONENTS; NO PHYSICAL COVARIANCE SELECTOR, FINITE-TIME ACTIVE-WAVE GAP, GRADE-5 REMAINDER, PREDICTION, PAPER, OR SUCCESSOR"
decision: STOCHASTIC_MULTIPLEXING_CAN_SUPPLY_THE_QUANTITATIVE_MODULUS_ONLY_AFTER_PHYSICS_SUPPLIES_COVARIANCE_RESPONSE_GAP_AND_FINITE_ACQUISITION
---

# Stochastic multiplexing observability gate

## Executive result

The active-wave route left one tempting shortcut:

> Instead of executing a designed family of sources one at a time, use one
> broadband random source whose realization contains many source components.

That shortcut is mathematically real. It is also easy to overread.

This swing proves a conditional positive. Let \(R_\theta\) be the response
operator of completion \(\theta\). Draw an independent Gaussian source
\(W\sim N(0,Q)\) and Gaussian readout weight \(V\sim N(0,S)\), and retain the
scalar

\[
m_{W,V}(\theta)=\langle V,R_\theta W\rangle.
\]

If every target-distinct pair satisfies the uniform noise-weighted response
gap

\[
\left\|
S^{1/2}(R_\theta-R_{\theta'})Q^{1/2}
\right\|_{\mathrm{HS}}
\geq s_\delta>0,
\]

then

\[
\Pr\left\{
\left|m_{W,V}(\theta)-m_{W,V}(\theta')\right|
\geq \frac{s_\delta}{\sqrt2}
\right\}
\geq\frac1{36}.
\]

After conditioning source and readout norms to finite bounds, the probability
remains at least \(1/72\) for sufficiently large bounds. If the response map
is operator-Lipschitz, this supplies all of the mathematical inputs needed by
`HC-DU-097` and yields an explicit finite stochastic packet.

The load-bearing premise is not Gaussianity. It is the uniform gap
\(s_\delta\). No audited active-wave theorem derives it for a finite-energy,
finite-bandwidth, finite-time, finite-readout experiment.

Three exact boundaries prevent overreading:

1. **Pairwise probability one is not uniform reconstruction.** A random
   scalar projection of the unit circle separates every pre-fixed pair almost
   surely, but every realized projection is globally noninjective.
2. **There is no nondegenerate isotropic finite-energy Gaussian source in an
   infinite-dimensional Hilbert space.** Full rotational invariance forces
   covariance \(cI\); trace class forces \(c=0\).
3. **The published one-white-noise inverse results use an ideal record.**
   Their source is distribution-valued, their complete incident and returned
   traces are retained, and operator recovery uses a limit as observation
   time tends to infinity. “One measurement” means one stochastic setting,
   not one finite certified record.

Published finite-measurement inverse results supply the clean positive
control: they obtain stability after assuming that the unknown belongs to a
known finite-dimensional subspace or manifold. They do not show that the
field dynamics selects that low-complexity class.

Dynamic Unity therefore remains quiescent.

Returned states:

```text
GAUSSIAN_BILINEAR_SMALL_BALL_BRIDGE
+ PAIRWISE_ALMOST_SURE_NOT_UNIFORM_RECONSTRUCTION
+ NO_ISOTROPIC_FINITE_ENERGY_INFINITE_DIMENSIONAL_SOURCE
+ WHITE_NOISE_SINGLE_SETTING_INFINITE_RECORD
+ FINITE_MEASUREMENT_LOW_COMPLEXITY_ABSORBER
+ PHYSICAL_COVARIANCE_AND_RESPONSE_GAP_STILL_SUPPLIED
+ NO_READY_SUCCESSOR
```

## 1. Frozen contract

Let:

- \((\Theta,d)\) be a compact physical completion class;
- \(T:\Theta\to(Z,d_Z)\) be the held-out target;
- \(K_\delta\subset\Theta^2\) contain pairs whose targets differ by at least
  \(\delta\);
- \(H_{\mathrm{in}},H_{\mathrm{out}}\) be separable real Hilbert spaces;
- \(R_\theta:H_{\mathrm{in}}\to H_{\mathrm{out}}\) be a bounded physical
  source-to-response map;
- \(Q\) and \(S\) be positive trace-class source and readout covariances; and
- \(W\sim N(0,Q)\), \(V\sim N(0,S)\) be independent.

The scalar probe is

\[
m_{W,V}(\theta)
=
\langle V,R_\theta W\rangle.
\]

The target and pair class may guide preregistered assay design. They do not
choose \(Q\), \(S\), the physical source family, detector algebra, or
completion class after the answer is known.

The physical coordinates remain independent:

- **scope:** an observer-local source/readout worldtube and a hidden target
  region;
- **status:** physical source and response occurrences versus the epistemic
  reconstruction made from them; and
- **formation:** ordinary disclosure under a fixed field law. No source
  issuance claim is involved.

## 2. Pairwise almost-sure separation is not one uniform reconstruction

Let

\[
\Theta=S^1\subset\mathbb R^2
\]

and let \(G\sim N(0,I_2)\). For each draw define

\[
m_G(\theta)=\langle G,\theta\rangle.
\]

### Pairwise statement

For every fixed \(\theta\neq\theta'\),

\[
m_G(\theta)-m_G(\theta')
=
\langle G,\theta-\theta'\rangle
\]

is a nondegenerate real Gaussian. Therefore

\[
\Pr\{m_G(\theta)=m_G(\theta')\}=0.
\]

Every pre-fixed pair is separated almost surely.

### Uniform statement

For every realized \(g\in\mathbb R^2\), the map

\[
\theta\longmapsto\langle g,\theta\rangle
\]

is noninjective on \(S^1\). If \(g\neq0\), reflect any non-extremal point of
the circle across the line spanned by \(g\); the two distinct points have the
same projection. If \(g=0\), every pair has the same value.

Hence

\[
\Pr\{m_G\text{ is injective on }S^1\}=0.
\]

The quantifiers do not commute:

\[
\forall\theta\neq\theta'\quad
\Pr_G[m_G(\theta)\neq m_G(\theta')]=1
\]

does not imply

\[
\Pr_G[
\forall\theta\neq\theta'\quad
m_G(\theta)\neq m_G(\theta')
]=1.
\]

This does not refute any inverse theorem that proves recovery of a complete
operator on one common probability-one event. It proves that a pairwise
almost-sure theorem, by itself, is not that result.

## 3. Gaussian bilinear small-ball bridge

Define, for \(\kappa=(\theta,\theta')\in K_\delta\),

\[
D_\kappa=R_\theta-R_{\theta'}
\]

and

\[
A_\kappa
=
S^{1/2}D_\kappa Q^{1/2}.
\]

Assume

\[
s_\delta
:=
\inf_{\kappa\in K_\delta}
\|A_\kappa\|_{\mathrm{HS}}
>0.
\]

### Theorem

For every \(\kappa\in K_\delta\),

\[
\Pr\left\{
\left|
\langle V,D_\kappa W\rangle
\right|
\geq
\frac{s_\delta}{\sqrt2}
\right\}
\geq
\frac1{36}.
\]

Thus the target-independent Gaussian source/readout law supplies a uniform
small-ball modulus

\[
a_\delta=\frac{s_\delta}{\sqrt2},
\qquad
p_\delta=\frac1{36}.
\]

### Proof

Let

\[
X_\kappa=\langle V,D_\kappa W\rangle.
\]

Using singular coordinates of \(A_\kappa\), or conditioning successively on
the two independent Gaussian variables,

\[
\mathbb E X_\kappa^2
=
\|A_\kappa\|_{\mathrm{HS}}^2.
\]

Conditional on \(W\), \(X_\kappa\) is a centered real Gaussian. Therefore

\[
\mathbb E X_\kappa^4
=
3\,\mathbb E
\left\|
S^{1/2}D_\kappa W
\right\|^4.
\]

For a Hilbert-valued centered Gaussian \(Y\) with covariance \(C\),

\[
\mathbb E\|Y\|^4
=
(\operatorname{tr}C)^2+2\operatorname{tr}(C^2)
\leq
3(\operatorname{tr}C)^2.
\]

Consequently,

\[
\mathbb E X_\kappa^4
\leq
9
\left(\mathbb E X_\kappa^2\right)^2.
\]

Apply Paley--Zygmund to the nonnegative variable \(X_\kappa^2\) at
threshold \(1/2\):

\[
\Pr\left\{
X_\kappa^2
\geq
\frac12\mathbb E X_\kappa^2
\right\}
\geq
\frac14
\frac{(\mathbb E X_\kappa^2)^2}
     {\mathbb E X_\kappa^4}
\geq
\frac1{36}.
\]

On this event,

\[
|X_\kappa|
\geq
\frac{\|A_\kappa\|_{\mathrm{HS}}}{\sqrt2}
\geq
\frac{s_\delta}{\sqrt2}.
\]

\(\square\)

### What the theorem does and does not select

The theorem turns a uniform physical response gap into the exact
`HC-DU-097` probability modulus. It does not derive:

- the covariances \(Q,S\);
- the observer boundary and response operator;
- the target-distinct completion class;
- finite source/readout norms;
- the uniform gap \(s_\delta\);
- joint repeatability;
- finite-time detector statistics; or
- source and readout realization provenance.

## 4. Bounded-resource corollary

Gaussian draws are unbounded. A physical packet therefore needs a bounded
source/readout contract.

Choose \(B_{\mathrm{in}},B_{\mathrm{out}}<\infty\) so that

\[
\Pr\{
\|W\|>B_{\mathrm{in}}
\text{ or }
\|V\|>B_{\mathrm{out}}
\}
\leq\frac1{72}.
\]

Let \(\nu_B\) be the joint Gaussian law conditioned on both norm bounds.
For every \(\kappa\in K_\delta\),

\[
\Pr\left(
|X_\kappa|\geq s_\delta/\sqrt2
\text{ and both bounds hold}
\right)
\geq
\frac1{36}-\frac1{72}
=
\frac1{72}.
\]

Since the conditioning event has probability at most one,

\[
\nu_B
\left\{
|X_\kappa|\geq s_\delta/\sqrt2
\right\}
\geq
\frac1{72}.
\]

If

\[
\|R_\theta-R_x\|_{\mathrm{op}}
\leq
M d(\theta,x),
\]

then every bounded probe is \(L\)-Lipschitz with

\[
L
=
M B_{\mathrm{in}}B_{\mathrm{out}}.
\]

`HC-DU-097` now applies with

\[
a_\delta=s_\delta/\sqrt2,
\qquad
p_\delta=1/72,
\qquad
\rho_\delta
=
\frac{s_\delta}
     {2\sqrt2\,M B_{\mathrm{in}}B_{\mathrm{out}}}.
\]

If \(Q_\delta=N(K_\delta,\rho_\delta)\), then

\[
N
\geq
\frac{\log Q_\delta+\log(1/\alpha)}
     {-\log(71/72)}
\]

independent bounded stochastic probes give the finite target-resolution
packet with design confidence at least \(1-\alpha\). Scalar acquisition error
below

\[
\frac{s_\delta}{4\sqrt2}
\]

preserves the certificate.

Conditioning is itself a physical sampling protocol. Rejected draws and
attempts must be visible to satisfy complete acquisition; otherwise this
corollary inherits the acquisition-visibility obstruction already banked by
Dynamic Unity.

## 5. No isotropic finite-energy Gaussian source in infinite dimension

Let \(H\) be infinite-dimensional and let \(W\sim N(0,Q)\) be an
\(H\)-valued Gaussian source. Finite mean squared source norm requires

\[
\mathbb E\|W\|^2
=
\operatorname{tr}Q
<\infty.
\]

Suppose the law is invariant under every unitary or orthogonal operator
\(U:H\to H\). Then its covariance satisfies

\[
UQU^*=Q
\]

for every \(U\). The commutant of the full unitary group consists only of
scalar multiples of the identity, so

\[
Q=cI.
\]

In infinite dimension, \(cI\) is trace class only when \(c=0\). Hence the
only fully isotropic finite-energy Hilbert-valued Gaussian source is the
degenerate source \(W=0\).

Equivalently, every nondegenerate finite-energy Gaussian design must select
unequal spectral weights, a covariance kernel, a scale, a basis/operator, or
some other structure.

Ideal white noise has formal covariance \(I\). It is therefore cylindrical or
distribution-valued rather than an \(H\)-valued finite-energy random source.
This is not a defect in the mathematics. It is the exact interface that must
be replaced before claiming a bounded physical packet.

## 6. Primary-source audit: what “one white-noise measurement” means

### Multidimensional scattering relation

Helin, Lassas, and Oksanen study a wave equation driven by Gaussian white
noise on
\((0,\infty)\times\partial M\)
([primary source](https://arxiv.org/abs/1308.4879)).
They prove that the complete realization of the source together with the
returned boundary trace determines the scattering relation almost surely,
and in specified simple/conformal cases determines the metric.

The theorem is a serious stochastic-multiplexing positive. Its retained
object is nevertheless:

- the distribution-valued source realization;
- the returned distributional boundary trace;
- the entire positive-time record;
- time-shifted correlations with \(N\to\infty\);
- a Gaussian-beam concentration limit; and
- a continuum scattering relation.

The proof's empirical averages converge almost surely only along an
unbounded time-translation sequence. Its displayed variance control is
asymptotic, not a finite-time uniform target margin.

### One-dimensional coefficient recovery

Blåsten, Helin, Kujanpää, Oksanen, and Railo prove that one white-noise
Neumann input and its pointwise Dirichlet response identify the admissible
coefficient of a \(1+1\)-dimensional wave equation
([primary source](https://arxiv.org/abs/2503.18515)).

The paper is unusually explicit about the interface:

- both the incident white noise and the response are recorded;
- the data are distributions on the time line;
- the proof reconstructs the full Neumann-to-Dirichlet operator in the sense
  of distributions;
- the correlation operator is averaged over \([0,T]\); and
- the decisive convergence is in \(L^2(P)\) as \(T\to\infty\), followed by
  probability-one subsequences and countable test-function limits.

The theorem statement gives pairwise almost-sure separation of two admissible
coefficients. Even where its proof reconstructs a richer operator, it does
not provide:

- a finite observation horizon;
- finite bandwidth or source energy;
- a finite retained alphabet;
- a uniform margin over a compact target-pair class;
- a detector noise and repetition bound; or
- complete-attempt acquisition under physical source conditioning.

### Exact Dynamic Unity reading

These papers show:

```text
one stochastic setting
  can multiplex a continuum source family
  and asymptotically recover a rich response operator.
```

They do not show:

```text
one stochastic setting
  = one finite-time, finite-energy, finite-bit certified record.
```

That distinction is the scientific return, not a criticism of the inverse
theorems.

## 7. Finite-measurement inverse problems as the positive control

Alberti and Santacesaria prove global uniqueness, Lipschitz stability, and a
convergent reconstruction algorithm for Calderón/Schrödinger inverse
problems from finitely many boundary inputs
([primary source](https://arxiv.org/abs/1803.04224)).

The exact enabling assumption is that the unknown potential belongs to a
known finite-dimensional subspace \(\mathcal W\). The number of measurements
depends explicitly on \(\mathcal W\), and the stability constant deteriorates
with that complexity. Each returned Dirichlet-to-Neumann value is also a
boundary function, not automatically a finite-bit scalar.

Alberti, Arroyo, and Santacesaria extend finite-discretization stability to
inverse problems whose unknowns lie on finite-dimensional manifolds
([primary source](https://arxiv.org/abs/2009.00574)).

These are the right controls for `HC-DU-097/098`:

```text
physically selected low-complexity class
  + response stability
  + finite discretization
  -> quantitative finite reconstruction.
```

They do not derive the low-complexity class from field dynamics.

For Gaussian measures on a Hilbert space, the covariance is a positive
trace-class operator; Owhadi and Scovel give a modern primary treatment in
the context of conditional Gaussian measures
([primary source](https://arxiv.org/abs/1506.04208)).
This supports the finite-energy covariance typing used above; the isotropy
no-go is proved directly here.

## 8. Impact on the active-wave route

The admission ladder is now sharper:

```text
physical law selects completion class and target topology
  + physical source state selects finite-energy covariance Q
  + detector selects finite-energy readout covariance S
  + uniform noise-weighted response gap s_delta
  -> stochastic small-ball modulus

bounded source/readout realization
  + operator-Lipschitz response
  + finite target-pair cover
  -> explicit stochastic packet count

finite time and bandwidth
  + known incident/readout provenance
  + complete attempted-process acquisition
  + calibrated scalar quantization
  + no-refit held-out transfer
  -> finite certified active-wave record.
```

Stochastic multiplexing can reduce the number of source settings. It cannot,
by itself, reduce:

- observation duration;
- input and output record dimension;
- source bandwidth or energy;
- completion-class complexity;
- inverse stability;
- covariance/interface selection; or
- acquisition lineage.

The white-noise results therefore improve the architecture without satisfying
the reopener.

## 9. Grade and disposition

### Earned

- **Scoped Grade 4:** pairwise almost-sure separation does not imply that one
  stochastic draw uniformly reconstructs an uncountable completion class.
- **Scoped Grade 4:** a nondegenerate fully isotropic finite-energy Gaussian
  source does not exist on an infinite-dimensional Hilbert source space.
- **Scoped Grade 4:** one-white-noise inverse uniqueness may retain an
  infinite-bandwidth source, full distribution-valued input/output record,
  and infinite-time correlation limit; experimental setting count is not
  record dimension.
- **Conditional Grade 3:** a physically selected source/readout covariance
  and uniform noise-weighted Hilbert--Schmidt response gap give an explicit
  Gaussian small-ball modulus, and bounded conditioning composes into
  `HC-DU-097`.

### Absorbed

The component mathematics is absorbed by Gaussian moment identities,
Paley--Zygmund, stochastic inverse problems, correlation imaging,
finite-measurement inverse problems, and low-dimensional model theory.

Dynamic Unity's contribution is the typed composition and the exact boundary
between a stochastic experimental setting and a finite certified causal
record. No new probability or inverse-problem theorem is claimed.

### Not earned

- physical selection of \(Q,S\);
- a finite-energy active-wave source law;
- a uniform finite-time response gap \(s_\delta\);
- one common probability-one event for the complete physical completion
  class;
- finite detector/readout dimension;
- joint repeatability or reset;
- complete attempted-process acquisition;
- no-refit transfer;
- a Grade-5 physical remainder or prediction;
- paper promotion; or
- a ready successor.

### Exact reopener

Reopen the stochastic active-wave candidate only when one physical arena
supplies, before held-out evaluation:

1. the `HC-DU-096` compact target class;
2. physically selected trace-class source/readout covariances or another
   bounded stochastic design;
3. a uniform finite-time gap
   \[
   \inf_{\kappa\in K_\delta}
   \|S^{1/2}D_\kappa Q^{1/2}\|_{\mathrm{HS}}>0;
   \]
4. operator-Lipschitz or equivalent finite-cover control;
5. a bounded source, detector, duration, bandwidth, repetition, and
   quantization packet;
6. complete joined source/output/attempt acquisition; and
7. no-refit transfer to a held-out causal or conformal target.

A finite-dimensional or manifold restriction is admissible only when a
physical law independently selects it and its complexity cost remains in the
record/resource bound.

## Resource disposition

Exact moment calculations, counterexamples, and primary-source theorem audits
decide the gate. A local stochastic simulation would only illustrate the
proved constants and fails the local-model learning gate. External hardware
is irrelevant until a physical covariance, uniform finite-time gap, and
finite acquisition contract exist.
