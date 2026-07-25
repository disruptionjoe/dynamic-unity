---
title: "Endogenous regional selection and noisy descent — coupled triple-diamond swing"
status: active_research
doc_type: triple_diamond_synthesis_and_executed_controls
created: 2026-07-25
run_id: RUN-20260725-064622-regional-selection-noisy-descent
claim_grade: "EXACT FINITE IDENTIFICATION/OBSTRUCTION CONTROLS / KNOWN COMPONENT MATHEMATICS / GENERAL PHYSICAL THEORY OPEN"
banked: false
seeded: false
---

# Regional selection and noisy descent

## Executive result

The two missing pieces of recursive regional finality are different
questions:

1. **Selection:** which regional cover and validator-origin model is actually
   identified by the available interventions?
2. **Descent:** once a cover is supplied, do its noisy local records possess
   a compatible global extension, and does its exported boundary preserve the
   upper action?

This swing executes the low-hanging exact finite part of both.

For selection, the correct object is a **version space**, not a favored graph.
If two regional models have the same response signature under every admitted
intervention, no data-only selector can choose between them. If a remaining
intervention separates them, the useful output is the smallest separating
suite. A deterministic relay, label change, or cloned validator must not
manufacture a new physical region or independent support source.

For noisy descent, two defects remain separate:

- **compatibility obstruction:** the local stochastic records admit no joint
  global extension;
- **action-factorization defect:** a joint process exists, but the boundary
  summary cannot reproduce an upper-layer response within the declared
  tolerance.

The smallest frustrated binary triangle has a sharp result. If two edges aim
to agree, one aims to disagree, and every edge has the same error
\(\epsilon\), the local mismatch records admit a joint global model exactly
when

\[
\epsilon\geq\frac13.
\]

This is an instance of the known even-parity polytope, not a new physical
threshold. It is nevertheless the first quantitative noisy obstruction in
the Dynamic Unity regional-finality branch.

## 1. The coupled research object

Let \(\mathcal M\) be a frozen finite grammar of candidate regional models,
\(\mathcal I\) the admitted interventions, \(D\) the observed response
records, and \(\sim\) the declared label/refinement equivalence.

The **regional version space** is

\[
\mathcal V(D)
=
\{M\in\mathcal M:
M\text{ reproduces }D\}/\!\sim.
\]

For one supplied \(M\), let \(\mathcal E_M(D)\) be the set of global
stochastic extensions of its compatible local records. Let
\(\delta_{\mathrm{act}}(M,C,U)\) be the minimum worst-case error for
simulating the frozen upper actions \(U\) through boundary summary \(C\).

The program now distinguishes:

| Version/extension state | Honest result |
|---|---|
| \(\mathcal V(D)=\varnothing\) | frozen candidate grammar is misspecified or the contract is incomplete |
| \(|\mathcal V(D)|>1\) and a held-out action separates candidates | underidentified, with a minimum separator |
| \(|\mathcal V(D)|>1\) and no admitted action separates candidates | observational equivalence in the declared class |
| \(|\mathcal V(D)|=1\), \(\mathcal E_M(D)=\varnothing\) | region identified, but local stochastic records are globally obstructed |
| \(|\mathcal V(D)|=1\), \(\mathcal E_M(D)\neq\varnothing\), \(\delta_{\mathrm{act}}>\tau\) | compatible process, action-insufficient boundary |
| \(|\mathcal V(D)|=1\), \(\mathcal E_M(D)\neq\varnothing\), \(\delta_{\mathrm{act}}\leq\tau\) | selected candidate descends for the frozen task, subject to safety/provenance gates |

This table is the central synthesis. **Underdetermination, incompatibility,
and lossy promotion are three different failures.**

## 2. Triple Diamond A — endogenous regionalization

### A1. Problem and estimand

#### Divergence

| Lens | Distinct warning or opportunity |
|---|---|
| Category/descent | A cover is task- and restriction-relative; drawing a boundary does not select it. |
| Counterfactual statistics | Selection needs an estimand: version-space reduction caused by one intervention. |
| Causal inference | Passive records commonly identify only an equivalence class; interventions orient or split it. |
| Active experimental design | Choose an intervention by worst-case or expected candidate reduction, not convenience. |
| Formal counterexamples | Preserve the smallest pair of candidates with identical current signatures. |
| Higher-order networks | Physical interactions may overlap as hyperedges rather than partition into communities. |
| Control/system identification | A region matters when an input-output response distinguishes it. |
| Adversarial distributed systems | Apparent validators can be correlated or Sybil copies of one origin. |
| Security/provenance | Independence requires failure-domain provenance, not signature count. |
| Commercial research operations | Negative identification results should name the next cheapest separating experiment. |
| Philosophy of science | Minimum description, elegance, or a preferred diagram is not physical selection without an independent principle. |

#### Convergence

The frozen question is:

> Relative to a predeclared candidate grammar and intervention family, which
> regional structures remain response-equivalent, and what minimum held-out
> intervention set makes their signatures injective up to declared
> representation equivalence?

The primary counterfactual estimand is version-space reduction, with both
worst-case and uniform-prior expected remaining candidate count retained.

### A2. Attack architecture

#### Divergence

The considered approaches were:

1. passive graph clustering;
2. minimum-description or minimum-edge covers;
3. observational causal-DAG discovery;
4. behavioral congruence and bisimulation;
5. Boolean interaction hypergraphs;
6. Bayesian active intervention design;
7. exhaustive cover enumeration; and
8. pair-separating hitting sets.

Passive clustering and an unsupported Occam tie-break fail the physical
selection question. Generic cover enumeration is expensive before it has a
response grammar. Behavioral congruence is useful downstream but can define
away the region if it is built from every target response.

#### Convergence

The finite pilot combines:

- a Boolean response table with its unique
  algebraic-normal-form/Möbius reconstruction;
- a frozen candidate family of regional interaction hypergraphs;
- exact version-space signatures;
- a minimum pair-separating intervention hitting set;
- label covariance;
- deterministic-relay collapse; and
- a separate failure-domain intervention for validator origins.

This is intentionally not claimed as the general physical representation.
It is a controlled class in which the difference between full identification,
underidentification, and representation ambiguity is exact.

### A3. Assurance and execution

The assurance diamond required:

1. exhaustive reconstruction, not selected examples;
2. a passive/singleton nonidentification counterexample;
3. a known ground-truth positive control;
4. overlapping regions, not only partitions;
5. relabeling covariance;
6. inert-relay nonselection;
7. raw-identity versus origin-independence separation;
8. a minimum separating experiment; and
9. a negative output when no admitted experiment separates candidates.

`tests/du_endogenous_regionalization_probe.py` passes `21/21`.

## 3. Executed regional-selection results

### 3.1 Finite signature-identification lemma

For a frozen finite candidate class, current actions identify one candidate
up to the declared quotient exactly when their response signature is
injective on quotient classes.

If it is not injective, every still-indistinguishable candidate pair defines
a requirement. An action covers that pair when their predicted responses
differ. A minimum separating action suite is therefore a minimum hitting set
over the indistinguishable pairs.

This is an elementary finite identification result, not a novel causal
discovery theorem.

### 3.2 Exhaustive Boolean reconstruction

The probe runs the Boolean Möbius transform and inverse on all `65,536`
four-input truth tables with zero failures.

Inside this frozen grammar, the complete intervention table uniquely selects
the algebraic normal form. It does **not** follow that nature uses Boolean
interactions or that monomials are fundamental physical regions.

### 3.3 Three rival regional covers

Four primitive controls \(A,B,C,D\) admit three perfect-matching interaction
covers:

```text
AB | CD
AC | BD
AD | BC
```

For the response rule given by the XOR of the two active pair interactions,
the passive action and every singleton action return zero in all three
models. Present records therefore leave a three-model version space.

Among the six pair interventions, the exact minimum **worst-case**
separating suite has size two. One result branch can finish after the first
query, but no one-query design distinguishes all three possible covers.

### 3.4 Identification cost is not hidden

The complete degree-two four-input grammar contains \(2^6=64\) models, one
for each choice of six pair coefficients. Every passive and singleton record
is again identical. Each pair intervention isolates one independent
coefficient, so all six pair interventions are necessary and sufficient for
complete identification.

This prevents the three-cover toy from being misread as a universal
two-query result.

### 3.5 Regions can overlap

The response

\[
f(A,B,C)=AB\oplus BC
\]

reconstructs the overlapping interaction hyperedges \(AB\) and \(BC\).
The finite region object therefore need not be a partition or hierarchy.
Permuting the primitive labels permutes the recovered hyperedges exactly.

### 3.6 Deterministic-relay nonselection

Add an inert relay \(R=A\). On every admissible state, the two response
extensions

\[
AB\oplus BC
\quad\text{and}\quad
RB\oplus BC
\]

agree. Their raw hypergraphs differ, so admissible behavior does not select
one raw refined diagram. Collapsing the deterministic relay sends both to
the same core interactions \(AB,BC\).

Raw topology is therefore representation-dependent until deterministic
copies are quotiented.

### 3.7 Validator-origin nonidentification

Three validators can present the same three successful signatures under two
origin models:

```text
independent: v1->alpha, v2->beta,  v3->gamma
clone:       v1->alpha, v2->alpha, v3->gamma
```

The present record is identical. A declared intervention on failure domain
`alpha` produces different joint failure records and separates the models.
This is a finite control showing why identity count cannot establish
independent support.

It is not permission to perform destructive failure injection in a physical
system; an empirical implementation needs a safe, ethical surrogate.

## 4. Triple Diamond B — noisy noninvertible descent

### B1. Problem and estimand

#### Divergence

| Lens | Distinct warning or opportunity |
|---|---|
| Stochastic processes | Local channels can be individually valid without one joint process. |
| Marginal-problem theory | Descent is existence of a compatible global extension. |
| Convex geometry | Compatibility is polytope membership; violated facets provide finite certificates. |
| Category/sheaf descent | Cycles create gluing obstructions absent on acyclic covers. |
| Contextuality | No global section can be meaningful, but must not be called quantum without a physical measurement scenario. |
| Information theory | A useful defect needs an operational task before it becomes a distance. |
| Approximate sufficiency | Global compatibility does not imply a boundary summary preserves upper responses. |
| QEC/logical access | Proper-subset access can erase a logical distinction even in standard quantum theory. |
| Adversarial consensus | Stochastic compatibility does not supply quorum safety, liveness, or independent support. |
| Metrology | A physical threshold requires calibrated channels, errors, resources, and uncertainty. |
| Formal methods | Preserve the smallest violated facet and the exact return type. |

#### Convergence

The run retains two independent estimands:

\[
\Delta_{\mathrm{cycle}}
=
\max_{F\subseteq E,\ |F|\text{ odd}}
\left[
\sum_{e\in F}x_e
-\sum_{e\notin F}x_e
-(|F|-1)
\right]_+
\]

for edge mismatch probabilities \(x_e\), and

\[
\delta_{\mathrm{act}}
=
\inf_{\widehat P(\cdot\mid C,a)}
\sup_{s,a}
\operatorname{TV}\!\left(
P(\cdot\mid s,a),
\widehat P(\cdot\mid C(s),a)
\right)
\]

for a supplied boundary summary \(C\).

\(\Delta_{\mathrm{cycle}}>0\) means the local mismatch records have no joint
cycle extension. \(\delta_{\mathrm{act}}>0\) means the supplied boundary is
lossy for an upper action. One does not imply the other.

### B2. Attack architecture

#### Divergence

The compared methods were:

1. Monte Carlo consistency checks;
2. additive error/union bounds;
3. generic linear programming;
4. optimal transport;
5. enriched or metric sheaf formulations;
6. cycle inequalities;
7. even-parity/cut polytopes; and
8. Bayesian model comparison.

Monte Carlo would obscure the exact smallest obstruction. A union bound is
not sufficient for global compatibility. A generic LP is the correct general
successor, but the smallest cycle has a closed exact structure that should be
banked first.

#### Convergence

For a binary cycle, every deterministic global node assignment creates an
even number of edge mismatches. Thus the possible mismatch-marginal vectors
form the even-parity polytope. Its odd-set inequalities give an exact
compatibility criterion.

On a triangle, the four even parity sectors are

```text
000, 011, 101, 110.
```

The mismatch marginals determine unique signed sector weights. Negative
weight is an exact extension obstruction. It is not an observed negative
probability or a physical distance.

For a binary upper response and deterministic summary, the minimum
worst-case total-variation error on one summary fiber is exactly half the
range of response probabilities in that fiber.

### B3. Assurance and execution

The assurance diamond required:

1. all even and odd deterministic parity vertices through cycle size seven;
2. every point on a complete rational triangle grid;
3. a sharp noisy frustrated family;
4. node-local noninvertible noise as a positive compatibility control;
5. a compatible but action-insufficient specimen;
6. a logical-access lift;
7. adversarial safety and independent-provenance gates;
8. all four existing descent outcomes; and
9. an explicit ban on interpreting facet slack as a physical metric.

`tests/du_noisy_noninvertible_descent_probe.py` passes `20/20`.

## 5. Executed noisy-descent results

### 5.1 Binary cycle descent criterion

For an \(n\)-cycle with mismatch probabilities \(x_e\in[0,1]\), a joint
distribution over global binary node assignments with those mismatch
marginals exists exactly when, for every odd \(F\subseteq E\),

\[
\sum_{e\in F}x_e-\sum_{e\notin F}x_e\leq |F|-1.
\]

The probe audits every even and odd deterministic vertex for
\(3\leq n\leq7\). All even vertices satisfy every inequality. Every odd
vertex carries a unit violated-facet witness.

This is the known parity-polytope theorem. The DU contribution at this grade
is its typing as a stochastic regional-record descent obstruction.

### 5.2 Triangle signed extension

For triangle mismatch marginals \((x_1,x_2,x_3)\), the signed weights of the
four even sectors are

\[
\begin{aligned}
w_{000}&=1-\frac{x_1+x_2+x_3}{2},\\
w_{011}&=\frac{x_2+x_3-x_1}{2},\\
w_{101}&=\frac{x_1+x_3-x_2}{2},\\
w_{110}&=\frac{x_1+x_2-x_3}{2}.
\end{aligned}
\]

They sum to one. The local records descend exactly when all four weights are
nonnegative. The probe checks all `343` points on the denominator-six cube;
the signed-weight and odd-facet criteria agree everywhere.

Inside the unit cube at most one sector weight is negative. If the maximum
facet violation is \(v\), the unique signed sector extension has negative
mass \(v/2\). Calling that an operational or physical distance requires a
separately frozen repair task and cost.

### 5.3 Sharp frustrated-noise threshold

Let the desired edge parities be equality, equality, inequality, each
reported incorrectly with probability \(\epsilon\). Then

\[
(x_1,x_2,x_3)
=
(\epsilon,\epsilon,1-\epsilon).
\]

The unique active facet violation is

\[
\Delta_{\mathrm{cycle}}
=
[1-3\epsilon]_+.
\]

Therefore descent occurs exactly at or above \(\epsilon=1/3\). Below that
point the signed extension has negative mass
\((1-3\epsilon)/2\).

This threshold is a compatibility threshold for one declared marginal
family. It is not a universal objectivity, collapse, or finality threshold.

### 5.4 Noninvertible local noise preserves compatibility

If a joint distribution already exists, applying independent binary
symmetric channels at its nodes—up to and including the fully erasing
channel with error \(1/2\)—leaves a joint distribution by construction.

The probe executes `972` distribution/channel cases. None creates a cycle
obstruction. The fully erasing control yields mismatch probability \(1/2\)
on every edge.

Thus noninvertibility alone is not the problem. Incompatible **edgewise
specifications** are.

### 5.5 Exact binary boundary half-range

For a fixed summary fiber and binary upper response probabilities
\(\{p_s\}\), any one summary response \(q\) has worst-case error at least

\[
\frac{\max_s p_s-\min_s p_s}{2}.
\]

Choosing the midpoint attains the bound.

The four-state fixture has a coarse-summary action defect \(2/5\); a
state-separating lift reduces it to zero. This remains ordinary approximate
sufficiency, not a new law.

### 5.6 Noisy GHZ logical-access control

For standard GHZ phase visibility \(v\), the two logical parity outcome
probabilities are

\[
p_+=\frac{1+v}{2},
\qquad
p_-=\frac{1-v}{2}.
\]

If a proper-subset boundary gives both phases the same summary, its optimal
worst-case logical-parity error is \(v/2\). A logical phase label reduces the
defect to zero.

This is standard noisy logical access. Qubits are not validators, and
entanglement is not consensus.

### 5.7 The four-outcome contract survives

The stochastic fixture exercises:

- `DESCENDS`;
- `REQUIRES_PROVENANCE_OR_LOGICAL_LIFT`;
- `REJECTS_FRUSTRATED_OR_UNSAFE_COMPOSITION`; and
- `INCOMPLETE_CONTRACT`.

Unsafe quorum and correlated provenance reject composition independently of
stochastic compatibility. A hardening layer can safely reject a positive
cycle obstruction, but rejection still does not create a higher-level fact.

## 6. What the combined result changes

The regional work should now run in this order:

```text
freeze primitive process and candidate grammar
    -> compute regional version space
    -> choose minimum held-out separator or return equivalence
    -> freeze one selected/equivalent regional object
    -> test stochastic overlap compatibility
    -> compute boundary action defect
    -> apply safety, liveness and independent-provenance gates
    -> promote to higher-layer node or return the typed obstruction
```

This prevents three recurring mistakes:

1. choosing one region diagram before it is identified;
2. assuming locally reasonable noisy records have one global extension; and
3. assuming global compatibility makes a boundary action-sufficient.

## 7. Collision and novelty map

The component mathematics is occupied:

- Boolean truth tables and algebraic normal forms are related by the Boolean
  Möbius transform; see the explicit transformation analysis by
  [Zhang and Tang](https://www.jstage.jst.go.jp/article/transfun/advpub/0/advpub_2022EAL2095/_article/-char/en).
- Intervention selection over observationally equivalent causal structures
  is established active-learning terrain; see
  [He and Geng](https://jmlr.org/beta/papers/v9/he08a.html) and
  [Ghassami, Salehkaleybar, and Kiyavash](https://arxiv.org/abs/1910.05651).
- The even-parity polytope and odd-set inequalities are standard
  polyhedral-combinatorics objects; see
  [Ermel and Walter](https://optimization-online.org/wp-content/uploads/2018/04/6566.pdf).
- Marginal compatibility and cycle obstructions have mature probabilistic
  and contextuality formulations; see
  [Vorob'ev](https://www.mathnet.ru/eng/tvp4692),
  [Abramsky and Brandenburger](https://arxiv.org/abs/1102.0264), and
  [Kharoof, Ipek, and Okay](https://arxiv.org/abs/2306.01459).

No standalone novelty claim is made for ANF reconstruction, hitting-set
experimental design, parity facets, signed triangle weights, or the
half-range approximation bound.

Potential distinctiveness remains the unchanged conjunction:

```text
physically selected regional cover
    + independently selected validator/failure origins
    + noisy noninvertible marginal descent
    + action-sufficient recursive promotion
    + adversarial safety and liveness
    + one quantum and one distributed realization
    + capability/resource consequence.
```

That conjunction is search-incomplete and unproved.

## 8. Prepared next approaches

### `ER-NEXT-01` — stochastic regional identification

- **Question:** which regional model is selected from finite noisy repeated
  interventions?
- **Approach:** freeze a finite stochastic instrument grammar; use exact
  likelihood ratios and sequential minimax/expected version-space reduction.
- **First decisive object:** the three matching covers with Bernoulli readout
  noise and an explicit stopping/error guarantee.
- **Negative output:** a finite-sample nonidentification or lower bound.
- **Cheap kill:** prior or complexity penalty determines the answer while
  interventions carry no separating information.
- **Scale gate:** calibrated coverage on held-out model families.

### `ER-NEXT-02` — safe validator-origin individuation

- **Question:** what measurements establish independent support without
  destructive failure injection?
- **Approach:** compare controlled common-mode perturbations, natural outage
  covariance, provenance attestations, and adversarial clone models.
- **First decisive object:** two origin partitions with matched marginals and
  one safe shared-cause probe.
- **Negative output:** an impossibility theorem under the admitted
  observation class.
- **Cheap kill:** signature/key identity is counted as failure independence.
- **Scale gate:** a preregistered classifier controls false-independence risk
  under held-out correlated failures.

### `ER-NEXT-03` — multi-time physical regional grammar

- **Question:** do interaction regions survive beyond Boolean endpoint
  functions?
- **Approach:** derive candidate regions from independently fixed
  multi-time instruments or process tensors, then quotient deterministic
  relay/refinement equivalences.
- **First decisive object:** three events, two overlapping instruments, one
  held-out causal-break action.
- **Negative output:** representation nonuniqueness or a target-defined
  region receipt.
- **Cheap kill:** the region changes when a causally inert implementation
  register is added.
- **Scale gate:** one grammar transfers without refit to a replayable
  distributed protocol.

### `ND-NEXT-01` — general finite marginal-descent compiler

- **Question:** which noisy local record covers admit a joint extension?
- **Approach:** exact rational linear feasibility with a dual/Farkas
  obstruction certificate; recover closed cycle facets as regression cases.
- **First decisive object:** two glued cycles and one nonacyclic hypergraph.
- **Negative output:** a smallest incompatible marginal family and dual
  witness.
- **Cheap kill:** pairwise overlap agreement is treated as global
  compatibility.
- **Scale gate:** sparse decomposition beats full global enumeration.

### `ND-NEXT-02` — authenticated protocol transfer

- **Question:** does the same stochastic descent defect survive an executable
  adversarial regional protocol?
- **Approach:** derive local marginal records from authenticated message
  schedules, corruption, withholding and replay rather than insert them.
- **First decisive object:** three regional nodes with a loop, one Byzantine
  origin, and enumerated delivery schedules.
- **Negative output:** the missing route/provenance register that restores a
  joint extension.
- **Cheap kill:** protocol safety is inferred from marginal compatibility.
- **Scale gate:** unchanged results under a second protocol architecture.

### `ND-NEXT-03` — quantum-instrument transfer

- **Question:** can an instrument-derived quantum marginal cover use the same
  compatibility/action-defect contract?
- **Approach:** construct complete CP instruments and accessible outcome
  marginals; compare ordinary joint-process, contextual, leakage, and
  logical-access models.
- **First decisive object:** a noisy three-context instrument with a complete
  implementation register.
- **Negative output:** standard process-tensor or QEC absorption.
- **Cheap kill:** a mathematical no-global-section result is called a
  physical quantum deviation without a valid measurement scenario.
- **Scale gate:** calibrated error bars and a held-out instrument.

### `ND-NEXT-04` — recursive defect composition

- **Question:** how do compatibility and action defects propagate across two
  region-to-node promotions?
- **Approach:** seek upper/lower composition bounds with explicit correlated
  error, resource, and decoder terms.
- **First decisive object:** two promoted triangles sharing one certified
  boundary.
- **Negative output:** a counterexample showing no scalar defect composes.
- **Cheap kill:** independent-error addition is assumed across shared
  provenance.
- **Scale gate:** a natural bound survives benign subdivision and one
  correlated-noise family.

## 9. Recommended concentration

The next big swing should not expand both legs uniformly.

Use one common physical/protocol specimen and run:

1. `ER-NEXT-03` to produce or fail to produce an independently selected
   multi-time regional grammar;
2. `ND-NEXT-01` to build the general exact marginal-descent compiler in
   parallel as the adjudicator; and then
3. transfer the same specimen through `ND-NEXT-02` or `ND-NEXT-03`.

This ordering makes a physical selection failure valuable and prevents the
general compiler from being fitted to a favored specimen.

## 10. Disposition

- Extend `HC-DU-035C` and the control grade of `H-CCR-16`.
- Extend `CONCEPT-DU-011` with the version-space and two-defect architecture.
- Add no new core concept: the existing recursive-regional-finality concept
  already owns both results.
- Add no prediction: the one-third threshold belongs to a declared toy
  marginal family and is not a physical forecast.
- Promote no claim, ontology, physical law, paper priority, or Factory state.
- Preserve both deterministic artifacts and all smallest counterexamples.
