# tests/

Computational checks and machine probes, each mapping to a claim, with
real-falsifier positive controls. A test that a genuine falsifier can pass is
not a test; controls are mandatory.

## HC-DU-206 common-view closure and metric-ruler boundary

`du_common_view_closure_probe.py` validates the exact finite controls for the
computation-first relationship atlas. It checks four individually lossy
two-bit perspective maps with a jointly separating rank-4 family, a rank-3
undercomplete falsifier, all fifteen classical and two-qubit-Pauli linear
response functionals, four axial metric responses of rank 4, and axes plus
pair sums of rank 10 for a general symmetric four-dimensional metric. Run:

```bash
python3 tests/du_common_view_closure_probe.py --write-artifact
```

The deterministic artifact is
`artifacts/du_common_view_closure_result.json`. Passing establishes only the
finite relationship, factorization, and nonselection controls. It does not
establish four fundamental degrees, a selected view family or metric,
computational ontology, or new physics.

## Computation-first hypothesis portfolio contract

`du_computation_first_portfolio_contract_probe.py` validates the conditional
closed-transition portfolio without treating it as scientific evidence. It
checks eight unique hypothesis families, twenty unique computational lenses,
exactly forty lens-to-hypothesis mappings, complete absorber/falsifier/grade
fields, an acyclic dependency graph, complete five-position coverage, and one
sole executable next action. Run:

```bash
python3 tests/du_computation_first_portfolio_contract_probe.py --write-artifact
```

The deterministic receipt is
`artifacts/du_computation_first_portfolio_contract_result.json`. Passing proves
only portfolio completeness and routing integrity. It does not establish that
reality is computation, promote any hypothesis, select a physical interface,
or claim new physics.

## HC-DU-205 record-algebra / consumer-action selector frontier

`du_record_action_selector_frontier_probe.py` checks that one reversible
binary writer and one formed sharp record support four record-preserving
consumer policies with four different target responses. It proves that the
inverse write erases the carrier without selecting the consumer, checks all
eight matched/unmatched binary relabeling cases, and validates the three
selector-mechanism dispositions against banked artifacts. Run:

```bash
python3 tests/du_record_action_selector_frontier_probe.py --write-artifact
```

The deterministic receipt is
`artifacts/du_record_action_selector_frontier_result.json`. Passing proves
only the exact finite consumer-freedom, inverse-write, matched-descent, and
artifact-consistency boundaries. It does not select a physical handoff,
establish a universal no-go, compose regional finality, or claim new physics.

## HC-DU-204 record-consumer diagonal descent

`du_record_consumer_diagonal_descent_probe.py` checks the coordinated versus
unmatched handoff boundary. It exhausts six stochastic re-encodings, `1,296`
deterministic encoder/policy/permutation cases, all `24` Pauli-label
permutations, and all six QEC-status permutations. It verifies exact matched
descent, the reachable-policy stabilizer criterion, Bell action-family
contraction, the QEC action/timing split, and consistency with the banked
source-audit artifacts. Run:

```bash
python3 tests/du_record_consumer_diagonal_descent_probe.py --write-artifact
```

The deterministic receipt is
`artifacts/du_record_consumer_diagonal_descent_result.json`. Passing proves
only the finite composition and artifact-consistency boundaries. It does not
validate either experiment, select a physical producer/consumer from bare
dynamics, establish per-attempt actuation, compose regional finality, or claim
new physics.

## HC-DU-203 Bell prescription/execution boundary

`du_bell_prescription_execution_probe.py` exhausts the four ideal Pauli
branches and all three traceless Pauli observables. It verifies that ignoring
a uniform Bell label depolarizes the target, active branchwise correction
restores it, record-conditioned terminal Pauli-frame interpretation recovers
compatible measurement statistics, and a fixed continuation that ignores the
record fails on an explicit hostile witness. Run:

```bash
python3 tests/du_bell_prescription_execution_probe.py --write-artifact
```

The deterministic receipt is
`artifacts/du_bell_prescription_execution_result.json`. Passing establishes
only the ideal Pauli algebra and the prescription/execution/deferred-terminal
boundary. It does not validate the source experiment, infer a physical Pauli
gate or adaptive controller, select an observer/continuation algebra, establish
arbitrary downstream capability, or claim new physics.

## HC-DU-201 heralded Bell-record capability quotient

`du_heralded_bell_record_capability_probe.py` reconstructs the eight-outcome
truth table of the source-pinned trapped-ion/photonic full Bell measurement.
It proves that the raw record `(passage, herald, atom)` factors through the
minimal two-bit action quotient `(passage, herald XOR atom)`, checks every raw
coordinate-deletion control, derives the ideal Haar-average fidelity loss when
either actionable bit is erased, and keeps three source-reported success
denominators separate when computing retry horizons. Run:

```bash
python3 tests/du_heralded_bell_record_capability_probe.py --write-artifact
```

The deterministic receipt is
`artifacts/du_heralded_bell_record_capability_result.json`. Passing establishes
only the finite ideal quotient, its action-relative minimality, and the stated
retry arithmetic. It does not validate the source experiment, select the
apparatus or record interface, prove single-world actualization, reconstruct
rejected-attempt lineage, distinguish quantum ontologies, or establish new
physics.

## HC-DU-202 action-family record selection

`du_action_family_record_selection_probe.py` exhausts all `4,140` partitions
of the eight-outcome HC-DU-201 Bell carrier and all `64` subsets of a frozen
six-task family. It independently checks the already banked `HC-DU-163`
coarsest action-relative quotient and monotone-refinement result, then adds the
source-grounded Bell specialization: correction plus either independent audit
bit restores the full carrier, exact Blackwell-style decision witnesses, and
the bare-carrier relabeling obstruction. Run:

```bash
python3 tests/du_action_family_record_selection_probe.py --write-artifact
```

The deterministic receipt is
`artifacts/du_action_family_record_selection_result.json`. Passing proves only
the finite partition, rank, naturality, and decision controls. It does not
select a physical task/continuation family, validate the source experiment,
establish ontology priority, or predict new physics.

`du_phenomenon_capability_atlas_probe.py` validates the completed, non-routing
Phenomenon-to-Capability Atlas v0.1. It checks the strict schema marker; six-card
bounded denominator; immutable, content-addressed source bindings; the guard
against casting Geometric Unity requirement rows as phenomena; the seven-stage
record ladder; physical observer profiles; matched P2C transition contrasts;
normalized capability; TaF projection/finality gates; Temporal Issuance
independence; structural provenance; evidence ceilings; and global nonclaims.
It also rejects 16 planted mutations covering category collapse, hidden
resources, false finality/issuance, geometry laundering, stale source custody,
and exhaustive-coverage inflation. Run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 tests/du_phenomenon_capability_atlas_probe.py
```

The deterministic receipt is
`artifacts/du_phenomenon_capability_atlas_result.json`. Passing establishes
source/provenance and representation integrity only. It does not validate the
physics summaries, novelty, ontology, a capability or finality law, paper
readiness, live routing, or permission to expand the catalog.

`du_phenomenon_capability_atlas_v02_probe.py` validates the additive,
non-routing v0.2 first run. It uses a fail-closed standard-library evaluator for
the exact JSON Schema vocabulary in the four v0.2 schemas, then checks
claim-level independent physics grounding, distinct review axes, the canonical
record vocabulary and relation DAG, typed capability projections, challenge
semantics, the 39-row source-first xenon adjudication, and the
superconducting-ring composition/source-closure failure. Its hostile suite also
proves that the core card schema accepts a synthetic additional ID while the
frozen release rejects it; no seventh card is published. Run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -S tests/du_phenomenon_capability_atlas_v02_probe.py
```

The deterministic receipt is
`artifacts/du_phenomenon_capability_atlas_v02_result.json`. Passing validates
the declared structure and source custody only. It does not establish accepted
physics beyond the pinned sources, blind independence, GU source closure,
finality, issuance, novelty, routing, or authority to expand the denominator.
The frozen first-run receipt covers four instances, 31 semantic invariants, and
36/36 rejected hostile mutations.

`du_physical_descent_ten_swing_campaign_probe.py` is a method/governance
check. It verifies that the physical-descent campaign contains ten ordered
and complete swing cards; preserves the Science Council, triple-diamond,
counterfactual, naturality, control, adjoint, value-of-information,
gauge/QFT, direct-action, metrology, adversarial, and overbuild-protection
lenses; permits only Swing 1 before a typed return; and matches either its
live `CURRENT-RESEARCH.yaml` execution packet or its governed additive
disposition. Run with
`--write-artifact` only when intentionally refreshing its deterministic
receipt. Passing establishes campaign completeness and routing only, never
physics, novelty, a theorem, a prediction, paper readiness, hardware
authorization, or permission to execute Swings 2--10.

`du_agent_orientation_contract_probe.py` is the exception in kind: it is a
deterministic governance/cold-start contract rather than a scientific assay.
It parses `../CURRENT-RESEARCH.yaml` as the sole mutable research authority;
enforces either one active scientific flagship with one executable action or
an explicit no-ready quiescent state with neither; also enforces one separately
typed prepared publication candidate, parked-work reopeners, WIP limits, typed
dependency target namespaces, normalized lanes and grades, acyclicity,
evidence-reference integrity, the conditional execution-packet contract, and
an unselected successor. It validates `../CURRENT-RESEARCH.schema.json`; checks that
`../LANES.yaml` contains only stable lane/channel/grade topology and the
canonical structured charter; rejects copied live-routing assertions; verifies
charter parity, run-home semantics, historical guards, entrypoint links, and a
bounded context-isolated cold start. It also requires independent
perspective/scope, ontic/epistemic, and disclosure/issuance coordinates across
the cold-start, durable-program, foundations, and concept surfaces; one
negative mutation per surface proves those markers are load-bearing. Its
positive control mutates all current program/action/publication identifiers in
memory and reruns the unchanged validator, proving current IDs are data rather
than validator code. Use
`--write-artifact` only when intentionally refreshing the compact deterministic
receipt. Passing establishes routing integrity only, never physics, ontology,
novelty, or paper readiness.

`du_near_term_swing_approach_atlas_probe.py` is another method/governance
check rather than a scientific assay. It verifies that the five-lens
near-term approach atlas contains 15 complete approach cards; covers all 27
paper candidates exactly once and every active dependency lane; retains
ownership, merge, dependency and no-reopen boundaries; reuses the existing
36-hypothesis method registry; preserves the nearer-paper versus flagship
distinction; and confirms that the dated atlas remains non-authoritative under
the current-research migration. Passing establishes coverage and historical
method integrity only. It does not validate an approach scientifically, rank
a swing, authorize work, change Factory state, harden a manuscript, or
establish publication readiness.

## HC-DU-110 conformal null-front transfer and scale-anchor gate

`du_conformal_null_front_transfer_scale_anchor_probe.py` preserves the exact
finite controls behind the conformal-transfer result:

- all four fixed phase covectors remain null under several positive Weyl
  factors;
- the same phase code recovers the same coordinate events throughout the
  conformal family;
- the conformal-wave, field, quadratic-coupling, and source weights all match;
- an explicit interior witness changes metric scale and coupling while the
  boundary conjugacy is the identity;
- holding the quadratic coefficient fixed produces the exact one-factor
  covariance mismatch; and
- breaking that gauge is recorded as necessary but not sufficient for metric
  injectivity.

Run:

```bash
python3 tests/du_conformal_null_front_transfer_scale_anchor_probe.py
```

The deterministic receipt is
`artifacts/du_conformal_null_front_transfer_scale_anchor_result.json`.
Passing establishes only the scoped conformal null-front/event-control
transfer, metric/coupling gauge, and fixed-coefficient scale-anchor boundary.
It does not establish fundamental scalar dynamics, physical source formation,
a nonzero four-wave symbol, selected coupling, source timing, provenance,
complete acquisition, full-metric reconstruction, new physics, prediction,
paper, model, hardware, provider, publication, or other external action.

## HC-DU-111 order-plus-volume metric reconstruction gate

`du_order_volume_metric_reconstruction_probe.py` preserves the exact finite
controls behind the volume-anchor result:

- four-dimensional cell volume exactly recovers piecewise-constant conformal
  scale by a positive fourth root;
- metric determinant scaling supplies an independent algebraic control;
- bounded relative volume error has an explicit relative-scale bound;
- volume is additive under benign partition refinement;
- duplicate occurrence identities defeat naive count additivity;
- known Poisson density gives quantified count and scale resolution;
- unknown global density leaves an exact absolute-scale gauge while preserving
  relative scale;
- unknown regional density absorbs arbitrary local factors; and
- equal cell integrals can hide different smooth conformal factors.

Run:

```bash
python3 tests/du_order_volume_metric_reconstruction_probe.py
```

The deterministic receipt is
`artifacts/du_order_volume_metric_reconstruction_result.json`.
Passing establishes only the scoped conformal-class-plus-volume
reconstruction and density/provenance/acquisition boundaries. It does not
select a physical volume measure, fundamental event density, formed count
record, complete acquisition, metric-independent partition, unrestricted
smooth metric, new physics, prediction, paper, model, hardware, provider,
publication, or other external action.

## HC-DU-112 complete causal-set scale-gauge gate

`du_causal_set_full_law_scale_gauge_probe.py` preserves the exact finite
controls behind the complete-law result:

- compensated metric-density rescaling preserves the exact Poisson intensity
  measure;
- representative joint count probabilities, not merely their means, agree;
- positive constant Weyl scaling preserves the causal order;
- representative unmarked graph summaries remain unchanged;
- free regional density absorbs local conformal scale;
- volume ratios and curvature in discreteness units remain invariant;
- a fixed known dimensionful pair mark breaks the scale gauge and
  conditionally reconstructs selected proper-time intervals; and
- an inversely covarying mark parameter restores the gauge.

Run:

```bash
python3 tests/du_causal_set_full_law_scale_gauge_probe.py
```

The deterministic receipt is
`artifacts/du_causal_set_full_law_scale_gauge_result.json`.
Passing establishes only the scoped complete-law scale nonidentifiability and
fixed-versus-covarying anchor controls. It does not select a physical density,
dimensionful mark, clock, mass, interface, formation, provenance, access,
certified record, new physics, prediction, paper, hardware, provider,
publication, or other external action.

## HC-DU-113 QCD dimensional-transmutation scale gate

`du_qcd_dimensional_transmutation_scale_gate_probe.py` preserves the exact
finite controls behind the scale-provenance result:

- one-loop asymptotically free flow reconstructs one invariant
  \(\Lambda\) along each trajectory;
- the beta law leaves the trajectory's integration constant free;
- specifying one reference coupling and specifying \(\Lambda\) are
  equivalent;
- a common energy-unit rescaling preserves the running;
- a one-loop finite scheme shift rescales \(\Lambda\) while physical masses
  and ratios remain invariant;
- lattice mass products require one measured reference mass to fix physical
  units;
- a fixed physical matter mark breaks the metric-scale gauge and
  conditionally reconstructs selected proper times;
- joint rescaling of the metric and every admitted dimensional scale is a
  common-unit gauge;
- holding another sector fixed changes a physical dimensionless ratio; and
- unequal local metric factors require forbidden local matter-law refit.

Run:

```bash
python3 tests/du_qcd_dimensional_transmutation_scale_gate_probe.py
```

The deterministic receipt is
`artifacts/du_qcd_dimensional_transmutation_scale_gate_result.json`.
Passing establishes only the scoped RG scale-provenance, lattice-matching,
common-unit, and fixed-matter-anchor controls. It does not prove a QCD mass
gap, select a Standard-Model parameter, form a physical clock or record,
establish provenance/access, reconstruct nature's metric, introduce new
physics, or authorize a prediction, paper, hardware, provider, publication,
or other external action.

## HC-DU-114 Multi-standard clock metric--matter rank gate

`du_multistandard_clock_metric_matter_rank_probe.py` preserves:

- an exact one-clock same-record/different-redshift witness when one
  matter-law nuisance is admitted;
- conditional one-clock reconstruction when that matter law is frozen;
- the minimum two-distinct-sensitivity repair for one nuisance;
- the failure of repeated identical species to add attribution rank;
- cancellation of metric common mode in clock ratios;
- a full-rank three-species redshift/alpha/mass-ratio control;
- the two-clock/two-nuisance dimension deficit;
- the exact universal-frequency-drift/redshift confounding witness; and
- inverse-error amplification for nearly parallel sensitivities.

Run:

```bash
python3 tests/du_multistandard_clock_metric_matter_rank_probe.py
```

The deterministic receipt is
`artifacts/du_multistandard_clock_metric_matter_rank_result.json`.
Passing establishes only the finite linear rank, kernel, and conditioning
controls. It does not select or form physical clocks, transport or compare
them, join their archives, establish provenance/access, warrant an
unrestricted nuisance class, reconstruct nature's metric, introduce new
physics, or authorize a prediction, paper, hardware, provider, publication,
or other external action.

## HC-DU-115 Haag/direct-action interface fork

`du_mediator_elimination_interface_fork_probe.py` preserves:

- exact stationary elimination of a finite quadratic mediator;
- equality of the explicit-mediator and effective source-only actions;
- equality of their source-response maps;
- exact one- and two-channel factorizations of the same scalar source kernel;
- different candidate channel weights under those source-equivalent
  factorizations;
- one mediator-facing action direction invisible to the original source; and
- the need to supply a factorization before reconstructing mediator
  coordinates.

Run:

```bash
python3 tests/du_mediator_elimination_interface_fork_probe.py
```

The deterministic receipt is
`artifacts/du_mediator_elimination_interface_fork_result.json`.
Passing establishes only the finite Schur-complement, query-relative
equivalence, factorization non-identifiability, and action-class enlargement
controls. It does not establish QED/AQFT/direct-action equivalence, resolve
Haag's theorem, select absorbers, validate RTI, cause collapse, form an event
or record, select ontology, isolate empirical excess, introduce new physics,
or authorize a prediction, paper, hardware, provider, publication, or other
external action.

## HC-DU-116 background-natural mediator elimination

`du_background_natural_mediator_elimination_probe.py` preserves:

- the exact on-shell envelope identity for a background-dependent quadratic
  mediator;
- a same-frozen-source-action/different-background-derivative
  counterexample;
- equality of total source response for one- and two-channel completions with
  the same complete parameter-dependent source kernel;
- non-identifiability of the local mediator-response partition; and
- the exact background derivative of a source-independent Gaussian
  determinant.

Run:

```bash
python3 tests/du_background_natural_mediator_elimination_probe.py
```

The deterministic receipt is
`artifacts/du_background_natural_mediator_elimination_result.json`.
Passing establishes only the finite variational identity,
pointwise-versus-background-natural equivalence boundary, local-partition
non-identifiability, and determinant-response control. It does not establish
gravity or QFT equivalence, select a metric or stress tensor, fix
renormalization, form a record, select ontology, isolate empirical excess,
introduce new physics, or authorize a prediction, paper, hardware, provider,
publication, or other external action.

## HC-DU-117 relative-entropy and index-descent admission

`du_relative_entropy_index_descent_admission_probe.py` preserves:

- exact KL preservation and recovery for a statistically sufficient record
  with a parameter-independent hidden conditional;
- positive full-state divergence and zero record divergence for an
  insufficient constant quotient;
- one reconstructable and one unreconstructable target under the same lossy
  record;
- invariance under bijective relabeling; and
- equal positive source kernels with opposite determinant orientations.

Run:

```bash
python3 tests/du_relative_entropy_index_descent_admission_probe.py
```

The deterministic receipt is
`artifacts/du_relative_entropy_index_descent_admission_result.json`.
Passing establishes only the finite classical sufficiency, target-relative
factorization, and determinant-orientation-loss controls. It does not
implement Araki relative entropy or a type-III algebra, select a physical
record channel, derive capacity or Landauer's law, model GU, establish an
index/torsion descent theorem, isolate empirical excess, introduce new
physics, or authorize a prediction, paper, hardware, provider, publication,
or other external action.

## HC-DU-118 local-QFT record-algebra selection

`du_local_qft_record_algebra_selection_probe.py` preserves:

- three distinct record channels induced by reversible couplings in the same
  finite system--probe arena;
- equality of every proper-local marginal for a full-support parity pair;
- an extended parity target with expectations \(+1/2\) and \(-1/2\);
- exact full divergence \((1/2)\log 3\) and zero divergence on every proper
  restriction; and
- two idempotent group averages that differ because their supplied
  \(\mathbb Z_2\) actions differ.

Run:

```bash
python3 tests/du_local_qft_record_algebra_selection_probe.py
```

The deterministic receipt is
`artifacts/du_local_qft_record_algebra_selection_result.json`.
Passing establishes only the finite realizability-versus-selection,
proper-local/extended-target, access-retyping, and relative conditional-
expectation controls. It does not model QFT or a type-III algebra, implement a
Fewster--Verch instrument, select a physical observable net or record channel,
prove formation, retention, provenance, or observer access, isolate empirical
excess, introduce new physics, or authorize a prediction, paper, hardware,
provider, publication, or other external action.

## HC-DU-119 Wilson-loop access/finality trichotomy

`du_wilson_loop_access_finality_probe.py` preserves:

- an exact three-share cat-ancilla parity protocol whose complete output
  reconstructs the extended target while every proper share subset is
  target-blind;
- equality of that protocol's nonselective channel with the parity Lüders
  channel on every computational matrix unit;
- preservation of within-parity coherence and removal of cross-parity
  coherence;
- strict refinement and additional disturbance under complete local data
  readout;
- equality of the ideal parity instrument produced by a sequential coherent
  ancilla under a different route/resource contract; and
- singleton conjugacy-class multiplication for \(\mathbb Z_2\) versus
  identity/three-cycle product ambiguity for the transposition class of
  \(S_3\).

Run:

```bash
python3 tests/du_wilson_loop_access_finality_probe.py
```

The deterministic receipt is
`artifacts/du_wilson_loop_access_finality_result.json` and reports `11/11`.
Passing establishes only the finite threshold-record, nondemolition versus
destructive, route/resource, and Abelian/non-Abelian algebraic-hinge
controls. It does not simulate gauge theory, prove the relativistic Wilson-
loop causality theorem, select a physical measurement apparatus, establish
authentication or Byzantine finality, isolate empirical excess, introduce
new physics, or authorize a prediction, paper, hardware, provider,
publication, or other external action.

## HC-DU-120 generalized-symmetry access/resource classification

`du_generalized_symmetry_access_resource_probe.py` preserves:

- exact finite-Abelian total-charge share laws for
  \(\mathbb Z_2,\mathbb Z_3,\mathbb Z_4\), and
  \(\mathbb Z_2\times\mathbb Z_2\);
- exact joined-share reconstruction and target blindness of every proper
  share subset;
- equality of the character-GHZ protocol with the total-charge Lüders channel
  on every computational matrix unit;
- \(|G|\) equal Schmidt probabilities for every charge-sector output and
  every nontrivial party cut;
- the \(\log_2|G|\) cutwise entanglement lower bound supplied by LOCC
  monotonicity; and
- equality of that lower bound with the character-GHZ resource entropy.

Run:

```bash
python3 tests/du_generalized_symmetry_access_resource_probe.py
```

The deterministic receipt is
`artifacts/du_generalized_symmetry_access_resource_result.json` and reports
`12/12` over five specimens. Passing establishes only the finite-Abelian
group/channel/Schmidt controls. The LOCC necessity step uses standard
entanglement monotonicity. The probe does not model QFT, AQFT, SymTFT, gauge
theory, or a relativistic detector; prove a universal generalized-symmetry
access classification; select an apparatus or resource; isolate empirical
excess; introduce new physics; or authorize a prediction, paper, hardware,
provider, publication, or other external action.

## HC-DU-121 finite-Abelian lattice-gauge QND transfer

`du_finite_abelian_gauge_qnd_transfer_probe.py` preserves the exact
matter-completed lattice-gauge transfer:

- gauge invariance of
  \(Y_{vw}=-\phi_v+U_{vw}+\phi_w\);
- bijection between complete dressed-link tuples and gauge orbits;
- reachability and independence of every \(G^E\) physical tuple;
- physical-basis factorization over the dressed links;
- telescoping equality between the dressed-link sum and Wilson holonomy;
- equality with the unchanged total-charge Lüders channel;
- proper-share blindness and exact joined reconstruction; and
- transfer of the matching \(\log_2|G|\) ancillary-entanglement lower and
  upper bounds.

Run:

```bash
python3 tests/du_finite_abelian_gauge_qnd_transfer_probe.py
```

The deterministic receipt is
`artifacts/du_finite_abelian_gauge_qnd_transfer_result.json` and reports
`14/14` over five specimens. Passing establishes only the exact finite
orbit/channel/resource regression under supplied regular-representation
matter and dressed-link access. It is not a dynamical or continuum
lattice-gauge simulation; a pure-gauge, continuous-group, non-Abelian, AQFT,
or universal QFT theorem; selection of matter, apparatus, stations, or
access; a complete energy or implementation cost; empirical excess; new
physics; or authorization for a prediction, paper, hardware, provider,
publication, or other external action.

## HC-DU-122 Wilson-record capability first leak

`du_wilson_record_capability_first_leak_probe.py` preserves the exact
capability-relative factorization theorem in the unchanged `HC-DU-121`
dressed-link basis:

- a path response factors through the formed Wilson record iff all
  coefficient multiplication endomorphisms agree on \(G\);
- every closed-loop winding response factors exactly;
- every proper simple matter-completed open path leaks;
- the smallest same-record/different-response witness changes two links;
- every Wilson fibre has \(|G|^{n-1}\) basis completions; and
- \(n-1\) additional \(G\)-valued coordinates are necessary and sufficient
  to complete all path responses.

Run:

```bash
python3 tests/du_wilson_record_capability_first_leak_probe.py
```

The deterministic receipt is
`artifacts/du_wilson_record_capability_first_leak_result.json` and reports
`14/14` over five finite-Abelian specimens. Passing is only a bounded exact
regression of the algebraic proof. It does not establish unrestricted
quantum-state reconstruction, select the finer interface, prove the repair
is nondemolition, transfer beyond the regular-matter finite-Abelian cycle,
produce empirical excess, or authorize a prediction, paper, hardware,
provider, publication, or other external action.

## HC-DU-123 graph-cycle cohomology and min-cut first leak

`du_graph_cycle_record_cohomology_probe.py` preserves the exact arbitrary-
graph generalization in the unchanged matter-completed finite-Abelian arena:

- a complete fundamental-cycle record has kernel equal to the coboundaries;
- its quotient is \(H^1(\Gamma;G)\) and its equivalence is spanning-tree
  invariant;
- an edge-chain response factors iff its vertex boundary annihilates \(G\);
- every ordinary closed chain reconstructs and every simple open path leaks;
- the minimum endpoint-leak support equals endpoint edge connectivity;
- each record fibre has \(|G|^{|V|-1}\) basis states; and
- \(|V|-1\) additional \(G\)-valued tree coordinates are necessary and
  sufficient to complete every path response.

Run:

```bash
python3 tests/du_graph_cycle_record_cohomology_probe.py
```

The deterministic receipt is
`artifacts/du_graph_cycle_record_cohomology_result.json` and reports `18/18`
over five trees/cycles/bridged/multiply-connected graph specimens. Passing is
only a bounded exact regression of the graph proof. It does not select the
graph, spanning tree, cycle instrument, matter, observer, or action class;
derive a joint resource law; establish unrestricted state reconstruction;
transfer to non-Abelian, continuous, higher-cell, AQFT, or continuum
theories; produce empirical excess; or authorize a prediction, paper,
hardware, provider, publication, or other external action.

## HC-DU-124 regional cycle-record gluing

`du_regional_cycle_record_gluing_probe.py` preserves the exact two-region
Mayer--Vietoris specialization in the unchanged matter-completed
finite-Abelian graph arena:

- connected overlap makes compatible complete local cycle records determine
  the global cycle class uniquely;
- an overlap with \(k\) connected components leaves exactly
  \(|G|^{k-1}\) global cycle classes per compatible local-record pair;
- \(k-1\) explicit cross-region cycle values are necessary and sufficient to
  complete the global class under a \(G\)-coordinate contract;
- overlap connectivity, not overlap vertex count, controls the deficit;
- the graph cycle ranks obey
  \(\beta_1(\Gamma)=\beta_1(A)+\beta_1(B)-\beta_1(I)+(k-1)\);
- each local-record fibre still contains
  \(|G|^{|V|+k-2}\) physical dressed-edge states; and
- cross-cycle values plus \(|V|-1\) spanning-tree values attain the minimum
  universal full-state coordinate count.

Run:

```bash
python3 tests/du_regional_cycle_record_gluing_probe.py
```

The deterministic receipt is
`artifacts/du_regional_cycle_record_gluing_result.json` and reports `17/17`
over five connected/disconnected/cyclic-overlap finite covers. Passing is
only a bounded exact regression of the standard gluing proof. It does not
select the regions or record interfaces; establish formation, provenance,
access, verification, BFT, public finality, consensus, or a resource law;
transfer to many-region, non-Abelian, continuous, higher-cell, AQFT, or
continuum theories; produce empirical excess; or authorize a prediction,
paper, hardware, provider, publication, or other external action.

## HC-DU-125 homomorphic cycle-record formation and direct-action descent

`du_cycle_record_formation_direct_action_probe.py` preserves four exact
finite boundaries:

- for any tested finite-Abelian homomorphism \(Q\), the uniform
  \(\ker Q\) ancillary state plus local controlled addition implements the
  exact selective Lüders instrument without within-fibre dephasing;
- each station subset's raw transcript reveals exactly its projected-kernel
  quotient, while joined regional correlations retain the cross-region
  gluing sector;
- the uniform-kernel state's Schmidt rank across \(S:\bar S\) is
  \(|\operatorname{im}Q_S\cap\operatorname{im}Q_{\bar S}|\), giving a
  matching cutwise LOCC lower bound and construction;
- for complete graph-cycle records, the resource exponent is
  \(|V|-c(S)-c(\bar S)+1\), the graphic-matroid connectivity function; and
- an exact star--triangle Schur complement gives one source kernel with
  interaction-graph cycle ranks zero and one, so a mediator-cycle record
  does not automatically descend to direct source action.

Run:

```bash
python3 tests/du_cycle_record_formation_direct_action_probe.py
```

The deterministic receipt is
`artifacts/du_cycle_record_formation_direct_action_result.json` and reports
`24/24` over three homomorphic, four graph, three regional, and one
star--triangle specimen. Passing is only a bounded exact regression of the
analytic proof. It does not select a homomorphism, graph, matter sector,
station factorization, resource, record interface, field or direct-action
ontology, absorber or RTI event rule; establish public finality or a complete
cost law; transfer to non-Abelian, continuous, AQFT, or continuum theories;
produce empirical excess; or authorize a prediction, paper, hardware,
provider, publication, or other external action.

## HC-DU-126 source-action response record and mediator fibre

`du_source_action_response_record_probe.py` preserves four exact finite
reciprocal-network boundaries:

- Schur/Kron elimination leaves the complete labeled boundary
  Dirichlet-to-Neumann operator unchanged;
- with \(b\) boundary terminals, \(b-1\) fixed independent potential probes
  with joined current-vector output are necessary and sufficient to
  reconstruct every held-out source response without refit;
- an interface returning only scalar action values instead needs
  \(n(n+1)/2\) fixed queries, where \(n=b-1\); and
- one complete three-terminal source response has positive simple mediator
  completions of every finite cycle rank, so internal topology does not
  factor through source-only behavior.

Run:

```bash
python3 tests/du_source_action_response_record_probe.py
```

The deterministic receipt is
`artifacts/du_source_action_response_record_result.json` and reports
`21/21` over six reconstruction specimens, exact full-rank and
rank-deficient controls, two scalar-interface controls, one robustness
comparison, and nine source-equivalent topology specimens. Passing is only
a bounded exact regression of standard response-map, Schur-complement, and
linear-identification mathematics. It does not select a probe, readout,
archive, observer, access boundary, field or direct-action ontology; turn
source-query operational duality into ontology equivalence; transfer to
continuum, QFT, gravity, nonreciprocal, or nonlinear systems; produce
empirical excess; or authorize a prediction, paper, hardware, provider,
publication, or other external action.

## HC-DU-127 pairing-complete dual-valued source response

`du_pairing_complete_source_response_probe.py` preserves the exact finite
controls behind the pairing-complete response theorem:

- two normalized signature-\((1,1)\) pairings with the same bare operator
  produce different dual-valued responses \(C=KM\);
- two same-signature packets produce the same \(C\) while their bare
  operators respectively commute and anticommute with one grading;
- the exact family
  \(K_n=\left(\begin{smallmatrix}n&1\\1&0\end{smallmatrix}\right)\),
  \(M_n=\left(\begin{smallmatrix}1&0\\-n&1\end{smallmatrix}\right)\)
  has \(K_nM_n\) constant for every integer \(n\);
- scalar quadratic values erase the antisymmetric part while polarization
  exactly reconstructs a symmetric response; and
- incomplete source or readout spans admit a fixed held-out first leak,
  whereas complete basis queries reconstruct \(C\).

Run:

```bash
python3 tests/du_pairing_complete_source_response_probe.py
```

The deterministic receipt is
`artifacts/du_pairing_complete_source_response_result.json` and reports
`26/26`. Passing is only a bounded exact regression of standard finite
duality, polarization, congruence, and indefinite-pairing mathematics. It
does not select a physical pairing, domain, adjoint, Green form, source
basis, probe, readout, archive, observer, field/direct-action ontology, or
GU construction; transfer to unbounded operators, QFT, or gravity; produce
empirical excess; or authorize a prediction, paper, hardware, provider,
publication, or other external action.

## HC-DU-128 positive-functional QFT reconstruction boundary

`du_positive_functional_qft_reconstruction_probe.py` preserves the exact
finite controls behind the positive-functional reconstruction boundary:

- one commutative Walsh star algebra and one noncommutative real matrix star
  algebra share the same state coordinates and identity two-point GNS Gram
  matrix but have opposite held-out triple expectation;
- within each fixed packet, left multiplication is a cyclic star
  representation and reconstructs the declared finite algebra;
- a normalized nonpositive functional has an exact negative-norm witness and
  cannot produce an ordinary Hilbert GNS packet;
- a nonfaithful positive state has a left-invariant null ideal and a
  one-dimensional quotient; and
- for every retained moment order \(0\) through \(6\), two strictly positive
  finite-support states agree through that order and differ at the next.

Run:

```bash
python3 tests/du_positive_functional_qft_reconstruction_probe.py
```

The deterministic receipt is
`artifacts/du_positive_functional_qft_reconstruction_result.json` and reports
`27/27`. Passing is a bounded exact regression of standard finite GNS,
star-algebra, positivity, null-quotient, moment, and finite-difference
mathematics. It does not establish Wightman/OS reconstruction by computation;
select an observable algebra, product, involution, state, spacetime,
source/test structure, record interface, observer, archive, or access
boundary; turn an infinite theoretical functional into a finite formed
record; transfer ordinary positivity to indefinite/Krein or GU structure;
produce empirical excess, a new law, new physics, or a prediction; or
authorize a paper, model, hardware, provider, publication, or other external
action.

## HC-DU-129 Gaussian finite-record ladder

`du_gaussian_finite_record_ladder_probe.py` preserves the exact controls
behind the Gaussian population/finite-shot boundary:

- for one through four modes, the
  \(n(2n+1)\) coordinate and pair-quadrature directions have complete exact
  covariance rank and reconstruct a supplied physical covariance;
- removing one direction leaves two strictly physical covariances with every
  retained variance equal and the held-out variance different;
- two different iid transcripts share the exact Gaussian likelihood-sufficient
  tuple \((N,\sum x,\sum x^2)\);
- one finite binned transcript has positive probability under two distinct
  physical Gaussian variances;
- the one-photon Fock state and mean-occupation-one thermal Gaussian share
  first moments and covariance while differing in fourth moment and number
  variance; and
- the conservative concentration formula produces finite declared-resolution
  sample budgets without simulation.

Run:

```bash
python3 tests/du_gaussian_finite_record_ladder_probe.py
```

The deterministic receipt is
`artifacts/du_gaussian_finite_record_ladder_result.json` and reports `33/33`.
Passing is a bounded exact regression of standard covariance tomography,
Gaussian likelihood, concentration, and moment mathematics. It does not
select the mode algebra, symplectic form, Gaussian class, Hamiltonian, state,
detector, digitization, observer, archive, access boundary, or target; prove
exact state determination from finite shots; transfer to continuum QFT,
non-Gaussian states, or GU/Krein theory; produce empirical excess, a new law,
new physics, or a prediction; or authorize a paper, model, hardware, provider,
publication, or other external action.

## HC-DU-130 covariant local finite-mode trilemma

`du_covariant_local_finite_mode_trilemma_probe.py` preserves the exact
controls behind the continuum packet boundary:

- compactly supported translated bumps with pairwise disjoint support have
  exact full orbit rank for tested packet sizes;
- a region-indexed finite local packet family obeys translation covariance;
- one fixed local packet changes under a sufficiently large translation;
- finite cyclic arenas retain finite local translation orbits, while character
  lines are finite and invariant but global;
- arbitrary retained Gaussian packet sizes can agree exactly while one hidden
  oscillator has different vacuum and thermal covariance; and
- an inside target agrees while a held-out Weyl target on the complementary
  mode differs.

Run:

```bash
python3 tests/du_covariant_local_finite_mode_trilemma_probe.py
```

The deterministic receipt is
`artifacts/du_covariant_local_finite_mode_trilemma_result.json` and reports
`36/36`. Passing is a bounded exact regression of the disjoint-translate
proof, indexed-family repair, periodic/nonlocal escapes, and Gaussian
restriction first leak. It does not select a mode family, state, algebra,
detector, observer, interface, compactification, QFT, empirical excess, new
law, new physics, or prediction; transfer the raw test-function result to
every on-shell quotient, net algebra, or interacting theory; or authorize a
paper, model, hardware, provider, publication, or other external action.

## HC-DU-131 AQFT nuclearity finite-resolution boundary

`du_aqft_nuclearity_finite_resolution_boundary_probe.py` preserves the exact
controls behind the nuclear finite-resolution/exact finite-record boundary:

- the infinite-rank diagonal map \(De_j=2^{-(j+1)}e_j\) has nuclear norm one;
- its finite-rank truncations have exact nuclear and operator tail bounds;
- every tested finite truncation admits a same-record/different-tail target
  witness saturating the \(2L\eta\) bound;
- genuinely finite-rank diagonal maps close exactly when every nonzero
  coordinate is retained;
- the zero and full-multiplet projectors commute with the rotation control;
  and
- four rank-one orthogonal projectors fail rotation equivariance.

Run:

```bash
python3 tests/du_aqft_nuclearity_finite_resolution_boundary_probe.py
```

The deterministic receipt is
`artifacts/du_aqft_nuclearity_finite_resolution_boundary_result.json` and
reports `38/38`. Passing is a bounded exact regression of standard nuclear
tails, finite-rank factorization, target-error, and symmetry-commutant
mathematics. It does not construct or simulate an AQFT; prove nuclearity for
every QFT; select a QFT, local algebra, region, state, Hamiltonian, damping
scale, finite approximant, probe, detector, observer, archive, access
boundary, or target; establish exact finite continuum reconstruction;
produce empirical excess, a new law, new physics, or a prediction; or
authorize a paper, model, hardware, provider, publication, or other external
action.

## HC-DU-132 AQFT spectral cutoff and phase-space width

`du_aqft_spectral_cutoff_width_probe.py` preserves the exact finite controls
behind the Hamiltonian-cutoff and finite-probe boundary:

- for \(\beta=\log2\), every tested bounded spectral cutoff obeys the exact
  energy-damped tail bound;
- a low-energy momentum-grid rank grows strictly under refinement, explicitly
  as a regression rather than continuum evidence;
- the compact-resolvent control with spectrum \(0,1,2,\ldots\) has finite-rank
  bounded spectral projections;
- an infinite geometric diagonal map and a flat rank-eight map share nuclear
  norm one while having different Kolmogorov-width profiles;
- the geometric widths converge without terminating, while the finite-rank
  widths close exactly at rank eight; and
- width values and conditional finite-probe existence are not treated as
  coordinate or physical-interface selectors.

Run:

```bash
python3 tests/du_aqft_spectral_cutoff_width_probe.py
```

The deterministic receipt is
`artifacts/du_aqft_spectral_cutoff_width_result.json` and reports `43/43`.
Passing is a bounded exact regression of spectral-tail, refinement,
compact-resolvent, and diagonal-width controls. It does not construct or
simulate an AQFT; supply numerical evidence for an infinite continuum; prove
that every QFT has continuous low-energy spectrum; select a QFT, region, state,
cutoff, target, approximating subspace, probe, detector, observer, archive, or
access boundary; establish record formation or no-refit transfer; produce
empirical excess, a new AQFT theorem, law, physics, or prediction; or authorize
a paper, model, hardware, provider, publication, or other external action.

## Certified Causal Reality assay contract

The governing research agenda is
`../docs/certified-causal-reality-research-program.md`. A central assay must
freeze, before seeing its result:

- the complete multi-event/intervention process, primitive operational
  precedence or composition, and every supplied temporal/geometric antecedent;
- the record instrument, provenance/meta-record structure, access map, and
  representation group;
- the observer, boundary, rival/adversary class, certificate, finalizer, and
  incompatibility condition;
- the resource ledger, bounded-risk action set, nulls, held-out tests, and
  finite falsifier;
- the warrant type and local-versus-global failure scope.

Required controls distinguish endpoint equality, mean-history models,
classical random-history mixtures, coherent histories, copying or
dissemination without finality, adversarial split views, hidden schedulers,
arbitrary interfaces, and free-resource completions as relevant. A probe may
not define record equivalence by agreement under every physical experiment it
later claims to predict.

## Quantum output carrier / classical shadow gate

`du_quantum_output_record_gate_probe.py` executes the exact finite controls
for `HC-DU-075`. At amplitude-damping strength \(\gamma=1/4\), one retained
environment qubit supports:

- a counting-like \(Z\) shadow that loses an input phase-sign target;
- a homodyne-like \(X\) shadow that retains that target;
- the opposite capability ordering for a population target; and
- full-carrier Helstrom errors matching the relevant predeclared action.

The same probe checks two isometric completions of a constant-output erasure
channel. Their full complements are related by environment `SWAP`, but the
fixed accessible port carries the input in only one completion, giving
equal-prior input-bit errors \(0\) and \(1/2\). Passing establishes the
carrier/shadow type separation and access-relocation witness only. It does
not select a physical environment, prove collapse, model gravity, establish
record ontology, or warrant hardware.

## Subsystem factor selection and quantum-mereology gate

`du_subsystem_factor_selection_probe.py` executes the exact finite controls
for `HC-DU-076`:

- the nondegenerate Hamiltonian `diag(0,1,2,4)` is preserved by `CZ`;
- `CZ` moves both two-qubit factor algebras while each rotated pair still
  commutes, intersects only in scalars, and generates all of \(M_4\);
- \(|++\rangle\) has subsystem entropy \(0\) in the original TPS and \(1\)
  in the rotated TPS;
- the same full-support state breaks the `CZ` symmetry of the
  Hamiltonian--state pair;
- the polynomial orbit \(R(H)|\psi\rangle\) has full rank, validating the
  finite assumption behind the invariant-profile classifier; and
- a selected two-sector dephasing center remains insufficient to fix the
  complete tensor-factor pair.

Run:

```bash
python3 tests/du_subsystem_factor_selection_probe.py
```

The deterministic receipt is
`artifacts/du_subsystem_factor_selection_result.json` and reports `19/19`.
Passing establishes only the scoped stabilizer-orbit witness,
classification/selection boundary, and observable-algebra positive control.
It does not derive a physical TPS, record carrier, spacetime, locality,
ontology, or new quantum law.

## Commutative-record modular-time gate

`du_commutative_record_modular_time_probe.py` executes the finite controls
for `HC-DU-077`:

- the complete classical record algebra is
  \(\mathcal D=\operatorname{span}\{I,Z\}\);
- two faithful ambient states agree on every observable in \(\mathcal D\)
  while inducing different ambient modular flows;
- the tracial ambient state has trivial modular dynamics;
- the coherent ambient state moves \(Z\) outside the record algebra;
- every projector in the commutative algebra remains fixed by its intrinsic
  modular flow;
- a faithful diagonal state supplies the positive noncommutative control:
  the record algebra stays fixed while off-diagonal observables acquire the
  exact eigenvalue-ratio phase; and
- normalized powers of the state rescale the modular parameter exactly.

Run:

```bash
python3 tests/du_commutative_record_modular_time_probe.py
```

The deterministic receipt is
`artifacts/du_commutative_record_modular_time_result.json` and reports
`19/19`. Passing establishes only the finite modular-silence and
same-record/different-ambient-flow certificate. It does not select a physical
state, Type-III algebra, proper-time calibration, geometry, formed record,
ontology, or new law.

## Self-tested modular reconstruction gate

`du_self_tested_modular_reconstruction_probe.py` executes the exact finite
controls for `HC-DU-078`:

- the \(\theta=\pi/8\) tilted-CHSH strategy attains
  \(4\sqrt6/3\), its exact quantum maximum;
- under the standard self-testing theorem, the labeled conditional law
  certifies an extracted noncommutative qubit factor and the faithful
  nontracial local state
  \(\operatorname{diag}((2+\sqrt2)/4,(2-\sqrt2)/4)\);
- the resulting target-factor modular eigenvalue ratio is
  \(3+2\sqrt2\);
- erasing the setting labels admits a setting-independent classical source
  with exactly the same pooled output distribution;
- retaining the labels separates the quantum and classical conditional laws;
  and
- maximal ordinary CHSH is the null control: it certifies noncommuting Pauli
  structure while its local reduced state is tracial and modularly silent.

Run:

```bash
python3 tests/du_self_tested_modular_reconstruction_probe.py
```

The deterministic receipt is
`artifacts/du_self_tested_modular_reconstruction_result.json` and reports
`23/23`. Passing establishes the exact two-qubit arithmetic and
context-erasure counterexample only. The self-testing implication comes from
the cited theorem. The probe does not select physical ports, separation,
settings, measurement independence, acquisition, record formation, ambient
modular flow, proper-time calibration, geometry, ontology, or new physics.

## Indivisible-stochastic modular-rigidity boundary

`du_indivisible_stochastic_modular_rigidity_probe.py` executes the exact
finite controls for `HC-DU-079`:

- the complete \(\theta=\pi/8\) tilted-CHSH conditional table is encoded as
  the column-stochastic object
  \(\Gamma_{(a,b),(x,y)}=p(a,b\mid x,y)\);
- the Schur-Hadamard family
  \(\Theta_\phi=\operatorname{diag}(1,1,1,e^{i\phi})\sqrt{\Gamma}\)
  leaves every labeled transition probability and output probability fixed;
- relative to one supplied \(A\otimes B\) output factor, the reduced
  eigenvalues are
  \(1/2\pm\sqrt{6+2\cos\phi}/8\);
- the fixed-factor modular ratio therefore changes from
  \(3+2\sqrt2\) at \(\phi=0\) to \(3\) at \(\phi=\pi\);
- the endpoint phase is controlled-\(Z\), diagonal in the configuration
  basis but nonlocal relative to the supplied factor; and
- two binary full-process realizers share every base-time transition matrix
  while giving probabilities one and zero to \(X_2=X_1\).

Run:

```bash
python3 tests/du_indivisible_stochastic_modular_rigidity_probe.py
```

The deterministic receipt is
`artifacts/du_indivisible_stochastic_modular_rigidity_result.json` and reports
`25/25`. Passing establishes only the finite phase-gauge,
fixed-factor-spectrum, and multi-time counterexamples. It does not prove the
cited stochastic-quantum or self-testing theorems, select a physical
configuration semantics, tensor factor, locality contract, instrument,
record, division event, time, geometry, ontology, or new law.

All pre-recharter probes and deterministic artifacts remain regression
evidence for their exact scoped findings. They are antecedents and benchmark
fixtures, not evidence that Certified Causal Reality, record-first ontology,
public finality, geometry reconstruction, or physical recovery is true.

## Meta-record geometry identification control

`du_meta_record_geometry_identification_probe.py` executes the exact finite
`HC-DU-038A` identification ladder using rational arithmetic. It checks:

- affine clock changes and different local elapsed allocations with unchanged
  authenticated order;
- one three-event timelike chain with the same causal matrix in Minkowski
  dimensions 2, 3, and 4;
- scalar-potential recovery exactly when calibrated cover-edge differences
  have zero signed circulation on every undirected cycle;
- incidence rank, the `m-n+c` independent cycle-obligation count, and
  additive-origin gauge;
- relabeling naturality and independent origins on disconnected components;
- an exact diamond and a one-edge nonzero-circulation mutation;
- one and two composed additive relay subdivisions;
- preservation of original-event reachability, potential differences,
  exactness, and cycle rank despite changed raw node, edge, interval, and hop
  counts;
- a nonadditive relay as a physical-contract change; and
- an arbitrary weighted-tree null with no cycle obstruction.

The deterministic artifact is
`artifacts/du_meta_record_geometry_identification_result.json` and reports
`21/21` checks. Passing establishes exact finite known-mathematics controls
only. The reconstructed scalar is not proper time, simultaneity, dimension,
curvature, Lorentzian distance, a metric, physical geometry, record
fundamentality, or new physics.

## Conformal record-geometry reconstruction tournament

`du_conformal_record_geometry_tournament_probe.py` executes `HC-DU-038B`
with exact rational polynomial integration and linear algebra. In the supplied
smooth \(1+1\) conformal arena it checks:

- positivity and common causal cones for the declared metric family;
- blindness of causal order, total volume, one anchored clock and one radar
  return;
- an exact one-dimensional fibre after one regional volume;
- full-rank reconstruction from two overlapping regional volumes;
- exact parameter inversion and a held-out remote-clock prediction;
- nonzero scalar curvature separating a curved fixture from flat space;
- an explicit smooth hidden mode that preserves every training record while
  changing the remote clock and curvature;
- row-span versus nullspace predictability under completion-class expansion;
  and
- the distinction between benign regional reaggregation and separately
  retained child-volume access that increases measurement rank.

The deterministic artifact is
`artifacts/du_conformal_record_geometry_tournament_result.json` and reports
`19/19` checks. Passing establishes exact reconstruction only in the declared
two-mode family and one smooth completion countermodel. The dimension,
coordinate strip, anchors, conformal ansatz and calibration are supplied. It
does not establish a selected spacetime, Einstein solution, physical
record-formation law, quantum-gravity result, new law, ontology or paper
verdict.

## Certified reconstruction fibre theorem

`du_certified_reconstruction_fiber_probe.py` executes the scoped
`HC-DU-039A` typed reconstruction theorem across three frozen specimens. It
checks:

- endpoint-record underdetermination and formed multi-time-record repair for
  the QND process versus endpoint rival;
- one-volume underdetermination, exact two-volume reconstruction with
  determinant `3/64`, and reopening by the smooth hidden conformal mode;
- the equivalence between target factorization and record-kernel inclusion on
  realized finite records;
- an exact increasing-size search for the inclusion-minimal simple binary
  pair-context obstruction;
- normalized local pair tables and matching singleton overlaps despite an
  empty global completion fibre;
- the vacuous truth bug in a constancy-only reconstruction classifier;
- the theorem that a same-class refinement can split a nonempty fibre but
  cannot make an empty coarse fibre nonempty; and
- the resulting distinction between record refinement and
  occurrence-identity/completion retyping.

The deterministic artifact is
`artifacts/du_certified_reconstruction_fiber_result.json` and reports
`12/12` checks. Passing establishes an exact set-theoretic program theorem and
minimum regional counterexample using known mathematics. It does not prove
physical completeness, a physical remainder, record-first ontology,
cross-platform completion of `HC-DU-039`, theorem novelty, or new physics.

## Robust reconstruction, vertical slice, and dynamics restriction

`du_robust_vertical_dynamics_reconstruction_probe.py` executes the coupled
`HC-DU-039B/036G/038C` boundary. With exact rational arithmetic it checks:

- independent record-realizability defect \(\eta\) and feasible-fibre target
  diameter \(\Delta\) across all exact/near and sufficient/insufficient
  combinations;
- the robustly empty-fibre branch and the zero-tolerance reduction to
  `HC-DU-039A`;
- total-variation contraction and fine-fibre inclusion under stochastic
  same-class record projection;
- four complete binary measure-and-prepare selective instruments that share
  outcome effects and formed archive values but differ on a held-out repeat;
- one complete value/provenance/finality/access/base-capability chain whose
  repeat target remains maximally underdetermined;
- exact repair by an independently formed selective-map receipt;
- the conformal hidden mode's survival under smoothness, analyticity and a
  positive finite Dirichlet-action bound;
- absorption of that mode by an unrestricted source \(J=u''\); and
- elimination of the record nullspace by the supplied source-free toy
  equation \(u''=0\), together with the general fixed-source kernel
  criterion.

The deterministic artifact is
`artifacts/du_robust_vertical_dynamics_reconstruction_result.json` and reports
`36/36` checks. Passing establishes an exact coupled program boundary using
known robust-inverse, quantum-instrument and linear-field-equation
mathematics. It does not establish a selected physical dynamics, Einstein
equation, complete physical record, physical remainder, new law, ontology,
new physics or paper verdict.

## Krein sea-flux law-versus-record attribution

`du_krein_sea_flux_attribution_probe.py` independently rechecks the minimal
real-spectrum/complex-spectrum GU branch fork and applies the existing
law/interface/reconstruction distinction to six exact finite cases. It
checks law-only closure, record-assisted target reduction, an uninformative
record, an empty lawful fibre, an unselected record interface, and the actual
GU/Finster incomplete-selector collision.

The deterministic artifact is
`artifacts/du_krein_sea_flux_attribution_result.json` and reports `13/13`
checks. Passing establishes only the marginal attribution rule: records earn
reconstructive credit when a separately selected and formed record reduces a
nonempty, still-open lawful target fibre. It does not compute baryogenesis,
turn functional-domain membership into physical selection, select a record
interface, establish record ontology, or imply new physics.

## CFS selector representation robustness

`du_cfs_selector_representation_robustness_probe.py` consumes the exact W246
action margins and classifies selector claims over a declared faithful
representation class. Its controls include opposite singleton selections,
the joint sign-reversing class, zero margin, an empty class, conditional
law-level selection when an independent physical map is supplied, and the
absence of record credit while the record interface remains unselected.

The deterministic artifact is
`artifacts/du_cfs_selector_representation_robustness_result.json` and reports
`10/10` checks. Passing establishes a representation-robust attribution rule:
an action is not a physical selector when admitted faithful representations
reverse its ordering. It does not identify the physical CFS local-correlation
map, select a GU branch, compute baryogenesis, form records, establish record
ontology, or imply new physics.

## Compute setup

The current numerical probes require NumPy and otherwise use the Python
standard library. SciPy is not currently imported by any tracked DU probe.
CPython 3.14.6 with NumPy 2.5.1 is the verified environment.

From the repository root:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-compute.txt
.venv/bin/python tests/du_loss_lambda_criticality_probe.py
```

The probe scripts are executable checks rather than one consolidated pytest
suite. Run them from the repository root, require exit 0, and inspect their
declared `tests/artifacts/*.json` output. Seeded output can still change across
NumPy releases, which is why the numerical dependency is pinned. A repeat run
under the pinned environment should be byte-identical.

Many probes are intentionally compute-heavy Monte Carlo or finite-enumeration
jobs. Run them sequentially in the foreground unless a probe explicitly says
otherwise; do not launch a parallel sweep merely to validate environment
readiness.

## Paper-opportunity portfolio audit

`du_paper_opportunity_portfolio_probe.py` validates the complete upstream
paper inventory in `../papers/paper-opportunity-portfolio.json`. It checks 27
deduplicated candidate families for stable IDs, required cheap-seed fields,
existing evidence pointers, declared readiness classes, overlap integrity,
concept and result-surface coverage, Factory-entry deduplication, and the exact
nine-item confirmed Factory intake mapping.

The generated artifact passes `20/20` deterministic checks. This establishes
portfolio and custody-record integrity only. It does not establish scientific
truth, novelty, manuscript quality, Factory priority, production activation,
submission, or publication.

## Concentrated paper-closing probes

`du_covariant_record_cost_closing_probe.py` checks the scoped binary
controlled-recorder package used in the `DU-PAPER-003` closing gate:

- the tight relation \(D_R^2\leq4\delta(1-\delta)\) between accessible record
  distinguishability and dephasing-channel distance;
- the conditionally independent fragment consequence; and
- the Holevo-Fano finite archive-support bound.

It passes `12/12` checks with byte-identical output across repeated runs. The
collision audit classifies the general package as absorbed; this probe is an
exact benchmark, not a novelty or publication verdict.

`du_noninvertible_history_certificate_compiler_probe.py` implements the finite
exact-rational `HC-DU-036B` pilot. It freezes a target-independent candidate
grammar before target-dependent selection and returns factorization, minimum
supplied refinement, candidate-class remainder, or incomplete contract. The
same typed kernel runs on a noisy quantum-like route fixture and an
authenticated distributed-history fixture. Both return minimum refinement:
formed history evidence plus certified route/layer provenance repairs the
base witness.

It passes `11/11` checks with byte-identical output across repeated runs. The
result establishes a viable finite compiler kernel only. It does not establish
physical record formation, an exhaustive completion class, a quantum/BFT
identity, an approximate theorem, a resource law, or a physical remainder.

`du_physical_interventional_sufficiency_probe.py` executes the first
published-platform evidence gate for `DU-PAPER-007`. It freezes the six-field
record, boundary, intervention, refinement, target, and strongest-null
contract; audits the Stricker et al. trapped-ion instrument and its linked
Zenodo record; proves that equal plotted means can have different shot
uncertainties and that equal marginals can hide different temporal memory; and
emits the minimum four-table reopening packet.

It passes `22/22` checks with byte-identical output and returns
`INCOMPLETE_CONTRACT`. The public record is figure-source data rather than the
trial-, calibration-, invalid-trial-, provenance-, and multitime-resolved
evidence needed for finite-shot factorization. Passing does not establish
record sufficiency, a remainder, a failed experiment, or new physics.

`du_csg_post_tail_uniformity_probe.py` supplies deterministic finite controls
for the `DU-PAPER-013` proof-or-kill. It checks the exact post semigroup,
transitive-percolation fixed point, regularly varying power-ratio families,
bounded-precursor uniformity, a logarithmic correction, the finite-support
\(P^{-1}\) endpoint, and the published sparse nonconvergent boundary.

It passes `8/8` checks. The analytic source receipt proves the scoped uniform
theorem; this probe tests its seams and provides figure-ready series. Passing
does not establish theorem novelty, a selected CSG law, post recurrence,
manifoldlike geometry, a physical scale, \(\Lambda\), or quantum causal-set
dynamics.

`du_csg_post_tail_second_method_probe.py` checks a separate internal proof
route. Exact rational controls verify both
\(T_{n+1}/T_n=\mathbb E[r_{n+K}]\) and the earlier shifted-binomial identity;
finite regular-ratio families then track localization of the post weights at
the implicit balance scale and convergence of the direct expectation.

It passes `5/5` checks. Passing strengthens the analytic audit only. It is not
independent peer review, theorem novelty, selection of a CSG law, or physical
cosmology.

`du_csg_post_tail_paper_hardening_probe.py` targets the two remaining
paper-grade seams. It changes an arbitrary finite prefix—including zeros and
large irregular entries—while keeping the same factorial tail, and it tests
precursors proportional to the implicit balance scale. In the
\(\alpha=1\) class, the latter converge to the positive solution of
\(x(c+x)=1\), rather than to the bounded-precursor value one.

It passes `5/5` checks. Passing supports the analytic finite-prefix estimate
and demonstrates that \(n=o(b_P)\) is a load-bearing scale boundary. It does
not replace the proof, establish novelty, select a CSG law, or supply a
physical interpretation.

`du_certified_causal_reconstruction_trichotomy_probe.py` implements the
finite exact-rational binary-outcome specialization of `HC-DU-036C`. For each
frozen record or completion kernel it exactly enumerates the vertices of the
stochastic-decoder linear program, computes the minimum worst-history
total-variation deficiency, and returns base reconstruction, resource-Pareto-
minimal refined reconstruction, class-relative remainder, or incomplete
contract.

It passes `11/11` checks twice with byte-identical output. A
boundary-expansion control absorbs the synthetic positive margin. Passing
does not establish a physically exhaustive completion class, an irreducible
remainder, ontology, finite-shot robustness, theorem novelty, or new physics.

`du_public_physical_evidence_screen_probe.py` records the bounded four-table
public-data screen for `DU-PAPER-007`. It keeps trial rows, calibration joins,
selective-map schemas, and multitime/reset rows distinct and forbids
promotion from figures or aggregates.

It passes `9/9` checks and finds no ingestible candidate. Xiang et al.'s
public RB/OQE repository is the strongest reopener, but the inspected schema
contains operation sequences plus aggregate `p0`, not the full joined
evidence contract. Passing is an evidence-routing result, not physical
sufficiency, a failed experiment, or new physics.

`du_physical_history_certificate_transfer_probe.py` extends that kernel to
stochastic record channels. It derives one QND stabilizer record from explicit
quantum matrices and one authenticated operation-DAG record from executable
DAG construction, content hashes, parent checks, fixture MAC tags, and
enumerated delivery schedules. The same exact rational criterion
\(P_a=RK_a\), path equalizer, candidate exclusions, and verdict language run
on both.

It passes `16/16` checks. In both fixtures the noisy public bit is
insufficient, another noisy copy remains insufficient, and a formed
error/delivery syndrome plus certified route/layer provenance is the minimum
sufficient refinement. Withholding the syndrome returns a boundary-relative
candidate remainder; a charged boundary expansion absorbs it. Passing does
not establish proper time, laboratory feasibility, physical interface
selection, cryptographic or BFT security, exhaustive admissibility, an
irreducible physical remainder, or a new law.

`du_central_record_interface_selection_probe.py` attacks the exogenous record
interface directly in one exact finite class. For \(\mathbb Z_2^k\)
random-unitary channels it computes the fixed algebra, its canonical classical
center, and the complementary environment's sector Gram matrix using exact
rational arithmetic. Uniform full-group twirls carry orthogonal
character-sector codes under coherent branch access; an exact Walsh decoder
reads them, while branch-basis dephasing erases them. Deterministic and biased
controls prove that the same fixed center can carry no or only partial
environmental evidence; a degenerate parity fixture exposes only the center
while preserving quantum multiplicity state. Coordinate, environment-gauge,
internal-block-rotation, access-algebra, and noncommuting-noise controls pass.
A matched Pauli-channel extension then holds the scalar exact
fixed algebra and finite-time \(Z\)-signal constant while environment-record
quality spans none, partial, and exact. A constructive grid checks the stronger
rectangle result: at fixed \(0<s<1\), environment distinguishability can span
the full unit interval while the system signal remains \(s^n\).

It passes `33/33` checks. The result is a known-mathematics finite
specialization and a DU dependency advance. It does not derive a physical
channel or system/environment cut, establish a general robust approximate
theorem, observer access, public finality, proper time, geometry, ontology, or
a new physical law.

`du_fresh_record_generativity_resource_probe.py` runs the bounded generativity
hedge. It verifies finite aliasing and the \(2^T\) support requirement for
exact binary-prefix records, then compares a preloaded realized-path tape, a
510-entry finite counterfactual tree, and a two-state fixed parity law. The
fixed law plus append-only output reproduces every declared counterfactual.

It passes `10/10` checks. The finite support-growth statement survives, while
the inference from fresh records or extensional tree size to a nonfixed source
does not. Passing does not establish physical openness, issuance,
computational irreducibility, or a universal resource lower bound.

## Conditional and abductive candidate artifacts

`conditional_candidate_harness.py` implements the comparison contract in
`lab/process/conditional-and-abductive-research-contract.md`. A governed
conditional or abductive probe supplies labeled assumptions, free choices,
observables, nulls, falsifiers, stop conditions, non-ordinal warrant types, and
formalization-versus-concept failure scope. The helper validates that shape and
writes a deterministic JSON artifact with a compact comparison receipt.

`COMPLETE` in that receipt means only that the research object is legible and
comparable. It is not a scientific pass, claim promotion, or banking decision.
The first three users are the Bianconi completion-robustness,
influence-redistribution abduction, and conditional finality-knee probes from
`SWING-DU-SCI-01`.

`du_science_council_three_track_comparison.py` collects their receipts into one
machine-readable comparison surface. It intentionally emits no scalar score,
vote, automatic winner, or scientific endorsement.

`SWING-DU-PHY-02` adds two live-object users of the same governed method:
`du_bianconi_physical_influence_probe.py` constructs Euclidean and affine-SPD
action-dissipation share profiles, while
`du_record_fisher_influence_probe.py` constructs a `GL(d)`-invariant observed
score-energy profile. The latter decomposes empirical residual energy, not the
Fisher-information matrix; expected information contribution remains uniform
for iid identical records.

`du_physical_influence_selector_comparison.py` keeps those constructions as
separate receipts and tests their replication/accretion asymptotics without
inventing a score or winner. Its `NOT_EVALUABLE` disposition for the prior
incomparable-profile pair means the required physical embedding, matched
carrier, and independent response law are absent. The reported check counts
establish deterministic execution only; they do not select a concentration
functional, identify a unit-bearing physical scale, or promote a claim.

## Five-persona council contested-finding probes

The five-persona next-actions council adds three bounded executable swings:

- `du_orthodox_normalization_null_probe.py` shows that an ordinary quadratic
  relaxation reproduces the point-like zero-activity residue and exact
  replication exponents without a higher-order influence mechanism.
- `du_heterodox_driven_bianconi_probe.py` shows that open anisotropic driving
  can sustain work-balanced Bianconi dissipation while making the imported
  drive cadence and unselected mobility explicit.
- `du_wild_frontier_fisher_csg_scale_bridge_probe.py` constructs a finite
  transition-Fisher/count-scale skeleton and then kills direct
  cardinality-running feedback because statewise relabeling invariance does not
  ensure equal path weight across natural labelings.

The commercial-scientist and philosopher-of-science contested swings are
analytic dependency, dimensional-analysis, and inferential-separability
arguments recorded in their persona memos. None of the five results is a vote,
claim promotion, bank decision, or prediction seed.

## Five-persona successor-wave probes

The successor wave starts from every first-wave output, the complete
fifty-six-item divergent list, and all four Condorcet receipts. Its five
bounded probes are:

- `du_successor_orthodox_post_rg_identifiability_probe.py`, which reproduces
  the exact CSG post semigroup and factorial asymptotic, then constructs a
  hidden-fibre null showing that raw-to-physical Fisher retention is not
  identified by the physical order law;
- `du_successor_heterodox_post_rg_half_power_probe.py`, which tests the
  corrected physical post sector `(T_1,T_2,...)`, reproduces
  `T_2/T_1~sqrt(u/P)` for the factorial family, and contrasts it with the
  killed direct stage-running control;
- `du_successor_commercial_post_rg_decision_probe.py`, which turns the known
  post map, hierarchy conditions, and fixed-history replay into a compact
  route-disposition receipt;
- `du_successor_wild_frontier_post_tail_probe.py`, which evaluates exact
  finite binomial transforms for
  `t_n=u^n/(n!)^alpha` and shows that the post exponent depends on the tail
  class rather than universally equaling `-1/2`; and
- `du_successor_philosopher_post_rg_identifiability_probe.py`, which separates
  projective conditional memory, within-era online feedback, bare-family
  selection, physical scale, and `Lambda` identity through an exact
  frozen-law countermodel and cross-history intervention.

After a post, `T_0` is physically irrelevant because empty-past births are
excluded. Post-effective ratios must use the projective physical sequence
`(T_1,T_2,...)`; both relevant successor probes use `T_2/T_1`.

The five artifacts report `13/13`, `8/8`, `8/8`, `7/7`, and `10/10`
deterministic checks. These execution counts do not establish post recurrence,
family selection, held-out geometry, physical units, or a `Lambda` identity.

## Dual primitive-record-clock council probes

The next five-persona wave compares two admitted conditional premises: a
universal local record cadence without global synchronization and one actual
fundamental global update clock. The latter is split into one record per tick
(`G-full`), gated physical record admission (`G-gated`), and an explicitly
quotiented or operationally hidden scheduler (`G-hidden`).

- `du_record_rate_orthodox_clock_tournament.py` gives the local and global
  models the same A-only echo, then separates them with the remote observer's
  record, a common boost, reunion, and moving-light-clock tests.
- `du_record_rate_heterodox_dual_clock_probe.py` shows that causal order plus
  common spacetime-event density conditionally recovers exact `1+1` Lorentz
  algebra, while `G-full` fails reunion and a fitted `G-gated` completion
  requires both clock and material response.
- `du_record_rate_commercial_delay_reunion_probe.py` turns propagation
  correction, synchronization reslicing, independent distance calibration,
  reunion, and closed-loop anisotropy into a compact route decision.
- `du_record_rate_wild_frontier_clock_quotient_probe.py` constructs a finite
  scheduler quotient and a conditional null-volume clock, showing that
  scheduler tags rather than causal order expose a hidden preferred layering.
- `du_record_rate_philosopher_clock_ontology_probe.py` proves the finite
  compilation underdetermination: every causal-record DAG admits some global
  topological schedule plus gates, while a scheduler-sensitive future kernel
  distinguishes merely hidden order from a true gauge quotient.

The artifacts report `19/19`, `17/17`, `11/11`, `14/14`, and `11/11`
deterministic checks. Their shared local conclusion is that distance-dependent
message delay does not produce unequal accumulated records at reunion under
`G-full`. They do not reject every global-clock construction: exact
construction-specific `1+1` Clock-QW/QCA covariance is retained as a
literature positive control whose durable observer-record semantics have not
yet been reproduced. No probe derives a physical observer, dimensional `c`,
higher-dimensional Lorentz invariance, gravity, DU dynamics, or `Lambda`.

## Recursive viable-systems council probes

The fourth five-persona wave tests whether an unknown number of
viable-system-like levels can be discovered rather than named:

- `du_recursive_viability_orthodox_depth_tournament.py` recovers planted
  depths `m=0,1,2` only when each level earns held-out controlled invariance
  and pays an explicit complexity cost.
- `du_recursive_viability_heterodox_rep3_probe.py` constructs a scrambled
  two-level repetition regulator. Endpoint survival leaves `220/280`
  partitions perfect, while causal repair provenance uniquely recovers the
  planted partition on training and held-out interventions.
- `du_recursive_viability_commercial_passport_probe.py` shows a held-out
  advantage for `m=2` over `m=1`, while a flat global regulator ties `m=2`,
  an overlapping cover overfits, and valid-state aliases fool every fixed
  decoder.
- `du_recursive_viability_wild_frontier_majority_closure_probe.py` constructs
  three repeated active-closure levels, level-specific durable records, and
  dimensionless response ratios while retaining arbitrary-tree, ordinary-RG,
  redundant-depth, resolution, and family-shift controls.
- `du_recursive_viability_philosopher_identifiability_probe.py` shows that
  identity/relay refinement makes raw scalar depth nonidentifiable, then uses
  held-out lesions to recover a relabeling-invariant overlapping role cover.

The artifacts report `17/17`, `23/23`, `17/17`, `24/24`, and `18/18`
deterministic checks, or `99/99` in total. They construct and delimit exact toy
regulators. They do not establish that a causal post, Clock QCA, observer,
physical scale, or the universe realizes recursive viable-system
organization, and they do not derive units, gravity, cosmology, or `Lambda`.

## Premise-free foundational council probes

The fifth five-persona wave supplied no new common physical premise. Each
persona selected and executed the foundational move it judged most valuable
from the complete four-wave state:

- `du_foundational_orthodox_clock_qca_record_entailment_probe.py` audits the
  Clock-QW/QCA source semantics, distinguishes reset countdown/control signals
  from accumulated memory, and separates a representation-stable macro
  interaction trace from raw patch/update counts.
- `du_foundational_heterodox_record_capacity_probe.py` constructs an
  intervention-relative history quotient and proves exact retained-capacity
  saturation for a fixed finite classical state space, with copy, parity,
  archive, and scheduler controls.
- `du_foundational_commercial_record_resource_gate.py` turns exact elapsed
  counts, full event histories, cyclic aliasing, growing QCA support,
  rescheduling, and replay into a compact record-resource gate.
- `du_foundational_wild_frontier_predictive_record_quotient_probe.py` proves
  that the complete standard-CSG transition algebra is equivalent to the
  projective post-transformed coupling sequence, then constructs strictly
  positive couplings that fool every declared finite transition horizon.
- `du_foundational_philosopher_record_identifiability_probe.py` shows that
  durability and predicate-specific classical copyability do not canonically
  select a record under the full automorphism group, while a declared physical
  interface reduces the group and identifies its readout algebra.

The artifacts report `15/15`, `16/16`, `16/16`, `16/16`, and `15/15`
deterministic checks, or `78/78` in total. They support an explicit finite
recorder-extension build and an exact CSG predictive-law quotient. They do not
establish a physical observer, unbounded memory, proper time, a dimensional
unit, post recurrence, geometry, gravity, cosmology, `Lambda`, or DU identity.
Passing checks establishes reproducibility of the declared arguments, not
physical truth.

## Covariant recorder naturalization probe

`du_covariant_recorder_naturality_probe.py` executes the concentrated
`HC-DU-031B` swing against the exact `1+1` Clock QCA. It constructs complete
finite counter-extended scattering matrices, tests canonical and
all-placement rectangular patches, and includes held-out patch, arbitrary
active-unitary, algebraic-forgetting, recorder-off, alias, interference,
copying, no-cloning, and carrier-loss controls.

The artifact reports `31/31` deterministic checks. In the pinned environment,
two successive runs produce the same SHA-256:

```text
42f74179477a8c9f6c1722c5da4e9d9bf54b1f23aa87325b8c766b5bfa41362d
```

The pass establishes an exact finite coherent counter, an inert-`q`
covariance-closure result, and the declared one-gate backreaction witness. It
does not turn the non-isometric algebraic quotient into physical forgetting,
simulate spatial reunion, construct an irreversible archive, select a
physical law, or establish an observer, proper time, continuum covariance,
gravity, cosmology, or Dynamic Unity.

## Covariant archive and boundary probe

`du_covariant_archive_boundary_probe.py` executes `HC-DU-031C`. It replaces
the orthogonal one-event counter with a tunable qubit pointer, checks complete
unitarity and exact source-sense Clock-QCA covariance, and verifies the
two-history relation

```text
V = |cos(theta)|,
D = |sin(theta)|,
V^2 + D^2 = 1.
```

The probe then distinguishes coherent retention, pointer-basis CNOT export,
SWAP transfer, repeated fanout, and independent fresh record formation. It
checks carrier loss, finite recurrence, fresh-support scaling, a
refinement-sensitive rival, arbitrary-active-unitary nonselection, restricted
observational equivalence, and an archive intervention followed by a fixed
reunion recoupling.

The artifact reports `31/31` deterministic checks. In the pinned environment,
two successive runs produce the same SHA-256:

```text
f280617b9309af21dbceae13283dd317240ff7fe48fbe4647368ddebe79dd018
```

The terminal outcomes are
`COVARIANT_FINITE_ARCHIVE_WITH_EXACT_COMPLEMENTARITY` and
`INTERFACE_ONLY_ARCHIVE`. Passing establishes the exact finite construction,
evidence-conservation/resource controls, and the graded
boundary-relocation witness. It does not select the pointer basis, archive
coupling, blank support, reunion, or record law; construct classical
irreversibility; or establish an observer, proper time, continuum covariance,
gravity, cosmology, or Dynamic Unity.

## HC-DU-033A finite record-selection and access quotient

`du_record_selection_quotient_probe.py` executes the finite classical
selection/access baseline for Certified Causal Reality.

It exhaustively checks:

- all partitions through five states (`1, 2, 5, 15, 52`);
- equality-constraint generation and both directions of unique quotient
  factorization;
- every self-map through five states against the generated-equivalence
  criterion;
- partition meet/join universal properties and associativity;
- selection/access constraint composition;
- full-symmetry, declared-interface, copyability, equivariant-channel,
  durability and coalition-access fixtures;
- the strict local-hardening-versus-joint-hardening ordering control; and
- cadence, inaccessible-selection, noncongruent Set quotient, destructive
  pooling, Bell-marginal, Byzantine split-view, held-out, and fixed-codomain
  countermodels.

The artifact reports `25/25` named checks. In the pinned environment, two
successive runs produce the same SHA-256:

```text
173c4f64e80178609791ecb540cd47859df70ceafae6eaef6b01373a04ba77c5
```

Passing establishes the exact finite Set/partition specializations under
supplied constraints. It does not form a record, select the physical
symmetry/interface/cadence/observer, establish a structured process quotient,
make marginal-kernel pooling valid for destructive or quantum channels, prove
common knowledge or Byzantine finality, or derive quantum classicality.

## HC-DU-035A layered threshold objectivity

`du_layered_threshold_objectivity_probe.py` executes the finite
reconstruction/finality/capability separation and ten-lens threshold controls.

Using only the Python standard library and exact `Fraction` arithmetic, it
checks:

- all `240` `(N,f,q)` parameter cases through `N=8` and every quorum pair
  against the exact locked-quorum condition `2q>N+f`;
- the converse split view, safety versus withholding availability, and the
  stochastic honest-lock surplus `h=max(0,2q-N-f)`;
- all 16 binary local hardenings of a two-fragment reliability fixture, whose
  exact raw and sign-hardened Bayes errors are `7/40` and `1/4`;
- IID majority concentration versus an equal-marginal common-shock error
  floor;
- separate reconstruction and action-risk crossings, four named layer
  countermodels, and every truth vector for full reconstruction, finality,
  and action-relevant capability;
- exact metastable rollback, topology, replay/Sybil provenance, and
  inconsistent threshold-secret-sharing controls;
- every GHZ proper-subset reduction plus local-`X` parity recovery; and
- every Bell single-qubit marginal and joint Bell-projector outcome.

The artifact reports `23/23` named checks. Passing establishes the exact
finite controls and rejects a universal scalar objectivity threshold. It does
not form or physically select a record, prove public broadcastable
classicality, supply view-change liveness or common knowledge, prove an LOCC
no-go, establish a thermodynamic phase transition, or derive a novel
quantum/BFT law. The component mathematics is known; the
formation-to-finality physical resource law remains open.

## HC-DU-036A repository-wide council factorization/witness probes

Three independently selected council swings execute complementary finite
specializations of the interventional record-sufficiency discriminator:

- `du_council_orthodox_factorization_witness_probe.py` exhaustively checks
  finite deterministic behavioral equivalence, the tight `n-2`
  action-input witness bound under a free-initial-readout convention, stable
  congruences, record-process upgrades, tight chains, and the no-size-free
  horizon family.
- `du_council_heterodox_delayed_remainder_probe.py` constructs equal-endpoint
  delayed-response rivals that agree through every frozen finite horizon,
  verifies synchronized product search, and proves the exact behavioral-state
  cost of hiding the response in that fixture.
- `du_council_wild_frontier_interventional_closure_probe.py` exhaustively
  checks the greatest intervention-stable refinement, its `n-b_0` witness
  bound, the smallest delayed fixture, tight chains, a finite linear
  reachable-rank control, clone invariance, and a decision-relevant witness.

The artifacts report `7/7`, `51/51`, and `9/9` named checks, or `67/67` in
total. Repeated runs are byte-identical. Passing establishes known finite
automata and linear-equivalence specializations plus exact controls for
`HC-DU-036A`. It does not physically form a record, justify a complete
intervention basis, establish noisy or quantum sufficiency, or license an
irreducible-physics verdict. A separating word proves candidate-record
insufficiency; physical-remainder language additionally requires a nonempty,
target-independent, physically admissible and resource-bounded record
refinement class.

The associated commercial `HC-DU-034A` memo supplies an analytic signed
all-port coherent-history identity and exact incoherent-history null. It has
no dedicated probe because its result is a direct two-history trace
calculation; actual proper-time operations, robust instrument nulls, and
calibrated implementation remain open.

## Finite holonomy, public-finality, and provenance probe

`du_holonomy_finality_provenance_probe.py` executes the exact finite baseline
selected independently by the open-frontier Science Council wave.

Using the Python standard library, exact rational arithmetic, and exhaustive
finite enumeration where applicable, it checks:

- record descent through holonomy orbits for all subgroups of `S3` and every
  three-state fact partition;
- nonincrease, including strict losses, of orbit-public capacity when a
  same-fibre reconciliation generator is added;
- the exact action-relative minimum provenance alphabet;
- the `gcd(m,k)` orbit law for translation-loop triangles through `m=12`;
- cycle-lift rank `|E|-|V|+1` on tree and cyclic graph fixtures;
- the qubit fixed algebra of `Ad_X`;
- coherent route quadratures for phase-different implementations of identical
  ordinary channels, with dephased and routed-refinement controls; and
- the additive approximate-loop error budget.

The artifact reports `9/9` named checks. Passing establishes exact finite
group-action, graph-cohomology, fixed-algebra, and information-support
specializations. It does not establish physical perspectival curvature,
public objectivity, common knowledge, a thermodynamic reconciliation cost,
spacetime geometry, or record-first ontology. The coherent route result is
currently classified as interface incompleteness because the routed
implementation refinement predicts it. Noisy/noninvertible reconciliation,
adversarial protocols, approximate fixed algebras, and an actual coherent
proper-time realization remain open.

## Regional finality descent and recursive composition

`du_regional_finality_descent_probe.py` installs the exact finite
`HC-DU-035C` baseline and audits ten counterfactual successor approaches.
Using only the Python standard library and exact `Fraction` arithmetic for
the quantum fixture, it checks:

- the binary cycle-syndrome descent theorem on all `647` connected simple
  graphs through four vertices and every edge parity;
- quorum safety on all `204` `(N,f,q)` cases through `N=8`, the independent
  safety/liveness split at `N=4,f=1`, and raw-count versus independent-origin
  support;
- a two-of-three threshold-access abstraction that separates public
  verification from witness disclosure without claiming a cryptographic
  construction;
- the exact action-factorization criterion for promoting a region to one
  higher-layer node and the minimum boundary lift in a four-state fixture;
- invariance of flat and frustrated descent under causally inert edge
  subdivision despite changed hop count;
- forward-only capability activation at fixed past accessible record;
- a GHZ phase twin whose proper-subset records agree while a global logical
  parity restores a phase-sensitive upper action;
- all four typed outcomes on the distributed twin and the complete
  five-factor counterfactual surface; and
- ten approach cards, each with lenses, kits, an estimand, smallest object,
  absorber, first move, negative output, cheap kill, and scale gate.

The deterministic artifact is
`artifacts/du_regional_finality_descent_result.json` and reports `24/24`
checks. Passing establishes a reusable conjunction of known finite controls,
not endogenous physical regions or validators, a cryptographic security
proof, noisy/noninvertible descent, public objectivity, geometry, ontology,
or a departure from quantum theory.

## Endogenous regionalization

`du_endogenous_regionalization_probe.py` executes the first selection
successor to `HC-DU-035C`. It treats regionalization as finite candidate
identification relative to frozen interventions and a declared
label/refinement quotient.

Using only the Python standard library, it checks:

- exact ANF/Möbius reconstruction of all `65,536` four-input Boolean response
  tables;
- three rival perfect-matching interaction covers with identical passive and
  singleton records and a minimum worst-case separator of two pair actions;
- all 64 quadratic four-input interaction models, for which all six pair
  actions are necessary and sufficient;
- overlapping interaction regions and label covariance;
- two raw deterministic-relay refinements that agree on every admissible
  state and collapse to one core cover;
- independent-versus-cloned validator origins with identical present
  signatures and a separating failure-domain intervention; and
- identified, underidentified-with-separator, observationally-equivalent, and
  incomplete return types.

The deterministic artifact is
`artifacts/du_endogenous_regionalization_result.json` and reports `21/21`
checks. Passing does not select a physical Boolean grammar, make ANF
monomials fundamental regions, turn minimum description into a law, authorize
destructive failure injection, or establish noisy/continuous regional
identification.

## Noisy noninvertible regional descent

`du_noisy_noninvertible_descent_probe.py` separates stochastic global
compatibility from approximate boundary-action sufficiency.

Using exact `Fraction` arithmetic, it checks:

- every even and odd parity vertex through cycle size seven against all
  odd-set facets of the known even-parity polytope;
- all `343` points of a denominator-six triangle grid against the unique
  signed parity-sector extension;
- the exact frustrated equality/equality/inequality family, whose equal-noise
  compatibility threshold is \(\epsilon=1/3\);
- `972` joint-distribution/local-binary-symmetric-channel cases, including a
  fully erasing noninvertible channel, none of which creates a compatibility
  obstruction;
- the exact half-range formula for binary approximate boundary
  factorization;
- a noisy GHZ logical-access specialization with coarse defect \(v/2\) and
  zero defect after the logical lift; and
- all four existing descent outcomes with separate quorum-safety and
  independent-provenance gates.

The deterministic artifact is
`artifacts/du_noisy_noninvertible_descent_result.json` and reports `20/20`
checks. Facet slack and signed negative mass are mathematical obstruction
receipts, not yet operational or physical distances. Passing does not
establish a general stochastic descent theorem, contextuality, a finality
field, protocol security, quantum modification, geometry, or ontology.

## Multi-time regional grammar and general marginal transfer

`du_exact_marginal_extension_compiler.py` is the reusable exact-rational
finite marginal engine. For arbitrary finite alphabets and context
hypergraphs, it constructs `Aq=b, q>=0` and runs a Phase-I simplex with Bland
tie-breaking. It returns:

- `GLOBAL_EXTENSION` with a sparse exact joint distribution;
- `DUAL_OBSTRUCTION` with an integer-normalized Farkas certificate satisfying
  `A^T y >= 0` and `b^T y < 0`; or
- `INCOMPLETE_CONTRACT`.

Every certificate is independently substituted before return.

`du_multitime_marginal_transfer_probe.py` applies the unchanged compiler and
instrument-parent extractor to:

- exact commuting three-qubit QND parity instruments, which derive
  overlapping `AB` and `BC` regions and separate an endpoint-equivalent rival
  under a held-out post-record causal break;
- replayable route- and epoch-authenticated regional transcripts, where
  coarse canonical-origin gluing is obstructed but route provenance restores
  a two-state joint process and exposes equivocation requiring safe rejection;
- compatible and frustrated glued-cycle controls;
- all `343` denominator-six binary-triangle points against the prior closed
  signed-sector oracle, with `119` primal and `224` dual results and zero
  disagreements; and
- six complete two-qubit Mermin--Peres instruments, where the compiler
  recovers the exact inclusion-minimal noncontextual gluing obstruction while
  context-indexed instruments admit an exact `4096`-support product
  extension.

The deterministic artifact is
`artifacts/du_multitime_marginal_transfer_result.json` and reports `33/33`
checks. Passing installs a finite compiler and exact known-mathematics
controls. It does not establish scalable inference, a unique physical
regional grammar, cross-context record identity, cryptographic/BFT security,
joint quantum measurability, beyond-standard dynamics, public finality,
geometry, ontology, or a new law.

## Operational theory landscape

`du_operational_theory_landscape_probe.py` separates conditional validity,
no-signalling, local extendibility, explicit quantum realization, quantum
exclusion and unresolved quantum status on one frozen binary CHSH interface.

Using exact `Fraction` and `Q(sqrt(2))` arithmetic, it checks:

- deterministic-local and isotropic local-boundary behaviors with explicit
  global counterfactual extensions;
- an exact rational Bell-state realization with `CHSH=14/5` and an exact
  Farkas obstruction to a local joint distribution;
- an exact algebraic Tsirelson-saturating realization whose state-supported
  squared CHSH operator has eigenvalue `8`;
- isotropic `CHSH=3` and PR-box `CHSH=4` no-signalling post-quantum controls;
- signalling and invalid-table rejection;
- a withheld-realization twin that preserves the behavior but correctly
  returns unresolved quantum evidence status;
- rejection of a mismatched purported quantum receipt; and
- unchanged landscape cards for the authenticated-route and Mermin--Peres
  controls.

The deterministic artifact is
`artifacts/du_operational_theory_landscape_result.json` and reports `28/28`
checks. Passing establishes a typed classifier using known Bell, Tsirelson,
GPT, marginal-polytope and quantum-instrument mathematics. It does not
compile the general quantum set, establish a generalized causal theory,
derive a finality bound, select an ontology, or add a new physical result.

## Certified overlap identity

`du_certified_overlap_identity_probe.py` executes the first typed precondition
to marginal descent. It distinguishes a repeated label, equality of outcome
effects, equality of selective instruments, multi-time continuation identity,
and authenticated provenance/value identity.

Using exact Gaussian-rational matrices and bounded fixture authentication, it
checks:

- identical QND Z instruments;
- an outcome-dependent Z-phase implementation that induces the same complete
  selective CP maps and must be quotiented;
- a post-record X-flip rival with exactly the same POVM effects and
  tomographically complete outcome probabilities but a different next-Z
  continuation;
- consistent cross-route origin/epoch/value commitments;
- two individually authentic same-origin messages that equivocate across
  routes; and
- cross-epoch nonidentity.

The deterministic artifact is
`artifacts/du_certified_overlap_identity_result.json` and reports `16/16`
checks. Passing establishes an exact finite typed identity assay using known
instrument-tomography and authenticated-record mathematics. It does not
select physical overlaps, close calibration or compatibility loopholes,
establish cryptographic/BFT security, modify quantum theory, or prove a
recursive composition law.

## Record formation to certified composition

Three deterministic probes execute the coordinated
record-formation-to-certified-composition wave.

`du_record_formation_composition_probe.py` checks:

- the exact nondemolition history algebra selected by a frozen two-history
  controlled clock operation;
- nonselection of a unique selective readout by the same interaction and
  nonselective clock channel;
- a signed coherent-erasure certificate with total-variation gap `1/2` from
  every arbitrary-weight mixture of the same two histories;
- identical certificate-record rows for the two latent histories, proving
  that the record does not disclose run-level history; and
- destruction of that certificate by a which-history archive that does
  disclose the history.

Its artifact is
`artifacts/du_record_formation_composition_result.json` and reports `24/24`
checks. This is an exact effective-instrument result using known quantum
instrument and eraser mathematics. It does not supply an
implementation-complete proper-time experiment or physically select the
certificate readout and archive.

`du_recursive_record_composition_probe.py` checks:

- the maximal typed overlap identity obtained by intersecting independently
  formed evidence with the required signature kernels;
- tight total-variation path bounds for identity and boundary-action defects;
- exact join-tree gluing and a sharp cyclic pairwise-agreement/no-global-
  extension counterexample;
- preservation of the true `Z2` obstruction under inert relay subdivision
  while a naive scalar compatibility distance changes from `1/3` to `1/4`;
- logical independence of identity, global-marginal, and upper-action defect
  coordinates; and
- recursive action sufficiency without history disclosure.

Its artifact is
`artifacts/du_recursive_record_composition_result.json` and reports `22/22`
checks. Passing installs a known-mathematics finite composition contract, not
physical regional formation, general quantum joint measurability,
zero-knowledge security, public finality, or a new law.

`du_quantum_strength_selection_probe.py` checks the probability-level
frontier gate:

- one PR box is no-signalling and passes single-copy Local Orthogonality;
- two independent PR boxes violate an exact five-event LO inequality by
  `5/4`;
- ordinary quantum behavior is admitted; and
- probability-level LO/Consistent Exclusivity does not select quantum theory
  because the almost-quantum set also satisfies it.

Its artifact is
`artifacts/du_quantum_strength_selection_result.json` and reports `25/25`
checks. Passing closes probability-only finality/exclusivity as a Dynamic
Unity quantum selector. The exact reopener is physically formed sharp
instrument composition.

## Formed-sharp physical selection and descent

Three deterministic probes execute the formed-sharp selection-boundary swing.

`du_formed_sharp_instrument_probe.py` builds an explicit finite
system–pointer–archive circuit and checks:

- the complete pointer and archive implementation rather than only a POVM;
- the exact binary-QND equivalence among sharp effects, immediate
  repeatability, and perfect disclosure of the supplied sectors;
- rejection of a named misaligned basis only after the source algebra is
  frozen independently;
- nonselection among self-relative conjugate bases;
- different selective continuations sharing one sharp PVM, repeatability,
  central nondisturbance, and archive;
- loss of observer-accessible sharpness through a noisy archive and partial
  recovery through charged majority decoding; and
- preservation of the distinction between process-class certification and
  run-history disclosure.

Its artifact is `artifacts/du_formed_sharp_instrument_result.json` and reports
`34/34` checks. Passing establishes a scoped physical-selection dependency,
not a new repeatability/sharpness theorem, a generated pointer coupling,
public finality, or new physics.

`du_formed_sharp_descent_probe.py` checks:

- the standard common-system sharp-PVM pairwise-to-global construction;
- exact join-tree gluing and a cyclic no-global-extension obstruction;
- relabeling, inert-subdivision, and redundant-marginal controls;
- explicit pairwise joint measurements for noisy Pauli \(X/Y/Z\) effects at
  \(\eta=2/3\) and the exact failure of the triple bound;
- equal sharp effects with different selective maps and continuations; and
- a globally valid archive whose exported coarse certificate is not
  sufficient for the declared upper action.

Its artifact is `artifacts/du_formed_sharp_descent_result.json` and reports
`36/36` checks. Passing closes abstract common sharp-PVM descent as occupied
spectral/joint-measurability terrain. It does not derive the common physical
archive.

`du_formed_sharp_quantum_selection_probe.py` checks:

- a commuting projective target with one global joint archive;
- a context-split Specker archive showing that local record formation does
  not establish cross-context identity;
- the same noisy Pauli pairwise-but-not-triple control; and
- the finite landscape classification supporting the dilation-fork gate.

Its artifact is
`artifacts/du_formed_sharp_quantum_selection_result.json` and reports `16/16`
checks. Passing shows that contextwise sharp dilation is too weak and a
full-cover common commuting dilation restates joint measurability. Specker's
almost-quantum exclusion remains known conditional terrain; no Dynamic Unity
quantum selector is derived.

## Robust physical instrument-orbit selection

`du_robust_physical_instrument_selection_probe.py` freezes one complete
source--pointer--archive family and checks:

- the exact binary relation
  \(\delta_Z=(1-\sqrt{1-D^2})|\sin\theta|\) between record distinction,
  axis misalignment, and source-action disturbance;
- the parallel coupling-symmetry defect against a frozen
  source-plus-degenerate-pointer generator;
- exact source-axis selection up to outcome relabeling for every \(D>0\), and
  the corresponding approximate-alignment bound;
- a matched conjugate-axis foil with the same record quality and resources;
- observer-access degradation through archive noise and separately charged
  three-copy majority decoding;
- a continuation twist with the same sharp effects, archive,
  repeatability, and central nondisturbance;
- rejection of that twist by a full block action algebra, together with the
  degeneracy control showing why source energy alone can fail;
- coherent target-versus-twist routing with every difference reproduced by
  the complete standard-quantum model; and
- two distinguishable retained-environment dilations inducing exactly the
  same reduced effective instrument.

Its artifact is
`artifacts/du_robust_physical_instrument_selection_result.json` and reports
`31/31` checks. Passing selects a source-aligned effective Lüders instrument
orbit only relative to the declared source, action, and candidate classes.
It does not derive a laboratory Hamiltonian, apparatus-asymmetry budget,
perturbation class, unique microscopic dilation, public finality, quantum
theory, or new physics.

## Conservation-to-certified-record interface-necessity gate

`du_conservation_certified_record_probe.py` lifts the finite QND selector into
an explicit \(U(1)\)-conserving source--reference--pointer--archive
architecture and checks:

- a four-outcome joint PVM whose every projector commutes with the additive
  source-plus-reference charge;
- a charge-intertwining formation isometry that writes the result to
  orthogonal pointer and durable archive labels;
- the exact induced equatorial source POVM and all four selective source
  Choi maps;
- informationally complete reconstruction of those selective maps from four
  source preparations;
- the exact accessible-distinguishability and forced-guess-capability
  surfaces under reference visibility, phase mismatch, beam-splitter
  imbalance, and archive sign-flip noise;
- a positive closed-form perturbation-ball floor and a fixed-seed `1000`-case
  off-grid stress test;
- an orientation foil in which two references have identical charge moments,
  purity, phase QFI, trace-asymmetry magnitude, dimensions, processor, and
  resource ledger but program orthogonal source record axes;
- twirled, misaligned, and archive-noise controls; and
- explicit consumption of the oriented reference resource.

Its artifact is
`artifacts/du_conservation_certified_record_result.json` and reports `21/21`
checks. Passing establishes a finite Interface-Necessity No-Go: conservation
and a symmetry-invariant asymmetry budget select at most a measurement orbit;
the oriented reference state supplies the axis. The capability gain is
standard reference-resource accounting. WAY theory, asymmetry resource
theory, no-programming, constrained state discrimination, interferometry, and
instrument tomography absorb the component physics. The result closes
further fitted finite-selector work; it does not establish a new theorem,
physical law, ontology, prediction, paper seed, public finality, or unique
apparatus.

## Entangled layered-finality absorption boundary

`du_entangled_finality_absorption_probe.py` fixes the standard-quantum null
before Dynamic Unity treats layered finality as an extension.

Using only the Python standard library and deterministic finite matrices with
an explicit floating-point tolerance, it checks:

- Bell local randomness, joint \(ZZ/XX\) correlations, and CHSH
  \(2\sqrt 2\);
- no change to the remote marginal under local trace-preserving dephasing;
- redundant copying and exact uncomputation of orthogonal pointer records,
  alongside the nonorthogonal no-broadcasting control;
- embedding of finite thresholds and hysteresis as a retained
  classical-quantum control process;
- absorption and uncomputation of a route-conditioned Bell phase;
- an apparent post-causal-break history residual generated by one omitted
  memory bit and removed by resetting that bit; and
- a deliberately naive ensemble-dependent nonlinear escape that makes
  equivalent preparations distinguishable and fails no-signalling.

The deterministic artifact is
`artifacts/du_entangled_finality_absorption_result.json` and reports `18/18`
checks. Passing establishes that finite history/finality labels selecting
linear CPTP maps are ordinary enlarged quantum processes. It does not
establish a fundamental finality memory, graph-triggered collapse,
perspectival curvature, public-fact phase, actualization cost, capability
backreaction, record gravity, or any departure from quantum theory. The live
frontier is a residual after an implementation-complete causal break resets
every admitted quantum and classical memory.

## Eighteen-lens hypothesis quadratic-vote audit

`du_technical_lens_hypothesis_quadratic_vote_probe.py` audits the
repository-wide technical hypothesis panel. It validates:

- exactly 18 nonredundant lenses;
- exactly two uniquely identified, falsifiable, graded hypotheses per lens;
- one complete 36-hypothesis weight surface per voter;
- exclusion of both voter-owned hypotheses;
- explicit zero weights for every unselected non-owned hypothesis;
- exactly 100 quadratic credits per ballot;
- reconciliation to 1,800 credits and 436 vote units; and
- deterministic ranking of all 36 hypotheses.

The artifact reports `8/8` checks. Its top result is `HG-B`,
Cycle-Filling Public-Finality, tied at 39 vote units with `DC-A`,
Loop-Resolution Finality, and winning the stable tie-break through broader
support. Passing establishes only that the recorded ballot obeys its rules
and that the arithmetic is reproducible. Persona hypotheses and votes are
exploratory curiosity/priority signals, not scientific evidence, novelty,
core-hypothesis promotion, a prediction or claim seed, or authorization for
the suggested next swing.

## Ten-lens efficient-approach registry audit

`du_hypothesis_efficient_approach_registry_probe.py` validates the method
companion to the 36-hypothesis panel. Five divergent problem-solving
lenses—category theory, counterfactual statistics, formal counterexample
engineering, experimental metrology architecture, and research
portfolio/operations—join the five standing Science Council lenses.

The registry attaches to every hypothesis:

- a smallest informative object;
- a recommended proof, search, statistical, or experimental attack;
- one first decisive contrast;
- reusable method kits and outputs;
- a condition for increasing scale; and
- the brute-force or semantic-refit trap to avoid.

The artifact reports `10/10` checks, exactly ten lenses, ten shared method
kits, and exactly one attachment for each of the 36 source hypotheses.
Passing establishes completeness and referential integrity only. The registry
does not select, eliminate, defer, grade, validate, or rerank a hypothesis and
does not authorize a swing.

## Cross-repo hardening controls probe

`du_cross_repo_hardening_controls_probe.py` locally rechecks the six finite
control shapes in
`../lab/process/cross-repo-hardening-control-contract.md`:

- an immutable stage-zero oracle carrying a realized path and finite
  counterfactual response tree;
- locally record-isomorphic states separated only by a declared
  boundary-crossing environmental read;
- raw fragment-count inflation absorbed by audited independent support;
- reachability preserved while hop count changes under benign relay
  subdivision;
- changed-instrument versus matched-frame capability comparisons; and
- a proper inclusion from the starter completion constructors into DU's
  extended, explicitly nonexhaustive adversary inventory.

The deterministic artifact is
`artifacts/du_cross_repo_hardening_controls_result.json` and reports `14/14`
named checks. Passing establishes finite control-shape execution only. It does
not import sibling claims, establish physical realizability, define novelty as
noncomputability, select an observer boundary, prove a universal SBS absorber,
identify physical topology, exhaust completion classes, or promote a claim,
hypothesis, prediction, ontology, or seed.

## Triplet boundary index and flavor identifiability

`du_triplet_boundary_flavor_integrated_probe.py` executes the exact finite
kernel for `HC-DU-040A`. It checks:

- index multiplication for a unit-index boundary map tensored with a triplet;
- carrier-dimension and target-coded controls showing where the number three
  enters;
- a vectorlike global-index-zero completion with an accessible rank-three
  sector;
- invariance under inert direct-sum stabilization;
- indistinguishable terminal operators with different construction
  provenance;
- the scalar commutant of the irreducible spin-one triplet;
- the common-eigenbasis obstruction for two operators generated by one cyclic
  action; and
- a noncommuting flavor fit as a deliberately nonexplanatory positive
  control.

The deterministic artifact is
`artifacts/du_triplet_boundary_flavor_integrated_probe_result.json` and reports
`21/21` checks. Passing establishes a conditional finite index bridge plus
scoped identifiability and symmetry no-gos. It does not construct the physical
GU source operator/domain, distinguish a fundamental index from an
independently justified access boundary, derive flavor, explain three
generations, or promote a prediction, claim, ontology, paper, or new physics.

## Inverse chirality and three-generation retrodiction

`du_inverse_chirality_generation_tournament_probe.py` freezes three protected
accessible chiral Standard Model families with consistent completion and
nonzero flavor CP as a conditional endpoint, then works backward. It checks:

- exact rational one-family `SU(3)^3`, `SU(3)^2U(1)`,
  `SU(2)^2U(1)`, `U(1)^3`, mixed gravitational and global `SU(2)` anomaly
  controls;
- homogeneous anomaly cancellation for one through six repeated families;
- hidden-mode completions with the same accessible `(3,0)` chirality across
  global indices `-5` through `5`;
- hidden mirror-pair freedom even after global index three is fixed;
- the standard angle and irreducible Dirac-CP-phase counts for one through six
  generations;
- a unitary three-family nonzero Jarlskog/commutator positive control;
- a common cyclic flavor-algebra null; and
- six rival endpoint preimages plus eight count-sensitive successor channels.

The deterministic artifact is
`artifacts/du_inverse_chirality_generation_tournament_result.json` and reports
`27/27` checks. Passing establishes that ordinary Standard Model anomalies are
family-count blind, ordinary CKM-like CP supplies a lower bound of three rather
than an exact count, and accessible chirality underidentifies the admitted
global completion. It does not construct a physical operator, establish that
every finite completion is a consistent QFT, derive three generations or
flavor, or promote a claim, prediction, ontology, paper, or new physics.

## Physical sufficiency acquisition gate

`du_physical_sufficiency_acquisition_gate_probe.py` validates the prospective
physical input to `HC-DU-036C/036D`. It checks:

- the versioned embedded-table schema;
- strict retention of every attempted shot and invalid attempt;
- trial-to-calibration, controller, decoder, route and immutable-attachment
  joins;
- selective multi-time event coverage;
- independent reset receipts covering every admitted retained memory;
- simultaneous Hoeffding--Bonferroni response and readout-calibration
  intervals;
- conservative interval inversion with a frozen joint SPAM/drift allowance;
- tolerance-bounded base reconstruction;
- componentwise resource-Pareto-minimal refined reconstruction;
- a completion-class-relative remainder candidate;
- an honest finite-shot inconclusive branch; and
- refusal of Xiang-style aggregate `p0`, missing attempts, broken calibration
  joins and incomplete reset scope.

Run the deterministic controls with:

```bash
python3 tests/du_physical_sufficiency_acquisition_gate_probe.py
```

Assess one prospective JSON packet without rewriting the control artifact
with:

```bash
python3 tests/du_physical_sufficiency_acquisition_gate_probe.py \
  --packet path/to/packet.json
```

An incomplete packet prints its exact refusal codes and exits `2`.

The deterministic artifact is
`artifacts/du_physical_sufficiency_acquisition_gate_result.json` and reports
`12/12` checks. The classification fixtures are generated in memory with
`evidence_kind=synthetic_contract_control` and always carry
`scientific_verdict=false`. Passing establishes a prospective acquisition and
binary-response analysis gate only. It does not supply a physical packet,
complete selective-process tomography, exact equality, an exhaustive
completion class, a physical remainder, record-first ontology, new physics,
or statistical novelty.

## Provider acquisition visibility bridge

`du_acquisition_visibility_bridge_probe.py` validates `HC-DU-036E` without
contacting a provider. It checks:

- the strict provider-capture schema and frozen 19-circuit QND-memory suite;
- calibration, training, held-out, and causal-break coverage;
- circuit-manifest, row, attachment, execution-span, attempt, and reset joins;
- refusal of post-freeze semantic refits, mutated rows, missing shots, and
  post-acquisition freezes;
- a pre-provider authorization guard on real hardware submission;
- four distinct claim ceilings for synthetic control, provider-returned rows,
  all attempts without complete reset, and implementation-complete mapping;
- the exact finite acquisition-visibility factorization equivalence; and
- a counterexample in which acceptance probability and every accepted outcome
  agree while the unobserved rejected stratum and complete attempted process
  differ.

Run:

```bash
python3 tests/du_acquisition_visibility_bridge_probe.py
```

The deterministic artifact is
`artifacts/du_acquisition_visibility_bridge_result.json` and reports `15/15`
checks with byte-identical repeated output. Passing establishes a
provider-facing acquisition contract and exact claim ceiling only. The
factorization lemma is standard conditional-probability algebra. No hardware
job, physical packet, physical factorization, remainder, ontology, new
physics, or statistical novelty is established.

`artifacts/du_ibm_runtime_acquisition_dry_run_result.json` separately records
the Qiskit 2.5.1/Aer 0.17.2 dry run: 19 circuits, 32 shots each, 608 joined
rows, strict schema validation, and byte-identical repeated captures. It is
also synthetic and has the same no-physical-verdict ceiling.

## Interventional-sufficiency novelty and reachability gate

`du_interventional_sufficiency_reachability_gate_probe.py` freezes
`HC-DU-036F`'s source collision, provider-observability matrix, and six-rung
claim ladder. It checks that:

- process tensors, instrument-specific quantum memory, quantum-instrument
  tomography, and postselection already occupy the component problems;
- the unlocated five-part DU conjunction remains
  `UNRESOLVED_NOT_PROMOTED`, not novel;
- public-interface silence remains `NOT_DOCUMENTED`, never documented
  physical absence;
- the existing IBM bridge is the only pilot-ready path in the scoped matrix,
  while no inspected standard interface documents all-attempt visibility and
  complete admitted-memory reset;
- an API-boundary result cannot be promoted to the complete physical
  substrate; and
- external hardware is assumed unavailable until the local-exhaustion gate,
  after which one awareness note routes the branch locally or parks it unless
  Joe separately authorizes pursuit;
- provider searching, adapter building, and repeated hardware proposals stay
  stopped without a new reopener; and
- finding an exact integrated prior result would switch the route to
  `ABSORBED_STOP`.

Run:

```bash
python3 tests/du_interventional_sufficiency_reachability_gate_probe.py
```

The deterministic receipt is
`artifacts/du_interventional_sufficiency_reachability_gate_result.json`.
Passing reports `29/29` and `FORMAL_FIRST_PARTNER_GATED`, including the three
significant locally executable theorem, counterexample, and
minimum-discriminator routes plus the unavailable-by-default hardware
posture, one-awareness-note boundary, separate authorization, and
anti-circling rule. It establishes a research route and claim ceiling only.
It does not establish novelty, provider absence, hardware feasibility,
physical factorization, a physical remainder, or new physics.

## Local model learning gate

`du_local_model_learning_gate_probe.py` validates the repository-wide
`LMLG-01` admission and checkpoint contract. It checks that:

- exact finite counterexample search and minimum-discriminating-experiment
  computation are admitted because they produce decision-changing learning
  locally before hardware;
- reproduction of a published curve routes to bounded research;
- a provider adapter whose first informative result requires hardware stops;
- target-coded, no-decision-value, incomplete, and needlessly oversized
  builds are refused;
- a generated insight and a decision-changing null are bankable at their
  earned grade; and
- an admitted build stops when its local checkpoint produces no learning or
  encounters an external dependency early.

Run:

```bash
python3 tests/du_local_model_learning_gate_probe.py
```

The deterministic receipt is
`artifacts/du_local_model_learning_gate_result.json` and reports `16/16`.
Passing establishes model-work routing only. It does not build a model,
establish literature novelty, prove a physical result, require hardware, or
authorize an external action.

## HC-DU-036H selective autonomous-record quotient spine

`du_certified_causal_spine_probe.py` checks the exact finite controlled
quotient condition

\[
\sum_{z:r(z)=q'}K_a(s,y,z\mid h_0)
=
\sum_{z:r(z)=q'}K_a(s,y,z\mid h_1)
\]

for every same-record pair, action, acquisition stratum, response, and
next-record class. Passing establishes a well-defined autonomous quotient
kernel and, by induction, equality of all finite labelled-record trace laws.
This is controlled strong lumpability/probabilistic bisimulation, not a new
theorem. Predictive sufficiency for one frozen tester family remains the
weaker Blackwell-factorization question.

The probe also checks:

- the inclusion-minimal three-state deterministic endpoint/continuation
  witness and exhaustive absence of a two-state witness;
- a three-state stochastic example where event and next-record marginals
  agree but their joint selective row differs;
- accepted-only visibility hiding a rejected-stratum difference;
- system-only versus complete reset of recouplable hidden memory;
- realizability before target constancy;
- refusal of target-coded repair and representation-sensitive selection;
- the unchanged QND-versus-flip quantum-instrument shadow;
- the unchanged metastable-versus-BFT authenticated-process shadow; and
- resource-Pareto repair only inside each frozen finite admissible class.

Run:

```bash
python3 tests/du_certified_causal_spine_probe.py
```

The deterministic receipt is
`artifacts/du_certified_causal_spine_result.json` and reports `19/19` with
`KNOWN_MATHEMATICS__INTEGRATED_ASSURANCE_ONLY`. It establishes no physical
record selection, complete quantum process, physical remainder, ontology, new
law, new physics, paper promotion, hardware need, or external action.

## HC-DU-033D action-center formation and capability boundary

`du_action_center_capability_boundary_probe.py` preserves exact rational
controls for the direct finite-dimensional operator-algebra proof:

- the minimal central projections of \(M_2\oplus M_2\) form the finest
  action-internal sharp PVM whose Lüders channel preserves the complete
  action algebra;
- a rank-one projector inside one block is internal but noncentral and
  exactly disturbs a within-block \(X\) action;
- an explicit blank pointer/archive isometry writes the central sector and
  intertwines every block action;
- block-scalar complete event/next-record effects descend to an autonomous
  central row, while one noncentral effect separates two same-record states
  with probability margin one;
- a factor has no nontrivial tested internal central record, while a
  nontrivial commutant pointer is nondisturbing but noninternal;
- a commutative diagonal action algebra is completely represented by its
  minimal central record even though density operators outside that action
  contract may differ; and
- a common exact permutation conjugation preserves every verdict and the
  hostile margin.

Run:

```bash
python3 tests/du_action_center_capability_boundary_probe.py
```

The deterministic receipt is
`artifacts/du_action_center_capability_boundary_result.json` and reports
`24/24` with
`KNOWN_MATHEMATICS__ACTION_CENTER_FORMATION_TO_CAPABILITY_BOUNDARY_EXACT`.
The executable is regression only after the direct proof. It does not select
the physical action algebra, source/pointer/archive boundary, formation
coupling, decoder, observer, microscopic dilation, ontology, new law, new
physics, paper state, hardware path, or external action.

## HC-DU-035D center-screening regional finality and first leak

`du_center_screening_regional_finality_probe.py` preserves exact finite
controls for layered composition of public centers with explicit retained
noncommutative fibres:

- a two-region public-sector controlled update pulls every later public
  center effect into the earlier center;
- sequential, tensor, and public-record-adaptive screened maps remain
  screened;
- a fibre-population-controlled update produces a noncentral pullback and a
  same-public-record/different-later-outcome witness;
- a fibre-phase-controlled update distinguishes \(|+\rangle\) from
  \(|-\rangle\) with probability margin one although they have identical
  public centers and fibre-\(Z\) populations;
- physical fibre dephasing screens that phase assay by making the hostile
  inputs identical;
- a selective fibre-\(X\) route leaks even though the route-averaged channel
  preserves the center;
- backward effect propagation identifies the first noncentral transition;
- the exact block spectral-width margin equals twice operator-norm distance
  to the center;
- a common permutation representation change preserves every verdict; and
- the distributed shadow separates certificate-only regional updates from a
  hidden-local-state hook.

Run:

```bash
python3 tests/du_center_screening_regional_finality_probe.py
```

The deterministic receipt is
`artifacts/du_center_screening_regional_finality_result.json` and reports
`29/29` with
`KNOWN_MATHEMATICS__CENTER_SCREENING_FINALITY_AND_FIRST_LEAK_EXACT`.
Passing proves a scoped finite center-screening, composition, and first-leak
boundary. It does not select physical regions, action algebras, boundaries,
formation couplings, archives, observers, the complete future action class,
ontology, a new law, new physics, paper state, hardware path, or external
action.

## HC-DU-039C screened effective physics and source attribution

`du_screened_effective_physics_attribution_probe.py` preserves the smallest
exact Boolean/Clifford controls for the fourth campaign swing:

- four source assignments \(x=(\tau,\chi)\in\mathbb F_2^2\) share one
  screened three-event public causal chain;
- public reachability and center statistics are source independent;
- one noncentral readout reconstructs the total phase
  \(\phi=\tau+\chi\);
- \((0,1)\) and \((1,0)\) have the same total-phase record but opposite
  duration and field-source targets;
- a second independently calibrated \(\tau\)-sensitive readout makes the
  source sensitivity matrix full rank;
- exhaustive enumeration of all `16` sensitivity-row subsets and four
  linear targets confirms `64/64` instances of
  target factorization iff kernel containment;
- no one-bit nonzero linear probe reconstructs two source bits, while every
  pair of distinct nonzero sensitivities does;
- record-fibre sizes shrink exactly `4 -> 2 -> 1`;
- target-coded repair and invertible source reparameterization are
  classified correctly;
- distinguishable capability classes grow `1 -> 2 -> 4` only as the
  independently calibrated interfaces are added; and
- a distributed latency/provenance shadow preserves the rank statement
  without identifying network delay with proper time.

Run:

```bash
python3 tests/du_screened_effective_physics_attribution_probe.py
```

The deterministic receipt is
`artifacts/du_screened_effective_physics_attribution_result.json` and reports
`27/27` with
`KNOWN_MATHEMATICS__SCREENED_OPERATIONAL_EQUIVALENCE_AND_ATTRIBUTION_RANK_EXACT`.
Passing establishes a finite operational-equivalence and source-attribution
boundary. It does not supply a physical clock, metric, field source,
interface selector, strict-compression result in a real arena, ontology, new
law, new physics, paper state, hardware path, or external action.

## HC-DU-039D proper-time certification and mechanism attribution

`du_proper_time_certification_attribution_probe.py` independently preserves
the exact finite mathematics behind the fifth campaign swing:

- one interior two-level coherence factor has an explicit two-point
  classical random-proper-time representation;
- the exact two-history Ramsey construction has distinct history unitaries,
  bright- and dark-port subnormalized unitary channels, and a nonzero
  conditioned population witness outside every convex mixture of the frozen
  two-history set;
- the rational half-angle control gives
  \(p_+=337/625\), \(\langle Z\rangle_+=-288/337\),
  \(p_-=288/625\), and \(\langle Z\rangle_-=1\);
- identical histories, removal of the intermediate control for this
  population statistic, an unrelated erasure label, incoherent averaging,
  free-set broadening, and complete coherence loss remain explicit nulls;
- history-erasure, clock, and motional nuisance factors remain separately
  receipted;
- every output-only functional of
  \(\theta_\tau+\theta_\chi\) has rank-one sensitivity and exact local null
  \((1,-1)\);
- another same-channel output and complete output tomography do not repair
  mechanism attribution;
- one independently calibrated source-selective intervention row makes the
  local two-parameter map full rank; and
- the nonclassical-history verdict and physical-source-attribution verdict
  can differ.

Run:

```bash
python3 tests/du_proper_time_certification_attribution_probe.py
```

The deterministic receipt is
`artifacts/du_proper_time_certification_attribution_result.json` and reports
`36/36` with
`KNOWN_MATHEMATICS__PROPER_TIME_HISTORY_CERTIFICATION_AND_SOURCE_ATTRIBUTION_AXES_SEPARATED`.
Passing is a primary-source-pinned channel and identifiability boundary. It
does not report an observed proper-time effect, exclude arbitrary classical
protocols, identify a unique physical generator or interpretation, select an
observer/interface, establish ontology, new law, new physics, paper state,
hardware path, or external action.

## HC-DU-040B algebraic-QFT record transport and capability-stable finality

`du_algebraic_qft_record_transport_probe.py` preserves the exact finite
controls behind the von Neumann/AQFT transport boundary:

- a diagonal commutative action algebra admits its two-sector internal sharp
  record, while the full coherent matrix factor does not;
- the Lüders disturbance equals the commutator norm in the binary exact
  control;
- two states with the same public diagonal record are separated by a
  within-factor coherent action;
- a record final for a restricted action set ceases to be final after a
  coherent capability is admitted;
- the exact rational rotation
  \(\cos\theta=99/101,\sin\theta=20/101\) has modest one-step leakage but
  reaches
  \(\sin(8\theta)=10825473963759840/10828567056280801>0.9997\);
- a full `S3` symmetry selects an interface orbit but no member, while an
  oriented physical reference reduces the stabilizer and selects one axis.

Run:

```bash
python3 tests/du_algebraic_qft_record_transport_probe.py
```

The deterministic receipt is
`artifacts/du_algebraic_qft_record_transport_result.json` and reports `37/37`
with
`KNOWN_OPERATOR_ALGEBRA_TRANSPORT__FACTOR_INTERNAL_RECORD_NO_GO__FINITE_HORIZON_APPROXIMATE_FINALITY_ONLY`.
Passing preserves exact regression controls for the theorem and its failure
modes. It does not construct a local QFT record, prove all QFT local algebras
are factors, select a split inclusion or instrument, establish a universal
approximate-finality law, report new physics, promote a paper, or authorize
hardware or any external action.

## HC-DU-041 capability-indexed North-Star adjudication

`du_capability_indexed_north_star_probe.py` preserves the finite exact
controls behind the completed five-swing adjudication:

- exhaustive four-state binary factorization composition;
- the \(9\to3\) material \(Z_3\) gauge quotient and interior-action leak;
- the \(16\to4\) correctable repetition-code quotient and full-class logical
  leak;
- capability enlargement as refinement of operational equivalence;
- exact one-clock Einstein target-fibre widths \(1/2\) and \(3/4\);
- joined two-clock sensitivity determinant \(1/4\), identifying the repair as
  source tomography;
- the total-phase source null and injective two-sensitivity repair; and
- the unchanged candidate audit showing no current endogenous,
  strict-compression, held-out-transfer winner.

Run:

```bash
python3 tests/du_capability_indexed_north_star_probe.py
```

The deterministic receipt is
`artifacts/du_capability_indexed_north_star_result.json` and reports `20/20`
with `TARGET_ACTION_INDEXED_MIXED_VERDICT`. Passing preserves the
factorization, capability-filtration, and attribution controls. It does not
select a physical interface, establish endogenous compressive
reconstruction, prove a representation-robust physical remainder, choose an
ontology, report new physics, promote a paper, or authorize hardware or any
external action.

## HC-DU-044 epoch-archive boundary

`du_epoch_archive_boundary_probe.py` preserves the exact finite controls
behind the matter--environment provenance-lift result:

- exhaustive classification of all `256` binary deterministic transducers,
  with one exact set/retain/reset solution after event semantics are frozen;
- exhaustive rejection of all `16` assignments of reversible bit maps;
- the even-write `CWCW` counterexample to parity-as-occurrence;
- equality of the host-internal turnover flag and the terminal
  ready/retained class over allowed cycle prefixes;
- separation of the stale and rewritten same-endpoint paths by an externally
  initialized epoch flag;
- injectivity of a source-labelled fresh-output branch map, making it
  extensible to a reversible completion with charged output support;
- two injective completion twins with the same reduced matter branch map but
  branch information sent to the admitted archive in one and a hidden
  reservoir in the other; and
- strict binary occurrence compression plus its first write-count leak.

Run:

```bash
python3 tests/du_epoch_archive_boundary_probe.py
```

The deterministic receipt is
`artifacts/du_epoch_archive_boundary_result.json` and reports
`SUPPLIED_EPOCH_ARCHIVE`. Passing preserves the minimum-transducer,
reversible-carrier, internal-reset-collapse, conditional-output-history, and
capability-leak boundaries. It does not derive a microscopic environment,
select a completion or epoch archive, establish a universal cost law,
actualization, ontology, new physics, paper state, hardware path, or external
action.

## HC-DU-045 completion-common transfer

`du_completion_invariant_transfer_probe.py` preserves the exact finite
controls behind the visible-archive/hidden-reservoir transfer result:

- the complete visible and hidden states are injective and have the same
  reduced matter history/branch map;
- the finest target-independent quotient common to both `A`-only native
  records is the terminal matter-state partition;
- exhaustive enumeration of all `21,147` partitions of the nine-history
  arena finds `15` common quotients and one unique finest quotient;
- lossless relabeling of the visible history tokens preserves that quotient;
- the common endpoint reconstructs the complete next reduced-matter branch
  law but not write occurrence, count, or the resolved history word;
- the visible binary epoch record reconstructs occurrence and first fails at
  count;
- the cross-completion capability filtration first fails at occurrence;
- target-coded occurrence repair is not a quotient of the hidden native
  record; and
- enlarging access from `A` to `A+H` reconstructs every target only by
  changing the observer/action/resource contract and becoming injective on
  the finite history class.

Run:

```bash
python3 tests/du_completion_invariant_transfer_probe.py
```

The deterministic receipt is
`artifacts/du_completion_invariant_transfer_result.json` and reports
`31/31`. Passing preserves the finite completion-common quotient,
positive Markov-transfer, adverse history-transfer, and two-tier first-leak
classification. It does not select a microscopic completion or archive,
establish an endogenous record, prove a universal no-go or ontological
remainder, report new physics, promote a paper, or authorize hardware or any
external action.

## HC-DU-046 metastable-host robustness adjudication

`du_metastable_host_robustness_adjudication_probe.py` preserves the exact
finite controls behind the arbitrary-horizon and archive-relocation result:

- endpoint occurrence factorization holds through horizon three and first
  fails at the completed four-edge cycle;
- the empty-history/four-edge witness remains present through every tested
  horizon from four to forty;
- the next reduced-matter branch law continues to factor through endpoint;
- lossless history-token relabelings preserve the information class;
- subdivisions from one through eight microsteps per event contract to the
  same macro witness;
- four positive priors and five rational history-reveal probabilities obey
  the exact Bayes-risk formula;
- the equal-prior witness has risk \((1-\lambda)/2\) and reaches zero only at
  complete revelation;
- accessible/hidden archive relocation preserves the host antecedent while
  changing the admitted interface; and
- full-environment access removes routing dependence only by reading the
  unique full-history token.

Run:

```bash
python3 tests/du_metastable_host_robustness_adjudication_probe.py
```

The deterministic receipt is
`artifacts/du_metastable_host_robustness_adjudication_result.json` and reports
`16/16`. Passing is regression coverage for the analytic arbitrary-horizon,
exact-risk, and archive-relocation proofs. It is not the proof itself, a
microscopic environment simulation, a universal record no-go, evidence of
new physics, a prediction, a paper promotion, or authority for hardware or
external action.

## HC-DU-047 joint-input no-minting and dependency-sensitive amplification

`du_joint_input_amplification_probe.py` preserves the exact finite controls
behind the stochastic/consensus Position-1 result:

- every downstream deterministic certificate remains measurable through the
  common source record;
- every tested binary stochastic garbling has Bayes risk no lower than its
  input experiment;
- XOR and \(2\)-of-\(3\) Shamir sharing recover a target from a joint tuple
  while every individual marginal is target-independent;
- IID majority amplifies, while duplication, common shock, and clustered
  origin limit or eliminate the gain;
- three exchangeable pairwise-independent laws with the same marginal and
  pairwise moments have different majority tails;
- stigmergic replication obeys the exact formation-plus-readout error law and
  approaches the formation-error floor;
- uniform and eclipse sampling differ at fixed population and sample size;
  and
- threshold certificates, FHE/MPC functions, and zero-knowledge transcripts
  do not reconstruct physical targets absent from their complete admitted
  inputs.

Run:

```bash
python3 tests/du_joint_input_amplification_probe.py
```

The deterministic receipt is
`artifacts/du_joint_input_amplification_result.json` and reports `24/24`.
Passing is regression coverage for the analytic factorization, synergy,
dependence, stigmergy, sampling, and cryptographic boundaries. It is not a
network simulator, a cryptographic implementation, a physical model, a
universal effective-support law, new physics, a prediction, a paper
promotion, or authority for hardware or external action.

## HC-DU-048 synergy-preserving gossip, DAG provenance, and knowledge

`du_synergy_gossip_dag_provenance_probe.py` preserves the exact finite
controls behind the propagation/provenance Position-2 result:

- a source-bound XOR world and a target-independent null world have the same
  complete payload-pair law and the same fixed ideal signed-DAG artifact law;
- lossless delivery of both shares reconstructs the target, while partition,
  duplicated-origin eclipse, and churn without retention leave Bayes error
  \(1/2\);
- endpoint payload and source order do not identify route, while retained
  parent links identify declared ancestry;
- raw path length changes under benign relay insertion, while reachability
  between distinguished original source and terminal events survives;
- signed labels distinguish declared key-origin rank but not physical source
  independence;
- partitioned views miss a fork that a merged signed view proves;
- the source group has distributed knowledge before any member knows the
  target, and pooling converts that information into recipient capability;
- every tested finite asynchronous acknowledgment chain retains a
  false-proposition world in the common-knowledge component;
- total order does not identify source truth;
- an event-bound proof certifies a declared relation but not an unmodeled
  physical target; and
- a shared trace may preserve target sufficiency while compressing or losing
  formation provenance.

Run:

```bash
python3 tests/du_synergy_gossip_dag_provenance_probe.py
```

The deterministic receipt is
`artifacts/du_synergy_gossip_dag_provenance_result.json` and reports `34/34`.
Passing is regression coverage for the analytic information-factorization,
declared-provenance, reachability, epistemic, and statement-binding
boundaries. It is not a network simulator, Hashgraph implementation,
cryptographic implementation, physical model, consensus novelty, common-
knowledge theorem, new physics, a prediction, a paper promotion, or authority
for hardware or external action.

## HC-DU-049 metastable-to-Byzantine hardening and provenance lift

`du_metastable_byzantine_provenance_hardening_probe.py` preserves the exact
finite controls behind the Position-3 composition result:

- Avalanche-like wrong-preference probability is \(1/7\) for one frozen
  sample, \(1/343\) for three independent samples, \(1/7\) for one reused
  correlated neighborhood, and one under eclipse;
- any two \(5\)-of-\(7\) quorums intersect in at least three validators, so a
  correct non-conflicting lock excludes conflicting certificates under two
  Byzantine faults;
- a \(4\mid3\) partition blocks liveness while preserving that safety;
- the source-bound and target-independent null worlds have identical
  proposal and hardened-certificate laws, despite physical-target error zero
  versus \(1/2\);
- validator quorum size does not identify source-evidence or physical
  controller rank;
- explicit and bitmap-bearing certificates retain declared signers, while
  ordinary group-key threshold verification may not;
- a plain final quorum certificate does not reconstruct rejected
  equivocation;
- semantic provenance survives benign relay subdivision while raw route
  structure does not;
- epoch/membership binding and proactive refresh are separate premises;
- ZK, VSS, MPC, and threshold verification do not attest an unmodeled
  physical target; and
- every one of eight omitted composition premises returns its own exact
  first failure.

Run:

```bash
python3 tests/du_metastable_byzantine_provenance_hardening_probe.py
```

The deterministic receipt is
`artifacts/du_metastable_byzantine_provenance_hardening_result.json` and
reports `43/43`. Passing is regression coverage for the analytic
combinatorics, factorization fibres, certificate projections, and
first-failure controls. It is not an Avalanche, Byzantine-consensus,
threshold-signature, DKG, ZK, MPC, or physical implementation; a security
proof; new physics; a prediction; a paper promotion; or authority for
hardware or external action.

## HC-DU-050 capability-relative selective views and regional handoff

`du_capability_relative_selective_view_handoff_probe.py` preserves the exact
finite controls behind the Position-4 theorem and handoff boundary:

- all view-field subsets are exhausted over 512 frozen histories to recover
  the minimum semantic view for tentative response, conflict-safe execution,
  signer accountability, equivocation-proof readiness, and physical-source
  adjudication;
- explicit and compressed threshold certificates can both close execution,
  while only the explicit view preserves signer accountability;
- adding audit and physical-adjudication capabilities strictly refines the
  action-relevant history equivalence;
- incompatible incomplete regional views can each close their local action
  without reconstructing global history;
- joined complementary views can support an attributable-fork audit that
  neither supports alone;
- the same certificate and provenance commitment can have different evidence
  availability;
- the same compact group-key record can be current or stale relative to
  receiver epoch;
- a self-confirming adaptive interest filter hides a corrective event;
- positive signed fork evidence is monotone under history extension, while
  absence of a fork is not;
- equal dead-reckoning position/velocity can hide a target-changing
  acceleration, while an authoritative correction supports explicit rollback;
- isolated shards do not close a nonlocal quota invariant that their joined
  view does;
- a complete protocol-only view remains insufficient for the matched null
  physical target; and
- every one of eight omitted handoff premises returns its own exact first
  failure.

Run:

```bash
python3 tests/du_capability_relative_selective_view_handoff_probe.py
```

The deterministic receipt is
`artifacts/du_capability_relative_selective_view_handoff_result.json` and
reports `28/28`. Passing is regression coverage for analytic finite
factorization, selective-view minima, capability refinement, and first-failure
controls. It is not an MMO, database, network, cryptographic, consensus, or
physical implementation; a security proof; new physics; a prediction; a
paper promotion; or authority for hardware or external action.

## HC-DU-051 distributed/physical record collision

`du_distributed_physical_collision_probe.py` preserves the exact finite
controls behind the completed `N5-SCF-P5` collision:

- a QND-formed gauge record and a preloaded/null record have the same visible
  marginal while only the formed relation reconstructs boundary flux;
- signatures over the declared value preserve that same visible law and do
  not identify physical formation mode;
- the material flux archive exactly closes boundary actions while interior
  charge and microscopic formation history remain same-record remainders;
- independent archive corruption lowers majority-readout risk across odd
  sizes `1,3,5,7,9`, while common shock remains at its error floor;
- finite full-support noise remains exactly nonidentifying even when majority
  risk improves;
- ideal and noisy downstream copies do not split the source record's
  interior fibre;
- all 48 physical handoff rows require archive value, availability, current
  epoch, calibrated orientation, and a preserved boundary envelope;
- an old archive remains historical truth but is not sufficient for current
  flux after an unlogged crossing;
- a hardened certificate can close a declared execution rule while leaving
  physical source binding open;
- the MMO dual-mesh control proves that a signed render mesh can identify the
  delivered representation while failing to identify `BLOCK` versus `PASS`
  on the authoritative collision surface;
- endpoint replication, signing, and hardening do not repair the closed
  metastable-host occurrence fibre; and
- full-history access repairs that witness only by injective tomography.

Run:

```bash
python3 tests/du_distributed_physical_collision_probe.py
```

The deterministic receipt is
`artifacts/du_distributed_physical_collision_result.json` and reports
`35/35`. Passing is regression coverage for analytic finite factorization,
exact binomial risk, physical capability refinement, dual-mesh
non-unification, and hostile-host controls. It is not a network, consensus,
cryptographic, gauge, quantum, or hardware implementation; a new theorem in
those component fields; strong emergence; new physics; a prediction; a paper
promotion; or authority for external action.

## HC-DU-052 3+1 lawful causal-exterior remainder

`du_3plus1_lawful_causal_remainder_probe.py` preserves the exact finite
response-matrix certificate behind `N5-RS-P3`:

- three jointly available local scalar/vector responses exactly reconstruct
  their three source coefficients;
- two incoming transverse-traceless modes lie in the complete local-record
  kernel;
- the two modes independently change the two-polarization future
  gauge-invariant target;
- adding the target rows raises exact rank from three to five;
- one polarization is already a minimum exact lawful remainder;
- a no-incoming-radiation condition closes the target before records are
  consulted; and
- the full incoming characteristic archive closes the finite class only by
  injective resource expansion.

Run:

```bash
python3 tests/du_3plus1_lawful_causal_remainder_probe.py
```

The deterministic receipt is
`artifacts/du_3plus1_lawful_causal_remainder_result.json` and reports
`14/14`. Passing is regression coverage for the analytic rank attribution.
It is not a numerical-relativity or detector simulation, an independent
proof of characteristic-Cauchy existence, a novel GR theorem, new physics,
a prediction, a paper promotion, or authority for CFS, hardware, or external
action.

## HC-DU-053 3+1 causally closed noninjective transfer

`du_3plus1_closed_noninjective_transfer_probe.py` preserves the exact finite
certificate behind `N5-RS-P4`:

- both plus and cross incoming amplitudes are inside the frozen two-mode
  completion class;
- aligned and rationally rotated polarization transports are exactly
  orthogonal;
- normalized quadratic intensity is strictly noninjective on polarization
  orientation and transfers to a later polarization-insensitive response
  through one decoder without refit;
- the primary law-only target diameter is two and the
  record-conditioned diameter is zero;
- an orientation-sensitive capability exposes a same-intensity interior
  remainder;
- a linear plus record transfers under aligned propagation and fails when
  the hidden cross direction recouples with exact coefficient `4/5`;
- the mixed component target has law-only diameter `14/5` and
  record-conditioned diameter `8/5`;
- full two-polarization repair is injective tomography; and
- a back-propagated target row repairs only by changing the interface.

Run:

```bash
python3 tests/du_3plus1_closed_noninjective_transfer_probe.py
```

The deterministic receipt is
`artifacts/du_3plus1_closed_noninjective_transfer_result.json` and reports
`22/22`. Passing is regression coverage for the analytic factorization,
diameter, invariance, and first-recoupling result. It is not a
numerical-relativity or detector simulation, an independent proof of
characteristic closure or physical record formation, a novel GR theorem,
new physics, a prediction, a paper promotion, or authority for CFS, hardware,
or external action.

## HC-DU-054 cross-arena dynamic sufficiency and formation separation

`du_cross_arena_dynamic_sufficiency_probe.py` preserves the exact finite
certificate behind `N5-RS-P5`:

- the supplied gravitational-wave intensity record is strictly noninjective,
  transfers under the frozen polarization-insensitive action, and fails
  after oriented capability enlargement;
- accessible and hidden scalar-archive routing preserve the packet/probe
  antecedent while changing the observer interface, making its
  antecedent-guaranteed common quotient constant;
- the metastable endpoint strictly compresses history and transfers the next
  reduced law, while occurrence fails at the first completed cycle;
- accessible and hidden history routing preserve the host antecedent, with
  endpoint as the finest common quotient;
- lossless relabeling, exact subdivision, and reveal/erase controls preserve
  the respective boundaries;
- full repairs are injective/tomographic and the two arenas charge
  differently typed resources; and
- complete-interface selection and state/history transfer are logically
  independent.

Run:

```bash
python3 tests/du_cross_arena_dynamic_sufficiency_probe.py
```

The deterministic receipt is
`artifacts/du_cross_arena_dynamic_sufficiency_result.json` and reports
`26/26`. Passing is regression coverage for the cross-arena selector,
factorization, common-quotient, capability-leak, and resource-type
separation. It is not a universal formation no-go, common native physical
mechanism, new theorem, new physics, prediction, paper promotion, hardware
result, provider action, or external action.

## HC-DU-055 conservative certification and physical feedback

`du_conservative_certification_feedback_probe.py` preserves the exact finite
controls behind `N5-PF-P2`:

- semantic certificate relabeling is inert after complete pre-response
  history and physical boundary matching;
- deterministic declared-control sufficiency is exactly quotient
  factorization;
- a same-label route/memory witness exposes omitted physical boundary state;
- stochastic response reconstruction succeeds through one exact positive
  postprocessing and fails for both an equal-row obstruction and an
  invertible channel whose unique signed decoder has negative entries;
- identical complete quantum instruments ignore semantic labels, while
  physically distinct \(I\) and \(Z\) instruments share a classical
  population-preserving label and differ exactly under an \(X\)-basis
  response;
- certificate-conditioned policy strictly enlarges safe action capability
  through ordinary physical feedback without changing the source law; and
- two linear extensions of one causal partial order give the same result,
  leaving the exactly compensated preferred foliation inert.

Run:

```bash
python3 tests/du_conservative_certification_feedback_probe.py
```

The deterministic receipt is
`artifacts/du_conservative_certification_feedback_result.json` and reports
`24/24`. Passing is regression coverage for the directly proved scoped
deterministic, stochastic-kernel, and quantum-process necessity package. It
does not select the complete physical boundary, prove conditional
independence from marginal channel factorization alone, establish a
certificate-only force, introduce new mathematics or physics, earn a
grade-5 remainder, promote a prediction or paper, or authorize hardware,
provider, publication, or other external action.

## HC-DU-056 feedback-boundary response-equivalence selection

`du_feedback_boundary_selection_probe.py` preserves the exact finite controls
behind `N5-PF-P3`:

- a response-class selector exists exactly when the complete future response
  signature is constant on antecedent fibres;
- raw microscopic implementation identity is not required;
- nested future action families refine operational equivalence
  monotonically;
- the unchanged material `Z3` specimen splits into `1 -> 2 -> 4` response
  classes under source-only, fixed-pointer, and intermediate-path testers;
- the unchanged metastable specimen splits into `1 -> 2 -> 4` response
  classes under endpoint, occurrence, and next-cycle-memory testers;
- material orientation and route/reset-lineage premises close the declared
  finite classes while future-invisible microtags remain plural;
- a semantic reset certificate does not fix retained future-readable memory;
  and
- two linear extensions of one causal partial order preserve the complete
  boundary and response, leaving the exactly compensated foliation inert.

Run:

```bash
python3 tests/du_feedback_boundary_selection_probe.py
```

The deterministic receipt is
`artifacts/du_feedback_boundary_selection_result.json` and reports `21/21`.
Passing is regression coverage for a directly proved scoped selector,
capability-refinement, and reset-memory necessity package. It does not prove
that a current physical antecedent endogenously selects a complete interface,
establish microscopic uniqueness, introduce new behavioral-equivalence or
quantum-process mathematics, earn a new law, ontology, grade-5 remainder,
prediction, paper, hardware, provider, publication, or other external action.

## HC-DU-057 regional-finality excess audit

`du_regional_finality_excess_audit_probe.py` preserves the exact finite
controls behind `N5-PF-P4`:

- one causal tick with ordinary formation probabilities \(1/2\) and \(3/4\)
  reaches error \(1/8\) in three and two steps respectively;
- an arbitrary policy wait changes decision latency without changing causal
  propagation or the physical formation process;
- the rate classification has four branches, separating new Lorentz-covariant
  dynamics from both preferred-frame leakage and inaccessible hidden
  structure;
- noncommuting unsharp \(X/Z\) effects at \(\eta=1/2\) have an exact positive
  joint POVM whose four effects each have trace \(1/2\) and determinant
  \(1/32\);
- provenance-tagged formed classical records merge associatively,
  commutatively, and idempotently downstream;
- a monotone power of an unselected finality score preserves ordering while
  changing the apparent exponent;
- a finite analytic crossover becomes sharply knee-like without becoming a
  critical singularity; and
- two linear extensions of one causal partial order preserve formed record and
  safe action, leaving the exactly compensated foliation inert.

Run:

```bash
python3 tests/du_regional_finality_excess_audit_probe.py
```

The deterministic receipt is
`artifacts/du_regional_finality_excess_audit_result.json` and reports `20/20`.
Passing is regression coverage for a scoped three-candidate classification and
its exact counterexamples. It does not derive a new finality rate, derive
complementarity, select a universal critical exponent or objective-collapse
coefficient, provide preferred-foliation evidence, earn a new ontology or
grade-5 remainder, promote a prediction or paper, or authorize hardware,
provider, publication, or other external action.

## HC-DU-072 operational duality and no-priority

`du_operational_duality_no_priority_probe.py` preserves the exact finite
controls behind the cross-platform operational-duality result:

- exhaustive four-history binary checks show that equal deterministic
  kernels give identical target-factorization scope;
- a noisy binary experiment and an irrelevant outcome-splitting refinement
  mutually garble exactly;
- a repetition-code correction quotient and syndrome record are dual for the
  frozen recovery action, while logical \(\overline X\) is the first leak;
- an authenticated public-action quotient and certificate are dual for the
  frozen execution action, while physical formation provenance is the first
  leak; and
- a same-alphabet, same-marginal source-unbound certificate fails the gate.

Run:

```bash
python3 tests/du_operational_duality_no_priority_probe.py
```

The deterministic receipt is
`artifacts/du_operational_duality_no_priority_result.json` and reports `8/8`.
Passing establishes scoped operational equivalence and its action-relative
breaks. It does not establish ontological identity or priority, native-state
equality, physical record formation, interface selection, new probability or
physics, a grade-5 remainder, prediction, paper, model, hardware, provider,
publication, or other external action.

## HC-DU-073 causal-priority intervention ladder

`du_causal_priority_intervention_probe.py` preserves the exact finite controls
behind the causal-priority reopener:

- source-to-record, record-to-source, and common-source structural models
  share one passive binary endpoint law;
- passive observation and a diagonal joint intervention orient nothing;
- either one-sided surgical intervention separates one direct-arrow model
  while leaving the other confounded with common source;
- both arrow-breaking interventions distinguish all three, with exact
  classical total-variation margin \(1/2\), and exhaustive subset search
  verifies the minimum cover size is two;
- deterministic authentication preserves endpoint value without identifying
  formation direction; and
- opposite CNOT formation circuits plus a Bell-pair replacement channel share
  one terminal density matrix, while two pre-formation phase interventions
  give three exact \(X\otimes X\) signatures.

Run:

```bash
python3 tests/du_causal_priority_intervention_probe.py
```

The deterministic receipt is
`artifacts/du_causal_priority_intervention_result.json` and reports `12/12`.
Passing establishes only the declared model-class-relative intervention
minimum and unchanged process transfer. It does not establish a universal
causal-discovery bound, physical realizability of the intervention ports,
complete acquisition, interface selection, ontological substrate priority,
new causal or quantum law, a grade-5 remainder, prediction, paper, model,
hardware, provider, publication, or other external action.

## HC-DU-091 ETH actuality-algebra naturality

`du_eth_actuality_algebra_naturality_probe.py` preserves the exact finite
controls for the ETH center-of-centralizer gate:

- the tracial centralizer of \(M_2(\mathbb C)\) is the full algebra, whose
  center is scalar;
- restricting the same state to either
  \(\operatorname{span}\{I,Z\}\) or \(\operatorname{span}\{I,X\}\) produces a
  two-dimensional actuality algebra;
- a faithful nontracial state supplies a control in which restriction rotates
  the actuality algebra rather than merely exploiting tracial degeneracy;
- the Hadamard star-automorphism preserves the frozen symmetric antecedent,
  exchanges the two restricted event algebras, and verifies representation
  covariance;
- the two atomic event partitions are individually canonical up to labels
  but mutually incompatible; and
- once either partition and its event time are fixed, the ETH conditioning
  step has the exact probabilities and posterior states of the matched Lüders
  projective instrument.

Run:

```bash
python3 tests/du_eth_actuality_algebra_naturality_probe.py
```

The deterministic receipt is
`artifacts/du_eth_actuality_algebra_naturality_result.json` and reports
`19/19`. Passing establishes only the scoped representation-covariance,
restriction/co-filtration non-naturality, symmetry-orbit, and finite
instrument-absorption controls. It does not refute ETH, select a physical
future-algebra net, derive an event time, form a durable record, select
provenance or access, establish source issuance or empirical excess, earn a
grade-5 remainder, or authorize a prediction, paper, model, hardware,
provider, publication, or other external action.

## HC-DU-133 standard split canonical-factor boundary

`HC-DU-133` is proof- and primary-literature-only. It corrects the earlier
broad statement that AQFT split structure cannot canonically choose an
intermediate type-I factor:

- a bare split inclusion supplies existence and can have infinitely many
  intermediate factors;
- a standard split triple supplies the Doplicher--Longo canonical factor;
- the construction is equivariant under equivalences of the full triple;
- the nontrivial AQFT factor is type \(I_\infty\);
- its faithful reference-state density has infinite rank;
- a positive spectral threshold gives a finite basis-free compression with
  exact trace-distance error; and
- one complement-supported normal state proves that compression is not
  uniform over the local normal-state space.

No new scientific executable was added because modular theory, trace-class
spectral calculus, and the one-state counterexample decide every boundary
exactly. The repository governance suite remains the executable regression.
Passing it does not select the net, regions, standard state, tolerance, probe,
instrument, record write, lineage, archive, access, outcome, target, new AQFT
theorem, empirical excess, law, physics, prediction, paper, hardware,
provider, publication, or other external action.

## HC-DU-134 standard split relative-entropy uniform-compression boundary

`HC-DU-134` is proof- and primary-literature-only. It tests the exact
state-family reopener left by `HC-DU-133`:

- binary relative-entropy data processing turns a bounded forward
  \(D(\rho\Vert\sigma)\) radius into a uniform bound on probability outside
  the canonical spectral projection of \(\sigma\);
- the bound vanishes with the reference tail, making the admitted family
  trace-norm compact;
- a reference-replacement CPTP map has finite-dimensional output and uniform
  trace-norm error at most \(2\sqrt p+p\);
- every fixed downstream channel, effect, and spectator-extended experiment
  inherits that control;
- a reverse-relative-entropy family has a closed-form escaping sequence; and
- pure tail states prove that entropy and rank bounds do not replace forward
  relative-entropy control.

No new scientific executable was added because data processing, spectral
tightness, the gentle-measurement inequality, and the hostile sequences decide
the boundary exactly. The repository governance suite remains the executable
regression. Passing it does not select the standard triple, physical state
family, entropy radius, tolerance, compression dynamics, finite classical
code, probe, acquisition, record write, lineage, archive, access, target, new
operator-algebra theorem, AQFT theorem, empirical excess, law, physics,
prediction, paper, hardware, provider, publication, or other external action.

## HC-DU-135 modular-resource physical-family selector boundary

`HC-DU-135` is proof- and primary-literature-only. It tests whether physical
resource constraints select the exact family required by `HC-DU-134`:

- a bound on the same one-sided split modular energy
  \(K_\sigma=-\log\sigma\) bounds forward relative entropy;
- an ordinary Hamiltonian controls that modular energy precisely when a
  quadratic-form comparison \(K_\sigma\le aH+bI\) is proved;
- a genuine Gibbs reference supplies the clean energy/free-energy
  specialization;
- norm-one, success-one spectral swaps give an exact unbounded-relative-entropy
  counterexample;
- a compact-resolvent Hamiltonian can have a bounded-energy family with
  unbounded relative entropy when the split modular cost grows faster;
- the failed split-relative route can still leave a finite physical
  \(H\)-spectral carrier;
- negative ambient-modular preparation costs constrain a different signed
  object; and
- finite-volume CFT modular inclusions can select a global Hamiltonian without
  selecting the split comparison or a formed record.

No new scientific executable was added because the resource inequalities and
hostile sequences decide the boundary exactly. The repository governance
suite remains the executable regression. Passing it does not select a generic
QFT comparison, energy or work budget, operation class, resource meter,
probe, acquisition, record write, lineage, archive, access, target, new
operator-algebra theorem, AQFT theorem, empirical excess, law, physics,
prediction, paper, hardware, provider, publication, or other external action.

## HC-DU-136 physical reliability and reconstruction-floor boundary

`HC-DU-136` is proof- and primary-literature-only. It tests whether a target
packing count plus a generic physical resource produces a universal finite
reconstruction floor:

- a \(d\)-level zero-Hamiltonian family proves that ordinary state energy
  alone does not bound accessible information across untyped systems;
- Norton completion odds, Landauer expectation identities, controller
  dissipation, finite-time activity, work, duration, reliability, support,
  and measurement capacity remain separately typed;
- Myrvold and Norton explicitly establish that their fluctuation and
  Landauer analyses are compatible;
- an \(M_T(2\delta)\)-point target packing and a physical accessible-capacity
  bound \(\mathcal C_\Pi(B)\) compose through Fano to give the exact necessary
  resolution inequality;
- Fano/minimax, rate-distortion, energy-constrained channel capacity, and
  stochastic thermodynamics absorb the mathematical components;
- the completion class, protocol, resource vector, budget, target topology,
  capacity, archive, and observer access remain physically unselected; and
- reliability bounds can use the reverse relative-entropy orientation that
  `HC-DU-134` already proves insufficient for its canonical finite carrier.

No new scientific executable was added for `HC-DU-136`; the exact theorem and
counterexample are proof checks. The repository governance suite remains the
executable regression. Passing it does not establish the next metastable
specimen, a model-selected capacity, a formed record, physical remainder,
ontology, source issuance, empirical excess, law, physics, prediction, paper,
hardware, provider, publication, or other external action.

## HC-DU-137 physical-interface antecedent-completion boundary

`HC-DU-137` is an exact proof composition using two already banked finite
regressions:

- `du_feedback_boundary_selection_probe.py` preserves the theorem that a
  fixed-action response-class selector exists exactly when the complete
  response signature is constant on antecedent fibres, and that richer
  future actions refine the quotient; and
- `du_source_action_response_record_probe.py` preserves one exact source
  response with vector-current and scalar-action interfaces whose minimum
  complete fixed-probe counts are respectively \(n\) and \(n(n+1)/2\).

Together they establish the campaign boundary:

- a response-preserving automorphism cannot move an interface outside the
  response equivalence class defined by that same response structure;
- the correct operational nonselection witness is
  same-antecedent/different-response;
- the source response does not select the probe, write, archive, access, or
  action envelope;
- a complete physical apparatus process can select its operational quotient
  relative to its frozen actions; and
- inserting the desired response-class label after inspection is
  action-coded repair.

Run:

```bash
python3 tests/du_feedback_boundary_selection_probe.py
python3 tests/du_source_action_response_record_probe.py
```

No new scientific executable was added because another finite model would
replay already proved factorization and apparatus controls. Passing the two
regressions establishes only the scoped finite antecedent-completion boundary.
It does not select an apparatus in nature, prove a universal record-interface
no-go, establish an observer-independent record ontology, transfer to
continuum or QFT, produce empirical excess, authorize hardware, or promote a
paper.

## HC-DU-138 physical action-envelope compiler

`HC-DU-138` closes one premise left explicit by `HC-DU-137`. A complete
physical controller packet—joint dynamics, reachable controller
preparations, reset, resources, horizon, and readout—compiles its induced
action envelope. That envelope then induces the fixed-action response
quotient. The exact regression contains:

- a one-qubit control specimen in which the same drift \(Z\) has a
  one-dimensional reachable Lie algebra without a control generator and
  generates \(\mathfrak{su}(2)\) after \(X\) control is admitted;
- a fixed controlled-H processor whose reachable program support compiles
  either \(\{I\}\) or \(\{I,H\}\);
- an exact \(|+\rangle,|-\rangle\) pair identified by the smaller envelope
  and separated by the larger one; and
- a same-actual-program-history/different-counterfactual-envelope witness.

Run:

```bash
python3 tests/du_physical_action_envelope_compiler_probe.py
```

Passing establishes only the finite controller-relative compiler,
monotonicity, and actual-history nonselection boundary. Quantum control,
no-programming, and counterfactual-task formalisms absorb the component
mathematics. It does not select an observer, controller, preparation class,
record, archive, or access boundary in nature, and it establishes no
ontology, universal no-go, physical remainder, empirical excess, prediction,
law, new physics, hardware need, or paper promotion.

## HC-DU-139 constructor-repertoire/action-envelope boundary

`HC-DU-139` is a primary-source and exact type-level collision. It establishes
that:

- constructor theory makes possible/impossible tasks legitimate physical
  primitives rather than merely semantic action labels;
- its global task repertoire is asymptotic and repeatability-sensitive;
- a DU action envelope is instead finite, observer/controller/access/resource/
  horizon/readout indexed and may include one-shot operations;
- the same global repertoire can support different finite observer envelopes;
- one finite observer envelope cannot recover the global repertoire;
- a subsidiary theory plus a typed physical adapter is required; and
- the general witness theorem imports a scoped mediator nonclassicality
  remainder under its explicit locality, interoperability, determinism,
  mediation, and no-direct-interaction assumptions.

No new scientific executable was added. The result is decided by definitions,
two exact nonfactorization witnesses, and the published status of current
constructor-theory tests. The repository governance suite remains the
executable regression. Passing it does not validate constructor theory, select
a global repertoire or finite observer envelope, observe mediator
nonclassicality, form or certify a record, produce constructor-specific
empirical excess, authorize hardware, or promote a paper.

## HC-DU-146 mediator-component attribution boundary

`du_mediator_component_attribution_probe.py` preserves the exact finite
counterexample used to distinguish total-mediator nonclassicality from
named-component attribution:

- probes \(A,B\) and candidate mediator components \(G,Q\);
- no direct \(A\)--\(B\) gate;
- one coherent CNOT path through \(G\) and one through \(Q\);
- unit Bell fidelity at the active midpoint;
- the same final Bell pair at \(A,B\);
- both mediator components reset to the same blank endpoint;
- equality of the complete four-system endpoint; and
- a component-tagged interaction receipt that distinguishes the paths.

Run:

```bash
python3 tests/du_mediator_component_attribution_probe.py --write-artifact
```

Passing proves only the finite factorization obstruction and its provenance
positive control. It does not model gravity or QFT, validate or refute
constructor theory, adjudicate the Aziz--Howl calculation or its rebuttals,
establish an observed BMV result, prove exclusive mediation in nature, select
a record ontology, produce empirical excess, authorize hardware, or promote
a paper.

## HC-DU-147 mediator-diagnostic identifiability boundary

`du_mediator_diagnostic_identifiability_probe.py` upgrades the `HC-DU-146`
endpoint control to a complete-probe-process symmetry regression:

- candidate mediator factors \(G,Q\) are exchanged by one inaccessible swap;
- the mediator initialization is swap invariant;
- every admitted probe control commutes with the swap;
- the two routed processes are swap conjugate;
- 16 informationally spanning probe inputs and 100 pairs of probe controls
  give 1,600 identical reduced probe outputs;
- the named active-component target nevertheless differs; and
- a calibrated component-selective \(X_G\) pulse breaks the symmetry and
  changes the accessible final \(A B\) parity exactly.

Run:

```bash
python3 tests/du_mediator_diagnostic_identifiability_probe.py --write-artifact
```

Passing proves only the finite symmetry regression and positive control. The
general all-probe statement follows from the swap-covariance proof in
`HC-DU-147`, not from protocol enumeration. Neither establishes gravity as
the active mediator, invalidates effective-process or quantum-memory
diagnostics, validates a proposed gravity experiment, observes exclusive
mediation, produces empirical excess, authorizes hardware, or promotes a
paper.

## HC-DU-148 commutator-phase direct-action descent

`du_commutator_phase_direct_action_descent_probe.py` preserves the exact
finite control used to distinguish a commutator-derived phase from unique
mediator attribution:

- source \(S\) and probe \(P\) act only through mediator \(M\);
- the mediated sequence is
  \(C_X(S,M),C_Z(P,M),C_X(S,M),C_Z(P,M)\);
- the sequence equals \(CZ(S,P)\otimes I_M\) on all eight basis states and
  64 informationally spanning product inputs;
- the mediator is restored exactly at the endpoint for every input;
- a mediator-facing midpoint measurement gives \(P(M=1)=1/2\) in the mediated
  path and \(0\) in the direct path.

Run:

```bash
python3 tests/du_commutator_phase_direct_action_descent_probe.py --write-artifact
```

Passing proves only the central-Weyl/Pauli descent and its mediator-facing
positive control. It does not model linearized gravity, reproduce or refute
the Chen--Giacomini phase, select a physical direct-action law, erase the
phase's conditional excess over Newtonian and declared classical models,
observe a gravity signal, authorize hardware, add a DU prediction, or promote
a paper.

## HC-DU-149 relational phase-decomposition gate

`du_relational_phase_decomposition_gate_probe.py` preserves the exact finite
control used to distinguish a complete relational outcome probability from
the commutator-labelled pieces of one Hamiltonian split:

- \(H=X+Z\) is held fixed;
- \(H_0^{(\alpha)}=(1-\alpha)X\) and
  \(H_I^{(\alpha)}=Z+\alpha X\) give five exactly equivalent tested splits;
- the labelled commutator norm varies continuously from \(2\sqrt2\) to zero;
- the exact propagator and endpoint contract stay fixed;
- jointly transforming state, evolution, and readout preserves the Born
  probability; and
- transforming state and evolution while retaining the old readout changes
  it, providing the positive control.

Run:

```bash
python3 tests/du_relational_phase_decomposition_gate_probe.py --write-artifact
```

Passing proves only scoped Hamiltonian-split nonidentifiability and unitary
relational-probability covariance. It is not a diffeomorphism or gravitational
gauge calculation; it does not show that the Chen--Giacomini phase is
gauge-dependent, reproduce or refute that phase, complete probe/reference
back-reaction, select a physical decomposition, observe gravity, authorize
hardware, add a DU prediction, or promote a paper.

## HC-DU-150 conserved-controller gauge-completion gate

`du_conserved_controller_gauge_completion_probe.py` preserves the exact
periodic-lattice Ward-identity and affine-completion fixture:

- a nonconserved symmetric probe source has a nonzero gauge variation;
- exact discrete summation by parts equates that variation with the pairing
  of the gauge parameter and source divergence;
- two controllers carry the opposite divergence and cancel the probe shift;
- both controller-inclusive total sources are exactly conserved and
  gauge-invariant;
- the controllers differ by a nonzero divergence-free discrete Airy tensor;
  and
- the two equally conserved completions differ on a held-out interaction
  pairing.

Run:

```bash
python3 tests/du_conserved_controller_gauge_completion_probe.py --write-artifact
```

Passing proves only the scoped conserved-total-source requirement and affine
controller-completion nonuniqueness for the exact finite coupling. It is not a
simulation of linearized gravity or a realistic controller; it does not show
that the Chen--Giacomini fringe is gauge-dependent, calculate or cancel its
phase, select a physical apparatus, observe gravity, authorize hardware, add
a DU prediction, or promote a paper.

## HC-DU-151 apparatus-twin influence-phase gate

`du_apparatus_twin_influence_phase_probe.py` preserves the exact rational
Gaussian-response criterion and controls:

- two nonconserved reduced probe branches are kept fixed across apparatus
  twins;
- both controller families carry the opposite probe divergence and make
  every total branch source conserved;
- a common divergence-free controller addition changes the relative
  influence phase by exactly
  \(\langle T_1-T_0,GK\rangle\);
- the common controller self-phase cancels;
- the nonzero cross pairing proves that conservation alone does not imply
  apparatus independence;
- a constructed nonzero response-orthogonal completion leaves the relative
  phase exactly unchanged; and
- identical branch totals remain a zero-relative-phase positive control.

Run:

```bash
python3 tests/du_apparatus_twin_influence_phase_probe.py --write-artifact
```

Passing proves only the scoped quadratic factorization criterion and exact
finite counterexample. The kernel is not a Lorentzian graviton propagator and
the controllers are not laboratory models. It does not calculate, correct,
or refute a published gravitational phase; select a physical apparatus;
observe gravity; authorize hardware; add a DU prediction; or promote a paper.

## HC-DU-153 reduced-QRF access-attribution and handoff gate

`du_qrf_access_attribution_handoff_probe.py` preserves two exact finite
boundaries from the reduced-QRF audit:

- in the source's \(\mathbb Z_2\) block-preserving effect structure, a
  conditional reference flip fails the dynamical-compatibility commutator and
  changes an output population from one to zero;
- a commuting conditional phase preserves the population;
- one local Ramsey rate \(\gamma_{\rm local}=\gamma_{\rm env}+
  \gamma_{\rm ref}\) has design rank one and null direction \((1,-1)\);
- environment/reference twins \((2,3)\) and \((4,1)\) give the same complete
  exponential visibility law;
- two uncalibrated references still retain the common-mode null
  \((-1,1,1)\); and
- an independent reference-calibration row restores full rank.

Run:

```bash
python3 tests/du_qrf_access_attribution_handoff_probe.py --write-artifact
```

Passing proves only the scoped compatibility and attribution boundary. It
does not select a QRF, subsystem factorization, accessible algebra, PVM,
initial assignment, phase reference, record, archive, observer, gravity
signal, physical remainder, new physics, hardware path, or paper.

## HC-DU-154 QRF outcome-broadcast and layered-finality boundary

Run:

```bash
python3 tests/du_qrf_outcome_broadcast_layering_probe.py --write-artifact
```

The exact fixture reproduces the load-bearing structure of Vanrietvelde's
position-superposed-lab communication protocol. A first local copy
temporarily marks which position branch is occupied; the second local copy
removes that tag while leaving the external receiver with the definite
outcome. The final reference-position state is exactly the initial coherent
state.

A hostile third register copies the temporary tag before the second contact.
The receiver still gets the outcome, but the inaccessible copy prevents
position-coherence restoration. A partial-message control uses overlap
\(3/5\), visibility \(3/5\), and distinguishability \(4/5\), saturating
\(V^2+D^2=1\).

Passing establishes an exact finite separation between outcome information
and reference-branch information. It does not solve the measurement problem,
select a Heisenberg cut, subsystem factorization, outcome basis, apparatus,
record, observer, archive, access/certification protocol, regional finality
law, new physics, prediction, hardware need, or paper.

## HC-DU-155 reduced-QRF loop defect and perspectival-curvature gate

Run:

```bash
python3 tests/du_qrf_reduced_loop_curvature_gate_probe.py --write-artifact
```

The exact fixture preserves four controls:

- a CNOT outward-and-return transformation closes exactly when the same
  carrier lineage is retained;
- discarding that carrier and substituting a fresh blank makes the reduced
  return dephase \(|+\rangle\), with \(X{+}\) probability defect \(1/2\);
- on every basis operator of \(M_2\), the reduced-loop defect equals the
  discarded-lineage term in the general closure identity; and
- two qubit conditional expectations onto nonparallel, nonorthogonal axes
  have an exact order-dependent probability and trace-distance difference
  \(6/25\), while identical/orthogonal controls commute and joint
  representation change preserves the statistics.

Passing establishes only the scoped full-versus-reduced-loop,
discarded-lineage, noncommuting-access, and curvature-admission boundaries.
It does not realize a physical QRF loop, select a frame, assignment, access
map, record algebra, archive, regional-finality protocol, or certificate,
establish perspectival curvature or new physics, predict an anomaly, justify
hardware, or promote a paper.

## HC-DU-156 equivariant stochastic interface-selector gate

Run:

```bash
python3 tests/du_stochastic_interface_selector_gate_probe.py --write-artifact
```

The exact fixture verifies a transitive \(C_3\) orbit with no equivariant
point selector but a unique invariant lottery, a two-orbit case with
nonunique invariant lotteries, and the proof receipts for normalized
invariant-probability failure under integer translations and on the Lorentz
hyperboloid. It also verifies two cyclically covariant labelled qubit
instruments with the same unlabelled Bloch channel \(r\mapsto r/3\) and
different accessible conditional responses.

Passing establishes only the deterministic/stochastic selector distinction
and the sampler/archive formation boundary. It does not numerically prove the
continuous hyperbolic theorem or select a physical sampler, realized
interface, record, observer, access path, provenance, ontology, new physics,
prediction, hardware action, or paper.

## HC-DU-140 quantum probability-port / completion-odds / capacity boundary

`HC-DU-140` is a primary-source and exact information-theoretic collision. It
establishes that:

- Krhač's scalar port pairing encodes instantaneous Born-probability flow
  across a declared additive decomposition;
- Norton's odds concern dynamically realized thermodynamic
  completion/reversion probabilities for a declared fluctuation-suppression
  process;
- observer-accessible capacity additionally requires a source encoding,
  instrument, transcript, access, decoder, task, and resource contract;
- for fixed success probability \(s\), a \(d\)-ary erasure family can preserve
  aggregate port flow and completion odds \(s/(1-s)\) while its accessible
  information is \(s\log d\);
- “not an energy eigenstate” does not imply absence of an energy distribution
  or expectation; and
- a complete selected physical packet can compose flow into an outcome law,
  odds, accessible information, and then the `HC-DU-136` reconstruction floor,
  but the three probability quantities are not interchangeable.

No new scientific executable was added. Direct algebra and the erasure-channel
witness decide the universal claim. The repository governance suite remains
the executable regression. Passing it does not select a subsystem
decomposition, measurement, actual outcome, record write, archive, observer
access, success task, thermodynamic implementation, physical capacity,
finality-cost law, empirical excess, prediction, new physics, hardware need,
or paper promotion.

## HC-DU-141 hybrid-measurement finite-time capacity positive control

`HC-DU-141` freezes the smallest binary packet in the exactly solvable
Krhač--Schuller--Stramigioli hybrid measurement law and proves that:

- measurement-eigenstate inputs and a uniform blank pointer induce the binary
  symmetric channel \(q(t)=e^{-\gamma t}/2\);
- its exact capacity is \(C(t)=1-h_2(q(t))\), and the uniform source saturates
  the binary Fano relation;
- the packet-relative readout odds satisfy
  \(O_{\rm read}=2e^{\gamma t}-1\) and
  \(C=1-h_2(1/(1+O_{\rm read}))\);
- the hybrid generator is one-way, so its finite error is incomplete
  relaxation rather than a fluctuation-induced reversion probability;
- the smallest reversible two-rate repair makes finite-time capacity depend
  independently on thermodynamic bias \(\alpha/\beta\) and kinetic depth
  \((\alpha+\beta)t\);
- Norton's \(\Delta S=k_{\rm B}\log O\) enters only after a thermodynamic or
  local-detailed-balance realization is supplied; and
- stochastic thermodynamics has a current--log-affinity entropy-production
  pairing, but the quantum-to-thermodynamic adapter and actual ex-post record
  remain unselected.

No numerical executable was added because the exact solution and channel
algebra decide the result. The governance probe remains the executable
regression. Passing it does not select the measurement, pointer, rate, read
time, bath, reversible dynamics, actual outcome, archive, provenance,
observer access, thermodynamic cost, universal port law, empirical excess,
prediction, new physics, hardware need, or paper promotion.

## HC-DU-142 thermodynamic quantum-record packet selector audit

`HC-DU-142` audits the strongest bounded measurement-model classes and
separates three physical joints that earlier shorthand combined:

- formation of a macroscopic pointer or detector signal;
- actualization of one outcome in an individual run; and
- retention of an accessible provenance-bearing archive.

Metastable apparatus and autonomous-detector sources strongly model formation,
thermodynamic performance, and reset. Bohmian and objective-collapse theories
provide explicit single-run exits by adding primitive ontology or modified
dynamics. No audited source selects the complete unchanged packet.

The exact regression argument uses one dephasing Lindbladian. Its direct-count
unravelling has zero information about a binary \(Z\)-eigenstate source, while
its homodyne unravelling has strictly positive sign-channel capacity.
Unconditional dynamics therefore does not select a unique trajectory record
or capacity even up to information equivalence.

No numerical executable was added because the exact probability laws and
bounded primary-source audit decide the scoped result. The governance probe
remains the executable regression. Passing it does not select the monitoring
boundary, detector, transcript, individual ontology, retained archive,
provenance, observer access, task, no-refit capacity, empirical excess,
prediction, new physics, hardware need, or paper promotion.

## HC-DU-143 non-Markovian collapse/Bohmian record-duality gate

`HC-DU-143` imports the Tilloy--Wiseman exact construction in which a
non-Markovian stochastic collapse trajectory is represented by a deterministic
Bohmian system-plus-bath completion. The bath initial distribution pushes
forward to the collapse-noise law, and the conditioned system wavefunction
plus a natural local beable agree pathwise.

Ordinary measurable pushforward then proves that every unchanged passive
record/archive kernel downstream of the matched path has the same law. A
formed record in this class therefore cannot identify progressive stochastic
issuance versus disclosure from an enlarged initial completion.

The result does not establish global ontology identity or equality under
active interventions. That stronger claim requires one no-refit
correspondence natural across the complete intervention family. Bath/global
access, symmetry or covariance, implementation resources, and the singular
Markovian limit remain possible first leaks.

No numerical executable was added because the published pathwise theorem and
the exact pushforward proof decide the passive-record result. The governance
probe remains the executable regression. Passing it does not validate either
ontology, prove universal collapse equivalence, select an archive or access
boundary, establish intervention-natural equivalence, produce empirical
excess, predict new physics, justify hardware, or promote a paper.

## HC-DU-144 collapse/Bohmian system-control naturality gate

`HC-DU-144` closes the smallest active reopener from `HC-DU-143`:

- conditional projection commutes with a system-only unitary,
  \(\langle x|(U\otimes I_B)|\Psi\rangle=U\langle x|\Psi\rangle\);
- the pulse leaves the bath coordinate and fixed initial noise map unchanged;
- equal conditional paths therefore restart equal and compose across every
  finite pulse sequence; and
- feedback selected from a matched record prefix also closes under one
  supplied common controller and policy.

The result simultaneously blocks the opposite overclaim. One uncontrolled
trajectory does not determine every intervention response. A three-time
one-bit witness gives the same complete no-intervention path but opposite
responses to a flip, depending on whether the process propagates the current
state or restores hidden initial memory. Arbitrary instruments require a
process tensor or equivalent joint completion. If both descriptions inherit
one common process tensor, all declared system-side instrument statistics
agree by construction.

No numerical executable was added because direct conditional-state algebra,
the exact finite counterexample, and established process-tensor theorems
decide the result. The governance probe remains the executable regression.
Passing it does not select an instrument, controller, bath, physical
implementation, symmetry, resource contract, ontology, empirical excess,
prediction, hardware action, or paper promotion.

## HC-DU-145 collapse/Bohmian stable-covariant realization gate

`HC-DU-145` tests the first physical seam left by `HC-DU-144`.
The literal Tilloy--Wiseman bath is

\[
H_B=d\Gamma(M_\omega)
\]

on a full bosonic Fock space over signed frequencies. If a normalized
one-particle packet has negative expectation
\(\epsilon_f=\langle f,M_\omega f\rangle<0\), the \(n\)-boson state in that
mode has energy \(n\epsilon_f\to-\infty\). The even coupling needed by the
exact mixed-frequency path map supplies the negative partner for every
ordinary nonzero positive-frequency support. The literal exact realization is
therefore not bounded below.

A stable repair must restrict or retype the physical packet: band limit,
carrier/rotating frame, reference or pump, occupation sector, nonlinear
stabilization, different beables/coupling, regulator, or future boundary.
None inherits the exact pathwise theorem without a new proof and matched
resource audit.

Lorentz covariance does not itself produce a discriminator. Tilloy's
Lorentz-invariant statistical-field rewriting of regularized interacting QFT
is explicitly intended to retain orthodox QFT observation statistics. It is
a representation-level absorber, not the same real-noise/Bohmian path map or
a rigorous stable nonperturbative selector of a record/archive interface.
Band-limited analyticity gives arbitrary finite forecasting accuracy, not an
exact finite-precision certificate of the future.

No numerical executable was added because the exact spectrum lemma and
primary-source construction audit decide the scoped result. The governance
probe remains the executable regression. Passing it does not prove a
universal stable-dilation no-go, select a physical implementation, record,
archive, access boundary, ontology, or regulator, establish empirical excess,
predict new physics, justify hardware, or promote a paper.

## Minimal-antecedent coherent campaign governance

`du_minimal_antecedent_campaign_probe.py` verifies that the ratified campaign
retains all seventeen named theorem, hypothesis, principle, benchmark, and
moonshot seeds; exposes ten ordered conditional swing cards; and leaves only
Swing 1 executable through an explicit activation packet and transition
automaton.

This is a governance and context-retention test only. Passing establishes no
selector, no-section theorem, material record, reconstruction, remainder, new
law, prediction, or publication claim.

## HC-DU-160 action-indexed selection frontier

`du_action_indexed_selection_frontier_probe.py` exactly enumerates the
selection frontiers of a predeclared two-bit candidate family under three
nested action classes. It checks upper closure, antitone action refinement,
and the expected zero-, two-, and three-member minimal-frontier antichains.

The same probe checks a qubit measurement-model boundary while holding the
unlabelled dephasing channel fixed. Changing the pointer observable at fixed
coupling, or the coupling isometry at fixed pointer observable, changes the
labelled instrument. The pair is therefore a scoped formal-instrument
minimum inside the declared model.

Run:

```bash
python3 tests/du_action_indexed_selection_frontier_probe.py --write-artifact
```

The artifact is
`artifacts/du_action_indexed_selection_frontier_result.json`. Passing proves
only the finite antichains and measurement-model deletion witnesses. It
establishes no universal physical selector, formed record, observer, ontology,
prediction, empirical result, or new physics.

## HC-DU-161 source-pinned coupling-response rank

`du_source_pinned_coupling_response_rank_probe.py` checks the exact local
response boundary for the Peronnin et al. sequential superconducting-qubit
readout platform:

- the residual-population slope and phase-calibrated output slope/curvature
  have Jacobian determinant \(g/2\) with respect to
  \((g,\kappa_r,\kappa_b)\);
- one weak-coupling terminal endpoint has exact coupling/unmonitored-loss
  twins even inside the conservative low-pump regime; and
- the source's main reported operating ratio lies outside the strict
  reflection-calibration regime but inside its wider two-mode release-model
  regime.

Run:

```bash
python3 tests/du_source_pinned_coupling_response_rank_probe.py --write-artifact
```

The artifact is
`artifacts/du_source_pinned_coupling_response_rank_result.json`. Passing
establishes only the exact rank and endpoint counterexample in the frozen
two-mode model. It establishes no complete record packet, physical selector,
anomalous response, empirical result, new law, or new physics.

## HC-DU-162 sequential-readout complete-packet boundary

`du_sequential_readout_complete_record_packet_probe.py` checks exact finite
controls for the source-pinned packet audit:

- distinct raw traces can differ by a nonzero vector in the calibrated
  statistic's kernel and therefore share the same complex statistic and
  binary label;
- full-lineage and streaming-summary archive policies can return the same
  label counts and repeat-agreement summary while retaining different trial
  provenance;
- the source-reported positive cross-classification probabilities make a
  binary label non-identifying for preparation history; and
- the reported release and QND figures are approximate and do not define
  archive-memory reset.

Run:

```bash
python3 tests/du_sequential_readout_complete_record_packet_probe.py --write-artifact
```

The artifact is
`artifacts/du_sequential_readout_complete_record_packet_result.json`.
Passing establishes only finite logical controls around the primary-source
audit. It establishes no experimental fact, complete physical record,
reconstruction, remainder, new law, or new physics.

## HC-DU-163 action-relative materialization boundary

`du_action_relative_materialization_probe.py` checks exact finite controls
for the frozen repeat-readout action:

- equality of complete future-response signatures induces a unique quotient;
- homogeneous and within-record-heterogeneous completions can have identical
  candidate-record distributions, identical joined one-step response laws,
  and identical \(95\%\) aggregate repeat agreement while possessing
  different physical-history quotients;
- zero conditional response-propensity variance separates sufficiency from
  an observed conditional mean in the finite control;
- binary label, calibrated statistic, raw trace, and an idealized identity
  archive can be exact, overfine, coarse, or incomparable relative to the
  quotient; and
- adding one explicitly excluded response action strictly refines the
  behavioral quotient.

Run:

```bash
python3 tests/du_action_relative_materialization_probe.py --write-artifact
```

The artifact is
`artifacts/du_action_relative_materialization_result.json`. Passing proves
only the exact finite quotient and nonidentification controls. It establishes
no hidden apparatus variable, complete physical archive, reconstruction,
remainder, new law, or new physics.

## HC-DU-164 QND-tomography material-archive boundary

`du_qnd_tomography_material_archive_probe.py` checks exact controls for the
bounded QND-tomography reopener audit:

- ideal rank-one projective outcome maps have one-dimensional Liouville range,
  so the outcome label fixes the posterior system state;
- an independent coin-label outcome map has full qubit Liouville rank, and a
  later \(Z\) effect distinguishes histories sharing that label;
- two measurement dilations agree on a complete input matrix-unit basis after
  tracing hidden support, hence induce the same accessible system-plus-label
  instrument for every input and later accessible action; and
- the same dilations leave a hidden archive register blank versus copied, so
  extending access to that register strictly distinguishes them.

Run:

```bash
python3 tests/du_qnd_tomography_material_archive_probe.py --write-artifact
```

The artifact is
`artifacts/du_qnd_tomography_material_archive_result.json`. Passing proves
only the exact finite label-sufficiency and material-dilation nonselection
controls. It establishes no fact about the IBM apparatus, complete physical
archive, reconstruction, remainder, new law, or new physics.

## HC-DU-165 minimal-instrument-dilation invariant boundary

`du_minimal_instrument_dilation_invariant_probe.py` checks exact controls for
the bounded minimal-realization audit:

- ideal projective outcome maps have Liouville/Choi rank pair \((1,1)\);
- a coin-labelled identity outcome has pair \((4,1)\), while a completely
  depolarizing replacer has pair \((1,4)\), proving that operational
  label-sufficiency rank and minimal Kraus multiplicity are independent;
- a rational rotation of a two-Kraus dephasing representation preserves the
  map on the complete matrix-unit basis;
- a redundant two-coordinate Kraus list realizes the same rank-one-Choi coin
  map;
- for outcome-sector profile \((1,2)\), exact commutant equations have rank
  seven in a nine-dimensional operator space, leaving exactly the two
  outcome-sector identities fixed; and
- summing the outcome Choi ranks gives the standard minimal normal apparatus
  dimensions for the declared controls.

Run:

```bash
python3 tests/du_minimal_instrument_dilation_invariant_probe.py --write-artifact
```

The artifact is
`artifacts/du_minimal_instrument_dilation_invariant_result.json`. Passing
proves only the finite two-rank, Kraus-gauge, redundant-realization, and
fixed-algebra controls. It establishes no physical minimality, material
carrier, archive, provenance, reset, observer, remainder, law, or new
physics.

## HC-DU-166 GU source-action admission adapter

`du_gu_source_action_admission_probe.py` checks the exact type boundary
between GU's new candidate source-action construction and Dynamic Unity's
record/reconstruction ladder:

- the seven rung requirement sets are strictly nested from candidate
  functional through DU reconstruction;
- the frozen GU N1/N3 property set clears only the candidate-action rung;
- one fixed action admits constant and identity record maps with different
  fibres;
- one fixed response law admits distinct material carrier/provenance packets;
  and
- the frozen GU packet, N3 result, and post-N3 rebase retain their explicit
  Euler, stationarity, domain, probability, observer-feedback, and RB8
  boundaries.

Run:

```bash
python3 tests/du_gu_source_action_admission_probe.py --write-artifact
```

The artifact is
`artifacts/du_gu_source_action_admission_result.json`. Passing proves only
the typed dependency ladder, source-marker audit, and finite logical
nonimplication controls. It establishes no GU action, lawful solution,
physical response, instrument, material record, reconstruction, prediction,
scientific successor, or new physics.

## HC-DU-167 calibrated ground-truth remainder instrument

`du_calibrated_remainder_instrument_probe.py` enumerates a source-known
32-world render/collision/navigation/authority control and verifies:

- exact reconstruction is target constancy on the frozen
  action--observation fibres;
- five nested envelopes refine the partition through
  `2 -> 4 -> 8 -> 16 -> 32` equivalence classes;
- repeating an unchanged deterministic query does not shrink the structural
  remainder;
- a downstream-only render coordinate can be reconstructible while an
  action-modifiable remote collision coordinate remains unresolved outside
  its action envelope; and
- authenticating the render coordinate does not bind the independent
  collision coordinate.

Run:

```bash
python3 tests/du_calibrated_remainder_instrument_probe.py --write-artifact
```

The artifact is
`artifacts/du_calibrated_remainder_instrument_result.json`. Passing validates
only a finite calibration method and its causal-direction counterexamples. It
establishes no game-engine ontology, physical record selector, quantum result,
prediction, scientific successor, or new physics.

## HC-DU-168 Rigetti fast-feedback packet audit

`du_rigetti_fast_feedback_packet_audit.py` audits the external
`fast_feedback_raw_data.h5` file pinned by MD5 and SHA-256. It verifies:

- eight Ankaa-2 circuit groups with 1,000 aligned returned rows each;
- 216,000 classified and 216,000 complex soft measurement events;
- row-joined decoder registers, timing, and post-feedback qubit-50 response;
- the source-documented conditional-\(X\) response relation without fitting;
- 176 repeated complete hard histories covering 389 rows with no observed
  `DASR` conflicts;
- immediate reference/calibration groups and explicit no-reset metadata; and
- absence of an all-trigger/rejection census, main physical program,
  firmware/configuration, controller route/memory, waveform lineage, archive
  policy, and environment scope.

After downloading the frozen 5.6 MB source file, run:

```bash
uv run --with h5py python tests/du_rigetti_fast_feedback_packet_audit.py \
  --source /path/to/fast_feedback_raw_data.h5 \
  --write-artifact
```

The artifact is
`artifacts/du_rigetti_fast_feedback_packet_result.json`. Passing establishes a
joined returned-shot physical packet and exact implementation boundary. It
does not establish an all-attempt process, complete material archive,
remainder, prediction, ontology, or new physics.

## HC-DU-169 action/resource finality quotient audit

`du_action_resource_finality_quotient_audit.py` uses the source-defined
decoder action quotient

```text
DASR 0 or 2 -> no X
DASR 1      -> X
```

and verifies:

- status 2 has a higher retained median time than status 0 within every
  circuit from rounds 3 through 9;
- all seven empirical probabilities of superiority exceed 0.70 and all
  seven KS distances exceed 0.35;
- a round/pre-state-stratified response test detects no status-0/status-2
  split at five percent;
- the held-out timing CSV contains 300,000 rows but no decoder status or
  stable row identity, so it cannot replicate the action-quotient test.

Run:

```bash
uv run --with h5py python \
  tests/du_action_resource_finality_quotient_audit.py \
  --fast-source /path/to/fast_feedback_raw_data.h5 \
  --timing-source /path/to/decoder_timings_each_repetition.csv \
  --write-artifact
```

The artifact is
`artifacts/du_action_resource_finality_quotient_result.json`. Passing
establishes only a source-pinned sample-level action/resource distinction and
the held-out schema boundary. It establishes no causal status effect,
population law, implementation-complete process, physical remainder,
ontology, or new physics.

## HC-DU-170 controller-sidecar recovery audit

`du_controller_sidecar_recovery_audit.py` pins the arXiv v1 TeX source bundle
for `arXiv:2410.05202` and verifies:

- source descriptions of proprietary assembly, decoder initialization,
  measurement buffering, 32-bit packet formatting, status polling,
  conditional \(X\), matched idle, WISHBONE, star routing, clock crossing,
  and the aggregate qubit-\(T_1\) physical timing check;
- the complete source bundle contains no executable, configuration, data, or
  log member; and
- one exact latent-state twin preserves the returned
  pre-state/command/response tuple while changing physical pulse delivery.

Run:

```bash
python3 tests/du_controller_sidecar_recovery_audit.py \
  --source /path/to/arxiv-2410.05202-v1-source.tar \
  --write-artifact
```

The artifact is
`artifacts/du_controller_sidecar_recovery_result.json`. Passing establishes
only a source-pinned workflow/executable boundary and command/actuation
nonidentification control. It does not show a lost pulse, laboratory defect,
physical remainder, ontology, or new physics.

## HC-DU-171 public-sidecar availability audit

`du_public_sidecar_availability_audit.py` pins the final supplement, complete
Zenodo record, official Riverlane/Rigetti public-repository inventories, and
five plausible Riverlane source checkouts. It verifies:

- the Zenodo deposit contains the exact 18 published data files and no
  executable/configuration sidecar;
- official repository metadata and the pinned plausible source trees contain
  no experiment companion, prototype compiler, or exact implementation
  artifact;
- QECIPHY postdates the archived experiment packet and is a generic interface;
  and
- one exact twin keeps the later interface view fixed while changing
  historical executable identity and held-out actuation.

Run:

```bash
python3 tests/du_public_sidecar_availability_audit.py \
  --zenodo-record /path/to/zenodo-record-15364358.json \
  --riverlane-repos /path/to/riverlane-public-repos.json \
  --rigetti-repos /path/to/rigetti-public-repos.json \
  --qeciphy-repo /path/to/qeciphy-repo.json \
  --nature-supplement /path/to/final-supplement.pdf \
  --riverlane-checkouts /path/to/pinned-riverlane-checkouts \
  --write-artifact
```

The artifact is
`artifacts/du_public_sidecar_availability_result.json`. Passing establishes
absence only on the declared frozen public surfaces and a historical
non-substitution control. It does not prove private or global absence,
evaluate the experiment, establish a physical remainder, or support new
physics.

## HC-DU-172 stage-local instrument-section triviality

`du_stage_local_instrument_section_triviality_probe.py` preserves the exact
finite controls behind the analytic theorem:

- the identity channel has rank-one Choi support;
- coin components sum to the identity and transport naturally through
  representative downstream channels;
- downstream naturality transports those coin components to dephasing;
- the projective \(Z\)-instrument is an informative decomposition of the
  same dephasing channel;
- that informative decomposition violates the bare-arrow stage-local
  naturality equation; and
- once the projective cut is marked, its components transport through later
  dynamics and still sum to the composite.

Run:

```bash
python3 tests/du_stage_local_instrument_section_triviality_probe.py \
  --write-artifact
```

The artifact is
`artifacts/du_stage_local_instrument_section_triviality_result.json`. Passing
preserves the proof controls only; the general result is analytic. It does
not select a physical cut, instrument, sampler, outcome, archive, provenance
chain, observer, new physics, prediction, paper, hardware, provider, or later
scientific action.

## HC-DU-173 quantum-switch order-record relocation

`du_quantum_switch_order_record_relocation_probe.py` preserves the exact
finite controls behind the access-relative causal-order result:

- three pure-marker cases satisfy the exact
  \(D^2+V^2=1\) distinguishability--visibility relation;
- a coherent order-marker completion and its incoherent mixture have the
  same diagonal record and reduced order control;
- one joint \(X\otimes X\) action distinguishes those completions exactly;
  and
- complementary-basis marker conditioning restores unit interference while
  the unconditioned response remains zero.

Run:

```bash
python3 tests/du_quantum_switch_order_record_relocation_probe.py \
  --write-artifact
```

The artifact is
`artifacts/du_quantum_switch_order_record_relocation_result.json`. Passing
establishes only the finite complementarity and coherent-access witnesses.
It does not prove causal nonseparability, select a switch, marker, sampler,
archive, provenance chain, access boundary, observer, global actualization,
new physics, paper, hardware, provider, or later scientific action.

## HC-DU-174 regional reference-alignment gate

`du_regional_reference_alignment_gate_probe.py` preserves the finite controls
behind the collective-reference theorem:

- direct density-matrix expectations match
  \(\operatorname{Re}[\eta e^{i\sum_i\theta_i}]\);
- proper-coalition GHZ indistinguishability is retained explicitly as an
  already-banked regression control;
- simultaneous state and measurement frame changes leave the response
  invariant;
- zero-sum local frame shifts lie in the collective-character kernel;
- independent reference errors factor through local first Fourier moments;
- one independently uniform regional twirl closes the parity discriminator;
- locally uniform but anticorrelated frames preserve full relational access;
- two fixed parity settings reconstruct the complex relational coherence;
- local dephasing and reference quality multiply but remain separately typed;
- an exact twin leaves both parity quadratures unchanged while reallocating
  loss between source/dephasing and reference factors;
- independent reference degradation scales smoothly rather than as a
  consensus threshold; and
- a wrong collective basis hides undephased coherence.

Run:

```bash
python3 tests/du_regional_reference_alignment_gate_probe.py \
  --write-artifact
```

The artifact is
`artifacts/du_regional_reference_alignment_gate_result.json`. Passing
establishes only the scoped reference/access formulas and controls. It does
not select a reference, regional factorization, record, provenance join,
observer, consensus rule, preferred frame, collapse law, new physics, paper,
hardware, provider, or later scientific action.

## HC-DU-175 relational-reference symmetry-reduction gate

`du_relational_reference_symmetry_reduction_probe.py` preserves the exact
finite controls behind the reference-generation boundary:

- \(|10\rangle\langle10|\) is invariant under independent local
  \(U(1)^2\) phases;
- full-local-covariance controls create no
  \(|10\rangle\langle01|\) character mode;
- the exchange Hamiltonian conserves total excitation while breaking each
  separate local-number symmetry;
- quarter-swap evolution creates magnitude-\(1/2\) relational coherence
  while both local reduced states remain diagonal;
- the coherence is reversible and therefore is not itself a record;
- local coordinate changes move the coupling and state together while
  common phase remains free;
- physical run-to-run phase randomization erases the system-only mode;
- a retained phase relation restores the conditional mode;
- reusing the same stable coupling embodies the reference for a bounded
  action family; and
- a coupling mismatch \(\delta\) gives exact return probability
  \(\cos^2(\delta/2)\).

Run:

```bash
python3 tests/du_relational_reference_symmetry_reduction_probe.py \
  --write-artifact
```

The artifact is
`artifacts/du_relational_reference_symmetry_reduction_result.json`. Passing
establishes only the scoped character-mode, symmetry-reduction, and
action-relative reference controls. It does not select a material archive,
occurrence provenance, portable certificate, observer, public finality, new
physics, paper, hardware, provider, or later scientific action.

## HC-DU-176 stage–resource–persistence separation

`du_stage_resource_persistence_separation_probe.py` preserves the exact
finite controls behind the scoped joint-target theorem and blocks the
universal ladder as an inference from differently scoped typed results:

- exhaustive four-history archives satisfy the joint-target criterion iff
  they satisfy both component criteria;
- stage plus persistence need not carry a nontrivial relational character;
- relational character plus persistence need not carry formation
  provenance;
- stage plus character need not persist to the declared horizon;
- a supplied all-three architecture is an exact positive control;
- horizon evolution may erase nuisance detail while retaining the target;
- merging distinct target classes is exactly a persistence failure; and
- a persistent terminal value need not certify that a write occurred.

Run:

```bash
python3 tests/du_stage_resource_persistence_separation_probe.py \
  --write-artifact
```

The artifact is
`artifacts/du_stage_resource_persistence_separation_result.json`. Passing
establishes only the scoped factorization, persistence, and logical
target-independence controls in the abstract fixture. It does not prove
independent physical realizability or select a physical stage, symmetry
resource, material archive, common response object, hyperbolic dynamics,
observer, finality, new physics, paper, hardware, provider, or later
scientific action.

## HC-DU-179 material-trace lineage boundary

`du_material_trace_lineage_probe.py` preserves the exact finite controls
behind the distinction between a material marked-site field and causal
lineage:

- the cycle graph \(C_4\) has two admissible perfect path covers;
- both covers produce the same four-site material record while assigning
  different same-source edges;
- the marked-site record exactly factors local material formation but not
  path membership;
- a physical edge tag repairs lineage factorization;
- narrowing the admissible graph to a path makes the cover unique without
  changing the record;
- a time-insensitive undirected segment does not determine traversal
  direction;
- an ordered endpoint tag repairs direction; and
- deterministic development or scanning of the same latent field cannot
  restore lineage already lost in its fibre.

Run:

```bash
python3 tests/du_material_trace_lineage_probe.py --write-artifact
```

The artifact is
`artifacts/du_material_trace_lineage_result.json`. Passing establishes only
the finite site/path and direction factorization boundaries. It does not
model nuclear-emulsion chemistry, prove the physical realization of the
four-site witness, identify a particle or source, timestamp an event, select
a readout or archive, establish new physics, or authorize later work.

## HC-DU-180 oriented-trace and head-tail boundary

`du_oriented_trace_head_tail_probe.py` preserves the exact finite controls
behind the distinction between an unoriented spatial axis, a physically
polarized response profile, and a bounded-error orientation certificate:

- an unweighted three-site axis does not factor traversal direction;
- a reflection-asymmetric profile factors direction in a frozen noiseless
  response class;
- a centered reflection-odd moment changes sign under path reversal;
- a reflection-symmetric profile carries no orientation information;
- overlapping orientation-conditioned laws give total variation \(3/5\)
  and minimum equal-prior error \(1/5\), not zero error;
- disjoint laws give exact orientation;
- a noisy downstream readout contracts total variation from \(3/5\) to
  \(3/10\);
- axis-only coarse-graining erases head-tail information; and
- a known source label can repair a joint packet while remaining imported
  side information rather than intrinsic detector provenance.

Run:

```bash
python3 tests/du_oriented_trace_head_tail_probe.py --write-artifact
```

The artifact is
`artifacts/du_oriented_trace_head_tail_result.json`. Passing establishes only
finite orientation factorization, binary-testing, and data-processing
boundaries. It does not model TPC physics, prove persistent material
orientation, certify any experimental event with zero error, establish path
membership, event time, particle identity, selected calibration/readout,
new physics, or later scientific action.

## HC-DU-181 selected-interface round-trip boundary

`du_selected_interface_round_trip_probe.py` preserves the exact finite
controls behind the conditional GU-to-record-to-DU closed loop:

- each of two named direct/flipped interfaces has its own exact decoder;
- the same pair fails to admit one untagged decoder because cross-interface
  record-law collisions mix target values;
- retaining interface identity repairs the collision by enlarging the
  record packet;
- a selected informative interface closes the law-level round trip;
- selecting a constant interface does not create identifiability;
- no selector is needed when the target descends across the complete
  interface family;
- distinct overlapping laws identify the target at law level while
  forbidding a zero-error event decoder;
- disjoint target-conditioned supports give an exact event decoder;
- a common noisy readout contracts total variation from \(3/5\) to \(3/10\);
- a common readout cannot repair equal upstream laws; and
- physical record and target maps must descend through the declared gauge
  quotient.

Run:

```bash
python3 tests/du_selected_interface_round_trip_probe.py --write-artifact
```

The artifact is
`artifacts/du_selected_interface_round_trip_result.json`. Passing establishes
only finite factorization, cross-interface ambiguity, support separation,
gauge-descent, and data-processing boundaries. It does not construct a GU
flag or source action, select a detector/archive/observer, prove a physical
GU--DU round trip, establish new physics, or authorize a later campaign wave.

## HC-DU-182 time-resolved TPC acquired-packet boundary

`du_time_resolved_tpc_record_packet_probe.py` preserves the exact finite
controls behind the source-pinned negative-ion TPC audit:

- one carrier records event-time-plus-depth and separately identifies
  neither target;
- two distinct calibrated carrier velocities give a nonzero determinant and
  exact conditional reconstruction of event time and depth;
- duplicate carrier speed does not repair the rank deficiency;
- one raw hit packet admits different event-membership partitions;
- a physically retained event tag repairs the finite partition fixture;
- deterministic clustering of the common packet does not create occurrence
  provenance;
- a lossless archive cannot repair an absent minority peak; and
- a joined acquisition packet need not factor source identity.

Run:

```bash
python3 tests/du_time_resolved_tpc_record_packet_probe.py --write-artifact
```

The artifact is
`artifacts/du_time_resolved_tpc_record_packet_result.json`. Passing
establishes only finite rank and factorization boundaries. It does not model
TPC physics, select a trigger/event builder/archive, prove universal
minority-carrier detection, establish head-tail sense or source identity,
combine duties from different detector platforms, reveal new physics, or
authorize a later campaign wave.

## HC-DU-183 dual-phase S1/S2 event-pairing boundary

`du_dual_phase_s1_s2_pairing_probe.py` preserves the exact finite controls
behind the source-pinned dual-phase xenon audit:

- one drift-time window can admit two exact S1/S2 perfect matchings;
- raw triggerless peaks then fail to factor event pairing and paired depths;
- a retained common event tag repairs both targets by record refinement;
- a uniquely matchable compatibility graph repairs conditionally by
  completion narrowing;
- correctly paired S1/S2 delay reconstructs depth;
- S2 alone does not separate detector-relative event time and depth;
- a lossless triggerless archive does not create pairing provenance;
- overlapping S2/S1-style response laws do not give zero-error class
  certification; and
- a complete detector packet need not factor upstream source identity.

Run:

```bash
python3 tests/du_dual_phase_s1_s2_pairing_probe.py --write-artifact
```

The artifact is
`artifacts/du_dual_phase_s1_s2_pairing_result.json`. Passing establishes
only finite matching and factorization boundaries. It does not simulate
xenon response, estimate accidental-coincidence rates, select an event
builder/archive/observer, certify path polarity or source identity, reveal
new physics, or authorize a later campaign wave.

## HC-DU-184 DRIFT joined depth/head-tail boundary

`du_drift_joined_depth_head_tail_probe.py` preserves the exact finite
controls behind the source-pinned DRIFT-IId audit:

- one packet can join multi-carrier depth timing and a head-tail statistic;
- distinct carrier velocities retain full depth rank;
- a missing minority peak restores the one-carrier depth ambiguity;
- orientation-conditioned ensemble means can reverse while event laws
  overlap with nonzero optimal error;
- replication strengthens ensemble detection without certifying one event;
- disjoint laws give the exact zero-error positive control;
- known calibration-source geometry repairs an ambiguous event only by
  imported side information;
- the joined packet need not factor recoil species; and
- triggered acquisition does not force path orientation.

Run:

```bash
python3 tests/du_drift_joined_depth_head_tail_probe.py --write-artifact
```

The artifact is
`artifacts/du_drift_joined_depth_head_tail_result.json`. Passing establishes
only finite rank, binary-testing, and factorization boundaries. It does not
simulate DRIFT, resolve its reported systematics, certify any event's path
sense or source, reveal new physics, or authorize a later campaign wave.

## HC-DU-185 predictive versus representational absorption

`du_predictive_vs_representational_absorption_probe.py` preserves the exact
finite controls behind the corrected response reopener:

- two laws can share every training value and disagree held out;
- a universal response family can represent both without predicting either;
- target-blind challenger selection adds a locked prediction;
- target constancy on the frozen incumbent fibre is the positive control;
- choosing a matching law after reveal remains refitting;
- first nonzero response-difference order survives a nonsingular source
  reparameterization but can move under a singular map; and
- selecting a response law does not select a physical record interface.

Run:

```bash
python3 tests/du_predictive_vs_representational_absorption_probe.py --write-artifact
```

The artifact is
`artifacts/du_predictive_vs_representational_absorption_result.json`. Passing
establishes only the predictive-absorption and coordinate boundaries. It does
not refute a standard response formalism, select a physical coefficient or
interface, reveal new physics, or authorize a later campaign wave.

## HC-DU-186 predictive-excess trichotomy

`du_predictive_excess_trichotomy_probe.py` preserves the exact controls behind
the corrected modular experiment gate:

- absorption, predictive sharpening, and rival-excluding excess are
  exhaustive for one locked challenger target;
- a resolving interface preserves rival excess while a coarse interface can
  erase it;
- a readout cannot create a distinction from identical raw predictions;
- response and acquisition selectors can be independently frozen;
- a quadratic three-configuration response escapes a preregistered affine
  nuisance family by its second finite difference; and
- one free scalar nuisance absorbs one single-configuration scalar delta.

Run:

```bash
python3 tests/du_predictive_excess_trichotomy_probe.py --write-artifact
```

The artifact is
`artifacts/du_predictive_excess_trichotomy_result.json`. Passing establishes
only finite prediction-relation, readout, modular-composition, and
response-shape boundaries. It validates no CSL or gravity law, complete
nuisance class, observed anomaly, new physics, or later campaign wave.

## HC-DU-187 reversible-pointer CSL three-width prediction lock

`du_csl_three_width_prediction_lock_probe.py` preserves the exact finite
controls behind the hardened `PRED-DU-005` response geometry:

- one contrast annihilates a shared path-loss column and a width-linear
  timing-loss column;
- a strictly convex breathing response survives that contrast;
- two widths are saturated by the two unknown nuisance coefficients;
- three widths restore rank in the frozen minimal model;
- force-only scans retain the known CSL/environment collinearity;
- arbitrary configuration-specific nuisance terms kill attribution; and
- the paper's baseline/aggressive pair is not a matched-width-only control.

Run:

```bash
python3 tests/du_csl_three_width_prediction_lock_probe.py --write-artifact
```

The artifact is
`artifacts/du_csl_three_width_prediction_lock_result.json`. Passing
establishes only finite rank, contrast, and prediction-lock boundaries. It
does not validate CSL, a complete nuisance family, the proposal's engineering
estimates, an apparatus, an observed anomaly, new physics, or a later
campaign wave.

## HC-DU-188 reversible-pointer CSL conditioning boundary

`du_csl_three_width_conditioning_probe.py` preserves the numerical learning
gate behind the local stop on `PRED-DU-005`:

- both rounded v4 breathing factors are reproduced;
- Simpson-grid convergence is checked;
- a wide `q=(10,20,50)` redesign retains a finite but exposure-expensive
  contrast;
- source-near preparation ratios make the contrast catastrophically
  ill-conditioned; and
- useful curvature requires preparation frequencies orders below the
  source-analyzed setting.

Run:

```bash
python3 tests/du_csl_three_width_conditioning_probe.py --write-artifact
```

The artifact is
`artifacts/du_csl_three_width_conditioning_result.json`. Passing establishes
only a source-model numerical conditioning and local-stop boundary. The shot
counts are optimistic diagnostics, not device forecasts. It validates no CSL
parameter, complete nuisance model, apparatus, observed anomaly, new physics,
hardware action, or later campaign wave.

## HC-DU-189 quantum-gravity phase-family boundary

`du_quantum_gravity_phase_family_boundary_probe.py` preserves the exact
controls behind the Chen--Giacomini phase-family split:

- the wide-source cross phase depends on both source profiles;
- the displayed commutator phases contain no source dependency;
- the commutator contribution survives source deletion, cancels from a pure
  source-branch comparison, and can distinguish probe branches;
- a rank-one isotropic stress has transverse-traceless fraction (4/15);
- the combined coefficient is (61/360) times the unprojected Gaussian
  integral;
- halving Gaussian probe width multiplies that integral by eight;
- the point-probe limit diverges and equal integrated stresses with different
  widths give different phases; and
- omitted probe self-gravity enters at the same formal perturbative order.

Run:

```bash
python3 tests/du_quantum_gravity_phase_family_boundary_probe.py --write-artifact
```

The artifact is
`artifacts/du_quantum_gravity_phase_family_boundary_result.json`. Passing
establishes only the displayed dependency, source-deletion, Gaussian-profile,
angular-projection, and perturbative-order boundaries. It does not simulate
quantum gravity, validate either paper, select a probe profile or apparatus,
identify a source--probe mediator, reveal new physics, or authorize a later
campaign wave.

## HC-DU-190 wide-source local-energy spectral boundary

`du_quantum_gravity_wide_source_preparation_probe.py` preserves the exact
controls behind the Chen--Giacomini preparation gate:

- local energy cells sum to the global source Hamiltonian;
- the frozen global source Hamiltonian is positive definite;
- positive hopping makes the two local cells noncommuting and removes their
  common eigenvectors;
- a spatially wide state remains an exact global-energy eigenstate with zero
  mean current while retaining nonzero local variances and commutator action;
- the commuting limit has localized exact profiles whose cross-source kernel
  is exactly the lattice Newton potential;
- coarsening to total mass erases spatial shape; and
- replacing a profile-valued phase distribution by its mean can erase a
  visibility loss.

Run:

```bash
python3 tests/du_quantum_gravity_wide_source_preparation_probe.py --write-artifact
```

The artifact is
`artifacts/du_quantum_gravity_wide_source_preparation_result.json`. Passing
establishes only the finite global-energy/local-profile, joint-spectrum,
commuting-Newton, coarse-graining, and phase-averaging boundaries. It proves
no universal QFT no-go, refutation of the published algebra, apparatus,
observed effect, hardware action, new DU law, or later campaign wave.

## HC-DU-191 wide-source model tournament and cumulant reopener

`du_quantum_gravity_source_model_tournament_probe.py` preserves the exact
controls behind the many-body source classification:

- an $N$-boson Hartree mode has binomial local occupation with variance
  $Np(1-p)$ and relative noise $O(N^{-1/2})$;
- its exact phase characteristic differs from the phase of its mean profile;
- at fixed accumulated mean phase, that discrepancy vanishes at the
  mean-field $1/N$ rate;
- a fragmented local-number state has an exact broad profile whose bilinear
  density-kernel phase is the classical extended-density functional;
- a translated-profile cat retains local variance;
- Hartree and fragmented states with the same mean density differ first in
  higher cumulants and visibility;
- a coherent-field occupation analogue remains Poissonian; and
- a number-diagonal classical mixture reproduces the diagonal phase
  characteristic, while complementary coherence distinguishes it from the
  pure Hartree source.

Run:

```bash
python3 tests/du_quantum_gravity_source_model_tournament_probe.py --write-artifact
```

The artifact is
`artifacts/du_quantum_gravity_source_model_tournament_result.json`. Passing
establishes only finite occupation-statistics, classical density-kernel,
concentration, cumulant, and complementary-coherence boundaries. It proves no
universal QFT no-go, Chen--Giacomini refutation, unique quantum-gravity
witness, apparatus, observed effect, hardware action, new DU law, or later
campaign wave.

## HC-DU-192 same-mean/different-cumulant rival hierarchy

`du_quantum_gravity_cumulant_rival_prediction_probe.py` preserves the exact
finite controls behind the rival-prediction tournament:

- same-mean Hartree and fragmented sources have different second cumulants;
- expectation-value-only closure identifies them while a profile-sensitive
  phase channel gives different visibility;
- a classical profile lottery reproduces the full diagonal characteristic;
- Gaussian stochastic noise matches the first two cumulants but misses the
  nonzero third cumulant at the expected cubic order;
- complementary coherence excludes a pre-existing incoherent source mixture;
- a controlled profile phase crosses an exact separable-channel witness bound;
- copy--phase--uncompute mediation and direct action are endpoint-equivalent;
  and
- intermediate mediator access separates those implementations.

Run:

```bash
python3 tests/du_quantum_gravity_cumulant_rival_prediction_probe.py --write-artifact
```

The artifact is
`artifacts/du_quantum_gravity_cumulant_rival_prediction_result.json`. Passing
establishes only the scoped observable/rival hierarchy and endpoint mediation
nonidentification. It proves no universal classical-gravity no-go, unique
quantum-gravity witness, observed effect, apparatus, material interface,
hardware action, new DU law, or later campaign wave.

## HC-DU-193 matched-noise response and ordered-spectrum boundary

`du_quantum_gravity_matched_noise_response_probe.py` preserves the exact
finite controls behind the response-rival boundary:

- calibrated KMS symmetrized noise and dissipative response obey one quantum
  fluctuation--dissipation relation;
- a real classical Gaussian process exactly reproduces the quantum
  symmetrized harmonic covariance;
- a classical input--output model can copy the causal c-number response;
- that copy does not supply the quantum ordered-correlation imaginary part;
- a thermal quantum spectrum has emission/absorption asymmetry while a real
  stationary commuting scalar spectrum is even;
- two calibrated frequencies reject one classical equilibrium temperature;
- the quantum contrast has an exact strict-monotonicity certificate; and
- the classical FDT is recovered in the high-temperature limit.

Run:

```bash
python3 tests/du_quantum_gravity_matched_noise_response_probe.py --write-artifact
```

The artifact is
`artifacts/du_quantum_gravity_matched_noise_response_result.json`. Passing
establishes only the scoped KMS dependency, classical realization,
commuting-noise exclusion, two-frequency equilibrium-FDT discriminator, and
field-attribution stop. It proves no universal classical-gravity no-go, unique
quantum-gravity witness, observed effect, apparatus, material interface,
hardware action, new DU law, or later campaign wave.

## HC-DU-194 graviton-noise commutative Gaussian record boundary

`du_graviton_noise_commutative_gaussian_record_probe.py` preserves the exact
finite controls behind the primary-source disposition:

- the vacuum symmetrized kernel has an explicit positive classical Gaussian
  factorization;
- the complete Gaussian characteristic functional and Wick moments match;
- squeezed nonstationary kernels factor through classical quadratures across
  three source parameters;
- deterministic nonlinear detector processing preserves the absorption;
- two-detector correlations have a shared classical common-cause model;
- one no-refit classical spectral law copies the full vacuum power surface;
- the commutative record erases the ordered imaginary component; and
- an energy-selective ordered rate is outside the classical arm record.

Run:

```bash
python3 tests/du_graviton_noise_commutative_gaussian_record_probe.py --write-artifact
```

The artifact is
`artifacts/du_graviton_noise_commutative_gaussian_record_result.json`.
Passing establishes only the scoped commutative-record nonidentification,
classical realizations, ordering-erasure boundary, and quantum-process
reopener. It proves no source-paper error, universal stochastic-gravity no-go,
unique quantum-gravity witness, observed effect, apparatus, selected material
interface, hardware action, new DU law, or later campaign wave.

## HC-DU-195 pre-saddle quantum-detector channel boundary

`du_pre_saddle_quantum_detector_channel_probe.py` preserves the exact finite
controls behind the harmonic-trap source disposition:

- every classical random-Hamiltonian mixture is unital;
- vacuum amplitude damping is nonunital and lies outside that rival class;
- downward-without-upward transition retains the bosonic vacuum term;
- a real stationary classical force has an even rate surface;
- an ordinary classical decay process copies the energy-basis record;
- a direct quantum ancilla copies the complete endpoint channel;
- finite switching replaces delta squared with a bounded resonance window; and
- two independently fixed trap gaps select two resonance frequencies.

Run:

```bash
python3 tests/du_pre_saddle_quantum_detector_channel_probe.py --write-artifact
```

The artifact is
`artifacts/du_pre_saddle_quantum_detector_channel_result.json`. Passing
establishes only the scoped random-unitary obstruction, endpoint attribution
stop, harmonic-trap source correction, and finite-time contract boundary. It
proves no universal classical- or semiclassical-gravity no-go, unique graviton
witness, observed effect, finite apparatus, selected mediator record, hardware
action, new DU law, or later campaign wave.

## HC-DU-196 finite trapped-detector process and dilation boundary

`du_finite_time_trapped_detector_dilation_probe.py` preserves the exact finite
controls behind the process-dilation disposition:

- the resonant two-state exchange block is unitary and bounded;
- its weak-coupling limit recovers the finite sinc-squared window;
- the reduced detector map is trace preserving and nonunital;
- one direct quantum ancilla copies the complete channel on a spanning input
  set and one predeclared coupling family copies two gaps;
- Kraus rank forces a minimum two-dimensional pure environment without
  identifying it;
- the complementary channel carries the detector's lost population and
  coherence;
- a full swap moves the complete input record out of the detector;
- an environment isometry changes mediator records without changing the
  detector channel; and
- single-mode revival excludes only an irreversible memoryless semigroup.

Run:

```bash
python3 tests/du_finite_time_trapped_detector_dilation_probe.py --write-artifact
```

The artifact is
`artifacts/du_finite_time_trapped_detector_dilation_result.json`. Passing
establishes only the scoped finite-channel construction, minimal-memory
invariant, detector-only dilation nonidentification, and interface-expansion
necessity. It proves no complete continuum detector theory, universal
direct-action equivalence, unique graviton witness, selected expanded port,
observed effect, hardware action, new DU law, or later campaign wave.

## HC-DU-197 source–mediator–detector causal-cut boundary

`du_source_mediator_causal_cut_probe.py` preserves the exact finite controls
behind the relative mediation disposition:

- natural serial mediation and a fixed direct-edge rival have the same
  source-conditioned detector response;
- one replacement of the candidate port still leaves the two responses
  identical;
- the missing replacement separates them;
- exhaustive enumeration of all 16 Boolean responses yields the completion
  count `4 -> 2 -> 1` for natural, one-cut, and complete replacement surfaces;
- the complete response decides direct source dependence at fixed port value;
- the operationally complete port record remains identical under two distinct
  physical implementation labels; and
- source settings, intervention arms, and detector rows remain explicitly
  joined.

Run:

```bash
python3 tests/du_source_mediator_causal_cut_probe.py --write-artifact
```

The artifact is `artifacts/du_source_mediator_causal_cut_result.json`. Passing
establishes only one-cut insufficiency, finite relative causal-bottleneck
identification, and physical-label nonfactorization. It proves no gravitational
mediator, complete quantum-field port, observed causal break, selected physical
interface, Grade-5 remainder, hardware action, new causal theorem, or later
campaign wave.

## HC-DU-198 constraint-compatible gravity intervention boundary

`du_constraint_compatible_intervention_probe.py` preserves the exact finite
controls behind the lawful-action correction and radiative reopener:

- the full binary source--port cube has four points while `M=S` admits two;
- both off-surface cuts violate the frozen constraint;
- mediated `D=M` and direct `D=S` presentations agree on every lawful
  near-field action;
- the full mathematical cube would separate them only by using off-law cuts;
- an independently variable radiative input separates a near-field-only rival;
- a response-equivalent direct presentation survives that radiative test;
- no reviewed gravitational platform supplies all eight packet fields; and
- a complete native cavity/phonon analogue transfers no gravity attribution.

Run:

```bash
python3 tests/du_constraint_compatible_intervention_probe.py --write-artifact
```

The artifact is
`artifacts/du_constraint_compatible_intervention_result.json`. Passing
establishes only the scoped lawful-intervention, constrained-duality,
radiative-response, ontology, and source-bounded platform-audit boundary. It
proves no direct-action gravity, field ontology, quantized gravity,
experimental impossibility, observation, complete gravitational packet,
Grade-5 remainder, hardware action, new gravity law, or later campaign wave.

## HC-DU-199 gravitational-radiation Gaussian tomography boundary

`du_gravitational_radiation_gaussian_tomography_probe.py` preserves the exact
finite controls behind the radiative reconstruction and evidence-formation
boundary:

- known nonzero transfer exactly reconstructs incident Gaussian moments;
- two distinct physical input/transfer pairs have the same detector covariance
  at one receiver setting when transfer is not calibrated;
- two known receiver references recover transfer from their response slope
  when the source is fixed across arms;
- three quadrature phases span a one-mode covariance while two leave the cross
  covariance unidentified;
- a two-quantum input has $g^{(2)}=1/2$ at two different transfers;
- the double-event probability remains proportional to $\eta^2$, imposing a
  one-hundredfold trial penalty for a tenfold smaller transfer;
- a sub-vacuum output excludes vacuum plus a classical random displacement;
  and
- a response-equivalent quantum ancilla remains observationally identical at
  the receiver.

Run:

```bash
python3 tests/du_gravitational_radiation_gaussian_tomography_probe.py --write-artifact
```

The artifact is
`artifacts/du_gravitational_radiation_gaussian_tomography_result.json`. Passing
establishes only conditional one-mode Gaussian reconstruction plus scoped
calibration, phase-design, finite-evidence, classical-rival, and ontology
boundaries. It proves no astrophysical state preparation, gravitational-wave
quantization, graviton observation, universal classical-gravity exclusion,
experimental feasibility, field ontology, Grade-5 remainder, hardware action,
new gravity law, active successor, or later campaign wave.

## D2 QD/SBS audit-gap witness (Q-0063 decoherence-null campaign)

`du_qd_sbs_audit_gap_witness_probe.py` executes discriminator D2 of the
frozen Q-0063 campaign plan
(`../explorations/decoherence-null-audit-layer-confrontation-campaign-scoping-2026-08-03.md`)
with exact rational arithmetic and no load-bearing floating point:

- exact controlled-rotation central-spin dynamics generate branching states
  whose proper fragments satisfy the raw quantum-Darwinism plateau
  $I(S{:}F)=H(S)$ exactly (certified spectral multiset equality) at $N=2$
  and, for half-environment fragments, at $N=4$;
- the same states fail every audited condition by finite exact margins:
  conditional-fragment overlap $3/5$, an exact NPT compression determinant
  ($-576/15625$ at $N=2$) certifying positive S:F discord, and a Holevo
  pointer-access gap of $\approx 0.18$ bits below the plateau;
- perfect records with system-independent correlated junk keep the exact
  plateau, perfect distinguishability, and zero discord while failing the
  SBS product form by one full bit of conditional fragment-fragment mutual
  information, uniformly in fragment number;
- mandatory controls: the ideal SBS state passes every audit, asymmetric
  overlaps break the exact plateau, and independent junk passes the
  independence audit; and
- the two-sidedness sweep records that in the ideal pure family at $N=8$
  plateau and audit co-occur asymptotically, locating the null's surviving
  corner.

Run:

```bash
python3 tests/du_qd_sbs_audit_gap_witness_probe.py
```

The deterministic receipt is
`artifacts/du_qd_sbs_audit_gap_witness_result.json` and reports `16/16` with
byte-identical reruns. Passing establishes only the scoped exact finite
witness: plateau-with-failed-audit states exist at realizable scales, so raw
and audited redundancy differ empirically per the frozen D2 table. The audit
conditions witnessed are exactly the published SBS/strong-quantum-Darwinism
conditions; the probe establishes no new physics, mechanism, consensus
ontology, grade movement, banking, prediction, paper, hardware, provider,
publication, or other external action. The results note is
`../explorations/qd-sbs-audit-gap-witness-d2-execution-2026-08-03.md`.

## Forty-lens common-view-selector A/B vote

`du_common_view_selector_40_lens_vote_probe.py` audits the exploratory
common-view-selector portfolio assessment. It validates:

- twenty computational and twenty mathematical/physical lenses;
- one explicit Grade-0 hypothesis, decisive test, and absorber per lens;
- separate complete 100-credit linear and quadratic ballots;
- exclusion of every self-vote;
- reconciliation to 4,000 credits in each arm;
- complete deterministic A/B rankings; and
- descriptive disciplinary-distance and cross-family support metadata.

The artifact is
`artifacts/du_common_view_selector_40_lens_vote_result.json` and reports `7/7`
checks. Linear allocation favors `P35`, Covariant Action-Response Closure;
quadratic allocation and the social-distance bridge measure favor `P30`, the
Interventional Causal-State Selector. The vote therefore selects an attempt
order—`P35 -> P30 -> P33`, with `P40/P31` as the obstruction branch—not a
scientific winner. Passing proves only the ballot contract and arithmetic.
Every hypothesis remains Grade 0; no claim, prediction, physical selector,
novelty judgment, paper, hardware action, or successor is established.
