---
title: "Positive-functional QFT reconstruction, algebra antecedents, and the finite-record boundary"
status: completed_scoped_result
doc_type: reconstruction_import_exact_counterexamples_and_transfer_boundary
created: 2026-07-29
hypothesis_id: HC-DU-128
run_id: RUN-20260729-152601-positive-functional-qft-reconstruction
authority: "Joe direct chat: Go"
lanes:
  - lane_1
  - lane_2
  - lane_3
  - lane_6
  - lane_7
channels:
  - CH-FORMAL
  - CH-MODEL
  - CH-COLLIDE
  - CH-SYN
warrants:
  - DERIVED
  - CONSTRUCTIVELY_REALIZED
maximum_grade: "Scoped Grade 4 exact positivity, algebra-antecedent, and finite-hierarchy necessity boundary plus conditional Grade 3 import of GNS/Wightman/Osterwalder-Schrader reconstruction; no selected QFT, physical record interface, finite acquisition theorem, GU transfer, empirical excess, ontology priority, new law, new physics, or prediction"
probe: "../tests/du_positive_functional_qft_reconstruction_probe.py"
artifact: "../tests/artifacts/du_positive_functional_qft_reconstruction_result.json"
---

# Positive-functional QFT reconstruction

## Executive result

The swing returned:

```text
FIXED STAR ALGEBRA + FULL POSITIVE FUNCTIONAL
  -> CYCLIC HILBERT REPRESENTATION, PAIRING, NULL QUOTIENT AND DOMAIN

BUT

FUNCTIONAL VALUES + TWO-POINT PAIRING
  -/> ALGEBRA PRODUCT, INVOLUTION, SOURCE/TEST SPACE OR SPACETIME

EVERY FIXED FINITE CORRELATION ORDER
  -/> UNRESTRICTED FULL FUNCTIONAL

THEORETICAL FULL FUNCTIONAL
  != PHYSICALLY FORMED FINITE RECORD

WIGHTMAN / OSTERWALDER-SCHRADER
  = REAL CONDITIONAL QFT RECONSTRUCTION POSITIVE

ORDINARY POSITIVITY
  -/> GU OR AN INDEFINITE-METRIC QFT WITHOUT EXTRA STRUCTURE

NO READY SUCCESSOR
```

This is the first serious physical-theory transfer after `HC-DU-127`, and it
returns a genuine positive:

> Once the observable star algebra and a complete positive state functional
> are fixed, the functional constructs its own Hilbert pairing, null quotient,
> cyclic representation, vacuum vector, and common algebraic domain.

In relativistic QFT, Wightman reconstruction strengthens this. A complete
positive hierarchy satisfying the Wightman axioms reconstructs the
corresponding field theory up to the theorem's unitary equivalence.
Osterwalder--Schrader reconstruction supplies the Euclidean route: suitable
Schwinger functions, with reflection positivity and the remaining OS
conditions, reconstruct Lorentzian Wightman/Hamiltonian data.

This conditionally discharges the **Hilbert pairing and representation-domain**
part of the `HC-DU-127` reopener. It does not discharge the **algebra,
spacetime, state, source, or physical-record-interface** parts. Those are
antecedents of the reconstruction theorem.

The result identifies a much cleaner North-Star seam:

> A complete QFT functional can hold a complete observer-algebraic
> description of the physics, but no known theorem here says that a bounded
> observer physically forms or accesses that infinite functional.

## 1. The exact reconstruction object

Let \(\mathcal A\) be a fixed unital star algebra and let

\[
\omega:\mathcal A\longrightarrow\mathbb C
\]

be normalized and positive:

\[
\omega(1)=1,
\qquad
\omega(a^*a)\geq0.
\tag{1}
\]

Define the null space

\[
\mathcal N_\omega
=
\{a\in\mathcal A:\omega(a^*a)=0\}.
\tag{2}
\]

Positivity and Cauchy--Schwarz make \(\mathcal N_\omega\) a left ideal in the
standard GNS setting. The quotient carries

\[
\langle[a],[b]\rangle_\omega
=
\omega(a^*b).
\tag{3}
\]

Completing the quotient gives a Hilbert space
\(\mathcal H_\omega\). Left multiplication gives

\[
\pi_\omega(a)[b]=[ab],
\tag{4}
\]

and

\[
\Omega_\omega=[1]
\tag{5}
\]

is cyclic:

\[
\overline{\pi_\omega(\mathcal A)\Omega_\omega}
=
\mathcal H_\omega.
\tag{6}
\]

The state is recovered as

\[
\omega(a)
=
\langle\Omega_\omega,
\pi_\omega(a)\Omega_\omega\rangle.
\tag{7}
\]

The cyclic representation is unique up to the standard unitary equivalence.
For an unbounded field algebra, the invariant algebraic span

\[
\mathcal D_\omega
=
\pi_\omega(\mathcal A)\Omega_\omega
\tag{8}
\]

is the initial common domain; closures, extensions, localization, and gauge or
indefinite-metric conditions can require more.

### Theorem 1 — complete functional reconstruction

On a fixed \(\mathcal A\), equality of complete functionals,

\[
\omega_1(a)=\omega_2(a)
\quad
\text{for every }a\in\mathcal A,
\tag{9}
\]

is sufficient for equality of every algebra-observable expectation and gives
unitarily equivalent cyclic GNS packets.

Conversely, any record equivalence that reconstructs every
\(\omega(a)\) must refine equality of \(\omega\): if
\(\omega_1\neq\omega_2\), linear-functional inequality supplies one
\(a_\star\in\mathcal A\) with

\[
\omega_1(a_\star)\neq\omega_2(a_\star).
\tag{10}
\]

Thus the full positive functional is the minimal complete state-response
record, up to information-equivalent encoding, for **all queries in the fixed
algebra**.

“Record” in this theorem is an information quotient. It is not yet a
physically formed archive.

## 2. What Wightman and OS reconstruction really add

For smeared fields, the hierarchy

\[
W_n(f_1,\ldots,f_n)
=
\omega\!\left(
\phi(f_1)\cdots\phi(f_n)
\right)
\tag{11}
\]

is one representation of the complete functional on a Borchers--Uhlmann-type
field algebra.

The Wightman reconstruction theorem uses the complete hierarchy plus its
positivity, covariance, spectrum, locality, hermiticity, and regularity
structure to reconstruct the Hilbert space, cyclic vacuum, fields on a common
domain, and Poincaré representation up to the declared equivalence. Work on
generalized Wightman functionals makes the algebra input explicit:
[Ritter](https://arxiv.org/abs/math-ph/0404027) extends the construction to
fields valued in a topological star algebra precisely because the original
theorem does not automatically cover an arbitrary gauge or noncommutative
target algebra.

The Euclidean route is equally substantive. Osterwalder and Schrader's
[1973 paper](https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-31/issue-2/Axioms-for-Euclidean-Greens-functions/cmp/1103858969.pdf)
constructs the Hilbert space and positive-energy Lorentzian theory from
Euclidean Green functions under their axioms; the
[1975 sequel](https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-42/issue-3/Axioms-for-Euclidean-Greens-functions-II-with-an-Appendix-by/cmp/1103899050.pdf)
repairs and refines the regularity/equivalence conditions.

A modern operator-level formulation makes the output particularly clear:
reflection-positive measures correspond, under its stated cutoff and
regularity conditions, to OS data consisting of a Hilbert space, positive
self-adjoint Hamiltonian, and cyclic ground state
([Lang, Liegener, and Thiemann](https://arxiv.org/abs/1711.05685)).

This is not merely “another representation.” It is an established
reconstruction theorem. But it reconstructs from a heavily typed input:

```text
field/test-function algebra
+ product and involution
+ spacetime and symmetry action
+ state/correlation hierarchy
+ positivity or reflection positivity
+ spectrum/locality/regularity conditions
-> cyclic QFT representation.
```

It does not derive the left-hand side from a finite observer record.

## 3. Exact algebra-antecedent counterexample

The new hostile control uses one four-dimensional real vector space with basis

\[
(1,a,b,c)
\tag{12}
\]

and the same linear state coordinates

\[
\omega(1)=1,
\qquad
\omega(a)=\omega(b)=\omega(c)=0.
\tag{13}
\]

### Packet A — commutative Walsh algebra

Represent the basis as the four Walsh functions on four points:

\[
\begin{aligned}
1&=(1,1,1,1),\\
a&=(1,1,-1,-1),\\
b&=(1,-1,1,-1),\\
c&=(1,-1,-1,1),
\end{aligned}
\tag{14}
\]

with pointwise multiplication, identity involution, and uniform-average
state. Then

\[
ab=c,
\qquad
abc=1,
\qquad
\omega(abc)=1.
\tag{15}
\]

### Packet B — noncommutative matrix algebra

Represent the same coordinate basis by

\[
1=I,
\qquad
a=
\begin{pmatrix}0&1\\1&0\end{pmatrix},
\qquad
b=
\begin{pmatrix}0&1\\-1&0\end{pmatrix},
\qquad
c=
\begin{pmatrix}1&0\\0&-1\end{pmatrix},
\tag{16}
\]

with transpose involution and normalized-trace state. Then

\[
ab=-c,
\qquad
abc=-1,
\qquad
\omega(abc)=-1.
\tag{17}
\]

In both packets,

\[
\omega(e_i^*e_j)=\delta_{ij}.
\tag{18}
\]

Therefore they have:

- the same underlying vector coordinates;
- the same one-point state functional;
- the same positive two-point GNS Gram matrix;
- faithful four-dimensional cyclic representations; and
- different multiplication, commutators, and held-out triple correlation.

### Theorem 2 — state/pairing does not select product

A state functional on a bare vector space, even together with its complete
two-point Hilbert pairing, does not select the star-algebra product.

The product is not optional notation. It determines what an \(n\)-point query
means. A “complete functional” becomes complete only **on a fixed algebra**.

This is the QFT-level analogue of `HC-DU-127`:

```text
bare operator M
  needs the pairing K

bare state values and pairing
  need the algebra product, involution, and test/source structure.
```

## 4. Positivity is load-bearing

On

\[
\mathcal A=\mathbb R[x]/(x^2=1),
\tag{19}
\]

define a normalized functional by

\[
\omega(1)=1,
\qquad
\omega(x)=2.
\tag{20}
\]

The candidate Gram matrix in basis \((1,x)\) is

\[
G=
\begin{pmatrix}
1&2\\
2&1
\end{pmatrix}.
\tag{21}
\]

For \(v=1-x\),

\[
\omega(v^*v)
=
(1,-1)G(1,-1)^\mathsf T
=-2.
\tag{22}
\]

No positive Hilbert GNS packet follows.

By contrast, the state

\[
\omega(1)=\omega(x)=1
\tag{23}
\]

has

\[
G=
\begin{pmatrix}
1&1\\
1&1
\end{pmatrix}.
\tag{24}
\]

The vector \(1-x\) has zero norm and spans a left-invariant null ideal.
Quotienting it produces a one-dimensional GNS space.

This proves two exact type boundaries:

1. positivity is not cosmetic; it creates the Hilbert pairing; and
2. the physical representation space is functional-relative after the null
   quotient, not automatically the original bare source vector space.

## 5. Why this does not transfer directly to GU or every gauge QFT

GU's current relevant packet is indefinite/Krein rather than positive
Hilbert. Ordinary GNS/Wightman positivity therefore cannot simply be declared
to reconstruct it.

Indefinite-metric QFT has its own reconstruction theory.
[Morchio and Strocchi](https://www.numdam.org/item/AIHPA_1980__33_3_251_0.pdf)
replace ordinary positivity with a Hilbert-space structure condition and
construct a Hilbert topology plus bounded nondegenerate metric operator under
their hypotheses.
[Albeverio, Gottschalk, and Wu](https://arxiv.org/abs/math-ph/0409057)
give concrete models whose truncated Wightman functions satisfy that
condition. This is positive evidence that indefinite reconstruction is
possible—not evidence that the necessary Hilbert majorant, metric operator,
domain, or physical quotient is selected in GU.

The transfer boundary is:

```text
positive Wightman functional
  -> ordinary Hilbert reconstruction

indefinite Wightman functional
  + Hilbert-space structure condition
  -> conditional Krein reconstruction

GU-native source/domain/Green-form packet
  -> still unbuilt at the frozen GU revision.
```

No GU claim or grade changes.

## 6. Every fixed finite hierarchy still leaks

This part is an absorbed regression of `HC-DU-100`, now stated on a fixed
polynomial star algebra.

Two positive probability states give:

\[
\mu_A
=
\tfrac12\delta_{-1}
+\tfrac12\delta_1,
\tag{25}
\]

\[
\mu_B
=
\tfrac13\delta_{-1}
+\tfrac12\delta_0
+\tfrac16\delta_2.
\tag{26}
\]

Their moments satisfy

\[
m_0=1,
\qquad
m_1=0,
\qquad
m_2=1
\tag{27}
\]

for both, while

\[
m_3(\mu_A)=0,
\qquad
m_3(\mu_B)=1.
\tag{28}
\]

The executable control generalizes this. For every retained order \(N\), put
signed finite-difference weights on \(0,\ldots,N+1\):

\[
w_i=(-1)^{N+1-i}\binom{N+1}{i}.
\tag{29}
\]

They annihilate every polynomial of degree at most \(N\) and give
\((N+1)!\) on degree \(N+1\). A sufficiently small exact perturbation of the
uniform distribution in the \(\pm w\) directions gives two strictly positive
states with identical moments through \(N\) and different moment \(N+1\).

Therefore:

> No fixed finite correlation order determines an unrestricted positive
> functional hierarchy.

This is not new moment mathematics. Its DU consequence is decisive:
Wightman reconstruction starts from an infinite exact hierarchy. It is not
yet a theorem that bounded formed records reconstruct that hierarchy.

A finite repair needs a physical class such as:

- quasifree/Gaussian closure, where the two-point function fixes higher
  correlations by Wick structure;
- finite-dimensional or finite-recurrence closure;
- a common analytic tail and target margin, as in `HC-DU-100`; or
- another independently selected finite sufficient-statistic theorem.

Choosing such a class after seeing the target would be completion refit.

## 7. Field/direct-action consequence

Suppose a field presentation and a direct-action presentation:

1. use the same source/observable star algebra \(\mathcal A\);
2. induce the same complete positive functional \(\omega\) on \(\mathcal A\);
   and
3. satisfy the same reconstruction hypotheses.

Then GNS/Wightman uniqueness gives equivalent cyclic observable
representations for every query in \(\mathcal A\).

This is stronger than matching one kernel, response matrix, or S-matrix. It
is an exact **conditional operational duality** on the shared algebra.

It still does not establish:

- that a mediator-local field belongs to the shared algebra;
- equality of different local nets or extended operator algebras;
- equality of determinant, anomaly, boundary, regulator, or gravitational
  response packets;
- one ontology;
- one physical record interface; or
- empirical excess.

A mediator-facing observable outside \(\mathcal A\) reopens the fibre exactly
as in `HC-DU-115`, `HC-DU-125`, and `HC-DU-126`.

## 8. What this means for the North Star

The result identifies three nested completeness targets:

```text
complete functional on a fixed observable algebra
  -> complete expectation and cyclic-representation reconstruction

complete theoretical correlation hierarchy
  -> conditional Wightman/OS QFT reconstruction

physically formed finite certified record
  -> still not shown to determine either object.
```

The first two are real mathematical positives. The third is Dynamic Unity's
unresolved physical problem.

This also clarifies what can be said to “hold the state of the physics”:

> Relative to a fixed observable algebra, the complete positive functional
> holds the state strongly enough to reconstruct its cyclic Hilbert
> realization. Relative to a Wightman/OS field contract, the full correlation
> hierarchy holds the QFT realization. Neither object selects its own
> algebraic, spacetime, or acquisition antecedents.

That is a much more precise statement than “the wavefunction,” “the records,”
or “the source operator” holds everything.

## 9. Absorption, grade, and stop

### Earned

- **Conditional Grade 3 import:** a complete positive Wightman/OS functional
  reconstructs a QFT representation under its exact axioms.
- **Scoped Grade 4 necessity:** positivity is required for ordinary Hilbert
  GNS reconstruction.
- **Scoped Grade 4 nonselection:** the state functional and induced two-point
  pairing do not select the algebra product.
- **Scoped Grade 4 finite boundary:** every fixed finite correlation order
  leaves an exact next-order first leak in the unrestricted positive class.
- **Scoped Grade 4 transfer boundary:** ordinary positive reconstruction does
  not establish an indefinite/Krein or GU reconstruction.

### Absorbed

The component mathematics is absorbed by:

- GNS;
- Wightman reconstruction;
- Osterwalder--Schrader reconstruction;
- the classical moment problem and finite differences;
- indefinite-metric Wightman reconstruction; and
- algebraic system identification.

DU's increment is the typed composition with `HC-DU-127`, the exact
same-functional/same-pairing/different-product witness, and the separation
between theoretical functional completeness and formed finite-record
completeness.

### Not earned

- a selected observable or field algebra;
- a selected physical state or Euclidean measure;
- emergent spacetime or causal order;
- a finite formed correlation hierarchy;
- a selected probe, detector, archive, observer, or access boundary;
- an indefinite/GU reconstruction;
- field or direct-action ontology priority;
- empirical excess, new law, new physics, or prediction; or
- a ready successor.

### Exact reopener

Reopen only when one serious physical arena supplies, before held-out
evaluation:

1. a fixed physical observable/source algebra and causal/test-function
   structure;
2. a dynamically selected positive state functional or an explicitly typed
   indefinite replacement;
3. a theorem making a finite physically formable record sufficient for the
   target functional class at a declared resolution;
4. a realizable source/probe/readout/archive/access interface;
5. complete attempt lineage and bounded resources; and
6. a no-refit held-out target or cross-arena transfer.

More finite GNS examples or formal correlation hierarchies add no value.

## Honest status

`HC-DU-128` is a scoped Grade-4 boundary assembled from standard mathematics
and exact rational controls, with established Wightman/OS reconstruction
imported at conditional Grade 3.

It gives DU a genuine reconstruction positive and locates its precise
physical shortfall. It does not select the input theory or convert an infinite
theoretical functional into a finite observer record.
