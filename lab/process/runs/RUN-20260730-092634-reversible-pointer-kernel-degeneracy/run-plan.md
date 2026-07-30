---
title: "Reversible-pointer CSL quadratic-kernel attribution gate — run plan"
status: completed
doc_type: governed_run_plan
created: 2026-07-30
run_id: RUN-20260730-092634-reversible-pointer-kernel-degeneracy
work_id: ANOMALY-CSL-PATH-KERNEL-ATTRIBUTION
action_id: RPCSL-02-QUADRATIC-KERNEL-DEGENERACY-GATE
claim_id: HC-DU-158
authority: "Joe direct chat: Go"
owner_repo: dynamic-unity
---

# Reversible-pointer CSL quadratic-kernel attribution gate

## Cold-start contract

- **Purpose/North Star:** determine whether independently selected,
  observer-indexed certified causal records reconstruct observer-accessible
  physics or leave a finite physical remainder.
- **Perspective/ontology:** methodological physical realism. A measured
  visibility loss is an ontic response of the admitted apparatus, while its
  attribution to CSL, environmental scattering, or technical noise is a
  model-relative inference requiring a separately frozen response family.
- **Current authority:** `CURRENT-RESEARCH.yaml` revision 110 is quiescent
  after `HC-DU-157`; no scientific successor is selected.
- **Completed evidence consumed:** `HC-DU-157` proves that the reversible
  pointer can close in phase space while a CSL path functional remains
  nonzero, and that one visibility identifies only total loss. It leaves the
  actual CSL response vector and ordinary-loss nuisance span abstract.
- **Remaining obligation:** instantiate that span from the source's own
  equations and determine whether the proposed force, frequency, or path scan
  can attribute the loss without refitting.
- **Lanes/channels:** Lane 1 primary; Lanes 3, 4, and 7 supporting;
  `CH-FORMAL`, `CH-COLLIDE`, and `CH-SYN`.
- **Maximum grade:** scoped Grade 4 attribution obstruction and conditional
  assay-design theorem. No experimental result, CSL evidence, selected
  apparatus, or new dynamics can be earned here.
- **Strongest absorber:** standard filter-function decoherence, CSL
  phenomenology, environmental resolution expansions, nuisance-parameter
  identifiability, and optimal experimental design.
- **Cheapest kill:** show that the CSL column is not proportional to any
  physically admitted ordinary-loss column over the source's frozen scan, or
  that an already included calibration measures the nuisance coefficient
  independently at the required grade.
- **Dependencies:** the Renkel preprint is an external conditional specimen,
  not evidence; `HC-DU-157` is internal completed evidence; no sibling result
  or external hardware blocks this run.

## Exact question

In the pointlike or finite-width small-separation regime, do the proposed CSL
loss and any admitted ordinary loss share the same path statistic

\[
I_D=\int_0^\tau D^2(t)\,dt,
\]

so that varying only the controlled force, path amplitude, or trap frequency
cannot identify CSL? If so, what is the smallest intervention coordinate or
response nonlinearity that restores rank?

## Pre-registered targets

### Target A — quadratic-path attribution obstruction

Using the source's own frozen equations, form the loss design matrix for:

- pointlike small-separation CSL;
- finite-width small-separation CSL;
- residual-gas and blackbody small-separation decoherence; and
- intra-shot white electric-field phase noise.

If, on a fixed pointer and fixed-width-shape force-amplitude scan, every
column is a scalar multiple of \(I_D\), then arbitrary exact path-only data
have rank one and cannot identify CSL provenance.

### Target B — exact coupling-coordinate repair

For matched nonzero paths \(D_i(t)\), compare the CSL and white-electric
columns

\[
K_{{\rm CSL},i}\propto m_i^2I_{D,i},
\qquad
K_{E,i}\propto q_i^2I_{D,i}.
\]

The two-column design should have rank two exactly when the admitted
configurations do not keep \(m_i^2/q_i^2\) constant. This is only a
conditional repair: all remaining quadratic environmental coefficients must
also be independently bounded or given their own noncollinear controls.

### Target C — nonquadratic-separation boundary

Compare the exact pointlike CSL response

\[
1-\exp[-D^2/(4r_c^2)]
\]

with a quadratic nuisance response. Bound the first nonquadratic departure
over the source's baseline and aggressive operating points. If it is
negligible in the advertised \(D_{\max}\ll r_c\) regime, do not call a
larger-separation scan an already available repair.

## Retreat costs and stop rules

- **If Target A fails:** retain the earlier abstract rank gate and record the
  nonproportional source term; do not claim a kernel no-go.
- **If Target B fails:** do not recommend a mass/charge coupling-coordinate
  control.
- **If Target C is already large:** treat the nonlinear response as a live
  local discriminator rather than a remote redesign.
- **If the source-off or calibration arm independently identifies every
  path-correlated nuisance:** the obstruction is conditional on removing
  those measurements and must not be generalized.
- **Stop:** after the smallest exact design-rank result and response bound.
  Do not optimize an apparatus, estimate shots, survey collapse models, or
  request hardware.

## Local-model learning gate

Direct algebra can decide proportionality and rank. A numerical model is
admissible only if the finite-width integral creates a decision-changing
response direction that cannot be bounded analytically. Otherwise, no model
is built. Hardware is unavailable and unnecessary.

## Allowed returns

```text
EXACT_QUADRATIC_PATH_DEGENERACY
FORCE_AMPLITUDE_SCAN_NONIDENTIFYING
COUPLING_COORDINATE_RANK_REPAIR
NONQUADRATIC_CSL_SHAPE_LIVE
NONQUADRATIC_CSL_SHAPE_TOO_SMALL_IN_SOURCE_REGIME
INDEPENDENT_NUISANCE_CALIBRATION_REQUIRED
SOURCE_ALREADY_CLOSES_ATTRIBUTION
NO_READY_SUCCESSOR
```

No return may turn a projected ordinary-loss budget into an observed
calibration, a conditional design into a selected apparatus, or an
attribution theorem into evidence for CSL.

## Closure

The run returned:

```text
EXACT_QUADRATIC_PATH_DEGENERACY
+ FORCE_AMPLITUDE_SCAN_NONIDENTIFYING
+ SOURCE_OFF_VISIBILITY_NONCALIBRATING_FOR_PATH_LOSS
+ BREATHING_CONTRAST_RANK_REPAIR
+ COUPLING_COORDINATE_RANK_REPAIR
+ NONQUADRATIC_CSL_SHAPE_TOO_SMALL_IN_SOURCE_REGIME
+ INDEPENDENT_NUISANCE_CALIBRATION_REQUIRED
+ NO_READY_SUCCESSOR
```

The cheapest kill did not overturn the pointlike obstruction. The
finite-width calculation did prevent an overbroad negative verdict: it
supplies a noncollinear breathing-response direction and therefore a
conditional matched-preparation assay. No local model or hardware was
needed.
