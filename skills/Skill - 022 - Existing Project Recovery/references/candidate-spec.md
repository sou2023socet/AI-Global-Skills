# Source candidate specification

- **Purpose/problem; goal/outcome:** Abandoned, damaged, or poorly understood projects lack a safe recovery path; recover a working baseline, prioritize blockers, and define a controlled plan.
- **Behavior; activation/non-activation:** Triage recovery state and preserve working functionality; do not overwrite, delete, or “repair” before snapshot/scope approval.
- **Inputs/tools/dependencies/handoff:** Project identity, user goal, current Git state, backups/runtime evidence; discovery, logs, tests, backups if authorized; depends 04/06; hands technical unknowns to 08–15, fixes to 29.
- **Procedure/decision:** 1) Record current status and protect uncommitted changes. 2) Inventory breakage, backups, dependencies, and reproducibility. 3) Rank reversible recovery options. 4) If data loss/destructive action is possible, stop for explicit approval and backup confirmation.
- **Outputs/acceptance/failure:** Recovery report, preserved baseline, sequenced actions/rollback points; pass when critical unknowns and non-restorable data are explicit. If backup integrity is uncertain, block restoration.
- **Security/example/evidence/maintenance:** Least privilege; never copy credentials to reports. Example: missing build dependency but source intact yields a reproducible environment plan, not a clean/reset. **Status:** partial—discovery and RCA exist separately; no recovery workflow. Review after each checkpoint.
