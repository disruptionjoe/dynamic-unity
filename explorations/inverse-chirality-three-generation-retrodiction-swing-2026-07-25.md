---
title: "Inverse chirality and three-generation retrodiction swing"
status: active_research
doc_type: conditional_inverse_problem_and_scoped_no_go
created: 2026-07-25
run_id: RUN-20260725-235834-inverse-chirality-generation
parent_run: RUN-20260725-234255-triplet-boundary-flavor-integrated-swing
lanes: [2, 3, 4, 6, 7, A]
channels: [CH-SYN, CH-FORMAL, CH-MODEL, CH-COLLIDE, CH-FRONTIER]
claim_grade: "CONDITIONALLY ENTAILED / EXACT FINITE AND ALGEBRAIC CONTROLS / KNOWN-MATHEMATICS SYNTHESIS / PHYSICAL SOURCE OPEN"
owner_boundary: "Dynamic Unity owns the inverse-identification contract; gu-formalization owns the actual GU carrier, source action, operator/domain, anomaly completion, chirality, flavor and generation verdict"
---

# Inverse chirality and three-generation retrodiction

## Outcome

Working backward from the strongest conditional target is useful, but it does
not derive three. It locates where an exact-three explanation would have to
live.

Assume:

> The three observed matter generations form the protected chiral low-energy
> kernel of one source-derived physical operator, with a consistent local and
> global anomaly/mirror completion and source-derived restricted flavor
> breaking that yields nondegenerate masses, nontrivial mixing and a nonzero
> rephasing-invariant CP witness.

The exact inverse tournament returns:

```text
ordinary Standard Model anomalies
    -> constrain one-family content
    -> do not select the family count

ordinary CKM-like CP violation
    -> requires at least three generations
    -> does not exclude more than three

three accessible chiral families
    -> do not identify the global index or hidden completion

nonzero flavor CP invariant
    -> requires a noncommutative projected flavor algebra
    -> rejects full triplet equivariance and one common cyclic algebra
```

Therefore exact three remains source-sensitive. It must enter through an
independently derived count-sensitive operator, topology, family structure or
held-out flavor relation—not through ordinary anomaly cancellation, chirality
alone, CP existence alone, or low-energy access alone.

This is a constraint map and a no-go synthesis, not a physical GU operator or
generation derivation.

## Exact result 1 — anomaly replication is count-blind

Write one Standard Model family entirely as left-handed Weyl fields:

| field | representation role | hypercharge | multiplicity |
|---|---|---:|---:|
| \(Q_L\) | color triplet, weak doublet | \(1/6\) | 6 |
| \(u_R^c\) | color antitriplet | \(-2/3\) | 3 |
| \(d_R^c\) | color antitriplet | \(1/3\) | 3 |
| \(L_L\) | weak doublet | \(-1/2\) | 2 |
| \(e_R^c\) | singlet | \(1\) | 1 |

Adding a hypercharge-zero sterile \(\nu_R^c\) does not change these sums.

With common positive Dynkin-index normalizations suppressed, the exact
one-family anomaly vector is:

\[
\begin{aligned}
\mathcal A_{SU(3)^3} &= 2-1-1=0,\\
\mathcal A_{SU(3)^2U(1)}
  &=2(1/6)-2/3+1/3=0,\\
\mathcal A_{SU(2)^2U(1)}
  &=3(1/6)-1/2=0,\\
\mathcal A_{U(1)^3}
  &=6(1/6)^3+3(-2/3)^3+3(1/3)^3
    +2(-1/2)^3+1=0,\\
\mathcal A_{\mathrm{grav}^2U(1)}
  &=6(1/6)+3(-2/3)+3(1/3)+2(-1/2)+1=0.
\end{aligned}
\]

There are four weak doublets per family after color is counted, so the tested
Witten \(SU(2)\) parity is also even.

### Lemma — anomaly replication

For any additive anomaly functional \(\mathcal A\), if a complete family
\(F\) satisfies \(\mathcal A(F)=0\), then

\[
\mathcal A(F^{\oplus N})=N\mathcal A(F)=0
\]

for every positive integer \(N\). In this family,
\(4N=0\pmod 2\) also passes the global \(SU(2)\) parity condition for every
\(N\).

The exact probe checks \(N=1,\ldots,6\); every value passes all tested
constraints. This finite sweep illustrates the general additive lemma.

**Consequence.** Ordinary Standard Model anomaly cancellation constrains the
contents and charges of a complete family. Once one family cancels, it cannot
explain why the multiplicity is three.

Any anomaly-based exact-three route must therefore introduce an independently
derived nonfactorizing structure—such as a horizontal/discrete family
symmetry, a mixed family anomaly or a global cobordism condition—and then pass
its own complete anomaly audit. Merely postulating such a symmetry would move
the inserted three rather than derive it.

## Exact result 2 — CP supplies a lower bound, not an exact count

For \(N\) ordinary unitary quark generations, the mixing matrix has

\[
\frac{N(N-1)}{2}
\]

physical angles and

\[
\frac{(N-1)(N-2)}{2}
\]

irreducible Dirac CP phases.

Thus:

| generations | angles | Dirac CP phases |
|---:|---:|---:|
| 1 | 0 | 0 |
| 2 | 1 | 0 |
| 3 | 3 | 1 |
| 4 | 6 | 3 |

Under those assumptions, nonzero CKM-like CP violation excludes one and two
generations. It does not exclude four or more.

The positive control constructs a unitary three-family mixing matrix with:

```text
unitarity residual       2.52e-16
Jarlskog invariant       3.013e-05
|det[H_u,H_d]|           1.471e11
```

The precise values are inputs used only to verify that the discriminator can
fire. The theorem-level content is the parameter count and the nonzero
rephasing-invariant/commutator condition.

**Consequence.** CP offers a meaningful explanation of why three is the
minimum family dimension capable of ordinary irreducible quark CP violation.
It does not explain why nature stops at three.

This creates a useful conditional target:

> Find a source structure for which three is simultaneously the first
> CP-capable family dimension and the maximum admissible or dynamically
> accessible one.

The second half is the missing count-sensitive result.

## Exact result 3 — accessible chirality does not identify global chirality

Freeze the accessible low-energy endpoint to:

\[
(n_L^{\mathrm{access}},n_R^{\mathrm{access}})=(3,0).
\]

For any integer \(I\), choose

\[
n_R=\max(0,3-I),\qquad n_L=n_R+I.
\]

Then \(n_L\ge 3\), the three left modes can be exposed by the declared access
map, and the global index is

\[
n_L-n_R=I.
\]

The finite probe checks every \(I\in[-5,5]\). All eleven completions have the
same accessible endpoint.

Even after global index three is independently supplied, the family

\[
(n_L,n_R)=(3+k,k),\qquad k\ge0
\]

contains arbitrarily many hidden mirror pairs with the same net index.

### Scoped nonidentification theorem

> In the broad finite hidden-mode completion class, three accessible
> left-chiral modes and no accessible right-chiral modes identify neither the
> global index nor the total mirror-pair content.

This does not assert that every combinatorial completion is a local, unitary,
gauge-consistent QFT. It proves that the endpoint record alone cannot supply
those physical premises.

The missing discriminators are:

- complete boundary/energy expansion;
- partner and threshold searches;
- source/operator provenance;
- topological response under a physically permitted deformation;
- anomaly inflow and global consistency;
- and the mechanism that makes hidden sectors heavy or inaccessible.

## Exact result 4 — CP constrains the flavor algebra

For nondegenerate quark mass-squared operators \(H_u,H_d\), a nonzero
Jarlskog/commutator CP witness requires that the projected flavor operators
do not commute.

The parent swing already established that:

1. complete irreducible triplet equivariance leaves only scalar
   endomorphisms; and
2. two normal operators built only from one common order-three action commute
   and share an eigenbasis.

The inverse probe reruns the second obstruction as a null: the common cyclic
algebra has exactly zero commutator, while the three-family CP positive control
has nonzero Jarlskog and commutator determinant.

**Consequence.** If the conditional target is true, the physical source must
project at least two differently oriented, noncommuting flavor structures—or
an equivalent noncommutative algebra—onto the three chiral modes. “There is a
triplet” and “there is a \(Z/3\) action” are insufficient.

This is a necessary condition, not a flavor model. Generic noncommuting
Yukawa matrices can fit the data and explain nothing.

## Candidate-preimage tournament

| candidate preimage | same accessible endpoint? | global index | where three enters | first decisive discriminator |
|---|---:|---:|---|---|
| direct global index three | yes | 3 | physical pairing, if derived | topological response plus anomaly/inflow |
| unit index times triplet | yes | 3 | carrier multiplicity | operator factorization and triplet provenance |
| vectorlike completion/access three | yes | 0 | access boundary | boundary expansion, partners and running |
| index three plus hidden mirror pairs | yes | 3 | net imbalance | complete mirror census and mass mechanism |
| target-coded defect/rectangularity | yes | 3 | selected input | independent derivation of count-setting datum |
| three copied families | yes | undefined | matter inventory | source-owned count-changing counterfactual |

No row currently satisfies the complete conditional packet. The physical GU
source operator/domain is still undefined.

## Count-sensitive successor channels

The backward pass changes the search order:

### 1. Actual source-derived index pairing

Highest direct value. Construct the GU operator/domain before choosing the
index result. It must return zero, nonthree, target-coded-three or
independently derived three without reinterpretation.

### 2. Nonfactorizing family consistency

Search only structures already motivated by the source for a horizontal or
discrete family symmetry, mixed anomaly, global obstruction or cobordism
condition that does not vanish independently within each family. Do not add a
family symmetry solely because its anomaly equations return three.

### 3. Projected flavor algebra

Compute the centralizer and generated algebra of the actual source terms after
zero-mode projection. A viable target must be noncommutative, economical, and
capable of producing at least one held-out mass, mixing, CP, running or
partner relation.

### 4. Completion-sensitive access tests

For an effective-three route, freeze the boundary, energy and resource frame,
then predict where mirror/vectorlike partners, nonunitarity, threshold running
or rare transitions should appear. Absence of a pinned scale or coupling
leaves this exploratory.

## Literature collision

The ingredients are established terrain:

- Kobayashi and Maskawa identified the multi-family structure required for
  irreducible weak CP violation:
  [CP-Violation in the Renormalizable Theory of Weak Interaction](https://doi.org/10.1143/PTP.49.652).
- Jarlskog supplied the basis-independent mass-commutator invariant:
  [Commutator of the Quark Mass Matrices](https://doi.org/10.1103/PhysRevLett.55.1039).
- Witten's global \(SU(2)\) anomaly excludes an odd number of left-handed
  doublets:
  [An SU(2) Anomaly](https://doi.org/10.1016/0370-2693(82)90728-6).
- Nielsen and Ninomiya delimit ordinary lattice realizations of chiral
  fermions:
  [A No-Go Theorem for Regularizing Chiral Fermions](https://doi.org/10.1016/0370-2693(81)91026-1).
- Kaplan demonstrates chiral defect-localized zero modes and anomaly flow:
  [A Method for Simulating Chiral Fermions on the Lattice](https://arxiv.org/abs/hep-lat/9206013).
- Lüscher shows how anomaly-free chiral multiplets can be treated with exact
  lattice gauge invariance under the stated conditions:
  [Abelian Chiral Gauge Theories on the Lattice](https://arxiv.org/abs/hep-lat/9811032).
- Three defect-localized generations and overlap-generated hierarchy have
  explicit prior constructions:
  [Frère, Libanov and Troitsky](https://arxiv.org/abs/hep-ph/0012306).

The anomaly lemma, CKM parameter count, Jarlskog obstruction, index arithmetic
and boundary-localization ingredients are not claimed as new. Possible DU
value lies in the typed inverse-identification contract and in any future
source-derived operator that connects multiplicity, chirality, completion and
predictive flavor without importing the target.

## Executable receipt

The deterministic probe
[`tests/du_inverse_chirality_generation_tournament_probe.py`](../tests/du_inverse_chirality_generation_tournament_probe.py)
passes `27/27`. Its artifact is
[`tests/artifacts/du_inverse_chirality_generation_tournament_result.json`](../tests/artifacts/du_inverse_chirality_generation_tournament_result.json).

Its integrated return is:

```text
CONDITIONAL_TARGET_CONSTRAINS
ANOMALIES_COUNT_BLIND
CP_LOWER_BOUND_NOT_EXACT_COUNT
UV_CAUSE_NONIDENTIFIED
PHYSICAL_SOURCE_OPERATOR_OPEN
```

## Revised research question

The useful question is no longer merely:

> Can the GU triplet be made chiral?

It is:

> Does one independently derived GU source operator simultaneously supply a
> consistent chiral completion, distinguish global index from accessible
> rank, make three the exact count rather than merely the first CP-capable
> count, and restrict the noncommutative flavor algebra enough to predict a
> held-out relation?

That question can return `ZERO`, `NONTHREE`, `EFFECTIVE_THREE`,
`TARGET_CODED_THREE`, `THREE_WITHOUT_FLAVOR`, or
`PREDICTIVE_UNIFIED_OPERATOR`.

## Status consequence

- The conditional assumption is retained as an inverse-search instrument, not
  evidence.
- `HC-DU-040A` gains an inverse retrodiction stage and count-sensitive search
  order.
- `CONCEPT-DU-012` gains anomaly-blindness, CP-lower-bound and completion
  nonidentification controls.
- `CPRED-02` remains retired; this swing supplies no replacement prediction.
- The actual source operator remains undefined and GU's generation verdict
  remains `OPEN / located-not-forced`.
- No law, physical theorem, generation claim, ontology, new physics, paper,
  Factory state, submission, publication or external action is promoted.
