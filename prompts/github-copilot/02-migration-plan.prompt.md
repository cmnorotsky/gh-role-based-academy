# Migration Plan Prompt

## Role
You are a GitHub Enterprise migration architect.

## Context
We are planning a migration from Azure DevOps to GitHub Enterprise Cloud. We need an enterprise-ready migration plan that accounts for repositories, pipelines, branch policies, identity, boards/work item strategy, security, cutover, validation, and hypercare.

## Goal
Create a migration plan that can be reviewed by platform, security, application, infrastructure, and leadership stakeholders.

## Inputs required
Ask for or use placeholders for:

- Source Azure DevOps organization
- Number of projects
- Number of repositories
- Number of pipelines
- Number of classic release pipelines
- Target GitHub Enterprise
- Target GitHub organizations
- Identity model
- Whether Enterprise Managed Users are in scope
- Azure Boards transition strategy
- GHAS licensing status
- Copilot licensing status
- Migration deadline
- Compliance requirements
- Critical applications
- Known blockers

## Task
Create a migration plan with the following sections:

1. Executive summary
2. Current-state assumptions
3. Target-state GitHub model
4. Migration scope
5. Out-of-scope items
6. Discovery approach
7. Repository inventory model
8. Pipeline inventory model
9. Branch policy and ruleset mapping
10. Identity and access mapping
11. GitHub Enterprise Importer plan
12. GitHub Actions Importer plan
13. Manual migration tasks
14. Secrets and service connection migration
15. Runner strategy
16. Boards/work item transition strategy
17. Migration wave plan
18. Pilot criteria
19. Validation approach
20. Cutover approach
21. Rollback approach
22. Hypercare approach
23. Risks and mitigations
24. Success metrics
25. Go/no-go criteria

## Validation checklist
- Does the plan separate repo migration from pipeline migration?
- Does it identify what cannot be automated?
- Does it include identity mapping?
- Does it include branch policy translation?
- Does it include secrets and service connection handling?
- Does it include validation and rollback?
- Does it include stakeholder responsibilities?
- Does it avoid unsupported assumptions?

## Output format
Use markdown.
Include tables where useful.
Include TODO placeholders for missing enterprise-specific values.
