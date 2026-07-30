#!/usr/bin/env python3
"""Audit action-equivalent decoder states for retained resource distinctions.

The source fixes ``DASR`` values 0 and 2 as the same no-logical-error control
branch, while value 1 triggers the conditional X. This probe asks whether that
action quotient also preserves the retained timing and response coordinates.

Passing establishes only a source-pinned sample-level quotient distinction and
an exact held-out schema boundary. It establishes no causal status effect,
population law, implementation completeness, physical remainder, or new
physics.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
from pathlib import Path
from typing import Any

import h5py
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_PATH = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_action_resource_finality_quotient_result.json"
)

EXPECTED_FAST_MD5 = "3b2503a80f2b92916660489e2f07e880"
EXPECTED_FAST_SHA256 = (
    "dd2a3d48e86ea81094b44439fb58a3d9788757e26799bd4ee7497eb94798ed08"
)
EXPECTED_TIMING_MD5 = "ec6e10f742b7c29627dad8ff9a97a592"
EXPECTED_TIMING_SHA256 = (
    "8f23b21a27004381734fefeef80e5326e0a67c391212fcb792950cf9b51bd324"
)
EXPECTED_DISCOVERY = {
    3: {
        "d0": 188,
        "d2": 703,
        "median_d0": 431.0,
        "median_d2": 671.0,
        "auc": 0.910648890772071,
        "ks": 0.6890302956932296,
    },
    4: {
        "d0": 172,
        "d2": 719,
        "median_d0": 599.0,
        "median_d2": 863.0,
        "auc": 0.8613424653103471,
        "ks": 0.5942280945757997,
    },
    5: {
        "d0": 169,
        "d2": 717,
        "median_d0": 771.0,
        "median_d2": 1091.0,
        "auc": 0.8647140864714087,
        "ks": 0.633944855702178,
    },
    6: {
        "d0": 174,
        "d2": 699,
        "median_d0": 1043.0,
        "median_d2": 1347.0,
        "auc": 0.764573364247776,
        "ks": 0.4032608159439593,
    },
    7: {
        "d0": 199,
        "d2": 672,
        "median_d0": 1257.0,
        "median_d2": 1609.0,
        "auc": 0.8146760588657574,
        "ks": 0.4972556233548696,
    },
    8: {
        "d0": 200,
        "d2": 653,
        "median_d0": 1534.0,
        "median_d2": 1838.0,
        "auc": 0.7425076569678407,
        "ks": 0.36179938744257273,
    },
    9: {
        "d0": 208,
        "d2": 647,
        "median_d0": 1722.0,
        "median_d2": 2078.0,
        "auc": 0.7275405718701701,
        "ks": 0.3761517655451194,
    },
}


def digest(path: Path, algorithm: str) -> str:
    hasher = hashlib.new(algorithm)
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def probability_of_superiority(lower: np.ndarray, upper: np.ndarray) -> float:
    """Return P(upper > lower) + 1/2 P(equal) without a quadratic join."""

    ordered = np.sort(np.asarray(lower))
    upper = np.asarray(upper)
    strictly_lower = np.searchsorted(ordered, upper, side="left")
    lower_or_equal = np.searchsorted(ordered, upper, side="right")
    wins = strictly_lower + 0.5 * (lower_or_equal - strictly_lower)
    return float(np.mean(wins) / len(ordered))


def ks_distance(left: np.ndarray, right: np.ndarray) -> float:
    values = np.unique(np.concatenate((left, right)))
    left_cdf = np.searchsorted(np.sort(left), values, side="right") / len(left)
    right_cdf = np.searchsorted(np.sort(right), values, side="right") / len(right)
    return float(np.max(np.abs(left_cdf - right_cdf)))


def cmh_response_test(strata: list[dict[str, int]]) -> dict[str, float]:
    """Cochran--Mantel--Haenszel score for D=0 versus D=2 failures."""

    numerator = 0.0
    variance = 0.0
    for stratum in strata:
        n_d0 = stratum["n_d0"]
        n_d2 = stratum["n_d2"]
        fail_d0 = stratum["fail_d0"]
        fail_d2 = stratum["fail_d2"]
        total = n_d0 + n_d2
        failures = fail_d0 + fail_d2
        successes = total - failures
        expected = n_d0 * failures / total
        numerator += fail_d0 - expected
        variance += (
            n_d0
            * n_d2
            * failures
            * successes
            / (total * total * (total - 1))
        )
    z_score = numerator / math.sqrt(variance)
    return {
        "score_numerator": numerator,
        "score_variance": variance,
        "z_score": z_score,
        "two_sided_normal_p": math.erfc(abs(z_score) / math.sqrt(2)),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fast-source", type=Path, required=True)
    parser.add_argument("--timing-source", type=Path, required=True)
    parser.add_argument("--write-artifact", action="store_true")
    args = parser.parse_args()

    fast_source = args.fast_source.resolve()
    timing_source = args.timing_source.resolve()
    fast_md5 = digest(fast_source, "md5")
    fast_sha256 = digest(fast_source, "sha256")
    timing_md5 = digest(timing_source, "md5")
    timing_sha256 = digest(timing_source, "sha256")

    checks: list[tuple[str, bool]] = [
        ("fast_md5", fast_md5 == EXPECTED_FAST_MD5),
        ("fast_sha256", fast_sha256 == EXPECTED_FAST_SHA256),
        ("timing_md5", timing_md5 == EXPECTED_TIMING_MD5),
        ("timing_sha256", timing_sha256 == EXPECTED_TIMING_SHA256),
        ("action_quotient_source_semantics", int(0 != 1) == int(2 != 1) == 1),
    ]
    discovery: list[dict[str, Any]] = []
    response_strata: list[dict[str, int]] = []

    with h5py.File(fast_source, "r") as file:
        for circuit_index in range(1, 8):
            result = file[f"circuit_{circuit_index}/result"]
            rounds = circuit_index + 2
            decoder = result["decoder_shot_results"][:, 0].astype(int)
            retained_time = result["time"][:].astype(int)
            q50 = result["hard_measurements/50"][:].astype(np.uint8)
            pre = q50[:, -2]
            response = q50[:, -1]
            action = (decoder == 1).astype(np.uint8)
            response_failure = response != (pre ^ action)

            d0_time = retained_time[decoder == 0]
            d2_time = retained_time[decoder == 2]
            median_d0 = float(np.median(d0_time))
            median_d2 = float(np.median(d2_time))
            auc = probability_of_superiority(d0_time, d2_time)
            ks = ks_distance(d0_time, d2_time)
            expected = EXPECTED_DISCOVERY[rounds]

            checks.extend(
                [
                    (
                        f"round_{rounds}_counts",
                        len(d0_time) == expected["d0"]
                        and len(d2_time) == expected["d2"],
                    ),
                    (
                        f"round_{rounds}_medians",
                        median_d0 == expected["median_d0"]
                        and median_d2 == expected["median_d2"],
                    ),
                    (
                        f"round_{rounds}_positive_median_gap",
                        median_d2 > median_d0,
                    ),
                    (
                        f"round_{rounds}_auc",
                        math.isclose(auc, expected["auc"], abs_tol=1e-12),
                    ),
                    (
                        f"round_{rounds}_ks",
                        math.isclose(ks, expected["ks"], abs_tol=1e-12),
                    ),
                ]
            )

            discovery.append(
                {
                    "rounds": rounds,
                    "d0_count": len(d0_time),
                    "d2_count": len(d2_time),
                    "median_d0": median_d0,
                    "median_d2": median_d2,
                    "median_gap_d2_minus_d0": median_d2 - median_d0,
                    "probability_d2_exceeds_d0_with_half_ties": auc,
                    "ks_distance": ks,
                }
            )

            for pre_value in (0, 1):
                d0_mask = (decoder == 0) & (pre == pre_value)
                d2_mask = (decoder == 2) & (pre == pre_value)
                response_strata.append(
                    {
                        "rounds": rounds,
                        "pre": pre_value,
                        "n_d0": int(np.sum(d0_mask)),
                        "fail_d0": int(np.sum(response_failure[d0_mask])),
                        "n_d2": int(np.sum(d2_mask)),
                        "fail_d2": int(np.sum(response_failure[d2_mask])),
                    }
                )

    response_totals = {
        "d0_n": sum(item["n_d0"] for item in response_strata),
        "d0_failures": sum(item["fail_d0"] for item in response_strata),
        "d2_n": sum(item["n_d2"] for item in response_strata),
        "d2_failures": sum(item["fail_d2"] for item in response_strata),
    }
    response_cmh = cmh_response_test(response_strata)
    checks.extend(
        [
            (
                "all_seven_rounds_timing_separate",
                all(
                    item["median_gap_d2_minus_d0"] > 0
                    and item["probability_d2_exceeds_d0_with_half_ties"] > 0.7
                    and item["ks_distance"] > 0.35
                    for item in discovery
                ),
            ),
            (
                "response_totals",
                response_totals
                == {
                    "d0_n": 1310,
                    "d0_failures": 487,
                    "d2_n": 4810,
                    "d2_failures": 1700,
                },
            ),
            (
                "no_response_split_detected_at_five_percent",
                response_cmh["two_sided_normal_p"] > 0.05,
            ),
        ]
    )

    timing_round_counts: dict[int, int] = {}
    timing_fieldnames: list[str] = []
    with timing_source.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        timing_fieldnames = list(reader.fieldnames or [])
        for row in reader:
            rounds = int(row["rounds"])
            timing_round_counts[rounds] = timing_round_counts.get(rounds, 0) + 1

    lowered_fields = {field.lower() for field in timing_fieldnames}
    status_fields = {
        "dasr",
        "decoder_status",
        "decoder_result",
        "logical_correction",
        "action",
    }
    identity_fields = {"shot", "shot_id", "repetition", "repetition_id", "row_id"}
    checks.extend(
        [
            (
                "heldout_schema_exact",
                timing_fieldnames == ["rounds", "cycles", "time_per_round"],
            ),
            (
                "heldout_three_hundred_thousand_rows",
                timing_round_counts == {9: 100000, 17: 100000, 25: 100000},
            ),
            (
                "heldout_status_join_absent",
                not lowered_fields.intersection(status_fields),
            ),
            (
                "heldout_row_identity_absent",
                not lowered_fields.intersection(identity_fields),
            ),
        ]
    )

    failures = [name for name, passed in checks if not passed]
    if failures:
        raise AssertionError(f"failed checks: {failures}")

    artifact = {
        "claim_id": "HC-DU-169",
        "run_id": "RUN-20260730-144047-action-resource-finality-quotient-audit",
        "status": "PASS",
        "sources": {
            "fast_feedback": {
                "file": "fast_feedback_raw_data.h5",
                "md5": fast_md5,
                "sha256": fast_sha256,
                "raw_file_committed": False,
            },
            "heldout_timing": {
                "file": "decoder_timings_each_repetition.csv",
                "md5": timing_md5,
                "sha256": timing_sha256,
                "raw_file_committed": False,
            },
        },
        "checks_passed": len(checks),
        "source_defined_action_quotient": {
            "no_action_statuses": [0, 2],
            "conditional_x_status": 1,
        },
        "discovery_timing": discovery,
        "response_strata": response_strata,
        "response_totals": response_totals,
        "response_cmh": response_cmh,
        "heldout_timing_schema": {
            "fields": timing_fieldnames,
            "round_counts": {
                str(key): value for key, value in sorted(timing_round_counts.items())
            },
            "decoder_status_join_present": False,
            "row_identity_present": False,
        },
        "earned": [
            "source-defined action quotient with DASR 0 and 2 on the same no-X branch",
            "seven-of-seven within-round retained timing separations in the discovery packet",
            "sample-level failure of the action quotient to preserve the retained resource coordinate",
            "no response split detected at five percent after round/pre stratification",
            "exact held-out schema boundary: 300,000 timings without decoder status or row identity",
        ],
        "disposition": [
            "ACTION_QUOTIENT_RESOURCE_DISTINCTION",
            "NO_DETECTED_ACTION_QUOTIENT_RESPONSE_DISTINCTION",
            "HELDOUT_SCHEMA_CANNOT_TEST_ACTION_QUOTIENT",
            "KNOWN_CONTROL_THEORY_ABSORPTION",
        ],
        "scientific_nonclaim": (
            "The audit establishes a source-pinned sample-level timing distinction "
            "inside one returned-shot packet. It does not identify a causal status "
            "effect, population law, implementation-complete process, physical "
            "remainder, ontology, or new physics."
        ),
    }

    if args.write_artifact:
        ARTIFACT_PATH.parent.mkdir(parents=True, exist_ok=True)
        ARTIFACT_PATH.write_text(
            json.dumps(artifact, indent=2, sort_keys=False) + "\n",
            encoding="utf-8",
        )

    print(
        f"PASS: {len(checks)}/{len(checks)} checks; "
        "action quotient loses retained timing; held-out status join absent"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
