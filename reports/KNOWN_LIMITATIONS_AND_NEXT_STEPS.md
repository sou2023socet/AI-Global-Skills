# Known limitations and next steps

- Canonical packages are reusable instruction contracts, not autonomous
  executors.
- The 125 active canonical skills are structurally validated; functional and
  platform verification remains unrun.
- The Universal Project Structure & Governance skill's five requested
  application scenarios remain `NOT_TESTED`; its structural validation does
  not establish functional effectiveness.
- All 143 source skills have a hashed, traceable canonical destination. The
  143 `legacy-*` folders remain source-preserving provenance copies and are not
  active registry records.
- Similarity pairs in `SKILL_OVERLAP_REVIEW.csv` are review evidence, not proof
  of duplication. Capability owners should review medium-confidence pairs
  before future deprecation.
- Dependency edges remain conservative. The graph is cycle-checked, but
  domain-specific optional dependencies may still need owner enrichment.
- The previously generated release archive is not refreshed for the latest
  skill update; its earlier verification does not cover current workspace
  changes.
- License ownership and runtime effectiveness were not independently verified.
