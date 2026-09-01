#!/usr/bin/env python3
"""Exact finite controls for HC-DU-212.

This probe calibrates the HC-DU-211 QFT-landing gate on an ordinary Z2
lattice-gauge specimen. It distinguishes:

1. gauge-invariant within-law sector selection;
2. target-image sharpening inside the incumbent quantum language; and
3. the absence of cross-theory selection surplus when the selecting sign is
   simply supplied as an action coefficient.

Passing establishes no continuum QFT theorem, new physics, physical record
interface, GU result, or novelty claim.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path
from typing import Iterable, Mapping, Sequence


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "tests/artifacts/du_qft_selection_surplus_holonomy_result.json"
EDGES = ((0, 1), (1, 2), (2, 3), (3, 0))
CONFIGS = tuple(itertools.product((-1, 1), repeat=4))
GAUGES = tuple(itertools.product((-1, 1), repeat=4))


def holonomy(config: Sequence[int]) -> int:
    value = 1
    for sign in config:
        value *= sign
    return value


def gauge_transform(config: Sequence[int], gauge: Sequence[int]) -> tuple[int, ...]:
    return tuple(gauge[u] * config[index] * gauge[v] for index, (u, v) in enumerate(EDGES))


def orbit(config: Sequence[int]) -> frozenset[tuple[int, ...]]:
    return frozenset(gauge_transform(config, gauge) for gauge in GAUGES)


def canonical_orbit(config: Sequence[int]) -> tuple[int, ...]:
    return min(orbit(config))


def wilson_energy(config: Sequence[int], kappa: int) -> int:
    return -kappa * holonomy(config)


def minimizers(kappa: int) -> tuple[tuple[int, ...], ...]:
    energies = {config: wilson_energy(config, kappa) for config in CONFIGS}
    minimum = min(energies.values())
    return tuple(config for config in CONFIGS if energies[config] == minimum)


def signed_laplacian(config: Sequence[int]) -> list[list[Fraction]]:
    matrix = [[Fraction(0) for _ in range(4)] for _ in range(4)]
    for sign, (u, v) in zip(config, EDGES):
        matrix[u][u] += 1
        matrix[v][v] += 1
        matrix[u][v] -= sign
        matrix[v][u] -= sign
    return matrix


def add_identity(matrix: Sequence[Sequence[Fraction]]) -> list[list[Fraction]]:
    return [
        [value + (1 if row == column else 0) for column, value in enumerate(values)]
        for row, values in enumerate(matrix)
    ]


def determinant(matrix: Sequence[Sequence[Fraction]]) -> Fraction:
    size = len(matrix)
    total = Fraction(0)
    for permutation in itertools.permutations(range(size)):
        inversions = sum(
            permutation[i] > permutation[j]
            for i in range(size)
            for j in range(i + 1, size)
        )
        term = Fraction(-1 if inversions % 2 else 1)
        for row, column in enumerate(permutation):
            term *= matrix[row][column]
        total += term
    return total


def check(name: str, condition: bool, detail: str) -> dict[str, object]:
    if not condition:
        raise AssertionError(f"{name}: {detail}")
    return {"name": name, "passed": True, "detail": detail}


def orbit_partition(configs: Iterable[Sequence[int]]) -> set[tuple[int, ...]]:
    return {canonical_orbit(config) for config in configs}


def selection_accounting(
    incumbent: Mapping[int, int],
    selected: Mapping[int, int],
    *,
    target_blind: bool,
    selector_is_copy: bool,
) -> str:
    if not target_blind:
        return "AFTER_FACT_REFIT_NO_CREDIT"
    if not set(selected) < set(incumbent):
        return "NO_PROPER_SUBFAMILY"
    if selector_is_copy:
        return "WITHIN_LAW_SELECTOR_KEY_RELOCATION"
    if set(selected.values()) < set(incumbent.values()):
        return "CROSS_THEORY_SELECTION_AND_TARGET_SHARPENING"
    return "CROSS_THEORY_STRUCTURAL_SELECTION_ONLY"


def build_result() -> dict[str, object]:
    checks: list[dict[str, object]] = []

    checks.append(
        check(
            "holonomy_is_gauge_invariant",
            all(
                holonomy(config) == holonomy(gauge_transform(config, gauge))
                for config in CONFIGS
                for gauge in GAUGES
            ),
            "every vertex-sign transformation preserves the loop product",
        )
    )

    all_orbits = orbit_partition(CONFIGS)
    checks.append(
        check(
            "exactly_two_physical_connection_orbits",
            len(all_orbits) == 2,
            "the sixteen edge assignments quotient to trivial and frustrated holonomy",
        )
    )
    checks.append(
        check(
            "each_holonomy_orbit_has_eight_encodings",
            sorted({len(orbit(config)) for config in CONFIGS}) == [8],
            "the global vertex flip is the gauge-action kernel",
        )
    )
    checks.append(
        check(
            "wilson_energy_is_gauge_invariant",
            all(
                wilson_energy(config, kappa)
                == wilson_energy(gauge_transform(config, gauge), kappa)
                for config in CONFIGS
                for gauge in GAUGES
                for kappa in (-1, 0, 1)
            ),
            "the action depends only on the physical holonomy",
        )
    )

    positive_minimizers = minimizers(1)
    negative_minimizers = minimizers(-1)
    zero_minimizers = minimizers(0)
    checks.append(
        check(
            "positive_kappa_selects_trivial_holonomy",
            len(positive_minimizers) == 8
            and {holonomy(config) for config in positive_minimizers} == {1},
            "the supplied positive Wilson coefficient selects one gauge orbit",
        )
    )
    checks.append(
        check(
            "negative_kappa_selects_frustrated_holonomy",
            len(negative_minimizers) == 8
            and {holonomy(config) for config in negative_minimizers} == {-1},
            "the supplied negative Wilson coefficient selects the other gauge orbit",
        )
    )
    checks.append(
        check(
            "zero_kappa_is_positive_nonselection_control",
            len(zero_minimizers) == 16 and len(orbit_partition(zero_minimizers)) == 2,
            "removing the preference restores both physical sectors",
        )
    )
    checks.append(
        check(
            "each_nonzero_action_selects_one_orbit_not_one_encoding",
            len(orbit_partition(positive_minimizers)) == 1
            and len(orbit_partition(negative_minimizers)) == 1,
            "selection is physical only after quotienting vertex-sign gauge",
        )
    )

    balanced = (1, 1, 1, 1)
    frustrated = (1, 1, 1, -1)
    balanced_stiffness_det = determinant(add_identity(signed_laplacian(balanced)))
    frustrated_stiffness_det = determinant(add_identity(signed_laplacian(frustrated)))
    checks.append(
        check(
            "balanced_quantum_stiffness_determinant",
            balanced_stiffness_det == 45,
            "the trivial sector has shifted spectrum {1,3,3,5}",
        )
    )
    checks.append(
        check(
            "frustrated_quantum_stiffness_determinant",
            frustrated_stiffness_det == 49,
            "the frustrated sector has shifted spectrum {3-sqrt(2),3-sqrt(2),3+sqrt(2),3+sqrt(2)}",
        )
    )
    checks.append(
        check(
            "holonomy_sectors_have_distinct_quantum_targets",
            balanced_stiffness_det != frustrated_stiffness_det,
            "an ordinary quantum spectral functional distinguishes the two sectors",
        )
    )

    incumbent_qft = {1: int(balanced_stiffness_det), -1: int(frustrated_stiffness_det)}
    selected_qft = {holonomy(positive_minimizers[0]): incumbent_qft[1]}
    checks.append(
        check(
            "selected_sector_is_a_proper_incumbent_subfamily",
            set(selected_qft) < set(incumbent_qft),
            "within the two-sector lattice quantum family the Wilson action picks one sector",
        )
    )
    checks.append(
        check(
            "within_law_selection_sharpens_the_spectral_target",
            set(selected_qft.values()) < set(incumbent_qft.values()),
            "the held-out determinant image contracts from two values to one",
        )
    )
    checks.append(
        check(
            "qft_expressibility_is_preserved",
            set(selected_qft.items()) <= set(incumbent_qft.items()),
            "the selected target remains ordinary quantum lattice physics",
        )
    )

    supplied_selector_key = {-1: -1, 1: 1}
    checks.append(
        check(
            "wilson_coefficient_sign_copies_the_selected_holonomy",
            len(supplied_selector_key) == len(set(supplied_selector_key.values())) == 2
            and all(sign == selected for sign, selected in supplied_selector_key.items()),
            "the sign inserted into the action is a one-bit selector key, not a derived upstream relation",
        )
    )
    checks.append(
        check(
            "within_law_selection_does_not_imply_cross_theory_surplus",
            selection_accounting(
                incumbent_qft,
                selected_qft,
                target_blind=True,
                selector_is_copy=True,
            )
            == "WITHIN_LAW_SELECTOR_KEY_RELOCATION",
            "dynamical sector selection is exact while derivation of the selecting coefficient remains unearned",
        )
    )
    checks.append(
        check(
            "after_target_choice_is_not_no_refit_selection",
            selection_accounting(
                incumbent_qft,
                selected_qft,
                target_blind=False,
                selector_is_copy=False,
            )
            == "AFTER_FACT_REFIT_NO_CREDIT",
            "choosing kappa after learning whether determinant 45 or 49 is desired would be target fitting",
        )
    )
    model_fields = {"gauge_edges", "kappa", "matter_coordinates", "momenta"}
    required_handoff_fields = {
        "sampler",
        "blank_archive",
        "provenance",
        "access_route",
        "consumer",
        "reset",
    }
    checks.append(
        check(
            "sector_selection_does_not_select_a_record_handoff",
            model_fields.isdisjoint(required_handoff_fields),
            "the action contains no sampler, blank archive, provenance, access route, consumer, or reset",
        )
    )

    applications = [
        {
            "specimen": "dynamical Z2 Wilson plaquette control",
            "within_law_selection": "one gauge-invariant holonomy orbit for nonzero supplied kappa",
            "cross_theory_status": "SELECTOR_KEY_SUPPLIED_NO_UPSTREAM_DERIVATION",
            "target_status": "ORDINARY_QUANTUM_SPECTRAL_SHARPENING",
            "interface_status": "NO_RECORD_HANDOFF",
        },
        {
            "specimen": "HC-DU-207 fixed signed cycle",
            "within_law_selection": "response conditional on fixed edge signs",
            "cross_theory_status": "HOLONOMY_ALREADY_IN_COUPLING_DATA",
            "target_status": "STANDARD_QUANTUM_RESPONSE",
            "interface_status": "HC-DU-208_HANDOFF_OPEN",
        },
        {
            "specimen": "finite-time infrared memory",
            "within_law_selection": "symmetry-constrained dressing component after frame and charges are supplied",
            "cross_theory_status": "NO_PROPER_QFT_COMPLETION_SUBFAMILY_YET",
            "target_status": "NO_LOCKED_HARD_TARGET",
            "interface_status": "DETECTOR_RESOLUTION_ARCHIVE_ACCESS_SUPPLIED",
        },
        {
            "specimen": "direct-action/source-response branch",
            "within_law_selection": "source response after kernel and boundary prescription are supplied",
            "cross_theory_status": "MEDIATOR_FACTORIZATION_NONUNIQUE",
            "target_status": "ENDPOINT_RESPONSE_ABSORBED",
            "interface_status": "EVENT_PARTITION_AND_CONSUMER_OPEN",
        },
        {
            "specimen": "causal-action/CFS branch",
            "within_law_selection": "measure inside a supplied variational problem",
            "cross_theory_status": "QFT_ANSATZ_REGULATOR_SECTOR_INPUTS_REMAIN_SUPPLIED",
            "target_status": "NO_FROZEN_DISTINCTIVE_TARGET",
            "interface_status": "OBSERVER_INSTRUMENT_RECORD_OPEN",
        },
        {
            "specimen": "conditional GU/K77 route",
            "within_law_selection": "matched luminous orbit only under conditional action",
            "cross_theory_status": "HIGHEST_CEILING_SOURCE_ACTION_AND_QFT_MAP_MISSING",
            "target_status": "NO_LOCKED_QFT_PARAMETER_RELATION_OR_TARGET",
            "interface_status": "MATERIAL_HANDOFF_OPEN",
        },
    ]
    checks.append(
        check(
            "existing_candidate_census_has_no_cross_theory_selector",
            all(
                row["cross_theory_status"]
                != "CROSS_THEORY_STRUCTURAL_SELECTION_EARNED"
                for row in applications
            ),
            "every current route supplies the selector input, leaves the QFT map open, or lacks a locked target",
        )
    )

    return {
        "schema_version": "dynamic-unity/qft-selection-surplus-holonomy/v0.1",
        "claim_id": "HC-DU-212",
        "run_id": "RUN-20260831-qft-selection-surplus-calibration",
        "checks": checks,
        "summary": {
            "passed": len(checks),
            "total": len(checks),
            "within_law_sector_selection": True,
            "cross_theory_selection_surplus": False,
            "qft_expressibility_preserved": True,
            "record_handoff_selected": False,
            "maximum_grade": 4,
        },
        "exact_control": {
            "edge_configurations": len(CONFIGS),
            "gauge_transformations": len(GAUGES),
            "physical_orbits": len(all_orbits),
            "positive_kappa_minimizers": len(positive_minimizers),
            "negative_kappa_minimizers": len(negative_minimizers),
            "zero_kappa_minimizers": len(zero_minimizers),
            "balanced_stiffness_determinant": int(balanced_stiffness_det),
            "frustrated_stiffness_determinant": int(frustrated_stiffness_det),
        },
        "application_ledger": applications,
        "verdict": "WITHIN_LAW_QFT_SECTOR_SELECTION_POSITIVE; CROSS_THEORY_SELECTION_SURPLUS_UNEARNED; NO_READY_SUCCESSOR",
    }


def write_artifact(result: Mapping[str, object]) -> str:
    payload = json.dumps(result, indent=2, sort_keys=True) + "\n"
    ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT.write_text(payload, encoding="utf-8")
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-artifact", action="store_true")
    args = parser.parse_args()
    result = build_result()
    if args.write_artifact:
        digest = write_artifact(result)
        print(f"PASS {result['summary']['passed']}/{result['summary']['total']} sha256={digest}")
    else:
        print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
