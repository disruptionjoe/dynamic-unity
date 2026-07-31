---
run_id: RUN-20260731-103723-gravitational-radiation-gaussian-tomography
claim_id: HC-DU-199
status: complete
created: 2026-07-31
grade: 4
disposition: CALIBRATED_GAUSSIAN_RADIATIVE_STATE_RECONSTRUCTION_COUPLING_INVARIANT_RATIO_NOT_ACQUISITION_INVARIANT_SCOPED_CLASSICAL_DRIVE_EXCLUSION_NOT_FIELD_ONTOLOGY
---

# Result

The 2026 gravitational-wave tomography proposal materially instantiates the
receiver side of `HC-DU-198`'s radiative reopener. In its frozen one-mode
vacuum-receiver beamsplitter model, known nonzero transfer makes detector first
and second moments injective for the incident Gaussian state.

That is conditional reconstruction, not interface selection. At one vacuum-
receiver setting, two distinct physical Gaussian inputs at transfers $1/4$
and $1/2$ produce the identical detector covariance when transfer is not
calibrated. A two-reference receiver response can reconstruct transfer from
its slope, but only if the source is fixed across arms. Three quadrature phases
span the covariance, while the two cardinal phases leave its cross term
unidentified.

The normalized $g^{(2)}$ ratio can cancel transfer exactly without cancelling
finite evidence cost. In the exact two-quantum control, $g^{(2)}=1/2$ for all
nonzero transfer, while the double-event probability is $\eta^2$. Reducing
$\eta$ tenfold increases the expected trial count for the same number of
double events one hundredfold.

A sub-vacuum detector quadrature excludes vacuum plus an exogenous classical
random displacement. A response-equivalent quantum ancilla or direct quantum
law survives, so gravitational field ontology is not selected.

## Exact receipt

`tests/du_gravitational_radiation_gaussian_tomography_probe.py` passes thirteen
checks covering:

- physical covariance witnesses;
- known-transfer inversion, single-setting collision, and fixed-source
  reference-slope calibration;
- phase-design rank;
- exact coupling-independent normalized coherence;
- coupling-dependent finite event formation;
- scoped classical random-drive exclusion; and
- survival of a response-equivalent quantum realization.

## Scientific disposition

```text
CONDITIONAL_GAUSSIAN_RECONSTRUCTION = EARNED
PHYSICAL_INTERFACE_SELECTION        = NOT_EARNED
TRANSFER_AND_PHASE_CALIBRATION       = LOAD_BEARING
REFERENCE_SLOPE_CALIBRATION          = CONDITIONAL_ON_FIXED_SOURCE
COUPLING_INVARIANT_FINITE_EVIDENCE   = FALSE
SCOPED_CLASSICAL_DRIVE_EXCLUSION     = EARNED
GRAVITATIONAL_FIELD_ONTOLOGY         = NOT_IDENTIFIED
LIVE_STATE_TRANSITION                = NONE
```

No observation, experimental-feasibility result, universal classical-gravity
exclusion, Grade-5 remainder, hardware action, new gravity law, paper action,
or active successor was earned. The scientific portfolio remains quiescent.

The artifact is
`tests/artifacts/du_gravitational_radiation_gaussian_tomography_result.json`.
