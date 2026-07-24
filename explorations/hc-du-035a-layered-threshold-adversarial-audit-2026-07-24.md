---
title: "HC-DU-035A layered threshold objectivity — hostile audit"
status: completed_hostile_audit
doc_type: adversarial_audit
created: 2026-07-24
run_id: RUN-20260724-174434-hc-du-035a-layered-threshold
hardening_id: HC-DU-035A
verdict: "LAYER SEPARATION SURVIVES / SINGLE THRESHOLD AND STATIC NOVELTY CLAIMS REJECTED"
banked: false
seeded: false
---

# HC-DU-035A layered threshold objectivity — hostile audit

## Verdict

The exact finite controls survive. The hoped-for universal objectivity
threshold does not.

The wave began with a plausible cross-domain picture:

```text
many fragments
    -> statistical threshold
    -> consensus or finality threshold
    -> quantum-to-classical threshold
    -> enlarged capability
```

Every arrow needs additional typed structure. Fragment accumulation needs a
dependence model. Finality needs authenticated honest intersection and
locking. Public objectivity needs redundant independent access to a compatible
algebra. Capability needs an action-relevant loss and resource contract.
Criticality needs a scaling family and order parameter.

What remains is a strong negative design result:

> Reconstruction, finality, public objectivity, and capability must be
> composed explicitly. None can be substituted for another by using the word
> “threshold.”

## Attack matrix

| Attack | Minimal hostile case | Result | Correction accepted |
|---|---|---|---|
| One scalar threshold is assumed | reconstruction uses sample count; finality uses validator intersections; capability uses risk/cost | quantities live on different parameter spaces | reject the universal scalar; type each threshold |
| Agreement is called truth | \(N=4,f=1,q=3\) safely locks an uninformative or wrong value | incompatible certificates are excluded but reconstruction can fail | finality safety is uniqueness, not accuracy |
| Strong reconstruction is called finality | private evidence has error \(1/10\), while \(N=3,f=1,q=2\) admits a split view | truth estimate does not prevent conflicting certificates | require locking and honest intersection |
| Reconstruction plus finality is called capability | actuator disabled or verification cost exceeds benefit | no new action becomes admissible | freeze action, loss, cost, risk, and resource contract |
| Full history is demanded for every action | history \(H=(G,J)\), but the action depends only on \(G\) | coarse evidence enables the action without full reconstruction | distinguish full-history from action-relevant sufficiency |
| Capability is claimed independent of finality without qualification | local reversible action can proceed under a split view | only public irreversible capability needs public finality by definition | expose \(C_{\rm action}\) and \(C_{\rm public}=F\wedge C_{\rm action}\) |
| Local hardening is declared universally bad | the local output is already sufficient for the declared action | hardening can be lossless and may reduce resource cost | use the exact Bayes-action equality criterion |
| Provenance is confused with confidence | a strong/weak reliability label helps decoding but does not authenticate source identity | statistical weight is not causal independence or signer identity | keep reliability and provenance separate |
| Fragment count is called evidence accumulation | common-shock channel has the same one-fragment accuracy as IID evidence | IID error vanishes; common-shock error has a floor | state the dependence contract |
| Marginal lock reliability is called finality reliability | common-mode lock bug versus IID lock failures | same one-validator marginal gives different conflict risk | carry lock-failure correlations |
| Threshold secret sharing is called consistency | two authorized pairs interpolate secrets \(0\) and \(3\) from inconsistent shares | access alone permits incompatible reconstructions | add dealer consistency or verifiable sharing |
| Signature count is called provenance support | signer list `A,A,B` is treated as three validators | replay passes naive count but fails unique authentication | count roots, not messages |
| Static safety is called liveness | safe \(N=7,f=2,q=5\) system split into components four and three | no component can gather a quorum | add topology, timing, and availability |
| Metastable confidence is called finality | confidence state \(2\) rolls back to \(0\) with probability \(1/7\) before hard boundary \(3\) | confidence is reversible | supply absorbing/locking semantics and rollback bound |
| Adaptive threshold crossing uses a fixed-horizon bound | sample repeatedly until a favorable crossing | nominal confidence is miscalibrated | preregister horizon or use anytime-valid inference |
| GHZ phase is called quantum public objectivity | every proper subset is ignorant and all three shares are required | no redundancy or independent access exists | use GHZ as synergy-only negative control |
| GHZ phase is called a collective quantum-measurement advantage | each party measures \(X\), then parity reveals the bit | local measurements and classical pooling suffice | withdraw the collective-measurement claim |
| GHZ phase is called QEC or general QSS | one missing or malicious share destroys or flips the result | no error correction and only one classical label is encoded | access-only grade |
| Equal quantum marginals are treated as an LOCC no-go | two orthogonal pure states may be LOCC distinguishable | marginal equality is insufficient | use direct joint-channel wording or a proved data-hiding fixture |
| Bell joint access is called finality | Bell measurement identifies a state but supplies no provenance, locking, redundancy, or action | reconstruction only | keep finality separate |
| A finite knee is called a phase transition | no \(N\to\infty\) family or order parameter is supplied | no universality or critical exponent exists | call it a finite crossover or access threshold |
| Static quantum/BFT correspondence is called new | QSS, QEC, quantum Byzantine agreement, and verifiable QSS already exist | conjunction collides with prior art | novelty requires a coupled formation/resource theorem |
| Physical records are claimed to emerge | every evidence and quantum channel is supplied at the readout cut | formation and interface selection remain open | parent `HC-DU-033` remains a dependency |

## Surviving exact propositions

Within the frozen finite contracts:

1. Locked equal-size quorum safety holds exactly when \(2q>N+f\).
2. When the inequality fails, a split view can be constructed without any
   honest validator double-signing.
3. Worst-case withholding availability is distinct and requires
   \(q\le N-f\).
4. The honest-intersection surplus
   \(h=\max(0,2q-N-f)\) is the exact number of additional honest
   double-signers needed to make a conflict constructible.
5. Deterministic hardening cannot improve optimal Bayes risk.
6. The hardening is lossless for a declared zero-one decision exactly when
   every fiber retains a common optimal history; the analogous
   action-sufficiency condition applies to general loss.
7. The two-fragment reliability fixture has exact errors \(7/40\) before and
   \(1/4\) after local sign hardening.
8. IID majority and the declared common-shock channel have equal
   one-fragment accuracy but different accumulation laws.
9. The finite countermodels separate full reconstruction, finality,
   action-relevant capability, and public irreversible capability.
10. The metastable fixture has exact rollback probability \(1/7\).
11. The GHZ phase pair has identical proper-subset reduced states and perfect
    three-share parity access.
12. The four Bell states have identical one-qubit marginals and perfect direct
    joint Bell-basis readout.

## Survives only with labels

- **Evidence** means output of the declared channel, not an independently
  selected physical record.
- **Independent** means the supplied joint law factorizes; distinct message
  paths or names do not establish independence.
- **Provenance** means authenticated causal/source identity, not a reliability
  magnitude.
- **Finality** means incompatible-certificate safety in one instance under
  declared locks and faults; it does not include truth, liveness, view change,
  or common knowledge.
- **Capability** is observer-, action-, risk-, cost-, and resource-relative.
- **Public capability** includes the declared finality requirement; local or
  reversible capability need not.
- **Quantum access** is an authorized-channel statement, not QEC, objectivity,
  collapse, classicality, or ontology.
- **Threshold** means a crossing under a declared parameterized family. It
  does not imply a phase transition.

## Corrections to the original swing

### 1. Rename the object

Use **Layered Threshold Objectivity**, not a universal objectivity threshold.
The output is a no-collapse theorem-and-control package.

### 2. Narrow the hardening claim

The exact claim is not:

```text
always delay local decisions.
```

It is:

```text
preserve an action-sufficient statistic and authenticated provenance
until the decisions that need them have been made.
```

If the local statistic is sufficient, hardening is lossless. If not, the
accuracy loss must be traded against bandwidth, privacy, latency, memory, and
fault containment.

### 3. Split capability

The full truth cube concerns

```text
full reconstruction
+ finality safety
+ action-relevant local capability.
```

For an irreversible public action, finality is an explicit prerequisite:

\[
C_{\mathrm{public}}=F\wedge C_{\mathrm{action}}.
\]

Do not report public capability without that qualification.

### 4. Regrade GHZ

GHZ phase is:

```text
KNOWN 3-of-3 CLASSICAL-LABEL ACCESS IN A QUANTUM STATE
```

It is not:

```text
GENERAL QUANTUM SECRET SHARING
QEC
REDUNDANT OBJECTIVITY
COLLECTIVE-MEASUREMENT ADVANTAGE
PUBLIC FINALITY
```

### 5. Move novelty downstream

The static cross-domain access theorem is already occupied. The next
potentially novel object must begin before the readout cut, at physical
formation, and end after certification, at a strict action/resource
consequence.

## What not to spend more time on

- finding one numerical threshold that overlays sample size, quorum size,
  code distance, and action risk;
- adding more IID voters without a dependence model;
- refining static quorum intersection without view-change or physical
  formation content;
- treating signature aggregation as truth reconstruction;
- treating secret-sharing access as consistency;
- using GHZ as evidence of public classicality;
- claiming LOCC impossibility from equal marginals;
- calling every sigmoid or finite knee criticality;
- juxtaposing Blackwell, QSS, and BFT conditions as a new law; or
- constructing another supplied record channel while leaving its physical
  selection unexplained.

## Remaining hard problem

The hard question is now sharper:

> What must physically change—and what must be paid—to convert a distinction
> that is merely reconstructable by one authorized joint channel into a fact
> that is independently accessible, adversarially fork-safe, stable under the
> required interventions, and useful for a bounded-risk public action?

A successful next theorem needs:

- physical record formation rather than a post-cut channel;
- a direct classical or quantum coalition channel;
- a declared adversary and incompatibility relation;
- public accessibility or approximate broadcastability;
- a strict action consequence; and
- a lower bound or converse on support, disturbance, coherence, redundancy,
  memory, authentication, entropy, or latency.

Until that result:

```text
HC-DU-035A EXACT FINITE CONTROLS SURVIVE
ONE UNIVERSAL OBJECTIVITY THRESHOLD REJECTED
STATIC QUANTUM/BFT NOVELTY REJECTED
PHYSICAL FORMATION-TO-FINALITY RESOURCE LAW OPEN
NO CLAIM BANKED OR SEEDED
```
