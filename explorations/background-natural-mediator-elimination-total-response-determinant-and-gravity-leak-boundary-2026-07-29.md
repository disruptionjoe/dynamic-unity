---
title: "Background-natural mediator elimination: total response, determinant, and gravity-leak boundary"
status: completed_scoped_result
doc_type: exact_variational_theorem_counterexample_and_quantum_effective_action_boundary
created: 2026-07-29
hypothesis_id: HC-DU-116
run_id: RUN-20260729-101854-background-natural-mediator-elimination
authority: "Joe direct chat: Go"
lanes:
  - lane_1
  - lane_2
  - lane_3
  - lane_4
  - lane_6
  - lane_7
channels:
  - CH-FORMAL
  - CH-COLLIDE
  - CH-MODEL
  - CH-SYN
maximum_grade: "Scoped Grade 4 background-natural elimination theorem and pointwise-equivalence counterexample; no empirical excess, selected record, ontology priority, new law, new physics, or prediction"
probe: "../tests/du_background_natural_mediator_elimination_probe.py"
artifact: "../tests/artifacts/du_background_natural_mediator_elimination_result.json"
---

# Background-natural mediator elimination

## Executive result

The swing returned:

```text
ON_SHELL_BACKGROUND_RESPONSE_PRESERVED_BY_EXACT_ELIMINATION
+ POINTWISE_SOURCE_EQUIVALENCE_DOES_NOT_FIX_BACKGROUND_DERIVATIVE
+ FULL_PARAMETER_KERNEL_EQUIVALENCE_ABSORBS_SOURCE_GRAVITY_DISCRIMINATOR
+ LOCAL_MEDIATOR_RESPONSE_PARTITION_IS_NOT_ELIMINATION_INVARIANT
+ SOURCE_INDEPENDENT_QUANTUM_DETERMINANT_CAN_CARRY_BACKGROUND_RESPONSE
+ FULL_QUANTUM_BACKGROUND_EQUIVALENCE_REQUIRES_DETERMINANT_MEASURE_STATE_AND_BOUNDARY
+ HELD_OUT_BACKGROUND_RESPONSE_IS_A_CANDIDATE_FIRST_LEAK_NOT_AN_EARNED_REMAINDER
+ NO_EMPIRICAL_EXCESS_OR_ONTOLOGY_PRIORITY_FOLLOWS
+ NO_READY_SUCCESSOR
```

`HC-DU-115` proved that an explicit quadratic mediator and its exact
source-to-source action are indistinguishable to every query that factors
through the frozen-background on-shell source action. The present result
asks the next question: does that equivalence survive when a physical
background is varied?

There are three different answers because there are three different
contracts:

1. **Exact classical elimination preserves total on-shell background
   response.** This is the envelope theorem. If the mediator solves its field
   equation and all background dependence and boundary conditions are
   retained, differentiating the reduced action gives the same total
   derivative as differentiating the unreduced action on shell.
2. **Agreement at one background does not fix background response.** Two
   mediator completions can give exactly the same source action at
   \(\lambda_0\) and different first derivatives there. If \(\lambda\) is a
   metric parameter, this is a same-source/different-metric-response witness.
   It exposes an incomplete equivalence contract, not new physics.
3. **Quantum equivalence requires more than the source kernel.** Gaussian
   elimination produces a determinant that is source-independent at a frozen
   background. If its kinetic operator depends on the background, its
   derivative need not vanish. It can therefore contribute to the quantum
   effective action's metric response even when every source-facing query
   agrees.

This corrects a phrase in `HC-DU-115`: “source-independent determinant” means
irrelevant to the declared frozen-background source query, not physically
irrelevant to every enlarged query.

The new Dynamic Unity guard is:

> Field/direct-action equivalence is background-natural only when the complete
> effective action—including determinant, measure, state, boundary,
> regulator, and allowed counterterms—matches over the admitted background
> family. Matching one source kernel at one background is insufficient.

Even then, a local split of total response into mediator, matter, absorber, or
channel pieces need not be invariant. Only the total response is protected.

This is a scoped Grade-4 theorem and counterexample assembled from standard
variational and Gaussian-integration mathematics. It does not establish a
physical field/direct-action difference, a gravitational anomaly, an
experiment, or a ready successor.

## 1. Literature and type boundary

[Wheeler and Feynman](https://doi.org/10.1103/RevModPhys.17.157) developed a
direct-interparticle account of electrodynamics, while
[Narlikar](https://doi.org/10.1017/S0305004100043838) proved a broad,
assumption-scoped correspondence between field theories and direct-particle
actions in curved spacetime. These results make the background question
legitimate: a curved-spacetime translation must preserve how the interaction
depends on the geometry, not only its value on one geometry.

The present finite result is not a curved-spacetime field theorem. It uses a
generic parameter \(\lambda\). The following types must remain separate:

| Object | Meaning |
|---|---|
| \(S(j,\phi;\lambda)\) | full finite action with explicit mediator |
| \(S_{\rm eff}(j;\lambda)\) | stationary reduced source action |
| \(dS_{\rm eff}/d\lambda\) | generic background response |
| \(\delta S/\delta g^{\mu\nu}\) | metric variation, related to total stress-energy only after convention, boundary, and covariance are fixed |
| local mediator stress | branch-specific decomposition of total response |
| quantum effective action | includes fluctuation determinant, measure, state, regulator, boundary, and counterterm data |
| certified record | independently formed and accessed physical output; none is selected here |

A generic derivative becomes a gravitational claim only after \(\lambda\)
parameterizes an admitted metric variation and the relevant action and
boundary contract is frozen.

## 2. Classical background-envelope theorem

### Frozen object

Let \(j\) be a source coordinate, \(\phi\) an explicit mediator, and
\(\lambda\) a differentiable background parameter. Define

\[
S(j,\phi;\lambda)
=
\frac12 A(\lambda)j^2
+B(\lambda)j\phi
+\frac12K(\lambda)\phi^2,
\qquad K(\lambda)\ne0.
\tag{1}
\]

The stationary mediator is

\[
\phi_*(j,\lambda)
=
-\frac{B(\lambda)}{K(\lambda)}j,
\tag{2}
\]

and the reduced action is

\[
S_{\rm eff}(j;\lambda)
=
S(j,\phi_*(j,\lambda);\lambda)
=
\frac12
\left(
A(\lambda)-\frac{B(\lambda)^2}{K(\lambda)}
\right)j^2.
\tag{3}
\]

### Theorem 1 — total response is preserved on shell

For fixed \(j\),

\[
\frac{dS_{\rm eff}}{d\lambda}
=
\left.
\frac{\partial S}{\partial\lambda}
\right|_{\phi=\phi_*}.
\tag{4}
\]

### Proof

By the chain rule,

\[
\frac{d}{d\lambda}
S(j,\phi_*(j,\lambda);\lambda)
=
\left.
\frac{\partial S}{\partial\lambda}
\right|_{\phi_*}
+
\left.
\frac{\partial S}{\partial\phi}
\right|_{\phi_*}
\frac{\partial\phi_*}{\partial\lambda}.
\tag{5}
\]

Stationarity makes the second term zero. Therefore (4) follows. Directly,

\[
\frac{dS_{\rm eff}}{d\lambda}
=
\frac12j^2
\left[
A'
-\frac{2BB'}{K}
+\frac{B^2K'}{K^2}
\right],
\tag{6}
\]

which equals \(\partial_\lambda S\) evaluated at
\(\phi_*=-Bj/K\). \(\square\)

The proof is more general than the quadratic specimen: any differentiable
stationary elimination obeys the envelope identity when the solution and
boundary conditions are well behaved. The finite quadratic form makes every
term inspectable and exact.

### Meaning

If \(\lambda\) really is a metric parameter and the explicit and reduced
actions are the same complete functional of that metric, eliminating the
mediator does not erase total classical stress response. The response has
been transferred into the metric dependence of the nonlocal source kernel.

This closes the naive discriminator:

> “One formulation has a local field stress tensor and the other has no
> explicit field, so gravity must distinguish them.”

Not necessarily. Exact elimination can preserve the total metric variation.

## 3. Pointwise equivalence does not fix the first background jet

The preceding positive theorem assumes one common
\(S(j,\phi;\lambda)\) and retains its complete \(\lambda\)-dependence.
`HC-DU-115` froze \(\lambda\) and matched only the source kernel at that point.
That weaker contract does not determine (6).

### Counterexample 1 — same action, different derivative

At \(\lambda_0=0\), take

\[
A_1=A_2=0,\qquad
B_1=B_2=1,\qquad
K_1=K_2=1,
\tag{7}
\]

but

\[
K_1'=1,\qquad K_2'=2,
\qquad
A_1'=A_2'=B_1'=B_2'=0.
\tag{8}
\]

Both reduced source kernels at \(\lambda_0\) are

\[
C_1=C_2=A-\frac{B^2}{K}=-1.
\tag{9}
\]

Thus every value and source derivative of the frozen-background quadratic
action agrees. Their first background derivatives are

\[
C_1'=1,\qquad C_2'=2.
\tag{10}
\]

For nonzero \(j\),

\[
\left.
\frac{dS_{{\rm eff},1}}{d\lambda}
\right|_0
=
\frac12j^2,
\qquad
\left.
\frac{dS_{{\rm eff},2}}{d\lambda}
\right|_0
=
j^2.
\tag{11}
\]

This is an exact same-source/different-background-response witness.

### What it earns

It proves:

> Pointwise source equivalence is not background-natural equivalence.

If a proposed field/direct-action translation was fitted only at one metric,
a held-out metric derivative is a legitimate first-leak assay.

It does not prove:

- that nature realizes either completion;
- that \(\lambda\) is a metric;
- that both actions share the same boundary and renormalization contract;
- that the difference survives an allowed counterterm;
- that any observer can access the response; or
- that standard QFT is violated.

## 4. Full source-family equivalence absorbs the source discriminator

The exact source kernel for diagonal mediator channels is

\[
C(\lambda)
=
A(\lambda)
-\sum_i\frac{B_i(\lambda)^2}{K_i(\lambda)}.
\tag{12}
\]

If two completions have the same \(C(\lambda)\) on an open neighborhood,
then every derivative of the source action allowed by that regularity class
also agrees. No source-only background-response experiment can distinguish
them.

The regression uses:

\[
B^{(1)}=(1),\qquad
B^{(2)}=\left(\frac35,\frac45\right),
\qquad
K^{(1)}=(k),\qquad
K^{(2)}=\operatorname{diag}(k,k).
\tag{13}
\]

Because \(9/25+16/25=1\), both give

\[
C(\lambda)=-\frac1{k(\lambda)}
\tag{14}
\]

and the same \(C'(\lambda)\).

This is the correct absorber:

> Once the complete background-dependent effective source action is matched,
> gravity does not automatically reopen a source-facing difference.

## 5. Total response does not identify a local partition

In (13), the one-channel completion assigns the entire response to one
mediator coordinate. The two-channel completion assigns fractions

\[
\frac9{25},
\qquad
\frac{16}{25}
\tag{15}
\]

to two coordinates while preserving the same sum.

Therefore the total source response does not determine:

- mediator count;
- local mediator stress;
- absorber-channel identity;
- which channel formed a candidate record; or
- the provenance of one local response contribution.

One may select a local decomposition by supplying an explicit field
factorization and coupling a local probe to it. That is a legitimate
branch-specific theory. It is not reconstructed from the effective source
kernel.

## 6. Quantum correction: the determinant can respond to the background

For a finite Euclidean Gaussian mediator, exact integration has the form

\[
\int d\phi\;e^{-S(j,\phi;\lambda)}
\propto
\left[\det K(\lambda)\right]^{-1/2}
e^{-S_{\rm eff}(j;\lambda)}.
\tag{16}
\]

Up to convention-dependent constants, the effective action therefore
contains

\[
\Gamma_{\rm eff}(j;\lambda)
=
S_{\rm eff}(j;\lambda)
+\frac12\log\det K(\lambda).
\tag{17}
\]

At one frozen background the determinant is independent of \(j\), so it
cancels from normalized source correlators under the usual fixed-background
contract. But

\[
\frac{d}{d\lambda}\log\det K
=
\operatorname{tr}(K^{-1}K')
\tag{18}
\]

need not vanish.

For the source-equivalent one- and two-channel families in (13),

\[
\frac{d}{d\lambda}\log\det K^{(1)}
=
\frac{k'}k,
\qquad
\frac{d}{d\lambda}\log\det K^{(2)}
=
2\frac{k'}k.
\tag{19}
\]

The extra mediator direction is invisible to the source kernel and visible
to the determinant's background response.

### Exact interpretation

This is not automatically an observable difference. There are three cases:

1. **The mediator is a physical fluctuating degree of freedom.** Its
   determinant is part of the full quantum theory and can contribute to
   background response.
2. **The mediator is an auxiliary representation variable.** Its measure or
   normalization must be defined so that no extra physical determinant is
   introduced.
3. **The difference is removable by admitted local counterterms or vacuum
   normalization.** Then it is absorbed within that frozen renormalization
   contract.

The source kernel alone does not decide which case holds.

The quantum branch-invariance contract must therefore preserve:

\[
\text{source effective action}
+
\text{fluctuation determinant}
+
\text{measure}
+
\text{state}
+
\text{boundary prescription}
+
\text{regulator and counterterms}.
\tag{20}
\]

Dropping one of these and discovering a difference later is not a physical
remainder. It is an incomplete translation.

## 7. Dynamic Unity consequence

The mediator-elimination ladder is now:

```text
same source action at one background
  < same finite background jet
  < same source effective action on a background family
  < same complete quantum effective action
  < same formed records, interventions, access, resources, and capabilities.
```

Each step is strictly stronger. A theorem at one step must not be reported as
if it had reached the next.

The highest-information held-out target after a frozen-background source
match is a background derivative. If it differs, the result locates the
missing interface term. If it agrees after the full effective action is
matched, gravity has absorbed that proposed discriminator and the search must
move to an independently selected local interface or record.

This also clarifies the North Star:

- geometry can test whether a proposed representation map is complete;
- it does not by itself select one representation;
- total stress response is more invariant than a local energy partition;
- a local field record remains branch-relative unless a physical local probe
  survives the full translation; and
- a determinant can carry physical information outside a source-only record
  without constituting a certified observer record.

## 8. What changed

### Learned

1. Exact stationary elimination preserves total classical background response
   when the full background dependence is retained.
2. Equality at one background does not determine even the first background
   derivative.
3. Matching the complete background-dependent source kernel absorbs every
   source-only derivative discriminator.
4. Total background response does not select a local mediator or absorber
   partition.
5. A source-independent Gaussian determinant can be background-dependent and
   therefore cannot be dropped automatically in a gravitational query.
6. Full quantum branch equivalence is a statement about the complete
   effective action and its measure/state/boundary/renormalization contract,
   not only the current kernel.

### Not learned

- that explicit fields or direct action are fundamental;
- that the branches differ empirically;
- that a determinant contribution survives renormalization;
- that a metric, stress tensor, local probe, event, or record was selected;
- that gravity supplies Dynamic Unity's missing record interface;
- that a new physical law or prediction exists; or
- that a successor is ready.

## 9. Exact reopener

Reopen this branch only with one frozen physical theory or experiment that:

1. defines both sides on the same background family;
2. fixes the complete quantum effective action, measure, state, boundary
   conditions, regulator, gauge quotient, and allowed counterterms;
3. matches all admitted source observables without refit;
4. independently forms and accesses a finite held-out background, local
   stress, or mediator-facing target;
5. proves that the target is not recoverable from the complete translated
   action; and
6. yields a finite matched empirical difference or a branch-invariant
   reconstruction theorem.

Until then:

> Treat pointwise source agreement as a frozen-background result, preserve the
> full effective action before asking gravity to discriminate, and treat
> local stress or record partitions as branch-relative.
