---
name: Skill - 171 - Diagnostic Debugging and Root-Cause Analysis
description: Use when investigating runtime errors, diagnosing server crashes, parsing complex exception stacktraces, analyzing application logs, or conducting root-cause analysis (RCA).
---

# Skill - 171 - Diagnostic Debugging and Root-Cause Analysis

## Purpose and Scope
Perform systematic, evidence-driven diagnostic investigations into application bugs, runtime crashes, unexpected HTTP status codes, performance regressions, and intermittent failures. Isolates the definitive root cause through log tracing, state inspection, and reproducible minimal test cases, preventing symptom-masking hacks.

## Trigger Conditions
- Application throws uncaught exceptions (e.g. `NullPointerException`, `ConnectionRefused`, `SyntaxError`, `IndexOutOfBounds`).
- Backend returns unexpected HTTP 4xx or 5xx status codes.
- Diagnostic logs reveal unexpected behavior, deadlocks, or gateway timeouts.
- User requests debugging of a specific failure scenario or intermittent bug.

## Non-Trigger Conditions
- Do not trigger for proactive performance profiling without a manifested failure (use `performance-profiling-scalability`).
- Do not trigger for general code cleanup or refactoring (use `clean-code-refactoring`).
- Do not trigger for broad architectural redesign (use `system-architecture-design`).

## Prerequisites and Inputs
- Raw error output, stacktrace, log file, or HTTP response payload.
- Source code of the affected module and its dependency tree.
- Access to diagnostic logging or terminal execution output.

## Execution Workflow
1. **Error Capture & Triage**:
   - Extract the root cause exception from the top or bottom of the stacktrace (e.g. `Caused by:` in Java, innermost traceback in Python).
   - Identify the exact file path, class/module, and line number where failure occurred.
2. **State & Input Reconstruction**:
   - Determine the runtime parameters, arguments, or environment variables that triggered the error.
   - Differentiate between environmental failures (bad database port, missing variable) and algorithmic logic bugs (off-by-one, null dereference).
3. **Reproduction in Isolation**:
   - Construct a minimal, reproducible unit test or standalone script reproducing the exact failure without external service dependencies.
4. **Root Cause Analysis (RCA)**:
   - Apply the "5 Whys" methodology to determine why the boundary condition was unhandled.
   - Inspect whether preconditions were improperly validated upstream.
5. **Targeted Remediation & Verification**:
   - Implement the smallest safe fix addressing the root cause.
   - Run the reproduction test to verify the fix eliminates the error cleanly without regressions.
6. **Post-Mortem Documentation**:
   - Document the bug mechanism, root cause, fix, and preventative recommendations.

## Commands and Examples
```powershell
# Windows: Search application log files for ERROR and WARN events
Get-Content .\backend\logs\spring.log | Select-String -Pattern "ERROR|Exception" -Context 2, 5

# Trace TCP socket connection failure to database
Test-NetConnection -ComputerName localhost -Port 5432
```

```bash
# POSIX: Grep recent stacktraces
grep -rn -C 5 "Traceback" ai-service/logs/
```

## Deliverables and Outputs
- `docs/RCA_<issue-id>.md`: Root Cause Analysis document detailing symptom, timeline, root cause, fix, and verification.
- Targeted code fix in the affected source file.
- Automated regression test added to the test suite to prevent recurrence.

## Quality Gates and Acceptance Criteria
- The bug is deterministically reproduced before the fix and proven resolved after the fix.
- The fix addresses the underlying root cause rather than merely catching and suppressing the exception.
- All existing unit and integration tests continue to pass with zero regressions.

## Security and Safety Rules
- Redact user passwords, bearer tokens, and PII from error logs and RCA reports.
- Do not mask security exceptions or bypass permission gates to silence an authorization error.
