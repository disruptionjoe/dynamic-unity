#!/usr/bin/env python3
"""Audit the source-pinned Riverlane/Rigetti fast-feedback HDF5 packet.

Run through ``uv run --with h5py`` and pass the downloaded source explicitly.
Passing establishes joined returned-shot structure and its exact schema
boundary only. It establishes no all-attempt completeness, physical remainder,
new law, ontology, or empirical excess.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import h5py
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_PATH = (
    ROOT / "tests" / "artifacts" / "du_rigetti_fast_feedback_packet_result.json"
)

EXPECTED_MD5 = "3b2503a80f2b92916660489e2f07e880"
EXPECTED_SHA256 = "dd2a3d48e86ea81094b44439fb58a3d9788757e26799bd4ee7497eb94798ed08"
EXPECTED_RESPONSE_SUCCESSES = (746, 718, 703, 626, 617, 631, 583, 599)
EXPECTED_DASR_COUNTS = (
    {0: 502, 1: 498},
    {0: 188, 1: 109, 2: 703},
    {0: 172, 1: 109, 2: 719},
    {0: 169, 1: 114, 2: 717},
    {0: 174, 1: 127, 2: 699},
    {0: 199, 1: 129, 2: 672},
    {0: 200, 1: 147, 2: 653},
    {0: 208, 1: 145, 2: 647},
)


def digest(path: Path, algorithm: str) -> str:
    hasher = hashlib.new(algorithm)
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def scalar_text(dataset: h5py.Dataset) -> str:
    value = dataset[()]
    if isinstance(value, bytes):
        return value.decode("utf-8")
    return str(value)


def hard_history_key(group: h5py.Group, row: int) -> tuple[int, ...]:
    values: list[int] = []
    for qubit in sorted(group["hard_measurements"], key=int):
        measurement = group[f"hard_measurements/{qubit}"][row]
        if qubit == "50":
            measurement = measurement[:-1]
        values.extend(map(int, measurement))
    return tuple(values)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--write-artifact", action="store_true")
    args = parser.parse_args()

    source = args.source.resolve()
    checks: list[tuple[str, bool]] = []
    md5 = digest(source, "md5")
    sha256 = digest(source, "sha256")
    checks.extend(
        [
            ("official_md5_matches", md5 == EXPECTED_MD5),
            ("audited_sha256_matches", sha256 == EXPECTED_SHA256),
        ]
    )

    totals = {
        "returned_rows": 0,
        "hard_measurement_events": 0,
        "soft_measurement_events": 0,
        "decoder_rows": 0,
        "time_rows": 0,
        "repeated_hard_history_groups": 0,
        "repeated_hard_history_rows": 0,
        "decoder_conflict_groups": 0,
        "decoder_conflict_rows": 0,
    }
    circuits: list[dict[str, Any]] = []

    with h5py.File(source, "r") as file:
        expected_roots = {
            *(f"circuit_{index}" for index in range(8)),
            "reference_data",
            "session_data",
        }
        checks.append(("root_schema_exact", set(file) == expected_roots))
        checks.extend(
            [
                (
                    "session_description",
                    scalar_text(file["session_data/experiment_description"])
                    == "Stability-8 experiment with real-time FPGA decoding and conditional operation.",
                ),
                (
                    "session_qpu",
                    scalar_text(file["session_data/qpu_name"]) == "Ankaa-2",
                ),
                (
                    "session_timestamp_present",
                    scalar_text(file["session_data/utc_time"])
                    == "2024-07-17 17:30:20.406054",
                ),
            ]
        )

        all_schema_names: list[str] = []
        file.visit(all_schema_names.append)

        for circuit_index in range(8):
            circuit = file[f"circuit_{circuit_index}"]
            result = circuit["result"]
            rounds = int(result.attrs["rounds"])
            checks.extend(
                [
                    (f"circuit_{circuit_index}_rounds", rounds == circuit_index + 2),
                    (
                        f"circuit_{circuit_index}_conditional_qubit",
                        int(result.attrs["conditional_qubit"]) == 50,
                    ),
                    (
                        f"circuit_{circuit_index}_no_resets",
                        not bool(result.attrs["use_resets"]),
                    ),
                    (
                        f"circuit_{circuit_index}_returned_rows",
                        result["time"].shape == (1000,),
                    ),
                    (
                        f"circuit_{circuit_index}_decoder_rows",
                        result["decoder_shot_results"].shape[0] == 1000,
                    ),
                ]
            )

            hard = result["hard_measurements"]
            soft = result["soft_measurements"]
            qubits = sorted(hard, key=int)
            aligned = set(hard) == set(soft) and all(
                hard[qubit].shape == soft[qubit].shape
                and hard[qubit].shape[0] == 1000
                for qubit in qubits
            )
            checks.append((f"circuit_{circuit_index}_hard_soft_join", aligned))
            checks.append(
                (
                    f"circuit_{circuit_index}_q50_extra_response",
                    hard["50"].shape == (1000, rounds + 1),
                )
            )
            checks.append(
                (
                    f"circuit_{circuit_index}_complex_soft_values",
                    all(np.issubdtype(soft[qubit].dtype, np.complexfloating) for qubit in qubits),
                )
            )

            decoder = result["decoder_shot_results"][:, 0].astype(int)
            action = decoder == 1
            q50 = hard["50"][:].astype(np.uint8)
            pre_feedback = q50[:, -2]
            response = q50[:, -1]
            expected_response = pre_feedback ^ action.astype(np.uint8)
            response_successes = int(np.sum(response == expected_response))
            dasr_counts = dict(sorted(Counter(map(int, decoder)).items()))
            checks.extend(
                [
                    (
                        f"circuit_{circuit_index}_dasr_counts",
                        dasr_counts == EXPECTED_DASR_COUNTS[circuit_index],
                    ),
                    (
                        f"circuit_{circuit_index}_response_relation",
                        response_successes
                        == EXPECTED_RESPONSE_SUCCESSES[circuit_index],
                    ),
                    (
                        f"circuit_{circuit_index}_response_nonconstant",
                        set(map(int, response)) == {0, 1},
                    ),
                ]
            )

            histories = [
                hard_history_key(result, row) for row in range(result["time"].shape[0])
            ]
            history_counts = Counter(histories)
            decoder_by_history: defaultdict[tuple[int, ...], set[int]] = defaultdict(set)
            for history, decision in zip(histories, decoder, strict=True):
                decoder_by_history[history].add(int(decision))
            conflicts = {
                history
                for history, decisions in decoder_by_history.items()
                if len(decisions) > 1
            }

            repeated_groups = sum(count > 1 for count in history_counts.values())
            repeated_rows = sum(
                count for count in history_counts.values() if count > 1
            )
            conflict_rows = sum(history_counts[history] for history in conflicts)

            totals["returned_rows"] += 1000
            totals["decoder_rows"] += result["decoder_shot_results"].shape[0]
            totals["time_rows"] += result["time"].shape[0]
            totals["repeated_hard_history_groups"] += repeated_groups
            totals["repeated_hard_history_rows"] += repeated_rows
            totals["decoder_conflict_groups"] += len(conflicts)
            totals["decoder_conflict_rows"] += conflict_rows
            for qubit in qubits:
                totals["hard_measurement_events"] += hard[qubit].size
                totals["soft_measurement_events"] += soft[qubit].size

            circuits.append(
                {
                    "circuit": circuit_index,
                    "rounds": rounds,
                    "returned_rows": 1000,
                    "dasr_counts": {str(key): value for key, value in dasr_counts.items()},
                    "documented_branch_response_successes": response_successes,
                    "documented_branch_response_rate": response_successes / 1000,
                    "unique_hard_histories": len(history_counts),
                    "repeated_hard_history_groups": repeated_groups,
                    "repeated_hard_history_rows": repeated_rows,
                    "decoder_conflict_groups": len(conflicts),
                    "time_range": [
                        int(np.min(result["time"][:])),
                        int(np.max(result["time"][:])),
                    ],
                }
            )

        checks.extend(
            [
                ("eight_thousand_joined_rows", totals["returned_rows"] == 8000),
                (
                    "measurement_event_counts",
                    totals["hard_measurement_events"] == 216000
                    and totals["soft_measurement_events"] == 216000,
                ),
                (
                    "decoder_and_time_alignment",
                    totals["decoder_rows"] == totals["time_rows"] == 8000,
                ),
                (
                    "repeated_history_positive_control",
                    totals["repeated_hard_history_groups"] == 176
                    and totals["repeated_hard_history_rows"] == 389,
                ),
                (
                    "no_observed_decoder_conflict_on_repeats",
                    totals["decoder_conflict_groups"] == 0
                    and totals["decoder_conflict_rows"] == 0,
                ),
                (
                    "reference_group_counts",
                    len(file["reference_data/delays"]) == 13
                    and len(file["reference_data/measurement_fidelity"]) == 2
                    and len(file["reference_data/double_measurement"]) == 2,
                ),
                (
                    "reference_programs_retained",
                    all(
                        "program" in file[path]
                        for path in (
                            "reference_data/double_measurement/zeros",
                            "reference_data/double_measurement/ones",
                            "reference_data/measurement_fidelity/zeros",
                            "reference_data/measurement_fidelity/ones",
                        )
                    ),
                ),
                (
                    "main_hardware_program_not_retained",
                    all("program" not in file[f"circuit_{index}"] for index in range(8)),
                ),
            ]
        )

        schema_lower = "\n".join(all_schema_names).lower()
        absent_schema_terms = (
            "accepted",
            "rejected",
            "retry",
            "attempt_selector",
            "trigger_census",
            "controller_memory",
            "firmware",
            "route_state",
            "raw_waveform",
            "archive_policy",
        )
        checks.append(
            (
                "all_attempt_and_controller_schema_absent",
                all(term not in schema_lower for term in absent_schema_terms),
            )
        )

    failures = [name for name, passed in checks if not passed]
    if failures:
        raise AssertionError(f"failed checks: {failures}")

    artifact = {
        "claim_id": "HC-DU-168",
        "run_id": "RUN-20260730-142222-rigetti-fast-feedback-packet-audit",
        "status": "PASS",
        "source": {
            "record": "https://zenodo.org/records/15364358",
            "file": "fast_feedback_raw_data.h5",
            "md5": md5,
            "sha256": sha256,
            "raw_file_committed": False,
        },
        "checks_passed": len(checks),
        "totals": totals,
        "circuits": circuits,
        "earned": [
            "source-pinned Ankaa-2 physical session",
            "8,000 row-joined returned hardware repetitions",
            "216,000 classified and 216,000 complex soft measurement events",
            "decoder-register and timing row joins",
            "documented conditional-X branch and later q50 response",
            "immediate fidelity, double-measurement, and T1 reference packets",
            "explicit no-reset metadata",
        ],
        "missing": [
            "census of every pre-return trigger, rejected attempt, and retry",
            "main physical Quil/pulse program and decoder firmware/configuration",
            "controller route and hidden memory state",
            "raw within-measurement waveform lineage",
            "physical archive retention/access/reset policy",
            "declared hidden-environment completion scope",
        ],
        "disposition": "RETURNED_SHOT_MULTI_TIME_PARTIAL_REOPENER",
        "scientific_nonclaim": (
            "The packet supports returned-shot record/action/response analysis. "
            "It does not identify the all-attempt process or a complete material "
            "archive, and it establishes no remainder, new law, or new physics."
        ),
    }

    if args.write_artifact:
        ARTIFACT_PATH.write_text(json.dumps(artifact, indent=2) + "\n", encoding="utf-8")

    print(
        "PASS:",
        f"{len(checks)}/{len(checks)} checks;",
        "8000 joined returned rows;",
        "implementation-complete boundary remains",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
