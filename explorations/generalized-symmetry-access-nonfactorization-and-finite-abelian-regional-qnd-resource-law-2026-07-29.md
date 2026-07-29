---
title: "Generalized-symmetry access nonfactorization and the finite-Abelian regional-QND resource law"
status: completed_scoped_result
doc_type: access_nonfactorization_theorem_and_exact_resource_law
created: 2026-07-29
hypothesis_id: HC-DU-120
run_id: RUN-20260729-113556-generalized-symmetry-access-resource-classification
authority: "Joe direct chat: Go"
lanes:
  - lane_1
  - lane_3
  - lane_4
  - lane_5
  - lane_7
channels:
  - CH-FORMAL
  - CH-COLLIDE
  - CH-MODEL
  - CH-SYN
maximum_grade: "Scoped Grade 4 exact finite-Abelian resource necessity/sufficiency theorem and symmetry-versus-access nonfactorization result; no universal QFT measurement theorem, selected physical apparatus, empirical excess, ontology priority, new physics, or prediction"
frozen_read_revisions:
  dynamic_unity_parent: b2aa3bacd74d
probe: "../tests/du_generalized_symmetry_access_resource_probe.py"
artifact: "../tests/artifacts/du_generalized_symmetry_access_resource_result.json"
---

# Generalized symmetry does not by itself classify access

## Executive result

The swing returned:

```text
GENERALIZED_SYMMETRY_CLASSIFIES_ALGEBRAIC_SECTORS_NOT_ACCESS
+ ACCESS_DOES_NOT_FACTOR_THROUGH_SYMMETRY_DATA_ALONE
+ FINITE_ABELIAN_QND_CHARGE_MEASUREMENT_HAS_EXACT_CUTWISE_RESOURCE_COST
+ LOG_GROUP_ORDER_EBITS_PER_NONTRIVIAL_CUT_ARE_NECESSARY
+ GROUP_GHZ_RESOURCE_ACHIEVES_THE_BOUND
+ PROPER_LOCAL_SHARES_ARE_BLIND_AND_JOINTLY_COMPLETE
+ SPACELIKE_RESOURCE_AND_TIMELIKE_QUANTUM_ROUTE_ARE_DIFFERENT_CONTRACTS
+ NO_UNIVERSAL_GENERALIZED_SYMMETRY_ACCESS_CLASSIFICATION
+ NO_SELECTED_PHYSICAL_FORMATION_MECHANISM
+ NO_READY_SUCCESSOR
```

The strongest correction is a factorization boundary:

> Generalized-symmetry data can classify an extended charge, its fusion, its
> dual, and its linking algebra. They do not determine whether a declared
> observer can measure that charge, whether the measurement can be
> nondemolition, or what physical resource makes it possible.

The access profile factors through a larger packet:

\[
\operatorname{Access}
=
F(
  \text{net/representation},
  \text{region and target},
  \text{instrument},
  \text{causal route},
  \text{matter/probe},
  \text{resource},
  \text{acquisition/access}
).
\tag{1}
\]

It does not factor through the generalized-symmetry label alone.

The swing also earns a positive exact result. For a finite Abelian group
\(G\), an exact spacelike regional Lüders measurement of total \(G\)-charge
using local operations, later classical aggregation, and a pre-distributed
quantum resource has optimal cutwise entanglement cost

\[
E_{\min}(A:B)=\log_2|G|
\tag{2}
\]

for every nontrivial partition of the participating region. Necessity follows
because the measurement can create exactly \(\log_2|G|\) entanglement from a
product input on every outcome and every cut. A character-\(G\)-GHZ resource
attains the bound and produces proper-local shares that are individually
blind and jointly complete.

This is the invariant resource law missing from `HC-DU-119` for the
finite-Abelian charge family. Its ingredients are absorbed by standard
entanglement monotonicity, nonlocal-measurement cost, GHZ measurement, and
higher-form symmetry classification. Dynamic Unity's contribution is the
typed conjunction and exact regional-record consequence, not new
entanglement or QFT mathematics.

## 1. What the modern symmetry results actually classify

### 1.1 The \(D>2\), finite-index higher-form result

[Casini and
Magán](https://arxiv.org/abs/2511.21810) prove a higher-form analogue of DHR
reconstruction under a substantial frozen contract. In particular, the
theory is \(\pi_0\)-complete, the relevant additive-to-maximal inclusions are
finite-index subfactors, sectors are transportable, and the AQFT assumptions
needed by the reconstruction are in force.

In that scope:

- sectors for a \(k\)-dimensional loop have finite Abelian group
  \(G^\ast\) fusion rules;
- sectors for the dual loop carry the Pontryagin-dual group \(G\);
- generalized knot sectors are already classified by unknot sectors; and
- the commutator of linked nonlocal operators is fixed by the character
  pairing raised to the linking number.

Schematically,

\[
W_g(K_1)T_\chi(K_2)
=
\chi(g)^{\,\ell(K_1,K_2)}
T_\chi(K_2)W_g(K_1).
\tag{3}
\]

This materially narrows the proposed generalized-symmetry access project.
For this important \(D>2\) finite-index class, the algebraic loop sector is
not an unconstrained non-invertible fusion category. It is group-like and
Abelian after the declared completion step.

It does **not** follow that every such operator is measurable. The theorem
classifies Haag-duality-violating sectors and their operator algebra. It does
not construct a localizable probe, a measurement instrument, a retained
output, or an observer acquisition route.

The continuous/infinite-index cases, non-\(\pi_0\)-complete theories, lower
dimensions, boundaries, and other non-invertible settings remain outside
this finite theorem.

### 1.2 Non-invertible symmetry and algebra assignment

[Shao, Sorce, and
Srivastava](https://arxiv.org/abs/2503.20863) study symmetric sectors of
1+1-dimensional CFTs and lattice systems. Their examples distinguish:

- additivity failure associated with invertible elements; and
- Haag-duality failure associated with non-invertible elements.

The paper explicitly keeps the assignment of algebras to regions as a
choice; there is no canonical assignment in its general setup. It also does
not formulate a measurement theory.

This is a second reason not to derive access from a bare symmetry category.
Even before choosing a physical instrument, one must specify which
region-algebra assignment is under discussion.

### 1.3 SymTFT still needs the physical theory

[Bhardwaj and
Schäfer-Nameki](https://arxiv.org/abs/2305.17159) characterize generalized
charges through topological defects of the symmetry TFT. The SymTFT encodes
both the generalized symmetry and the physical theory through its boundary
conditions.

This blocks another overreach:

> The symmetry category by itself is not the complete physical input even for
> the algebraic charge classification.

Boundary condition, representation, matter, and operational realization
cannot be erased by calling the symmetry data universal.

## 2. The access nonfactorization theorem

Let \(S\) denote the algebraic data of one generalized-symmetry target and
let \(O\) denote the operational envelope: admitted instruments, resources,
causal route, matter/probe content, and access semantics.

### Proposition 1 — symmetry-only access classification fails

There is no function

\[
f:S\longrightarrow
\{\text{QND measurable},\text{not QND measurable}\}
\tag{4}
\]

that correctly classifies the finite-Abelian total-charge target across all
admitted operational envelopes.

### Proof

Fix a nontrivial finite Abelian group \(G\), the same \(n\)-party system, and
the same total-charge projectors \(\{P_q\}_{q\in G}\).

Compare two envelopes:

1. local operations and classical communication with no pre-shared
   entanglement and no quantum communication during formation;
2. the same operations plus the character-\(G\)-GHZ resource constructed in
   Section 4.

Section 3 proves that envelope 1 cannot implement the exact selective Lüders
instrument because that instrument creates \(\log_2|G|>0\) entanglement from
a product state across every cut. Section 4 constructs the exact instrument
in envelope 2.

The algebraic symmetry data and target are unchanged, while the access value
changes. Therefore access does not factor through \(S\). \(\square\)

This proposition does not refute a classification that freezes the complete
operational packet. It proves why that packet is necessary.

## 3. Exact finite-Abelian lower bound

Let each of \(n\ge2\) parties possess a register with orthonormal basis
\(\{|g\rangle:g\in G\}\). Define total charge

\[
Q(g_1,\ldots,g_n)=\sum_{i=1}^n g_i
\tag{5}
\]

and let \(P_q\) project onto the sector \(Q=q\).

Freeze the desired instrument to the selective Lüders instrument

\[
\mathcal I_q(\rho)=P_q\rho P_q.
\tag{6}
\]

This is stronger than merely returning the right classical label. It retains
all coherence inside a charge sector and removes coherence between sectors.

Take the product input

\[
|\Omega\rangle
=
|+\rangle_G^{\otimes n}
=
|G|^{-n/2}
\sum_{g_1,\ldots,g_n\in G}
|g_1,\ldots,g_n\rangle.
\tag{7}
\]

Every charge occurs with probability \(1/|G|\). Conditional on outcome \(q\),
the normalized output is

\[
|\psi_q\rangle
=
|G|^{-(n-1)/2}
\sum_{\sum_i g_i=q}
|g_1,\ldots,g_n\rangle.
\tag{8}
\]

Choose any nontrivial partition of the parties into \(A\) and \(B\). Define
the normalized fixed-sum states

\[
|r\rangle_A
=
|G|^{-(|A|-1)/2}
\sum_{\sum_{i\in A}g_i=r}
|g_A\rangle,
\tag{9}
\]

and similarly on \(B\). States with different sums are orthogonal. Equation
(8) has Schmidt decomposition

\[
|\psi_q\rangle
=
|G|^{-1/2}
\sum_{r\in G}
|r\rangle_A\,|q-r\rangle_B.
\tag{10}
\]

There are \(|G|\) equal Schmidt probabilities \(1/|G|\), so

\[
E_{A:B}(|\psi_q\rangle)=\log_2|G|
\tag{11}
\]

for every \(q\) and every nontrivial cut.

### Theorem 1 — cutwise resource necessity

Suppose the exact instrument (6) is implemented by local operations and
classical communication using a pre-shared resource \(\eta\), with no quantum
system crossing the cut during formation. Then, for every nontrivial
partition \(A:B\),

\[
E_F^{A:B}(\eta)\ge\log_2|G|,
\tag{12}
\]

where \(E_F\) is entanglement of formation. For a pure resource, this is the
ordinary entanglement entropy.

### Proof

The data input (7) is separable across every party cut. The complete initial
entanglement across \(A:B\) is therefore the resource entanglement.

An exact implementation produces the pure data state (8) conditional on
each outcome. Discarding any leftover apparatus cannot increase
entanglement, so each complete output branch carries at least the data
entanglement (11). The outcomes are uniform, but every branch has the same
value \(\log_2|G|\), so the average output entanglement is at least
\(\log_2|G|\).

Average entanglement cannot increase under LOCC. Hence the initial resource
must satisfy (12). \(\square\)

The proof is the entanglement-production method used in the established
literature on the cost of nonlocal measurements, especially
[Bandyopadhyay, Brassard, Kimmel, and
Wootters](https://arxiv.org/abs/0809.2264). The finite-Abelian regional
application is the present composition, not a claim to a new general
entanglement monotone.

## 4. Matching \(G\)-GHZ construction

Let \(\widehat G\) be the character group. Pre-distribute

\[
|\mathrm{GHZ}_{\widehat G}\rangle
=
|G|^{-1/2}
\sum_{\chi\in\widehat G}
|\chi\rangle^{\otimes n}.
\tag{13}
\]

Each party applies the local controlled character

\[
|g_i\rangle|\chi\rangle
\longmapsto
\chi(g_i)|g_i\rangle|\chi\rangle.
\tag{14}
\]

The resource becomes

\[
|G|^{-1/2}
\sum_{\chi\in\widehat G}
\chi(Q)|\chi\rangle^{\otimes n}.
\tag{15}
\]

Each party measures its resource share in the Fourier-dual basis. Let the
local outcomes be \(s_1,\ldots,s_n\in G\). Character orthogonality gives

\[
\Pr(s_1,\ldots,s_n\mid q)
=
\begin{cases}
|G|^{-(n-1)},&
\sum_i s_i=q,\\
0,&
\text{otherwise}.
\end{cases}
\tag{16}
\]

For every complete share string \(s\), the data Kraus operator is
proportional to \(P_{\sum_i s_i}\). Therefore the nonselective channel is
exactly

\[
\mathcal L_Q(\rho)
=
\sum_{q\in G}P_q\rho P_q.
\tag{17}
\]

It preserves within-sector coherence and erases only cross-sector coherence.

### Proposition 2 — exact regional threshold record

Under (16):

1. the complete share set reconstructs \(q\) exactly;
2. every proper share subset is uniform and independent of \(q\);
3. the complete share law depends only on \(q\), not on the finer data
   configuration; and
4. the instrument is the exact charge Lüders instrument.

The character-GHZ resource has \(|G|\) equal Schmidt coefficients across
every nontrivial party cut, hence exactly \(\log_2|G|\) entanglement.

### Corollary — exact optimal cost

Minimizing over allowed pre-distributed resource states,

\[
\min_\eta E_F^{A:B}(\eta)=\log_2|G|
\tag{18}
\]

for every nontrivial cut, and one resource attains all cutwise minima
simultaneously.

This is a cost optimum. It does not say every resource with that much
entanglement realizes the instrument.

## 5. Why the timelike route is not a counterexample

A coherent \(|G|\)-level carrier can visit the parties sequentially, acquire
the total character phase, and be read after the route completes. It may
start without pre-shared entanglement.

That route permits a quantum system to cross each relevant cut. It is not an
LOCC implementation of the spacelike formation event and is outside the
premise of Theorem 1.

The two valid implementations expose a real resource alternative:

```text
spacelike regional formation
  -> pre-distributed log2(|G|) entanglement across every cut
  -> local writes
  -> later classical aggregation

timelike sequential formation
  -> coherent quantum carrier crosses cuts
  -> route latency and transmission risk
  -> one later readout
```

The ideal target channel can agree while provenance, causal route, resource,
and failure surface differ. An eventual cross-route resource law must type
those currencies separately before comparing them.

## 6. Exact executable controls

The deterministic probe checks:

- \(\mathbb Z_2,\mathbb Z_3,\mathbb Z_4\), and
  \(\mathbb Z_2\times\mathbb Z_2\);
- three-party specimens and one four-party specimen;
- every proper share subset;
- every computational matrix unit for the induced channel;
- every target charge and every nontrivial party cut; and
- equality of the exact lower-bound Schmidt vector and the resource Schmidt
  vector.

It passes `12/12` controls over five specimens. The receipt preserves rational
Schmidt probabilities; no floating-point eigensolver is used.

The script validates the finite group and channel algebra. It does not prove
LOCC monotonicity, model a generalized-symmetry QFT, or construct a
relativistic detector.

## 7. The two-stage classification that survives

The evidence supports a typed classification architecture rather than one
universal lookup table.

### Stage A — algebraic sector

In the finite-index \(D>2\) scope:

\[
\mathsf A
=
(G,G^\ast,\chi,\ell,\mathcal A_{\rm add}\subseteq\mathcal A_{\rm max}).
\tag{19}
\]

This identifies charge labels, fusion, duality, and linked commutation.

### Stage B — operational envelope

\[
\mathsf O
=
(
\text{instrument semantics},
\text{local net and representation},
\text{matter/probe},
\text{topology},
\text{causal route},
\text{resource},
\text{acquisition/access}
).
\tag{20}
\]

Only the pair \((\mathsf A,\mathsf O)\) determines whether the target is:

- locally measurable;
- regionally QND-measurable;
- destructively measurable only;
- changeable but unmeasurable;
- measurable but locally unchangeable; or
- forbidden by causality.

For the finite-Abelian Lüders/LOCC slice, Theorem 1 and Proposition 2 fill one
cell exactly. The other cells remain controlled by the Wilson-loop cases and
future physical constructions.

## 8. Relation to the North Star

The result strengthens Dynamic Unity's layered-regional picture without
promoting it to ontology.

A charge distinction can be:

1. physically present in the admitted algebraic theory;
2. written into a distributed carrier on one spacelike slice;
3. absent from every proper-local share;
4. reconstructible from the joined regional record;
5. inaccessible to every participant until causal aggregation; and
6. action-enabling only after the access contract permits the aggregate.

The minimum entanglement bound says this architecture is not free. The
regional record's size is not merely its classical target entropy. The
spacelike nondemolition formation mechanism must carry enough nonlocal
quantum resource to support the entanglement that the sharp projection can
create.

That is a concrete connection between:

- algebraic generalized-symmetry structure;
- quantum resource theory;
- physical record formation; and
- layered observer access.

It does not show that generalized symmetries are consensus systems, that the
resource is a prior record of the target, or that records constitute physical
reality.

## 9. Absorbers, grade, and novelty

### Absorbed ingredients

- finite higher-form sector classification and linking algebra:
  Casini--Magán;
- generalized/non-invertible charge classification: SymTFT;
- noncanonical region-algebra assignment in scoped non-invertible examples:
  Shao--Sorce--Srivastava;
- entanglement monotonicity and entanglement-production measurement bounds:
  standard LOCC resource theory and Bandyopadhyay et al.;
- GHZ-assisted modular charge measurement: standard stabilizer/group-Fourier
  measurement architecture; and
- Wilson-loop access and causality cases:
  Beckman--Gottesman--Kitaev--Preskill.

### Earned

- scoped Grade-4 proof that access cannot factor through generalized-symmetry
  data alone;
- exact finite-Abelian cutwise resource lower bound;
- matching character-GHZ construction;
- exact \(|G|\)-ary all-shares regional record;
- one two-stage classification surface; and
- a precise premise boundary separating pre-distributed spacelike resources
  from sequential quantum communication.

### Not earned

- universal classification of non-invertible or continuous symmetries;
- a new DHR, SymTFT, entanglement-cost, or gauge-theory theorem;
- proof that every QFT total-charge instrument realizes the finite model;
- selection of one physical detector, resource, archive, or observer;
- a cross-route exchange rate between entanglement and quantum communication;
- held-out time, geometry, field, or capability reconstruction;
- empirical excess, new law, new physics, or ontology priority.

The literature search found no exact prior statement of the present
finite-Abelian regional-record conjunction, but that is not evidence of
novelty. The mathematical ingredients are mature, so the result remains an
honest synthesis until a dedicated priority search or expert review shows
otherwise.

## 10. Successor disposition

No new flagship is selected.

The generalized-symmetry access reopener is partially discharged:

- the relevant finite \(D>2\) algebraic sectors are much more classified than
  the prior DU framing suggested;
- symmetry data alone provably cannot classify access; and
- the regional QND resource cost is exact for finite Abelian total charge.

The highest-value next reopeners are now narrower.

### Reopener A — physical QFT transfer

Construct one explicit local-QFT or lattice-gauge measurement whose operator,
local factorization, character-GHZ resource, formed shares, and observer
acquisition map implement the unchanged \(G\)-charge instrument. Verify the
cutwise lower bound in that physical contract.

### Reopener B — cross-route tradeoff

Prove a resource inequality comparing pre-distributed entanglement with
quantum communication dimension, causal depth, station count, error, and
aggregation latency. The currencies must remain typed; a scalar analogy is
not enough.

### Reopener C — beyond finite Abelian sectors

Identify one continuous, infinite-index, boundary, or non-invertible target
for which the finite-Abelian proof fails, then derive the correct replacement
or the smallest obstruction.

### Reopener D — no-refit North-Star transfer

Use the same physically formed charge record and unchanged access contract to
reconstruct a held-out time, geometry, field, or capability target.

Until one fires, more parity, modular-sum, or GHZ-size variants repeat the
proved family.

## Bottom line

The generalized-symmetry program does not hand Dynamic Unity a universal
answer to “who can know or act on this physical distinction?” It hands over
the algebraic skeleton.

For the finite-Abelian slice, Dynamic Unity can now add one exact operational
law:

> Forming an exact spacelike nondemolition record of a regional total charge
> costs at least \(\log_2|G|\) entanglement across every cut of the region,
> and a character-GHZ carrier attains that cost while keeping every proper
> local share blind.

So the emerging picture is sharper:

```text
symmetry classifies the distinction
  != operation makes it measurable
  != resource makes that operation possible
  != distributed formation makes a regional record
  != aggregation makes the value accessible
  != access makes it action-enabling.
```

That is real progress toward a coherent layered account. It is still a
known-physics theorem boundary, not the North-Star reconstruction result.
