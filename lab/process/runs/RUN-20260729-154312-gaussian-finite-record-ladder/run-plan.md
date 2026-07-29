---
run_id: RUN-20260729-154312-gaussian-finite-record-ladder
status: completed
started_at: 2026-07-29T15:43:15-05:00
repository: dynamic-unity
authority: "Joe direct chat: Go"
run_type: progress
mode: execute
work_id: CCR-GAUSSIAN-FINITE-RECORD-LADDER
claim_id: HC-DU-129
primary_lane: lane_1
supporting_lanes:
  - lane_3
  - lane_4
  - lane_6
  - lane_7
channels:
  - CH-FORMAL
  - CH-COLLIDE
  - CH-MODEL
  - CH-SYN
maximum_grade: "Scoped Grade 4 population-setting minimality, finite-shot nonidentification, Gaussian-class, and non-Gaussian first-leak boundary plus conditional Grade 3 finite-resolution reconstruction; no selected mode algebra, Gaussian sector, Hamiltonian, state, detector, observer, interface, empirical excess, new law, new physics, or prediction"
external_action_authorization: "Repository-local proof, bounded primary-source collision, minimal exact regression, evidence/authority integration, explicit-path commit, and non-force push only; no publication, submission, hardware, provider, contact, or other external action."
frozen_read_revisions:
  dynamic_unity_parent: 44bf1d807942ffdd05ba0aa308553272b709cc04
lane_selection:
  owner: dynamic-unity
  primary_lane_id: "1"
  supporting_lane_ids:
    - "3"
    - "4"
    - "6"
    - "7"
  manifest_revision: 97
  manifest_sha256: 7d8bf6650a229fdac42dd63397fbc15352e42457d9f70ea0e036f8003573d80a
  current_research_revision: 79
  current_research_sha256: 0a0adb8d1d90e89f3a733f7143d582e7770ef86fe54f1f6a91e841f36dc1b4f2
  branch: agent/research-compute-cleanup-2026-07-22
  selection_basis: "Joe authorized the next bounded successor. DU is explicitly quiescent. HC-DU-128 names quasifree/Gaussian closure as the cheapest serious candidate for turning an infinite functional hierarchy into finite sufficient data. HC-DU-102 already proves that causal Weyl response does not select the quasifree state, so this run tests state reconstruction and physical finite acquisition rather than repeating channel-state nonidentification."
write_boundary:
  - lab/process/runs/RUN-20260729-154312-gaussian-finite-record-ladder/run-plan.md
  - explorations/gaussian-population-reconstruction-finite-shot-certificate-and-nongaussian-first-leak-2026-07-29.md
  - tests/du_gaussian_finite_record_ladder_probe.py
  - tests/artifacts/du_gaussian_finite_record_ladder_result.json
  - CURRENT-RESEARCH.yaml
  - COUNTER-ASSUMPTIVE-FINDINGS-REGISTER.md
  - docs/quantum-foundations-orientation-surface.md
  - explorations/concept-register.md
  - tests/README.md
  - tests/du_agent_orientation_contract_probe.py
---

# Gaussian population reconstruction and finite-record ladder

## Cold-start contract

Dynamic Unity's Purpose is to make physical reality intelligible as one
coherent, evidence-accountable whole. Its North Star asks whether independently
selected, observer-indexed certified causal records reconstruct all
observer-accessible time, geometry, fields, and capability, or leave a finite
physical remainder.

The current authority is quiescent at revision 79. `HC-DU-128` established the
positive-functional reconstruction boundary:

```text
fixed star algebra + complete positive functional
  -> cyclic GNS/QFT representation reconstruction

but

infinite theoretical functional
  != finite physically formed observer record.
```

It named quasifree/Gaussian closure as the cheapest serious finite-statistic
reopener. `HC-DU-102` already showed that the causal Weyl response and
symplectic form do not select the quasifree covariance.

This run asks whether the Gaussian restriction closes the remaining record
gap, and at which rung.

## Typed arena

Let \(n\) be a finite number of bosonic modes, \(m=2n\), and let

\[
R=(Q_1,P_1,\ldots,Q_n,P_n)
\]

be a supplied calibrated canonical-quadrature vector with supplied symplectic
form \(\Omega\).

A Gaussian state is parameterized by:

\[
d_i=\langle R_i\rangle,
\qquad
V_{ij}
=
\tfrac12\langle
(R_i-d_i)(R_j-d_j)+(R_j-d_j)(R_i-d_i)
\rangle,
\]

with the physical uncertainty condition

\[
V+\tfrac{i}{2}\Omega\geq0.
\]

For one supplied homodyne direction \(u\in\mathbb R^m\), the population
quadrature distribution is Gaussian with mean \(u^\mathsf Td\) and variance
\(u^\mathsf TVu\).

Keep four objects distinct:

1. **State parameter:** the theoretical pair \((d,V)\).
2. **Population packet:** exact means and variances of declared quadrature
   distributions.
3. **Formed transcript:** finitely many detector outcomes, with setting,
   attempt, calibration, and digitization lineage.
4. **Certificate:** a confidence-qualified region for \((d,V)\) or a
   held-out target.

Statistical sufficiency of a transcript summary does not imply that the true
state parameter is exactly determined.

## Assumptions and warrants

### `STANDARD`

- finite canonical bosonic mode algebra;
- Gaussian characteristic functions are determined by first and second
  moments;
- homodyne quadrature populations have Gaussian mean and variance;
- finite-dimensional linear algebra and exact Gaussian likelihoods.

### `CONDITIONAL_POSIT`

- the mode decomposition, phase reference, units, and symplectic form;
- the Gaussian state class;
- the quadrature directions and detector calibration;
- independent repeated preparations;
- digitization/binning and complete attempt lineage;
- an upper covariance/effective-energy bound for finite-resolution
  concentration; and
- the target radius, accuracy, and error probability.

These are frozen inputs, not results of the run.

### Warrants

- `DERIVED`: setting minimality, likelihood support, and reconstruction/error
  bounds.
- `CONSTRUCTIVELY_REALIZED`: exact finite linear-algebra, sufficient-statistic,
  transcript-overlap, and non-Gaussian controls.

## Exact questions

1. What is the minimum number of single-quadrature population settings needed
   to reconstruct every Gaussian \(d,V\)?
2. Does a finite formed transcript exactly determine the underlying
   continuous state parameter?
3. At a declared resolution and confidence, what finite conditional
   reconstruction is available?
4. Does exact first/second-moment reconstruction survive removal of the
   Gaussian assumption?
5. Does quadratic dynamics select the Gaussian state, or merely preserve a
   supplied Gaussian sector?

## Pre-registered theorem spine

### Proposition 1 — population-setting minimum

There are

\[
k=\dim\operatorname{Sym}_m=\frac{m(m+1)}2=n(2n+1)
\]

independent covariance coordinates. Each one-dimensional quadrature
population supplies one variance functional
\(V\mapsto u^\mathsf TVu\), so fewer than \(k\) settings cannot identify every
covariance.

The directions

\[
\{e_i\}_{i=1}^m
\cup
\{e_i+e_j\}_{1\leq i<j\leq m}
\]

attain the bound:

\[
V_{ii}=v(e_i),
\qquad
V_{ij}
=
\frac{v(e_i+e_j)-v(e_i)-v(e_j)}2.
\]

The coordinate-direction means recover \(d\). Thus \(k\) population
quadrature distributions are necessary and sufficient in this single-output
contract.

### Proposition 2 — finite-shot exact nonidentification

Fix any finite set of settings and any finite digitized transcript whose bins
have nonzero width. Every nonsingular Gaussian state assigns strictly positive
probability to every finite sequence of those bins. Therefore one finite
formed transcript has a continuum of same-record/different-\((d,V)\)
completions. More shots shrink likelihood or confidence regions; no finite
shot count gives exact rival exclusion in the continuous unrestricted
parameter class.

For ideal real-valued outcomes, the per-setting count, sum, and sum of squares
are likelihood-sufficient statistics for the univariate Gaussian family.
They retain all sample likelihood information and still do not make the true
parameter a function of the record.

### Proposition 3 — conditional finite-resolution reconstruction

Assume \(\lambda_{\max}(V)\leq B\), take \(N\) independent repetitions per
direction, and let \(k=m(m+1)/2\). Coordinate sample means and sample variances
give a finite confidence-qualified record.

Gaussian mean and chi-square concentration, followed by a union bound, yield
a finite \(N\) for any declared mean error, covariance-entry error, and
failure probability. A sufficient variance scaling is

\[
N
=
O\!\left(
\frac{B^2}{\varepsilon_V^2}
\log\frac{k}{\alpha}
\right),
\]

with the product interpreted as the usual concentration scaling
\(O((B/\varepsilon_V)^2\log(k/\alpha))\). The exact constants and propagation
to bounded-radius Weyl expectations will be stated in the result.

This is probabilistic reconstruction at declared resolution, not exact state
selection.

### Proposition 4 — non-Gaussian first leak

For one mode, the Fock state \(|1\rangle\) and the centered thermal Gaussian
state with mean occupation \(\bar n=1\) have the same first moments and
covariance

\[
V=\tfrac32 I.
\]

They differ on a held-out fourth moment or number variance. Thus the complete
Gaussian population packet is complete only relative to the Gaussian
completion class.

### Proposition 5 — preservation is not selection

A supplied quadratic Hamiltonian preserves Gaussianity. A specified stable
quadratic Hamiltonian together with a specified ground-state or KMS contract
may select one Gaussian state, but then the state is fixed by the law packet
and the record is not doing the selecting. Without that state contract,
quadratic evolution does not turn an arbitrary initial state Gaussian and
does not choose one covariance.

## Primary-source collision

The run uses these sources only as absorbers and physical-scope controls:

- Zhang and Mølmer, *Prediction and retrodiction with continuously monitored
  Gaussian states* (2017): Gaussian oscillator states are characterized by
  quadrature means and covariance under Gaussian-preserving monitoring.
- Holevo, *The structure of general quantum Gaussian observable* (2020):
  homodyne/heterodyne observables are members of a larger typed Gaussian
  observable class rather than a uniquely selected readout.
- Tripier-Mondancin et al., *Optimal Moment-Based Characterization of a
  Gaussian State* (2025): moment-based homodyne/double-homodyne estimation
  reaches the Cramér--Rao bound in the stated squeezed-state task.
- Roh et al., *Experimental Quantum State Tomography of Multimode Gaussian
  States* (2026): single and joint homodyne schemes reconstruct covariance
  matrices from finite experimental samples, with physicality and
  finite-sample error remaining live.
- Wolf, Giedke, and Cirac, *Extremality of Gaussian Quantum States* (2006):
  fixing a covariance does not generally fix a state outside the Gaussian
  class.

No literature result is claimed as DU novelty.

## Strongest absorber, cheapest kill, and stop

- **Strongest absorber:** Gaussian quantum tomography plus
  Fisher--Neyman sufficiency and normal/chi-square concentration.
- **Cheapest positive:** exact rank proof that \(k=n(2n+1)\) population
  quadrature settings determine every Gaussian \(d,V\).
- **Cheapest kill:** one finite binned transcript has positive probability
  under two distinct physical Gaussian states.
- **Scope kill:** \(|1\rangle\) and the \(\bar n=1\) thermal Gaussian share
  first and second moments and differ on a fourth-order target.
- **Stop:** stop after separating population identifiability,
  sample-likelihood sufficiency, finite-resolution certification, and
  physical class selection. Do not build a tomography simulator or provider
  bridge.

## Local-model learning gate

Direct formal analysis supplies the result. The executable artifact is a
minimal exact regression of direction-span, reconstruction, likelihood
factorization, transcript overlap, and the non-Gaussian witness. It is not an
admitted simulation or learning model.

Disposition: `PROOF_FIRST_MINIMAL_REGRESSION_ONLY`.

External hardware is irrelevant to this swing. Existing experiments establish
physical realizability of homodyne covariance estimation; DU is not repeating
them.

## Durable return

One dated exploration, exact regression and artifact, appended completion
receipt, and only the live/register surfaces needed to bank the scoped result.
No paper seed, selected successor, ontology promotion, hardware note,
cross-repository claim, or external action.

## Completion receipt

```yaml
completed_at: 2026-07-29T15:54:06-05:00
result: GAUSSIAN_POPULATION_PACKET_HAS_A_FINITE_MINIMAL_SETTING_BASIS+FINITE_IID_SUMMARY_IS_LIKELIHOOD_SUFFICIENT_NOT_PARAMETER_DETERMINING+EVERY_FINITE_DIGITIZED_TRANSCRIPT_HAS_MULTIPLE_GAUSSIAN_COMPLETIONS+BOUNDED_COVARIANCE_GIVES_FINITE_CONFIDENCE_RECONSTRUCTION+FIRST_SECOND_MOMENTS_FAIL_OUTSIDE_THE_GAUSSIAN_CLASS+QUADRATIC_PRESERVATION_IS_NOT_STATE_SELECTION+NO_READY_SUCCESSOR
claim_grade:
  scoped_grade_4:
    - single-output population-setting minimum
    - incomplete-setting covariance witness
    - finite-binned-transcript nonidentification
    - Gaussian-class boundary
    - non-Gaussian first leak
    - preservation-versus-selection boundary
  conditional_grade_3:
    - finite-resolution confidence certificate
tests:
  gaussian_finite_record_ladder: "PASS 33/33"
  positive_functional_qft_reconstruction: "PASS 27/27"
  bounded_weyl_causal_propagator: "PASS 64 factorizations; 16 symplectic relabelings"
  agent_orientation_contract: "PASS 37/37; 5984/6000 cold-start words"
selected_successor: null
external_actions: none
```
