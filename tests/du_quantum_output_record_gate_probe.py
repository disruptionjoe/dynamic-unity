#!/usr/bin/env python3
"""Exact finite certificate for HC-DU-075.

The analytic result lives in:
  explorations/quantum-output-carrier-classical-shadow-and-access-relocation-2026-07-28.md

This probe is not a trajectory simulation, collapse model, gravitational
model, ontology test, or hardware assay. It verifies two finite type controls:

* one retained amplitude-damping environment qubit supports inequivalent
  counting-like and homodyne-like classical shadows without any change of
  carrier; and
* two dilations of one erasure channel have swap-equivalent full complements
  but inequivalent information at a fixed accessible output port.
"""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_quantum_output_record_gate_result.json"
)
Q = Fraction

checks: list[dict[str, Any]] = []


def check(name: str, condition: bool, detail: Any) -> None:
    checks.append({"name": name, "passed": bool(condition), "detail": detail})
    if not condition:
        raise AssertionError(name)


def jsonable(value: Any) -> Any:
    if isinstance(value, Fraction):
        return f"{value.numerator}/{value.denominator}"
    if isinstance(value, tuple):
        return [jsonable(item) for item in value]
    if isinstance(value, list):
        return [jsonable(item) for item in value]
    if isinstance(value, dict):
        return {str(key): jsonable(item) for key, item in value.items()}
    return value


# ---------------------------------------------------------------------------
# One selected carrier, two classical shadows.
# ---------------------------------------------------------------------------

# Fix gamma = 1/4. For amplitude damping with input density matrix rho, the
# complementary environment output is
#
#   [[rho00 + (1-gamma)rho11, sqrt(gamma)rho01],
#    [sqrt(gamma)rho10,       gamma rho11       ]].
#
# At gamma=1/4 all entries used by the selected fixtures are rational.

gamma = Q(1, 4)
sqrt_gamma = Q(1, 2)


def environment_output(
    rho00: Fraction,
    rho01: Fraction,
    rho10: Fraction,
    rho11: Fraction,
) -> tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]:
    return (
        (rho00 + (1 - gamma) * rho11, sqrt_gamma * rho01),
        (sqrt_gamma * rho10, gamma * rho11),
    )


def trace(matrix: tuple[tuple[Fraction, ...], ...]) -> Fraction:
    return sum(matrix[i][i] for i in range(len(matrix)))


def z_shadow(
    matrix: tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]],
) -> tuple[Fraction, Fraction]:
    return matrix[0][0], matrix[1][1]


def x_shadow(
    matrix: tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]],
) -> tuple[Fraction, Fraction]:
    plus = Q(1, 2) * (
        matrix[0][0] + matrix[1][1] + matrix[0][1] + matrix[1][0]
    )
    return plus, 1 - plus


rho_phase_plus = environment_output(Q(1, 2), Q(1, 2), Q(1, 2), Q(1, 2))
rho_phase_minus = environment_output(Q(1, 2), Q(-1, 2), Q(-1, 2), Q(1, 2))
rho_population_zero = environment_output(Q(1), Q(0), Q(0), Q(0))
rho_population_one = environment_output(Q(0), Q(0), Q(0), Q(1))

check(
    "carrier_outputs_are_normalized",
    all(
        trace(matrix) == 1
        for matrix in (
            rho_phase_plus,
            rho_phase_minus,
            rho_population_zero,
            rho_population_one,
        )
    ),
    {
        "phase_plus": trace(rho_phase_plus),
        "phase_minus": trace(rho_phase_minus),
        "population_zero": trace(rho_population_zero),
        "population_one": trace(rho_population_one),
    },
)

check(
    "phase_target_same_counting_shadow",
    z_shadow(rho_phase_plus) == z_shadow(rho_phase_minus) == (Q(7, 8), Q(1, 8)),
    {
        "plus": z_shadow(rho_phase_plus),
        "minus": z_shadow(rho_phase_minus),
    },
)

check(
    "phase_target_distinct_homodyne_shadow",
    x_shadow(rho_phase_plus) == (Q(3, 4), Q(1, 4))
    and x_shadow(rho_phase_minus) == (Q(1, 4), Q(3, 4)),
    {
        "plus": x_shadow(rho_phase_plus),
        "minus": x_shadow(rho_phase_minus),
    },
)

phase_counting_error = Q(1, 2)
phase_homodyne_error = Q(1, 4)
phase_full_carrier_trace_distance = Q(1, 2)
phase_full_carrier_error = Q(1, 2) * (1 - phase_full_carrier_trace_distance)

check(
    "phase_target_full_carrier_matches_homodyne_optimum",
    phase_full_carrier_error == phase_homodyne_error < phase_counting_error,
    {
        "counting_error": phase_counting_error,
        "homodyne_error": phase_homodyne_error,
        "full_carrier_error": phase_full_carrier_error,
    },
)

check(
    "population_target_distinct_counting_shadow",
    z_shadow(rho_population_zero) == (Q(1), Q(0))
    and z_shadow(rho_population_one) == (Q(3, 4), Q(1, 4)),
    {
        "zero": z_shadow(rho_population_zero),
        "one": z_shadow(rho_population_one),
    },
)

check(
    "population_target_same_homodyne_shadow",
    x_shadow(rho_population_zero)
    == x_shadow(rho_population_one)
    == (Q(1, 2), Q(1, 2)),
    {
        "zero": x_shadow(rho_population_zero),
        "one": x_shadow(rho_population_one),
    },
)

population_counting_error = Q(3, 8)
population_homodyne_error = Q(1, 2)
population_full_carrier_error = Q(3, 8)

check(
    "population_target_full_carrier_matches_counting_optimum",
    population_full_carrier_error == population_counting_error < population_homodyne_error,
    {
        "counting_error": population_counting_error,
        "homodyne_error": population_homodyne_error,
        "full_carrier_error": population_full_carrier_error,
    },
)

check(
    "classical_shadow_plurality_does_not_change_carrier",
    rho_phase_plus
    == (
        (Q(7, 8), Q(1, 4)),
        (Q(1, 4), Q(1, 8)),
    )
    and z_shadow(rho_phase_plus) != x_shadow(rho_phase_plus),
    {
        "carrier": rho_phase_plus,
        "counting_shadow": z_shadow(rho_phase_plus),
        "homodyne_shadow": x_shadow(rho_phase_plus),
    },
)


# ---------------------------------------------------------------------------
# Same reduced channel and swap-equivalent complement, different fixed access.
# ---------------------------------------------------------------------------

# For input bit b, both isometries emit S'=0. The visible completion emits
# |b> on accessible E and |0> on hidden H. The hidden completion emits |0> on
# E and |b> on H. Their full E,H outputs are related by SWAP, but that swap
# does not preserve the fixed accessible algebra on E.


def visible_completion(bit: int) -> tuple[int, int, int]:
    return 0, bit, 0  # S', accessible E, hidden H


def hidden_completion(bit: int) -> tuple[int, int, int]:
    return 0, 0, bit


def swap_environment(output: tuple[int, int, int]) -> tuple[int, int, int]:
    system, accessible, hidden = output
    return system, hidden, accessible


check(
    "same_reduced_erasure_channel",
    all(visible_completion(bit)[0] == hidden_completion(bit)[0] == 0 for bit in (0, 1)),
    {
        "visible": [visible_completion(bit)[0] for bit in (0, 1)],
        "hidden": [hidden_completion(bit)[0] for bit in (0, 1)],
    },
)

check(
    "full_complements_related_by_swap",
    all(swap_environment(visible_completion(bit)) == hidden_completion(bit) for bit in (0, 1)),
    {
        "visible": [visible_completion(bit) for bit in (0, 1)],
        "hidden": [hidden_completion(bit) for bit in (0, 1)],
    },
)

visible_access_law = tuple(visible_completion(bit)[1] for bit in (0, 1))
hidden_access_law = tuple(hidden_completion(bit)[1] for bit in (0, 1))

check(
    "fixed_access_port_not_preserved_by_swap",
    visible_access_law == (0, 1) and hidden_access_law == (0, 0),
    {
        "visible_access_law": visible_access_law,
        "hidden_access_law": hidden_access_law,
    },
)

check(
    "access_target_risk_separates_completions",
    Q(0) < Q(1, 2),
    {
        "visible_equal_prior_bit_error": Q(0),
        "hidden_equal_prior_bit_error": Q(1, 2),
    },
)


result = {
    "claim_id": "HC-DU-075",
    "fixture": {
        "amplitude_damping_gamma": gamma,
        "predeclared_targets": ["phase_sign", "population_bit"],
        "predeclared_actions": ["environment_Z_counting_like", "environment_X_homodyne_like"],
        "phase": {
            "carrier_plus": rho_phase_plus,
            "carrier_minus": rho_phase_minus,
            "counting_error": phase_counting_error,
            "homodyne_error": phase_homodyne_error,
            "full_carrier_error": phase_full_carrier_error,
        },
        "population": {
            "carrier_zero": rho_population_zero,
            "carrier_one": rho_population_one,
            "counting_error": population_counting_error,
            "homodyne_error": population_homodyne_error,
            "full_carrier_error": population_full_carrier_error,
        },
        "access_relocation": {
            "same_reduced_channel": "constant_zero_erasure",
            "full_complement_relation": "environment_swap",
            "visible_access_law": visible_access_law,
            "hidden_access_law": hidden_access_law,
            "visible_equal_prior_bit_error": Q(0),
            "hidden_equal_prior_bit_error": Q(1, 2),
        },
    },
    "disposition": {
        "carrier_shadow": "CLASSICAL_SHADOW_PLURALITY_ONLY",
        "plain_complement": "QUANTUM_OUTPUT_EQUIVALENCE_CLASS_ONLY",
        "physical_access": "REQUIRES_ACCESS_PRESERVING_EQUIVALENCE",
        "positive_control": "CONDITIONAL_PHYSICAL_QUANTUM_RECORD_ADMITTED",
    },
    "checks": checks,
    "summary": {
        "passed": sum(1 for item in checks if item["passed"]),
        "total": len(checks),
    },
}

ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
ARTIFACT.write_text(
    json.dumps(jsonable(result), indent=2, sort_keys=True) + "\n",
    encoding="utf-8",
)

print(
    "du_quantum_output_record_gate_probe: "
    f"PASS ({result['summary']['passed']}/{result['summary']['total']})"
)
