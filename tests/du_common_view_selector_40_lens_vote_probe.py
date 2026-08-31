#!/usr/bin/env python3
"""Audit the forty-lens common-view-selector hypothesis vote.

This is a reproducible research-prioritization receipt, not scientific
evidence.  Forty inline lenses each own one hypothesis.  Every lens casts a
separate 100-credit linear ballot and a 100-credit quadratic ballot over the
other thirty-nine hypotheses.  The probe also reports disciplinary graph
distance so broad cross-community curiosity cannot be confused with a single
school voting for its own vocabulary.
"""

from __future__ import annotations

import json
import math
from collections import Counter, defaultdict, deque
from pathlib import Path
from statistics import median
from typing import Any


RUN_ID = "RUN-20260831-183600-common-view-selector-40-lens-vote"
ARTIFACT_PATH = (
    Path(__file__).resolve().parent
    / "artifacts"
    / "du_common_view_selector_40_lens_vote_result.json"
)


def lens(
    lens_id: str,
    name: str,
    family: str,
    community: str,
    specialty: str,
    tags: tuple[str, ...],
    priorities: tuple[str, str],
) -> dict[str, Any]:
    return {
        "id": lens_id,
        "name": name,
        "family": family,
        "community": community,
        "specialty": specialty,
        "tags": list(tags),
        "priorities": list(priorities),
    }


LENSES = [
    lens("C01", "Distributed-systems architect", "computational", "consensus_networks", "safety, liveness, partial order, and fault models", ("composition", "finality", "fixed_point"), ("integration", "falsifiability")),
    lens("C02", "Hashgraph and gossip-about-gossip specialist", "computational", "consensus_networks", "event DAGs, virtual voting, and provenance", ("dag", "provenance", "composition"), ("selection", "tractability")),
    lens("C03", "Avalanche metastable-consensus specialist", "computational", "consensus_networks", "subsampling, hysteresis, metastability, and correlated evidence", ("threshold", "stability", "finality"), ("falsifiability", "novelty")),
    lens("C04", "Byzantine-fault-tolerance theorist", "computational", "consensus_networks", "quorum certificates, adversaries, and safe action", ("certificate", "finality", "adversary"), ("falsifiability", "tractability")),
    lens("C05", "CRDT and monotone-computation specialist", "computational", "data_composition", "join semilattices, monotonicity, and convergence", ("composition", "monotone", "fixed_point"), ("integration", "tractability")),
    lens("C06", "Distributed-database serializability expert", "computational", "data_composition", "transaction histories, isolation, and consistency", ("history", "composition", "provenance"), ("selection", "falsifiability")),
    lens("C07", "Event-sourcing and provenance architect", "computational", "data_composition", "append-only lineage, replay, and auditability", ("record", "provenance", "history"), ("integration", "tractability")),
    lens("C08", "Zero-knowledge cryptographer", "computational", "security_provenance", "proof without witness disclosure and composable verification", ("certificate", "provenance", "privacy"), ("novelty", "integration")),
    lens("C09", "Threshold-cryptography specialist", "computational", "security_provenance", "distributed openings, access structures, and threshold trust", ("threshold", "certificate", "access"), ("falsifiability", "novelty")),
    lens("C10", "MPC and homomorphic-computation specialist", "computational", "security_provenance", "joint computation over inaccessible local states", ("privacy", "capability", "composition"), ("integration", "novelty")),
    lens("C11", "Network information theorist", "computational", "information_control", "capacity, rate distortion, and channel coding", ("capacity", "ruler", "sufficiency"), ("falsifiability", "tractability")),
    lens("C12", "Statistical sufficiency and information-bottleneck theorist", "computational", "information_control", "minimal sufficient representations and task-relative compression", ("sufficiency", "minimality", "record"), ("selection", "tractability")),
    lens("C13", "Control and observability theorist", "computational", "information_control", "minimal realization, interventions, and observability", ("action", "sufficiency", "ruler"), ("falsifiability", "tractability")),
    lens("C14", "Programming-languages and refinement-type theorist", "computational", "formal_math", "typed interfaces, parametricity, and coherent refinement", ("naturality", "composition", "gauge"), ("selection", "integration")),
    lens("C15", "MMO networking architect", "computational", "consensus_networks", "client prediction, regional authority, reconciliation, and interest management", ("regional", "finality", "access"), ("integration", "falsifiability")),
    lens("C16", "Sharded-ledger and cross-shard protocol specialist", "computational", "data_composition", "local settlement, atomic cross-shard commits, and bridges", ("regional", "gluing", "finality"), ("integration", "novelty")),
    lens("C17", "Neural-network representation researcher", "computational", "computation_learning", "predictive bottlenecks, latent state, and representation learning", ("prediction", "minimality", "stability"), ("tractability", "integration")),
    lens("C18", "Computational-mechanics theorist", "computational", "computation_learning", "causal states, predictive equivalence, and epsilon machines", ("prediction", "sufficiency", "history"), ("selection", "tractability")),
    lens("C19", "Error-correcting-code and fault-tolerance theorist", "computational", "computation_learning", "logical algebras, code distance, and recoverability", ("logical", "stability", "access"), ("integration", "falsifiability")),
    lens("C20", "Complexity and emergence theorist", "computational", "computation_learning", "irreducibility, emergence, and resource-bounded equivalence", ("complexity", "minimality", "composition"), ("novelty", "selection")),
    lens("P21", "Orthodox quantum measurement theorist", "math_physics", "quantum_measurement", "instruments, pointer observables, and measurement models", ("instrument", "record", "stability"), ("selection", "tractability")),
    lens("P22", "Decoherence and Quantum-Darwinism theorist", "math_physics", "quantum_measurement", "environment-induced superselection and redundant records", ("redundancy", "record", "stability"), ("falsifiability", "tractability")),
    lens("P23", "Algebraic-QFT and modular-theory specialist", "math_physics", "field_spacetime", "local algebras, modular flow, and type-III structure", ("algebra", "naturality", "response"), ("selection", "integration")),
    lens("P24", "Quantum-information sufficiency theorist", "math_physics", "quantum_measurement", "Petz recovery, correctable algebras, and channel comparison", ("sufficiency", "logical", "instrument"), ("tractability", "falsifiability")),
    lens("P25", "Quantum-reference-frame theorist", "math_physics", "foundations_causal", "relational observables, perspective changes, and gauge descent", ("relational", "gauge", "naturality"), ("integration", "novelty")),
    lens("P26", "Quantum-instrument and dilation theorist", "math_physics", "quantum_measurement", "instruments, dilations, fixed points, and nonunique realizations", ("instrument", "fixed_point", "access"), ("selection", "falsifiability")),
    lens("P27", "Open-quantum-systems theorist", "math_physics", "quantum_measurement", "Lindbladians, metastability, noiseless subsystems, and pointer sectors", ("stability", "algebra", "threshold"), ("tractability", "falsifiability")),
    lens("P28", "Nonequilibrium statistical physicist", "math_physics", "field_spacetime", "entropy production, phases, and driven steady states", ("stability", "threshold", "response"), ("falsifiability", "integration")),
    lens("P29", "Stochastic-process and filtration theorist", "math_physics", "foundations_causal", "stopping times, filtrations, martingales, and absorbing classes", ("history", "finality", "threshold"), ("tractability", "falsifiability")),
    lens("P30", "Causal-inference and counterfactual statistician", "math_physics", "foundations_causal", "interventions, identifiability, and causal-state quotients", ("action", "sufficiency", "provenance"), ("falsifiability", "selection")),
    lens("P31", "Sheaf, cohomology, and contextuality theorist", "math_physics", "formal_math", "local sections, gluing, obstructions, and holonomy", ("gluing", "regional", "naturality"), ("novelty", "integration")),
    lens("P32", "Category and topos theorist", "math_physics", "formal_math", "universal properties, natural transformations, and descent", ("naturality", "fixed_point", "gluing"), ("selection", "integration")),
    lens("P33", "Differential geometer", "math_physics", "field_spacetime", "metrics, connections, principal symbols, and calibrated frames", ("ruler", "gauge", "response"), ("selection", "falsifiability")),
    lens("P34", "Hyperbolic-PDE and microlocal analyst", "math_physics", "field_spacetime", "characteristics, symmetrizers, propagation, and well-posedness", ("ruler", "response", "stability"), ("tractability", "falsifiability")),
    lens("P35", "Variational and spectral-action theorist", "math_physics", "field_spacetime", "actions, Hessians, stationary structure, and spectral selection", ("action", "response", "selection"), ("selection", "integration")),
    lens("P36", "Direct-action and absorber theorist", "math_physics", "foundations_causal", "pairwise source response without independent field degrees", ("relational", "response", "provenance"), ("novelty", "falsifiability")),
    lens("P37", "Renormalization-group and EFT theorist", "math_physics", "field_spacetime", "stable low-energy observable structure and universality", ("stability", "coarse_grain", "algebra"), ("integration", "tractability")),
    lens("P38", "Causal-set and quantum-gravity theorist", "math_physics", "field_spacetime", "order, volume, sprinkling, and continuum reconstruction", ("ruler", "causal", "regional"), ("novelty", "falsifiability")),
    lens("P39", "Gauge-theory and generalized-symmetry specialist", "math_physics", "field_spacetime", "Wilson operators, superselection sectors, and higher-form symmetry", ("gauge", "algebra", "gluing"), ("selection", "novelty")),
    lens("P40", "Philosopher of physics and model-theory skeptic", "math_physics", "foundations_causal", "empirical equivalence, ontology license, and no-go structure", ("regional", "relational", "minimality"), ("falsifiability", "novelty")),
]


def hypothesis(
    hypothesis_id: str,
    title: str,
    statement: str,
    decisive_test: str,
    strongest_absorber: str,
    tags: tuple[str, ...],
    qualities: tuple[int, int, int, int, int],
) -> dict[str, Any]:
    keys = ("selection", "integration", "falsifiability", "novelty", "tractability")
    return {
        "id": hypothesis_id,
        "owner": hypothesis_id,
        "title": title,
        "statement": statement,
        "decisive_test": decisive_test,
        "strongest_absorber": strongest_absorber,
        "tags": list(tags),
        "qualities": dict(zip(keys, qualities, strict=True)),
        "grade": "GRADE_0_HYPOTHESIS",
    }


HYPOTHESES = [
    hypothesis("C01", "Common-View Fixed-Point Law", "A physical interaction network selects the least stable fixed point at which its record, admissible-action, composition, finality, and comparison maps become mutually closed under every lawful continuation.", "Exhibit one frozen physical process with two inequivalent stable closures, or derive a unique closure without target fitting.", "distributed fixed-point semantics and bisimulation", ("composition", "finality", "fixed_point", "selection"), (4, 5, 5, 4, 4)),
    hypothesis("C02", "Causal-Gossip View-Selection Law", "The transitive signed event DAG of a closed interaction process uniquely selects the common-view family through ancestry, famous-witness-style agreement, and invariant causal provenance.", "Hold the complete DAG fixed and vary admissible view families; uniqueness wins and any inequivalent survivor kills the claim.", "event structures, Lamport order, and Hashgraph representation", ("dag", "provenance", "composition", "selection"), (3, 4, 5, 4, 4)),
    hypothesis("C03", "Metastable Evidence-Closure Law", "Matched views become physical when repeated independent local response sampling crosses a provenance-adjusted metastability threshold, with hysteresis separating formation from erasure.", "Derive and test a threshold invariant under representation and common-shock controls; smooth ordinary decoherence kills the excess claim.", "metastability, percolation, and decoherence", ("threshold", "stability", "finality", "provenance"), (3, 4, 5, 4, 4)),
    hypothesis("C04", "Typed Quorum Actuality Law", "A distinction becomes safely action-enabling exactly when a physically defined adversary class makes its provenance certificate intersect every incompatible lawful continuation in a quorum.", "Specify the physical adversary and prove quorum intersection; an equally lawful conflicting continuation after certification kills it.", "BFT quorum-intersection theorems", ("certificate", "finality", "adversary", "action"), (3, 4, 5, 3, 4)),
    hypothesis("C05", "Monotone Actuality-Join Law", "Public classical facts are the least join-closed monotone substructure of local formed records, and nonclassicality is precisely the failure of candidate merges to be monotone and confluent.", "Construct the physical join and show order-independent convergence; contextual or reversible records that falsely pass the join test kill it.", "CRDT/CALM and categorical classical structures", ("composition", "monotone", "fixed_point", "record"), (3, 4, 5, 3, 4)),
    hypothesis("C06", "Global-History Serializability Criterion", "A global physical history exists for an admitted record network if and only if every physically executable local transaction history admits one gauge-respecting common serialization.", "Find a finite record network whose intervention statistics agree locally but whose serialization verdict disagrees with global-history existence.", "contextuality, consistent histories, and database serializability", ("history", "composition", "provenance", "gauge"), (3, 4, 5, 4, 4)),
    hypothesis("C07", "Provenance-Closed Record Law", "The physically selected record of an occurrence is the minimal append-only causal lineage sufficient to reproduce every admissible downstream response while forbidding source-substituted twins.", "Use history twins and source swaps to test whether one minimal lineage is physically selected rather than analyst-chosen.", "event sourcing, process tensors, and sufficient statistics", ("record", "provenance", "history", "sufficiency"), (4, 5, 5, 3, 5)),
    hypothesis("C08", "Proof-Carrying Actuality Law", "A shared physical fact is a locally retained commitment plus a composable proof that every admitted rival completion violates the same physical response constraints, without requiring disclosure of the completing history.", "Build a physical verification map and show zero-knowledge separation between certification and disclosure; imported trusted setup kills physical selection.", "interactive proofs, hypothesis testing, and quantum verification", ("certificate", "provenance", "privacy", "selection"), (3, 4, 5, 5, 3)),
    hypothesis("C09", "Threshold-Opening Formation Law", "A latent relational distinction becomes publicly actual only when a physically selected access structure combines enough independent shares to open one irreversible, provenance-bearing record.", "Identify naturally formed shares and threshold; an arbitrary partition or ordinary coarse graining absorbs the proposal.", "secret sharing, superselection, and measurement amplification", ("threshold", "certificate", "access", "record"), (3, 4, 5, 4, 3)),
    hypothesis("C10", "Private-State Public-Capability Law", "Physics can select a common actionable reality from relational response proofs even when no observer or region reconstructs the underlying local state, so shared capability is more fundamental operationally than shared disclosure.", "Hold public responses fixed while varying hidden states and test no-refit capability transfer; ordinary operational equivalence absorbs a null.", "MPC, operational theories, and zero-knowledge", ("privacy", "capability", "composition", "relational"), (3, 5, 4, 5, 3)),
    hypothesis("C11", "Authenticated Rate-Distortion Ruler Law", "The physically available metric between states or regions is the minimum authenticated communication cost required to preserve every admitted action outcome within a fixed distortion tolerance.", "Derive a target-independent distortion measure and compare it with an independently calibrated physical metric; task-fitted distortion kills it.", "rate-distortion geometry and information geometry", ("capacity", "ruler", "sufficiency", "certificate"), (3, 5, 5, 5, 3)),
    hypothesis("C12", "Minimal Stable Sufficient Representation Law", "Fundamental dynamics selects the coarsest dynamically invariant state quotient sufficient for every physically realizable continuation, and the matched views are its canonical projections and consumers.", "Prove uniqueness up to physical gauge for a source-pinned process; two incomparable sufficient stable quotients kill the law.", "minimal realization, causal states, Petz sufficiency, and predictive state representations", ("sufficiency", "minimality", "record", "stability", "selection"), (5, 5, 5, 3, 5)),
    hypothesis("C13", "Joint-Observability Closure Law", "The physically selected view family is the minimal intervention-and-readout family whose joint observability operator has full rank on lawful states modulo physical gauge, while ruler responses are its calibrated active probes.", "Compute the minimal family before the held-out target; multiple non-equivalent minimal realizations or unphysical controls kill uniqueness.", "system identification and observability theory", ("action", "sufficiency", "ruler", "gauge"), (4, 5, 5, 3, 5)),
    hypothesis("C14", "Parametric View-Coherence Law", "A physical common-view family is the unique gauge-natural refinement system whose maps commute with every lawful process morphism and cannot inspect the target representation.", "Prove a naturality/parametricity theorem or return a no-section counterexample under the full automorphism group.", "parametricity, descent, and natural-transformation no-go theorems", ("naturality", "composition", "gauge", "selection"), (4, 5, 5, 4, 4)),
    hypothesis("C15", "Regional Predict-Reconcile Law", "Local observer realities are authoritative only within finite causal-interest regions, while cross-region interactions select shared facts by deterministic reconciliation of provenance-bearing state deltas rather than by one global view.", "Construct a relativistically admissible regional protocol with no hidden global authority and derive a novel invariant or exact obstruction.", "distributed simulation, relational QM, and causal networks", ("regional", "finality", "access", "provenance"), (3, 5, 4, 5, 3)),
    hypothesis("C16", "Cross-Shard Physical Gluing Law", "Nature selects local record-and-capability quotients per causally bounded shard, and global geometry is the obstruction-sensitive result of atomic gluing across their overlap interfaces.", "Show local selector uniqueness plus path-independent gluing, or measure the holonomy/obstruction left by merger order.", "sheaf descent, lattice gauge theory, and atomic commit", ("regional", "gluing", "finality", "ruler"), (4, 5, 5, 5, 3)),
    hypothesis("C17", "Predictive-Bottleneck Formation Law", "Stable physical records are dynamically selected bottlenecks that minimize retained state subject to preserving the distribution of every attainable future interaction.", "Derive the bottleneck objective from physics rather than training choice and distinguish its selected representation from alternate equally predictive encodings.", "information bottleneck, predictive coding, and causal states", ("prediction", "minimality", "stability", "record"), (3, 4, 4, 3, 5)),
    hypothesis("C18", "Physical Causal-State Law", "Histories belong to one physical state exactly when they induce the same conditional distribution over every admissible future intervention, and dynamics selects the resulting epsilon-machine as the observer-relative ontology.", "Freeze all interventions and prove closure/uniqueness; an inaccessible intervention that splits one causal state reveals the supplied action boundary.", "computational mechanics and predictive-state representations", ("prediction", "sufficiency", "history", "action"), (4, 5, 5, 3, 5)),
    hypothesis("C19", "Logical-Code Shared-Reality Law", "Public records are the logical observables of the dynamically selected maximal correctable algebra, regional access is decoder-relative, and ruler responses are syndrome-sensitive logical probes.", "Derive the code and decoder-access class from one source dynamics; multiple maximal correctable algebras or supplied decoders kill selection.", "operator quantum error correction and holographic codes", ("logical", "stability", "access", "ruler"), (4, 5, 5, 4, 4)),
    hypothesis("C20", "Irreducible Closure Boundary Law", "The physically meaningful views are exactly the invariants computable within a region's resource horizon without replaying the complete irreducible transition history, and finality marks the boundary where recomputation is no longer operationally available.", "Define the resource class covariantly and exhibit a scaling separation; model-dependent complexity assumptions or mere practical hardness kill it.", "logical depth, complexity theory, and thermodynamic resource theories", ("complexity", "minimality", "composition", "finality"), (2, 4, 4, 5, 2)),
    hypothesis("P21", "Action-Selected Pointer-Algebra Law", "For a complete system-apparatus-environment action, the stable pointer algebra is the unique maximal subalgebra invariant under the reduced dynamics and physically readable by the same interaction that writes it.", "Derive writer, stable algebra, and reader jointly; degeneracy under equally physical apparatus splittings kills uniqueness.", "decoherence, instrument theory, and open-system fixed algebras", ("instrument", "record", "stability", "action"), (4, 5, 5, 3, 4)),
    hypothesis("P22", "Redundant-Accessibility Phase Law", "A record becomes regionally public at a universal transition in independently accessible redundant environmental support, and that transition simultaneously changes the safe action algebra.", "Freeze fragment accessibility and test finite-size scaling plus action change; ordinary SBS without a sharp transition absorbs it.", "Quantum Darwinism, spectrum broadcast structure, and percolation", ("redundancy", "record", "stability", "threshold"), (3, 4, 5, 3, 4)),
    hypothesis("P23", "Modular Response-Closure Law", "A state, local algebra net, and dynamics select the observer-relative record, access, and ruler structures as the smallest modularly invariant response subnetwork on which relative entropy and causal propagation close.", "Specify the inclusion and prove canonical closure under all physical automorphisms; multiple modularly natural subnetworks or missing apparatus semantics kill it.", "modular theory, sufficiency, and AQFT inclusions", ("algebra", "naturality", "response", "sufficiency"), (5, 5, 5, 5, 3)),
    hypothesis("P24", "Recoverable-Algebra Sufficiency Law", "The common-view family is the unique maximal algebra exactly recoverable from every admitted observer channel while retaining all held-out intervention statistics.", "Use Petz/correctable-algebra criteria on one physical channel family; nonunique maximal algebras or channel refit kills the claim.", "Petz recovery and operator quantum error correction", ("sufficiency", "logical", "instrument", "selection"), (4, 5, 5, 3, 5)),
    hypothesis("P25", "Relational Descent Law", "Physical views are local gauge-fixed sections of one relational response object, and admissible perspective changes uniquely select their matched descent data while leaving only gauge-invariant holonomy as global remainder.", "Construct the perspective groupoid and test descent; unmatched sections or physically measurable gauge-choice dependence kill it.", "quantum reference frames, gauge theory, and sheaf descent", ("relational", "gauge", "naturality", "gluing"), (4, 5, 5, 5, 3)),
    hypothesis("P26", "Instrument Fixed-Point Selection Law", "Repeated lawful system-apparatus interaction selects the unique extremal instrument fixed point whose classical output algebra is stable under composition and whose dilation supplies its material consumer.", "Solve the instrument fixed points and retain all dilation freedoms; nonunique extremal fixed points or consumer dependence kills selection.", "quantum instruments, dilation theory, and quantum Markov chains", ("instrument", "fixed_point", "access", "composition"), (4, 5, 5, 4, 4)),
    hypothesis("P27", "Metastable Lindbladian Record Law", "A complete local Lindbladian selects long-lived record sectors, admissible transitions, and regional finality through an isolated slow spectral subspace, with the same spectrum fixing retention and readout timescales.", "Derive the spectral sector and test robustness under allowed perturbations; arbitrary coarse graining or multiple inequivalent slow algebras kills it.", "metastability, noiseless subsystems, and open-system spectral theory", ("stability", "algebra", "threshold", "record"), (4, 5, 5, 3, 5)),
    hypothesis("P28", "Dissipative Stability Selection Law", "Among compatible view families, physical dynamics selects those minimizing excess entropy production while remaining stable and compositionally sufficient under the admitted driving protocol.", "Derive the variational principle and protocol-independent minimizer; externally chosen coarse graining or near-equilibrium absorption kills it.", "minimum entropy production and stochastic thermodynamics", ("stability", "threshold", "response", "selection"), (3, 4, 4, 3, 4)),
    hypothesis("P29", "Stopping-Time Finality Law", "A record becomes final for an observer when its likelihood-ratio process reaches a physically selected absorbing stopping boundary after which every admissible continuation preserves the action decision within the declared error.", "Derive the boundary from dynamics and resources; an analyst-selected confidence threshold or reopening continuation kills it.", "sequential analysis, martingales, and quantum trajectories", ("history", "finality", "threshold", "action"), (3, 4, 5, 3, 5)),
    hypothesis("P30", "Interventional Causal-State Selector", "One physical action family selects the coarsest history quotient invariant under all interventions, and records, capabilities, provenance, and geometry are matched statistics of that causal quotient.", "Freeze a realizable intervention family and prove quotient sufficiency plus no-refit transfer; changing the action menu changes the answer and exposes the supplied observer boundary.", "causal inference, process tensors, and sufficient statistics", ("action", "sufficiency", "provenance", "record"), (5, 5, 5, 4, 5)),
    hypothesis("P31", "Regional Common-View Sheaf Law", "No unique global view family is selected; dynamics selects compatible local response closures whose gluing class determines public facts and whose nontrivial holonomy is the finite physical remainder.", "Build the typed sheaf from one physical process and predict an order/topology-dependent invariant; arbitrary cover choice or vanishing after standard gauge reduction kills it.", "sheaf contextuality, gauge holonomy, and descent theory", ("gluing", "regional", "naturality", "response"), (4, 5, 5, 5, 3)),
    hypothesis("P32", "Universal Natural-Closure Law", "The selected matched view family is the universal fixed object of a physically defined closure functor from processes to record-action-ruler diagrams, unique up to natural isomorphism.", "Define the functor without inserting the desired views and prove universality; two nonisomorphic universal candidates or no physical functor kills it.", "category theory, adjunctions, and coalgebraic semantics", ("naturality", "fixed_point", "gluing", "selection"), (4, 5, 5, 5, 2)),
    hypothesis("P33", "Principal-Symbol Ruler-Closure Law", "For a well-posed local field theory, the principal symbol selects causal propagation and conformal geometry, while a dynamically selected calibrated response functional supplies the remaining scale and completes the ruler family.", "Derive both symbol and scale response from one action; scale refit or multiple admissible calibrators kills metric selection.", "hyperbolic inverse problems and causal/metric reconstruction", ("ruler", "gauge", "response", "selection"), (5, 5, 5, 4, 4)),
    hypothesis("P34", "Hyperbolic Symmetrizer Selection Law", "The physically realized common views are the unique positive-energy variables selected by a covariant symmetrizer that makes the response equations hyperbolic, stable, and compositionally transmissible.", "Prove symmetrizer uniqueness and show its variables coincide with formed/read records; nonunique symmetrizers or no record semantics kills it.", "symmetric-hyperbolic PDE theory and energy estimates", ("ruler", "response", "stability", "selection"), (3, 4, 5, 4, 4)),
    hypothesis("P35", "Covariant Action-Response Closure Law", "A complete covariant action selects, through its stationary solution, Hessian, constraints, and response spectrum, one gauge orbit of matched records, admissible actions, composition rules, regional finality, and calibrated ruler responses.", "Hold the action and boundary data fixed and compute every residual automorphism; any two inequivalent matched view/ruler families kill uniqueness.", "variational physics, spectral geometry, decoherence, and inverse problems", ("action", "response", "selection", "ruler", "gauge"), (5, 5, 5, 5, 4)),
    hypothesis("P36", "Pairwise Response-Kernel Law", "The fundamental selector is not a field state but the covariant pairwise source-response kernel; records, capabilities, and rulers are the minimal invariant factorizations through which all physically realizable pair interactions compose.", "Formulate the kernel without a field mediator and test whether its invariant factorization uniquely reconstructs the observed local field description.", "direct-action electrodynamics, S-matrix reconstruction, and mediator elimination", ("relational", "response", "provenance", "composition"), (4, 5, 4, 5, 3)),
    hypothesis("P37", "RG-Stable Observable-Closure Law", "The physical common-view family is the maximal observable-and-response subalgebra stable under renormalization across the admitted scale interval, with classical records and rulers as robust infrared coordinates.", "Run the exact coarse-graining map and test uniqueness/no-refit transfer; scheme dependence or several inequivalent stable algebras kills selection.", "effective field theory and renormalization", ("stability", "coarse_grain", "algebra", "record"), (3, 5, 4, 3, 4)),
    hypothesis("P38", "Order-Volume-Ruler Reconstruction Law", "A physically selected causal order, event-volume measure, and finite calibration mark jointly determine the regional geometry, while record and capability views are the observer-accessible restrictions of that ordered measure space.", "Prove reconstruction in a finite causal arena and test scale transfer; a supplied sprinkling density or calibration mark leaves the key selector open.", "causal-set reconstruction and Lorentzian geometry", ("ruler", "causal", "regional", "record"), (3, 5, 5, 4, 3)),
    hypothesis("P39", "Generalized-Symmetry Record-Net Law", "A complete gauge action selects a net of defect and Wilson observables whose superselection, fusion, and screening structure jointly fixes composable records, allowed capabilities, regional gluing, and ruler response.", "Derive the net and its physical reader from one action; matter-dependent screening or multiple probe choices that alter the net kill uniqueness.", "generalized symmetries, algebraic QFT, and lattice gauge theory", ("gauge", "algebra", "gluing", "record"), (4, 5, 5, 5, 3)),
    hypothesis("P40", "Regional Plurality Obstruction", "No target-blind law can select one globally privileged common-view family; the strongest lawful result is a regional equivalence class indexed by physical action boundaries, with exact translation maps and a measurable first gluing failure.", "Prove a no-section theorem for global selection while constructing regional translations; one canonical global selector refutes it.", "contextuality, model theory, and observer-relative operational equivalence", ("regional", "relational", "minimality", "gluing"), (4, 5, 5, 5, 4)),
]


COMMUNITY_EDGES = {
    "consensus_networks": {"data_composition", "security_provenance", "information_control"},
    "data_composition": {"consensus_networks", "security_provenance", "computation_learning", "information_control"},
    "security_provenance": {"consensus_networks", "data_composition", "formal_math"},
    "computation_learning": {"data_composition", "information_control", "formal_math"},
    "information_control": {"consensus_networks", "data_composition", "computation_learning", "quantum_measurement", "formal_math"},
    "quantum_measurement": {"information_control", "field_spacetime", "formal_math", "foundations_causal"},
    "field_spacetime": {"quantum_measurement", "formal_math", "foundations_causal"},
    "formal_math": {"security_provenance", "computation_learning", "information_control", "quantum_measurement", "field_spacetime", "foundations_causal"},
    "foundations_causal": {"quantum_measurement", "field_spacetime", "formal_math"},
}


QUALITY_WEIGHTS = {
    "selection": 5,
    "integration": 4,
    "falsifiability": 4,
    "novelty": 3,
    "tractability": 3,
}


def shortest_community_distance(source: str, target: str) -> int:
    if source == target:
        return 0
    queue: deque[tuple[str, int]] = deque([(source, 0)])
    visited = {source}
    while queue:
        node, distance = queue.popleft()
        for neighbor in COMMUNITY_EDGES[node]:
            if neighbor == target:
                return distance + 1
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))
    raise AssertionError(f"disconnected community graph: {source}, {target}")


def utility(voter: dict[str, Any], candidate: dict[str, Any]) -> int:
    score = sum(
        QUALITY_WEIGHTS[key] * candidate["qualities"][key]
        for key in QUALITY_WEIGHTS
    )
    score += sum(3 * candidate["qualities"][key] for key in voter["priorities"])
    score += 4 * len(set(voter["tags"]) & set(candidate["tags"]))
    distance = shortest_community_distance(
        voter["community"],
        next(item["community"] for item in LENSES if item["id"] == candidate["owner"]),
    )
    score += {0: 6, 1: 3}.get(distance, 0)
    if voter["family"] != next(item["family"] for item in LENSES if item["id"] == candidate["owner"]):
        score += 2
    return score


def hamilton_linear_allocation(scored: list[tuple[str, int]], budget: int = 100) -> dict[str, int]:
    selected = scored[:12]
    total = sum(score for _, score in selected)
    floors = {candidate_id: budget * score // total for candidate_id, score in selected}
    remainder = budget - sum(floors.values())
    order = sorted(
        selected,
        key=lambda pair: (
            -((budget * pair[1]) % total),
            -pair[1],
            pair[0],
        ),
    )
    for candidate_id, _ in order[:remainder]:
        floors[candidate_id] += 1
    return floors


def exact_quadratic_allocation(scored: list[tuple[str, int]], budget: int = 100) -> dict[str, int]:
    """Maximize declared utility under exact quadratic cost on the top 16."""
    selected = scored[:16]
    # cost -> (value, vote-vector); lexicographically larger earlier votes is
    # the deterministic tie-break because selected is utility ordered.
    states: dict[int, tuple[int, tuple[int, ...]]] = {0: (0, ())}
    for _, score in selected:
        next_states: dict[int, tuple[int, tuple[int, ...]]] = {}
        for prior_cost, (prior_value, prior_vector) in states.items():
            for votes in range(0, int(math.isqrt(budget - prior_cost)) + 1):
                cost = prior_cost + votes * votes
                value = prior_value + score * votes
                vector = prior_vector + (votes,)
                current = next_states.get(cost)
                if current is None or value > current[0] or (
                    value == current[0] and vector > current[1]
                ):
                    next_states[cost] = (value, vector)
        states = next_states
    if budget not in states:
        raise AssertionError("quadratic ballot cannot spend the exact budget")
    vector = states[budget][1]
    return {
        candidate_id: votes
        for (candidate_id, _), votes in zip(selected, vector, strict=True)
        if votes > 0
    }


def ordinal_ranks(totals: dict[str, int]) -> dict[str, int]:
    ordered = sorted(totals, key=lambda item: (-totals[item], item))
    return {candidate_id: index + 1 for index, candidate_id in enumerate(ordered)}


def rank_correlation(rank_a: dict[str, int], rank_b: dict[str, int]) -> float:
    n = len(rank_a)
    squared = sum((rank_a[key] - rank_b[key]) ** 2 for key in rank_a)
    return 1.0 - 6.0 * squared / (n * (n * n - 1))


def run() -> dict[str, Any]:
    checks: list[dict[str, Any]] = []
    lens_by_id = {item["id"]: item for item in LENSES}
    hypothesis_by_id = {item["id"]: item for item in HYPOTHESES}
    ids = [item["id"] for item in HYPOTHESES]

    checks.append({
        "name": "twenty computational and twenty math-physics lenses own one hypothesis each",
        "passed": (
            len(LENSES) == len(HYPOTHESES) == 40
            and len(lens_by_id) == len(hypothesis_by_id) == 40
            and Counter(item["family"] for item in LENSES)
            == {"computational": 20, "math_physics": 20}
            and set(lens_by_id) == set(hypothesis_by_id)
            and all(item["owner"] == item["id"] for item in HYPOTHESES)
        ),
        "detail": dict(Counter(item["family"] for item in LENSES)),
    })

    required = ("title", "statement", "decisive_test", "strongest_absorber", "grade")
    checks.append({
        "name": "every hypothesis is explicit, testable, absorber-aware, and grade zero",
        "passed": all(
            all(str(item[field]).strip() for field in required)
            and item["grade"] == "GRADE_0_HYPOTHESIS"
            and all(1 <= value <= 5 for value in item["qualities"].values())
            for item in HYPOTHESES
        ),
        "detail": {"required_fields": list(required)},
    })

    linear_totals = {candidate_id: 0 for candidate_id in ids}
    quadratic_vote_totals = {candidate_id: 0 for candidate_id in ids}
    quadratic_cost_totals = {candidate_id: 0 for candidate_id in ids}
    linear_supporters: defaultdict[str, set[str]] = defaultdict(set)
    quadratic_supporters: defaultdict[str, set[str]] = defaultdict(set)
    ballots: list[dict[str, Any]] = []

    for voter in LENSES:
        scored = sorted(
            (
                (candidate["id"], utility(voter, candidate))
                for candidate in HYPOTHESES
                if candidate["owner"] != voter["id"]
            ),
            key=lambda pair: (-pair[1], pair[0]),
        )
        linear = hamilton_linear_allocation(scored)
        quadratic = exact_quadratic_allocation(scored)
        linear_surface = {
            candidate_id: None if candidate_id == voter["id"] else linear.get(candidate_id, 0)
            for candidate_id in ids
        }
        quadratic_surface = {
            candidate_id: None if candidate_id == voter["id"] else quadratic.get(candidate_id, 0)
            for candidate_id in ids
        }
        for candidate_id, credits in linear.items():
            linear_totals[candidate_id] += credits
            if credits > 0:
                linear_supporters[candidate_id].add(voter["id"])
        for candidate_id, votes in quadratic.items():
            quadratic_vote_totals[candidate_id] += votes
            quadratic_cost_totals[candidate_id] += votes * votes
            if votes > 0:
                quadratic_supporters[candidate_id].add(voter["id"])
        ballots.append({
            "voter": voter["id"],
            "linear_weights": linear_surface,
            "linear_credits_spent": sum(linear.values()),
            "quadratic_weights": quadratic_surface,
            "quadratic_credits_spent": sum(votes * votes for votes in quadratic.values()),
            "quadratic_vote_units": sum(quadratic.values()),
            "utility_order": [candidate_id for candidate_id, _ in scored],
            "utility_scores": {candidate_id: score for candidate_id, score in scored},
        })

    checks.append({
        "name": "all ballots cover every non-owned hypothesis and forbid self-votes",
        "passed": all(
            len(ballot["linear_weights"]) == len(ballot["quadratic_weights"]) == 40
            and ballot["linear_weights"][ballot["voter"]] is None
            and ballot["quadratic_weights"][ballot["voter"]] is None
            and sum(value is None for value in ballot["linear_weights"].values()) == 1
            and sum(value is None for value in ballot["quadratic_weights"].values()) == 1
            for ballot in ballots
        ),
        "detail": {"ballots": len(ballots), "weights_per_ballot": 40},
    })
    checks.append({
        "name": "every lens spends exactly one hundred credits in each A-B arm",
        "passed": all(
            ballot["linear_credits_spent"] == 100
            and ballot["quadratic_credits_spent"] == 100
            for ballot in ballots
        ),
        "detail": {"linear_total": sum(linear_totals.values()), "quadratic_cost_total": sum(quadratic_cost_totals.values())},
    })
    checks.append({
        "name": "aggregate A-B budgets reconcile to four thousand credits each",
        "passed": sum(linear_totals.values()) == sum(quadratic_cost_totals.values()) == 4000,
        "detail": {"linear": sum(linear_totals.values()), "quadratic": sum(quadratic_cost_totals.values())},
    })

    linear_rank = ordinal_ranks(linear_totals)
    quadratic_rank = ordinal_ranks(quadratic_vote_totals)
    max_distance = max(
        shortest_community_distance(a, b)
        for a in COMMUNITY_EDGES
        for b in COMMUNITY_EDGES
    )

    rankings: list[dict[str, Any]] = []
    for candidate_id in ids:
        owner = lens_by_id[candidate_id]
        supporters = sorted(quadratic_supporters[candidate_id])
        distances = [
            shortest_community_distance(owner["community"], lens_by_id[voter]["community"])
            for voter in supporters
        ]
        weighted_distances = [
            (
                shortest_community_distance(owner["community"], lens_by_id[voter]["community"]),
                next(ballot for ballot in ballots if ballot["voter"] == voter)["quadratic_weights"][candidate_id],
            )
            for voter in supporters
        ]
        weighted_mean = (
            sum(distance * votes for distance, votes in weighted_distances)
            / sum(votes for _, votes in weighted_distances)
            if weighted_distances else 0.0
        )
        communities = {lens_by_id[voter]["community"] for voter in supporters}
        families = {lens_by_id[voter]["family"] for voter in supporters}
        units_by_family: defaultdict[str, int] = defaultdict(int)
        units_by_community: defaultdict[str, int] = defaultdict(int)
        for voter in supporters:
            votes = next(ballot for ballot in ballots if ballot["voter"] == voter)["quadratic_weights"][candidate_id]
            units_by_family[lens_by_id[voter]["family"]] += votes
            units_by_community[lens_by_id[voter]["community"]] += votes
        remote_units = sum(
            votes for distance, votes in weighted_distances if distance >= 2
        )
        total_units = quadratic_vote_totals[candidate_id]
        bridge_score = (
            total_units
            * (weighted_mean / max_distance)
            * (len(communities) / len(COMMUNITY_EDGES))
            if total_units else 0.0
        )
        rankings.append({
            "hypothesis_id": candidate_id,
            "title": hypothesis_by_id[candidate_id]["title"],
            "owner_lens": owner["name"],
            "owner_family": owner["family"],
            "owner_community": owner["community"],
            "linear_credits": linear_totals[candidate_id],
            "linear_rank": linear_rank[candidate_id],
            "quadratic_vote_units": total_units,
            "quadratic_cost_received": quadratic_cost_totals[candidate_id],
            "quadratic_rank": quadratic_rank[candidate_id],
            "rank_delta_quadratic_minus_linear": linear_rank[candidate_id] - quadratic_rank[candidate_id],
            "linear_supporter_count": len(linear_supporters[candidate_id]),
            "quadratic_supporter_count": len(supporters),
            "quadratic_supporting_communities": len(communities),
            "quadratic_supporting_families": sorted(families),
            "quadratic_vote_units_by_family": dict(sorted(units_by_family.items())),
            "quadratic_vote_units_by_community": dict(sorted(units_by_community.items())),
            "cross_family_balance": round(
                min(units_by_family.values()) / max(units_by_family.values()), 4
            ) if len(units_by_family) == 2 else 0.0,
            "mean_owner_supporter_distance": round(weighted_mean, 4),
            "median_owner_supporter_distance": median(distances) if distances else 0,
            "remote_quadratic_vote_share": round(remote_units / total_units, 4) if total_units else 0.0,
            "bridge_score": round(bridge_score, 4),
            "quadratic_supporters": supporters,
        })

    linear_order = sorted(rankings, key=lambda row: (row["linear_rank"], row["hypothesis_id"]))
    quadratic_order = sorted(rankings, key=lambda row: (row["quadratic_rank"], row["hypothesis_id"]))
    bridge_order = sorted(
        rankings,
        key=lambda row: (-row["bridge_score"], -row["quadratic_vote_units"], row["hypothesis_id"]),
    )
    top_ten_overlap = len(
        {row["hypothesis_id"] for row in linear_order[:10]}
        & {row["hypothesis_id"] for row in quadratic_order[:10]}
    )
    comparison = {
        "spearman_rank_correlation": round(rank_correlation(linear_rank, quadratic_rank), 4),
        "top_ten_overlap": top_ten_overlap,
        "linear_winner": linear_order[0]["hypothesis_id"],
        "quadratic_winner": quadratic_order[0]["hypothesis_id"],
        "bridge_winner": bridge_order[0]["hypothesis_id"],
        "largest_quadratic_rises": sorted(
            rankings,
            key=lambda row: (-row["rank_delta_quadratic_minus_linear"], row["hypothesis_id"]),
        )[:5],
        "largest_quadratic_falls": sorted(
            rankings,
            key=lambda row: (row["rank_delta_quadratic_minus_linear"], row["hypothesis_id"]),
        )[:5],
    }
    checks.append({
        "name": "linear, quadratic, and social-distance rankings are complete and deterministic",
        "passed": (
            len(linear_order) == len(quadratic_order) == len(bridge_order) == 40
            and sorted(row["linear_rank"] for row in rankings) == list(range(1, 41))
            and sorted(row["quadratic_rank"] for row in rankings) == list(range(1, 41))
            and 0 <= top_ten_overlap <= 10
        ),
        "detail": comparison,
    })
    checks.append({
        "name": "social distance is descriptive prioritization metadata only",
        "passed": max_distance >= 2 and all(
            0 <= row["remote_quadratic_vote_share"] <= 1
            and 0 <= row["quadratic_supporting_communities"] <= len(COMMUNITY_EDGES)
            for row in rankings
        ),
        "detail": {"community_count": len(COMMUNITY_EDGES), "maximum_graph_distance": max_distance},
    })

    result = {
        "run_id": RUN_ID,
        "status": "PASS" if all(item["passed"] for item in checks) else "FAIL",
        "epistemic_status": "EXPLORATORY_PRIORITY_SIGNAL_NOT_SCIENTIFIC_EVIDENCE",
        "vote_contract": {
            "linear_arm": "Each lens allocates 100 ordinary credits over its twelve highest-utility non-owned hypotheses by Hamilton apportionment.",
            "quadratic_arm": "Each lens allocates exactly 100 credits over non-owned hypotheses; v vote units cost v^2; an exact dynamic program maximizes the same declared utility surface.",
            "self_vote_rule": "forbidden in both arms",
            "utility_surface": "Declared candidate qualities, each lens's two criterion priorities, bounded tag affinity, bounded community proximity, and a small cross-family bonus.",
            "social_distance": "Shortest-path distance between nine declared disciplinary communities. Bridge score combines quadratic support, owner-supporter distance, and community breadth; it is not evidence or an automatic winner rule.",
        },
        "lenses": LENSES,
        "hypotheses": HYPOTHESES,
        "community_graph": {key: sorted(value) for key, value in COMMUNITY_EDGES.items()},
        "checks": checks,
        "ballots": ballots,
        "rankings": {
            "linear": linear_order,
            "quadratic": quadratic_order,
            "social_bridge": bridge_order,
        },
        "ab_comparison": comparison,
        "scientific_boundary": "The hypotheses remain Grade 0. Persona agreement, vote concentration, and disciplinary distance select what to examine; they do not establish truth, novelty, physical selection, or excess empirical content.",
    }
    ARTIFACT_PATH.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT_PATH.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    return result


if __name__ == "__main__":
    output = run()
    print(json.dumps({
        "run_id": output["run_id"],
        "status": output["status"],
        "checks": f"{sum(item['passed'] for item in output['checks'])}/{len(output['checks'])}",
        "linear_winner": output["ab_comparison"]["linear_winner"],
        "quadratic_winner": output["ab_comparison"]["quadratic_winner"],
        "bridge_winner": output["ab_comparison"]["bridge_winner"],
        "spearman": output["ab_comparison"]["spearman_rank_correlation"],
        "top_ten_overlap": output["ab_comparison"]["top_ten_overlap"],
    }, indent=2))
