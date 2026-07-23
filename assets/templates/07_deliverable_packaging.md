# {{PROJECT_NAME}} — Deliverable Packaging (v{{VERSION}})

Date: {{DATE}}

> This template covers Phase 7.5: compiling all project artifacts into client-facing deliverables (DOCX + PPTX).

## 1) Delivery Package Contents

### Document (DOCX)
- [ ] Title page with project name, client, date, version
- [ ] Table of contents
- [ ] Section 1: Project Overview (from `00_project_charter.md` + context map diagram)
- [ ] Section 2: Requirements Discovery (from `01_discovery_notes.md` + scenario flow + taxonomy diagrams)
- [ ] Section 3: SOW & Scope (from `02_sow_scope_freeze.md` + RACI swimlane diagram)
- [ ] Section 4: Delivery Readiness (access/security checklist + deployment topology diagram)
- [ ] Section 5: Platform Architecture (C4 model diagrams)
- [ ] Section 6: Engineering Delivery (chunking/retrieval/agent policy + agent arch + RAG flow diagrams)
- [ ] Section 7: Evaluation Results (from `05_acceptance_eval_plan.md` + dashboard mockup diagram)
- [ ] Section 8: Go-Live Plan (from `06_cutover_runbook.md` + cutover flowchart + ops runbook diagrams)
- [ ] Appendices: Diagram sources, template versions, change log

### Presentation (PPTX)
- [ ] Slide 1: Title (project name, client, date)
- [ ] Slide 2: Executive summary (charter goals + success metrics + context map)
- [ ] Slide 3: Scope & approach (SOW scope + milestone plan)
- [ ] Slide 4: RACI & responsibilities (RACI table + swimlane diagram)
- [ ] Slide 5: Architecture overview (C4 architecture)
- [ ] Slide 6: Agent & data flow (agent architecture + RAG flow)
- [ ] Slide 7: Evaluation results (metrics + dashboard mockup)
- [ ] Slide 8: Deployment topology (topology diagram)
- [ ] Slide 9: Cutover & rollback (cutover flowchart)
- [ ] Slide 10: Roadmap & next steps (operations plan)

## 2) Diagram Manifest (cross-reference)

> Fill from `08_diagram_manifest.md`. Every diagram must have a source file and at least one placement (DOCX section or PPT slide).

| Diagram | Source file | DOCX section | PPT slide | Status |
|---|---|---|---|---|
| Project context map | TBD | §1 | Slide 2 | TBD |
| Scenario flow diagram | TBD | §2 | — | TBD |
| Taxonomy tree | TBD | §2 | — | TBD |
| RACI swimlane | TBD | §3 | Slide 4 | TBD |
| Deployment topology | TBD | §4 | Slide 8 | TBD |
| C4 architecture (Context) | TBD | §5 | Slide 5 | TBD |
| C4 architecture (Container) | TBD | §5 | Slide 5 | TBD |
| C4 architecture (Component) | TBD | §5 | Slide 5 | TBD |
| Agent architecture | TBD | §6 | Slide 6 | TBD |
| RAG data flow | TBD | §6 | Slide 6 | TBD |
| Eval dashboard mockup | TBD | §7 | Slide 7 | TBD |
| Cutover/rollback flowchart | TBD | §8 | Slide 9 | TBD |
| Ops runbook flow | TBD | §8 | — | TBD |

## 3) Export Settings

### Diagrams → DOCX
- Format: PNG at 300 DPI
- Max width: 6.5 inches (Word page width minus margins)
- Caption format: "Figure N: <description>"
- Source files preserved in delivery package

### Diagrams → PPT
- Format: PNG at 200 DPI (or SVG for modern PowerPoint)
- Max width: 10 inches (slide width minus margins)
- Alt text: diagram name + brief description for accessibility

## 4) Quality Gates

- [ ] All diagrams render correctly in both DOCX and PPTX
- [ ] Document has no broken image references
- [ ] PPT slides are not overcrowded (max 2 diagrams per slide)
- [ ] All source files (`.drawio`, `.svg`) are included in delivery package
- [ ] Diagram manifest is complete and accurate
- [ ] Delivery package is versioned and stored in agreed location

## 5) Approval

- [ ] Delivery lead review: TBD
- [ ] Client review (if applicable): TBD
- [ ] Final version tag: TBD
