#!/usr/bin/env python3
"""Audit the 18-lens Dynamic Unity hypothesis quadratic vote.

This probe is a governance and arithmetic receipt, not scientific evidence.
It validates hypothesis ownership, complete non-owner weighting, no
self-votes, exactly 100 quadratic credits per lens, aggregate rank, and
deterministic machine-readable output.
"""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path
from typing import Any


RUN_ID = "RUN-20260724-195026-technical-lens-hypothesis-vote"
ARTIFACT_PATH = (
    Path(__file__).resolve().parent
    / "artifacts"
    / "du_technical_lens_hypothesis_quadratic_vote_result.json"
)


LENSES = [
    {
        "id": "MC",
        "name": "Metastable consensus",
        "specialty": "Avalanche-style subsampling, hysteresis, and correlated evidence",
    },
    {
        "id": "HG",
        "name": "Hypergraphs and higher-order structure",
        "specialty": "hyperedges, higher categories, loop filling, and gluing",
    },
    {
        "id": "CA",
        "name": "Cellular automata and QCA",
        "specialty": "local reversible dynamics, causal cones, and record formation",
    },
    {
        "id": "DC",
        "name": "Distributed consensus",
        "specialty": "BFT certificates, finality layers, and safe action",
    },
    {
        "id": "AD",
        "name": "Adversarial distributed systems",
        "specialty": "equivocation, adaptive schedules, split views, and fault models",
    },
    {
        "id": "ZK",
        "name": "Zero-knowledge cryptography",
        "specialty": "existence, certification, disclosure, succinctness, and trust",
    },
    {
        "id": "DB",
        "name": "Distributed databases and data networking",
        "specialty": "serializability, provenance, gossip, and anti-entropy",
    },
    {
        "id": "QI",
        "name": "Quantum information and process tensors",
        "specialty": "multi-time instruments, routed implementations, and fixed algebras",
    },
    {
        "id": "QE",
        "name": "Quantum error correction and fault tolerance",
        "specialty": "logical algebras, syndromes, access structures, and thresholds",
    },
    {
        "id": "IT",
        "name": "Information theory and coding",
        "specialty": "confusability, authenticated rate, rate distortion, and task metrics",
    },
    {
        "id": "CT",
        "name": "Control theory and system identification",
        "specialty": "observability, interventions, minimal realization, and finite bases",
    },
    {
        "id": "SP",
        "name": "Stochastic processes and phase transitions",
        "specialty": "percolation, reentrant phases, finite-size scaling, and universality",
    },
    {
        "id": "FM",
        "name": "Formal methods and model checking",
        "specialty": "decidability, counterexample generation, and proof certificates",
    },
    {
        "id": "EM",
        "name": "Experimental metrology and optical clocks",
        "specialty": "proper-time histories, complete outcome records, and calibration",
    },
    {
        "id": "TR",
        "name": "Thermodynamics and resource theory",
        "specialty": "work, support, coherence, reversibility, and optionality",
    },
    {
        "id": "CP",
        "name": "Causal inference and philosophy of science",
        "specialty": "interventional equivalence, actuality, and ontology license",
    },
    {
        "id": "CG",
        "name": "Causal sets and emergent geometry",
        "specialty": "meta-record reconstruction, continuum limits, and curvature",
    },
    {
        "id": "NW",
        "name": "Temporal networks and network science",
        "specialty": "time-respecting cuts, topology, bandwidth, and capability",
    },
]


def hypothesis(
    hypothesis_id: str,
    owner: str,
    slot: str,
    title: str,
    statement: str,
    why: str,
    falsifier: str,
    grade: str,
) -> dict[str, str]:
    return {
        "id": hypothesis_id,
        "owner": owner,
        "slot": slot,
        "title": title,
        "statement": statement,
        "why": why,
        "falsifier": falsifier,
        "grade": grade,
    }


HYPOTHESES = [
    hypothesis(
        "MC-A",
        "MC",
        "primary",
        "Provenance-Weighted Hysteretic Finality",
        "In metastable sampling consensus, the transition to irreversible "
        "action is controlled by effective independent provenance rank and "
        "the protocol spectral gap, producing distinct upward and downward "
        "finality thresholds after marginal vote accuracy is held fixed.",
        "It turns metastability into a measurable capability transition rather "
        "than a confidence metaphor and could distinguish public finality from "
        "smooth accumulation.",
        "Matched finite-size experiments show no hysteresis, or a smooth "
        "history-aware confidence model predicts rollback and action as well "
        "without a threshold.",
        "CONDITIONAL EMPIRICAL HYPOTHESIS",
    ),
    hypothesis(
        "MC-B",
        "MC",
        "frontier",
        "Correlated-Evidence Finality Ceiling",
        "With a nonzero common-shock component, repeated subsampling cannot "
        "drive conflict risk below a correlation floor unless genuinely new "
        "independent provenance enters; more rounds or replicas alone cannot "
        "create public finality.",
        "This would generalize the repository's common-shock control into a "
        "protocol-level stop law for metastable consensus.",
        "A frozen protocol with no new independent evidence beats the derived "
        "correlation floor under the complete adversary and resource contract.",
        "MODEL-CLASS THEOREM CANDIDATE / CROSS-PROTOCOL FORM OPEN",
    ),
    hypothesis(
        "HG-A",
        "HG",
        "primary",
        "Higher-Order Record Insufficiency",
        "There are multi-party record processes with identical vertices, "
        "edges, pairwise overlaps, and pairwise interventions but different "
        "responses to one genuine hyperedge intervention; pairwise graphs are "
        "therefore not sufficient record objects for that class.",
        "A finite constructive counterexample would justify higher-order "
        "records without assuming them and directly sharpen HC-DU-036B.",
        "Every declared higher-order intervention in the frozen class factors "
        "through pairwise records and maps.",
        "FINITE COUNTEREXAMPLE / NECESSITY THEOREM CANDIDATE",
    ),
    hypothesis(
        "HG-B",
        "HG",
        "frontier",
        "Cycle-Filling Public-Finality Theorem",
        "An independently certified higher-order constraint acts like filling "
        "selected reconciliation loops: it quotients the loop action by the "
        "normal closure of the certified syndromes, and the resulting fixed "
        "algebra is exactly the enlarged path-independent public fact algebra.",
        "This gives layered consensus a precise mathematical job and connects "
        "hypergraphs, holonomy, finality, and capability in one theorem.",
        "A frozen higher-order certificate kills the stated loop syndromes but "
        "the computed quotient/fixed algebra fails to match the safe public "
        "facts or actions.",
        "EXACT FINITE THEOREM TARGET / PHYSICAL MAPPING OPEN",
    ),
    hypothesis(
        "CA-A",
        "CA",
        "primary",
        "Homogeneous Reversible Record-Selection No-Go",
        "A finite translation-invariant reversible CA or QCA starting from an "
        "exactly symmetric blank condition cannot uniquely select a nontrivial "
        "local record or pointer algebra without a symmetry-breaking state, "
        "boundary, ancilla, superselection sector, or dissipative/coarse-grained "
        "ingredient.",
        "It would isolate the missing structure in Dynamic Unity's covariant "
        "recorder constructions instead of building another admissible recorder.",
        "A completely homogeneous finite reversible rule and symmetric initial "
        "condition dynamically selects one unique stable nontrivial record "
        "algebra without any listed extra structure.",
        "SCOPED NO-GO CANDIDATE",
    ),
    hypothesis(
        "CA-B",
        "CA",
        "frontier",
        "Local Causal-Cone Witness Bound",
        "For bounded-state, bounded-radius CA/QCA record models, any locally "
        "intervention-distinguishable pair has a separating experiment inside "
        "a causal cone whose depth is bounded by local behavioral rank or "
        "tensor-network realization dimension.",
        "This could turn the finite automata witness theorem into a locality-"
        "respecting physical bound.",
        "A finite model with the declared rank/dimension is locally "
        "distinguishable but first separates beyond every proposed "
        "rank-relative cone bound.",
        "THEOREM CANDIDATE / QUANTUM EXTENSION OPEN",
    ),
    hypothesis(
        "DC-A",
        "DC",
        "primary",
        "Loop-Resolution Finality Criterion",
        "A stronger consensus layer strictly enlarges the bounded-risk action "
        "set if and only if it rejects, repairs, records, or quotients an "
        "action-relevant loop syndrome that the lower layer leaves unresolved; "
        "otherwise it changes only latency, cost, or confidence.",
        "It directly formalizes the user's layered-finality insight and gives "
        "HC-DU-037 a necessary-and-sufficient target.",
        "After complete cost and risk accounting, safe capability strictly "
        "grows even though the upper layer resolves no action-relevant history "
        "distinction, or it resolves one and capability never changes where it "
        "should.",
        "CONDITIONAL NECESSARY-AND-SUFFICIENT THEOREM TARGET",
    ),
    hypothesis(
        "DC-B",
        "DC",
        "frontier",
        "Certified-View Equalizer Theorem",
        "Relative to a declared fault and view-change class, the maximal "
        "fork-safe public fact is the equalizer of all admissible certified "
        "views, not the majority endpoint state.",
        "This is a clean noninvertible successor to the finite holonomy orbit "
        "theorem and a bridge to real consensus protocols.",
        "A fact outside the computed equalizer remains fork-safe, or a fact "
        "inside it yields incompatible authorized actions under the frozen "
        "protocol.",
        "EXACT PROTOCOL-CLASS THEOREM TARGET",
    ),
    hypothesis(
        "AD-A",
        "AD",
        "primary",
        "Equivocation-Provenance Lower Bound",
        "To preserve a task under an adaptive equivocation fault class, an "
        "honest public record needs at least as many authenticated provenance "
        "states as the maximum number of action-distinct adversarial loop "
        "sectors inside one endpoint-record fibre.",
        "It extends project-or-lift from benign loops to adversarial split "
        "views and could yield a tight security lower bound.",
        "A zero-error protocol preserves all declared action sectors with "
        "fewer accessible authenticated states and no additional trust, "
        "secret, or computational assumption.",
        "FINITE INFORMATION/SECURITY LOWER-BOUND TARGET",
    ),
    hypothesis(
        "AD-B",
        "AD",
        "frontier",
        "Adaptive Refinement Dichotomy",
        "For a finite adversary class and finite formed-record refinement "
        "family, either some refinement coequalizes every honest view or an "
        "adaptive schedule yields a bounded split-view intervention witness.",
        "This is the adversarial analogue of factorization-or-witness and would "
        "make the physical-remainder comparison contract executable.",
        "A finite frozen instance has no sufficient refinement and no bounded "
        "adaptive split-view witness, or the proposed bound fails.",
        "DECIDABLE FINITE DICHOTOMY TARGET",
    ),
    hypothesis(
        "ZK-A",
        "ZK",
        "primary",
        "Certification Without Shared Biography",
        "A proposition can become public, robust, and action-enabling through "
        "zero-knowledge certification while the detailed witness history "
        "remains undisclosed and nonreconstructible to the participants.",
        "It cleanly separates existence, binding, certification, disclosure, "
        "and shared biography, constraining any record-first ontology.",
        "Every physically realizable action-enabling certificate in the "
        "declared class requires participants to reconstruct the witness "
        "history.",
        "KNOWN CRYPTOGRAPHIC CONSTRUCTION / PHYSICAL-ONTOLOGY MAPPING OPEN",
    ),
    hypothesis(
        "ZK-B",
        "ZK",
        "frontier",
        "Succinct Proof Does Not Erase Provenance Debt",
        "Succinct or zero-knowledge proof systems can compress disclosure and "
        "verification work, but cannot preserve M action-distinct route sectors "
        "with fewer than M total authenticated support states once the proof, "
        "reference string, verifier key, trust, and computational assumptions "
        "are charged.",
        "It tests whether cryptography genuinely evades project-or-lift or "
        "merely relocates its resources.",
        "A complete protocol preserves M exact action sectors with total "
        "authenticated support below M and no uncharged trust or assumption.",
        "RESOURCE-AWARE LOWER-BOUND CONJECTURE",
    ),
    hypothesis(
        "DB-A",
        "DB",
        "primary",
        "Serializability-Holonomy Correspondence",
        "For a declared reversible transaction-comparison class, a global "
        "serialization exists exactly when loop holonomy acts trivially on the "
        "transaction algebra; when full flatness fails, the holonomy-invariant "
        "subalgebra is exactly the safely serializable public fact.",
        "It joins database correctness to the new public-fixed-algebra theorem "
        "without relying on metaphor.",
        "A scoped history is globally serializable with nontrivial action "
        "holonomy, or the invariant subalgebra contains an unsafe transaction "
        "fact.",
        "EXACT RESTRICTED-CORRESPONDENCE TARGET",
    ),
    hypothesis(
        "DB-B",
        "DB",
        "frontier",
        "Gossip Reconciliation Anti-Monotonicity",
        "Adding an authenticated gossip or anti-entropy edge can increase "
        "information access while reducing safe action throughput because it "
        "reveals a previously hidden conflict cycle; a later resolution layer "
        "restores only the quotient or provenance it explicitly settles.",
        "It gives a directly measurable distributed twin for reconciliation "
        "frustration.",
        "Across matched fixtures, safe throughput is monotone in added edges "
        "or every decrease is fully explained by congestion rather than the "
        "new conflict syndrome.",
        "CONDITIONAL SYSTEMS HYPOTHESIS",
    ),
    hypothesis(
        "QI-A",
        "QI",
        "primary",
        "Implementation-Complete Flatness Null",
        "Within standard quantum theory, every closed-route record signal is "
        "predicted by a complete routed implementation, process tensor, phase "
        "reference, memory, and environmental provenance; no extra "
        "perspectival-curvature variable remains.",
        "This is the decisive null that any new physical curvature proposal "
        "must beat.",
        "Two operationally identical complete process descriptions yield a "
        "repeatable different closed-loop outcome after all ordinary controls.",
        "STANDARD-QUANTUM NULL HYPOTHESIS",
    ),
    hypothesis(
        "QI-B",
        "QI",
        "frontier",
        "Noisy Public Fixed-Algebra Convergence",
        "Repeated noisy reconciliation converges toward the fixed/equalizer "
        "algebra of the generated channel semigroup, with convergence rate "
        "controlled by its spectral gap and safe-action error controlled by "
        "distance to that algebra.",
        "It is the most direct noninvertible and approximate extension of the "
        "new exact finite theorem.",
        "Invariant observables decay or noninvariant observables remain "
        "public without provenance beyond the derived gap/error bound.",
        "QUANTUM CHANNEL-SEMIGROUP THEOREM TARGET",
    ),
    hypothesis(
        "QE-A",
        "QE",
        "primary",
        "Public Fact as Correctable Logical Algebra",
        "Relative to an observer-access and adversary class, durable public "
        "facts are exactly the correctable logical observable algebra; an "
        "objectivity threshold coincides with correctability, not raw "
        "redundancy.",
        "It could unify public facts, logical codes, adversaries, and bounded-"
        "risk action using mature but precise machinery.",
        "A durable fork-safe public capability lies outside the correctable "
        "algebra, or a correctable logical fact fails public action after "
        "access and decoder resources are matched.",
        "CROSS-PLATFORM CORRESPONDENCE HYPOTHESIS",
    ),
    hypothesis(
        "QE-B",
        "QE",
        "frontier",
        "Syndrome-Provenance Duality",
        "The minimum provenance register needed to preserve a noninvariant "
        "task is isomorphic, in an appropriate code construction, to the "
        "syndrome information needed to correct the corresponding "
        "reconciliation errors.",
        "It would turn project-or-lift into a quantum error-correction theorem "
        "rather than an analogy.",
        "The code corrects all declared route sectors with a smaller syndrome "
        "space than the exact action-relative provenance requirement, or the "
        "mapping changes the task semantics.",
        "CONSTRUCTIVE DUALITY CONJECTURE",
    ),
    hypothesis(
        "IT-A",
        "IT",
        "primary",
        "Action-Relative Reconciliation Rate",
        "The asymptotic authenticated communication rate required to establish "
        "a shared action is the conditional graph-entropy or rate-distortion "
        "quantity of the action-confusability relation, not the entropy of the "
        "raw history.",
        "It supplies a task-sensitive quantitative law for reality bandwidth "
        "and provenance cost.",
        "A protocol beats the derived rate under the same side information and "
        "fault class, or the optimum varies independently of the declared "
        "confusability object.",
        "INFORMATION-THEORETIC LAW TARGET",
    ),
    hypothesis(
        "IT-B",
        "IT",
        "frontier",
        "No Universal Informational Distance",
        "No single task-independent scalar informational distance determines "
        "reconciliation fidelity, cost, and capability for all admitted "
        "interventions; the natural geometry is a task-indexed family, "
        "possibly directed or Finsler-like.",
        "A no-go would prevent Dynamic Unity from forcing unlike access "
        "relations into one unearned metric.",
        "One representation-invariant scalar predicts all declared task rates, "
        "errors, and capabilities across a sufficiently rich intervention "
        "class.",
        "NO-GO CONJECTURE",
    ),
    hypothesis(
        "CT-A",
        "CT",
        "primary",
        "Joint Observability-Action Finality Equivalence",
        "A shared record becomes action-enabling exactly when combined "
        "observability separates every state pair requiring different safe "
        "actions within the declared risk, control, and resource bounds.",
        "It translates public finality into a necessary-and-sufficient control "
        "condition rather than a confidence threshold.",
        "A safe action distinction exists without joint observability, or full "
        "joint observability fails to enable the action after all declared "
        "control and cost conditions hold.",
        "CONTROL-THEORETIC CORRESPONDENCE TARGET",
    ),
    hypothesis(
        "CT-B",
        "CT",
        "frontier",
        "Finite Intervention-Basis Compactness",
        "For a bounded finite-dimensional instrument and refinement family, a "
        "finite tester basis suffices to decide factorization for every "
        "candidate and yields a uniform finite remainder certificate.",
        "This attacks the most important blocker left by HC-DU-036A: a uniform "
        "witness across an admissible physical refinement class.",
        "A family satisfying the declared compact finite-dimensional "
        "conditions requires infinitely many independent testers or evades "
        "every proposed uniform certificate.",
        "HIGH-PRIORITY COMPACTNESS THEOREM TARGET",
    ),
    hypothesis(
        "SP-A",
        "SP",
        "primary",
        "Reentrant Public-Fact Transition",
        "As authenticated connectivity rises, access first percolates, loop "
        "frustration then reduces invariant public capacity, and higher-order "
        "hardening finally restores a protected quotient, producing a "
        "reentrant or hysteretic public-fact phase diagram.",
        "It combines the new anti-monotonic theorem with a risky scaling "
        "prediction rather than assuming a one-way objectivity transition.",
        "Finite-size families show only monotone or smooth reliability after "
        "access, conflict, and hardening are separately measured.",
        "SPECULATIVE STOCHASTIC-PHASE HYPOTHESIS",
    ),
    hypothesis(
        "SP-B",
        "SP",
        "frontier",
        "Objectivity Phase Scaling Discriminator",
        "A genuine public-fact phase transition exhibits preregistered "
        "finite-size collapse, susceptibility, and critical scaling that a "
        "smooth architecture-specific reliability curve cannot reproduce.",
        "It supplies a clean empirical standard for deciding whether "
        "objectivity is a phase or only a threshold convention.",
        "The proposed scaling exponents drift arbitrarily with architecture, "
        "or a smooth finite model absorbs the complete scaling surface.",
        "EMPIRICAL DISCRIMINATOR HYPOTHESIS",
    ),
    hypothesis(
        "FM-A",
        "FM",
        "primary",
        "Decidable Refinement-Trichotomy Compiler",
        "For finite noninvertible record networks and a finite formed-"
        "refinement class, an algorithm can return exactly one of "
        "factorization, interface incompleteness with a sufficient refinement, "
        "or class-relative remainder with a bounded intervention witness.",
        "This turns the program's ontology discipline into an executable "
        "scientific product and supplies the next swing's core.",
        "The algorithm misclassifies an exhaustive finite instance, lacks the "
        "declared witness/refinement certificate, or its complexity bound "
        "fails.",
        "DECIDABLE FINITE THEOREM/COMPILER TARGET",
    ),
    hypothesis(
        "FM-B",
        "FM",
        "frontier",
        "Machine-Checkable Ontology License",
        "Every finite class-relative physical-remainder claim can carry a "
        "machine-checkable certificate that the witness separates the "
        "candidate and every admissible formed refinement; absent such a "
        "certificate, only interface insufficiency is licensed.",
        "It makes ontology inflation technically auditable and reusable across "
        "platforms.",
        "A correct finite remainder result cannot be represented by any "
        "finite proof certificate under the declared semantics, or the "
        "certificate accepts a false remainder.",
        "FORMAL ASSURANCE THEOREM TARGET",
    ),
    hypothesis(
        "EM-A",
        "EM",
        "primary",
        "Proper-Time Robust Separability",
        "For a specified coherent optical-clock instrument, the complete "
        "clock, motion, port, setting, and provenance record has positive "
        "distance from the convex set of every admitted classical proper-time "
        "history after calibrated preparation, leakage, phase, detector, and "
        "drift errors.",
        "This is the nearest physical stop/go test for the record-refinement "
        "program.",
        "The physical alternative lies inside the calibrated null set or its "
        "robust margin is no larger than systematic uncertainty.",
        "OPEN PHYSICAL HYPOTHESIS / HC-DU-034B SEAM",
    ),
    hypothesis(
        "EM-B",
        "EM",
        "frontier",
        "Clock Provenance-Capacity Threshold",
        "In a coherent multi-route clock network, path-independent action on a "
        "chosen noninvariant readout is restored exactly when accessible "
        "authenticated route states reach the task-sector count predicted by "
        "the project-or-lift bound, while invariant clock observables remain "
        "stable throughout.",
        "It is a direct measurable prediction of the finite provenance theorem "
        "inside a quantum-history platform.",
        "The capability threshold occurs at a different accessible-state count "
        "after phase, memory, noise, and coding resources are controlled.",
        "EXPERIMENTAL HYPOTHESIS / PLATFORM OPEN",
    ),
    hypothesis(
        "TR-A",
        "TR",
        "primary",
        "Finality-Optionality Resource Inequality",
        "At fixed reliability and action task, stronger public finality must "
        "consume additional physical support, work, or authenticated memory, "
        "or reduce coherent/reversible optionality; a resource monotone bounds "
        "the trade.",
        "It would turn the program's strongest capability intuition into a "
        "quantitative cross-platform law.",
        "A protocol delivers strictly stronger finality with an unchanged "
        "complete resource ledger and unchanged reversible/coherent options.",
        "HIGH-IMPACT RESOURCE-LAW CONJECTURE",
    ),
    hypothesis(
        "TR-B",
        "TR",
        "frontier",
        "No Residual Actualization Cost",
        "After complete Landauer, measurement, communication, authentication, "
        "memory, coherence, and displaced-information accounting, no additional "
        "physical cost depends only on semantic completion-space reduction.",
        "This is the necessary null against which any reconciliation or "
        "actualization heat law must compete.",
        "Matched reversible protocols exhibit a reproducible residual cost "
        "scaling with independently formed completion-class contraction.",
        "ORTHODOX RESOURCE NULL",
    ),
    hypothesis(
        "CP-A",
        "CP",
        "primary",
        "Intervention-Indexed Actuality",
        "The physically meaningful fact relative to an agent is an equivalence "
        "class of histories with identical responses to that agent's admitted "
        "interventions; expanding the intervention set can split a former fact "
        "into newly actionable distinctions.",
        "It ties actuality to operational content while keeping observer and "
        "intervention relativity explicit.",
        "Two histories in the same complete intervention-response class yield "
        "different admitted predictions or capabilities.",
        "OPERATIONAL DEFINITION/THEOREM SCHEMA",
    ),
    hypothesis(
        "CP-B",
        "CP",
        "frontier",
        "No-Finite-Metaphysics Theorem",
        "Two ontologies inducing the same complete operational process cannot "
        "be distinguished by an experiment inside that process class; an "
        "ontological verdict requires an expanded process, a novel prediction, "
        "or explicitly nonempirical criteria such as compression or uniqueness.",
        "It prevents finite experiments from being asked to choose between "
        "descriptions that agree by construction.",
        "An experiment wholly inside the shared complete process selects one "
        "ontology while preserving operational identity.",
        "EXACT PROGRAM-LEVEL NO-GO",
    ),
    hypothesis(
        "CG-A",
        "CG",
        "primary",
        "Certified Meta-Record Geometry Reconstruction",
        "A suitably rich network of who can certify whose records, with "
        "provenance, primitive operational influence, and independently "
        "justified event density, reconstructs causal order, dimension, and "
        "metric scale up to gauge and predicts held-out geometric observables.",
        "This is the direct route from certified causal reality to spacetime "
        "rather than an analogy between graphs and geometry.",
        "Nonisomorphic geometries share the complete declared meta-record "
        "structure but disagree on a held-out observer-accessible experiment, "
        "or scale/dimension must be inserted.",
        "FOUNDATIONAL RECONSTRUCTION CONJECTURE",
    ),
    hypothesis(
        "CG-B",
        "CG",
        "frontier",
        "Coarse-Grained Holonomy-Curvature Bridge",
        "Under a controlled refinement and continuum limit, reconciliation "
        "holonomy of physically formed record perspectives converges to a "
        "spacetime connection curvature that predicts transport or geometric-"
        "phase observables.",
        "This is the most profound possible bridge from the current exact "
        "finite theorem to physical geometry.",
        "No covariant discretization-independent limit exists, the map depends "
        "arbitrarily on record cover, or known geometric/process phases absorb "
        "every proposed signal.",
        "WILD FOUNDATIONAL CONJECTURE",
    ),
    hypothesis(
        "NW-A",
        "NW",
        "primary",
        "Temporal Min-Cut Reality Bandwidth",
        "The maximum asymptotic rate at which two perspectives can establish "
        "mutually certified action facts is bounded, and under declared coding "
        "conditions attained, by a time-respecting authenticated min-cut of "
        "their temporal record network.",
        "It supplies an operational, nonspatial reality-bandwidth law with a "
        "clear network test.",
        "A protocol exceeds the cut under the same trust and resource class, "
        "or achievable certified rate varies independently of the cut after "
        "coding assumptions hold.",
        "NETWORK INFORMATION-LAW TARGET",
    ),
    hypothesis(
        "NW-B",
        "NW",
        "frontier",
        "Topology-Capability Response Law",
        "For a fixed action task, the marginal capability effect of adding a "
        "network edge decomposes into time-respecting access gain minus loop-"
        "frustration and provenance cost; spatial distance alone cannot "
        "predict the sign.",
        "It could unify informational closeness, reconciliation frustration, "
        "and capability in a measurable engineering law.",
        "No task-stable decomposition predicts matched edge-addition "
        "experiments, or spatial/ordinary channel variables absorb every "
        "effect.",
        "CROSS-PLATFORM NETWORK CONJECTURE",
    ),
]


POSITIVE_BALLOTS: dict[str, list[tuple[str, int]]] = {
    "MC": [
        ("DC-A", 8), ("SP-A", 4), ("QI-B", 3), ("HG-B", 2),
        ("TR-A", 2), ("QE-A", 1), ("FM-A", 1), ("EM-B", 1),
    ],
    "HG": [
        ("DC-A", 9), ("QI-B", 3), ("DB-A", 2), ("CG-B", 2),
        ("FM-A", 1), ("QE-B", 1),
    ],
    "CA": [
        ("QI-A", 6), ("FM-A", 5), ("CT-B", 4), ("CG-A", 3),
        ("HG-A", 2), ("QI-B", 2), ("EM-A", 2), ("CP-B", 1),
        ("NW-A", 1),
    ],
    "DC": [
        ("HG-B", 9), ("AD-A", 3), ("DB-A", 2), ("FM-A", 2),
        ("QE-A", 1), ("SP-A", 1),
    ],
    "AD": [
        ("DC-B", 8), ("ZK-B", 4), ("FM-A", 3), ("HG-B", 2),
        ("QE-A", 2), ("DB-A", 1), ("CP-B", 1), ("CT-B", 1),
    ],
    "ZK": [
        ("DC-B", 6), ("QE-A", 5), ("IT-A", 4), ("HG-B", 3),
        ("FM-B", 2), ("AD-A", 2), ("TR-A", 2), ("EM-A", 1),
        ("CG-A", 1),
    ],
    "DB": [
        ("DC-A", 5), ("HG-B", 4), ("FM-A", 4), ("AD-A", 3),
        ("IT-A", 3), ("QI-B", 2), ("NW-A", 2), ("SP-A", 2),
        ("CT-A", 2), ("QE-A", 2), ("ZK-A", 1), ("EM-A", 1),
        ("HG-A", 1), ("CP-B", 1), ("CG-A", 1),
    ],
    "QI": [
        ("QE-A", 9), ("EM-A", 3), ("HG-B", 2), ("CP-B", 2),
        ("FM-A", 1), ("TR-A", 1),
    ],
    "QE": [
        ("QI-B", 6), ("DC-B", 5), ("ZK-A", 4), ("HG-B", 3),
        ("TR-A", 2), ("FM-A", 2), ("EM-B", 2), ("IT-A", 1),
        ("CP-A", 1),
    ],
    "IT": [
        ("ZK-B", 5), ("AD-A", 4), ("HG-B", 4), ("CT-A", 3),
        ("DC-B", 3), ("QE-B", 2), ("NW-A", 2), ("FM-A", 2),
        ("TR-A", 2), ("ZK-A", 2), ("QI-B", 1), ("FM-B", 1),
        ("EM-A", 1), ("SP-A", 1), ("DB-A", 1),
    ],
    "CT": [
        ("FM-A", 8), ("CA-B", 4), ("QI-A", 3), ("DC-A", 2),
        ("EM-A", 2), ("HG-A", 1), ("CP-A", 1), ("AD-B", 1),
    ],
    "SP": [
        ("MC-A", 8), ("QI-B", 4), ("DC-A", 3), ("HG-B", 2),
        ("TR-A", 2), ("NW-A", 1), ("EM-B", 1), ("FM-A", 1),
    ],
    "FM": [
        ("CT-B", 9), ("DC-A", 3), ("HG-B", 2), ("CA-B", 2),
        ("QI-A", 1), ("AD-B", 1),
    ],
    "EM": [
        ("QI-A", 9), ("FM-A", 3), ("CT-B", 2), ("QI-B", 2),
        ("ZK-A", 1), ("TR-A", 1),
    ],
    "TR": [
        ("QI-B", 6), ("DC-A", 5), ("QE-A", 4), ("ZK-A", 3),
        ("HG-B", 2), ("EM-A", 2), ("CP-B", 2), ("IT-A", 1),
        ("SP-A", 1),
    ],
    "CP": [
        ("ZK-A", 5), ("QI-A", 4), ("CT-B", 4), ("CG-A", 3),
        ("HG-A", 3), ("FM-B", 2), ("DC-B", 2), ("IT-B", 2),
        ("EM-A", 2), ("QE-A", 2), ("HG-B", 1), ("NW-A", 1),
        ("AD-A", 1), ("TR-A", 1), ("DB-A", 1),
    ],
    "CG": [
        ("HG-A", 9), ("QI-A", 3), ("NW-A", 2), ("CT-B", 2),
        ("CP-A", 1), ("DB-A", 1),
    ],
    "NW": [
        ("IT-A", 5), ("DC-A", 4), ("DB-A", 4), ("CG-A", 3),
        ("HG-B", 3), ("AD-A", 2), ("CT-A", 2), ("QI-B", 2),
        ("EM-B", 2), ("HG-A", 2), ("FM-A", 1), ("QE-A", 1),
        ("ZK-A", 1), ("SP-A", 1), ("TR-A", 1),
    ],
}


def main() -> None:
    lens_ids = [lens["id"] for lens in LENSES]
    hypothesis_ids = [item["id"] for item in HYPOTHESES]
    owner_by_hypothesis = {
        item["id"]: item["owner"] for item in HYPOTHESES
    }
    title_by_hypothesis = {
        item["id"]: item["title"] for item in HYPOTHESES
    }

    checks: list[dict[str, Any]] = []

    checks.append(
        {
            "name": "eighteen unique lenses present",
            "passed": len(lens_ids) == len(set(lens_ids)) == 18,
            "detail": {"lens_count": len(lens_ids)},
        }
    )

    ownership_counts = {
        lens_id: sum(
            item["owner"] == lens_id for item in HYPOTHESES
        )
        for lens_id in lens_ids
    }
    checks.append(
        {
            "name": "exactly two unique hypotheses per lens",
            "passed": (
                len(hypothesis_ids) == len(set(hypothesis_ids)) == 36
                and all(count == 2 for count in ownership_counts.values())
            ),
            "detail": {
                "hypothesis_count": len(hypothesis_ids),
                "ownership_counts": ownership_counts,
            },
        }
    )

    required_fields = (
        "id", "owner", "slot", "title", "statement",
        "why", "falsifier", "grade",
    )
    complete_hypotheses = all(
        all(str(item[field]).strip() for field in required_fields)
        and item["slot"] in {"primary", "frontier"}
        for item in HYPOTHESES
    )
    checks.append(
        {
            "name": "all hypotheses have scope, value, falsifier, and grade",
            "passed": complete_hypotheses,
            "detail": {"required_fields": list(required_fields)},
        }
    )

    ballots: list[dict[str, Any]] = []
    vote_totals: defaultdict[str, int] = defaultdict(int)
    supporter_sets: defaultdict[str, set[str]] = defaultdict(set)
    received_costs: defaultdict[str, int] = defaultdict(int)
    self_vote_count = 0
    total_credits = 0
    total_vote_units = 0

    for voter in lens_ids:
        positive_pairs = POSITIVE_BALLOTS[voter]
        positive = dict(positive_pairs)
        duplicate_positive_ids = (
            len(positive_pairs) != len(positive)
        )
        owned = {
            hypothesis_id
            for hypothesis_id, owner in owner_by_hypothesis.items()
            if owner == voter
        }
        self_vote_count += sum(
            positive.get(hypothesis_id, 0) > 0
            for hypothesis_id in owned
        )

        weights: dict[str, int | None] = {}
        for hypothesis_id in hypothesis_ids:
            if hypothesis_id in owned:
                weights[hypothesis_id] = None
            else:
                weights[hypothesis_id] = positive.get(hypothesis_id, 0)

        cost = sum(
            int(weight) ** 2
            for weight in weights.values()
            if weight is not None
        )
        vote_units = sum(
            int(weight)
            for weight in weights.values()
            if weight is not None
        )
        total_credits += cost
        total_vote_units += vote_units

        for hypothesis_id, weight in weights.items():
            if weight is None:
                continue
            vote_totals[hypothesis_id] += weight
            received_costs[hypothesis_id] += weight * weight
            if weight > 0:
                supporter_sets[hypothesis_id].add(voter)

        ballots.append(
            {
                "voter": voter,
                "owned_hypotheses": sorted(owned),
                "weights": weights,
                "positive_allocations": [
                    {
                        "hypothesis_id": hypothesis_id,
                        "title": title_by_hypothesis[hypothesis_id],
                        "vote_units": weight,
                        "quadratic_cost": weight * weight,
                    }
                    for hypothesis_id, weight in positive_pairs
                ],
                "duplicate_positive_ids": duplicate_positive_ids,
                "quadratic_credits_spent": cost,
                "vote_units_cast": vote_units,
            }
        )

    checks.append(
        {
            "name": "every ballot explicitly weights every non-owned hypothesis",
            "passed": all(
                len(ballot["weights"]) == 36
                and sum(
                    weight is None
                    for weight in ballot["weights"].values()
                ) == 2
                and not ballot["duplicate_positive_ids"]
                for ballot in ballots
            ),
            "detail": {
                "weights_per_ballot": 36,
                "owned_exclusions_per_ballot": 2,
            },
        }
    )

    checks.append(
        {
            "name": "no lens votes on its own hypotheses",
            "passed": self_vote_count == 0,
            "detail": {"self_vote_count": self_vote_count},
        }
    )

    ballot_costs = {
        ballot["voter"]: ballot["quadratic_credits_spent"]
        for ballot in ballots
    }
    checks.append(
        {
            "name": "every lens spends exactly one hundred quadratic credits",
            "passed": all(cost == 100 for cost in ballot_costs.values()),
            "detail": {"ballot_costs": ballot_costs},
        }
    )

    checks.append(
        {
            "name": "aggregate credit and vote totals reconcile",
            "passed": total_credits == 1800 and total_vote_units == 436,
            "detail": {
                "total_quadratic_credits": total_credits,
                "total_vote_units": total_vote_units,
            },
        }
    )

    ranked_ids = sorted(
        hypothesis_ids,
        key=lambda hypothesis_id: (
            -vote_totals[hypothesis_id],
            -len(supporter_sets[hypothesis_id]),
            hypothesis_id,
        ),
    )
    ranking = [
        {
            "rank": rank,
            "hypothesis_id": hypothesis_id,
            "title": title_by_hypothesis[hypothesis_id],
            "owner": owner_by_hypothesis[hypothesis_id],
            "vote_units": vote_totals[hypothesis_id],
            "supporting_lenses": len(supporter_sets[hypothesis_id]),
            "supporters": sorted(supporter_sets[hypothesis_id]),
            "quadratic_credits_received": received_costs[hypothesis_id],
        }
        for rank, hypothesis_id in enumerate(ranked_ids, start=1)
    ]

    checks.append(
        {
            "name": "all hypotheses appear exactly once in deterministic rank",
            "passed": (
                len(ranking) == 36
                and {item["hypothesis_id"] for item in ranking}
                == set(hypothesis_ids)
                and ranking[0]["hypothesis_id"] == "HG-B"
                and ranking[1]["hypothesis_id"] == "DC-A"
            ),
            "detail": {
                "ranked_count": len(ranking),
                "top_two": [
                    ranking[0]["hypothesis_id"],
                    ranking[1]["hypothesis_id"],
                ],
            },
        }
    )

    failed = [check for check in checks if not check["passed"]]
    result = {
        "probe": "du_technical_lens_hypothesis_quadratic_vote_probe",
        "run_id": RUN_ID,
        "status": "EXPLORATORY_PRIORITY_SIGNAL_ONLY",
        "scientific_evidence": False,
        "authorization_effect": "NONE",
        "rules": {
            "lenses": 18,
            "hypotheses_per_lens": 2,
            "hypotheses": 36,
            "credits_per_lens": 100,
            "quadratic_cost": "sum(vote_units^2)",
            "self_votes": "forbidden on both owned hypotheses",
            "zero_weights": "explicit for every non-owned unselected hypothesis",
            "rank_order": (
                "total vote units descending, supporting lenses descending, "
                "hypothesis id ascending"
            ),
        },
        "lenses": LENSES,
        "hypotheses": HYPOTHESES,
        "ballots": ballots,
        "ranking": ranking,
        "totals": {
            "quadratic_credits": total_credits,
            "vote_units": total_vote_units,
            "self_votes": self_vote_count,
        },
        "checks_passed": sum(check["passed"] for check in checks),
        "checks_total": len(checks),
        "checks": checks,
        "not_established": [
            "truth of any hypothesis",
            "scientific evidence from persona agreement",
            "novelty or publishability",
            "core hypothesis promotion",
            "prediction or claim banking",
            "authorization of the next research swing",
        ],
    }

    ARTIFACT_PATH.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    if failed:
        raise AssertionError(failed)

    print(
        f"{result['checks_passed']}/{result['checks_total']} checks passed; "
        f"{total_credits} credits; {total_vote_units} vote units; "
        f"winner={ranking[0]['hypothesis_id']}"
    )


if __name__ == "__main__":
    main()
