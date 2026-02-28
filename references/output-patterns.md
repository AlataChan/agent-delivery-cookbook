# Output Patterns (copy/paste friendly)

Use these formats to keep deliverables consistent across projects.

## 1) Milestones & Gates (table)

| Phase | Gate name | Key outputs (deliverables) | Owner roles | Target date | Status |
|---|---|---|---|---|---|
| 0 | North Star Gate | Project charter v0, success metrics draft, risk register v0 | Biz owner / Delivery lead | TBD | TBD |
| 1 | Discovery Gate | Scenario catalog, taxonomy v1, data inventory | Biz SME / Knowledge lead | TBD | TBD |
| 2 | SOW Freeze Gate | SOW, RACI, change control | PM / Biz owner | TBD | TBD |
| 3 | Readiness Gate | Access checklist, data governance, observability schema | IT/Sec / Delivery | TBD | TBD |
| 4 | Model Deploy Gate | Runtime ready, safety/compliance, baseline perf | Platform/vendor | TBD | TBD |
| 5 | Platform Deploy Gate | Runtime+KB+index stack, tool gateway, audit/trace | Platform/vendor | TBD | TBD |
| 6 | Delivery Gate | chunking v1, retrieval policy v1, agent policy v1 | Delivery / Product | TBD | TBD |
| 7 | UAT Gate | eval set, metrics, UAT checklist, regression loop | QA / Biz sign-off | TBD | TBD |
| 8 | Go-Live Gate | runbook, on-call, monitoring, rollback | Ops / Delivery | TBD | TBD |

## 2) Gate Checklist (DoR/DoD)

**Gate:** `<Gate Name>`

- **Inputs (DoR)**
  - [ ] …
- **Outputs**
  - [ ] …
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

