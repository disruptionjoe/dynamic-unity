---
title: "SWING-DU-COV-02 — covariant-count and perturbation kill of the Lambda(N) cosmology"
status: completed_scoped_exploration
doc_type: exploration
created: 2026-07-21
lane: "1 / Channel 1.4 (covariant cosmology and observational confrontation)"
verdict: "VIABLE_ONLY_AS_LAMBDA_LIMIT. A natural local covariant lift exists at complete-Q interacting-vacuum grade, so COV-01 is not merely coordinate bookkeeping. But the lift fixes a scalar force with c_N^2=beta Omega_V^3/[2(1-Omega_V)]; at every accelerating COV-01 fixed point c_N^2=3 Omega_V*>1. The geodesic/zero-sound escape contradicts the local count transport for any growing matter mode when beta>0. Linear-scale growth independently pressures beta toward ~1e-5 or below under a deliberately weak force/gravity discriminator, where Lambda changes by <1e-5 since z=2. No ghost-free claim is available without an action. The surviving physical branch is the constant-Lambda limit; the causal-past four-volume remains a distinct retarded nonlocal model, not a rescue of this background."
preregistered_outcome: VIABLE_ONLY_AS_LAMBDA_LIMIT
claim_status_change: none
banked: false
probe: tests/du_lambda_N_covariant_perturbation_kill.py
artifact: tests/artifacts/du_lambda_N_covariant_perturbation_kill_result.json
run_plan: lab/process/runs/RUN-20260721-230002-covariant-count-perturbation/run-plan.md
grade: "Exact/structural for the covariant equations, gauge-invariant comoving closure, principal characteristic, fixed-point identity, causal-volume power-law calculation, and beta=0 control; deterministic finite-model grade for the single-fluid linear-growth integration (18/18 checks, 30k/60k convergence); phenomenological interacting-vacuum grade for the complete-Q model; no fundamental action, Boltzmann hierarchy, baryon/radiation split, nonlinear structure simulation, or likelihood. Scoped to the declared count candidates and strongest local lift; not a universal no-go for every nonlocal/UV completion."
---

# SWING-DU-COV-02 — covariant-count and perturbation kill

## Answer up front

The result is sharper than either “the background was fake” or “the model works.”

1. **A real covariant lift exists.** Treat `N` as a scalar counter carried by the
   matter congruence, and replace coordinate `H` with the local expansion scalar
   `Theta/3`. With `V(N)=A/sqrt(N)`, the vacuum stress fixes the complete transfer
   four-vector. No arbitrary `Q(a)` or momentum-transfer function is needed.
2. **That lift fails its perturbation test.** The count perturbation and matter
   expansion form a propagating scalar mode whose characteristic speed is fixed:

   ```text
   c_N^2 = beta Omega_V^3 / [2(1-Omega_V)].
   ```

   At every accelerating fixed point from COV-01 this simplifies exactly to
   `c_N^2=3 Omega_V*>1`. Within the declared continuum equations, the characteristic
   cone is wider than the metric light cone.
3. **The obvious escape is unavailable.** Setting the transfer parallel to the
   matter four-velocity would make the effective sound speed zero, but it also sets
   the comoving `delta N` to zero. The actual count transport then forces the local
   expansion perturbation to vanish. That removes the growing structure mode unless
   `beta=0`.
4. **Growth points the same way.** On `k=0.1 h/Mpc`, the scalar force becomes as
   large as dust gravity near `beta=1.03e-5`. At that value the model's `Lambda`
   changes by only `8.04e-7` between `z=2` and today. This is an internal fail-fast
   discriminator, not an observational confidence interval, but it exposes the
   scale hierarchy.

The preregistered outcome is therefore:

```text
VIABLE_ONLY_AS_LAMBDA_LIMIT
```

The `Lambda~1/sqrt(N)` scaling remains a mathematical/statistical object in the
program. What fails here is this particular constant-`kappa`, matter-congruence
rolling-vacuum completion as nontrivial dark-energy physics.

## 1. Candidate audit: which `N` is meant?

“Four-volume is a scalar” is not enough. The region being counted is part of the
definition.

| candidate | covariance/locality | does it reproduce COV-01? | disposition |
|---|---|---|---|
| Homogeneous `N(t)` or volume between slices | coordinate/slicing dependent; global | yes only by declaration | `BACKGROUND_ONLY` |
| Volume of an arbitrary comoving cell | slice dependent and normalization dependent | a cell choice fixes the amplitude by hand | `BACKGROUND_ONLY` |
| Causal-past volume `Vol(J^-(x) cap J^+(Sigma_0))` | covariant and retarded, but nonlocal | no: its `kappa_eff` depends on the expansion history | separate model |
| Scalar counter carried by matter flow | covariant and local along the physical congruence | yes, exactly | advance to perturbations |
| Geodesic `Q^a parallel u^a` imposed after the fact | covariant as an interaction class | background yes; inhomogeneous count law no | `REIMPORTS_TARGET_HISTORY_OR_BETA_ZERO` |

Two non-intuitive points matter.

First, multiplying the arbitrary comoving cell by `16` multiplies `N` by `16` and
therefore divides `Lambda` by `4`. That is not a prediction; it is an amplitude knob.

Second, the invariant causal-past count is not the same model. For a flat power-law
FLRW spacetime `a(t)=t^p`, `0<p<1`, direct light-cone integration gives

```text
Vol(J^-(T)) = C(p) T^4,
C(p) = [4 pi / 3(1-p)^4] B((1+3p)/(1-p), 4),
kappa_eff(p) = (dN/dt)/H^-3 = 4 C(p) p^3.
```

The executable analytic/numeric cross-check gives

```text
kappa_eff(p=1/2) = 0.119679720137
kappa_eff(p=2/3) = 0.203092858414
ratio             = 1.696969696970
```

Thus a genuine causal-past volume does produce the dimensional `H^-3` scaling in a
power-law era, but not with the constant coefficient used by COV-01 across eras. Its
perturbation is also a retarded integral over the perturbed past light cone, not a
local scalar perturbation. It deserves a separate nonlocal build; importing it here
while retaining the old background would mix two models.

## 2. The strongest local covariant lift

Use metric signature `(-,+,+,+)`. Let `u^a` be the matter four-velocity,
`Theta=nabla_a u^a`, `D_a=h_a^b nabla_b`, and

```text
V(N) = A N^(-1/2),
u^a nabla_a N = S(Theta) = kappa (Theta/3)^(-3),
T_V^{ab} = -V g^{ab}.
```

On FLRW, `Theta=3H`, so the scalar transport reduces exactly to the COV-01 law
`Ndot=kappa H^-3`.

The vacuum divergence is not optional:

```text
nabla_a T_V^{ab} = -nabla^b V.
```

Total conservation therefore fixes the matter equations:

```text
nabla_a T_m^{ab} = +nabla^b V,
dot(rho_m) + Theta rho_m = -dot(V),
rho_m a^b = D^b V.
```

The background energy transfer is exactly `Q=-Vdot`, reproducing COV-01. The spatial
projection fixes the momentum transfer. This is the required complete `Q^a`; no
rest-frame prescription is selected after seeing the perturbations.

This passes COV-02A at **phenomenological covariant interacting-vacuum grade**.

### Action status

A tempting minimal action is

```text
S_N = integral sqrt(-g) [-V(N) + chi(u.nabla N-S(Theta))].
```

But variation with respect to `N` gives an equation of the form
`nabla_a(chi u^a)=-V_N`. Since `V_N=-V/(2N)` is nonzero, `chi` cannot vanish, and
the multiplier sector contributes stress. Silently omitting it does not derive the
COV-01 stress split.

This is not a theorem that no action exists. It establishes the honest grade: the
model below is a complete-`Q` covariant phenomenology, not a ghost-cleared fundamental
action. Consequently, the kinetic sign cannot be banked even though the classical
principal mode is oscillatory rather than gradient-unstable.

## 3. Gauge-invariant scalar closure

For any scalar `X`, define its matter-comoving perturbation

```text
delta X_c = delta X + Xdot theta_m.
```

It is invariant under `t -> t+T`, because `delta X -> delta X-Xdot T` and
`theta_m -> theta_m+T`. Work in matter-comoving gauge only as a convenient
representation; every variable below is the corresponding gauge invariant.

The model fixes

```text
delta V_c = V_N delta N_c,
phi_c = delta V_c / rho_m,
delta(dot N)_c - Ndot phi_c = S_Theta delta Theta_c,
delta(dot rho)_c - rhodot phi_c + Theta delta rho_c + rho deltaTheta_c
    = -delta(dot V)_c + Vdot phi_c,
delta(dot Theta)_c - Thetadot phi_c + (2/3)Theta deltaTheta_c
    + 4 pi G (delta rho_c - 2 delta V_c) - D^2 phi_c = 0.
```

There is no free `delta Q`, sound speed, or momentum-transfer potential.

The transfer force is a scalar gradient and the vacuum has no anisotropic stress, so
the model supplies no new transverse vector or tensor principal mode at linear order.
The scalar sector is the discriminating one.

## 4. Principal characteristic: the exact perturbative kill

At high spatial frequency, background and metric-potential terms without gradients are
lower order. The two load-bearing equations become

```text
delta(dot N)_c = S_Theta deltaTheta_c + lower order,
delta(dot Theta)_c = D^2(delta V_c/rho_m) + lower order.
```

Because

```text
S_Theta = -S/H < 0,
V_N = -V/(2N) < 0,
```

the scalar principal equation is

```text
delta(ddot N)_c + c_N^2 (k^2/a^2) delta N_c = lower order,
c_N^2 = S_Theta V_N / rho_m
      = beta Omega_V^3 / [2(1-Omega_V)].
```

The unstable-interaction control flips the sign of `V_N`; the same executable
principal system then has `c_N^2<0` and exponential gradient growth. The discriminator
can therefore see both sides.

For the positive COV-01 fixed point,

```text
3(1-Omega_V*) = (beta/2) Omega_V*^2.
```

Substitution gives the exact identity

```text
c_N^2(fixed point) = 3 Omega_V*.
```

Acceleration requires `Omega_V*>1/3`. Therefore every accelerating fixed point of
this lift has

```text
c_N^2 > 1.
```

This is not a ghost verdict: there is no action from which to compute a kinetic
Hamiltonian. It is a metric-causality verdict on the declared continuum PDE. A UV
completion could change the high-frequency characteristic, but supplying that new
operator content would be a different model, not a pass earned here.

## 5. Why the zero-sound/geodesic escape does not work

Interacting-vacuum literature contains a useful positive control: if
`Q^a` is parallel to the matter velocity, then the comoving vacuum perturbation
vanishes and the combined rest-frame sound speed is zero.

For this model, however,

```text
Q_a = -nabla_a V,
V_N != 0,
Q^a parallel u^a  =>  D_a V=0  =>  delta N_c=0.
```

Geodesic flow also gives `phi_c=0`. The perturbed transport law then reduces to

```text
0 = S_Theta deltaTheta_c.
```

For `beta>0`, `S_Theta` is nonzero, so `deltaTheta_c=0`. That excludes the ordinary
growing matter mode. One can obtain zero sound only by:

- setting `beta=0`, so the count transport decouples;
- driving `N` with the background `H(t)` instead of local `Theta`, which restores a
  preferred/global history; or
- imposing `delta N_c=0` independently of its equation after seeing the result.

The latter two are the preregistered `REIMPORTS_TARGET_HISTORY` failure, not a rescue.

## 6. Linear growth foreground probe

The executable finite model evolves the exact background plus the comoving scalar
system from `z=100`. Define

```text
n = delta N_c/N,
d = delta rho_c/rho_m,
e = deltaTheta_c/H,
g = beta Omega_V^2,
r = Omega_V/(1-Omega_V),
phi_c = -r n/2,
K = k/(aH).
```

With prime `d/dln(a)`, the integrated equations are

```text
n' = -g(e+n-phi_c),
d' = -c_N^2(d+n/2) + (r/2)n' + (3r/2)n - e,
e' = -(1/2+3Omega_V/2)e -(9/2)(1-Omega_V)phi_c
     -(3/2)(1-Omega_V)d -(3/2)Omega_V n - K^2 phi_c.
```

At `beta=0`, `n=phi_c=0` and these reduce to the standard constant-`Lambda`
growth equation. The independent second-order positive control agrees exactly at the
reported precision. The 30,000-step and 60,000-step integrations agree to
`2.1e-15` on the convergence fixture.

| `beta` | growth ratio at `0.01 h/Mpc` | growth ratio at `0.1 h/Mpc` | force/gravity today at `0.1 h/Mpc` |
|---:|---:|---:|---:|
| `1e-6` | `0.9999981` | `0.9998069` | `0.0967` |
| `1e-5` | `0.9999806` | `0.9980730` | `0.9673` |
| `1e-4` | `0.9998056` | `0.9811111` | `9.6733` |
| `1e-3` | `0.9980592` | `0.8450482` | `96.7327` |
| `1e-2` | `0.9808808` | `0.6465974` | `967.3267` |

The force/gravity ratio is a deliberately weak internal discriminator, not a fit.
Requiring it not to exceed unity today gives

```text
beta <= 1.0338e-5  at k=0.1 h/Mpc,
beta <= 1.0338e-3  at k=0.01 h/Mpc.
```

At the tighter linear-scale value:

```text
Omega_V(z=1100)                 = 1.627e-9,
fractional Lambda change z=2->0 = -8.040e-7.
```

Thus the branch that protects ordinary clustering has already made the count-driven
roll physically negligible. Separately, the natural `beta=9` normalization still
reaches `rho_m=0` near `z=0.179`, re-verifying the COV-01 matter-positivity failure.

This calculation deliberately stops short of a Boltzmann-code likelihood. The exact
future characteristic already fails the declared metric-causal gate, so a precision
fit would optimize a model that has not earned physical admission.

## 7. External primary-source comparison — not DU evidence

- Wands, De-Santiago and Wang,
  [*Inhomogeneous vacuum energy*](https://arxiv.org/abs/1203.6776), establishes
  the relevant standard: a spacetime-dependent vacuum needs a covariant local
  prescription or equivalently `Q_mu=-nabla_mu V`; complete-`Q` phenomenology can be
  perturbatively defined even without a Lagrangian.
- Wang et al.,
  [*Cosmological constraints on a decomposed Chaplygin gas*](https://arxiv.org/abs/1301.5315),
  is the positive control for the distinction between a pressure-carrying/barotropic
  interaction and a geodesic zero-sound interaction. DU re-derives why the latter is
  incompatible with its own count transport rather than importing that model.
- Ahmed, Dodelson, Greene and Sorkin,
  [*Everpresent Lambda*](https://arxiv.org/abs/astro-ph/0209274), is the causal-set
  ancestry of the volume/fluctuation idea; it does not supply this local transport or
  its perturbation closure.
- Aslanbeigi, Saravani and Sorkin,
  [*Generalized Causal Set d'Alembertians*](https://arxiv.org/abs/1403.1622), is a
  useful warning that Lorentz-invariant retarded causal-set operators can remain
  nonlocal and that stability is operator-dependent. It supports keeping the
  causal-past alternative separate rather than calling covariance “locality.”

The foreground equations, characteristic identity, candidate dispositions, and
growth numbers are all Dynamic Unity's own calculation.

## 8. Exact disposition

### What moved

- `HC-DU-002` (covariant/local `N`): **PARTIAL**. A local congruence scalar exists;
  the causal-past definition remains a separate nonlocal model.
- `HC-DU-003` (complete interaction/action): **PARTIAL**. Complete `Q^a` exists;
  no stress-preserving fundamental action or ghost verdict exists.
- `HC-DU-004` (perturbations/growth): **SCOPED FAIL**. The scalar principal cone is
  superluminal on every accelerating attractor and growth is strongly scale dependent.
- `HC-DU-005` (likelihood): **NOT RUN, NO LONGER THE NEXT GATE** for this local
  completion. A likelihood becomes warranted only after a different completion fixes
  the causal principal structure without inserting a free history.

### What did not move

- The half-power scaling's mathematical/statistical grade.
- The unsourced coefficient and external sign.
- Any GU, TaF, TI, P2C, or Continuity Ledger claim.
- Canon, public posture, or publication state.

### Surviving next work

1. Treat the causal-past volume as **`SWING-DU-COV-03`**, a separate retarded
   nonlocal model. Recompute its background from the actual light-cone functional;
   do not reuse constant `kappa`.
2. Complete the typed-`N` diagram (`HC-DU-007`) so causal volume, local counter,
   record count, algebraic count, and observer count cannot be substituted silently.
3. Preserve COV-01 as a scoped background theorem and this COV-02 result as its
   physical-completion boundary.
4. Do not spend on a likelihood or coefficient sourcing for this local closure unless
   new operator content changes the principal cone at a preregistered scale.

## Reproduction

```text
PYTHONDONTWRITEBYTECODE=1 python -B tests/du_lambda_N_covariant_perturbation_kill.py
```

Result: `18/18` checks pass. The JSON artifact is deterministic and includes every
candidate disposition, equation, control, growth row, threshold, and limitation used
in the verdict.
