#!/usr/bin/env python3
"""Exact regression certificate for ECR-N5-S5 / HC-DU-046.

The proof lives in the accompanying exploration.  This executable checks the
finite instances and exact rational decision formulas used there:

* the first endpoint/history factorization failure occurs at horizon four and
  remains present through longer prefix horizons;
* positive stochastic weighting cannot repair a support-level failure;
* lossless relabeling and benign temporal subdivision preserve the witness;
* a full-history erasure channel has an exact Bayes boundary; and
* relocating the archive while holding the host antecedent fixed defeats
  interface selection, whereas full-environment access is injective.

It is a deterministic theorem-regression artifact, not a microscopic model,
hardware experiment, or empirical prediction.
"""

from __future__ import annotations

import json
import math
from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Callable, Hashable, Mapping, Sequence


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_metastable_host_robustness_adjudication_result.json"
)

NEXT_STATE = {
    "x0": "x1",
    "x1": "x2",
    "x2": "x3",
    "x3": "x0",
}
EDGE_KIND = {
    "x0": "W",
    "x1": "C",
    "x2": "W",
    "x3": "C",
}


@dataclass(frozen=True)
class History:
    length: int
    word: str
    endpoint: str


@dataclass(frozen=True)
class RoutedCompletion:
    """One fixed host with a choice of accessible archive routing."""

    history: History
    routing: str


def build_histories(max_length: int) -> tuple[History, ...]:
    state = "x1"
    word = ""
    histories = [History(0, word, state)]
    for length in range(1, max_length + 1):
        word += EDGE_KIND[state]
        state = NEXT_STATE[state]
        histories.append(History(length, word, state))
    return tuple(histories)


def occurrence(history: History) -> int:
    return int("W" in history.word)


def write_count(history: History) -> int:
    return history.word.count("W")


def next_branch(history: History) -> tuple[str, str]:
    return history.endpoint, NEXT_STATE[history.endpoint]


def factorizes(
    histories: Sequence[History],
    record: Callable[[History], Hashable],
    target: Callable[[History], Hashable],
) -> bool:
    decoder: dict[Hashable, Hashable] = {}
    for history in histories:
        key = record(history)
        value = target(history)
        if key in decoder and decoder[key] != value:
            return False
        decoder[key] = value
    return True


def normalized_prior(weights: Mapping[int, int]) -> dict[int, Fraction]:
    total = sum(weights.values())
    return {
        index: Fraction(weight, total)
        for index, weight in weights.items()
    }


def bayes_error_under_history_erasure(
    histories: Sequence[History],
    prior: Mapping[int, Fraction],
    reveal_probability: Fraction,
) -> Fraction:
    """Bayes 0-1 error for occurrence under full-history erasure.

    The accessible output always contains the endpoint.  With probability
    ``reveal_probability`` it also contains a unique history token; otherwise
    it contains the common symbol ERASED.
    """

    masses: dict[tuple[str, str], dict[int, Fraction]] = defaultdict(
        lambda: defaultdict(Fraction)
    )
    for index, probability in prior.items():
        history = histories[index]
        label = occurrence(history)
        masses[
            (history.endpoint, f"H{history.length}")
        ][label] += probability * reveal_probability
        masses[
            (history.endpoint, "ERASED")
        ][label] += probability * (1 - reveal_probability)
    return sum(
        min(label_masses.get(0, Fraction()), label_masses.get(1, Fraction()))
        for label_masses in masses.values()
    )


def endpoint_ambiguity_mass(
    histories: Sequence[History],
    prior: Mapping[int, Fraction],
) -> Fraction:
    masses: dict[str, dict[int, Fraction]] = defaultdict(
        lambda: defaultdict(Fraction)
    )
    for index, probability in prior.items():
        history = histories[index]
        masses[history.endpoint][occurrence(history)] += probability
    return sum(
        min(label_masses.get(0, Fraction()), label_masses.get(1, Fraction()))
        for label_masses in masses.values()
    )


def subdivided_word(history: History, subdivisions: int) -> tuple[str, ...]:
    return tuple(
        f"{event}.{microstep}"
        for event in history.word
        for microstep in range(1, subdivisions + 1)
    )


def contract_subdivision(
    micro_word: Sequence[str],
    subdivisions: int,
) -> str:
    return "".join(
        micro_word[index].split(".", maxsplit=1)[0]
        for index in range(0, len(micro_word), subdivisions)
    )


def host_antecedent(completion: RoutedCompletion) -> tuple[object, ...]:
    """The frozen generator does not include environment routing/access."""

    return (
        tuple(sorted(NEXT_STATE.items())),
        tuple(sorted(EDGE_KIND.items())),
        completion.history.length,
        completion.history.endpoint,
    )


def accessible_interface(completion: RoutedCompletion) -> tuple[str, str]:
    token = (
        f"H{completion.history.length}"
        if completion.routing == "A"
        else "blank"
    )
    return completion.history.endpoint, token


def full_environment_interface(
    completion: RoutedCompletion,
) -> tuple[str, str]:
    """Read the history token wherever the routing placed it."""

    return completion.history.endpoint, f"H{completion.history.length}"


def fraction_text(value: Fraction) -> str:
    return (
        str(value.numerator)
        if value.denominator == 1
        else f"{value.numerator}/{value.denominator}"
    )


def canonical_json(value: object) -> str:
    return json.dumps(value, indent=2, sort_keys=True) + "\n"


def build_result() -> dict[str, object]:
    max_horizon = 40
    histories = build_histories(max_horizon)

    horizon_rows: list[dict[str, object]] = []
    for horizon in range(max_horizon + 1):
        prefix = histories[: horizon + 1]
        occurrence_factors = factorizes(
            prefix, lambda item: item.endpoint, occurrence
        )
        count_factors = factorizes(
            prefix, lambda item: item.endpoint, write_count
        )
        word_factors = factorizes(
            prefix, lambda item: item.endpoint, lambda item: item.word
        )
        horizon_rows.append(
            {
                "horizon": horizon,
                "occurrence_factors_through_endpoint": occurrence_factors,
                "count_factors_through_endpoint": count_factors,
                "word_factors_through_endpoint": word_factors,
                "next_branch_factors_through_endpoint": factorizes(
                    prefix, lambda item: item.endpoint, next_branch
                ),
            }
        )

    first_occurrence_failure = next(
        row["horizon"]
        for row in horizon_rows
        if not row["occurrence_factors_through_endpoint"]
    )

    relabelings = (
        lambda history: f"opaque-{history.length}",
        lambda history: f"token-{max_horizon - history.length:02d}",
        lambda history: ("archive", 17 * history.length + 3),
    )
    relabel_checks = [
        len({label(history) for history in histories})
        == len(histories)
        for label in relabelings
    ]

    subdivision_rows = []
    empty_history = histories[0]
    cycle_history = histories[4]
    for subdivisions in range(1, 9):
        empty_micro = subdivided_word(empty_history, subdivisions)
        cycle_micro = subdivided_word(cycle_history, subdivisions)
        subdivision_rows.append(
            {
                "subdivisions_per_event": subdivisions,
                "contracted_empty": contract_subdivision(
                    empty_micro, subdivisions
                ),
                "contracted_cycle": contract_subdivision(
                    cycle_micro, subdivisions
                ),
                "same_endpoint": (
                    empty_history.endpoint == cycle_history.endpoint
                ),
                "different_occurrence": (
                    occurrence(empty_history) != occurrence(cycle_history)
                ),
            }
        )

    priors = {
        "equal_h0_h4": normalized_prior({0: 1, 4: 1}),
        "uniform_h0_h8": normalized_prior(
            {index: 1 for index in range(9)}
        ),
        "increasing_h0_h8": normalized_prior(
            {index: index + 1 for index in range(9)}
        ),
        "decreasing_h0_h8": normalized_prior(
            {index: 2 ** (8 - index) for index in range(9)}
        ),
    }
    reveal_probabilities = tuple(
        Fraction(numerator, 4) for numerator in range(5)
    )
    leakage_rows = []
    leakage_formula_checks = []
    for prior_name, prior in priors.items():
        ambiguity = endpoint_ambiguity_mass(histories, prior)
        for reveal_probability in reveal_probabilities:
            observed = bayes_error_under_history_erasure(
                histories, prior, reveal_probability
            )
            expected = (1 - reveal_probability) * ambiguity
            leakage_formula_checks.append(observed == expected)
            leakage_rows.append(
                {
                    "prior": prior_name,
                    "reveal_probability": fraction_text(
                        reveal_probability
                    ),
                    "endpoint_ambiguity_mass": fraction_text(ambiguity),
                    "bayes_error": fraction_text(observed),
                    "formula_value": fraction_text(expected),
                }
            )

    equal_prior_risks = {
        fraction_text(reveal_probability): fraction_text(
            bayes_error_under_history_erasure(
                histories,
                priors["equal_h0_h4"],
                reveal_probability,
            )
        )
        for reveal_probability in reveal_probabilities
    }

    archive_visible = RoutedCompletion(cycle_history, "A")
    archive_hidden = RoutedCompletion(cycle_history, "H")
    archive_swap_checks = {
        "host_antecedent_invariant": (
            host_antecedent(archive_visible)
            == host_antecedent(archive_hidden)
        ),
        "accessible_interface_changes": (
            accessible_interface(archive_visible)
            != accessible_interface(archive_hidden)
        ),
        "full_environment_interface_invariant": (
            full_environment_interface(archive_visible)
            == full_environment_interface(archive_hidden)
        ),
    }

    resource_rows = [
        {
            "horizon": horizon,
            "endpoint_alphabet_upper_bits": 2,
            "full_history_distinctions": horizon + 1,
            "full_history_minimum_bits": math.ceil(
                math.log2(horizon + 1)
            ),
        }
        for horizon in (4, 8, 16, 32, 40)
    ]

    checks = {
        "first_occurrence_failure_is_horizon_four": (
            first_occurrence_failure == 4
        ),
        "all_horizons_below_four_factor_occurrence": all(
            row["occurrence_factors_through_endpoint"]
            for row in horizon_rows[:4]
        ),
        "all_horizons_from_four_fail_occurrence": all(
            not row["occurrence_factors_through_endpoint"]
            for row in horizon_rows[4:]
        ),
        "all_horizons_preserve_next_branch_factorization": all(
            row["next_branch_factors_through_endpoint"]
            for row in horizon_rows
        ),
        "h0_h4_same_endpoint": (
            histories[0].endpoint == histories[4].endpoint
        ),
        "h0_h4_different_occurrence": (
            occurrence(histories[0]) != occurrence(histories[4])
        ),
        "h0_h4_different_count": (
            write_count(histories[0]) != write_count(histories[4])
        ),
        "h0_h4_different_word": histories[0].word != histories[4].word,
        "lossless_relabelings_are_injective": all(relabel_checks),
        "all_subdivisions_contract_to_same_macro_witness": all(
            row["contracted_empty"] == ""
            and row["contracted_cycle"] == histories[4].word
            and row["same_endpoint"]
            and row["different_occurrence"]
            for row in subdivision_rows
        ),
        "all_leakage_formula_checks": all(leakage_formula_checks),
        "equal_pair_zero_reveal_risk_is_half": (
            equal_prior_risks["0"] == "1/2"
        ),
        "equal_pair_full_reveal_risk_is_zero": (
            equal_prior_risks["1"] == "0"
        ),
        "every_partial_reveal_has_positive_equal_pair_error": all(
            bayes_error_under_history_erasure(
                histories,
                priors["equal_h0_h4"],
                reveal_probability,
            )
            > 0
            for reveal_probability in reveal_probabilities[:-1]
        ),
        "archive_swap_obstruction_holds": all(
            archive_swap_checks.values()
        ),
        "full_history_cost_eventually_exceeds_endpoint_cost": (
            resource_rows[-1]["full_history_minimum_bits"]
            > resource_rows[-1]["endpoint_alphabet_upper_bits"]
        ),
    }

    return {
        "claim": "HC-DU-046",
        "campaign": "ECR-N5-S5",
        "theorem_package": {
            "arbitrary_horizon": (
                "the finest visible/hidden A-only common quotient remains "
                "terminal endpoint at every prefix horizon; historical "
                "occurrence first fails at horizon four and the h0/h4 "
                "witness persists at every longer horizon"
            ),
            "positive_weights": (
                "strictly positive stochastic weights preserve exact "
                "nonfactorization because both witness histories remain "
                "in support"
            ),
            "representation_invariance": (
                "lossless token relabeling and target-preserving temporal "
                "subdivision preserve the record and target kernels"
            ),
            "approximate_boundary": (
                "under complete-history reveal probability lambda and "
                "otherwise endpoint-only erasure, Bayes occurrence error "
                "equals (1-lambda) times endpoint ambiguity mass"
            ),
            "archive_relocation": (
                "an archive interface cannot be selected by a host "
                "antecedent invariant under accessible/hidden routing swap"
            ),
        },
        "horizon_certificate": {
            "tested_through": max_horizon,
            "first_occurrence_failure": first_occurrence_failure,
            "rows": horizon_rows,
        },
        "subdivision_certificate": subdivision_rows,
        "stochastic_and_leakage_certificate": {
            "rows": leakage_rows,
            "equal_h0_h4_bayes_risk": equal_prior_risks,
            "equal_h0_h4_total_variation": {
                fraction_text(reveal_probability): fraction_text(
                    reveal_probability
                )
                for reveal_probability in reveal_probabilities
            },
        },
        "archive_relocation_certificate": archive_swap_checks,
        "resource_normalization": resource_rows,
        "host_selected_premise_audit": {
            "selected_by_frozen_host": [
                "four-state matter carrier",
                "alternating write/turnover edge architecture",
                "terminal next-state law",
                "ready/retained orbit structure up to relabeling",
            ],
            "not_selected_by_frozen_host": [
                "environment factorization into A and H",
                "blank archive preparation",
                "history-routing coupling",
                "retention horizon and epoch boundary",
                "observer boundary and access route",
                "archive location",
            ],
        },
        "verdict": {
            "positive": "MARKOV_OPERATIONAL_CLOSURE",
            "historical_host_verdict": (
                "SELECTION_OR_FORMATION_OBSTRUCTION"
            ),
            "full_environment_control": "INJECTIVE_TOMOGRAPHY_ONLY",
            "scope": (
                "final for the frozen metastable host and declared "
                "robustness family; not a universal record no-go"
            ),
            "north_star": (
                "H-CCR-17 remains open outside this host; compile the "
                "minimum missing premise and re-rank the DU portfolio"
            ),
        },
        "checks": {
            "passed": sum(checks.values()),
            "total": len(checks),
            "all_pass": all(checks.values()),
            "details": checks,
        },
    }


def main() -> None:
    result = build_result()
    ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT.write_text(canonical_json(result), encoding="utf-8")
    checks = result["checks"]
    if not checks["all_pass"]:
        failed = [
            name
            for name, passed in checks["details"].items()
            if not passed
        ]
        raise SystemExit(f"failed checks: {failed}")
    print(
        "HC-DU-046 metastable-host robustness certificate: "
        f"{checks['passed']}/{checks['total']} passed"
    )
    print(
        "first occurrence failure:",
        result["horizon_certificate"]["first_occurrence_failure"],
    )
    print("verdict:", result["verdict"]["historical_host_verdict"])
    print("artifact:", ARTIFACT)


if __name__ == "__main__":
    main()
