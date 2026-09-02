---
title: "Dirac--Maxwell charge-flux constraint witness — run plan"
status: complete
doc_type: governed_run_plan
created: 2026-09-02
run_id: RUN-20260902-dirac-maxwell-charge-flux-constraint-witness
work_id: CCR-DIRAC-MAXWELL-CHARGE-FLUX-CONSTRAINT-WITNESS
claim_id: HC-DU-223
owner_repo: dynamic-unity
---

# Exact question

Does the ordinary Dirac--Maxwell action supply a natural response family that
is sufficient for a useful locked target while remaining noninjective on
irrelevant spinor microstructure, and how far is that response from a formed
material record?

# Scope and authority

Dynamic Unity is the sole write scope. The wave is exact, local, and
hardware-independent. It composes the already banked spinor-response result
`HC-DU-222` with the already banked Gauss-law boundary-flux positive control.
It does not re-earn either component and does not assume GU, a new gauge law,
or a new record ontology.

# Frozen chain

```text
Dirac--Maxwell action and U(1) representation
  -> Noether/electromagnetic current j
  -> conserved charge Q on a declared region
  -> Gauss-law boundary flux Phi
  -> optional calibrated material write W(Phi)
  -> retained record and target use
```

The locked positive target is total enclosed electric charge. Spin,
within-region charge distribution, source provenance, and boundary-crossing
history are hostile targets.

# Exact tests

1. Verify that the charge target factors through the action-selected current
   and the Gauss-law boundary flux.
2. Verify strict compression: distinct spin, phase, distribution, and history
   completions share the same charge/flux response.
3. Exhibit an upstream response leak: equal charge/flux with different spin or
   interior distribution.
4. Exhibit a provenance leak: preloaded and transported charge histories have
   the same final current/flux response.
5. Verify a calibrated identity write preserves the charge target.
6. Exhibit a downstream material-write leak: a magnitude-only pointer merges
   opposite charges.
7. Verify that boundary-crossing history must be retained separately when the
   target is a process rather than an endpoint charge.
8. Preserve the response-versus-record boundary: a constrained gauge field is
   a physical witness, not automatically a blank-to-written durable archive.

# Absorbers and grade

Noether's theorem, the Dirac current, Maxwell's equations, Gauss's law,
superselection, sufficient statistics, and ordinary detector theory absorb
the component mathematics. The maximum grade is scoped Grade 4 for the exact
typed composition, compressive target-sufficiency result, and first-leak
localization. No new gauge law, record-formation theorem, prediction, or new
physics can be earned.

# Cheapest kill and stop

The positive is killed if total charge does not factor through the frozen
current/flux response or if the response is injective on every admitted
microstate. The stronger record claim is killed if the action does not select
the region, material pointer, calibration, blank state, retention,
provenance, access, or reset.

Stop if:

- the electromagnetic field is renamed a durable record merely because it is
  correlated with charge;
- global charge sufficiency is extended to spin, distribution, or history;
- a supplied region or detector is described as action-selected;
- the old Gauss-law result is counted as newly earned; or
- another repository, provider, simulation, or hardware path is used.

# Decision states

```text
ACTION_SELECTED_CHARGE_RESPONSE
COMPRESSIVE_TARGET_SUFFICIENCY
GAUSS_CONSTRAINT_WITNESS
UPSTREAM_MICROSTATE_AND_PROVENANCE_LEAK
CALIBRATED_WRITE_CAN_PRESERVE_TARGET
DOWNSTREAM_WRITE_CAN_DESTROY_SUFFICIENCY
CONSTRAINT_WITNESS_IS_NOT_MATERIAL_RECORD
NO_READY_SUCCESSOR
```
