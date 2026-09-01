---
title: "Spinor/twistor transport, interference, and soldered readout — run receipt"
status: complete
doc_type: governed_run_receipt
created: 2026-09-01
run_id: RUN-20260901-spinor-twistor-transport-interference-and-soldered-readout
work_id: CCR-SPINOR-TWISTOR-TRANSPORT-INTERFERENCE-AND-SOLDERED-READOUT
claim_id: HC-DU-221
owner_repo: dynamic-unity
---

# Spinor/twistor transport, interference, and soldered readout

## Disposition

```text
SPIN_CONNECTION_SELECTS_TRANSPORT_ORBIT
+ CENTRAL_Z2_PHASE_ERASED_ON_SINGLE_RAY
+ REFERENCE_INTERFERENCE_REOPENS_VISIBILITY
+ READOUT_BASIS_REMAINS_INTERFACE
+ DISTINCT_SPIN_FRAME_REQUIRES_INTERTWINER
+ TWISTOR_TRANSPORT_DOES_NOT_SELECT_MATERIAL_COUPLING
+ NO_READY_SUCCESSOR
```

The wave is complete at scoped Grade 4. It realizes the preceding abstract
holonomy/handoff boundary with exact spinor and interference controls, then
extends the result to twistors only at the level the mathematics supports.

## Result

The connection and path select a spin transport map and a gauge-covariant
holonomy orbit. The central returns `+I` and `-I` yield opposite spinor vectors
but the same isolated ray and density operator. A coherent path reference turns
that sign into a relative phase: an `X`-basis recombination distinguishes the
two cases perfectly, whereas a path `Z` readout or deletion of the reference
does not.

Independent source and target spin frames admit no fixed alignment. A physical
inter-system handoff therefore still needs an intertwiner. Schur rigidity can
contract that freedom to a scalar for equal irreducible representations, but a
relative phase still needs a physical reference. Twistor incidence and
transport can package conformal and spinorial geometry, but do not select a
material transducer, meter, archive, provenance chain, access route, or use.

## Boundaries

This result does not construct a physical spinor or twistor substrate, derive a
connection or path, select an instrument, transfer GU, prove source issuance,
identify a remainder, or predict new physics. Its component mathematics is
absorbed by standard spin-bundle transport, projective quantum states,
interferometry, representation theory, tetrad/solder forms, twistor incidence,
and quantum instruments.

## Repository transition

- `HC-DU-221` is banked in the durable exploration.
- `NI-DU-259` records the transport/observable/record correction.
- The concept, connection, and test surfaces carry the typed reopener.
- `CURRENT-RESEARCH.yaml` advances from revision 170 to 171.
- The portfolio remains quiescent `no_ready`; no scientific or publication
  successor was activated.
- No sibling repository, hardware, provider, data acquisition, prediction,
  paper, or external action was activated.

## Validation

- `python3 tests/du_spinor_twistor_transport_readout_boundary_probe.py
  --write-artifact` — **PASS**, `15/15`.
- Python compilation of the new probe — **PASS**.
- `python3 tests/du_agent_orientation_contract_probe.py --write-artifact` —
  **PASS**, `37/37`, 372 unique counter-assumptive findings, 83 resolving
  current references, 40 resolving stable-entrypoint links, no active or
  executable scientific action, and 6,521 cold-start words within the admitted
  guidance-overage band.
- Direct PyYAML revision, quiescence, successor, and `HC-DU-221` assertions —
  **PASS**.
- `git diff --check` — **PASS** before receipt finalization.

## Durable files

- `explorations/spinor-twistor-transport-projective-phase-interference-and-material-readout-boundary-2026-09-01.md`
- `tests/du_spinor_twistor_transport_readout_boundary_probe.py`
- `tests/artifacts/du_spinor_twistor_transport_readout_boundary_result.json`
- `COUNTER-ASSUMPTIVE-FINDINGS-REGISTER.md`
- `explorations/concept-register.md`
- `CONNECTIONS.md`
- `CURRENT-RESEARCH.yaml`
- `tests/README.md`
- this run plan and receipt
