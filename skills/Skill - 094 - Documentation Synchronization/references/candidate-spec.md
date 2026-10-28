# Source candidate specification

- **Purpose/problem; goal/outcome:** Docs drift after source/config/API changes; detect impacted docs and synchronize canonical claims.
- **Behavior; activation/non-activation:** Compare source changes to linked docs; do not overwrite user-maintained content without review.
- **Inputs/tools/dependencies/handoff:** Diff, source-of-truth map, docs, owner rules; Git, links, API/schema extraction; depends 06/14/43/75; handoff updated docs to review.
- **Procedure/decision:** 1) Map changed interfaces to docs. 2) Locate stale statements/examples. 3) Update bounded references. 4) If sources conflict or content is intentionally historical, retain with date/context and seek owner decision.
- **Outputs/acceptance/failure:** Change-to-doc map, diff, link check; pass when each impacted doc is updated, confirmed unaffected, or explicitly deferred. Broken link means fail.
- **Security/example/maintenance:** Never copy secret config into examples. Example: renamed route updates API and client setup docs with contract test reference. **Status:** partial—documentation skill says drift checking but no synchronization workflow evidence. Run at release/change.
