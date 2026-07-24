#!/usr/bin/env python3
"""Commercial dual-record-clock decision probe.

This probe compares two admitted conditional architectures:

* Branch L: each observer carries a local primitive record cadence.  For the
  special-relativistic benchmark only, record count is conditionally mapped
  to elapsed proper time.
* Branch G: one actual global update count ``K`` pushes record addition for
  every observer.  ``G-full`` adds one record per observer per global tick;
  ``G-gated`` adds an extra local admission law.

The smallest useful discriminators are exact:

1. A separated echo can create a raw clock offset that disappears when the
   known propagation delay is removed.
2. Radar distance makes ``c=1`` by construction.  Message records identify
   only distance/speed until an independent distance and tick calibration are
   supplied.
3. At a reunion, propagation delay is zero.  ``G-full`` predicts equal counts,
   while the declared SR-compatible Branch-L completion predicts unequal
   proper-time counts.
4. A preferred-frame, delay-only ``G-full`` propagation model predicts a
   closed-loop orientation effect.  A ``G-gated`` completion can cancel it,
   but only by adding the Lorentz gate and length-response laws that the
   delay-only premise did not contain.
5. A Clock-QCA-like discrete global evolution is retained as a positive
   literature control: exact discrete Lorentz covariance is possible in a
   particular 1+1 construction, so the narrow ``G-full`` failure must not be
   generalized to every globally updated discrete model.

The calculation is a conditional kinematic and identifiability assay.  It
does not derive special relativity, a microscopic record ontology, gravity,
or the dimensional value of the speed of light.
"""

from __future__ import annotations

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
    / "du_record_rate_commercial_delay_reunion_probe_result.json"
)


def fraction_text(value: Fraction) -> str:
    """Return a deterministic exact representation."""

    return f"{value.numerator}/{value.denominator}"


def radar_and_synchronization_fixture() -> dict[str, Any]:
    """Expose what a two-way message record defines and what it cannot."""

    send_count = Fraction(20)
    receive_count = Fraction(36)
    reflection_count = Fraction(28)
    round_trip = receive_count - send_count
    radar_time = (send_count + receive_count) / 2
    radar_distance = round_trip / 2
    radar_speed = radar_distance / (round_trip / 2)

    synchronization_rows = []
    for epsilon in (Fraction(-3), Fraction(0), Fraction(3)):
        forward_latency = radar_distance + epsilon
        return_latency = radar_distance - epsilon
        synchronization_rows.append(
            {
                "epsilon": fraction_text(epsilon),
                "forward_latency": fraction_text(forward_latency),
                "return_latency": fraction_text(return_latency),
                "forward_one_way_speed": fraction_text(
                    radar_distance / forward_latency
                ),
                "return_one_way_speed": fraction_text(
                    radar_distance / return_latency
                ),
                "round_trip_latency": fraction_text(
                    forward_latency + return_latency
                ),
                "two_way_speed": fraction_text(
                    2 * radar_distance
                    / (forward_latency + return_latency)
                ),
            }
        )

    scale_gauge = []
    for distance, speed in (
        (Fraction(8), Fraction(1)),
        (Fraction(24), Fraction(3)),
        (Fraction(40), Fraction(5)),
    ):
        scale_gauge.append(
            {
                "distance": fraction_text(distance),
                "speed": fraction_text(speed),
                "one_way_latency": fraction_text(distance / speed),
                "round_trip_latency": fraction_text(2 * distance / speed),
            }
        )

    independent_distance = Fraction(24)
    tick_duration = Fraction(1)
    independently_recovered_two_way_speed = (
        2 * independent_distance / (round_trip * tick_duration)
    )

    return {
        "records": {
            "A_send_count": fraction_text(send_count),
            "B_reflection_count": fraction_text(reflection_count),
            "A_receive_count": fraction_text(receive_count),
        },
        "constructed_radar_time": fraction_text(radar_time),
        "constructed_radar_distance_in_record_ticks": fraction_text(
            radar_distance
        ),
        "radar_speed_by_definition": fraction_text(radar_speed),
        "synchronization_reslicings": synchronization_rows,
        "distance_speed_scale_gauge": scale_gauge,
        "independent_calibration": {
            "independent_spatial_distance": fraction_text(
                independent_distance
            ),
            "record_tick_duration": fraction_text(tick_duration),
            "recovered_two_way_speed": fraction_text(
                independently_recovered_two_way_speed
            ),
            "reading": (
                "The dimensional speed is recovered only after an independent "
                "distance and tick-duration calibration. Radar c=1 alone is "
                "an operational convention."
            ),
        },
    }


def propagation_correction_fixture() -> dict[str, Any]:
    """Show that a delay-only separated-clock offset is removable."""

    global_send = Fraction(20)
    forward_latency = Fraction(5)
    return_latency = Fraction(11)
    remote_reply_count = global_send + forward_latency
    local_receive_count = (
        global_send + forward_latency + return_latency
    )
    raw_remote_minus_local = remote_reply_count - local_receive_count
    propagation_corrected_remote_count = (
        remote_reply_count + return_latency
    )
    corrected_remote_minus_local = (
        propagation_corrected_remote_count - local_receive_count
    )

    return {
        "global_send_count": fraction_text(global_send),
        "forward_latency": fraction_text(forward_latency),
        "return_latency": fraction_text(return_latency),
        "remote_reply_count_carried_by_message": fraction_text(
            remote_reply_count
        ),
        "local_count_on_receipt": fraction_text(local_receive_count),
        "raw_remote_minus_local": fraction_text(raw_remote_minus_local),
        "propagation_corrected_remote_count": fraction_text(
            propagation_corrected_remote_count
        ),
        "corrected_remote_minus_local": fraction_text(
            corrected_remote_minus_local
        ),
        "reading": (
            "The raw separated-clock offset equals the return latency and "
            "vanishes when that latency is exactly propagated forward."
        ),
    }


def reunion_fixture() -> dict[str, Any]:
    """Compare G-full with an SR-compatible Branch-L completion."""

    global_ticks = Fraction(100)
    beta = Fraction(3, 5)
    inverse_gamma = Fraction(4, 5)
    gamma = Fraction(5, 4)

    g_full_A = global_ticks
    g_full_B = global_ticks

    branch_l_A = global_ticks
    branch_l_B = global_ticks * inverse_gamma
    branch_l_difference = branch_l_A - branch_l_B

    g_gated_A = global_ticks
    g_gated_B = global_ticks * inverse_gamma

    return {
        "fixture": (
            "A and B share departure E0 and reunion E1. A is at rest in the "
            "benchmark frame; B has two equal inertial legs at |beta|=3/5 "
            "with an idealized turnaround."
        ),
        "global_ticks_between_shared_endpoints": fraction_text(global_ticks),
        "beta": fraction_text(beta),
        "gamma": fraction_text(gamma),
        "inverse_gamma": fraction_text(inverse_gamma),
        "G_full": {
            "A_records": fraction_text(g_full_A),
            "B_records": fraction_text(g_full_B),
            "A_minus_B": fraction_text(g_full_A - g_full_B),
            "prediction": "equal reunited counts",
        },
        "L_with_SR_proper_time_map": {
            "A_records": fraction_text(branch_l_A),
            "B_records": fraction_text(branch_l_B),
            "A_minus_B": fraction_text(branch_l_difference),
            "prediction": (
                "path-dependent reunited counts under the conditional "
                "N_i=proper_time_i/delta_tau map"
            ),
        },
        "G_gated_minimum_completion": {
            "A_records": fraction_text(g_gated_A),
            "B_records": fraction_text(g_gated_B),
            "A_minus_B": fraction_text(g_gated_A - g_gated_B),
            "required_gate_for_B": fraction_text(inverse_gamma),
            "extra_law": (
                "admit records at dN/dK=sqrt(1-beta^2) for the moving "
                "observer in the preferred-clock description"
            ),
        },
        "delay_only_null": (
            "No send/receive latency exists at E0 or E1. Resynchronization "
            "and propagation correction cannot alter either stored count."
        ),
    }


def preferred_frame_fixture() -> dict[str, Any]:
    """Expose the preferred-frame price of a pure global-delay model."""

    c = Fraction(1)
    beta = Fraction(3, 5)
    arm_length = Fraction(8)
    inverse_gamma = Fraction(4, 5)

    stationary_round_trip = 2 * arm_length / c
    parallel_outbound = arm_length / (c - beta)
    parallel_return = arm_length / (c + beta)
    parallel_round_trip = parallel_outbound + parallel_return
    transverse_round_trip = 2 * arm_length / inverse_gamma

    contracted_parallel_length = arm_length * inverse_gamma
    gated_parallel_global_ticks = (
        2 * contracted_parallel_length / (1 - beta * beta)
    )
    gated_transverse_global_ticks = transverse_round_trip
    gated_parallel_records = gated_parallel_global_ticks * inverse_gamma
    gated_transverse_records = (
        gated_transverse_global_ticks * inverse_gamma
    )

    return {
        "parameters": {
            "preferred_frame_signal_speed": fraction_text(c),
            "apparatus_speed_beta": fraction_text(beta),
            "rest_arm_length": fraction_text(arm_length),
        },
        "G_full_delay_only_no_contraction": {
            "stationary_round_trip_records": fraction_text(
                stationary_round_trip
            ),
            "parallel_outbound_records": fraction_text(parallel_outbound),
            "parallel_return_records": fraction_text(parallel_return),
            "parallel_round_trip_records": fraction_text(
                parallel_round_trip
            ),
            "transverse_round_trip_records": fraction_text(
                transverse_round_trip
            ),
            "parallel_to_transverse_ratio": fraction_text(
                parallel_round_trip / transverse_round_trip
            ),
            "preferred_frame_signal": (
                "The two-way closed-loop count depends on orientation and "
                "absolute apparatus speed."
            ),
        },
        "G_gated_Lorentz_completion": {
            "parallel_length_in_preferred_frame": fraction_text(
                contracted_parallel_length
            ),
            "parallel_global_ticks": fraction_text(
                gated_parallel_global_ticks
            ),
            "transverse_global_ticks": fraction_text(
                gated_transverse_global_ticks
            ),
            "parallel_local_records": fraction_text(
                gated_parallel_records
            ),
            "transverse_local_records": fraction_text(
                gated_transverse_records
            ),
            "reading": (
                "Length response sqrt(1-beta^2) plus the same record-admission "
                "gate cancels the preferred-frame signal on this fixture. "
                "Those are additional dynamical laws, not propagation delay."
            ),
        },
    }


def positive_global_clock_control() -> dict[str, Any]:
    """Record the scoped primary-source control without claiming replication."""

    return {
        "source": (
            "P. Arrighi, S. Facchini, and M. Forets, Discrete Lorentz "
            "covariance for Quantum Walks and Quantum Cellular Automata "
            "(2014), arXiv:1404.4499"
        ),
        "url": "https://arxiv.org/abs/1404.4499",
        "positive_result": (
            "The Clock QW and Clock QCA are proved exactly discrete Lorentz "
            "covariant in 1+1 dimensions; the Clock QCA uses a fixed "
            "three-dimensional wire state space."
        ),
        "covariance_scope": (
            "A solution is mapped to a solution of the same discrete "
            "dynamics through construction-specific encodings that replace "
            "lattice points by lightlike rectangular patches. Rational "
            "velocities require a global rescaling."
        ),
        "commercial_reading": (
            "This is a positive control for G-gated or gauge-hidden global "
            "discrete updating, not evidence for G-full latency-only record "
            "addition."
        ),
        "not_established": [
            "a primitive append-only record ontology",
            "one equivalent observer record per global update",
            "a reunion record-count admission law",
            "generic model-independent Lorentz covariance",
            "3+1 dimensional isotropy, interactions, gravity, or a dimensional c",
        ],
        "local_replication_status": "LITERATURE_CONTROL_NOT_RECOMPUTED",
    }


def main() -> None:
    radar = radar_and_synchronization_fixture()
    propagation = propagation_correction_fixture()
    reunion = reunion_fixture()
    frame = preferred_frame_fixture()
    positive_control = positive_global_clock_control()

    reslicings = radar["synchronization_reslicings"]
    scale_rows = radar["distance_speed_scale_gauge"]
    checks = [
        {
            "name": "radar time and radar distance are constructed exactly from local send and receive counts",
            "pass": (
                radar["constructed_radar_time"] == "28/1"
                and radar[
                    "constructed_radar_distance_in_record_ticks"
                ]
                == "8/1"
            ),
        },
        {
            "name": "radar c equals one by definition on the declared record-tick units",
            "pass": radar["radar_speed_by_definition"] == "1/1",
        },
        {
            "name": "synchronization reslicing changes one-way speeds while preserving the two-way result",
            "pass": (
                len(
                    {
                        row["forward_one_way_speed"]
                        for row in reslicings
                    }
                )
                == 3
                and {
                    row["round_trip_latency"] for row in reslicings
                }
                == {"16/1"}
                and {row["two_way_speed"] for row in reslicings}
                == {"1/1"}
            ),
        },
        {
            "name": "message records alone identify distance over speed rather than dimensional distance and speed separately",
            "pass": (
                {row["one_way_latency"] for row in scale_rows}
                == {"8/1"}
                and {row["round_trip_latency"] for row in scale_rows}
                == {"16/1"}
            ),
        },
        {
            "name": "an independent distance and tick calibration produces a nondefinitional dimensional two-way speed",
            "pass": (
                radar["independent_calibration"][
                    "recovered_two_way_speed"
                ]
                == "3/1"
            ),
        },
        {
            "name": "exact propagation correction removes the separated-clock delay-only offset",
            "pass": (
                propagation["raw_remote_minus_local"] == "-11/1"
                and propagation["corrected_remote_minus_local"] == "0/1"
            ),
        },
        {
            "name": "G-full predicts equal record accumulation between shared reunion endpoints",
            "pass": reunion["G_full"]["A_minus_B"] == "0/1",
        },
        {
            "name": "the declared SR-compatible Branch-L completion predicts a path-dependent reunion difference",
            "pass": (
                reunion["L_with_SR_proper_time_map"]["A_minus_B"]
                == "20/1"
            ),
        },
        {
            "name": "G-gated reproduces the reunion difference only by adding the Lorentz admission factor",
            "pass": (
                reunion["G_gated_minimum_completion"]["A_minus_B"]
                == "20/1"
                and reunion["G_gated_minimum_completion"][
                    "required_gate_for_B"
                ]
                == "4/5"
            ),
        },
        {
            "name": "pure preferred-frame G-full propagation predicts a closed-loop orientation signal",
            "pass": (
                frame["G_full_delay_only_no_contraction"][
                    "parallel_to_transverse_ratio"
                ]
                == "5/4"
            ),
        },
        {
            "name": "the Lorentz-gated global completion hides this signal only after adding matching clock and length laws",
            "pass": (
                frame["G_gated_Lorentz_completion"][
                    "parallel_local_records"
                ]
                == "16/1"
                and frame["G_gated_Lorentz_completion"][
                    "transverse_local_records"
                ]
                == "16/1"
            ),
        },
    ]
    passed = sum(bool(check["pass"]) for check in checks)

    candidate = {
        "schema_version": SCHEMA_VERSION,
        "candidate_id": "DU-COMMERCIAL-DUAL-RECORD-CLOCK-DECISION",
        "track": (
            "Science Council commercial primitive-record-rate wave / "
            "Branch L versus Branch G"
        ),
        "question": (
            "What is the minimum operational product that distinguishes a "
            "universal local cadence from one global record clock, removes "
            "signal delay as an explanation of elapsed-time differences, "
            "and separates radar-defined c from independently recovered c?"
        ),
        "warrants": [
            "DERIVED",
            "CONDITIONALLY_ENTAILED",
            "CONSTRUCTIVELY_REALIZED",
            "ABDUCTIVELY_PREFERRED",
        ],
        "assumptions": [
            {
                "id": "A1",
                "statement": (
                    "Branch L supplies local append-only record sequences "
                    "without a shared synchronization; for the SR benchmark "
                    "only, N_i=proper_time_i/delta_tau is a conditional map."
                ),
                "status": "CONDITIONAL_POSIT",
                "role": (
                    "Defines the strongest local-cadence completion used in "
                    "the reunion comparison without claiming proper time was "
                    "derived."
                ),
            },
            {
                "id": "A2",
                "statement": (
                    "Branch G-full supplies one actual global update count K "
                    "and every observer appends exactly one equivalent record "
                    "per K tick."
                ),
                "status": "CONDITIONAL_POSIT",
                "role": (
                    "Makes the user's global-clock premise predictively sharp "
                    "rather than rejecting it by definition."
                ),
            },
            {
                "id": "A3",
                "statement": (
                    "Messages traverse the finite fixture with declared "
                    "one-way latencies; the preferred-frame null uses one "
                    "spatial unit per global tick."
                ),
                "status": "CONDITIONAL_POSIT",
                "role": (
                    "Constructs delay-only offsets and exposes the preferred "
                    "frame of the simplest G-full propagation completion."
                ),
            },
            {
                "id": "A4",
                "statement": (
                    "A dimensional speed is evaluated only when spatial "
                    "distance and record-tick duration are independently "
                    "calibrated."
                ),
                "status": "STANDARD",
                "role": (
                    "Prevents radar distance from defining and then appearing "
                    "to predict the same signal speed."
                ),
            },
        ],
        "free_choices": [
            {
                "id": "C1",
                "choice": (
                    "Use exact counts (20,28,36), including asymmetric "
                    "one-way latencies 5 and 11."
                ),
                "why_not_forced": "They are minimal arithmetic fixtures.",
                "sensitivity_test": (
                    "Use three synchronization reslicings while preserving "
                    "the same round-trip latency."
                ),
            },
            {
                "id": "C2",
                "choice": (
                    "Use a reunion benchmark with beta=3/5 and 100 global "
                    "ticks."
                ),
                "why_not_forced": (
                    "The rational values make gamma=5/4 exact; the formulas "
                    "hold for every nonzero subluminal beta."
                ),
                "sensitivity_test": (
                    "Require the exact symbolic distinction G-full: deltaN=0 "
                    "versus L+SR: deltaN=T(1-sqrt(1-beta^2))."
                ),
            },
            {
                "id": "C3",
                "choice": (
                    "Use an eight-unit two-arm closed-loop fixture in the "
                    "preferred-frame control."
                ),
                "why_not_forced": (
                    "It is the smallest exact orientation comparison with "
                    "the same beta=3/5."
                ),
                "sensitivity_test": (
                    "Compare pure delay-only G-full with the explicit "
                    "Lorentz-gated and length-responsive completion."
                ),
            },
        ],
        "equations": [
            "radar_time=(n_send+n_receive)/2",
            "radar_distance=(n_receive-n_send)/2",
            "(D,c)->(aD,ac) leaves message latency D/c unchanged",
            "G-full reunion: Delta N_A=Delta N_B=Delta K",
            "L+SR reunion: Delta N_B=Delta N_A sqrt(1-beta^2)",
            "G-gated rescue: dN/dK=sqrt(1-beta^2)",
            "G-full preferred-frame parallel round trip=L/(1-beta)+L/(1+beta)",
            "G-full preferred-frame transverse round trip=2L/sqrt(1-beta^2)",
        ],
        "observables": [
            "raw and propagation-corrected separated-clock offset",
            "reunited local record-count difference",
            "round-trip count under synchronization reslicing",
            "closed-loop orientation anisotropy",
            "two-way speed after independent distance and tick calibration",
        ],
        "comparators": [
            "Branch L with an explicitly conditional SR proper-time map",
            "Branch G-full with exact one-record-per-global-tick addition",
            "Branch G-gated with a Lorentz-factor admission law",
            (
                "construction-specific Clock QW/QCA exact discrete Lorentz "
                "covariance in 1+1 as a literature positive control"
            ),
            "pure preferred-frame delay-only propagation",
            "synchronization-resliced and distance-speed-rescaled message logs",
        ],
        "null_models": [
            "asymmetric message latency whose apparent offset vanishes after exact propagation correction",
            "Einstein and non-Einstein synchronization reslicings of one round trip",
            "co-located departure and reunion endpoints with zero propagation delay",
            "a rotated closed-loop apparatus in the global-clock preferred frame",
        ],
        "falsifiers": [
            "G-full yields unequal equivalent record counts at reunion without a gate",
            "propagation correction changes stored reunited record counts",
            "radar c ceases to equal one when radar distance is defined from the same round trip",
            "message counts independently determine D and c despite the exact common-rescaling family",
            "pure preferred-frame propagation has no closed-loop orientation dependence",
            "G-gated recovers the SR fixture without a velocity/path/field-dependent admission or length law",
        ],
        "stop_conditions": [
            "Stop using separated remote timestamp offsets as evidence once exact propagation correction removes them.",
            "Stop claiming physical c from radar c=1 until an independent distance or metric map exists.",
            "Stop G-full as a model of relativistic elapsed time if equivalent reunited records differ.",
            "Keep G-gated open only with an independently generated admission law and a preferred-frame audit.",
            (
                "Do not generalize the G-full delay-only failure to every "
                "global discrete clock: first compare against the exact 1+1 "
                "Clock-QCA positive control and preserve its limited scope."
            ),
            "If fundamental records cannot be read or compared at reunion, mark the L/G physical comparison NOT_EVALUABLE rather than expanding ontology.",
            "Do not claim Branch L derives SR merely because one conditional proper-time map is compatible with it.",
        ],
        "concept": {
            "concept_id": "PRIMITIVE-RECORD-CLOCK-DUAL",
            "invariant": (
                "A physical record-clock proposal must make a propagation-"
                "corrected reunion or closed-loop prediction that is not "
                "created by synchronization convention."
            ),
            "formalization_id": "FORMALIZATION-COM-RR-DUAL-01",
            "failure_scope": "FORMALIZATION",
        },
        "result": {
            "claim": (
                "Separated message offsets do not discriminate the branches "
                "when propagation removes them. A reunion count is the "
                "minimum clean discriminator: G-full predicts equality, while "
                "an SR-compatible local-cadence completion predicts a "
                "path-dependent difference. G-gated can reproduce that "
                "difference only by adding the Lorentz admission law, and "
                "the simplest global-frame propagation model has a "
                "closed-loop orientation signal unless matching length and "
                "clock dynamics are added. This is a narrow failure of "
                "G-full latency-only, not of all global discrete evolution: "
                "the exact 1+1 Clock-QCA construction remains a positive "
                "control for a G-gated or gauge-hidden completion."
            ),
            "grade": (
                "EXACT CONDITIONAL DECISION ASSAY / G-FULL DELAY-ONLY "
                "INSUFFICIENT FOR REUNION TIME DILATION / G-GATED OR "
                "CLOCK-QCA-LIKE GLOBAL COMPLETIONS OPEN WITH SCOPED "
                "LORENTZ AND PREFERRED-FRAME BURDENS"
            ),
            "admission": "CONDITIONAL_CANDIDATE",
            "remaining_uncertainty": (
                "No microscopic observer/record law, Lorentz-factor "
                "derivation, independent physical distance map, gravity "
                "response, or empirical record-to-clock identity is supplied. "
                "The Clock-QCA antecedent has not been locally reproduced or "
                "extended from its construction-specific 1+1 covariance to "
                "the present reunion-record semantics."
            ),
            "checks": checks,
        },
    }
    receipt = comparison_receipt(candidate)
    if passed != len(checks):
        failed = [check["name"] for check in checks if not check["pass"]]
        raise AssertionError(f"failed checks: {failed}")
    if receipt["contract_status"] != "COMPLETE":
        raise AssertionError(receipt["contract_errors"])

    write_candidate_artifact(
        ARTIFACT_PATH,
        candidate,
        {
            "radar_and_synchronization": radar,
            "propagation_correction": propagation,
            "reunion": reunion,
            "preferred_frame": frame,
            "positive_global_clock_control": positive_control,
            "commercial_decision": {
                "minimum_product": (
                    "A co-located departure/reunion record-count comparison, "
                    "preceded by a propagation-corrected echo and followed "
                    "only if necessary by a closed-loop preferred-frame test."
                ),
                "G_full_disposition": (
                    "Useful exact delay null; insufficient as a relativistic "
                    "elapsed-time model."
                ),
                "G_gated_price": (
                    "First reproduce and reinterpret the Clock-QCA positive "
                    "control instead of fitting 1/gamma by hand. Then derive "
                    "the record admission and matching spatial response from "
                    "the substrate and show whether the global foliation is "
                    "observable across boosts and fields."
                ),
                "Branch_L_price": (
                    "Derive rather than assume the map from local record "
                    "count to proper time and the Lorentzian message cone."
                ),
                "c_price": (
                    "Supply independent spatial calibration or metric "
                    "reconstruction plus a tick-duration unit."
                ),
            },
            "checks_passed": passed,
            "checks_total": len(checks),
        },
    )
    print(
        "du_record_rate_commercial_delay_reunion_probe: "
        f"{passed}/{len(checks)} checks passed"
    )
    print(f"artifact: {ARTIFACT_PATH}")


if __name__ == "__main__":
    main()
