---
title: "3D Ising bootstrap minimal-stable-antecedent calibration — run plan"
status: complete
doc_type: governed_run_plan
created: 2026-08-31
run_id: RUN-20260831-ising-bootstrap-minimal-stable-antecedent-calibration
work_id: CCR-ISING-BOOTSTRAP-MINIMAL-STABILITY-CALIBRATION
claim_id: HC-DU-215
owner_repo: dynamic-unity
---

# Exact question

Does the three-dimensional Ising conformal-bootstrap and renormalization-group
universality program supply a real positive control for `HC-DU-214`'s repaired
gate: a compact, non-target-curated antecedent whose independent consistency
conditions produce a stable held-out response without selecting one microscopic
model?

This run does not ask whether the conformal bootstrap selects all of physics,
whether the Ising universality class is fundamental, or whether a CFT datum is a
formed record.

# Frozen specimen and targets

The specimen is the unitary three-dimensional `Z2`-symmetric CFT class used in
the mixed-correlator Ising bootstrap. The antecedent ladder is frozen as:

1. three spacetime dimensions and conformal invariance;
2. unitarity and `Z2` symmetry;
3. the leading odd scalar `sigma` and leading even scalar `epsilon`;
4. `sigma` and `epsilon` as the only relevant scalars in their parity sectors;
5. crossing consistency for the `ssss`, `ssee`, and `eeee` correlator system;
6. the single-operator/OPE-ratio condition used by the precision-island scan.

The locked targets are:

- `Delta_sigma`;
- `Delta_epsilon`;
- `lambda_sigma_sigma_epsilon` and `lambda_epsilon_epsilon_epsilon`; and
- the derived critical exponents `eta=2 Delta_sigma-1` and
  `nu=1/(3-Delta_epsilon)`.

No Monte Carlo value may be used to choose or tune the bootstrap assumptions.
Agreement with lattice results is a source-separated transfer check, not a
historical preregistration claim.

# Tests

1. **Generated-class test.** Determine whether the CFT axioms and spectral
   passport generate an infinite candidate class rather than a finite list
   containing the answer.
2. **Non-copy test.** Check whether crossing and positivity contain a coordinate
   isomorphic to any locked numerical target.
3. **Premise-ablation test.** Compare the single-correlator corner, the
   mixed-correlator closed island, and the precision island. Identify which
   added premises or constraints do the sharpening.
4. **Numerical-enrichment test.** Check whether enlarging the functional search
   space by increasing derivative cutoff shrinks toward a stable island rather
   than moving the answer arbitrarily.
5. **Microdomain-enlargement test.** Compare distinct lattice realizations in
   the same three-dimensional, short-range, `Z2` universality class.
6. **Ruler and selection audit.** State exactly which physical scales cancel in
   dimensionless exponents and which universality-class passport remains
   supplied.
7. **Handoff firewall.** Do not infer a detector, archive, provenance, observer
   access boundary, consumer, or finality rule from CFT consistency.

# Evidence, grade, absorbers, and kills

Primary sources:

- El-Showk et al., *Solving the 3D Ising Model with the Conformal Bootstrap*;
- Kos, Poland, and Simmons-Duffin, *Bootstrapping Mixed Correlators in the 3D
  Ising Model*;
- Kos et al., *Precision Islands in the Ising and O(N) Models*; and
- Hasenbusch, *A Finite Size Scaling Study of Lattice Models in the
  Three-Dimensional Ising Universality Class*.

Maximum grade is scoped Grade 4 for a literature-grounded positive calibration
and an exact selection/nonselection boundary. The result cannot earn a new CFT
theorem, new critical exponent, physical record interface, or new law of
physics.

Strongest absorbers are conformal bootstrap, critical phenomena, RG
universality, finite-size scaling, semidefinite programming, and ordinary
model-class specification.

Cheapest kill: the prediction island exists only after a target value is
inserted, shifts materially with legitimate numerical enlargement, or fails to
transfer across independent microscopic realizations of the declared class.

Stop if:

- a published Ising number is called a DU prediction;
- empirical identification of the universality class is called dynamical
  selection of that class;
- numerical convergence is called a proof of exact uniqueness;
- universality is expanded beyond three-dimensional short-range `Z2` systems;
- a dimensionless CFT datum is called a complete physical ruler; or
- any CFT observable is renamed as a formed material record.

# Decision states

```text
MINIMAL_STABLE_ANTECEDENT_POSITIVE_CONTROL
NON_COPY_CONSISTENCY_INTERSECTION
MICRODOMAIN_UNIVERSALITY_POSITIVE
SCOPED_PREMISE_MINIMALITY_ONLY
ANTECEDENT_PASSPORT_UNSELECTED
COMPLETE_HANDOFF_UNSELECTED
NO_READY_SUCCESSOR
```

# Local-learning boundary

This is a primary-source and formal audit. Re-running a modern numerical
bootstrap locally would spend substantial compute to reproduce published
information and is excluded. Local computation is admitted only for an exact
decision-changing identity or counterexample unavailable from the sources.
