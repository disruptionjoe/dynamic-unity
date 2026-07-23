# Dynamic Unity compute readiness cleanup

Status: complete

Run: `RUN-20260723T024341Z-dynamic-unity-direct`

Mode: execute

Lane: `A`

Starting revision: `af4b9d5cdec2fa398b1b8cc26f14d1f1b02b3c2d`

## Objective

Make the numerical probe environment reproducible and verify one current
North-Star-adjacent computation without changing scientific grades or Lane
priority.

## Result

The repository now pins NumPy 2.5.1 in `requirements-compute.txt`, documents a
local virtual-environment workflow, and ignores local environment/cache state.
The import census found NumPy across the current numerical probes and no SciPy
imports, so SciPy is not added as a DU dependency.

`du_loss_lambda_criticality_probe.py` was run twice under CPython 3.14.6 and
NumPy 2.5.1. Both runs returned 20/20 checks and exit 0. The second output was
byte-identical to the first at SHA-256:

```text
84ce711fe70ff5bfea425468fb8500ee14d874c6b189b04cb6d9faa135048759
```

The newly pinned environment changed some Monte Carlo samples and last-bit
floating values relative to the previously tracked artifact, but every
pre-registered tolerance and discriminator remained satisfied. The regenerated
artifact is therefore retained as the reproducible NumPy 2.5.1 baseline. This
is environment/provenance movement only, not scientific promotion.

## Boundary

- No Dynamic Unity claim, grade, North Star, Lane priority, or publication
  posture moved.
- No scheduled CapacityOS relationship or automation was created; the repo
  remains manual pending an explicit owner registration decision.
- NumPy is required and now pinned. SciPy is available in the shared workspace
  environment for sibling work but is not a DU dependency today.

## Validation

- dependency census: ten tracked probe files import NumPy; zero import SciPy;
- two sequential probe runs: 20/20 checks, exit 0, byte-identical second output;
- `git diff --check`: required at close.
