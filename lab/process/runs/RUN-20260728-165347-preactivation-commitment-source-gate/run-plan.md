---
title: "Preactivation commitment and physical-source gate — run plan"
status: completed
doc_type: governed_run_plan
created: 2026-07-28
run_id: RUN-20260728-165347-preactivation-commitment-source-gate
work_id: PCSG-PREACTIVATION-COMMITMENT-SOURCE-GATE
program_id: CCR-PREDICTIVE-SELECTION-TO-FORECASTING-ISSUANCE
authority: "Joe direct chat: Go"
owner_repo: dynamic-unity
---

# Can a prior commitment distinguish disclosure from issuance?

## Question

`HC-DU-087` proved that record-graph settlement cannot distinguish a type
created at activation from a fixed dormant type activated later. It named a
binding commitment as one possible source-sensitive reopener.

What does a commitment actually certify?

In particular:

1. can a time-anchored binding commitment certify that a later type was fixed
   in a prior registry without disclosing it then;
2. can a membership or nonmembership proof certify physical source
   pre-existence or absence; and
3. can an append-only extension receipt distinguish source issuance from
   disclosure by a hidden reservoir or fixed generator?

## Frozen contract

- **Primary Lane:** 1, supported by 3, 4, 5, and 7.
- **Channels:** formal, literature collision, and synthesis.
- **Maximum grade:** scoped Grade 4 certification/necessity boundary using
  standard commitment, proof-system, and factorization mathematics; no new
  cryptographic primitive, physical source issuance, or new physics.
- **Commitment object:** a finite set or typed registry \(S_0\), commitment
  \(C_0\), provenance/time anchor \(a_0\), and later opening, membership,
  nonmembership, or authenticated update proof.
- **Physical target:** whether type \(\tau\) existed in the admitted physical
  source before activation, kept separate from whether its label belonged to
  \(S_0\).
- **Strongest absorbers:** fixed hidden reservoir, fixed generator, completed
  history, uncommitted source state, non-extractive commitments, compromised
  setup, unavailable openings, and a supplied rather than selected
  registry-to-source adapter.
- **Cheapest kill:** construct two physical source histories with identical
  commitments, proofs, updates, access, and actions but different
  preactivation physical type status.
- **Local-model boundary:** exact definitions, proof, and the minimum matched
  histories decide the question. No cryptographic implementation, stochastic
  simulation, or hardware is warranted.
- **Hardware:** unavailable and irrelevant.

## Method

1. Type binding, hiding, soundness, temporal anchoring, knowledge,
   availability, physical source fidelity, and exhaustiveness separately.
2. Prove the strongest valid registry-relative prior-fixation statement.
3. Carry zero-knowledge membership and nonmembership through the same typing.
4. Build matched physical histories with the same cryptographic transcript
   and different physical source pre-existence.
5. State the exact additional adapter and exhaustiveness conditions under
   which a registry result would become source-sensitive.
6. Test append-only registry extension and failed opening as proposed issuance
   witnesses.
7. Correct the `HC-DU-087` reopener and return the minimum remaining physical
   discriminator.

## Stop

Stop when the cryptographic transcript either factors through the committed
registry and therefore fails on a matched physical-source pair, or one exact
security property plus independently selected physical adapter defeats that
pair. Do not treat a label commitment as a physical inventory, binding as
knowledge, hiding as absence, nonmembership as ontic nonexistence, or protocol
extension as source issuance.
