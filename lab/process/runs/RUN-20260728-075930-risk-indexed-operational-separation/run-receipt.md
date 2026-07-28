---
title: "Risk-indexed operational separation — run receipt"
status: completed
doc_type: governed_run_receipt
created: 2026-07-28
run_id: RUN-20260728-075930-risk-indexed-operational-separation
work_id: RISK-INDEXED-OPERATIONAL-SEPARATION
program_id: CCR-RISK-INDEXED-OPERATIONAL-SEPARATION
claim_id: HC-DU-070
authority: "Joe direct chat: Go"
owner_repo: dynamic-unity
---

# Risk-indexed operational separation

## Receipt

The run composes `HC-DU-069`'s exact support topology with Dynamic Unity's
existing probability-law, bounded-score, finite-shot, and CHSH controls.

It returns:

```text
SUPPORT_AND_PROBABILITY_NON_UNIFICATION
+ RISK_INDEXED_REOPENER_CORRECTION
```

The run is complete. No physical successor is activated.

## Scientific return

`HC-DU-070` proves:

1. one full-support member of a null family makes every nontrivial zero-error
   finite test impossible;
2. this does not remove finite statistical content;
3. disjoint closed convex null and alternative law families have a positive
   robust bounded-score gap equal to their minimum total-variation distance;
4. conditional null ceilings and alternative floors give a memory-robust
   finite-sample test without assuming IID;
5. passive post-processing cannot increase the robust separation;
6. quantum CHSH contains a full-support behavior, so no finite transcript
   logically excludes the quantum class;
7. nevertheless, \(n\) consecutive CHSH wins have quantum-null probability
   at most \(((2+\sqrt2)/4)^n\), while an ideal PR box produces the transcript
   with probability one; and
8. Dynamic Unity's physical reopener must accept exact-support or
   controlled-risk routes while keeping their evidence types distinct.

The Bell, total-variation, convex-separation, concentration, and finite-
statistics components are known. The earned DU content is their typed
composition with completion closure, capability, acquisition completeness,
and evidence grade.

## CHSH control

The existing operational-theory landscape probe passed unchanged at `28/28`.
Closed-form arithmetic gives:

- \(19\) consecutive wins for quantum-null error at most \(0.05\);
- \(44\) for error at most \(0.001\); and
- \(96\) for the one-sided five-sigma convention
  \(2.8665\times10^{-7}\).

Each bound remains strictly nonzero for finite \(n\). These are type-I error
bounds, not posterior probabilities and not a proposed PR-box experiment.

## Portfolio transition

`CURRENT-RESEARCH.yaml` advances from revision 18 to 19.

- `CCR-RISK-INDEXED-OPERATIONAL-SEPARATION` is completed with `HC-DU-070`.
- No scientific successor is selected.
- `DU-PAPER-013-HARDENING` remains separately prepared and unchanged.
- The successor class
  `physically-selected-positive-margin-law-family-with-complete-assay` is
  recorded but inactive.
- The zero-error candidate remains available as a stricter sibling route.
- The previous closure result remains durable evidence; its live program
  block is replaced to preserve the cold-start budget.

## Durable files

- `explorations/risk-indexed-operational-separation-and-support-probability-non-unification-2026-07-28.md`
- `explorations/concept-register.md`
- `docs/quantum-foundations-orientation-surface.md`
- `COUNTER-ASSUMPTIVE-FINDINGS-REGISTER.md`
- `CURRENT-RESEARCH.yaml`
- `tests/du_agent_orientation_contract_probe.py`
- `tests/artifacts/du_agent_orientation_contract_result.json`
- this run plan and receipt

## Validation

- `python3 tests/du_operational_theory_landscape_probe.py` — **PASS**,
  28/28 unchanged CHSH/GPT controls
- `python3 tests/du_agent_orientation_contract_probe.py --write-artifact` —
  **PASS**, 35 checks, 221 unique counter-assumptive rows, 5,927/6,000
  cold-start words
- `python3 tests/du_hypothesis_efficient_approach_registry_probe.py` —
  **PASS**, 10/10
- `python3 tests/du_near_term_swing_approach_atlas_probe.py` — **PASS**,
  16/16
- `python3 tests/du_capability_indexed_north_star_probe.py` — **PASS**,
  20/20
- changed-document local links — **PASS**; the new theorem and orientation
  link resolve
- `git diff --check` — **PASS**
