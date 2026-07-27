#!/usr/bin/env python3
"""Exact regression controls for HC-DU-041.

The accompanying exploration proves the factorization statements directly.
This executable preserves only their smallest finite witnesses, the exact
Einstein-source widths, and the current candidate audit.

It is not a simulation, physical model, novelty proof, or hardware assay.
All calculations use finite enumeration, integers, or exact Fraction
arithmetic.
"""

from __future__ import annotations

from fractions import Fraction
import itertools
import json
from pathlib import Path
from typing import Any, Callable, Hashable, Iterable


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT = (
    ROOT
    / "tests"
    / "artifacts"
    / "du_capability_indexed_north_star_result.json"
)
Q = Fraction
State = Hashable
Map = Callable[[State], Hashable]


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, indent=2) + "\n"


def jsonable(value: Any) -> Any:
    if isinstance(value, Fraction):
        return str(value)
    if isinstance(value, tuple):
        return [jsonable(item) for item in value]
    if isinstance(value, list):
        return [jsonable(item) for item in value]
    if isinstance(value, dict):
        return {str(key): jsonable(item) for key, item in value.items()}
    return value


checks: list[dict[str, Any]] = []


def check(name: str, condition: bool, detail: str) -> None:
    checks.append({"name": name, "passed": bool(condition), "detail": detail})
    if not condition:
        raise AssertionError(name)


def factorizes(states: Iterable[State], record: Map, target: Map) -> bool:
    """Return ker(record) subset ker(target) on the supplied finite class."""

    seen: dict[Hashable, Hashable] = {}
    for state in states:
        key = record(state)
        value = target(state)
        if key in seen and seen[key] != value:
            return False
        seen[key] = value
    return True


def partition(states: Iterable[State], observable: Map) -> frozenset[frozenset[State]]:
    blocks: dict[Hashable, set[State]] = {}
    for state in states:
        blocks.setdefault(observable(state), set()).add(state)
    return frozenset(frozenset(block) for block in blocks.values())


def refines(
    fine: frozenset[frozenset[State]],
    coarse: frozenset[frozenset[State]],
) -> bool:
    """Return whether every fine block lies inside one coarse block."""

    return all(any(block <= parent for parent in coarse) for block in fine)


def strict_compression(states: Iterable[State], record: Map) -> bool:
    states_tuple = tuple(states)
    return 1 < len({record(state) for state in states_tuple}) < len(states_tuple)


def xor_pauli(
    left: tuple[tuple[int, ...], tuple[int, ...]],
    right: tuple[tuple[int, ...], tuple[int, ...]],
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    return (
        tuple(a ^ b for a, b in zip(left[0], right[0], strict=True)),
        tuple(a ^ b for a, b in zip(left[1], right[1], strict=True)),
    )


def symplectic(
    left: tuple[tuple[int, ...], tuple[int, ...]],
    right: tuple[tuple[int, ...], tuple[int, ...]],
) -> int:
    return (
        sum(a * b for a, b in zip(left[0], right[1], strict=True))
        + sum(a * b for a, b in zip(left[1], right[0], strict=True))
    ) % 2


def syndrome(
    pauli: tuple[tuple[int, ...], tuple[int, ...]],
    stabilizers: tuple[tuple[tuple[int, ...], tuple[int, ...]], ...],
) -> tuple[int, ...]:
    return tuple(symplectic(pauli, stabilizer) for stabilizer in stabilizers)


def row_fibre_width(
    record_row: tuple[Fraction, Fraction],
    target_row: tuple[Fraction, Fraction],
    box_side: Fraction = Q(2),
) -> Fraction:
    """Maximum target width on one linear-record fibre in [0,box_side]^2."""

    s1, s2 = record_row
    t1, t2 = target_row
    bounds = []
    if s2:
        bounds.append(box_side / abs(s2))
    if s1:
        bounds.append(box_side / abs(s1))
    if not bounds:
        return box_side * (abs(t1) + abs(t2))
    lambda_max = min(bounds)
    return lambda_max * abs(t1 * s2 - t2 * s1)


def main() -> int:
    # The fixed-envelope theorem is just composition of quotient maps. Exhaust
    # the smallest nontrivial binary maps as a regression against code drift.
    four_states = tuple(range(4))
    binary_maps = tuple(itertools.product((0, 1), repeat=4))
    antecedent_count = 0
    counterexamples = 0
    for record_values, behavior_values, target_values in itertools.product(
        binary_maps, repeat=3
    ):
        record = lambda state, values=record_values: values[state]
        behavior = lambda state, values=behavior_values: values[state]
        target = lambda state, values=target_values: values[state]
        if factorizes(four_states, record, behavior) and factorizes(
            four_states, behavior, target
        ):
            antecedent_count += 1
            if not factorizes(four_states, record, target):
                counterexamples += 1
    check(
        "fixed-envelope factorization composition is exhaustive at four states",
        antecedent_count > 0 and counterexamples == 0,
        f"{antecedent_count} binary antecedents, zero counterexamples.",
    )

    # Material Z3 gauge quotient.
    gauge_states = tuple(itertools.product(range(3), repeat=2))
    flux = lambda state: (state[0] + state[1]) % 3
    interior = lambda state: state[0]
    boundary_behavior = lambda state: flux(state)
    enlarged_behavior = lambda state: (flux(state), interior(state))
    check(
        "Z3 flux is a strict noninjective public quotient",
        strict_compression(gauge_states, flux),
        "Nine interior configurations map to three boundary sectors.",
    )
    check(
        "boundary charge target factors through flux",
        factorizes(gauge_states, flux, flux),
        "The public quotient reconstructs the declared boundary charge.",
    )
    check(
        "interior charge does not factor through boundary flux",
        not factorizes(gauge_states, flux, interior),
        "(1,0) and (0,1) share flux but differ on the interior target.",
    )
    check(
        "enlarged gauge capability refines boundary capability",
        refines(
            partition(gauge_states, enlarged_behavior),
            partition(gauge_states, boundary_behavior),
        ),
        "Adding an interior-sensitive action can only split old equivalence classes.",
    )

    # Three-qubit repetition-code quotient.
    zero = (0, 0, 0)
    identity = (zero, zero)
    x1 = ((1, 0, 0), zero)
    x2 = ((0, 1, 0), zero)
    x3 = ((0, 0, 1), zero)
    logical_x = ((1, 1, 1), zero)
    logical_z = (zero, (1, 1, 1))
    stabilizers = (
        (zero, (1, 1, 0)),
        (zero, (0, 1, 1)),
    )
    stabilizer_group = (
        identity,
        stabilizers[0],
        stabilizers[1],
        xor_pauli(stabilizers[0], stabilizers[1]),
    )
    correctable_representatives = (identity, x1, x2, x3)
    correctable = tuple(
        xor_pauli(representative, stabilizer)
        for representative in correctable_representatives
        for stabilizer in stabilizer_group
    )
    correction_label = {
        syndrome(representative, stabilizers): index
        for index, representative in enumerate(correctable_representatives)
    }
    correction_target = lambda pauli: correction_label[
        syndrome(pauli, stabilizers)
    ]
    check(
        "repetition-code syndrome strictly compresses correctable histories",
        len(set(correctable)) == 16
        and len({syndrome(item, stabilizers) for item in correctable}) == 4,
        "Sixteen physical Pauli histories map to four correction syndromes.",
    )
    check(
        "correction target factors through syndrome on the correctable class",
        factorizes(
            correctable,
            lambda pauli: syndrome(pauli, stabilizers),
            correction_target,
        ),
        "The syndrome selects the declared recovery class without logging the error.",
    )
    pauli_states = tuple(
        (
            tuple(bits[:3]),
            tuple(bits[3:]),
        )
        for bits in itertools.product((0, 1), repeat=6)
    )
    logical_signature = lambda pauli: (
        symplectic(pauli, logical_z),
        symplectic(pauli, logical_x),
    )
    check(
        "logical action does not factor through syndrome on the full Pauli class",
        not factorizes(
            pauli_states,
            lambda pauli: syndrome(pauli, stabilizers),
            logical_signature,
        ),
        "Identity and logical operators can share a syndrome.",
    )
    check(
        "logical capability refines syndrome-only capability",
        refines(
            partition(
                pauli_states,
                lambda pauli: (
                    syndrome(pauli, stabilizers),
                    logical_signature(pauli),
                ),
            ),
            partition(
                pauli_states,
                lambda pauli: syndrome(pauli, stabilizers),
            ),
        ),
        "Adding logical actions splits, but never merges, syndrome classes.",
    )
    check(
        "identity and logical X form the minimum same-record witness",
        syndrome(identity, stabilizers) == syndrome(logical_x, stabilizers)
        and logical_signature(identity) != logical_signature(logical_x),
        "The old syndrome is not final for the enlarged logical-action envelope.",
    )

    # Exact weak-field Einstein source-width controls.
    target_row = (Q(1, 2), Q(1, 4))
    r0_row = (Q(1), Q(1))
    r3_row = (Q(1, 4), Q(1, 2))
    r0_width = row_fibre_width(r0_row, target_row)
    r3_width = row_fibre_width(r3_row, target_row)
    determinant = r0_row[0] * r3_row[1] - r0_row[1] * r3_row[0]
    check(
        "first one-clock maximal record leaves exact target width one half",
        r0_width == Q(1, 2),
        f"Exact target-fibre width is {r0_width}.",
    )
    check(
        "second one-clock maximal record leaves exact target width three quarters",
        r3_width == Q(3, 4),
        f"Exact target-fibre width is {r3_width}.",
    )
    check(
        "joined two-clock sensitivity is injective",
        determinant == Q(1, 4),
        "The joined two-by-two source sensitivity has determinant 1/4.",
    )
    check(
        "joined clock reconstruction is tomography rather than strict compression",
        determinant != 0,
        "The repair identifies the full two-parameter source class.",
    )
    check(
        "held-out redshift is the exact joined-record combination",
        (
            Q(3, 4) * r0_row[0] - r3_row[0],
            Q(3, 4) * r0_row[1] - r3_row[1],
        )
        == target_row,
        "t=(3/4)r0-r3 without refitting.",
    )

    # Binary phase/source attribution control.
    phase_states = tuple(itertools.product((0, 1), repeat=2))
    total_phase = lambda state: state[0] ^ state[1]
    tau = lambda state: state[0]
    joined_phase = lambda state: (total_phase(state), tau(state))
    check(
        "total phase is a strict quotient of two source bits",
        strict_compression(phase_states, total_phase),
        "Four sources map to two total phases.",
    )
    check(
        "proper-duration component is not identified by total phase",
        not factorizes(phase_states, total_phase, tau),
        "(0,1) and (1,0) share total phase and disagree on tau.",
    )
    check(
        "independent second sensitivity makes the source map injective",
        len({joined_phase(state) for state in phase_states})
        == len(phase_states),
        "The repair is full source identification, not a nontrivial quotient.",
    )

    # Current candidate audit: every apparent positive misses at least one
    # requirement of endogenous nontrivial record-first reconstruction.
    criteria = (
        "interface_selected",
        "record_formed",
        "strict_noninjective",
        "held_out_physical_target",
        "no_refit",
    )
    candidates = {
        "material_gauge": {
            "interface_selected": False,
            "record_formed": True,
            "strict_noninjective": True,
            "held_out_physical_target": True,
            "no_refit": True,
        },
        "stabilizer_qec": {
            "interface_selected": False,
            "record_formed": True,
            "strict_noninjective": True,
            "held_out_physical_target": True,
            "no_refit": True,
        },
        "einstein_two_clock": {
            "interface_selected": False,
            "record_formed": True,
            "strict_noninjective": False,
            "held_out_physical_target": True,
            "no_refit": True,
        },
        "localized_aqft": {
            "interface_selected": False,
            "record_formed": True,
            "strict_noninjective": True,
            "held_out_physical_target": False,
            "no_refit": True,
        },
        "authenticated_bft": {
            "interface_selected": False,
            "record_formed": True,
            "strict_noninjective": True,
            "held_out_physical_target": False,
            "no_refit": True,
        },
        "two_sensitivity_phase": {
            "interface_selected": False,
            "record_formed": False,
            "strict_noninjective": False,
            "held_out_physical_target": True,
            "no_refit": True,
        },
    }
    winners = [
        name
        for name, verdict in candidates.items()
        if all(verdict[criterion] for criterion in criteria)
    ]
    check(
        "no current specimen closes endogenous compressive reconstruction",
        winners == [],
        "Every current positive is supplied, nonphysical, noncompressive, or lacks a held-out physical target.",
    )
    check(
        "all candidate audits use the same five criteria",
        all(tuple(verdict) == criteria for verdict in candidates.values()),
        "No arena-specific success definition was introduced.",
    )

    payload = {
        "schema_version": "1.0",
        "hypothesis_id": "HC-DU-041",
        "prepared_id": "CCR-N5-S5",
        "status": "PASS" if all(item["passed"] for item in checks) else "FAIL",
        "disposition": "TARGET_ACTION_INDEXED_MIXED_VERDICT",
        "exact_results": {
            "fixed_envelope_antecedents_checked": antecedent_count,
            "fixed_envelope_counterexamples": counterexamples,
            "gauge_state_count": len(gauge_states),
            "gauge_public_sector_count": len({flux(state) for state in gauge_states}),
            "qec_correctable_history_count": len(set(correctable)),
            "qec_syndrome_count": len(
                {syndrome(item, stabilizers) for item in correctable}
            ),
            "einstein_r0_target_fibre_width": r0_width,
            "einstein_r3_target_fibre_width": r3_width,
            "einstein_joined_sensitivity_determinant": determinant,
            "current_endogenous_compressive_winners": winners,
        },
        "candidate_audit": candidates,
        "checks": checks,
        "summary": {
            "passed": sum(item["passed"] for item in checks),
            "total": len(checks),
        },
    }
    ARTIFACT.write_text(canonical_json(jsonable(payload)), encoding="utf-8")
    print(
        f"PASS {payload['summary']['passed']}/{payload['summary']['total']} "
        f"artifact={ARTIFACT.relative_to(ROOT)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
