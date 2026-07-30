---
title: Non-Markovian collapse/Bohmian stable-covariant realization boundary
date: 2026-07-30
claim_id: HC-DU-145
evidence_grade: 4
status: banked_scoped_result
programs:
  - CCR-PHYSICAL-RELIABILITY-RECONSTRUCTION-FLOOR
  - CCR-PREDICTIVE-SELECTION-TO-FORECASTING-ISSUANCE
---

# Non-Markovian collapse/Bohmian stable-covariant realization boundary

## Result

`HC-DU-144` moved the first possible difference between the matched
non-Markovian collapse and Bohmian-bath descriptions outside their common
system process. The next question was whether stability, covariance, or
resource matching turns that formal difference into a finite physical
remainder.

It does not do so automatically.

> The literal Tilloy--Wiseman oscillator realization has an exact
> fixed-class stability obstruction: every nontrivial even coupling to paired
> positive and negative frequency modes puts negative one-particle energy in
> a bosonic Fock space, so the bath Hamiltonian is unbounded below. A
> bounded-below laboratory repair must restrict the frequency support and
> introduce a carrier, reference, boundary, truncation, or different
> field/unravelling. That repair is a new physical packet whose pathwise
> correspondence must be proved again.

At the broader operational level, covariance does not force a discriminator.
Tilloy's Lorentz-invariant statistical-field reformulation of a regularized
interacting QFT is constructed to retain orthodox QFT measurement statistics.
It therefore supplies a strong representation-level absorber: a
non-Markovian, collapse-like local-beable description can be covariant and
operationally equivalent to an orthodox field theory. It is not the same
pathwise real-noise/Bohmian bath construction, and its localization analysis
is explicitly partial.

The honest disposition is consequently two-level:

1. **fixed pathwise class:** nontrivial exact realization is not
   bounded below;
2. **broader stable/covariant class:** operational equivalence remains
   available, but only after changing the beables, coupling, regulator, or
   boundary contract.

This is a realization and typing boundary. It is not a finite
observer-accessible empirical remainder, a universal collapse no-go, an
ontology choice, or new physics.

## Claim and grade

`HC-DU-145` earns **scoped Grade 4** for:

1. an exact spectral obstruction within the literal paired-frequency
   Tilloy--Wiseman Fock-bath class;
2. an exact identification of band limitation as a necessary restriction
   for the bounded-below repair described by the source;
3. separation of pathwise equivalence from operational QFT equivalence;
4. a resource and contract audit of the available repairs;
5. the finding that stability and covariance restrict or retype the
   realization without themselves generating empirical excess; and
6. the forecasting consequence that the bounded-band histories considered
   by the source are analytic and arbitrarily finitely forecastable, without
   thereby becoming exactly reconstructible from a finite-precision record.

The spectral lemma is elementary second quantization applied to the published
Hamiltonian. Tilloy and Wiseman themselves flag both the lack of a lower
bound and the band-limited consequence of a physical repair. DU's increment
is the typed composition with process, record, resource, and issuance
questions. Novelty is therefore low. No Grade-5 physical remainder, paper
claim, or physical law is earned.

## Frozen exact realization

The Tilloy--Wiseman construction uses

\[
H_B=\sum_k\int_{\mathbb R}d\omega\,
     \omega\,a^\dagger_{k,\omega}a_{k,\omega}
\]

with real even couplings

\[
\kappa^\ell_{k,\omega}=\kappa^\ell_{k,-\omega}.
\]

The interaction is linear in the bath momenta. The paired modes support
commuting quadratures \(x^+_{k,\omega}\) and \(x^-_{k,\omega}\), and the
kernel is

\[
D_{jk}(t,s)
=
\sum_\ell\int_0^\infty d\omega\,
\kappa^\ell_{j,\omega}\kappa^\ell_{k,\omega}
\cos\!\bigl(\omega(t-s)\bigr).
\]

With the source's chosen bath variables, the conditioned Bohmian
wavefunction and redefined collapse noise agree pathwise. This exact packet
includes:

- the full bosonic Fock space;
- the signed-frequency multiplication operator;
- the even coupling;
- the mixed-frequency Bohmian quadratures;
- the Fock vacuum;
- the system--bath boundary; and
- the fixed noise map.

Changing any of these may produce a good physical model. It does not
automatically preserve the same pathwise theorem.

Primary source:

- Antoine Tilloy and Howard M. Wiseman, “Non-Markovian wave-function collapse
  models are Bohmian-like theories in disguise,” *Quantum* **5**, 594
  (2021), [arXiv:2105.06115](https://arxiv.org/abs/2105.06115).

## Fixed-class paired-frequency stability obstruction

### Lemma

Let

\[
\mathcal F_B=\Gamma_s\!\left(L^2(\mathbb R,d\omega)\otimes\mathbb C^d\right)
\]

be the full symmetric Fock space and let

\[
H_B=d\Gamma(M_\omega)
\]

be second quantization of multiplication by \(\omega\). If a normalized
one-particle wavepacket \(f\) has support in a negative-frequency region and

\[
\epsilon_f=\langle f,M_\omega f\rangle<0,
\]

then

\[
\inf\operatorname{spec}(H_B)=-\infty.
\]

### Proof

Put \(n\) bosons in the normalized mode \(f\). The corresponding Fock state
has energy

\[
\langle H_B\rangle_n=n\epsilon_f.
\]

Since \(\epsilon_f<0\), this tends to \(-\infty\) as \(n\to\infty\).

If an ordinary square-integrable coupling has nonzero support at positive
frequency, evenness supplies the corresponding negative-frequency support.
Thus the literal nontrivial paired-frequency realization contains such an
\(f\). A distribution supported only at \(\omega=0\) is outside the generic
colored-noise class and does not repair it.

### Scope

The lemma proves only:

```text
literal signed-frequency Hamiltonian
+ full bosonic Fock occupation
+ nontrivial even coupling
=> no lower energy bound
```

It does not prove that no stable dilation of the same reduced system process
exists. It proves that a stable dilation cannot retain every element of the
literal realization packet unchanged.

## What a bounded-below repair buys and changes

Tilloy and Wiseman state that a bounded-below physical bath forces the noise
in their paired-frequency construction to be band-limited. A standard
physical reading is that signed frequencies become detunings around a
positive carrier. A finite carrier can accommodate
\(\omega\in[-\Omega,\Omega]\), but not an unbounded signed spectrum.

Such a repair can be physically reasonable, yet it introduces at least one
of:

- a finite spectral cutoff;
- a carrier oscillator or rotating frame;
- a clock, pump, phase reference, or explicitly time-dependent control;
- a restricted initial sector or occupation cutoff;
- nonlinear stabilizing terms; or
- a different bath field and Bohmian variable.

These are resources and boundary data, not harmless changes of notation.
They can change the allowed kernel, the primitive record path, or both. An
exact repaired pathwise theorem must therefore specify the laboratory
Hamiltonian, state sector, reference resource, approximation error, and
readout/access contract.

### Analyticity is forecasting, not a finite exact certificate

For the band-limited case, the source observes that the wavefunction
evolution is analytic and that a value at finite future time can be predicted
to arbitrary accuracy from finitely many derivatives.

This matters for Dynamic Unity:

- imposing physical stability does not make progressive stochastic issuance
  easier to identify;
- in this class it instead makes the future increasingly disclosure-like
  from a sufficiently rich Cauchy-surface state.

But “arbitrary accuracy” is not exact finite reconstruction. The required
derivative order grows with horizon and accuracy, while derivative values
must themselves be known with adequate precision. No finite
observer-accessible certificate of the complete future follows.

## Covariant-QFT absorber

Tilloy earlier reformulated a regularized interacting fermion--boson QFT as a
Lorentz-invariant statistical field theory of a complex random local-beable
field:

- Antoine Tilloy, “Interacting quantum field theories as relativistic
  statistical field theories of local beables,”
  [arXiv:1702.06325](https://arxiv.org/abs/1702.06325).

The probability measure is built from the QFT influence functional and a
Girsanov-type reweighting. The intended empirical content is the same as
orthodox interacting QFT. Consequently:

> Lorentz covariance plus a collapse-like statistical-field ontology does
> not by itself force empirical excess over standard QFT.

This is a strong absorber, but not the missing exact repair:

| Tilloy--Wiseman pathwise packet | Tilloy covariant-QFT packet |
|---|---|
| real colored noise | complex Gaussian field |
| mixed positive/negative-frequency quadratures | spacetime local-beable field |
| momentum-quadrature coupling | QFT source/field coupling |
| exact conditioned-wavefunction equality | influence-functional statistical rewriting |
| literal bath Hamiltonian unbounded below | covariantly regularized QFT construction |
| exact generic non-Markovian path theorem | localization analysis under restrictive assumptions |

The QFT paper explicitly describes its regularized treatment as naive at the
current stage and its realistic collapse calculation as a hint rather than a
rigorous proof. It shows representation-level covariance and empirical
absorption, not a nonperturbative stable Hamiltonian theorem selecting a
unique local-beable field, record, archive, or observer boundary.

Tilloy and Wiseman also discuss using the electromagnetic field as the bath.
They explicitly note that this is not precisely their construction: the
beables are vector-potential modes rather than their mixed-frequency
quadratures, the coupling uses the vector potential rather than its conjugate
momenta, and the matter operators are not the assumed local collapse
operators. They call the structural analogy plausible, not proved.

## Markovian comparator does not transfer

Myrvold proves that, under relativistic causality and stable-vacuum
assumptions, a relativistically invariant **Markovian** stochastic collapse
theory built only from standard QFT degrees of freedom has deterministic
evolution:

- Wayne C. Myrvold, “Relativistically Invariant Markovian Dynamical Collapse
  Theories Must Employ Nonstandard Degrees of Freedom,” *Physical Review A*
  **96**, 062116 (2017),
  [arXiv:1709.03219](https://arxiv.org/abs/1709.03219).

This is a useful typed comparator. It does not prove a no-go for the
non-Markovian Tilloy--Wiseman class. Conversely, the non-Markovian
correspondence does not refute Myrvold's Markovian theorem. Moving to the
white-noise limit requires a continuously infinite bath and is a singular
class transition in the source construction.

## Resource and contract audit

| Candidate realization | Exact path map? | Lower bound? | Covariance? | Added or changed structure | DU disposition |
|---|---:|---:|---:|---|---|
| Literal signed-frequency Fock bath | yes | no | not established | full \(\mathbb R\) spectrum and mixed quadratures | fixed-class obstruction |
| Finite-band carrier/rotating-frame bath | not yet proved | potentially | model-dependent | cutoff, carrier, reference/pump, approximation contract | restricted retyped packet |
| Positive-energy QED/EM bath | not the same map | expected in physical sector | yes at operational theory level | gauge field, different beables/coupling/operators | plausible distinct construction |
| Lorentz-invariant statistical QFT field | operational rewriting | formal/regularized | yes at measure level | complex field, regulator, boundary measure | strong operational absorber |
| Markovian white-noise limit | singular limit | not supplied by finite bath | separate problem | continuous infinity/nonstandard degrees | class exit |
| Late-boundary/all-at-once beables | different map | model-dependent | potentially | future boundary and non-Cauchy ontology | causal-contract retyping |

No resource comparison is meaningful until both sides inhabit one frozen
physical packet. The literal bath's unbounded negative-energy capacity is not
a legitimate free resource. A carrier, cutoff, regulator, field sector, pump,
or final boundary must be charged explicitly on a repaired side.

## Discriminator audit

### System-side operations

Closed by `HC-DU-144` once a common process completion is supplied.

### Direct bath or beable access

Can distinguish realization variables, but changes the observer-access
boundary and exits the system-side comparison. It is not a same-packet
empirical remainder.

### Energy instability

Rejects the literal realization as a fundamental physical model. It does not
make the stochastic description and a stable repaired completion issue
different predictions on one shared arena.

### Band limitation

Restricts the class of admissible kernels. A collapse model with spectral
support beyond the chosen band is not realized by that repaired bath. This is
model-class exclusion, not a measurement outcome on two co-admitted models.

### Lorentz violation

A chosen bath that leaks a preferred frame can be tested. Lorentz leakage is
not forced by the non-Markovian process: the covariant-QFT rewriting is the
counterexample at representation grade. A concrete leakage coefficient must
be selected before there is a prediction.

### Covariant regularization

The regulator is an admitted physical input in the covariant statistical
field proposal. Until it is selected and transferred without refitting, it
does not yield a unique finite prediction.

## Smallest exact boundary

The result can be stated compactly:

> **Paired-frequency stability boundary.** Within the literal
> Tilloy--Wiseman Fock-bath realization, any ordinary nonzero even coupling
> supporting the exact mixed-frequency path map makes the bath Hamiltonian
> unbounded below. A bounded-below realization must restrict the spectrum or
> change the physical realization. Such restriction does not by itself yield
> empirical excess, because covariant non-Markovian statistical-field
> rewritings can retain orthodox QFT statistics.

The boundary prevents two opposite errors:

1. treating the published exact dilation as already a stable fundamental
   physical implementation; and
2. treating the failure of that implementation as evidence that collapse and
   deterministic-completion descriptions must be empirically separable.

## Plain-English meaning

The exact correspondence was built with a mathematical bath that contains
oscillators whose energy can keep falling without limit. That is acceptable
for proving a representation theorem, but not as a complete physical world.

Making the bath physical is not impossible. It means choosing a finite band,
a carrier or real field, a regulator, and a particular way to read that field.
Those choices narrow or change the model. They do not reveal which ontology
was “really there,” and they do not automatically create a new experimental
signal. In fact, existing QFT work shows that a covariant collapse-like
description can be arranged to have the same ordinary predictions.

The most interesting consequence is about issuance. In the stable
band-limited version, the supposedly fresh stochastic future becomes
analytic and increasingly forecastable from present data. Stability pushes
this example toward hidden disclosure rather than supplying evidence for
genuine source issuance.

## Reopener and stop

A legitimate reopener must supply one of:

1. an explicit bounded-below, covariant Hamiltonian and primitive-variable
   construction preserving the same non-Markovian path map, with a complete
   approximation and resource theorem;
2. two co-admitted stable/covariant realizations making different finite
   predictions under one frozen system--instrument--archive--access contract;
3. an action- or symmetry-selected local-beable field that also selects
   formation, single-run actualization, retained provenance, observer access,
   and a held-out target without refitting; or
4. a proof that every stable/covariant realization of a declared kernel class
   has one finite observer-accessible remainder.

Generic searches for another bath, another unravelling, or another
collapse/interpretation label should stop. `HC-DU-142` already proves that
unconditional dynamics does not select a unique trajectory record, and
`HC-DU-144` closes ordinary system-side controls once one process is supplied.
Without one of the reopeners above, there is no ready scientific successor.

## Non-promotions

This result does **not** establish:

- a universal no-go on stable collapse dilations;
- a rigorous nonperturbative construction of the covariant statistical QFT;
- a unique physical ontology;
- exact future reconstruction from finitely many noisy records;
- a preferred foliation or its absence;
- a selected record, archive, access boundary, or capacity;
- empirical excess over quantum theory or QFT;
- new physics;
- a hardware need; or
- a paper promotion.
