---
title: "Aharonov--Casher charge-selected fluxoid transition rule — run receipt"
status: complete
doc_type: governed_run_receipt
created: 2026-09-02
run_id: RUN-20260902-aharonov-casher-charge-selected-fluxoid-transition-rule
work_id: CCR-AHARONOV-CASHER-CHARGE-SELECTED-FLUXOID-TRANSITION-RULE
claim_id: HC-DU-225
owner_repo: dynamic-unity
---

# Aharonov--Casher charge-selected fluxoid transition rule

## Disposition

```text
AHARONOV_CASHER_PHYSICAL_COUPLING_FOUND
+ CHARGE_PARITY_SELECTS_TRANSITION_RULE
+ FLUXOID_PARITY_PROTECTION_IS_CONDITIONAL
+ FULL_CHARGE_IS_QUOTIENTED_AWAY
+ TRANSITION_RULE_IS_NOT_RECORD_VALUE
+ ONE_ENDPOINT_IS_NOT_ZERO_ERROR_CHARGE_CERTIFICATE
+ TIME_REVERSAL_FORBIDS_UNBIASED_SIGNED_WRITE
+ SYMMETRY_AND_ORIENTATION_REMAIN_ANTECEDENTS
+ NO_COMPLETE_HC-DU-223-TO-224_HANDOFF
+ NO_READY_SUCCESSOR
```

The wave is complete at scoped Grade 4. It finds a standard-physics coupling
between electric charge and fluxoid memory while proving that its natural
output is a selected transition/protection rule rather than a copied record
value.

## Result

In a coherent two-path superconducting circuit, island charge supplies the
relative Aharonov--Casher phase between fluxon paths. At equal path amplitudes,
odd integral charge cancels single fluxon slips. Double slips remain, so the
winding transition graph separates into even and odd parity components. Even
charge admits single slips and reconnects the graph.

The source thereby controls whether the material fluxoid record has protected
parity. It retains charge only modulo `2e` and does not choose the actual
winding endpoint. A one-shot endpoint has overlapping parity-conditioned
support. Exact protection also depends on coherent symmetric paths, and
time-reversal covariance forbids a charge-only deterministic map to a nonzero
signed winding without a time-odd bias or orientation.

## Physical collision

Friedman--Averin, Pop et al., Bell et al., and Kalashnikov et al. absorb the
Aharonov--Casher interference, charge-controlled tunnelling, and bifluxon
protection. The earned DU result is the typed transition-rule/value distinction,
factorization boundary, and signed-writer obstruction—not new device physics.

## Boundary

The wave does not complete the `HC-DU-223` to `HC-DU-224` handoff. The natural
bridge quotients total charge to parity, changes the record's dynamics rather
than fixing its value, and omits formation provenance, readout, archive,
observer access, consumer, reset, and finality semantics.

## Repository transition

- `HC-DU-225` is banked in the durable exploration.
- `NI-DU-263` records the value-versus-transition-rule correction.
- The concept, connection, and test surfaces carry the narrowed reopener.
- `CURRENT-RESEARCH.yaml` advances from revision 174 to 175.
- The portfolio remains quiescent `no_ready`; no scientific or publication
  successor was activated.
- No sibling repository, provider, hardware, acquisition, prediction, paper,
  or external action was activated.

## Validation

- `python3 tests/du_aharonov_casher_charge_fluxoid_transition_rule_probe.py
  --write-artifact` — **PASS**, `13/13`.
- Python compilation of the new probe — **PASS**.
- Regression controls: `HC-DU-223` **11/11** and `HC-DU-224` **12/12**.
- `python3 tests/du_agent_orientation_contract_probe.py --write-artifact` —
  **PASS**, with 376 unique counter-assumptive findings and no active or
  executable scientific action.
- Direct PyYAML revision, quiescence, successor, and `HC-DU-225` assertions —
  **PASS**.
- `git diff --check` — **PASS** before receipt finalization.

## Durable files

- `explorations/aharonov-casher-charge-parity-selected-fluxoid-transition-rule-and-signed-writer-obstruction-2026-09-02.md`
- `tests/du_aharonov_casher_charge_fluxoid_transition_rule_probe.py`
- `tests/artifacts/du_aharonov_casher_charge_fluxoid_transition_rule_result.json`
- `COUNTER-ASSUMPTIVE-FINDINGS-REGISTER.md`
- `explorations/concept-register.md`
- `CONNECTIONS.md`
- `CURRENT-RESEARCH.yaml`
- `tests/README.md`
- this run plan and receipt
