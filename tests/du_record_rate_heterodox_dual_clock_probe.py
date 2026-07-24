#!/usr/bin/env python3
"""Heterodox dual-clock swing: local order+density versus a global scheduler.

The probe compares three deliberately small architectures.

``L-order-density``
    Observer records and causal messages form an asynchronous partial order.
    In 1+1 echo coordinates, causal-order-preserving linear comparisons have
    the form ``u' = a u, v' = b v`` with ``a,b>0``.  Order alone leaves the
    conformal factor ``a*b`` free.  Requiring a common spacetime-event density
    (not merely a density of records along one observer chain) sets ``a*b=1``.
    The resulting map is a Lorentz boost and preserves ``s^2=u*v``.

``G-full``
    One physical global update index K advances all observers, and every
    observer writes one record at every tick.  Messages propagate at a fixed
    substrate speed.  This creates delay and Doppler effects, but reunited
    observers have equal record counts.  A two-way light-time experiment also
    exposes absolute motion relative to the substrate.

``G-gated``
    K opens an update opportunity.  A quadratic update-budget gate
    ``r(v)^2 + (v/c0)^2 = 1`` admits only a fraction
    ``r(v)=sqrt(1-(v/c0)^2)`` of internal records.  If all moving bound
    structures also contract by the same factor, the finite twin and
    round-trip fixtures reproduce the special-relativistic values.  Those are
    additional dynamical assumptions; message delay alone does not provide
    them.

The calculation is an exact dependency and counterexample receipt.  It does
not derive a dimensional speed of light, an observer ontology, a continuum
limit, gravity, or a Dynamic Unity cosmological identity.
"""

from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Iterable


ARTIFACT_PATH = (
    Path(__file__).resolve().parent
    / "artifacts"
    / "du_record_rate_heterodox_dual_clock_probe_result.json"
)


def causal_matrix(
    events: Iterable[tuple[Fraction, Fraction]],
) -> tuple[tuple[bool, ...], ...]:
    """Causal precedence in 1+1 null coordinates, excluding equality."""

    rows = tuple(events)
    return tuple(
        tuple(
            index != other_index
            and u <= other_u
            and v <= other_v
            for other_index, (other_u, other_v) in enumerate(rows)
        )
        for index, (u, v) in enumerate(rows)
    )


def scale_null_coordinates(
    events: Iterable[tuple[Fraction, Fraction]],
    a: Fraction,
    b: Fraction,
) -> tuple[tuple[Fraction, Fraction], ...]:
    if a <= 0 or b <= 0:
        raise ValueError("causal-axis scale factors must be positive")
    return tuple((a * u, b * v) for u, v in events)


def radar_coordinates(
    send_count: Fraction,
    return_count: Fraction,
) -> tuple[Fraction, Fraction]:
    if return_count < send_count:
        raise ValueError("return cannot precede send")
    return (
        (send_count + return_count) / 2,
        (return_count - send_count) / 2,
    )


def interval_squared(
    delta_u: Fraction,
    delta_v: Fraction,
) -> Fraction:
    return delta_u * delta_v


def count_topological_orders(
    names: tuple[str, ...],
    edges: tuple[tuple[str, str], ...],
) -> int:
    """Exhaustively count linear extensions of a tiny message DAG."""

    predecessors = {
        name: {left for left, right in edges if right == name}
        for name in names
    }

    def recurse(prefix: tuple[str, ...], remaining: frozenset[str]) -> int:
        if not remaining:
            return 1
        placed = set(prefix)
        available = sorted(
            name
            for name in remaining
            if predecessors[name].issubset(placed)
        )
        return sum(
            recurse(prefix + (name,), remaining - {name})
            for name in available
        )

    return recurse(tuple(), frozenset(names))


def round_trip_global_ticks(
    rest_separation: Fraction,
    signal_speed: Fraction,
    apparatus_speed: Fraction,
    length_factor: Fraction,
) -> Fraction:
    """Two-way substrate time for a collinear comoving emitter and mirror."""

    if abs(apparatus_speed) >= signal_speed:
        raise ValueError("apparatus must be sub-signal")
    moving_separation = rest_separation * length_factor
    outbound = moving_separation / (signal_speed - apparatus_speed)
    inbound = moving_separation / (signal_speed + apparatus_speed)
    return outbound + inbound


def budget_gate(beta: Fraction) -> Fraction:
    """Exact quadratic update-budget gate for Pythagorean beta fixtures."""

    squared = Fraction(1) - beta * beta
    if squared < 0:
        raise ValueError("beta must be subluminal")
    numerator_root = math.isqrt(squared.numerator)
    denominator_root = math.isqrt(squared.denominator)
    if (
        numerator_root * numerator_root != squared.numerator
        or denominator_root * denominator_root != squared.denominator
    ):
        raise ValueError("fixture does not have a rational square-root gate")
    return Fraction(numerator_root, denominator_root)


def alternative_gate(beta: float, power: float) -> float:
    """A sensitivity family exposing that the quadratic budget is selected."""

    return (1.0 - abs(beta) ** power) ** (1.0 / power)


def main() -> None:
    # Common echo transcript.  It is observationally compatible with both an
    # asynchronous local-clock account and a stationary global-clock account.
    send = Fraction(10)
    reflected = Fraction(17)
    returned = Fraction(24)
    radar_time, radar_distance = radar_coordinates(send, returned)

    # Branch L: exact order/conformal-factor factorization.
    events = (
        (Fraction(0), Fraction(0)),
        (Fraction(1), Fraction(0)),
        (Fraction(0), Fraction(1)),
        (Fraction(1), Fraction(1)),
        (Fraction(2), Fraction(1)),
        (Fraction(1), Fraction(2)),
        (Fraction(2), Fraction(2)),
    )
    lorentz_a = Fraction(2)
    lorentz_b = Fraction(1, 2)
    conformal_a = Fraction(2)
    conformal_b = Fraction(1)
    base_order = causal_matrix(events)
    lorentz_order = causal_matrix(
        scale_null_coordinates(events, lorentz_a, lorentz_b)
    )
    conformal_order = causal_matrix(
        scale_null_coordinates(events, conformal_a, conformal_b)
    )
    sample_interval = (Fraction(3), Fraction(5))
    base_interval = interval_squared(*sample_interval)
    lorentz_interval = interval_squared(
        lorentz_a * sample_interval[0],
        lorentz_b * sample_interval[1],
    )
    conformal_interval = interval_squared(
        conformal_a * sample_interval[0],
        conformal_b * sample_interval[1],
    )
    doppler_factor = lorentz_a
    gamma = (doppler_factor + 1 / doppler_factor) / 2
    beta = (
        (doppler_factor - 1 / doppler_factor)
        / (doppler_factor + 1 / doppler_factor)
    )

    # This ordinary integer null-coordinate lattice is not invariant under
    # this boost: odd v values become half-integral.  A homogeneous Poisson
    # intensity, by contrast, has invariant measure because det=1.  This is
    # not a no-go for qualified Lorentzian lattices in 1+1 dimensions or for
    # specially constructed exactly covariant Clock-QCA circuit encodings.
    lattice = tuple(
        (Fraction(u), Fraction(v))
        for u in range(5)
        for v in range(5)
    )
    boosted_lattice = scale_null_coordinates(
        lattice, lorentz_a, lorentz_b
    )
    lattice_points_remaining_integral = sum(
        point_u.denominator == 1 and point_v.denominator == 1
        for point_u, point_v in boosted_lattice
    )

    # The causal/message graph forgets simultaneity labels.  A scheduler can
    # therefore look asynchronous even though one selected layering exists.
    dag_names = ("A0", "B0", "A1", "B1", "A2", "B2")
    dag_edges = (
        ("A0", "A1"),
        ("A1", "A2"),
        ("B0", "B1"),
        ("B1", "B2"),
        ("A1", "B2"),
    )
    linear_extension_count = count_topological_orders(dag_names, dag_edges)

    # Common reunion fixture: c0=5 cells/tick and |v|=3 cells/tick gives
    # beta=3/5 and an exact gate 4/5.  The traveler spends 50 ticks outbound
    # and 50 inbound, ending at the shared event.
    signal_speed = Fraction(5)
    traveler_speed = Fraction(3)
    reunion_ticks = Fraction(100)
    beta_g = traveler_speed / signal_speed
    gate = budget_gate(beta_g)
    g_full_a_records = reunion_ticks
    g_full_b_records = reunion_ticks
    target_a_proper = reunion_ticks
    target_b_proper = reunion_ticks * gate
    g_gated_a_records = reunion_ticks
    g_gated_b_records = reunion_ticks * gate

    # Preferred-frame two-way null, requiring no distant synchronization.
    rest_separation = Fraction(40)
    rest_round_trip = round_trip_global_ticks(
        rest_separation,
        signal_speed,
        Fraction(0),
        Fraction(1),
    )
    moving_full_round_trip = round_trip_global_ticks(
        rest_separation,
        signal_speed,
        traveler_speed,
        Fraction(1),
    )
    moving_gate_only_local_records = moving_full_round_trip * gate
    moving_contraction_only_global_records = round_trip_global_ticks(
        rest_separation,
        signal_speed,
        traveler_speed,
        gate,
    )
    moving_gate_and_contraction_local_records = (
        moving_contraction_only_global_records * gate
    )

    # Branch-L reunion from the order+density interval in echo/null units.
    # Each 50-tick leg has spatial displacement 150 cells = 30 light ticks.
    leg_coordinate_time = Fraction(50)
    leg_light_distance = Fraction(30)
    leg_delta_u = leg_coordinate_time - leg_light_distance
    leg_delta_v = leg_coordinate_time + leg_light_distance
    branch_l_leg_interval = math.isqrt(
        interval_squared(leg_delta_u, leg_delta_v).numerator
    )
    branch_l_traveler_records = 2 * branch_l_leg_interval

    # Delay-only control: after the known seven-tick outward and return
    # propagation legs are removed, the stationary global transcript contains
    # no clock offset or differential accumulation.
    modeled_round_trip_delay = returned - send
    delay_subtracted_offset = (
        reflected - send - modeled_round_trip_delay / 2
    )

    checks = [
        {
            "name": "common echo defines radar time and distance but not an independent dimensional speed",
            "pass": (
                radar_time == reflected
                and radar_distance == Fraction(7)
            ),
        },
        {
            "name": "positive null-axis rescaling preserves the full finite causal order",
            "pass": (
                base_order == lorentz_order == conformal_order
            ),
        },
        {
            "name": "order-preserving maps retain a free conformal factor",
            "pass": conformal_interval == 2 * base_interval,
        },
        {
            "name": "common spacetime-event density removes that factor for the boost fixture",
            "pass": (
                lorentz_a * lorentz_b == 1
                and lorentz_interval == base_interval
            ),
        },
        {
            "name": "the order-plus-density map yields the beta=3/5 Lorentz coefficients",
            "pass": gamma == Fraction(5, 4) and beta == Fraction(3, 5),
        },
        {
            "name": "the tested ordinary integer null-coordinate lattice leaks under the same boost",
            "pass": lattice_points_remaining_integral < len(lattice),
        },
        {
            "name": "forgetting scheduler layers leaves multiple asynchronous linear extensions",
            "pass": linear_extension_count > 1,
        },
        {
            "name": "G-full produces equal reunited record counts",
            "pass": g_full_a_records == g_full_b_records,
        },
        {
            "name": "G-full therefore misses the target twin elapsed-time difference",
            "pass": g_full_b_records != target_b_proper,
        },
        {
            "name": "modeled propagation delay subtracts to zero stationary clock offset",
            "pass": delay_subtracted_offset == 0,
        },
        {
            "name": "G-full two-way light time exposes absolute apparatus motion",
            "pass": moving_full_round_trip != rest_round_trip,
        },
        {
            "name": "quadratic G-gating reproduces the finite twin record difference",
            "pass": (
                gate == Fraction(4, 5)
                and g_gated_a_records == target_a_proper
                and g_gated_b_records == target_b_proper
            ),
        },
        {
            "name": "clock gating alone does not hide the preferred frame in two-way light time",
            "pass": moving_gate_only_local_records != rest_round_trip,
        },
        {
            "name": "material contraction alone does not hide the preferred frame in recorded time",
            "pass": moving_contraction_only_global_records != rest_round_trip,
        },
        {
            "name": "G-gating plus universal material contraction hides the frame on the finite round-trip fixture",
            "pass": (
                moving_gate_and_contraction_local_records
                == rest_round_trip
            ),
        },
        {
            "name": "Branch-L order-density interval reproduces the target reunion count conditionally",
            "pass": branch_l_traveler_records == int(target_b_proper),
        },
        {
            "name": "the quadratic update budget is a selected completion, not forced by cadence alone",
            "pass": (
                abs(alternative_gate(float(beta_g), 1.0) - float(gate))
                > 0.1
                and abs(
                    alternative_gate(float(beta_g), 4.0) - float(gate)
                )
                > 0.1
            ),
        },
    ]

    payload = {
        "probe": "du_record_rate_heterodox_dual_clock_probe",
        "question": (
            "Does universal record cadence plus causal message delay suffice "
            "for Lorentzian kinematics and reunion aging, and are Branch L "
            "and Branch G-full equally complete without added structure?"
        ),
        "warrants": [
            "DERIVED",
            "CONDITIONALLY_ENTAILED",
            "CONSTRUCTIVELY_REALIZED",
            "STRUCTURAL_ANALOGY",
        ],
        "common_echo": {
            "send_local_count": str(send),
            "reflection_local_count": str(reflected),
            "return_local_count": str(returned),
            "radar_time": str(radar_time),
            "radar_distance_in_record_ticks": str(radar_distance),
            "reading": (
                "The transcript defines radar coordinates and c=1 in those "
                "units.  It does not independently determine dimensional c, "
                "a simultaneity convention, or which clock architecture made it."
            ),
        },
        "branch_L_order_density": {
            "architecture": (
                "asynchronous causal/message order plus a common spacetime-"
                "event density and a separate observer-chain calibration"
            ),
            "cadence_denominator": (
                "one admitted local record transition; no global-time denominator"
            ),
            "order_only_family": "u'=a*u, v'=b*v for arbitrary a,b>0",
            "density_condition": "a*b=1",
            "boost_fixture": {
                "a": str(lorentz_a),
                "b": str(lorentz_b),
                "gamma": str(gamma),
                "beta": str(beta),
                "interval_before": str(base_interval),
                "interval_after": str(lorentz_interval),
            },
            "order_only_null": {
                "a": str(conformal_a),
                "b": str(conformal_b),
                "interval_before": str(base_interval),
                "interval_after": str(conformal_interval),
            },
            "reunion_fixture": {
                "stationary_records": int(target_a_proper),
                "traveler_records": branch_l_traveler_records,
                "status": (
                    "conditional on event-density/manifoldlike echo geometry "
                    "and observer-chain record calibration"
                ),
            },
            "regular_lattice_control": {
                "boosted_points_remaining_integral": (
                    lattice_points_remaining_integral
                ),
                "total_points": len(lattice),
                "reading": (
                    "the tested ordinary integer null-coordinate lattice is "
                    "not boost invariant; determinant one protects homogeneous "
                    "volume measure, not this fixed grid. This does not exclude "
                    "qualified 1+1 Lorentzian lattices or specially constructed "
                    "exactly covariant Clock-QCA circuit encodings"
                ),
            },
        },
        "branch_G": {
            "global_tick": "K, one substrate update interval",
            "signal_speed": (
                f"{signal_speed} substrate cells per global tick"
            ),
            "asynchronous_appearance": {
                "message_dag_linear_extensions": linear_extension_count,
                "reading": (
                    "if K labels are not stored, local records plus messages "
                    "do not identify the selected scheduler layering"
                ),
            },
            "G_full": {
                "record_rule": "exactly one record per observer per K",
                "reunion": {
                    "A_records": int(g_full_a_records),
                    "B_records": int(g_full_b_records),
                    "target_B_proper_ticks": int(target_b_proper),
                },
                "two_way_preferred_frame_null": {
                    "rest_global_and_local_ticks": str(rest_round_trip),
                    "moving_global_and_local_ticks": str(
                        moving_full_round_trip
                    ),
                },
                "delay_only_result": (
                    "propagation changes separated assignments but not reunited "
                    "record totals; the modeled stationary offset is zero"
                ),
            },
            "G_gated": {
                "extra_clock_gate": "r(v)=sqrt(1-(v/c0)^2)",
                "gate_at_beta_3_over_5": str(gate),
                "possible_native_story": (
                    "quadratic isotropic update budget "
                    "r^2+(v/c0)^2=1; the budget is an added posit"
                ),
                "extra_material_response": (
                    "all comoving bound lengths contract by the same r(v)"
                ),
                "reunion": {
                    "A_records": int(g_gated_a_records),
                    "B_records": int(g_gated_b_records),
                },
                "two_way_controls": {
                    "gate_only_local_ticks": str(
                        moving_gate_only_local_records
                    ),
                    "contraction_only_global_ticks": str(
                        moving_contraction_only_global_records
                    ),
                    "gate_and_contraction_local_ticks": str(
                        moving_gate_and_contraction_local_records
                    ),
                    "rest_local_ticks": str(rest_round_trip),
                },
                "completion_sensitivity": {
                    "power_1_gate": alternative_gate(
                        float(beta_g), 1.0
                    ),
                    "power_2_gate": float(gate),
                    "power_4_gate": alternative_gate(
                        float(beta_g), 4.0
                    ),
                },
                "reading": (
                    "the global foliation is hidden on these two finite "
                    "fixtures only after adding a Lorentz-shaped gate and a "
                    "universal material response; full operational hiding "
                    "remains unestablished"
                ),
            },
            "positive_antecedent_scope": {
                "Clock_QCA": (
                    "Arrighi, Facchini, and Forets construct a special 1+1 "
                    "Clock QCA with exact discrete covariance under their "
                    "circuit-encoding Lorentz transformations. This keeps a "
                    "global-clock completion live but does not establish that "
                    "its internal counters or keep-going signals equal an "
                    "observer's irreversible physical record count"
                ),
                "next_test": (
                    "extract an operational observer and reunion-record "
                    "functional from the exact Clock-QCA construction, then "
                    "test covariance of accumulated records rather than only "
                    "of the circuit dynamics"
                ),
            },
        },
        "typed_result": {
            "operational_definition": (
                "radar time/distance and c=1 in record-tick units"
            ),
            "conditional_construction": (
                "Branch L order+spacetime density and Branch G-gated "
                "clock+material response each realize the finite target"
            ),
            "kinematic_recovery": (
                "exact 1+1 boost/interval algebra for L; twin and two-way "
                "fixtures for the declared G-gated completion"
            ),
            "dynamical_selection": "OPEN in both branches",
            "dimensional_calibration": "OPEN beyond declared cell/tick units",
            "physical_prediction": "NONE",
        },
        "checks": checks,
        "checks_passed": sum(bool(check["pass"]) for check in checks),
        "checks_total": len(checks),
        "verdict": (
            "CADENCE-PLUS-DELAY-ALONE-OVERTURNED / "
            "L-ORDER-PLUS-SPACETIME-DENSITY-CONDITIONALLY-RECOVERS-1P1-KINEMATICS / "
            "G-FULL-FAILS-REUNION-AND-PREFERRED-FRAME-NULLS / "
            "G-GATED-FINITE-RECOVERY-REQUIRES-EXPOSED-CLOCK-AND-MATERIAL-DYNAMICS"
        ),
        "forbidden_overclaims": [
            "the common echo transcript predicts dimensional c",
            "local observer-record density is automatically spacetime volume density",
            "G-full message delay is relativistic differential aging",
            "the quadratic gate or material contraction is selected by the global clock",
            "two finite cancellations prove the global foliation is gauge",
            "the tested ordinary integer lattice rules out qualified 1+1 Lorentzian lattices",
            "the G-full counterexample rules out special exactly covariant Clock-QCA constructions",
            "either branch derives gravity, cosmology, or Lambda",
        ],
    }

    ARTIFACT_PATH.parent.mkdir(parents=True, exist_ok=True)
    ARTIFACT_PATH.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    if payload["checks_passed"] != payload["checks_total"]:
        failed = [
            check["name"] for check in checks if not bool(check["pass"])
        ]
        raise SystemExit(f"failed checks: {failed}")
    print(
        f"{payload['checks_passed']}/{payload['checks_total']} checks pass"
    )
    print(payload["verdict"])
    print(ARTIFACT_PATH)


if __name__ == "__main__":
    main()
