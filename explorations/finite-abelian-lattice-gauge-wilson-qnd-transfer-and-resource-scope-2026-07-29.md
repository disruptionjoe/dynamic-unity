---
title: "Finite-Abelian lattice-gauge Wilson-QND transfer and its resource scope"
status: completed_scoped_result
doc_type: physical_lattice_transfer_theorem_and_resource_boundary
created: 2026-07-29
hypothesis_id: HC-DU-121
run_id: RUN-20260729-125319-finite-abelian-gauge-qnd-transfer
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
maximum_grade: "Scoped Grade 4 exact finite-Abelian lattice-gauge transfer theorem; no continuum-QFT theorem, physically selected matter/probe/interface, complete physical cost law, empirical excess, ontology priority, new physics, or prediction"
frozen_read_revisions:
  dynamic_unity_parent: 910d0965841c
probe: "../tests/du_finite_abelian_gauge_qnd_transfer_probe.py"
artifact: "../tests/artifacts/du_finite_abelian_gauge_qnd_transfer_result.json"
---

# A finite-Abelian Wilson record inherits the exact regional resource law

## Executive result

The swing returned:

```text
GAUGE_INVARIANT_DRESSED_LINK_REDUCTION_IS_EXACT
+ PHYSICAL_ORBIT_BASIS_FACTORS_OVER_MATTER_COMPLETED_LINKS
+ WILSON_HOLONOMY_IS_THE_UNCHANGED_TOTAL_GROUP_TARGET
+ FINITE_ABELIAN_GAUGE_QND_INSTRUMENT_TRANSFERS_UNCHANGED
+ LOG_GROUP_ORDER_ANCILLA_ENTANGLEMENT_REMAINS_NECESSARY
+ CHARACTER_GHZ_RESOURCE_REMAINS_SUFFICIENT
+ MATTER_PROBE_AND_LOCAL_ACCESS_ARE_SUPPLIED_NOT_SELECTED
+ ANCILLA_ENTANGLEMENT_IS_NOT_COMPLETE_PHYSICAL_COST
+ PURE_GAUGE_AND_NONABELIAN_CASES_DO_NOT_INHERIT_THE_THEOREM
+ NO_NEW_QFT_OR_ENTANGLEMENT_THEOREM
+ NO READY SUCCESSOR
```

The first reopener from `HC-DU-120` is satisfied in a bounded physical arena.
The exact finite-Abelian regional-QND resource law is not confined to an
abstract tensor product. It transfers unchanged to a finite lattice gauge
theory containing regular-representation charged matter.

For a finite Abelian group \(G\), matter turns each link coordinate into an
independent local gauge-invariant dressed variable. Around a closed loop, the
sum of those dressed variables is exactly the Wilson holonomy. Therefore the
selective Wilson-holonomy Lüders instrument is the same total-\(G\) instrument
proved in `HC-DU-120`.

Under the same regional LOCC contract:

\[
E_{\min}^{A:B}=\log_2|G|
\tag{1}
\]

of pre-shared ancillary entanglement is necessary across every nontrivial
link-station cut, and a character-\(G\)-GHZ ancilla attains every cutwise
bound simultaneously.

This is an exact conditional physical theorem, not a complete physical cost
law. It assumes:

- regular-representation charged matter;
- one accessible dressed-link algebra per station;
- the selective nondemolition Wilson instrument;
- a pre-distributed gauge-invariant ancilla;
- later classical aggregation; and
- no quantum carrier between stations during formation.

The action does not select those conditions. Equation (1) prices only the
ancillary entanglement after they are supplied.

## 1. The primary-source hinge

[Beckman, Gottesman, Kitaev, and
Preskill](https://arxiv.org/abs/hep-th/0110205) distinguish sharply among
Wilson-loop targets.

For an Abelian lattice gauge theory with suitable charged matter, they:

1. replace gauge-dependent link and matter coordinates with local
   gauge-invariant dressed link variables;
2. express the Wilson loop as the product of those local variables;
3. distribute an entangled ancilla around the loop;
4. couple each local dressed variable to its local ancilla share; and
5. recover only the Wilson value after later aggregation, without resolving
   the individual link values.

That is a localizable nondemolition measurement. Their same analysis shows
that:

- measuring every dressed link separately is destructive because it obtains
  a finer record;
- pure Abelian gauge theory has a different observable algebra;
- homologically nontrivial pure-gauge Wilson loops may be locally
  inaccessible; and
- non-Abelian spacelike Wilson-loop nondemolition measurement is
  causality-forbidden under their assumptions.

The matter completion is therefore not cosmetic. It changes which local
gauge-invariant variables exist and which instrument can be implemented.

[Casini, Huerta, and
Rosabal](https://arxiv.org/abs/1312.1183) supply the strongest factorization
warning. Gauge constraints can obstruct a canonical tensor factorization of
the physical Hilbert space; regional gauge-invariant algebras can have
centers, and different boundary-algebra choices can yield different entropy
assignments. A cutwise entanglement law cannot simply call gauge links
independent.

The construction below meets that warning in its frozen matter-completed
arena by proving the orbit reduction explicitly. It does not erase the
warning for any other arena.

## 2. Exact gauge reduction

### 2.1 Kinematic coordinates

Let \(C_n\) be an oriented cycle. At each vertex \(v\), put a
regular-representation matter coordinate

\[
\phi_v\in G.
\]

On each oriented link \(e=(v,w)\), put a gauge coordinate

\[
U_{vw}\in G.
\]

The kinematic basis is labeled by \(G^V\times G^E\). Under a local gauge
transformation \(\lambda\in G^V\),

\[
\phi_v\longmapsto\phi_v+\lambda_v,
\tag{2}
\]

\[
U_{vw}\longmapsto
U_{vw}+\lambda_v-\lambda_w.
\tag{3}
\]

### 2.2 Dressed links

Define

\[
Y_{vw}
=
-\phi_v+U_{vw}+\phi_w.
\tag{4}
\]

Substituting (2)--(3) into (4) gives

\[
Y_{vw}\longmapsto Y_{vw},
\]

so every \(Y_e\) is gauge invariant.

### Proposition 1 — gauge orbits are exactly dressed-link tuples

The map

\[
[(\phi,U)]_{\mathrm{gauge}}
\longmapsto
(Y_e)_{e\in E}
\tag{5}
\]

is a bijection from gauge orbits to \(G^E\).

### Proof

**Surjectivity.** For any \(y\in G^E\), choose

\[
\phi_v=0,\qquad U_e=y_e.
\]

Then \(Y_e=y_e\).

**Injectivity.** Suppose \((\phi,U)\) and \((\phi',U')\) have the same dressed
tuple. Set

\[
\lambda_v=\phi'_v-\phi_v.
\]

Equality of the dressed coordinates implies

\[
U'_{vw}
=
U_{vw}+\lambda_v-\lambda_w.
\]

Equations (2)--(3) therefore carry the first configuration to the second.
They lie in the same orbit. \(\square\)

The gauge action is free because it translates every matter coordinate.
Every orbit has \(|G|^{|V|}\) kinematic configurations.

### Corollary 1 — exact physical factorization

Let a physical orbit state be the normalized gauge-invariant superposition
over one orbit. Proposition 1 gives an orthonormal basis

\[
\{|y_1,\ldots,y_n\rangle_{\mathrm{phys}}:y_i\in G\}.
\]

Hence

\[
\mathcal H_{\mathrm{phys}}
\cong
\bigotimes_{e\in E}\mathbb C[G]_{Y_e}.
\tag{6}
\]

This is not a generic statement about gauge theories. It depends on the
regular-representation matter completion and the frozen dressed-link
observable assignment.

## 3. The target is unchanged

Define the additive Wilson holonomy

\[
H_C=\sum_{e\in C}U_e.
\tag{7}
\]

Summing (4) around the closed cycle gives

\[
\sum_{e=(v,w)\in C}Y_{vw}
=
\sum_{e\in C}U_e
+\sum_{e=(v,w)\in C}(-\phi_v+\phi_w)
=H_C,
\tag{8}
\]

because the matter terms telescope.

For every character \(\chi\in\widehat G\), the Wilson operator is therefore

\[
W_\chi(C)=\chi(H_C)
=
\chi\!\left(\sum_eY_e\right).
\tag{9}
\]

Let \(P_q\) project onto \(H_C=q\). Under (6), these are exactly the
total-\(G\) projectors used in `HC-DU-120`. Neither the target nor the
selective instrument

\[
\mathcal I_q(\rho)=P_q\rho P_q
\tag{10}
\]

has been redefined.

## 4. Exact physical transfer theorem

### Theorem 1 — finite-Abelian Wilson-QND ancillary resource law

Let:

1. \(G\) be a nontrivial finite Abelian group;
2. \(C_n\) be an oriented lattice cycle with \(n\ge2\);
3. regular-representation charged matter complete the gauge field as in
   Section 2;
4. each link station access its local dressed variable \(Y_e\) and one share
   of a pre-distributed gauge-invariant ancilla;
5. local operations finish before classical aggregation;
6. no quantum system cross a station cut during formation; and
7. the target be the exact selective Lüders instrument (10).

Then any exact implementation using a pre-shared resource \(\eta\) satisfies

\[
E_F^{A:B}(\eta)\ge\log_2|G|
\tag{11}
\]

for every nontrivial bipartition \(A:B\) of the link stations. A
character-\(G\)-GHZ resource achieves the instrument exactly and has
\(\log_2|G|\) entanglement across every such cut.

### Proof

By Corollary 1, the physical data Hilbert space is the tensor product of the
dressed-link registers. By (8), the target projectors are the unchanged
total-\(G\) projectors.

Apply (10) to the physical product state

\[
|+\rangle_G^{\otimes n}
=
|G|^{-n/2}
\sum_{y_1,\ldots,y_n}
|y_1,\ldots,y_n\rangle_{\mathrm{phys}}.
\tag{12}
\]

Conditional on holonomy \(q\), the normalized output is

\[
|\psi_q\rangle
=
|G|^{-(n-1)/2}
\sum_{\sum_i y_i=q}
|y_1,\ldots,y_n\rangle_{\mathrm{phys}}.
\tag{13}
\]

Across every nontrivial station cut, (13) has \(|G|\) equal Schmidt
coefficients. It therefore contains \(\log_2|G|\) entanglement.
Average-entanglement monotonicity under LOCC requires at least that much
initial resource entanglement on every cut.

The character-\(G\)-GHZ construction from `HC-DU-120` couples each \(Y_e\)
only to the ancilla share at that station. Because every \(Y_e\) is gauge
invariant, each controlled operation preserves the physical subspace. Local
Fourier readout gives uniformly random proper subsets of shares whose full
sum is \(q\), and the induced data channel is exactly (10). The resource has
\(|G|\) equal Schmidt coefficients across every cut, attaining (11).
\(\square\)

The lower-bound step is standard entanglement monotonicity; the physical
Wilson-loop construction is absorbed by Beckman--Gottesman--Kitaev--Preskill.
The new repository result is the exact typed transfer of `HC-DU-120` into
that matter-completed gauge arena.

## 5. What the resource law prices

Equation (11) prices one resource:

```text
pre-shared ancillary entanglement
across each declared link-station cut.
```

It does not price:

- the existence or preparation of regular-representation charged matter;
- establishment of a superconducting/order-parameter medium along the loop;
- station placement and region assignment;
- access to the local dressed current or link variable;
- construction and control accuracy of the local coupling;
- ancilla creation and distribution energy;
- storage lifetime and error correction;
- later classical communication and aggregation latency;
- acquisition completeness or rejected attempts; or
- observer readout, certification, and action integration.

The exact statement is therefore:

> \(\log_2|G|\) is the optimal ancillary entanglement stock under a supplied
> matter-completed regional instrument contract.

It is not:

> \(\log_2|G|\) is the complete physical cost of measuring a Wilson loop.

This distinction is a direct application of Dynamic Unity's resource and
interface typing, not a weakness in the mathematical lower bound.

## 6. Why the surrounding cases stay separate

### 6.1 Pure Abelian gauge theory

Without charged matter, the dressed variables (4) are unavailable. A
homologically trivial loop may be represented through local plaquette fluxes,
but a homologically nontrivial Wilson loop can fall outside the algebra
generated by local observables. The theorem above cannot simply delete
\(\phi\) and keep its conclusion.

### 6.2 Continuous Abelian groups

For compact continuous groups, exact ideal ancilla states can become
non-normalizable; finite precision requires an approximation contract. The
finite-group exact resource law does not transfer without introducing error,
energy, dimension, and resolution terms.

### 6.3 Non-Abelian loops

Ordered multiplication and noncommuting representations replace the Abelian
sum. Beckman--Gottesman--Kitaev--Preskill prove that the spacelike
nondemolition operation is acausal under their non-Abelian assumptions. The
finite-Abelian theorem is not a lower-order approximation to that case.

### 6.4 Other regional algebra assignments

Gauss constraints and boundary centers make region-to-algebra assignments
noncanonical in general. The factorization (6) is earned only in the explicit
matter-completed link algebra. An electric-center, magnetic-center,
pure-gauge, AQFT, or continuum assignment requires its own proof.

## 7. Record and observer consequences

The physical architecture is now explicit:

```text
finite-Abelian gauge field plus charged matter
  -> gauge-invariant dressed link variables
  -> local controlled writes into pre-shared entangled shares
  -> every proper share subset is Wilson-blind
  -> later causal aggregation recovers the holonomy
  -> the data undergoes the exact Wilson-sector Lüders channel
  -> an observer with joined-share access can act on the Wilson fact.
```

This is a real known-physics example of layered regional formation:

- the physical distinction exists in the gauge/matter system;
- local stations interact with it without individually learning it;
- the shares form on the measurement slice;
- the joined record becomes accessible only after aggregation; and
- the target is final relative to the declared nondemolition instrument.

It does not establish that records create the gauge field, that regional
finality is fundamental, that the apparatus is selected by the gauge action,
or that every observer has access.

## 8. Exact regression

The deterministic probe checks:

- \(\mathbb Z_2,\mathbb Z_3,\mathbb Z_4\), and
  \(\mathbb Z_2\times\mathbb Z_2\);
- three-link cycles plus one four-link cycle;
- every kinematic configuration and every local gauge transformation;
- gauge invariance of every dressed link;
- equality of each dressed tuple with exactly one gauge orbit;
- reachability and independence of all \(G^E\) physical tuples;
- equality of bare and dressed Wilson holonomy;
- equality with the unchanged total-charge Lüders channel;
- blindness of every proper share subset;
- exact joined-share reconstruction; and
- equality of the inherited lower and upper entanglement bounds.

It returns `14/14` over five specimens. It is a regression for the exact proof,
not a dynamical lattice simulation or a source of new physical evidence.

## 9. Grade, novelty, and disposition

### Earned

- exact physical orbit reduction for the frozen matter-completed finite
  lattice arena;
- unchanged transfer of the finite-Abelian total-charge instrument to Wilson
  holonomy;
- exact ancillary-entanglement necessity and sufficiency in that arena;
- explicit separation of ancillary resource cost from supplied physical
  interface cost; and
- a concrete known-physics regional record architecture.

### Absorbed

- localizable Abelian Wilson-loop nondemolition measurement;
- gauge-invariant dressed link variables;
- gauge-theory factorization warnings;
- LOCC entanglement monotonicity;
- entanglement production as a measurement-cost lower bound; and
- GHZ/group-Fourier distributed measurement.

### Not earned

- a selected matter/probe/access interface;
- a complete resource or energy law;
- pure-gauge, continuous, non-Abelian, arbitrary-topology, AQFT, or continuum
  transfer;
- a held-out time, geometry, field, or capability reconstruction;
- empirical excess or a finite physical remainder;
- ontology priority, new physics, or prediction; or
- a paper or experiment.

The grade is scoped Grade 4 because the conditional physical transfer and
resource necessity are exact. Novelty remains modest: the ingredients are
mature, and the contribution is their rigorous typed conjunction at Dynamic
Unity's record/access boundary.

## 10. North-Star consequence and reopeners

`HC-DU-120` asked whether its exact abstract resource law survived a physical
QFT/lattice-gauge realization. In this finite matter-completed arena, it does.

That advances the North Star by replacing one abstract candidate with a
genuinely gauge-invariant record-formation example. The remaining hard step
has moved:

> The question is no longer whether one Wilson target can be formed as an
> exact regional record. It is whether physics selects this interface, or
> whether the formed Wilson record reconstructs an independently held-out
> observer capability without refitting the apparatus.

Reopen through one of:

1. transfer the unchanged formed Wilson record to a held-out gauge-field
   response or observer capability under a frozen action class;
2. derive a typed tradeoff among ancillary entanglement, quantum
   communication, causal depth, station count, error, and aggregation
   latency;
3. prove a natural interface selector within a frozen gauge/matter theory;
4. obtain an exact finite-error continuous-group law with physical energy and
   resolution accounting; or
5. identify a non-Abelian or algebraic-QFT access result that is not absorbed
   by the known causality and regional-algebra boundaries.

No successor is selected. More finite-Abelian group or cycle variants without
one of these increments are stopped.
