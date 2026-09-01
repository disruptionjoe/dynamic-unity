---
title: "GU K77 trace reversal, 2+1 origin, luminous polarization, and the record boundary"
status: banked_conditional_bridge_and_exact_type_separation
doc_type: cross_repo_conditional_theorem_and_exact_finite_control
created: 2026-08-31
claim_id: HC-DU-209
run_id: RUN-20260831-gu-k77-luminous-polarization-bridge
action_id: GU-K77-LUMINOUS-POLARIZATION-BRIDGE-AUDIT
owner_repo: dynamic-unity
external_source_repo: gu-formalization
evidence_grade: 4
gu_transfer_grade: 1
maximum_evidence_grade: 4
portfolio_return: CONDITIONAL_RELATIONAL_LUMINOUS_ORBIT_WITH_UNSELECTED_2PLUS1_COUPLING_AND_RECORD
---

> **GU-COMPARATOR-ROUTING — scope before inference.** This artifact contains or
> borders a conventional particle-physics comparator. Any result about a
> standard Higgs/VEV, ordinary family index or net chirality, SO(10) `126`
> Majorana mechanism, anomaly selector, VEV-only breaking or familiar vector-
> mass route binds only that named model. It is not evidence for or against
> Weinstein's source-native mechanism without an explicit typed bridge. Read
> `../../gu-formalization/lab/methods/source-native-comparator-routing.md` and
> follow its source-native pointers before reusing this result.

# Executive result

Joe's proposed join is structurally important, but it contains six typed axes
that must not be identified:

1. trace reversal of the vertical Frobenius metric supplies GU's indefinite
   carrier;
2. W/mirror names the two cross-paired halves of that carrier;
3. `2+1` says where two true-family slots and one effective imposter slot come
   from;
4. fundamental chirality describes the complete theory's handedness;
5. luminous/non-luminous says which sector remains light, coupled, and
   accessible in one physical regime; and
6. a material record says how a physical occurrence is sampled, retained,
   routed, and used.

The exact finite control earns one conditional positive theorem:

> A swap-symmetric, globally non-chiral parent can select a unique relational
> luminous-half orbit through an action-owned odd order parameter. At low
> curvature two conjugate stable vacua make one half light and the other
> heavy. At high curvature the symmetric vacuum is restored and the halves
> recouple.

It also earns two exact boundaries:

- the `2+1` origin grading commutes with the luminous/mirror grading, so the
  mere existence of two true slots and one imposter slot selects neither the
  luminous half nor an imposter-specific response coupling; and
- even a selected luminous projector admits inequivalent QND instruments with
  the same effect and orthogonal conditional continuations.

The result is therefore:

```text
trace-reversed paired carrier
  + action-owned exchange-odd order parameter
  + curvature-dependent stability law
  -> relational luminous-half orbit

relational luminous-half orbit
  -/-> derived 2+1 response coupling
  -/-> selected material record interface.
```

The conditional theorem is scoped Grade 4. Its transfer to current GU is only
Grade 1 because the GU repository does not yet supply the complete source
action, stationary background, exchange-odd order parameter, curvature law,
or derived imposter-sensitive coupling. Landau symmetry breaking, Krein/Witt
decomposition, equivariant bifurcation, and quantum-instrument nonuniqueness
absorb the mathematics. No new physics or GU verdict is claimed.

# 1. Correction: current K77, not the older K95 fork

The prior conversational summary used the older conditional `(9,5)` carrier.
That is not the correct current source-native object for this question.

The current GU routing authority distinguishes:

- the settled K77 chimeric metric: horizontal `(1,3)` plus trace-reversed
  vertical `(6,4)`, yielding a total split `(7,7)` carrier; and
- the older conditional K95 `(9,5)` construction, which remains a rival fork.

The trace reversal itself acts on the vertical Frobenius metric of the
symmetric metric fibre:

\[
S^2T^*X:\quad (7,3)\longrightarrow(6,4).
\]

This audit uses K77. It does not import K95's quaternionic carrier,
coefficients, chirality operator, or imposter construction into K77.

Source routing:

- [GU object boundary](../../gu-formalization/GEOMETER-VS-PHYSICS-OBJECTS.md)
  distinguishes the current K77 and older K95 objects;
- [source-native comparator routing](../../gu-formalization/lab/methods/source-native-comparator-routing.md)
  makes the non-chiral `2+1` target explicit; and
- [source-native high-energy `2+1` audit](../../gu-formalization/lab/active-research/joe-directed/high-energy-two-plus-one/he1-imposter-separation-invariant-2026-08-14.md)
  locates the two true-family sectors and effective imposter/remainder sector
  without supplying their physical coupling law; and
- [current GU next-step record](../../gu-formalization/NEXT-STEPS.md)
  records the exact W/mirror pairing and luminous-selection boundaries.

# 2. The six typed axes

| Axis | Mathematical role | Current status |
|---|---|---|
| K77 trace-reversed form | Indefinite carrier and W/mirror cross-pairing | Source-owned geometry |
| W/mirror half grading | Two conjugate carrier halves | Kinematically located, no half selected |
| `2+1` origin grading | Two true-family slots plus one effective imposter slot | Source-native label/construction, not a physical coupling law |
| Fundamental chirality | Net/graded chirality of the complete theory | GU target remains globally non-chiral |
| Luminous status | Which sector is light, stable, coupled, and accessible in a regime | Open action/dynamics burden |
| Material record | Sampler, writer, provenance, archive, observer access, consumer | Not selected by the preceding structures |

“Luminous” is therefore not another spelling of fundamental chirality. The
strongest coherent reading is relational and dynamical:

> luminous means the half that remains light and operationally coupled
> relative to the selected broken vacuum and curvature regime.

# 3. What trace reversal supplies—and what it does not

The current K77 work reports that the owned trace-`H_q` form vanishes on the W
half and on its mirror separately, while their cross-pair is nondegenerate. On
`W direct-sum mirror` the full form has Witt inertia `(192,192)`.

The six-dimensional exact control uses the minimal faithful shadow

\[
B=I_3\otimes
\begin{pmatrix}0&1\\1&0\end{pmatrix},
\qquad
L=I_3\otimes
\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\]

Here `L` names W versus mirror and `B` pairs them. The projectors

\[
P_W=\frac{I+L}{2},
\qquad
P_M=\frac{I-L}{2}
\]

satisfy

\[
P_W^TBP_W=P_M^TBP_M=0,
\]

while the cross-pair has full rank three. Thus the form supplies a relation
between the halves, not a positive form on either half and not a preferred
half.

This is the first correction to the intuitive story:

```text
trace reversal makes luminous selection possible to formulate
  !=
trace reversal performs luminous selection.
```

# 4. The `2+1` axis is independent

Let

\[
O=\operatorname{diag}(0,0,1)\otimes I_2
\]

project onto the imposter-origin slot. The complement contains the two true
slots. Then

\[
[O,L]=0.
\]

Each half contains the same `2+1` pattern: two true slots and one imposter
slot. The W/mirror exchange flips `L` and preserves `O`.

Consequently, neither label determines the other. In particular, both

\[
G_{\rm equal}=\operatorname{diag}(1,1,1)
\]

and

\[
G_{\rm split}=\operatorname{diag}(1,1,2)
\]

can multiply the same odd W/mirror response while preserving exchange
covariance and equivalence of the two true slots. One treats the imposter like
the true slots; the other gives it a different response. The typed geometry
admits both.

Current GU representation work supplies possible separators—representation
type, pairing ladders, Casimirs, and Dynkin indices—but does not yet derive
which one enters the physical source action, with what coefficient or scale.
The exact `2+1` label is therefore not yet a luminous-coupling law.

This also preserves the repository's imposter homonym fence. The source-native
effective imposter label and the separate `144` partner/comparator are not
silently identified.

# 5. Conditional luminous-polarization theorem

## Antecedent

Let `E` exchange W and mirror, and let a real order parameter `z` be odd:

\[
E:L\mapsto-L,
\qquad z\mapsto-z.
\]

Use the even potential

\[
V_R(z)=\frac14z^4+\frac12a(R)z^2,
\]

where `R` is a declared curvature response and `a(R)` changes sign at one
critical regime. Let the matter response be

\[
M^2(z)=m_0^2I-gzL.
\]

This is a conditional normal form. `z` is a coordinate on a possible
action-owned order-parameter orbit, not a proposal to add a separate Higgs
scalar to GU. A valid GU realization must derive it from the source-native
connection, curvature, distortion, nonzero-fermion Hessian, BV/BFV complex,
or analytic domain.

## Theorem 1 — matched luminous orbit

If `a(R)<0`, the stable minima are

\[
z_\pm=\pm\sqrt{-a(R)}.
\]

At `z_+`, one half is lighter; at `z_-`, its exchanged partner is lighter.
The two complete descriptions are related by

\[
(z_+,P_W)\longleftrightarrow(z_-,P_M).
\]

Therefore the absolute name W or mirror is not selected, but the relational
statement

```text
the half aligned with the selected vacuum is luminous
```

is unique on the physical exchange orbit.

If `a(R)>0`, the unique stable minimum is `z=0`, for which

\[
M^2(0)=m_0^2I.
\]

The two halves are response-degenerate and recouple. `square`

This gives a mathematically coherent version of Weinstein's stated picture:
a globally non-chiral parent, low-curvature chiral-looking separation, and
high-curvature reconnection. It is standard spontaneous-symmetry-breaking
mathematics, not evidence that GU contains the required term.

## Why this advances DU

`HC-DU-204` established that absolute labels need not be selected when a
matched producer--consumer orbit descends. The theorem above applies the same
correction to physical sectors: an action need not declare “W is luminous.” It
can select the matched orbit “the vacuum-aligned half is luminous.”

That is a real way around an overly strong half-selection demand. It does not
avoid the need to derive the action and vacuum.

# 6. Exact source-selection obstruction in current GU

Current GU work already establishes the negative controls this theorem needs:

- the W and mirror principal fingerprints coincide;
- trace-`H_q` pairs the halves rather than choosing one;
- compatibility admits both the full and block-preserving parents;
- a real exchange-invariant action Hessian at an exchange-fixed stationary
  background has equal W/mirror rank and spectrum; and
- the currently tested physical-operator inventory supplies no
  luminous-half selector.

Therefore the required positive object must be one of:

1. an action-owned stationary vacuum not fixed by W/mirror exchange;
2. an exchange-odd composite order parameter derived from existing GU fields;
3. an asymmetric but source-owned BV/BFV or closed-domain condition; or
4. a boundary/initial condition whose physical provenance and selection law
   are explicit.

Choosing a projector, compatible connection, holonomy sign, positive half, or
external VEV after seeing the desired luminous sector does not qualify.

# 7. Sector selection is still not record formation

The broken-vacuum theorem can select a physical action/capability sector. It
does not select a material record.

In the finite control, the luminous projector has rank three. A unitary that
exchanges the two true-family slots commutes with:

- the `2+1` origin projector;
- the selected luminous projector; and
- the broken-vacuum mass response.

The Lüders operations and the within-sector-twisted operations have identical
luminous/mirror effects. One true-family input receives the same certain
luminous result but has orthogonal conditional continuations.

Thus the `HC-DU-208` boundary survives:

```text
action-selected luminous capability sector
  != selected sampler
  != selected pointer/archive/provenance
  != selected observer access
  != selected consumer or public finality.
```

This is not a criticism of the luminous mechanism. It locates it one rung
earlier in the North-Star ladder: it could select the physical sector whose
interactions later form records.

# 8. Complete bridge passport

| Field | Current disposition |
|---|---|
| K77 trace-reversed indefinite carrier | Source-owned |
| W/mirror exchange and cross-pair | Source-owned / exactly reconstructed |
| `2+1` origin labels | Source-native construction, typed separately |
| Full GU source action | Not complete |
| Stationary background | Not selected for this mechanism |
| Exchange-odd order parameter | Not derived |
| Curvature-dependent sign change | Source-stated shape, no equation/coefficient |
| Relational luminous projector | Conditionally selected by Theorem 1 |
| Imposter-sensitive coupling | Not selected |
| Material sampler and writer | Not selected |
| Provenance, archive, access, consumer | Not selected |
| Public finality and record reconstruction | Not reached |

# 9. Grade, novelty, and routing

## Earned

- an exact separation of trace/Krein, `2+1` origin, chirality, luminous status,
  and material-record types;
- a conditional theorem showing how a non-chiral parent can select a matched
  luminous orbit without selecting an absolute half;
- an exact low-curvature separation / high-curvature reconnection control;
- an exact `2+1`-coupling ambiguity; and
- an exact proof that luminous-sector selection does not yet close the DU
  record gate.

## Not earned

- the GU source action or stationary vacuum;
- a GU-derived order parameter, curvature threshold, coupling, mass, or
  observed particle spectrum;
- a physical third generation or chirality mechanism;
- a material record, observer, or finality law;
- empirical excess or a new physical theory.

## Routing

This is a sharper conditional reopener, not an executable DU successor. The
next load-bearing construction is owned upstream by GU:

1. derive the exchange-odd order parameter from the full action rather than
   adding it;
2. prove a non-exchange-fixed stationary orbit and its stability;
3. derive the curvature dependence and W/mirror mass response;
4. derive rather than fit the imposter-sensitive coupling; and
5. export the resulting action/domain/state/process packet for DU's independent
   instrument, record, access, and no-refit tests.

Until then Dynamic Unity remains explicitly no-ready. GU repository state was
read as external evidence and was not modified.
