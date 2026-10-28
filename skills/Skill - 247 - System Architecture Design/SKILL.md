---
name: Skill - 247 - System Architecture Design
description: Use when designing high-level system structures, defining microservice boundaries, establishing ADRs, evaluating cross-layer communication protocols, or decoupling monolithic codebases.
---

# Skill - 247 - System Architecture Design

## Purpose and Scope
Formulate, evaluate, and document enterprise software architectures, microservice boundaries, data flow topologies, and technology selections. Ensures systems maintain high cohesion, loose coupling, deterministic state boundaries, and maintainable cross-layer communication contracts.

## Trigger Conditions
- User requests an architectural design for a new project or subsystem.
- Establishing microservice boundaries between backend APIs, AI engines, and frontend clients.
- Creating Architecture Decision Records (ADRs) to document pivotal technical tradeoffs.
- Refactoring tightly coupled monolithic systems into distributed or tiered services.

## Non-Trigger Conditions
- Do not trigger for minor bugfixes, routine endpoint implementation, or CSS styling.
- Do not trigger for low-level algorithm optimization within a single function (use `clean-code-refactoring`).
- Do not trigger for database indexing or query tuning (use `database-architecture-migration`).

## Prerequisites and Inputs
- Functional requirements and user journey specifications.
- Non-functional requirements (latency, throughput, concurrency, security boundaries, deployment constraints).
- Inventory of candidate technologies, runtimes, and persistence options.

## Execution Workflow
1. **Requirements & Constraint Analysis**:
   - Classify requirements into functional capabilities and non-functional bounds ($O(1)$/$O(n)$ metrics, availability targets, regulatory compliance).
2. **Tier & Domain Boundary Definition**:
   - Establish service tiers: Presentation (SPA/Mobile), Orchestration Gateway (REST/BFF), Business Logic, Computation Service (AI/CAS), Persistence.
   - Enforce unidirectional dependency rules: High-level policies must not depend on low-level implementation details.
3. **Communication Protocol Selection**:
   - Synchronous REST / JSON over HTTP for request-response state queries.
   - Server-Sent Events (SSE) or WebSockets for real-time calculation progress and AI token streaming.
   - Constant-time HMAC headers (`X-Internal-Key`) or mTLS for internal microservice authentication.
4. **Failure Domain & Resilience Modeling**:
   - Implement circuit breakers, timeouts, and exponential backoff retry patterns for external LLM or cloud API interactions.
   - Decouple compute-heavy jobs (model training, matrix elimination) via background workers or asynchronous task queues.
5. **ADR Documentation**:
   - Capture Title, Status, Context, Decision, and Consequences for each architectural choice.

## Commands and Examples
```markdown
# Architectural Decision Record (ADR) Template:

## ADR-001: Separation of Neuro-Symbolic Math Engine from Generative LLM
- **Status:** Accepted
- **Context:** Large Language Models exhibit hallucinations and sign reversal anomalies in quantitative tasks.
- **Decision:** Decouple natural language intent classification from mathematical computation. Route parsed AST nodes to deterministic Java/SymPy computing engines.
- **Consequences:** Eliminates calculation hallucinations; requires building a formal Pratt parser and AST compiler.
```

## Deliverables and Outputs
- `ARCHITECTURE.md`: High-level system design document with Mermaid sequence and component diagrams.
- `docs/adr/ADR-xxx.md`: Concrete Architecture Decision Records documenting key technical choices.
- Interface contract definitions (OpenAPI specifications, JSON Schema definitions).

## Quality Gates and Acceptance Criteria
- Service boundaries clearly delineate data ownership and persistence responsibilities.
- No circular dependencies across architectural modules or microservice endpoints.
- High-compute operations are prevented from blocking synchronous HTTP request threads.

## Security and Safety Rules
- Defense-in-depth: Never trust client input; validate at the gateway and the domain service.
- Microservice isolation: Internal endpoints must not be exposed directly to the public Internet without gateway authentication.
- Zero-trust network communication between microservices using internal secret verification.
