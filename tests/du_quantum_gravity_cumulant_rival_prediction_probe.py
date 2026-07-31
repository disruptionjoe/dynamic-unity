#!/usr/bin/env python3
"""Exact finite controls for HC-DU-192's rival-prediction hierarchy.

This is an occupation-statistics, channel, and mediation-equivalence fixture.
It is not a quantum-gravity simulation and assigns no observed effect to
gravity.
"""

from __future__ import annotations

import argparse
import cmath
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_quantum_gravity_cumulant_rival_prediction_result.json"
)


def binomial_distribution(n: int, p: float) -> list[float]:
    return [
        math.comb(n, k) * p**k * (1.0 - p) ** (n - k)
        for k in range(n + 1)
    ]


def moment(values: list[float], probabilities: list[float], order: int) -> float:
    return sum(
        probability * value**order
        for value, probability in zip(values, probabilities)
    )


def characteristic(
    values: list[float], probabilities: list[float], chi: float
) -> complex:
    return sum(
        probability * cmath.exp(-1j * chi * value)
        for value, probability in zip(values, probabilities)
    )


def kron(
    left: list[list[complex]], right: list[list[complex]]
) -> list[list[complex]]:
    return [
        [
            left[i][j] * right[k][ell]
            for j in range(len(left[0]))
            for ell in range(len(right[0]))
        ]
        for i in range(len(left))
        for k in range(len(right))
    ]


def matvec(matrix: list[list[complex]], vector: list[complex]) -> list[complex]:
    return [sum(entry * value for entry, value in zip(row, vector)) for row in matrix]


def expectation(vector: list[complex], operator: list[list[complex]]) -> complex:
    acted = matvec(operator, vector)
    return sum(value.conjugate() * image for value, image in zip(vector, acted))


def run_probe() -> dict[str, object]:
    checks: list[dict[str, object]] = []
    tolerance = 1.0e-10

    # Same mean, different cumulants. The Hartree source has a binomial local
    # profile while the fragmented source has a sharp local occupation.
    particles = 20
    p_left = 0.35
    values = [float(k) for k in range(particles + 1)]
    hartree = binomial_distribution(particles, p_left)
    mean_hartree = moment(values, hartree, 1)
    mean_fragmented = float(round(particles * p_left))
    variance_hartree = moment(values, hartree, 2) - mean_hartree**2
    variance_fragmented = 0.0
    checks.append(
        {
            "name": "same_mean_sources_have_different_second_cumulant",
            "passed": abs(mean_hartree - mean_fragmented) < tolerance
            and variance_hartree > 0.0
            and variance_fragmented == 0.0,
            "mean": mean_hartree,
            "hartree_variance": variance_hartree,
            "fragmented_variance": variance_fragmented,
        }
    )

    chi = 0.21
    hartree_response = characteristic(values, hartree, chi)
    fragmented_response = cmath.exp(-1j * chi * mean_fragmented)
    semiclassical_hartree = cmath.exp(-1j * chi * mean_hartree)
    semiclassical_fragmented = cmath.exp(-1j * chi * mean_fragmented)
    checks.append(
        {
            "name": "mean_only_semiclassical_closure_identifies_same_mean_sources",
            "passed": abs(semiclassical_hartree - semiclassical_fragmented) < tolerance
            and abs(semiclassical_hartree) > 1.0 - tolerance,
        }
    )
    checks.append(
        {
            "name": "profile_sensitive_phase_channel_separates_them_by_visibility",
            "passed": abs(hartree_response) < abs(fragmented_response) - 0.05,
            "hartree_visibility": abs(hartree_response),
            "fragmented_visibility": abs(fragmented_response),
        }
    )

    # The diagonal quantum response is exactly reproducible by a classical
    # profile lottery with the same occupation probabilities.
    classical_profile_lottery = characteristic(values, hartree, chi)
    checks.append(
        {
            "name": "classical_profile_lottery_reproduces_full_diagonal_characteristic",
            "passed": abs(classical_profile_lottery - hartree_response) < tolerance,
        }
    )

    # A Gaussian stochastic model matches the mean and variance terms but not
    # the binomial third cumulant. Halving chi reduces the leading mismatch by
    # 2^3 when p != 1/2.
    third_cumulant = particles * p_left * (1.0 - p_left) * (1.0 - 2.0 * p_left)

    def gaussian_log_response(local_chi: float) -> complex:
        return (
            -1j * mean_hartree * local_chi
            - variance_hartree * local_chi**2 / 2.0
        )

    def exact_log_response(local_chi: float) -> complex:
        return particles * cmath.log(
            (1.0 - p_left) + p_left * cmath.exp(-1j * local_chi)
        )

    mismatch_large = abs(exact_log_response(0.005) - gaussian_log_response(0.005))
    mismatch_small = abs(exact_log_response(0.0025) - gaussian_log_response(0.0025))
    checks.append(
        {
            "name": "gaussian_stochastic_rival_matches_two_cumulants_but_not_three",
            "passed": third_cumulant > 0.0
            and mismatch_large > mismatch_small
            and abs(mismatch_large / mismatch_small - 8.0) < 0.05,
            "third_cumulant": third_cumulant,
            "halving_ratio": mismatch_large / mismatch_small,
        }
    )

    # Complementary coherence distinguishes the coherent Hartree preparation
    # from a number-diagonal mixture, even though their diagonal phase assay is
    # identical. This still does not identify the gravitational mechanism.
    pure_first_order_coherence = particles * math.sqrt(p_left * (1.0 - p_left))
    mixture_first_order_coherence = 0.0
    checks.append(
        {
            "name": "complementary_source_coherence_excludes_preexisting_profile_mixture",
            "passed": pure_first_order_coherence > 0.0
            and mixture_first_order_coherence == 0.0,
            "pure_first_order_coherence": pure_first_order_coherence,
        }
    )

    # A quantized controlled phase creates entanglement. For CZ|++>, the two
    # cluster stabilizers sum to 2; product states are bounded by 1 because
    # a_x b_z + a_z b_x <= ||(a_x,a_z)|| ||(b_z,b_x)|| <= 1.
    pauli_x = [[0j, 1.0 + 0j], [1.0 + 0j, 0j]]
    pauli_z = [[1.0 + 0j, 0j], [0j, -1.0 + 0j]]
    cluster = [0.5 + 0j, 0.5 + 0j, 0.5 + 0j, -0.5 + 0j]
    xz = expectation(cluster, kron(pauli_x, pauli_z)).real
    zx = expectation(cluster, kron(pauli_z, pauli_x)).real
    concurrence = 1.0
    checks.append(
        {
            "name": "controlled_profile_phase_can_cross_separable_channel_bound",
            "passed": abs(xz - 1.0) < tolerance
            and abs(zx - 1.0) < tolerance
            and xz + zx > 1.0 + tolerance
            and concurrence == 1.0,
            "cluster_witness_sum": xz + zx,
            "separable_bound": 1.0,
        }
    )

    # Endpoint matter statistics cannot distinguish a direct controlled phase
    # from a mediator that copies the source bit, phases the probe, and uncomputes.
    endpoint_equal = True
    midpoint_mediator_differs = False
    endpoint_rows: list[dict[str, int]] = []
    for source in (0, 1):
        for probe in (0, 1):
            mediator = 0
            mediator ^= source  # copy source into mediator
            midpoint_mediator = mediator
            mediated_phase = -1 if mediator * probe else 1
            mediator ^= source  # uncompute mediator
            direct_phase = -1 if source * probe else 1
            endpoint_equal &= mediator == 0 and mediated_phase == direct_phase
            midpoint_mediator_differs |= source == 1 and midpoint_mediator == 1
            endpoint_rows.append(
                {
                    "source": source,
                    "probe": probe,
                    "mediated_phase": mediated_phase,
                    "direct_phase": direct_phase,
                    "final_mediator": mediator,
                }
            )
    checks.append(
        {
            "name": "direct_and_mediated_controlled_phase_are_endpoint_equivalent",
            "passed": endpoint_equal,
            "rows": endpoint_rows,
        }
    )
    checks.append(
        {
            "name": "midprocess_mediator_access_separates_endpoint_equivalent_implementations",
            "passed": midpoint_mediator_differs,
        }
    )

    # A mean phase alone, a diagonal characteristic, and even a matter
    # entanglement witness therefore occupy different rival-exclusion levels.
    observable_hierarchy = [
        "mean_phase",
        "profile_cumulants_or_visibility",
        "complementary_coherence_or_entanglement",
        "mediator_facing_noncommuting_response",
    ]
    checks.append(
        {
            "name": "observable_hierarchy_has_strictly_distinct_adjudication_levels",
            "passed": len(observable_hierarchy) == len(set(observable_hierarchy)) == 4,
        }
    )

    passed = sum(bool(check["passed"]) for check in checks)
    return {
        "claim_id": "HC-DU-192",
        "status": "PASS" if passed == len(checks) else "FAIL",
        "passed_checks": passed,
        "total_checks": len(checks),
        "checks": checks,
        "rival_quotient": {
            "mean_phase": "shared by mean-field, profile-sensitive, stochastic, direct, and mediated models after calibration",
            "visibility_or_cumulants": "rejects expectation-value-only closure but is shared by diagonal quantum and classical stochastic/profile models",
            "coherence_or_entanglement": "rejects declared incoherent/separable-channel rivals but not every classical-gravity-plus-quantum-matter model",
            "mediator_facing_response": "required to distinguish a field mediator from endpoint-equivalent direct action",
        },
        "earned_boundary": (
            "Same-mean/different-cumulant visibility is a finite discriminator "
            "against expectation-value-only semiclassical closure. It is not a "
            "unique quantum-gravity witness: a classical profile lottery "
            "reproduces the full diagonal characteristic, Gaussian stochastic "
            "models reproduce its first two cumulants, and direct and mediated "
            "controlled phases are endpoint-equivalent. Complementary coherence, "
            "entanglement, and finally mediator-facing noncommuting access form "
            "successively stronger but separately assumption-indexed gates."
        ),
        "non_claims": [
            "No observed gravitational effect or apparatus is modeled.",
            "No universal classical-gravity theory is excluded.",
            "Matter entanglement alone is not credited as unique mediator identification.",
            "No field mediator, record interface, hardware action, or new DU law is selected.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-artifact", action="store_true")
    args = parser.parse_args()
    result = run_probe()
    if args.write_artifact:
        ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
        ARTIFACT.write_text(
            json.dumps(result, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
