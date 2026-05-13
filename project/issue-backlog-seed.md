# Issue Backlog Seed

Use this file to create GitHub Issues manually or with GitHub CLI.

## M00 Orientation

### 001 - Set up GitHub, VS Code, GitHub CLI, and Copilot

Labels: track:foundations, role:app-dev, role:infra, role:devops, type:lab, cert:foundations  
Milestone: M00 Orientation  
Effort: 2 hours

#### Objective
Prepare the learner workstation for GitHub Enterprise training.

#### Prerequisites
- GitHub account or enterprise-managed account
- VS Code installed
- Git installed
- GitHub CLI installed
- Copilot license assigned, if available

#### Steps
1. Sign in to GitHub.
2. Verify access to the training organization.
3. Install VS Code.
4. Install GitHub Copilot and GitHub Pull Requests extensions.
5. Install GitHub CLI.
6. Run `gh auth login`.
7. Clone this academy repo.
8. Create a branch named `learner/<your-name>/orientation`.
9. Add a file under `evidence/orientation/<your-name>.md`.
10. Open a pull request.

#### Evidence required
- Screenshot or markdown note confirming `gh auth status`
- Link to pull request
- Note confirming Copilot Chat works in VS Code

#### Definition of done
- Learner can clone, branch, commit, push, and open a PR.
- Learner can use Copilot Chat in VS Code.
- Mentor approves PR.

---

### 002 - Complete GitHub Foundations baseline assessment

Labels: track:foundations, role:app-dev, role:infra, role:devops, type:assessment, cert:foundations  
Milestone: M01 Foundations  
Effort: 1 hour

#### Objective
Assess baseline GitHub knowledge.

#### Steps
1. Read `docs/01-foundations/module-overview.md`.
2. Complete the baseline questions in `templates/repo-readiness-scorecard.md`.
3. Create an issue comment summarizing current strengths and gaps.
4. Identify which labs are mandatory for your role.

#### Evidence required
- Completed baseline scorecard
- Comment with personal learning goals

#### Definition of done
- Mentor confirms the learner understands the required path.

---

## M04 Migration Specialist

### 020 - Build an Azure DevOps repository inventory

Labels: track:migration, role:devops, role:architect, type:lab  
Milestone: M04 Migration Specialist  
Effort: 4 hours

#### Objective
Create an inventory model for Azure DevOps repositories before migration.

#### Steps
1. Review `docs/04-migration-specialist/lab-02-repo-inventory.md`.
2. Use `samples/migration-data/sample-repo-inventory.csv`.
3. Add columns for:
   - ADO organization
   - ADO project
   - Repo name
   - Default branch
   - Repo size
   - Branch count
   - PR count
   - Pipeline count
   - Last commit date
   - Archive candidate
   - Migration complexity
   - Target GitHub organization
   - Target GitHub repository
4. Run or review `scripts/migration/repo-inventory.ps1`.
5. Produce a sample inventory output.
6. Identify migration blockers.

#### Evidence required
- Completed sample inventory
- List of blockers
- Recommended migration wave

#### Definition of done
- Inventory is complete enough to support wave planning.
- Mentor can explain why each repo is low, medium, or high complexity.

---

### 021 - Create a migration wave plan

Labels: track:migration, role:devops, role:architect, type:lab  
Milestone: M04 Migration Specialist  
Effort: 4 hours

#### Objective
Group repositories into migration waves.

#### Steps
1. Review the sample repo inventory.
2. Define wave criteria:
   - Business criticality
   - Repo complexity
   - Team readiness
   - Pipeline complexity
   - GHAS risk
   - Dependency relationships
3. Create at least four waves:
   - Pilot
   - Low complexity
   - Medium complexity
   - High complexity
4. Document cutover assumptions.
5. Document rollback assumptions.
6. Create executive summary.

#### Evidence required
- Migration wave spreadsheet or markdown table
- Risk notes
- Go/no-go criteria

#### Definition of done
- Waves are logical, explainable, and reviewable.
- High-risk repos are not placed in the first wave unless intentionally justified.

---

## M05 GHAS Specialist

### 040 - Enable and validate CodeQL code scanning

Labels: track:ghas, role:security, role:app-dev, type:lab, cert:ghas  
Milestone: M05 GHAS Specialist  
Effort: 3 hours

#### Objective
Configure CodeQL code scanning for a sample repo.

#### Steps
1. Review `docs/05-ghas/lab-02-code-scanning-codeql.md`.
2. Add `.github/workflows/codeql-analysis.yml`.
3. Choose target languages.
4. Commit workflow to a feature branch.
5. Open a pull request.
6. Review code scanning results.
7. Triage one sample alert or document why no alert exists.
8. Document remediation workflow.

#### Evidence required
- Pull request link
- CodeQL workflow file
- Screenshot or markdown summary of code scanning result
- Triage notes

#### Definition of done
- Code scanning workflow runs successfully.
- Learner can explain alert ownership and remediation SLA.

---

## M06 Copilot Adoption

### 060 - Build a Copilot adoption and value dashboard model

Labels: track:copilot, role:manager, role:devops, role:architect, type:lab, cert:copilot  
Milestone: M06 Copilot Adoption  
Effort: 4 hours

#### Objective
Define how Copilot adoption and value will be measured.

#### Steps
1. Review `COPILOT-ADOPTION-MODEL.md`.
2. Review `VALUE-MEASUREMENT.md`.
3. Define metrics:
   - Licensed users
   - Active users
   - Engaged users
   - Chat usage
   - Suggestion acceptance
   - Lines accepted
   - PR activity
   - PR cycle time
   - Developer survey score
4. Use `samples/migration-data/sample-copilot-metrics.csv`.
5. Run `scripts/metrics/copilot-usage-sample.py`.
6. Produce a sample monthly adoption report.
7. Identify three enablement actions based on the data.

#### Evidence required
- Sample report
- Metrics interpretation
- Recommended actions

#### Definition of done
- Learner distinguishes usage from value.
- Learner does not claim ROI based only on lines of code.
- Learner includes qualitative and delivery-flow measures.

---

## M07 AI-SDLC

### 070 - Create requirements-as-code using GitHub Issues

Labels: track:aidlc, role:ba-product, role:architect, type:lab  
Milestone: M07 AI-SDLC  
Effort: 3 hours

#### Objective
Use GitHub Issues and markdown requirements to establish traceable requirements-as-code.

#### Steps
1. Review `docs/07-aidlc/lab-01-requirements-as-code.md`.
2. Create a sample epic issue.
3. Create three user story issues.
4. Link stories to the epic.
5. Add acceptance criteria.
6. Add test considerations.
7. Use Copilot Chat to improve clarity.
8. Open a PR adding markdown requirements under `requirements/`.

#### Evidence required
- Epic issue
- Three user stories
- Pull request with requirements markdown
- Traceability notes

#### Definition of done
- Requirements are clear, testable, and linked to delivery work.
- Human review confirms Copilot did not introduce incorrect assumptions.

---

## M09 AI Coach Enablement

### 081 - Define the AI Coach role and client engagement model

Labels: track:ai-coach, role:ai-coach, type:story, cert:copilot  
Milestone: M09 AI Coach Enablement  
Effort: 2 hours

#### Objective
Understand what an AI Coach does when embedded with a client team.

#### Steps
1. Read `AI-COACH-PLAYBOOK.md`.
2. Create a summary of the AI Coach responsibilities.
3. Identify what the coach should and should not do.
4. Describe how the coach supports developers, QA, BAs, architects, DevOps, security, and managers.
5. Create a one-page client-facing explanation of the AI Coach role.

#### Evidence required
- One-page AI Coach role summary
- List of in-scope and out-of-scope responsibilities
- Example client engagement model

#### Definition of done
- Learner can clearly explain that the AI Coach enables teams but does not replace engineering accountability.

---

### 082 - Complete a client AI readiness assessment

Labels: track:ai-coach, role:ai-coach, type:assessment, cert:copilot  
Milestone: M09 AI Coach Enablement  
Effort: 3 hours

#### Objective
Assess whether a client team is ready for Copilot and AI-SDLC enablement.

#### Steps
1. Open `templates/ai-coach-client-readiness-assessment.md`.
2. Assess:
   - License readiness
   - IDE readiness
   - GitHub access
   - Security policy
   - Data handling policy
   - Current SDLC maturity
   - Developer openness
   - Manager support
   - Existing automation
   - GHAS readiness
3. Score the team as low, medium, or high readiness.
4. Identify blockers.
5. Recommend next steps.

#### Evidence required
- Completed readiness assessment
- Risk and blocker list
- Recommended 30-day enablement plan

#### Definition of done
- Assessment is specific enough to support a real coaching plan.

---

### 083 - Shadow a team workflow and identify AI enablement opportunities

Labels: track:ai-coach, role:ai-coach, type:lab, cert:copilot  
Milestone: M09 AI Coach Enablement  
Effort: 4 hours

#### Objective
Observe how a delivery team works and identify practical AI use cases.

#### Steps
1. Review `templates/ai-coach-shadowing-notes.md`.
2. Observe or simulate:
   - Backlog refinement
   - Story writing
   - Development
   - Pull request review
   - Testing
   - Build/deploy
   - Release notes
3. Identify at least ten AI enablement opportunities.
4. Rank them by value and risk.
5. Select three use cases for coaching.

#### Evidence required
- Shadowing notes
- AI opportunity list
- Prioritized coaching backlog

#### Definition of done
- Opportunities are connected to real team work, not generic AI demos.

---

### 084 - Run a developer Copilot coaching session

Labels: track:ai-coach, role:ai-coach, role:app-dev, type:lab, cert:copilot  
Milestone: M09 AI Coach Enablement  
Effort: 3 hours

#### Objective
Coach developers on practical Copilot usage.

#### Steps
1. Prepare a sample coding task.
2. Demonstrate Copilot Chat for code explanation.
3. Demonstrate inline suggestions.
4. Demonstrate prompt refinement.
5. Demonstrate test generation.
6. Demonstrate refactoring assistance.
7. Demonstrate PR description generation.
8. Explain review and validation expectations.
9. Capture developer questions and friction points.

#### Evidence required
- Workshop agenda
- Sample prompts
- Before/after code example
- Follow-up action list

#### Definition of done
- Developers can apply Copilot to a real coding workflow and explain required validation steps.

---

### 085 - Run a BA/Product AI-SDLC coaching session

Labels: track:ai-coach, role:ai-coach, role:ba-product, type:lab  
Milestone: M09 AI Coach Enablement  
Effort: 3 hours

#### Objective
Coach BAs and product owners on AI-assisted requirements work.

#### Steps
1. Start with a vague feature idea.
2. Use Copilot Chat to produce clarifying questions.
3. Convert the idea into an epic.
4. Break the epic into user stories.
5. Add acceptance criteria.
6. Add negative scenarios and edge cases.
7. Add test considerations.
8. Link requirements to GitHub Issues.
9. Explain human review expectations.

#### Evidence required
- Epic
- Three user stories
- Acceptance criteria
- Traceability notes

#### Definition of done
- BA/Product participants can use AI to improve clarity without delegating product judgment to AI.

---

### 086 - Create an AI Coach value report

Labels: track:ai-coach, role:ai-coach, role:manager, type:assessment, cert:copilot  
Milestone: M09 AI Coach Enablement  
Effort: 4 hours

#### Objective
Produce a value report for an AI coaching engagement.

#### Steps
1. Review `templates/ai-coach-value-report.md`.
2. Gather sample adoption data.
3. Gather sample qualitative feedback.
4. Compare baseline and current-state behaviors.
5. Document coaching activities completed.
6. Identify measurable improvements.
7. Identify unproven assumptions.
8. Recommend the next 30 days of enablement.

#### Evidence required
- AI Coach value report
- Metrics table
- Qualitative feedback summary
- Recommended next actions

#### Definition of done
- Report distinguishes adoption, engagement, behavior change, and business value.
