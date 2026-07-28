---
title: "Preactivation commitment provenance and the source-issuance boundary"
status: completed_scoped_result
doc_type: cryptographic_certification_theorem_counterexamples_and_reopener_correction
created: 2026-07-28
run_id: RUN-20260728-165347-preactivation-commitment-source-gate
work_id: PCSG-PREACTIVATION-COMMITMENT-SOURCE-GATE
program_id: CCR-PREDICTIVE-SELECTION-TO-FORECASTING-ISSUANCE
authority: "Joe direct chat: Go"
claim_ids:
  - HC-DU-088
claim_grade: "SCOPED GRADE-4 COMMITMENT-RELATIVE PRIOR-FIXATION AND PHYSICAL-SOURCE ADAPTER NECESSITY / STANDARD CRYPTOGRAPHIC AND FACTORIZATION MATHEMATICS / NO SOURCE ISSUANCE OR NEW PHYSICS"
claim_status_change: "HC-DU-088 banked at scoped grade"
prediction_status_change: none
paper_state_change: none
hardware_state_change: none
current_authority_change: "CURRENT-RESEARCH.yaml revision 39 remains quiescent with no selected successor"
---

# Commitments can prove prior registry fixation—not physical source issuance

## Executive result

`HC-DU-087` named a binding commitment as one possible discriminator between
a type that was fixed before activation and one genuinely issued later.
`HC-DU-088` proves the exact boundary.

A time-anchored, binding commitment can provide strong positive evidence that
a particular registry existed in committed form before activation. A valid
opening can reveal the registry later. A zero-knowledge set proof can certify
membership or nonmembership relative to it while hiding everything beyond the
declared query.

That is real evidence, but it is evidence about the committed
representation:

```text
prior commitment of registry S
  != committer knew every opening at commit time
  != physical source contained every label in S
  != S exhausts the source's fixed generative possibilities
  != a later registry extension was physical source issuance.
```

Two physical histories can have the same prior commitment, membership and
nonmembership proofs, authenticated append-only update, observer access, and
action consequences while differing on whether the later type already existed
in an uncommitted reservoir or was created at activation. Every cryptographic
transcript then factors through the registry history and cannot identify the
physical-source target.

The corrected reopener is therefore:

> A commitment becomes source-sensitive only when an independently selected,
> provenance-bearing physical adapter makes the committed registry faithful
> to—and exhaustive of—the admitted fixed source state, generators,
> boundaries, and controllers.

Cryptography can enforce that the committed representation does not change
silently. It cannot establish the physical adapter or its exhaustiveness.
Those are the source-selection and completion-class obligations the issuance
question already needed.

## 1. What is standard and what is Dynamic Unity's increment?

| label | content | role |
|---|---|---|
| `STANDARD` | binding and hiding commitments, set membership/nonmembership proofs, soundness, zero knowledge, authenticated append-only updates | proof machinery |
| `PROJECT_NATIVE` | registry, physical source state, generator closure, record formation, provenance, access, capability, and issuance remain separate types | attribution boundary |
| `NEW_SCOPED_RESULT` | exact matched-source factorization and the correction of a commitment as a standalone `HC-DU-087` reopener | banked as `HC-DU-088` |

[Pedersen commitments](https://link.springer.com/book/10.1007/3-540-46766-1)
provide the familiar split between information-theoretic hiding and
computational binding. [Zero-knowledge
sets](https://doi.org/10.1109/SFCS.2003.1238183) explicitly support later
membership and nonmembership proofs relative to a committed finite set
without disclosing more than those answers. [Vector
commitments](https://www.iacr.org/archive/pkc2013/77780054/77780054.pdf)
support position binding and authenticated updates. These works supply the
cryptographic functions. None claims that the committed database is a
complete physical ontology.

## 2. Frozen typed object

Let:

- \(H\) be the admitted physical-history class;
- \(X_0(h)\) be the physical source state and fixed source boundary before
  activation;
- \(\mathcal G_0(h)\) be the types generable under the fixed source state,
  law, controller, boundary, seed, and oracle admitted at that time;
- \(S_0(h)\) be a finite committed type registry;
- \(C_0=\operatorname{Com}_{pp}(S_0;r_0)\) be its commitment;
- \(a_0\) be a provenance/time anchor showing that this exact commitment
  existed before activation;
- \(\pi_\tau^+\) or \(\pi_\tau^-\) be a later membership or nonmembership
  proof for type \(\tau\);
- \(U_\tau\) be an authenticated update from \(S_0\) to
  \(S_1=S_0\cup\{\tau\}\);
- \(O_\tau(h)\) state whether a physical occurrence of \(\tau\) is
  independently formed after activation; and
- \(P_\tau(h)=1_{\{\tau\in\mathcal G_0(h)\}}\) be the preactivation physical
  source/generator target.

The cryptographic transcript is:

\[
\Gamma_\tau(h)=
(pp,a_0,C_0,\pi_\tau^\pm,U_\tau,\text{verification results}).
\]

The decisive type distinction is:

\[
\tau\in S_0
\qquad\text{versus}\qquad
\tau\in\mathcal G_0.
\]

The first is a statement about the registry. The second is a statement about
the physical completion class.

## 3. The certification ladder

A commitment-based source claim needs more than “there is a hash.”

| rung | property | what it can establish | what remains open |
|---:|---|---|---|
| C0 | digest or commitment string | stable identifier if retained | binding, hiding, origin |
| C1 | binding | at most one admissible opening, up to security error | disclosure, knowledge, physical truth |
| C2 | hiding | current transcript withholds committed content | absence or nonexistence |
| C3 | sound membership/nonmembership | declared set relation | source fidelity |
| C4 | provenance and time anchor | the same commitment preceded activation | who knew or formed its content |
| C5 | proof of knowledge/extractability | an admitted committer possessed a witness under the proof model | physical source truth |
| C6 | physically formed faithful adapter | registry statements track the declared source variable | omitted generators and controllers |
| C7 | exhaustive fixed-completion theorem | registry equals the admitted fixed generative closure | source extension, conditional on occurrence |

The first five rungs are cryptographic/protocol properties. Rungs C6 and C7
are physical and model-class claims.

Binding is also security-relative. A computationally binding commitment gives
its conclusion against a declared feasible adversary; it is not an
unconditional metaphysical fact. Setup trapdoors, compromised keys, security
parameter, algorithm class, and verification horizon belong in the evidence
grade.

## 4. `HC-DU-088A` — commitment-relative prior-fixation theorem

### Statement

Suppose:

1. \(a_0\) validly anchors \(C_0\) before the activation of \(\tau\);
2. the commitment is binding with failure probability at most
   \(\epsilon_b\);
3. the opening or set proof is sound with failure probability at most
   \(\epsilon_s\); and
4. the anchor/provenance contract fails with probability at most
   \(\epsilon_a\).

Then an accepted later opening to \(S_0\), or an accepted membership or
nonmembership proof for \(\tau\), certifies the corresponding
registry-relative statement about the previously anchored commitment with
failure probability at most:

\[
\epsilon_a+\epsilon_b+\epsilon_s.
\]

If the commitment/proof system is hiding or zero knowledge under its declared
model, that registry statement can have been fixed without the observer
having access to the rest of \(S_0\).

### Proof

The time anchor identifies the prior commitment string. Binding prevents the
same anchored string from supporting inconsistent committed registries, up to
\(\epsilon_b\). Sound verification prevents a false opening, membership
statement, or nonmembership statement relative to that registry, up to
\(\epsilon_s\). The anchor itself can fail only with probability
\(\epsilon_a\). A union bound yields the stated error.

Hiding or zero knowledge concerns the verifier's information about the
committed value or witness. It is logically compatible with binding. Thus
the content can be fixed relative to the commitment while remaining
undisclosed through the admitted view. \(\square\)

### What the theorem does not say

It does not say:

- the committer physically measured the source;
- the committer knew the opening at the commit time without a separate
  proof-of-knowledge contract;
- every registry label denoted an extant physical type;
- the registry contained every dormant state or fixed-generator output;
- the commitment/opening remained available to every observer; or
- a type absent from the registry was absent from the physical source.

This is the precise useful content of “reality as an unopened commitment”:
binding and disclosure can separate. It is not a physical ontology theorem.

## 5. `HC-DU-088B` — physical-source nonidentifiability

### Theorem

If the transcript map factors through the registry/update history,

\[
\Gamma_\tau=\gamma_\tau\circ K,
\]

and the physical pre-existence target \(P_\tau\) is nonconstant on a fibre of
\(K\), then no decoder \(d\) can reconstruct \(P_\tau\) from the complete
cryptographic transcript:

\[
P_\tau\ne d\circ\Gamma_\tau.
\]

### Proof

Choose \(h_D,h_I\in H\) such that:

\[
K(h_D)=K(h_I)
\quad\text{but}\quad
P_\tau(h_D)\ne P_\tau(h_I).
\]

Since \(\Gamma_\tau=\gamma_\tau\circ K\),

\[
\Gamma_\tau(h_D)=\Gamma_\tau(h_I).
\]

Any decoder applied to those equal transcripts returns the same answer, while
the target differs. \(\square\)

### Minimum matched histories

Use the same:

- initial public registry \(S_0\), with \(\tau\notin S_0\);
- commitment randomness and anchored \(C_0\);
- valid nonmembership proof for \(\tau\);
- later independently formed occurrence record for \(\tau\);
- append-only update \(S_1=S_0\cup\{\tau\}\);
- signers, update proof, membership proof under \(S_1\), access, and actions.

Only the hidden physical source differs:

| history | preactivation physical source | registry transcript |
|---|---|---|
| \(h_D\): disclosure | dormant \(\tau\) or fixed generator for \(\tau\) already present | \(\tau\notin S_0\), then authenticated addition |
| \(h_I\): issuance | no admitted preactivation state/generator for \(\tau\) | identical |

The append-only proof certifies:

```text
tau was not in the committed registry S0
tau is in the later committed registry S1
```

It cannot certify:

```text
tau was not in the physical source closure before activation.
```

This counterexample survives a perfect proof system. Stronger cryptography
does not repair an omitted physical adapter.

## 6. A second matched pair: committed labels need not be physical

Let \(S_0\) contain \(\tau\) in both histories and provide an identical valid
membership proof.

- In one history, \(S_0\) is formed from a faithful measurement of a dormant
  physical type.
- In the other, a controller commits the same label while the physical source
  lacks that type until activation.

Every commitment result is identical. Physical pre-existence differs.

Therefore even positive prior membership does not establish physical source
pre-existence unless the registry-to-source formation relation is separately
certified.

This is the same source-attribution boundary previously found for signatures,
quorum certificates, and zero-knowledge relations in `HC-DU-047--051`, now
specialized to preactivation type registries.

## 7. `HC-DU-088C` — exact source-sensitive repair

Define a physical adapter:

\[
e:X_0\longrightarrow S_0
\]

with retained formation provenance. For the source-preexistence question it
must satisfy, over the complete admitted source class:

\[
\tau\in e(X_0)
\iff
\tau\in\mathcal G_0.
\tag{*}
\]

The forward direction blocks false registry inclusions. The reverse direction
blocks omitted dormant types, compact generators, seeds, boundary inputs,
oracles, and controllers.

If:

1. the source boundary and fixed-completion class are frozen independently of
   the result;
2. \(e\) is physically selected or necessary rather than supplied for the
   example;
3. its blank-to-written formation provenance and observer access are retained;
4. equivalence \((*)\) is proved;
5. the commitment/proof security contract holds; and
6. a later physical occurrence \(O_\tau=1\) is independently certified,

then a valid prior nonmembership proof can establish that \(\tau\) lay outside
the admitted fixed generative closure. The later occurrence forces at least
one of:

```text
the source/completion contract was false
the adapter or cryptographic assumptions failed
an external source crossed the declared boundary
the physical source class extended.
```

Calling the last branch “issuance” additionally requires excluding the first
three under the declared scope.

### Necessity

Without the reverse implication in \((*)\), \(h_D\) supplies the hidden
reservoir/fixed-generator counterexample. Without the forward implication, a
valid registry membership proof can concern a label with no physical
pre-existence. Without provenance, the registry may have been preloaded or
formed from an unrelated source. Without a frozen boundary, an external
controller or oracle relocates the source.

The repair is therefore not another cryptographic primitive. It is exactly
the independently warranted completion theorem and physical formation
interface already demanded by Dynamic Unity.

## 8. Failed openings, silence, and unavailable evidence

None of these certifies issuance:

- no commitment was published;
- the observer cannot retrieve an opening;
- the committer refuses to open;
- a proof fails verification;
- the commitment was deleted;
- the observer lacks the decryption or threshold shares; or
- a later type was not queried before activation.

Each has ordinary alternatives: absence of protocol participation, archive
loss, adversarial withholding, key loss, malformed proof, insufficient
capability, or an uncommitted fixed source.

This preserves `HC-DU-050`:

```text
binding != availability != disclosure != observer access.
```

An observer may safely act on a verified predicate while remaining unable to
audit the complete registry or physical source.

## 9. What zero knowledge and threshold opening add

Zero knowledge can change the disclosure surface:

- prove \(\tau\in S_0\) without revealing other registry members;
- prove \(\tau\notin S_0\) without revealing the set;
- prove that a committed update satisfies a declared rule; or
- prove existence of some witness satisfying a predicate without exposing it.

Threshold opening can change which coalition must cooperate before content is
accessible. Homomorphic or MPC evaluation can let a group act on a property
without reconstructing the full registry at any one participant.

These are genuine capability and access changes. They do not change the
physical target when the complete cryptographic input is identical in
\(h_D\) and \(h_I\).

## 10. Result matrix

| evidence | strongest earned statement | not earned |
|---|---|---|
| anchored binding commitment, later valid opening | registry was committed before activation, security-relative | physical source truth or exhaustiveness |
| zero-knowledge membership | queried type belonged to committed registry | other members, physical pre-existence |
| zero-knowledge nonmembership | queried type was outside committed registry | absence from hidden state or generator closure |
| authenticated append-only update | protocol registry extended after anchor | physical source issued the type |
| proof of knowledge at commit time | admitted prover possessed a witness under proof model | physical source contained its denotation |
| faithful but nonexhaustive source adapter | included labels track source | omitted fixed possibilities |
| faithful exhaustive adapter plus later formed occurrence | fixed-completion class is contradicted or extended | unconditional ontology beyond the frozen scope |

## 11. Reopener correction and next boundary

`HC-DU-087` should not list “binding commitment” alone as a route separating
dormant fixed types from source issuance.

The corrected ladder is:

```text
binding commitment
  -> prior fixation relative to a committed representation

binding commitment + physical source provenance
  -> registry-relative source statement

binding commitment + selected faithful exhaustive adapter
+ fixed completion/boundary + formed later occurrence
  -> conditional source-extension discriminator.
```

The remaining low-cost source-sensitive routes are:

1. a preactivation physical intervention whose response differs between a
   dormant fixed type/generator and genuine absence;
2. a preactivation physical footprint with a frozen resource and completion
   class; or
3. an independently proved exhaustive source/completion theorem.

A commitment is useful inside any of those routes for tamper-evident temporal
provenance. It is not a substitute for them.

## 12. Grade, novelty, and stop

`HC-DU-088` earns:

- **Grade 4, scoped certification:** a valid time-anchored binding opening or
  set proof certifies a prior registry-relative statement under explicit
  security errors;
- **Grade 4, scoped necessity:** physical source pre-existence cannot be
  reconstructed when it varies inside a complete cryptographic-transcript
  fibre;
- **Grade 4, scoped adapter necessity:** source-sensitive nonmembership
  requires a faithful exhaustive physical adapter and frozen completion
  boundary;
- **a useful positive:** commitments exactly realize fixed-but-undisclosed
  content and therefore provide a clean disclosure control; and
- **no source issuance, new cryptographic primitive, selected physical record
  interface, new physics, or empirical prediction.**

The components are absorbed by commitment/proof-system security and ordinary
factorization. Dynamic Unity's increment is the typed physical-source
counterexample and correction of its own reopener.

Stop cryptographic strengthening on this branch. Reopen only when a physical
adapter or source theorem—not merely a stronger proof over supplied
statements—changes the matched-history pair.
