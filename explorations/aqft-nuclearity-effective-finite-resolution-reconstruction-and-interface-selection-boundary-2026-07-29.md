---
title: "AQFT nuclearity, effective finite-resolution reconstruction, and the interface-selection boundary"
status: completed_scoped_result
doc_type: aqft_phase_space_finite_resolution_positive_exact_finite_no_go_and_interface_selection_boundary
created: 2026-07-29
hypothesis_id: HC-DU-131
run_id: RUN-20260729-161446-aqft-nuclearity-finite-resolution-boundary
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
maximum_grade: "Scoped Grade 4 exact-finite versus nuclear finite-resolution necessity, infinite-rank first-leak, and symmetry-selection boundary plus conditional Grade 3 target-relative finite-resolution reconstruction; no selected QFT, state, region, nuclearity scale, finite coordinates, instrument, observer, record interface, empirical excess, new law, new physics, or prediction"
probe: "../tests/du_aqft_nuclearity_finite_resolution_boundary_probe.py"
artifact: "../tests/artifacts/du_aqft_nuclearity_finite_resolution_boundary_result.json"
---

# AQFT nuclearity and the finite-resolution record boundary

## Executive result

The swing returned:

```text
AQFT NUCLEARITY
  + SUPPLIED REGION, STATE, HAMILTONIAN AND ENERGY SCALE
  -> A PHYSICALLY MOTIVATED COMPACT / NUCLEAR LOCAL PHASE-SPACE IMAGE
  -> FINITE-RANK APPROXIMATION AT EVERY NONZERO TOLERANCE

NUCLEARITY
  -/-> FINITE RANK
  -/-> EXACT FINITE CONTINUUM RECORD
  -/-> SELECTED FINITE COORDINATES
  -/-> PHYSICALLY FORMED RECORD INTERFACE

INFINITE-RANK NUCLEAR MAP
  -> EVERY EXACT FINITE LINEAR RECORD HAS A FIRST LEAK

SUPPLIED FINITE-RANK APPROXIMATION WITH ERROR eta
  + L-LIPSCHITZ TARGET
  -> SAME FINITE RECORD IMPLIES TARGET GAP AT MOST 2 L eta

SYMMETRY
  -> MAY SELECT A COMPLETE MULTIPLET
  -/-> ONE COORDINATE INSIDE THAT MULTIPLET

NO READY SUCCESSOR
```

This is the first physically established continuum bridge after
`HC-DU-128--130`.

It replaces an unhelpful binary:

```text
finite exact record
versus
unmanageable infinite continuum
```

with a typed three-part result:

1. a QFT phase-space law can make the energy-damped local possibility set
   compact or nuclear;
2. that set can then be approximated by finite-dimensional data to any
   declared nonzero tolerance; and
3. neither the coordinates nor their physical acquisition follow from
   nuclearity alone.

The new architectural possibility is:

> Physics may warrant an effective approximation envelope before it selects
> a record coordinate system or record-forming apparatus.

That is progress toward the North Star. It is not yet a North-Star
reconstruction theorem.

## 1. The typed object

Let \(X,Y\) be Banach spaces. A bounded map \(T:X\to Y\) is nuclear when it
admits a representation

\[
Tx=\sum_{j=1}^{\infty}\phi_j(x)y_j,
\qquad
\sum_{j=1}^{\infty}\|\phi_j\|\,\|y_j\|<\infty,
\tag{1}
\]

with \(\phi_j\in X^*\) and \(y_j\in Y\).

The standard Buchholz--Wichmann energy-nuclearity specimen in algebraic
quantum field theory is

\[
\Theta_{\beta,O}:\mathcal A(O)\longrightarrow\mathcal H,
\qquad
\Theta_{\beta,O}(A)=e^{-\beta H}A\Omega.
\tag{2}
\]

Here:

- \(O\) is a bounded spacetime region;
- \(\mathcal A(O)\) is its local observable algebra in a supplied
  representation;
- \(H\) is the Hamiltonian;
- \(\Omega\) is the vacuum or other declared reference vector; and
- \(\beta>0\) fixes the energy-damping scale.

Nuclearity constrains the number of locally excitable states after energy
damping. It is a phase-space condition, not an observer record.

The antecedents in (2) are load-bearing. The QFT, net, representation,
region, state, Hamiltonian, and damping scale are supplied. Whether a given
theory satisfies a useful nuclearity bound is a physical/mathematical fact
about that supplied packet.

Keep seven objects distinct:

1. the local algebra and its norm-bounded source domain;
2. the energy-damped image \(\Theta_{\beta,O}(B)\);
3. finite-rank mathematical approximants to that image;
4. a choice of finite coordinates for an approximant;
5. a physically realizable probe and readout of those coordinates;
6. a retained, certified finite transcript; and
7. a target that factors through the transcript to declared accuracy.

Nuclearity acts at steps 1--3. Dynamic Unity's record question lives at
steps 4--7.

## 2. Nuclearity gives finite resolution, not finite truth

### Theorem 1 — nuclear tail approximation

For a representation (1), define

\[
T_Nx=\sum_{j=1}^{N}\phi_j(x)y_j.
\tag{3}
\]

Then \(T_N\) has finite rank and

\[
\|T-T_N\|
\leq
\sum_{j>N}\|\phi_j\|\,\|y_j\|
\longrightarrow0.
\tag{4}
\]

Consequently, the image of the unit ball under \(T\) is relatively compact
and totally bounded. For every \(\epsilon>0\), finitely many
\(\epsilon\)-balls cover it.

### Proof

For \(\|x\|\leq1\),

\[
\|(T-T_N)x\|
\leq
\sum_{j>N}|\phi_j(x)|\,\|y_j\|
\leq
\sum_{j>N}\|\phi_j\|\,\|y_j\|.
\]

The summable tail tends to zero. Thus finite-rank \(T_N\) converge to \(T\)
in operator norm. The image of the unit ball under each \(T_N\) is bounded
inside a finite-dimensional space and is totally bounded; a sufficiently
close finite-rank image supplies a finite cover of \(T(B_X)\).
\(\square\)

The theorem does **not** say the series terminates. Nuclear maps may have
infinite rank.

### Exact infinite-rank control

On \(\ell^2\), set

\[
De_j=2^{-(j+1)}e_j.
\tag{5}
\]

The map is trace class and hence nuclear, with

\[
\|D\|_1=\sum_{j=0}^{\infty}2^{-(j+1)}=1.
\tag{6}
\]

It has infinite rank. Retaining the first \(N\) coordinates gives

\[
\|D-D_N\|=2^{-(N+1)}
\tag{7}
\]

and nuclear tail

\[
\|D-D_N\|_1=2^{-N}.
\tag{8}
\]

Every finite truncation is accurate, and every finite truncation has a
nonzero exact tail. The two facts coexist.

## 3. Infinite rank forbids exact finite linear completeness

### Theorem 2 — exact finite-record first leak

Let \(T:X\to Y\) be a bounded infinite-rank linear map and let
\(R:X\to\mathbb R^m\) be any finite-rank linear record. Then there exist
\(x,x'\in X\) such that

\[
Rx=Rx'
\qquad\text{and}\qquad
Tx\neq Tx'.
\tag{9}
\]

Moreover, a continuous linear target \(f\in Y^*\) can distinguish the two
outputs.

### Proof

If equality of \(R\) always implied equality of \(T\), then

\[
\ker R\subseteq\ker T.
\tag{10}
\]

The rule

\[
\widetilde T(Rx)=Tx
\tag{11}
\]

would therefore be well-defined and would factor \(T\) through the
finite-dimensional space \(\operatorname{im}R\). Hence \(T\) would have
finite rank, a contradiction.

Thus some \(h\in\ker R\) has \(Th\neq0\). Take \(x=0\) and \(x'=h\), scaling
both into any declared norm ball if needed. Hahn--Banach supplies
\(f\in Y^*\) with \(f(Th)\neq0\).
\(\square\)

For (5), the witness after retaining the first \(N\) coordinates is simply

\[
x=e_N,
\qquad
x'=-e_N.
\tag{12}
\]

They have the same retained record, while the first omitted-coordinate
target differs by \(2^{-N}\).

### Exact positive escape

If \(T\) really has rank \(m<\infty\), a complete coordinate map on
\(\operatorname{im}T\) is an exact finite record. The theorem therefore
identifies the boundary precisely:

```text
finite rank
  -> exact finite linear representation is possible

infinite rank, even nuclear
  -> every exact finite linear representation leaks.
```

This is not a claim about arbitrary nonlinear encodings with infinite
precision. Such encodings can hide an infinite object in one real number
and violate the bounded physical-record contract rather than solve it.

## 4. Target-relative finite-resolution reconstruction

Exact full-image reconstruction is stronger than the North Star needs.
Observer capability may depend only on a stable target.

### Theorem 3 — Lipschitz target certificate

Let \(B_X\) be the unit ball, let

\[
\|T-T_N\|\leq\eta,
\tag{13}
\]

and let \(F:T(B_X)\to\mathbb R\) be \(L\)-Lipschitz. If

\[
T_Nx=T_Nx',
\tag{14}
\]

then

\[
|F(Tx)-F(Tx')|
\leq2L\eta.
\tag{15}
\]

### Proof

By (14) and the triangle inequality,

\[
\begin{aligned}
\|Tx-Tx'\|
&\leq
\|Tx-T_Nx\|
+\|T_Nx'-Tx'\|\\
&\leq2\eta.
\end{aligned}
\]

Lipschitz continuity gives (15).
\(\square\)

For (5), the omitted-coordinate target is one-Lipschitz and the pair (12)
saturates the bound \(2\eta\).

This theorem earns a conditional reconstruction statement:

> Given a supplied finite-rank approximation and a supplied Lipschitz target,
> equality of the finite approximate record controls the target error.

It does not yet earn a physical certificate. A real finite transcript adds:

- probe and coupling error;
- calibration and digitization error;
- sampling uncertainty;
- missing/rejected-attempt visibility;
- drift and model-mismatch error;
- archive and provenance failure; and
- observer access and action limits.

Those errors must be composed explicitly rather than hidden inside \(\eta\).

## 5. Symmetry can select a block without selecting coordinates

The nuclear expansion (1) is generally nonunique. Even a natural
finite-dimensional approximating subspace need not contain natural
one-dimensional coordinates.

### Proposition 4 — irreducible rotation block

Let \(V=\mathbb R^2\) carry the ordinary irreducible rotation
representation. The only orthogonal projectors commuting with every rotation
are

\[
P=0
\qquad\text{and}\qquad
P=I.
\tag{16}
\]

### Proof

It is enough to commute with the quarter turn

\[
J=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix}.
\tag{17}
\]

For a symmetric projector

\[
P=
\begin{pmatrix}
a&b\\
b&d
\end{pmatrix},
\]

\(PJ=JP\) forces \(b=0\) and \(a=d\). Idempotence then gives
\(a\in\{0,1\}\), yielding (16).
\(\square\)

Thus the whole degenerate multiplet is invariant, while no rank-one
coordinate is. A physical reference frame, boundary, coupling, defect,
apparatus orientation, or other asymmetry can select coordinates, but that
is additional structure.

The scoped lesson is:

```text
symmetry-selected approximation sector
  != symmetry-selected basis
  != physically formed coordinate record.
```

This is not a universal no-selector theorem. Nondegenerate spectra, boundary
conditions, localized apparatus structure, or other physical asymmetry may
provide a natural coordinate family. They must be shown rather than inferred
from nuclearity.

## 6. Collision with algebraic QFT

### Haag--Swieca and Buchholz--Wichmann

Haag and Swieca introduced a compactness requirement on bounded-energy local
excitations as a phase-space condition. Buchholz and Wichmann strengthened
the idea using the nuclearity of energy-damped local maps and related its
growth to thermodynamic behavior
([Haag--Swieca primary paper](https://jaswieca.if.uff.br/ArtigosPublicados_JASwieca/artigos%20em%20pdf/Swieca_CommMathPhys_1_1965-308.pdf);
[Buchholz--Wichmann primary paper](https://doi.org/10.1007/BF01454978)).

This is exactly the physical ingredient missing from a generic compactness
argument: local QFT dynamics and spectral structure can warrant a restricted
phase-space image.

It does not supply a detector, observer, pointer, archive, or finite
coordinate list.

### Nuclearity and the split property

Suitable nuclearity conditions imply the split property for separated local
regions. The split property inserts a type-I factor between nested local
algebras and gives a strong form of subsystem independence
([Fewster review](https://arxiv.org/abs/1601.06936)).

That is physically important, but it does not turn the local algebra into a
finite-dimensional matrix algebra. Nor does it canonically choose:

- one intermediate type-I factor;
- one tensor-product identification;
- one probe state;
- one measurement basis; or
- one retained record.

This agrees with `NI-DU-57`: type-I interpolation supplies a subsystem
bridge, not a selected physical interface.

### Curved spacetime and modular nuclearity

Locally covariant split results and modular \(\ell^p\) conditions extend the
phase-space program beyond one stationary Minkowski model. Modular
nuclearity-type conditions can be stable under causal propagation and hold
for broad free-field state classes
([Fewster](https://arxiv.org/abs/1501.02682);
[Lechner--Sanders](https://arxiv.org/abs/1511.09027)).

These results strengthen the case that effective local phase-space control
is not merely a finite toy artifact. They still do not identify nuclearity
with record formation. Lechner and Sanders explicitly treat the precise
physical interpretation of their modular \(\ell^p\) condition as an open
issue.

### Type III is not the opposite of finite-resolution usefulness

Local AQFT algebras may remain type III and infinite. Nuclearity constrains a
particular energy-damped map from their unit ball; it does not assert that
the algebra itself is finite.

Therefore both slogans are wrong:

```text
type III / infinite local algebra
  -> no finite observer-relevant approximation is possible

nuclearity / split property
  -> the local physical state is finitely recorded.
```

The correct middle is a quantitative approximation claim about a typed map.

## 7. Relation to the recent Dynamic Unity sequence

### `HC-DU-095--098`

Those swings established the abstract finite-resolution architecture:
compact target classes admit finite covers, energy bounds alone need not
give compactness in the chosen norm, finite probes require observability, and
Sobolev/entropy bounds can quantify approximation.

`HC-DU-131` does not repeat that mathematics. It supplies a mature QFT
phase-space condition under which the relevant energy-damped local image is
nuclear and hence compact.

### `HC-DU-128`

A complete positive functional on a supplied algebra can reconstruct its
cyclic GNS representation. Nuclearity addresses a different question: how
large the energy-damped image of bounded local operations is.

Neither result turns the full theoretical functional into a formed finite
record.

### `HC-DU-129`

A selected finite Gaussian mode sector admits exact population-level
mean/covariance reconstruction and confidence-qualified finite-shot
certification.

Nuclearity can justify finite approximation of a larger local phase-space
image, but it does not imply Gaussian closure or select the quadrature
settings.

### `HC-DU-130`

Finite properly local packets form a covariant region-indexed family whose
full continuum orbit is infinite. Nuclearity does not collapse that family
to one fixed finite packet. It offers a different repair:

```text
at each supplied region and energy scale:
  approximate the typed energy-damped local image to tolerance eta

across all regions:
  preserve local covariance of the family

for a supplied stable target:
  propagate eta into a target-error certificate.
```

This is the most coherent finite-resolution continuum architecture presently
earned in DU.

## 8. What the result changes

### A law can constrain approximation before it selects observation

The program should no longer ask only:

> Does the law select one exact finite record?

It should also ask:

> Does the law select a physically natural approximation envelope, error
> norm, and scaling law within which a realizable record can be certified?

The second question is weaker but scientifically meaningful. A positive
answer can determine which finite interfaces are adequate without making one
interface ontologically privileged.

### Approximation and formation remain separate

The following chain must not be collapsed:

```text
QFT law and state
  -> nuclear local map
  -> finite-rank mathematical approximation
  -> coordinate/probe choice
  -> physical interaction
  -> formed transcript
  -> certified observer access
  -> target-relative capability.
```

The first two arrows can be law-side. The middle arrows remain the physical
record-selection problem.

### Exactness may be the wrong demand for operational targets

Theorem 2 preserves the exact no-go. Theorem 3 shows why the no-go need not
end the program. If all observer-accessible targets are stable under the
nuclear tail at declared resource resolution, then finite records may be
operationally complete without encoding the exact continuum state.

That is a conditional route, not a result. DU has not shown:

- which targets constitute the full observer capability set;
- that they are uniformly Lipschitz in the nuclearity norm;
- that one finite physical instrument captures an adequate approximant;
- that the error remains controlled under regional transport and gluing; or
- that the record adds information beyond the QFT law and supplied state
  class.

## 9. Grade, absorption, and stop

### Earned

- **Scoped Grade 4:** nuclear maps admit operator-norm finite-rank
  approximation with a summable tail and need not have finite rank.
- **Scoped Grade 4:** every exact finite-rank linear record leaks on an
  infinite-rank nuclear map; finite rank is the exact positive escape.
- **Scoped Grade 4:** a nontrivial one-dimensional coordinate need not be
  symmetry-selectable inside a degenerate irreducible multiplet.
- **Conditional Grade 3:** a supplied finite-rank approximation with error
  \(\eta\) reconstructs a supplied \(L\)-Lipschitz target to diameter at most
  \(2L\eta\).
- **Physical import:** established AQFT nuclearity conditions provide a real
  continuum phase-space specimen rather than an arbitrary compact class.

### Absorbed

The mathematical and physical components are absorbed by:

- nuclear and compact operator theory;
- Haag--Swieca phase-space compactness;
- Buchholz--Wichmann energy nuclearity;
- nuclearity/split-property results;
- locally covariant and modular nuclearity; and
- elementary representation and symmetry theory.

DU's increment is the typed composition:

\[
\text{physical QFT phase-space restriction}
+\text{finite-rank approximation}
+\text{exact finite-record no-go}
+\text{target-stability bound}
+\text{coordinate-selection boundary}.
\tag{18}
\]

This is useful North-Star architecture. It is not a new AQFT theorem or
standalone blockbuster.

### Not earned

- nuclearity for every QFT or state;
- a selected QFT, algebra, state, region, Hamiltonian, or damping scale;
- exact finite continuum reconstruction;
- a canonical finite-rank decomposition or coordinate basis;
- a physically realizable selected probe;
- blank-to-written record formation, provenance, archive, or access;
- an observer-complete target class;
- a quantitative empirical discriminator;
- empirical excess, a new law, new physics, or a prediction; or
- a ready successor.

### Exact reopener

Reopen only with one physical QFT arena that supplies, before held-out
evaluation:

1. a declared local net, representation, state family, region class,
   Hamiltonian, and energy/resolution scale;
2. a quantitative nuclearity or approximation-number bound with a fixed
   physical norm;
3. a symmetry-natural finite subspace or a QFT-realizable finite probe family
   whose choice is independent of the held-out target;
4. complete acquisition, calibration, attempt-lineage, archive, and access
   semantics;
5. a frozen observer action/target class with a uniform tail-stability
   theorem;
6. a complete error composition and bounded resource contract; and
7. no-refit transfer to a held-out region, state, or target showing that the
   formed record adds information beyond the law packet.

An abstract compactness theorem, another arbitrary truncation, or a basis
chosen after seeing the target does not satisfy this reopener.

## Honest status

`HC-DU-131` does not select the record substrate.

It establishes a more useful middle:

> In a physically important class of continuum QFTs, local energy-damped
> possibilities can be finitely approximated at every nonzero resolution.
> If the underlying map remains infinite rank, no finite exact linear record
> captures it. Stable held-out targets can nevertheless inherit a rigorous
> finite-resolution error bound.

The remaining scientific problem is no longer merely “how can a finite
observer hold an infinite field?” It is:

> Which physical dynamics or symmetry breaking selects a realizable finite
> probe family, and do all observer-accessible targets remain stable on the
> resulting nuclear tail?

That is the exact boundary now banked.
