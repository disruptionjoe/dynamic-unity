---
title: "Gaseous-TPC oriented trace, head-tail information, and zero-error boundary"
status: banked_scoped_result
doc_type: exploration
created: 2026-07-30
claim_id: HC-DU-180
run_id: RUN-20260731-020729-oriented-material-trace-gate
work_id: ORIENTED-MATERIAL-TRACE-HEAD-TAIL-GATE
action_id: ORIENTED-MATERIAL-TRACE-HEAD-TAIL-GATE
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

# Gaseous-TPC oriented trace, head-tail information, and zero-error boundary

## Executive return

```text
PHYSICAL_ORIENTATION_INFORMATION_FOUND
+ EXACT_ORIENTATION_ONLY_IN_FROZEN_NOISELESS_REGIME
+ BOUNDED_ERROR_HEAD_TAIL_CERTIFICATE
+ ZERO_ERROR_EVENT_CERTIFICATE_NOT_EARNED
+ TRANSIENT_SIGNAL_NOT_RETAINED_MATERIAL_ARCHIVE
+ KNOWN_SOURCE_AND_CALIBRATION_SEPARATELY_TYPED
+ DETERMINISTIC_READOUT_CANNOT_CREATE_ORIENTATION_INFORMATION
+ STANDARD_DETECTOR_AND_STATISTICS_ABSORPTION
+ RESPONSE_ORDER_GATE_UNMET
+ NO_READY_SUCCESSOR
```

`HC-DU-179` showed that a time-insensitive marked-site trace need not contain
an arrow. This wave finds the missing *kind* of physical coordinate:

> A reflection-asymmetric response profile along a track can carry
> orientation information even when the unweighted track geometry is only an
> unoriented axis.

Low-pressure gaseous time-projection chambers realize this condition
imperfectly. Stopping and ionization physics can make the two ends of a recoil
track statistically different. DRIFT, MIMAC, and high-definition TPC work
extract that difference from charge distributions or waveforms. The
orientation information is therefore not merely a label invented by an
observer.

The stronger conclusion does not follow. The primary ionization is transient;
drift, diffusion, avalanche, electronics, digitization, calibration, and
reconstruction intervene before a retained accessible record exists.
Orientation-conditioned signal laws overlap. Published demonstrations rely
on calibrated detector response, known source geometries, ensemble
statistics, simulation, or a fitted response model. These are legitimate
physical and inferential interfaces, but they do not turn every event into a
zero-error certificate of its vector sense or upstream source.

The exact statistical boundary is:

\[
P_{\mathrm{err}}^\star
=
\frac{1-\operatorname{TV}(\mu_+,\mu_-)}{2}
\tag{1}
\]

for equal orientation priors. Here \(\mu_+\) and \(\mu_-\) are the complete
orientation-conditioned record laws. Nonzero total variation gives usable
head-tail information. Zero error requires mutually singular laws.

This is a real advance from an unweighted spatial trace to a physically
polarized trace. It is fully absorbed by standard stopping-power, detector,
directional-reconstruction, and statistical-decision theory. It supplies no
unabsorbed higher-response question, so the causal-response campaign remains
quiescent.

## 1. Frozen question and evidence coordinates

The run asked:

> Does a gaseous TPC physically encode recoil-vector sense, or is head-tail
> direction supplied only by a known source, time sampling, calibration, or a
> reconstruction model?

The scope/status/formation coordinates are:

- **scope:** a prepared detector and its declared readout/action envelope,
  not a global record;
- **status:** the ionization, drift, and induced signals are physical; the
  inferred orientation and source classification are model- and
  error-relative;
- **formation:** the asymmetry is formed by a recoil and detector response;
  the result does not adjudicate source issuance versus disclosure for the
  universe as a whole.

No observer's belief creates the ionization profile. Conversely, calling the
profile physical does not make its interpretation exact or its archive
automatically selected.

## 2. Typed detector chain

Keep the full chain explicit:

\[
X
\longrightarrow
H
\longrightarrow
I
\longrightarrow
D
\longrightarrow
A
\longrightarrow
W
\longrightarrow
\widehat q
\longrightarrow
\widehat o
\longrightarrow
\widehat s .
\tag{2}
\]

Here:

- \(X\) is the upstream particle/source history;
- \(H\) is the stochastic recoil and collision history;
- \(I\) is the primary ionization field along the recoil;
- \(D\) is drift and diffusion;
- \(A\) is avalanche amplification and induced current;
- \(W\) is a sampled waveform or pixel-charge packet;
- \(\widehat q\) is a calibrated or deconvolved charge profile;
- \(\widehat o\) is a head-tail statistic, likelihood, or orientation
  estimate; and
- \(\widehat s\) is an inferred particle/source class.

The chain prevents four casts:

```text
physical primary asymmetry != retained archive;
sample order != intrinsic event time;
known calibration-source direction != detector-internal provenance;
bounded-error head-tail estimate != exact upstream biography.
```

## 3. Primary-source reconstruction

### 3.1 DRIFT: physical asymmetry, known source, ensemble certificate

Battat et al.,
[“First measurement of nuclear recoil head-tail sense in a fiducialised WIMP
dark matter detector”](https://arxiv.org/abs/1606.05364),
use a low-pressure negative-ion TPC. Sulfur, fluorine, and carbon recoils were
produced by a \(^{252}\mathrm{Cf}\) neutron source placed at declared
\(+z,-z,-x,-y\) locations around the detector.

Several duties are physically realized:

- recoil ionization is produced in the gas;
- charge carriers drift under an electric field;
- minority-carrier arrival-time differences supply an absolute drift-axis
  position after calibration; and
- microsecond sampling converts the drift coordinate into an ordered
  waveform coordinate.

The head-tail statistic is not the bare track axis. The source splits the main
signal peak into two equal time regions and defines:

\[
\alpha=\frac{\eta_1}{\eta_2},
\tag{3}
\]

where \(\eta_1,\eta_2\) are integrated charges in the two halves. The physical
premise is that nuclear-recoil ionization density is larger near the start of
the track than near the end in the admitted regime. The paper then compares
mean asymmetries across detector sides and source placements.

The reported result is significant head-tail *sensitivity*, not a proof that
each event has an error-free orientation. The authors report dependence on
energy, diffusion, detector axis, analysis threshold, charge shaping,
scattered neutrons, and unresolved recoil species. The known source placement
is necessary to validate which sign should count as correct.

Typed verdict:

```text
gas response contains orientation information;
known source plus calibrated waveform tests that information;
the published ensemble asymmetry is not an intrinsic zero-error event label.
```

### 3.2 MIMAC: transient response contains information that readout distorts

Beaufort et al.,
[“Directionality and head-tail recognition in the keV-range with the MIMAC
detector by deconvolution of the ionic
signal”](https://arxiv.org/abs/2112.12469),
make the source-to-readout boundary especially clear.

At high gain, avalanche ions distort the signal induced on the Micromegas
grid. The paper derives and experimentally validates an analytical
deconvolution that estimates the primary-electron time distribution. In its
admitted proton-energy and gas regime, the stopping power is asymmetric along
the path, producing more charge near one end. That response supports
head-tail recognition and reconstructed monoenergetic neutron spectra with
reported angular resolution better than \(15^\circ\).

This is a positive for Dynamic Unity:

> The downstream ionic signal is not a detached symbol. It is a physical
> transformation of a transient primary-electron distribution that already
> contains directional information.

It is also a boundary:

- the deconvolution has approximations and an observed offset;
- the relation uses detector gain, gas response, ionization quenching,
  diffusion, drift, and source geometry;
- source beams and calibration establish the physical polarity convention;
  and
- the signal becomes retained only through electronic acquisition.

Deconvolution may recover information obscured by a known physical channel.
It does not create information that was absent from the primary response.

### 3.3 Primary-track recovery: two hypotheses, not an intrinsic arrow

Lewis et al.,
[“Primary track recovery in high-definition gas time projection
chambers”](https://arxiv.org/abs/2106.15829),
model the primary charge density with a Bragg-profile fit. The reconstruction
fits both the default and flipped orientations and selects the lower
\(\chi^2\) hypothesis.

The paper explicitly treats:

- stochastic primary ionization;
- multiple-scattering loss of the initial direction;
- diffusion, amplification, saturation, thresholding, and pixel integration;
- a Bragg model obtained from simulated recoil profiles;
- calibration of diffusion for absolute drift position; and
- head-tail efficiency as the fraction of truth-labelled tracks assigned the
  correct sign.

This is standard, honest model-based discrimination. It supplies an excellent
host for the exact statistical statement in Section 5. It does not support an
unqualified claim that the visible point cloud intrinsically contains its own
causal arrow.

### 3.4 Material comparison

Couturier et al.,
[“Dark Matter directional detection: comparison of the track direction
determination”](https://arxiv.org/abs/1607.08157),
use SRIM histories to compare directional preservation in emulsions,
anisotropic crystals, and low-pressure gaseous TPCs. The simulated initial
direction is lost earlier in the emulsion and crystal specimens and is better
preserved in the gas mixture. The authors still call for calibration beams
with known direction and energy to validate the simulations.

This directly refines `HC-DU-179`: a material is not merely “a track
detector.” Its collision and stopping regime determines how much initial
direction survives into the formed response.

## 4. Exact oriented-trace theorem

Let an unweighted path be an unoriented interval
\([0,L]/(s\sim L-s)\). Let a scalar response profile on a chosen
parameterization be \(q(s)\). Path reversal acts by:

\[
(\mathcal Rq)(s)=q(L-s).
\tag{4}
\]

Let \(o\in\{+,-\}\) be the target orientation.

### Proposition 1 — deterministic orientation factorization

Within a frozen response class in which:

1. the only orientation alternatives are \(q\) and \(\mathcal Rq\); and
2. the physical response law fixes which profile polarity corresponds to the
   start of the event,

the complete profile factors \(o\) exactly iff:

\[
q\ne\mathcal Rq.
\tag{5}
\]

If \(q=\mathcal Rq\), the two orientations have the same record and no
record-only function can recover \(o\). If they differ, the two-element
record fibre separates the orientations.

A reflection-odd functional, such as a centered first moment,

\[
M(q)=\int_0^L(s-L/2)q(s)\,ds,
\tag{6}
\]

satisfies \(M(\mathcal Rq)=-M(q)\). In a regime where \(M(q)\ne0\) and the
physical polarity convention is frozen, its sign is an orientation tag.

This proposition does **not** say arbitrary asymmetry identifies the start of
a track. Without a physical response law or calibration connecting profile
polarity to event order, the profile merely distinguishes its two ends.

### Proposition 2 — stochastic head-tail boundary

Let \(\mu_+\) and \(\mu_-\) be the complete record laws conditioned on the two
orientations. Under equal priors, the optimal decision error is Equation (1).
Therefore:

\[
\operatorname{TV}(\mu_+,\mu_-)>0
\quad\Longleftrightarrow\quad
P_{\mathrm{err}}^\star<\frac12,
\tag{7}
\]

and:

\[
P_{\mathrm{err}}^\star=0
\quad\Longleftrightarrow\quad
\mu_+\perp\mu_-.
\tag{8}
\]

The first condition earns usable head-tail information. The second earns
zero-error orientation certification.

The exact finite fixture uses:

\[
\mu_+=(4/5,1/5),\qquad
\mu_-=(1/5,4/5).
\tag{9}
\]

It gives:

\[
\operatorname{TV}=3/5,\qquad
P_{\mathrm{err}}^\star=1/5.
\tag{10}
\]

This is informative and nonfinal.

### Proposition 3 — downstream readout cannot create missing orientation

Let \(K\) be any common stochastic channel representing diffusion,
amplification, digitization, or deterministic reconstruction. Then:

\[
\operatorname{TV}(K_\ast\mu_+,K_\ast\mu_-)
\le
\operatorname{TV}(\mu_+,\mu_-).
\tag{11}
\]

This is the data-processing contraction for total variation. A downstream
pipeline may expose a sufficient statistic or reverse a known invertible
distortion, but it cannot exceed the discrimination information in the
complete input it receives.

Adding a known source label is not a counterexample. It enlarges the record
packet with side information rather than processing the detector response
alone.

## 5. What kind of record has formed?

The audited TPC chain crosses some but not all rungs:

| rung | disposition |
|---|---|
| recoil occurrence | physically admitted but not identified by the signal alone |
| primary ionization trace | physically formed, local, and transient |
| spatial axis | reconstructible in a declared resolution regime |
| physical polarity information | present when orientation-conditioned laws differ |
| bounded-error orientation certificate | available after a frozen detector/calibration contract |
| zero-error orientation certificate | not generally earned because the laws overlap |
| persistent material archive | not supplied by the transient gas charge cloud |
| path membership in multi-event exposure | requires event building and association |
| event time and upstream source identity | separately inferred and generally nonunique |
| public/action-enabling fact | requires retained acquisition, access, fault, and decision contracts |

This corrects two opposite errors:

```text
reconstruction used -> no physical provenance
```

is false because stopping and ionization dynamics can physically polarize a
track; while:

```text
head-tail sensitivity -> exact causal biography
```

is false because the polarity is noisy, transient, calibrated, and
target-relative.

## 6. Campaign effect

The material provenance ladder is refined to:

```text
local material formation
< spatial trace or axis
< reflection-asymmetric physical profile
< bounded-error orientation certificate
< zero-error orientation certificate
< path/event membership
< event time
< source identity.
```

The `<` symbols mark stronger target duties, not a claim that every detector
implements a universal linear ladder.

`HC-DU-180` answers one question left by `HC-DU-179`: an explicit clock or
edge tag is not the only possible orientation carrier. A graded response
field can break the reversal symmetry. But the advance does not join the two
positive detector branches:

- emulsion supplies long material retention but weak/ambiguous direction;
- gaseous TPCs preserve and expose more direction but the ionization carrier
  is transient and the retained record is supplied by acquisition.

The yet-unbuilt physical conjunction is:

```text
formed event
+ retained spatial carrier
+ physically polarized path
+ bounded or exact association
+ selected acquisition/access
+ invariant held-out response consequence.
```

## 7. Absorber and novelty audit

The components are absorbed by:

- stopping power and Bragg curves;
- ionization quenching and range straggling;
- negative-ion and electron-drift TPC physics;
- diffusion, avalanche, electronics, and detector calibration;
- directional dark-matter detector reconstruction;
- binary hypothesis testing and likelihood ratios;
- total variation and data-processing inequalities; and
- sufficient statistics and source classification.

Dynamic Unity's contribution here is a typed synthesis and exact boundary:
it distinguishes an unoriented material axis, physical response polarity,
bounded-error orientation, zero-error certification, persistent archive, and
upstream source identity. That is useful architecture, not new detector
physics or a new law.

## 8. Grade and nonclaims

Earned:

- scoped Grade-4 deterministic factorization, stochastic certification, and
  readout-contraction boundaries;
- conditional Grade-3 bounded-error orientation reconstruction inside a
  frozen detector and response class;
- Grade-2 reconstruction of four primary detector sources; and
- an exact nine-check local regression.

Not earned:

- zero-error experimental head-tail certification;
- retained material orientation in the gaseous carrier;
- unique path membership, event time, or particle/source identity;
- physically selected calibration, readout, archive, observer, or action
  class;
- an invariant unabsorbed higher-response discriminator;
- new physics, record ontology, public finality, or a paper claim.

## 9. Disposition

```text
PHYSICAL_ORIENTATION_INFORMATION_FOUND
+ EXACT_ORIENTATION_ONLY_IN_FROZEN_NOISELESS_REGIME
+ BOUNDED_ERROR_HEAD_TAIL_CERTIFICATE
+ ZERO_ERROR_EVENT_CERTIFICATE_NOT_EARNED
+ TRANSIENT_SIGNAL_NOT_RETAINED_MATERIAL_ARCHIVE
+ STANDARD_DETECTOR_AND_STATISTICS_ABSORPTION
+ RESPONSE_ORDER_GATE_UNMET
+ NO_READY_SUCCESSOR
```

Wave 3 remains ineligible. A future reopener must join a physically retained
path carrier and polarity/association mechanism with a selected access
contract, and must still expose an invariant response-order consequence not
already absorbed by standard detector or response theory.
