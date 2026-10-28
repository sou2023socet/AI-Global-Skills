# Source candidate specification

- **Purpose/problem; goal/outcome:** Work begins with incomplete assumptions about code, dependencies, configuration, and docs; produce a bounded, evidence-linked project context baseline.
- **Behavior; activation/non-activation:** Analyze requested project scope and confidence; do not edit files or run unsafe commands during discovery-only use.
- **Inputs/tools/dependencies/handoff:** Canonical project path, task intent, relevant constraints; file/Git search, manifests, optional safe runtime facts; depends 03/73; hands evidence to 07–25.
- **Procedure/decision:** 1) Inspect instructions/status/manifests. 2) Map modules and relevant files. 3) Compare docs with code and record unknowns. 4) If scope is too large, narrow by task and disclose omissions; if identity is ambiguous, stop.
- **Outputs/acceptance/failure:** Context summary with citations, stack/modules, current changes, limitations; pass when each material claim has source evidence and secret values are redacted. Tool errors are explicit, not treated as absence.
- **Security/example/evidence/maintenance:** Read-only by default; never print secrets. Example: unfamiliar Angular repo yields package/runtime facts and unknown backend contract, not guessed routes. **Status:** partial—`project-discovery-audit` covers discovery but not normalized context freshness contract. Reassess sources as repo changes.
