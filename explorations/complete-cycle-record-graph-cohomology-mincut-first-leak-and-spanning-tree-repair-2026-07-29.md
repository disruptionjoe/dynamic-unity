---
title: "Complete cycle records: graph cohomology, min-cut first leaks, and spanning-tree repair"
status: completed_scoped_result
doc_type: graph_cohomological_reconstruction_and_topological_remainder_theorem
created: 2026-07-29
hypothesis_id: HC-DU-123
run_id: RUN-20260729-131834-graph-cycle-record-cohomology
authority: "Joe direct chat: Go"
lanes:
  - lane_1
  - lane_4
  - lane_5
  - lane_7
channels:
  - CH-FORMAL
  - CH-COLLIDE
  - CH-MODEL
  - CH-SYN
maximum_grade: "Scoped Grade 4 exact graph-cohomological reconstruction, topology-controlled first-leak, and minimum universal informational-repair theorem in the matter-completed finite-Abelian arena; no selected graph, cycle basis, joint instrument, observer boundary, unrestricted state reconstruction, continuum transfer, empirical excess, new physics, or prediction"
frozen_read_revisions:
  dynamic_unity_parent: 71f736c6da3d
probe: "../tests/du_graph_cycle_record_cohomology_probe.py"
artifact: "../tests/artifacts/du_graph_cycle_record_cohomology_result.json"
---

# A complete loop record is exactly a cohomology class, not the complete physical network

## Executive result

The swing returned:

```text
COMPLETE_CYCLE_RECORD_IS_THE_GRAPH_COHOMOLOGY_CLASS
+ CYCLE_RECORD_FIBRE_IS_EXACTLY_AN_AFFINE_COBBOUNDARY_CLASS
+ RECORD_EQUIVALENCE_IS_SPANNING_TREE_INVARIANT
+ ALL_CLOSED_CHAIN_CHARACTER_RESPONSES_RECONSTRUCT
+ OPEN_PATH_RESPONSES_EXPOSE_ENDPOINT_RELATIVE_REMAINDER
+ RESPONSE_FACTORS_IFF_CHAIN_BOUNDARY_ANNIHILATES_THE_GROUP
+ MINIMUM_OPEN_PATH_LEAK_SUPPORT_EQUALS_ENDPOINT_EDGE_CONNECTIVITY
+ BRIDGES_CREATE_ONE_EDGE_FIRST_LEAKS
+ CYCLE_SPECIALIZATION_RECOVERS_THE_HC_DU_122_TWO_LINK_WITNESS
+ FIBRE_SIZE_IS_GROUP_ORDER_TO_VERTEX_COUNT_MINUS_ONE
+ SPANNING_TREE_ACCESS_IS_INFORMATIONALLY_MINIMAL_UNIVERSAL_REPAIR
+ MATTER_MAKES_COBBOUNDARY_DIRECTIONS_PHYSICAL_NOT_GAUGE
+ NO_JOINT_RESOURCE_LAW_INTERFACE_SELECTION_OR_EMPIRICAL_EXCESS
+ NO READY SUCCESSOR
```

`HC-DU-122` proved on one cycle that the formed Wilson record reconstructs
every closed-loop winding but no proper open path. The one-cycle answer was
not accidental. It is the specialization of an exact theorem on every finite
connected graph.

Let \(G\) be a nontrivial finite Abelian group and let the physical
matter-completed dressed-edge configuration be

\[
y\in C^1(\Gamma;G)=G^E.
\]

A complete independent set of cycle holonomies records precisely the
cohomology class

\[
[y]\in H^1(\Gamma;G).
\]

Its fibre is not an unspecified remainder. It is exactly the affine
coboundary class

\[
y+\operatorname{im}d,
\]

containing

\[
|G|^{|V|-1}
\]

physical dressed-edge configurations.

Every closed-cycle character response is fixed on that fibre. Every ordinary
open path between distinct endpoints varies inside it.

The new sharp result is a distance law:

> The fewest dressed edges that can change while every cycle record remains
> fixed and an open \(u\)-to-\(v\) response changes is exactly the minimum
> \(u\)-\(v\) edge-cut size \(\lambda_\Gamma(u,v)\).

Thus:

- a bridge permits a one-edge first leak;
- a simple cycle requires two coordinated edge changes;
- \(K_4\) requires three for every endpoint pair.

This is the graph-topological form of capability-relative record sufficiency.
It is absorbed mathematics composed with known Wilson/open-line physics, not
new physics. But it gives Dynamic Unity a reusable exact architecture in
which regional records, physical remainders, network robustness, and finer
access are one theorem rather than an analogy.

## 1. Physical and operational setup

Let

\[
\Gamma=(V,E)
\]

be a finite connected simple graph with an arbitrary edge orientation.

Retain the matter completion from `HC-DU-121`. For each oriented edge
\(e=(u,v)\), the gauge-invariant dressed variable is

\[
y_e=-\phi_u+U_{uv}+\phi_v\in G.
\tag{1}
\]

Complete dressed-edge tuples label distinct physical gauge orbits. In
particular, changing \(y\) by a graph coboundary is not a gauge
transformation: every \(y_e\) is already gauge invariant.

[Beckman, Gottesman, Kitaev, and
Preskill](https://arxiv.org/abs/hep-th/0110205) supply the physical
matter-dressed Abelian Wilson-loop measurement and the distinction between
nondemolition loop access and finer local access.

[Gliozzi](https://arxiv.org/abs/hep-lat/0511039) supplies the corresponding
gauge-invariant open-line class: a gauge transporter along an open path is
saturated by charged matter at its endpoints.

The graph theorem below does not derive the graph, matter, apparatus, cycle
basis, or observer access. It asks what an already formed complete cycle
record reconstructs.

## 2. Coordinating the complete cycle record

Choose a spanning tree

\[
T\subseteq E.
\]

Every chord \(e\in E\setminus T\) closes one fundamental cycle \(z_e\). The
number of chords is the graph's first Betti number

\[
\beta_1=|E|-|V|+1.
\tag{2}
\]

Define the cycle-record map

\[
Q_T:C^1(\Gamma;G)\to G^{\beta_1}
\]

by

\[
Q_T(y)
=
\big(\langle z_e,y\rangle\big)_{e\notin T}.
\tag{3}
\]

Each component is an Abelian Wilson holonomy. Because every fundamental cycle
contains its own chord and no other chord, \(Q_T\) is surjective.

The spanning tree is a coordinate choice, not a physical foliation, preferred
network, or selected observer boundary.

## 3. The record fibre is exactly the coboundary space

Define the graph coboundary

\[
d:C^0(V;G)\to C^1(E;G)
\]

by

\[
(da)_{uv}=a_v-a_u.
\tag{4}
\]

### Theorem 1 — complete cycle record kernel

For every connected finite graph, finite Abelian \(G\), and spanning tree
\(T\),

\[
\ker Q_T=\operatorname{im}d.
\tag{5}
\]

### Proof

If \(y=da\), its sum around every closed cycle telescopes to zero. Therefore
\(\operatorname{im}d\subseteq\ker Q_T\).

Conversely, suppose every fundamental-cycle integral of \(y\) vanishes.
Choose a root vertex \(r\). For every vertex \(v\), define \(a_v\) by
integrating \(y\) along the unique tree path from \(r\) to \(v\), with signs
set by the edge orientation. Then

\[
y_e=(da)_e
\]

on every tree edge. For a chord, its zero fundamental-cycle integral forces
the same equality on that chord. Hence \(y=da\). \(\square\)

### Corollary 1 — exact quotient

Because a graph has no cellular 2-cochains,

\[
H^1(\Gamma;G)
=
C^1(\Gamma;G)/\operatorname{im}d.
\tag{6}
\]

Equations (3)--(5) therefore give

\[
C^1(\Gamma;G)/\ker Q_T
\cong
H^1(\Gamma;G)
\cong
G^{\beta_1}.
\tag{7}
\]

The complete cycle record is exactly a coordinate presentation of the
cohomology class \([y]\).

### Corollary 2 — tree invariance

Every spanning tree gives the same kernel \(\operatorname{im}d\). Changing
trees changes the fundamental-cycle coordinates by an invertible integral
basis transformation, but not which physical configurations the record
identifies.

This is the relevant invariance result:

```text
decoder coordinates change
record equivalence does not.
```

## 4. Exact capability-factorization theorem

Let

\[
c\in C_1(\Gamma;\mathbb Z)
\]

be an integer edge chain. Define its \(G\)-valued physical response

\[
L_c(y)=\langle c,y\rangle=\sum_{e\in E}c_e y_e.
\tag{8}
\]

The complete charged-probe response family is

\[
\mathcal R_c(y)
=
\{\chi(L_c(y)):\chi\in\widehat G\}.
\tag{9}
\]

Finite-Abelian characters separate group elements, so \(\mathcal R_c\)
factors through \(Q_T\) exactly when \(L_c\) does.

Write \(\partial c\) for the vertex boundary of the chain. For an integer
\(m\), \([m]_G\) denotes multiplication by \(m\) on \(G\).

### Theorem 2 — boundary criterion

The following are equivalent:

1. \(\mathcal R_c\) is reconstructed from the complete cycle record;
2. \(L_c\) is constant on every cycle-record fibre;
3. \(L_c\) annihilates \(\operatorname{im}d\); and
4. every vertex-boundary coefficient annihilates \(G\):

   \[
   [(\partial c)_v]_G=0
   \qquad
   \text{for all }v\in V.
   \tag{10}
   \]

### Proof

Conditions 1--3 follow from character separation, fibre factorization, and
Theorem 1.

Discrete integration by parts gives

\[
L_c(da)
=
\langle c,da\rangle
=
\langle\partial c,a\rangle
=
\sum_{v\in V}(\partial c)_v a_v.
\tag{11}
\]

If (10) holds, (11) vanishes for every vertex potential \(a\), proving
condition 3.

Conversely, choose \(a\) supported on one vertex. If (11) vanishes for every
value of that vertex potential, its boundary coefficient must act as the zero
endomorphism on \(G\). Repeat at every vertex to obtain (10). \(\square\)

Condition (10), rather than literal integer boundary zero, is exact for finite
groups. A coefficient divisible by the exponent of \(G\) also annihilates the
group. The ordinary physical cycle/open-path cases do not need that
periodicity caveat, but the theorem and regression retain it.

## 5. Closed reconstruction and open-path remainder

### Corollary 3 — every ordinary closed response reconstructs

If \(c\) is an integer cycle,

\[
\partial c=0.
\]

Theorem 2 says that every character response of \(c\) is exactly determined by
the complete cycle record.

Equivalently, every cycle is an integer combination of the fundamental
cycles, so its value is the same combination of the recorded components.

### Corollary 4 — every simple open path leaks

Let \(p\) be an oriented simple path from \(u\) to \(v\), with \(u\ne v\).
Then

\[
\partial p=v-u.
\tag{12}
\]

The coefficients \(-1\) and \(+1\) do not annihilate a nontrivial \(G\).
Therefore \(L_p\) does not factor through \(Q_T\).

This remains true even if every cycle holonomy in the graph has been formed
and retained.

## 6. The first-leak support is exactly a minimum cut

Theorem 1 says that two configurations have the same complete cycle record
exactly when their difference is a coboundary:

\[
y'-y=da.
\tag{13}
\]

For a \(u\)-to-\(v\) path, equation (11) becomes

\[
L_p(y')-L_p(y)
=
a_v-a_u.
\tag{14}
\]

Thus an undetected change alters the endpoint response exactly when the
potential differs at the endpoints.

Let

\[
\lambda_\Gamma(u,v)
\]

be the size of a minimum edge cut separating \(u\) and \(v\).

### Theorem 3 — topological first-leak distance

Among all same-cycle-record pairs with different \(u\)-to-\(v\) path
responses,

\[
\min
\big|\operatorname{supp}(y'-y)\big|
=
\lambda_\Gamma(u,v).
\tag{15}
\]

### Proof

**Upper bound.** Let \(S\subset V\) be one side of a minimum \(u\)-\(v\) cut,
with \(u\in S\) and \(v\notin S\). Choose nonzero \(g\in G\) and set

\[
a_w=
\begin{cases}
0,&w\in S,\\
g,&w\notin S.
\end{cases}
\]

Then \(da\) is nonzero exactly on the cut edges. It lies in the cycle-record
kernel, has support \(\lambda_\Gamma(u,v)\), and changes every \(u\)-to-\(v\)
path response by \(g\).

**Lower bound.** Let \(da\) change the endpoint response, so
\(a_u\ne a_v\). Remove every edge on which \(da\ne0\). Along every remaining
edge the endpoint potentials agree, so \(u\) and \(v\) lie in different
connected components. The support of \(da\) therefore contains an
\(u\)-\(v\) cut and has size at least \(\lambda_\Gamma(u,v)\).
\(\square\)

### Exact specializations

```text
tree bridge:
  lambda = 1
  one physical edge can leak while all cycle records stay fixed

simple cycle:
  lambda = 2
  recovers the +a/-a two-link HC-DU-122 witness

complete graph K4:
  lambda = 3
  every endpoint leak needs at least three coordinated edge changes
```

The min-cut acts like a record-fibre distance for that endpoint capability.
This is a formal statement, not an imported consensus, cryptographic, or
error-correction theorem.

## 7. Exact fibre size

The kernel of

\[
d:G^V\to G^E
\]

is the constant vertex potentials, a copy of \(G\). Therefore

\[
|\operatorname{im}d|
=
\frac{|G|^{|V|}}{|G|}
=
|G|^{|V|-1}.
\tag{16}
\]

Every complete cycle-record fibre consequently has exactly

\[
|G|^{|V|-1}
\]

physical dressed-edge basis configurations, independent of the graph's cycle
rank.

The cycle rank determines the size of the recorded quotient. The vertex rank
determines the size of the remaining physical fibre:

\[
|G|^{|E|}
=
\underbrace{|G|^{|E|-|V|+1}}_{\text{cycle record}}
\times
\underbrace{|G|^{|V|-1}}_{\text{coboundary remainder}}.
\tag{17}
\]

Equation (17) is cardinal multiplication, not an entropy or thermodynamic
decomposition.

## 8. Minimum universal repair

The admitted open paths include every single edge, whose full character
family separates its dressed value. Completing all open- and closed-path
responses is therefore equivalent to reconstructing the complete tuple
\(y\in G^E\).

If every additional coordinate has at most \(|G|\) values, distinguishing the
\(|G|^{|V|-1}\) states in one fibre requires

\[
k\ge |V|-1
\tag{18}
\]

additional coordinates.

Any spanning tree attains the bound. Given:

1. all fundamental-cycle records \(Q_T(y)\); and
2. the \(|V|-1\) dressed-edge values \(y_e\) on \(T\),

the fundamental-cycle equation for each chord uniquely recovers that chord's
value. Thus the whole edge tuple is reconstructed.

The same information can be expressed as rooted matter-completed open-path
values, but a root and path family are then supplied.

This is a universal informational repair theorem. It does not prove that:

- the tree values are selected naturally;
- their acquisition is nondemolition;
- they can be formed for the same resource cost as cycle records; or
- a spanning tree has physical priority.

## 9. Why matter changes the conclusion

In a pure Abelian gauge theory, exact one-cochains can represent gauge
redundancy, and loop holonomies may classify a connection only up to gauge
under suitable conditions.

That reading is unavailable here. In the frozen `HC-DU-121` arena:

\[
y_e=-\phi_u+U_{uv}+\phi_v
\]

is already gauge invariant, and complete \(y\)-tuples label distinct physical
orbits. Two tuples separated by \(da\) are physically distinct even though
all their closed-loop records agree. Matter-saturated open lines can expose
the difference.

Therefore:

> Whether the cohomology quotient is a complete physical description or a
> capability-relative coarse record depends on the matter and action
> interface—not on graph topology alone.

This is the load-bearing type correction. Dropping the matter while retaining
its physical open-line capabilities would silently change the theory.

## 10. Regional and distributed-systems interpretation

The exact theorem has a disciplined distributed reading:

- cycle records certify all circulations around the network;
- different spanning-tree decoders agree on the same quotient;
- endpoint-relative potentials remain unresolved;
- an endpoint capability sees that remainder;
- graph connectivity sets the support required for an undetected endpoint
  change; and
- a spanning-tree-sized finer interface completes the network state.

This helps explain why a highly redundant regional record can be robust and
still incomplete. Robustness against sparse changes is not completeness for
every action.

But no FLP, CAP, BFT, Hashgraph, Avalanche, cryptographic, or common-knowledge
claim follows. Those theories add faults, schedules, authentication,
probabilities, decision rules, and liveness/safety contracts not present in
this graph theorem.

## 11. Grade and absorber audit

### Earned

- exact cohomological identity of the complete cycle record;
- exact affine-coboundary record fibre;
- spanning-tree invariance of record equivalence;
- exact iff factorization criterion for every integer edge chain;
- exact reconstruction of all closed-cycle character responses;
- exact failure of all ordinary simple open paths;
- exact min-cut first-leak distance;
- bridge, cycle, and \(K_4\) specializations;
- exact fibre cardinality; and
- exact \(|V|-1\)-coordinate universal repair lower bound and construction.

### Absorbed

- cellular graph cohomology;
- fundamental-cycle bases and spanning trees;
- cycle/cut duality;
- max-flow/min-cut reasoning;
- finite-Abelian character separation;
- Wilson and matter-completed open-line physics; and
- Dynamic Unity's generic fibre factorization.

### Not earned

- selection of graph, group, matter, orientation, spanning tree, cycle
  coordinates, joint QND instrument, or observer action class;
- an optimal resource law for forming all overlapping cycle records;
- an information/disturbance tradeoff for tree repair;
- unrestricted quantum-state or process reconstruction;
- transfer to pure gauge theory, non-Abelian or continuous groups,
  higher-dimensional cell complexes, AQFT, or continuum QFT;
- empirical excess over standard physics;
- ontology priority, new physics, or a prediction.

The maximum grade is scoped Grade 4. The necessity and distance theorems are
exact, but their ingredients are mature and the physical interface remains
supplied.

## 12. Exact local evidence

The deterministic regression checks:

- a four-vertex tree;
- a triangle;
- a square with diagonal;
- two triangles connected by a bridge; and
- \(K_4\);
- \(\mathbb Z_2,\mathbb Z_3\), and
  \(\mathbb Z_2\times\mathbb Z_2\);
- every spanning tree in each graph;
- every edge chain in \(\{-1,0,1\}^{|E|}\);
- every simple path between every endpoint pair;
- every record kernel and fibre;
- every endpoint min-cut against exhaustive vertex potentials; and
- every spanning-tree repair map.

It returns `18/18`. The theorem is proved algebraically; enumeration is only a
bounded exact regression and earns no independent scientific grade.

## 13. Reopeners

1. Derive a natural physical dynamics that selects a cycle quotient, an
   endpoint/open-path quotient, or a nested family rather than supplying it.
2. Derive the exact joint resource and disturbance tradeoff for forming a
   cycle basis and then refining it with tree/open-path access.
3. Extend the result to a finite 2-complex, where plaquette relations and
   \(H^2\) can distinguish local curvature records from global holonomy.
4. Determine the non-Abelian replacement, where holonomies do not add and
   cycle-basis coordinates are conjugation- and ordering-sensitive.
5. Seek a continuum algebraic version in which a conditional expectation
   replaces \(Q_T\), its kernel is physically typed, and a finite admitted
   action realizes the first leak.

No reopener is selected automatically.
