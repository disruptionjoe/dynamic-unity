---
title: "Science Council wild-frontier scientist — next actions after SWING-DU-PHY-02"
status: completed_independent_council_work
doc_type: council_next_actions
created: 2026-07-24
persona: wild-frontier scientist
predecessor: explorations/physical-influence-selector-wave-synthesis-2026-07-24.md
contract: explorations/science-council-five-persona-next-actions-contract-2026-07-24.md
probe: tests/du_wild_frontier_fisher_csg_scale_bridge_probe.py
artifact: tests/artifacts/du_wild_frontier_fisher_csg_scale_bridge_probe_result.json
verdict: "CONSTRUCTIVE-SKELETON-FOUND / NAIVE-COUNT-RUNNING-KILLED — the priority survives, but full path covariance must precede geometry or cosmology"
claim_status_change: none
banked: false
seeded: false
---

# Wild-frontier scientist: next actions after SWING-DU-PHY-02

## Headline

The current pivot is directionally right, but “label-invariant order-first
growth with feedback and a generated scale” hides a sharper obstruction than
the synthesis records:

> A transition rule can be exactly invariant under relabeling at every finite
> state and still make the *probability of a completed causal set* depend on
> which natural labeling was used to grow it.

I built the smallest coherent bridge I could:

1. transitive-percolation births on a causal order;
2. a KL/Fisher metric on the transition family, selecting a
   coordinate-covariant mobility;
3. a target-free-in-scale natural flow
   `dg/dlogN=1`;
4. the invariant count scale `N_*=N exp(-g)`;
5. the unit map `ell_*=ell_atom N_*^(1/d)`; and
6. a genuine **expected Fisher-information contribution profile** over the
   possible physical births.

Every algebraic piece works. The combined cardinality-running growth law does
not: an exact three-event test gives path probabilities

```text
constant p:     [0.143883, 0.143883, 0.143883]
count-running p:[0.118190, 0.118190, 0.078793]
```

for three natural labelings of the same causal set. The ratio is `1.5`.
Statewise relabeling invariance passed exactly; discrete general covariance
failed.

My verdict is therefore:

> **`CONSTRUCTIVE-SKELETON-FOUND /
> NAIVE-COUNT-RUNNING-KILLED`.**

The opportunity is narrower and better than before. Seek a **covariant
renormalization of a fixed growth law**, or make coupling updates themselves
physical order records. Do not let a coupling run directly with birth index
and call cardinality an invariant clock.

## 1. Direct re-audit

I inspected the complete wave contract, pre-result audit, synthesis, Track A
and Track B interpretations, their executable probes and stored artifacts,
Track C's independent comparison, the concept register, live `LANES.yaml`,
the `HC-DU-011` and `HC-DU-022` hardening entries, and the prior
`SWING-DU-CMF-01` causal-memory result.

I then reran all three wave probes:

| Receipt | Result reproduced |
|---|---|
| Bianconi dissipation shares | `16/16`; Euclidean and affine profiles differ by `0.395652`; terminal raw dissipation ratios `2.08e-15` and `3.75e-16`; exact stationary profiles undefined |
| Record score-energy shares | `30/30`; `GL(4)` path covariance; participation/Shannon `N^-1/2`; native Gini tends `3/8`; every individual share vanishes |
| Selector/persistence comparison | `24/24`; `SELECTOR_OPEN`; old pair `NOT_EVALUABLE`; no unit-bearing nonzero scale |

The artifacts remained byte-identical:

```text
Track A  9c2df4fc74bac7685a2c7b71da8a8f3f8e2f3b49b3020417653dce495c5abec5
Track B  cd33b66d54e53706f79e6c1cbf4d96179e245251fb4a855527217ca72622e3cf
Track C  c6adee67175830a6fcd2a9b6057eb1fe13f8d19ceac3c1fe2a1f84497bf5df7b
```

### Re-audit conclusions

The current wave interpretation is sound on its own scope:

- normalized shape contains no discarded common magnitude or units;
- Bianconi dissipation is completion-dependent and vanishes;
- Track B decomposes observed residual energy, not expected Fisher
  information;
- persistent Gini is relative inequality, not a persistent physical scale;
- the old incomparable pair cannot be physically ordered without an embedding
  and independent response;
- `NO-NONZERO-PHYSICAL-SCALE-IDENTIFIED` is an empirical wave disposition, not
  a no-go theorem; and
- the influence concept is neither identified with dark energy nor falsified.

The part needing refinement is the proposed successor's admission language.
“Label-invariant” must include equal path weight across natural labelings, not
only invariance of a transition formula under a permutation at one state.

## 2. Contested finding

### Exact current proposition

The synthesis treats the coupled `HC-DU-011 + HC-DU-022` object as an open,
unbuilt frontier:

> a label-invariant order-first causal growth/action law whose
> past-cardinality feeds back, reconstructs geometry, and endogenously
> generates a dimensional memory scale.

Its implied research posture is that no constructive bridge yet connects
order-first growth, a selected mobility, a generated count/length scale, and
the influence diagnostics.

### Why it may be too coarse

Four of those pieces can be joined without cosmological fitting:

1. a causal growth law already defines a statistical manifold of possible
   births;
2. local relative entropy supplies its Fisher metric;
3. a marginal natural flow can transmute a dimensionless coupling into a count
   hierarchy; and
4. Fisher contributions of transition outcomes are a mechanism-native
   influence object.

That does not solve the frontier, but it turns “unbuilt” into a specific
compatibility question.

### Evidence that would change the proposition

A minimal construction had to demonstrate:

- valid causal births from order data alone;
- statewise relabeling equivariance;
- a coordinate-covariant mobility with all choices exposed;
- an invariant count scale absent from the update's target;
- a downstream response/influence decomposition; and
- equal total probability for different natural labelings of one completed
  causal set.

Failure of the last item was the declared cheap kill.

## 3. Bounded evidence-producing swing

### 3.1 Order-first transition law

At a finite causal set `C`, independently propose a direct link from a new
maximal event to each existing event with probability `p`, then take the
transitive closure. The physical outcomes are down-sets of `C`.

For a fixed `p`, this is the transitive-percolation family. The probe enumerates
every raw link subset and aggregates histories that produce the same physical
down-set.

On a four-event diamond at `p=0.31`, the transition distribution and its
Fisher contributions are exactly equivariant under three nontrivial event
permutations.

### 3.2 A mobility selected by the response law

Use logit coordinate

```text
g = log[p/(1-p)].
```

For `n` independent direct-link proposals, the local KL Hessian is

```text
F_raw = n p(1-p).
```

Insert the relation-favouring source potential

```text
S(g;C) = -E[number of proposed direct links] = -n p.
```

Then

```text
dS/dg = -F_raw
dg/dlogN = -F_raw^-1 dS/dg = 1.
```

The probe checks this at five couplings and checks the same path under the
nonlinear coordinate `h=sinh(g)`. The natural flow transforms by the chain
rule to machine precision.

This is a conditional mobility selection, not a discovery from nowhere. The
inserted choices are:

- Bernoulli direct links as physical microhistory;
- KL as the local path cost;
- the sign `S=-E[m]`, which favours relation creation;
- log cardinality as the flow coordinate; and
- unit normalization of that coordinate.

### 3.3 A transmuted count hierarchy

The exact flow gives

```text
g(N)=g_ref+log(N/N_ref)
N_* = N exp[-g(N)] = N_ref exp(-g_ref).
```

`N_*` does not appear as a target in the update. Three fixtures with
`N_*=4,16,64` preserve the invariant to `2e-14` relative or better. Conditional
on atom length `ell_atom` and recovered dimension `d`,

```text
ell_* = ell_atom N_*^(1/d).
```

For `d=4`, the three illustrative ratios are `sqrt(2)`, `2`, and `2sqrt(2)`.

This is a dimensional-transmutation **skeleton**, not a selected physical
scale. The scale value remains controlled by the initial dimensionless
coupling; `ell_atom` and `d` are separate inputs; no hierarchy was predicted.

### 3.4 Influence becomes a downstream response object

For each physical down-set outcome `y`, let

```text
q_y(g) = probability of that causal birth
s_y    = d log q_y / dg
I_y    = q_y s_y^2.
```

Then

```text
F_downset = sum_y I_y
p_y^F     = I_y/F_downset.
```

This is a genuine expected Fisher-information decomposition of the growth
law. It is not Track B's observed residual-energy decomposition.

Causal closure itself becomes informative. Relative to the raw-link Fisher
metric, the retained down-set Fisher fractions are:

```text
four-event antichain  1.000000
four-event diamond    0.677127
four-event chain      0.623652
```

The antichain retains every raw link distinction. Nontrivial order identifies
several raw link histories with one physical birth, so Fisher information
falls by data processing. The order therefore changes both the response
magnitude and its influence allocation without fitting a target profile.

This is the genuinely new opportunity I did not see before:

> The missing response law may be the transition experiment itself. Causal
> order does not merely carry an influence profile; by coarse-graining possible
> births, it *redistributes observable Fisher response*.

### 3.5 The cheap kill

Take the completed three-event causal set with `a<c` and `b` isolated. It has
three natural birth orders:

```text
(a,b,c), (b,a,c), (a,c,b).
```

With constant `p=0.27`, the exact path probability is `0.143883` for all
three. The null passes.

Let the natural flow instead run with birth cardinality:

```text
g(N) = -log(16) + log N
p(N) = logistic(g(N)).
```

The same completed causet receives:

```text
0.118190, 0.118190, 0.078793.
```

The growth history can now reveal which natural labeling was used. The
cardinality-running feedback law fails discrete general covariance even though
its fixed-state transition kernel is exactly relabeling-equivariant.

## 4. Reconciliation

### Result on the contested finding

**Narrowed, not overturned.**

- **Overturned at skeleton level:** order-first growth, Fisher mobility,
  count-scale transmutation, and a mechanism-native influence profile are not
  mutually alien. A single algebraic construction contains all four.
- **Upheld at physical-model level:** the obvious way to combine them—run the
  transition coupling directly with birth cardinality—fails the first exact
  discrete-covariance null. No admissible generated-scale growth law exists
  yet.
- **Still not evaluable:** whether a covariant coupling flow can reconstruct
  3+1 geometry, generate a transfer-operator gap, or source a cosmological
  observable.

### Concept-level versus formalization-local implication

The failure belongs to the formalization:

```text
FORMALIZATION-WF-01:
count-running transitive-percolation logit under KL/Fisher flow
```

It does not falsify:

- order-first causal growth;
- dimensional transmutation;
- Fisher-selected mobility;
- `CONCEPT-DU-001`; or
- the coupled `HC-DU-011 + HC-DU-022` research program.

### Corrections to the current synthesis

1. **Keep the scientific disposition.** The prior wave still identified no
   nonzero physical scale.
2. **Interpret the three-part reopener as a claim conjunction, not a ban on
   staged research.** A response law can be built and killed before a units map
   exists; that is exactly what happened here.
3. **Strengthen “label-invariant.”** Statewise permutation covariance is
   necessary but insufficient. Equal path probability across natural
   labelings must be an admission test.
4. **Do not call `HC-DU-011 + HC-DU-022` one monolithic build.** It is a
   dependency chain whose first decision product is a covariant feedback law.
5. **The influence branch remains stopped as a dark-energy identification
   branch.** Its objects can already be used as downstream telemetry in
   candidate growth laws.

There is no conflict with `OBJECT-FOUND / SELECTOR-OPEN`. The new construction
selects a response metric conditional on a transition law; it still does not
select participation, Shannon, or Gini as `Lambda`.

## 5. Sequenced next-actions roadmap

Actions are ordered by dependency and information gain.

### Action 1 — freeze the full covariance passport

**Output.** A minimal `HC-DU-011A` contract distinguishing:

- statewise relabeling equivariance;
- equal path weight across all natural labelings;
- Markov sum-rule normalization;
- spectator/Bell-causality behavior;
- past immutability; and
- whether coupling records are physical state or gauge bookkeeping.

**Falsifier / stop.** A candidate that calls birth count a scalar but changes
the probability of an unlabeled completed causal set is stopped immediately.

**Why now.** The probe shows the present phrase “label-invariant” is too weak
to reject the cheapest false bridge.

### Action 2 — exhaust small unlabeled causets before any large simulation

**Output.** Enumerate all causets through the largest feasible small `n`, all
natural labelings, and path weights for each feedback candidate. Preserve the
first counterexample, not just a pass count.

Test at least:

1. explicit `p(N)` or `g(N)` running—the killed null;
2. running on current height, width, or past-cardinality statistics;
3. a fixed generalized-percolation coupling sequence;
4. a post-to-post effective coupling transformation; and
5. a coupling record added as physical order content.

**Falsifier / stop.** Any unlabeled final causet with unequal natural-labeling
weights kills that exact law.

**Why now.** This is far cheaper and more decisive than geometry recovery,
spectral calculations, or cosmological fitting.

### Action 3 — try only two covariant scale routes

#### Route A: renormalize fixed CSG couplings at covariant landmarks

**Output.** Begin with one fixed, path-covariant coupling law. Define a
coarse-graining transformation only at order-defined landmarks such as posts
or covariantly characterized eras. Look for an invariant

```text
N_* = F(couplings)
```

that does not reference birth labels or a fitted cosmic epoch.

**Falsifier / stop.** The inferred `N_*` changes under natural relabeling,
microscopic blocking convention, or landmark redefinition beyond a declared
universality class.

#### Route B: make coupling change a physical record

**Output.** Add the minimal causal record whose content changes the next
transition law. Two histories with different coupling updates must then be
different physical causets, not different labels of one causet. State the
resource/noise cost of writing that record.

**Falsifier / stop.** If the record is only an external schedule, if it can be
deleted without changing observables, or if it requires future history, the
return arrow is not built.

**Why now.** These are the two coherent escapes from the exact path-covariance
failure. Adding more arbitrary running kernels has near-zero information
value.

### Action 4 — derive the transition response and mobility

**Output.** For every survivor, derive:

```text
q_y(C)                 transition probabilities
F_ab(C)                Fisher/KL response metric
I_y or I_y,ab          outcome Fisher contributions
K_response             retarded linear response
K_noise                positive covariance/noise
```

Then compare Fisher-natural, Euclidean, and affine-SPD mobilities only where
they are actually defined on the same coarse state.

**Falsifier / stop.** If the proposed mobility changes under reparameterization
or is selected only because it produces the desired concentration profile,
stop it.

**Why now.** This supplies the independent response law the influence program
was missing and can select a mobility before a cosmological identity is
attempted.

### Action 5 — recover geometry and a genuine gap

**Output.** On held-out growth histories, recover dimension and causal
geometry without supplied FLRW coordinates. Build the transition or response
operator and measure its smallest nonzero gap across `N`, blocking rules,
seeds, and neighboring admissible laws.

**Falsifier / stop.**

- no stable 3+1-ish geometry basin;
- gap tracks the atom cutoff or finite matrix size;
- scale moves with blocking convention;
- scale exists only for selected seeds; or
- preserving geometry requires a coupling schedule keyed to `N`.

**Why now.** Only a survivor here begins to meet `HC-DU-022`; the analytic
`N_*` skeleton alone does not.

### Action 6 — connect the old influence objects as diagnostics

**Output.**

- Compare true transition Fisher contributions with empirical record
  score-energy shares on held-out histories.
- If the coarse geometry is SPD statistical data, derive whether its
  information metric predicts the affine Bianconi completion.
- Treat Euclidean Bianconi as a declared null mobility unless the microscopic
  response selects it.
- Predeclare one downstream susceptibility or prediction before reading the
  influence profile.

**Falsifier / stop.** No held-out response difference, completion reversal,
or a units map that changes under common rescaling.

**Why now.** This uses the completed influence work as instrumentation without
reopening proxy proliferation.

### Action 7 — only then build the unit-bearing return and forward arrows

**Output.** Convert the generated count/gap into a dimensional memory scale
using the recovered atom density and dimension; construct stress-consistent
retarded response plus positive noise; derive the common-past spectrum and one
background prediction.

**Falsifier / stop.** An inserted `H0`, present age, `N0`, favorable seed,
window, offset, absolute value, or fitted sign.

**Why now.** This is the first stage that can challenge the existing tracker,
early-RMS, sign-persistence, and de Sitter kills.

## 6. Hypothesis, conjecture, and possible-claim ledger

| ID | Hypothesis / conjecture / possible claim | Current warrant and grade | Decisive test | What may not yet be said |
|---|---|---|---|---|
| `WF-H1` | A causal growth law defines a statistical experiment whose Fisher metric can select a coordinate-covariant mobility. | `DERIVED / CONSTRUCTIVELY_REALIZED` for the Bernoulli-link fixture; physical interpretation conditional. | Derive the metric from an admissible full CSG action and compare under nonlinear reparameterization. | Fisher mobility is not yet the unique fundamental DU dynamics. |
| `WF-H2` | Causal closure redistributes and generally reduces observable Fisher response. | `DERIVED / CONSTRUCTIVELY_REALIZED` in the finite transition model. | Prove the data-processing inequality for the declared closure channel and test diverse causets. | The retained-Fisher fraction is not `Lambda` or a physical scale. |
| `WF-H3` | A marginal natural flow can transmute a dimensionless coupling into an invariant count hierarchy. | `CONDITIONALLY_ENTAILED / CONSTRUCTIVELY_REALIZED` algebraically. | Produce the invariant from a path-covariant growth law and show blocking universality. | No hierarchy value, length, or cosmological coincidence is predicted. |
| `WF-F1` | Direct cardinality running `p(N)` is compatible with discrete general covariance. | `FORMALIZATION-FALSIFIED` by the three-event counterexample. | Reopen only if the physical state is enlarged so the compared histories are no longer gauge-equivalent, with that enlargement independently justified. | Statewise relabeling invariance cannot be cited as a repair. |
| `WF-C1` | Fixed CSG couplings can acquire a covariant post-to-post effective flow with an RG-invariant count scale. | `CONJECTURE / DU-H0`. | Exact transformation on small causets, then stable scale under repeated covariant blocking. | Cosmological renormalization is not assumed to generate the needed hierarchy. |
| `WF-C2` | Writing coupling updates as causal records closes the return arrow without an external schedule. | `CONJECTURE / DU-H0`. | Explicit transition law, resource ledger, full path covariance, and an observable difference from fixed-law CSG. | “Feedback” alone is not source ownership or becoming. |
| `WF-C3` | The empirical Track B score-energy profile converges to a true transition-Fisher influence profile for generated records. | `STRUCTURAL_ANALOGY / TESTABLE`. | Simulate held-out histories from an admissible law; compare expected Fisher contributions with empirical score-energy calibration and residuals. | Track B has not retroactively become a Fisher-information decomposition. |
| `WF-C4` | Information geometry on a coarse SPD covariance selects the affine Bianconi mobility. | `CONJECTURE / STRUCTURAL_ANALOGY`. | Derive the SPD state and KL metric from transition statistics; predict Euclidean/affine dissipation before observing either path. | The present affine completion remains unselected. |
| `WF-C5` | A generated transfer-operator gap supplies the dimensional memory scale that breaks the causal-past tracker theorem. | `CONJECTURE / OPEN`. | Stable non-cutoff gap, early-history suppression, late acceleration, sign persistence, and de Sitter stationarity without calibration. | A finite-matrix spectral gap is not dimensional transmutation. |
| `WF-PC1` | An admissible order-first law can make influence profiles useful transition/phase diagnostics. | `POSSIBLE_CLAIM`, not ready. | Predeclared response changes after profile movement on held-out histories and survives completion/data-model controls. | No existing influence functional is selected as dark energy. |

## 7. Stop ledger

| Work no longer worth time | Why stop | Exact reopener |
|---|---|---|
| More normalized influence proxies or endpoint maps | They cannot restore discarded units or choose a response law. | Independent transition response, matched held-out states, and a unit-bearing observable map. |
| More Bianconi relaxation on the same fixed action/mobilities | Completion sensitivity and zero-activity residue are already established. | A microscopic response principle that predicts one mobility and a new held-out basin/dimension. |
| More iid Track B sample-size sweeps | The `N^-1/2`, `N^-1/2`, constant-Gini split is analytic. | A non-iid record law generated by the surviving causal dynamics, with ex ante scaling predictions. |
| Any `p(N)`, `g(N)`, or kernel schedule keyed directly to birth count | The cheapest specimen violates path covariance; birth order becomes observable. | A proof of full discrete covariance, or physical coupling records that make the histories genuinely distinct. |
| Calling statewise permutation invariance “discrete general covariance” | The probe separates them exactly. | Exhaustive natural-labeling equality on the declared finite domain plus a general argument. |
| Spectral gaps measured only in cutoff units | Prior spectral flow already showed cutoff tracking can masquerade as transmutation. | Blocking-invariant gap tied to a beta function or universality class. |
| Geometry tuning at one `N` | Prior governance work found a tuned crossing, not a dimension basin. | Fixed-law dimension plateau across increasing `N` and held-out seeds. |
| CMB, `H(z)`, or `Omega_Lambda` fitting | No admissible growth law or generated physical scale exists. | Actions 1–7 through a unit-bearing response/noise completion. |
| Selecting a favorable stochastic sign or applying `abs` | It defeats the prior sign-persistence test by insertion. | A source-owned sign-persistence law with a positive state/resource ledger. |

## 8. Outcomes whose best use differs from the current synthesis

### 8.1 Track B's correction is a design clue, not only a warning

The fact that observed score energy is **not** Fisher information reveals the
right next comparison. A future transition law supplies both:

- expected Fisher contribution from the law; and
- empirical residual score energy from realized records.

Their difference is a calibrated model-misspecification or nonequilibrium
observable. Track B can become a detector of when the causal growth law stops
explaining its own records.

### 8.2 Completion disagreement is a mobility-selection instrument

The Euclidean/affine Bianconi split should not merely be carried as generic
telemetry. If coarse order statistics form an SPD covariance state, information
geometry makes a sharp ex ante prediction: affine/Fisher mobility should win.
Failure would kill that bridge. The current `0.395652` disagreement is
therefore a high-gain discriminator waiting for a microscopic response model.

### 8.3 Data-processing loss may be more primitive than concentration

The new finite model shows that order affects how much raw transition
information remains observable after causal closure. The ratio

```text
F_downset / F_raw
```

is neither participation, Shannon, nor Gini. It is selected by a channel and a
response experiment. It may be a better bridge observable than another
functional of normalized influence weights.

This does **not** reopen proxy proliferation: it is meaningful only inside a
declared transition law.

### 8.4 The three-part influence reopener is stageable

The synthesis correctly requires response, held-out embedding, and units
together before a physical identification. But they need not be discovered in
one leap. This swing built a response object, then killed its growth law before
units or cosmology. That is productive progress, not a violation of the branch
stop.

## 9. Final unconstrained divergent wish list

Every item below is deliberately
`UNRANKED / UNCOMMITTED / NOT_A_CLAIM`.

### D1 — cosmological renormalization at causal posts

- **Idea/question.** Do fixed CSG couplings transform after a post into an
  effective law with a repeated scale hierarchy?
- **Why it might matter.** Posts are order-defined landmarks and may permit
  running without a birth-label clock.
- **First object.** Derive the exact coupling transformation on finite causets
  with one post and test path covariance before/after it.
- **Known collision.** A post selected because it occurs near the desired epoch
  reimports the cosmic clock.
- **Status.** `UNRANKED / UNCOMMITTED / NOT_A_CLAIM`.

### D2 — coupling records as new causal atoms

- **Idea/question.** Encode the sufficient statistics that update the growth
  coupling as actual events in the order.
- **Why it might matter.** It could turn feedback from an external schedule
  into a source-owned return arrow.
- **First object.** A five-to-eight-event example with explicit update records,
  transition probabilities, and equal path weights.
- **Known collision.** It may merely add bookkeeping atoms under a fixed
  meta-law, reproducing the fixed-law absorber.
- **Status.** `UNRANKED / UNCOMMITTED / NOT_A_CLAIM`.

### D3 — Fisher geometry of the unlabeled-causet transition simplex

- **Idea/question.** Quotient transition probabilities by automorphisms first,
  then compute information geometry directly on unlabeled outcomes.
- **Why it might matter.** The quotient may remove label redundancy before a
  mobility is selected.
- **First object.** Exact Fisher matrices for every unlabeled causet through
  small `n`, with singular strata and automorphism factors explicit.
- **Known collision.** Quotient singularities and changing dimension may make
  a smooth metric ill-defined.
- **Status.** `UNRANKED / UNCOMMITTED / NOT_A_CLAIM`.

### D4 — information lost under causal closure as an order observable

- **Idea/question.** Study
  `1-F_downset/F_raw` as a response-selected measure of causal redundancy.
- **Why it might matter.** It measures how much proposed microhistory becomes
  observationally identical once order is enforced.
- **First object.** Exact values across chains, antichains, diamonds, layered
  causets, and manifold sprinklings.
- **Known collision.** Without a physical raw-link microhistory this is only a
  model-dependent channel statistic.
- **Status.** `UNRANKED / UNCOMMITTED / NOT_A_CLAIM`.

### D5 — Chentsov-style uniqueness as a mobility selector

- **Idea/question.** Does monotonicity under causal coarse-graining select
  Fisher mobility uniquely on the transition family?
- **Why it might matter.** It could replace the Euclidean/affine completion
  choice with an operational theorem.
- **First object.** State the admissible Markov morphisms and test metric
  monotonicity on finite transition simplices.
- **Known collision.** The theorem's assumptions may not survive changing
  state dimension, constraints, or indefinite geometry.
- **Status.** `UNRANKED / UNCOMMITTED / NOT_A_CLAIM`.

### D6 — affine Bianconi mobility from coarse transition covariance

- **Idea/question.** Treat `G` as the covariance/information tensor of causal
  transition features and derive its natural SPD flow.
- **Why it might matter.** It gives the existing Bianconi completion
  disagreement a direct microphysical selector.
- **First object.** One feature map from down-sets to an SPD covariance, its
  KL Hessian, and the predicted dissipation operator.
- **Known collision.** The Bianconi action and the statistical covariance may
  share notation without being the same physical object.
- **Status.** `UNRANKED / UNCOMMITTED / NOT_A_CLAIM`.

### D7 — transfer-operator gap rather than Dirac cutoff gap

- **Idea/question.** Use the spectral gap of the *growth transition operator*,
  not the finite causal-set Dirac matrix, as the memory rate.
- **Why it might matter.** A stochastic mixing gap is naturally tied to
  response and may avoid the prior cutoff-tracking kill.
- **First object.** Transition matrices on small unlabeled causets, gap flow
  under covariant coarse-graining, and neighboring-law controls.
- **Known collision.** Finite-state gaps can still scale only with truncation
  size and disappear in the large-state limit.
- **Status.** `UNRANKED / UNCOMMITTED / NOT_A_CLAIM`.

### D8 — common-past mutual information

- **Idea/question.** Replace prescribed independent marks with mutual
  information induced by overlapping causal transition histories.
- **Why it might matter.** It could derive the common-past noise kernel from
  one growth law rather than append noise.
- **First object.** Joint transition distributions for two future events with
  a controlled shared past and an exact mutual-information curve.
- **Known collision.** It may reproduce the already-killed horizon-scale CMB
  correlations without suppressing early amplitude.
- **Status.** `UNRANKED / UNCOMMITTED / NOT_A_CLAIM`.

### D9 — score-energy residual as a nonequilibrium alarm

- **Idea/question.** Compare empirical Track B score energy with the true
  transition Fisher profile during phases of causal growth.
- **Why it might matter.** A persistent mismatch could detect phase change,
  model failure, or emergence of unmodeled degrees of freedom.
- **First object.** Calibration curves under a known law plus one held-out law
  change.
- **Known collision.** Outliers or heteroskedasticity can mimic the alarm;
  those controls already exist and must remain explicit.
- **Status.** `UNRANKED / UNCOMMITTED / NOT_A_CLAIM`.

### D10 — path-covariance cohomology

- **Idea/question.** Treat log transition weights on the graph of natural
  labelings as a one-form; path covariance is vanishing holonomy around
  diamonds.
- **Why it might matter.** It could turn discrete general covariance into a
  local obstruction calculation rather than exhaustive path enumeration.
- **First object.** Compute cycle sums for the three-event counterexample and
  derive the cocycle condition for one candidate family.
- **Known collision.** A formal zero-curvature condition may restate rather
  than solve the CSG constraints.
- **Status.** `UNRANKED / UNCOMMITTED / NOT_A_CLAIM`.

### D11 — heavy-tail or burst universality after a generated scale

- **Idea/question.** Could an admissible growth transition produce correlated
  bursts below `N_*` and summable increments above it?
- **Why it might matter.** It offers a mechanism-level transition into the
  class where the North-Star half-power is valid.
- **First object.** Increment covariance and tail-index curves on both sides
  of a predeclared generated crossover.
- **Known collision.** Choosing a crossover to recover `-1/2` would repeat the
  target-fitting error; the scale must come first.
- **Status.** `UNRANKED / UNCOMMITTED / NOT_A_CLAIM`.

### D12 — causal order as an information bottleneck selecting dimension

- **Idea/question.** Ask whether the retained-Fisher fraction has a stable
  extremum or plateau near manifoldlike dimension.
- **Why it might matter.** Geometry recovery and response selection might be
  two faces of the same causal compression law.
- **First object.** Compare retained Fisher, Myrheim–Meyer dimension, height
  scaling, and width on matched causal ensembles.
- **Known collision.** Optimizing retained information can trivially prefer
  the antichain, which retains everything but supplies no spacetime.
- **Status.** `UNRANKED / UNCOMMITTED / NOT_A_CLAIM`.

## 10. Files, derivations, and validation

Files created:

```text
explorations/science-council-wild-frontier-next-actions-2026-07-24.md
tests/du_wild_frontier_fisher_csg_scale_bridge_probe.py
tests/artifacts/du_wild_frontier_fisher_csg_scale_bridge_probe_result.json
```

Commands used:

```bash
.venv/bin/python tests/du_bianconi_physical_influence_probe.py
.venv/bin/python tests/du_record_fisher_influence_probe.py
.venv/bin/python tests/du_physical_influence_selector_comparison.py
.venv/bin/python -m py_compile tests/du_wild_frontier_fisher_csg_scale_bridge_probe.py
.venv/bin/python tests/du_wild_frontier_fisher_csg_scale_bridge_probe.py
```

New probe result:

```text
12/12 execution checks pass
artifact SHA-256:
b3eb1907d6a74d0687ae58ef3f8dbd1cbdf4003bfaf61a53ca32a9e5af1959a6
```

The checks establish execution of the declared construction and kill. They do
not establish physical truth.

## Unresolved disagreement with the current synthesis

I agree with every `SWING-DU-PHY-02` scientific disposition and with stopping
standalone influence-proxy work.

I retain two narrow disagreements:

1. “Reopen only when one construction supplies all three” is correct as a
   physical-identification gate, but too coarse as a research sequencing rule.
   The response, embedding, and units legs should be built and killed
   sequentially.
2. “Label-invariant growth” is under-specified. The successor contract must
   require path covariance across natural labelings. Without that, the
   proposed feedback can secretly reimport a birth clock even while every
   displayed formula is permutation-invariant.

Neither disagreement promotes a claim, reopens dark-energy identification, or
changes the existing bank/seed disposition.
