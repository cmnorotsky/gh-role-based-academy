# Lab 02: Reusable Workflows

## Objective
Create a reusable workflow and call it.

## Target audience
DevOps, platform

## Prerequisites
- Lab 01

## Estimated time
2 hours

## Tools required
- GitHub Actions

## Step-by-step lab
1. Create a reusable workflow in `.github/workflows/reusable-build.yml`.
2. Call it from another workflow using `workflow_call`.
3. Pass inputs and secrets.
4. Open a PR and run the workflow.

## Common mistakes
- Not exposing required inputs

## Evidence to submit
- PR link and run logs

## Review checklist
- Reusable workflow is versioned and documented

## Definition of done
- Workflow executes from caller
