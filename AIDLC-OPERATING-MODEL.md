# AI-SDLC Operating Model

## Requirements as code
- Store requirements in markdown with version control
- Link issues to requirements files

## Architecture as code
- Use ADRs and diagrams under version control
- Review architecture changes in PRs

## Tests as code
- Treat tests as first-class deliverables
- Require tests for AI-generated code

## Security as code
- Use GHAS, CodeQL, dependency review, secret scanning

## Compliance evidence as code
- Store evidence in repo and link to issues/PRs

## PR-based governance
- All changes reviewed via PRs
- Require approvals and checks

## Agent/persona files
- Store persona rules in prompts/agents

## Prompt files
- Store reusable prompts in prompts/github-copilot

## Human approval gates
- Require approval for production changes
- Include security review and testing checkpoints

## Traceability
- Maintain traceability from idea to issue to branch to PR to release
