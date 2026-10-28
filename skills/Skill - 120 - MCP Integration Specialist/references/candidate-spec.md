# Source candidate specification

- **Purpose/problem; goal/outcome:** Tool servers are connected without clear contracts/permissions; discover, design, and verify supported MCP integrations safely.
- **Behavior; activation/non-activation:** Inspect actual platform/server capabilities and document tool schemas; do not assume endpoint/permissions or configure external systems without approval.
- **Inputs/tools/dependencies/handoff:** Use case, host/server versions, tool schemas, data flows, auth policy; MCP client/docs and safe test server; depends 17/23–25/57; hands workflow to 52–59.
- **Procedure/decision:** 1) Verify current protocol/host support from authoritative docs. 2) Map tool inputs, outputs, errors, permissions and data boundaries. 3) Test read-only contract on safe fixture. 4) If security/scope or host support is unclear, do not enable.
- **Outputs/acceptance/failure:** Integration spec, permission matrix, tests/fallbacks; pass when schema/error/denial behavior verified. Unavailable capability is explicitly blocked.
- **Security/example/maintenance:** Least privilege, secrets via approved store, no prompt injection trust. Example: read-only repository search server returns structured result and denies write. **Status:** proposed—no MCP assets found. Revalidate host/protocol changes.
