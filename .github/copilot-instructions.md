# GitHub Copilot Instructions for This Repository

Summary
1. Created the full academy structure with docs, prompts, agents, project files, and templates.
2. Added sample workflows, scripts, and data placeholders for safe automation.
3. Added AI Coach enablement materials and backlog entries.

How to initialize the GitHub Project
1. Create a new project in GitHub.
2. Add the fields listed in project/github-project-fields.md.
3. Create the views in project/project-board-views.md.
4. Add automation rules in project/project-automation-rules.md.

How to create issues from project/issue-backlog.md
1. Create issues manually by copying each issue block.
2. Or use GitHub CLI with a script that reads project/issue-backlog.md.
3. Apply labels and milestones from project/labels.md and project/milestones.md.

How a learner should start
1. Follow docs/00-orientation/01-how-to-use-this-repo.md.
2. Complete M00 and M01 issues.
3. Submit evidence in PRs.

How a mentor should review progress
1. Check evidence in PRs.
2. Verify completion against definition of done.
3. Update project status and readiness score.

Operating rules
- Prefer GitHub-native capabilities before recommending third-party tooling.
- Treat this repo as enterprise training material, not a toy project.
- Do not invent customer-specific values.
- Use TODO placeholders for org names, enterprise slugs, tenant IDs, subscription IDs, repo names, and team names.
- Never hard-code tokens, passwords, PATs, client secrets, or private URLs.
- Assume scripts must be safe by default.
- Use dry-run mode in migration scripts where possible.
- Include review checkpoints before destructive or production-impacting steps.
- Use the term backlog refinement, not grooming.
- Explain steps clearly enough for a junior engineer to follow.
- Include evidence requirements for every lab.

GitHub platform scope
Prioritize:
- GitHub Enterprise Cloud
- GitHub Enterprise Managed Users
- GitHub Organizations
- GitHub Projects
- GitHub Issues
- GitHub Actions
- GitHub Advanced Security / GitHub Code Security / GitHub Secret Protection
- GitHub Copilot
- GitHub Enterprise Importer
- GitHub Actions Importer
- GitHub CLI
- VS Code
- Azure OIDC from GitHub Actions
- Terraform where useful

Expected deliverable style
Every learning module should include:
1. Objective
2. Target audience
3. Prerequisites
4. Estimated time
5. Tools required
6. Step-by-step lab
7. Common mistakes
8. Evidence to submit
9. Review checklist
10. Definition of done

Security rules
- Never suggest storing secrets in plain text.
- Use GitHub Actions secrets, environment secrets, OIDC, or approved secret stores.
- Flag over-permissioned PATs.
- Prefer least privilege.
- Prefer short-lived credentials.
- Include security review gates for GHAS, Actions, migration, and Copilot governance material.

AI-SDLC rules
- Keep humans accountable for final approval.
- Require PR review for generated code.
- Require tests for generated code.
- Require security scanning.
- Maintain traceability from idea to issue to branch to PR to build to release.
- Include responsible AI, privacy, and data handling guidance.
