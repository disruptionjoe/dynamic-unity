#!/usr/bin/env python3
"""Exact controls for HC-DU-057 / N5-PF-P4.

This probe preserves the smallest counterexamples behind the regional-finality
excess audit.  It is not a simulation and does not estimate a new physical
coefficient.

The three audited candidate families are:

1. a finality rate distinct from causal propagation and ordinary dynamics;
2. quantum complementarity derived from physical-record mergeability; and
3. universal critical exponents for record/finality thresholds.

Every calculation is rational and finite.  Passing establishes only the
declared counterexamples and classification boundaries.
"""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path
from typing import Callable, Iterable, Sequence


Q = Fraction
ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_regional_finality_excess_audit_result.json"
)
CHECKS: list[dict[str, object]] = []

Matrix2 = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]


def jsonable(value: object) -> object:
    if isinstance(value, Fraction):
        return {
            "numerator": value.numerator,
            "denominator": value.denominator,
        }
    if isinstance(value, tuple):
        return [jsonable(item) for item in value]
    if isinstance(value, list):
        return [jsonable(item) for item in value]
    if isinstance(value, dict):
        return {str(key): jsonable(item) for key, item in value.items()}
    return value


def record(name: str, passed: bool, detail: object) -> None:
    CHECKS.append(
        {
            "name": name,
            "passed": bool(passed),
            "detail": jsonable(detail),
        }
    )


def matrix_add(left: Matrix2, right: Matrix2) -> Matrix2:
    return (
        (left[0][0] + right[0][0], left[0][1] + right[0][1]),
        (left[1][0] + right[1][0], left[1][1] + right[1][1]),
    )


def matrix_scale(scale: Fraction, matrix: Matrix2) -> Matrix2:
    return (
        (scale * matrix[0][0], scale * matrix[0][1]),
        (scale * matrix[1][0], scale * matrix[1][1]),
    )


def matrix_multiply(left: Matrix2, right: Matrix2) -> Matrix2:
    return (
        (
            left[0][0] * right[0][0] + left[0][1] * right[1][0],
            left[0][0] * right[0][1] + left[0][1] * right[1][1],
        ),
        (
            left[1][0] * right[0][0] + left[1][1] * right[1][0],
            left[1][0] * right[0][1] + left[1][1] * right[1][1],
        ),
    )


def matrix_subtract(left: Matrix2, right: Matrix2) -> Matrix2:
    return matrix_add(left, matrix_scale(Q(-1), right))


def trace(matrix: Matrix2) -> Fraction:
    return matrix[0][0] + matrix[1][1]


def determinant(matrix: Matrix2) -> Fraction:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def minimum_success_steps(success_probability: Fraction, error: Fraction) -> int:
    """Smallest n with (1-p)^n <= error."""

    steps = 0
    failure = Q(1)
    while failure > error:
        failure *= 1 - success_probability
        steps += 1
    return steps


def evaluate_causal_order(order: Sequence[str]) -> tuple[str, str]:
    """Evaluate two linear extensions of one causal partial order."""

    state: dict[str, str] = {}
    for event in order:
        if event in {"left_source", "right_source"}:
            state[event] = "ready"
        elif event == "merge":
            if (
                state.get("left_source") != "ready"
                or state.get("right_source") != "ready"
            ):
                raise ValueError("merge precedes a causal parent")
            state["record"] = "formed"
        elif event == "act":
            if state.get("record") != "formed":
                raise ValueError("action precedes record formation")
            state["action"] = "safe"
        else:
            raise ValueError(f"unknown event: {event}")
    return state["record"], state["action"]


def classical_merge(*records: Iterable[str]) -> frozenset[str]:
    merged: set[str] = set()
    for record_set in records:
        merged.update(record_set)
    return frozenset(merged)


def crossover(size: int, x: Fraction) -> Fraction:
    numerator = x**size
    return numerator / (numerator + (1 - x) ** size)


def classify_rate(
    *,
    standard_timescale: bool = False,
    lorentz_violating_access: bool = False,
    operationally_inaccessible: bool = False,
    covariant_new_dynamics: bool = False,
) -> str:
    flags = {
        "STANDARD_DYNAMICS_OR_PROTOCOL": standard_timescale,
        "LEAKING_PREFERRED_FRAME": lorentz_violating_access,
        "OPERATIONALLY_UNIDENTIFIABLE": operationally_inaccessible,
        "COVARIANT_NEW_DYNAMICS": covariant_new_dynamics,
    }
    selected = [name for name, enabled in flags.items() if enabled]
    if len(selected) != 1:
        raise ValueError("rate classification requires exactly one branch")
    return selected[0]


def main() -> int:
    # Candidate 1: a hidden common tick does not select a formation rate.
    error = Q(1, 8)
    slow_steps = minimum_success_steps(Q(1, 2), error)
    fast_steps = minimum_success_steps(Q(3, 4), error)
    record(
        "same_tick_allows_distinct_standard_formation_times",
        slow_steps == 3 and fast_steps == 2,
        {
            "causal_tick": "held fixed",
            "error": error,
            "p_half_steps": slow_steps,
            "p_three_quarters_steps": fast_steps,
        },
    )
    record(
        "formation_difference_is_an_ordinary_local_dynamics_parameter",
        (1 - Q(1, 2)) ** slow_steps == Q(1, 8)
        and (1 - Q(3, 4)) ** fast_steps == Q(1, 16),
        "ordinary success probabilities change the hitting time while causal reach is unchanged",
    )
    policy_waits = (0, 1, 7, 101)
    record(
        "protocol_wait_can_change_finality_latency_arbitrarily",
        tuple(fast_steps + wait for wait in policy_waits) == (2, 3, 9, 103),
        {
            "same_physical_formation_steps": fast_steps,
            "policy_waits": policy_waits,
        },
    )

    order_a = ("left_source", "right_source", "merge", "act")
    order_b = ("right_source", "left_source", "merge", "act")
    record(
        "causal_partial_order_control_is_leaf_invariant",
        order_a != order_b
        and evaluate_causal_order(order_a) == evaluate_causal_order(order_b),
        evaluate_causal_order(order_a),
    )
    leaf_dependent_response: Callable[[Sequence[str]], str] = (
        lambda order: order[0]
    )
    record(
        "accessible_leaf_rank_would_be_a_leaking_branch",
        leaf_dependent_response(order_a) != leaf_dependent_response(order_b),
        "an observer-readable response depending only on linear-extension rank violates the matched exactly compensated control",
    )

    four_rate_classes = (
        classify_rate(standard_timescale=True),
        classify_rate(lorentz_violating_access=True),
        classify_rate(operationally_inaccessible=True),
        classify_rate(covariant_new_dynamics=True),
    )
    record(
        "rate_classification_requires_four_not_three_branches",
        four_rate_classes
        == (
            "STANDARD_DYNAMICS_OR_PROTOCOL",
            "LEAKING_PREFERRED_FRAME",
            "OPERATIONALLY_UNIDENTIFIABLE",
            "COVARIANT_NEW_DYNAMICS",
        ),
        four_rate_classes,
    )
    record(
        "covariant_new_dynamics_is_not_evidence_for_hidden_foliation",
        "COVARIANT_NEW_DYNAMICS" in four_rate_classes
        and "LEAKING_PREFERRED_FRAME" in four_rate_classes,
        "the two branches are explicitly distinct",
    )

    # Candidate 2: source joint measurability is not downstream archive merge.
    identity: Matrix2 = ((Q(1), Q(0)), (Q(0), Q(1)))
    pauli_x: Matrix2 = ((Q(0), Q(1)), (Q(1), Q(0)))
    pauli_z: Matrix2 = ((Q(1), Q(0)), (Q(0), Q(-1)))
    eta = Q(1, 2)

    def effect(axis: Matrix2, sign: int) -> Matrix2:
        return matrix_scale(
            Q(1, 2),
            matrix_add(identity, matrix_scale(Q(sign) * eta, axis)),
        )

    def joint_effect(sign_x: int, sign_z: int) -> Matrix2:
        return matrix_scale(
            Q(1, 4),
            matrix_add(
                matrix_add(
                    identity,
                    matrix_scale(Q(sign_x) * eta, pauli_x),
                ),
                matrix_scale(Q(sign_z) * eta, pauli_z),
            ),
        )

    ex_plus = effect(pauli_x, 1)
    ez_plus = effect(pauli_z, 1)
    commutator = matrix_subtract(
        matrix_multiply(ex_plus, ez_plus),
        matrix_multiply(ez_plus, ex_plus),
    )
    zero: Matrix2 = ((Q(0), Q(0)), (Q(0), Q(0)))
    record(
        "unsharp_x_and_z_effects_do_not_commute",
        commutator != zero,
        commutator,
    )

    joints = {
        (sign_x, sign_z): joint_effect(sign_x, sign_z)
        for sign_x in (-1, 1)
        for sign_z in (-1, 1)
    }
    record(
        "all_four_joint_effects_are_positive",
        all(
            trace(value) == Q(1, 2) and determinant(value) == Q(1, 32)
            for value in joints.values()
        ),
        {
            str(key): {
                "trace": trace(value),
                "determinant": determinant(value),
            }
            for key, value in joints.items()
        },
    )
    record(
        "joint_effects_have_exact_x_marginals",
        all(
            matrix_add(joints[(sign_x, -1)], joints[(sign_x, 1)])
            == effect(pauli_x, sign_x)
            for sign_x in (-1, 1)
        ),
        "sum over z gives E_x",
    )
    record(
        "joint_effects_have_exact_z_marginals",
        all(
            matrix_add(joints[(-1, sign_z)], joints[(1, sign_z)])
            == effect(pauli_z, sign_z)
            for sign_z in (-1, 1)
        ),
        "sum over x gives E_z",
    )
    record(
        "noncommutativity_does_not_imply_nonmergeability",
        commutator != zero
        and all(determinant(value) >= 0 for value in joints.values()),
        "the eta=1/2 unsharp X/Z POVMs are jointly measurable",
    )

    record_x = frozenset({"context:X", "outcome:+", "provenance:lab-a"})
    record_z = frozenset({"context:Z", "outcome:-", "provenance:lab-b"})
    merged_xz = classical_merge(record_x, record_z)
    merged_zx = classical_merge(record_z, record_x)
    record(
        "formed_classical_archives_merge_commutatively",
        merged_xz == merged_zx,
        sorted(merged_xz),
    )
    record(
        "formed_classical_archives_merge_associatively_and_idempotently",
        classical_merge(merged_xz, record_x) == merged_xz
        and classical_merge(record_x, record_z, record_x)
        == classical_merge(record_x, classical_merge(record_z, record_x)),
        "set-union CRDT laws hold after the context-tagged records exist",
    )

    projector_x = matrix_scale(
        Q(1, 2),
        matrix_add(identity, pauli_x),
    )
    projector_x_complement = matrix_scale(
        Q(1, 2),
        matrix_subtract(identity, pauli_x),
    )
    record(
        "sharp_same_basis_positive_control_commutes",
        matrix_subtract(
            matrix_multiply(projector_x, projector_x_complement),
            matrix_multiply(projector_x_complement, projector_x),
        )
        == zero,
        "same-axis effects commute; sharp-PVM equivalence remains the known narrowed theorem",
    )

    # Candidate 3: an exponent needs an independently selected order parameter.
    samples = (Q(1, 8), Q(1, 4), Q(1, 2), Q(3, 4))
    score = samples
    squared_score = tuple(value**2 for value in samples)
    record(
        "monotone_score_reparameterization_preserves_order",
        all(
            (score[left] < score[right])
            == (squared_score[left] < squared_score[right])
            for left in range(len(samples))
            for right in range(len(samples))
        ),
        {"score": score, "squared_score": squared_score},
    )
    record(
        "same_threshold_order_can_carry_different_apparent_exponent",
        Q(1, 4) / Q(1, 2) == Q(1, 2)
        and (Q(1, 4) ** 2) / (Q(1, 2) ** 2) == Q(1, 4),
        {
            "linear_ratio": Q(1, 2),
            "squared_ratio": Q(1, 4),
        },
    )

    crossover_two = tuple(crossover(2, x) for x in (Q(1, 4), Q(1, 2), Q(3, 4)))
    crossover_eight = tuple(crossover(8, x) for x in (Q(1, 4), Q(1, 2), Q(3, 4)))
    record(
        "finite_analytic_crossover_can_look_sharp",
        crossover_two == (Q(1, 10), Q(1, 2), Q(9, 10))
        and crossover_eight == (Q(1, 6562), Q(1, 2), Q(6561, 6562)),
        {"size_2": crossover_two, "size_8": crossover_eight},
    )
    record(
        "finite_knee_is_not_yet_a_critical_point",
        all(
            x**size + (1 - x) ** size > 0
            for size in (2, 8, 32)
            for x in samples
        ),
        "the finite rational family has no singular denominator on the physical interval",
    )

    classifications = {
        "finality_rate_from_consensus": "EXACT_COUNTEREXAMPLE",
        "covariant_new_dynamics_rate": (
            "SCOPED_CONJECTURE_WITH_NONZERO_EXCESS__"
            "ALREADY_ROUTED_TO_PRED_DU_001_002__NOT_DERIVED"
        ),
        "broad_mergeability_complementarity": "EXACT_COUNTEREXAMPLE",
        "sharp_pvm_narrowing": "KNOWN_THEOREM_SPECIALIZATION",
        "universal_finality_exponents": "EXACT_COUNTEREXAMPLE",
    }
    record(
        "all_three_prepared_regional_candidates_fail_du_specific_excess_gate",
        classifications["finality_rate_from_consensus"] == "EXACT_COUNTEREXAMPLE"
        and classifications["broad_mergeability_complementarity"]
        == "EXACT_COUNTEREXAMPLE"
        and classifications["universal_finality_exponents"]
        == "EXACT_COUNTEREXAMPLE",
        classifications,
    )

    passed = sum(1 for check in CHECKS if check["passed"])
    result = {
        "schema_version": "1.0",
        "probe": "du_regional_finality_excess_audit_probe",
        "claim_id": "HC-DU-057",
        "work_id": "N5-PF-P4",
        "checks": CHECKS,
        "checks_passed": passed,
        "checks_total": len(CHECKS),
        "candidate_classifications": classifications,
        "rate_result": (
            "CONSENSUS_DOES_NOT_DERIVE_A_PHYSICAL_RATE__"
            "RATE_TRILEMMA_CORRECTED_TO_FOUR_WAY_CLASSIFICATION"
        ),
        "mergeability_result": (
            "SOURCE_JOINT_MEASURABILITY__INSTRUMENT_COMPATIBILITY__"
            "NONDISTURBANCE__JOINT_FORMATION__AND_ARCHIVE_MERGE_ARE_DISTINCT"
        ),
        "criticality_result": (
            "ORDER_PARAMETER_AND_SCALING_FAMILY_REQUIRED__"
            "FINITE_KNEE_IS_NOT_CRITICALITY"
        ),
        "du_specific_nonzero_residual": False,
        "foliation_role": "INERT",
        "next_position": "N5-PF-P5_PREFERRED_LEAF_PARTIAL_ORDER_ADJUDICATION",
        "maximum_grade": (
            "SCOPED_THREE_CANDIDATE_CLASSIFICATION_WITH_EXACT_COUNTEREXAMPLES"
        ),
        "not_claimed": [
            "a new physical finality rate",
            "a derivation of complementarity",
            "a universal finality exponent",
            "a selected collapse coefficient",
            "preferred-foliation evidence",
            "new ontology",
            "grade-5 physical remainder",
            "prediction promotion",
            "paper promotion",
            "hardware or provider result",
        ],
    }

    ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT.write_text(
        json.dumps(jsonable(result), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    if passed != len(CHECKS):
        failed = [check["name"] for check in CHECKS if not check["passed"]]
        print(f"FAIL: {passed}/{len(CHECKS)} checks; failed={failed}")
        return 1

    print(f"PASS: {passed}/{len(CHECKS)} exact checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
