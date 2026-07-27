---
title: "Synergy-preserving gossip, DAG provenance, and knowledge-layer separation"
status: completed_scoped_result
doc_type: exact_finite_theorem_counterexample_and_protocol_boundary
created: 2026-07-27
claim_id: HC-DU-048
run_id: N5-SCF-P2
authority: "Joe direct chat: Go"
claim_status_change: "N5-SCF-P2 complete as HC-DU-048; N5-SCF-P3 executable"
paper_state_change: none
hardware_state_change: none
provider_state_change: none
local_model_gate: proof_certificate_outside_research_model_admission
---

# Synergy-preserving gossip, DAG provenance, and knowledge-layer separation

## Executive result

`HC-DU-047` showed that a target can be absent from every individual record
while being exactly present in their joint correlation. This swing follows
that information through propagation, signed events, a hash-DAG, epistemic
pooling, and a statement-bound cryptographic proof.

The main result is:

> Lossless gossip can move complementary source information together and
> thereby turn distributed knowledge into one recipient's actionable
> knowledge. A signed hash-DAG can additionally preserve declared origin and
> ancestry and can make an encountered fork attributable. Neither operation
> certifies that the source correlation was physically target-binding.

Two source worlds make the boundary exact:

1. **Synergy world**

   \[
   R_1=U,\qquad R_2=T\oplus U,
   \]

   with independent uniform \(T,U\). Each share alone is independent of
   \(T\), while the pair reconstructs \(T\).

2. **Null world**

   \[
   T,\ R_1,\ R_2
   \]

   are independent uniform bits.

Both worlds induce the same uniform law on the complete payload pair
\((R_1,R_2)\). Consequently they also induce the same law on every fixed
plain-gossip transcript, signed-event transcript, hash-DAG, DAG-derived vote,
and total-order output constructed only from those events. Yet:

\[
P(T=R_1\oplus R_2)=
\begin{cases}
1 & \text{synergy world},\\
1/2 & \text{null world}.
\end{cases}
\]

The protocol can preserve or expose a relation already bound into its
admitted source events. It cannot infer that physical binding from
cryptographic structure alone.

The swing also establishes:

- plain gossip is sufficient to pool XOR shares; consensus is not required;
- a partition, eclipse delivery of duplicated origin, or churn without
  retention leaves the one-share Bayes error at \(1/2\);
- signed source labels identify declared key origin, not physical
  independence of sensors or controllers;
- parent-hash retention identifies declared route ancestry, while endpoint
  values and total ordering do not;
- raw path length is changed by benign relay insertion, while reachability
  between the original source and terminal events is invariant;
- a signed fork is detectable only in a view that contains both incompatible
  branches;
- the source group can have distributed knowledge before any individual
  knows the target;
- finite asynchronous acknowledgements do not create common knowledge;
- an event-bound commitment or zero-knowledge proof can certify a declared
  consistency predicate without revealing its witnesses, but it certifies
  physical truth only if a physical target/formation attestation is itself an
  admitted bound input; and
- a shared environmental trace is an archive: it may preserve a sufficient
  statistic, compress provenance, evaporate, or be forged. Replicating its
  readout does not independently validate its formation.

The result is a scoped Dynamic Unity classification using known
information-factorization, signed-DAG, reachability, epistemic-logic,
authenticated-agreement, and zero-knowledge components. It is not a new
gossip, consensus, Hashgraph, common-knowledge, cryptographic, emergence, or
physical theorem.

## 1. Plain-English interpretation

There are three different ways a network can appear to “create” something:

1. **Pooling.** Two people each have a useless-looking piece, but putting the
   pieces together reveals an answer.
2. **Provenance.** The network preserves who declared which message and which
   earlier messages a later event names as parents.
3. **Hardening.** A protocol makes it safe for participants to order or act on
   a declared fact under a fault model.

None of those means the network created the underlying physical truth.

In the XOR specimen, the answer exists in the joint source correlation before
any one participant can access it. Gossip changes *who can access the joint
information*. A DAG changes *which declared history can be audited*. A
certificate changes *which actions are safe under declared assumptions*.
Those are real capability changes, but they are not interchangeable.

This matters to Dynamic Unity because regional finality may similarly contain
jointly sufficient physical correlations before a particular observer can
read them. The observer's acquisition can realize a capability without being
the event that first made the source correlation physically true. Conversely,
many observers agreeing on a copied trace can be action-safe while the
trace's physical source remains underidentified.

## 2. Frozen typed contract

Let:

- \(W\) be the physical-world class;
- \(T:W\to\mathcal T\) be the held-out physical target;
- \(R=(R_1,\ldots,R_n)\) be the complete admitted source-event payload;
- \(E\) be the source-event object, including any admitted creator labels,
  signatures, commitments, and parent references;
- \(S\) be the fixed communication schedule, routing, partition, delay,
  churn, and fault transcript;
- \(U_P\) be protocol randomness independent of the physical world
  conditional on \((E,S)\);
- \(A\) be the complete protocol artifact or node view;
- \(P_{\rm decl}\) be declared origin/ancestry provenance;
- \(P_{\rm phys}\) be physical formation/source provenance;
- \(K_i\), \(D_G\), and \(C_G\) denote individual, distributed, and common
  knowledge relative to an explicitly frozen epistemic model;
- \(O\) be any total-order output;
- \(\chi\) be an action certificate; and
- \(\mathcal D\) be the admitted task, loss, resource, and adversary class.

The protocol has the form:

\[
A=\Phi(E,S,U_P).
\]

The contract freezes separately:

1. payload delivery;
2. creator-key attribution;
3. parent/ancestry retention;
4. target-binding source formation;
5. observer retention and pooling;
6. the fault and timing model;
7. total-order semantics;
8. the proposition certified by any commitment or proof;
9. the physical meaning, if any, of the committed target; and
10. the action for which a certificate is claimed safe.

A signature is not a sensor. A parent hash is not a physical causal relation.
A consensus order is not a truth predicate. A proof of a statement does not
establish that the statement's inputs are physically complete.

## 3. Source-binding nonidentifiability theorem

### Deterministic form

Let two physical worlds \(w_0,w_1\) satisfy:

\[
E(w_0)=E(w_1),\qquad S(w_0)=S(w_1),
\]

while a held-out target or source-binding predicate differs:

\[
Z(w_0)\ne Z(w_1).
\]

For every downstream deterministic protocol:

\[
A=\Phi(E,S),
\]

we have:

\[
A(w_0)=A(w_1).
\]

Therefore \(Z\) does not factor through \(A\).

This remains true when \(A\) contains:

- every delivered payload;
- ideal creator signatures;
- collision-free parent hashes;
- the complete admitted event DAG;
- any deterministic virtual-vote or total-order function of that DAG;
- a threshold certificate over those events; or
- a proof of a predicate whose public statement is the same in both worlds.

### Stochastic form

Let \(\mu_0,\mu_1\) be two world distributions with:

\[
E_*\mu_0=E_*\mu_1.
\]

If the protocol randomness satisfies the same kernel
\(K(A\mid E,S)\) in both worlds, then:

\[
A_*\mu_0=A_*\mu_1.
\]

This is ordinary data processing. No test of \(A\) can identify which source
world generated it.

### Exact matched control

The synergy and null source worlds have:

\[
P(R_1=r_1,R_2=r_2)=1/4
\]

for all four payload pairs. The exact certificate builds the same ideal
signed relayed DAG for each pair. The induced distributions of:

- event bodies;
- creator labels;
- signatures;
- parent hashes;
- terminal event;
- source order; and
- one deterministic DAG-derived vote shadow

are equal across the two worlds.

Yet the source-binding predicate

\[
Z=\mathbf 1[T=R_1\oplus R_2]
\]

is constant one in the synergy world and has probability \(1/2\) in the null
world.

### Meaning

The theorem does not weaken cryptographic integrity. It types what integrity
means. If the source event asserts \(x\), a valid signature can authenticate
that a declared key signed \(x\). It cannot, without another admitted
interface, prove that \(x\) is the complete or correct physical observation.

## 4. Synergy-preserving propagation theorem

Suppose:

\[
T=d(R_1,R_2)
\]

for a frozen decoder \(d\), and a recipient view \(V\) contains a lossless
encoding of the pair:

\[
(R_1,R_2)=h(V).
\]

Then:

\[
T=(d\circ h)(V).
\]

No consensus, total order, or cryptographic proof is required for this
factorization. A reliable delivery and retention path is enough.

For the XOR source:

\[
d(r_1,r_2)=r_1\oplus r_2.
\]

The exact controls return:

| Recipient view | Bayes error for \(T\) |
|---|---:|
| \(R_1\) only | \(1/2\) |
| \(R_2\) only | \(1/2\) |
| duplicated \(R_1,R_1\) | \(1/2\) |
| retained \(R_1,R_2\) | \(0\) |

Thus:

- full gossip preserves source-formed joint sufficiency;
- a partition leaves target access absent;
- an eclipse route that returns two copies of one origin does not replace the
  complementary source;
- delayed delivery changes the time at which the target becomes accessible;
  it does not change the source relation; and
- churn that discards the first share before the second arrives destroys the
  recipient's reconstruction unless a retained archive is charged.

### Dynamic Unity consequence

“No observer individually possesses the target” is not a formation
obstruction. It may be an access boundary. A regional group can possess
distributed information that becomes individually actionable only after a
physical pooling channel forms.

## 5. Declared provenance theorem and its boundary

### Endpoint and order are not route

The certificate compares:

```text
source-1 ─┐
          ├─> terminal
source-2 ─┘
```

with:

```text
source-1 -> relay-a ─┐
                     ├─> terminal
source-2 -> relay-b ─┘
```

Both deliver the same two source values in the same declared source order.
An endpoint payload projection or ordered value list cannot distinguish the
routes.

If every retained event contains its declared parents, a collision-resistant
hash of its body, and an unforgeable creator signature, the event DAG
distinguishes the two declared histories under those cryptographic
assumptions.

This is **declared protocol ancestry**:

\[
P_{\rm decl}=\text{the parent/creator structure authenticated by the event schema}.
\]

It is not automatically:

\[
P_{\rm phys}=\text{the complete physical process that formed the values}.
\]

The latter requires an independently justified source-to-event interface.

### Benign subdivision

Inserting one relay on each source path changes:

- node count;
- edge count; and
- source-to-terminal path length from one to two.

It preserves:

- the original source identities;
- reachability from each source to the terminal;
- the delivered source values; and
- the XOR target when source binding is admitted.

Any proposed informational distance, finality depth, or physical scale based
on raw relay or hop count therefore fails benign-subdivision invariance.
Reachability among distinguished original events survives this control.

### Origin rank

Signed origin labels distinguish:

```text
(source-1:0, source-2:1)
```

from:

```text
(source-1:0, source-1:1).
```

This proves two versus one **declared key origins**. It does not prove two
independent sensors, controllers, physical sources, or error mechanisms. Two
keys can still share a controller or common shock.

## 6. Equivocation visibility theorem

Let one declared creator produce two incompatible signed events at the same
sequence:

\[
e_0=(c,k,0),\qquad e_1=(c,k,1).
\]

A view containing both events has an attributable fork witness. A partitioned
view containing only one event does not.

Therefore:

```text
local absence of equivocation evidence
    != global non-equivocation
```

Signatures make an encountered conflict attributable. They do not force
every observer to encounter every branch. A DAG may retain a fork after
branches merge, but a locally incomplete DAG cannot certify that no hidden
branch exists.

This is one reason delivery, knowledge, and Byzantine finality must remain
typed separately.

## 7. Knowledge-layer separation

### Individual versus distributed knowledge

Let the two source views be:

\[
V_1=U,\qquad V_2=T\oplus U.
\]

For every realized history, each local information cell contains both
\(T=0\) and \(T=1\). Neither source individually knows \(T\).

The intersection of their information partitions fixes the pair
\((V_1,V_2)\), and therefore fixes:

\[
T=V_1\oplus V_2.
\]

In the standard epistemic terminology, the group has distributed knowledge
of \(T\): an ideal pooling of its members' information determines the target.
Gossiping both retained shares to one node converts that distributed
knowledge into individual knowledge for the recipient.

This is a genuine capability transition caused by access and pooling. It is
not target minting.

### Finite asynchronous communication and common knowledge

The exact certificate also constructs the standard finite acknowledgment
chain:

- \(A\) sends a message about proposition \(p\);
- \(B\) may acknowledge;
- \(A\) may acknowledge the acknowledgment;
- messages alternate;
- the last message may always have been lost.

For every tested finite chain from zero through eight delivered messages, the
transitive closure of the two agents' indistinguishability relations still
connects the actual \(p=\mathrm{true}\) run to a \(p=\mathrm{false}\) run.
Thus \(p\) is not common knowledge.

This is a finite certificate for the familiar asynchronous last-message
obstruction, not a new result. Halpern and Moses distinguish individual,
distributed, and common knowledge and show that practical systems cannot in
general attain literal common knowledge, motivating weaker variants
([primary paper](https://arxiv.org/abs/cs/0006009)).

### No scalar knowledge depth

The layers are not one monotone scalar:

- distributed knowledge can exist before any individual has the target;
- one recipient can know the target while other nodes remain partitioned;
- a total order can be produced over events whose physical truth is
  underidentified;
- an action certificate can be sufficient for one task without disclosing
  the target witness; and
- a widely readable copied trace need not become common knowledge or acquire
  independent support.

## 8. Total ordering and action safety

A total-order protocol answers:

> Under this membership, network, authentication, and fault model, which
> admitted event is ordered first?

It does not answer:

> Did an event's payload truthfully and completely encode the physical source?

Hashgraph is a useful positive example of why the distinction matters. Its
hashgraph records who has said what to whom; peers can compute votes from
shared DAG information, while multiple communication cycles remain required
([Crary's formal analysis](https://arxiv.org/abs/2102.01167)). Crary explicitly
describes each peer as holding a potentially different subset of the graph
and signatures/hashes as preventing disagreement about shared content—not as
certifying payload truth or complete global visibility.

Authenticated Byzantine agreement similarly restricts undetected behavior
and supports agreement under a fault model; it does not turn authentication
into a truth oracle
([Dolev--Strong](https://doi.org/10.1137/0212045)). Bracha's asynchronous
agreement construction uses reliable broadcast to filter Byzantine behavior
before agreement
([primary paper](https://doi.org/10.1016/0890-5401(87)90054-X)).

The Dynamic Unity typing is:

```text
payload availability
    != source binding
    != declared ancestry
    != equivocation evidence
    != target reconstruction
    != distributed knowledge
    != individual knowledge
    != common knowledge
    != total order
    != action-safe finality
    != physical truth.
```

## 9. Commitment and zero-knowledge boundary

### Unbound statement

The predicate:

\[
\exists a,b:\ a\oplus b=t
\]

is true for both values of \(t\). A proof of that statement says nothing
about the actual delivered source events.

### Event-bound statement

A useful statement instead binds:

- commitments to the two actual source-event payloads;
- the source-event digests;
- a commitment to a declared target; and
- the relation:

  \[
  R_1\oplus R_2=t_{\rm decl}.
  \]

Under a complete proof-system contract, a zero-knowledge proof can establish
that relation without disclosing the shares. The proof changes verifier
capability and disclosure, not the underlying source information. This is the
functionality introduced by zero-knowledge proof systems
([Goldwasser--Micali--Rackoff](https://doi.org/10.1145/22145.22178)).

### Physical-attestation boundary

The same valid statement proof is compatible with:

```text
physical target = declared target
```

and:

```text
physical target != declared target.
```

unless the map from the physical target to the committed target is also part
of the admitted, independently justified interface.

Thus a proof can make the declared predicate action-enabling under its setup,
key, soundness, and adversary assumptions while leaving physical source truth
open.

This is not a defect in zero knowledge. It is the difference between proving
a statement and establishing that its public inputs exhaust the relevant
physics.

## 10. Direct gossip and stigmergic traces

A shared environmental mark is a communication medium and archive, not a
free source of objectivity.

Three trace types give different receipts:

1. **Pair-preserving trace:** stores \((R_1,R_2)\). It retains the synergy and
   permits exact reconstruction, but charges a shared archive.
2. **Parity trace:** stores \(R_1\oplus R_2\). In the synergy world it is a
   target-sufficient strict compression, but it erases which of two source
   pairs produced a given parity and must have a physically justified write
   rule.
3. **Evaporated or forged trace:** an erased mark loses access; a copied
   matching mark can reproduce the value without reproducing the formation
   history.

The exact parity alphabet is identical in the null world, where it has Bayes
error \(1/2\) for the physical target. The trace's symbol semantics therefore
comes from its formation relation, not its alphabet or number of readers.

Stigmergic replication can improve read availability. It does not by itself
establish independent evidence origins, source truth, or public finality.

## 11. First-identifiable-layer receipt

| Target | First sufficient layer in the frozen specimens | What remains open |
|---|---|---|
| Event delivery | Recipient view containing the event | Completeness of the view |
| XOR target reconstruction | First retained view containing both complementary shares | Physical truth of the XOR source relation |
| Authenticated declared origin | Signed source event | Physical controller/sensor independence |
| Declared route ancestry | Retained parent-hash DAG | Complete physical formation history |
| Equivocation evidence | One view containing both incompatible signed branches | Whether hidden branches exist elsewhere |
| Distributed knowledge | The source group before pooling | Individual access |
| Individual target knowledge | Recipient after both shares arrive and remain retained | What other observers know |
| Common knowledge | No finite asynchronous acknowledgment layer in the tested family | Requires stronger timing/public-event semantics or an approximation |
| Total order | Separately specified consensus rule under its fault assumptions | Payload truth and source completeness |
| Action safety | Task-, statement-, setup-, and adversary-relative certificate | Safety for other tasks or physical targets |
| Physical source truth | Not identified by the protocol stack | Independently selected formation/attestation channel |

The table is not a universal chronology. Several rows are incomparable.

## 12. Exact certificate

The regression artifact is:

```text
tests/du_synergy_gossip_dag_provenance_probe.py
tests/artifacts/du_synergy_gossip_dag_provenance_result.json
```

It reports:

```text
HC-DU-048 gossip/DAG provenance certificate: 34/34 passed
```

The checks cover:

1. matched synergy/null payload laws;
2. individual and joint Bayes risks;
3. identical signed-DAG artifact laws with different source binding;
4. full, partitioned, eclipse, delayed, and churn views;
5. endpoint-versus-parent-DAG route identifiability;
6. path-length failure and reachability invariance under relay insertion;
7. payload origin rank versus signed declared origin rank;
8. partitioned and merged equivocation views;
9. individual, distributed, and pooled knowledge;
10. finite asynchronous common-knowledge obstructions;
11. total-order/source-truth separation;
12. unbound versus event-bound proof statements;
13. statement-relative action versus physical attestation; and
14. pair, parity, erased, and forged stigmergic traces.

The ideal signatures, hashes, and proof transcripts are typed labels. The
certificate does not claim computational security or implement Hashgraph,
gossip networking, Byzantine agreement, zero knowledge, or a physical
recording device.

## 13. Prior-art collision and honest grade

### Component terrain

- Epidemic dissemination and rumor spreading absorb propagation.
- Baird's signed gossip-about-gossip DAG and virtual-vote architecture
  supplies the closest event-history comparator
  ([technical report](https://leemon.com/papers/2016b2.pdf)).
- Crary's Coq work verifies the scoped batch Hashgraph algorithm and
  explicitly separates shared graph information from communication progress
  ([paper](https://arxiv.org/abs/2102.01167)).
- Authenticated and asynchronous Byzantine agreement absorb agreement and
  fork-filtering components
  ([Dolev--Strong](https://doi.org/10.1137/0212045);
  [Bracha](https://doi.org/10.1016/0890-5401(87)90054-X)).
- Halpern--Moses absorbs the individual/distributed/common-knowledge
  separation and the practical common-knowledge obstruction
  ([paper](https://arxiv.org/abs/cs/0006009)).
- Goldwasser--Micali--Rackoff absorbs the zero-knowledge functionality
  boundary
  ([paper](https://doi.org/10.1145/22145.22178)).
- Ordinary data processing, sufficient statistics, graph reachability, and
  provenance databases absorb the remaining mathematical components.

### Dynamic Unity increment

The useful DU contribution is one unchanged typed assay spanning:

```text
physical formation
    -> joint source information
    -> propagation and retention
    -> declared cryptographic provenance
    -> epistemic access
    -> ordering/certification
    -> capability-relative action
```

It identifies exactly where a proposed layered-finality story changes
information, access, provenance, knowledge, or safety—and where it silently
imports physical source attestation.

### Maximum grade

```text
SCOPED GRADE 4:
exact necessary factorization and finite counterexample classification
```

This grade applies only to the frozen finite information/protocol objects.
It is not:

- a new distributed-systems theorem;
- a cryptographic construction or security proof;
- a proof of strong emergence;
- a physical record-selection result;
- a quantum/classical correspondence;
- a public-objectivity law;
- a new prediction;
- an ontology; or
- a paper promotion.

## 14. Dynamic Unity implications

### What changed

The program should now distinguish four possible meanings of “regional
actualization”:

1. the physical source correlation formed;
2. the group jointly possessed sufficient information;
3. one observer acquired and retained enough records to reconstruct it; and
4. a declared fault-tolerant certificate made some public action safe.

These may occur at different layers and times.

### What did not change

Nothing here establishes that quantum records are gossip events, that
entanglement is a network edge, that spacetime is a hash-DAG, or that
consensus protocols describe physical collapse. The shared object is the
typed information/access/provenance relation only.

### Physical bridge requirement

For distributed-systems structure to contribute more than an analogy to the
North Star, a physical arena must supply:

1. independently formed complementary records;
2. a physical source-binding relation;
3. a retained acquisition/ancestry interface;
4. a frozen observer and action class;
5. a finite target reconstructed only after pooling or certification; and
6. a hostile matched world with the same protocol-level artifact but a
   different physical target.

Without those maps, agreement and provenance are useful controls but not
physical selection.

## 15. Branch decision

`N5-SCF-P2` is complete as `HC-DU-048`.

The sole next executable work object is:

```text
N5-SCF-P3
Provenance-Preserving Metastable-to-Byzantine Hardening
```

It should use the exact matched source worlds from this swing and ask:

> Can a fast probabilistic preference layer and a later BFT or threshold
> certificate harden one source-bound joint fact without compressing away the
> provenance needed to distinguish independent support, duplication,
> equivocation, and an unbound null source?

The next swing must:

1. keep payload value, source-event digest, declared origin, physical
   source-binding status, and route ancestry separately typed;
2. compare an Avalanche-like confidence layer with a locked
   quorum/threshold certificate under one fault contract;
3. preserve the null world as a mandatory hostile control;
4. compare explicit signer sets, multisignatures, and compressed threshold
   signatures without inferring physical origin independence;
5. track rollback risk, fork safety, liveness, latency, provenance
   sufficiency, and action class separately;
6. retain the first signed equivocation witness through certificate
   compression;
7. test benign relay/DAG subdivision; and
8. stop at the first exact composition theorem or smallest
   provenance-erasing counterexample.

Do not build a network simulator. Do not infer public physical truth from
high confidence, quorum lock, threshold authority, or key count. Positions 4
and 5 remain conditional. `N5-RS-P2` remains deferred, not canceled. No paper,
prediction, hardware, provider, publication, or external-contact state
changes.
