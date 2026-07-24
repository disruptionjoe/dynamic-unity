#!/usr/bin/env python3
"""Exact finite controls for HC-DU-035A Layered Threshold Objectivity.

This probe keeps three predicates separate.

* Reconstruction: a declared evidence channel supports a history decision
  below a frozen Bayes-error threshold.
* Finality: authenticated, locked quorums cannot certify two incompatible
  histories under a declared Byzantine fault bound.
* Action capability: an independently declared action passes both a
  failure-risk limit and a cost-aware loss comparison.  Public irreversible
  capability additionally requires the declared finality predicate.

The finite calculations deliberately use known mathematics: quorum
intersection, Bayes/data-processing order, binomial concentration, gambler's
ruin, and a GHZ access structure.  Passing the probe does not show that
physical reality runs consensus, that a finite crossover is a critical phase
transition, or that a quantum access threshold is public classical finality.
"""

from __future__ import annotations

import itertools
import json
import math
from collections import defaultdict, deque
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any, Callable, Hashable, Iterable, Mapping


ARTIFACT_PATH = (
    Path(__file__).resolve().parent
    / "artifacts"
    / "du_layered_threshold_objectivity_result.json"
)


def fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def fraction_record(value: Fraction) -> dict[str, Any]:
    return {"exact": fraction_text(value), "decimal": float(value)}


@dataclass
class CheckBook:
    checks: list[dict[str, Any]]

    def add(self, name: str, passed: bool, detail: Any = None) -> None:
        self.checks.append(
            {"name": name, "passed": bool(passed), "detail": detail}
        )

    @property
    def passed(self) -> int:
        return sum(check["passed"] for check in self.checks)


def quorum_safe(population: int, faults: int, quorum: int) -> bool:
    """Whether every two q-quorums share more than f validators."""
    return 2 * quorum > population + faults


def quorum_available(population: int, faults: int, quorum: int) -> bool:
    """Whether a quorum remains possible if every faulty validator is silent."""
    return quorum <= population - faults


def minimum_intersection(population: int, quorum: int) -> int:
    return max(0, 2 * quorum - population)


def minimum_safe_quorum(population: int, faults: int) -> int:
    return (population + faults) // 2 + 1


def split_view_witness(
    population: int, faults: int, quorum: int
) -> dict[str, list[int]] | None:
    """Return two q-quorums whose intersection can be wholly Byzantine."""
    if quorum_safe(population, faults, quorum):
        return None
    overlap = minimum_intersection(population, quorum)
    left = list(range(quorum))
    if overlap:
        right = list(range(overlap)) + list(range(quorum, population))
    else:
        right = list(range(quorum, 2 * quorum))
    if len(right) != quorum:
        raise AssertionError("invalid split-view construction")
    shared = sorted(set(left) & set(right))
    if len(shared) > faults:
        raise AssertionError("split-view overlap exceeds fault budget")
    return {
        "left_certificate": left,
        "right_certificate": right,
        "byzantine_intersection": shared,
    }


def exhaustive_quorum_check(max_population: int) -> dict[str, int]:
    cases = 0
    safe_cases = 0
    unsafe_cases = 0
    for population in range(1, max_population + 1):
        validators = tuple(range(population))
        for faults in range(population + 1):
            for quorum in range(1, population + 1):
                quorums = tuple(
                    itertools.combinations(validators, quorum)
                )
                exact = all(
                    len(set(left) & set(right)) > faults
                    for left in quorums
                    for right in quorums
                )
                formula = quorum_safe(population, faults, quorum)
                if exact != formula:
                    raise AssertionError(
                        (population, faults, quorum, exact, formula)
                    )
                witness = split_view_witness(
                    population, faults, quorum
                )
                if formula:
                    safe_cases += 1
                    if witness is not None:
                        raise AssertionError("safe case returned a split view")
                else:
                    unsafe_cases += 1
                    if witness is None:
                        raise AssertionError("unsafe case lacks split view")
                cases += 1
    return {
        "parameter_cases": cases,
        "safe_cases": safe_cases,
        "unsafe_cases": unsafe_cases,
    }


def bayes_error(
    plus: Mapping[Hashable, Fraction],
    minus: Mapping[Hashable, Fraction],
) -> Fraction:
    """Optimal zero-one Bayes error for equal priors."""
    outcomes = set(plus) | set(minus)
    return sum(
        (min(plus.get(outcome, Fraction(0)),
             minus.get(outcome, Fraction(0))) for outcome in outcomes),
        Fraction(0),
    ) / 2


def product_channel(
    channel: Mapping[Hashable, Fraction], copies: int
) -> dict[tuple[Hashable, ...], Fraction]:
    result: dict[tuple[Hashable, ...], Fraction] = {}
    outcomes = tuple(channel)
    for values in itertools.product(outcomes, repeat=copies):
        probability = Fraction(1)
        for value in values:
            probability *= channel[value]
        result[values] = probability
    return result


def pushforward(
    channel: Mapping[Hashable, Fraction],
    mapping: Callable[[Hashable], Hashable],
) -> dict[Hashable, Fraction]:
    result: defaultdict[Hashable, Fraction] = defaultdict(Fraction)
    for outcome, probability in channel.items():
        result[mapping(outcome)] += probability
    return dict(result)


def hardening_fixture() -> dict[str, Any]:
    """Two variable-strength reports; scalar signs erase visible reliability."""
    plus_single = {
        ("S", 1): Fraction(9, 20),
        ("S", -1): Fraction(1, 20),
        ("W", 1): Fraction(3, 10),
        ("W", -1): Fraction(1, 5),
    }
    minus_single = {
        (kind, sign): plus_single[(kind, -sign)]
        for kind, sign in plus_single
    }
    plus_raw = product_channel(plus_single, 2)
    minus_raw = product_channel(minus_single, 2)
    raw_error = bayes_error(plus_raw, minus_raw)

    hard_map = lambda pair: tuple(value[1] for value in pair)
    plus_hard = pushforward(plus_raw, hard_map)
    minus_hard = pushforward(minus_raw, hard_map)
    hard_error = bayes_error(plus_hard, minus_hard)

    # The Bayes/data-processing inequality should hold for every binary local
    # relabeling of this four-outcome fragment, not only for sign hardening.
    outcomes = tuple(sorted(plus_single))
    binary_maps_checked = 0
    binary_violations = 0
    for labels in itertools.product((0, 1), repeat=len(outcomes)):
        local_map = dict(zip(outcomes, labels, strict=True))
        pair_map = lambda pair, m=local_map: (m[pair[0]], m[pair[1]])
        coarse_error = bayes_error(
            pushforward(plus_raw, pair_map),
            pushforward(minus_raw, pair_map),
        )
        binary_maps_checked += 1
        if coarse_error < raw_error:
            binary_violations += 1

    return {
        "single_fragment_plus_channel": {
            f"{key[0]}:{key[1]:+d}": fraction_text(value)
            for key, value in sorted(plus_single.items())
        },
        "reliability_types": {
            "S_accuracy": "9/10",
            "W_accuracy": "3/5",
            "type_probability_each": "1/2",
        },
        "raw_joint_bayes_error": fraction_record(raw_error),
        "local_sign_hardened_bayes_error": fraction_record(hard_error),
        "strict_error_penalty": fraction_record(hard_error - raw_error),
        "binary_local_maps_checked": binary_maps_checked,
        "binary_data_processing_violations": binary_violations,
    }


def majority_error(sample_count: int, accuracy: Fraction) -> Fraction:
    if sample_count % 2 != 1:
        raise ValueError("odd sample count required")
    maximum_correct_for_error = sample_count // 2
    return sum(
        (
            Fraction(math.comb(sample_count, correct))
            * accuracy**correct
            * (1 - accuracy) ** (sample_count - correct)
            for correct in range(maximum_correct_for_error + 1)
        ),
        Fraction(0),
    )


def binomial_upper_tail(
    trials: int, probability: Fraction, minimum_successes: int
) -> Fraction:
    if minimum_successes <= 0:
        return Fraction(1)
    if minimum_successes > trials:
        return Fraction(0)
    return sum(
        (
            Fraction(math.comb(trials, successes))
            * probability**successes
            * (1 - probability) ** (trials - successes)
            for successes in range(minimum_successes, trials + 1)
        ),
        Fraction(0),
    )


def stochastic_lock_fixture() -> dict[str, Any]:
    """Convert quorum intersection into an honest-lock failure margin."""
    population, faults, quorum = 10, 2, 7
    honest = population - faults
    required_honest_double_signers = max(
        0, 2 * quorum - population - faults
    )
    marginal_lock_failure = Fraction(1, 100)
    independent_conflict_possible = binomial_upper_tail(
        honest,
        marginal_lock_failure,
        required_honest_double_signers,
    )
    # Common mode: with probability lambda every honest lock fails,
    # otherwise none do.  Each validator has the same marginal lambda.
    common_mode_conflict_possible = marginal_lock_failure
    return {
        "N": population,
        "f": faults,
        "q": quorum,
        "deterministically_safe_when_honest_locks_hold": quorum_safe(
            population, faults, quorum
        ),
        "honest_validators": honest,
        "required_honest_double_signers_for_conflict": (
            required_honest_double_signers
        ),
        "honest_lock_failures_tolerated": (
            required_honest_double_signers - 1
        ),
        "per_honest_validator_failure_marginal": fraction_record(
            marginal_lock_failure
        ),
        "independent_failure_conflict_possibility": fraction_record(
            independent_conflict_possible
        ),
        "common_mode_failure_conflict_possibility": fraction_record(
            common_mode_conflict_possible
        ),
        "interpretation": (
            "under a worst-case scheduler, incompatible certificates are "
            "combinatorially possible exactly when enough honest locks "
            "double-sign"
        ),
    }


def iid_and_common_shock_fixture() -> dict[str, Any]:
    accuracy = Fraction(3, 4)
    common_shock_weight = Fraction(1, 5)
    rows: list[dict[str, Any]] = []
    for sample_count in (1, 3, 5, 9, 17, 33):
        iid_error = majority_error(sample_count, accuracy)
        shock_error = (
            common_shock_weight * (1 - accuracy)
            + (1 - common_shock_weight) * iid_error
        )
        hoeffding = math.exp(
            -2
            * sample_count
            * (float(accuracy) - 0.5) ** 2
        )
        rows.append(
            {
                "sample_count": sample_count,
                "iid_error": fraction_record(iid_error),
                "hoeffding_upper_bound": hoeffding,
                "common_shock_error": fraction_record(shock_error),
            }
        )
    return {
        "single_fragment_accuracy": fraction_record(accuracy),
        "common_shock_weight": fraction_record(common_shock_weight),
        "common_shock_error_floor": fraction_record(
            common_shock_weight * (1 - accuracy)
        ),
        "rows": rows,
    }


def first_odd_threshold(
    accuracy: Fraction, maximum_error: Fraction, limit: int = 199
) -> tuple[int, Fraction]:
    for sample_count in range(1, limit + 1, 2):
        error = majority_error(sample_count, accuracy)
        if error <= maximum_error:
            return sample_count, error
    raise AssertionError("threshold not found within finite search")


def layer_case(
    name: str,
    reconstruction_error: Fraction,
    population: int,
    faults: int,
    quorum: int,
    verification_cost: Fraction,
) -> dict[str, Any]:
    reconstruction_limit = Fraction(1, 5)
    action_failure_limit = Fraction(3, 20)
    abstain_loss = Fraction(3, 10)
    reconstruction = reconstruction_error <= reconstruction_limit
    finality = quorum_safe(population, faults, quorum)
    commit_loss = reconstruction_error + verification_cost
    capability = (
        reconstruction
        and finality
        and reconstruction_error <= action_failure_limit
        and commit_loss < abstain_loss
    )
    return {
        "name": name,
        "reconstruction": reconstruction,
        "finality": finality,
        "capability": capability,
        "reconstruction_error": fraction_text(reconstruction_error),
        "quorum": {"N": population, "f": faults, "q": quorum},
        "verification_cost": fraction_text(verification_cost),
        "commit_expected_loss": fraction_text(commit_loss),
        "abstain_loss": fraction_text(abstain_loss),
    }


def layered_separation_fixture() -> list[dict[str, Any]]:
    return [
        layer_case(
            "reconstruction_without_finality",
            Fraction(1, 10),
            3,
            1,
            2,
            Fraction(1, 20),
        ),
        layer_case(
            "finality_without_reconstruction",
            Fraction(1, 2),
            4,
            1,
            3,
            Fraction(1, 20),
        ),
        layer_case(
            "reconstruction_and_finality_without_capability",
            Fraction(1, 10),
            4,
            1,
            3,
            Fraction(1, 4),
        ),
        layer_case(
            "all_three_layers",
            Fraction(1, 10),
            4,
            1,
            3,
            Fraction(1, 20),
        ),
    ]


def truth_cube_fixture() -> list[dict[str, Any]]:
    """Realize every (full reconstruction, finality, action capability) triple."""
    rows: list[dict[str, Any]] = []
    for reconstruction_target, finality_target, capability_target in (
        itertools.product((False, True), repeat=3)
    ):
        if reconstruction_target:
            evidence = "full_GJ"
            full_history_error = Fraction(0)
            action_failure = Fraction(0)
        elif capability_target:
            evidence = "coarse_G"
            full_history_error = Fraction(1, 2)
            action_failure = Fraction(0)
        else:
            evidence = "none"
            full_history_error = Fraction(3, 4)
            action_failure = Fraction(1, 2)
        population, faults, quorum = (
            (4, 1, 3) if finality_target else (3, 1, 2)
        )
        actuator = capability_target
        action_benefit = Fraction(1)
        action_cost = Fraction(1, 4)
        reconstruction = full_history_error == 0
        finality = quorum_safe(population, faults, quorum)
        action_capability = (
            actuator
            and action_failure == 0
            and action_benefit > action_cost
        )
        rows.append(
            {
                "truth_vector": [
                    reconstruction,
                    finality,
                    action_capability,
                ],
                "evidence": evidence,
                "full_history_error": fraction_text(full_history_error),
                "action_relevant_G_error": fraction_text(action_failure),
                "quorum": {
                    "N": population,
                    "f": faults,
                    "q": quorum,
                },
                "actuator_enabled": actuator,
                "action_benefit": fraction_text(action_benefit),
                "action_cost": fraction_text(action_cost),
                "public_irreversible_capability": (
                    finality and action_capability
                ),
            }
        )
    return rows


def metastable_fixture() -> dict[str, Any]:
    """Biased random walk on 0..3, starting after crossing confidence state 2."""
    upward = Fraction(2, 3)
    downward = 1 - upward
    rollback_from_2 = downward**2 / (1 - upward * downward)
    rollback_from_1 = downward + upward * rollback_from_2
    recurrence_1 = (
        rollback_from_1
        == downward + upward * rollback_from_2
    )
    recurrence_2 = rollback_from_2 == downward * rollback_from_1
    return {
        "states": [0, 1, 2, 3],
        "confidence_crossing_state": 2,
        "hard_final_state": 3,
        "up_probability": fraction_record(upward),
        "rollback_before_hard_finality_from_crossing": fraction_record(
            rollback_from_2
        ),
        "recurrences_hold": recurrence_1 and recurrence_2,
        "hard_finality_rollback_under_frozen_absorbing_model": "0/1",
    }


def connected_components(
    population: int, edges: Iterable[tuple[int, int]]
) -> list[list[int]]:
    neighbors = {node: set() for node in range(population)}
    for left, right in edges:
        neighbors[left].add(right)
        neighbors[right].add(left)
    unseen = set(range(population))
    components: list[list[int]] = []
    while unseen:
        start = min(unseen)
        unseen.remove(start)
        queue = deque([start])
        component = [start]
        while queue:
            node = queue.popleft()
            for neighbor in sorted(neighbors[node]):
                if neighbor in unseen:
                    unseen.remove(neighbor)
                    queue.append(neighbor)
                    component.append(neighbor)
        components.append(sorted(component))
    return components


def topology_fixture() -> dict[str, Any]:
    population, faults, quorum = 7, 2, 5
    complete_edges = tuple(itertools.combinations(range(population), 2))
    split_edges = tuple(itertools.combinations(range(4), 2)) + tuple(
        itertools.combinations(range(4, 7), 2)
    )
    complete_components = connected_components(population, complete_edges)
    split_components = connected_components(population, split_edges)
    return {
        "N": population,
        "f": faults,
        "q": quorum,
        "quorum_safety": quorum_safe(population, faults, quorum),
        "complete_graph_component_sizes": [
            len(component) for component in complete_components
        ],
        "split_graph_component_sizes": [
            len(component) for component in split_components
        ],
        "complete_graph_can_disseminate_quorum": any(
            len(component) >= quorum for component in complete_components
        ),
        "split_graph_can_disseminate_quorum": any(
            len(component) >= quorum for component in split_components
        ),
    }


Density = dict[tuple[int, int], Fraction]


def ghz_density(phase: int) -> Density:
    if phase not in (-1, 1):
        raise ValueError("phase must be plus or minus one")
    return {
        (0, 0): Fraction(1, 2),
        (7, 7): Fraction(1, 2),
        (0, 7): Fraction(phase, 2),
        (7, 0): Fraction(phase, 2),
    }


def project_bits(index: int, keep: tuple[int, ...], qubits: int = 3) -> int:
    result = 0
    for output_position, qubit in enumerate(keep):
        bit = (index >> (qubits - qubit - 1)) & 1
        result |= bit << (len(keep) - output_position - 1)
    return result


def partial_trace(density: Density, keep: tuple[int, ...]) -> Density:
    traced = tuple(qubit for qubit in range(3) if qubit not in keep)
    result: defaultdict[tuple[int, int], Fraction] = defaultdict(Fraction)
    for (left, right), value in density.items():
        if all(
            ((left >> (2 - qubit)) & 1)
            == ((right >> (2 - qubit)) & 1)
            for qubit in traced
        ):
            result[
                (project_bits(left, keep), project_bits(right, keep))
            ] += value
    return {
        key: value for key, value in result.items() if value != 0
    }


def trace_product(left: Density, right: Density) -> Fraction:
    return sum(
        (
            value * right.get((column, row), Fraction(0))
            for (row, column), value in left.items()
        ),
        Fraction(0),
    )


def ghz_access_fixture() -> dict[str, Any]:
    plus = ghz_density(1)
    minus = ghz_density(-1)
    proper_subsets: list[dict[str, Any]] = []
    for subset_size in (1, 2):
        for keep in itertools.combinations(range(3), subset_size):
            equal = partial_trace(plus, keep) == partial_trace(minus, keep)
            proper_subsets.append(
                {"coalition": list(keep), "reduced_states_equal": equal}
            )
    local_x_distributions: dict[str, dict[str, str]] = {}
    for phase, label in ((1, "plus"), (-1, "minus")):
        distribution: dict[str, str] = {}
        for local_signs in itertools.product((-1, 1), repeat=3):
            probability = (
                Fraction(1, 4)
                if math.prod(local_signs) == phase
                else Fraction(0)
            )
            distribution[
                ",".join(f"{sign:+d}" for sign in local_signs)
            ] = fraction_text(probability)
        local_x_distributions[label] = distribution
    return {
        "proper_subset_controls": proper_subsets,
        "all_proper_subsets_indistinguishable": all(
            row["reduced_states_equal"] for row in proper_subsets
        ),
        "full_plus_measurement_on_plus": fraction_text(
            trace_product(plus, plus)
        ),
        "full_plus_measurement_on_minus": fraction_text(
            trace_product(minus, plus)
        ),
        "full_states_orthogonal": trace_product(plus, minus) == 0,
        "local_X_measurements": {
            "distributions": local_x_distributions,
            "pooled_parity_recovers_phase": True,
            "requires_entangled_collective_measurement": False,
        },
        "interpretation": (
            "exact 3-of-3 access to one classical phase bit; authenticated "
            "pooling of local X outcomes suffices, so this is neither a "
            "general quantum-secret code nor a genuinely collective-quantum "
            "hardening advantage or public-finality result"
        ),
    }


def project_bits_two(index: int, keep: tuple[int, ...]) -> int:
    result = 0
    for output_position, qubit in enumerate(keep):
        bit = (index >> (1 - qubit)) & 1
        result |= bit << (len(keep) - output_position - 1)
    return result


def partial_trace_two_qubits(
    density: Density, keep: tuple[int, ...]
) -> Density:
    traced = tuple(qubit for qubit in range(2) if qubit not in keep)
    result: defaultdict[tuple[int, int], Fraction] = defaultdict(Fraction)
    for (left, right), value in density.items():
        if all(
            ((left >> (1 - qubit)) & 1)
            == ((right >> (1 - qubit)) & 1)
            for qubit in traced
        ):
            result[
                (
                    project_bits_two(left, keep),
                    project_bits_two(right, keep),
                )
            ] += value
    return {
        key: value for key, value in result.items() if value != 0
    }


def bell_density(parity: int, phase: int) -> Density:
    if parity not in (0, 1) or phase not in (-1, 1):
        raise ValueError("invalid Bell label")
    left = 0 if parity == 0 else 1
    right = 3 if parity == 0 else 2
    return {
        (left, left): Fraction(1, 2),
        (right, right): Fraction(1, 2),
        (left, right): Fraction(phase, 2),
        (right, left): Fraction(phase, 2),
    }


def bell_joint_channel_fixture() -> dict[str, Any]:
    states = {
        f"parity_{parity}_phase_{phase:+d}": bell_density(parity, phase)
        for parity in (0, 1)
        for phase in (-1, 1)
    }
    single_marginals_equal = True
    for keep in ((0,), (1,)):
        marginals = [
            partial_trace_two_qubits(state, keep)
            for state in states.values()
        ]
        single_marginals_equal &= all(
            marginal == marginals[0] for marginal in marginals[1:]
        )
    joint_probabilities: dict[str, dict[str, str]] = {}
    for input_label, input_state in states.items():
        joint_probabilities[input_label] = {
            outcome_label: fraction_text(
                trace_product(input_state, projector)
            )
            for outcome_label, projector in states.items()
        }
    return {
        "single_qubit_marginals_all_equal": single_marginals_equal,
        "joint_Bell_measurement_probabilities": joint_probabilities,
        "joint_channel_perfectly_distinguishes_all_four": all(
            probability
            == ("1/1" if input_label == outcome_label else "0/1")
            for input_label, row in joint_probabilities.items()
            for outcome_label, probability in row.items()
        ),
        "interpretation": (
            "direct joint quantum channel control; LOCC impossibility and "
            "public finality are not proved by this finite check"
        ),
    }


def provenance_fixture() -> dict[str, Any]:
    claimed_signers = ["A", "A", "B"]
    unique_signers = sorted(set(claimed_signers))
    required = 3
    return {
        "claimed_fragment_count": len(claimed_signers),
        "unique_authenticated_provenance_count": len(unique_signers),
        "required_quorum": required,
        "naive_count_passes": len(claimed_signers) >= required,
        "authenticated_count_passes": len(unique_signers) >= required,
        "interpretation": "replay or Sybil aliases do not create quorum support",
    }


def interpolate_secret(
    left: tuple[int, int], right: tuple[int, int], prime: int
) -> int:
    """Degree-one polynomial intercept through two finite-field points."""
    x_left, y_left = left
    x_right, y_right = right
    slope = (
        (y_right - y_left)
        * pow((x_right - x_left) % prime, -1, prime)
    ) % prime
    return (y_left - slope * x_left) % prime


def secret_sharing_fixture() -> dict[str, Any]:
    shares = [(1, 0), (2, 0), (3, 1)]
    first_secret = interpolate_secret(shares[0], shares[1], 5)
    second_secret = interpolate_secret(shares[1], shares[2], 5)
    return {
        "field": "F_5",
        "claimed_access_structure": "2-of-3",
        "shares": [list(share) for share in shares],
        "coalition_12_secret": first_secret,
        "coalition_23_secret": second_secret,
        "inconsistent_authorized_reconstructions": (
            first_secret != second_secret
        ),
        "interpretation": (
            "threshold reconstruction without dealer consistency or "
            "verifiability is not finality"
        ),
    }


def build_artifact() -> dict[str, Any]:
    checks = CheckBook([])

    quorum_enumeration = exhaustive_quorum_check(8)
    checks.add(
        "quorum_intersection_iff_2q_gt_N_plus_f",
        quorum_enumeration["parameter_cases"] > 0,
        quorum_enumeration,
    )
    unsafe = split_view_witness(3, 1, 2)
    safe = split_view_witness(4, 1, 3)
    checks.add(
        "smallest_named_split_view_N3_f1_q2",
        unsafe
        == {
            "left_certificate": [0, 1],
            "right_certificate": [0, 2],
            "byzantine_intersection": [0],
        },
        unsafe,
    )
    checks.add(
        "named_safe_quorum_N4_f1_q3",
        safe is None and quorum_safe(4, 1, 3),
    )
    checks.add(
        "safety_and_erasure_availability_are_distinct",
        quorum_safe(4, 1, 4)
        and not quorum_available(4, 1, 4)
        and quorum_available(4, 1, 3),
    )
    stochastic_locks = stochastic_lock_fixture()
    checks.add(
        "honest_intersection_surplus_sets_lock_failure_margin",
        stochastic_locks[
            "required_honest_double_signers_for_conflict"
        ]
        == 2
        and stochastic_locks["honest_lock_failures_tolerated"] == 1
        and Fraction(
            stochastic_locks[
                "common_mode_failure_conflict_possibility"
            ]["exact"]
        )
        > Fraction(
            stochastic_locks[
                "independent_failure_conflict_possibility"
            ]["exact"]
        ),
        stochastic_locks,
    )

    hardening = hardening_fixture()
    checks.add(
        "deterministic_binary_hardening_never_beats_raw_channel",
        hardening["binary_data_processing_violations"] == 0,
        {
            "maps_checked": hardening["binary_local_maps_checked"],
            "violations": hardening["binary_data_processing_violations"],
        },
    )
    checks.add(
        "local_sign_hardening_is_strictly_worse",
        Fraction(hardening["strict_error_penalty"]["exact"]) > 0,
        hardening,
    )

    stochastic = iid_and_common_shock_fixture()
    rows = stochastic["rows"]
    checks.add(
        "iid_majority_error_decreases_on_declared_grid",
        all(
            Fraction(rows[index + 1]["iid_error"]["exact"])
            < Fraction(rows[index]["iid_error"]["exact"])
            for index in range(len(rows) - 1)
        ),
    )
    checks.add(
        "hoeffding_bounds_each_iid_error",
        all(
            row["iid_error"]["decimal"]
            <= row["hoeffding_upper_bound"] + 1e-15
            for row in rows
        ),
    )
    checks.add(
        "same_marginal_accuracy_common_shock_has_error_floor",
        Fraction(rows[0]["iid_error"]["exact"])
        == Fraction(rows[0]["common_shock_error"]["exact"])
        and all(
            Fraction(row["common_shock_error"]["exact"])
            >= Fraction(stochastic["common_shock_error_floor"]["exact"])
            for row in rows
        ),
    )

    reconstruction_threshold = first_odd_threshold(
        Fraction(3, 4), Fraction(1, 10)
    )
    capability_risk_threshold = first_odd_threshold(
        Fraction(3, 4), Fraction(1, 50)
    )
    checks.add(
        "reconstruction_and_capability_risk_thresholds_separate",
        capability_risk_threshold[0] > reconstruction_threshold[0],
        {
            "reconstruction": {
                "maximum_error": "1/10",
                "first_odd_N": reconstruction_threshold[0],
                "error": fraction_text(reconstruction_threshold[1]),
            },
            "capability_risk": {
                "maximum_error": "1/50",
                "first_odd_N": capability_risk_threshold[0],
                "error": fraction_text(capability_risk_threshold[1]),
            },
        },
    )

    layers = layered_separation_fixture()
    layer_index = {row["name"]: row for row in layers}
    checks.add(
        "reconstruction_does_not_imply_finality",
        layer_index["reconstruction_without_finality"][
            "reconstruction"
        ]
        and not layer_index["reconstruction_without_finality"]["finality"],
    )
    checks.add(
        "finality_does_not_imply_reconstruction",
        layer_index["finality_without_reconstruction"]["finality"]
        and not layer_index["finality_without_reconstruction"][
            "reconstruction"
        ],
    )
    checks.add(
        "reconstruction_plus_finality_does_not_imply_capability",
        layer_index[
            "reconstruction_and_finality_without_capability"
        ]["reconstruction"]
        and layer_index[
            "reconstruction_and_finality_without_capability"
        ]["finality"]
        and not layer_index[
            "reconstruction_and_finality_without_capability"
        ]["capability"],
    )
    checks.add(
        "all_three_layers_are_jointly_realizable",
        all(
            layer_index["all_three_layers"][field]
            for field in ("reconstruction", "finality", "capability")
        ),
    )
    truth_cube = truth_cube_fixture()
    checks.add(
        "full_reconstruction_finality_action_capability_truth_cube",
        {
            tuple(row["truth_vector"]) for row in truth_cube
        }
        == set(itertools.product((False, True), repeat=3))
        and all(
            row["public_irreversible_capability"]
            == (row["truth_vector"][1] and row["truth_vector"][2])
            for row in truth_cube
        ),
        {
            "truth_vectors": [
                row["truth_vector"] for row in truth_cube
            ],
            "public_capability_rule": (
                "finality AND action_relevant_capability"
            ),
        },
    )

    metastability = metastable_fixture()
    checks.add(
        "metastable_confidence_crossing_can_roll_back",
        Fraction(
            metastability[
                "rollback_before_hard_finality_from_crossing"
            ]["exact"]
        )
        == Fraction(1, 7)
        and metastability["recurrences_hold"],
        metastability,
    )

    topology = topology_fixture()
    checks.add(
        "quorum_safety_does_not_supply_dissemination_availability",
        topology["quorum_safety"]
        and topology["complete_graph_can_disseminate_quorum"]
        and not topology["split_graph_can_disseminate_quorum"],
        topology,
    )

    provenance = provenance_fixture()
    checks.add(
        "authenticated_provenance_defeats_replay_counting",
        provenance["naive_count_passes"]
        and not provenance["authenticated_count_passes"],
        provenance,
    )
    secret_sharing = secret_sharing_fixture()
    checks.add(
        "threshold_reconstruction_does_not_supply_consistency",
        secret_sharing["inconsistent_authorized_reconstructions"]
        and secret_sharing["coalition_12_secret"] == 0
        and secret_sharing["coalition_23_secret"] == 3,
        secret_sharing,
    )

    quantum = ghz_access_fixture()
    checks.add(
        "GHZ_phase_is_exact_3_of_3_classical_bit_access",
        quantum["all_proper_subsets_indistinguishable"]
        and quantum["full_states_orthogonal"]
        and quantum["full_plus_measurement_on_plus"] == "1/1"
        and quantum["full_plus_measurement_on_minus"] == "0/1",
        quantum,
    )
    bell_joint = bell_joint_channel_fixture()
    checks.add(
        "Bell_basis_direct_joint_channel_beats_single_marginals",
        bell_joint["single_qubit_marginals_all_equal"]
        and bell_joint[
            "joint_channel_perfectly_distinguishes_all_four"
        ],
        bell_joint,
    )
    checks.add(
        "finite_threshold_is_not_labeled_critical_phase_transition",
        True,
        {
            "order_parameter": None,
            "thermodynamic_or_scaling_limit": None,
            "grade": "FINITE_CROSSOVER_OR_ACCESS_THRESHOLD_ONLY",
        },
    )

    if checks.passed != len(checks.checks):
        failed = [
            check["name"]
            for check in checks.checks
            if not check["passed"]
        ]
        raise AssertionError(f"failed checks: {failed}")

    return {
        "metadata": {
            "run_id": "RUN-20260724-174434-hc-du-035a-layered-threshold",
            "hardening_id": "HC-DU-035A",
            "claim_grade": (
                "EXACT FINITE CLASSICAL SPECIALIZATIONS "
                "PLUS QUANTUM ACCESS CONTROL"
            ),
            "novelty_status": (
                "KNOWN COMPONENT THEOREMS / "
                "CROSS-PLATFORM CONJUNCTION SEARCH-INCOMPLETE"
            ),
            "scope": (
                "frozen finite evidence, quorum, action, topology, "
                "metastability, and quantum access fixtures"
            ),
        },
        "summary": {
            "checks_passed": checks.passed,
            "checks_total": len(checks.checks),
            "result": "LAYERED_THRESHOLDS_SEPARATE",
            "public_finality_result": (
                "CLASSICAL_LOCKED_QUORUM_CONTROL_EXACT"
            ),
            "quantum_result": (
                "GHZ_CLASSICAL_PHASE_ACCESS_AND_BELL_JOINT_CHANNEL_CONTROLS"
            ),
            "phase_transition_result": (
                "NOT_ESTABLISHED_BY_FINITE_THRESHOLDS"
            ),
        },
        "results": {
            "quorum": {
                "condition": "2q > N + f",
                "minimum_safe_quorum": "floor((N+f)/2)+1",
                "enumeration": quorum_enumeration,
                "unsafe_control_N3_f1_q2": unsafe,
                "safe_control_N4_f1_q3": {
                    "safe": quorum_safe(4, 1, 3),
                    "available_under_one_silent_fault": quorum_available(
                        4, 1, 3
                    ),
                },
            },
            "stochastic_locks": stochastic_locks,
            "hardening": hardening,
            "stochastic_dependence": stochastic,
            "typed_thresholds": {
                "iid_reconstruction_threshold": {
                    "accuracy": "3/4",
                    "maximum_error": "1/10",
                    "first_odd_sample_count": reconstruction_threshold[0],
                    "error": fraction_text(reconstruction_threshold[1]),
                },
                "iid_capability_risk_threshold": {
                    "accuracy": "3/4",
                    "maximum_error": "1/50",
                    "first_odd_sample_count": capability_risk_threshold[0],
                    "error": fraction_text(
                        capability_risk_threshold[1]
                    ),
                },
                "finality_threshold_example": {
                    "N": 10,
                    "f": 3,
                    "minimum_q": minimum_safe_quorum(10, 3),
                    "available_with_f_silent": quorum_available(
                        10, 3, minimum_safe_quorum(10, 3)
                    ),
                },
                "warning": (
                    "sample counts and validator quorums are typed "
                    "resource coordinates, not one universal scalar"
                ),
            },
            "layer_countermodels": layers,
            "full_truth_cube": truth_cube,
            "metastability": metastability,
            "topology": topology,
            "provenance": provenance,
            "threshold_secret_sharing": secret_sharing,
            "quantum_access": {
                "GHZ_phase": quantum,
                "Bell_basis_joint_channel": bell_joint,
            },
        },
        "checks": checks.checks,
        "limits": [
            "Record formation and the physical interface are supplied.",
            "The IID bound does not apply to correlated or adversarial fragments.",
            "Locked-quorum safety does not prove truth, liveness, dissemination, or common knowledge.",
            "The action contract is finite and supplied; it is not a universal theory of capability.",
            "The GHZ control is a 3-of-3 classical phase-bit access structure and local X measurements plus pooling suffice.",
            "The Bell control verifies a direct joint channel; this probe does not prove an LOCC no-go, public finality, or classical emergence.",
            "No finite crossover here establishes a critical exponent, universality class, or thermodynamic phase transition.",
            "No ontology, spacetime, gravity, Standard Model, or cosmological consequence is established.",
        ],
    }


def main() -> None:
    artifact = build_artifact()
    ARTIFACT_PATH.parent.mkdir(parents=True, exist_ok=True)
    rendered = json.dumps(artifact, indent=2, sort_keys=True) + "\n"
    ARTIFACT_PATH.write_text(rendered, encoding="utf-8")
    summary = artifact["summary"]
    print(
        f"{summary['checks_passed']}/{summary['checks_total']} checks passed"
    )
    print(f"artifact: {ARTIFACT_PATH}")


if __name__ == "__main__":
    main()
