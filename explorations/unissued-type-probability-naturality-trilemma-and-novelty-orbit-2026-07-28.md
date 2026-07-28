---
title: "Unissued-type probability naturality trilemma and novelty orbit"
status: completed_scoped_result
doc_type: extension_naturality_probability_no_go
created: 2026-07-28
run_id: RUN-20260728-163614-unissued-type-probability-naturality
work_id: PFI-S4-UNISSUED-TYPE-PROBABILITY-NATURALITY
program_id: CCR-PREDICTIVE-SELECTION-TO-FORECASTING-ISSUANCE
authority: "Joe direct chat: Go"
claim_ids:
  - HC-DU-086
claim_grade: "SCOPED GRADE-4 NATURALITY NECESSITY / ELEMENTARY PROBABILITY AND GROUP-ACTION MATHEMATICS / NO EVIDENCE FOR SOURCE ISSUANCE"
claim_status_change: "HC-DU-086 banked at scoped grade"
prediction_status_change: none
paper_state_change: none
hardware_state_change: none
current_authority_change: "CURRENT-RESEARCH.yaml revision 37 remains quiescent with no selected successor"
---

# A model-independent forecast cannot price individually unissued types

## Executive result

`HC-DU-085` showed that an old interface can forecast a total novelty mass
without identifying the later content. The next question is whether that mass
can be distributed coherently among individually not-yet-issued types without
already supplying a richer type universe or generator.

The answer is no under the minimum naturality conditions:

```text
permutation symmetry among unissued types
+ conservative probability for an already named type
+ normalized positive probability through unbounded type extension
= impossible.
```

Equivalently, there is no probability distribution on every nonempty finite
type set that is natural under every injection. A singleton-to-two-type
extension already gives the contradiction.

Without extra structure, all unissued types form one symmetry orbit. The
maximal invariant forecast collapses that orbit to one `NOVEL` symbol. To
split its probability mass, a model must add at least one of:

- a finite bound on the future type set;
- a base measure, metric, feature geometry, or type grammar;
- a fixed hyperprior or random-partition process;
- a physically selected asymmetry or extension lineage;
- revision of earlier allocations as the type set grows; or
- a non-normalized/improper weight rather than an operational probability.

Those are not necessarily illegitimate. They are the structure that makes the
forecast possible. If fixed in advance, they also become the correct
disclosure control: later class appearance is forecast relative to that
ambient structure, not model-independent evidence of source issuance.

The strongest earned statement is therefore:

```text
MODEL_INDEPENDENT_EXACT_NEW_TYPE_PROBABILITY: IMPOSSIBLE
MODEL_INDEPENDENT_NOVELTY_MASS: AVAILABLE
TYPE_SPECIFIC_FORECAST: REQUIRES_TYPED_PRIOR_STRUCTURE
SOURCE_ISSUANCE: NOT_ESTABLISHED
```

## 1. Why the initially proposed rate theorem was not pursued

The first candidate after `HC-DU-085` was a stable-core/innovation-budget
theorem:

> Persistent forecastability under issuance requires old predictions to
> survive conservative extensions and requires novelty/adaptation load to fit
> inside a resource budget.

That statement is useful but not currently additive:

- Time as Finality already defines a conservative type-extension morphism and
  proves that its old attainability envelope is unchanged.
- Nonstationary online-learning theory already uses variation budgets to
  characterize when long-run or dynamic-regret performance remains possible
  ([Besbes, Gur, and Zeevi](https://arxiv.org/abs/1307.5449)).
- Open-world recognition already separates known-class performance, rejection
  of unknowns, and incremental class addition
  ([Bendale and Boult](https://arxiv.org/abs/1412.5687)).

Dynamic Unity therefore does not bank another generic “too much novelty
destroys prediction” curve. The probability naturality problem below is the
sharper joint those results leave exposed.

## 2. Warrant and assumption ledger

| label | content | role |
|---|---|---|
| `STANDARD` | probability normalization, pushforward along a function, permutation invariance, orbit quotients | exact mathematical engine |
| `PROJECT_NATIVE` | old forecast interface, type extension, physical selector, access, capability, and source issuance remain separate | Dynamic Unity typing |
| `CONDITIONAL_POSIT` | the source may add types not individually represented by the prior interface | the hypothesis being explored |
| `IMPORTED` | Temporal Issuance's fixed-hyperprior absorber and Time as Finality's conservative extension object | hostile controls only |

Material free choices are the category of allowed extensions, identity of a
type across extensions, symmetry group, total novelty mass, probability
update law, ambient feature/base measure, resource contract, and admitted
completion class.

The result is strongest for **arbitrary addition-only extensions with no
extra structure**. A physically selected restricted extension category is an
honest class exit and a new burden, not a counterexample.

## 3. `HC-DU-086A` — no probability law natural under arbitrary injections

Let \(\mathbf{FinInj}_{+}\) be the category whose objects are nonempty finite
sets and whose morphisms are injections. Suppose a family assigns to every
object \(X\) a probability distribution

\[
\mu_X\in\Delta(X)
\]

and is natural under injections:

\[
i_*\mu_X=\mu_Y
\qquad
\text{for every injection }i:X\hookrightarrow Y.
\]

### Theorem

No such family exists.

### Proof

Take a singleton \(X=\{\bullet\}\) and a two-element set
\(Y=\{a,b\}\). Normalization forces

\[
\mu_X(\bullet)=1.
\]

There are two injections:

\[
i_a(\bullet)=a,
\qquad
i_b(\bullet)=b.
\]

Naturality along \(i_a\) requires

\[
\mu_Y=\delta_a,
\]

while naturality along \(i_b\) requires

\[
\mu_Y=\delta_b.
\]

Since \(\delta_a\ne\delta_b\), no single \(\mu_Y\) satisfies both.
\(\square\)

### Meaning

The theorem does not say that probability on a growing type set is
impossible. It says that arbitrary type extension does not itself determine
one. The injection identifying the old type, the distribution of new mass,
or some equivalent structure must matter.

In Dynamic Unity language:

> Type growth admits probability laws; it does not select one naturally.

## 4. `HC-DU-086B` — symmetry, conservativity, and normalization trilemma

The same obstruction has a form closer to forecasting.

Let

\[
U_n=\{u_1,\ldots,u_n\}
\]

be \(n\) individually represented future types. Let
\(p^{(n)}_j\) be the prior probability assigned to \(u_j\).
Require:

1. **Symmetry:** every permutation of \(U_n\) preserves the forecast, so
   \(p^{(n)}_1=\cdots=p^{(n)}_n\).
2. **Per-type conservativity:** adding another type does not revise the
   probability already assigned to an existing type:
   \[
   p^{(n+1)}_j=p^{(n)}_j
   \quad (j\le n).
   \]
3. **Normalization through unbounded extension:**
   \[
   \sum_{j=1}^{n}p^{(n)}_j\le 1
   \quad\text{for every }n.
   \]

### Theorem

The only family satisfying all three conditions for arbitrarily large \(n\)
assigns zero probability to every individually represented future type.

### Proof

Symmetry gives one common weight \(w_n\) at stage \(n\). Conservativity gives

\[
w_{n+1}=w_n,
\]

so all stages share one weight \(w\). Normalization requires

\[
n w\le 1
\]

for every \(n\). Therefore \(w=0\).
\(\square\)

If the total novelty mass is fixed at \(h>0\), symmetry instead forces

\[
p^{(n)}_j=\frac{h}{n}.
\]

Every increase from \(n\) to \(n+1\) revises the previous allocations. Thus
fixed positive novelty mass, symmetry, and per-type conservativity cannot all
hold even at adjacent sizes.

### Interpretation

An unbounded family of unknown future types cannot each receive a positive,
symmetric, never-revised probability. The forecaster must choose what to
surrender:

| surrendered condition | resulting object |
|---|---|
| individual typing | one `NOVEL` catch-all mass |
| symmetry | a feature, lineage, metric, base measure, or physical asymmetry privileges types |
| conservativity | prior probabilities are revised as types are added |
| unbounded extension | a finite type cap is supplied |
| normalization | weights cease to be operational probabilities |

This is the exact version of “forecasting issuance requires a prior.”

## 5. `HC-DU-086C` — the novelty orbit is the maximal invariant forecast

Let a symmetry group \(G\) act transitively on the candidate unissued types
\(U\). Any forecast observable

\[
f:U\to Z
\]

that is invariant under every \(g\in G\),

\[
f(gu)=f(u),
\]

is constant on \(U\). Therefore it factors through the orbit quotient

\[
U\longrightarrow U/G=\{\star\}.
\]

The catch-all `NOVEL` symbol from `HC-DU-085` is not merely a convenient
engineering choice. It is the maximal forecast content invariant under the
declared symmetry when no additional structure distinguishes the possible
new types.

To forecast a broad class, constraint, or consequence before issuance, that
class must already be invariantly expressible in the old vocabulary. This
does not identify the new member inside the class.

## 6. The strongest absorbers and honest exits

### 6.1 Fixed base measure or feature geometry

A base measure \(H\), metric, embedding, or grammar can allocate probability
to future observations or type features. The theorem no longer applies
because the candidate types are not structureless and the morphisms are no
longer arbitrary injections.

That can be physically legitimate. But the forecast is then relative to
\(H\), the geometry, or the grammar. Dynamic Unity must ask who or what
selects it and whether the later “new” type was already an event in that
ambient space.

### 6.2 Bayesian nonparametrics

The Blackwell--MacQueen Pólya scheme assigns probability to a new draw using
a fixed parameter/base measure while allowing newly occupied colors or
clusters to appear
([primary paper](https://people.eecs.berkeley.edu/~jordan/courses/281B-spring04/readings/blackwell-macqueen.pdf)).

This is the decisive positive control:

```text
fixed random-measure process
  -> coherent novelty probability
  -> newly occupied observed types.
```

It escapes the no-prior theorem by supplying exactly the missing prior
structure. It therefore supports operational open-world forecasting while
absorbing a claim that observed class birth alone is source issuance.

### 6.3 Physical asymmetry or lineage

A physical event may select an extension map, lineage, or unequal weight.
This is the most interesting Dynamic Unity exit because it may supply a
formed provenance-bearing reason that one future type is more likely.

It still establishes only a type-specific forecast relative to that
antecedent. Source issuance requires the separate completion-class result
that the antecedent is not a fixed richer disclosure mechanism.

### 6.4 Revision

Open-world learners can reserve unknown mass and redistribute it when a new
class is identified. That is valid learning. Its receipt must price:

- probability revision on old candidates;
- detection delay and false novelty;
- relabeling or class-splitting;
- memory and retraining;
- action loss during recovery; and
- no-refit transfer.

Revision is not conservativity, and model adaptation is not source issuance.

## 7. Seeing, choosing, and issuance

The prior agent addendum separated seeing as disclosure-shaped from choosing
as the remaining issuance candidate. The separation is useful but not yet a
theorem.

A choice among an antecedently fixed action set

\[
a\in A
\]

is selection within a pretyped space. It may change the realized future
without issuing a new action type. A stochastic outcome within fixed \(Y\)
has the same boundary.

Choice becomes an operational type-issuance candidate only when the physical
process forms a conservative extension

\[
A_t\hookrightarrow A_{t+1}
\]

that introduces a genuinely new admissible action or distinction, with a
formation/provenance receipt and a matched-resource capability consequence.
Even then, a fixed controller or grammar that already contains all later
actions is the disclosure control.

Thus:

```text
seeing -/-> necessarily disclosure
choosing -/-> necessarily issuance

the deciding object is the typed physical completion and extension,
not the first-person verb.
```

## 8. What this predicts about an issuance-compatible forecaster

If genuine type issuance occurs, a scientifically honest forecaster should
exhibit the following architecture:

1. calibrated probabilities over currently represented outcomes;
2. one or more old-vocabulary novelty or constraint orbits;
3. no unsupported probability split inside a symmetry orbit;
4. a physical detector for interface failure;
5. an explicit extension map and lineage when new types become available;
6. a receipt for probability revision and recovery cost; and
7. a clear declaration of the base measure, hyperprior, feature geometry, or
   physical asymmetry used for any type-specific advance forecast.

This is a testable audit of forecasting systems. It is not yet a prediction
that fundamental physics contains issuance.

## 9. Grade, novelty, and stop

`HC-DU-086` earns:

- **Grade 4, scoped naturality necessity:** no probability distribution is
  natural under all injections of nonempty finite type sets;
- **Grade 4, scoped trilemma:** positive symmetric per-type mass,
  per-type conservativity, and normalized unbounded extension are jointly
  impossible;
- **Grade 4, scoped maximality:** without type-distinguishing structure, an
  invariant forecast factors through the single novelty orbit; and
- **no physical source issuance, no unique prior, no universal objective, and
  no claim that choice creates types.**

The mathematics is elementary and belongs to standard probability, group
actions, and naturality. The Dynamic Unity contribution is the exact
forecasting boundary and supplied-versus-selected audit.

No simulation or external hardware is warranted. Reopen only with a physical
extension mechanism that selects a nontrivial prior/asymmetry before the new
type is observed and then survives the fixed-generator and completion
controls.
