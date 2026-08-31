---
title: "Record algebra, consumer action, inverse-write boundary, and three-mechanism selector frontier"
status: banked_scoped_consumer_nonselection_and_selector_frontier
doc_type: exploration
created: 2026-08-31
claim_id: HC-DU-205
run_id: RUN-20260831-151458-record-module-selector-tournament
program_id: CCR-MINIMAL-PHYSICAL-ANTECEDENT-TO-FINITE-REMAINDER
owner_repo: dynamic-unity
evidence_grade: 4
---

# Executive result

The most important correction from `HC-DU-204` was that physics need not
select absolute record labels and consumer labels separately. It can select a
matched orbit if the complete physical response descends across that orbit.

The present swing asks the next question:

> Does selecting or physically forming the record side determine the matched
> consumer side?

The answer is **no in general**, for an exact reason:

> A fixed formed record algebra admits many record-preserving conditional
> actions with different downstream capabilities. The inverse of the write
> operation returns the carrier to blank; it does not select one of those
> actions.

The smallest reversible control uses source bit `S`, blank record bit `R`, and
target bit `T`:

```text
write:      R <- R XOR S
consume:    T <- T XOR f(R)
unwrite:    R <- R XOR S
```

For all four policies `f:{0,1}->{0,1}`:

- the same writer forms the same record;
- the consumer leaves source and record unchanged;
- the inverse writer returns the record to blank; and
- the four target response signatures remain different.

Thus neither record formation, nondemolition preservation, nor microscopic
reversibility selects the consumer meaning.

This local theorem reframes the three proposed physical selector routes:

| Route | What it selects | Where it stops |
|---|---|---|
| Source-action/QND stability | A record axis or effective instrument orbit inside a frozen informative candidate class | Same record effects admit different conditional continuations; archive and consumer remain unselected |
| Finite-time infrared memory | Soft carrier structure and a conditional dressing component | Bounded detector, resolution, provenance archive, access, and consumer remain supplied |
| Direct action | A source relation/response after the theory and boundary prescription are supplied | The source kernel does not select absorber factorization, event partition, archive, or consumer |

None selects a complete physical handoff. This is a clean null, not a universal
no-go. It identifies the minimum reopener:

> One target-blind physical action, constraint, or stable interaction must tie
> write and downstream use together so that every admissible full handoff on
> the antecedent fibre lies in one matched physical-gauge orbit.

Removing that cross-boundary law must restore distinct consumers, and the law
must also preserve formation, provenance, archive, resources, interventions,
and held-out capability. A writer plus its inverse is not enough.

This is scoped Grade 4 as an exact necessity/nonimplication result and
source-grounded selector disposition. Controlled operations, quantum
instruments, classical structures, quantum combs, automata, and feedback
control absorb the mathematics. It is not a new theorem of physics, a full
selector, a regional composition law, or a prediction. No successor is ready.

# Duplicate gate: the complete handoff object already existed

The swing does not invent another interface schema. `HC-DU-054` already typed
the complete accessible formed interface as:

```text
source binding
material carrier and blank preparation
write coupling and occurrence identity
orientation/reference
retention, reset, and epoch
archive support and routing
observer access
future action envelope
resource horizon.
```

`HC-DU-137` proved that an antecedent selects this object exactly when the
interface is constant on every antecedent fibre. `HC-DU-175` showed that a
stable interaction can embody a relational reference for a bounded action
without producing a record. `HC-DU-203` separated a correction prescription
from enacted capability. `HC-DU-204` then proved diagonal descent of a matched
producer-consumer relabeling.

The only required addition is explicit typing of the consumer relation:

```text
complete handoff
  = complete accessible formed interface
  + physical consumer/action map
  + producer-consumer alignment
```

Absolute label spelling may be quotiented out. The physical alignment,
provenance, resource law, and action family may not.

# Formal handoff object

Let `X` be the admitted source/history class, `R` a formed finite record
carrier, and `Y` a declared downstream response. A complete operational
handoff contains at least:

```text
K(r | x)       producer / instrument
W             material blank-to-written implementation
Pi            occurrence and source provenance
C(y | r)       consumer / continuation
Alpha          producer-consumer alignment
Archive        retention, routing, reset, and access
A,H            interventions, resources, and horizon
```

Its closed response is

\[
H(y\mid x)=\sum_r C(y\mid r)K(r\mid x).
\]

A record relabeling is physical gauge only when it co-transforms every field
and all declared response, resource, provenance, and intervention quantities
descend. `HC-DU-204` proved the response part. The present result proves that
the producer side alone does not supply the missing co-transformation.

# Theorem 1 — record-preserving consumer freedom

Let a finite quantum record have orthogonal sector projectors
\(\{P_r\}_{r\in R}\) on \(\mathcal H_R\). For any family of target unitaries
\(\{V_r\}\), define the record-controlled consumer

\[
C_V=\sum_r P_r\otimes V_r.
\]

Then

\[
[C_V,P_r\otimes I]=0
\qquad\text{for every }r.
\]

Consequently `C_V` preserves the sharp record algebra and every record-sector
probability. Two choices `V` and `V'` may nevertheless give different target
responses.

## Corollary

Any claimed antecedent determined only by:

- the source dynamics;
- the producer/write map;
- the formed record values or algebra; and
- nondemolition preservation of that record

cannot select a unique consumer whenever two admitted controlled families
act differently on the target.

The proof is immediate: the antecedent is identical for the two consumers,
while the downstream capability differs. Its kernel therefore does not refine
the consumer-action kernel.

This is standard controlled-operation mathematics. Its DU consequence is
the load-bearing part:

```text
selected record algebra
  != selected use of that algebra.
```

In algebraic language, the copyable/deletable classical structure does not
choose its downstream action. Coecke, Pavlovic, and Vicary identify
orthonormal bases with commutative dagger-Frobenius structures whose
comultiplication copies basis data and whose counit deletes it
([primary source](https://arxiv.org/abs/0810.0812)). That classical interface
still does not select which conditional operation a later system performs.

# Theorem 2 — the inverse write is erasure, not selected use

Let `W` be a reversible ideal write on a source and blank record:

\[
W\,|r\rangle_S|0\rangle_R
=
|r\rangle_S|r\rangle_R.
\]

Then

\[
W^\dagger|r\rangle_S|r\rangle_R
=
|r\rangle_S|0\rangle_R.
\]

`W†` reverses formation and removes the record. It has no target system
and selects no family `V_r`.

If a separately chosen consumer `C_V` acts before the inverse write, then

\[
W^\dagger C_V W
\bigl(|r\rangle_S|0\rangle_R|\psi\rangle_T\bigr)
=
|r\rangle_S|0\rangle_R V_r|\psi\rangle_T.
\]

The target can retain the consumer's action after the record is erased, but
the chosen `V_r` remains independent of `W`. Time reversal or microscopic
reversibility therefore does not close the handoff selector.

This blocks the cheapest tempting repair:

```text
writer + inverse writer
  does not imply
writer + physically selected record consumer.
```

An irreversible material archive may prevent practical uncomputation, but
irreversibility also does not choose the semantic action performed by a
downstream controller.

# Exact finite control

The executable uses the classical basis of an eight-dimensional reversible
quantum circuit. It exhausts the four binary policies.

| Policy `f(0),f(1)` | Formed record for sources `0,1` | Final target signature after consume + unwrite |
|---|---|---|
| `0,0` | `0,1` | `0,0` |
| `0,1` | `0,1` | `0,1` |
| `1,0` | `0,1` | `1,0` |
| `1,1` | `0,1` | `1,1` |

Every controlled permutation commutes exactly with both record-sector
projectors. The same one formed-record snapshot therefore supports four
distinct target-response signatures.

The matched-orbit regression checks all eight combinations of two label
permutations and four policies. All eight coordinated transformations preserve
the response. Six unmatched combinations are harmless: the four identity
cases and the two constant policies under label swap. The two nonconstant
policies are changed by an unmatched swap, exactly as the stabilizer criterion
of `HC-DU-204` predicts.

# Three-mechanism selector tournament

The mechanisms are compared under the unchanged complete-handoff passport.
No score is assigned for merely inserting the desired controller into the
antecedent.

## 1. Source-action and QND stability

`HC-DU-040D` is the strongest positive already in the repository. Within a
frozen informative binary-QND candidate class, exact preservation of the
source action selects the source-aligned record axis up to outcome relabeling.
Approximate preservation gives a quantitative alignment bound.

But the same effects, immediate repeatability, archive values, and central
source nondisturbance admit a Lüders continuation and an outcome-conditioned
internal twist whose selected outputs are orthogonal. A richer within-sector
action algebra can reject the twist, but that algebra is an additional
antecedent.

**Disposition:** `PRODUCER_ORBIT_PARTIALLY_SELECTED; CONSUMER_OPEN`.

This is closest to a local theorem because it already selects one side of the
handoff. Repeating another pointer-axis or QND host has no value unless a new
physical law couples the write and read actions.

## 2. Finite-time infrared memory

`HC-DU-068` finds genuine partial physical typing. QED and perturbative
gravity produce soft carrier structure; within a supplied time frame and
rotation subgroup, part of the dressing is conditionally selected.

The finite operational record remains unselected. Detector worldtube,
duration, resolution, local instrument, blank archive, provenance, decoder,
action class, and held-out inverse target remain supplied or missing. The
physical resolution indexes a family of observer quotients rather than
choosing one.

**Disposition:** `CARRIER_PARTIALLY_SELECTED; WRITE_AND_CONSUMER_OPEN`.

The route remains high-ceiling field physics, but it fails earlier than the
QND route on the handoff passport.

## 3. Direct action

`HC-DU-115/126` show that a direct-action or source-effective description can
carry a complete response relation for the frozen source-query class. Exact
mediator elimination preserves that response.

The same source kernel has inequivalent mediator and absorber
factorizations. It therefore does not select a channel/event partition,
mediator-local record, archive, or downstream action. RTI proposes an
absorber-triggered actualization, but the audited trigger remains conditional
and contested rather than an earned normalized selector.

**Disposition:** `SOURCE_RELATION_SELECTED_AFTER_THEORY_CHOICE;
EVENT_AND_CONSUMER_OPEN`.

Direct action remains the most ontologically disruptive branch, but it does
not presently supply the complete handoff DU needs.

# Embodied-relation control

`HC-DU-175` prevents an overcorrection. A consumer does not always require a
portable classical label. Reusing one stable interaction can embody the
relational reference for a bounded prepare-and-invert capability.

That construction is exactly reversible and contains no retained occurrence
record, provenance archive, observer access boundary, or public certificate.
It proves:

```text
action-relative capability can exist without a record token.
```

It does not prove:

```text
a selected stable interaction is a selected record handoff.
```

This is why the missing law must be allowed to select a relation rather than
an explicit controller label, while still satisfying the material formation
and provenance receipts when a record claim is made.

# Strongest absorber and novelty boundary

The mathematics is occupied:

- classical structures copy and delete basis data;
- controlled operations support arbitrary record-conditioned actions;
- quantum instruments include outcome and conditional state change;
- instrument post-processing studies conditional later instruments and their
  equivalence classes
  ([Leppäjärvi and Sedlák](https://arxiv.org/abs/2010.15816));
- quantum combs and supermaps type composed operations; and
- automata, coding, feedback control, and realization theory distinguish a
  symbol alphabet from its transition/action semantics.

Therefore `HC-DU-205` is not claimed as new mathematics. Its useful increment
is the cross-mechanism physical selector frontier:

> The current candidates select complementary pieces—stable alphabet,
> carrier, or source relation—but none supplies the cross-boundary law that
> turns formed distinctions into one selected action-bearing handoff.

# Grade, stop, and exact reopener

- **Grade 4:** exact consumer-freedom and inverse-write nonselection
  boundaries, plus unchanged-passport source-grounded tournament.
- **Not earned:** a full handoff selector, universal impossibility theorem,
  regional composition, empirical excess, new physics, or ontology priority.
- **Stop:** no more pointer-axis, quotient, relabeling, inverse-write,
  metastable-host, IR-detector, or direct-action factorization variants absent
  a new cross-boundary physical premise.
- **Reopen:** one independently motivated action, conservation law, symmetry,
  interaction, or variational principle must select a writer-consumer pair or
  matched orbit target-blindly; deleting that premise must restore physically
  distinct consumers. The complete formation, provenance, archive, access,
  resource, intervention, and held-out capability packet must descend without
  refit.

Only after that local selector exists should DU ask whether several handoffs
compose into regional certified reality.

# Executable receipt

`tests/du_record_action_selector_frontier_probe.py` verifies:

1. exact reversibility of the binary writer;
2. commutation of every conditional consumer with the sharp record algebra;
3. one formed record and four distinct target capabilities;
4. inverse-write erasure without consumer selection;
5. matched-label descent and unmatched stabilizer regression; and
6. consistency with the banked QND, infrared-memory, direct-action, and
   embodied-relation evidence.

Passing validates only these finite and artifact-consistency boundaries.
