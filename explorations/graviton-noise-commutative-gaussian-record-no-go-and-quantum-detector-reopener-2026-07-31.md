---
title: "Graviton noise: commutative Gaussian record no-go and quantum-detector reopener"
status: explored
doc_type: governed_research_swing
created: 2026-07-31
claim_id: HC-DU-194
claim_status_change: none
disposition: CLASSICAL_ARM_RECORD_ABSORBED_QUANTUM_DETECTOR_PROCESS_REOPENED
---

# Graviton-noise record boundary

## Result

Parikh, Wilczek, and Zahariade supply a real source-to-response calculation:
they integrate out a quantized linear gravitational field, derive its
influence functional, and obtain state-dependent noise and radiation reaction
for a model interferometer arm. But the prediction surface they recommend for
observation is deliberately converted into a classical stochastic process.
The vacuum, thermal, squeezed, and nearby-detector kernels enter through
Gaussian noise, the arm is taken to a classical equal-path saddle, and the
reported mean, variance, autocorrelation, power spectrum, and cross-detector
correlation are commutative record statistics.

That yields an exact scope result:

> No statistic of a commutative Gaussian detector record can certify that its
> source was a quantized field. The complete record law has a classical
> Gaussian realization; any deterministic classical detector response or
> post-processing preserves that observational equivalence.

This does not refute the quantum derivation. It blocks the stronger inference
from a noise spectrum—even one containing $\hbar$, a squeezed enhancement, or
cross-detector correlations—to unique graviton or field attribution. The
paper's exact pre-saddle quantum transition probability remains a legitimate
reopener. It would need to be accessed by incompatible detector preparations,
energy-selective transitions, or another multi-time quantum instrument that
retains the ordered rather than only symmetrized field correlation.

The result earns a scoped Grade-4 nonidentification theorem and primary-source
disposition. It earns no new gravitational prediction.

## Cold-start contract

- **Purpose / North Star:** find a target-blind physical antecedent and a
  finite no-refit record that separates physical rivals without promoting a
  representation into ontology.
- **Current state:** the scientific portfolio remains explicitly quiescent.
  `HC-DU-193` reopened a source-pinned two-frequency or ordered-response map.
  This swing audits the closest gravitational noise/response construction and
  does not change `CURRENT-RESEARCH.yaml`.
- **Bounded question:** does the graviton-noise power/correlation packet expose
  ordered quantum response, or only a classically realizable commutative
  record?
- **Perspective / status:** the quantum field, detector, and interaction are
  ontic within the candidate model; the acquired arm record is epistemic
  evidence; field and direct/stochastic ontologies remain rival descriptions.
- **Lanes / channels:** Lane 1 with Lanes 2, 3, 4, 6, and 7 support;
  `CH-FORMAL`, `CH-MODEL`, `CH-COLLIDE`, and `CH-EMPIRICAL`.
- **Maximum grade:** scoped Grade 4. Grade 5 would require a finite source-pinned
  statistic outside the complete admitted classical/direct rival family.
- **Strongest absorber:** Feynman--Vernon/Hubbard--Stratonovich reduction,
  stochastic gravity, Gaussian-process realization, and classical detector
  theory.
- **Cheapest kill:** an explicit classical stochastic process with the same
  complete arm-record law.
- **Hardware:** unavailable and unnecessary. The decision is reached from the
  primary equations and one exact finite covariance fixture.

## Primary object reconstructed

The audited source is:

- Maulik Parikh, Frank Wilczek, and George Zahariade, *Signatures of the
  Quantization of Gravity at Gravitational Wave Detectors*,
  [arXiv:2010.08208](https://arxiv.org/abs/2010.08208),
  *Physical Review D* **104**, 046021 (2021).

The model first calculates an exact transition probability for a quantum arm
coordinate after tracing over the final gravitational-field state. Its
influence phase has a real fluctuation kernel and an imaginary dissipative
kernel. For the vacuum, the symmetrized kernel is

\[
A_0(t,t')=\frac{4\hbar G}{\pi}
\int_0^\infty d\omega\,\omega
\cos\!\left(\omega(t-t')\right).
\]

The source then applies the Feynman--Vernon Gaussian identity, introducing a
real stochastic function $\mathcal N_0$ with

\[
\mathbb E[\mathcal N_0(t)]=0,
\qquad
\mathbb E[\mathcal N_0(t)\mathcal N_0(t')]=A_0(t,t').
\]

Its power spectrum is displayed as

\[
S_0(\omega)=4G\hbar |\omega|,
\]

where the absolute value makes explicit the even continuation required for a
real stationary covariance. Thermal and squeezed states add state-dependent
Gaussian kernels. A nearby second detector couples to the same stochastic
function, producing shared noise.

To obtain the quoted detector equation, the source takes the macroscopic arm
to a saddle and makes the simplifying equal-path ansatz $\xi=\xi'$. The result
is a classical Langevin-like equation with a fifth-derivative radiation
reaction term. For phenomenological estimates the radiation-reaction term is
then dropped and the arm response is linearized:

\[
\xi(t)\simeq\xi_0
\left(1+\frac12\left(\bar h(t)+\mathcal N(t)\right)\right).
\]

The recommended observables are consequently statistics of a classical
stochastic arm record.

## The commutative Gaussian-record theorem

### Statement

Let $R=(R_1,\ldots,R_n)$ be a finite set of jointly accessible commuting
record values. Suppose its complete characteristic function is Gaussian,

\[
\Phi_R(k)=
\exp\!\left(ik^T\mu-\frac12 k^TCk\right),
\qquad C\succeq0.
\]

Then there exists an ordinary classical Gaussian vector $X\sim N(\mu,C)$
with the same complete law. For every measurable record statistic $f$,

\[
f(R)\overset{d}=f(X).
\]

The conclusion persists for multiple detectors, nonstationary covariance,
and deterministic classical dynamics or post-processing driven by the
record. Therefore no hypothesis test measurable only on that record can
identify whether its Gaussian covariance originated in a noncommuting
operator field.

### Proof

Positive semidefiniteness of $C$ makes the displayed function the
characteristic function of a classical Gaussian probability measure. Equality
of characteristic functions gives equality of joint laws. Measurable
pushforward preserves equality of laws. Multi-detector and nonstationary cases
merely enlarge the finite covariance matrix. QED.

The theorem is standard Gaussian probability applied to a typed physical
record. DU's contribution is the attribution stop: a quantum derivation of
$C$ does not make quantization identifiable from a record whose full law
factors through $C$.

## Exact collision with the proposed signatures

### Vacuum power

The vacuum spectrum's dependence on $G$, $\hbar$, and $|\omega|$ is a
source-derived formula, but a single classical stochastic law can use the
same covariance at every frequency without post-result refitting. A physical
constant appearing in a fitted or stipulated classical covariance does not
identify the ontology that generated it.

This statement is stronger than “mundane detector noise may look similar.” It
is exact equality of the complete idealized record law.

### Thermal and squeezed kernels

For one squeezed mode and zero squeeze angle, the total symmetrized kernel has
the form

\[
\begin{aligned}
A_r(t,t')=a\big[&\cosh(2r)\cos\omega(t-t')\\
&-\sinh(2r)\cos\omega(t+t')\big].
\end{aligned}
\]

It factors exactly as

\[
A_r(t,t')=a\left[
e^{-2r}\cos\omega t\cos\omega t'
+e^{2r}\sin\omega t\sin\omega t'
\right].
\]

Thus it is the covariance of a classical process with two independent
quadratures of variances $ae^{-2r}$ and $ae^{2r}$. Nonstationarity and
exponential squeezing enhancement do not remove the classical realization.
The same source-parameter map $r\mapsto A_r$ can be installed as one unchanged
classical rival family.

This does not say a squeezed quantum gravitational state is classical. It
says the inspected commuting Gaussian record does not certify what prepared
it.

### Nearby-detector correlation

One shared Gaussian latent process driving two detector arms gives exactly the
proposed cross-correlation. Independent sensor noise can be added on each arm
without changing the common-cause construction. Correlation across detectors
therefore distinguishes independent local noise but not classical shared
stochastic gravity from a quantized field.

### Nonlinear detector output

The absorption is not limited to linear output. Once the candidate has
replaced the field influence by a classical Gaussian drive and the arm by a
classical stochastic equation, any deterministic nonlinear functional of
that drive remains a classical stochastic process. Its output may be
non-Gaussian without becoming a quantum witness.

## What the record erased

For a vacuum oscillator mode, the ordered correlation is schematically

\[
C^>(t,t')=a e^{-i\omega(t-t')}.
\]

The arm-noise record retains its real symmetrized part
$a\cos\omega(t-t')$ and discards the imaginary commutator part. At zero
temperature the ordered positive- and negative-frequency weights are unequal;
a real stationary commuting scalar process has an even spectrum. This is the
same ordered/symmetrized boundary earned abstractly in `HC-DU-193`.

The ordinary interferometer arm record in the inspected phenomenology is not
an energy-selective two-level detector and does not measure those two ordered
weights separately. Its reported power spectrum is explicitly even.

## The quantum-detector reopener

The paper contains a stronger object before classicalization: an exact
transition probability between quantum arm states $|\phi_A\rangle$ and
$|\phi_B\rangle$ after the gravitational field is traced out. The next
admissible question is therefore:

> Does the unchanged pre-saddle detector process, interrogated through at
> least two incompatible or energy-selective instruments, produce a finite
> ordered statistic that no admitted classical stochastic gravitational drive
> can reproduce?

A serious packet must freeze:

1. the gravitational source/state preparation rather than only naming vacuum,
   thermal, or squeezed sectors;
2. the detector's quantum Hilbert space and coupling, including switching and
   finite spatial profile;
3. at least two incompatible preparations/readouts or upward/downward
   transition rates;
4. the complete influence functional before the equal-path saddle;
5. the classical stochastic Hamiltonian/force rival class;
6. a direct quantum action/environment rival;
7. source deletion, detector self-dynamics, radiation reaction, controller,
   and acquisition controls; and
8. one finite no-refit target across at least two frequencies or gaps.

Even a positive return would first certify a noncommuting effective
environment under the frozen coupling. Field identity remains a separate
burden because an endpoint-equivalent direct quantum environment can reproduce
the same detector process unless locality, component access, or provenance
excludes it.

## Absorbers and novelty

- The Feynman--Vernon influence functional and Gaussian auxiliary-noise
  transform are the source's own method, not a DU discovery.
- Stochastic gravity and quantum Brownian motion already organize noise and
  dissipation kernels: [Johnson and Hu](https://arxiv.org/abs/quant-ph/0012137).
- Quantum-noise spectroscopy explains why ordered transition rates require a
  quantum detector rather than a classical power meter:
  [Clerk et al.](https://arxiv.org/abs/0810.4729).
- Classical-output commutativity in gravitational-wave interferometry is a
  known measurement-theory boundary:
  [Braginsky et al.](https://arxiv.org/abs/gr-qc/0109003).

The component facts are mature. The useful DU result is their composition
with the certified-record contract: a source-derived quantum covariance can
be physically meaningful while the selected material record still erases the
very ordering needed to attribute quantization.

## Exact local probe

`tests/du_graviton_noise_commutative_gaussian_record_probe.py` verifies:

- a classical factorization and positivity certificate for the vacuum
  symmetrized kernel;
- equality of the complete Gaussian characteristic functional;
- classical quadrature factorization of squeezed nonstationary kernels across
  three source parameters;
- Wick-moment and nonlinear-postprocessing absorption;
- a classical common-cause realization of two-detector correlation;
- one no-refit classical copy of the complete vacuum power surface; and
- the ordered imaginary component and asymmetric rate target erased by the
  commuting record.

The probe preserves a proof boundary. It does not simulate a detector or
quantum gravity.

## Disposition

Disposition:
`CLASSICAL_ARM_RECORD_ABSORBED_QUANTUM_DETECTOR_PROCESS_REOPENED`.

The Parikh--Wilczek--Zahariade arm-noise surface does not satisfy the
`HC-DU-193` ordered-response reopener in its published classical-record form.
Its exact pre-saddle transition law is the smallest legitimate continuation.
No apparatus or hardware work should begin before that law is tested against
the frozen classical stochastic and direct quantum rivals.

No universal stochastic-gravity no-go, error in the source paper, unique
quantum-gravity witness, observed effect, selected material interface, new DU
law, paper promotion, successor, or later-wave activation is earned.
