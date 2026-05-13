# Lab 04: OIDC to Azure

## Objective
Use OIDC for Azure authentication.

## Target audience
DevOps, platform

## Prerequisites
- Lab 01

## Estimated time
2 hours

## Tools required
- Azure subscription, GitHub Actions

## Step-by-step lab
1. Create an Azure app registration for OIDC.
2. Configure federated credentials.
3. Add workflow using `azure/login` with OIDC.
4. Run a dry-run deployment step.
5. Document required permissions.

## Common mistakes
- Using client secrets instead of OIDC

## Evidence to submit
- Workflow snippet and permissions list

## Review checklist
- Least-privilege permissions defined

## Definition of done
- OIDC authentication works in workflow
