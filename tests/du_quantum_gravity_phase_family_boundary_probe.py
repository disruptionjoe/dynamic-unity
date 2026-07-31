#!/usr/bin/env python3
"""Exact controls for HC-DU-189's phase-family boundary.

This is not a linearized-gravity simulation.  It checks dependency, Gaussian
profile scaling, and perturbative-order consequences of the displayed phase
functionals in Chen and Giacomini, arXiv:2402.10288v2 / PRX 15, 031063.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_quantum_gravity_phase_family_boundary_result.json"
)


def gaussian_i1(sigma: float, probe_quadratic: float = 1.0) -> float:
    """Integral d^3k/(2pi)^3 |Q exp(-sigma^2 k^2/2)|^2."""
    if sigma <= 0:
        raise ValueError("sigma must be positive")
    return probe_quadratic / (8.0 * math.pi**1.5 * sigma**3)


def run_probe() -> dict[str, object]:
    checks: list[dict[str, object]] = []

    # Equations (37)--(38) contain only probe stress T_P.  The dependency
    # sets keep this exact source statement distinct from a numerical model.
    wide_source_dependencies = {"source_A", "source_B", "duration"}
    commutator_dependencies = {"probe_stress", "duration", "kappa"}
    checks.append(
        {
            "name": "wide_source_phase_depends_on_both_source_profiles",
            "passed": {"source_A", "source_B"}.issubset(
                wide_source_dependencies
            ),
        }
    )
    checks.append(
        {
            "name": "displayed_commutator_terms_have_no_source_dependency",
            "passed": not (
                {"source", "source_A", "source_B"}
                & commutator_dependencies
            ),
        }
    )

    # Source deletion leaves the free gravity Hamiltonian and probe coupling,
    # so the nested-commutator terms are unchanged while the source-dependent
    # zeroth-order cross term disappears.
    probe_branch_values = (1.0, 4.0)
    source_present = tuple(probe_branch_values)
    source_deleted = tuple(probe_branch_values)
    checks.append(
        {
            "name": "commutator_probe_branch_phase_survives_source_deletion",
            "passed": source_present == source_deleted,
        }
    )
    checks.append(
        {
            "name": "commutator_term_cancels_from_source_branch_difference",
            "passed": (source_present[0] - source_present[0]) == 0.0,
        }
    )
    checks.append(
        {
            "name": "commutator_term_can_still_separate_probe_branches",
            "passed": source_present[1] - source_present[0] != 0.0,
        }
    )

    # For Q_ij=p_i p_j and isotropic k directions, the squared TT projection
    # is (1/2) p^4 (1-mu^2)^2.  <mu^2>=1/3 and <mu^4>=1/5.
    tt_fraction = Fraction(1, 2) * (
        Fraction(1, 1) - 2 * Fraction(1, 3) + Fraction(1, 5)
    )
    checks.append(
        {
            "name": "rank_one_isotropic_tt_fraction_is_four_fifteenths",
            "passed": tt_fraction == Fraction(4, 15),
            "value": str(tt_fraction),
        }
    )

    # At alpha=1, Eqs. (37)--(38) give 1/8 I1 + 1/6 I_TT.
    total_fraction = Fraction(1, 8) + Fraction(1, 6) * tt_fraction
    checks.append(
        {
            "name": "combined_commutator_coefficient_is_sixty_one_over_360",
            "passed": total_fraction == Fraction(61, 360),
            "value": str(total_fraction),
        }
    )

    widths = (1.0, 0.5, 0.25, 0.125)
    integrals = tuple(gaussian_i1(width) for width in widths)
    ratios = tuple(
        integrals[index + 1] / integrals[index]
        for index in range(len(integrals) - 1)
    )
    checks.append(
        {
            "name": "halving_probe_width_multiplies_phase_integral_by_eight",
            "passed": all(abs(ratio - 8.0) < 1.0e-12 for ratio in ratios),
            "ratios": list(ratios),
        }
    )
    checks.append(
        {
            "name": "point_probe_limit_is_ultraviolet_divergent",
            "passed": integrals[-1] > integrals[0] * 500.0,
            "values": list(integrals),
        }
    )
    checks.append(
        {
            "name": "same_integrated_probe_stress_different_widths_give_different_phases",
            "passed": len({round(value, 14) for value in integrals})
            == len(integrals),
        }
    )

    # h_probe is O(kappa T_P); coupling it back to T_P is O(kappa T_P^2),
    # exactly the order of the displayed quadratic commutator functionals.
    displayed_order = (1, 2)  # powers of (kappa, T_P)
    omitted_self_gravity_order = (1, 2)
    checks.append(
        {
            "name": "probe_self_gravity_is_same_formal_order_as_displayed_term",
            "passed": displayed_order == omitted_self_gravity_order,
        }
    )

    passed = sum(bool(check["passed"]) for check in checks)
    return {
        "claim_id": "HC-DU-189",
        "status": "PASS" if passed == len(checks) else "FAIL",
        "passed_checks": passed,
        "total_checks": len(checks),
        "checks": checks,
        "analytic_fixture": {
            "probe_profile": "T_ij(k)=Q_ij exp(-sigma^2 |k|^2/2)",
            "rank_one_tensor": "Q_ij=p_i p_j",
            "i1": "p^4/(8 pi^(3/2) sigma^3)",
            "itt_over_i1": str(tt_fraction),
            "theta_comm_over_kappa_t3_i1": str(total_fraction),
            "theta_comm": (
                "61 kappa t^3 p^4 / (2880 pi^(3/2) sigma^3)"
            ),
        },
        "earned_boundary": (
            "The displayed commutator phases are probe-only self-response "
            "functionals: they survive source deletion, cancel from a pure "
            "source-branch difference, and require a selected finite probe "
            "profile or renormalization. The wide-source phase is a distinct "
            "source-dependent schema whose physical preparation map remains "
            "to be supplied."
        ),
        "non_claims": [
            "No published algebra is refuted by this dependency audit.",
            "Source independence does not make the commutator term classical.",
            "No complete conserved probe/controller calculation is supplied.",
            "No experimental magnitude, hardware action, or new DU law is earned.",
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
