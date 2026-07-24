#!/usr/bin/env python3
"""Orthodox dual-clock benchmark: local Lorentz clocks versus one global clock.

This probe compares three explicitly different conditional constructions.

``L-SR``
    Each observer carries an equally calibrated local record counter and
    reciprocal echo factors compose multiplicatively.  On the conventional
    inertial/light-signal fixture this is Bondi's ``k`` calculus:

        k^2 = (1+beta)/(1-beta),
        beta = (k^2-1)/(k^2+1),
        gamma = (k+k^-1)/2.

    This operationally reconstructs Lorentz rapidity once reciprocity and the
    signal cone are admitted.  Local cadence alone does not derive either.

``G-full``
    One physical update index ``K`` is global, every observer adds exactly one
    physical record per ``K`` tick, Euclidean positions are defined on its
    slices, and signals have slopes ``+/-1`` in that preferred frame.  Finite
    propagation reproduces the same A-only echo as ``L-SR`` but not the
    reflecting observer's count, reciprocal Doppler factors, boost
    invariance, moving-laboratory two-way signal speed, or differential
    reunion aging.

``G-gated``
    The same global substrate is retained, but moving physical clocks admit
    records at ``1/gamma`` per global tick and moving rods contract by
    ``1/gamma``.  This Lorentz-ether-style completion repairs the finite
    fixtures and can hide the preferred frame from ideal rods and clocks.
    It is an additional dynamical mechanism, not a consequence of message
    latency, and it is not ``G-full``.

All calculations use exact rational arithmetic.  The selected velocities have
rational beta, gamma, and k.  The result is a scoped discriminator, not a
derivation of spacetime, dimensional c, gravity, or Dynamic Unity.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any

from conditional_candidate_harness import (
    SCHEMA_VERSION,
    comparison_receipt,
    write_candidate_artifact,
)


ARTIFACT_PATH = (
    Path(__file__).resolve().parent
    / "artifacts"
    / "du_record_rate_orthodox_clock_tournament_result.json"
)


@dataclass(frozen=True)
class RationalBoost:
    beta: Fraction
    gamma: Fraction
    k: Fraction


BOOSTS = (
    RationalBoost(Fraction(5, 13), Fraction(13, 12), Fraction(3, 2)),
    RationalBoost(Fraction(3, 5), Fraction(5, 4), Fraction(2, 1)),
    RationalBoost(Fraction(8, 17), Fraction(17, 15), Fraction(5, 3)),
)


def q(value: Fraction) -> str:
    """Stable JSON representation of an exact rational."""

    return (
        str(value.numerator)
        if value.denominator == 1
        else f"{value.numerator}/{value.denominator}"
    )


def boost_is_consistent(boost: RationalBoost) -> bool:
    beta, gamma, k = boost.beta, boost.gamma, boost.k
    return (
        gamma * gamma * (1 - beta * beta) == 1
        and k * k == (1 + beta) / (1 - beta)
        and gamma == (k + 1 / k) / 2
    )


def echo_fixture(boost: RationalBoost, send: Fraction) -> dict[str, Any]:
    """Return exact L-SR and G-full predictions for one reflected signal.

    A and B meet at the origin.  In the G-full coordinates A is at rest and B
    follows x=beta*K.  A emits at count/time ``send``.  The signal has slope
    +1, reflects immediately at B, and returns to A with slope -1.
    """

    beta, gamma, k = boost.beta, boost.gamma, boost.k
    receive_a = send * (1 + beta) / (1 - beta)
    radar_time = (send + receive_a) / 2
    radar_distance = (receive_a - send) / 2

    # Branch L target: B's local counter is proper-time calibrated.
    reflect_l = radar_time / gamma
    outward_l = reflect_l / send
    inward_l = receive_a / reflect_l

    # Branch G-full: every observer's physical record counter equals K.
    reflect_g = send / (1 - beta)
    outward_g = reflect_g / send
    inward_g = receive_a / reflect_g

    # Branch G-gated: the same preferred K drives update opportunities, but
    # B's moving physical clock admits only 1/gamma of them as records.
    reflect_gated = reflect_g / gamma
    outward_gated = reflect_gated / send
    inward_gated = receive_a / reflect_gated

    return {
        "beta": q(beta),
        "gamma": q(gamma),
        "k": q(k),
        "send_A": q(send),
        "return_A": q(receive_a),
        "radar_time_A": q(radar_time),
        "radar_distance_A": q(radar_distance),
        "radar_beta": q(radar_distance / radar_time),
        "radar_c": q(2 * radar_distance / (receive_a - send)),
        "L_SR": {
            "reflect_B": q(reflect_l),
            "outward_factor": q(outward_l),
            "inward_factor": q(inward_l),
            "delay_corrected_A_time_over_B_count": q(
                radar_time / reflect_l
            ),
        },
        "G_full": {
            "reflect_B": q(reflect_g),
            "outward_factor": q(outward_g),
            "inward_factor": q(inward_g),
            "delay_corrected_A_time_minus_B_count": q(
                radar_time - reflect_g
            ),
        },
        "G_gated": {
            "reflect_B": q(reflect_gated),
            "outward_factor": q(outward_gated),
            "inward_factor": q(inward_gated),
            "record_admission_per_global_tick": q(1 / gamma),
        },
        "_exact": {
            "receive_a": receive_a,
            "radar_time": radar_time,
            "radar_distance": radar_distance,
            "reflect_l": reflect_l,
            "outward_l": outward_l,
            "inward_l": inward_l,
            "reflect_g": reflect_g,
            "outward_g": outward_g,
            "inward_g": inward_g,
            "reflect_gated": reflect_gated,
            "outward_gated": outward_gated,
            "inward_gated": inward_gated,
        },
    }


def resynchronization_null(fixture: dict[str, Any]) -> dict[str, Any]:
    """Re-slice the reflection event without changing any physical counts."""

    exact = fixture["_exact"]
    send = Fraction(fixture["send_A"])
    receive = exact["receive_a"]
    distance = exact["radar_distance"]
    rows = []
    for epsilon in (Fraction(1, 4), Fraction(1, 2), Fraction(3, 4)):
        coordinate_time = (1 - epsilon) * send + epsilon * receive
        outward_speed = distance / (coordinate_time - send)
        inward_speed = distance / (receive - coordinate_time)
        rows.append(
            {
                "epsilon": q(epsilon),
                "reflection_coordinate_time": q(coordinate_time),
                "outward_one_way_speed": q(outward_speed),
                "inward_one_way_speed": q(inward_speed),
                "round_trip_speed": q(
                    2 * distance / (receive - send)
                ),
            }
        )
    return {
        "rows": rows,
        "unchanged_observer_counts": {
            "L_SR_reflect_B": fixture["L_SR"]["reflect_B"],
            "G_full_reflect_B": fixture["G_full"]["reflect_B"],
            "G_gated_reflect_B": fixture["G_gated"]["reflect_B"],
            "return_A": fixture["return_A"],
        },
    }


def g_full_echo_factors(
    observer_a_velocity: Fraction,
    observer_b_velocity: Fraction,
) -> tuple[Fraction, Fraction, Fraction]:
    """Split global-count factors and A-only product in the preferred frame."""

    u = observer_a_velocity
    v = observer_b_velocity
    if not (-1 < u < v < 1):
        raise ValueError("require -1<u<v<1 for the fixture")
    outward = (1 - u) / (1 - v)
    inward = (1 + v) / (1 + u)
    return outward, inward, outward * inward


def g_gated_echo_factors(
    observer_a_velocity: Fraction,
    observer_b_velocity: Fraction,
    gamma_a_over_gamma_b: Fraction,
) -> tuple[Fraction, Fraction, Fraction]:
    """Split physical-record factors after Lorentz-ether clock gating."""

    outward_g, inward_g, _ = g_full_echo_factors(
        observer_a_velocity,
        observer_b_velocity,
    )
    # n_A=K/gamma_A and m_B=K/gamma_B.
    outward = outward_g * gamma_a_over_gamma_b
    inward = inward_g / gamma_a_over_gamma_b
    return outward, inward, outward * inward


def boost_and_preferred_frame_tests() -> dict[str, Any]:
    """Hold relative rapidity fixed and inspect A-only versus split records."""

    first = BOOSTS[1]  # beta=3/5, k=2
    second = BOOSTS[0]  # beta=5/13, k=3/2
    composed_k = first.k * second.k
    beta_from_k = (composed_k * composed_k - 1) / (
        composed_k * composed_k + 1
    )
    einstein_beta = (first.beta + second.beta) / (
        1 + first.beta * second.beta
    )
    galilean_beta = first.beta + second.beta

    # These two pairs are related by a common Lorentz boost of 1/5:
    # (u,v)=(0,3/5) -> (1/5,5/7).  Both have Einstein-relative beta=3/5.
    base_u, base_v = Fraction(0), Fraction(3, 5)
    shifted_u, shifted_v = Fraction(1, 5), Fraction(5, 7)
    base_relative_beta = (base_v - base_u) / (1 - base_u * base_v)
    shifted_relative_beta = (
        (shifted_v - shifted_u) / (1 - shifted_u * shifted_v)
    )

    base_g_full = g_full_echo_factors(base_u, base_v)
    shifted_g_full = g_full_echo_factors(shifted_u, shifted_v)

    # gamma_A/gamma_B is rational for both selected pairs even though the
    # individual gammas in the shifted pair contain sqrt(24).
    base_gamma_ratio = Fraction(4, 5)
    shifted_gamma_ratio = Fraction(5, 7)
    assert (
        base_gamma_ratio * base_gamma_ratio
        == (1 - base_v * base_v) / (1 - base_u * base_u)
    )
    assert (
        shifted_gamma_ratio * shifted_gamma_ratio
        == (1 - shifted_v * shifted_v)
        / (1 - shifted_u * shifted_u)
    )
    base_g_gated = g_gated_echo_factors(
        base_u,
        base_v,
        base_gamma_ratio,
    )
    shifted_g_gated = g_gated_echo_factors(
        shifted_u,
        shifted_v,
        shifted_gamma_ratio,
    )

    return {
        "L_SR_composition": {
            "k1": q(first.k),
            "k2": q(second.k),
            "k_composed": q(composed_k),
            "beta_from_composed_k": q(beta_from_k),
            "einstein_velocity_addition": q(einstein_beta),
        },
        "G_full_composition": {
            "galilean_velocity_sum": q(galilean_beta),
            "preferred_signal_limit": "1",
        },
        "common_Lorentz_boost_null": {
            "base_velocities_u_v": [q(base_u), q(base_v)],
            "shifted_velocities_u_v": [q(shifted_u), q(shifted_v)],
            "base_Einstein_relative_beta": q(base_relative_beta),
            "shifted_Einstein_relative_beta": q(shifted_relative_beta),
            "G_full": {
                "base_outward_inward_product": [q(x) for x in base_g_full],
                "shifted_outward_inward_product": [
                    q(x) for x in shifted_g_full
                ],
                "A_only_product_invariant": (
                    base_g_full[2] == shifted_g_full[2]
                ),
                "split_reflector_record_leaks_preferred_frame": (
                    base_g_full[:2] != shifted_g_full[:2]
                ),
            },
            "G_gated": {
                "base_outward_inward_product": [q(x) for x in base_g_gated],
                "shifted_outward_inward_product": [
                    q(x) for x in shifted_g_gated
                ],
                "split_factors_hidden_on_fixture": (
                    base_g_gated == shifted_g_gated
                ),
            },
        },
        "_exact": {
            "beta_from_k": beta_from_k,
            "einstein_beta": einstein_beta,
            "galilean_beta": galilean_beta,
            "base_relative_beta": base_relative_beta,
            "shifted_relative_beta": shifted_relative_beta,
            "base_g_full": base_g_full,
            "shifted_g_full": shifted_g_full,
            "base_g_gated": base_g_gated,
            "shifted_g_gated": shifted_g_gated,
        },
    }


def reunion_and_light_clock(boost: RationalBoost) -> dict[str, Any]:
    """Price delay-free reunion and the minimal Lorentz-ether rescue."""

    beta, gamma = boost.beta, boost.gamma
    global_duration = Fraction(100)
    rest_rod_length = Fraction(12)

    l_a_records = global_duration
    l_b_records = global_duration / gamma
    g_a_records = global_duration
    g_b_records = global_duration
    gated_b_records = global_duration / gamma

    # G-full moving laboratory: preferred-frame separation is unchanged and
    # its clock records every K tick.
    g_full_roundtrip_ticks = (
        2 * rest_rod_length / (1 - beta * beta)
    )
    g_full_two_way_speed = (
        2 * rest_rod_length / g_full_roundtrip_ticks
    )

    # G-gated Lorentz-ether completion: preferred-frame rod separation
    # contracts, and the physical clock admits only 1/gamma records per K.
    preferred_rod_length = rest_rod_length / gamma
    gated_roundtrip_global_ticks = (
        2 * preferred_rod_length / (1 - beta * beta)
    )
    gated_roundtrip_physical_records = (
        gated_roundtrip_global_ticks / gamma
    )
    gated_two_way_speed = (
        2 * rest_rod_length / gated_roundtrip_physical_records
    )

    return {
        "global_duration": q(global_duration),
        "reunion": {
            "L_SR": {
                "A_records": q(l_a_records),
                "B_records": q(l_b_records),
                "difference": q(l_a_records - l_b_records),
            },
            "G_full": {
                "A_records": q(g_a_records),
                "B_records": q(g_b_records),
                "difference": q(g_a_records - g_b_records),
            },
            "G_gated": {
                "global_updates_seen_by_B": q(global_duration),
                "B_physical_records": q(gated_b_records),
                "record_admission_per_global_tick": q(1 / gamma),
            },
        },
        "moving_light_clock": {
            "rest_rod_length": q(rest_rod_length),
            "G_full": {
                "global_roundtrip_ticks": q(g_full_roundtrip_ticks),
                "measured_two_way_speed": q(g_full_two_way_speed),
            },
            "G_gated": {
                "preferred_frame_rod_length": q(preferred_rod_length),
                "global_roundtrip_ticks": q(
                    gated_roundtrip_global_ticks
                ),
                "physical_clock_records": q(
                    gated_roundtrip_physical_records
                ),
                "measured_two_way_speed": q(gated_two_way_speed),
            },
        },
        "_exact": {
            "l_a_records": l_a_records,
            "l_b_records": l_b_records,
            "g_a_records": g_a_records,
            "g_b_records": g_b_records,
            "gated_b_records": gated_b_records,
            "g_full_two_way_speed": g_full_two_way_speed,
            "gated_two_way_speed": gated_two_way_speed,
        },
    }


def strip_exact(value: Any) -> Any:
    if isinstance(value, dict):
        return {
            key: strip_exact(item)
            for key, item in value.items()
            if key != "_exact"
        }
    if isinstance(value, list):
        return [strip_exact(item) for item in value]
    return value


def main() -> None:
    send = Fraction(60)
    echoes = [echo_fixture(boost, send) for boost in BOOSTS]
    primary = echoes[1]
    reslicing = resynchronization_null(primary)
    boost_tests = boost_and_preferred_frame_tests()
    reunion = reunion_and_light_clock(BOOSTS[1])

    all_echoes_same_for_a = all(
        row["_exact"]["receive_a"]
        == send * boost.k * boost.k
        for row, boost in zip(echoes, BOOSTS)
    )
    l_reciprocal = all(
        row["_exact"]["outward_l"]
        == row["_exact"]["inward_l"]
        == boost.k
        for row, boost in zip(echoes, BOOSTS)
    )
    g_nonreciprocal = all(
        row["_exact"]["outward_g"] != row["_exact"]["inward_g"]
        for row in echoes
    )
    g_gated_reciprocal = all(
        row["_exact"]["outward_gated"]
        == row["_exact"]["inward_gated"]
        == boost.k
        for row, boost in zip(echoes, BOOSTS)
    )
    radar_recovers_beta = all(
        row["_exact"]["radar_distance"]
        / row["_exact"]["radar_time"]
        == boost.beta
        for row, boost in zip(echoes, BOOSTS)
    )
    delay_correction_erases_g_difference = all(
        row["_exact"]["radar_time"] == row["_exact"]["reflect_g"]
        for row in echoes
    )
    l_recovers_gamma = all(
        row["_exact"]["radar_time"] / row["_exact"]["reflect_l"]
        == boost.gamma
        for row, boost in zip(echoes, BOOSTS)
    )

    checks = [
        {
            "name": "rational boost fixtures satisfy gamma, k, and beta identities",
            "pass": all(boost_is_consistent(boost) for boost in BOOSTS),
        },
        {
            "name": "L-SR and G-full give the same A-only send-return echoes",
            "pass": all_echoes_same_for_a,
        },
        {
            "name": "L-SR local counts give reciprocal Doppler factors",
            "pass": l_reciprocal,
        },
        {
            "name": "G-full global-count records give nonreciprocal factors",
            "pass": g_nonreciprocal,
        },
        {
            "name": "G-gated clock admission repairs reciprocal echo factors",
            "pass": g_gated_reciprocal,
        },
        {
            "name": "A radar coordinates recover beta in the common fixture",
            "pass": radar_recovers_beta,
        },
        {
            "name": "exact travel-time correction erases the G-full remote clock difference",
            "pass": delay_correction_erases_g_difference,
        },
        {
            "name": "L-SR reciprocal record factors reconstruct gamma",
            "pass": l_recovers_gamma,
        },
        {
            "name": "epsilon resynchronization changes one-way speeds but not round-trip speed",
            "pass": (
                [row["outward_one_way_speed"] for row in reslicing["rows"]]
                == ["2", "1", "2/3"]
                and [row["inward_one_way_speed"] for row in reslicing["rows"]]
                == ["2/3", "1", "2"]
                and all(
                    row["round_trip_speed"] == "1"
                    for row in reslicing["rows"]
                )
            ),
        },
        {
            "name": "multiplicative local exchange factors give Einstein boost composition",
            "pass": (
                boost_tests["_exact"]["beta_from_k"]
                == boost_tests["_exact"]["einstein_beta"]
                == Fraction(4, 5)
            ),
        },
        {
            "name": "G-full A-only echo is invariant under a common Lorentz boost",
            "pass": (
                boost_tests["_exact"]["base_relative_beta"]
                == boost_tests["_exact"]["shifted_relative_beta"]
                == Fraction(3, 5)
                and boost_tests["_exact"]["base_g_full"][2]
                == boost_tests["_exact"]["shifted_g_full"][2]
                == 4
            ),
        },
        {
            "name": "G-full split reflector record leaks the preferred frame",
            "pass": (
                boost_tests["_exact"]["base_g_full"][:2]
                == (Fraction(5, 2), Fraction(8, 5))
                and boost_tests["_exact"]["shifted_g_full"][:2]
                == (Fraction(14, 5), Fraction(10, 7))
            ),
        },
        {
            "name": "G-gated split factors hide the frame on the boost fixture",
            "pass": (
                boost_tests["_exact"]["base_g_gated"]
                == boost_tests["_exact"]["shifted_g_gated"]
                == (Fraction(2), Fraction(2), Fraction(4))
            ),
        },
        {
            "name": "G-full reunited observers have equal record counts",
            "pass": (
                reunion["_exact"]["g_a_records"]
                == reunion["_exact"]["g_b_records"]
            ),
        },
        {
            "name": "L-SR reunion retains differential elapsed local records with zero endpoint delay",
            "pass": (
                reunion["_exact"]["l_a_records"]
                > reunion["_exact"]["l_b_records"]
                == 80
            ),
        },
        {
            "name": "G-full moving-laboratory two-way signal speed depends on absolute velocity",
            "pass": reunion["_exact"]["g_full_two_way_speed"] == Fraction(16, 25),
        },
        {
            "name": "G-gated Lorentz-ether clock and rod laws repair the two-way signal fixture",
            "pass": reunion["_exact"]["gated_two_way_speed"] == 1,
        },
        {
            "name": "G-gated repairs reunion aging only by skipping physical records",
            "pass": (
                reunion["_exact"]["gated_b_records"]
                == reunion["_exact"]["l_b_records"]
                < Fraction(100)
            ),
        },
        {
            "name": "radar c=1 follows identically from the radar-distance definition",
            "pass": all(row["radar_c"] == "1" for row in echoes),
        },
    ]
    passed = sum(bool(item["pass"]) for item in checks)

    candidate = {
        "schema_version": SCHEMA_VERSION,
        "candidate_id": "DU-ORTHODOX-DUAL-RECORD-CLOCK-TOURNAMENT",
        "track": (
            "Science Council dual primitive-record-clock wave / conventional "
            "echo, boost, delay, reunion, and preferred-frame benchmark"
        ),
        "question": (
            "Can G-full—one physical record per global tick with all apparent "
            "differences attributed to message delay—recover the operational "
            "Lorentz kinematics available to a reciprocal local-clock model, "
            "or is an additional G-gating dynamics required?"
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
                    "The bounded comparator is a 1+1 inertial echo and reunion "
                    "fixture with instantaneous reflection/turnaround."
                ),
                "status": "STANDARD",
                "role": "Defines a conventional special-relativistic target.",
            },
            {
                "id": "A2",
                "statement": (
                    "L-SR uses equally calibrated local physical records plus "
                    "a reciprocal limiting-signal exchange law."
                ),
                "status": "CONDITIONAL_POSIT",
                "role": (
                    "Allows operational k, rapidity, beta, and gamma "
                    "reconstruction without a global synchronization."
                ),
            },
            {
                "id": "A3",
                "statement": (
                    "G-full has a global update K, Euclidean preferred slices, "
                    "signal slope +/-1 on those slices, and exactly one "
                    "physical observer record per K tick."
                ),
                "status": "CONDITIONAL_POSIT",
                "role": "Tests the strongest literal delay-only branch.",
            },
            {
                "id": "A4",
                "statement": (
                    "G-gated admits records at 1/gamma per K and contracts a "
                    "moving rod by 1/gamma."
                ),
                "status": "CONDITIONAL_POSIT",
                "role": (
                    "Constructs the minimum Lorentz-ether-style rescue on the "
                    "declared finite fixtures."
                ),
            },
            {
                "id": "A5",
                "statement": (
                    "The record interval and limiting slope are dimensionless "
                    "units; no dimensional value of c is inferred."
                ),
                "status": "IMPORTED",
                "role": "Prevents a radar convention from becoming metrology.",
            },
        ],
        "free_choices": [
            {
                "id": "C1",
                "choice": (
                    "Use beta in {5/13,3/5,8/17}, whose gamma and k are rational."
                ),
                "why_not_forced": "They are exact finite audit fixtures.",
                "sensitivity_test": (
                    "Require every branch identity across all three velocities."
                ),
            },
            {
                "id": "C2",
                "choice": "Use Einstein radar time as the displayed midpoint.",
                "why_not_forced": "One-way synchronization is conventional.",
                "sensitivity_test": (
                    "Sweep epsilon in {1/4,1/2,3/4}; physical counts and "
                    "round-trip speed must remain unchanged."
                ),
            },
            {
                "id": "C3",
                "choice": (
                    "Use the textbook Lorentz-ether gating and contraction laws."
                ),
                "why_not_forced": (
                    "A fundamental record model would have to derive them."
                ),
                "sensitivity_test": (
                    "Keep the G-full comparator visible and record which "
                    "additional laws repair which failed observables."
                ),
            },
        ],
        "equations": [
            "k^2=(1+beta)/(1-beta)",
            "beta=(k^2-1)/(k^2+1)",
            "gamma=(k+k^-1)/2",
            "L-SR: m_B=k n_s and n_r=k m_B",
            "G-full: m_B=n_s/(1-beta), n_r=n_s(1+beta)/(1-beta)",
            "G-gated: m_B=n_s/[gamma(1-beta)]=k n_s",
            "t_radar=(n_s+n_r)/2; rho_radar=(n_r-n_s)/2",
            "G-full reunion: Delta n_A=Delta n_B=Delta K",
            "L-SR/G-gated reunion: Delta n_B=Delta K/gamma",
            "G-full moving-lab c_2way=1-beta^2",
            "G-gated: L_preferred=L_rest/gamma and dn/dK=1/gamma",
        ],
        "observables": [
            "A send and return counts",
            "B reflection count returned in the message",
            "outbound and inbound record ratios",
            "radar time and radar distance",
            "reunion record counts",
            "two-way moving-laboratory signal speed",
            "common-boost dependence of the split reflector record",
        ],
        "comparators": [
            "L-SR reciprocal local-clock benchmark",
            "G-full exact one-record-per-global-tick delay model",
            "G-gated Lorentz-ether-style rescue",
        ],
        "null_models": [
            "exact signal-travel-time subtraction",
            "epsilon resynchronization",
            "common Lorentz boost at fixed relative rapidity",
            "zero-delay reunion",
            "moving-laboratory round trip",
        ],
        "falsifiers": [
            "G-full yields unequal reunion counts without gating",
            "G-full record ratios are reciprocal for nonzero beta",
            "G-full split record factors depend only on relative rapidity",
            "G-full moving laboratories measure the same two-way signal speed",
            "G-gated repairs the targets without motion-dependent record admission",
        ],
        "stop_conditions": [
            "Do not reject every global-clock theory from the G-full failure.",
            "Do not call a Lorentz-ether gating law a consequence of latency.",
            "Do not say Branch L derives proper time from local cadence alone.",
            "Do not call radar c=1 an independent prediction.",
            "Do not infer gravity, dimensional c, a DU observer ontology, or Lambda.",
        ],
        "concept": {
            "concept_id": "DU-DUAL-PRIMITIVE-RECORD-CLOCK",
            "invariant": (
                "A successful record-clock architecture must separate "
                "propagation delay from path-dependent elapsed records and "
                "must either hide or expose its preferred foliation."
            ),
            "formalization_id": (
                "ORTHODOX-L-SR-VS-G-FULL-WITH-G-GATED-RESCUE"
            ),
            "failure_scope": "FORMALIZATION",
        },
        "result": {
            "claim": (
                "A-only echoes underdetermine L-SR versus G-full, but the "
                "reflector's record split, boost covariance, reunion count, and "
                "moving-laboratory round trip separate them. G-full "
                "delay-only fails those Lorentz targets. A G-gated "
                "Lorentz-ether completion can repair them only with additional "
                "motion-dependent clock and rod dynamics."
            ),
            "grade": (
                "EXACT FINITE DISCRIMINATOR / G-FULL DELAY-ONLY OVERTURNED / "
                "L-SR KINEMATICS CONDITIONAL / G-GATED RESCUE CONSTRUCTED"
            ),
            "admission": "CONDITIONAL_CANDIDATE",
            "remaining_uncertainty": (
                "Neither local cadence nor a global update clock selects its "
                "signal law, derives the Lorentz factor, supplies a metric or "
                "dimensional c, extends to gravity, or identifies a DU record."
            ),
            "checks": checks,
        },
    }

    payload = {
        "probe": "du_record_rate_orthodox_clock_tournament",
        "contested_proposition": (
            "G-full, with every apparent difference caused only by message "
            "latency, can reproduce reciprocal Lorentz exchange, boost "
            "invariance, and unequal reunion elapsed times without an "
            "additional motion-dependent record mechanism."
        ),
        "definitions": {
            "local_record_count": (
                "irreversible physical counter carried by one observer"
            ),
            "global_update_count": (
                "Branch-G substrate index K shared across preferred slices"
            ),
            "message": (
                "limiting-signal send/reflection/receipt edge carrying the "
                "reflector's local count"
            ),
            "radar_time": "(n_s+n_r)/2 under Einstein synchronization",
            "radar_distance": "(n_r-n_s)/2 in declared record-tick units",
            "proper_time_target": (
                "path-dependent elapsed physical-clock record count in L-SR; "
                "not derived from cadence alone"
            ),
        },
        "echo_fixtures": strip_exact(echoes),
        "synchronization_null": reslicing,
        "boost_and_preferred_frame": strip_exact(boost_tests),
        "reunion_and_light_clock": strip_exact(reunion),
        "checks": checks,
        "checks_passed": passed,
        "checks_total": len(checks),
        "verdict": (
            "G-FULL DELAY-ONLY OVERTURNED AT THE CONVENTIONAL LORENTZ "
            "BENCHMARK / L-SR CONDITIONALLY RECONSTRUCTS KINEMATICS / "
            "G-GATED LORENTZ-ETHER RESCUE REMAINS LIVE BUT ADDS DYNAMICS"
        ),
        "scope": {
            "earned": [
                "an exact observer-message discriminator beyond A-only radar",
                "an exact delay-only and zero-delay reunion control",
                "an exact preferred-frame leakage fixture for G-full's split records",
                "a constructive finite G-gated rescue",
            ],
            "not_earned": [
                "a derivation of the reciprocal signal law or Lorentz factor",
                "a global no-go on hidden-clock or emergent-Lorentz theories",
                "a dimensional invariant speed",
                "gravity, a DU observer ontology, Lambda, or cosmology",
            ],
        },
    }

    receipt = comparison_receipt(candidate)
    if receipt["contract_status"] != "COMPLETE":
        raise RuntimeError(
            f"incomplete candidate contract: {receipt['contract_errors']}"
        )
    write_candidate_artifact(ARTIFACT_PATH, candidate, payload)

    print("ORTHODOX DUAL RECORD-CLOCK TOURNAMENT")
    for check in checks:
        print(f"{'PASS' if check['pass'] else 'FAIL'}  {check['name']}")
    print(f"{passed}/{len(checks)} checks pass")
    print(
        "VERDICT: G-FULL DELAY-ONLY OVERTURNED / "
        "L-SR CONDITIONAL / G-GATED RESCUE LIVE"
    )
    print(f"contract: {receipt['contract_status']} (not scientific endorsement)")
    print(f"artifact: {ARTIFACT_PATH}")
    if passed != len(checks):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
