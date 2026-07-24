---
title: "SWING-DU-PHY-02 contract — physical influence objects and selector/persistence kill"
status: active_research_swing
doc_type: experiment_contract
created: 2026-07-24
lanes: "1.3 / 2.2 / 4.4 / A.1"
directed_by: "Joe direct chat, 2026-07-24"
method: lab/process/conditional-and-abductive-research-contract.md
predecessor: explorations/science-council-three-track-swing-synthesis-2026-07-23.md
---

# SWING-DU-PHY-02 contract

## Decision question

Can a live Dynamic Unity construction supply a nonnegative, normalized,
coordinate-invariant influence distribution and thereby select a concentration
functional or sustain nonzero concentration **without fitting** `rho`, `Lambda`,
or a target concentration?

This wave physicalizes the only live lead from `SWING-DU-SCI-01`. It does not
reopen the Bianconi coefficient/mean search or the finality-knee fit.

## Shared admission boundary

A candidate influence distribution is admitted only where all of the following
are explicit:

1. the live dynamical object from which it is computed;
2. the scalar decomposition whose nonnegative contributions are normalized;
3. the coordinate-change group under which the contributions are invariant;
4. the domain where the normalizing scalar is nonzero;
5. all imported geometry, initial data, and completion choices;
6. the uniform/null case and at least one legitimate perturbation;
7. transient versus persistent concentration; and
8. a comparison with participation, Shannon/KL, and Gini/Lorenz readings.

“Basis-invariant” must name a group. Orthogonal-similarity invariance is not
silently promoted to arbitrary-congruence or nonlinear-reparameterization
invariance. Undefined zero-dissipation limits are reported as such rather than
filled with a preferred distribution.

Contract completeness remains legibility, not physical truth.

## Track A — Bianconi dissipation spectrum

Use the already-tested non-diagonal SPD Bianconi action and both dissipative
completions from `tests/du_bianconi_completion_robustness_probe.py`.

For the Euclidean completion, test the modal decomposition

```text
A_E = grad_G S
D_E = tr(A_E^2)
p_i^E = eig_i(A_E)^2 / D_E .
```

For the affine-invariant completion, test

```text
A_AI = G^(1/2) (grad_G S) G^(1/2)
D_AI = tr(A_AI^2)
p_i^AI = eig_i(A_AI)^2 / D_AI .
```

These are candidate dissipation-share distributions wherever `D>0`.

Required checks:

- nonnegativity, normalization, and reconstruction of the total dissipation;
- invariance under independently generated orthogonal changes of basis;
- action descent for the associated completion;
- sensitivity to noncommuting initial geometry, eigenspectrum, and timestep;
- agreement or disagreement between Euclidean and affine completions on the
  existing concentration measures;
- behavior approaching the stationary metric, where `D -> 0`;
- an isotropic or equal-modal null; and
- no fitted `rho`, `Lambda`, or target distribution.

Passing this track constructs a live influence object. It does not select the
physical completion.

## Track B — record-score/Fisher-metric leverage

Use the named finality-consistency empirical loss from
`tests/du_loss_lambda_criticality_probe.py`, generalized only as far as needed
to expose a nontrivial vector record object:

```text
L_N(theta) = (1/2N) sum_i (theta-r_i)^T Sigma^-1 (theta-r_i).
```

The predeclared per-record candidate is observed score leverage in the total
Fisher metric:

```text
s_i = Sigma^-1 (r_i-theta)
I_N = N Sigma^-1
ell_i = s_i^T I_N^-1 s_i
p_i^F = ell_i / sum_j ell_j .
```

Required checks:

- nonnegativity, normalization, and the exact observed residual-energy
  decomposition `sum_i ell_i = 2 L_N`;
- invariance under invertible linear reparameterizations when `theta`, records,
  and `Sigma` transform together;
- distinction between expected Fisher contribution (uniform for iid identical
  records) and observed score leverage (sample-dependent and **not** a
  decomposition of expected Fisher information);
- equal-radius/null records, iid records, correlated or heteroskedastic
  sensitivity, and an outlier control;
- behavior along a Fisher-natural-gradient flow and under record accretion;
  any Euclidean-gradient comparison must expose its coordinate choice rather
  than inherit the pointwise leverage invariant;
- finite-`N` versus large-`N` scaling of all three concentration readings; and
- no amplitude, `rho`, `Lambda`, or target concentration inserted into the
  record weights.

Passing this track constructs a record-native influence object. It does not
establish that observed score leverage is the cosmological observable.

## Track C — selector and persistence kill

Compare Tracks A and B on one receipt without assigning a scalar council score.

The comparison must answer:

1. Do the physical candidates choose the same ordering on profiles that the
   proxy tournament left incomparable? This question is answered only if both
   old profiles are explicitly embedded into each candidate's physical state
   space and an independent response functional supplies an ordering.
   Otherwise report `NOT_IDENTIFIED`; a physical candidate outputs a profile,
   not an ordering rule over arbitrary profiles.
2. Does either candidate privilege participation, Shannon/KL, or Gini/Lorenz
   through an independent conservation, additivity, or prediction criterion?
3. Is any nonuniform concentration persistent in the candidate's own physical
   time/accretion variable, rather than merely present in a normalized
   transient?
4. Does a nonzero absolute scale survive growth, or only an `O(N^-1/2)`
   finite-sample enhancement over the uniform baseline?
5. Which disagreements trace to a completion, data model, metric, initial
   condition, or to the concept invariant itself?

No majority vote, persona count, check count, or contract-completeness count is
scientific evidence.

### Pre-result audit correction

The independent Track C audit was applied before either construction reported:

- With common covariance,
  `ell_i=(r_i-theta)^T Sigma^-1(r_i-theta)/N` and
  `sum_i ell_i=2L_N`. The name “Fisher-metric leverage” refers to the metric
  used for contraction; it is not an additive Fisher-information share.
- Pointwise `ell_i` is invariant under joint invertible linear
  reparameterization, but an ordinary Euclidean gradient flow is not generally
  equivariant under that group. A coordinate-covariant dynamics must use the
  corresponding natural-gradient mobility.
- A normalized `p_i` is degree-zero under common rescaling. Neither persistent
  inequality nor persistent normalized modal shape supplies a dimensionful
  nonzero scale without a separately identified raw observable and units map.
- Correlated or heteroskedastic specimens change the simple
  `I_N=N Sigma^-1` model. They must be treated either with an explicit
  generalized information metric or as reference-model stress tests, never as
  silent instances of the iid formula.

## Predeclared dispositions

- **PHYSICAL-SELECTOR-FOUND:** at least one candidate has the declared
  invariance, a non-fitted persistent scale, and an independent reason that
  selects a concentration functional.
- **OBJECT-FOUND / SELECTOR-OPEN:** a live influence object exists, but
  completion/data/metric choices still change the ordering or no functional is
  independently selected.
- **TRANSIENT-ONLY:** normalized concentration exists but vanishes, becomes
  undefined, or scales away in the physical limit.
- **FORMALIZATION-LOCAL-FAIL:** a candidate violates its own declared
  decomposition or invariance; this does not kill `CONCEPT-DU-001`.
- **CONCEPT-PRESSURE:** materially diverse live candidates fail for a common
  reason traced to the predeclared concept invariant. This is not
  `CONCEPT-FALSIFIED` without the contract's concept-level closure rule.

## Stop conditions

Stop the wave rather than repair it by:

- choosing weights because they reproduce a favored proxy;
- replacing a zero-dissipation limit with a hand-selected distribution;
- fitting `rho`, `Lambda`, an outlier rate, or a concentration target;
- treating coordinate dependence as physical concentration;
- calling finite-sample leverage a persistent cosmological scale;
- averaging completion disagreement away; or
- reopening the finality knee without a new finality-specific observable.

## Deliverables

- one deterministic Track A probe, artifact, and interpretation;
- one deterministic Track B probe, artifact, and interpretation;
- one deterministic Track C comparison, artifact, and synthesis;
- live updates to the concept register and `LANES.yaml`; and
- no claim promotion, prediction seeding, or external publication.
