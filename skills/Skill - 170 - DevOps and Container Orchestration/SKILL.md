---
name: Skill - 170 - DevOps and Container Orchestration
description: Use when authoring multi-stage Dockerfiles, writing Docker Compose orchestration files, configuring Nginx reverse proxies, setting up CI/CD pipelines, or troubleshooting container networking.
---

# Skill - 170 - DevOps and Container Orchestration

## Purpose and Scope
Architect, containerize, orchestrate, and automate multi-tier distributed software environments using Docker, Docker Compose, Nginx reverse proxies, and CI/CD pipelines (GitHub Actions, GitLab CI). Enforces multi-stage image optimization, non-root container security, service dependency ordering, healthcheck probes, and isolated virtual networks.

## Trigger Conditions
- Creating or optimizing Dockerfiles for Java, Python, or Angular frontend applications.
- Authoring or troubleshooting `docker-compose.yml` multi-container deployments.
- Configuring Nginx reverse proxies with API routing, SSL termination, and Content Security Policies.
- Resolving container-to-container networking issues (DNS resolution, port mapping, internal hostnames).
- Designing CI/CD automated build and test pipelines.

## Non-Trigger Conditions
- Do not trigger for application-internal Java or Python business logic.
- Do not trigger for raw database query tuning (use `database-architecture-migration`).
- Do not trigger for live cloud infrastructure provisioning (use `production-deployment-verification`).

## Prerequisites and Inputs
- Docker Engine and Docker Compose CLI installed.
- Target application components (Backend JAR, Python virtual environment, Angular production build).
- Environment configuration file (`.env`) with parameter bindings.

## Execution Workflow
1. **Multi-Stage Dockerfile Design**:
   - Backend (Java): Builder stage (`maven:3.9-eclipse-temurin-21`) $\rightarrow$ Runtime stage (`eclipse-temurin:21-jre-alpine`).
   - AI Service (Python): Builder stage $\rightarrow$ Runtime stage (`python:3.12-slim`).
   - Frontend (Angular): Node build stage (`node:22-alpine`) $\rightarrow$ Nginx web server stage (`nginx:1.27-alpine`).
2. **Container Security Hardening**:
   - Run container processes as non-root users (`USER appuser`).
   - Strip build tools, compilers, and development headers from final production images.
3. **Docker Compose Multi-Tier Orchestration**:
   - Define services: `postgres`, `ai-service`, `backend`, `frontend`.
   - Enforce healthchecks and dependency sequencing (`depends_on: { postgres: { condition: service_healthy } }`).
   - Bind internal microservices to a private bridge network; expose only necessary gateway ports (80/443 or 8088).
4. **Nginx Reverse Proxy Configuration**:
   - Forward `/api/` traffic to Spring Boot backend (`http://backend:8080`).
   - Route `/` client requests to compiled Angular static files with `try_files $uri $uri/ /index.html`.
   - Enforce HTTP security headers (CSP, HSTS, X-Frame-Options).
5. **Configuration Parameterization**:
   - Pass environment variables dynamically via `docker-compose.yml` reading from `.env`.

## Commands and Examples
```powershell
# Build and launch all multi-container services in detached mode
docker compose up -d --build

# View real-time container logs with service filtering
docker compose logs -f backend ai-service

# Check health status and port bindings of running containers
docker compose ps
```

```dockerfile
# Multi-stage Java Dockerfile Example
FROM maven:3.9.12-eclipse-temurin-21 AS build
WORKDIR /app
COPY pom.xml .
RUN mvn dependency:go-offline
COPY src ./src
RUN mvn clean package -DskipTests

FROM eclipse-temurin:21-jre-alpine
WORKDIR /app
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
COPY --from=build /app/target/*.jar app.jar
USER appuser
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]
```

## Deliverables and Outputs
- Optimized, multi-stage `Dockerfile` files for each microservice.
- Validated `docker-compose.yml` file with health checks and volume mappings.
- Hardened `nginx.conf` reverse proxy configuration.
- CI/CD workflow manifests (`.github/workflows/*.yml`).

## Quality Gates and Acceptance Criteria
- All containers build cleanly and boot into `healthy` status via `docker compose up`.
- Zero hardcoded secrets in Dockerfiles or checked-in Compose files.
- Production container images minimize layer footprints and eliminate unnecessary build tools.

## Security and Safety Rules
- Containers must never run as root in production environments.
- Internal service ports (e.g. database port 5432, internal AI key port 8000) must not be exposed to the public host unless strictly necessary for debugging.
