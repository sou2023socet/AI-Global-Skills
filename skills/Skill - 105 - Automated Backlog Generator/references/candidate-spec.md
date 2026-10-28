# Source candidate specification

- **Purpose/problem; goal/outcome:** Verified findings do not become actionable work; create deduplicated backlog candidates with acceptance and dependencies.
- **Behavior; activation/non-activation:** Transform issues/gaps/risks into proposed tasks; do not auto-approve, assign, or create external tickets without permission.
- **Inputs/tools/dependencies/handoff:** Evidence, severity, project backlog schema, priorities; issue/task API if authorized; depends 06/14/15/23/41/42/61/68; hands to 22/70/78.
- **Procedure/decision:** 1) Validate finding and source. 2) Search existing backlog duplicates. 3) Draft task with impact, acceptance, dependencies and owner suggestion. 4) Require review before publishing or committing priority.
- **Outputs/acceptance/failure:** Backlog candidates and traceability links; pass when each derives from verified evidence or is labeled idea. API unavailable leaves draft only.
- **Security/example/maintenance:** Remove sensitive reproduction details from broad tickets. Example: recurring failing contract test becomes a fix candidate linked to run ID. **Status:** partial—planning/RCA outputs, no backlog generator. Tune prioritization with owner feedback.
