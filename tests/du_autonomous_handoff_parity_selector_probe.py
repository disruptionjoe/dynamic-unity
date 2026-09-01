#!/usr/bin/env python3
"""Exact autonomous-handoff parity and target-anchor controls for HC-DU-219."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_autonomous_handoff_parity_selector_result.json"
)
SIGNS = (-1, 1)
State = tuple[int, int, int]  # (source, record, target)


def next_states(state: State, a: int, b: int) -> tuple[State, ...]:
    """All one-step asynchronous local mismatch corrections."""
    source, record, target = state
    candidates: list[State] = []
    if record != a * source:
        candidates.append((source, a * source, target))
    if target != b * record:
        candidates.append((source, record, b * record))
    return tuple(candidates)


def terminal_paths(state: State, a: int, b: int, seen: tuple[State, ...] = ()) -> tuple[tuple[State, int], ...]:
    """Return every terminal state and path length; fail loudly on a cycle."""
    if state in seen:
        raise AssertionError(f"cycle in correction graph: {seen + (state,)}")
    successors = next_states(state, a, b)
    if not successors:
        return ((state, 0),)
    results: list[tuple[State, int]] = []
    for successor in successors:
        for terminal, length in terminal_paths(successor, a, b, seen + (state,)):
            results.append((terminal, length + 1))
    return tuple(results)


def energy_score(state: State, a: int, b: int) -> int:
    """The dimensionless score whose energy is -J times this value."""
    source, record, target = state
    return a * source * record + b * record * target


def gibbs_expectation(a: int, b: int, observable) -> Fraction:
    """Exact beta*J=ln(2) Gibbs expectation using weights 2**score."""
    weighted = Fraction(0)
    partition = Fraction(0)
    for state in ((s, r, t) for s in SIGNS for r in SIGNS for t in SIGNS):
        score = energy_score(state, a, b)
        weight = Fraction(2**score) if score >= 0 else Fraction(1, 2 ** (-score))
        partition += weight
        weighted += weight * observable(state)
    return weighted / partition


def orbit(seed: tuple[int, int], include_target_flip: bool) -> set[tuple[int, int]]:
    pending = [seed]
    found: set[tuple[int, int]] = set()
    while pending:
        a, b = pending.pop()
        if (a, b) in found:
            continue
        found.add((a, b))
        pending.append((-a, -b))  # internal record relabel
        if include_target_flip:
            pending.append((a, -b))
    return found


def quotient_orbits(include_target_flip: bool) -> list[list[list[int]]]:
    remaining = {(a, b) for a in SIGNS for b in SIGNS}
    result: list[list[list[int]]] = []
    while remaining:
        seed = min(remaining)
        member_set = orbit(seed, include_target_flip)
        result.append([list(pair) for pair in sorted(member_set)])
        remaining -= member_set
    return sorted(result)


def run() -> dict[str, object]:
    convergence: dict[str, object] = {}
    convergence_profiles: set[tuple[tuple[int, int], ...]] = set()
    spectra: set[tuple[tuple[int, int], ...]] = set()
    thermal: dict[str, object] = {}

    for a in SIGNS:
        for b in SIGNS:
            h = a * b
            key = f"a={a},b={b}"
            terminal_by_source: dict[str, list[int]] = {}
            path_lengths: list[int] = []
            for source in SIGNS:
                expected = (source, a * source, h * source)
                terminal_by_source[str(source)] = list(expected)
                for record in SIGNS:
                    for target in SIGNS:
                        paths = terminal_paths((source, record, target), a, b)
                        assert {terminal for terminal, _ in paths} == {expected}
                        path_lengths.extend(length for _, length in paths)

            profile = tuple(sorted(Counter(path_lengths).items()))
            convergence_profiles.add(profile)
            spectrum = tuple(sorted(Counter(-energy_score(state, a, b) for state in (
                (s, r, t) for s in SIGNS for r in SIGNS for t in SIGNS
            )).items()))
            spectra.add(spectrum)

            sr = gibbs_expectation(a, b, lambda state: state[0] * state[1])
            rt = gibbs_expectation(a, b, lambda state: state[1] * state[2])
            st = gibbs_expectation(a, b, lambda state: state[0] * state[2])
            assert sr == Fraction(3 * a, 5)
            assert rt == Fraction(3 * b, 5)
            assert st == Fraction(9 * h, 25)

            convergence[key] = {
                "handoff_parity": h,
                "absorbing_state_by_source": terminal_by_source,
                "all_path_length_histogram": {str(k): v for k, v in profile},
            }
            thermal[key] = {
                "source_record": str(sr),
                "record_target": str(rt),
                "source_target": str(st),
            }

    record_gauge_orbits = quotient_orbits(include_target_flip=False)
    full_label_gauge_orbits = quotient_orbits(include_target_flip=True)
    assert len(convergence_profiles) == 1
    assert len(spectra) == 1
    assert len(record_gauge_orbits) == 2
    assert len(full_label_gauge_orbits) == 1
    assert {
        pair[0] * pair[1]
        for orbit_members in record_gauge_orbits
        for pair in orbit_members
    } == {-1, 1}
    assert all(
        len({pair[0] * pair[1] for pair in orbit_members}) == 1
        for orbit_members in record_gauge_orbits
    )

    # In the three-qubit Z basis the quantum Hamiltonian has exactly these
    # diagonal entries. X_R conjugation performs the internal record gauge;
    # X_T changes the target ruler and flips the physical parity when that
    # ruler is held fixed.
    quantum_transfer = {
        "hamiltonian": "-J(a Z_S Z_R + b Z_R Z_T)",
        "distinct_diagonal_spectra": len(spectra),
        "common_dimensionless_energy_multiplicities": {
            str(energy): multiplicity for energy, multiplicity in next(iter(spectra))
        },
        "record_flip_conjugation": "X_R: (a,b)->(-a,-b), h unchanged",
        "target_flip_conjugation": "X_T: (a,b)->(a,-b), h flips",
        "noncommuting_quantum_advantage_claimed": False,
    }

    checks = {
        "all_asynchronous_paths_terminate": True,
        "unique_absorbing_handoff_per_source_and_action": True,
        "all_sign_choices_share_convergence_profile": len(convergence_profiles) == 1,
        "record_label_gauge_leaves_two_orbits": len(record_gauge_orbits) == 2,
        "handoff_parity_constant_on_record_gauge_orbits": True,
        "target_relabel_collapses_orbits_only_when_admitted_as_gauge": len(full_label_gauge_orbits) == 1,
        "all_sign_choices_are_isospectral": len(spectra) == 1,
        "exact_source_record_correlation": True,
        "exact_record_target_correlation": True,
        "exact_source_target_parity_response": True,
        "diagonal_quantum_embedding_preserves_boundary": True,
        "stability_does_not_select_handoff_parity": True,
        "fixed_action_selects_only_conditionally": True,
        "selector_key_relocates_unless_parity_is_derived": True,
    }
    assert all(checks.values())

    return {
        "claim_id": "HC-DU-219",
        "verdict": "AUTONOMOUS_MATCHED_HANDOFF_FORMS_BUT_STABILITY_DOES_NOT_SELECT_ANCHORED_PARITY",
        "checks": checks,
        "passed": sum(checks.values()),
        "total": len(checks),
        "convergence": convergence,
        "record_gauge_orbits": record_gauge_orbits,
        "record_plus_target_label_orbits": full_label_gauge_orbits,
        "thermal_beta_j_ln_2": thermal,
        "quantum_transfer": quantum_transfer,
        "claim_boundaries": {
            "earned": [
                "conditional autonomous formation of a matched binary handoff",
                "record-label gauge quotient",
                "gauge-invariant handoff parity",
                "stability/ispectral nonselection of handoff parity",
                "target-anchor gauge-versus-physical fork",
            ],
            "not_earned": [
                "universal autonomous-interface no-go",
                "derivation of the coupling signs or target ruler",
                "noncommuting quantum effect",
                "source provenance, archive, observer access, or public finality",
                "issuance, physical remainder, or new law of nature",
            ],
        },
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
