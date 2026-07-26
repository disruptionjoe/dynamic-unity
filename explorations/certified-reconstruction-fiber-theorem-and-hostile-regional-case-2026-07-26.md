---
title: "Certified reconstruction fibre theorem and hostile regional case"
date: 2026-07-26
status: completed_scoped_cross_platform_theorem
doc_type: exact_typed_theorem_and_minimum_counterexample
run_id: RUN-20260726-103543-typed-reconstruction-unification
claim_grade: "EXACT SET-THEORETIC RECONSTRUCTION THEOREM + INCLUSION-MINIMAL BINARY REGIONAL COUNTEREXAMPLE / COMPONENT MATHEMATICS KNOWN / NO PHYSICAL COMPLETENESS, ONTOLOGY, NEW LAW, OR PAPER PROMOTION"
candidate_ids:
  - HC-DU-039A
related_ids:
  - HC-DU-034
  - HC-DU-035C
  - HC-DU-036C
  - HC-DU-038B
lanes:
  - lane_1
  - lane_5
  - lane_6
  - lane_7
  - lane_A
channels:
  - CH-FORMAL
  - CH-MODEL
  - CH-COLLIDE
probe_ref: tests/du_certified_reconstruction_fiber_probe.py
artifact_ref: tests/artifacts/du_certified_reconstruction_fiber_result.json
---

# Certified Reconstruction Fibre Theorem

## Result in plain English

One reconstruction framework does survive the multi-time process,
conformal-geometry, and layered-regional-finality specimens, but only after
one correction:

> Before asking whether all models compatible with a record predict the same
> held-out result, first ask whether the record has any admissible model at
> all.

The resulting three scientific branches are:

1. **unrealizable record** — the supplied local records, identities, and
   completion class admit no joint completion;
2. **target reconstruction** — at least one completion exists and every
   completion predicts the same declared target; or
3. **target underdetermination** — at least two completions share the record
   and predict different target values.

This distinction matters because target constancy is vacuously true on an
empty completion fibre. A reconstruction theorem that checks only constancy
would therefore call an inconsistent record bundle a success.

The minimum hostile regional case is exact and small:

\[
A=B,\qquad B=C,\qquad C\ne A
\]

with uniform binary pair records. Every pair table is normalized, all
singleton overlap marginals agree, and every one-context deletion has a
global completion. The full three-context cycle has none. Exact search finds
no smaller inconsistent simple binary pair-context cover.

The same framework correctly classifies the other two specimens:

- the ordinary endpoint record does not reconstruct the held-out causal
  break of the multi-time process, while the independently formed
  intermediate record transcript does; and
- one regional volume does not reconstruct the remote clock, two volumes do
  inside the frozen two-mode conformal family, and the hostile smooth mode
  reopens underdetermination in the enlarged class.

The important additional result is about repairs:

> Adding information within the same completion class can split a nonempty
> fibre. It cannot make an empty fibre nonempty. If provenance or context
> splitting restores a process after a regional obstruction, the operation
> changed the occurrence-identity or completion type; it was not an ordinary
> record refinement.

The executable check passes `12/12` exact controls. The mathematics is
standard factorization, fibre, and marginal-consistency terrain. The gain is
a common Dynamic Unity typing and a sharper boundary among reconstruction,
remainder candidates, incompatibility, and contract repair.

## 1. One typed framework

A **certified reconstruction contract** is

\[
\mathfrak R=(M,Q,Y,r,t,q;\mathcal I,\mathcal G),
\]

where:

| type | meaning |
|---|---|
| \(M\) | the frozen admissible completion or model class |
| \(Q\) | the typed certified-record alphabet |
| \(Y\) | the typed held-out observable, response, or action alphabet |
| \(r:M\to Q\) | the record map |
| \(t:M\to Y\) | the target map |
| \(q\in Q\) | the declared observed record |
| \(\mathcal I\) | frozen occurrence, provenance, and overlap identities used to define \(M\) and \(r\) |
| \(\mathcal G\) | declared gauge or benign-refinement identifications |

Formation, access, target independence, resources, and physical admissibility
remain premises attached to these types. The theorem does not manufacture
them.

Define the completion fibre

\[
F_q=r^{-1}(q)=\{m\in M:r(m)=q\}.
\]

The order of adjudication is:

```text
freeze M, Q, Y, r, t, q, identity, gauge, access and resources
    -> test whether F_q is nonempty
    -> only then test whether t is constant on F_q
    -> return a same-record/different-target witness when it is not
```

If any required type is unfrozen, the result is `INCOMPLETE_CONTRACT`,
which is non-adjudication rather than a fourth scientific branch.

## 2. The common theorem

### Theorem 1 — realizability-first reconstruction trichotomy

For every complete certified reconstruction contract and declared record
\(q\), exactly one holds:

1. \(F_q=\varnothing\), returning `UNREALIZABLE_RECORD`;
2. \(F_q\ne\varnothing\) and \(|t(F_q)|=1\), returning
   `RECONSTRUCTS_TARGET`; or
3. \(F_q\ne\varnothing\) and \(|t(F_q)|\ge2\), returning
   `UNDERDETERMINED_TARGET` with
   \(m_0,m_1\in F_q\) such that \(t(m_0)\ne t(m_1)\).

#### Proof

The fibre is empty or nonempty. If nonempty, its target image is a nonempty
set and therefore has either one element or at least two. These cases are
pairwise disjoint and exhaustive. In the last case, choosing elements with
two distinct target values gives the witness. \(\square\)

This elementary theorem is intentionally weaker than a physical
reconstruction claim. Its force is that it prevents an invalid inference at
the exact point where local regional records differ from the other two
specimens.

### Theorem 2 — kernel/factorization criterion on realized records

There exists a decoder

\[
\bar t:\operatorname{im}r\to Y
\]

such that

\[
t=\bar t\circ r
\]

exactly when

\[
\ker r\subseteq\ker t,
\]

meaning

\[
r(m_0)=r(m_1)\Longrightarrow t(m_0)=t(m_1).
\]

#### Proof

If \(t=\bar t\circ r\), equal records have equal decoded targets. Conversely,
if \(t\) is constant on every record fibre, define
\(\bar t(q')=t(m)\) for any \(m\) satisfying \(r(m)=q'\). Fibre constancy
makes this definition independent of the representative. \(\square\)

This criterion applies only on \(\operatorname{im}r\). It says nothing about
a proposed record outside that image. That is precisely why Theorem 1 must
test existence first.

### Theorem 3 — refinement cannot resurrect an empty fibre

Let \(r_2:M\to Q_2\) refine \(r_1:M\to Q_1\) on the same completion class:

\[
r_1=\pi\circ r_2
\]

for some projection \(\pi:Q_2\to Q_1\). Then for every \(q_2\in Q_2\),

\[
r_2^{-1}(q_2)
\subseteq
r_1^{-1}(\pi(q_2)).
\]

Therefore:

1. a refinement may split a nonempty coarse fibre and make the target
   constant;
2. if a coarse fibre is empty, every fine fibre projecting to it is empty;
   and
3. a proposed “repair” that turns an empty coarse fibre into a nonempty one
   must change \(M\), \(\pi\), the occurrence identity \(\mathcal I\), or
   another contract type.

#### Proof

If \(m\in r_2^{-1}(q_2)\), then

\[
r_1(m)=\pi(r_2(m))=\pi(q_2),
\]

so \(m\in r_1^{-1}(\pi(q_2))\). The consequences follow immediately.
\(\square\)

This is the exact difference between adding a useful record and correcting a
false gluing assumption.

## 3. Unchanged application to the multi-time specimen

Use the two frozen completions from the existing QND-parity control:

1. the recorded process forms and retains
   \(r_{AB}=A\oplus B\) and \(r_{BC}=B\oplus C\); and
2. the endpoint rival directly computes \(A\oplus C\).

For all eight binary inputs, both produce the same ordinary endpoint table:

\[
r_{AB}\oplus r_{BC}=A\oplus C.
\]

Take that complete no-break table as \(q\). Take the response after a
predeclared primitive reset as \(t\). The recorded process retains the old
parities; the endpoint rival returns the reset value. Their held-out tables
differ on exactly four of eight inputs.

The common classifier returns:

```text
ordinary endpoint record
    -> nonempty two-model fibre
    -> different held-out causal-break tables
    -> UNDERDETERMINED_TARGET
```

Now add the independently formed intermediate instrument transcript to the
record. This is a same-class refinement: forgetting the transcript recovers
the endpoint record. The refined fibre containing the recorded process is a
singleton and returns `RECONSTRUCTS_TARGET`.

This is not a new process-tensor result. It is an exact translation of the
existing multi-time control into the common reconstruction type.

## 4. Unchanged application to conformal geometry

Use the existing static \(1+1\) conformal arena

\[
g_u=u(x)(-dt^2+dx^2).
\]

### One volume

Flat space and the exact rival

\[
(a,b)=\left(\frac1{10},-\frac25\right)
\]

share the left regional volume \(V_L=1\), while their held-out right-clock
values are

\[
\tau_R^2=1
\quad\text{and}\quad
\tau_R^2=\frac35.
\]

The fibre is nonempty and target-nonconstant:
`UNDERDETERMINED_TARGET`.

### Two volumes

Adding the overlapping regional volume \(V_Q\) is an ordinary same-class
refinement. Its two-mode measurement matrix has

\[
\det A=\frac3{64}\ne0.
\]

The full declared two-mode family therefore has singleton training fibres,
and the held-out clock factors through \((V_L,V_Q)\):
`RECONSTRUCTS_TARGET`.

### Enlarged smooth completion class

The hostile mode

\[
h(x)=(x+1)(1-3x-6x^2+10x^3)
\]

preserves total volume, both training volumes, and the anchored left clock,
but changes

\[
\tau_R^2:1\longmapsto\frac{26}{25}
\]

and produces nonzero center curvature. Enlarging \(M\) therefore reopens a
nonempty target-disagreeing fibre:
`UNDERDETERMINED_TARGET`.

This separates two operations that are often blurred:

- adding a record refines fibres inside one \(M\); and
- adding a physically admitted mode enlarges \(M\) and can reopen a
  previously reconstructed target.

## 5. Hostile application to layered regional finality

Consider three uniform binary pair records:

\[
\begin{aligned}
p_{AB}(a,b)&=\frac12\,\mathbf 1[a=b],\\
p_{BC}(b,c)&=\frac12\,\mathbf 1[b=c],\\
p_{CA}(c,a)&=\frac12\,\mathbf 1[c\ne a].
\end{aligned}
\]

Each pair table is normalized. Every singleton marginal is uniform, so all
overlap-probability checks pass.

Any global distribution reproducing these tables would assign weight only
to assignments satisfying

\[
a\oplus b=0,\qquad b\oplus c=0,\qquad c\oplus a=1.
\]

But XORing the three left-hand sides gives zero for every assignment, while
the right-hand sides XOR to one. Hence no global assignment is available for
the support of such a distribution, and the completion fibre is empty.

The exact local search:

- searches simple binary pair-context covers in increasing size, with a
  four-variable search bound;
- enumerates every edge-parity labeling;
- enumerates every global binary assignment; and
- requires every one-context deletion to reproduce its remaining uniform
  pair tables.

Its first obstruction has three variables and three contexts. Every proper
deletion has a two-assignment uniform global extension. The fixture is thus
inclusion-minimal in the declared simple binary pair-context class.

### The counterexample to the weaker unification

A constancy-only criterion computes

\[
|t(F_q)|\le1
\]

and returns true when \(F_q=\varnothing\). It would label this frustrated
regional record “reconstructive,” despite there being no admitted world in
which the record exists.

The realizability-first theorem returns `UNREALIZABLE_RECORD`. The upper
action must not be reconstructed from that bundle. A layered finality system
may safely reject the composition, revise the overlap identity, or declare
the completion class incomplete.

### Why provenance splitting is not ordinary refinement

Replacing \(A,B,C\) by route- or context-indexed occurrences such as
\(A@AB\) and \(A@CA\) restores a product extension. But Theorem 3 shows that
no same-\(M\) refinement could make the empty fibre nonempty.

The successful lift changed the cross-context occurrence identity and hence
the completion type. Its correct classification is:

```text
CONTRACT_RETYPE_NOT_SAME_CLASS_REFINEMENT
```

That repair may be physically warranted by formed provenance. It is not
evidence that the original coarse record reconstructed anything.

## 6. What the three specimens now say together

The common theorem yields a sharper reconstruction surface:

| completion fibre | target image | scientific meaning | permitted next move |
|---|---|---|---|
| empty | empty | incompatible record/identity/completion contract | reject, retype, or complete the contract |
| nonempty | singleton | target reconstruction in the frozen class | test physical warrant and held-out transfer |
| nonempty | multiple values | target underdetermination / finite remainder candidate | find a formed refinement or defend the remainder class |

This changes how absorbers are recorded:

1. **Record refinement** adds formed/accessed information within one model
   class and can resolve underdetermination.
2. **Completion enlargement** adds admitted models and can reopen a
   reconstructed target.
3. **Identity or contract retyping** changes which local occurrences may be
   glued and can turn an inconsistent contract into a realizable one.

These are mathematically different. Calling all three “add the missing
variable” loses the exact reason a result changed.

## 7. Consequence for the North Star

The North Star remains unchanged, but its reconstruction obligation is now
ordered:

```text
physical formation and typed occurrence identity
    -> nonempty admissible completion fibre
    -> target constancy or a same-record/different-target witness
    -> resource-accounted same-class refinement
       OR explicitly charged completion/identity retyping
    -> physical completeness and ontology adjudication
```

In particular:

- an empty fibre is not a physical remainder;
- a contextual or marginal obstruction is not by itself missing physics;
- a positive factorization result applies to realized record values and a
  declared completion class;
- provenance can correct the contract without becoming a new physical
  degree of freedom; and
- layered regional finality contributes an admissibility obligation that the
  process and geometry cases can hide because their records were generated
  from admitted models by construction.

This is the most important research learning from the swing.

## 8. Collision and earned grade

The ingredients are occupied:

- factorization through fibres and quotient maps is elementary set/category
  theory;
- finite sufficient-statistic and behavioral-congruence criteria already
  use the same kernel inclusion;
- cyclic marginal obstruction, contextuality, database join consistency,
  and sheaf global-section failure already cover the hostile triangle; and
- finite inverse-problem rank/nullspace and process-tensor multi-time
  distinctions already cover the specimen mathematics.

The result is therefore not promoted as a novel theorem in the literature.
Its exact earned contribution is programmatic:

> one unchanged, realizability-first reconstruction type now spans the three
> specimens, and it proves that same-class refinement, completion
> enlargement, and identity retyping must not be merged.

`HC-DU-039A` is a scoped three-specimen result, not completion of
`HC-DU-039`'s broader quantum/distributed/causal-set/QFT invariance target.

## 9. Local-model learning receipt

| field | result |
|---|---|
| admission | `ADMIT_LOCAL_LEARNING_BUILD` |
| research-only baseline | standard fibre factorization and known cyclic marginal obstructions |
| generated local delta | the minimum exact DU hostile fixture exposes vacuous constancy and the refinement/retyping boundary |
| generated-not-encoded control | simple covers and parity labels were searched in increasing size; every assignment and one-context deletion was enumerated through the first obstruction; no verdict was inserted |
| checkpoint | `REALIZABILITY_FIRST_COMMON_THEOREM_WITH_MINIMUM_HOSTILE_CASE` |
| decision consequence | install realizability before reconstruction and type provenance repair as contract retyping |
| stop | `STOP_EXACT_BOUNDARY_EARNED` |
| hardware | none; external hardware cannot strengthen this formal boundary |

The deterministic artifact SHA-256 is
`4660ed3c383f81806f15f213300dededf6c3ce8de2b3608e022065ac1406c751`.

## 10. Stops and next reopener

Do not claim:

- record-first ontology from target factorization;
- physical impossibility from an empty fibre under a poorly warranted
  identity or completion class;
- physical remainder from regional inconsistency;
- an ordinary refinement when occurrence identity or \(M\) changed;
- universal geometry from the two-mode positive case;
- theorem novelty for the common fibre result; or
- completion of the five-platform `HC-DU-039` target.

The next high-value use is not another synthetic example. It is to make every
active reconstruction assay report these two receipts separately:

1. **realizability receipt:** why the certified record lies in the image of
   the admitted physical record map; and
2. **sufficiency receipt:** why the declared target is constant on that
   nonempty fibre, or the exact witness proving otherwise.

Only after that retrofit should a physical specimen be escalated.
