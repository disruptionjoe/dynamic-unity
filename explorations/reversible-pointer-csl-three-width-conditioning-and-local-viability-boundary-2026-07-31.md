---
title: "Reversible-pointer CSL three-width conditioning and local-viability boundary"
status: banked_scoped_numerical_boundary
doc_type: exploration
created: 2026-07-31
claim_id: HC-DU-188
prediction_id: PRED-DU-005
run_id: RUN-20260731-064400-csl-three-width-conditioning
work_id: CSL-THREE-WIDTH-CONDITIONING
action_id: CSL-THREE-WIDTH-CONDITIONING
program_id: CCR-MINIMAL-PHYSICAL-ANTECEDENT-TO-FINITE-REMAINDER
owner_repo: dynamic-unity
primary_lane: lane_7
supporting_lanes:
  - lane_1
  - lane_3
  - lane_4
channels:
  - CH-EMPIRICAL
  - CH-MODEL
  - CH-FORMAL
  - CH-COLLIDE
evidence_grade: 4
maximum_grade: 4
---

# Reversible-pointer CSL three-width conditioning boundary

## Executive return

```text
HC-DU-187_STRICT-CONVEXITY_REPAIR_CONFIRMED
+ BOTH_SOURCE_BREATHING_FACTORS_REPRODUCED
+ FORMAL_IDENTIFIABILITY_DOES_NOT_IMPLY_NUMERICAL_CONDITIONING
+ SOURCE-TIGHT_PREPARATION_MAKES_THE_CURVATURE_EFFECTIVELY_FLAT
+ SOURCE-NEAR_THREE-WIDTH_CONTRAST_HAS_ASTRONOMICAL_SHOT_PENALTY
+ LARGE_CONTRAST_REQUIRES_TWO-TO-THREE-ORDER_PREPARATION_REDESIGN
+ REDESIGN_LEAVES_THE_SOURCE-AUDITED_SYSTEMATICS_PACKET
+ LOCAL_MODEL_GATE_REACHES_A_CLEAN_HARDWARE_BOUNDARY
+ PRED-DU-005_REMAINS_VALID_BUT_IS_NOT_LOCALLY_ACTIONABLE
+ CHEN-GIACOMINI_RETAINS_THE_HIGHEST_CONDITIONAL_LOCAL_CEILING
+ NO_CSL_EVIDENCE_DEVICE_FORECAST_HARDWARE_ACTION_NEW_DU_LAW_OR_WAVE-3
```

`HC-DU-187` proved that three distinct prepared widths can, in principle,
separate the CSL breathing response from one shared path-loss coefficient and
one width-linear timing-loss coefficient. The proof is exact because the CSL
breathing factor is strictly convex in endpoint variance.

Exact rank is not enough. The remaining question was whether the curve is
curved enough in the proposal's actual regime to support a finite
discriminator. A bounded local calculation now answers that question.

Near the source's very tight preparation trap, the response is nearly flat
after quotienting the two nuisance columns. The three-width contrast is
formally nonzero but catastrophically ill-conditioned. A measurable contrast
requires lowering the preparation trap by orders of magnitude, which is a
new device regime whose systematics the source does not analyze.

This closes the authorized local route before hardware. It does not refute
CSL or the proposed single-point visibility test.

## 1. Source, version, and nonownership

The sole physical source remains Peter Renkel,
["Testing Continuous Spontaneous Localization by Coherently Simulating a
Measurement with a Nanoparticle"](https://arxiv.org/abs/2606.22707),
arXiv:2606.22707v4, revised July 21, 2026.

The paper proposes an experiment and supplies projected sensitivities; it
reports no acquired result. Its baseline parameters include

\[
m=10^{-18}\,\mathrm{kg},\quad
T=0.4\,\mathrm K,\quad
r_c=100\,\mathrm{nm},\quad
\omega=2000\,\mathrm{s}^{-1},\quad
\omega_0=10^7\,\mathrm{s}^{-1}.
\]

The aggressive point uses $ω=1000\,\mathrm{s}^{-1}$ with the same
$ω_0$. The source reports breathing factors $0.0482$ and $0.0241$,
respectively, a benchmark exposure $N_0=5\times10^5$, and an ordinary-loss
budget $\Lambda_0=0.3$.

This run does not own those equations or validate the engineering proposal.

## 2. Dimensionless conditioning object

Let

\[
q=\frac{\omega_0}{\omega},
\qquad
\alpha=\frac{k_BT}{m\omega^2r_c^2},
\qquad
u=\omega t.
\]

For the harmonic path, the source's conservative 3D breathing factor becomes

\[
S(q)
=
\frac1{3\pi}
\int_0^{2\pi}
(1-\cos u)^2
\left[
1+\alpha\left(\sin^2u+\frac{\cos^2u}{q^2}\right)
\right]^{-5/2}du.
\]

The prepared endpoint variance in units of $r_c^2$ is

\[
x(q)=\frac{W}{r_c^2}=\frac{\alpha}{q^2}.
\]

For three ratios $q_i$, `HC-DU-187` fixes weights

\[
w=
(x_3-x_2,\;x_1-x_3,\;x_2-x_1),
\]

which are normalized here so $\sum_i|w_i|=1$. The surviving dimensionless
curvature is

\[
C_S=\sum_iw_iS(q_i).
\]

This quotient removes the common and width-linear nuisance columns. Its
absolute magnitude, not merely its nonzero rank, controls statistical
conditioning.

## 3. Primary-source reproduction

Composite Simpson quadrature with 20,000 panels gives:

| Source point | $q$ | Reported $S_{\rm br}$ | Calculated |
|---|---:|---:|---:|
| baseline | 5,000 | 0.0482 | 0.0481602302 |
| aggressive | 10,000 | 0.0241 | 0.0240797416 |

Doubling the retained grid changes either value by less than
$10^{-12}$. The calculation therefore reproduces the source's rounded
breathing factors before drawing a conditioning conclusion.

## 4. Shot diagnostic and its narrow meaning

The source writes

\[
\Lambda_{\rm CSL}=\lambda K(r_c)
\]

and uses normalized visibility noise $1/\sqrt N$. For a small-signal
log-visibility contrast with L1-normalized weights, optimal allocation
$N_i\propto|w_i|$ gives the optimistic total-shot diagnostic

\[
N_{5\sigma}^{\rm contrast}
\simeq
\frac{25e^{2\Lambda_0}}
{\left|aC_S\right|^2},
\]

where

\[
a
=
\lambda
\frac{K(q_{\rm source})}{S(q_{\rm source})}
\]

is the pointlike exponent amplitude inferred from the source's rounded
kernel. This is deliberately optimistic. It assumes:

- the complete nuisance basis is already correct;
- timing statistics are common and independently monitored;
- width and visibility are joined without selection loss;
- the source's $1/\sqrt N$ model transfers to the contrast;
- configuration overhead is zero; and
- the small-signal approximation holds.

The number is a conditioning diagnostic, not a device forecast.

## 5. Result: the source regime is practically flat

### 5.1 Wide exploratory redesign

The most favorable retained diagnostic uses

\[
q=(10,20,50).
\]

All three preparation traps remain above the weak trap, but they are two to
three orders below the paper's $10^7\,\mathrm{s}^{-1}$ preparation.

| Point | Breathing factors $S(q_i)$ | $|C_S|$ | Optimistic total shots at source $\lambda_{\min}$ | Penalty vs $N_0$ |
|---|---|---:|---:|---:|
| baseline | 0.0085410, 0.0266497, 0.0432603 | 0.0045079 | $5.67\times10^7$ | 113× |
| aggressive | 0.0005689, 0.0042541, 0.0161577 | 0.0042468 | $1.62\times10^7$ | 32× |

These counts do not themselves kill the redesign. They show that even a
large width excursion loses one to two orders of exposure relative to the
single-point source estimate before real redesign systematics are charged.

### 5.2 Source-near preparation family

To test whether the original tight-preparation regime can carry the contrast,
use

\[
q=(500,1000,q_{\rm source}).
\]

| Point | $q_{\rm source}$ | $|C_S|$ | Optimistic total shots |
|---|---:|---:|---:|
| baseline | 5,000 | $3.95\times10^{-9}$ | $7.37\times10^{19}$ |
| aggressive | 10,000 | $3.26\times10^{-8}$ | $2.76\times10^{17}$ |

The contrast is nonzero, exactly as the theorem requires. It is not useful at
the source benchmark. The momentum-spread term, which is independent of
$ω_0$, dominates the breathing integral; changing an already very
tight initial position width barely bends the response.

## 6. Local-viability theorem

### Proposition — formal identifiability without source-regime viability

Within the frozen v4 Gaussian small-separation model:

1. three distinct prepared widths make the CSL column linearly independent
   of one constant and one width-linear nuisance column;
2. at the source's tight-trap ratios, the nuisance-quotiented CSL contrast is
   so small that the paper's own idealized shot model incurs at least a
   $10^{12}$-fold baseline or $10^{11}$-fold aggressive increase over
   $N_0$ for the source-near fixtures; and
3. obtaining an order-$10^{-3}$ breathing contrast requires preparation
   ratios of order 10 to 50, outside the source-analyzed preparation
   and systematic packet.

The first statement is a theorem about rank. The latter two are
source-parameter numerical facts. Together they show that the existing
proposal does not instantiate the formal repair.

The exact penalty ratios in the retained probe are stronger than the coarse
bounds stated here. The coarse statement avoids treating rounded source
parameters as high-precision engineering forecasts.

## 7. Reopener and stop

The reversible-pointer route now has one non-circling reopener:

> A source-pinned device packet must demonstrate a wide preparation-frequency
> range with three fixed widths, measured timing statistics, a complete
> width-dependent nuisance basis, joined attempted-run lineage, and a finite
> predeclared shot/error budget.

Until then:

- do not search for a provider or laboratory;
- do not optimize the local model further;
- do not treat strict convexity as practical identifiability;
- do not reuse the paper's baseline/aggressive pair as a width control; and
- do not mutate `PRED-DU-005-v1` after a future result.

This is exactly the local-model learning rule Joe set: compute only until the
needed insight appears, then stop before external hardware becomes the source
of learning.

## 8. Portfolio consequence

`PRED-DU-005` remains a legitimate imported conditional discriminator. Its
three-width response lock is mathematically sound. It is no longer the
closest **locally actionable** packet because the physical configuration that
would make it informative is unbuilt.

The Chen--Giacomini phase surface retains the highest conditional ceiling and
can still be advanced through source reconstruction, rival-fibre analysis,
and acquisition-contract work without first designing a new device. This
result does not select that branch; it removes the reason to keep spending
local cycles on CSL.

The work is fully absorbed by CSL/open-system phenomenology, numerical
quadrature, conditioning, shot-noise analysis, and optimal experimental
design. No CSL evidence, exclusion, complete apparatus, external hardware
action, new Dynamic Unity law, paper, successor, or Wave-3 activation is
earned.
