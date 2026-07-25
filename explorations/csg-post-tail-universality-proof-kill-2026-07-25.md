---
title: "CSG post-tail universality proof-or-kill"
date: 2026-07-25
status: paper_core_survives
paper_id: DU-PAPER-013
claim_grade: "DERIVED in a declared classical CSG sequence class; causal-set novelty provisional"
lanes:
  - lane_7
channels:
  - CH-FORMAL
  - CH-MODEL
  - CH-COLLIDE
  - CH-PAPER
---

# CSG post-tail universality proof-or-kill

## Verdict

`paper_core_survives`.

The broad claim that a causal-set post universally produces a half-power is
false. A sharper mathematical core survives:

> For an eventually decreasing positive CSG coupling sequence whose adjacent
> ratios are regularly varying with index \(-\alpha<0\), the post-conditioned
> effective coupling is uniformly controlled by one implicit tail scale
> \(b_P\). The induced exponent is \(-\alpha/(\alpha+1)\). The familiar
> half-power is exactly the \(\alpha=1\) class, not a property of posts alone.

This is a locally derived theorem about classical sequential growth (CSG),
not new physics. It does not select a CSG law, generate posts, recover a
manifold, supply units, establish a cosmological parameter, or extend to
quantum causal-set dynamics.

The primary causal-set collision found the exact post map, its fixed points,
its broad convergence theorem, its unrestricted counterexample, and the
factorial half-power already in the literature. It did **not** find the
regular-ratio rate theorem, its bounded-precursor uniformity, the logarithmic
correction, or the boundary classification below. That novelty judgment is
provisional pending a paper-grade bibliographic review outside causal-set
literature, because the proof method is a standard saddle/concentration
argument even if this CSG statement appears unoccupied.

## 1. What was frozen before deriving an exponent

Let \(t=(t_m)_{m\geq0}\) be a nonnegative CSG coupling sequence. A post with
\(P\) ancestors induces the established binomial transform

\[
T_n(P)=\sum_{k=0}^{P}\binom{P}{k}t_{n+k}.
\]

After a post, empty-past births are excluded. The physical projective
sequence therefore begins at \(T_1\), and the first effective percolation
ratio is \(T_2/T_1\), not \(T_1/T_0\).

The theorem uses the following independently declared tail class.

### Definition — regular-ratio CSG tail

For some \(\alpha>0\), require:

1. \(t_m>0\) eventually;
2. the adjacent ratios
   \[
   r_m=\frac{t_{m+1}}{t_m}
   \]
   are eventually nonincreasing; and
3. for every compact interval \([a,c]\subset(0,\infty)\),
   \[
   \sup_{x\in[a,c]}
   \left|
   \frac{r_{\lfloor xm\rfloor}}{r_m}-x^{-\alpha}
   \right|\longrightarrow0.
   \]

This fixes a tail property of the bare coupling sequence. It does not assume
an after-post exponent.

Define \(b_P\) by the tail-balance condition

\[
\frac{P\,r_{b_P}}{b_P}\longrightarrow1.
\]

With eventual monotonicity one concrete choice is the last integer \(b\) for
which \(P r_b\geq b\). Regular variation then gives
\(b_P\to\infty\) and \(b_P/P\to0\).

## 2. The surviving theorem

### Theorem — bounded-precursor uniform post-tail law

Let \(t\) have a regular-ratio CSG tail of index \(-\alpha<0\), and let
\(h(P)=o(b_P)\). Then

\[
\sup_{1\leq n\leq h(P)}
\left|
\frac{T_{n+1}(P)/T_n(P)}{b_P/P}-1
\right|
\longrightarrow0.
\]

Thus the early post-era projective coupling ratios become
precursor-independent uniformly throughout every window smaller than the
tail-balance scale.

### Proof

For fixed \(P,n\), assign the finite weights

\[
W_{P,n}(k)=\binom{P}{k}t_{n+k},
\qquad 0\leq k\leq P,
\]

and normalize them to a random variable \(K_{P,n}\). Consecutive weights obey

\[
\frac{W_{P,n}(k+1)}{W_{P,n}(k)}
=
\frac{P-k}{k+1}\,r_{n+k}.
\tag{1}
\]

Take \(k=\lfloor x b_P\rfloor\), with \(x\) bounded away from zero and
infinity. Since \(n\leq h(P)=o(b_P)\), regular variation and the definition
of \(b_P\) give, uniformly in the declared \(n\)-window,

\[
\frac{W_{P,n}(k+1)}{W_{P,n}(k)}
\longrightarrow x^{-(\alpha+1)}.
\tag{2}
\]

For every fixed \(\delta>0\), (2) is uniformly greater than one below
\((1-\delta)b_P\) and uniformly less than one above
\((1+\delta)b_P\). Eventual monotonicity makes the weight ratio in (1)
eventually decreasing. Multiplying the ratio bounds across an interval of
order \(b_P\) suppresses both tails exponentially. Since regular variation
also implies \(\log P=O(\log b_P)\), the number of possible terms cannot
overcome that suppression. Therefore

\[
\frac{K_{P,n}}{b_P}\longrightarrow1
\]

in probability, uniformly for \(1\leq n\leq h(P)\), with uniformly
negligible tails.

There is also an exact identity. Shifting all but the final term in
\(T_{n+1}\) gives

\[
\frac{T_{n+1}(P)}{T_n(P)}
=
\mathbb E\!\left[
\frac{K_{P,n}}{P-K_{P,n}+1}
\right]
+
\frac{t_{n+P+1}}{T_n(P)}.
\tag{3}
\]

The last term equals
\(r_{n+P}\Pr(K_{P,n}=P)\) and is killed by the same right-tail bound.
Because \(K_{P,n}/b_P\to1\) and \(b_P/P\to0\), the expectation in (3) is
asymptotic to \(b_P/P\), uniformly in the precursor window. This proves the
claim. \(\square\)

### Power-ratio corollary

If

\[
r_m\sim u\,m^{-\alpha}, \qquad u>0,
\]

then

\[
b_P\sim(uP)^{1/(\alpha+1)}
\]

and

\[
\frac{T_{n+1}(P)}{T_n(P)}
\sim
u^{1/(\alpha+1)}
P^{-\alpha/(\alpha+1)}
\]

uniformly for \(n=o(P^{1/(\alpha+1)})\).

For

\[
t_m=\frac{u^m}{(m!)^\alpha},
\]

the adjacent ratio has exactly this tail. Hence:

| \(\alpha\) | induced exponent |
|---:|---:|
| \(1/2\) | \(-1/3\) |
| \(1\) | \(-1/2\) |
| \(2\) | \(-2/3\) |

The Sorkin--Dou factorial model is the middle row. Its half-power is real,
but tail-class conditional.

## 3. Tight boundary cases

### Lower boundary: transitive percolation

For \(t_m=u^m\), \(r_m=u\) does not decay. The post transform is

\[
T_n(P)=(1+u)^P u^n,
\]

so every projective ratio remains exactly \(u\). This is the
\(\alpha=0\) boundary and has no post-induced running.

### Slowly varying corrections

If

\[
r_m\sim u\,m^{-\alpha}(\log m)^\gamma,
\]

the power exponent remains \(-\alpha/(\alpha+1)\), but the prefactor is not a
constant:

\[
\frac{T_{n+1}}{T_n}
\sim
u^{1/(\alpha+1)}
(\alpha+1)^{-\gamma/(\alpha+1)}
P^{-\alpha/(\alpha+1)}
(\log P)^{\gamma/(\alpha+1)}.
\]

Thus even inside regular variation, a pure-power statement without its
slowly varying factor is false.

### Upper endpoint: finite support

If \(t_m=0\) above a largest index \(M\), then for every fixed \(n<M\),

\[
\frac{T_{n+1}(P)}{T_n(P)}
\sim\frac{M-n}{P}.
\]

This is the \(P^{-1}\) endpoint. It violates eventual positivity, so it is
outside the theorem rather than a counterexample to it. General CSG with
zero transitions makes this a legitimate mathematical boundary case, though
it is not automatically a realistic causal-set dynamics.

### No tail regularity: convergence can fail

Martin, O'Connor, Rideout, and Sorkin already constructed the sparse sequence

\[
t_m=
\begin{cases}
m,&m\text{ a power of two},\\
0,&\text{otherwise},
\end{cases}
\]

for which \(T_2(P)/T_1(P)\) oscillates near \(1/2\) and \(2\).
Regularity assumptions are therefore load-bearing, not cosmetic.

Together the boundaries are tight:

```text
constant ratio       regularly varying decay         finite support
exponent 0        -> alpha/(alpha+1) in (0,1)     -> exponent 1
exact fixed point     tail-class running               endpoint
```

## 4. Deterministic finite controls

The standard-library probe
[`du_csg_post_tail_uniformity_probe.py`](../tests/du_csg_post_tail_uniformity_probe.py)
uses exact rational arithmetic where possible and stable log-summed finite
binomial transforms elsewhere. It passes `8/8` frozen checks.

At \(P=65{,}536\):

| \(\alpha\) | predicted slope | fitted slope | largest sampled \(n\leq\sqrt{b_P}\) relative error |
|---:|---:|---:|---:|
| \(1/2\) | \(-0.333333\) | \(-0.337891\) | \(0.008256\) |
| \(1\) | \(-0.500000\) | \(-0.498091\) | \(0.029970\) |
| \(2\) | \(-0.666667\) | \(-0.649039\) | \(0.097529\) |

The deliberately log-corrected \(\alpha=1,\gamma=2\) family is only
`1.22%` from its implicit \(b_P/P\) target at the largest finite point, while
its ratio to an uncorrected \(P^{-1/2}\) target grows from `4.58` to `7.66`.

For finite support \(M=9\), the normalized endpoint quantity

\[
\frac{P}{M-n}\frac{T_{n+1}}{T_n}
\]

lies between `1.00049` and `1.00147` at \(P=4096\) for
\(n\in\{1,3,5\}\).

The sparse published counterfamily gives, in the window
\(16{,}384\leq P<32{,}768\),

\[
\min T_2/T_1=0.500473,\qquad
\max T_2/T_1=1.996829.
\]

The machine-readable result and figure-ready series are in
[`du_csg_post_tail_uniformity_result.json`](../tests/artifacts/du_csg_post_tail_uniformity_result.json).
These finite calculations test the theorem's seams; they are not being used
as its proof.

## 5. Claim-specific primary-literature collision

### Occupied

1. Rideout and Sorkin,
   [*A Classical Sequential Growth Dynamics for Causal Sets*](https://arxiv.org/abs/gr-qc/9904062),
   derive the nonnegative coupling-sequence representation and CSG transition
   law.
2. Martin, O'Connor, Rideout, and Sorkin,
   [*On the “renormalization” transformations induced by cycles of expansion and contraction in causal set cosmology*](https://arxiv.org/abs/gr-qc/0009063),
   establish the binomial post semigroup, identify transitive percolation as
   the only fixed-point family, exclude nontrivial finite cycles, prove
   pointwise convergence when \(\lim t_m^{1/m}\) exists, and supply an
   unrestricted nonconvergent counterexample. For the zero-root class their
   theorem yields \(T_{n+1}/T_n\to0\), not its decay rate.
3. Dou's thesis,
   [*Causal Sets, a Possible Interpretation for the Black Hole Entropy, and Related Topics*](https://arxiv.org/abs/gr-qc/0106024),
   and Sorkin,
   [*Indications of causal set cosmology*](https://arxiv.org/abs/gr-qc/0003043),
   derive the factorial model's effective \(\sqrt{u/P}\) behavior and stress
   the assumptions behind repeated posts.
4. Varadarajan and Rideout,
   [*A general solution for classical sequential growth dynamics of Causal Sets*](https://arxiv.org/abs/gr-qc/0504066),
   extend the CSG solution to vanishing transition probabilities, which keeps
   the finite-support boundary honest.
5. Dowker and Zalel,
   [*Evolution of Universes in Causal Set Cosmology*](https://arxiv.org/abs/1703.07556),
   extend the effective-coupling result from posts to breaks and partial
   breaks.
6. Zalel,
   [*The structure of covtree: searching for manifestly covariant causal set dynamics*](https://arxiv.org/abs/2008.02607),
   constructs the covariant analogue of cosmic renormalization in covtree.
   It is an adjacent generalization, not a tail-rate classification of CSG
   couplings.

### Residual not found in the claim-specific search

- the implicit balance scale \(P r_{b_P}\sim b_P\);
- a uniform theorem for all \(n=o(b_P)\);
- the full \(-\alpha/(\alpha+1)\) regular-ratio class;
- slowly varying corrections to the apparent power law;
- the joined constant-ratio / regular-ratio / finite-support boundary
  classification.

Searches covered the primary CSG/post papers, their identified modern
covariant extension, and targeted combinations of “causal set,” “post,”
“cosmic renormalization,” “tail,” “regular variation,” and coupling-ratio
asymptotics through 2026-07-25. Failure to find a collision is not proof of
novelty.

## 6. Exact paper disposition

The candidate is no longer “one numerical pattern plus a literature gap.”
It has:

- a frozen sequence class;
- a concise analytic theorem and proof;
- a known special case recovered exactly;
- load-bearing counterfamilies;
- deterministic figure-ready controls; and
- a claim-specific causal-set collision.

Its honest remaining work is paper production plus two hardening tasks:

1. obtain independent mathematical proof review, including whether a more
   general binomial-transform theorem already subsumes the result; and
2. perform a systematic bibliographic search suitable for a novelty statement.

The publishable contribution, if those survive, is a mathematical
classification inside classical CSG. It is not a causal-set cosmology result
and should not be sold as evidence for Dynamic Unity's record-first North
Star.

## 7. Stops

- Do not call the half-power universal across posts.
- Do not infer a selected \(\alpha\), bare coupling sequence, or physical
  trajectory.
- Do not infer post occurrence or recurrence.
- Do not infer manifoldlikeness, locality, continuum geometry, or a viable
  cosmology from convergence toward percolation.
- Do not attach units or identify the effective ratio with \(\Lambda\).
- Do not promote a classical CSG theorem to quantum causal-set dynamics.
- Do not claim final novelty until the mathematical and bibliographic
  hardening tasks close.
