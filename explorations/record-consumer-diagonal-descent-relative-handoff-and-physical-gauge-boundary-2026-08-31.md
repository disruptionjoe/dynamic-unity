---
title: "Record-consumer diagonal descent, relative handoff, and the physical-gauge boundary"
status: banked_scoped_selection_or_joint_descent_result
doc_type: exploration
created: 2026-08-31
claim_id: HC-DU-204
run_id: RUN-20260831-144802-record-consumer-diagonal-descent
program_id: CCR-MINIMAL-PHYSICAL-ANTECEDENT-TO-FINITE-REMAINDER
owner_repo: dynamic-unity
evidence_grade: 4
---

# Executive result

`HC-DU-159` and `HC-DU-172` proved that a bare process does not naturally
select an informative record instrument. `HC-DU-181` then established the
correct alternative: select an interface or prove that the target descends
across the interface family. `HC-DU-203` exposed the next missing object: a
record may prescribe a correction without any physical system consuming it.

The present swing joins those results and corrects one remaining over-demand:

> Physics need not select an absolute record encoding and an absolute consumer
> separately. It may select a matched record-consumer relation—or an orbit of
> such matched pairs—provided the complete declared physical response descends
> across that orbit.

An absolute label such as “Bell outcome 2” or “decoder status 1” is not the
capability. Capability depends on whether the receiving controller gives that
label the matching physical meaning. A coordinated relabeling of both sides is
harmless. Relabeling only the producer or only the consumer generally changes
the response.

This yields an exact **selection-or-joint-descent boundary**:

```text
point-select record and consumer
  OR
select a matched orbit and prove full physical descent
  OR
retain a physical alignment/provenance coordinate.
```

The theorem is elementary composition/factorization mathematics. Quantum
combs, link products, Pauli frames, feedback control, automata minimization,
coding, and state-space realization absorb it. DU's gain is a sharper North-
Star object: the target-blind physical antecedent may select a relational
handoff class rather than a privileged internal code.

This is scoped Grade 4 as a necessity and nonimplication result. It does not
show that the Bell or QEC specimens dynamically select their own controllers;
it creates no new empirical prediction, observer ontology, regional finality
law, paper, or successor.

# Frozen types

Let `X` be a physical input/history class, `R` a finite formed record carrier,
and `Y` a declared response space. Write

```text
K(r | x)  : physical producer / record instrument
C(y | r)  : physical consumer / continuation
```

for stochastic kernels. Their closed response is

```text
H(y | x) = sum_r C(y | r) K(r | x).
```

In quantum language, an instrument has CP maps `{I_r}` and an
outcome-conditioned continuation has channels `{C_r}`. The closed channel is

```text
Gamma = sum_r C_r o I_r.
```

The record carrier, its material formation, and the consumer remain present in
the expanded description even when the final closed map forgets the internal
wire.

# The diagonal handoff theorem

Let `pi:R->R` be a bijective re-encoding. Define

```text
K^pi(r | x) = K(pi^-1(r) | x),
C^pi(y | r) = C(y | pi^-1(r)).
```

## Theorem 1 — matched diagonal descent

The co-transformed pair has exactly the same closed response:

```text
sum_r C^pi(y | r) K^pi(r | x) = H(y | x).
```

### Proof

Substitute `s=pi^-1(r)`. Because `pi` is a bijection, the sum becomes

```text
sum_s C(y | s) K(s | x).
```

The quantum statement is the same reindexing of
`sum_r C_r o I_r`. No dynamical claim is required. The theorem says only that
an internal record alphabet has no absolute physical meaning when producer
and consumer transform together.

## Theorem 2 — unmatched-handoff criterion

If only the producer is re-encoded while `C` is fixed, the response becomes

```text
H_pi(y | x) = sum_s C(y | pi(s)) K(s | x).
```

Therefore the unmatched change is harmless exactly when

```text
sum_s [C(. | pi(s)) - C(. | s)] K(s | x) = 0
```

for every admitted `x`.

For a deterministic producer whose image is `S subset R`, this reduces to

```text
C(. | pi(r)) = C(. | r)  for every r in S.
```

Thus the harmless unmatched transformations form the stabilizer of the
consumer on the reachable record set. Enlarging the action/target family can
only shrink that stabilizer.

# Why this is not automatic physical gauge

The theorem proves formal response descent under relabeling. Calling the
relabeling physical gauge requires more:

- the material encoding and write process must be related by an admitted
  physical or representational equivalence;
- timing, energy, reliability, archive, reset, and fault behavior must descend;
- provenance and access paths must transform coherently;
- every declared intervention and capability must descend; and
- the transformation cannot be fitted after seeing a held-out target.

A transformation may therefore be gauge for one action and physical for
another retained coordinate. This is not subjectivity. It is an objective
statement about which closed physical relations the declared task probes.

# Bell application

The Bell quotient in `HC-DU-201` has four Pauli labels. In the ideal
teleportation identity, branch `P` produces the conditional state `P rho P`,
and the matching consumer applies or tracks `P`.

The exact probe exhausts all `24` permutations of `{I,X,Y,Z}`:

| Contract | Harmless permutations |
|---|---:|
| Producer and correction table co-transform | `24/24` |
| Producer relabeled, full unknown-qubit correction fixed | `1/24` |
| Producer relabeled, terminal `Z` statistic only | `4/24` |

The full correction signatures of the four Paulis are distinct, so an
unmatched full-qubit handoff permits only the identity. A terminal `Z`
statistic distinguishes only whether the Pauli commutes or anticommutes with
`Z`, leaving the four permutations within those two sign classes.

This is the exact physical meaning of action-relative record equivalence:

```text
absolute Pauli-label spelling       representation
matched label-to-correction relation capability-bearing
terminal-Z sign quotient            sufficient only for that terminal task.
```

The Arenskötter et al. source,
[Phys. Rev. Research 6, 023061 (2024)](https://doi.org/10.1103/PhysRevResearch.6.023061),
reports the formed Bell outcome and conditional process tomography but no
outcome-conditioned physical Pauli gate. The descent theorem therefore
clarifies the required controller; it does not retrofit one into the source.

# Real-time QEC application

`HC-DU-169` and `HC-DU-170` supply the materially different positive control.
In the Riverlane/Rigetti packet, decoder statuses obey

```text
0 -> idle,
1 -> conditional X,
2 -> idle.
```

The public source describes the record-consuming controller workflow and
route architecture and supplies aggregate physical feedback evidence, although
it lacks per-attempt actuation lineage. See the
[primary paper](https://arxiv.org/abs/2410.05202) and the source-pinned local
audits.

For the action target alone, the unmatched policy stabilizer contains two
permutations:

```text
identity,
swap status 0 with status 2.
```

But the retained timing law separates statuses `0` and `2` in every audited
round. Their swap is therefore harmless for the binary actuation branch and
physical for the resource/timing coordinate.

The same definitions have now transferred unchanged:

```text
Bell:  record -> correction prescription / terminal frame
QEC:   record -> real-time command / aggregate physical feedback
```

The difference is not quantum versus classical. It is whether a material
consumer is part of the source-grounded process and which target family is
declared.

# The corrected North-Star object

The prior shorthand asked physics to select a material record interface and
then an observer/access/continuation algebra. That remains one sufficient
route, but it is stronger than necessary.

The minimum honest target is now:

```text
target-blind physical antecedent
  -> point-selected record-consumer pair
     OR matched pair orbit with complete physical descent
  -> material formation and provenance
  -> physically realized consumption
  -> declared capability/resource/horizon response
  -> reconstruction or finite remainder.
```

This avoids two opposite mistakes:

1. demanding a privileged internal label when only a relative handoff is
   physical; and
2. calling an unmatched or target-dependent reconfiguration “gauge” merely
   because one endpoint statistic is unchanged.

The possible high-ceiling extension is now precise: local record-consumer
orbits could compose into regional public-finality structures. That extension
is not earned here. It first needs a physical composition rule preserving
formation, provenance, faults, resources, and downstream capabilities.

# Absorber and novelty audit

The formal content is mature:

- Chiribella, D'Ariano, and Perinotti's
  [quantum-comb framework](https://arxiv.org/abs/0904.4483) represents networks
  and their connection through the link product;
- their [quantum-supermap framework](https://arxiv.org/abs/0804.0180) types
  transformations of operations;
- [software Pauli tracking](https://arxiv.org/abs/1401.5872) explicitly
  propagates teleportation byproducts and reinterprets outputs;
- feedback control and automata distinguish internal encodings from closed
  input-output behavior; and
- minimal state-space realizations are ordinarily unique only up to internal
  similarity transformations.

Therefore neither theorem is claimed as new mathematics. The DU increment is
the typed physical consequence and its transfer across two source-grounded
record/consumer specimens:

> interface nonselection does not by itself block capability when the complete
> matched handoff descends; it does block claims about the unmatched producer,
> consumer, material lineage, or action family.

# Grade, stop, and reopener

- **Grade 4:** exact matched-descent and unmatched-stabilizer necessity
  boundary, plus source-grounded cross-specimen transfer.
- **Not earned:** physical selection of either apparatus/controller from bare
  dynamics, per-attempt QEC actuation provenance, a universal observer,
  regional finality, empirical excess, or new physics.
- **Stop:** do not demand unique label names; do not infer a consumer from a
  prescription; do not call endpoint invariance full physical gauge; do not
  generate further finite relabeling variants.
- **Reopen:** one physical model must select a matched producer-consumer orbit
  target-blindly, demonstrate material formation and consumption, and pass an
  unchanged held-out response/resource/provenance family. A regional extension
  additionally needs a no-refit composition law across several such loops.

# Executable control

`tests/du_record_consumer_diagonal_descent_probe.py` verifies:

1. exact stochastic descent for all six relabelings of a three-label handoff;
2. `1,296` exhaustive deterministic encoder/policy/permutation cases;
3. the exact reachable-policy stabilizer criterion;
4. Bell stabilizer contraction from terminal `Z` to arbitrary qubit
   continuation;
5. the QEC action stabilizer and timing counter-witness; and
6. consistency with the banked Bell and QEC source-audit artifacts.

Passing validates these formal and artifact-consistency controls only. It does
not validate the source experiments, select a physical loop, or establish a
new law.
