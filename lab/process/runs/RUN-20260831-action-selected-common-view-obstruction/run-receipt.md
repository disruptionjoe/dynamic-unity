---
title: "Action-selected common-view obstruction — run receipt"
status: complete
doc_type: governed_run_receipt
created: 2026-08-31
run_id: RUN-20260831-action-selected-common-view-obstruction
work_id: CTS-A2-COMMON-VIEW-CLOSURE-SELECTOR-OR-OBSTRUCTION
program_id: DU-COMPUTATION-FIRST-CLOSED-TRANSITION-SUBSTRATE
claim_id: HC-DU-207
owner_repo: dynamic-unity
---

# Return

```text
PARTIAL_ACTION_SELECTED_TRANSPORT_ORBIT
+ GLOBAL_COMMON_VIEW_SELECTOR_OBSTRUCTION
+ CAUSAL_STATE_UNIQUE_ONLY_RELATIVE_TO_UNSELECTED_ACTION_FAMILY
+ PROPAGATION_AND_HOLONOMY_SELECTED
+ ABSOLUTE_RULER_UNSELECTED
+ ACTION_SELECTED_REGIONAL_NO_SECTION
+ OBSERVER_INDEX_REMAINS_SUPPLIED
```

# Exact result

The four-site signed-cycle action selects its `Z2` holonomy, signed transport
gauge orbit, Hessian spectrum, and coarse spectral bands.  Its residual signed
symmetry is vertex-transitive, so it selects no observer site.  Low-band,
high-band, and full probe families are all covariant functions of the same
Hessian but have ranks `2`, `2`, and `4`; the resulting sufficient quotient is
therefore action-family relative.

This is conditional action selection: the complete action and coupling signs
are frozen antecedents. The run does not derive that action from a broader
theory or select the frustrated signs from the balanced rival.

For negative holonomy, every edge-deleted tree has a one-dimensional nonzero
parallel-section space while the full cycle has none.  The finite obstruction
is response-visible through the nonzero gap and `det(L)=4`.  Rescaling an
external square embedding changes perimeter from `4` to `12` without changing
the dimensionless action, so absolute ruler scale remains unselected.

Adding the same mass and quantizing the four coupled oscillators preserves a
different normal-mode spectrum for the two holonomy classes.  This is a
standard-quantum transfer, not new physics.

# Relation to prior work

`HC-DU-123` characterized the fibre of an already formed cycle record.  This
run starts upstream with a source action and derives its latent transport
holonomy.  It still finds no selected sampler, material archive, provenance,
observer access, or consumer.  The missing action-to-record bridge is therefore
not repaired by cohomology language.

# Absorber and grade

Signed/connection graph Laplacians, structural balance, cellular sheaves,
gauge holonomy, equivariance, observability, and quadratic quantization absorb
the component mathematics.  Grade 4 applies only to the exact scoped selection
and nonselection boundary under the frozen antecedent.  No universal no-go,
new physical law, empirical excess, ontology, prediction, paper, or hardware
result is claimed.

# Validation

- `python3 tests/du_action_selected_common_view_obstruction_probe.py --write-artifact`
  — **PASS**, `18/18`;
- all sixteen sign assignments form two eight-element gauge orbits;
- every one of the four proper tree regions has section nullity one;
- the frustrated full cycle has section nullity zero;
- all sixteen residual signed symmetries preserve the Hessian and act
  transitively on vertices;
- low/high spectral projectors descend under every residual symmetry;
- quantum normal-mode transfer and external-ruler negative control pass.
- `CURRENT-RESEARCH.yaml` advances from revision `156` to `157` and passes
  the repository semantic-schema fallback;
- `python3 tests/du_agent_orientation_contract_probe.py --write-artifact`
  — **PASS**, `37/37`, at `5,998/6,000` cold-start words.

# Routing

`CTS-A2` is complete with return class
`COMMON_VIEW_NO_SECTION_OR_AMBIGUITY_OBSTRUCTION`.

The selected successor is
`CTS-A3-ACTION-SELECTED-HOLONOMY-MATERIAL-RECORD-GATE`: test whether the newly
source-selected holonomy selects a complete material record/action handoff in
one unchanged standard-quantum or finite-gauge realization.  Supplying the
instrument, archive, access boundary, or consumer is the cheapest kill.
