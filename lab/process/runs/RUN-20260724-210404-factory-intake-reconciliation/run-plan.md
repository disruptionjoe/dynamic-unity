---
run_id: RUN-20260724-210404-factory-intake-reconciliation
status: completed
repository: dynamic-unity
workflow: Drafting Factory intake reconciliation
authority: "Joe direct chat, 2026-07-24"
claim_grade: "FACTORY CUSTODY RECONCILIATION / NO SCIENTIFIC OR PRODUCTION PROMOTION"
starting_revision: 0504f948891a97b87fdfca561575d3490d92d97d
---

# Drafting Factory intake reconciliation

## Objective

Update Dynamic Unity's authoritative paper-opportunity portfolio after the
Drafting Factory accepts the nine proposal-complete records prepared by the
repository-wide audit.

## Intended changes

- Replace seven unsent standalone-proposal states with confirmed unselected
  Factory-seed custody.
- Replace two unsent merge-review states with confirmed Factory merge-review
  custody.
- Preserve all scientific grades, manuscript-distance estimates, blockers,
  merge relationships, and source ownership.
- Preserve the other eighteen candidates at their existing upstream
  dispositions.
- Record no hardening request, production activation, draft, submission, or
  publication.

## Validation

The portfolio probe must match the exact Factory seed mapping, report zero
remaining complete-unsent proposals, preserve all 27 candidates and ten
concept families, and remain byte-deterministic.

## Result

Completed.

- Confirmed Drafting Factory intake at
  `ca7b748e58e9210fbace1ad897df88f849ae9ff5`.
- Reconciled seven standalone source records to
  `factory_seeded_unselected`.
- Reconciled two source records to `factory_seeded_merge_review`.
- Reduced the complete-unsent proposal batch from nine to zero.
- Preserved all 27 candidate families, all ten concept families, manuscript
  distances, source grades, blockers, merge links, and other-owner
  dispositions.
- Advanced `LANES.yaml` to revision `25` and corrected the conditional
  prediction register so cheap merge-review custody is not confused with
  prediction hardening.

Validation:

- portfolio audit: `PASS 20/20`;
- repeated artifact output: byte-identical;
- artifact SHA-256:
  `51b18d0214e845028d7daffc6e2c13304b4752143f30de81260f1a8bbfc06911`;
- existing cross-repo hardening controls: `PASS 14/14`;
- portfolio and artifact JSON parse: pass;
- `LANES.yaml` parse at manifest/provenance revision `25`: pass;
- probe compilation and `git diff --check`: pass;
- branch comparison: `20` ahead and `0` behind `origin/main`.

No production home, hardening request, research-priority amendment, scientific
grade, draft, submission, publication, or external action changed.
