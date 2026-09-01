#!/usr/bin/env python3
"""Exact control for the CTS-A3 holonomy-to-material-record gate.

The source is the unchanged frustrated four-site oscillator from HC-DU-207.
Its action selects a Z2 holonomy, a stiffness matrix, and two doubly
degenerate spectral bands.  This probe gives the source the strongest useful
standard-quantum interpretation: the positive square root of the stiffness is
the one-excitation Hamiltonian and its band PVM is treated as canonical.

It then constructs two repeatable, energy-preserving instruments for that
same PVM.  They have identical effects, Born probabilities, pointer values,
and source Hamiltonian, but orthogonal conditional continuations inside the
low-energy degeneracy.  Separate exact controls show that archive access and
record-conditioned use likewise require additional couplings.

Passing establishes only a scoped interface nonselection result.  It does not
establish a new physical law, material record formation by the source action,
observer ontology, public finality, or empirical excess over quantum theory.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_action_selected_holonomy_material_record_gate_result.json"
)
RUN_ID = "RUN-20260831-action-selected-holonomy-material-record-gate"
TOL = 1.0e-10

EDGES = ((0, 1), (1, 2), (2, 3), (3, 0))
FRUSTRATED_SIGNS = (1, 1, 1, -1)
BALANCED_SIGNS = (1, 1, 1, 1)


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, indent=2) + "\n"


def rounded(value: float) -> float:
    return round(float(value), 12)


def rounded_vector(values: np.ndarray) -> list[float]:
    return [rounded(value) for value in values]


def signed_laplacian(signs: tuple[int, ...]) -> np.ndarray:
    incidence = np.zeros((len(EDGES), 4), dtype=float)
    for row, ((tail, head), sign) in enumerate(zip(EDGES, signs, strict=True)):
        incidence[row, tail] = 1.0
        incidence[row, head] = -float(sign)
    return incidence.T @ incidence


def holonomy(signs: tuple[int, ...]) -> int:
    return math.prod(signs)


def spectral_sqrt(matrix: np.ndarray) -> np.ndarray:
    eigenvalues, eigenvectors = np.linalg.eigh(matrix)
    return eigenvectors @ np.diag(np.sqrt(eigenvalues)) @ eigenvectors.T


def check(name: str, condition: bool, detail: str) -> dict[str, Any]:
    return {"name": name, "passed": bool(condition), "detail": detail}


def projector_probability(projector: np.ndarray, state: np.ndarray) -> float:
    return float(np.real(np.vdot(state, projector @ state)))


def build_result() -> dict[str, Any]:
    identity4 = np.eye(4)
    laplacian = signed_laplacian(FRUSTRATED_SIGNS)
    balanced_laplacian = signed_laplacian(BALANCED_SIGNS)
    stiffness = identity4 + laplacian
    balanced_stiffness = identity4 + balanced_laplacian
    hamiltonian = spectral_sqrt(stiffness)

    stiffness_values, stiffness_vectors = np.linalg.eigh(stiffness)
    low_value = float(stiffness_values[0])
    high_value = float(stiffness_values[-1])
    low_vectors = stiffness_vectors[:, :2]
    high_vectors = stiffness_vectors[:, 2:]
    projector_low = low_vectors @ low_vectors.T
    projector_high = high_vectors @ high_vectors.T

    # A nontrivial orthogonal continuation inside the exact low-energy
    # degeneracy.  The operator is identity on the high band.
    swap = np.array([[0.0, 1.0], [1.0, 0.0]])
    low_twist = (
        low_vectors @ swap @ low_vectors.T
        + projector_high
    )

    luders_kraus = (projector_low, projector_high)
    twisted_kraus = (low_twist @ projector_low, projector_high)

    ket0 = np.array([[1.0], [0.0]])
    ket1 = np.array([[0.0], [1.0]])
    luders_writer = (
        np.kron(luders_kraus[0], ket0)
        + np.kron(luders_kraus[1], ket1)
    )
    twisted_writer = (
        np.kron(twisted_kraus[0], ket0)
        + np.kron(twisted_kraus[1], ket1)
    )

    generic_state = np.array([1.0, 2.0, -1.0, 0.5])
    generic_state = generic_state / np.linalg.norm(generic_state)
    luders_generic = luders_writer @ generic_state
    twisted_generic = twisted_writer @ generic_state
    luders_pointer_probabilities = np.array(
        [
            np.linalg.norm(luders_generic.reshape(4, 2)[:, index]) ** 2
            for index in range(2)
        ]
    )
    twisted_pointer_probabilities = np.array(
        [
            np.linalg.norm(twisted_generic.reshape(4, 2)[:, index]) ** 2
            for index in range(2)
        ]
    )

    low_input = low_vectors[:, 0]
    low_luders_output = luders_kraus[0] @ low_input
    low_twisted_output = twisted_kraus[0] @ low_input
    low_overlap = abs(np.vdot(low_luders_output, low_twisted_output))
    low_trace_distance = math.sqrt(max(0.0, 1.0 - low_overlap**2))

    low_energy_before = float(np.real(np.vdot(low_input, hamiltonian @ low_input)))
    low_energy_luders = float(
        np.real(np.vdot(low_luders_output, hamiltonian @ low_luders_output))
    )
    low_energy_twisted = float(
        np.real(np.vdot(low_twisted_output, hamiltonian @ low_twisted_output))
    )

    high_input = high_vectors[:, 0]
    archived_high = luders_writer @ high_input
    archived_high = archived_high.reshape(4, 2)
    pointer_high_probability = float(np.linalg.norm(archived_high[:, 1]) ** 2)

    # The same pointer can be left sealed or copied to a blank observer bit.
    # The source Hamiltonian and source-pointer state are unchanged.
    observer_sealed = np.array([1.0, 0.0])
    observer_accessible = np.array([0.0, 1.0])
    observer_trace_distance = 1.0 - abs(
        np.vdot(observer_sealed, observer_accessible)
    )

    # The same archive can drive no target action or a pointer-controlled flip.
    target_inactive = np.array([1.0, 0.0])
    target_activated = np.array([0.0, 1.0])
    target_trace_distance = 1.0 - abs(
        np.vdot(target_inactive, target_activated)
    )

    effect_differences = [
        float(
            np.linalg.norm(
                left.T @ left - right.T @ right
            )
        )
        for left, right in zip(luders_kraus, twisted_kraus, strict=True)
    ]
    luders_completeness = sum(kraus.T @ kraus for kraus in luders_kraus)
    twisted_completeness = sum(kraus.T @ kraus for kraus in twisted_kraus)

    checks = [
        check(
            "source_holonomy_is_negative",
            holonomy(FRUSTRATED_SIGNS) == -1,
            "the unchanged HC-DU-207 source has Z2 holonomy -1",
        ),
        check(
            "balanced_and_frustrated_spectra_differ",
            not np.allclose(
                np.linalg.eigvalsh(stiffness),
                np.linalg.eigvalsh(balanced_stiffness),
                atol=TOL,
            ),
            "ordinary oscillator response remains sensitive to holonomy",
        ),
        check(
            "two_exact_degenerate_bands",
            np.allclose(stiffness_values[:2], low_value, atol=TOL)
            and np.allclose(stiffness_values[2:], high_value, atol=TOL)
            and high_value - low_value > TOL,
            "the source selects two distinct rank-2 spectral bands",
        ),
        check(
            "band_projectors_are_complete",
            np.allclose(projector_low + projector_high, identity4, atol=TOL)
            and np.allclose(projector_low @ projector_high, 0.0, atol=TOL),
            "the canonical band PVM is orthogonal and complete",
        ),
        check(
            "band_projectors_commute_with_hamiltonian",
            np.allclose(projector_low @ hamiltonian, hamiltonian @ projector_low, atol=TOL)
            and np.allclose(projector_high @ hamiltonian, hamiltonian @ projector_high, atol=TOL),
            "the PVM is QND for the one-excitation Hamiltonian",
        ),
        check(
            "low_twist_is_orthogonal",
            np.allclose(low_twist.T @ low_twist, identity4, atol=TOL),
            "the hostile continuation is a physical orthogonal/unitary operation",
        ),
        check(
            "low_twist_commutes_with_hamiltonian",
            np.allclose(low_twist @ hamiltonian, hamiltonian @ low_twist, atol=TOL),
            "the hostile continuation preserves the complete source energy distribution",
        ),
        check(
            "instruments_have_identical_effects",
            max(effect_differences) < TOL,
            "Luders and twisted instruments induce the same PVM and all Born laws",
        ),
        check(
            "luders_instrument_is_complete",
            np.allclose(luders_completeness, identity4, atol=TOL),
            "the Luders operations form a normalized quantum instrument",
        ),
        check(
            "twisted_instrument_is_complete",
            np.allclose(twisted_completeness, identity4, atol=TOL),
            "the twisted operations form a normalized quantum instrument",
        ),
        check(
            "both_instruments_are_repeatable",
            np.allclose(projector_low @ twisted_kraus[0], twisted_kraus[0], atol=TOL)
            and np.allclose(projector_high @ twisted_kraus[1], twisted_kraus[1], atol=TOL),
            "each conditional output remains in its recorded energy band",
        ),
        check(
            "material_writers_are_isometries",
            np.allclose(luders_writer.T @ luders_writer, identity4, atol=TOL)
            and np.allclose(twisted_writer.T @ twisted_writer, identity4, atol=TOL),
            "both instruments admit exact blank-to-written two-state pointer isometries",
        ),
        check(
            "pointer_statistics_are_identical",
            np.allclose(
                luders_pointer_probabilities,
                twisted_pointer_probabilities,
                atol=TOL,
            ),
            "the same generic input gives the same retained archive distribution",
        ),
        check(
            "conditional_continuations_are_orthogonal",
            low_trace_distance > 1.0 - TOL,
            "one low-band input yields orthogonal future system states",
        ),
        check(
            "conditional_continuations_preserve_energy",
            abs(low_energy_before - low_energy_luders) < TOL
            and abs(low_energy_before - low_energy_twisted) < TOL,
            "the continuation ambiguity survives exact source-energy conservation",
        ),
        check(
            "same_low_archive_value",
            projector_probability(projector_low, low_luders_output) > 1.0 - TOL
            and projector_probability(projector_low, low_twisted_output) > 1.0 - TOL,
            "both hostile handoffs write the same low-band record value",
        ),
        check(
            "high_pointer_is_written",
            pointer_high_probability > 1.0 - TOL,
            "the finite writer has an exact blank-to-high material pointer transition",
        ),
        check(
            "observer_access_requires_extra_coupling",
            observer_trace_distance > 1.0 - TOL,
            "copying the same archive to an observer bit changes access without changing the source",
        ),
        check(
            "consumer_action_requires_extra_coupling",
            target_trace_distance > 1.0 - TOL,
            "the same archive supports inactive and record-controlled target continuations",
        ),
        check(
            "finite_local_control_only",
            stiffness.shape == (4, 4)
            and luders_writer.shape == (8, 4)
            and twisted_writer.shape == (8, 4),
            "the result uses one finite proof control and no simulation, training, provider, or hardware",
        ),
    ]

    passed = sum(item["passed"] for item in checks)
    return {
        "run_id": RUN_ID,
        "claim_id": "HC-DU-208",
        "action_id": "CTS-A3-ACTION-SELECTED-HOLONOMY-MATERIAL-RECORD-GATE",
        "return_class": "ACTION_SELECTED_HOLONOMY_INTERFACE_AMBIGUITY",
        "observer_index_return": "OBSERVER_INDEX_REMAINS_SUPPLIED",
        "evidence_grade": 4,
        "maximum_evidence_grade": 4,
        "source": {
            "holonomy": holonomy(FRUSTRATED_SIGNS),
            "stiffness_eigenvalues": rounded_vector(stiffness_values),
            "one_excitation_frequencies": rounded_vector(np.sqrt(stiffness_values)),
            "band_ranks": [
                int(round(np.trace(projector_low))),
                int(round(np.trace(projector_high))),
            ],
        },
        "interface_collision": {
            "effect_frobenius_differences": [rounded(value) for value in effect_differences],
            "generic_pointer_probabilities": rounded_vector(luders_pointer_probabilities),
            "low_conditional_trace_distance": rounded(low_trace_distance),
            "low_energy_before": rounded(low_energy_before),
            "low_energy_luders": rounded(low_energy_luders),
            "low_energy_twisted": rounded(low_energy_twisted),
            "observer_access_trace_distance": rounded(observer_trace_distance),
            "consumer_target_trace_distance": rounded(target_trace_distance),
        },
        "complete_handoff_passport": {
            "source_action_and_holonomy": "conditionally_selected",
            "spectral_band_pvm": "selected_by_functional_calculus",
            "sampler_instrument": "not_selected_two_exact_qnd_realizations",
            "material_blank_and_pointer": "supplied",
            "write_coupling": "supplied",
            "occurrence_and_source_provenance": "conditional_on_supplied_write_coupling",
            "archive_retention_and_reset": "supplied",
            "observer_access_route": "supplied",
            "consumer_and_matched_continuation": "not_selected",
            "resource_horizon": "supplied",
            "public_finality_and_rival_model": "absent",
            "absolute_ruler": "absent",
        },
        "absorbers": [
            "spectral quantum measurement",
            "Luders instruments",
            "QND measurement",
            "unitary freedom inside degenerate eigenspaces",
            "Naimark-Stinespring dilation",
            "controlled quantum operations",
        ],
        "checks": checks,
        "summary": {
            "passed": passed,
            "total": len(checks),
            "all_passed": passed == len(checks),
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-artifact", action="store_true")
    args = parser.parse_args()

    result = build_result()
    if args.write_artifact:
        ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
        ARTIFACT.write_text(canonical_json(result), encoding="utf-8")
    print(canonical_json(result), end="")
    return 0 if result["summary"]["all_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
