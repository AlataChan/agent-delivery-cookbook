# Output Patterns (copy/paste friendly)

Use these formats to keep deliverables consistent across projects.

## 1) Milestones & Gates (table)

| Phase | Gate name | Key outputs (deliverables) | Visual artifacts | Owner roles | Target date | Status |
|---|---|---|---|---|---|---|
| 0 | North Star Gate | Project charter v0, success metrics draft, risk register v0 | Context map (drawio) | Biz owner / Delivery lead | TBD | TBD |
| 1 | Discovery Gate | Scenario catalog, taxonomy v1, data inventory | Scenario flow + taxonomy tree (fireworks) | Biz SME / Knowledge lead | TBD | TBD |
| 2 | SOW Freeze Gate | SOW, RACI, change control | RACI swimlane (drawio) | PM / Biz owner | TBD | TBD |
| 3 | Readiness Gate | Access checklist, data governance, observability schema | Deployment topology (drawio) | IT/Sec / Delivery | TBD | TBD |
| 4 | Model Deploy Gate | Runtime ready, safety/compliance, baseline perf | — | Platform/vendor | TBD | TBD |
| 5 | Platform Deploy Gate | Runtime+KB+index stack, tool gateway, audit/trace | C4 architecture (drawio) | Platform/vendor | TBD | TBD |
| 6 | Delivery Gate | chunking v1, retrieval policy v1, agent policy v1 | Agent arch + RAG flow (fireworks) | Delivery / Product | TBD | TBD |
| 7 | UAT Gate | eval set, metrics, UAT checklist, regression loop | Dashboard mockup (fireworks) | QA / Biz sign-off | TBD | TBD |
| 7.5 | Packaging Gate | DOCX + PPTX + delivery package | All diagrams embedded | Delivery lead | TBD | TBD |
| 8 | Go-Live Gate | runbook, on-call, monitoring, rollback | Cutover flowchart (drawio) | Ops / Delivery | TBD | TBD |

## 2) Gate Checklist (DoR/DoD)

**Gate:** `<Gate Name>`

- **Inputs (DoR)**
  - [ ] …
- **Outputs**
  - [ ] …
  - [ ] **Visual artifact**: `<diagram name>` (`<skill>`)
- **Exit criteria (DoD)**
  - [ ] …
- **Open risks / blockers**
  - [ ] …

## 3) RACI (compact)

R=Responsible (do) · A=Accountable (sign off) · C=Consulted · I=Informed

| Work item | Client Biz/SME | Client IT/Sec | Delivery/Vendor | Platform/OEM | Ops |
|---|---|---|---|---|---|
| Taxonomy & labels | A/C | I | R | C | C |
| Chunking template & QA gate | A | I | R | C | C |
| Retrieval policy & thresholds | C | I | A/R | C | I |
| Escalation rules & handoff fields | A/R | I | C | I | A/R |
| Integrations & permissions | C | A/R | R | C | I |
| Observability & replay | C | A/R | R | I | C |
| Evaluation & acceptance | A | I | R | C | A |
| Diagram production | C | C | A/R | C | I |
| Deliverable packaging (DOCX/PPT) | A | I | R | I | I |

## 4) Diagram Manifest

Tracks all visual artifacts produced throughout the project. See `08_diagram_manifest.md` template.

| Phase | Diagram name | Type | Skill | Source file | Used in DOCX | Used in PPT | Status |
|---|---|---|---|---|---|---|---|
| 0 | Project context map | Architecture / Mind map | drawio-skill | TBD | ✓ | ✓ | TBD |
| 1 | Scenario flow diagram | Flowchart | fireworks-tech-graph | TBD | ✓ | — | TBD |
| 1 | Taxonomy tree | Mind map | fireworks-tech-graph | TBD | ✓ | ✓ | TBD |
| 2 | RACI swimlane | Swimlane | drawio-skill | TBD | ✓ | ✓ | TBD |
| 3 | Deployment topology | Network topology | drawio-skill | TBD | ✓ | ✓ | TBD |
| 5 | C4 system architecture | C4 model (multi-page) | drawio-skill | TBD | ✓ | ✓ | TBD |
| 6 | Agent architecture | Agent architecture | fireworks-tech-graph | TBD | ✓ | ✓ | TBD |
| 6 | RAG data flow | Data flow | fireworks-tech-graph | TBD | ✓ | — | TBD |
| 7 | Eval dashboard mockup | Comparison matrix | fireworks-tech-graph | TBD | ✓ | ✓ | TBD |
| 8 | Cutover/rollback flowchart | Flowchart | drawio-skill | TBD | ✓ | — | TBD |
| 8 | Ops runbook flow | Flowchart / BPMN | drawio-skill | TBD | ✓ | — | TBD |

## 5) Deliverable Packaging Structure

```
delivery_package/
├── doc/
│   ├── {project_name}_delivery_report.docx      # Compiled from all phase artifacts
│   └── images/                                   # All diagram PNGs/SVGs embedded in doc
├── ppt/
│   ├── {project_name}_executive_deck.pptx        # Executive presentation
│   └── images/                                   # All diagram PNGs/SVGs embedded in PPT
├── diagrams/
│   ├── *.drawio                                  # All drawio source files
│   └── *.svg                                     # All fireworks-tech-graph SVG sources
├── templates/
│   └── *.md                                      # All filled-in markdown templates
└── manifest/
    └── diagram_manifest.md                       # Completed diagram manifest
```

## 6) PPT Deck Outline (recommended)

| Slide | Section | Content source | Embedded diagram |
|---|---|---|---|
| 1 | Title | Project name, client, date, version | — |
| 2 | Executive summary | Charter goals + success metrics | Context map (Phase 0) |
| 3 | Scope & approach | SOW scope + milestone plan | — |
| 4 | RACI & responsibilities | RACI table | RACI swimlane (Phase 2) |
| 5 | Architecture overview | Platform deployment summary | C4 architecture (Phase 5) |
| 6 | Agent & data flow | Engineering delivery summary | Agent arch + RAG flow (Phase 6) |
| 7 | Evaluation results | Eval metrics + UAT results | Dashboard mockup (Phase 7) |
| 8 | Deployment topology | Readiness + model deploy | Topology (Phase 3) |
| 9 | Cutover & rollback | Go-live plan | Cutover flowchart (Phase 8) |
| 10 | Roadmap & next steps | Operations plan | — |
