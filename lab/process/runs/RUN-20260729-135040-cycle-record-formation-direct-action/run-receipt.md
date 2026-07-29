---
run_id: RUN-20260729-135040-cycle-record-formation-direct-action
status: completed
started_at: 2026-07-29T13:50:40-05:00
completed_at: 2026-07-29T14:03:19-05:00
repository: dynamic-unity
work_id: CCR-CYCLE-RECORD-FORMATION-DIRECT-ACTION-DESCENT
claim_id: HC-DU-125
state_revision: 76
---

# Run receipt

## Outcome

Banked a scoped Grade-4 exact finite-Abelian homomorphic-record formation,
cutwise resource necessity/sufficiency, regional-correlation gluing, and
field/direct-action descent theorem.

For any finite-Abelian homomorphism \(Q:D\to H\), a uniform state on
\(\ker Q\), local controlled addition, and local group-basis readout
implement the exact selective Lüders instrument for \(Q\). The raw
transcript reveals only the target fibre and causes no dephasing within it.

Across a station cut \(S:\bar S\), the exact ancillary-entanglement
necessity and sufficiency is

\[
\log_2
\left|
\operatorname{im}Q_S
\cap
\operatorname{im}Q_{\bar S}
\right|.
\]

For a complete graph-cycle record this becomes

\[
\bigl(|V|-c(S)-c(\bar S)+1\bigr)\log_2|G|,
\]

the graphic-matroid connectivity function times the group information unit.

In a two-region cover, each local masked transcript reveals exactly its
local cycle class. The cross-region gluing sector is absent from both
marginals and present in their joined correlations.

An exact star--triangle control gives the same reduced source action with
interaction-graph cycle ranks zero and one. Therefore a mediator/field-cycle
record does not automatically descend to a direct source action.

## Exact returns

```text
UNIFORM_KERNEL_ANCILLA_IMPLEMENTS_EXACT_HOMOMORPHIC_LUDERS_MEASUREMENT
RAW_TRANSCRIPT_REVEALS_ONLY_THE_TARGET_FIBRE
LOCAL_TRANSCRIPT_REVEALS_EXACTLY_THE_PROJECTED_KERNEL_QUOTIENT
COMPLETE_CYCLE_INSTRUMENT_IS_BASIS_INVARIANT
UNIFORM_COBOUNDARY_RESOURCE_FORMS_ALL_LOCAL_AND_CROSS_CYCLE_RECORDS
REGIONAL_MARGINALS_REVEAL_ONLY_LOCAL_CYCLE_CLASSES
CROSS_REGION_GLUE_LIVES_IN_JOINED_TRANSCRIPT_CORRELATIONS
DISCARDING_LINEAGE_ERASES_THE_GLUE_SECTOR
CUTWISE_RESOURCE_COST_IS_LOG_SHARED_SYNDROME_ORDER
GRAPH_CYCLE_RESOURCE_COST_IS_MATROID_CONNECTIVITY_TIMES_LOG_GROUP_ORDER
ONE_RESOURCE_ATTAINS_EVERY_CUTWISE_LOWER_BOUND
SOURCE_ACTION_DOES_NOT_DETERMINE_MEDIATOR_CYCLE_TOPOLOGY
STAR_AND_TRIANGLE_HAVE_ONE_SOURCE_KERNEL_AND_DIFFERENT_CYCLE_RANK
FIELD_CYCLE_RECORD_DOES_NOT_AUTOMATICALLY_DESCEND_TO_DIRECT_ACTION
DIRECT_ACTION_CAN_HOST_A_RELATIONAL_RECORD_ONLY_AFTER_RETYPE_AND_INTERFACE_SUPPLY
NO_FIELD_OR_DIRECT_ACTION_ONTOLOGY_SELECTION
NO_PUBLIC_FINALITY_COMPLETE_RESOURCE_LAW_OR_EMPIRICAL_EXCESS
NO_READY_SUCCESSOR
```

## Homomorphic instrument

With

\[
|\Omega_K\rangle
=
|K|^{-1/2}\sum_{k\in K}|k\rangle,
\qquad K=\ker Q,
\]

the joined raw result \(z\) satisfies

\[
\Pr(z\mid y)
=
|K|^{-1}\mathbf1[Q(z)=Q(y)].
\]

Its Kraus operator is

\[
M_z=|K|^{-1/2}P_{Q(z)}.
\]

Coarse-graining by \(Q(z)\) is therefore exactly the selective Lüders
instrument. A station subset \(S\) sees a uniform coset

\[
y_S+\pi_S(K)
\]

and hence exactly the quotient \(D_S/\pi_S(K)\).

## Cutwise resource theorem

Writing

\[
I_S=\operatorname{im}Q_S\cap\operatorname{im}Q_{\bar S},
\]

the kernel state has \(|I_S|\) equal Schmidt coefficients across the cut.
Applying the target measurement to a product uniform input produces, in
every outcome branch, an affine-kernel state with the same entanglement.
LOCC monotonicity gives the lower bound, while the kernel state attains it on
all cuts simultaneously.

For the complete cycle map, \(\ker Q_\Gamma=\operatorname{im}d\), and the
shared-syndrome exponent is

\[
\lambda_\Gamma(S)
=
r(S)+r(\bar S)-r(E)
=
|V|-c(S)-c(\bar S)+1.
\]

This is graphic-matroid connectivity, not endpoint min-cut, overlap
component count, BFT threshold, or communication cost.

## Regional-correlation theorem

The global uniform-coboundary transcript restricts to the exact local
uniform-coboundary transcript in each connected region. Therefore:

- local marginal equality is exactly local-cycle-class equality;
- global cycle classes sharing the same local pair have identical local
  marginals; and
- their joined transcript supports are disjoint.

The \(k-1\) missing Mayer--Vietoris gluing coordinates from `HC-DU-124` live
in transcript correlations. Preserving joined lineage retains them;
discarding the association erases them.

## Direct-action boundary

The star action

\[
S_Y=\frac12\sum_{i=1}^{3}3(x_i-x_0)^2
\]

has, after stationary elimination of \(x_0\), the same boundary quadratic
form as the unit-conductance triangle

\[
S_\Delta=\frac12\sum_{i<j}(x_i-x_j)^2.
\]

The source kernel is identical for all boundary assignments, but the star
has cycle rank zero and the triangle cycle rank one.

Thus:

- source queries factoring through the complete reduced action are
  preserved;
- mediator-local cycle topology and the associated field record are not
  preserved automatically; and
- a direct-action-native relation record is possible only after relation
  variables, actions, factorization, target, resource, formation, and access
  are retyped and supplied.

This does not select a field or direct-action ontology. Full quantum
equivalence additionally needs determinant, measure, state, boundary,
regulator, gauge, background, and counterterm matching.

## Strongest absorbers

- finite-Abelian homomorphism and quotient mathematics;
- subgroup and stabilizer-state entanglement;
- graph cycle/cut spaces and matroid connectivity;
- Abelian Wilson-loop nondemolition measurement;
- Mayer--Vietoris gluing; and
- Schur complements, Dirichlet-to-Neumann maps, and star--triangle
  equivalence.

The Dynamic Unity increment is their exact typed composition, not new
component mathematics or empirical excess.

## Local-model disposition

`MINIMAL_EXACT_REGRESSION_ONLY`.

The analytic proof decides the result. Enumeration preserves exact
transcript fibres, matrix-unit factors, Schmidt spectra, graph-cut ranks,
regional marginals/correlations, cycle-basis invariance, and the rational
star--triangle Schur complement. No simulation or hardware can raise the
grade.

## Validation

- `python3 tests/du_cycle_record_formation_direct_action_probe.py` —
  **PASS**, `24/24`;
- `python3 tests/du_regional_cycle_record_gluing_probe.py` —
  **PASS**, `17/17`;
- `python3 tests/du_graph_cycle_record_cohomology_probe.py` —
  **PASS**, `18/18`;
- `python3 tests/du_wilson_record_capability_first_leak_probe.py` —
  **PASS**, `14/14`;
- `python3 tests/du_finite_abelian_gauge_qnd_transfer_probe.py` —
  **PASS**, `14/14`;
- relevant `python3 -m py_compile` — **PASS**;
- `python3 tests/du_agent_orientation_contract_probe.py --write-artifact` —
  **PASS**, `37/37`;
- counter-assumptive register — `282` unique rows;
- cold-start contract — `5,985/6,000` words; and
- exact deterministic artifact —
  `tests/artifacts/du_cycle_record_formation_direct_action_result.json`.

## State transition

- `CURRENT-RESEARCH.yaml` advanced from revision `75` to `76`.
- No active scientific program, executable action, or successor was
  selected.
- `NI-DU-169` preserves the formation/resource/descent correction.
- The concept, quantum-foundations, and test surfaces expose the result and
  its non-transfer boundaries.

## Reopeners

1. Define a source-action-native record invariant under mediator
   elimination, star--triangle moves, and other response-preserving
   transformations.
2. Test whether a physical direct-action law selects that record and its
   factorization rather than merely admitting it.
3. Extend the resource theorem beyond finite Abelian quotient records.
4. Add authentication, access, and a declared fault model before interpreting
   correlation-carried glue as regional public finality.
5. Obtain an unchanged local-QFT or direct-action transfer with a
   physically selected interface.

## Non-promotions

No selected homomorphism, graph, matter sector, field, direct-action theory,
absorber, RTI event rule, relation complex, station factorization, resource,
instrument, observer, access boundary, provenance, authentication, fault
class, finalizer, complete resource law, consensus/BFT theorem, continuum or
AQFT transfer, empirical excess, new physics, prediction, paper, experiment,
hardware path, provider action, publication, submission, contact, or
sibling-repository mutation was authorized or produced.
