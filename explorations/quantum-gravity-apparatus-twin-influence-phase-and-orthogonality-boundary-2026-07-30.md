---
title: "Quantum-gravity apparatus-twin influence phase and orthogonality boundary"
status: completed_scoped_result
doc_type: primary_source_follow_on_collision_exact_gaussian_influence_phase_theorem_and_physical_reopener
created: 2026-07-30
hypothesis_id: HC-DU-151
run_id: RUN-20260730-053950-apparatus-twin-influence-phase
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
maximum_grade: "Scoped Grade 4 quadratic influence-phase criterion, exact conserved apparatus-twin counterexample and positive control, and primary-source apparatus boundary; Grade 5 only after a physical controller class and complete relational probability retain frozen no-refit excess."
probe: "../tests/du_apparatus_twin_influence_phase_probe.py"
artifact: "../tests/artifacts/du_apparatus_twin_influence_phase_result.json"
---

# Quantum-gravity apparatus-twin influence phase

## Executive result

The swing returned:

```text
A_CLOSED_LINEAR_GAUSSIAN_FIELD_PHASE_IS_QUADRATIC_IN_THE_TOTAL_BRANCH_SOURCE
+ A_COMMON_CONTROLLER_SELF_PHASE_CANCELS_FROM_THE_RELATIVE_PHASE
+ THE_SOURCE_CONTROLLER_CROSS_PHASE_NEED_NOT_CANCEL
+ CONSERVATION_AND_GAUGE_ADMISSIBILITY_DO_NOT_IMPLY_APPARATUS_INDEPENDENCE
+ A_COMMON_DIVERGENCE_FREE_COMPLETION_SHIFTS_THE_RELATIVE_PHASE_BY_ONE_RESPONSE_PAIRING
+ APPARATUS_INDEPENDENCE_IS_EQUIVALENT_TO_RESPONSE_ORTHOGONALITY_ON_THE_ADMITTED_COMPLETION_SPACE
+ AN_EXACT_NONZERO_ORTHOGONAL_COMPLETION_PRESERVES_THE_PHASE
+ CHRISTODOULOU_ET_AL_IDENTIFY_THE_MISSING_APPARATUS_AND_USE_HEAVY_HOMOGENEOUS_SUFFICIENT_APPROXIMATIONS
+ OPERATIONAL_GIE_MODELS_RETAIN_EXTERNAL_FORCE_OR_TRAP_INTERFACES
+ THE_MATHEMATICS_IS_ABSORBED_BY_GAUSSIAN_INFLUENCE_FUNCTIONALS
+ THE_PHYSICAL_REOPENER_IS_SELECTION_PLUS_ORTHOGONALITY_OR_A_NO_REFIT_VIOLATION
+ NO_PUBLISHED_PHASE_VERDICT_DU_PREDICTION_HARDWARE_PATH_OR_READY_SUCCESSOR
```

`HC-DU-150` showed that an externally driven probe is an open subsystem:
linearized gravitational gauge completion requires the controller or support
to carry the missing stress-energy exchange. It also showed that conservation
selects only an affine class of controllers.

This swing asks the next question: does the **full field-integrated phase**
become independent of that class?

In general, no. Let \(G\) be a symmetric response kernel on an admitted
conserved-source space and define the Gaussian on-shell or influence phase

\[
I(T)=\frac{1}{2}\langle T,GT\rangle.
\tag{1}
\]

For two branches with total sources \(T_0,T_1\), add the same conserved
controller completion \(K\) to both. The relative phase is

\[
\Delta I(K)=I(T_1+K)-I(T_0+K).
\tag{2}
\]

Direct expansion gives

\[
\Delta I(K)-\Delta I(0)
=\langle T_1-T_0,GK\rangle.
\tag{3}
\]

The controller self-phase

\[
\frac12\langle K,GK\rangle
\]

cancels between branches. The cross phase with the branch-difference source
does not generally cancel.

Therefore the phase is constant on a linear admitted completion space
\(\mathcal K\) exactly when

\[
\langle T_1-T_0,GK\rangle=0
\qquad\text{for every }K\in\mathcal K.
\tag{4}
\]

Equation (4), not conservation alone, is the exact apparatus-independence
condition.

The exact finite control realizes both sides. On a periodic rational lattice:

- both reduced probe branches are nonconserved open subsystems;
- two controller families repair the same probe divergences;
- every completed branch source is conserved;
- a common divergence-free controller addition changes the relative phase
  from \(1967351/4785\) to \(14198501/23925\);
- the exact shift is \(4361746/23925\), equal to the response cross pairing;
- the common controller self-phase cancels;
- a constructed nonzero response-orthogonal completion leaves the relative
  phase exactly unchanged; and
- identical branch totals give zero relative phase before and after the same
  completion.

The numbers are exact theorem witnesses, not physical constants.

The primary-source audit also corrects the implied novelty boundary.
Christodoulou et al. already state that arbitrary driven point-particle
trajectories need apparatus stress to make total energy-momentum conserved.
They then argue that the particle-only phase is recovered when the apparatus
is sufficiently heavy and its field is sufficiently homogeneous over the
particle paths. In the present language, those are physical sufficient
conditions intended to suppress the two controller terms:

- heaviness makes the apparatus self-action approximately branch
  independent; and
- field homogeneity makes its cross action approximately path independent.

That is closely aligned with Equation (4), but it is an approximation for a
declared apparatus regime, not a theorem that conservation forces
completion-independence for every controller.

The mathematical result is substantially absorbed by ordinary Gaussian
field integration and influence-functional algebra. The useful Dynamic Unity
advance is a typed physical burden:

> A reduced gravitational phase is apparatus-independent only after the
> physical theory selects the admitted controller class and the
> branch-difference source is response-orthogonal to that entire class, or a
> complete no-refit calculation shows the same relational outcome law
> directly.

No published phase is refuted or corrected. No physical apparatus twin,
observed packet, Dynamic Unity prediction, hardware path, or ready successor
is earned.

## 1. The exact theorem

### 1.1 Common completion

Let \(V\) be a real vector space of admissible total sources, let
\(\langle\cdot,\cdot\rangle\) be a nondegenerate pairing, and let
\(G:V\to V\) be self-adjoint on the tested domain. The quadratic functional
is Equation (1).

For one common addition \(K\),

\[
\begin{aligned}
I(T_a+K)
&=\frac12\langle T_a+K,G(T_a+K)\rangle\\
&=I(T_a)+\langle T_a,GK\rangle
  +\frac12\langle K,GK\rangle.
\end{aligned}
\tag{5}
\]

Subtracting branch \(0\) from branch \(1\) cancels the last term and proves
Equation (3).

This separates two statements that are easy to conflate:

1. **Common apparatus self-action cancels.**
2. **The apparatus has no branch-relative effect.**

The first follows algebraically. The second additionally requires Equation
(4).

### 1.2 Branch-dependent completions

For different additions \(K_0,K_1\),

\[
\begin{aligned}
\Delta I(K_0,K_1)-\Delta I(0,0)
={}&\langle T_1,GK_1\rangle
 +\frac12\langle K_1,GK_1\rangle\\
&-\langle T_0,GK_0\rangle
 -\frac12\langle K_0,GK_0\rangle.
\end{aligned}
\tag{6}
\]

There is then no generic self-phase cancellation either. This is physically
important because a momentum-balancing apparatus can recoil differently on
different interferometer branches.

Equation (3) is therefore the favorable case: it gives the controller the
same additional internal conserved structure in both branches. Even that
case needs response orthogonality.

### 1.3 Necessary and sufficient condition

Let \(\mathcal K\) be the linear space of common completion directions
admitted by the frozen physical controller contract. Then

\[
\Delta I(K)=\Delta I(0)\quad\forall K\in\mathcal K
\tag{7}
\]

if and only if Equation (4) holds.

Equivalently,

\[
G(T_1-T_0)\in\mathcal K^\perp
\tag{8}
\]

when \(G\) is self-adjoint.

This condition can arise for different reasons:

- symmetry may make the controller field constant over the branch
  difference;
- separation of support may make the relevant response pairing vanish;
- a physical constraint may exclude every nonorthogonal completion;
- a decoupling or large-mass limit may suppress the cross pairing;
- a relational quotient may identify only the orthogonal target; or
- the complete apparatus dynamics may make the branch-dependent terms
  cancel without decomposing them into a common \(K\).

These are different physical mechanisms. They must not be collapsed into
“the apparatus is irrelevant.”

## 2. Conservation is necessary but not sufficient

Let

\[
\partial_\mu T_a^{\mu\nu}=0,
\qquad
\partial_\mu K^{\mu\nu}=0.
\tag{9}
\]

Then every \(T_a+K\) remains conserved. For a gauge-compatible linear
response, this is enough to remove pure-gauge dependence from the source
coupling. It does not impose Equation (4).

The two requirements live at different types:

| Requirement | Mathematical form | What it buys |
|---|---|---|
| Gauge admissibility | \(\partial_\mu T^{\mu\nu}=0\) | Pure-gauge directions decouple from the complete source |
| Apparatus independence | \(\langle T_1-T_0,GK\rangle=0\) on \(\mathcal K\) | The relative phase factors through the reduced branch description |
| Physical selection | dynamics, boundary conditions, state, controller, and resources select \(\mathcal K\) | The quotient is about one physical experiment rather than an arbitrary class |
| Empirical closure | one complete preparation-to-readout probability survives no-refit controls | A creditable observable rather than an internal phase allocation |

Gauge invariance can hold for two completions while the completed physical
sources and their relational phases differ. This is not a gauge ambiguity.
It is ordinary physical underdetermination from an incomplete apparatus
contract.

## 3. Exact finite fixture

### 3.1 Arena

The executable uses a \(4\times5\) periodic lattice with rational arithmetic.
The objects are:

- symmetric \(2\times2\) tensor fields;
- a backward-difference divergence;
- divergence-free discrete Airy tensors;
- the symmetric nonlocal response

\[
G=(I+L_{\rm graph})^{-1}
\tag{10}
\]

applied componentwise; and
- the phase in Equation (1).

Because the periodic response commutes with lattice translations and
differences, it maps the conserved test sources to conserved responses.

This is not a Lorentzian graviton propagator. Its job is to decide the
universal implication

\[
\text{conserved completion}
\Longrightarrow
\text{completion-independent quadratic phase}.
\tag{11}
\]

One exact counterexample is enough to refute Equation (11).

### 3.2 Apparatus twins

For branch \(a\), choose a nonconserved reduced probe \(P_a\) and a conserved
total source \(T_a\). Controller family A is

\[
C_a^{A}=T_a-P_a.
\tag{12}
\]

Controller family B adds one common divergence-free \(K\):

\[
C_a^{B}=C_a^{A}+K.
\tag{13}
\]

The reduced probes remain exactly \(P_a\), while the total sources become

\[
T_a^{B}=T_a+K.
\tag{14}
\]

Both controller families carry the opposite divergence to their probes.
Both total-source families are conserved.

The phase values are:

| Quantity | Exact value |
|---|---:|
| Relative phase, family A | \(1967351/4785\) |
| Relative phase, family B | \(14198501/23925\) |
| Family-B minus family-A shift | \(4361746/23925\) |
| Response pairing \(\langle T_1-T_0,GK\rangle\) | \(4361746/23925\) |
| Common completion self-phase | \(23940214/23925\) |

The equal shift and response pairing prove Equation (3). The nonzero
self-phase appears in both branches and cancels from the relative phase.

### 3.3 Orthogonal positive control

The probe constructs two nonzero divergence-free completion directions
\(K_1,K_2\). If

\[
a=\langle T_1-T_0,GK_1\rangle,
\qquad
b=\langle T_1-T_0,GK_2\rangle,
\tag{15}
\]

then

\[
K_\perp=bK_1-aK_2
\tag{16}
\]

is response-orthogonal to the branch difference. It is nonzero in the frozen
fixture and satisfies

\[
\langle T_1-T_0,GK_\perp\rangle=0.
\tag{17}
\]

Adding \(K_\perp\) leaves the relative phase exactly
\(1967351/4785\). Thus the executable does not merely show that controllers
can matter; it verifies the exact condition under which they do not.

All 14 preregistered assertions pass.

## 4. Primary-source collision

### 4.1 Christodoulou et al.: the missing apparatus is explicit

Christodoulou et al.,
[*Locally Mediated Entanglement in Linearised Quantum
Gravity*](https://arxiv.org/abs/2202.03368), derive branch phases as
on-shell actions in Lorentz-explicit linearized gravity.

Their setup uses spin-dependent magnetic fields to drive prescribed particle
paths. The paper states that the coupling of the magnetic field to gravity,
spin back-reaction on that field, and gravitational back-reaction on the
particle paths are neglected.

More importantly for this gate, the supplementary derivation explicitly
notes:

1. arbitrary point-particle trajectories need not have conserved
   stress-energy;
2. a linearized Einstein solution therefore requires the apparatus stress
   \(\widetilde T^{\mu\nu}\) so that
   \(T^{\mu\nu}+\widetilde T^{\mu\nu}\) is conserved;
3. the apparatus contributes its own field and creates particle--apparatus
   cross action plus apparatus self-action;
4. a sufficiently heavy apparatus moves negligibly, making its self-action
   approximately common across branches; and
5. a sufficiently homogeneous apparatus field makes the cross term
   approximately common over the particle paths.

This is the closest located physical absorber. It does not ignore the
controller issue; it states a sufficient approximation for suppressing it.

In the present notation, the last two steps aim to enforce Equation (4) for
the declared experiment. The paper does not prove that every conserved
apparatus completion satisfies it, nor does it select all controller
stress-energy from conservation alone.

This corrects the previous audit's emphasis. The open item is not “did the
literature remember the apparatus?” At least this source did. The open item
is whether a concrete implementation establishes the heavy/homogeneous
approximation or another exact completion-independence mechanism at the
accuracy claimed.

### 4.2 Operational and exact matter-dynamics comparators

Braccini, Serafini, and Bose,
[*Mass-Independent Gravitationally Induced
Entanglement*](https://arxiv.org/abs/2602.19306), analytically solve two
interacting Stern--Gerlach interferometers with operator-valued qubit forces,
traps, recombination, open dynamics, and realistic noise. This is a strong
positive comparator for treating the massive degrees of freedom
dynamically. In the displayed Hamiltonian, however, the trap and qubit force
remain supplied control terms; their stress-energy is not promoted into the
gravitational source packet. It does not decide Equation (4).

Yant and Blencowe,
[*An Operational Quantum Field Theoretic Model for Gravitationally Induced
Entanglement*](https://arxiv.org/abs/2503.20855), model each mass as a scalar-
field excitation in an external harmonic potential and construct a field
observable for fringe visibility. This improves the operational target but
still leaves the external potential as a supplied apparatus interface.

Chen and Giacomini's
[*Quantum Reference Fields Transformations in Linearized Quantum
Gravity*](https://arxiv.org/abs/2606.09344) supplies a different positive
architecture: reference fields, clock, and measurement device are physical
and enter the constraints. It does not transport a declared
source--probe--controller phase calculation into a selected controller class.

Mougiakakos, Riva, and Vernizzi,
[*Gravitational Bremsstrahlung in the Post-Minkowskian Effective Field
Theory*](https://arxiv.org/abs/2102.08339), provide a useful field-theory
positive control: interacting two-body dynamics can be organized into a
conserved stress-energy tensor that couples linearly to gravity. That does
not supply an interferometer controller or prove completion independence.

### 4.3 Mathematics absorber

Integrating out a Gaussian field gives a quadratic functional of its source.
The expansion in Equations (3)--(6) is standard Feynman--Vernon/on-shell-
action algebra. Ward identities impose source conservation. Neither
mathematical ingredient is novel.

Dynamic Unity's scoped contribution is the typed conjunction:

1. controller completion is required by the physical conservation law;
2. that completion is nonunique under conservation alone;
3. the full quadratic phase descends to the reduced probe quotient if and
   only if a response-orthogonality condition holds on the **physically
   admitted** completion directions; and
4. a claim of phase invariance must state what selects that direction space.

This is a reusable audit theorem, not new gravitational dynamics.

## 5. What this changes

The apparatus-twin reopener is partly consumed. Dynamic Unity now has:

- an exact pair of conserved algebraic apparatus twins;
- an exact same-probe/different-relative-phase witness;
- an exact nonzero same-probe/same-relative-phase control;
- the necessary-and-sufficient linear completion criterion; and
- the closest primary-source sufficient approximation.

The remaining work is no longer “add a controller and see what happens.” It
is one of two sharply different physical routes:

### Route A — prove descent

Supply one physical controller model whose dynamics, state, boundary
conditions, and resources select \(\mathcal K\), then prove or bound

\[
\sup_{K\in\mathcal K}
\left|\langle T_1-T_0,GK\rangle\right|
\tag{18}
\]

below the frozen experimental tolerance without refitting the controller
between held-out configurations.

### Route B — exhibit a first leak

Construct two dynamically explicit controller realizations that:

- generate the same reduced source/probe paths at the declared accuracy;
- satisfy total conservation and the same boundary conditions;
- remain within one physical resource and apparatus class;
- differ by an admitted nonorthogonal completion direction; and
- produce different complete relational readout probabilities after every
  nuisance and lineage control.

Route A would strengthen the ordinary phase proposal. Route B would show
that the reduced phase is apparatus-relative. Neither outcome is a Dynamic
Unity prediction by itself.

## 6. Grade and disposition

### Earned

- the exact common-completion phase-shift theorem;
- the necessary-and-sufficient response-orthogonality criterion;
- an exact conserved same-probe/different-phase counterexample;
- an exact nonzero orthogonal-completion positive control;
- a corrected primary-source apparatus boundary; and
- a finite physical descent/first-leak reopener.

### Not earned

- mathematical novelty for Gaussian field integration;
- a realistic controller or Lorentzian gravitational solution;
- proof that a published gravitational phase is apparatus dependent;
- violation of the heavy/homogeneous approximation;
- a controller-selection law;
- an observed physical record;
- a Dynamic Unity prediction;
- a hardware path;
- new physics;
- a paper promotion; or
- a ready successor.

The result is scoped Grade 4 because it proves an exact factorization
criterion and counterexample and locates its physical absorber. Its
mathematics is standard. The unabsorbed object is a selected physical
controller class with either uniform response orthogonality or one no-refit
relational violation.

The repository remains quiescent.

## 7. Search boundary

Primary sources inspected:

- Marios Christodoulou et al.,
  [*Locally Mediated Entanglement in Linearised Quantum
  Gravity*](https://arxiv.org/abs/2202.03368),
  *Physical Review Letters* **130**, 100202 (2023).
- Lorenzo Braccini, Alessio Serafini, and Sougato Bose,
  [*Mass-Independent Gravitationally Induced
  Entanglement*](https://arxiv.org/abs/2602.19306) (2026).
- Jackson Yant and Miles Blencowe,
  [*An Operational Quantum Field Theoretic Model for Gravitationally
  Induced Entanglement*](https://arxiv.org/abs/2503.20855) (2025).
- Lin-Qing Chen and Flaminia Giacomini,
  [*Quantum Reference Fields Transformations in Linearized Quantum
  Gravity*](https://arxiv.org/abs/2606.09344) (2026).
- Stavros Mougiakakos, Massimiliano Maria Riva, and Filippo Vernizzi,
  [*Gravitational Bremsstrahlung in the Post-Minkowskian Effective Field
  Theory*](https://arxiv.org/abs/2102.08339) (2021).
- Yui Kuramochi and Hiroyasu Tajima,
  [*Wigner--Araki--Yanase theorem for continuous and unbounded conserved
  observables*](https://arxiv.org/abs/2208.13494) (2022).

The search was bounded to Gaussian/on-shell linearized-gravity phases,
conserved apparatus completion, Stern--Gerlach/trap dynamics, relational
reference fields, and conservation-limited measurement. No source was found
that selects a complete physical controller class and proves Equation (4)
uniformly for the current DU target. That is an audit boundary, not proof of
absence.
