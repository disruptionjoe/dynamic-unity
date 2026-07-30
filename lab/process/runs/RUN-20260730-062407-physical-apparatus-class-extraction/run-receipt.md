---
title: "PDSI-01 physical apparatus class extraction — run receipt"
status: completed
doc_type: governed_run_receipt
created: 2026-07-30
run_id: RUN-20260730-062407-physical-apparatus-class-extraction
work_id: CCR-PHYSICAL-RECORD-INTERFACE-SELECTION
action_id: PDSI-01-PHYSICAL-APPARATUS-CLASS-EXTRACTION
claim_id: HC-DU-152
state_revision: 105
authority: "Joe direct chat: Go"
owner_repo: dynamic-unity
---

# PDSI-01 physical apparatus class extraction

## Scientific return

```text
UNSELECTED_INTERFACE
+ OBSERVER_OR_CONTROLLER_SUPPLIED
+ CONDITIONAL_MATTER_FIELD_RESPONSE_WELL_DEFINED
+ TOTAL_STRESS_CONSERVATION_REQUIREMENT_EXPLICIT
+ APPARATUS_STRESS_AND_FIELD_ACKNOWLEDGED
+ HEAVY_AND_HOMOGENEOUS_SUFFICIENT_REGIME_STATED_QUALITATIVELY
+ NO_APPARATUS_DYNAMICS_VARIATION_CLASS_NORM_ERROR_OR_NO_REFIT_TRANSFER
+ HC_DU_151_PHYSICAL_COMPLETION_SPACE_REMAINS_UNDEFINED
+ SWING_2_NOT_ACTIVATED
+ SWING_6_NOT_ACTIVATED
+ NO_READY_SUCCESSOR
```

Christodoulou et al. explicitly require apparatus stress to complete the
total conserved source and identify the apparatus self and particle cross
terms. They argue that a sufficiently massive apparatus with a sufficiently
homogeneous field suppresses the branch-relative contributions.

That is a strong and correctly credited absorber. It is not a selected
apparatus class. The source gives no apparatus action, stress family,
variation domain, norm, tolerance, uniform approximation error, or held-out
no-refit transfer. The physically admitted completion space required by
`HC-DU-151` therefore remains undefined.

The result does not challenge the paper's phase calculation. It states the
additional packet needed to turn a conditional effective model into an
apparatus-independent descent claim.

## Portfolio disposition

- `HC-DU-152` is banked at scoped Grade 4.
- The source-interface program is parked at its exact reopener.
- Swing 2 is not activated because no physical apparatus class was selected.
- Swing 6 is not activated because omission is not a physical automorphism
  of a defined class.
- Dynamic Unity returns to explicit `NO_READY_SUCCESSOR` quiescence.
- The prepared publication program is unchanged.
- No model, simulation, hardware path, prediction, or external contact was
  activated.

## Durable files

- `explorations/christodoulou-gie-apparatus-class-selection-and-descent-boundary-2026-07-30.md`
- this run plan
- this run receipt
- `CURRENT-RESEARCH.yaml`

## Validation

- `python3 tests/du_physical_descent_ten_swing_campaign_probe.py
  --write-artifact` — **PASS**, 10/10 checks; Swing 1 is completed as
  `HC-DU-152`, and zero later swings are executable.
- `python3 tests/du_agent_orientation_contract_probe.py --write-artifact` —
  **PASS**, 37/37 checks, 308 unique counter-assumptive rows, and
  5,856/6,000 cold-start words.
- direct PyYAML revision, quiescence, evidence-chain, and no-execution-packet
  assertions — **PASS** at revision 105.
- changed-test Python compilation — **PASS**.
- changed-document local-link check — **PASS**.
- `git diff --check` — **PASS**.
