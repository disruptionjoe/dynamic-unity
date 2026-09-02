---
title: "Dirac--Maxwell charge-flux constraint witness — run receipt"
status: complete
doc_type: governed_run_receipt
created: 2026-09-02
run_id: RUN-20260902-dirac-maxwell-charge-flux-constraint-witness
work_id: CCR-DIRAC-MAXWELL-CHARGE-FLUX-CONSTRAINT-WITNESS
claim_id: HC-DU-223
owner_repo: dynamic-unity
---

# Dirac--Maxwell charge-flux constraint witness

## Disposition

```text
ACTION_SELECTED_CHARGE_RESPONSE
+ COMPRESSIVE_TARGET_SUFFICIENCY
+ GAUSS_CONSTRAINT_WITNESS
+ UPSTREAM_MICROSTATE_AND_PROVENANCE_LEAK
+ CALIBRATED_WRITE_CAN_PRESERVE_TARGET
+ DOWNSTREAM_WRITE_CAN_DESTROY_SUFFICIENCY
+ CONSTRAINT_WITNESS_IS_NOT_MATERIAL_RECORD
+ NO_READY_SUCCESSOR
```

The wave is complete at scoped Grade 4. It positively closes the
target-sufficient-response branch of the `HC-DU-222` reopener without
relabeling the response as a material record.

## Result

In a frozen Dirac--Maxwell theory, the action selects the electromagnetic
current and Maxwell equation. The integrated current and Gauss boundary flux
both determine total enclosed charge. This response is a strict quotient:
eighty frozen completions map to five charge/flux classes, while spin,
interior distribution, provenance, and boundary-crossing history remain
variable inside a flux fibre.

The field is therefore a lawful physical constraint witness. It is not an
occurrence certificate or durable archive. A calibrated identity write
preserves charge exactly; a magnitude-only write merges opposite charges and
loses sign. This separates upstream response loss from downstream write loss.

## Boundary

The general response quotient, Dirac current, and Gauss-law control were
already banked. This run composes them and localizes the remaining burden. It
does not select the `U(1)` theory, charge representation, region, orientation,
boundary conditions, detector, pointer, blank state, calibration,
amplification, retention, provenance, access, reset, or consumer.

## Repository transition

- `HC-DU-223` is banked in the durable exploration.
- `NI-DU-261` records the complete-state and field-is-record corrections.
- The concept, connection, and test surfaces carry the narrower handoff
  reopener.
- `CURRENT-RESEARCH.yaml` advances from revision 172 to 173.
- The portfolio remains quiescent `no_ready`; no scientific or publication
  successor was activated.
- No sibling repository, hardware, provider, acquisition, prediction, paper,
  or external action was activated.

## Validation

- `python3 tests/du_dirac_maxwell_charge_flux_constraint_witness_probe.py
  --write-artifact` — **PASS**, `11/11`.
- Python compilation of the new probe — **PASS**.
- `python3 tests/du_agent_orientation_contract_probe.py --write-artifact` —
  **PASS**, `37/37`, 374 unique counter-assumptive findings, 91 resolving
  current references, 40 resolving stable-entrypoint links, no active or
  executable scientific action, and 6,674 cold-start words within the admitted
  guidance-overage band.
- Direct PyYAML revision, quiescence, successor, and `HC-DU-223` assertions —
  **PASS**.
- Regression controls: `HC-DU-222` **13/13**, `HC-DU-163` **8/8**, and the
  capability-indexed gauge-boundary suite **20/20**.
- `git diff --check` — **PASS** before receipt finalization.

## Durable files

- `explorations/dirac-maxwell-charge-flux-compressive-sufficiency-and-constraint-witness-boundary-2026-09-02.md`
- `tests/du_dirac_maxwell_charge_flux_constraint_witness_probe.py`
- `tests/artifacts/du_dirac_maxwell_charge_flux_constraint_witness_result.json`
- `COUNTER-ASSUMPTIVE-FINDINGS-REGISTER.md`
- `explorations/concept-register.md`
- `CONNECTIONS.md`
- `CURRENT-RESEARCH.yaml`
- `tests/README.md`
- this run plan and receipt
