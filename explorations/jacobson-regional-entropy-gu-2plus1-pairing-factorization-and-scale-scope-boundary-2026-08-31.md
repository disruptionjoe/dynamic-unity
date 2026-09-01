---
title: "Jacobson regional entropy, GU 2+1 pairing, and the scale/scope factorization boundary"
status: completed_scoped_result
doc_type: primary_source_bridge_factorization_theorem_and_reopener
created: 2026-08-31
claim_id: HC-DU-210
run_id: RUN-20260831-jacobson-regional-entropy-pairing-bridge
work_id: CTS-A4-JACOBSON-REGIONAL-ENTROPY-PAIRING-BRIDGE
owner_repo: dynamic-unity
external_source_repo: gu-formalization
lanes:
  - lane_1
  - lane_5
  - lane_6
channels:
  - CH-SYN
  - CH-FORMAL
  - CH-COLLIDE
evidence_grade: 4
maximum_grade: "Scoped Grade 4 factorization and nonselection boundary; current GU transfer Grade 1; no new gravitational law, record selection, generation result, empirical excess, or prediction"
probe: ../tests/du_jacobson_regional_entropy_pairing_bridge_probe.py
artifact: ../tests/artifacts/du_jacobson_regional_entropy_pairing_bridge_result.json
---

# Jacobson regional entropy and the GU `2+1` pairing

## Executive result

The swing returns:

```text
JACOBSON_SUPPLIES_A_REGIONAL_GEOMETRIC_RESPONSE_PRINCIPLE
+ REGIONAL_RESPONSE_FACTORS_THROUGH_REGIONAL_STATE_DATA
+ EQUAL_REGIONAL_STATES_ERASE_MICROSCOPIC_PAIRING_PROVENANCE
+ CAUSAL_REGION_AND_ENERGY_SCALE_ARE_INDEPENDENT_AXES
+ CURRENT_GU_2PLUS1_PAIRING_REMOVES_A_PAIR_BELOW_THE_HIGH_SYMMETRY_REGIME
+ HIGHER_ENERGY_RECOUPLES_THE_PAIR_ON_THE_CURRENT_ROUTE
+ ORDINARY_EFT_ABSORBS_AN_UNFIXED_HEAVY_SECTOR_CONTRIBUTION
+ NO_DARK_MATTER_OR_RENDER_RADIUS_INFERENCE
+ ONE_SHARP_SOURCE_ACTION_REOPENER
+ NO_READY_SUCCESSOR
```

The proposed larger picture contains a real and useful join, but not the one
first suggested.

Jacobson's program says, schematically, that a small causal region's aggregate
matter/entanglement response and its boundary geometry obey an equilibrium or
constitutive relation. It therefore gives Dynamic Unity a principled way to
talk about **regional physical response**. It does not tell the region which
microscopic family paired with a mirror sector, select the algebra assigned to
the region, form a material record, or identify an observer.

The exact current GU `2+1` result is an **energy/symmetry-scale** statement. A
mirror-family-shaped block occurs once, and invariant pairing channels appear
as symmetry is lowered:

```text
Spin(10)       Pati--Salam       Standard Model
   0       ->       2        ->       11
```

Consequently, on this route a family/mirror pair can become massive and leave
the low-energy chiral spectrum below the relevant breaking scale. At higher
energy and restored `Spin(10)` symmetry, that pairing invariant vanishes and
the specific removal channel closes; absent another mass mechanism, the removed
degrees must reappear. Reading the current result as “the connection peels off
at high energy” reverses this route's direction.

The important structural correction is therefore:

> Causal-region inclusion and energy-scale reduction are two independent
> coordinates. Jacobson supplies no theorem identifying them. GU would need a
> source-owned law selecting their joint dependence.

That clarification prevents three tempting but unsupported moves: treating a
far galaxy as unrendered, treating dark matter as inaccessible information,
or treating the `2+1` pairing as the origin of regional causal horizons.

## 1. What Jacobson's program actually contributes

The primary-source chain is strong but scoped.

1. [Jacobson 1995](https://arxiv.org/abs/gr-qc/9504004) derives the Einstein
   equation as an equation of state by requiring the Clausius relation for all
   local Rindler horizons, with area entropy, energy flux, and Unruh
   temperature.
2. [Eling, Guedens, and Jacobson 2006](https://arxiv.org/abs/gr-qc/0602001)
   shows that curvature-dependent entropy generally requires a
   non-equilibrium entropy-production term. This is already a warning that one
   universal equilibrium scalar is not enough for arbitrary higher-curvature
   response.
3. [Jacobson 2015](https://arxiv.org/abs/1505.04753) relates stationarity of
   vacuum entanglement in small geodesic balls at fixed volume to the
   semiclassical Einstein equation for first-order conformal-field variations;
   the nonconformal extension carries an explicit conjectural step.
4. [Jacobson and Visser 2018](https://arxiv.org/abs/1812.01596) derives causal-
   diamond first-law and Smarr relations and recovers generalized-entropy
   stationarity for small diamonds.
5. [Jacobson and Visser 2019](https://arxiv.org/abs/1904.04843) formulates small-
   diamond spacetime equilibrium using free conformal energy and a negative-
   temperature interpretation.
6. [Jacobson and Visser 2023](https://arxiv.org/abs/2212.10608) defines a
   causal-diamond ensemble using an explicit York boundary and warns, by the
   construction itself, that the boundary defines the physical system rather
   than emerging for free.
7. [Banihashemi and Jacobson 2025](https://arxiv.org/abs/2411.00267) studies the
   formal gravitational partition function as a state count for a volume of
   space while emphasizing that its canonical and path-integral foundations
   remain unsettled.
8. [Banihashemi and Jacobson 2025](https://arxiv.org/abs/2405.10307) derives a
   lapse-contour prescription from constraint projection and integration order
   in the declared gravitational path integral. It reinforces
   constraint/boundary-first method; it does not select a GU region or entropy
   functional.

These are not claims that gravity is an ordinary entropic force or that
spacetime is rendered only when observed. The strongest common reading is:

> In the declared semiclassical regimes, Einstein dynamics behaves like a
> regional constitutive/equilibrium relation joining causal-boundary geometry
> to matter energy and entanglement data.

For local QFT algebras, ordinary density-matrix entropy is not generally the
right primitive. The reusable DU object remains Araki relative entropy and its
modular-energy/entanglement-first-law specialization, as already banked in
`HC-DU-117`, `HC-DU-134`, and `HC-DU-135`.

## 2. The typed joint object

Let:

- `Reg` be a poset of admitted causal regions or diamonds;
- `Scale` be a poset of energy/resolution scales;
- \(\mathcal A(D,\mu)\) be the observable algebra assigned to region \(D\) at
  scale \(\mu\);
- \(r_{D,\mu}(\omega)=\omega|_{\mathcal A(D,\mu)}\) be restriction of a global
  completion/state;
- \(\sigma_{D,\mu}\) be a declared reference state;
- \(J_{D,\mu}\) be the declared Jacobson-type first-order geometric response;
  and
- \(p\) be microscopic pairing provenance, such as which family-shaped block
  participated in the multiplicity-one mirror pairing.

The two orders do different jobs:

```text
larger causal region                       different RG/energy scale
D1 <= D2                                  mu_IR <= mu_UV
    |                                           |
    v                                           v
A(D1,mu) -> A(D2,mu)                  A(D,mu_IR) <- A(D,mu_UV)
scope / access inclusion                    effective reduction
```

The arrow orientation of an RG map depends on whether one uses observables,
states, or effective actions. That convention does not change the type
boundary: `Reg` and `Scale` form a product-indexed problem until a physical law
couples them.

Neither a causal-diamond assignment nor an RG threshold is yet a record. A DU
record additionally requires a selected formation process, carrier, retained
state, provenance semantics, access path, consumer/action envelope, and
resource horizon.

## 3. Regional-response factorization theorem

### Proposition 1 — provenance blindness

Fix \((D,\mu)\), its algebra, reference state, couplings, and response rule. If
the response is computed only from the regional state,

\[
J_{D,\mu}(\omega)
=F_{D,\mu}\!\left(r_{D,\mu}(\omega),\sigma_{D,\mu}\right),
\tag{1}
\]

then

\[
r_{D,\mu}(\omega_1)=r_{D,\mu}(\omega_2)
\quad\Longrightarrow\quad
J_{D,\mu}(\omega_1)=J_{D,\mu}(\omega_2).
\tag{2}
\]

Therefore no such response can reconstruct any target \(p\) that differs
between \(\omega_1\) and \(\omega_2\).

This is a direct factorization theorem, not new Jacobson or operator-algebra
mathematics. Its use here is to type what the proposed bridge can and cannot
carry.

### Exact smallest quantum witness

Take

\[
|\Phi_\pm\rangle
=\frac{|00\rangle\pm|11\rangle}{\sqrt2}.
\tag{3}
\]

They are orthogonal globally and an \(X\otimes X\) measurement returns opposite
values. Yet restriction to either qubit gives

\[
\rho_D^+=\rho_D^-=\frac{I}{2}.
\tag{4}
\]

Every fixed regional entropy, relative entropy, modular-energy expectation,
or regional response therefore agrees. The global phase/provenance remains a
finite physical remainder relative to that region.

The lesson is not that Jacobson fails. It is that a successful regional field
equation is not an inverse microscope for the global completion.

### Corollary 1 — stress-response provenance blindness

When the first-order response depends only on the admitted total stress tensor
or modular-energy variation, two microscopic sector histories producing the
same admitted variation yield the same geometric response. Einstein's equation
does not label which family or hidden sector supplied that stress.

If family-sensitive observables or couplings alter the regional state, they can
alter the response. But those additional couplings then do the selection work;
entropy equilibrium does not infer their provenance by itself.

## 4. The `2+1` consequence is an unlabelled orbit

The exact GU source packet supplies three identical chiral `16` family copies
and a `144` containing one mirror-family-shaped block with multiplicity one at
Pati--Salam. The consequence is subtractive:

\[
n_g\longmapsto n_g-1.
\tag{5}
\]

It does not derive \(n_g=3\), name which family is removed, or establish the
physical mass scale.

The finite control represents each choice as a normalized projector onto two
of three slots. The three projectors are microscopically distinct but have the
same spectrum

\[
\left\{\frac12,\frac12,0\right\}
\tag{6}
\]

and agree on the tested permutation-invariant response algebra. Thus entropy
and an unlabelled multiplicity-one condition select at most the orbit “one of
three is removed.” They do not select a family label. A source-owned
family-sensitive coupling, vacuum, boundary condition, or symmetry breaking is
required to do more.

This strengthens `HC-DU-209`: the `2+1` origin grading is independent not only
of luminous-half selection and record formation, but also of aggregate
regional entropic response.

## 5. Region and scale do not determine their coupling

### Proposition 2 — marginal-axis underdetermination

Separate regional and scale data do not determine a joint region--scale law.
The smallest exact witness is the pair

\[
P=\begin{pmatrix}1/2&0\\0&1/2\end{pmatrix},
\qquad
Q=\begin{pmatrix}0&1/2\\1/2&0\end{pmatrix}.
\tag{7}
\]

They have identical row marginals and identical column marginals, but opposite
region--scale parity. Therefore a regional net plus an RG flow does not select
how the two are matched.

The mathematical point is modest and load-bearing. To turn “larger causal
region” into “lower energy,” “higher access,” or “more global rendering,” a
theory must supply a bivariate law, not a verbal identification.

Known physics sometimes supplies such relations in special regimes—modular
Hamiltonians of symmetric regions, finite-size scaling, redshift, horizon
thermodynamics, or holographic UV/IR relations. Those are regime-specific
physical structures, not a universal equality of scope and scale.

## 6. The Wilsonian absorber

If a vectorlike family/mirror pair acquires a heavy mass \(M\), ordinary
[Appelquist--Carazzone decoupling](https://doi.org/10.1103/PhysRevD.11.2856)
and effective field theory integrate it out. Schematically,

\[
\Gamma_{\mathrm{eff}}
=\Gamma_{\mathrm{light}}
+\delta\Lambda\!\int\!\sqrt{-g}
+\delta(1/G)\!\int\!\sqrt{-g}\,R
+\sum_k\frac{c_k}{M^{d_k-4}}\!\int\!\sqrt{-g}\,\mathcal O_k.
\tag{8}
\]

Curved-spacetime decoupling can be technically subtle, but threshold shifts,
running couplings, and higher-curvature operators are incumbent physics. A
Jacobson-type response sees the resulting effective state and couplings. It
does not, without more structure, certify their microscopic origin.

Therefore the mere statement

> the paired sector changes generalized entropy, hence changes gravity

has no excess content. Almost any coupled quantum field changes the effective
action and entanglement structure.

A GU-specific result would require a source-derived mass, coupling, sign, and
coefficient that survive regulator and scheme changes and are not absorbed by
ordinary renormalization of \(G\), \(\Lambda\), matter couplings, or allowed
higher-curvature terms.

## 7. What the picture does and does not say about distant regions

The causal-diamond language supports a disciplined regional picture:

- an observer's operational algebra is limited by causal accessibility;
- larger regions can contain additional observables and completions;
- generalized/relative entropy can compare states without requiring a global
  density matrix for a type-III local algebra; and
- compatible regional assignments may glue into a larger description without
  granting any single observer total access.

It does **not** support an on-demand render interpretation. Light and other
signals received from distant galaxies are ordinary physical inputs to our
causal past. Events outside our causal past are inaccessible because of causal
structure, not because the theory has demonstrated that they were never
computed.

Nor does it support identifying dark matter with information that is rendered
elsewhere. Dark matter is inferred precisely because it has gravitational
effects on accessible baryonic matter, lensing, and large-scale structure. A
replacement hypothesis would need a quantitative stress/lensing/growth law
different from and at least as successful as the incumbent models. Nothing in
the regional entropy or `2+1` results supplies that law.

## 8. The surviving high-ceiling hypothesis

The coherent strengthened hypothesis is:

> A GU source action selects a bivariate net
> \(\mathcal A(D,\mu)\), its physical reference states and admissible
> restrictions; the multiplicity-one mirror pairing then produces a fixed,
> regulator-robust mixed regional/scale response whose generalized- or
> relative-entropy contribution is not reducible to ordinary EFT
> renormalization, and whose induced geometric response transfers without
> refit across at least two causal regions or regimes.

A useful diagnostic for a frozen source packet is a mixed response such as

\[
\Xi
=\Delta_D\Delta_{\log\mu}
S_{\mathrm{rel}}^{\mathcal A(D,\mu)}(\omega\Vert\sigma).
\tag{9}
\]

Nonzero \(\Xi\) alone is not new physics; ordinary QFT can produce
region-dependent threshold effects. The candidate earns excess content only
if GU fixes the algebra assignment, state/reference, pairing scale, observable,
coefficient, and incumbent-subtracted verdict before comparison.

### Exact reopener

Reopen this route only when the source packet supplies all of:

1. a stationary GU action and physical observed `3+1` sector;
2. a selected family of causal-region algebras or operational interfaces;
3. a selected reference state and generalized/relative-entropy functional;
4. the real-form-correct `2+1` pairing, mass scale, and coupling;
5. a fixed regional/scale matching law;
6. a regulator- and scheme-robust observable coefficient or sign; and
7. a no-refit comparison against GR plus curved-spacetime QFT/EFT.

Until then the Jacobson line is a powerful benchmark and type discipline, not
the missing DU physical selector.

## 9. Exact-control receipt

`du_jacobson_regional_entropy_pairing_bridge_probe.py` passes `16/16` exact
checks. It verifies:

- orthogonal global completions with identical regional state;
- equal regional response with a globally distinguishable target;
- three distinct family-removal embeddings with common entropy spectrum and
  invariant response;
- identical region and scale marginals with opposite mixed parity; and
- the imported `0 -> 2 -> 11` pairing-ladder direction.

These controls prove only the factorization and nonselection boundary in the
declared finite specimens. The primary-source and EFT audits carry the
physical scope. No simulation, fitted model, provider, external hardware, GU
write, or empirical claim was used.

## Disposition

`HC-DU-210` is banked as a scoped Grade-4 typed factorization/nonselection
result with mature mathematical absorbers. It corrects the larger story
without closing it:

- Jacobson gives the best current bridge from regional quantum state data to
  geometric response;
- GU `2+1` gives a possible sector threshold, presently at representation
  grade;
- their composition is coherent at Grade 1;
- their joint physical law remains unselected; and
- DU stays quiescent until the exact reopener is met.
