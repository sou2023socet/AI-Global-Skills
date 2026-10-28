---
name: Skill - 255 - Test Automation Engineering (Legacy Source Record)
description: Use when building or executing repeatable automated tests for web, desktop, API, mobile, or service workflows using the project's existing automation tools.
---

# Skill - 255 - Test Automation Engineering (Legacy Source Record)

## Purpose and Scope
Implement reliable, repeatable automation around observable application behavior using existing project test runners and authorized browser, API, or device tools. Preserve real application behavior and report evidence without fabricating results.

## Trigger Conditions
- Automate UI, API, end-to-end, smoke, or cross-device workflows.
- Add or repair Playwright, Selenium, Cypress, Appium, or equivalent test coverage.
- Capture screenshots, traces, logs, or recordings from actual test execution.

## Non-Trigger Conditions
- Do not use for one-off manual feature acceptance without an automation deliverable; use `functional-testing`.
- Do not use for a single isolated unit; use `unit-test-engineering`.
- Do not automate production mutations or bypass authorization.

## Prerequisites and Inputs
- Application, target environment, test identity, approved test data, and expected behavior.
- Existing browser/device/test runner configuration and supported platform matrix.
- Permission for actions that write data, send messages, or incur external service cost.

## Execution Workflow
1. Inspect test scripts, configuration, existing selectors, service endpoints, and available tools before installing anything.
2. Confirm environment, authorization, account scope, cleanup, and external side effects. Prefer local mocks for external dependencies.
3. Define stable test boundaries and deterministic setup/teardown. Use accessible roles/labels or documented API contracts rather than brittle DOM structure.
4. Obtain approval for the exact test/code changes and command-scoped approval before running automation. Implement one scenario at a time with explicit assertions, bounded waits, and useful failure output. Do not add arbitrary sleeps.
5. Keep test data unique and clean up only resources created by the run. Avoid parallelism against shared mutable state unless concurrency itself is under test.
6. Run focused tests, inspect screenshots/traces/network errors, and fix test flakiness at its source rather than retrying blindly.
7. Capture evidence from the real run. Include viewport/device/browser, test command, and timestamps; redact credentials and personal data.
8. Report passed, failed, skipped, and blocked cases separately. Close only test-owned browser/device sessions and processes.

## Commands and Examples
Use project-discovered commands; these are generic inspection examples:

```powershell
Get-Content package.json
Get-ChildItem -Recurse -Include playwright.config.*,cypress.config.*,pom.xml,build.gradle
```

```bash
cat package.json
find . -maxdepth 4 \( -name 'playwright.config.*' -o -name 'cypress.config.*' -o -name 'pom.xml' -o -name 'build.gradle' \)
```

Run the configured test selector from the correct project directory after reviewing its side effects.

## Deliverables and Outputs
- Reusable automated test(s) and any narrowly scoped fixture/setup helper.
- Reproducible run command and structured test outcomes.
- Real screenshots, traces, logs, or recordings where useful, indexed with scenario and environment details.

## Quality Gates and Acceptance Criteria
- Assertions verify application outcomes, not merely that a page loaded or request returned a success status.
- Runs are stable, bounded, and isolated; failures preserve diagnostic context.
- Evidence is authentic, correctly associated with the run, and free of sensitive data.
- Automated suite does not leave persistent test data or background processes behind.

## Security and Safety Rules
- Never expose credentials, tokens, personal data, or private endpoints in source, console output, reports, or recordings.
- Do not target production unless the user explicitly authorizes a specific non-destructive check.
- Do not submit external prompts, emails, payments, or irreversible actions without explicit approval.
- Avoid downloading or enabling tools before confirming they are needed and permitted.
