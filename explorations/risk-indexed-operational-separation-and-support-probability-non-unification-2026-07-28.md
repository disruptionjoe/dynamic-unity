---
title: "Risk-indexed operational separation and support/probability non-unification"
status: completed_scoped_theorem_and_chsh_control
doc_type: exact_statistical_separation_theorem_support_control_and_reopener_correction
created: 2026-07-28
claim_id: HC-DU-070
work_id: RISK-INDEXED-OPERATIONAL-SEPARATION
program_id: CCR-RISK-INDEXED-OPERATIONAL-SEPARATION
run_id: RUN-20260728-075930-risk-indexed-operational-separation
claim_grade: "SCOPED GRADE-4 EXACT SUPPORT/PROBABILITY NON-UNIFICATION, ROBUST SCORE-SEPARATION THEOREM, MEMORY-ROBUST FINITE-SAMPLE GATE, AND REOPENER CORRECTION / NEYMAN-PEARSON, TOTAL-VARIATION, CONVEX-SEPARATION, HOEFFDING-AZUMA, AND FINITE-STATISTICS BELL COMPONENTS ABSORBED / NO NEW BELL RESULT, QUANTUM PRINCIPLE, PHYSICAL LAW, RECORD ONTOLOGY, GRADE-5 REMAINDER, PREDICTION, PAPER, MODEL, OR HARDWARE RESULT"
paper_state_change: none
prediction_state_change: none
hardware_state_change: none
---

# Risk-indexed operational separation

## Executive result

`HC-DU-069` correctly proved:

> A finite record excludes a completion class with zero error exactly when
> its record fibre lies outside the class's operational closure.

That is not the whole empirical-content question for stochastic physics.
There is a second, non-equivalent object: a family of probability laws over
the admitted finite records.

A null theory can assign positive probability to **every** finite transcript,
making zero-error exclusion impossible, while still imposing probability
bounds that a finite preregistered test can violate at arbitrarily small
declared error.

The resulting ladder is:

```text
support-disjoint finite record
  = zero-error exclusion

overlapping support + positive probability-law margin
  = finite-confidence exclusion

positive repeated-trial margin
  = asymptotically vanishing error

law outside a named family but inside its closed convex hull
  = no uniform bounded-score separation at that interface
```

The CHSH calibration makes the distinction exact.

- Ordinary quantum theory contains a full-support behavior, so every
  nonempty finite CHSH transcript has positive probability under some quantum
  model. No finite transcript logically excludes the whole quantum class.
- Yet the quantum CHSH win ceiling
  \[
  p_Q=\frac{2+\sqrt2}{4}
  \]
  makes \(n\) consecutive wins have quantum-null probability at most
  \(p_Q^n\), even with arbitrary between-trial memory under the frozen
  conditional quantum contract.
- An ideal PR box wins every trial. Therefore the all-win event has type-I
  error at most \(p_Q^n>0\) and type-II error \(0\).

For illustration:

| Declared quantum-null error \(\alpha\) | Minimum consecutive wins |
|---:|---:|
| \(0.05\) | \(19\) |
| \(0.001\) | \(44\) |
| \(2.8665\times10^{-7}\), one-sided five-sigma convention | \(96\) |

These numbers do not propose an experiment or claim a PR box exists. They
prove the type distinction:

```text
no exact finite separator
    does not imply
no finite empirical discriminator.
```

The current Dynamic Unity physical reopener must therefore admit two routes:

1. a support-disjoint finite fibre for zero-error exclusion; or
2. a physically selected probability-law family with a positive robust score
   gap, implementation-complete acquisition, and preregistered error budget.

The mathematics is standard and absorbed. The Dynamic Unity result is the
typed composition of support closure, probability geometry, observer
capability, and evidence grade.

## 1. Two different operational objects

Let \(Z\) be the finite transcript space of one frozen experiment.

### Support object

A completion or support class says which transcripts are possible:

\[
\operatorname{Supp}(\mathcal N)
=
\bigcup_{P\in\mathcal N}\operatorname{supp}(P),
\]

where \(\mathcal N\subseteq\Delta(Z)\) is the null family.

A nonempty event \(E\subseteq Z\) is a zero-error null exclusion when

\[
\sup_{P\in\mathcal N}P(E)=0.
\]

Equivalently,

\[
E\cap\operatorname{Supp}(\mathcal N)=\varnothing.
\]

This is the finite probability-space instance of `HC-DU-069`.

### Probability-law object

A statistical test is a function

\[
\phi:Z\longrightarrow[0,1],
\]

where \(\phi(z)\) is the probability of rejecting the null after transcript
\(z\). For an alternative family
\(\mathcal A\subseteq\Delta(Z)\), define

\[
\alpha(\phi)
=
\sup_{P\in\mathcal N}\mathbb E_P[\phi],
\]

\[
\beta(\phi)
=
\sup_{Q\in\mathcal A}\mathbb E_Q[1-\phi].
\]

Here:

- \(\alpha\) is the worst-case probability of rejecting an admitted null;
- \(\beta\) is the worst-case probability of failing to reject an admitted
  alternative; and
- \(1-\alpha\) is **not** the probability that the null is false.

Zero-error exclusion is the special case \(\alpha=0\) with nonzero power. It
is not the only valid finite evidence contract.

## 2. Full support kills exact exclusion

### Proposition 1 — full-support null obstruction

If \(\mathcal N\) contains a law \(P_*\) satisfying

\[
P_*(z)>0
\qquad
\text{for every }z\in Z,
\]

then every nontrivial test has positive type-I error:

\[
\phi\not\equiv0
\quad\Longrightarrow\quad
\alpha(\phi)>0.
\]

In particular, no nonempty event is a zero-error null exclusion.

### Proof

If \(\phi\not\equiv0\), then some \(z\) has \(\phi(z)>0\). Hence

\[
\mathbb E_{P_*}[\phi]
=
\sum_{z\in Z}P_*(z)\phi(z)>0.
\]

Because \(P_*\in\mathcal N\),
\(\alpha(\phi)\geq\mathbb E_{P_*}[\phi]>0\). \(\square\)

For \(n\) finite trials, the same result holds whenever the null contains a
full-support law on \(Z^n\). An IID full-support member is sufficient but not
necessary.

### Meaning

Full support says:

> No finite observed transcript is logically impossible under the null.

It does not say:

> All finite transcripts have comparable probability under the null and the
> alternative.

Support forgets weights. Statistical testing uses them.

## 3. Convex probability separation

Let:

\[
\mathcal N_c
=
\overline{\operatorname{conv}}(\mathcal N),
\qquad
\mathcal A_c
=
\overline{\operatorname{conv}}(\mathcal A).
\]

Because \(Z\) is finite, these are compact convex subsets of the probability
simplex when the original families are bounded, as they automatically are.

For a score \(s:Z\to[0,1]\), define the robust gap

\[
g(s)
=
\inf_{Q\in\mathcal A_c}\mathbb E_Q[s]
-
\sup_{P\in\mathcal N_c}\mathbb E_P[s].
\]

Define

\[
g^*
=
\sup_{0\leq s\leq1}g(s).
\]

### Theorem 1 — robust score-separation criterion

\[
g^*>0
\quad\Longleftrightarrow\quad
\mathcal N_c\cap\mathcal A_c=\varnothing.
\]

Moreover,

\[
g^*
=
\inf_{\substack{P\in\mathcal N_c\\Q\in\mathcal A_c}}
\operatorname{TV}(P,Q),
\]

where

\[
\operatorname{TV}(P,Q)
=
\frac12\sum_{z\in Z}|P(z)-Q(z)|.
\]

### Proof boundary

For fixed \(P,Q\),

\[
\operatorname{TV}(P,Q)
=
\sup_{0\leq s\leq1}
\left(\mathbb E_Q[s]-\mathbb E_P[s]\right).
\]

The score cube and the two compact convex law sets satisfy the finite-
dimensional minimax hypotheses, so the supremum over scores and infimum over
\((P,Q)\) exchange. Disjoint compact convex sets have positive metric
distance and admit strict linear separation; intersecting convex closures
have distance and robust gap zero. \(\square\)

### Why convex closure is required

If the null may randomize among models, or an unobserved classical variable
chooses a null member, the operational null includes its convex hull.
Separating only the unconvexified catalog can manufacture a false margin.

Likewise, if the alternative is composite, a useful certificate must work
for its declared worst case rather than for a retrospectively selected member.

## 4. Finite-sample theorem with memory

Let \(S_i\in[0,1]\) be a frozen score on trial \(i\), and let
\(\mathcal F_{i-1}\) contain every admitted previous setting, output, record,
and device memory.

Assume the null contract gives:

\[
\mathbb E_P[S_i\mid\mathcal F_{i-1}]
\leq b
\qquad
\text{for every admitted null process and every }i.
\]

Assume the alternative contract gives:

\[
\mathbb E_Q[S_i\mid\mathcal F_{i-1}]
\geq a
\qquad
\text{for every admitted alternative process and every }i,
\]

with \(a>b\). Write \(g=a-b\).

### Theorem 2 — memory-robust bounded-score gate

There exists a threshold test on

\[
\overline S_n
=
\frac1n\sum_{i=1}^nS_i
\]

with type-I error at most \(\alpha\) and type-II error at most \(\beta\)
whenever

\[
\boxed{
n\geq
\frac{
\left(
\sqrt{\log(1/\alpha)}
+
\sqrt{\log(1/\beta)}
\right)^2
}{2g^2}.
}
\]

### Proof

The null conditional-mean bound and Hoeffding's lemma give

\[
\Pr_P(\overline S_n\geq b+t)
\leq
e^{-2nt^2}.
\]

This is a supermartingale concentration result; IID trials are not required.
Similarly, the alternative conditional-mean bound gives

\[
\Pr_Q(\overline S_n\leq a-t)
\leq
e^{-2nt^2}.
\]

A threshold \(\tau\) simultaneously satisfies the two error budgets when

\[
b+\sqrt{\frac{\log(1/\alpha)}{2n}}
\leq
\tau
\leq
a-\sqrt{\frac{\log(1/\beta)}{2n}}.
\]

The boxed sample-size condition is exactly the condition that this interval
is nonempty. \(\square\)

This is sufficient, not generally optimal. Likelihood-ratio,
prediction-based-ratio, or inequality-specific tests can use the same
transcripts more efficiently.

### Corollary 1 — positive robust margin gives asymptotic separation

If one frozen score has \(g>0\) under the complete conditional null and
alternative classes, there is a sequence of finite tests with

\[
\alpha_n\to0,
\qquad
\beta_n\to0.
\]

If the closed convex law families intersect, no single one-round bounded
score has a uniform positive gap. Additional interventions, longer blocks,
or a narrower physically justified class may change the law object; passive
relabeling cannot.

## 5. CHSH exact control

Use the frozen binary CHSH interface:

- uniformly random settings \(x,y\in\{0,1\}\);
- binary outputs \(a,b\);
- no communication during the round;
- setting independence relative to the devices and trial history;
- complete retention of settings and outputs; and
- win score
  \[
  W=\mathbf1[a\oplus b=xy].
  \]

The known ceilings are:

\[
p_L=\frac34,
\qquad
p_Q=\frac{2+\sqrt2}{4},
\qquad
p_{\mathrm{PR}}=1.
\]

The existing `28/28` Dynamic Unity calibration independently checks the
local, quantum, no-signalling, PR, signalling, and invalid controls. This run
does not reconstruct those results.

### Proposition 2 — no finite zero-error quantum exclusion

The quantum class contains the uniform local behavior

\[
P_U(a,b\mid x,y)=\frac14.
\]

With every setting assigned nonzero probability, \(P_U\) gives positive
probability to every finite input-output transcript. By Proposition 1, no
nonempty finite transcript event excludes the complete quantum class with
zero type-I error.

This remains true even though some complete conditional probability tables,
including the PR table, lie outside the quantum set.

### Proposition 3 — all-win finite-confidence separator

Suppose that, conditional on every admitted past history, the next-round law
is quantum and the fresh settings satisfy the frozen CHSH contract. Then

\[
\Pr_Q(W_i=1\mid\mathcal F_{i-1})\leq p_Q.
\]

Therefore:

\[
\Pr_Q(W_1=\cdots=W_n=1)
\leq p_Q^n.
\]

### Proof

Iterated conditioning gives:

\[
\Pr_Q(W_1=\cdots=W_n=1)
=
\mathbb E_Q\left[
\mathbf1_{\{W_1=\cdots=W_{n-1}=1\}}
\Pr_Q(W_n=1\mid\mathcal F_{n-1})
\right]
\]

\[
\leq
p_Q\Pr_Q(W_1=\cdots=W_{n-1}=1).
\]

Iterate to obtain \(p_Q^n\). \(\square\)

An ideal PR box wins with probability \(1\), so the same event has:

\[
\alpha_n\leq p_Q^n>0,
\qquad
\beta_n=0.
\]

Consequently:

\[
n\geq
\left\lceil
\frac{\log\alpha}{\log p_Q}
\right\rceil
\]

is sufficient for a declared quantum-null error \(\alpha\).

The strict inequality \(p_Q^n>0\) for every finite \(n\) is precisely why
this is statistical exclusion rather than logical impossibility.

### Proposition 4 — local versus quantum control

For local histories, the conditional win ceiling is \(b=3/4\). For the
specified ideal Tsirelson-saturating quantum strategy,

\[
a=p_Q.
\]

Theorem 2 gives a conservative sufficient sample count of \(559\) trials for
\(\alpha=\beta=0.05\).

This is only a calibration:

- it is not an optimal Bell-test analysis;
- an actual alternative floor must include source, measurement, loss, drift,
  and acquisition effects;
- a local-null rejection does not establish that the realized law is quantum;
  and
- the known local/quantum separation is not Dynamic Unity novelty.

## 6. Capability and processing

Let \(K\) be a passive Markov kernel applied to the transcript, representing
coarse-graining, forgetting, or stochastic post-processing.

### Theorem 3 — passive data-processing monotonicity

\[
\operatorname{TV}(PK,QK)
\leq
\operatorname{TV}(P,Q).
\]

Therefore the robust score distance between processed null and alternative
families cannot exceed the distance available before processing.

### Proof

Every output score \(s'\in[0,1]\) pulls back to the input score

\[
Ks'(z)=\mathbb E[s'(Z')\mid Z=z]\in[0,1].
\]

The processed optimization ranges over only scores obtainable through this
pullback, a subset of all input scores. \(\square\)

This is the probability-law companion to:

- `HC-DU-050B`'s action-relative history refinement;
- `HC-DU-064`'s capability-record Galois closure; and
- `HC-DU-069`'s topology-refinement monotonicity.

A richer intervention family may increase the best available separation
because it adds experiments. A passive record cannot receive credit for a
gap revealed only after an active capability expansion.

## 7. The corrected evidentiary ladder

### Layer A — exact support

```text
record fibre disjoint from null support
    =>
zero-error finite exclusion.
```

This is the strongest finite certificate and remains governed by
`HC-DU-069`.

### Layer B — finite confidence

```text
overlapping support
+ physically fixed probability law family
+ positive robust score gap
+ complete acquisition and error contract
    =>
finite rejection at declared alpha and beta.
```

This is not logical impossibility, but it is genuine finite empirical
content.

### Layer C — asymptotic separation

```text
history-uniform positive conditional margin
    =>
finite tests whose two errors vanish with trial count.
```

The claim remains relative to the repeated-trial, setting, memory, drift, and
selection contract.

### Layer D — law-family underdetermination

If the relevant closed convex law families intersect, no bounded score on
the frozen transcript has a uniform positive gap. A more capable experiment
may separate them; merely collecting more IID samples from an operationally
identical law cannot.

## 8. Collision with known work

The scientific components are occupied.

- Clauser, Horne, Shimony, and Holt formulated a realizable Bell test in
  [“Proposed Experiment to Test Local Hidden-Variable
  Theories”](https://doi.org/10.1103/PhysRevLett.23.880) (1969).
- Tsirelson bounded ordinary quantum Bell correlations in
  [“Quantum Generalizations of Bell's
  Inequality”](https://www.ma.huji.ac.il/~ohadfeld/Tsirelson/download/qbell80.html)
  (1980).
- Popescu and Rohrlich supplied the no-signalling superquantum foil in
  [“Quantum Nonlocality as an
  Axiom”](https://doi.org/10.1007/BF02058098) (1994).
- Gill explicitly treated Bell-test time, arbitrary memory, martingales, and
  finite statistics in
  [“Time, Finite Statistics, and Bell's Fifth
  Position”](https://arxiv.org/abs/quant-ph/0301059) (2003).
- Zhang, Glancy, and Knill developed memory-robust prediction-based-ratio
  tests in
  [“Asymptotically Optimal Data Analysis for Rejecting Local
  Realism”](https://arxiv.org/abs/1108.2468) (2011).
- Elkouss and Wehner derived sharp finite-data Bell p-value bounds valid with
  arbitrary device memory in
  [“(Nearly) Optimal P-values for All Bell
  Inequalities”](https://arxiv.org/abs/1510.07233) (2015).

Within Dynamic Unity:

- the operational-theory landscape contract already freezes the exact CHSH
  classes;
- the robust history-certificate compiler already uses convex score margins;
- `HC-DU-036D` already gives a simultaneous finite-shot epsilon certificate;
  and
- `HC-DU-069` already isolates zero-error support closure.

`HC-DU-070` does not claim any component as new. It composes them to correct
the repository's physical reopener and prevent support density from being
misreported as empirical vacuity.

## 9. What changes for Dynamic Unity

### Earned

`HC-DU-070` banks:

1. exact non-unification of support closure and probability-law separation;
2. the full-support obstruction to nontrivial zero-error finite tests;
3. robust finite-law separation iff the closed convex law families are
   disjoint;
4. the total-variation expression for the optimal robust score gap;
5. a memory-robust finite-sample gate from conditional score bounds;
6. exact CHSH controls showing finite confidence without finite logical
   exclusion;
7. passive data-processing monotonicity; and
8. a correction to the physical successor gate.

### Corrected physical reopener

A finite physical remainder or rival-excluding result may proceed through
either route:

#### Route 1 — zero error

- physically selected completion/support class;
- explicit operational topology;
- realizable finite record fibre disjoint from the strongest legitimate
  support enlargement; and
- complete acquisition and no-refit proof.

#### Route 2 — controlled risk

- physically selected probability-law class over a frozen complete
  transcript;
- strongest legitimate null convexified before testing;
- positive robust score gap;
- frozen intervention, setting, memory, calibration, drift, loss,
  postselection, and acquisition-visibility contracts;
- preregistered \(\alpha,\beta\) or an equivalent valid sequential evidence
  contract; and
- a held-out physical target or rival that the same score separates without
  refit.

Neither route may infer target-class membership merely by rejecting one
rival.

### Portfolio consequence

The CHSH specimen satisfies the mathematical calibration but does not select
a Dynamic Unity scientific successor:

- the theory classes and score are known and supplied;
- no formed record interface or observer boundary is newly selected;
- no new quantum-strength principle is derived;
- no unexplained physical remainder appears; and
- no new experiment or hardware action is warranted.

The repository remains quiescent. The successor class becomes more accurate,
not more populated.

## 10. What is not earned

- no new Bell, Tsirelson, PR-box, convex-separation, or concentration result;
- no claim that a p-value is the probability a theory is false;
- no quantum membership theorem from a Bell-bound result;
- no physical selection of settings, instruments, records, observers, or
  error budgets;
- no universal IID assumption;
- no proof that every statistically distinct theory is feasibly testable
  under realistic resources;
- no new quantum principle, dynamics, law, or ontology;
- no Grade-5 remainder or prediction;
- no paper selection or promotion; and
- no model, provider, or hardware result.

## 11. Stop and reopener

### Stop

Do not:

- say a full-support or support-dense theory has no empirical content without
  checking its probability laws;
- call a finite-confidence rejection an exact impossibility;
- treat the observed p-value as a posterior probability;
- ignore convex mixtures, history-dependent nulls, setting independence,
  acquisition visibility, or selection effects;
- credit passive records for active experimental separation; or
- rerun CHSH as though the calibration were a DU physical advance.

### Reopener

Reopen a physical candidate only when it supplies, before seeing the result:

1. a physically selected support or probability-law family;
2. the complete finite transcript and observer/action contract;
3. the strongest legitimate support or convex-law enlargement;
4. either a support-disjoint event or positive robust score gap;
5. implementation-complete acquisition, calibration, and selection lineage;
6. an error and resource budget;
7. a held-out target or rival; and
8. a no-refit transfer or realization argument.

## 12. Computation and hardware disposition

No new local model was built. The existing `28/28` exact CHSH landscape probe
was rerun unchanged and passed. The only arithmetic checks evaluated closed-
form sample-count formulas.

No external hardware is required to establish this theorem. A future
physical assay becomes relevant only after a non-calibration candidate
selects its law family, complete interface, score, and target.

## Bottom line

> Exact support closure answers whether a finite record makes a theory
> logically impossible. Probability geometry answers whether a finite test
> makes that theory statistically untenable at declared risk. Physics needs
> both, and neither can substitute for the other.
