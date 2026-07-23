# Delivery Lifecycle Checkpoints (Gates)

Use this as a standard checklist to prevent "scope drift" and "acceptance drift". Keep the structure stable; fill content from the client's specifics.

## 0) North Star Gate

**Inputs**
- Stakeholder list (business / IT / security / operations / vendor).
- High-level context: channels, languages, regions, products, known constraints.

**Outputs (artifacts)**
- Project charter v0: goals, non-goals, scope boundary.
- Success metrics draft (business + quality + cost/latency).
- Risk register v0 (top 10).
- **Visual**: Project context map / stakeholder map (`drawio-skill` → architecture or mind map).

**Exit criteria (DoD)**
- Everyone agrees on "what success looks like" and what is out-of-scope.
- A first set of "must-not-fail" constraints exists (PII, compliance, latency, cost).

---

## 1) Requirements Discovery Gate (需求调研)

**Inputs**
- Current SOPs, FAQ/docs, VOC/tickets, error code lists, known integration surfaces.
- User journey map (at least for the highest volume scenarios).

**Outputs**
- Scenario catalog (by channel/language/region): happy path + edge cases.
- Escalation policy draft: what must go to humans vs self-serve.
- Taxonomy v1: intent/problem types + labels; glossary v1 (terms + aliases).
- Data inventory: sources, owners, access method, update cadence, data quality risks.
- **Visual**: Scenario flow diagram (`fireworks-tech-graph` → flowchart).
- **Visual**: Taxonomy tree (`fireworks-tech-graph` → mind map).

**Exit criteria (DoD)**
- Top scenarios are enumerated with acceptance signals.
- Data access path is unblocked (or explicitly listed as "blockers").

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
- **Visual**: Cutover/rollback flowchart (`drawio-skill` → flowchart).
- **Visual**: Ops runbook flow (`drawio-skill` → flowchart or BPMN).

**Exit criteria (DoD)**
- You can operate the system: observe, triage, fix, and verify.
