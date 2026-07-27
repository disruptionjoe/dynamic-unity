---
title: "Capability-relative selective views and regional handoff"
status: completed_scoped_theorem_and_counterexample_boundary
doc_type: exact_finite_factorization_theorem_counterexamples_and_handoff_contract
created: 2026-07-27
claim_id: HC-DU-050
run_id: N5-SCF-P4
authority: "Joe direct chat: Go go"
claim_status_change: "N5-SCF-P4 complete as HC-DU-050; N5-SCF-P5 executable"
paper_state_change: none
hardware_state_change: none
provider_state_change: none
local_model_gate: proof_certificate_outside_research_model_admission
---

# Capability-relative selective views and regional handoff

## Executive result

This swing asks whether differently filtered regional views can be
simultaneously sufficient for what their holders need to do without requiring
one globally replicated history. It also asks exactly what happens when an
observer's or participant's capability expands.

The return is:

```text
CAPABILITY_RELATIVE_SELECTIVE_VIEW_AND_REGIONAL_HANDOFF_THEOREM
WITH AVAILABILITY, EPOCH, AND MONOTONICITY BOUNDARIES
```

The positive result is:

> A region can possess a final-enough record for one frozen action even when
> its view is incompatible with another region's view and neither region can
> reconstruct the global history. Safe handoff requires only that the
> receiver's target action factor through the exported certificate together
> with the receiver's declared context.

The boundary is:

> Finality is indexed by an action and a capability surface. A record that is
> sufficient for conflict-safe execution can remain insufficient for signer
> accountability, equivocation proof production, route forensics, or physical
> source adjudication. Adding one of those capabilities refines the relevant
> history equivalence and can reopen distinctions that were final for the
> smaller capability.

Three small counterexamples are load-bearing:

1. the same valid compact certificate and provenance root permit a fork proof
   when the committed sidecar is retrievable and do not permit it when the
   sidecar is unavailable;
2. the same group-key verification record is safe at its signed membership
   epoch and stale at a different receiver epoch; and
3. an interest filter driven by its own current preference can forward the
   same confirming event in two histories while suppressing a corrective event
   that changes the proper action.

The exact finite certificate exhausts 512 histories and passes 28/28 checks.
It computes the inclusion-minimal field bundles for five frozen action
classes:

| Action | Minimum sufficient semantic fields in the frozen arena |
|---|---|
| tentative response | tentative preference |
| conflict-safe execution | decision, certificate validity, current-epoch status |
| signer accountability | certificate validity, signer subset |
| equivocation-proof readiness | fork commitment, sidecar availability |
| physical-source adjudication | independently formed source attestation |

These are minima only for the frozen finite contract. They are not universal
wire formats. An explicit quorum certificate and a compressed threshold
certificate are incomparable implementations that can both realize the same
execution quotient.

The Dynamic Unity advance is a precise replacement for the vague idea that
all participants need progressively more copies of one global state:

```text
full admitted history
    -> action-independent selective view
    -> capability-relative action quotient
    -> receiver-contextual handoff
    -> optional capability expansion and fibre refinement
```

No software participant is identified with a physical observer. The physical
collision remains for Position 5.

## 1. Plain-English interpretation

An MMO client does not need the exact state of every object in the world to
render the five objects its player is watching. A payment executor does not
need the identity of every signer if a valid group signature is enough to
authorize the payment. An auditor does need more: the signer set, the rejected
branch, or the underlying archive opening. A physicist asking whether the
original event actually happened needs a different kind of evidence again.

Those are not five confidence levels on one scale. They are five different
questions.

A local view can therefore be complete for its job while being radically
incomplete as a biography of the whole system. This is not an inconsistency.
It becomes unsafe only when:

- the job changes without changing the view;
- the receiver interprets the certificate under a different epoch or validity
  rule;
- a compact commitment is mistaken for available evidence;
- the filter selecting the view depends on the view's current conclusion and
  hides corrective evidence; or
- the target was never present in any admitted upstream record.

The practical slogan is:

```text
send the quotient needed for the action
bind the context needed to interpret it
retain an available opening for every promised audit
reopen the record when the capability changes
```

That is a distributed-systems theorem shape. Dynamic Unity may later discover
an analogous physical architecture, but this result does not establish that
physics uses one.

## 2. Frozen typed contract

Let:

- \(H\) be the admitted finite history space;
- \(V:H\to Q\) be an action-independent record or selective-view map;
- \(A_c:H\to Y_c\) be the target action for capability \(c\);
- \(E:H\to X\) be a regional export;
- \(K:H\to C\) be the receiver context admitted by the handoff contract; and
- \(G\) be a declared gauge or benign representation equivalence, when one is
  needed.

The five capabilities are frozen before selecting any view:

1. reversible tentative response;
2. conflict-safe execution;
3. signer accountability;
4. production of a verifiable equivocation packet; and
5. physical-source adjudication.

The finite history fields are:

- tentative preference;
- decided value;
- certificate-validity bit;
- current-epoch status;
- signer subset;
- whether an encountered fork is committed;
- whether its sidecar remains available;
- independently formed source attestation;
- physical target; and
- route label.

All protocol fields vary independently of the physical target in the hostile
null source. The source attestation equals the target only in the explicit
positive source-bound control.

The route label is deliberately present. It is absent from every minimum view
for the five frozen actions. If route forensics is later added as a capability,
the action family changes and route information can become necessary.

## 3. The action-relative selective-view theorem

### Theorem HC-DU-050A

For a frozen capability \(c\), a selective view \(V\) is exactly sufficient
for action \(A_c\) iff any of the following equivalent conditions holds:

\[
\exists d_c:Q\to Y_c
\quad\text{such that}\quad
A_c=d_c\circ V,
\]

\[
\ker V\subseteq\ker A_c,
\]

or, in plain English:

> no two histories that look identical through the view demand different
> actions.

### Proof

If \(A_c=d_c\circ V\), equal view values have equal action values, so
\(\ker V\subseteq\ker A_c\).

Conversely, if the kernel inclusion holds, define \(d_c(q)\) as \(A_c(h)\) for
any history \(h\) with \(V(h)=q\). The kernel condition makes the definition
independent of which representative is chosen.

This is the ordinary fibre factorization result. The Dynamic Unity content is
its typed use across:

- regional filtering;
- certificate compression;
- receiver context;
- capability expansion; and
- physical-source boundaries.

### Corollary: global replication is not required

Let regions \(r\) possess views \(V_r\) and assigned actions \(A_r\). If

\[
\ker V_r\subseteq\ker A_r
\qquad\text{for every }r,
\]

each region can be locally action-sufficient even if:

\[
\ker V_r\not\subseteq\ker \operatorname{id}_H
\]

for every region. In other words, none need reconstruct the global history.

The exact control instantiates:

- one execution region holding decision, certificate validity, and epoch
  status;
- one audit region holding fork commitment and sidecar availability.

Each closes its assigned action. Neither reconstructs the full history.

### Joint-view corollary

Individual insufficiency does not imply joint insufficiency:

\[
A\not\preceq V_1,\qquad A\not\preceq V_2
\]

does not imply

\[
A\not\preceq (V_1,V_2).
\]

In the finite control, neither the execution view nor the fork view supports
an attributable-fork packet alone. Their joined view, with explicit signer
identity, does.

This preserves the correction already learned in `HC-DU-047/048`: distributed
composition can pool complementary information that upstream sources
actually formed.

## 4. Minimum views and non-unique implementations

The exhaustive calculation searches every subset of the nine eligible view
fields. It returns:

\[
\begin{aligned}
V_{\mathrm{tentative}}&=(p),\\
V_{\mathrm{execute}}&=(d,v,e),\\
V_{\mathrm{signers}}&=(v,S),\\
V_{\mathrm{fork}}&=(f,a),\\
V_{\mathrm{source}}&=(\alpha),
\end{aligned}
\]

where:

- \(p\) is tentative preference;
- \(d\) is decision;
- \(v\) is certificate validity;
- \(e\) is current-epoch status;
- \(S\) is signer subset;
- \(f\) says the fork is committed;
- \(a\) says the necessary openings are available; and
- \(\alpha\) is an independently formed source attestation.

The exact target quotient is canonical for a frozen action. The field or wire
encoding need not be.

For execution, both of these can be sufficient:

```text
decision + epoch + explicit individual signatures
decision + epoch + compressed threshold verification
```

The first also supports signer accountability. The second does not. It is
therefore wrong to ask for one universal “minimum record” without first
freezing:

- the action family;
- the verifier's decoder and trust assumptions;
- the membership epoch;
- the audit horizon; and
- the available opening channels.

## 5. Capability expansion law

For an action family \(C\), define:

\[
h\sim_C h'
\iff
\forall c\in C,\ A_c(h)=A_c(h').
\]

If \(C\subseteq C'\), then:

\[
\sim_{C'}\ \subseteq\ \sim_C.
\]

### Theorem HC-DU-050B

Capability enlargement can only preserve or refine the action-relevant
history partition. It cannot coarsen it.

### Proof

Agreement on every action in \(C'\) entails agreement on the subset \(C\).

### Exact control

The finite partition counts are:

| Capability family | Equivalence classes |
|---|---:|
| execution only | 3 |
| execution + signer + fork audit | 14 |
| execution + protocol audit + physical adjudication | 28 |

Thus a certificate final for execution becomes nonfinal for a stronger audit.
This is not retroactive failure of the earlier action. It is a change in what
distinctions matter.

The candidate law for future physical collision is:

> finality is stable under capability preservation and can reopen under
> capability enlargement.

This remains a formal program law, not a physical law.

## 6. Regional handoff theorem

### Receiver-contextual factorization

A regional export \(E\) is sufficient for receiver action \(A_c\) under
receiver context \(K\) iff:

\[
A_c=d_c\circ(E,K)
\]

for some decoder \(d_c\), equivalently:

\[
\ker(E,K)\subseteq\ker A_c.
\]

### Operational premises

The exact handoff disposition requires eight typed premises:

1. **sender action sufficiency** — the sender's admitted state already
   determines the target it promises to export;
2. **certificate-semantic alignment** — sender and receiver interpret
   decision, validity, conflict, and finality predicates the same way;
3. **epoch and membership binding** — the signed claim binds the membership
   context under which it is authorized;
4. **commitment binding** — any promised sidecar or fork evidence is bound to
   the compact export;
5. **required evidence availability** — the receiver can actually retrieve
   the openings needed by its action;
6. **receiver decoder and access** — the receiver has the verification,
   decryption, disclosure, or control capability the export presumes;
7. **frozen capability contract** — the target action has not silently
   expanded; and
8. **target present in admitted input** — the handoff does not claim to
   reconstruct a physical distinction absent from every upstream input.

When all eight hold, the finite contract returns:

```text
CAPABILITY_RELATIVE_SAFE_REGIONAL_HANDOFF
```

Removing each premise returns its own first typed failure.

The operational list is not an independent sufficiency theorem for every real
network. It is the interface contract that makes the mathematical
factorization statement meaningful.

## 7. Three hostile handoffs

### 7.1 Commitment without availability

Consider two histories with the same:

- decision certificate;
- provenance root; and
- committed fork event set.

In one, the branch openings remain available. In the other, the archive has
discarded or withheld them.

The compact record is identical, but:

\[
\operatorname{CanProduceForkProof}=1
\]

in only one history.

Therefore:

\[
\operatorname{CanProduceForkProof}
\not\preceq
(\text{certificate},\text{root}).
\]

Adding a frozen availability bit repairs this finite pair:

\[
\operatorname{CanProduceForkProof}
\preceq
(\text{certificate},\text{root},\text{availability}).
\]

In a real system the repair also needs a retrieval protocol, horizon, access
right, and valid openings.

This distinction is directly aligned with data-availability research:
cryptographic commitment, validity, and data availability are different
assurances. Al-Bassam, Sonnino, and Buterin combine fraud proofs with
probabilistic availability sampling precisely because a light client cannot
infer underlying data availability from a favored header alone
([primary paper](https://arxiv.org/abs/1809.09044)).

### 7.2 Stale membership epoch

Two receiver situations share:

```text
group key + message + valid group-signature semantics
```

In one, the signed epoch equals the receiver's current membership epoch. In the
other, the receiver has advanced to a new membership.

The group record alone does not determine whether execution is authorized.
Binding the signed epoch and admitting receiver epoch context repairs the
finite handoff.

The lesson is not that every certificate must contain a large membership
list. The lesson is that any compressed form must bind an unambiguous
membership commitment whose interpretation is available to the receiver.

### 7.3 Self-confirming interest filter

Both hostile histories begin with preference \(0\) and contain a support event
for \(0\). One later contains a corrective event for \(1\).

The filter forwards only events agreeing with its current preference. It
therefore exports the same support event in both histories and hides the
correction:

\[
V_{\mathrm{adaptive}}(h_0)
=
V_{\mathrm{adaptive}}(h_1),
\]

while:

\[
A(h_0)\ne A(h_1).
\]

This is an exact self-confirming eclipse. The filter is not fitted to the
held-out answer; it is driven by its own current state.

Expanding the interest set to include every declared action-relevant effect
reveals the first omitted distinction in this pair.

### 7.4 Prediction, rollback, and partitioned invariants

Two motion histories can share last position and velocity while differing in
a hidden acceleration. Dead reckoning therefore supports a useful tentative
display but does not exactly determine the next position. Adding the
authoritative acceleration at handoff repairs the pair.

Likewise, two histories can share one tentative preference while later
receiving different certified decisions. The tentative view is sufficient
for a reversible display action and insufficient for irreversible execution.
The joined handoff view determines whether rollback is required.

Finally, neither side of a two-shard allocation closes the global invariant
that total allocation must not exceed one. The joined allocation view does.
This is the smallest control against overreading local action closure:

> selective finality can avoid global replication for one local action
> without making every cross-region invariant coordination-free.

## 8. Monotonicity boundary

Treat record histories as growing sets of signed events.

The predicate:

```text
there exists a signed conflicting pair at this height
```

is monotone under history extension. Once witnessed, later records do not
erase the witness.

The predicate:

```text
no equivocation has occurred
```

is not monotone. A later conflicting branch can falsify it.

This places an exact boundary on regional finality:

- positive encountered-fork evidence can close locally once its authenticity
  and occurrence identity are frozen;
- absence of a fork cannot become globally final from a merely incomplete
  growing view without a closure, horizon, or coordination premise.

This generic coordination boundary is strongly absorbed by the CALM theorem,
which connects coordination-free consistent implementation with monotonic
logic
([Hellerstein and Alvaro](https://arxiv.org/abs/1901.01930)), and by invariant
confluence, which gives an application-invariant-relative necessary and
sufficient condition for safe coordination avoidance
([Bailis et al.](https://arxiv.org/abs/1402.2237)).

Dynamic Unity should not claim those results. Its useful move is to put:

```text
monotone evidence
coordination requirement
selective record fibre
capability-relative finality
physical source boundary
```

on one typed interface.

## 9. Relation to distributed-systems prior art

The distributed result is not a claim that incomplete views are newly
discovered.

- **Partial replication.** PRACTI separates invalidations from data bodies and
  uses conservative imprecise invalidations so nodes can maintain declared
  consistency while storing only data and metadata relevant to them
  ([Belaramani et al.](https://www.usenix.org/legacy/event/nsdi06/tech/full_papers/belaramani/belaramani_html/)).
- **Lower bounds for selective causal metadata.** Partially replicated causal
  memory has topology-dependent necessary metadata; the share graph determines
  which causal edges a replica must track
  ([Xiang and Vaidya](https://arxiv.org/abs/1703.05424)).
- **Area of interest and effect.** Peer virtual-environment work propagates a
  state change when its area of effect intersects a participant's area of
  interest
  ([Heger et al.](https://eceasst.org/index.php/eceasst/article/view/2493)).
- **Attention-relative fidelity.** Donnybrook keeps high-fidelity replicas for
  a small changing interest set and lower-fidelity representations outside it
  ([Bharambe et al.](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/donnybrook.pdf)).
- **Data availability.** Commitment and validity do not by themselves provide
  every receiver the underlying data needed for fraud adjudication
  ([Al-Bassam, Sonnino, and Buterin](https://arxiv.org/abs/1809.09044)).

These are absorbers and engineering exemplars. `HC-DU-050` does not compete
with them as a new networking protocol. It uses their strongest lessons to
freeze the formal interface that a later distributed-to-physical comparison
must preserve.

## 10. Physical-source no-minting boundary

Carry forward the matched null source from `HC-DU-049`.

Let \(T,R_1,R_2\) be independent uniform bits and let every protocol artifact
be a deterministic or stochastic downstream function of:

\[
(R_1,R_2).
\]

The decision is the declared XOR:

\[
d=R_1\oplus R_2.
\]

The complete selective protocol view includes:

- decision;
- valid certificate;
- signer set;
- membership epoch;
- provenance root; and
- available sidecar.

It still does not reconstruct \(T\):

\[
P(T=0\mid V)=P(T=1\mid V)=\frac12.
\]

No filter, partial replica, handoff, compression scheme, quorum, or archive
can mint a target relation absent from the admitted upstream input. This is
the downstream data-processing/no-minting boundary already established across
`HC-DU-047/048/049`.

An independent physical-source attestation can repair source adjudication, but
then the evidentiary work is done by that newly admitted formation channel,
not by regional handoff.

## 11. What is actually new for Dynamic Unity

### Bankable scoped program result

Dynamic Unity can now state:

> Regional finality need not mean one globally replicated state. It can be a
> family of action-relative quotients, each supported by a different
> selective record view. Their safe composition is receiver-contextual.
> Capability enlargement refines the quotient and can reopen prior closure.

This is the missing interface between:

- source formation;
- gossip and DAG pooling;
- metastable preference;
- Byzantine hardening;
- selective replication;
- regional handoff; and
- observer-relative capability.

### Not earned

This swing does not establish:

- that physical reality is a distributed database;
- that a network client is a physical observer;
- that quantum measurement is consensus;
- that there is no global physical state;
- that public facts obey a particular networking protocol;
- that commitment availability is a new law of physics;
- that a regional physical-finality theorem has been proved; or
- that any new empirical prediction has been produced.

### Maximum evidentiary grade

The result is an exact finite formal/program boundary with a regression
certificate. It is not a research-model result and not physical evidence.

## 12. Exact certificate

Run:

```bash
python3 tests/du_capability_relative_selective_view_handoff_probe.py
```

Expected:

```text
HC-DU-050 capability-relative selective-view/handoff certificate: 28/28 passed
```

The artifact is:

```text
tests/artifacts/du_capability_relative_selective_view_handoff_result.json
```

The certificate verifies:

1. exhaustive minimum views for all five frozen actions;
2. route irrelevance for the frozen action family;
3. two incomparable execution-certificate implementations;
4. execution sufficiency without signer sufficiency;
5. strict capability-partition refinement;
6. locally sufficient incomplete regional views;
7. absence of global-history reconstruction;
8. joint-view synergy;
9. commitment/availability separation;
10. stale-epoch handoff failure;
11. self-confirming adaptive-filter failure;
12. interest-expansion first leak;
13. monotone positive fork evidence;
14. nonmonotone absence of fork;
15. dead-reckoning failure under hidden acceleration;
16. authoritative correction and explicit rollback;
17. failure of isolated shards to close a nonlocal quota invariant;
18. physical-source no-minting; and
19. eight handoff-premise first-failure controls.

The script contains no fitted research model. Its finite enumeration preserves
the analytic fibre statements and counterexamples.

## 13. Decision and next work

`N5-SCF-P4` is complete as `HC-DU-050`.

Position 5 is now executable:

```text
N5-SCF-P5
DU Physical Collision and Portfolio Handoff
```

Position 5 must apply the completed distributed stack unchanged to one
physical record arena and the closed metastable host as a hostile control.
It must ask whether:

- physical records supply genuinely new target-sensitive information;
- regional physical access can be typed as action-relative views without
  importing database semantics;
- capability expansion reveals a physical distinction or only an epistemic
  one;
- record availability has a genuine physical counterpart;
- an independently formed source relation survives the full handoff; and
- the translation fails at a precise arrow if no exact physical unification
  is available.

`N5-RS-P2` remains deferred until Position 5 returns the cross-arena portfolio
handoff.

## 14. Stop conditions

Stop this line if a successor:

- treats a commitment as proof of availability;
- treats certificate verification as signer accountability;
- treats “no fork seen” as a monotone fact without a closure premise;
- silently changes receiver epoch or capability;
- fits the interest filter to the held-out action;
- repairs a failed handoff by silently expanding the view;
- infers physical source truth from downstream consensus;
- identifies software regions with physical observers; or
- builds a network simulator before an exact physical collision requires one.
