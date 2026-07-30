---
title: "Quantum-switch order record: relocation, access-relative causal definiteness, and first leak"
status: banked_scoped_result
doc_type: exploration
created: 2026-07-30
claim_id: HC-DU-173
run_id: RUN-20260730-165119-quantum-switch-order-record-relocation
work_id: QUANTUM-SWITCH-ORDER-RECORD-RELOCATION
action_id: QUANTUM-SWITCH-ORDER-RECORD-RELOCATION
program_id: CCR-MINIMAL-PHYSICAL-ANTECEDENT-TO-FINITE-REMAINDER
owner_repo: dynamic-unity
evidence_grade: 4
maximum_grade: 4
---

# Quantum-switch order record

## Executive result

The quantum switch supplies a genuinely different stage specimen from the
bare channels excluded by `HC-DU-172`: two operation orders can be coherently
controlled, and an additional physical carrier can become correlated with
the order branch.

The decisive distinction is:

> A distinguishable carrier of causal-order information can make the order
> classical for a restricted observer without selecting one globally
> actualized order. Under unitary quantum mechanics, the lost order coherence
> may reside in correlations with that carrier and reappear under a coherent
> extension of access.

For pure marker states with overlap
\(\gamma=\langle r_0|r_1\rangle\), the accessible order-interference
visibility and optimal marker distinguishability obey

\[
V=|\gamma|,
\qquad
D=\sqrt{1-|\gamma|^2},
\qquad
D^2+V^2=1.
\]

With orthogonal markers, the reduced order control has no interference. But
the coherent completion and the corresponding incoherent mixture have the
same diagonal order record and the same reduced control while differing
exactly under one joint \(X\otimes X\) action. Measuring the marker in a
complementary basis conditionally restores unit visibility. The record has
therefore **relocated** the coherence rather than destroyed it globally.

The 2026 process-matrix result of Benhaj, Sengupta, and Branciard supplies the
broader causal-order boundary: dephasing all relevant systems, or leaving
only the future coherent, makes bipartite processes and quantum circuits
with quantum control of causal order causally separable in their stated
classes; leaving one non-future system coherent can preserve causal
nonseparability.

The combined return is:

```text
ORDER_COHERENCE_RELOCATION
+ ACCESS_RELATIVE_CAUSAL_DEFINITENESS
+ EXACT_COHERENT_ACCESS_FIRST_LEAK
+ PURE_MARKER_COMPLEMENTARITY
+ KNOWN_PROCESS_MATRIX_AND_QUANTUM_ERASER_ABSORPTION
+ NO_GLOBAL_ACTUALIZATION
+ NO_PHYSICAL_RECORD_SELECTOR
+ NO_READY_SUCCESSOR
```

This is a scoped Grade-4 typed necessity/first-leak result. It is not a new
quantum-information theorem, a new causal-order theorem, new physics, or a
claim that the actual world has indefinite causal order.

## 1. Source collision

Four primary results fix the earned scope.

1. Goswami et al. experimentally realized a photonic quantum switch in which
   polarization coherently controls the order of two operations on a spatial
   mode, and reported a causal-witness violation 18 standard deviations
   beyond the definite-order bound:
   [arXiv:1803.04302](https://arxiv.org/abs/1803.04302).
2. Taddei, Nery, and Aolita formalized quantum control of causal orders as a
   resource and developed free process-matrix concatenations and
   distillation:
   [arXiv:1903.06180](https://arxiv.org/abs/1903.06180).
3. Benhaj, Sengupta, and Branciard proved dephasing conditions under which
   bipartite processes and the physically motivated QC-QC class become
   causally separable, while also showing that coherence in one non-future
   system can suffice for causal nonseparability:
   [arXiv:2605.22807](https://arxiv.org/abs/2605.22807).
4. Englert's which-way inequality bounds distinguishable path information
   against interference visibility:
   [Phys. Rev. Lett. 77, 2154
   (1996)](https://doi.org/10.1103/PhysRevLett.77.2154).

These sources do not establish a DU record ontology. They supply the process,
resource, dephasing, and complementarity mathematics against which the typed
claim must be graded.

## 2. Typed specimen

Let the control states label two causal orders:

\[
|0\rangle_C\leftrightarrow A\prec B,
\qquad
|1\rangle_C\leftrightarrow B\prec A.
\]

Let \(|w_0\rangle\) and \(|w_1\rangle\) denote the corresponding process
branches. A marker \(R\), initialized in a supplied blank state, becomes
correlated with the branch:

\[
|\Omega\rangle
=
\frac{1}{\sqrt2}
\left(
|0\rangle_C|w_0\rangle|r_0\rangle_R
+
e^{i\phi}|1\rangle_C|w_1\rangle|r_1\rangle_R
\right).
\tag{1}
\]

The object ladder is:

```text
coherently controlled process
  != branch-correlated quantum carrier
  != diagonal order observable
  != sampled one-run value
  != retained material archive
  != action-relative causal definiteness
  != global ontic actualization
```

The first two objects can exist under unitary dynamics. The later arrows
require additional typing.

## 3. Order-marker complementarity

Tracing out \(R\) multiplies every off-diagonal order term by

\[
\gamma=\langle r_0|r_1\rangle.
\tag{2}
\]

Thus a branch-interference observable normalized to unit visibility for an
unmarked pure control has

\[
V=|\gamma|.
\tag{3}
\]

For two equiprobable pure marker states, their optimal distinguishability is

\[
D=\frac12
\left\|
|r_0\rangle\!\langle r_0|
-
|r_1\rangle\!\langle r_1|
\right\|_1
=
\sqrt{1-|\gamma|^2}.
\tag{4}
\]

Therefore

\[
D^2+V^2=1.
\tag{5}
\]

The exact regression checks three rational cases:

| marker | \(V\) | \(D\) | \(D^2+V^2\) |
|---|---:|---:|---:|
| identical | \(1\) | \(0\) | \(1\) |
| \(3\)-\(4\)-\(5\) overlap | \(3/5\) | \(4/5\) | \(1\) |
| orthogonal | \(0\) | \(1\) | \(1\) |

This is ordinary pure-state complementarity applied to an order label. The
new DU value is the type diagnosis: record distinguishability and retained
order coherence are not two independent record-quality scores.

## 4. Exact relocation witness

For orthogonal markers, suppress the process branch factors and write the
order-control/marker completion as

\[
\rho_{\mathrm{coh}}
=
\frac12
\left(
|00\rangle\!\langle00|
+
|11\rangle\!\langle11|
+
|00\rangle\!\langle11|
+
|11\rangle\!\langle00|
\right).
\tag{6}
\]

Compare it with the incoherent completion

\[
\rho_{\mathrm{mix}}
=
\frac12
\left(
|00\rangle\!\langle00|
+
|11\rangle\!\langle11|
\right).
\tag{7}
\]

They have:

- the same diagonal order-marker distribution;
- the same reduced control state \(I/2\); and
- the same response under every action restricted to the joint diagonal
  algebra.

But

\[
\operatorname{tr}
\left[
\rho_{\mathrm{coh}}(X\otimes X)
\right]=1,
\qquad
\operatorname{tr}
\left[
\rho_{\mathrm{mix}}(X\otimes X)
\right]=0.
\tag{8}
\]

So the coherent joint action \(X\otimes X\) is an exact first leak. The
diagonal order record is final for the restricted action algebra and not
final for the enlarged coherent algebra.

### Quantum-eraser control

Condition the coherent state on the marker effects

\[
P_\pm=|\pm\rangle\!\langle\pm|.
\]

Each occurs with probability \(1/2\), and the conditional control states have

\[
\langle X\rangle_+=1,
\qquad
\langle X\rangle_-=-1.
\tag{9}
\]

The unconditioned expectation remains zero because the two conditional
fringes cancel. This is not retrocausality and does not rewrite a past order.
It shows that the coherent completion retained phase information absent from
the restricted marginal.

## 5. What dephasing earns

Benhaj, Sengupta, and Branciard prove more than the finite control above. In
their declared bipartite and QC-QC classes, sufficient system-wide dephasing
makes the effective process causally separable. That is a real theorem about
the reduced process class.

It does not imply:

```text
reduced causal separability
  => one globally selected causal order
  => an implementation-complete order archive
  => irreversible ontic actualization
```

A classical mixture of orders can be proper or improper relative to a larger
completion. Process-matrix causal separability classifies the admitted
operational object. It does not, by itself, select which purification,
environment, archive, or observer boundary physically realizes that object.

The new source also blocks an over-simple story in the other direction:
decohering one obvious control register is not the universal criterion.
Causal nonseparability can persist while one non-future system remains
coherent. Any DU finality claim must inventory the complete admitted coherent
support rather than name one preferred register.

## 6. Relation to the stage-local no-section result

`HC-DU-172` says a bare end-to-end channel cannot naturally supply an
informative earlier-stage label under every downstream continuation. The
quantum switch adds a stage-bearing carrier, but it exposes three levels that
must not be collapsed:

1. **coherent stage carrier:** a quantum system correlated with order;
2. **restricted classical order:** a diagonal algebra or dephased reduced
   process for which the orders form a classical mixture; and
3. **material finality:** a retained archive whose declared future action
   class cannot coherently reopen the order distinction.

The first exits the bare-arrow contract. The second can close a scoped
operational action class. Neither automatically supplies the third.

This is a useful correction to the phrase “marked cut.” A physical mark can
be a reversible quantum correlation. It becomes final only relative to a
declared access/action boundary, or under additional nonunitary dynamics that
must be independently justified.

## 7. Selected-versus-supplied ledger

| object | status |
|---|---|
| two process branches and operations \(A,B\) | supplied by the switch specimen |
| control/order correspondence | supplied |
| marker carrier and coupling | supplied |
| marker overlap \(\gamma\) | supplied physical parameter |
| reduced-coherence law | derived |
| pure-marker \(D\)-\(V\) tradeoff | derived, standard |
| diagonal order algebra | supplied access restriction |
| exact diagonal-record twin | derived |
| coherent \(X\otimes X\) first leak | derived |
| causal separability after declared dephasing | source-proved in stated classes |
| sampled one-run order | not selected |
| retained material archive and provenance | absent |
| observer/action boundary | supplied |
| global actualization or collapse | not derived |

## 8. Prediction and falsification status

The scoped standard-quantum prediction is:

> In a frozen two-branch controlled-order implementation with pure marker
> states, increasing physically available order distinguishability reduces
> unconditional branch interference according to
> \(D^2+V^2=1\); coherent marker-basis conditioning can recover the hidden
> interference.

This is measurable but not novel. Englert complementarity, quantum erasure,
and process-matrix dephasing absorb it.

A result would exceed the completed standard model only if, after a complete
implementation and nuisance audit, one found either:

- simultaneously perfect unconditional order interference and perfect
  available order distinguishability in the same action class; or
- failure of every coherent access extension to recover phase information
  where the complete unitary model predicts recovery.

No such result is claimed, and the present work does not authorize hardware.

## 9. North-Star consequence

The specimen advances Dynamic Unity in two ways.

First, it supplies a concrete stage-bearing structure that a bare channel
lacks: a physical order carrier. Second, it proves that formation of that
carrier does not settle finality without an action/access contract. The
smallest exact remainder is the off-diagonal completion exposed by coherent
joint access.

The correct reusable pattern is:

```text
formation of a quantum order carrier
  -> restricted causal definiteness
  -> coherent-access first leak
  -> material-finality question still open
```

That is compatible with DU's layered regional picture: different systems may
possess different causal-order quotients because their physically admitted
access algebras differ. It does not show that reality uses consensus, that
records are fundamental, or that one observer creates causal order.

No successor activates. Reopen only if a source-pinned physical theory or
implementation independently fixes the switch, marker formation,
dephasing/retention mechanism, archive lineage, and action boundary, then
supports a no-refit held-out causal witness.

## Final status

**BANKED SCOPED RESULT / A DISTINGUISHABLE CAUSAL-ORDER CARRIER CAN MAKE A
REDUCED QUANTUM-CONTROLLED PROCESS CLASSICAL FOR A RESTRICTED ACTION CLASS
WITHOUT SELECTING ONE GLOBAL ORDER / PURE MARKERS OBEY THE EXACT
DISTINGUISHABILITY–VISIBILITY TRADEOFF / ORTHOGONAL MARKERS ADMIT AN EXACT
DIAGONAL-RECORD TWIN AND COHERENT \(X\otimes X\) FIRST LEAK / QUANTUM ERASURE
RESTORES CONDITIONAL INTERFERENCE / 2026 PROCESS-MATRIX DEPHASING RESULTS
SUPPLY THE BROADER CAUSAL-SEPARABILITY BOUNDARY / STANDARD COMPLEMENTARITY,
PURIFICATION, QUANTUM-ERASER, AND CAUSAL-ORDER RESOURCE THEORY ABSORB THE
MATHEMATICS / NO GLOBAL ACTUALIZATION, MATERIAL RECORD SELECTOR, NEW PHYSICS,
PAPER, HARDWARE, OR READY SUCCESSOR.**
