---
title: "HC-DU-035A — layered threshold objectivity"
status: completed_scoped_result
doc_type: theorem_and_counterexample_synthesis
created: 2026-07-24
run_id: RUN-20260724-174434-hc-du-035a-layered-threshold
hardening_id: HC-DU-035A
probe: tests/du_layered_threshold_objectivity_probe.py
artifact: tests/artifacts/du_layered_threshold_objectivity_result.json
claim_grade: "EXACT FINITE SPECIALIZATIONS / USEFUL TYPED SYNTHESIS / PHYSICAL FORMATION-TO-FINALITY LAW OPEN"
novelty_status: "KNOWN COMPONENT THEOREMS / STATIC CONJUNCTION COLLIDES / RESOURCE-COUPLED PHYSICAL CONJUNCTION SEARCH-INCOMPLETE"
banked: false
seeded: false
---

# HC-DU-035A — layered threshold objectivity

## Executive result

The proposed single “objectivity threshold” does not survive.

There are at least three differently typed thresholds:

1. **reconstruction:** enough evidence to distinguish a declared history
   within a frozen error contract;
2. **finality:** enough authenticated and locked support to exclude
   incompatible certificates within a frozen adversary contract; and
3. **capability:** enough action-relevant evidence and public stability to
   make a declared action pass independent risk, reversal, cost, and resource
   limits.

They can occur separately. Their numerical coincidence has no invariant
meaning until a common physical path and resource coordinate have been
declared.

The strongest exact findings are:

- locked equal-size quorums exclude incompatible certificates exactly when
  \(2q>N+f\), with a constructive split view when the inequality fails;
- the honest-intersection surplus
  \[
  h=\max(0,2q-N-f)
  \]
  is exactly the number of honest double-sign failures required before a
  worst-case scheduler can construct incompatible certificates;
- deterministic local scalar hardening cannot improve optimal decision risk,
  and it is strictly worse when a hardening fiber merges observations with
  different optimal actions;
- fragment count and one-fragment accuracy do not determine reliability:
  IID evidence concentrates, while an equal-marginal common-shock channel has
  a nonzero error floor;
- a metastable confidence crossing can roll back before a separately supplied
  absorbing finality boundary;
- threshold reconstruction, dissemination, consistency, public knowledge,
  finality, and capability are not interchangeable; and
- the GHZ phase pair is an exact three-of-three access structure for one
  classical bit, but local \(X\) measurements plus authenticated parity
  pooling suffice. It is neither general quantum secret sharing, quantum
  fault tolerance, redundant objectivity, nor public finality.

The result is scientifically useful because it kills an attractive but
misleading unification:

```text
more fragments
    -> one universal threshold
    -> objective fact
    -> capability
```

The surviving architecture is:

```text
formed evidence + dependence/provenance model
    -> action-relevant reconstruction
authenticated access + honest-intersection locking
    -> incompatible-certificate safety
rollback/cost/resource contract
    -> bounded-risk public capability
```

No component theorem is novel. The static quantum/BFT access conjunction also
collides with mature prior work. The next credible contribution is therefore
not another threshold theorem. It is a quantitative
**formation-to-finality resource bound** on converting a physically selected,
synergy-only or private distinction into a redundant, fork-safe,
independently accessible, action-enabling public fact.

## 1. Frozen typed contract

### 1.1 Reconstruction

Let \(H\) be a finite declared history label with prior \(\pi\). A coalition
receives a direct channel \(X\) whose outputs include every retained
reliability and provenance field. A local-hardening architecture applies a
declared channel

\[
T:X\to Y
\]

before coalition aggregation. Reconstruction is always relative to:

- the history or action-relevant quotient being reconstructed;
- the supplied channel and dependence model;
- the admitted decoder;
- a loss function or error threshold; and
- the access, disturbance, latency, and resource contract.

A count without those objects is not a reconstruction threshold.

### 1.2 Finality

Let \(V\) contain \(N\) authenticated validators. At most \(f\) are Byzantine.
A certificate for one of two incompatible histories contains \(q\) distinct
signers. In one frozen finality instance:

- an honest validator signs or locks at most one incompatible history;
- a Byzantine validator may support both;
- signatures are authenticated and replay or aliases do not add signers; and
- the theorem concerns same-instance safety, not view-change liveness.

### 1.3 Capability

The action family, actuator access, loss table, verification cost, reversal
risk, and resource bound are fixed before outcomes.

Two capabilities remain distinct:

- **action-relevant capability:** some evidence quotient makes a local or
  reversible action admissible;
- **public irreversible capability:** the action-relevant condition holds
  and the required public-finality contract also holds.

Under this contract,

\[
C_{\mathrm{public}}
=
F\wedge C_{\mathrm{action}}.
\]

That implication is definitional, not an empirical discovery. Complete
history reconstruction is not generally necessary: an action may depend on a
proper quotient of history.

## 2. Exact finality results

### Theorem 1 — equal-size locked-quorum safety and converse

For any two size-\(q\) quorums \(Q_0,Q_1\subseteq V\),

\[
|Q_0\cap Q_1|\ge 2q-N.
\]

Incompatible certificates are impossible under the frozen honest-locking
contract exactly when

\[
2q-N>f,
\]

or equivalently

\[
\boxed{2q>N+f}.
\]

The minimum safe integer threshold is

\[
q_{\min}
=
\left\lfloor\frac{N+f}{2}\right\rfloor+1.
\]

#### Proof

The union of two quorums contains at most \(N\) validators, so

\[
|Q_0\cap Q_1|
=|Q_0|+|Q_1|-|Q_0\cup Q_1|
\ge 2q-N.
\]

If \(2q-N>f\), every intersection contains at least one honest validator.
That validator cannot support both incompatible histories, so two
certificates cannot exist.

Conversely, if \(2q\le N+f\), set

\[
t=\max(0,2q-N)\le f.
\]

Choose an overlap \(B\) of \(t\) Byzantine validators and disjoint sets
\(A,C\), each of size \(q-t\). Then

\[
Q_0=B\cup A,\qquad Q_1=B\cup C
\]

are size-\(q\) quorums whose entire overlap can equivocate. Every honest
validator still signs only one history. \(\square\)

The executable canonical split view is

```text
N=3, f=1, q=2
Q0={B,H0}
Q1={B,H1}.
```

The canonical safe and withholding-available control is

```text
N=4, f=1, q=3.
```

### Safety and availability are different

If every faulty validator may remain silent, availability also requires

\[
q\le N-f.
\]

A safe threshold and worst-case withholding availability coexist exactly
when \(N\ge3f+1\). A larger \(q\) may improve intersection safety while
destroying availability.

### Theorem 2 — stochastic honest-lock margin

Suppose \(D\) validators outside the declared Byzantine set suffer
instance-specific double-sign failures. Define

\[
\boxed{h=\max(0,2q-N-f)}.
\]

Under worst-case scheduling, incompatible size-\(q\) certificates are
combinatorially possible exactly when

\[
D\ge h.
\]

#### Proof

Two quorums need at least \(\max(0,2q-N)\) common validators. At most \(f\) of
those can come from the declared Byzantine set. Every remaining common
validator must violate the honest lock. The minimum required number is
\(\max(0,2q-N-f)\). The converse construction in Theorem 1 works after adding
exactly those \(h\) double-signing honest validators to the shared set.
\(\square\)

If the \(N-f\) honest lock failures are IID with probability \(\lambda\), the
probability that an adversary has enough failed locks to make a conflict
structurally possible is the exact binomial tail

\[
\Pr(\text{conflict possible})
=
\Pr[\operatorname{Bin}(N-f,\lambda)\ge h].
\]

This is a worst-case-scheduler possibility probability, not an ordinary
execution frequency.

The probe uses \(N=10,f=2,q=7\). Then \(h=2\): one honest double-sign failure
is tolerated, two make conflicting certificates constructible. With
\(\lambda=1/100\):

```text
IID honest-lock failures:
    P(conflict possible)
    = 26900777395207 / 10^16
    ~= 0.00269008

same one-validator marginal, common-mode lock bug:
    P(conflict possible)
    = 1/100
```

Correlation changes finality risk just as it changes reconstruction risk.

Under both deterministic safety and worst-case availability
\(q\le N-f\),

\[
h\le N-3f.
\]

At the minimal resilient size \(N=3f+1\), a live protocol has at most
\(h=1\): one additional honest double-sign failure can destroy safety.

## 3. Exact hardening result

### Theorem 3 — deterministic hardening cannot improve Bayes risk

For finite hidden history \(H\), raw observation \(X\), deterministic
hardening \(Y=T(X)\), prior \(\pi\), and zero-one loss, let

\[
R_X^*
=
1-\sum_x\max_h p(h,x)
\]

and

\[
R_Y^*
=
1-\sum_y\max_h
\sum_{x:T(x)=y}p(h,x).
\]

Then

\[
\boxed{R_X^*\le R_Y^*}.
\]

#### Proof

For each hardening fiber,

\[
\max_h\sum_{x:T(x)=y}p(h,x)
\le
\sum_{x:T(x)=y}\max_h p(h,x).
\]

Summing over \(y\) gives the result. Any decoder on \(Y\) can also be pulled
back to a decoder on \(X\), so hardening cannot enlarge the decision set.
\(\square\)

For zero-one loss, equality holds exactly when every positive-probability
hardening fiber has a common Bayes-optimal history:

\[
\forall y,\quad
\bigcap_{x\in T^{-1}(y),\,p(x)>0}
\arg\max_h p(h,x)\ne\varnothing.
\]

For a general loss, replace “history” with “Bayes action.” Equality across
every decision problem is the stronger Blackwell-sufficiency condition.

### Strict reliability-erasure fixture

Let \(H\in\{-1,+1\}\) be uniform. Each of two independent fragments has a
visible reliability type \(S\) or \(W\), each with probability \(1/2\):

\[
\Pr(Z=H\mid S)=\frac9{10},
\qquad
\Pr(Z=H\mid W)=\frac35.
\]

The joint raw channel retains both type and sign. Local scalar hardening
retains only the sign.

Exact optimal errors are:

```text
raw, reliability-preserving aggregation:  7/40
locally sign-hardened aggregation:         1/4
strict loss:                               3/40
```

The probe also enumerates every one of the 16 binary local maps on the four
single-fragment outcomes. None beats the raw channel.

This is not a theorem that local decisions are intrinsically bad. The exact
conclusion is:

> Local scalarization is lossless for a declared decision problem exactly
> when it preserves an action-sufficient statistic. Deleting
> action-relevant confidence or provenance can be strictly lossy.

Local hardening may still buy bandwidth, privacy, latency, or fault
containment. Those resources must be compared rather than ignored.

## 4. Correlation no-go for fragment counts

### Theorem 4 — equal marginal accuracy, unequal accumulation

For odd \(n\), let IID fragments be correct with probability \(p>1/2\).
Majority error is

\[
E_n^{\mathrm{iid}}(p)
=
\sum_{k=0}^{(n-1)/2}
{n\choose k}p^k(1-p)^{n-k}.
\]

It obeys the declared IID concentration bound

\[
E_n^{\mathrm{iid}}(p)
\le
\exp[-2n(p-1/2)^2].
\]

Now use a common-shock channel. With probability \(\rho\), every fragment
shares one correctness bit whose accuracy is \(p\); otherwise all fragments
are IID with the same \(p\). Every one-fragment marginal remains unchanged,
but

\[
E_n^{\mathrm{shock}}
=
\rho(1-p)+(1-\rho)E_n^{\mathrm{iid}}(p)
\longrightarrow
\rho(1-p).
\]

Therefore fragment count and one-fragment accuracy do not determine
reconstruction reliability, its exponent, or whether any capability-risk
threshold is eventually crossed. \(\square\)

The probe uses \(p=3/4,\rho=1/5\), giving an exact error floor \(1/20\).

This no-go applies equally to aliases, Sybils, duplicated messages, and a
giant connected component that disseminates one correlated mistake. A law of
large numbers needs an independence, mixing, dependency-graph, martingale, or
other explicit dependence contract.

## 5. Layer separation

### Theorem 5 — reconstruction, finality, and capability are not equivalent

Finite fixtures realize every truth vector

\[
(R,F,C_{\mathrm{action}})\in\{0,1\}^3.
\]

Let the full history be \(H=(G,J)\), uniform on two bits.

- `none` reveals neither bit; full-history Bayes error is \(3/4\).
- `coarse` reveals \(G\); full-history Bayes error is \(1/2\).
- `full` reveals both bits; full-history Bayes error is \(0\).

Define full reconstruction as zero-error recovery of \((G,J)\). A directional
actuator needs only \(G\), returns benefit \(1\), costs \(1/4\), and admits
zero decision error. Therefore `coarse` evidence enables the action without
reconstructing full history. Toggle safe versus unsafe quorums and enabled
versus disabled actuators to obtain all eight truth vectors.

This proves:

- safe finality need not be truthful;
- accurate private reconstruction need not prevent conflicting public
  certificates;
- action-relevant sufficiency may require less than complete-history
  reconstruction;
- reconstruction plus finality does not create an actuator or make its cost
  favorable; and
- public irreversible capability additionally requires the declared
  finality condition.

The theorem is elementary. Its value is to prevent a false scalar
identification, not to claim novel logic.

### Numeric action-risk control

For IID accuracy \(p=3/4\):

```text
first odd n with majority error <= 1/10:  n=7
first odd n with majority error <= 1/50:  n=15
```

Even within one evidence family, a coarse reconstruction standard and a
stricter action-risk standard cross at different sample counts.

## 6. Access, topology, and metastability controls

### Threshold access is not consistency

Over \(\mathbb F_5\), use the apparent two-of-three shares

```text
(1,0), (2,0), (3,1).
```

The first pair interpolates a degree-one polynomial with secret \(0\). The
second pair interpolates one with secret \(3\). Both authorized coalitions
reconstruct, but they reconstruct incompatible values.

Dealer consistency, verifiable secret sharing, honest-intersection semantics,
or another validation layer is additional structure.

### Safety is not dissemination

For \(N=7,f=2,q=5\), the locked-quorum condition is safe. A complete
communication graph can gather five reports. A graph split into components of
sizes four and three cannot. Safety did not provide dissemination,
availability, timing, or common knowledge.

### Replay is not support

The apparent signer list

```text
A, A, B
```

has three messages and only two authenticated provenance roots. It does not
satisfy a three-signer quorum.

### Confidence is not finality

Use a biased random walk on states \(0,1,2,3\), stepping upward with
probability \(2/3\). Announce confidence on reaching state \(2\); make state
\(3\) a separately supplied absorbing hard-final boundary.

Starting at state \(2\):

```text
immediate fall below confidence:          1/3
full rollback to 0 before hard finality:  1/7
```

The absorbing boundary, not confidence magnitude, supplies finality. In a
finite irreducible chain, a high-confidence state eventually escapes.

Adaptive sampling creates an additional hazard: a fixed-horizon confidence
bound is invalid when a process repeatedly samples until it sees a favorable
crossing. An anytime-valid or preregistered stopping contract is required.

## 7. Quantum controls and the correction they force

### GHZ phase: exact access-only null

Let

\[
|\psi_s\rangle
=
\frac{|000\rangle+s|111\rangle}{\sqrt2},
\qquad
s\in\{+1,-1\}.
\]

Every proper-subset reduced state is

\[
\rho_s^S
=
\frac12\left(
|0^{|S|}\rangle\!\langle0^{|S|}|
+
|1^{|S|}\rangle\!\langle1^{|S|}|
\right),
\]

independent of \(s\). The full states are orthogonal.

However,

\[
X\otimes X\otimes X|\psi_s\rangle=s|\psi_s\rangle.
\]

Each party can measure \(X\) locally and publish \(x_i\in\{-1,+1\}\); the
pooled parity

\[
s=x_1x_2x_3
\]

recovers the phase exactly.

The exact grade is:

```text
3-of-3 access to one classical phase label
proper subsets individually uninformative
no erasure tolerance
one malicious report can flip the parity
local measurements plus classical pooling suffice
no general quantum-secret encoding
no redundant objectivity
no finality or capability result
```

This makes GHZ a particularly useful negative control:

```text
perfect authorized-set reconstruction
    does not imply redundancy
    does not imply fault tolerance
    does not imply finality
    does not imply public objectivity
    does not imply capability.
```

### Bell-basis direct-channel control

The probe also checks all four Bell states. Every one-qubit marginal is
maximally mixed, while a direct joint Bell-basis measurement distinguishes
all four exactly.

That verifies the direct-channel-versus-marginal distinction required by
`HC-DU-033A`. The probe does not prove an LOCC impossibility. Any such claim
must use the relevant quantum discrimination literature rather than infer it
from equal marginals alone.

Neither quantum fixture supplies a broadcastable public algebra. A positive
objectivity fixture must add redundant independently accessible records, such
as a spectrum-broadcast-like structure, and then expose its formation,
disturbance, adversarial, and resource costs.

## 8. What the ten lenses uniquely contributed

| Lens | Surviving contribution | What it prevents |
|---|---|---|
| Threshold cryptography | Access threshold and inconsistent-share control | reconstruction called consistency |
| Byzantine quorum systems | exact \(2q>N+f\) safety and converse | readability called finality |
| Coding and soft decisions | hardening risk inequality and equality criterion | early scalarization treated as free |
| Quantum fault tolerance/access | GHZ access-only correction and Bell joint channel | access called QEC or objectivity |
| Large deviations | exact IID tail and explicit assumption boundary | count alone called reliability |
| Metastability | \(1/7\) rollback control | confidence called finality |
| Percolation/hypergraphs | access and dissemination depend on topology | quorum size treated as complete |
| Critical phenomena | scaling limit and order parameter remain required | finite knee called a phase transition |
| Gossip/provenance | paths, copies, replay, and roots remain distinct | message count called independent evidence |
| Adversarial reliability | honest-lock surplus \(h\) and common-mode risk | marginal failure rate treated as a system guarantee |

## 9. Exact executable receipt

`tests/du_layered_threshold_objectivity_probe.py` uses only the Python
standard library and exact `Fraction` arithmetic for every finite
probability, field, quorum, and density-matrix calculation.

It checks:

- all \(240\) \((N,f,q)\) cases through \(N=8\) and every quorum pair;
- the exact converse split-view construction;
- safety versus withholding availability;
- the stochastic honest-lock margin and IID/common-mode comparison;
- all 16 binary local hardenings of the strict reliability fixture;
- IID majority tails, Hoeffding controls, and the common-shock floor;
- distinct reconstruction and action-risk crossings;
- the four named layer countermodels and the full eight-vector truth cube;
- exact \(1/7\) metastable rollback;
- topology, replay/Sybil provenance, and inconsistent secret-sharing nulls;
- all GHZ proper-subset reductions and local-\(X\) parity recovery;
- all Bell single-qubit marginals and joint Bell-projector outcomes; and
- the explicit non-promotion of a finite threshold to criticality.

All `23/23` named checks pass.

## 10. Scientific disposition

### Close

Close the scalar threshold hypothesis:

```text
ONE UNIVERSAL OBJECTIVITY THRESHOLD = REJECTED
```

Close the current finite sub-result at:

```text
LAYERED RECONSTRUCTION / FINALITY / CAPABILITY SEPARATION EXACT
CLASSICAL LOCKED-QUORUM CONTROL EXACT
STOCHASTIC HONEST-LOCK MARGIN EXACT
LOCAL-HARDENING LOSS FIXTURE EXACT
IID / COMMON-SHOCK ACCUMULATION SEPARATION EXACT
GHZ CLASSICAL-PHASE ACCESS CONTROL EXACT
BELL DIRECT-JOINT-CHANNEL CONTROL EXACT
COMPONENT MATHEMATICS KNOWN
STATIC CROSS-PLATFORM CONJUNCTION NOT NOVEL
NO CLAIM BANKED OR SEEDED
```

### Keep open

- physical formation and selection of the record interface;
- multi-time causal provenance rather than terminal labels;
- view changes, timing, liveness, and common knowledge;
- noisy quantum channels, malicious shares, and approximate decoding;
- formation of a stable approximately commutative or broadcastable public
  algebra;
- exact resource, coherence, entropy, latency, memory, and authentication
  costs;
- public capability after those costs; and
- one unchanged theorem across a physical quantum fixture and an adversarial
  distributed fixture.

### Next meaningful swing

Execute `HC-DU-035B — Formation-to-Finality Cost`.

Compare, under one frozen physical channel:

1. a synergy-only encoded distinction, using GHZ-like access as the negative
   control;
2. a redundant independently accessible record structure, using a
   spectrum-broadcast or verifiable-access positive control; and
3. an adversarial distributed realization with the same typed access,
   incompatibility, finalizer, and action contract.

The target is a lower bound or necessary-and-sufficient condition on the
additional disturbance, support, memory, redundancy, authentication, latency,
entropy, or coherent optionality required to obtain:

```text
fork-safe
+ independently accessible
+ bounded-risk actionable
```

from a physically formed distinction.

If the result is only an intersection of Blackwell sufficiency, secret-sharing
access, and quorum safety, stop. Advancement requires a coupled resource bound,
a physical selection result, or a finite intervention that separates two
equal-record candidates.
