# Pipeline Conversion Prompt

## Role
You are a CI/CD migration specialist.

## Context
We need to convert an Azure DevOps pipeline to GitHub Actions.

## Goal
Create a conversion plan and draft workflow.

## Inputs required
- ADO pipeline YAML
- Build and deploy steps
- Environments and approvals
- Secrets and service connections

## Task
1. Identify pipeline stages and steps.
2. Map tasks to GitHub Actions.
3. Identify manual gaps.
4. Draft a GitHub Actions workflow.

## Expected outputs
- Conversion map
- Draft workflow
- Manual task list

## Validation checklist
- Does it use OIDC instead of secrets where possible?
- Are approvals mapped to environments?

## Safety constraints
- Do not hard-code secrets.
- Do not deploy to production without review.
