---
title: "Superconducting fluxoid topology-selected material-record formation and provenance boundary"
status: banked_scoped_topological_material_record_result
doc_type: exact_topology_formation_sufficiency_and_first_leak_boundary
created: 2026-09-02
claim_id: HC-DU-224
run_id: RUN-20260902-superconducting-fluxoid-topological-material-record
program_id: CCR-MINIMAL-PHYSICAL-ANTECEDENT-TO-FINITE-REMAINDER
owner_repo: dynamic-unity
evidence_grade: 4
maximum_evidence_grade: 4
---

# Executive result

`HC-DU-223` established that an action-derived gauge response can be exactly
sufficient for a target without being a material record. This wave asks the
next narrower question: does ordinary gauge-field matter contain a case in
which physical dynamics and topology form a retained record before an observer
reads it?

A superconducting ring supplies that positive control. After a condensate forms
with nonzero complex order parameter around the ring, the normalized phase is a
map

\[
u:S^1\longrightarrow U(1).
\]

Its winding number

\[
n=\frac{1}{2\pi i}\oint_{S^1}u^{-1}du\in\mathbb Z
\tag{1}
\]

is constant under every continuous deformation that keeps the order parameter
nonzero. Changing `n` requires a phase slip: the condensate amplitude must
vanish somewhere, allowing the phase map to leave `U(1)` and reconnect in a
different homotopy class. In the frozen circuit/London window, `n` determines
the persistent-current branch. The ring therefore carries a target-sufficient,
durable material distinction before a SQUID or transport readout interrogates
it.

This is the first clean material-record positive immediately downstream of the
recent response-family work. It is not a complete solution to the North Star.
The ring, material phase, environment, quench or write protocol, operating
window, orientation, and readout are supplied antecedents. Winding records the
topological sector, not the full condensate microstate, formation time, causal
route, or source identity. The experiments and topology are standard; the
earned Dynamic Unity increment is the exact typed result and its first leaks.

The disposition is:

```text
TOPOLOGY_SELECTS_MATERIAL_RECORD_COORDINATE
+ BLANK_TO_WRITTEN_FLUXOID_FORMATION
+ NONZERO_ORDER_PARAMETER_PROTECTS_WINDING
+ PHASE_SLIP_IS_THE_ERASURE_GATE
+ BINARY_WINDOW_TARGET_SUFFICIENCY
+ FULL_SECTOR_AND_PROVENANCE_FIRST_LEAK
+ READOUT_REVEALS_BUT_DOES_NOT_CREATE_RECORD
+ CONDITIONAL_MATERIAL_POSITIVE_NOT_UNIVERSAL_SELECTOR
+ DOES_NOT_COMPLETE_HC-DU-223_CHARGE_HANDOFF
+ NO_READY_SUCCESSOR
```

# 1. Frozen physical packet

The admitted chain is:

```text
normal state: condensate amplitude can vanish, so no winding record
  -> cooling or controlled preparation crosses the superconducting transition
  -> nonzero U(1) order parameter forms around a ring
  -> one integer winding/fluxoid sector is occupied
  -> a persistent-current branch is retained behind a phase-slip barrier
  -> an optional SQUID or transport circuit reads the already formed branch.
```

The candidate material record is `n`, or an explicitly restricted function of
it such as winding parity. The locked held-out target is the later persistent
current in a fixed circuit with fixed external flux and inductance. Exact
formation provenance and microscopic phase configuration are hostile targets.

This is a conditional physical packet. It does not claim that a source action
uniquely selects superconducting matter, a ring, a bath schedule, or a binary
memory window across all possible worlds.

# 2. The topology theorem and the erasure gate

Let the complex superconducting order parameter be

\[
\Psi(x)=|\Psi(x)|e^{i\theta(x)}.
\]

When `|Psi|>0` everywhere on the ring, the normalized field
`u=Psi/|Psi|` is well-defined. Homotopy classes of maps from the ring to the
phase circle satisfy

\[
[S^1,U(1)]\simeq\pi_1(U(1))\simeq\mathbb Z.
\tag{2}
\]

Therefore two nonvanishing configurations with different winding numbers
cannot be joined by a continuous path inside the nonvanishing configuration
space. Every physical path that changes winding must cross a configuration at
which `Psi=0` somewhere. In superconducting language that crossing is a phase
slip.

This theorem does two jobs that an arbitrary metastable memory does not:

1. it identifies the exact record coordinate selected by the carrier topology;
2. it identifies the exact structural gate through which the record can be
   changed or erased.

The theorem does not make the barrier infinite. Thermal or quantum phase slips
can occur. Finality is thus conditional on a declared time, temperature,
geometry, and error tolerance. Topological separation supplies protection, not
absolute permanence.

# 3. Formation is not readout

The normal phase is a genuine blank for this record type. When the condensate
amplitude vanishes, `u` and its winding number are undefined. Crossing into the
nonvanishing superconducting phase creates a configuration on which `n` is
defined. A passive quench may choose the sector stochastically; an engineered
drive may bias or write it deliberately. Either way, the material distinction
exists before the later readout.

This is stronger than a field being merely correlated with a source. The
fluxoid sector:

- is encoded in a physical condensate configuration;
- persists through ordinary small local disturbances;
- controls later persistent-current and switching responses; and
- can be changed only by crossing the identified phase-slip gate.

A SQUID or transport probe supplies access and transduction. It need not create
the sector it reports. Conversely, the existence of a sector does not select
one observer, readout circuit, calibration, archive, or public-finality rule.

# 4. Target-relative sufficiency and strict compression

In a standard thin-ring circuit model with fixed external flux
`phi_ext=Phi_ext/Phi_0`, the current branch has the form

\[
I_n=I_0(n-\phi_{\rm ext}),
\tag{3}
\]

where `I_0` is fixed by the circuit. Thus `n` is sufficient for the locked
branch-current target. It is not sufficient for the full microscopic state:
many phase-gradient configurations have the same total winding.

The exact finite control realizes this with a six-edge phase ring. Principal
increments take values in `{-2,-1,0,1,2}` modulo five, subject to closure. Local
gradient-redistribution moves preserve nonvanishing phase continuity. The 3,125
configurations split into exactly five connected components:

| winding | component size |
|---:|---:|
| -2 | 21 |
| -1 | 666 |
| 0 | 1,751 |
| 1 | 666 |
| 2 | 21 |

The components are exactly the winding fibres. This is a finite control of the
continuum homotopy theorem, not a replacement for it.

The model also separates a useful binary memory from the complete sector
family. In the declared window `n in {0,1}`, parity identifies the branch and
therefore determines the current. On the full family, parity merges `n=-1` and
`n=1`, which have different currents. Binary sufficiency is an operating-window
claim, not an intrinsic reduction of all fluxoid sectors to one bit.

# 5. Orientation and provenance first leaks

Reversing the orientation of the ring sends

\[
n\longmapsto -n.
\tag{4}
\]

Signed winding therefore presupposes an orientation convention or a physical
orientation reference such as the direction of an applied field and calibrated
coupling. Winding parity survives this reversal. An unoriented carrier can
select a `Z2` orbit while failing to select the signed integer coordinate.

The endpoint sector also loses provenance. A passive cool-through transition
and a field-biased engineered write can end in the same `n`. The retained
fluxoid then answers “which topological/current branch is the ring in?” but not:

- which source caused that branch;
- whether it formed passively or was written deliberately;
- when the transition occurred;
- which microscopic route reached it; or
- how many intermediate slips occurred.

These are same-record/different-provenance witnesses. Recovering those targets
requires a process record or additional source-bound lineage, not a more
confident reading of `n`.

# 6. Primary-source collision

The physical premises are independently established rather than inferred from
the finite model.

1. Monaco et al., *Spontaneous Fluxoid Formation in Superconducting Loops*
   (2009), observed fluxoid formation after cooling superconducting loops
   through the transition and studied its quench dependence:
   <https://arxiv.org/abs/0907.2505>.
2. Petkovic, Lollo, and Harris, *Phase-Slip Statistics of a Single Isolated
   Flux-Biased Superconducting Ring* (2020), measured thermally activated
   transitions between fluxoid states using independently characterized ring
   parameters: <https://doi.org/10.1103/PhysRevLett.125.067002>.
3. Ligato et al., *A superconducting phase-slip memory* (2021), engineered a
   winding-parity memory with controlled write/read operations and multi-day
   persistence: <https://doi.org/10.1038/s41467-021-25209-y>.

These sources establish physical formation, retention, readout, and phase-slip
transition controls in different regimes. They do not establish Dynamic
Unity's full provenance, observer-access, or universal-selection claims.

# 7. Absorbers, novelty, and grade

The components are absorbed by mature theory and engineering:

- homotopy and the degree of maps `S1 -> U(1)`;
- fluxoid quantization and London/Ginzburg--Landau theory;
- Kibble--Zurek spontaneous defect formation;
- thermal and quantum phase slips;
- persistent-current superconducting circuits; and
- fluxoid/phase-slip memories and SQUID readout.

No new superconducting prediction or topological theorem is claimed. The
scoped Dynamic Unity result is:

> A physical carrier can form a material record before readout when its
> dynamically occupied configuration space splits into topologically protected
> response sectors. The sector label is target-sufficient and strictly
> compressive; the permitted transition out of a sector locates the erasure
> gate, while orientation and causal provenance remain separately typed.

That earns scoped Grade 4 for selection/necessity and exact first-leak
localization. It earns no Grade-5 remainder, empirical excess, new law, source
issuance, universal finality, observer selection, or new physics.

# 8. Relation to the current theorem spine

This result advances the physical-record branch but does not literally finish
the `HC-DU-223` electric-charge handoff.

- `HC-DU-223` concerns electric matter current, enclosed charge, and electric
  Gauss flux.
- `HC-DU-224` concerns a superconducting condensate's phase winding, magnetic
  fluxoid, and persistent current.

Both live in `U(1)` gauge physics, but equality of gauge group notation is not
an interface. The new result proves that ordinary gauge matter contains a real
topology-selected material memory mechanism. It does not prove that the
Dirac--Maxwell electric boundary flux automatically writes into that mechanism
or that the source action selects the complete coupling between them.

The sharper architecture is now:

```text
law selects a response family
  -> a locked target may factor through a compressive response
  -> a material phase may supply a blank-to-written sector coordinate
  -> topology may protect that coordinate and identify its erasure gate
  -> a selected transducer must still couple the upstream response to that record
  -> provenance, access, consumer, reset, and finality remain separate burdens.
```

# 9. North-Star consequence and reopener

The result removes one possible overstatement from the research program: DU no
longer needs to ask whether known physics can form any observer-independent
material record before readout. It can. The live question is narrower and more
valuable:

> Under what physical antecedent does a source-selected response become coupled
> to a topology- or phase-selected material record whose retained quotient is
> sufficient for a locked downstream target and carries the required causal
> lineage?

Reopen only with one of:

1. an exact source-to-fluxoid transducer whose coupling is selected rather than
   target-fitted and whose record preserves the `HC-DU-223` electric-charge
   target;
2. a physical process record proving fluxoid provenance beyond endpoint sector;
3. an autonomous source-plus-environment derivation of the admitted ring,
   binary window, orientation, and writer/consumer coupling; or
4. a finite no-refit remainder after the complete record packet is admitted.

Until then, the portfolio remains `NO_READY_SUCCESSOR`.

# 10. Exact validation

`tests/du_superconducting_fluxoid_topological_record_probe.py` exhausts all
3,125 finite ring configurations and returns `12/12`:

- connected components equal winding sectors;
- winding is protected under admitted local deformations;
- an inter-sector change crosses the phase-slip gate;
- orientation reversal negates winding while preserving parity;
- winding determines the frozen persistent-current target;
- parity succeeds only in the declared two-sector window;
- microstate and provenance fail to factor through winding; and
- the normal blank has no winding while every admitted condensate state does.

The artifact is
`tests/artifacts/du_superconducting_fluxoid_topological_record_result.json`.
