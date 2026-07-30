---
title: "Action-indexed physical selection frontier, antichain, and measurement-model boundary"
status: banked_scoped_result
doc_type: exploration
created: 2026-07-30
claim_id: HC-DU-160
run_id: RUN-20260730-113004-physical-selection-frontier
work_id: MPA-02-PHYSICAL-SELECTION-FRONTIER
action_id: MPA-02-PHYSICAL-SELECTION-FRONTIER
program_id: CCR-MINIMAL-PHYSICAL-ANTECEDENT-TO-FINITE-REMAINDER
owner_repo: dynamic-unity
evidence_grade: 4
maximum_grade: 4
---

# Action-indexed physical selection frontier

## Executive return

```text
INCOMPARABLE_MINIMAL_FRONTIERS
+ PARTIAL_SELECTION_FRONTIER
+ ACTION_CLASS_IS_BASE_INDEX
+ KNOWN_RESULT_ABSORPTION
```

There is no context-free object called **the** minimal physical antecedent.
The operational distinctions to be selected depend on the interventions,
readouts, and future responses admitted for the observer. The action/access
class must therefore index the selection problem rather than appear as one
more coordinate inside it.

For a fixed action class, however, the problem is exact:

> A bundle of antecedent coordinates selects the operational response class
> exactly when equality on that bundle implies equality of every admitted
> response. In a finite declared coordinate family, the selecting bundles
> form an upper set and their inclusion-minimal members form an antichain.
> There is one least bundle exactly when the intersection of all selecting
> bundles still selects.

An exact two-bit fixture realizes all three relevant cases as the action class
is enlarged: a zero-coordinate minimum, two incomparable minima, and three
incomparable minima. This is a finite control, not a physical theory.

A qubit measurement model supplies the physical positive control. Holding the
same dephasing channel fixed, changing either the coupling isometry or the
pointer observable changes the labelled instrument. Within that declared
two-coordinate model, coupling plus readout algebra is jointly sufficient and
each is individually necessary for the **formal instrument**. Neither selects
a sampler, one-run outcome, material archive, occurrence provenance, or
observer access.

The theorem is absorbed by finite sufficient-statistic, candidate-key, and
measurement-model mathematics. Dynamic Unity's useful increment is the typed
correction:

```text
action/access class H
  indexes the operational equivalence to be selected

coupling + readout + material carrier + provenance mechanisms
  are candidate antecedents within that indexed problem

informativeness + formation + retention + accessibility
  are predicates the selected packet must satisfy
```

This correction prevents a false universal minimum while preserving a
source-pinnable path to the material-substitution gate. Swing 3 is not
activated here.

## 1. Typed problem

Let \(M\) be a declared completion set and let

\[
R_H:M\longrightarrow Y_H
\]

collect every response admitted by a fixed action/access class \(H\).
Equality under \(R_H\) is operational equivalence:

\[
m\sim_Hm'
\quad\Longleftrightarrow\quad
R_H(m)=R_H(m').
\]

Let \(J\) be a finite, target-blind family of candidate antecedent coordinates

\[
a_j:M\longrightarrow A_j,
\qquad j\in J.
\]

For \(S\subseteq J\), write

\[
a_S=(a_j)_{j\in S}.
\]

The bundle \(S\) **selects the \(H\)-response class** when

\[
a_S(m)=a_S(m')
\Longrightarrow
R_H(m)=R_H(m')
\tag{1}
\]

for every \(m,m'\in M\). Equivalently, as equivalence relations,

\[
\ker(a_S)\subseteq\ker(R_H).
\tag{2}
\]

This is a factorization/sufficiency statement. It does not assert that nature
selects a value of \(a_S\), that the coordinates are material, or that an
observer can access them.

### Why \(H\) is not another coordinate

Removing a coupling while holding \(H\) fixed asks whether the same
operational distinctions remain selected. Removing \(H\) changes which
distinctions count as operational. It changes the codomain and kernel of the
selection target itself.

Consequently, counterfactually minimizing

```text
coupling, readout, archive, provenance, H
```

inside one ordinary subset poset is ill typed. The correct object is a family
of antecedent posets indexed by \(H\). Selecting \(H\) physically is a
separate controller, action-envelope, and access problem.

## 2. Finite selection-frontier theorem

Define

\[
\mathcal U_H
=
\{S\subseteq J:\ker(a_S)\subseteq\ker(R_H)\}.
\]

### Proposition 1 — upper closure

If \(S\in\mathcal U_H\) and \(S\subseteq T\subseteq J\), then
\(T\in\mathcal U_H\).

### Proof

Adding coordinates can only refine their common kernel:

\[
\ker(a_T)\subseteq\ker(a_S)\subseteq\ker(R_H).
\]

### Proposition 2 — frontier antichain and unique-minimum criterion

The inclusion-minimal members

\[
\mathfrak F_H=\min_{\subseteq}\mathcal U_H
\]

form an antichain. They contain one least bundle exactly when

\[
\bigcap_{S\in\mathcal U_H}S
\in\mathcal U_H.
\tag{3}
\]

### Proof

Two distinct inclusion-minimal elements cannot contain one another, so
\(\mathfrak F_H\) is an antichain. If the intersection in (3) selects, it is
contained in every selecting bundle and is the unique least element.
Conversely, because \(J\) is finite, every selecting bundle contains an
inclusion-minimal selecting bundle. If that minimum is unique, every
selecting bundle contains it, so it equals the intersection.

### Proposition 3 — action refinement is antitone

Suppose \(H\preceq H'\) means every \(H\)-response is recoverable from the
\(H'\)-response. Then

\[
\ker(R_{H'})\subseteq\ker(R_H)
\]

and

\[
\mathcal U_{H'}\subseteq\mathcal U_H.
\tag{4}
\]

### Meaning

A stronger action class distinguishes at least as many completions. Fewer
antecedent bundles suffice to select all of those distinctions. The minimal
frontier can split, jump, or acquire larger bundles when capability expands.
There is no contradiction in one physical system having different minimal
frontiers for differently capable observers.

## 3. Exact finite antichain

Take

\[
M=\mathbb F_2^2
\]

with completions \((b,c)\), and declare three target-blind coordinates:

\[
a_b=b,\qquad
a_c=c,\qquad
a_w=b\oplus c.
\]

Use three nested response classes:

| action class | response \(R_H\) | inclusion-minimal selecting bundles |
|---|---|---|
| no access | constant | \(\{\varnothing\}\) |
| outcome access | \(b\) | \(\{\{b\},\{c,w\}\}\) |
| audit access | \((b,c)\) | \(\{\{b,c\},\{b,w\},\{c,w\}\}\) |

The middle line has two incomparable minima: the target bit directly, or the
other bit plus parity. The final line has all three two-coordinate
candidate keys. Exact enumeration also verifies

\[
\mathcal U_{\rm audit}
\subset
\mathcal U_{\rm outcome}
\subset
\mathcal U_{\rm none}.
\]

This fixture proves that antichains and capability-indexed frontier changes
are real mathematical possibilities. It is fully absorbed by elementary
candidate-key, parity/secret-sharing, and sufficient-statistic theory. It is
not evidence that nature uses these bits or that any coordinate is a record.

## 4. Qubit measurement-model boundary

Let the system and pointer both be qubits. A measurement model with coupling
isometry \(V\) and pointer PVM \(E=\{E_x\}\) induces

\[
\Phi_x(\rho)
=
\operatorname{Tr}_{P}
\left[
(I\otimes E_x)V\rho V^\dagger
\right].
\tag{5}
\]

### Copy coupling with a \(Z\) pointer

Define

\[
V_{\rm copy}|0\rangle=|0\rangle|0\rangle,
\qquad
V_{\rm copy}|1\rangle=|1\rangle|1\rangle.
\]

Reading the pointer in the \(Z\) basis gives

\[
\Phi_0(\rho)=P_0\rho P_0,
\qquad
\Phi_1(\rho)=P_1\rho P_1.
\tag{6}
\]

Its unlabelled channel is \(Z\)-dephasing:

\[
\Delta_Z(\rho)=P_0\rho P_0+P_1\rho P_1.
\]

### Same coupling, different pointer

Read the same pointer in the \(X\) basis. The conditional maps become

\[
\Phi_+(\rho)=\frac12\rho,
\qquad
\Phi_-(\rho)=\frac12 Z\rho Z.
\tag{7}
\]

They still sum to \(\Delta_Z\), but the labelled instrument differs from
(6). Thus the coupling and unlabelled process do not select the readout
algebra.

### Same pointer, different coupling

Hold the pointer \(Z\) PVM fixed and use

\[
V_{\rm phase}
=
\frac1{\sqrt2}
\left(
I\otimes|0\rangle+Z\otimes|1\rangle
\right).
\]

The resulting instrument is again (7), and its sum is again \(\Delta_Z\).
Thus the pointer algebra and unlabelled process do not select the coupling
realization.

Within the frozen candidate family \(\{V,E\}\), the pair determines (5),
while either coordinate alone admits the incompatible instruments (6) and
(7). Hence

\[
\mathfrak F_{\rm formal\ instrument}=\{\{V,E\}\}.
\]

This is a scoped unique minimum for a formal measurement model, not a
universal physical selector. The apparatus initial state and system-pointer
split are already built into the declaration.

Minimal measurement-model and instrument-dilation work establishes the
relevant representation theory and its unitary freedoms; complete observable
measurements also show that changing pointer refinement changes what the
measurement resolves. See
[Pellonpää and Tukiainen](https://arxiv.org/abs/1509.08886) and
[Pellonpää](https://arxiv.org/abs/1206.2506). Operationally complete
multi-time response additionally requires intervention structure of the sort
formalized by process tensors; see
[Pollock et al.](https://arxiv.org/abs/1512.00589).

## 5. Complete-packet counterfactuals

The formal minimum above does not lift automatically to the complete physical
record packet.

| removed structure | what remains | exact loss |
|---|---|---|
| sampler | an instrument-valued probability law | no selected one-run realization |
| material carrier/archive | a sampled value or formal branch | no blank-to-written retained physical trace |
| provenance/lineage | a terminal value | no distinction between formed, copied, prewritten, erased, or source-swapped histories |
| reset semantics | a retained value | no declared boundary on older readable memory |
| action/access class \(H\) | possibly a physical archive | no fixed operational equivalence or proof that a particular observer can read/use it |

The first separation is already enforced by `HC-DU-156` and `HC-DU-159`;
the archive separation by `HC-DU-142`; and the provenance/access separations
by the formed-record and action-relative results preceding this campaign.
The present swing reuses rather than rebuilds those witnesses.

Experimental quantum-instrument tomography reinforces the typing: a
mid-circuit measurement has both a classical output and a conditional quantum
output, and characterizing it requires more than its unlabelled channel. See
[Rudinger et al.](https://arxiv.org/abs/2103.03008). That supports the
measurement-model boundary; it does not physically choose an archive or
observer.

## 6. Selected-versus-supplied ledger

| object | status in this result |
|---|---|
| completion family \(M\) | supplied |
| action/access class \(H\) | supplied base index |
| response map \(R_H\) | supplied by the operational contract |
| candidate antecedent coordinates | declared target-blind |
| selecting-family theorem | derived |
| finite antichain | exact finite construction |
| system/pointer split and pointer initialization | supplied |
| coupling \(V\) and pointer PVM \(E\) | exact formal-instrument frontier coordinates |
| formal instrument given \(V,E\) | calculated |
| physical sampler and one-run outcome | unselected |
| material carrier, retention, reset, provenance | unselected |
| observer access/action envelope | unselected and not a same-level coordinate |
| new physical law or observable excess | absent |

## 7. Absorber audit

The component mathematics is mature:

- finite sufficient statistics and candidate keys absorb the kernel/frontier
  theorem and parity fixture;
- quantum instruments and measurement dilations absorb the \(V,E\) model;
- dilation freedom absorbs the fact that an unlabelled channel does not
  determine a unique measurement realization;
- process tensors absorb the need to declare the multi-time intervention
  class; and
- experimental instrument tomography absorbs the classical-output plus
  conditional-quantum-output typing.

The result therefore claims no new theorem of quantum information and no new
physics. Its Dynamic Unity value is architectural and exact: it prevents the
program from asking for one universal minimum across changing capability
classes, and it identifies coupling and readout as coordinates that a
source-pinned material assay may vary without confusing them with the action
index.

## 8. Campaign disposition

The pre-registered return is:

```text
INCOMPARABLE_MINIMAL_FRONTIERS
+ PARTIAL_SELECTION_FRONTIER
+ ACTION_CLASS_IS_BASE_INDEX
+ KNOWN_RESULT_ABSORPTION
```

Swing 2 is complete at scoped Grade 4.

Swing 3's scientific prerequisite is satisfied only in this limited sense:
coupling and readout access survive as genuine frontier coordinates. Before
Swing 3 can run, one of them must be pinned to a primary-source physical
platform and expressed as a target-blind material substitution with a frozen
nuisance span. This result neither chooses that platform nor authorizes the
next swing.

## Reproducibility

The exact finite and qubit controls are in:

```text
tests/du_action_indexed_selection_frontier_probe.py
tests/artifacts/du_action_indexed_selection_frontier_result.json
```

Passing proves only the declared finite antichains and measurement-model
deletion witnesses. It establishes no universal selector, formed record,
observer, ontology, prediction, empirical result, or new physics.
