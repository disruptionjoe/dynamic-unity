---
title: "Equivariant stochastic interface selection and formed-record gate — run receipt"
status: completed
doc_type: governed_run_receipt
created: 2026-07-30
completed_at: "2026-07-30 08:37:20 CDT"
run_id: RUN-20260730-082843-stochastic-interface-selector-gate
work_id: ANOMALY-STOCHASTIC-INTERFACE-SELECTOR
action_id: SIS-01-EQUIVARIANT-STOCHASTIC-SELECTOR-GATE
claim_id: HC-DU-156
authority: "Joe direct chat: Go"
owner_repo: dynamic-unity
---

# Equivariant stochastic interface selection and formed-record gate

## Disposition

```text
DETERMINISTIC_SELECTOR_IS_INVARIANT_DIRAC_CASE
+ STOCHASTIC_ONLY_SELECTOR_EXISTS_ON_COMPACT_ORBITS
+ STOCHASTIC_SELECTION_NOT_AUTOMATIC_OR_UNIQUE
+ LORENTZ_H3_HAS_NO_NORMALIZED_INVARIANT_SELECTOR
+ SELECTED_KERNEL_NOT_REALIZED_INTERFACE_OR_FORMED_RECORD
+ SAME_UNLABELLED_CHANNEL_DIFFERENT_LABELLED_INSTRUMENTS
+ STANDARD_COVARIANT_INSTRUMENT_ABSORPTION
+ NO_READY_SUCCESSOR
```

The run completed at scoped Grade 4. It corrected the repository's selector
typing and proved exact compact-positive, nonunique, and noncompact-negative
cases. It did not produce a Grade-5 physical remainder, prediction, or
selected successor.

## Earned result

For one antecedent orbit \(Gx\), with stabilizer \(H=G_x\):

- deterministic equivariant selectors correspond to \(H\)-fixed points of
  the candidate-interface fibre;
- equivariant Markov kernels correspond to \(H\)-invariant probabilities on
  that fibre; and
- deterministic selection is the invariant-Dirac special case.

Finite and compact averaging can therefore select a lottery when no point is
selected. Two disjoint finite orbits show that symmetry need not select the
inter-orbit mixture weight. Integer translations and the Lorentz action on
the future-unit hyperboloid show that a noncompact orbit can lack every
normalized invariant probability.

The exact quantum control uses:

- a uniformly labelled \(X/Y/Z\)-dephasing instrument; and
- a labelled \(I/X/Y/Z\) Pauli-error instrument with weights
  \(1/2,1/6,1/6,1/6\).

Both induce the unlabelled Bloch map \(r\mapsto r/3\). For
\(\lvert+x\rangle\), their label-conditioned \(X+\) probabilities are
\((1,1/2,1/2)\) and \((1,1,0,0)\), while both coarse probabilities equal
\(2/3\). The unlabelled channel therefore does not identify its labelled
instrument or archive.

## Scientific meaning

The prior deterministic no-selector theorems remain correct but were not a
complete classification of physical selection. DU now has the exact ladder:

```text
candidate orbit
  -> invariant probability kernel
  -> physical sampler/instrument
  -> realized interface
  -> formed retained record
  -> accessible/certified record
```

The first arrow may close without the second. It may also fail on a
noncompact physical orbit. Standard invariant-measure, covariant-instrument,
dilation, and spontaneous-symmetry-breaking theory absorbs the component
mathematics.

## Portfolio transition

- `CURRENT-RESEARCH.yaml` advanced from revision 108 to 109.
- `HC-DU-156` was attached to the parked physical-record interface-selection
  program.
- its reopener now admits a source-selected stochastic instrument and archive;
- no parked reopener was satisfied;
- no scientific program or executable action was activated; and
- successor selection remains `no_ready`.

## Resource disposition

Exact finite group and channel algebra plus the continuous orbit proof fully
decide the scoped question. Larger simulation, cloud execution, and external
hardware would instantiate absorbed cases without selecting the missing
sampler or archive.

## Durable files

- `explorations/equivariant-stochastic-interface-selection-normalized-orbit-boundary-and-formed-record-gate-2026-07-30.md`
- `tests/du_stochastic_interface_selector_gate_probe.py`
- `tests/artifacts/du_stochastic_interface_selector_gate_result.json`
- `COUNTER-ASSUMPTIVE-FINDINGS-REGISTER.md`
- `explorations/concept-register.md`
- `docs/quantum-foundations-orientation-surface.md`
- `tests/README.md`
- `CURRENT-RESEARCH.yaml`
- this run plan and receipt

## Validation

- `python3 tests/du_stochastic_interface_selector_gate_probe.py --write-artifact`
  — **PASS**, 20/20 exact scientific checks.
- `python3 tests/du_agent_orientation_contract_probe.py --write-artifact` —
  **PASS**, 37/37 governance checks, 312 unique counter-assumptive findings,
  and 5,897/6,000 cold-start words.
- Python compilation of both changed probes — **PASS**.
- direct PyYAML/JSON revision, quiescence, successor, and exact-check
  assertions — **PASS**.
- repository-local Markdown links on changed surfaces — **PASS**.
- `git diff --check` — **PASS**.
