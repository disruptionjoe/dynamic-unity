---
title: "AQFT standard split inclusions: relative-entropy classes, uniform finite compression, and the remaining record boundary"
date: 2026-07-29
status: banked_scoped_result
claim_id: HC-DU-134
work_id: CCR-AQFT-SPLIT-RELATIVE-ENTROPY-UNIFORM-COMPRESSION
primary_lane: lane_1
supporting_lanes:
  - lane_3
  - lane_4
  - lane_7
channels:
  - CH-FORMAL
  - CH-COLLIDE
  - CH-SYN
evidence_grade: 4
maximum_grade: 4
novelty_status: absorbed_mathematics_typed_du_composition
---

# AQFT standard split inclusions: relative-entropy classes, uniform finite compression, and the remaining record boundary

## Result in one paragraph

`HC-DU-133`'s nonuniformity obstruction has a sharp conditional repair. Let a
standard split triple select its canonical type-\(I_\infty\) factor and faithful
reference density \(\sigma\). Although no finite spectral corner approximates
all normal states, the same corners **do** uniformly approximate every forward
relative-entropy ball

\[
\mathcal K_D(\sigma)
=\{\rho:\ D(\rho\Vert\sigma)\le D\}.
\]

If \(P\) is a finite spectral projection of \(\sigma\),
\(q=\operatorname{Tr}\sigma(1-P)\), and
\(p_\rho=\operatorname{Tr}\rho(1-P)\), binary data processing gives

\[
p_\rho
\le
\min\!\left\{
1,\frac{D+\log2}{\log(1/q)}
\right\}.
\]

The right side tends to zero as the reference tail \(q\) tends to zero. A
reference-relative CPTP compression into \(P\mathcal K\) then approximates the
whole class uniformly, including under every fixed downstream channel, with an
explicit trace-norm error tending to zero. This is the exact positive missing
from `HC-DU-133`: one canonical finite carrier can control a nontrivial,
infinite family of states. The orientation is load-bearing. Reverse balls
\(D(\sigma\Vert\rho)\le D\), bounded von Neumann entropy, and bounded rank all
admit states that escape completely into the spectral tail. The result still
does not select the entropy radius, physical state/process family, tolerance,
probe, acquisition, archive, observer access, or held-out target. It is a
conditional finite state-family approximation theorem, not a formed record or
new physics.

## 1. Question inherited from `HC-DU-133`

The standard split triple

\[
\Lambda=(A,B,\Omega)
\]

canonically selects an intermediate type-I factor

\[
N_\Lambda\cong B(\mathcal K)
\]

and the distinguished vector state restricts to a faithful density

\[
\sigma=\rho_\Lambda>0,\qquad
\operatorname{Tr}\sigma=1.
\]

In the nontrivial AQFT setting, \(\mathcal K\) is infinite-dimensional and
\(\sigma\) has infinite rank.

For a declared spectral threshold \(\tau>0\),

\[
P_\tau=\mathbf1_{[\tau,\infty)}(\sigma)
\]

has finite rank and approximates \(\sigma\). But `HC-DU-133` also gave the
obvious uniformity kill: a pure state supported in
\((1-P_\tau)\mathcal K\) places no mass in the retained corner.

That kill answers the unrestricted question. It does not answer the sharper
one:

> Is there a state family warranted by the same reference state for which the
> canonical spectral corners are uniformly sufficient at finite resolution?

Forward relative entropy is the strongest cheap candidate because it is:

- defined by the selected reference state;
- representation invariant;
- monotone under physical channels;
- available on type-I and type-III algebras; and
- already established as a compactness/coercivity instrument in
  infinite-dimensional quantum information.

## 2. Primary-source and novelty boundary

The ingredients are mature:

- Umegaki introduced operator-algebraic relative entropy in
  [“Conditional expectation in an operator algebra, IV”](https://doi.org/10.2996/kmj/1138844604).
- Lindblad proved monotonicity under trace-preserving completely positive maps
  in
  [“Completely positive maps and entropy inequalities”](https://doi.org/10.1007/BF01609396).
- Winter's coding work contains the standard gentle-measurement estimate; see
  [“Coding Theorems of Quantum Information Theory”](https://arxiv.org/abs/quant-ph/9907077).
- Shirokov proves a more general compactness statement: for a compact
  reference set \(C\), trace-bounded positive operators lying at bounded
  relative entropy from some member of \(C\) form a trace-norm compact set.
  See Lemma 9 of
  [“Convergence criterion for quantum relative entropy and its use”](https://doi.org/10.4213/sm9794e).
- The standard-split antecedent remains the Doplicher--Longo construction
  audited in `HC-DU-133`.

No new relative-entropy, compactness, or AQFT theorem is claimed. The Dynamic
Unity increment is:

1. the exact composition with the canonical standard-split density;
2. an explicit spectral-tail and deterministic-compression bound;
3. the reverse-orientation counterexample;
4. the distinction between compact state-family control and a formed finite
   record; and
5. the corrected finite-QFT selector ladder.

## 3. Typed setup

Let \(\mathcal K\) be separable and infinite-dimensional. Let

\[
\sigma>0,\qquad \operatorname{Tr}\sigma=1
\]

be the faithful density selected by the standard split triple on
\(N_\Lambda\cong B(\mathcal K)\).

For any density \(\rho\), write the Umegaki relative entropy

\[
D(\rho\Vert\sigma)
=\operatorname{Tr}\rho(\log\rho-\log\sigma)
\]

with its usual extended-value convention. Fix a finite radius
\(D_0<\infty\) and define

\[
\mathcal K_{D_0}(\sigma)
=\{\rho:\ D(\rho\Vert\sigma)\le D_0\}.
\]

Let \(P\) be a nonzero finite-rank spectral projection of \(\sigma\), set
\(Q=1-P\), and define

\[
q=\operatorname{Tr}(\sigma Q),\qquad
p_\rho=\operatorname{Tr}(\rho Q).
\]

For the threshold projection \(P=P_\tau\), trace-class summability gives

\[
q=q_\tau\longrightarrow0
\qquad(\tau\downarrow0),
\]

while

\[
\operatorname{rank}P_\tau\le\frac1\tau.
\]

The declared packet is:

| Object | Status |
|---|---|
| AQFT net, representation, and nested regions | supplied |
| standard vector/reference state | supplied or theory-selected only in the declared model |
| canonical split factor \(N_\Lambda\) | selected relative to the standard triple |
| faithful density \(\sigma\) | selected by restriction of that state |
| forward orientation \(D(\rho\Vert\sigma)\) | mathematical choice justified below |
| radius \(D_0\) | supplied admissibility/resource parameter |
| spectral threshold or target error | supplied accuracy parameter |
| finite compression map | canonically constructed relative to \((\sigma,P)\), not dynamically selected |
| probe, write, archive, access, and target | not supplied by this theorem |

## 4. Proposition A — forward relative entropy forces uniform spectral tightness

Apply the two-outcome measurement

\[
\mathcal M_P(\rho)
=\big(\operatorname{Tr}\rho P,\operatorname{Tr}\rho Q\big)
=(1-p_\rho,p_\rho).
\]

Lindblad monotonicity gives

\[
D(\rho\Vert\sigma)
\ge
d(p_\rho\Vert q),
\]

where

\[
d(p\Vert q)
=p\log\frac pq+(1-p)\log\frac{1-p}{1-q}.
\]

Rewrite:

\[
d(p\Vert q)
=p\log\frac1q
-h_2(p)
-(1-p)\log(1-q),
\]

with binary entropy

\[
h_2(p)=-p\log p-(1-p)\log(1-p).
\]

Since

\[
h_2(p)\le\log2
\]

and

\[
-(1-p)\log(1-q)\ge0,
\]

we obtain

\[
d(p\Vert q)
\ge
p\log\frac1q-\log2.
\]

Therefore every \(\rho\in\mathcal K_{D_0}(\sigma)\) satisfies

\[
\boxed{
p_\rho
\le
b(D_0,q)
:=
\min\!\left\{
1,\frac{D_0+\log2}{\log(1/q)}
\right\}.
}
\]

For fixed \(D_0\),

\[
b(D_0,q)\longrightarrow0
\qquad(q\downarrow0).
\]

Thus:

\[
\boxed{
\sup_{\rho\in\mathcal K_{D_0}(\sigma)}
\operatorname{Tr}\rho(1-P_\tau)
\longrightarrow0.
}
\]

This is uniform tightness in the **same** basis-free spectral family selected
by \(\sigma\). It directly repairs the unrestricted nonuniformity in
`HC-DU-133` after the forward-relative-entropy class is declared.

The exact best binary bound can be written

\[
p_\rho
\le
\sup\{p\in[0,1]:d(p\Vert q)\le D_0\}.
\]

The displayed \(b(D_0,q)\) is less sharp but explicit and sufficient.

## 5. Corollary — the forward-relative-entropy ball is trace-norm compact

The state space on an infinite-dimensional Hilbert space is not compact in
trace norm. A closed family of density operators is trace-norm compact exactly
when it is uniformly tight with respect to finite-rank projections.

The set \(\mathcal K_{D_0}(\sigma)\) is closed because relative entropy is
lower semicontinuous. Proposition A supplies one increasing family of
finite-rank projections with uniformly vanishing tails. Hence

\[
\boxed{
\mathcal K_{D_0}(\sigma)
\text{ is compact in trace norm.}
}
\]

This is the singleton-reference specialization of Shirokov's more general
compact-reference-set theorem.

Compactness has a precise but limited consequence:

> At every nonzero trace-distance tolerance, finitely many states cover the
> whole admitted family.

It does not canonically choose the covering centers and does not turn a density
matrix into a finite classical output alphabet.

## 6. Proposition B — one canonical finite-output channel controls the family

Define the normalized retained reference state

\[
\sigma_P
=\frac{P\sigma P}{1-q}.
\]

Now define

\[
\mathcal C_P(\rho)
=P\rho P+\operatorname{Tr}(\rho Q)\sigma_P.
\]

This map:

- is completely positive;
- is trace preserving;
- has output supported on finite-dimensional \(P\mathcal K\);
- fixes every input already supported in \(P\mathcal K\);
- uses no basis inside a degenerate spectral subspace; and
- is equivariant under unitary equivalences carrying \((\sigma,P)\) to the
  corresponding pair.

It is a natural **choice** relative to \((\sigma,P)\), not a theorem of unique
physical implementation.

Let \(p=p_\rho\). The gentle-measurement bound gives

\[
\|\rho-P\rho P\|_1\le2\sqrt p.
\]

Since

\[
\|p\sigma_P\|_1=p,
\]

the triangle inequality gives

\[
\boxed{
\|\rho-\mathcal C_P(\rho)\|_1
\le
2\sqrt p+p.
}
\]

Combining with Proposition A:

\[
\boxed{
\sup_{\rho\in\mathcal K_{D_0}(\sigma)}
\|\rho-\mathcal C_P(\rho)\|_1
\le
\varepsilon(D_0,q)
:=
\min\{2,\,2\sqrt{b(D_0,q)}+b(D_0,q)\}.
}
\]

For \(P=P_\tau\),

\[
\varepsilon(D_0,q_\tau)\longrightarrow0.
\]

So one canonical spectral family and one canonical reference-relative
compression family uniformly approximate the whole forward-relative-entropy
ball.

## 7. What the uniform bound transfers

Let \(\Phi\) be any **fixed** CPTP downstream process. Contractivity gives

\[
\|\Phi(\rho)-\Phi(\mathcal C_P(\rho))\|_1
\le
\varepsilon(D_0,q).
\]

For every fixed output effect \(0\le E\le1\),

\[
\left|
\operatorname{Tr}E\Phi(\rho)
-\operatorname{Tr}E\Phi(\mathcal C_P(\rho))
\right|
\le
\frac12\varepsilon(D_0,q).
\]

The same estimate survives an arbitrary spectator/reference system. If a
joint state \(\rho_{\mathcal K R}\) has marginal
\(\rho_\mathcal K\in\mathcal K_{D_0}(\sigma)\), then
\(\mathcal C_P\otimes\operatorname{id}_R\) obeys the same
\(2\sqrt p+p\) bound by applying the projection \(P\otimes1_R\).

This earns a real uniformity statement:

> Every fixed bounded target experiment downstream of the admitted input
> family is uniformly approximated by a finite system carrier.

It does **not** earn uniform reconstruction of an unknown channel, an
arbitrary multi-time process, or an instrument family. Those objects must be
fixed independently before trace-distance contractivity applies.

## 8. Type-III-to-type-I restriction bridge

The result is not limited to state families first defined on the type-I
factor.

Let \(\widehat\rho,\widehat\sigma\) be normal states on an outer AQFT algebra
containing \(N_\Lambda\), with \(\widehat\sigma|_{N_\Lambda}=\sigma\).
Monotonicity of Araki relative entropy under restriction gives

\[
S_{\mathrm{outer}}(\widehat\rho\Vert\widehat\sigma)
\ge
D_{N_\Lambda}
\big(
\widehat\rho|_{N_\Lambda}
\Vert
\widehat\sigma|_{N_\Lambda}
\big).
\]

Therefore a full-algebra family satisfying

\[
S_{\mathrm{outer}}(\widehat\rho\Vert\widehat\sigma)\le D_0
\]

has restrictions uniformly controlled by the canonical finite split
compressions.

This bridge is useful because the outer local algebra may be type III and have
no density matrix or ordinary von Neumann entropy, while the canonical split
factor is type I and does.

The bridge still controls only the **restricted state family**. It does not
prove that the finite corner is an intermediate algebra containing \(A\), or
that every outer-algebra action descends through the compression.

## 9. Proposition C — the direction of relative entropy is essential

Forward and reverse relative entropy are not interchangeable.

Let

\[
\sigma=\sum_{n\ge1}s_n|e_n\rangle\langle e_n|,
\qquad
s_n>0,\qquad
s_n\longrightarrow0.
\]

Fix \(0<c<1\) and define

\[
\rho_n
=(1-c)\sigma+c|e_n\rangle\langle e_n|.
\]

The states commute with \(\sigma\), and

\[
\rho_n\ge(1-c)\sigma.
\]

Hence

\[
D(\sigma\Vert\rho_n)\le-\log(1-c)
\]

for every \(n\). Explicitly,

\[
D(\sigma\Vert\rho_n)
=(1-s_n)(-\log(1-c))
+s_n\log
\frac{s_n}{(1-c)s_n+c}.
\]

For every fixed finite spectral projection containing only finitely many
\(e_n\), choose \(n\) outside it. Then

\[
\operatorname{Tr}\rho_n(1-P)
\ge c.
\]

Therefore:

\[
\boxed{
\{\rho:D(\sigma\Vert\rho)\le D_0\}
\text{ need not be uniformly tight for any }D_0>0.
}
\]

Indeed choose \(c\le1-e^{-D_0}\).

By contrast,

\[
D(|e_n\rangle\langle e_n|\Vert\sigma)
=-\log s_n\longrightarrow\infty.
\]

The forward ball excludes precisely this tail escape.

## 10. Proposition D — entropy and rank are insufficient substitutes

The pure states

\[
\pi_n=|e_n\rangle\langle e_n|
\]

obey

\[
S(\pi_n)=0,\qquad
\operatorname{rank}\pi_n=1.
\]

Yet for every fixed finite spectral \(P\), some \(\pi_n\) satisfies

\[
\operatorname{Tr}\pi_n(1-P)=1.
\]

Thus none of the following alone supplies uniform spectral control:

- finite von Neumann entropy;
- a uniform upper bound on von Neumann entropy;
- finite rank; or
- a uniform rank bound.

The issue is not how mixed each state is. It is whether the family is
uniformly localized relative to the reference-state spectrum.

## 11. No universal dimension or resource law follows

For a fixed \(\sigma\), the theorem guarantees a finite rank at every nonzero
error. It gives no reference-independent rank rate.

The required rank depends on the tail profile of \(\sigma\). Across faithful
trace-class densities, that tail may decrease arbitrarily slowly. Even the
reference state itself lies in every forward ball, so any universal
dimension bound would have to uniformly approximate every faithful density's
own spectrum, which is impossible without an additional spectral-decay,
nuclearity, energy, entropy, geometry, or model-class hypothesis.

Accordingly:

```text
finite rank exists at each declared tolerance
  != universal rank-versus-error law
  != area law
  != detector cost
  != finite record bits
```

Nuclearity or model-specific split-entropy bounds may constrain the spectrum,
but that is an additional theorem and must be carried explicitly.

## 12. Why this is still not a formed record

The result advances the state-carrier rung but not the formation rung.

### 12.1 The class radius is not selected

The reference state supplies the divergence. It does not select \(D_0\).
When \(\sigma\) is Gibbs for a physical Hamiltonian, forward relative entropy
can equal a scaled nonequilibrium free-energy excess under the usual
finiteness assumptions. For the canonical split density,

\[
K_\sigma=-\log\sigma
\]

is a modular Hamiltonian, but its parameter is not automatically calibrated
proper time or laboratory energy. Calling \(D_0\) a physical resource budget
requires an independent bridge.

### 12.2 A finite quantum carrier is not a finite classical record

The state space on \(P\mathcal K\) is finite-dimensional but continuous. A
finite classical encoding at nonzero accuracy exists because the admitted
family is compact, but:

- a finite cover is not unique;
- no covering cell is an actual measurement outcome;
- identifying a cell requires a measurement campaign and repeated
  preparation assumptions; and
- acquisition, calibration, failure probability, and lineage remain open.

### 12.3 Compression is not acquisition

\(\mathcal C_P\) is a CPTP map and therefore has an abstract dilation. That
does not prove that AQFT dynamics selects or locally realizes it, that a blank
archive is changed, or that an observer retains its output.

### 12.4 Approximate expectations are not exact action closure

The finite corner generally does not contain the inner algebra \(A\).
Approximate expectation values for fixed bounded actions do not make
\(A\to P N_\Lambda P\) a star-homomorphic representation or preserve every
adaptive process without an error ledger.

## 13. Corrected selector ladder

| Rung | Exact return | Status |
|---:|---|---|
| 0 | supplied AQFT net, representation, regions | antecedent |
| 1 | standard split triple | antecedent/theory condition |
| 2 | canonical type-\(I_\infty\) factor | selected relative to triple |
| 3 | faithful reference density \(\sigma\) | selected by state restriction |
| 4 | forward-relative-entropy family | canonical form, supplied radius |
| 5 | uniform spectral tightness | exact theorem |
| 6 | canonical finite-output CPTP approximation | exact conditional construction |
| 7 | uniform fixed-target/process error | exact conditional theorem |
| 8 | physically selected state/process family | open |
| 9 | realized probe and formed retained record | open |
| 10 | observer access, certificate, finality | open |
| 11 | no-refit held-out target verdict | open |

The new gain is rungs 4–7. It closes the **unrestricted-state** objection only
inside a declared, forward-relative-entropy-bounded family.

## 14. Relationship to recent Dynamic Unity results

### `HC-DU-117`

Relative entropy did not select an algebra, state family, reference, channel,
or physical record. That remains true. `HC-DU-134` uses it only after
`HC-DU-133` supplies a canonical factor and reference state relative to a
standard triple.

### `HC-DU-131--132`

Nuclearity and Hamiltonian spectral calculus supplied finite-resolution
envelopes without a generic finite low-energy subspace. Here the spectrum is
that of a trace-class reference density, so every positive density threshold
has finite rank. The price is reference-state and relative-entropy-class
dependence.

### `HC-DU-133`

The strongest statement is now:

```text
all normal states
  -> no uniform finite split-state compression

bounded forward-relative-entropy family
  -> one canonical spectral family uniformly controls every member
  -/-> selected physical family
  -/-> formed record.
```

### `HC-DU-095--098`

Those results identify compactness and finite target separation as the right
abstract finite-resolution conditions. This result supplies a concrete
state-family compactness mechanism and an explicit approximating channel,
but not a selected measurement interface.

## 15. Strongest positive interpretation

If a physical model and experiment independently fix:

1. a standard split triple;
2. its reference state;
3. a forward-relative-entropy-bounded admissible family;
4. an accuracy target; and
5. a fixed downstream intervention/target process,

then a finite-dimensional subsystem carrier can approximate every admitted
input and every output of that fixed process with a uniform, explicit error.

This is materially stronger than approximating only the vacuum:

> Finite effective QFT state carriers can be uniform over a nontrivial
> physically interpretable family, rather than being reference-state
> one-offs.

The remaining decisive question is no longer whether such a family can exist.
It is whether one physical theory or apparatus **selects and forms** the
family, tolerance, compression, and record interface without refitting them
to the held-out target.

## 16. Evidence grade and disposition

### Established mathematics

- Umegaki relative entropy;
- Lindblad data processing;
- trace-norm compactness of bounded forward-relative-entropy classes;
- gentle measurement;
- standard split factors and trace-class reference densities.

### Direct consequences proved here

- the explicit binary tail bound;
- the canonical reference-replacement compression and uniform error;
- downstream fixed-channel transfer;
- the reverse-relative-entropy escaping sequence;
- entropy/rank hostile controls; and
- the typed standard-split selector ladder.

### Grade

Scoped Grade 4 for the exact forward-relative-entropy compactness,
uniform-compression, orientation-asymmetry, and finite-record boundaries;
conditional Grade 3 for uniform finite-resolution state-family
reconstruction after the full standard triple, radius, tolerance, and target
contract are fixed.

No new operator-algebra theorem, AQFT theorem, empirical excess, physical
record selector, law, new physics, prediction, paper promotion, hardware
path, or selected successor is earned.

## 17. Disposition

Bank the positive and leave Dynamic Unity quiescent.

Do not continue by testing another mathematical state-family bound. Reopen
this line only when a concrete physical QFT model or apparatus supplies at
least one of:

1. a dynamically invariant or operationally forced state family whose
   forward-relative-entropy radius is physically bounded;
2. a locally realized version of the canonical compression with complete
   acquisition and archive lineage; or
3. a held-out target for which the same selected packet transfers without
   refitting.

The durable return is:

```text
STANDARD_SPLIT_REFERENCE
+ FORWARD_RELATIVE_ENTROPY_RADIUS
-> TRACE_NORM_COMPACT_STATE_FAMILY
-> CANONICAL_UNIFORM_FINITE_STATE_CARRIER
+ EXPLICIT_FIXED_PROCESS_ERROR

BUT

REVERSE_RELATIVE_ENTROPY_OR_ENTROPY_OR_RANK
-/-> UNIFORM_CONTROL

AND

COMPACT_STATE_FAMILY
-/-> PHYSICALLY_SELECTED_FAMILY
-/-> FORMED_CERTIFIED_RECORD
```
