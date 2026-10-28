---
name: Skill - 150 - Clean Code Refactoring
description: Use when refactoring messy, tightly coupled, or duplicated code, eliminating technical debt, enforcing SOLID principles, or applying clean code conventions across Java, Python, and TypeScript.
---

# Skill - 150 - Clean Code Refactoring

## Purpose and Scope
Refactor legacy, duplicated, complex, or brittle code into clean, maintainable, modular, and idiomatic components without altering external behavior. Enforces SOLID principles, eliminates code smells, reduces cyclomatic complexity, and ensures strict type safety across Java, Python, TypeScript, and modern enterprise stacks.

## Trigger Conditions
- Code review identifies architectural smells (God classes, long methods, magic numbers, deep nesting).
- Reducing technical debt and removing dead code.
- Restructuring tightly coupled classes into testable, dependency-injected interfaces.
- Standardizing naming conventions, formatting, and docstrings across a repository.

## Non-Trigger Conditions
- Do not trigger when adding major new functional features (use `backend-spring-microservices` or `frontend-spa-engineering`).
- Do not trigger if automated tests do not exist to protect against behavioral regression (write tests first via `qa-test-automation-strategy`).
- Do not trigger for database migration refactors (use `database-architecture-migration`).

## Prerequisites and Inputs
- Existing working source code.
- Baseline automated unit test suite passing 100% to guarantee zero behavioral regressions.
- Language compiler/linter configured (e.g. Checkstyle, SonarLint, flake8, ruff, ESLint).

## Execution Workflow
1. **Regression Baseline Verification**:
   - Run existing unit tests to confirm the current implementation passes 100%. If tests are missing, author safety tests before touching code.
2. **Code Smell & Anti-Pattern Identification**:
   - Identify targets: Long Methods (>30 lines), High Cyclomatic Complexity (>10 branches), Feature Envy, Primitive Obsession, Duplicated Logic.
3. **Incremental Micro-Refactorings**:
   - Apply Martin Fowler's atomic refactoring steps:
     - Extract Method / Extract Class
     - Replace Magic Number with Typed Constant
     - Introduce Parameter Object / Record
     - Decompose Conditional Logic into Strategy Pattern or Polymorphism
     - Rename Variables and Methods for High Domain Expressiveness
4. **Compile & Re-verify Continuously**:
   - Run the compiler and unit tests after each microscopic refactoring step. Immediately revert if any check breaks.
5. **Static Analysis & Linting Audit**:
   - Verify code formatting, import sorting, and lint rule compliance.

## Commands and Examples
```powershell
# Java: Run Maven surefire unit tests during refactoring
mvn test -Dtest=AgentServiceTest

# Python: Check formatting and linting
python -m ruff check app/
python -m unittest discover -s tests -v

# TypeScript / Angular: Run linter
npm run lint
```

```java
// Before: Primitive Obsession & Deep Nesting
public Map<String, Object> execute(String userId, String conversationId, Map<String, Object> args) { ... }

// After: Idiomatic Java 21 Record Encapsulation
public record ToolContext(String userId, String conversationId) {}
public Map<String, Object> execute(ToolContext ctx, Map<String, Object> args) { ... }
```

## Deliverables and Outputs
- Refactored source code files with improved readability, testability, and cohesion.
- Zero behavioral changes; existing test suite passes cleanly.
- Reduced cyclomatic complexity and cleaner module boundaries.

## Quality Gates and Acceptance Criteria
- 100% of existing unit tests pass before and after the refactoring.
- Cyclomatic complexity per method reduced below established thresholds (typically $\le 10$).
- No compiler warnings or linting violations introduced.

## Security and Safety Rules
- Preserve all existing security validation checks, permission gates, and input sanitization routines.
- Never bypass or delete an existing test to make a refactored class compile.
