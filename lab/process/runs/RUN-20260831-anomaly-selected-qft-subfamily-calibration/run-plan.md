---
title: "Anomaly-selected QFT subfamily and non-copy selector calibration — run plan"
status: complete
doc_type: governed_run_plan
created: 2026-08-31
run_id: RUN-20260831-anomaly-selected-qft-subfamily-calibration
work_id: CCR-ANOMALY-QFT-SUBFAMILY-CALIBRATION
claim_id: HC-DU-213
owner_repo: dynamic-unity
---

# Exact question

Can a standard quantum-field-theoretic consistency condition provide the
first exact positive control for `HC-DU-212`'s non-copy selection gate?

More precisely: in a target-blind bounded family of four-dimensional chiral
`U(1)` Weyl spectra, do cancellation of the cubic gauge anomaly and the mixed
gauge-gravitational anomaly select a proper physical subfamily without
inserting a coordinate isomorphic to the selected spectrum, and does that
subfamily sharpen an independently frozen quadratic representation target?

# Frozen family, quotient, selector, and target

Before enumeration, freeze:

- candidate objects: unordered five-charge multisets of nonzero integers from
  `{-9,...,-1,1,...,9}`;
- primitive normalization: `gcd(|q_i|)=1`;
- chirality: no vectorlike pair `q,-q` occurs in one spectrum;
- representation quotient: charge permutation and simultaneous global sign;
- selector equations:
  `A_1=sum(q_i)=0` and `A_3=sum(q_i^3)=0`;
- held-out target: `B_2=sum(q_i^2)`, the quadratic representation weight;
- secondary untargeted audit: `B_4=sum(q_i^4)` and candidate-count/orbit
  structure; and
- no-refit rule: the charge range, cardinality, quotient, anomaly equations,
  and targets do not change after enumeration.

The known primitive chiral solution `(-9,-5,-1,7,8)` is a positive control,
not the candidate list. The full bounded family is generated independently.

# Attempt order

1. Prove the anomaly equations and the residual representation quotient are
   typed independently of `B_2`.
2. Enumerate the complete frozen family and quotient it exactly.
3. Determine the selected orbit count and the incumbent/selected images of
   `B_2` and `B_4`.
4. Run adversarial controls for range dependence, normalization dependence,
   vectorlike contamination, and target coding.
5. Classify the result as non-copy structural selection, target sharpening,
   absorption, or failure.
6. Apply the result to DU's live candidate classes without promoting a known
   anomaly constraint into new physics or a selected record handoff.

# Evidence, grade, absorbers, and kills

Consumes `HC-DU-211--212`. Primary collision includes Adler/Bardeen anomaly
results and the modern exact `U(1)` anomaly-equation literature.

Maximum grade is scoped Grade 4: a bounded necessity/selection calibration.

Strongest absorbers:

- standard perturbative gauge-anomaly cancellation;
- mixed gauge-gravitational anomaly cancellation;
- Diophantine classification of anomaly-free `U(1)` spectra;
- representation theory and charge-normalization freedom; and
- ordinary one-loop gauge response and renormalization-group theory.

Cheapest kill: the selected family is empty, is not proper, or has the same
`B_2` image as the incumbent; the quotient or target depends on an unfrozen
normalization; or the finite range/cardinality supplies the claimed answer.

Stop if:

- anomaly freedom is called a new DU theorem;
- bounded enumeration is promoted to a universal QFT classification;
- structural consistency is called dynamical issuance;
- charge normalization or a response ruler is hidden;
- target sharpening is called a unique prediction when several values remain;
- a consistency-selected spectrum is called a selected material record; or
- GU, Drafting Factory, a provider, or external hardware is written.

# Local-learning boundary and output

The exact enumeration can reveal orbit counts, minimal examples, target-image
contraction, and range stability on the current computer. It has a complete
pre-hardware checkpoint and no hardware continuation. Literature and formal
analysis own the theorem; any executable artifact is a minimal exhaustive
certificate, not a claim that simulation discovered anomaly cancellation.

Durable output:

- one exact enumeration/proof-boundary probe and deterministic artifact;
- one scoped selection-accounting exploration with primary-source collision;
- one candidate-portfolio consequence and corrected reopener;
- one counter-assumptive finding if the gate changes; and
- one governed run receipt.
