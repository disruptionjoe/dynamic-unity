---
date: 2026-07-26
run_id: RUN-20260726-070222-hardware-acquisition-bridge
status: HARDWARE_BRIDGE_READY
lanes:
  - lane_1
  - lane_3
  - lane_4
  - lane_7
  - lane_A
channels:
  - CH-EMPIRICAL
  - CH-FORMAL
  - CH-MODEL
  - CH-COLLIDE
claim_grade: "exact acquisition-visibility ceiling plus hardware-ready provider contract; no hardware run or physical verdict"
---

# Acquisition visibility and the first hardware-ready bridge

## Result in plain English

Dynamic Unity can now run its smallest record-sufficiency experiment through a
current shot-resolved quantum-provider interface without losing the declared
classical registers, circuit identity, calibration arms, held-out arms, causal
break, or provider execution windows.

That does **not** yet close the physical-evidence gate. A standard provider
result says which requested shots were returned. It does not certify that
every lower-level physical trigger, retry, rejected attempt, selection reason,
controller memory, and environmental memory is visible. Therefore:

> “The returned shots factor through this record” is a conditional result
> about the provider-visible population, not yet a result about the complete
> attempted physical process.

The swing closes the software bridge and sharpens the remaining experimental
contract. It does not submit a hardware job and does not produce a physical
factorization, remainder, ontology, or new-physics verdict.

## Acquisition-Visibility Factorization Lemma

Let:

- \(h\) be a physical history;
- \(a\) be a held-out intervention;
- \(R(h)\) be the candidate certified record;
- \(S\) identify the acquisition/selection stratum, such as returned versus
  rejected; and
- \(Y\) be the response, including an appropriate invalid/rejection outcome
  when \(S=0\).

For histories with the same candidate record and the same intervention,

\[
P(S,Y\mid h,a)
\]

factors through \((R(h),a)\) if and only if both:

\[
P(S\mid h,a)
\]

factors through \((R(h),a)\), and, for every stratum \(s\) with nonzero
support,

\[
P(Y\mid S=s,h,a)
\]

also factors through \((R(h),a)\).

This is the ordinary conditional-probability decomposition

\[
P(S,Y\mid h,a)
=
P(S\mid h,a)P(Y\mid S,h,a),
\]

not a claimed new statistics theorem. Its Dynamic Unity consequence is
load-bearing: an accepted-shot assay observes only the \(S=1\) response
kernel. Even an exactly known acceptance rate does not identify the rejected
stratum.

### Exact counterexample

Take two histories \(h_0,h_1\) with the same candidate record. List joint
probabilities in the order
\((S{=}0,Y{=}0),(S{=}0,Y{=}1),(S{=}1,Y{=}0),(S{=}1,Y{=}1)\):

\[
\begin{aligned}
P_{h_0} &= (1/2,0,1/2,0),\\
P_{h_1} &= (0,1/2,1/2,0).
\end{aligned}
\]

Both histories have acceptance probability \(1/2\). Every accepted response
is \(Y=0\). The provider-visible distributions and acceptance rates are
identical, yet the rejected responses—and therefore the complete attempted
processes—differ.

The deterministic probe exhaustively checked all 100 pairs of four-cell
probability kernels with denominator two and recovered the stated
factorization equivalence.

## Provider collision

The current IBM interface is sufficient for a valuable first hardware pass:

- IBM documents dynamic circuits with mid-circuit measurement and reset
  support through the Sampler path
  ([dynamic-circuit guide](https://quantum.cloud.ibm.com/docs/en/guides/execute-dynamic-circuits)).
- A Sampler result contains one ordered `BitArray` per named classical
  register, so pointer, environment, reset witness, and output can remain
  joined by shot index
  ([Sampler inputs and outputs](https://quantum.cloud.ibm.com/docs/en/guides/sampler-input-output)).
- `ExecutionSpans` provide start/stop windows and PUB/shot masks. These are
  honest bounds, not exact per-shot timestamps
  ([execution-span section](https://quantum.cloud.ibm.com/docs/en/guides/sampler-input-output#view-execution-spans)).
- Jobs retain stable identifiers and results can be retrieved later
  ([job retrieval](https://quantum.cloud.ibm.com/docs/en/guides/save-jobs)).
- Provider options distinguish per-shot initialization and classified versus
  kerneled measurement
  ([execution options](https://quantum.cloud.ibm.com/docs/en/guides/executor-options)).

Those features preserve the provider-visible experiment. None of the cited
interfaces promises that its returned result is a census of every
lower-level physical attempt or that all provider/controller/environment
memory has been exposed and causally broken. The capture contract records that
absence rather than inventing it away.

## Frozen hardware suite

The bridge freezes 19 circuits over three qubits:

| Arm | Count | Purpose |
|---|---:|---|
| pointer/environment/output readout calibration | 6 | prepare and read 0/1 for each response register |
| reset calibration | 3 | prepare 1, reset, and witness each qubit |
| training experiment | 4 | two histories × identity/flip interventions |
| held-out experiment | 4 | distinct circuit identities for the same frozen factorial design |
| causal break | 2 | reset all declared qubits, witness reset, reset again, then read environment/output |

The roles are:

- `q0`: response system;
- `q1`: formed environment record;
- `q2`: deliberately incomplete pointer record;
- `pointer`: candidate record;
- `environment`: first admissible formed completion;
- `reset_witness`: causal-break evidence; and
- `output`: held-out response.

The expected ordinary-quantum branch is deliberately nontrivial but not new
physics: the incomplete pointer should fail to reconstruct every held-out
response, adding the formed environment record should repair it within
tolerance, and a complete causal break should remove accessible history
dependence. A surprising result is not creditable until calibration,
selection, drift, route, and reset alternatives pass.

## What was executed

Using Qiskit 2.5.1 and Aer 0.17.2:

- all 19 circuits built and transpiled;
- 32 shots per circuit produced 608 shot-register rows;
- every pointer, environment, reset-witness, and output row joined;
- all frozen manifest, attachment, row, span, calibration, holdout, and reset
  structural checks passed; and
- the result remained correctly classified as `SYNTHETIC_CONTROL_ONLY`.

The standard-library adversarial probe passed `15/15` checks twice with
byte-identical output. It also verified that:

- refitting a circuit after freeze is refused;
- mutating a register row is refused by both row and attachment hashes;
- losing one shot is refused;
- freezing after acquisition is refused;
- a hardware call is refused before provider import or contact without exact
  direct-chat authorization;
- provider-returned rows stop at
  `RETURNED_SHOT_CONDITIONAL_ONLY`;
- complete attempt visibility without complete reset stops at
  `ALL_ATTEMPTS_OBSERVED_NO_REMAINDER`; and
- only complete attempt visibility plus complete reset reaches
  `IMPLEMENTATION_COMPLETE_MAPPING_ELIGIBLE`.

Artifacts:

- [provider-capture schema](../specs/physical-sufficiency-provider-capture-v0.1.schema.json)
- [acquisition driver](../lab/acquisition/ibm_runtime_du_acquisition.py)
- [driver guide](../lab/acquisition/README.md)
- [adversarial probe](../tests/du_acquisition_visibility_bridge_probe.py)
- [deterministic receipt](../tests/artifacts/du_acquisition_visibility_bridge_result.json)
- [Qiskit/Aer dry-run receipt](../tests/artifacts/du_ibm_runtime_acquisition_dry_run_result.json)

## North-Star consequence

This creates a useful two-rung physical program:

1. **Provider-conditional hardware pilot.** Run the frozen suite on a real
   device to test whether the circuit, calibration, held-out, and
   pointer-plus-environment reconstruction behavior survives hardware noise.
   The ceiling is explicitly conditional on returned shots.
2. **Implementation-complete laboratory packet.** Co-design acquisition with
   a platform team that can expose physical triggers, invalid/rejected rows,
   selection reasons, route/controller state, and a causal break over every
   admitted retained memory. Only this rung can adjudicate the physical
   remainder.

The pilot is still useful: it can kill an unworkable instrument, quantify
noise and completion size, and prepare a laboratory collaboration. It cannot
by itself answer whether certified records reconstruct all
observer-accessible physics.

## Exact next action

After direct authorization, run one low-shot provider pilot with the frozen
manifest and retain the complete capture. Report its result only as
provider-returned-shot conditional evidence. In parallel or afterward,
approach a laboratory capable of exposing the additional acquisition and
reset boundary. Do not spend another swing on synthetic factorization unless
the hardware pilot reveals a concrete software or calibration defect.
