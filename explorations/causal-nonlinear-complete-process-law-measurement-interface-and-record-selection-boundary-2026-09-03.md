---
title: "Causal nonlinear complete-process law, measurement-interface, and record-selection boundary"
status: banked_scoped_result
doc_type: exploration
created: 2026-09-03
claim_id: HC-DU-230
maximum_grade: 4
primary_lane: 1
supporting_lanes: [3, 7]
channels: [CH-FORMAL, CH-COLLIDE]
---

# Result

Existing nonlinear frameworks prove that `HC-DU-229` must not be read as a
universal impossibility theorem. They also sharpen the cost of leaving its
assumptions:

> A complete causal or no-signalling nonlinear process law can escape the
> fixed-state affine boundary, but causal admissibility does not select the
> measured observable, apparatus coupling, pointer family, realized outcome,
> archive, provenance, or observer-access relation. Those are a second
> physical-selection problem.

Neither audited framework derives the low-amplitude cutoff in `PRED-DU-006`.
The complete-process reopener therefore remains unmet.

# Typed audit contract

The candidate must distinguish at least:

```text
physical state and its required history/boundary data
nonlinear evolution and coupling constants
multi-system composition
spacelike locality / no-signalling
relativistic covariance / foliation independence
measurement observable and interaction
state-update rule
realized outcome
material retention and provenance
observer access and downstream action
```

A law may complete some rows without completing all of them.

# Kaplan--Rajendran: a real class exit with explicit purchases

Kaplan and Rajendran add state-dependent terms to QFT by replacing interacting
field operators with expectation values in the full quantum state. Retarded
Green functions make the low-energy single-particle evolution depend on the
state's past light cone. This is not the naive branchwise cutoff rejected by
`HC-DU-229`; it changes the dynamics and multi-particle contract at the field-
theory level.

The framework supplies real structure that the cutoff lacked:

- nonlinear evolution is interaction- and field-dependent;
- the full past history, or the wavefunction on an initial slice plus a
  background sourced-field boundary value, is required;
- separated systems receive an additive field-theoretic composition rule;
- retarded propagation and factorized evolution are used to argue causality;
  and
- norm preservation supports probabilistic interpretation.

Those are meaningful purchases. They show that a causal nonlinear escape class
is not empty. They do **not** supply Dynamic Unity's missing selector.

The paper defines measurement by bringing a system into contact with a
measuring device prepared in a sufficiently stable state. To measure a chosen
Hermitian observable, the interaction Hamiltonian is designed to correlate its
eigenstates with chosen, easily interpreted apparatus states. The observable,
apparatus initial state, interaction, and pointer family are therefore inputs
to the measurement construction. The nonlinear dynamics generally prevents
perfectly orthogonal, stationary, repeatable pointer states; the authors call
measurement unavoidably noisy and finally define it using energy eigenstates
or coherent states of the **linear** apparatus Hamiltonian to stay close to
ordinary quantum mechanics.

So the framework provides a conditional measurement dynamics:

```text
chosen observable
+ prepared apparatus
+ engineered coupling
+ full-state nonlinear law
-> imperfect correlated apparatus states
```

It does not provide:

```text
nonlinear law -> uniquely selected observable/apparatus/pointer/archive
```

Nor does it derive the threshold form `max(Tr(P rho)-c,0)`, the value of `c`,
an all-attempt detector census, or a provenance-bearing record transducer.

# Fiorentino--Weigert: no-signalling still leaves update freedom

Fiorentino and Weigert hold the ordinary finite-dimensional quantum state
space, unitary evolution, tensor-product composition, projective observables,
and Born probabilities fixed. They vary only the post-measurement update map.
Their generalized update rules take a supplied outcome projector and supplied
pre-measurement state to a subnormalized post-measurement state.

They require completeness/context independence, local covariance,
self-consistency, no-signalling, and local commutativity. Multiple
unconventional rules survive those requirements, including passive,
correlation-free, depolarizing, and probability-amplifying examples in
different scopes. Thus no-signalling plus their core consistency conditions
does not uniquely select the Lüders rule. For composite systems, their Theorem
2 recovers Lüders only after adding both coherence and composition
compatibility.

This is an exact positive and an exact limit for DU:

- **positive:** alternative state-update theories can be specified coherently
  enough to escape a simplistic universal signalling argument;
- **limit:** the rules begin after a measurement and outcome projector have
  already been supplied, and the whole framework keeps observables and Born
  probabilities as axioms;
- **selection consequence:** operational consistency does not by itself choose
  the update rule, much less the physical apparatus that makes and retains an
  outcome record.

Some nonlinear rules make proper and improper mixtures operationally
distinguishable, confirming `HC-DU-229`'s statement that an escape changes the
state/composition contract. That is a purchased extra structure, not a repair
of the old state-only rule.

# Causality is not one checkbox

Four properties must not be collapsed:

| property | question |
|---|---|
| retarded/local source dependence | does the generator use only admitted causal support? |
| no-signalling | can a spacelike choice change local operational statistics? |
| relativistic covariance | do different frames describe the same law? |
| foliation independence | does hypersurface evolution give one result independent of slicing? |

Kaplan--Rajendran claim a causal and gauge-invariant construction. A 2026
Tomonaga--Schwinger analysis by Hsu argues that generic state-dependent terms
fail integrability and operational locality. Diósi's primary-source comment
argues that Hsu's covariance calculation is mistaken: local nonlinear
Tomonaga--Schwinger evolution can remain integrable, while acausality may still
arise from entanglement plus local measurements if collapse is imposed.

This exchange does not settle the Kaplan--Rajendran framework here. It does
settle a DU typing rule: covariance, foliation independence, local generator
support, and operational no-signalling require separate proofs. Calling a
framework “causal” cannot stand in for all four.

# Exact implication boundary

Let a candidate package be

\[
\mathcal P=(\mathcal S,\mathcal H,\mathcal C,\mathcal U,
             \mathcal M,\mathcal R,\mathcal A),
\]

where `S` is the state/history domain, `H` the evolution law, `C` composition,
`U` the update rule, `M` the physical measurement interface, `R` the retained
record/provenance map, and `A` the observer action/access class.

Kaplan--Rajendran materially strengthens `(S,H,C)` and gives a conditional
measurement construction after much of `M` is supplied. Fiorentino--Weigert
hold `(S,H,C)` and the observable part of `M` fixed while proving that several
`U` remain admissible under their core constraints. Neither supplies a map

\[
(\mathcal S,\mathcal H,\mathcal C)
\longrightarrow
(\mathcal M,\mathcal R,\mathcal A)
\]

that is natural, target-blind, and physically selecting.

Therefore:

1. nonlinear causal/no-signalling theories are a genuine logical escape from
   the state-only affine boundary;
2. the escape purchases a larger typed theory rather than validating the old
   cutoff;
3. completing evolution and update does not imply record-interface selection;
   and
4. `PRED-DU-006` reopens only if one source-owned package predicts its local
   contrast, predicts zero spacelike contrast, and supplies the complete
   apparatus/provenance/all-attempt semantics without refit.

# Absorber, novelty, and disposition

The mathematical and physical components are absorbed by nonlinear quantum
mechanics, QFT measurement models, generalized instruments/update rules,
Gisin--Polchinski analysis, and relativistic integrability work. DU's useful
result is the typed nonimplication and reopener audit, not a new nonlinear law.

- **Earned grade:** scoped Grade 4 necessity/nonimplication boundary.
- **Not earned:** evidence for a cutoff, a selected record ontology, a new
  physical law, anomaly, standalone paper, ready successor, or hardware action.
- **Local model:** rejected as `DESK_RESEARCH_FIRST`; reproducing the cited
  equations would add no decision-changing result.
- **Portfolio:** remain `no_ready`.

# Primary sources

- Kaplan and Rajendran, [Causal framework for nonlinear quantum
  mechanics](https://doi.org/10.1103/PhysRevD.105.055002), *Phys. Rev. D* 105,
  055002 (2022); [arXiv full text](https://arxiv.org/abs/2106.10576).
- Fiorentino and Weigert, [Beyond the projection postulate and back: Quantum
  theories with generalized state-update rules](https://doi.org/10.1103/2zpm-jsh7),
  *Phys. Rev. A* 113, 012204 (2026); [arXiv full
  text](https://arxiv.org/abs/2506.06207).
- Hsu, [Relativistic covariance and nonlinear quantum mechanics:
  Tomonaga--Schwinger analysis](https://arxiv.org/abs/2511.15935) (2026).
- Diósi, [Comment on “Relativistic covariance and nonlinear quantum mechanics:
  Tomonaga--Schwinger analysis”](https://arxiv.org/abs/2602.06845) (2026).
