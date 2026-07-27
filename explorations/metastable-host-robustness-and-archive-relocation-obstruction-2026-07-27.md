---
title: "Metastable-host robustness and the archive-relocation obstruction"
status: completed_scoped_host_adjudication
doc_type: theorem_and_adjudication_result
created: 2026-07-27
claim_id: HC-DU-046
campaign: ECR-N5-S5
authority: "Joe direct chat: Go"
run_plan: "../runs/2026-07-27-metastable-host-robustness-adjudication.md"
probe: "../tests/du_metastable_host_robustness_adjudication_probe.py"
artifact: "../tests/artifacts/du_metastable_host_robustness_adjudication_result.json"
predecessor: "completion-common-record-quotient-and-two-tier-capability-leak-2026-07-27.md"
claim_status_change: "ECR-N5-S5 complete as HC-DU-046; frozen host closed adversely for endogenous historical records"
paper_state_change: none
prediction_state_change: none
hardware_state_change: none
---

# Metastable-host robustness and the archive-relocation obstruction

## Executive result

The finite failure in `HC-DU-045` is not a short-horizon artifact.

For the frozen four-state metastable host:

1. the unique finest record common to the visible-archive and
   hidden-reservoir completions is the terminal matter endpoint at every
   prefix horizon;
2. that endpoint continues to reconstruct the next reduced-matter branch
   law;
3. exact historical occurrence first stops factoring through it when the
   first four-step cycle closes;
4. the same empty-history/four-edge witness remains available at every
   longer horizon;
5. positive stochastic branch weights, lossless token relabeling, and benign
   temporal subdivision do not repair the exact failure;
6. a probabilistic full-history leak has an exact error law and reaches exact
   sufficiency only at complete revelation;
7. no premise encoded solely by the frozen matter host can select whether
   the history archive lies in accessible fragment \(A\) or hidden fragment
   \(H\); and
8. reading \(A+H\) repairs every history target only by changing the access
   contract into horizon-growing injective tomography.

The final verdict for this host is therefore:

```text
SELECTION_OR_FORMATION_OBSTRUCTION
```

This closes the metastable host. It is not a universal theorem that physical
records cannot form. It says that this host does not select the environmental
routing, archive location, epoch, or observer access needed to turn its
selected write/turnover architecture into an endogenous historical record.

The broader `H-CCR-17` North-Star challenge remains open outside this host.
The next work should compile the minimum missing physical premise and compare
that route against the strongest non-record alternatives across Dynamic
Unity. It should not fit another archive to this host.

## 1. Frozen contract

### 1.1 Matter dynamics

The inherited host is the deterministic four-state cycle

\[
x_0\xrightarrow{W}x_1
\xrightarrow{C}x_2
\xrightarrow{W}x_3
\xrightarrow{C}x_0 ,
\]

viewed from initial state \(x_1\). Its event word is therefore

\[
C,W,C,W,C,W,\ldots .
\]

Let \(h_k\) denote the history containing the first \(k\) transitions and
let

\[
\Omega_N=\{h_0,h_1,\ldots,h_N\}
\]

be the prefix-history class through horizon \(N\). Write \(X(h_k)\) for the
terminal matter state.

### 1.2 Matched completion pair

The two completions have identical matter histories and reduced transition
laws.

- In the **visible completion** \(V\), a unique history token is retained in
  admitted fragment \(A\), while \(H\) is blank.
- In the **hidden completion** \(H\), the same token is retained in reservoir
  \(H\), while admitted fragment \(A\) is blank.

At the \(A\)-only observer boundary their native records are

\[
r_V(h_k)=(X(h_k),\operatorname{token}(h_k))
\]

and

\[
r_H(h_k)=(X(h_k),\bot).
\]

The frozen historical targets are:

\[
O(h_k)=
\begin{cases}
1 & \text{if a write occurred,}\\
0 & \text{otherwise,}
\end{cases}
\]

\[
C_W(h_k)=\text{number of writes},
\qquad
W(h_k)=\text{resolved event word}.
\]

The positive control is the complete next reduced-matter branch profile
\(B(h_k)\), which depends only on \(X(h_k)\).

No detector, environment Hamiltonian, archive factorization, or target-coded
record is added during adjudication.

## 2. Arbitrary-horizon common-quotient theorem

### Theorem 1 — completion-common quotient at every horizon

For every finite \(N\geq0\), the unique finest target-independent quotient
that factors through both \(r_V\) and \(r_H\) is

\[
q_N(h_k)=X(h_k).
\]

#### Proof

Any statistic common to both native records must factor through \(r_H\).
But \(r_H\) contains only \(X(h_k)\) and a constant blank symbol. Therefore
every common statistic is a function of \(X\).

Conversely, \(X\) is a projection of both \(r_V\) and \(r_H\). It is itself a
common statistic. Hence it is the unique finest common quotient, up to
bijective relabeling. \(\square\)

This is stronger than checking a finite partition table. It covers every
prefix horizon and makes clear why adding visible history detail cannot
alter the completion-common answer while the hidden completion remains
admitted.

### Corollary 1 — operational future closure survives

The next reduced-matter branch law factors through \(q_N\) for every \(N\):

\[
B=d_B\circ q_N .
\]

The host therefore earns a real positive result:

```text
MARKOV_OPERATIONAL_CLOSURE
```

The present matter state is enough to predict the next reduced matter step.
This is not yet historical-record reconstruction.

### Theorem 2 — exact first historical failure

For \(N<4\), the endpoint happens to distinguish every admitted prefix, so
all three historical targets factor accidentally.

At \(N=4\),

\[
X(h_0)=X(h_4)=x_1,
\]

while

\[
O(h_0)=0,\qquad O(h_4)=1,
\]

\[
C_W(h_0)=0,\qquad C_W(h_4)=2,
\]

and

\[
W(h_0)=\epsilon,\qquad W(h_4)=CWCW.
\]

Therefore occurrence, count, and word do not factor through \(q_N\) for any
\(N\geq4\).

#### Proof

The host has period four. The pair \(h_0,h_4\) belongs to every
\(\Omega_N\) with \(N\geq4\), has the same endpoint, and differs on all three
historical targets. Enlarging the horizon cannot remove an existing
same-record/different-target witness. \(\square\)

Thus the first failure is exactly the first completed cycle, not a
large-system approximation or an asymptotic effect.

## 3. Stochastic weights do not repair exact factorization

Exact target factorization is a support property:

\[
r(m_1)=r(m_2)\Longrightarrow t(m_1)=t(m_2).
\]

Changing probabilities without removing a witness from support cannot make
this implication true.

### Proposition 1 — positive-weight robustness

Let \(P\) be any probability distribution on \(\Omega_N\), \(N\geq4\), with

\[
P(h_0)>0,\qquad P(h_4)>0.
\]

Then occurrence, count, and word remain nonfactorizing through the terminal
endpoint almost surely on the positive support.

The result also survives a continuous-time version of the same directed
cycle. For any finite nonexplosive continuous-time Markov chain with
strictly positive transition rates and any positive observation time, both
the zero-jump and four-jump histories have positive probability. They end at
the same state and disagree on occurrence.

Probability can make the adverse history rare. It cannot turn exact
sufficiency into a theorem. Approximate decision quality is a separate
question, treated in Section 5.

## 4. Representation and subdivision invariance

### 4.1 Lossless relabeling

Let \(\alpha\) be a bijection on archive tokens. Replacing
\(\operatorname{token}(h)\) with \(\alpha(\operatorname{token}(h))\) leaves
every record kernel unchanged. The common quotient and all factorization
verdicts are therefore invariant.

This rules out dependence on the spelling, encoding, or numerical identity
of the history token.

### 4.2 Benign temporal subdivision

Let \(c_s:\widetilde\Omega_{sN}\to\Omega_N\) contract each block of \(s\)
micro-events into one macro-event. A subdivision is **benign for this
contract** when:

1. records and targets are pulled back along \(c_s\);
2. no new intermediate microstate is granted observer access; and
3. completed macro-boundaries retain the original endpoint and event
   identity.

Then the subdivided histories \(\tilde h_0\) and \(\tilde h_{4s}\) contract to
\(h_0\) and \(h_4\). They retain the same endpoint and different occurrence.
The obstruction therefore survives every \(s\geq1\).

If the new microstates are made observable, or if a new clock/event counter
is added at subdivision boundaries, the record map has been refined. That
may repair a target, but it is not representation invariance; it is a
stronger physical interface contract.

## 5. Exact boundary for approximate archive leakage

To distinguish exact sufficiency from useful but imperfect inference, add
one declared stochastic channel. It does not reveal a target-coded
occurrence bit. It reveals the complete history token with probability
\(\lambda\), and otherwise erases it:

\[
Z_\lambda(h)=
\begin{cases}
(X(h),\operatorname{token}(h)) & \text{with probability }\lambda,\\
(X(h),\bot) & \text{with probability }1-\lambda.
\end{cases}
\]

The hidden reservoir still retains the complete token. Only its accessible
leak is varied.

### Theorem 3 — exact versus approximate boundary

Assume the support contains \(h_0\) and \(h_4\).

- If \(0\leq\lambda<1\), exact occurrence reconstruction fails.
- If \(\lambda=1\), every resolved history is revealed and all historical
  targets factor.

#### Proof

For \(\lambda<1\), output \((x_1,\bot)\) has positive probability under both
\(h_0\) and \(h_4\), whose occurrence values differ. At \(\lambda=1\), the
history token is injective on \(\Omega_N\). \(\square\)

There is no exact noninjective “sweet spot” in this leak family. Exact repair
arrives only with full-history revelation.

### Theorem 4 — Bayes error law

Let \(P\) be any prior over histories and use zero-one loss for occurrence.
Then the optimal Bayes error is

\[
R_{\mathrm{Bayes}}(\lambda)
=(1-\lambda)
\sum_x
\min\!\left\{
P(O=0,X=x),
P(O=1,X=x)
\right\}.
\]

#### Proof

Every revealed token identifies its history and contributes zero error.
Every erased output retains only endpoint \(x\). The optimal decision at that
output chooses the more probable occurrence label, incurring the smaller
of the two endpoint-label masses. Erasure multiplies every such mass by
\(1-\lambda\). Summing over endpoints gives the result. \(\square\)

For the equal-prior pair \(h_0,h_4\),

\[
R_{\mathrm{Bayes}}(\lambda)
=R_{\mathrm{minimax}}(\lambda)
=\frac{1-\lambda}{2}.
\]

The total-variation distance between their output distributions is
\(\lambda\). Thus the error moves smoothly from \(1/2\) to zero, while exact
factorization changes only at \(\lambda=1\).

This is the required decision boundary. Any future statement that an archive
is “approximately sufficient” must declare the leak family, prior or
minimax class, loss, target, and action envelope. It cannot inherit the exact
claim’s language.

## 6. Resource normalization and tomography control

At every horizon the common endpoint record has at most four values, hence
at most two bits of distinguishability.

The resolved prefix history has \(N+1\) possible values and therefore
requires at least

\[
\left\lceil\log_2(N+1)\right\rceil
\]

bits even under ideal lossless coding. The concrete fresh-output
implementation additionally uses growing physical support and retention.

Granting access to both \(A\) and \(H\) allows the observer to read the token
wherever it was routed. This reconstructs occurrence, count, and word, but:

1. it changes the observer boundary and action envelope;
2. it makes the record injective on the finite history class; and
3. its information requirement grows with horizon.

The appropriate control verdict is:

```text
INJECTIVE_TOMOGRAPHY_ONLY
```

It is an important positive control, not the endogenous compressive result
sought by `H-CCR-17`.

## 7. Archive-relocation obstruction

The central remaining question was whether some premise genuinely selected
by the metastable host could exclude the hidden completion.

### Theorem 5 — symmetry obstruction to interface selection

Let

\[
a:M\to A
\]

be a claimed physical antecedent and

\[
\xi:M\to I
\]

the archive/interface structure it is claimed to select. Suppose there is an
involution

\[
\tau:M\to M,\qquad \tau^2=\mathrm{id},
\]

such that

\[
a\circ\tau=a
\]

but

\[
\xi\circ\tau\neq\xi
\]

for at least one completion.

Then no selector \(s:A\to I\) can satisfy

\[
\xi=s\circ a.
\]

#### Proof

If such \(s\) existed, then

\[
\xi\circ\tau=s\circ a\circ\tau=s\circ a=\xi,
\]

contradicting the assumed interface change. \(\square\)

This is a general fibre criterion, not new mathematics by itself. Its useful
content here is the exact physical typing of the symmetry.

### Instantiation on the frozen host

Let \(\tau\) swap the location of the same history token between accessible
fragment \(A\) and hidden reservoir \(H\), holding fixed:

- the complete matter trajectory;
- the four-state carrier;
- the write/turnover generator;
- the transition and rate architecture;
- the ready/retained orbit structure;
- the terminal state and next reduced law; and
- the total environmental retention of the history token.

The maximal host-only antecedent is invariant under this swap. The admitted
\(A\)-only archive interface is not.

Therefore the frozen host cannot select archive location or observer access.
No theorem stated solely in terms of its matter generator can exclude the
hidden twin.

### Premise audit

| structure | host status | consequence |
|---|---|---|
| four-state material carrier | selected/frozen | legitimate host structure |
| alternating write/turnover edge architecture | selected up to relabeling | distinguishes transition roles |
| terminal next-state law | selected | supports Markov operational closure |
| ready/retained value orbit | orbit-selected | does not certify occurrence |
| environment factorization \(A\otimes H\) | supplied | not fixed by host |
| blank archive carrier | supplied | formation antecedent |
| history-routing coupling | supplied | decides visible versus hidden completion |
| retention horizon and epoch | supplied | decides historical semantics |
| archive location | not selected | changed by \(\tau\) |
| observer boundary and access route | supplied | decides capability |

A richer source-plus-environment law could break the relocation symmetry.
That is not forbidden. But it is a new physical antecedent, and it must
select the interface independently of the desired history target. Adding it
to this host simply to eliminate the hostile completion would be refitting.

## 8. Strongest absorber collision

### Markov sufficiency

Absorbs the positive future result. A Markov state is supposed to determine
the next reduced transition law. Dynamic Unity should keep this result as a
typed positive control, not claim novelty for it.

### Hidden-state and complementary-channel freedom

Absorbs the fact that one reduced process can have multiple environmental
realizations carrying different accessible history. Stinespring,
unravelling, and process-tensor perspectives all warn that reduced dynamics
does not select an archive decomposition.

### Observability and sufficient statistics

Absorb the endpoint/history distinction at the mathematical level. The
Dynamic Unity contribution is the joint audit of:

- physical formation;
- completion transfer;
- observer access;
- exact versus approximate sufficiency;
- capability growth; and
- resource-normalized tomography.

### Distributed systems

Distributed systems supplies an architectural control: current state, event
provenance, durable log, public certificate, and action-safe finality are
different objects. It does not prove that nature implements a ledger. Here it
helps prevent terminal matter value from being mislabeled as a historical
certificate.

No component theorem alone is a new law of physics. The result’s value is
that it closes an attractive physical host without confusing operational
future closure, environmental memory, accessible record formation, and
historical reconstruction.

## 9. `H-CCR-17` passport

| obligation | result on this host |
|---|---|
| physically natural dynamics | yes, as a frozen finite metastable toy |
| interface selected by the same antecedent | **no**; archive relocation symmetry |
| record physically formed from a blank carrier | conditional on supplied fresh-output completion |
| observer access selected | **no** |
| record noninjective on lawful nongauge class | endpoint is noninjective |
| held-out historical target reconstructs | **no** from endpoint |
| no refit across action/resource envelope | full repair changes access and becomes injective |

The conjunction fails before historical transfer because selection and
formation are incomplete. The first exact historical leak remains
occurrence.

## 10. Final adjudication

The allowed verdict list was:

```text
ENDOGENOUS_COMPRESSIVE_RECONSTRUCTION
ENDOGENOUS_OPERATIONAL_DUALITY_ONLY
FINITE_CAPABILITY_RELATIVE_REMAINDER
SELECTION_OR_FORMATION_OBSTRUCTION
INJECTIVE_TOMOGRAPHY_ONLY
INCOMPLETE_CONTRACT
```

The host-level verdict is:

```text
SELECTION_OR_FORMATION_OBSTRUCTION
```

with two typed companion results:

```text
positive reduced-future control: MARKOV_OPERATIONAL_CLOSURE
full-environment repair control: INJECTIVE_TOMOGRAPHY_ONLY
```

This is a complete contract for the frozen host, not an
`INCOMPLETE_CONTRACT` return. The negative statement is scoped:

> Within the declared host and robustness family, the matter dynamics does
> not select an accessible historical archive. Endpoint records close the
> reduced future but fail at the first completed cycle, and every exact
> history repair either supplies the archive/access structure or reveals the
> full history injectively.

It does **not** establish:

- a universal impossibility of physical record formation;
- a remainder beyond standard quantum or stochastic physics;
- a new empirical prediction;
- a paper-ready novelty claim;
- an external-hardware requirement; or
- closure of `H-CCR-17` in other physical arenas.

## 11. Next decision

`ECR-N5-S1` through `ECR-N5-S5` are complete. The metastable host should now
leave active routing.

The initially queued object was:

```text
N5-RS-P2
Minimum-Premise Compiler and Whole-DU Portfolio Pivot
```

Joe subsequently interposed the
[`N5-SCF` stochastic/consensus/complexity/cryptography
sequence](next-five-swing-stochastic-consensus-finality-scaffold-2026-07-27.md).
Only `N5-SCF-P1` is now executable. `N5-RS-P2` remains deferred and, if
resumed, must:

1. build the premise lattice for source/environment law, physical
   factorization, blank preparation, write coupling, provenance, retention,
   archive routing, observer access, action envelope, and resource horizon;
2. determine the weakest independently motivated premise that breaks the
   archive-relocation symmetry;
3. distinguish selection, permission, exposure, and target coding;
4. compare continued record-selection work with the \(3+1\) law-filtered
   reconstruction seam, localized AQFT, environment-selected records/SBS,
   causal-action/CFS narrowing, and deliberate stop; and
5. return exactly one named route rather than opening several builds.

Until that comparison closes, no new record host, detector, provider,
hardware run, paper, or prediction is activated.

## 12. Local certificate

Run:

```bash
python3 tests/du_metastable_host_robustness_adjudication_probe.py
```

The deterministic certificate:

- checks horizons \(0\) through \(40\);
- verifies that failure begins at four and remains afterward;
- checks lossless relabelings and subdivisions \(s=1,\ldots,8\);
- evaluates the exact rational Bayes formula under four positive priors and
  five leak probabilities;
- checks the archive-swap selection obstruction;
- reports the injective resource-growth control; and
- writes
  `tests/artifacts/du_metastable_host_robustness_adjudication_result.json`.

The finite checks are regression coverage for the analytic proofs above.
They are not the proof of arbitrary horizon, a physical simulation, or
evidence about nature.

## Bottom line

The host really does select enough structure to predict its next reduced
step. It does not select where its own history becomes an accessible record.
Once a cycle closes, the same terminal state can mean “nothing happened” or
“a complete write/turnover cycle happened.” Longer time, stochastic
weighting, relabeling, and harmless subdivision do not change that. Partial
history leakage improves decisions by an exactly calculable amount, but
exact recovery arrives only when the whole history is exposed.

The valuable conclusion is not “records fail.” It is:

> A dynamics can select state evolution and even write-like transition roles
> without selecting the archive-routing and access structure required for
> historical reality. On this host, that missing interface is the decisive
> physical premise.
