---
title: "QFT selection-surplus accounting and dynamical-holonomy calibration"
status: banked_scoped_selection_accounting_and_positive_control
doc_type: theorem_boundary_exact_lattice_control_and_candidate_census
created: 2026-08-31
claim_id: HC-DU-212
run_id: RUN-20260831-qft-selection-surplus-calibration
program_id: CCR-MINIMAL-PHYSICAL-ANTECEDENT-TO-FINITE-REMAINDER
owner_repo: dynamic-unity
evidence_grade: 4
maximum_evidence_grade: 4
---

# Executive result

The first application of the `HC-DU-211` landing spine produces a positive
control and a correction.

```text
DYNAMICAL_GAUGE_ORBIT_SELECTION_POSITIVE
WITHIN_LAW_QUANTUM_SECTOR_SELECTION_POSITIVE
QFT_EXPRESSIBILITY_PRESERVED
LOCKED_SPECTRAL_TARGET_SHARPENED
SELECTOR_KEY_RELOCATION_EXPOSED
CROSS_THEORY_SELECTION_SURPLUS_UNEARNED
RECORD_HANDOFF_UNSELECTED
NO_CURRENT_CANDIDATE_PASSES_CROSS_THEORY_GATE
NORTH_STAR_UNCHANGED
NO_READY_SUCCESSOR
```

On a four-edge `Z2` plaquette, promote the fixed signs of `HC-DU-207` into
gauge configurations and add

\[
E_\kappa(\sigma)=-\kappa\prod_e\sigma_e.
\]

For every nonzero `kappa`, the action selects exactly one physical holonomy
orbit:

\[
\kappa>0\Rightarrow h=+1,
\qquad
\kappa<0\Rightarrow h=-1.
\]

Coupling the selected orbit to the unchanged quantized oscillator gives an
ordinary quantum spectral distinction. The shifted stiffness determinants
are

\[
\det(I+L_+)=45,
\qquad
\det(I+L_-)=49.
\]

Thus the action selects a proper subfamily of the two-sector quantum model and
sharpens a locked spectral target. QFT compatibility did not absorb the
selection.

But the sign of `kappa` is a one-bit copy of the selected holonomy. The model
does not derive that sign from an independently fixed upstream structure. It
therefore earns **within-law sector selection**, not **cross-theory selection
surplus**. The unresolved choice has moved from the gauge configuration into
the action coefficient.

This is not a semantic downgrade. It is the exact distinction the project
needed:

```text
a law selects a state or sector
  !=
an upstream theory selects which low-energy law/parameter/sector obtains
  !=
the selected low-energy family sharpens a held-out target
  !=
the selected physics forms a complete record handoff.
```

The positive control proves that DU's admission gate can recognize ordinary
physical selection. The correction prevents a supplied selector key from
being counted as a deeper derivation.

# 1. Why this was the next question

`HC-DU-211` corrected the overstrict rule that a deeper theory must escape QFT.
A healthy deeper theory should normally land inside QFT in QFT's regime. Its
possible contribution is to select field content, a sector, a parameter
relation, a boundary condition, or a state class that the frozen incumbent
left open.

That correction creates a new possible overclaim:

> Any action that picks one QFT realization has explained why that realization
> obtains.

The statement is false. Ordinary dynamics selects states and sectors after
the action, couplings, boundary conditions, and candidate class are fixed.
An upstream unification claim has a different burden: it must derive some of
those QFT inputs from independently fixed structure rather than repeat the
desired input in a new vocabulary.

The present run freezes that distinction before returning to GU, direct
action, infrared memory, or causal action.

# 2. Exact gauge specimen

Use a four-edge cycle with edge variables

\[
\sigma_e\in\{+1,-1\}.
\]

Vertex gauge transformations act by

\[
\sigma_{uv}\mapsto\eta_u\sigma_{uv}\eta_v,
\qquad \eta_v\in\{+1,-1\}.
\]

The loop product

\[
h(\sigma)=\prod_e\sigma_e
\]

is invariant. Exhaustive enumeration gives:

- sixteen encoded edge assignments;
- sixteen vertex-sign transformations with one global-sign kernel;
- two physical gauge orbits;
- eight encodings in each orbit; and
- orbit labels `h=+1` and `h=-1`.

This is the smallest exact form of `Z2` lattice-gauge holonomy. Gauge-invariant
Ising models and plaquette actions are standard, originating with Wegner's
generalized Ising construction
([1971 primary paper](https://doi.org/10.1063/1.1665530)); Wilson's lattice
formulation established gauge-invariant discrete gauge dynamics in the form
used throughout lattice field theory
([1974 primary paper](https://doi.org/10.1103/PhysRevD.10.2445)).

No novelty is claimed for the construction.

# 3. The action selects a physical orbit

Define

\[
E_\kappa(\sigma)=-\kappa h(\sigma).
\]

Because it depends only on `h`, the energy is gauge invariant. Exhaustive
minimization gives:

| coefficient | minimizers | selected physical family |
|---|---:|---|
| `kappa > 0` | 8 encodings | the single `h=+1` orbit |
| `kappa < 0` | 8 encodings | the single `h=-1` orbit |
| `kappa = 0` | 16 encodings | both orbits; no selection |

This improves the typing of `HC-DU-207`. There the edge signs were fixed in
the antecedent, so the holonomy was constant on the fixed action's
representation orbit. Here the edge signs are admitted variables and the
Wilson term dynamically selects the physical orbit.

The result is exactly gauge-relative. The action does not pick one encoded
edge assignment, nor should it.

# 4. Ordinary quantum landing

Couple the gauge configuration to the same four oscillator coordinates:

\[
H_\sigma
=
\frac12p^Tp
+
\frac12q^T(I+L_\sigma)q.
\]

For trivial holonomy, the shifted stiffness spectrum is

\[
\{1,3,3,5\},
\]

so its determinant is `45`.

For frustrated holonomy, the shifted spectrum is

\[
\{3-\sqrt2,3-\sqrt2,3+\sqrt2,3+\sqrt2\},
\]

so its determinant is `49`.

Take the frozen incumbent quantum family to contain both sectors and the
held-out target to be this spectral determinant. Before `kappa` is fixed, the
target image is

\[
\{45,49\}.
\]

For either nonzero fixed sign of `kappa`, the selected target image is a
singleton. This is an exact instance of `HC-DU-211`'s
`SOURCE_SELECTED_SHARPENING` pattern at the **within-law** level:

```text
the selected family remains inside the incumbent quantum language
and the locked target image contracts.
```

Nothing about QFT expressibility destroys that result. Conversely, nothing
about the target contraction makes the model new physics. It is the standard
positive control.

This finite specimen is a lattice-gauge/quantized-matter control, not a
continuum-QFT theorem. Its role is to validate the selection accounting used
when a genuine continuum construction arrives.

# 5. Two-level selection accounting

Let:

- `d` be incumbent data;
- `Q_I(d)` be the incumbent QFT completion family;
- `u` be independently frozen upstream data;
- `Lambda(u)` be the upstream-to-QFT input/family map;
- `D_q` be dynamics after QFT input `q` is fixed; and
- `tau` be a locked held-out target.

Keep two factorization questions separate.

## Level 1 — within-law selection

For fixed `q`, does the dynamics select a state, phase, orbit, or sector?

The Wilson control answers yes. This is an ordinary physical result and may
be gauge-relative.

## Level 2 — cross-theory structural selection

Does independently fixed upstream structure make

\[
Q_S(d,u)=\Lambda(u)\subsetneq Q_I(d)
\]

without copying the selected QFT input into `u` or choosing `u` after the
target is known?

This is the deeper-theory burden. It is not discharged merely because
`D_q` selects something after `q` is supplied.

## Target consequence

Even if Level 2 succeeds, predictive sharpening additionally requires

\[
\tau(Q_S(d,u))\subsetneq\tau(Q_I(d)).
\]

Otherwise the result is structural selection only for that target.

# 6. The selector-key relocation boundary

In the control,

\[
\operatorname{sign}(\kappa)\longleftrightarrow h_\text{selected}
\]

is a bijection. One input bit was inserted and one sector bit was selected.
The action has converted the coefficient into physical sector preference, but
it has not explained the coefficient.

Call this a **selector-key relocation**:

> A proposed upstream selector earns no cross-theory surplus merely by adding
> an antecedent coordinate isomorphic to the QFT choice it claims to derive.

This is a grading rule, not a universal scalar law. There is no canonical
measure of explanatory simplicity, naturalness, or premise cost. Data
processing proves that output distinctions cannot exceed distinctions in a
deterministic antecedent, but it does not decide which antecedent is physically
natural.

Accordingly, DU should not invent a numerical “selection-surplus score.” It
should instead record:

1. the frozen incumbent family;
2. every newly supplied upstream distinction;
3. the map from upstream distinctions to QFT inputs;
4. whether that map is a copy/relabeling or a nontrivial constraint;
5. which physical action or theorem makes the constraint necessary;
6. the target image before and after selection; and
7. whether any fitting occurred after target reveal.

A nontrivial relation among several QFT parameters, an index, anomaly
constraint, quantization condition, or action-selected orbit may eventually
earn cross-theory structural value. The present control earns none because the
coefficient sign is simply supplied.

# 7. Record-interface boundary

The Wilson action contains no:

- measurement instrument or sampler;
- blank material archive;
- occurrence/source provenance;
- retention, reset, or routing;
- observer-access channel;
- consumer/continuation map; or
- resource and intervention envelope.

Therefore:

```text
dynamical sector selection
  != material record formation
  != complete handoff selection.
```

`HC-DU-208`'s instrument ambiguity remains unchanged. Selecting the holonomy
more strongly does not select how its spectral consequence is measured or
used.

# 8. Unchanged candidate census

| Candidate | Within-law selection | Cross-theory QFT status | Target and handoff disposition |
|---|---|---|---|
| Dynamic `Z2` Wilson control | One gauge orbit for nonzero supplied `kappa` | Selector-key sign is supplied | Ordinary spectral sharpening; no record handoff |
| `HC-DU-207` fixed signed cycle | Response after edge signs are fixed | Holonomy already resides in coupling data | Standard quantum response; `HC-DU-208` leaves handoff open |
| Finite-time infrared memory | Symmetry-constrained dressing component after frame and charges are fixed | No proper QFT completion subfamily yet | No locked hard target; detector/resolution/archive/access supplied |
| Direct action/source response | Source response after kernel and boundary prescription are fixed | Mediator/QFT factorization remains nonunique | Endpoint response absorbed; event partition and consumer open |
| Causal action/CFS | A measure inside a supplied variational class | QFT ansatz, regulator, sector, and continuum inputs remain supplied | No frozen distinctive target; observer/instrument/record open |
| Conditional GU/K77 | Matched luminous orbit only under the conditional action | Highest ceiling, but source action and QFT map remain missing | No locked QFT relation/target; material handoff open |

No current candidate earns `CROSS_THEORY_STRUCTURAL_SELECTION` under the
unchanged gate.

This does not make the candidates useless:

- the Wilson control proves the gate admits known physics;
- infrared memory remains a partial physical carrier construction;
- direct action remains an important ontology/representation fork;
- causal action remains a serious within-framework selector; and
- GU remains the highest-ceiling possible source of nontrivial QFT relations.

They simply have different current grades.

# 9. Consequence for the next reopener

The previous wording “source-selected proper QFT subfamily” was necessary but
not sufficient. It admits a trivial selector key.

The corrected reopener is:

> Produce an upstream physical action, index, anomaly, quantization condition,
> or stable constraint that derives at least one proper relation among frozen
> QFT inputs from independently justified antecedents, without inserting an
> isomorphic copy of the selected input; then test whether that relation
> contracts a locked target image without refit.

For GU specifically, the first admissible packet would contain:

1. the GU-owned source action and lawful domain;
2. the stationary/broken orbit it actually selects;
3. the explicit map into a frozen QFT field/parameter/sector family;
4. an accounting of which selecting signs, scales, and coefficients were
   supplied rather than derived;
5. one locked target sensitive to the derived relation; and
6. the complete physical readout only if an empirical claim is made.

Until such a packet exists, repeating a low-energy action with a preferred
coefficient merely relocates the question.

# 10. Grade, novelty, and stop

## Earned at scoped Grade 4

- exact enumeration of sixteen `Z2` connections and their two gauge orbits;
- exact Wilson-action selection of one orbit for nonzero coefficient;
- exact `kappa=0` nonselection control;
- exact ordinary quantum spectral landing and target-image contraction;
- exact separation of within-law selection from cross-theory selection;
- exact selector-key relocation diagnosis for this specimen; and
- unchanged six-candidate disposition under the `HC-DU-211` spine.

## Absorbed

- the gauge dynamics and holonomy are standard Wegner/Wilson lattice-gauge
  structure;
- the oscillator spectra are standard quadratic quantization;
- factorization, data processing, and target-image comparison supply the
  formal accounting; and
- the anti-copy discipline continues DU's prior boundary-relocation and
  target-coded-interface controls.

The mathematics and physics are not new. The useful DU result is a corrected
admission distinction and a positive calibration showing that the North-Star
gate is neither vacuous nor automatically satisfied.

## Not earned

- continuum QFT, Standard Model, GU, cosmological, or empirical result;
- cross-theory selection surplus;
- explanation or derivation of `kappa`;
- material record, observer, access, consumer, or finality;
- new law, prediction beyond incumbent physics, paper, provider, or hardware;
- activation of a successor.

# Reproducibility

Run:

```bash
python3 tests/du_qft_selection_surplus_holonomy_probe.py --write-artifact
```

The deterministic artifact is
`tests/artifacts/du_qft_selection_surplus_holonomy_result.json`. It reports
`19/19` exact checks.

# Final status

**BANKED SCOPED GRADE-4 SELECTION-ACCOUNTING RESULT / A DYNAMICAL `Z2` WILSON
ACTION SELECTS ONE PHYSICAL HOLONOMY ORBIT AND SHARPENS AN ORDINARY QUANTUM
SPECTRAL TARGET / QFT EXPRESSIBILITY PRESERVES RATHER THAN KILLS THAT SELECTION
/ THE SELECTING COEFFICIENT SIGN IS AN ISOMORPHIC SELECTOR KEY, SO NO
CROSS-THEORY STRUCTURAL SURPLUS IS EARNED / THE RECORD HANDOFF REMAINS
UNSELECTED / NO CURRENT DU CANDIDATE PASSES THE CORRECTED UPSTREAM-TO-QFT GATE
/ NORTH STAR UNCHANGED / NO READY SUCCESSOR.**
