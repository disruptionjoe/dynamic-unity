---
title: "Covariant local finite-mode trilemma, indexed-family repair, and continuum Gaussian first leak"
status: completed_scoped_result
doc_type: exact_local_finite_covariance_no_go_positive_family_repair_and_gaussian_restriction_boundary
created: 2026-07-29
hypothesis_id: HC-DU-130
run_id: RUN-20260729-155829-covariant-local-finite-mode-trilemma
authority: "Joe direct chat: Go"
lanes:
  - lane_1
  - lane_3
  - lane_4
  - lane_6
  - lane_7
channels:
  - CH-FORMAL
  - CH-COLLIDE
  - CH-MODEL
  - CH-SYN
warrants:
  - DERIVED
  - CONSTRUCTIVELY_REALIZED
maximum_grade: "Scoped Grade 4 local--finite--translation-covariance necessity and continuum-Gaussian first-leak boundary plus conditional Grade 3 target-relative reconstruction; no selected QFT, state, mode family, observer, record interface, empirical excess, new law, new physics, or prediction"
probe: "../tests/du_covariant_local_finite_mode_trilemma_probe.py"
artifact: "../tests/artifacts/du_covariant_local_finite_mode_trilemma_result.json"
---

# Covariant local finite-mode trilemma

## Executive result

The swing returned:

```text
ONE FIXED NONZERO PACKET
  + FINITE DIMENSION
  + COMPACT LOCAL SUPPORT
  + FULL TRANSLATION INVARIANCE
  -> IMPOSSIBLE ON NONCOMPACT CONTINUUM SPACETIME

BUT

REGION-INDEXED FINITE LOCAL PACKETS
  -> EXACTLY COVARIANT AS A FAMILY

FINITE TRANSLATION-INVARIANT CHARACTER SECTORS
  -> POSSIBLE BUT NONLOCAL

FINITE PERIODIC SITE ARENA
  -> POSSIBLE BECAUSE FINITENESS/DISCRETIZATION IS SUPPLIED

FINITE GAUSSIAN PACKET
  -> EXACT RECONSTRUCTION OF THE RESTRICTED GAUSSIAN STATE
  -/> CONTINUUM STATE OR COMPLEMENT TARGET

NO READY SUCCESSOR
```

This resolves the first kinematic ambiguity left by `HC-DU-129`.

The finite Gaussian packet does not transfer to continuum QFT as one fixed,
globally covariant local object. On noncompact spacetime, the translation
orbit of any nonzero compactly supported test function contains arbitrarily
many linearly independent elements.

The correction is just as important as the no-go:

> Local covariance does not require one local packet to remain fixed. It
> requires a family of packets to move coherently with their physical
> regions.

Thus a finite local record can be covariant when it is indexed by an
apparatus region, source worldtube, or other physically formed localization.
The full family is infinite, while every individual acquisition can remain
finite.

This is not a derivation of observers, records, or spacetime from nothing.
It is a necessity result about the type of any finite local continuum
interface.

## 1. The exact question

Let

\[
\mathcal D=C_c^\infty(\mathbb R^d;\mathbb R)
\tag{1}
\]

be the real compactly supported smooth test-function space, with translation

\[
(\tau_a f)(x)=f(x-a).
\tag{2}
\]

A fixed local mode packet is a linear subspace

\[
S\subset\mathcal D.
\]

Ask whether all three conditions can hold:

1. \(S\neq\{0\}\) and \(\dim S<\infty\);
2. every member of \(S\) is compactly supported; and
3. \(\tau_aS=S\) for every \(a\in\mathbb R^d\).

The answer is no.

The statement concerns the **physical source/readout label space**. It does
not automatically prove the corresponding result for every on-shell quotient
\(C_c^\infty/P C_c^\infty\), every net algebra, or every interacting QFT.
Those transfers need separate domain and quotient arguments.

## 2. Fixed-packet theorem

### Theorem 1 — no nonzero finite local translation-invariant packet

There is no nonzero finite-dimensional translation-invariant subspace of
\(C_c^\infty(\mathbb R^d)\).

### Proof

Assume \(S\) has the stated properties and choose nonzero \(f\in S\). Let

\[
K=\operatorname{supp}f.
\]

Because \(K\) is compact, choose a translation vector \(v\) large enough that

\[
K,\;K+v,\;K+2v,\ldots
\]

are pairwise disjoint.

Translation invariance places

\[
f,\tau_vf,\tau_{2v}f,\ldots
\tag{3}
\]

inside \(S\).

They are linearly independent. Choose \(x_0\) with \(f(x_0)\neq0\).
Evaluating a finite relation

\[
\sum_{j=0}^N c_j\tau_{jv}f=0
\]

at \(x_0+jv\) leaves only one nonzero summand and gives

\[
c_jf(x_0)=0.
\]

Hence every \(c_j=0\). Equation (3) supplies arbitrarily many linearly
independent elements of \(S\), contradicting finite dimensionality.
\(\square\)

The exact regression checks the private-support evaluation matrix through
eight translates; it is the identity and has full rank at every size.

### Stronger known classification

The elementary proof is enough for the compact-support result. It sits inside
a mature harmonic-analysis classification:

- [Anselone and Korevaar](https://doi.org/10.1090/S0002-9939-1964-0169048-7)
  proved that finite-dimensional translation-invariant spaces of continuous
  functions or distributions are made from exponential polynomials.
- [Engert](https://msp.org/pjm/1970/32-2/pjm-v32-n2-p05-s.pdf)
  extended the classification to measurable functions on suitable locally
  compact Abelian groups.

Nonzero exponential-polynomial modes are global rather than compactly
supported. The DU theorem is therefore an elementary corollary specialized
to physical local smearing labels, not new harmonic analysis.

## 3. The exact trilemma

For one **fixed** nontrivial packet on noncompact continuum spacetime, at
least one column must be surrendered:

| packet type | finite | properly local | same packet invariant under all translations |
|---|---:|---:|---:|
| fixed local detector packet | yes | yes | no |
| full orbit of a local packet | no | yes | yes |
| finite character/plane-wave sector | yes | no | yes |
| finite periodic-site arena | yes | relative to supplied sites | yes |

The last row is not a counterexample. It changes the arena from
\(\mathbb R^d\) to a supplied finite group or finite periodic lattice.

Compactification alone also should not be conflated with finite
discretization. A continuum torus is compact but still has infinitely many
local degrees of freedom. Finite Fourier sectors exist there because their
members are global; a finite orbit of local delta-site states occurs only
after a finite site arena is supplied.

The theorem also does not prohibit:

- invariance under a finite subgroup;
- an approximate cutoff with a declared covariance error;
- a finite energy/bandwidth sector with nonlocal modes;
- an apparatus-relative packet that moves under translations; or
- a target-relative finite sufficient statistic on a compact physical class.

Each is a differently typed claim.

## 4. The indexed-family repair

Choose one finite packet \(S_0\) localized near a reference region and define

\[
S_x=\tau_xS_0.
\tag{4}
\]

Then

\[
\tau_aS_x=S_{x+a}.
\tag{5}
\]

Equation (5) is exact covariance. The theory does not preserve one packet;
it preserves the relation among the family members.

This is the correct locally covariant type. Brunetti, Fredenhagen, and Verch
formulate locally covariant QFT using covariant functors between spacetime
and algebra categories, with fields as natural transformations rather than
one background-fixed observable
([primary source](https://arxiv.org/abs/math-ph/0112041)).

The relevant DU distinction is:

```text
fixed packet invariance
  != indexed-family covariance
  != physical selection of the index
  != formation of a record at that index.
```

A laboratory can physically occupy a worldtube and thereby instantiate one
member \(S_x\). That does not mean the observer's beliefs constitute the
packet. The index is ontic interface data. But this theorem does not derive
which laboratory, region, coupling, or access boundary is realized.

### Why the union remains infinite

If \(S_0\) contains one nonzero compactly supported \(f\), then its family
contains the entire orbit \(\{\tau_xf\}\). Theorem 1 shows that this orbit has
infinite span. Therefore:

\[
\text{finite fibre at each region}
\quad\not\Rightarrow\quad
\text{finite global family}.
\tag{6}
\]

This is a useful continuum architecture, not a failure. A net, sheaf, or
functor can have finite local acquisitions while retaining infinitely many
possible regional placements.

Infinite orbit dimension does not imply an infinitely long law description
or that infinitely many records are simultaneously instantiated. Equation
(4) specifies the whole family compactly from one packet and the translation
action. The result concerns the dimension of the physical mode family, not
the description length of its generating rule.

## 5. Physical measurement does not remove the index

Fewster, Jubb, and Ruep construct asymptotic measurement schemes for local
observables of a linear scalar QFT. Their schemes explicitly retain a
coupling zone, processing region, probe theory, preparation, and probe
observable. Compactly coupled schemes approximate the target and charge an
effort that grows with accuracy
([primary source](https://arxiv.org/abs/2203.09529)).

This is a positive physical realization result. It supports, rather than
eliminates, the indexed-family structure:

```text
local observable
  + chosen region
  + chosen probe/coupling/readout
  -> realizable or asymptotically realizable measurement
```

It does not select one finite global mode packet. Nor should it: moving the
experiment moves the local observable and its coupling region.

Fewster and Verch's broader review makes the same architectural point at
theory scale: local covariance is functorial, and even a single preferred
state selected naturally across all spacetimes is excluded under their
scoped assumptions
([primary source](https://arxiv.org/abs/1504.00586)).
That no-natural-state theorem is an absorber and caution, not a proof of the
present packet theorem.

## 6. The continuum Gaussian first leak

`HC-DU-129` showed that a finite \(n\)-mode Gaussian state is exactly
determined at population level by a finite mean/covariance packet.

The continuum question is whether the finite restriction determines the
state outside the selected modes.

### Proposition 2 — same finite restriction, different complement

Let the supplied symplectic space contain a direct sum

\[
H=S\oplus T,
\tag{7}
\]

where \(S\) is the accessible finite symplectic sector and \(T\) contains at
least one oscillator mode. Consider two centered product Gaussian states:

\[
\omega_A=\omega_S\otimes\omega_{\mathrm{vac}},
\qquad
\omega_B=\omega_S\otimes\omega_{\mathrm{th},\,\bar n=1}.
\tag{8}
\]

They have the same restriction to every Weyl observable generated by \(S\):

\[
\omega_A(W(s))=\omega_B(W(s))
\qquad
\forall s\in S.
\tag{9}
\]

For a held-out unit quadrature \(q\in T\), use the convention

\[
\omega(W(q))
=
\exp\!\left[-\frac12V(q,q)\right].
\tag{10}
\]

The vacuum and thermal variances are

\[
V_A(q,q)=\frac12,
\qquad
V_B(q,q)=\frac32,
\tag{11}
\]

so

\[
\omega_A(W(q))=e^{-1/4},
\qquad
\omega_B(W(q))=e^{-3/4}.
\tag{12}
\]

Thus the complete ideal Gaussian population packet on \(S\) leaves an exact
same-record/different-complement target.
\(\square\)

The executable control repeats (8)--(12) after one, two, three, and five
retained oscillator modes. The retained covariance block is exact in every
case, and the extra mode remains the first leak.

This component is standard quasifree/Weyl mathematics. Gaussian states on a
Weyl algebra are fixed by their Gaussian kernel; QFT retains infinitely many
degrees of freedom and inequivalent representations
([Longo](https://arxiv.org/abs/2111.11266)).

### Why this is stronger than finite-shot ambiguity

`HC-DU-129`'s finite-shot fibre remained because Gaussian outcome
distributions have overlapping support.

Proposition 2 survives even if the observer receives **exact population
statistics** for every observable in the finite sector. It is not sampling
error. It is omitted physical support:

```text
finite-shot leak      = rival parameters inside the same finite sector
complement-mode leak  = rival states outside the complete retained sector.
```

The remedies are different. More repetitions reduce the first. Only an
expanded sector or a law theorem relating the complement to \(S\) can remove
the second.

## 7. Target-relative reconstruction

Let

\[
r_S(\omega)=\omega|_{\mathcal W(S)}
\tag{13}
\]

be the exact restricted-state record. A held-out target \(T\) reconstructs
from that record exactly when

\[
r_S(\omega_1)=r_S(\omega_2)
\Longrightarrow
T(\omega_1)=T(\omega_2)
\tag{14}
\]

on the frozen completion class.

Equation (14) holds automatically for targets inside
\(\mathcal W(S)\). Proposition 2 kills it for a target on the independently
admitted complement.

This gives a real conditional positive:

> A covariant region-indexed finite Gaussian packet can reconstruct every
> declared target that factors through its local restricted state.

It cannot establish that all observer-accessible targets do so. Capability
and access must be frozen independently; otherwise the conclusion is a
sufficiency tautology.

## 8. What changes for Dynamic Unity

### `HC-DU-129`

The finite Gaussian theorem remains exact. Its correct continuum lift is:

```text
for each physically indexed finite sector S_x:
  finite Gaussian population packet
    -> exact restricted Gaussian state

across all regions:
  {S_x}_x has an infinite orbit
  and does not become one finite global packet.
```

### `HC-DU-102/103`

Those results require target-independent source/readout localization before
causal or conformal reconstruction. `HC-DU-130` explains why the local
packet should be a covariant **family** of source/readout identities, not one
translation-invariant finite list.

It does not provide the missing cover-saturation or uniform inverse margin.

### Observer indexing

The result gives one scoped reason a finite local record must carry a
localization index if the surrounding continuum theory is translation
covariant.

It does **not** prove:

- that conscious observers are fundamental;
- that every fact is observer-relative;
- that records create reality;
- that no preferred foliation exists;
- that global states do not exist; or
- that the index is epistemic.

The index may be an apparatus worldtube, interaction region, source lineage,
or observer access boundary. Its physical selection remains a separate
formation question.

### Regional architecture

The result supports a layered architecture:

\[
\{\text{finite local packets}\}
\longrightarrow
\text{regional gluing/transport}
\longrightarrow
\text{larger accessible algebra}.
\]

But it supplies no consensus, finality, threshold, or gluing law. Importing
those from distributed systems without a physical map would repeat the
forbidden metaphor transfer.

## 9. Grade, absorption, and stop

### Earned

- **Scoped Grade 4:** no nonzero finite-dimensional subspace of
  \(C_c^\infty(\mathbb R^d)\) is invariant under every translation.
- **Scoped Grade 4:** a covariant indexed family of finite local packets is
  the exact positive repair, and its full orbit has infinite span.
- **Scoped Grade 4:** finite translation-invariant nonlocal character sectors
  and supplied finite-periodic arenas are valid escape controls.
- **Scoped Grade 4:** exact finite Gaussian restricted-state data need not
  determine one independently admitted complementary mode.
- **Conditional Grade 3:** targets that factor through the finite restricted
  state reconstruct exactly.

### Absorbed

The components are absorbed by:

- Anselone--Korevaar/Engert translation-invariant-subspace theory;
- locally covariant QFT and algebraic nets;
- local QFT measurement theory;
- CCR direct sums and quasifree states; and
- ordinary restriction/factorization mathematics.

DU's increment is the typed composition:

\[
\text{finite Gaussian closure}
+\text{continuum locality}
+\text{covariance}
\Rightarrow
\text{indexed-family architecture plus a complement first leak}.
\]

This is likely a useful flagship lemma. It is not presently a standalone
blockbuster or a new QFT theorem.

### Not earned

- a theorem on every on-shell field quotient or interacting QFT;
- a selected finite local mode family;
- a selected apparatus, region, state, observer, archive, or access boundary;
- a finite global continuum record;
- a finite-sufficient theorem for all observer-accessible targets;
- regional gluing or finality;
- a GU/Krein transfer;
- empirical excess, new law, new physics, or prediction; or
- a ready successor.

### Exact reopener

Reopen only with one physical arena that supplies, before held-out evaluation:

1. a dynamically formed or independently selected covariant family
   \(x\mapsto S_x\);
2. a realizable source/readout instrument and complete attempt lineage for
   each admitted packet;
3. a compact, energy-bounded, bandlimited, or otherwise finite-complexity
   completion class;
4. a theorem that the declared observer action/target family factors through
   finitely many region-indexed restricted states, with a uniform margin;
5. calibrated finite-resolution certification from `HC-DU-129`; and
6. no-refit transfer showing the records add information beyond the law
   packet.

Another arbitrary finite truncation, more Gaussian tomography, or a fixed
mode basis chosen after seeing the target does not satisfy this reopener.

## Honest status

`HC-DU-130` does not close the continuum path. It corrects its object.

The viable object is not one finite local record packet invariant everywhere.
It is a covariant family of finite local packets, physically instantiated at
particular regions, with an infinite global orbit. Each packet can exactly
reconstruct its restricted Gaussian state; targets outside that restriction
remain an exact physical remainder until dynamics or a frozen capability
contract removes them.
