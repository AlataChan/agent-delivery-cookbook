# Minimal Discovery Questions (to unblock the next gate)

Ask only what you need to progress to the next gate; mark unknowns as `（待确认）/TBD`.

## A0) Qualification (先问 — 决定要不要做)
- Whose pain is this, by name and role? What do they do today, how often, and how long does it take?
- What is solving it worth — hours/week, loaded cost, cost of one error, what freed capacity would do instead?
- Who owns this on the business side (not IT)? If the answer is only IT, ask why no business unit is sponsoring it.
- Can we see real data and real users before committing? If not, why not, and when?
- What accuracy does the consequence actually require? Is "90% + human review" acceptable, or does this genuinely need 99%?
- If two or more risk signals are present (no business owner / real data withheld / unbounded scope), stop here and write the "when, not no" note instead of proceeding to North Star.

## A) North Star (必问)
- Target outcomes: What business outcomes must improve? (deflection, CSAT, resolution time, cost, etc.)
- Non-goals: What is explicitly not addressed in this phase?
- Scope boundary: Which channels (web/app/email/phone), languages, regions, products?
- Hard constraints: compliance, data residency, latency ceiling, budget ceiling.

## B) Scenarios (必问)
- Top 20 scenarios by volume and by risk (separate lists).
- For each key scenario: “good answer” definition and “must escalate” triggers.
- Current SOP: decision points and required fields (serial number, error code, firmware, etc.).
- **Ask to watch, not only to be told**: can we sit with someone handling real cases for half a day? What people report doing and what they do diverge, and only the second one predicts adoption.
- Where do people step outside the system — side spreadsheets, chat groups, "ask X for that number", manual re-checks before decisions? Every workaround is an unmet need in plain sight.
- Which data source do you actually trust for this decision — and is it the official one? If not, we connect to the trusted one.
- Did this requirement come from the person with the pain, or was it relayed? Relayed requirements arrive already converted into someone else's solution.

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
- Baseline: what are we comparing against (human team, current bot, none)? **Capture the actual numbers now** — handling time, volume, error/escalation rate, headcount — and get the client to acknowledge them. The pre-change state cannot be reconstructed later, and a metric the client didn't agree to has no authority at acceptance.

## G) Operations (尽早确认)
- Who owns knowledge updates and release approvals?
- On-call and escalation path; incident definition and SLA/SLO.
- Monitoring expectations: what dashboards are required?

