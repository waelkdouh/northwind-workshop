---
description: "Squad routing: request patterns mapped to roles, autonomy tiers, and parallel eligibility"
---

# Squad Routing

| Pattern / Keyword                          | Role(s)                      | Autonomy Tier | Parallel-Eligible |
|--------------------------------------------|------------------------------|---------------|-------------------|
| research, investigate, explore, find out   | researcher                   | auto          | yes               |
| plan, break down, sequence, design plan    | lead                         | confirm       | no                |
| implement, build, code, fix                | developer                    | confirm       | no                |
| review, validate, check quality            | tester                       | auto          | yes               |
| brainstorm, ideate, shape this idea, explore options, what should we build, help me think through, we want to, kick off a brief | designer, analyst | confirm | no |
| validate requirements, requirements readiness, requirements complete, requirements clear, intake check, are the requirements ready | intake-validator | auto | yes |
| design, UX, UI, wireframe, journey, interaction design | designer                | confirm       | yes               |
| requirements, BRD, PRD, user story, acceptance criteria | analyst                     | confirm       | yes               |
| journey map, persona, design thinking, empathize, ideate, problem statement | designer | confirm | yes           |
| roadmap, backlog, epic, sprint, prioritize, story, PRD to work items, work item hierarchy | product-owner | confirm    | no                |
| GitLab merge request, GitLab pipeline, GitLab issue, open an MR | product-owner        | escalate      | no                |
| experiment, hypothesis, validate assumption, MVE, riskiest assumption | experimenter        | confirm | yes         |
| presentation, deck, slides, executive summary, pitch | presenter                    | confirm       | no                |
| document, write up, summarize for stakeholders, readme | technical-writer           | confirm       | no                |
| data profile, data dictionary, EDA, exploratory analysis, notebook, dashboard, dataset, Power BI, DAX, semantic model, star schema, report design, Fabric, Lakehouse, OneLake | data-scientist | confirm | no |
| validate, cross-check, pre-implementation review, council, design review, go/no-go, implement-and-cost, implement-and-risk | architect, security, cost-manager, product-owner, rai (optional) | confirm | yes |
