---
title: "Record formation to certified composition: proper-time interface theorem and no-go"
status: completed_scoped_result
doc_type: theorem_no_go_and_physical_dependency
created: 2026-07-25
authority: "Joe direct chat: orchestrate the record-formation to certified-composition wave"
claim_grade: "EXACT FINITE EFFECTIVE-INSTRUMENT RESULT / COMPONENT MATHEMATICS KNOWN / PHYSICAL PROPER-TIME IMPLEMENTATION INCOMPLETE / NEW DU DEPENDENCY RESULT / NO NOVEL-PHYSICS PROMOTION"
run_plan: "system-runtime#meta/runs/history/repositories/dynamic-unity/lab/process/runs/RUN-20260725-100452-record-formation-certified-composition/run-plan.md"
probe: "../tests/du_record_formation_composition_probe.py"
artifact: "../tests/artifacts/du_record_formation_composition_result.json"
---

# Record formation to certified composition

## Result in plain English

The proper-time coupling and the proper-time certificate select different
things.

In the frozen two-history clock--motion process below, the interaction itself
selects a two-sector **nondemolition history algebra**: the distinction between
the two proper-time branches is the only nontrivial motion distinction that
commutes with the complete coupling. This is a positive interface-selection
result, but only for a *candidate history label*.

It still does not create a record. A continuum of different motion readouts
can be placed after exactly the same coupling. They all give the same
unconditioned clock channel, but their outcome-conditioned clock operations
are different. One readout reveals which history; another coherently erases
that distinction and certifies interference between the histories. The
coupling does not choose between them.

The coherent-erasure readout yields a particularly useful exact distinction:

> A durable port/clock record can certify that the selected operation is not
> an arbitrary classical mixture of the same two specified histories while
> disclosing no run-level history in the frozen symmetric fixture.

That statement separates four objects that Dynamic Unity had sometimes held
too close together:

```text
latent history label
    != selected erasure instrument
    != formed certificate record
    != proposition certified by the record.
```

The result is fully contained in standard quantum instrument and quantum
eraser mathematics. Its value for Dynamic Unity is a dependency correction:
**history certification does not require history disclosure, and a
certificate-forming interface need not be the stable history interface
selected by the source coupling.** The coherent erasure instrument, physical
archive, access algebra, durability rule, uncertainty model, and resource
contract remain additional structure.

The current primary sources do not support an honest
implementation-complete proper-time instrument. Sorci et al. derive a
clock--motion Hamiltonian and experimentally motivated signatures, including
clock--motion entanglement, but not the complete durable
history-erasure/archive instrument required here
([PRL](https://doi.org/10.1103/qhj9-pc2b);
[arXiv](https://arxiv.org/abs/2509.09573)). Zeng supplies a two-history
selective-erasure certification protocol and explicitly limits it to
classical mixtures of the specified histories, but it remains a theoretical
preprint and does not freeze the full SPAM, drift, leakage, archive, and
resource contract
([arXiv](https://arxiv.org/abs/2606.12755)).

The executed product is therefore an exact finite effective-instrument
theorem and interface-necessity no-go, not laboratory proper-time
certification.

## The four typed objects

| Object | Frozen meaning here | What it is not |
|---|---|---|
| Latent history label \(h\) | Spectral sector of the two-valued effective proper-time operator on motion | A recorded classical trajectory or a claim that one branch “really occurred” |
| Selected erasure instrument | Complementary motion readout with Kraus maps \(K_\pm=(V_0\pm V_1)/2\) | Something selected by the source coupling or by stability |
| Formed certificate record \(C=(S,X)\) | Classical port sign, clock-\(X\) result, setting/provenance, and validity record after the supplied readout/archive | The history label \(h\), public finality, or an unmodeled observer |
| Certified proposition | The selected operation is outside arbitrary-weight classical mixtures of the same two frozen history operations | Exclusion of arbitrary classical protocols, proof of one run's history, or beyond-quantum physics |

The classical archive is treated as formed only after the selected
measurement coupling. The probe does not derive the archive's amplification,
durability, or public accessibility.

## Frozen effective contract

The finite fixture is deliberately small enough for an exact analytic
result.

### Systems and preparation

- Motion/history system \(M\): one qubit with supplied orthogonal history
  sectors \(P_0=|0\rangle\langle0|\) and
  \(P_1=|1\rangle\langle1|\).
- Clock \(C\): one qubit with \(Z_C\) as its energy direction.
- Motion input:
  \(|+\rangle_M=(|0\rangle+|1\rangle)/\sqrt2\).
- Clock input:
  \(|+\rangle_C=(|0\rangle+|1\rangle)/\sqrt2\), the \(+1\)
  eigenstate of \(X_C\).

### Proper-time history operations

Freeze the symmetric relative phase

\[
V_0=e^{-i\pi Z_C/4},
\qquad
V_1=e^{+i\pi Z_C/4},
\]

and the joint controlled evolution

\[
U_{MC}
=P_0\otimes V_0+P_1\otimes V_1.
\]

This is the finite two-history specialization of a coupling
\(e^{-iH_C\otimes\hat\tau}\). It preserves the physically relevant fact that
different motional proper-time sectors enact different clock phases. It does
not reproduce the harmonic oscillator, squeezing protocol, relativistic
small parameters, trap controls, or noise model of the optical-ion proposal.

### Admitted readouts

The motion readout basis is parameterized by

\[
\begin{aligned}
|r_0(\alpha)\rangle
  &=\cos\alpha\,|0\rangle+\sin\alpha\,|1\rangle,\\
|r_1(\alpha)\rangle
  &=-\sin\alpha\,|0\rangle+\cos\alpha\,|1\rangle .
\end{aligned}
\]

It produces selective clock operators

\[
\begin{aligned}
K_0^{(\alpha)}
  &=\frac{\cos\alpha\,V_0+\sin\alpha\,V_1}{\sqrt2},\\
K_1^{(\alpha)}
  &=\frac{-\sin\alpha\,V_0+\cos\alpha\,V_1}{\sqrt2}.
\end{aligned}
\]

Two named interfaces are frozen:

- \(\alpha=0\): which-history readout;
- \(\alpha=\pi/4\): coherent history-erasure readout.

After the erasure readout, the clock is measured in \(X_C\). The ideal
archive stores the port sign \(S\in\{+1,-1\}\), clock sign
\(X\in\{+1,-1\}\), setting, provenance, and valid-trial flag.

### Alternative and null

The alternative is the equal-amplitude coherent process under \(U_{MC}\)
followed by the frozen erasure instrument.

The null is every arbitrary-weight incoherent mixture of the **same two**
history operations:

\[
\rho_{\mathrm{null}}(q)
=q\,P_0\otimes V_0\rho V_0^\dagger
+ (1-q)\,P_1\otimes V_1\rho V_1^\dagger,
\qquad 0\leq q\leq1.
\]

It does not include different history operations, additional controls,
detector leakage, or an arbitrary classical simulator. That limitation is
load-bearing.

### Resource and uncertainty boundary

The exact fixture charges:

- one motion qubit and one clock qubit per coherent trial;
- coherent preservation of the motion label through erasure;
- one selected two-outcome motion readout;
- one clock-\(X\) readout;
- two classical outcome bits plus setting/provenance/validity storage; and
- \(N\) independent repetitions for a statistical certificate.

SPAM, motional leakage, finite temperature, phase drift, detector confusion,
archive failure, correlated trials, coherence lifetime, energy, latency, and
trap-control cost are **excluded**, not silently set to zero as empirical
facts. Their omission is why this is not implementation-complete.

## Theorem 1 — interaction-selected history algebra

Let

\[
U=P_0\otimes V_0+P_1\otimes V_1
\]

on \(\mathbb C^2_M\otimes\mathcal H_C\), with \(V_0\) and \(V_1\)
distinct as operators. Then the motion algebra commuting with the complete
interaction is

\[
\mathcal A_H
=\{A_M:[A_M\otimes I_C,U]=0\}
=\operatorname{span}\{P_0,P_1\}
=C^*(\hat\tau).
\]

Thus the coupling selects the two-sector nondemolition history algebra.

### Proof

Write \(A_M=(a_{ij})\) in the \(P_0,P_1\) basis. The \(ij\) block of the
commutator is

\[
a_{ij}(V_j-V_i).
\]

The diagonal blocks vanish. Because the two branch operations are distinct,
the off-diagonal blocks vanish only when \(a_{01}=a_{10}=0\). Therefore the
commutant consists exactly of diagonal motion operators. \(\square\)

### Scope

This is an interaction-relative QND selection result, not formation of a
classical record. The two-valued effective proper-time operator and the
motion/clock factorization remain supplied by the physical model. Degenerate
histories with \(V_0=V_1\) restore the full motion algebra. For interpreting
the sectors as distinct *clock histories* rather than a motion-only relative
phase, one must additionally require
\(\operatorname{Ad}_{V_0}\ne\operatorname{Ad}_{V_1}\), equivalently
\(V_0\not\propto V_1\). The frozen fixture satisfies this stronger
condition.

The broad content is standard commutant and nondemolition structure. No
novelty claim attaches to the theorem.

## Theorem 2 — selective-interface necessity

For every \(\alpha\),

\[
\sum_{r=0}^1
K_r^{(\alpha)}\rho K_r^{(\alpha)\dagger}
=\frac12
\left(
V_0\rho V_0^\dagger+V_1\rho V_1^\dagger
\right).
\]

Hence every rotated motion readout has the same nonselective clock channel.
When \(V_0,V_1\) are linearly independent, the selective maps differ as
\(\alpha\) changes. The source interaction and reduced clock dynamics
therefore do not select one outcome-bearing record instrument.

### Proof

Insert the two rotated Kraus operators. The \(V_0\rho V_1^\dagger\) and
\(V_1\rho V_0^\dagger\) cross terms cancel by orthogonality of the two rows
of the rotation matrix, while the diagonal coefficients sum to one. The
remaining channel is independent of \(\alpha\). Linear independence makes
at least one selective map change under a nontrivial rotation. \(\square\)

This is the familiar unitary freedom of Kraus/instrument realizations, within
the operational tradition of
[Davies and Lewis](https://doi.org/10.1007/BF01647093),
[Kraus](https://doi.org/10.1016/0003-4916(71)90108-4),
[Stinespring](https://doi.org/10.1090/S0002-9939-1955-0069403-4), and
[Ozawa](https://doi.org/10.1063/1.526000). It is not new mathematics.

### Minimal-extra-structure classification

A record-forming completion must add at least one physical structure that
breaks this instrument freedom:

1. an explicit measurement/pointer/archive interaction;
2. an independently derived environment or detector access algebra;
3. a dynamical pointer-selection criterion with a declared tolerance;
4. a symmetry, conservation, locality, or resource constraint that uniquely
   restricts admissible instruments; or
5. an explicit agent-chosen assay interface, honestly classified as a
   controlled intervention rather than a naturally selected record.

Environment-induced pointer selection and redundancy are established
candidate mechanisms, not missing vocabulary; see Zurek's
[predictability-sieve proposal](https://arxiv.org/abs/gr-qc/9402011) and
[Quantum Darwinism](https://arxiv.org/abs/quant-ph/0308163). Dynamic Unity's
open question is whether its stricter history/provenance/access contract
selects anything beyond those mechanisms.

## Theorem 3 — certificate without run-level history disclosure

For the frozen symmetric phases,

\[
K_+
=\frac{V_0+V_1}{2}
=\frac{I}{\sqrt2},
\qquad
K_-
=\frac{V_0-V_1}{2}
=-\frac{iZ}{\sqrt2}
\]

up to a harmless port-sign convention. With clock input \(|+\rangle_C\)
and clock \(X_C\) readout,

\[
p_{\mathrm{coh}}(S=s,X=x)
=\frac12\,\delta_{s,x}.
\]

Therefore

\[
\mathbb E_{\mathrm{coh}}[SX]=1,
\qquad
p_{\mathrm{coh}}(S)=p_{\mathrm{coh}}(X)=\left(\frac12,\frac12\right).
\]

For every \(q\in[0,1]\) in the arbitrary-weight classical-history null,

\[
p_{\mathrm{null},q}(S=s,X=x)=\frac14,
\qquad
\mathbb E_{\mathrm{null},q}[SX]=0.
\]

Moreover, even when the null branch \(h\) is supplied as a latent variable,

\[
p(S,X\mid h=0)=p(S,X\mid h=1)
=\left(\frac14,\frac14,\frac14,\frac14\right).
\]

Thus:

1. the joint certificate record separates the coherent process from the
   declared classical-history set, with single-trial total-variation gap
   \(1/2\);
2. neither record marginal separates them;
3. no stochastic decoder from the complete certificate record can recover
   the run-level history label in the null; and
4. in the coherent alternative, no classical run-level \(h\) is assumed in
   the first place.

### Proof

The displayed Kraus identities follow by adding and subtracting the two
opposite \(Z\) rotations. At the \(+\) port the clock remains
\(|+\rangle_C\); at the \(-\) port \(Z\) maps it to the \(-1\)
\(X_C\) eigenstate. Each port occurs with probability \(1/2\), giving perfect
signed correlation.

After which-history dephasing, an \(X_M\) port readout is uniform for either
history. Each of the two clock-history states lies at \(Y_C=\pm1\) on the
Bloch sphere and therefore has uniform \(X_C\) outcomes. Their joint record
is consequently uniform for each history separately and for every mixture
weight. Identical record rows cannot factor the distinct identity target
\((h=0,h=1)\). \(\square\)

### What “certificate” means

One trial is not a deterministic proof because the coherent and null
distributions overlap. The durable records support a predeclared repeated-run
hypothesis test on the signed score \(SX\). The exact theorem identifies the
population-level separation; finite-shot confidence requires an explicit
sampling and error contract.

This theorem is a specialized form of coherent history recombination and the
signed all-port identity already recorded as `HC-DU-034A`. Zeng's recent
preprint directly occupies the proper-time-history certification framing and
also stresses that the conclusion is relative to the specified history set.
The DU-specific contribution is the four-way typing and its consequence for
the record-formation dependency, not the interference witness itself.

## Unchanged `HC-DU-036` factorization verdict

The existing factorization logic is not semantically refit.

Freeze the candidate record kernel under the classical branch null:

\[
R_C(h)
=p(S,X\mid h)
=\left(\frac14,\frac14,\frac14,\frac14\right)
\]

for both \(h=0,1\). Freeze the target as run-level history disclosure,
\(Y(h)=h\). Because the two rows of \(R_C\) are identical and the two target
rows differ, no stochastic decoder \(D\) can satisfy

\[
Y=R_C D.
\]

The certificate record is therefore **history-insufficient**.

By contrast, a which-history archive has record kernel \(R_H=I_2\) and
factors the history target exactly. But forming that archive before erasure
dephases the two histories and drives the signed certificate to zero. The
two records enable different actions:

| Record | Factors run-level history? | Certifies coherent recombination? |
|---|---:|---:|
| Clock endpoint \(X\) only | no | no |
| Which-history archive | yes | no |
| Coherent port \(S\) only | no | no |
| Joint erasure certificate \((S,X)\) | no | yes, relative to the frozen null |

This is not a violation of record sufficiency. It shows that **the target
proposition must be typed**: a record can be sufficient for a proposition
about a process class while being deliberately insufficient for a latent
history label.

## Standard absorbers and hostile controls

### Absorber 1 — ordinary enlarged quantum process

The motion label, clock, chosen readout basis, detector, archive, and control
settings form one standard quantum instrument plus classical output. No
post-quantum map or record-relative nonlinear dynamics appears.

### Absorber 2 — supplied erasure interface

The certificate exists because the experimenter supplies coherent access to
the complementary motion basis. It is not selected by the proper-time
coupling, the QND history algebra, or the endpoint clock state.

### Absorber 3 — which-history dephasing

Dephase motion in the selected history algebra before the erasure readout.
The joint record becomes uniform and the signed witness vanishes exactly.
The witness is therefore coherence-sensitive, not evidence that a prior
durable history record existed.

### Absorber 4 — classical-null scope

The theorem excludes arbitrary weights over the same two specified history
operations. A classical model with different histories, additional controls,
readout dependence, leakage, or a larger implementation class is outside the
executed null.

### Absorber 5 — no interface-independent record claim

All rotated motion instruments give the same nonselective clock channel.
Any claim that the reduced clock process alone chose the certificate record
is false in this fixture.

## What is established

- **Exact finite theorem:** the controlled proper-time coupling selects the
  diagonal QND history algebra in the frozen nondegenerate two-history class.
- **Exact finite no-go:** the same coupling and nonselective clock channel do
  not select a unique outcome-bearing instrument.
- **Exact finite theorem:** the selected coherent-erasure archive carries a
  process-class certificate with zero run-history information in the frozen
  symmetric fixture.
- **Exact finite factorization result:** certificate sufficiency and history
  sufficiency are distinct, without changing the existing factorization
  contract.
- **Exact absorber:** which-history dephasing erases the certificate.
- **Program result:** interface selection, evidence formation, disclosure,
  and certification must remain separately typed.

The executable probe passes `24/24` deterministic checks.

## What is known rather than DU-specific

- controlled-unitary commutants and QND observables;
- Stinespring/Kraus unitary freedom;
- quantum instruments and their measurement realizations;
- which-path/quantum-erasure complementarity;
- coherent-history recombination;
- proper-time-induced clock--motion entanglement;
- classical-random-time absorption of reduced dephasing; and
- the recent specified-history Choi/separation framing.

These components block any claim that the finite theorem is a new quantum
law.

## The exact Dynamic Unity delta

The useful new repository-level statement is narrower:

> A formed record should be typed by the proposition and action it certifies,
> not presumed to disclose the latent history whose process class it
> constrains. In coherent-history assays, the source-selected stable history
> algebra and the certificate-forming complementary instrument can be
> intentionally different. Therefore `HC-DU-033` interface selection and
> `HC-DU-034` history certification are coupled but neither subsumes the
> other.

This corrects two tempting inferences:

```text
certificate about histories
    does not imply
record of which history;

source-selected history algebra
    does not imply
source-selected certificate interface.
```

## Ontology-compatible interpretations

The result leaves all three charter outcomes open.

1. **Record-first reconstruction.** The certificate record may be the
   actionable object, while a run-level history is not part of the observer's
   certified reality.
2. **Operational duality.** The enlarged quantum instrument and the typed
   record description are two complete operational accounts of the same
   fixture.
3. **Physics-first remainder.** The selected readout coupling, coherent
   control, detector, and archive are physical structures not derivable from
   the abstract record relation alone.

Nothing here chooses among them.

## Exact next dependency

The next primary physical attempt should not add another abstract history
label. It must replace the two-qubit effective fixture with one frozen
laboratory-level instrument containing:

1. the actual clock--motion Hamiltonian and squeezed motional preparation;
2. the implemented coarse-graining that defines the finite proper-time
   history set;
3. a physically specified coherent-recombination/readout coupling;
4. all clock and motion operations at every event slot;
5. every detector port, invalid event, setting, and provenance field;
6. a durable archive channel and declared observer/access algebra;
7. calibrated SPAM, drift, phase noise, motional leakage, detector confusion,
   and classical-control nulls;
8. coherence, energy, memory, latency, and discarded-support costs; and
9. a target-independent admissible interface-refinement class.

Only then can the existing robust convex separation and
`HC-DU-036B` factorization machinery return one of:

- a physically formed proper-time certificate;
- interface incompleteness repaired by a charged refinement;
- a formation-relative physical remainder; or
- an incomplete comparison contract.

The sharp research question is not whether the ideal witness is nonzero. It
is:

> Which physical feature selects and durably forms the coherent certificate
> instrument, and does its calibrated record retain separation after every
> admitted implementation completion?

## State and custody disposition

This scoped result does not by itself warrant:

- a new physical-law claim;
- a prediction-register entry;
- a new ontology concept;
- closure of parent `HC-DU-033`, physical `HC-DU-034B`, or `HC-DU-036B`;
- promotion of `HC-DU-035B` public-finality work;
- geometry, QFT, gravity, or cosmology recovery; or
- a Drafting Factory submission.

It is a useful exact exploration and dependency result. Shared ledgers and
lane state remain for the integrating lead to assess.

## Reproducibility

Run:

```bash
python3 tests/du_record_formation_composition_probe.py
```

Expected receipt:

```text
24/24 checks passed
```

The deterministic machine artifact is
`tests/artifacts/du_record_formation_composition_result.json`.
