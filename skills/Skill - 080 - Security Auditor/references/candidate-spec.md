# Source candidate specification

- **Purpose/problem; goal/outcome:** Security defects across code/config/dependencies are missed; perform authorized, evidence-based review with prioritized findings.
- **Behavior; activation/non-activation:** Review static and approved dynamic surfaces; not exploit third-party systems absent authorization or unbounded penetration testing.
- **Inputs/tools/dependencies/handoff:** Authorized scope, architecture, data classification, source/manifests; approved scanners and manual review; depends 02/23–25/31/33; findings to 29/32/42.
- **Procedure/decision:** 1) Confirm scope and exclusions. 2) Review auth, input, secrets, dependencies, data exposure and boundaries. 3) Validate safely and rate impact/confidence. 4) If proof needs risky access, stop and report unverified.
- **Outputs/acceptance/failure:** Private report with finding, evidence, impact, confidence, remediation; pass means review complete, not necessarily zero findings. Scanner errors disclosed.
- **Security/example/maintenance:** Never publish secrets/findings; follow disclosure policy and approvals. Example: source review finds missing owner check; report exact evidence without accessing another account. **Status:** partial—appsec skill and security policy exist; no scan results for candidate set. Reassess advisories.
