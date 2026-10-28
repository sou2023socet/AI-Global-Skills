# Source candidate specification

- **Purpose/problem; goal/outcome:** A claimed build/package may be unreproducible or wrong artifact; verify native build, packaging, and install procedure.
- **Behavior; activation/non-activation:** Execute approved local checks and identify artifact; not live deployment.
- **Inputs/tools/dependencies/handoff:** Build manifest, runtime, commit, expected artifact; project-native tools; depends 25/28–31/35/42; hands artifact to 47/48/50.
- **Procedure/decision:** 1) Inspect scripts and working tree. 2) Confirm exact build command and side effects/approval. 3) Run and record exit code/artifact hash/path. 4) On failure preserve logs; do not retry with changed flags without explanation/approval.
- **Outputs/acceptance/failure:** Build/package report with environment and artifact identity; pass only if command succeeded and artifact is present/valid. Missing tool or environment is blocked.
- **Security/example/maintenance:** No secrets in artifact/logs; builds may execute project code, so review scope. Example: package JAR with verified commit SHA and test result. **Status:** partial—backend/frontend/DevOps examples, no generic evidence process. Revalidate on toolchain changes.
