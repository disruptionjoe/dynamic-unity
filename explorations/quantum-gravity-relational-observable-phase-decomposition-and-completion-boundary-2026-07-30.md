---
title: "Quantum-gravity relational observable, phase decomposition, and completion boundary"
status: completed_scoped_result
doc_type: primary_source_follow_on_collision_exact_nonidentifiability_theorem_and_empirical_reopener
created: 2026-07-30
hypothesis_id: HC-DU-149
run_id: RUN-20260730-025707-relational-phase-decomposition-gate
authority: "Joe direct chat: Go"
lanes:
  - lane_1
  - lane_2
  - lane_3
  - lane_4
  - lane_6
  - lane_7
channels:
  - CH-COLLIDE
  - CH-FORMAL
  - CH-MODEL
  - CH-EMPIRICAL
maximum_grade: "Scoped Grade 4 phase-decomposition nonidentifiability, relational-probability invariance, and primary-source completion boundary; Grade 5 only after one observed relational no-refit phase surface survives gauge, split, back-reaction, truncation, rival-model, nuisance, and acquisition controls"
probe: "../tests/du_relational_phase_decomposition_gate_probe.py"
artifact: "../tests/artifacts/du_relational_phase_decomposition_gate_result.json"
---

# Quantum-gravity relational observable and phase-decomposition gate

## Executive result

The swing returned:

```text
THE_EMPIRICAL_TARGET_IS_A_COMPLETE_RELATIONAL_JOINT_PROBABILITY
+ A_COMMUTATOR_LABELLED_HAMILTONIAN_SUBTERM_IS_NOT_SEPARATELY_IDENTIFIABLE
+ EQUIVALENT_FREE_INTERACTION_SPLITS_CAN_CHANGE_OR_REMOVE_THAT_COMMUTATOR
+ FULLY_TRANSFORMED_RELATIONAL_PROBABILITIES_REMAIN_INVARIANT
+ CHEN_GIACOMINI_2026_SUPPLIES_GAUGE_INVARIANT_REFERENCE_FIELD_MACHINERY
+ THE_REFERENCE_FIELDS_ARE_PHYSICAL_AND_BACKREACT
+ NO_EXPLICIT_TRANSPORT_OF_THE_2025_PHASE_INTO_THAT_MACHINERY_WAS_FOUND
+ PROBE_BACKREACTION_AND_SAME_ORDER_COMPLETION_REMAIN_OPEN
+ THE_PHASE_SURFACE_REMAINS_A_CONDITIONAL_EMPIRICAL_REOPENER
+ NO_DU_PREDICTION_HARDWARE_PATH_OR_READY_SUCCESSOR
```

`HC-DU-148` was right to preserve Chen and Giacomini's proposed phase
**surface** as conditional empirical content and wrong only if read as already
having completed every invariance burden. The 2025 calculation is performed
in temporal gauge, neglects the probe's gravitational back-reaction, neglects
declared source/probe and longitudinal-field commutators, and evaluates a
selected Zassenhaus expansion through \(t^3\). Those are legitimate
approximations for a proposal. They also mean that the named pieces
\(\Theta^{(0)},\Theta^{(1)},\Theta^{(2)}\) are derivation-level quantities
until the complete measured probability is shown to be invariant under the
admitted gauge, reference, split, and same-order completion class.

The same authors' 2026 quantum-reference-field work supplies exactly the
formal direction needed to close part of this gap:

- four dynamical scalar reference fields enter the gravitational constraints;
- relational observables are gauge invariant;
- unitary maps relate reduced descriptions in different quantum reference
  fields;
- the reference fields' stress-energy and back-reaction are not ignored; and
- a relational von Neumann measurement scheme makes a class of observables
  operationally accessible in principle.

That is a substantial new bridge, not a cosmetic citation. But the inspected
paper does not explicitly rederive the 2025 wide-source or gravitational
commutator phase, and its more complete relativistic measurement theory is
left for future work. A targeted title, text, and reference search found no
published transport theorem. This is a bounded search result, not proof that
no such calculation exists.

The exact finite control proves why the transport is necessary. One fixed
Hamiltonian \(H=X+Z\) has the family of decompositions

\[
H_0^{(\alpha)}=(1-\alpha)X,
\qquad
H_I^{(\alpha)}=Z+\alpha X.
\tag{1}
\]

Every \(\alpha\) gives the same \(H\), exact propagator, and endpoint
probabilities. Yet

\[
[H_0^{(\alpha)},H_I^{(\alpha)}]
=(1-\alpha)[X,Z]
\tag{2}
\]

varies continuously and is zero at \(\alpha=1\). Therefore a phase
contribution named by the commutator of one supplied “free” and “interaction”
split is not itself an observable merely because the total phase is.

This control does **not** show that Chen and Giacomini chose an illegitimate
split or that their phase vanishes in another gravitational gauge. It proves
the narrower burden:

> The experimentally creditable object is the complete relational joint
> outcome law. A commutator-labelled contribution earns separate physical
> status only after the theory selects the decomposition and the contribution
> survives the relevant relational transformations and same-order
> completion.

The positive side also remains exact. If state, dynamics, and readout are
transformed together by one unitary perspective map, the Born probability is
unchanged. If the readout is silently held fixed while the other objects are
transformed, the probability changes. A “gauge-invariant phase” therefore
requires a complete transformed preparation-and-measurement contract, not
only a transformed Hamiltonian symbol.

No Dynamic Unity prediction, observed packet, hardware path, or ready
successor follows. The reopener is now much sharper.

## 1. What the 2025 proposal actually fixes

Chen and Giacomini's published
[Physical Review X paper](https://doi.org/10.1103/hl1c-t8z9) and
[full preprint](https://arxiv.org/abs/2402.10288) study linearized quantum
gravity for delocalized matter sources.

The wide-source result remains as classified in `HC-DU-148`: its functional
form can exceed the Newton potential and the declared classical or
semiclassical rivals, while an explicit ad hoc matter-only representation
blocks unique field ontology.

The commutator-phase construction is more delicate. The paper fixes:

1. a static general quantum source and moving probe;
2. externally controlled source and probe potentials;
3. temporal gauge \(h_{0\mu}=0\);
4. a field state constrained by the source alone;
5. negligible probe back-reaction, so the probe does not change that field
   state or its expectation values;
6. a weak-commutation condition which neglects the longitudinal
   field-momentum commutator on the physical state;
7. retention of the transverse field commutator;
8. omission of other source/probe position-momentum commutators from the
   displayed effect; and
9. a Zassenhaus expansion evaluated through \(t^3\).

The source explicitly notes that the evolution time used in the polynomial
is temporal-gauge time and differs from laboratory time only by a negligible
correction at the retained order. It also argues that higher expansion terms
do not alter the qualitative dependence on the gravitational canonical
commutator.

That supports a proposal-level physical signal. It does not yet prove that
each displayed term is independently gauge invariant or separately
measurable. The source's own observable is ultimately a relative phase
accessed through a joint source--probe experiment, not an instrument that
reads “the first gravitational commutator term” in isolation.

## 2. What the 2026 follow-on adds

Chen and Giacomini's
[Quantum Reference Fields Transformations in Linearized Quantum
Gravity](https://arxiv.org/abs/2606.09344) addresses a real upstream issue:
without external coordinates, matter and geometry must be specified
relationally using physical internal systems.

Its construction adds four scalar quantum reference fields \(X_A^{(\mu)}\)
whose stress-energy enters the linearized gravitational constraints. This
matters for Dynamic Unity because it does not treat the observer's coordinate
system as a free label. The reference field is part of the physical
completion and can back-react.

The paper then:

- constructs perspective-neutral relational observables;
- reduces them to the perspective of a chosen quantum reference field;
- derives unitary transformations between reference-field perspectives;
- shows that the gravitational perturbation transforms with the form of a
  linearized diffeomorphism whose parameter is now a physical quantum field;
- keeps the relational observables invariant under ordinary
  diffeomorphisms; and
- outlines a relational von Neumann measurement interaction built from
  constraint-compatible observables.

The construction is perturbative and imposes admissibility conditions on the
reference fields. It distinguishes a pure perspective change from a unitary
which changes the physical configuration. It also states that more
sophisticated relativistic relational measurement theory remains future
work.

### 2.1 What this closes

It refutes an overstrong diagnosis that linearized quantum gravity has no
available language for:

- physical reference systems;
- gauge-invariant relational observables;
- transformations between internal perspectives;
- reference-system back-reaction; or
- operational access in principle.

Dynamic Unity should therefore not park the 2025 phase merely because it was
written in temporal gauge. There is now a concrete native framework in which
to ask whether the phase survives.

### 2.2 What it does not yet close

The inspected follow-on does not:

- cite or rederive the 2025 commutator-phase proposal;
- construct its particular source, probe, and interference readout as
  relational observables;
- include the probe back-reaction omitted in the 2025 calculation;
- show that the \(t^3\) coefficient is reference-field independent;
- prove that the separation into \(\Theta^{(0)},\Theta^{(1)},\Theta^{(2)}\)
  is invariant;
- include every same-order source, probe, constraint, and reference-field
  term; or
- produce a complete acquisition packet.

The 2026 paper supplies machinery and a legitimate reopener. It is not the
missing transport calculation.

## 3. Exact split-decomposition theorem

### 3.1 Statement

Let a total Hamiltonian \(H\) be decomposed as \(H=H_0+H_I\). Suppose only the
total evolution and endpoint preparation/readout statistics are physically
fixed. Then a commutator \([H_0,H_I]\) is not identifiable from those
statistics without an independently selected decomposition.

### 3.2 Smallest witness

Take a qubit and Pauli operators \(X,Z\). For
\(\alpha\in[0,1]\), define Equation (1). Then:

\[
H_0^{(\alpha)}+H_I^{(\alpha)}=X+Z
\quad\text{for every }\alpha,
\tag{3}
\]

while Equation (2) holds. The Frobenius norm of the labelled commutator runs
from \(2\sqrt2\) at \(\alpha=0\) to zero at \(\alpha=1\). Nevertheless,

\[
U(t)=e^{-it(X+Z)}
\tag{4}
\]

is identical throughout the family. Every complete endpoint statistic is
therefore identical.

The regression checks \(\alpha=0,\frac14,\frac12,\frac34,1\). All five total
Hamiltonians agree exactly, and all five labelled commutator norms differ.

### 3.3 Scope

The theorem is elementary decomposition nonidentifiability. It is not:

- a diffeomorphism;
- a gravitational gauge transformation;
- a claim that the free-field/interaction split lacks physical motivation;
- a calculation of the 2025 phase;
- a proof that its total fringe signal is gauge dependent; or
- a rival gravity theory.

It blocks only this inference:

```text
a BCH/Zassenhaus term contains [H_G,H_I]
therefore that term is a separately invariant observable
```

A physical theory can repair the inference by selecting the split and proving
the resulting coefficient survives the admitted transformation and
completion class.

## 4. Exact relational-probability control

For state \(\rho\), evolution \(U\), and effect \(E\), the measured
probability is

\[
p=\operatorname{Tr}(E\,U\rho U^\dagger).
\tag{5}
\]

Under one unitary perspective map \(W\),

\[
\rho'=W\rho W^\dagger,\qquad
U'=WUW^\dagger,\qquad
E'=WEW^\dagger,
\tag{6}
\]

cyclicity gives

\[
\operatorname{Tr}(E'U'\rho'U'^\dagger)=p.
\tag{7}
\]

The finite regression uses \(U=e^{-0.37i(X+Z)}\), a \(Z\)-perspective
rotation by \(0.61\), an \(X\)-basis input, and a \(Y\)-basis readout. The
fully transformed contract agrees to \(10^{-12}\). Holding the coordinate
readout fixed instead changes the probability by more than \(10^{-3}\), the
required positive control.

This is the correct structural analogue of the 2026 reference-field move:
transforming a symbol is insufficient; the complete relational
preparation--dynamics--measurement tuple carries the invariant probability.

## 5. Sharpened empirical reopener

The next admissible object is not:

```text
observe Theta^(1) by name
```

It is:

```text
one relational joint source--probe outcome distribution
+ a preregistered multi-configuration phase estimator
+ one unchanged reference-field and measurement construction
+ all same-order terms
+ frozen gauge and perspective covariance checks
+ frozen back-reaction and truncation error
+ frozen rival laws and nuisance parameters
+ complete acquisition lineage
```

The minimum theory packet must do the following.

### Joint A — relational construction

Express the source preparation, probe trajectory, clock/time variable, metric
perturbation, interaction, and final joint readout as Dirac/relational
observables in one admissible quantum-reference-field completion.

### Joint B — same-order completion

Include or rigorously bound:

- probe gravitational back-reaction;
- reference-field stress-energy and back-reaction;
- the source/probe commutators omitted from the displayed 2025 term;
- the longitudinal constraint contribution;
- all terms at the same order in \(G\), time, and experimental controls; and
- the remainder from truncating the expansion.

The requirement is not “calculate everything exactly.” It is “show that the
held-out coefficient is not an artifact of dropping an equally large term.”

### Joint C — perspective covariance

Transform the entire preparation--dynamics--measurement packet between at
least two admissible quantum reference fields and prove equality of the
complete outcome law. The internal decomposition may change. The
preregistered phase estimator must not.

### Joint D — no-refit functional excess

Across held-out source shapes, probe stress-energy profiles, durations, and
controls, fit the candidate laws only on the training subset. Compare:

- the Newton potential;
- the declared classical and semiclassical rivals;
- physically motivated direct-action/influence-functional rivals;
- the completed relational linearized-QG prediction; and
- acquisition and nuisance alternatives.

The claim is model-class excess only if one frozen phase surface survives.
Unique field ontology still requires mediator-facing provenance, exclusive
mediation, or a theorem excluding the matched representation class.

## 6. Decision table

| Outcome | Dynamic Unity disposition |
|---|---|
| The complete relational probability retains the proposed held-out scaling | bank conditional model-class excess; seek an implementation-complete packet |
| Total fringe survives but the named commutator pieces mix | preserve the observable, retire separate ontological attribution to the pieces |
| Same-order back-reaction or omitted terms cancel the scaling | close the commutator-phase reopener; retain the methodological result |
| Two reference-field perspectives give different complete outcome laws | the construction is incomplete or inconsistent at the claimed order |
| A direct-action rival matches after one frozen fit | field ontology remains unselected; compare law selection and other observables |
| Only detector, clock, or reference refitting preserves the signal | classify as supplied-interface absorption |

## 7. Dynamic Unity meaning

The swing does not close the high-ceiling possibility from `HC-DU-148`. It
improves its type.

Before:

```text
look for a gravitational commutator phase
```

After:

```text
look for a relational joint probability surface whose excess remains after
the commutator decomposition is allowed to move
```

That is closer to the North Star. Dynamic Unity cares whether a physically
selected record determines a held-out target. Here:

- the record is the complete relational source--probe transcript;
- the target is the held-out multi-configuration outcome distribution;
- the completion fibre includes gauge/reference descriptions,
  free/interaction splits, same-order back-reaction, rival realizations,
  nuisance models, and acquisition histories; and
- a physical remainder exists only if the target varies after every
  legitimate quotient has been taken, not because one derivation names a
  component differently.

The result is Grade 4 for the exact finite nonidentifiability theorem,
relational covariance control, and scoped primary-source boundary. It is not
Grade 5 physics. The repository remains quiescent because no completed
relational calculation or observed packet is ready for execution.

## 8. Sources and search boundary

Primary sources:

- Lin-Qing Chen and Flaminia Giacomini,
  [*Quantum Effects in Gravity Beyond the Newton Potential from a
  Delocalized Quantum Source*](https://doi.org/10.1103/hl1c-t8z9),
  *Physical Review X* **15**, 031063 (2025);
  [full derivation](https://arxiv.org/abs/2402.10288).
- Lin-Qing Chen and Flaminia Giacomini,
  [*Quantum Reference Fields Transformations in Linearized Quantum
  Gravity*](https://arxiv.org/abs/2606.09344) (2026).

The follow-on search was limited to the paper text and references plus
targeted title/author/phase/gauge/back-reaction searches available on
2026-07-30. No explicit transport of the 2025 phase was found. That absence
is recorded only as the current audit boundary.
