# Issue Backlog

This backlog contains detailed issues for the academy. Each issue includes steps, evidence, definition of done, and reviewer criteria.

## M00 Orientation

### 001 - Set up GitHub account access
Track: foundations
Role: app-dev, infra, devops
Certification: foundations
Prerequisites: None
Steps:
1. Confirm whether EMU is required.
2. Sign in to GitHub.
3. Verify training org access.
4. Enable MFA if required.
Evidence: Screenshot or note confirming org access
Definition of done: Access confirmed
Reviewer criteria: Access verified and documented

### 002 - Install VS Code, Git, and GitHub CLI
Track: foundations
Role: app-dev, infra, devops
Certification: foundations
Prerequisites: 001
Steps:
1. Install Git.
2. Install VS Code.
3. Install GitHub CLI.
4. Run `gh auth login`.
Evidence: `gh auth status` output note
Definition of done: Tools installed and CLI authenticated
Reviewer criteria: Authenticated and working

### 003 - Install Copilot and PR extensions
Track: foundations
Role: app-dev, infra, devops
Certification: foundations
Prerequisites: 002
Steps:
1. Install Copilot extension.
2. Install GitHub PR extension.
3. Sign in to GitHub in VS Code.
4. Verify Copilot Chat.
Evidence: Screenshot or note of Copilot Chat
Definition of done: Copilot works in VS Code
Reviewer criteria: Copilot verified

### 004 - Clone repo and open first PR
Track: foundations
Role: app-dev, infra, devops
Certification: foundations
Prerequisites: 002
Steps:
1. Clone the repo.
2. Create a branch `learner/<name>/orientation`.
3. Add evidence file.
4. Open a PR.
Evidence: PR link
Definition of done: PR approved
Reviewer criteria: Branch and evidence file correct

### 005 - Read academy overview and choose role path
Track: foundations
Role: all
Certification: foundations
Prerequisites: 004
Steps:
1. Read README and ROLE-MATRIX.
2. Document your required modules.
3. Add a short learning goal to evidence file.
Evidence: Evidence update
Definition of done: Mentor confirms path
Reviewer criteria: Role path is accurate

## M01 Foundations

### 006 - Git basics lab
Track: foundations
Role: all
Certification: foundations
Prerequisites: 004
Steps:
1. Create a branch for git-basics.
2. Add evidence file.
3. Commit and push changes.
4. Open PR.
Evidence: PR link
Definition of done: PR approved
Reviewer criteria: Git flow correct

### 007 - Branching and PR workflow
Track: foundations
Role: all
Certification: foundations
Prerequisites: 006
Steps:
1. Create a feature branch.
2. Make a small change.
3. Open PR with clear description.
4. Address review comments.
Evidence: PR link and review notes
Definition of done: PR merged
Reviewer criteria: Review process followed

### 008 - Issues and milestones basics
Track: foundations
Role: all
Certification: foundations
Prerequisites: 006
Steps:
1. Create a learning story issue.
2. Add milestone and labels.
3. Add to project board.
Evidence: Issue link
Definition of done: Issue tracked in project
Reviewer criteria: Labels and milestone correct

### 009 - GitHub Projects basics
Track: foundations
Role: all
Certification: foundations
Prerequisites: 008
Steps:
1. Open the project board.
2. Create a custom view by track.
3. Move your issue across status.
Evidence: Screenshot or note
Definition of done: View created
Reviewer criteria: View exists and issue updated

### 010 - Repo settings overview
Track: foundations
Role: all
Certification: foundations
Prerequisites: 006
Steps:
1. Review repository settings.
2. Identify default branch.
3. Note existing protections.
Evidence: Short summary note
Definition of done: Summary approved
Reviewer criteria: Summary accurate

### 011 - Create a CODEOWNERS proposal
Track: foundations
Role: app-dev, devops
Certification: foundations
Prerequisites: 010
Steps:
1. Draft a CODEOWNERS file in a branch.
2. Use team placeholders.
3. Open PR.
Evidence: PR link
Definition of done: PR reviewed
Reviewer criteria: CODEOWNERS matches governance model

### 012 - Create a PR template proposal
Track: foundations
Role: app-dev, devops
Certification: foundations
Prerequisites: 010
Steps:
1. Draft a PR template in a branch.
2. Include checklist and security notes.
3. Open PR.
Evidence: PR link
Definition of done: PR reviewed
Reviewer criteria: Template is usable

### 013 - Evidence workflow
Track: foundations
Role: all
Certification: foundations
Prerequisites: 006
Steps:
1. Create evidence folder.
2. Add a lab summary.
3. Link your evidence in PR.
Evidence: Evidence file
Definition of done: Evidence structure created
Reviewer criteria: Evidence is clear and organized

### 014 - GitHub CLI basics
Track: foundations
Role: all
Certification: foundations
Prerequisites: 002
Steps:
1. Run `gh repo view`.
2. Run `gh issue list`.
3. Document commands used.
Evidence: Command notes
Definition of done: Notes reviewed
Reviewer criteria: Commands executed correctly

### 015 - Foundations checkpoint
Track: foundations
Role: all
Certification: foundations
Prerequisites: 006-014
Steps:
1. Review completed labs.
2. Summarize strengths and gaps.
3. Create a checkpoint issue comment.
Evidence: Summary comment
Definition of done: Mentor confirms readiness
Reviewer criteria: Gaps identified

## M02 Administration

### 016 - Define enterprise org model
Track: admin
Role: devops, architect
Certification: admin
Prerequisites: Foundations
Steps:
1. Draft org structure.
2. Define shared services org.
3. Define ownership.
Evidence: Org model doc
Definition of done: Reviewed by mentor
Reviewer criteria: Ownership clear

### 017 - Team and permission matrix
Track: admin
Role: devops, security
Certification: admin
Prerequisites: 016
Steps:
1. Map roles to permissions.
2. Use teams not individuals.
3. Document EMU impacts.
Evidence: Permission matrix
Definition of done: Matrix approved
Reviewer criteria: Least privilege applied

### 018 - SSO/SAML/SCIM planning
Track: admin
Role: devops, security
Certification: admin
Prerequisites: 017
Steps:
1. Identify identity provider.
2. Document SSO and SCIM requirements.
3. Identify EMU needs.
Evidence: Identity plan
Definition of done: Plan approved
Reviewer criteria: Identity path is clear

### 019 - Rulesets and branch protections
Track: admin
Role: devops, security
Certification: admin
Prerequisites: 016
Steps:
1. Draft required rulesets.
2. Map to branch protections.
3. Define exceptions and escalation.
Evidence: Ruleset plan
Definition of done: Plan reviewed
Reviewer criteria: Security and delivery balanced

### 020 - Audit log review process
Track: admin
Role: security
Certification: admin
Prerequisites: 016
Steps:
1. Identify required audit events.
2. Define review cadence.
3. Define escalation path.
Evidence: Audit plan
Definition of done: Approved by governance
Reviewer criteria: Owners assigned

### 021 - Repo lifecycle policy
Track: admin
Role: devops
Certification: admin
Prerequisites: 016
Steps:
1. Define repo creation standards.
2. Define archival and deletion policy.
3. Document ownership requirements.
Evidence: Lifecycle policy
Definition of done: Policy approved
Reviewer criteria: Policy aligns with governance

### 022 - Organization policy checklist
Track: admin
Role: devops, security
Certification: admin
Prerequisites: 016
Steps:
1. List required org policies.
2. Map policies to compliance needs.
3. Identify enforcement tooling.
Evidence: Policy checklist
Definition of done: Checklist approved
Reviewer criteria: Policies complete

### 023 - Admin checkpoint
Track: admin
Role: devops, security
Certification: admin
Prerequisites: 016-022
Steps:
1. Summarize admin work completed.
2. Identify remaining gaps.
3. Add summary to evidence.
Evidence: Summary note
Definition of done: Mentor confirms readiness
Reviewer criteria: Gaps identified

## M03 Actions

### 024 - Basic CI workflow
Track: actions
Role: app-dev, devops
Certification: actions
Prerequisites: Foundations
Steps:
1. Add basic CI workflow.
2. Run on PR.
3. Capture run output.
Evidence: PR link and run log
Definition of done: CI passes
Reviewer criteria: Workflow runs successfully

### 025 - Reusable workflow
Track: actions
Role: devops
Certification: actions
Prerequisites: 024
Steps:
1. Create reusable workflow.
2. Call from another workflow.
3. Pass inputs.
Evidence: PR link and run log
Definition of done: Reusable workflow executed
Reviewer criteria: Inputs documented

### 026 - Environment approvals
Track: actions
Role: devops
Certification: actions
Prerequisites: 024
Steps:
1. Create environment with approval.
2. Update workflow to use environment.
3. Trigger and approve run.
Evidence: Approval screenshot
Definition of done: Approval gate enforced
Reviewer criteria: Approval required

### 027 - OIDC to Azure
Track: actions
Role: devops, infra
Certification: actions
Prerequisites: 024
Steps:
1. Create OIDC app registration.
2. Configure federated credentials.
3. Update workflow to use OIDC.
Evidence: Workflow snippet and permissions list
Definition of done: OIDC auth works
Reviewer criteria: Least privilege documented

### 028 - Self-hosted runner strategy
Track: actions
Role: infra, devops
Certification: actions
Prerequisites: 024
Steps:
1. Identify workloads needing self-hosted runners.
2. Define runner labels and groups.
3. Document security controls.
Evidence: Runner strategy doc
Definition of done: Strategy reviewed
Reviewer criteria: Isolation and security addressed

### 029 - ADO pipeline conversion analysis
Track: actions
Role: devops
Certification: actions
Prerequisites: 024
Steps:
1. Inventory a sample ADO pipeline.
2. Map tasks to Actions.
3. Identify manual gaps.
Evidence: Conversion map
Definition of done: Plan reviewed
Reviewer criteria: Gaps documented

### 030 - Actions secrets and variables
Track: actions
Role: devops
Certification: actions
Prerequisites: 024
Steps:
1. Identify secrets used by a pipeline.
2. Map to Actions secrets.
3. Document variable usage and scope.
Evidence: Mapping table
Definition of done: Mapping approved
Reviewer criteria: No secrets in code

### 031 - Deployment workflow with environment
Track: actions
Role: devops
Certification: actions
Prerequisites: 026
Steps:
1. Create deployment workflow.
2. Use environment approvals.
3. Add rollback note.
Evidence: Workflow file and run log
Definition of done: Workflow approved
Reviewer criteria: Approval required

### 032 - Actions security checklist
Track: actions
Role: devops, security
Certification: actions
Prerequisites: 024
Steps:
1. Create Actions security checklist.
2. Include permissions and OIDC guidance.
3. Add to evidence.
Evidence: Checklist
Definition of done: Checklist reviewed
Reviewer criteria: Security risks addressed

### 033 - Actions checkpoint
Track: actions
Role: devops
Certification: actions
Prerequisites: 024-032
Steps:
1. Summarize workflow work.
2. Identify remaining gaps.
Evidence: Summary note
Definition of done: Mentor confirms readiness
Reviewer criteria: Gaps documented

## M04 Migration Specialist

### 034 - Migration discovery report
Track: migration
Role: devops, architect
Certification: admin
Prerequisites: Actions basics
Steps:
1. Use discovery template.
2. Capture ADO orgs and projects.
3. Identify critical apps.
Evidence: Discovery report
Definition of done: Report reviewed
Reviewer criteria: Critical apps identified

### 035 - Repo inventory build
Track: migration
Role: devops, architect
Certification: admin
Prerequisites: 034
Steps:
1. Populate repo inventory template.
2. Add size and branch counts.
3. Flag high-risk repos.
Evidence: Inventory file
Definition of done: Inventory reviewed
Reviewer criteria: Complete and accurate

### 036 - Git sizer assessment
Track: migration
Role: devops
Certification: admin
Prerequisites: 035
Steps:
1. Run git-sizer wrapper.
2. Record output.
3. Flag history cleanup needs.
Evidence: Results table
Definition of done: Risks documented
Reviewer criteria: Mitigations noted

### 037 - GEI migration plan
Track: migration
Role: devops
Certification: admin
Prerequisites: 034
Steps:
1. Identify repos for GEI.
2. Document migration steps.
3. Note limitations.
Evidence: GEI plan
Definition of done: Plan reviewed
Reviewer criteria: Manual steps documented

### 038 - Actions Importer analysis
Track: migration
Role: devops
Certification: actions
Prerequisites: 034
Steps:
1. Run or simulate Actions Importer analysis.
2. Document conversion coverage.
3. Identify manual tasks.
Evidence: Analysis report
Definition of done: Report reviewed
Reviewer criteria: Gaps documented

### 039 - Pipeline dry-run plan
Track: migration
Role: devops
Certification: actions
Prerequisites: 038
Steps:
1. Choose pilot pipelines.
2. Define dry-run success criteria.
3. Document rollback approach.
Evidence: Dry-run plan
Definition of done: Plan approved
Reviewer criteria: Criteria are measurable

### 040 - Boards transition strategy
Track: migration
Role: ba-product, devops
Certification: admin
Prerequisites: 034
Steps:
1. Decide dual-tracking vs cutover.
2. Map work item types.
3. Define timeline.
Evidence: Boards plan
Definition of done: Plan reviewed
Reviewer criteria: Stakeholder alignment

### 041 - Work item linking strategy
Track: migration
Role: ba-product, devops
Certification: admin
Prerequisites: 040
Steps:
1. Define issue/PR linking rules.
2. Create example links.
3. Document guidance.
Evidence: Linking guidance
Definition of done: Guidance approved
Reviewer criteria: Traceability clear

### 042 - Repo migration waves
Track: migration
Role: devops, architect
Certification: admin
Prerequisites: 035
Steps:
1. Define wave criteria.
2. Assign repos to waves.
3. Document risks per wave.
Evidence: Wave plan
Definition of done: Plan reviewed
Reviewer criteria: Risk-based ordering

### 043 - Cutover plan
Track: migration
Role: devops
Certification: admin
Prerequisites: 042
Steps:
1. Define cutover windows.
2. Define freeze and validation.
3. Define rollback triggers.
Evidence: Cutover plan
Definition of done: Plan approved
Reviewer criteria: Rollback included

### 044 - Hypercare plan
Track: migration
Role: devops
Certification: admin
Prerequisites: 043
Steps:
1. Define support window.
2. Define issue routing.
3. Define escalation.
Evidence: Hypercare plan
Definition of done: Plan approved
Reviewer criteria: Owners and SLAs defined

### 045 - Migration executive readout
Track: migration
Role: architect, manager
Certification: admin
Prerequisites: 034-044
Steps:
1. Create a summary deck or doc.
2. Include risks, waves, and timeline.
3. Include go/no-go criteria.
Evidence: Executive summary
Definition of done: Reviewed by sponsor
Reviewer criteria: Decision-ready

## M05 GHAS Specialist

### 046 - Enable GHAS features
Track: ghas
Role: security, app-dev
Certification: ghas
Prerequisites: Foundations
Steps:
1. Enable code scanning, secret scanning, dependency review.
2. Document licensing constraints.
Evidence: Feature enablement note
Definition of done: Enabled or gaps documented
Reviewer criteria: Licensing notes included

### 047 - CodeQL workflow
Track: ghas
Role: security, app-dev
Certification: ghas
Prerequisites: 046
Steps:
1. Add CodeQL workflow.
2. Run on PR.
3. Review alerts.
Evidence: PR link and alert summary
Definition of done: Workflow runs
Reviewer criteria: Alerts triaged

### 048 - Secret scanning workflow
Track: ghas
Role: security
Certification: ghas
Prerequisites: 046
Steps:
1. Enable secret scanning and push protection.
2. Document incident workflow.
Evidence: Workflow note
Definition of done: Process documented
Reviewer criteria: Push protection covered

### 049 - Dependency review in PRs
Track: ghas
Role: security, app-dev
Certification: ghas
Prerequisites: 046
Steps:
1. Add dependency review workflow.
2. Run with a dependency change.
3. Triage findings.
Evidence: PR link and notes
Definition of done: Workflow runs
Reviewer criteria: Findings triaged

### 050 - Dependabot configuration
Track: ghas
Role: security, app-dev
Certification: ghas
Prerequisites: 046
Steps:
1. Add Dependabot config.
2. Define update schedule.
Evidence: Config file
Definition of done: Dependabot enabled
Reviewer criteria: Schedule reasonable

### 051 - Security campaign plan
Track: ghas
Role: security
Certification: ghas
Prerequisites: 047
Steps:
1. Select target alerts.
2. Define owners and timeline.
3. Define tracking.
Evidence: Campaign plan
Definition of done: Plan approved
Reviewer criteria: Owners assigned

### 052 - Alert triage workflow
Track: ghas
Role: security
Certification: ghas
Prerequisites: 046
Steps:
1. Define SLA by severity.
2. Define escalation path.
3. Document tooling.
Evidence: Triage workflow
Definition of done: Workflow reviewed
Reviewer criteria: SLAs defined

### 053 - GHAS metrics report
Track: ghas
Role: security, manager
Certification: ghas
Prerequisites: 046
Steps:
1. Define metrics list.
2. Create monthly report format.
3. Add baseline data.
Evidence: Metrics report
Definition of done: Report approved
Reviewer criteria: Metrics include trends

### 054 - GHAS checkpoint
Track: ghas
Role: security
Certification: ghas
Prerequisites: 046-053
Steps:
1. Summarize findings and gaps.
2. Add to evidence file.
Evidence: Summary note
Definition of done: Mentor confirms readiness
Reviewer criteria: Gaps documented

## M06 Copilot Adoption

### 055 - Copilot setup verification
Track: copilot
Role: all
Certification: copilot
Prerequisites: Foundations
Steps:
1. Verify license assignment.
2. Sign in to Copilot in IDE.
3. Confirm Chat works.
Evidence: Screenshot or note
Definition of done: Copilot works in IDE
Reviewer criteria: Verified

### 056 - Prompt library creation
Track: copilot
Role: all
Certification: copilot
Prerequisites: 055
Steps:
1. Create prompts for code, tests, docs.
2. Store in evidence file.
3. Add safe usage notes.
Evidence: Prompt library
Definition of done: Library reviewed
Reviewer criteria: Safe and specific

### 057 - Copilot for tests
Track: copilot
Role: qa, app-dev
Certification: copilot
Prerequisites: 055
Steps:
1. Generate tests with Copilot.
2. Run tests.
3. Document adjustments.
Evidence: Test file and run logs
Definition of done: Tests verified
Reviewer criteria: Tests executed

### 058 - Copilot for PR review
Track: copilot
Role: app-dev
Certification: copilot
Prerequisites: 055
Steps:
1. Use Copilot to summarize PR.
2. Verify accuracy.
3. Draft review notes.
Evidence: PR notes
Definition of done: Notes verified
Reviewer criteria: Human verification included

### 059 - Copilot adoption plan
Track: copilot
Role: manager
Certification: copilot
Prerequisites: 055
Steps:
1. Define pilot teams.
2. Define enablement activities.
3. Define success metrics.
Evidence: Adoption plan
Definition of done: Plan approved
Reviewer criteria: Metrics and risks included

### 060 - Copilot usage metrics model
Track: copilot
Role: manager
Certification: copilot
Prerequisites: 059
Steps:
1. Define adoption and engagement metrics.
2. Use sample data.
3. Create sample report.
Evidence: Report
Definition of done: Report reviewed
Reviewer criteria: Avoids ROI overclaims

### 061 - Copilot checkpoint
Track: copilot
Role: manager
Certification: copilot
Prerequisites: 055-060
Steps:
1. Summarize Copilot work.
2. List gaps and next actions.
Evidence: Summary note
Definition of done: Mentor confirms readiness
Reviewer criteria: Gaps documented

## M07 AI-SDLC

### 062 - Requirements as code
Track: aidlc
Role: ba-product, architect
Certification: copilot
Prerequisites: Foundations
Steps:
1. Create epic and stories.
2. Add acceptance criteria.
3. Add requirements markdown.
Evidence: Issues and PR link
Definition of done: Requirements reviewed
Reviewer criteria: Testable criteria

### 063 - Architecture as code
Track: aidlc
Role: architect
Certification: admin
Prerequisites: 062
Steps:
1. Create ADR.
2. Add alternatives.
3. Open PR.
Evidence: ADR PR link
Definition of done: ADR approved
Reviewer criteria: Alternatives documented

### 064 - Tests as code
Track: aidlc
Role: qa, app-dev
Certification: copilot
Prerequisites: 062
Steps:
1. Create tests for a story.
2. Run tests in CI.
3. Document coverage.
Evidence: Test PR and run log
Definition of done: Tests approved
Reviewer criteria: Tests executed

### 065 - AI-assisted story refinement
Track: aidlc
Role: ba-product
Certification: copilot
Prerequisites: 062
Steps:
1. Use Copilot to refine story.
2. Add negative scenarios.
3. Validate with team.
Evidence: Updated story
Definition of done: Story reviewed
Reviewer criteria: Human validation included

### 066 - AI-assisted QA plan
Track: aidlc
Role: qa
Certification: copilot
Prerequisites: 064
Steps:
1. Generate test cases for a story.
2. Validate and adjust.
3. Add to test plan.
Evidence: Test plan
Definition of done: Plan reviewed
Reviewer criteria: Edge cases included

### 067 - AI-assisted release notes
Track: aidlc
Role: release-manager
Certification: copilot
Prerequisites: 062
Steps:
1. Generate draft release notes.
2. Verify against PRs.
3. Publish in draft.
Evidence: Draft release notes
Definition of done: Notes approved
Reviewer criteria: Accuracy verified

### 068 - Agentic workflow guardrails
Track: aidlc
Role: architect, security
Certification: admin
Prerequisites: 062
Steps:
1. Define allowed agent tasks.
2. Define human approval gates.
3. Document escalation.
Evidence: Guardrails doc
Definition of done: Guardrails approved
Reviewer criteria: Safety enforced

## M08 Capstone

### 069 - Capstone discovery pack
Track: capstone
Role: architect, devops
Certification: admin
Prerequisites: 034-068
Steps:
1. Compile discovery inputs.
2. Summarize risks and dependencies.
Evidence: Discovery pack
Definition of done: Review board approved
Reviewer criteria: Risks documented

### 070 - Capstone migration wave plan
Track: capstone
Role: devops
Certification: admin
Prerequisites: 069
Steps:
1. Build waves.
2. Include pilot criteria.
3. Include rollback.
Evidence: Wave plan
Definition of done: Approved
Reviewer criteria: Risk-based sequencing

### 071 - Capstone governance model
Track: capstone
Role: devops, security
Certification: admin
Prerequisites: 069
Steps:
1. Compile governance policies.
2. Include rulesets and approvals.
Evidence: Governance doc
Definition of done: Approved
Reviewer criteria: Complete policies

### 072 - Capstone executive readout
Track: capstone
Role: manager
Certification: admin
Prerequisites: 069-071
Steps:
1. Create executive readout.
2. Include go/no-go criteria.
Evidence: Readout
Definition of done: Sponsor review
Reviewer criteria: Decision-ready

### 073 - Capstone field readiness checklist
Track: capstone
Role: manager
Certification: admin
Prerequisites: 069-072
Steps:
1. Complete field readiness checklist.
2. Identify remaining gaps.
Evidence: Checklist
Definition of done: Approved
Reviewer criteria: Gaps documented

## M09 AI Coach Enablement

### 074 - AI Coach role summary
Track: ai-coach
Role: ai-coach
Certification: copilot
Prerequisites: Copilot and AI-SDLC
Steps:
1. Summarize AI Coach responsibilities.
2. Document in-scope and out-of-scope.
Evidence: Role summary
Definition of done: Reviewed
Reviewer criteria: Clear boundaries

### 075 - Client readiness assessment
Track: ai-coach
Role: ai-coach
Certification: copilot
Prerequisites: 074
Steps:
1. Complete readiness assessment template.
2. Identify blockers.
3. Recommend next steps.
Evidence: Assessment
Definition of done: Reviewed
Reviewer criteria: Actionable blockers

### 076 - AI coaching workshop plan
Track: ai-coach
Role: ai-coach
Certification: copilot
Prerequisites: 075
Steps:
1. Create developer workshop plan.
2. Include prompts and exercises.
3. Add safety checklist.
Evidence: Workshop plan
Definition of done: Reviewed
Reviewer criteria: Hands-on focus

### 077 - Office hours plan
Track: ai-coach
Role: ai-coach
Certification: copilot
Prerequisites: 075
Steps:
1. Define weekly office hours topics.
2. Define intake and follow-up.
Evidence: Office hours plan
Definition of done: Reviewed
Reviewer criteria: Topics map to needs

### 078 - AI Coach value report
Track: ai-coach
Role: ai-coach
Certification: copilot
Prerequisites: 075
Steps:
1. Collect sample metrics.
2. Capture qualitative feedback.
3. Draft value report.
Evidence: Value report
Definition of done: Reviewed
Reviewer criteria: No ROI overclaims

### 079 - Client champion handoff plan
Track: ai-coach
Role: ai-coach
Certification: copilot
Prerequisites: 078
Steps:
1. Identify champions.
2. Define handoff plan.
3. Define ongoing support.
Evidence: Handoff plan
Definition of done: Reviewed
Reviewer criteria: Ownership defined

### 080 - AI Coach checkpoint
Track: ai-coach
Role: ai-coach
Certification: copilot
Prerequisites: 074-079
Steps:
1. Summarize AI coach work.
2. Identify remaining gaps.
Evidence: Summary note
Definition of done: Mentor confirms readiness
Reviewer criteria: Gaps documented
