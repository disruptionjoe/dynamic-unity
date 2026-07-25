#!/usr/bin/env python3
"""Exact operational-theory landscape calibration and DU transfer.

The probe separates six receipts that are often collapsed in foundational
arguments:

* conditional-table validity;
* no-signalling;
* local/global-counterfactual extendibility;
* explicit quantum realization;
* quantum exclusion by a declared bound; and
* quantum membership not resolved by the supplied evidence.

The CHSH calibration is known mathematics.  Its purpose here is to validate a
typed Dynamic Unity research contract, not to claim a new Bell result.  The
same receipt fields are then applied to the existing authenticated-route and
Mermin--Peres controls.
"""

from __future__ import annotations

import hashlib
import itertools
import json
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any, Mapping, Sequence

from du_exact_marginal_extension_compiler import (
    MarginalProblem,
    compile_marginal_extension,
    complete_context,
)
from du_multitime_marginal_transfer_probe import (
    authenticated_protocol_control,
    quantum_contextual_instrument_control,
)


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_operational_theory_landscape_result.json"
)


@dataclass(frozen=True, eq=False)
class Qsqrt2:
    """An exact ordered element ``rational + radical * sqrt(2)``."""

    rational: Fraction = Fraction(0)
    radical: Fraction = Fraction(0)

    def __post_init__(self) -> None:
        object.__setattr__(self, "rational", Fraction(self.rational))
        object.__setattr__(self, "radical", Fraction(self.radical))

    @staticmethod
    def coerce(value: Any) -> "Qsqrt2":
        if isinstance(value, Qsqrt2):
            return value
        return Qsqrt2(Fraction(value), Fraction(0))

    def __add__(self, other: Any) -> "Qsqrt2":
        target = self.coerce(other)
        return Qsqrt2(
            self.rational + target.rational,
            self.radical + target.radical,
        )

    def __radd__(self, other: Any) -> "Qsqrt2":
        return self + other

    def __sub__(self, other: Any) -> "Qsqrt2":
        target = self.coerce(other)
        return Qsqrt2(
            self.rational - target.rational,
            self.radical - target.radical,
        )

    def __rsub__(self, other: Any) -> "Qsqrt2":
        return self.coerce(other) - self

    def __neg__(self) -> "Qsqrt2":
        return Qsqrt2(-self.rational, -self.radical)

    def __mul__(self, other: Any) -> "Qsqrt2":
        target = self.coerce(other)
        return Qsqrt2(
            self.rational * target.rational
            + 2 * self.radical * target.radical,
            self.rational * target.radical
            + self.radical * target.rational,
        )

    def __rmul__(self, other: Any) -> "Qsqrt2":
        return self * other

    def __truediv__(self, other: Any) -> "Qsqrt2":
        target = self.coerce(other)
        denominator = (
            target.rational * target.rational
            - 2 * target.radical * target.radical
        )
        if denominator == 0:
            raise ZeroDivisionError("zero quadratic-surd denominator")
        return self * Qsqrt2(
            target.rational / denominator,
            -target.radical / denominator,
        )

    def sign(self) -> int:
        a = self.rational
        b = self.radical
        if a == 0:
            return (b > 0) - (b < 0)
        if b == 0:
            return (a > 0) - (a < 0)
        if a > 0 and b > 0:
            return 1
        if a < 0 and b < 0:
            return -1
        comparison = a * a - 2 * b * b
        if comparison == 0:
            return 0
        if a > 0 and b < 0:
            return 1 if comparison > 0 else -1
        return -1 if comparison > 0 else 1

    def __eq__(self, other: object) -> bool:
        try:
            target = self.coerce(other)
        except (TypeError, ValueError, ZeroDivisionError):
            return False
        return (
            self.rational == target.rational
            and self.radical == target.radical
        )

    def __hash__(self) -> int:
        return hash((self.rational, self.radical))

    def __lt__(self, other: Any) -> bool:
        return (self - other).sign() < 0

    def __le__(self, other: Any) -> bool:
        return (self - other).sign() <= 0

    def __gt__(self, other: Any) -> bool:
        return (self - other).sign() > 0

    def __ge__(self, other: Any) -> bool:
        return (self - other).sign() >= 0

    def __abs__(self) -> "Qsqrt2":
        return self if self.sign() >= 0 else -self

    def __bool__(self) -> bool:
        return self != 0

    def text(self) -> str:
        if self.radical == 0:
            return str(self.rational)
        if self.rational == 0:
            return f"{self.radical}*sqrt(2)"
        sign = "+" if self.radical > 0 else ""
        return f"{self.rational}{sign}{self.radical}*sqrt(2)"


Scalar = Qsqrt2
Matrix = tuple[tuple[Scalar, ...], ...]
Behavior = dict[tuple[int, int, int, int], Scalar]


def q(value: Any = 0, radical: Any = 0) -> Qsqrt2:
    return Qsqrt2(Fraction(value), Fraction(radical))


def jsonable(value: Any) -> Any:
    if isinstance(value, Qsqrt2):
        return value.text()
    if isinstance(value, Fraction):
        return str(value)
    if isinstance(value, tuple):
        return [jsonable(item) for item in value]
    if isinstance(value, list):
        return [jsonable(item) for item in value]
    if isinstance(value, dict):
        return {str(key): jsonable(item) for key, item in value.items()}
    return value


def canonical_json(value: Any) -> str:
    return json.dumps(jsonable(value), sort_keys=True, separators=(",", ":"))


def matrix(rows: Sequence[Sequence[Any]]) -> Matrix:
    target = tuple(tuple(Qsqrt2.coerce(value) for value in row) for row in rows)
    if not target or any(len(row) != len(target[0]) for row in target):
        raise ValueError("invalid_matrix")
    return target


def matrix_add(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(a + b for a, b in zip(lrow, rrow, strict=True))
        for lrow, rrow in zip(left, right, strict=True)
    )


def matrix_subtract(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(a - b for a, b in zip(lrow, rrow, strict=True))
        for lrow, rrow in zip(left, right, strict=True)
    )


def matrix_scale(value: Any, target: Matrix) -> Matrix:
    scalar = Qsqrt2.coerce(value)
    return tuple(
        tuple(scalar * item for item in row)
        for row in target
    )


def matrix_multiply(left: Matrix, right: Matrix) -> Matrix:
    if len(left[0]) != len(right):
        raise ValueError("matrix_dimension_mismatch")
    return tuple(
        tuple(
            sum(
                (
                    left[row][inner] * right[inner][column]
                    for inner in range(len(right))
                ),
                start=q(),
            )
            for column in range(len(right[0]))
        )
        for row in range(len(left))
    )


def matrix_transpose(target: Matrix) -> Matrix:
    return tuple(
        tuple(target[row][column] for row in range(len(target)))
        for column in range(len(target[0]))
    )


def matrix_trace(target: Matrix) -> Scalar:
    return sum(
        (target[index][index] for index in range(len(target))),
        start=q(),
    )


def matrix_equal(left: Matrix, right: Matrix) -> bool:
    return left == right


def identity(dimension: int) -> Matrix:
    return matrix(
        tuple(
            tuple(int(row == column) for column in range(dimension))
            for row in range(dimension)
        )
    )


def kronecker(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            left[left_row][left_column]
            * right[right_row][right_column]
            for left_column in range(len(left[0]))
            for right_column in range(len(right[0]))
        )
        for left_row in range(len(left))
        for right_row in range(len(right))
    )


def bell_state_density() -> Matrix:
    return matrix(
        (
            (Fraction(1, 2), 0, 0, Fraction(1, 2)),
            (0, 0, 0, 0),
            (0, 0, 0, 0),
            (Fraction(1, 2), 0, 0, Fraction(1, 2)),
        )
    )


def projector(observable: Matrix, output: int) -> Matrix:
    sign = 1 if output == 0 else -1
    return matrix_scale(
        Fraction(1, 2),
        matrix_add(identity(len(observable)), matrix_scale(sign, observable)),
    )


def behavior_digest(behavior: Mapping[tuple[int, int, int, int], Scalar]) -> str:
    payload = tuple(
        {
            "x": key[0],
            "y": key[1],
            "a": key[2],
            "b": key[3],
            "probability": behavior[key],
        }
        for key in sorted(behavior)
    )
    return hashlib.sha256(canonical_json(payload).encode()).hexdigest()


def quantum_behavior(
    realization_id: str,
    alice: Mapping[int, Matrix],
    bob: Mapping[int, Matrix],
    *,
    require_tsirelson_square: bool,
) -> tuple[Behavior, dict[str, Any]]:
    rho = bell_state_density()
    state_checks = {
        "hermitian": matrix_equal(rho, matrix_transpose(rho)),
        "trace_one": matrix_trace(rho) == 1,
        "pure_projector": matrix_equal(matrix_multiply(rho, rho), rho),
    }
    observable_checks = {
        f"A{setting}": {
            "hermitian": matrix_equal(value, matrix_transpose(value)),
            "involution": matrix_equal(
                matrix_multiply(value, value), identity(2)
            ),
        }
        for setting, value in alice.items()
    }
    observable_checks.update(
        {
            f"B{setting}": {
                "hermitian": matrix_equal(value, matrix_transpose(value)),
                "involution": matrix_equal(
                    matrix_multiply(value, value), identity(2)
                ),
            }
            for setting, value in bob.items()
        }
    )

    projector_checks: list[bool] = []
    behavior: Behavior = {}
    for x, y, a, b in itertools.product((0, 1), repeat=4):
        pa = projector(alice[x], a)
        pb = projector(bob[y], b)
        for local_projector in (pa, pb):
            projector_checks.append(
                matrix_equal(
                    matrix_multiply(local_projector, local_projector),
                    local_projector,
                )
                and matrix_equal(
                    local_projector, matrix_transpose(local_projector)
                )
            )
        joint = kronecker(pa, pb)
        behavior[(x, y, a, b)] = matrix_trace(
            matrix_multiply(rho, joint)
        )

    chsh_operator = matrix_add(
        kronecker(alice[0], matrix_add(bob[0], bob[1])),
        kronecker(alice[1], matrix_subtract(bob[0], bob[1])),
    )
    expectation = matrix_trace(matrix_multiply(rho, chsh_operator))
    behavior_chsh = chsh_value(behavior)
    state_is_chsh_eigenstate = matrix_equal(
        matrix_multiply(chsh_operator, rho),
        matrix_scale(expectation, rho),
    )
    square_is_eight_on_state_support = matrix_equal(
        matrix_multiply(
            matrix_multiply(chsh_operator, chsh_operator), rho
        ),
        matrix_scale(8, rho),
    )
    receipt = {
        "receipt_type": "EXPLICIT_STATE_AND_MEASUREMENT_REALIZATION",
        "realization_id": realization_id,
        "state": "two-qubit Bell state |Phi+><Phi+|",
        "state_checks": state_checks,
        "observable_checks": observable_checks,
        "all_projectors_hermitian_idempotent": all(projector_checks),
        "all_probabilities_nonnegative": all(
            probability >= 0 for probability in behavior.values()
        ),
        "all_contexts_normalized": all(
            sum(
                (
                    behavior[(x, y, a, b)]
                    for a, b in itertools.product((0, 1), repeat=2)
                ),
                start=q(),
            )
            == 1
            for x, y in itertools.product((0, 1), repeat=2)
        ),
        "chsh_operator_expectation": expectation,
        "chsh_expectation_matches_behavior": expectation == behavior_chsh,
        "state_is_chsh_operator_eigenstate": state_is_chsh_eigenstate,
        "chsh_operator_square_is_eight_on_state_support": (
            square_is_eight_on_state_support
        ),
        "tsirelson_square_required": require_tsirelson_square,
    }
    receipt["verified"] = (
        all(state_checks.values())
        and all(
            row["hermitian"] and row["involution"]
            for row in observable_checks.values()
        )
        and receipt["all_projectors_hermitian_idempotent"]
        and receipt["all_probabilities_nonnegative"]
        and receipt["all_contexts_normalized"]
        and receipt["chsh_expectation_matches_behavior"]
        and (
            not require_tsirelson_square
            or (
                state_is_chsh_eigenstate
                and square_is_eight_on_state_support
            )
        )
    )
    receipt["behavior_digest"] = behavior_digest(behavior)
    return behavior, receipt


def isotropic_behavior(visibility: Any) -> Behavior:
    v = Qsqrt2.coerce(visibility)
    behavior: Behavior = {}
    for x, y, a, b in itertools.product((0, 1), repeat=4):
        target_sign = -1 if (x == 1 and y == 1) else 1
        output_sign = 1 if a == b else -1
        behavior[(x, y, a, b)] = (
            q(1) + target_sign * output_sign * v
        ) / 4
    return behavior


def deterministic_local_behavior() -> Behavior:
    return {
        (x, y, a, b): q(int(a == 0 and b == 0))
        for x, y, a, b in itertools.product((0, 1), repeat=4)
    }


def signalling_behavior() -> Behavior:
    return {
        (x, y, a, b): q(int(a == 0 and b == x))
        for x, y, a, b in itertools.product((0, 1), repeat=4)
    }


def invalid_behavior() -> Behavior:
    behavior = deterministic_local_behavior()
    behavior[(0, 0, 0, 0)] = q(2)
    return behavior


def validate_behavior(behavior: Mapping[tuple[int, int, int, int], Scalar]) -> dict[str, Any]:
    expected = set(itertools.product((0, 1), repeat=4))
    supplied = set(behavior)
    errors: list[str] = []
    if supplied != expected:
        errors.append("incomplete_behavior_table")
    if any(probability < 0 for probability in behavior.values()):
        errors.append("negative_probability")
    context_sums = {
        f"{x}{y}": sum(
            (
                behavior.get((x, y, a, b), q())
                for a, b in itertools.product((0, 1), repeat=2)
            ),
            start=q(),
        )
        for x, y in itertools.product((0, 1), repeat=2)
    }
    if any(total != 1 for total in context_sums.values()):
        errors.append("context_not_normalized")
    return {
        "valid": not errors,
        "errors": tuple(sorted(set(errors))),
        "context_sums": context_sums,
    }


def no_signalling_receipt(
    behavior: Mapping[tuple[int, int, int, int], Scalar],
) -> dict[str, Any]:
    alice_marginals = {
        (x, y, a): sum(
            (behavior[(x, y, a, b)] for b in (0, 1)),
            start=q(),
        )
        for x, y, a in itertools.product((0, 1), repeat=3)
    }
    bob_marginals = {
        (x, y, b): sum(
            (behavior[(x, y, a, b)] for a in (0, 1)),
            start=q(),
        )
        for x, y, b in itertools.product((0, 1), repeat=3)
    }
    alice_violations = tuple(
        {
            "x": x,
            "a": a,
            "difference": alice_marginals[(x, 0, a)]
            - alice_marginals[(x, 1, a)],
        }
        for x, a in itertools.product((0, 1), repeat=2)
        if alice_marginals[(x, 0, a)] != alice_marginals[(x, 1, a)]
    )
    bob_violations = tuple(
        {
            "y": y,
            "b": b,
            "difference": bob_marginals[(0, y, b)]
            - bob_marginals[(1, y, b)],
        }
        for y, b in itertools.product((0, 1), repeat=2)
        if bob_marginals[(0, y, b)] != bob_marginals[(1, y, b)]
    )
    return {
        "no_signalling": not alice_violations and not bob_violations,
        "alice_setting_independence_violations": alice_violations,
        "bob_setting_independence_violations": bob_violations,
    }


def correlators(
    behavior: Mapping[tuple[int, int, int, int], Scalar],
) -> dict[str, Scalar]:
    return {
        f"E{x}{y}": sum(
            (
                (1 if a == b else -1) * behavior[(x, y, a, b)]
                for a, b in itertools.product((0, 1), repeat=2)
            ),
            start=q(),
        )
        for x, y in itertools.product((0, 1), repeat=2)
    }


def chsh_value(
    behavior: Mapping[tuple[int, int, int, int], Scalar],
) -> Scalar:
    values = correlators(behavior)
    return values["E00"] + values["E01"] + values["E10"] - values["E11"]


def chsh_local_bound_receipt(observed: Scalar) -> dict[str, Any]:
    vertex_values = []
    for a0, a1, b0, b1 in itertools.product((-1, 1), repeat=4):
        vertex_values.append(a0 * b0 + a0 * b1 + a1 * b0 - a1 * b1)
    return {
        "receipt_type": "DIRECT_CHSH_BELL_FUNCTIONAL",
        "deterministic_vertex_count": len(vertex_values),
        "deterministic_vertex_minimum": min(vertex_values),
        "deterministic_vertex_maximum": max(vertex_values),
        "local_bound": q(2),
        "observed_value": observed,
        "proves_nonlocal_under_frozen_identity_contract": abs(observed) > 2,
    }


def rational_marginal_problem(
    behavior_id: str,
    behavior: Mapping[tuple[int, int, int, int], Scalar],
) -> MarginalProblem:
    if any(value.radical != 0 for value in behavior.values()):
        raise ValueError("behavior_is_not_rational")
    outcomes = {
        name: ("0", "1")
        for name in ("A0", "A1", "B0", "B1")
    }
    contexts = []
    for x, y in itertools.product((0, 1), repeat=2):
        variables = (f"A{x}", f"B{y}")
        probabilities = {
            (str(a), str(b)): behavior[(x, y, a, b)].rational
            for a, b in itertools.product((0, 1), repeat=2)
        }
        contexts.append(
            complete_context(
                f"x{x}y{y}", variables, outcomes, probabilities
            )
        )
    return MarginalProblem(
        problem_id=f"chsh-local-extension:{behavior_id}",
        variable_outcomes=tuple(outcomes.items()),
        contexts=tuple(contexts),
    )


def theory_landscape_card(**fields: Any) -> dict[str, Any]:
    required = (
        "card_id",
        "operational_object",
        "frozen_assumptions",
        "restrictive_foil",
        "target_class",
        "permissive_foil",
        "membership_receipt",
        "exclusion_receipt",
        "selection_principle",
        "held_out_discriminator",
        "disposition",
        "does_not_establish",
    )
    card = dict(fields)
    missing = tuple(
        name
        for name in required
        if name not in card
        or card[name] is None
        or card[name] == ""
        or card[name] == ()
    )
    card["contract_complete"] = not missing
    card["missing_fields"] = missing
    return card


def classify_behavior(
    behavior_id: str,
    behavior: Behavior,
    *,
    quantum_receipt: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    validity = validate_behavior(behavior)
    digest = behavior_digest(behavior)
    if not validity["valid"]:
        return {
            "behavior_id": behavior_id,
            "behavior_digest": digest,
            "validity": validity,
            "landscape_position": "OUTSIDE_VALID_CONDITIONAL_BEHAVIORS",
            "no_signalling": None,
            "local_status": "NOT_APPLICABLE",
            "quantum_status": "NOT_APPLICABLE",
        }

    signalling = no_signalling_receipt(behavior)
    value = chsh_value(behavior)
    correlator_table = correlators(behavior)
    local_bound = chsh_local_bound_receipt(value)
    if not signalling["no_signalling"]:
        return {
            "behavior_id": behavior_id,
            "behavior_digest": digest,
            "validity": validity,
            "no_signalling": signalling,
            "correlators": correlator_table,
            "chsh_value": value,
            "local_bound_receipt": local_bound,
            "landscape_position": "VALID_SIGNALING_CONDITIONAL_BEHAVIOR",
            "local_status": "REJECTED_BEFORE_LOCAL_CLASSIFICATION",
            "quantum_status": "REJECTED_BY_DECLARED_SPACELIKE_NO_SIGNALLING_CONTRACT",
        }

    rational = all(value.radical == 0 for value in behavior.values())
    marginal_result: dict[str, Any] | None = None
    if rational:
        marginal_result = compile_marginal_extension(
            rational_marginal_problem(behavior_id, behavior)
        )
        local_status = (
            "LOCAL_GLOBAL_COUNTERFACTUAL_EXTENSION"
            if marginal_result["verdict"] == "GLOBAL_EXTENSION"
            else "PROVEN_NONLOCAL_EXACT_FARKAS_OBSTRUCTION"
        )
    else:
        local_status = (
            "PROVEN_NONLOCAL_DIRECT_CHSH_WITNESS"
            if local_bound["proves_nonlocal_under_frozen_identity_contract"]
            else "LOCAL_STATUS_UNRESOLVED_FOR_ALGEBRAIC_BEHAVIOR"
        )

    tsirelson_bound = q(0, 2)
    quantum_receipt_accepted = bool(
        quantum_receipt
        and quantum_receipt.get("verified")
        and quantum_receipt.get("behavior_digest") == digest
    )
    if local_status == "LOCAL_GLOBAL_COUNTERFACTUAL_EXTENSION":
        quantum_status = "QUANTUM_REALIZABLE_BY_LOCAL_CLASSICAL_EMBEDDING"
        landscape_position = "LOCAL_SUBSET"
    elif quantum_receipt_accepted:
        quantum_status = "EXPLICIT_QUANTUM_REALIZATION"
        landscape_position = "QUANTUM_NONLOCAL"
    elif abs(value) > tsirelson_bound:
        quantum_status = "PROVEN_POST_QUANTUM_IN_FROZEN_CHSH_SCENARIO"
        landscape_position = "NO_SIGNALLING_POST_QUANTUM"
    else:
        quantum_status = "QUANTUM_STATUS_UNRESOLVED"
        landscape_position = (
            "NO_SIGNALLING_NONLOCAL_QUANTUM_STATUS_UNRESOLVED"
        )

    return {
        "behavior_id": behavior_id,
        "behavior_digest": digest,
        "validity": validity,
        "no_signalling": signalling,
        "correlators": correlator_table,
        "chsh_value": value,
        "local_bound_receipt": local_bound,
        "rational_exact_marginal_receipt": marginal_result,
        "local_status": local_status,
        "tsirelson_receipt": {
            "bound": tsirelson_bound,
            "observed_value": value,
            "exceeds_bound": abs(value) > tsirelson_bound,
            "saturates_bound": abs(value) == tsirelson_bound,
            "assumptions": (
                "binary plus-or-minus-one observables",
                "ordinary Hilbert-space state and Born probabilities",
                "commuting or tensor-separated Alice/Bob observables",
                "frozen setting identities and measurement independence",
            ),
        },
        "quantum_receipt_supplied": quantum_receipt is not None,
        "quantum_receipt_accepted": quantum_receipt_accepted,
        "quantum_realization_receipt": (
            dict(quantum_receipt) if quantum_receipt else None
        ),
        "quantum_status": quantum_status,
        "landscape_position": landscape_position,
        "force_permit_disposition": (
            "CONSTRUCTIVELY_REALIZED"
            if quantum_status
            in {
                "EXPLICIT_QUANTUM_REALIZATION",
                "QUANTUM_REALIZABLE_BY_LOCAL_CLASSICAL_EMBEDDING",
            }
            else (
                "EXCLUDED_FROM_QUANTUM_UNDER_DECLARED_ASSUMPTIONS"
                if quantum_status
                == "PROVEN_POST_QUANTUM_IN_FROZEN_CHSH_SCENARIO"
                else "PERMITTED_BY_TESTED_BOUNDS_NOT_PROVED_QUANTUM"
            )
        ),
    }


def chsh_calibration() -> dict[str, Any]:
    x = matrix(((0, 1), (1, 0)))
    z = matrix(((1, 0), (0, -1)))
    alice = {0: z, 1: x}

    rational_bob = {
        0: matrix_add(
            matrix_scale(Fraction(3, 5), z),
            matrix_scale(Fraction(4, 5), x),
        ),
        1: matrix_subtract(
            matrix_scale(Fraction(3, 5), z),
            matrix_scale(Fraction(4, 5), x),
        ),
    }
    rational_quantum, rational_receipt = quantum_behavior(
        "bell-rational-pauli-plane-3-4-5",
        alice,
        rational_bob,
        require_tsirelson_square=False,
    )

    inverse_sqrt_two = q(0, Fraction(1, 2))
    tsirelson_bob = {
        0: matrix_scale(inverse_sqrt_two, matrix_add(z, x)),
        1: matrix_scale(inverse_sqrt_two, matrix_subtract(z, x)),
    }
    tsirelson_quantum, tsirelson_receipt = quantum_behavior(
        "bell-tsirelson-saturating",
        alice,
        tsirelson_bob,
        require_tsirelson_square=True,
    )

    fixtures = {
        "deterministic_local": classify_behavior(
            "deterministic_local", deterministic_local_behavior()
        ),
        "isotropic_local_boundary": classify_behavior(
            "isotropic_local_boundary",
            isotropic_behavior(q(Fraction(1, 2))),
        ),
        "rational_quantum_nonlocal": classify_behavior(
            "rational_quantum_nonlocal",
            rational_quantum,
            quantum_receipt=rational_receipt,
        ),
        "same_behavior_realization_withheld": classify_behavior(
            "same_behavior_realization_withheld",
            rational_quantum,
        ),
        "tsirelson_quantum_boundary": classify_behavior(
            "tsirelson_quantum_boundary",
            tsirelson_quantum,
            quantum_receipt=tsirelson_receipt,
        ),
        "isotropic_postquantum": classify_behavior(
            "isotropic_postquantum",
            isotropic_behavior(q(Fraction(3, 4))),
        ),
        "pr_box": classify_behavior(
            "pr_box", isotropic_behavior(q(1))
        ),
        "signalling_control": classify_behavior(
            "signalling_control", signalling_behavior()
        ),
        "invalid_control": classify_behavior(
            "invalid_control", invalid_behavior()
        ),
    }
    forged = classify_behavior(
        "pr_box_with_mismatched_quantum_receipt",
        isotropic_behavior(q(1)),
        quantum_receipt=rational_receipt,
    )
    landscape_card = theory_landscape_card(
        card_id="TL-CHSH-01",
        operational_object="complete binary p(a,b|x,y) behavior",
        frozen_assumptions=(
            "binary settings and outputs",
            "setting identities fixed before outcomes",
            "measurement independence",
            "Alice/Bob tensor or commuting separation",
        ),
        restrictive_foil="local global-counterfactual extension on A0,A1,B0,B1",
        target_class="ordinary quantum behavior with explicit realization",
        permissive_foil="all normalized no-signalling behaviors",
        membership_receipt=(
            "exact local primal or explicit state-and-measurement Born table"
        ),
        exclusion_receipt=(
            "exact marginal Farkas/Bell witness and exact Tsirelson comparison"
        ),
        selection_principle=(
            "ordinary Hilbert-space composition, operator algebra, and Born rule"
        ),
        held_out_discriminator=(
            "CHSH functional with local 2, quantum 2*sqrt(2), and "
            "no-signalling 4 controls"
        ),
        disposition=(
            "KNOWN_MATHEMATICS_CALIBRATION_NOT_DYNAMIC_UNITY_NOVELTY"
        ),
        does_not_establish=(
            "one true ontology",
            "superluminal influence",
            "record substrate fundamentality",
            "a Dynamic Unity physical law",
        ),
    )
    return {
        "fixtures": fixtures,
        "forged_receipt_control": forged,
        "rational_quantum_realization": rational_receipt,
        "tsirelson_quantum_realization": tsirelson_receipt,
        "landscape_card": landscape_card,
        "identity_sensitive_statement": (
            "Bell nonexistence excludes the declared global "
            "A0,A1,B0,B1 identity/common-cause model; it does not exclude "
            "the explicit quantum process or select an ontology"
        ),
    }


def cross_platform_transfer() -> dict[str, Any]:
    protocol = authenticated_protocol_control()
    quantum = quantum_contextual_instrument_control()

    protocol_card = theory_landscape_card(
        card_id="TL-DU-AUTH-01",
        operational_object=(
            "complete authenticated route/epoch transcript marginals and "
            "declared upper actions"
        ),
        frozen_assumptions=(
            "origin, route, epoch, parentage and fixture authenticator fixed",
            "same-origin cross-route identity proposed before compilation",
            "equivocation adversary admitted",
        ),
        restrictive_foil=(
            "one canonical origin value across every authenticated route"
        ),
        target_class=(
            "route/epoch-provenance process with explicit equivocation handling"
        ),
        permissive_foil=(
            "independent occurrence value for every route transcript"
        ),
        membership_receipt={
            "coarse_verdict": protocol["coarse_origin_problem"]["verdict"],
            "provenance_lift_verdict": protocol[
                "route_provenance_lift"
            ]["verdict"],
            "disposition": protocol["protocol_disposition"],
        },
        exclusion_receipt=(
            "exact Farkas obstruction excludes canonical-origin gluing "
            "under the frozen identity map"
        ),
        selection_principle=(
            "formed origin/route/epoch provenance plus declared "
            "equivocation and failure-domain rules"
        ),
        held_out_discriminator=(
            "cross-epoch replay, same-epoch equivocation and upper action defect"
        ),
        disposition=(
            "COARSE_IDENTITY_EXCLUDED / PROVENANCE_PROCESS_REALIZED / "
            "SAFE_REJECTION_REQUIRED"
        ),
        does_not_establish=(
            "cryptographic security",
            "BFT safety or liveness",
            "physical public finality",
            "one universal provenance ontology",
        ),
    )

    quantum_card = theory_landscape_card(
        card_id="TL-DU-MP-01",
        operational_object=(
            "six complete commuting Mermin--Peres context instruments and "
            "their exact outcome marginals"
        ),
        frozen_assumptions=(
            "nine repeated observable labels",
            "six implemented compatible contexts",
            "context-independent value identity proposed before compilation",
            "complete instrument context retained in the physical process",
        ),
        restrictive_foil=(
            "one noncontextual preassigned value for each repeated observable"
        ),
        target_class=(
            "explicit context-indexed ordinary quantum instruments"
        ),
        permissive_foil=(
            "maximal occurrence splitting with one unrelated variable per context"
        ),
        membership_receipt={
            "noncontextual_gluing": quantum[
                "compiled_noncontextual_gluing"
            ]["verdict"],
            "context_indexed_extension": quantum[
                "context_indexed_product_extension"
            ],
            "physical_disposition": quantum[
                "physical_process_disposition"
            ],
        },
        exclusion_receipt=(
            "inclusion-minimal exact dual obstruction excludes the supplied "
            "noncontextual gluing"
        ),
        selection_principle=(
            "independently certified operational equivalence, compatibility, "
            "nondisturbance, repeatability and disturbance accounting"
        ),
        held_out_discriminator=(
            "context permutation, sequential repeatability, causal break and "
            "context-dependent disturbance rival"
        ),
        disposition=(
            "NONCONTEXTUAL_IDENTITY_EXCLUDED / STANDARD_QUANTUM_PROCESS_REALIZED / "
            "PHYSICAL_OVERLAP_SELECTION_OPEN"
        ),
        does_not_establish=(
            "failure of the quantum process",
            "observer-relative collapse",
            "beyond-standard quantum dynamics",
            "record-first ontology",
        ),
    )

    return {
        "authenticated_route_landscape": protocol_card,
        "quantum_context_landscape": quantum_card,
        "shared_open_selection_problem": (
            "warrant cross-context identity strongly enough to prevent "
            "arbitrary occurrence splitting without inserting a classical "
            "global biography"
        ),
        "unchanged_receipt_order": (
            "operational object",
            "frozen assumptions",
            "restrictive exclusion",
            "formed realization",
            "permissive foil",
            "selection principle",
            "held-out discriminator",
        ),
    }


def run() -> dict[str, Any]:
    calibration = chsh_calibration()
    transfer = cross_platform_transfer()
    fixtures = calibration["fixtures"]

    rational_quantum = fixtures["rational_quantum_nonlocal"]
    withheld = fixtures["same_behavior_realization_withheld"]
    tsirelson = fixtures["tsirelson_quantum_boundary"]
    postquantum = fixtures["isotropic_postquantum"]
    pr_box = fixtures["pr_box"]

    checks = {
        "local_deterministic_has_exact_global_extension": (
            fixtures["deterministic_local"]["local_status"]
            == "LOCAL_GLOBAL_COUNTERFACTUAL_EXTENSION"
        ),
        "isotropic_half_is_exact_local_boundary": (
            fixtures["isotropic_local_boundary"]["chsh_value"] == 2
            and fixtures["isotropic_local_boundary"]["local_status"]
            == "LOCAL_GLOBAL_COUNTERFACTUAL_EXTENSION"
        ),
        "rational_quantum_realization_verifies": calibration[
            "rational_quantum_realization"
        ]["verified"],
        "rational_quantum_chsh_is_fourteen_fifths": (
            rational_quantum["chsh_value"] == q(Fraction(14, 5))
        ),
        "rational_quantum_has_exact_local_dual": (
            rational_quantum["rational_exact_marginal_receipt"]["verdict"]
            == "DUAL_OBSTRUCTION"
            and rational_quantum["rational_exact_marginal_receipt"][
                "verification"
            ]["strictly_negative_observed_value"]
        ),
        "rational_quantum_is_explicitly_realized": (
            rational_quantum["quantum_status"]
            == "EXPLICIT_QUANTUM_REALIZATION"
        ),
        "withheld_realization_preserves_behavior_digest": (
            withheld["behavior_digest"]
            == rational_quantum["behavior_digest"]
        ),
        "withheld_realization_does_not_become_quantum_proof": (
            withheld["quantum_status"] == "QUANTUM_STATUS_UNRESOLVED"
        ),
        "tsirelson_realization_verifies": calibration[
            "tsirelson_quantum_realization"
        ]["verified"],
        "tsirelson_operator_square_is_eight_on_state_support": calibration[
            "tsirelson_quantum_realization"
        ]["chsh_operator_square_is_eight_on_state_support"],
        "tsirelson_behavior_saturates_exact_bound": (
            tsirelson["chsh_value"] == q(0, 2)
            and tsirelson["tsirelson_receipt"]["saturates_bound"]
        ),
        "tsirelson_behavior_is_explicit_quantum_nonlocal": (
            tsirelson["local_status"]
            == "PROVEN_NONLOCAL_DIRECT_CHSH_WITNESS"
            and tsirelson["quantum_status"]
            == "EXPLICIT_QUANTUM_REALIZATION"
        ),
        "three_quarter_is_no_signalling_postquantum": (
            postquantum["chsh_value"] == 3
            and postquantum["no_signalling"]["no_signalling"]
            and postquantum["quantum_status"]
            == "PROVEN_POST_QUANTUM_IN_FROZEN_CHSH_SCENARIO"
        ),
        "pr_box_reaches_algebraic_four": (
            pr_box["chsh_value"] == 4
            and pr_box["no_signalling"]["no_signalling"]
        ),
        "pr_box_has_exact_local_dual": (
            pr_box["rational_exact_marginal_receipt"]["verdict"]
            == "DUAL_OBSTRUCTION"
        ),
        "pr_box_is_excluded_from_ordinary_quantum_chsh": (
            pr_box["quantum_status"]
            == "PROVEN_POST_QUANTUM_IN_FROZEN_CHSH_SCENARIO"
        ),
        "signalling_control_is_rejected_before_landscape_nesting": (
            fixtures["signalling_control"]["landscape_position"]
            == "VALID_SIGNALING_CONDITIONAL_BEHAVIOR"
        ),
        "invalid_control_is_not_classified": (
            fixtures["invalid_control"]["landscape_position"]
            == "OUTSIDE_VALID_CONDITIONAL_BEHAVIORS"
        ),
        "mismatched_quantum_receipt_is_rejected": (
            not calibration["forged_receipt_control"][
                "quantum_receipt_accepted"
            ]
            and calibration["forged_receipt_control"]["quantum_status"]
            == "PROVEN_POST_QUANTUM_IN_FROZEN_CHSH_SCENARIO"
        ),
        "chsh_landscape_card_is_complete": calibration[
            "landscape_card"
        ]["contract_complete"],
        "authenticated_transfer_card_is_complete": transfer[
            "authenticated_route_landscape"
        ]["contract_complete"],
        "authenticated_coarse_identity_is_excluded": (
            transfer["authenticated_route_landscape"]["membership_receipt"][
                "coarse_verdict"
            ]
            == "DUAL_OBSTRUCTION"
        ),
        "authenticated_provenance_process_is_realized": (
            transfer["authenticated_route_landscape"]["membership_receipt"][
                "provenance_lift_verdict"
            ]
            == "GLOBAL_EXTENSION"
        ),
        "authenticated_result_preserves_safe_rejection": (
            transfer["authenticated_route_landscape"]["membership_receipt"][
                "disposition"
            ]
            == "SAFE_REJECTION_EQUIVOCATION_PROVENANCE_FORMED"
        ),
        "quantum_transfer_card_is_complete": transfer[
            "quantum_context_landscape"
        ]["contract_complete"],
        "quantum_noncontextual_identity_is_excluded": (
            transfer["quantum_context_landscape"]["membership_receipt"][
                "noncontextual_gluing"
            ]
            == "DUAL_OBSTRUCTION"
        ),
        "quantum_context_indexed_extension_is_exact": (
            transfer["quantum_context_landscape"]["membership_receipt"][
                "context_indexed_extension"
            ]["normalization"]
            == 1
            and transfer["quantum_context_landscape"][
                "membership_receipt"
            ]["context_indexed_extension"]["all_context_marginals_exact"]
        ),
        "transfer_retains_overlap_identity_as_open_problem": (
            "warrant cross-context identity"
            in transfer["shared_open_selection_problem"]
        ),
    }
    failures = tuple(name for name, passed in checks.items() if not passed)
    return {
        "schema_version": (
            "dynamic-unity/operational-theory-landscape/v0.1"
        ),
        "run_id": (
            "RUN-20260725-075017-operational-theory-landscape"
        ),
        "claim_grade": (
            "EXACT FINITE OPERATIONAL CALIBRATION / KNOWN BELL-GPT "
            "MATHEMATICS / DYNAMIC-UNITY SELECTION PRINCIPLE OPEN"
        ),
        "theory_nesting_for_frozen_chsh_interface": (
            "LOCAL_SUBSET_OF_QUANTUM_SUBSET_OF_NO_SIGNALLING_"
            "SUBSET_OF_VALID_CONDITIONAL"
        ),
        "chsh_calibration": calibration,
        "cross_platform_transfer": transfer,
        "checks": checks,
        "check_count": len(checks),
        "failure_count": len(failures),
        "failures": failures,
        "verdict": (
            "THEORY_LANDSCAPE_RECEIPTS_SEPARATED / EXACT_CHSH_CALIBRATION "
            "PASSES / EXISTING_PROTOCOL_AND_QUANTUM_FIXTURES_TRANSFER / "
            "CERTIFIED_OVERLAP_IDENTITY_REMAINS_THE_OPEN_SELECTION_PRINCIPLE"
        ),
        "does_not_establish": (
            "new Bell, Tsirelson, GPT or contextuality mathematics",
            "general quantum-set membership compilation",
            "a generalized quantum causal theory",
            "a regional-finality quantum bound",
            "a physical overlap-identity selector",
            "information or records as fundamental",
            "a new physical law, prediction or ontology",
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
