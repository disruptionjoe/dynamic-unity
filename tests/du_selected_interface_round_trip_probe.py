#!/usr/bin/env python3
"""Exact finite controls for the HC-DU-181 round-trip boundary.

The probe distinguishes:

* reconstruction conditional on a named interface;
* reconstruction that is independent of an unrecorded interface choice;
* reconstruction after a physical selector is supplied;
* law-level identifiability; and
* zero-error certification from one realized record.

Passing proves only finite factorization, support-separation, and
data-processing statements. It does not construct a GU flag, source action,
detector, archive, observer, decoder implementation, or physical prediction.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path
from typing import Hashable


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_selected_interface_round_trip_result.json"
)

Completion = Hashable
Interface = Hashable
Target = Hashable
Outcome = Hashable
Law = dict[Outcome, Fraction]
Kernel = dict[Outcome, dict[Outcome, Fraction]]


def canonical_law(law: Law) -> tuple[tuple[str, int, int], ...]:
    """Return a stable exact representation of a finite probability law."""

    return tuple(
        sorted(
            (
                repr(outcome),
                probability.numerator,
                probability.denominator,
            )
            for outcome, probability in law.items()
            if probability
        )
    )


def factors_through(
    domain: tuple[Hashable, ...],
    record: dict[Hashable, Hashable],
    target: dict[Hashable, Hashable],
) -> bool:
    """Return whether target is constant on every record fibre."""

    return all(
        record[left] != record[right] or target[left] == target[right]
        for left in domain
        for right in domain
    )


def fixed_interface_reconstructs(
    completions: tuple[Completion, ...],
    laws: dict[tuple[Interface, Completion], Law],
    target: dict[Completion, Target],
    interface: Interface,
) -> bool:
    record = {
        completion: canonical_law(laws[(interface, completion)])
        for completion in completions
    }
    return factors_through(completions, record, target)


def untagged_family_reconstructs(
    interfaces: tuple[Interface, ...],
    completions: tuple[Completion, ...],
    laws: dict[tuple[Interface, Completion], Law],
    target: dict[Completion, Target],
) -> bool:
    """Test whether one decoder works without receiving an interface tag."""

    domain = tuple(
        (interface, completion)
        for interface in interfaces
        for completion in completions
    )
    record = {
        point: canonical_law(laws[point])
        for point in domain
    }
    lifted_target = {
        point: target[point[1]]
        for point in domain
    }
    return factors_through(domain, record, lifted_target)


def tagged_family_reconstructs(
    interfaces: tuple[Interface, ...],
    completions: tuple[Completion, ...],
    laws: dict[tuple[Interface, Completion], Law],
    target: dict[Completion, Target],
) -> bool:
    """Test the enlarged packet that explicitly retains interface identity."""

    domain = tuple(
        (interface, completion)
        for interface in interfaces
        for completion in completions
    )
    record = {
        point: (point[0], canonical_law(laws[point]))
        for point in domain
    }
    lifted_target = {
        point: target[point[1]]
        for point in domain
    }
    return factors_through(domain, record, lifted_target)


def selected_interface_reconstructs(
    completions: tuple[Completion, ...],
    laws: dict[tuple[Interface, Completion], Law],
    target: dict[Completion, Target],
    selector: dict[Completion, Interface],
) -> bool:
    record = {
        completion: canonical_law(
            laws[(selector[completion], completion)]
        )
        for completion in completions
    }
    return factors_through(completions, record, target)


def event_level_exact(
    completions: tuple[Completion, ...],
    selected_laws: dict[Completion, Law],
    target: dict[Completion, Target],
) -> bool:
    """Return whether one outcome can be decoded with zero target error."""

    return all(
        target[left] == target[right]
        or set(selected_laws[left]).isdisjoint(selected_laws[right])
        for left in completions
        for right in completions
    )


def total_variation(left: Law, right: Law) -> Fraction:
    outcomes = set(left) | set(right)
    return sum(
        abs(left.get(outcome, Fraction(0)) - right.get(outcome, Fraction(0)))
        for outcome in outcomes
    ) / 2


def pushforward(law: Law, channel: Kernel) -> Law:
    result: Law = {}
    for source, probability in law.items():
        row = channel[source]
        if sum(row.values()) != 1:
            raise ValueError(f"channel row for {source!r} is not normalized")
        for outcome, conditional in row.items():
            result[outcome] = (
                result.get(outcome, Fraction(0))
                + probability * conditional
            )
    return result


def descends_through_equivalence(
    completions: tuple[Completion, ...],
    equivalence_class: dict[Completion, Hashable],
    values: dict[Completion, Hashable],
) -> bool:
    return all(
        equivalence_class[left] != equivalence_class[right]
        or values[left] == values[right]
        for left in completions
        for right in completions
    )


def as_json_fraction(value: Fraction) -> dict[str, int]:
    return {
        "numerator": value.numerator,
        "denominator": value.denominator,
    }


def run_probe() -> dict[str, object]:
    completions = (0, 1)
    interfaces = ("direct", "flip")
    target = {0: 0, 1: 1}

    direct_flip_laws: dict[tuple[Interface, Completion], Law] = {
        ("direct", 0): {0: Fraction(1)},
        ("direct", 1): {1: Fraction(1)},
        ("flip", 0): {1: Fraction(1)},
        ("flip", 1): {0: Fraction(1)},
    }

    checks: list[dict[str, object]] = []
    checks.append(
        {
            "name": "each_named_interface_has_a_conditional_decoder",
            "passed": all(
                fixed_interface_reconstructs(
                    completions,
                    direct_flip_laws,
                    target,
                    interface,
                )
                for interface in interfaces
            ),
        }
    )
    checks.append(
        {
            "name": "conditional_decoders_do_not_imply_untagged_decoder",
            "passed": not untagged_family_reconstructs(
                interfaces,
                completions,
                direct_flip_laws,
                target,
            ),
        }
    )
    checks.append(
        {
            "name": "retained_interface_tag_repairs_by_record_enlargement",
            "passed": tagged_family_reconstructs(
                interfaces,
                completions,
                direct_flip_laws,
                target,
            ),
        }
    )

    direct_selector = {0: "direct", 1: "direct"}
    checks.append(
        {
            "name": "selected_informative_interface_closes_law_round_trip",
            "passed": selected_interface_reconstructs(
                completions,
                direct_flip_laws,
                target,
                direct_selector,
            ),
        }
    )

    constant_laws: dict[tuple[Interface, Completion], Law] = {
        ("constant", 0): {"same": Fraction(1)},
        ("constant", 1): {"same": Fraction(1)},
    }
    constant_selector = {0: "constant", 1: "constant"}
    checks.append(
        {
            "name": "physical_selection_does_not_imply_identifiability",
            "passed": not selected_interface_reconstructs(
                completions,
                constant_laws,
                target,
                constant_selector,
            ),
        }
    )

    invariant_laws: dict[tuple[Interface, Completion], Law] = {
        (interface, completion): {completion: Fraction(1)}
        for interface in interfaces
        for completion in completions
    }
    checks.append(
        {
            "name": "selector_not_needed_when_target_descends_across_family",
            "passed": untagged_family_reconstructs(
                interfaces,
                completions,
                invariant_laws,
                target,
            ),
        }
    )

    overlapping = {
        0: {"left": Fraction(4, 5), "right": Fraction(1, 5)},
        1: {"left": Fraction(1, 5), "right": Fraction(4, 5)},
    }
    overlapping_record = {
        completion: canonical_law(overlapping[completion])
        for completion in completions
    }
    overlap_tv = total_variation(overlapping[0], overlapping[1])
    checks.append(
        {
            "name": "law_identifiability_does_not_imply_event_certificate",
            "passed": (
                factors_through(completions, overlapping_record, target)
                and not event_level_exact(
                    completions,
                    overlapping,
                    target,
                )
                and overlap_tv == Fraction(3, 5)
            ),
            "total_variation": as_json_fraction(overlap_tv),
            "minimum_equal_prior_error": as_json_fraction(
                (1 - overlap_tv) / 2
            ),
        }
    )

    disjoint = {
        0: {"left_only": Fraction(1)},
        1: {"right_only": Fraction(1)},
    }
    checks.append(
        {
            "name": "disjoint_target_supports_give_exact_event_decoder",
            "passed": event_level_exact(completions, disjoint, target),
        }
    )

    noisy_channel: Kernel = {
        "left": {
            "reported_left": Fraction(3, 4),
            "reported_right": Fraction(1, 4),
        },
        "right": {
            "reported_left": Fraction(1, 4),
            "reported_right": Fraction(3, 4),
        },
    }
    downstream_left = pushforward(overlapping[0], noisy_channel)
    downstream_right = pushforward(overlapping[1], noisy_channel)
    downstream_tv = total_variation(downstream_left, downstream_right)
    checks.append(
        {
            "name": "common_downstream_channel_contracts_target_information",
            "passed": (
                downstream_tv == Fraction(3, 10)
                and downstream_tv <= overlap_tv
            ),
            "upstream_total_variation": as_json_fraction(overlap_tv),
            "downstream_total_variation": as_json_fraction(downstream_tv),
        }
    )

    identical_upstream = {
        0: {"same": Fraction(1)},
        1: {"same": Fraction(1)},
    }
    same_channel: Kernel = {
        "same": {
            "a": Fraction(1, 3),
            "b": Fraction(2, 3),
        }
    }
    checks.append(
        {
            "name": "common_readout_cannot_repair_equal_upstream_laws",
            "passed": (
                pushforward(identical_upstream[0], same_channel)
                == pushforward(identical_upstream[1], same_channel)
            ),
        }
    )

    gauge_completions = ("m_g0", "m_g1", "n_g0", "n_g1")
    gauge_class = {
        "m_g0": "m",
        "m_g1": "m",
        "n_g0": "n",
        "n_g1": "n",
    }
    gauge_invariant_target = {
        "m_g0": 0,
        "m_g1": 0,
        "n_g0": 1,
        "n_g1": 1,
    }
    gauge_dependent_record = {
        "m_g0": "r0",
        "m_g1": "r1",
        "n_g0": "s0",
        "n_g1": "s1",
    }
    gauge_invariant_record = {
        "m_g0": "r",
        "m_g1": "r",
        "n_g0": "s",
        "n_g1": "s",
    }
    checks.append(
        {
            "name": "physical_round_trip_requires_gauge_descent",
            "passed": (
                descends_through_equivalence(
                    gauge_completions,
                    gauge_class,
                    gauge_invariant_target,
                )
                and not descends_through_equivalence(
                    gauge_completions,
                    gauge_class,
                    gauge_dependent_record,
                )
                and descends_through_equivalence(
                    gauge_completions,
                    gauge_class,
                    gauge_invariant_record,
                )
            ),
        }
    )

    passed = sum(1 for check in checks if check["passed"])
    result = {
        "claim_id": "HC-DU-181",
        "run_id": "RUN-20260731-022601-selected-interface-round-trip-gate",
        "scope": "finite exact factorization and support controls only",
        "checks": checks,
        "summary": {
            "passed": passed,
            "total": len(checks),
            "status": "PASS" if passed == len(checks) else "FAIL",
        },
        "nonclaims": [
            "No GU flag or source action is constructed.",
            "No detector, retained archive, observer, or capability is selected.",
            "No finite fixture establishes new physics or ontology.",
            "A retained interface tag is record enlargement, not free repair.",
            "Law-level identifiability is not one-event certification.",
        ],
    }
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--write-artifact",
        action="store_true",
        help="write the deterministic JSON artifact",
    )
    args = parser.parse_args()

    result = run_probe()
    if args.write_artifact:
        ARTIFACT.parent.mkdir(parents=True, exist_ok=True)
        ARTIFACT.write_text(
            json.dumps(result, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )

    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["summary"]["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
