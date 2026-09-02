---
title: "Superconducting fluxoid topological material record — run plan"
status: complete
doc_type: governed_run_plan
created: 2026-09-02
run_id: RUN-20260902-superconducting-fluxoid-topological-material-record
work_id: CCR-SUPERCONDUCTING-FLUXOID-TOPOLOGICAL-MATERIAL-RECORD
claim_id: HC-DU-224
owner_repo: dynamic-unity
---

# Exact question

Does a superconducting ring's order-parameter topology select a material
record variable before readout, and if so, which targets, orientations,
histories, and operating windows does that record actually preserve?

# Scope and authority

Dynamic Unity is the sole write scope. The wave is a local exact theorem and
primary-source collision. It deepens the existing phenomenon-atlas fluxoid
card; it does not re-credit that atlas, mutate a sibling repository, or claim
new superconducting physics.

# Frozen physical chain

```text
normal state with vanishing condensate amplitude
  -> cool-through superconducting transition
  -> nonvanishing U(1) order parameter on a ring
  -> integer winding/fluxoid sector
  -> metastable persistent-current response
  -> optional SQUID or transport readout
```

The record candidate is winding number `n`, or its orientation-invariant
parity when only a binary memory orbit is physically admitted. The held-out
response is persistent current in a frozen London/circuit window. Exact
formation history and condensate microconfiguration are hostile targets.

# Exact tests

1. Enumerate a finite nonvanishing ring order-parameter class and verify that
   its local continuous-deformation graph has connected components exactly
   indexed by winding number.
2. Verify that changing winding requires leaving that graph, representing a
   phase slip where the order parameter vanishes somewhere.
3. Verify strict compression: many phase configurations share each central
   winding sector.
4. Verify orientation reversal sends `n` to `-n`, while parity is invariant.
5. Verify winding determines persistent current in the frozen circuit model.
6. Verify parity determines current only in the declared two-sector operating
   window and fails on the untruncated sector family.
7. Verify the normal blank has no winding value, while post-transition states
   do: the record coordinate is formed, not merely read.
8. Exhibit same-record/different-microstate and same-record/different-
   provenance witnesses.

# Primary-source anchors

- Monaco et al. (2009), spontaneous fluxoid formation after passive cooling;
- Petkovic, Lollo, and Harris (2020), measured thermally activated transitions
  between fluxoid states with independently characterized parameters; and
- Ligato et al. (2021), a superconducting phase-slip memory whose winding-
  parity state persisted for almost three days and whose write/readout
  operations are explicitly engineered.

# Absorbers and grade

Homotopy of maps `S1 -> U1`, fluxoid quantization, Ginzburg--Landau/London
theory, Kibble--Zurek defect formation, metastability, phase-slip theory, and
superconducting-memory engineering absorb the components. Maximum grade is
scoped Grade 4 for a topologically selected material-record coordinate,
formation/erasure boundary, and target-relative sufficiency result. No
universal record law, Born rule, issuance, permanent finality, new prediction,
or new physics can be earned.

# Cheapest kill and stop

Cheapest kill: local nonvanishing deformations connect different windings, or
the frozen future current is not constant on a winding fibre. The broader
claim is killed if the ring, phase, quench, bath, operating window, or readout
must be supplied—which limits scope even if the topology theorem survives.

Stop if:

- a readout is said to create the fluxoid;
- the fluxoid value is said to encode its complete causal provenance;
- binary parity sufficiency is exported beyond the two-sector window;
- metastability is called absolute finality;
- a quench-created branch is called fundamental issuance; or
- local computation is used for phenomenological parameter fitting.

# Decision states

```text
TOPOLOGY_SELECTS_MATERIAL_RECORD_COORDINATE
BLANK_TO_WRITTEN_FLUXOID_FORMATION
NONZERO_ORDER_PARAMETER_PROTECTS_WINDING
PHASE_SLIP_IS_THE_ERASURE_GATE
BINARY_WINDOW_TARGET_SUFFICIENCY
FULL_SECTOR_AND_PROVENANCE_FIRST_LEAK
READOUT_REVEALS_BUT_DOES_NOT_CREATE_RECORD
CONDITIONAL_MATERIAL_POSITIVE_NOT_UNIVERSAL_SELECTOR
DOES_NOT_COMPLETE_HC-DU-223_CHARGE_HANDOFF
NO_READY_SUCCESSOR
```
