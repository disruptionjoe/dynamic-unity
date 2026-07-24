#!/usr/bin/env python3
"""Exact finite probe for the HC-DU-033 record/access quotient.

The probe checks three deliberately narrow statements.

1. Equality constraints imposed by declared symmetries and durable
   post-write evolution generate an equivalence relation ``E_sel``.  The
   quotient ``X/E_sel`` is universal among set-valued maps that obey those
   constraints.
2. If observer ``i`` has indistinguishability relation ``E_i``, pooling a
   coalition intersects its relations.  A fixed-label fact recoverable by
   every authorized coalition is instead constant on the join of the
   coalition relations.
3. A fact that is both selected in sense (1) and robustly accessible in sense
   (2) factors through the join of the selection and accessibility relations.

These are finite set/partition results.  They do not select the physical
symmetry, evolution, access family, readout cut, observer, record codomain, or
interface.  They do not establish common knowledge, Byzantine finality,
irreversibility, quantum objectivity, or record-first ontology.

One wording trap is tested explicitly: the universal quotient is a
set-valued record object.  If a scalar codomain has fewer labels than quotient
classes, there need not be a finest record within that fixed codomain.
"""

from __future__ import annotations

import itertools
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Iterator, Sequence


ARTIFACT_PATH = (
    Path(__file__).resolve().parent
    / "artifacts"
    / "du_record_selection_quotient_result.json"
)

Partition = tuple[int, ...]
StateMap = tuple[int, ...]


def canonical_partition(labels: Sequence[Any]) -> Partition:
    """Return restricted-growth labels for the kernel of ``labels``."""
    relabel: dict[Any, int] = {}
    result: list[int] = []
    for value in labels:
        if value not in relabel:
            relabel[value] = len(relabel)
        result.append(relabel[value])
    return tuple(result)


def partitions(size: int) -> list[Partition]:
    """Enumerate every partition of ``range(size)`` exactly once."""
    if size == 0:
        return [tuple()]

    result: list[Partition] = []

    def extend(prefix: list[int]) -> None:
        if len(prefix) == size:
            result.append(tuple(prefix))
            return
        maximum = max(prefix)
        for label in range(maximum + 2):
            prefix.append(label)
            extend(prefix)
            prefix.pop()

    extend([0])
    return result


def class_count(partition: Partition) -> int:
    return 0 if not partition else max(partition) + 1


def refines(finer: Partition, coarser: Partition) -> bool:
    """Whether every block of ``finer`` is contained in a block of ``coarser``."""
    if len(finer) != len(coarser):
        return False
    seen: dict[int, int] = {}
    for fine_label, coarse_label in zip(finer, coarser, strict=True):
        previous = seen.setdefault(fine_label, coarse_label)
        if previous != coarse_label:
            return False
    return True


def factor_map(finer: Partition, coarser: Partition) -> tuple[int, ...] | None:
    """Return the unique map of quotient labels when ``finer <= coarser``."""
    if not refines(finer, coarser):
        return None
    mapping = [-1] * class_count(finer)
    for fine_label, coarse_label in zip(finer, coarser, strict=True):
        if mapping[fine_label] == -1:
            mapping[fine_label] = coarse_label
        elif mapping[fine_label] != coarse_label:
            raise AssertionError("factor map is inconsistent")
    return tuple(mapping)


def compose_factor(
    quotient: Partition, mapping: Sequence[int]
) -> Partition:
    return canonical_partition(tuple(mapping[label] for label in quotient))


def meet(partitions_: Iterable[Partition]) -> Partition:
    """Meet in the refinement-ordered partition lattice: relation intersection."""
    items = list(partitions_)
    if not items:
        raise ValueError("meet requires at least one partition")
    return canonical_partition(
        tuple(tuple(partition[state] for partition in items) for state in range(len(items[0])))
    )


def partition_from_edges(
    size: int, edges: Iterable[tuple[int, int]]
) -> Partition:
    """Equivalence closure of undirected equality constraints."""
    parent = list(range(size))

    def find(item: int) -> int:
        while parent[item] != item:
            parent[item] = parent[parent[item]]
            item = parent[item]
        return item

    def union(left: int, right: int) -> None:
        left_root = find(left)
        right_root = find(right)
        if left_root == right_root:
            return
        if left_root < right_root:
            parent[right_root] = left_root
        else:
            parent[left_root] = right_root

    for left, right in edges:
        union(left, right)
    return canonical_partition(tuple(find(state) for state in range(size)))


def join(partitions_: Iterable[Partition]) -> Partition:
    """Join in the refinement-ordered partition lattice: equivalence closure."""
    items = list(partitions_)
    if not items:
        raise ValueError("join requires at least one partition")
    size = len(items[0])
    edges: list[tuple[int, int]] = []
    for partition in items:
        if len(partition) != size:
            raise ValueError("partition sizes differ")
        for left in range(size):
            for right in range(left + 1, size):
                if partition[left] == partition[right]:
                    edges.append((left, right))
    return partition_from_edges(size, edges)


def generated_partition(
    size: int, maps: Iterable[StateMap]
) -> Partition:
    return partition_from_edges(
        size,
        (
            (state, state_map[state])
            for state_map in maps
            for state in range(size)
        ),
    )


def canonical_retraction(partition: Partition) -> StateMap:
    representatives: dict[int, int] = {}
    for state, label in enumerate(partition):
        representatives.setdefault(label, state)
    return tuple(representatives[label] for label in partition)


def compose(left: StateMap, right: StateMap) -> StateMap:
    """Return ``left`` after ``right``."""
    return tuple(left[right[state]] for state in range(len(right)))


def all_undirected_edge_sets(
    size: int,
) -> Iterator[tuple[tuple[int, int], ...]]:
    possible = tuple(itertools.combinations(range(size), 2))
    for mask in range(1 << len(possible)):
        yield tuple(
            edge
            for index, edge in enumerate(possible)
            if (mask >> index) & 1
        )


def binary_partition(mask: int, size: int) -> Partition:
    return canonical_partition(tuple((mask >> state) & 1 for state in range(size)))


def copy_map_is_bijection(mask: int, size: int) -> bool:
    outputs = {
        (state, blank ^ ((mask >> state) & 1))
        for state in range(size)
        for blank in (0, 1)
    }
    return len(outputs) == 2 * size


def invariant_binary_masks(
    size: int, group: Iterable[StateMap]
) -> list[int]:
    result: list[int] = []
    for mask in range(1 << size):
        if all(
            all(
                ((mask >> state) & 1)
                == ((mask >> permutation[state]) & 1)
                for state in range(size)
            )
            for permutation in group
        ):
            result.append(mask)
    return result


def all_permutations(size: int) -> tuple[StateMap, ...]:
    return tuple(itertools.permutations(range(size)))


def interface_stabilizer(partition: Partition) -> tuple[StateMap, ...]:
    return tuple(
        permutation
        for permutation in all_permutations(len(partition))
        if all(
            partition[permutation[state]] == partition[state]
            for state in range(len(partition))
        )
    )


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


def exhaustive_quotient_checks(book: CheckBook) -> dict[str, Any]:
    bell_numbers: dict[str, int] = {}
    graph_cases = 0
    graph_partition_comparisons = 0
    quotient_pair_cases = 0
    factorization_positive = 0
    factorization_negative = 0
    self_map_cases = 0
    map_record_cases = 0
    pair_retraction_join_cases = 0

    for size in range(1, 6):
        all_partitions = partitions(size)
        bell_numbers[str(size)] = len(all_partitions)

        for expected in all_partitions:
            retraction = canonical_retraction(expected)
            assert generated_partition(size, (retraction,)) == expected

        all_maps = itertools.product(range(size), repeat=size)
        for state_map_values in all_maps:
            state_map = tuple(state_map_values)
            self_map_cases += 1
            generated = generated_partition(size, (state_map,))
            for record in all_partitions:
                map_record_cases += 1
                invariant = all(
                    record[state_map[state]] == record[state]
                    for state in range(size)
                )
                assert invariant == refines(generated, record)

        for edges in all_undirected_edge_sets(size):
            graph_cases += 1
            generated = partition_from_edges(size, edges)
            assert all(generated[left] == generated[right] for left, right in edges)
            for candidate in all_partitions:
                graph_partition_comparisons += 1
                contains_edges = all(
                    candidate[left] == candidate[right]
                    for left, right in edges
                )
                assert refines(generated, candidate) == contains_edges

        for quotient in all_partitions:
            for record in all_partitions:
                quotient_pair_cases += 1
                mapping = factor_map(quotient, record)
                if refines(quotient, record):
                    factorization_positive += 1
                    assert mapping is not None
                    assert compose_factor(quotient, mapping) == record

                    # Surjectivity of the quotient fixes every value of a
                    # possible factor map, establishing uniqueness.
                    for quotient_label in range(class_count(quotient)):
                        witnesses = [
                            state
                            for state, label in enumerate(quotient)
                            if label == quotient_label
                        ]
                        assert witnesses
                        forced_values = {
                            record[state] for state in witnesses
                        }
                        assert forced_values == {mapping[quotient_label]}
                else:
                    factorization_negative += 1
                    assert mapping is None
                    assert any(
                        quotient[left] == quotient[right]
                        and record[left] != record[right]
                        for left in range(size)
                        for right in range(size)
                    )

                retraction_quotient = canonical_retraction(quotient)
                retraction_record = canonical_retraction(record)
                generated_pair = generated_partition(
                    size, (retraction_quotient, retraction_record)
                )
                assert generated_pair == join((quotient, record))
                pair_retraction_join_cases += 1

    book.add(
        "all equality-constraint graphs through five states generate the least containing equivalence",
        True,
        {
            "graph_cases": graph_cases,
            "graph_partition_comparisons": graph_partition_comparisons,
        },
    )
    book.add(
        "every admissible finite record factors uniquely through its generated quotient",
        True,
        {
            "partition_pair_cases": quotient_pair_cases,
            "positive": factorization_positive,
            "negative": factorization_negative,
        },
    )
    book.add(
        "all self-maps through five states obey the generated-equivalence invariance criterion",
        True,
        {
            "self_maps": self_map_cases,
            "map_record_partition_cases": map_record_cases,
            "canonical_retraction_join_cases": pair_retraction_join_cases,
        },
    )
    return {
        "bell_numbers": bell_numbers,
        "graph_cases": graph_cases,
        "graph_partition_comparisons": graph_partition_comparisons,
        "quotient_record_pair_cases": quotient_pair_cases,
        "factorization_positive_cases": factorization_positive,
        "factorization_negative_cases": factorization_negative,
        "self_map_cases": self_map_cases,
        "map_record_partition_cases": map_record_cases,
        "canonical_retraction_join_cases": pair_retraction_join_cases,
    }


def exhaustive_lattice_checks(book: CheckBook) -> dict[str, Any]:
    pair_cases = 0
    comparison_cases = 0
    product_kernel_cases = 0
    combined_record_access_cases = 0
    triple_cases = 0

    for size in range(1, 6):
        all_partitions = partitions(size)
        for left in all_partitions:
            for right in all_partitions:
                pair_cases += 1
                pooled = meet((left, right))
                public = join((left, right))
                assert refines(pooled, left)
                assert refines(pooled, right)
                assert refines(left, public)
                assert refines(right, public)

                product_kernel = canonical_partition(
                    tuple(
                        (left[state], right[state])
                        for state in range(size)
                    )
                )
                assert product_kernel == pooled
                product_kernel_cases += 1

                for candidate in all_partitions:
                    comparison_cases += 1

                    is_lower_bound = refines(candidate, left) and refines(
                        candidate, right
                    )
                    if is_lower_bound:
                        assert refines(candidate, pooled)

                    is_upper_bound = refines(left, candidate) and refines(
                        right, candidate
                    )
                    if is_upper_bound:
                        assert refines(public, candidate)

                    # A fact is recoverable from both access quotients exactly
                    # when both kernels refine the fact's kernel.  The join is
                    # the universal finest such common deterministic fact.
                    robust_from_both = is_upper_bound
                    factors_through_public = refines(public, candidate)
                    assert robust_from_both == factors_through_public

                    # The same join statement combines record-selection and
                    # robust-access constraints.
                    jointly_admissible = refines(left, candidate) and refines(
                        right, candidate
                    )
                    assert jointly_admissible == factors_through_public
                    combined_record_access_cases += 1

        for first in all_partitions:
            for second in all_partitions:
                for third in all_partitions:
                    triple_cases += 1
                    assert meet((meet((first, second)), third)) == meet(
                        (first, meet((second, third)))
                    )
                    assert join((join((first, second)), third)) == join(
                        (first, join((second, third)))
                    )

    book.add(
        "pooled observations use partition meet and robust common facts use partition join",
        True,
        {
            "partition_pair_cases": pair_cases,
            "lattice_comparisons": comparison_cases,
            "product_kernel_cases": product_kernel_cases,
        },
    )
    book.add(
        "selection and robust-access constraints combine by equivalence join",
        True,
        {"fact_comparisons": combined_record_access_cases},
    )
    book.add(
        "partition meet and join are associative through five states",
        True,
        {"ordered_partition_triples": triple_cases},
    )
    return {
        "partition_pair_cases": pair_cases,
        "lattice_comparisons": comparison_cases,
        "product_kernel_cases": product_kernel_cases,
        "combined_record_access_fact_comparisons": combined_record_access_cases,
        "ordered_partition_triples": triple_cases,
    }


def selection_fixtures(book: CheckBook) -> dict[str, Any]:
    size = 4
    identity = tuple(range(size))
    full_group = all_permutations(size)
    full_selection = generated_partition(size, (*full_group, identity))

    first_bit = (0, 0, 1, 1)
    stabilizer = interface_stabilizer(first_bit)
    interface_selection = generated_partition(size, (*stabilizer, identity))

    fixed_plus_three_cycle = (0, 2, 3, 1)
    asymmetric_selection = generated_partition(
        size, (fixed_plus_three_cycle,)
    )

    partial_merge = (0, 0, 2, 2)
    merged_selection = generated_partition(size, (partial_merge,))
    total_collapse = (0, 0, 0, 0)
    collapsed_selection = generated_partition(size, (total_collapse,))

    all_copyable = all(
        copy_map_is_bijection(mask, size) for mask in range(1 << size)
    )
    invariant_masks = invariant_binary_masks(size, full_group)

    identity_channel = tuple(range(size))
    equivariant_identity = all(
        identity_channel[permutation[state]]
        == permutation[identity_channel[state]]
        for permutation in full_group
        for state in range(size)
    )

    book.add(
        "full transitive symmetry leaves only a constant universal scalar quotient",
        class_count(full_selection) == 1 and invariant_masks == [0, 15],
        {
            "quotient": list(full_selection),
            "invariant_binary_masks": invariant_masks,
        },
    )
    book.add(
        "declared first-bit interface produces exactly its two-block quotient",
        interface_selection == first_bit,
        {
            "stabilizer_order": len(stabilizer),
            "quotient": list(interface_selection),
        },
    )
    book.add(
        "asymmetric fixed-point plus three-cycle dynamics selects two durable classes",
        asymmetric_selection == (0, 1, 1, 1),
        {"quotient": list(asymmetric_selection)},
    )
    book.add(
        "permitted post-write evolution can merge or collapse record distinctions",
        merged_selection == (0, 0, 1, 1)
        and class_count(collapsed_selection) == 1,
        {
            "partial_merge": list(merged_selection),
            "total_collapse": list(collapsed_selection),
        },
    )
    book.add(
        "predicate-specific classical copyability does not select among predicates",
        all_copyable and len(invariant_masks) == 2,
        {
            "copyable_binary_predicates": 1 << size,
            "full_symmetry_invariant_binary_predicates": len(invariant_masks),
        },
    )
    book.add(
        "an equivariant identity channel retains all states while invariant scalars are constant",
        equivariant_identity
        and class_count(canonical_partition(range(size))) == size
        and len(invariant_masks) == 2,
        {
            "equivariant_channel_classes": size,
            "invariant_scalar_classes": class_count(full_selection),
        },
    )

    return {
        "state_count": size,
        "full_symmetry": {
            "group_order": len(full_group),
            "selection_quotient": list(full_selection),
            "class_count": class_count(full_selection),
        },
        "declared_first_bit_interface": {
            "interface_partition": list(first_bit),
            "stabilizer_order": len(stabilizer),
            "selection_quotient": list(interface_selection),
            "class_count": class_count(interface_selection),
        },
        "asymmetric_dynamics": {
            "map": list(fixed_plus_three_cycle),
            "selection_quotient": list(asymmetric_selection),
            "class_count": class_count(asymmetric_selection),
        },
        "durability_maps": {
            "partial_merge_map": list(partial_merge),
            "partial_merge_quotient": list(merged_selection),
            "total_collapse_map": list(total_collapse),
            "total_collapse_quotient": list(collapsed_selection),
        },
        "copyability_null": {
            "binary_predicate_count": 1 << size,
            "all_predicate_specific_copy_maps_bijective": all_copyable,
            "full_symmetry_invariant_binary_masks": invariant_masks,
        },
        "equivariant_non_scalar_control": {
            "channel": "identity X -> X with transported codomain action",
            "equivariance_holds_for_all_permutations": equivariant_identity,
            "retained_class_count": size,
            "invariant_scalar_class_count": class_count(full_selection),
        },
    }


def access_fixtures(book: CheckBook) -> dict[str, Any]:
    states = ["00", "01", "10", "11"]
    observer_a = (0, 0, 1, 1)
    observer_b = (0, 1, 0, 1)
    observer_c = (0, 1, 1, 0)

    pooled_ab = meet((observer_a, observer_b))
    singleton_robust = join((observer_a, observer_b))

    redundant_pool = meet((observer_a, observer_a))
    redundant_robust = join((observer_a, observer_a))

    common_core_a = (0, 0, 1, 2)
    common_core_b = (0, 1, 1, 2)
    common_core_pool = meet((common_core_a, common_core_b))
    common_core_robust = join((common_core_a, common_core_b))

    pair_ab = meet((observer_a, observer_b))
    pair_ac = meet((observer_a, observer_c))
    pair_bc = meet((observer_b, observer_c))
    threshold_public = join((pair_ab, pair_ac, pair_bc))

    book.add(
        "complementary bits separate pooled evidence from singleton-robust public fact",
        class_count(pooled_ab) == 4
        and class_count(singleton_robust) == 1,
        {
            "pooled": list(pooled_ab),
            "robust_across_singletons": list(singleton_robust),
        },
    )
    book.add(
        "redundant copies make pooled and robust quotients coincide",
        redundant_pool == observer_a
        and redundant_robust == observer_a,
        {
            "pooled": list(redundant_pool),
            "robust": list(redundant_robust),
        },
    )
    book.add(
        "two complementary views can retain a nontrivial common deterministic core",
        class_count(common_core_pool) == 4
        and common_core_robust == (0, 0, 0, 1),
        {
            "pooled": list(common_core_pool),
            "robust": list(common_core_robust),
        },
    )
    book.add(
        "two-of-three complementary access gives every authorized pair the full fact",
        all(
            class_count(partition) == 4
            for partition in (pair_ab, pair_ac, pair_bc)
        )
        and class_count(threshold_public) == 4,
        {
            "authorized_pair_relations": [
                list(pair_ab),
                list(pair_ac),
                list(pair_bc),
            ],
            "robust_public": list(threshold_public),
        },
    )

    return {
        "state_encoding": states,
        "complementary_bits": {
            "observer_a": list(observer_a),
            "observer_b": list(observer_b),
            "pooled_coalition_meet": list(pooled_ab),
            "pooled_class_count": class_count(pooled_ab),
            "authorized_singletons_join": list(singleton_robust),
            "robust_public_class_count": class_count(singleton_robust),
        },
        "redundant_copies": {
            "observer_a": list(observer_a),
            "observer_b": list(observer_a),
            "pooled_coalition_meet": list(redundant_pool),
            "authorized_singletons_join": list(redundant_robust),
            "class_count": class_count(redundant_robust),
        },
        "common_core_plus_complements": {
            "observer_a": list(common_core_a),
            "observer_b": list(common_core_b),
            "pooled_coalition_meet": list(common_core_pool),
            "robust_common_join": list(common_core_robust),
            "robust_common_class_count": class_count(common_core_robust),
        },
        "two_of_three_access": {
            "observer_a": list(observer_a),
            "observer_b": list(observer_b),
            "observer_c": list(observer_c),
            "authorized_coalitions": [["A", "B"], ["A", "C"], ["B", "C"]],
            "coalition_meets": [
                list(pair_ab),
                list(pair_ac),
                list(pair_bc),
            ],
            "robust_public_join": list(threshold_public),
            "class_count": class_count(threshold_public),
        },
    }


def hardening_order_fixture(book: CheckBook) -> dict[str, Any]:
    """Show that local scalar hardening and later pooling need not commute."""
    selection = (0, 0, 1)
    observer_one = (0, 1, 0)
    observer_two = (0, 1, 1)

    raw_pool = meet((observer_one, observer_two))
    harden_after_pool = join((selection, raw_pool))

    locally_hardened_one = join((selection, observer_one))
    locally_hardened_two = join((selection, observer_two))
    pool_after_local_hardening = meet(
        (locally_hardened_one, locally_hardened_two)
    )

    strict = refines(harden_after_pool, pool_after_local_hardening) and not refines(
        pool_after_local_hardening, harden_after_pool
    )
    book.add(
        "pooling raw fragments and local scalar hardening do not commute",
        class_count(harden_after_pool) == 2
        and class_count(pool_after_local_hardening) == 1
        and strict,
        {
            "harden_after_raw_pool": list(harden_after_pool),
            "pool_after_local_hardening": list(pool_after_local_hardening),
        },
    )

    return {
        "state_count": 3,
        "selection_relation": list(selection),
        "observer_one_relation": list(observer_one),
        "observer_two_relation": list(observer_two),
        "raw_pool_relation": list(raw_pool),
        "harden_after_raw_pool": list(harden_after_pool),
        "locally_hardened_relations": [
            list(locally_hardened_one),
            list(locally_hardened_two),
        ],
        "pool_after_local_hardening": list(pool_after_local_hardening),
        "strict_nondistributive_inclusion": strict,
        "interpretation": (
            "Complementary raw fragments can jointly support an invariant "
            "fact that is destroyed when each fragment is forced through a "
            "fixed-label invariant scalar before pooling."
        ),
        "scope": (
            "standard nondistributivity of the three-state partition lattice; "
            "not a consensus, quantum, or physical finality theorem"
        ),
    }


def boundary_countermodels(book: CheckBook) -> dict[str, Any]:
    """Finite controls that prevent the Set theorem from absorbing physics."""
    identity_two = (0, 1)
    flip = (1, 0)
    one_step = generated_partition(2, (flip,))
    two_step = generated_partition(2, (compose(flip, flip),))

    selected_full = (0, 1, 2, 3)
    observer_first_bit = (0, 0, 1, 1)
    accessible_selected = join((selected_full, observer_first_bit))

    # An orbit relation under simultaneous automorphisms need not be a
    # congruence for a binary operation because representatives can be chosen
    # independently in the quotient product.
    swap_zero_one = (1, 0, 2)
    operation = (
        (0, 2, 2),
        (2, 1, 2),
        (2, 2, 2),
    )
    automorphism_holds = all(
        swap_zero_one[operation[left][right]]
        == operation[swap_zero_one[left]][swap_zero_one[right]]
        for left in range(3)
        for right in range(3)
    )
    orbit_partition = generated_partition(3, (swap_zero_one,))
    quotient_outputs: dict[tuple[int, int], set[int]] = {}
    for left in range(3):
        for right in range(3):
            key = (orbit_partition[left], orbit_partition[right])
            quotient_outputs.setdefault(key, set()).add(
                orbit_partition[operation[left][right]]
            )
    ill_defined_cells = {
        str(key): sorted(outputs)
        for key, outputs in quotient_outputs.items()
        if len(outputs) > 1
    }

    # Abstractly intersecting observation kernels assumes the tuple of
    # readouts is physically available.  Here each first read destroys the
    # other bit, so neither allowed order realizes the four-valued product.
    states = ((0, 0), (0, 1), (1, 0), (1, 1))
    first_bit_partition = (0, 0, 1, 1)
    second_bit_partition = (0, 1, 0, 1)
    abstract_pool = meet((first_bit_partition, second_bit_partition))
    first_then_second_outputs = tuple((first, 0) for first, _ in states)
    second_then_first_outputs = tuple((second, 0) for _, second in states)
    first_then_second_kernel = canonical_partition(first_then_second_outputs)
    second_then_first_kernel = canonical_partition(second_then_first_outputs)

    # Bell-phase histories have identical one-fragment marginals but are
    # orthogonal under a collective measurement.  Use unnormalised integer
    # amplitudes; normalization does not affect equality or orthogonality.
    bell_plus = (1, 0, 0, 1)
    bell_minus = (1, 0, 0, -1)
    bell_inner_product = sum(
        left * right for left, right in zip(bell_plus, bell_minus, strict=True)
    )
    single_qubit_marginal_signature = ((1, 0), (0, 1))

    # Two size-two quorums among three nodes can intersect only at the faulty
    # node, which equivocates to produce conflicting certificates.
    quorum_zero = frozenset({"honest_a", "byzantine"})
    quorum_one = frozenset({"honest_b", "byzantine"})
    honest_intersection = (
        quorum_zero & quorum_one
    ) - {"byzantine"}

    held_out_map = (1, 2, 0, 4, 3)
    held_out_quotient = generated_partition(5, (held_out_map,))

    book.add(
        "record quotient depends on the declared preservation cadence",
        class_count(one_step) == 1
        and two_step == identity_two,
        {
            "one_step": list(one_step),
            "two_step": list(two_step),
        },
    )
    book.add(
        "the selected quotient can retain facts unavailable to the observer",
        selected_full != accessible_selected
        and accessible_selected == observer_first_bit,
        {
            "selected": list(selected_full),
            "accessible_selected": list(accessible_selected),
        },
    )
    book.add(
        "a Set orbit quotient need not preserve binary process composition",
        automorphism_holds and bool(ill_defined_cells),
        {
            "orbit_partition": list(orbit_partition),
            "ill_defined_quotient_cells": ill_defined_cells,
        },
    )
    book.add(
        "kernel intersection can overstate pooling when readouts disturb one specimen",
        class_count(abstract_pool) == 4
        and class_count(first_then_second_kernel) == 2
        and class_count(second_then_first_kernel) == 2,
        {
            "abstract_pool": list(abstract_pool),
            "first_then_second": list(first_then_second_kernel),
            "second_then_first": list(second_then_first_kernel),
        },
    )
    book.add(
        "local quantum marginals need not determine collective distinguishability",
        bell_inner_product == 0,
        {
            "both_single_fragment_marginals": [
                list(row) for row in single_qubit_marginal_signature
            ],
            "joint_inner_product": bell_inner_product,
        },
    )
    book.add(
        "common deterministic readability does not imply Byzantine quorum finality",
        not honest_intersection,
        {
            "certificate_zero": sorted(quorum_zero),
            "certificate_one": sorted(quorum_one),
            "honest_intersection": sorted(honest_intersection),
        },
    )
    book.add(
        "held-out five-state generator produces the declared two-class quotient",
        held_out_quotient == (0, 0, 0, 1, 1),
        {"quotient": list(held_out_quotient)},
    )

    return {
        "readout_cadence": {
            "physical_flip": list(flip),
            "one_step_preservation_quotient": list(one_step),
            "two_step_preservation_map": list(compose(flip, flip)),
            "two_step_preservation_quotient": list(two_step),
        },
        "accessibility_gap": {
            "selected_quotient": list(selected_full),
            "observer_relation": list(observer_first_bit),
            "combined_selected_accessible_quotient": list(accessible_selected),
        },
        "process_congruence_failure": {
            "automorphism": list(swap_zero_one),
            "automorphism_holds": automorphism_holds,
            "orbit_partition": list(orbit_partition),
            "ill_defined_quotient_cells": ill_defined_cells,
        },
        "destructive_pooling": {
            "abstract_kernel_intersection": list(abstract_pool),
            "first_then_second_kernel": list(first_then_second_kernel),
            "second_then_first_kernel": list(second_then_first_kernel),
            "tuple_readout_physically_available": False,
        },
        "correlated_quantum_access": {
            "histories": ["Phi_plus", "Phi_minus"],
            "single_fragment_marginals_equal": True,
            "single_fragment_marginal_signature": [
                list(row) for row in single_qubit_marginal_signature
            ],
            "joint_states_orthogonal": bell_inner_product == 0,
            "consequence": (
                "For correlated or quantum fragments, specify the coalition "
                "channel directly rather than intersecting marginal kernels."
            ),
        },
        "byzantine_split_view": {
            "node_count": 3,
            "quorum_size": 2,
            "fault_count": 1,
            "certificate_zero": sorted(quorum_zero),
            "certificate_one": sorted(quorum_one),
            "honest_intersection": sorted(honest_intersection),
            "conflicting_certificates_possible": not honest_intersection,
        },
        "held_out_five_state_case": {
            "generator": list(held_out_map),
            "quotient": list(held_out_quotient),
        },
    }


def fixed_codomain_counterexample(book: CheckBook) -> dict[str, Any]:
    size = 3
    universal_quotient = (0, 1, 2)
    binary_records = {
        binary_partition(mask, size) for mask in range(1 << size)
    }
    nonconstant_binary_records = {
        partition
        for partition in binary_records
        if class_count(partition) == 2
    }
    finest_binary_candidates = [
        candidate
        for candidate in nonconstant_binary_records
        if all(
            refines(candidate, record)
            for record in nonconstant_binary_records
        )
    ]

    three_label_injection = universal_quotient
    three_label_is_universal = all(
        refines(three_label_injection, record) for record in binary_records
    )

    book.add(
        "a fixed two-label codomain need not contain a finest record for a three-class quotient",
        not finest_binary_candidates and three_label_is_universal,
        {
            "universal_class_count": 3,
            "distinct_nonconstant_binary_partitions": len(
                nonconstant_binary_records
            ),
            "finest_binary_candidates": [
                list(candidate) for candidate in finest_binary_candidates
            ],
        },
    )

    return {
        "state_count": size,
        "universal_quotient": list(universal_quotient),
        "universal_class_count": class_count(universal_quotient),
        "fixed_binary_codomain": {
            "distinct_nonconstant_record_partitions": len(
                nonconstant_binary_records
            ),
            "finest_record_exists": bool(finest_binary_candidates),
        },
        "three_label_codomain": {
            "injective_quotient_available": True,
            "factors_all_binary_records": three_label_is_universal,
        },
        "correction": (
            "The universal object is X/E. A finest record inside a fixed "
            "codomain Y is guaranteed only when Y can label every quotient "
            "class; uniqueness is then only up to relabeling."
        ),
    }


def build_result() -> dict[str, Any]:
    book = CheckBook(checks=[])
    quotient = exhaustive_quotient_checks(book)
    lattice = exhaustive_lattice_checks(book)
    selection = selection_fixtures(book)
    access = access_fixtures(book)
    hardening_order = hardening_order_fixture(book)
    boundary = boundary_countermodels(book)
    codomain = fixed_codomain_counterexample(book)

    all_passed = book.passed == len(book.checks)
    return {
        "schema_version": "1.0",
        "run_id": "RUN-20260724-162458-hc-du-033-record-selection",
        "hardening_id": "HC-DU-033",
        "method": (
            "exact exhaustive finite partition/equivalence enumeration using "
            "only the Python standard library"
        ),
        "scope": {
            "state_sizes": [1, 2, 3, 4, 5],
            "record_type": (
                "set-valued universal quotient and its fixed-label scalar "
                "postprocessings"
            ),
            "access_type": (
                "deterministic zero-error observer/coalition "
                "indistinguishability equivalences"
            ),
            "not_established": [
                "physical selection of symmetry, dynamics, readout cut, interface, access family, or observer",
                "equivalence for noisy, probabilistic, nonorthogonal, or adversarial access",
                "common knowledge or Byzantine public finality",
                "irreversible classicality or a physical record ontology",
                "continuum, relativistic, gravitational, cosmological, or Dynamic Unity identification",
            ],
        },
        "theorems": {
            "selection_coequalizer": {
                "statement": (
                    "The quotient by the least equivalence generated by "
                    "x~g(x) and x~k(x) is universal among maps invariant "
                    "under every declared g and durable under every declared k."
                ),
                "nontrivial_iff": "the generated equality graph has more than one connected component",
                "grade": "EXACT FINITE SET THEOREM / STANDARD COEQUALIZER SPECIALIZATION",
            },
            "access_meet_join": {
                "statement": (
                    "Pooling a coalition intersects observer kernels; the "
                    "finest fixed-label fact recoverable by every authorized "
                    "coalition is the quotient by the join of coalition meets."
                ),
                "grade": "EXACT FINITE PARTITION-LATTICE / COMMON-PART SPECIALIZATION",
            },
            "record_access_factorization": {
                "statement": (
                    "The finest fact satisfying both selection constraints "
                    "and every authorized coalition's recoverability "
                    "constraints is the quotient by the join of the selection "
                    "and robust-access equivalences."
                ),
                "grade": "EXACT FINITE SYNTHESIS / CLAIM-SPECIFIC NOVELTY SEARCH-INCOMPLETE",
            },
        },
        "exhaustive_quotient_enumeration": quotient,
        "exhaustive_access_lattice_enumeration": lattice,
        "selection_fixtures": selection,
        "access_fixtures": access,
        "hardening_order_fixture": hardening_order,
        "boundary_countermodels": boundary,
        "fixed_codomain_counterexample": codomain,
        "checks": book.checks,
        "check_summary": {
            "passed": book.passed,
            "total": len(book.checks),
            "all_passed": all_passed,
        },
        "terminal_disposition": (
            "FINITE_RECORD_ACCESS_QUOTIENT_EXACT / "
            "SCALAR_CODOMAIN_CAVEAT_EXPOSED / "
            "PHYSICAL_INTERFACE_AND_PUBLIC_FINALITY_OPEN"
        ),
        "banked": False,
        "seeded": False,
    }


def main() -> None:
    result = build_result()
    ARTIFACT_PATH.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT_PATH.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        f"{result['check_summary']['passed']}/"
        f"{result['check_summary']['total']} checks passed"
    )
    print(result["terminal_disposition"])
    print(ARTIFACT_PATH)
    if not result["check_summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
