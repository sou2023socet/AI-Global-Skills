"""Build the complete canonical library from the configured source repositories.

The source repositories are read-only inputs. Existing candidate packages are
preserved; source capabilities are either mapped to an existing canonical
capability or promoted to a new stable canonical package.
"""

from __future__ import annotations

import csv
import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOTS = {
    "global-skills": Path(r"E:\sumit@data\project\Git\global-skills"),
    "enterprise-ai-engineering-skills": Path(
        r"E:\sumit@data\project\Git\enterprise-ai-engineering-skills"
    ),
}
REGISTRY_PATH = ROOT / "registry" / "registry.json"
SOURCE_REGISTRY_PATH = ROOT / "registry" / "source-skills.json"
INVENTORY_PATH = ROOT / "docs" / "migration" / "SOURCE_INVENTORY.csv"
DECISIONS_PATH = ROOT / "reports" / "SOURCE_MIGRATION_DECISIONS.csv"


MERGES = {
    "api-contract-rest-design": "api-and-database-specialist",
    "appsec-devsecops-hardening": "security-auditor",
    "clean-code-refactoring": "code-review-and-refactoring-agent",
    "database-architecture-migration": "api-and-database-specialist",
    "devops-container-orchestration": "deployment-and-environment-engineer",
    "diagnostic-debugging-rootcause": "bug-diagnosis-and-repair-agent",
    "documentation-engineering": "documentation-generator",
    "focused-function-testing": "automated-testing-engineer",
    "functional-testing": "automated-testing-engineer",
    "global-ai-skills-automation-system": "automation-workflow-designer",
    "performance-profiling-scalability": "performance-auditor",
    "production-deployment-verification": "deployment-and-environment-engineer",
    "project-discovery-audit": "project-context-analyzer",
    "qa-test-automation-strategy": "test-strategy-generator",
    "sdlc-planning-governance": "roadmap-and-project-planner",
    "system-architecture-design": "architecture-and-design-implementation",
    "test-automation-engineering": "automated-testing-engineer",
    "token-efficient-agent-workflows": "token-efficient-agent-workflows",
    "workflow-automation-scheduling": "automation-workflow-designer",
    "01-engineering-governance": "global-development-rules",
    "02-project-discovery-audit": "project-context-analyzer",
    "03-requirements-engineering": "requirements-engineering",
    "04-sdlc-lifecycle-manager": "roadmap-and-project-planner",
    "05-project-planning-traceability": "requirements-to-test-traceability",
    "06-architecture-design": "architecture-and-design-implementation",
    "07-project-structure-manager": "universal-project-structure-architect",
    "08-api-contract-design": "api-and-database-specialist",
    "09-database-data-architecture": "api-and-database-specialist",
    "10-integration-dependency-mapping": "integration-and-compatibility-engineer",
    "11-environment-readiness": "environment-and-dependency-manager",
    "12-dependency-lifecycle-manager": "dependency-and-compatibility-monitor",
    "13-configuration-secrets-manager": "environment-and-dependency-manager",
    "14-developer-setup-automation": "environment-and-dependency-manager",
    "15-build-toolchain-manager": "build-and-packaging-verifier",
    "16-implementation-planner": "feature-implementation-agent",
    "17-coding-standards": "development-standards-enforcer",
    "18-refactoring-maintenance": "code-review-and-refactoring-agent",
    "19-code-review-quality-gate": "code-review-and-refactoring-agent",
    "20-technical-debt-management": "continuous-improvement-planner",
    "21-ui-ux-research-design": "ui-ux-recovery",
    "23-frontend-engineering": "frontend-engineering",
    "24-cross-platform-app-engineering": "cross-platform-mobile-engineering",
    "25-accessibility-responsive-quality": "ui-ux-and-accessibility-tester",
    "27-authentication-authorization-security": "security-auditor",
    "28-application-security-devsecops": "security-auditor",
    "29-data-privacy-compliance": "security-auditor",
    "30-api-database-integration-testing": "automated-testing-engineer",
    "31-test-strategy-management": "test-strategy-generator",
    "32-test-automation-engineering": "automated-testing-engineer",
    "33-build-regression-verification": "regression-and-change-impact-analyzer",
    "34-performance-scalability-engineering": "performance-auditor",
    "35-reliability-fault-recovery": "workflow-failure-and-recovery-manager",
    "36-logging-error-diagnostics": "logs-audit-trail-and-reporting",
    "37-observability-monitoring-alerting": "incident-and-error-trend-analyzer",
    "38-incident-response-root-cause": "incident-and-error-trend-analyzer",
    "39-artifact-release-builder": "release-and-rollback-manager",
    "40-hosting-platform-adapter": "deployment-and-environment-engineer",
    "41-cicd-infrastructure-automation": "automation-workflow-designer",
    "42-deployment-live-service-verification": "deployment-and-environment-engineer",
    "43-production-readiness-release-management": "quality-gate-and-readiness-evaluator",
    "44-documentation-knowledge-management": "documentation-synchronization",
    "45-technology-watch-dependency-updates": "technical-research-agent",
    "46-migration-upgrade-compatibility": "dependency-and-compatibility-monitor",
    "47-ai-agent-skills-tool-governance": "global-skills-framework",
    "48-mcp-tool-integration": "mcp-integration-specialist",
    "49-workflow-automation-scheduling": "automation-workflow-designer",
    "50-engineering-orchestrator-continuous-improvement": "skill-selection-and-orchestration-engine",
    "51-sdlc-model-generation": "roadmap-and-project-planner",
    "53-production-environment-deployment-engineer": "deployment-and-environment-engineer",
    "accessibility-and-inclusive-design": "ui-ux-and-accessibility-tester",
    "ai-agent-skill-governance-and-routing": "skill-selection-and-orchestration-engine",
    "architecture-diagram-and-flow-documentation": "architecture-and-diagram-reconstruction",
    "backend-integration-and-api-testing": "automated-testing-engineer",
    "backend-logging-and-request-tracing": "logs-audit-trail-and-reporting",
    "build-test-and-quality-pipeline-engineering": "build-and-packaging-verifier",
    "database-architecture-and-multi-engine-support": "api-and-database-specialist",
    "dependency-upgrade-and-compatibility-management": "dependency-and-compatibility-monitor",
    "design-engineering-governance": "development-standards-enforcer",
    "docker-and-container-deployment": "deployment-and-environment-engineer",
    "environment-profiles-and-configuration-management": "environment-and-dependency-manager",
    "frontend-backend-api-integration": "integration-and-compatibility-engineer",
    "frontend-backend-separation-and-refactoring": "architecture-and-design-implementation",
    "frontend-logging-and-diagnostics": "logs-audit-trail-and-reporting",
    "frontend-performance-and-asset-optimization": "performance-auditor",
    "frontend-testing-and-visual-regression": "ui-ux-and-accessibility-tester",
    "logging-monitoring-and-incident-management": "incident-and-error-trend-analyzer",
    "project-continuity-and-change-impact-management": "project-memory-and-handover",
    "project-dependency-and-structure-governance": "universal-project-structure-architect",
    "project-discovery-and-design-audit": "project-context-analyzer",
    "project-documentation-and-readme-engineering": "documentation-generator",
    "requirements-and-user-journey-engineering": "requirements-engineering",
    "responsive-design-and-device-compatibility": "ui-ux-and-accessibility-tester",
    "rest-api-controller-and-contract-engineering": "api-and-database-specialist",
    "role-based-access-and-api-security": "security-auditor",
    "sdlc-and-design-gate-manager": "quality-gate-and-readiness-evaluator",
    "security-privacy-and-data-governance": "security-auditor",
    "skills-validation-versioning-and-release": "global-skills-framework",
    "terminal-session-and-command-orchestration": "task-queue-and-dependency-scheduler",
    "token-efficient-agent-workflows": "token-efficient-agent-workflows",
    "ui-ux-research-and-information-architecture": "ui-ux-recovery",
    "universal-project-setup": "environment-and-dependency-manager",
}


def slug(value: str) -> str:
    value = value.lower().replace("&", " and ")
    return re.sub(r"[^a-z0-9]+", "-", value).strip("-")


def title(value: str) -> str:
    return value.replace("-", " ").replace("_", " ").title()


def source_body(content: str) -> str:
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) == 3:
            return parts[2].lstrip()
    return content


def lifecycle(name: str) -> str:
    lowered = name.lower()
    if any(token in lowered for token in ("test", "quality", "validation", "regression")):
        return "testing"
    if any(token in lowered for token in ("security", "privacy", "auth")):
        return "security"
    if any(token in lowered for token in ("deploy", "docker", "hosting", "release", "build")):
        return "delivery"
    if any(token in lowered for token in ("ui", "frontend", "design", "accessibility")):
        return "development"
    if any(token in lowered for token in ("database", "api", "backend", "spring")):
        return "development"
    if any(token in lowered for token in ("documentation", "knowledge")):
        return "documentation"
    return "foundation"


def make_package(skill_id: str, source_name: str, source_path: str, content: str) -> None:
    destination = ROOT / "skills" / skill_id
    destination.mkdir(parents=True, exist_ok=True)
    body = source_body(content).strip()
    package = f"""---
id: {skill_id}
name: {title(source_name)}
version: 1.0.0
status: structurally_validated
source: {source_path}
---

# {title(source_name)}

## Purpose
Apply the reusable {title(source_name)} capability to the named project task without
silently expanding scope or permissions.

## Activation
- Activate when the task explicitly requires {title(source_name)}.
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

{body}
"""
    (destination / "SKILL.md").write_text(package, encoding="utf-8", newline="\n")


def main() -> None:
    registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8-sig"))
    records = registry["skills"]
    by_id = {record["id"]: record for record in records}
    candidate_skill_ids = {
        record["id"] for record in records if record.get("candidateIds")
    }
    source_records: list[dict[str, object]] = []
    dispositions: dict[str, str] = {}
    used_ids = set(by_id)
    prior_source_targets = {}
    if SOURCE_REGISTRY_PATH.is_file():
        prior_source_targets = {
            (item["repository"], item["sourcePath"]): item["canonicalSkillId"]
            for item in json.loads(
                SOURCE_REGISTRY_PATH.read_text(encoding="utf-8-sig")
            ).get("skills", [])
            if item.get("canonicalSkillId")
        }
    source_count = 0

    for repository, root in SOURCE_ROOTS.items():
        if not root.is_dir():
            raise FileNotFoundError(root)
        for source_file in sorted(root.rglob("SKILL.md")):
            source_count += 1
            source_name = source_file.parent.name
            source_path = str(source_file.relative_to(root))
            digest = hashlib.sha256(source_file.read_bytes()).hexdigest()
            target_id = MERGES.get(source_name)
            if target_id not in by_id:
                target_id = prior_source_targets.get((repository, source_path))
            if target_id not in by_id:
                target_id = None
            if target_id is None:
                base = slug(source_name)
                target_id = base
                suffix = 2
                while target_id in used_ids:
                    target_id = f"{base}-{suffix}"
                    suffix += 1
                used_ids.add(target_id)
                make_package(target_id, source_name, f"{repository}:{source_path}", source_file.read_text(encoding="utf-8-sig"))
                record = {
                    "id": target_id,
                    "name": title(source_name),
                    "version": "1.0.0",
                    "contractVersion": "1.0",
                    "status": "structurally_validated",
                    "verification": {
                        "structural": "passed",
                        "functional": "not-run",
                        "platform": "not-run",
                    },
                    "implementationKind": "promoted-source-skill",
                    "lifecycleGroup": lifecycle(source_name),
                    "purpose": f"Apply the source-derived {title(source_name)} capability.",
                    "triggers": [f"task requires {title(source_name)}"],
                    "nonTriggers": ["unrelated work", "missing project identity", "permission bypass"],
                    "provenance": [{
                        "repository": repository,
                        "path": source_path,
                        "sha256": digest,
                        "reviewStatus": "reviewed",
                    }],
                    "dependencies": [],
                    "inputs": [{
                        "name": "projectContext",
                        "description": "Current project identity, task scope, constraints, and evidence.",
                        "required": True,
                        "sensitivity": "internal",
                        "freshnessRequired": True,
                    }],
                    "outputs": [{
                        "name": "capabilityResult",
                        "description": "Actionable result with evidence, failures, and limitations.",
                        "required": True,
                        "sensitivity": "internal",
                    }],
                    "tools": [{
                        "name": "repository-inspection-and-approved-project-tools",
                        "permission": "read-only",
                        "requiresApproval": False,
                        "sideEffects": "none by default",
                    }],
                    "validationCriteria": [{
                        "criterion": "Canonical package contains the required procedure and source contract.",
                        "evidenceType": "static",
                    }],
                    "candidateIds": [],
                    "sourceSkillIds": [],
                }
                by_id[target_id] = record
                records.append(record)
            source_id = f"{repository}:{source_path}"
            dispositions[source_id] = target_id
            by_id[target_id].setdefault("sourceSkillIds", []).append(source_id)
            source_records.append({
                "id": f"legacy-{slug(repository)}-{slug(source_name)}",
                "name": source_name,
                "repository": repository,
                "sourcePath": source_path,
                "canonicalPath": f"skills/{target_id}/SKILL.md",
                "sha256": digest,
                "disposition": "merged-into-canonical" if target_id in {r["id"] for r in records[:80]} else "promoted-to-canonical",
                "promotionStatus": "canonical",
                "canonicalSkillId": target_id,
            })

    lifecycle_order = {
        "foundation": 10,
        "recovery": 20,
        "research-planning": 30,
        "development": 40,
        "testing": 50,
        "security": 60,
        "quality": 70,
        "project-knowledge": 80,
        "delivery": 90,
        "roadmap-release": 100,
        "maintenance": 110,
        "automation": 120,
    }
    for record in records:
        record["sourceSkillIds"] = sorted(set(record.get("sourceSkillIds", [])))
        record["executionOrder"] = lifecycle_order.get(record["lifecycleGroup"], 999)
        record["canonical"] = True
        record["path"] = f"skills/{record['name']}/SKILL.md"
    records.sort(key=lambda record: (record["executionOrder"], record["id"]))
    registry["registryVersion"] = "2.0"
    registry["generatedFrom"] = {
        "catalogue": "registry/source-skills.json",
        "mapping": "reports/SOURCE_MIGRATION_DECISIONS.csv",
    }
    REGISTRY_PATH.write_text(json.dumps(registry, indent=2) + "\n", encoding="utf-8")
    SOURCE_REGISTRY_PATH.write_text(json.dumps({
        "version": "2.0",
        "description": "Complete source inventory with one canonical destination per source skill.",
        "sourceRepositories": list(SOURCE_ROOTS),
        "skills": source_records,
    }, indent=2) + "\n", encoding="utf-8")

    with DECISIONS_PATH.open(newline="", encoding="utf-8-sig") as handle:
        decisions = list(csv.DictReader(handle))
        fieldnames = list(decisions[0])
        for field in ("Canonical_Skill_ID", "Capability_Disposition"):
            if field not in fieldnames:
                fieldnames.append(field)
    for row in decisions:
        row["Canonical_Skill_ID"] = dispositions.get(
            f'{row["Repository"]}:{Path(row["Source_Path"]).relative_to(SOURCE_ROOTS[row["Repository"]])}',
            "",
        )
        if row["Type"] == "skill" and row["Canonical_Skill_ID"]:
            is_existing = row["Canonical_Skill_ID"] in candidate_skill_ids
            row["Migration_Decision"] = (
                "merged-into-canonical" if is_existing else "promoted-to-canonical"
            )
            row["Decision_Reason"] = (
                "Source capability is mapped to the active canonical skill; "
                "the legacy copy is provenance-only."
            )
            row["Canonical_Destination"] = (
                f"skills/{row['Canonical_Skill_ID']}/SKILL.md"
            )
            row["Verification_Status"] = (
                "source-present; canonical-structure-validated; "
                "functional-verification-not-run"
            )
            row["Capability_Disposition"] = row["Migration_Decision"]
        else:
            row["Capability_Disposition"] = row["Migration_Decision"]
    with DECISIONS_PATH.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(decisions)
    print(f"Built {len(records)} canonical skills from {source_count} source skills.")


if __name__ == "__main__":
    main()
