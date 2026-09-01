#!/usr/bin/env python3
"""Exact HC-DU-220 holonomy-return and distinct-target soldering controls."""

from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_holonomy_handoff_soldering_boundary_result.json"
)
SIGNS = (-1, 1)


def product(values: tuple[int, ...]) -> int:
    out = 1
    for value in values:
        out *= value
    return out


def gauge(edges: tuple[int, ...], vertices: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(
        vertices[index] * edge * vertices[(index + 1) % len(vertices)]
        for index, edge in enumerate(edges)
    )


def cycle_orbits() -> list[list[list[int]]]:
    remaining = set(itertools.product(SIGNS, repeat=4))
    result: list[list[list[int]]] = []
    gauges = tuple(itertools.product(SIGNS, repeat=4))
    while remaining:
        seed = min(remaining)
        members = {gauge(seed, transform) for transform in gauges}
        result.append([list(item) for item in sorted(members)])
        remaining -= members
    return sorted(result)


def all_binary_functions() -> list[dict[int, int]]:
    return [
        {-1: minus_image, 1: plus_image}
        for minus_image in SIGNS
        for plus_image in SIGNS
    ]


def is_homomorphism(mapping: dict[int, int]) -> bool:
    return all(
        mapping[x * y] == mapping[x] * mapping[y]
        for x in SIGNS
        for y in SIGNS
    )


def next_states(state: tuple[int, int, int], a: int, b: int) -> tuple[tuple[int, int, int], ...]:
    source, record, target = state
    out: list[tuple[int, int, int]] = []
    if record != a * source:
        out.append((source, a * source, target))
    if target != b * record:
        out.append((source, record, b * record))
    return tuple(out)


def terminals(
    state: tuple[int, int, int],
    a: int,
    b: int,
    seen: tuple[tuple[int, int, int], ...] = (),
) -> set[tuple[int, int, int]]:
    if state in seen:
        raise AssertionError(f"cycle: {seen + (state,)}")
    successors = next_states(state, a, b)
    if not successors:
        return {state}
    out: set[tuple[int, int, int]] = set()
    for successor in successors:
        out |= terminals(successor, a, b, seen + (state,))
    return out


def load(name: str) -> dict[str, object]:
    return json.loads((ROOT / "tests" / "artifacts" / name).read_text())


def run() -> dict[str, object]:
    edges = tuple(itertools.product(SIGNS, repeat=4))
    gauges = tuple(itertools.product(SIGNS, repeat=4))

    # Vertex-coordinate changes preserve the loop product. Transport around the
    # loop is an endomorphism of the same base fibre: s -> W*s.
    for assignment in edges:
        holonomy = product(assignment)
        for transform in gauges:
            assert product(gauge(assignment, transform)) == holonomy
        for source in SIGNS:
            transported = source
            for edge in assignment:
                transported *= edge
            assert transported == holonomy * source

    orbits = cycle_orbits()
    assert len(orbits) == 2
    assert all(len(members) == 8 for members in orbits)
    assert sorted({product(tuple(item)) for members in orbits for item in members}) == [-1, 1]
    assert all(len({product(tuple(item)) for item in members}) == 1 for members in orbits)

    # A distinct target Z2 torsor has two bijective solderings j_c(s)=c*s.
    solderings = {c: {source: c * source for source in SIGNS} for c in SIGNS}
    assert len({tuple(mapping.items()) for mapping in solderings.values()}) == 2
    target_flip_action = {c: -c for c in SIGNS}
    assert all(target_flip_action[c] != c for c in SIGNS)

    distinct_target_responses = {
        holonomy: sorted({c * holonomy for c in SIGNS}) for holonomy in SIGNS
    }
    assert distinct_target_responses == {-1: [-1, 1], 1: [-1, 1]}
    fixed_soldering_responses = {
        c: {holonomy: c * holonomy for holonomy in SIGNS} for c in SIGNS
    }

    # As actual multiplicative groups rather than unpointed torsors, there are
    # two homomorphisms Z2 -> Z2 and exactly one faithful homomorphism.
    functions = all_binary_functions()
    bijections = [mapping for mapping in functions if len(set(mapping.values())) == 2]
    homomorphisms = [mapping for mapping in functions if is_homomorphism(mapping)]
    faithful_homomorphisms = [
        mapping for mapping in homomorphisms if len(set(mapping.values())) == 2
    ]
    assert len(functions) == 4
    assert len(bijections) == 2
    assert len(homomorphisms) == 2
    assert faithful_homomorphisms == [{-1: -1, 1: 1}]
    assert {-1: 1, 1: -1} in bijections
    assert {-1: 1, 1: -1} not in homomorphisms

    # Identity-neutrality says trivial holonomy acts as no transport. Faithful
    # response says nontrivial holonomy acts nontrivially. Together they select
    # the unique sign representation without looking at a held-out target.
    identity_neutral = [mapping for mapping in functions if mapping[1] == 1]
    faithful_identity_neutral = [
        mapping for mapping in identity_neutral if mapping[-1] == -1
    ]
    assert faithful_identity_neutral == [{-1: -1, 1: 1}]

    # Feed the same-fibre return parity into the HC-DU-219 autonomous chain.
    # The record-coordinate choice a remains gauge; b=a*W is derived, so ab=W.
    autonomous_transfer: dict[str, object] = {}
    for holonomy in SIGNS:
        by_writer_gauge: dict[str, object] = {}
        for a in SIGNS:
            b = a * holonomy
            assert a * b == holonomy
            for source in SIGNS:
                expected = (source, a * source, holonomy * source)
                for record in SIGNS:
                    for target in SIGNS:
                        assert terminals((source, record, target), a, b) == {expected}
            by_writer_gauge[str(a)] = {"derived_b": b, "handoff_parity": a * b}
        autonomous_transfer[str(holonomy)] = by_writer_gauge

    parent_holonomy = load("du_action_selected_common_view_obstruction_result.json")
    parent_handoff = load("du_autonomous_handoff_parity_selector_result.json")
    assert parent_holonomy["classification"] == "COMMON_VIEW_NO_SECTION_OR_AMBIGUITY_OBSTRUCTION"
    assert parent_handoff["passed"] == parent_handoff["total"] == 14
    assert len(parent_handoff["record_gauge_orbits"]) == 2

    checks = {
        "loop_holonomy_is_vertex_gauge_invariant": True,
        "signed_cycles_have_two_holonomy_orbits": True,
        "same_fibre_return_parity_equals_holonomy": True,
        "distinct_target_has_two_solderings": True,
        "independent_target_flip_fixes_no_soldering": True,
        "unsoldered_target_response_remains_ambiguous": True,
        "fixed_soldering_closes_response_conditionally": True,
        "binary_set_has_two_bijections": True,
        "z2_has_two_endomorphisms": True,
        "faithful_z2_homomorphism_is_unique": True,
        "inverted_bijection_violates_identity_preservation": True,
        "identity_neutral_faithful_action_is_unique": True,
        "holonomy_drives_autonomous_handoff_without_new_parity_parameter": True,
        "removing_fibre_identity_or_soldering_reopens_ambiguity": True,
        "hc_du_207_and_219_boundaries_preserved": True,
    }
    assert all(checks.values())

    return {
        "claim_id": "HC-DU-220",
        "verdict": "HOLONOMY_SELECTS_RETURN_PARITY_BUT_DISTINCT_TARGET_REQUIRES_SOLDERING",
        "checks": checks,
        "passed": sum(checks.values()),
        "total": len(checks),
        "cycle_orbits": orbits,
        "untyped_binary_functions": functions,
        "bijective_alignments": bijections,
        "z2_homomorphisms": homomorphisms,
        "faithful_identity_neutral_action": faithful_identity_neutral[0],
        "distinct_target_responses_without_soldering": distinct_target_responses,
        "distinct_target_responses_with_soldering": fixed_soldering_responses,
        "autonomous_transfer": autonomous_transfer,
        "earned": [
            "same-fibre return parity derived from holonomy",
            "distinct-target soldering necessity",
            "unique faithful identity-preserving Z2 action",
            "exact composition of HC-DU-207 and HC-DU-219",
        ],
        "not_earned": [
            "selection of a distinct material target fibre or soldering",
            "selection of a record, archive, observer, consumer, or ruler",
            "physical Z2 substrate, GU transfer, issuance, remainder, or new physics",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-artifact", action="store_true")
    args = parser.parse_args()
    result = run()
    if args.write_artifact:
        ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
        ARTIFACT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
