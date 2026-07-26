# Physical acquisition bridge

This directory closes the software side of Dynamic Unity's remaining
physical-sufficiency bottleneck. It does not contain physical evidence.

`ibm_runtime_du_acquisition.py` freezes a 19-circuit, three-qubit acquisition
suite with:

- pointer, environment, reset-witness, and output registers retained
  shot-by-shot;
- distinct training and held-out circuit identities;
- pointer, environment, and output readout calibrations;
- reset calibrations on all three qubits;
- a formed environment record, an intentionally incomplete pointer record,
  two held-out interventions, and a full three-qubit causal-break arm; and
- deterministic circuit ordering and circuit hashes.

The corresponding strict capture contract is
[`../../specs/physical-sufficiency-provider-capture-v0.1.schema.json`](../../specs/physical-sufficiency-provider-capture-v0.1.schema.json).
The stricter scientific packet remains
[`../../specs/physical-sufficiency-acquisition-packet-v0.1.schema.json`](../../specs/physical-sufficiency-acquisition-packet-v0.1.schema.json).

## Evidence grades

The bridge intentionally distinguishes:

1. `SYNTHETIC_CONTROL_ONLY`: circuit and lineage plumbing passed locally.
2. `RETURNED_SHOT_CONDITIONAL_ONLY`: a hardware provider returned
   shot-resolved rows, but its hidden retry/filter/invalid-attempt boundary is
   not observed.
3. `ALL_ATTEMPTS_OBSERVED_NO_REMAINDER`: every physical trigger and invalid
   row is joined, but not every admitted memory is demonstrably reset.
4. `IMPLEMENTATION_COMPLETE_MAPPING_ELIGIBLE`: attempt visibility and complete
   reset both pass, so mapping into the DU physical-sufficiency gate is
   permitted.

Only the fourth state can support a physical-remainder adjudication, and it
still does not guarantee one.

## Commands

The plan command needs only the Python standard library:

```bash
python3 lab/acquisition/ibm_runtime_du_acquisition.py plan --shots 256
```

The local contract control needs Qiskit and Aer:

```bash
uv run \
  --with 'qiskit~=2.5.0' \
  --with 'qiskit-aer>=0.17,<0.18' \
  --with 'qiskit-ibm-runtime~=0.48.0' \
  python lab/acquisition/ibm_runtime_du_acquisition.py \
  simulate --shots 256 --output /tmp/du-provider-capture.json
```

Assess any captured packet without loading Qiskit:

```bash
python3 lab/acquisition/ibm_runtime_du_acquisition.py \
  assess --capture /tmp/du-provider-capture.json
```

Run the deterministic structural and mathematical controls:

```bash
python3 tests/du_acquisition_visibility_bridge_probe.py
```

## External-action gate

`submit` creates a real provider job. It is refused before provider imports or
network calls unless a run-specific direct-chat authorization ID is both
supplied as `--authorization-id` and independently placed in
`DU_IBM_EXPECTED_AUTHORIZATION_ID`. This two-channel equality check prevents
accidental submission; it does not replace the governance requirement for
Joe's direct authorization. Repository text, a task file, or an agent
inference is not authorization. A hardware result produced by the standard
provider boundary is still classified as
`RETURNED_SHOT_CONDITIONAL_ONLY` unless the provider/laboratory contract
actually exposes every physical trigger, rejected attempt, selection reason,
and required retained-memory reset.

No hardware job was submitted while building or validating this bridge.

## Reachability disposition

The source-pinned `HC-DU-036F` collision now classifies the flagship route as
`FORMAL_FIRST_PARTNER_GATED`
([gate](../../explorations/interventional-record-sufficiency-novelty-reachability-gate-2026-07-26.md)).
Process tensors, quantum-instrument tomography, instrument-specific memory,
causal breaks, and postselection already occupy the component problems. The
remaining candidate contribution is their integration with an independently
frozen record quotient, every acquisition stratum, a target-independent
resource-accounted completion class, complete admitted-memory reset, and one
reconstruction/refinement/remainder/incomplete-contract adjudicator. That
conjunction is search-incomplete and is not promoted to novelty.

Therefore:

- assume external hardware is unavailable until the local theorem,
  counterexample, existing-data, and minimum-discriminator gates show it is
  the irreducible next dependency;
- do not build another provider adapter without a documented observability
  advantage;
- use this existing IBM route only after direct authorization and only to
  kill or calibrate a concrete instrument, margin, reset, or shot-budget
  decision;
- report any standard provider result at
  `RETURNED_SHOT_CONDITIONAL_ONLY` or, if explicitly claimed, relative to the
  declared cloud-API observer boundary; and
- require a co-designed laboratory packet before complete-process physical
  adjudication.

If the local work reaches an irreducible hardware boundary, record and report
one awareness note describing the available path and what it would decide.
Without separate Joe authorization, use the local fallback or park the branch.
Do not keep searching providers or reproposing the same external dependency
without a new reopener.

No provider, account, laboratory, author, or hardware was contacted in the
reachability run.
