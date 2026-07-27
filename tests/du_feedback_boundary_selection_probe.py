#!/usr/bin/env python3
"""Exact controls for HC-DU-056 / N5-PF-P3.

This is a regression for a directly proved finite selector theorem, not a
simulation.  It asks whether a physical antecedent selects a complete feedback
boundary up to every response available to a frozen future action/tester
family.

The two fixtures are unchanged shadows of existing Dynamic Unity specimens:

1. the material Z3 gauge-boundary formation orbit from HC-DU-040D; and
2. the closed metastable host with archive/reset relocation from
   HC-DU-043..046/054.

All comparisons are exact.  No sampling, numerical tolerance, provider, or
external hardware is used.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import json
from typing import Callable, Hashable, Iterable, Mapping, Sequence


Q = Fraction
CHECKS: list[dict[str, object]] = []


def record(name: str, passed: bool, detail: object) -> None:
    CHECKS.append({"name": name, "passed": bool(passed), "detail": detail})


def factors_through(
    domain: Iterable[Hashable],
    antecedent: Callable[[Hashable], Hashable],
    response: Callable[[Hashable], Hashable],
) -> bool:
    """Finite form of ker(antecedent) subseteq ker(response)."""

    seen: dict[Hashable, Hashable] = {}
    for implementation in domain:
        key = antecedent(implementation)
        value = response(implementation)
        if key in seen and seen[key] != value:
            return False
        seen[key] = value
    return True


def response_signature(
    implementation: Hashable,
    action_family: Sequence[str],
    responses: Mapping[str, Callable[[Hashable], Hashable]],
) -> tuple[Hashable, ...]:
    return tuple(responses[action](implementation) for action in action_family)


def partition(
    domain: Iterable[Hashable],
    classifier: Callable[[Hashable], Hashable],
) -> frozenset[frozenset[Hashable]]:
    cells: dict[Hashable, set[Hashable]] = {}
    for item in domain:
        cells.setdefault(classifier(item), set()).add(item)
    return frozenset(frozenset(cell) for cell in cells.values())


def refines(
    finer: frozenset[frozenset[Hashable]],
    coarser: frozenset[frozenset[Hashable]],
) -> bool:
    return all(any(cell <= large for large in coarser) for cell in finer)


@dataclass(frozen=True)
class GaugeBoundary:
    orientation: int
    path: int
    invisible_dilation: str


@dataclass(frozen=True)
class HostBoundary:
    archive_route: str
    reset_lineage: str
    invisible_microtag: str


def evaluate_causal_events(order: Sequence[str]) -> dict[str, object]:
    state: dict[str, object] = {}
    for event in order:
        if event == "source":
            state["source"] = 1
        elif event == "orientation":
            state["orientation"] = 1
        elif event == "reset":
            state["reset"] = "clean"
        elif event == "control":
            if (
                state.get("source") != 1
                or state.get("orientation") != 1
                or state.get("reset") != "clean"
            ):
                raise ValueError("control executed before a causal parent")
            state["boundary"] = ("plus", "path_0", "clean")
        elif event == "response":
            if "boundary" not in state:
                raise ValueError("response executed before control")
            state["response"] = "stable"
        else:
            raise ValueError(f"unknown event {event}")
    return state


def main() -> int:
    # General finite selector theorem and uniqueness on the antecedent image.
    theorem_domain = (
        ("a0", "b0", "r0"),
        ("a0", "b1", "r0"),
        ("a1", "b2", "r1"),
    )
    record(
        "response_class_selector_exists_exactly_on_antecedent_fibres",
        factors_through(
            theorem_domain,
            lambda item: item[0],
            lambda item: item[2],
        ),
        "same antecedent always has the same response class",
    )
    record(
        "raw_boundary_identity_is_not_required",
        not factors_through(
            theorem_domain,
            lambda item: item[0],
            lambda item: item[1],
        ),
        "a0 contains b0 and b1 but both lie in response class r0",
    )
    selector = {
        antecedent: response
        for antecedent, _boundary, response in theorem_domain
    }
    record(
        "induced_selector_is_unique_on_the_antecedent_image",
        selector == {"a0": "r0", "a1": "r1"},
        selector,
    )

    # Material Z3 gauge-boundary formation orbit.
    gauge_domain = tuple(
        GaugeBoundary(orientation, path, microtag)
        for orientation in (1, -1)
        for path in (0, 1)
        for microtag in ("dilation_a", "dilation_b")
    )
    gauge_responses: dict[str, Callable[[Hashable], Hashable]] = {
        # The selected write orbit is source-QND in either orientation.
        "source_only": lambda item: (0, 1, 2),
        # One frozen pointer/controller convention reads f -> +/- f mod 3.
        "fixed_pointer": lambda item: tuple(
            (item.orientation * flux) % 3  # type: ignore[attr-defined]
            for flux in (0, 1, 2)
        ),
        # HC-DU-040D proves endpoint-identical Hamiltonian paths admit an
        # intermediate-time detector assay.  The path bit records that exact
        # witness; the invisible dilation is outside the admitted tester.
        "intermediate_path": lambda item: item.path,  # type: ignore[attr-defined]
    }
    gauge_a0 = ("source_only",)
    gauge_a1 = ("source_only", "fixed_pointer")
    gauge_a2 = ("source_only", "fixed_pointer", "intermediate_path")

    gauge_sig = lambda family: (
        lambda item: response_signature(item, family, gauge_responses)
    )
    gauge_p0 = partition(gauge_domain, gauge_sig(gauge_a0))
    gauge_p1 = partition(gauge_domain, gauge_sig(gauge_a1))
    gauge_p2 = partition(gauge_domain, gauge_sig(gauge_a2))

    record(
        "gauge_law_selects_source_only_response_orbit",
        factors_through(gauge_domain, lambda _item: "gauge_qnd_orbit", gauge_sig(gauge_a0)),
        "controlled add and subtract both preserve the source sectors",
    )
    record(
        "fixed_pointer_capability_reopens_orientation_orbit",
        not factors_through(
            gauge_domain,
            lambda _item: "gauge_qnd_orbit",
            gauge_sig(gauge_a1),
        ),
        "f=1 is read as pointer 1 under + and pointer 2 under -",
    )
    record(
        "material_orientation_selects_endpoint_response_class",
        factors_through(
            gauge_domain,
            lambda item: item.orientation,
            gauge_sig(gauge_a1),
        ),
        "orientation is a sufficient supplied premise for final pointer control",
    )
    record(
        "intermediate_tester_reopens_endpoint_identical_paths",
        not factors_through(
            gauge_domain,
            lambda item: item.orientation,
            gauge_sig(gauge_a2),
        ),
        "same oriented endpoint instrument; different formation path",
    )
    record(
        "orientation_and_path_select_full_admitted_response_class",
        factors_through(
            gauge_domain,
            lambda item: (item.orientation, item.path),
            gauge_sig(gauge_a2),
        ),
        "microscopic dilation tags remain unselected but response-equivalent",
    )
    record(
        "gauge_raw_implementation_remains_plural",
        not factors_through(
            gauge_domain,
            lambda item: (item.orientation, item.path),
            lambda item: item,
        ),
        "response selection is strictly weaker than microscopic identity",
    )
    record(
        "gauge_capability_partitions_refine_monotonically",
        (
            refines(gauge_p2, gauge_p1)
            and refines(gauge_p1, gauge_p0)
            and tuple(map(len, (gauge_p0, gauge_p1, gauge_p2))) == (1, 2, 4)
        ),
        {
            "source_only_classes": len(gauge_p0),
            "plus_pointer_classes": len(gauge_p1),
            "plus_midpath_classes": len(gauge_p2),
        },
    )

    # Closed metastable host with route/access and reset-lineage relocation.
    host_domain = tuple(
        HostBoundary(route, reset, microtag)
        for route in ("visible", "hidden")
        for reset in ("clean", "retained")
        for microtag in ("micro_a", "micro_b")
    )
    host_responses: dict[str, Callable[[Hashable], Hashable]] = {
        "endpoint_next_law": lambda _item: (Q(3, 4), Q(1, 4)),
        "occurrence_query": lambda item: (
            "WRITE" if item.archive_route == "visible" else "UNAVAILABLE"  # type: ignore[attr-defined]
        ),
        "next_cycle_memory_probe": lambda item: (
            0 if item.reset_lineage == "clean" else 1  # type: ignore[attr-defined]
        ),
    }
    host_a0 = ("endpoint_next_law",)
    host_a1 = ("endpoint_next_law", "occurrence_query")
    host_a2 = (
        "endpoint_next_law",
        "occurrence_query",
        "next_cycle_memory_probe",
    )
    host_sig = lambda family: (
        lambda item: response_signature(item, family, host_responses)
    )
    host_p0 = partition(host_domain, host_sig(host_a0))
    host_p1 = partition(host_domain, host_sig(host_a1))
    host_p2 = partition(host_domain, host_sig(host_a2))

    record(
        "host_antecedent_selects_reduced_endpoint_response_class",
        factors_through(
            host_domain,
            lambda _item: "same_host_endpoint_and_reset_command",
            host_sig(host_a0),
        ),
        "archive route and retained reset memory do not alter the frozen reduced endpoint law",
    )
    record(
        "occurrence_capability_exposes_archive_route_relocation",
        not factors_through(
            host_domain,
            lambda _item: "same_host_endpoint_and_reset_command",
            host_sig(host_a1),
        ),
        "visible archive returns WRITE; hidden route returns UNAVAILABLE",
    )
    record(
        "route_premise_selects_occurrence_response_only",
        factors_through(
            host_domain,
            lambda item: item.archive_route,
            host_sig(host_a1),
        ),
        "declared route closes the occurrence query but not reset lineage",
    )
    record(
        "next_cycle_tester_exposes_incomplete_reset",
        not factors_through(
            host_domain,
            lambda item: item.archive_route,
            host_sig(host_a2),
        ),
        "same reset command and route; future-readable retained memory changes response",
    )
    record(
        "route_and_reset_lineage_select_full_host_response_class",
        factors_through(
            host_domain,
            lambda item: (item.archive_route, item.reset_lineage),
            host_sig(host_a2),
        ),
        "future-invisible microtags remain unselected",
    )
    record(
        "semantic_reset_certificate_does_not_select_physical_reset",
        not factors_through(
            host_domain,
            lambda _item: ("same_host", "RESET_CERTIFIED"),
            host_sig(host_a2),
        ),
        "certificate is identical across clean and retained memory realizations",
    )
    record(
        "complete_future_readable_memory_is_the_minimum_reset_repair",
        (
            factors_through(
                host_domain,
                lambda item: (item.archive_route, item.reset_lineage),
                host_sig(host_a2),
            )
            and not factors_through(
                host_domain,
                lambda item: item.archive_route,
                host_sig(host_a2),
            )
        ),
        "reset need not identify invisible microstructure; it must fix every future-readable memory class",
    )
    record(
        "host_capability_partitions_refine_monotonically",
        (
            refines(host_p2, host_p1)
            and refines(host_p1, host_p0)
            and tuple(map(len, (host_p0, host_p1, host_p2))) == (1, 2, 4)
        ),
        {
            "endpoint_classes": len(host_p0),
            "plus_occurrence_classes": len(host_p1),
            "plus_reset_memory_classes": len(host_p2),
        },
    )

    # The response signature is always the formal coarsest exact repair, but
    # using it as a premise is tester-coded rather than physical selection.
    record(
        "response_signature_is_a_formal_but_action_coded_repair",
        factors_through(gauge_domain, gauge_sig(gauge_a2), gauge_sig(gauge_a2))
        and factors_through(host_domain, host_sig(host_a2), host_sig(host_a2)),
        "identity factorization is a positive control, not an independently selected antecedent",
    )

    # Matched preferred-leaf / causal-partial-order control.
    preferred_order = (
        "source",
        "orientation",
        "reset",
        "control",
        "response",
    )
    alternate_linear_extension = (
        "reset",
        "orientation",
        "source",
        "control",
        "response",
    )
    preferred_result = evaluate_causal_events(preferred_order)
    partial_order_result = evaluate_causal_events(alternate_linear_extension)
    record(
        "matched_linear_extensions_preserve_boundary_and_response",
        preferred_order != alternate_linear_extension
        and preferred_result == partial_order_result,
        preferred_result,
    )
    record(
        "forgetting_privileged_simultaneity_preserves_selector_verdicts",
        (
            preferred_result["boundary"] == partial_order_result["boundary"]
            and preferred_result["response"] == partial_order_result["response"]
        ),
        "only causal parents, not leaf ranks, enter the boundary response",
    )

    passed = sum(1 for check in CHECKS if check["passed"])
    result = {
        "probe": "du_feedback_boundary_selection_probe",
        "claim_id": "HC-DU-056",
        "work_id": "N5-PF-P3",
        "checks": CHECKS,
        "checks_passed": passed,
        "checks_total": len(CHECKS),
        "selector_theorem": (
            "KER_A_SUBSET_KERNEL_OF_COMPLETE_RESPONSE_SIGNATURE_IFF_SELECTOR_EXISTS"
        ),
        "raw_identity_required": False,
        "gauge_verdict": "ORBIT_THEN_ORIENTATION_THEN_FORMATION_PATH",
        "host_verdict": "ENDPOINT_THEN_ROUTE_THEN_RESET_LINEAGE",
        "capability_verdict": "RESPONSE_EQUIVALENCE_REFINES_UNDER_ACTION_GROWTH",
        "physical_selection_verdict": (
            "CURRENT_WEAK_ANTECEDENTS_SELECT_RESTRICTED_CLASSES_ONLY"
        ),
        "repair_verdict": (
            "ROUTE_ORIENTATION_PATH_AND_RESET_FIELDS_CLOSE_ONLY_WHEN_PHYSICALLY_PREDECLARED"
        ),
        "complete_interface_selected_endogenously": False,
        "mathematical_core": "KNOWN_MATHEMATICS__FULLY_ABSORBED",
        "foliation_role": "INERT",
        "next_position": "N5-PF-P4_REGIONAL_FINALITY_EXCESS_CONTENT_HOSTILE_AUDIT",
        "maximum_grade": "SCOPED_NECESSITY_AND_OBSTRUCTION_THEOREM",
        "not_claimed": [
            "microscopic implementation uniqueness",
            "endogenous complete feedback boundary",
            "new behavioral-equivalence theorem",
            "new quantum process theorem",
            "new physical law",
            "ontological result",
            "grade-5 physical remainder",
            "prediction",
            "paper promotion",
            "hardware result",
        ],
    }

    if passed != len(CHECKS):
        failed = [check["name"] for check in CHECKS if not check["passed"]]
        print(f"FAIL: {passed}/{len(CHECKS)} checks; failed={failed}")
        return 1

    print(json.dumps(result, indent=2, sort_keys=True, default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
