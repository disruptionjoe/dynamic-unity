---
title: "Relational reference from symmetry reduction: embodied coupling and certificate boundary"
status: banked_scoped_result
doc_type: exploration
created: 2026-07-30
claim_id: HC-DU-175
run_id: RUN-20260730-173717-relational-reference-symmetry-reduction
work_id: RELATIONAL-REFERENCE-SYMMETRY-REDUCTION-GATE
action_id: RELATIONAL-REFERENCE-SYMMETRY-REDUCTION-GATE
program_id: CCR-MINIMAL-PHYSICAL-ANTECEDENT-TO-FINITE-REMAINDER
owner_repo: dynamic-unity
evidence_grade: 4
maximum_grade: 4
---

# Relational reference from symmetry reduction

## Executive result

`HC-DU-174` established that joined regional coherence access needs a
physical relation among local controls, not one absolute global phase frame.
It left that relation supplied.

The obvious next construction—showing that a material phase law selects a
phase orbit—was already banked by the endogenous-record and autonomous-
finality audits. Repeating a Josephson, XY, Kuramoto, flatness, or holonomy
version would rename existing knowledge.

The surviving result is sharper:

> A process covariant under every independent local phase cannot create the
> nontrivial character mode required for a relational reference from a
> locally phase-invariant input. A physical cross-region interaction can
> create that mode without choosing any absolute phase by reducing
> \(U(1)^2\) to its diagonal \(U(1)\).

The smallest positive control is an ordinary number-conserving exchange
interaction. Starting from the locally phase-invariant state
\(|10\rangle\langle10|\), it creates a coherent superposition of
\(|10\rangle\) and \(|01\rangle\). Each local reduced state remains diagonal:
the new resource exists only in the relation.

The more consequential finding is operational:

> A stable physical coupling can itself embody the relational reference for
> a bounded prepare-and-invert task. An explicit classical phase label is
> sufficient but not necessary.

Using the same coupling for preparation and inversion returns the input with
probability one for every coupling phase. If the readout coupling is
mismatched by \(\delta\), the return probability is

\[
\cos^2(\delta/2).
\]

This corrects an overly narrow reading of “reference certificate.” The
reference may be:

- an explicit retained phase carrier;
- a correlation with another system; or
- a stable reusable interaction that implements the same relational
  standard across actions.

But coherent interaction is not yet a record. The construction is exactly
reversible, retains no occurrence provenance, and does not supply a portable
archive, observer access boundary, fault model, or public-finality rule.

The complete return is:

```text
COUPLED_PHASE_ORBIT_DUPLICATE_STOP
+ FULL_LOCAL_COVARIANCE_NO_GENERATION
+ DIAGONAL_U1_SYMMETRY_REDUCTION
+ RELATIONAL_COHERENCE_WITH_ZERO_LOCAL_COHERENCE
+ NO_ABSOLUTE_FRAME_SELECTED
+ STABLE_COUPLING_AS_ACTION_RELATIVE_REFERENCE
+ PHASE_MISMATCH_COSINE_SQUARED_ACCESS_LAW
+ PHYSICAL_RANDOMIZATION_AND_FIXED_UNKNOWN_PHASE_SEPARATED
+ COHERENCE_NOT_YET_CERTIFICATE
+ KNOWN_ASYMMETRY_QRF_WAY_AND_EXCHANGE_ABSORPTION
+ NO_NEW_PHYSICS_OR_READY_SUCCESSOR
```

This is a scoped Grade-4 necessity and selection result inside standard
finite quantum mechanics. It does not supply empirical excess.

## 1. Duplicate gate

Four tempting claims were already occupied inside Dynamic Unity:

1. symmetric material dynamics can select a phase orbit without selecting
   one oriented token;
2. conservation and asymmetry magnitude constrain measurement but do not
   select an oriented reference;
3. multipartite phase can live only in joined correlations and be recovered
   by local controls plus pooling; and
4. graph-cycle phases and holonomies classify gluing obstructions.

Those results remain controls. No new credit is assigned to a generic
phase-locking, flat-connection, or cycle-holonomy theorem.

The open seam was where the relational character required by `HC-DU-174`
enters the physical process.

## 2. Character-mode no-generation theorem

Let

\[
G=U(1)_A\times U(1)_B
\]

act on two excitation modes through

\[
U_{\alpha,\beta}
=
\exp[-i(\alpha N_A+\beta N_B)].
\]

Call a state locally phase invariant when

\[
U_{\alpha,\beta}\rho U_{\alpha,\beta}^\dagger=\rho
\quad
\text{for all }(\alpha,\beta).
\]

The operator

\[
X_{\mathrm{rel}}=|10\rangle\langle01|
\]

transforms as

\[
U_{\alpha,\beta}
X_{\mathrm{rel}}
U_{\alpha,\beta}^\dagger
=
e^{-i(\alpha-\beta)}
X_{\mathrm{rel}}.
\tag{1}
\]

It lies in a nontrivial character mode of \(G\).

Let \(\Phi\) be \(G\)-covariant:

\[
\Phi(U_g\rho U_g^\dagger)
=
U_g\Phi(\rho)U_g^\dagger.
\tag{2}
\]

If \(\rho\) is \(G\)-invariant, Equations (1)--(2) imply that
\(\Phi(\rho)\) is also \(G\)-invariant. Consequently

\[
\boxed{
\langle10|\Phi(\rho)|01\rangle=0.
}
\tag{3}
\]

This is the finite two-region specialization of the standard modes-of-
asymmetry result. In character-projector language,

\[
\mathcal P_\chi(X)
=
\int_G dg\,
\overline{\chi(g)}
U_g X U_g^\dagger,
\]

and covariance gives

\[
\Phi\mathcal P_\chi
=
\mathcal P_\chi\Phi.
\]

No nontrivial output mode can appear when the corresponding input mode is
zero.

### What the theorem does and does not say

It does not say relational coherence is impossible. It says one of these
must be physically present:

1. an input resource carrying the needed character;
2. an environment/reference state carrying it;
3. a channel that does not respect the full independent local symmetry; or
4. a larger relational system in which the mode is already stored in
   correlations.

This is a provenance statement about the reference resource, not a
preferred-frame theorem.

## 3. Exact symmetry-reduction positive control

Freeze the number-conserving exchange Hamiltonian

\[
H_\phi
=
J\left(
e^{i\phi}|10\rangle\langle01|
+
e^{-i\phi}|01\rangle\langle10|
\right).
\tag{4}
\]

It obeys

\[
[H_\phi,N_A+N_B]=0
\]

but

\[
[H_\phi,N_A]\neq0,
\qquad
[H_\phi,N_B]\neq0.
\]

Thus the interaction preserves the diagonal \(U(1)\) generated by total
excitation while reducing the independent \(U(1)^2\) symmetry.

With \(\tau=Jt\),

\[
e^{-iH_\phi t}|10\rangle
=
\cos\tau\,|10\rangle
-i e^{-i\phi}\sin\tau\,|01\rangle.
\tag{5}
\]

The resulting relational coherence is

\[
\boxed{
\langle10|\rho_\phi(\tau)|01\rangle
=
i e^{i\phi}\cos\tau\sin\tau.
}
\tag{6}
\]

At \(\tau=\pi/4\), its magnitude is \(1/2\). Yet both local reduced states
are diagonal. The interaction has created mutual/internal coherence without
creating either local phase orientation.

This is the constructive answer:

```text
locally phase-invariant systems
+ physical cross-region exchange relation
-> relational coherence
+ conserved total excitation
+ no absolute phase
```

## 4. Why no absolute frame has been smuggled in

A local coordinate change gives

\[
U_{\alpha,\beta}
H_\phi
U_{\alpha,\beta}^\dagger
=
H_{\phi-\alpha+\beta}.
\tag{7}
\]

The created state transforms by the same rule. A common shift
\(\alpha=\beta\) changes neither the Hamiltonian nor any state on the
one-excitation sector.

Therefore:

- \(\phi\) is not an absolute phase;
- the physical object is the relation encoded by the coupling and state
  together; and
- the unbroken diagonal \(U(1)\) leaves one absolute origin unselected.

On a two-node graph the coupling phase can be moved by a basis change. That
does not make the coupling physically irrelevant: the same interaction
defines which preparations and readouts compose. Gauge-invariant cycle
holonomy becomes relevant only on larger loops, and that classification is
already banked elsewhere.

## 5. Stable coupling as an embodied reference

Prepare with

\[
U_\phi=e^{-iH_\phi t}
\quad\text{at}\quad
Jt=\pi/4
\]

and decode with \(U_{\phi+\delta}^\dagger\). The probability of returning to
\(|10\rangle\) is

\[
\boxed{
P_{\mathrm{return}}(\delta)
=
\cos^2(\delta/2).
}
\tag{8}
\]

In particular,

\[
P_{\mathrm{return}}(0)=1
\]

for every value of \(\phi\). The bounded task needs no numerical phase label
when the same stable physical coupling is reused.

This earns a broader category of **relational reference resource**:

> A physical structure functions as a reference for an action family when
> reusing it makes the relevant relational transformations compose
> reproducibly, even if it never emits a detached classical coordinate.

This is action-relative and is **not automatically a certificate**. The
stable coupling does not by itself rival-exclude its own provenance or prove
a historical occurrence. It is also not automatically:

- portable to a disconnected region;
- independently readable;
- retained after the device changes;
- provenance-bearing for one historical interaction;
- robust to an admitted fault class; or
- public across systems that cannot access the coupling.

An embodied standard and a durable record remain different interface types.

## 6. Randomization, ignorance, and relocation

For a physically randomized run-to-run coupling phase with distribution
\(p(\phi)\), the system-only coherence is multiplied by

\[
\Gamma_\phi
=
\mathbb E[e^{i\phi}].
\tag{9}
\]

A uniform four-phase control has \(\Gamma_\phi=0\), so the reduced ensemble
contains no relative-character coherence.

If a phase carrier \(R\) is retained,

\[
\rho_{RS}
=
\sum_\phi
p(\phi)
|\phi\rangle\langle\phi|_R
\otimes
\rho_\phi,
\tag{10}
\]

then conditioning on \(R\) restores

\[
e^{-i\phi}
\langle10|\rho_\phi|01\rangle
=
i\cos\tau\sin\tau.
\tag{11}
\]

Equation (10) is a record-relocation positive control, not an endogenous
archive theorem. The register and its joined lineage are supplied.

Keep three cases separate:

1. **actual physical randomization:** the ensemble really contains different
   couplings;
2. **restricted operational access:** the admitted observer cannot resolve
   the phase carrier; and
3. **fixed but unknown \(\phi\):** the physical state remains coherent, and
   stable self-referenced operations can still exploit it.

Epistemic uncertainty alone is not physical dephasing.

## 7. Selected-versus-supplied ledger

| object | status |
|---|---|
| two regional excitation modes | supplied |
| local \(U(1)^2\) action | supplied representation contract |
| locally invariant input | supplied |
| total-number conservation | derived for \(H_\phi\) |
| reduction \(U(1)^2\to U(1)_{\mathrm{diag}}\) | derived |
| relational character no-generation under full covariance | necessary theorem |
| relational coherence under exchange | derived physical positive |
| absence of local coherence | derived |
| absence of an absolute phase | derived covariance result |
| exchange Hamiltonian and coupling support | supplied physical antecedent |
| stable reuse as bounded action reference | derived conditionally |
| phase label or carrier | supplied in the relocation control |
| one-run occurrence provenance | absent |
| retained material archive | absent |
| portable/public certificate | absent |
| observer/access and fault/finality class | supplied or absent |
| new dynamics or empirical excess | absent |

The interaction is a target-blind physical selector **within the frozen
model**. This does not explain why nature selected that Hamiltonian, region,
material carrier, or coupling history.

## 8. Literature collision and novelty

The mathematical core is occupied:

- Marvian and Spekkens prove that symmetry modes are preserved mode-by-mode
  by covariant processing, so an output mode requires the corresponding
  input resource:
  [*Modes of asymmetry*](https://arxiv.org/abs/1312.0680).
- Their WAY/no-programming account shows why symmetric processing needs an
  asymmetric resource to simulate an asymmetric measurement:
  [*An information-theoretic account of the Wigner--Araki--Yanase
  theorem*](https://arxiv.org/abs/1212.3378).
- Bartlett, Rudolph, and Spekkens review group twirling, missing reference
  frames, and relational encodings:
  [*Reference frames, superselection rules, and quantum
  information*](https://arxiv.org/abs/quant-ph/0610030).
- Martinelli and Soares-Pinto explicitly study local, global, and mutual
  asymmetry, identifying mutual/internal coherence as a relational resource:
  [*Quantifying quantum reference frames in composed
  systems*](https://arxiv.org/abs/1808.04209).
- De la Hamette and Galley construct quantum-reference changes directly from
  group actions and physical reference systems:
  [*Quantum reference frames for general symmetry
  groups*](https://arxiv.org/abs/2004.14292).

Number-conserving exchange, beam-splitter dynamics, phase mismatch, and
coherent inversion are standard quantum mechanics.

Dynamic Unity's earned increment is the typed bridge:

```text
reference needed for regional access
-> nontrivial character mode
-> full-local-covariance no-generation
-> symmetry-reducing cross-region interaction
-> embodied action-relative reference
-/-> retained provenance-bearing certificate
```

No new theorem in asymmetry theory, quantum reference frames, interferometry,
or many-body physics is claimed.

## 9. North-Star consequence

`HC-DU-174` should no longer be read as demanding an externally calibrated
absolute frame or even necessarily a detached reference record.

The minimum physical search packet is now:

```text
regional carrier and decomposition
+ symmetry-reducing interaction or asymmetric resource
+ stability over the admitted action family
+ source-to-interaction provenance
+ retained carrier only when portability/history requires it
+ joined access and fault/finality contract
```

This is real narrowing. A future source-pinned candidate must say which
object breaks the independent local symmetry:

- a cross-region coupling;
- an environment/reference state;
- a pump or controller;
- a boundary condition;
- or a retained correlated carrier.

Merely reporting aligned measurement axes, phase-lock quality, or successful
pooling does not identify that source.

The result does not activate the flagship. No current source-pinned specimen
selects the full carrier--interaction--provenance--archive--access packet,
and the external-custody QEC reopener remains unchanged.

## 10. Reproducibility

Run:

```bash
python3 tests/du_relational_reference_symmetry_reduction_probe.py \
  --write-artifact
```

The exact regression checks:

1. local \(U(1)^2\) invariance of the input;
2. no character generation in full-covariance controls;
3. total-number conservation and local-symmetry reduction;
4. exact relational coherence with diagonal local marginals;
5. reversible time dependence;
6. joint Hamiltonian/state rephasing covariance;
7. retained global-phase freedom;
8. system-only loss under physical phase randomization;
9. conditional recovery with a retained relation;
10. the \(\cos^2(\delta/2)\) mismatch law; and
11. the no-record coherent round trip.

Passing verifies the finite formulas. It does not simulate a laboratory or
select a record interface.

## Final status

**BANKED SCOPED RESULT / A FULLY \(U(1)^2\)-COVARIANT PROCESS CANNOT CREATE
THE NONTRIVIAL RELATIVE CHARACTER FROM A LOCALLY INVARIANT INPUT / AN
ORDINARY TOTAL-NUMBER-CONSERVING EXCHANGE INTERACTION CREATES RELATIONAL
COHERENCE BY REDUCING \(U(1)^2\) TO DIAGONAL \(U(1)\) WHILE EVERY LOCAL
MARGINAL REMAINS PHASE-INVARIANT / NO ABSOLUTE FRAME IS SELECTED / REUSING
THE SAME STABLE COUPLING EMBODIES THE RELATION FOR A BOUNDED ACTION FAMILY,
WITH MISMATCH RESPONSE \(\cos^2(\delta/2)\) / AN EMBODIED REFERENCE NEED NOT
BE A CLASSICAL LABEL, BUT REVERSIBLE COHERENCE IS NOT A RETAINED,
PROVENANCE-BEARING OR PUBLIC CERTIFICATE / STANDARD MODES-OF-ASYMMETRY, QRF,
WAY, MUTUAL-ASYMMETRY AND EXCHANGE PHYSICS ABSORB THE COMPONENTS / NO NEW
PHYSICS, EMPIRICAL EXCESS, HARDWARE, PAPER OR READY SUCCESSOR.**
