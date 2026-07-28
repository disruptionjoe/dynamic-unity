---
title: "Relativistic ETH: physical co-filtration, large-N event selection, and the external-device boundary"
status: completed_scoped_result
doc_type: primary_source_reopener_and_exact_selection_boundary
created: 2026-07-28
work_id: CCR-RELATIVISTIC-ETH-COFILTRATION-SELECTOR-AUDIT
claim_id: HC-DU-092
run_id: RUN-20260728-184603-relativistic-eth-cofiltration-selector-audit
lanes:
  - lane_1
  - lane_2
  - lane_3
  - lane_4
  - lane_6
  - lane_7
channels:
  - CH-COLLIDE
  - CH-FORMAL
  - CH-SYN
claim_grade: "GRADE 4 SCOPED PHYSICAL-TYPING AND INTERFACE-NONSELECTION BOUNDARY, WITH AN EXACT MAXIMAL-TORUS NO-POINT-SELECTOR COROLLARY; NO NEW PHYSICS, COMPLETE RECORD INTERFACE, EMPIRICAL EXCESS, ISSUANCE, OR PAPER PROMOTION"
decision: PARTIAL_PHYSICAL_TYPING_WITH_SUPPLIED_EVENT_INTERFACE
---

# Relativistic ETH physical co-filtration audit

## Executive verdict

This audit corrects an overly broad possible reading of `HC-DU-091`.

The generic \(M_2(\mathbb C)\) counterexample proved that the
center-of-centralizer rule does not select the future algebra to which it is
applied. It did **not** prove that physics cannot select such an algebra.
Relativistic ETH supplies two real partial positives:

1. In the scoped four-dimensional massless-field construction, a spacetime
   point and the local QFT net determine a future-cone algebra, and Huygens'
   principle yields a strict co-filtration. This is not an arbitrary matrix
   subalgebra inserted after the fact.
2. In the 2026 large-\(N\) \(\mathcal N=4\) SYM construction, strict
   time-band inclusion is proved above the Hawking--Page temperature and is
   argued not to hold below the transition or at zero temperature.
   Diminishing potentialities can therefore be a physical, phase-relative
   algebraic property.

The correction does not produce a complete selector. The same sources expose
the next boundary:

```text
physical spacetime/net/phase
    -> a physically typed shrinking future algebra

shrinking future algebra
    -/-> a nontrivial event
    -/-> a selected event interface
    -/-> a formed certified record.
```

In the large-\(N\) thermal state, the centralizer has trivial center, so no ETH
event occurs in exact equilibrium. The published construction obtains a first
event only after:

- adjoining an external device by a crossed product;
- choosing one maximal Abelian subgroup \(H\subset G\);
- choosing an extended device state \(k\in L^2(H)\); and
- choosing a countable partition of the joint Cartan spectrum.

The source explicitly describes the construction as rather ad hoc, identifies
the crossed product with an external measuring device, and says the spectral
partition is nonunique and lacks a preferred rule.

There is also an exact symmetry obstruction. For the non-Abelian compact
semisimple symmetry group used in the model, no maximal torus is fixed by all
inner automorphisms. A covariant rule can return the conjugacy class of
maximal tori, but not one physical torus without a symmetry-breaking device
or state. The first-event basis is therefore selected by the added interface,
not by the equilibrium black-hole algebra alone.

Once a partition and event time are fixed, the ETH state update is the
ordinary Lüders projective instrument. No empirical excess over the matched
AQFT, holographic, and instrument account was isolated.

The returned states are:

```text
CONDITIONAL_NET_SELECTION_ONLY
+ STRICT_DIMINUTION_MODEL_RELATIVE
+ NONTRIVIAL_ACTUALITY_NOT_GUARANTEED
+ REGION_OR_STATE_RELATIVE_EVENT_AMBIGUITY
+ STANDARD_AQFT_INSTRUMENT_ABSORPTION
+ NO_REOPENER
```

`NO_REOPENER` means no immediate event-to-record successor is activated. It
does not erase the partial positive or declare ETH closed.

## Primary-source basis

The audit reconstructs:

- [Relativistic Quantum Theory](https://arxiv.org/abs/1912.00726), which
  associates a future-event algebra \(\mathcal E_P\) with a spacetime point,
  states the relativistic Principle of Diminishing Potentialities, defines
  events through the center of a state centralizer, and makes collapse and
  spacelike-event compatibility explicit axioms;
- [The Time-Evolution of States in Quantum
  Mechanics](https://arxiv.org/abs/2101.01044), which gives the explicit
  future-cone/diamond algebra construction for a free electromagnetic field,
  derives strict inclusion from Huygens' principle in that model, and labels
  the collapse rule an axiom;
- [Two Results in the Quantum Theory of
  Measurements](https://arxiv.org/abs/2312.00599), which distinguishes an
  actuality from the completion of a measurement of a supplied physical
  quantity at instrument-dependent accuracy; and
- [Principle of Diminishing Potentialities in Large \(N\)
  Algebras](https://arxiv.org/abs/2508.11688), published in JHEP in July 2026,
  which proves the temperature/phase-relative large-\(N\) result and
  constructs a first event only after an external-device extension.

These sources establish the mathematical claims attributed to their
frameworks. They do not establish that the ETH ontology is physically true.

## The typed construction

### Relativistic future-cone algebras

The relativistic framework begins with a spacetime \(M\), a local net
\(O\mapsto\mathcal A(O)\), a represented global algebra \(\mathcal E\), and a
state. For each point \(P\), \(\mathcal E_P\) is the von Neumann algebra
generated by quantities localized in the future of \(P\).

For causally ordered points \(P\prec P'\), the proposed physical condition is

\[
\mathcal E_{P'}\subsetneq\mathcal E_P
\]

with an infinite-dimensional noncommutative relative commutant. Fröhlich
calls this the Principle of Diminishing Potentialities. In the explicit free
electromagnetic-field model, field operators are smeared over future cones
and diamonds. Huygens' principle makes the relevant relative commutant the
diamond algebra and establishes strict inclusion.

This earns conditional physical-typing credit. Given the spacetime, point,
time orientation, field net, representation, and admitted massless
propagation law, the future algebra is geometrically and dynamically
motivated rather than chosen from all subalgebras of \(B(\mathcal H)\).

The scope matters:

- the spacetime, local net, system, representation, state, and point or
  trajectory remain antecedents;
- the explicit proof is tied to four-dimensional massless propagation and
  Huygens-type structure;
- the 2021 source says the interacting four-dimensional relativistic case is
  not under general mathematical control; and
- in the abstract 2019 formulation, the family
  \(\{\mathcal E_P\}_{P\in M}\) satisfying PDP is part of the data specifying
  the physical system.

The correct grade is therefore `CONDITIONAL_NET_SELECTION_ONLY`, not a
parameter-free derivation of the local net, observer boundary, or event
interface.

### Large-\(N\) phase-relative diminution

Sia's large-\(N\) construction supplies a sharper physical comparator.
For the single-boundary large-\(N\) algebra of thermal
\(\mathcal N=4\) SYM:

\[
\mathcal M_{\ge t}\subsetneq\mathcal M_{\ge t'}
\qquad (t>t')
\]

above the Hawking--Page temperature. The source argues that the strict
inclusion does not hold below the transition or at zero temperature.

This is useful to Dynamic Unity because it separates three claims that had
often been verbally compressed:

1. a future-algebra co-filtration exists;
2. its inclusions are strict; and
3. an actual event occurs.

The first two can be physically phase-relative while the third fails. In
exact thermal equilibrium, the centralizer of the thermofield-double state
coincides with the scalar center of the factor. Hence

\[
Z_{\omega_{\mathrm{TFD}}}(\mathcal M)=\mathbb C I
\]

and the ETH event criterion returns no event.

Strict loss of accessible future algebra is therefore not yet formation,
actuality, a record, or finality. It is a physical access-structure result.

## Exact maximal-torus no-point-selector corollary

The large-\(N\) paper obtains a nontrivial event algebra by crossing the
right-boundary algebra with a maximal Abelian subgroup

\[
H\simeq U(1)^5
\]

of

\[
G=SO(4)\times SU(4)_R.
\]

The relevant general obstruction is elementary.

### Proposition

Let \(G\) be a compact connected non-Abelian semisimple Lie group. No rule
depending only on \(G\) can select one maximal torus \(T\subset G\) while
remaining invariant under every inner automorphism of \(G\).

### Proof

If a selected maximal torus were invariant under every inner automorphism,
then

\[
gTg^{-1}=T
\qquad\text{for every }g\in G,
\]

so \(T\) would be a normal subgroup. Its Lie algebra \(\mathfrak t\) would
then be an Abelian ideal in the semisimple Lie algebra \(\mathfrak g\).
Semisimplicity permits no nonzero Abelian ideal. But a maximal torus of a
positive-rank compact semisimple group has nonzero Lie algebra. This is a
contradiction. \(\square\)

All maximal tori are conjugate, so the group does select an orbit of
admissible tori. It does not select one member. Applied to
\(SO(4)\times SU(4)_R\), the chosen \(U(1)^5\) is therefore not invariant
under the complete antecedent symmetry.

There are two legitimate exits, with different meanings:

- if conjugate choices are gauge-equivalent, the physically selected object
  is only the orbit, not one first-event basis;
- if an external device or nonequilibrium state breaks the symmetry, that
  additional physical interface selects the torus.

Neither exit credits the equilibrium algebra alone with selecting the event.

## The source's own interface disclosures

The large-\(N\) construction makes the missing structure unusually visible.

### External device

The crossed product by \(H\) is interpreted as coupling to an external
measuring device. The chosen wavefunction

\[
k\in L^2(H)
\]

is an additional device state that drives the extension away from the
original KMS equilibrium.

That is a coherent physical story. It is also exactly the typed statement
Dynamic Unity requires: the event appears only after a source--probe boundary
and device state are added.

### Noncanonical event coarse graining

The first event is represented by spectral projectors of the commuting
Cartan charges. To obtain a countable partition of unity, the joint spectrum
is partitioned into countably many measurable cells. The source states that
this partition is not unique and that no preferred or canonical rule is
provided.

Thus even after \(H\) and \(k\) are fixed:

```text
commutative centralizer
    -> admitted spectral measure
    -/-> one selected finite/countable event partition.
```

Stochastic selection of one projector does not select which projector family
defined the sample space.

### Collapse and measurement

For a fixed event family \(\{P_\xi\}\), ETH uses

\[
p_\xi=\omega(P_\xi),
\qquad
\omega_\xi(X)
=
\frac{\omega(P_\xi X P_\xi)}{\omega(P_\xi)}.
\]

This is the standard Lüders projective instrument. It is an explicit ETH
postulate in the relativistic source, not a consequence of Huygens' principle
or strict algebra inclusion.

The separate measurement paper adds a further conditional relation: an
actuality can be interpreted as the completion of a measurement only when it
approximately commutes with the operator representing a supplied physical
quantity, at an accuracy set by the instrument. The instrument, observable,
resolution, archive, and access relation are not selected by the event
criterion.

## Selection-versus-supply ledger

| Object | Earned status |
|---|---|
| spacetime and causal future | supplied physical antecedent in the relativistic construction |
| local AQFT net | supplied theory structure; not selected by ETH |
| future-cone algebra once net and point are fixed | conditionally derived |
| strict co-filtration in the free massless four-dimensional model | proved in scope through Huygens structure |
| strict large-\(N\) time-band inclusion | proved above Hawking--Page; argued not to hold below the transition or at zero temperature |
| nontrivial actuality in exact thermal equilibrium | ruled out in the audited large-\(N\) state |
| maximal Abelian subgroup \(H\) | chosen; only its conjugacy class is symmetry-natural |
| external-device state \(k\) | supplied |
| commutative center of the extended centralizer | derived after \(H\) and \(k\) are supplied |
| event partition of the joint spectrum | noncanonical supplied coarse graining |
| realized projector and Born weight | stochastic under the ETH Collapse Postulate |
| posterior state | ordinary Lüders conditioning once the partition is fixed |
| measured quantity and resolution | supplied by the instrument contract |
| durable carrier, provenance, access, certification, regional finality | not selected |

## Relation to `HC-DU-091`

The new result does not overturn the finite restriction theorem. It locates
its physical exit.

```text
HC-DU-091:
    state + ambient algebra alone
        -/-> future-algebra member

HC-DU-092:
    spacetime + local net + causal point/phase
        -> conditionally typed future-algebra co-filtration

    co-filtration + equilibrium state
        -/-> nontrivial event

    co-filtration + chosen external device/interface
        -> conditional event algebra
        -/-> uniquely selected record interface.
```

The program should therefore stop saying or implying that the physical
co-filtration is wholly arbitrary. The sharper result is that present models
can select the **access-loss architecture**, while the actual event and record
still depend on added nonequilibrium interface structure.

## Absorbers and empirical excess

The strongest matched absorbers are:

- ordinary AQFT future-cone and time-band algebras for the co-filtration;
- standard holographic large-\(N\) subregion/subalgebra results for the
  Hawking--Page dependence;
- ordinary physical symmetry breaking or a selected reference device for the
  maximal-torus choice;
- standard projective instruments for the outcome probabilities and state
  updates; and
- ordinary detector modeling for the measured observable, resolution, and
  archive.

No audited prediction differs from the matched standard account after these
objects are frozen. The large-\(N\) paper makes a novel mathematical
connection between PDP and holographic algebra phases, but that is not a
Dynamic Unity empirical remainder.

## North-Star meaning

This swing is a real advance because it moves the missing selector one layer
downstream:

```text
before:
    can physics select a future algebra at all?

now:
    yes, conditionally, in important QFT/holographic classes;
    but can the source--probe interaction select the event quotient,
    carrier, provenance, and access without refitting?
```

It also gives a useful negative control for layered regional finality.
Algebraic accessibility can shrink sharply across time or a phase transition
without producing a public fact. A shrinking capability envelope is not
itself consensus, certification, or settlement.

## Stop and exact reopener

Do not continue generic ETH co-filtration or center-of-centralizer work.
Do not build a record layer on top of the large-\(N\) event until its physical
interface is selected.

Reopen only with one frozen nonequilibrium source--probe model that:

1. derives the probe coupling, symmetry breaking, commuting charge family,
   and spectral coarse graining from independently fixed physical
   antecedents;
2. proves invariance of the resulting actionable quotient under conjugate
   descriptions, or records the physical device variable that separates
   them;
3. produces a blank-to-written carrier with retained provenance and a bounded
   access relation;
4. transfers without refitting across at least one state, region, or phase
   change; and
5. yields a held-out consequence not already fixed by the matched AQFT plus
   quantum-instrument model.

That is a genuine reopener, not an activated successor.

## Resource disposition

Primary-source reconstruction and the exact maximal-torus argument decide the
gate. No local numerical model could raise the grade, and no external hardware
is relevant. No paper, prediction, publication, submission, provider, or
contact action was authorized or performed.
