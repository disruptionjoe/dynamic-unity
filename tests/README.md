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
