---
title: "Record/Fisher influence leverage — a GL-invariant live object with measure-dependent persistence"
status: active_research
doc_type: research_result
created: 2026-07-24
lane: "1.3 / 2.2 / 4.4 / A.1"
swing: SWING-DU-PHY-02
candidate_id: DU-PHY-02-TB-RECORD-FISHER
probe: tests/du_record_fisher_influence_probe.py
artifact: tests/artifacts/du_record_fisher_influence_probe_result.json
admission: CONDITIONAL_CANDIDATE
verdict: "OBJECT-FOUND / SELECTOR-OPEN / DATA-MODEL-CONDITIONAL / MEASURE-DEPENDENT-PERSISTENCE"
---

# Record/Fisher influence leverage

## Outcome

Track B constructs a live, nonnegative, normalized, record-native influence
distribution on the nonzero-score domain:

```text
L_N(theta) = (1/2N) sum_i (theta-r_i)^T Sigma^-1 (theta-r_i)
s_i          = Sigma^-1 (r_i-theta)
I_N          = N Sigma^-1
ell_i        = s_i^T I_N^-1 s_i
             = (1/N)(r_i-theta)^T Sigma^-1(r_i-theta)
p_i^F        = ell_i / sum_j ell_j .
```

It is invariant under the declared full linear coordinate group `GL(d)` when
`theta`, the records, and `Sigma` transform together. It needs no fitted
`rho`, `Lambda`, amplitude, or target concentration.

That earns **OBJECT-FOUND**, not a selector or cosmological observable.
Expected Fisher contribution is uniform for iid identical records, while
observed score leverage is sample-dependent. Under iid growth:

- participation and Shannon/KL amplitude readings vanish as `N^-1/2`;
- their enhancements over the uniform baseline also vanish as `N^-1/2`;
- the maximum individual record share vanishes faster in the measured range;
- Gini retains the nonzero *relative inequality* of the score distribution.

The last disagreement is scientifically useful. The same physical weight
vector does not choose which concentration functional represents a physical
scale. Gini persistence cannot be called persistent cosmological influence
while every individual share vanishes.

## What is—and is not—being decomposed

For common `Sigma`,

```text
ell_i = q_i/N,
q_i   = (r_i-theta)^T Sigma^-1(r_i-theta),
sum_i ell_i = 2 L_N.
```

More generally,

```text
sum_i ell_i
  = tr(I_total^-1 sum_i s_i s_i^T).
```

This is an exact decomposition of **observed residual/score energy measured in
the total Fisher metric**. It is not an exact decomposition of Fisher
information itself.

That distinction matters. For iid identical records,

```text
I_i = Sigma^-1,
tr(I_N^-1 I_i) = d/N
```

for every record. The expected Fisher contribution is therefore uniform.
Also, `E[s_i s_i^T]=I_i`, so `E[ell_i]=d/N`; by exchangeability,
`E[p_i^F]=1/N`. But a realized batch has unequal score norms and hence unequal
observed leverage.

For the `N=16`, `d=4` Monte Carlo control:

- exact expected normalized share: `0.0625`;
- standard deviation of observed shares: `0.04176`;
- one batch ranged from `0.00836` to `0.15211`.

Uniform expectation and nonuniform observation are different statements, not
competing interpretations of one quantity.

## Exact coordinate statement

The tested group is not merely orthogonal similarity. For any invertible
linear map `A`:

```text
theta' = A theta
r_i'   = A r_i
Sigma' = A Sigma A^T
s_i'   = A^-T s_i
I_N'   = A^-T I_N A^-1
I_N'^-1 = A I_N^-1 A^T.
```

Therefore:

```text
ell_i'
  = s_i'^T I_N'^-1 s_i'
  = s_i^T I_N^-1 s_i
  = ell_i.
```

A non-orthogonal `GL(4)` transform with condition number `11.43` changed:

- individual leverages by at most `1.58e-15`;
- normalized weights by at most `2.98e-16`;
- the named loss by `1.55e-15`.

The dynamics was hardened separately. The declared completion is the natural
gradient in the **per-record** Fisher metric:

```text
theta_dot = -Sigma grad_theta L_N = -(theta-rbar).
```

Its unit time normalization is conventional. It is used because the Euclidean
vector gradient would be coordinate-dependent. Jointly transforming the whole
path gives

```text
theta'(t)
  = A rbar + exp(-t)(A theta_0-A rbar)
  = A theta(t).
```

Across all sampled times, the executable transformed-path check found:

- maximum path equivariance error: `5.09e-16`;
- maximum path weight error: `2.98e-16`;
- maximum path loss error: `2.66e-15`.

## Null, iid, heteroskedastic, and outlier cases

### Equal-radius and zero-score nulls

Eight records at equal Mahalanobis radius gave exactly uniform influence:

```text
p_i^F = 1/8,
Lambda_participation = Lambda_Shannon = Lambda_Gini = 1/sqrt(8).
```

If every record equals `theta`, every score and leverage vanishes. The
normalizer is zero, so `p_i^F` is undefined. The probe does not fill that limit
with a preferred uniform distribution.

### Iid observed records

A representative `N=64`, `d=4` iid batch produced:

| Reading | Uniform baseline | Observed |
|---|---:|---:|
| participation amplitude | `0.125000` | `0.150021` |
| Shannon/KL amplitude | `0.125000` | `0.139438` |
| endpoint-matched Gini reading | `0.125000` | `0.451195` |
| maximum record share | `0.015625` nominal | `0.045433` |

This is ordinary realized score variation. It is not evidence of a
macroscopic preferred record.

### Common-rescaling and exact-duplication nulls

Multiplying every raw leverage by `37` multiplied the raw normalizer by `37`
and changed no normalized weight. Thus `p_i^F` retains shape but discards the
common score-energy magnitude exactly.

Duplicating every record four times—without adding independent
evidence—assigned `p_i/4` to each copy:

```text
participation amplitude ratio = 1/2
Shannon amplitude ratio       = 1/2
native Gini change            < 2e-14
```

The normalized profile cannot distinguish independent accretion from exact
copies. Any information-growth reading must therefore be carried separately
by the data model and raw scale ledger, not inferred from `p` alone.

### Known heteroskedastic extension

The minimal declared extension uses known record-specific covariance:

```text
I_total = sum_i Sigma_i^-1,
ell_i   = s_i^T I_total^-1 s_i.
```

Three equal-size groups used covariance multipliers `0.25`, `1`, and `4`.
Their observed group shares were:

| Covariance multiplier | Expected mean weight per record | Observed group share |
|---:|---:|---:|
| `0.25` | `0.007619` | `0.774224` |
| `1.00` | `0.001905` | `0.175884` |
| `4.00` | `0.000476` | `0.049892` |

More precise records carry greater expected Fisher contribution. Thus
uniformity is conditional on iid *identical* records; it is not invariant
under changing the data model. The covariance model remains imported.

### Outlier control

Replacing one whitened residual in a matched `N=64` batch by radius `12`
changed the data, not the weight equation. That record received share
`0.395350`, and all three readings increased:

| Reading | Matched batch | With outlier |
|---|---:|---:|
| participation amplitude | `0.152689` | `0.406227` |
| Shannon/KL amplitude | `0.140853` | `0.219889` |
| endpoint-matched Gini reading | `0.465364` | `0.667003` |

Observed leverage is consequently sensitive to high-score records. No outlier
rate was fitted or promoted into the model.

## Flow and accretion

Along the per-record-Fisher-natural path, the loss descended from `6.84548` to
`2.45923`. The leverage vector moved by `L1=0.51657` and settled to within
`3.42e-4` between `t=8` and `t=16`. This shows that leverage is a live
`theta`-dependent object. Concentration is not assumed to be a Lyapunov
observable merely because the loss is.

For record accretion, the relaxed estimator followed the exact online update:

```text
theta_hat_N
  = theta_hat_(N-1) + (r_N-theta_hat_(N-1))/N.
```

A declared early outlier's share fell:

```text
N=16:    0.652748
N=4096:  0.008632
```

The tail slope was `-0.93495`, for a `75.62x` dilution. A fixed high-score
record does not sustain a nonzero individual scale under iid accretion.

## Large-N selector result

For iid Gaussian records at the true parameter with `d=4`, whitened score
energy is

```text
q_i ~ chi-square_4,
p_i = q_i / sum_j q_j.
```

Across 128 trials at each of nine sizes from `N=32` through `8192`:

| Quantity | Measured scaling/limit | Exact asymptotic reference |
|---|---:|---:|
| participation amplitude slope | `-0.49844` | `-1/2` |
| Shannon/KL amplitude slope | `-0.49935` | `-1/2` |
| participation enhancement slope | `-0.49135` | `-1/2` |
| Shannon enhancement slope | `-0.49390` | `-1/2` |
| maximum-share slope | `-0.87120` | tends to zero |
| Gini slope | `+0.00509` | `0` |
| participation `N_eff/N` at `8192` | `0.666592` | `2/3` |
| Shannon `N_eff/N` at `8192` | `0.794915` | `0.794822` |
| Gini at `8192` | `0.374828` | `3/8` |

At `N=8192`, mean maximum share was only `0.000750`. Participation and
Shannon amplitudes were `0.013533` and `0.012392`; both are finite-sample
`N^-1/2` objects. The endpoint-matched Gini reading remained `0.381781`
because Gini measures the relative inequality of the nondegenerate
`chi-square_4` score population.

So the physical object does not resolve the proxy tournament by itself:

- participation asks about the quadratic effective count;
- Shannon asks about information-effective count;
- Gini asks about relative rank inequality;
- all operate on the same generated `p_i^F`;
- they answer differently about persistence.

No independent conservation law, additivity property, or prediction in this
track privileges one of them.

## Warrant ledger

| Warrant | Earned content |
|---|---|
| `DERIVED` | Common-covariance `ell_i=q_i/N`, `sum ell_i=2L_N`, and `GL(d)` invariance follow from the stated equations. |
| `CONDITIONALLY_ENTAILED` | Given the score-leverage interpretation and declared record model, null, outlier, flow, and scaling consequences follow. |
| `CONSTRUCTIVELY_REALIZED` | A deterministic executable object passes null, perturbation, flow, accretion, reparameterization, and large-`N` checks. |
| `STRUCTURAL_ANALOGY` | Fisher/loss geometry supplies a DU-native record influence candidate; no identity with cosmological `Lambda` is established. |
| `ABDUCTIVELY_PREFERRED` | **Not earned.** The candidate does not select a concentration functional or beat Track A before cross-track comparison. |

## Commercial-style accounting

The shared candidate contract is `COMPLETE`, meaning legible and comparable,
not physically true. It exposes:

- 7 assumptions;
- 5 material free choices;
- 7 observables;
- 5 null models;
- 7 falsifiers;
- 30 executable checks, all passing.

The imported or conditional pieces remain visible: the score-leverage
interpretation, record covariance/data law, natural-gradient kinetic
completion, record dimension, control cases, and finite computational grid.

## Disposition and stop rule

The honest Track B disposition is:

> **OBJECT-FOUND / SELECTOR-OPEN / DATA-MODEL-CONDITIONAL /
> MEASURE-DEPENDENT-PERSISTENCE**

Continue only through the predeclared Track C comparison or a genuinely
independent DU conservation/prediction criterion. Stop rather than:

- call residual-energy leverage a decomposition of Fisher information;
- replace the zero-score limit with hand-selected weights;
- fit `rho`, `Lambda`, an amplitude, outlier rate, or target concentration;
- infer independent information or an absolute scale from normalization or
  exact record duplication;
- call finite-sample participation/Shannon enhancement a persistent scale;
- call Gini's relative inequality a persistent cosmological influence; or
- promote observed score leverage to the cosmological observable without a
  new discriminator.

This result supports the concept at formalization level and leaves its physical
interpretation open. It promotes no claim or prediction.

## Reproduction

From the repository root:

```bash
.venv/bin/python tests/du_record_fisher_influence_probe.py
```

Verified result: **30/30 checks pass**, NumPy `2.5.1`, contract `COMPLETE`,
artifact written deterministically with raw normalized weights for Track C.
