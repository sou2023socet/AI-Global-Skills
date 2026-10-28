# Source candidate specification

- **Purpose/problem; goal/outcome:** Repeated incidents are handled individually; aggregate safe event data to identify recurring causes and prevention.
- **Behavior; activation/non-activation:** Normalize incidents/time windows and compare trends; not live incident response or surveillance.
- **Inputs/tools/dependencies/handoff:** Authorized incident/log data, taxonomy, retention, time range; approved log query/analysis; depends 06/41/58–59/63; hands root causes to 29/39/62/70.
- **Procedure/decision:** 1) Confirm access and redact identifiers. 2) Normalize categories and deduplicate events. 3) Compare rates/severity with baseline. 4) If sample size or logging is insufficient, report uncertainty, not trend.
- **Outputs/acceptance/failure:** Trend report with methods, sample limits, repeat patterns; pass when conclusions are reproducible and privacy-safe. Query errors or missing logs are visible.
- **Security/example/maintenance:** Minimize PII and restrict raw log access. Example: repeated timeout incidents cluster around one dependency after version change, hypothesis pending validation. **Status:** proposed; diagnostic skill handles individual RCA only. Reassess taxonomy.
