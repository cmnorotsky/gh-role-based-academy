# Governance Model

## Enterprise structure
- Define enterprise and org boundaries
- Align orgs to business units or domains

## Org strategy
- Central platform org plus product orgs
- Shared templates and workflows

## Repo naming
- Use consistent prefixes and ownership tags
- Example: <domain>-<service>-<type>

## Team naming
- Use domain and role in names
- Example: team-<domain>-<role>

## Permission model
- Least privilege by default
- Use teams, not individual user grants

## Rulesets
- Require PR review and status checks
- Restrict force push and branch deletion

## Branch protections
- Protect main branches and release branches

## Required checks
- Build, tests, security scan, lint

## Environments
- Use approvals for production
- Separate dev/test/prod

## Approvals
- Require code owner or security approval for sensitive changes

## Secrets
- Use Actions secrets or environment secrets
- Avoid long-lived secrets; prefer OIDC

## Variables
- Use environment variables for non-sensitive config

## Audit logging
- Central audit log review cadence

## Cost management
- Monitor Actions and Copilot usage

## Copilot policy
- Define acceptable use and data handling

## GHAS policy
- Required scanning and triage SLAs

## Repository lifecycle
- Standardize repo creation and archiving
