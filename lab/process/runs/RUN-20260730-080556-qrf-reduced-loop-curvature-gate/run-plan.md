---
title: "Reduced-QRF loop defect and perspectival-curvature gate — run plan"
status: completed
doc_type: governed_run_plan
created: 2026-07-30
run_id: RUN-20260730-080556-qrf-reduced-loop-curvature-gate
work_id: ANOMALY-QRF-REDUCED-LOOP-CURVATURE
action_id: QRF-03-REDUCED-LOOP-CURVATURE-GATE
claim_id: HC-DU-155
authority: "Joe direct chat: Go"
owner_repo: dynamic-unity
---

# Reduced-QRF loop defect and perspectival-curvature gate

## Cold-start contract

- **Purpose/North Star:** determine whether independently selected,
  observer-indexed certified causal records reconstruct observer-accessible
  physics or leave a finite physical remainder.
- **Perspective/ontology:** methodological physical realism. Reference
  systems, discarded carriers, access reductions, and retained records are
  physical; observer indexing is not subjective belief.
- **Current authority:** `CURRENT-RESEARCH.yaml` revision 107 is quiescent
  after `HC-DU-154`; no scientific successor is selected.
- **Completed evidence consumed:** `HC-DU-153` gives a reduced-QRF handoff
  channel and exact block-preservation condition; `HC-DU-154` separates
  outcome broadcast from reference-branch decoherence and identifies retained
  branch information as the first leak.
- **Remaining obligation:** determine whether path dependence among reduced
  perspective handoffs is a representation-invariant physical obstruction or
  ordinary loss caused by intermediate access reduction.
- **Lanes/channels:** Lane 5 primary; Lanes 1, 4, and 7 supporting;
  `CH-FORMAL`, `CH-COLLIDE`, `CH-MODEL`, and `CH-SYN`.
- **Maximum grade:** scoped Grade 4 loop-closure criterion and exact
  coarse-graining/path-dependence boundary. Grade 5 requires a physically
  selected complete loop with excess surviving every standard-QM dilation,
  access, and representation control.

## Exact question

For a reversible full quantum-reference transformation and a reduced
observer-access channel:

1. when does a forward-and-return loop close on the accessible state or
   observable algebra;
2. can a nonzero reduced loop defect occur even when the full transformation
   closes exactly;
3. can different orders of reduced access maps produce different outcomes;
4. and what additional controls are required before either effect may be
   called perspectival curvature rather than ordinary discarded-information
   or noncommuting-channel order dependence?

## Sources and absorbers

Primary sources:

- Luppi, Kabel, Giacomini, and Smirne, “Reduced Quantum-Reference-Frame
  Channels for Open Quantum Systems,” arXiv:2607.05578 (2026).
- Carette, Głowacki, and Loveridge, “Operational Quantum Reference Frame
  Transformations,” *Quantum* 9, 1680 (2025), arXiv:2303.14002.
- Ballesteros, Giacomini, and Gubitosi, “The group structure of dynamical
  transformations between quantum reference frames,” arXiv:2012.15769.

Strongest absorbers:

- Stinespring dilation and reversibility of quantum channels;
- data processing and recoverability;
- conditional expectations and commuting squares;
- ordinary quantum erasure, which-path information, and noncommuting
  dephasing channels; and
- QRF group or operational-equivalence composition before access reduction.

## Pre-registered theorem target

Let \(J_A\) and \(J_B\) assign accessible states to a full packet, let \(R_A\)
and \(R_B\) reduce to the declared accessible systems with
\(R_iJ_i=\mathrm{id}\), and let \(U_{A\to B}=U\) with
\(U_{B\to A}=U^\dagger\). Define

\[
Q_{A\to B}=R_B\,\mathrm{Ad}_U\,J_A,
\qquad
Q_{B\to A}=R_A\,\mathrm{Ad}_{U^\dagger}\,J_B.
\]

The reduced loop closes on every admitted input exactly when

\[
R_A\,\mathrm{Ad}_{U^\dagger}
\bigl(J_BR_B-\mathrm{id}\bigr)
\mathrm{Ad}_U\,J_A=0
\]

as a map on the admitted state span. A stronger sufficient condition is that
\(J_BR_B\) acts identically on the forward image
\(\mathrm{Ad}_U J_A\).

For an observable algebra \(\mathcal A_A\), closure is only required on that
algebra:

\[
Q_{A\to B}^{\dagger}Q_{B\to A}^{\dagger}(a)=a
\quad
\forall a\in\mathcal A_A.
\]

This is the exact candidate bridge from algebra-relative finality to
composable handoff.

## Controls

1. **Retained-lineage positive control:** a controlled copy followed by its
   inverse using the same retained carrier closes exactly.
2. **Discard-and-refresh hostile control:** trace the carrier after the first
   operation and supply a fresh blank carrier to the inverse. The reduced
   loop should dephase a coherent input although the full unitary loop is
   identity.
3. **Noncommuting-reduction control:** compose two exact dephasings in
   nonorthogonal bases in both orders. The outputs should differ.
4. **Commuting controls:** identical and mutually unbiased Pauli dephasings
   should commute in the chosen two-dimensional specimen.
5. **Representation control:** transform state, channels, and readout
   together. Every probability should remain invariant.

## Local-model learning gate

- **Question:** find the smallest exact witness separating full-loop closure,
  reduced-loop closure, and order-dependent reduction.
- **Research-only baseline:** channel theory predicts the distinction, but
  does not by itself provide the smallest typed DU witness and exact
  curvature-admission gate.
- **Local learning delta:** exact rational/algebraic loop defects, smallest
  order witness, and the specific condition that a future physical
  curvature proposal must beat.
- **Generated not encoded:** the hostile angle and input are fixed before
  evaluation; the probe computes the complete channel outputs and
  representation controls rather than labeling them.
- **Pre-hardware checkpoint:** exact symbolic defects or a null showing that
  the proposed distinction collapses.
- **Decision changed:** a positive ordinary-QM witness prevents promotion of
  reduced path dependence as curvature; a null would leave the curvature
  candidate less absorbed.
- **Minimal build:** two qubits for loop closure and one Bloch qubit for
  noncommuting reduction.
- **Stop/hardware boundary:** stop after exact finite proof controls. No
  simulation scaling, provider work, or hardware is warranted.

## Cheapest kill and stop

**Cheapest kill of the moonshot inference:** one exact full-unitary identity
loop whose reduced version fails solely because an intermediate carrier was
discarded.

**Cheapest kill of the formal result:** an algebraic error in the
necessary-and-sufficient closure identity or failure of the positive and
hostile controls.

Stop after banking one of:

```text
FULL_AND_REDUCED_LOOP_CLOSE
REDUCED_LOOP_DEFECT_FROM_DISCARDED_LINEAGE
NONCOMMUTING_REDUCTION_PATH_DEPENDENCE
REPRESENTATION_INVARIANT_PHYSICAL_HOLONOMY_CANDIDATE
STANDARD_QM_COARSE_GRAINING_ABSORPTION
NO_READY_SUCCESSOR
```

No result here selects the reference system, access boundary, assignment,
record algebra, archive, or certification rule.
