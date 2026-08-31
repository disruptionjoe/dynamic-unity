#!/usr/bin/env python3
"""Exact controls for the heralded Bell-record capability quotient.

The finite truth table is reconstructed from Eqs. (10)--(13) of
Arenskoetter et al., Phys. Rev. Research 6, 023061 (2024).  The script does
not simulate the apparatus or validate the source experiment.  It checks the
record quotient, its deterministic minimality, Haar-average fidelity losses
under record erasure, and finite retry costs from the source-reported success
probabilities.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "tests" / "artifacts" / "du_heralded_bell_record_capability_result.json"


# Encodings: passage 0/1 = first/second; herald 0/1 = H/V;
# atom 0/1 = +/- projection.  The raw triple is a physical detector record;
# the correction label is its action-relative quotient.
CORRECTION = {
    (0, 0): "Y",  # first passage, Psi+
    (0, 1): "X",  # first passage, Psi-
    (1, 0): "Z",  # second passage, Phi+
    (1, 1): "I",  # second passage, Phi-
}


def quotient(raw: tuple[int, int, int]) -> tuple[int, int]:
    passage, herald, atom = raw
    return passage, herald ^ atom


def correction(raw: tuple[int, int, int]) -> str:
    return CORRECTION[quotient(raw)]


def partition_by(indices: tuple[int, ...]) -> dict[tuple[int, ...], list[tuple[int, int, int]]]:
    blocks: dict[tuple[int, ...], list[tuple[int, int, int]]] = {}
    for raw in itertools.product((0, 1), repeat=3):
        key = tuple(raw[i] for i in indices)
        blocks.setdefault(key, []).append(raw)
    return blocks


def block_corrections(block: list[tuple[int, int, int]]) -> set[str]:
    return {correction(raw) for raw in block}


def optimal_haar_fidelity(indices: tuple[int, ...]) -> float:
    """Best average fidelity using only the selected uniformly sampled bits.

    For an unknown qubit, a correct Pauli correction has Haar-average fidelity
    1 and any wrong nonidentity Pauli has average fidelity 1/3.  Within each
    observed block the optimal deterministic decoder selects a most frequent
    correction.
    """
    total = 0.0
    for block in partition_by(indices).values():
        counts = {label: sum(correction(raw) == label for raw in block) for label in CORRECTION.values()}
        correct = max(counts.values())
        wrong = len(block) - correct
        total += correct + wrong / 3.0
    return total / 8.0


def attempts_for_confidence(success_probability: float, confidence: float) -> int:
    if not 0.0 < success_probability < 1.0:
        raise ValueError("success_probability must lie in (0,1)")
    if not 0.0 < confidence < 1.0:
        raise ValueError("confidence must lie in (0,1)")
    return math.ceil(math.log1p(-confidence) / math.log1p(-success_probability))


def run() -> dict[str, object]:
    raw_rows = []
    for raw in itertools.product((0, 1), repeat=3):
        q = quotient(raw)
        raw_rows.append(
            {
                "raw": list(raw),
                "quotient": list(q),
                "bell_family": "Psi" if q[0] == 0 else "Phi",
                "sign": "+" if q[1] == 0 else "-",
                "correction": correction(raw),
            }
        )

    correction_classes: dict[str, list[list[int]]] = {}
    for row in raw_rows:
        correction_classes.setdefault(str(row["correction"]), []).append(row["raw"])

    assert len(correction_classes) == 4
    assert all(len(rows) == 2 for rows in correction_classes.values())
    assert {row["bell_family"] for row in raw_rows if row["raw"][0] == 0} == {"Psi"}
    assert {row["bell_family"] for row in raw_rows if row["raw"][0] == 1} == {"Phi"}

    # The pre-registered action-relative quotient is sufficient: all raw
    # records in a quotient block demand the same correction.
    q_blocks: dict[tuple[int, int], list[tuple[int, int, int]]] = {}
    for raw in itertools.product((0, 1), repeat=3):
        q_blocks.setdefault(quotient(raw), []).append(raw)
    assert len(q_blocks) == 4
    assert all(len(block_corrections(block)) == 1 for block in q_blocks.values())

    # No coordinate deletion from the raw record remains exact.  This is a
    # hostile control against mistaking any two raw detector bits for the
    # capability-minimal quotient.
    coordinate_subsets: dict[str, dict[str, object]] = {}
    for size in range(4):
        for indices in itertools.combinations(range(3), size):
            blocks = partition_by(indices)
            exact = all(len(block_corrections(block)) == 1 for block in blocks.values())
            coordinate_subsets["".join(map(str, indices)) or "none"] = {
                "indices": list(indices),
                "classes": len(blocks),
                "exact": exact,
                "optimal_haar_fidelity": optimal_haar_fidelity(indices),
            }
            if size < 3:
                assert not exact
    assert coordinate_subsets["012"]["exact"] is True

    # Four different required Pauli actions imply at least four quotient
    # classes (two bits) for exact deterministic recovery of every input.
    minimum_action_classes = len(set(CORRECTION.values()))
    minimum_action_bits = math.ceil(math.log2(minimum_action_classes))
    assert minimum_action_classes == 4
    assert minimum_action_bits == 2

    # Erasing either actionable quotient bit aliases two equiprobable Pauli
    # corrections.  The best unknown-qubit average fidelity is exactly 2/3;
    # erasing both gives the fully depolarized 1/2 boundary.
    quotient_fidelities = {
        "full_two_bit_record": 1.0,
        "passage_only": 2.0 / 3.0,
        "parity_only": 2.0 / 3.0,
        "no_actionable_bits": 0.5,
    }
    assert quotient_fidelities["passage_only"] == 2.0 / 3.0
    assert quotient_fidelities["parity_only"] == 2.0 / 3.0

    # For independent symmetric flips of the two actionable bits, a wrong
    # Pauli has Haar-average fidelity 1/3.  Quantum advantage over 2/3 requires
    # the complete label to be right more than half the time.
    bit_error_threshold = 1.0 - 1.0 / math.sqrt(2.0)
    for epsilon in (0.0, bit_error_threshold, 0.5):
        p_correct = (1.0 - epsilon) ** 2
        fidelity = 1.0 / 3.0 + 2.0 * p_correct / 3.0
        if epsilon == 0.0:
            assert math.isclose(fidelity, 1.0)
        if epsilon == bit_error_threshold:
            assert math.isclose(fidelity, 2.0 / 3.0)

    # Source-reported first- and second-passage success probabilities are
    # disjoint outcomes.  The source also supplies three different
    # denominators.  Conditional correctness and finite-horizon availability
    # are therefore different capability coordinates, and the resource
    # normalization must be declared rather than silently interchanged.
    source_success = {
        "per_experimental_run": (1.76e-4, 2.21e-5),
        "per_generated_pair": (6.47e-7, 8.15e-8),
        "per_incoming_photon_at_ion": (1.71e-5, 2.16e-6),
    }
    retry: dict[str, dict[str, float | int]] = {}
    for denominator, (first, second) in source_success.items():
        combined = first + second
        retry[denominator] = {
            "first_passage_success": first,
            "second_passage_success": second,
            "combined_success": combined,
            "expected_units": 1.0 / combined,
            "units_for_95_percent": attempts_for_confidence(combined, 0.95),
            "units_for_99_percent": attempts_for_confidence(combined, 0.99),
        }
        assert retry[denominator]["units_for_99_percent"] > retry[denominator]["units_for_95_percent"]

    result = {
        "source": {
            "citation": "Arenskoetter et al., Phys. Rev. Research 6, 023061 (2024)",
            "doi": "10.1103/PhysRevResearch.6.023061",
            "source_claims_validated_by_probe": False,
        },
        "raw_rows": raw_rows,
        "correction_classes": correction_classes,
        "action_quotient": {
            "map": "(passage, herald, atom) -> (passage, herald XOR atom)",
            "raw_classes": 8,
            "action_classes": minimum_action_classes,
            "minimum_action_bits": minimum_action_bits,
            "raw_redundancy_bits": 1,
            "sufficient": True,
        },
        "coordinate_deletion_controls": coordinate_subsets,
        "ideal_quotient_fidelities": quotient_fidelities,
        "independent_bit_error_threshold_for_fidelity_above_two_thirds": bit_error_threshold,
        "finite_retry": retry,
        "scientific_boundary": {
            "proves": [
                "exact action-relative factorization of the ideal raw record",
                "two-bit deterministic minimality for an arbitrary unknown qubit",
                "separation of conditional correctness from finite-horizon availability",
            ],
            "does_not_prove": [
                "source-paper validity",
                "apparatus selection from bare quantum laws",
                "single-world actualization",
                "implementation-complete attempt lineage",
                "new physics or ontology priority",
            ],
        },
    }
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-artifact", action="store_true")
    args = parser.parse_args()
    result = run()
    if args.write_artifact:
        ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
        ARTIFACT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
