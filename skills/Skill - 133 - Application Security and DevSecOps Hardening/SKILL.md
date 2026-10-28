---
name: Skill - 133 - Application Security and DevSecOps Hardening
description: Use when conducting security audits, mitigating OWASP Top 10 vulnerabilities, scanning for exposed secrets, hardening JWT authentication, or auditing code generation for dangerous calls.
---

# Skill - 133 - Application Security and DevSecOps Hardening

## Purpose and Scope
Identify, audit, mitigate, and prevent security vulnerabilities across application source code, dependency trees, container configurations, and CI/CD pipelines. Enforces OWASP Top 10 defenses, cryptographic best practices, JWT/RBAC access control, input sanitization, and AST-based static analysis for AI-generated code.

## Trigger Conditions
- Conducting an application security review or pre-deployment security gate.
- Investigating potential vulnerabilities (SQL Injection, Path Traversal, SSRF, XSS, Broken Object-Level Authorization).
- Auditing configuration files and git repositories for accidentally committed credentials or API keys.
- Hardening authentication mechanisms, token storage, and internal microservice keys.
- Implementing AST security guards for code-generation engines.

## Non-Trigger Conditions
- Do not trigger for ordinary bug fixes unrelated to security vulnerabilities.
- Do not trigger for routine unit test authoring (use `qa-test-automation-strategy`).
- Do not trigger for live penetration testing against external systems without written authorization.

## Prerequisites and Inputs
- Application source code, configuration files, and dependency manifests.
- Security scanners or AST inspection tooling (e.g. Python `ast`, OWASP Dependency-Check, Trivy, npm audit).
- Architecture diagram and data classification records.

## Execution Workflow
1. **Secret & Credential Exposure Scan**:
   - Audit `application.yml`, `.env`, and source trees for raw passwords, private keys, or API tokens.
   - Replace raw values with environment variable bindings (`${DB_PASSWORD:dev-pass}`).
2. **Input Sanitization & Injection Defense**:
   - Ensure all database interactions utilize parameterized queries or ORM binding (Spring Data JPA) to prevent SQL injection.
   - Enforce path traversal barriers on filesystem tools (e.g. `_safe_path` resolving strictly within `AI_DATA_DIR`).
3. **Authentication & Authorization Hardening**:
   - Verify JWT HS256/RS256 secret entropy (minimum 256 bits).
   - Verify that all sensitive REST endpoints require authenticated caller context; reject IDOR vulnerabilities by verifying resource ownership.
4. **AST Code-Generation Security Analyzer**:
   - Inspect generated code via Abstract Syntax Tree traversal:
     - Ban dangerous builtins: `eval`, `exec`, `compile`, `__import__`.
     - Ban dangerous modules: `subprocess`, `socket`, `ctypes`, `shutil`, `os.system`, `os.popen`.
     - Mark code `executed: false` to prevent autonomous execution.
5. **Content Security Policy (CSP) & Web Headers**:
   - Configure Nginx and Spring Security with strict security headers: `Content-Security-Policy`, `X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY`.

## Commands and Examples
```powershell
# Scan repository for potential committed secrets or private keys
Get-ChildItem -Path . -Recurse -File | Select-String -Pattern "BEGIN (RSA|EC|OPENSSH) PRIVATE KEY|password\s*=\s*['\"][^'\"]+['\"]"

# Node/Angular dependency security vulnerability audit
npm audit --production

# Python AST security scanner snippet
python -c "import ast; tree = ast.parse('import subprocess'); print([n.names[0].name for n in ast.walk(tree) if isinstance(n, ast.Import)])"
```

## Deliverables and Outputs
- `docs/SECURITY_AUDIT.md`: Vulnerability report with CVSS ratings, affected code lines, and remediations.
- Remediated configuration files with all raw secrets removed.
- Hardened Spring Security / Nginx configuration files.
- AST security analyzer module preventing dangerous code execution.

## Quality Gates and Acceptance Criteria
- Zero critical or high-severity vulnerabilities in dependencies (`npm audit`, `dependency-check`).
- Zero plaintext credentials or API keys committed to version control.
- All AST security tests pass, proving dangerous code execution is intercepted and rejected.

## Security and Safety Rules
- Never print real discovered passwords or secrets in audit logs; always truncate or mask (`abc***123`).
- All tool execution side effects must remain gated by explicit human approval.
