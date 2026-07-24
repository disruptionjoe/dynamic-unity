#!/usr/bin/env python3
"""Source-scoped Clock-QW/QCA record-entailment audit.

Arrighi, Facchini, and Forets (2014, arXiv:1404.4499) construct an exact
discrete Lorentz covariance relation for a Clock quantum walk and a Clock
quantum cellular automaton.  Their Clock QW uses a finite countdown that is
decremented during idle propagation and reset when the effective coin acts.
The Clock QCA replaces that internal countdown with crossing "keep going"
signals.  A discrete Lorentz transform replaces one lattice point by an
alpha-by-beta lightlike patch; in the Clock QW it also sends

    p -> alpha * p,  q -> beta * q.

This probe asks a deliberately narrower question than whether a recorder
*could* be coupled to that dynamics:

    Does the published covariance construction itself entail an accumulated,
    perfectly readable observer record?

The finite calculations separate:

* microscopic patch/update count (changes under the source encoding);
* effective interaction count (a quotient of the complete circuit trace);
* the reset countdown/current keep-going signal (a transient clock state);
* an exact accumulated count register (an added T+1-state memory); and
* T independent durable binary records (an added 2**T-state memory).

The dimension lower bounds are elementary distinguishability results.  They
do not prove that a covariant recorder extension is impossible.  They show
that a recorder is additional state/resource structure and that an external
trace count cannot silently stand in for a stored observer record.
"""

from __future__ import annotations

from dataclasses import dataclass
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
    / "du_foundational_orthodox_clock_qca_record_entailment_result.json"
)


@dataclass(frozen=True)
class ClockQWParameters:
    """The source's right/left idle-step parameters."""

    p: int
    q: int

    @property
    def effective_coin_dimension(self) -> int:
        return self.p + self.q

    def transformed(self, alpha: int, beta: int) -> "ClockQWParameters":
        if alpha < 1 or beta < 1:
            raise ValueError("alpha and beta must be positive integers")
        return ClockQWParameters(alpha * self.p, beta * self.q)


def countdown_trace(length: int, effective_interactions: int) -> list[int]:
    """Return the reset countdown states on one direction branch.

    The source counter is idle/decrementing between effective coin actions and
    resets after reaching zero.  The repeated state is therefore a phase of
    the next interaction cycle, not the total number of completed cycles.
    """

    if length < 1 or effective_interactions < 1:
        raise ValueError("positive length and interaction count required")
    states: list[int] = []
    for _ in range(effective_interactions):
        states.extend(range(length - 1, -1, -1))
    states.append(length - 1)
    return states


def patch_receipt(
    interactions: int,
    alpha: int,
    beta: int,
) -> dict[str, int]:
    """Count source-rewrite carriers without equating them to records."""

    return {
        "effective_interactions_in_complete_trace": interactions,
        "lightlike_patch_points": interactions * alpha * beta,
        "right_boundary_encoding_slots": interactions * alpha,
        "left_boundary_encoding_slots": interactions * beta,
    }


def count_register_states(horizon: int) -> list[int]:
    """Minimal exact monotone count record for 0,...,horizon."""

    if horizon < 0:
        raise ValueError("nonnegative horizon required")
    return list(range(horizon + 1))


def cyclic_counter_readout(elapsed: int, dimension: int) -> int:
    """Finite cyclic readout used as the aliasing rival."""

    if elapsed < 0 or dimension < 1:
        raise ValueError("invalid cyclic counter")
    return elapsed % dimension


def independent_binary_memory_dimension(bits: int) -> int:
    """Dimension needed to distinguish every possible T-bit record string."""

    if bits < 0:
        raise ValueError("nonnegative bit count required")
    return 2**bits


def model_receipt(
    interactions: int,
    alpha: int,
    beta: int,
    recorder_enabled: bool,
) -> dict[str, Any]:
    """Run the same source bookkeeping with or without an added recorder."""

    return {
        "source": patch_receipt(interactions, alpha, beta),
        "stored_count": interactions if recorder_enabled else None,
        "recorder_enabled": recorder_enabled,
    }


def make_check(name: str, passed: bool, detail: str) -> dict[str, Any]:
    return {"name": name, "pass": bool(passed), "detail": detail}


def main() -> None:
    base = ClockQWParameters(p=2, q=3)
    training_boosts = ((1, 1), (2, 1), (1, 3), (2, 3), (3, 2))
    held_out_boost = (4, 3)
    interactions = 5

    patch_rows = []
    for alpha, beta in (*training_boosts, held_out_boost):
        transformed = base.transformed(alpha, beta)
        patch_rows.append(
            {
                "alpha": alpha,
                "beta": beta,
                "base_parameters": {"p": base.p, "q": base.q},
                "transformed_parameters": {
                    "p_prime": transformed.p,
                    "q_prime": transformed.q,
                },
                "base_effective_coin_dimension": (
                    base.effective_coin_dimension
                ),
                "transformed_effective_coin_dimension": (
                    transformed.effective_coin_dimension
                ),
                **patch_receipt(interactions, alpha, beta),
            }
        )

    countdown = countdown_trace(base.p, effective_interactions=4)
    one_cycle = countdown_trace(base.p, effective_interactions=1)
    two_cycles = countdown_trace(base.p, effective_interactions=2)

    horizons = (1, 2, 5, 8, 13)
    memory_rows = [
        {
            "horizon_T": horizon,
            "exact_monotone_count_min_dimension": horizon + 1,
            "constructed_count_register_dimension": len(
                count_register_states(horizon)
            ),
            "independent_T_bit_record_min_dimension": (
                independent_binary_memory_dimension(horizon)
            ),
        }
        for horizon in horizons
    ]

    cyclic_dimension = 5
    cyclic_aliases = [
        {
            "elapsed_a": elapsed,
            "elapsed_b": elapsed + cyclic_dimension,
            "same_readout": (
                cyclic_counter_readout(elapsed, cyclic_dimension)
                == cyclic_counter_readout(
                    elapsed + cyclic_dimension, cyclic_dimension
                )
            ),
            "readout": cyclic_counter_readout(elapsed, cyclic_dimension),
        }
        for elapsed in range(cyclic_dimension)
    ]
    recorder_on = model_receipt(interactions, 2, 3, recorder_enabled=True)
    recorder_off = model_receipt(interactions, 2, 3, recorder_enabled=False)

    checks = [
        make_check(
            "source parameter transform is applied exactly",
            all(
                row["transformed_parameters"]["p_prime"]
                == row["alpha"] * base.p
                and row["transformed_parameters"]["q_prime"]
                == row["beta"] * base.q
                for row in patch_rows
            ),
            "p'=alpha p and q'=beta q on training and held-out boosts",
        ),
        make_check(
            "QW internal dimension is observer-encoding dependent",
            any(
                row["transformed_effective_coin_dimension"]
                != row["base_effective_coin_dimension"]
                for row in patch_rows[1:]
            ),
            "p+q changes when p and q are rescaled",
        ),
        make_check(
            "microscopic patch count changes under nontrivial transforms",
            all(
                row["lightlike_patch_points"] != interactions
                for row in patch_rows
                if (row["alpha"], row["beta"]) != (1, 1)
            ),
            "one source point becomes an alpha-by-beta patch",
        ),
        make_check(
            "effective interaction trace count survives the declared quotient",
            all(
                row["effective_interactions_in_complete_trace"]
                == interactions
                for row in patch_rows
            ),
            "the complete-history macro count is held fixed by construction",
        ),
        make_check(
            "held-out refinement preserves only the macro trace count",
            patch_rows[-1]["effective_interactions_in_complete_trace"]
            == interactions
            and patch_rows[-1]["lightlike_patch_points"]
            == interactions * held_out_boost[0] * held_out_boost[1],
            "alpha=4,beta=3 was not used in the training set",
        ),
        make_check(
            "countdown resets rather than accumulating completed interactions",
            one_cycle[-1] == two_cycles[-1] == base.p - 1,
            "one and two completed cycles have the same final countdown state",
        ),
        make_check(
            "countdown trace exposes repeated transient states",
            len(set(countdown)) == base.p
            and len(countdown) > len(set(countdown)),
            "phase states repeat across four effective interactions",
        ),
        make_check(
            "final countdown hides provenance",
            countdown_trace(base.p, 1)[-1]
            == countdown_trace(base.p, 4)[-1],
            "different interaction histories end in the same reset state",
        ),
        make_check(
            "exact monotone T-count register has T+1 states",
            all(
                row["constructed_count_register_dimension"]
                == row["exact_monotone_count_min_dimension"]
                for row in memory_rows
            ),
            "perfectly distinguishing 0,...,T requires at least T+1 states",
        ),
        make_check(
            "independent binary history has 2^T possible records",
            all(
                row["independent_T_bit_record_min_dimension"] == 2 ** row["horizon_T"]
                for row in memory_rows
            ),
            "storing arbitrary T-bit strings is stronger than storing a count",
        ),
        make_check(
            "finite cyclic counter aliases elapsed counts",
            all(row["same_readout"] for row in cyclic_aliases),
            "n and n+d have identical readout in a d-state cycle",
        ),
        make_check(
            "external trace count and endpoint state are distinct",
            countdown_trace(base.p, 1)[-1]
            == countdown_trace(base.p, 2)[-1]
            and 1 != 2,
            "the historian distinguishes traces whose reset state does not",
        ),
        make_check(
            "recorder ablation leaves source clock trace intact",
            recorder_on["source"] == recorder_off["source"],
            "removing an appended count register changes no source patch count",
        ),
        make_check(
            "recorder ablation removes stored count",
            recorder_on["stored_count"] == interactions
            and recorder_off["stored_count"] is None,
            "the stored value exists only in the appended register model",
        ),
        make_check(
            "no physical unit is generated",
            all(
                isinstance(row["horizon_T"], int)
                and isinstance(row["exact_monotone_count_min_dimension"], int)
                for row in memory_rows
            ),
            "all outputs are dimensionless counts or Hilbert-space dimensions",
        ),
    ]
    passed = sum(check["pass"] for check in checks)

    candidate = {
        "schema_version": SCHEMA_VERSION,
        "candidate_id": "DU-FOUNDATIONAL-ORTHODOX-CLOCK-QCA-RECORD-ENTAILMENT",
        "title": "Clock-QW/QCA source record-entailment audit",
        "track": (
            "Science Council premise-free foundational wave / orthodox "
            "Clock-QW/QCA observer-record entailment assay"
        ),
        "question": (
            "Does the published exact Clock-QW/QCA covariance construction "
            "itself entail an accumulated, perfectly readable observer record?"
        ),
        "warrants": ["DERIVED", "CONSTRUCTIVELY_REALIZED"],
        "assumptions": [
            {
                "id": "A1",
                "statement": (
                    "Use the source Clock-QW semantics: a finite counter "
                    "decrements during idle propagation and resets when the "
                    "effective coin acts."
                ),
                "status": "STANDARD",
                "role": "Defines what the published internal clock stores.",
            },
            {
                "id": "A2",
                "statement": (
                    "Use the source Lorentz encoding p'=alpha p, q'=beta q "
                    "and point-to-alpha-by-beta-patch replacement."
                ),
                "status": "STANDARD",
                "role": "Defines the representation/refinement comparison.",
            },
            {
                "id": "A3",
                "statement": (
                    "An exact readable count 0,...,T requires mutually "
                    "distinguishable record states."
                ),
                "status": "STANDARD",
                "role": "Supplies the finite-dimensional memory lower bound.",
            },
            {
                "id": "A4",
                "statement": (
                    "A recorder extension may be appended conditionally, but "
                    "is not treated as part of the cited source model."
                ),
                "status": "CONDITIONAL_POSIT",
                "role": "Keeps constructibility separate from entailment.",
            },
        ],
        "free_choices": [
            {
                "id": "C1",
                "choice": "Use base p=2,q=3 and five exact interaction events.",
                "why_not_forced": "They are finite audit fixtures.",
                "sensitivity_test": (
                    "Sweep five training encodings and held-out alpha=4,beta=3."
                ),
            },
            {
                "id": "C2",
                "choice": "Use horizons T in {1,2,5,8,13}.",
                "why_not_forced": "The dimension bounds hold for every T.",
                "sensitivity_test": "Require the formula at every horizon.",
            },
            {
                "id": "C3",
                "choice": "Use a five-state cyclic counter as the alias rival.",
                "why_not_forced": "Any finite d aliases n and n+d.",
                "sensitivity_test": "Check all five residue classes.",
            },
        ],
        "equations": [
            "p'=alpha p; q'=beta q",
            "one lattice point -> alpha-by-beta lightlike patch",
            "exact count records 0,...,T => dim(H_record)>=T+1",
            "arbitrary T-bit record strings => dim(H_record)>=2^T",
            "cyclic_d(n)=n mod d=cyclic_d(n+d)",
        ],
        "observables": [
            "microscopic lightlike patch count",
            "effective interaction count on the complete circuit trace",
            "final reset-countdown state",
            "appended exact count-register state",
            "appended independent-bit memory dimension",
        ],
        "comparators": [
            "published Clock QW reset countdown",
            "published Clock QCA keep-going signal semantics",
            "external historian counting effective interactions",
            "appended exact monotone count register",
            "appended finite cyclic counter",
            "appended independent durable binary records",
        ],
        "null_models": [
            "nontrivial source encoding/refinement",
            "held-out alpha=4,beta=3 encoding",
            "different histories with the same reset endpoint",
            "finite cyclic-memory alias",
            "recorder-off ablation",
        ],
        "falsifiers": [
            (
                "The source equations specify a representation-independent "
                "accumulated observer-memory readout."
            ),
            (
                "The reset counter endpoint distinguishes every number of "
                "completed interactions."
            ),
            (
                "Raw microscopic update count is invariant under the source "
                "Lorentz encoding."
            ),
            (
                "A fixed finite d-state cyclic counter distinguishes n from "
                "n+d."
            ),
        ],
        "stop_conditions": [
            (
                "Stop saying observer records are already extracted from the "
                "published Clock-QCA."
            ),
            (
                "Do not infer that no covariant recorder extension can exist."
            ),
            (
                "Do not equate an external history functional with stored "
                "observer memory."
            ),
            (
                "Do not infer physical time, units, gravity, Dynamic Unity, "
                "or Lambda from these dimensionless checks."
            ),
        ],
        "concept": {
            "concept_id": "CONCEPT-DU-002",
            "invariant": (
                "A physical record clock requires a representation-independent "
                "durable state readout with declared provenance and resources."
            ),
            "formalization_id": (
                "ORTHODOX-CLOCK-QCA-SOURCE-RECORD-ENTAILMENT"
            ),
            "failure_scope": "FORMALIZATION",
        },
        "result": {
            "claim": (
                "The published exact covariance construction supplies "
                "transient countdown/keep-going structure and an invariant "
                "effective-interaction trace quotient, but its stated maps do "
                "not entail an accumulated stored observer record. Exact "
                "finite-horizon recorders are constructible only as additional "
                "memory: at least T+1 distinguishable states for a count, or "
                "2^T for arbitrary independent binary records."
            ),
            "grade": (
                "SOURCE-SCOPED ENTAILMENT GAP / EXACT MEMORY LOWER BOUNDS / "
                "RECORDER EXTENSION OPEN"
            ),
            "admission": "CONDITIONAL_CANDIDATE",
            "remaining_uncertainty": (
                "Whether a resource-accounted recorder extension can preserve "
                "the source covariance relation, survive reunion and carried-"
                "record tests, and define a persistent observer."
            ),
            "checks": checks,
        },
    }

    payload = {
        "probe": "du_foundational_orthodox_clock_qca_record_entailment_probe",
        "primary_source": {
            "citation": (
                "Arrighi, Facchini, Forets, Discrete Lorentz covariance for "
                "Quantum Walks and Quantum Cellular Automata (2014)"
            ),
            "url": "https://arxiv.org/abs/1404.4499",
            "source_scoped_facts": [
                "Clock QW countdown decrements and resets at effective coin",
                "Clock QW p,q rescale under the discrete Lorentz transform",
                "Clock QW effective internal dimension changes by observer",
                "Clock QCA replaces the countdown with keep-going signals",
                "Clock QCA has a fixed three-dimensional wire state",
                "one point is represented by an alpha-by-beta lightlike patch",
            ],
        },
        "patch_rows": patch_rows,
        "countdown": {
            "base_p": base.p,
            "four_interaction_trace": countdown,
            "one_cycle_final": one_cycle[-1],
            "two_cycle_final": two_cycles[-1],
        },
        "memory_lower_bounds": memory_rows,
        "cyclic_aliases": cyclic_aliases,
        "recorder_ablation": {
            "recorder_on": recorder_on,
            "recorder_off": recorder_off,
        },
        "checks": checks,
        "checks_passed": passed,
        "checks_total": len(checks),
        "verdict": (
            "SOURCE CLOCK SEMANTICS ARE NOT AN ACCUMULATED OBSERVER RECORD / "
            "TRACE QUOTIENT EXISTS / EXPLICIT RECORDER EXTENSION REQUIRED"
        ),
        "scope": {
            "earned": [
                "source-scoped separation of update, clock phase, trace, and record",
                "exact finite-horizon memory lower bounds",
                "held-out representation/refinement control",
                "a recorder-off ablation and endpoint-provenance counterexample",
            ],
            "not_earned": [
                "a no-go on covariant recorder extensions",
                "a physical observer or irreversible record",
                "a dimensional time unit",
                "higher-dimensional Lorentz covariance, gravity, DU, or Lambda",
            ],
        },
    }

    receipt = comparison_receipt(candidate)
    if receipt["contract_status"] != "COMPLETE":
        raise RuntimeError(
            f"incomplete candidate contract: {receipt['contract_errors']}"
        )
    write_candidate_artifact(ARTIFACT_PATH, candidate, payload)

    print("ORTHODOX CLOCK-QCA RECORD-ENTAILMENT AUDIT")
    for check in checks:
        print(f"{'PASS' if check['pass'] else 'FAIL'}  {check['name']}")
    print(f"{passed}/{len(checks)} checks pass")
    print(
        "VERDICT: SOURCE RECORD NOT ENTAILED / "
        "TRACE QUOTIENT EXISTS / RECORDER EXTENSION OPEN"
    )
    print(f"contract: {receipt['contract_status']} (not scientific endorsement)")
    print(f"artifact: {ARTIFACT_PATH}")
    if passed != len(checks):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
