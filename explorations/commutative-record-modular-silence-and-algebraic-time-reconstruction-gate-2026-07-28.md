---
title: "Commutative-record modular silence and algebraic-time reconstruction gate"
status: completed
doc_type: exploration_result
created: 2026-07-28
claim_id: HC-DU-077
run_id: RUN-20260728-115711-modular-time-reconstruction-gate
run_plan: "system-runtime#meta/runs/history/repositories/dynamic-unity/lab/process/runs/RUN-20260728-115711-modular-time-reconstruction-gate/run-plan.md"
run_receipt: "../lab/process/runs/RUN-20260728-115711-modular-time-reconstruction-gate/run-receipt.md"
owner_repo: dynamic-unity
---

# Commutative-record modular silence and algebraic time

## Executive result

Dynamic Unity now has an exact boundary on one of the strongest algebraic
routes from quantum structure to time.

Tomita--Takesaki theory assigns a canonical modular automorphism group to a
von Neumann algebra together with a faithful normal state or standard vector.
In special quantum-field-theory settings, modular groups act geometrically.
This makes modular theory a serious candidate bridge from the
observable-algebra carrier required by `HC-DU-076` toward the North Star's
time and geometry targets.

But a classical record algebra is commutative, and:

> Every faithful state on a commutative von Neumann algebra is tracial, so
> its intrinsic modular automorphism group is trivial.

The obstruction is not missing statistical detail. Even the complete state
on the commutative record algebra is modularly silent.

The smallest hostile control is two-dimensional. Let

\[
\mathcal D=\operatorname{span}\{I,Z\}\subset M_2
\]

be the complete classical record algebra and compare the faithful ambient
states

\[
\rho_0=\frac I2,
\qquad
\rho_c=\frac12\left(I+\frac35X\right).
\]

They agree on every \(D\in\mathcal D\):

\[
\operatorname{Tr}(\rho_0D)
=
\operatorname{Tr}(\rho_cD).
\]

Nevertheless, \(\rho_0\) has trivial ambient modular flow while
\(\rho_c\) generates a nontrivial flow on \(M_2\) and moves \(Z\) outside
\(\mathcal D\). Thus the complete classical record state does not determine
the modular dynamics of a noncommutative ambient theory.

The positive route remains substantial:

```text
selected noncommutative algebra
  + selected faithful state or weight
    -> canonical dimensionless modular flow
  + physical calibration or dynamical identification
    -> candidate observer time
  + selected inclusions/net and modular-position conditions
    -> translations, symmetry, or geometric modular action
  + formed records, provenance, access, and held-out transfer
    -> Dynamic Unity reconstruction candidate.
```

The return is:

```text
COMMUTATIVE_RECORD_ALGEBRA_HAS_TRIVIAL_INTRINSIC_MODULAR_FLOW
+ COMPLETE_RECORD_STATE_DOES_NOT_FIX_AMBIENT_MODULAR_DYNAMICS
+ NONCOMMUTATIVE_ALGEBRA_STATE_PAIR_SELECTS_DIMENSIONLESS_MODULAR_FLOW
+ PHYSICAL_TIME_REQUIRES_CALIBRATION_OR_DYNAMICAL_IDENTIFICATION
+ GEOMETRIC_RECONSTRUCTION_REQUIRES_MODULAR_INCLUSIONS_OR_A_NET
+ COVARIANT_PREFERRED_STATE_IS_NOT_GENERICALLY_AVAILABLE
+ NO_READY_SCIENTIFIC_SUCCESSOR
```

This is a scoped Grade-4 necessity/non-reconstruction result composed from
standard modular mathematics. It is not a new Tomita--Takesaki theorem,
proper-time derivation, spacetime reconstruction, record ontology, or new
physics.

## 1. The typed modular object

Let \(\mathcal M\) be a von Neumann algebra and let \(\omega\) be a faithful
normal state. In a standard representation with cyclic and separating vector
\(\Omega\), the Tomita operator

\[
S_0(A\Omega)=A^*\Omega
\]

has polar decomposition

\[
S=J\Delta^{1/2}.
\]

Tomita--Takesaki theory gives the modular automorphisms

\[
\sigma_t^\omega(A)
=
\Delta^{it}A\Delta^{-it},
\qquad
t\in\mathbb R.
\]

In finite dimension, with density matrix \(\rho>0\),

\[
\sigma_t^\rho(A)
=
\rho^{it}A\rho^{-it}.
\]

This flow is canonical relative to the pair \((\mathcal M,\omega)\). It is
not selected by the abstract algebra alone, by the state alone, or by a
commutative record quotient.

## 2. The commutative modular-silence theorem

### Theorem 1

Let \(\mathcal D\) be a commutative von Neumann algebra and let \(\omega\) be
a faithful normal state. Then

\[
\sigma_t^\omega(D)=D
\]

for every \(D\in\mathcal D\) and \(t\in\mathbb R\).

### Proof

Every state on a commutative algebra is tracial because

\[
\omega(AB)=\omega(BA)
\]

holds identically. A faithful normal state is tracial exactly when its modular
automorphism group is trivial. Therefore the modular group of
\((\mathcal D,\omega)\) fixes every element. \(\square\)

### Scope

The theorem does **not** say that a classical causal record cannot contain:

- an explicitly recorded order;
- a clock value;
- a transition history;
- waiting-time statistics; or
- a time parameter supplied by its transition law.

It says that none of those becomes nontrivial **intrinsic modular flow** merely
by knowing the complete state on a commutative record algebra. If time or
order is already written into the record schema, that is a different
reconstruction contract and must pass the no-circularity test.

## 3. Same complete record, different ambient modular dynamics

### Theorem 2

The restriction

\[
(\mathcal M,\omega)
\longmapsto
(\mathcal D,\omega|_{\mathcal D})
\]

does not in general determine the modular automorphism group on
\(\mathcal M\), even when \(\mathcal D\subset\mathcal M\) is fixed and both
ambient states are faithful.

### Exact witness

Take

\[
\mathcal M=M_2,
\qquad
\mathcal D=\operatorname{span}\{I,Z\}.
\]

The states

\[
\rho_0=\frac I2,
\qquad
\rho_c=\frac12\left(I+\frac35X\right)
\]

are faithful. Since every \(D\in\mathcal D\) is diagonal and \(X\) is
off-diagonal,

\[
\operatorname{Tr}(XD)=0.
\]

Hence their restrictions to \(\mathcal D\) are identical.

For \(\rho_0\),

\[
\sigma_t^{\rho_0}(A)=A
\]

for all \(A\in M_2\). For \(\rho_c\), the eigenvalues are \(4/5\) and \(1/5\),
so the flow has nontrivial eigenvalue-ratio phase \(4^{it}\). At \(t=1\),
the executable gives

\[
\left\|
\sigma_1^{\rho_c}(Z)-Z
\right\|_{\rm HS}
\approx 1.8073,
\]

and the off-diagonal magnitude of
\(\sigma_1^{\rho_c}(Z)\) is approximately \(0.9830\).

Therefore:

```text
same algebra of classical record observables
+ same expectation of every record observable
!= same ambient modular flow.
```

This is an exact record-fibre witness for the modular-time target. It does not
show that the ambient flow is physical time.

## 4. The positive noncommutative control

Let

\[
\rho_d=
\begin{pmatrix}
4/5&0\\
0&1/5
\end{pmatrix}.
\]

Then:

\[
\sigma_t^{\rho_d}(Z)=Z,
\]

but

\[
\sigma_t^{\rho_d}(|0\rangle\langle1|)
=
4^{it}|0\rangle\langle1|.
\]

Thus the diagonal record algebra is pointwise fixed while off-diagonal
observables carry nontrivial modular evolution.

The useful physical lesson is not that coherence is “time.” It is:

> The noncommutative relations discarded by a classical record quotient can
> carry modular information absent from every record value in that quotient.

Those relations are either:

1. an operational remainder for the declared record interface; or
2. structure the complete certified causal description must reconstruct by
   interventions, inclusions, or another independently specified relation.

## 5. Modular parameter is not yet physical time

Tomita--Takesaki supplies a canonical real parameter \(t\) for a fixed
algebra--state pair. The parameter is dimensionless.

For a Gibbs state

\[
\rho=Z^{-1}e^{-\beta H},
\]

finite-dimensional modular flow satisfies, up to the sign convention for
Heisenberg evolution,

\[
\sigma_t^\rho(A)
=
e^{-i\beta tH}A e^{i\beta tH}.
\]

The conversion to physical time therefore uses the inverse-temperature scale
\(\beta\) and the physical Hamiltonian.

The exact probe also checks the algebraic rescaling:

\[
\rho_\alpha
=
\frac{\rho^\alpha}{\operatorname{Tr}(\rho^\alpha)}
\quad\Longrightarrow\quad
\sigma_t^{\rho_\alpha}
=
\sigma_{\alpha t}^{\rho}.
\]

This is not an ambiguity at fixed \((\mathcal M,\rho)\); changing the state
changes the antecedent. It demonstrates why a modular group alone does not
supply a dimensionful clock calibration.

Connes and Rovelli's
[thermal-time hypothesis](https://arxiv.org/abs/gr-qc/9406019) proposes a
physical interpretation of the state-dependent modular flow. The modular
flow is a theorem; its universal identification with physical time is a
hypothesis whose calibration and state-selection conditions remain part of
the physical claim.

## 6. When modular flow becomes geometric

### Bisognano--Wichmann

For suitable relativistic QFTs, the modular group of a wedge algebra in the
vacuum acts as the wedge-preserving Lorentz boosts. Mund derives the property
for a large class of massive Poincaré-covariant models in four dimensions
([primary source](https://arxiv.org/abs/hep-th/0101227)). Guido's
[review](https://arxiv.org/abs/0812.1511) details the theorem and related
reconstruction results.

This is a profound positive identification. It is not a record-first
derivation from classical facts. The standard statement already has:

- a QFT net;
- Minkowski spacetime;
- a wedge region and its algebra;
- the vacuum vector;
- locality/covariance and spectrum conditions; and
- a cyclic/separating standardness condition.

The theorem identifies the modular flow of that physically typed pair with a
known geometric symmetry.

### Modular inclusions

A half-sided modular inclusion contains strictly more structure than one
algebra:

\[
(\mathcal N\subset\mathcal M,\Omega),
\]

where \(\Omega\) is cyclic and separating for the relevant algebras and one
modular group maps \(\mathcal N\) into itself on one half-line. Under the
standard hypotheses, the relative modular data generates a positive-energy
translation group. Suitable families or modular positions can reconstruct
larger spacetime symmetry groups and nets.

This is the constructive lesson. Relative algebra position can encode order
and translation unavailable in one commutative ledger. It also makes the
premises explicit:

- at least two selected algebras;
- a selected common state/vector or weight;
- an inclusion relation;
- half-sided modularity;
- positivity/spectrum conditions; and
- additional intersections or families for local nets.

Araki and Zsidó give the repaired/generalized half-sided-inclusion structure
theorem ([primary source](https://arxiv.org/abs/math/0412061)). Guido's review
notes that nontriviality of reconstructed bounded-region algebras is not
automatic.

## 7. The state-selection obstruction

The algebra does not generally choose the faithful state required for its
modular flow.

Fewster and Verch prove, under dynamical locality and typical assumptions, a
model-independent obstruction to selecting one preferred state naturally
across all globally hyperbolic spacetimes
([primary source](https://arxiv.org/abs/1106.4785)).

This does not prove that no physical situation selects a state:

- Minkowski vacuum structure can do so in its declared arena;
- boundary or preparation conditions can select state families;
- KMS conditions can select equilibrium classes; and
- cosmological or observer conditions may supply additional data.

It blocks treating a generally covariant preferred state as a free universal
ingredient. A Dynamic Unity modular-time claim must receipt state selection
at the same grade as algebra and access selection.

## 8. Minimum modular reconstruction ladder

The resulting typed ladder is:

| rung | supplied or selected object | earned result | not yet earned |
|---|---|---|---|
| `M0` | commutative record algebra \(\mathcal D\) plus complete state | trivial intrinsic modular group | nontrivial modular time |
| `M1` | noncommutative \(\mathcal M\) plus faithful \(\omega\) | canonical modular automorphism group | physical clock calibration |
| `M2` | physical dynamics/KMS relation or another calibration | modular parameter related to an observer evolution | spacetime geometry |
| `M3` | selected inclusions/net, common standard state, modular-position and positivity conditions | translations or geometric modular action in the theorem's class | independently formed records |
| `M4` | source-to-record formation, provenance, bounded access, actions, and held-out target | candidate DU record-conditioned reconstruction | ontology |

This ladder prevents four substitutions:

```text
classical facts != ambient quantum algebra
modular flow != dimensionful physical time
geometric modular action != geometry selected from nothing
algebraic reconstruction != formed accessible record reconstruction.
```

## 9. North-Star consequence

The North Star remains open, but one possible overly narrow record ontology is
closed.

If “complete records” means only a commutative algebra of public values and
its complete probability law, those records cannot reconstruct nontrivial
modular time. The ambient noncommutative algebra--state relation is a finite
operational remainder in the exact witness.

Three live interpretations remain:

1. **Physics-first remainder.** The ambient noncommutative modular structure
   is physical information not captured by the classical record algebra.
2. **Enriched record-first reconstruction.** Complete certified causal
   records include enough intervention/response and inclusion structure to
   reconstruct the ambient algebra--state--inclusion triple.
3. **Operational duality.** The enriched record presentation and algebraic
   QFT presentation mutually reconstruct the same observer-accessible
   modular/geometric structure without selecting ontological priority.

The swing does not choose among them.

The most important new research question is:

> Can an independently formed certified causal process reconstruct a
> noncommutative algebra, faithful state or state class, and modular inclusion
> up to access-preserving equivalence without putting clock or geometry into
> the record definition?

That is a legitimate high-ceiling reopener. No current physical candidate
supplies its full premise.

## 10. Grade, absorber, stop, and reopener

### Earned

Scoped Grade 4:

- commutative modular-silence necessity;
- exact same-record/different-ambient-modular-flow witness;
- exact noncommutative positive and parameter-rescaling controls;
- typed separation of modular flow, physical time, and geometric action; and
- minimum algebra--state--inclusion reconstruction ladder.

### Strongest absorber

The component mathematics is standard:

- Tomita--Takesaki modular theory;
- finite matrix modular automorphisms;
- thermal time;
- Bisognano--Wichmann;
- Borchers/Wiesbrock/Araki--Zsidó modular inclusions; and
- Fewster--Verch locally covariant state nonselection.

Dynamic Unity's scoped increment is the certified-record restriction theorem,
same-record hostile witness, and North-Star dependency typing.

### Stop

Do not:

- seek modular time inside a commutative record algebra;
- call a written timestamp a derivation of time;
- treat a modular parameter as proper time without calibration;
- claim Bisognano--Wichmann derives its wedge or vacuum from records;
- treat a modular inclusion as a formed record; or
- infer record-first or physics-first ontology.

### Reopener

Reopen modular record reconstruction only when one physical antecedent
independently supplies or selects:

1. a noncommutative observable algebra or net;
2. a faithful state, weight, or physically defined state class;
3. at least one nontrivial inclusion/relative-position structure;
4. a calibration or theorem connecting modular and observer time;
5. formed record provenance and bounded access; and
6. one target-independent intervention family with a held-out temporal or
   geometric consequence.

No external hardware or larger local simulation is warranted before such a
candidate exists.

## Reproducibility

Run:

```bash
python3 tests/du_commutative_record_modular_time_probe.py
```

The deterministic finite receipt checks 19 properties and writes
`tests/artifacts/du_commutative_record_modular_time_result.json`.
