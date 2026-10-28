---
name: Skill - 183 - Focused Function Testing
description: Use when asked to check, exercise, or test one specific function, method, endpoint, control, or narrowly defined behavior and report its actual result.
---

# Skill - 183 - Focused Function Testing

## Purpose and Scope
Trace one named function or narrowly scoped behavior to its real execution boundary, select the smallest meaningful test method, run it safely, and report observed results. This is a bounded alternative to a broad project test campaign.

## Trigger Conditions
- A user asks to test a specific function, API operation, button, calculation, or error path.
- Reproduce a focused defect or verify one acceptance criterion.
- Need a targeted test selection and concise evidence-backed result.

## Non-Trigger Conditions
- Do not expand to unrelated features or a full application audit unless requested.
- Do not use for a feature spanning multiple user-visible steps; use `functional-testing`.
- Do not treat static code inspection as executed runtime testing.

## Prerequisites and Inputs
- Target symbol/control/endpoint and expected behavior, or enough context to identify it.
- Project-native test runner and a safe environment/data fixture.
- Permission for any side effects that the target operation may cause.

## Execution Workflow
1. Resolve the requested target using symbol navigation/search and inspect its implementation, callers, validation, and nearest existing tests.
2. Clarify the observable contract from requirements or current API/UI behavior; note any ambiguity instead of inventing expected results.
3. Choose the smallest test boundary that proves the behavior: direct unit test, API contract call, UI interaction, or end-to-end step.
4. Identify normal, boundary, invalid, and failure inputs relevant to this target. Avoid unrelated exploratory testing.
5. Inspect the exact command/action and obtain command-scoped approval before test execution. Run the targeted test with the project's supported selector, or exercise the real interface if no test exists and it is authorized.
6. Capture actual output, exceptions, network/API evidence, and screenshots where applicable. Distinguish expected error handling from a test harness error.
7. If a defect is reproduced, report minimal reproduction steps and evidence. Do not change production code unless the user authorized fixes.
8. State what was not tested and whether the observed result is sufficient to call the request complete.

## Commands and Examples
Inspect the target and project scripts before choosing the runner:

```powershell
rg "TargetFunction|target-operation" -n .
```

```bash
rg "TargetFunction|target-operation" -n .
```

Use the framework's focused selector only after discovering the actual test framework and test name; do not invent a command that could silently run no tests.

## Deliverables and Outputs
- Target name and exact test boundary.
- Test steps/input, expected and actual result, PASS/FAIL/BLOCKED, and evidence.
- Reproduction instructions for any defect plus explicit scope limitations.

## Quality Gates and Acceptance Criteria
- The requested function or behavior was actually executed, not only inspected.
- Assertions map directly to the stated behavior and relevant input classes.
- The correct test was selected and its execution is confirmed by runner output.
- No unrelated behavior is represented as covered.

## Security and Safety Rules
- Use authorized environments and synthetic inputs.
- Do not invoke destructive endpoints, mutate production data, or trigger external side effects without explicit approval.
- Redact credentials and personal data from requests, logs, and evidence.
- Stop if target identity or side effects cannot be determined safely.
