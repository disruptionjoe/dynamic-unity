---
title: "Superconducting fluxoid topological material record — run receipt"
status: complete
doc_type: governed_run_receipt
created: 2026-09-02
run_id: RUN-20260902-superconducting-fluxoid-topological-material-record
work_id: CCR-SUPERCONDUCTING-FLUXOID-TOPOLOGICAL-MATERIAL-RECORD
claim_id: HC-DU-224
owner_repo: dynamic-unity
---

# Superconducting fluxoid topological material record

## Disposition

```text
TOPOLOGY_SELECTS_MATERIAL_RECORD_COORDINATE
+ BLANK_TO_WRITTEN_FLUXOID_FORMATION
+ NONZERO_ORDER_PARAMETER_PROTECTS_WINDING
+ PHASE_SLIP_IS_THE_ERASURE_GATE
+ BINARY_WINDOW_TARGET_SUFFICIENCY
+ FULL_SECTOR_AND_PROVENANCE_FIRST_LEAK
+ READOUT_REVEALS_BUT_DOES_NOT_CREATE_RECORD
+ CONDITIONAL_MATERIAL_POSITIVE_NOT_UNIVERSAL_SELECTOR
+ DOES_NOT_COMPLETE_HC-DU-223_CHARGE_HANDOFF
+ NO_READY_SUCCESSOR
```

The wave is complete at scoped Grade 4. It supplies an ordinary-physics
positive for topology-selected material-record formation before readout while
preserving the source-to-record coupling and provenance boundary.

## Result

For a superconducting ring with nonvanishing complex order parameter, the
normalized phase is a map `S1 -> U(1)` and its winding labels disconnected
homotopy sectors. Continuous nonvanishing deformations preserve winding; a
sector change requires a phase slip through zero condensate amplitude. In the
frozen circuit/London model, winding exactly determines the persistent-current
branch while many microscopic phase configurations share the same winding.

The normal phase has no winding, so the superconducting transition can form a
new material record coordinate. The record exists before a later SQUID or
transport readout. It does not preserve exact formation route, time, source, or
microstate. Signed winding also needs orientation; winding parity determines
the response only in the declared binary sector window.

## Physical collision

- Monaco et al. (2009) provide a passive spontaneous-formation control.
- Petkovic, Lollo, and Harris (2020) provide a measured phase-slip transition
  control in an isolated flux-biased ring.
- Ligato et al. (2021) provide an engineered persistent phase-slip memory with
  explicit write and read operations.

The sources establish the physical premises, not a new DU prediction or a
universal interface law.

## Boundary

The result does not complete `HC-DU-223`. Electric Gauss flux and
superconducting magnetic fluxoid winding are distinct response/record types.
The source-selected coupling that writes the former target into the latter
record remains open. The ring, material phase, quench or write protocol, bath,
orientation, operating window, readout, archive, access route, consumer, and
finality contract remain supplied.

## Repository transition

- `HC-DU-224` is banked in the durable exploration.
- `NI-DU-262` records the readout/formation and topology/provenance correction.
- The concept, connection, and test surfaces carry the narrowed reopener.
- `CURRENT-RESEARCH.yaml` advances from revision 173 to 174.
- The portfolio remains quiescent `no_ready`; no scientific or publication
  successor was activated.
- No sibling repository, provider, hardware, acquisition, prediction, paper,
  or external action was activated.

## Validation

- `python3 tests/du_superconducting_fluxoid_topological_record_probe.py
  --write-artifact` — **PASS**, `12/12`.
- Python compilation of the new probe — **PASS**.
- `python3 tests/du_agent_orientation_contract_probe.py --write-artifact` —
  **PASS**, with 375 unique counter-assumptive findings and no active or
  executable scientific action.
- Direct PyYAML revision, quiescence, successor, and `HC-DU-224` assertions —
  **PASS**.
- Regression controls: `HC-DU-223` and the capability-indexed North-Star suite
  — **PASS** (`11/11` and `20/20`).
- `git diff --check` — **PASS** before receipt finalization.

## Durable files

- `explorations/superconducting-fluxoid-topology-selected-material-record-formation-and-provenance-boundary-2026-09-02.md`
- `tests/du_superconducting_fluxoid_topological_record_probe.py`
- `tests/artifacts/du_superconducting_fluxoid_topological_record_result.json`
- `COUNTER-ASSUMPTIVE-FINDINGS-REGISTER.md`
- `explorations/concept-register.md`
- `CONNECTIONS.md`
- `CURRENT-RESEARCH.yaml`
- `tests/README.md`
- this run plan and receipt
