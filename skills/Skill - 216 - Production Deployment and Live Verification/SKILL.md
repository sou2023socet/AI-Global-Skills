---
name: Skill - 216 - Production Deployment and Live Verification
description: Use when executing production releases, conducting post-deployment smoke tests, verifying health probes, managing rollbacks, or validating live system availability.
---

# Skill - 216 - Production Deployment and Live Verification

## Purpose and Scope
Execute, verify, and validate production software releases and infrastructure deployments. Enforces zero-downtime rollout strategies (Blue/Green, Rolling updates, Canary), automated post-deployment smoke verification, live service health monitoring, and deterministic rollback procedures.

## Trigger Conditions
- Deploying a verified build artifact into production, staging, or UAT environments.
- Executing post-deployment smoke tests against live service endpoints.
- Verifying container and microservice health probes (`/actuator/health`, `/health`).
- Initiating an automated or manual rollback upon detecting post-deploy anomalies.
- Validating zero-downtime service transition.

## Non-Trigger Conditions
- Do not trigger for local development unit test runs (use `qa-test-automation-strategy`).
- Do not trigger for authoring Dockerfiles or Compose files (use `devops-container-orchestration`).
- Do not trigger without explicit human authorization for production modification.

## Prerequisites and Inputs
- Fully built, packaged, and verified release artifacts (JARs, container images, UI bundles).
- Environment target URLs, ports, and configuration credentials.
- Rollback plan and previous stable release artifact identifiers.

## Execution Workflow
1. **Pre-Deployment Gate & Approval**:
   - Verify that all automated CI tests and security scans have passed.
   - Require explicit human signoff specifying target version, environment, and rollback procedure.
2. **Database Migration Pre-Flight**:
   - Execute Flyway migrations in non-destructive, backward-compatible mode before rolling out new application code.
3. **Staged Service Rollout**:
   - Deploy services in topological order: Persistence $\rightarrow$ AI Microservices $\rightarrow$ Backend Gateways $\rightarrow$ Reverse Proxy / UI.
   - Maintain prior running instance until the new instance passes health probes.
4. **Live Smoke Testing & Probe Verification**:
   - Query liveness and readiness probes:
     - Backend: `GET /actuator/health` $\rightarrow$ expect `{"status": "UP"}`.
     - AI Service: `GET /health` $\rightarrow$ expect `{"status": "ok"}`.
     - Frontend: `GET /` $\rightarrow$ expect HTTP 200 with valid index HTML bundle.
   - Execute synthetic transaction: Login $\rightarrow$ Create Conversation $\rightarrow$ Execute lightweight read-only tool query.
5. **Rollback Trigger & Recovery**:
   - If health probes fail or error rate spikes, halt rollout and immediately trigger rollback to previous stable artifact.

## Commands and Examples
```powershell
# Verify Spring Boot health probe
Invoke-RestMethod -Uri "http://localhost:8080/actuator/health"

# Verify FastAPI AI service health probe
Invoke-RestMethod -Uri "http://localhost:8000/health"

# Execute synthetic smoke test transaction
$login = Invoke-RestMethod -Method Post -Uri "http://localhost:8080/api/auth/login" -ContentType "application/json" -Body '{"email":"test@example.com","password":"password123"}'
Write-Host "Auth Token acquired: $($login.token.Substring(0, 10))..."
```

## Deliverables and Outputs
- `docs/DEPLOYMENT_VERIFICATION_<version>.md`: Smoke test report documenting probe responses and synthetic transactions.
- Active, verified live production service.
- Documented rollback verification evidence.

## Quality Gates and Acceptance Criteria
- 100% of service health probes return healthy status codes within 30 seconds of launch.
- Synthetic transaction completes with valid data and zero 5xx server errors.
- Rollback procedure verified and capable of executing within <2 minutes.

## Security and Safety Rules
- Production deployment commands must never run autonomously without explicit, user-confirmed approval.
- Secrets used during deployment must be injected dynamically via secure vaults or environment files and never logged to console.
