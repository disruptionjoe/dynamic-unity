---
title: "Wilson-Fisher passport derivation and critical-preparation boundary — run plan"
status: complete
doc_type: governed_run_plan
created: 2026-08-31
run_id: RUN-20260831-wilson-fisher-passport-derivation-and-critical-preparation-boundary
work_id: CCR-WILSON-FISHER-PASSPORT-DERIVATION-AND-PREPARATION-BOUNDARY
claim_id: HC-DU-216
owner_repo: dynamic-unity
---

# Exact question

Starting from a microscopic Ising-like action rather than an already named CFT,
which fields of the 3D Ising universality passport are derived by RG dynamics,
which are selected by a physical preparation/intervention, and which remain
supplied by the arena or model contract?

The purpose is to decide whether `HC-DU-215`'s remaining passport burden needs
an autonomous deeper selector, or whether a declared source-plus-preparation
contract already supplies an honest physical explanation for the conditional
critical response.

# Frozen ladder

The tested chain is:

```text
3D short-range microscopic Hamiltonian with Z2 order parameter
  -> coarse-grained one-real-scalar Landau-Ginzburg-Wilson action
  -> RG flow in coupling space
  -> critical-surface preparation
  -> Wilson-Fisher fixed point / 3D Ising CFT passport
  -> HC-DU-215 bootstrap response island.
```

The canonical continuum action is used only schematically:

```text
S[phi] = integral d^3x [
  (1/2)(grad phi)^2 + (r/2)phi^2 + (u/4!)phi^4 - h phi + ...
].
```

The audit separately types:

- spatial dimension and interaction range;
- order parameter, field content, and `Z2` symmetry;
- temperature/mass and magnetic-field relevant directions;
- critical tuning and basin membership;
- RG fixed point and irrelevant-coupling washout;
- conformal/scale-invariant effective passport;
- target critical dimensions/exponents; and
- every material record-interface field.

# Tests

1. **Microscopic-source test.** Determine what the Ising and Blume-Capel
   Hamiltonians fix before any RG argument.
2. **Coarse-graining test.** Identify what is derived versus assumed when a
   local scalar Landau-Ginzburg-Wilson action represents the long-distance
   order parameter.
3. **Linearized-RG test.** Separate relevant, irrelevant, and symmetry-forbidden
   perturbations around the Wilson-Fisher fixed point.
4. **Generic-attractor test.** Ask whether an open set of untuned microscopic
   systems flows to the critical fixed point or only points on a critical
   surface do.
5. **Preparation typing.** Decide when setting `h=0` and `T=T_c` is a legitimate
   declared intervention rather than a copied selector key.
6. **Passport output test.** State which Ising CFT passport fields the
   source-plus-preparation chain supports and at what proof grade.
7. **Record firewall.** Keep critical response, laboratory readout, formed
   archive, causal provenance, access, consumer, and finality separate.

# Primary sources and maximum grade

Primary anchors:

- Kadanoff, *Scaling Laws for Ising Models Near Tc*;
- Wilson, *Renormalization Group and Critical Phenomena I* and *II*;
- Wilson and Fisher, *Critical Exponents in 3.99 Dimensions*;
- Hasenbusch's Ising/Blume-Capel finite-size-scaling study; and
- the mixed-correlator and precision-bootstrap papers already frozen by
  `HC-DU-215`.

Maximum grade is scoped Grade 4 for a typed necessity/nonimplication boundary
and source-grounded disposition. It cannot earn a rigorous proof of the full
3D lattice-Ising-to-CFT limit, a new fixed point, a new critical exponent, or a
selected record interface.

# Absorbers, kill, and stop

Strongest absorbers are Wilsonian RG, Landau-Ginzburg-Wilson effective theory,
critical-surface/stable-manifold theory, finite-size scaling, conformal
bootstrap, and ordinary intervention/preparation semantics.

Cheapest kill: the Wilson-Fisher fixed point has relevant directions, so
generic source dynamics leaves criticality unless symmetry forbids and a
preparation tunes those directions.

Stop if:

- fine tuning is called autonomous law selection;
- a declared experimental preparation is rejected merely because it is not
  source-generated;
- the `epsilon` expansion is called an exact 3D lattice theorem;
- scale invariance is silently promoted to conformal invariance without scope;
- the field/order-parameter map is called uniquely derived for arbitrary
  matter;
- an RG fixed point is called a formed material record; or
- any repository other than Dynamic Unity is written.

# Decision states

```text
SOURCE_ACTION_PARTIALLY_DERIVES_PASSPORT
RG_BASIN_SELECTS_UNIVERSAL_RESPONSE
CRITICAL_SURFACE_NOT_GENERIC_ATTRACTOR
RELEVANT_DIRECTIONS_REQUIRE_SYMMETRY_OR_TUNING
PREPARATION_RELATIVE_SELECTION_VALID
AUTONOMOUS_REGIME_SELECTION_UNEARNED
LATTICE_TO_CFT_LINK_NOT_FULLY_RIGOROUS
COMPLETE_HANDOFF_UNSELECTED
NO_READY_SUCCESSOR
```

# Local-learning boundary

No local simulation is admitted. It cannot improve the theorem boundary over
the established RG and finite-size-scaling literature. No external hardware is
needed.
