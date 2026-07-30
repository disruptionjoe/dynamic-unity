---
title: "Quantum-gravity conserved-controller gauge completion and provenance boundary"
status: completed_scoped_result
doc_type: primary_source_follow_on_collision_exact_gauge_completion_theorem_and_empirical_reopener
created: 2026-07-30
hypothesis_id: HC-DU-150
run_id: RUN-20260730-030816-conserved-controller-gauge-completion
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
  - CH-MODEL
  - CH-EMPIRICAL
maximum_grade: "Scoped Grade 4 conserved-source gauge-completion theorem, exact controller/probe exchange control, and primary-source apparatus boundary; Grade 5 only after a closed relational source--probe--controller probability retains frozen no-refit empirical excess."
probe: "../tests/du_conserved_controller_gauge_completion_probe.py"
artifact: "../tests/artifacts/du_conserved_controller_gauge_completion_result.json"
---

# Quantum-gravity conserved-controller gauge completion

## Executive result

The swing returned:

```text
LINEARIZED_GRAVITY_COUPLING_REQUIRES_A_CONSERVED_TOTAL_SOURCE_FOR_GAUGE_INVARIANCE
+ AN_EXTERNALLY_DRIVEN_PROBE_IS_AN_OPEN_SUBSYSTEM_WITH_STRESS_EXCHANGE
+ THE_CONTROLLER_OR_SUPPORT_MUST_CARRY_THE_COMPENSATING_DIVERGENCE
+ THE_PROBE_ONLY_COUPLING_CAN_SHIFT_UNDER_A_GAUGE_TRANSFORMATION
+ THE_COMPLETE_CONTROLLER_INCLUSIVE_COUPLING_CAN_REMAIN_GAUGE_INVARIANT
+ CONSERVATION_SELECTS_AN_AFFINE_COMPLETION_CLASS_NOT_A_UNIQUE_CONTROLLER
+ DIVERGENCE_FREE_COMPLETIONS_CAN_CHANGE_A_HELD_OUT_INTERACTION_PAIRING
+ THE_2025_PHASE_MODEL_DISPLAYS_EXTERNAL_POTENTIALS_BUT_NOT_THEIR_PHYSICAL_STRESS_COMPLETION
+ THE_2026_REFERENCE_FIELD_MODEL_SHOWS_HOW_PHYSICAL_APPARATUS_ENTERS_THE_CONSTRAINTS
+ IT_DOES_NOT_SUPPLY_OR_TRANSPORT_THE_2025_EXTERNAL_CONTROLLERS
+ THE_PHASE_REOPENER_NOW_REQUIRES_ONE_CLOSED_CONSERVED_RELATIONAL_APPARATUS_PACKET
+ NO_DU_PREDICTION_HARDWARE_PATH_OR_READY_SUCCESSOR
```

The first missing joint after `HC-DU-149` is physical, not merely
representational. A source or probe held on a prescribed trajectory by an
external potential is an open subsystem: force and momentum are exchanged
with whatever realizes that potential. Linearized gravitational gauge
invariance couples to the **total conserved stress-energy**, not to a
conveniently isolated driven particle.

This does not refute an effective gauge-fixed calculation. It establishes
the completion burden for interpreting its phase as a closed relational
observable.

For the standard linearized coupling,

\[
S_{\mathrm{int}}[h,T]
=-\frac{\kappa}{2}\int d^4x\,h_{\mu\nu}T^{\mu\nu},
\tag{1}
\]

the transformation

\[
\delta_\xi h_{\mu\nu}
=\partial_\mu\xi_\nu+\partial_\nu\xi_\mu
\tag{2}
\]

gives, after integration by parts,

\[
\delta_\xi S_{\mathrm{int}}
=\kappa\int d^4x\,\xi_\nu\partial_\mu T^{\mu\nu}.
\tag{3}
\]

For arbitrary compactly supported \(\xi\), the coupling is gauge invariant
exactly when the tested total source is conserved in the distributional
sense:

\[
\partial_\mu T_{\mathrm{total}}^{\mu\nu}=0.
\tag{4}
\]

If a controlled probe has

\[
\partial_\mu T_{\mathrm{probe}}^{\mu\nu}=f^\nu,
\tag{5}
\]

then a closed apparatus must contain controller/support stress satisfying

\[
\partial_\mu T_{\mathrm{controller}}^{\mu\nu}=-f^\nu.
\tag{6}
\]

The key second result is that Equation (6) does not select the controller.
If \(T_{\mathrm{controller}}^{(0)}\) is one solution, then

\[
T_{\mathrm{controller}}^{(0)}+K,
\qquad
\partial_\mu K^{\mu\nu}=0
\tag{7}
\]

is another. Conservation therefore selects an affine completion class. Two
members can both restore gauge invariance while differing in their
gravitational coupling, phase contribution, physical records, resource
requirements, or access structure.

The exact finite regression proves both parts by discrete summation by parts.
An open probe has gauge variation \(1172\). Two controllers each contribute
\(-1172\), so both completed sources have exactly zero variation. The
controllers differ by a nonzero divergence-free discrete Airy tensor. Both
are conserved, yet a held-out pairing is \(0\) for one completion and
\(-2749\) for the other.

The numbers are not physics constants. They are exact integer witnesses for
the theorem shape.

## 1. Why the controller becomes part of the source

### 1.1 The continuum identity

Assume \(T^{\mu\nu}\) is symmetric and boundary terms vanish. Substituting
Equation (2) into Equation (1) yields

\[
\begin{aligned}
\delta_\xi S_{\mathrm{int}}
&=-\frac{\kappa}{2}\int
  (\partial_\mu\xi_\nu+\partial_\nu\xi_\mu)T^{\mu\nu}\\
&=-\kappa\int(\partial_\mu\xi_\nu)T^{\mu\nu}\\
&=\kappa\int\xi_\nu\partial_\mu T^{\mu\nu}.
\end{aligned}
\tag{8}
\]

This is the linearized gravitational Ward/Noether identity. The new
mathematics is not Equation (8); it is standard. The useful Dynamic Unity
result is its collision with the externally controlled phase packet.

A prescribed potential can consistently describe an open subsystem. But the
stress-energy of that subsystem generally obeys a balance law with a force
density on the right, not autonomous conservation. The missing support can
be a trap, optical field, actuator, laboratory platform, power supply, clock,
or other controller. In a closed gravitational description, the exchange
must be represented somewhere in total stress-energy.

### 1.2 What gauge invariance does and does not buy

It buys:

- cancellation of the gauge variation after every stress-exchanging
  component is included;
- a conservation constraint on the total physical packet; and
- a principled reason to include controller provenance rather than treating
  it as irrelevant engineering detail.

It does not buy:

- a unique controller or support tensor;
- a unique preparation, trajectory, clock, measurement, or archive;
- independence of the phase from apparatus realization;
- cancellation of the proposed phase;
- a selected record interface; or
- empirical excess over rival physical laws.

This is why the result is not “add the controller and the problem disappears.”
The controller closes one invariance condition and opens a sharply typed
completion fibre.

## 2. Exact periodic-lattice theorem fixture

### 2.1 Discrete definitions

On a periodic \(4\times5\) lattice, let \(D_\mu\) be the forward difference
and \(B_\mu\) the backward difference. Define

\[
(\operatorname{div}T)_\nu
=\sum_\mu B_\mu T_{\mu\nu},
\qquad
(\delta_\xi h)_{\mu\nu}
=D_\mu\xi_\nu+D_\nu\xi_\mu.
\tag{9}
\]

The interaction is

\[
S_{\mathrm{int}}=-\frac12\sum h_{\mu\nu}T_{\mu\nu}.
\tag{10}
\]

Periodic summation by parts gives exactly

\[
\delta_\xi S_{\mathrm{int}}
=\sum\xi_\nu(\operatorname{div}T)_\nu.
\tag{11}
\]

No floating-point approximation is involved.

### 2.2 Open probe and controller repair

The fixture chooses a nonconserved symmetric integer probe tensor and sets

\[
\xi=\operatorname{div}T_{\mathrm{probe}}.
\tag{12}
\]

Therefore

\[
\delta_\xi S_{\mathrm{probe}}
=\|\operatorname{div}T_{\mathrm{probe}}\|^2
=1172>0.
\tag{13}
\]

The first controller is

\[
T_{\mathrm{controller}}^{(1)}=-T_{\mathrm{probe}},
\tag{14}
\]

which makes the first total source zero. The construction is deliberately
algebraic rather than a laboratory model: it isolates the exchange identity.

### 2.3 Nonunique conserved completion

For a periodic scalar \(\phi\), define the symmetric discrete Airy tensor

\[
K_{00}=B_1B_1\phi,\qquad
K_{11}=B_0B_0\phi,\qquad
K_{01}=K_{10}=-B_0B_1\phi.
\tag{15}
\]

The backward differences commute, so

\[
\operatorname{div}K=0
\tag{16}
\]

exactly. The second controller is

\[
T_{\mathrm{controller}}^{(2)}
=-T_{\mathrm{probe}}+K.
\tag{17}
\]

Both completed sources are conserved and have zero gauge variation.
Nevertheless, using \(K\) itself as a held-out symmetric test field gives

\[
S_{\mathrm{int}}[K,T_{\mathrm{total}}^{(1)}]=0,
\qquad
S_{\mathrm{int}}[K,T_{\mathrm{total}}^{(2)}]
=-\frac12\|K\|^2=-2749.
\tag{18}
\]

Thus conservation repairs gauge invariance without making the apparatus
completion unique or target-irrelevant.

### 2.4 Scope

The fixture is:

- an exact finite Ward-identity control;
- an exact affine-completion counterexample; and
- a positive controller-deletion control.

It is not:

- a discretization of the Chen--Giacomini experiment;
- a solution of the linearized Einstein constraints;
- a physically realistic trap or controller;
- a claim that the paper's total fringe is gauge dependent;
- a prediction of apparatus-dependent gravity; or
- evidence for Dynamic Unity.

## 3. Collision with the primary proposals

### 3.1 Chen and Giacomini 2025

Chen and Giacomini's
[*Quantum Effects in Gravity Beyond the Newton Potential from a Delocalized
Quantum Source*](https://doi.org/10.1103/hl1c-t8z9)
([full preprint](https://arxiv.org/abs/2402.10288)) explicitly permits the
source position and probe momentum to be controlled by external potentials.
It works in temporal gauge and assumes the test particle does not
gravitationally back-react: the gravity state is constrained by the source
alone, while the probe interacts with that state.

Those choices are clear and useful for isolating the proposed effect. In the
displayed model, however, the degrees of freedom realizing the external
potentials do not appear as dynamical stress-energy components of the
gravitational source. The model therefore does not yet display the
controller-inclusive completion demanded by Equations (4)--(7).

This is a statement about the inspected packet, not a claim of mathematical
inconsistency. A gauge-fixed effective theory can consistently treat external
forces as supplied backgrounds. The additional burden arises when promoting
one subsystem phase to a closed relational observable.

### 3.2 Chen and Giacomini 2026

The authors' follow-on
[*Quantum Reference Fields Transformations in Linearized Quantum
Gravity*](https://arxiv.org/abs/2606.09344) supplies a powerful positive
comparator:

- the total matter stress includes the ordinary source and both sets of
  four-scalar quantum reference fields;
- those fields enter the gravitational constraints and can back-react;
- the measurement outline introduces a physical probe and clock;
- the probe and clock enter the constraints like the system; and
- the measurement interaction is built from relational observables.

The paper also says that a complete relativistic relational measurement
theory remains future work, and it does not transport the 2025 phase or model
the external controllers which generate its source/probe potentials.

The 2026 construction therefore validates the **type** of the repair: physical
reference, clock, and measurement devices belong inside the constrained
system. It does not provide the missing controller completion automatically.

### 3.3 Operational QFT comparator

Yant and Blencowe's
[*An Operational Quantum Field Theoretic Model for Gravitationally Induced
Entanglement*](https://arxiv.org/abs/2503.20855) makes the matter field and
readout more operational and avoids external beam splitters or mirrors, but
still confines the scalar excitations using a spatially dependent external
harmonic potential. In its static approximation it retains the energy
density component and neglects selected gravitational back-action/decoherence
terms.

Christodoulou et al.'s
[*Locally Mediated Entanglement in Linearised Quantum
Gravity*](https://doi.org/10.1103/PhysRevLett.130.100202)
([preprint](https://arxiv.org/abs/2202.03368)) is a positive comparator for a
Lorentz-explicit path-integral derivation. It does not by itself select a
controller, record, or acquisition packet.

Together these sources show that controller completion is a general
operational-gravity issue, not a criticism unique to one calculation.

## 4. The new Dynamic Unity object

### 4.1 From apparatus nuisance to physical provenance

The controller is where three DU lines meet:

1. **Action envelope.** It physically realizes which counterfactual source
   and probe trajectories are possible.
2. **Conservation completion.** It carries the stress exchange required to
   make the gravitational source closed.
3. **Provenance.** Its dynamics records how the trajectory and measurement
   were produced, even when the reduced probe path looks identical.

This does not mean every controller automatically forms an observer-readable
record. It means that deleting it can delete physical information which
gravity couples to. The apparatus is therefore upstream of any claim that a
reduced source--probe phase reconstructs the complete physical process.

### 4.2 Apparatus-twin discriminator

The highest-information next theoretical specimen is:

```text
same effective source and probe trajectories
+ same reduced external potentials
+ same source--probe preparation and readout
+ two dynamically explicit conserved controller/support realizations
+ different divergence-free stress completion
```

Then calculate one complete relational joint probability with no parameter
refit.

Possible outcomes:

| Outcome | Meaning |
|---|---|
| Both completions give the same held-out phase surface | A controller-independence theorem may exist; the reduced observable earns stronger status |
| The completions give different total fringes in ordinary linearized gravity | The reduced phase is apparatus-relative; the full controller packet is required |
| Controller terms cancel the proposed excess | Close the empirical reopener at the completed order |
| A residual survives and no frozen classical/direct-action rival matches | Advance a model-class empirical discriminator, not yet unique field ontology |
| Equality requires retuning controller or nuisance parameters | Supplied-interface absorption |

This is a local analytic/theoretical reopener. It does not yet warrant
hardware because no closed pair of physical apparatus twins is specified.

## 5. Minimum closed relational apparatus packet

Before the phase can support a physical-remainder claim, freeze:

1. source, probe, controller/support, reference fields, clock, measurement
   device, and gravitational field;
2. one total conserved stress-energy or constraint-satisfying equivalent;
3. dynamical rather than merely prescribed control potentials;
4. one relational preparation and joint readout;
5. probe, controller, reference, and measurement back-reaction at the claimed
   perturbative order;
6. the complete same-order phase and truncation remainder;
7. two apparatus realizations or a theorem proving completion independence;
8. frozen Newtonian, semiclassical, direct-action, influence-functional, and
   nuisance rivals;
9. no-refit held-out source/probe/controller configurations; and
10. acquisition lineage if the proposal reaches hardware.

The target remains the complete relational outcome distribution. The
controller-inclusive decomposition can change internally without changing
the target, but that invariance must be shown rather than presumed.

## 6. Grade and disposition

### Earned

- a continuum conserved-source gauge-completion theorem;
- an exact discrete summation-by-parts fixture;
- an exact affine nonuniqueness theorem;
- a controller-deletion positive control;
- a primary-source apparatus boundary; and
- a sharper apparatus-twin empirical/theoretical reopener.

### Not earned

- novelty for the Ward identity or affine PDE solution space;
- proof that the Chen--Giacomini total phase is gauge dependent;
- a completed relativistic source--probe--controller calculation;
- a controller-selection law;
- an observed physical record;
- a Dynamic Unity prediction;
- a hardware path;
- new physics;
- a paper promotion; or
- a ready successor.

The result is scoped Grade 4 because it proves a necessity/nonselection
boundary and applies it to a frozen physical proposal. Its mathematical
components are substantially absorbed by standard gauge theory and
conservation. The potentially novel scientific object is the no-refit
apparatus-twin phase test, not the identity itself.

The repository remains quiescent. Reopen only with a dynamically explicit
closed controller packet, a theorem that removes controller dependence, or
an observed relational no-refit phase surface.

## 7. Sources and search boundary

Primary sources inspected:

- Lin-Qing Chen and Flaminia Giacomini,
  [*Quantum Effects in Gravity Beyond the Newton Potential from a
  Delocalized Quantum Source*](https://doi.org/10.1103/hl1c-t8z9),
  *Physical Review X* **15**, 031063 (2025);
  [full preprint](https://arxiv.org/abs/2402.10288).
- Lin-Qing Chen and Flaminia Giacomini,
  [*Quantum Reference Fields Transformations in Linearized Quantum
  Gravity*](https://arxiv.org/abs/2606.09344) (2026).
- Jackson Yant and Miles Blencowe,
  [*An Operational Quantum Field Theoretic Model for Gravitationally
  Induced Entanglement*](https://arxiv.org/abs/2503.20855) (2025;
  subsequently published in *Physical Review D*).
- Marios Christodoulou et al.,
  [*Locally Mediated Entanglement in Linearised Quantum
  Gravity*](https://doi.org/10.1103/PhysRevLett.130.100202),
  *Physical Review Letters* **130**, 100202 (2023);
  [preprint](https://arxiv.org/abs/2202.03368).

The search was bounded to the displayed models, their operational and
reference-field follow-ons, and targeted gauge/conservation/apparatus
queries available on 2026-07-30. No published closed
source--probe--controller transport of the 2025 phase was found. That is an
audit boundary, not proof of absence.
