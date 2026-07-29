---
title: "Stochastic multiplexing observability gate — run receipt"
status: completed
doc_type: governed_run_receipt
created: 2026-07-28
run_id: RUN-20260728-210517-stochastic-multiplexing-observability-gate
work_id: CCR-STOCHASTIC-MULTIPLEXING-OBSERVABILITY-GATE
claim_id: HC-DU-098
authority: "Joe direct chat: Go, after HC-DU-097"
owner_repo: dynamic-unity
---

# Stochastic multiplexing observability gate

## Scientific return

Stochastic multiplexing can supply the quantitative object missing from
`HC-DU-097`, but only conditionally.

For independent Hilbert-valued Gaussian source and readout weights
\(W\sim N(0,Q)\), \(V\sim N(0,S)\), define

\[
m_{W,V}(\theta)=\langle V,R_\theta W\rangle.
\]

If

\[
s_\delta
=
\inf_{(\theta,\theta')\in K_\delta}
\left\|
S^{1/2}(R_\theta-R_{\theta'})Q^{1/2}
\right\|_{\rm HS}
>0,
\]

then Gaussian fourth moments and Paley--Zygmund give

\[
\Pr\left\{
|m_{W,V}(\theta)-m_{W,V}(\theta')|
\geq s_\delta/\sqrt2
\right\}
\geq 1/36
\]

uniformly. Conditioning source and readout norms to finite bounds preserves
probability at least \(1/72\). With an operator-Lipschitz response, this
composes into the explicit random packet theorem of `HC-DU-097`.

## Exact boundaries

- Random scalar projection of \(S^1\) separates every fixed pair almost
  surely, while every realized projection is globally noninjective.
  Pairwise probability-one events do not imply one uniform reconstruction
  event.
- A fully unitary-invariant infinite-dimensional Gaussian covariance is
  \(cI\). Hilbert-valued finite energy requires trace class, so \(c=0\).
  Nondegenerate finite-energy stochastic designs must select spectral
  weighting or equivalent structure.
- White-noise inverse-wave theorems use distribution-valued sources, complete
  incident and returned traces, and infinite-time correlation limits.
  One stochastic setting is not one finite certified record.
- Finite-measurement inverse positives assume a known finite-dimensional
  subspace or manifold; individual returned measurements may still be
  functions.

## Grade and disposition

- **Scoped Grade 4:** stochastic quantifier, isotropic finite-energy, and
  single-setting/finite-record boundaries.
- **Conditional Grade 3:** explicit Gaussian bilinear small-ball modulus and
  bounded-resource composition into `HC-DU-097`.
- **Not earned:** physical covariance selection, a uniform finite-time
  active-wave gap, finite detector/readout dimension, complete acquisition,
  no-refit transfer, new physics, Grade-5 remainder, prediction, paper, or
  successor.

`CURRENT-RESEARCH.yaml` advances from revision 48 to 49. Dynamic Unity remains
quiescent. The active-wave candidate now requires a physically selected
finite-energy stochastic design, uniform noise-weighted gap, and finite
complete acquisition.

## Resource disposition

Exact Gaussian moments, counterexamples, and primary-source theorem audits
decided the gate. A local stochastic model would only illustrate proved
constants. External hardware is irrelevant until the covariance, finite-time
gap, and acquisition contract exist.

## Durable files

- `explorations/stochastic-multiplexing-pairwise-uniform-observability-and-finite-energy-record-boundary-2026-07-28.md`
- `explorations/concept-register.md`
- `docs/quantum-foundations-orientation-surface.md`
- `COUNTER-ASSUMPTIVE-FINDINGS-REGISTER.md`
- `CURRENT-RESEARCH.yaml`
- `tests/du_agent_orientation_contract_probe.py`
- this run plan and receipt

## Validation

- `python3 -m py_compile tests/du_agent_orientation_contract_probe.py` —
  **PASS**
- `python3 tests/du_agent_orientation_contract_probe.py` — **PASS**, 37/37
  checks, 255 unique counter-assumptive findings, and 5,987/6,000 cold-start
  words; semantic schema fallback used because `jsonschema` is unavailable
- `python3 tests/du_hypothesis_efficient_approach_registry_probe.py` —
  **PASS**, 10/10
- `python3 tests/du_near_term_swing_approach_atlas_probe.py` — **PASS**,
  16/16
- direct PyYAML revision, quiescence, and successor-candidate assertions —
  **PASS**
- changed-document local-link assertions — **PASS**
- `git diff --check` — **PASS**
