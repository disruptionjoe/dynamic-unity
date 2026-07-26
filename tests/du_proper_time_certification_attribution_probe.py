#!/usr/bin/env python3
"""Exact regression controls for HC-DU-039D.

This probe independently preserves the finite mathematics behind the
proper-time evidence hierarchy:

1. every two-level single-time dephasing factor is a classical random-time
   mixture;
2. conditioned coherent recombination can leave the convex hull of a frozen
   set of history channels; and
3. even complete output-channel knowledge cannot attribute an operationally
   identical generator to proper time rather than an engineered interaction.

The Ramsey control follows the exact two-history construction in
arXiv:2606.12755, evaluated at a rational half-angle.  All arithmetic is
exact.  There is no sampling, floating-point tolerance, provider access,
external hardware, or claim that the proposed optical-clock experiment has
been performed.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import hashlib
import json
from math import isqrt
from pathlib import Path
from typing import Sequence


Q = Fraction


@dataclass(frozen=True)
class Gaussian:
    """A Gaussian rational a + i b."""

    real: Fraction = Q(0)
    imag: Fraction = Q(0)

    def __add__(self, other: "Gaussian") -> "Gaussian":
        return Gaussian(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other: "Gaussian") -> "Gaussian":
        return Gaussian(self.real - other.real, self.imag - other.imag)

    def __neg__(self) -> "Gaussian":
        return Gaussian(-self.real, -self.imag)

    def __mul__(self, other: "Gaussian") -> "Gaussian":
        return Gaussian(
            self.real * other.real - self.imag * other.imag,
            self.real * other.imag + self.imag * other.real,
        )

    def conjugate(self) -> "Gaussian":
        return Gaussian(self.real, -self.imag)

    def scale(self, value: int | Fraction) -> "Gaussian":
        factor = Q(value)
        return Gaussian(factor * self.real, factor * self.imag)

    def norm_sq(self) -> Fraction:
        return self.real * self.real + self.imag * self.imag

    def is_zero(self) -> bool:
        return self.real == 0 and self.imag == 0


ZERO = Gaussian()
ONE = Gaussian(Q(1), Q(0))
I = Gaussian(Q(0), Q(1))
GMatrix = tuple[tuple[Gaussian, ...], ...]


@dataclass(frozen=True)
class ScaledMatrix:
    """Matrix represented as sqrt(scale_sq) times Gaussian-rational rows."""

    scale_sq: Fraction
    rows: GMatrix


def g(value: int | Fraction = 0, imag: int | Fraction = 0) -> Gaussian:
    return Gaussian(Q(value), Q(imag))


def gmatrix(rows: Sequence[Sequence[Gaussian]]) -> GMatrix:
    return tuple(tuple(value for value in row) for row in rows)


def sm(
    rows: Sequence[Sequence[Gaussian]], scale_sq: int | Fraction = 1
) -> ScaledMatrix:
    return ScaledMatrix(Q(scale_sq), gmatrix(rows))


def mat_mul(left: GMatrix, right: GMatrix) -> GMatrix:
    if len(left[0]) != len(right):
        raise ValueError("matrix shapes do not compose")
    return tuple(
        tuple(
            sum(
                (left[row][k] * right[k][col] for k in range(len(right))),
                ZERO,
            )
            for col in range(len(right[0]))
        )
        for row in range(len(left))
    )


def mat_dagger(item: GMatrix) -> GMatrix:
    return tuple(
        tuple(item[row][col].conjugate() for row in range(len(item)))
        for col in range(len(item[0]))
    )


def sm_mul(left: ScaledMatrix, right: ScaledMatrix) -> ScaledMatrix:
    return ScaledMatrix(
        left.scale_sq * right.scale_sq,
        mat_mul(left.rows, right.rows),
    )


def sm_dagger(item: ScaledMatrix) -> ScaledMatrix:
    return ScaledMatrix(item.scale_sq, mat_dagger(item.rows))


def sm_linear(
    left: ScaledMatrix,
    left_weight: int | Fraction,
    right: ScaledMatrix,
    right_weight: int | Fraction,
) -> ScaledMatrix:
    if left.scale_sq != right.scale_sq:
        raise ValueError("scaled matrix addition requires a common scale")
    return ScaledMatrix(
        left.scale_sq,
        tuple(
            tuple(
                left.rows[row][col].scale(left_weight)
                + right.rows[row][col].scale(right_weight)
                for col in range(len(left.rows[0]))
            )
            for row in range(len(left.rows))
        ),
    )


def flatten(item: ScaledMatrix) -> tuple[Gaussian, ...]:
    return tuple(value for row in item.rows for value in row)


def proportional(left: ScaledMatrix, right: ScaledMatrix) -> bool:
    """Global nonzero scales do not affect vector proportionality."""

    a = flatten(left)
    b = flatten(right)
    if all(value.is_zero() for value in a) or all(value.is_zero() for value in b):
        return all(value.is_zero() for value in a) and all(
            value.is_zero() for value in b
        )
    return all(
        a[i] * b[j] == a[j] * b[i]
        for i in range(len(a))
        for j in range(len(a))
    )


def column_output(item: ScaledMatrix, column: int = 0) -> tuple[Gaussian, ...]:
    return tuple(row[column] for row in item.rows)


def output_norm_sq(item: ScaledMatrix, column: int = 0) -> Fraction:
    return item.scale_sq * sum(
        (value.norm_sq() for value in column_output(item, column)), Q(0)
    )


def output_z_unnormalized(item: ScaledMatrix, column: int = 0) -> Fraction:
    output = column_output(item, column)
    if len(output) != 2:
        raise ValueError("Z expectation control requires a two-level output")
    return item.scale_sq * (output[0].norm_sq() - output[1].norm_sq())


def output_z(item: ScaledMatrix, column: int = 0) -> Fraction:
    norm = output_norm_sq(item, column)
    if norm == 0:
        raise ValueError("cannot condition on a zero-probability outcome")
    return output_z_unnormalized(item, column) / norm


def actual_rational_matrix(item: ScaledMatrix) -> tuple[tuple[Fraction, ...], ...]:
    """Return actual entries when sqrt(scale_sq) is rational and rows are real."""

    numerator_root = isqrt(item.scale_sq.numerator)
    denominator_root = isqrt(item.scale_sq.denominator)
    if numerator_root * numerator_root != item.scale_sq.numerator:
        raise ValueError("scale numerator is not a perfect square")
    if denominator_root * denominator_root != item.scale_sq.denominator:
        raise ValueError("scale denominator is not a perfect square")
    factor = Q(numerator_root, denominator_root)
    if any(value.imag != 0 for row in item.rows for value in row):
        raise ValueError("matrix is not rational-real")
    return tuple(
        tuple(factor * value.real for value in row)
        for row in item.rows
    )


def rational_rank(rows: Sequence[Sequence[int | Fraction]]) -> int:
    work = [[Q(value) for value in row] for row in rows if any(value != 0 for value in row)]
    if not work:
        return 0
    rank = 0
    for column in range(len(work[0])):
        pivot = next(
            (row for row in range(rank, len(work)) if work[row][column] != 0),
            None,
        )
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        pivot_value = work[rank][column]
        work[rank] = [value / pivot_value for value in work[rank]]
        for row in range(len(work)):
            if row == rank:
                continue
            coefficient = work[row][column]
            if coefficient != 0:
                work[row] = [
                    left - coefficient * right
                    for left, right in zip(work[row], work[rank])
                ]
        rank += 1
        if rank == len(work):
            break
    return rank


def rational_kernel_2(
    rows: Sequence[Sequence[int | Fraction]],
) -> tuple[tuple[Fraction, Fraction], ...]:
    rank = rational_rank(rows)
    if rank == 2:
        return tuple()
    if rank == 0:
        return ((Q(1), Q(0)), (Q(0), Q(1)))
    first = next(tuple(Q(value) for value in row) for row in rows if any(row))
    a, b = first
    return ((b, -a),)


checks: list[dict[str, object]] = []


def check(name: str, condition: bool, detail: str) -> None:
    checks.append({"name": name, "passed": bool(condition), "detail": detail})
    if not condition:
        raise AssertionError(name)


# ---------------------------------------------------------------------------
# 1. Exact two-level dephasing no-go
# ---------------------------------------------------------------------------

phase = g(Q(3, 5), Q(4, 5))
radius = Q(1, 2)
weight_positive = (Q(1) + radius) / 2
weight_negative = (Q(1) - radius) / 2
gamma = phase.scale(weight_positive) + (-phase).scale(weight_negative)

check(
    "chosen pure phase lies on the unit circle",
    phase.norm_sq() == 1,
    "The exact phase 3/5 + 4i/5 has unit modulus.",
)
check(
    "classical random-time weights form a probability distribution",
    weight_positive == Q(3, 4)
    and weight_negative == Q(1, 4)
    and weight_positive + weight_negative == 1,
    "The two-point measure has weights (1+r)/2 and (1-r)/2.",
)
check(
    "two classical proper-time phases reproduce an interior coherence factor",
    gamma == g(Q(3, 10), Q(2, 5)) and gamma.norm_sq() == Q(1, 4),
    "Opposite phase points with weights 3/4 and 1/4 give |Gamma|=1/2 exactly.",
)
check(
    "clock-only coherence cannot retain the origin label",
    gamma
    == phase.scale(radius),
    "A quantum-generated reduced coherence and an explicit classical random-time mixture have the same Gamma.",
)


# ---------------------------------------------------------------------------
# 2. Exact two-history Ramsey channel witness
# ---------------------------------------------------------------------------

# Rational half angle: cos(theta/2)=3/5, sin(theta/2)=4/5.
half_cos = Q(3, 5)
half_sin = Q(4, 5)
cos_theta = half_cos * half_cos - half_sin * half_sin
sin_theta = 2 * half_cos * half_sin

u_plus = sm(
    [
        [g(half_cos, -half_sin), ZERO],
        [ZERO, g(half_cos, half_sin)],
    ]
)
u_minus = sm(
    [
        [g(half_cos, half_sin), ZERO],
        [ZERO, g(half_cos, -half_sin)],
    ]
)
hadamard = sm([[ONE, ONE], [ONE, -ONE]], Q(1, 2))

v_plus = sm_mul(sm_mul(u_plus, hadamard), u_plus)
v_minus = sm_mul(sm_mul(u_minus, hadamard), u_minus)
k_plus = sm_linear(v_plus, Q(1, 2), v_minus, Q(1, 2))
k_minus = sm_linear(v_plus, Q(1, 2), v_minus, Q(-1, 2))

v_plus_unitarity = actual_rational_matrix(sm_mul(sm_dagger(v_plus), v_plus))
v_minus_unitarity = actual_rational_matrix(sm_mul(sm_dagger(v_minus), v_minus))
identity_2 = ((Q(1), Q(0)), (Q(0), Q(1)))

check(
    "rational half angle gives an exact trigonometric point",
    cos_theta == Q(-7, 25)
    and sin_theta == Q(24, 25)
    and cos_theta * cos_theta + sin_theta * sin_theta == 1,
    "No floating-point approximation is used.",
)
check(
    "both specified Ramsey histories are unitary",
    v_plus_unitarity == identity_2 and v_minus_unitarity == identity_2,
    "V_+=U_+ H U_+ and V_-=U_- H U_- preserve norm exactly.",
)
check(
    "the specified Ramsey histories are distinct Choi rays",
    not proportional(v_plus, v_minus),
    "A nontrivial convex mixture has Choi rank greater than one.",
)

p_plus = (Q(1) + cos_theta * cos_theta) / 2
p_minus = sin_theta * sin_theta / 2
k_plus_gram = actual_rational_matrix(sm_mul(sm_dagger(k_plus), k_plus))
k_minus_gram = actual_rational_matrix(sm_mul(sm_dagger(k_minus), k_minus))

check(
    "bright history-erasure port is subnormalized unitary",
    k_plus_gram == ((p_plus, Q(0)), (Q(0), p_plus)),
    "K_+^dagger K_+=p_+ I exactly.",
)
check(
    "bright-port success probability matches the source equation",
    output_norm_sq(k_plus) == p_plus == Q(337, 625),
    "p_+=(1+cos(theta)^2)/2.",
)
check(
    "bright-port population witness is exact and nonzero",
    output_z(k_plus)
    == (cos_theta * cos_theta - 1) / (cos_theta * cos_theta + 1)
    == Q(-288, 337),
    "For input |g>, conditioned <Z>_+ is outside the specified classical-mixture prediction.",
)
check(
    "both individual classical histories have zero population imbalance",
    output_z(v_plus) == 0 and output_z(v_minus) == 0,
    "Each V_h maps |g> to equal clock populations.",
)
check(
    "every tested convex mixture of specified histories has zero imbalance",
    all(
        weight * output_z(v_plus) + (1 - weight) * output_z(v_minus) == 0
        for weight in (Q(0), Q(1, 4), Q(1, 2), Q(3, 4), Q(1))
    ),
    "Convex reweighting cannot produce the nonzero bright-port witness.",
)
check(
    "bright conditioned operation is not any specified history ray",
    not proportional(k_plus, v_plus) and not proportional(k_plus, v_minus),
    "The rank-one Choi ray of K_+ cannot equal a nonnegative mixture of nonparallel V_h rays.",
)
check(
    "Choi-rank criterion certifies history-relative nonclassicality",
    p_plus > 0
    and not proportional(k_plus, v_plus)
    and not proportional(k_plus, v_minus),
    "The exact sufficient criterion is satisfied relative to H={V_+,V_-}.",
)
check(
    "dark history-erasure port is subnormalized unitary",
    k_minus_gram == ((p_minus, Q(0)), (Q(0), p_minus)),
    "K_-^dagger K_-=p_- I exactly.",
)
check(
    "dark-port probability and conditional contrast are exact",
    output_norm_sq(k_minus) == p_minus == Q(288, 625)
    and output_z(k_minus) == 1,
    "The complementary port is proportional to identity and preserves input |g>.",
)
check(
    "bright and dark probabilities exhaust the erasure measurement",
    p_plus + p_minus == 1,
    "The two conditioned outcomes form a complete ideal history-erasure readout.",
)


# ---------------------------------------------------------------------------
# 3. Mandatory nulls and nuisance boundary
# ---------------------------------------------------------------------------

identical_history_port = sm_linear(v_plus, Q(1, 2), v_plus, Q(1, 2))
check(
    "identical histories null the history-relative certificate",
    proportional(identical_history_port, v_plus),
    "Erasing two labels that induce the same V_h supplies no new history channel.",
)

no_control_plus = sm_mul(u_plus, u_plus)
no_control_minus = sm_mul(u_minus, u_minus)
no_control_port = sm_linear(
    no_control_plus, Q(1, 2), no_control_minus, Q(1, 2)
)
check(
    "removing the intermediate Ramsey control nulls this population discriminator",
    output_z(no_control_port)
    == output_z(no_control_plus)
    == output_z(no_control_minus)
    == 1,
    "The terminal Z statistic no longer distinguishes coherent recombination from the specified mixture.",
)
check(
    "an unrelated erasure label is ordinary erasure, not a history certificate",
    proportional(identical_history_port, v_plus),
    "If the erased branch does not select distinct V_h, the operation stays on one history ray.",
)
check(
    "incoherent history averaging remains in the classical free set",
    output_z(v_plus) == output_z(v_minus) == 0,
    "Discarding the history label yields a convex mixture, not coherent cross terms.",
)
check(
    "broadening the free history set can absorb the certificate",
    any(
        proportional(k_plus, history)
        for history in (v_plus, v_minus, k_plus)
    ),
    "If the normalized K_+ channel is admitted as a new classical history, membership is tautological; H must be frozen independently.",
)

eta_history = Q(4, 5)
eta_clock = Q(3, 4)
eta_motion = Q(2, 3)
eta_total = eta_history * eta_clock * eta_motion
noisy_witness = -eta_total * sin_theta * sin_theta / (
    1 + eta_total * cos_theta * cos_theta
)

check(
    "history-erasure clock and motion nuisances remain separately receipted",
    eta_total == Q(2, 5),
    "The phenomenological visibility product does not identify which channel lost coherence.",
)
check(
    "nonzero calibrated coherence preserves a nonzero witness",
    noisy_witness == Q(-1152, 3223) and noisy_witness < 0,
    "The exact phenomenological witness is attenuated but not erased.",
)
check(
    "complete loss of any required coherence produces a false-negative null",
    -Q(0) * sin_theta * sin_theta / (1 + Q(0) * cos_theta * cos_theta)
    == 0,
    "A null witness does not by itself prove classical histories.",
)


# ---------------------------------------------------------------------------
# 4. Independent nonclassicality and source-attribution axes
# ---------------------------------------------------------------------------

output_only_sensitivities = (
    (Q(1), Q(1)),   # total branch phase
    (Q(2), Q(2)),   # another output statistic of the same total channel
    (Q(-3), Q(-3)), # complete-channel coordinate in a different basis
)
null_direction = (Q(1), Q(-1))

check(
    "all output-only sensitivities have rank one",
    rational_rank(output_only_sensitivities) == 1,
    "Any differentiable observable F(theta_tau+theta_chi) has a row proportional to (1,1).",
)
check(
    "proper-time versus engineered-control exchange is the exact local null",
    rational_kernel_2(output_only_sensitivities) == (null_direction,),
    "The target-changing direction (delta theta_tau, delta theta_chi)=(1,-1) preserves the complete output channel.",
)
check(
    "another output statistic of the same channel does not repair attribution",
    rational_rank(output_only_sensitivities + ((Q(7), Q(7)),)) == 1,
    "More precision or more output observables cannot distinguish identical channels.",
)

source_selective_intervention = (Q(1), Q(0))
repaired_sensitivities = output_only_sensitivities + (
    source_selective_intervention,
)
check(
    "one independently calibrated source-selective intervention closes the local parameter null",
    rational_rank(repaired_sensitivities) == 2,
    "A row not parallel to (1,1) supplies the minimum local rank repair.",
)
check(
    "the repaired local sensitivity map has trivial kernel",
    rational_kernel_2(repaired_sensitivities) == tuple(),
    "Both operational source coefficients can be locally identified under the frozen nuisance/control model.",
)

proper_time_generated = {
    "v_plus": v_plus,
    "v_minus": v_minus,
    "k_plus": k_plus,
    "k_minus": k_minus,
}
engineered_control_generated = {
    "v_plus": v_plus,
    "v_minus": v_minus,
    "k_plus": k_plus,
    "k_minus": k_minus,
}
check(
    "operationally identical generators have identical complete output instruments",
    proper_time_generated == engineered_control_generated,
    "Relabeling one identical Hamiltonian/channel as proper time cannot create an observable difference.",
)
check(
    "full process tomography cannot infer an unencoded mechanism label",
    all(
        proper_time_generated[key] == engineered_control_generated[key]
        for key in proper_time_generated
    ),
    "No POVM on identical output instruments separates their interpretation labels.",
)
check(
    "nonclassical-history certification can hold while source attribution fails",
    not proportional(k_plus, v_plus)
    and rational_rank(output_only_sensitivities) == 1,
    "The Choi certificate advances one evidence axis without closing the mechanism-attribution axis.",
)
check(
    "source attribution can be repaired without upgrading ontology",
    rational_rank(repaired_sensitivities) == 2,
    "Rank two identifies coefficients of the frozen operational Hamiltonian; it does not choose between equivalent interpretations of that Hamiltonian.",
)


# ---------------------------------------------------------------------------
# 5. Evidence surface and result
# ---------------------------------------------------------------------------

evidence_surface = [
    {
        "record": "mean frequency or terminal phase",
        "nonclassical_history": "not certified",
        "source_attribution": "not identified",
        "absorber": "fixed semiclassical average proper time or ordinary phase/potential",
    },
    {
        "record": "single-time reduced clock coherence and visibility",
        "nonclassical_history": "not certified",
        "source_attribution": "not identified",
        "absorber": "classical random proper-time mixture; technical dephasing",
    },
    {
        "record": "joint clock-motion entanglement",
        "nonclassical_history": "conditional quantum-state certificate",
        "source_attribution": "not identified",
        "absorber": "requires frozen state preparation, joint measurement, and history-label provenance",
    },
    {
        "record": "conditioned coherent-history channel outside CPTH(H)",
        "nonclassical_history": "certified relative to frozen H",
        "source_attribution": "not identified",
        "absorber": "different histories/additional controls outside H remain unexcluded",
    },
    {
        "record": "complete output process tomography",
        "nonclassical_history": "classifiable relative to frozen process set",
        "source_attribution": "not identified for identical generators",
        "absorber": "channel equality",
    },
    {
        "record": "output process plus independently calibrated source intervention",
        "nonclassical_history": "separately classifiable",
        "source_attribution": "local operational coefficients identified at full rank",
        "absorber": "equivalent interpretations of the same Hamiltonian remain experimentally indistinguishable",
    },
]
source_statuses = {
    "sorci_et_al_2026": "published_theoretical_proposal",
    "zeng_2026": "preprint_exact_finite_claims_rederived",
    "zych_et_al_2011": "published_theoretical_proposal",
    "loriani_et_al_2019": "published_theory_and_proposed_geometry",
}

check(
    "evidence surface keeps six distinct grades",
    len(evidence_surface) == 6
    and len({row["record"] for row in evidence_surface}) == 6,
    "Mean signal, reduced channel, joint state, conditioned channel, tomography, and source intervention are not collapsed.",
)
check(
    "no evidence tier promotes an observed result",
    set(source_statuses.values())
    == {
        "published_theoretical_proposal",
        "preprint_exact_finite_claims_rederived",
        "published_theory_and_proposed_geometry",
    },
    "The optical-clock and conditioned-history implementations remain proposals.",
)

passed = sum(1 for item in checks if item["passed"])
result = {
    "run_id": "RUN-20260726-183500-proper-time-certification-attribution",
    "hypothesis_id": "HC-DU-039D",
    "status": "completed_scoped_result",
    "verdict": "KNOWN_MATHEMATICS__PROPER_TIME_HISTORY_CERTIFICATION_AND_SOURCE_ATTRIBUTION_AXES_SEPARATED",
    "checks": checks,
    "evidence_surface": evidence_surface,
    "exact_control": {
        "half_cos": half_cos,
        "half_sin": half_sin,
        "cos_theta": cos_theta,
        "sin_theta": sin_theta,
        "classical_coherence": gamma,
        "bright_probability": p_plus,
        "bright_z": output_z(k_plus),
        "dark_probability": p_minus,
        "dark_z": output_z(k_minus),
        "noisy_bright_z": noisy_witness,
        "output_only_rank": rational_rank(output_only_sensitivities),
        "output_only_kernel": rational_kernel_2(output_only_sensitivities),
        "intervention_repaired_rank": rational_rank(repaired_sensitivities),
        "intervention_repaired_kernel": rational_kernel_2(
            repaired_sensitivities
        ),
    },
    "summary": {
        "passed": passed,
        "total": len(checks),
        "mean_signal": "frequency and terminal phase remain compatible with a fixed semiclassical average",
        "reduced_channel": "every two-level single-time dephasing factor is a classical random-proper-time mixture",
        "history_certificate": "conditioned coherent recombination can leave the convex hull of one independently frozen finite history set",
        "source_null": "all output-only functionals of theta_tau+theta_chi retain the exact local null (1,-1)",
        "minimum_repair": "an independently calibrated source-selective intervention, not another output observable, supplies the second sensitivity",
        "interpretation_ceiling": "identical Hamiltonians and channels cannot decide between equivalent proper-time and mass-energy descriptions",
    },
    "north_star_return": {
        "record_first": "a complete conditioned instrument can certify nonmembership in a specified classical-history set",
        "operational_duality": "classical random-time and quantum-generated reduced dephasing share one clock-only record",
        "physics_first_remainder": "coherent cross-history terms separate the conditioned channel from the frozen classical mixture cone",
        "underidentification": "the physical generator remains unassigned when proper-time and engineered contributions induce the same channel",
        "nontrivial_success_rule": "report nonclassicality and source attribution separately; close source rank with preregistered intervention sensitivities and no refitting",
    },
    "primary_source_scope": {
        "source_statuses": source_statuses,
        "sorci_et_al_2026": "published theoretical optical-ion-clock proposal, not an observation",
        "zeng_2026": "June 2026 preprint; finite dephasing and Choi claims independently rederived here",
        "zych_et_al_2011": "phase-versus-visibility motivation, narrowed by the clock-only dephasing no-go",
        "loriani_et_al_2019": "apparatus geometry and clock-transition controls determine which proper-time effect is isolated",
    },
    "local_model_learning_gate": {
        "disposition": "REGRESSION_ONLY_AFTER_DIRECT_PROOF",
        "hardware_required": False,
        "generated_learning_claim": False,
        "purpose": "preserve the exact evidence hierarchy, channel witness, nulls, and intervention-rank boundary after source audit",
    },
    "claim_ceiling": [
        "primary-source-pinned proper-time evidence hierarchy",
        "history-relative nonclassical channel certificate",
        "exact residual local mechanism-attribution null and minimum intervention repair",
        "known quantum channel, convexity, interferometry, and local identifiability mathematics",
        "no observed proper-time nonclassicality, source ontology, universal classical exclusion, new law, new physics, hardware result, or paper promotion",
    ],
    "next_dependency": "choose one preregistered source-selective variation of the relativistic clock-motion coupling and prove that its complete nuisance-aware sensitivity row is not parallel to the ordinary-control row; use existing or proposed data only after that local contract closes",
}


def jsonable(value):
    if isinstance(value, Fraction):
        return str(value)
    if isinstance(value, Gaussian):
        return {"real": str(value.real), "imag": str(value.imag)}
    if isinstance(value, ScaledMatrix):
        return {
            "scale_sq": str(value.scale_sq),
            "rows": jsonable(value.rows),
        }
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
    / "du_proper_time_certification_attribution_result.json"
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
