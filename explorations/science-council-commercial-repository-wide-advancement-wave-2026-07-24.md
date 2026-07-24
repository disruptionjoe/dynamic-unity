---
title: "Science Council commercial scientist — repository-wide advancement wave"
status: completed_persona_work
doc_type: council_persona_memo
created: 2026-07-24
persona: commercial_scientist
claim_grade: "EXACT FINITE ASSAY SPECIALIZATION / PRODUCTIZATION ADVANCE / NOT A NEW PHYSICAL LAW"
banked: false
seeded: false
---

# Commercial scientist: make causal-history certification experimentally buyable

## Executive result

I chose `HC-DU-034`, multi-event causal-history certification, but not as a
general manifesto and not because it is next in a fixed sequence. The
commercially strongest one-swing product is a **minimum viable history
certification assay**: preserve both coherent-recombination ports, sign the
clock result by the port record, and test one cross-history correlator.

The exact bounded result is:

> For any two coherently controlled histories, a signed all-port statistic
> isolates their cross-history coherence, while every incoherent classical
> mixture of the same specified histories has expectation zero. In the
> symmetric two-port fixture, retaining and signing both ports uses every
> preparation and therefore halves the expected preparation count relative
> to throwing one port away.

This is useful because it turns the repository's distinction between an
endpoint signal and a certified history into an experimental data contract.
It is not a new quantum law. The Choi-cone separation and conditioned-port
idea are already supplied by
[Zeng's proper-time-history certification proposal](https://arxiv.org/abs/2606.12755);
the physically motivated trapped-ion target is supplied by
[Sorci et al.](https://arxiv.org/abs/2509.09573). The increment here is the
all-port estimator, its exact null, a finite-shot calibration rule, and a
stage gate for deciding whether a clock platform is worth pursuing.

## Repository-wide candidate comparison

I compared materially different opportunities rather than treating the
latest threshold work as the default.

| Rank | Attempt | Profundity and novelty ceiling | One-swing and product judgment |
|---:|---|---|---|
| 1 | `HC-DU-034`: proper-time/history certification assay | Directly separates a quantum-looking endpoint from evidence of coherent causal history; could become the first physical discriminator in the rechartered program | Best combination of a real experimental customer, exact bounded mathematics, a protocol artifact, and a near-term kill |
| 2 | `HC-DU-036`: factorization-or-witness compiler | Closest to the central ontology fork and potentially foundational | Excellent future software product, but the finite-state core risks being ordinary automata minimization unless the physical intervention contract adds something |
| 3 | `HC-DU-033`: dynamical record-interface selection | Solves the first dependency and would be genuinely foundational | High ceiling, but one swing is more likely to produce another selected toy pointer algebra than a defensible selection law |
| 4 | `HC-DU-038`: geometry from provenance/meta-records | Potential blockbuster if metric structure, not mere reachability, is reconstructed | Too easy to import latency, density, or causal order and then announce it was recovered; not yet a responsible one-swing product |
| 5 | `HC-DU-035B/037`: formation, finality, capability, and optionality cost | Strong cross-domain law and direct relevance to reliable agents and distributed infrastructure | Worth pursuing after a physical record instrument is fixed; otherwise it decomposes into known resource and quorum results |
| 6 | Causal-growth generativity and held-out geometry | A native history dynamics could eventually connect records, scale, and geometry | Long experimental loop, substantial prior-art burden, and no immediate buyer-facing discriminator |
| 7 | GU, Standard Model, or cosmology recovery | Highest rhetorical ceiling | Dependencies are missing; a one-swing result would almost certainly be a conditional fit or imported scale rather than a publishable advance |

The selected assay dominates commercially because its negative result is also
valuable: a laboratory can learn cheaply that its proposed clock readout
cannot exclude the classical-history null before committing to a much larger
experiment.

## Frozen object and rival contract

Let `B` be a two-valued history-label system, `C` the clock or target system,
`rho` its prepared state, and `V_0,V_1` the two **experimentally specified**
history operations. The coherent process, allowing a real visibility
parameter `v` for clarity, is

\[
\rho_v={1\over2}\left(
|0\rangle\langle0|\otimes V_0\rho V_0^\dagger+
|1\rangle\langle1|\otimes V_1\rho V_1^\dagger+
v|0\rangle\langle1|\otimes V_0\rho V_1^\dagger+
v|1\rangle\langle0|\otimes V_1\rho V_0^\dagger
\right).
\]

The rival class is every incoherent mixture of these same declared histories,
with arbitrary weights:

\[
\sigma_{\rm cl}=\sum_{i=0}^1p_i|i\rangle\langle i|
\otimes V_i\rho V_i^\dagger.
\]

It does **not** include an adversary allowed to add a new coherent controller,
prepare an arbitrary replacement state after seeing the port, or change the
history set after the result. Such a broader rival would make this witness
irrelevant by changing the comparison contract.

The experiment measures `X_B` on the history label, giving port
`s in {-1,+1}`, and a bounded binary clock observable `W`, giving
`x in {-1,+1}`. It retains the provenance pair `(s,x)` and reports

\[
Y=sx.
\]

No public-finality claim is made. A detector click is a trace; retaining its
port, setting, calibration, and trial identity makes it an experimental
record. Authentication, independent access, and durable finalization remain
additional layers.

## Exact advancement

### Signed-port pooling theorem

For the contract above,

\[
\mathbb E_{\rho_v}[Y]
=\operatorname{Tr}[(X_B\otimes W)\rho_v]
=\operatorname{Re}\!\left[
v\,\operatorname{Tr}(W V_0\rho V_1^\dagger)
\right].
\]

For every `sigma_cl` in the rival class,

\[
\mathbb E_{\sigma_{\rm cl}}[Y]=0
\]

independently of the mixture weights and independently of the individual
history endpoints.

**Proof.** `X_B` has zero diagonal in the history basis, so both diagonal
terms of any incoherent mixture vanish in the trace. On `rho_v`, its two
off-diagonal matrix elements select the two conjugate cross-history terms;
their half-sum is the displayed real part. This uses the complete joint
record and cannot be recovered from the reduced endpoint state after `B` is
discarded. QED.

The estimator is also exactly the signed difference of the two conditional
ports:

\[
\mathbb E[Y]
=p_+\mathbb E[x\mid +]-p_-\mathbb E[x\mid -].
\]

Thus discarding a port is unnecessary. In the symmetric case where both
ports occur with probability `1/2` and become equivalent after changing the
sign, an accepted observation from either port has the same distribution.
Keeping both produces one observation per preparation; keeping only one
requires two preparations on average per accepted observation. The expected
preparation saving is exactly a factor of two.

### Minimal exact fixture

Choose

\[
V_0=I,\qquad V_1=X,\qquad \rho=|0\rangle\langle0|,\qquad W=X.
\]

Then

\[
P(s,x)={1+s x v\over4},\qquad \mathbb E[Y]=v.
\]

At `v=1`, the coherent process is the Bell state
`(|00>+|11>)/sqrt(2)` and `Y=+1` on every shot. At `v=0`, every incoherent
mixture has `E[Y]=0`. For the equal-weight dephased state generated by this
fixture at `v=0`, the reduced clock endpoint is `I/2`, just as it is for the
coherent Bell state. An endpoint-only clock readout therefore misses exactly
the distinction the joint history record detects.

This is a positive control, not a proper-time result. A physical clock
experiment must substitute its actual histories and accessible `W`.

### Calibrated finite-shot gate

Let calibration bound every admitted classical-null implementation by
`E[Y] <= b`, and let detector contrast and history visibility predict an
alternative mean

\[
\mu=\eta\left|\operatorname{Re}
\left[v\,\operatorname{Tr}(W V_0\rho V_1^\dagger)\right]\right|.
\]

Define the usable margin `g=mu-b`. If `g<=0`, the proposed assay is not
commercially ready. For `g>0`, with `Y in [-1,1]`, reject the null when

\[
\bar Y>b+\sqrt{{2\ln(1/\alpha)\over n}}.
\]

Hoeffding's inequality gives false-positive probability at most `alpha`.
Power is at least `1-beta` under the declared alternative whenever

\[
n\ \ge\
{2\left(\sqrt{\ln(1/\alpha)}+
\sqrt{\ln(1/\beta)}\right)^2\over g^2}.
\]

This is conservative rather than optimal, but it is preregistrable and needs
no fitted asymptotics. Unlike a one-port protocol, `n` is the number of
prepared trials because every authenticated port contributes.

## Resources, free choices, and falsifiers

The minimum fixture charges:

- one coherent history-label degree of freedom;
- controlled implementation of `V_0` and `V_1`;
- one history-erasing `X_B` measurement;
- one accessible binary clock measurement `W`;
- phase stability sufficient to maintain `v`;
- trial, setting, port, and clock-result provenance;
- calibration trials establishing `b` and detector contrast `eta`; and
- all preparations, including failed or invalid trials, in the resource
  ledger.

The free choices are the specified history set, input `rho`, readout `W`,
calibration model, and accepted device-drift envelope. They must be frozen
before looking at the witness data.

The result is killed for a proposed platform if:

1. no experimentally accessible `W` produces positive calibrated margin;
2. the dephased-history null produces the same signed statistic;
3. port relabeling, setting drift, leakage, or postselection can reproduce
   the result inside the admitted classical instrument class;
4. the predicted shot count exceeds the coherence or stability budget; or
5. the physical mapping to proper-time histories requires fitting a different
   `V_i` after each result.

## Exact result and grade

```text
SIGNED-PORT CROSS-HISTORY IDENTITY                  = EXACT
ARBITRARY-WEIGHT INCOHERENT-HISTORY NULL            = EXACT
TWO-PORT EXPECTED PREPARATION SAVING                = EXACT IN THE SYMMETRIC FIXTURE
FINITE-SHOT SIGNIFICANCE/POWER BOUND                = CONSERVATIVE DERIVATION
PROPER-TIME IMPLEMENTATION                          = OPEN
SPAM/DRIFT-ROBUST NULL CONE                         = OPEN
PUBLIC FINALITY OR OBJECTIVITY                      = NOT ESTABLISHED
RECORD-FIRST ONTOLOGY                               = NOT ESTABLISHED
NOVEL PHYSICAL LAW                                  = NO
PRODUCTIZATION / EXPERIMENT-DESIGN ADVANCE          = YES
CLAIM BANK / PREDICTION SEED                        = UNCHANGED
```

The honest grade is **EXACT FINITE ASSAY SPECIALIZATION / PRACTICAL
PRODUCTIZATION ADVANCE**. The algebra is not itself publication-level
novelty. A publishable result would require the actual ion-clock instrument,
a realistic calibrated null cone, and a surviving resource advantage or new
separation theorem.

## What failed or is no longer worth the time

- A frequency shift, visibility loss, or single-time dephasing trace by
  itself is not worth presenting as certification of nonclassical history.
- Discarding the dark or bright port is wasteful when a signed all-port record
  is available.
- The Bell-state fixture is not evidence of quantum proper time; it is only
  an exact assay control.
- More abstract analogies between quantum coherence and consensus should wait
  until one physical instrument survives the calibrated test.
- A universal scalar “objectivity threshold” is not needed for this assay.
- GU or cosmology recovery from the witness would be dependency-skipping.

## Newly visible hypotheses, theorems, and conjectures

1. **Multi-history character-pooling theorem — high priority.** For `m`
   histories, Fourier/character-weighted use of every recombination port may
   estimate the full off-diagonal history-coherence matrix without
   postselection. Determine the optimal accessible observable set and exact
   sample advantage.
2. **Robust instrument-cone separation theorem — high priority.** With a
   frozen SPAM, drift, leakage, and control-error class, certification should
   reduce to whether an empirical moment vector lies beyond the support
   function of a calibrated classical-history cone.
3. **History-certificate efficiency law — medium priority.** The relevant
   experimental figure of merit is not raw visibility but certified margin
   squared per complete resource cost, including invalid trials, coherence
   time, and provenance.
4. **Physical-remainder witness — medium priority.** If two implementations
   agree on every reduced clock trace but disagree on an admitted pooled
   cross-history statistic, the branch coherence or an operationally
   equivalent physical resource is a finite remainder beyond the reduced
   record quotient.
5. **Formation-to-publication chain — exploratory.** The cost of turning the
   ephemeral `(s,x)` correlation into a durable, independently auditable fact
   may supply a concrete physical input to `HC-DU-035B/037`, rather than
   beginning those laws from abstract fragments.

## Next decisive test

Take the explicitly specified two-history operations in the trapped-ion
proper-time proposal and solve, under the laboratory's allowed measurements,

\[
\max_W
\left|\operatorname{Re}\operatorname{Tr}
(W V_0\rho V_1^\dagger)\right|.
\]

Then freeze four arms:

1. coherent histories with both ports retained;
2. deliberately dephased history label;
3. reduced single-time clock readout only; and
4. randomized port provenance or phase as an instrumentation null.

Estimate `b`, `eta`, `v`, the signed margin, total preparations, coherence
budget, and drift window before claiming feasibility. Stop the platform if no
accessible `W` clears the systematic null with a tolerable shot count. If it
does clear, build the complete instrument-level Choi/cone comparison rather
than publishing the Bell control.

## Short divergent wish list

- An open-source “history certificate compiler” that converts declared
  controls and accessible measurements into optimal all-port witnesses.
- A distributed-systems twin of the same estimator using signed provenance
  branches rather than quantum amplitudes, to reveal exactly where the
  analogy breaks.
- A clock-network experiment in which the witness record is independently
  replicated after measurement, letting formation, access, and public
  finality be measured separately.
- A multi-port experiment where pooling changes an apparently infeasible
  postselected proposal into a feasible one.
- A formal value-of-experiment layer reporting dollars, instrument hours, and
  decision value alongside scientific power.

## Plain-English interpretation

A normal clock measurement can look quantum even when an ordinary lottery
over classical histories explains it. The useful move is to keep the piece of
the experiment that says **which coherent recombination output occurred** and
combine its sign with the clock result. Classical mixtures have no
cross-history term, so their signed average is zero. A coherent history can
make it nonzero even when the final clock state, viewed alone, looks exactly
the same.

The practical surprise is that the supposedly “dark” port is not waste. If
its result is sign-corrected, it contains the same kind of evidence as the
bright port. Keeping both can cut the preparation bill in half in the
symmetric case.

This does not show that information is fundamental, that proper time is
quantum, or that a public fact has formed. It gives Dynamic Unity something
more valuable at this stage: a small, honest assay that can tell an
experimental team whether its proposed evidence actually distinguishes
coherent causal histories from the specified classical alternative.
