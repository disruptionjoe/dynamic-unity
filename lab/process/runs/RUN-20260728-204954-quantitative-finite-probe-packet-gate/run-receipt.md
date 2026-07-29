---
title: "Quantitative finite-probe packet gate — run receipt"
status: completed
doc_type: governed_run_receipt
created: 2026-07-28
run_id: RUN-20260728-204954-quantitative-finite-probe-packet-gate
work_id: CCR-QUANTITATIVE-FINITE-PROBE-PACKET-GATE
claim_id: HC-DU-097
authority: "Joe direct chat: Go, after HC-DU-096"
owner_repo: dynamic-unity
---

# Quantitative finite-probe packet gate

## Scientific return

Compactness makes finite certification possible but not quantitatively
usable. The missing constructive object is a uniform physical observability
modulus.

If target-distinct completion pairs have a finite cover of size \(Q_\delta\),
all admitted probes are \(L\)-Lipschitz, and a physical probe distribution
satisfies

\[
\nu\{m:|m(\theta)-m(\theta')|\geq a_\delta\}
\geq p_\delta
\]

uniformly, then
\(0<p_\delta<1\) implies that

\[
N
\geq
\frac{\log Q_\delta+\log(1/\alpha)}
     {-\log(1-p_\delta)}
\]

independent probes give a uniform margin at least \(a_\delta/2\) with design
success probability \(1-\alpha\). Acquisition error below
\(a_\delta/4\) then yields the `HC-DU-095` target-resolution certificate.
For \(p_\delta=1\), one sampled probe covers the finite net almost surely.
An effective net and separator oracle give a deterministic
\(Q_\delta\)-probe version.

This is a target-relative assay construction. The probe family and physical
design law must be frozen independently of the held-out target; the result
does not select a universal physical record interface.

## Exact resource boundaries

- A packet with \(N\) coordinates and at most \(A\) retained values per
  coordinate must satisfy

  \[
  A^N\geq P_\delta(T(\Theta)).
  \]

- A compact \(n\)-point class with only singleton probes requires \(n-1\)
  coordinates, although unrestricted binary coding needs only
  \(\lceil\log_2n\rceil\) bits.
- The probe \(m_\varepsilon(x)=\varepsilon x\) separates \([0,1]\) with one
  coordinate while its robust margin \(\varepsilon\delta\) tends to zero.

Thus target entropy, probe-family coordinate count, response margin, and
physical repetition/source cost are independent resources.

## Sobolev entropy boundary

For the \(H^s\) unit ball on \(\mathbb T^d\), viewed in \(H^{s'}\) with
\(r=s-s'>0\), a Fourier sign-code construction gives

\[
\log P_\epsilon
\gtrsim
\epsilon^{-d/r}.
\]

The compact class has infinite box-counting dimension and cannot have a fixed
finite-dimensional Hölder-stable encoding for its full identity target.
Finite-dimensional manifolds, attractors, sparse/low-rank models, and
parametric classes escape only by adding low-complexity structure that
physics must independently select.

## Grade and disposition

- **Scoped Grade 4:** compactness gives no uniform packet count, margin,
  algorithm, or physical cost; full regularity balls remain infinitely
  complex at fine resolution.
- **Conditional Grade 3:** a physically selected small-ball observability
  modulus, effective pair cover, compatible campaign, and calibrated
  acquisition yield an explicit finite packet.
- **Not earned:** the physical probe distribution, low-complexity class,
  joint QFT execution, repetitions/resources, complete acquisition, no-refit
  transfer, new physics, Grade-5 remainder, prediction, paper, or successor.

`CURRENT-RESEARCH.yaml` advances from revision 47 to 48. Dynamic Unity remains
quiescent. The active-wave candidate now explicitly requires uniform physical
observability and a joint finite packet.

## Resource disposition

Exact covering, union-bound, finite-alphabet, and Fourier arguments decided
the gate. A local random-sampling model would only illustrate the proved
formula. External hardware is irrelevant until a physical probe measure,
modulus, and acquisition contract exist.

## Durable files

- `explorations/quantitative-finite-probe-construction-small-ball-observability-and-sobolev-entropy-boundary-2026-07-28.md`
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
  checks, 254 unique counter-assumptive findings, and 5,978/6,000 cold-start
  words; semantic schema fallback used because `jsonschema` is unavailable
- `python3 tests/du_hypothesis_efficient_approach_registry_probe.py` —
  **PASS**, 10/10
- `python3 tests/du_near_term_swing_approach_atlas_probe.py` — **PASS**,
  16/16
- direct PyYAML revision, quiescence, and successor-candidate assertions —
  **PASS**
- changed-document local-link assertions — **PASS**
- `git diff --check` — **PASS**
