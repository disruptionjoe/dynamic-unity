---
title: "Bianconi dissipation influence spectrum"
status: completed_conditional_probe
doc_type: research_result
created: 2026-07-24
wave: SWING-DU-PHY-02
track: A
grade: "OBJECT-FOUND / SELECTOR-OPEN / TRANSIENT-ONLY"
probe: tests/du_bianconi_physical_influence_probe.py
artifact: tests/artifacts/du_bianconi_physical_influence_probe_result.json
predecessor: tests/du_bianconi_completion_robustness_probe.py
---

# Bianconi dissipation influence spectrum

## Verdict

Both tested Bianconi gradient completions construct a live modal influence
object during relaxation:

```text
A_E  = grad_G S
D_E  = Tr(A_E^2)
p_i^E = eig_i(A_E)^2 / D_E

A_AI  = G^(1/2) (grad_G S) G^(1/2)
D_AI  = Tr(A_AI^2)
p_i^AI = eig_i(A_AI)^2 / D_AI .
```

Where `D_X>0`, each `p^X` is nonnegative, normalized, reconstructs the
completion's total action dissipation, and is invariant under simultaneous
orthogonal similarity. This is a constructive result, not a selector result.

The completions disagree strongly on the distribution at the same live state.
Both total dissipations then vanish along their relaxation, and `p` is
undefined at the exact stationary metric. The normalized profile is degree
zero at fixed modal dimension, so even its pathwise limiting shape has no
absolute magnitude or growth law.

**Disposition: `OBJECT-FOUND / SELECTOR-OPEN / TRANSIENT-ONLY`.**

## The constructed object

For the inherited action

```text
S(G) = sigma log det G + Tr[G(log G - log G_ind)] - Tr G
```

the Euclidean gradient is

```text
grad_G S = sigma G^(-1) + log G - log G_ind .
```

The Euclidean completion has
`-dS/dt=Tr[(grad_G S)^2]=D_E`. Under the affine-invariant SPD metric,
`-dS/dt=Tr[(G^(1/2) grad_G S G^(1/2))^2]=D_AI`. The first-variation
errors in the deterministic specimen were `2.21e-8` and `1.90e-7`,
respectively. Across 68 defined profiles, the worst relative modal
reconstruction error was `1.16e-15`.

The live object is therefore:

> the normalized share of instantaneous action dissipation carried by each
> eigenmode of the completion-specific gradient operator.

That wording matters. It is not yet a record influence distribution, a
cosmological observable, or a completion-independent property of the static
action.

## Shared-state completion comparison

The test reuses the exact seeded, non-diagonal, noncommuting `3x3` SPD fixture
from the completion-robustness probe. Its commutator norm is `2.098365`.

| Completion | Total `D` | Raw sorted modal shares |
|---|---:|---|
| Euclidean | `1.400731` | `[0.504816, 0.450657, 0.044527]` |
| Affine-invariant | `4.029030` | `[0.900468, 0.055501, 0.044031]` |

The maximum share difference is `0.395652`. The three inherited concentration
readings all call the affine profile more concentrated, but none is selected by
the action:

| Reading | Euclidean | Affine-invariant | Difference |
|---|---:|---:|---:|
| Participation `Lambda` | `0.678169` | `0.903250` | `+0.225081` |
| Shannon/KL `Lambda` | `0.656121` | `0.821855` | `+0.165734` |
| Gini/Lorenz `Lambda` | `0.771891` | `0.939323` | `+0.167431` |

Agreement among the three readouts on this pair is not independent physical
selection. They are three post-processing functionals applied to a raw profile
that already changes when the mobility metric changes.

## Invariance—and its boundary

For simultaneous `Q in O(3)`,

```text
(G,G_ind) -> (Q G Q^T, Q G_ind Q^T),
```

the matrix functions transform by similarity. Thus each `A_X` transforms by
similarity, and its eigenvalues, `D_X`, and sorted `p^X` are unchanged.

The numerical suite used six independently generated orthogonal specimens:
one reflection with determinant `-1` and five proper rotations. Maximum errors
were:

- action: `2.22e-15`;
- raw shares: `1.83e-15`;
- relative total dissipation: `4.41e-15`.

This is **orthogonal-similarity invariance**, not arbitrary coordinate
invariance. Under the predeclared nonorthogonal congruence control, the action
changed from `-3.402669` to `-6.386748`; the Euclidean raw profile changed by
up to `0.083571`, and the affine profile by up to `0.237181`. The displayed
matrix-log action does not license promoting the result to arbitrary
congruence or nonlinear reparameterization invariance.

## Null and sensitivity checks

The isotropic equal-modal null (`G=1.6 I`, `G_ind=I`) returns

```text
p^E = p^AI = [1/3, 1/3, 1/3]
```

and all three normalized concentration readings are zero.

The object is sensitive to physical/model choices rather than merely to
coordinates:

| Change | Euclidean max share change | Affine max share change |
|---|---:|---:|
| Noncommuting to commuting geometry at fixed spectrum | `0.231229` | `0.427336` |
| Initial eigenspectrum perturbation | `0.198011` | `0.066494` |

It is numerically stable under timestep refinement. At one integrator time
unit, the medium (`dt=0.01`) to fine (`dt=0.005`) raw-profile changes were
`0.000333` for Euclidean and `0.002142` for affine-invariant flow; both were
smaller than their coarse-to-fine differences. Every tested fixed-step and
Armijo trajectory remained SPD and descended the associated action.

No `rho`, `Lambda`, target distribution, target concentration, or amplitude
was fitted.

## Near stationarity: three different answers

“Does concentration persist?” has to separate three objects.

1. **Normalized shape at finite `D`: pathwise persistent in this specimen.**
   The slowest-decaying modal direction comes to dominate. Immediately before
   the numerical stationarity cutoff, the profiles are:

   ```text
   p^E  = [0.999999677, 0.000000323, 2.89e-14]
   p^AI = [0.999999788, 0.000000212, 1.73e-15].
   ```

   This is an observed limiting direction in the tested local basin, not a
   proof of a universal limit across actions, dimensions, or mobilities.

2. **Absolute dissipation: transient.** The terminal ratios are
   `D_E/D_E(0)=2.08e-15` and `D_AI/D_AI(0)=3.75e-16`. The apparently
   concentrated normalized shape multiplies an action-descent rate that is
   disappearing.

3. **Exact stationary distribution: undefined.** At the shared stationary
   metric, `D=0` and every modal contribution is zero. The expression is
   `0/0`; the artifact records `raw_normalized_weights: null` for both
   completions.

The predeclared `TRANSIENT-ONLY` disposition therefore applies: a normalized
shape remains along the approach, but no nonzero absolute influence survives
and no distribution exists at the endpoint.

## Why the normalized shape is not a physical scale

For any nonzero scalar `c`,

```text
p_i(c A) = p_i(A)
D(c A) = c^2 D(A).
```

The executable scale control verifies this identity at `c=0.1, 3, 10` with a
maximum raw-share error of `3.33e-16`. Modal dimension is fixed at `n=3`.
Consequently:

- `p` has no units and no absolute magnitude;
- it supplies no `N`-dependence or growth law;
- a persistent point-like shape cannot by itself become nonzero `Lambda`;
- only `D`, with a justified physical normalization and units, could carry an
  absolute scale—and here `D` vanishes.

This closes a tempting overinterpretation: concentration of *relative decay
shares* is not persistence of physical influence.

## Comparative-abduction result

The Bianconi action explains an instantaneous modal decomposition with no
fitted concentration target. That is genuine constructive progress. It does
not yet abductively prefer a full CONCEPT-DU-001 realization because:

- Euclidean and affine-invariant mobilities remain unselected;
- the raw profile changes materially between them;
- no conservation, additivity, prediction, or units argument selects
  participation, Shannon/KL, or Gini/Lorenz;
- the exact stationary object is undefined;
- the normalized profile is degree zero and fixed-dimensional; and
- the broader arbitrary-congruence invariant is absent.

This is a formalization-local limitation, not a concept-level failure.

## Reproduction

Run in the repository's pinned NumPy `2.5.1` environment:

```bash
.venv/bin/python tests/du_bianconi_physical_influence_probe.py
```

The run passes **16/16** scientific checks and emits a contract-complete
deterministic artifact. Contract completeness means legible and comparable,
not physically true or banked.
