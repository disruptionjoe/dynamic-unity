---
title: "Action-indexed physical selection frontier — run receipt"
status: completed
doc_type: governed_run_receipt
created: 2026-07-30
completed_at: "2026-07-30 11:38:13 CDT"
run_id: RUN-20260730-113004-physical-selection-frontier
work_id: MPA-02-PHYSICAL-SELECTION-FRONTIER
action_id: MPA-02-PHYSICAL-SELECTION-FRONTIER
program_id: CCR-MINIMAL-PHYSICAL-ANTECEDENT-TO-FINITE-REMAINDER
authority: "Joe direct chat: Go"
owner_repo: dynamic-unity
claim_id: HC-DU-160
---

# Action-indexed physical selection frontier

## Disposition

```text
INCOMPARABLE_MINIMAL_FRONTIERS
+ PARTIAL_SELECTION_FRONTIER
+ ACTION_CLASS_IS_BASE_INDEX
+ KNOWN_RESULT_ABSORPTION
+ SWING 3 NOT ACTIVATED
```

Swing 2 is complete. It replaces the proposed context-free minimal
antecedent with a family of selection frontiers indexed by action/access
capability.

## Exact results

1. For fixed action class \(H\), a target-blind antecedent bundle \(S\)
   selects the operational response class exactly when

   \[
   \ker(a_S)\subseteq\ker(R_H).
   \]

2. In a finite declared coordinate family, selecting bundles are upward
   closed, their inclusion-minimal members form an antichain, and a unique
   least bundle exists exactly when the intersection of all selecting
   bundles still selects.

3. Strengthening the action class refines the response kernel and shrinks
   the family of sufficient bundles. Thus the selection frontier is
   capability-indexed and can split or enlarge.

4. An exact two-bit fixture returns:

   ```text
   no access:      {∅}
   outcome access: {b}, {c,w}
   audit access:   {b,c}, {b,w}, {c,w}
   ```

5. In one frozen qubit measurement model, the same unlabelled dephasing
   channel supports different labelled instruments when either the coupling
   isometry or pointer observable changes. Coupling plus readout algebra is
   jointly sufficient and individually necessary for the formal instrument
   inside that two-coordinate family.

6. The formal minimum selects no sampler, one-run outcome, material archive,
   occurrence provenance, reset behavior, or observer access.

## Absorber result

Finite sufficient statistics, candidate keys, minimal measurement models,
quantum instruments and dilations, process tensors, and instrument tomography
absorb the mathematical components. The result claims no new quantum theorem
or new physics.

Dynamic Unity's scoped increment is the typed correction:

```text
H is the base index;
coupling/readout/material/provenance are candidate antecedents;
information/formation/retention/accessibility are predicates.
```

## Repository transition

- `HC-DU-160` is banked in the durable exploration.
- `CONCEPT-DU-019` carries the action-indexed frontier correction.
- `NI-DU-203` preserves the killed context-free-minimum assumption.
- The quantum-foundations orientation surface carries the correction.
- `CURRENT-RESEARCH.yaml` advances from revision 113 to 114.
- The campaign is prepared but quiescent. Swing 3's scientific prerequisite
  is satisfied at the abstract coupling/readout level; no action is active or
  executable without separate authorization and a source-pinned platform.
- No hardware or numerical simulation was needed.

## Durable files

- `explorations/action-indexed-physical-selection-frontier-antichain-and-measurement-model-boundary-2026-07-30.md`
- `explorations/concept-register.md`
- `docs/quantum-foundations-orientation-surface.md`
- `COUNTER-ASSUMPTIVE-FINDINGS-REGISTER.md`
- `CURRENT-RESEARCH.yaml`
- `tests/du_action_indexed_selection_frontier_probe.py`
- `tests/artifacts/du_action_indexed_selection_frontier_result.json`
- `tests/README.md`
- this plan and receipt

## Validation

- `python3 tests/du_action_indexed_selection_frontier_probe.py
  --write-artifact` — **PASS**; exact frontiers, upper closure, antitone
  action refinement, and both same-channel qubit deletion witnesses.
- `python3 tests/du_minimal_antecedent_campaign_probe.py --write-artifact` —
  **PASS**; all 17 seeds and 10 conditional swing cards remain preserved.
- `python3 tests/du_agent_orientation_contract_probe.py --write-artifact` —
  **PASS**; 37/37 governance checks, 316 unique counter-assumptive findings,
  67 resolving current references, 38 resolving stable-entrypoint links, no
  active/executable scientific action, and 5,866/6,000 cold-start words.
- Python compilation of all three probes — **PASS**.
- Direct PyYAML revision, quiescence, `HC-DU-160`, and Swing-3-preparation
  assertions — **PASS**.
- `git diff --check` — **PASS** before receipt finalization.

## Next boundary

If separately authorized, Swing 3 may choose one primary-source physical
platform, freeze its action and nuisance contracts, and test whether a
material change to one surviving coupling or readout coordinate creates a
response direction outside the nuisance span. This receipt does not choose
the platform or authorize that action.
