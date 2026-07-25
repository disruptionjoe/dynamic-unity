#!/usr/bin/env python3
"""Audit the ten-lens efficient-approach attachment for all 36 hypotheses.

Passing means the method registry is complete, referentially valid, and
deterministic. It does not validate any hypothesis or make a priority decision.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SOURCE_PATH = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_technical_lens_hypothesis_quadratic_vote_result.json"
)
OUTPUT_PATH = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_hypothesis_efficient_approach_registry_result.json"
)


LENSES = [
    {
        "id": "CAT",
        "name": "Category theorist",
        "instruction": "Find the typed object, universal property, invariant, composition law, and naturality obligation.",
    },
    {
        "id": "CFS",
        "name": "Counterfactual statistician",
        "instruction": "Freeze the estimand and rivals, then choose matched interventions by expected discrimination when defined.",
    },
    {
        "id": "FCE",
        "name": "Formal counterexample engineer",
        "instruction": "Quotient symmetries and synthesize the smallest witness with an independently checkable certificate.",
    },
    {
        "id": "EMA",
        "name": "Experimental metrology architect",
        "instruction": "Calculate identifiability and the effect-to-error margin before spending apparatus time.",
    },
    {
        "id": "RPO",
        "name": "Research-portfolio and operations scientist",
        "instruction": "Reuse fixtures, cache intermediate objects, and require a transferable artifact from every run.",
    },
    {
        "id": "ORT",
        "name": "Orthodox professor",
        "instruction": "Executable prior art and the strongest standard absorber precede novelty claims.",
    },
    {
        "id": "HET",
        "name": "Heterodox professor",
        "instruction": "Vary hidden assumptions one at a time and preserve counterfamilies and dual formulations.",
    },
    {
        "id": "COM",
        "name": "Commercial scientist",
        "instruction": "Build the thinnest complete vertical slice that produces a decision-enabling reusable output.",
    },
    {
        "id": "WILD",
        "name": "Wild-frontier scientist",
        "instruction": "Preserve the profound conjunction in a tiny falsifiable model with an invariance audit.",
    },
    {
        "id": "PHIL",
        "name": "Philosopher of science",
        "instruction": "Separate operational, mathematical, physical, and ontological conclusions and forbid semantic refit.",
    },
]


METHOD_KITS = {
    "K0": {
        "name": "Semantic and estimand lock",
        "output": "contract digest and claim-to-observable map",
    },
    "K1": {
        "name": "Symmetry-reduced finite search",
        "output": "smallest countermodel or finite exhaustive certificate",
    },
    "K2": {
        "name": "Proof-carrying algebra/compiler",
        "output": "algorithm, exact conditions, proof object, and tight example",
    },
    "K3": {
        "name": "Counterfactual sequential design",
        "output": "matched contrast, uncertainty update, and next-intervention rule",
    },
    "K4": {
        "name": "Authenticated distributed twin",
        "output": "replayable protocol trace, attack witness, and capability delta",
    },
    "K5": {
        "name": "Routed quantum twin",
        "output": "complete process reconstruction, null residual, and action algebra",
    },
    "K6": {
        "name": "Metrology preflight and sequential assay",
        "output": "assay passport, error budget, and calibrated outcome record",
    },
    "K7": {
        "name": "Scaling and universality toolkit",
        "output": "phase/scaling discriminator and finite-size controls",
    },
    "K8": {
        "name": "Resource and provenance accounting",
        "output": "complete ledger, bound, and resource-achieving specimen",
    },
    "K9": {
        "name": "Reconstruction and uniqueness ladder",
        "output": "assumption-minimal reconstruction or explicit remainder",
    },
}


def attachment(
    hypothesis_id: str,
    kits: str,
    lenses: str,
    smallest_object: str,
    recommended_attack: str,
    first_decisive_contrast: str,
    reusable_output: str,
    scale_up_when: str,
    avoid: str,
) -> dict[str, Any]:
    return {
        "hypothesis_id": hypothesis_id,
        "method_kits": kits.split(),
        "lead_lenses": lenses.split(),
        "smallest_informative_object": smallest_object,
        "recommended_attack": recommended_attack,
        "first_decisive_contrast": first_decisive_contrast,
        "reusable_output": reusable_output,
        "scale_up_when": scale_up_when,
        "avoid": avoid,
    }


ATTACHMENTS = [
    attachment(
        "MC-A",
        "K0 K3 K4 K7 K8",
        "CFS EMA RPO HET",
        "The smallest validator system with two correlated provenance sectors and one incompatible safe action.",
        "Derive a finite Markov or quasi-potential model, then run matched upward and downward sweeps with marginal accuracy and common-shock strength fixed.",
        "Equal marginal evidence with different independent-provenance rank.",
        "Analytic approximation, saved protocol trace, and hysteresis/scaling surface.",
        "The frozen small model identifies the signature and its target operating region.",
        "Undirected parameter grids or equating confidence with irreversible action.",
    ),
    attachment(
        "MC-B",
        "K0 K1 K2 K4 K8",
        "FCE ORT HET COM",
        "One latent common shock, repeated subsampling, and one authenticated independent evidence source.",
        "Solve the protocol as an indistinguishability game using exact enumeration, coupling, or linear programming and pair the bound with an achiever.",
        "More rounds without new provenance versus one genuinely independent provenance input.",
        "Scoped risk lower bound, assumptions, matching protocol, and minimal defeating counterexample.",
        "The bound is tight on the declared finite class and its assumptions are machine-checkable.",
        "Assuming sample independence or counting replicas as independent evidence.",
    ),
    attachment(
        "HG-A",
        "K0 K1 K2",
        "CAT FCE WILD PHIL",
        "A genuine three-party typed process with one ternary intervention.",
        "Canonically enumerate orbit representatives and synthesize two processes identical on every pairwise record and intervention but separated by one hyperedge action.",
        "Pairwise equivalence versus one frozen ternary intervention.",
        "Minimal process pair, pairwise-equivalence certificate, and separating intervention.",
        "Exhaustion confirms that no smaller typed process supports the distinction.",
        "Leaking the distinction through hyperedge labels or brute-forcing labeled graphs.",
    ),
    attachment(
        "HG-B",
        "K0 K1 K2",
        "CAT FCE COM WILD",
        "One unresolved reconciliation loop and one candidate 2-cell relation.",
        "Present a finite path category or 2-complex, compute loop generators and the normal closure induced by the higher certificate, and derive the invariant algebra.",
        "An additional evidence edge versus a relation that actually fills the loop.",
        "Normal-form theorem, executable reducer, proof certificate, and tight counterexample.",
        "The one-loop result is representation-stable and independently verified.",
        "Calling every extra quorum, vote, or message a loop-filling operation.",
    ),
    attachment(
        "CA-A",
        "K0 K1 K2",
        "CAT FCE ORT PHIL",
        "A homogeneous reversible orbit with symmetric candidate record sites.",
        "Prove the equivariance obstruction first and use symmetry-reduced CA or QCA search only to locate the smallest tight specimen.",
        "A symmetry-preserving selector versus one explicitly declared asymmetric resource.",
        "Scoped no-go, exact automorphism assumptions, saturating model, and minimal escape resource.",
        "The symmetry theorem and the smallest construction meet at the same boundary.",
        "Sweeping rule tables before quotienting symmetries or hiding the selector in readout.",
    ),
    attachment(
        "CA-B",
        "K0 K1 K2",
        "CAT FCE COM ORT",
        "The smallest local CA or QCA depth at which one admitted intervention separates two histories.",
        "Propagate the behavioral partition symbolically through causal cones using local rule composition, transfer matrices, or tensor-network light cones.",
        "Identical radius-r cones with adversarially varied exterior states.",
        "Local witness radius, complexity bound, and tight example.",
        "The local bound is verified against exhaustive global behavior on small systems.",
        "Enumerating the global state space when locality already bounds the witness.",
    ),
    attachment(
        "DC-A",
        "K0 K1 K2 K4",
        "CAT FCE COM PHIL",
        "The smallest split-view loop supporting one pair of incompatible safe actions.",
        "Define actions before certificates, compute the lower-layer loop syndrome, and compare an evidence-only layer with one imposing the exact missing relation.",
        "Equal raw evidence and provenance with versus without loop resolution.",
        "Necessary/sufficient conditions, paired protocol traces, and a model-checking certificate.",
        "The result survives a frozen nontrivial adversary and a second representation.",
        "Defining finality as a threshold and thereby making the theorem tautological.",
    ),
    attachment(
        "DC-B",
        "K0 K1 K2 K4",
        "CAT FCE ORT COM",
        "Two noninvertible certified-view maps with a nontrivial common safe subobject.",
        "Compute the equalizer or invariant action algebra directly and model-check whether exactly those facts remain safe across admissible view changes.",
        "Predicted invariant facts versus actually safe actions under every frozen view map.",
        "Equalizer algorithm, proof conditions, and the smallest boundary counterexample.",
        "The correspondence is exact on a declared protocol class and fails legibly outside it.",
        "Assuming reversible views, global state, or common knowledge.",
    ),
    attachment(
        "AD-A",
        "K0 K1 K2 K4 K8",
        "FCE CFS COM ORT",
        "One equivocator and the fewest honest recipients able to acquire incompatible certified views.",
        "Use an indistinguishability or communication-complexity game, synthesize the shortest attack schedule, and minimize authenticated provenance needed to prevent it.",
        "One fewer provenance distinction versus the first sufficient authenticated distinction.",
        "Lower bound, minimal attack trace, and matching protocol when available.",
        "The attack and achiever share the same frozen trust and resource contract.",
        "Counting signature bytes while ignoring key setup, trust roots, and verification work.",
    ),
    attachment(
        "AD-B",
        "K0 K1 K2 K4",
        "FCE CAT HET COM",
        "The smallest finite state space with an adaptive scheduler and one possible refinement.",
        "Encode the problem as a two-player game and compute the symbolic fixpoint with antichains or abstract interpretation.",
        "A sufficient frozen refinement versus the shortest adaptive split-view strategy.",
        "Independently replayable refinement certificate or adversarial trace.",
        "Both return branches are complete on the tiny class and scale compositionally.",
        "Monte Carlo adversary search that can miss the decisive rare schedule.",
    ),
    attachment(
        "ZK-A",
        "K0 K2 K4 K8",
        "ORT COM PHIL RPO",
        "A minimal standard commitment and zero-knowledge relation enabling one certified action.",
        "Instantiate the known construction as an executable positive control and map witness, verification, disclosure, reconstruction, and action to separate fields.",
        "A verified action with versus without disclosure of the witness biography.",
        "Reusable control fixture and exact DU implication crosswalk.",
        "The mapping preserves the cryptographic assumptions and the DU action semantics.",
        "Re-proving zero knowledge or inferring that an undisclosed witness was never instantiated.",
    ),
    attachment(
        "ZK-B",
        "K0 K2 K4 K8",
        "ORT FCE COM PHIL",
        "A matched proof system pair differing in succinctness but not in certified task.",
        "Track proof, reference string, verifier state, trusted parties, assumptions, and provenance through a resource-preserving reduction.",
        "Shrinking proof bytes while holding total certification task and security fixed.",
        "Complete resource ledger and either a residual lower bound or an absorbing construction.",
        "Every moved resource has an operational measure and a matched protocol.",
        "Equating proof size with total certification or provenance cost.",
    ),
    attachment(
        "DB-A",
        "K0 K1 K2 K4",
        "CAT FCE ORT HET",
        "The smallest transaction histories containing one serialization cycle and matched acyclic controls.",
        "Map serialization graphs to the frozen reconciliation category and test each direction of the proposed correspondence separately.",
        "Identical terminal values with acyclic versus cyclic operation provenance.",
        "Two directional theorems, exhaustive tiny-history table, and first failed direction.",
        "The mapping predicts a held-out history without changing transaction semantics.",
        "Stopping at analogy or comparing endpoints without operation order.",
    ),
    attachment(
        "DB-B",
        "K0 K3 K4",
        "CFS EMA RPO HET",
        "One replayable network schedule in which exactly one gossip path can be added.",
        "Run a controlled edge-addition experiment while holding load, routing budget, failures, data semantics, and safe action fixed.",
        "The same saved schedules before and after one added gossip path.",
        "Causal effect estimate, complete logs, and replay bundle.",
        "The effect replicates across new saved schedules and has a mechanism-specific mediator.",
        "Confounding informational topology with ordinary congestion.",
    ),
    attachment(
        "QI-A",
        "K0 K3 K5",
        "EMA ORT CFS PHIL",
        "A routed coherent process with identical reduced endpoints and explicit route-erased and dephased controls.",
        "Reconstruct an implementation-complete process tensor including routes, controls, memories, and readout, then fit the strongest standard-quantum absorber.",
        "The focal routed process versus complete coherent, dephased, and route-erased nulls.",
        "Process reconstruction, uncertainty-aware null residual, and omitted-port audit.",
        "A residual remains after held-out controls under the frozen complete implementation.",
        "Declaring new curvature after omitting an ordinary control port, memory, or phase.",
    ),
    attachment(
        "QI-B",
        "K0 K1 K2 K5",
        "CAT FCE ORT WILD",
        "The smallest noncommuting noisy channel semigroup with a nontrivial invariant action algebra.",
        "Compute the fixed algebra and spectral contraction exactly, then derive perturbation or diamond-norm bounds for approximate convergence.",
        "Exact fixed algebra versus the approximate action algebra at finite noise and time.",
        "Convergence theorem, rate/error bound, and tight channel examples.",
        "The small exact result extends under a stated perturbation class.",
        "Studying state convergence while leaving access and public actions undefined.",
    ),
    attachment(
        "QE-A",
        "K0 K2 K5 K8",
        "CAT ORT COM PHIL",
        "The first stabilizer or subsystem code with a nontrivial correctable logical algebra under varying access.",
        "Use operator-algebra quantum error correction with frozen access, adversary, decoder family, and safe actions.",
        "Crossing one access or erasure threshold while the logical fact and task stay fixed.",
        "Algebraic correspondence, decoder-independent portion, and boundary counterexample.",
        "The same action semantics works in a second code family or the distributed twin.",
        "Equating redundancy, fidelity, or one chosen decoder with public facthood.",
    ),
    attachment(
        "QE-B",
        "K0 K1 K2 K5 K8",
        "CAT FCE HET WILD",
        "A small code with multiple provenance sectors and a nontrivial syndrome space.",
        "Construct the map between provenance sectors and error cosets, then test faithfulness, fullness, and dimension bounds.",
        "Distinct unsafe provenance loops sharing one syndrome or one provenance distinction requiring none.",
        "Explicit map, tight dimension bound, and first obstruction.",
        "The map predicts a new code or network instance without relabeling.",
        "Renaming provenance labels as syndromes and calling that a duality.",
    ),
    attachment(
        "IT-A",
        "K0 K2 K3 K8",
        "CFS CAT ORT COM",
        "The smallest nontrivial action-confusability graph with two tasks on one raw channel.",
        "Seek a graph-entropy, rate-distortion, or zero-error coding theorem with matching achievability and converse.",
        "Equal raw channel statistics but different action-confusability structure.",
        "Operational rate, optimal code, converse certificate, and task-sensitivity analysis.",
        "The exact small solution yields a constructive code for a larger frozen class.",
        "Substituting raw mutual information for action-relative reconciliation.",
    ),
    attachment(
        "IT-B",
        "K0 K1 K2 K3",
        "FCE CFS HET PHIL",
        "The smallest alphabets and intervention sets supporting an ordering reversal.",
        "State axioms for a scalar metric class and synthesize two tasks or channels with equal scalar value but opposite capability order.",
        "One frozen scalar metric class versus an operational ordering reversal.",
        "A minimal counterexample that excludes the whole declared metric class.",
        "The counterexample is invariant to allowed reparameterizations and task labels.",
        "Testing named distance formulas one at a time or refitting the task.",
    ),
    attachment(
        "CT-A",
        "K0 K1 K2 K3",
        "CAT CFS ORT PHIL",
        "A finite system where individual observability fails and joint observability succeeds.",
        "Quotient histories by action response and compare that quotient with observability rank or the Gramian under a frozen control set.",
        "Joint-observability rank versus safe-action equivalence with control and cost explicit.",
        "Each implication, rank test, and counterexamples for missing control assumptions.",
        "The correspondence predicts a held-out control intervention.",
        "Treating observability as capability while ignoring controllability, risk, and cost.",
    ),
    attachment(
        "CT-B",
        "K0 K1 K2",
        "CAT FCE ORT COM",
        "A finite-dimensional tester space with a small process class and an exhaustible intervention set.",
        "Use span, convex separation, and basis extraction to replace universal intervention enumeration with a finite witness basis.",
        "Minimal extracted basis versus exhaustive interventions on the same tiny class.",
        "Compactness theorem, basis algorithm, and counterexample under restricted testers.",
        "The basis generalizes under a stated dimension or convexity bound.",
        "Enumerating all interventions or silently granting unphysical testers.",
    ),
    attachment(
        "SP-A",
        "K0 K3 K4 K7",
        "CFS EMA HET WILD",
        "A reduced stochastic model with separately controlled access, conflict propagation, and safe action.",
        "Analyze fixed points and bifurcations first, then use targeted numerical continuation and matched upward/downward sweeps.",
        "Connectivity and hardening changes with evidence accuracy and load held fixed.",
        "Bifurcation diagram, finite-size behavior, saved trajectories, and rival fit.",
        "The reduced mechanism predicts the operating region for larger systems.",
        "Large parameter grids or mistaking slow relaxation for hysteresis.",
    ),
    attachment(
        "SP-B",
        "K0 K3 K7",
        "CFS EMA ORT HET",
        "The smallest family of system sizes at which smooth, critical, crossover, and first-order rivals diverge.",
        "Preregister rival scaling forms, reserve held-out sizes, and allocate new sizes at maximum predictive disagreement.",
        "Out-of-sample size predictions rather than in-sample visual collapse.",
        "Predictive comparison, collapse uncertainty, and next-size acquisition rule.",
        "A rival is separated on held-out sizes with finite-size corrections explicit.",
        "Exponent fishing, visual collapse alone, or inferring universality from one architecture.",
    ),
    attachment(
        "FM-A",
        "K0 K1 K2",
        "FCE CAT COM RPO",
        "A tiny complete input language with at least one example in every return branch.",
        "Reduce factorization, sufficient refinement, and class-relative remainder to exact equivalence or reachability games and emit a certificate in every branch.",
        "Exhaustive tiny-instance truth versus compiler output and independent certificate verification.",
        "Composable compiler core, canonical cache, three proof-object types, and regression corpus.",
        "The complete vertical slice is correct before language or state-space expansion.",
        "Building a monolithic general prover before the three return contracts work end to end.",
    ),
    attachment(
        "FM-B",
        "K0 K2",
        "FCE PHIL ORT COM",
        "One valid and several minimally corrupted certificates for every compiler conclusion type.",
        "Define a conclusion-sensitive proof grammar and build a small independent verifier separated from the search implementation.",
        "A valid certificate versus mutations that omit one assumption or inference.",
        "Verifier, certificate grammar, mutation tests, and conclusion-grade receipt.",
        "Every inference and assumption has a rejection control.",
        "Treating compiler success, test coverage, or a serialized trace as ontological proof.",
    ),
    attachment(
        "EM-A",
        "K0 K3 K5 K6",
        "EMA CFS ORT COM",
        "The smallest coherent proper-time process with a classical-history convex hull and a recombination observable.",
        "Calculate the coherent prediction and full classical channel set, optimize the separating control, and build the calibration budget around the predicted margin.",
        "Coherent history recombination versus the strongest classical random-history channel with identical average shift.",
        "Assay passport, convex-null distance, error budget, sample rule, and full outcome record.",
        "The simulated separation exceeds systematic and model-completion uncertainty under held-out calibration.",
        "Looking for a frequency shift or dephasing that a classical mixture can reproduce.",
    ),
    attachment(
        "EM-B",
        "K0 K3 K5 K6 K8",
        "EMA CFS COM PHIL",
        "A routed quantum twin with one authenticated provenance distinction and matched ordinary channel capacity.",
        "Sweep provenance capacity while holding noise, decoder, energy, access, and task fixed; estimate the threshold before translating to a clock.",
        "One added provenance distinction at fixed conventional channel resources.",
        "Operational provenance measure, response surface, threshold uncertainty, and platform error requirement.",
        "The twin predicts a robust effect large enough for a frozen clock assay.",
        "Changing the decoder, observer boundary, or provenance definition at each setting.",
    ),
    attachment(
        "TR-A",
        "K0 K2 K3 K8",
        "CAT CFS ORT PHIL",
        "A matched protocol pair with identical action task but different finality or optionality.",
        "Define action optionality and resource monotones, derive a convex or information-theoretic lower bound, and seek an achieving construction.",
        "Equal task performance under a complete resource ledger with versus without the focal finality structure.",
        "Lower and upper bounds, achieving specimen, complete ledger, and remaining gap.",
        "The operational measure and ledger transfer unchanged across a second fixture.",
        "Comparing unmatched capabilities or omitting memory, coherence, trust, and support.",
    ),
    attachment(
        "TR-B",
        "K0 K3 K8",
        "ORT EMA PHIL COM",
        "The same matched protocols and complete ledger used by TR-A.",
        "Construct the strongest reversible or ordinary-accounting implementation and explicitly absorb every apparent actualization cost into known resources.",
        "Focal protocol versus a fully resource-matched ordinary implementation.",
        "Residual upper bound and the protocol that attains it.",
        "Every ledger term is operationally matched and the residual is calibration-limited.",
        "Defining the residual to be zero or weakening the comparison protocol.",
    ),
    attachment(
        "CP-A",
        "K0 K1 K2 K3",
        "CAT CFS PHIL HET",
        "Two histories merged by one finite action set and split by one controlled action-set expansion.",
        "Construct the behavioral quotient under declared interventions, prove composition and refinement properties, and reserve a held-out intervention.",
        "The frozen quotient prediction versus one controlled expansion of admissible actions.",
        "Quotient object, functoriality conditions, held-out result, and exact refinement semantics.",
        "The quotient composes across two agents or process stages without semantic refit.",
        "Defining equivalence using every possible experiment and then claiming sufficiency.",
    ),
    attachment(
        "CP-B",
        "K0 K1 K2 K9",
        "PHIL CAT FCE ORT",
        "Two ontologically different models exactly equivalent on one frozen finite evidence surface.",
        "Construct the explicit operational translation and prove the equivalence while stating the additional intervention that would separate the models if available.",
        "Identical finite evidence and actions versus divergent ontological interpretation.",
        "Scoped underdetermination theorem, model pair, translation, and ontology-license grammar.",
        "The equivalence is exact on the declared surface and its scope is machine-readable.",
        "Turning finite underdetermination into universal anti-realism.",
    ),
    attachment(
        "CG-A",
        "K0 K1 K2 K9",
        "CAT FCE WILD PHIL",
        "The smallest pair of nonisomorphic candidate geometries sharing the same certified meta-records.",
        "Generate countermodels first, then add locality, dimension, scale, and regularity assumptions one at a time until uniqueness up to declared gauge is earned.",
        "Reconstruction-fit observables versus geometric observables reserved as held-out predictions.",
        "Minimal assumption set, reconstruction algorithm, gauge class, and irreducible countermodel.",
        "A held-out geometric prediction succeeds without changing the record definition.",
        "Importing dimension, metric, manifold, or causal geometry through the input record.",
    ),
    attachment(
        "CG-B",
        "K0 K1 K2 K5 K9",
        "CAT EMA ORT WILD",
        "A synthetic discrete complex with known curvature plus flat topologically nontrivial controls.",
        "Define a discrete connection and gauge-invariant loop observable, subtract complete ordinary phases, and test naturality under controlled refinement.",
        "Known curved, flat, and topology-only specimens under the same route and control implementation.",
        "Refinement law, invariance audit, collision table, and continuum candidate map.",
        "The observable converges consistently across independent covers and survives the implementation-complete null.",
        "Calling every route-dependent phase curvature or fitting a continuum story per cover.",
    ),
    attachment(
        "NW-A",
        "K0 K1 K2 K4 K8",
        "CAT FCE ORT COM",
        "The smallest temporal network for which static and time-respecting authenticated cuts differ.",
        "Build a time-expanded authenticated flow graph and seek matching max-flow/min-cut converse and achievability under the frozen adversary.",
        "Static connectivity versus time-respecting authenticated capacity for one action commodity.",
        "Cut certificate, achieving code or protocol, and adversarial trace.",
        "The theorem predicts a larger replayable network without changing authentication semantics.",
        "Using static or unauthenticated channel capacity as reality bandwidth.",
    ),
    attachment(
        "NW-B",
        "K0 K3 K4 K5",
        "CFS EMA RPO HET",
        "One common task instantiated on matched distributed and routed-quantum twins with controlled edge interventions.",
        "Use factorial topology changes while separately holding access, provenance, noise, and resources fixed; fit a preregistered sparse causal response.",
        "Held-out edge additions or removals with all non-topological fields frozen.",
        "Causal topology contributions, interaction terms, predictions, and failed invariance cases.",
        "The same decomposition predicts held-out interventions on both twins.",
        "Post hoc regression on convenient graph summaries or allowing topology to change the task.",
    ),
]


def main() -> None:
    source_bytes = SOURCE_PATH.read_bytes()
    source = json.loads(source_bytes)
    source_hypotheses = source["hypotheses"]
    source_ids = [item["id"] for item in source_hypotheses]
    source_by_id = {item["id"]: item for item in source_hypotheses}

    lens_ids = {item["id"] for item in LENSES}
    attachment_ids = [item["hypothesis_id"] for item in ATTACHMENTS]
    required_fields = {
        "hypothesis_id",
        "method_kits",
        "lead_lenses",
        "smallest_informative_object",
        "recommended_attack",
        "first_decisive_contrast",
        "reusable_output",
        "scale_up_when",
        "avoid",
    }
    forbidden_priority_fields = {
        "priority",
        "rank",
        "grade",
        "vote",
        "worth",
        "eliminate",
        "defer",
        "authorization",
    }

    checks = [
        {
            "id": "source_panel_complete",
            "passed": len(source_hypotheses) == 36
            and source.get("checks_passed") == source.get("checks_total") == 8,
        },
        {
            "id": "exactly_ten_distinct_lenses",
            "passed": len(LENSES) == len(lens_ids) == 10,
        },
        {
            "id": "requested_lenses_present",
            "passed": {"CAT", "CFS", "ORT", "HET", "COM", "WILD", "PHIL"}
            <= lens_ids,
        },
        {
            "id": "one_attachment_per_source_hypothesis",
            "passed": len(ATTACHMENTS) == len(set(attachment_ids)) == 36
            and set(attachment_ids) == set(source_ids),
        },
        {
            "id": "all_attachment_fields_complete",
            "passed": all(
                set(item) == required_fields
                and all(item[field] for field in required_fields)
                for item in ATTACHMENTS
            ),
        },
        {
            "id": "method_and_lens_references_valid",
            "passed": all(
                item["method_kits"]
                and item["method_kits"][0] == "K0"
                and set(item["method_kits"]) <= set(METHOD_KITS)
                and set(item["lead_lenses"]) <= lens_ids
                for item in ATTACHMENTS
            ),
        },
        {
            "id": "divergent_lens_support_per_attachment",
            "passed": all(len(set(item["lead_lenses"])) >= 2 for item in ATTACHMENTS),
        },
        {
            "id": "every_shared_method_kit_exercised",
            "passed": set(METHOD_KITS)
            == {
                kit
                for item in ATTACHMENTS
                for kit in item["method_kits"]
            },
        },
        {
            "id": "no_priority_or_grade_override",
            "passed": all(
                not (set(item) & forbidden_priority_fields) for item in ATTACHMENTS
            ),
        },
        {
            "id": "source_titles_resolve",
            "passed": all(
                source_by_id[item["hypothesis_id"]]["title"]
                for item in ATTACHMENTS
            ),
        },
    ]

    enriched_attachments = [
        {
            **item,
            "source_title": source_by_id[item["hypothesis_id"]]["title"],
            "source_owner": source_by_id[item["hypothesis_id"]]["owner"],
        }
        for item in ATTACHMENTS
    ]
    passed = sum(int(check["passed"]) for check in checks)
    result = {
        "probe": "du_hypothesis_efficient_approach_registry_probe",
        "run_id": "RUN-20260724-200626-ten-lens-learning-rate-panel",
        "status": "COMPLETE_METHOD_ATTACHMENT_REGISTRY",
        "source": str(SOURCE_PATH.relative_to(ROOT)),
        "source_sha256": hashlib.sha256(source_bytes).hexdigest(),
        "purpose": "Improve how a lead attacks any chosen hypothesis without selecting, eliminating, deferring, grading, or reranking hypotheses.",
        "lenses": LENSES,
        "method_kits": METHOD_KITS,
        "attachments": enriched_attachments,
        "totals": {
            "lenses": len(LENSES),
            "method_kits": len(METHOD_KITS),
            "source_hypotheses": len(source_hypotheses),
            "attachments": len(ATTACHMENTS),
        },
        "checks": checks,
        "checks_passed": passed,
        "checks_total": len(checks),
        "scientific_evidence": False,
        "hypothesis_priority_effect": "NONE",
        "hypothesis_grade_effect": "NONE",
        "authorization_effect": "NONE",
        "not_established": [
            "truth or novelty of any hypothesis",
            "comparative worth or execution priority",
            "scientific validity of a recommended method",
            "authorization for a physical experiment or external action",
        ],
    }

    OUTPUT_PATH.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(
        f"{result['status']}: {passed}/{len(checks)} checks; "
        f"{len(ATTACHMENTS)} hypotheses; {len(LENSES)} lenses; "
        f"{len(METHOD_KITS)} shared method kits"
    )
    if passed != len(checks):
        failed = [check["id"] for check in checks if not check["passed"]]
        raise SystemExit(f"failed checks: {failed}")


if __name__ == "__main__":
    main()
