---
title: "Action-confusability graph no-go and higher-order formation profile"
status: earned_result
doc_type: research_exploration
created: 2026-07-27
claim_id: HC-DU-067
run_id: RUN-20260727-230941-action-confusability-no-go
program_id: CCR-CAPABILITY-RECORD-GALOIS-CLOSURE
authority: "Joe direct chat: Go"
owner_repo: dynamic-unity
grade: 4
---

# Action-confusability graph no-go

## Result in one sentence

An action-confusability graph formed by aggregating pairwise distinctions
over alternative physical interfaces can report a complete graph even when
no one interface jointly distinguishes any triple; the missing information
is exactly higher-order physical joint realizability, already typed by the
Admissible Record Envelope.

The minimum witness is the one-use unassisted Pauli-channel specimen.
Every pair of Pauli channels is perfectly distinguishable with a
pair-specific input, but no triple is perfectly distinguishable by one
unassisted qubit interface. A complete repetition-code syndrome interface
has the same aggregate pairwise graph and does distinguish all four error
labels jointly.

The result closes the graph-only form of `IT-A`. It does not supply a new
physical law, an endogenous interface selector, or a universal scalar
resource invariant.

## 1. Prior overlap and surviving delta

The cheap-kill audit found three occupied layers:

1. zero-error quantum communication and noncommutative graphs already encode
   perfect distinguishability for a fixed channel or operator space;
2. quantum channel discrimination already supplies the Pauli
   distinguishability and dimension arguments; and
3. `HC-DU-033E/038E` already defines the Admissible Record Envelope as a
   refinement order plus a physical joint-realizability complex.

`HC-DU-065` then attaches resource-Pareto formation receipts to that
complex. Therefore a new graph or a renamed compatibility hypergraph would
be duplicate work.

The surviving exact question is narrower:

> What is lost if an agent follows the proposed `IT-A` approach and
> collapses distinctions witnessed by different interventions into one
> pairwise action-confusability graph?

The answer is a quantifier and higher-order-formation failure.

## 2. Frozen typed contract

Let:

- \(X\) be a finite set of complete physical alternatives;
- \(b\) be a frozen resource budget;
- \(\mathcal I_b\) be the admitted physical interfaces under \(b\); and
- \(\rho_x^i\) be the complete accessible output state produced by
  alternative \(x\in X\) through interface \(i\in\mathcal I_b\).

An interface includes its preparation, occurrence identity, process uses,
reference systems, coupling, measurement, archive, provenance, decoder,
access route, and retained action horizon. Two interfaces that require
different preparations or measurements are alternatives, not automatically
one joint interface.

For each fixed interface \(i\), define

\[
\mathcal D_i
=
\left\{
S\subseteq X:
\operatorname{supp}\rho_x^i
\perp
\operatorname{supp}\rho_y^i
\text{ for all distinct }x,y\in S
\right\}.
\]

\(\mathcal D_i\) is a simplicial complex: every subset of a jointly
distinguishable set is jointly distinguishable. It is also the clique
complex of its own orthogonality graph \(G_i\). For one fixed family of
output states, pairwise orthogonal supports admit one projective support
measurement that distinguishes the whole family.

Now aggregate over alternative interfaces:

\[
\mathcal J_b
=
\bigcup_{i\in\mathcal I_b}\mathcal D_i.
\]

\(\mathcal J_b\) is the resource-indexed physical joint-realizability
complex. Its pairwise shadow is

\[
G_b=(X,E_b),
\qquad
\{x,y\}\in E_b
\iff
\{x,y\}\in\mathcal J_b.
\]

This document uses edges for perfect distinguishability. If
“confusability graph” is reserved for the complementary convention, replace
each graph by its complement; the loss of common-interface witness data is
unchanged.

Always,

\[
\mathcal J_b\subseteq\operatorname{Cl}(G_b),
\]

where \(\operatorname{Cl}\) is the flag or clique complex. Equality need not
hold because each edge of a clique may have a different witness interface.

## 3. Pairwise aggregation theorem

### Theorem 1 — fixed-interface sufficiency, aggregate insufficiency

For a fixed physical interface \(i\), its pairwise orthogonality graph
determines every jointly distinguishable subset:

\[
\mathcal D_i=\operatorname{Cl}(G_i).
\]

For an interface family \(\mathcal I_b\), its aggregate pairwise graph
\(G_b\) determines \(\mathcal J_b\) if and only if every clique of \(G_b\)
is jointly realized by at least one common interface:

\[
\forall S\in\operatorname{Cl}(G_b)\quad
\exists i\in\mathcal I_b:\ S\in\mathcal D_i.
\]

### Proof

For fixed \(i\), a set is a clique exactly when every pair of its output
supports is orthogonal. The direct sum of those supports then has one
support-valued measurement distinguishing every member, proving the first
statement.

By definition, a set belongs to \(\mathcal J_b\) exactly when one interface
witnesses the whole set. Since every such set is a clique in the aggregate
graph, \(\mathcal J_b\subseteq\operatorname{Cl}(G_b)\). Equality holds
exactly when every aggregate clique has a common witness. \(\square\)

The forbidden inference is

\[
\forall\{x,y\}\subseteq S\ \exists i_{xy}
\quad\Longrightarrow\quad
\exists i\ \forall\{x,y\}\subseteq S.
\]

No amount of pairwise graph analysis repairs that quantifier swap.

## 4. Minimum Pauli counterexample

Use the four one-qubit Pauli channels

\[
X=\{\mathcal I,\mathcal X,\mathcal Z,\mathcal Y\}
\]

under the one-use, no-reference budget from `HC-DU-065`. An interface may
choose any input qubit state and output measurement, but it receives only
one use of the unknown channel and no ancillary reference.

### Lemma 1 — every pair is distinguishable

Every two distinct Pauli channels are perfectly distinguishable by some
one-use unassisted interface.

### Proof

For distinct Pauli unitaries \(U,V\), the relative unitary
\(P=U^\dagger V\), up to phase, is a nonidentity Pauli. Choose a pure qubit
state \(\lvert\psi\rangle\) whose Bloch vector is perpendicular to the axis
of \(P\). Then

\[
\langle\psi|P|\psi\rangle=0,
\]

so \(U\lvert\psi\rangle\) and \(V\lvert\psi\rangle\) are orthogonal and one
binary measurement distinguishes them exactly. The required input generally
depends on the pair. \(\square\)

### Lemma 2 — no triple is jointly distinguishable

No one-use unassisted interface perfectly distinguishes any three distinct
Pauli channels.

### Proof

For one chosen input density operator, all conditional outputs are nonzero
states in a two-dimensional Hilbert space. Three perfect labels require
three pairwise orthogonal nonzero output supports. At most two such supports
fit in dimension two. \(\square\)

### Corollary 1 — the first flag defect is a triangle

The aggregate graph is

\[
G_b=K_4,
\]

but

\[
\mathcal J_b
=
\{S\subseteq X:|S|\le2\}.
\]

Thus \(\operatorname{Cl}(G_b)\) is the full tetrahedron while
\(\mathcal J_b\) is only its vertices and edges. The smallest false joint
inference has size three.

This is smaller and sharper than the earlier four-label top obstruction:
the graph already lies at its maximum while physical joint formation fails
at the first higher-order face.

## 5. Same graph, different physical architecture

Use the ideal three-qubit repetition-code control from `HC-DU-066` with

\[
X=\{I,X_1,X_2,X_3\}.
\]

A supplied complete QND syndrome interface resolves the four orthogonal
syndrome sectors and writes their label to a four-state archive. One fixed
interface therefore witnesses every subset:

\[
\mathcal J_b^{\mathrm{QEC}}=2^X,
\qquad
G_b^{\mathrm{QEC}}=K_4.
\]

Consequently,

\[
G_b^{\mathrm{Pauli}}
\cong
G_b^{\mathrm{QEC}}
\cong K_4,
\]

while

\[
\mathcal J_b^{\mathrm{Pauli}}
\not\cong
\mathcal J_b^{\mathrm{QEC}}.
\]

### Theorem 2 — graph nonidentification

No function of the aggregate pairwise action-confusability graph alone can
identify:

1. whether a common complete record interface exists;
2. the first order at which joint formation fails; or
3. the native resource receipt that forms the complete record.

### Proof

The Pauli and QEC specimens have isomorphic aggregate graphs. In the first,
no triple is jointly formable; in the second, all four labels are jointly
formable. The Pauli complete record requires either repeated process use or
an entangled reference and Bell measurement, while the QEC record uses
encoded-carrier redundancy and syndrome extraction. Any graph-only function
returns the same value on both and therefore cannot identify those
properties. \(\square\)

## 6. Exact task-relative criterion

Let \(t:X\to T\) be a frozen action or response target and define its required
separation edges

\[
E_t
=
\big\{\{x,y\}:t(x)\ne t(y)\big\}.
\]

### Theorem 3 — one-interface action sufficiency

A fixed interface \(i\) supports exact record-only action \(t\) if and only
if

\[
E_t\subseteq E(G_i).
\]

### Proof

Necessity follows because different required actions must be perfectly
distinguishable. For sufficiency, pairwise orthogonality across distinct
target classes makes the sums of their output supports mutually orthogonal.
One measurement can therefore decode the target class without needing to
distinguish alternatives inside a class. \(\square\)

The aggregate condition

\[
E_t\subseteq E(G_b)
\]

is weaker. It says that every required pair has some test, not that one
formed record supports the action.

## 7. A scoped quantitative consequence

Under a separately declared repeatable-source and classical-pooling
contract, define the **pair-separation cover number**

\[
\kappa_b(t)
=
\min
\left\{
|C|:
C\subseteq\mathcal I_b,\quad
E_t\subseteq\bigcup_{i\in C}E(G_i)
\right\}.
\]

This counts separately selectable test settings needed to cover all
action-relevant pair distinctions. It does not say that their results occur
in one process or form one record. To use the cover operationally, the
contract must additionally supply repeated instances with the same process
identity, compatible pooling, occurrence provenance, and retained outputs.

For the full Pauli label:

\[
\kappa_b(t_{\mathrm{Pauli}})=2.
\]

The \(Z\)- and \(X\)-basis testers together separate every distinct
\((a,b)\in\mathbb F_2^2\), while Lemma 2 excludes a one-interface cover of
the complete target. For the full repetition-code syndrome:

\[
\kappa_b(t_{\mathrm{QEC}})=1
\]

because the one complete QND syndrome interface already supplies \(K_4\).

The same distinction appears classically: two split ports may have cover
number two while one co-located joint port has cover number one.

This coordinate is exact but contract-relative. It is not:

- a cost of information;
- a formation receipt by itself;
- recoverable from \(G_b\) alone;
- invariant under changing the admitted interface family;
- a substitute for the resource-Pareto profile; or
- a physical law connecting quantum and distributed systems.

Adaptive, entangled, sequential, or jointly controlled strategies enter as
new composite interfaces with explicitly charged resources. They are not
free edges added after the calculation.

## 8. First-defect profile

The higher-order loss can be summarized without pretending it is universal:

\[
\delta_b
=
\min
\left\{
|S|:
S\in\operatorname{Cl}(G_b)\setminus\mathcal J_b
\right\},
\]

with \(\delta_b=\infty\) when the difference is empty.

For the one-use unassisted Pauli arena,

\[
\delta_b=3.
\]

For the complete QEC syndrome arena,

\[
\delta_b=\infty.
\]

Unlike the aggregate graph, this profile distinguishes the two physical
formation architectures. But it is derived from the full
joint-realizability complex, so it confirms the need for the existing ARE
rather than replacing it.

## 9. Literature collision

The component mathematics is occupied.

- Acín proves finite-use distinguishability results for finite families of
  unitary operations and supplies the standard unitary-discrimination
  setting
  ([Acín](https://arxiv.org/abs/quant-ph/0102064)).
- Quantum zero-error theory represents confusability for a fixed channel by
  operator spaces or noncommutative graphs and derives capacity bounds from
  that richer fixed-process object
  ([Duan, Severini, and Winter](https://arxiv.org/abs/1002.2514)).
- Measurement-context and compatibility research already warns that
  pairwise or contextwise data need not constitute one global empirical
  object. That neighboring lesson does not itself prove the present physical
  interface theorem.
- `HC-DU-033E/038E`, `HC-DU-065`, and `HC-DU-066` already own the
  joint-realizability complex, Pauli resource frontier, and QEC transfer.

The scoped DU addition is therefore not a new graph formalism. It is the
exact same-pairwise-shadow/different-formation counterexample and its routing
consequence:

> An action-confusability analysis must retain witness-interface labels or
> the complete resource-indexed joint-realizability complex.

## 10. What changes for Dynamic Unity

### Earned

- Pairwise aggregation over interventions can create false joint records.
- The failure is exactly a quantifier swap, not quantum mystery.
- The minimum Pauli witness has complete pairwise graph \(K_4\) and no
  jointly realizable triangle.
- A complete QEC syndrome has the same \(K_4\) pairwise graph and a full
  tetrahedral joint-realizability complex.
- Aggregate graphs cannot identify complete-interface existence, first
  formation defect, or native resource receipt.
- A fixed-interface target is exactly supported when all cross-target pairs
  have orthogonal output supports under that same interface.
- \(\kappa_b(t)\) and \(\delta_b\) are honest contract-relative diagnostics,
  not universal laws.

### Absorbed

- perfect support discrimination;
- Pauli-channel discrimination;
- stabilizer-syndrome discrimination;
- zero-error and noncommutative-graph mathematics;
- simplicial compatibility structure; and
- ordinary minimum set cover.

### Not earned

- no new quantum-information theorem;
- no quantitative universal relation between information and physical cost;
- no dynamics selecting \(\mathcal I_b\), \(\mathcal J_b\), or one interface;
- no cross-arena identity of native mechanisms;
- no new physics, prediction, experiment, hardware, ontology, or paper
  promotion; and
- no reopening of `H-CCR-17`.

### Stop

Do not:

- infer one common interface from pairwise edge witnesses;
- replace the ARE by its one-skeleton;
- treat a cover across repeated trials as one formed occurrence;
- hide changed preparations or measurements inside an edge;
- scalarize the full Pareto receipt using \(\kappa\); or
- call a supplied QND or Bell interface dynamically selected.

### Reopener

The graph-only `IT-A` route is closed. Reopen the physical-selection branch
only for:

1. dynamics selecting the resource-indexed joint interface or ARE;
2. an observable response law depending on \(\delta_b\), \(\kappa_b\), or
   another higher-order formation feature after the interface family is
   independently fixed; or
3. a quantitative invariant that survives changes of representation and
   resource bookkeeping rather than merely restating orthogonal support.

## 11. Portfolio return

```text
HC-DU-067: complete
FIXED_INTERFACE_GRAPH: sufficient for its own support family
AGGREGATE_PAIRWISE_GRAPH: insufficient for joint formation
PAULI_PAIRWISE_SHADOW: K4
PAULI_JOINT_COMPLEX: vertices + edges only
QEC_PAIRWISE_SHADOW: K4
QEC_JOINT_COMPLEX: full tetrahedron
FIRST_FLAG_DEFECT: Pauli 3; QEC infinity
PAIR_SEPARATION_COVER: Pauli 2; QEC 1
NEW_UNIVERSAL_INVARIANT: no
ENDOGENOUS_INTERFACE_SELECTION: open
H-CCR-17: not reopened
LOCAL_MODEL: not warranted
EXTERNAL_HARDWARE: irrelevant
NEXT_SCIENTIFIC_ACTION: unselected
```
