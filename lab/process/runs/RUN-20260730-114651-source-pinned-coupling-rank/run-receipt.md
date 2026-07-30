---
title: "Source-pinned coupling response rank — run receipt"
status: completed
doc_type: governed_run_receipt
created: 2026-07-30
completed_at: "2026-07-30 11:53:52 CDT"
run_id: RUN-20260730-114651-source-pinned-coupling-rank
work_id: MPA-03-SOURCE-PINNED-COUPLING-RESPONSE-RANK
action_id: MPA-03-SOURCE-PINNED-COUPLING-RESPONSE-RANK
program_id: CCR-MINIMAL-PHYSICAL-ANTECEDENT-TO-FINITE-REMAINDER
authority: "Joe direct chat: Go"
owner_repo: dynamic-unity
claim_id: HC-DU-161
---

# Source-pinned coupling response rank

## Disposition

```text
MATERIAL_RESPONSE_RANK
+ SINGLE_OUTPUT_NONIDENTIFIABILITY
+ LAW_ONLY_EXPLANATION
+ KNOWN_RESULT_ABSORPTION
+ STRONG_COUPLING_NO_REFIT_FAILURE
+ SWING 4 NOT ACTIVATED
```

Swing 3 is complete at scoped Grade 4. It source-pins the abstract
coupling/readout frontier to Peronnin et al.'s sequential superconducting-
qubit readout platform and identifies the exact response packet required to
separate coupling from the declared two-mode loss nuisances.

## Exact results

1. At the center of a symmetric pump pulse, with prepared readout amplitude,
   empty buffer, calibrated phase/time/gain, and frozen two-mode dynamics,
   define

   \[
   y_1=-\kappa_r,\qquad
   y_2=g,\qquad
   y_3=\frac g2(\kappa_r+\kappa_b).
   \]

2. The Jacobian of \((y_1,y_2,y_3)\) with respect to
   \((g,\kappa_r,\kappa_b)\) has determinant

   \[
   \det J=\frac g2.
   \]

   The coupling direction therefore leaves the declared loss-nuisance span
   whenever \(g\ne0\).

3. One terminal endpoint does not identify the coupling. In the weak-coupling
   population law

   \[
   \Gamma=\kappa_r+\frac{4g^2}{\kappa_b}+\kappa_p,
   \]

   the pairs \((g,\kappa_p)=(1,9/10)\) and \((2,3/5)\), at
   \(\kappa_b=40,\kappa_r=1/10\), both give \(\Gamma=11/10\) and therefore the
   same endpoint for every time.

4. Both twins lie inside the source's conservative low-pump ratio. More
   endpoint precision cannot repair the missing response direction.

5. The source's main reported operating ratio \(48/35\) is inside its wider
   two-mode release range but outside the strict reflection-calibration
   range. The strongest-pump discrepancies require effective \(g\) or
   \(\kappa_b\) refits or possible parasitic modes, so they do not inherit the
   scoped identification.

## Absorber and boundary

Passive linear quantum-system identification, quantum input-output theory,
classical observability, circuit-QED calibration, and the source paper itself
absorb the mathematical and physical components. This run claims no new law,
anomalous response, or new physics.

Dynamic Unity's advance is the typed boundary:

```text
one terminal response
  != identified physical coupling

calibrated multi-response mechanism identification
  != one joined formed record

faster strong-pump emptying after refit
  != no-refit transfer of the selected interface
```

The source's residual-population and output traces are obtained through
matched calibration arms. This run does not establish that they form one
blank-to-written, one-run, retained, provenance-bearing, accessible,
resettable record packet.

## Repository transition

- `HC-DU-161` is banked in the durable exploration.
- `CONCEPT-DU-019` records the source-pinned coupling-response correction.
- `NI-DU-204` preserves the endpoint-identification and strong-pump-refit
  traps.
- The quantum-foundations orientation surface carries the scoped correction.
- `CURRENT-RESEARCH.yaml` advances from revision 114 to 115.
- Swing 4 is scientifically eligible on the same platform but remains
  inactive and non-executable without separate authorization.
- No hardware, external provider, numerical simulation, prediction, or paper
  action was used or activated.

## Durable files

- `explorations/source-pinned-sequential-readout-coupling-response-rank-and-strong-pump-boundary-2026-07-30.md`
- `explorations/concept-register.md`
- `docs/quantum-foundations-orientation-surface.md`
- `COUNTER-ASSUMPTIVE-FINDINGS-REGISTER.md`
- `CURRENT-RESEARCH.yaml`
- `tests/du_source_pinned_coupling_response_rank_probe.py`
- `tests/artifacts/du_source_pinned_coupling_response_rank_result.json`
- `tests/README.md`
- this plan and receipt

## Validation

- `python3 tests/du_source_pinned_coupling_response_rank_probe.py
  --write-artifact` — **PASS**; determinant \(g/2\), exact endpoint twins,
  low-pump scope, and both source-regime boundary flags.
- `python3 tests/du_minimal_antecedent_campaign_probe.py --write-artifact` —
  **PASS**; all 17 seeds and 10 conditional swing cards remain preserved.
- `python3 tests/du_agent_orientation_contract_probe.py --write-artifact` —
  **PASS**; 37/37 governance checks, 317 unique counter-assumptive findings,
  69 resolving current references, 38 resolving stable-entrypoint links, no
  active/executable scientific action, and 5,883/6,000 cold-start words.
- Python compilation of all three probes — **PASS**.
- Direct PyYAML revision, quiescence, `HC-DU-161`, and Swing-4-preparation
  assertions — **PASS**.
- `git diff --check` — **PASS** before receipt finalization.

## Next boundary

If separately authorized, Swing 4 may stay on this platform and ask whether
its matched calibration arms constitute one joined formed record with
retention, provenance, observer access, reset semantics, and a held-out
action consequence. This receipt does not authorize that action or any later
reconstruction swing.
