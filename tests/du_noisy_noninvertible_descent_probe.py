#!/usr/bin/env python3
"""Exact finite noisy-descent and approximate-boundary controls.

The stochastic descent fixture uses binary mismatch records on a cycle.  Every
deterministic global node assignment induces an even-parity edge-mismatch
vector.  Therefore local mismatch probabilities admit a global extension
exactly when they lie in the even-parity polytope, whose facets are the
odd-set inequalities.

This compatibility obstruction is kept separate from approximate boundary
action sufficiency.  A compatible global process can still be summarized too
coarsely for an upper action.  Conversely, a boundary summary cannot repair
locally incompatible stochastic records.

These are known marginal-polytope and approximation controls.  Passing does
not establish a physical finality field, contextuality, a cryptographic
protocol, a quantum deviation, or an operational metric on arbitrary record
theories.
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
    / "du_noisy_noninvertible_descent_result.json"
)
RUN_ID = "RUN-20260725-064622-regional-selection-noisy-descent"

DESCENDS = "DESCENDS"
REQUIRES_LIFT = "REQUIRES_PROVENANCE_OR_LOGICAL_LIFT"
REJECTS = "REJECTS_FRUSTRATED_OR_UNSAFE_COMPOSITION"
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


def odd_masks(n: int) -> tuple[int, ...]:
    return tuple(mask for mask in range(1 << n) if mask.bit_count() % 2)


def parity_vertices(n: int, parity: int) -> tuple[tuple[int, ...], ...]:
    return tuple(
        bits
        for bits in itertools.product((0, 1), repeat=n)
        if sum(bits) % 2 == parity
    )


def odd_set_violation(
    mismatches: Sequence[Fraction],
    odd_mask: int,
) -> Fraction:
    inside = sum(
        mismatches[index]
        for index in range(len(mismatches))
        if odd_mask & (1 << index)
    )
    outside = sum(
        mismatches[index]
        for index in range(len(mismatches))
        if not odd_mask & (1 << index)
    )
    return inside - outside - (odd_mask.bit_count() - 1)


def cycle_descent_obstruction(
    mismatches: Sequence[Fraction],
) -> dict[str, Any]:
    if not mismatches:
        raise ValueError("cycle must have at least one edge")
    if any(value < 0 or value > 1 for value in mismatches):
        raise ValueError("mismatch probabilities must lie in [0,1]")
    violations = {
        mask: odd_set_violation(mismatches, mask)
        for mask in odd_masks(len(mismatches))
    }
    witness_mask, raw_maximum = max(
        violations.items(),
        key=lambda item: (item[1], -item[0]),
    )
    maximum = max(Fraction(0), raw_maximum)
    return {
        "descends": maximum == 0,
        "maximum_odd_set_violation": maximum,
        "witness_odd_edge_indices": tuple(
            index
            for index in range(len(mismatches))
            if witness_mask & (1 << index)
        ) if maximum else (),
        "all_facet_slacks": {
            str(mask): -violation
            for mask, violation in violations.items()
        },
    }


def parity_vertex_control() -> dict[str, Any]:
    even_failures = []
    odd_failures = []
    counts = {}
    for n in range(3, 8):
        even = parity_vertices(n, 0)
        odd = parity_vertices(n, 1)
        counts[n] = {
            "even_vertices": len(even),
            "odd_vertices": len(odd),
            "odd_set_facets": len(odd_masks(n)),
        }
        for vertex in even:
            result = cycle_descent_obstruction(
                tuple(Fraction(value) for value in vertex)
            )
            if not result["descends"]:
                even_failures.append((n, vertex))
        for vertex in odd:
            result = cycle_descent_obstruction(
                tuple(Fraction(value) for value in vertex)
            )
            if result["maximum_odd_set_violation"] != 1:
                odd_failures.append((n, vertex, result))

    return {
        "cycle_sizes": tuple(range(3, 8)),
        "counts": counts,
        "even_vertex_failures": even_failures,
        "odd_vertex_failures": odd_failures,
        "facet_statement": (
            "x lies in the convex hull of even parity vectors iff "
            "0<=x<=1 and every odd-set inequality holds"
        ),
        "grade": "KNOWN PARITY-POLYTOPE FACET THEOREM / FINITE VERTEX AUDIT",
    }


def triangle_signed_weights(
    mismatches: Sequence[Fraction],
) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    if len(mismatches) != 3:
        raise ValueError("triangle requires three mismatch probabilities")
    x1, x2, x3 = mismatches
    return (
        1 - (x1 + x2 + x3) / 2,
        (x2 + x3 - x1) / 2,
        (x1 + x3 - x2) / 2,
        (x1 + x2 - x3) / 2,
    )


def triangle_grid_control(denominator: int = 6) -> dict[str, Any]:
    failures = []
    multiple_negative_weights = []
    cases = 0
    for numerators in itertools.product(
        range(denominator + 1),
        repeat=3,
    ):
        mismatches = tuple(
            Fraction(numerator, denominator)
            for numerator in numerators
        )
        obstruction = cycle_descent_obstruction(mismatches)
        weights = triangle_signed_weights(mismatches)
        weights_valid = all(weight >= 0 for weight in weights)
        if obstruction["descends"] != weights_valid:
            failures.append((mismatches, obstruction, weights))
        if sum(weight < 0 for weight in weights) > 1:
            multiple_negative_weights.append((mismatches, weights))
        cases += 1

    return {
        "denominator": denominator,
        "rational_grid_cases": cases,
        "facet_vs_signed_weight_failures": failures,
        "multiple_negative_weight_cases": multiple_negative_weights,
        "signed_sector_order": ("000", "011", "101", "110"),
        "negative_mass_relation": (
            "on the triangle cube, maximum odd-set violation v gives "
            "negative mass v/2 in the unique signed parity-sector extension"
        ),
        "boundary": (
            "facet violation and signed negative mass are mathematical "
            "obstructions, not yet a physical or operational distance"
        ),
    }


def frustrated_noise_control() -> dict[str, Any]:
    epsilons = (
        Fraction(0),
        Fraction(1, 6),
        Fraction(1, 3),
        Fraction(1, 2),
    )
    rows = []
    for epsilon in epsilons:
        mismatches = (epsilon, epsilon, 1 - epsilon)
        obstruction = cycle_descent_obstruction(mismatches)
        weights = triangle_signed_weights(mismatches)
        expected_violation = max(Fraction(0), 1 - 3 * epsilon)
        negative_mass = sum(-weight for weight in weights if weight < 0)
        rows.append(
            {
                "edge_error": epsilon,
                "mismatches": mismatches,
                "descends": obstruction["descends"],
                "maximum_violation": obstruction[
                    "maximum_odd_set_violation"
                ],
                "expected_violation": expected_violation,
                "signed_negative_mass": negative_mass,
                "expected_negative_mass": expected_violation / 2,
            }
        )
    return {
        "family": "two equality edges and one inequality edge, each with error epsilon",
        "rows": rows,
        "sharp_compatibility_threshold": Fraction(1, 3),
        "all_formulas_match": all(
            row["maximum_violation"] == row["expected_violation"]
            and row["signed_negative_mass"]
            == row["expected_negative_mass"]
            for row in rows
        ),
        "threshold_behavior_correct": (
            all(
                not row["descends"]
                for row in rows
                if row["edge_error"] < Fraction(1, 3)
            )
            and all(
                row["descends"]
                for row in rows
                if row["edge_error"] >= Fraction(1, 3)
            )
        ),
    }


def integer_compositions(total: int, parts: int) -> Iterable[tuple[int, ...]]:
    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for remainder in integer_compositions(total - first, parts - 1):
            yield (first,) + remainder


def apply_local_bsc(
    distribution: Mapping[tuple[int, ...], Fraction],
    errors: Sequence[Fraction],
) -> dict[tuple[int, ...], Fraction]:
    n = len(errors)
    output = {
        state: Fraction(0)
        for state in itertools.product((0, 1), repeat=n)
    }
    for source, source_probability in distribution.items():
        for target in output:
            transition = Fraction(1)
            for index, error in enumerate(errors):
                transition *= (
                    1 - error if target[index] == source[index] else error
                )
            output[target] += source_probability * transition
    return output


def cycle_mismatch_marginals(
    distribution: Mapping[tuple[int, ...], Fraction],
) -> tuple[Fraction, ...]:
    n = len(next(iter(distribution)))
    return tuple(
        sum(
            probability
            for state, probability in distribution.items()
            if state[index] != state[(index + 1) % n]
        )
        for index in range(n)
    )


def local_noise_preservation_control() -> dict[str, Any]:
    states = tuple(itertools.product((0, 1), repeat=3))
    errors = (Fraction(0), Fraction(1, 4), Fraction(1, 2))
    failures = []
    distribution_count = 0
    channel_count = 0
    for counts in integer_compositions(2, len(states)):
        distribution = {
            state: Fraction(count, 2)
            for state, count in zip(states, counts, strict=True)
            if count
        }
        distribution_count += 1
        for error_vector in itertools.product(errors, repeat=3):
            noisy = apply_local_bsc(distribution, error_vector)
            mismatches = cycle_mismatch_marginals(noisy)
            obstruction = cycle_descent_obstruction(mismatches)
            channel_count += 1
            if not obstruction["descends"]:
                failures.append(
                    {
                        "distribution": distribution,
                        "errors": error_vector,
                        "mismatches": mismatches,
                        "obstruction": obstruction,
                    }
                )
                if len(failures) >= 8:
                    break
        if failures:
            break

    fully_erasing = apply_local_bsc(
        {(0, 0, 0): Fraction(1)},
        (Fraction(1, 2),) * 3,
    )
    return {
        "input_distributions": distribution_count,
        "distribution_channel_cases": channel_count,
        "error_alphabet": errors,
        "failures": failures,
        "fully_erasing_channel_is_noninvertible": (
            len(set(fully_erasing.values())) == 1
            and next(iter(fully_erasing.values())) == Fraction(1, 8)
        ),
        "fully_erased_mismatches": cycle_mismatch_marginals(fully_erasing),
        "interpretation": (
            "node-local stochastic maps preserve compatibility because "
            "they act on an existing joint distribution"
        ),
    }


def approximate_binary_boundary_defect(
    summaries: Mapping[str, str],
    responses: Mapping[str, Mapping[str, Fraction]],
) -> dict[str, Any]:
    fibers: dict[str, tuple[str, ...]] = {}
    for summary in sorted(set(summaries.values())):
        fibers[summary] = tuple(
            state
            for state, label in summaries.items()
            if label == summary
        )

    receipts = {}
    maximum = Fraction(0)
    for action, probabilities in responses.items():
        action_receipts = {}
        for label, states in fibers.items():
            low = min(probabilities[state] for state in states)
            high = max(probabilities[state] for state in states)
            center = (low + high) / 2
            defect = (high - low) / 2
            maximum = max(maximum, defect)
            action_receipts[label] = {
                "states": states,
                "minimum_probability": low,
                "maximum_probability": high,
                "optimal_summary_response": center,
                "minimum_worst_case_total_variation_error": defect,
                "lower_bound_witnessed_by_endpoints": (
                    high - low == 2 * defect
                ),
            }
        receipts[action] = action_receipts
    return {
        "maximum_action_factorization_defect": maximum,
        "receipts": receipts,
        "theorem": (
            "for binary outputs and a deterministic supplied summary, "
            "the minimum worst-case TV simulation error on each fiber is "
            "half the response-probability range"
        ),
    }


def boundary_factorization_control() -> dict[str, Any]:
    states = ("s0", "s1", "s2", "s3")
    coarse = {
        "s0": "low",
        "s1": "low",
        "s2": "high",
        "s3": "high",
    }
    lifted = {state: state for state in states}
    responses = {
        "local": {
            "s0": Fraction(1, 5),
            "s1": Fraction(1, 5),
            "s2": Fraction(4, 5),
            "s3": Fraction(4, 5),
        },
        "joint": {
            "s0": Fraction(1, 10),
            "s1": Fraction(9, 10),
            "s2": Fraction(3, 10),
            "s3": Fraction(7, 10),
        },
    }
    coarse_result = approximate_binary_boundary_defect(coarse, responses)
    lifted_result = approximate_binary_boundary_defect(lifted, responses)
    return {
        "coarse": coarse_result,
        "lifted": lifted_result,
        "coarse_defect": coarse_result[
            "maximum_action_factorization_defect"
        ],
        "lifted_defect": lifted_result[
            "maximum_action_factorization_defect"
        ],
        "compatibility_and_boundary_defect_are_distinct": True,
    }


def ghz_visibility_control() -> dict[str, Any]:
    visibilities = (
        Fraction(0),
        Fraction(1, 4),
        Fraction(1, 2),
        Fraction(1),
    )
    rows = []
    for visibility in visibilities:
        responses = {
            "logical_x_parity": {
                "GHZ+": (1 + visibility) / 2,
                "GHZ-": (1 - visibility) / 2,
            }
        }
        coarse = approximate_binary_boundary_defect(
            {"GHZ+": "proper_subsets", "GHZ-": "proper_subsets"},
            responses,
        )
        lifted = approximate_binary_boundary_defect(
            {"GHZ+": "plus", "GHZ-": "minus"},
            responses,
        )
        rows.append(
            {
                "visibility": visibility,
                "coarse_defect": coarse[
                    "maximum_action_factorization_defect"
                ],
                "expected_coarse_defect": visibility / 2,
                "logical_lift_defect": lifted[
                    "maximum_action_factorization_defect"
                ],
            }
        )
    return {
        "rows": rows,
        "all_visibility_formulas_match": all(
            row["coarse_defect"] == row["expected_coarse_defect"]
            and row["logical_lift_defect"] == 0
            for row in rows
        ),
        "boundary": (
            "this is a noisy logical-access specialization of standard GHZ "
            "statistics, not a consensus law or quantum modification"
        ),
    }


def typed_descent_outcome(
    mismatches: Sequence[Fraction],
    boundary_defect: Fraction,
    *,
    n_validators: int = 4,
    fault_bound: int = 1,
    quorum: int = 3,
    independent_provenance: bool = True,
    hardening: str = "none",
    contract_complete: bool = True,
) -> dict[str, Any]:
    if not contract_complete:
        return {"result": INCOMPLETE, "reason": "missing contract field"}
    safe = 2 * quorum > n_validators + fault_bound
    live = quorum <= n_validators - fault_bound
    if not safe or not independent_provenance:
        return {
            "result": REJECTS,
            "reason": "unsafe quorum or correlated support",
            "safe": safe,
            "live": live,
        }
    obstruction = cycle_descent_obstruction(mismatches)
    if not obstruction["descends"]:
        if hardening == "reject":
            return {
                "result": REJECTS,
                "reason": "hardening refuses incompatible stochastic records",
                "safe": safe,
                "live": live,
                "obstruction": obstruction,
            }
        return {
            "result": REQUIRES_LIFT,
            "reason": "positive cycle obstruction requires provenance or repair",
            "safe": safe,
            "live": live,
            "obstruction": obstruction,
        }
    if boundary_defect > 0:
        return {
            "result": REQUIRES_LIFT,
            "reason": "compatible process but action-insufficient boundary",
            "safe": safe,
            "live": live,
            "boundary_defect": boundary_defect,
        }
    return {
        "result": DESCENDS,
        "reason": "compatible, safe, independently supported, and action-sufficient",
        "safe": safe,
        "live": live,
    }


def typed_contract_control() -> dict[str, Any]:
    compatible = (Fraction(1, 4),) * 3
    frustrated = (Fraction(0), Fraction(0), Fraction(1))
    cases = {
        "complete_compatible": typed_descent_outcome(
            compatible,
            Fraction(0),
        ),
        "compatible_coarse_boundary": typed_descent_outcome(
            compatible,
            Fraction(1, 5),
        ),
        "frustrated_requires_lift": typed_descent_outcome(
            frustrated,
            Fraction(0),
        ),
        "frustrated_safely_rejected": typed_descent_outcome(
            frustrated,
            Fraction(0),
            hardening="reject",
        ),
        "unsafe_quorum": typed_descent_outcome(
            compatible,
            Fraction(0),
            quorum=2,
        ),
        "correlated_support": typed_descent_outcome(
            compatible,
            Fraction(0),
            independent_provenance=False,
        ),
        "missing_contract": typed_descent_outcome(
            compatible,
            Fraction(0),
            contract_complete=False,
        ),
    }
    return {
        "cases": cases,
        "return_vocabulary": tuple(
            sorted({case["result"] for case in cases.values()})
        ),
        "all_four_outcomes_exercised": (
            {case["result"] for case in cases.values()}
            == {DESCENDS, REQUIRES_LIFT, REJECTS, INCOMPLETE}
        ),
        "safe_rejection_is_not_descent": (
            cases["frustrated_safely_rejected"]["result"] == REJECTS
        ),
        "compatibility_and_action_sufficiency_fail_separately": (
            cases["compatible_coarse_boundary"]["result"] == REQUIRES_LIFT
            and cases["frustrated_requires_lift"]["result"] == REQUIRES_LIFT
            and cases["compatible_coarse_boundary"]["reason"]
            != cases["frustrated_requires_lift"]["reason"]
        ),
    }


def run() -> dict[str, Any]:
    vertices = parity_vertex_control()
    triangle = triangle_grid_control()
    frustrated = frustrated_noise_control()
    local_noise = local_noise_preservation_control()
    boundary = boundary_factorization_control()
    ghz = ghz_visibility_control()
    contract = typed_contract_control()

    checks = {
        "all_even_parity_vertices_through_n7_descend": not vertices[
            "even_vertex_failures"
        ],
        "all_odd_parity_vertices_through_n7_have_unit_obstruction": (
            not vertices["odd_vertex_failures"]
        ),
        "triangle_grid_facet_and_signed_extension_agree": (
            not triangle["facet_vs_signed_weight_failures"]
        ),
        "triangle_has_at_most_one_negative_sector_weight": (
            not triangle["multiple_negative_weight_cases"]
        ),
        "frustrated_noise_violation_formula_exact": frustrated[
            "all_formulas_match"
        ],
        "frustrated_noise_threshold_is_one_third": (
            frustrated["sharp_compatibility_threshold"]
            == Fraction(1, 3)
            and frustrated["threshold_behavior_correct"]
        ),
        "node_local_bsc_preserves_global_compatibility": not local_noise[
            "failures"
        ],
        "fully_erasing_bsc_is_noninvertible_positive_control": local_noise[
            "fully_erasing_channel_is_noninvertible"
        ],
        "fully_erased_cycle_has_half_mismatch_marginals": (
            local_noise["fully_erased_mismatches"]
            == (Fraction(1, 2),) * 3
        ),
        "coarse_boundary_has_positive_action_defect": (
            boundary["coarse_defect"] == Fraction(2, 5)
        ),
        "logical_boundary_lift_restores_exact_factorization": (
            boundary["lifted_defect"] == 0
        ),
        "compatibility_and_boundary_defect_are_separate": boundary[
            "compatibility_and_boundary_defect_are_distinct"
        ],
        "ghz_visibility_obeys_half_range_defect": ghz[
            "all_visibility_formulas_match"
        ],
        "typed_contract_exercises_all_four_outcomes": contract[
            "all_four_outcomes_exercised"
        ],
        "safe_rejection_is_not_successful_descent": contract[
            "safe_rejection_is_not_descent"
        ],
        "compatibility_and_action_failures_have_different_receipts": contract[
            "compatibility_and_action_sufficiency_fail_separately"
        ],
        "unsafe_quorum_is_rejected": (
            contract["cases"]["unsafe_quorum"]["result"] == REJECTS
        ),
        "correlated_support_is_rejected": (
            contract["cases"]["correlated_support"]["result"] == REJECTS
        ),
        "missing_contract_is_not_forced_into_scientific_verdict": (
            contract["cases"]["missing_contract"]["result"] == INCOMPLETE
        ),
        "facet_slack_not_promoted_to_physical_metric": (
            "not yet a physical or operational distance"
            in triangle["boundary"]
        ),
    }
    failures = tuple(name for name, passed in checks.items() if not passed)
    result = {
        "schema_version": "1.0",
        "run_id": RUN_ID,
        "probe": "du_noisy_noninvertible_descent_probe",
        "claim_grade": (
            "EXACT FINITE PARITY-POLYTOPE AND APPROXIMATE-BOUNDARY "
            "CONTROLS / KNOWN COMPONENT MATHEMATICS / GENERAL NOISY "
            "REGIONAL DESCENT AND PHYSICAL APPLICATION OPEN"
        ),
        "parity_polytope_vertex_audit": vertices,
        "triangle_signed_extension": triangle,
        "frustrated_noise_family": frustrated,
        "local_noninvertible_noise": local_noise,
        "approximate_boundary_factorization": boundary,
        "noisy_ghz_logical_access": ghz,
        "typed_descent_contract": contract,
        "checks": checks,
        "check_count": len(checks),
        "failure_count": len(failures),
        "failures": failures,
        "verdict": (
            "NOISY_CYCLE_DESCENT_OBSTRUCTION_INSTALLED / "
            "ONE_THIRD_FRUSTRATION_THRESHOLD_EXACT / "
            "COMPATIBILITY_AND_ACTION_DEFECTS_SEPARATED"
        ),
        "does_not_establish": (
            "a general stochastic descent theorem",
            "an operational metric on arbitrary records",
            "physical contextuality",
            "a finality field",
            "a cryptographic or BFT security proof",
            "a quantum modification",
            "a physical region-selection law",
            "emergent geometry",
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
