---
title: "Influence-redistribution abductive tournament — the invariant survives, no proxy wins, and target-free persistence is conditionally realized"
status: active_research
doc_type: research_result
created: 2026-07-23
lane: "2.2 / 1.3"
swing: SWING-DU-SCI-01
candidate_id: DU-SCI-01-T2-INFLUENCE-ABDUCTION
probe: tests/du_influence_redistribution_abduction_probe.py
artifact: tests/artifacts/du_influence_redistribution_abduction_probe_result.json
admission: CONCEPT_SUPPORTED
verdict: "CONCEPT-SUPPORTED-BY-DIVERSE-FORMALIZATIONS / MECHANISM-CONDITIONAL / NO-ABDUCTIVE-WINNER / VALUE-OPEN"
---

# Influence-redistribution abductive tournament

## Outcome

`CONCEPT-DU-001` survives a genuinely plural test, but the test does **not**
select a privileged proxy.

Participation-ratio effective count, Shannon/KL effective count, and
Gini/Lorenz concentration all:

1. recover the `1/sqrt(n)` baseline at uniform influence;
2. reach maximal concentration at a point mass; and
3. increase under every tested majorization ordering.

They nevertheless reverse one another's rankings on **13,266 of 54,994**
majorization-incomparable pairs (**24.123%**) in an exhaustive finite grid.
That is not an invariant failure: majorization itself is silent on those
pairs. It means the current evidence earns **no abductive winner**.

A separate target-free dynamics does conditionally realize invariant (iv).
Positive frequency-dependent reinforcement opposed by uniform mixing amplifies
an arbitrarily small finite asymmetry into a persistent concentrated fixed
point below a declared local instability. The equation contains no requested
concentration or `Lambda_target`, and the final amplitude is unchanged across
four decades of seed size. But the mechanism and its dimensionless phase ratio
are posits; neither the physical influence object nor the value of Lambda is
sourced.

## The three faithful formalizations

For normalized nonnegative influence weights `p_i`, with
`sum_i p_i = 1`:

| Formalization | Native object | Lambda readout used here | Distinct sensitivity |
|---|---|---|---|
| Participation / Hill `q=2` | `N_eff,2 = 1 / sum_i p_i^2` | `Lambda_2 = 1/sqrt(N_eff,2)` | Emphasizes dominant weights and the second moment |
| Shannon/KL / Hill `q=1` | `H=-sum p_i log p_i`, `D_KL(p||u)=log n-H`, `N_eff,1=exp(H)` | `Lambda_1 = 1/sqrt(N_eff,1)` | Emphasizes information/code length and is more tail-sensitive |
| Gini/Lorenz | normalized area from equal-influence Lorenz line | affine endpoint map from `1/sqrt(n)` to `1` | Emphasizes pairwise transfers and rank dispersion |

The Gini amplitude map is a declared free choice. Only its ordering enters the
comparative-abduction verdict; any strictly increasing remap leaves that
ordering unchanged.

## Result 1 — exact domain of agreement and disagreement

An eight-weight one-peak chain from uniform to a point mass was explicitly
majorization ordered. All three proxies rose strictly along it.

The stronger check enumerated all **632** permutation-quotiented distributions
on the four-weight grid with denominator 40:

- majorization-comparable pairs: **144,402**;
- violations by participation: **0**;
- violations by Shannon/KL: **0**;
- violations by Gini/Lorenz: **0**;
- majorization-incomparable pairs: **54,994**;
- pairs with at least one strict proxy-ranking reversal: **13,266**.

A clean reversal is:

| Profile | Participation Lambda | Shannon/KL Lambda | Gini/Lorenz Lambda |
|---|---:|---:|---:|
| `A=(37,1,1,1)/40` | `0.926013` | `0.839969` | `0.950000` |
| `B=(36,4,0,0)/40` | `0.905539` | `0.849981` | `0.966667` |

`A` has the larger first cumulative share (`0.925 > 0.900`), while `B` has
the larger first-two cumulative share (`1.000 > 0.950`). Neither majorizes the
other. Participation calls `A` more concentrated; Shannon/KL and Gini call
`B` more concentrated. This localizes the unresolved choice precisely: new
physics is needed on incomparable profiles.

## Result 2 — a mechanistic persistence specimen, not a target fit

The tested candidate flow is

```text
dp_i/dt = s p_i (p_i - sum_j p_j^2) + mu (1/n - p_i).
```

The nonlinear first term is self-reinforcing influence; the second is uniform
mixing. Both preserve the simplex. At uniform influence, any zero-sum
perturbation obeys the derived linear relation

```text
d epsilon_i/dt = (s/n - mu) epsilon_i
rho := n mu / s
```

so `rho=1` is the local stability boundary.

For the primary specimen `n=8`, `s=1`, `rho=0.64`:

- measured early growth rate: `+0.04500002`;
- derived rate: `+0.04500000`;
- final participation Lambda: `0.924707`, versus uniform `0.353553`;
- fixed-point residual: `1.53e-16`;
- drift during an additional 200 time units: `0`;
- all three proxies increased monotonically on the sampled path;
- seed sizes `1e-6`, `1e-4`, and `1e-2` reached the same amplitude;
- changing the initially favored coordinate changed identity, not
  permutation-invariant concentration.

Controls and sensitivities also behaved as required:

- `s=0` returned the concentrated state to uniform;
- small perturbations at `rho=1.28` decayed at the derived rate
  `-0.03500000`;
- the same near-uniform phase split held at `n=4,8,16`;
- strong mixing at `rho=3` erased even the concentrated starting state;
- halving the RK4 step changed the reported metrics by at most `3.33e-16`.

The `rho=1` statement is deliberately **local**, not global. At `rho=1.28`,
the uniform state is locally stable but a distant concentrated starting state
remains in a concentrated basin. The model therefore has nonlinear
basin/hysteresis structure that this swing diagnoses but does not fully map.
This does not weaken the below-threshold construction from a tiny asymmetry;
it prevents overclaiming a global unique-phase theorem.

## Typed warrant ledger

The warrant types answer different questions and are not an ordinal score:

| Warrant | Earned content |
|---|---|
| `DERIVED` | The transverse rate `s/n-mu` and local threshold `rho=1` follow from the stated candidate flow. |
| `CONDITIONALLY_ENTAILED` | Given the labeled reinforcement/mixing posit, the below-threshold path entails growth rather than restoration of uniformity. |
| `CONSTRUCTIVELY_REALIZED` | A deterministic executable flow reaches and maintains a nonzero concentrated fixed point and beats its declared controls. |
| `STRUCTURAL_ANALOGY` | Three concentration objects instantiate the influence-redistribution invariant; no physical identity with cosmological Lambda is established. |
| `ABDUCTIVELY_PREFERRED` | **Not earned.** The proxies disagree where majorization is silent, and no independent DU observable chooses among them. |

## Commercial-style accounting

The candidate contract is `COMPLETE`, which means legible and comparable—not
physically true. It exposes **7 assumptions**, **6 free choices**, **7
observables**, **3 nulls**, and **5 falsifiers**.

### Assumptions

| ID | Status | Charge |
|---|---|---|
| `A1` | `STANDARD` | Influence is a finite probability simplex. |
| `A2` | `PROJECT_NATIVE` | Uniform influence carries the `1/sqrt(n)` baseline. |
| `A3` | `STANDARD` | Majorization means unambiguously greater concentration. |
| `A4` | `CONDITIONAL_POSIT` | Proxy values may be read as Lambda amplitudes under the stated maps. |
| `A5` | `CONDITIONAL_POSIT` | Positive frequency dependence is a candidate higher-order mechanism. |
| `A6` | `CONDITIONAL_POSIT` | Uniform mixing is the declared competing process. |
| `A7` | `IMPORTED` | No DU-native identification of `p_i` or derivation of `rho` is supplied. |

### Free choices

| ID | Choice | Sensitivity paid |
|---|---|---|
| `F1` | Three representative proxies | Same endpoints, chains, and incomparable grid for all three |
| `F2` | Endpoint map for Gini | Only remap-invariant rankings used |
| `F3` | Main dimension `n=8` | Repeated at `n=4,8,16` |
| `F4` | Replicator-plus-mixing mechanism | Reinforcement-off and high-mixing controls |
| `F5` | Primary `rho=0.64` | Five-value phase sweep; amplitude variation retained |
| `F6` | Symmetry-breaking seed and RK4 resolution | Four-decade seed, winner, and timestep checks |

## Comparative-abduction verdict

- **Participation** has the best direct compression of the register's existing
  `N_eff` language, but its apparent consilience is not independent of the
  quadratic/variance structure already used by the CLT routes.
- **Shannon/KL** has the cleanest information-geometric decomposition, but it
  becomes physically preferred only if DU supplies a native likelihood,
  coding, or relative-entropy object.
- **Gini/Lorenz** most literally captures deviation from one-record-one-vote,
  but it supplies no canonical Lambda amplitude without an additional map.

There is therefore **no winner**. The progressive result is the smaller
question now exposed: which physical operation should determine sensitivity
to peaks, code length, or pairwise transfers?

## Heterodox locality and stop rules

No formalization failed the invariant. If one later fails a native-physics
test, its failure is `FORMALIZATION`, not `CONCEPT`, unless the failure traces
to monotone mechanistically generated deviation itself or recurs across an
exhausted diverse family.

The proxy tournament now hits a deliberate stop:

> Do not add more concentration measures to manufacture a winner. Reopen the
> ranking only when a DU-native observable or dynamics selects a functional.

The mechanism remains open only conditionally:

> Continue if a program-native influence object identifies `p_i` or derives
> `rho`/an equivalent scale without fitting Lambda. Stop if every next move
> merely retunes `rho`, inserts a concentration target, or swaps proxies after
> an unfavorable result.

Nothing here reaches bank review. The physical Lambda identity and value remain
open.

## Reproduction

From the repository root:

```bash
.venv/bin/python tests/du_influence_redistribution_abduction_probe.py
```

Verified result: **19/19 checks pass**, contract `COMPLETE`, artifact written
deterministically. Contract completeness is not scientific endorsement.
