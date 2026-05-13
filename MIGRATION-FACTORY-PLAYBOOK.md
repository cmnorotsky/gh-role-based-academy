# Migration Factory Playbook

## Discovery
- Collect ADO org, project, repo, pipeline lists
- Identify business critical systems

## Inventory
- Use inventory templates and scripts
- Record repo size, history, branch count

## Readiness scoring
- Score by size, pipeline complexity, risk

## Migration waves
- Define pilot, low, medium, high complexity waves

## GitHub Enterprise Importer planning
- Decide on GEI approach for repo migration
- Document limitations and manual steps

## GitHub Actions Importer planning
- Assess pipeline conversion
- Identify manual gaps (secrets, approvals, release gates)

## ADO Boards transition strategy
- Decide on dual-tracking or cutover

## Identity mapping
- Map ADO users to GitHub identities
- Define EMU mapping if applicable

## Branch policy translation
- Map ADO policies to GitHub rulesets

## Repo rulesets
- Define required checks and review rules

## Secrets migration
- Use OIDC and approved secret stores
- Never copy secrets to files

## Service connections to OIDC
- Use federated identity for Azure

## Runner strategy
- Decide hosted vs self-hosted

## Validation
- Validate repo integrity and pipeline runs

## Cutover
- Freeze windows, coordinate DNS and releases

## Hypercare
- Define support window and issue handling

## Rollback strategy
- Define criteria and rollback steps

## Executive reporting
- Weekly wave status and risks
