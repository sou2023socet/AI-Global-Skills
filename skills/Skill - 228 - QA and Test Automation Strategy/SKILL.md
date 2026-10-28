---
name: Skill - 228 - QA and Test Automation Strategy
description: Use when designing testing pyramids, authoring unit and integration tests, configuring test frameworks (JUnit, Mockito, pytest, Jasmine/Karma), or establishing automated quality gates.
---

# Skill - 228 - QA and Test Automation Strategy

## Purpose and Scope
Architect, implement, and maintain automated testing suites across all layers of the testing pyramid (Unit, Slice, Integration, End-to-End, and Contract). Ensures software reliability, regression resistance, boundary condition verification, and high test coverage across Java, Python, and Angular/TypeScript environments.

## Trigger Conditions
- Adding unit or integration test coverage to untested modules or legacy codebases.
- Implementing test slices (e.g. `@WebMvcTest`, `@DataJpaTest`, MockMvc) in Spring Boot.
- Implementing Python test fixtures and parameterized test suites (`unittest`, `pytest`).
- Configuring Angular frontend test runners (Jasmine, Karma, Jest, or Vitest) for components and services.
- Verifying agent tool loops, human approval denial flows, and error handling.

## Non-Trigger Conditions
- Do not trigger for manual, unrepeatable ad-hoc testing.
- Do not trigger for live production monitoring or post-deploy health checks (use `production-deployment-verification`).
- Do not trigger for static security scanning (use `appsec-devsecops-hardening`).

## Prerequisites and Inputs
- Target source code and module interfaces.
- Testing libraries installed in project manifests (`pom.xml`, `requirements.txt`, `package.json`).
- Mocking libraries available (Mockito, unittest.mock, ts-mockito).

## Execution Workflow
1. **Test Strategy & Pyramid Formulation**:
   - Establish ratio: 70% Unit tests (in-memory, fast, deterministic), 20% Integration/Slice tests (HTTP, DB, MockMvc), 10% E2E tests.
2. **Boundary & Equivalence Partitioning**:
   - For every method, identify: Valid normal inputs, Boundary limits (0, max values), Null/Empty inputs, Malformed/Unexpected types, and Gated/Unauthorized inputs.
3. **Unit Test Implementation**:
   - Follow the **Arrange-Act-Assert (AAA)** or Given-When-Then pattern.
   - Java: Use JUnit 5 and Mockito for dependency isolation.
   - Python: Use `unittest.TestCase` or `pytest` with parameterized test cases.
   - Angular: Test standalone components and RxJS services using `TestBed`.
4. **Integration & Approval Gate Verification**:
   - Test agent loops for: Normal tool execution, approval denial halt (`PENDING_APPROVAL`), unknown tool handling, and error output clamping.
5. **Coverage & Regression Execution**:
   - Run tests with coverage tracking to ensure zero broken builds.

## Commands and Examples
```powershell
# Java: Run Spring Boot Maven test suite
mvn test

# Python: Discover and run all unit tests with verbose reporting
python -m unittest discover -s tests -t . -v

# Angular: Run unit tests with headless browser
npm test -- --watch=false --browsers=ChromeHeadless
```

```java
// Java: Mockito Unit Test for Agent Approval Gate
@Test
void unapprovedToolHaltsExecution() {
    when(aiClient.chat(any())).thenReturn(new ChatResponse("Running tool", List.of(new ToolCall("train", Map.of()))));
    AgentResult result = agentService.run("Train model", Set.of()); // Empty approvals
    assertEquals(1, result.pendingApprovals().size());
    verify(toolRepo, never()).execute(any(), any());
}
```

## Deliverables and Outputs
- `*Test.java`, `test_*.py`, and `*.spec.ts` test files.
- Verified test execution reports showing 100% pass rates.
- Code coverage summaries highlighting tested code paths.

## Quality Gates and Acceptance Criteria
- 100% of newly authored tests pass deterministically without flaky or timing-dependent failures.
- Tests must be isolated and self-contained; no test may depend on the execution order of other tests.
- Mocking is strictly restricted to external boundaries; domain logic must be verified directly.

## Security and Safety Rules
- Never use live production databases or production credentials in automated test fixtures.
- Use in-memory mocks, Testcontainers, or dedicated ephemeral test databases.
