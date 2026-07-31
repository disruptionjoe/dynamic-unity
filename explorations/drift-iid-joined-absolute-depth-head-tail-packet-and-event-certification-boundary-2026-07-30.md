---
title: "DRIFT-IId joined absolute-depth/head-tail packet and event-certification boundary"
status: banked_scoped_result
doc_type: exploration
created: 2026-07-30
claim_id: HC-DU-184
run_id: RUN-20260731-031215-drift-joined-depth-head-tail-gate
work_id: DRIFT-JOINED-DEPTH-HEAD-TAIL-GATE
action_id: DRIFT-JOINED-DEPTH-HEAD-TAIL-GATE
program_id: CCR-MINIMAL-PHYSICAL-ANTECEDENT-TO-FINITE-REMAINDER
owner_repo: dynamic-unity
primary_lane: lane_3
supporting_lanes:
  - lane_1
  - lane_4
  - lane_7
channels:
  - CH-EMPIRICAL
  - CH-FORMAL
  - CH-MODEL
  - CH-COLLIDE
evidence_grade: 4
maximum_grade: 4
---

# DRIFT-IId joined absolute-depth/head-tail packet and event-certification boundary

## Executive return

```text
SINGLE-CONFIGURATION_DEPTH_AND_HEAD-TAIL_PACKET_FOUND
+ NO_CROSS-PLATFORM_STITCHING_REQUIRED
+ MULTI-CARRIER_ABSOLUTE_Z_AND_HEAD-TAIL_RESPONSE_JOINED
+ PHYSICAL_PATH-POLARITY_INFORMATION_JOINED
+ ENSEMBLE_DIRECTIONAL_SENSITIVITY_ESTABLISHED
+ ENSEMBLE_ASYMMETRY_DOES_NOT_IMPLY PER-EVENT CERTIFICATION
+ KNOWN_NEUTRON-SOURCE_GEOMETRY_IS IMPORTED SIDE INFORMATION
+ LOW-Z_PEAK-OVERLAP_AND_HIGH-Z_TRIGGER/DIFFUSION_RESTRICT THE EVENT CLASS
+ RECOIL_SPECIES_AND UPSTREAM_SOURCE_NOT CERTIFIED
+ STANDARD_DIRECTIONAL-TPC_AND BINARY-TESTING ABSORPTION
+ RESPONSE-ORDER_GATE_UNMET
+ NO_READY_SUCCESSOR
```

`HC-DU-182` concluded that absolute depth and head-tail response were
separately demonstrated but had not been joined in one source-pinned
instrument. That conclusion was too narrow. Battat et al.'s DRIFT-IId
[head-tail measurement](https://arxiv.org/abs/1606.05364) uses the same
oxygen-doped negative-ion operating mode to:

- form multiple carrier species with distinct arrival times;
- reconstruct the absolute \(z\) vertex of admitted events;
- retain individual triggered waveforms;
- compute an ionization-asymmetry statistic along the main charge pulse; and
- demonstrate that the ensemble asymmetry reverses under \(+z\) versus
  \(-z\) neutron illumination while transverse controls return null.

This is one real apparatus and one declared gas/readout mode. Dynamic Unity
can therefore bank a joined absolute-depth and physical head-tail response
packet without combining Timepix3, MIMAC, and negative-ion results.

The correction does not yield an event-level direction certificate. The
reported head-tail observable is an average asymmetry over source-positioned
event ensembles. The neutron-source location labels the expected run
direction. Event-statistic laws can have opposite means while retaining
overlapping support, so the optimal classification error for one unknown
event remains nonzero.

The exact boundary is:

> Ensemble reversal sensitivity establishes physical orientation
> information. It certifies the sense of one event with zero error only when
> the admitted orientation-conditioned event laws have disjoint support.

## 1. Frozen question

> Has one existing source-pinned detector physically joined absolute depth,
> acquired event waveforms, and path polarity; and if so, does its published
> head-tail result certify the direction of each realized event?

The swing forbids two opposite errors:

```text
ensemble head-tail sensitivity
!= merely an analyst label
```

and:

```text
ensemble head-tail sensitivity
!= zero-error direction certificate for every event.
```

## 2. The joined DRIFT-IId packet

The source describes two back-to-back negative-ion TPCs operated with
CS\(_2\)+CF\(_4\)+O\(_2\). Ionization produces a primary I cloud and several
minority carriers. Their distinct velocities make the I--P arrival
difference an absolute-\(z\) coordinate:

\[
z=(t_i-t_p)\frac{v_iv_p}{v_p-v_i}.
\tag{1}
\]

The same triggered waveform supplies the temporal ionization profile used
for head-tail analysis. The paper integrates charge over the first and
second halves of the main I peak and forms an asymmetry statistic. Source
runs from \(+z\), \(-z\), \(-x\), and \(-y\) test whether the statistic
tracks reversal rather than merely responding to any neutron exposure.

The physically joined event packet is at least

\[
q_{\rm DRIFT}
=
(\text{wire waveforms},t_D,t_P,t_S,t_I,
  z,\text{NIPs},\alpha,\text{trigger/calibration context}).
\tag{2}
\]

The exact field population varies by event: the analysis often used I and P
for depth because S could be suppressed at high \(z\). At low \(z\), the
carrier peaks overlap and the paper excludes roughly 30% of the active
volume from the head-tail analysis. At high \(z\) and low energy, diffusion
can broaden pulses below the acquisition trigger. These are typed event-class
restrictions, not reasons to deny the joined packet on its admitted domain.

The earlier DRIFT-IId
[fully fiducialised search](https://arxiv.org/abs/1410.7821)
independently demonstrates that the same minority-carrier mode was used in a
source-free directional search and provides explicit efficiency maps and
failure regions. That supports physical realizability and makes the
event-class boundary visible.

## 3. Physical orientation information versus event certification

Let \(A\) be the signed event asymmetry statistic and let
\(\mu_+\), \(\mu_-\) be its laws for opposite source-relative recoil
directions. A reversal-sensitive ensemble requires, at minimum,

\[
\mathbb E_{\mu_+}[A]\ne\mathbb E_{\mu_-}[A].
\tag{3}
\]

That implies the laws differ and therefore that \(A\) contains some
orientation information. It does not imply exact one-event decoding.

For equal priors, the minimum one-event classification error is

\[
P_e^\star
=
\frac{1-\operatorname{TV}(\mu_+,\mu_-)}{2}.
\tag{4}
\]

Zero error requires total variation one, equivalently disjoint supports up
to null sets.

### 3.1 Exact hostile fixture

Take \(A\in\{-1,0,+1\}\) with

\[
\mu_+=(0,\tfrac34,\tfrac14),
\qquad
\mu_-=(\tfrac14,\tfrac34,0).
\tag{5}
\]

Then

\[
\mathbb E_{\mu_+}[A]=\tfrac14,
\qquad
\mathbb E_{\mu_-}[A]=-\tfrac14,
\]

so the ensemble mean cleanly reverses. But

\[
\operatorname{TV}(\mu_+,\mu_-)=\tfrac14,
\qquad
P_e^\star=\tfrac38.
\tag{6}
\]

With four independent events, the shared all-zero outcome has probability
\((3/4)^4\), and the equal-prior error falls to \(81/512\). Replication makes
the ensemble result stronger while leaving the one-event error in (6)
unchanged. This is the exact distinction the source requires.

The fixture is not fitted to DRIFT data. It proves that an ensemble sign
reversal cannot, without a support or likelihood analysis, be promoted to a
zero-error event certificate.

## 4. The known-source-direction boundary

The calibration uses a \(^{252}\)Cf neutron source positioned around the
detector. Its placement determines which run should be \(+z\), \(-z\), or
transverse. That is a correct and powerful experimental design: source
reversal plus transverse null controls test whether the detector response
contains physical polarity information.

The source label is not an intrinsic field of an unknown event packet. For a
future WIMP candidate, the task is inverted: infer direction from the
waveform without knowing the source location. The event law, detector
calibration, efficiency, and systematics then determine the error.

This yields the typed result:

| Claim | Status |
|---|---|
| the gas/readout response carries head-tail information | source-pinned physical positive |
| absolute \(z\) and head-tail response coexist in one mode | source-pinned physical positive |
| ensemble means reverse under known source geometry | measured positive |
| every admitted event has a correct head-tail label | not established |
| carbon, fluorine, and sulfur recoil species are identified event by event | not established |
| upstream WIMP/neutron/source identity is certified | not established |

The paper also reports systematic discrepancies between the magnitude of the
\(+z\) and \(-z\) asymmetry outside the high-\(z\) subset. Those systematics
do not erase the measured orientation information, but they prevent a
stronger universal or calibration-free reading.

## 5. Updated material-record ladder

The detector campaign can now replace a hypothetical composite with one
real joined stage:

```text
formed ionization
< triggered waveform acquisition
< multi-carrier absolute-depth reconstruction
< reflection-asymmetric ionization response
< source-relative ensemble head-tail sensitivity
< per-event head-tail likelihood with declared error
< zero-error event polarity certificate
< retained source provenance
< selected observer access/finality quotient.
```

The first five stages are physically joined in DRIFT-IId on a restricted
event class. The last four are not.

## 6. Absorbers, novelty, and grade

The component result is absorbed by:

- negative-ion TPC transport and minority-carrier fiducialisation;
- stopping power and Bragg-like ionization response;
- triggered waveform acquisition and shaping correction;
- directional-detector calibration and source-reversal controls;
- binary hypothesis testing, total variation, and ensemble statistics;
- detector efficiency, diffusion, threshold, and systematic-error analysis;
  and
- particle/source classification.

The Dynamic Unity contribution at current grade is the typed correction:

> A single detector can physically join absolute-depth and head-tail
> information, while the strength of the head-tail claim remains indexed to
> ensemble, event law, and certification target.

Grades:

- **Grade 4:** exact ensemble/event-certification and factorization boundary;
- **conditional Grade 3:** joined absolute-depth and head-tail reconstruction
  on the source's admitted detector/event class;
- **Grade 2:** primary-source detector audit;
- **not earned:** a novel detector theorem, zero-error event certificate, new
  physics, response-order discriminator, paper seed, or successor.

## 7. Campaign consequence

One meaningful obligation is partially closed. Dynamic Unity no longer needs
to search for evidence that absolute depth and physical path-polarity
information can coexist in one acquired packet. They do.

The next detector-level obligation is narrower:

> For one source-pinned configuration, publish or derive the
> orientation-conditioned event laws, calibrated likelihood, or support
> boundary needed to turn ensemble head-tail sensitivity into a declared
> per-event error or certificate.

This still cannot reopen Wave 3 alone. The unabsorbed response-order
discriminator remains absent, and source identity plus selected access are
still open.

## 8. Exact regression

Run:

```bash
python3 tests/du_drift_joined_depth_head_tail_probe.py --write-artifact
```

The artifact is
`tests/artifacts/du_drift_joined_depth_head_tail_result.json`.

Passing establishes:

- one packet can join multi-carrier timing and an orientation statistic;
- distinct carrier speeds retain the absolute-depth rank repair;
- a missing minority peak restores depth ambiguity;
- opposite ensemble means can coexist with substantial event-law overlap;
- replication strengthens ensemble detection without certifying one event;
- disjoint event laws are the zero-error positive control;
- known source geometry is imported side information;
- the joined packet need not factor recoil species; and
- a trigger does not force path orientation.

It does not simulate DRIFT or promote a scientific successor.
