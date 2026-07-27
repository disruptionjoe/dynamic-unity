---
title: "Joint-input no-minting, synergistic recovery, and dependency-sensitive amplification"
status: completed_scoped_result
doc_type: exact_finite_theorem_counterexample_and_protocol_boundary
created: 2026-07-27
claim_id: HC-DU-047
run_id: N5-SCF-P1
authority: "Joe direct chat: Go"
claim_status_change: "N5-SCF-P1 complete as HC-DU-047; N5-SCF-P2 executable"
paper_state_change: none
hardware_state_change: none
provider_state_change: none
local_model_gate: proof_certificate_outside_research_model_admission
---

# Joint-input no-minting, synergistic recovery, and dependency-sensitive amplification

## Executive result

The first stochastic/consensus/finality swing corrects the question before
answering it.

This tempting statement is false:

> A network cannot recover a distinction that no participant individually
> possesses.

Secret sharing and XOR synergy are exact counterexamples. Each participant's
record can be individually independent of a target while the joint record
determines it perfectly.

The correct boundary is:

> A downstream protocol cannot recover a target distinction that is absent
> from the **entire joint admitted input channel**.

If participant inputs are all downstream of a common record \(Q\), then any
gossip, vote, DAG, threshold certificate, zero-knowledge transcript,
homomorphic computation, or multiparty output built only from those inputs is
also downstream of \(Q\). If a target is not constant on the fibres of \(Q\),
no such layer can make it exact.

When target-sensitive information is present in the joint input, population
and protocol layers can do important work:

- independent observations can exponentially reduce error;
- correlated or duplicated observations can leave a nonzero error floor;
- jointly encoded shares can reveal a target absent from every individual
  marginal;
- shared environmental traces can make one formed mark widely accessible
  without repairing errors in the formation of that mark;
- authenticated or threshold certificates can change authority and safe
  action without certifying independent evidence origins; and
- adversarial routing can defeat a sample-size guarantee without changing
  population size.

There is consequently no universal “effective number of observers” obtained
from raw \(N\), marginal accuracy, and pairwise correlation alone. Exact
amplification depends on the higher-order joint law, source origins, sampler,
topology, and adversary.

The result is a scoped Dynamic Unity classification built from known
factorization, Blackwell/data-processing, concentration, limited-independence,
secret-sharing, and cryptographic functionality mathematics. It is not a new
consensus theorem, cryptographic primitive, emergence law, physical ontology,
or prediction.

## 1. Plain-English interpretation

Many observers can help for three very different reasons:

1. **Independent evidence.** Each observer obtains a fresh noisy look at the
   target. Majority voting can average away independent noise.
2. **Complementary evidence.** Different observers receive different pieces
   whose correlations encode the answer. No one piece is sufficient, but the
   tuple is.
3. **Replication and certification.** Many observers copy, authenticate, or
   agree on one already-formed trace. This improves availability, integrity,
   disclosure control, or action safety, but not the trace's source
   information.

Those cases cannot be inferred from headcount. They must be typed from the
formation and dependency structure.

This changes Dynamic Unity's working language. “Every observer lost the
distinction” is not a sufficient hostile premise. The required premise is
that two target-different histories induce the same **joint** admitted input,
or the same joint-input law. Only then does downstream no-minting follow.

## 2. Frozen typed contract

Let:

- \(H\) be a hidden history or source state;
- \(T=t(H)\) be a held-out target;
- \(Q=q(H)\) be a finest common source record when one exists;
- \(R=(R_1,\ldots,R_N)\) be the complete tuple of admitted participant
  inputs;
- \(U\) be protocol randomness;
- \(C\) be the final certificate, output, or action-enabling record;
- \(S\) be the sampling/routing rule;
- \(A\) be the adversary contract; and
- \(\mathcal D\) be the declared decision or action class.

The contract freezes:

1. the source-to-record channels;
2. which correlations among participant records are admitted;
3. whether \(U\) is independent of \(H\) conditional on \(R\);
4. the sampler, topology, timing, membership, authentication, and fault
   model;
5. the target before the protocol is chosen; and
6. whether the claim concerns exact reconstruction, Bayes/minimax risk,
   agreement, provenance, common knowledge, disclosure, or action safety.

Changing any of these can be a valid new construction. It is not a repair of
the old theorem under unchanged premises.

## 3. Deterministic joint-input no-minting theorem

### Theorem

Let \(\Omega\) be a set of histories and suppose:

\[
R=f\circ Q,
\qquad
C=g\circ R.
\]

Then:

\[
C=(g\circ f)\circ Q.
\]

If a target \(T\) factors through \(C\), it also factors through \(Q\).
Equivalently:

\[
\ker Q\subseteq\ker C\subseteq\ker T.
\]

Therefore, if:

\[
\exists h_0,h_1:
Q(h_0)=Q(h_1),
\qquad
T(h_0)\ne T(h_1),
\]

no downstream certificate \(C\) can reconstruct \(T\).

### Proof

Composition gives \(C=g\circ f\circ Q\). If \(T=k\circ C\), then
\(T=k\circ g\circ f\circ Q\). Thus \(T\) is constant on every \(Q\)-fibre,
contradicting the witness. \(\square\)

### What the theorem covers

The map \(g\) may represent:

- deterministic aggregation or majority;
- gossip or DAG processing;
- a BFT state machine;
- a threshold-opening or signing function;
- a homomorphic or MPC evaluation;
- a deterministic verifier; or
- any composition of those functions.

The theorem does not say these operations are useless. It says they cannot
make an omitted target distinction appear without a new target-sensitive
input.

## 4. Stochastic no-improvement theorem

### Kernel form

Suppose the architecture is the Markov chain:

\[
H\longrightarrow Q\longrightarrow R\longrightarrow C.
\]

Then there are fixed kernels \(K_R\) and \(K_C\) such that:

\[
P(C\in dc\mid H=h)
=
\int K_C(dc\mid r)K_R(dr\mid q)\,P_Q(dq\mid h).
\]

If two histories induce the same \(Q\)-law, they induce the same \(C\)-law.
No test of \(C\) distinguishes them.

### Decision form

Because \(C\) is a garbling of \(Q\), \(Q\) Blackwell-dominates \(C\). For
every prior, loss function, and decision rule class admitted by the
experiment:

\[
\inf_{\delta_Q}\mathbb E[L(T,\delta_Q(Q))]
\le
\inf_{\delta_C}\mathbb E[L(T,\delta_C(C))].
\]

For binary exact reconstruction, a positive-prior same-\(Q\) target
disagreement gives positive zero-one risk downstream.

### Exact finite control

The certificate uses:

\[
\begin{array}{c|cc}
 & Q=0 & Q=1\\\hline
T=0 & 3/8 & 1/8\\
T=1 & 1/8 & 3/8
\end{array}
\]

The Bayes risk from \(Q\) is \(1/4\). Exhausting 25 binary stochastic
garblings with conditional probabilities in
\(\{0,\tfrac14,\tfrac12,\tfrac34,1\}\) finds no smaller risk.

### Necessary premise

If protocol randomness remains target-sensitive after conditioning on \(Q\),
then:

\[
H\not\!\perp U\mid Q.
\]

The Markov premise has failed. \(U\) is a new input channel, pre-correlated
oracle, measurement result, or physical record. Calling it “randomness” does
not make it downstream.

## 5. The individual-insufficiency counterexample

### XOR witness

Let \(T,U\) be independent uniform bits and define:

\[
R_1=U,
\qquad
R_2=T\oplus U.
\]

Then:

\[
I(T;R_1)=I(T;R_2)=0,
\]

and each individual observer's optimal error is \(1/2\). Jointly:

\[
T=R_1\oplus R_2,
\qquad
H(T\mid R_1,R_2)=0.
\]

The joint tuple contains synergistic target information that no individual
marginal contains.

### Threshold-secret-sharing control

For secret \(s\in\mathbb F_5\), choose uniform \(a\in\mathbb F_5\) and form:

\[
y_i=s+a x_i\pmod 5,
\qquad
x_i\in\{1,2,3\}.
\]

Every one-share distribution is uniform and independent of \(s\). Every
two-share pair determines the unique affine line and reconstructs \(s\).

This is the correct interpretation of threshold recovery:

> The protocol does not create the secret. The source encoded it in a joint
> correlation whose authorized subsets can decode it.

### Consequence for Dynamic Unity

The following hostile claim is invalid:

```text
no node individually records historical occurrence
therefore no regional certificate can recover occurrence
```

The valid claim must establish one of:

```text
the complete joint native record has a same-record/different-target witness
the admitted joint record law is target-indistinguishable
the required correlation exists only in an excluded environment or completion
the target-sensitive provenance/correlation is supplied rather than formed
```

This is the most important correction from Position 1.

## 6. When a large population really amplifies

Let \(X_i\) be binary correctness indicators for a uniform target.

### IID positive control

For odd \(N\), independent observations with accuracy \(p>1/2\) have majority
error:

\[
e_N(p)
=
\sum_{k=0}^{(N-1)/2}
\binom Nk p^k(1-p)^{N-k}.
\]

At \(p=3/4\), the exact certificate shows strictly decreasing error for:

\[
N\in\{1,3,5,9,15\}.
\]

Hoeffding/Chernoff bounds give the familiar exponential tail under their
independence or controlled-dependence premises.

### Duplicated-origin control

If every participant receives the same noisy bit:

\[
X_1=\cdots=X_N=X,
\]

majority is exactly \(X\). Error does not decrease with \(N\).

Duplicating one record, including through benign Sybil splitting, changes
replica count but not evidence-origin rank.

### Common-shock control

If:

\[
X_i=T\oplus B
\quad\text{for all }i,
\qquad
P(B=1)=\epsilon,
\]

then majority error equals \(\epsilon\) for every odd \(N\). The law of large
numbers cannot average away a perfectly shared formation error.

### Clustered-origin control

Suppose \(m\) independent decisions are each copied \(k\) times, with equal
odd \(k\). Majority over \(mk\) replicas is majority over the \(m\) origins.

For three independent origins of accuracy \(3/4\), each copied five times:

\[
P(\text{majority wrong})=\frac5{32}.
\]

Fifteen independent origins with the same accuracy have a far smaller error.
Both systems have \(N=15\).

## 7. Why no universal effective-support scalar is earned

Raw \(N\) fails, but replacing it with a scalar built from accuracy and
pairwise correlation also fails in general.

Consider three exchangeable correctness bits. Let \(K\) be the number
correct. Conditional on \(K=k\), distribute probability uniformly over the
\(\binom3k\) configurations. Compare:

\[
\begin{array}{c|cccc|c}
 & P(K=0)&P(K=1)&P(K=2)&P(K=3)&P(K\le1)\\\hline
A&1/54&15/54&21/54&17/54&8/27\\
\mathrm{IID}&1/27&6/27&12/27&8/27&7/27\\
B&3/54&9/54&27/54&15/54&2/9
\end{array}
\]

All three laws have:

\[
\mathbb E[K]=2,
\qquad
\mathbb E[K(K-1)]=\frac83.
\]

Thus each bit has accuracy \(2/3\), and every pair has joint correctness
probability:

\[
\frac{\mathbb E[K(K-1)]}{3\cdot2}=\frac49
=
\left(\frac23\right)^2.
\]

The bits are pairwise independent in every law, yet the majority-error
probabilities differ.

Therefore:

> Marginal accuracy and all pairwise correlations do not determine a
> threshold tail. Higher-order dependence matters.

“Effective support” can be useful only relative to a frozen model—for
example, an explicit cluster graph, dependency graph, mixing process,
exchangeable mixing measure, or adversarial origin model. It is not a
universal scalar invariant.

## 8. Stigmergic trace formation versus readout

Let a source target \(T\) form one environmental mark:

\[
M=T\oplus B_0,
\qquad
P(B_0=1)=\delta.
\]

Let \(N\) independent readers each observe \(M\) with error \(\epsilon<1/2\),
and let \(e_N(\epsilon)\) be majority error in reconstructing \(M\).

The final target error is exactly:

\[
\begin{aligned}
P(\widehat T\ne T)
&=P(M=T)P(\widehat M\ne M)
  +P(M\ne T)P(\widehat M=M)\\
&=(1-\delta)e_N+\delta(1-e_N)\\
&=\delta+(1-2\delta)e_N.
\end{aligned}
\]

As \(N\) grows, \(e_N\to0\), but:

\[
P(\widehat T\ne T)\to\delta.
\]

Many readers harden access to the mark. They do not repair its formation
error.

This makes the DU archive boundary explicit:

- mark formation is a source-to-archive operation;
- replication/readout is downstream accessibility;
- evaporation and overwriting change retention;
- forgery changes integrity;
- common readability does not by itself establish common knowledge; and
- no number of readers selects why this physical mark, rather than another
  interface, formed.

## 9. Sampling and topology are theorem premises

Consider a population of nine nodes: six carry the correct value and three
the wrong value. A size-three sample drawn uniformly without replacement has
majority-wrong probability:

\[
\frac{\binom32\binom61+\binom33\binom60}{\binom93}
=
\frac{19}{84}.
\]

An eclipse route that supplies exactly the three wrong nodes has error one.

The population and sample sizes are identical. The sampler/topology differs.
Consequently, an Avalanche-style or other repeated-subsampling guarantee must
consume:

- a sampling-distribution premise;
- a bound on adversarial population and routing control;
- topology/mixing assumptions;
- timing/churn assumptions; and
- a dependence model across repeated samples.

Observed confidence accumulation does not prove those premises.

## 10. Cryptographic corollaries and limits

### Zero knowledge

An ideal zero-knowledge proof can let a verifier act on:

```text
there exists a witness satisfying the declared relation
```

without disclosing the witness. This is a real capability change.

If two physical histories yield the same statement and simulated transcript
but differ on an omitted physical target, the proof does not reconstruct that
target. Completeness and soundness apply to the declared relation and setup;
faithful physical formation or attestation is another premise.

### Homomorphic encryption and multiparty computation

FHE/MPC can compute:

\[
f(R_1,\ldots,R_N)
\]

without any one party seeing the full tuple. It can therefore recover the XOR
or secret-sharing synergy above.

It cannot recover a target that is nonconstant on the fibres of the entire
tuple \(R\). Privacy-preserving computation is computation without
individual access, not information creation.

### Threshold cryptography

A threshold signature or opening proves that the declared authorization
condition was met under its key-generation, corruption, and verification
contract. It need not reveal:

- whether shares came from independent evidence origins;
- whether one controller split itself into many keys;
- which physical event formed each signer's input;
- whether the signed statement exhausts the underlying history; or
- whether the setup was unbiased and independently generated.

The finite certificate uses two histories with the same valid threshold
signature and different control-origin ranks. The signature is sufficient
for the authorized action and insufficient for the provenance target.

### Cryptographic conclusion

Cryptography can change:

- who can learn;
- who must cooperate;
- what can be verified;
- what remains private;
- who can authorize an action; and
- how tampering/equivocation is detected.

It cannot by itself certify that its admitted inputs are complete, independent
physical records. That arrow remains a physical formation and provenance
problem.

## 11. Emergence and scaling grade

The IID majority family, common-shock floor, clustered-origin control, and
stigmergic trace are all fully determined by their declared microprocesses.
They support:

```text
WEAK_COLLECTIVE_EMERGENCE
ENGINEERED_THRESHOLD_OR_CROSSOVER
ACTION_USEFUL_MACRO_VARIABLE
```

where appropriate.

They do not support:

```text
STRONG_EMERGENCE
UNIVERSALITY_CLASS
NEW_CAUSAL_POWER
NEW_PHYSICS
```

A finite sigmoid or confidence knee is insufficient. A criticality claim
would additionally need a system-size family, order parameter, finite-size
shift/rounding, correlation or susceptibility scale, topology/boundary
controls, and a scaling collapse or another invariant characterization.

## 12. Collision with `HC-DU-046`

`HC-DU-046` proved that the metastable host's terminal matter record omits
historical occurrence and that redundant terminal-value copies preserve the
failure.

`HC-DU-047` strengthens and corrects how that result may be reused:

1. **Valid negative.** If every participant input is a function or garbling
   of terminal matter, the entire joint tuple remains terminal-matter
   measurable. No aggregation or certificate repairs occurrence.
2. **Invalid overreach.** It is not enough to show that no participant
   individually reconstructs occurrence. An environment could form
   complementary shares whose tuple reconstructs it.
3. **Positive route.** A distributed history archive may exist as
   source-formed joint correlations even when no local record is sufficient.
4. **Unchanged burden.** The host must still select/form the complementary
   channels, correlation, provenance, retention, access, and threshold
   contract. Supplying a secret-sharing encoder does not solve endogenous
   record formation.

The first host remains closed adversely. The broader North-Star program gains
a sharper candidate route: do not search only for one local sufficient
archive; search for physically formed, provenance-bearing **joint
sufficiency** across regional records.

## 13. Position-2 branch decision

Position 1 succeeds and makes the next work object executable:

```text
N5-SCF-P2
Synergy-Preserving Gossip/DAG Provenance and Knowledge
```

The smallest informative arena must contain both:

1. a **synergy world** with source-formed complementary records
   \(R_1=U,\ R_2=T\oplus U\); and
2. a **null world** with locally identical uniform records but no
   target-binding joint correlation.

The Position-2 question is:

> What must signed gossip or a hash-DAG preserve for the network to
> distinguish source-formed joint sufficiency from coincidental, copied, or
> target-independent values—and which provenance or common-knowledge target
> remains absent unless it was present in the source event?

The unchanged comparison will track:

- value delivery;
- signed origin;
- source-formation relation;
- causal ancestry;
- equivocation evidence;
- distributed knowledge;
- common knowledge;
- total ordering;
- target reconstruction; and
- action sufficiency.

Plain gossip, signed gossip, hash-DAG ancestry, and one commitment or
zero-knowledge ancestry proof will use the same event set and fault model.
Delivered endpoint values will be held fixed while routes, duplicated
origins, and target-binding provenance vary.

The stop is exact:

```text
do not build a network simulator
do not call a DAG a physical causal set
do not infer source truth from a signature
stop after a finite factorization theorem or smallest route/provenance counterexample
```

## 14. Evidentiary grade

### Earned

```text
SCOPED GRADE-4 JOINT-INPUT NECESSITY CLASSIFICATION
EXACT FINITE SYNERGY / DEPENDENCE / STIGMERGY / SAMPLING / CRYPTOGRAPHIC CONTROLS
```

This means exact in the declared finite or general factorization contracts.

### Absorbers

The component mathematics is substantially absorbed by:

- ordinary function factorization and the data-processing inequality;
- Blackwell comparison of statistical experiments;
- Hoeffding/Chernoff and limited-independence concentration;
- multivariate synergy and partial-information-decomposition literature;
- Shamir secret sharing and threshold cryptography;
- zero-knowledge, FHE, and MPC functionality definitions;
- dependency-graph, exchangeability, and adversarial-sampling theory; and
- distributed knowledge/protocol literature.

Dynamic Unity's possible contribution is the typed synthesis across physical
record formation, joint sufficiency, provenance, capability, and layered
finality—not the component theorems.

### Not earned

No:

- universal scalar law of observer support;
- consensus or cryptographic novelty;
- strong emergence;
- physical record selector;
- quantum or QFT delta;
- new law or ontology;
- prediction;
- paper promotion;
- external hardware need; or
- provider action.

## 15. Primary literature boundary

- Blackwell's comparison of experiments supplies the statistical-garbling
  order used by the stochastic theorem:
  [Equivalent Comparisons of Experiments](https://doi.org/10.1214/aoms/1177729032).
- Hoeffding supplies the independent bounded-variable concentration baseline:
  [Probability Inequalities for Sums of Bounded Random Variables](https://doi.org/10.1080/01621459.1963.10500830).
- Schmidt, Siegel, and Srinivasan show that useful Chernoff--Hoeffding bounds
  can survive specified limited independence, while still requiring an
  explicit dependence contract:
  [Chernoff--Hoeffding Bounds for Applications with Limited Independence](https://doi.org/10.1137/S089548019223872X).
- Williams and Beer give one formal multivariate-information account of
  synergy:
  [Nonnegative Decomposition of Multivariate Information](https://arxiv.org/abs/1004.2515).
  The exact XOR counterexample does not depend on accepting one unique
  partial-information measure.
- Shamir supplies the threshold-secret-sharing control:
  [How to Share a Secret](https://doi.org/10.1145/359168.359176).
- Goldwasser, Micali, and Rackoff supply the zero-knowledge distinction:
  [The Knowledge Complexity of Interactive Proof Systems](https://doi.org/10.1137/0218012).
- Gentry supplies the FHE functionality control:
  [Fully Homomorphic Encryption Using Ideal Lattices](https://research.ibm.com/publications/fully-homomorphic-encryption-using-ideal-lattices).
- Gennaro, Jarecki, Krawczyk, and Rabin supply the active-adversary and
  key-bias discipline for distributed key generation:
  [Secure Distributed Key Generation for Discrete-Log Based Cryptosystems](https://doi.org/10.1007/s00145-006-0347-3).

These sources constrain the interpretation. They do not establish a physical
record ontology.

## 16. Exact certificate

Run:

```bash
python3 tests/du_joint_input_amplification_probe.py
```

The deterministic artifact is:

```text
tests/artifacts/du_joint_input_amplification_result.json
```

It passes 24/24 exact checks covering:

- deterministic joint-input factorization;
- stochastic garbling and Bayes risk;
- XOR synergy;
- \(2\)-of-\(3\) Shamir reconstruction over \(\mathbb F_5\);
- IID, copied, common-shock, and clustered evidence;
- same pairwise statistics with different threshold tails;
- stigmergic formation and readout error;
- uniform versus eclipse sampling;
- threshold-certificate provenance loss;
- FHE/MPC functional no-minting;
- zero-knowledge statement/physical-target separation; and
- target-sensitive “randomness” as a new input.

The analytic statements stand independently of the script. The script is a
finite proof/regression certificate and therefore remains outside research
model admission under the Local Model Lab Gate.
