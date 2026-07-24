---
title: "SWING-DU-PHY-02 pre-result adversarial audit — physical influence objects, selector, and scale"
status: completed_pre_result_audit
doc_type: adversarial_audit
created: 2026-07-24
swing: SWING-DU-PHY-02
contract: explorations/physical-influence-selector-wave-contract-2026-07-24.md
method: lab/process/conditional-and-abductive-research-contract.md
result_access: "Track A/B/C implementations and results were not inspected or run"
---

# Physical-influence selector: pre-result adversarial audit

## Audit boundary and headline

This is an audit of the frozen constructions, before their result probes exist.
It uses the prior Bianconi, loss, and influence-proxy probes only to recover the
objects that the new contract names. It does not score anticipated checks and
does not infer a scientific pass from contract completeness.

Both proposed constructions can yield legitimate nonnegative normalized
profiles. Neither profile, by itself, can carry an absolute physical scale:
normalization removes the common magnitude exactly. The wave can therefore find
a **live shape object** without finding a selector or a nonzero physical scale.

Four flaws in the frozen contract must remain visible in the result:

1. Track B's declared scalar contributions reconstruct the empirical residual
   loss, not the total Fisher-information matrix. Calling them “Fisher
   contributions” without qualification would be false.
2. Track C asks whether the candidates choose an ordering on previously
   incomparable profiles, but a candidate distribution does not itself define
   an ordering functional. No embedding of those profiles into either physical
   state space is frozen. That question is undefined until both an embedding
   and an independent response functional are supplied.
3. Track A has a physical relaxation variable but a fixed three-mode fixture;
   Track B has record accretion but no common dimensional scale map. The
   contract's “nonzero absolute scale survives growth” question is not
   answerable from normalized weights alone.
4. Track B's pointwise weights are invariant under simultaneous invertible
   linear reparameterization, but an ordinary Euclidean gradient flow is not.
   The multivariate flow needs an explicit mobility, such as the Fisher natural
   gradient, before its trajectory can inherit the claimed invariance.

These are not reasons to cancel the wave. They are reasons to prevent a
constructive object result from being upgraded into a selector or scale result.

## Track A: Bianconi dissipation spectra

### Exact decomposition

Write the Frobenius gradient of the tested real-SPD action as

\[
E(G;G_{\rm ind})
  = \nabla_G S
  = \sigma G^{-1}+\log G-\log G_{\rm ind}.
\]

For the Euclidean completion,

\[
\dot G=-E,\qquad
\frac{dS}{dt}
  =\operatorname{tr}(E\dot G)
  =-\operatorname{tr}(E^2)
  =-D_E .
\]

Because \(E\) is real symmetric, if \(\lambda_i(E)\) are its eigenvalues,

\[
D_E=\sum_i\lambda_i(E)^2,\qquad
a_i^E=\lambda_i(E)^2,\qquad
p_i^E=\frac{a_i^E}{D_E}
\]

is an exact nonnegative decomposition whenever \(D_E>0\).

For the affine-SPD mobility, define

\[
B=G^{1/2}EG^{1/2},\qquad
\dot G=-GEG .
\]

Then

\[
\frac{dS}{dt}
 =-\operatorname{tr}(EGEG)
 =-\operatorname{tr}(B^2)
 =-D_{AI},
\]

so

\[
D_{AI}=\sum_i\lambda_i(B)^2,\qquad
a_i^{AI}=\lambda_i(B)^2,\qquad
p_i^{AI}=\frac{a_i^{AI}}{D_{AI}}
\]

is also exact where \(D_{AI}>0\). Thus both profiles decompose an instantaneous
**action-dissipation rate**. They do not decompose the entropy term alone, the
raw extensive mean, a record count, or a cosmological observable.

### Valid invariance group

For the tested real-SPD model the valid group is simultaneous orthogonal
conjugation:

\[
G\mapsto QGQ^T,\qquad
G_{\rm ind}\mapsto QG_{\rm ind}Q^T,\qquad Q\in O(m).
\]

Functional calculus gives

\[
E\mapsto QEQ^T,\qquad B\mapsto QBQ^T.
\]

Therefore \(D_E,D_{AI}\), and the **unordered multisets** of \(p_i^E,p_i^{AI}\)
are invariant. A sorted profile is invariant; a named mode label is not
canonical through degeneracies or eigenvalue crossings.

This result must not be promoted to arbitrary \(GL(m)\) congruence. In general,

\[
\log(CGC^T)\ne C(\log G)C^T,
\]

and the frozen Bianconi action is not a scalar under arbitrary congruence.
Calling the mobility “affine-invariant” describes the standard SPD metric, not
an enlarged invariance group of this action or of the resulting profile.

### Expected relaxation asymptotic

Near a nondegenerate stationary metric \(G_\star\), let
\(\delta G=G-G_\star\) and let \(\mathcal H_\star\) be the action Hessian. To
leading order,

\[
E=\mathcal H_\star[\delta G]+O(\|\delta G\|^2).
\]

Each completion supplies a different positive mobility \(\mathcal M_\star\):

\[
\dot{\delta G}
 =-\mathcal M_\star\mathcal H_\star[\delta G]
  +O(\|\delta G\|^2).
\]

If the slowest generalized relaxation rate \(r_1>0\) is simple and the initial
condition has a component along its matrix eigenvector \(V_1\), then

\[
E(t)\sim c e^{-r_1t}\mathcal H_\star[V_1],\qquad
D(t)\sim C e^{-2r_1t},
\]

while the normalized profile can converge to

\[
p_i(t)\longrightarrow
\frac{\lambda_i(\mathcal H_\star[V_1])^2}
     {\sum_j\lambda_j(\mathcal H_\star[V_1])^2}.
\]

Thus a nonuniform limiting **shape** can persist while the raw dissipation
vanishes. At the stationary point itself \(D=0\) and \(p\) is undefined. A
degenerate slow subspace makes the normalized limit initial-condition
dependent; different mobilities can change both the slow subspace and the
limiting shape.

### Expected block-growth asymptotic

Track A has no native growing-cell variable. If block replication is used only
as a diagnostic, let one \(m\)-mode block have normalized profile \(q_j\) and
dissipation \(D_0>0\). For \(K\) identical independent blocks,

\[
D_K=KD_0,\qquad p_{kj}=\frac{q_j}{K}.
\]

The three native concentration readings then split:

\[
\lambda_2(K)
 =\sqrt{\sum_{k,j}p_{kj}^2}
 =K^{-1/2}\sqrt{\sum_jq_j^2},
\]

\[
\lambda_H(K)
 =e^{-H(p_K)/2}
 =K^{-1/2}e^{-H(q)/2},
\]

whereas the ordinary Gini coefficient is exactly unchanged by identical
replication (its finite-\(Km\) endpoint normalization has only a vanishing
correction). Meanwhile \(\max p_{kj}=\max q_j/K\to0\). A constant Gini in this
limit is persistent inequality of replicated modal types, not a nonzero
dissipation share or physical amplitude.

### Decisive Track A nulls

1. **Zero-dissipation null.** Set \(G=G_\star\). Then \(E=0\), both \(D\)'s are
   zero, and both profiles are undefined. Returning a uniform distribution, a
   last-step distribution, or a point mass fails the construction.
2. **Nonzero equal-modal null.** Choose an isotropic off-stationary state with
   \(G=gI\), \(G_{\rm ind}=hI\), and \(E=aI\ne0\). Both profiles must be exactly
   uniform even though dissipation is nonzero. This distinguishes dissipation
   magnitude from concentration.
3. **Orthogonal gauge null.** Independently generated \(Q\in O(m)\), applied to
   both \(G\) and \(G_{\rm ind}\), must preserve \(D\) and the sorted profile to
   numerical tolerance. A coordinate-index comparison is not enough.
4. **Common-rate null.** Multiplying every \(a_i\) by the same positive factor,
   whether by action rescaling or time reparameterization, changes the raw
   dissipation rate but leaves \(p\) unchanged. Any scale inferred from \(p\)
   alone fails this null.
5. **Replication null.** Identical block replication must produce the
   \(K^{-1/2},K^{-1/2},K^0\) split above. Treating the Gini leg as an absolute
   nonzero amplitude is a hard failure.

## Track B: observed score-energy profile

### What the formula actually decomposes

Let \(x_i=r_i-\theta\), and retain the frozen common covariance \(\Sigma\).
Then

\[
s_i=\Sigma^{-1}x_i,\qquad
I_N=N\Sigma^{-1},
\]

and therefore

\[
\ell_i=s_i^TI_N^{-1}s_i
       =\frac1N x_i^T\Sigma^{-1}x_i
       =\frac{q_i}{N}.
\]

Consequently,

\[
\sum_i\ell_i
 =\frac1N\sum_iq_i
 =2L_N(\theta),
\qquad
p_i^F=\frac{q_i}{\sum_jq_j}.
\]

This is an exact decomposition of twice the **mean empirical Mahalanobis
loss**. It is not an exact decomposition of the matrix
\(I_N=N\Sigma^{-1}\). For an iid Gaussian location model,
\(E[s_is_i^T]=\Sigma^{-1}\), so the expected matrix Fisher contribution is
identical for every record. The realized scalar \(\ell_i\) instead measures
observed score/residual energy in the total-Fisher metric.

The scientifically safe name is therefore “observed score-energy” or
“observed influence-function energy,” not “per-record Fisher contribution.”
The distinction is load-bearing: the expected information profile is uniform
while the observed residual-energy profile is generically nonuniform.

There is also a normalization convention hidden by \(p\). The Hessian of the
mean loss is \(\Sigma^{-1}\), while \(I_N=N\Sigma^{-1}\) is the information of
the summed log likelihood. Replacing \(I_N\) by the mean information rescales
all \(\ell_i\) by \(N\) and leaves \(p\) unchanged. Thus the normalized profile
cannot decide which raw scale is physical.

### Valid invariance group

For a common affine coordinate change

\[
r_i'=Cr_i+b,\qquad
\theta'=C\theta+b,\qquad
\Sigma'=C\Sigma C^T,\qquad C\in GL(d),
\]

one has

\[
s_i'=C^{-T}s_i,\qquad
I_N'=C^{-T}I_NC^{-1},
\]

and hence \(\ell_i'=\ell_i\). The profile is also equivariant under record
permutations \(S_N\). The valid pointwise group is therefore
\(Aff(d)\times S_N\), with the record weights permuted rather than individually
fixed.

No nonlinear-reparameterization invariance follows from these finite
differences. Nor does pointwise \(GL(d)\) invariance make an ordinary Euclidean
gradient trajectory invariant. For

\[
\nabla_\theta L_N=\Sigma^{-1}(\theta-\bar r),
\]

the Euclidean flow
\(\dot\theta=-\Sigma^{-1}(\theta-\bar r)\) is not equivariant under arbitrary
\(C\). A predeclared Fisher/natural mobility gives

\[
\dot\theta=-\Sigma\nabla_\theta L_N
           =-(\theta-\bar r),
\]

which is affine-equivariant. The Track B implementation must name which
mobility it uses and debit that completion choice.

### Frozen heteroskedastic/correlation inconsistency

The formula \(I_N=N\Sigma^{-1}\) is valid for iid records with one known
covariance. Under independent heteroskedastic records it becomes

\[
I_N=\sum_i\Sigma_i^{-1}.
\]

Under correlated records, the likelihood uses the inverse of the joint block
covariance and generally contains cross-record terms; there need not be a
unique nonnegative per-record decomposition at all.

Therefore the requested heteroskedastic and correlated cases must be labeled
either:

- stress tests against a fixed **reference** metric \(\Sigma\), in which case
  the weights are no longer true-model Fisher quantities; or
- new statistical models with newly declared information metrics and
  decomposition choices.

Silently retaining \(N\Sigma^{-1}\) while calling those cases Fisher leverage
would repair the contract after the fact by equivocation.

### Exact iid-Gaussian asymptotic

Take \(\theta\) to be the fixed true location and
\(r_i\overset{iid}{\sim}N(\theta,\Sigma)\). Then

\[
q_i=x_i^T\Sigma^{-1}x_i\sim\chi_d^2
     =\operatorname{Gamma}(k=d/2,\ {\rm scale}=2),
\qquad
p_i=\frac{q_i}{\sum_jq_j}.
\]

For fixed \(d\) and \(N\to\infty\), the participation amplitude obeys

\[
\sqrt N\,\lambda_2
=\sqrt{N\sum_i p_i^2}
\longrightarrow
\sqrt{\frac{E[q^2]}{E[q]^2}}
=\sqrt{\frac{d+2}{d}}.
\]

For Shannon effective count,

\[
H(p)
=\log N+\log k-\psi(k+1)+o(1),
\]

so

\[
\sqrt N\,\lambda_H
=\sqrt N\,e^{-H(p)/2}
\longrightarrow
\exp\!\left(\frac{\psi(k+1)-\log k}{2}\right).
\]

Both are constant multiples of \(N^{-1/2}\), not nonzero large-\(N\)
amplitudes. They differ only in the prefactor selected by the functional.

In contrast, the normalized Gini coefficient tends to

\[
G_\infty(d)
=\frac{E|q-q'|}{2E[q]}
=\frac{\Gamma(k+1/2)}
       {\sqrt\pi\,\Gamma(k+1)}
>0
\]

for every fixed finite \(d\). The prior proxy's endpoint-matched quantity

\[
\lambda_G=N^{-1/2}+(1-N^{-1/2})G_{\rm norm}
\]

therefore tends to \(G_\infty(d)>0\) even though
\(\max_i p_i\to0\). That nonzero limit is introduced by the affine endpoint
map; it is not a scale derived from the score-energy construction.

If \(\theta=\hat\theta=\bar r\) is estimated from the same records, finite-\(N\)
scores are constrained by \(\sum_i s_i=0\), and

\[
E\!\left[\sum_i\ell_i\right]
=\frac{d(N-1)}{N},
\]

not \(d\). The leading large-\(N\) limits above survive, but the finite-sample
law is not the independent Gamma/Dirichlet law and must not be reported as
such.

This asymptotic split blocks a functional selector. It shows that one live
profile supports three inequivalent native readings; it does not supply an
independent reason to choose one. Track C must encode:

```text
participation: exponent -1/2, prefactor sqrt((d+2)/d), role AMPLITUDE
Shannon:       exponent -1/2, prefactor exp((psi(d/2+1)-ln(d/2))/2),
               role AMPLITUDE
Gini:          exponent 0, limit G_infinity(d), role SHAPE_ONLY
endpoint Gini "Lambda": INVALID_AS_PHYSICAL_SCALE
selector:      OPEN absent an independent response law
```

### Decisive Track B nulls

1. **Equal-radius null.** If every \(q_i=q>0\), then \(p_i=1/N\), regardless of
   the residual directions. The construction deliberately discards angular
   score information.
2. **Zero-residual null.** If every \(r_i=\theta\), then all \(q_i=0\), the
   denominator vanishes, and \(p\) is undefined. This is not the uniform case.
3. **Affine-coordinate null.** A jointly transformed
   \((r_i,\theta,\Sigma)\) must preserve every \(\ell_i\) and \(p_i\). Transforming
   records while leaving the metric fixed is a different physical model, not
   an invariance test.
4. **Exact-duplication null.** Duplicate every record \(K\) times without
   adding independent information. Each copy gets \(p_i/K\);
   participation and Shannon amplitudes acquire \(K^{-1/2}\), while Gini
   remains constant. A claimed information gain or nonzero scale from this
   operation is spurious unless independence is separately justified.
5. **Expected-Fisher null.** Replace realized outer products by their iid
   expectation. Every record contributes the same matrix
   \(\Sigma^{-1}\), so the information profile is uniform. Persistence found
   only in realized residual energy is sample-shape persistence.
6. **Common-rescaling null.** Rescale every \(q_i\) by the same positive
   factor. The empirical loss changes but \(p\) does not. No absolute loss,
   rate, or cosmological scale is recoverable from \(p\) alone.
7. **Outlier/removal null.** A fixed-size outlier is diluted as \(N\) grows
   under the finite-moment iid model. A record retaining nonzero share requires
   \(q_{\rm out}=O(N)\), a heavy-tail/extreme-value mechanism, or correlated
   growth. Remove-one and robust-metric controls must identify which mechanism,
   rather than calling any finite-sample peak persistent.

## What would independently select a functional?

Evaluating three functionals on the same profile is comparison, not selection.
An independent selector must be a law or measurement that is not defined by
the desired functional and that makes different predictions on a predeclared
incomparable pair.

| Functional | An adequate independent selector | What is not enough |
|---|---|---|
| Participation / \(L^2\) | A physical response whose variance is derived as \(\operatorname{Var}(\sum_i p_iX_i)=v\sum_i p_i^2\), with exchangeability/independence tested independently | “Effective count” language or agreement with \(N^{-1/2}\) |
| Shannon / KL | A physical grouping/chain rule, coding multiplicity, likelihood, or thermodynamic work law whose observable is \(-\sum p_i\log p_i\) | Product additivity alone; Rényi-2 is additive under products too |
| Gini / Lorenz | A measured pairwise \(L^1\) disparity, transfer cost, or Lorenz-dominance response proportional to \(E|P-P'|\) | Endpoint-mapping Gini into a quantity named \(\Lambda\) |

The selector must be held out from profile construction, survive coordinate
and completion changes appropriate to its own law, and predict the sign of a
response difference on the old incomparable profile pair. If two functionals
predict the same calibration cases but reverse the held-out pair, observing the
response is selection evidence. Without that response, Track C must return
`SELECTOR_OPEN`.

## Normalized transient versus nonzero physical scale

For any raw nonnegative contributions \(a_i\) and

\[
p_i=\frac{a_i}{A},\qquad A=\sum_i a_i,
\]

one has \(p_i(ca)=p_i(a)\) for every \(c>0\). Every functional of \(p\) alone is
homogeneous of degree zero. It cannot reconstruct the common magnitude \(A\),
its units, or a physical clock rate.

Track C must therefore carry two separate ledgers:

1. **Shape ledger:** \(p\), \(\lambda_2\), \(\lambda_H\), native Gini,
   \(\max p\), and ordering on predeclared profiles.
2. **Scale ledger:** the raw carrier and its units—\(D_E\) or \(D_{AI}\) for
   Track A; \(2L_N=\sum\ell_i\), total likelihood information, and estimator
   error as distinct objects for Track B—plus the exact map, if any, from that
   carrier to a proposed physical observable.

Use the following exact classifications:

- `NORMALIZED_TRANSIENT`: \(p(t)\) is nonuniform for finite time but returns to
  uniform before the physical limit.
- `NORMALIZED_RESIDUE_AT_ZERO_ACTIVITY`: \(p(t)\to p_\star\ne u\) while the raw
  carrier \(A(t)\to0\); the limiting profile is undefined at the endpoint.
- `PERSISTENT_SHAPE_ONLY`: a native concentration statistic has a nonzero
  limit, but \(\max p_i\to0\) or no dimensionful carrier/map survives.
- `FINITE_SAMPLE_AMPLITUDE`: the proposed amplitude is
  \(cN^{-1/2}+o(N^{-1/2})\).
- `NONZERO_PHYSICAL_SCALE`: a predeclared observable with stated units and
  non-fitted normalization has a nonzero limit under the candidate's own
  physical growth/time limit, and a common-rescaling null cannot change that
  conclusion silently.
- `SCALE_UNASSESSED`: no native growth variable or physical units map exists.

A constant normalized Gini with vanishing \(\max p_i\) is
`PERSISTENT_SHAPE_ONLY`, never `NONZERO_PHYSICAL_SCALE`.

## Exact non-scalar Track C schema

Tracks A-Euclidean, A-affine, and B-score must remain three separate candidate
receipts. Do not average the two Track A completions.

For each candidate \(X\), record the typed tuple

```text
R_X = (
  algebra = {
    raw_contributions,
    exact_total_identity,
    nonnegative_domain,
    zero_total_behavior
  },
  invariance = {
    group,
    action_on_state,
    action_on_weights,
    maximality_not_claimed
  },
  evolution = {
    physical_variable,
    mobility_or_accretion_law,
    initial_data,
    endpoint_domain
  },
  shape = {
    lambda_2_native,
    lambda_H_native,
    Gini_native,
    max_weight,
    incomparable_pair_order_vector
  },
  scale = {
    raw_carrier,
    units,
    map_to_physical_observable,
    common_rescaling_result
  },
  asymptotics = {
    limit_definition,
    exponent_and_prefactor_for_each_native_reading,
    raw_carrier_limit,
    max_weight_limit
  },
  selector = {
    selected_functional_or_NONE,
    independent_law,
    held_out_prediction,
    result
  },
  dependencies = {
    completion,
    metric,
    data_model,
    initial_condition,
    fitted_parameters
  },
  nulls = {
    declared_expected_outcomes,
    observed_outcomes
  }
)
```

For every old incomparable pair \((p^L,p^R)\), the ordering field is defined
only if all three items exist:

```text
embedding_X: (p^L,p^R) -> (state_X^L,state_X^R)
matched_controls_X: raw carrier, dimension, and initial data held fixed
response_X: a predeclared physical observable F_X(state)
```

Then, and only then, record

\[
o_X=\operatorname{sgn}\!\left(F_X(state_X^L)-F_X(state_X^R)\right)
\in\{-1,0,+1\}.
\]

If any item is absent, set
`incomparable_pair_order_vector = NOT_EVALUABLE`; do not substitute the signs
of the same three proxy functionals that created the ambiguity.

The Track C comparison object is the product record

```text
R_C = {
  candidates: [R_AE, R_AAI, R_BF],
  algebra_failures: set(candidate, identity),
  invariance_failures: set(candidate, group_element),
  ordering: [o_AE, o_AAI, o_BF] or NOT_EVALUABLE entries,
  asymptotic_signature: {
    lambda_2: [(exponent, prefactor) by candidate],
    lambda_H: [(exponent, prefactor) by candidate],
    Gini: [(limit, role=SHAPE_ONLY) by candidate],
    raw_carrier: [limit by candidate]
  },
  selector_relation:
    SAME_INDEPENDENT_SELECTOR |
    DIFFERENT_INDEPENDENT_SELECTORS |
    SELECTOR_OPEN,
  scale_relation:
    NONZERO_PHYSICAL_SCALE |
    FINITE_SAMPLE_ONLY |
    SHAPE_ONLY |
    SCALE_UNASSESSED,
  disagreement_attribution:
    subset(COMPLETION, METRIC, DATA_MODEL, INITIAL_CONDITION,
           GROWTH_MAP, CONCEPT_INVARIANT),
  disposition
}
```

No field is converted to a number and no count of passing fields enters the
disposition.

## Root checklist and exact disposition logic

1. **Algebra root.** Does each candidate reconstruct its declared total on its
   declared nonzero domain?
   - No: `FORMALIZATION-LOCAL-FAIL`.
   - Yes: continue.
2. **Invariance root.** Does the full state transformation preserve the sorted
   profile under exactly the named group?
   - No: `FORMALIZATION-LOCAL-FAIL`.
   - Yes: continue.
3. **Zero-domain root.** Is \(A=0\) reported as undefined rather than filled?
   - No: `FORMALIZATION-LOCAL-FAIL`.
   - Yes: continue.
4. **Ordering root.** Are an embedding, matched controls, and an independent
   response frozen for the old incomparable pair?
   - No: `ORDERING_QUESTION_NOT_EVALUABLE`; continue without treating this as
     agreement or disagreement.
   - Yes: record the sign vector without voting.
5. **Persistence root.** In the candidate's own physical limit, report both
   the normalized shape and raw carrier.
   - Nonuniform \(p\) with raw carrier \(\to0\):
     `NORMALIZED_RESIDUE_AT_ZERO_ACTIVITY`.
   - Native inequality constant but all shares vanish:
     `PERSISTENT_SHAPE_ONLY`.
   - \(N^{-1/2}\) amplitude: `FINITE_SAMPLE_AMPLITUDE`.
6. **Scale root.** Is there a predeclared, unit-bearing, non-fitted map from the
   raw carrier to an observable with a nonzero physical limit?
   - No native limit/map: `SCALE_UNASSESSED`.
   - Map exists but vanishes: `TRANSIENT-ONLY` or `FINITE_SAMPLE_ONLY`.
   - Map survives and passes rescaling/growth controls: scale leg may pass.
7. **Selector root.** Does an independent law choose participation, Shannon,
   or Gini and make a held-out prediction?
   - No: `SELECTOR_OPEN`.
   - Yes: selector leg may pass.
8. **Final conjunction.**
   - `PHYSICAL-SELECTOR-FOUND` requires algebra and invariance passes **and**
     an independent selector **and** a non-fitted nonzero physical scale.
   - A valid live profile with either selector or scale open is
     `OBJECT-FOUND / SELECTOR-OPEN`.
   - A normalized profile whose physical carrier vanishes or whose only
     amplitude is finite-sample is `TRANSIENT-ONLY`/`FINITE_SAMPLE_ONLY` at the
     scale leg, even if its Gini shape persists.
   - `CONCEPT-PRESSURE` requires a shared failure traced to the declared
     concept invariant after completion, metric, data-model, initial-condition,
     and growth-map failures have been separated. The Gaussian
     participation/Shannon/Gini split is not such a shared invariant failure;
     it is precisely evidence that the functional selector remains open.

## Pre-result audit verdict

Track A can validly construct an orthogonal-similarity-invariant decomposition
of instantaneous action dissipation. Track B can validly construct an
affine-coordinate-invariant decomposition of observed empirical
Mahalanobis-loss energy under the iid common-covariance model. Those are real
constructive advances if their checks pass.

The frozen wave does not yet contain:

- a canonical ordering functional on the previously incomparable profiles;
- a common growth embedding for Track A;
- a true Fisher decomposition for heteroskedastic or correlated Track B cases;
- or a unit-bearing map by which a normalized profile supplies a nonzero
  physical scale.

Accordingly, the strongest result available without additional independent
physics is `OBJECT-FOUND / SELECTOR-OPEN`. In particular, the anticipated iid
Gaussian split—participation and Shannon amplitudes proportional to
\(N^{-1/2}\), normalized Gini approaching a nonzero constant—must be recorded
as a functional-role conflict. It cannot be used to select Gini or to claim a
persistent cosmological amplitude.
