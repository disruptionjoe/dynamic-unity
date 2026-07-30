---
title: "Minimal instrument dilation, outcome-sector invariants, and the material-archive gauge boundary"
status: banked_scoped_result
doc_type: exploration
created: 2026-07-30
claim_id: HC-DU-165
run_id: RUN-20260730-182456-minimal-instrument-dilation-invariant-audit
work_id: MPA-MINIMAL-INSTRUMENT-DILATION-INVARIANT-AUDIT
action_id: MPA-MINIMAL-INSTRUMENT-DILATION-INVARIANT-AUDIT
program_id: CCR-MINIMAL-PHYSICAL-ANTECEDENT-TO-FINITE-REMAINDER
owner_repo: dynamic-unity
evidence_grade: 4
maximum_grade: 4
---

# Minimal instrument dilation and the material-archive gauge boundary

## Executive return

```text
TWO_RANK_TYPE_SEPARATION
+ MINIMAL_NORMAL_APPARATUS_PROFILE
+ OUTCOME_SECTOR_FIXED_ALGEBRA
+ MATERIAL_CARRIER_NONSELECTION
+ KNOWN_RESULT_ABSORPTION
+ IMPLEMENTATION_COMPLETE_REOPENER_UNCHANGED
+ NO_READY_SUCCESSOR
```

`HC-DU-164` proved that complete tomography of an accessible quantum
instrument does not identify its material archive or physical dilation. This
audit asks the strongest possible repair:

> Even if the physical dilation is not unique, does the instrument itself
> force a canonical minimal apparatus that can count as the record?

The answer has a real positive and a decisive limit.

For a finite-dimensional, finite-outcome instrument
\(\{\mathcal E_x\}_{x\in X}\), standard Choi--Kraus--Stinespring measurement
theory fixes an **abstract minimal normal apparatus profile**

\[
\mathcal K_{\min}
=
\bigoplus_{x\in X}\mathbb C^{r_x},
\qquad
r_x=\operatorname{rank}J(\mathcal E_x).
\tag{1}
\]

The pointer projection \(P_x\) selects the \(x\)-sector, and

\[
\dim\mathcal K_{\min}=\sum_xr_x.
\tag{2}
\]

Within the declared class of normal unitary measurement models, this is a
formal dimension floor. Minimal realizations are unique up to
outcome-preserving apparatus unitaries.

That does **not** select a material archive. Under the full within-outcome
Kraus-basis gauge

\[
G=\prod_xU(r_x),
\tag{3}
\]

the pointwise fixed apparatus algebra is exactly

\[
\mathcal B(\mathcal K_{\min})^G
=
\bigoplus_x\mathbb C I_{r_x}
=
\operatorname{span}\{P_x:x\in X\}.
\tag{4}
\]

Thus the instrument forces an abstract outcome-sector algebra and its
multiplicities. It does not force a basis or provenance token inside a
sector, a material carrier, a location, a retention or reset process, a
physical sampler, an access boundary, or the realized outcome. Nonminimal
archives remain arbitrarily enlargeable.

The mathematical core is known. Dynamic Unity's earned result is the typed
boundary:

```text
operational response rank
is not
minimal realization multiplicity
is not
material record selection
```

The implementation-complete reopener remains necessary.

## 1. Literature boundary

Three established results absorb the mathematical spine.

1. [Choi's theorem](https://doi.org/10.1016/0024-3795(75)90075-0)
   characterizes finite-dimensional completely positive maps by positive
   Choi matrices and operator-sum representations.
2. [Ozawa's measurement-process
   theorem](https://doi.org/10.1063/1.526000) establishes the
   correspondence between completely positive instruments and indirect
   measurement processes.
3. Pellonpää and Tukiainen's
   [minimal normal measurement-model
   analysis](https://arxiv.org/abs/1509.08886) proves that, outside a stated
   infinite-dimensional pathology, the minimal apparatus Hilbert space is
   unitarily isomorphic to the instrument's minimal Stinespring space. In the
   finite discrete case, the apparatus dimension is bounded below by the sum
   of the outcome Kraus ranks; minimal normal models are unique up to the
   corresponding unitary transformations.

This audit stays finite-dimensional. It therefore does not inherit the
paper's exceptional rank-infinite case, where a unitary extension can require
one additional apparatus dimension.

The same source also makes the scope restriction important: a **normal**
measurement model uses a pure probe, unitary system--apparatus interaction,
and sharp apparatus pointer. More general nonnormal models can use a smaller
apparatus for some trivial observables. Equation (2) is not asserted here as
a lower bound on every operational encoding called a measurement.

## 2. The two ranks

Let

\[
\mathcal E_x:\mathcal B(\mathcal H)\to\mathcal B(\mathcal H)
\tag{5}
\]

be a nonzero completely positive, trace-nonincreasing outcome map, with
\(\sum_x\mathcal E_x\) trace preserving.

Two matrices associated with \(\mathcal E_x\) answer different questions.

### 2.1 Liouville or superoperator rank

Choose a matrix-unit basis and define \(L_x\) by

\[
\operatorname{vec}(\mathcal E_x(A))
=
L_x\operatorname{vec}(A).
\tag{6}
\]

Set

\[
\ell_x=\operatorname{rank}L_x.
\tag{7}
\]

`HC-DU-164` proved:

\[
\ell_x=1
\quad\Longleftrightarrow\quad
\mathcal E_x(\rho)
=
\operatorname{tr}(F_x\rho)\tau_x
\tag{8}
\]

for a fixed posterior state \(\tau_x\). This is the exact criterion that
outcome label \(x\) fixes every later system-only response across admitted
input histories.

The Liouville rank therefore measures the dimension of the outcome map's
linear response range. It is an **operational dependence** object.

### 2.2 Choi or Kraus rank

Define the positive Choi matrix

\[
J_x
=
\sum_{i,j}|i\rangle\langle j|
\otimes
\mathcal E_x(|i\rangle\langle j|),
\tag{9}
\]

and set

\[
r_x=\operatorname{rank}J_x.
\tag{10}
\]

The spectral decomposition of \(J_x\) gives a minimal linearly independent
Kraus family

\[
\mathcal E_x(A)
=
\sum_{\alpha=1}^{r_x}
K_{x\alpha}A K_{x\alpha}^{\dagger}.
\tag{11}
\]

No Kraus representation uses fewer than \(r_x\) terms. The Choi rank
therefore measures **minimal dilation multiplicity**, not operational label
sufficiency.

### 2.3 Independence

The two ranks do not order each other.

| Qubit outcome map | \(\ell\) | \(r\) | Meaning |
|---|---:|---:|---|
| \(A\mapsto P_nAP_n\) | 1 | 1 | label sufficient; one Kraus coordinate |
| \(A\mapsto A/2\) | 4 | 1 | one Kraus coordinate; label preserves the whole prior state |
| \(A\mapsto\operatorname{tr}(A)I/2\) | 1 | 4 | label sufficient; four Kraus coordinates required |

The last two rows are exact reverse controls:

```text
r=1 does not imply label sufficiency
ell=1 does not imply one-dimensional minimal apparatus
```

This prevents a false progression from “minimal realization” to “minimal
sufficient record.”

## 3. Minimal instrument-dilation theorem

### Proposition 1 — finite minimal normal apparatus profile

Let \(\{\mathcal E_x\}_{x\in X}\) be a finite-outcome instrument on a
finite-dimensional system, and let

\[
r_x=\operatorname{rank}J(\mathcal E_x).
\]

Then:

1. the instrument has a minimal Stinespring dilation on

   \[
   \mathcal K_{\min}=\bigoplus_x\mathbb C^{r_x};
   \]
2. the sharp pointer is the PVM

   \[
   P_x:
   \mathcal K_{\min}\to\mathbb C^{r_x};
   \]
3. every minimal instrument dilation is related to this one by an
   outcome-preserving apparatus unitary;
4. in finite dimension, the dilation is extendable to a normal unitary
   measurement model; and
5. every normal unitary model of the same instrument has apparatus dimension
   at least \(\sum_xr_x\).

### Construction and proof boundary

Choose minimal Kraus families from equation (11), let
\(\{e_{x\alpha}\}\) be the standard sector bases, and define

\[
V\psi
=
\sum_{x,\alpha}
K_{x\alpha}\psi\otimes e_{x\alpha}.
\tag{12}
\]

Trace preservation of \(\sum_x\mathcal E_x\) gives

\[
V^\dagger V=I.
\tag{13}
\]

Moreover,

\[
\mathcal E_x(\rho)
=
\operatorname{tr}_{\mathcal K}
\left[
(I\otimes P_x)V\rho V^\dagger
\right].
\tag{14}
\]

Linear independence of each minimal Kraus family makes the instrument
dilation minimal. Standard minimal-Stinespring uniqueness gives an
intertwining unitary \(W\). Since it must also intertwine every \(P_x\),

\[
W=\bigoplus_xW_x,
\qquad
W_x\in U(r_x).
\tag{15}
\]

In finite dimension, the isometry from
\(\mathcal H\otimes\mathbb C\xi\) onto \(V\mathcal H\) extends to a unitary on
\(\mathcal H\otimes\mathcal K_{\min}\). This is exactly the regime in which
the infinite-dimensional unitary-extension pathology does not occur.

The lower bound and uniqueness statement are established measurement-theory
results, not a new Dynamic Unity theorem.

## 4. What survives the dilation gauge

Minimality removes redundant Kraus coordinates but leaves the
within-outcome transformation in equation (15).

### Proposition 2 — pointwise fixed apparatus algebra

Let

\[
G=\prod_xU(r_x)
\]

act on \(\mathcal B(\mathcal K_{\min})\) by conjugation. Then

\[
\mathcal B(\mathcal K_{\min})^G
=
\left\{
\bigoplus_x\lambda_xI_{r_x}:\lambda_x\in\mathbb C
\right\}
=
\operatorname{span}\{P_x\}.
\tag{16}
\]

### Proof

Write an apparatus operator \(A\) in outcome blocks \(A_{xy}\).
Independent scalar phases on the \(x\)- and \(y\)-sectors imply

\[
A_{xy}=0
\qquad(x\ne y)
\tag{17}
\]

for every pointwise invariant \(A\). Each diagonal block must then satisfy

\[
U_xA_{xx}U_x^\dagger=A_{xx}
\qquad
\text{for every }U_x\in U(r_x).
\tag{18}
\]

The commutant of the defining full unitary representation is scalar, so

\[
A_{xx}=\lambda_xI_{r_x}.
\tag{19}
\]

Equations (17)--(19) give equation (16).

### Exact finite control

For sector profile \((1,2)\), the probe imposes commutation with:

1. a sign separating the one- and two-dimensional outcome sectors;
2. a swap inside the two-dimensional sector; and
3. a phase sign inside that sector.

The resulting exact rational constraint system has:

\[
9\text{ operator coordinates}
-
7\text{ independent constraints}
=
2\text{ fixed dimensions}.
\]

The two fixed basis elements are the identities on the two outcome sectors.
A within-sector basis projector and a cross-sector matrix unit both fail.

### Scope correction

Equation (16) does not say that every natural object associated with a
minimal dilation must be a scalar. A complementary channel, a state family,
or an apparatus observable may be carried **covariantly** from one dilation
representative to another. Their unitary-equivalence classes can contain
nontrivial information.

The narrower and relevant statement is:

> The instrument alone supplies no pointwise preferred within-sector basis or
> material token. A concrete such preference requires additional physical
> structure that breaks or instantiates the dilation equivalence.

Examples of such extra structure include a Hamiltonian, spatial
factorization, detector material, environmental coupling, prepared reference,
readout chain, archive policy, or access protocol. If one of these selects a
basis or carrier, that antecedent—not abstract instrument minimality—does the
physical selection.

## 5. Redundancy is not removed from the world

Minimality is a property of a representation class, not a law that actual
apparatuses contain no redundant degrees of freedom.

For example, the map

\[
\mathcal E(A)=A/2
\tag{20}
\]

has Choi rank one. It also admits the nonminimal two-coordinate Kraus list

\[
K_1=I/2,
\qquad
K_2=I/2,
\tag{21}
\]

because

\[
K_1AK_1^\dagger+K_2AK_2^\dagger=A/2.
\tag{22}
\]

Appending blank ancillas, copied labels, inaccessible memories, or
environmental degrees creates further nonminimal realizations without
changing the accessible instrument.

The standard theorem therefore says:

```text
there exists an effective realization with no representational redundancy
```

not:

```text
the physical apparatus is that realization
or
every physical degree of freedom is operationally visible
```

This is the same representation-versus-selection boundary encountered in
causal-action and stochastic-dilation audits.

## 6. What the instrument forces and does not force

### Forced inside the frozen mathematical class

- the outcome-labelled family of CP maps;
- the Choi ranks \(r_x\);
- the abstract minimal sector profile \((r_x)_{x\in X}\);
- the total minimal normal apparatus dimension \(\sum_xr_x\);
- the outcome-sector pointer algebra \(\operatorname{span}\{P_x\}\); and
- a minimal complementary/dilation structure up to
  outcome-preserving unitary equivalence.

The outcome set itself is part of the supplied instrument. The theorem does
not explain why nature chose that outcome decomposition.

### Not forced

- an actual material carrier or its location;
- a preferred basis within a multiplicity sector;
- which physical degrees realize the minimal coordinates;
- whether the real apparatus is minimal;
- blank-to-written formation or a physical sampler;
- which outcome actually occurs;
- copying, redundancy, durability, or public availability;
- provenance, authentication, retention, or reset;
- an observer/access boundary;
- a physically selected action class; or
- a finite remainder beyond the reduced instrument.

Neither \(r_x\) nor \(\sum_xr_x\) should be called a number of physical memory
bits without an independently specified encoding and apparatus architecture.

## 7. Dynamic Unity disposition

### Earned result

`HC-DU-165` banks the following scoped statement:

> A finite labelled quantum instrument forces an abstract minimal normal
> apparatus-sector profile whose multiplicities are the outcome Choi ranks.
> Minimal realizations remain related by outcome-preserving unitaries, and the
> pointwise fixed algebra under the full within-sector gauge is only the
> supplied outcome-sector algebra. Therefore minimal instrument dilation does
> not select a material archive or provenance-bearing record interface.

This is Grade 4 because it is an exact scoped necessity/nonselection boundary,
not because its mathematical components are novel.

### Relation to `HC-DU-164`

The two results now form a typed square:

```text
Liouville rank ell_x
  -> does the label fix later system responses?

Choi rank r_x
  -> how many abstract Kraus coordinates does a minimal normal realization need?

minimal-dilation unitary class
  -> what effective realization structure is representation-independent?

material packet
  -> what carrier formed, retained, authenticated, reset, and exposed the record?
```

No arrow may silently replace the next.

### Reopener

More instrument tomography, a reported Kraus rank, or a minimal Stinespring
model does not reopen material reconstruction.

The existing implementation-complete reopener is sharpened but unchanged:
the source packet must physically instantiate enough additional structure to
break or realize the dilation equivalence and must preserve joined
per-attempt acquisition, hidden-environment scope, provenance, retention,
access, and reset semantics. It must then pass separate material
factorization and behavioral-minimality tests.

### Program state

```text
KNOWN MATHEMATICAL MINIMUM
+ EXACT GAUGE BOUNDARY
- PHYSICAL CARRIER SELECTION
- COMPLETE ARCHIVE
- PROVENANCE / RESET / ACCESS
- FINITE REMAINDER
= NO READY SCIENTIFIC SUCCESSOR
```

The coherent campaign remains parked. No hardware, provider, prediction,
paper, later campaign card, or external action is activated.

## 8. Exact artifact

Run:

```bash
python3 tests/du_minimal_instrument_dilation_invariant_probe.py --write-artifact
```

The probe verifies:

- the exact rank pairs \((1,1)\), \((4,1)\), and \((1,4)\);
- equality of a dephasing channel under a rational within-sector Kraus
  rotation;
- equality of a minimal and redundant Kraus realization of \(A\mapsto A/2\);
- the two-dimensional fixed algebra for sector profile \((1,2)\); and
- the distinct minimal normal apparatus profiles for the three controls.

Passing establishes no empirical apparatus fact, physical minimality,
material archive, provenance, reset, observer, remainder, law, or new
physics.
