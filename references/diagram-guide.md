# Diagram Guide — When and How to Use Visual Skills

This guide maps each phase's visual artifact to the appropriate skill (`drawio-skill` or `fireworks-tech-graph`) with specific diagram types, recommended export formats, and practical tips.

## Skill Selection Principles

| Use `drawio-skill` when | Use `fireworks-tech-graph` when |
|---|---|
| Need polished, client-facing diagrams with precise geometry | Need quick, SVG-native technical diagrams |
| C4 models, swimlanes, network topology | Agent architecture, data flow, comparison matrices |
| Need `.drawio` source for ongoing editing | Need lightweight SVG that renders in Markdown/GitHub |
| Need multi-page drill-down (C4 Context → Container → Component) | Need one of 8 built-in style presets (dark, blueprint, etc.) |
| Need export to PNG/SVG/PDF with embedded XML | Need Python-based generation with validation pipeline |
| Need sequence diagrams with deterministic layout | Need arrow semantics by flow type (data, control, memory) |

**When in doubt**: Use `drawio-skill` for external/client deliverables; use `fireworks-tech-graph` for internal/technical diagrams.

---

## Phase-by-Phase Diagram Guide

### Phase 0: North Star — Project Context Map

| Attribute | Value |
|---|---|
| **What** | Shows stakeholders, business goals, and scope boundary |
| **Skill** | `drawio-skill` |
| **Diagram type** | Architecture diagram or mind map |
| **Key nodes** | Business goals, non-goals, constraints, stakeholder groups |
| **Export** | `.drawio` + `.drawio.png` (embedded) |
| **Tips** | Keep it high-level; this is for executive alignment, not technical detail |

### Phase 1: Discovery — Scenario Flow Diagram

| Attribute | Value |
|---|---|
| **What** | Flowchart of top scenarios (happy path + escalation) |
| **Skill** | `fireworks-tech-graph` |
| **Diagram type** | Flowchart / Process Flow |
| **Key nodes** | User entry → intent classification → self-serve path / escalation path |
| **Export** | `.svg` + `.png` |
| **Style** | Style 1 (Flat Icon) or Style 6 (Claude Official) |
| **Tips** | Use diamond shapes for decision points (escalate vs self-serve); label arrows with trigger conditions |

### Phase 1: Discovery — Taxonomy Tree

| Attribute | Value |
|---|---|
| **What** | Visual taxonomy of problem types, intents, and entities |
| **Skill** | `fireworks-tech-graph` |
| **Diagram type** | Mind Map / Concept Map |
| **Key nodes** | Root: problem domain → level 1: intent categories → level 2: specific intents + entities |
| **Export** | `.svg` + `.png` |
| **Tips** | Central node = project/product name; first-level branches = top intent categories |

### Phase 2: SOW — RACI Swimlane Diagram

| Attribute | Value |
|---|---|
| **What** | Visual representation of RACI responsibilities across phases |
| **Skill** | `drawio-skill` |
| **Diagram type** | Cross-Functional Flowchart / Swimlane |
| **Key nodes** | Swimlane rows = role groups (Biz, IT, Delivery, Platform, Ops); columns = phases/work items |
| **Export** | `.drawio` + `.drawio.png` |
| **Tips** | Use R/A/C/I badges in cells; color-code by accountability (R=blue, A=red, C=yellow, I=gray) |

### Phase 3: Readiness — Deployment Topology

| Attribute | Value |
|---|---|
| **What** | Network topology showing environments, services, and data flows |
| **Skill** | `drawio-skill` |
| **Diagram type** | Network Topology |
| **Key nodes** | Environments (dev/staging/prod), services, databases, firewalls, LB |
| **Export** | `.drawio` + `.drawio.png` |
| **Tips** | Use official cloud icons (AWS/Azure/GCP) via `shapesearch.py`; group by environment |

### Phase 5: Platform Deploy — C4 System Architecture

| Attribute | Value |
|---|---|
| **What** | C4 model: System Context → Container → Component (multi-page with drill-down) |
| **Skill** | `drawio-skill` |
| **Diagram type** | C4 Model |
| **Key nodes** | Context: external actors + system; Container: agent runtime, KB, tool gateway, observability; Component: per-container internals |
| **Export** | `.drawio` (multi-page) + `.drawio.png` per page |
| **Tips** | Use `scripts/c4.py` for structured C4 generation; add click-to-drill-down links between pages |

### Phase 6: Engineering — Agent Architecture Diagram

| Attribute | Value |
|---|---|
| **What** | Shows how the agent reasons, uses tools, and manages memory |
| **Skill** | `fireworks-tech-graph` |
| **Diagram type** | Agent Architecture |
| **Key layers** | Input → Agent core (LLM + reasoning loop) → Memory (short/long-term) → Tool layer → Output |
| **Export** | `.svg` + `.png` |
| **Tips** | Use cyclic arrows for iterative reasoning; separate memory types visually (dashed = ephemeral, solid = persistent) |

### Phase 6: Engineering — RAG Data Flow Diagram

| Attribute | Value |
|---|---|
| **What** | Data flow from query through retrieval to response |
| **Skill** | `fireworks-tech-graph` |
| **Diagram type** | Data Flow |
| **Key nodes** | Query → Embed → VectorSearch → Retrieve → Rerank → Augment → LLM → Response |
| **Export** | `.svg` + `.png` |
| **Tips** | Label every arrow with data type; use wider strokes for primary data paths; use `fireworks-tech-graph` arrow semantics (blue=data, green=memory, orange=control) |

### Phase 7: Eval — Evaluation Metrics Dashboard

| Attribute | Value |
|---|---|
| **What** | Visual summary of eval metrics and go/no-go thresholds |
| **Skill** | `fireworks-tech-graph` |
| **Diagram type** | Comparison / Feature Matrix or Timeline |
| **Key content** | Metric name, baseline, current, threshold, pass/fail |
| **Export** | `.svg` + `.png` |
| **Tips** | Use green/red tinting for pass/fail cells; include a legend |

### Phase 8: Go-Live — Cutover/Rollback Flowchart

| Attribute | Value |
|---|---|
| **What** | Step-by-step cutover and rollback decision flow |
| **Skill** | `drawio-skill` |
| **Diagram type** | Flowchart |
| **Key nodes** | Entry criteria check → cutover steps → monitoring → decision (proceed/rollback) → rollback steps |
| **Export** | `.drawio` + `.drawio.png` |
| **Tips** | Use red for rollback path, green for proceed path; include "stop-the-line" signals as decision diamonds |

### Phase 8: Go-Live — Ops Runbook Flow

| Attribute | Value |
|---|---|
| **What** | Decision tree for operations triage and incident response |
| **Skill** | `drawio-skill` |
| **Diagram type** | Flowchart (or BPMN) |
| **Key nodes** | Incident detection → severity classification → triage path → resolution/escalation |
| **Export** | `.drawio` + `.drawio.png` |
| **Tips** | Consider using `scripts/runbook.py` to turn the flowchart into a click-through triage app |

---

## Phase 7.5: Packaging — Diagram Embedding

When compiling deliverables in Phase 7.5:

1. **Gather all diagram files**: Reference `08_diagram_manifest.md` for the complete list.
2. **Export for DOCX embedding**: Use PNG (300 DPI recommended) for Word compatibility.
3. **Export for PPT embedding**: Use PNG or SVG (SVG scales better on modern PowerPoint).
4. **Maintain source files**: Always include `.drawio` and `.svg` source files in the delivery package for future editing.
5. **Version control**: Tag diagram versions with the project version (e.g., `architecture_v1.2.drawio`).

### DOCX Diagram Placement

| Diagram | Suggested section | Caption |
|---|---|---|
| Context map | 1. Project Overview | Figure 1: Project Context & Stakeholders |
| Scenario flow | 2. Requirements Discovery | Figure 2: Top Scenario Flow |
| Taxonomy tree | 2. Requirements Discovery | Figure 3: Problem Taxonomy (v1) |
| RACI swimlane | 3. SOW & Scope | Figure 4: RACI Responsibility Matrix |
| Deployment topology | 4. Delivery Readiness | Figure 5: Deployment Topology |
| C4 architecture | 5. Platform Architecture | Figure 6–8: C4 Model (Context/Container/Component) |
| Agent architecture | 6. Engineering Delivery | Figure 9: Agent Architecture |
| RAG data flow | 6. Engineering Delivery | Figure 10: RAG Data Flow |
| Eval dashboard | 7. Evaluation Results | Figure 11: Evaluation Metrics Summary |
| Cutover flowchart | 8. Go-Live Plan | Figure 12: Cutover & Rollback Procedure |
| Ops runbook | 8. Operations | Figure 13: Operations Runbook Flow |

### PPT Diagram Placement

See `references/output-patterns.md` → "PPT Deck Outline" for the recommended slide-by-slide mapping.
