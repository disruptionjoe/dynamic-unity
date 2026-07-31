---
title: "Quantum-gravity matched-noise response: classical realization and two-frequency FDT boundary"
status: explored
doc_type: governed_research_swing
created: 2026-07-31
claim_id: HC-DU-193
claim_status_change: none
disposition: ORDERED_SPECTRUM_COMMUTING_NOISE_KILL_AND_FIELD_ATTRIBUTION_STOP
---

# Quantum-gravity matched-noise response boundary

## Result

The reopener from `HC-DU-192` separates into three different claims. First, in
a calibrated equilibrium KMS class, the symmetrized noise and dissipative
linear response are not independent: the quantum fluctuation--dissipation
relation joins them. Second, outside that class, a classical Gaussian
input--output process can reproduce both an arbitrary admissible symmetrized
covariance and a chosen causal susceptibility. A measured c-number response is
therefore not yet an operator commutator or a quantum-mediator certificate.
Third, an **ordered** noise spectrum supplies a narrower discriminator: its KMS
emission/absorption asymmetry excludes a real stationary commuting scalar-noise
rival, and a two-frequency calibrated FDT contrast excludes a single-temperature
classical equilibrium FDT. Neither identifies a gravitational field, because a
direct quantum interaction or environment can reproduce the same probe process.

This is a scoped Grade-4 rival boundary, not a new law or a quantum-gravity
prediction.

## Cold-start contract

- **Purpose / North Star:** find a selected material interface and a finite
  no-refit rival discriminator before assigning a response to new physics.
- **Current state:** the scientific portfolio remains quiescent. `HC-DU-192`
  leaves one conditional reopener at ordered response after matching mean and
  symmetrized noise. This swing does not change `CURRENT-RESEARCH.yaml`.
- **Bounded question:** what does causal susceptibility add after noise is
  matched, and what is the smallest extra observable that excludes a declared
  commuting stochastic rival?
- **Perspective / status:** model systems and interactions are ontic;
  estimated spectra are epistemic; field mediation and direct action remain
  competing ontologies after endpoint process equivalence.
- **Lanes / channels:** Lane 1 with Lanes 2, 6, and 7 support;
  `CH-FORMAL`, `CH-MODEL`, `CH-COLLIDE`, and `CH-EMPIRICAL`.
- **Maximum grade:** scoped Grade 4. Grade 5 would require a source-pinned,
  no-refit statistic separating every frozen rival in a realizable packet.

## Frozen objects and rivals

For one selected scalar probe observable, distinguish:

1. the mean response;
2. the symmetrized covariance or noise spectrum;
3. the retarded c-number susceptibility;
4. the two ordered spectra or sequential response; and
5. the provenance and component access that attribute the process to a
   mediator.

The rivals are:

- an equilibrium quantum harmonic environment;
- a real stationary commuting Gaussian noise process;
- an unrestricted classical stochastic input--output realization;
- a one-temperature classical equilibrium linear bath;
- a direct quantum interaction or environment; and
- quantized-field mediation.

No rival may be refit after the target statistic is revealed.

## 1. KMS makes the proposed same-noise/different-response pair inconsistent

For observables $A$ and $B$, the retarded Kubo response is

\[
\chi_{AB}(t)=\frac{i}{\hbar}\,\theta(t)\,
\omega\!\left([A(t),B(0)]\right).
\]

For a calibrated beta-KMS state, the KMS relation joins the two orderings of
the correlation function. In the harmonic scalar case,

\[
\frac{S_{\mathrm{sym}}(\omega)}{\chi''(\omega)}
=\hbar\coth\!\left(\frac{\beta\hbar\omega}{2}\right).
\]

Thus, at fixed temperature and within the frozen equilibrium class, matching
the complete symmetrized spectrum already matches the dissipative response.
The proposed target cannot be varied independently there. This is not a new DU
result: it is the physical specialization of the passive-response
reconstruction already banked in `HC-DU-099`.

The qualification matters. Without calibrated temperature, equilibrium, and
the complete relevant frequency domain, the reconstruction does not follow.
Dispersive terms also require the usual causal analyticity and subtraction
contract.

## 2. Noise plus c-number response still has a classical realization

Let $N(t-s)$ be any positive-definite real stationary covariance with a finite
harmonic representation

\[
N(t-s)=\sum_j A_j\cos\!\left(\omega_j(t-s)\right).
\]

Choose independent standard normal variables $u_j,v_j$ and define

\[
\xi(t)=\sum_j\sqrt{A_j}
\left(u_j\cos\omega_j t+v_j\sin\omega_j t\right).
\]

Then $\mathbb E[\xi(t)\xi(s)]=N(t-s)$. For any selected causal kernel $D_R$,
the classical input--output law

\[
X_f(t)=\xi(t)+\int D_R(t-s)f(s)\,ds
\]

reproduces both that covariance and that mean response exactly. It need not be
an autonomous equilibrium bath, but it is an exact operational realization.
Consequently, observing a symmetrized noise kernel and a c-number
susceptibility does not by itself prove a noncommuting mediator.

This closes the loose wording in `HC-DU-192`: “mediator-facing noncommuting
response” cannot mean susceptibility alone.

## 3. Ordered spectra exclude the commuting scalar-noise rival

For a thermal quantum oscillator, using the convention
$S(\omega)=\int dt\,e^{i\omega t}\langle x(t)x(0)\rangle$,

\[
\frac{S(-\omega)}{S(+\omega)}=e^{-\beta\hbar\omega}.
\]

A two-level quantum probe can sample the two orderings through its upward and
downward transition rates. By contrast, for a real scalar stationary classical
process, commutativity and stationarity imply $C(-t)=C(t)$ and hence
$S(-\omega)=S(+\omega)$. A nonunit ratio therefore excludes that frozen
commuting external-noise class.

It does **not** exclude arbitrary classical stochastic dynamics. A larger
state-space model with feedback, state-dependent transitions, or an explicitly
installed response can reproduce the same endpoint transition law. Such a
repair changes the rival from scalar noise into a complete dynamical
input--output model and must be named rather than silently counted as the same
class.

## 4. Two calibrated frequencies give an exact equilibrium discriminator

In units $k_B=\hbar=1$, define

\[
T_{\mathrm{eff}}(\omega)
=\frac{\omega}{2}\,
\frac{S_{\mathrm{sym}}(\omega)}{\chi''(\omega)}.
\]

The classical one-temperature equilibrium FDT makes
$T_{\mathrm{eff}}(\omega)=T$ at every frequency. The quantum harmonic relation
gives

\[
T_{\mathrm{eff}}^{q}(\omega)
=\frac{\omega}{2}\coth\!\left(\frac{\beta\omega}{2}\right).
\]

This is strictly increasing for positive frequency at finite beta. Writing
$x=\beta\omega/2$, the derivative of $x\coth x$ has numerator
$\sinh x\cosh x-x>0$, because its derivative is $2\sinh^2x$. Therefore two
distinct calibrated modes reject a single-temperature classical equilibrium
FDT without an absolute magnitude fit. The contrast disappears continuously
in the high-temperature limit, which is the required positive control.

The result is class-relative. A colored nonequilibrium stochastic model can
match both frequencies by construction.

## 5. Direct action remains an attribution absorber

Ordered asymmetry can certify that the effective probe environment is not the
declared commuting scalar-noise process. It does not certify that the relevant
noncommutativity belongs to a gravitational field. `HC-DU-148` already proves
the decisive finite counterexample: a mediator can copy, apply a controlled
phase, and uncompute, producing the same endpoint matter channel as a direct
quantum controlled interaction. Gaussian influence-function representations
likewise preserve response and noise kernels after the field is eliminated.

Field attribution therefore needs at least one of:

- component access that cannot be represented inside the direct model;
- a source-pinned cross-response whose direct and field rivals make different
  locked predictions;
- a separately selected local mediator algebra and provenance map; or
- a theorem restricting the admissible direct-action realization class.

## Revised observable hierarchy

The prior four-level hierarchy must be refined:

1. **Mean:** rejects only rivals with a different calibrated mean law.
2. **Symmetrized cumulants / visibility:** rejects expectation-only closure but
   is reproducible by classical profile and stochastic models.
3. **Complementary coherence / entanglement:** excludes declared incoherent or
   separable-channel rivals, not every direct quantum rival.
4. **C-number causal susceptibility:** adds response, but has an exact
   classical input--output realization.
5. **Ordered spectral asymmetry or incompatible sequential response:** excludes
   the frozen real commuting scalar-noise class.
6. **Mediator provenance or component access:** is still required to identify
   a field rather than an endpoint-equivalent direct quantum interaction.

## Literature collision

- Kubo's fluctuation--dissipation theorem supplies the equilibrium response
  relation: [Kubo 1957](https://doi.org/10.1103/PhysRev.101.1620).
- Quantum-noise measurement and asymmetric spectra are standard open-system
  machinery: [Clerk et al.](https://arxiv.org/abs/0810.4729).
- Two-level systems as spectrometers operationalize the two orderings:
  [Schoelkopf et al.](https://arxiv.org/abs/cond-mat/0210247).
- Quantum Langevin and influence-functional constructions explain why noise
  and dissipation kernels can descend to reduced stochastic descriptions:
  [Johnson and Hu](https://arxiv.org/abs/quant-ph/0012137),
  [Hu, Paz, and Zhang](https://arxiv.org/abs/gr-qc/9512049).
- `HC-DU-099`, `HC-DU-101`, and `HC-DU-148` are the in-repository absorbers.

The component mathematics is mature. DU's earned contribution here is the
typed rival and attribution boundary, not discovery of FDT or quantum noise
spectroscopy.

## Exact local probe

`tests/du_quantum_gravity_matched_noise_response_probe.py` verifies:

- the harmonic KMS covariance and response objects;
- an explicit classical Gaussian realization of the symmetrized covariance;
- exact copying of the c-number causal response;
- the missing imaginary ordered-correlation part in the commuting scalar
  model;
- KMS emission/absorption asymmetry versus an even classical spectrum;
- the two-frequency one-temperature FDT discriminator;
- the strict-monotonicity certificate; and
- recovery of the classical FDT in the high-temperature limit.

The probe is an exact finite boundary fixture, not an empirical simulation.

## Disposition and reopener

Disposition:
`ORDERED_SPECTRUM_COMMUTING_NOISE_KILL_AND_FIELD_ATTRIBUTION_STOP`.

The next admissible theoretical reopener is narrow:

> In a source-pinned gravitational candidate, can one transport the frozen
> response to two independently calibrated frequencies or to an ordered
> sequential statistic, while retaining source deletion, conserved apparatus,
> direct-action, and quantized-matter cross-talk controls without refitting?

Before that map exists, apparatus optimization and hardware work are
premature. A positive ordered-spectrum result would reject a declared
commuting-noise rival; it would still require a distinct field-attribution
receipt.

## Nonclaims

- No observed gravitational effect or experimental apparatus is modeled.
- No universal classical stochastic, semiclassical, or direct-action theory
  is excluded.
- No operator commutator is inferred from a fitted c-number susceptibility.
- No gravitational field ontology, material record interface, new DU law,
  paper promotion, successor, or later-wave activation is earned.
