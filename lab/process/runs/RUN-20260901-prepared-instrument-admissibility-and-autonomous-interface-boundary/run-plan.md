---
title: "Prepared-instrument admissibility and autonomous-interface boundary — run plan"
status: complete
doc_type: governed_run_plan
created: 2026-09-01
run_id: RUN-20260901-prepared-instrument-admissibility-and-autonomous-interface-boundary
work_id: CCR-PREPARED-INSTRUMENT-ADMISSIBILITY-AND-AUTONOMOUS-INTERFACE-BOUNDARY
claim_id: HC-DU-217
owner_repo: dynamic-unity
---

# Exact question

Does `HC-DU-216`'s preparation-relative selection correction apply to quantum
instruments? In particular, can an independently prepared and calibrated
physical apparatus select an instrument for a conditional experiment without
earning the stronger claim that the source dynamics autonomously selected a
record interface?

# Frozen distinctions

The run keeps separate:

1. a mathematical POVM, channel, or instrument written into an analysis;
2. a physically prepared indirect measurement model fixed before the outcome;
3. the CP instrument induced by that packet;
4. a microscopic apparatus realization;
5. a durable material record handoff with provenance, archive, access,
   consumer, reset, resources, and finality; and
6. an autonomously selected natural interface.

# Tests

1. **Primary-source reconstruction.** Recover the Davies--Lewis instrument and
   Ozawa indirect measurement packet without relying on a secondary summary.
2. **Source-only kill.** Reuse `HC-DU-208` to test whether a Hamiltonian and
   spectral PVM determine the instrument.
3. **Prepared-packet factorization.** State the exact map from probe,
   preparation, coupling, and meter to a CP instrument.
4. **Realization boundary.** Determine whether an instrument uniquely selects
   apparatus microphysics or only a statistical equivalence class.
5. **Record firewall.** Test whether instrument selection implies retained
   archive, provenance, observer access, consumer, resources, reset, or
   finality.
6. **Claim-relative admission.** Separate conditional laboratory prediction
   from autonomous interface-emergence claims.
7. **Anti-copy gate.** Require precommitment, held-out transfer, and no refit.

# Absorbers and maximum grade

The strongest absorbers are Davies--Lewis instruments, Ozawa indirect
measurement models and realization, Naimark--Stinespring dilation, quantum
control, calibration/system identification, and DU's existing fibre theorem.

Maximum grade is scoped Grade 4 for an exact selection/nonselection boundary
and live-gate correction. No new instrument theorem, quantum prediction,
material record, or autonomous interface law can be earned.

# Cheapest kill and stop rules

Cheapest kill: identical source Hamiltonian and PVM permit distinct instruments
with the same Born law and different conditional continuations.

Stop if:

- a prepared apparatus is credited to the isolated source law;
- a purely mathematical interface is called physically selected;
- a CP instrument is called a unique apparatus microrealization;
- an instrument is called a retained provenance-bearing record;
- conditional experimental selection is rejected because it is not autonomous;
- autonomous classicality is claimed from an externally prepared apparatus;
- target data are used to refit the apparatus packet; or
- any repository other than Dynamic Unity is written.

# Decision states

```text
PREPARED_INSTRUMENT_VALID_PHYSICAL_ANTECEDENT
SOURCE_ONLY_INSTRUMENT_SELECTION_UNEARNED
INDIRECT_PACKET_SELECTS_CP_INSTRUMENT
MICROREALIZATION_NOT_UNIQUE
INSTRUMENT_NOT_COMPLETE_RECORD_HANDOFF
CONDITIONAL_AND_AUTONOMOUS_SELECTION_DISTINCT
NO_READY_SUCCESSOR
```

# Local-learning boundary

No local simulation or hardware run is admitted. Existing exact theory and the
banked finite counterexample determine the boundary.
