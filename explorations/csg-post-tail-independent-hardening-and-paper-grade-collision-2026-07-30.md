---
title: "CSG post-tail theorem — independent hardening and paper-grade collision"
date: 2026-07-30
status: source_hardened_for_manuscript
doc_type: exploration
claim_grade: "DERIVED in a declared classical CSG sequence class; application novelty qualified by bounded search"
paper_id: DU-PAPER-013
seed_id: DU-SEED-CSG-POST-TAIL-CLASSES
lanes:
  - lane_7
channels:
  - CH-FORMAL
  - CH-MODEL
  - CH-COLLIDE
  - CH-PAPER
probe_ref: tests/du_csg_post_tail_paper_hardening_probe.py
artifact_ref: tests/artifacts/du_csg_post_tail_paper_hardening_result.json
---

# CSG post-tail theorem — independent hardening and paper-grade collision

## Decision

`SOURCE_HARDENED_FOR_MANUSCRIPT`.

The mathematical core of `DU-PAPER-013` survives an independent
line-by-line rederivation, a hostile quantifier audit, a new finite-prefix
control, and a paper-grade collision against the causal-set and general
asymptotic literatures.

One compressed step in the earlier proof has been repaired. Concentration in
a fixed-width window does **not** by itself make the adjacent-ratio observable
converge to one. The correct argument is:

1. prove concentration at the implicit balance scale;
2. use the uniform convergence theorem for regular variation to obtain
   convergence in probability of the ratio observable;
3. prove uniform integrability by separating a fixed central half-window
   from the exponentially suppressed far-left tail; and
4. then pass to expectations.

The repaired proof also makes eventual positivity exact by defining the
balance point only inside the positive tail and treating the arbitrary finite
prefix as a separately bounded contribution.

The hostile audit found a useful strengthening:

> The condition \(n=o(b_P)\) is a genuine scale boundary. If
> \(n/b_P\to c>0\), the normalized response generally converges to a
> \(c\)-dependent value strictly below one.

Thus the paper can state both the bounded-precursor theorem and its
proportional-precursor extension. The latter explains precisely where and how
precursor independence fails.

The novelty conclusion remains deliberately narrow. Regular variation,
consecutive-term saddle localization, discrete Laplace asymptotics, and
large-power coefficient methods are occupied. The bounded search did not
locate the exact CSG application: a uniform regular-ratio index map together
with the proportional-window extension and the boundary classification.
Absence from a bounded search is not proof of priority, so manuscript language
must use “we establish” and “we did not locate,” never an unqualified “first.”

No outside reviewer is a release prerequisite under the standing publication
rule. This receipt supplies the required independent derivation and hostile
verification for source hardening. It does not publish the paper or authorize
an external upload.

## 1. Exact theorem

Let \(t=(t_m)_{m\geq0}\) be nonnegative. Assume there is an integer \(m_0\)
such that \(t_m>0\) for every \(m\geq m_0\). Define, on that positive tail,

\[
r_m=\frac{t_{m+1}}{t_m}.
\]

Assume:

1. \(r_m\) is nonincreasing for \(m\geq m_0\); and
2. \(r\) is regularly varying with index \(-\alpha\), where \(\alpha>0\):
   for every compact \([a,c]\subset(0,\infty)\),
   \[
   \sup_{x\in[a,c]}
   \left|
   \frac{r_{\lfloor xm\rfloor}}{r_m}-x^{-\alpha}
   \right|\longrightarrow0.
   \]

For sufficiently large \(P\), define

\[
b_P=\max\{b\geq m_0:P r_b\geq b\}.
\tag{1}
\]

Let \(h:\mathbb N\to\mathbb N\) satisfy \(h(P)/b_P\to0\), and define the
post transform

\[
T_n(P)=\sum_{k=0}^{P}\binom Pk t_{n+k}.
\tag{2}
\]

Then

\[
\sup_{1\leq n\leq h(P)}
\left|
\frac{T_{n+1}(P)/T_n(P)}{b_P/P}-1
\right|
\longrightarrow0.
\tag{3}
\]

This is a theorem about a declared class of classical sequential-growth
couplings. It does not select the class, produce a post, or give \(b_P/P\)
physical units.

## 2. Proof

### 2.1 The balance point exists and is asymptotically exact

Regular variation with negative index gives \(r_m\to0\) and
\(r_m/m\to0\). For each sufficiently large \(P\), the set in (1) is nonempty
because \(P r_{m_0}\geq m_0\), and finite because \(P r_b/b\to0\) as
\(b\to\infty\).

For every fixed \(B\geq m_0\), \(P r_B\geq B\) when \(P\) is large, so
\(b_P\to\infty\). Maximality gives

\[
\frac{P r_{b_P}}{b_P}\geq1,
\qquad
\frac{P r_{b_P+1}}{b_P+1}<1.
\]

Therefore

\[
1
\leq
\frac{P r_{b_P}}{b_P}
<
\frac{b_P+1}{b_P}\frac{r_{b_P}}{r_{b_P+1}}.
\]

The right side tends to one because consecutive ratios of a regularly
varying sequence tend to one. Hence

\[
\frac{P r_{b_P}}{b_P}\longrightarrow1.
\tag{4}
\]

Since \(r_{b_P}\to0\), equation (4) also gives \(b_P/P\to0\).

### 2.2 Tail weights localize uniformly

On indices where \(n+k\geq m_0\), set

\[
W_{P,n}(k)=\binom Pk t_{n+k}.
\]

Their consecutive ratios are

\[
q_{P,n}(k)
:=
\frac{W_{P,n}(k+1)}{W_{P,n}(k)}
=
\frac{P-k}{k+1}r_{n+k}.
\tag{5}
\]

For \(k=\lfloor x b_P\rfloor\), with \(x\) in a compact subinterval of
\((0,\infty)\), equation (5) factors as

\[
q_{P,n}(k)
=
\frac{P r_{b_P}}{b_P}
\left(1-\frac{k}{P}\right)
\frac{b_P}{k+1}
\frac{r_{n+k}}{r_{b_P}}.
\]

Equations (4), \(b_P/P\to0\), \(n/b_P\to0\), and uniform convergence for
regular variation give

\[
q_{P,n}(\lfloor x b_P\rfloor)
\longrightarrow
x^{-(\alpha+1)}
\tag{6}
\]

uniformly for \(1\leq n\leq h(P)\) and compact \(x\)-ranges.

The binomial factor in (5) decreases with \(k\), and \(r_{n+k}\) is
nonincreasing once its argument is in the declared tail. Consequently
\(q_{P,n}\) is nonincreasing there.

Fix \(\delta\in(0,1)\). Equation (6) supplies a constant
\(\eta_\delta>0\) such that, uniformly in the precursor window and for all
large \(P\):

- weights grow by a factor at least \(1+\eta_\delta\) through a fixed
  fractional interval below \(b_P\); and
- weights decay by a factor at most \(1-\eta_\delta\) through a fixed
  fractional interval above \(b_P\).

Monotonicity extends the comparison toward both endpoints. Multiplying these
ratio bounds across an interval of length proportional to \(b_P\), and
summing the resulting geometric tails, gives constants
\(c_\delta,C_\delta>0\) such that

\[
\sup_{1\leq n\leq h(P)}
\Pr\!\left(
\left|K_{P,n}/b_P-1\right|>\delta
\right)
\leq
C_\delta e^{-c_\delta b_P},
\tag{7}
\]

where \(K_{P,n}\) is distributed according to the normalized positive-tail
weights.

The arbitrary prefix \(m<m_0\) does not alter (7). It contributes only
finitely many values of \(n+k\). Each corresponding binomial coefficient is
polynomial in \(P\), while the ratio product from the first positive-tail
weight to a central weight grows exponentially in \(b_P\). The finite prefix
therefore has normalized mass \(O(P^{m_0}e^{-c b_P})\), uniformly in the
declared \(n\)-window, and this tends to zero.

### 2.3 The expectation step

Within the positive tail,

\[
\frac{
\sum_k\binom Pk t_{n+k+1}
}{
\sum_k\binom Pk t_{n+k}
}
=
\mathbb E_{P,n}[r_{n+K_{P,n}}].
\tag{8}
\]

The finitely many omitted prefix and boundary terms are exponentially small
relative to the central weights, even after division by
\(r_{b_P}=b_P^{-\alpha+o(1)}\). Thus equation (8) differs from the full
\(T_{n+1}/T_n\) by \(o(r_{b_P})\), uniformly in \(n\).

Equation (7), \(n/b_P\to0\), and the uniform convergence theorem imply

\[
\frac{r_{n+K_{P,n}}}{r_{b_P}}
\longrightarrow1
\]

in probability, uniformly in the precursor window. This is the point at
which the earlier proof needs a two-limit argument: for fixed
\(\delta>0\), regular variation only traps the ratio between values near
\((1-\delta)^{-\alpha}\) and \((1+\delta)^{-\alpha}\); one first takes
\(P\to\infty\) and then \(\delta\downarrow0\).

It remains to justify expectations. On
\(\{K_{P,n}\geq b_P/2\}\), eventual monotonicity and regular variation give

\[
0\leq
\frac{r_{n+K_{P,n}}}{r_{b_P}}
\leq
\frac{r_{\lfloor b_P/2\rfloor}}{r_{b_P}}
=O(1).
\]

On the complementary event, the numerator is bounded by the finite maximum
of the positive-tail ratios, while Potter bounds give
\(1/r_{b_P}\leq b_P^{\alpha+\epsilon}\) for any fixed
\(\epsilon>0\) and large \(P\). Equation (7) then yields

\[
\mathbb E\!\left[
\frac{r_{n+K_{P,n}}}{r_{b_P}};
K_{P,n}<b_P/2
\right]
\leq
C b_P^{\alpha+\epsilon}e^{-c b_P}
\longrightarrow0.
\]

The ratio observables are therefore uniformly integrable. Passing to
expectations in (8) gives

\[
\frac{T_{n+1}(P)}{T_n(P)}
\sim r_{b_P}\sim\frac{b_P}{P}
\]

uniformly for \(1\leq n\leq h(P)\), proving (3).

## 3. The window boundary is real

The same ratio method gives a stronger statement. Suppose

\[
\frac{n(P)}{b_P}\longrightarrow c\geq0.
\]

For \(k=\lfloor x b_P\rfloor\), equation (5) now gives

\[
q_{P,n}(k)
\longrightarrow
\frac{1}{x(c+x)^\alpha}.
\tag{9}
\]

The right side is strictly decreasing from infinity to zero, so there is a
unique \(x_c>0\) satisfying

\[
x_c(c+x_c)^\alpha=1.
\tag{10}
\]

The same geometric-ratio argument localizes
\(K_{P,n}/b_P\) at \(x_c\). For uniform integrability, split at
\((x_c/2)b_P\): above that threshold monotonicity and regular variation give
a fixed bound, while below it the geometric tail is exponentially small and
dominates the same polynomial Potter factor used in Section 2.3. Regular
variation then gives

\[
\frac{T_{n+1}(P)/T_n(P)}{b_P/P}
\longrightarrow
(c+x_c)^{-\alpha}
=x_c.
\tag{11}
\]

At \(c=0\), equation (10) gives \(x_0=1\), recovering the bounded-precursor
theorem. For every \(c>0\), \(x_c<1\). Thus \(n=o(b_P)\) is not a decorative
technical restriction: the response changes at the \(b_P\) scale.

For the factorial class \(\alpha=1\),

\[
x_c=\frac{\sqrt{c^2+4}-c}{2}.
\]

The hostile finite probe matches this limit at \(P=65{,}536\) within
\(0.00040\) for \(c\in\{1/2,1,2\}\). It also changes the first five bare
couplings—including zeros and extremely large irregular values—while keeping
the factorial tail fixed. The normalized post response becomes numerically
identical by \(P=4096\), supporting the finite-prefix estimate. These are
controls, not proof.

## 4. Index map and boundaries

If

\[
r_m\sim u\,m^{-\alpha},
\qquad u>0,
\]

then the balance equation gives

\[
b_P\sim(uP)^{1/(\alpha+1)}
\]

and therefore

\[
\frac{T_{n+1}(P)}{T_n(P)}
\sim
u^{1/(\alpha+1)}
P^{-\alpha/(\alpha+1)}
\]

uniformly for \(n=o(P^{1/(\alpha+1)})\).

The map of adjacent-ratio exponents is

\[
-\alpha\longmapsto-\frac{\alpha}{\alpha+1}.
\]

The half-power is the \(\alpha=1\) case, not a universal effect of a post.

The sharp comparison families remain:

- **constant ratio:** \(t_m=u^m\), so the projective ratio stays exactly
  \(u\);
- **regularly varying decay:** the index map above, with slowly varying
  factors carried through the implicit balance equation;
- **finite support:** a \(P^{-1}\) endpoint outside eventual positivity; and
- **irregular sparse support:** no convergence need occur.

## 5. Systematic collision

### 5.1 Search scope

The paper-grade collision covered:

1. the original CSG construction and coupling parametrization;
2. the original cosmic-renormalization paper, including its cited rate and
   counterexample discussion;
3. the factorial example and causal-set cosmology exposition;
4. the general CSG extension allowing zero transition probabilities;
5. the extension from posts to breaks and partial breaks;
6. the covtree analogue and later covariant-growth review;
7. the causal-set Living Review's post-renormalization section and
   bibliography;
8. regular-variation monographs and Potter/uniform-convergence machinery;
9. discrete Laplace and consecutive-term saddle methods; and
10. large-power coefficient asymptotics and Khinchin-family treatments.

Search expressions included combinations of:

- `causal set`, `post`, `cosmic renormalisation`, `coupling`, `rate`,
  `factorial`, `asymptotic`, and `precursor`;
- `binomial transform`, `binomial convolution`, `regular variation`,
  `successive ratios`, and `adjacent ratios`; and
- exact fragments of \(\sum_k\binom Pk t_{n+k}\).

### 5.2 Occupied results

The following are not novel:

- Rideout and Sorkin derive the CSG family and its nonnegative coupling
  parametrization.
- Martin, O'Connor, Rideout, and Sorkin derive the post map, identify the
  transitive-percolation fixed line, exclude nontrivial cycles, establish a
  broad pointwise basin of attraction, and give an irregular nonconvergent
  sequence.
- Sorkin and Dou discuss the factorial family and its half-power behavior.
- Varadarajan and Rideout allow vanishing transitions.
- Dowker and Zalel extend the effective-coupling transformation to breaks.
- Zalel supplies the manifestly covariant covtree analogue and a later
  overview.
- Bingham, Goldie, and Teugels supply the regular-variation tools.
- Gardy, Bender and Richmond, Paris, and the later large-powers literature
  occupy the surrounding saddle, concentration, and coefficient-asymptotic
  methods.

The 2019 causal-set Living Review still summarizes the established
post result as pointwise convergence when the coupling root limit exists. It
does not state a regular-ratio rate, a growing precursor window, or the
proportional-window law.

### 5.3 Residual contribution

The bounded search did not locate an exact prior statement combining:

1. the CSG post transform;
2. an eventually monotone regularly varying adjacent-coupling ratio;
3. the index map \(-\alpha\mapsto-\alpha/(\alpha+1)\);
4. uniformity for every \(n=o(b_P)\);
5. the \(n/b_P\to c\) response \(x_c\);
6. slowly varying and finite-support boundaries; and
7. the published sparse nonconvergent boundary.

That is the defensible manuscript delta. The method is standard; the
application-specific theorem and classification are the contribution.

### 5.4 Novelty language allowed

Allowed:

> We establish a uniform rate classification for a declared regular-ratio
> class of CSG post transforms and identify the precursor scale at which the
> uniform law fails.

Allowed:

> We did not locate this exact CSG statement in the bounded literature
> search.

Not allowed:

- “the first theorem” without qualification;
- “a new asymptotic method”;
- “universal post running”;
- “physical selection of the coupling tail”; or
- a cosmological interpretation of \(b_P/P\).

## 6. Source-to-paper gate

The source gate now passes:

- exact statement with tail-start quantifiers;
- proof with the expectation step repaired;
- arbitrary finite-prefix control;
- a nontrivial proportional-window extension;
- three deterministic probe suites;
- causal-set and general-mathematics collision; and
- explicit physical and novelty limits.

The candidate may move from seed to a canonical Markdown formal draft.

It should remain a short technical causal-set paper. The paper is worthwhile
because it says exactly how a known cosmic-renormalization map approaches its
fixed family for a broad, explicit tail class—and exactly where that
classification stops. It is not the Dynamic Unity flagship and should not be
sold as new fundamental physics.
