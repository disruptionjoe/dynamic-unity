---
title: "Heralded Bell records: action quotient, resource normalization, and ontology boundary"
status: banked_scoped_physical_positive_and_boundary
doc_type: exploration
created: 2026-08-31
claim_id: HC-DU-201
run_id: RUN-20260831-132230-heralded-bell-record-roundtrip
program_id: CCR-MINIMAL-PHYSICAL-ANTECEDENT-TO-FINITE-REMAINDER
owner_repo: dynamic-unity
evidence_grade: 4
---

# Executive result

This swing finds a stronger physical positive than the sources reviewed in
HC-DU-142.  The ion--photon apparatus of Arenskötter et al. physically forms
and accesses a heralded Bell-measurement record which is immediately useful
for a later action on a remote photon.  In the ideal protocol:

1. the apparatus supplies eight raw record values,
   `r=(passage, herald, atom) in Z_2^3`;
2. those values factor exactly through the four-class quotient
   `q(r)=(passage, herald XOR atom) in Z_2^2`;
3. the two quotient bits are necessary and sufficient to select the correct
   Pauli action for an arbitrary unknown input qubit;
4. the discarded raw bit is action-null for that task, but can remain live for
   provenance, calibration, or fault diagnosis;
5. conditional teleportation fidelity does not by itself establish useful
   finite-horizon capability, because the apparatus is heralded and rare; and
6. no downstream processing of this record can discriminate quantum
   ontologies which induce the same instrument and record-conditioned target
   channel.

The result is a source-grounded physical record-to-capability positive and a
scoped Grade-4 minimality/boundary result.  It does **not** select the apparatus
or instrument from bare quantum laws, prove single-world actualization, supply
an implementation-complete census of all attempted events, distinguish a new
ontology, or predict new physics.  Standard teleportation, quantum-instrument,
data-processing, and resource-accounting theory absorb every component.

# Frozen source and evidential scope

The physical specimen is:

> J. Arenskötter et al., “Full Bell-basis measurement of an atom-photon
> 2-qubit state and its application for quantum networks,” *Physical Review
> Research* **6**, 023061 (2024),
> [DOI 10.1103/PhysRevResearch.6.023061](https://doi.org/10.1103/PhysRevResearch.6.023061).

The experiment uses a trapped `40Ca+` ion, a pair of entangled photons, a
heralded Raman absorption process, passage timing, herald polarization, and a
final ion-state projection.  Its Eqs. (10)--(13) map eight raw outcomes onto
four Bell states.  The corresponding two classical bits determine which of
four Pauli operations is required on the retained remote photon.

The source reports a mean teleportation process fidelity of `76(9)%` without
background correction and `81(5)%` with it.  These values support the physical
specimen; the local probe below does not independently validate them.  It
reconstructs only the finite truth table and the resource consequences of the
source-reported success probabilities.

No claim is made that a particular detector click is a complete ontology of
the event.  Tomographic states and reported fidelities are epistemic estimates
constructed from records; the ion, photons, interactions, detector changes,
and retained outputs are treated as physical.

# Typed physical ladder

The apparatus makes the record leg concrete:

```text
prepared ion + incoming photon
          |
          v
Raman absorption interaction
          |
          +--> 393-nm herald polarization h
          +--> first/second-passage timing p
          |
          v
ion-state projection a
          |
          v
raw acquired record r=(p,h,a)
          |
          v
action quotient q=(p,h XOR a)
          |
          v
Pauli correction on retained remote photon
          |
          v
conditional teleportation capability
```

This is not a derivation of the instrument from the quantum state.  The laser
sequence, reference bases, timing windows, detector channels, state
preparation, controller logic, correction map, tomography, and reset procedure
are engineered antecedents.  Given that apparatus, however, the record is
materially formed, retained long enough to be read, and causally used rather
than merely postulated by an external analyst.

# Result 1 — exact action-relative quotient

Encode first/second passage by `p in Z_2`, Raman-herald polarization by
`h in Z_2`, and ion projection by `a in Z_2`.  Define

```text
q : Z_2^3 -> Z_2^2
q(p,h,a) = (p, h XOR a).
```

The first quotient bit selects the Bell family, `Psi` or `Phi`.  The parity
bit selects its sign.  A convention-equivalent correction table is:

| Passage | `h XOR a` | Bell state | Correction |
|---:|---:|---|---|
| 0 | 0 | `Psi+` | `Y` |
| 0 | 1 | `Psi-` | `X` |
| 1 | 0 | `Phi+` | `Z` |
| 1 | 1 | `Phi-` | `I` |

Each correction class contains two raw records.  Therefore the correction map
factors through `q`, and `q` is sufficient for the ideal held-out task.  This
is an action-relative statement: it does not say the two raw records in one
class are physically identical for every possible investigation.

The one-bit difference between the raw record and the action quotient is an
explicit finite remainder relative to the correction task.  It is a useful
counterexample to both extremes:

- not every physically acquired distinction changes the immediate action; and
- task-irrelevance does not erase a distinction's possible audit value.

# Result 2 — two actionable bits are minimal

An exact deterministic protocol for an arbitrary unknown qubit must distinguish
four Pauli corrections.  Hence every exact action-sufficient quotient requires
at least four classes, or two bits.  This counting lower bound is attained by
`q`.

The hostile deletion controls give the finite operational loss:

- retain both quotient bits: ideal Haar-average fidelity `1`;
- erase passage or parity: optimal Haar-average fidelity `2/3`;
- erase both: optimal Haar-average fidelity `1/2`.

The `2/3` value is the classical unknown-qubit boundary.  The result is not
merely that two bits happen to occur in the paper: dropping either actionable
bit removes the ideal quantum advantage.  Dropping any single *raw coordinate*
also fails, because the sufficient two-bit object is a quotient involving a
parity, not an arbitrary pair of detector bits.

If the two actionable bits independently flip with probability `epsilon`, the
ideal Haar-average fidelity is

```text
F(epsilon) = 1/3 + (2/3)(1-epsilon)^2.
```

It exceeds `2/3` exactly when

```text
epsilon < 1 - 1/sqrt(2) ~= 0.292893.
```

This is a protocol-level error boundary, not a fit to the experimental data.

# Result 3 — conditional capability is not finite-horizon availability

The paper reports success under three denominators.  They cannot be silently
interchanged:

| Denominator | Combined success | Expected units/success | Units for 95% at least one | Units for 99% at least one |
|---|---:|---:|---:|---:|
| Experimental runs | `1.981e-4` | `5,048` | `15,121` | `23,245` |
| Generated photon pairs | `7.285e-7` | `1,372,684` | `4,112,192` | `6,321,440` |
| Photons arriving at the ion | `1.926e-5` | `51,921` | `155,541` | `239,104` |

These figures answer different resource questions.  A high fidelity
conditioned on a successful herald is compatible with a poor one-shot or
short-horizon capability.  A complete capability statement therefore needs at
least:

```text
(conditional correctness, success normalization, retry budget, time horizon,
 accepted/rejected lineage, reset assumptions).
```

The source reports aggregate attempts and coincidences, but the published
article is not treated here as an implementation-complete, shot-joined archive
of every accepted and rejected lower-level event.  That distinction remains
important if a future claim depends on absence of hidden memory or selection.

# Result 4 — downstream ontology nonidentification

Let two candidate physical theories induce the same frozen quantum instrument
`I`, the same distribution of accessible record values `r`, and the same
record-conditioned target channel `E_r`.  For any later archive, compression,
decision, or action map `D` that depends only on the accessible packet,

```text
D o (r,E_r)  is identical under the two theories.
```

This is immediate functorial/data-processing nonidentification: appending more
downstream record handling cannot reveal a distinction already erased at the
instrument/channel boundary.  Consequently, running this apparatus under
unitary, Bohmian, collapse, or other descriptions is not by itself a productive
ontology tournament when those descriptions make the same operational
predictions.  A discriminator must alter or constrain something upstream—the
instrument, finite response, success law, noise law, or other accessible
channel—without after-fact refitting.

This is also why the physical positive does not prove that records create
reality.  It proves that, in this apparatus, a formed record changes what an
agent can reliably do.

# Selection-versus-supply audit

| Object | Status in this specimen |
|---|---|
| Ion, photons, and their lawful responses | Physical |
| Raman herald, timing, and ion readout | Physically formed by the constructed apparatus |
| Raw record retention and controller access | Implemented conditionally in the apparatus |
| Two-bit action quotient | Derived from the frozen correction task |
| Pauli correction and conditional target recovery | Standard quantum protocol |
| Apparatus, reference bases, timing gates, controller, and task | Supplied/engineered |
| Unique record interface from bare quantum dynamics | Not selected |
| Complete occurrence identity for every lower-level attempt | Not established |
| Single-world actualization or preferred ontology | Not identified |
| Nonabsorbed finite prediction | None |

# Relation to the existing DU spine

## Correction to HC-DU-142

HC-DU-142 correctly found that its reviewed sources did not provide one
unchanged packet joining formation, individual actualization, archive/access,
provenance, reset, and action.  The present 2024 specimen was not in that source
set.  It materially advances the positive-control side by joining a physical
heralded record to a real conditional action and target recovery.

It does not close HC-DU-142's stronger actualization and implementation-lineage
requirements.  The correct update is therefore “stronger physical positive,
same selection boundary,” not “record selection solved.”

## Collision with HC-DU-200

HC-DU-200 showed that generic redundancy/objectivity theorems do not select an
observer-accessible fragment at a physical rate.  This apparatus does not infer
access from redundancy.  It engineers a definite detector/controller path and
thereby supplies an existence proof that access can be physically implemented.
The price is explicit: the access structure is part of the apparatus contract,
not selected from the system state alone.

## North-Star consequence

The North Star should retain three separately typed questions:

1. **formation:** which physical interactions create durable distinctions?;
2. **access and action:** which quotient of those distinctions is available and
   sufficient for a declared task?; and
3. **selection:** what physical antecedent, if any, selects that apparatus,
   interface, and quotient without using the target after the fact?

The experiment gives a strong positive for the first two under a supplied
apparatus.  The third remains open.

# Grade, absorber, disposition, and reopener

- **Earned:** scoped Grade 4 for the exact minimality and downstream
  nonidentification boundaries, plus a source-grounded physical positive for
  record-to-action capability.
- **Not earned:** new mechanism, new empirical prediction, ontology priority,
  interface selection, issuance, or a Grade-5 reconstruction theorem.
- **Strongest absorber:** ordinary quantum teleportation, heralded trapped-ion
  measurement, quantum instruments, data processing, and resource accounting.
- **Disposition:** bank HC-DU-201; do not activate a successor from it.
- **Reopen implementation lineage:** only for a source-pinned packet retaining
  every admitted attempt, rejection, reset, and controller-memory state when a
  held-out no-refit target makes those distinctions operationally necessary.
- **Reopen ontology:** only when two theories predict different finite outcomes
  for the same frozen apparatus and nuisance contract.
- **Reopen selection:** only when a physical principle selects the apparatus or
  interface from an admitted family target-blindly.

# Reproduction

Run:

```bash
python3 tests/du_heralded_bell_record_capability_probe.py --write-artifact
```

The machine-readable result is
`tests/artifacts/du_heralded_bell_record_capability_result.json`.  The probe is
an exact finite check of the truth table and derived bounds.  It is not an
experimental-data reanalysis.
