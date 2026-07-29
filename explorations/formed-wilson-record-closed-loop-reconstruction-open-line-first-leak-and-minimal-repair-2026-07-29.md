---
title: "Formed Wilson record: closed-loop reconstruction, open-line first leak, and minimal universal repair"
status: completed_scoped_result
doc_type: capability_relative_reconstruction_and_first_leak_theorem
created: 2026-07-29
hypothesis_id: HC-DU-122
run_id: RUN-20260729-130657-wilson-record-capability-first-leak
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
maximum_grade: "Scoped Grade 4 exact capability-relative reconstruction, first-leak, and minimum universal informational-repair theorem in the HC-DU-121 finite-Abelian lattice arena; no selected interface, unrestricted quantum-state tomography, universal gauge theorem, empirical excess, new physics, or prediction"
frozen_read_revisions:
  dynamic_unity_parent: 6a77b0737f84
probe: "../tests/du_wilson_record_capability_first_leak_probe.py"
artifact: "../tests/artifacts/du_wilson_record_capability_first_leak_result.json"
---

# One formed physical record can be complete for one action and incomplete for another

## Executive result

The swing returned:

```text
CLOSED_LOOP_PROBE_RESPONSE_FACTORS_THROUGH_FORMED_WILSON_RECORD
+ ALL_WINDING_CHARACTER_RESPONSES_ARE_EXACTLY_RECONSTRUCTED
+ PATH_RESPONSE_FACTORS_IFF_COEFFICIENT_ENDOMORPHISMS_AGREE
+ EVERY_PROPER_OPEN_PATH_IS_A_CAPABILITY_FIRST_LEAK
+ SAME_RECORD_DIFFERENT_OPEN_LINE_RESPONSE_HAS_A_TWO_LINK_WITNESS
+ ONE_FORMED_RECORD_SUPPORTS_RECONSTRUCTION_AND_REMAINDER_RELATIVE_TO_ACTION
+ WILSON_FIBRE_HAS_GROUP_ORDER_TO_N_MINUS_ONE_BASIS_COMPLETIONS
+ N_MINUS_ONE_ADDITIONAL_GROUP_COORDINATES_COMPLETE_ALL_PATH_RESPONSES
+ UNIVERSAL_REPAIR_IS_A_FINER_POTENTIALLY_DESTRUCTIVE_INTERFACE
+ NO_INTERFACE_SELECTION_OR_EMPIRICAL_EXCESS
+ NO READY SUCCESSOR
```

`HC-DU-121` established a real finite lattice-gauge formation architecture.
Regular-representation charged matter turns the physical orbit basis into
independent gauge-invariant dressed links

\[
y=(y_1,\ldots,y_n)\in G^n,
\]

and the regional QND protocol forms only their Wilson sum

\[
Q(y)=\sum_{i=1}^n y_i=q.
\tag{1}
\]

This result holds that arena and record fixed and asks what the already formed
record predicts.

The answer is exact:

> The Wilson record reconstructs every character response of every complete
> closed-loop winding. It does not reconstruct the corresponding response of
> any proper matter-completed open path. The first leak needs only two link
> changes that cancel in the loop sum.

There is no contradiction. Record sufficiency is relative to a declared
future action and target:

```text
same formed record q
  -> exact for all closed-loop winding responses
  -> incomplete for every proper open-line response.
```

This is the first exact Dynamic Unity specimen in which one independently
formed physical record supports both a positive reconstruction theorem and a
finite physical remainder, depending only on which admitted capability is
queried.

The constituent gauge physics is known. The factorization proof is elementary
finite-group mathematics. The earned contribution is the typed, no-refit
composition: formation, record, response class, first leak, and repair are all
held apart in one physical arena.

## 1. Frozen physical arena

Retain the complete `HC-DU-121` contract:

1. \(G\) is a nontrivial finite Abelian group;
2. \(n\ge2\) dressed links form an oriented cycle;
3. regular-representation matter gives the physical orbit basis
   \(\mathbb C[G]^{\otimes n}\);
4. \(y_i\in G\) is the gauge-invariant dressed value of link \(i\);
5. the regional QND instrument has already formed only \(q=Q(y)\);
6. no dressed-link transcript is silently retained; and
7. future capabilities are charged-probe character responses fixed before
   checking record sufficiency.

[Beckman, Gottesman, Kitaev, and
Preskill](https://arxiv.org/abs/hep-th/0110205) establish the physical
distinction between an Abelian nondemolition Wilson-loop measurement and the
finer, potentially destructive access obtained by resolving local
matter-dressed variables.

[Gliozzi](https://arxiv.org/abs/hep-lat/0511039) treats open Wilson lines whose
charged matter endpoints make them gauge-invariant physical observables.
Thus an open line in the matter-completed arena is not a gauge-dependent
fiction. It is a different admitted operation.

Neither source says that one Wilson record reconstructs the complete gauge
configuration. That is the question tested here.

## 2. The held-out response family

For an integer coefficient vector

\[
c=(c_1,\ldots,c_n)\in\mathbb Z^n,
\]

define the path value

\[
L_c(y)=\sum_{i=1}^n c_i y_i\in G.
\tag{2}
\]

For every character \(\chi\in\widehat G\), define the diagonal charged-probe
response operator

\[
W_{\chi,c}|y\rangle
=
\chi(L_c(y))|y\rangle.
\tag{3}
\]

The complete held-out response is

\[
\mathcal R_c(y)
=
\{\chi(L_c(y)):\chi\in\widehat G\}.
\tag{4}
\]

Characters separate the points of a finite Abelian group. Consequently,
reconstructing every response in (4) is equivalent to reconstructing the
single group element \(L_c(y)\).

The relevant physical cases are:

- a loop winding \(k\) times:
  \(c=(k,\ldots,k)\);
- the once-around Wilson loop:
  \(c=(1,\ldots,1)\); and
- a proper simple matter-completed open path:
  \(c_i\in\{0,1\}\), with at least one included and one excluded link.

## 3. Exact factorization theorem

For \(m\in\mathbb Z\), write

\[
[m]_G:G\to G,\qquad x\mapsto mx
\]

for the integer-multiplication endomorphism.

### Theorem 1 — capability-relative Wilson-record factorization

The following are equivalent:

1. the complete response family \(\mathcal R_c\) is determined by the formed
   Wilson record \(Q\);
2. \(L_c\) is constant on every fibre \(Q^{-1}(q)\);
3. \(L_c=f\circ Q\) for some map \(f:G\to G\); and
4. all coefficient endomorphisms agree:

   \[
   [c_1]_G=[c_2]_G=\cdots=[c_n]_G.
   \tag{5}
   \]

When these conditions hold,

\[
L_c=[c_1]_G\circ Q.
\tag{6}
\]

### Proof

Characters separate points, so conditions 1 and 2 are equivalent. Conditions
2 and 3 are the ordinary fibre-factorization criterion.

If (5) holds, then

\[
L_c(y)
=\sum_i[c_i]_G(y_i)
=\sum_i[c_1]_G(y_i)
=[c_1]_G\!\left(\sum_i y_i\right),
\]

which proves (6).

Conversely, suppose \(L_c=f\circ Q\). Both \(Q\) and \(L_c\) are group
homomorphisms, and \(Q:G^n\to G\) is surjective. Therefore \(f\) is a group
homomorphism. Put an arbitrary \(x\in G\) on link \(i\) and zero on every
other link. Then

\[
f(x)=L_c(0,\ldots,x,\ldots,0)=[c_i]_G(x).
\]

This holds for every link and every \(x\), forcing (5). \(\square\)

The condition compares endomorphisms, not literal integer coefficients.
For example, coefficients differing by the exponent of \(G\) act
identically. The exact regression checks this periodicity rather than
replacing it with integer equality.

### Operator form

Let \(P_q\) project onto the formed Wilson sector \(Q=q\). Theorem 1 is
equivalently:

\[
P_qW_{\chi,c}P_q
\quad\text{is a scalar multiple of }P_q
\]

for every \(q,\chi\) exactly when (5) holds.

Thus the result is not limited to ignorance about classical basis labels. In
a formed \(q\)-sector, every admitted closed-loop response is fixed, whereas
an open-line response can still distinguish density operators supported in
that same sector.

## 4. Closed-loop positive

For a \(k\)-fold loop,

\[
c=(k,\ldots,k).
\]

Every coefficient endomorphism is \([k]_G\), so Theorem 1 gives

\[
L_c(y)
=
[k]_G(Q(y))
=
kq.
\tag{7}
\]

Therefore:

> The formed Wilson value reconstructs the complete character-response family
> for every winding number, with no access to the individual dressed links.

This is a genuine target-relative reconstruction theorem. It is not full
gauge-state reconstruction.

## 5. Every proper open path is a first leak

A proper simple open path has at least one coefficient \(1\) and at least one
coefficient \(0\). Since \(G\) is nontrivial,

\[
[1]_G\ne[0]_G.
\]

Theorem 1 immediately gives:

### Corollary 1 — universal proper-open-path failure

No proper simple matter-completed open-path character response factors through
the formed Wilson record.

This is not an abstract missing variable. The response is a gauge-invariant
physical observable in the frozen matter-completed arena.

## 6. The smallest exact witness

Choose:

- a link \(i\) inside the proper path;
- a link \(j\) outside it; and
- any nonzero \(a\in G\).

Compare

\[
y=(0,\ldots,0)
\]

with

\[
y'_i=a,\qquad
y'_j=-a,\qquad
y'_\ell=0\quad(\ell\notin\{i,j\}).
\tag{8}
\]

Their Wilson records agree:

\[
Q(y)=0=Q(y').
\tag{9}
\]

But the open-path values differ:

\[
L_c(y)=0,\qquad L_c(y')=a.
\tag{10}
\]

Because finite-Abelian characters separate points, at least one physical
character probe distinguishes (10).

One link cannot change while preserving its total sum. Equation (8) changes
exactly two links, so the witness is support-minimal.

This is the smallest physical remainder exposed by enlarging the action class
from complete closed loops to one proper open line.

## 7. Fibre size and repair

For every \(q\in G\), freely choose \(y_1,\ldots,y_{n-1}\). The final link is
then fixed by

\[
y_n=q-\sum_{i=1}^{n-1}y_i.
\]

Therefore:

\[
|Q^{-1}(q)|=|G|^{n-1}.
\tag{11}
\]

There are two distinct repair questions.

### 7.1 Repairing one predeclared target

Adding the single value \(L_c(y)\) repairs the response for that one path.
This is mathematically minimal but target-coded. It does not produce a
general physical interface and cannot be added after seeing which held-out
target failed.

### 7.2 Completing all path responses

The admitted proper paths include every single-link path, and their complete
character families separate every dressed-link tuple. Completing all such
responses is therefore equivalent to identifying the full physical basis
label \(y\).

Suppose every added coordinate takes at most \(|G|\) values. Distinguishing
all \(|G|^{n-1}\) states in one Wilson fibre requires at least \(n-1\)
additional coordinates:

\[
|G|^k\ge |G|^{n-1}
\quad\Longrightarrow\quad
k\ge n-1.
\tag{12}
\]

The record

\[
\big(Q(y),y_1,\ldots,y_{n-1}\big)
\tag{13}
\]

attains the bound and reconstructs \(y_n\), hence every path response.

Equation (12) is an informational cardinality bound under a declared
\(G\)-valued-coordinate contract. It is not a thermodynamic, energetic, or
QND measurement-cost law.

Most importantly, the repair is a finer interface. Resolving local dressed
links can destroy coherence within a fixed Wilson sector, exactly as the
Wilson-loop measurement literature warns. The original regional QND protocol
cannot be called universally sufficient by silently replacing it with (13).

## 8. What changed for Dynamic Unity

Before this result, the program had:

1. a generic theorem saying record sufficiency is target-relative;
2. a real regional mechanism that forms a gauge record; and
3. an exact ancillary-entanglement price for that formation mechanism.

It now has one complete known-physics composition:

```text
finite gauge/matter arena
  -> independent dressed-link physical basis
  -> regional QND formation of q
  -> exact closed-loop response reconstruction
  -> two-link first leak under proper open-line access
  -> finite universal repair dimension.
```

The key scientific lesson is:

> A physical record does not need to encode the entire underlying state to be
> fully real or exactly sufficient. Its sufficiency boundary is the quotient
> induced by the actions the observer can actually perform.

Conversely:

> Enlarging capability can split a previously adequate record fibre without
> changing the already formed record or falsifying its earlier reconstruction
> theorem.

This is the cleanest current bridge between Dynamic Unity's record-first and
physical-remainder branches. Both can be true in the same system.

## 9. Grade and absorber audit

### Earned

- exact iff factorization theorem for all integer path coefficients;
- exact reconstruction of every closed-loop winding response;
- exact failure for every proper simple open path;
- support-minimal two-link same-record/different-response witness;
- exact Wilson-fibre cardinality;
- exact \(n-1\) universal \(G\)-coordinate repair bound and construction; and
- one no-refit composition of physical record formation, reconstruction,
  capability enlargement, and remainder.

### Absorbed

- Wilson and open-Wilson-line physics;
- character separation for finite Abelian groups;
- quotient/fibre factorization;
- elementary finite-group homomorphism algebra; and
- cardinality lower bounds.

### Not earned

- selection of \(G\), matter, graph, action class, stations, instrument, or
  observer boundary;
- unrestricted gauge-state, process, or continuum-field reconstruction;
- a proof that the universal repair can be formed nondestructively;
- transfer to pure gauge theory, non-Abelian or continuous groups, arbitrary
  topology, AQFT, or continuum QFT;
- empirical excess over standard gauge theory;
- a novel physical law or prediction; or
- evidence that records are the fundamental substrate of reality.

The maximum grade is scoped Grade 4. The theorem is exact and physically typed,
but it organizes known physics rather than exceeding it.

## 10. Local evidence

The deterministic regression checks:

- \(\mathbb Z_2,\mathbb Z_3,\mathbb Z_4,\mathbb Z_2\times\mathbb Z_2\);
- three-link cycles, plus a four-link \(\mathbb Z_2\) cycle;
- all coefficient vectors in \(\{-2,-1,0,1,2\}^n\);
- all proper simple paths;
- closed windings from \(-3\) through \(3\);
- exact dual-character separation;
- two-link witness minimality;
- every fibre cardinality; and
- necessity and sufficiency of the universal repair dimension.

It returns `14/14`. The theorem is proved algebraically; enumeration is only a
bounded regression and has no independent scientific grade.

## 11. Reopeners

1. Determine whether a dynamics, state family, or observer action class
   physically selects the Wilson quotient rather than supplying it.
2. Test whether any target-independent coarser record than full link access
   reconstructs a physically natural intermediate path family.
3. Generalize the factorization boundary to arbitrary finite graphs, where
   cycle-space and path-space quotients may replace the one-cycle criterion.
4. Determine the exact information/disturbance/resource tradeoff between the
   QND loop record and finer open-line access.
5. Ask whether an analogous conditional expectation and first-leak theorem
   survives in a continuum local-algebraic gauge theory.

No successor is selected automatically. Each reopener needs its own absorber,
physical-interface, and no-refit audit.
