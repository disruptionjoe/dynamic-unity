---
title: "Certified Causal Reconstruction formal spine and two-anchor freeze"
status: executed_scoped_result
date: 2026-07-26
run_id: RUN-20260726-144910-certified-causal-spine
lanes:
  - lane_1
  - lane_3
  - lane_5
  - lane_7
channels:
  - CH-FORMAL
  - CH-COLLIDE
  - CH-MODEL
  - CH-EMPIRICAL
claim_grade: "EXACT FINITE QUOTIENT SPECIALIZATION / COMPONENT MATHEMATICS KNOWN / INTEGRATED ASSURANCE SPINE ONLY"
convergence_outcome: KNOWN_MATHEMATICS__INTEGRATED_ASSURANCE_ONLY
---

# Certified Causal Reconstruction formal spine and two-anchor freeze

## Result in one sentence

Dynamic Unity now has one exact finite condition that can be used unchanged on
a multi-time quantum-instrument shadow and an authenticated distributed-process
shadow:

> A record is an autonomous controlled state exactly when every complete
> acquisition-stratum, response, and next-record probability is unchanged
> between histories carrying that record, under every admitted action.

The theorem is controlled strong lumpability or probabilistic bisimulation in
typed Dynamic Unity form. It is not a new theorem or a physical law. Its value
is that it closes the formal-first uncertainty, prevents several recurrent
false positives, and makes **physical record formation and interface
selection** the next scientific bottleneck.

The exact probe passes `19/19`:

- [probe](../tests/du_certified_causal_spine_probe.py)
- [artifact](../tests/artifacts/du_certified_causal_spine_result.json)

## What was frozen

The result applies only after freezing:

| Type | Frozen object |
|---|---|
| `H` | finite admitted residual histories, completions, implementations, or adversary/scheduler states |
| `A` | intervention and continuation actions |
| `S` | every acquisition stratum, including accepted, rejected, invalid, missing, and no-click rows |
| `Y` | response or complete selective-continuation target |
| `R` | independently declared candidate record |
| `G` | representation, gauge, and occurrence-identity relation |
| `C` | target-independent admissible refinement class |
| `L` | resource partial order |
| `B` | reset or causal-break scope over every admitted retained memory |
| `T` | held-out target or tester family |

Changing these after seeing the result is contract retyping or refitting, not a
repair earned by the original record.

## Exact finite theorem

### Stochastic controlled form

Let \(H\), \(A\), \(S\), \(Y\), and \(Q\) be finite. Let

\[
K_a(s,y,h'\mid h)
\]

be a normalized controlled selective kernel and let

\[
r:H\to Q
\]

be a deterministic record.

The record has a well-defined autonomous controlled quotient if and only if,
for every pair \(h_0,h_1\) with \(r(h_0)=r(h_1)\), action \(a\), stratum
\(s\), response \(y\), and next-record class \(q'\),

\[
\boxed{
\sum_{z:r(z)=q'} K_a(s,y,z\mid h_0)
=
\sum_{z:r(z)=q'} K_a(s,y,z\mid h_1).
}
\]

When this holds, define

\[
\bar K_a(s,y,q'\mid q)
=
\sum_{z:r(z)=q'}K_a(s,y,z\mid h)
\]

for any \(h\) with \(r(h)=q\). The equality makes this independent of the
chosen representative.

### Proof

**Necessity.** If a quotient kernel exists, every hidden state carrying
record \(q\) must induce the same quotient row
\(\bar K_a(\cdot,\cdot,\cdot\mid q)\). The displayed equality follows.

**Sufficiency.** The displayed equality makes \(\bar K\) well-defined. Apply
the chain rule and sum over hidden states after each action. Induction on the
action word proves that the distribution of every finite
\((s,y,q')\)-labelled record trace depends only on the starting record.
Because the trace law agrees at every branch, the result also covers policies
that choose the next action from the observed trace.

### Linear form

Let \(V\) be the finite-dimensional real space spanned by \(H\), with record
map \(R:V\to W\), complete selective response maps

\[
J_a=\bigoplus_{\sigma\in\Sigma_a}J_{a,\sigma},
\]

and admitted residual-continuation maps \(C_c:V\to V\). The equivalent kernel
conditions are

\[
\ker R\subseteq\ker J_a
\quad\text{for every }a,
\]

and

\[
C_c(\ker R)\subseteq\ker R
\quad\text{for every }c.
\]

They are equivalent to unique maps on the realized quotient
\(\operatorname{im}R\):

\[
J_a=\bar J_aR,
\qquad
RC_c=\bar C_cR.
\]

For stochastic record channels, positivity of a decoder on the full raw
record alphabet must be checked. For quantum channels, complete positivity
and extension outside the realized image must also be checked. Kernel
inclusion alone supplies only a linear decoder on the realized quotient.

## The crucial qualification

There are two different questions:

1. **Predictive sufficiency for a frozen tester family.** Can all declared
   response traces be decoded from the record?
2. **Autonomous record state.** Can the record itself be updated recursively
   under every admitted continuation?

The theorem above is necessary and sufficient for the second. It is
sufficient but not generally necessary for the first.

For one frozen response family, predictive sufficiency is ordinary
Blackwell/statistical-experiment factorization:

\[
K^\star=D\circ R,
\]

where \(K^\star\) bundles the declared tester outcomes. A process may be
predictively sufficient for that family even when hidden states inside one
record class evolve differently in ways the family never observes.

Dynamic Unity needs the stronger autonomous form whenever later records,
regional composition, selective continuation, reset, or capability depend on
the quotient as a state. The distinction prevents us from calling a useful
terminal statistic a complete causal record.

## Why the joint selective row is load-bearing

It is not enough to check:

- the marginal stratum/response distribution; and
- the marginal next-record distribution.

Those two marginals can agree while their correlation differs. The smallest
exact stochastic control uses three states. Histories \(h_0,h_1\) share record
\(q_0\), and \(v\) has record \(q_1\):

\[
\begin{aligned}
h_0 &: \tfrac12(s_0,y_0,h_0)+\tfrac12(s_1,y_0,v),\\
h_1 &: \tfrac12(s_0,y_0,v)+\tfrac12(s_1,y_0,h_1).
\end{aligned}
\]

Both histories have the same event marginal and the same next-record
marginal. The full \((s,y,q')\) rows are different. A later readout exposes
the difference.

Use subnormalized joint stratum blocks. Dividing by a selection probability
can erase zero-support strata and makes accepted-only equality look stronger
than it is.

## Exact hostile controls

| Failure | Smallest or canonical control | What it prevents |
|---|---|---|
| Endpoint without continuation | Three deterministic states with record partition `(q0,q0,q1)`; the two `q0` states emit the same current response but transition into different next-record classes. Exhaustive two-state search finds no witness. | Calling current output factorization a multi-time theorem. |
| Weak stochastic marginals | The three-state half/half construction above. | Replacing the joint selective row by separate marginals. |
| Returned-only visibility | Two histories have the same acceptance probability and accepted response but different rejected responses. | Inferring the complete attempted process from returned rows. |
| Hidden reset memory | A system reset maps `(x,m)` to `(0,m)`; a later recoupling reveals `m`. A complete reset maps both to `(0,0)`. | Calling a system-only causal break a complete reset. |
| Empty fibre | An observed record outside `im R` makes target constancy vacuous. | Treating unrealizability as reconstruction. |
| Target-coded repair | Appending the held-out target makes the finite quotient exact by construction. | Treating target-fitted completion as record formation. |
| Representation-sensitive selector | Two admitted faithful encodings reverse the selected candidate. | Treating a representation-dependent ranking as physical selection. |

### Witness bounds

Failure of the displayed selective-lumpability condition already gives a
one-action witness:

\[
(q,h_0,h_1,a,s,y,q').
\]

For deterministic response-only behavioral equivalence, partition refinement
gives a separating word of length at most

\[
|H|-b_0,
\]

where \(b_0\) is the number of initial observable blocks. In finite linear,
stochastic, or quantum presentations, the safe general replacement is a
reachable-rank bound, at most \(\dim V-1\) for a fixed detectable residual
direction. No witness-length claim survives without a frozen finite state,
horizon, or rank bound.

## Two unchanged anchors

The same fields and decision rule were used on both specimens.

| Field | Quantum-instrument anchor | Authenticated distributed-process anchor |
|---|---|---|
| Hidden residual `H` | QND versus flip-after-record implementation and source bit | metastable-final versus BFT-hardened-final residual, plus pending state |
| Base record `R` | immutable archive value | public endpoint value |
| Held-out action | repeat the measured system | introduce an authenticated late conflict |
| Base result | same archive, different repeat response | same public endpoint, different reopen/hold behavior |
| Admissible refinement | complete selective-instrument receipt | authenticated operation-DAG/layer provenance |
| Refined result | autonomous finite quotient | autonomous finite quotient |
| Evidence grade | exact finite classical shadow of standard measure-and-prepare instruments | exact finite authenticated protocol shadow |

Both specimens therefore instantiate one operational theorem without
semantic refitting. Neither is a hardware experiment, a complete quantum
process theorem, or a physical remainder.

The two minimum discriminators are:

- quantum: one `repeat_system` continuation;
- distributed: one authenticated `late_conflict` continuation.

Within each explicitly finite candidate class, the declared independent
refinement is resource-Pareto-minimal. That statement does not establish a
unique or minimal repair in an unrestricted physical class.

## Prior-art collision

The mathematical core is occupied:

- [Blackwell, “Equivalent Comparisons of Experiments”](https://doi.org/10.1214/aoms/1177729032)
  absorbs restricted-family experiment sufficiency and garbling;
- [Larsen and Skou, “Bisimulation through Probabilistic Testing”](https://doi.org/10.1016/0890-5401(91)90030-6)
  and finite strong lumpability absorb the autonomous labelled quotient;
- [Chiribella, D'Ariano, and Perinotti, “Theoretical Framework for Quantum Networks”](https://doi.org/10.1103/PhysRevA.80.022339)
  and [Pollock et al., “Non-Markovian Quantum Processes”](https://doi.org/10.1103/PhysRevA.97.012127)
  absorb complete multi-time quantum process and tester composition;
- [Pollock et al., “Operational Markov Condition for Quantum Processes”](https://doi.org/10.1103/PhysRevLett.120.040405)
  and instrument-specific quantum Markov-order work absorb ordinary
  intervention-conditioned memory questions; and
- finite realization, observability, Moore--Nerode refinement, and system
  identification absorb the rank and bounded-witness machinery.

The bounded collision did not locate one source that combines every DU
assurance obligation. That absence is `NOT_LOCATED_SEARCH_INCOMPLETE`, not a
novelty claim.

## The retained Dynamic Unity contribution

The useful survivor is an integrated assurance contract:

1. freeze the observer and record before held-out targets;
2. test record realizability before target constancy;
3. retain every acquisition stratum;
4. retain the joint subnormalized selective continuation, not only terminal
   values or normalized selected rows;
5. admit only target-independent, physically formed refinements with
   provenance and resource vectors;
6. verify reset over every admitted retained memory while preserving the
   intended archive until readout;
7. require results to descend across the admitted representation/gauge class;
8. distinguish a recursive autonomous quotient from sufficiency for a finite
   tester family; and
9. return a typed result:
   `BASE_QUOTIENT`, `PARETO_REPAIR`, `CLASS_RELATIVE_FAILURE`,
   `UNREALIZABLE`, `INCONCLUSIVE`, or `INCOMPLETE_CONTRACT`.

With finite data, exact equality is unavailable. The empirical successor must
report calibrated \(\varepsilon\)-sufficiency or a positive insufficiency
margin, including leakage, drift, selection, reset, SPAM/gauge, and joint
systematic allowances.

## What changed

Before this swing, the formal-first route was still a live novelty and theorem
uncertainty. It is now closed at the correct grade:

- the exact recursive quotient theorem is known mathematics;
- the selected/rejected and continuation requirements are jointly necessary
  for an autonomous record state;
- the quantum and distributed anchors share one schema;
- the smallest deterministic and stochastic failure modes are frozen; and
- no hardware is required to learn anything further about this formal
  question.

This is a scientific advance because it tells the program what **not** to
confuse with the North Star. More synthetic factorization fixtures, platform
analogies, or provider adapters will not improve the formal result.

## Campaign decision

Swing 1 succeeds as a formal and assurance spine, not as a novel theorem.

The next swing should attack the newly isolated uncertainty:

> Which candidate record, selective interface, archive, provenance field,
> reset boundary, and admissible refinement is independently formed or
> selected by the physical process—and which remains supplied, fitted, or
> representation-dependent?

That is a Lane-3 physical formation/interface-selection problem. It should
begin with the existing conservation/asymmetry and stabilizer no-gos, use the
formal spine as its acceptance test, and stay local until a specific physical
question is proved to require external hardware.

## Claim boundary

This swing establishes:

- one exact finite autonomous-record quotient specialization;
- a proof and exact counterexample suite;
- one unchanged two-platform operational typing; and
- the assurance contract that later physical work must satisfy.

It does **not** establish:

- a physically privileged record;
- physical formation or selection of either repair;
- a complete quantum or QFT process result;
- a physical remainder;
- record-first ontology;
- a novel theorem, physical law, prediction, or new physics;
- paper promotion; or
- any need for external hardware.
