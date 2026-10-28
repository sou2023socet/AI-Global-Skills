---
name: Skill - 253 - Test Account Provisioning (Legacy Source Record)
description: Use when creating, provisioning, or cleaning up a temporary demo/test account through an application's authorized backend workflow for testing authentication or roles.
---

# Skill - 253 - Test Account Provisioning (Legacy Source Record)

## Purpose and Scope
Provision a short-lived, least-privilege test identity through an existing authorized backend or development fixture. When the project has no safe mechanism, guide a guarded backend-side implementation rather than bypassing authentication or inserting insecure credentials.

## Trigger Conditions
- A user requests a temporary, demo, fixture, or test account for an authorized application.
- Authentication or role-based workflows require a test identity.
- A test environment needs repeatable account setup and cleanup.

## Non-Trigger Conditions
- Do not create accounts in production or on third-party systems without explicit authorization.
- Do not bypass login, MFA, email verification, authorization, or account policy.
- Do not use for generating arbitrary demo data unrelated to identity; use `safe-demo-data-seeding`.

## Prerequisites and Inputs
- Explicit authorization and a confirmed non-production environment.
- Supported account lifecycle mechanism (test fixture, seed command, admin API, or documented backend workflow).
- Required role, expiry/cleanup policy, and safe credential delivery method.
- Test mailbox or synthetic identity domain approved for the environment.

## Execution Workflow
1. Inspect backend auth configuration, profiles, account creation flow, password hashing, role checks, and cleanup support. Do not print existing credentials or user records.
2. Confirm the target is a dedicated test/dev environment using an explicit profile or server-side guard. If environment identity is uncertain, stop and ask.
3. Prefer existing test fixtures or documented administrative tooling. Do not create public registration endpoints, hardcoded accounts, authentication bypasses, or backdoor credentials.
4. If a backend change is required, propose a test-profile-only seeder/command guarded to fail closed outside test/dev. Obtain approval for the exact code change and a separate command-scoped approval before executing account creation.
5. Generate a unique synthetic identity and a strong random secret. Assign only the role needed. Store the password using the project's existing secure hasher; never store plaintext. Obtain command-scoped approval before any test execution that creates or changes an account.
6. Keep credentials out of source, logs, screenshots, command history, and reports. Deliver them only through the approved secure channel, or let tests retrieve secrets from a protected environment variable/store.
7. Verify only the intended login and authorization outcomes. Confirm denied access for an unassigned role when in scope.
8. Revoke/delete the test account and associated sessions/tokens using the approved lifecycle. Confirm cleanup without exposing account secrets.

## Commands and Examples
Inspect the backend's existing profile and test entry points before invoking any seeder:

```powershell
Get-ChildItem -Recurse -Include *Test*.java,application*.yml,application*.properties
Get-ChildItem Env: | Where-Object Name -Match 'SPRING|PROFILE|TEST'
```

```bash
find . -type f \( -name '*Test*.java' -o -name 'application*.yml' -o -name 'application*.properties' \)
env | grep -E '^(SPRING|PROFILE|TEST)'
```

These commands inspect only; use the repository's documented test-profile command after reviewing its effects.

## Deliverables and Outputs
- Environment and authorization confirmation.
- Account lifecycle method, assigned role, expiry, and cleanup outcome without logging the password.
- Test results for login and scoped authorization.
- Any proposed backend-only test provisioning design, clearly separated from executed actions.

## Quality Gates and Acceptance Criteria
- Account creation is impossible or explicitly rejected in production configuration.
- Passwords use the existing server-side password hashing and secret handling.
- Identity is synthetic, unique, least-privilege, and time-bounded or explicitly cleaned up.
- Authentication and authorization are tested through normal application paths.

## Security and Safety Rules
- Never hardcode, print, commit, screenshot, or include account passwords, reset links, tokens, or personal data.
- Never weaken production authentication to enable tests.
- Never query or mutate production user tables for demo purposes.
- If authorization, environment isolation, secure delivery, or cleanup cannot be verified, do not create the account.
