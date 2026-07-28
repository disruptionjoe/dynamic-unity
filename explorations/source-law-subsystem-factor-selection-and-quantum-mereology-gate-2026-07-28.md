---
title: "Source-law subsystem factor selection and quantum-mereology gate"
status: completed
doc_type: exploration_result
created: 2026-07-28
claim_id: HC-DU-076
run_id: RUN-20260728-113459-subsystem-factor-selection
run_plan: "../lab/process/runs/RUN-20260728-113459-subsystem-factor-selection/run-plan.md"
run_receipt: "../lab/process/runs/RUN-20260728-113459-subsystem-factor-selection/run-receipt.md"
owner_repo: dynamic-unity
---

# Source-law subsystem factor selection and quantum mereology

## Executive result

Dynamic Unity's quantum-record requirement was still one type too loose.

`HC-DU-075` said a quantum record needs a physically selected carrier,
retention, provenance, bounded access, and action consequences. This swing
sharpens “carrier”:

> A Hilbert-space tensor factor is a representation until physics selects the
> corresponding observable algebra, net region, interaction boundary, or an
> access-preserving equivalent.

A bare Hamiltonian generally selects at most an orbit of subsystem
factorizations under its own symmetries. In the smallest exact witness, the
nondegenerate Hamiltonian

\[
H=\operatorname{diag}(0,1,2,4)
\]

is preserved by controlled-\(Z\). The same unitary moves

\[
\mathcal A_0=M_2\otimes I,\qquad
\mathcal B_0=I\otimes M_2
\]

to a different commuting factor pair. The state \(|++\rangle\) is product in
the original factorization and maximally entangled in the rotated one. Any
Hamiltonian-only natural score is constant on this stabilizer orbit.

That does **not** prove that a Hamiltonian plus a state can never characterize
a factorization. A 2025 theorem by Soulas, Franzmann, and Di Biagio correctly
shows that, for a nondegenerate finite Hamiltonian and a state with nonzero
support on every energy eigenvector, a complete table of subsystem
entropies for all vectors \(R(H)|\psi\rangle\) uniquely characterizes a TPS.
The table spans enough information because those vectors span the full
Hilbert space.

The Dynamic Unity classification is narrower:

> The theorem proves that a target factorization has a complete invariant
> fingerprint. It does not supply a physical rule that chooses the
> fingerprint values from \(H\) and \(|\psi\rangle\) alone.

Indeed, the same fixed \(H,|\psi\rangle\) supports one entropy table for each
candidate TPS. Specifying the desired table is classification data; it is not
yet source selection. This is close to Stoica's 2026 criticism, but the
present result does not adopt his full no-go or deny the theorem's stated
existential result.

The positive boundary is exact. If physics independently supplies commuting
full matrix observable algebras with trivial intersection that generate the
whole operator algebra, those algebras reconstruct a tensor-product
structure. That is the right type of object. It is also exactly the object
Dynamic Unity still lacks in its physical-output candidates.

The return is:

```text
HAMILTONIAN_ONLY_TPS_POINT_SELECTION_BLOCKED_BY_STABILIZER_ORBIT
+ HAMILTONIAN_STATE_CLASSIFICATION_THEOREM_PRESERVED
+ TARGET_DERIVED_ENTROPY_PROFILE_IS_NOT_SOURCE_SELECTION
+ OBSERVABLE_ALGEBRA_PAIR_RECONSTRUCTS_TPS
+ CENTRAL_RECORD_SECTORS_DO_NOT_SELECT_FULL_TPS
+ PHYSICAL_CARRIER_MUST_BE_ALGEBRAICALLY_ANCHORED
+ NO_READY_SCIENTIFIC_SUCCESSOR
```

This is a scoped Grade-4 necessity/nonselection result. It is not a new
quantum-mereology theorem, a physical subsystem derivation, emergent
spacetime, record ontology, or new physics.

## 1. The correct candidate object

Let \(\mathcal H\) be a finite-dimensional Hilbert space and let
\(\operatorname{TPS}_{m,n}(\mathcal H)\) denote bipartite tensor-product
structures

\[
\mathcal H\simeq\mathbb C^m\otimes\mathbb C^n
\]

modulo local basis changes and, when appropriate, factor exchange.

Equivalently, a TPS can be represented by two unital subalgebras

\[
(\mathcal A,\mathcal B)\subseteq B(\mathcal H)
\]

satisfying:

\[
[\mathcal A,\mathcal B]=0,
\qquad
\mathcal A\cap\mathcal B=\mathbb CI,
\qquad
\mathcal A\vee\mathcal B=B(\mathcal H),
\]

with

\[
\mathcal A\simeq M_m(\mathbb C),
\qquad
\mathcal B\simeq M_n(\mathbb C).
\]

This observable-induced view is standard. Zanardi introduced virtual
subsystems in
[2001](https://arxiv.org/abs/quant-ph/0103030), and Zanardi, Lidar, and
Lloyd gave the explicit observable-algebra/TPS correspondence in
[2004](https://arxiv.org/abs/quant-ph/0308043).

The distinction matters physically:

```text
abstract vector-space isomorphism H ~= H_A tensor H_B
    !=
selected observable algebras A and B
    !=
formed output carrier
    !=
retained accessible record.
```

## 2. Stabilizer-orbit selection boundary

Let an antecedent \(S\) be acted on by a unitary group, and let
\(\mathcal K\) be a class of candidate structures under the same action.
Suppose a selection score

\[
f(S,K)
\]

is natural:

\[
f(USU^\dagger,UKU^\dagger)=f(S,K).
\]

### Theorem 1 — stabilizer-orbit constancy

For every \(U\in\operatorname{Stab}(S)\),

\[
f(S,UKU^\dagger)=f(S,K).
\]

Therefore a source-only natural criterion can point-select \(K\) only if the
winning stabilizer orbit is one point under the declared physical
equivalence. Otherwise the maximum selected object is the orbit.

### Proof

If \(USU^\dagger=S\), naturality gives

\[
f(S,UKU^\dagger)
=f(USU^\dagger,UKU^\dagger)
=f(S,K).
\]

\(\square\)

This is the subsystem instance of `HC-DU-033F`'s antecedent-fibre theorem. The
new work is applying it to the carrier factor required by `HC-DU-075` and
installing the exact minimum witness below.

## 3. Exact four-dimensional witness

Use the standard two-qubit factor pair

\[
\mathcal A_0=M_2\otimes I,
\qquad
\mathcal B_0=I\otimes M_2.
\]

Let

\[
W=CZ=\operatorname{diag}(1,1,1,-1)
\]

and

\[
H=\operatorname{diag}(0,1,2,4).
\]

The spectrum of \(H\) is nondegenerate and

\[
[W,H]=0.
\]

Nevertheless:

\[
W(X\otimes I)W^\dagger=X\otimes Z,
\]

\[
W(I\otimes X)W^\dagger=Z\otimes X.
\]

Thus

\[
(\mathcal A_1,\mathcal B_1)
=
(W\mathcal A_0W^\dagger,W\mathcal B_0W^\dagger)
\]

is a distinct commuting factor pair preserved in the same Hamiltonian
antecedent fibre.

The physical meaning is visible on one fixed state:

\[
|\psi\rangle=|+\rangle\otimes|+\rangle.
\]

Relative to \((\mathcal A_0,\mathcal B_0)\), its subsystem entropy is zero.
Relative to the rotated TPS it equals the entropy of

\[
W^\dagger|\psi\rangle
=
\frac{|00\rangle+|01\rangle+|10\rangle-|11\rangle}{2},
\]

which is one bit. Entanglement, local observables, and candidate carrier
identity have changed while the Hamiltonian has not.

The executable verifies:

- nondegenerate source spectrum;
- exact Hamiltonian invariance under \(CZ\);
- both factor pairs commute, have scalar intersection, and generate all of
  \(M_4\);
- the local generators are moved;
- product entropy \(0\) versus entanglement entropy \(1\); and
- a dephasing-selected two-sector center remains compatible with both full
  factor pairs.

The last item corrects a tempting shortcut: selecting central record sectors
does not automatically select the complete subsystem decomposition or
multiplicity matching inside those sectors.

## 4. Why adding the state changes the theorem

The same witness must not be broadened carelessly.

For \(|\psi\rangle=|++\rangle\),

\[
|\langle\psi|W|\psi\rangle|=\frac12,
\]

so \(W\) does not stabilize the pair \((H,|\psi\rangle)\). More generally,
when \(H\) is nondegenerate and \(|\psi\rangle\) has nonzero support on every
energy eigenvector, the only diagonal phase symmetry fixing both is a global
phase.

The Hamiltonian-only orbit obstruction is therefore not a theorem that every
\((H,|\psi\rangle)\) pair has multiple factorization orbits. A state can
remove the immediate symmetry degeneracy.

Removing a no-go is not yet supplying a selector.

## 5. The 2025 invariant classifier, stated fairly

Soulas, Franzmann, and Di Biagio's
[Theorem 3.9](https://arxiv.org/abs/2512.07468) assumes:

1. a finite-dimensional \(\mathcal H\);
2. a nondegenerate Hamiltonian spectrum;
3. a state with nonzero projection on every energy eigenvector; and
4. the number and dimensions of the desired tensor factors supplied in
   advance.

Under the first three conditions,

\[
\{R(H)|\psi\rangle:R\in\mathbb C[X]\}=\mathcal H.
\]

For a candidate TPS \(T\), define the full profile

\[
L_T
=
\left\{
S\!\left(
\rho_i^T(R(H)|\psi\rangle)
\right)
:
R\in\mathbb C[X],\ i=1,\ldots,n
\right\}.
\]

Because the polynomial orbit spans every vector, equality of this entropy
profile for two TPSs forces them to agree on the pure-tensor variety and
hence to be the same TPS up to local transformations.

That is a valid and useful classification theorem.

### The selector distinction

For fixed \(H,|\psi\rangle\), the property

\[
P_L(H,|\psi\rangle,T)
\]

says that the entropies equal the externally specified values \(L\). To
select a particular target \(T_*\), the proof takes

\[
L=L_{T_*}.
\]

The values are calculated using the factorization that they later identify.
The theorem shows:

```text
target TPS
  -> complete invariant fingerprint
  -> target TPS uniquely classified.
```

It does not yet show:

```text
H and psi
  -> independently chosen physical law for L
  -> one TPS selected.
```

The exact witness makes this visible without disputing the theorem. For the
same \(H,|++\rangle\):

- \(L_{T_0}\) assigns zero entropy to the \(R=1\) vector;
- \(L_{T_1}\) assigns one bit to that same vector.

Either table identifies its own TPS. The source pair alone does not say which
table is the physical constraint.

Stoica's 2026
[comment](https://arxiv.org/abs/2602.20331) makes a related and stronger
criticism: the invariant values function as added input and physical
relevance remains unresolved. Dynamic Unity adopts only the narrow
classification/selection boundary above. The wider debate about Hilbert
space fundamentalism and time dependence remains open.

## 6. Constructive programs and their exact status

The literature does contain more physical candidate criteria:

| program | actual contribution | DU classification |
|---|---|---|
| Cotler et al., [locality from the spectrum](https://doi.org/10.1007/s00220-019-03376-w) | Generic \(k\)-locality can constrain an equivalence class of TPSs once factor count, dimensions, and locality class are fixed | Conditional source-relative criterion, not an access/record formation theorem |
| Carroll--Singh, [quantum mereology](https://arxiv.org/abs/2005.12938) | Searches factorizations for low entanglement growth and quasi-classical pointer dynamics | Constructive objective relative to supplied factor sizes, pointer/classicality objective, and approximation choices |
| Zanardi et al., [operational quantum mereology](https://arxiv.org/abs/2212.14340) | Defines generalized TPSs as an algebra/commutant pair and proposes minimum short-time scrambling as a dynamical criterion | Right-type carrier-algebra candidate; still needs candidate class, uniqueness/tie control, physical access, formation, provenance, and held-out transfer |
| Loizeau--Sels, [subsystems from the spectrum](https://arxiv.org/abs/2409.01391) | Relates subsystem and spectral decompositions and seeks size/locality signatures | Conditional reconstruction program, not a formed-record selector |
| Soulas--Franzmann--Di Biagio, [relational invariant classifier](https://arxiv.org/abs/2512.07468) | Proves existence of a complete TPS fingerprint from \(H,\psi\) plus specified entropy values | Classification/identification after supplying the fingerprint; no autonomous physical value selector |

None should be dismissed. None currently closes the Dynamic Unity conjunction:

```text
source-selected carrier algebra
  + physical blank-to-written formation
  + retention and provenance
  + bounded observer access
  + independently held-out target consequence.
```

Minimal scrambling is the most relevant constructive bridge because it acts
directly on observable algebras. But selecting a minimally scrambling algebra
does not itself show that the algebra is an outgoing carrier, that anything
has been written to it, or that an observer can retain and act on it.

## 7. Positive reconstruction theorem

### Theorem 2 — observable algebras determine the finite TPS

Let \(\mathcal A,\mathcal B\subseteq B(\mathcal H)\) be commuting unital full
matrix algebras such that:

\[
\mathcal A\cap\mathcal B=\mathbb CI,
\qquad
\mathcal A\vee\mathcal B=B(\mathcal H).
\]

Then there is a unitary

\[
U:\mathcal H\longrightarrow\mathbb C^m\otimes\mathbb C^n
\]

with

\[
U\mathcal AU^\dagger=M_m\otimes I,
\qquad
U\mathcal BU^\dagger=I\otimes M_n.
\]

The induced TPS is unique up to local unitaries and any declared equal-factor
permutation.

This is standard finite-dimensional operator-algebra structure. The probe's
two factor pairs supply positive controls: each pair commutes, intersects
only in scalars, and its products span all 16 dimensions of \(M_4\).

The theorem answers “what would be enough?”:

> Physics need not label abstract tensor factors. It can select mutually
> commuting physical action/observable algebras that jointly exhaust the
> admitted system.

What remains open is whether a serious physical antecedent selects those
algebras without importing the observer, detector, region, or desired
record.

## 8. Quantum-record passport correction

The `HC-DU-075` passport used a carrier \(E\). The physical version should be
read as:

\[
\mathcal Q=
\left(
\mathfrak A_{\rm car},
\Psi,
\mathfrak A_{\rm acc},
\beta,
\mathcal R,
\mathcal P,
\mathcal M
\right),
\]

where:

- \(\mathfrak A_{\rm car}\) is a selected physical observable algebra or net
  region inside the total theory;
- \(\Psi\) is the source-to-carrier process;
- \(\mathfrak A_{\rm acc}\subseteq\mathfrak A_{\rm car}\) is the bounded
  observer-access algebra;
- \(\beta\) is the blank/input condition;
- \(\mathcal R\) is retained future-readable evolution;
- \(\mathcal P\) is source/route/epoch provenance; and
- \(\mathcal M\) is a target-independent action menu.

A tensor-factor notation may represent this structure after it is selected.
It does not select it.

In AQFT, a net can supply candidate local algebras relative to a spacetime
region. The region, probe coupling, archive route, and observer access still
require receipts. In finite input--output models, a Stinespring factor
supplies a mathematical complement. A physical output algebra and access
boundary remain additional unless the model's actual field content and
local couplings select them.

## 9. What changed and what did not

### Changed

1. The carrier bottleneck is now upstream of measurement: physical subsystem
   algebra selection must be receipted.
2. “Hamiltonian plus state can characterize a TPS” no longer counts
   automatically as “the source selects its physical parts.”
3. Quantum-mereology methods are live candidate selectors, not solved record
   theories.
4. The most promising form is algebraic and operational, not a bare
   factorization of vectors.
5. A dynamically selected classical center can coexist with an unselected
   full subsystem factorization.

### Unchanged

1. A selected subsystem is not yet a formed record.
2. A formed quantum carrier need not already be classical.
3. Observer actions may select later classical shadows without creating the
   upstream carrier.
4. No current physical candidate closes formation, provenance, retention,
   bounded access, and held-out reconstruction.
5. The selected-record campaign remains quiescent and Swing 2 remains
   inactive.

## 10. Grade, kill, and reopener

### Earned grade

Scoped Grade 4:

- exact stabilizer-orbit necessity;
- exact two-qubit witness;
- exact algebra-pair positive reconstruction condition;
- fair classification/selection audit of the 2025 theorem; and
- physical-carrier passport refinement.

### Strongest absorber

The mathematics is absorbed by:

- observable-induced TPS and virtual-subsystem theory;
- locality and quantum-mereology selection programs;
- invariant classification;
- finite operator-algebra reconstruction; and
- Dynamic Unity's prior antecedent-fibre theorem.

### Kill condition

The Hamiltonian-only point-selection claim is killed by one source symmetry
that moves the TPS. The broader Hamiltonian--state impossibility claim is
itself killed by the full-support-state control and is not made.

### Reopener

Reopen physical subsystem selection only when one antecedent independently
fixes:

1. the candidate algebra class and physical equivalence;
2. a unique algebra or access-preserving orbit under a physically motivated
   criterion;
3. a localized source-to-carrier formation process;
4. finite retention, provenance, and observer access;
5. one target-independent action menu; and
6. one independently escrowed target consequence.

No external hardware is needed before such a candidate exists.

## Reproducibility

Run:

```bash
python3 tests/du_subsystem_factor_selection_probe.py
```

The deterministic receipt checks 19 exact finite properties and writes
`tests/artifacts/du_subsystem_factor_selection_result.json`.
