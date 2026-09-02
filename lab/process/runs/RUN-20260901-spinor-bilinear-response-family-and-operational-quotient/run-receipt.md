---
title: "Spinor bilinear response family and operational quotient — run receipt"
status: complete
doc_type: governed_run_receipt
created: 2026-09-01
run_id: RUN-20260901-spinor-bilinear-response-family-and-operational-quotient
work_id: CCR-SPINOR-BILINEAR-RESPONSE-FAMILY-AND-OPERATIONAL-QUOTIENT
claim_id: HC-DU-222
owner_repo: dynamic-unity
---

# Spinor bilinear response family and operational quotient

## Disposition

```text
ACTION_CAN_SELECT_RESPONSE_FAMILY_BEFORE_DETECTOR
+ WEYL_CURRENT_RECONSTRUCTS_PROJECTIVE_TWO_SPINOR
+ DIRAC_VECTOR_CURRENT_IS_NOT_STATE_COMPLETE
+ FULL_DIRAC_BILINEAR_FAMILY_IS_ALGEBRAICALLY_COMPLETE
+ COUPLING_FIELD_CONTENT_SELECTS_OPERATIONAL_QUOTIENT
+ REFERENCE_EXTENSION_CAN_REOPEN_ERASED_PHASE
+ RESPONSE_FAMILY_IS_NOT_MATERIAL_RECORD
+ NO_READY_SUCCESSOR
```

The wave is complete at scoped Grade 4. It turns the `HC-DU-221` coupling
suggestion into an exact action-relative response-family result without
calling tomography or current data a material record.

## Result

A physical action may select an admissible family of interactions through its
carrier, symmetries, field content, and vertices. Equality of every response in
that family defines a canonical operational state quotient. The exact controls
show that this quotient's sufficiency depends on the carrier.

The full Weyl current reconstructs a local two-component density operator and,
on pure states, its projective spinor ray. The Dirac vector current spans only
four of sixteen operator directions: upper spin-up and spin-down are orthogonal
but share current `(1,0,0,0)`. The full Dirac bilinear family spans all sixteen
matrix directions. Every spin-only bilinear still erases global phase; adding a
physical path reference enlarges the response algebra and reopens relative
phase.

## Boundary

Lorentz covariance alone permits several bilinear channel types and does not
select field content or coupling constants. An action-selected response family
does not select a realized vertex, measurement instrument, material transducer,
archive, provenance chain, access route, consumer, finality rule, or target.
Twistor incidence and action formulations preserve the same distinction.

## Repository transition

- `HC-DU-222` is banked in the durable exploration.
- `NI-DU-260` records the detector-versus-response-family and Weyl-versus-Dirac
  correction.
- The concept, connection, and test surfaces carry the exact reopener.
- `CURRENT-RESEARCH.yaml` advances from revision 171 to 172.
- The portfolio remains quiescent `no_ready`; no scientific or publication
  successor was activated.
- No sibling repository, hardware, provider, acquisition, prediction, paper,
  or external action was activated.

## Validation

- `python3 tests/du_spinor_bilinear_response_quotient_probe.py
  --write-artifact` — **PASS**, `13/13`.
- Python compilation of the new probe — **PASS**.
- `python3 tests/du_agent_orientation_contract_probe.py --write-artifact` —
  **PASS**, `37/37`, 373 unique counter-assumptive findings, 87 resolving
  current references, 40 resolving stable-entrypoint links, no active or
  executable scientific action, and 6,610 cold-start words within the admitted
  guidance-overage band.
- Direct PyYAML revision, quiescence, successor, and `HC-DU-222` assertions —
  **PASS**.
- `git diff --check` — **PASS** before receipt finalization.

## Durable files

- `explorations/action-selected-spinor-bilinear-response-family-operational-quotient-and-record-boundary-2026-09-01.md`
- `tests/du_spinor_bilinear_response_quotient_probe.py`
- `tests/artifacts/du_spinor_bilinear_response_quotient_result.json`
- `COUNTER-ASSUMPTIVE-FINDINGS-REGISTER.md`
- `explorations/concept-register.md`
- `CONNECTIONS.md`
- `CURRENT-RESEARCH.yaml`
- `tests/README.md`
- this run plan and receipt
