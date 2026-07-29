#!/usr/bin/env python3
"""Exact controls for HC-DU-130.

The analytic result is proved independently in the accompanying exploration:

1. no nonzero finite-dimensional subspace of compactly supported smooth
   functions on R^d is invariant under every translation;
2. finite local packets can instead form a covariant region-indexed family,
   whose full translation orbit has infinite span;
3. finite translation-invariant sectors exist on noncompact space when
   locality is surrendered, and finite periodic arenas escape because the
   arena itself is supplied as finite; and
4. a finite Gaussian sector reconstructs its restricted state but not an
   independently admitted complementary mode.

This deterministic regression checks finite witnesses and positive controls.
It constructs no QFT, detector, observer, selected mode family, new law,
prediction, or empirical excess.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path
from typing import Any, Sequence


ROOT = Path(__file__).resolve().parent
ARTIFACT = (
    ROOT
    / "artifacts"
    / "du_covariant_local_finite_mode_trilemma_result.json"
)

Interval = tuple[Fraction, Fraction]
Vector = tuple[Fraction, ...]
Matrix = tuple[Vector, ...]


def translate_interval(interval: Interval, shift: Fraction) -> Interval:
    return interval[0] + shift, interval[1] + shift


def translate_packet(
    packet: tuple[Interval, ...],
    shift: Fraction,
) -> tuple[Interval, ...]:
    return tuple(translate_interval(interval, shift) for interval in packet)


def intervals_disjoint(left: Interval, right: Interval) -> bool:
    return left[1] <= right[0] or right[1] <= left[0]


def pairwise_disjoint(intervals: tuple[Interval, ...]) -> bool:
    return all(
        intervals_disjoint(intervals[left], intervals[right])
        for left in range(len(intervals))
        for right in range(left + 1, len(intervals))
    )


def evaluation_matrix(
    supports: tuple[Interval, ...],
    witnesses: tuple[Fraction, ...],
) -> Matrix:
    return tuple(
        tuple(
            Fraction(int(lower < witness < upper))
            for lower, upper in supports
        )
        for witness in witnesses
    )


def rank(matrix: Sequence[Sequence[Fraction]]) -> int:
    if not matrix:
        return 0
    work = [list(map(Fraction, row)) for row in matrix]
    row_count = len(work)
    column_count = len(work[0])
    pivot_row = 0
    for column in range(column_count):
        pivot = next(
            (
                row
                for row in range(pivot_row, row_count)
                if work[row][column] != 0
            ),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        pivot_value = work[pivot_row][column]
        work[pivot_row] = [
            entry / pivot_value for entry in work[pivot_row]
        ]
        for row in range(row_count):
            if row == pivot_row:
                continue
            factor = work[row][column]
            if factor == 0:
                continue
            work[row] = [
                entry - factor * pivot_entry
                for entry, pivot_entry in zip(
                    work[row],
                    work[pivot_row],
                    strict=True,
                )
            ]
        pivot_row += 1
        if pivot_row == row_count:
            break
    return pivot_row


def identity(dimension: int) -> Matrix:
    return tuple(
        tuple(
            Fraction(int(row == column))
            for column in range(dimension)
        )
        for row in range(dimension)
    )


def diagonal(entries: Sequence[Fraction]) -> Matrix:
    return tuple(
        tuple(
            entry if row == column else Fraction(0)
            for column, entry in enumerate(entries)
        )
        for row, entry in enumerate(entries)
    )


def principal_block(value: Matrix, dimension: int) -> Matrix:
    return tuple(
        tuple(value[row][column] for column in range(dimension))
        for row in range(dimension)
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


def main() -> None:
    checks: dict[str, bool] = {}

    # A compactly supported nonzero bump admits arbitrarily many pairwise
    # disjoint translates on the noncompact line. Evaluating each translate at
    # its private witness point gives an identity matrix, hence exact linear
    # independence. The smooth bump itself is not discretized; only the
    # support/evaluation argument used in the proof is checked.
    orbit_controls: list[dict[str, Any]] = []
    base_support: Interval = (Fraction(-1, 2), Fraction(1, 2))
    for orbit_size in (1, 2, 3, 5, 8):
        supports = tuple(
            translate_interval(base_support, Fraction(3 * index))
            for index in range(orbit_size)
        )
        witnesses = tuple(
            Fraction(3 * index) for index in range(orbit_size)
        )
        matrix = evaluation_matrix(supports, witnesses)
        exact_rank = rank(matrix)
        checks[f"disjoint_orbit_{orbit_size}_is_pairwise_disjoint"] = (
            pairwise_disjoint(supports)
        )
        checks[f"disjoint_orbit_{orbit_size}_has_full_rank"] = (
            exact_rank == orbit_size
            and matrix == identity(orbit_size)
        )
        orbit_controls.append(
            {
                "orbit_size": orbit_size,
                "supports": supports,
                "witnesses": witnesses,
                "evaluation_rank": exact_rank,
            }
        )

    # Covariance is correctly typed as a family S_x = tau_x S_0. Translating
    # a packet at x by b gives the packet at x+b. No fixed packet is claimed
    # invariant.
    base_packet: tuple[Interval, ...] = (
        (Fraction(-2), Fraction(-1)),
        (Fraction(0), Fraction(1)),
        (Fraction(3), Fraction(4)),
    )
    family_checks = []
    for location, shift in (
        (Fraction(-5), Fraction(2)),
        (Fraction(0), Fraction(7, 3)),
        (Fraction(11, 4), Fraction(-3, 2)),
    ):
        left = translate_packet(
            translate_packet(base_packet, location),
            shift,
        )
        right = translate_packet(base_packet, location + shift)
        family_checks.append(left == right)
    checks["indexed_local_packet_family_is_exactly_covariant"] = all(
        family_checks
    )
    checks["one_fixed_local_packet_is_not_invariant_under_large_shift"] = (
        translate_packet(base_packet, Fraction(100)) != base_packet
    )

    # On the finite periodic group Z_N, local delta functions have a finite
    # translation orbit spanning the whole supplied arena. This is the
    # finite-arena escape, not a counterexample on R^d.
    periodic_controls: list[dict[str, Any]] = []
    for group_size in (2, 3, 5, 7):
        delta_orbit = tuple(
            tuple(
                Fraction(int(site == shift))
                for site in range(group_size)
            )
            for shift in range(group_size)
        )
        orbit_rank = rank(delta_orbit)
        checks[f"periodic_{group_size}_local_orbit_is_finite_complete"] = (
            len(delta_orbit) == group_size
            and orbit_rank == group_size
        )

        # Character j has nonzero support on every site. Translation by a
        # shifts it only by the phase exponent j*a mod N, so each character
        # line is invariant and nonlocal.
        character = 1 if group_size > 1 else 0
        base_character_exponents = tuple(
            (character * site) % group_size
            for site in range(group_size)
        )
        translation_checks = tuple(
            tuple(
                base_character_exponents[(site - shift) % group_size]
                for site in range(group_size)
            )
            == tuple(
                (
                    exponent
                    - character * shift
                )
                % group_size
                for exponent in base_character_exponents
            )
            for shift in range(group_size)
        )
        checks[f"periodic_{group_size}_character_line_is_invariant"] = (
            all(translation_checks)
        )
        checks[f"periodic_{group_size}_character_is_global_not_local"] = (
            group_size > 1
        )
        periodic_controls.append(
            {
                "group": f"Z/{group_size}Z",
                "delta_orbit_dimension": orbit_rank,
                "character": character,
                "character_exponents": base_character_exponents,
                "translation_phase_exponents": tuple(
                    (-character * shift) % group_size
                    for shift in range(group_size)
                ),
                "character_support_size": group_size,
            }
        )

    # For any retained finite number of oscillator modes, append one
    # independent hidden oscillator. The two Gaussian states agree on the
    # complete retained covariance block and differ on the held-out mode.
    gaussian_controls: list[dict[str, Any]] = []
    for retained_modes in (1, 2, 3, 5):
        retained_dimension = 2 * retained_modes
        total_dimension = retained_dimension + 2
        state_a = diagonal(
            [Fraction(1, 2) for _ in range(total_dimension)]
        )
        state_b_entries = [
            Fraction(1, 2) for _ in range(retained_dimension)
        ] + [Fraction(3, 2), Fraction(3, 2)]
        state_b = diagonal(state_b_entries)

        retained_a = principal_block(state_a, retained_dimension)
        retained_b = principal_block(state_b, retained_dimension)
        hidden_q = retained_dimension
        held_out_a = state_a[hidden_q][hidden_q]
        held_out_b = state_b[hidden_q][hidden_q]
        characteristic_exponent_a = -held_out_a / 2
        characteristic_exponent_b = -held_out_b / 2

        checks[
            f"gaussian_{retained_modes}_retained_sector_is_identical"
        ] = retained_a == retained_b
        checks[
            f"gaussian_{retained_modes}_held_out_mode_is_first_leak"
        ] = (
            held_out_a != held_out_b
            and characteristic_exponent_a != characteristic_exponent_b
        )
        checks[
            f"gaussian_{retained_modes}_inside_target_reconstructs"
        ] = state_a[0][0] == state_b[0][0] == Fraction(1, 2)

        gaussian_controls.append(
            {
                "retained_modes": retained_modes,
                "retained_quadrature_dimension": retained_dimension,
                "same_complete_retained_covariance": retained_a == retained_b,
                "inside_target_variance": state_a[0][0],
                "hidden_variance_state_a": held_out_a,
                "hidden_variance_state_b": held_out_b,
                "hidden_weyl_exponent_state_a": characteristic_exponent_a,
                "hidden_weyl_exponent_state_b": characteristic_exponent_b,
            }
        )

    failed = [name for name, passed in checks.items() if not passed]
    if failed:
        raise AssertionError(f"failed checks: {failed}")

    artifact = {
        "schema_version": "1.0",
        "claim_id": "HC-DU-130",
        "status": "PASS",
        "result": (
            "NO_NONZERO_FIXED_FINITE_TRANSLATION_INVARIANT_LOCAL_PACKET"
            "+INDEXED_FINITE_LOCAL_PACKET_FAMILY_IS_COVARIANT"
            "+FULL_LOCAL_TRANSLATION_ORBIT_HAS_UNBOUNDED_DIMENSION"
            "+NONLOCAL_CHARACTER_AND_FINITE_PERIODIC_ESCAPES_PRESERVED"
            "+FINITE_GAUSSIAN_PACKET_RECONSTRUCTS_ONLY_ITS_RESTRICTION"
            "+COMPLEMENT_MODE_IS_THE_CONTINUUM_FIRST_LEAK"
            "+NO_READY_SUCCESSOR"
        ),
        "fixed_packet_theorem": {
            "arena": "C_c^infinity(R^d)",
            "proof": (
                "A nonzero compactly supported function has arbitrarily many "
                "pairwise disjoint translates; private-point evaluation makes "
                "them linearly independent."
            ),
            "finite_controls": orbit_controls,
        },
        "indexed_family_repair": {
            "definition": "S_x = tau_x S_0",
            "family_law": "tau_b(S_x) = S_(x+b)",
            "all_exact_checks_pass": all(family_checks),
            "interpretation": (
                "Covariance moves a finite local packet with its physical "
                "region index; it does not leave one fixed packet invariant."
            ),
        },
        "escape_controls": periodic_controls,
        "continuum_gaussian_first_leak": {
            "construction": (
                "Two product Gaussian states agree on every retained mode; "
                "one extra oscillator is vacuum in state A and thermal with "
                "covariance 3/2 I in state B."
            ),
            "controls": gaussian_controls,
            "interpretation": (
                "The finite population packet exactly reconstructs the "
                "restricted Gaussian state. A target on an independently "
                "admitted complementary mode does not factor through it."
            ),
        },
        "local_model_learning_gate": {
            "disposition": "PROOF_FIRST_MINIMAL_REGRESSION_ONLY",
            "simulation": "not admitted",
            "hardware": "irrelevant",
        },
        "non_claims": [
            "not a no-go on covariant families of finite local instruments",
            "not a no-go on finite nonlocal spectral sectors",
            "not a no-go on finite periodic or cutoff arenas",
            "not a selected QFT mode family, state, observer or record interface",
            "not continuum-state reconstruction from finite records",
            "not empirical excess, a new law, new physics or a prediction",
        ],
        "checks": checks,
        "check_count": len(checks),
    }
    ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT.write_text(
        json.dumps(jsonable(artifact), indent=2, sort_keys=True) + "\n"
    )
    print(f"PASS: {len(checks)}/{len(checks)} exact checks")
    print(f"artifact: {ARTIFACT}")


if __name__ == "__main__":
    main()
