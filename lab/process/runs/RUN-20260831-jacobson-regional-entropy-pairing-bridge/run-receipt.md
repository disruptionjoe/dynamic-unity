---
title: "Jacobson regional-entropy / GU 2+1 pairing bridge — run receipt"
status: complete
doc_type: governed_run_receipt
created: 2026-08-31
run_id: RUN-20260831-jacobson-regional-entropy-pairing-bridge
work_id: CTS-A4-JACOBSON-REGIONAL-ENTROPY-PAIRING-BRIDGE
claim_id: HC-DU-210
owner_repo: dynamic-unity
external_source_repo: gu-formalization
---

# Return

```text
REGIONAL_GEOMETRIC_RESPONSE_ADMITTED
+ MICROSCOPIC_PAIRING_PROVENANCE_BLIND
+ REGION_AND_SCALE_AXES_INDEPENDENT
+ HIGH_ENERGY_DIRECTION_CORRECTED
+ ORDINARY_EFT_ABSORPTION
+ SOURCE_ACTION_REOPENER_PRESERVED
+ NO_READY_SUCCESSOR
```

# Exact result

A fixed Jacobson-type response factors through the declared regional state,
reference, and effective couplings. Equal regional states therefore produce
equal response even when an enlarged algebra distinguishes their global
completion. The theorem makes the physical ceiling explicit: regional
entropy or modular energy cannot identify which family participated in the GU
multiplicity-one mirror pairing.

The finite `2+1` control likewise shows that removing any one of three
unlabelled slots gives the same entropy spectrum and permutation-invariant
response while leaving three distinct microscopic embeddings. Separate
regional and energy-scale marginals also admit opposite joint correlations,
so causal scope and RG scale remain independent until a physical law couples
them.

The imported GU pairing ladder is `0 -> 2 -> 11` as symmetry lowers from
`Spin(10)` through Pati--Salam to the Standard Model. On that route the pair
becomes removable below the higher-symmetry regime, while that specific
pairing channel vanishes at restored `Spin(10)`. The proposed monotone
high-energy “peel-off” reading is reversed.

# Grade and source admission

The factorization and minimal counterexamples earn scoped Grade 4. The
mathematics is absorbed by state restriction, purification freedom, AQFT
relative entropy, sufficient statistics, and product-index underdetermination.
Jacobson horizon/diamond thermodynamics and Wilsonian/curved-spacetime EFT
absorb the physical components.

Current GU transfer remains Grade 1. GU does not yet select the regional/scale
algebra net, reference state, real-form-correct pairing mass and coupling, or a
regulator-robust response beyond ordinary threshold renormalization. No GU
verdict, generation result, gravity law, record formation, dark-matter model,
render ontology, new physics, prediction, paper, provider, or hardware result
is claimed. GU was read only.

# Validation

- `python3 tests/du_jacobson_regional_entropy_pairing_bridge_probe.py --write-artifact`
  — **PASS**, `16/16`;
- orthogonal Bell completions restrict to the same exact `I/2` regional state;
- the global `X tensor X` target differs while the regional response agrees;
- all three unlabelled family removals have spectrum `(1/2,1/2,0)` and the
  same invariant response;
- equal region and scale marginals admit mixed parity `+1` and `-1`; and
- the imported pairing ladder has zero high-symmetry channels and increasing
  lower-symmetry channels.
- repeated artifact SHA-256 remained
  `afa8824be63e141132dfa6d205108d779d7d5a721e0297f5c5b2bad7d4b418a7`;
- `python3 tests/du_relative_entropy_index_descent_admission_probe.py --write-artifact`
  — **PASS** regression;
- `python3 tests/du_agent_orientation_contract_probe.py` — **PASS**, `37/37`,
  cold-start `5919/6000` words; and
- Python bytecode compilation and `git diff --check` — **PASS**.

# Routing

`HC-DU-210` sharpens the GU-inclusive route but does not satisfy the standing
reopener. Reopen only with a GU-owned stationary action that selects the
bivariate region/scale net, reference state, pairing scale/coupling, and a
no-refit response not absorbed by GR plus curved-spacetime QFT/EFT. Dynamic
Unity remains `no_ready`.
