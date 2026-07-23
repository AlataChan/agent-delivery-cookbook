---
name: agent-delivery-cookbook
description: "Standardized end-to-end delivery workflow for LLM/agent projects (especially customer service/support): requirements discovery, SOW/scope freeze, model + platform deployment readiness, knowledge engineering (taxonomy/chunking/indexing/retrieval), agent/tooling build, evaluation & acceptance, deliverable packaging (doc + PPT), go-live, and operations. Use when asked to plan/execute these phases, produce checklists/artifacts/diagrams, define milestones & gates, or align responsibilities (RACI) across parties."
---

# Agent Delivery Cookbook

## Overview

Drive a repeatable "from discovery → SOW → deployment → delivery → packaging → go-live → ops" lifecycle, while keeping the *framework standardized* and letting project-specific content be filled from the client's context.

## Workflow

Use the workflow below as the default backbone. Treat it as iterative (expect back-and-forth), but keep gates explicit so scope/acceptance don't drift.

### 0) Define North Star (before doing "work")
- Confirm target business outcomes, non-goals, and constraints (cost/latency/compliance/languages/channels).
- Define "Definition of Success" (metrics + acceptance principle).
- **Visual artifact**: Project context map / stakeholder map → use `drawio-skill`.

### 1) Requirements Discovery (需求调研)
- Elicit scenarios, user journeys, edge cases, escalation, and integrations.
- Inventory data sources (FAQ/docs/VOC/tickets/error codes/workflows) and access constraints.
- Freeze a first-pass taxonomy (problem types + labels + entity glossary) as *v1*.
- **Visual artifacts**: Scenario flow diagram + taxonomy tree → use `fireworks-tech-graph`.

### 2) SOW / Scope Freeze (SOW确认)
- Convert discovery into: scope, assumptions, out-of-scope, deliverables, milestones, responsibilities (RACI), and acceptance gates.
- Lock change-control: what counts as a change, how to approve, and how it affects timeline/cost.
- **Visual artifact**: RACI swimlane diagram → use `drawio-skill`.

### 3) Delivery Readiness (交付就绪)
- Security/legal/compliance alignment (PII, retention, logging, redaction).
- Environments/accounts/network/SSO readiness.
- Data readiness: cleaning rules, chunking/template standard, versioning & conflict governance.
- **Visual artifact**: Deployment topology diagram → use `drawio-skill`.

### 4) Model Deployment (模型部署)
- Decide hosting boundary (cloud/on-prem), cost/latency budget, fallback strategy, and safety rails.
- Validate: connectivity, auth, rate limits, observability hooks, rollback.

### 5) Platform Deployment (软件平台部署)
- Deploy/validate agent runtime, knowledge base service, vector/keyword indexes, tool gateway, and audit/trace.
- Define the minimum observability schema (trace fields, evidence, tool calls, escalation reason).
- **Visual artifact**: C4 system architecture (Context → Container → Component) → use `drawio-skill`.

### 6) Engineering Delivery (工程实施交付)
- Knowledge engineering: taxonomy freeze → chunking template → quality gate → indexing strategy → retrieval/threshold/degeneration rules.
- Agent building: dialog policy, tool integration, escalation, multilingual handling, safety & refusal behaviors.
- **Visual artifacts**: Agent architecture diagram + RAG data flow diagram → use `fireworks-tech-graph`.

### 7) Evaluation, UAT (评估验收)
- Build evaluation sets early; run offline eval before UAT to prevent "验收漂移".
- Define UAT checklist and go/no-go criteria.
- **Visual artifact**: Evaluation metrics dashboard mockup → use `fireworks-tech-graph`.

### 7.5) Deliverable Packaging (交付物打包)
- Compile all phase artifacts into a structured **client-facing document** (Markdown → DOCX) with embedded diagrams.
- Generate an **executive presentation deck** (PPTX) with key findings, architecture, metrics, and roadmap.
- Embed all diagrams produced throughout the project (from Phases 0-7) into the doc and PPT.
- Produce a final delivery package: DOCX + PPTX + all `.drawio`/`.svg` source files + templates.
- See `references/diagram-guide.md` for diagram skill selection and `references/output-patterns.md` for packaging patterns.
- **Templates**: `07_deliverable_packaging.md`, `08_diagram_manifest.md`.

### 8) Go-Live & Operations (上线与运营)
- Prepare cutover, on-call, runbook, and rollback plan.
- Define release cadence, knowledge update governance, badcase triage loop, SLA/SLO, and dashboards.
- Keep a "single source of truth" for versions, changes, and regressions.
- **Visual artifact**: Cutover/rollback flowchart + ops runbook flow → use `drawio-skill`.

## How to Use This Skill Efficiently

- If the user needs a *plan*: produce phase-by-phase milestones + gates using `references/lifecycle-checkpoints.md`.
- If the user needs *artifacts*: copy/instantiate templates from `assets/templates/` (or run the scaffold script).
- If the user needs *diagrams*: consult `references/diagram-guide.md` for which skill to use at each phase, then invoke `drawio-skill` or `fireworks-tech-graph` accordingly.
- If the user needs *client deliverables*: use Phase 7.5 to compile DOCX + PPTX with embedded diagrams.
- If scope is ambiguous: ask only the "fewest questions that unblock the next gate", then proceed.
- If anything is uncertain: explicitly mark it as `（待确认）` / `TBD` to avoid false precision.

## Bundled Resources

### scripts/
- `scripts/scaffold_artifacts.py`: generate a ready-to-edit artifact pack from `assets/templates/`, including a diagram manifest and deliverable packaging scaffolding.

### references/
- `references/lifecycle-checkpoints.md`: phase checklist (inputs/outputs, DoR/DoD, gates) — now includes visual artifact outputs per phase.
- `references/discovery-min-questions.md`: minimal question set to unblock each phase.
- `references/output-patterns.md`: recommended output formats (milestone plan, RACI, gate checklist, diagram manifest, deliverable packaging).
- `references/diagram-guide.md`: when/how to use `drawio-skill` and `fireworks-tech-graph` for each phase's visual artifacts.

### assets/
- `assets/templates/`: markdown templates (discovery, SOW, milestones, RACI, acceptance, runbook, deliverable packaging, diagram manifest).
