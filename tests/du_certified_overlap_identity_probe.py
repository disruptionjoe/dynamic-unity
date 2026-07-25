#!/usr/bin/env python3
"""Exact finite pilot for typed certified-overlap identity.

The previous marginal-transfer swing showed that a compatibility compiler can
only adjudicate the cross-context identities it is given.  This probe attacks
the missing precondition.  It distinguishes:

* a repeated label;
* equality of outcome effects;
* equality of selective instruments;
* equality of multi-time continuation behavior; and
* provenance/value identity in an authenticated route fixture.

The quantum arm contains an important positive and negative control.  A
context-dependent post-measurement flip has exactly the same Z-outcome effects
as a QND Z instrument, but it is a different selective instrument and reverses
the next Z result.  An outcome-dependent Z phase is implementation-different
but induces the same selective CP maps, so it must be quotiented.

This is known finite quantum-instrument and authenticated-record mathematics.
It establishes a typed assay contract, not a physical identity-selection law.
"""

from __future__ import annotations

import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path
from typing import Any, Mapping, Sequence

from du_multitime_marginal_transfer_probe import (
    GaussianFraction,
    canonical_json,
    identity,
    matrix,
    matrix_add,
    matrix_dagger,
    matrix_equal,
    matrix_multiply,
    matrix_scale,
    matrix_trace,
    signed_message,
    verify_message,
)


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_certified_overlap_identity_result.json"
)

Matrix = tuple[tuple[GaussianFraction, ...], ...]


def jsonable(value: Any) -> Any:
    if isinstance(value, Fraction):
        return str(value)
    if isinstance(value, GaussianFraction):
        if value.imag:
            return f"{value.real}+{value.imag}i"
        return str(value.real)
    if isinstance(value, tuple):
        return [jsonable(item) for item in value]
    if isinstance(value, list):
        return [jsonable(item) for item in value]
    if isinstance(value, dict):
        return {str(key): jsonable(item) for key, item in value.items()}
    return value


def kraus_effect(kraus: Matrix) -> Matrix:
    return matrix_multiply(matrix_dagger(kraus), kraus)


def selective_map(kraus: Matrix, state: Matrix) -> Matrix:
    return matrix_multiply(
        matrix_multiply(kraus, state), matrix_dagger(kraus)
    )


def add_matrices(targets: Sequence[Matrix]) -> Matrix:
    result = matrix_scale(0, targets[0])
    for target in targets:
        result = matrix_add(result, target)
    return result


def matrix_unit(row: int, column: int) -> Matrix:
    return matrix(
        tuple(
            tuple(int(i == row and j == column) for j in range(2))
            for i in range(2)
        )
    )


def physical_probe_states() -> dict[str, Matrix]:
    imaginary = GaussianFraction(Fraction(0), Fraction(1))
    return {
        "zero": matrix(((1, 0), (0, 0))),
        "one": matrix(((0, 0), (0, 1))),
        "plus": matrix(
            (
                (Fraction(1, 2), Fraction(1, 2)),
                (Fraction(1, 2), Fraction(1, 2)),
            )
        ),
        "plus_i": matrix(
            (
                (Fraction(1, 2), -imaginary / 2),
                (imaginary / 2, Fraction(1, 2)),
            )
        ),
    }


def instrument_from_postunitary(
    postunitary: Matrix,
) -> tuple[Matrix, Matrix]:
    i2 = identity(2)
    z = matrix(((1, 0), (0, -1)))
    p0 = matrix_scale(Fraction(1, 2), matrix_add(i2, z))
    p1 = matrix_scale(
        Fraction(1, 2), matrix_add(i2, matrix_scale(-1, z))
    )
    return tuple(
        matrix_multiply(postunitary, projector)
        for projector in (p0, p1)
    )


def instrument_receipt(
    left_id: str,
    left: Sequence[Matrix],
    right_id: str,
    right: Sequence[Matrix],
) -> dict[str, Any]:
    if len(left) != 2 or len(right) != 2:
        raise ValueError("binary_instruments_required")
    i2 = identity(2)
    basis = tuple(
        matrix_unit(row, column)
        for row, column in itertools.product(range(2), repeat=2)
    )
    probes = physical_probe_states()

    left_effects = tuple(kraus_effect(kraus) for kraus in left)
    right_effects = tuple(kraus_effect(kraus) for kraus in right)
    effect_identity = left_effects == right_effects

    probe_probability_identity = all(
        matrix_trace(matrix_multiply(effect_left, state))
        == matrix_trace(matrix_multiply(effect_right, state))
        for effect_left, effect_right in zip(
            left_effects, right_effects, strict=True
        )
        for state in probes.values()
    )
    selective_map_identity = all(
        matrix_equal(
            selective_map(left_kraus, basis_element),
            selective_map(right_kraus, basis_element),
        )
        for left_kraus, right_kraus in zip(left, right, strict=True)
        for basis_element in basis
    )
    left_tp = matrix_equal(add_matrices(left_effects), i2)
    right_tp = matrix_equal(add_matrices(right_effects), i2)

    continuation_rows = []
    for initial in (0, 1):
        state = probes["zero" if initial == 0 else "one"]
        for outcome in (0, 1):
            left_post = selective_map(left[outcome], state)
            right_post = selective_map(right[outcome], state)
            probability = matrix_trace(left_post)
            if probability == 0:
                continue
            left_next = tuple(
                matrix_trace(matrix_multiply(effect, left_post))
                for effect in left_effects
            )
            right_next = tuple(
                matrix_trace(matrix_multiply(effect, right_post))
                for effect in left_effects
            )
            continuation_rows.append(
                {
                    "initial": initial,
                    "record_outcome": outcome,
                    "record_probability": probability,
                    "left_next_z_weights": left_next,
                    "right_next_z_weights": right_next,
                    "same_continuation": left_next == right_next,
                }
            )
    continuation_identity = all(
        row["same_continuation"] for row in continuation_rows
    )
    separator_count = sum(
        not row["same_continuation"] for row in continuation_rows
    )

    if selective_map_identity:
        disposition = (
            "SELECTIVE_INSTRUMENT_IDENTITY_CERTIFIED_"
            "RELATIVE_TO_DECLARED_LINEAR_MAP_CLASS"
        )
    elif effect_identity and not continuation_identity:
        disposition = (
            "OUTCOME_EFFECT_IDENTITY_ONLY / "
            "MULTITIME_INSTRUMENT_IDENTITY_REFUTED"
        )
    elif not effect_identity:
        disposition = "OUTCOME_EFFECT_IDENTITY_REFUTED"
    else:
        disposition = "INSTRUMENT_IDENTITY_UNDERIDENTIFIED"

    return {
        "left_instrument": left_id,
        "right_instrument": right_id,
        "same_record_label": True,
        "effects_equal_exactly": effect_identity,
        "tomographically_complete_probe_probabilities_equal": (
            probe_probability_identity
        ),
        "selective_maps_equal_on_matrix_basis": selective_map_identity,
        "both_nonselective_maps_trace_preserving": left_tp and right_tp,
        "held_out_next_z_continuation_equal": continuation_identity,
        "held_out_separator_count": separator_count,
        "continuation_rows": continuation_rows,
        "disposition": disposition,
        "identity_type": (
            "complete selective instrument"
            if selective_map_identity
            else (
                "outcome effect only"
                if effect_identity
                else "label only"
            )
        ),
    }


def quantum_overlap_control() -> dict[str, Any]:
    i2 = identity(2)
    x = matrix(((0, 1), (1, 0)))
    z = matrix(((1, 0), (0, -1)))

    qnd = instrument_from_postunitary(i2)
    inert_phase = instrument_from_postunitary(z)
    post_record_flip = instrument_from_postunitary(x)

    identical = instrument_receipt(
        "context_A_qnd_Z", qnd, "context_B_qnd_Z", qnd
    )
    phase_quotient = instrument_receipt(
        "context_A_qnd_Z", qnd, "context_B_outcome_phase_Z", inert_phase
    )
    disturbance_rival = instrument_receipt(
        "context_A_qnd_Z", qnd, "context_B_post_record_X", post_record_flip
    )

    return {
        "identical_context_control": identical,
        "implementation_phase_quotient_control": phase_quotient,
        "matched_effect_disturbance_rival": disturbance_rival,
        "lesson": (
            "equality of POVM effects licenses equality of outcome statistics "
            "but not equality of selective instruments, retained histories "
            "or future capabilities"
        ),
        "frozen_identity_receipt": (
            "compare effects and selective maps before marginal descent; "
            "hold out a sequential continuation and quotient implementations "
            "that induce the same complete CP maps"
        ),
    }


def value_commitment(origin: str, epoch: int, value: int) -> str:
    payload = {
        "origin": origin,
        "epoch": epoch,
        "value": value,
    }
    return hashlib.sha256(canonical_json(payload).encode()).hexdigest()


def protocol_pair_receipt(
    left: Mapping[str, Any],
    right: Mapping[str, Any],
) -> dict[str, Any]:
    left_valid = verify_message(
        left,
        expected_route=str(left["route"]),
        expected_epoch=int(left["epoch"]),
    )
    right_valid = verify_message(
        right,
        expected_route=str(right["route"]),
        expected_epoch=int(right["epoch"]),
    )
    same_origin = left["origin"] == right["origin"]
    same_epoch = left["epoch"] == right["epoch"]
    left_commitment = value_commitment(
        str(left["origin"]), int(left["epoch"]), int(left["value"])
    )
    right_commitment = value_commitment(
        str(right["origin"]), int(right["epoch"]), int(right["value"])
    )
    same_value_commitment = left_commitment == right_commitment
    canonical_value_identity = (
        left_valid
        and right_valid
        and same_origin
        and same_epoch
        and same_value_commitment
    )
    if canonical_value_identity:
        disposition = (
            "CANONICAL_VALUE_IDENTITY_CERTIFIED_IN_FIXTURE_"
            "BY_FORMED_ORIGIN_EPOCH_VALUE_COMMITMENT"
        )
    elif left_valid and right_valid and same_origin and same_epoch:
        disposition = (
            "AUTHENTICATED_OCCURRENCES / CANONICAL_VALUE_IDENTITY_REFUTED_"
            "BY_EQUIVOCATION"
        )
    else:
        disposition = "PROVENANCE_IDENTITY_INCOMPLETE_OR_REJECTED"
    return {
        "both_route_messages_authentic": left_valid and right_valid,
        "same_origin_label": same_origin,
        "same_epoch": same_epoch,
        "same_route": left["route"] == right["route"],
        "same_formed_origin_epoch_value_commitment": same_value_commitment,
        "canonical_value_identity_certified": canonical_value_identity,
        "disposition": disposition,
    }


def protocol_overlap_control() -> dict[str, Any]:
    consistent = protocol_pair_receipt(
        signed_message("A", "AB", 7, 0),
        signed_message("A", "CA", 7, 0),
    )
    equivocation = protocol_pair_receipt(
        signed_message("A", "AB", 7, 0),
        signed_message("A", "CA", 7, 1),
    )
    cross_epoch = protocol_pair_receipt(
        signed_message("A", "AB", 7, 0),
        signed_message("A", "CA", 8, 0),
    )
    return {
        "consistent_cross_route_control": consistent,
        "authenticated_equivocation_control": equivocation,
        "cross_epoch_nonidentity_control": cross_epoch,
        "lesson": (
            "authentication certifies each occurrence and its route; it does "
            "not force two same-origin occurrences to carry one value"
        ),
    }


def run() -> dict[str, Any]:
    quantum = quantum_overlap_control()
    protocol = protocol_overlap_control()
    q_identical = quantum["identical_context_control"]
    q_phase = quantum["implementation_phase_quotient_control"]
    q_rival = quantum["matched_effect_disturbance_rival"]
    p_consistent = protocol["consistent_cross_route_control"]
    p_equivocation = protocol["authenticated_equivocation_control"]
    p_epoch = protocol["cross_epoch_nonidentity_control"]

    checks = {
        "identical_quantum_instruments_have_equal_effects": q_identical[
            "effects_equal_exactly"
        ],
        "identical_quantum_instruments_have_equal_selective_maps": q_identical[
            "selective_maps_equal_on_matrix_basis"
        ],
        "identical_quantum_instruments_have_equal_continuations": q_identical[
            "held_out_next_z_continuation_equal"
        ],
        "phase_changed_kraus_implementation_has_equal_effects": q_phase[
            "effects_equal_exactly"
        ],
        "phase_changed_kraus_implementation_quotients_to_same_cp_maps": q_phase[
            "selective_maps_equal_on_matrix_basis"
        ],
        "phase_changed_kraus_implementation_has_equal_continuations": q_phase[
            "held_out_next_z_continuation_equal"
        ],
        "post_record_flip_has_identical_outcome_effects": q_rival[
            "effects_equal_exactly"
        ],
        "post_record_flip_matches_tomographic_outcome_probabilities": q_rival[
            "tomographically_complete_probe_probabilities_equal"
        ],
        "post_record_flip_is_not_same_selective_instrument": not q_rival[
            "selective_maps_equal_on_matrix_basis"
        ],
        "post_record_flip_is_separated_by_next_measurement": (
            not q_rival["held_out_next_z_continuation_equal"]
            and q_rival["held_out_separator_count"] == 2
        ),
        "all_quantum_candidate_instruments_are_trace_preserving": all(
            row["both_nonselective_maps_trace_preserving"]
            for row in (q_identical, q_phase, q_rival)
        ),
        "consistent_protocol_occurrences_are_authentic": p_consistent[
            "both_route_messages_authentic"
        ],
        "consistent_origin_epoch_value_commitment_certifies_fixture_identity": (
            p_consistent["canonical_value_identity_certified"]
        ),
        "authenticated_equivocation_preserves_occurrence_authenticity": (
            p_equivocation["both_route_messages_authentic"]
        ),
        "authenticated_equivocation_refutes_canonical_value_identity": (
            not p_equivocation["canonical_value_identity_certified"]
            and "EQUIVOCATION" in p_equivocation["disposition"]
        ),
        "cross_epoch_occurrences_are_not_one_certified_value": (
            not p_epoch["canonical_value_identity_certified"]
        ),
    }
    failures = tuple(name for name, passed in checks.items() if not passed)
    return {
        "schema_version": "dynamic-unity/certified-overlap-identity/v0.1",
        "run_id": "RUN-20260725-075017-operational-theory-landscape",
        "claim_grade": (
            "EXACT FINITE TYPED IDENTITY ASSAY / KNOWN QUANTUM-INSTRUMENT "
            "AND AUTHENTICATED-RECORD MATHEMATICS / PHYSICAL SELECTION OPEN"
        ),
        "typed_identity_ladder": (
            "same label",
            "same outcome effect",
            "same selective instrument",
            "same multi-time continuation",
            "same provenance/value",
            "same declared upper action",
        ),
        "quantum_instrument_control": quantum,
        "authenticated_protocol_control": protocol,
        "checks": checks,
        "check_count": len(checks),
        "failure_count": len(failures),
        "failures": failures,
        "verdict": (
            "OUTCOME_EFFECT_IDENTITY_SEPARATED_FROM_INSTRUMENT_HISTORY_"
            "IDENTITY / IMPLEMENTATION_GAUGE_QUOTIENTED / AUTHENTICATION_"
            "SEPARATED_FROM_CROSS_ROUTE_VALUE_IDENTITY"
        ),
        "does_not_establish": (
            "a physical law selecting overlap identities",
            "device-independent instrument equivalence",
            "laboratory robustness",
            "cryptographic security",
            "BFT finality",
            "beyond-standard quantum dynamics",
            "record-first ontology",
        ),
    }


def main() -> None:
    result = run()
    ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT.write_text(
        json.dumps(jsonable(result), indent=2, sort_keys=True) + "\n"
    )
    if result["failure_count"]:
        raise SystemExit(
            f"{result['failure_count']}/{result['check_count']} checks failed: "
            f"{result['failures']}"
        )
    print(
        f"{result['check_count']}/{result['check_count']} checks passed: "
        f"{ARTIFACT}"
    )


if __name__ == "__main__":
    main()
