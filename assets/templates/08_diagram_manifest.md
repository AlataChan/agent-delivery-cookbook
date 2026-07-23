# {{PROJECT_NAME}} — Diagram Manifest (v{{VERSION}})

Date: {{DATE}}

> Tracks all visual artifacts produced throughout the project. Each diagram must reference its source file, the skill used, and placement in the final deliverables.

## How to Use

1. **During each phase**: Fill in the diagram details as it's produced.
2. **At Phase 7.5**: Verify all diagrams are accounted for and embedded in the DOCX/PPT.
3. **Post-delivery**: Archive with the delivery package for future reference and editing.

## Phase 0: North Star

| Diagram name | Skill | Diagram type | Source file | Export format | DOCX section | PPT slide | Status |
|---|---|---|---|---|---|---|---|
| Project context map | drawio-skill | Architecture / Mind map | TBD | .drawio + .png | §1 | Slide 2 | TBD |

## Phase 1: Discovery

| Diagram name | Skill | Diagram type | Source file | Export format | DOCX section | PPT slide | Status |
|---|---|---|---|---|---|---|---|
| Scenario flow diagram | fireworks-tech-graph | Flowchart | TBD | .svg + .png | §2 | — | TBD |
| Taxonomy tree | fireworks-tech-graph | Mind map | TBD | .svg + .png | §2 | — | TBD |

## Phase 2: SOW

| Diagram name | Skill | Diagram type | Source file | Export format | DOCX section | PPT slide | Status |
|---|---|---|---|---|---|---|---|
| RACI swimlane | drawio-skill | Swimlane | TBD | .drawio + .png | §3 | Slide 4 | TBD |

## Phase 3: Readiness

| Diagram name | Skill | Diagram type | Source file | Export format | DOCX section | PPT slide | Status |
|---|---|---|---|---|---|---|---|
| Deployment topology | drawio-skill | Network topology | TBD | .drawio + .png | §4 | Slide 8 | TBD |

## Phase 5: Platform Deploy

| Diagram name | Skill | Diagram type | Source file | Export format | DOCX section | PPT slide | Status |
|---|---|---|---|---|---|---|---|
| C4 — System Context | drawio-skill | C4 (page 1) | TBD | .drawio + .png | §5 | Slide 5 | TBD |
| C4 — Container | drawio-skill | C4 (page 2) | TBD | .drawio + .png | §5 | Slide 5 | TBD |
| C4 — Component | drawio-skill | C4 (page 3) | TBD | .drawio + .png | §5 | Slide 5 | TBD |

## Phase 6: Engineering

| Diagram name | Skill | Diagram type | Source file | Export format | DOCX section | PPT slide | Status |
|---|---|---|---|---|---|---|---|
| Agent architecture | fireworks-tech-graph | Agent architecture | TBD | .svg + .png | §6 | Slide 6 | TBD |
| RAG data flow | fireworks-tech-graph | Data flow | TBD | .svg + .png | §6 | Slide 6 | TBD |

## Phase 7: Evaluation

| Diagram name | Skill | Diagram type | Source file | Export format | DOCX section | PPT slide | Status |
|---|---|---|---|---|---|---|---|
| Eval dashboard mockup | fireworks-tech-graph | Comparison matrix | TBD | .svg + .png | §7 | Slide 7 | TBD |

## Phase 8: Go-Live

| Diagram name | Skill | Diagram type | Source file | Export format | DOCX section | PPT slide | Status |
|---|---|---|---|---|---|---|---|
| Cutover/rollback flowchart | drawio-skill | Flowchart | TBD | .drawio + .png | §8 | Slide 9 | TBD |
| Ops runbook flow | drawio-skill | Flowchart / BPMN | TBD | .drawio + .png | §8 | — | TBD |

## Summary

| Skill | Diagrams produced | Source files | Embedded in DOCX | Embedded in PPT |
|---|---|---|---|---|
| drawio-skill | TBD | TBD | TBD | TBD |
| fireworks-tech-graph | TBD | TBD | TBD | TBD |
| **Total** | TBD | TBD | TBD | TBD |

## Notes

- All `.drawio` files should be editable in draw.io desktop (use `-e` flag for embedded XML).
- All `.svg` files should be valid (run `validate-svg.sh` from fireworks-tech-graph).
- All `.png` exports for DOCX should be at least 300 DPI.
- All `.png` exports for PPT should be at least 200 DPI (or use SVG for modern PowerPoint).
