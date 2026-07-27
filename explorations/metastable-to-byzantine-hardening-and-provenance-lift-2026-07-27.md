---
title: "Metastable-to-Byzantine hardening and the provenance-lift boundary"
status: completed_scoped_result
doc_type: exact_finite_composition_theorem_counterexamples_and_protocol_boundary
created: 2026-07-27
claim_id: HC-DU-049
run_id: N5-SCF-P3
authority: "Joe direct chat: Go"
claim_status_change: "N5-SCF-P3 complete as HC-DU-049; N5-SCF-P4 executable"
paper_state_change: none
hardware_state_change: none
provider_state_change: none
local_model_gate: proof_certificate_outside_research_model_admission
---

# Metastable-to-Byzantine hardening and the provenance-lift boundary

## Executive result

`HC-DU-047/048` separated source-formed joint information, propagation,
declared DAG provenance, knowledge, ordering, and physical source truth. This
swing carries the same source-bound and matched-null worlds through a fast
sampling-confidence layer, a quorum-lock layer, explicit and compressed
certificates, threshold signing, private relation verification, partitions,
adaptive corruption, and membership churn.

The return is:

```text
SCOPED_LAYERED_FINALITY_COMPOSITION
WITH A MANDATORY CAPABILITY-INDEXED PROVENANCE LIFT
```

The central positive result is:

> A quorum-intersecting lock certificate can turn a probabilistic local
> preference into a conflict-safe public action authorization under a frozen
> membership, fault, validity, authentication, and timing contract.

The central boundary is:

> Hardening preserves only predicates that factor through the proposal,
> votes, lock state, and public certificate actually retained. It does not
> strengthen the physical truth of the proposal. Certificate compression can
> erase signer, rejected-branch, membership-epoch, and formation provenance
> even while preserving decision verification.

In the frozen \(n=7,f=2,q=5\) control:

- an Avalanche-like sample of \(k=3\) nodes with a two-response threshold
  draws a wrong local majority with probability \(1/7\) when only two nodes
  support the wrong value;
- three independent successful wrong samples have probability \(1/343\);
- reusing one correlated neighborhood leaves the probability at \(1/7\);
- a fully eclipsed view makes it \(1\);
- any two five-validator quorums intersect in at least three validators;
- because three exceeds the two-fault budget, a correct non-conflicting lock
  rule forbids two conflicting certificates;
- a \(4\mid3\) partition cannot form a five-validator certificate on either
  side, so safety can survive while liveness fails; and
- five available honest validators can form a certificate, while one
  additional honest outage plus two Byzantine withholders prevents it.

The proposal contains the two source-event digests and the declared relation:

\[
t_{\mathrm{decl}}=R_1\oplus R_2.
\]

The source-bound XOR world and the target-independent null world have the same
complete proposal law. Every fixed sampling, vote, lock, quorum, multisignature,
threshold-signature-verification, zero-knowledge-verification, or MPC-output
artifact built only from that proposal therefore has the same law in both
worlds. The hardened certificate is valid in both, while:

\[
P(T=t_{\mathrm{decl}})=
\begin{cases}
1 & \text{source-bound world},\\
1/2 & \text{null world}.
\end{cases}
\]

Consensus can make a declared claim stable enough to act on. It cannot make
the claim physically true.

The useful Dynamic Unity advance is an exact decomposition:

```text
source binding
    -> proposal validity
    -> sampled preference
    -> quorum/lock safety
    -> certificate verification
    -> retained provenance
    -> observer-specific action capability
```

Every arrow has its own premise and first failure. There is no scalar
“finality level” that subsumes them all.

## 1. Plain-English interpretation

Imagine that a fast leaderless network tentatively favors an answer after
sampling a few peers. Repeating the sample can make the node increasingly
confident, but only if those samples provide genuinely fresh information.
Sampling the same neighborhood repeatedly—or being trapped behind an
eclipse—does not multiply evidence.

A later Byzantine quorum can do something stronger and genuinely different:
it can guarantee that two conflicting answers will not both receive valid
commit certificates, assuming the fault bound and locking rules hold. That
can justify an irreversible shared action where the earlier tentative
preference justified only a reversible one.

But the quorum has not measured the world again. It has hardened the network's
relationship to the proposal it was given.

The difference is:

```text
metastability reduces local rollback risk
BFT hardening prevents conflicting public authorization
cryptography authenticates the declared authorization
provenance says what evidence and history that authorization actually covers
none of these alone establishes physical source truth
```

A compact threshold signature may be perfectly sufficient for “may I execute
this decided command?” while being insufficient for “which validators signed
it?”, “were those keys independently controlled?”, “did the leader
equivocate?”, or “was the original sensor relation physically true?” Finality
is therefore indexed by the observer's action and audit capability.

## 2. Frozen typed contract

### Source worlds

Let \(T,U\) be independent uniform bits.

The source-bound world has:

\[
R_1=U,\qquad R_2=T\oplus U.
\]

The matched null world has independent uniform:

\[
T,\ R_1,\ R_2.
\]

Both induce the same uniform law on \((R_1,R_2)\).

### Proposal

The proposal is:

\[
m=(e,h,d_1,d_2,t_{\mathrm{decl}},V),
\]

where:

- \(e\) is a fixed membership/key epoch;
- \(h\) is one fixed conflict domain or height;
- \(d_1,d_2\) are the two signed source-event digests;
- \(t_{\mathrm{decl}}=R_1\oplus R_2\); and
- \(V\) is the declared validity identifier stating that the committed source
  values satisfy that XOR relation.

For validation, the complete witness supplies either the committed source
openings or an event-bound proof of that declared relation. Those validation
objects are typed separately from the compact public proposal.

The proposal does not contain a physical attestation that
\(T=t_{\mathrm{decl}}\).

### Metastable layer

Freeze:

```text
n = 7 participants
b = 2 wrong-preference participants
k = 3 sampled participants without replacement
alpha = 2 responses required for one successful sample
beta = 3 consecutive successful samples for local confidence
```

This is an exact Avalanche-like sampling control. It is not an implementation
or security analysis of Avalanche.

### Hard-finality layer

Freeze:

```text
n = 7 validators
f = 2 Byzantine validators
q = 5 votes per quorum certificate
one epoch and one conflict domain
authenticated votes
correct validators do not sign conflicting locked proposals
proposal validity checked only against V, the admitted event commitments,
and the frozen opening-or-proof path
```

The single-domain non-conflicting lock is the smallest exact quorum-safety
core. It is not a complete multi-view HotStuff implementation or proof.

### Certificate views

Compare:

1. **Explicit QC:** proposal plus five individually attributable votes.
2. **Aggregate/multisignature with bitmap:** compact signature plus the
   externally retained signer set.
3. **Compressed threshold verification record:** group public key, proposal,
   and valid group-signature result, without an accountable signer sidecar.
4. **Provenance lift:** certificate plus epoch, membership root, validity
   identifier, source-event digests, and a canonical semantic-event root with
   available openings for action-relevant forks.

The comparison concerns the information each public record retains. It does
not claim that every multisignature or threshold-signature scheme has one
fixed disclosure policy. Accountable threshold signatures are an explicit
positive alternative.

### Adversary and timing

Keep separately frozen:

- static Byzantine bound;
- mobile/adaptive corruptions and share refresh;
- partitions and eclipse;
- response dependence across samples;
- Byzantine withholding;
- membership/key epoch changes;
- reliable delivery and partial-synchrony assumptions used for liveness;
- source-event truthfulness;
- key-controller independence;
- archive retention and opening availability; and
- computational cryptographic assumptions.

## 3. Metastable confidence dependence lemma

Let \(b\) of \(n\) participants favor the wrong value. Sampling \(k\) without
replacement and requiring at least \(\alpha\) wrong responses gives:

\[
s(n,b,k,\alpha)=
\sum_{j=\alpha}^{k}
\frac{\binom{b}{j}\binom{n-b}{k-j}}{\binom{n}{k}}.
\]

For \((n,b,k,\alpha)=(7,2,3,2)\):

\[
s=\frac{\binom22\binom51}{\binom73}=\frac{5}{35}=\frac17.
\]

If the three confidence rounds are conditionally independent with the same
fixed population state:

\[
P(\text{three wrong successful samples})=s^3=\frac1{343}.
\]

If all three rounds reuse the same sampled neighborhood, the events are fully
correlated:

\[
P(\text{three wrong reports})=s=\frac17.
\]

Under a complete eclipse that supplies only wrong responses:

\[
P(\text{wrong reports})=1.
\]

### Consequence

A confidence counter is not self-authenticating evidence. Its error semantics
depend on:

- sampler coverage;
- independence or mixing;
- topology and routing;
- adversarial control;
- participant-origin dependence; and
- whether repeated responses are fresh or duplicated.

The confidence transition is real under its model, but it does not survive a
silent change from fresh samples to one common neighborhood.

The Snow/Avalanche family explicitly builds probabilistic BFT around
metastability and network subsampling
([primary paper](https://arxiv.org/abs/1906.08936)). The finite calculation
above is only a hostile assumption check for Dynamic Unity.

## 4. Quorum-lock hardening lemma

For two signer sets \(Q_0,Q_1\subseteq N\), each of size \(q\):

\[
|Q_0\cap Q_1|\ge 2q-n.
\]

With \(n=7,q=5\):

\[
|Q_0\cap Q_1|\ge3.
\]

At most \(f=2\) validators are Byzantine. Therefore every pair of quorums has
at least one correct validator in its intersection.

If a correct validator does not sign two conflicting locked proposals in the
same conflict domain, two conflicting five-vote certificates cannot both
exist.

This is exact conflict safety. It is not a probability statement about the
physical truth of the proposal.

### Locking is load-bearing

Threshold unforgeability or signer count alone is insufficient. If correct
validators may sign both conflicting proposals, the same five validators can
authorize both. The non-conflicting lock or a stronger multi-view safe-vote
rule is what turns quorum intersection into safety.

HotStuff makes the same distinction at full protocol scale: voting and lock
rules establish safety, while its pacemaker and partial-synchrony assumptions
address liveness separately
([primary paper](https://arxiv.org/abs/1803.05069)).

### Safety is not liveness

In a \(4\mid3\) partition, neither component contains five validators.
Conflicting certificates remain impossible, but no certificate can form.

If all five correct validators communicate, they can form a five-vote
certificate even when two Byzantine validators withhold. If one correct
validator is also unavailable, only four votes remain and progress stops.

This finite witness is consistent with the broader terrain:

- deterministic fully asynchronous consensus can have a nonterminating
  execution with one fault
  ([Fischer--Lynch--Paterson](https://doi.org/10.1145/3149.214121)); and
- partial synchrony introduces the timing conditions under which
  fault-tolerant progress can be recovered
  ([Dwork--Lynch--Stockmeyer](https://dwork.seas.harvard.edu/publications/consensus-presence-partial-synchrony)).

## 5. Proposal-validity non-amplification theorem

Let \(E\) be the complete admitted source-event tuple, \(M\) the proposal,
\(W\) the complete sampling/vote/lock witness, and \(C\) the public
certificate:

\[
W_{\mathrm{phys}}
\xrightarrow{E}
E
\xrightarrow{d}
M
\xrightarrow{\Psi}
W
\xrightarrow{\pi}
C.
\]

If two physical-world distributions induce the same law on \(E\), and every
later protocol kernel is the same conditional on \(E\), then they induce the
same law on \(C\).

The source-bound and null worlds satisfy this premise. Therefore no fixed
metastable or Byzantine hardening artifact distinguishes them.

The validators can enforce:

\[
V(M)=\mathbf 1[t_{\mathrm{decl}}=R_1\oplus R_2]
\]

exactly. But that predicate is true in both worlds. It does not include:

\[
Z(W_{\mathrm{phys}})
=\mathbf 1[T=t_{\mathrm{decl}}].
\]

Thus:

```text
certificate validity
    != proposal physical truth.
```

The result does not weaken consensus. Consensus solves agreement and safe
replication relative to an external-validity predicate. The source-to-proposal
map must separately earn its physical meaning.

## 6. Validator quorum is not evidence quorum

Suppose five validators inspect the same two source events and vote for the
same proposal.

The certificate contains five validator endorsements. It does not contain
five independent measurements of \(T\).

Even an explicit signer set is compatible with:

```text
two independently controlled source keys
```

and:

```text
two source keys controlled by one device or one common shock.
```

The validator quorum can be independent for agreement purposes while the
source evidence rank remains one or two under a separate physical-source
model.

Therefore:

```text
validator fault independence
    != source evidence independence.
```

This is the distributed-systems version of the repeated Dynamic Unity warning
that more copies, readers, or certifiers do not automatically supply more
independent target-sensitive information.

## 7. Certificate-provenance factorization theorem

Let \(\Omega\) be the complete witness-history class and:

\[
\pi:\Omega\to\mathcal C
\]

the public certificate projection. Let \(Z:\Omega\to\mathcal Z\) be any
action-relevant target, such as:

- decided value;
- signer subset;
- physical controller rank;
- leader equivocation;
- first conflicting branch;
- membership epoch;
- source-event relation;
- source physical truth; or
- route ancestry.

Then \(Z\) is reconstructible from the certificate exactly when:

\[
\ker\pi\subseteq\ker Z.
\]

Equivalently, every two complete histories producing the same public
certificate must agree on \(Z\).

This is ordinary factorization mathematics. Its value here is to prevent a
certificate strong for one action from being silently treated as complete for
every later audit.

### Exact first leaks

| Public record | What factors | First omitted target |
|---|---|---|
| Metastable local preference | current favored value and declared sample transcript | global conflict safety |
| Quorum decision value | decided proposal under the lock/fault contract | signer identity if signatures are compressed |
| Explicit QC | decision and declared signer set | rejected equivocation branch |
| Bitmap-bearing aggregate signature | decision and declared signer set | controller independence and hidden branches |
| Ordinary compressed threshold verification record | decision under group key and threshold setup | actual signer subset |
| QC plus semantic provenance lift and available openings | declared source/proposal/vote/fork history in its committed class | physical source binding unless separately attested |

These records form an action-relative partial order, not a universal scalar
ladder.

## 8. Threshold compression boundary

FROST is a useful exact comparator. It:

- lets a threshold of participants cooperate to produce a Schnorr signature;
- produces a signature verified under one group public key as though produced
  by a single signer;
- assumes the participant set is chosen externally;
- leaves trusted-dealer versus DKG configuration outside the signing
  protocol;
- assumes reliable authenticated delivery for completion; and
- requires application-specific message validation
  ([RFC 9591](https://www.rfc-editor.org/rfc/rfc9591.html)).

Its standard final verification record establishes a group-key signature on
the message. It does not, by itself, provide the verifier an accountable
signer-subset receipt.

The exact finite control compares two different five-signer subsets that
project to the same semantic record:

```text
(group public key, message, signature valid)
```

An explicit QC or bitmap-bearing aggregate record distinguishes the subsets.
An accountable threshold signature can also do so. That is a stronger
primitive, not a property to infer from threshold validity. The accountable
threshold-signature literature defines accountability precisely by requiring
the signature to identify the signer quorum
([Boneh--Partap--Rotem](https://eprint.iacr.org/2022/1656)).

### DKG and VSS do not close every provenance target

A secure DKG or verifiable secret-sharing setup can establish, under its
cryptographic model:

- consistent share generation;
- a group public key without one trusted dealer;
- threshold reconstruction/signing authority; and
- resistance to a declared number of corrupt participants.

It does not automatically establish:

- which subset signed a later message;
- that keys remain under independent physical control;
- that the signed application input is physically truthful;
- that an old membership epoch is not being reused; or
- liveness under withholding.

FROST itself explicitly leaves key-share configuration to a trusted dealer or
a separate DKG and does not provide signing robustness against refusal.

### Adaptive/mobile corruption

With \(q=5\), an adversary collecting two persistent shares per epoch can hold
six distinct shares after three epochs if shares are neither refreshed nor
erased. A static “at most two at once” statement is then insufficient.

A correctly specified proactive refresh changes the share epoch so old and
new shares cannot simply be combined. But refresh, erasure, epoch identity,
and corruption timing are new premises and resources. Proactive
accountability is itself a separate cryptographic problem, not a free
consequence of threshold signing.

## 9. Equivocation and the provenance-erasing certificate

Consider two complete histories:

1. a leader proposes \(m\), and \(m\) receives a valid QC;
2. the leader proposes \(m\) to one region and conflicting \(m'\) to another,
   but only \(m\) receives the final QC.

The final decision value and signer set can be identical. Therefore a plain
explicit QC need not reconstruct whether the rejected conflicting proposal
ever existed.

This is the smallest hardening/provenance counterexample:

```text
same hard-final certificate
different signed equivocation history.
```

A later blame, slash, forensic, or source-history action cannot use the plain
QC as a sufficient record.

### Minimum provenance lift

For the frozen action family, use:

\[
C^+
=
(C,e,\rho_N,V,d_1,d_2,\rho_{\mathrm{sem}}),
\]

where:

- \(C\) is the decision certificate;
- \(e\) is the key/membership epoch;
- \(\rho_N\) is the membership root;
- \(V\) identifies the validity predicate;
- \(d_1,d_2\) bind the source events; and
- \(\rho_{\mathrm{sem}}\) commits to the distinguished source, proposal,
  vote, lock, and encountered-equivocation events.

For an equivocation accusation, the observer additionally needs available
openings for both conflicting signed branches. A root without retained
openings gives binding, not availability or disclosure.

### Benign-subdivision control

A Merkle root over every transport event changes when one harmless relay is
inserted. It is therefore not a refinement-natural identity for the semantic
history.

The positive control commits to a canonical distinguished-event quotient:

- source events;
- proposals;
- votes/locks;
- decision certificates; and
- signed equivocation witnesses.

Transport-only relay insertion may remain in a separate route log. The
semantic root and source-to-decision reachability survive.

This choice is not automatic. The action-relevant event type and quotient must
be frozen independently of the observed result.

## 10. Membership churn and epoch binding

Two disjoint validator memberships can use or inherit one group public key
across a resharing transition. A public record containing only:

```text
(group public key, message, valid signature)
```

does not identify which membership epoch authorized the decision.

Binding the epoch and membership root into the signed statement separates the
histories. It also makes membership migration, key refresh, and certificate
verification part of the resource and trust contract.

This is another capability-relative first leak:

- an execution client that needs only a valid current group-key decision may
  accept the compact record;
- an auditor of validator accountability or churn safety needs the
  epoch/membership lift.

## 11. Verification and computation without disclosure

### Event-bound zero knowledge

A proof can bind:

- commitments to \(R_1,R_2\);
- source-event digests;
- \(t_{\mathrm{decl}}\); and
- the relation \(R_1\oplus R_2=t_{\mathrm{decl}}\).

Validators can verify the relation without learning the shares. They can then
lock and certify \(t_{\mathrm{decl}}\).

The proof transcript has the same law in the source-bound and null worlds
because the committed pair has the same law. Physical source truth remains
open unless the physical target-to-commitment interface is separately
attested.

### MPC or homomorphic computation

An MPC/FHE layer can compute \(R_1\oplus R_2\) without reconstructing both
shares at one participant. That changes:

- disclosure;
- which coalitions can compute;
- key/setup requirements; and
- action capability.

It does not change the source relation. The same private computation returns
the same declared parity in the null world.

### Verifiable sharing

VSS can ensure that distributed shares encode one consistent declared secret
and can make malformed sharing detectable under its assumptions. It does not
prove that the secret equals an unmodeled physical target
([Rabin--Ben-Or](https://doi.org/10.1145/73007.73014)).

## 12. Exact scoped composition theorem

Let:

- \(E\) be independently formed admitted source events;
- \(M=d(E)\) be a proposal;
- \(V(E,M)\) be the frozen validity predicate;
- \(P\) be a metastable preference artifact;
- \(W\) be the complete vote/lock witness;
- \(C=\pi(W)\) be a public certificate;
- \(C^+\) be any declared provenance lift;
- \(A\) be a future action; and
- \(\mathcal F\) be the fault, timing, key, archive, observer, and resource
  contract.

The stack supports \(A\) without refit when:

1. **Source adequacy:** every physical target needed by \(A\) factors through
   \(E\), or is explicitly carried as an additional attested premise.
2. **Validity adequacy:** correct validators check every proposal predicate
   needed by \(A\).
3. **Preference accounting:** the sampling-confidence error is bounded under
   the actual dependence and routing model.
4. **Conflict safety:** quorum intersection plus the correct lock rule exclude
   conflicting certificates under \(\mathcal F\).
5. **Liveness:** delivery, synchrony, availability, and nonwithholding
   premises sufficient for progress hold separately.
6. **Certificate sufficiency:** the public certificate and provenance lift
   retain every target needed by \(A\):

   \[
   \ker(C,C^+)\subseteq\ker A.
   \]

7. **Epoch/setup integrity:** membership, key generation, corruption timing,
   refresh, and trusted setup match the claimed certificate semantics.
8. **Archive availability:** every action-required provenance opening remains
   retrievable within the declared horizon.

If all eight hold, hardening composes for that action class.

If any one fails, the earliest failed arrow is the correct result. Later
layers cannot repair it merely by adding confidence, signatures, quorum size,
or certificate compression.

This theorem is exact but scoped. It organizes standard component results; it
does not claim a new universal consensus theorem.

## 13. What each layer genuinely adds

| Layer | Genuine addition | Does not add |
|---|---|---|
| Fresh repeated sampling | model-relative reduction in local preference error | source truth or deterministic conflict safety |
| Retained gossip/DAG | delivery, declared ancestry, encountered fork evidence | complete global visibility |
| Quorum intersection plus lock | conflicting-certificate safety under the fault contract | liveness or payload truth |
| Explicit QC | decision plus declared signer attribution | physical controller independence or rejected branches |
| Aggregate signature plus bitmap | smaller authentication with retained signer set | source evidence rank |
| Ordinary threshold group signature | compact threshold authority under one group key | signer accountability unless separately designed |
| DKG/VSS | distributed setup/share consistency under its security model | physical input truth or later signing provenance |
| ZK | verification without witness disclosure | physical attestation of omitted inputs |
| MPC/FHE | computation without central access to all inputs | information absent from the joint input |
| Provenance lift | action-relative auditability of committed semantic history | truth beyond the admitted formation interface |

## 14. Capability-relative finality

The same certificate can be:

- final for executing one command;
- nonfinal for identifying the signer subset;
- nonfinal for blaming an equivocator;
- nonfinal for validating source independence;
- nonfinal for reconstructing the route; and
- silent about physical truth.

Therefore a hardened record is not simply “more final.” It changes a vector
of capabilities.

The minimum observer/action examples are:

1. **Tentative client:** may perform a cheap reversible action after a
   metastable preference.
2. **Execution client:** may perform an irreversible shared action after a
   valid QC under the fault contract.
3. **Accountability auditor:** additionally needs signer and epoch provenance.
4. **Equivocation auditor:** additionally needs available conflicting-branch
   openings.
5. **Physical-source adjudicator:** needs an independently justified
   source-to-event attestation channel not supplied by consensus.

This is the exact bridge to Position 4: differently filtered views can be
complete for different actions without any one view being the global history.

## 15. Resource receipt

No universal cost law is claimed. The frozen comparison charges different
resource classes:

| Record | Principal charged resources |
|---|---|
| Metastable preference | \(k\beta\) sampled replies, sampler coverage, latency, rollback exposure |
| Explicit QC | five votes/signatures, signer bitmap, lock state, message delivery |
| Aggregate/multisignature QC | aggregation and verification plus retained bitmap/key list |
| Threshold signature | DKG or dealer, share custody, two-round coordination in the FROST comparator, authenticated reliable delivery, group verification |
| Accountable threshold lift | additional trace/accountability construction and metadata |
| Semantic provenance lift | event archive, canonicalization, root, inclusion proofs, retention and availability |
| ZK/VSS/MPC path | setup, proof/circuit/share traffic, key custody, disclosure policy and verification |
| Membership change | epoch transition, resharing/refresh, erasure, membership-root distribution |

Compactness trades against some audit capabilities. It is not free
information preservation.

## 16. Exact certificate

The deterministic regression artifact is:

```text
tests/du_metastable_byzantine_provenance_hardening_probe.py
tests/artifacts/du_metastable_byzantine_provenance_hardening_result.json
```

It checks exact finite:

- hypergeometric sampling and independent/correlated/eclipse confidence;
- quorum intersection and lock necessity;
- partition/withholding liveness;
- matched source-bound/null certificate laws;
- source-evidence versus validator-quorum rank;
- explicit, bitmap, threshold, and accountable certificate projections;
- clean-versus-equivocating histories;
- semantic versus raw transport roots under benign relay subdivision;
- membership-epoch ambiguity;
- mobile-corruption accumulation and refresh typing;
- ZK/VSS/MPC source-truth boundaries; and
- capability-indexed certificate factorization.

The script uses exact finite sets, rational arithmetic, ideal signatures, and
ideal commitment labels. It is a proof/regression certificate after the
analytic result. It is not a network simulator, consensus implementation,
cryptographic implementation, security proof, or physical model.

## 17. Prior-art collision and honest grade

### Strong absorbers

- Snow/Avalanche absorbs metastable leaderless subsampling consensus.
- Quorum intersection, authenticated BFT, HotStuff-style locking, FLP, and
  partial synchrony absorb conflict safety and liveness structure.
- Multisignature, threshold-signature, FROST, DKG, VSS, accountable-signature,
  proactive-refresh, ZK, and MPC theory absorb the cryptographic functions.
- Ordinary factorization, sufficient statistics, data processing, and
  provenance systems absorb the certificate-sufficiency mathematics.

### Dynamic Unity increment

The DU-owned result is the unchanged end-to-end typed assay:

```text
physical source formation
    -> joint information
    -> propagation
    -> probabilistic preference
    -> conflict-safe hardening
    -> cryptographic compression
    -> retained provenance
    -> observer-relative action
```

It identifies the smallest missing arrow when a public-finality claim silently
moves from “safe to execute” to “true,” “independently supported,”
“accountable,” or “complete.”

### Maximum grade

```text
SCOPED GRADE 4:
exact necessity/sufficiency and finite counterexample classification
for the frozen information, quorum, certificate, and action objects
```

This is not:

- a new Avalanche, BFT, HotStuff, or threshold-signature theorem;
- a new cryptographic construction or security proof;
- a distributed-systems performance result;
- a phase transition or strong-emergence result;
- a physical record-selection theorem;
- a quantum/classical correspondence;
- a public-reality law;
- a prediction;
- new physics;
- an ontology; or
- a paper promotion.

## 18. Branch decision

`N5-SCF-P3` is complete as `HC-DU-049`.

The composition succeeds for action safety only with all premises typed, and
plain certificate hardening returns exact provenance-erasing
counterexamples. This is sufficient to activate:

```text
N5-SCF-P4
Capability-Relative Selective Views and Regional Handoff
```

Position 4 should:

1. reuse the tentative, execution, accountability, equivocation-audit, and
   physical-source action classes from this swing;
2. freeze target-independent area-of-interest filters for each class;
3. give different regional observers different subsets of the decision,
   signer, fork, route, source, and epoch records;
4. prove the minimal view sufficient for each action;
5. test cross-region handoff with a compact certificate plus on-demand
   provenance sidecar;
6. expose the first leak when a capability expands;
7. test partition, churn, rollback, stale membership, selective replication,
   feedback-driven interest changes, and archive unavailability;
8. preserve the matched null source; and
9. stop at an exact action-relative local-finality theorem or the smallest
   unsafe-handoff counterexample.

Position 5 remains conditional. `N5-RS-P2` remains deferred, not canceled. No
paper, prediction, hardware, provider, publication, submission, or external
contact state changes.
