---
title: "Representational versus predictive absorption and response-order reopener correction"
status: banked_scoped_result_and_gate_correction
doc_type: exploration
created: 2026-07-30
claim_id: HC-DU-185
run_id: RUN-20260731-033201-predictive-absorption-gate-correction
work_id: PREDICTIVE-ABSORPTION-GATE-CORRECTION
action_id: PREDICTIVE-ABSORPTION-GATE-CORRECTION
program_id: CCR-MINIMAL-PHYSICAL-ANTECEDENT-TO-FINITE-REMAINDER
owner_repo: dynamic-unity
primary_lane: lane_1
supporting_lanes:
  - lane_3
  - lane_4
  - lane_7
channels:
  - CH-FORMAL
  - CH-COLLIDE
  - CH-SYN
  - CH-MODEL
evidence_grade: 4
maximum_grade: 4
---

# Representational versus predictive absorption and response-order reopener correction

## Executive return

```text
REPRESENTATIONAL_ABSORPTION_SEPARATED_FROM_PREDICTIVE_ABSORPTION
+ UNIVERSAL_RESPONSE_HOST_CANNOT_BY_ITSELF_KILL_A_NEW_LAW
+ PREDICTIVE_ABSORPTION_REQUIRES_TARGET_CONSTANCY_ON_THE_INCUMBENT_FIBRE
+ AFTER-FACT_PARAMETER_FIT_IS_NOT_PREDICTION
+ FIRST_NONZERO_RESPONSE_DIFFERENCE_REMAINS_A_VALID_TYPED_TARGET
+ NONSINGULAR_SOURCE_REPARAMETERIZATION_PRESERVES_ITS_ORDER
+ RESPONSE-ORDER_GATE_WAS_OVERCONSTRAINED
+ REOPENER_REWRITTEN_TO_REQUIRE_INCUMBENT-UNDERDETERMINED_NO-REFIT_EXCESS
+ PHYSICAL_INTERFACE_AND_RESPONSE-LAW_SELECTION_REMAIN_SEPARATE_DUTIES
+ NO_RESPONSE_CANDIDATE_SELECTED_YET
+ NO_READY_SUCCESSOR
```

The current campaign required an “invariant higher-response distinction not
absorbed by Peierls, effective-action, Schwinger--Dyson, stochastic-gravity,
relative-Cauchy, or process-tensor theory.” That wording is too strong in the
wrong way.

Several listed absorbers are universal or deliberately broad
**representational frameworks**. A process tensor can represent arbitrary
admissible multi-time quantum response on its declared slots. An effective
action or Schwinger--Dyson hierarchy can represent new interaction terms and
new correlation dynamics. Encoding a candidate inside such a framework does
not show that the incumbent physical antecedents predict its coefficient,
scaling, symmetry relation, or held-out consequence.

If mere representability counts as absorption, almost any future discovery
can be rejected after the fact:

```text
new response observed
-> add the corresponding kernel, vertex, channel, or coefficient
-> framework represents it
-> declare it absorbed.
```

That is refitting, not scientific explanation.

The corrected gate is:

> A candidate response claim is predictively absorbed only when the frozen
> incumbent antecedents make its held-out target constant across the
> incumbent completion fibre. Mere encodability, parameter availability, or
> after-fact fitting is representational absorption only.

This correction does not activate Wave 3. It makes Wave 3 possible to
satisfy without demanding a new mathematical language for every new physical
law.

## 1. Frozen question

> Does “standard response theory can represent the candidate” establish that
> the candidate has no excess physical content, or must absorption require a
> locked incumbent prediction under matched antecedents?

The audit distinguishes:

1. **formal containment:** a framework has enough expressive capacity to
   encode the candidate;
2. **model containment:** some parameter choice or completion reproduces it;
3. **predictive absorption:** all incumbent completions compatible with the
   frozen antecedents agree on the held-out target;
4. **explanatory selection:** the incumbent independently selects the
   relevant parameter, law, interface, and regime; and
5. **empirical success:** the locked prediction survives the held-out test.

Only item 3 defeats a claim of predictive excess. Items 4 and 5 are stronger.

## 2. Exact absorption criterion

Let \(\mathcal C_I(a,r)\) be the incumbent completion fibre compatible with
antecedents \(a\) and training record \(r\). Let \(T\) be a held-out response
target. Let a challenger \(H\) select target value \(T_H(a,r)\) before the
held-out value is revealed.

### Theorem — predictive absorption

The incumbent predictively absorbs the challenger target exactly when

\[
\forall c,c'\in\mathcal C_I(a,r),
\qquad
T(c)=T(c')=T_H(a,r).
\tag{1}
\]

Equivalently, \(T\) is constant on the incumbent fibre and equals the
challenger prediction.

### Proof

If (1) holds, every incumbent completion licensed by the frozen contract
gives the challenger's held-out value, so the challenger adds no prediction
for \(T\). If (1) fails, two incumbent completions consistent with the same
antecedents and training record give different held-out values, so the
incumbent did not determine \(T\). The fact that one completion matches the
challenger establishes representability, not prediction. \(\square\)

This is Dynamic Unity's existing fibre criterion applied to novelty and
absorption rather than record reconstruction.

## 3. Smallest exact counterexample

Consider source values \(x=0,1,2\) and two laws:

\[
f(x)=x,\qquad g(x)=x^2.
\]

Both give the same training packet

\[
(y(0),y(1))=(0,1),
\]

but at the frozen held-out input \(x=2\),

\[
f(2)=2,\qquad g(2)=4.
\]

A polynomial or universal response framework represents both. Therefore:

- \(g\) is representationally absorbed;
- the incumbent family \(\{f,g\}\) does not predict the held-out target;
- a target-blind challenger selecting \(g\) predicts \(4\); and
- choosing \(g\) only after observing \(4\) is a refit.

Restricting the incumbent to \(\{g\}\) before reveal is the positive control:
the target fibre is constant and predictive absorption holds.

Nothing about this example is novel statistics. Its purpose is to prevent a
universal formal language from being mistaken for a physical prediction.

## 4. Why the listed absorbers do not all have the same force

### 4.1 Process tensors

Pollock et al.'s
[process-tensor framework](https://arxiv.org/abs/1512.00589)
is explicitly designed as a universal operational representation of
arbitrary non-Markovian quantum processes on declared intervention slots.
That makes it a powerful type and realizability control.

It does not mean a pre-existing Hamiltonian, state, environment, and
instrument contract predicted every process tensor that the formalism can
represent. A candidate process is killed only if the matched incumbent
contract fixes the same held-out operational statistics without refit.

### 4.2 Effective-action and correlation hierarchies

Calzetta and Hu's
[closed-time-path correlation hierarchy](https://arxiv.org/abs/hep-ph/9903291)
organizes successively higher correlations, truncation, slaving, noise, and
dissipation. It absorbs the generic idea “higher correlations can affect
lower-order dynamics.”

It does not preselect every vertex, state, closure, noise kernel, or
coefficient expressible in that hierarchy. A distinctive coefficient or
relation can remain predictively open even though the hierarchy supplies its
natural mathematical home.

### 4.3 Relative Cauchy evolution

Fewster and Schenkel's
[locally covariant source-response construction](https://arxiv.org/abs/1402.2436)
shows that quotient and functorial structure matter before response objects
can be compared. It is a strong covariance and redundancy absorber.

Again, functorial representability does not select a candidate physical
source, state, detector, coefficient, or record interface.

### 4.4 Nonlinear response theory

Lucarini and Colangeli
[extend fluctuation-response relations to nonlinear orders](https://arxiv.org/abs/1202.1073).
This absorbs the bare conjecture that nonlinear response/correlation
relations exist.

It does not fix every system's first nonzero response coefficient or the
held-out consequences of a new proposed dynamics.

## 5. Response order remains useful after correction

For one frozen physical source \(J\), observable \(O\), and response law,
consider the difference between challenger and incumbent:

\[
\Delta R(J)=R_H(J)-R_I(J).
\]

If

\[
\Delta R^{(0)}(0)=\cdots=\Delta R^{(k-1)}(0)=0,
\qquad
\Delta R^{(k)}(0)\ne0,
\tag{2}
\]

then \(k\) is the first response order at which the laws differ.

Under a smooth local source change \(J=\phi(K)\) with
\(\phi(0)=0\) and \(\phi'(0)\ne0\), the order \(k\) in (2) is preserved.
Higher coefficients mix, but the first nonzero order cannot move because
the leading term is multiplied by \(\phi'(0)^k\).

A singular change such as \(J=K^2\) can change the order and is not an
equivalent local source coordinate. Thus the existing representation
discipline remains valid.

What changes is the novelty test. A physically meaningful first difference
does not need to escape every standard response language. It must:

1. use a frozen physical source, observable, event class, and equivalence;
2. be selected before the held-out measurement;
3. vary across the matched incumbent completion fibre;
4. remain fixed under the challenger without target-dependent refit; and
5. have a finite observable consequence.

## 6. Interface selection is still independent

Correcting absorption does not let a response law create a record interface.
The detector results `HC-DU-178--184` show physically selected formation and
acquisition duties. The response host results show lawful counterfactual
maps. Neither direction implies the other:

```text
selected detector/interface
!= selected fundamental response law;

selected response law
!= selected detector/archive/access quotient.
```

Wave 3 still requires both sides in one source-pinned contract or an exact
typed composition between them.

## 7. Revised campaign gate

Replace:

> exposes a higher-order distinction not absorbed by the standard hierarchy

with:

> locks a finite response target that varies across the matched incumbent
> completion fibre, remains fixed under the challenger without refit, and is
> measured through a physically selected interface.

Standard frameworks remain essential controls:

- they can show that a purportedly new object is merely renamed;
- they can expose supplied slots, states, sources, gauges, and closures;
- they can absorb a generic structural claim already proved in the
  literature; and
- they can provide the correct language for the candidate.

They cannot defeat a locked prediction merely by being able to encode it.

## 8. Grade and consequence

Earned:

- scoped Grade-4 predictive-absorption criterion;
- exact finite representational/predictive counterexample;
- response-order coordinate-stability boundary;
- correction of the Wave-3 reopener; and
- preservation of the interface/law selection split.

Absorbed:

- model comparison, preregistration, sufficient statistics, identifiability,
  and no-refit prediction;
- process-tensor universality;
- effective-action and correlation hierarchies;
- relative Cauchy evolution; and
- nonlinear response theory.

Not earned:

- no specific response law or coefficient is selected;
- no incumbent physical theory is empirically defeated;
- no detector is connected to a distinctive response target;
- no new physics, prediction result, paper, or successor is promoted.

The portfolio remains no-ready, but the route is no longer
self-disqualifying. The next response swing should search for a
source-pinned, preregistrable coefficient, scaling law, symmetry relation, or
finite response statistic that the matched incumbent leaves variable.

## 9. Exact regression

Run:

```bash
python3 tests/du_predictive_vs_representational_absorption_probe.py --write-artifact
```

The artifact is
`tests/artifacts/du_predictive_vs_representational_absorption_result.json`.

Passing establishes:

- two representable laws can share training data and differ held out;
- representability does not imply predictive absorption;
- target-blind selection supplies a locked prediction;
- a target-constant incumbent fibre is the positive control;
- after-fact fitting is not prediction;
- first nonzero response difference is preserved by nonsingular source
  reparameterization and can change under a singular one; and
- response-law selection does not select a physical interface.

It establishes no physical coefficient or new law.
