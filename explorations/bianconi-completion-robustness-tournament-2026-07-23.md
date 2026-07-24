---
title: "SWING-DU-SCI-01 Track 1 — Bianconi completion robustness: fixed point survives, half-power is correlation-conditional, mean is unscreened"
status: active_research
doc_type: research_result
created: 2026-07-23
lanes: "1.1 / 1.3 / 2.2 / A.1"
swing: SWING-DU-SCI-01
candidate_id: SWING-DU-SCI-01-T1
probe: tests/du_bianconi_completion_robustness_probe.py
artifact: tests/artifacts/du_bianconi_completion_robustness_probe_result.json
verdict: "PARTIAL — completion-robust local stationary metric and mixing-class half-power; trajectory not selected, observable imported, extensive mean unscreened"
---

# Bianconi completion-robustness tournament

## Outcome

The earlier Bianconi swing remains a real conditional construction, but this
robustness pass narrows its strongest wording.

Two legitimate dissipative dynamics on a genuinely non-diagonal,
noncommuting positive metric reach the same stable stationary equation:

1. the Frobenius/Euclidean entropy gradient; and
2. the affine-invariant Riemannian gradient on the SPD cone.

Their initial vector fields are materially non-collinear, so the variational
action does **not** select a unique trajectory. A conservative isospectral
control moves the metric while preserving the action and does not relax. The
stationary target is therefore robust across the two dissipative mobilities,
while a physical time law remains a completion choice.

The fluctuation result is sharper:

> Extensivity alone does not force `Lambda_eff ~ N^-1/2`.

The half-power follows for independent or sufficiently mixing,
finite-variance local contributions—equivalently when
`Var(sum_i X_i)=Theta(N)`. Long-range nonsummable correlations change the
exponent, and one global mode removes the suppression entirely.

Finally, neither tested completion screens the extensive vacuum mean. Exact
block replication leaves a constant nonzero mean density. The Sorkin-style
step "subtract the mean and retain the fluctuation" remains imported.

## Typed warrant ledger

| Warrant | Earned | Not earned |
|---|---|---|
| `DERIVED` | Both gradient vector fields descend the same action; the Toeplitz covariance formula fixes each tested fluctuation exponent. | A unique physical mobility, cosmological response, or subtraction rule. |
| `CONDITIONALLY_ENTAILED` | Summable local covariance entails the half-power; long-range and global covariance entail different exponents. | An unconditional half-power from the trace term alone. |
| `CONSTRUCTIVELY_REALIZED` | Two non-collinear SPD flows, a conservative control, four covariance classes, and a no-screening replication control are executable. | Cell issuance, finality, or observed dark energy. |
| `ABDUCTIVELY_PREFERRED` | **Not earned.** The tested action does not choose Euclidean over affine-invariant mobility. | A preferred dynamics or physical Lambda identification. |

These warrants answer different questions; the constructive result does not
erase the conditional assumptions.

## Completion tournament

For

```text
S(G) = sigma log det G + Tr[G(log G - log G_ind)] - Tr G
grad_E S = sigma G^-1 + log G - log G_ind,
```

the tested completions were

```text
dot G_E  = -grad_E S
dot G_AI = -G (grad_E S) G.
```

The second is the gradient under the affine-invariant metric on positive
matrices. An exponential-map update preserved positivity.

On the three-dimensional noncommuting fixture:

| Quantity | Result |
|---|---:|
| Initial `[G,G_ind]` Frobenius norm | `2.098365` |
| Matrix directional-gradient relative error | `1.62e-9` |
| Initial flow-direction cosine | `0.721833` |
| Noncollinearity residual | `0.692067` |
| Euclidean stationary residual | `5.40e-8` |
| Affine-invariant stationary residual | `5.83e-8` |
| Endpoint disagreement | `1.41e-7` |
| Conservative action drift | `4.44e-16` |
| Conservative endpoint displacement | `1.415541` |

The dissipative endpoints agree to the declared float64 stationary tolerance
while their paths do not. The conservative control demonstrates that
"dynamics on the same metric/action" does not by itself imply relaxation.

## Correlation-class result

For stationary covariance `C(r)`,

```text
Var(sum_i X_i) =
    N C(0) + 2 sum_{r=1}^{N-1} (N-r) C(r),
Lambda_eff(N) = sqrt(Var(sum_i X_i)) / N.
```

The tail slopes over `N=128...16384` were:

| Correlation class | Covariance | Measured slope |
|---|---|---:|
| Independent | `C(r>0)=0` | `-0.500000` |
| Short-range mixing | `C(r)=0.65^r` | `-0.499772` |
| Long-range | `C(r)=(1+r)^-0.5` | `-0.245013` |
| Global mode | `C(r)=1` | `0.000000` |

Thus the portable statement is:

> The half-power is robust for summable, finite-variance correlations. It is
> not forced by extensivity without a correlation-class assumption.

This also means the earlier Bianconi and learning/CLT routes are not fully
independent evidence when they reuse the same additive/mixing mechanism.

## Extensive-mean control

At the shared stationary block,

```text
sigma log det G* = 0.1092266.
```

Replicating the block from 3 to 192 cells gives raw-mean slope exactly `+1` and
constant mean density `0.0364089`. Neither mobility changes that stationary
fact.

**No-screening verdict:** the current action and tested completions do not
solve the cosmological-constant mean problem. Continue this leg only if a
separately named constraint or dynamics makes the raw mean subextensive
without hand subtraction.

## Commercial candidate surface

The common harness records:

- 6 labeled assumptions;
- 4 free choices with sensitivity tests;
- 4 observables, 2 nulls, and 4 falsifiers;
- 13/13 executable checks;
- admission `CONDITIONAL_CANDIDATE`;
- `scientific_endorsement: false`.

The artifact is comparable to Tracks 2 and 3; contract completeness does not
promote its physics.

## Heterodox failure scope and stop conditions

This is one Bianconi/SPD formalization adjacent to `CONCEPT-DU-001`. Failure of
a mobility, covariance class, or screening proposal is
`FORMALIZATION`-local. It does not close the broader influence-redistribution
concept.

The route should now obey three stops:

1. do not call the trajectory selected until a physical mobility principle
   distinguishes the completions;
2. do not call `-1/2` forced without the summable-correlation condition; and
3. stop the mean-screening leg unless a predeclared constraint makes the raw
   mean subextensive.

Only after one of those additions earns a new discriminator should a
cell-accretion/growing-complex extension be attempted. That prevents the wild
frontier extension from hiding the unresolved fixed-substrate debit.

## Reproduction

From the repository root:

```bash
.venv/bin/python tests/du_bianconi_completion_robustness_probe.py
```

The deterministic artifact is
`tests/artifacts/du_bianconi_completion_robustness_probe_result.json`.
