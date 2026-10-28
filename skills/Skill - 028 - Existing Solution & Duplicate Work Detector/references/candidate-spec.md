# Source candidate specification

- **Purpose/problem; goal/outcome:** Teams build capabilities already in code, tools, or another approved project; recommend reuse/build/retire with evidence.
- **Behavior; activation/non-activation:** Search current project and authorized reusable sources; do not copy code or assume another project’s license/access.
- **Inputs/tools/dependencies/handoff:** Problem/requirements, canonical project registry, existing assets, reuse permissions; code search and registry; depends 03/04/17; hands decision to 19/22/28/60.
- **Procedure/decision:** 1) Search symbols, manifests, catalogs, and integrations. 2) Compare capability and constraints. 3) Verify ownership/license/maintenance. 4) Recommend reuse only if fit and rights are evidenced; otherwise mark candidate for evaluation.
- **Outputs/acceptance/failure:** Reuse-vs-build matrix with evidence and rationale; pass when search scope and exclusions are disclosed. Restricted projects are not searched.
- **Security/example/evidence/maintenance:** Keep project data isolated; no secret/code exfiltration. Example: existing CSV export covers format but lacks required access controls, so gap is explicit. **Status:** proposed workflow; discovery/search tools exist but no duplicate detector. Recheck before implementation.
