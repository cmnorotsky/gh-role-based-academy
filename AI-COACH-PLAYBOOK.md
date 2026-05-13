# AI Coach Playbook

## Purpose

The AI Coach helps client teams adopt GitHub Copilot and AI-assisted SDLC practices in real delivery work. The coach’s job is to move teams from casual experimentation to repeatable, governed, measurable AI-enabled engineering behavior.

## AI Coach outcomes

An AI Coach should help a client team achieve:

1. Developers can use Copilot Chat, inline suggestions, and prompt files effectively.
2. BAs and product owners can improve stories, acceptance criteria, and backlog refinement.
3. QA engineers can generate test cases, test data ideas, and automation starting points.
4. DevOps engineers can use AI to improve workflows, scripts, IaC, and release notes.
5. Security practices remain intact through PR review, GHAS, CodeQL, dependency review, and secret scanning.
6. Managers can measure adoption, engagement, and delivery impact.
7. Client champions can continue enablement after the coach exits.

## AI Coach responsibilities

The AI Coach should:

- Assess team readiness.
- Identify role-specific use cases.
- Run hands-on workshops.
- Pair with developers during real work.
- Host office hours.
- Build reusable prompt libraries.
- Create team-specific examples.
- Help teams avoid unsafe AI usage.
- Measure adoption and value.
- Prepare client champions for long-term ownership.

## AI Coach is not responsible for

The AI Coach should not:

- Replace engineering judgment.
- Approve production code alone.
- Bypass security review.
- Create unreviewed production changes.
- Claim ROI without supporting evidence.
- Encourage pasting secrets, credentials, private customer data, or restricted code into unauthorized tools.
- Present Copilot as a replacement for disciplined SDLC practices.

## Engagement model

### Phase 1: Discovery

Duration: 1-2 weeks

Activities:

- Interview engineering managers.
- Review current SDLC.
- Review GitHub, Azure DevOps, Jira, or other delivery tooling.
- Identify pilot teams.
- Identify current AI usage.
- Identify security and compliance concerns.
- Identify blockers such as IDE access, license assignment, network restrictions, or policy gaps.

Deliverables:

- AI readiness assessment
- Role/persona map
- Adoption risks
- Initial coaching backlog

### Phase 2: Pilot enablement

Duration: 2-4 weeks

Activities:

- Run role-based workshops.
- Set up Copilot in IDEs.
- Teach prompt patterns.
- Pair with developers on real issues.
- Use AI in PR review, tests, documentation, and refactoring.
- Establish human review and security gates.

Deliverables:

- Prompt library
- Team workflow examples
- Office hours notes
- Adoption metrics baseline

### Phase 3: Embedded coaching

Duration: 4-8 weeks

Activities:

- Join sprint ceremonies where appropriate.
- Support backlog refinement.
- Support issue creation.
- Support test planning.
- Support PR review improvements.
- Support GitHub Actions and GHAS usage.
- Coach team champions.

Deliverables:

- Team-specific enablement plan
- AI-SDLC workflow
- Value report
- Champion readiness checklist

### Phase 4: Handoff

Duration: 1-2 weeks

Activities:

- Train client champions.
- Document repeatable patterns.
- Create office-hours runbook.
- Finalize value report.
- Identify next wave teams.

Deliverables:

- Handoff plan
- Champion guide
- Executive readout
- Recommended next steps

## Role-specific coaching examples

| Role | Coaching focus |
|---|---|
| Developer | Prompting, code explanation, refactoring, tests, PR descriptions, secure coding |
| QA engineer | Test cases, edge cases, automation scaffolding, traceability |
| BA/Product Owner | User stories, acceptance criteria, requirements-as-code, backlog refinement |
| Architect | Architecture decision records, threat modeling prompts, design review |
| DevOps engineer | GitHub Actions, reusable workflows, scripts, IaC, release notes |
| Security engineer | GHAS triage, secure prompt patterns, AI-assisted remediation review |
| Manager | Adoption metrics, value model, team enablement, risk management |

## AI Coach success metrics

Measure both usage and behavior change.

### Adoption metrics

- Assigned Copilot licenses
- Active users
- Engaged users
- Chat usage
- IDE usage
- Pull request usage
- Training attendance
- Office hours attendance

### Engineering flow metrics

- PR cycle time
- Review turnaround time
- Build success rate
- Deployment frequency
- Lead time for changes
- Defect escape rate
- Rework rate

### Quality and security metrics

- Code scanning alerts opened/closed
- Secret scanning incidents
- Dependency review findings
- Test coverage trend
- Security remediation time

### Human feedback

- Developer confidence
- Perceived usefulness
- Friction points
- Skills gaps
- Manager observations

## AI Coach field readiness checklist

An AI Coach is field-ready when they can:

- Explain GitHub Copilot licensing, usage, and governance.
- Configure Copilot in VS Code.
- Teach prompt patterns to multiple roles.
- Coach developers through real coding tasks.
- Coach BAs through story and acceptance criteria improvement.
- Coach QA through test generation and validation.
- Explain secure AI usage.
- Explain why human review is still required.
- Connect Copilot usage to GitHub Issues, PRs, Actions, GHAS, and Projects.
- Produce an adoption/value report.
- Prepare client champions to continue enablement.
