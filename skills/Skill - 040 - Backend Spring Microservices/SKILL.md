description: 'Apply the source-derived Backend Spring Microservices capability.'
---
id: backend-spring-microservices
name: Skill - 040 - Backend Spring Microservices
version: 1.0.0
status: structurally_validated
source: global-skills:skills\backend-spring-microservices\SKILL.md
---

# Skill - 040 - Backend Spring Microservices

## Purpose
Apply the reusable Backend Spring Microservices capability to the named project task without
silently expanding scope or permissions.

## Activation
- Activate when the task explicitly requires Backend Spring Microservices.
- Confirm project identity, scope, required evidence, and permission boundaries first.
- Do not activate for unrelated work or when a more specific canonical skill owns the task.

## Required procedure
1. Inspect the project context, applicable contracts, and existing implementation before acting.
2. Follow the source capability contract below, adapting examples to the actual project.
3. Record inputs, decisions, outputs, evidence, failures, and unresolved limitations.
4. Validate the acceptance criteria with the smallest approved check; never claim an unrun check.

## Failure handling
Stop on missing prerequisites, unknown project identity, unsafe permissions, or contradictory
evidence. Preserve partial work, report the exact blocker, and return control to the
orchestrator rather than inventing a successful result.

## Permissions
Read-only inspection is the default. File changes require task scope; execution, external
access, persistent writes, production impact, and generated artifacts require explicit
command-scoped approval.

## Acceptance criteria
- The requested capability is applied to the identified project and scope.
- Outputs are actionable, traceable to evidence, and free of secrets.
- Failures and unverified steps are explicit.

## Source capability contract

The following source-preserving contract is the basis for this canonical package:

# Backend Spring Microservices Engineering

## Purpose and Scope
Architect, develop, secure, and maintain high-performance enterprise backend microservices using Java 21 LTS and Spring Boot 3.x. Enforces clean architectural separation (Web Controllers, Service Orchestrators, Domain Entities, Spring Data JPA Repositories), stateless JWT authentication, exception handling, and tool execution boundaries.

## Trigger Conditions
- Implementing or modifying Spring Boot REST controllers, services, or repository layers.
- Configuring Spring Security 6 filter chains and JWT stateless token authentication.
- Implementing Java agent tools conforming to the `AgentTool` interface.
- Integrating backend services with internal Python AI microservices via HTTP clients.
- Resolving dependency injection, circular bean references, or transaction management issues.

## Non-Trigger Conditions
- Do not trigger for frontend Angular component development (use `frontend-spa-engineering`).
- Do not trigger for Python AI microservice internal logic (use `mlops-llm-pipeline-engineering`).
- Do not trigger for raw database engine configuration (use `database-architecture-migration`).

## Prerequisites and Inputs
- Java Development Kit (JDK 21 LTS) installed.
- Apache Maven 3.9+ or Gradle build toolchain.
- Project `pom.xml` with Spring Boot 3.3+ dependencies.
- Database access configuration (PostgreSQL/MySQL/H2).

## Execution Workflow
1. **Layered Module Architecture**:
   - `web/`: `@RestController` classes handling HTTP mapping and DTO validation.
   - `service/`: `@Service` classes holding domain logic, transaction boundaries (`@Transactional`), and agent orchestration.
   - `domain/`: JPA entities mapping to relational tables.
   - `repo/`: `JpaRepository` interfaces with optimized Spring Data query methods.
   - `tools/`: Java agent tools implementing the `AgentTool` contract.
2. **Stateless Security Filter Chain**:
   - Configure `SecurityFilterChain` bean: disable CSRF for stateless APIs, set session management to `STATELESS`, authorize public auth endpoints (`/api/auth/**`), and protect all other `/api/**` routes with a custom `JwtAuthFilter`.
3. **Agent Loop Orchestration**:
   - Implement orchestrator loop: Gather tool schemas (Java + Python `/v1/tools`) $\rightarrow$ Call AI microservice $\rightarrow$ If tool calls returned, check approval status $\rightarrow$ Execute approved tools or record `PENDING_APPROVAL` $\rightarrow$ Feed results back to model (up to `maxSteps`).
4. **Centralized Exception Handling**:
   - Provide `@RestControllerAdvice` capturing domain exceptions and mapping them to standard HTTP status codes (e.g. 400 for bad input, 401 for bad auth, 404 for missing entities, 409 for conflicts).
5. **Configuration Parameterization**:
   - Use `@ConfigurationProperties` to bind properties type-safely from `application.yml`.

## Commands and Examples
```powershell
# Compile and run unit tests via Maven
mvn test

# Package Spring Boot executable JAR
mvn clean package -DskipTests

# Run local Spring Boot application
mvn spring-boot:run
```

```java
// Spring Boot Agent Tool Pattern
@Component
public class ConversationStatsTool implements AgentTool {
    private final ConversationRepository conversations;
    public ConversationStatsTool(ConversationRepository c) { this.conversations = c; }

    @Override public String name() { return "conversation_stats"; }
    @Override public String description() { return "Returns the user's total conversation count."; }
    @Override public Map<String, Object> parameters() {
        return Map.of("type", "object", "properties", Map.of());
    }
    @Override public Map<String, Object> execute(ToolContext ctx, Map<String, Object> args) {
        long count = conversations.countByUserId(ctx.userId());
        return Map.of("conversationCount", count);
    }
}
```

## Deliverables and Outputs
- Spring Boot `@RestController`, `@Service`, and `@Component` classes.
- Security configuration classes and JWT authentication filters.
- Passing Mockito unit tests in `src/test/java/`.

## Quality Gates and Acceptance Criteria
- Code compiles cleanly with zero errors on JDK 21 and Spring Boot 3.3+.
- All unit and mock tests pass (`mvn test`).
- No sensitive database passwords or JWT secrets hardcoded in source or `application.yml`.

## Security and Safety Rules
- Enforce strict parameter validation on all incoming controller requests using `@Valid`.
- Validate caller ownership on entity queries to prevent Insecure Direct Object References (IDOR).
