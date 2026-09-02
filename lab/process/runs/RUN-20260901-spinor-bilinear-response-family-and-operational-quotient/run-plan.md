---
title: "Spinor bilinear response family and operational quotient — run plan"
status: complete
doc_type: governed_run_plan
created: 2026-09-01
run_id: RUN-20260901-spinor-bilinear-response-family-and-operational-quotient
work_id: CCR-SPINOR-BILINEAR-RESPONSE-FAMILY-AND-OPERATIONAL-QUOTIENT
claim_id: HC-DU-222
owner_repo: dynamic-unity
---

# Exact question

Can a source-pinned spinor action select a physically meaningful family of
coupling responses that determines the observer-accessible state quotient,
even when it does not select one detector or material record interface?

# Scope and authority

Dynamic Unity is the sole write scope. The wave is local, exact, and
hardware-independent. It tests standard Weyl/Dirac bilinear and twistor-adjacent
geometry as a candidate realization of the `HC-DU-221` chain. It does not
assume GU, a twistor substrate, or new physics.

# Frozen types

1. spinor carrier and projective state;
2. source action and its symmetry/field content;
3. permitted bilinear interaction channels;
4. the linear span of response observables;
5. the induced operational quotient on states;
6. one prepared interaction vertex;
7. one measurement instrument and material archive; and
8. observer access and a held-out target.

# Tests

1. Verify the four Weyl current matrices span the full two-by-two operator
   space and reconstruct every frozen qubit density matrix.
2. Verify the pure-Weyl current is null and determines the projective spinor
   ray while erasing global phase.
3. Construct the sixteen Dirac bilinear covariants and verify exact full rank.
4. Verify the Dirac vector-current subfamily has rank four only.
5. Exhibit two orthogonal Dirac states with identical vector currents and a
   different response in another bilinear channel.
6. Verify the operational-quotient theorem: equal responses are exactly the
   Hilbert--Schmidt orthogonal complement of the admitted response span.
7. Preserve `HC-DU-221`: a path reference can reveal a relative central sign
   that every spin-only bilinear erases.
8. Type the scalar, pseudoscalar, vector, axial, and tensor coupling families
   separately; covariance permits the family decomposition but field content
   and the action select which channels exist.

# Absorbers and grade

The component mathematics is absorbed by Pauli/Bloch reconstruction, Dirac
bilinear covariants, Fierz completeness, Noether currents, local gauge/Yukawa
couplings, effective field theory, projective quantum mechanics, and twistor
incidence/Penrose-transform machinery.

Maximum grade is scoped Grade 4 for an exact action-relative response-family
selection and sufficiency/non-sufficiency boundary. No record, ontology,
twistor dynamics, prediction, or new physics can be earned.

# Cheapest kill and stop

Cheapest kill: the vector current is informationally complete for a Weyl
spinor ray but not for a Dirac spinor state, and no material record follows in
either case.

Stop if:

- bilinear response is renamed a record;
- tomographic completeness is renamed physical interface selection;
- Lorentz covariance is said to select field content or coupling constants;
- a global phase is promoted to a local observable;
- a twistor incidence relation is promoted to an instrument; or
- another repository or external platform is used.

# Decision states

```text
ACTION_CAN_SELECT_RESPONSE_FAMILY_BEFORE_DETECTOR
WEYL_CURRENT_RECONSTRUCTS_PROJECTIVE_TWO_SPINOR
DIRAC_VECTOR_CURRENT_IS_NOT_STATE_COMPLETE
FULL_DIRAC_BILINEAR_FAMILY_IS_ALGEBRAICALLY_COMPLETE
COUPLING_FIELD_CONTENT_SELECTS_OPERATIONAL_QUOTIENT
REFERENCE_EXTENSION_CAN_REOPEN_ERASED_PHASE
RESPONSE_FAMILY_IS_NOT_MATERIAL_RECORD
NO_READY_SUCCESSOR
```
