# Source candidate specification

- **Purpose/problem; goal/outcome:** Individually working components fail across boundaries; verify contracts, versions, devices, services, and environments as a system.
- **Behavior; activation/non-activation:** Build compatibility matrix and test interactions; not a replacement for full architecture redesign.
- **Inputs/tools/dependencies/handoff:** Component versions, interfaces, deployment targets, test environment; API/browser/device/test tools; depends 09/25/26/30; hands defects to 29/35/40.
- **Procedure/decision:** 1) Identify component pairs and contract versions. 2) Prioritize supported combinations. 3) Execute bounded cross-boundary scenarios. 4) If target/tool is unavailable, mark combination unverified rather than infer compatibility.
- **Outputs/acceptance/failure:** Compatibility matrix and integration test results; pass only for tested combinations with evidence. Environment faults are classified separately.
- **Security/example/maintenance:** Authorized endpoints and synthetic data; external provider calls need approval/cost awareness. Example: Angular DTO + Spring endpoint + database path validated end-to-end. **Status:** partial—architecture/testing/mobile skills. Refresh on dependency or API version changes.
