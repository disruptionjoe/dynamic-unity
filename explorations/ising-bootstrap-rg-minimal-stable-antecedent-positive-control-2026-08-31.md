---
title: "3D Ising bootstrap and RG minimal-stable-antecedent positive control"
status: banked_scoped_positive_control_and_selection_boundary
doc_type: primary_source_calibration_premise_ablation_and_portfolio_disposition
created: 2026-08-31
claim_id: HC-DU-215
run_id: RUN-20260831-ising-bootstrap-minimal-stable-antecedent-calibration
program_id: CCR-MINIMAL-PHYSICAL-ANTECEDENT-TO-FINITE-REMAINDER
owner_repo: dynamic-unity
evidence_grade: 4
maximum_evidence_grade: 4
---

# Executive result

The repaired gate from `HC-DU-214` is attainable in a scientifically important
success case, but only at the response-selection layer.

```text
MINIMAL_STABLE_ANTECEDENT_POSITIVE_CONTROL
GENERATED_INFINITE_CANDIDATE_CLASS
NON_COPY_CONSISTENCY_INTERSECTION
PREMISE_ABLATION_IS_LOAD_BEARING
NUMERICAL_ENRICHMENT_SHRINKS_THE_ISLAND
MICRODOMAIN_UNIVERSALITY_POSITIVE
LOCKED_TARGETS_TRANSFER_ACROSS_METHODS
SCOPED_MINIMALITY_ONLY
UNIVERSALITY_CLASS_PASSPORT_UNSELECTED
NO_MATERIAL_RECORD_HANDOFF
NO_READY_SUCCESSOR
```

The three-dimensional Ising conformal-bootstrap program begins with a compact
passport—dimension, conformal invariance, unitarity, `Z2` symmetry, leading odd
and even scalars, and a coarse relevant-spectrum condition. It then ranges over
an infinite class of possible spectra and OPE data. Crossing symmetry and
unitarity do not contain the Ising exponents as hidden input. Their intersection
first places the Ising theory at a corner, then closes a small mixed-correlator
island, and finally yields a precision island after an additional
single-operator/OPE-ratio constraint.

The resulting dimensions and critical exponents agree, without fitting those
numbers, with independent Monte Carlo studies of distinct lattice Hamiltonians
in the same universality class. Increasing the bootstrap functional cutoff
shrinks the island approximately self-similarly rather than sending it to an
unrelated location. These are strong positive controls for non-copy constraint
intersection, no-refit target sharpening, numerical stability, and
microdomain-insensitive prediction.

This does **not** show that the bootstrap selects why nature realizes the 3D
Ising universality class. The passport is supplied or empirically identified.
Nor is absolute inclusion-minimality proved: the sources test a specific
antecedent ladder, not every possible axiom set. The earned result is therefore
an **action- and class-indexed minimal-stability positive control**, not a unique
theory selector.

The deeper lesson for Dynamic Unity is constructive:

> A physical theory need not select inaccessible microphysics uniquely. A
> compact class passport plus independent consistency constraints can select a
> stable response island, while RG universality makes many microscopic
> realizations equivalent for the locked target.

That closes one ambiguity in the North-Star gate. DU should credit stable
response selection even when microdomain identity remains open. Its remaining
burdens are upstream and downstream: derive or physically select the applicable
passport, and separately select the material writer, archive, provenance,
access, consumer, and resource handoff before making any record claim.

The result is scoped Grade 4 as a source-grounded positive calibration and
selection/nonselection boundary. Its science is established conformal-bootstrap
and RG-universality work. No new critical exponent, CFT theorem, physical law,
record interface, or ready DU successor is claimed.

# 1. Frozen object, antecedent, and targets

## Candidate object

The candidate class is not a finite catalogue of lattice models. It is the
space of spectra and OPE coefficients for unitary three-dimensional CFTs with a
`Z2` global symmetry, subject to declared spectral conditions.

For the mixed-correlator system, the relevant external primaries are:

- `sigma`, the leading `Z2`-odd scalar; and
- `epsilon`, the leading `Z2`-even scalar.

The correlators are

```text
<sigma sigma sigma sigma>,
<sigma sigma epsilon epsilon>,
<epsilon epsilon epsilon epsilon>.
```

The compact antecedent ladder used in the sources is:

| layer | supplied content | role |
|---|---|---|
| geometry/type | three dimensions and conformal invariance | fixes the CFT object and conformal blocks |
| consistency | unitarity and crossing symmetry | supplies positivity and equality constraints |
| symmetry | global `Z2` | types odd and even operator sectors |
| spectral passport | `sigma` and `epsilon` are the only relevant odd/even scalars | identifies the Ising-like relevant-spectrum class |
| correlator family | three mixed/identical four-point functions | supplies independent crossing channels |
| precision refinement | one operator at the shared scaling dimension, scanned through the OPE-coefficient ratio | contracts the island further |

The locked targets were fixed before the source-to-source transfer comparison:

```text
Delta_sigma
Delta_epsilon
lambda_sigma_sigma_epsilon
lambda_epsilon_epsilon_epsilon
eta = 2 Delta_sigma - 1
nu  = 1 / (3 - Delta_epsilon).
```

Monte Carlo values were not admitted as bootstrap constraints in this audit.
Because the historical papers already knew earlier Ising estimates, this is not
retroactively called a preregistered prediction. It is a no-refit,
source-separated agreement test.

# 2. What the bootstrap actually selects

For one identical scalar, crossing has the schematic form

```text
sum_O lambda_phi_phi_O^2 F_{Delta,l}(u,v) = 0.
```

Unitarity makes the squared OPE coefficients nonnegative. A linear functional
that is positive on every admitted nonidentity block but normalized on the
identity proves that a proposed spectrum cannot satisfy the crossing equation.
The method therefore eliminates whole regions of spectral data without
enumerating a finite answer list.

Mixed correlators are stronger. Cross terms such as
`lambda_sigma_sigma_O lambda_epsilon_epsilon_O` do not have fixed sign, so the
crossing problem becomes a semidefinite program. Positivity is imposed on a
matrix of functionals while simultaneously satisfying all three correlator
crossing equations.

This is a genuine consistency intersection:

```text
unitary 3D Z2 CFT spectra
  intersect identical-correlator crossing
  intersect mixed-correlator crossing
  intersect relevant-spectrum gaps
  intersect single-operator/OPE-ratio consistency
  -> precision Ising island.
```

No input coordinate equals `0.5181489`, `1.412625`, `0.0362978`, or
`0.629971`. The numerical values arise from feasibility boundaries in the
crossing/positivity problem. This passes DU's non-copy selector control far more
strongly than a coefficient sign chosen to select one binary sector.

The primary progression is explicit:

1. El-Showk et al. found the 3D Ising model at a corner of the allowed
   single-correlator parameter space using crossing and unitarity
   ([primary paper](https://arxiv.org/abs/1203.6064)).
2. Kos, Poland, and Simmons-Duffin added the mixed correlator system and assumed
   `sigma` and `epsilon` were the only relevant scalars. They obtained a small
   closed region in `(Delta_sigma,Delta_epsilon)`
   ([primary paper](https://arxiv.org/abs/1406.4858)).
3. Kos et al. scanned the relative leading OPE coefficients, incorporating the
   information that there is a single operator at the given scaling dimension,
   and obtained a much smaller three-dimensional island and precise dimensions
   and OPE coefficients
   ([primary paper](https://arxiv.org/abs/1603.04436)).

This is not “consistency alone selects the Ising model.” It is “a compact,
typed antecedent plus increasingly complete independent consistency conditions
selects a narrow Ising response island.”

# 3. Premise-ablation ladder

The literature supplies a natural ablation sequence even though it does not
enumerate every logical subset of the passport.

| ablation or addition | observed effect | DU reading |
|---|---|---|
| identical `sigma` correlator only | corner/kink at the Ising location, not a tiny closed island | crossing and unitarity locate a special boundary but do not yet isolate it |
| add mixed `sigma`/`epsilon` correlators | small closed two-dimensional island | cross-channel consistency is load-bearing |
| require `sigma` and `epsilon` to be the only relevant scalars | island is interpreted as the Ising relevant-spectrum class | the gap passport is load-bearing and supplied |
| scan the leading OPE-coefficient ratio with a single-operator condition | much smaller three-dimensional precision island | multiplicity consistency adds real non-copy information |
| increase functional derivative cutoff `Lambda` | islands shrink approximately self-similarly | stronger numerical witness space sharpens rather than arbitrarily relocates the answer |

Two cautions prevent overclaiming.

First, “only two relevant scalars” is not derived by crossing in this chain. It
is a coarse empirical/universality-class identifier. Removing it changes the
candidate class; the published small-island claim does not survive unchanged.

Second, the sequence does not prove that this is the unique inclusion-minimal
axiom set among all possible descriptions. It proves scoped load-bearing
behavior for the tested ladder. The correct status is
`SCOPED_PREMISE_MINIMALITY_ONLY`.

# 4. Numerical-enrichment stability

The precision study represents functionals as combinations of derivatives at
the crossing-symmetric point. `Lambda` limits the maximum derivative order.
The authors used `Lambda=11,19,27,35,43` and report that the three-dimensional
island shrinks approximately self-similarly as `Lambda` increases.

This is an important but typed stability check:

- increasing `Lambda` enlarges the numerical certificate/search space;
- it does not enlarge the physical CFT candidate domain;
- exclusion power should therefore grow and the allowed island should nest or
  contract; and
- the reported contraction toward the same small region supports numerical
  stability of the response.

It is not a proof that the `Lambda -> infinity` island is a single point or that
the numerical implementation is mathematically complete. The 2014 paper also
uses rational approximations to conformal blocks and finitely many spins in
practice. These are controlled numerical approximations, not physical
truncations of the operator spectrum.

The positive result is consequently `NUMERICAL_ENRICHMENT_SHRINKS_THE_ISLAND`,
not `EXACT_CFT_UNIQUENESS_PROVED`.

# 5. Microdomain enlargement and RG universality

The Ising case also supplies the missing positive control for benign
microdomain enlargement. Hasenbusch studied both the spin-`1/2` Ising model
and the spin-1 Blume-Capel model at several values of its parameter `D` on the
simple cubic lattice. These are different microscopic Hamiltonians and even
different local spin alphabets:

```text
Ising:       s_x in {-1,+1}
Blume-Capel: s_x in {-1,0,+1}.
```

Within the continuous-transition region, they share the three-dimensional,
short-range, `Z2` universality class. The study obtains

```text
nu  = 0.63002(10)
eta = 0.03627(10)
```

and demonstrates that improved observables from the two models produce
consistent estimates after leading corrections to scaling are controlled
([primary paper](https://arxiv.org/abs/1004.4486)). The bootstrap precision
values are

```text
Delta_sigma   = 0.5181489(10)
Delta_epsilon = 1.412625(10)
eta           = 0.0362978(20)
nu            = 0.629971(4).
```

The Monte Carlo and bootstrap uncertainties are not identical and the older
Monte Carlo central values need not coincide digit for digit. The key test is
that independent microscopic models and a non-lattice CFT consistency method
converge on the same universal target region without the bootstrap fitting its
dimensions to those lattice results.

This is precisely the scientifically successful architecture identified by
`HC-DU-214`:

```text
many microphysical realizations
  -> RG universality quotient
  -> one effective CFT passport
  -> independent crossing/positivity intersection
  -> stable dimensionless response island.
```

Unique microdomain selection is unnecessary for these targets. Asking which
lattice Hamiltonian is “the” source would add a burden that the universal
critical response neither needs nor can answer.

# 6. Ruler audit

The selected targets are dimensionless scaling dimensions, OPE coefficients
under a declared normalization convention, and critical exponents. Their
dimensionlessness is an advantage: no meter stick or absolute energy scale is
needed to compare `eta` and `nu` across realizations.

It does not remove every ruler premise:

- the spatial dimension is supplied;
- short-range interaction and `Z2` order-parameter symmetry identify the
  universality class on the lattice side;
- operator normalization conventions matter for OPE coefficients;
- critical tuning and finite-size scaling define how lattice observables
  approach the fixed point; and
- mapping a material experiment into the class requires physical
  identification of its order parameter, range, and critical regime.

Thus the bootstrap supplies ruler-complete **dimensionless universal targets
within the class**, not a selector of the physical system/class map.

# 7. Exact selection boundary

Let `B_Ising` denote the declared CFT passport and `C(B_Ising)` its generated
class of spectra and OPE data. Let `Q(B_Ising)` be the subset satisfying the
frozen crossing and positivity conditions. Let `T` map a candidate to the
locked dimensions, OPE data, and derived exponents.

The sources support:

```text
T(Q(B_Ising)) is a small, numerically stable island,
```

and independent lattice realizations support constancy of the critical
exponent targets across a nontrivial microscopic family.

They do not support:

```text
nature selects B_Ising from all physical passports,
```

nor:

```text
the bootstrap selects one material system, detector, record, or observer.
```

This gives the clean typed theorem boundary:

> Stable target selection on a generated class does not imply physical
> selection of the antecedent passport that generated the class. RG
> universality can make microscopic identity irrelevant to the target without
> explaining why that universality class obtains in a particular material.

The first sentence is elementary specification logic. The second is standard
critical-phenomena physics. DU's contribution here is the explicit placement
of both inside its selection and reconstruction contract.

# 8. What this changes for Dynamic Unity

## What is now calibrated positively

`HC-DU-214`'s repaired gate is not merely aspirational. The Ising program
passes five important components:

1. a compact antecedent generates an infinite candidate class;
2. independent consistency constraints are non-copy selectors;
3. premise additions and ablations visibly control the response diameter;
4. numerical enrichment contracts toward a stable response region; and
5. RG universality makes the target robust across distinct microdomains.

Future DU work should not demand unique microscopic ontology when a declared
universality quotient is sufficient for the locked action/target class.

## What remains missing

The success case sharpens the actual DU frontier:

1. **Passport selection or derivation.** A deeper source theory would have to
   derive the dimension/symmetry/relevant-spectrum class, or a physical
   transition would have to identify it independently of the held-out target.
2. **Complete physical response.** The Ising targets are universal critical
   data, not the full response of a material instrument under a declared
   observer action class.
3. **Material handoff.** No writer, archive, causal provenance, access channel,
   consumer/controller, or resource horizon follows from the bootstrap island.
4. **Record reconstruction.** No formed record map or nonempty certified-record
   fibre is supplied, so no DU reconstruction or remainder verdict follows.
5. **New excess.** The values and consistency machinery are established physics;
   the audit does not create a new prediction.

The portfolio therefore remains `NO_READY_SUCCESSOR`. The positive control
improves the search contract rather than selecting a new active program.

# 9. Repaired next reopener

The next high-information candidate should look like this:

```text
source-owned compact passport
  -> generated physical class
  -> independent non-copy consistency/dynamic intersection
  -> declared universality quotient or benign-enlargement stability
  -> locked ruler-complete response island
  -> independently selected complete material handoff
  -> record-conditioned reconstruction or finite remainder.
```

A candidate can enter before the final handoff only as a response-selection
calibration. It becomes a DU flagship successor only when the handoff and
record-conditioned target test are physically present.

The cheapest future discriminator is not another selector survey. It is one
source-owned theory whose own dynamics derives an antecedent passport and then
inherits an Ising-like no-refit consistency island, or one physical apparatus
whose complete handoff is selected and whose record-conditioned response
strictly sharpens beyond the law-only image.

# 10. Grade, novelty, and stop

**Earned:**

- a real positive control for the action-indexed minimal-stable-antecedent
  criterion;
- non-copy consistency-intersection calibration on an infinite class;
- a premise-ablation ladder from corner to closed island to precision island;
- numerical-enrichment and microscopic-universality stability controls;
- a clean boundary between response selection, passport selection, and material
  record-handoff selection; and
- a correction that unique microdomain selection is not required for universal
  target prediction.

**Not earned:**

- a new conformal-bootstrap or RG theorem;
- exact uniqueness of the 3D Ising CFT;
- absolute inclusion-minimality of the passport;
- physical selection of the Ising universality class;
- a material detector, formed record, observer, provenance, or finality rule;
- a DU prediction or finite physical remainder; or
- a ready scientific successor.

**Stop:** do not reproduce the numerical bootstrap locally. Do not run another
abstract selector census. Reopen with a source-owned passport derivation, a
new locked target that the established consistency intersection predicts
without fitting, or a physically selected complete handoff that makes a record
reconstruction test possible.
