---
title: "Holonomy-to-handoff return map and soldering boundary — run receipt"
status: complete
doc_type: governed_run_receipt
created: 2026-09-01
run_id: RUN-20260901-holonomy-to-handoff-return-map-and-soldering-boundary
work_id: CCR-HOLONOMY-TO-HANDOFF-RETURN-MAP-AND-SOLDERING-BOUNDARY
claim_id: HC-DU-220
owner_repo: dynamic-unity
---

# Holonomy-to-handoff return map and soldering boundary

## Disposition

```text
HOLONOMY_SELECTS_SAME_FIBRE_RETURN_PARITY
+ DISTINCT_TARGET_REQUIRES_SOLDERING
+ FAITHFUL_IDENTITY_PRESERVING_Z2_ACTION_IS_UNIQUE
+ UNTYPED_ALIGNMENT_HAS_NO_CANONICAL_SECTION
+ HANDOFF_PARITY_DERIVED_ONLY_AFTER_FIBRE_IDENTITY_OR_SOLDERING
+ MATERIAL_RECORD_INTERFACE_STILL_UNSELECTED
+ NO_READY_SUCCESSOR
```

The wave is complete at scoped Grade 4. It composes `HC-DU-207` and
`HC-DU-219` at their exact types rather than identifying two printed `Z2`
labels.

## Result

Signed transport around the four-cycle returns the source to the same base
fibre with parity equal to the gauge-invariant loop holonomy. Feeding that
return parity into the autonomous correction chain derives the consumer sign
up to internal record gauge and preserves convergence from every initial state
and update order. The residual bit in `HC-DU-219` is therefore not universal.

A handoff into a distinct independently relabelable target fibre remains
different. There are two source-target solderings, and target relabeling
exchanges them freely. Holonomy selects neither. If the target is physically
pointed and required to carry an identity-preserving faithful `Z2` action, the
action is unique; the inverted bijection fails because it sends trivial
holonomy to a target flip.

The sharpened architectural question is now whether a candidate is a
same-fibre return, same-bundle transport along a physically selected path, or
an inter-system transfer requiring a selected soldering/intertwiner.

## Boundaries

The result selects a response relation only. It does not select a blank
archive, write event, provenance, observer access route, consumer resource
contract, reset, certification, public finality, or remainder. The component
mathematics is fully absorbed by standard holonomy, torsor, representation,
gauge, signed-graph, and equivariant-selector theory.

## Repository transition

- `HC-DU-220` is banked in the durable exploration.
- `NI-DU-258` records the same-fibre versus distinct-target correction.
- The concept, connection, and test surfaces carry the typed reopener.
- `CURRENT-RESEARCH.yaml` advances from revision 169 to 170.
- The portfolio remains quiescent `no_ready`; no scientific or publication
  successor was activated.
- No sibling repository, hardware, provider, data acquisition, prediction,
  paper, or external action was activated.

## Validation

- `python3 tests/du_holonomy_handoff_soldering_boundary_probe.py
  --write-artifact` — **PASS**, `15/15`.
- Python compilation of the new probe — **PASS**.
- `python3 tests/du_agent_orientation_contract_probe.py --write-artifact` —
  **PASS**, `37/37`, 371 unique counter-assumptive findings, 79 resolving
  current references, 40 resolving stable-entrypoint links, no active or
  executable scientific action, and 6,411 cold-start words within the admitted
  guidance-overage band.
- Direct PyYAML revision, quiescence, successor, and `HC-DU-220` assertions —
  **PASS**.
- `git diff --check` — **PASS** before receipt finalization.

## Durable files

- `explorations/holonomy-to-handoff-return-map-faithful-action-and-soldering-boundary-2026-09-01.md`
- `tests/du_holonomy_handoff_soldering_boundary_probe.py`
- `tests/artifacts/du_holonomy_handoff_soldering_boundary_result.json`
- `COUNTER-ASSUMPTIVE-FINDINGS-REGISTER.md`
- `explorations/concept-register.md`
- `CONNECTIONS.md`
- `CURRENT-RESEARCH.yaml`
- `tests/README.md`
- this run plan and receipt
