---
name: Skill - 224 - Project Discovery Audit (Legacy Source Record)
description: Use when tasked with auditing an unfamiliar codebase, discovering technology stacks, verifying installed toolchains, mapping dependencies, or diagnosing documentation drift.
---

# Skill - 224 - Project Discovery Audit (Legacy Source Record)

## Purpose and Scope
Perform an empirical, non-destructive audit of a software repository to uncover its architecture, technology stack, dependency graph, configuration parameters, operational health, and documentation alignment. Establishes a verified baseline without modifying source code or configuration.

## Trigger Conditions
- User requests a comprehensive project audit, tech stack discovery, or architecture review.
- Starting work on a new or unfamiliar repository.
- Investigating suspected drift between documented features and actual codebase reality.
- Preparing for major architectural refactoring, migration, or security hardening.

## Non-Trigger Conditions
- Do not trigger for targeted single-file bugfixes or routine feature development.
- Do not trigger if the task is strictly to execute a pre-defined build or test command (use `build-test-approval-gate`).
- Do not trigger for modifying application code or deleting files.

## Prerequisites and Inputs
- Accessible repository directory or workspace path.
- Standard inspection tools available in environment (`git`, shell tools like PowerShell or Bash, file reading capabilities).
- Read access to project root, build manifests, and documentation.

## Execution Workflow
1. **Manifest & Stack Discovery**:
   - Inspect build manifests: `pom.xml`, `package.json`, `requirements.txt`, `build.gradle`, `Cargo.toml`.
   - Identify active language runtimes, compilers, and framework versions.
2. **Directory & Module Layout Inventory**:
   - Traverse the workspace up to 3 levels deep, excluding heavy vendor folders (`node_modules`, `target`, `dist`, `.git`, `__pycache__`).
   - Group files into logical tiers: Backend, AI Microservice, Frontend UI, Persistence, Documentation.
3. **Environment & Runtime Verification**:
   - Check local versions of required runtimes (`java -version`, `python --version`, `node --version`, `mvn -v`, `docker -v`).
   - Compare installed toolchain against project requirements.
4. **Configuration & Drift Inspection**:
   - Check configuration templates (`.env.example`, `application.yml`) against active configurations (`.env`, `application-local.yml`).
   - Flag hardcoded credentials, non-standard local ports, or stripped environment placeholders.
5. **Documentation vs. Code Discrepancy Analysis**:
   - Verify whether documented services, directories, or endpoints actually exist in code.
   - Detect phantom artifacts (e.g. references to missing fallback UIs).
6. **Report Generation**:
   - Compile findings into an evidence-backed audit report citing exact file paths and line ranges.

## Commands and Examples
```powershell
# Windows PowerShell: Inspect project structure excluding vendor dirs
Get-ChildItem -Path . -Recurse -File | Where-Object {
    $_.FullName -notmatch "node_modules|target|dist|__pycache__|\.git|\.angular"
} | Select-Object FullName, Length

# Inspect open ports and local service bindings
Get-NetTCPConnection -State Listen | Select-Object LocalAddress, LocalPort, OwningProcess

# Check Java, Python, and Node versions
java -version
python --version
node --version
```

```bash
# POSIX Bash: Fast file count and extension mapping
find . -maxdepth 3 -not -path '*/.*' -not -path '*/node_modules/*' -not -path '*/target/*'
```

## Deliverables and Outputs
- `PROJECT_AUDIT.md`: A structured audit document detailing:
  - Executive summary and architectural strengths.
  - Technology stack and dependency matrix with verified versions.
  - API endpoint and integration catalog.
  - Documentation vs. code reality discrepancy table.
  - Security risks and configuration drift findings.

## Quality Gates and Acceptance Criteria
- Every claim in the audit is backed by empirical inspection (file existence, line number, or command output).
- No speculative assertions; missing files or tools are recorded honestly as missing.
- Zero modifications made to application source code or configuration files.

## Security and Safety Rules
- Read-only inspection only; never run destructive clean or delete commands.
- Never print or commit plaintext passwords, JWT secrets, or cloud access keys found during configuration review; redact with `***`.
- Scrutinize `.env` files for accidentally committed production secrets.
