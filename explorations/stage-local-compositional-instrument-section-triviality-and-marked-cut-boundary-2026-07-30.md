---
title: "Stage-local compositional instrument-section triviality and marked-cut boundary"
status: banked_scoped_result
doc_type: exploration
created: 2026-07-30
claim_id: HC-DU-172
run_id: RUN-20260730-162741-stage-local-instrument-section
work_id: STAGE-LOCAL-INSTRUMENT-SECTION-TRIVIALITY
action_id: STAGE-LOCAL-INSTRUMENT-SECTION-TRIVIALITY
program_id: CCR-MINIMAL-PHYSICAL-ANTECEDENT-TO-FINITE-REMAINDER
owner_repo: dynamic-unity
evidence_grade: 4
maximum_grade: 4
---

# Stage-local compositional instrument-section triviality

## Executive return

```text
BARE_PROCESS_STAGE_LOCAL_SECTION_TRIVIALITY
+ MARKED_COMPOSITION_CUT_NECESSITY
+ INFORMATIVE_MARKED_INSTRUMENT_POSITIVE_CONTROL
+ KNOWN_CP_MAP_AND_INFORMATION_DISTURBANCE_ABSORPTION
+ MATERIAL_RECORD_SELECTION_UNCHANGED
+ NO_READY_SUCCESSOR
```

`HC-DU-159` proved that a unitary channel has no informative
instrument refinement and that nonunitary channels can have nontrivial
mathematical decompositions. The present result sharpens the scope:

> If a finite-dimensional channel is required to select the same
> stage-local outcome decomposition naturally under **every downstream
> channel**, then every selected component is only a process-independent
> coin multiple of the channel. This holds for every channel, not only
> unitaries.

The load-bearing requirement is downstream naturality. It says that attaching
arbitrary later dynamics does not change which earlier-stage event the label
names. That is exactly the requirement one would want from a provenance-bearing
stage record—but a bare end-to-end channel does not contain the stage boundary.

The result therefore does not show that physical records are impossible. It
shows that an informative record cannot be selected from a bare unmarked
process arrow while also pretending that its formation stage survives
arbitrary composition for free. At least one additional antecedent is needed:

- a marked composition cut or event;
- an explicit classical/central output sector;
- a selected environment, dilation, detector, or output field;
- a restricted class of downstream maps that preserves the record; or
- a material archive and provenance path.

The component mathematics is elementary and absorbed by Choi theory,
Radon--Nikodym order for completely positive maps, pure transformations, and
no-information-without-disturbance. Dynamic Unity earns a typed necessity
boundary, not a new quantum-information theorem or new physics.

## 1. Frozen object and contract

Let \(\mathsf{Chan}(A,B)\) denote finite-dimensional completely positive,
trace-preserving maps

\[
\Phi:\mathcal L(\mathcal H_A)\longrightarrow\mathcal L(\mathcal H_B).
\]

Fix a finite outcome set \(X\). An instrument section assigns to every
channel \(\Phi:A\to B\) completely positive trace-nonincreasing maps

\[
S_x(\Phi):A\to B
\qquad (x\in X)
\]

such that

\[
\sum_{x\in X}S_x(\Phi)=\Phi.
\tag{1}
\]

The new condition is **downstream stage-local naturality**:

\[
S_x(\Psi\circ\Phi)
=
\Psi\circ S_x(\Phi)
\tag{2}
\]

for every channel \(\Psi:B\to C\).

Equation (2) is stronger than covariance under a change of representation.
It asserts that the label selected at the stage of \(\Phi\) remains the same
label after arbitrary later processing. It also fixes one outcome alphabet:
the later channel does not append a second outcome.

No observer, material carrier, sampler, realized outcome, archive, reset,
access envelope, or held-out target enters this theorem.

## 2. Stage-local compositional triviality theorem

### Theorem

For every input system \(A\), any instrument section satisfying (1) and (2)
has the form

\[
S_x(\Phi)=p_x^{A}\Phi
\tag{3}
\]

for a probability vector \(p^A=(p_x^A)_{x\in X}\) independent of \(\Phi\)
and its input state.

Consequently, on every trace-one input \(\rho\),

\[
\operatorname{tr}S_x(\Phi)(\rho)=p_x^A.
\tag{4}
\]

The selected outcome is an uninformative coin toss.

### Proof

Apply (1) to the identity channel on \(A\):

\[
\sum_xS_x(\operatorname{id}_A)=\operatorname{id}_A.
\tag{5}
\]

The Choi operator of \(\operatorname{id}_A\) is the rank-one positive
operator

\[
J(\operatorname{id}_A)
=
|I_A\rangle\!\rangle\langle\!\langle I_A|.
\]

Complete positivity of every component gives

\[
0\le J(S_x(\operatorname{id}_A))
\le J(\operatorname{id}_A).
\]

Every positive operator dominated by a rank-one positive operator has the
same one-dimensional support. Therefore

\[
S_x(\operatorname{id}_A)=p_x^A\operatorname{id}_A,
\qquad
p_x^A\ge0,
\qquad
\sum_xp_x^A=1.
\tag{6}
\]

For an arbitrary channel \(\Phi:A\to B\), use
\(\Phi=\Phi\circ\operatorname{id}_A\) and (2):

\[
\begin{aligned}
S_x(\Phi)
&=S_x(\Phi\circ\operatorname{id}_A)\\
&=\Phi\circ S_x(\operatorname{id}_A)\\
&=p_x^A\Phi.
\end{aligned}
\]

This proves (3), and trace preservation gives (4). \(\square\)

### Scope

The proof needs only:

1. a category of finite-dimensional quantum channels;
2. CP components summing to the channel;
3. purity of the identity in the cone of CP maps; and
4. naturality under arbitrary downstream channels.

It does not use convex affinity, unitary covariance, a particular Kraus
representation, or a held-out target.

## 3. What this adds to `HC-DU-159`

`HC-DU-159` supplied three facts:

1. trivial coin sections exist universally;
2. every refinement of a unitary channel is such a coin section; and
3. nonunitary channels can have informative mathematical decompositions.

The third fact could be misread as leaving a universal process-only selector
open on the nonunitary sector. The theorem above closes that route under the
stage-local composition contract. A nonunitary channel can have an informative
instrument, but no assignment can choose such instruments for all channels
and commute with every downstream continuation.

The obstruction is not nonunitarity. It is loss of the stage boundary when a
factored history is replaced by one bare composite arrow.

## 4. Positive and hostile controls

### 4.1 Informative marked-stage control

For a qubit, define

\[
\mathcal M_0(\rho)=P_0\rho P_0,
\qquad
\mathcal M_1(\rho)=P_1\rho P_1.
\]

Then

\[
\mathcal M_0+\mathcal M_1=\Delta_Z,
\]

the dephasing channel. The outcome probabilities are \((1,0)\) on
\(|0\rangle\langle0|\) and \((0,1)\) on
\(|1\rangle\langle1|\). This is an informative instrument.

If the cut after \(\mathcal M\) is retained, later dynamics \(\Psi\) transports
the already selected components as

\[
\{\Psi\circ\mathcal M_x\}_x.
\]

They still sum to \(\Psi\circ\Delta_Z\). Nothing in the theorem forbids this:
the marked factorization or external outcome wire supplies the stage.

### 4.2 Bare-arrow hostile control

Apply downstream naturality to

\[
\Delta_Z
=
\Delta_Z\circ\operatorname{id}.
\]

Since the identity can only carry coin components
\(p_x\operatorname{id}\), equation (2) forces

\[
S_x(\Delta_Z)=p_x\Delta_Z,
\]

not \(\mathcal M_x\). Therefore the informative projective decomposition and
bare-arrow downstream naturality cannot both hold.

### 4.3 Restricted-morphism exit

An explicit classical output register or central sector can define an
informative split, and postprocessing that preserves that sector transports
it. This leaves the theorem's class by supplying a marked classical structure
or restricting the downstream maps. The exit is legitimate, but its price
must remain in the antecedent ledger.

## 5. Why the naturality premise is not free

Equation (2) can look innocent because it resembles ordinary functoriality.
It is not automatic.

The left side asks a selector looking only at the **whole composite channel**
to identify an outcome decomposition. The right side asks it to preserve an
outcome formed at a specified earlier stage. Those are the same task only if
the stage is already marked or reconstructible.

This is the exact Dynamic Unity boundary:

```text
bare end-to-end process
  != factored process with a marked cut
  != instrument at that cut
  != sampled outcome
  != material archive and provenance
```

In distributed-systems language, flattening a pipeline to its end-to-end
input/output function erases the log boundary at which an event was committed.
A later log cannot recover that boundary from functional equivalence alone.
That is a typed comparison, not an identification of quantum dynamics with a
database.

## 6. Absorber collision and novelty

The mathematics has strong prior absorbers.

- Raginsky reviews the Radon--Nikodym order interval of completely positive
  maps, which characterizes CP submaps dominated by a channel:
  [arXiv:math-ph/0303056](https://arxiv.org/abs/math-ph/0303056).
- D'Ariano, Perinotti, and Tosini treat tests as collections of operations
  summing to a channel and connect incompatibility with information extraction
  without disturbance:
  [arXiv:2204.07956](https://arxiv.org/abs/2204.07956).
- Heinosaari, Leppäjärvi, and Plávala characterize trivial coin-toss
  observables in no-information/no-disturbance results and show that the
  exact implication is theory-class dependent:
  [arXiv:1808.07376](https://arxiv.org/abs/1808.07376).
- Chiribella, D'Ariano, and Perinotti derive no-information-without-disturbance
  within operational theories with purification:
  [arXiv:0908.1583](https://arxiv.org/abs/0908.1583).

The two-line compositional proof is best treated as a direct corollary of
these mature structures, not advertised as new mathematics. The earned DU
increment is the typed interpretation:

> **stage-local provenance requires a stage-bearing physical antecedent.**

That is useful for stopping process-only reconstruction loops and for stating
the next reopener precisely.

## 7. North-Star consequence

The North Star is not closed. It is narrowed.

The next admissible physical interface candidate may not be only an
unlabelled channel or end-to-end process. It must expose, or dynamically
select, a stage-bearing structure that survives the declared continuation
class. Candidate forms include:

- an output algebra with a distinguished classical center;
- a spacetime-local detector coupling and output field;
- a source-pinned instrument dilation with a retained event wire;
- a physical archive whose later access maps preserve its lineage; or
- a process tensor with an independently selected, materially formed slot
  interface.

This theorem does not choose among them. It forbids crediting the bare arrow
for a cut that was supplied in its factorization.

## 8. Observer and campaign disposition

```text
OBSERVER_INDEX_IRRELEVANT_TO_SCOPED_THEOREM
```

The theorem is about process and stage typing. An observer index becomes
necessary only when access, action, resource, and certification semantics are
added. Those remain unselected.

The result is banked at scoped Grade 4 because it proves a necessity boundary
inside the frozen finite-dimensional class. It claims:

```text
NEW QUANTUM INFORMATION THEOREM: NO
NEW PHYSICS OR EMPIRICAL EXCESS: NO
EXACT PROCESS_ONLY_SELECTION_BOUNDARY: YES
MARKED_STAGE_OR_RESTRICTED_MORPHISM_REQUIREMENT: YES
MATERIAL_RECORD_SELECTED: NO
```

No scientific successor is activated. The QEC implementation-complete
reopener remains external-custody, and future local work must bring a genuinely
new stage-selecting physical antecedent rather than another bare-channel
decomposition.

## Final status

**BANKED SCOPED RESULT / DOWNSTREAM-NATURAL STAGE-LOCAL INSTRUMENT SECTIONS
ARE COIN-TOSS TRIVIAL / PROOF EXTENDS THE UNITARY CORNER TO EVERY CHANNEL
UNDER THE DECLARED NATURALITY CONTRACT / INFORMATIVE MARKED INSTRUMENT
PRESERVED AS POSITIVE CONTROL / MARKED CUT, CLASSICAL SECTOR, DILATION,
RESTRICTED MORPHISM, OR MATERIAL ARCHIVE REQUIRED / KNOWN CP-MAP AND
INFORMATION-DISTURBANCE ABSORPTION / NO NEW PHYSICS, PREDICTION, PAPER, OR
READY SUCCESSOR.**
