---
name: Skill - 241 - SDLC Planning and Governance
description: Use when planning project milestones, defining stage gates, establishing risk management policies, tracking traceability, or organizing multi-phase development roadmaps.
---

# Skill - 241 - SDLC Planning and Governance

## Purpose and Scope
Establish predictable, disciplined Software Development Life Cycle (SDLC) governance across enterprise software projects. Provides milestone planning, stage-gate checklists, risk ownership matrices, requirements traceability, and progress tracking to ensure software is built incrementally with empirical verification.

## Trigger Conditions
- Initiating a multi-task software development initiative (e.g. 7-task delivery milestones).
- Defining formal stage gates for transitioning from discovery to implementation to production.
- Establishing requirements traceability matrices linking user stories to tests.
- Auditing project velocity, blockers, and compliance against architectural governance policies.

## Non-Trigger Conditions
- Do not trigger for ad-hoc single-line coding questions.
- Do not trigger for technical troubleshooting of runtime build errors (use `diagnostic-debugging-rootcause`).
- Do not trigger for standalone Git release tagging (use `production-deployment-verification`).

## Prerequisites and Inputs
- Project charter, functional requirements, or system specification.
- Target release milestones and delivery deadlines.
- Known technical, compliance, or operational constraints.

## Execution Workflow
1. **Work Breakdown Structure (WBS)**:
   - Decompose high-level goals into sequential, testable task increments (e.g., Task 1: Audit, Task 2: Skills, Task 3: Infrastructure, Task 4: Core, Task 5: Integration, Task 6: Verification, Task 7: Release).
2. **Stage Gate Definition**:
   - Establish strict entry and exit criteria for each phase:
     - *Gate 1 (Discovery & Audit)*: Verified baseline report completed; no application code changed.
     - *Gate 2 (Skills & Architecture)*: Reusable skills repository initialized; contracts specified.
     - *Gate 3 (Implementation)*: Unit tests pass 100%; zero compiler warnings.
     - *Gate 4 (Production Readiness)*: Security scan clean; smoke tests verified.
3. **Risk & Ownership Assessment**:
   - Identify risks across Technical, Operational, and Security dimensions.
   - Assign mitigation strategies, probability, impact, and rollback procedures.
4. **Requirements Traceability Matrix (RTM)**:
   - Map each functional requirement (FR-xxx) to architectural components and automated test cases.
5. **Progress & Governance Logging**:
   - Document completed milestones, verified deliverables, and pending tasks in persistent markdown logs.

## Commands and Examples
```markdown
# Requirements Traceability Matrix (RTM) Template:

| Req ID | Requirement Description | Architecture Module | Test Suite / Verification | Status |
|---|---|---|---|---|
| FR-01 | User authentication via JWT | `AuthService.java` | `AuthServiceTest.java` | Verified |
| FR-02 | AST security analysis | `codegen.py` | `test_core.py:test_codegen` | Verified |
| FR-03 | Approval-gated LM training | `AgentService.java` | `AgentServiceTest.java` | Verified |
```

## Deliverables and Outputs
- `docs/SDLC_PLAN.md` or `ROADMAP.md`: Sequenced project milestones with acceptance gates.
- `docs/REQUIREMENTS_TRACEABILITY.md`: Bidirectional requirement-to-test mapping matrix.
- `docs/RISK_MANAGEMENT.md`: Risk register with severity ratings and mitigation actions.

## Quality Gates and Acceptance Criteria
- Every milestone has explicit, objective completion criteria (not subjective claims).
- Progression to the next stage is strictly blocked until current gate exit criteria are satisfied.
- Blockers and unverified assumptions are explicitly highlighted.

## Security and Safety Rules
- Risk assessments must evaluate credential exposure, denial-of-service risks, and data corruption scenarios.
- Stage gates must require security scanning and code review before release signoff.
