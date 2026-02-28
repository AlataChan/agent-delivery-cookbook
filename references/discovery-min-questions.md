# Minimal Discovery Questions (to unblock the next gate)

Ask only what you need to progress to the next gate; mark unknowns as `（待确认）/TBD`.

## A) North Star (必问)
- Target outcomes: What business outcomes must improve? (deflection, CSAT, resolution time, cost, etc.)
- Non-goals: What is explicitly not addressed in this phase?
- Scope boundary: Which channels (web/app/email/phone), languages, regions, products?
- Hard constraints: compliance, data residency, latency ceiling, budget ceiling.

## B) Scenarios (必问)
- Top 20 scenarios by volume and by risk (separate lists).
- For each key scenario: “good answer” definition and “must escalate” triggers.
- Current SOP: decision points and required fields (serial number, error code, firmware, etc.).

## C) Knowledge & Data (必问)
- What sources exist (docs/FAQ/VOC/tickets/error codes/workflows)? Who owns each?
- Update cadence and versioning: product/firmware/region differences?
- Red flags: contradictions, outdated docs, missing coverage, multilingual gaps.

## D) Integration & Tools (尽早确认)
- What systems must be called (orders, logistics, CRM, ticketing)? Read vs write?
- Auth method (SSO/OAuth/API key), rate limits, and test environment availability.
- Failure handling expectation (timeouts, missing permission, partial data).

## E) Safety, Security, Compliance (尽早确认)
- PII definition + redaction requirements.
- Logging/trace retention policy and audit requirements.
- Forbidden behaviors: what the agent must never do or say.

## F) Evaluation & Acceptance (尽早确认)
- Who signs off? What is the acceptance rubric?
- What are the “must-pass” tests? (high-risk scenarios, policy compliance)
- Baseline: what are we comparing against (human team, current bot, none)?

## G) Operations (尽早确认)
- Who owns knowledge updates and release approvals?
- On-call and escalation path; incident definition and SLA/SLO.
- Monitoring expectations: what dashboards are required?

