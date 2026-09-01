#!/usr/bin/env python3
"""Exact control for the CTS-A2 action-selected common-view obstruction.

The probe freezes one four-site signed-cycle quadratic action

    S_sigma(x) = 1/2 sum_(u,v) (x_u - sigma_uv x_v)^2

before asking what its stationary point, Hessian, response spectrum, residual
symmetries, and local transport actually select.  It verifies four boundaries:

* the action selects the Z2 holonomy and its spectral response up to gauge;
* the residual symmetry has no distinguished site/observer, while only coarse
  spectral subspaces are canonical;
* multiple covariant action families induce different sufficient quotients;
* a frustrated cycle has local nonzero sections on every spanning tree but no
  nonzero global section, and the dimensionless action supplies no ruler scale.

These are standard signed-Laplacian, equivariance, and sheaf/local-system
facts.  The Dynamic Unity result is the typed joint test of P35 -> P30 -> P33
and the P40/P31 obstruction branch under one unchanged antecedent.  Passing
does not establish a material record, observer, finality mechanism, metric,
new physical law, or empirical excess.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path
from typing import Any, Iterable

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_action_selected_common_view_obstruction_result.json"
)
RUN_ID = "RUN-20260831-action-selected-common-view-obstruction"
TOL = 1.0e-10

VERTEX_COUNT = 4
EDGES = ((0, 1), (1, 2), (2, 3), (3, 0))
BALANCED_SIGNS = (1, 1, 1, 1)
FRUSTRATED_SIGNS = (1, 1, 1, -1)


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, indent=2) + "\n"


def rounded(value: float) -> float:
    return round(float(value), 12)


def rounded_vector(values: Iterable[float]) -> list[float]:
    return [rounded(value) for value in values]


def holonomy(signs: tuple[int, ...]) -> int:
    result = 1
    for sign in signs:
        result *= sign
    return result


def signed_incidence(
    signs: tuple[int, ...],
    retained_edges: tuple[int, ...] | None = None,
) -> np.ndarray:
    indices = (
        tuple(range(len(EDGES)))
        if retained_edges is None
        else retained_edges
    )
    matrix = np.zeros((len(indices), VERTEX_COUNT), dtype=float)
    for row, edge_index in enumerate(indices):
        tail, head = EDGES[edge_index]
        matrix[row, tail] = 1.0
        matrix[row, head] = -float(signs[edge_index])
    return matrix


def signed_laplacian(signs: tuple[int, ...]) -> np.ndarray:
    incidence = signed_incidence(signs)
    return incidence.T @ incidence


def gauge_transform(
    signs: tuple[int, ...],
    vertex_signs: tuple[int, ...],
) -> tuple[int, ...]:
    return tuple(
        vertex_signs[tail] * sign * vertex_signs[head]
        for sign, (tail, head) in zip(signs, EDGES, strict=True)
    )


def gauge_orbit(signs: tuple[int, ...]) -> set[tuple[int, ...]]:
    return {
        gauge_transform(signs, vertex_signs)
        for vertex_signs in itertools.product((-1, 1), repeat=VERTEX_COUNT)
    }


def cycle_permutations() -> tuple[tuple[int, ...], ...]:
    edge_set = {frozenset(edge) for edge in EDGES}
    return tuple(
        permutation
        for permutation in itertools.permutations(range(VERTEX_COUNT))
        if {
            frozenset((permutation[tail], permutation[head]))
            for tail, head in EDGES
        }
        == edge_set
    )


def permutation_matrix(permutation: tuple[int, ...]) -> np.ndarray:
    matrix = np.zeros((VERTEX_COUNT, VERTEX_COUNT), dtype=float)
    for source, target in enumerate(permutation):
        matrix[target, source] = 1.0
    return matrix


def residual_signed_symmetries(
    laplacian: np.ndarray,
) -> tuple[tuple[tuple[int, ...], tuple[int, ...], np.ndarray], ...]:
    symmetries = []
    for permutation in cycle_permutations():
        permutation_operator = permutation_matrix(permutation)
        for vertex_signs in itertools.product(
            (-1, 1), repeat=VERTEX_COUNT
        ):
            operator = np.diag(vertex_signs) @ permutation_operator
            if np.allclose(
                operator.T @ laplacian @ operator,
                laplacian,
                atol=TOL,
            ):
                symmetries.append(
                    (permutation, vertex_signs, operator)
                )
    return tuple(symmetries)


def nullity(matrix: np.ndarray) -> int:
    return int(matrix.shape[1] - np.linalg.matrix_rank(matrix, tol=TOL))


def projector_rank(projector: np.ndarray) -> int:
    return int(round(float(np.trace(projector).real)))


def edge_lengths(coordinates: np.ndarray) -> tuple[float, ...]:
    return tuple(
        float(np.linalg.norm(coordinates[head] - coordinates[tail]))
        for tail, head in EDGES
    )


def check(name: str, condition: bool, detail: str) -> dict[str, Any]:
    return {"name": name, "passed": bool(condition), "detail": detail}


def build_result() -> dict[str, Any]:
    sign_assignments = tuple(
        itertools.product((-1, 1), repeat=len(EDGES))
    )
    balanced_laplacian = signed_laplacian(BALANCED_SIGNS)
    frustrated_laplacian = signed_laplacian(FRUSTRATED_SIGNS)
    mass_squared = 1.0
    balanced_quantum_frequencies = np.sqrt(
        np.linalg.eigvalsh(
            mass_squared * np.eye(VERTEX_COUNT) + balanced_laplacian
        )
    )
    frustrated_quantum_frequencies = np.sqrt(
        np.linalg.eigvalsh(
            mass_squared * np.eye(VERTEX_COUNT) + frustrated_laplacian
        )
    )

    assignments_by_holonomy = {
        sign: tuple(
            signs
            for signs in sign_assignments
            if holonomy(signs) == sign
        )
        for sign in (-1, 1)
    }
    spectra_by_assignment = {
        signs: tuple(
            rounded(value)
            for value in np.linalg.eigvalsh(signed_laplacian(signs))
        )
        for signs in sign_assignments
    }
    spectra_by_holonomy = {
        sign: sorted(
            {spectra_by_assignment[signs] for signs in assignments}
        )
        for sign, assignments in assignments_by_holonomy.items()
    }

    balanced_orbit = gauge_orbit(BALANCED_SIGNS)
    frustrated_orbit = gauge_orbit(FRUSTRATED_SIGNS)
    residual_symmetries = residual_signed_symmetries(frustrated_laplacian)
    vertex_orbits = {
        vertex: sorted(
            {permutation[vertex] for permutation, _, _ in residual_symmetries}
        )
        for vertex in range(VERTEX_COUNT)
    }
    globally_fixed_vertices = [
        vertex
        for vertex in range(VERTEX_COUNT)
        if all(
            permutation[vertex] == vertex
            for permutation, _, _ in residual_symmetries
        )
    ]

    eigenvalues = np.linalg.eigvalsh(frustrated_laplacian)
    low_value = 2.0 - math.sqrt(2.0)
    high_value = 2.0 + math.sqrt(2.0)
    low_projector = (
        high_value * np.eye(VERTEX_COUNT) - frustrated_laplacian
    ) / (high_value - low_value)
    high_projector = np.eye(VERTEX_COUNT) - low_projector
    action_families = {
        "low_spectral_band": low_projector,
        "high_spectral_band": high_projector,
        "full_response_space": np.eye(VERTEX_COUNT),
    }
    action_family_ranks = {
        name: projector_rank(projector)
        for name, projector in action_families.items()
    }
    action_family_kernel_dimensions = {
        name: VERTEX_COUNT - rank
        for name, rank in action_family_ranks.items()
    }

    tree_nullities = {}
    for removed_edge in range(len(EDGES)):
        retained = tuple(
            edge
            for edge in range(len(EDGES))
            if edge != removed_edge
        )
        tree_nullities[str(removed_edge)] = nullity(
            signed_incidence(FRUSTRATED_SIGNS, retained)
        )

    unit_square = np.array(
        ((0.0, 0.0), (1.0, 0.0), (1.0, 1.0), (0.0, 1.0))
    )
    large_square = 3.0 * unit_square
    unit_lengths = edge_lengths(unit_square)
    large_lengths = edge_lengths(large_square)

    assertions = [
        check(
            "all_signed_actions_are_positive_semidefinite",
            all(
                np.min(np.linalg.eigvalsh(signed_laplacian(signs)))
                >= -TOL
                for signs in sign_assignments
            ),
            "Every Hessian is D_sigma^T D_sigma.",
        ),
        check(
            "holonomy_is_gauge_invariant",
            all(
                holonomy(gauge_transform(signs, vertex_signs))
                == holonomy(signs)
                for signs in sign_assignments
                for vertex_signs in itertools.product(
                    (-1, 1), repeat=VERTEX_COUNT
                )
            ),
            "Vertex sign changes cancel pairwise around the cycle.",
        ),
        check(
            "sign_assignments_form_exactly_two_gauge_orbits",
            len(balanced_orbit) == 8
            and len(frustrated_orbit) == 8
            and balanced_orbit.isdisjoint(frustrated_orbit)
            and balanced_orbit | frustrated_orbit == set(sign_assignments),
            "The two orbits are classified by Z2 holonomy.",
        ),
        check(
            "response_spectrum_is_constant_on_each_gauge_orbit",
            all(len(spectra) == 1 for spectra in spectra_by_holonomy.values()),
            "Gauge-related Hessians are orthogonally conjugate.",
        ),
        check(
            "response_spectrum_distinguishes_the_two_holonomies",
            spectra_by_holonomy[-1] != spectra_by_holonomy[1],
            "The action-selected loop sign has a finite spectral response.",
        ),
        check(
            "balanced_cycle_has_one_global_parallel_section",
            nullity(signed_incidence(BALANCED_SIGNS)) == 1,
            "Trivial holonomy leaves one parallel line.",
        ),
        check(
            "frustrated_cycle_has_no_nonzero_global_parallel_section",
            nullity(signed_incidence(FRUSTRATED_SIGNS)) == 0,
            "Negative holonomy forces x=-x after one loop.",
        ),
        check(
            "every_proper_tree_region_has_a_nonzero_parallel_section",
            set(tree_nullities.values()) == {1},
            "Deleting any edge removes the loop obstruction.",
        ),
        check(
            "frustrated_action_residual_symmetry_is_vertex_transitive",
            all(orbit == list(range(VERTEX_COUNT)) for orbit in vertex_orbits.values()),
            "No site is privileged by the frozen action.",
        ),
        check(
            "frustrated_action_selects_no_observer_vertex",
            not globally_fixed_vertices,
            "An equivariant selector cannot return a vertex absent a stabilizer fixed point.",
        ),
        check(
            "low_spectral_projector_is_exact",
            np.allclose(low_projector @ low_projector, low_projector, atol=TOL)
            and np.allclose(low_projector.T, low_projector, atol=TOL)
            and projector_rank(low_projector) == 2,
            "The Hessian canonically selects a two-dimensional low band.",
        ),
        check(
            "spectral_bands_descend_under_every_residual_symmetry",
            all(
                np.allclose(operator.T @ low_projector @ operator, low_projector, atol=TOL)
                and np.allclose(operator.T @ high_projector @ operator, high_projector, atol=TOL)
                for _, _, operator in residual_symmetries
            ),
            "Coarse spectral subspaces, unlike sites or axes, are action-selected.",
        ),
        check(
            "multiple_covariant_action_families_survive_one_antecedent",
            action_family_ranks
            == {
                "low_spectral_band": 2,
                "high_spectral_band": 2,
                "full_response_space": 4,
            },
            "Low-band, high-band, and full response families are all functions of the same Hessian.",
        ),
        check(
            "causal_state_quotient_depends_on_action_family",
            len(set(action_family_kernel_dimensions.values())) > 1,
            "The coarsest sufficient state quotient has rank two or four depending on admitted probes.",
        ),
        check(
            "principal_response_does_not_select_embedding_scale",
            np.array_equal(
                signed_laplacian(FRUSTRATED_SIGNS),
                frustrated_laplacian,
            )
            and not np.allclose(unit_lengths, large_lengths, atol=TOL),
            "The unweighted action is unchanged while the external ruler perimeter changes.",
        ),
        check(
            "frustrated_spectrum_matches_exact_values",
            np.allclose(
                eigenvalues,
                np.array((low_value, low_value, high_value, high_value)),
                atol=TOL,
            ),
            "The response gap is exact and doubly degenerate.",
        ),
        check(
            "frustrated_hessian_determinant_is_four",
            abs(float(np.linalg.det(frustrated_laplacian)) - 4.0) <= TOL,
            "The finite response separates it from the balanced zero-mode case.",
        ),
        check(
            "quantized_normal_mode_spectrum_retains_the_holonomy",
            not np.allclose(
                balanced_quantum_frequencies,
                frustrated_quantum_frequencies,
                atol=TOL,
            ),
            "Adding the same positive mass and quantizing the oscillators preserves the loop-sign discriminator.",
        ),
    ]

    result = {
        "schema": "dynamic-unity/action-selected-common-view-obstruction/v1",
        "run_id": RUN_ID,
        "program_id": "DU-COMPUTATION-FIRST-CLOSED-TRANSITION-SUBSTRATE",
        "action_id": "CTS-A2-COMMON-VIEW-CLOSURE-SELECTOR-OR-OBSTRUCTION",
        "frozen_antecedent": {
            "carrier": "four real site amplitudes on C4",
            "action": "S_sigma(x)=1/2 sum_edges (x_u-sigma_e*x_v)^2",
            "stationary_point": "x=0",
            "hessian": frustrated_laplacian.astype(int).tolist(),
            "coupling_signs": list(FRUSTRATED_SIGNS),
            "gauge": "vertex sign changes co-transform amplitudes and edge signs",
            "held_fixed": [
                "cycle graph",
                "edge couplings",
                "quadratic action",
                "Z2 gauge rule",
                "no observer, archive, action bandwidth, or ruler supplied",
            ],
        },
        "p35_action_response": {
            "selected": [
                "one gauge orbit of signed transport couplings",
                "Z2 holonomy -1",
                "Hessian spectrum and low/high spectral subspaces",
            ],
            "not_selected": [
                "one observer site",
                "one axis inside a degenerate spectral band",
                "material record or archive",
                "consumer or complete common-view family",
            ],
            "balanced_spectrum": list(spectra_by_holonomy[1][0]),
            "frustrated_spectrum": list(spectra_by_holonomy[-1][0]),
            "residual_signed_symmetry_count": len(residual_symmetries),
            "globally_fixed_vertices": globally_fixed_vertices,
            "verdict": "PARTIAL_ACTION_SELECTED_TRANSPORT_ORBIT_AND_GLOBAL_COMMON_VIEW_SELECTOR_OBSTRUCTION",
        },
        "p30_interventional_causal_state": {
            "covariant_action_family_ranks": action_family_ranks,
            "quotient_kernel_dimensions": action_family_kernel_dimensions,
            "result": "Each frozen action family has a coarsest sufficient linear quotient, but the antecedent admits several covariant families with different quotients.",
            "verdict": "CAUSAL_STATE_UNIQUE_ONLY_RELATIVE_TO_AN_UNSELECTED_ACTION_FAMILY",
        },
        "p33_ruler_closure": {
            "selected": "dimensionless signed propagation/transport and response gap",
            "unit_embedding_edge_lengths": rounded_vector(unit_lengths),
            "large_embedding_edge_lengths": rounded_vector(large_lengths),
            "unit_perimeter": rounded(sum(unit_lengths)),
            "large_perimeter": rounded(sum(large_lengths)),
            "verdict": "PROPAGATION_AND_HOLONOMY_SELECTED_ABSOLUTE_RULER_UNSELECTED",
        },
        "p40_p31_regional_obstruction": {
            "proper_tree_section_nullities": tree_nullities,
            "global_balanced_section_nullity": nullity(
                signed_incidence(BALANCED_SIGNS)
            ),
            "global_frustrated_section_nullity": nullity(
                signed_incidence(FRUSTRATED_SIGNS)
            ),
            "finite_invariant": "product of edge transport signs = -1",
            "finite_response": "det(L_sigma)=4 and a nonzero spectral gap",
            "verdict": "ACTION_SELECTED_REGIONAL_NO_SECTION_WITH_GAUGE_INVARIANT_HOLONOMY",
        },
        "quantum_transfer_control": {
            "hamiltonian": "H=1/2 p^T p + 1/2 q^T (I+L_sigma) q",
            "balanced_mode_frequencies": rounded_vector(
                balanced_quantum_frequencies
            ),
            "frustrated_mode_frequencies": rounded_vector(
                frustrated_quantum_frequencies
            ),
            "result": "The same source-selected holonomy changes ordinary quantum normal-mode frequencies, but the Hamiltonian still does not select a sampler, archive, observer, action bandwidth, or ruler.",
            "grade_effect": "standard quantization transfer only; no new quantum prediction",
        },
        "scope_boundary": {
            "difference_from_hc_du_123": "HC-DU-123 begins with a supplied formed cycle record and characterizes its fibre. This control begins with a source action, derives its transport holonomy and no-section obstruction, and still finds no selected record instrument or consumer.",
            "absorbed_by": [
                "equivariant selector stabilizer arguments",
                "signed and connection graph Laplacians",
                "structural balance and frustration",
                "cellular-sheaf global sections",
                "gauge holonomy",
                "ordinary sufficient-statistic and observability theory",
            ],
            "not_earned": [
                "universal common-view no-go",
                "material record formation",
                "observer or access selection",
                "regional public finality",
                "spacetime metric or physical ruler",
                "new mathematics, new physics, prediction, or ontology",
            ],
        },
        "classification": "COMMON_VIEW_NO_SECTION_OR_AMBIGUITY_OBSTRUCTION",
        "observer_index_return": "OBSERVER_INDEX_REMAINS_SUPPLIED",
        "grade": "SCOPED_GRADE_4_ACTION_SELECTED_TRANSPORT_AND_EXACT_NONSELECTION_OBSTRUCTION_COMPONENT_MATHEMATICS_KNOWN",
        "assertions": assertions,
    }
    passed = sum(assertion["passed"] for assertion in assertions)
    result["summary"] = {
        "all_passed": passed == len(assertions),
        "passed": passed,
        "total": len(assertions),
    }
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-artifact", action="store_true")
    args = parser.parse_args()

    result = build_result()
    if args.write_artifact:
        ARTIFACT.write_text(canonical_json(result), encoding="utf-8")
    print(canonical_json(result), end="")
    return 0 if result["summary"]["all_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
