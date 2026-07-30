#!/usr/bin/env python3
"""Audit bounded public surfaces for the Rigetti/Riverlane implementation sidecar.

Passing pins a negative availability result on the declared public surfaces and
an elementary successor-non-substitution control. It does not prove that no
artifact exists privately or elsewhere, evaluate the experiment's correctness,
or establish a physical remainder, ontology, law, or new physics.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_PATH = (
    ROOT / "tests" / "artifacts" / "du_public_sidecar_availability_result.json"
)

EXPECTED_HASHES = {
    "zenodo_record": "3426065169e13a5dee1b952769bc088af91e41b0810e562fa93e62d9d7c98568",
    "riverlane_repos": "9de330581d2eaad311883ce73ae1a6c2328cfe86c808fe9c999dfba419d49b8c",
    "rigetti_repos": "62402cd22a28094aff99440b0af815a717ae78626fdbedf79eb3315ad238de3f",
    "qeciphy_repo": "69bc3baad89a02cec63ac43c718324a4dad09ec36891ac3d5f1bd3f4532681d8",
    "nature_supplement": "e5f2ef9eabd2831d85daa74569cf95175d114a97c2a127e41d9e32f2c9f2cd95",
}
EXPECTED_ZENODO_FILES = {
    "decoder_timings_each_repetition.csv",
    "defect_rates_per_round.txt",
    "defect_rates_per_round_stability_9.txt",
    "fast_feedback_raw_data.h5",
    "fig4b_decoding_response_time.csv",
    "figS4c_feedback_response_time_probability_density_data.csv",
    "figS4c_feedback_response_time_probability_density_fit_parameters.csv",
    "figS4d_t1_time_fitting.csv",
    "lep_belief_matching.txt",
    "lep_fpga.txt",
    "lep_mwpm.txt",
    "lep_mwpm_soft_info_pairwise_correlation_graph.txt",
    "lep_mwpm_soft_info_pairwise_correlation_graph_with_resets.txt",
    "lep_mwpm_stability_9.txt",
    "mean_decoding_time.txt",
    "stability_8_with_resets_raw_data.h5",
    "stability_8_without_resets_raw_data.h5",
    "stability_9_raw_data.h5",
}
EXPECTED_RIVERLANE_REPOS = {
    "ACID",
    "HiddenStateHackathon",
    "QHAL",
    "QStone",
    "caravel_user_project",
    "dockerized-verification-setup",
    "h2_compilation",
    "paris",
    "pauli_lcu",
    "purification-without-post-selection",
    "qeciphy",
    "quantum-freeze",
    "soft_information_models",
}
EXPECTED_RELEVANT_COMMITS = {
    "ACID": "801b2ab41d2ee2a6f78f8b7624335c003b2bb81b",
    "QHAL": "e61b9b80e5a54f277cb65854f62a51c23981ec62",
    "QStone": "3aa26d5b45ecf282438d5d4eb68b84dae1574aeb",
    "qeciphy": "a88289e25f1511ffc75959478799632eea2123b7",
    "soft_information_models": "25f493206c210d53a954539859d76b6d7ca3db79",
}
EXPERIMENT_TERMS = (
    "2410.05202",
    "demonstrating real-time and low-latency quantum error correction",
    "fast_feedback_raw_data",
    "decoder_shot_results",
    "ankaa-2",
    "collision clustering",
    "prototype compiler",
)
EXECUTABLE_SUFFIXES = {
    ".asm",
    ".bin",
    ".bit",
    ".elf",
    ".hex",
    ".json",
    ".py",
    ".qasm",
    ".quil",
    ".sv",
    ".tar",
    ".toml",
    ".v",
    ".vhd",
    ".yaml",
    ".yml",
    ".zip",
}


def digest(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def repo_inventory_text(repos: list[dict[str, Any]]) -> str:
    fields: list[str] = []
    for repo in repos:
        fields.extend(
            str(repo.get(key) or "")
            for key in ("name", "description", "homepage", "html_url")
        )
    return "\n".join(fields).lower()


def git_head(path: Path) -> str:
    return subprocess.run(
        ["git", "-C", str(path), "rev-parse", "HEAD"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()


def scan_checkout(path: Path) -> list[dict[str, str]]:
    hits: list[dict[str, str]] = []
    for candidate in path.rglob("*"):
        if not candidate.is_file() or ".git" in candidate.parts:
            continue
        if candidate.stat().st_size > 2_000_000:
            continue
        try:
            text = candidate.read_text(encoding="utf-8").lower()
        except (UnicodeDecodeError, OSError):
            continue
        for term in EXPERIMENT_TERMS:
            if term in text or term in candidate.name.lower():
                hits.append(
                    {
                        "repository": path.name,
                        "file": str(candidate.relative_to(path)),
                        "term": term,
                    }
                )
    return hits


def successor_non_substitution_twin() -> dict[str, Any]:
    """A later shared interface does not identify one historical executable."""

    historical_a = {
        "later_interface_view": "generic_qec_link_v1",
        "historical_executable_digest": "program-A",
        "historical_route_state": "route-A",
        "held_out_target": "actuation-A",
    }
    historical_b = {
        "later_interface_view": "generic_qec_link_v1",
        "historical_executable_digest": "program-B",
        "historical_route_state": "route-B",
        "held_out_target": "actuation-B",
    }
    return {
        "visible_fields": ["later_interface_view"],
        "historical_a": historical_a,
        "historical_b": historical_b,
        "same_successor_interface_view": (
            historical_a["later_interface_view"]
            == historical_b["later_interface_view"]
        ),
        "different_historical_identity": (
            historical_a["historical_executable_digest"]
            != historical_b["historical_executable_digest"]
        ),
        "different_held_out_target": (
            historical_a["held_out_target"] != historical_b["held_out_target"]
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--zenodo-record", type=Path, required=True)
    parser.add_argument("--riverlane-repos", type=Path, required=True)
    parser.add_argument("--rigetti-repos", type=Path, required=True)
    parser.add_argument("--qeciphy-repo", type=Path, required=True)
    parser.add_argument("--nature-supplement", type=Path, required=True)
    parser.add_argument("--riverlane-checkouts", type=Path, required=True)
    parser.add_argument("--write-artifact", action="store_true")
    args = parser.parse_args()

    inputs = {
        "zenodo_record": args.zenodo_record.resolve(),
        "riverlane_repos": args.riverlane_repos.resolve(),
        "rigetti_repos": args.rigetti_repos.resolve(),
        "qeciphy_repo": args.qeciphy_repo.resolve(),
        "nature_supplement": args.nature_supplement.resolve(),
    }
    hashes = {name: digest(path) for name, path in inputs.items()}
    checks: list[tuple[str, bool]] = [
        (f"{name}_sha256", hashes[name] == expected)
        for name, expected in EXPECTED_HASHES.items()
    ]

    zenodo = load_json(inputs["zenodo_record"])
    zenodo_names = {entry["key"] for entry in zenodo["files"]}
    zenodo_executables = sorted(
        name
        for name in zenodo_names
        if Path(name).suffix.lower() in EXECUTABLE_SUFFIXES
    )
    checks.extend(
        [
            ("zenodo_record_id", zenodo["id"] == 15364358),
            ("zenodo_concept_id", str(zenodo["conceptrecid"]) == "13961129"),
            ("zenodo_exact_inventory", zenodo_names == EXPECTED_ZENODO_FILES),
            ("zenodo_no_executable_sidecar", not zenodo_executables),
        ]
    )

    riverlane = load_json(inputs["riverlane_repos"])
    rigetti = load_json(inputs["rigetti_repos"])
    qeciphy = load_json(inputs["qeciphy_repo"])
    riverlane_names = {entry["name"] for entry in riverlane}
    public_inventory_hits = {
        "riverlane": [
            term
            for term in EXPERIMENT_TERMS
            if term in repo_inventory_text(riverlane)
        ],
        "rigetti": [
            term for term in EXPERIMENT_TERMS if term in repo_inventory_text(rigetti)
        ],
    }
    checks.extend(
        [
            ("riverlane_exact_public_inventory", riverlane_names == EXPECTED_RIVERLANE_REPOS),
            ("rigetti_public_inventory_count", len(rigetti) == 59),
            (
                "public_inventory_has_no_experiment_companion",
                not any(public_inventory_hits.values()),
            ),
            ("qeciphy_created_after_archive", qeciphy["created_at"] > zenodo["updated"]),
            (
                "qeciphy_is_generic_interface",
                "physical layer implementation"
                in str(qeciphy.get("description") or "").lower(),
            ),
        ]
    )

    checkout_root = args.riverlane_checkouts.resolve()
    checkout_commits: dict[str, str] = {}
    checkout_hits: list[dict[str, str]] = []
    for repo_name, expected_commit in EXPECTED_RELEVANT_COMMITS.items():
        repo_path = checkout_root / repo_name
        head = git_head(repo_path)
        checkout_commits[repo_name] = head
        checks.append((f"{repo_name}_commit", head == expected_commit))
        checkout_hits.extend(scan_checkout(repo_path))
    checks.append(("relevant_checkout_no_experiment_sidecar", not checkout_hits))

    supplement_bytes = inputs["nature_supplement"].read_bytes()
    checks.extend(
        [
            ("supplement_is_pdf", supplement_bytes.startswith(b"%PDF-")),
            ("supplement_has_no_embedded_file_marker", b"/EmbeddedFiles" not in supplement_bytes),
        ]
    )

    twin = successor_non_substitution_twin()
    checks.extend(
        [
            (
                "successor_same_interface_view",
                twin["same_successor_interface_view"],
            ),
            (
                "successor_different_historical_identity",
                twin["different_historical_identity"],
            ),
            (
                "successor_different_held_out_target",
                twin["different_held_out_target"],
            ),
        ]
    )

    failures = [name for name, passed in checks if not passed]
    if failures:
        raise AssertionError(f"failed checks: {failures}")

    artifact = {
        "claim_id": "HC-DU-171",
        "run_id": "RUN-20260730-161103-public-sidecar-availability-audit",
        "status": "PASS",
        "bounded_surfaces": {
            "nature_supplement": {
                "file": inputs["nature_supplement"].name,
                "sha256": hashes["nature_supplement"],
                "embedded_file_marker": False,
            },
            "zenodo": {
                "record_id": zenodo["id"],
                "concept_record_id": zenodo["conceptrecid"],
                "updated": zenodo["updated"],
                "file_count": len(zenodo_names),
                "files": sorted(zenodo_names),
                "executable_sidecars": zenodo_executables,
            },
            "official_public_repository_inventories": {
                "riverlane_repository_count": len(riverlane),
                "rigetti_repository_count": len(rigetti),
                "inventory_term_hits": public_inventory_hits,
            },
            "relevant_riverlane_checkout_scan": {
                "commits": checkout_commits,
                "term_hits": checkout_hits,
            },
            "qeciphy": {
                "created_at": qeciphy["created_at"],
                "description": qeciphy.get("description"),
                "historical_mapping_or_digest_found": False,
            },
        },
        "checks_passed": len(checks),
        "successor_non_substitution_twin": twin,
        "disposition": [
            "BOUNDED_PUBLIC_SIDECAR_SEARCH_COMPLETE",
            "NO_EXACT_EXECUTABLE_OR_LINEAGE_SIDECAR_FOUND",
            "EXTERNAL_CUSTODY_DEPENDENCY_CONFIRMED",
            "LATER_OPEN_INTERFACE_NOT_HISTORICAL_REPAIR",
            "PUBLIC_SEARCH_STOP",
            "NO_READY_SUCCESSOR",
        ],
        "scientific_nonclaim": (
            "Passing establishes absence on the declared, frozen public surfaces "
            "and a provenance non-substitution control. It does not prove global "
            "or private absence, evaluate the experiment, establish a physical "
            "remainder, or support new physics."
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
        "bounded public sidecar search closed"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
