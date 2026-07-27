#!/usr/bin/env python3
"""Exact regression controls for HC-DU-035E.

The accompanying exploration derives the public-shadow descent contract and
the native-type-erasure obstruction directly. This executable preserves only
the smallest finite witnesses and the unchanged first-obstruction grammar.

It is not a simulation, physical model, novelty proof, or hardware assay.
All calculations use integers, booleans, or exact Fraction arithmetic.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from fractions import Fraction
import hashlib
import itertools
import json
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_typed_public_shadow_descent_result.json"
)
Q = Fraction
Matrix = tuple[tuple[Fraction, ...], ...]


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, indent=2) + "\n"


def jsonable(value: Any) -> Any:
    if isinstance(value, Fraction):
        return str(value)
    if isinstance(value, tuple):
        return [jsonable(item) for item in value]
    if isinstance(value, list):
        return [jsonable(item) for item in value]
    if isinstance(value, dict):
        return {str(key): jsonable(item) for key, item in value.items()}
    return value


checks: list[dict[str, Any]] = []


def check(name: str, condition: bool, detail: str) -> None:
    checks.append({"name": name, "passed": bool(condition), "detail": detail})
    if not condition:
        raise AssertionError(name)


@dataclass(frozen=True)
class DescentPassport:
    name: str
    formed_local_interface: bool
    nonempty_joint_realization: bool
    occurrence_provenance_identity: bool
    selective_restrictions: bool
    jointly_realizable_resources: bool
    future_public_screening: bool
    benign_refinement_naturality: bool
    native_lift_selected: bool = False


OBSTRUCTION_ORDER = (
    ("formed_local_interface", "NO_FORMED_LOCAL_INTERFACE"),
    ("nonempty_joint_realization", "EMPTY_JOINT_REALIZATION"),
    (
        "occurrence_provenance_identity",
        "OCCURRENCE_OR_PROVENANCE_MISMATCH",
    ),
    ("selective_restrictions", "SELECTIVE_RESTRICTION_MISMATCH"),
    (
        "jointly_realizable_resources",
        "JOINT_RESOURCE_OR_INTERFACE_FAILURE",
    ),
    ("future_public_screening", "PUBLIC_ACTION_LEAK"),
    ("benign_refinement_naturality", "REFINEMENT_NONNATURAL"),
)


def classify(passport: DescentPassport) -> str:
    for field, disposition in OBSTRUCTION_ORDER:
        if not getattr(passport, field):
            return disposition
    if passport.native_lift_selected:
        return "PUBLIC_SHADOW_DESCENDS__NATIVE_LIFT_EARNED"
    return "PUBLIC_SHADOW_DESCENDS__NATIVE_LIFT_UNDERDETERMINED"


def parity_cycle_solutions(
    edge_constraints: tuple[int, int, int]
) -> tuple[tuple[int, int, int], ...]:
    """Return assignments satisfying A xor B, B xor C, C xor A."""

    solutions = []
    for a, b, c in itertools.product((0, 1), repeat=3):
        if (
            (a ^ b) == edge_constraints[0]
            and (b ^ c) == edge_constraints[1]
            and (c ^ a) == edge_constraints[2]
        ):
            solutions.append((a, b, c))
    return tuple(solutions)


def qnd_and_flip_rows() -> tuple[dict[str, int], ...]:
    rows = []
    for input_bit in (0, 1):
        outcome = input_bit
        rows.append(
            {
                "input": input_bit,
                "outcome": outcome,
                "qnd_next": input_bit,
                "flip_next": 1 - input_bit,
            }
        )
    return tuple(rows)


Pauli = tuple[tuple[int, ...], tuple[int, ...]]


def symplectic(left: Pauli, right: Pauli) -> int:
    x_left, z_left = left
    x_right, z_right = right
    return (
        sum(a * b for a, b in zip(x_left, z_right, strict=True))
        + sum(a * b for a, b in zip(z_left, x_right, strict=True))
    ) % 2


def syndrome(pauli: Pauli, stabilizers: Iterable[Pauli]) -> tuple[int, ...]:
    return tuple(symplectic(pauli, stabilizer) for stabilizer in stabilizers)


def mul(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            sum(
                (left[row][k] * right[k][col] for k in range(len(right))),
                Q(0),
            )
            for col in range(len(right[0]))
        )
        for row in range(len(left))
    )


def sub(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            left[row][col] - right[row][col]
            for col in range(len(left[0]))
        )
        for row in range(len(left))
    )


def nonzero(item: Matrix) -> bool:
    return any(value != 0 for row in item for value in row)


def main() -> int:
    # D1: exact cyclic full-cover obstruction.
    flat = parity_cycle_solutions((0, 0, 0))
    frustrated = parity_cycle_solutions((0, 0, 1))
    check(
        "flat binary triangle has exactly two global assignments",
        flat == ((0, 0, 0), (1, 1, 1)),
        "One root bit fixes the connected flat cover.",
    )
    check(
        "odd binary triangle has no global assignment",
        frustrated == (),
        "Pairwise relations are locally satisfiable but the full cover is empty.",
    )
    check(
        "inert relay preserves cycle syndrome",
        (0 ^ 0 ^ 1) == (0 ^ 0 ^ 0 ^ 1),
        "Subdividing one zero-parity edge does not change the obstruction.",
    )

    # D3: same value/effect, different selective continuation.
    instrument_rows = qnd_and_flip_rows()
    check(
        "QND and flip instruments expose the same first record value",
        all(row["outcome"] == row["input"] for row in instrument_rows),
        "Both instruments have the same sharp Z outcome effects.",
    )
    check(
        "held-out continuation separates QND from flip",
        all(row["qnd_next"] != row["flip_next"] for row in instrument_rows),
        "A repeated Z read separates the selective maps with certainty.",
    )

    # Gauge public quotient and first interior leak.
    gauge_left = (1, 0)
    gauge_right = (0, 1)
    flux_left = sum(gauge_left) % 3
    flux_right = sum(gauge_right) % 3
    check(
        "two interior configurations share one Z3 boundary flux",
        flux_left == flux_right == 1,
        "The boundary archive reconstructs total enclosed charge.",
    )
    check(
        "interior readout exposes the gauge fibre",
        gauge_left[0] != gauge_right[0],
        "An admitted n1-sensitive action separates the same-flux states.",
    )

    # QEC same-syndrome logical witness.
    zero = (0, 0, 0)
    stabilizers = (
        (zero, (1, 1, 0)),  # Z1 Z2
        (zero, (0, 1, 1)),  # Z2 Z3
    )
    identity_pauli = (zero, zero)
    logical_x = ((1, 1, 1), zero)
    encoded_zero = (0, 0, 0)
    encoded_one = tuple(1 - bit for bit in encoded_zero)
    check(
        "identity and logical X have the same complete syndrome",
        syndrome(identity_pauli, stabilizers)
        == syndrome(logical_x, stabilizers)
        == (0, 0),
        "Both commute with every stabilizer generator.",
    )
    check(
        "logical Z distinguishes the same-syndrome pair",
        encoded_zero[0] != encoded_one[0],
        "I maps |0_L> to |0_L>; X_L maps it to |1_L>.",
    )

    # Authenticated quorum and independent-support controls.
    n_validators, fault_bound = 4, 1
    check(
        "three-of-four quorum is Byzantine-safe at f=1",
        2 * 3 > n_validators + fault_bound,
        "Any two q=3 quorums contain more than f shared validators.",
    )
    check(
        "two-of-four quorum is unsafe at f=1",
        not (2 * 2 > n_validators + fault_bound),
        "Two q=2 quorums can intersect only in the Byzantine validator.",
    )
    raw_signatures = 3
    independent_origins = len({"alpha", "alpha", "alpha"})
    check(
        "raw signature count can exceed independent provenance rank",
        raw_signatures == 3 and independent_origins == 1,
        "Copies controlled by one origin do not supply three independent supports.",
    )

    # Exact noncommuting-state witness used by the no-broadcasting collision.
    rho_zero: Matrix = ((Q(1), Q(0)), (Q(0), Q(0)))
    rho_plus: Matrix = (
        (Q(1, 2), Q(1, 2)),
        (Q(1, 2), Q(1, 2)),
    )
    commutator = sub(mul(rho_zero, rho_plus), mul(rho_plus, rho_zero))
    check(
        "|0> and |+> density operators do not commute",
        nonzero(commutator),
        "The pair lies outside the exactly broadcastable commuting class.",
    )

    passports = (
        DescentPassport(
            name="einstein_matter_A1_flow_without_archive",
            formed_local_interface=False,
            nonempty_joint_realization=True,
            occurrence_provenance_identity=True,
            selective_restrictions=True,
            jointly_realizable_resources=True,
            future_public_screening=True,
            benign_refinement_naturality=True,
        ),
        DescentPassport(
            name="aqft_A2_induction_family_without_pointer",
            formed_local_interface=False,
            nonempty_joint_realization=True,
            occurrence_provenance_identity=True,
            selective_restrictions=True,
            jointly_realizable_resources=True,
            future_public_screening=True,
            benign_refinement_naturality=True,
        ),
        DescentPassport(
            name="frustrated_three_region_cover",
            formed_local_interface=True,
            nonempty_joint_realization=False,
            occurrence_provenance_identity=True,
            selective_restrictions=True,
            jointly_realizable_resources=True,
            future_public_screening=True,
            benign_refinement_naturality=True,
        ),
        DescentPassport(
            name="raw_signature_count_with_correlated_origin",
            formed_local_interface=True,
            nonempty_joint_realization=True,
            occurrence_provenance_identity=False,
            selective_restrictions=True,
            jointly_realizable_resources=True,
            future_public_screening=True,
            benign_refinement_naturality=True,
        ),
        DescentPassport(
            name="same_effect_different_continuation",
            formed_local_interface=True,
            nonempty_joint_realization=True,
            occurrence_provenance_identity=True,
            selective_restrictions=False,
            jointly_realizable_resources=True,
            future_public_screening=True,
            benign_refinement_naturality=True,
        ),
        DescentPassport(
            name="one_clock_counterfactual_join",
            formed_local_interface=True,
            nonempty_joint_realization=True,
            occurrence_provenance_identity=True,
            selective_restrictions=True,
            jointly_realizable_resources=False,
            future_public_screening=True,
            benign_refinement_naturality=True,
        ),
        DescentPassport(
            name="qec_syndrome_under_full_logical_actions",
            formed_local_interface=True,
            nonempty_joint_realization=True,
            occurrence_provenance_identity=True,
            selective_restrictions=True,
            jointly_realizable_resources=True,
            future_public_screening=False,
            benign_refinement_naturality=True,
        ),
        DescentPassport(
            name="relay_count_dependent_representation",
            formed_local_interface=True,
            nonempty_joint_realization=True,
            occurrence_provenance_identity=True,
            selective_restrictions=True,
            jointly_realizable_resources=True,
            future_public_screening=True,
            benign_refinement_naturality=False,
        ),
        DescentPassport(
            name="material_gauge_boundary_flux_envelope",
            formed_local_interface=True,
            nonempty_joint_realization=True,
            occurrence_provenance_identity=True,
            selective_restrictions=True,
            jointly_realizable_resources=True,
            future_public_screening=True,
            benign_refinement_naturality=True,
        ),
        DescentPassport(
            name="qec_syndrome_correctable_envelope",
            formed_local_interface=True,
            nonempty_joint_realization=True,
            occurrence_provenance_identity=True,
            selective_restrictions=True,
            jointly_realizable_resources=True,
            future_public_screening=True,
            benign_refinement_naturality=True,
        ),
        DescentPassport(
            name="aqft_A4_supplied_formed_archive",
            formed_local_interface=True,
            nonempty_joint_realization=True,
            occurrence_provenance_identity=True,
            selective_restrictions=True,
            jointly_realizable_resources=True,
            future_public_screening=True,
            benign_refinement_naturality=True,
        ),
        DescentPassport(
            name="safe_authenticated_certificate",
            formed_local_interface=True,
            nonempty_joint_realization=True,
            occurrence_provenance_identity=True,
            selective_restrictions=True,
            jointly_realizable_resources=True,
            future_public_screening=True,
            benign_refinement_naturality=True,
            native_lift_selected=False,
        ),
    )
    expected = {
        "einstein_matter_A1_flow_without_archive": "NO_FORMED_LOCAL_INTERFACE",
        "aqft_A2_induction_family_without_pointer": "NO_FORMED_LOCAL_INTERFACE",
        "frustrated_three_region_cover": "EMPTY_JOINT_REALIZATION",
        "raw_signature_count_with_correlated_origin": (
            "OCCURRENCE_OR_PROVENANCE_MISMATCH"
        ),
        "same_effect_different_continuation": (
            "SELECTIVE_RESTRICTION_MISMATCH"
        ),
        "one_clock_counterfactual_join": (
            "JOINT_RESOURCE_OR_INTERFACE_FAILURE"
        ),
        "qec_syndrome_under_full_logical_actions": "PUBLIC_ACTION_LEAK",
        "relay_count_dependent_representation": "REFINEMENT_NONNATURAL",
        "material_gauge_boundary_flux_envelope": (
            "PUBLIC_SHADOW_DESCENDS__NATIVE_LIFT_UNDERDETERMINED"
        ),
        "qec_syndrome_correctable_envelope": (
            "PUBLIC_SHADOW_DESCENDS__NATIVE_LIFT_UNDERDETERMINED"
        ),
        "aqft_A4_supplied_formed_archive": (
            "PUBLIC_SHADOW_DESCENDS__NATIVE_LIFT_UNDERDETERMINED"
        ),
        "safe_authenticated_certificate": (
            "PUBLIC_SHADOW_DESCENDS__NATIVE_LIFT_UNDERDETERMINED"
        ),
    }
    classifications = {item.name: classify(item) for item in passports}
    for name, disposition in expected.items():
        check(
            f"unchanged descent grammar classifies {name}",
            classifications[name] == disposition,
            disposition,
        )

    check(
        "first-obstruction grammar is total on the frozen controls",
        set(classifications) == set(expected),
        "Every control receives exactly one ordered return type.",
    )
    check(
        "public descent never silently earns native-interface identity",
        all(
            not item.native_lift_selected
            for item in passports
            if classify(item).startswith("PUBLIC_SHADOW_DESCENDS")
        ),
        "All positive public controls retain a plural or supplied native lift.",
    )

    all_passed = all(item["passed"] for item in checks)
    result = {
        "run_id": "RUN-20260726-dynamic-unity-typed-public-shadow-descent",
        "hypothesis_id": "HC-DU-035E",
        "scope": (
            "exact finite regression for the public-shadow descent "
            "and native-type-erasure result"
        ),
        "scientific_evidence": (
            "direct theorem analysis; this executable is regression only"
        ),
        "obstruction_order": [
            {"field": field, "failure": failure}
            for field, failure in OBSTRUCTION_ORDER
        ],
        "controls": [
            {
                "passport": asdict(passport),
                "classification": classifications[passport.name],
            }
            for passport in passports
        ],
        "finite_witnesses": {
            "flat_cycle_solutions": flat,
            "frustrated_cycle_solutions": frustrated,
            "selective_instrument_rows": instrument_rows,
            "gauge_same_flux_pair": {
                "left": gauge_left,
                "right": gauge_right,
                "flux": flux_left,
                "interior_n1_separates": True,
            },
            "qec_same_syndrome_pair": {
                "identity_syndrome": syndrome(
                    identity_pauli, stabilizers
                ),
                "logical_x_syndrome": syndrome(logical_x, stabilizers),
                "held_out_logical_z_margin": 1,
            },
            "byzantine_quorum": {
                "N": n_validators,
                "f": fault_bound,
                "q3_safe": True,
                "q2_safe": False,
                "raw_signatures": raw_signatures,
                "independent_origins": independent_origins,
            },
            "noncommuting_state_commutator": commutator,
        },
        "checks": checks,
        "all_passed": all_passed,
    }
    serialized = canonical_json(jsonable(result))
    digest = hashlib.sha256(serialized.encode("utf-8")).hexdigest()
    final = json.loads(serialized)
    final["sha256_without_digest"] = digest
    ARTIFACT.write_text(canonical_json(final), encoding="utf-8")

    passed = sum(item["passed"] for item in checks)
    print(
        "typed public-shadow descent regression: "
        f"{passed}/{len(checks)} checks passed"
    )
    print(f"artifact: {ARTIFACT}")
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
