---
title: "Spinor/twistor transport, projective phase, interference, and material-readout boundary"
status: banked_scoped_spin_transport_and_interface_necessity_result
doc_type: exact_spinor_control_typed_twistor_extension_and_record_boundary
created: 2026-09-01
claim_id: HC-DU-221
run_id: RUN-20260901-spinor-twistor-transport-interference-and-soldered-readout
program_id: CCR-MINIMAL-PHYSICAL-ANTECEDENT-TO-FINITE-REMAINDER
owner_repo: dynamic-unity
evidence_grade: 4
maximum_evidence_grade: 4
---

# Executive result

This wave tests the proposed richer realization of `HC-DU-220`: spinors or
twistors transported along a physical coupling, with an intertwiner at the
endpoint.

The proposal is structurally coherent, but it contains three independent
arrows:

```text
connection + path
  -> spinor/twistor transport and holonomy
  -> reference-relative observable response
  -> material write, archive, access, and use
```

The exact result is:

```text
SPIN_CONNECTION_SELECTS_TRANSPORT_ORBIT
+ CENTRAL_Z2_PHASE_ERASED_ON_SINGLE_RAY
+ REFERENCE_INTERFERENCE_REOPENS_VISIBILITY
+ READOUT_BASIS_REMAINS_INTERFACE
+ DISTINCT_SPIN_FRAME_REQUIRES_INTERTWINER
+ TWISTOR_TRANSPORT_DOES_NOT_SELECT_MATERIAL_COUPLING
+ NO_READY_SUCCESSOR
```

In plain language:

> A spin connection can transport a spinor and give it a real holonomy. But a
> central `-1` holonomy is only a global phase on one isolated spinor state, so
> the state's ray and density operator do not change. A coherent reference arm
> converts that sign into a relative phase; a suitable recombination and
> measurement basis then makes it visible. None of those later structures is
> selected merely because the connection exists.

Twistors can package conformal, causal, and spinorial transport more richly,
but they do not bypass this ladder. Twistor incidence and transport require
geometric structure; a material detector still requires a physically selected
coupling, transducer, meter, archive, and access route.

This is standard spin, projective-quantum, interferometric, representation, and
twistor mathematics. The Dynamic Unity result is the typed separation and the
exact location of the material-record burden. No new physics is claimed.

# 1. Frozen spin-holonomy control

Use the two-component spinor carrier `C^2` and the eight quaternion/Pauli
holonomies

\[
 \{+I,-I,\pm iX,\pm iY,\pm iZ\}.
\tag{1}
\]

A 24-element octahedral spin-frame shadow acts by conjugation on the three
Pauli axes. Exact enumeration produces three conjugacy orbits:

\[
 \{+I\},\qquad \{-I\},\qquad
 \{\pm iX,\pm iY,\pm iZ\}.
\tag{2}
\]

The raw matrix axis of a noncentral holonomy is frame-dependent. The central
elements remain invariant under every frame change. In the continuous
`SU(2)` description, trace/eigenangle and conjugacy class—not a printed matrix
axis—are the corresponding gauge-covariant data.

This is a finite exact shadow, not a derivation of a Lorentzian spin connection
or a claim that physical holonomies are restricted to (1).

# 2. Projective-erasure theorem

Let `psi` be a nonzero spinor. The central holonomies produce vectors

\[
 \psi_+=\psi,
 \qquad
 \psi_-=-\psi.
\tag{3}
\]

They differ as vectors, but

\[
 [\psi_+]=[\psi_-],
 \qquad
 |\psi_+\rangle\langle\psi_+|
 =|\psi_-\rangle\langle\psi_-|.
\tag{4}
\]

## Theorem 1 — isolated-ray erasure

No measurement on the isolated spinor alone distinguishes the central
holonomies `+I` and `-I` when their only difference is the global phase in
(3).

## Proof

Every isolated-spin measurement probability factors through the density
operator. Equation (4) makes those density operators identical. `square`

This is the first correction to a naive transfer from `HC-DU-220`. A
gauge-invariant or central return sign can be physically real as transport
structure while remaining absent from the declared endpoint state.

It is therefore not yet a record, capability, or even an endpoint-observable
difference.

# 3. Coherent-reference reopener

Introduce a physical path qubit. Send one arm through identity and the other
through spin holonomy `U`. Starting from a coherent equal-arm state gives the
unnormalized joint output

\[
 |0\rangle\otimes|\psi\rangle
 +|1\rangle\otimes U|\psi\rangle.
\tag{5}

For `U=+I`, the path exits as `|+>`; for `U=-I`, it exits as `|->`. Exact
`X`-basis path probabilities are

\[
\begin{array}{c|cc}
U & P(+) & P(-)\\
\hline
+I&1&0\\
-I&0&1.
\end{array}
\tag{6}

The same two cases both give

\[
 P(0)=P(1)=\frac12
\tag{7}

in the path `Z` basis. Deleting or tracing out the path again leaves identical
spin density operators.

## Theorem 2 — visibility is interface-relative

The central spin holonomy becomes perfectly distinguishable after adding a
coherent reference, preserving relative phase, recombining the arms, and
measuring in a phase-sensitive basis. It remains indistinguishable under a
which-path basis or after the reference is deleted.

Thus:

```text
transport holonomy
  != endpoint ray difference
  != reference-relative observable
  != selected material record.
```

The reference arm and readout basis are not cognitive conventions. They are
physical parts of the experiment. But they are additional antecedents and must
be prepared, selected, or dynamically generated at the appropriate claim
grade.

# 4. Distinct spin-frame and intertwiner boundary

For a same-bundle endpoint with a physically fixed path, the connection gives
parallel transport between the two fibres. For a separate target carrier with
an independent spin frame, the coupling needs an intertwiner

\[
 J:S_{\mathrm{source}}\to S_{\mathrm{target}}.
\tag{8}
\]

Under independent source and target frame changes,

\[
 J\mapsto G_T J G_S^{-1}.
\tag{9}
\]

The exact finite Pauli-frame control has four alignments. Independent source
and target frame changes act transitively on all four, fixing none. A coupling
that contains one `J` reduces the product frame freedom to the subgroup that
preserves that intertwiner; deleting the coupling restores the ambiguity.

There is also a positive representation-theoretic repair. In the
two-dimensional irreducible carrier, a complex-linear map commuting with the
full spin action is a scalar by Schur's lemma. The exact finite control verifies
that a real matrix commuting with the generating `X` and `Z` actions is

\[
 J=\lambda I.
\tag{10}
\]

For unitary intertwiners, the complex theory leaves a `U(1)` scalar phase. That
phase is erased on an isolated projective state and can reappear relative to a
reference coupling, exactly as in Section 3.

Consequently, an irreducible representation can contract a large alignment
freedom to a scalar phase, but it does not automatically select the physical
reference that would make the phase observable.

# 5. Where a solder form belongs

Several geometrical maps must not be identified:

- the **spin connection** transports spinors within a selected spin bundle;
- a **path** says which transport is physically realized;
- a **tetrad/solder form** relates tangent-vector and spinor/bispinor geometric
  descriptions;
- an **intertwiner or interaction vertex** couples distinct representations or
  physical systems; and
- a **measurement/transduction coupling** converts a response into a material
  pointer or archive.

A complete action may relate or derive several of these objects. Their
co-occurrence in one formula does not make them the same object. In particular,
a tetrad that relates geometry to spin structure is not automatically a
detector, archive, provenance map, or observer interface.

# 6. Twistor extension

A local twistor may be written schematically as

\[
 Z^\alpha=(\omega^A,\pi_{A'}).
\tag{11}

Its incidence relation has the familiar form

\[
 \omega^A=i x^{AA'}\pi_{A'}.
\tag{12}

This makes twistors promising for the DU seam because one carrier jointly
touches spinorial and conformal/null geometry. But (12) also exposes the
types that must already exist: conformal spin structure, spacetime/incidence
data, and the relation between the twistor and local geometric carrier.

Likewise, twistor transport requires a conformal spin/twistor connection and a
path or propagation process. Even if their holonomy is physically selected,
turning it into a laboratory or observer record still requires a coupling from
the twistor carrier into material degrees of freedom, a phase-sensitive or
dissipative response, a meter, retention, and access.

The finite Pauli/quaternion probe does not construct or validate a full local-
twistor theory. It establishes a type boundary that any such construction must
pass:

```text
twistor incidence/transport
  != selected endpoint intertwiner
  != observable relative phase
  != material record handoff.
```

# 7. The coherent candidate architecture

The strongest version of Joe's suggestion is therefore:

```text
source-pinned action
  -> spin/conformal connection and carrier representation
  -> physically selected path or coupling network
  -> spinor/twistor holonomy
  -> same-bundle transport OR selected inter-system intertwiner
  -> reference-relative observable response
  -> selected material instrument, archive, and access
  -> locked record-conditioned target.
```

This architecture could genuinely connect geometry, quantum state transport,
and record formation. Its scientific content lies in which arrows one action
derives rather than in the fact that all arrows can be written down.

The highest-information future test is not a larger spinor simulation. It is
an action audit asking whether a concrete physical theory simultaneously
selects:

1. the connection and representation;
2. the path/network;
3. the endpoint intertwiner or same-bundle identity;
4. a reference-relative response channel; and
5. a material archive/access handoff.

Deleting any proposed selector should reopen exactly the freedom it claimed to
close.

# 8. Grade and boundaries

The wave earns scoped Grade 4 for:

1. the exact spin-holonomy conjugacy control;
2. isolated-ray erasure of central spin phase;
3. exact coherent-reference and readout-basis discrimination;
4. exact distinct-frame no-fixed-alignment control;
5. the scalar-intertwiner/relative-phase boundary; and
6. a faithful typed twistor-to-material extension.

It does not earn:

- a physical spinor or twistor substrate;
- derivation of a spin/twistor connection, representation, or path;
- selection of a reference arm, interferometer, detector, archive, observer,
  or target ruler;
- a full local-twistor construction;
- GU transfer;
- source issuance, a physical remainder, or empirical excess; or
- new physics.

# 9. Exact reopener

Reopen only with a concrete action or physical platform that supplies a
complete typed packet:

1. source and carrier;
2. spin/twistor connection and path;
3. same-bundle endpoint or derived intertwiner;
4. coherent reference or dissipative response mechanism;
5. fixed measurement/transduction coupling;
6. material archive, provenance, access, reset, and resources; and
7. a locked held-out target.

The candidate must distinguish law-selected structure from prepared apparatus,
survive gauge quotienting and selector deletion, and transfer without refit.
No current DU candidate meets that contract, so the portfolio remains
`no_ready`.

# 10. Reproduction

Run:

```bash
python3 tests/du_spinor_twistor_transport_readout_boundary_probe.py --write-artifact
```

The deterministic artifact is
`tests/artifacts/du_spinor_twistor_transport_readout_boundary_result.json` and
reports `15/15` checks.
