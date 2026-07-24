---
title: "SWING-DU-PHY-02 synthesis — live influence objects found, selector and physical scale remain open"
status: completed_research_swing
doc_type: synthesis
created: 2026-07-24
lanes: "1.3 / 2.2 / 4.4 / A.1"
directed_by: "Joe direct chat, 2026-07-24"
contract: explorations/physical-influence-selector-wave-contract-2026-07-24.md
pre_result_audit: explorations/physical-influence-selector-adversarial-audit-2026-07-24.md
track_a: explorations/bianconi-dissipation-influence-spectrum-2026-07-24.md
track_b: explorations/record-fisher-influence-leverage-2026-07-24.md
comparison_probe: tests/du_physical_influence_selector_comparison.py
comparison_artifact: tests/artifacts/du_physical_influence_selector_comparison_result.json
verdict: "OBJECTS FOUND / SELECTOR OPEN / NO NONZERO PHYSICAL SCALE IDENTIFIED — no claim banked or seeded"
---

# SWING-DU-PHY-02 synthesis

## Executive result

The wave executed the highest-leverage successor to `SWING-DU-SCI-01`:
replace hand-selected influence proxies with distributions extracted from live
Dynamic Unity constructions, then ask whether the constructions select a
functional or sustain a nonzero physical scale.

The physicalization step succeeded. The selector and scale steps did not:

| Candidate | Constructive result | Limitation | Disposition |
|---|---|---|---|
| Bianconi Euclidean dissipation shares | Exact nonnegative `O(3)`-invariant decomposition of instantaneous action dissipation on `D_E>0` | Completion unselected; `D_E -> 0`; exact stationary profile undefined; no native growth law | `OBJECT-FOUND / NORMALIZED_RESIDUE_AT_ZERO_ACTIVITY / SCALE_UNASSESSED` |
| Bianconi affine-SPD dissipation shares | Exact nonnegative `O(3)`-invariant decomposition of the affine completion's dissipation on `D_AI>0` | Profile differs from Euclidean completion; `D_AI -> 0`; exact stationary profile undefined; no native growth law | `OBJECT-FOUND / NORMALIZED_RESIDUE_AT_ZERO_ACTIVITY / SCALE_UNASSESSED` |
| Record score-energy/Fisher-metric leverage | Exact nonnegative `GL(d)`-invariant observed residual-energy distribution on nonzero-score batches | Not a Fisher-information decomposition; data law and mobility conditional; functional-dependent asymptotics; no cosmological units map | `OBJECT-FOUND / DATA-MODEL-CONDITIONAL / SCALE_UNASSESSED` |

The comparison returns:

> **`OBJECT-FOUND / SELECTOR-OPEN /
> NO-NONZERO-PHYSICAL-SCALE-IDENTIFIED`.**

That is a real positive construction plus a hard stopping result. It is not a
failure of `CONCEPT-DU-001`, and it is not permission to add another proxy.

No claim reaches bank review, prediction seeding, or external publication.

## The pre-result audit changed the build

The independent audit found two load-bearing defects before the result probes
were accepted:

1. The record candidate

   ```text
   ell_i = s_i^T I_N^-1 s_i
   ```

   decomposes observed Mahalanobis residual energy:

   ```text
   ell_i = q_i/N
   sum_i ell_i = 2 L_N.
   ```

   It does **not** decompose the Fisher-information matrix. Expected Fisher
   contribution remains uniform for iid identical records.

2. A physical construction outputs a profile; it does not automatically order
   the incomparable profiles from the prior proxy tournament. Such an ordering
   requires an explicit embedding, matched raw carrier and controls, and a
   held-out physical response functional.

The contract was corrected before results. Track B then used a
Fisher-natural-gradient trajectory so the dynamics, not only the pointwise
weights, is covariant under the declared linear coordinate group. Track C
records the old incomparable-pair question as `NOT_EVALUABLE`, not as
agreement, disagreement, or a proxy vote.

This is the philosopher-of-science move made operational: expose when the
question itself is under-specified rather than forcing a result.

## Track A — Bianconi dissipation object

For the tested action,

```text
S(G) = sigma log det G + Tr[G(log G-log G_ind)] - Tr G,
```

the two already-admitted dissipative completions give:

```text
A_E  = grad_G S
D_E  = Tr(A_E^2)
p_i^E = eig_i(A_E)^2 / D_E

A_AI  = G^(1/2) (grad_G S) G^(1/2)
D_AI  = Tr(A_AI^2)
p_i^AI = eig_i(A_AI)^2 / D_AI.
```

Each distribution exactly reconstructs its completion's instantaneous action
dissipation and is invariant under simultaneous orthogonal similarity. The
numerical suite includes a reflection. It also demonstrates that arbitrary
nonorthogonal congruence is outside the action's invariance group.

At the same noncommuting live state:

```text
p_E  = [0.504816, 0.450657, 0.044527]
p_AI = [0.900468, 0.055501, 0.044031].
```

The maximum share difference is `0.395652`. Participation, Shannon/KL, and
Gini/Lorenz all rank the affine profile as more concentrated on this pair, but
that agreement does not select either mobility or any functional.

Along relaxation:

```text
D_E(end)/D_E(0)   = 2.08e-15
D_AI(end)/D_AI(0) = 3.75e-16.
```

The normalized profiles become almost point-like because the slowest decaying
direction dominates. At the exact shared stationary metric every contribution
is zero, so `p=0/0` and is left undefined.

The result is therefore a normalized residue at zero activity, not persistent
absolute influence.

## Track B — record score-energy object

For the named vector finality-consistency loss,

```text
L_N(theta) = (1/2N) sum_i (theta-r_i)^T Sigma^-1(theta-r_i),
```

the live record profile is:

```text
s_i   = Sigma^-1(r_i-theta)
I_N   = N Sigma^-1
ell_i = s_i^T I_N^-1 s_i
p_i^F = ell_i / sum_j ell_j.
```

The distribution is invariant under joint invertible linear transformations of
`theta`, records, and `Sigma`. The full Fisher-natural-gradient path passes the
same covariance check. Equal-radius records give uniform weights; zero-score
records leave the profile undefined; heteroskedastic and outlier controls show
that the profile responds to declared data-model changes.

A fixed early outlier is diluted under iid record accretion:

```text
share at N=16    0.652748
share at N=4096  0.008632
tail slope       -0.93495.
```

For iid Gaussian records with `d=4`, the comparison independently recovers:

```text
participation slope       -0.499583
Shannon/KL slope          -0.499918
native Gini slope         +0.001855
maximum-share slope       -0.881292

sqrt(N) participation     1.224173  (theory 1.224745)
sqrt(N) Shannon/KL        1.121322  (theory 1.121670)
native Gini               0.374389  (theory 0.375).
```

Participation and Shannon are finite-sample `N^-1/2` amplitudes. Native Gini
retains relative inequality while every individual share vanishes. The prior
endpoint map that turns Gini into a quantity named `Lambda` therefore creates
its nonzero limit by definition; the record dynamics does not select it.

## Track C — no hidden selector

Track C keeps Euclidean Bianconi, affine Bianconi, and record score energy as
three separate receipts. It does not average completions or convert checks into
a score.

### Replication result

Identical replication of either Bianconi transient profile gives the exact
signature:

```text
raw D                 K^(+1)
participation         K^(-1/2)
Shannon/KL            K^(-1/2)
native Gini           K^(0)
maximum share         K^(-1).
```

Thus the participation/Shannon versus Gini split is not peculiar to the
Gaussian record model. It follows whenever a fixed nonuniform profile is
replicated. Constant Gini means persistent relative shape, not a nonzero share
or physical amplitude.

### Shape and scale are separate ledgers

For raw contributions `a_i`,

```text
p_i = a_i / sum_j a_j
```

is homogeneous of degree zero. No statistic of `p` alone can recover the raw
magnitude, units, or physical clock rate discarded by normalization.

- Bianconi carries raw action dissipation, but it vanishes under relaxation
  and lacks a native growth law.
- Record leverage carries dimensionless mean residual energy, but no
  unit-bearing map to a cosmological observable is supplied.
- Gini carries shape inequality; participation and Shannon carry
  finite-sample amplitudes.

None supplies a non-fitted nonzero physical `Lambda`.

### The old incomparable pair

The prior pair

```text
[37,1,1,1] / 40
[36,4,0,0] / 40
```

is still mathematically incomparable under majorization. It is **not**
physically ordered here because the wave contains no:

- embedding into all three candidate state spaces;
- matched raw carrier and initial controls; or
- independent response observable.

Track C correctly records `NOT_EVALUABLE / NOT_IDENTIFIED`.

## Council moves realized

### Commercial scientist

The wave produced executable objects and receipts rather than another
discussion:

- 16/16 Track A checks;
- 30/30 Track B checks;
- 24/24 Track C execution checks;
- deterministic artifacts with pinned NumPy `2.5.1`.

The counts establish execution, not scientific truth.

### Philosopher of science

The work separated:

- expected information from observed residual energy;
- normalized shape from a unit-bearing scale;
- coordinate invariance from a broader unearned covariance claim;
- an undefined ordering question from a negative result; and
- formalization-local limits from concept-level failure.

### Heterodox professor

Conditional construction was allowed to succeed on its own terms. The result
does not become worthless because no microscopic derivation was supplied:
three live normalized objects were built. Equally, their constructive success
does not erase their imported mobilities, data laws, or missing observable
maps.

## Concept disposition

`CONCEPT-DU-001` gains stronger formalization-level support:

- live DU-linked dynamics can generate nonuniform influence distributions
  without fitting a target concentration;
- the constructions survive their declared algebra and coordinate groups; and
- local limitations do not trace to the concept invariant itself.

But the concept does not yet identify physical dark energy:

- no independent law chooses participation, Shannon/KL, or Gini/Lorenz;
- no common physical observable orders the old incomparable pair;
- no unit-bearing nonzero scale survives; and
- no value of `Lambda` is sourced.

Updated status:

> **`CONCEPT-SUPPORTED-BY-LIVE-OBJECTS /
> SELECTOR-OPEN / SCALE-OPEN / VALUE-OPEN`.**

## Portfolio decision — stop this branch and pivot

The bounded physicalization build has now been executed. Further proxy,
coefficient, `rho`, or normalized-profile work does not count as progress.

There is one legitimate reopener:

> Supply an independently motivated physical response law, explicitly embed a
> held-out incomparable pair at matched raw carrier, and provide a unit-bearing
> map from the winning response to the proposed observable.

Without all three, the influence branch stays stopped.

The next major Dynamic Unity construction returns to the already-prioritized
coupled `HC-DU-011 + HC-DU-022` object:

> a label-invariant order-first causal growth/action law whose
> past-cardinality feeds back, reconstructs geometry, and endogenously
> generates a dimensional memory scale before cosmological calibration.

This is a pivot, not a claim that the influence concept failed. It implements
Joe's preference not to circle one object without a buildable breakthrough.

The finality knee remains stopped pending a finality-specific observable. The
Bianconi amplitude/mean branch remains stopped pending a native screening or
mobility principle.

## Reproduction

From the repository root:

```bash
.venv/bin/python tests/du_bianconi_physical_influence_probe.py
.venv/bin/python tests/du_record_fisher_influence_probe.py
.venv/bin/python tests/du_physical_influence_selector_comparison.py
```

All probes exit zero and rewrite byte-identical artifacts under the pinned
environment. No result is banked, seeded, or published.
