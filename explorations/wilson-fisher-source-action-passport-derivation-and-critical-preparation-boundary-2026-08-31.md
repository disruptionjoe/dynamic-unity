---
title: "Wilson-Fisher source-action passport derivation and critical-preparation boundary"
status: banked_scoped_source_preparation_response_factorization
doc_type: primary_source_rg_derivation_ladder_selection_boundary_and_portfolio_disposition
created: 2026-08-31
claim_id: HC-DU-216
run_id: RUN-20260831-wilson-fisher-passport-derivation-and-critical-preparation-boundary
program_id: CCR-MINIMAL-PHYSICAL-ANTECEDENT-TO-FINITE-REMAINDER
owner_repo: dynamic-unity
evidence_grade: 4
maximum_evidence_grade: 4
---

# Executive result

The Ising success case does not need one autonomous law that selects its entire
passport. It needs a typed composition of arena, source, preparation, RG
quotient, and response constraints.

```text
SOURCE_ACTION_PARTIALLY_DERIVES_PASSPORT
MICROSCOPIC_SYMMETRY_AND_RANGE_FIX_THE_RG_SECTOR
RG_BASIN_SELECTS_UNIVERSAL_RESPONSE
IRRELEVANT_MICRODETAIL_IS_WASHED_OUT
CRITICAL_SURFACE_NOT_A_GENERIC_ATTRACTOR
RELEVANT_DIRECTIONS_REQUIRE_SYMMETRY_OR_TUNING
PREPARATION_RELATIVE_SELECTION_IS_VALID
AUTONOMOUS_CRITICAL_REGIME_SELECTION_UNEARNED
LATTICE_TO_CFT_LINK_PHYSICALLY_STRONG_NOT_FULLY_RIGOROUS
COMPLETE_MATERIAL_HANDOFF_UNSELECTED
NO_READY_SUCCESSOR
```

A short-range three-dimensional microscopic Hamiltonian with a scalar `Z2`
order parameter supplies more of the CFT passport than `HC-DU-215` credited to
the bootstrap alone. Coarse graining maps its long-distance order-parameter
sector to a one-real-scalar Landau-Ginzburg-Wilson family. RG flow then explains
why many distinct microscopic couplings and even different local spin alphabets
share one universal response: irrelevant perturbations contract toward the
Wilson-Fisher fixed point.

But the fixed point is not a generic attractor in the full coupling space. The
thermal/mass and magnetic-field directions are relevant. Exact `Z2` symmetry
sets the odd magnetic perturbation to zero, while reaching the ordinary
critical point requires tuning temperature or the even mass-like coordinate to
its critical value. A generic untuned system flows away into an ordered or
disordered massive phase.

This makes the selection boundary exact:

> RG dynamics selects the universal response **conditional on basin membership
> and critical-surface preparation**. It does not autonomously select the
> critical regime from a generic source state.

That conditional is not a defect when the scientific target is explicitly
“what will this physically prepared system do at criticality?” A preparation
may be a legitimate action-indexed antecedent rather than a smuggled selector
key. It becomes an explanatory deficit only when a theory claims that its own
uncontrolled dynamics makes criticality obtain.

The Ising passport therefore factorizes as:

```text
arena:        d=3 and spatial/locality contract
source:       short-range scalar order parameter and Z2 symmetry
preparation:  h=0 and temperature/mass tuned to the critical surface
quotient:     RG flow removes irrelevant microscopic detail
response:     Wilson-Fisher/Ising CFT data sharpened by bootstrap consistency.
```

No one arrow selects the complete material handoff. The laboratory apparatus,
formed archive, causal provenance, observer access, consumer/controller,
resource envelope, and finality rule remain separate.

The result is scoped Grade 4 as a source/preparation/response factorization and
selection/nonselection boundary. Wilsonian RG, critical phenomena, and ordinary
experimental preparation absorb its content. No new fixed point, exponent,
CFT theorem, record interface, or physical prediction is claimed.

# 1. Why this is the right upstream test

`HC-DU-215` established a positive response-selection architecture:

```text
supplied 3D Z2 CFT passport
  + crossing / unitarity / mixed-correlator constraints
  + RG microdomain universality
  -> stable critical-response island.
```

It left “why this passport?” as one undifferentiated upstream burden. That
phrase combined at least four questions:

1. Why is the physical arena three-dimensional at the scales considered?
2. Why is the long-distance order parameter a real scalar with `Z2` symmetry?
3. Why is the system in the basin of the Ising/Wilson-Fisher fixed point?
4. Why is it on the critical surface rather than in one of the adjacent
   massive phases?

A microscopic source action can answer the middle two partially without
answering the first or fourth. Treating the passport as one indivisible object
therefore made the selection burden look larger and less physical than it is.

# 2. Microscopic source fields

The two primary lattice specimens from `HC-DU-215` are:

```text
Ising:
H = -beta sum_<xy> s_x s_y - h sum_x s_x,
s_x in {-1,+1};

Blume-Capel:
H = -beta sum_<xy> s_x s_y + D sum_x s_x^2 - h sum_x s_x,
s_x in {-1,0,+1}.
```

They do not share microscopic state spaces or all couplings. They do share:

- a three-dimensional simple-cubic spatial setting in the tested models;
- finite/short-range interactions;
- a scalar magnetization order parameter;
- a global spin-flip `Z2` symmetry when `h=0`; and
- a continuous-transition region for the admitted parameter range.

Hasenbusch explicitly studies both models and multiple `D` values, finding the
same critical exponents after leading corrections to scaling are controlled
([primary paper](https://arxiv.org/abs/1004.4486)).

The microscopic action therefore does select a physical RG sector. It rules
out, for this target, vector order parameters, long-range interactions, broken
`Z2` source terms, other spatial dimensions, and first-order/tricritical
regions. That is real source information, not a relabel of the critical
exponents.

It does not select why physical space is three-dimensional, why one material
has that order parameter, or why an experimental specimen is described by the
Hamiltonian. Those are arena and material-model identification fields.

# 3. Coarse-grained action and its scope

For an Ising-like scalar order parameter, the continuum family is represented
schematically by

```text
S[phi] = integral d^3x [
  (1/2)(grad phi)^2
  + (r/2) phi^2
  + (u/4!) phi^4
  - h phi
  + higher local operators
].
```

The exact `Z2` transformation is `phi -> -phi`; it forbids odd terms when
`h=0`. The mass-like coefficient `r` is controlled by temperature relative to
criticality. The quartic coupling prevents the theory from being a purely
Gaussian model and stabilizes the usual local potential in its admitted
regime.

Kadanoff's block-spin construction introduced the decisive physical move:
divide the Ising model into cells that are large microscopically but small
compared with the correlation length, and use cell magnetization as the
collective variable ([primary paper](https://journals.aps.org/ppf/abstract/10.1103/PhysicsPhysiqueFizika.2.263)).
Wilson then made the scaling flow explicit. His phase-space-cell analysis
integrates successive momentum ranges and obtains a recursion among effective
Landau-Ginzburg-type interactions
([primary paper](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.4.3184)).

This chain earns a long-distance effective representation. It does not prove
that every microscopic `Z2` system has exactly this local truncation, nor that
the displayed finite polynomial is the complete theory. The ellipsis is
essential: RG explains why higher operators may become irrelevant near the
fixed point; it does not license deleting them before their scaling roles are
known.

# 4. Linearized RG and the stable-manifold boundary

Let `g*` denote a fixed point in a theory/coupling space and `delta g` a small
perturbation. Linearizing one coarse-graining step gives

```text
delta g' = M delta g.
```

In an eigenbasis, a scaling field `u_i` changes as

```text
u_i' = b^(y_i) u_i
```

for scale factor `b>1`:

- `y_i<0`: irrelevant; it contracts toward the fixed point;
- `y_i=0`: marginal; nonlinear analysis is required;
- `y_i>0`: relevant; it grows and drives the system away.

For the 3D Ising fixed point, the leading relevant directions are physically
the thermal/even and magnetic/odd perturbations. In CFT notation they are
associated with `epsilon` and `sigma`. Their positive RG eigenvalues are

```text
y_t = 1/nu = d - Delta_epsilon,
y_h = (d+2-eta)/2 = d - Delta_sigma.
```

Using the `HC-DU-215` precision values in `d=3` gives both positive. This is not
a new computation; it restates the standard relation between CFT dimensions
and RG relevance.

Wilson's first RG paper explicitly connects scaling with asymptotic approach
to a fixed point when irrelevant variables are present
([primary paper](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.4.3174)).
Wilson and Fisher then calculate critical exponents for the Ising-like fixed
point in `d=4-epsilon` using RG techniques
([primary paper](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.28.240)).

The dynamical geometry is therefore:

```text
full local coupling space
  contains a critical stable manifold
    flowing toward the Wilson-Fisher fixed point along irrelevant directions;
  relevant perturbations transverse to that manifold
    grow and leave the critical regime.
```

Calling the fixed point an “IR attractor” without the stable-manifold qualifier
is misleading. It attracts a basin **within the critical surface**, not a
generic open neighborhood in the full physical coupling space.

# 5. The two relevant directions are selected differently

The two relevant directions do not impose two identical fine tunings.

## Magnetic/odd direction

If the source Hamiltonian has exact `Z2` symmetry and the preparation sets
`h=0`, the odd magnetic perturbation is forbidden by symmetry. The flow remains
inside the `Z2`-invariant subspace. This is structural selection by the source
and preparation contract.

If `h` is nonzero, the odd direction is admitted and relevant. The system is no
longer on the zero-field Ising critical trajectory.

## Thermal/even direction

`Z2` symmetry does not forbid the mass/temperature perturbation. The system
must be brought to its critical temperature or critical mass relation. Away
from it, the finite correlation length supplies an IR scale and the flow enters
an ordered or disordered phase.

The usual equilibrium Ising action therefore does not autonomously choose
criticality. A laboratory sets temperature; a numerical study tunes `beta`; a
theoretical critical limit imposes the corresponding condition. The critical
surface is physically accessible and highly informative, but it is not the
generic endpoint of the uncontrolled dynamics.

# 6. Preparation is not automatically smuggling

DU's anti-copy discipline must not turn into a ban on interventions. A
temperature setting is a physical operation with a calibrated ruler and a
declared target context. It is legitimate when the claim is conditional:

> Given this source system, symmetry sector, and independently specified
> critical preparation, the long-distance response belongs to the Ising
> universality class and satisfies the locked universal targets.

That claim does not pretend to explain why the system was prepared. It predicts
what follows from the preparation without copying the exponent values into the
control setting.

The same tuning is insufficient for a stronger claim:

> The source law itself makes the physical world critical without an external
> intervention or boundary condition.

For that claim, the tuned parameter is a relocated selector key. A distinct
mechanism would have to make the critical manifold dynamically attracting,
constrain the relevant coordinate, or explain the boundary/initial condition.

The correct criterion is therefore claim-relative:

| claim | status of critical preparation |
|---|---|
| conditional critical response | legitimate action-indexed antecedent |
| universal response across prepared microdomains | legitimate and tested by RG/finite-size scaling |
| autonomous emergence of criticality | unearned unless the source selects the relevant coordinates |
| unique theory of nature | not addressed |

This is the preparation analogue of DU's law-only/record-conditioned
attribution rule. A preparation may narrow the completion class, but it is not
record information and should not be credited to the source law.

# 7. What passport fields are actually derived

The audit decomposes the previously monolithic passport:

| field | strongest earned source | status |
|---|---|---|
| `d=3` | physical arena/lattice geometry | supplied in this chain |
| short-range locality | microscopic Hamiltonian | source-selected for the specimen |
| scalar order parameter | material/Hamiltonian and coarse-grained magnetization | physically motivated and source-relative, not unique for arbitrary matter |
| `Z2` symmetry | spin-flip-invariant Hamiltonian at `h=0` | source plus preparation selected |
| one-real-scalar effective family | block-spin/Landau-Ginzburg-Wilson representation | derived at effective-theory grade within assumptions |
| Wilson-Fisher basin | RG flow from admitted microscopic family | strongly supported; microdetails quotient out |
| critical-surface membership | `T=T_c`/mass tuning and `h=0` | prepared, not generic source outcome |
| two leading relevant sectors | linearized RG/CFT spectrum (`sigma`,`epsilon`) | established effective fixed-point structure |
| conformal-bootstrap island | crossing, unitarity, spectral/multiplicity passport | non-copy response selection from `HC-DU-215` |
| material realization map | comparison of source observables and universal scaling | empirical/model identification, not bootstrap-selected |
| writer/archive/access/provenance | apparatus dynamics | absent |

This factorization is the main knowledge gain. “The passport is unselected” was
true but too coarse. Several fields are selected by the microscopic source;
one is selected by the physical preparation; some emerge under the RG quotient;
and others remain arena or material-identification antecedents.

# 8. Proof-grade boundary

The combined RG, Monte Carlo, and bootstrap evidence for the 3D Ising
universality class is exceptionally strong. It is not one general rigorous
theorem proving that every admitted three-dimensional microscopic lattice
model converges to one unique continuum CFT with all stated data.

The sources used here span different grades:

- Kadanoff supplies the scaling/block-spin construction;
- Wilson supplies the RG/fixed-point mechanism and approximate 3D analysis;
- Wilson-Fisher supplies the controlled `epsilon` expansion near four
  dimensions;
- finite-size scaling supplies independent numerical universality evidence;
- conformal bootstrap supplies high-precision consistency islands conditional
  on the CFT passport.

Their convergence is a major scientific success. It should not be rewritten as
a theorem whose antecedent-to-conclusion chain no single source proves. The
honest return is
`LATTICE_TO_CFT_LINK_PHYSICALLY_STRONG_NOT_FULLY_RIGOROUS`.

# 9. Dynamic Unity consequence

The North-Star gate should now admit **source-plus-preparation selection**:

```text
source-owned law / Hamiltonian
  + independently fixed physical preparation and arena
  -> generated effective candidate class
  -> RG basin / universality quotient
  -> non-copy consistency-selected response
  -> complete material handoff
  -> record-conditioned reconstruction or finite remainder.
```

This is not a weakening. It prevents two opposite errors:

1. demanding that a source law explain the experimenter's temperature choice
   before receiving credit for a correct conditional prediction; and
2. pretending that a hand-tuned critical parameter proves autonomous
   self-selection by the source.

The required receipt must state which fields are law-selected, symmetry-fixed,
prepared, boundary-supplied, quotient-invariant, measured, or fitted.

# 10. What remains open and what not to do next

The wave does not produce a ready DU successor.

1. No current DU candidate supplies a source-owned physical action with a new
   non-copy response consequence beyond its established universality class.
2. The Ising chain remains a calibration of successful conditional selection,
   not a solution to record-interface selection.
3. The material order-parameter identification and laboratory preparation are
   independently warranted but not derived from an all-physics source.
4. The complete writer--archive--provenance--access--consumer--resource handoff
   is absent.
5. No record-conditioned target or finite physical remainder has been tested.

Do not pursue a generic “why criticality?” survey. That would mix equilibrium
critical points, quantum criticality, self-organized criticality, cosmological
criticality, and fitted scale invariance. Reopen the autonomous-regime branch
only with one source-pinned mechanism and a fixed relevant-coordinate
discriminator.

The higher-value next reopener is one concrete source-plus-preparation physical
packet that continues through a complete material instrument, allowing DU to
test whether the formed record adds target information beyond the law and
preparation alone.

# 11. Grade, novelty, and stop

**Earned:**

- a field-by-field decomposition of the Ising universality passport;
- exact separation of source-selected, preparation-selected, RG-quotiented,
  response-selected, and still-supplied structure;
- the critical stable-manifold/relevant-direction boundary;
- acceptance of declared physical preparation without crediting it to source
  dynamics;
- a sharper source-plus-preparation North-Star admission contract; and
- a concrete downstream reopener for a complete material packet.

**Not earned:**

- autonomous dynamical selection of criticality;
- a rigorous universal 3D lattice-to-CFT theorem;
- selection of spatial dimension or arbitrary material order parameters;
- a new critical exponent, CFT datum, or physical law;
- a selected detector, archive, observer, access, provenance, or finality
  mechanism; or
- a ready successor or Grade-5 discriminator.

**Stop:** do not simulate another Ising model, repeat the bootstrap, or survey
self-organized criticality. Reopen with one source-pinned physical packet that
includes independently fixed preparation, complete material handoff, and a
locked law-only versus record-conditioned target comparison.
