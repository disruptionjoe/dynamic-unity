# Homomorphic cycle-record formation, matroid resource, regional correlation, and the direct-action boundary

**Date:** 2026-07-29
**Run:** `RUN-20260729-135040-cycle-record-formation-direct-action`
**Claim:** `HC-DU-125`
**Status:** **BANKED — SCOPED GRADE 4 EXACT FINITE-ABELIAN HOMOMORPHIC-RECORD FORMATION / CUTWISE RESOURCE NECESSITY AND SUFFICIENCY / REGIONAL-CORRELATION GLUING / FIELD–DIRECT-ACTION DESCENT BOUNDARY / STANDARD FINITE-GROUP, STABILIZER, MATROID, AND SCHUR-COMPLEMENT MATHEMATICS / NO ONTOLOGY SELECTION, PUBLIC FINALITY, COMPLETE COST LAW, CONTINUUM TRANSFER, OR EMPIRICAL EXCESS**

## Plain-English result

There are two substantive results and one important warning.

First, the regional loop records from `HC-DU-121`--`124` can all be formed
by one unchanged distributed quantum instrument. The instrument does not
measure each desired loop separately. It prepares one correlated mask drawn
uniformly from the kernel of the complete record map, lets every station add
its local physical value to its share, and reads the shares locally.

The joined readout reveals exactly the desired complete cycle record and
nothing finer. Every region's readout marginal reveals exactly that region's
local cycle record. When two locally complete regions still miss a
cross-region loop fact, that fact is not stored at either endpoint: it lives
in the correlation between the two masked transcripts. Preserving their
joined lineage recovers it. Discarding that association destroys it.

Second, the pre-shared entanglement needed across any declared station cut is
exact:

\[
E_{\min}^{S:\bar S}
=
\lambda_\Gamma(S)\log_2|G|,
\]

where

\[
\lambda_\Gamma(S)
=
|V|-c(S)-c(\bar S)+1
\]

is the connectivity function of the graph's cycle matroid. A tree costs zero
on every cut. A multiply connected graph can require several independent
group units. This is neither the endpoint min-cut from `HC-DU-123` nor the
overlap-component count from `HC-DU-124`.

Third, direct-action theory changes which object can carry the record. Exact
elimination of an explicit mediator preserves the complete source response,
but it does not preserve the mediator's graph topology. A three-arm star and
a direct triangle have exactly the same boundary/source action while their
cycle ranks are zero and one. Therefore a loop record defined on an explicit
field or mediator network is not automatically a record of the reduced
direct action.

This does **not** make direct action mathematically deficient. It says that a
direct-action theory must define its native record on source relations,
responses, or another invariant of the reduced action. It cannot silently
inherit a field-cycle record whose identity disappeared during elimination.

## Why this matters to Dynamic Unity

`HC-DU-124` ended with a precise but still formal question:

> Can the complete local records and the missing cross-region records be
> physically formed under one unchanged causal and resource contract?

That question is now answered positively in the finite-Abelian
regular-matter arena.

The direct-action question is different:

> Is this record a property of the source physics itself, or only of one
> explicit-field presentation of that physics?

That question is answered negatively for mediator-cycle topology. Source
equivalence preserves source queries, not every internal decomposition.

The combination is useful because it prevents two opposite errors:

1. declaring the regional record merely formal because no common instrument
   was given; and
2. declaring it ontology-independent merely because a field and a
   direct-action presentation agree on source behavior.

## Frozen arena

Let

\[
D=\prod_{e=1}^{n}G_e
\]

be a finite product of local finite-Abelian data groups, let \(H\) be a
finite Abelian group, and let

\[
Q:D\longrightarrow H
\]

be a fixed homomorphism. Write

\[
K=\ker Q.
\]

One data register and one ancillary share are assigned to each station. The
group, target homomorphism, station factorization, local controlled-add
couplings, pre-shared ancillary state, readout basis, transcript lineage,
and later aggregation are supplied.

For the graph specialization:

1. \(\Gamma=(V,E)\) is a finite connected graph;
2. every edge carries one physical gauge-invariant dressed value in the
   finite Abelian group \(G\), as constructed in `HC-DU-121`;
3. \(Q_\Gamma\) is any complete independent cycle map; and
4. its kernel is the physical coboundary subgroup
   \(\operatorname{im}d\).

No graph, matter field, record interface, observer, source ontology, or
action class is selected by the theorem.

## Theorem 1 — the uniform-kernel instrument

Prepare the ancillary state

\[
|\Omega_K\rangle
=
\frac{1}{\sqrt{|K|}}
\sum_{k\in K}|k\rangle.
\]

At station \(e\), apply only

\[
|y_e\rangle|k_e\rangle
\longmapsto
|y_e\rangle|k_e+y_e\rangle
\]

and then measure the ancillary share in the group basis. Let
\(z\in D\) be the joined raw transcript.

Then

\[
\Pr(z\mid y)
=
\begin{cases}
|K|^{-1},&Q(z)=Q(y),\\
0,&Q(z)\neq Q(y).
\end{cases}
\]

The raw-result Kraus operator is

\[
M_z
=
|K|^{-1/2}P_{Q(z)},
\]

where \(P_q\) projects onto the data subspace with record value \(q\).
Coarse-graining the \(|K|\) raw values with the same \(q\) gives

\[
\rho\longmapsto P_q\rho P_q.
\]

Thus the protocol implements the exact selective Lüders instrument for
\(Q\). The raw mask is random, but it neither distinguishes nor dephases
states within one \(Q\)-fibre.

### Proof

For basis input \(y\), the ancillary support after controlled addition is

\[
y+K.
\]

Therefore \(z\) occurs exactly when \(z-y\in K\), equivalently
\(Q(z)=Q(y)\), and every supported result has amplitude
\(|K|^{-1/2}\). Acting on a superposition makes the corresponding diagonal
operator exactly \(|K|^{-1/2}P_{Q(z)}\). Summing the \(|K|\) identical
selective branches inside one coarse-grained result gives the Lüders
instrument. \(\square\)

## Theorem 2 — each local transcript is an exact quotient

For a set \(S\) of stations, let

\[
\pi_S:D\longrightarrow D_S
\]

be coordinate projection. Its raw transcript marginal is uniform on

\[
y_S+\pi_S(K).
\]

It therefore reveals exactly the quotient

\[
D_S/\pi_S(K).
\]

In the complete graph-cycle specialization,

\[
K=\operatorname{im}d.
\]

For a connected subgraph \(A\),

\[
\pi_A(\operatorname{im}d)
=
\operatorname{im}d_A.
\]

Consequently, the transcript visible inside \(A\) depends exactly on the
local cycle class

\[
[y|_A]\in H^1(A;G),
\]

not on a finer local edge assignment or on a cross-region cycle value.

This is an exact local-information statement. It is not authentication,
provenance, public access, or finality.

## Theorem 3 — exact cutwise entanglement cost

Split the stations into \(S\) and \(\bar S\), and write

\[
Q(y)=Q_S(y_S)+Q_{\bar S}(y_{\bar S}).
\]

Define the shared-syndrome subgroup

\[
I_S
=
\operatorname{im}Q_S
\cap
\operatorname{im}Q_{\bar S}.
\]

Then the uniform-kernel state has a flat Schmidt spectrum of rank
\(|I_S|\) across \(S:\bar S\). Hence

\[
S\!\left(\Omega_K^S\right)
=
\log_2|I_S|.
\]

Moreover, every exact LOCC implementation of the selective \(Q\)-measurement
requires at least this much pre-shared entanglement across that cut, and
\(|\Omega_K\rangle\) attains the bound.

### Schmidt decomposition

An element \((k_S,k_{\bar S})\) belongs to \(K\) exactly when

\[
Q_S(k_S)=-Q_{\bar S}(k_{\bar S}).
\]

Partition the uniform sum by the common syndrome
\(i\in I_S\). Distinct syndrome sectors have orthogonal support on both
sides. Every sector has the same cardinality, giving \(|I_S|\) equal Schmidt
coefficients.

### Necessity

Apply the target instrument to the product state that is uniform over every
local data register. Conditional on any record value \(q\), the output is a
uniform affine translate of \(K\), so it has the same cut entanglement
\(\log_2|I_S|\). Every outcome branch has that value. LOCC cannot increase
the average pure-state entanglement across the cut, so the initial shared
resource must contain at least \(\log_2|I_S|\) ebits across it.

The one state \(|\Omega_K\rangle\) realizes the protocol and has equality on
every cut simultaneously. This is cutwise optimality, not uniqueness or a
complete classification of multipartite resources. Stabilizer-state
entanglement rank is standard terrain; see
[Fattal et al.](https://arxiv.org/abs/quant-ph/0406168).

## Theorem 4 — graphic-matroid resource law

For a connected graph and edge subset \(S\), let \(c(S)\) be the number of
connected components of the spanning subgraph \((V,S)\), including isolated
vertices. Set

\[
\lambda_\Gamma(S)
=
|V|-c(S)-c(E\setminus S)+1.
\]

For the complete cycle record,

\[
|I_S|
=
|G|^{\lambda_\Gamma(S)}.
\]

Therefore

\[
\boxed{
E_{\min}^{S:\bar S}
=
\lambda_\Gamma(S)\log_2|G|
}.
\]

### Proof

The complete cycle map has kernel \(\operatorname{im}d\). The image of an
edge subset under the cycle quotient has size determined by the graphic
matroid rank

\[
r(S)=|V|-c(S).
\]

The shared-syndrome exponent is

\[
r(S)+r(\bar S)-r(E)
=
(|V|-c(S))+(|V|-c(\bar S))-(|V|-1),
\]

which is exactly \(\lambda_\Gamma(S)\). The finite-Abelian incidence map has
the corresponding group cardinality
\(|G|^{\lambda_\Gamma(S)}\). \(\square\)

Three superficially similar numbers are now separated:

| Quantity | What it controls |
|---|---|
| endpoint min-cut from `HC-DU-123` | minimum support of a same-cycle-record/different-open-path witness |
| \(k-1\) from `HC-DU-124` | number of cross-region cycle coordinates missed by two complete local cycle records |
| \(\lambda_\Gamma(S)\) here | entanglement needed to form the complete cycle record across one station cut |

None is automatically a communication cost, Byzantine threshold, consensus
quorum, latency, energy, or thermodynamic law.

## Theorem 5 — the missing regional fact lives in correlations

Let \(\Gamma=A\cup B\) be the two-region cover from `HC-DU-124`, with
\(A\cap B\) having \(k\) connected components.

Under the uniform-coboundary instrument:

1. \(A\)'s transcript marginal depends exactly on \([y|_A]\);
2. \(B\)'s transcript marginal depends exactly on \([y|_B]\);
3. the \(|G|^{k-1}\) global cycle classes sharing those local records have
   identical \(A\) and \(B\) marginals; and
4. their joined transcript supports are disjoint.

Therefore the \(k-1\) cross-region coordinates are encoded in transcript
correlations, not in either local transcript by itself.

```text
A marginal = complete A-cycle record
B marginal = complete B-cycle record
joined transcript with lineage = complete global cycle record
local record values without the join = cross-region sector erased
```

This gives an exact physical implementation of the gluing repair from
`HC-DU-124` without running a second target-coded measurement. It does not
make the joined data public or trustworthy. Formation, association,
retention, authentication, access, rival class, and verification remain
separate.

## Theorem 6 — source equivalence does not preserve mediator-cycle records

The direct-action issue can be stated as a descent condition.

Let

\[
\pi:\mathcal F\longrightarrow\mathcal S
\]

map an explicit field/mediator completion to its complete reduced source
action. A field record \(R_F\) defines a source-action record exactly when it
is constant on every fibre of \(\pi\):

\[
\pi(f_1)=\pi(f_2)
\quad\Longrightarrow\quad
R_F(f_1)=R_F(f_2).
\]

Mediator-cycle topology fails this test.

### Exact star–triangle witness

Take three boundary/source coordinates \(x_1,x_2,x_3\). The star model has
one internal mediator \(x_0\) and action

\[
S_Y
=
\frac12\sum_{i=1}^{3}3(x_i-x_0)^2.
\]

Stationarity gives

\[
x_0=\frac{x_1+x_2+x_3}{3}.
\]

Eliminating \(x_0\) yields

\[
S_{Y,\mathrm{eff}}
=
\frac12x^\mathsf T
\begin{pmatrix}
2&-1&-1\\
-1&2&-1\\
-1&-1&2
\end{pmatrix}
x.
\]

The direct triangle with unit pairwise conductances has

\[
S_\Delta
=
\frac12\sum_{i<j}(x_i-x_j)^2,
\]

which is exactly the same quadratic form for every source assignment.

Yet the star has

\[
\beta_1(Y)=0,
\]

while the triangle has

\[
\beta_1(\Delta)=1.
\]

Thus the complete reduced source kernel does not determine the cycle rank of
an interaction completion. This is the standard Schur-complement and
electrical-network equivalence behind star--triangle reduction; see
[Beard et al.](https://arxiv.org/abs/2210.05761) and
[Paal and Umbleja](https://arxiv.org/abs/1504.01269).

### What descends and what does not

| Object | Status under exact mediator elimination |
|---|---|
| complete source response encoded by the reduced action | preserved |
| every query that factors through that source response | preserved |
| internal mediator dimension or factorization | not preserved automatically |
| mediator-local algebra, stress partition, or cycle topology | not preserved automatically |
| the field-cycle record and its station resource law | not preserved automatically |
| a newly defined record on direct source relations | conditionally buildable after retyping |

This is compatible with the original Wheeler--Feynman project of formulating
electrodynamics through direct interparticle action
([1949 paper record](https://cds.cern.ch/record/1062647?ln=en)). It neither
selects direct action nor rules out fields.

The witness is classical and fixed-background. Full quantum equivalence also
requires the determinant, measure, state, boundary conditions, regulator,
gauge quotient, background dependence, and allowed counterterms identified
in `HC-DU-116`.

## What direct action genuinely contributes

The user's intuition is correct in the following precise sense:

> Direct action makes pairwise source relations candidates for the primitive
> physical object, so it forces Dynamic Unity to distinguish a record of
> relational source response from a record of an independently represented
> field.

That is a valuable structural fork.

A direct-action-native finite relation graph can instantiate Theorems 1--5
if it supplies:

1. physical local relation variables;
2. a tensor or commuting action factorization that makes the station
   couplings meaningful;
3. a homomorphic target \(Q\);
4. a realizable shared resource and local interaction;
5. retained transcript lineage; and
6. an observer/access contract.

Once supplied, the same homomorphic mathematics applies. But that is a new
relational record construction. It is not proof that the eliminated field's
Wilson loop was secretly the same record.

The next genuinely discriminating direct-action question is therefore not
“Can direct action be represented mathematically?” It can. It is:

> Does a physical direct-action law select a source-relation record,
> formation instrument, and access boundary that remain invariant across
> all source-equivalent factorizations, or are those interfaces still
> supplied?

## Exact computation

The deterministic local probe checks:

- three general homomorphic specimens over
  \(\mathbb Z_3\), \(\mathbb Z_2\), and
  \(\mathbb Z_2\times\mathbb Z_2\);
- every nontrivial cut of four graph specimens, including a tree, a product-
  group triangle, bridged cycles, and \(K_4\);
- spanning-tree/cycle-basis invariance;
- three two-region covers with connected and disconnected overlaps;
- equality of every local marginal and separation by joined correlations;
  and
- the exact rational star--triangle Schur complement.

It returns `24/24`.

The script is a finite exact regression of the analytic proof. It does not
simulate gauge dynamics, direct-action QED, an absorber, a continuum field,
or a physical detector.

## Absorbers and novelty disposition

The component mathematics is mature:

- finite-Abelian quotient and Fourier/stabilizer measurement;
- entanglement rank of subgroup and stabilizer states;
- graph cycle/cut spaces and matroid connectivity;
- Abelian Wilson-loop measurement with pre-shared entanglement, as in
  [Beckman et al.](https://arxiv.org/abs/hep-th/0110205);
- Mayer--Vietoris gluing; and
- Schur complements and star--triangle equivalence.

The Dynamic Unity increment is their typed composition:

```text
one physical homomorphic instrument
  -> exact local record quotients
  -> global glue stored only in correlations
  -> exact cutwise formation resource
  -> explicit failure of field-cycle descent to source-only direct action.
```

That composition is scientifically useful and exact in its arena. It is not
yet empirical excess or a new fundamental law.

## North-Star disposition

This is real progress toward the finite-remainder North Star:

- the record is now physically formed rather than merely defined;
- local and global record content are distinguished exactly;
- the missing gluing fact has a physical carrier in joined correlations;
- the formation resource is exact and topology-sensitive;
- closed responses reconstruct from the complete formed cycle record;
- open-path physical remainders remain finite and action-relative; and
- field versus direct-action representation is now an explicit descent test.

The remaining highest-level gaps are unchanged:

1. the physical theory still does not select the graph, matter completion,
   homomorphic record, station factorization, resource, or access interface;
2. no fault/adversary model or public-finality rule has been added;
3. no source-action-native record has yet been selected;
4. no non-Abelian, continuous, AQFT, or continuum transfer is proved; and
5. no empirical delta over standard physics is produced.

`NO_READY_SUCCESSOR` remains the honest disposition.

## Reopeners

1. Define the strongest source-action-native record invariant under
   mediator elimination, star--triangle moves, and other
   response-preserving transformations.
2. Determine whether a physically motivated direct-action law selects that
   record and its factorization or merely admits many of them.
3. Extend the subgroup-state resource theorem to non-Abelian or
   operator-algebraic records, where ordinary quotient fibres no longer
   suffice.
4. Add a declared fault, authentication, and access model to test when
   correlation-carried glue becomes regional public finality.
5. Seek a local-QFT or direct-action specimen in which the same unchanged
   instrument and target transfer without finite-model refitting.

## Non-promotions

`HC-DU-125` does not select fields, direct action, Wheeler--Feynman absorber
theory, RTI, one ontology, a graph, relation complex, gauge group, matter
sector, homomorphic target, regional cover, station factorization, local
coupling, resource preparation, transcript association, observer, access
boundary, verification rule, fault class, or finalizer.

It does not prove a complete energy, entropy, latency, bandwidth,
communication, cryptographic, consensus, BFT, or thermodynamic law. It does
not transfer to pure gauge theory, non-Abelian or continuous groups, AQFT,
continuum QFT, gravity, arbitrary direct-action theories, or unrestricted
regional networks. It produces no empirical excess, new-physics prediction,
paper activation, hardware path, provider action, publication, submission,
contact, or sibling-repository mutation.
