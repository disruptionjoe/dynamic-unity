#!/usr/bin/env python3
"""Exact finite controls for HC-DU-211.

The probe validates only the ordered theorem spine:

1. antecedent-relative selection up to an explicitly declared gauge orbit;
2. the stabilizer fixed-point necessity for equivariant selection;
3. matched producer-consumer relabeling versus consumer freedom;
4. structural and predictive classifications after an incumbent landing; and
5. readout preservation/erasure of a pre-existing target distinction.

It is not a physical model, QFT calculation, GU result, or novelty proof.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Hashable, Iterable, Mapping, Sequence


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = ROOT / "tests" / "artifacts" / "du_complete_handoff_selection_landing_result.json"


@dataclass(frozen=True)
class Handoff:
    """Small deterministic producer-consumer handoff with two record labels."""

    producer: tuple[int, int]
    consumer: tuple[int, int]
    archive: str = "retained"
    access: str = "available"
    resource: int = 1

    def response(self) -> tuple[int, int]:
        return tuple(self.consumer[r] for r in self.producer)


SWAP = (1, 0)
IDENTITY = (0, 1)


def transform_handoff(handoff: Handoff, permutation: tuple[int, int]) -> Handoff:
    inverse = tuple(permutation.index(label) for label in IDENTITY)
    producer = tuple(permutation[label] for label in handoff.producer)
    consumer = tuple(handoff.consumer[inverse[label]] for label in IDENTITY)
    return Handoff(
        producer=producer,
        consumer=consumer,
        archive=handoff.archive,
        access=handoff.access,
        resource=handoff.resource,
    )


def canonical_gauge_orbit(handoff: Handoff) -> tuple[object, ...]:
    images = [transform_handoff(handoff, permutation) for permutation in (IDENTITY, SWAP)]
    return min(
        (
            image.producer,
            image.consumer,
            image.archive,
            image.access,
            image.resource,
        )
        for image in images
    )


def factors_through(
    worlds: Iterable[Mapping[str, object]],
    antecedent: Callable[[Mapping[str, object]], Hashable],
    target: Callable[[Mapping[str, object]], Hashable],
) -> bool:
    fibres: dict[Hashable, set[Hashable]] = defaultdict(set)
    for world in worlds:
        fibres[antecedent(world)].add(target(world))
    return all(len(values) == 1 for values in fibres.values())


def stabilizer_fixed_candidates(
    candidates: Sequence[str],
    stabilizer_actions: Sequence[Mapping[str, str]],
) -> list[str]:
    return [
        candidate
        for candidate in candidates
        if all(action[candidate] == candidate for action in stabilizer_actions)
    ]


def landing_classification(
    incumbent: Mapping[str, int],
    selected: Mapping[str, int],
    *,
    target_blind: bool,
) -> dict[str, object]:
    if not selected:
        return {"classification": "INVALID_EMPTY_SELECTION"}
    if not target_blind:
        return {"classification": "AFTER_FACT_REFIT_NO_CREDIT"}

    incumbent_names = set(incumbent)
    selected_names = set(selected)
    incumbent_targets = set(incumbent.values())
    selected_targets = set(selected.values())
    expressible = selected_names <= incumbent_names
    structural_selection = expressible and selected_names < incumbent_names

    if not selected_targets <= incumbent_targets:
        classification = "RIVAL_EXCLUDING_EXCESS"
    elif selected_targets < incumbent_targets:
        classification = "SOURCE_SELECTED_SHARPENING"
    elif structural_selection:
        classification = "STRUCTURAL_SELECTION_ONLY"
    elif expressible:
        classification = "QFT_PREDICTIVELY_ABSORBED"
    else:
        classification = "RIVAL_STRUCTURE_TARGET_ABSORBED"

    return {
        "classification": classification,
        "qft_expressible": expressible,
        "structural_selection": structural_selection,
        "incumbent_targets": sorted(incumbent_targets),
        "selected_targets": sorted(selected_targets),
    }


def pushforward(values: Iterable[int], channel: Callable[[int], Hashable]) -> set[Hashable]:
    return {channel(value) for value in values}


def check(name: str, condition: bool, detail: str) -> dict[str, object]:
    if not condition:
        raise AssertionError(f"{name}: {detail}")
    return {"name": name, "passed": True, "detail": detail}


def build_result() -> dict[str, object]:
    checks: list[dict[str, object]] = []

    identity_handoff = Handoff(IDENTITY, IDENTITY)
    matched_swap = transform_handoff(identity_handoff, SWAP)
    flip_consumer = Handoff(IDENTITY, SWAP)

    gauge_worlds = [
        {"antecedent": "same-source", "handoff": identity_handoff},
        {"antecedent": "same-source", "handoff": matched_swap},
    ]
    checks.append(
        check(
            "absolute_encoding_is_not_selected",
            not factors_through(gauge_worlds, lambda w: w["antecedent"], lambda w: w["handoff"]),
            "matched relabelings differ as encoded tuples",
        )
    )
    checks.append(
        check(
            "matched_handoff_orbit_is_selected",
            factors_through(
                gauge_worlds,
                lambda w: w["antecedent"],
                lambda w: canonical_gauge_orbit(w["handoff"]),  # type: ignore[arg-type]
            ),
            "the complete matched pair is constant modulo the declared label gauge",
        )
    )
    checks.append(
        check(
            "matched_relabeling_preserves_closed_response",
            identity_handoff.response() == matched_swap.response() == IDENTITY,
            "producer and consumer co-transform",
        )
    )

    consumer_worlds = [
        {"antecedent": "same-source-writer", "alignment": "identity", "handoff": identity_handoff},
        {"antecedent": "same-source-writer", "alignment": "flip", "handoff": flip_consumer},
    ]
    checks.append(
        check(
            "writer_does_not_select_consumer_orbit",
            not factors_through(
                consumer_worlds,
                lambda w: w["antecedent"],
                lambda w: canonical_gauge_orbit(w["handoff"]),  # type: ignore[arg-type]
            ),
            "same source and writer support inequivalent closed response handoffs",
        )
    )
    checks.append(
        check(
            "consumer_freedom_changes_target_response",
            identity_handoff.response() != flip_consumer.response(),
            "record-preserving consumers can implement different continuations",
        )
    )
    checks.append(
        check(
            "alignment_premise_repairs_selection",
            factors_through(
                consumer_worlds,
                lambda w: (w["antecedent"], w["alignment"]),
                lambda w: canonical_gauge_orbit(w["handoff"]),  # type: ignore[arg-type]
            ),
            "an independently physical alignment coordinate separates the two fibres",
        )
    )

    swap_action = {"left": "right", "right": "left", "symmetric": "symmetric"}
    fixed_without_symmetric = stabilizer_fixed_candidates(["left", "right"], [swap_action])
    fixed_with_symmetric = stabilizer_fixed_candidates(
        ["left", "right", "symmetric"], [swap_action]
    )
    checks.append(
        check(
            "stabilizer_without_fixed_candidate_blocks_equivariant_point_selector",
            fixed_without_symmetric == [],
            "a fixed antecedent cannot equivariantly choose either member of a swapped pair",
        )
    )
    checks.append(
        check(
            "stabilizer_fixed_candidate_is_positive_control",
            fixed_with_symmetric == ["symmetric"],
            "the stabilizer test admits a genuinely fixed candidate",
        )
    )

    incumbent_sharpen = {"linear": 2, "quadratic": 4}
    selected_sharpen = {"quadratic": 4}
    sharpen = landing_classification(incumbent_sharpen, selected_sharpen, target_blind=True)
    checks.append(
        check(
            "qft_expressibility_allows_predictive_sharpening",
            sharpen["classification"] == "SOURCE_SELECTED_SHARPENING"
            and sharpen["qft_expressible"] is True,
            "the selected law is inside the incumbent language but the incumbent target fibre was nonconstant",
        )
    )

    incumbent_structural = {"field-content-a": 4, "field-content-b": 4}
    selected_structural = {"field-content-a": 4}
    structural = landing_classification(
        incumbent_structural, selected_structural, target_blind=True
    )
    checks.append(
        check(
            "structural_selection_is_distinct_from_target_excess",
            structural["classification"] == "STRUCTURAL_SELECTION_ONLY"
            and structural["structural_selection"] is True,
            "an upstream theory can select a QFT input without sharpening this held-out target",
        )
    )

    absorbed = landing_classification({"only": 4}, {"only": 4}, target_blind=True)
    checks.append(
        check(
            "constant_incumbent_target_is_predictively_absorbed",
            absorbed["classification"] == "QFT_PREDICTIVELY_ABSORBED",
            "the frozen incumbent already predicts the selected target",
        )
    )

    excess = landing_classification({"incumbent": 2}, {"challenger": 4}, target_blind=True)
    checks.append(
        check(
            "outside_incumbent_target_is_rival_excluding",
            excess["classification"] == "RIVAL_EXCLUDING_EXCESS",
            "the challenger target lies outside the frozen incumbent target image",
        )
    )

    refit = landing_classification(incumbent_sharpen, selected_sharpen, target_blind=False)
    checks.append(
        check(
            "after_fact_selection_gets_no_credit",
            refit["classification"] == "AFTER_FACT_REFIT_NO_CREDIT",
            "target reveal cannot be used to choose the successful completion",
        )
    )

    raw_incumbent = {2}
    raw_challenger = {4}
    identity_channel = lambda value: value
    parity_channel = lambda value: value % 2
    checks.append(
        check(
            "resolving_readout_preserves_raw_excess",
            pushforward(raw_incumbent, identity_channel)
            != pushforward(raw_challenger, identity_channel),
            "a resolving channel retains the target difference",
        )
    )
    checks.append(
        check(
            "coarse_readout_can_erase_raw_excess",
            pushforward(raw_incumbent, parity_channel)
            == pushforward(raw_challenger, parity_channel),
            "parity identifies two distinct raw predictions",
        )
    )

    exhaustive_handoffs = [
        Handoff(tuple(producer), tuple(consumer))
        for producer in itertools.product(IDENTITY, repeat=2)
        for consumer in itertools.product(IDENTITY, repeat=2)
    ]
    orbit_response_consistent = all(
        handoff.response() == transform_handoff(handoff, SWAP).response()
        for handoff in exhaustive_handoffs
    )
    checks.append(
        check(
            "matched_descent_exhaustive_over_binary_handoffs",
            orbit_response_consistent and len(exhaustive_handoffs) == 16,
            "all 16 deterministic producer-consumer pairs preserve closed response under matched swap",
        )
    )

    applications = [
        {
            "specimen": "HC-DU-207 action-selected holonomy",
            "selection": "transport orbit, holonomy, response spectrum and coarse bands",
            "first_open_field": "instrument/material handoff",
            "classification": "RELATIONAL_STRUCTURE_SELECTED_HANDOFF_OPEN",
        },
        {
            "specimen": "HC-DU-208 spectral PVM",
            "selection": "PVM/effect statistics",
            "first_open_field": "selective instrument and consumer",
            "classification": "PRODUCER_EFFECT_SELECTED_CONTINUATION_OPEN",
        },
        {
            "specimen": "HC-DU-209 conditional GU K77 2+1",
            "selection": "matched luminous orbit only under supplied conditional action",
            "first_open_field": "GU-owned source action and QFT parameter relations",
            "classification": "CONDITIONAL_STRUCTURAL_SELECTION_NO_SOURCE_ACTION",
        },
        {
            "specimen": "HC-DU-210 Jacobson regional response",
            "selection": "regional response after region/reference/couplings are fixed",
            "first_open_field": "provenance-sensitive joint region-scale source law",
            "classification": "QFT_EFT_REPRESENTABLE_NO_PROVENANCE_SELECTION",
        },
    ]

    return {
        "schema_version": "dynamic-unity/complete-handoff-selection-landing/v0.1",
        "claim_id": "HC-DU-211",
        "run_id": "RUN-20260831-complete-handoff-selection-landing-spine",
        "theorem_parts": [
            "selection_up_to_physical_gauge_is_fibre_factorization",
            "equivariant_point_selection_requires_stabilizer_fixed_candidate",
            "matched_label_descent_does_not_remove_complete_handoff_duties",
            "qft_expressibility_is_distinct_from_structural_and_predictive_absorption",
            "readout_can_preserve_or_erase_but_not_create_raw_excess",
        ],
        "checks": checks,
        "summary": {
            "passed": len(checks),
            "total": len(checks),
            "single_new_mathematical_theorem": False,
            "ordered_theorem_spine": True,
            "maximum_grade": 4,
        },
        "application_ledger": applications,
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
