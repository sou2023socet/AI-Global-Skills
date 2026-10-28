---
name: Skill - 157 - Database Architecture and Migration
description: Use when designing database schemas, writing Flyway/Liquibase migration scripts, configuring connection pooling (HikariCP), modeling entities, or optimizing SQL queries.
---

# Skill - 157 - Database Architecture and Migration

## Purpose and Scope
Architect, model, evolve, and maintain robust persistence layers across relational (PostgreSQL, MySQL) and document-oriented (MongoDB) databases. Enforces idempotent schema migrations, entity mapping, indexing strategies, referential integrity, and connection pool optimization.

## Trigger Conditions
- Creating new database entities, tables, indexes, or relationships.
- Writing or refactoring Flyway migration scripts (`V1__init.sql`, `V2__...sql`).
- Configuring database connection pools (HikariCP) and Spring Data JPA repositories.
- Optimizing slow queries, eliminating N+1 select bottlenecks, or adding missing indexes.
- Resolving connection failures or database configuration drift in containerized environments.

## Non-Trigger Conditions
- Do not trigger for purely in-memory data caching without persistence changes.
- Do not trigger for destructive schema wipes or unverified production drops.
- Do not trigger for frontend form modeling (use `frontend-spa-engineering`).

## Prerequisites and Inputs
- Target database engine and version (e.g. PostgreSQL 16 Alpine, MongoDB 7).
- Relational schema model or entity requirements.
- Migration framework configured (Flyway, Liquibase).
- Active or template database connection parameters.

## Execution Workflow
1. **Schema & Entity Modeling**:
   - Design normalized relational tables ($3^{rd}$ Normal Form) with primary keys (`UUID` or `BIGSERIAL`), foreign keys, and cascading delete policies.
   - Java: Model entities using JPA/Hibernate (`@Entity`, `@Table`, `@Id`, `@Enumerated`).
2. **Flyway Migration Script Authoring**:
   - Create strictly versioned, immutable migration scripts in `src/main/resources/db/migration/` (e.g. `V1__init.sql`).
   - Use idempotent SQL constructs (`CREATE TABLE IF NOT EXISTS`, `CREATE INDEX IF NOT EXISTS`).
3. **Audit Trail & Metadata Tables**:
   - Ensure auditing tables (e.g. `tool_runs`, `audit_logs`) capture timestamps, user identities, operation statuses, and JSON argument payloads.
4. **Connection Pool & Timeout Tuning**:
   - Configure HikariCP in `application.yml` (`maximum-pool-size: 10`, `connection-timeout: 20000`, `idle-timeout: 300000`).
5. **Configuration Parameterization**:
   - Bind database host and port to environment variables (`${DB_URL:jdbc:postgresql://localhost:5432/db}`) to ensure container compatibility.

## Commands and Examples
```sql
-- Flyway Migration Example: V1__init.sql
CREATE TABLE IF NOT EXISTS users (
    id VARCHAR(36) PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    display_name VARCHAR(100) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS tool_runs (
    id VARCHAR(36) PRIMARY KEY,
    tool_name VARCHAR(100) NOT NULL,
    arguments JSONB,
    status VARCHAR(50) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_tool_runs_created_at ON tool_runs(created_at DESC);
```

```powershell
# Windows: Verify local PostgreSQL connection
Test-NetConnection -ComputerName localhost -Port 5432
```

## Deliverables and Outputs
- `V<version>__<description>.sql`: Immutable Flyway migration scripts.
- JPA Entity classes and Spring Data JPA Repositories.
- Optimized database indexing definitions.

## Quality Gates and Acceptance Criteria
- Flyway migrations execute cleanly from scratch on an empty database without syntax errors.
- Foreign keys properly enforce referential integrity with cascading rules where appropriate.
- Database connection URLs read from environment variables rather than hardcoded local ports.

## Security and Safety Rules
- Destructive operations (`DROP TABLE`, `TRUNCATE`) are strictly forbidden in automated scripts without explicit user authorization and verified backup dumps.
- Passwords must be hashed using strong one-way algorithms (BCrypt or Argon2) before persistence.
