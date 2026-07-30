#!/usr/bin/env python3
"""Pin the public controller-workflow source and its executable-artifact boundary.

The arXiv source describes the controller architecture and intended feedback
workflow in unusual detail.  It does not contain an executable program,
firmware/configuration image, per-attempt controller log, or material archive.

Passing preserves that source boundary and an elementary command/actuation
nonidentification control.  It establishes no laboratory fault, physical
remainder, new law, ontology, or new physics.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import tarfile
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_PATH = (
    ROOT / "tests" / "artifacts" / "du_controller_sidecar_recovery_result.json"
)

EXPECTED_MD5 = "c540a68e31307224b1ed2370cbfe0e00"
EXPECTED_SHA256 = (
    "25f66da6b24385f5456da6c8fd078e597e4d3993b00bf1eb0d7759c55588d8f6"
)
EXPECTED_TEXT_MEMBERS = {"main.tex", "supplement.tex"}
EXECUTABLE_OR_DATA_SUFFIXES = {
    ".py",
    ".quil",
    ".qasm",
    ".bin",
    ".bit",
    ".v",
    ".sv",
    ".vhd",
    ".json",
    ".yaml",
    ".yml",
    ".csv",
    ".h5",
    ".hdf5",
    ".log",
}
POSITIVE_MARKERS = {
    "proprietary_assembly": "proprietary assembly language",
    "decoder_initialization": "Writes to the decoder experiment features",
    "measurement_buffer": (
        "Stores the outcomes of the latest measurement round in the decoder "
        "sequencer's memory"
    ),
    "packet_format": "series of $32$-bit binary strings",
    "status_poll": "polling of the decoder's status register",
    "conditional_x": "Applies an $X$ gate conditionally on the decoding result",
    "matched_idle": (
        "otherwise the qubit is left to idle until measurement for a time "
        "equal to the gate's duration"
    ),
    "wishbone": "32-bit WISHBONE interface",
    "star_route": "hub of a star network",
    "clock_crossing": "clock-crossing logic",
    "physical_clock_check": (
        "measure the delay to applying the conditional operation by "
        "considering its effect on the qubit $T_1$ decay"
    ),
}


def digest(path: Path, algorithm: str) -> str:
    hasher = hashlib.new(algorithm)
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def read_text_member(archive: tarfile.TarFile, name: str) -> str:
    member = archive.getmember(name)
    extracted = archive.extractfile(member)
    if extracted is None:
        raise AssertionError(f"cannot read {name}")
    return extracted.read().decode("utf-8")


def command_actuation_twin() -> dict[str, Any]:
    """Two latent implementations with one returned command/response tuple."""

    delivered = {
        "reported_m1": 0,
        "logical_result": 1,
        "issued_command": "X",
        "latent_post_m1_state": 0,
        "physical_x_delivered": 1,
        "reported_y": 1,
    }
    lost = {
        "reported_m1": 0,
        "logical_result": 1,
        "issued_command": "X",
        # A non-projective/misclassified post-measurement state is admitted by
        # the source's measured P(S|M) calibration.
        "latent_post_m1_state": 1,
        "physical_x_delivered": 0,
        "reported_y": 1,
    }
    visible_fields = ("reported_m1", "logical_result", "issued_command", "reported_y")
    return {
        "visible_fields": list(visible_fields),
        "delivered": delivered,
        "lost": lost,
        "same_visible_tuple": all(delivered[key] == lost[key] for key in visible_fields),
        "different_physical_actuation": (
            delivered["physical_x_delivered"] != lost["physical_x_delivered"]
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--write-artifact", action="store_true")
    args = parser.parse_args()

    source = args.source.resolve()
    md5 = digest(source, "md5")
    sha256 = digest(source, "sha256")
    checks: list[tuple[str, bool]] = [
        ("source_md5", md5 == EXPECTED_MD5),
        ("source_sha256", sha256 == EXPECTED_SHA256),
    ]

    with tarfile.open(source, "r:*") as archive:
        members = sorted(
            member.name.rstrip("/")
            for member in archive.getmembers()
            if member.name.rstrip("/")
        )
        member_set = set(members)
        checks.append(
            ("required_text_members", EXPECTED_TEXT_MEMBERS.issubset(member_set))
        )
        source_text = "\n".join(
            read_text_member(archive, member) for member in EXPECTED_TEXT_MEMBERS
        )

    marker_results = {
        marker_id: marker_text in source_text
        for marker_id, marker_text in POSITIVE_MARKERS.items()
    }
    checks.extend(
        (f"marker_{marker_id}", present)
        for marker_id, present in marker_results.items()
    )

    executable_members = [
        member
        for member in members
        if Path(member).suffix.lower() in EXECUTABLE_OR_DATA_SUFFIXES
    ]
    checks.append(("no_executable_or_data_members", not executable_members))

    twin = command_actuation_twin()
    checks.extend(
        [
            ("command_actuation_same_visible_tuple", twin["same_visible_tuple"]),
            (
                "command_actuation_physical_difference",
                twin["different_physical_actuation"],
            ),
        ]
    )

    failures = [name for name, passed in checks if not passed]
    if failures:
        raise AssertionError(f"failed checks: {failures}")

    artifact = {
        "claim_id": "HC-DU-170",
        "run_id": "RUN-20260730-153100-controller-sidecar-recovery-audit",
        "status": "PASS",
        "source": {
            "name": "arXiv:2410.05202 v1 source bundle",
            "file": source.name,
            "md5": md5,
            "sha256": sha256,
            "raw_file_committed": False,
        },
        "checks_passed": len(checks),
        "bundle_members": members,
        "positive_source_markers": marker_results,
        "executable_or_data_members": executable_members,
        "public_sidecar_ladder": [
            {
                "level": "declared_workflow_and_architecture",
                "status": "SOURCE_SPECIFIED",
            },
            {
                "level": "exact_executable_program_firmware_and_configuration",
                "status": "ABSENT_FROM_SOURCE_BUNDLE",
            },
            {
                "level": "intended_command_semantics",
                "status": "SOURCE_SPECIFIED",
            },
            {
                "level": "per_attempt_command_and_route_lineage",
                "status": "ABSENT_FROM_SOURCE_BUNDLE",
            },
            {
                "level": "aggregate_physical_actuation_check",
                "status": "PARTIALLY_SPECIFIED",
            },
            {
                "level": "per_attempt_physical_actuation_acknowledgement",
                "status": "ABSENT_FROM_SOURCE_BUNDLE",
            },
            {
                "level": "all_attempt_disposition_census",
                "status": "ABSENT_FROM_SOURCE_BUNDLE",
            },
            {
                "level": "archive_retention_access_reset_semantics",
                "status": "ABSENT_FROM_SOURCE_BUNDLE",
            },
            {
                "level": "declared_environment_and_persistence_scope",
                "status": "ABSENT_FROM_SOURCE_BUNDLE",
            },
        ],
        "command_actuation_twin": twin,
        "earned": [
            "source-pinned recovery of the public controller workflow and route architecture",
            "exact distinction between intended command semantics and per-attempt actuation lineage",
            "finite latent-state countermodel showing returned command/response nonidentification of actuation",
            "narrowed fault-model-relative sidecar request",
        ],
        "disposition": [
            "DESCRIPTIVE_CONTROLLER_SIDECAR_RECOVERED",
            "EXECUTABLE_AND_CONFIGURATION_SIDECAR_ABSENT",
            "AGGREGATE_ACTUATION_EVIDENCE_ONLY",
            "PER_ATTEMPT_ACTUATION_NONIDENTIFICATION",
            "ATTEMPT_ARCHIVE_ENVIRONMENT_GATES_UNCHANGED",
            "NO_READY_SUCCESSOR",
        ],
        "scientific_nonclaim": (
            "Passing establishes a public-source boundary and an elementary "
            "nonidentification control. It does not show that a pulse was lost, "
            "that the laboratory record is defective, that a physical remainder "
            "exists, or that new physics is present."
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
        "workflow recovered, executable/actuation sidecars absent"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
