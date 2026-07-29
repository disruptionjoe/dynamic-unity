# Source-action-native response record, intervention minimality, unbounded mediator fibre, and operational duality

**Date:** 2026-07-29
**Run:** `RUN-20260729-142639-source-action-response-record`
**Claim:** `HC-DU-126`
**Status:** **BANKED — SCOPED GRADE 4 EXACT FINITE RECIPROCAL SOURCE-RESPONSE RECONSTRUCTION / FIXED-INTERVENTION NECESSITY AND SUFFICIENCY / UNBOUNDED MEDIATOR-REPRESENTATION FIBRE / STANDARD DIRICHLET-TO-NEUMANN, SCHUR-COMPLEMENT, AND INVERSE-NETWORK MATHEMATICS / NO ONTOLOGY SELECTION, CONTINUUM OR QUANTUM TRANSFER, EMPIRICAL EXCESS, OR NEW PHYSICS**

## Plain-English result

The last swing showed that a loop record belonging to an explicit mediator
network does not automatically survive when the mediator is eliminated.
This swing asks the constructive follow-up:

> What is the strongest complete record that really does belong to the
> reduced source action itself?

In the finite quadratic network arena, the answer is exact: it is the full
boundary response operator. It says, for every allowed pattern imposed at the
source boundary, what current response comes back. It is unchanged by exact
elimination of internal variables, and it predicts every held-out source
query without refitting.

If there are \(b\) boundary terminals, grounding one leaves
\(n=b-1\) independent source coordinates. Exactly \(n\) fixed linearly
independent vector-response experiments are necessary and sufficient to
reconstruct the operator. If the interface returns only one scalar action
value per experiment, the minimum rises to \(n(n+1)/2\). The distinction is
not in the physical source law; it is in the supplied readout interface.

The complete source record does **not** reconstruct a unique mediator
network. One fixed three-terminal response is realized by:

- a star with cycle rank \(0\); and
- for every \(m\geq1\), a positive simple network with cycle rank \(m\).

The number of internal vertices and edges is unbounded on the same exact
source-response fibre. An explicit-field presentation and a direct-relation
presentation are therefore operationally dual for the frozen source-query
class while remaining different presentations with different
mediator-facing possibilities.

That is the earned result. It is neither a proof that direct action is
fundamental nor a proof that internal fields are unreal.

## Why this matters to Dynamic Unity

`HC-DU-125` established a real descent failure:

\[
\text{mediator-cycle record}
\not\Rightarrow
\text{source-action record}.
\]

That negative left two possibilities:

1. direct action has no record object rich enough for reconstruction; or
2. the correct record is an invariant of source behavior rather than
   mediator topology.

The finite quadratic control selects the second answer within its scope.
The response operator is a source-native operational object, admits an exact
finite formation contract, and reconstructs the complete declared source
capability.

It also sharpens the ontology boundary:

```text
complete source response
  = complete for all frozen source queries
  ≠ complete mediator history or topology
```

This is a concrete specimen of Dynamic Unity's central rule: record
sufficiency is relative to an independently fixed action and target class.
Changing from source-facing to mediator-facing action is not a harmless
change of wording. It reopens the completion fibre.

## Frozen arena

Let \(N=(V,E,c)\) be a finite connected simple graph with strictly positive
rational conductances \(c_e\). Let \(B\subseteq V\) be a labeled boundary
with \(b\geq2\) terminals and \(I=V\setminus B\) the interior. The graph
Laplacian is partitioned as

\[
L_N=
\begin{pmatrix}
L_{BB}&L_{BI}\\
L_{IB}&L_{II}
\end{pmatrix}.
\]

For a potential \(u\in\mathbb R^V\), the quadratic action is

\[
S_N(u)=\frac12u^\mathsf TL_Nu.
\]

Holding the boundary value \(x=u|_B\) fixed and imposing stationarity on the
interior gives

\[
u_I=-L_{II}^{-1}L_{IB}x.
\]

Substitution produces the boundary Dirichlet-to-Neumann operator

\[
\Lambda_N
=
L_{BB}-L_{BI}L_{II}^{-1}L_{IB},
\]

with

\[
S_{\mathrm{eff}}(x)=\frac12x^\mathsf T\Lambda_Nx,
\qquad
j_B(x)=\Lambda_Nx.
\]

\(\Lambda_N\) is symmetric and positive semidefinite, its rows sum to zero,
and constants span its kernel. Grounding the final boundary terminal gives a
symmetric positive-definite matrix

\[
A_N\in\operatorname{Sym}_{n},
\qquad n=b-1.
\]

The graph, conductances, boundary labels, grounding convention, allowed
potential interventions, readout, trial association, and observer access
are supplied. This is a reciprocal classical control, not direct-action
electrodynamics, AQFT, gravity, or a quantum effective action.

## Theorem 1 — exact response descent

Exact stationary elimination of any subset of interior variables preserves
the final boundary response operator.

### Proof

Eliminating all interior variables in one step gives the Schur complement
\(L_N/L_{II}\). Eliminating them in stages gives an iterated Schur
complement. The quotient identity for Schur complements makes the two
results equal whenever the eliminated blocks are invertible. Positivity and
connectedness give that invertibility for every grounded interior block.
Therefore every exact sequence of Kron reductions returns the same
\(\Lambda_N\), boundary action, and boundary current map. \(\square\)

This is standard network mathematics. Dörfler and Bullo explicitly formulate
Kron reduction as the Schur complement of the network Laplacian
([2011](https://arxiv.org/abs/1102.2950)). Curtis, Ingerman, and Morrow call
the boundary voltage-to-current map the network response and use the same
Schur-complement machinery
([1998](https://sites.math.washington.edu/~curtis/cim.pdf)).

## Theorem 2 — the minimal complete source record

Fix the complete linear source capability

\[
\mathcal Q_{\mathrm{source}}
=
\{x\mapsto A_Nx:x\in\mathbb R^n\}.
\]

Then \(A_N\) is a complete record for \(\mathcal Q_{\mathrm{source}}\), and
it is minimal up to information-equivalent encoding.

### Proof

Given \(A_N\), every source response is calculated as \(A_Nx\).
Conversely, suppose two completions \(N_1,N_2\) are equivalent under a
candidate record and that every source query factors through that record.
Then

\[
A_{N_1}x=A_{N_2}x
\quad
\text{for every }x.
\]

Equality of two linear maps on every input implies
\(A_{N_1}=A_{N_2}\). Any complete record equivalence must therefore refine
equality of \(A_N\), while \(A_N\) itself is sufficient. \(\square\)

“Minimal” here means minimal equivalence relation for this capability. It
does not claim a minimum bit encoding, a selected archive, or a unique
physical representation.

## Theorem 3 — vector-response intervention count

Choose before observing the system a matrix of \(q\) boundary probes

\[
X=(x_1,\ldots,x_q)\in\mathbb R^{n\times q}
\]

and retain the joined output

\[
Y=(A_Nx_1,\ldots,A_Nx_q)=A_NX.
\]

Then \(n=b-1\) linearly independent probes are necessary and sufficient to
identify \(A_N\) over the frozen class.

### Sufficiency and no-refit transfer

If \(q=n\) and \(X\) is invertible,

\[
A_N=YX^{-1}.
\]

Every later source query is predicted, with no new fit, by

\[
j(x)=YX^{-1}x.
\]

### Necessity

If \(\operatorname{rank}X<n\), choose nonzero
\(v\perp\operatorname{im}X\) and set

\[
\Delta=vv^\mathsf T.
\]

Then \(\Delta X=0\).

The grounded response matrices of strictly positive complete boundary
networks form the open cone

\[
\mathcal R_n^\circ
=
\left\{
A\in\operatorname{Sym}_n:
A_{ij}<0\ (i\neq j),\
\sum_jA_{ij}>0
\right\}.
\]

Choose \(A_0\) in its interior. For sufficiently small
\(\varepsilon>0\),

\[
A_\pm=A_0\pm\varepsilon\Delta
\]

both remain in \(\mathcal R_n^\circ\). They are therefore realized by
strictly positive boundary-only networks. Yet

\[
A_+X=A_-X
\]

while

\[
(A_+-A_-)v
=
2\varepsilon\|v\|^2v
\neq0.
\]

Every rank-deficient probe family consequently leaves a physical
same-record/different-source-response witness. \(\square\)

### Robustness

If the measured output is \(Y+E\), then

\[
\widehat A-A=EX^{-1}
\]

and hence

\[
\|\widehat A-A\|
\leq
\|E\|\,\|X^{-1}\|.
\]

Under a fixed maximum-singular-value normalization, an orthogonal probe
design minimizes the worst inverse amplification. This is a conditioning
result after identifiability has been established, not a new information
law.

## Theorem 4 — scalar-action interface count

Suppose the interface returns only

\[
W_A(x)=\frac12x^\mathsf TAx
\]

rather than the current vector \(Ax\).

Because

\[
\dim\operatorname{Sym}_n=\frac{n(n+1)}2,
\]

exactly

\[
d=\frac{n(n+1)}2
\]

fixed scalar queries are necessary and sufficient over the open physical
response class.

### Sufficiency

Query \(e_i\) and \(e_i+e_j\) for all \(i<j\). Then

\[
A_{ii}=2W_A(e_i)
\]

and

\[
A_{ij}
=
W_A(e_i+e_j)-W_A(e_i)-W_A(e_j).
\]

These \(d\) values reconstruct every entry of \(A\).

### Necessity

Each scalar query is one linear functional on
\(\operatorname{Sym}_n\). Fewer than \(d\) such functionals have a nonzero
common kernel direction \(\Delta\). For any interior point \(A_0\) of
\(\mathcal R_n^\circ\), sufficiently small
\(A_0\pm\varepsilon\Delta\) remain positive-network responses, agree on all
selected scalar actions, and differ on some held-out action. \(\square\)

Thus one source law can have two different minimum formation costs because
the readout interface is different:

| Frozen output per intervention | Necessary and sufficient fixed probes |
|---|---:|
| full current vector \(Ax\) | \(n=b-1\) |
| scalar action \(x^\mathsf TAx/2\) | \(n(n+1)/2\) |

The action does not select either interface.

## Theorem 5 — one source record has every finite mediator cycle rank

Fix the three-terminal response

\[
\Lambda_\triangle
=
\begin{pmatrix}
2&-1&-1\\
-1&2&-1\\
-1&-1&2
\end{pmatrix},
\]

the response of the unit-conductance boundary triangle.

### Rank zero

A three-arm star with one interior vertex and conductance \(3\) on every
arm has Schur complement \(\Lambda_\triangle\). Its cycle rank is \(0\).

### Every positive rank

For each integer \(m\geq1\):

1. retain unit boundary edges \(0\!-\!2\) and \(1\!-\!2\);
2. replace the edge \(0\!-\!1\) by \(m\) internally disjoint two-edge
   paths; and
3. put conductance \(2/m\) on every path edge.

Each path has series conductance \(1/m\), so the parallel family has total
conductance \(1\). The source response is therefore exactly
\(\Lambda_\triangle\).

The network is connected, simple, and positive, with

\[
|V|=m+3,\qquad
|E|=2m+2,\qquad
\beta_1=|E|-|V|+1=m.
\]

Together with the star, one source-response fibre realizes

\[
\beta_1\in\{0,1,2,\ldots\}.
\]

Internal vertex count, edge count, topology, local potential profile, and
energy-flow partition do not factor through the complete source response.
\(\square\)

This does not contradict inverse-network uniqueness results. Those results
require a fixed recoverable or critical graph class. Curtis, Ingerman, and
Morrow prove recovery of conductances for a fixed critical circular-planar
network and show that the critical graph itself is unique only up to
star--triangle equivalence; noncritical networks reduce to response-equivalent
critical ones. The unbounded family here deliberately does not freeze one
critical graph class.

## Corollary — scoped field/direct-action operational duality

Let \(\pi\) send an explicit mediator network to its complete boundary
response. Then the source-action record is simply

\[
R_{\mathrm{source}}(N)=\pi(N)=A_N.
\]

It is constant on every mediator-elimination fibre by construction.

Therefore an explicit mediator presentation and a direct boundary-relation
presentation with the same \(A_N\) are operationally equivalent for all
queries in \(\mathcal Q_{\mathrm{source}}\).

They need not be equivalent for:

- interventions on internal nodes or edges;
- local mediator records;
- local energy or stress partitions;
- topology-changing operations;
- determinant, measure, state, regulator, or background-sensitive quantum
  targets; or
- any action not already represented by the frozen source operator.

The right conclusion is **source-query operational duality**, not ontology
equivalence.

## Dynamic Unity typing

The result separates five objects that should not be collapsed:

| Object | Earned status |
|---|---|
| source response law \(A\) | exact reduced-action invariant |
| associated probe/output transcript \((X,Y)\) | formed operational record under a supplied interface |
| complete source capability | exactly reconstructed when \(X\) has full rank |
| mediator topology | unbounded representation fibre under source-only access |
| mediator-local target | physical remainder only after a mediator-facing action is independently admitted |

The law and the record are not identical. \(A\) is the object to be learned;
\((X,Y)\) becomes its operational record only because the probe, readout,
association, retention, and access contract has been supplied.

The topology fibre is physically meaningful as a family of possible
presentations. It is not yet a Grade-5 observer-accessible remainder for a
source-only observer, because no source query distinguishes its members.

## Strongest absorbers and novelty assessment

The component mathematics is mature:

- Dirichlet-to-Neumann response maps in inverse resistor networks;
- Schur complements and Kron reduction;
- star--triangle transformations;
- linear-system identification and experimental design; and
- nonuniqueness outside a frozen recoverable graph class.

Relevant primary sources include:

- Dörfler and Bullo,
  [*Kron Reduction of Graphs with Applications to Electrical Networks*](https://arxiv.org/abs/1102.2950);
- Curtis, Ingerman, and Morrow,
  [*Circular Planar Graphs and Resistor Networks*](https://sites.math.washington.edu/~curtis/cim.pdf); and
- Paal and Umbleja,
  [*Note on Star-Triangle Equivalence in Conducting Networks*](https://arxiv.org/abs/1504.01269).

The Dynamic Unity increment is the typed composition:

1. a source-action-native record invariant under mediator elimination;
2. a necessary-and-sufficient fixed formation contract;
3. no-refit transfer to every held-out source query;
4. an explicit unbounded mediator completion fibre; and
5. a precise action-enlargement rule for when that fibre becomes
   observer-accessible.

This is a useful exact control and a transferable theorem shape. It is not
new inverse-network mathematics, empirical excess, or a candidate physical
law by itself.

## What it changes

The direct-action branch no longer lacks a constructive record candidate in
the finite quadratic arena. The response operator is the maximal source-native
record for the declared capability.

The next high-ceiling question is not “can direct action have records?” It is:

> Does a physically serious direct-action or field theory select a finite,
> formable source-response interface whose unchanged record reconstructs a
> held-out physical target beyond the law used to define it?

Any continuation must add at least one substantive increment:

1. a nonlinear or quantum source action with an independently selected
   realizable probe algebra;
2. a background-natural response including determinant, measure, state,
   boundary, regulator, gauge, and counterterm data;
3. a finite physically formed source archive rather than a stipulated exact
   response surface;
4. an unchanged transfer to time, geometry, field, capability, or regional
   finality; or
5. one mediator-facing operation that is physically available under one
   architecture and absent under the other.

More resistor-network variants without one of these increments are stopped.

## Exact regression

Run:

```bash
python3 tests/du_source_action_response_record_probe.py
```

The deterministic artifact is
`tests/artifacts/du_source_action_response_record_result.json`.

It reports `21/21` checks over:

- six exact response/reconstruction specimens;
- sequential versus one-shot Schur elimination;
- full-rank and rank-deficient vector probe families;
- a physical same-record/different-held-out-response pair;
- complete and incomplete scalar-action designs;
- orthogonal versus weak-direction conditioning; and
- nine source-equivalent topology specimens with cycle ranks \(0\) through
  \(8\), plus the analytic construction for every \(m\geq0\).

The computation is a regression for the analytic proof. It supplies no
continuum, quantum, empirical, or ontological evidence.

## Verdict

```text
BOUNDARY_RESPONSE_OPERATOR_DESCENDS_THROUGH_EXACT_MEDIATOR_ELIMINATION
RESPONSE_OPERATOR_IS_MINIMAL_COMPLETE_RECORD_FOR_LINEAR_SOURCE_CAPABILITY
B_MINUS_ONE_INDEPENDENT_VECTOR_PROBES_ARE_NECESSARY
B_MINUS_ONE_INDEPENDENT_VECTOR_PROBES_ARE_SUFFICIENT
FIXED_PROBE_RECORD_TRANSFERS_TO_EVERY_HELD_OUT_BOUNDARY_QUERY
ORTHOGONAL_VECTOR_PROBES_MINIMIZE_INVERSE_AMPLIFICATION
SCALAR_ACTION_INTERFACE_NEEDS_N_TIMES_N_PLUS_ONE_OVER_TWO_QUERIES
ONE_SOURCE_RESPONSE_HAS_MEDIATOR_COMPLETIONS_OF_EVERY_CYCLE_RANK
INTERNAL_TOPOLOGY_DOES_NOT_FACTOR_THROUGH_SOURCE_ACTION
FIELD_AND_DIRECT_RELATION_PRESENTATIONS_ARE_OPERATIONALLY_DUAL_FOR_SOURCE_QUERIES
MEDIATOR_FACING_ACTION_REOPENS_THE_EQUIVALENCE_CLASS
RESPONSE_LAW_DOES_NOT_SELECT_PROBE_ARCHIVE_OBSERVER_OR_ACCESS
NO_DIRECT_ACTION_OR_FIELD_ONTOLOGY_SELECTION
NO_CONTINUUM_QUANTUM_OR_EMPIRICAL_EXCESS
NO_READY_SUCCESSOR
```
