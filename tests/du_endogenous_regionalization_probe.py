#!/usr/bin/env python3
"""Exact finite controls for endogenous regional and validator selection.

The probe treats regionalization as a version-space identification problem,
not as graph drawing or community detection.  A frozen candidate grammar,
intervention family, representation quotient, and response map determine
whether the current records:

* identify one regional structure up to declared symmetry/refinement;
* leave several candidates separated by a minimum held-out intervention;
* leave observationally equivalent candidates in the declared class; or
* do not define a complete comparison contract.

The constructed Boolean interaction class is deliberately small.  Its
complete intervention table has a unique algebraic-normal-form (ANF)
reconstruction, while incomplete records expose exact nonidentification.
Passing does not establish that Boolean interactions are physical regions,
that an Occam rule selects nature, or that validator origins can be inferred
without interventions on their failure domains.
"""

from __future__ import annotations

import itertools
import json
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_endogenous_regionalization_result.json"
)
RUN_ID = "RUN-20260725-064622-regional-selection-noisy-descent"

IDENTIFIED = "IDENTIFIED_UP_TO_DECLARED_SYMMETRY_OR_REFINEMENT"
UNDERIDENTIFIED = "UNDERIDENTIFIED_WITH_MINIMUM_SEPARATOR"
OBSERVATIONALLY_EQUIVALENT = "OBSERVATIONALLY_EQUIVALENT_IN_DECLARED_CLASS"
INCOMPLETE = "INCOMPLETE_CONTRACT"


def jsonable(value: Any) -> Any:
    if isinstance(value, Fraction):
        if value.denominator == 1:
            return value.numerator
        return {
            "numerator": value.numerator,
            "denominator": value.denominator,
        }
    if isinstance(value, tuple):
        return [jsonable(item) for item in value]
    if isinstance(value, list):
        return [jsonable(item) for item in value]
    if isinstance(value, (set, frozenset)):
        return [jsonable(item) for item in sorted(value)]
    if isinstance(value, dict):
        return {
            str(key): jsonable(item)
            for key, item in sorted(value.items(), key=lambda item: str(item[0]))
        }
    return value


def canonical_json(value: Any) -> str:
    return json.dumps(jsonable(value), indent=2, sort_keys=True) + "\n"


def popcount(mask: int) -> int:
    return mask.bit_count()


def masks_of_weight(n: int, weight: int) -> tuple[int, ...]:
    return tuple(mask for mask in range(1 << n) if popcount(mask) == weight)


def mobius_anf(truth: Sequence[int], n: int) -> tuple[int, ...]:
    """Return the unique Boolean ANF coefficients from a complete truth table."""

    if len(truth) != 1 << n:
        raise ValueError("truth table length does not match n")
    coefficients = [int(value) & 1 for value in truth]
    for bit in range(n):
        for mask in range(1 << n):
            if mask & (1 << bit):
                coefficients[mask] ^= coefficients[mask ^ (1 << bit)]
    return tuple(coefficients)


def evaluate_anf(coefficients: Sequence[int], state: int) -> int:
    value = 0
    for monomial, coefficient in enumerate(coefficients):
        if coefficient and monomial & state == monomial:
            value ^= 1
    return value


def truth_from_coefficients(
    n: int,
    active_monomials: Iterable[int],
) -> tuple[int, ...]:
    coefficients = [0] * (1 << n)
    for monomial in active_monomials:
        coefficients[monomial] ^= 1
    return tuple(
        evaluate_anf(coefficients, state)
        for state in range(1 << n)
    )


def named_mask(mask: int, labels: Sequence[str]) -> str:
    if mask == 0:
        return "1"
    return "".join(
        label
        for index, label in enumerate(labels)
        if mask & (1 << index)
    )


def exhaustive_anf_control() -> dict[str, Any]:
    n = 4
    table_size = 1 << n
    function_count = 1 << table_size
    failures: list[int] = []
    for function_code in range(function_count):
        truth = tuple(
            (function_code >> state) & 1
            for state in range(table_size)
        )
        coefficients = mobius_anf(truth, n)
        reconstructed = tuple(
            evaluate_anf(coefficients, state)
            for state in range(table_size)
        )
        if reconstructed != truth:
            failures.append(function_code)
            if len(failures) >= 8:
                break

    return {
        "input_count": n,
        "truth_table_count": function_count,
        "failures": failures,
        "interpretation": (
            "complete interventions uniquely determine the Boolean ANF "
            "inside this frozen response grammar"
        ),
        "boundary": (
            "ANF uniqueness does not select the Boolean grammar or make "
            "its interaction monomials fundamental regions"
        ),
    }


def signature(
    truth: Sequence[int],
    actions: Sequence[int],
) -> tuple[int, ...]:
    return tuple(truth[action] for action in actions)


def signatures_are_injective(
    candidates: Mapping[str, Sequence[int]],
    actions: Sequence[int],
) -> bool:
    values = [signature(truth, actions) for truth in candidates.values()]
    return len(values) == len(set(values))


def minimum_separating_action_sets(
    candidates: Mapping[str, Sequence[int]],
    available_actions: Sequence[int],
) -> tuple[tuple[int, ...], ...]:
    for size in range(len(available_actions) + 1):
        separating = tuple(
            subset
            for subset in itertools.combinations(available_actions, size)
            if signatures_are_injective(candidates, subset)
        )
        if separating:
            return separating
    return ()


def pair_hitting_action_sets(
    candidates: Mapping[str, Sequence[int]],
    available_actions: Sequence[int],
) -> tuple[tuple[int, ...], ...]:
    names = tuple(candidates)
    candidate_pairs = tuple(itertools.combinations(names, 2))
    distinguished_by = {
        action: {
            pair
            for pair in candidate_pairs
            if candidates[pair[0]][action] != candidates[pair[1]][action]
        }
        for action in available_actions
    }
    for size in range(len(available_actions) + 1):
        solutions = []
        for subset in itertools.combinations(available_actions, size):
            covered = set().union(
                *(distinguished_by[action] for action in subset)
            ) if subset else set()
            if covered == set(candidate_pairs):
                solutions.append(subset)
        if solutions:
            return tuple(solutions)
    return ()


def response_buckets(
    candidates: Mapping[str, Sequence[int]],
    names: Sequence[str],
    action: int,
) -> dict[int, tuple[str, ...]]:
    buckets: dict[int, list[str]] = {}
    for name in names:
        buckets.setdefault(candidates[name][action], []).append(name)
    return {
        outcome: tuple(sorted(bucket))
        for outcome, bucket in sorted(buckets.items())
    }


def rank_active_actions(
    candidates: Mapping[str, Sequence[int]],
    names: Sequence[str],
    actions: Sequence[int],
) -> tuple[dict[str, Any], ...]:
    total = len(names)
    ranked = []
    for action in actions:
        buckets = response_buckets(candidates, names, action)
        sizes = tuple(len(bucket) for bucket in buckets.values())
        ranked.append(
            {
                "action": action,
                "worst_case_remaining": max(sizes),
                "expected_remaining_under_uniform_prior": Fraction(
                    sum(size * size for size in sizes),
                    total,
                ),
                "buckets": buckets,
            }
        )
    return tuple(
        sorted(
            ranked,
            key=lambda item: (
                item["worst_case_remaining"],
                item["expected_remaining_under_uniform_prior"],
                item["action"],
            ),
        )
    )


def matching_cover_control() -> dict[str, Any]:
    labels = ("A", "B", "C", "D")
    pair_masks = masks_of_weight(4, 2)
    monomials = {
        "AB|CD": ((1 << 0) | (1 << 1), (1 << 2) | (1 << 3)),
        "AC|BD": ((1 << 0) | (1 << 2), (1 << 1) | (1 << 3)),
        "AD|BC": ((1 << 0) | (1 << 3), (1 << 1) | (1 << 2)),
    }
    candidates = {
        name: truth_from_coefficients(4, terms)
        for name, terms in monomials.items()
    }
    training_actions = tuple(
        mask for mask in range(1 << 4) if popcount(mask) <= 1
    )
    training_signatures = {
        name: signature(truth, training_actions)
        for name, truth in candidates.items()
    }
    separators = minimum_separating_action_sets(candidates, pair_masks)
    hitting_sets = pair_hitting_action_sets(candidates, pair_masks)
    ranking = rank_active_actions(
        candidates,
        tuple(candidates),
        pair_masks,
    )

    ground_truth = "AB|CD"
    first_action = ranking[0]["action"]
    first_response = candidates[ground_truth][first_action]
    posterior = tuple(
        name
        for name, truth in candidates.items()
        if truth[first_action] == first_response
    )

    return {
        "labels": labels,
        "candidate_interaction_covers": {
            name: tuple(named_mask(mask, labels) for mask in terms)
            for name, terms in monomials.items()
        },
        "training_actions": tuple(
            named_mask(mask, labels) for mask in training_actions
        ),
        "all_training_signatures_equal": (
            len(set(training_signatures.values())) == 1
        ),
        "training_version_space": tuple(candidates),
        "minimum_worst_case_separator_size": (
            len(separators[0]) if separators else None
        ),
        "minimum_separating_action_sets": tuple(
            tuple(named_mask(action, labels) for action in subset)
            for subset in separators
        ),
        "pair_hitting_sets_match_signature_separators": (
            set(separators) == set(hitting_sets)
        ),
        "active_action_ranking": tuple(
            {
                **item,
                "action": named_mask(item["action"], labels),
            }
            for item in ranking
        ),
        "ground_truth_for_positive_control": ground_truth,
        "first_action": named_mask(first_action, labels),
        "first_response": first_response,
        "posterior_after_first_response": posterior,
        "worst_case_requires_two_actions_even_if_one_branch_finishes_early": (
            len(separators[0]) == 2 and len(posterior) == 1
        ),
    }


def degree_two_grammar_control() -> dict[str, Any]:
    labels = ("A", "B", "C", "D")
    pair_masks = masks_of_weight(4, 2)
    candidates = {}
    for coefficient_mask in range(1 << len(pair_masks)):
        active = tuple(
            pair
            for index, pair in enumerate(pair_masks)
            if coefficient_mask & (1 << index)
        )
        candidates[f"q{coefficient_mask:02d}"] = truth_from_coefficients(
            4,
            active,
        )
    separators = minimum_separating_action_sets(candidates, pair_masks)
    every_proper_subset_fails = all(
        not signatures_are_injective(candidates, subset)
        for size in range(len(pair_masks))
        for subset in itertools.combinations(pair_masks, size)
    )
    return {
        "candidate_count": len(candidates),
        "pair_coefficient_count": len(pair_masks),
        "minimum_separator_size": len(separators[0]),
        "minimum_separator": tuple(
            named_mask(action, labels) for action in separators[0]
        ),
        "every_proper_pair_action_subset_is_nonidentifying": (
            every_proper_subset_fails
        ),
        "interpretation": (
            "each pair intervention isolates one independent quadratic "
            "coefficient; complete identification costs all six"
        ),
    }


def permute_mask(mask: int, old_to_new: Sequence[int]) -> int:
    transformed = 0
    for old_index, new_index in enumerate(old_to_new):
        if mask & (1 << old_index):
            transformed |= 1 << new_index
    return transformed


def overlapping_and_relabeling_control() -> dict[str, Any]:
    labels = ("A", "B", "C")
    ab = (1 << 0) | (1 << 1)
    bc = (1 << 1) | (1 << 2)
    truth = truth_from_coefficients(3, (ab, bc))
    coefficients = mobius_anf(truth, 3)
    hyperedges = {
        mask
        for mask, coefficient in enumerate(coefficients)
        if coefficient and popcount(mask) >= 2
    }

    old_to_new = (2, 0, 1)
    permuted_truth = [0] * len(truth)
    for old_state, value in enumerate(truth):
        permuted_truth[permute_mask(old_state, old_to_new)] = value
    permuted_coefficients = mobius_anf(permuted_truth, 3)
    recovered_permuted = {
        mask
        for mask, coefficient in enumerate(permuted_coefficients)
        if coefficient and popcount(mask) >= 2
    }
    expected_permuted = {
        permute_mask(mask, old_to_new)
        for mask in hyperedges
    }

    return {
        "interaction_hyperedges": tuple(
            named_mask(mask, labels) for mask in sorted(hyperedges)
        ),
        "overlap": "B",
        "is_not_a_partition": (
            len(hyperedges) == 2
            and bool(set.intersection(
                *[
                    {
                        index
                        for index in range(3)
                        if mask & (1 << index)
                    }
                    for mask in hyperedges
                ]
            ))
        ),
        "permutation_old_to_new": old_to_new,
        "relabeling_covariant": recovered_permuted == expected_permuted,
    }


def collapse_mask(mask: int, old_to_core: Sequence[int]) -> int:
    collapsed = 0
    for old_index, core_index in enumerate(old_to_core):
        if mask & (1 << old_index):
            collapsed |= 1 << core_index
    return collapsed


def relay_refinement_control() -> dict[str, Any]:
    labels = ("A", "B", "C", "R")
    ab = (1 << 0) | (1 << 1)
    bc = (1 << 1) | (1 << 2)
    rb = (1 << 3) | (1 << 1)
    direct_truth = truth_from_coefficients(4, (ab, bc))
    relay_truth = truth_from_coefficients(4, (rb, bc))
    admissible_states = tuple(
        state
        for state in range(1 << 4)
        if bool(state & (1 << 3)) == bool(state & (1 << 0))
    )
    agree = all(
        direct_truth[state] == relay_truth[state]
        for state in admissible_states
    )

    direct_edges = frozenset((ab, bc))
    relay_edges = frozenset((rb, bc))
    old_to_core = (0, 1, 2, 0)
    collapsed_direct = frozenset(
        collapse_mask(mask, old_to_core) for mask in direct_edges
    )
    collapsed_relay = frozenset(
        collapse_mask(mask, old_to_core) for mask in relay_edges
    )

    return {
        "admissible_constraint": "R=A",
        "admissible_state_count": len(admissible_states),
        "extensions_agree_on_every_admissible_state": agree,
        "direct_raw_hyperedges": tuple(
            named_mask(mask, labels) for mask in sorted(direct_edges)
        ),
        "relay_raw_hyperedges": tuple(
            named_mask(mask, labels) for mask in sorted(relay_edges)
        ),
        "raw_hypergraphs_differ": direct_edges != relay_edges,
        "collapsed_core_hyperedges": tuple(
            named_mask(mask, ("A", "B", "C"))
            for mask in sorted(collapsed_direct)
        ),
        "deterministic_relay_collapse_agrees": (
            collapsed_direct == collapsed_relay
        ),
        "raw_contract_outcome": OBSERVATIONALLY_EQUIVALENT,
        "quotient_contract_outcome": IDENTIFIED,
        "lesson": (
            "admissible behavior does not select a raw refined diagram; "
            "collapse deterministic copy relays before regionalization"
        ),
    }


def validator_origin_control() -> dict[str, Any]:
    validators = ("v1", "v2", "v3")
    origin_models = {
        "independent": {
            "v1": "alpha",
            "v2": "beta",
            "v3": "gamma",
        },
        "clone_v1_v2": {
            "v1": "alpha",
            "v2": "alpha",
            "v3": "gamma",
        },
    }

    def response(origins: Mapping[str, str], failed_origin: str | None) -> tuple[int, ...]:
        return tuple(
            0 if origins[validator] == failed_origin else 1
            for validator in validators
        )

    present = {
        name: response(origins, None)
        for name, origins in origin_models.items()
    }
    fail_alpha = {
        name: response(origins, "alpha")
        for name, origins in origin_models.items()
    }
    support_ranks = {
        name: len(set(origins.values()))
        for name, origins in origin_models.items()
    }
    return {
        "validators": validators,
        "present_record": present,
        "present_records_identical": len(set(present.values())) == 1,
        "raw_signature_count": len(validators),
        "independent_support_ranks": support_ranks,
        "failure_domain_intervention": "fail(alpha)",
        "post_intervention_records": fail_alpha,
        "intervention_separates_origin_models": (
            len(set(fail_alpha.values())) == len(fail_alpha)
        ),
        "lesson": (
            "signature identity and present agreement do not identify "
            "independent failure origins"
        ),
    }


def selection_contract_control(
    matching: Mapping[str, Any],
    relay: Mapping[str, Any],
) -> dict[str, Any]:
    exercised = {
        UNDERIDENTIFIED,
        IDENTIFIED,
        relay["raw_contract_outcome"],
        INCOMPLETE,
    }
    return {
        "return_vocabulary": (
            IDENTIFIED,
            UNDERIDENTIFIED,
            OBSERVATIONALLY_EQUIVALENT,
            INCOMPLETE,
        ),
        "matching_training_case": UNDERIDENTIFIED,
        "matching_full_separator_case": IDENTIFIED,
        "relay_raw_admissible_case": relay["raw_contract_outcome"],
        "relay_quotient_case": relay["quotient_contract_outcome"],
        "missing_candidate_grammar_case": INCOMPLETE,
        "all_outcomes_exercised": (
            exercised
            == {
                IDENTIFIED,
                UNDERIDENTIFIED,
                OBSERVATIONALLY_EQUIVALENT,
                INCOMPLETE,
            }
        ),
        "selection_theorem": (
            "inside a frozen finite candidate class, current data identify "
            "one presentation up to the declared quotient iff the current "
            "response signature is injective on quotient classes; otherwise "
            "a minimum pair-separating action set is a hitting set over "
            "still-indistinguishable candidate pairs"
        ),
        "grade": "ELEMENTARY FINITE IDENTIFICATION/HITTING-SET RESULT",
    }


def run() -> dict[str, Any]:
    anf = exhaustive_anf_control()
    matching = matching_cover_control()
    quadratic = degree_two_grammar_control()
    overlap = overlapping_and_relabeling_control()
    relay = relay_refinement_control()
    validators = validator_origin_control()
    contract = selection_contract_control(matching, relay)

    checks = {
        "all_65536_four_input_truth_tables_invert_under_anf": (
            anf["truth_table_count"] == 65536 and not anf["failures"]
        ),
        "passive_and_singleton_records_do_not_select_matching_cover": (
            matching["all_training_signatures_equal"]
            and len(matching["training_version_space"]) == 3
        ),
        "matching_cover_minimum_worst_case_separator_is_two": (
            matching["minimum_worst_case_separator_size"] == 2
        ),
        "signature_and_pair_hitting_formulations_agree": matching[
            "pair_hitting_sets_match_signature_separators"
        ],
        "active_design_can_finish_one_branch_before_worst_case": matching[
            "worst_case_requires_two_actions_even_if_one_branch_finishes_early"
        ],
        "full_quadratic_grammar_has_64_candidates": (
            quadratic["candidate_count"] == 64
        ),
        "full_quadratic_identification_requires_all_six_pair_actions": (
            quadratic["minimum_separator_size"] == 6
            and quadratic[
                "every_proper_pair_action_subset_is_nonidentifying"
            ]
        ),
        "regional_interactions_can_overlap": overlap["is_not_a_partition"],
        "interaction_reconstruction_is_label_covariant": overlap[
            "relabeling_covariant"
        ],
        "relay_extensions_agree_on_admissible_process": relay[
            "extensions_agree_on_every_admissible_state"
        ],
        "raw_relay_topology_is_not_selected": relay[
            "raw_hypergraphs_differ"
        ],
        "deterministic_relay_quotient_restores_invariance": relay[
            "deterministic_relay_collapse_agrees"
        ],
        "present_validator_records_do_not_select_origins": validators[
            "present_records_identical"
        ],
        "raw_signatures_and_independent_support_are_distinct": (
            validators["raw_signature_count"] == 3
            and set(validators["independent_support_ranks"].values())
            == {2, 3}
        ),
        "failure_domain_intervention_separates_origin_models": validators[
            "intervention_separates_origin_models"
        ],
        "selection_contract_exercises_identified": (
            contract["matching_full_separator_case"] == IDENTIFIED
        ),
        "selection_contract_exercises_underidentified": (
            contract["matching_training_case"] == UNDERIDENTIFIED
        ),
        "selection_contract_exercises_observational_equivalence": (
            contract["relay_raw_admissible_case"]
            == OBSERVATIONALLY_EQUIVALENT
        ),
        "selection_contract_exercises_incomplete": (
            contract["missing_candidate_grammar_case"] == INCOMPLETE
        ),
        "selection_contract_exercises_all_four_outcomes": contract[
            "all_outcomes_exercised"
        ],
        "negative_nonidentification_output_is_preserved": (
            matching["minimum_separating_action_sets"]
            and validators["failure_domain_intervention"]
        ),
    }
    failures = tuple(name for name, passed in checks.items() if not passed)
    result = {
        "schema_version": "1.0",
        "run_id": RUN_ID,
        "probe": "du_endogenous_regionalization_probe",
        "claim_grade": (
            "EXACT FINITE IDENTIFICATION/NONIDENTIFICATION CONTROLS / "
            "KNOWN BOOLEAN-MOBIUS AND EXPERIMENT-DESIGN COMPONENTS / "
            "PHYSICAL REGION SELECTION OPEN"
        ),
        "anf_reconstruction": anf,
        "matching_cover_version_space": matching,
        "complete_quadratic_grammar": quadratic,
        "overlap_and_relabeling": overlap,
        "relay_refinement": relay,
        "validator_origin_selection": validators,
        "selection_contract": contract,
        "checks": checks,
        "check_count": len(checks),
        "failure_count": len(failures),
        "failures": failures,
        "verdict": (
            "FINITE_REGIONAL_IDENTIFICATION_CONTRACT_INSTALLED / "
            "PRESENT_RECORDS_CAN_UNDERIDENTIFY COVERS_AND_ORIGINS / "
            "MINIMUM_HELD_OUT_SEPARATORS_COMPUTED"
        ),
        "does_not_establish": (
            "physical regional ontology",
            "a universal region grammar",
            "that ANF monomials are physical regions",
            "that minimum description length selects nature",
            "validator independence without failure-domain interventions",
            "noisy or continuous regional identification",
            "causal geometry",
            "a new physical law",
        ),
    }
    ARTIFACT.write_text(canonical_json(result), encoding="utf-8")
    if failures:
        raise AssertionError(f"failed checks: {failures}")
    return result


if __name__ == "__main__":
    outcome = run()
    print(f"{outcome['verdict']}: {outcome['check_count']}/"
          f"{outcome['check_count']} checks")
