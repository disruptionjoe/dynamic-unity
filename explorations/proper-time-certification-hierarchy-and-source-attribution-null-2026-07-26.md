---
title: "Proper-time certification hierarchy and source-attribution null"
status: completed_scoped_result
doc_type: primary_source_collision_exact_channel_theorem_and_research_boundary
created: 2026-07-26
hypothesis_id: HC-DU-039D
run_id: RUN-20260726-183500-proper-time-certification-attribution
authority: "Joe direct chat: Go, proceeding with the fifth large swing of the five-swing Dynamic Unity campaign"
claim_grade: "PRIMARY-SOURCE-PINNED PROPER-TIME EVIDENCE HIERARCHY, HISTORY-RELATIVE CHANNEL CERTIFICATE, AND RESIDUAL MECHANISM-ATTRIBUTION NULL / KNOWN QUANTUM CHANNEL, CONVEXITY, INTERFEROMETRY, AND LOCAL IDENTIFIABILITY MATHEMATICS / NO OBSERVED PROPER-TIME NONCLASSICALITY, ONTOLOGY, NEW LAW, NEW PHYSICS, HARDWARE RESULT, OR PAPER PROMOTION"
run_plan: "../lab/process/runs/RUN-20260726-183500-proper-time-certification-attribution/run-plan.md"
probe: "../tests/du_proper_time_certification_attribution_probe.py"
artifact: "../tests/artifacts/du_proper_time_certification_attribution_result.json"
---

# Proper-time certification hierarchy and source-attribution null

## Result in plain English

The optical-clock literature gives Dynamic Unity a much better physical arena
than the previous abstract two-source phase control, but it does **not** give
one ladder on which every new observable is simply “stronger evidence for
proper time.”

It gives two independent questions:

1. **Is the observed clock process reproducible by classical proper-time
   histories?**
2. **If it is not, does the experiment identify proper time as the physical
   cause of that nonclassical process?**

Those questions can have different answers.

- A mean frequency shift or terminal phase can be reproduced by a
  semiclassical average.
- Even the complete two-level clock coherence, including reduced visibility
  loss, can be reproduced by a classical random distribution of proper times.
- A joint clock-motion experiment can certify entanglement under a frozen
  preparation and measurement contract.
- A conditioned coherent-recombination channel can lie outside the convex
  set of classical mixtures of the **same specified histories**.
- But even complete tomography of that nonclassical channel cannot identify
  whether an operationally identical Hamiltonian arose from proper-time
  coupling, mass-energy coupling, or a matched engineered interaction.

The exact remaining null is therefore not “we need a more precise
measurement of the same output.” It is:

\[
(\delta\theta_\tau,\delta\theta_\chi)=(1,-1),
\]

where \(\theta_\tau\) is the proper-time contribution and
\(\theta_\chi\) is an operationally equivalent coherent-control contribution
to the same total history angle

\[
\theta=\theta_\tau+\theta_\chi.
\]

Every output observable of that frozen channel is blind to exchanging one
contribution for the other.

The minimum repair is an independently calibrated intervention whose
sensitivity is not parallel to \((1,1)\): for example, vary the motional
quantity that the relativistic coupling predicts should matter while the
ordinary control Hamiltonian is frozen. This can identify coefficients of
the operational Hamiltonian. It still cannot experimentally choose between
two mathematically equivalent interpretations of that same Hamiltonian.

The fifth-swing return is therefore:

```text
NONCLASSICAL-HISTORY CERTIFICATION AND PHYSICAL-SOURCE ATTRIBUTION
ARE INDEPENDENT EVIDENCE AXES.
```

That is the useful physical refinement of `HC-DU-039C`.

## What the primary sources actually establish

### Sorci et al. — a published theoretical proposal

Sorci, Foo, Leibfried, Sanner, and Pikovski,
[*Quantum Signatures of Proper Time in Optical Ion
Clocks*](https://arxiv.org/abs/2509.09573), was published in *Physical Review
Letters* in April 2026. It is a theoretical proposal using realistic
trapped-ion-clock parameters, not a report that quantum proper-time effects
have been observed.

For a harmonically trapped clock, their low-energy Hamiltonian is

\[
\hat H
=
\hat H_c
+\hbar\omega\left(\hat n+\frac12\right)
-\frac{\hbar\omega}{2mc^2}\hat H_c\hat P^2.
\]

The last term couples the internal clock to motion. It can entangle the
clock and motional degrees of freedom.

The paper itself makes a source-attribution point that is central here:

> The same Hamiltonian can be interpreted as mass-energy equivalence or as
> proper-time evolution to the stated order.

This is not an experimental ambiguity that additional tomography can solve.
The interpretations name the same mathematical dynamics.

The paper separates several observables:

| Observable | What it responds to | Primary-source ceiling |
|---|---|---|
| ordinary SODS | mean motional kinetic energy | classical proper-time parameter suffices |
| vacuum SODS | quantum ground-state motion | frequency shift still admits a semiclassical average description |
| squeezing SODS | squeezed motional energy distribution | frequency shift alone remains insufficient |
| reduced clock visibility | clock-motion correlation after motion is ignored | proposed as an entanglement signature in the supplied Hamiltonian |
| direct joint clock-motion measurement | nonseparability of the joint state | can test entanglement under a frozen state/instrument model |
| qSODS conditioned phase | interference involving clock-dependent motional dynamics and added controls | not captured by the simple \(\langle\tau\rangle\) model, but a terminal phase statistic is not by itself a complete history-channel certificate |

The crucial distinction is between:

\[
\text{not reproduced by one mean proper time}
\]

and

\[
\text{not reproduced by any admitted classical random-history channel}.
\]

The second claim is stronger.

### Zeng — a recent preprint with an exact finite theorem

Zeng,
[*Certifying Nonclassical Proper-Time Histories with a Quantum
Clock*](https://arxiv.org/abs/2606.12755), is a June 2026 preprint. Its
finite channel statements are simple enough to rederive exactly, and this
swing does so rather than treating the preprint as authority by citation.

It establishes three evidence levels.

#### Level 1 — two-level reduced dephasing is classically simulable

Let a two-level clock coherence transform as

\[
\rho_{ge}\longmapsto\Gamma\rho_{ge},
\qquad |\Gamma|\le 1.
\]

Every such \(\Gamma\) has a classical random-proper-time representation

\[
\Gamma
=
\int d\mu(\tau)e^{-i\omega\tau}.
\]

The reason is exact: the convex hull of the unit phase circle is the unit
disk. If

\[
\Gamma=re^{i\phi},
\]

mix the opposite phases \(e^{i\phi}\) and \(-e^{i\phi}\) with weights
\((1+r)/2\) and \((1-r)/2\).

The same conclusion follows when a self-adjoint motional label
\(\hat\tau\) generates the joint unitary

\[
U=e^{-iH_C\otimes\hat\tau}
\]

from an initially uncorrelated clock-motion state. After motion is traced
out, the clock coherence is the characteristic function of the classical
probability measure induced by the spectral measure of \(\hat\tau\).

Therefore:

> Quantum-generated reduced clock noise can have entirely classical
> clock-only statistics.

This sharpens the older visibility language. A reduction in clock-only
visibility does not, without more structure, certify a nonclassical
proper-time history.

#### Level 2 — freeze a classical set of complete histories

A history

\[
h=(\tau_1,\ldots,\tau_L)
\]

interleaved with known controls \(R_1,\ldots,R_{L-1}\) induces

\[
V_h
=
U_{\tau_L}R_{L-1}U_{\tau_{L-1}}\cdots R_1U_{\tau_1}.
\]

For an independently specified finite set \(\mathcal H\), define

\[
\mathsf{CPTH}(\mathcal H)
=
\operatorname{conv}
\left\{
\rho\mapsto V_h\rho V_h^\dagger:
h\in\mathcal H
\right\}.
\]

This set permits classical uncertainty, postselection, reweighting, and the
known controls already included in the histories. It excludes coherent cross
terms between different histories.

Its meaning is class-relative. If the history set is expanded after seeing
the result to include the observed channel itself, the certificate becomes
tautological. Dynamic Unity therefore imports the set only with a frozen
history/provenance/control receipt.

#### Level 3 — conditioned coherent recombination can leave that set

If a branch register coherently labels histories and is measured in a basis
that erases their identity, a conditioned operation can have

\[
K_m=\sum_{h\in\mathcal H}c_{m,h}V_h.
\]

Suppose

\[
K_m^\dagger K_m=p_mI,
\qquad p_m>0,
\]

so that \(W_m=K_m/\sqrt{p_m}\) is unitary. If

\[
W_m\not\propto V_h
\qquad\text{for every }h\in\mathcal H,
\]

then the conditioned channel is outside
\(\mathsf{CPTH}(\mathcal H)\).

The proof is a rank-one Choi argument. A nonnegative sum of rank-one Choi
projectors has rank one only when every nonzero vector in the sum is
parallel. This is standard quantum-channel convexity, applied to the frozen
proper-time-history set.

The result rules out classical mixtures of those histories. It does not rule
out:

- every imaginable classical protocol;
- histories with different controls;
- a history set expanded after the result;
- an unrelated quantum eraser;
- technical readout bias;
- an operationally identical non-proper-time Hamiltonian; or
- an ontologically different description of the same Hamiltonian.

### Zych et al. — why phase alone was already insufficient

Zych, Costa, Pikovski, and Brukner,
[*Quantum interferometric visibility as a witness of general relativistic
proper time*](https://arxiv.org/abs/1105.4531), emphasized that a
matter-wave phase shift can be reproduced by an effective potential in flat
spacetime. They proposed visibility loss from a clock-path coupling as a
stronger signature.

The 2026 dephasing result narrows the evidential reading:

- the proposed joint dynamics can be genuinely entangling;
- direct joint measurements can test that entanglement;
- but a reduced two-level visibility statistic alone remains inside the
  classical random-time disk.

This is a correction in evidence type, not a refutation of the joint
Hamiltonian calculation.

### Loriani et al. — apparatus geometry is part of the claim

Loriani et al.,
[*Interference of Clocks: A Quantum Twin
Paradox*](https://arxiv.org/abs/1905.09102), showed that closed light-pulse
interferometers without clock transitions are not sensitive to gravitational
time dilation in a linear potential, while a specifically designed
quantum-clock geometry can isolate the desired effect.

Dynamic Unity should retain that as an instrument-selection control:

> “The system contains clocks and paths” is not enough. The complete control
> sequence, transitions, geometry, and held-out observable determine which
> source direction the experiment can see.

## Theorem 1 — the reduced-clock ceiling

For a two-level clock, the complete single-time reduced dephasing channel is
specified by \(\Gamma\) in the unit disk.

For every \(\Gamma\), there exists a two-point classical random-time measure
with the same channel.

Therefore the following do not certify nonclassical proper-time histories by
themselves:

- one mean phase;
- one frequency shift;
- one Ramsey visibility;
- the complete terminal two-level dephasing factor; or
- arbitrarily precise repetition of those same statistics.

This is an exact representation no-go. Precision cannot repair absent
sensitivity.

### Exact control

The probe uses

\[
e^{i\phi}=\frac35+\frac45i,
\qquad r=\frac12.
\]

The classical weights \(3/4\) and \(1/4\) on opposite phases give

\[
\Gamma
=
\frac{3}{10}+\frac25i,
\qquad |\Gamma|=\frac12.
\]

The same clock-only record therefore admits both a quantum-generated
description and an explicit classical random-time description.

## Theorem 2 — the minimum history-relative channel certificate

Use

\[
U_\pm=e^{\mp i\theta Z/2},
\qquad
R
=
\frac1{\sqrt2}
\begin{pmatrix}
1&1\\
1&-1
\end{pmatrix},
\qquad
V_\pm=U_\pm R U_\pm.
\]

Condition on the history-erasing outcomes

\[
K_\pm=\frac12(V_+\pm V_-).
\]

For the bright port,

\[
p_+
=
\frac{1+\cos^2\theta}{2},
\qquad
\langle Z\rangle_+
=
\frac{\cos^2\theta-1}{\cos^2\theta+1}.
\]

Each classical history maps input \(|g\rangle\) to equal populations, so
every convex mixture predicts

\[
\langle Z\rangle_{\mathrm{cl}}=0.
\]

The dark port has

\[
p_-=\frac{\sin^2\theta}{2},
\qquad
\langle Z\rangle_-=1.
\]

The exact control uses

\[
\cos\frac\theta2=\frac35,
\qquad
\sin\frac\theta2=\frac45,
\]

so

\[
\cos\theta=-\frac7{25},
\qquad
\sin\theta=\frac{24}{25}.
\]

It returns

\[
p_+=\frac{337}{625},
\qquad
\langle Z\rangle_+=-\frac{288}{337},
\]

and

\[
p_-=\frac{288}{625},
\qquad
\langle Z\rangle_-=1.
\]

All results are exact.

### Mandatory nulls

| Null | What it prevents |
|---|---|
| \(V_1=V_2\) | erasing two names for one history from being called history certification |
| no intermediate Ramsey control | this terminal population discriminator no longer separates coherent recombination from the specified mixture |
| erased label unrelated to \(V_h\) | ordinary quantum erasure from being relabeled proper-time-history erasure |
| incoherent averaging | convex mixtures from being mistaken for cross-history coherence |
| free-set expansion after the result | the observed channel from being defined into “classical” or “nonclassical” after inspection |
| zero clock, motion, or erasure coherence | a false-negative null from being treated as proof of classicality |

## Theorem 3 — nonclassicality and source attribution are independent

Suppose the complete frozen instrument depends on the total angle

\[
\theta=\theta_\tau+\theta_\chi,
\]

where:

- \(\theta_\tau\) is the coefficient attributed to the relativistic
  clock-motion term; and
- \(\theta_\chi\) is a matched coherent-control contribution.

Every differentiable output statistic has the form

\[
O_j=F_j(\theta_\tau+\theta_\chi).
\]

Its sensitivity row is

\[
\nabla O_j
=
F_j'(\theta)(1,1).
\]

Stacking any number of output observables therefore gives a matrix of rank at
most one. Its kernel contains

\[
\operatorname{span}\{(1,-1)\}.
\]

This remains true for:

- mean phase;
- visibility;
- bright- and dark-port probabilities;
- conditioned population imbalance;
- joint-state expectations;
- any other POVM statistic; and
- complete process tomography.

If the two generators produce the same complete channel, no measurement on
that channel can distinguish their source labels.

At the same time, the conditioned channel may satisfy

\[
\Phi\notin\mathsf{CPTH}(\mathcal H).
\]

Thus:

\[
\text{nonclassical-history certificate}
\centernot\Longrightarrow
\text{proper-time source attribution}.
\]

This is the central `HC-DU-039D` result.

## Minimum source-attribution repair

Another output statistic of the same total channel adds a row parallel to
\((1,1)\) and leaves the rank unchanged.

The minimum repair is an intervention row not parallel to it. In the ideal
two-parameter local model:

\[
S
=
\begin{pmatrix}
1&1\\
1&0
\end{pmatrix}
\]

has full rank.

The second row must be physically and independently calibrated. Candidate
source-pinned variations include:

- change the Fock-branch separation \(\Delta n\);
- change trap frequency \(\Omega\);
- change interrogation time \(t\);
- change clock transition frequency \(\omega_0\);
- vary motional squeezing while freezing clock-control phases; or
- compare a source-on/source-off geometry under the same complete control
  sequence.

The proposed two-history ion scale is

\[
\theta_\tau
\simeq
\frac{\omega_0t\hbar\Omega}{4mc^2}\Delta n.
\]

A useful intervention contract must:

1. fix the ordinary control contribution before the source variation;
2. measure or bound clock, motional, erasure, and readout nuisance channels;
3. forbid run-by-run control refitting;
4. predict a held-out slope or channel change;
5. include a source-disabled or sensitivity-rotated null;
6. transfer across at least one held-out setting; and
7. state whether it identifies an operational coefficient, a Hamiltonian
   term, or an interpretation.

### The interpretation ceiling

Sorci et al. explicitly note that mass-energy coupling and proper-time
evolution are equivalent interpretations of the same Hamiltonian at the
declared order.

No experiment can distinguish two descriptions that make exactly the same
complete operational predictions. A full-rank sensitivity audit can
attribute a coefficient to the relativistic clock-motion term. It cannot
turn an interpretation choice into an observable fact.

Dynamic Unity must therefore keep:

\[
\text{operational source coefficient}
\ne
\text{unique ontology}.
\]

## The two-axis evidence surface

| Formed record | Classical-history verdict | Source-attribution verdict |
|---|---|---|
| mean frequency or terminal phase | classically/semiclassically reproducible | not identified |
| complete single-time clock coherence | classical random-time representation always exists for a two-level clock | not identified |
| joint clock-motion state | can certify entanglement under frozen preparation and measurement | generator still requires calibration |
| conditioned channel outside \(\mathsf{CPTH}(\mathcal H)\) | excludes classical mixtures of the same frozen histories | operationally identical generators remain |
| complete output process tomography | classifies membership relative to a declared process set | identical source channels remain indistinguishable |
| process plus source-selective intervention | nonclassicality remains a separate verdict | local operational coefficients can become identifiable at full rank |

This surface is more useful than calling one observable “the quantum proper
time signal.” It tells future agents what each record can and cannot earn.

## Nuisance and provenance ledger

| Quantity | Type | If omitted |
|---|---|---|
| \(\eta_h\) | history-erasure fidelity | ordinary erasure/readout loss can suppress or bias the conditioned witness |
| \(\eta_c\) | clock coherence | laser noise or clock dephasing can imitate reduced contrast |
| \(\eta_m\) | motional-branch coherence | heating and trap noise can erase cross-history terms |
| readout offset | detector calibration | a nonzero population imbalance can be manufactured |
| \(\Delta\langle p^2\rangle\) or \(\Delta n\) | proper-time-history label receipt | an unrelated branch label can be mistaken for a proper-time label |
| \(R_j\) controls | complete history definition | a changed control sequence can change the free set and the witness |
| \(\mathcal H\) | rival/classical history set | broadening or weakening rivals after the result invalidates the certificate |
| postselection probability | resource and selection receipt | a high-contrast rare port can be reported without its shot cost |
| reset and preparation | occurrence identity | apparent transfer may be refitting or a new process |

The simple phenomenological product

\[
\eta_{\mathrm{tot}}=\eta_h\eta_c\eta_m
\]

is useful for visibility budgeting, but it does not identify which nuisance
failed. Product fitting must not replace separate calibration receipts.

## What this changes in Dynamic Unity

### 1. `HC-DU-039C` is physically instantiated, but not closed

The previous abstract rank result said that one total phase does not identify
its sources. The optical-clock literature now provides a real hierarchy of
formed records and a source-pinned next intervention.

The physical result is still a boundary:

- nonclassical-history certification can be exact relative to
  \(\mathcal H\);
- proper-time source attribution remains open without a second sensitivity;
- ontology remains open even after operational coefficient attribution.

### 2. Reduced visibility is demoted as a standalone certificate

Agents should not repeat the older shorthand that clock-only visibility loss
by itself certifies nonclassical proper-time histories. It may be generated
by entangling dynamics, but the reduced two-level channel has a classical
random-time representation.

Direct joint entanglement measurements and conditioned history-channel
witnesses are stronger, differently typed records.

### 3. qSODS needs its complete instrument, not just its phase

The qSODS proposal uses conditioned motional projection and additional
clock-state-dependent operations to expose a term not captured by the simple
mean-\(\tau\) model.

The terminal phase alone remains a point in the two-level dephasing disk.
Before Dynamic Unity credits qSODS as history certification, it must retain:

- the complete conditioned instrument;
- its specified classical history set;
- the motional-label provenance;
- its Choi or witness nonmembership test; and
- its nuisance and success-probability ledger.

### 4. The program now has a precise external-hardware boundary

No hardware is needed to earn the present result. The theorem, absorbers,
null direction, and minimum intervention type are all decidable locally.

External hardware would become relevant only after a concrete platform
contract supplies:

- independently calibrated source variation;
- complete operations and readouts;
- nuisance bounds;
- a no-refitting transfer test; and
- a predicted margin that existing data cannot already decide.

At that point hardware would test an explicit operational coefficient or
channel-membership prediction. Until then, provider work would add machinery
without adding knowledge.

## Exact executable result

The deterministic probe
[`du_proper_time_certification_attribution_probe.py`](../tests/du_proper_time_certification_attribution_probe.py)
passes `36/36` checks.

It independently verifies:

- an exact classical two-point decomposition of an interior clock coherence;
- the two-history Ramsey unitaries;
- exact bright- and dark-port probabilities and conditioned populations;
- the Choi-ray separation criterion;
- identical-history, removed-control, unrelated-label, incoherent-average,
  free-set-broadening, and coherence-loss nulls;
- a nuisance-attenuated nonzero witness;
- rank one for every output-only sensitivity to
  \(\theta_\tau+\theta_\chi\);
- the exact local null \((1,-1)\);
- failure of another same-channel output to repair attribution;
- full-rank repair by one source-selective intervention row; and
- indistinguishability of operationally identical source mechanisms under
  complete output tomography.

The executable is a regression after proof. It is not a clock simulation or
an experimental result.

## Novelty collision

The mathematical components are known:

- convex hull of the unit circle;
- characteristic functions of probability measures;
- quantum channels and Choi operators;
- rank-one mixture geometry;
- Ramsey interferometry;
- quantum erasure;
- entanglement witnesses;
- local Jacobian rank; and
- structural identifiability.

The 2026 preprint already states the reduced-dephasing no-go and
history-relative Choi certificate.

Dynamic Unity's useful contribution in this swing is the typed composition:

> Evidence for nonclassical histories, evidence for a particular physical
> generator, and evidence for an ontology are three different reconstruction
> problems.

That synthesis is research infrastructure and a precise North-Star boundary.
It is not presently promoted as new mathematics, new physics, or a paper.

## North-Star return

The result supports the North Star in a constrained way.

### Record-first success

A complete conditioned record can establish that an operation lies outside
a frozen classical-history set.

### Operational duality

A quantum-generated reduced clock channel and a classical random-time model
can be record-equivalent.

### Physics-first remainder

Coherent cross-history terms can create a finite separating operation not
available to the specified classical mixture.

### Remaining underidentification

The same separating channel can be generated by operationally identical
Hamiltonians with different source labels or interpretations.

### Nontrivial success rule

Future claims must report three receipts separately:

1. **history nonclassicality:** nonmembership in a frozen classical process
   set;
2. **source attribution:** full-rank preregistered intervention sensitivity;
3. **ontology:** an empirically distinct prediction, not a renamed
   Hamiltonian.

## Highest-information next dependency

Do not build another channel toy and do not open hardware access.

The next useful local action is to write one concrete source-selective
intervention contract from the published trapped-ion equations:

1. select one variation, preferably \(\Delta n\) or \(\Omega\);
2. derive the full sensitivity of phase, visibility, bright/dark ports, and
   nuisance parameters;
3. identify the exact rank after all calibrated controls are included;
4. construct the smallest matched coherent-control model that could mimic
   the same slope;
5. name the minimum held-out setting that separates it without refitting; and
6. stop if the remaining distinction is only between equivalent
   interpretations of one Hamiltonian.

That calculation can tell us whether there is a genuinely source-selective
proper-time experiment worth escalating, or whether the whole branch is
absorbed by standard metrology plus channel certification.

## Claim ceiling

This result earns:

- a primary-source-pinned proper-time evidence hierarchy;
- an independently rederived, history-relative channel certificate;
- an exact residual mechanism-attribution null;
- a minimum source-selective intervention requirement; and
- a precise local-versus-hardware boundary.

It does not earn:

- an observed quantum proper-time effect;
- proof that records create physical reality;
- a unique physical source from one channel;
- a unique interpretation of the relativistic Hamiltonian;
- a universal exclusion of classical protocols;
- a selected observer, archive, or finality rule;
- a new law or new physics;
- paper promotion; or
- authorization for hardware, provider work, contact, submission, or
  publication.
