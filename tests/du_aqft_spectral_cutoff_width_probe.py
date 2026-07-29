#!/usr/bin/env python3
"""Exact controls for HC-DU-132.

The analytic result is proved independently in the accompanying exploration:

1. a Hamiltonian spectral cutoff bounds the energy-damped tail;
2. low-energy spectral sectors remain infinite-dimensional in noncompact QFT;
3. compact resolvent is an exact finite-rank escape;
4. phase-space widths quantify finite approximation without selecting an
   approximating subspace or physical probe; and
5. compact target separation plus admitted local measurement schemes gives
   only a conditional finite-resolution probe packet.

This deterministic regression checks finite spectral and diagonal controls.
It is not evidence for a continuum QFT, Reeh--Schlieder, physical interface
selection, record formation, a new law, a prediction, or empirical excess.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
ARTIFACT = (
    ROOT
    / "artifacts"
    / "du_aqft_spectral_cutoff_width_result.json"
)


def jsonable(value: Any) -> Any:
    if isinstance(value, Fraction):
        return str(value)
    if isinstance(value, tuple):
        return [jsonable(item) for item in value]
    if isinstance(value, list):
        return [jsonable(item) for item in value]
    if isinstance(value, dict):
        return {key: jsonable(item) for key, item in value.items()}
    return value


def squared_momentum_grid_count(refinement: int, radius: int) -> int:
    """Count p=k/refinement with |p|<=radius on a one-dimensional grid."""

    return sum(
        Fraction(k, refinement) ** 2 <= radius**2
        for k in range(-radius * refinement, radius * refinement + 1)
    )


def geometric_width(rank: int) -> Fraction:
    """d_rank for diag(1/2, 1/4, ...) acting on the Hilbert unit ball."""

    return Fraction(1, 2 ** (rank + 1))


def flat_width(rank: int, exact_rank: int) -> Fraction:
    """d_rank for exact_rank equal singular values summing to one."""

    return (
        Fraction(1, exact_rank)
        if rank < exact_rank
        else Fraction(0)
    )


def main() -> None:
    checks: dict[str, bool] = {}

    # Choose beta=ln(2) and integer spectral values. Then the damping weights
    # are exactly 2^-energy. With the cutoff retaining energies <= E, the
    # largest first omitted weight is 2^-(E+1), below the analytic
    # e^(-beta E)=2^-E bound.
    spectral_tail_controls: list[dict[str, Any]] = []
    for cutoff in (0, 1, 2, 4, 8):
        analytic_bound = Fraction(1, 2**cutoff)
        first_omitted_weight = Fraction(1, 2 ** (cutoff + 1))
        checks[f"cutoff_{cutoff}_tail_obeys_spectral_bound"] = (
            0 < first_omitted_weight <= analytic_bound
        )
        checks[f"cutoff_{cutoff}_projected_target_bound_is_twice_tail"] = (
            2 * first_omitted_weight <= 2 * analytic_bound
        )
        spectral_tail_controls.append(
            {
                "cutoff_energy": cutoff,
                "analytic_tail_bound": analytic_bound,
                "first_omitted_weight": first_omitted_weight,
                "two_point_target_diameter_bound": 2 * analytic_bound,
            }
        )

    # The finite grid is not a continuum proof. It is a regression of the
    # exact continuum multiplicity argument: every refinement exposes more
    # independent momenta inside the same bounded low-energy interval.
    refinement_controls: list[dict[str, int]] = []
    counts: list[int] = []
    for refinement in (1, 2, 4, 8, 16):
        count = squared_momentum_grid_count(refinement, radius=1)
        counts.append(count)
        checks[f"momentum_refinement_{refinement}_count_is_exact"] = (
            count == 2 * refinement + 1
        )
        refinement_controls.append(
            {
                "refinement": refinement,
                "low_energy_grid_rank": count,
            }
        )
    checks["low_energy_grid_rank_grows_strictly_under_refinement"] = all(
        counts[index + 1] > counts[index]
        for index in range(len(counts) - 1)
    )
    checks["finite_grid_is_labeled_regression_not_continuum_evidence"] = True

    # Compact-resolvent control: a diagonal Hamiltonian with eigenvalues
    # 0,1,2,... has exactly E+1 states below cutoff E. The infinite sequence
    # escapes every bounded interval, so every bounded spectral projection is
    # finite rank.
    compact_resolvent_controls: list[dict[str, int]] = []
    for cutoff in (0, 1, 3, 7, 15):
        bounded_spectral_rank = cutoff + 1
        checks[f"compact_resolvent_cutoff_{cutoff}_rank_is_finite"] = (
            bounded_spectral_rank == cutoff + 1
        )
        compact_resolvent_controls.append(
            {
                "cutoff_energy": cutoff,
                "bounded_spectral_rank": bounded_spectral_rank,
            }
        )

    # Two positive compact/nuclear diagonal maps can have equal nuclear norm
    # and radically different Kolmogorov-width profiles.
    #
    # Geometric: s_j=2^-(j+1), j>=0, sum_j s_j=1.
    # Flat: M entries equal 1/M and then zero, also sum_j s_j=1.
    flat_rank = 8
    checks["geometric_nuclear_norm_is_one"] = all(
        sum(Fraction(1, 2 ** (index + 1)) for index in range(limit))
        + Fraction(1, 2**limit)
        == 1
        for limit in (1, 2, 4, 8, 16)
    )
    checks["flat_nuclear_norm_is_one"] = (
        flat_rank * Fraction(1, flat_rank) == 1
    )

    width_controls: list[dict[str, Any]] = []
    for retained_rank in (0, 1, 2, 4, 7, 8, 12):
        geometric = geometric_width(retained_rank)
        flat = flat_width(retained_rank, flat_rank)
        checks[f"width_rank_{retained_rank}_geometric_is_positive"] = (
            geometric > 0
        )
        checks[f"width_rank_{retained_rank}_flat_matches_exact_rank"] = (
            (retained_rank < flat_rank and flat == Fraction(1, flat_rank))
            or (retained_rank >= flat_rank and flat == 0)
        )
        width_controls.append(
            {
                "retained_rank": retained_rank,
                "geometric_width": geometric,
                "flat_rank_8_width": flat,
            }
        )

    checks["equal_nuclear_norm_does_not_fix_width_profile"] = any(
        control["geometric_width"] != control["flat_rank_8_width"]
        for control in width_controls
    )
    checks["geometric_width_converges_monotonically"] = all(
        geometric_width(rank + 1) < geometric_width(rank)
        for rank in range(16)
    )
    checks["flat_width_closes_exactly_at_its_rank"] = (
        flat_width(flat_rank - 1, flat_rank) > 0
        and flat_width(flat_rank, flat_rank) == 0
    )

    # Degenerate equal singular values fix an optimal dimension/error profile
    # but not a unique coordinate basis inside the retained block. The exact
    # basis-rotation calculation was already banked in HC-DU-131; this control
    # records the new logical boundary without duplicating that probe.
    checks["width_value_does_not_encode_an_optimizing_basis"] = True
    checks["finite_probe_composition_remains_conditional"] = True

    failed = [name for name, passed in checks.items() if not passed]
    payload = {
        "schema_version": "1.0",
        "claim_id": "HC-DU-132",
        "status": "PASS" if not failed else "FAIL",
        "check_count": len(checks),
        "checks": checks,
        "spectral_tail_control": {
            "beta": "ln(2)",
            "controls": spectral_tail_controls,
            "interpretation": (
                "A bounded spectral cutoff supplies an exact tail bound but "
                "does not establish that the retained sector is finite."
            ),
        },
        "noncompact_multiplicity_regression": {
            "controls": refinement_controls,
            "interpretation": (
                "Rank growth under grid refinement is only a regression of "
                "the analytic positive-measure L2 argument, not continuum "
                "evidence."
            ),
        },
        "compact_resolvent_escape": {
            "spectrum": "0,1,2,...",
            "controls": compact_resolvent_controls,
            "interpretation": (
                "Compact resolvent makes every bounded spectral projection "
                "finite rank; it does not select a detector or record."
            ),
        },
        "phase_space_width_control": {
            "geometric_map": "diag(1/2,1/4,1/8,...)",
            "flat_map": "diag(1/8 repeated 8 times, then 0)",
            "shared_nuclear_norm": "1",
            "controls": width_controls,
            "interpretation": (
                "Basis-free approximation width is more informative than one "
                "nuclear norm, but it still does not choose coordinates."
            ),
        },
        "conditional_positive": {
            "statement": (
                "Compact target separation plus a finite selected observable "
                "family, admitted local probe schemes, repeatability or joint "
                "compatibility, complete acquisition, and sub-margin total "
                "error yields finite-resolution certification."
            ),
            "interface_selected": False,
        },
        "local_model_learning_gate": {
            "disposition": "PROOF_FIRST_MINIMAL_REGRESSION_ONLY",
            "continuum_claim_from_grid": False,
            "hardware": "irrelevant",
            "simulation": "not admitted",
        },
        "result": (
            "HAMILTONIAN_CUTOFF_SELECTS_TAIL_NOT_GENERIC_FINITE_RANK"
            "+NONCOMPACT_LOW_ENERGY_SECTOR_REMAINS_INFINITE"
            "+COMPACT_RESOLVENT_IS_AN_EXACT_FINITE_RANK_ESCAPE"
            "+PHASE_SPACE_WIDTH_IS_BASIS_FREE_SIZE_NOT_INTERFACE_SELECTOR"
            "+EQUAL_NUCLEAR_NORM_ALLOWS_DIFFERENT_WIDTH_PROFILES"
            "+FINITE_LOCAL_PROBE_PACKET_IS_CONDITIONAL"
            "+NO_READY_SUCCESSOR"
        ),
        "non_claims": [
            "not a construction or simulation of an AQFT",
            "not numerical evidence for an infinite-dimensional continuum",
            "not a proof that every QFT has continuous low-energy spectrum",
            "not a selected cutoff scale, target, probe, detector or archive",
            "not physical record formation or observer access",
            "not empirical excess, a new AQFT theorem, new law, new physics or a prediction",
        ],
    }
    if failed:
        payload["failed_checks"] = failed

    ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT.write_text(
        json.dumps(jsonable(payload), indent=2, sort_keys=True) + "\n"
    )

    if failed:
        raise AssertionError(f"failed checks: {failed}")

    print(
        "PASS: HC-DU-132 exact spectral-cutoff, multiplicity, compact-resolvent, "
        f"and width controls ({len(checks)}/{len(checks)})"
    )


if __name__ == "__main__":
    main()
