---
run_id: RUN-20260729-213813-hybrid-measurement-capacity-positive-control
status: complete
started_at: 2026-07-29T21:38:13-05:00
completed_at: 2026-07-29T21:45:08-05:00
repository: dynamic-unity
authority: "Joe direct chat: Go"
run_type: progress
mode: execute
work_id: CCR-PHYSICAL-RELIABILITY-RECONSTRUCTION-FLOOR
action_id: PRRF-04-HYBRID-MEASUREMENT-CAPACITY-POSITIVE-CONTROL
claim_id: HC-DU-141
evidence_grade: 4
maximum_grade: "Scoped Grade 4 exact channel/capacity and thermodynamic-nonimplication boundary; at most conditional Grade 3 source-label reconstruction inside the frozen packet. No selected apparatus, actual record, thermodynamic law, empirical excess, or new physics."
frozen_read_revisions:
  dynamic_unity_parent: 13baef582279
lane_selection:
  owner: dynamic-unity
  primary_lane_id: "4"
  supporting_lane_ids:
    - "3"
    - "7"
  branch: agent/research-compute-cleanup-2026-07-22
write_boundary:
  - explorations/hybrid-quantum-measurement-finite-time-capacity-and-thermodynamic-nonimplication-2026-07-29.md
  - lab/process/runs/RUN-20260729-213813-hybrid-measurement-capacity-positive-control/run-plan.md
  - explorations/concept-register.md
  - COUNTER-ASSUMPTIVE-FINDINGS-REGISTER.md
  - tests/README.md
  - tests/du_agent_orientation_contract_probe.py
  - tests/artifacts/du_agent_orientation_contract_result.json
  - CURRENT-RESEARCH.yaml
external_action_authorization: "Repository-local primary-source audit, exact symbolic derivation, authority integration, explicit-path commit, and non-force push only. No hardware, provider, contact, mailbox mutation, publication, submission, or other external action."
---

# PRRF-04 — hybrid-measurement capacity positive control

## Cold-start contract

Dynamic Unity's Purpose is to make physical reality intelligible as one
coherent, evidence-accountable whole. Its North Star asks whether
independently selected, observer-indexed certified causal records reconstruct
all observer-accessible time, geometry, fields, and capability, or leave a
finite physical remainder.

The repository is quiescent at revision 92. `HC-DU-140` separates
probability-port flow, thermodynamic completion odds, and observer-accessible
capacity, but names the finite-time hybrid measurement equation as a candidate
positive control. This run freezes the smallest binary packet and asks exactly
what it selects.

The source, hybrid state, and pointer distribution are ontic physical model
objects. The source prior, channel capacity, and forecast are epistemic tools
applied to them. A pointer distribution is not cast as an actual ex-post
record, and neither reliability nor record-relative determinacy is cast as
source issuance.

## Exact question

For the exactly solvable hybrid measurement law

\[
p(z,t)=e^{-\gamma t}p(z,0)
 +(1-e^{-\gamma t})\operatorname{tr}(P_z\hat\rho(0)),
\]

does one frozen binary source--measurement--pointer packet:

1. derive an exact finite-time classical channel and accessible capacity;
2. derive completion odds from that same channel without refit; and
3. make Norton's thermodynamic entropy-of-odds law follow from the hybrid
   dynamics?

## Frozen packet

- source alphabet \(X=\{0,1\}\), uniform;
- encoding \(\rho_x=P_x\) into the two measurement eigenstates;
- measurement \(M=\sum_xm_xP_x\);
- classical pointer alphabet \(Z=\{0,1\}\);
- uniform initial pointer law \(p(z,0)=1/2\);
- exact hybrid implementation with declared \(\gamma>0\);
- one declared read time \(t\ge0\);
- pointer readout \(Y=Z_t\);
- success means \(Y=X\);
- no bath, temperature, detailed balance, work reservoir, entropy-production
  functional, retention, provenance, certification, or ex-post outcome
  mechanism beyond the declared read.

## Preregistered returns

### Exact finite-time channel

The frozen packet is a binary symmetric channel with a closed-form crossover
probability and Shannon capacity.

### Model-specific odds--capacity relation

Because success is defined inside the same frozen channel, its success odds
and capacity are both functions of \(\gamma t\), producing an exact
packet-relative relation rather than a universal probability currency.

### Thermodynamic implication

The hybrid law itself supplies the dynamically realized thermal
completion/reversion process required by Norton, so
\(\Delta S=k_{\rm B}\log O\) follows without additional structure.

### Thermodynamic nonimplication

Correct-pointer odds are an outcome-channel statistic. Without a bath,
temperature, detailed balance, thermal occupation dynamics, or reversion
process, Norton does not apply. Imposing his realization afterward is a
conditional composition, not a derivation.

### Record-formation boundary

The paper's ex-ante pointer distribution does not by itself select one actual
ex-post write, retention, provenance, access, or certification chain.

## Exact controls

1. At \(t=0\), a uniform blank pointer must give capacity zero and odds one.
2. As \(t\to\infty\), the channel must approach perfect binary transmission.
3. The conditional entropy calculation must reproduce the binary symmetric
   channel capacity without simulation.
4. Changing the physical thermal realization while preserving the same
   classical channel must leave capacity fixed while allowing thermodynamic
   accounting to change.
5. A conditional Norton specialization must be labeled as added typing rather
   than as a consequence of the hybrid equation.

## Strongest absorber, cheapest kill, and stop

- **Strongest absorber:** binary symmetric channel capacity, Fano equality,
  finite-duration open-system measurement, and stochastic thermodynamics.
- **Cheapest kill:** the exact hybrid equation contains no temperature, heat,
  work, local detailed balance, or thermal reversion process from which
  Norton's entropy law could be derived.
- **Positive control:** an exact finite-time channel and capacity selected
  after the binary apparatus packet is frozen.
- **Stop:** bank the model-specific relation and the thermodynamic/record
  boundary. Do not simulate, generalize alphabets, infer a universal cost law,
  or activate hardware.

## Local-model learning gate

The exact solution and elementary channel algebra decide every preregistered
branch. Numerical simulation would reproduce a closed form and add no
decision-changing evidence.

Disposition: `DESK_RESEARCH_FIRST`.

External hardware is irrelevant.

## Validation

```bash
python3 tests/du_agent_orientation_contract_probe.py --write-artifact
git diff --check
```

## Durable output

One dated exploration, this governed receipt, and the minimum authority,
concept, counter-assumptive, and regression updates needed to preserve the
result. No paper seed, hardware note, prediction, or external action.

## In-turn sharpening

Joe corrected the motivating statement from “probability, not energy” to the
conditional Boltzmann relation

\[
\Delta S=k_{\rm B}\log O.
\]

He also distinguished sharing a probability variable from sharing port
structure. The run therefore added two controls without changing the frozen
packet:

1. distinguish finite readout-success odds from thermodynamic
   completion/reversion odds; and
2. check whether probability current paired with a log-ratio force is an
   established structure or a new conjecture.

The first control produced the decisive one-way-generator result. The second
is absorbed by standard stochastic-thermodynamic current--affinity theory,
while the quantum-to-thermodynamic adapter remains open.

## Result

```text
EXACT_HYBRID_BINARY_SYMMETRIC_CHANNEL
+ q(t)=exp(-gamma*t)/2
+ C(t)=1-h_2(q(t))
+ PACKET_RELATIVE_O_read=2*exp(gamma*t)-1
+ CONDITIONAL_BINARY_SOURCE_RECONSTRUCTION
+ READOUT_FAILURE_IS_INCOMPLETE_RELAXATION_NOT_REVERSION
+ ONE_WAY_RATE_ODDS_ARE_INFINITE
+ REVERSIBLE_REPAIR_SEPARATES_BIAS_ALPHA/BETA_FROM_DEPTH_(ALPHA+BETA)t
+ NORTON_LOG_ODDS_REQUIRES_THERMODYNAMIC_REALIZATION
+ STOCHASTIC_CURRENT--LOG_AFFINITY_PORT_HOST_IS_KNOWN
+ NO_SELECTED_QUANTUM_TO_THERMODYNAMIC_ADAPTER
+ EX_ANTE_DISTRIBUTION_IS_NOT_ACTUAL_RETAINED_RECORD
+ NO_READY_SUCCESSOR
```

The exact finite-time channel and model-specific odds--capacity branches
passed. The thermodynamic-implication branch failed. The thermodynamic-
nonimplication and record-formation boundary branches passed.

The reversible two-rate positive control gives

\[
q(t)
=
\frac1{1+O_{\rm th}}
+
\left(\frac12-\frac1{1+O_{\rm th}}\right)e^{-(\alpha+\beta)t},
\qquad
O_{\rm th}=\frac{\alpha}{\beta}.
\]

Therefore finite-time capacity depends separately on thermodynamic bias and
kinetic depth. Only after an independently supplied detailed-balance map may
one substitute \(O_{\rm th}=e^{\Delta S/k_{\rm B}}\).

No local model, hardware, provider, publication, prediction, or external
action was activated.

## Validation disposition

The exact solution and algebra decide the scientific result. The governance
probe is only a repository regression.

Validation completed:

- `37/37` governance and cold-start checks passed;
- all `298/298` counter-assumptive IDs are unique;
- `43` current evidence and action references resolve;
- required cold-start surfaces remain at `5,939/6,000` words;
- `git diff --check` passed; and
- the portfolio remains quiescent with no scientific executable.
