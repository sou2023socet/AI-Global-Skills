# Source candidate specification

- **Purpose/problem; goal/outcome:** Technical docs are incomplete or inconsistent; create audience-specific, sourced artifacts from verified code and decisions.
- **Behavior; activation/non-activation:** Generate requested docs and examples; do not create phantom endpoints, setup steps, or compliance claims.
- **Inputs/tools/dependencies/handoff:** Audience, requirements, source code, actual commands, templates; Markdown/Mermaid/link checker; depends 06/10–13/20; hands to 44/45/50.
- **Procedure/decision:** 1) Identify canonical sources and audience. 2) Build outline against requirements. 3) Draft with source links and uncertainty labels. 4) If an example cannot be executed/verified, label it illustrative or omit it.
- **Outputs/acceptance/failure:** README/API/runbook/architecture docs per request; pass when links resolve, claims are evidenced, and secrets are absent. Renderer failure is recorded.
- **Security/example/maintenance:** Redact secrets/internal details. Example: endpoint docs include schema only after matching controller and tests. **Status:** partial—documentation-engineering skill exists; no generated artifact validation evidence. Regenerate on source changes.
