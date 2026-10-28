---
name: Skill - 197 - Functional Testing
description: Use when validating user-visible features, forms, buttons, navigation, workflows, CRUD, validation, and API-integrated behavior against functional requirements.
---

# Skill - 197 - Functional Testing

## Purpose and Scope
Verify whether implemented features behave as users and requirements expect across complete workflows. Cover positive, negative, boundary, error, and relevant end-to-end behavior; distinguish functional testing from unit-level implementation details.

## Trigger Conditions
- Test an application feature, screen, form, navigation flow, settings option, or CRUD workflow.
- Validate user-visible behavior against acceptance criteria or documented requirements.
- Create a feature checklist and record reproducible pass/fail/blocked outcomes.

## Non-Trigger Conditions
- Do not use for the sole purpose of authoring isolated unit tests; use `unit-test-engineering`.
- Do not use for implementing full test automation infrastructure; use `test-automation-engineering`.
- Do not infer missing functionality or claim untested behavior is correct.

## Prerequisites and Inputs
- Application and authorized environment access.
- Feature scope, expected behavior, safe test identities/data, and side-effect boundaries.
- Available browser/device/API tools and any required test evidence format.

## Execution Workflow
1. Discover implemented routes, controls, feature flags, APIs, requirements, and existing tests. Separate implemented features from planned or unavailable ones.
2. Create feature-wise cases for primary success, invalid input, boundaries, authorization, error handling, and cancel/retry where relevant.
3. Identify persistent or external side effects before execution. Confirm authorization for account creation, CRUD writes, email, payments, or provider calls.
4. Obtain command-scoped approval for test execution. Before any UI/API action that writes data or triggers an external effect, get explicit approval for that exact action. Execute authorized cases through normal user flows. For API-integrated features, inspect both UI behavior and actual request/response when safe and available.
5. Validate outcome semantics, not status alone: check result content, state changes, validation messages, and cleanup.
6. Test supported desktop/mobile layouts and platform-specific flows within available tools. Label unavailable devices and unsupported targets BLOCKED.
7. Record exact steps, expected/actual results, status, errors, and evidence path for every case.
8. Summarize defects with severity and reproducible steps. Fix only when authorized; otherwise document them without source changes.

## Commands and Examples
Start with repository discovery and the configured test runner:

```powershell
Get-ChildItem -Force
Get-ChildItem -Recurse -Include package.json,pom.xml,build.gradle,*.spec.ts,*Test.java
```

```bash
find . -maxdepth 4 -type f \( -name 'package.json' -o -name 'pom.xml' -o -name 'build.gradle' -o -name '*.spec.ts' -o -name '*Test.java' \)
```

Examples locate project files only. Execute feature flows using the app's documented interface and the authorized tools available in the environment.

## Deliverables and Outputs
- Feature inventory and test-case checklist.
- Case-level results with steps, expected/actual behavior, status, errors, and evidence.
- Defect reports and an honest coverage/limitations summary.

## Quality Gates and Acceptance Criteria
- Every identified feature is accounted for as tested, failed, blocked, or not applicable.
- No unexecuted scenario is marked PASS.
- Negative, boundary, and error cases are included when meaningful.
- Evidence and results are traceable to exact test cases and the correct environment.

## Security and Safety Rules
- Use synthetic test data and least-privilege accounts.
- Do not change production or shared persistent data without explicit scope and approval.
- Avoid real email, payment, external AI, or irreversible actions unless explicitly authorized.
- Protect credentials in screenshots, recordings, logs, and reports.
