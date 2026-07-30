---
title: "Probe-process mediator diagnostics, symmetry identifiability, and component attribution"
status: banked_scoped_result
doc_type: all_probe_process_component_nonidentifiability_theorem_exact_symmetry_control_diagnostic_ladder_primary_source_collision_and_successor_disposition
created: 2026-07-30
claim_id: HC-DU-147
work_id: CCR-PHYSICAL-RECORD-INTERFACE-SELECTION
action_id: PRIS-11-MEDIATOR-DIAGNOSTIC-IDENTIFIABILITY
run_id: RUN-20260730-022641-mediator-diagnostic-identifiability
lanes:
  - lane_1
  - lane_3
  - lane_4
  - lane_6
  - lane_7
channels:
  - CH-COLLIDE
  - CH-FORMAL
  - CH-MODEL
  - CH-EMPIRICAL
evidence_grade: 4
maximum_grade: 4
---

# Probe-process mediator diagnostics and component attribution

## Executive result

This swing takes the cheapest repair left by `HC-DU-146`: replace one final
entanglement readout with a complete family of probe preparations,
interventions, time-indexed observations, and output measurements.

The return is:

```text
EFFECTIVE_PROCESS_AND_MEDIATOR_REGIME_CAN_BE_IDENTIFIED_CONDITIONALLY
+ COMPLETE_PROBE_PROCESS_STILL_NEED_NOT_IDENTIFY_THE_NAMED_COMPONENT
+ INACCESSIBLE_COMPONENT_SWAP_GIVES_AN_ALL_PROTOCOLS_NO_GO
+ COMPONENT_SELECTIVE_ACCESS_OR_PROVENANCE_BREAKS_THE_SYMMETRY_EXACTLY
+ ONE_SIDED_READOUT_IS_NOT_THE_SAME_AS_PROBE_ONLY_INTERVENTION
+ THEORY_SPECIFIC_COMMUTATOR_AND_MEMORY_SIGNATURES_REMAIN CONDITIONAL REOPENERS
+ NO_OBSERVED_EXCLUSIVE_MEDIATION_PACKET
+ NO_READY_SUCCESSOR
```

Richer diagnostics are genuinely useful. They can identify an effective
channel, reject a classical-memory realization class, distinguish an active
from a frozen mediator within a fixed model, or recover Hamiltonian
parameters up to an input--output equivalence. `HC-DU-146` should therefore
not be read as saying that all endpoint and time-series work is empty.

But richer probe data does not automatically recover causal provenance:

> If two inaccessible candidate components are related by a symmetry that
> fixes every accessible probe preparation, intervention, and measurement,
> then even complete probe-process tomography cannot determine which named
> component carried the interaction.

The result is stronger than the earlier same-endpoint counterexample. It
holds for every finite adaptive protocol on the probes, not only for one
chosen final state.

The repair is also exact. Break the inaccessible-component symmetry with an
independently calibrated component-selective operation, a known coupling
topology, retained causal provenance, an exclusive-mediation theorem, or a
frozen component-specific excess prediction. In the finite control, one
\(X_G\) pulse changes the accessible final \(A B\) parity in opposite ways
depending on whether \(G\) or \(Q\) was active.

This earns a scoped Grade-4 process-level attribution boundary and an exact
positive control. It does not identify gravity in nature, validate any
proposed gravity experiment, prove that all system identification is
nonunique, observe mediator nonclassicality, or produce new physics.

## 1. What the successor question actually asks

Let the accessible probes be \(P=A B\), and let the inaccessible candidate
mediator packet be

\[
M=GQ.
\]

There are at least five distinct inference targets.

1. **Endpoint target:** what is the final reduced probe state?
2. **Effective-process target:** which input--output channel or process tensor
   acts on the probes?
3. **Realization-class target:** does every realization require quantum
   memory, noncommuting mediator observables, or another declared resource?
4. **Parameter target:** what couplings or frequencies occur inside a frozen
   Hamiltonian family?
5. **Component-attribution target:** did the physical component named \(G\),
   rather than \(Q\), carry the relevant interaction?

Each target is finer than some of the preceding targets, but none is merely
another name for them. A method can succeed at targets 2--4 while failing at
target 5.

For Dynamic Unity, this distinction is a record-fibre statement. Let

\[
\Pi_P(c)
\]

denote the complete accessible input--output behavior of completion \(c\)
under the frozen probe protocol class, and let

\[
\tau_G(c)\in\{0,1\}
\]

state whether named component \(G\) was active. Component attribution from
the complete probe process exists exactly when

\[
\ker \Pi_P\subseteq\ker\tau_G.
\]

`HC-DU-147` constructs a symmetry orbit contained in
\(\ker\Pi_P\) but not in \(\ker\tau_G\).

## 2. All-probe-process component nonidentifiability

Let

\[
\mathcal H
=\mathcal H_P\otimes\mathcal H_G\otimes\mathcal H_Q
\]

and let \(S_{GQ}\) exchange the two candidate mediator factors. Assume:

1. the initial inaccessible state is swap invariant,

   \[
   S_{GQ}\rho_M S_{GQ}^{\dagger}=\rho_M;
   \]

2. every admitted preparation, intervention, instrument, and measurement is
   accessible on \(P\) only and therefore commutes with \(S_{GQ}\);
3. the \(Q\)-active realization is the swap conjugate of the \(G\)-active
   realization at every dynamical segment,

   \[
   U_j^{(Q)}
   =S_{GQ}U_j^{(G)}S_{GQ}^{\dagger};
   \]
4. the attribution target changes under that swap:

   \[
   \tau_G(c_G)=1,\qquad \tau_G(c_Q)=0.
   \]

### Theorem

Every finite probe-only adaptive protocol has the same full outcome
distribution in \(c_G\) and \(c_Q\), although the named active-component
target differs. Consequently \(\tau_G\) does not factor through the complete
probe process.

### Proof

For a nonadaptive protocol, commute \(S_{GQ}\) through each probe operation.
The two final global states are swap conjugate. A probe POVM has the form
\(E_y\otimes I_{GQ}\), so

\[
\begin{aligned}
p_Q(y)
&=\operatorname{tr}\!\left[
  (E_y\otimes I)\,
  S_{GQ}\rho_G^{\rm out}S_{GQ}^{\dagger}
  \right] \\
&=\operatorname{tr}\!\left[
  S_{GQ}^{\dagger}(E_y\otimes I)S_{GQ}\,
  \rho_G^{\rm out}
  \right] \\
&=\operatorname{tr}\!\left[
  (E_y\otimes I)\rho_G^{\rm out}
  \right] \\
&=p_G(y).
\end{aligned}
\]

For an adaptive protocol, apply the same argument branch by branch. The first
probe outcome has the same probability in both realizations, and the
conditional postmeasurement states are again related by \(S_{GQ}\). Because
the controller receives the same outcome history, it chooses the same next
probe operation. Induction closes every finite branch.

Thus

\[
\Pi_P(c_G)=\Pi_P(c_Q)
\quad\text{but}\quad
\tau_G(c_G)\ne\tau_G(c_Q).
\]

The factorization criterion then rules out a probe-process-only attribution
map. \(\square\)

### Scope

This is a stabilizer theorem, not a universal denial of component
identifiability. If independent physical information removes the swap from
the admitted completion class, the theorem no longer applies. That
information must be named rather than silently imported.

Examples include:

- known network topology or known interaction graph;
- a calibrated actuator coupled to one component only;
- a component-specific observable or source response;
- retained provenance identifying which coupling occurred;
- an exclusive-mediation result;
- a theory-specific prediction whose functional form no rival realization
  in the frozen class shares.

## 3. Exact finite regression

The executable control extends `HC-DU-146`. Use qubits

\[
(A,B,G,Q)
\]

with mediators initialized to \(|00\rangle_{GQ}\). The \(M\)-active path is

\[
\operatorname{CNOT}_{A\to M},
\quad \mathcal A_1,
\quad \operatorname{CNOT}_{M\to B},
\quad \mathcal A_2,
\quad \operatorname{CNOT}_{A\to M},
\]

where \(\mathcal A_1,\mathcal A_2\) act only on \(A B\).

The regression verifies:

- swap conjugacy on all 16 computational basis states;
- commutation of the \(G/Q\) swap with ten probe-control generators;
- equality of the reduced probe output for 16 informationally spanning
  product inputs and all 100 pairs of the admitted controls;
- zero reduced-state difference across 1,600 finite protocols; and
- equality of the full outputs after swapping the inaccessible factors.

The enumeration is a regression, not the proof. The symmetry theorem covers
arbitrary probe-only instruments.

### Positive control

Insert one independently calibrated \(X_G\) pulse after the first routed
coupling. For input

\[
|+\rangle_A|0\rangle_B|00\rangle_{GQ},
\]

the \(G\)-active route ends in

\[
\frac{|0110\rangle+|1010\rangle}{\sqrt 2},
\]

so the \(A B\) parity is odd with probability one. The \(Q\)-active route ends
in

\[
\frac{|0010\rangle+|1110\rangle}{\sqrt 2},
\]

so the \(A B\) parity is even with probability one.

The attribution became possible because the experiment bought
component-specific access. It was not extracted from more repetitions of the
same symmetric probe record.

Run:

```bash
python3 tests/du_mediator_diagnostic_identifiability_probe.py --write-artifact
```

## 4. What established diagnostics actually identify

### Inaccessible-object nonclassicality

Krisnanda et al.'s
[inaccessible-object witness](https://arxiv.org/abs/1607.01140) infers that
the total inaccessible mediator developed nonclassical correlations under a
frozen local-interaction packet. It is a realization-class witness, not a
microscopic component selector.

Raia, Di Pietra, and Marletto derive
[quantitative bounds](https://arxiv.org/abs/2410.00824) relating correlation
growth at the probes to noncommutativity of mediator observables appearing in
the supplied interaction Hamiltonians. The result is stronger than an
endpoint slogan, but its component labels and Hamiltonian factorization are
antecedent.

### Model-relative mediator regimes

Christopher and Shankaranarayanan use
[dynamical fidelity susceptibility](https://arxiv.org/abs/2506.04300) of a
reduced two-oscillator state to distinguish frozen/heavy and dynamically
active/light mediator regimes in a fixed three-oscillator model. This is a
useful diagnostic of the supplied model's mediator dynamics. It does not
show that no operationally equivalent hidden component could implement the
same reduced process.

### Quantum-memory witnesses

Beyer, Kim, and Pikovski propose a
[one-sided witness for quantum gravitational
dynamics](https://arxiv.org/abs/2507.15588). Their classical-memory null has
the sequential form

\[
\mathcal E_1(\rho)=\sum_i K_i\rho K_i^\dagger,
\qquad
\mathcal E_2(\rho)
=\sum_i\Phi_i[K_i\rho K_i^\dagger].
\]

Failure of every such decomposition witnesses quantum memory in the admitted
joint process. That is a meaningful realization-class result.

Two guards matter:

1. one-sided **measurement** is not automatically probe-only
   **intervention**; the ideal construction includes controlled operations
   in the joint probe--memory packet; and
2. the interpretation freezes product initialization, negligible rival
   forces, the admitted local operations, and the physical identification of
   the memory.

The authors also distinguish an experimentally accessible witness from a
unique virtual-particle or microscopic ontological mechanism. Dynamic Unity
should preserve that distinction.

### Quantum system identification

Burgarth and Yuasa's
[quantum system-identification theorem](https://arxiv.org/abs/1104.0583)
defines operational equivalence by equality under all admitted input--output
experiments. Under controllability, equivalent closed systems are related by
a unitary similarity:

\[
H_k=U\widehat H_kU^\dagger,\qquad
M_\ell=U\widehat M_\ell U^\dagger,\qquad
\rho_0=U\widehat\rho_0U^\dagger.
\]

Thus complete experiment data can identify the system only up to the
residual equivalence that preserves the experiment. Known Hamiltonian
elements, topology, or an infecting controlled subset can shrink that
freedom and sometimes identify couplings up to local phase conventions.

This is the established positive and negative result DU needs:

- full input--output data is much stronger than one endpoint;
- it can reconstruct effective dynamics under explicit controllability and
  model assumptions;
- it does not generally turn an equivalence-class representative into a
  uniquely selected ontology.

### Theory-specific excess

Chen and Giacomini propose a
[field-commutator phase and extended-source
signature](https://arxiv.org/abs/2402.10288) beyond the ordinary Newton
potential in a supplied linearized quantum-gravity treatment. Di Pietra and
Marletto give
[temporal witnesses](https://arxiv.org/abs/2205.00198) using a probe plus a
conservation-law packet.

These are legitimate conditional reopeners because their goal is a frozen
functional form or resource class, not mere endpoint entanglement. They
remain proposals until the model class, rival absorbers, acquisition, and
observed packet are fixed.

Vidal, Marletto, Vedral, and Chiribella's
[nonlocally tomographic
models](https://arxiv.org/abs/2506.21122) are a particularly strong warning:
what counts as a locally classical mediator can change when the surrounding
theory's composition rule changes. A witness must freeze that rule before
attributing a component.

## 5. The diagnostic ladder

| Evidence packet | What it can earn | What it does not yet earn |
|---|---|---|
| Final probe entanglement under the complete Marletto--Vedral premises | exclusion of the declared all-classical total-mediator class | named component, history, or gravity attribution |
| Reduced time series or fidelity susceptibility in a frozen model | active/frozen regime or parameter sensitivity | selection of the model or microscopic component |
| Two-time quantum-memory witness | exclusion of a classical-memory realization class | unique mediator mechanism or component provenance |
| Complete probe input--output identification | effective process or Hamiltonian equivalence class | a target that varies inside that equivalence class |
| Known topology or component-selective intervention | component parameters or route within that frozen architecture | proof that the architecture was physically selected |
| Formed component provenance or exclusive mediation | named-component attribution | theory-independent ontology beyond the certificate's scope |
| Frozen component-specific excess observed against rivals | empirical component discrimination | universal reconstruction without the remaining assumptions |

The ladder prevents two opposite errors:

- dismissing every mediator diagnostic because endpoint attribution fails;
- promoting effective-process reconstruction into unique component ontology.

## 6. Dynamic Unity consequence

The complete observer-accessible process is a legitimate record object. It
can reconstruct everything the observer can predict and control even when it
does not name a unique inaccessible implementation. That is not a failure of
operational reconstruction.

It becomes a failure only when the target is explicitly finer—for example,
"the gravitational field, rather than quantum matter or another hidden
component, carried the nonclassical path." For that target, the physical
completion fibre must first quotient harmless gauge freedom while retaining
real component distinctions. The record then has to be constant on the
remaining fibre.

The resulting research rule is:

> Diagnose effective dynamics with the richest justified probe process, but
> require a symmetry-breaking physical interface before claiming named
> component provenance.

This is directly analogous to distributed-system observability. Complete
client traces can identify the replicated service behavior while leaving
which symmetric replica executed a request unknowable. A signed receipt,
replica-selective fault injection, or fixed topology can identify the node.
The analogy organizes the contract; the quantum symmetry theorem supplies
the result.

## 7. Disposition

### Bank

Bank `HC-DU-147` as:

1. a scoped all-probe-process component-attribution
   nonidentifiability theorem;
2. an exact inaccessible-factor swap counterexample;
3. an exact component-selective positive control;
4. a typed hierarchy separating regime, process, realization class,
   parameter, and component attribution; and
5. a primary-source map of conditional empirical reopeners.

### Do not promote

Do not promote:

- a claim that tomography is useless;
- a universal nonidentifiability theorem without a stabilizer;
- a gravity ontology;
- an observed mediator result;
- a new law or empirical prediction;
- a hardware campaign;
- a paper seed; or
- a scientific successor.

### Exact reopener

Reopen this branch only with one of:

1. an observed exclusive-mediation packet with retained component
   provenance;
2. an independently calibrated component-selective intervention or source
   response;
3. a frozen topology and controllability theorem that removes the relevant
   stabilizer;
4. a component-specific excess functional form that survives the complete
   admitted rival class; or
5. a stronger physical theorem showing that the candidate swap is not a
   lawful completion symmetry.

Until then, further probe-only tomography can improve effective-process
knowledge but cannot, by itself, close the named-component target.

## 8. Grade

**Evidence grade: scoped Grade 4.**

The all-probe theorem is exact under declared symmetry assumptions; the
finite regression and positive control pass exactly; the diagnostic hierarchy
is grounded in primary sources.

The result is substantially absorbed by input--output equivalence, unitary
similarity, system identification, realization freedom, and ordinary
symmetry reasoning. No Grade-5 empirical excess, observed acquisition packet,
new physics, gravity verdict, or flagship successor is earned.
