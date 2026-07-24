# tests/

Computational checks and machine probes, each mapping to a claim, with
real-falsifier positive controls. A test that a genuine falsifier can pass is
not a test; controls are mandatory.

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
