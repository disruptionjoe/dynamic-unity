---
title: "Holonomy-to-handoff return map and soldering boundary — run plan"
status: complete
doc_type: governed_run_plan
created: 2026-09-01
run_id: RUN-20260901-holonomy-to-handoff-return-map-and-soldering-boundary
work_id: CCR-HOLONOMY-TO-HANDOFF-RETURN-MAP-AND-SOLDERING-BOUNDARY
claim_id: HC-DU-220
owner_repo: dynamic-unity
---

# Exact question

Can the action-selected `Z2` holonomy banked in `HC-DU-207` derive the anchored
autonomous handoff parity isolated by `HC-DU-219`, or does composing the two
results require another supplied alignment?

# Scope and authority

Dynamic Unity is the only write scope. Joe's direct `Go` reopens the exact
`HC-DU-207 -> HC-DU-219` seam for one bounded theorem-or-counterexample wave.
No sibling repository, provider, hardware, or external data acquisition is in
scope.

# Frozen distinctions

The run keeps separate:

1. signed edge transport on a closed cycle;
2. its gauge-invariant loop holonomy;
3. the canonical return map on the base fibre;
4. a handoff into the same fibre after transport;
5. a handoff into a distinct target fibre;
6. an identity-preserving faithful `Z2` representation;
7. a chosen source-target soldering/isomorphism; and
8. an autonomously selected material writer, archive, consumer, and ruler.

# Tests

1. **Closed-loop positive.** Exhaust signed four-cycle transports and vertex
   gauges; verify that loop transport canonically returns the base fibre with
   parity equal to holonomy.
2. **Distinct-target obstruction.** Enumerate every source-target bijection and
   prove that independent target relabeling exchanges the two candidates and
   fixes neither.
3. **Typed group repair.** Enumerate multiplicative `Z2` homomorphisms and test
   whether identity preservation plus faithful response selects one map.
4. **No-effect control.** Require trivial holonomy to act trivially. Verify
   that the inverted bijection fails this condition rather than counting as a
   second faithful group action.
5. **Soldering ablation.** Compare same-fibre return, separate target with no
   soldering, and separate target with a fixed soldering. Delete the soldering
   and require the response ambiguity to reopen.
6. **Autonomous transfer.** Feed the derived parity into the exact `HC-DU-219`
   correction model and verify convergence without adding an independent
   parity parameter.
7. **Existing-result regression.** Load the `HC-DU-207` and `HC-DU-219`
   artifacts and preserve their earned boundaries.

# Absorbers and maximum grade

The strongest absorbers are principal-bundle holonomy, torsors, equivariant
maps, representation theory, gauge fixing, solder forms, and ordinary signed
graph/Ising dynamics.

Maximum grade is scoped Grade 4 for an exact composition theorem and
nonselection boundary. It cannot establish a physical `Z2` substrate, a
material record, GU transfer, observer access, source issuance, a finite
remainder, empirical excess, or a new law of nature.

# Cheapest kill and stop rules

Cheapest kill: closed-loop holonomy is an automorphism of one fibre, but a map
to an independently relabelable target fibre has two equally admissible
solderings.

Stop if:

- equality of two printed `Z2` labels is treated as a physical identification;
- a same-fibre return theorem is promoted to an arbitrary cross-system handoff;
- identity preservation or faithful response is imposed after seeing the
  desired target;
- a soldering map written into the action is called source-free selection;
- the standard mathematics is advertised as new physics; or
- any repository other than Dynamic Unity is written.

# Decision states

```text
HOLONOMY_SELECTS_SAME_FIBRE_RETURN_PARITY
DISTINCT_TARGET_REQUIRES_SOLDERING
FAITHFUL_IDENTITY_PRESERVING_Z2_ACTION_IS_UNIQUE
UNTYPED_ALIGNMENT_HAS_NO_CANONICAL_SECTION
HANDOFF_PARITY_DERIVED_ONLY_AFTER_FIBRE_IDENTITY_OR_SOLDERING
MATERIAL_RECORD_INTERFACE_STILL_UNSELECTED
NO_READY_SUCCESSOR
```

# Local-learning boundary

Only exact finite enumeration and theorem proof are admitted. No simulation,
training, provider, hardware, or literature campaign is needed.
