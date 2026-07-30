---
title: "Christodoulou GIE apparatus-class selection and descent boundary"
status: completed_scoped_result
doc_type: primary_source_apparatus_passport_and_selected_supplied_boundary
created: 2026-07-30
hypothesis_id: HC-DU-152
run_id: RUN-20260730-062407-physical-apparatus-class-extraction
authority: "Joe direct chat: Go"
lanes:
  - lane_1
  - lane_2
  - lane_3
  - lane_4
  - lane_6
  - lane_7
channels:
  - CH-COLLIDE
  - CH-FORMAL
  - CH-SYN
maximum_grade: "Scoped Grade 4 source-interface nonselection and exact descent-readiness boundary; no Grade-5 remainder, prediction, apparatus correction, or empirical claim."
---

# Christodoulou GIE apparatus-class selection and descent boundary

## Executive return

Swing 1 returns:

```text
UNSELECTED_INTERFACE
+ OBSERVER_OR_CONTROLLER_SUPPLIED
+ CONDITIONAL_MATTER_FIELD_RESPONSE_WELL_DEFINED
+ TOTAL_STRESS_CONSERVATION_REQUIREMENT_EXPLICIT
+ APPARATUS_STRESS_AND_FIELD_ACKNOWLEDGED
+ HEAVY_AND_HOMOGENEOUS_SUFFICIENT_REGIME_STATED_QUALITATIVELY
+ NO_APPARATUS_DYNAMICS_VARIATION_CLASS_NORM_ERROR_OR_NO_REFIT_TRANSFER
+ HC_DU_151_PHYSICAL_COMPLETION_SPACE_REMAINS_UNDEFINED
+ SWING_2_NOT_ACTIVATED
+ SWING_6_NOT_ACTIVATED
+ NO_READY_SUCCESSOR
```

The result is narrow and useful.

Christodoulou et al.,
[*Locally Mediated Entanglement in Linearised Quantum
Gravity*](https://arxiv.org/abs/2202.03368), do **not** forget that a driven
particle is an open subsystem. Their supplement explicitly says that
arbitrary particle trajectories need not have conserved stress-energy and
that the apparatus stress \(\widetilde T^{\mu\nu}\) must be included so the
total source is conserved. It also identifies apparatus self-action and
particle--apparatus cross action.

The source then argues that a sufficiently massive apparatus with a
sufficiently homogeneous gravitational field recovers the particle-only
relative phase to the intended approximation. That is the strongest
absorber against a careless “missing apparatus” objection.

It is not, however, a selection of the physical controller-completion class
needed by `HC-DU-151`. The paper supplies no apparatus Lagrangian,
stress-energy family, reachable variation class, mass or homogeneity
tolerance, response norm, approximation-error bound, or held-out
configuration on which the same apparatus must transfer without refitting.
“Can be ensured by proper design” states an existence/design premise; it
does not define the set over which apparatus independence can be proved.

The exact conclusion is therefore:

> The paper supplies a physically motivated sufficient apparatus regime and
> a conditional matter--field calculation, but it does not make the
> controller-completion space in `HC-DU-151` a selected mathematical object.

This does not show that the proposed phase is wrong, apparatus dependent in
an implementation, or empirically distinguishable from a rival. It shows
where the source stops and what a complete descent proof would still have to
specify.

## 1. Frozen source passport

The audit uses the paper's displayed model and supplementary apparatus
discussion. It does not demand that an effective calculation model every
laboratory component. The question is only whether that calculation selects
the **class of apparatus completions** required for a controller-independent
phase claim.

| Object | Source status | Exact audit reading |
|---|---|---|
| Two spin-\(1/2\) masses | specified | Matter content and masses are model inputs. |
| Spin-dependent magnetic field \(B_z\) | supplied control | It prescribes branch-dependent planar motion. Its coupling to gravity and spin back-reaction are neglected. |
| Particle paths \(x_a^\sigma(t)\) | prescribed/approximated | Stationary-phase paths are determined conditional on the supplied magnetic control; gravitational back-reaction on them is neglected. |
| Linearized gravitational field | dynamically represented | Given the declared source, gauge treatment, and boundary conditions, the field is integrated and its on-shell action supplies branch phases. |
| Initial/final field and path boundary data | supplied | Common pure, separable boundaries and sufficient relaxation time are imposed. |
| Particle stress \(T_\sigma^{\mu\nu}\) | defined conditionally | It is tied to the prescribed point-particle histories. Arbitrary driven histories need not be conserved alone. |
| Total conservation | physically required | The supplement requires \(T_\sigma+\widetilde T_\sigma\) to be conserved. |
| Apparatus stress \(\widetilde T_\sigma^{\mu\nu}\) | required but not constructed | The source says it must account for the momentum exchange but gives no apparatus action or solution family. |
| Apparatus field \(\widetilde h_{\mu\nu}\) | acknowledged | Its self and particle cross terms are identified qualitatively. |
| Heavy-apparatus limit | assumed sufficient regime | Negligible branch-dependent apparatus motion is argued to suppress self-action differences; no mass/error inequality is given. |
| Homogeneous-apparatus-field limit | assumed sufficient regime | Approximate homogeneity over the particle paths is argued to suppress the cross-phase difference; no norm, region, or tolerance is given. |
| Apparatus design and calibration | supplied | The relevant regime is said to be obtainable by proper design rather than selected by the displayed dynamics. |
| Apparatus variation class | absent | There is no declared set of alternative controllers required to realize the same reduced paths. |
| Observer/readout boundary | supplied at this gate | Spin preparation and final spin measurement define the operational target; no physical observer-selection theorem is needed or supplied. |
| Resource/no-refit contract | absent | There is no fixed apparatus packet transferred across a held-out family with one error budget. |

The positive control matters. The paper does define a definite
**conditional response calculation** after its masses, prescribed histories,
field action, approximation, and boundary data have been supplied. This
audit is not treating every antecedent as a fatal omission. The failure is
localized to the object Swing 1 asked for: a physically selected apparatus
variation class.

## 2. The exact descent boundary

For branch \(\sigma\), conservation requires

\[
\partial_\mu\!\left(
T_\sigma^{\mu\nu}+\widetilde T_\sigma^{\mu\nu}
\right)=0.
\tag{1}
\]

As `HC-DU-150` established, one solution does not determine another. If
\(\widetilde T_\sigma^{(0)}\) is a completion, then an admissible
divergence-free addition remains possible before further physics is imposed.

For the quadratic response functional in `HC-DU-151`, a common completion
direction \(K\) changes the relative phase by

\[
\Delta I(K)-\Delta I(0)
=
\left\langle T_1-T_0,GK\right\rangle.
\tag{2}
\]

A quantitative apparatus-independence statement therefore needs a physical
set \(\mathcal K_{\mathrm{phys}}\), a response topology or norm, and a
tolerance \(\varepsilon\) such that

\[
\sup_{K\in\mathcal K_{\mathrm{phys}}}
\left|
\left\langle T_1-T_0,GK\right\rangle
\right|
\le \varepsilon
\tag{3}
\]

for the same apparatus contract across the declared held-out
configurations.

The source's qualitative conditions are good candidates for constructing
such a set:

\[
\text{large apparatus mass}
\quad+\quad
\text{small field variation over every branch path}.
\tag{4}
\]

But Equation (4) is not yet a mathematical domain. The source does not
define:

1. which apparatus degrees of freedom are admitted;
2. which initial and boundary conditions they obey;
3. which variations preserve the prescribed reduced paths;
4. how “heavy” and “homogeneous” are measured;
5. how those bounds control apparatus self and cross terms;
6. whether the bound is uniform over a held-out configuration family; or
7. which preparation, readout, calibration, and resources must remain fixed.

Consequently, the supremum in Equation (3) is not shown to vanish, fail, or
even be defined by the source. The correct result is
`UNSELECTED_INTERFACE`, not a nonzero phase correction.

## 3. Strongest absorber and cheapest kill

### Strongest absorber

The supplement already contains the physically correct repair shape:

- close the stress-energy packet with the apparatus;
- include the apparatus gravitational field;
- recognize self and cross contributions; and
- choose a massive, approximately homogeneous apparatus so those
  contributions become approximately branch independent.

Any future use of `HC-DU-150/151` must begin there. Repeating “the apparatus
was omitted” without this qualification would misrepresent the source.

### Cheapest kill

The preregistered kill nevertheless fires. The apparatus enters
existentially and through qualitative design conditions. No dynamics or
boundary-value problem selects the completion family, and no quantitative
uniform-error contract makes Equation (3) decidable.

This is a **source-interface boundary**, not a criticism that the effective
model is mathematically inconsistent. An effective particle-only
calculation may be valid inside a properly engineered regime. The source
does not itself provide the full packet needed to certify that regime for
Dynamic Unity's descent question.

## 4. Why neither prepared successor activates

### Swing 2 does not activate

Swing 2 requires `SELECTED_PHYSICAL_CLASS` or
`PARTIAL_PHYSICAL_TYPING`. Neither return was earned. There is no closed
apparatus class on which to compile the tangent space and response span.
Inventing one would replace source reconstruction with apparatus design.

### Swing 6 does not activate

Swing 6 requires an exact **physical** ambiguity or automorphism of an
already defined admissible interface class. `HC-DU-150/151` provide exact
abstract completion ambiguities, but this source does not select a physical
class on which a symmetry can act. Absence of a model is not itself a
physical automorphism. Promoting it would merely restate the prior theorem at
a looser type.

The campaign therefore returns `NO_READY_SUCCESSOR`.

## 5. What would reopen the line

The smallest legitimate reopener is one source-pinned apparatus packet that
supplies all of the following without post-hoc fitting:

1. a dynamical apparatus/controller action and total conserved stress;
2. preparation and boundary conditions;
3. the reachable apparatus family that realizes the prescribed branch
   histories;
4. a normed heavy/homogeneous approximation with an explicit error bound;
5. one fixed preparation, readout, calibration, resource, and gauge contract;
6. at least one held-out branch geometry or timing configuration; and
7. either a uniform proof of Equation (3) or two admitted apparatus
   realizations producing different complete relational probabilities.

The first six items would make the question well posed. The seventh would
decide descent or a lawful remainder.

No simulation is warranted before that packet exists. A locally invented
apparatus family could illustrate the algebra already proved by
`HC-DU-151`, but it could not tell Dynamic Unity which family physical law
selects.

## 6. Grade and claim boundary

Earned:

- a primary-source typed apparatus passport;
- a scoped Grade-4 source-interface nonselection result;
- a positive conditional-response control;
- a corrected absorber that credits the source's explicit apparatus
  discussion; and
- an exact reopener for physical descent.

Not earned:

- a claim that the paper's phase is wrong;
- a physical apparatus-dependent correction;
- a proof that no apparatus can satisfy the approximation;
- a selected observer or record interface;
- a same-experiment empirical remainder;
- a Dynamic Unity prediction;
- a hardware or collaboration requirement;
- a paper promotion; or
- activation of any later campaign swing.

## 7. Primary source

- Marios Christodoulou, Andrea Di Biagio, Markus Aspelmeyer, Časlav Brukner,
  Carlo Rovelli, and Richard Howl,
  [*Locally Mediated Entanglement in Linearised Quantum
  Gravity*](https://arxiv.org/abs/2202.03368), *Physical Review Letters* 130,
  100202 (2023), especially the model assumptions in the main text and the
  supplementary apparatus-contribution discussion.

## Final disposition

```text
claim_id: HC-DU-152
return: UNSELECTED_INTERFACE
observer_return: OBSERVER_OR_CONTROLLER_SUPPLIED
grade: scoped Grade 4
next: NO_READY_SUCCESSOR
hardware: not warranted
simulation: not warranted
prediction: none
paper_state: unchanged
```
