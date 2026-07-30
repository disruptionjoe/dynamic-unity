---
title: "Reduced-QRF loop defect and perspectival-curvature gate — run receipt"
status: completed
doc_type: governed_run_receipt
created: 2026-07-30
completed_at: "2026-07-30 08:17:16 CDT"
run_id: RUN-20260730-080556-qrf-reduced-loop-curvature-gate
work_id: ANOMALY-QRF-REDUCED-LOOP-CURVATURE
action_id: QRF-03-REDUCED-LOOP-CURVATURE-GATE
claim_id: HC-DU-155
authority: "Joe direct chat: Go"
owner_repo: dynamic-unity
---

# Reduced-QRF loop defect and perspectival-curvature gate

## Disposition

```text
REDUCED_LOOP_DEFECT_FROM_DISCARDED_LINEAGE
+ NONCOMMUTING_REDUCTION_PATH_DEPENDENCE
+ REPRESENTATION_COVARIANT_STATISTICS
+ STANDARD_QM_COARSE_GRAINING_ABSORPTION
+ NO_READY_SUCCESSOR
```

The run completed at scoped Grade 4. It proved an exact closure boundary for
reversible complete perspective transformations followed by access reduction
and supplied exact quantum controls. It did not produce a Grade-5 physical
remainder, a new prediction, or a selected successor.

## Earned result

For assignments and reductions satisfying \(R_AJ_A=R_BJ_B=\mathrm{id}\), and
a reversible complete transformation \(\mathcal U\), the reduced handoffs

\[
Q_{A\to B}=R_B\mathcal UJ_A,
\qquad
Q_{B\to A}=R_A\mathcal U^{-1}J_B
\]

obey

\[
Q_{B\to A}Q_{A\to B}-\mathrm{id}
=
R_A\mathcal U^{-1}
\bigl(J_BR_B-\mathrm{id}\bigr)
\mathcal UJ_A.
\]

Thus a complete forward-and-return loop may close exactly while the reduced
loop fails solely because the intermediate access map discarded
return-relevant lineage.

The exact controls established:

- a CNOT outward-and-return loop with the same retained carrier closes;
- discarding that carrier, attaching a fresh blank, and applying the nominal
  return map sends \(|+\rangle\) to \(I/2\), producing an \(X_+\)-probability
  defect of \(1/2\);
- the closure identity holds on a basis of the full qubit operator space;
- two noncommuting dephasing conditional expectations produce a path-order
  trace distance and \(X_+\)-probability difference of exactly \(6/25\);
- identical reductions are idempotent and the selected orthogonal Pauli
  reductions commute; and
- jointly rotating the state, access maps, and readout leaves every reported
  probability invariant.

## Scientific meaning

Reduced-loop failure and path-order dependence are not sufficient evidence
for perspectival curvature. Standard quantum channel theory absorbs them as,
respectively:

1. discarded lineage in an otherwise reversible complete loop; and
2. different orders of noncommuting physical reductions.

A future curvature candidate must instead supply a physically selected
complete loop and survive complete-lineage, same-protocol, covariance, benign
refinement, and standard-quantum controls with one frozen held-out statistic.

The result narrows but does not eliminate the high-ceiling conjecture. The
easy version—curvature inferred from reduced-description path
dependence—is closed.

## Portfolio transition

- `CURRENT-RESEARCH.yaml` advanced from revision 107 to 108.
- `HC-DU-155` was attached as a supporting scoped Grade-4 boundary for the
  parked physical-reliability branch.
- no parked reopener was satisfied;
- no scientific program or executable action was activated; and
- successor selection remains `no_ready`.

## Resource disposition

Exact finite channel algebra and primary-source collision fully decided the
question posed by this run. Larger numerical QRF loops, cloud execution, and
external hardware would instantiate the absorbed effects without testing the
surviving admission boundary.

## Durable files

- `explorations/qrf-reduced-loop-defect-conditional-expectation-path-order-and-perspectival-curvature-gate-2026-07-30.md`
- `tests/du_qrf_reduced_loop_curvature_gate_probe.py`
- `tests/artifacts/du_qrf_reduced_loop_curvature_gate_result.json`
- `COUNTER-ASSUMPTIVE-FINDINGS-REGISTER.md`
- `explorations/concept-register.md`
- `docs/quantum-foundations-orientation-surface.md`
- `tests/README.md`
- `CURRENT-RESEARCH.yaml`
- this run plan and receipt

## Validation

- `python3 tests/du_qrf_reduced_loop_curvature_gate_probe.py --write-artifact`
  — **PASS**, 18/18 exact scientific checks.
- `python3 tests/du_agent_orientation_contract_probe.py --write-artifact` —
  **PASS**, 37/37 governance checks, 311 unique counter-assumptive findings,
  and 5,982/6,000 cold-start words.
- Python compilation of both changed probes — **PASS**.
- direct PyYAML/JSON revision, quiescence, successor, and exact-check
  assertions — **PASS**.
- 121 repository-local Markdown links on changed surfaces — **PASS**.
- `git diff --check` — **PASS**.
