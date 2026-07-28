---
title: "Record-graph settlement and delayed-activation nonidentifiability"
status: completed_scoped_result
doc_type: cross_repo_reopener_audit_and_exact_activation_absorber
created: 2026-07-28
run_id: RUN-20260728-164506-record-graph-activation-absorber
work_id: RGAA-RECORD-GRAPH-ACTIVATION-ABSORBER
program_id: CCR-PREDICTIVE-SELECTION-TO-FORECASTING-ISSUANCE
authority: "Joe direct chat: Go"
claim_ids:
  - HC-DU-087
claim_grade: "SCOPED GRADE-4 GRAPH-FACTOR NECESSITY AND SOURCE-PREEXISTENCE NONIDENTIFIABILITY / STANDARD FACTORIZATION MATHEMATICS / NO SOURCE ISSUANCE OR NEW PHYSICS"
claim_status_change: "HC-DU-087 banked at scoped grade"
prediction_status_change: none
paper_state_change: none
hardware_state_change: none
current_authority_change: "CURRENT-RESEARCH.yaml revision 38 remains quiescent with no selected successor"
external_input:
  repo: time-as-finality
  revision: 9981cb1
  artifact: explorations/nucleation-ratchet-toy-2026-07-28.md
---

# Settlement can identify the record graph—not whether its types pre-existed

## Executive result

Time as Finality's nucleation-ratchet toy found that its strongest remaining
in-model difference between a "nucleated" arm and an initially declared arm
was a chain-versus-star record graph:

```text
arriving type + consume current head -> chain
initially declared type + consume base -> star.
```

That is a real difference between those two implementations. It is not a
signature of type arrival. The comparison changed two variables together:

1. whether the type was declared before activation; and
2. which consumption-edge rule it used.

`HC-DU-087` supplies the missing hostile arm and the exact theorem.

Put every type in a fixed reservoir at the initial stage, keep it dormant,
and activate it at the same time, with the same variant, weight, record, and
rule:

```text
on activation, consume the current head.
```

The resulting time-indexed weighted record graph is identical to the
nucleated arm. Every settlement quantity computed from that graph is
therefore identical. A completed-history model can make the construction
even stronger by fixing the entire activation and variant sequence at the
initial stage.

The corrected attribution is:

```text
attainability equality       <- conservative extension law
defect structure             <- local variant selection + contact rule
settlement-price difference  <- weighted consumption graph
type pre-existence           <- not identified by any of the above
source issuance              <- not established
```

The Time as Finality result remains useful. It locates where path dependence
is carried: provenance-bearing consumption edges can change later settlement
without changing old-task attainability. Dynamic Unity's correction is that
record-graph path dependence identifies neither source-side type creation nor
the absence of a fixed generator.

## 1. Scope and warrant

| label | content | role |
|---|---|---|
| `EXTERNAL_INPUT_VERIFIED` | TaF's three-arm toy and its reported split outcomes | motivates the question; does not set DU's grade |
| `STANDARD` | graph isomorphism, reachability, factorization through a statistic | exact proof engine |
| `PROJECT_NATIVE` | source type, activation, formed record, provenance edge, settlement, access, and capability remain distinct | DU typing |
| `IMPORTED_CONTROL` | Temporal Issuance's stage-0 fixed-oracle/completed-history absorber | hostile control only |

The theorem does not assume that the world is a graph. It concerns any
proposed settlement observable that is explicitly defined as a functional of
the formed weighted record graph.

## 2. The complete settlement object

At stage \(t\), let

\[
G_t=(V_t,E_t,\lambda_t,c_t)
\]

be the accessible record graph:

- \(V_t\) is the set of formed record occurrences;
- \(E_t\subseteq V_t\times V_t\) is the consumption/provenance relation;
- \(\lambda_t\) contains the retained record labels needed by the declared
  interface; and
- \(c_t:V_t\to\mathbb R_{\ge0}\) contains the declared physical prices or
  weights.

TaF's un-commit price is an example. If \(D_t(r)\) is the downstream closure
of record \(r\), then

\[
W_t(r)=\sum_{v\in D_t(r)}c_t(v).
\]

The factor \(1/\ln 2\) and any declared Landauer floor can be included in
\(c_t\); they do not change the argument.

Other declared settlement grades are functions of \(W_t(r)\), the agent
class, and its fixed resource envelope. They therefore also factor through
the weighted graph and the separately supplied agent class.

## 3. `HC-DU-087A` — weighted-graph factorization

### Theorem

Let two source models \(M\) and \(M'\) induce time-indexed accessible record
graphs \(G_t\) and \(G'_t\). Suppose that for every \(t\) there is an
isomorphism

\[
\phi_t:G_t\overset{\cong}{\longrightarrow}G'_t
\]

preserving occurrence labels admitted by the interface, edge direction, and
weights, and that these isomorphisms commute with stage restriction.

Then every settlement observable

\[
S_t=\Phi(G_{\le t})
\]

defined only from that time-indexed record process has the same value in the
two models, up to the declared relabeling.

### Proof

The isomorphisms preserve every argument supplied to \(\Phi\). Hence

\[
\Phi(G_{\le t})=\Phi(G'_{\le t})
\]

after transport by \(\phi_t\). For the un-commit price specifically,
\(\phi_t\) preserves directed reachability and weights, so it maps
\(D_t(r)\) bijectively to \(D'_t(\phi_t r)\), giving

\[
W_t(r)
=
\sum_{v\in D_t(r)}c_t(v)
=
\sum_{v'\in D'_t(\phi_t r)}c'_t(v')
=
W'_t(\phi_t r).
\]

Any grade computed from this price and the same agent class is therefore
equal. \(\square\)

### Boundary

This is a sufficiency theorem for the declared settlement functional. It does
not show that the record graph contains all physical structure, that its
interface is selected, or that every possible future intervention factors
through it.

## 4. `HC-DU-087B` — the delayed-activation absorber

Consider any finite "issuance-labeled" history:

\[
(\tau_j,t_j,v_j,r_j,p_j,c_j)_{j=1}^{n},
\]

where type \(\tau_j\) is said to enter at time \(t_j\), variant \(v_j\) is
selected, record \(r_j\) is formed, \(p_j\) is its consumed parent record,
and \(c_j\) is its weight.

Construct a fixed-reservoir model at the initial stage:

1. the reservoir contains every \(\tau_j\);
2. the activation schedule and variant kernel reproduce \(t_j,v_j\);
3. dormant types are outside the old observer's active task/record interface;
4. the fixed activation rule emits \(r_j\) with weight \(c_j\); and
5. the rule binds its parent to the same \(p_j\)—or, for the ratchet,
   evaluates the fixed expression `current_head_at_activation`.

The two models then generate the same \(G_t\) for every \(t\).

### Corollary

No record-graph settlement statistic distinguishes the claim:

```text
the type did not exist before t_j
```

from:

```text
the type and its activation rule existed, but the type was dormant until t_j.
```

The models differ in a source-side pre-existence variable that the declared
record map does not expose.

### Strong fixed-completion control

The absorber does not require online reselection. A stage-0 completed-history
model can contain the whole finite sequence

\[
(t_j,v_j,p_j,c_j)_{j=1}^{n}
\]

and disclose it one activation at a time. A fixed algorithmic generator can
instead compute the sequence. Ruling out one representation does not rule
out the other.

This is precisely why stochasticity, path dependence, and late appearance
are insufficient for source issuance.

## 5. The missing factorial comparison

The TaF toy coupled type pre-existence and edge rule:

| arm | source type status | activation | consumption edge |
|---|---|---|---|
| `nucleated` | added at activation | stochastic | current head / chain |
| `declared` | present initially | stochastic or canonical | base / star |

The complete attribution grid is:

| source type status | base-parent rule | current-head rule |
|---|---|---|
| present initially | predeclared star | **predeclared chain** |
| added at activation | arriving star | arriving chain |

Holding activation times, variants, record weights, and contacts fixed:

- star versus chain changes settlement;
- canonical versus stochastic variant selection changes defects;
- type pre-existence versus late addition changes neither observable once the
  exposed graph process is matched.

The missing predeclared-chain cell is not a speculative simulation result.
It is the constructive model in Section 4. It uses a fixed conditional edge
rule, which is exactly the strongest legitimate fixed-generator rival.

## 6. Minimum finite witness

Take one base record \(r_0\) and three later records:

\[
r_1\to r_0,\qquad
r_2\to r_1,\qquad
r_3\to r_2,
\]

where the arrow means "consumes" and the weights are \(7,4,3\).

For the chain,

\[
W(r_1)=\frac{7+4+3}{\ln2}
\]

before any additional contact records. For the star, where all three consume
\(r_0\),

\[
W(r_1)=\frac{7}{\ln2}.
\]

The difference is large and real. But both of these constructions are
available whether the three types were:

- declared initially and activated later; or
- added to the active type set at their activation times.

The weighted graph, not source pre-existence, fixes the result.

TaF's larger value shift from approximately \(10.10\) to \(103.87\) has the
same attribution after its defect and contact descendants are included.

## 7. What each observable actually identifies

| observed difference | identified cause at the frozen contract | not identified |
|---|---|---|
| old-task envelope unchanged | conservative task extension | source issuance |
| variant defects | local variant mismatch plus contact/reconciliation rule | type non-preexistence |
| chain/star settlement difference | consumption-edge topology and weights | whether types existed before activation |
| region-final but unshared records | declared local grade plus contact/access graph | first-person ontology |
| delayed activation | activation process | type creation |
| later named type | observer-interface extension | source extension |

The first-person/third-person reading remains a useful operational
decomposition:

```text
local formation != cross-region reconciliation.
```

It is not an ontological result. The same local/shared/gap sets occur in the
fixed-reservoir completion when the record graph is preserved.

## 8. What could distinguish pre-existence from issuance?

At least one source-sensitive object must be added.

### 8.1 Pre-activation intervention

An admitted operation before \(t_j\) might distinguish a dormant type from
its absence. If it succeeds, the type was operationally present relative to
that richer action class. If every admitted pre-activation operation gives
the same response, dormant and absent remain in one response-equivalence
class.

### 8.2 Physical footprint

A dormant type might carry an independently measurable storage, energy,
stress-energy, charge, or boundary cost before activation. This can defeat a
particular fixed-reservoir model. A compact generator or external completion
remains a rival unless the physical completion class excludes it.

### 8.3 Binding commitment

A stage-0 commitment to the type reservoir, later opened with valid
provenance, can establish precommitment relative to its trust and
cryptographic assumptions. Zero-knowledge membership can even certify that a
future type belongs to the committed reservoir without revealing which type.

This is a positive disclosure witness. Absence of such a commitment is not a
certificate of issuance.

### 8.4 Completion-class theorem

The strongest route is a source-side theorem that the later type or edge is
not generated by any admitted fixed state, seed, boundary, oracle, grammar,
or controller. That is the Temporal Issuance burden. Dynamic Unity may use
such a result if independently verified; record settlement cannot manufacture
it.

## 9. Reopener verdict

The new Time as Finality input does not satisfy Dynamic Unity's reopener:

```text
physical extension mechanism selected before observation: NO
record interface independently selected: NO
survives fixed-generator completion: NO
settlement path dependence: YES
provenance-edge sensitivity: YES
source issuance: UNEARNED
```

No additional TaF simulation is needed. Its existing third arm already
separates defect formation from type arrival; the exact delayed-activation
construction closes the remaining settlement attribution.

## 10. Grade, novelty, and stop

`HC-DU-087` earns:

- **Grade 4, scoped factorization necessity:** graph-derived settlement
  observables cannot distinguish models with the same time-indexed weighted
  record graph;
- **Grade 4, scoped nonidentifiability:** type pre-existence versus delayed
  activation is not identified by the TaF attainability, defect, settlement,
  or sharing outputs;
- **a useful positive:** order-dependent consumption edges are genuine
  provenance structure and can strongly change settlement values; and
- **no physical source issuance, selected record interface, time law,
  ontology, empirical prediction, or new mathematical theorem family.**

The mathematical components are standard factorization and graph
isomorphism. The Dynamic Unity increment is the exact attribution correction
and the minimum source-sensitive reopener.

Stop this branch. Reopen only with a pre-activation intervention, physical
footprint, binding provenance object, or independently warranted completion
theorem that separates dormant fixed types from genuine source extension.
