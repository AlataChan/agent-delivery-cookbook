# Delivery Lifecycle Checkpoints (Gates)

Use this as a standard checklist to prevent "scope drift" and "acceptance drift". Keep the structure stable; fill content from the client's specifics.

## Q) Qualification & Refusal Gate (立项资格)

The only gate whose correct outcome is sometimes "don't do this project". Delivery capacity is the scarcest resource in this model; a wrong project doesn't cost one deal, it removes the team from the market for a quarter.

**Inputs**
- The stated request, plus who is actually asking and who is paying.
- Whatever access to real data and real users can be arranged before commitment.

**Outputs**
- Qualification memo: the three tests answered, with evidence rather than assertion.
  - **Pain** — a named role's specific, recurring pain. "The support lead spends 3h every Monday reconciling escalations across 4 systems" qualifies; "improve support efficiency" does not.
  - **Economics** — hours/week consumed, loaded cost, cost of one error, what the freed capacity would do instead.
  - **Feasibility** — where the data actually lives and its true state; what accuracy the business consequence requires (90% + human review is frequently the right target, and an order of magnitude cheaper than 99%).
- Risk-signal check (two or more ⇒ decline or restructure):
  - No business owner — only IT is the interface. Compliance and stability are not reasons to start a project.
  - Real data withheld — "prove it on sample data first". Validation without real data manufactures false positives.
  - Unbounded scope — "cover every scenario company-wide" in the first meeting usually means no single scenario is ready.
- If declining: a "when, not no" note — the 2–3 conditions that would make this viable, and the smaller scenario that would produce them.

**Exit criteria (DoD)**
- A go/no-go decision is recorded with its reasoning, not deferred into discovery.
- If go: the specific scenario and its owner are named.
- If no-go: the relationship is preserved and the re-entry condition is written down.

---

## 0) North Star Gate

**Inputs**
- Stakeholder list (business / IT / security / operations / vendor).
- High-level context: channels, languages, regions, products, known constraints.

**Outputs (artifacts)**
- Project charter v0: goals, non-goals, scope boundary.
- Success metrics draft (business + quality + cost/latency).
- **Pre-project baseline snapshot**: current handling time, volume, error/escalation rate, headcount on the task, and how each number was measured. Capture it now — the baseline exists only before you change anything, and without it "we improved X by Y%" is unprovable at acceptance and unarguable at renewal.
- Risk register v0 (top 10).
- **Visual**: Project context map / stakeholder map (`drawio-skill` → architecture or mind map).

**Exit criteria (DoD)**
- Everyone agrees on "what success looks like" and what is out-of-scope.
- A first set of "must-not-fail" constraints exists (PII, compliance, latency, cost).
- Baseline numbers are recorded and acknowledged by the client (metrics they don't accept have no authority later).

---

## 1) Requirements Discovery Gate (需求调研)

**Inputs**
- Current SOPs, FAQ/docs, VOC/tickets, error code lists, known integration surfaces.
- User journey map (at least for the highest volume scenarios).
- **Direct observation sessions** with real users doing real cases — booked, not improvised. Documents describe how the organization believes it works; observation shows how it actually works.

**Outputs**
- Scenario catalog (by channel/language/region): happy path + edge cases.
- **Workaround log**: every place users step outside the official process — the spreadsheet maintained beside the system, the "ask Wang for that number" dependency, the manual re-check before a decision meeting. Each entry is an unmet need, and collectively they reveal which data people actually trust versus which is merely official. Connect to the trusted source, not the nominal one.
- **Translation check**: for each requirement, note whether it came from the person with the pain or was relayed through IT/procurement/a consultant. Relayed requirements arrive pre-converted ("we need a data platform") and cause you to build for the translation instead of the problem.
- Escalation policy draft: what must go to humans vs self-serve.
- Taxonomy v1: intent/problem types + labels; glossary v1 (terms + aliases).
- Data inventory: sources, owners, access method, update cadence, data quality risks.
- **Visual**: Scenario flow diagram (`fireworks-tech-graph` → flowchart).
- **Visual**: Taxonomy tree (`fireworks-tech-graph` → mind map).

**Exit criteria (DoD)**
- Top scenarios are enumerated with acceptance signals.
- Data access path is unblocked (or explicitly listed as "blockers").
- At least the highest-volume scenario has been observed first-hand, not only described.

---

## 1.5) Pilot Graduation Gate (试点毕业标准)

Exists to prevent the most expensive failure mode in AI delivery: the pilot that is never declared dead and never declared done, consuming the team indefinitely while appearing in status reports as "progressing".

**Inputs**
- Selected scenario from the discovery gate, with its named business owner.
- Real data access in the real environment (not an export, not a synthetic set).

**Outputs**
- Graduation contract, agreed before any build starts:
  - Maximum duration — weeks, not months. A long deadline doesn't buy quality; it removes the forcing function that makes both sides trade off honestly.
  - Acceptance metric and threshold, tied to the Gate 0 baseline.
  - What happens if the threshold isn't met — the parting terms, written while everyone is still optimistic.
- Scope statement narrowed by *scenario*, not by *quality*: one scenario handled end-to-end, rather than five handled at 70%. Partial quality across many scenarios satisfies nobody and demonstrates nothing.
- Real-data validation note: field mismatches, null rates, and encoding surprises found during the pilot (these are the things sample data hides and go-live discovers).

**Exit criteria (DoD)**
- Both sides can state the pilot's end date and its pass/fail number from memory.
- The pilot ran on real data in the real environment.
- Outcome recorded: graduate to the next phase, or stop cleanly — no third option, and no silent extension.

---

## 2) SOW / Scope Freeze Gate (SOW确认)

**Inputs**
- Outputs from discovery gate.

**Outputs**
- SOW: scope, assumptions, out-of-scope, deliverables, milestones, acceptance gates.
- RACI: roles, ownership, and escalation path.
- Change control: definition of change, approval workflow, impact handling.
- **Visual**: RACI swimlane diagram (`drawio-skill` → cross-functional flowchart / swimlane).

**Exit criteria (DoD)**
- Deliverables and acceptance are measurable (not only "looks good").
- Change control is agreed (so timeline is defendable).

---

## 3) Delivery Readiness Gate (交付就绪)

**Inputs**
- Target environments (dev/test/prod), network topology, security requirements.

**Outputs**
- Access & security checklist: accounts, network allowlists, SSO, logging policy, retention.
- Data readiness rules: cleaning/redaction rules; chunking template; versioning/conflict governance.
- Observability schema draft: required trace fields, evidence requirements, tool call logging.
- **Visual**: Deployment topology diagram (`drawio-skill` → network topology).

**Exit criteria (DoD)**
- Environments and permissions are ready for deployment work.
- Minimum governance exists for data and knowledge change (otherwise knowledge quality will collapse).

---

## 4) Model Deployment Gate (模型部署)

**Inputs**
- Hosting decision constraints (cloud/on-prem), traffic estimate, latency/cost targets.

**Outputs**
- Model runtime deployed (or vendor endpoint ready) with auth, quotas, and fallback.
- Safety & compliance: prompt/data policy; PII handling; refusal rules; redaction.
- Benchmark baselines (even rough): latency, cost, error rate.

**Exit criteria (DoD)**
- Stable connectivity + auth + rate limits verified.
- Rollback path exists.

---

## 5) Platform Deployment Gate (软件平台部署)

**Inputs**
- Infra readiness, model deployment output.

**Outputs**
- Agent runtime + KB service + indexing stack deployed.
- Tool gateway / integration layer deployed (even if mocked initially).
- Observability + audit: trace, logs, dashboards, incident workflow.
- **Visual**: C4 system architecture — Context → Container → Component (`drawio-skill` → C4 model, multi-page with drill-down).

**Exit criteria (DoD)**
- A minimal end-to-end "hello world" works (query → retrieve → answer) with trace.

---

## 6) Knowledge Engineering & Agent Build Gate (工程实施交付)

**Inputs**
- Taxonomy v1, data sources, platform running.

**Outputs**
- Taxonomy v1 freeze (or clearly versioned).
- Chunking/template v1 + quality gate (sampling + rejection criteria).
- Index strategy: keyword vs vector vs structured; filtering rules.
- Retrieval policy: TopK, thresholds, de-dup, rerank, "no-evidence → don't answer/hand off".
- Agent policy: dialog flows, tool calling, escalation, multilingual support.
- **Visual**: Agent architecture diagram (`fireworks-tech-graph` → agent architecture).
- **Visual**: RAG data flow diagram (`fireworks-tech-graph` → data flow).

**Exit criteria (DoD)**
- Badcase can be replayed and attributed (data vs retrieval vs policy vs tool vs hallucination).
- "Unsafe/uncertain" path is controlled (no confident fabrication).

---

## 7) Evaluation & UAT Gate (评估验收)

**Inputs**
- Scenario catalog, implemented agent, knowledge base.

**Outputs**
- Evaluation set: representative queries with expected outcomes and evidence requirements.
- Metrics: success, hallucination, escalation correctness, tool success, latency.
- UAT checklist + go/no-go threshold + regression process.
- **Visual**: Evaluation metrics dashboard mockup (`fireworks-tech-graph` → comparison matrix or timeline).

**Exit criteria (DoD)**
- UAT is anchored on a stable rubric; changes trigger re-eval.

---

## 7.5) Deliverable Packaging Gate (交付物打包)

**Inputs**
- All artifacts from Phases 0–7 (charters, SOW, RACI, eval results, runbook).
- All visual artifacts produced (context map, scenario flows, topology, C4 architecture, agent/data flow, dashboard mockup).
- Diagram manifest (`08_diagram_manifest.md`).

**Outputs**
- **Client-facing document** (DOCX): compiled from all phase artifacts with embedded diagrams.
- **Executive presentation deck** (PPTX): key findings, architecture, metrics, roadmap — with embedded diagrams.
- **Delivery package**: DOCX + PPTX + all `.drawio`/`.svg` source files + templates archive.
- Diagram manifest (completed): listing all diagrams produced, their source files, and where they appear in the doc/PPT.

**Exit criteria (DoD)**
- Document and PPT are reviewed and approved by delivery lead.
- All diagrams are embedded and render correctly in both DOCX and PPTX.
- Delivery package is versioned and stored in the agreed location.

---

## 8) Go-Live & Operations Gate (上线与运营)

**Inputs**
- UAT sign-off, cutover plan draft, deliverable package.

**Outputs**
- Cutover runbook + rollback runbook.
- On-call / escalation procedure; incident severity definition.
- Knowledge update mechanism: submission → review → publish → rollback.
- Weekly ops cadence: badcase review, release notes, KPI review.
- **Adoption plan with a numeric target**: what share of the *target user group* (not of provisioned accounts) is in stable, unprompted use by day 30 and day 90. Launch is an administrative event; adoption is a behavioral one, and a system can pass every operational check while being entirely unused.
- **Role map for the three groups RACI does not model**:
  - *Champion* — stakes their own reputation on this. Verify there is more than one; single-point sponsorship dies with a reorg.
  - *Influencer* — no formal authority, but the person colleagues actually ask. One "this actually works" from them outweighs any management announcement, and one "it's for show" kills adoption quietly. Recruit them as early users and make adopted suggestions visible and attributed.
  - *Displaced* — loses work, status, gatekeeping power, or hard-won exclusive knowledge. Design their path forward *before* go-live (redirected capacity, gatekeeper → coach, explicit commitments about roles). Resistance here is rational, not lazy, and it is far cheaper to address than to overcome.
- **Visual**: Cutover/rollback flowchart (`drawio-skill` → flowchart).
- **Visual**: Ops runbook flow (`drawio-skill` → flowchart or BPMN).

**Exit criteria (DoD)**
- You can operate the system: observe, triage, fix, and verify.
- Adoption is measured against the target user group and trending toward the day-30/day-90 threshold — not merely "deployed and available".
- Every group in the role map has a named owner on the client side, including the displaced.
- The system is still used at the same rate after the delivery team steps back. Usage that decays on handover was accompaniment, not adoption.
