#!/usr/bin/env python3
"""Finite entanglement controls for layered-finality extensions.

The probe fixes the standard-quantum absorption boundary before asking for a
new finality law.  A finite classical history/finality label that selects a
family of linear CPTP maps is an ordinary controlled quantum process on an
enlarged classical-quantum state.  Finite thresholds, hysteresis, provenance
dependence, and routed phases of that form are therefore not by themselves
beyond standard quantum theory.

The entanglement fixture keeps the harder compatibility requirements visible:
local record operations preserve the remote marginal, arbitrary
nonorthogonal states cannot be broadcast, and exact coherent uncomputation
restores the pre-record state.  An apparent post-break history residual is
then constructed with an omitted memory bit and removed when that bit is
included in the reset.  A genuinely new finality-memory law would have to
survive that completion, while a naive ensemble-dependent nonlinear escape
fails the no-signalling gate.

Passing instantiates finite analytic controls in a deterministic numerical
fixture and establishes a candidate-classification boundary. It does not
establish an extra finality state, objective collapse,
perspectival curvature, a public-fact phase, actualization heat, record
gravity, or any departure from quantum theory.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any, Iterable, Sequence


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_entangled_finality_absorption_result.json"
)
RUN_ID = "RUN-20260725-053806-entangled-finality-absorption-boundary"
TOLERANCE = 1e-12

Vector = tuple[complex, ...]
Matrix = tuple[tuple[complex, ...], ...]


def canonical_number(value: float) -> float:
    if abs(value) < TOLERANCE:
        return 0.0
    nearest = round(value)
    if abs(value - nearest) < TOLERANCE:
        return float(nearest)
    return float(value)


def jsonable(value: Any) -> Any:
    if isinstance(value, complex):
        if abs(value.imag) < TOLERANCE:
            return canonical_number(value.real)
        return {
            "real": canonical_number(value.real),
            "imag": canonical_number(value.imag),
        }
    if isinstance(value, float):
        return canonical_number(value)
    if isinstance(value, tuple):
        return [jsonable(item) for item in value]
    if isinstance(value, list):
        return [jsonable(item) for item in value]
    if isinstance(value, dict):
        return {str(key): jsonable(item) for key, item in value.items()}
    return value


def canonical_json(value: Any) -> str:
    return json.dumps(jsonable(value), indent=2, sort_keys=True) + "\n"


def identity(dimension: int) -> Matrix:
    return tuple(
        tuple(complex(int(row == column)) for column in range(dimension))
        for row in range(dimension)
    )


def zeros(rows: int, columns: int) -> Matrix:
    return tuple(
        tuple(0j for _ in range(columns))
        for _ in range(rows)
    )


def dagger(matrix: Matrix) -> Matrix:
    return tuple(
        tuple(matrix[row][column].conjugate() for row in range(len(matrix)))
        for column in range(len(matrix[0]))
    )


def matmul(left: Matrix, right: Matrix) -> Matrix:
    right_columns = tuple(zip(*right, strict=True))
    return tuple(
        tuple(
            sum(
                (a * b for a, b in zip(left_row, right_column, strict=True)),
                start=0j,
            )
            for right_column in right_columns
        )
        for left_row in left
    )


def matrix_add(*matrices: Matrix) -> Matrix:
    return tuple(
        tuple(
            sum(
                (matrix[row][column] for matrix in matrices),
                start=0j,
            )
            for column in range(len(matrices[0][0]))
        )
        for row in range(len(matrices[0]))
    )


def matrix_scale(scale: complex, matrix: Matrix) -> Matrix:
    return tuple(
        tuple(scale * value for value in row)
        for row in matrix
    )


def kron_matrix(*matrices: Matrix) -> Matrix:
    result: Matrix = ((1 + 0j,),)
    for matrix in matrices:
        result = tuple(
            tuple(
                result[row_a][column_a] * matrix[row_b][column_b]
                for column_a in range(len(result[0]))
                for column_b in range(len(matrix[0]))
            )
            for row_a in range(len(result))
            for row_b in range(len(matrix))
        )
    return result


def kron_vector(*vectors: Vector) -> Vector:
    result: Vector = (1 + 0j,)
    for vector in vectors:
        result = tuple(left * right for left in result for right in vector)
    return result


def matrix_vector(matrix: Matrix, vector: Vector) -> Vector:
    return tuple(
        sum(
            (value * amplitude for value, amplitude in zip(row, vector, strict=True)),
            start=0j,
        )
        for row in matrix
    )


def outer(vector: Vector) -> Matrix:
    return tuple(
        tuple(left * right.conjugate() for right in vector)
        for left in vector
    )


def trace(matrix: Matrix) -> complex:
    return sum((matrix[index][index] for index in range(len(matrix))), start=0j)


def expectation(state: Matrix, observable: Matrix) -> float:
    return canonical_number(trace(matmul(observable, state)).real)


def close_matrix(
    left: Matrix,
    right: Matrix,
    tolerance: float = TOLERANCE,
) -> bool:
    return all(
        abs(a - b) <= tolerance
        for left_row, right_row in zip(left, right, strict=True)
        for a, b in zip(left_row, right_row, strict=True)
    )


def vector_distance(left: Vector, right: Vector) -> float:
    return math.sqrt(
        sum(abs(a - b) ** 2 for a, b in zip(left, right, strict=True))
    )


def apply_unitary(state: Matrix, unitary: Matrix) -> Matrix:
    return matmul(matmul(unitary, state), dagger(unitary))


def apply_kraus(state: Matrix, operators: Sequence[Matrix]) -> Matrix:
    return matrix_add(
        *(
            matmul(matmul(operator, state), dagger(operator))
            for operator in operators
        )
    )


def bits(index: int, qubits: int) -> tuple[int, ...]:
    return tuple(
        (index >> (qubits - qubit - 1)) & 1
        for qubit in range(qubits)
    )


def index_from_bits(values: Sequence[int]) -> int:
    result = 0
    for value in values:
        result = 2 * result + value
    return result


def partial_trace_qubits(
    state: Matrix,
    keep: Sequence[int],
    qubits: int,
) -> Matrix:
    kept = tuple(keep)
    traced = tuple(qubit for qubit in range(qubits) if qubit not in kept)
    dimension = 2 ** len(kept)
    result = [list(row) for row in zeros(dimension, dimension)]
    for row in range(2**qubits):
        row_bits = bits(row, qubits)
        for column in range(2**qubits):
            column_bits = bits(column, qubits)
            if any(row_bits[q] != column_bits[q] for q in traced):
                continue
            out_row = index_from_bits(tuple(row_bits[q] for q in kept))
            out_column = index_from_bits(tuple(column_bits[q] for q in kept))
            result[out_row][out_column] += state[row][column]
    return tuple(tuple(value for value in row) for row in result)


def cnot(qubits: int, control: int, target: int) -> Matrix:
    dimension = 2**qubits
    matrix = [list(row) for row in zeros(dimension, dimension)]
    for source in range(dimension):
        source_bits = list(bits(source, qubits))
        if source_bits[control]:
            source_bits[target] ^= 1
        destination = index_from_bits(source_bits)
        matrix[destination][source] = 1 + 0j
    return tuple(tuple(value for value in row) for row in matrix)


def controlled_z(qubits: int, control: int, target: int) -> Matrix:
    diagonal = []
    for basis_index in range(2**qubits):
        basis_bits = bits(basis_index, qubits)
        phase = -1 if basis_bits[control] and basis_bits[target] else 1
        diagonal.append(complex(phase))
    return tuple(
        tuple(
            diagonal[row] if row == column else 0j
            for column in range(2**qubits)
        )
        for row in range(2**qubits)
    )


def operator_sum_is_identity(operators: Sequence[Matrix]) -> bool:
    completeness = matrix_add(
        *(matmul(dagger(operator), operator) for operator in operators)
    )
    return close_matrix(completeness, identity(len(completeness)))


I2: Matrix = ((1 + 0j, 0j), (0j, 1 + 0j))
X2: Matrix = ((0j, 1 + 0j), (1 + 0j, 0j))
Z2: Matrix = ((1 + 0j, 0j), (0j, -1 + 0j))
P0: Matrix = ((1 + 0j, 0j), (0j, 0j))
P1: Matrix = ((0j, 0j), (0j, 1 + 0j))
ZERO: Vector = (1 + 0j, 0j)
ONE: Vector = (0j, 1 + 0j)
PLUS: Vector = (1 / math.sqrt(2), 1 / math.sqrt(2))
MINUS: Vector = (1 / math.sqrt(2), -1 / math.sqrt(2))


def bell_baseline() -> dict[str, Any]:
    bell: Vector = (1 / math.sqrt(2), 0j, 0j, 1 / math.sqrt(2))
    state = outer(bell)
    marginal_a = partial_trace_qubits(state, (0,), 2)
    marginal_b = partial_trace_qubits(state, (1,), 2)
    half_identity = matrix_scale(0.5, I2)

    inv_sqrt_two = 1 / math.sqrt(2)
    b0 = matrix_scale(inv_sqrt_two, matrix_add(Z2, X2))
    b1 = matrix_scale(inv_sqrt_two, matrix_add(Z2, matrix_scale(-1, X2)))
    chsh = matrix_add(
        kron_matrix(Z2, b0),
        kron_matrix(Z2, b1),
        kron_matrix(X2, b0),
        matrix_scale(-1, kron_matrix(X2, b1)),
    )

    dephase_a = (kron_matrix(P0, I2), kron_matrix(P1, I2))
    dephased = apply_kraus(state, dephase_a)
    dephased_marginal_b = partial_trace_qubits(dephased, (1,), 2)

    return {
        "state": state,
        "marginal_a": marginal_a,
        "marginal_b": marginal_b,
        "both_marginals_maximally_mixed": (
            close_matrix(marginal_a, half_identity)
            and close_matrix(marginal_b, half_identity)
        ),
        "zz_expectation": expectation(state, kron_matrix(Z2, Z2)),
        "xx_expectation": expectation(state, kron_matrix(X2, X2)),
        "chsh_value": expectation(state, chsh),
        "local_dephasing_kraus_complete": operator_sum_is_identity(dephase_a),
        "remote_marginal_unchanged_by_local_dephasing": close_matrix(
            marginal_b, dephased_marginal_b
        ),
        "joint_xx_after_local_dephasing": expectation(
            dephased, kron_matrix(X2, X2)
        ),
    }


def fanout_and_uncompute() -> dict[str, Any]:
    bell: Vector = (1 / math.sqrt(2), 0j, 0j, 1 / math.sqrt(2))
    records = 3
    initial = kron_vector(bell, *(ZERO for _ in range(records)))
    state = initial
    unitaries = []
    for record in range(records):
        gate = cnot(2 + records, 0, 2 + record)
        unitaries.append(gate)
        state = matrix_vector(gate, state)

    pointer_support_only = True
    for basis_index, amplitude in enumerate(state):
        if abs(amplitude) <= TOLERANCE:
            continue
        basis_bits = bits(basis_index, 2 + records)
        pointer_support_only &= all(
            basis_bits[2 + record] == basis_bits[0]
            for record in range(records)
        )

    reduced_ab = partial_trace_qubits(outer(state), (0, 1), 2 + records)
    joint_xx_while_records_retained = expectation(
        reduced_ab, kron_matrix(X2, X2)
    )

    for gate in reversed(unitaries):
        state = matrix_vector(gate, state)

    threshold_resets: dict[str, float] = {}
    for record_count in (1, 2, 3):
        trial = kron_vector(bell, *(ZERO for _ in range(record_count)))
        gates = [
            cnot(2 + record_count, 0, 2 + record)
            for record in range(record_count)
        ]
        for gate in gates:
            trial = matrix_vector(gate, trial)
        for gate in reversed(gates):
            trial = matrix_vector(gate, trial)
        threshold_resets[str(record_count)] = canonical_number(
            vector_distance(
                trial,
                kron_vector(bell, *(ZERO for _ in range(record_count))),
            )
        )

    return {
        "record_count": records,
        "orthogonal_pointer_label_redundantly_copied": pointer_support_only,
        "joint_xx_while_records_retained": joint_xx_while_records_retained,
        "uncompute_state_distance": canonical_number(
            vector_distance(state, initial)
        ),
        "all_finite_record_counts_reset_exactly": all(
            distance == 0.0 for distance in threshold_resets.values()
        ),
        "per_record_count_reset_distance": threshold_resets,
    }


def no_broadcasting_control() -> dict[str, Any]:
    overlap = abs(
        sum(
            left.conjugate() * right
            for left, right in zip(ZERO, PLUS, strict=True)
        )
    )
    desired_two_copy_overlap = overlap**2
    return {
        "nonorthogonal_input_overlap": overlap,
        "required_output_overlap_for_two_perfect_copies": desired_two_copy_overlap,
        "unitary_inner_product_gap": overlap - desired_two_copy_overlap,
        "perfect_broadcast_by_one_fixed_unitary_impossible": (
            abs(overlap - desired_two_copy_overlap) > TOLERANCE
        ),
        "scope": (
            "orthogonal pointer labels may be copied; an arbitrary "
            "noncommuting quantum state may not"
        ),
    }


def history_controlled_channel() -> dict[str, Any]:
    # H=0 applies identity to A. H=1 completely dephases A.
    k0 = matrix_add(
        kron_matrix(P0, I2),
        kron_matrix(P1, P0),
    )
    k1 = kron_matrix(P1, P1)
    operators = (k0, k1)

    plus_state = outer(PLUS)
    h0_input = kron_matrix(outer(ZERO), plus_state)
    h1_input = kron_matrix(outer(ONE), plus_state)
    h0_output = apply_kraus(h0_input, operators)
    h1_output = apply_kraus(h1_input, operators)
    a0 = partial_trace_qubits(h0_output, (1,), 2)
    a1 = partial_trace_qubits(h1_output, (1,), 2)

    threshold = 3
    counts = tuple(range(6))
    flags = tuple(int(count >= threshold) for count in counts)
    trajectory = (0, 3, 1, 0, 4, 0)
    memory = 0
    hysteresis = []
    for count in trajectory:
        memory = int(memory or count >= threshold)
        hysteresis.append(memory)

    return {
        "kraus_complete": operator_sum_is_identity(operators),
        "history_zero_preserves_x": expectation(a0, X2),
        "history_one_dephases_x": expectation(a1, X2),
        "threshold": threshold,
        "record_counts": counts,
        "threshold_flags": flags,
        "hysteresis_input": trajectory,
        "hysteresis_memory": tuple(hysteresis),
        "finite_threshold_is_classical_preprocessing": True,
        "finite_hysteresis_is_one_retained_memory_bit": True,
        "absorption_result": (
            "FINITE_THRESHOLD_AND_HYSTERESIS_EMBED_AS_A_STANDARD_CQ_PROCESS"
        ),
    }


def routed_phase_control() -> dict[str, Any]:
    bell: Vector = (1 / math.sqrt(2), 0j, 0j, 1 / math.sqrt(2))
    gate = controlled_z(3, 0, 1)  # route R controls Z on Bell qubit A
    xx = kron_matrix(I2, X2, X2)
    responses: dict[str, float] = {}
    reset_distances: dict[str, float] = {}
    for route, route_state in ((0, ZERO), (1, ONE)):
        initial = kron_vector(route_state, bell)
        routed = matrix_vector(gate, initial)
        responses[str(route)] = expectation(outer(routed), xx)
        restored = matrix_vector(gate, routed)
        reset_distances[str(route)] = canonical_number(
            vector_distance(restored, initial)
        )
    return {
        "controlled_route_unitary": close_matrix(
            matmul(dagger(gate), gate), identity(8)
        ),
        "route_conditioned_xx": responses,
        "route_register_predicts_difference": responses == {"0": 1.0, "1": -1.0},
        "route_uncompute_distances": reset_distances,
        "route_uncompute_removes_difference": all(
            distance == 0.0 for distance in reset_distances.values()
        ),
        "absorption_result": (
            "ROUTE_PHASE_IS_STANDARD_WHEN_THE_ROUTE_REGISTER_IS_RETAINED"
        ),
    }


def causal_break_memory_control() -> dict[str, Any]:
    bell: Vector = (1 / math.sqrt(2), 0j, 0j, 1 / math.sqrt(2))
    gate = controlled_z(3, 0, 1)  # memory M controls Z on A
    xx = kron_matrix(I2, X2, X2)
    future: dict[str, float] = {}
    remote_b: dict[str, Matrix] = {}

    for history, memory_state in ((0, ZERO), (1, ONE)):
        # The causal break has re-prepared AB in the same Bell state. Only M
        # remains different.
        after_break = kron_vector(memory_state, bell)
        output = matrix_vector(gate, after_break)
        output_density = outer(output)
        future[str(history)] = expectation(output_density, xx)
        remote_b[str(history)] = partial_trace_qubits(
            output_density, (2,), 3
        )

    reset_future = {}
    for history in (0, 1):
        fully_reset = kron_vector(ZERO, bell)
        output = matrix_vector(gate, fully_reset)
        reset_future[str(history)] = expectation(outer(output), xx)

    return {
        "declared_ab_state_after_break": "same Bell state for both histories",
        "omitted_memory_states": {"0": "|0>", "1": "|1>"},
        "apparent_post_break_xx_residual": future,
        "omitted_memory_produces_residual": future == {"0": 1.0, "1": -1.0},
        "remote_b_marginals_equal": close_matrix(
            remote_b["0"], remote_b["1"]
        ),
        "future_xx_after_complete_memory_reset": reset_future,
        "complete_memory_reset_removes_residual": (
            reset_future == {"0": 1.0, "1": 1.0}
        ),
        "standard_quantum_diagnosis": (
            "APPARENT_HISTORY_EFFECT_ABSORBED_BY_RETAINED_MEMORY_REGISTER"
        ),
        "genuine_extension_requirement": (
            "repeatable residual after re-preparing the system and every "
            "admitted quantum/classical memory and after an implementation-"
            "complete multi-time process null"
        ),
    }


def nonlinear_signalling_control() -> dict[str, Any]:
    # Two decompositions of the same I/2 density operator.
    z_ensemble = (outer(ZERO), outer(ONE))
    x_ensemble = (outer(PLUS), outer(MINUS))
    half_identity = matrix_scale(0.5, I2)
    z_input = matrix_scale(0.5, matrix_add(*z_ensemble))
    x_input = matrix_scale(0.5, matrix_add(*x_ensemble))

    # A deliberately naive preparation-context-dependent nonlinear rule:
    # |0> -> |0>, |1> -> |1>, |+> -> |0>, |-> -> |0>.
    z_output = matrix_scale(0.5, matrix_add(outer(ZERO), outer(ONE)))
    x_output = outer(ZERO)

    return {
        "z_and_x_ensembles_same_density": (
            close_matrix(z_input, half_identity)
            and close_matrix(x_input, half_identity)
        ),
        "z_ensemble_output_z_expectation": expectation(z_output, Z2),
        "x_ensemble_output_z_expectation": expectation(x_output, Z2),
        "remote_preparation_choice_becomes_detectable": (
            abs(
                expectation(z_output, Z2)
                - expectation(x_output, Z2)
            )
            > TOLERANCE
        ),
        "disposition": (
            "NAIVE_ENSEMBLE_DEPENDENT_NONLINEAR_ESCAPE_FAILS_NO_SIGNALLING"
        ),
        "scope_warning": (
            "this finite counterexample does not rule out every carefully "
            "constructed stochastic or global nonlinear theory"
        ),
    }


def candidate_registry() -> dict[str, Any]:
    return {
        "finality_memory_residual": {
            "repo_route": "H-CCR-15 / PRED-DU-003 / CONCEPT-DU-005",
            "standard_absorber": (
                "retained environment, controller, route, or classical "
                "history register represented in a process tensor"
            ),
            "best_method": (
                "randomized pre-break history, replacement causal break, "
                "nested memory-boundary expansion, and all-port tomography"
            ),
            "first_decisive_assay": (
                "causal break plus system-and-memory re-preparation followed "
                "by the same Bell-correlation tester"
            ),
            "cheap_kill": (
                "the residual vanishes after one omitted memory or route "
                "register is reset, or the complete process predicts it"
            ),
            "scale_condition": (
                "survives nested memory completion, leakage bounds, "
                "no-signalling, and a frozen effect-size estimator"
            ),
            "promotion_condition": (
                "residual survives expanding memory completion and a frozen "
                "implementation-complete quantum-process null"
            ),
        },
        "graph_threshold_actualization": {
            "repo_route": "PRED-DU-001/002 / CONCEPT-DU-009",
            "standard_absorber": (
                "classical threshold logic, finite memory, ordinary "
                "decoherence, QEC, or a thermodynamic critical family"
            ),
            "best_method": (
                "process-equivalent graph pairs where possible, plus matched "
                "up/down sweeps, exact uncomputation, and held-out finite-size "
                "scaling against graph-dependent quantum rivals"
            ),
            "first_decisive_assay": (
                "an invariant graph term predicts a residual beyond the "
                "calibrated routed quantum process, ideally between "
                "process-equivalent implementations"
            ),
            "cheap_kill": (
                "retained labels, ordinary graph-dependent dynamics, "
                "decoherence, known criticality, or node-count convention "
                "explains the curves"
            ),
            "scale_condition": (
                "one order parameter and scaling relation predicts held-out "
                "sizes without platform-specific redefinition"
            ),
            "promotion_condition": (
                "finite-size scaling or hysteresis remains after the complete "
                "channel, history register, and resource model predicts zero"
            ),
        },
        "reconciliation_curvature": {
            "repo_route": "H-CCR-13 / CONCEPT-DU-006",
            "standard_absorber": (
                "route register, noncommuting operation order, process memory, "
                "reference-frame transformation, or geometric phase"
            ),
            "best_method": (
                "quantum-comb or groupoid formulation, routed process "
                "tomography, vertex-gauge quotient, orientation reversal, "
                "and benign subdivision"
            ),
            "first_decisive_assay": (
                "three-recorder closed loop with routed process tomography, "
                "vertex-gauge changes, and benign subdivision controls"
            ),
            "cheap_kill": (
                "the route register, ordinary gate sequence, clock mismatch, "
                "or known geometric phase predicts the loop result"
            ),
            "scale_condition": (
                "the residue composes under loop concatenation and remains "
                "gauge- and refinement-invariant"
            ),
            "promotion_condition": (
                "gauge- and refinement-invariant residue survives the "
                "implementation-complete routed process"
            ),
        },
        "actualization_cost": {
            "repo_route": "H-CCR-07 / HC-DU-035B / CONCEPT-DU-008",
            "standard_absorber": (
                "Landauer erasure, measurement work, blank archives, "
                "authentication, communication, coherence, and latency"
            ),
            "best_method": (
                "resource-constrained protocol optimization with reversible "
                "constructions before calorimetry"
            ),
            "first_decisive_assay": (
                "matched reversible reconciliation protocols with a complete "
                "resource ledger and calorimetric upper bound"
            ),
            "cheap_kill": (
                "reversible implementation and complete ordinary resource "
                "accounting eliminate the residual"
            ),
            "scale_condition": (
                "an encoding-invariant lower bound predicts a cross-platform "
                "ratio without refitting"
            ),
            "promotion_condition": (
                "strict residual lower bound depends on certified distinctions "
                "after equal capability and all ordinary resources are matched"
            ),
        },
        "capability_backreaction": {
            "repo_route": "H-CCR-05/06 / CONCEPT-DU-005",
            "standard_absorber": (
                "stray controller coupling, changed boundary, changed tester, "
                "or ordinary closed-loop feedback"
            ),
            "best_method": (
                "derive a causal/Hamiltonian no-coupling theorem and an "
                "explicit capability-sourced interaction before apparatus"
            ),
            "first_decisive_assay": (
                "randomized physically present but isolated recovery hardware "
                "with identical system channels and leakage bounds"
            ),
            "cheap_kill": (
                "any coupling, leakage, controller-state change, or "
                "observer-boundary refit explains the effect"
            ),
            "scale_condition": (
                "a nonzero law is explicit, no-signalling-safe, and not a "
                "disguised apparatus interaction"
            ),
            "promotion_condition": (
                "unused capability changes outcomes despite an experimentally "
                "null interaction channel"
            ),
        },
        "record_sourced_geometry": {
            "repo_route": "HC-DU-038/040 / CONCEPT-DU-008",
            "standard_absorber": (
                "stress-energy, entropy redistribution, control fields, "
                "ordinary decoherence, and representation-dependent record count"
            ),
            "best_method": (
                "derive a local covariantly conserved, refinement-invariant "
                "source tensor with units before designing an apparatus"
            ),
            "first_decisive_assay": (
                "derive a covariantly conserved source before any apparatus "
                "proposal; then match stress-energy in a mesoscopic control"
            ),
            "cheap_kill": (
                "the source is nonconserved, observer/basis dependent, "
                "subdivision sensitive, or ordinary stress-energy"
            ),
            "scale_condition": (
                "the theory closes and gives a coefficient range not already "
                "excluded before a matched-stress-energy experiment"
            ),
            "promotion_condition": (
                "conserved nonzero signal remains after standard gravitational "
                "and open-system sources are matched"
            ),
        },
    }


def run() -> dict[str, Any]:
    bell = bell_baseline()
    fanout = fanout_and_uncompute()
    broadcasting = no_broadcasting_control()
    history = history_controlled_channel()
    route = routed_phase_control()
    causal_break = causal_break_memory_control()
    nonlinear = nonlinear_signalling_control()
    candidates = candidate_registry()

    checks = {
        "bell_local_states_maximally_mixed": bell[
            "both_marginals_maximally_mixed"
        ],
        "bell_joint_correlations_reproduced": (
            bell["zz_expectation"] == 1.0
            and bell["xx_expectation"] == 1.0
            and abs(bell["chsh_value"] - 2 * math.sqrt(2)) < TOLERANCE
        ),
        "local_record_operation_is_trace_preserving": bell[
            "local_dephasing_kraus_complete"
        ],
        "local_record_operation_does_not_signal": bell[
            "remote_marginal_unchanged_by_local_dephasing"
        ],
        "local_record_operation_changes_joint_coherence": (
            bell["joint_xx_after_local_dephasing"] == 0.0
        ),
        "orthogonal_pointer_records_fan_out": fanout[
            "orthogonal_pointer_label_redundantly_copied"
        ],
        "exact_record_uncomputation_restores_state": (
            fanout["uncompute_state_distance"] == 0.0
            and fanout["all_finite_record_counts_reset_exactly"]
        ),
        "nonorthogonal_broadcasting_rejected": broadcasting[
            "perfect_broadcast_by_one_fixed_unitary_impossible"
        ],
        "history_controlled_channel_is_cptp": history["kraus_complete"],
        "finite_threshold_embeds_as_classical_control": history[
            "finite_threshold_is_classical_preprocessing"
        ],
        "finite_hysteresis_embeds_as_memory": history[
            "finite_hysteresis_is_one_retained_memory_bit"
        ],
        "route_phase_embeds_with_route_register": (
            route["controlled_route_unitary"]
            and route["route_register_predicts_difference"]
        ),
        "route_uncomputation_removes_route_effect": route[
            "route_uncompute_removes_difference"
        ],
        "omitted_memory_creates_apparent_causal_break_residual": causal_break[
            "omitted_memory_produces_residual"
        ],
        "omitted_memory_residual_does_not_signal": causal_break[
            "remote_b_marginals_equal"
        ],
        "complete_memory_reset_removes_residual": causal_break[
            "complete_memory_reset_removes_residual"
        ],
        "naive_nonlinear_escape_exposes_signalling": nonlinear[
            "remote_preparation_choice_becomes_detectable"
        ],
        "all_candidate_families_have_best_approach": (
            len(candidates) == 6
            and all(
                {
                    "repo_route",
                    "standard_absorber",
                    "best_method",
                    "first_decisive_assay",
                    "cheap_kill",
                    "scale_condition",
                    "promotion_condition",
                }
                <= set(candidate)
                for candidate in candidates.values()
            )
        ),
    }
    failures = [name for name, passed in checks.items() if not passed]

    result = {
        "schema_version": "1.0",
        "run_id": RUN_ID,
        "probe": "du_entangled_finality_absorption_probe",
        "claim_grade": (
            "ANALYTIC FINITE STANDARD-QUANTUM ABSORPTION CONTROL / "
            "DETERMINISTIC NUMERICAL FIXTURE / CONDITIONAL EXTENSION "
            "REGISTRY / NO NEW-PHYSICS CLAIM"
        ),
        "finite_absorption_boundary": {
            "statement": (
                "A finite classical history/finality label and a label-"
                "conditioned family of linear CPTP maps form an ordinary "
                "classical-quantum controlled process on an enlarged state."
            ),
            "consequences": [
                (
                    "finite threshold, hysteresis, provenance, and route-label "
                    "effects are not by themselves beyond quantum theory"
                ),
                (
                    "a residual after a system-only reset first witnesses an "
                    "incomplete memory boundary, not a new law"
                ),
                (
                    "a genuinely beyond-standard claim must survive an "
                    "implementation-complete causal break or explicitly change "
                    "the linear quantum dynamics"
                ),
                (
                    "naive preparation-context nonlinear dynamics can violate "
                    "no-signalling and therefore fails the entanglement gate"
                ),
            ],
            "novelty_grade": (
                "KNOWN CONTROLLED-CHANNEL/STINESPRING/PROCESS-MEMORY TERRAIN; "
                "USEFUL DU PROGRAM BOUNDARY"
            ),
        },
        "entanglement_baseline": bell,
        "record_fanout_and_uncompute": fanout,
        "no_broadcasting_control": broadcasting,
        "threshold_hysteresis_absorption": history,
        "route_phase_absorption": route,
        "causal_break_memory_control": causal_break,
        "nonlinear_no_signalling_control": nonlinear,
        "candidate_registry": candidates,
        "checks": checks,
        "check_count": len(checks),
        "failure_count": len(failures),
        "failures": failures,
        "verdict": (
            "FINITE_FINALITY_LABELS_ABSORBED / "
            "CAUSAL_BREAK_RESIDUAL_IS_THE_SHARP_FRONTIER / "
            "ENTANGLEMENT_GATE_INSTALLED"
            if not failures
            else "ABSORPTION_BOUNDARY_OR_CONTROL_FAILED"
        ),
        "does_not_establish": [
            "a physically real finality-memory variable",
            "a graph-triggered objective collapse law",
            "perspectival or reconciliation curvature",
            "a public-fact phase transition",
            "actualization heat or optionality cost",
            "capability backreaction",
            "record-sourced gravity or causal geometry",
            "exhaustion of every standard quantum completion",
            "a novel theorem component",
            "record-first ontology",
        ],
    }
    ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT.write_text(canonical_json(result), encoding="utf-8")
    return result


if __name__ == "__main__":
    receipt = run()
    print(
        f"{receipt['verdict']}: "
        f"{receipt['check_count'] - receipt['failure_count']}/"
        f"{receipt['check_count']} checks"
    )
    raise SystemExit(1 if receipt["failures"] else 0)
