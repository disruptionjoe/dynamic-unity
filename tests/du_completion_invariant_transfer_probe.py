#!/usr/bin/env python3
"""Exact finite certificate for ECR-N5-S4 completion transfer.

The analytic result is the finite common-quotient theorem:

For record maps r_i on one completion set, the finest statistic q that
factors through every r_i has kernel equal to the join of the record
equivalence relations.  A target t transfers through every native record
without refitting exactly when ker(q) is contained in ker(t).

This probe checks that theorem on the minimum visible-archive/hidden-reservoir
completion pair inherited from HC-DU-044.  It also freezes four targets before
testing:

* the next reduced-matter branch law;
* write occurrence since epoch reset;
* write count; and
* the full resolved history word.

The executable is a finite partition certificate, not a microscopic
environment simulation.  It cannot select a physical completion, observer
boundary, archive, epoch, or ontology.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Hashable, Iterable, Iterator, Sequence


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_completion_invariant_transfer_result.json"
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
RATE_CLASS = {
    "x0": "fast:alpha",
    "x1": "slow:kappa",
    "x2": "fast:alpha",
    "x3": "slow:kappa",
}

Partition = tuple[tuple[int, ...], ...]


@dataclass(frozen=True)
class History:
    length: int
    word: str
    endpoint: str


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, indent=2) + "\n"


def build_histories(max_length: int = 8) -> tuple[History, ...]:
    state = "x1"
    word = ""
    histories = [History(0, word, state)]
    for length in range(1, max_length + 1):
        word += EDGE_KIND[state]
        state = NEXT_STATE[state]
        histories.append(History(length, word, state))
    return tuple(histories)


def token_word(word: str) -> str:
    return word if word else "EMPTY"


def visible_complete_state(history: History) -> tuple[str, str, str]:
    return (
        history.endpoint,
        f"A:{token_word(history.word)}",
        "H:blank",
    )


def hidden_complete_state(history: History) -> tuple[str, str, str]:
    return (
        history.endpoint,
        "A:blank",
        f"H:{token_word(history.word)}",
    )


def visible_native_record(history: History) -> tuple[str, str]:
    state = visible_complete_state(history)
    return state[0], state[1]


def hidden_native_record(history: History) -> tuple[str, str]:
    state = hidden_complete_state(history)
    return state[0], state[1]


def visible_epoch_record(history: History) -> tuple[str, int]:
    return history.endpoint, occurrence_target(history)


def terminal_matter_record(history: History) -> str:
    return history.endpoint


def globally_accessible_visible_record(
    history: History,
) -> tuple[str, str, str]:
    return visible_complete_state(history)


def globally_accessible_hidden_record(
    history: History,
) -> tuple[str, str, str]:
    return hidden_complete_state(history)


def next_matter_target(history: History) -> tuple[str, str, str]:
    """Complete one-step reduced branch profile at the terminal state."""

    state = history.endpoint
    return state, NEXT_STATE[state], RATE_CLASS[state]


def occurrence_target(history: History) -> int:
    return int("W" in history.word)


def count_target(history: History) -> int:
    return history.word.count("W")


def word_target(history: History) -> str:
    return token_word(history.word)


def values(
    histories: Sequence[History],
    function: Callable[[History], Hashable],
) -> tuple[Hashable, ...]:
    return tuple(function(history) for history in histories)


def partition_from_values(items: Sequence[Hashable]) -> Partition:
    blocks: dict[Hashable, list[int]] = {}
    for index, item in enumerate(items):
        blocks.setdefault(item, []).append(index)
    return canonical_partition(blocks.values())


def canonical_partition(blocks: Iterable[Iterable[int]]) -> Partition:
    normalized = [tuple(sorted(block)) for block in blocks]
    return tuple(sorted(normalized, key=lambda block: block[0]))


class UnionFind:
    def __init__(self, size: int) -> None:
        self.parent = list(range(size))

    def find(self, value: int) -> int:
        while self.parent[value] != value:
            self.parent[value] = self.parent[self.parent[value]]
            value = self.parent[value]
        return value

    def union(self, left: int, right: int) -> None:
        left_root = self.find(left)
        right_root = self.find(right)
        if left_root != right_root:
            self.parent[right_root] = left_root


def join_partitions(partitions: Sequence[Partition], size: int) -> Partition:
    """Least equivalence relation containing every supplied partition."""

    union_find = UnionFind(size)
    for partition in partitions:
        for block in partition:
            anchor = block[0]
            for item in block[1:]:
                union_find.union(anchor, item)
    joined: dict[int, list[int]] = {}
    for item in range(size):
        joined.setdefault(union_find.find(item), []).append(item)
    return canonical_partition(joined.values())


def partition_refines(fine: Partition, coarse: Partition) -> bool:
    """Return whether every fine block lies in one coarse block."""

    coarse_lookup: dict[int, int] = {}
    for block_index, block in enumerate(coarse):
        for item in block:
            coarse_lookup[item] = block_index
    return all(
        len({coarse_lookup[item] for item in block}) == 1
        for block in fine
    )


def restricted_growth_strings(size: int) -> Iterator[tuple[int, ...]]:
    if size == 0:
        yield ()
        return

    def extend(prefix: list[int], maximum: int) -> Iterator[tuple[int, ...]]:
        if len(prefix) == size:
            yield tuple(prefix)
            return
        for label in range(maximum + 2):
            prefix.append(label)
            yield from extend(prefix, max(maximum, label))
            prefix.pop()

    yield from extend([0], 0)


def partition_from_labels(labels: Sequence[int]) -> Partition:
    blocks: dict[int, list[int]] = {}
    for item, label in enumerate(labels):
        blocks.setdefault(label, []).append(item)
    return canonical_partition(blocks.values())


def enumerate_common_quotients(
    native_partitions: Sequence[Partition],
    size: int,
) -> tuple[int, tuple[Partition, ...]]:
    enumerated = 0
    common: list[Partition] = []
    for labels in restricted_growth_strings(size):
        enumerated += 1
        candidate = partition_from_labels(labels)
        if all(
            partition_refines(native, candidate)
            for native in native_partitions
        ):
            common.append(candidate)
    return enumerated, tuple(common)


def factorizes(
    record_values: Sequence[Hashable],
    target_values: Sequence[Hashable],
) -> bool:
    return partition_refines(
        partition_from_values(record_values),
        partition_from_values(target_values),
    )


def decoder(
    record_values: Sequence[Hashable],
    target_values: Sequence[Hashable],
) -> dict[str, Hashable] | None:
    result: dict[str, Hashable] = {}
    for record_value, target_value in zip(
        record_values, target_values, strict=True
    ):
        key = repr(record_value)
        if key in result and result[key] != target_value:
            return None
        result[key] = target_value
    return result


def factorization_witness(
    record_values: Sequence[Hashable],
    target_values: Sequence[Hashable],
) -> tuple[int, int] | None:
    for left in range(len(record_values)):
        for right in range(left + 1, len(record_values)):
            if (
                record_values[left] == record_values[right]
                and target_values[left] != target_values[right]
            ):
                return left, right
    return None


def witness_payload(
    histories: Sequence[History],
    record_values: Sequence[Hashable],
    target_values: Sequence[Hashable],
) -> dict[str, Any] | None:
    witness = factorization_witness(record_values, target_values)
    if witness is None:
        return None
    left, right = witness
    return {
        "left": {
            "history": histories[left].word,
            "endpoint": histories[left].endpoint,
            "record": record_values[left],
            "target": target_values[left],
        },
        "right": {
            "history": histories[right].word,
            "endpoint": histories[right].endpoint,
            "record": record_values[right],
            "target": target_values[right],
        },
    }


def partition_words(
    partition: Partition,
    histories: Sequence[History],
) -> list[list[str]]:
    return [
        [token_word(histories[index].word) for index in block]
        for block in partition
    ]


def completion_branch_map(
    history_location: str,
) -> dict[tuple[str, str], tuple[str, str, str]]:
    """One-step completion map before projection to the matter carrier."""

    result: dict[tuple[str, str], tuple[str, str, str]] = {}
    for state in NEXT_STATE:
        if history_location == "A":
            result[(state, "no_jump")] = (
                state,
                "A:retain",
                "H:blank",
            )
            result[(state, "jump")] = (
                NEXT_STATE[state],
                f"A:append:{EDGE_KIND[state]}",
                "H:blank",
            )
        elif history_location == "H":
            result[(state, "no_jump")] = (
                state,
                "A:blank",
                "H:retain",
            )
            result[(state, "jump")] = (
                NEXT_STATE[state],
                "A:blank",
                f"H:append:{EDGE_KIND[state]}",
            )
        else:
            raise ValueError(f"unsupported history location: {history_location}")
    return result


def matter_projection(
    branches: dict[tuple[str, str], tuple[str, str, str]],
) -> dict[tuple[str, str], str]:
    return {
        branch: completion_state[0]
        for branch, completion_state in branches.items()
    }


def build_result() -> dict[str, Any]:
    histories = build_histories()
    size = len(histories)

    visible_values = values(histories, visible_native_record)
    hidden_values = values(histories, hidden_native_record)
    endpoint_values = values(histories, terminal_matter_record)
    visible_epoch_values = values(histories, visible_epoch_record)
    visible_global_values = values(
        histories, globally_accessible_visible_record
    )
    hidden_global_values = values(
        histories, globally_accessible_hidden_record
    )

    target_functions: dict[str, Callable[[History], Hashable]] = {
        "T_next": next_matter_target,
        "T_occ": occurrence_target,
        "T_count": count_target,
        "T_word": word_target,
    }
    target_values = {
        name: values(histories, function)
        for name, function in target_functions.items()
    }

    visible_partition = partition_from_values(visible_values)
    hidden_partition = partition_from_values(hidden_values)
    endpoint_partition = partition_from_values(endpoint_values)
    common_partition = join_partitions(
        (visible_partition, hidden_partition), size
    )
    visible_epoch_partition = partition_from_values(visible_epoch_values)
    global_common_partition = join_partitions(
        (
            partition_from_values(visible_global_values),
            partition_from_values(hidden_global_values),
        ),
        size,
    )

    enumerated, common_quotients = enumerate_common_quotients(
        (visible_partition, hidden_partition), size
    )
    maximum_block_count = max(
        len(partition) for partition in common_quotients
    )
    finest_common = tuple(
        partition
        for partition in common_quotients
        if len(partition) == maximum_block_count
    )

    relabel = {
        word: f"opaque-token-{index:02d}"
        for index, word in enumerate(
            reversed(tuple(token_word(history.word) for history in histories))
        )
    }
    relabelled_visible_values = tuple(
        (history.endpoint, relabel[token_word(history.word)])
        for history in histories
    )
    relabelled_common = join_partitions(
        (
            partition_from_values(relabelled_visible_values),
            hidden_partition,
        ),
        size,
    )

    record_families: dict[str, tuple[Hashable, ...]] = {
        "completion_common": endpoint_values,
        "visible_binary_epoch": visible_epoch_values,
        "visible_full_archive": visible_values,
        "hidden_A_only": hidden_values,
    }
    factorization_table: dict[str, Any] = {}
    for record_name, record_items in record_families.items():
        factorization_table[record_name] = {}
        for target_name, targets in target_values.items():
            factorization_table[record_name][target_name] = {
                "factors": factorizes(record_items, targets),
                "witness": witness_payload(
                    histories, record_items, targets
                ),
            }

    global_record_values = tuple(
        (history.endpoint, token_word(history.word))
        for history in histories
    )
    global_factorization = {
        name: factorizes(global_record_values, targets)
        for name, targets in target_values.items()
    }

    capability_maps: dict[str, tuple[Hashable, ...]] = {
        "H_matter": tuple(
            (target_values["T_next"][index],)
            for index in range(size)
        ),
        "H_occ": tuple(
            (
                target_values["T_next"][index],
                target_values["T_occ"][index],
            )
            for index in range(size)
        ),
        "H_count": tuple(
            (
                target_values["T_next"][index],
                target_values["T_occ"][index],
                target_values["T_count"][index],
            )
            for index in range(size)
        ),
        "H_output": tuple(
            (
                target_values["T_next"][index],
                target_values["T_occ"][index],
                target_values["T_count"][index],
                target_values["T_word"][index],
            )
            for index in range(size)
        ),
    }
    capability_factorization = {
        record_name: {
            capability_name: factorizes(record_items, behavior)
            for capability_name, behavior in capability_maps.items()
        }
        for record_name, record_items in record_families.items()
    }

    common_first_failure = next(
        capability
        for capability in ("H_matter", "H_occ", "H_count", "H_output")
        if not capability_factorization["completion_common"][capability]
    )
    visible_binary_first_failure = next(
        capability
        for capability in ("H_matter", "H_occ", "H_count", "H_output")
        if not capability_factorization["visible_binary_epoch"][capability]
    )

    reduced_visible = {
        history.word: visible_complete_state(history)[0]
        for history in histories
    }
    reduced_hidden = {
        history.word: hidden_complete_state(history)[0]
        for history in histories
    }
    visible_branches = completion_branch_map("A")
    hidden_branches = completion_branch_map("H")

    checks: dict[str, bool] = {
        "visible_complete_states_injective": (
            len(set(map(visible_complete_state, histories))) == size
        ),
        "hidden_complete_states_injective": (
            len(set(map(hidden_complete_state, histories))) == size
        ),
        "same_reduced_history_endpoint_map": (
            reduced_visible == reduced_hidden
        ),
        "completion_branch_maps_are_physically_distinct": (
            visible_branches != hidden_branches
        ),
        "same_reduced_one_step_branch_map": (
            matter_projection(visible_branches)
            == matter_projection(hidden_branches)
        ),
        "visible_native_record_is_full_history": (
            len(visible_partition) == size
        ),
        "hidden_native_record_is_endpoint_only": (
            hidden_partition == endpoint_partition
        ),
        "common_join_equals_endpoint_partition": (
            common_partition == endpoint_partition
        ),
        "partition_enumeration_bell_9": enumerated == 21147,
        "common_quotient_candidate_count": len(common_quotients) == 15,
        "finest_common_quotient_unique": len(finest_common) == 1,
        "enumerated_finest_equals_join": finest_common == (common_partition,),
        "lossless_relabel_preserves_common_join": (
            relabelled_common == common_partition
        ),
        "next_target_factors_common": factorization_table[
            "completion_common"
        ]["T_next"]["factors"],
        "occurrence_target_fails_common": not factorization_table[
            "completion_common"
        ]["T_occ"]["factors"],
        "count_target_fails_common": not factorization_table[
            "completion_common"
        ]["T_count"]["factors"],
        "word_target_fails_common": not factorization_table[
            "completion_common"
        ]["T_word"]["factors"],
        "visible_epoch_reconstructs_occurrence": factorization_table[
            "visible_binary_epoch"
        ]["T_occ"]["factors"],
        "visible_epoch_reconstructs_matter_future": factorization_table[
            "visible_binary_epoch"
        ]["T_next"]["factors"],
        "visible_epoch_does_not_reconstruct_count": not factorization_table[
            "visible_binary_epoch"
        ]["T_count"]["factors"],
        "visible_full_reconstructs_all_targets": all(
            entry["factors"]
            for entry in factorization_table[
                "visible_full_archive"
            ].values()
        ),
        "hidden_A_only_reconstructs_only_next": (
            factorization_table["hidden_A_only"]["T_next"]["factors"]
            and not factorization_table["hidden_A_only"]["T_occ"][
                "factors"
            ]
            and not factorization_table["hidden_A_only"]["T_count"][
                "factors"
            ]
            and not factorization_table["hidden_A_only"]["T_word"][
                "factors"
            ]
        ),
        "common_next_decoder_exists": decoder(
            endpoint_values, target_values["T_next"]
        )
        is not None,
        "common_occurrence_decoder_absent": decoder(
            endpoint_values, target_values["T_occ"]
        )
        is None,
        "target_coded_occurrence_not_hidden_quotient": not factorizes(
            hidden_values, target_values["T_occ"]
        ),
        "global_access_common_partition_is_full_history": (
            len(global_common_partition) == size
        ),
        "global_access_reconstructs_all_targets": all(
            global_factorization.values()
        ),
        "cross_completion_first_leak_is_occurrence": (
            common_first_failure == "H_occ"
        ),
        "visible_binary_first_leak_is_count": (
            visible_binary_first_failure == "H_count"
        ),
        "capability_filtration_is_strict_at_common_shadow": (
            capability_factorization["completion_common"]["H_matter"]
            and not capability_factorization["completion_common"]["H_occ"]
        ),
        "capability_filtration_is_strict_at_visible_epoch": (
            capability_factorization["visible_binary_epoch"]["H_occ"]
            and not capability_factorization["visible_binary_epoch"][
                "H_count"
            ]
        ),
    }

    return {
        "claim": "HC-DU-045",
        "campaign": "ECR-N5-S4",
        "theorem": {
            "name": "finite completion-common quotient theorem",
            "statement": (
                "the finest target-independent quotient common to all "
                "native records has kernel equal to the equivalence join "
                "of their kernels; a target transfers through every native "
                "record iff that join is contained in the target kernel"
            ),
            "component_math_grade": "known finite quotient/factorization",
        },
        "arena": {
            "initial_state": "x1",
            "histories": [
                {
                    "length": history.length,
                    "word": token_word(history.word),
                    "endpoint": history.endpoint,
                }
                for history in histories
            ],
            "visible_completion": (
                "history token retained in admitted archive A"
            ),
            "hidden_completion": (
                "same history token retained in reservoir H outside the "
                "A-only observer boundary"
            ),
            "same_reduced_matter_law": reduced_visible == reduced_hidden,
            "same_reduced_one_step_branch_map": (
                matter_projection(visible_branches)
                == matter_projection(hidden_branches)
            ),
        },
        "partitions": {
            "visible_native": partition_words(
                visible_partition, histories
            ),
            "hidden_native": partition_words(hidden_partition, histories),
            "completion_common_join": partition_words(
                common_partition, histories
            ),
            "terminal_matter": partition_words(
                endpoint_partition, histories
            ),
            "visible_binary_epoch": partition_words(
                visible_epoch_partition, histories
            ),
            "global_A_plus_H_common": partition_words(
                global_common_partition, histories
            ),
            "enumerated_set_partitions": enumerated,
            "common_quotient_candidates": len(common_quotients),
            "finest_common_candidates": len(finest_common),
        },
        "target_factorization": factorization_table,
        "capability_factorization": capability_factorization,
        "first_leaks": {
            "across_completions_at_A_only_boundary": common_first_failure,
            "within_visible_binary_epoch_record": (
                visible_binary_first_failure
            ),
            "interpretation": (
                "the completion-common endpoint predicts reduced matter "
                "behavior but first fails at historical occurrence; inside "
                "the visible history completion the binary epoch quotient "
                "first fails at write count"
            ),
        },
        "access_retyping": {
            "A_only_common_record": "terminal matter endpoint",
            "A_plus_H_common_record": "complete resolved history",
            "all_targets_factor_after_A_plus_H": all(
                global_factorization.values()
            ),
            "contract_change": (
                "granting H access changes the observer boundary, action "
                "envelope, and resource contract; it does not repair the "
                "A-only record within the old contract"
            ),
        },
        "absorber_collision": {
            "markov_sufficiency": (
                "terminal matter state is sufficient for the next reduced "
                "matter branch law"
            ),
            "blackwell_and_partition_sufficiency": (
                "target transfer is exactly kernel containment through "
                "the common quotient"
            ),
            "stinespring_and_complementary_channels": (
                "fixed reduced dynamics does not determine which "
                "complementary fragment carries accessible history"
            ),
            "process_tensor_and_full_environment": (
                "full multi-time/environment access can retain history, "
                "but that is a stronger access contract"
            ),
        },
        "verdict": {
            "completion_invariant_positive": (
                "strict endpoint compression reconstructs future reduced "
                "matter behavior"
            ),
            "positive_grade": (
                "MARKOV_OPERATIONAL_CLOSURE / NOT HISTORY-ARCHIVE "
                "RECONSTRUCTION"
            ),
            "history_result": "COMPLETION_AND_ACCESS_RELATIVE_SUFFICIENCY",
            "archive_result": "NO_ENDOGENOUS_ARCHIVE_FOR_THIS_HOST",
            "north_star": "H-CCR-17 REMAINS OPEN",
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
    if not result["checks"]["all_pass"]:
        failed = [
            name
            for name, passed in result["checks"]["details"].items()
            if not passed
        ]
        raise SystemExit(f"failed checks: {failed}")
    print(
        "HC-DU-045 completion-invariant transfer certificate: "
        f"{result['checks']['passed']}/{result['checks']['total']} passed"
    )
    print(
        "common quotient:",
        result["partitions"]["completion_common_join"],
    )
    print("first leaks:", result["first_leaks"])
    print("artifact:", ARTIFACT)


if __name__ == "__main__":
    main()
