---
title: "Heralded Bell records: prescription, execution, and deferred-correction boundary"
status: banked_source_audit_and_exact_type_boundary
doc_type: exploration
created: 2026-08-31
claim_id: HC-DU-203
run_id: RUN-20260831-141529-bell-prescription-execution-audit
program_id: CCR-MINIMAL-PHYSICAL-ANTECEDENT-TO-FINITE-REMAINDER
owner_repo: dynamic-unity
evidence_grade: 4
---

# Executive result

`HC-DU-201` correctly reconstructed the source paper's eight Bell outcomes and
their two-bit quotient into four Pauli labels. `HC-DU-202` correctly showed
that this quotient is minimal only for that frozen correction family. The
primary-source audit in this swing narrows what physical capability those
results establish.

Arenskötter et al. physically form the eight-outcome Bell record, condition
target-photon tomography on that record, and reconstruct four branchwise
process matrices. They derive which Pauli rotation would reveal the prepared
input state. The paper does **not** report an outcome-conditioned Pauli gate on
the target photon or an adaptive quantum controller consuming that label for
arbitrary downstream use. Its documented target workflow is successive
polarization tomography, event binning, conditional evaluation, and maximum-
likelihood process reconstruction.

The corrected ladder is therefore:

```text
formed Bell record
  -> correction prescription / Pauli frame
  -> compatible terminal-statistic recovery
  -> enacted adaptive quantum continuation.
```

The first three rungs are physically and mathematically supported in the
scoped terminal-tomography setting. The fourth is a further implementation
contract, not something the record enacts by existing.

This does not invalidate conditional teleportation. A physical Pauli gate is
not always necessary: Pauli byproducts can be tracked classically and absorbed
into later compatible measurements or adaptive operations. But that standard
equivalence makes the DU distinction sharper rather than weaker:

> A record-to-policy map is not yet a record-to-enacted-capability map. The
> record must be consumed by a physically realized correction, frame tracker,
> adaptive measurement, or other continuation appropriate to the claimed
> task.

The source-grounded correction is Grade 3. The exact necessity/type boundary
is scoped Grade 4. Standard teleportation, Pauli-frame tracking, quantum
instruments, and deferred measurement absorb the physics and mathematics. No
new dynamics, physical selector, empirical excess, paper, or successor is
earned.

# Frozen source audit

The primary source is Arenskötter et al.,
[“Full Bell-basis measurement of an atom-photon 2-qubit state and its
application for quantum networks”](https://doi.org/10.1103/PhysRevResearch.6.023061),
*Physical Review Research* 6, 023061 (2024), also available as
[arXiv:2301.06091](https://arxiv.org/abs/2301.06091).

## What the paper reports

1. Passage, herald polarization, and atomic projection produce eight physical
   measurement outcomes.
2. Equations (10)--(13) group those outcomes into four Bell projections.
3. Successful events are binned by input phase; the target photon is measured
   successively in the `H/V`, `D/A`, and `R/L` polarization bases.
4. Those probabilities enter a maximum-likelihood reconstruction of a process
   matrix conditioned on each Bell outcome.
5. The four reconstructed branches identify `I`, `X`, `Y`, or `Z` as the
   rotation required to reveal the prepared input.

## What the paper does not report

- a real-time outcome-conditioned Pauli gate applied to target photon B;
- a live Pauli-frame controller propagating the outcome through arbitrary
  later quantum operations; or
- an implementation-complete archive of rejected attempts and controller
  memory.

The paper's unrelated use of the phrase “feed-forward stabilization” concerns
magnetic-field compensation coils, not teleportation correction. Its “with
correction” tables concern documented data corrections such as background and
phase-binning treatment; they are not evidence of an outcome-conditioned
physical Pauli gate.

This audit makes no claim that such a gate could not be added. It says only
that it is not part of the reported evidence and therefore cannot carry the
grade of `HC-DU-201` or `HC-DU-202`.

# Exact algebraic boundary

Let `r` be the retained Bell outcome and let `P_r` be its Pauli byproduct. For
an ideal input state `rho`, the conditional target state is

```text
rho_r = P_r rho P_r.
```

## Record ignored

If the four branches are uniform and `r` is discarded,

```text
(1/4) sum_r P_r rho P_r = I/2.
```

The unconditional channel is completely depolarizing. Formation of the Bell
record is therefore not dispensable: the correlations live in the joined
classical--quantum object, not in the target marginal alone.

## Active correction

Because every Pauli is self-inverse up to phase,

```text
P_r rho_r P_r = rho.
```

An outcome-conditioned active correction restores the live target branchwise.

## Terminal deferred correction

For a terminal observable `M`, cyclicity of trace gives

```text
Tr[(P_r M P_r) rho_r] = Tr[M rho].
```

Thus a controller that retains `r` may conjugate the measurement frame or
reinterpret a compatible terminal result rather than applying `P_r` to the
hardware state. This is not merely hypothetical engineering. Pauli tracking
is standard in teleportation-based and fault-tolerant computation; Paler et
al., [arXiv:1401.5872](https://arxiv.org/abs/1401.5872), give an explicit
software tracking construction, while Childs, Leung, and Nielsen,
[arXiv:quant-ph/0404132](https://arxiv.org/abs/quant-ph/0404132), derive
measurement-based schemes with outcome feed-forward.

## Arbitrary downstream continuation

Terminal equivalence does not supply an unconstrained future quantum state.
To reproduce “correct, then apply `Lambda`,” a later controller must either:

1. physically apply the correction before `Lambda`;
2. propagate the Pauli frame through `Lambda` and adapt later operations; or
3. restrict the task to a terminal statistic for which outcome-dependent
   measurement/relabeling is sufficient.

A fixed continuation that ignores `r` generally fails. For example, an `X`
branch maps the `Z=+1` state to `Z=-1`; a fixed `Z` readout disagrees with the
corrected target. Multiplying that terminal result by the known frame sign
recovers the one statistic, but it does not recreate a live quantum state for
an arbitrary future interaction.

# What is selected and what remains supplied

| Object | Status in the source-pinned specimen |
|---|---|
| Eight-outcome Bell carrier | Physically formed |
| Two-bit Pauli label | Derived from source dynamics and detector outcomes |
| Correction prescription | Source-grounded |
| Conditional terminal tomography | Physically implemented and evaluated |
| Physical Pauli gate on target | Not reported |
| Pauli-frame propagation through later gates | Not reported |
| Arbitrary continuation algebra | Supplied / absent |
| Observer boundary and task | Engineered |
| Complete attempt lineage | Not acquired in the published packet |

This is the smallest concrete example yet of why DU must type a capability by
both a record and its consuming continuation:

```text
capability = formed record + accessible policy + physically realized consumer
             + declared task/resource/horizon contract.
```

The equation is a typing discipline, not a scalar law.

# Relation to the North Star

The swing corrects the strongest current physical positive without closing it.
The Bell apparatus still demonstrates a real material record, a nontrivial
record quotient, and source-grounded conditional response. What it no longer
supports is the shorthand “the record itself enacts correction capability.”

This strengthens the North-Star reopener:

> Find a physical mechanism that not only forms and types a record but also
> selects or realizes the continuation that consumes it, then test a held-out
> response without refit.

That is more precise than asking for another record metric or quotient. It
also blocks a recurring category error: process tomography can certify a
conditional channel without having implemented the correction channel whose
action it identifies.

# Absorber and novelty audit

The result is absorbed by mature quantum-information machinery:

- teleportation identities distinguish conditional byproducts from their
  corrections;
- Pauli-frame tracking defers hardware corrections;
- quantum instruments type the classical outcome jointly with the conditional
  quantum map; and
- adaptive/measurement-based computation explicitly consumes outcome records
  in later controls.

DU's contribution here is not a new teleportation theorem. It is the
source-audited separation of physical formation, prescription, terminal
equivalence, and enacted continuation inside the program's record/capability
grading system.

# Grade, kill, stop, and reopener

- **Grade 3:** source-grounded formed Bell record, branchwise process
  tomography, and correction prescription.
- **Scoped Grade 4:** exact necessity result that prescription and terminal
  deferred correction do not by themselves establish an enacted arbitrary
  continuation.
- **Cheapest kill of the stronger claim:** the source reports no
  outcome-conditioned target correction or arbitrary adaptive controller.
- **Stop:** do not infer a live corrected quantum state from a reconstructed
  process matrix; do not require a hardware Pauli gate when a fully specified
  frame-aware continuation is operationally equivalent; do not call terminal
  relabeling universal capability.
- **Reopen:** one source-pinned apparatus must retain the Bell label and
  physically consume it through an active correction or declared frame-aware
  continuation, then pass a held-out no-refit downstream task beyond terminal
  tomography.

# Exact executable control

`tests/du_bell_prescription_execution_probe.py` exhausts the four Pauli
branches and three traceless Pauli observables. It verifies:

1. ignoring a uniform record removes every Bloch component;
2. active branchwise correction restores all components;
3. terminal record-conditioned frame correction restores every Pauli
   expectation; and
4. a fixed continuation that ignores the record fails on an explicit `X`/`Z`
   witness.

The control validates only the algebra above. It does not validate the source,
infer unreported hardware, select an action algebra, or establish new physics.
