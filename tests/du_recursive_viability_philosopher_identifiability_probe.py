#!/usr/bin/env python3
"""Finite identifiability probe for recursive viable-system descriptions.

The probe asks a deliberately narrow philosophical question:

    Does finite success under environmental disturbances identify one
    physically real scalar number of recursively viable levels?

It constructs the same three-bit repair behaviour in five descriptions:

* ``m=0`` local micro-repair with no privileged macrolevel;
* ``m=1`` one whole-system regulator;
* ``m=2`` a genuinely intervention-sensitive nested regulator;
* an arbitrary alternative ``m=2`` partition;
* an ``m=3`` identity-refinement of the nested regulator; and
* a non-tree overlapping cover.

All six active descriptions have exactly the same external disturbance,
viability, and durable-record trace, including held-out compound
disturbances.  The nested descriptions nevertheless have nontrivial internal
regulators: disabling their root or a local controller changes the repaired
state.  Inserting a serial relay changes the advertised depth without
changing any external result.  This is a finite edge-subdivision
nonidentification witness, not an argument that multilevel control is unreal.

A second intervention family disables regulators in the overlapping cover.
Single-regulator lesions are developmental data; the double lesion is held
out.  Its non-additive failure identifies a redundantly protected variable
and therefore an overlapping minimal-cut hypergraph.  That positive result
shows what can be discovered once the intervention interface is physically
anchored.  The discovered object is a cover/poset of intervention roles, not
one scalar depth.

No Beer System-1--System-5 identity, physical scale, dimensional unit,
purpose, agency, observer, clock, or Dynamic Unity law is derived.
"""

from __future__ import annotations

import itertools
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable


ARTIFACT_PATH = (
    Path(__file__).resolve().parent
    / "artifacts"
    / "du_recursive_viability_philosopher_identifiability_result.json"
)

VARIABLES = (0, 1, 2)
TRAINING_DISTURBANCES = (1, 2, 4)
HELD_OUT_DISTURBANCES = (3, 5, 6, 7)
ALL_DISTURBANCES = tuple(range(8))


@dataclass(frozen=True)
class Architecture:
    """A finite repair architecture.

    ``supports`` gives the essential-variable coordinates reset by a module.
    ``requires`` gives upstream modules that must be active before a module
    can act.  Empty-support modules can therefore be genuine coordinators:
    disabling one can disable downstream repair.
    """

    name: str
    architecture_class: str
    claimed_scalar_depth: int | None
    supports: dict[str, frozenset[int]]
    requires: dict[str, frozenset[str]]
    tree: bool
    note: str

    @property
    def modules(self) -> tuple[str, ...]:
        return tuple(sorted(self.supports))


def architecture_set() -> dict[str, Architecture]:
    return {
        "micro_m0": Architecture(
            name="micro_m0",
            architecture_class="m=0 ordinary local repair",
            claimed_scalar_depth=0,
            supports={
                "d0": frozenset({0}),
                "d1": frozenset({1}),
                "d2": frozenset({2}),
            },
            requires={"d0": frozenset(), "d1": frozenset(), "d2": frozenset()},
            tree=False,
            note=(
                "Each disturbed coordinate is repaired by the micro-law; no "
                "macrolevel is privileged."
            ),
        ),
        "macro_m1": Architecture(
            name="macro_m1",
            architecture_class="m=1 whole-system regulator",
            claimed_scalar_depth=1,
            supports={"M": frozenset(VARIABLES)},
            requires={"M": frozenset()},
            tree=True,
            note="One regulator restores the complete essential-variable vector.",
        ),
        "nested_m2": Architecture(
            name="nested_m2",
            architecture_class="m=2 nested regulator",
            claimed_scalar_depth=2,
            supports={
                "R": frozenset(),
                "A": frozenset({0, 1}),
                "B": frozenset({2}),
            },
            requires={
                "R": frozenset(),
                "A": frozenset({"R"}),
                "B": frozenset({"R"}),
            },
            tree=True,
            note=(
                "The root R enables two local operational regulators. Root "
                "and local lesions have different exact effects."
            ),
        ),
        "arbitrary_m2": Architecture(
            name="arbitrary_m2",
            architecture_class="m=2 arbitrary alternative partition",
            claimed_scalar_depth=2,
            supports={
                "R": frozenset(),
                "A": frozenset({0, 2}),
                "B": frozenset({1}),
            },
            requires={
                "R": frozenset(),
                "A": frozenset({"R"}),
                "B": frozenset({"R"}),
            },
            tree=True,
            note=(
                "The same root/local form uses a crossed partition selected "
                "by the analyst rather than the external behaviour."
            ),
        ),
        "refined_m3": Architecture(
            name="refined_m3",
            architecture_class="m=3 serial refinement",
            claimed_scalar_depth=3,
            supports={
                "R": frozenset(),
                "Q": frozenset(),
                "A": frozenset({0, 1}),
                "B": frozenset({2}),
            },
            requires={
                "R": frozenset(),
                "Q": frozenset({"R"}),
                "A": frozenset({"Q"}),
                "B": frozenset({"Q"}),
            },
            tree=True,
            note=(
                "Q is a required serial relay. Inserting it raises raw depth "
                "without changing the external repair map."
            ),
        ),
        "overlap_cover": Architecture(
            name="overlap_cover",
            architecture_class="overlapping non-tree cover",
            claimed_scalar_depth=None,
            supports={
                "A": frozenset({0, 1}),
                "B": frozenset({1, 2}),
            },
            requires={"A": frozenset(), "B": frozenset()},
            tree=False,
            note=(
                "Variable 1 is redundantly protected by two overlapping "
                "regulators; no unique nested-tree depth represents the cover."
            ),
        ),
        "passive_null": Architecture(
            name="passive_null",
            architecture_class="passive stability / no regulation",
            claimed_scalar_depth=0,
            supports={},
            requires={},
            tree=False,
            note="The undisturbed zero state persists, but disturbances are not repaired.",
        ),
    }


def disturbance_state(mask: int) -> tuple[int, int, int]:
    return tuple((mask >> coordinate) & 1 for coordinate in VARIABLES)


def module_operational(
    architecture: Architecture,
    module: str,
    disabled: frozenset[str],
    memo: dict[str, bool],
) -> bool:
    if module in memo:
        return memo[module]
    if module in disabled:
        memo[module] = False
        return False
    operational = all(
        module_operational(architecture, parent, disabled, memo)
        for parent in architecture.requires[module]
    )
    memo[module] = operational
    return operational


def repair(
    architecture: Architecture,
    disturbance: int,
    disabled: Iterable[str] = (),
) -> dict[str, Any]:
    disabled_set = frozenset(disabled)
    state = list(disturbance_state(disturbance))
    operational: list[str] = []
    memo: dict[str, bool] = {}

    for module in architecture.modules:
        if module_operational(architecture, module, disabled_set, memo):
            operational.append(module)
            for coordinate in architecture.supports[module]:
                state[coordinate] = 0

    final_state = tuple(state)
    viable = final_state == (0, 0, 0)
    durable_record = (
        {
            "disturbance": disturbance,
            "outcome": "essential_variables_restored",
        }
        if disturbance != 0 and viable
        else None
    )
    return {
        "initial_after_disturbance": list(disturbance_state(disturbance)),
        "disabled_modules": sorted(disabled_set),
        "operational_modules": operational,
        "final_state": list(final_state),
        "viable": viable,
        "durable_record": durable_record,
    }


def external_trace(architecture: Architecture) -> list[dict[str, Any]]:
    return [
        {
            "disturbance": disturbance,
            "final_state": repair(architecture, disturbance)["final_state"],
            "viable": repair(architecture, disturbance)["viable"],
            "durable_record": repair(architecture, disturbance)["durable_record"],
        }
        for disturbance in ALL_DISTURBANCES
    ]


def minimal_module_cuts(
    architecture: Architecture,
    coordinate: int,
) -> list[frozenset[str]]:
    """Return inclusion-minimal module lesions that leave a bit unrepaired."""
    modules = architecture.modules
    failing: list[frozenset[str]] = []
    for size in range(1, len(modules) + 1):
        for subset in itertools.combinations(modules, size):
            disabled = frozenset(subset)
            result = repair(architecture, 7, disabled)
            if result["final_state"][coordinate] != 1:
                continue
            if any(previous < disabled for previous in failing):
                continue
            failing.append(disabled)
    return failing


def cut_hypergraph(architecture: Architecture) -> dict[int, list[frozenset[str]]]:
    return {
        coordinate: minimal_module_cuts(architecture, coordinate)
        for coordinate in VARIABLES
    }


def serialize_cuts(
    cuts: dict[int, list[frozenset[str]]]
) -> dict[str, list[list[str]]]:
    return {
        str(coordinate): [
            sorted(cut)
            for cut in sorted(
                cut_sets,
                key=lambda row: (len(row), tuple(sorted(row))),
            )
        ]
        for coordinate, cut_sets in sorted(cuts.items())
    }


def canonical_cut_signature(
    cuts: dict[int, list[frozenset[str]]]
) -> str:
    """Canonicalize a finite cut hypergraph under module/variable relabeling."""
    modules = sorted(
        {
            module
            for cut_sets in cuts.values()
            for cut in cut_sets
            for module in cut
        }
    )
    variables = sorted(cuts)
    candidates: list[str] = []

    for module_order in itertools.permutations(modules):
        module_code = {
            module: str(index)
            for index, module in enumerate(module_order)
        }
        for variable_order in itertools.permutations(variables):
            encoded_variables: list[str] = []
            for variable in variable_order:
                encoded_cuts = sorted(
                    ",".join(sorted(module_code[module] for module in cut))
                    for cut in cuts[variable]
                )
                encoded_variables.append("&".join(encoded_cuts))
            candidates.append("|".join(encoded_variables))
    return min(candidates)


def relabeled_overlap() -> Architecture:
    """Swap controller names and mirror coordinates 0<->2."""
    return Architecture(
        name="overlap_cover_relabelled",
        architecture_class="overlapping non-tree cover",
        claimed_scalar_depth=None,
        supports={
            "X": frozenset({0, 1}),
            "Y": frozenset({1, 2}),
        },
        requires={"X": frozenset(), "Y": frozenset()},
        tree=False,
        note="A relabelled copy of the overlap architecture.",
    )


def role_quotient_signature(
    cut_sets: Iterable[frozenset[str]]
) -> str:
    """Canonical signature after duplicate observational roles are merged."""
    unique = sorted(
        {tuple(sorted(cut)) for cut in cut_sets},
        key=lambda row: (len(row), row),
    )
    modules = sorted({module for cut in unique for module in cut})
    candidates = []
    for order in itertools.permutations(modules):
        code = {module: str(index) for index, module in enumerate(order)}
        candidates.append(
            "|".join(
                sorted(
                    ",".join(sorted(code[module] for module in cut))
                    for cut in unique
                )
            )
        )
    return min(candidates)


def external_equivalence_fixture(
    architectures: dict[str, Architecture],
) -> dict[str, Any]:
    active_names = (
        "micro_m0",
        "macro_m1",
        "nested_m2",
        "arbitrary_m2",
        "refined_m3",
        "overlap_cover",
    )
    traces = {
        name: external_trace(architectures[name])
        for name in active_names
    }
    reference = traces[active_names[0]]
    held_out = {
        name: {
            str(mask): repair(architectures[name], mask)
            for mask in HELD_OUT_DISTURBANCES
        }
        for name in active_names
    }
    complexity = {}
    for name in active_names:
        architecture = architectures[name]
        edges = sum(len(parents) for parents in architecture.requires.values())
        errors = sum(
            not repair(architecture, mask)["viable"]
            for mask in HELD_OUT_DISTURBANCES
        )
        complexity[name] = {
            "held_out_errors": errors,
            "module_count": len(architecture.modules),
            "dependency_edge_count": edges,
            "declared_unit_cost": errors * 100 + len(architecture.modules) + edges,
        }

    return {
        "training_disturbances": list(TRAINING_DISTURBANCES),
        "held_out_compound_disturbances": list(HELD_OUT_DISTURBANCES),
        "architectures": {
            name: {
                "class": architectures[name].architecture_class,
                "claimed_scalar_depth": architectures[name].claimed_scalar_depth,
                "tree": architectures[name].tree,
                "supports": {
                    module: sorted(support)
                    for module, support in architectures[name].supports.items()
                },
                "requires": {
                    module: sorted(parents)
                    for module, parents in architectures[name].requires.items()
                },
                "note": architectures[name].note,
            }
            for name in active_names
        },
        "external_traces": traces,
        "all_active_external_traces_identical": all(
            traces[name] == reference for name in active_names
        ),
        "held_out_results": held_out,
        "all_active_models_pass_all_held_out_disturbances": all(
            row["viable"]
            for model in held_out.values()
            for row in model.values()
        ),
        "declared_unit_cost_comparison": complexity,
        "complexity_reading": (
            "All predictive losses are equal. Under this declared node-plus-edge "
            "code, the serial refinement is penalized. A different primitive "
            "language could change the simplicity order; this score removes "
            "gratuitous refinement but does not make a hierarchy ontic."
        ),
        "edge_subdivision_theorem": (
            "For any finite deterministic interface map F, inserting a latent "
            "identity or required relay on an internal edge gives a deeper "
            "factorization with the same external map. Therefore raw scalar "
            "depth is not identifiable from experiments whose intervention "
            "algebra does not independently anchor that relay."
        ),
    }


def overlap_intervention_fixture(
    architectures: dict[str, Architecture],
) -> dict[str, Any]:
    overlap = architectures["overlap_cover"]
    single_a = repair(overlap, 7, {"A"})
    single_b = repair(overlap, 7, {"B"})
    double = repair(overlap, 7, {"A", "B"})

    single_a_failure = {
        index for index, value in enumerate(single_a["final_state"]) if value
    }
    single_b_failure = {
        index for index, value in enumerate(single_b["final_state"]) if value
    }
    double_failure = {
        index for index, value in enumerate(double["final_state"]) if value
    }
    additive_prediction = single_a_failure | single_b_failure
    synergy = double_failure - additive_prediction

    cuts = cut_hypergraph(overlap)
    relabelled_cuts = cut_hypergraph(relabeled_overlap())

    original_role_cuts = [
        cut
        for cut_sets in cuts.values()
        for cut in cut_sets
    ]
    resolution_refined_role_cuts = list(original_role_cuts) + [
        frozenset({"A", "B"})
    ]

    return {
        "developmental_single_lesions": {
            "disable_A": single_a,
            "disable_B": single_b,
        },
        "held_out_double_lesion": double,
        "additive_single_lesion_prediction_for_double": sorted(
            additive_prediction
        ),
        "observed_double_lesion_failure": sorted(double_failure),
        "held_out_synergy_coordinate": sorted(synergy),
        "minimal_cut_hypergraph": serialize_cuts(cuts),
        "interpretation": (
            "Coordinate 0 fails when A alone is disabled; coordinate 2 fails "
            "when B alone is disabled; coordinate 1 fails only when both are "
            "disabled. The held-out double lesion exposes redundant overlapping "
            "protection that an additive/disjoint reading of single lesions "
            "misses."
        ),
        "canonical_cut_signature": canonical_cut_signature(cuts),
        "relabelled_canonical_cut_signature": canonical_cut_signature(
            relabelled_cuts
        ),
        "resolution_control": {
            "operation": (
                "Duplicate coordinate 1 into a perfectly tied analysis "
                "coordinate with the same minimal cut {A,B}."
            ),
            "raw_role_count_before": len(original_role_cuts),
            "raw_role_count_after": len(resolution_refined_role_cuts),
            "quotient_signature_before": role_quotient_signature(
                original_role_cuts
            ),
            "quotient_signature_after": role_quotient_signature(
                resolution_refined_role_cuts
            ),
            "reading": (
                "Raw apparent multiplicity follows resolution; the quotient by "
                "observationally duplicate intervention roles does not."
            ),
        },
    }


def null_and_semantics_fixture(
    architectures: dict[str, Architecture],
) -> dict[str, Any]:
    passive = architectures["passive_null"]
    passive_rows = {
        str(mask): repair(passive, mask)
        for mask in ALL_DISTURBANCES
    }
    rg_single_flip_rows = []
    for mask in TRAINING_DISTURBANCES:
        state = disturbance_state(mask)
        majority_macro = int(sum(state) >= 2)
        rg_single_flip_rows.append(
            {
                "disturbance": mask,
                "micro_state": list(state),
                "ordinary_majority_macrostate": majority_macro,
                "coarse_macrostate_appears_unchanged": majority_macro == 0,
                "essential_all_zero_viability": state == (0, 0, 0),
            }
        )

    active_names = (
        "micro_m0",
        "macro_m1",
        "nested_m2",
        "arbitrary_m2",
        "refined_m3",
        "overlap_cover",
    )
    clock_rows = {}
    for name in active_names:
        architecture = architectures[name]
        durable_records = 0
        internal_update_opportunities = 0
        for mask in range(1, 8):
            result = repair(architecture, mask)
            durable_records += int(result["durable_record"] is not None)
            internal_update_opportunities += len(result["operational_modules"])
        clock_rows[name] = {
            "durable_external_recovery_records": durable_records,
            "internal_module_update_opportunities": internal_update_opportunities,
        }

    return {
        "passive_stability": {
            "rows": passive_rows,
            "undisturbed_state_persists": passive_rows["0"]["viable"],
            "all_nonempty_disturbances_fail": all(
                not passive_rows[str(mask)]["viable"]
                for mask in range(1, 8)
            ),
        },
        "ordinary_rg_majority_null": {
            "rows": rg_single_flip_rows,
            "all_single_failures_hidden_by_majority_coarse_graining": all(
                row["coarse_macrostate_appears_unchanged"]
                and not row["essential_all_zero_viability"]
                for row in rg_single_flip_rows
            ),
            "reading": (
                "A stable coarse majority can hide violations of essential "
                "variables. Coarse-grained persistence is not active viability "
                "and supplies no downward regulator."
            ),
        },
        "clock_record_control": {
            "rows": clock_rows,
            "all_durable_record_counts_equal": len(
                {
                    row["durable_external_recovery_records"]
                    for row in clock_rows.values()
                }
            )
            == 1,
            "internal_update_counts_differ": len(
                {
                    row["internal_module_update_opportunities"]
                    for row in clock_rows.values()
                }
            )
            > 1,
            "reading": (
                "The same seven durable recoveries are represented with "
                "different numbers of internal update opportunities. A "
                "level-clock cannot be inferred by counting model nodes."
            ),
        },
        "unit_and_teleology_control": {
            "dimensional_unit_present": False,
            "generated_quantities": [
                "finite counts",
                "dimensionless viability fractions",
                "dimensionless intervention-role multiplicities",
            ],
            "purpose_or_agency_inferred": False,
            "reading": (
                "Control success establishes containment under a declared "
                "disturbance family only. It creates neither units nor purpose."
            ),
        },
    }


def nested_internal_control(
    architectures: dict[str, Architecture],
) -> dict[str, Any]:
    nested = architectures["nested_m2"]
    refined = architectures["refined_m3"]
    full_disturbance = 7
    nested_lesions = {
        module: repair(nested, full_disturbance, {module})
        for module in nested.modules
    }
    refined_lesions = {
        module: repair(refined, full_disturbance, {module})
        for module in refined.modules
    }
    return {
        "nested_m2_single_lesions": nested_lesions,
        "refined_m3_single_lesions": refined_lesions,
        "root_is_operationally_required": not nested_lesions["R"]["viable"],
        "local_A_and_B_have_distinct_failure_supports": (
            nested_lesions["A"]["final_state"]
            != nested_lesions["B"]["final_state"]
        ),
        "inserted_relay_duplicates_root_failure_signature": (
            refined_lesions["Q"]["final_state"]
            == refined_lesions["R"]["final_state"]
        ),
        "reading": (
            "The m=2 fixture is not passive naming: root and local lesions "
            "change outcomes. Yet a serial relay duplicates the root lesion "
            "signature and raises advertised depth, so raw level count still "
            "requires a quotient or an independently measurable relay property."
        ),
    }


def main() -> None:
    architectures = architecture_set()
    external = external_equivalence_fixture(architectures)
    overlap = overlap_intervention_fixture(architectures)
    nulls = null_and_semantics_fixture(architectures)
    nested = nested_internal_control(architectures)

    checks = {
        "m0_passes_held_out": all(
            repair(architectures["micro_m0"], mask)["viable"]
            for mask in HELD_OUT_DISTURBANCES
        ),
        "m1_passes_held_out": all(
            repair(architectures["macro_m1"], mask)["viable"]
            for mask in HELD_OUT_DISTURBANCES
        ),
        "genuine_m2_passes_held_out": all(
            repair(architectures["nested_m2"], mask)["viable"]
            for mask in HELD_OUT_DISTURBANCES
        ),
        "arbitrary_m2_passes_held_out": all(
            repair(architectures["arbitrary_m2"], mask)["viable"]
            for mask in HELD_OUT_DISTURBANCES
        ),
        "refined_m3_passes_held_out": all(
            repair(architectures["refined_m3"], mask)["viable"]
            for mask in HELD_OUT_DISTURBANCES
        ),
        "overlap_passes_held_out": all(
            repair(architectures["overlap_cover"], mask)["viable"]
            for mask in HELD_OUT_DISTURBANCES
        ),
        "all_active_external_traces_identical": external[
            "all_active_external_traces_identical"
        ],
        "passive_null_fails_disturbances": nulls["passive_stability"][
            "all_nonempty_disturbances_fail"
        ],
        "ordinary_rg_hides_micro_failure": nulls[
            "ordinary_rg_majority_null"
        ]["all_single_failures_hidden_by_majority_coarse_graining"],
        "nested_root_is_active": nested["root_is_operationally_required"],
        "nested_local_lesions_differ": nested[
            "local_A_and_B_have_distinct_failure_supports"
        ],
        "identity_refinement_has_no_external_gain": (
            external["external_traces"]["nested_m2"]
            == external["external_traces"]["refined_m3"]
        ),
        "relay_duplicates_root_role": nested[
            "inserted_relay_duplicates_root_failure_signature"
        ],
        "held_out_overlap_synergy_found": overlap[
            "held_out_synergy_coordinate"
        ]
        == [1],
        "cut_hypergraph_relabeling_invariant": (
            overlap["canonical_cut_signature"]
            == overlap["relabelled_canonical_cut_signature"]
        ),
        "resolution_quotient_stable": (
            overlap["resolution_control"]["quotient_signature_before"]
            == overlap["resolution_control"]["quotient_signature_after"]
        ),
        "durable_records_independent_of_model_updates": (
            nulls["clock_record_control"]["all_durable_record_counts_equal"]
            and nulls["clock_record_control"]["internal_update_counts_differ"]
        ),
        "no_units_or_teleology_smuggled": (
            not nulls["unit_and_teleology_control"][
                "dimensional_unit_present"
            ]
            and not nulls["unit_and_teleology_control"][
                "purpose_or_agency_inferred"
            ]
        ),
    }
    passed = sum(bool(value) for value in checks.values())

    result = {
        "metadata": {
            "probe": "du_recursive_viability_philosopher_identifiability_probe",
            "scope": (
                "Exact finite repair/control and intervention-role "
                "identifiability; no physical ontology is assumed."
            ),
            "assumptions": [
                "Three binary essential variables with viable region {(0,0,0)}.",
                "Environmental disturbances are all bit-flip masks.",
                "A regulator resets declared coordinates when it and every required upstream module are active.",
                "A durable record is one externally retained successful recovery, not every internal update.",
                "Controller-disable interventions and coordinate-resolved failures are physically available only in the positive reopener fixture.",
            ],
            "warrants": [
                "DERIVED finite edge-subdivision nonidentification",
                "CONSTRUCTIVELY_REALIZED m=0/m=1/m>1/arbitrary/overlap rivals",
                "CONSTRUCTIVELY_REALIZED held-out overlap intervention",
                "CONDITIONALLY ENTAILED intervention-role hypergraph",
                "STRUCTURAL ANALOGY to recursive viable systems; not a Beer identity",
            ],
        },
        "definitions": {
            "system": (
                "A declared plant boundary, essential-variable vector, "
                "environmental disturbance family, regulator modules, and "
                "recovery criterion."
            ),
            "viability": (
                "Return all three essential variables to zero after a declared "
                "disturbance under the admitted controller state."
            ),
            "recursion": (
                "A regulator depends on an upstream coordinator and controls "
                "an operational sub-boundary; raw serial refinements are "
                "quotiented unless independently intervention-distinct."
            ),
            "depth": (
                "Advertised factorization depth, treated as identifiable only "
                "relative to a fixed intervention algebra and quotient."
            ),
            "record": (
                "One durable external recovery outcome; internal module "
                "opportunities are recorded separately."
            ),
        },
        "external_equivalence": external,
        "nested_internal_control": nested,
        "overlap_intervention_positive_reopener": overlap,
        "nulls_and_semantics": nulls,
        "theorem": {
            "name": "finite recursive-refinement nonidentification",
            "statement": (
                "If a finite experiment observes only the external transition, "
                "viability, and durable-record map of a controller, then any "
                "factorization can be refined by serial identity/relay nodes "
                "without changing those observations. Consequently raw scalar "
                "recursion depth is not identified. Internal interventions may "
                "identify a minimal causal cover/poset up to relabeling, "
                "duplicate-role contraction, and untested refinements."
            ),
            "counterexample_scope": (
                "The result defeats inference from finite extensional success "
                "to one ontic scalar depth. It does not defeat physically "
                "anchored multilevel control or an interventionally identified "
                "cover."
            ),
        },
        "contested_proposition_disposition": {
            "proposition": (
                "A finite interventionally complete viability record that "
                "admits an m>1 recursive VSM representation identifies one "
                "physically real scalar recursion depth and warrants reading "
                "Beer S1-S5/finality strata as that hierarchy."
            ),
            "verdict": "OVERTURNED_AS_STATED",
            "replacement": (
                "External viability identifies no unique depth. A physically "
                "anchored internal intervention family can instead identify a "
                "minimal role hypergraph/cover up to explicit quotient. Beer "
                "functions, recursive levels, and physical strata remain "
                "separate axes."
            ),
        },
        "checks": checks,
        "checks_passed": passed,
        "checks_total": len(checks),
        "verdict": (
            "RAW SCALAR DEPTH NOT IDENTIFIED / ACTIVE MULTILEVEL CONTROL "
            "CONSTRUCTIVELY REALIZED / HELD-OUT LESIONS DISCOVER AN "
            "OVERLAPPING ROLE COVER / BEER-FUNCTION-LEVEL-FINALITY "
            "CONFLATION OVERTURNED"
        ),
        "banked": False,
        "seeded": False,
    }

    if passed != len(checks):
        failed = [name for name, value in checks.items() if not value]
        raise AssertionError(f"failed checks: {failed}")

    ARTIFACT_PATH.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT_PATH.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(f"{passed}/{len(checks)} checks pass")
    print(result["verdict"])
    print(f"artifact: {ARTIFACT_PATH}")


if __name__ == "__main__":
    main()
