# Source candidate specification

- **Purpose/problem; goal/outcome:** Existing screens/flows are unknown; inventory UI, navigation, validation, responsiveness, and accessibility without forcing redesign.
- **Behavior; activation/non-activation:** Inspect authorized UI in available viewports and map observable flows; do not alter visuals or access data beyond test scope.
- **Inputs/tools/dependencies/handoff:** App URL/build, supported devices, authorized account, expected constraints; browser/device tools and screenshots; depends 04/09; hands gaps to 10/20/37/43.
- **Procedure/decision:** 1) Inventory routes/screens and role gates. 2) Exercise representative forms/navigation. 3) Capture viewport/keyboard/validation evidence. 4) If login or tooling is unavailable, report inaccessible areas as unverified, not absent.
- **Outputs/acceptance/failure:** Screen/flow inventory, findings, redacted screenshots; pass when each scoped screen has state and viewport coverage recorded. Broken capture is documented.
- **Security/example/evidence/maintenance:** Use synthetic identity; hide user data. Example: map calculator route and invalid-input feedback at desktop/mobile sizes. **Status:** partial—frontend and functional skills cover implementation/testing, not recovery inventory. Refresh on UI release.
