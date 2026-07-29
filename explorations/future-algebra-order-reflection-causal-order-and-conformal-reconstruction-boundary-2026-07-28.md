---
title: "Future-algebra order reflection: causal-order and conformal-reconstruction boundary"
status: completed_scoped_theorem_and_counterexample
doc_type: exact_order_theorem_counterexample_and_physical_reconstruction_boundary
created: 2026-07-28
work_id: CCR-FUTURE-ALGEBRA-CAUSAL-ORDER-RECONSTRUCTION-GATE
claim_id: HC-DU-093
run_id: RUN-20260728-190323-future-algebra-causal-order-reconstruction
lanes:
  - lane_1
  - lane_2
  - lane_6
  - lane_7
channels:
  - CH-FORMAL
  - CH-SYN
  - CH-COLLIDE
claim_grade: "GRADE 4 SCOPED ORDER-REFLECTION NECESSITY AND CONDITIONAL CAUSAL/CONFORMAL RECONSTRUCTION, WITH AN EXACT BRANCHING COUNTEREXAMPLE AND TIME-BAND CHAIN NO-GO; KNOWN ORDER, AQFT, MODULAR, AND CAUSAL-GEOMETRY MATHEMATICS; NO FORMED RECORD, SELECTED INTERFACE, METRIC SCALE, NEW PHYSICS, EMPIRICAL EXCESS, OR PAPER PROMOTION"
decision: CONDITIONAL_CAUSAL_RECONSTRUCTION_WITH_ORDER_REFLECTION_REQUIRED
---

# Future-algebra causal-order reconstruction

## Executive result

`HC-DU-092` showed that scoped field physics can conditionally determine
strictly shrinking future algebras. This swing asks what that positive
structure actually contains after the spacetime labels used to construct it
are removed.

The exact answer is:

> A future-algebra family reconstructs causal order from inclusion exactly
> when its assignment is order-reflecting. Isotony and strict diminution
> supply only the forward implication.

For an event poset \(X\), define

\[
x\preceq_F y
\quad\Longleftrightarrow\quad
F(y)\subseteq F(x).
\]

Any antitone future-algebra assignment makes the physical causal order a
subrelation of \(\preceq_F\). It reconstructs the original order exactly only
when the converse holds. Otherwise the algebraic order can:

- identify distinct events whose future algebras coincide; or
- invent causal comparability between physically incomparable events whose
  algebras happen to be nested.

A three-event branching counterexample proves that even strict diminution
with infinite noncommutative relative commutants does not force order
reflection.

There is also an exact chain no-go:

> No single totally ordered co-filtration can order-reflect a causal poset
> containing spacelike-incomparable events.

Thus the large-\(N\) time-band chain audited in `HC-DU-092` may physically
encode loss of future access and may carry rich operator content. Its
**inclusion order alone** cannot reconstruct spatial branching, dimension, or
the full causal order. Recovering those would require internal subregion
algebras, commutation, modular data, or another enrichment—in effect, a
richer net.

The positive ceiling remains substantial. The complete family of geometric
future sets is itself an order anti-embedding. If a physical algebra net
faithfully reflects inclusion on that family, its unlabelled inclusion
diagram reconstructs causal order up to order isomorphism. Under the standard
distinguishing smooth-spacetime hypotheses, the
Hawking--King--McCarthy--Malament results then recover topology,
differential structure, and conformal geometry. The conformal factor or
metric scale still requires volume, clocks, dynamics, or equivalent data.

The result is useful but absorbed. It combines ordinary order theory, AQFT
net distinctions, algebraic/modular reconstruction results, and causal
geometry. It does not establish that an observer physically forms or accesses
the complete algebra diagram, and it does not derive geometry from certified
records.

Returned states:

```text
FULL_CAUSAL_ORDER_CONDITIONALLY_RECONSTRUCTED
+ ORDER_REFLECTION_ADDITIONAL_PREMISE
+ TIME_BAND_CHAIN_SPATIAL_INFORMATION_LOSS
+ ALGEBRA_TYPE_WITHOUT_NET_INSUFFICIENT
+ CONFORMAL_ONLY_UNDER_CONTINUUM_HYPOTHESES
+ TARGET_LABEL_CIRCULARITY
+ KNOWN_MATHEMATICS_ABSORPTION
+ NO_READY_SUCCESSOR
```

## 1. The reconstruction object

Let \((X,\preceq)\) be a causal or operational event poset. Let
\(\operatorname{Sub}(\mathcal A)\) be the poset of admitted von Neumann
subalgebras of an ambient algebra, ordered by inclusion. A future-algebra
assignment is an antitone map

\[
F:X\longrightarrow\operatorname{Sub}(\mathcal A),
\qquad
x\preceq y\Longrightarrow F(y)\subseteq F(x).
\]

The input to reconstruction is the unlabelled diagram consisting of its
algebras and actual inclusion arrows. Point names, coordinates, causal
relations, dimension, metric, and the region labels used to build the net are
not retained.

Define the algebra-induced relation

\[
x\preceq_F y
\quad\Longleftrightarrow\quad
F(y)\subseteq F(x).
\]

This distinction prevents a circular argument:

```text
spacetime labels -> local/future algebras -> return the same labels
```

is a faithful representation, not reconstruction from the unlabelled
algebraic object.

## 2. Theorem 1 — exact order-reflection criterion

### Theorem

For every antitone \(F:(X,\preceq)\to\operatorname{Sub}(\mathcal A)\):

1. \(\preceq_F\) is a preorder.
2. \(\preceq\subseteq\preceq_F\).
3. Quotienting by

   \[
   x\sim_F y
   \quad\Longleftrightarrow\quad
   F(x)=F(y)
   \]

   gives a partial order determined by the unlabelled inclusion diagram.
4. The diagram reconstructs \((X,\preceq)\) up to order isomorphism exactly
   when \(F\) is order-reflecting:

   \[
   F(y)\subseteq F(x)
   \Longrightarrow x\preceq y.
   \]

### Proof

Reflexivity and transitivity of algebra inclusion make \(\preceq_F\) a
preorder. Antitonicity gives

\[
x\preceq y\Longrightarrow F(y)\subseteq F(x),
\]

so \(\preceq\subseteq\preceq_F\).

The equivalence relation induced by equality of algebras is exactly the
antisymmetrization of this preorder. Hence the unlabelled diagram always
recovers the quotient order.

If \(F\) is order-reflecting, then
\(\preceq_F\subseteq\preceq\), so the relations are equal. Equality of
algebras then implies both \(x\preceq y\) and \(y\preceq x\); antisymmetry of
\(X\) gives \(x=y\). Thus \(F\) is an order anti-embedding and the inclusion
diagram is order-isomorphic to \(X^{op}\).

Conversely, if the diagram reconstructs the original order, every algebra
inclusion must represent an actual order relation, which is precisely order
reflection. \(\square\)

### Meaning

AQFT isotony is the forward implication. It says that a larger spacetime
region admits at least the observables of a smaller region. It does not, as
an axiom, say that every algebra inclusion proves the corresponding region
inclusion.

Likewise, strict diminution

\[
x\prec y\Longrightarrow F(y)\subsetneq F(x)
\]

prevents collisions along already comparable events. It says nothing about
equalities or extra inclusions between incomparable events.

## 3. Theorem 2 — strict diminution does not reflect order

The smallest nontrivial branching control has three events:

\[
o\prec a,\qquad o\prec b,\qquad a\parallel b.
\]

Let \(R\) be a noncommutative factor represented on \(\mathcal H_R\), and
work on \(\mathcal H_R^{\otimes3}\). Define

\[
\begin{aligned}
F(o)&=R\ \overline\otimes\ R\ \overline\otimes\ R,\\
F(a)&=R\ \overline\otimes\ R\ \overline\otimes\ I,\\
F(b)&=R\ \overline\otimes\ I\ \overline\otimes\ I.
\end{aligned}
\]

Then

\[
F(b)\subsetneq F(a)\subsetneq F(o).
\]

Both true causal comparisons are represented strictly:

\[
F(a)\subsetneq F(o),
\qquad
F(b)\subsetneq F(o).
\]

If \(R\) is an infinite factor, their relative commutants contain
noncommutative infinite factors. Thus the construction retains the
infinite-noncommutative-relative-commutant shape emphasized by the
relativistic Principle of Diminishing Potentialities.

Nevertheless,

\[
F(b)\subsetneq F(a)
\]

implies \(a\prec_F b\), even though \(a\parallel b\) in the physical poset.
Strict diminution therefore does not by itself reconstruct causal order.

This is an abstract order/algebra countermodel. It does not claim that the
specific free electromagnetic or large-\(N\) nets realize this false
inclusion. It proves that their additional field, covariance, locality,
duality, state, or modular assumptions must do any order-reflection work;
PDP-shaped strictness alone cannot.

## 4. Theorem 3 — a chain cannot reconstruct branching

### Theorem

Let \(C\) be a totally ordered family of algebras. If an antitone map

\[
F:X\longrightarrow C
\]

is order-reflecting, then \(X\) is totally ordered.

### Proof

For any \(x,y\in X\), totality of \(C\) gives either

\[
F(y)\subseteq F(x)
\quad\text{or}\quad
F(x)\subseteq F(y).
\]

Order reflection gives either \(x\preceq y\) or \(y\preceq x\). Hence every
pair in \(X\) is comparable. \(\square\)

Every relativistic causal structure containing spacelike-separated events is
not total. Therefore no one-parameter inclusion chain can reconstruct its
full causal order **from the chain relation alone**.

This theorem does not say that the algebras inside the chain are empty of
spatial information. Their internal subalgebra lattices, commutants,
entanglement, modular structure, charges, or correlation functions might
encode more. Using those objects changes the reconstruction input from one
chain to an enriched net.

## 5. Positive control — full future sets

The geometric future-set assignment loses no order information.

For any reflexive causal poset, let

\[
\uparrow x=\{z\in X:x\preceq z\}.
\]

Then

\[
x\preceq y
\quad\Longleftrightarrow\quad
\uparrow y\subseteq\uparrow x.
\]

The forward direction follows by transitivity. For the converse,
\(y\in\uparrow y\); inclusion therefore gives \(y\in\uparrow x\), which means
\(x\preceq y\).

Thus:

```text
complete geometric future-set family
    -> exact causal order

order-reflecting algebra assignment on that family
    -> exact causal order from algebra inclusions

distinguishing smooth-spacetime hypotheses
    -> conformal geometry

volume / clocks / physical dynamics
    -> possible metric scale
```

The only nontrivial first arrow in the algebraic route is whether

\[
\mathcal A(\uparrow y)\subseteq\mathcal A(\uparrow x)
\quad\Longrightarrow\quad
\uparrow y\subseteq\uparrow x
\]

holds in the admitted physical net after labels are erased.

## 6. What established physics supplies

### Relativistic ETH

Fröhlich's
[relativistic framework](https://arxiv.org/abs/1912.00726) translates
spacetime structure into future-event algebras and emphasizes massless modes
and Huygens structure. Fröhlich and Pizzo's
[model analysis](https://arxiv.org/abs/2101.01044) establishes strict future
inclusions in its declared field setting.

These results support physical antitonicity and scoped strictness. The
audited statements do not prove that the unlabelled future-algebra family is
order-reflecting for every admitted point or region.

### AQFT nets

Fewster and Rejzner's
[AQFT introduction](https://arxiv.org/abs/1904.04051) presents isotony as the
region-inclusion-to-algebra-inclusion direction and emphasizes that physical
information belongs to the net, not an isolated algebra isomorphism type.
Local algebras in broad QFT classes often share universal factor types, which
makes the individual type especially poor as a region label.

Known positive theorems use much richer inputs:

- Weiner's [algebraic Haag
  theorem](https://arxiv.org/abs/1006.4726) reconstructs an algebraic QFT
  model under split and geometric-modular assumptions from a complete
  correspondence of double-cone algebras on a fixed spacelike
  half-hyperplane. The geometric region correspondence is part of the
  hypothesis.
- Buchholz, Dreyer, Florig, and Summers
  [derive spacetime symmetry groups](https://arxiv.org/abs/math-ph/9805026)
  from partially ordered algebra families, states, and geometric modular
  action under additional conditions.
- Half-sided modular-inclusion results can reconstruct translations or
  conformal nets from selected inclusions plus a common standard vector and
  modular/positivity conditions, as already typed in `HC-DU-077`.

These are important positive controls. They show that enriched
algebra--state--inclusion structure can encode geometry. They do not make
strict inclusion alone an order-reflection theorem.

### Causal geometry

Hawking, King, and McCarthy's
[path-topology result](https://doi.org/10.1063/1.522874) and Malament's
[causal reconstruction theorem](https://doi.org/10.1063/1.523436) show that,
under their continuum and distinguishing hypotheses, sufficiently complete
causal structure determines topology, differential structure, and the
conformal metric.

They do not determine the conformal factor. Nor do they show that a finite
record, one chain, or an algebra family lacking order reflection already
contains the required causal structure.

## 7. Application to the two `HC-DU-092` positives

| physical object | earned content | reconstruction limit |
|---|---|---|
| full future-cone family over spacetime points | potentially rich enough to retain causal branching | exact causal recovery additionally requires point separation and order reflection after labels are removed |
| high-temperature large-\(N\) time-band co-filtration | physical phase-relative strict loss of future algebra | its external inclusion order is one chain and cannot reconstruct spacelike branching |
| individual future algebra or factor type | one observable algebra at one cut | isolated isomorphism type does not locate the region |
| enriched local net plus state/modular structure | can reconstruct models, translations, or symmetries in known theorem classes | regions, state/vector, modular action, covariance, split/duality, and positivity remain theorem premises |

This corrects two opposite overreadings:

1. `HC-DU-092` is not merely a relabel. Physics can select a real access-loss
   architecture.
2. Physical selection and strictness of that architecture do not imply that
   it holds the complete causal geometry.

## 8. North-Star consequence

The result identifies the minimum geometry-bearing algebraic object more
sharply:

```text
one algebra
  < one time-band chain
  < a point-separating order-reflecting future-cone net
  < an enriched algebra--state--modular net
  < an independently formed and accessible operational record of that net.
```

The first two cannot carry full causal branching through inclusion order.
The third conditionally reconstructs causal order. The fourth can reconstruct
additional symmetries and dynamics in known theorem classes. Only the fifth
would directly address Dynamic Unity's record-first North Star.

This also answers part of the recurring “what holds the state of physics?”
question:

> Not a single record value, factor, or nested chain. The candidate
> information-bearing object is a structured net: algebras, inclusions,
> commutation/relative position, state or weight, and physical access. Which
> of that structure is independently formed rather than theoretically
> supplied remains the open issue.

## 9. Grade, absorber, and reopener

### Earned

Scoped Grade 4:

- exact order-reflection necessity and sufficiency;
- exact three-event branching counterexample;
- exact time-band chain no-go;
- conditional causal-order and conformal reconstruction ladder; and
- typed separation of physical co-filtration, causal reconstruction, metric
  scale, and formed records.

### Absorbed

The mathematical components are absorbed by:

- order embeddings and preorder antisymmetrization;
- AQFT isotony and net reconstruction;
- modular and half-sided-inclusion reconstruction; and
- Hawking--King--McCarthy--Malament causal geometry.

No novel theorem of operator algebras, spacetime geometry, or physics is
claimed.

### Stop

Do not:

- use the original spacetime index to “reconstruct” spacetime;
- infer order reflection from strict diminution;
- infer spatial geometry from a one-parameter chain;
- infer metric scale from causal/conformal order;
- call an algebra net a certified record; or
- build another arbitrary finite net.

### Exact reopener

Reopen only with a physically formed operational net that:

1. identifies future-access equivalence without using target spacetime
   labels;
2. separates points or regions and proves order reflection over a declared
   causal class;
3. retains the commutation, inclusion, state, and access data used by the
   reconstruction;
4. transfers without refit to a held-out causal or conformal relation; and
5. exposes either metric-scale reconstruction or a finite lawful remainder.

No present candidate supplies that complete premise. No scientific successor
is activated.

## Resource disposition

Primary-source reconstruction and exact order theory decide the gate. No
local model could raise the grade, and no external hardware is relevant. No
paper, prediction, publication, submission, provider, or contact action was
authorized or performed.
