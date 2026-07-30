#!/usr/bin/env python3
"""Exact finite controls for HC-DU-163.

Passing proves only the quotient, factorization, observed-mean, finite-twin,
and action-extension controls declared for Swing 5. It does not establish a
physical archive, a latent variable in the Peronnin apparatus, reconstruction,
a remainder, a new law, or new physics.
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Callable, Hashable, Iterable


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_action_relative_materialization_result.json"
)

History = tuple[str, str, int, int]
Signature = tuple[Fraction, ...]
RecordMap = Callable[[History], Hashable]
SignatureMap = Callable[[History], Signature]


def histories() -> tuple[History, ...]:
    return tuple(
        (label, propensity, beta_noise, trace_noise)
        for label in ("g", "e")
        for propensity in ("stable", "fragile")
        for beta_noise in (0, 1)
        for trace_noise in (0, 1)
    )


def exact_signature(history: History) -> Signature:
    label, _, _, _ = history
    repeat = Fraction(19, 20)
    if label == "g":
        return (repeat, 1 - repeat)
    return (1 - repeat, repeat)


def heterogeneous_signature(history: History) -> Signature:
    label, propensity, _, _ = history
    repeat = Fraction(1) if propensity == "stable" else Fraction(9, 10)
    if label == "g":
        return (repeat, 1 - repeat)
    return (1 - repeat, repeat)


def extended_signature(history: History) -> Signature:
    """Baseline exact-repeat response plus one explicitly excluded audit."""
    label, propensity, _, _ = history
    audit_yes = Fraction(propensity == "stable")
    return exact_signature(history) + (audit_yes, 1 - audit_yes)


def label_record(history: History) -> Hashable:
    return history[0]


def beta_record(history: History) -> Hashable:
    label, _, beta_noise, _ = history
    return (label, beta_noise)


def raw_trace_record(history: History) -> Hashable:
    label, _, beta_noise, trace_noise = history
    return (label, beta_noise, trace_noise)


def idealized_identity_archive(history: History) -> Hashable:
    return history


def kernel(
    domain: Iterable[History],
    mapping: Callable[[History], Hashable],
) -> frozenset[tuple[History, History]]:
    items = tuple(domain)
    return frozenset(
        (left, right)
        for left in items
        for right in items
        if mapping(left) == mapping(right)
    )


def class_count(
    domain: Iterable[History],
    mapping: Callable[[History], Hashable],
) -> int:
    return len({mapping(item) for item in domain})


def relation(
    domain: Iterable[History],
    record: RecordMap,
    response: SignatureMap,
) -> str:
    record_kernel = kernel(domain, record)
    response_kernel = kernel(domain, response)
    if record_kernel == response_kernel:
        return "EXACT_REALIZATION"
    if record_kernel < response_kernel:
        return "OVERFINE_RESPONSE_SUFFICIENT"
    if response_kernel < record_kernel:
        return "COARSE_RESPONSE_LOSS"
    return "INCOMPARABLE"


def conditional_means(
    domain: Iterable[History],
    record: RecordMap,
    response: SignatureMap,
) -> dict[str, list[str]]:
    grouped: dict[Hashable, list[Signature]] = defaultdict(list)
    for item in domain:
        grouped[record(item)].append(response(item))

    result: dict[str, list[str]] = {}
    for key, values in grouped.items():
        mean = tuple(
            sum((value[index] for value in values), Fraction(0))
            / len(values)
            for index in range(len(values[0]))
        )
        result[repr(key)] = [str(value) for value in mean]
    return dict(sorted(result.items()))


def conditional_repeat_variance(
    domain: Iterable[History],
    record: RecordMap,
    response: SignatureMap,
) -> dict[str, str]:
    grouped: dict[Hashable, list[Fraction]] = defaultdict(list)
    for item in domain:
        label = item[0]
        signature = response(item)
        repeat_probability = signature[0] if label == "g" else signature[1]
        grouped[record(item)].append(repeat_probability)

    result: dict[str, str] = {}
    for key, values in grouped.items():
        mean = sum(values, Fraction(0)) / len(values)
        variance = (
            sum(((value - mean) ** 2 for value in values), Fraction(0))
            / len(values)
        )
        result[repr(key)] = str(variance)
    return dict(sorted(result.items()))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-artifact", action="store_true")
    args = parser.parse_args()

    domain = histories()
    records: dict[str, RecordMap] = {
        "binary_label": label_record,
        "calibrated_statistic": beta_record,
        "raw_trace": raw_trace_record,
        "idealized_identity_archive": idealized_identity_archive,
    }

    exact_relations = {
        name: relation(domain, record, exact_signature)
        for name, record in records.items()
    }
    heterogeneous_relations = {
        name: relation(domain, record, heterogeneous_signature)
        for name, record in records.items()
    }

    joined_observed_twins = {
        name: (
            conditional_means(domain, record, exact_signature)
            == conditional_means(domain, record, heterogeneous_signature)
        )
        for name, record in records.items()
        if name != "idealized_identity_archive"
    }

    exact_variance = conditional_repeat_variance(
        domain,
        label_record,
        exact_signature,
    )
    heterogeneous_variance = conditional_repeat_variance(
        domain,
        label_record,
        heterogeneous_signature,
    )

    baseline_kernel = kernel(domain, exact_signature)
    extended_kernel = kernel(domain, extended_signature)
    action_extension = {
        "baseline_quotient_classes": class_count(domain, exact_signature),
        "extended_quotient_classes": class_count(domain, extended_signature),
        "extended_kernel_strictly_refines_baseline": (
            extended_kernel < baseline_kernel
        ),
        "binary_label_relation_after_extension": relation(
            domain,
            label_record,
            extended_signature,
        ),
    }

    report_twins = {
        "domain_size": len(domain),
        "same_candidate_record_distribution": True,
        "same_joined_one_step_laws": joined_observed_twins,
        "aggregate_repeat_probability_exact": "19/20",
        "aggregate_repeat_probability_heterogeneous": str(
            sum(
                (
                    heterogeneous_signature(item)[0]
                    if item[0] == "g"
                    else heterogeneous_signature(item)[1]
                    for item in domain
                ),
                Fraction(0),
            )
            / len(domain)
        ),
        "exact_physical_quotient_classes": class_count(
            domain,
            exact_signature,
        ),
        "heterogeneous_physical_quotient_classes": class_count(
            domain,
            heterogeneous_signature,
        ),
        "label_conditional_variance_exact": exact_variance,
        "label_conditional_variance_heterogeneous": heterogeneous_variance,
    }

    checks = {
        "physical_quotient_exists_by_signature_image": (
            report_twins["exact_physical_quotient_classes"] == 2
            and report_twins["heterogeneous_physical_quotient_classes"] == 4
        ),
        "same_joined_observed_law_different_physical_quotient": (
            all(joined_observed_twins.values())
            and report_twins["exact_physical_quotient_classes"]
            != report_twins["heterogeneous_physical_quotient_classes"]
        ),
        "aggregate_repeat_rate_matches_source_summary": (
            report_twins["aggregate_repeat_probability_exact"] == "19/20"
            and report_twins[
                "aggregate_repeat_probability_heterogeneous"
            ]
            == "19/20"
        ),
        "zero_conditional_heterogeneity_iff_exact_in_control": (
            set(exact_variance.values()) == {"0"}
            and set(heterogeneous_variance.values()) == {"1/400"}
        ),
        "label_exact_in_one_twin_and_lossy_in_other": (
            exact_relations["binary_label"] == "EXACT_REALIZATION"
            and heterogeneous_relations["binary_label"]
            == "COARSE_RESPONSE_LOSS"
        ),
        "statistic_and_trace_can_be_incomparable": (
            heterogeneous_relations["calibrated_statistic"]
            == "INCOMPARABLE"
            and heterogeneous_relations["raw_trace"] == "INCOMPARABLE"
        ),
        "identity_archive_is_sufficient_but_overfine": (
            exact_relations["idealized_identity_archive"]
            == "OVERFINE_RESPONSE_SUFFICIENT"
            and heterogeneous_relations["idealized_identity_archive"]
            == "OVERFINE_RESPONSE_SUFFICIENT"
        ),
        "action_extension_strictly_refines_quotient": (
            action_extension["extended_kernel_strictly_refines_baseline"]
            and action_extension["baseline_quotient_classes"] == 2
            and action_extension["extended_quotient_classes"] == 4
            and action_extension["binary_label_relation_after_extension"]
            == "COARSE_RESPONSE_LOSS"
        ),
    }
    if not all(checks.values()):
        failed = [name for name, passed in checks.items() if not passed]
        raise AssertionError(f"action-relative controls failed: {failed}")

    result = {
        "probe": "du_action_relative_materialization_probe",
        "status": "PASS",
        "claim_id": "HC-DU-163",
        "scope": "frozen_repeat_readout_action_and_exact_finite_twins",
        "frozen_action": (
            "unchanged second binary readout beginning 220 ns after the first, "
            "with no outcome-conditioned intervention"
        ),
        "exact_relations": exact_relations,
        "heterogeneous_relations": heterogeneous_relations,
        "report_twins": report_twins,
        "action_extension": action_extension,
        "checks": checks,
        "disclaimer": (
            "Passing establishes only exact finite quotient and "
            "nonidentification controls. It establishes no latent variable in "
            "the source apparatus, complete physical archive, reconstruction, "
            "remainder, new law, or new physics."
        ),
    }
    if args.write_artifact:
        ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
        ARTIFACT.write_text(
            json.dumps(result, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
