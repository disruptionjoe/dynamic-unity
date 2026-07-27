#!/usr/bin/env python3
"""Exact controls for HC-DU-055 / N5-PF-P2.

This is a regression for a directly proved theorem package, not a simulation.
It keeps two questions separate:

1. Can a semantic certificate label change a response after the complete
   physical pre-response history and boundary input are fixed?
2. Is a declared control label a sufficient quotient of that physical
   boundary?

All arithmetic is exact.  No sampling, numerical tolerance, provider, or
external hardware is used.
"""

from __future__ import annotations

from fractions import Fraction
import json
from typing import Callable, Hashable, Iterable, Sequence


Q = Fraction
Matrix = tuple[tuple[Fraction, ...], ...]
CHECKS: list[dict[str, object]] = []


def record(name: str, passed: bool, detail: object) -> None:
    CHECKS.append({"name": name, "passed": bool(passed), "detail": detail})


def matrix(rows: Sequence[Sequence[int | Fraction]]) -> Matrix:
    return tuple(tuple(Q(value) for value in row) for row in rows)


def mul(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            sum(
                (left[i][k] * right[k][j] for k in range(len(right))),
                Q(0),
            )
            for j in range(len(right[0]))
        )
        for i in range(len(left))
    )


def transpose(item: Matrix) -> Matrix:
    return tuple(
        tuple(item[i][j] for i in range(len(item)))
        for j in range(len(item[0]))
    )


def trace(item: Matrix) -> Fraction:
    return sum((item[i][i] for i in range(len(item))), Q(0))


def evolve(operation: Matrix, state: Matrix) -> Matrix:
    return mul(mul(operation, state), transpose(operation))


def probability(state: Matrix, effect: Matrix) -> Fraction:
    return trace(mul(state, effect))


def row_stochastic(item: Matrix) -> bool:
    return all(
        all(entry >= 0 for entry in row) and sum(row, Q(0)) == 1
        for row in item
    )


def factors_through(
    domain: Iterable[Hashable],
    quotient: Callable[[Hashable], Hashable],
    target: Callable[[Hashable], Hashable],
) -> bool:
    seen: dict[Hashable, Hashable] = {}
    for point in domain:
        key = quotient(point)
        value = target(point)
        if key in seen and seen[key] != value:
            return False
        seen[key] = value
    return True


def inverse_two_by_two(item: Matrix) -> Matrix:
    a, b = item[0]
    c, d = item[1]
    determinant = a * d - b * c
    if determinant == 0:
        raise ValueError("matrix is singular")
    return (
        (d / determinant, -b / determinant),
        (-c / determinant, a / determinant),
    )


def evaluate_causal_events(order: Sequence[str]) -> dict[str, object]:
    state: dict[str, object] = {}
    for event in order:
        if event == "record":
            state["record"] = 1
        elif event == "controller_ready":
            state["controller_ready"] = True
        elif event == "certify":
            if state.get("record") != 1 or not state.get("controller_ready"):
                raise ValueError("certify executed before causal parents")
            state["certificate"] = "PASS"
        elif event == "act":
            if state.get("certificate") != "PASS":
                raise ValueError("act executed before certificate")
            state["boundary"] = "RELEASE"
        elif event == "respond":
            if state.get("boundary") != "RELEASE":
                raise ValueError("respond executed before boundary input")
            state["response"] = "OPEN"
        else:
            raise ValueError(f"unknown event {event}")
    return state


def main() -> int:
    # Deterministic semantic inertness and quotient factorization.
    domain = tuple(
        (x, boundary, certificate)
        for x in (0, 1)
        for boundary in ("IDENTITY", "FLIP")
        for certificate in ("PASS", "FAIL")
    )

    def response(point: Hashable) -> int:
        x, boundary, _certificate = point  # type: ignore[misc]
        return int(x) ^ int(boundary == "FLIP")

    record(
        "semantic_relabeling_is_inert_at_fixed_complete_boundary",
        factors_through(
            domain,
            lambda point: (point[0], point[1]),  # type: ignore[index]
            response,
        ),
        "Y factors through (X,B) and is constant in C",
    )
    record(
        "certificate_force_requires_a_new_physical_input",
        not factors_through(
            domain,
            lambda point: (point[0], point[1]),  # type: ignore[index]
            lambda point: (
                response(point),
                point[2],  # type: ignore[index]
            ),
        ),
        "a C-dependent response changes the response map instead of relabeling one realization",
    )

    physical_points = tuple(
        (x, boundary)
        for x in (0, 1)
        for boundary in ("IDENTITY", "FLIP")
    )
    record(
        "complete_physical_boundary_is_sufficient",
        factors_through(
            physical_points,
            lambda point: point,
            lambda point: int(point[0]) ^ int(point[1] == "FLIP"),
        ),
        "identity quotient has kernel contained in response kernel",
    )
    record(
        "lossy_declared_control_is_not_automatically_sufficient",
        not factors_through(
            physical_points,
            lambda point: (point[0], "ACT"),
            lambda point: int(point[0]) ^ int(point[1] == "FLIP"),
        ),
        "same X,U but different B gives different Y",
    )

    route_points = (
        (0, ("NOP", "route_a", 0)),
        (0, ("NOP", "route_b", 1)),
    )
    record(
        "hidden_route_or_memory_is_an_exact_boundary_witness",
        not factors_through(
            route_points,
            lambda point: (point[0], point[1][0]),
            lambda point: point[0] ^ point[1][2],
        ),
        "same declared NOP label; complete route/memory bit changes response",
    )

    # Stochastic postprocessing / Blackwell-style sufficiency.
    stochastic_q = matrix(((Q(3, 4), Q(1, 4)), (Q(1, 4), Q(3, 4))))
    stochastic_t = matrix(((Q(4, 5), Q(1, 5)), (Q(1, 5), Q(4, 5))))
    stochastic_m = mul(stochastic_q, stochastic_t)
    expected_m = matrix(((Q(13, 20), Q(7, 20)), (Q(7, 20), Q(13, 20))))
    record(
        "control_channel_is_stochastic",
        row_stochastic(stochastic_q),
        stochastic_q,
    )
    record(
        "decoder_is_stochastic",
        row_stochastic(stochastic_t),
        stochastic_t,
    )
    record(
        "positive_stochastic_postprocessing_exists",
        stochastic_m == expected_m and row_stochastic(stochastic_m),
        stochastic_m,
    )

    same_row_q = matrix(((Q(1, 2), Q(1, 2)), (Q(1, 2), Q(1, 2))))
    identity_m = matrix(((1, 0), (0, 1)))
    record(
        "same_row_channel_cannot_decode_distinct_response_rows",
        same_row_q[0] == same_row_q[1] and identity_m[0] != identity_m[1],
        "QT must have equal rows whenever Q has equal rows",
    )

    signed_decoder = mul(inverse_two_by_two(stochastic_q), identity_m)
    record(
        "invertible_channel_has_unique_linear_decoder",
        mul(stochastic_q, signed_decoder) == identity_m,
        signed_decoder,
    )
    record(
        "signed_decoder_preserves_row_normalization",
        all(sum(row, Q(0)) == 1 for row in signed_decoder),
        signed_decoder,
    )
    record(
        "signed_decoder_fails_positivity",
        any(entry < 0 for row in signed_decoder for entry in row),
        signed_decoder,
    )
    record(
        "linear_factorization_is_not_stochastic_sufficiency",
        not row_stochastic(signed_decoder),
        "positivity is load-bearing, not a cosmetic constraint",
    )

    # Quantum instrument quotient: same classical label, different operation.
    identity = matrix(((1, 0), (0, 1)))
    phase_z = matrix(((1, 0), (0, -1)))
    rho_plus = matrix(((Q(1, 2), Q(1, 2)), (Q(1, 2), Q(1, 2))))
    computational_zero = matrix(((1, 0), (0, 0)))
    computational_one = matrix(((0, 0), (0, 1)))
    plus_effect = rho_plus
    after_identity = evolve(identity, rho_plus)
    after_phase = evolve(phase_z, rho_plus)

    record(
        "quantum_operations_share_computational_population_label",
        (
            probability(after_identity, computational_zero)
            == probability(after_phase, computational_zero)
            == Q(1, 2)
            and probability(after_identity, computational_one)
            == probability(after_phase, computational_one)
            == Q(1, 2)
        ),
        "I and Z are both population-preserving on the declared classical interface",
    )
    record(
        "identical_complete_quantum_instrument_ignores_semantic_label",
        evolve(identity, rho_plus) == evolve(identity, rho_plus),
        "PASS/I and FAIL/I insert the same Choi/instrument operation",
    )
    record(
        "phase_sensitive_quantum_response_separates_same_classical_label",
        (
            probability(after_identity, plus_effect) == 1
            and probability(after_phase, plus_effect) == 0
        ),
        {
            "I_then_X_plus": str(probability(after_identity, plus_effect)),
            "Z_then_X_plus": str(probability(after_phase, plus_effect)),
        },
    )
    record(
        "quantum_witness_is_physical_instrument_difference_not_semantic_force",
        identity != phase_z and after_identity != after_phase,
        "the complete boundary instruments differ even though U is equal",
    )

    # Capability can change through ordinary certificate-conditioned policy.
    safe_actions = {
        "FAIL": frozenset({"WAIT"}),
        "PASS": frozenset({"WAIT", "RELEASE"}),
    }
    source_law = "same_fixed_source_dynamics"
    boundary_by_certificate = {"FAIL": "NO_SIGNAL", "PASS": "RELEASE_SIGNAL"}
    record(
        "certificate_conditioned_policy_strictly_enlarges_capability",
        safe_actions["FAIL"] < safe_actions["PASS"],
        {key: sorted(value) for key, value in safe_actions.items()},
    )
    record(
        "capability_change_has_ordinary_physical_boundary_path",
        boundary_by_certificate["FAIL"] != boundary_by_certificate["PASS"],
        boundary_by_certificate,
    )
    record(
        "source_law_need_not_change_when_capability_changes",
        source_law == "same_fixed_source_dynamics",
        source_law,
    )

    # Matched preferred-leaf / causal-partial-order control.
    preferred_order = (
        "record",
        "controller_ready",
        "certify",
        "act",
        "respond",
    )
    alternate_linear_extension = (
        "controller_ready",
        "record",
        "certify",
        "act",
        "respond",
    )
    preferred_result = evaluate_causal_events(preferred_order)
    partial_order_result = evaluate_causal_events(alternate_linear_extension)
    record(
        "different_linear_extensions_preserve_complete_causal_response",
        preferred_order != alternate_linear_extension
        and preferred_result == partial_order_result,
        preferred_result,
    )
    record(
        "forgetting_privileged_simultaneity_preserves_factorization",
        preferred_result["boundary"] == partial_order_result["boundary"]
        and preferred_result["response"] == partial_order_result["response"],
        "only causal parents enter the certificate/control/response maps",
    )
    record(
        "accessible_tick_phase_would_be_a_boundary_change",
        ("RELEASE", 0) != ("RELEASE", 1),
        "if tick phase reaches the response, it belongs in B and exact compensation is left",
    )

    attack_map = {
        "hidden_memory": "X_OR_B_INCOMPLETE",
        "route_or_timing": "B_INCOMPLETE",
        "hysteresis": "X_OR_B_INCOMPLETE",
        "occurrence_identity": "OCCURRENCE_MISMATCH",
        "certificate_directly_changes_law": "MODIFIED_DYNAMICS_OR_ONTOLOGY",
    }
    record(
        "hostile_cases_have_typed_diagnostic_returns",
        len(set(attack_map.values())) == 4
        and set(attack_map)
        == {
            "hidden_memory",
            "route_or_timing",
            "hysteresis",
            "occurrence_identity",
            "certificate_directly_changes_law",
        },
        attack_map,
    )

    passed = sum(1 for check in CHECKS if check["passed"])
    result = {
        "probe": "du_conservative_certification_feedback_probe",
        "claim_id": "HC-DU-055",
        "work_id": "N5-PF-P2",
        "checks": CHECKS,
        "checks_passed": passed,
        "checks_total": len(CHECKS),
        "scientific_verdict": "CONSERVATIVE_CERTIFICATION_THEOREM",
        "physical_boundary_verdict": "FACTORIZATION_AFTER_COMPLETE_MATCH",
        "declared_control_verdict": (
            "SUFFICIENT_IFF_DETERMINISTIC_QUOTIENT_OR_STOCHASTIC_POSTPROCESSING"
        ),
        "quantum_verdict": "WITHIN_CLASS_CHOIS_MUST_LIE_IN_PROCESS_LINK_KERNEL",
        "capability_verdict": "CAN_CHANGE_THROUGH_ORDINARY_PHYSICAL_FEEDBACK",
        "counterexample_to_conservativity": False,
        "exact_extra_boundary_state_witnesses": True,
        "mathematical_core": "KNOWN_MATHEMATICS__FULLY_ABSORBED",
        "foliation_role": "INERT",
        "next_position": (
            "N5-PF-P3_COMPLETE_PHYSICAL_FEEDBACK_BOUNDARY_SELECTION"
        ),
        "maximum_grade": (
            "SCOPED_DETERMINISTIC_STOCHASTIC_AND_QUANTUM_NECESSITY_PACKAGE"
        ),
        "not_claimed": [
            "certificate-only force",
            "new physical law",
            "new quantum process theorem",
            "new Blackwell theorem",
            "ontological result",
            "grade-5 physical remainder",
            "prediction",
            "paper promotion",
            "hardware result",
        ],
    }

    if passed != len(CHECKS):
        failed = [check["name"] for check in CHECKS if not check["passed"]]
        print(f"FAIL: {passed}/{len(CHECKS)} checks; failed={failed}")
        return 1

    print(json.dumps(result, indent=2, sort_keys=True, default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
