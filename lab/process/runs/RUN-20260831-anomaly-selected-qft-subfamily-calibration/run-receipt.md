---
title: "Anomaly-selected QFT subfamily and non-copy selector calibration — run receipt"
status: complete
doc_type: governed_run_receipt
created: 2026-08-31
run_id: RUN-20260831-anomaly-selected-qft-subfamily-calibration
work_id: CCR-ANOMALY-QFT-SUBFAMILY-CALIBRATION
claim_id: HC-DU-213
owner_repo: dynamic-unity
---

# Return

```text
NONCOPY_QFT_CONSISTENCY_SELECTION_POSITIVE
ANOMALY_FREE_SUBFAMILY_PROPER
QFT_EXPRESSIBILITY_PRESERVED
BOUNDED_QUADRATIC_TARGET_SHARPENED
FINITE_DOMAIN_UNIQUENESS_NOT_PHYSICAL
CHARGE_NORMALIZATION_REQUIRES_COUPLING_RULER
RECORD_HANDOFF_UNSELECTED
NORTH_STAR_GATE_CALIBRATED
NO_READY_SUCCESSOR
```

# Result

In the frozen primitive chiral five-charge `U(1)` family with `|q|<=9`, the
standard linear and cubic anomaly equations reduce `8,129` physical candidate
orbits to `(-9,-5,-1,7,8)` without a supplied survivor bit. The bounded
quadratic target image contracts from 313 values to `{220}` and the quartic
image from 1,075 values to `{13,684}`.

The uniqueness is not physical. Increasing the charge bound to ten adds
`(-10,-4,-2,7,9)` and changes the selected quadratic image to `{220,250}`;
changing cardinality produces lower-charge solutions. Bare `B2` also changes
under charge normalization while `g^2 B2` remains invariant when the coupling
co-transforms.

# Grade and collision

`HC-DU-213` is banked at scoped Grade 4 as a bounded non-copy selection
calibration and domain/ruler boundary. Standard anomaly cancellation,
Diophantine `U(1)` spectrum classification, representation theory, and
ordinary gauge response absorb the science and mathematics. No novelty or
new physics is claimed.

# Decision consequence

The DU gate now has a known-physics positive example of a non-copy selector.
The missing object is narrower: a physical theory must select the candidate
domain and ruler as well as a proper subfamily, then sharpen a locked physical
target and independently select the material handoff. No current candidate
does all of that; routing remains `no_ready`.

# Validation

- exact exhaustive probe: `19/19 PASS`;
- deterministic artifact SHA-256:
  `af4ffd2de4e3b5c761bb66c143993165f2ccd34131054e3b8dc728347d2aa071`;
- Python compilation: pass;
- source, schema, semantic-governance, orientation, and focused regressions:
  recorded in final repository validation.

# Routing

`CURRENT-RESEARCH.yaml` revision 163 retains `no_ready`. Reopen with a
physically selected candidate domain plus a non-copy action, index, anomaly,
quantization condition, or stable constraint; fix the physical quotient and
ruler; then test a locked target without refit. A separate source-selected
complete handoff remains necessary for any empirical record claim.
