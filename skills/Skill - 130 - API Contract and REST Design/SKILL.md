---
name: Skill - 130 - API Contract and REST Design
description: Use when designing RESTful API endpoints, crafting OpenAPI/Swagger specifications, establishing request/response DTO contracts, or standardizing error response envelopes.
---

# Skill - 130 - API Contract and REST Design

## Purpose and Scope
Design, specify, standardize, and maintain robust RESTful API contracts, OpenAPI/Swagger specifications, JSON schemas, Data Transfer Objects (DTOs), and predictable HTTP error envelopes. Ensures cross-layer consistency between frontend clients, API gateways, and microservices.

## Trigger Conditions
- Designing new REST endpoints or modifying existing API payloads.
- Authoring or updating OpenAPI 3.0+ specifications.
- Defining strongly typed request/response DTOs in Java (Records) or TypeScript (Interfaces).
- Resolving contract mismatches between backend responses and frontend client models.

## Non-Trigger Conditions
- Do not trigger for database schema modeling (use `database-architecture-migration`).
- Do not trigger for frontend state management without API contract changes (use `frontend-spa-engineering`).
- Do not trigger for network proxy routing (use `devops-container-orchestration`).

## Prerequisites and Inputs
- Functional requirement specifying the data exchange format and required parameters.
- Target endpoints and HTTP methods (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`).
- Existing API versioning conventions (e.g. `/api/v1/...`).

## Execution Workflow
1. **Resource URI & Method Modeling**:
   - Design nouns-based, hierarchical REST URIs (e.g., `/api/conversations/{id}/messages`).
   - Map operations strictly to standard HTTP semantics (`GET` for idempotent queries, `POST` for creation, `DELETE` for removal).
2. **DTO Contract Specification**:
   - Java: Define immutable Java 21 Records for request bodies and response projections.
   - TypeScript: Mirror DTOs as clean interfaces in `core/models.ts`.
   - Enforce Jakarta Bean Validation annotations (`@NotBlank`, `@Size`, `@Email`).
3. **Standardized Error Envelope**:
   - Standardize on RFC 7807 (Problem Details) or clean enterprise error envelopes:
     `{"timestamp": "...", "status": 400, "error": "Bad Request", "message": "...", "path": "..."}`.
4. **Internal Microservice Header Contracts**:
   - For internal service-to-service calls, mandate constant-time header authentication (`X-Internal-Key`) and correlation IDs (`X-Correlation-Id`).
5. **Contract Verification**:
   - Validate that status codes conform to standards: `200 OK`, `201 CREATED`, `204 NO CONTENT`, `400 BAD REQUEST`, `401 UNAUTHORIZED`, `403 FORBIDDEN`, `404 NOT FOUND`, `409 CONFLICT`.

## Commands and Examples
```java
// Java 21 Record DTO Example
public record ChatRequest(
    String conversationId,
    @NotBlank(message = "Message cannot be empty") String message,
    Set<String> approvedTools,
    String provider
) {}

public record ChatResponse(
    String conversationId,
    String reply,
    String provider,
    String model,
    List<ToolCallInfo> toolCalls,
    List<PendingApproval> pendingApprovals
) {}
```

```typescript
// TypeScript Client Interface Mirror
export interface ChatRequest {
  conversationId?: string;
  message: string;
  approvedTools?: string[];
  provider?: string;
}
```

## Deliverables and Outputs
- `docs/API.md` or `openapi.yaml`: Comprehensive REST contract documentation.
- Java request/response Record DTO classes with Jakarta validation.
- Matching TypeScript interface definitions in client core libraries.

## Quality Gates and Acceptance Criteria
- All request parameters have explicit validation rules and type constraints.
- Frontend and backend DTO schemas match 100% field-for-field without serialization errors.
- Internal service calls strictly require HMAC authentication headers.

## Security and Safety Rules
- Never expose internal database entity IDs or sensitive credentials in API DTOs.
- Sanitize error messages; never return database stacktraces or SQL snippets to external clients.
