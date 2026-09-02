---
title: "Action-selected spinor bilinear response family, operational quotient, and record boundary"
status: banked_scoped_response_family_selection_and_sufficiency_result
doc_type: exact_spinor_reconstruction_theorem_coupling_family_audit_and_twistor_boundary
created: 2026-09-01
claim_id: HC-DU-222
run_id: RUN-20260901-spinor-bilinear-response-family-and-operational-quotient
program_id: CCR-MINIMAL-PHYSICAL-ANTECEDENT-TO-FINITE-REMAINDER
owner_repo: dynamic-unity
evidence_grade: 4
maximum_evidence_grade: 4
---

# Executive result

`HC-DU-221` separated spin/twistor transport, reference-relative visibility,
and material recording. This wave asks a more productive question than whether
the source action selects one detector:

> Can the action select the complete *family of physical response channels*,
> with the actual apparatus selecting one member of that family?

The answer is yes in ordinary field theory, relative to the action's supplied
carrier, symmetries, field content, and coupling constants. That family induces
a canonical operational quotient:

\[
 \rho\sim_{\mathcal V}\rho'
 \quad\Longleftrightarrow\quad
 \operatorname{tr}[(\rho-\rho')A]=0
 \text{ for every }A\in\mathcal V,
\tag{1}
\]

where `V` is the linear span of physically admitted response observables.

The exact spinor comparison then exposes a carrier-dependent boundary:

```text
two-component Weyl current
  -> complete for the local projective spinor/density operator

four-component Dirac vector current
  -> incomplete; 12 operator directions remain

full scalar + pseudoscalar + vector + axial + tensor Dirac family
  -> complete 16-dimensional matrix span.
```

Thus a source action can select meaningful physical distinctions before it
selects a detector. But this is still not a material record. Field content and
the action determine which couplings are possible; preparation or environmental
dynamics realizes a coupling; an instrument, transducer, archive, provenance
chain, access route, and consumer remain downstream.

The disposition is:

```text
ACTION_CAN_SELECT_RESPONSE_FAMILY_BEFORE_DETECTOR
+ WEYL_CURRENT_RECONSTRUCTS_PROJECTIVE_TWO_SPINOR
+ DIRAC_VECTOR_CURRENT_IS_NOT_STATE_COMPLETE
+ FULL_DIRAC_BILINEAR_FAMILY_IS_ALGEBRAICALLY_COMPLETE
+ COUPLING_FIELD_CONTENT_SELECTS_OPERATIONAL_QUOTIENT
+ REFERENCE_EXTENSION_CAN_REOPEN_ERASED_PHASE
+ RESPONSE_FAMILY_IS_NOT_MATERIAL_RECORD
+ NO_READY_SUCCESSOR
```

No new spinor, twistor, tomography, QFT, or measurement theorem is claimed.
The Dynamic Unity contribution is the action-to-response-family placement and
the exact carrier-dependent sufficiency boundary.

# 1. Response families, not one universal detector

Let `H` be a finite carrier and let `V` be the real linear span of Hermitian
operators that occur in the declared physical interaction family. A state is
operationally represented by

\[
 R_{\mathcal V}(\rho)
   =\big(\operatorname{tr}(\rho A)\big)_{A\in\mathcal V}.
\tag{2}
\]

Equation (1) is the fibre relation of this response map. It has an exact linear
description:

\[
 R_{\mathcal V}(\rho)=R_{\mathcal V}(\rho')
 \quad\Longleftrightarrow\quad
 \rho-\rho'\in\mathcal V^\perp
\tag{3}
\]

under the Hilbert--Schmidt pairing. If `V` spans the full operator space, the
response is state-complete. If it does not, every physically allowed
state-difference in `V`'s orthogonal complement is an exact same-response /
different-state witness.

This is elementary quantum tomography and dual-space linear algebra. Its
importance here is architectural:

```text
source action, symmetry, and field content
  -> permitted interaction/response family V
  -> operational state quotient H / ~V
  -> one prepared or dynamically realized vertex
  -> instrument and outcome
  -> retained material record and access.
```

The first two arrows need not wait for a detector. Conversely, neither arrow
forms a record.

# 2. Exact Weyl current reconstruction

For a two-component spinor `psi`, use

\[
 \sigma^\mu=(I,X,Y,Z),
 \qquad
 j^\mu=\psi^\dagger\sigma^\mu\psi.
\tag{4}
\]

The four matrices span the full complex two-by-two matrix space. For a
normalized density operator,

\[
 \rho=\frac12\left(j^0I+j^1X+j^2Y+j^3Z\right).
\tag{5}
\]

For a normalized pure spinor,

\[
 (j^0)^2-(j^1)^2-(j^2)^2-(j^3)^2=0.
\tag{6}
\]

The spatial current is the Bloch sphere. It fixes the projective spinor ray,
while

\[
 \psi\mapsto e^{i\alpha}\psi
\tag{7}
\]

leaves every current component unchanged.

## Theorem 1 — Weyl-current projective completeness

On the two-component carrier, equality of all four current components is
equivalent to equality of density operators. On pure normalized states it is
equivalent to equality of projective rays.

This result gives a concrete geometry-to-response bridge: the spinor bilinear
defines a future-null spacetime direction and reconstructs the local quantum
ray. It does not reconstruct a global phase, nor should it.

The exact probe verifies (5)--(7) on the six Pauli eigenstates using Gaussian
rational arithmetic.

# 3. Dirac vector-current insufficiency

For a four-component Dirac spinor, the standard bilinear families have
dimensions

\[
 1+1+4+4+6=16:
\tag{8}
\]

- scalar;
- pseudoscalar;
- vector;
- axial vector; and
- antisymmetric tensor.

They correspond to a basis built from

\[
 I,\quad \gamma^5,\quad \gamma^\mu,\quad
 \gamma^\mu\gamma^5,\quad \sigma^{\mu\nu}.
\tag{9}
\]

The exact probe constructs a Dirac gamma representation over Gaussian
rationals, verifies the Clifford relations, and finds rank sixteen for (9).
Multiplication by invertible `gamma^0` preserves that span when these matrices
are used as expectation-value observables.

The vector-current family alone is

\[
 j^\mu=\bar\psi\gamma^\mu\psi
        =\psi^\dagger\gamma^0\gamma^\mu\psi.
\tag{10}
\]

Its operator span has rank four. The orthogonal operator remainder therefore
has dimension

\[
 16-4=12.
\tag{11}
\]

The exact witness is especially small. Positive-energy upper spin-up and
upper spin-down basis states are orthogonal but both give

\[
 j^\mu=(1,0,0,0).
\tag{12}

Another Dirac bilinear distinguishes them.

## Theorem 2 — carrier-relative current sufficiency

The full Weyl-current family is operator-complete for a two-component carrier.
The Dirac vector current is not operator-complete for a four-component carrier.
The full sixteen-element Dirac bilinear family is algebraically complete.

This is not a claim that every bilinear can be measured simultaneously, that
all are independently unconstrained on pure spinors, or that a physical theory
contains mediators for every channel. Fierz identities constrain values on
spinor states; the exact rank statement concerns the operator span. Bilinear
classification and its Fierz structure are mature subjects; see Bonora, de
Brito, and da Rocha's [arbitrary-dimensional classification](https://arxiv.org/abs/1411.1590).

# 4. What the action actually selects

A concrete field theory does more than announce Lorentz covariance. Its field
content and action determine which interaction vertices occur.

Examples include:

\[
 A_\mu\bar\psi\gamma^\mu\psi
 \quad\text{(vector gauge coupling)},
\tag{13}
\]

\[
 \phi\bar\psi\psi
 \quad\text{(scalar/Yukawa coupling)},
\tag{14}
\]

and axial, pseudoscalar, tensor, or higher-dimensional EFT interactions when
the mediator content and symmetries permit them.

Consequently:

1. **Lorentz covariance does not select one response family.** All five types
   in (8) have covariant roles.
2. **A full action can select a response family conditionally.** Once its
   fields, representations, charges, symmetries, and coefficients are fixed,
   its interaction vertices are physical law, not an analyst's arbitrary
   measurement list.
3. **That family need not be state-complete.** QED's vector coupling does not
   become a complete local Dirac-state tomography merely because it is
   dynamically real.
4. **Incompleteness need not be a defect.** States identified by every admitted
   physical coupling are operationally equivalent for that theory and action
   envelope. A new mediator or intervention enlarges the response family and
   can refine the quotient.

This corrects an overstrict reading of the North Star. Dynamic Unity should not
require the source law alone to choose one universal detector. It may instead
ask whether the law naturally generates the admissible response family while a
precommitted apparatus or environment selects and realizes one interaction.
Claims of autonomous classicality still owe the stronger interface-selection
arrow.

# 5. Projective phase and reference extension

Every spin-only bilinear is invariant under (7), so the central `-I` return of
`HC-DU-221` remains erased locally. This is not an information deficit inside
the physical ray.

The distinction becomes physical only in an enlarged interaction algebra. For

\[
 |\Psi_\pm\rangle
   =|0\rangle|\psi\rangle\pm|1\rangle|\psi\rangle,
\tag{15}
\]

all spin-only reduced responses agree, while

\[
 \langle\Psi_\pm|X_{\rm path}\otimes I|\Psi_\pm\rangle
 =\pm 2
\tag{16}

in the unnormalized exact control.

The reference does not uncover a hidden absolute phase. It creates a larger
physical relational system in which the phase difference is represented by an
allowed cross-path coupling.

That gives a precise DU rule:

> When a distinction is absent from one action-selected response family but
> present after a physical reference or mediator is added, classify the move as
> an action/interface enlargement, not improved knowledge of the unchanged
> system.

# 6. Twistor consequence

A twistor contains Weyl-spinor components and packages null/conformal geometry.
The Weyl result therefore supplies a clean local possibility:

```text
projective two-spinor
  <-> null current/flag direction
  -> conformal or twistor incidence structure.
```

But the interaction family remains action-relative. Twistor actions can encode
self-dual and full Yang--Mills sectors, and matter multiplets can be coupled in
specified constructions. Those are genuine action-level bridges, not automatic
material records. See Mason's [twistor actions for non-self-dual
fields](https://arxiv.org/abs/hep-th/0507269), Boels, Mason, and Skinner's
[supersymmetric gauge theories with matter in twistor
space](https://arxiv.org/abs/hep-th/0604040), and Popov's [twistor-space Yang--Mills
action](https://arxiv.org/abs/2103.11840).

Also keep two different references separate. A reference twistor used to fix an
axial gauge in an amplitude construction is a gauge/calculation choice. The
coherent reference arm in `HC-DU-221` is a physical subsystem whose relative
phase affects a measurement. Matching vocabulary does not identify them.

# 7. What changed for the North Star

Before this wave, the live chain risked demanding that one source action select
every downstream object at once. The corrected decomposition is:

```text
law-level selection
  carrier + symmetries + field content + permitted response family

conditional experiment
  independently prepared interaction + instrument + archive + access

autonomous-classicality claim
  source-plus-environment dynamics selects the realized interaction and handoff

reconstruction/remainder test
  retained record is sufficient or fails for a locked target under that action envelope.
```

This is a substantive positive refinement. It says what a physical law can
reasonably select before observers and instruments exist: not necessarily one
view, but the admissible family of ways systems can physically respond to one
another.

It does not lower the material-record standard. A response expectation, current,
interaction vertex, S-matrix element, or complete tomographic coordinate is not
a blank-to-written archive with provenance and access.

# 8. Grade, absorbers, and reopener

The wave earns scoped Grade 4 for:

1. the exact operational-quotient theorem in the frozen finite carrier;
2. Weyl-current projective completeness;
3. Dirac vector-current incompleteness with an orthogonal state witness;
4. full Dirac-bilinear algebraic completeness;
5. the action-level response-family selection correction; and
6. preservation of the reference-relative phase and material-record boundaries.

It does not earn:

- derivation of Standard Model field content or couplings;
- simultaneous physical realization of every bilinear channel;
- a detector, outcome, archive, observer, access route, or finality rule;
- a twistor action for DU or GU;
- a physical remainder or empirical prediction; or
- new physics.

The strongest absorbers are Pauli/Bloch reconstruction, Fierz/bilinear spinor
classification, Noether currents, standard gauge/Yukawa interaction vertices,
EFT operator bases, projective quantum states, tomography, and twistor action
theory.

The exact reopener is a physical candidate whose action naturally generates a
response family `V` and for which one can prove at least one of:

1. `V` is sufficient for a locked observer-accessible target while remaining
   noninjective on irrelevant microstate structure;
2. source-plus-environment dynamics selects one material handoff from `V`;
3. no admissible response-family enlargement removes an exact finite remainder;
   or
4. the same response-family construction transfers without refit across two
   physical regimes.

No current candidate clears that reopener, so the portfolio remains
`no_ready`.

# 9. Reproduction

Run:

```bash
python3 tests/du_spinor_bilinear_response_quotient_probe.py --write-artifact
```

The deterministic artifact is
`tests/artifacts/du_spinor_bilinear_response_quotient_result.json` and reports
`13/13` checks.
