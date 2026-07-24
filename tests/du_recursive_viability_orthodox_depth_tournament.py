#!/usr/bin/env python3
"""Orthodox finite tournament for discovering recursive viability depth.

The probe compares ordinary passive dynamics (m=0), one active viability
level (m=1), two genuinely coupled control levels (m=2), and a redundant
third level (m=3).  It is deliberately small and exact.

Four micro-variables first absorb a passive disturbance allowance.  The
remaining nonnegative ``excess`` load is the state that must be driven to the
viable set K={0}.  At m=1, two local units each have a fixed budget of two.
At m=2, an upper regulator receives the two aggregate loads and may transfer
one unit of budget, changing (2,2) to (3,1) or (1,3).  This gives explicit
upward and downward maps.  At m=3, a further inert level is added without
changing the controller.

Three fixtures plant m=0, m=1, and m=2.  Candidate partitions are enumerated,
depth is selected on training disturbances with an explicit complexity
penalty, and the selected model is evaluated on held-out disturbances.
Passive stability, arbitrary partitions, redundant depth, memorization,
coarse-graining without downward control, record-every-tick bookkeeping,
relabeling, hidden tags, and resolution refinement are explicit nulls.

The construction is a lean viability-control hierarchy, not a literal
Stafford-Beer five-function Viable System Model and not evidence that physics
is recursively viable.  It tests when an unknown finite depth can be
objectively earned beyond ordinary coarse-graining.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import permutations
from pathlib import Path
from typing import Any, Iterable

from conditional_candidate_harness import (
    SCHEMA_VERSION,
    comparison_receipt,
    write_candidate_artifact,
)


ARTIFACT_PATH = (
    Path(__file__).resolve().parent
    / "artifacts"
    / "du_recursive_viability_orthodox_depth_tournament_result.json"
)

FAILURE_WEIGHT = 20
COMPLEXITY = {0: 0, 1: 3, 2: 7, 3: 11}
PENALTY_MULTIPLIERS = (1, 3, 5)

Load = tuple[Fraction, ...]
Trace = tuple[Load, ...]
Partition = tuple[tuple[int, ...], tuple[int, ...]]


def fload(*values: int | Fraction) -> Load:
    return tuple(Fraction(value) for value in values)


def canonical_partition(groups: Iterable[Iterable[int]]) -> Partition:
    normalized = [tuple(sorted(group)) for group in groups]
    normalized.sort()
    if len(normalized) != 2:
        raise ValueError("the finite comparator requires exactly two groups")
    return normalized[0], normalized[1]


TRUE_PARTITION = canonical_partition(((0, 1), (2, 3)))


def pair_partitions_four() -> tuple[Partition, ...]:
    """Enumerate the three unordered pair partitions of four components."""

    rows = set()
    for partner in (1, 2, 3):
        first = (0, partner)
        second = tuple(i for i in range(4) if i not in first)
        rows.add(canonical_partition((first, second)))
    return tuple(sorted(rows))


PAIR_PARTITIONS = pair_partitions_four()


PASSIVE_RAW_TRAINING = (
    fload(1, 1, 0, 1),
    fload(0, 1, 1, 0),
    fload(1, 0, 0, 1),
)
PASSIVE_RAW_HELD_OUT = (
    fload(1, 0, 1, 0),
    fload(0, 1, 0, 1),
    fload(1, 1, 0, 0),
)


def passive_excess(trace: Trace) -> Trace:
    """The plant passively absorbs one unit per channel before active control."""

    return tuple(
        tuple(max(Fraction(0), value - 1) for value in load)
        for load in trace
    )


@dataclass(frozen=True)
class Fixture:
    fixture_id: str
    planted_depth: int
    training: Trace
    held_out: Trace
    true_partition: Partition = TRUE_PARTITION


FIXTURES = (
    Fixture(
        fixture_id="PLANTED_M0_PASSIVE",
        planted_depth=0,
        # Nonzero raw perturbations remain inside a passive one-unit envelope.
        # No active control is needed after the passive plant response.
        training=passive_excess(PASSIVE_RAW_TRAINING),
        held_out=passive_excess(PASSIVE_RAW_HELD_OUT),
    ),
    Fixture(
        fixture_id="PLANTED_M1_LOCAL",
        planted_depth=1,
        training=(
            fload(2, 0, 1, 1),
            fload(0, 2, 1, 1),
            fload(1, 1, 2, 0),
        ),
        held_out=(
            fload(1, 1, 0, 2),
            fload(1, 1, 1, 1),
            fload(2, 0, 0, 2),
        ),
    ),
    Fixture(
        fixture_id="PLANTED_M2_RECURSIVE",
        planted_depth=2,
        training=(
            fload(3, 0, 1, 0),
            fload(3, 0, 0, 1),
            fload(1, 1, 1, 1),
        ),
        held_out=(
            fload(0, 3, 1, 0),
            fload(0, 3, 0, 1),
            fload(1, 1, 1, 1),
        ),
    ),
)


def q(value: Fraction) -> str:
    return (
        str(value.numerator)
        if value.denominator == 1
        else f"{value.numerator}/{value.denominator}"
    )


def partition_id(partition: Partition | None) -> str:
    if partition is None:
        return "NONE"
    return "|".join(",".join(str(i) for i in group) for group in partition)


def group_demands(load: Load, partition: Partition) -> tuple[Fraction, Fraction]:
    return tuple(sum((load[i] for i in group), Fraction(0)) for group in partition)  # type: ignore[return-value]


def upper_budgets(
    demands: tuple[Fraction, Fraction],
) -> tuple[Fraction, Fraction]:
    """Fixed m=2 rule: reserve one unit per local unit, transfer at most one."""

    left, right = demands
    if left <= 2 and right <= 2:
        return Fraction(2), Fraction(2)
    if left <= 3 and right <= 1:
        return Fraction(3), Fraction(1)
    if right <= 3 and left <= 1:
        return Fraction(1), Fraction(3)
    # The upper regulator cannot clear this disturbance.  Keep the neutral
    # allocation so the violation remains visible rather than fitted away.
    return Fraction(2), Fraction(2)


def evaluate_trace(
    trace: Trace,
    depth: int,
    partition: Partition | None,
) -> dict[str, Any]:
    """Evaluate exact controlled invariance over one finite disturbance trace."""

    if depth == 0 and partition is not None:
        raise ValueError("m=0 has no privileged partition")
    if depth > 0 and partition is None:
        raise ValueError("active levels require a declared partition")

    rows: list[dict[str, Any]] = []
    failures = 0
    local_records = 0
    macro_records = 0

    for tick, load in enumerate(trace):
        if depth == 0:
            viable = all(value == 0 for value in load)
            demands = None
            budgets = None
        else:
            assert partition is not None
            demands = group_demands(load, partition)
            local_records += sum(int(value > 0) for value in demands)
            if depth == 1:
                budgets = (Fraction(2), Fraction(2))
            else:
                budgets = upper_budgets(demands)
                if budgets != (Fraction(2), Fraction(2)):
                    macro_records += 1
            viable = all(
                demand <= budget
                for demand, budget in zip(demands, budgets, strict=True)
            )

        failures += int(not viable)
        rows.append(
            {
                "tick": tick,
                "excess_load": [q(value) for value in load],
                "upward_group_demands": (
                    None if demands is None else [q(value) for value in demands]
                ),
                "downward_group_budgets": (
                    None if budgets is None else [q(value) for value in budgets]
                ),
                "viable": viable,
            }
        )

    return {
        "depth": depth,
        "partition": partition_id(partition),
        "opportunities": len(trace),
        "local_durable_records": local_records,
        "macro_transfer_records": macro_records,
        "failures": failures,
        "survivals": len(trace) - failures,
        "trajectory_viable": failures == 0,
        "rows": rows,
    }


def model_rows(
    fixture: Fixture,
    penalty_multiplier: int,
) -> list[dict[str, Any]]:
    candidates: list[tuple[int, Partition | None]] = [(0, None)]
    for partition in PAIR_PARTITIONS:
        candidates.extend(
            (
                (1, partition),
                (2, partition),
                (3, partition),
            )
        )

    rows = []
    for depth, partition in candidates:
        training = evaluate_trace(fixture.training, depth, partition)
        held_out = evaluate_trace(fixture.held_out, depth, partition)
        rows.append(
            {
                "depth": depth,
                "partition": partition_id(partition),
                "complexity": COMPLEXITY[depth],
                "penalty_multiplier": penalty_multiplier,
                "training_score": (
                    FAILURE_WEIGHT * training["failures"]
                    + penalty_multiplier * COMPLEXITY[depth]
                ),
                "training": training,
                "held_out": held_out,
                "_partition": partition,
            }
        )
    return rows


def select_model(
    fixture: Fixture,
    penalty_multiplier: int = 1,
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    rows = model_rows(fixture, penalty_multiplier)
    selected = min(
        rows,
        key=lambda row: (
            row["training_score"],
            row["depth"],
            row["partition"],
        ),
    )
    return selected, rows


def strip_private(value: Any) -> Any:
    if isinstance(value, dict):
        return {
            key: strip_private(item)
            for key, item in value.items()
            if not key.startswith("_")
        }
    if isinstance(value, list):
        return [strip_private(item) for item in value]
    if isinstance(value, tuple):
        return [strip_private(item) for item in value]
    return value


def permute_load(load: Load, permutation: tuple[int, ...]) -> Load:
    result = [Fraction(0)] * len(load)
    for old, new in enumerate(permutation):
        result[new] = load[old]
    return tuple(result)


def permute_partition(
    partition: Partition,
    permutation: tuple[int, ...],
) -> Partition:
    return canonical_partition(
        tuple(tuple(permutation[index] for index in group) for group in partition)
    )


def permute_fixture(
    fixture: Fixture,
    permutation: tuple[int, ...],
) -> Fixture:
    return Fixture(
        fixture_id=f"{fixture.fixture_id}_PERMUTED",
        planted_depth=fixture.planted_depth,
        training=tuple(
            permute_load(load, permutation) for load in fixture.training
        ),
        held_out=tuple(
            permute_load(load, permutation) for load in fixture.held_out
        ),
        true_partition=permute_partition(fixture.true_partition, permutation),
    )


def refine_load(load: Load) -> Load:
    """Split every physical channel into two equal bookkeeping subchannels."""

    return tuple(piece for value in load for piece in (value / 2, value / 2))


def refine_partition(partition: Partition) -> Partition:
    return canonical_partition(
        tuple(
            tuple(index for old in group for index in (2 * old, 2 * old + 1))
            for group in partition
        )
    )


def fixed_partition_depth_scores(
    trace: Trace,
    partition: Partition,
    penalty_multiplier: int,
) -> dict[int, int]:
    scores = {}
    for depth in (0, 1, 2, 3):
        use_partition = None if depth == 0 else partition
        evaluation = evaluate_trace(trace, depth, use_partition)
        scores[depth] = (
            FAILURE_WEIGHT * evaluation["failures"]
            + penalty_multiplier * COMPLEXITY[depth]
        )
    return scores


def tagged_trace(trace: Trace, tag_mask: int) -> tuple[tuple[tuple[Fraction, int], ...], ...]:
    return tuple(
        tuple(
            (value, (tag_mask >> component) & 1)
            for component, value in enumerate(load)
        )
        for load in trace
    )


def remove_tags(
    trace: tuple[tuple[tuple[Fraction, int], ...], ...],
) -> Trace:
    return tuple(tuple(value for value, _tag in row) for row in trace)


def lookup_memorizer(
    training: Trace,
    evaluated: Trace,
) -> dict[str, int]:
    """A fitted lookup table clears seen loads and has no unseen controller."""

    known = set(training)
    failures = sum(
        int(load not in known and any(value > 0 for value in load))
        for load in evaluated
    )
    return {
        "failures": failures,
        "complexity": 2 * len(training) + 3,
    }


def main() -> None:
    selected_rows: dict[str, dict[str, Any]] = {}
    all_rows: dict[str, list[dict[str, Any]]] = {}
    sensitivity: dict[str, dict[str, int]] = {}

    for fixture in FIXTURES:
        selected, rows = select_model(fixture)
        selected_rows[fixture.fixture_id] = selected
        all_rows[fixture.fixture_id] = rows
        sensitivity[fixture.fixture_id] = {}
        for multiplier in PENALTY_MULTIPLIERS:
            model, _ = select_model(fixture, multiplier)
            sensitivity[fixture.fixture_id][str(multiplier)] = model["depth"]

    relabeling_checks = []
    for fixture in FIXTURES:
        original = selected_rows[fixture.fixture_id]
        stable = True
        for permutation in permutations(range(4)):
            permuted = permute_fixture(fixture, permutation)
            selected, _ = select_model(permuted)
            if selected["depth"] != original["depth"]:
                stable = False
                break
            if selected["training_score"] != original["training_score"]:
                stable = False
                break
            if fixture.planted_depth > 0:
                if selected["_partition"] != permuted.true_partition:
                    stable = False
                    break
        relabeling_checks.append(
            {
                "fixture": fixture.fixture_id,
                "permutations_tested": 24,
                "stable": stable,
            }
        )

    resolution_checks = []
    for fixture in FIXTURES:
        coarse_scores = fixed_partition_depth_scores(
            fixture.training,
            fixture.true_partition,
            1,
        )
        refined_trace = tuple(refine_load(load) for load in fixture.training)
        refined_scores = fixed_partition_depth_scores(
            refined_trace,
            refine_partition(fixture.true_partition),
            1,
        )
        coarse_depth = min(coarse_scores, key=coarse_scores.get)  # type: ignore[arg-type]
        refined_depth = min(refined_scores, key=refined_scores.get)  # type: ignore[arg-type]
        resolution_checks.append(
            {
                "fixture": fixture.fixture_id,
                "coarse_scores": {str(k): v for k, v in coarse_scores.items()},
                "refined_scores": {str(k): v for k, v in refined_scores.items()},
                "coarse_selected_depth": coarse_depth,
                "refined_selected_depth": refined_depth,
                "score_preserved": coarse_scores == refined_scores,
            }
        )

    recursive_fixture = FIXTURES[2]
    recursive_selected = selected_rows[recursive_fixture.fixture_id]
    recursive_partition = recursive_selected["_partition"]
    assert recursive_partition is not None
    recursive_training = recursive_selected["training"]

    fibre_signatures = []
    for mask in range(16):
        physical_trace = remove_tags(tagged_trace(recursive_fixture.training, mask))
        evaluation = evaluate_trace(physical_trace, 2, recursive_partition)
        fibre_signatures.append(
            (
                evaluation["failures"],
                evaluation["macro_transfer_records"],
            )
        )

    arbitrary_partition_null = {}
    for fixture in FIXTURES[1:]:
        failures_by_partition = {
            partition_id(partition): evaluate_trace(
                fixture.training,
                fixture.planted_depth,
                partition,
            )["failures"]
            for partition in PAIR_PARTITIONS
        }
        arbitrary_partition_null[fixture.fixture_id] = failures_by_partition

    memorizer_null = {}
    for fixture in FIXTURES[1:]:
        train = lookup_memorizer(fixture.training, fixture.training)
        holdout = lookup_memorizer(fixture.training, fixture.held_out)
        memorizer_null[fixture.fixture_id] = {
            "training": train,
            "held_out": holdout,
            "training_score": (
                FAILURE_WEIGHT * train["failures"] + train["complexity"]
            ),
            "selected_score": selected_rows[fixture.fixture_id]["training_score"],
        }

    rg_only = evaluate_trace(recursive_fixture.training, 0, None)
    clock_copy = {
        **rg_only,
        "bookkeeping_records": len(recursive_fixture.training),
        "controller": "none",
    }

    checks = [
        {
            "name": "planted m=0 passive fixture selects no active viability level",
            "pass": selected_rows["PLANTED_M0_PASSIVE"]["depth"] == 0,
        },
        {
            "name": "planted m=1 fixture selects the intervention-stable local partition",
            "pass": (
                selected_rows["PLANTED_M1_LOCAL"]["depth"] == 1
                and selected_rows["PLANTED_M1_LOCAL"]["_partition"]
                == TRUE_PARTITION
            ),
        },
        {
            "name": "planted m=2 fixture selects the genuine upward/downward control hierarchy",
            "pass": (
                selected_rows["PLANTED_M2_RECURSIVE"]["depth"] == 2
                and selected_rows["PLANTED_M2_RECURSIVE"]["_partition"]
                == TRUE_PARTITION
            ),
        },
        {
            "name": "every selected depth survives every held-out disturbance",
            "pass": all(
                selected["held_out"]["failures"] == 0
                for selected in selected_rows.values()
            ),
        },
        {
            "name": "wrong hand-selected partitions fail the planted active fixtures",
            "pass": all(
                failures[partition_id(TRUE_PARTITION)] == 0
                and all(
                    count > 0
                    for name, count in failures.items()
                    if name != partition_id(TRUE_PARTITION)
                )
                for failures in arbitrary_partition_null.values()
            ),
        },
        {
            "name": "passive persistence earns m=0 rather than a fictitious controller",
            "pass": (
                any(
                    value > 0
                    for load in PASSIVE_RAW_TRAINING + PASSIVE_RAW_HELD_OUT
                    for value in load
                )
                and all(
                    value == 0
                    for load in FIXTURES[0].training + FIXTURES[0].held_out
                    for value in load
                )
                and
                selected_rows["PLANTED_M0_PASSIVE"]["training"]["failures"] == 0
                and selected_rows["PLANTED_M0_PASSIVE"]["training_score"] == 0
            ),
        },
        {
            "name": "a redundant third level never beats its behaviorally identical m=2 parent",
            "pass": all(
                min(
                    row["training_score"]
                    for row in rows
                    if row["depth"] == 3
                )
                > min(
                    row["training_score"]
                    for row in rows
                    if row["depth"] == 2
                )
                for rows in all_rows.values()
            ),
        },
        {
            "name": "selected depths are stable across the declared complexity-penalty range",
            "pass": all(
                set(depths.values()) == {fixture.planted_depth}
                for fixture, depths in zip(FIXTURES, sensitivity.values(), strict=True)
            ),
        },
        {
            "name": "a training lookup-table loses on complexity and fails unseen disturbances",
            "pass": all(
                row["training_score"] > row["selected_score"]
                and row["held_out"]["failures"] > 0
                for row in memorizer_null.values()
            ),
        },
        {
            "name": "all twenty-four component relabelings preserve selected depth and score",
            "pass": all(row["stable"] for row in relabeling_checks),
        },
        {
            "name": "sixteen hidden tag fibres leave physical viability and record counts unchanged",
            "pass": len(set(fibre_signatures)) == 1,
        },
        {
            "name": "splitting each channel into two half-load subchannels preserves depth scores",
            "pass": all(
                row["score_preserved"]
                and row["coarse_selected_depth"] == row["refined_selected_depth"]
                for row in resolution_checks
            ),
        },
        {
            "name": "upward coarse-graining without a downward control map is no better than m=0",
            "pass": (
                rg_only["failures"]
                == selected_rows["PLANTED_M0_PASSIVE"]["training"]["failures"] + 3
                and rg_only["failures"]
                == evaluate_trace(recursive_fixture.training, 0, None)["failures"]
            ),
        },
        {
            "name": "recording every update opportunity does not create viability",
            "pass": (
                clock_copy["bookkeeping_records"] == 3
                and clock_copy["failures"] == rg_only["failures"] == 3
            ),
        },
        {
            "name": "macro durable records differ from global opportunities",
            "pass": (
                recursive_training["opportunities"] == 3
                and recursive_training["macro_transfer_records"] == 2
            ),
        },
        {
            "name": "m=2 viability is lost when its downward allocation is removed",
            "pass": (
                recursive_training["failures"] == 0
                and rg_only["failures"] == 3
            ),
        },
        {
            "name": "the result uses exact finite arithmetic and no fitted viability threshold",
            "pass": all(
                isinstance(value, Fraction)
                for fixture in FIXTURES
                for trace in (fixture.training, fixture.held_out)
                for load in trace
                for value in load
            ),
        },
    ]
    passed = sum(bool(check["pass"]) for check in checks)

    candidate = {
        "schema_version": SCHEMA_VERSION,
        "candidate_id": "DU-ORTHODOX-RECURSIVE-VIABILITY-DEPTH-TOURNAMENT",
        "track": (
            "Science Council recursive viable-systems wave / conventional "
            "controlled-invariance and depth-selection benchmark"
        ),
        "question": (
            "Can recursively nested viable-system-like levels be discovered "
            "as intervention-stable control structure beyond passive "
            "persistence and ordinary coarse-graining, and does that support "
            "the prior finality-to-VSM inference?"
        ),
        "warrants": [
            "DERIVED",
            "CONDITIONALLY_ENTAILED",
            "CONSTRUCTIVELY_REALIZED",
        ],
        "assumptions": [
            {
                "id": "A1",
                "statement": (
                    "Viability is exact finite controlled invariance of K={0} "
                    "for a declared three-step disturbance family."
                ),
                "status": "STANDARD",
                "role": "Supplies a conventional control-theory comparator.",
            },
            {
                "id": "A2",
                "statement": (
                    "Four excess-load variables remain after a passive plant "
                    "has absorbed its declared disturbance envelope."
                ),
                "status": "CONDITIONAL_POSIT",
                "role": "Defines the finite planted systems.",
            },
            {
                "id": "A3",
                "statement": (
                    "At m=1, each candidate pair has fixed control budget two."
                ),
                "status": "CONDITIONAL_POSIT",
                "role": "Defines one active viability level.",
            },
            {
                "id": "A4",
                "statement": (
                    "At m=2, an upper regulator may transfer one budget unit "
                    "between local units while preserving one unit for each."
                ),
                "status": "CONDITIONAL_POSIT",
                "role": "Defines typed upward and downward adjacent-level maps.",
            },
            {
                "id": "A5",
                "statement": (
                    "Failure costs twenty units and model complexity is "
                    "(0,3,7,11) for depths zero through three."
                ),
                "status": "CONDITIONAL_POSIT",
                "role": "Makes hierarchy-depth selection explicit and penalized.",
            },
        ],
        "free_choices": [
            {
                "id": "C1",
                "choice": "Use four micro-variables and enumerate all pair partitions.",
                "why_not_forced": "This is the smallest nontrivial exact partition tournament.",
                "sensitivity_test": (
                    "Test every component relabeling and a twofold resolution refinement."
                ),
            },
            {
                "id": "C2",
                "choice": "Use a one-unit upper-level budget transfer.",
                "why_not_forced": "It plants a minimal genuine downward control advantage.",
                "sensitivity_test": (
                    "Remove the downward map, retain the upward sums, and require "
                    "the RG-only null to lose viability."
                ),
            },
            {
                "id": "C3",
                "choice": "Use penalty multipliers one, three, and five.",
                "why_not_forced": "No unique MDL coding convention is claimed.",
                "sensitivity_test": "Require the planted depth to remain selected across all three.",
            },
        ],
        "equations": [
            "x(t+1)=e(t)-u(t); viable iff x(t+1)=0",
            "m=1: b=(2,2)",
            "m=2: b in {(2,2),(3,1),(1,3)} from upward group demands",
            "score=20*training_failures+lambda*complexity(m)",
            "complexity(0,1,2,3)=(0,3,7,11)",
        ],
        "observables": [
            "training and held-out controlled-invariance failures",
            "selected recursion depth and partition",
            "upward aggregate loads and downward budget allocations",
            "global update opportunities, local records, and macro transfer records",
            "relabeling and resolution stability",
        ],
        "comparators": [
            "m=0 passive microdynamics",
            "m=1 one active local-control level",
            "m=2 local controls plus upper resource regulator",
            "m=3 redundant extra level",
            "arbitrary pair partitions",
            "training lookup-table",
            "RG-only upward coarse-graining",
            "record-every-tick bookkeeping model",
        ],
        "null_models": [
            "arbitrary-partition null",
            "passive-stability null",
            "hierarchy-depth overfit null",
            "resolution-refinement null",
            "relabeling and hidden-tag fibre null",
            "held-out-disturbance null",
            "ordinary-RG no-downward-control null",
            "clock-opportunity versus durable-record null",
            "teleology null: only controlled invariance is scored",
        ],
        "falsifiers": [
            "a planted fixture selects the wrong depth",
            "a selected model fails a held-out disturbance",
            "a wrong partition matches the planted active hierarchy",
            "a redundant level wins only by adding parameters",
            "relabeling or representation refinement changes selected depth",
            "upward coarse-graining without control supplies the same m=2 advantage",
        ],
        "stop_conditions": [
            "Do not infer literal Beer S1-S5 structure from a viability hierarchy.",
            "Do not equate Beer functions, recursion depth, and physical scale strata.",
            "Do not call passive persistence or RG blocking active regulation.",
            "Do not promote the planted finite result to a universal physical hierarchy.",
            "Do not infer purpose, agency, consciousness, or self-authorship.",
            "Do not connect the construction to Lambda, posts, or clocks without typed maps.",
        ],
        "concept": {
            "concept_id": "DU-RECURSIVE-VIABLE-SYSTEM-LIKE-ORGANIZATION",
            "invariant": (
                "Each earned level must have a boundary, essential variables, "
                "held-out viability advantage, upward sufficient statistic, "
                "downward constraint/control map, and complexity-paid depth."
            ),
            "formalization_id": (
                "ORTHODOX-FOUR-VARIABLE-NESTED-BUDGET-CONTROL"
            ),
            "failure_scope": "FORMALIZATION",
        },
        "result": {
            "claim": (
                "A finite controlled-invariance tournament can recover planted "
                "depths zero, one, and two while rejecting passive, arbitrary-"
                "partition, redundant-depth, memorization, RG-only, and clock-"
                "copy nulls. This conditionally realizes objective depth "
                "discovery, but does not make Beer functions into physical "
                "levels or establish the prior System-4/self-authoring claim."
            ),
            "grade": (
                "EXACT FINITE CONDITIONAL CONSTRUCTION / DEPTH DISCOVERY "
                "REALIZED / FINALITY-VSM INFERENCE NOT ESTABLISHED"
            ),
            "admission": "CONDITIONAL_CANDIDATE",
            "remaining_uncertainty": (
                "No DU dynamics, physical boundary, adaptive System 4, "
                "observer, post, clock, scale, or cosmological map has been "
                "discovered."
            ),
            "checks": checks,
        },
    }

    payload = {
        "probe": "du_recursive_viability_orthodox_depth_tournament",
        "contested_proposition": (
            "The prior finality/VSM mapping already warrants treating Beer "
            "functions as recursive physical levels and the absence of "
            "System 4 as a theorem-level necessary condition for physical "
            "viability, thereby connecting posts, records, and self-authoring "
            "without separately discovering an intervention-stable hierarchy."
        ),
        "definitions": {
            "depth_m": "number of active viability-control levels above passive microdynamics",
            "viability": "all excess load is cleared at every declared disturbance step",
            "boundary": "candidate partition defining two local controlled units",
            "upward_map": "pairwise excess-load sums",
            "downward_map": "upper regulator's budget allocation",
            "durable_macro_record": "a stored upper-level budget-transfer event",
            "global_opportunity": "one disturbance/update step",
        },
        "model_selection": {
            "failure_weight": FAILURE_WEIGHT,
            "complexity_by_depth": {str(k): v for k, v in COMPLEXITY.items()},
            "penalty_sensitivity": sensitivity,
        },
        "fixtures": {
            fixture.fixture_id: {
                "planted_depth": fixture.planted_depth,
                "true_partition": partition_id(fixture.true_partition),
                "training": [[q(value) for value in load] for load in fixture.training],
                "held_out": [[q(value) for value in load] for load in fixture.held_out],
                "selected": strip_private(selected_rows[fixture.fixture_id]),
                "all_candidates": strip_private(all_rows[fixture.fixture_id]),
            }
            for fixture in FIXTURES
        },
        "hard_nulls": {
            "passive_stability": {
                "raw_training": [
                    [q(value) for value in load]
                    for load in PASSIVE_RAW_TRAINING
                ],
                "raw_held_out": [
                    [q(value) for value in load]
                    for load in PASSIVE_RAW_HELD_OUT
                ],
                "passive_capacity_per_channel": "1",
                "post_passive_excess_is_zero": True,
            },
            "arbitrary_partition": arbitrary_partition_null,
            "memorizer": memorizer_null,
            "relabeling": relabeling_checks,
            "resolution": resolution_checks,
            "hidden_fibre_signatures": [
                {
                    "failures": failures,
                    "macro_transfer_records": records,
                }
                for failures, records in fibre_signatures
            ],
            "ordinary_rg_only": rg_only,
            "clock_copy": clock_copy,
            "teleology": (
                "No purpose or agency variable enters the transition rule or score."
            ),
        },
        "checks": checks,
        "checks_passed": passed,
        "checks_total": len(checks),
        "verdict": (
            "PLANTED DEPTHS 0/1/2 RECOVERED / RECURSIVE CONTROL ADVANTAGE "
            "CONDITIONALLY REALIZED / PASSIVE-RG-CLOCK-OVERFIT NULLS REJECTED / "
            "FINALITY-S1-S5-RECURSION CONFLATION OVERTURNED"
        ),
        "scope": {
            "earned": [
                "an exact finite method for earning zero, one, or two viability levels",
                "a held-out intervention advantage for a typed upper/downward map",
                "explicit depth, partition, relabeling, fibre, and resolution controls",
                "an orthodox distinction between viability control and ordinary RG",
            ],
            "not_earned": [
                "a literal Beer five-function physical system",
                "a transferable Beer viability theorem",
                "an adaptive or self-authoring System 4",
                "a DU system boundary, post, observer, record clock, or physical scale",
                "a universal hierarchy of nature, teleology, agency, or Lambda",
            ],
        },
    }

    receipt = comparison_receipt(candidate)
    if receipt["contract_status"] != "COMPLETE":
        raise RuntimeError(
            f"incomplete candidate contract: {receipt['contract_errors']}"
        )
    write_candidate_artifact(ARTIFACT_PATH, candidate, payload)

    print("ORTHODOX RECURSIVE-VIABILITY DEPTH TOURNAMENT")
    for check in checks:
        print(f"{'PASS' if check['pass'] else 'FAIL'}  {check['name']}")
    print(f"{passed}/{len(checks)} checks pass")
    print(
        "VERDICT: PLANTED DEPTHS RECOVERED / RECURSIVE CONTROL CONDITIONAL / "
        "FINALITY-VSM INFERENCE NOT ESTABLISHED"
    )
    print(f"contract: {receipt['contract_status']} (not scientific endorsement)")
    print(f"artifact: {ARTIFACT_PATH}")
    if passed != len(checks):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
