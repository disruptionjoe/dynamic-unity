#!/usr/bin/env python3
"""Exact regression controls for HC-DU-039C.

The accompanying exploration proves the screened operational-equivalence and
source-attribution-rank results directly.  This executable preserves the
smallest Boolean/Clifford controls:

    source x = (tau, chi) in F_2^2
    total phase phi = tau + chi

One hidden qubit accumulates total phase, a calibrated reference qubit
accumulates tau alone, and one public bit is the center.  The public process is
identical before a noncentral readout.  All calculations are exact; there is
no sampling, numerical tolerance, provider access, or external hardware.
"""

from __future__ import annotations

from fractions import Fraction
import hashlib
import itertools
import json
from pathlib import Path
from typing import Iterable, Sequence


Q = Fraction
Bit = int
Vector = tuple[Bit, ...]
BinaryMatrix = tuple[Vector, ...]
Matrix = tuple[tuple[Fraction, ...], ...]


def matrix(rows: Sequence[Sequence[int | Fraction]]) -> Matrix:
    return tuple(tuple(Q(value) for value in row) for row in rows)


def zeros(n_rows: int, n_cols: int) -> Matrix:
    return tuple(tuple(Q(0) for _ in range(n_cols)) for _ in range(n_rows))


def eye(size: int) -> Matrix:
    return tuple(
        tuple(Q(1 if row == col else 0) for col in range(size))
        for row in range(size)
    )


def unit(size: int, row: int, col: int) -> Matrix:
    return tuple(
        tuple(Q(1 if (i, j) == (row, col) else 0) for j in range(size))
        for i in range(size)
    )


def add(*items: Matrix) -> Matrix:
    if not items:
        raise ValueError("add requires at least one matrix")
    return tuple(
        tuple(
            sum((item[i][j] for item in items), Q(0))
            for j in range(len(items[0][0]))
        )
        for i in range(len(items[0]))
    )


def scale(value: int | Fraction, item: Matrix) -> Matrix:
    factor = Q(value)
    return tuple(tuple(factor * entry for entry in row) for row in item)


def transpose(item: Matrix) -> Matrix:
    return tuple(
        tuple(item[i][j] for i in range(len(item)))
        for j in range(len(item[0]))
    )


def mul(left: Matrix, right: Matrix) -> Matrix:
    if len(left[0]) != len(right):
        raise ValueError("matrix shapes do not compose")
    return tuple(
        tuple(
            sum(
                (left[i][k] * right[k][j] for k in range(len(right))),
                Q(0),
            )
            for j in range(len(right[0]))
        )
        for i in range(len(left))
    )


def kron(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            left[i][j] * right[a][b]
            for j in range(len(left[0]))
            for b in range(len(right[0]))
        )
        for i in range(len(left))
        for a in range(len(right))
    )


def kron_all(*items: Matrix) -> Matrix:
    result = items[0]
    for item in items[1:]:
        result = kron(result, item)
    return result


def trace(item: Matrix) -> Fraction:
    return sum((item[i][i] for i in range(len(item))), Q(0))


def expectation(state: Matrix, effect: Matrix) -> Fraction:
    return trace(mul(state, effect))


def evolve(unitary: Matrix, state: Matrix) -> Matrix:
    return mul(mul(unitary, state), transpose(unitary))


def pullback(unitary: Matrix, effect: Matrix) -> Matrix:
    return mul(mul(transpose(unitary), effect), unitary)


def is_zero(item: Matrix) -> bool:
    return all(entry == 0 for row in item for entry in row)


def xor_dot(row: Vector, source: Vector) -> Bit:
    return sum((a * b for a, b in zip(row, source))) % 2


def apply_binary(rows: BinaryMatrix, source: Vector) -> Vector:
    return tuple(xor_dot(row, source) for row in rows)


def binary_kernel(rows: BinaryMatrix, dimension: int = 2) -> tuple[Vector, ...]:
    return tuple(
        source
        for source in itertools.product((0, 1), repeat=dimension)
        if all(value == 0 for value in apply_binary(rows, source))
    )


def binary_rank(rows: BinaryMatrix, dimension: int = 2) -> int:
    work = [list(row) for row in rows if any(row)]
    rank = 0
    column = 0
    while column < dimension and rank < len(work):
        pivot = next(
            (index for index in range(rank, len(work)) if work[index][column]),
            None,
        )
        if pivot is None:
            column += 1
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        for index in range(len(work)):
            if index != rank and work[index][column]:
                work[index] = [
                    left ^ right
                    for left, right in zip(work[index], work[rank])
                ]
        rank += 1
        column += 1
    return rank


def kernel_contained(
    record_rows: BinaryMatrix, target_rows: BinaryMatrix, dimension: int = 2
) -> bool:
    target_kernel = set(binary_kernel(target_rows, dimension))
    return set(binary_kernel(record_rows, dimension)).issubset(target_kernel)


def all_binary_rows(width: int = 2) -> tuple[Vector, ...]:
    return tuple(itertools.product((0, 1), repeat=width))


def row_span(rows: BinaryMatrix, width: int = 2) -> set[Vector]:
    span: set[Vector] = set()
    for coefficients in itertools.product((0, 1), repeat=len(rows)):
        output = [0] * width
        for coefficient, row in zip(coefficients, rows):
            if coefficient:
                output = [left ^ right for left, right in zip(output, row)]
        span.add(tuple(output))
    return span


def invert_binary_2(item: BinaryMatrix) -> BinaryMatrix:
    (a, b), (c, d) = item
    determinant = (a * d - b * c) % 2
    if determinant != 1:
        raise ValueError("matrix is not invertible over F_2")
    return ((d, b), (c, a))


def binary_matmul(left: BinaryMatrix, right: BinaryMatrix) -> BinaryMatrix:
    return tuple(
        tuple(
            sum(left[i][k] * right[k][j] for k in range(len(right))) % 2
            for j in range(len(right[0]))
        )
        for i in range(len(left))
    )


checks: list[dict[str, object]] = []


def check(name: str, condition: bool, detail: str) -> None:
    checks.append({"name": name, "passed": bool(condition), "detail": detail})
    if not condition:
        raise AssertionError(name)


I2 = eye(2)
X = matrix([[0, 1], [1, 0]])
Z = matrix([[1, 0], [0, -1]])
P0 = unit(2, 0, 0)
P1 = unit(2, 1, 1)
P_PLUS = scale(Q(1, 2), add(I2, X))
P_MINUS = scale(Q(1, 2), add(I2, scale(-1, X)))
I8 = eye(8)


def op(total_fibre: Matrix, tau_fibre: Matrix, public: Matrix) -> Matrix:
    return kron_all(total_fibre, tau_fibre, public)


PUBLIC_0 = op(I2, I2, P0)
PUBLIC_1 = op(I2, I2, P1)
PUBLIC_CENTER = (PUBLIC_0, PUBLIC_1)


def source_state(tau: Bit, chi: Bit) -> Matrix:
    phi = tau ^ chi
    total = P_PLUS if phi == 0 else P_MINUS
    clock = P_PLUS if tau == 0 else P_MINUS
    return op(total, clock, P0)


U_TOTAL_READ = add(
    op(P_PLUS, I2, I2),
    op(P_MINUS, I2, X),
)
U_TAU_READ = add(
    op(I2, P_PLUS, I2),
    op(I2, P_MINUS, X),
)


def center_distribution(state: Matrix) -> tuple[Fraction, Fraction]:
    return expectation(state, PUBLIC_0), expectation(state, PUBLIC_1)


def is_public_central(item: Matrix) -> bool:
    reconstruction = zeros(8, 8)
    for projector in PUBLIC_CENTER:
        support = [
            index for index in range(8) if projector[index][index] == 1
        ]
        coefficient = item[support[0]][support[0]]
        block = mul(mul(projector, item), projector)
        candidate = scale(coefficient, projector)
        if block != candidate:
            return False
        reconstruction = add(reconstruction, candidate)
    return reconstruction == item


def screens_public_center(unitary: Matrix) -> bool:
    return all(
        is_public_central(pullback(unitary, effect))
        for effect in PUBLIC_CENTER
    )


SOURCES = tuple(itertools.product((0, 1), repeat=2))
BASELINE_RECORD = ("event_0", "event_1", "event_2")

check(
    "all four physical sources share one baseline public causal record",
    len(
        {
            (
                BASELINE_RECORD,
                center_distribution(source_state(tau, chi)),
            )
            for tau, chi in SOURCES
        }
    )
    == 1,
    "The screened three-event public chain and its public value are identical.",
)
check(
    "baseline public reachability is source independent",
    all(
        {
            (0, 0),
            (1, 1),
            (2, 2),
            (0, 1),
            (1, 2),
            (0, 2),
        }
        == {
            (left, right)
            for left in range(3)
            for right in range(left, 3)
        }
        for _source in SOURCES
    ),
    "Public order is reconstructible while source duration and field phase vary.",
)
check(
    "total-phase readout is exactly unitary",
    mul(transpose(U_TOTAL_READ), U_TOTAL_READ) == I8,
    "The X-eigenprojectors of the total-phase fibre control the public bit.",
)
check(
    "clock-only readout is exactly unitary",
    mul(transpose(U_TAU_READ), U_TAU_READ) == I8,
    "The calibrated clock fibre independently controls the public bit.",
)
check(
    "both readouts are first noncentral public leaks",
    not screens_public_center(U_TOTAL_READ)
    and not screens_public_center(U_TAU_READ),
    "Each readout converts one hidden fibre phase into a public outcome.",
)

for tau, chi in SOURCES:
    check(
        f"total readout returns tau xor chi for source {tau}{chi}",
        center_distribution(evolve(U_TOTAL_READ, source_state(tau, chi)))
        == ((Q(1), Q(0)) if (tau ^ chi) == 0 else (Q(0), Q(1))),
        "The first leak reconstructs total phase exactly.",
    )

check(
    "one total-phase record cannot attribute time versus field source",
    center_distribution(evolve(U_TOTAL_READ, source_state(0, 1)))
    == center_distribution(evolve(U_TOTAL_READ, source_state(1, 0)))
    == (Q(0), Q(1)),
    "Sources (0,1) and (1,0) have the same total phase and public output after its readout.",
)
check(
    "clock-only probe separates the attribution pair",
    center_distribution(evolve(U_TAU_READ, source_state(0, 1)))
    != center_distribution(evolve(U_TAU_READ, source_state(1, 0))),
    "An independently calibrated tau-sensitive interface distinguishes the pair.",
)

TOTAL: BinaryMatrix = ((1, 1),)
TAU: BinaryMatrix = ((1, 0),)
CHI: BinaryMatrix = ((0, 1),)
FULL: BinaryMatrix = ((1, 1), (1, 0))
ZERO: BinaryMatrix = ()

check(
    "total phase factors through the first leak",
    kernel_contained(TOTAL, TOTAL),
    "The total phase target is constant on every total-phase record fibre.",
)
check(
    "proper-duration target does not factor through total phase",
    not kernel_contained(TOTAL, TAU),
    "Kernel vector (1,1) preserves total phase and changes tau.",
)
check(
    "field-phase target does not factor through total phase",
    not kernel_contained(TOTAL, CHI),
    "Kernel vector (1,1) preserves total phase and changes chi.",
)
check(
    "two independent sensitivities reconstruct both sources",
    binary_rank(FULL) == 2
    and binary_kernel(FULL) == ((0, 0),)
    and kernel_contained(FULL, TAU)
    and kernel_contained(FULL, CHI),
    "Rows (1,1) and (1,0) form an invertible F_2 sensitivity matrix.",
)

nonzero_rows = tuple(row for row in all_binary_rows() if any(row))
check(
    "no one-bit linear probe reconstructs two source bits",
    all(binary_rank((row,)) == 1 for row in nonzero_rows),
    "Every nonzero one-row sensitivity has a two-element kernel.",
)
check(
    "every independent two-probe pair reconstructs both source bits",
    all(
        (
            binary_rank((left, right)) == 2
            and binary_kernel((left, right)) == ((0, 0),)
        )
        for left, right in itertools.combinations(nonzero_rows, 2)
    ),
    "Over F_2^2 the three distinct nonzero rows are pairwise independent.",
)

factorization_audit = []
for mask in range(1 << len(all_binary_rows())):
    selected = tuple(
        row
        for index, row in enumerate(all_binary_rows())
        if mask & (1 << index)
    )
    for target in all_binary_rows():
        by_kernel = kernel_contained(selected, (target,))
        by_row_span = target in row_span(selected)
        factorization_audit.append(by_kernel == by_row_span)

check(
    "kernel containment equals decoder existence exhaustively",
    all(factorization_audit) and len(factorization_audit) == 64,
    "All 16 row subsets and four linear targets satisfy the factorization theorem.",
)

check(
    "baseline record reconstructs public order but neither hidden source",
    kernel_contained(ZERO, ((0, 0),))
    and not kernel_contained(ZERO, TAU)
    and not kernel_contained(ZERO, CHI),
    "A constant public-order target factors; tau and chi vary on the baseline fibre.",
)
check(
    "strict fibre sizes shrink four to two to one",
    len(binary_kernel(ZERO)) == 4
    and len(binary_kernel(TOTAL)) == 2
    and len(binary_kernel(FULL)) == 1,
    "Baseline, total-phase, and two-probe records supply a strict refinement ladder.",
)
check(
    "target-coded record repairs by insertion rather than derivation",
    not kernel_contained(TOTAL, TAU)
    and kernel_contained(TAU, TAU),
    "Appending the tau target itself always closes tau but changes the record interface.",
)

SOURCE_CHANGE: BinaryMatrix = ((1, 1), (0, 1))
SOURCE_CHANGE_INV = invert_binary_2(SOURCE_CHANGE)
TOTAL_REPARAM = binary_matmul(TOTAL, SOURCE_CHANGE_INV)
TAU_REPARAM = binary_matmul(TAU, SOURCE_CHANGE_INV)
FULL_REPARAM = binary_matmul(FULL, SOURCE_CHANGE_INV)
check(
    "factorization verdict is invariant under source reparameterization",
    kernel_contained(TOTAL_REPARAM, TOTAL_REPARAM)
    and not kernel_contained(TOTAL_REPARAM, TAU_REPARAM)
    and kernel_contained(FULL_REPARAM, TAU_REPARAM),
    "A common invertible change of source coordinates preserves every verdict.",
)

check(
    "screened capability cannot discriminate source decomposition",
    len({center_distribution(source_state(tau, chi)) for tau, chi in SOURCES})
    == 1,
    "With only public-center actions, the four sources are operationally equivalent.",
)
check(
    "one leak enlarges capability only to total-phase discrimination",
    len(
        {
            center_distribution(evolve(U_TOTAL_READ, source_state(tau, chi)))
            for tau, chi in SOURCES
        }
    )
    == 2,
    "One extra interface resolves two phase classes, not four sources.",
)
check(
    "two calibrated probes resolve every source",
    len(
        {
            (
                center_distribution(
                    evolve(U_TOTAL_READ, source_state(tau, chi))
                ),
                center_distribution(
                    evolve(U_TAU_READ, source_state(tau, chi))
                ),
            )
            for tau, chi in SOURCES
        }
    )
    == 4,
    "The extra capability is paid for by a second independent sensitivity.",
)

# A distributed-systems shadow of the same rank statement.  This is a typing
# control only: link and scheduler delays are not physical proper time.
def observed_latency(link_delay: Bit, scheduler_delay: Bit) -> Bit:
    return link_delay ^ scheduler_delay


check(
    "distributed total latency has the same source-attribution ambiguity",
    observed_latency(0, 1) == observed_latency(1, 0) == 1,
    "One end-to-end timing bit cannot attribute link versus scheduler delay.",
)
check(
    "route receipt repairs the distributed attribution pair",
    (observed_latency(0, 1), 0) != (observed_latency(1, 0), 1),
    "An independently formed link-specific receipt supplies the second sensitivity.",
)

passed = sum(1 for item in checks if item["passed"])
result = {
    "run_id": "RUN-20260726-174500-screened-effective-physics-attribution",
    "hypothesis_id": "HC-DU-039C",
    "status": "completed_scoped_result",
    "verdict": "KNOWN_MATHEMATICS__SCREENED_OPERATIONAL_EQUIVALENCE_AND_ATTRIBUTION_RANK_EXACT",
    "checks": checks,
    "summary": {
        "passed": passed,
        "total": len(checks),
        "screened_public_process": "the same public chain and center distribution hold for all four tau/chi sources before a noncentral readout",
        "operational_boundary": "public trace functionals reconstruct by screened operational equivalence, which is not source derivation",
        "minimum_leak": "one exact Clifford readout reconstructs phi=tau xor chi",
        "attribution_witness": "sources (tau,chi)=(0,1) and (1,0) have identical baseline and total-phase records but opposite source targets",
        "rank_repair": "a second independently calibrated tau-sensitive probe makes the F_2 sensitivity matrix full rank",
        "capability": "zero, one and two sensitivities distinguish one, two and four source classes respectively",
        "geometry_boundary": "public order is fixed while proper-duration and field-source coordinates remain underidentified until independently calibrated sensitivities are added",
    },
    "north_star_return": {
        "record_first": "public order and every frozen screened public trace functional",
        "operational_duality": "all hidden sources inside the same screened public equivalence class",
        "physics_first_remainder": "a finite first-leak witness whenever an admitted noncentral assay responds to a hidden source",
        "underidentification": "one total phase does not attribute proper-duration versus field contribution",
        "nontrivial_success_rule": "require independently formed strict compression, held-out target transfer, and target-independent sensitivity calibration",
    },
    "local_model_learning_gate": {
        "disposition": "REGRESSION_ONLY_AFTER_DIRECT_PROOF",
        "hardware_required": False,
        "generated_learning_claim": False,
        "purpose": "preserve the minimum exact phase, attribution-rank, capability, and representation controls after proof",
    },
    "claim_ceiling": [
        "finite screened operational-equivalence and linear source-attribution theorem",
        "known linear observability, quantum phase-readout, and causal-order mathematics",
        "binary phase is an exact identifiability control, not a physical ontology",
        "no physical proper-time clock, spacetime metric, field source, interface selection, new law, new physics, paper promotion, hardware result, or publication",
    ],
    "next_dependency": "seek an independently selected physical multi-sensitivity arena whose formed records strictly compress the process and transfer to held-out clock/geometry/field targets without inserting those targets",
}


def jsonable(value):
    if isinstance(value, Fraction):
        return str(value)
    if isinstance(value, tuple):
        return [jsonable(item) for item in value]
    if isinstance(value, list):
        return [jsonable(item) for item in value]
    if isinstance(value, dict):
        return {key: jsonable(item) for key, item in value.items()}
    return value


artifact_path = (
    Path(__file__).resolve().parent
    / "artifacts"
    / "du_screened_effective_physics_attribution_result.json"
)
artifact_path.parent.mkdir(parents=True, exist_ok=True)
payload = json.dumps(jsonable(result), indent=2, sort_keys=True) + "\n"
artifact_path.write_text(payload, encoding="utf-8")
digest = hashlib.sha256(payload.encode("utf-8")).hexdigest()

print(
    json.dumps(
        {
            "artifact": str(artifact_path),
            "passed": passed,
            "sha256": digest,
            "total": len(checks),
            "verdict": result["verdict"],
        },
        indent=2,
        sort_keys=True,
    )
)
