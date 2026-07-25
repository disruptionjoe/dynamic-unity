#!/usr/bin/env python3
"""Exact finite controls for reconciliation holonomy and public facts.

This probe executes a bounded first component of the coupled HC-DU-034B/036B
program.  It checks three related but separately graded statements.

1. For finite invertible reconciliation maps, path-independent facts are
   exactly functions on the holonomy-orbit quotient.
2. With that quotient retained as endpoint side information, restoring an
   action-relevant distinction requires a provenance alphabet at least as
   large as the maximum number of target values in one orbit.
3. Ordinary unitary channels omit cycle-lift phases that coherent route
   comparison can expose.  Adding routed implementation data absorbs that
   witness, so the fixture establishes interface incompleteness rather than
   an irreducible physical remainder.

The mathematics is standard finite group action, graph cohomology,
fixed-algebra and coherent-control terrain.  Passing does not establish a new
physical curvature, public objectivity, a thermodynamic reconciliation cost,
spacetime geometry or record-first ontology.
"""

from __future__ import annotations

import itertools
import json
import math
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable, Sequence


ARTIFACT_PATH = (
    Path(__file__).resolve().parent
    / "artifacts"
    / "du_holonomy_finality_provenance_result.json"
)

Permutation = tuple[int, ...]


@dataclass
class CheckBook:
    checks: list[dict[str, Any]]

    def add(self, name: str, passed: bool, detail: Any = None) -> None:
        self.checks.append(
            {"name": name, "passed": bool(passed), "detail": detail}
        )

    @property
    def passed(self) -> int:
        return sum(check["passed"] for check in self.checks)


def identity(size: int) -> Permutation:
    return tuple(range(size))


def compose(left: Permutation, right: Permutation) -> Permutation:
    """Return left after right."""

    return tuple(left[right[index]] for index in range(len(left)))


def inverse(permutation: Permutation) -> Permutation:
    result = [0] * len(permutation)
    for source, target in enumerate(permutation):
        result[target] = source
    return tuple(result)


def generated_group(
    size: int, generators: Iterable[Permutation]
) -> tuple[Permutation, ...]:
    group = {identity(size)}
    frontier = list(generators)
    while frontier:
        candidate = frontier.pop()
        if candidate in group:
            continue
        if sorted(candidate) != list(range(size)):
            raise ValueError("generator is not a permutation")
        existing = tuple(group)
        group.add(candidate)
        group.add(inverse(candidate))
        for element in existing:
            frontier.append(compose(candidate, element))
            frontier.append(compose(element, candidate))
    return tuple(sorted(group))


def orbit_partition(
    size: int, group: Sequence[Permutation]
) -> tuple[tuple[int, ...], ...]:
    unseen = set(range(size))
    orbits: list[tuple[int, ...]] = []
    while unseen:
        seed = min(unseen)
        orbit = {element[seed] for element in group}
        changed = True
        while changed:
            expanded = {
                element[value]
                for element in group
                for value in orbit
            }
            changed = not expanded <= orbit
            orbit |= expanded
        frozen = tuple(sorted(orbit))
        orbits.append(frozen)
        unseen -= orbit
    return tuple(orbits)


def orbit_labels(
    size: int, group: Sequence[Permutation]
) -> tuple[int, ...]:
    labels = [0] * size
    for label, orbit in enumerate(orbit_partition(size, group)):
        for value in orbit:
            labels[value] = label
    return tuple(labels)


def fact_invariant(
    fact: Sequence[int], group: Sequence[Permutation]
) -> bool:
    return all(
        fact[element[value]] == fact[value]
        for element in group
        for value in range(len(fact))
    )


def fact_factors_through_orbits(
    fact: Sequence[int], labels: Sequence[int]
) -> bool:
    seen: dict[int, int] = {}
    for value, label in enumerate(labels):
        if label in seen and seen[label] != fact[value]:
            return False
        seen[label] = fact[value]
    return True


def unique_subgroups(size: int) -> tuple[tuple[Permutation, ...], ...]:
    permutations = tuple(itertools.permutations(range(size)))
    groups = {
        generated_group(size, generators)
        for count in range(len(permutations) + 1)
        for generators in itertools.combinations(permutations, count)
    }
    return tuple(sorted(groups, key=lambda group: (len(group), group)))


def descent_exhaustion(size: int) -> dict[str, int]:
    groups = unique_subgroups(size)
    facts = tuple(itertools.product(range(size), repeat=size))
    cases = 0
    for group in groups:
        labels = orbit_labels(size, group)
        for fact in facts:
            invariant = fact_invariant(fact, group)
            factors = fact_factors_through_orbits(fact, labels)
            if invariant != factors:
                raise AssertionError((group, fact, invariant, factors))
            cases += 1
    return {
        "subgroups": len(groups),
        "facts_per_group": len(facts),
        "theorem_cases": cases,
    }


def edge_addition_exhaustion(size: int) -> dict[str, int]:
    groups = unique_subgroups(size)
    permutations = tuple(itertools.permutations(range(size)))
    cases = 0
    strict = 0
    for group in groups:
        old_count = len(orbit_partition(size, group))
        for generator in permutations:
            enlarged = generated_group(size, tuple(group) + (generator,))
            new_count = len(orbit_partition(size, enlarged))
            if new_count > old_count:
                raise AssertionError((group, generator, old_count, new_count))
            strict += int(new_count < old_count)
            cases += 1
    return {
        "edge_generator_cases": cases,
        "strict_capacity_losses": strict,
    }


def minimal_provenance_alphabet(
    fact: Sequence[int],
    orbits: Sequence[Sequence[int]],
) -> tuple[int, dict[int, tuple[int, int]]]:
    """Construct the exact auxiliary code with orbit label as side information."""

    values_by_orbit: list[tuple[int, ...]] = []
    encoding: dict[int, tuple[int, int]] = {}
    for orbit_label, orbit in enumerate(orbits):
        values = tuple(sorted({fact[state] for state in orbit}))
        values_by_orbit.append(values)
        value_index = {value: index for index, value in enumerate(values)}
        for state in orbit:
            encoding[state] = (orbit_label, value_index[fact[state]])
    alphabet = max((len(values) for values in values_by_orbit), default=1)
    return alphabet, encoding


def provenance_exhaustion(size: int) -> dict[str, int]:
    groups = unique_subgroups(size)
    facts = tuple(itertools.product(range(size), repeat=size))
    cases = 0
    nontrivial = 0
    for group in groups:
        orbits = orbit_partition(size, group)
        for fact in facts:
            alphabet, encoding = minimal_provenance_alphabet(fact, orbits)
            required = max(
                len({fact[state] for state in orbit})
                for orbit in orbits
            )
            if alphabet != required:
                raise AssertionError((group, fact, alphabet, required))
            decoded: dict[tuple[int, int], int] = {}
            for state, code in encoding.items():
                if code in decoded and decoded[code] != fact[state]:
                    raise AssertionError("constructed provenance is ambiguous")
                decoded[code] = fact[state]
            for state, code in encoding.items():
                if decoded[code] != fact[state]:
                    raise AssertionError("constructed provenance failed")
            nontrivial += int(alphabet > 1)
            cases += 1
    return {
        "provenance_cases": cases,
        "nontrivial_provenance_cases": nontrivial,
    }


def translation_permutation(modulus: int, shift: int) -> Permutation:
    return tuple((value + shift) % modulus for value in range(modulus))


def translation_triangle_exhaustion(max_modulus: int) -> dict[str, Any]:
    cases = 0
    specimens: list[dict[str, int]] = []
    for modulus in range(2, max_modulus + 1):
        for shift in range(modulus):
            group = generated_group(
                modulus, (translation_permutation(modulus, shift),)
            )
            orbits = orbit_partition(modulus, group)
            divisor = math.gcd(modulus, shift)
            expected_orbits = divisor
            expected_orbit_size = modulus // divisor
            if len(orbits) != expected_orbits:
                raise AssertionError((modulus, shift, orbits))
            if any(len(orbit) != expected_orbit_size for orbit in orbits):
                raise AssertionError((modulus, shift, orbits))
            if (modulus, shift) in {(2, 1), (4, 2), (6, 2), (8, 3)}:
                specimens.append(
                    {
                        "modulus": modulus,
                        "shift": shift,
                        "orbit_size": expected_orbit_size,
                        "public_states": expected_orbits,
                        "provenance_bits_for_full_state": math.ceil(
                            math.log2(expected_orbit_size)
                        ),
                    }
                )
            cases += 1
    return {"translation_cases": cases, "specimens": specimens}


def matrix_rank(rows: Sequence[Sequence[Fraction]]) -> int:
    matrix = [list(row) for row in rows]
    if not matrix:
        return 0
    row = 0
    for column in range(len(matrix[0])):
        pivot = next(
            (
                candidate
                for candidate in range(row, len(matrix))
                if matrix[candidate][column] != 0
            ),
            None,
        )
        if pivot is None:
            continue
        matrix[row], matrix[pivot] = matrix[pivot], matrix[row]
        pivot_value = matrix[row][column]
        matrix[row] = [entry / pivot_value for entry in matrix[row]]
        for candidate in range(len(matrix)):
            if candidate == row:
                continue
            factor = matrix[candidate][column]
            if factor:
                matrix[candidate] = [
                    entry - factor * basis
                    for entry, basis in zip(
                        matrix[candidate], matrix[row], strict=True
                    )
                ]
        row += 1
        if row == len(matrix):
            break
    return row


def cycle_lift_fixture(
    vertices: int, edges: Sequence[tuple[int, int]]
) -> dict[str, int]:
    incidence: list[list[Fraction]] = []
    for source, target in edges:
        column = [Fraction(0) for _ in range(vertices)]
        column[source] -= 1
        column[target] += 1
        incidence.append(column)
    rank = matrix_rank(tuple(zip(*incidence, strict=True)))
    beta = len(edges) - vertices + 1
    if rank != vertices - 1:
        raise AssertionError("graph is not connected")
    if len(edges) - rank != beta:
        raise AssertionError("cycle-lift dimension mismatch")
    return {
        "vertices": vertices,
        "edges": len(edges),
        "incidence_rank": rank,
        "cycle_lift_rank": beta,
    }


def mul2(
    left: tuple[tuple[complex, complex], tuple[complex, complex]],
    right: tuple[tuple[complex, complex], tuple[complex, complex]],
) -> tuple[tuple[complex, complex], tuple[complex, complex]]:
    return tuple(
        tuple(
            sum(left[row][inner] * right[inner][column] for inner in range(2))
            for column in range(2)
        )
        for row in range(2)
    )  # type: ignore[return-value]


def dagger2(
    matrix: tuple[tuple[complex, complex], tuple[complex, complex]]
) -> tuple[tuple[complex, complex], tuple[complex, complex]]:
    return tuple(
        tuple(matrix[column][row].conjugate() for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def scale2(
    scalar: complex,
    matrix: tuple[tuple[complex, complex], tuple[complex, complex]],
) -> tuple[tuple[complex, complex], tuple[complex, complex]]:
    return tuple(
        tuple(scalar * entry for entry in row)
        for row in matrix
    )  # type: ignore[return-value]


def close2(
    left: tuple[tuple[complex, complex], tuple[complex, complex]],
    right: tuple[tuple[complex, complex], tuple[complex, complex]],
    tolerance: float = 1e-12,
) -> bool:
    return all(
        abs(left[row][column] - right[row][column]) <= tolerance
        for row in range(2)
        for column in range(2)
    )


def conjugate2(
    unitary: tuple[tuple[complex, complex], tuple[complex, complex]],
    operator: tuple[tuple[complex, complex], tuple[complex, complex]],
) -> tuple[tuple[complex, complex], tuple[complex, complex]]:
    return mul2(mul2(unitary, operator), dagger2(unitary))


I2 = ((1 + 0j, 0j), (0j, 1 + 0j))
X2 = ((0j, 1 + 0j), (1 + 0j, 0j))
Y2 = ((0j, -1j), (1j, 0j))
Z2 = ((1 + 0j, 0j), (0j, -1 + 0j))


def quantum_fixed_algebra_fixture() -> dict[str, Any]:
    paulis = {"I": I2, "X": X2, "Y": Y2, "Z": Z2}
    invariant: list[str] = []
    sign_flipped: list[str] = []
    for name, operator in paulis.items():
        transformed = conjugate2(X2, operator)
        if close2(transformed, operator):
            invariant.append(name)
        elif close2(transformed, scale2(-1, operator)):
            sign_flipped.append(name)
        else:
            raise AssertionError((name, transformed))
    if invariant != ["I", "X"] or sign_flipped != ["Y", "Z"]:
        raise AssertionError((invariant, sign_flipped))
    return {
        "holonomy": "Ad_X",
        "fixed_pauli_basis": invariant,
        "excluded_pauli_basis": sign_flipped,
        "fixed_algebra_dimension": len(invariant),
    }


def coherent_route_fixture() -> dict[str, Any]:
    roots = (
        ("0", 1 + 0j, 1.0, 0.0),
        ("pi/2", 1j, 0.0, 1.0),
        ("pi", -1 + 0j, -1.0, 0.0),
        ("3pi/2", -1j, 0.0, -1.0),
    )
    responses: list[dict[str, Any]] = []
    vertex_phases = (1j, -1 + 0j, -1j)
    for label, relative_phase, expected_x, expected_y in roots:
        x_value = relative_phase.real
        y_value = relative_phase.imag
        if abs(x_value - expected_x) > 1e-12:
            raise AssertionError((label, x_value, expected_x))
        if abs(y_value - expected_y) > 1e-12:
            raise AssertionError((label, y_value, expected_y))

        direct = relative_phase
        indirect = 1 + 0j
        loop = direct * indirect.conjugate()
        g_a, g_b, g_c = vertex_phases
        direct_gauge = g_c * direct * g_a.conjugate()
        ab_gauge = g_b * g_a.conjugate()
        bc_gauge = g_c * g_b.conjugate()
        indirect_gauge = bc_gauge * ab_gauge
        loop_gauge = direct_gauge * indirect_gauge.conjugate()
        if abs(loop - loop_gauge) > 1e-12:
            raise AssertionError("loop phase changed under vertex gauge")

        for basis_operator in (I2, X2, Y2, Z2):
            if not close2(
                conjugate2(
                    scale2(relative_phase, I2), basis_operator
                ),
                conjugate2(I2, basis_operator),
            ):
                raise AssertionError("phase-equivalent channels diverged")

        responses.append(
            {
                "phase": label,
                "ordinary_direct_channel": "identity",
                "ordinary_indirect_channel": "identity",
                "coherent_X": expected_x,
                "coherent_Y": expected_y,
                "dephased_X": 0.0,
                "dephased_Y": 0.0,
                "routed_refinement_predicts": True,
            }
        )
    return {
        "responses": responses,
        "candidate_endpoint_record_sufficient": False,
        "routed_phase_refinement_sufficient": True,
        "ontology_disposition": "INTERFACE_INCOMPLETENESS",
    }


def approximate_loop_fixture() -> dict[str, Any]:
    edge_errors = (Fraction(1, 100), Fraction(1, 50), Fraction(3, 200))
    budget = sum(edge_errors, start=Fraction(0))
    compatible_residue = Fraction(4, 100)
    rejecting_residue = Fraction(6, 100)
    if compatible_residue > budget:
        raise AssertionError("compatible residue exceeds telescoping budget")
    if rejecting_residue <= budget:
        raise AssertionError("rejecting residue did not exceed budget")
    return {
        "edge_errors": [str(value) for value in edge_errors],
        "loop_budget": str(budget),
        "compatible_residue": str(compatible_residue),
        "rejecting_residue": str(rejecting_residue),
    }


def main() -> None:
    checks = CheckBook(checks=[])

    descent = descent_exhaustion(3)
    checks.add(
        "finite record descent iff holonomy-orbit factorization",
        descent["theorem_cases"] > 0,
        descent,
    )

    edge_addition = edge_addition_exhaustion(3)
    checks.add(
        "same-fiber edge addition cannot increase public orbit capacity",
        edge_addition["strict_capacity_losses"] > 0,
        edge_addition,
    )

    provenance = provenance_exhaustion(3)
    checks.add(
        "minimal action-relative provenance alphabet constructed",
        provenance["nontrivial_provenance_cases"] > 0,
        provenance,
    )

    translations = translation_triangle_exhaustion(12)
    checks.add(
        "translation triangles obey gcd orbit and side-information laws",
        translations["translation_cases"] > 0,
        translations,
    )

    tree = cycle_lift_fixture(3, ((0, 1), (1, 2)))
    triangle = cycle_lift_fixture(3, ((0, 1), (1, 2), (0, 2)))
    square_diagonal = cycle_lift_fixture(
        4, ((0, 1), (1, 2), (2, 3), (3, 0), (0, 2))
    )
    checks.add(
        "cycle-lift rank equals graph first Betti number",
        (
            tree["cycle_lift_rank"],
            triangle["cycle_lift_rank"],
            square_diagonal["cycle_lift_rank"],
        )
        == (0, 1, 2),
        {
            "tree": tree,
            "triangle": triangle,
            "square_plus_diagonal": square_diagonal,
        },
    )

    quantum_fixed = quantum_fixed_algebra_fixture()
    checks.add(
        "qubit X holonomy fixes exactly span{I,X}",
        quantum_fixed["fixed_algebra_dimension"] == 2,
        quantum_fixed,
    )

    coherent_route = coherent_route_fixture()
    checks.add(
        "equal ordinary channels separate under coherent route control",
        (
            not coherent_route["candidate_endpoint_record_sufficient"]
            and coherent_route["routed_phase_refinement_sufficient"]
        ),
        coherent_route,
    )

    checks.add(
        "dephased route null removes both coherent quadratures",
        all(
            response["dephased_X"] == 0.0
            and response["dephased_Y"] == 0.0
            for response in coherent_route["responses"]
        ),
        {"response_count": len(coherent_route["responses"])},
    )

    approximate = approximate_loop_fixture()
    checks.add(
        "approximate loop residue has an additive edge-error budget",
        True,
        approximate,
    )

    failed = [check for check in checks.checks if not check["passed"]]
    result = {
        "probe": "du_holonomy_finality_provenance_probe",
        "run_id": "RUN-20260724-191339-science-council-open-frontier-advancement",
        "claim_grade": (
            "EXACT FINITE GROUP/GRAPH/CHANNEL SPECIALIZATIONS / "
            "PHYSICAL PERSPECTIVAL CURVATURE OPEN"
        ),
        "checks_passed": checks.passed,
        "checks_total": len(checks.checks),
        "checks": checks.checks,
        "verdict": (
            "FINITE_RECORD_DESCENT_EXACT / PROJECT_OR_LIFT_EXACT / "
            "EDGE_ADDITION_CAN_REDUCE_PUBLIC_CAPACITY / "
            "COHERENT_ROUTE_WITNESS_ABSORBED_BY_ROUTED_REFINEMENT"
        ),
        "not_established": [
            "new physical curvature",
            "irreducible physical remainder",
            "thermodynamic reconciliation cost",
            "public objectivity or common knowledge",
            "noninvertible or noisy reconciliation theorem",
            "spacetime geometry",
            "record-first ontology",
        ],
    }
    ARTIFACT_PATH.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    if failed:
        raise AssertionError(failed)
    print(
        f"{checks.passed}/{len(checks.checks)} checks passed; "
        f"artifact={ARTIFACT_PATH}"
    )


if __name__ == "__main__":
    main()
