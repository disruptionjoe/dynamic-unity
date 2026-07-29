---
title: "Gaussian population reconstruction, finite-shot certification, and the non-Gaussian first leak"
status: completed_scoped_result
doc_type: finite_record_reconstruction_theorem_statistical_boundary_and_scope_counterexample
created: 2026-07-29
hypothesis_id: HC-DU-129
run_id: RUN-20260729-154312-gaussian-finite-record-ladder
authority: "Joe direct chat: Go"
lanes:
  - lane_1
  - lane_3
  - lane_4
  - lane_6
  - lane_7
channels:
  - CH-FORMAL
  - CH-COLLIDE
  - CH-MODEL
  - CH-SYN
warrants:
  - DERIVED
  - CONSTRUCTIVELY_REALIZED
maximum_grade: "Scoped Grade 4 population-setting minimality, finite-shot nonidentification, Gaussian-class, and non-Gaussian first-leak boundary plus conditional Grade 3 finite-resolution reconstruction; no selected mode algebra, Gaussian sector, Hamiltonian, state, detector, observer, interface, empirical excess, new law, new physics, or prediction"
probe: "../tests/du_gaussian_finite_record_ladder_probe.py"
artifact: "../tests/artifacts/du_gaussian_finite_record_ladder_result.json"
---

# Gaussian population reconstruction and finite-record ladder

## Executive result

The swing returned:

```text
FIXED FINITE-MODE GAUSSIAN CLASS
  + EXACT QUADRATURE POPULATION STATISTICS
  -> FINITE MINIMAL STATE-RECONSTRUCTION PACKET

BUT

FINITE POPULATION PARAMETERIZATION
  != FINITE-SHOT EXACT IDENTIFICATION

FINITE IID SUFFICIENT STATISTIC
  != TRUE-PARAMETER DETERMINATION

BOUNDED COVARIANCE + IID LINEAGE + DECLARED ERROR/CONFIDENCE
  -> FINITE CONDITIONAL CERTIFICATE

FIRST AND SECOND MOMENTS
  -/> NON-GAUSSIAN HELD-OUT TARGETS

QUADRATIC DYNAMICS PRESERVES GAUSSIANITY
  != SELECTS THE GAUSSIAN STATE

NO READY SUCCESSOR
```

This is a genuine positive response to the `HC-DU-128` reopener:

> On a fixed \(n\)-mode bosonic algebra, the complete Gaussian state is
> determined by finitely many first and second moments. Under a
> single-output quadrature-population contract, exactly
> \(n(2n+1)\) settings are necessary and sufficient.

The positive is at the **population** level. It assumes exact probability
distributions or their exact means and variances. It does not mean that a
finite experimental transcript determines the true continuous parameter.

The physical result is therefore sharper:

> A finite formed record can certify a Gaussian state only relative to a
> declared accuracy, confidence, energy/covariance bound, acquisition model,
> calibration, and digitization contract. Exact finite-shot reconstruction
> fails even inside the Gaussian class.

And the class restriction is load-bearing. A one-photon Fock state and a
thermal Gaussian state can have identical means and covariance while differing
on a fourth moment and number variance.

## 1. Four different completeness claims

Let \(m=2n\) and let

\[
R=(Q_1,P_1,\ldots,Q_n,P_n)
\]

be a supplied calibrated canonical-quadrature vector. Write

\[
d_i=\langle R_i\rangle
\tag{1}
\]

and

\[
V_{ij}
=
\frac12\left\langle
(R_i-d_i)(R_j-d_j)
+
(R_j-d_j)(R_i-d_i)
\right\rangle.
\tag{2}
\]

A Gaussian state has characteristic function

\[
\chi_\rho(u)
=
\exp\!\left(
i u^\mathsf Td
-\frac12u^\mathsf TVu
\right)
\tag{3}
\]

in the declared convention. Thus \((d,V)\) determines every Weyl expectation
in the fixed finite-mode algebra.

Keep the following separate:

| Object | What it is | What it can establish |
|---|---|---|
| \((d,V)\) | theoretical Gaussian-state parameter | every Gaussian-state expectation on the fixed algebra |
| exact quadrature populations | ideal probability laws for declared settings | exact means and variances |
| finite transcript | finitely many setting-indexed detector outcomes | one stochastic sample path |
| likelihood-sufficient summary | count, sum, and squared sum per iid setting | all likelihood information in that transcript |
| certificate | confidence-qualified parameter/target region | finite-error rival exclusion under declared assumptions |

The first two can exactly reconstruct the Gaussian state. The last three do
not exactly identify a continuous true parameter at finite sample size.

[Zhang and Mølmer](https://journals.aps.org/pra/abstract/10.1103/PhysRevA.96.062131)
use precisely the finite mean/covariance description for Gaussian oscillator
states under Gaussian-preserving continuous monitoring. That is a physical
and mathematical precedent for the representation, not a theorem that a
particular observer forms the complete packet.

## 2. Minimal population-setting theorem

For a supplied real direction \(u\in\mathbb R^m\), one quadrature population
has

\[
\mu(u)=u^\mathsf Td
\tag{4}
\]

and

\[
v(u)=u^\mathsf TVu.
\tag{5}
\]

### Theorem 1 — single-output setting minimum

For the class of all physical \(m\)-quadrature Gaussian states, at least

\[
k
=
\dim\operatorname{Sym}_m
=
\frac{m(m+1)}2
=
n(2n+1)
\tag{6}
\]

single-output quadrature-population settings are necessary to reconstruct
every covariance. The bound is attained by

\[
\mathcal U
=
\{e_i\}_{i=1}^m
\cup
\{e_i+e_j:1\leq i<j\leq m\}.
\tag{7}
\]

#### Necessity

For each setting, \(V\mapsto u^\mathsf TVu\) is one linear functional on
\(\operatorname{Sym}_m\). The physical covariance cone has nonempty interior,
so fewer than \(k\) such functionals leave a nonzero covariance direction in
their joint kernel. Physical covariances on both sides of a sufficiently small
perturbation therefore share every retained variance.

#### Sufficiency

The coordinate settings give

\[
V_{ii}=v(e_i).
\tag{8}
\]

The pair settings give

\[
V_{ij}
=
\frac{
v(e_i+e_j)-v(e_i)-v(e_j)
}{2}.
\tag{9}
\]

The coordinate means give \(d_i=\mu(e_i)\). Equations (8)--(9) reconstruct
\((d,V)\), and therefore (3), exactly.

Normalizing \(e_i+e_j\) changes only the calibration factor. It does not
change the setting count.

The exact regression verifies full rank and reconstruction for one through
four modes:

| modes \(n\) | quadratures \(m\) | settings \(n(2n+1)\) | exact rank |
|---:|---:|---:|---:|
| 1 | 2 | 3 | 3 |
| 2 | 4 | 10 | 10 |
| 3 | 6 | 21 | 21 |
| 4 | 8 | 36 | 36 |

Dropping one setting produces, at every tested size, two strictly physical
covariances with identical retained populations and different held-out
variance.

This count is interface-relative. A joint multivariate readout supplies
several covariance functionals per setting and can use fewer settings.
[Holevo's structure theorem](https://arxiv.org/abs/2007.02340) places homodyne
and heterodyne readouts inside a larger Gaussian-observable class, so no
setting count is meaningful without its output type. Consistently, the 2026
multimode experiment by
[Roh et al.](https://arxiv.org/abs/2603.21380) uses
\(n(2n+1)\) settings for its single-homodyne design and fewer joint-homodyne
settings because each joint outcome carries cross-mode correlation data.

## 3. Likelihood sufficiency is not physical reconstruction

At one fixed direction, suppose the frozen instrument returns iid samples

\[
x_1,\ldots,x_N
\sim
\mathcal N(\mu,q).
\]

The likelihood is

\[
L(\mu,q\mid x)
\propto
q^{-N/2}
\exp\!\left[
-\frac{
\sum_tx_t^2-2\mu\sum_tx_t+N\mu^2
}{2q}
\right].
\tag{10}
\]

Therefore the tuple

\[
\left(
N,\sum_tx_t,\sum_tx_t^2
\right)
\tag{11}
\]

is sufficient for this iid Gaussian likelihood. The executable control uses
two different ordered transcripts,

\[
(0,0,3,3)
\quad\text{and}\quad
(0,1,1,4),
\tag{12}
\]

which share

\[
\left(N,\sum x,\sum x^2\right)
=(4,6,18).
\tag{13}
\]

They have the same likelihood for every \((\mu,q)\).

That is a real compression theorem. It is not a state-reconstruction theorem:

1. the summary is sufficient only under the supplied iid Gaussian process;
2. it erases ordering and provenance that can matter outside that process;
3. every nonsingular parameter still has positive likelihood; and
4. exact real sums are not automatically finite-bit physical records.

This is the same type distinction DU encountered with Barandes's stochastic
tuple and process tensors: sufficient for a declared likelihood family does
not mean interventionally or historically complete.

## 4. Exact finite-shot nonidentification

### Theorem 2 — every finite digitized transcript has a Gaussian fibre

Fix any finite family of quadrature settings and any finite detector
transcript whose bins have nonempty width. Every nonsingular Gaussian
quadrature distribution has strictly positive density everywhere. Hence it
assigns strictly positive probability to every nonempty bin.

For any finite transcript \(r\),

\[
\Pr_{d,V}(R=r)>0
\tag{14}
\]

for every physical Gaussian packet whose projected variances are nonzero.
Therefore

\[
\mathcal C(r)
=
\{(d,V):\Pr_{d,V}(R=r)>0\}
\tag{15}
\]

contains a continuum of distinct states.

The exact control gives one four-bin transcript with probability

\[
1.54\times10^{-5}
\]

under a centered variance-\(1/2\) population and

\[
3.64\times10^{-5}
\]

under a centered variance-\(3/2\) population. The likelihoods differ, but both
states remain in the physical completion fibre.

Thus:

> No finite shot count exactly identifies an unrestricted continuous Gaussian
> state from ordinary noisy quadrature outcomes.

Increasing \(N\) changes relative support and confidence. It never makes an
ordinary finite sample impossible under every rival with full support.

This is not a defect in Gaussian tomography. It is the ordinary distinction
between estimation and logical identification.

## 5. What finite data can earn

The exact North-Star repair is an accuracy-and-confidence certificate.

Assume:

- \(N\) independent preparations per direction;
- complete attempt/setting lineage;
- \(\lambda_{\max}(V)\leq B\);
- requested coordinate-mean error \(\varepsilon_d\);
- requested covariance-entry error \(\varepsilon_V<3B\); and
- total failure probability \(\alpha\).

For coordinate sample means,

\[
\Pr(
|\widehat d_i-d_i|\geq\varepsilon_d
)
\leq
2\exp\!\left(
-\frac{N\varepsilon_d^2}{2B}
\right).
\tag{16}
\]

For an unbiased sample variance \(S_u^2\), Gaussian chi-square concentration
and \(u^\mathsf TVu\leq2B\) on the directions (7) give, for
\(\eta<2B\),

\[
\Pr(
|S_u^2-u^\mathsf TVu|\geq\eta
)
\leq
2\exp\!\left(
-\frac{(N-1)\eta^2}{32B^2}
\right).
\tag{17}
\]

If every retained variance is within

\[
\eta=\frac{2}{3}\varepsilon_V,
\tag{18}
\]

then (8)--(9) reconstruct every covariance entry within
\(\varepsilon_V\). Splitting the error budget between means and variances and
using a union bound, it is sufficient that

\[
N
\geq
\max\left\{
\frac{2B}{\varepsilon_d^2}
\log\frac{4m}{\alpha},
\;
1+
\frac{72B^2}{\varepsilon_V^2}
\log\frac{4k}{\alpha}
\right\}.
\tag{19}
\]

This bound is intentionally conservative. It proves finiteness and makes the
assumption price explicit; it is not presented as an optimal tomography
protocol. For \(B=2\), errors \(0.2\), and \(\alpha=0.05\), it gives the
following per-setting budgets:

| modes | settings | sufficient repetitions per setting |
|---:|---:|---:|
| 1 | 3 | 39,462 |
| 2 | 10 | 48,131 |
| 3 | 21 | 53,473 |

Modern estimators can perform substantially better. The point is the
contract:

```text
finite formed transcript
  + bounded physical class
  + frozen iid acquisition
  + declared epsilon and alpha
  -> finite certificate.
```

[Tripier-Mondancin et al.](https://arxiv.org/abs/2503.14188) provide a
strong physical absorber: in their squeezed-state task, a moment estimator
using homodyne/double-homodyne samples reaches the Cramér--Rao bound.
[Roh et al.](https://arxiv.org/abs/2603.21380) show why the distinction remains
operationally important: finite-sample direct covariance estimates can be
unphysical, while a constrained maximum-likelihood reconstruction enforces
the uncertainty condition.

### Finite-bit acquisition

Equation (19) treats calibrated real-valued outcomes before digitization. A
finite-bit physical record needs two further declared budgets.

If \(\|d\|\leq D\), every direction in (7) satisfies
\(|\mu(u)|\leq\sqrt2D\). Clipping at \(L>\sqrt2D\) gives

\[
\Pr(\text{any clip})
\leq
2kN
\exp\!\left[
-\frac{(L-\sqrt2D)^2}{4B}
\right].
\tag{20}
\]

On the no-clip event, rounding with step \(\Delta\) adds at most
\(\Delta/2\) to a sample mean. For the biased second-central-moment form, the
deterministic variance perturbation is bounded by

\[
2L\Delta+\frac{\Delta^2}{2}.
\tag{21}
\]

Calibration drift, detector noise, saturation, missing attempts, and
non-iid preparation add their own terms. They cannot be renamed statistical
error.

This is why “finite moments determine a Gaussian state” does not by itself
solve physical record formation.

## 6. The non-Gaussian first leak

Use the convention \([Q,P]=i\), so vacuum covariance is
\(\tfrac12I\).

The one-photon Fock state \(|1\rangle\) has

\[
d=0,
\qquad
V=\frac32I.
\tag{22}
\]

The centered thermal Gaussian state with mean occupation
\(\bar n=1\) has exactly the same packet:

\[
d=0,
\qquad
V=\left(\bar n+\frac12\right)I
=\frac32I.
\tag{23}
\]

Their held-out fourth quadrature moments differ:

\[
\langle Q^4\rangle_{|1\rangle}
=
\frac{15}{4},
\qquad
\langle Q^4\rangle_{\mathrm{thermal}}
=
\frac{27}{4}.
\tag{24}
\]

Their number variances differ even more simply:

\[
\operatorname{Var}_{|1\rangle}(N)=0,
\qquad
\operatorname{Var}_{\mathrm{thermal}}(N)=2.
\tag{25}
\]

Therefore exact first and second moments determine all held-out Gaussian
queries only after the Gaussian completion class is fixed.

The broader fact that many non-Gaussian states share a covariance is central
to Gaussian extremality results; see
[Wolf, Giedke, and Cirac](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.96.080502).
Those results can make a Gaussian state an extremal bound for a target without
making it the unique physical completion.

## 7. Preservation, selection, and law-only absorption

A quadratic Hamiltonian maps quadratures linearly and preserves Gaussianity
of a Gaussian initial state. It does not select the initial state.

More strongly, an invertible Gaussian unitary cannot turn a non-Gaussian state
into a Gaussian one. If \(U\rho U^\dagger\) were Gaussian, applying the inverse
Gaussian unitary would make \(\rho\) Gaussian.

There are two different positive branches:

1. **Law-side singleton.** A specified stable quadratic Hamiltonian plus a
   specified nondegenerate ground-state contract, or a specified inverse
   temperature and KMS/Gibbs contract, can select one Gaussian state. The
   held-out state is then fixed by the law packet; records confirm or estimate
   realization but do not perform the selection.
2. **Record-conditioned family.** If Hamiltonian parameters, temperature,
   preparation, or noise are not fixed, the Gaussian record estimates them
   relative to a supplied Gaussian mode and detector model.

“Quadratic dynamics” alone does neither job. Preservation is not state
selection, and a law-only singleton is not record-first reconstruction.

## 8. Relation to the preceding DU results

### `HC-DU-102`

The Weyl displacement channel exposes the symplectic form but does not select
the symmetric covariance. `HC-DU-129` supplies the missing finite-mode
population packet for that covariance—conditional on a separately supplied
mode algebra, Gaussian class, and quadrature interface.

### `HC-DU-128`

The infinite full-functional hierarchy collapses to \((d,V)\) inside the
finite-mode Gaussian class. This is the first exact finite-parameter closure
of that reopener.

The new boundary is physical acquisition:

```text
finite Gaussian parameterization
  != finite population data
  != finite transcript
  != finite confidence certificate
  != exact rival exclusion.
```

### Full QFT

No continuum QFT transfer follows. A quasifree field state is determined by a
two-point distribution, but that distribution remains an infinite object.
Selecting finitely many modes or smearings is an additional truncation and
localization contract whose discarded directions may contain the held-out
target.

### GU/Krein

No GU transfer follows. The present arena is positive Hilbert/CCR Gaussian
theory. `HC-DU-128`'s indefinite reconstruction debt remains.

## 9. Grade, absorption, and stop

### Earned

- **Scoped Grade 4:** \(n(2n+1)\) single-output quadrature-population settings
  are necessary and sufficient for every finite-mode Gaussian state.
- **Scoped Grade 4:** fewer settings admit exact physical
  same-record/different-covariance witnesses.
- **Scoped Grade 4:** every finite digitized transcript remains compatible
  with a continuum of nonsingular Gaussian parameters.
- **Conditional Grade 3:** bounded covariance, iid acquisition, full lineage,
  and declared \((\varepsilon,\alpha)\) yield a finite certificate.
- **Scoped Grade 4:** the one-photon/thermal witness proves exact
  first/second-moment insufficiency outside the Gaussian class.
- **Scoped Grade 4:** closed quadratic preservation does not select a Gaussian
  state.

### Absorbed

The component mathematics is absorbed by:

- Gaussian-state characteristic functions;
- Gaussian quantum tomography;
- Fisher--Neyman factorization;
- normal and chi-square concentration;
- Gaussian versus non-Gaussian moment theory; and
- quadratic/Gaussian unitary dynamics.

DU's increment is the typed reconstruction ladder joining population
completeness, formed transcript, statistical sufficiency, confidence
certificate, class selection, and first leak.

### Not earned

- a selected mode algebra, symplectic form, phase reference, or localization;
- a dynamically selected Gaussian completion class;
- a selected Hamiltonian, temperature, state, preparation, detector, or
  quadrature schedule;
- exact finite-shot state determination;
- a QFT continuum or GU/Krein reconstruction;
- a public finality or action-capability theorem;
- empirical excess, new law, new physics, or prediction; or
- a ready successor.

### Exact reopener

Reopen only when one serious physical arena supplies, before held-out
evaluation:

1. a dynamically selected finite mode/subalgebra or a finite-sufficient
   continuum theorem;
2. an independently selected exact or quantitatively controlled
   near-Gaussian state class;
3. a physically realized, fully acquired and calibrated instrument with
   attempt lineage;
4. a declared target, accuracy, confidence, action, and resource contract;
5. a no-refit held-out transfer; and
6. a comparator showing the record adds information beyond the law packet.

More Gaussian tomography examples do not satisfy this reopener.

## Honest status

`HC-DU-129` closes the easiest finite-functional interpretation without
closing the North Star.

The Gaussian restriction turns the infinite state hierarchy into finitely
many theoretical parameters. It also supports finite experimental
certification at declared resolution. It does not turn a finite stochastic
record into exact state truth, select the restriction, or survive removal of
the Gaussian class.
