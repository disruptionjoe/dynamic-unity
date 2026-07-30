---
title: "Local-mediator nonclassicality, component attribution, and the gravity-witness boundary"
status: banked_scoped_result
doc_type: mediator_totality_component_attribution_theorem_exact_finite_counterexample_primary_source_collision_and_successor_disposition
created: 2026-07-30
claim_id: HC-DU-146
work_id: CCR-PHYSICAL-RECORD-INTERFACE-SELECTION
action_id: PRIS-10-MEDIATOR-COMPONENT-ATTRIBUTION-COLLISION
run_id: RUN-20260730-021341-mediator-component-attribution
lanes:
  - lane_1
  - lane_2
  - lane_3
  - lane_6
  - lane_7
channels:
  - CH-COLLIDE
  - CH-FORMAL
  - CH-SYN
evidence_grade: 4
maximum_grade: 4
---

# Local-mediator nonclassicality and component attribution

## Executive result

This swing corrects the strongest empirical reopener left by `HC-DU-139`.
The return is:

```text
CONDITIONAL_TOTAL_MEDIATOR_REMAINDER_SURVIVES
+ NAMED_COMPONENT_ATTRIBUTION_DOES_NOT_FOLLOW
+ SAME_COMPLETE_ENDPOINT_DIFFERENT_ACTIVE_MEDIATOR_EXACTLY
+ COMPONENT_PROVENANCE_OR_ISOLATING_INTERVENTION_REPAIRS_THE_FINITE_CASE
+ GRAVITY-ENTANGLEMENT CALCULATION AND CLASSIFICATION REMAIN CONTESTED
+ NO COMPLETED OBSERVED ACQUISITION PACKET FOUND
+ NO_READY_SUCCESSOR
```

Under the Marletto--Vedral constructor-information assumptions, entanglement
of two probes through one declared locally mediating system excludes an
admitted one-variable classical description of that **total mediator**. That
conditional theorem is not withdrawn.

The stronger physical cast does not follow:

> Entanglement observed at the probes does not by itself identify which named
> component of a composite mediation path carried the nonclassical degree.

An exact four-qubit control proves the distinction. Two implementations use
only probe--mediator gates. One routes the coherent path through component
\(G\); the other routes it through component \(Q\). Both produce the same
Bell pair, reset both candidate mediators to the same blank state, and
therefore have the same complete endpoint even if all four endpoint systems
are read. Only a component-tagged interaction history distinguishes them.

This is the Dynamic Unity point in its cleanest form. A present value can
certify that a nonclassical mediation event was possible in the total packet
without preserving the causal provenance needed to say which physical
component did the work.

The current gravity literature makes that distinction load-bearing rather
than academic. There are live, mutually incompatible analyses of whether a
classical gravitational field coupled to quantum matter can generate the
relevant entanglement, and there are models called classical gravity that do
generate gravitationally induced entanglement. These results differ in
mediator class, matter description, locality, tomography, stochastic
dynamics, binding, and allowed channels. Dynamic Unity must not adjudicate
that dispute by choosing a label.

`HC-DU-146` is a scoped Grade-4 attribution theorem, exact finite
counterexample, and current-literature boundary. The factorization theorem is
elementary and substantially absorbed by causal attribution, dilation
freedom, and DU's own mediator fibre. No new gravity result, constructor
theorem, empirical anomaly, physical remainder in nature, prediction, or new
physics is earned.

## 1. Three different targets

Let \(A\) and \(B\) be the probes and let the complete mediating packet be

\[
\mathsf M=(M_1,\ldots,M_k,\mathcal I,\mathcal B),
\]

where the component systems, allowed interactions \(\mathcal I\), and
boundary conditions \(\mathcal B\) are all part of the physical antecedent.
Keep three targets distinct.

### Probe entanglement

\[
E(c)=1
\]

means that the declared probe output is entangled in completion \(c\).

### Total-mediator nonclassicality

\[
N_{\rm tot}(c)=1
\]

means that the complete mediating system falls outside the declared
all-classical mediator class.

### Named-component nonclassicality

\[
N_j(c)=1
\]

means that the particular component \(M_j\)—for example, the gravitational
field rather than quantum matter, a direct channel, or a hidden boundary
mode—carries the nonclassical structure required by the process.

A mediator-witness theorem can establish, under its assumptions,

\[
E=1\Longrightarrow N_{\rm tot}=1.
\]

It establishes

\[
E=1\Longrightarrow N_j=1
\]

only when the physical packet independently establishes that \(M_j\) is the
complete exclusive mediator in the theorem's sense. That additional premise
is not word choice. It is a causal-factorization and acquisition claim.

## 2. Component-attribution factorization theorem

Let \(\mathcal C\) be a completion class. Let

\[
r:\mathcal C\to\mathcal R
\]

be the certified observer record, and let

\[
\tau_j:\mathcal C\to\{0,1\}
\]

state whether named component \(M_j\) carried the coherent mediation path.

### Theorem

A record-only named-component attribution exists exactly when

\[
\ker r\subseteq\ker\tau_j.
\]

Equivalently, there is a map

\[
h_j:\mathcal R\to\{0,1\}
\quad\text{with}\quad
\tau_j=h_j\circ r
\]

if and only if every pair of completions with the same certified record
agrees on the named active component.

### Proof

This is the ordinary factorization criterion. If
\(\tau_j=h_j\circ r\), equality of records implies equality of targets.
Conversely, if \(\tau_j\) is constant on every fibre of \(r\), define
\(h_j(r(c))=\tau_j(c)\); fibre constancy makes the definition well posed.
\(\square\)

The theorem is elementary. Its physical force comes from freezing the record
and target separately before asking whether an entanglement witness closes
the target.

## 3. Smallest exact endpoint counterexample

Use four qubits ordered as

\[
(A,B,G,Q).
\]

Prepare

\[
|+\rangle_A|0\rangle_B|0\rangle_G|0\rangle_Q.
\]

No direct \(A\)--\(B\) gate is allowed.

### Completion \(c_G\)

Route through \(G\):

\[
\operatorname{CNOT}_{A\to G},
\quad
\operatorname{CNOT}_{G\to B},
\quad
\operatorname{CNOT}_{A\to G}.
\]

After the first gate, \(A\) and \(G\) occupy a Bell state. After the third,

\[
|\Psi_{\rm final}\rangle
=|\Phi^+\rangle_{AB}|0\rangle_G|0\rangle_Q.
\]

### Completion \(c_Q\)

Route through \(Q\):

\[
\operatorname{CNOT}_{A\to Q},
\quad
\operatorname{CNOT}_{Q\to B},
\quad
\operatorname{CNOT}_{A\to Q}.
\]

The final state is exactly the same:

\[
|\Psi_{\rm final}\rangle
=|\Phi^+\rangle_{AB}|0\rangle_G|0\rangle_Q.
\]

Thus:

\[
r_{\rm endpoint}(c_G)=r_{\rm endpoint}(c_Q)
\]

even when the endpoint record includes every qubit, while

\[
\tau_G(c_G)=1,
\qquad
\tau_G(c_Q)=0.
\]

Therefore:

\[
\ker r_{\rm endpoint}\not\subseteq\ker\tau_G.
\]

The named-component target does not factor through the endpoint.

Both completions nevertheless agree on the coarser statement that the total
mediator complex carried one coherent path. The finite control therefore
does not refute a total-mediator witness. It proves that totality cannot be
silently narrowed to one component.

The regression is:

```bash
python3 tests/du_mediator_component_attribution_probe.py --write-artifact
```

It verifies:

- no direct probe gate;
- unit Bell fidelity at the active midpoint;
- the same Bell output at the probes;
- the same reset state of both mediators;
- the same complete endpoint; and
- distinct component-tagged interaction receipts.

## 4. Minimum repair

Define the provenance-bearing record

\[
r_{\rm prov}(c)
=
\bigl(r_{\rm endpoint}(c),\operatorname{receipt}(c)\bigr),
\]

where the receipt identifies the interacting component at each step.
Then:

\[
r_{\rm prov}(c_G)\neq r_{\rm prov}(c_Q).
\]

The finite target now factors.

In a physical experiment the analogous repair need not be a literal gate
log. It may be:

- a component-specific switch or intervention;
- an independently calibrated spectral or spatial signature;
- a timing/topology constraint that excludes every rival route;
- a bound on matter exchange, tunnelling, direct coupling, shared noise, and
  unwanted fields;
- a component-local readout that survives the interaction; or
- a theorem proving exclusive mediation for the complete admitted theory
  class.

Each repair adds physical information. It is not contained in endpoint
entanglement merely because the experimenter intended one component to be the
mediator.

## 5. Primary-source collision

### General constructor-information witness

Marletto and Vedral's
[*Witnessing non-classicality beyond quantum theory*](https://arxiv.org/abs/2003.07974)
states a theory-independent mediator result using constructor-information
premises. This supports the conditional total-mediator implication already
imported by `HC-DU-139`.

The theorem's mediation structure is load-bearing. If the physical mediator
is a composite of gravity, quantum matter, constraints, boundary modes, or an
unaccounted channel, then the theorem applies to that complete mediating
object unless an exclusive component factorization has independently been
proved.

### Nonlocal tomography changes what “classical-looking” means

Vidal, Marletto, Vedral, and Chiribella,
[*Bose--Marletto--Vedral experiment without observable spacetime
superpositions*](https://arxiv.org/abs/2506.21122), construct three toy
theories in which the gravitational mediator has a locally classical basis
and no observable spacetime superpositions, while non-locally-tomographic
coupling to quantum matter still permits entanglement. They classify the
mediator as nonclassical because of the composite coupling structure.

This reinforces the typing correction:

> Visible superposition of a named mediator variable is not the same target
> as nonclassicality of the total interaction theory.

### Models named classical gravity can predict entanglement

Trillo and Navascués,
[*The Diósi--Penrose model of classical gravity predicts gravitationally
induced entanglement*](https://arxiv.org/abs/2411.02287), derive parameter
regimes in which the DP dynamics entangles the mechanical degrees of freedom,
while later driving them toward separability. Their result does not satisfy
every premise of the constructor witness, and “classical” names a different
dynamical class. It nevertheless rules out the untyped inference that the
word classical alone fixes the no-entanglement side.

### The full-QFT classical-gravity claim is live and contested

Aziz and Howl,
[*Classical theories of gravity produce
entanglement*](https://arxiv.org/abs/2510.19714), argue that a classical
gravitational interaction combined with quantum-field-theoretic matter can
generate entanglement through virtual-matter propagation. Their proposed
effect would attribute the nonclassical channel to quantum matter rather
than a quantum gravitational field.

That calculation is not settled. The current primary-source dispute includes:

- Marletto and Vedral,
  [*Classical Gravity Cannot Mediate Entanglement by Local
  Means*](https://arxiv.org/abs/2510.19969), which argues that the claimed
  process does not establish local classical gravitational mediation;
- Diósi,
  [*No, classical gravity does not entangle quantized matter
  fields*](https://arxiv.org/abs/2511.00852), which gives a nonperturbative
  Heisenberg-picture objection;
- Xue and collaborators,
  [*Aziz and Howl's Gravity-Induced Entanglement Channel is Essentially
  Classical Mechanics*](https://arxiv.org/abs/2604.16276), which interprets
  the proposed channel as wave-packet propagation and challenges its
  physical size; and
- Gundhi, Infantino, and Bassi,
  [*Can classical theories of gravity produce
  entanglement?*](https://arxiv.org/abs/2604.19696), whose July 2026 revision
  argues that omitted transition amplitudes restore factorization in the
  frozen-particle-number regime.

Dynamic Unity therefore records:

```text
CONTESTED_PHYSICAL_CALCULATION
```

It does not use the Aziz--Howl result as an established counterexample, nor
the rebuttals as a universal no-go. The exact finite attribution theorem
survives either outcome.

### Experimental status

The 2025 multi-author white paper
[*A Spin-Based Pathway to Testing the Quantum Nature of
Gravity*](https://arxiv.org/abs/2509.01586) describes a proposed experimental
path and the consortium-scale work still required. A bounded search through
2026-07-30 found feasibility, parameter, decoherence, and theory studies, but
no completed gravitationally induced entanglement acquisition packet.

No empirical reopener is therefore present.

## 6. What an observed packet would have to contain

To support named-component attribution rather than only total-mediator
nonclassicality, a future packet must freeze:

1. joined probe outcomes, settings, trial identities, exclusions, and
   calibration records sufficient to certify entanglement;
2. the complete matter and field model in the admitted energy, distance, and
   time regime;
3. bounds on direct probe coupling, electromagnetic and Casimir channels,
   matter exchange or tunnelling, shared noise, preparation correlation, and
   postselection;
4. the locality and mediation topology;
5. the exact classical, quantum, post-quantum, stochastic, and
   non-locally-tomographic completion classes being excluded;
6. at least one component-isolating intervention or an independently proved
   exclusive-mediation theorem;
7. acquisition visibility, including rejected trials and every selection
   rule needed by the inference; and
8. a retained provenance map from the physical interaction to the certified
   claim.

This is demanding because the target is demanding. “The probes became
entangled” and “the gravitational field carried a nonclassical degree” are
different statements.

## 7. Relation to the North Star

This result clarifies what a finite physical remainder can and cannot be.

An observer record may force:

\[
\text{the admitted all-classical total mediator class is incomplete}
\]

without reconstructing:

\[
\text{which field, matter sector, boundary mode, or direct relation carries
the missing structure}.
\]

That is not a failure of the North Star. It is a typed answer:

- class exclusion can be record-supported;
- component ontology requires stronger causal provenance;
- endpoint finality can erase the mediator history that attribution needs;
- a direct-action and a field-mediated presentation may remain
  operationally dual until mediator-facing access is independently admitted;
  and
- regional or layered finality cannot manufacture the missing component
  identity after the interaction trace has been erased.

The result strengthens the case that certified causal records must include
formation and provenance, not merely final values.

## 8. Absorber and novelty audit

The mathematical parts are occupied by:

- ordinary factorization through fibres;
- causal attribution and latent-path nonidentifiability;
- Stinespring and process-realization freedom;
- quantum circuit uncomputation;
- constructor-information mediator witnesses;
- local-tomography and superselection theory; and
- `HC-DU-115/116/126`, which already prove mediator-elimination and
  source-response fibres.

Dynamic Unity's contribution is the joined distinction among:

1. probe entanglement;
2. total-mediator class exclusion;
3. named-component attribution;
4. endpoint versus provenance-bearing records; and
5. proposal, disputed calculation, and observed acquisition grades.

That integration is useful and exact. It is not a new entanglement theorem or
new gravity theory.

## 9. Portfolio disposition

### Bank

- `HC-DU-146` at scoped Grade 4;
- the component-attribution factorization theorem;
- the same-complete-endpoint/different-active-mediator witness;
- the minimum component-provenance or isolating-intervention repair;
- the conditional status of the total-mediator theorem; and
- the live disputed status of classical-gravity entanglement calculations.

### Correct

The `HC-DU-139` import should henceforth be read as:

> Under its full theorem packet, the witness excludes the declared
> all-classical **total mediator**. Attribution to a named gravitational field
> additionally requires an exclusive-mediation/factorization packet.

### Stop

- no generic mediator-nonclassicality survey;
- no local gravity simulation;
- no BMV hardware or provider proposal;
- no treating Aziz--Howl as settled;
- no treating a rebuttal as a universal theorem;
- no inference from observed entanglement to one named component without the
  attribution packet; and
- no replay of the finite circuit in larger Hilbert spaces.

### Reopen

Reopen with at least one of:

1. a completed observed acquisition packet meeting the eight fields above;
2. a theorem that makes one named component the exclusive mediator across a
   physically justified QFT or post-QFT completion class;
3. a component-isolating intervention with a no-refit prediction and
   independently bounded rival channels; or
4. a theory-specific quantitative signature that distinguishes the disputed
   completion classes rather than merely detecting entanglement.

Until then the successor status remains:

```text
NO_READY_SUCCESSOR
```

## 10. Validation boundary

```bash
python3 tests/du_mediator_component_attribution_probe.py --write-artifact
python3 tests/du_agent_orientation_contract_probe.py --write-artifact
```

Passing the first probe validates only the exact finite attribution
counterexample and positive provenance control. Passing the second validates
repository orientation. Neither validates a gravity model, constructor
theory, the Aziz--Howl calculation or its rebuttals, an observed BMV result,
exclusive mediation in nature, a record ontology, empirical excess, a
prediction, hardware need, or new physics.
