---
title: "ETH actuality-algebra naturality: restriction counterexample and instrument boundary"
status: completed_scoped_result
doc_type: exact_theorem_counterexample_and_absorber_gate
created: 2026-07-28
work_id: CCR-ETH-ACTUALITY-ALGEBRA-NATURALITY
claim_id: HC-DU-091
run_id: RUN-20260728-183138-eth-actuality-algebra-naturality
lanes:
  - lane_1
  - lane_2
  - lane_3
  - lane_4
  - lane_7
channels:
  - CH-COLLIDE
  - CH-FORMAL
  - CH-SYN
claim_grade: "GRADE 4 SCOPED COVARIANCE/NON-NATURALITY THEOREM AND EXACT FINITE COUNTEREXAMPLE; KNOWN COMPONENT MATHEMATICS; NO NEW PHYSICS, ONTOLOGY-PRIORITY, ISSUANCE, PREDICTION, OR PAPER PROMOTION"
decision: ALGEBRA_RELATIVE_EVENT_AMBIGUITY
---

# ETH actuality-algebra naturality

## Executive verdict

The ETH center-of-centralizer construction passes one naturality test and
fails the more important one:

```text
faithful re-presentation
    -> REPRESENTATION_NATURALITY

restriction to a future subalgebra
    -> ALGEBRA_RELATIVE_EVENT_AMBIGUITY

selection of that future-algebra co-filtration
    -> NO_PHYSICAL_COFILTRATION_SELECTOR

fixed event projections + Collapse Postulate
    -> STANDARD_INSTRUMENT_ABSORPTION
```

The positive result is exact. If a star-isomorphism carries both the algebra
and state, it carries the centralizer and its center. ETH does not depend on
coordinates or a chosen matrix basis in this elementary sense.

The negative result is also exact. Restricting the same state to a supplied
subalgebra can create a nontrivial actuality algebra that did not exist in the
ambient algebra, and different symmetry-related subalgebras can create
incompatible event algebras. Consequently, the center-of-centralizer rule
does not by itself select the physical future-algebra co-filtration to which
it is applied.

This closes the present lower selector gate. It does **not** refute ETH, prove
that every physical ETH model is ambiguous, or show that no QFT construction
can select a future-algebra net. It shows exactly what must be added before
Dynamic Unity can credit ETH with a physically selected event interface.

## Frozen imported object

Following the ETH construction audited in
[HC-DU-090](event-formation-antecedent-tournament-eventum-eth-kent-2026-07-28.md),
let \(A\) be a von Neumann algebra and \(\omega\) a state. Define

\[
C_\omega(A)
=
\{Y\in A:\omega([Y,X])=0\text{ for all }X\in A\}
\]

and the actuality algebra

\[
Z_\omega(A)=Z(C_\omega(A)).
\]

An ETH event family is a partition of unity whose projections generate a
nontrivial \(Z_\omega(A)\) and have positive weights. The Collapse Postulate
chooses one event projection \(P_i\) with probability \(\omega(P_i)\) and
conditions the state:

\[
\omega_i(X)
=
\frac{\omega(P_i X P_i)}{\omega(P_i)}.
\]

The primary ETH sources are:

- [The Time-Evolution of States in Quantum Mechanics](https://arxiv.org/abs/2101.01044);
- [A Brief Review of the ETH-Approach](https://arxiv.org/abs/1905.06603);
- [A Garden of Forking Paths](https://arxiv.org/abs/1603.09664); and
- [Relativistic Quantum Theory](https://arxiv.org/abs/1912.00726).

These sources motivate and define the construction. The theorems below
concern its typed selector boundary, not the truth of its ontology.

## Assumption and warrant ledger

| Item | Type | Role |
|---|---|---|
| finite \(M_2(\mathbb C)\), states, star-isomorphisms, projective instruments | `STANDARD` | smallest exact arena |
| center-of-centralizer event rule and Collapse Postulate | `IMPORTED` | ETH object under audit |
| a physical selector must respect declared physical equivalence and cannot be supplied by the target interface | `PROJECT_NATIVE` | Dynamic Unity selection discipline |
| \(B_z\) and \(B_x\) are alternative mathematical refinements of one coarse future-algebra net | `CONDITIONAL_POSIT` | hostile completion pair |

The conditional posit does not say that Nature implements either refinement.
It asks what the frozen antecedent can select before an additional physical
net, apparatus, boundary, or asymmetry is supplied.

## Theorem 1 — representation covariance

Let

\[
\alpha:A\rightarrow A'
\]

be a unital star-isomorphism and define

\[
\omega'=\omega\circ\alpha^{-1}.
\]

Then

\[
\alpha(C_\omega(A))=C_{\omega'}(A')
\]

and

\[
\alpha(Z_\omega(A))=Z_{\omega'}(A').
\]

### Proof

For \(Y,X\in A\),

\[
\omega'([\alpha(Y),\alpha(X)])
=
\omega(\alpha^{-1}(\alpha([Y,X])))
=
\omega([Y,X]).
\]

Thus \(Y\) belongs to the original centralizer exactly when
\(\alpha(Y)\) belongs to the transported centralizer. A star-isomorphism also
maps the center of an algebra onto the center of its image. Therefore it maps
the actuality algebra exactly. \(\square\)

### Consequence

A state-preserving automorphism maps \(Z_\omega(A)\) to itself. This is the
earned `REPRESENTATION_NATURALITY` result. It prevents a mere matrix-basis
change from manufacturing an event.

## Theorem 2 — restriction naturality fails

There exist a unital inclusion \(B\subset A\) and a faithful state \(\omega\)
such that

\[
Z_{\omega|_B}(B)
\ne
B\cap Z_\omega(A).
\]

### Smallest symmetric counterexample

Take

\[
A=M_2(\mathbb C),\qquad
\tau(X)=\frac12\operatorname{Tr}(X).
\]

Because \(\tau\) is tracial,

\[
C_\tau(A)=A.
\]

Hence

\[
Z_\tau(A)=Z(A)=\mathbb C I.
\]

Now restrict to the maximal Abelian subalgebra

\[
B_z=\operatorname{span}\{I,Z\}.
\]

Since \(B_z\) is commutative,

\[
C_{\tau|_{B_z}}(B_z)=B_z
\quad\text{and}\quad
Z_{\tau|_{B_z}}(B_z)=B_z.
\]

But

\[
B_z\cap Z_\tau(A)=\mathbb C I.
\]

The left side of the proposed restriction law has complex dimension two; the
right side has dimension one. \(\square\)

### Nontracial control

The failure is not only an artifact of a maximally mixed state. Let

\[
\rho=\operatorname{diag}(3/4,1/4)
\]

and \(\omega_\rho(X)=\operatorname{Tr}(\rho X)\). In the ambient algebra,

\[
C_{\omega_\rho}(A)
=
Z_{\omega_\rho}(A)
=
B_z.
\]

Restricting the same state to

\[
B_x=\operatorname{span}\{I,X\}
\]

gives

\[
Z_{\omega_\rho|_{B_x}}(B_x)=B_x,
\]

while

\[
B_x\cap B_z=\mathbb C I.
\]

Restriction can therefore rotate the actuality algebra even when the ambient
state is faithful and nondegenerate.

## Corollary — coarse future data does not select its event refinement

Under the tracial state and identity dynamics, compare two decreasing
co-filtrations:

\[
M_2(\mathbb C)\supset B_z\supset\mathbb C I
\]

and

\[
M_2(\mathbb C)\supset B_x\supset\mathbb C I.
\]

They have the same coarse endpoints. Their intermediate actuality algebras
are \(B_z\) and \(B_x\), respectively. Since

\[
[X,Z]\ne0,
\]

the corresponding atomic event projections are incompatible.

The Hadamard automorphism

\[
\alpha_H(Y)=HYH^\dagger
\]

preserves the tracial state and identity dynamics while exchanging
\(B_z\) and \(B_x\). Thus the frozen symmetric antecedent does not select one
intermediate co-filtration point. Coarse time data also does not determine
which refinement was inserted.

This is a nonidentification result, not a claim that every subalgebra is
physically admissible. A physical theory can exit the counterexample by
selecting a particular local net, boundary, interaction, reference structure,
or symmetry-breaking state. The price of that exit must remain explicit.

## Theorem 3 — no equivariant MASA point selector in the symmetric fixture

Let the antecedent be

\[
(M_2(\mathbb C),\tau,\mathrm{id})
\]

and let its physical-equivalence group contain all inner unitary
automorphisms. There is no selector that:

1. returns one maximal Abelian subalgebra of \(M_2(\mathbb C)\); and
2. is invariant under every automorphism preserving the antecedent.

### Proof

Every maximal Abelian subalgebra of \(M_2(\mathbb C)\) is unitarily conjugate
to \(B_z\). The Hadamard unitary sends \(B_z\) to the distinct algebra \(B_x\).
Conjugating this observation shows that no maximal Abelian subalgebra is
fixed by the full unitary symmetry group. Therefore an equivariant selector
cannot return one orbit point. It may return the whole orbit or the invariant
trivial algebra, neither of which is a selected material event basis.
\(\square\)

This is the precise stabilizer obstruction. The problem is not that ETH uses
a basis. The problem is that the future-algebra co-filtration must already
contain the physical asymmetry that makes one event algebra available.

## Atomic generating-family control

Once either two-dimensional atomic Abelian algebra is fixed, its two minimal
projections are unique up to relabeling:

\[
P_{z,\pm}=\frac{I\pm Z}{2},
\qquad
P_{x,\pm}=\frac{I\pm X}{2}.
\]

Any nontrivial pair of nonzero orthogonal projections in that algebra that
sums to \(I\) is its pair of minimal projections. Thus the finite kill is not
generated by a gratuitously noncanonical event family. It is already present
at the earlier algebra/co-filtration-selection layer.

In diffuse or non-atomic Abelian algebras, generating-family conventions may
remain an additional burden. That broader issue is not needed for this
counterexample.

## Standard-instrument absorption

For a fixed projective family \(\{P_i\}\), the ETH Collapse Postulate uses

\[
p_i=\operatorname{Tr}(\rho P_i)
\]

and

\[
\rho_i=\frac{P_i\rho P_i}{p_i}.
\]

These are exactly the probabilities and posterior states of the ordinary
Lüders projective instrument

\[
\mathcal I_i(\rho)=P_i\rho P_i.
\]

In the exact tracial fixture, both event families have weights \(1/2\), their
conditioned states are the corresponding rank-one projectors, and a sequential
\(Z\)-then-\(X\) history has four joint weights \(1/4\).

Therefore the fixed finite event step returns
`STANDARD_INSTRUMENT_ABSORPTION`. ETH can still make an ontological assertion
that one event objectively occurs. But the matched finite probabilities and
state updates provide no operational excess over standard quantum
instruments once the event projections and occurrence time are supplied.

This does not prove empirical equivalence for every ETH model. A physical
event trigger or continuous-time law could have excess content. It must first
be selected and then compared with a frozen ordinary-quantum null.

## Abductive comparison

| Candidate explanation | Compression | Independent content | Robustness | Progressivity |
|---|---|---|---|---|
| center-of-centralizer alone selects physical events | low after the counterexample; the result changes with the supplied subalgebra | none beyond the supplied co-filtration in this fixture | fails restriction and refinement | loses a free choice only after a physical co-filtration is added |
| ordinary projective instrument | explains the finite outcome probabilities and updates exactly | no ontology claim | exact for the matched fixture | strongest operational absorber |
| ETH plus independently selected physical co-filtration | could select an objective event algebra without an apparatus pointer convention | open | must survive physical equivalence, restriction, and no-refit transfer | live only after the physical net is derived |

The exact result favors neither a global hidden completion nor an
observer-created ontology. It types the missing selector.

## What Dynamic Unity learned

The partial event selector from `HC-DU-090` has a clean boundary:

```text
physical process
    + supplied future-algebra co-filtration
    + state
        -> selected actuality algebra

physical process + state alone
        -/-> selected future-algebra co-filtration
        -/-> selected event algebra.
```

This means the event-to-record continuation is premature. A durable record,
provenance, access, certification, and regional finality should not be built
on top of an event algebra whose physical co-filtration remains supplied.

The result also improves the program's larger picture. “The records create
reality” cannot be answered by inserting a record or event algebra and then
showing that the dynamics closes over it. The theory must select the
algebraic cut—or prove that every physically admissible cut yields the same
actionable quotient.

## Disposition and exact reopener

Bank:

```text
REPRESENTATION_NATURALITY
+ ALGEBRA_RELATIVE_EVENT_AMBIGUITY
+ NO_PHYSICAL_COFILTRATION_SELECTOR
+ STANDARD_INSTRUMENT_ABSORPTION
+ STOP_LOWER_SELECTOR_FAILED
```

Reopen only with a concrete physical proposal that:

1. derives a future-algebra co-filtration from an independently frozen
   system, dynamics, locality/boundary, and state contract;
2. proves invariance under the proposal's physical equivalences;
3. shows that legitimate restriction and time-refinement choices give one
   material event quotient or records the exact physical condition that
   separates them;
4. selects event timing and the realized-event law without fitting a held-out
   result; and
5. produces a no-refit consequence not already represented by the matched
   standard quantum instrument.

Until such a proposal arrives, Dynamic Unity should stop generic
actuality-algebra naturality and event-to-record work. There is no activated
scientific successor.

## Reproducibility

The deterministic exact-arithmetic regression is:

- `tests/du_eth_actuality_algebra_naturality_probe.py`
- `tests/artifacts/du_eth_actuality_algebra_naturality_result.json`

It reports `19/19`. Under the local-model learning gate, it is a proportional
regression added after the proof and earns no independent model-derived
learning claim.
