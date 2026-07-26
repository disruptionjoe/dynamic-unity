---
title: "CSG post-tail theorem — second-method proof audit and general collision"
date: 2026-07-25
status: paper_core_survives_with_novelty_narrowed
doc_type: exploration
claim_grade: "SECOND INTERNAL PROOF ROUTE / GENERAL METHOD OCCUPIED / EXACT CSG COROLLARY NOVELTY PROVISIONAL"
paper_id: DU-PAPER-013
lanes:
  - lane_7
channels:
  - CH-FORMAL
  - CH-COLLIDE
  - CH-PAPER
probe_ref: tests/du_csg_post_tail_second_method_probe.py
artifact_ref: tests/artifacts/du_csg_post_tail_second_method_result.json
---

# CSG post-tail theorem — second-method proof audit and general collision

## Verdict

`PAPER_CORE_SURVIVES_WITH_NOVELTY_NARROWED`.

The bounded-precursor regular-ratio theorem survives a genuinely different
proof route. The new route uses the exact identity

\[
\frac{T_{n+1}(P)}{T_n(P)}
=
\mathbb E_{P,n}\!\left[r_{n+K}\right],
\tag{1}
\]

rather than the shifted-binomial identity used in the first proof. It closes
the two places where the original proof was most compressed:

- uniform control of the far tails; and
- uniform integrability of the transformed-ratio observable.

No contradiction or counterexample was found. The earlier shifted identity is
also exact; it is simply unnecessary.

The general mathematical collision materially narrows the novelty claim.
Regular variation, adjacent-ratio saddle localization, coefficient
asymptotics for large powers, and discrete Laplace methods are established
mathematics. This project must not claim a new asymptotic method.

The residual potentially publishable contribution is only:

> an application-specific, bounded-precursor uniform classification of the
> classical sequential growth post transform by the regular-variation index
> of its adjacent coupling ratios, including its sharp boundary families.

The bounded search found no exact prior statement of that CSG theorem. That
is still provisional. This was a second **internal** derivation, not an
independent expert or peer proof review.

The new probe passes `5/5` checks.

## Statement audited

Let

\[
T_n(P)=\sum_{k=0}^{P}\binom Pk t_{n+k},
\qquad
r_m=\frac{t_{m+1}}{t_m}.
\]

Assume:

1. \(t_m>0\) eventually;
2. \(r_m\) is eventually nonincreasing; and
3. \(r_m\) is regularly varying with index \(-\alpha<0\), uniformly on
   compact multiplicative intervals.

Let \(b_P\) be the last integer \(b\) with \(P r_b\geq b\), and let
\(h(P)=o(b_P)\). The audited conclusion is

\[
\sup_{1\leq n\leq h(P)}
\left|
\frac{T_{n+1}(P)/T_n(P)}{b_P/P}-1
\right|
\longrightarrow0.
\tag{2}
\]

## Second proof

### 1. The implicit scale is asymptotically balanced

Because \(b_P\) is the final integer satisfying \(P r_b\geq b\),

\[
\frac{P r_{b_P}}{b_P}\geq1,
\qquad
\frac{P r_{b_P+1}}{b_P+1}<1.
\]

Regular variation gives \(r_{b_P+1}/r_{b_P}\to1\), so the two inequalities
squeeze

\[
\frac{P r_{b_P}}{b_P}\longrightarrow1.
\tag{3}
\]

Since \(\alpha>0\), \(r_m\to0\). Equation (3) then implies
\(b_P/P\to0\), while \(b_P\to\infty\).

### 2. Post weights concentrate at \(b_P\)

For fixed \(P,n\), normalize

\[
W_{P,n}(k)=\binom Pk t_{n+k},
\qquad 0\leq k\leq P,
\]

to a random variable \(K_{P,n}\). Consecutive weights satisfy

\[
q_{P,n}(k)
:=
\frac{W_{P,n}(k+1)}{W_{P,n}(k)}
=
\frac{P-k}{k+1}r_{n+k}.
\tag{4}
\]

The binomial factor decreases in \(k\), and the tail of \(r\) is
nonincreasing, so \(q_{P,n}\) is eventually decreasing. For
\(k=\lfloor x b_P\rfloor\), uniformly for \(x\) in a compact subset of
\((0,\infty)\) and \(1\leq n\leq h(P)\),

\[
q_{P,n}(k)
\longrightarrow x^{-(\alpha+1)}.
\tag{5}
\]

Here \(n/b_P\to0\), \(b_P/P\to0\), equation (3) supplies the normalization,
and the uniform convergence theorem for regular variation supplies the
uniformity.

Fix \(\delta>0\). Equation (5) gives an \(\eta_\delta>0\) such that, for all
large \(P\), the weights grow by at least \(1+\eta_\delta\) through the last
fixed-width fraction below \((1-\delta)b_P\), and decay by at least a factor
\(1-\eta_\delta\) beyond \((1+\delta)b_P\). Monotonicity extends these bounds
toward the endpoints. Multiplying the ratios across a distance proportional
to \(b_P\) gives

\[
\sup_{1\leq n\leq h(P)}
\Pr\!\left(
\left|K_{P,n}/b_P-1\right|>\delta
\right)
\leq
\exp[-c_\delta b_P]
\tag{6}
\]

after harmless polynomial factors. Thus \(K_{P,n}/b_P\to1\) in probability
uniformly over the bounded-precursor window.

The finite probe directly tracks this localization. At \(P=4096\), for
\(\alpha=1/2,1,2\), the modal index lies within ten percent of the implicit
scale. The measured mass outside a \(25\%\) window around \(b_P\) decreases
with \(P\) in every family. These are finite controls, not the proof.

### 3. Use the direct expectation identity

First suppose \(t_m>0\) throughout the physical sector \(m\geq1\). By
definition of the normalized weights,

\[
\begin{aligned}
\mathbb E_{P,n}[r_{n+K}]
&=
\frac{1}{T_n(P)}
\sum_{k=0}^{P}
\binom Pk t_{n+k}
\frac{t_{n+k+1}}{t_{n+k}}\\
&=
\frac{T_{n+1}(P)}{T_n(P)}.
\end{aligned}
\tag{7}
\]

On the central event in (6), regular variation gives

\[
\frac{r_{n+K}}{r_{b_P}}\longrightarrow1
\]

uniformly in \(n\). The right tail is harmless because eventual
monotonicity bounds this ratio above by a fixed central value.

On the far left, the largest possible numerator is bounded by a finite
initial maximum of \(r\), while regular variation gives
\(1/r_{b_P}=b_P^{\alpha+o(1)}\). The polynomial factor is dominated by the
exponential probability in (6). Hence the family
\(r_{n+K}/r_{b_P}\) is uniformly integrable, and

\[
\sup_{1\leq n\leq h(P)}
\left|
\frac{\mathbb E_{P,n}[r_{n+K}]}{r_{b_P}}-1
\right|
\longrightarrow0.
\tag{8}
\]

Combining (3), (7), and (8) proves (2). \(\square\)

Under the theorem's weaker eventual-positivity statement, choose a fixed
index \(m_0\) beyond which every \(t_m\) is positive. Split from both
transforms the finitely many terms with \(n+k<m_0\). The same left-tail ratio
comparison used in (6) makes their normalized weight—and the corresponding
shifted numerator contribution—exponentially small relative to the saddle,
uniformly in the declared \(n\)-window. Apply equations (7)--(8) to the
positive tail and restore the negligible prefix. This avoids ever dividing
by a zero coupling and gives the same limit.

The exact-rational control uses a strictly positive source and checks equation
(7) and the original shifted identity on every admissible \(n\) for five
finite post sizes. Both hold exactly.

## General mathematical collision

### Occupied method terrain

The proof uses no new general machinery:

- Bingham, Goldie, and Teugels'
  [Regular Variation](https://doi.org/10.1017/CBO9780511721434)
  is the standard source for the uniform convergence and Potter-type controls
  used around equation (5).
- Gardy's
  [coefficient asymptotics for large powers](https://doi.org/10.1016/0012-365X(94)00133-4)
  explicitly studies saddle-point approximations, including approximate
  saddle locations and regimes where coefficient and power indices scale
  differently.
- Paris'
  [discrete analogue of Laplace's method](https://doi.org/10.1016/j.camwa.2011.03.092)
  justifies the same broad move for positive discrete sums by locating their
  maximum through consecutive-term ratios.
- Bender and Richmond's
  [large-power coefficient asymptotics](https://doi.org/10.37236/1440)
  and related local-limit literature occupy the surrounding coefficient and
  concentration methodology.

These sources do not automatically imply equation (2) under exactly the
stated sequence assumptions; translation and uniform precursor control still
need proof. They do prevent any claim that the ratio-defined saddle,
regular-variation scaling, or discrete concentration technique is novel.

### Occupied causal-set terrain

The causal-set collision remains unchanged:

- the CSG dynamics and coupling parametrization are established;
- the post-induced binomial transformation is established;
- transitive percolation is the attractive fixed family;
- unrestricted convergence has known failures; and
- the factorial \(t_n\propto u^n/n!\) half-power example is known.

Primary anchors are Martin, O'Connor, Rideout, and Sorkin's
[renormalization analysis](https://arxiv.org/abs/gr-qc/0009063),
Sorkin's [causal-set cosmology note](https://arxiv.org/abs/gr-qc/0003043),
and Rideout and Sorkin's
[classical sequential growth construction](https://arxiv.org/abs/gr-qc/9904062).

The bounded causal-set and general-mathematics searches did not locate:

- the regular-ratio index map
  \(-\alpha\mapsto-\alpha/(\alpha+1)\);
- uniformity for all \(n=o(b_P)\);
- the slowly varying logarithmic correction in this CSG post setting; or
- the combined constant-ratio, finite-support, and sparse boundary
  classification.

Absence from this search is not proof of novelty.

## Publication consequence

`DU-PAPER-013` is still a plausible short technical paper, but its honest
contribution is narrower than “new post universality” and much narrower than
a new asymptotic method.

The strongest defensible framing is:

> The post map does not itself force a half-power. Under an explicit
> regular-ratio tail class, it converts the bare ratio index into a precise
> effective index, uniformly across bounded precursor sizes; known boundary
> classes show exactly why each assumption matters.

This could be useful to causal-set researchers because it classifies which
bare CSG tails produce which early post-era running. It does not show that any
tail is physically selected, that posts occur in the relevant dynamics, or
that the running has a continuum or cosmological interpretation.

The next paper gate is now small and unforgiving:

1. independent expert proof review, specifically equations (5)--(8);
2. a systematic bibliography search for Tauberian/binomial-transform
   theorems that may subsume (2);
3. a line-by-line collision against every post-renormalization rate result
   cited by Martin et al. and later reviews; and
4. only if all survive, draft the theorem as a CSG corollary using known
   asymptotic machinery.
