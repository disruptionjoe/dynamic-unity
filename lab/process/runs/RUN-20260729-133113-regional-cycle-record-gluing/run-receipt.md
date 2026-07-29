---
run_id: RUN-20260729-133113-regional-cycle-record-gluing
status: completed
started_at: 2026-07-29T13:31:13-05:00
completed_at: 2026-07-29T13:41:27-05:00
repository: dynamic-unity
work_id: CCR-REGIONAL-CYCLE-RECORD-GLUING
claim_id: HC-DU-124
state_revision: 75
---

# Run receipt

## Outcome

Banked a scoped Grade-4 exact two-region gluing-deficit, minimum
cross-coordinate repair, and layered physical-remainder theorem in the
unchanged finite-Abelian regular-matter graph arena.

Let a connected graph \(\Gamma=A\cup B\) be covered by connected subgraphs
whose nonempty intersection has \(k\) connected components. Restriction of a
global cycle class to the two complete local cycle records has kernel

\[
\ker\!\left(
H^1(\Gamma;G)\to H^1(A;G)\oplus H^1(B;G)
\right)
\cong G^{k-1}.
\]

Every compatible local-record pair therefore has exactly
\(|G|^{k-1}\) global cycle-class completions.

## Exact returns

```text
CONNECTED_OVERLAP_MAKES_COMPATIBLE_LOCAL_CYCLE_RECORDS_GLOBALLY_UNIQUE
DISCONNECTED_OVERLAP_CREATES_EXACT_CROSS_REGION_GLUE_DEFICIT
GLUE_DEFICIT_IS_GROUP_ORDER_TO_OVERLAP_COMPONENTS_MINUS_ONE
OVERLAP_COMPONENT_COUNT_NOT_OVERLAP_SIZE_CONTROLS_THE_DEFICIT
K_MINUS_ONE_CROSS_CYCLE_COORDINATES_ARE_NECESSARY
K_MINUS_ONE_CROSS_CYCLE_COORDINATES_ARE_SUFFICIENT
REGIONAL_CYCLE_RANK_OBEYS_THE_MAYER_VIETORIS_IDENTITY
LOCAL_TO_GLOBAL_CYCLE_COMPLETION_STILL_LEAVES_PHYSICAL_COBBOUNDARY_REMAINDER
LOCAL_RECORD_FIBRE_SIZE_IS_GROUP_ORDER_TO_VERTICES_PLUS_COMPONENTS_MINUS_TWO
TOTAL_UNIVERSAL_REPAIR_NEEDS_VERTICES_PLUS_COMPONENTS_MINUS_TWO_GROUP_COORDINATES
REGIONAL_GLUE_IS_NOT_PUBLIC_FINALITY_WITHOUT_ACCESS_FAULT_AND_CERTIFICATION_TYPES
NO_RESOURCE_LAW_INTERFACE_SELECTION_OR_EMPIRICAL_EXCESS
NO_READY_SUCCESSOR
```

## Gluing theorem

The Mayer--Vietoris sequence gives

\[
H^0(A;G)\oplus H^0(B;G)
\to H^0(A\cap B;G)
\to H^1(\Gamma;G)
\to H^1(A;G)\oplus H^1(B;G).
\]

Connected \(A\) and \(B\) contribute one constant each, while the
\(k\)-component overlap contributes \(G^k\). Quotienting by the diagonal
constant gives \(G^{k-1}\).

Consequently:

- connected overlap gives unique global cycle completion;
- disconnected overlap leaves exactly \(k-1\) independent \(G\)-valued
  cross-region loop facts; and
- overlap connectivity rather than overlap vertex count controls the
  deficit.

One path out through \(A\) and back through \(B\) for each non-base overlap
component constructs a sufficient cross-cycle basis. Cardinality makes
\(k-1\) necessary under the frozen \(G\)-valued-coordinate contract.

## Cycle-rank identity

The exact rank relation is

\[
\beta_1(\Gamma)
=
\beta_1(A)+\beta_1(B)-\beta_1(A\cap B)+(k-1).
\]

The last term is the global cross-region cycle sector absent from the two
local cycle records after overlap-cycle compatibility is enforced.

## Layered physical remainder

`HC-DU-123` leaves \(|G|^{|V|-1}\) physical dressed-edge configurations in
every complete global cycle class. Therefore each compatible local-record
fibre contains

\[
|G|^{k-1}|G|^{|V|-1}
=
|G|^{|V|+k-2}
\]

physical basis configurations.

The exact repair decomposition is:

```text
complete local cycle records
  + k-1 cross-region cycle values
    = complete global cycle record
  + |V|-1 spanning-tree dressed-edge values
    = complete dressed-edge basis state.
```

Global gluing and physical-state completion are distinct.

## Exact controls

The deterministic probe exhausts five finite covers:

- two triangles sharing one vertex: connected overlap and one global
  completion;
- two paths sharing two disconnected terminals: \(k=2\) and three global
  completions for \(G=\mathbb Z_3\);
- two trees sharing three disconnected terminals: \(k=3\) and four global
  completions for \(G=\mathbb Z_2\);
- a cyclic overlap plus one isolated overlap vertex: internal overlap
  compatibility plus one cross-coordinate deficit for
  \(G=\mathbb Z_2^2\); and
- two squares sharing one edge: two shared vertices but connected overlap
  and one global completion.

The second and fifth specimens hold the overlap vertex count at two while
changing its component count. The completion count changes from three to
one, isolating connectivity from size.

## Strongest absorbers

- the Mayer--Vietoris exact sequence;
- cellular graph cohomology;
- fundamental-cycle and spanning-tree coordinates;
- finite-Abelian cardinality; and
- the `HC-DU-121`--`123` matter-completed Wilson/cycle-record arena.

The mathematics is standard. The Dynamic Unity increment is the typed
regional-to-global-to-physical remainder decomposition.

## Local-model disposition

`MINIMAL_EXACT_REGRESSION_ONLY`.

The theorem decides the result. The bounded script preserves the rank
identity, overlap-component count, exact local-to-global fibres, explicit
cross-cycle repair, layered physical-state fibres, and minimum coordinate
counts. No simulation or hardware can raise the grade.

## Validation

- `python3 tests/du_regional_cycle_record_gluing_probe.py` —
  **PASS**, `17/17`, five regional-cover specimens;
- `python3 tests/du_graph_cycle_record_cohomology_probe.py` —
  **PASS**, `18/18`, five parent graph/cohomology specimens;
- `python3 tests/du_wilson_record_capability_first_leak_probe.py` —
  **PASS**, `14/14`, five parent capability specimens;
- `python3 tests/du_finite_abelian_gauge_qnd_transfer_probe.py` —
  **PASS**, `14/14`, five parent gauge specimens;
- `python3 -m py_compile tests/du_regional_cycle_record_gluing_probe.py tests/du_graph_cycle_record_cohomology_probe.py tests/du_wilson_record_capability_first_leak_probe.py tests/du_agent_orientation_contract_probe.py`
  — **PASS**;
- `python3 tests/du_agent_orientation_contract_probe.py --write-artifact` —
  **PASS**, `37/37`;
- counter-assumptive register — `281` unique rows;
- cold-start contract — `5,983/6,000` words; and
- exact deterministic artifact —
  `tests/artifacts/du_regional_cycle_record_gluing_result.json`.

## State transition

- `CURRENT-RESEARCH.yaml` advanced from revision `74` to `75`.
- No active scientific program, executable action, or successor was
  selected.
- `NI-DU-168` preserves the regional-gluing and layered-remainder correction.
- The concept, quantum-foundations, and test surfaces expose the theorem and
  its non-transfer boundaries.

## Reopeners

1. Extend to covers by three or more regions and type the Čech nerve.
2. Extend to finite two-complexes and separate \(H^1\) gluing from curvature
   and \(H^2\).
3. Physically form the local and cross-cycle records under one unchanged
   causal, resource, and disturbance contract.
4. Add a fault/adversary model before asking whether a cross-cycle value is a
   public-finality certificate.
5. Find the non-Abelian or operator-algebraic replacement.

## Non-promotions

No selected graph, regional cover, overlap, matter, cycle basis, local record
instrument, cross path, spanning tree, observer, action class, provenance,
access, verification, fault model, public-finality semantics, BFT or
cryptographic threshold, communication/latency/energy/entropy/entanglement
resource law, nondemolition repair, unrestricted reconstruction,
many-region, higher-cell, non-Abelian, continuous-group, AQFT, or continuum
transfer, empirical excess, new physical law, prediction, ontology priority,
paper, experiment, hardware path, provider action, publication, submission,
contact, or sibling-repository mutation was authorized or produced.
