# Source candidate specification

- **Purpose/problem; goal/outcome:** Inconsistent runtimes/configuration prevent reproducible work; inventory environment and compatibility, then propose safe changes.
- **Behavior; activation/non-activation:** Inspect manifests, runtimes, env templates, and supported dependencies; do not install/update packages without explicit scope.
- **Inputs/tools/dependencies/handoff:** Project manifest, lockfiles, runtime requirements, target platform; version commands/package managers; depends 04/17/24; hands compatibility to 26–31/34–47.
- **Procedure/decision:** 1) Read manifests/lockfiles and installed tool versions. 2) Compare declared vs available requirements. 3) Trace incompatible/transitive constraints. 4) If remediation requires upgrade/install, present diff/risk/rollback and wait for approval.
- **Outputs/acceptance/failure:** Environment matrix and reproducibility plan; pass when required vs installed versions are distinguished. Missing tool is a blocker, not silently installed.
- **Security/example/evidence/maintenance:** Do not print secret env values; report variable names only. Example: expected Java 21 but runtime 17 results in blocked build recommendation. **Status:** partial—project discovery/DevOps/database instructions. Recheck on lockfile/runtime changes.
