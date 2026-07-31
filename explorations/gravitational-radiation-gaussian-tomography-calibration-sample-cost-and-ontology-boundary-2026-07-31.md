---
title: "Gravitational-radiation Gaussian tomography: calibration, sample cost, and ontology boundary"
status: explored
doc_type: governed_research_swing
created: 2026-07-31
claim_id: HC-DU-199
claim_status_change: none
disposition: CALIBRATED_GAUSSIAN_RADIATIVE_STATE_RECONSTRUCTION_COUPLING_INVARIANT_RATIO_NOT_ACQUISITION_INVARIANT_SCOPED_CLASSICAL_DRIVE_EXCLUSION_NOT_FIELD_ONTOLOGY
---

# Gravitational-radiation Gaussian tomography boundary

## Result

The radiative reopener in `HC-DU-198` is no longer merely hypothetical.
Toccacelo, Beitel, Andersen, and Pikovski propose a 2026 receiver in which one
resonant gravitational-wave mode and one acoustic mode interact through an
effective beamsplitter Hamiltonian. They derive detector counting statistics,
exact transfer of normalized second-order coherence, and a phase-sensitive
route to Gaussian-state tomography.

That proposal supplies a substantially sharper **receiver-side operational
interface** than the six-platform audit previously recorded. It does not
select the complete interface. The source, one-mode reduction, rotating-wave
approximation, detector preparation, transfer coefficient, phase reference,
Gaussian model class, and gravitational provenance remain antecedents.

Within that frozen model, this swing earns four exact results:

1. **Calibrated conditional reconstruction.** A known nonzero transfer factor
   and detector first and second moments uniquely reconstruct the incident
   Gaussian state's first and second moments.
2. **Single-setting calibration nonidentifiability and a repair.** If the
   transfer factor is not fixed, two distinct physical Gaussian input states
   at two distinct couplings can produce exactly the same detector covariance
   for one vacuum-receiver setting. Two known receiver references can recover
   the transfer from their response slope, but only if the source is stable
   across those arms.
3. **Statistic/evidence separation.** The normalized $g^{(2)}$ statistic can
   be exactly independent of coupling even while the number of trials needed
   to form its finite record grows as the inverse fourth power of the
   amplitude coupling, or $\eta^{-2}$ in transfer probability.
4. **Scoped nonclassicality without ontology.** A transferred sub-vacuum
   quadrature excludes a detector driven only by an exogenous classical random
   displacement. A response-equivalent quantum ancilla or direct quantum law
   survives, so gravitational field ontology is not selected.

This is a scoped Grade-3 reconstruction result plus Grade-4 calibration,
finite-evidence, rival, and ontology boundaries. It is not an observation,
feasibility result, new gravity law, Grade-5 remainder, or active successor.
`CURRENT-RESEARCH.yaml` remains quiescent.

## Cold-start contract

- **Purpose / North Star:** identify a target-blind physical antecedent that
  selects a record interface sufficient for a held-out target, or isolate the
  first lawful remainder.
- **Question:** what does the 2026 graviton-counting tomography proposal
  actually reconstruct, what must be calibrated, and which rival classes does
  its record exclude?
- **Current state:** quiescent. Joe authorized this bounded swing, not a new
  program or hardware campaign.
- **Perspective / status:** the detector output is a physically proposed
  record; its interpretation as an incident gravitational state is conditional
  on a selected channel and mode; ontology is a separate target.
- **Lanes / channels:** Lane 1 with Lanes 2, 3, 4, 6, and 7 support;
  `CH-FORMAL`, `CH-MODEL`, `CH-COLLIDE`, and `CH-EMPIRICAL`.
- **Maximum grade:** scoped Grade 4. A Grade-5 result would require a frozen,
  acquired discriminator surviving the full classical, direct-quantum,
  detector, source, and calibration rival class.
- **Strongest absorbers:** Gaussian attenuation channels, homodyne tomography,
  loss-invariant normalized correlations, finite-sample statistics, classical
  stochastic-wave realizations, and input--output equivalence.
- **Cheapest kill:** exhibit two physical incident states with the same
  single-setting detector output when the transfer is uncalibrated, then test
  whether the proposal's controlled reference family repairs it without
  assuming source stability for free.
- **Hardware:** unavailable and unnecessary. The identifiability and evidence-
  formation boundaries are exact before any experiment is attempted.

## Local Model Learning Gate

| Field | Frozen answer |
|---|---|
| Question | Does the proposed receiver turn the radiative reopener into selected reconstruction, and does coupling cancellation make it locally viable? |
| Research-only baseline | A known Gaussian attenuation channel is invertible on Gaussian moments for nonzero transfer; controlled reference amplitudes can calibrate attenuation under a stable source; normalized correlations can cancel loss. |
| Local learning delta | Separate single-setting collision from reference-slope repair, channel inversion from channel selection, and population-level loss cancellation from finite-event cost. |
| Generated, not encoded | Exact physical covariance pairs, measurement-design ranks, two loss levels, event probabilities, and rival witnesses. |
| Pre-hardware checkpoint | One same-output/different-input calibration witness and one exact ratio-versus-trial-cost witness. |
| Decision changed | Recognize a real conditional receiver-side reconstruction theorem, but do not infer viability or field ontology from normalized coupling independence. |
| Minimal build | One-mode vacuum attenuation channel, three quadrature phases, a two-quantum loss control, and classical/quantum rival classes. |
| Stop / hardware boundary | Stop once calibration, acquisition, and ontology boundaries are exact; do not simulate astrophysical rates or request hardware. |

**Admission:** `ADMIT_LOCAL_LEARNING_BUILD`. The build exposes a finite-record
condition absent from the population-level ratio and changes the grading of the
radiative reopener before external hardware.

## 1. What the 2026 proposal adds

The primary proposal assumes one on-shell gravitational-wave mode $a$ near
resonance with one bulk acoustic mode $b$. Under its rotating-wave
approximation, the interaction is

\[
H_{\mathrm{int}}
=
\hbar\gamma_g
\left(b^\dagger a+b a^\dagger\right),
\tag{1}
\]

up to the stated time phases. The resulting Heisenberg evolution is a
beamsplitter transformation. With the detector initially in vacuum and after
absorbing a known local phase, the paper obtains

\[
V_b^{\mathrm{out}}
=
\cos^2(\gamma_g t)\frac{I}{2}
+
\sin^2(\gamma_g t)V_g,
\qquad
m_b^{\mathrm{out}}
=
\sin(\gamma_g t)m_g.
\tag{2}
\]

Set

\[
\eta=\sin^2(\gamma_g t).
\]

Then (2) is the familiar one-mode pure-loss Gaussian channel

\[
V_{\mathrm{out}}
=(1-\eta)\frac I2+\eta V_{\mathrm{in}},
\qquad
m_{\mathrm{out}}=\sqrt{\eta}\,m_{\mathrm{in}}.
\tag{3}
\]

The paper also shows

\[
g_b^{(2)}(0)=g_g^{(2)}(0)
\tag{4}
\]

for nonzero coupling, and supplies a phase-sensitive correlation protocol in
which different prepared phases of the acoustic reference expose the Gaussian
quadrature moments.

This is a genuine improvement over a detector click. A click is one outcome;
the proposed joined family of prepared phases and intensity correlations can,
within the assumed Gaussian channel, identify the incident state moments.

It remains a proposal and a conditional model. The authors themselves state
that finite timing, detector noise, local-oscillator amplitude noise, phase
control, thermal occupation, and long measurement times limit the achievable
tomography.

Primary source:

- Toccacelo, Beitel, Andersen, and Pikovski, [“Quantum State
  Characterization of Gravitational Waves via Graviton Counting
  Statistics”](https://arxiv.org/abs/2602.09125) (2026).

## 2. The lawful radiative intervention algebra

`HC-DU-198` rejected arbitrary replacement of a constraint-bound near field.
The present proposal operates on a different object: a selected free
radiative mode and a controlled receiver.

The physically proposed operations are receiver-side:

\[
\mathfrak A_{\mathrm{recv}}
=
\{\text{prepare }\beta e^{i\phi},
\text{ wait through the declared window},
\text{ count},
\text{ correlate}\}.
\tag{5}
\]

They are lawful in the model because they vary the acoustic detector rather
than overwrite a constrained gravitational coordinate. Three distinct things
must nevertheless remain typed apart:

1. the asymptotic or on-shell **radiative algebra** admitted by linearized
   gravity;
2. the selected **single resonant mode** used by (1); and
3. the controlled **receiver action algebra** in (5).

Radiative phase spaces and gauge-invariant radiative observables exist in the
linearized theory, but that fact does not select the particular mode,
detector, phase reference, or Gaussian quotient used here. Relevant anchors
include Ashtekar's null-infinity radiative phase space and Benini et al.'s
construction of radiative observables and states:

- Ashtekar, [“Geometry and Physics of Null
  Infinity”](https://arxiv.org/abs/1409.1800) (2014).
- Benini, Dappiaggi, and Murro, [“Radiative observables for linearized
  gravity”](https://arxiv.org/abs/1404.4551) (2014).

## 3. Conditional Gaussian reconstruction theorem

### Theorem 1 — calibrated one-mode Gaussian reconstruction

For the frozen channel (3), if the vacuum receiver model and
$\eta>0$ are independently known, then the incident Gaussian state is
uniquely reconstructed from the detector first and second moments:

\[
m_{\mathrm{in}}=\frac{m_{\mathrm{out}}}{\sqrt\eta},
\qquad
V_{\mathrm{in}}
=
\frac{V_{\mathrm{out}}-(1-\eta)I/2}{\eta}.
\tag{6}
\]

The proof is direct inversion. Its scientific grade is conditional
reconstruction, not channel selection. Equation (6) says what follows if the
input port, vacuum receiver, transfer factor, and Gaussian class have already
been physically fixed.

### Minimal phase design

A real symmetric covariance has three independent entries

\[
(V_{xx},V_{xp},V_{pp}).
\]

Quadrature variances at phases $0,\pi/2,\pi/4$ give the exact design rows

\[
\begin{pmatrix}
1&0&0\\
0&0&1\\
1/2&1&1/2
\end{pmatrix},
\tag{7}
\]

which have rank three. The two cardinal phases alone have rank two and leave
the cross covariance unidentified. This finite calculation makes phase
control a reconstruction condition rather than a practical footnote.

## 4. Calibration is load-bearing

If $\eta$ is not independently fixed, the same detector covariance may come
from distinct physical inputs. Consider

\[
\eta_A=\frac14,
\qquad
V_A=
\begin{pmatrix}
1/4&0\\
0&1
\end{pmatrix},
\tag{8}
\]

and

\[
\eta_B=\frac12,
\qquad
V_B=
\begin{pmatrix}
3/8&0\\
0&3/4
\end{pmatrix}.
\tag{9}
\]

Both are physical one-mode covariance matrices: their determinants are
$1/4$ and $9/32$, respectively. Substitution into (3) gives the identical
output

\[
V_{\mathrm{out}}
=
\begin{pmatrix}
7/16&0\\
0&5/8
\end{pmatrix}.
\tag{10}
\]

### Theorem 2 — single-setting transfer obstruction

One vacuum-receiver output does not reconstruct the incident Gaussian state
on a completion class in which the transfer factor varies. The target becomes
constant only after $\eta$, the receiver vacuum model, or an equivalent
calibration record is added.

That addition is not free. A calibration may be a physically formed record,
an external assumption, or a fitted nuisance parameter. The grade depends on
which it is.

### Positive control — receiver-reference slope

The proposal's varied coherent receiver is capable, in principle, of forming
the missing calibration record. For two known receiver preparations whose
amplitude difference is $\Delta\beta$, hold the incident source state fixed.
The gravitational contribution to the output-mean difference cancels, leaving

\[
\Delta m_{\mathrm{out}}
=
\sqrt{1-\eta}\,\Delta\beta.
\tag{11}
\]

Hence

\[
\eta
=
1-
\left(
\frac{\Delta m_{\mathrm{out}}}{\Delta\beta}
\right)^2.
\tag{12}
\]

For the exact control $\Delta\beta=2$ and
$\Delta m_{\mathrm{out}}=1$, the reconstructed transfer is $\eta=3/4$.
This is an internal calibration route, not a refutation of the obstruction:
it enlarges the record from one output state to a joined intervention family
and assumes the same incident state across its arms. For an astrophysical wave,
source stationarity over the detection window and repeatability across
reference settings are therefore part of the physical contract.

## 5. Coupling-independent statistic is not coupling-independent evidence

Equation (4) is exact at the population level because loss multiplies both
factorial moments by matching powers of $\eta$. It does not imply a fixed
finite acquisition cost.

Use an incident two-quantum Fock state as the smallest exact control. After
loss,

\[
p_2=\eta^2,
\qquad
p_1=2\eta(1-\eta),
\qquad
p_0=(1-\eta)^2.
\tag{13}
\]

The mean and second factorial moment are

\[
\langle n\rangle=2\eta,
\qquad
\langle n(n-1)\rangle=2\eta^2,
\]

so

\[
g^{(2)}=\frac{2\eta^2}{(2\eta)^2}=\frac12
\tag{14}
\]

for every $\eta>0$. Yet the probability of the double event used in the
numerator is $\eta^2$. To expect $K$ such events requires

\[
N=\frac K{\eta^2}.
\tag{15}
\]

For $K=100$, changing $\eta$ from $1/10$ to $1/100$ changes the expected
trial count from $10^4$ to $10^6$. The ratio is unchanged; the evidence-
formation burden grows one hundredfold.

### Corollary — invariant target / noninvariant capability

Loss invariance of a normalized statistic is a statement about the target
functional on ideal distributions. It is not a statement that a finite
observer has coupling-independent access to that target. A physical record
requires enough events, retention, phase reference, calibration, and noise
control to estimate the ratio.

This is the principal DU-owned addition to the quantum-optical result.

## 6. What a sub-vacuum output excludes

For a vacuum detector subject only to a classical random displacement $z$,
the output covariance has the form

\[
V_{\mathrm{cl}}=\frac I2+\operatorname{Cov}(z).
\tag{16}
\]

Because $\operatorname{Cov}(z)\succeq0$, no quadrature variance can fall below
$1/2$. The exact output (10) has minimum variance $7/16$. It therefore
excludes this declared classical random-drive channel.

Carney gives the same scoped distinction in the gravitational setting:
ordinary clicks, Poisson statistics, and enhanced noise can have classical
wave explanations, while transferred sub-vacuum noise cannot be produced by a
purely classical c-number signal in the beamsplitter model. He also estimates
that the effect is extraordinarily difficult to observe with realistic
gravitational detectors:

- Carney, [“Comments on graviton
  detection”](https://arxiv.org/abs/2408.00094) (2024).

The exclusion must not be overextended. It assumes that detector squeezing,
parametric response, calibration drift, thermal correlations, and other
quantum apparatus effects have been controlled. It excludes a specified
classical input model, not every classical or hybrid gravity theory.

## 7. Why field ontology still does not follow

Replace the named gravitational input mode with a nongravitational quantum
ancilla having the same state and the same beamsplitter channel. Every detector
moment, phase scan, count probability, and multi-time detector statistic in
the frozen model is unchanged.

Equivalently, a direct quantum source--receiver action can be chosen to induce
the same receiver process. Thus the record reconstructs a state **relative to
the selected input port and channel**. It does not reconstruct the ontological
statement “an independent gravitational field mode carried this state.”

The outcomes separate cleanly:

| Question | Earned answer |
|---|---|
| Is the incident Gaussian state reconstructible under a calibrated channel? | Yes, exactly. |
| Does one receiver setting select its own transfer factor? | No. |
| Can a known receiver-reference family calibrate transfer? | Yes, conditional on one stable source across arms. |
| Can phase-sensitive records exclude a scoped classical random drive? | Yes, if sub-vacuum and controls pass. |
| Do clicks or super-vacuum noise alone exclude classical waves? | No. |
| Does state reconstruction identify gravitational field ontology? | No. |
| Is the proposal locally/hardware ready for DU? | No. |

## 8. Updated platform assessment

The 2026 proposal upgrades the `HC-DU-198` platform row from “receiver exists”
to “conditional receiver-side Gaussian tomography is defined.” It supplies:

- a named radiative input mode;
- a receiver and effective interaction;
- prepared detector reference states and phases;
- count and correlation targets; and
- declared detector-noise limitations.

It does not supply:

- controllable or independently verified astrophysical state preparation;
- an action-selected one-mode quotient;
- source stationarity/repeatability and calibration lineage that cannot be
  fitted after the fact;
- complete attempt-level acquisition lineage;
- a no-refit distinction from detector squeezing and direct quantum rivals; or
- a realistic finite packet satisfying DU's no-external-hardware learning rule.

The correct disposition is therefore additive, not promotional. A real
conditional reconstruction theorem now occupies the radiative branch, but the
branch still lacks a physically selected complete packet and a locally
obtainable Grade-5 discriminator.

## 9. Exact regression

Run:

```bash
python3 tests/du_gravitational_radiation_gaussian_tomography_probe.py --write-artifact
```

The artifact is
`tests/artifacts/du_gravitational_radiation_gaussian_tomography_result.json`.
The probe checks:

- physicality of both incident covariance witnesses;
- exact same-output/different-input single-setting nonidentifiability;
- exact receiver-reference slope calibration under a fixed source;
- exact covariance and displacement inversion when transfer is known;
- rank three for the three-phase covariance design and rank two without the
  cross-quadrature phase;
- exact $g^{(2)}=1/2$ at two different couplings;
- double-event probability proportional to $\eta^2$;
- a one-hundredfold trial penalty for a tenfold smaller transfer;
- a sub-vacuum detector output;
- exclusion of the scoped classical random-displacement rival; and
- survival of a response-equivalent quantum ancilla.

Passing proves no astrophysical state preparation, gravitational-wave
quantization, graviton observation, universal classical-gravity exclusion,
experimental feasibility, field ontology, Grade-5 remainder, hardware action,
new DU law, or active successor.

## 10. Disposition and reopener

```text
RADIATIVE_GAUSSIAN_RECONSTRUCTION = CONDITIONAL_GRADE_3
TRANSFER_CALIBRATION               = LOAD_BEARING
REFERENCE_SLOPE_REPAIR             = CONDITIONAL_ON_FIXED_SOURCE
PHASE_REFERENCE                    = LOAD_BEARING
G2_COUPLING_CANCELLATION           = POPULATION_LEVEL_ONLY
FINITE_RECORD_COST                 = COUPLING_DEPENDENT
CLASSICAL_RANDOM_DRIVE             = EXCLUDED_BY_CONTROLLED_SUBVACUUM
QUANTUM_DIRECT_TWIN                = SURVIVES
GRAVITATIONAL_FIELD_ONTOLOGY       = NOT_SELECTED
LIVE_STATE_TRANSITION              = NONE
```

Reopen local work only if a candidate supplies, before external hardware, one
of the following:

1. a source-selected or independently stable state family and an internally
   formed calibration record with an exact no-refit statistic that separates
   the direct quantum twin;
2. a mediator-facing record with independently formed gravitational
   provenance that does not factor through the receiver process; or
3. a proof that the relevant channel, mode, and phase reference are selected
   by the physical theory rather than declared by the measurement design.

Otherwise the next research action should be chosen from the full DU portfolio
rather than continuing to elaborate this hardware-gated branch.

## Boundary

Discovery / Lane-2 instrument. Concepts are *held*, not banked;
formalizations are tested; only invariant-level falsification closes a
concept. This prevents losing an idea to a single articulation.
