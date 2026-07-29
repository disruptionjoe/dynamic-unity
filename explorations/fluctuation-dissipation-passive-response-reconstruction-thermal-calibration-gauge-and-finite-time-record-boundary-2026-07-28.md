---
title: "Fluctuation-dissipation passive response reconstruction, the thermal-calibration gauge, and the finite-time record boundary"
status: completed_scoped_equilibrium_response_reconstruction_thermal_gauge_counterexample_and_finite_time_bridge
doc_type: passive_observability_theorem_counterexample_and_physical_interface_gate
created: 2026-07-28
work_id: CCR-FLUCTUATION-DISSIPATION-PASSIVE-OBSERVABILITY-GATE
claim_id: HC-DU-099
run_id: RUN-20260728-211727-fluctuation-dissipation-passive-observability-gate
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
claim_grade: "GRADE 4 SCOPED SAME-COMPLETE-PASSIVE-PATH-LAW/DIFFERENT-LINEAR-RESPONSE AND FDT-RELATION/INTERFACE-SELECTION BOUNDARIES; CONDITIONAL GRADE 3 EQUILIBRIUM RESPONSE RECONSTRUCTION AND EXPLICIT FINITE-TIME CORRELATION BOUND UNDER INDEPENDENT TEMPERATURE/FORCE CALIBRATION, SELECTED OBSERVABLE/COUPLING, STATIONARITY, UNIFORM MIXING, COMPACT RESPONSE CLASS, COMPLETE ACQUISITION, AND NO-REFIT TRANSFER; KUBO/CALLEN-WELTON, KMS, KRAMERS-KRONIG, ORNSTEIN-UHLENBECK SYSTEM IDENTIFICATION, PASSIVE IMAGING, AND LOCALLY COVARIANT NO-NATURAL-STATE RESULTS ABSORB THE COMPONENTS; NO UNIVERSAL KMS-STATE, OBSERVABLE, DETECTOR, TEMPERATURE, PHASE, GEOMETRIC TARGET, GRADE-5 REMAINDER, PREDICTION, PAPER, OR SUCCESSOR"
decision: FLUCTUATION_DISSIPATION_CLOSES_A_COVARIANCE_RESPONSE_RELATION_NOT_THE_PHYSICAL_RECORD_INTERFACE
---

# Fluctuation-dissipation passive-observability gate

## Executive result

`HC-DU-098` left an apparently artificial premise in the active-wave route:
someone had to choose the source and readout covariances \(Q\) and \(S\).
Equilibrium fluctuation-dissipation physics supplies the first serious
alternative:

> Do not inject a mathematically chosen random source. Use the system's own
> equilibrium fluctuations, whose covariance is physically tied to its
> dissipative response.

This is a real advance. The fluctuation-dissipation theorem (FDT) and the KMS
condition do more than permit a covariance: after the observable, conjugate
perturbation, dynamics, equilibrium state, and thermal calibration are fixed,
the complete equilibrium two-time correlation determines the retarded linear
response. In a narrow overdamped Langevin class, two covariance values and a
known inverse temperature reconstruct every parameter of the response.

But the relation is not a complete selector. The exact counterexample is:

\[
dX_t=-\mu kX_t\,dt+\mu f(t)\,dt+
\sqrt{2\mu/\beta}\,dW_t.
\]

At \(f=0\), the stationary covariance is

\[
C(t)=\frac{1}{\beta k}e^{-\mu k|t|},
\]

and the force-response kernel is

\[
\chi(t)=\mu e^{-\mu kt}\mathbf 1_{t\geq0}.
\]

For any \(a>0\),

\[
(\beta,k,\mu)
\longmapsto
(a\beta,k/a,a\mu)
\]

leaves the complete unforced stochastic differential equation—and therefore
the entire passive path law—unchanged, while

\[
\chi(t)\longmapsto a\chi(t).
\]

Every member satisfies FDT. The missing datum is not another covariance
sample. It is an independent temperature/force calibration.

Once \(\beta\) is fixed, the ambiguity closes exactly. If

\[
A=C(0),\qquad B=C(\tau),\qquad \tau>0,
\]

then

\[
k=\frac1{\beta A},
\qquad
\lambda:=\mu k=-\frac1\tau\log\frac BA,
\qquad
\mu=\beta A\lambda.
\]

Thus two passive correlation values reconstruct the entire response kernel.
A uniform mixing bound makes those values finitely estimable from one
finite-duration trajectory.

The honest return is therefore:

```text
FULL_EQUILIBRIUM_CORRELATION_RECONSTRUCTS_LINEAR_RESPONSE
+ FDT_SELECTS_RELATION_NOT_COMPLETE_INTERFACE
+ THERMAL_CALIBRATION_GAUGE_COUNTEREXAMPLE
+ FINITE_TIME_MIXING_BRIDGE
+ KMS_STATE_AND_OBSERVABLE_SELECTION_STILL_SUPPLIED
+ NO_READY_SUCCESSOR
```

Dynamic Unity remains quiescent.

## 1. Frozen contract

### General equilibrium contract

Let:

- \((\mathcal A,\alpha_t)\) be a supplied observable algebra and time
  evolution;
- \(\omega\) be a supplied \(\beta\)-KMS state;
- \(A\) be the readout observable;
- \(B\) be the observable to which a small external force couples;
- \(C_{AB}(t)=\omega(\alpha_t(A)B)\) be the ordered equilibrium
  correlation; and
- \(\chi_{AB}\) be the retarded response of \(A\) to the force conjugate to
  \(B\).

The full physical interface additionally requires a detector/worldtube,
clock and frequency calibration, observation window, resolution, attempt
lineage, reset or stationarity contract, retained statistic, and held-out
target.

### Exact finite control

Use the stationary overdamped Langevin model

\[
dX_t=-\mu kX_t\,dt+\mu f(t)\,dt+
\sqrt{\frac{2\mu}{\beta}}\,dW_t,
\qquad
\beta,\mu,k>0.
\tag{1}
\]

Here:

- \(X\) is the declared physical readout;
- \(f\) is a separately calibrated generalized force;
- \(k\) is stiffness;
- \(\mu\) is mobility; and
- \(\beta\) is inverse temperature in fixed energy units.

The passive record is the complete unforced stationary path law. The held-out
target is the linear response to \(f\). This is a disclosure problem under a
fixed physical model, not an issuance claim.

## 2. What KMS/FDT reconstructs

For a quantum equilibrium system, linear response has the Kubo form

\[
\chi_{AB}(t)
=
\frac{i}{\hbar}\mathbf 1_{t\geq0}
\omega\!\left([\alpha_t(A),B]\right).
\tag{2}
\]

Therefore the two ordered correlations

\[
C_{AB}(t)=\omega(\alpha_t(A)B),
\qquad
C_{BA}(-t)=\omega(B\alpha_t(A))
\]

determine \(\chi_{AB}\) directly.

The KMS condition relates the two orderings by analytic continuation. In a
standard spectral convention it gives detailed balance

\[
\widehat C_{BA}(-\nu)
=
e^{-\beta\hbar\nu}\widehat C_{AB}(\nu),
\tag{3}
\]

so the commutator spectrum is

\[
\widehat\rho_{AB}(\nu)
=
\left(1-e^{-\beta\hbar\nu}\right)
\widehat C_{AB}(\nu).
\tag{4}
\]

The retarded susceptibility is the causal transform of this spectral
function. When the susceptibility has the required decay or specified
subtractions, Kramers--Kronig reconstructs its dispersive part from its
dissipative part.

This establishes a conditional positive:

```text
selected algebra + dynamics + beta-KMS state
+ selected observable and conjugate coupling
+ complete equilibrium correlation
+ causal/asymptotic convention
-> complete retarded linear response.
```

It does **not** establish:

- a unique KMS state or phase;
- a preferred observable or coupling;
- an independently formed detector record;
- temperature or force-unit calibration;
- finite time or bandwidth;
- nonlinear or far-from-equilibrium response;
- a geometric target; or
- a target-independent record interface.

Callen and Welton's original theorem relates generalized resistance to
equilibrium force fluctuations
([primary source](https://doi.org/10.1103/PhysRev.83.34)). Kubo's
linear-response paper states the general correlation/susceptibility relation
([primary source](https://doi.org/10.1143/JPSJ.12.570)). A recent
many-body result illustrates rather than removes the contract: deriving an
approximate KMS relation for individual non-Abelian energy eigenstates
requires a non-Abelian ETH and retains finite-size corrections
([primary source](https://arxiv.org/abs/2507.07249)).

## 3. Exact thermal-calibration gauge

Set \(f=0\) in (1) and define

\[
\lambda=\mu k,
\qquad
D=\frac{\mu}{\beta}.
\]

The stationary process is the centered Ornstein--Uhlenbeck process

\[
dX_t=-\lambda X_t\,dt+\sqrt{2D}\,dW_t.
\]

Its stationary variance and covariance are

\[
A
=
\frac{D}{\lambda}
=
\frac1{\beta k},
\qquad
C(t)=Ae^{-\lambda|t|}.
\tag{5}
\]

The impulse response to the physical force \(f\) is

\[
\chi(t)
=
\mu e^{-\lambda t}\mathbf 1_{t\geq0}.
\tag{6}
\]

It obeys the classical FDT identity

\[
\chi(t)
=
-\beta\mathbf 1_{t\geq0}\frac{dC(t)}{dt}.
\tag{7}
\]

### Theorem: complete passive-law nonidentifiability

For every \(a>0\), set

\[
\beta_a=a\beta,
\qquad
k_a=\frac{k}{a},
\qquad
\mu_a=a\mu.
\tag{8}
\]

Then

\[
\mu_a k_a=\mu k,
\qquad
\frac{\mu_a}{\beta_a}=\frac{\mu}{\beta},
\qquad
\beta_a k_a=\beta k.
\]

Consequently:

1. the drift coefficient is unchanged;
2. the diffusion coefficient is unchanged;
3. the stationary initial law is unchanged;
4. every finite-dimensional distribution is unchanged;
5. the complete unforced path measure is unchanged; but
6. the held-out force response is
   \[
   \chi_a(t)=a\chi(t).
   \]

Every member satisfies the same fluctuation-dissipation relation with its own
\(\beta_a\). Hence FDT plus the complete passive \(X\)-record does not identify
the force response when thermal/force calibration is outside the record.

This is stronger than the generic passive factorization ambiguity

\[
S_Y(\nu)=R(\nu)Q(\nu)R(\nu)^*,
\qquad
(R,Q)\sim
\left(RG,G^{-1}QG^{-*}\right),
\tag{9}
\]

because the one-parameter family (8) remains inside a standard equilibrium
FDT model.

### Scope

An independent thermometer, energy scale, or calibrated perturbation closes
this particular ambiguity. The theorem does not say the response is
unknowable. It says the passive record is sufficient only relative to an
explicit calibration/access contract.

## 4. Exact positive after calibration

Fix \(\beta\) independently. Choose one lag \(\tau>0\), and suppose the exact
stationary correlations

\[
A=C(0)>0,
\qquad
B=C(\tau)\in(0,A)
\]

are known. Equation (5) gives

\[
\lambda
=
-\frac1\tau\log\frac BA,
\qquad
k=\frac1{\beta A},
\qquad
\mu=\frac{\lambda}{k}=\beta A\lambda.
\tag{10}
\]

Therefore

\[
\chi(t)
=
\beta A\lambda e^{-\lambda t}\mathbf 1_{t\geq0}
\tag{11}
\]

is reconstructed exactly.

This is a strict passive reconstruction:

- the stochastic forcing is endogenous rather than experimenter-designed;
- the record \((A,B)\) is noninjective on uncalibrated
  \((\beta,k,\mu)\)-space;
- the independent \(\beta\) calibration removes exactly the identified
  gauge; and
- the held-out response was not used to choose the two lags.

The result is narrow. The OU model, observable, force port, stationarity, and
thermal interpretation are supplied. It is a positive control for the
North-Star architecture, not a selected field or geometric record theory.

## 5. Finite-time correlation bridge

An ensemble correlation is not yet a finite observer record. Let \(X_t\) be
any centered stationary process and, for fixed \(\tau\), define

\[
Z_t^\tau=X_tX_{t+\tau},
\qquad
\widehat C_L(\tau)
=
\frac1L\int_0^L Z_t^\tau\,dt.
\]

If

\[
M_\tau
:=
\int_0^\infty
\left|
\operatorname{Cov}(Z_0^\tau,Z_s^\tau)
\right|\,ds
<\infty,
\tag{12}
\]

then

\[
\operatorname{Var}\widehat C_L(\tau)
=
\frac{2}{L^2}
\int_0^L
(L-s)\operatorname{Cov}(Z_0^\tau,Z_s^\tau)\,ds
\leq
\frac{2M_\tau}{L}.
\tag{13}
\]

Therefore

\[
\Pr\left\{
\left|\widehat C_L(\tau)-C(\tau)\right|
\geq\epsilon
\right\}
\leq
\frac{2M_\tau}{L\epsilon^2}.
\tag{14}
\]

This theorem needs no IID assumption. It does need a finite, preferably
uniform, integrated mixing bound.

### Exact OU constant

For (5), Isserlis' identity gives

\[
\operatorname{Cov}(Z_0^\tau,Z_s^\tau)
=
C(s)^2+C(s+\tau)C(s-\tau).
\]

Hence

\[
M_\tau
=
A^2
\left[
\frac{1+e^{-2\lambda\tau}}{2\lambda}
+\tau e^{-2\lambda\tau}
\right].
\tag{15}
\]

In particular,

\[
M_0=\frac{A^2}{\lambda}.
\]

Two finite-time estimates at lags \(0\) and \(\tau\) have simultaneous error
at most \(\epsilon\) with probability at least \(1-\alpha\) whenever

\[
L
\geq
\frac{2(M_0+M_\tau)}{\alpha\epsilon^2}.
\tag{16}
\]

### Uniform reconstruction stability

Suppose

\[
A\in[A_{\min},A_{\max}],
\qquad
\lambda\in[\lambda_{\min},\lambda_{\max}],
\qquad
\beta\in[\beta_{\min},\beta_{\max}]
\]

with \(\beta\) measured independently. Let

\[
B_{\min}
=
A_{\min}e^{-\lambda_{\max}\tau}.
\]

If both correlation errors are at most

\[
\epsilon<\frac12\min(A_{\min},B_{\min}),
\]

then the reconstructed decay rate satisfies

\[
|\widehat\lambda-\lambda|
\leq
\frac{2\epsilon}{\tau}
\left(
\frac1{A_{\min}}+\frac1{B_{\min}}
\right).
\tag{17}
\]

Equations (10)--(11) then give explicit Lipschitz bounds for
\(k,\mu,\chi\) on every fixed response horizon. Thus a compact calibrated OU
class has a genuine finite-duration passive response certificate.

The bound becomes expensive or nonuniform as
\(\lambda_{\min}\downarrow0\), as \(B_{\min}\downarrow0\), or as the
correlation class ceases to be integrably mixing. Slow modes, conserved
quantities, phase coexistence, and critical slowing are therefore physical
boundaries, not merely numerical inconvenience.

## 6. Why this does not select the complete record interface

FDT changes the status of one premise in `HC-DU-098`:

```text
arbitrary mathematical covariance
  -> physically constrained equilibrium covariance-response relation.
```

It does not produce:

```text
unique physical state
+ unique observable/coupling
+ formed finite detector archive
+ observer access and calibration
+ held-out geometric target.
```

The missing choices are exact:

1. **Dynamics and algebra.** KMS is defined relative to a supplied time
   evolution and observable algebra.
2. **Temperature.** The thermal-calibration gauge above is invisible to the
   complete passive \(X\)-path law.
3. **State or phase.** At fixed dynamics and temperature, infinite systems
   can have multiple equilibrium phases. In locally covariant QFT, Fewster
   and Verch prove under dynamical-locality and standard assumptions that one
   cannot make a covariant preferred-state choice on all spacetimes
   ([primary source](https://arxiv.org/abs/1106.4785)).
4. **Observable and perturbation port.** FDT relates fluctuations of declared
   observables to their conjugate response; it does not select which physical
   detector or force coupling defines those variables.
5. **Finite access.** A theoretical \(C(t)\) is an ensemble object. A
   trajectory becomes evidence only through stationarity/ergodicity or mixing,
   finite duration, detector calibration, and retained attempt lineage.
6. **Regime.** FDT is an equilibrium linear-response theorem. Non-equilibrium
   internal fluctuations need not equal external response; causal
   Kramers--Kronig constraints can survive more broadly without restoring FDT
   ([primary source](https://arxiv.org/abs/0710.0958)).

The correct phrase is:

> FDT physically constrains a response-covariance relation inside a selected
> equilibrium interface. It does not universally select that interface.

## 7. Collision with passive imaging

Passive imaging already demonstrates the positive mechanism at serious
scale. Helin, Lassas, Oksanen, and Saksala use empirical correlations of a
white-noise-driven wavefield and show that their \(T\to\infty\) limit
determines a nontrapping Riemannian manifold up to isometry
([primary source](https://arxiv.org/abs/1609.08022)).

That theorem is stronger geometrically than the OU control. Its interface is
also stronger:

- white-noise statistics and source support are assumed;
- a continuum receiver region is observed;
- the correlation is retained as a function of two spacetime arguments;
- statistical stability is an infinite-time limit; and
- the metric class and asymptotics are fixed.

Finite passive records carry residual correlation fluctuations. Larose,
Derode, Roux, and Campillo explicitly analyze how finite time/source averaging,
scattering, and absorption affect Green-function reconstruction
([primary source](https://arxiv.org/abs/0805.0195)).

The literature therefore absorbs both component directions:

```text
equilibrium or ambient fluctuations
  -> passive response/Green-function information;

finite duration and incomplete source averaging
  -> residual error and stability cost.
```

Dynamic Unity's surviving contribution is the typed boundary:

```text
physical covariance-response relation
!= selected state/interface
!= finite formed record
!= held-out target reconstruction.
```

## 8. Impact on the active-wave route

The prior ladder required a physically selected external stochastic design.
There are now two separate routes.

### Active route

```text
physical source mechanism selects finite-energy Q and readout S
+ uniform noise-weighted response gap
-> HC-DU-098 small-ball packet.
```

### Passive equilibrium route

```text
physical algebra/dynamics
+ selected equilibrium state or phase
+ independent beta and force calibration
+ selected observable/coupling
-> FDT/KMS response-correlation relation

compact target class
+ uniform correlation-response separation
+ uniform integrated mixing
+ finite detector and complete acquisition
-> finite passive response certificate.
```

The passive route eliminates active source design in its valid regime. It
does not eliminate state, interface, calibration, finite-time, or target-gap
selection.

The next physically meaningful reopener is therefore narrower:

> Find one serious field or geometric arena in which dynamics and boundary
> conditions select an equilibrium or stationary state class, a detector
> coupling and thermal calibration are independently physical, the
> target-distinct correlation laws have a uniform finite-time gap, and one
> unchanged finite record transfers to a held-out causal or conformal target.

A finite OU control proves this architecture is coherent. It does not select
that arena.

## 9. Grade and disposition

### Earned

- **Scoped Grade 4:** the complete passive equilibrium path law need not
  determine the held-out response. The one-parameter family (8) is an exact
  FDT-compliant same-record/different-response witness.
- **Scoped Grade 4:** FDT/KMS selects a relation conditional on algebra,
  dynamics, state, inverse temperature, observable, and coupling; it does not
  universally select those objects.
- **Conditional Grade 3:** with independently fixed \(\beta\), two OU
  covariance values reconstruct the complete linear response.
- **Conditional Grade 3:** an integrated product-covariance bound supplies an
  explicit finite-time passive correlation certificate without IID.

### Absorbed

The component mathematics is absorbed by Callen--Welton/Kubo
fluctuation-dissipation theory, KMS/detailed balance, Kramers--Kronig,
Ornstein--Uhlenbeck system identification, passive imaging, mixing estimates,
and locally covariant no-natural-state results.

Dynamic Unity's contribution is the exact composition and the calibrated
boundary between an endogenous physical fluctuation law, a selected
measurement interface, and a finite certified record.

### Not earned

- a universal equilibrium/KMS-state selector;
- a physical selection law for temperature, phase, observable, coupling,
  detector, or access boundary;
- finite-time field or geometric reconstruction;
- a uniform passive correlation gap in a serious physical completion class;
- complete attempted-process acquisition;
- no-refit second-arena transfer;
- a Grade-5 physical remainder or prediction;
- paper promotion; or
- a ready successor.

### Exact reopener

Reopen the passive route only when one physical arena supplies, before
held-out evaluation:

1. a physically justified stationary/equilibrium completion class;
2. a selected state or phase class and independently calibrated
   temperature/force scale;
3. a physical observable/coupling and finite detector interface;
4. a target-distinct uniform response/correlation margin;
5. a uniform finite integrated-mixing or concentration bound;
6. bounded duration, bandwidth, precision, quantization, memory, and
   complete attempt acquisition; and
7. no-refit transfer to a held-out causal, conformal, field, or capability
   target.

## Resource disposition

Exact Gaussian process algebra and primary-source theorems decide the gate.
A local stochastic simulation would only illustrate equations (5)--(17) and
fails the local-model learning gate. External hardware is irrelevant until a
serious physical arena supplies the state, interface, calibration, finite-time
gap, and acquisition contract.
