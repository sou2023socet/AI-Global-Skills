# Source candidate specification

- **Purpose/problem; goal/outcome:** Useful documentation is missing, fragmented, or stale; reconstruct a sourced, usable baseline and uncertainty register.
- **Behavior; activation/non-activation:** Search docs/comments/manifests/tests and link claims to source; do not invent commands/features or rewrite authoritative content without scope.
- **Inputs/tools/dependencies/handoff:** Repository, existing doc locations, intended audience, available runtime evidence; file search, Markdown link check; depends 04/06/08; hands to 14/43–45.
- **Procedure/decision:** 1) Inventory canonical and orphan docs. 2) Compare statements to code/tests/runtime. 3) Draft missing sections with source citations and uncertainty labels. 4) If conflicts cannot be resolved, preserve both evidence and request owner decision.
- **Outputs/acceptance/failure:** Recovery index, proposed docs, discrepancy list; pass when links resolve and unsupported statements are removed or qualified. Tool failure becomes explicit gap.
- **Security/example/evidence/maintenance:** Remove secret values/PII. Example: reconstruct local setup only from manifest and verified scripts, marking missing environment variables. **Status:** partial—documentation engineering handles authoring/drift but no recovery provenance contract. Re-audit when code changes.
