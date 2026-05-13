# GitHub Role-Based Academy

Purpose
This repository is a role-based academy for GitHub Enterprise Cloud migration, implementation, security enablement, Copilot adoption, and AI-assisted SDLC. It is designed to take a learner from beginner to field-ready specialist through structured modules, labs, and a capstone.

Who should use this
- Application developers, infrastructure engineers, DevOps/platform engineers
- Security engineers, QA engineers, BAs/product owners
- Architects, engineering managers, and delivery leaders
- Migration factory teams and enablement coaches

How to clone and start
1. Install Git, GitHub CLI, and VS Code.
2. Sign in with `gh auth login`.
3. Clone the repo:

```bash
git clone https://github.com/TODO_ORG/gh-role-based-academy.git
cd gh-role-based-academy
```

4. Read [docs/00-orientation/01-how-to-use-this-repo.md](docs/00-orientation/01-how-to-use-this-repo.md).
5. Pick your role in [ROLE-MATRIX.md](ROLE-MATRIX.md).
6. Start the M00 Orientation issues.

Learning path
1. Orientation and Foundations
2. Administration and Governance
3. Actions and CI/CD
4. Migration Specialist
5. GHAS Specialist
6. Copilot Adoption
7. AI-SDLC
8. Capstone
9. AI Coach Enablement (for embedded enablement roles)

12-week training plan (example)
| Week | Focus | Deliverables |
|---|---|---|
| 1 | Orientation + Foundations | Labs 00-01, baseline assessment |
| 2 | Foundations | PRs, Projects, repo protections |
| 3 | Administration | Org model, teams, rulesets |
| 4 | Actions | Basic CI, reusable workflows |
| 5 | Actions | Environments, approvals, OIDC |
| 6 | Migration Specialist | Discovery, inventory, waves |
| 7 | Migration Specialist | Importers, cutover, hypercare |
| 8 | GHAS | CodeQL, secret scanning, Dependabot |
| 9 | Copilot Adoption | Enablement plan, metrics |
| 10 | AI-SDLC | Requirements, architecture, tests |
| 11 | Capstone | Draft deliverables |
| 12 | Capstone + Field readiness | Final readout and checklist |

30/60/90-day enterprise rollout plan
| Timeline | Focus | Outcomes |
|---|---|---|
| 0-30 days | Pilot and readiness | Org model, identity plan, initial repos, baseline metrics |
| 31-60 days | Scale enablement | Actions templates, GHAS rollout plan, Copilot pilot |
| 61-90 days | Migration factory | Waves in motion, training cohorts, governance in place |

Capstone expectations
Learners must deliver discovery, migration wave plan, governance model, GHAS plan, Copilot adoption plan, AI-SDLC model, pilot implementation artifacts, and an executive readout with a go/no-go recommendation.

Certification alignment
This academy maps to GitHub Foundations, Actions, Administration, Advanced Security, and Copilot certifications. See [CERTIFICATION-PATH.md](CERTIFICATION-PATH.md).

## AI Coach Enablement Track

This academy includes an AI Coach track for consultants who will work directly with client delivery teams to accelerate practical AI adoption.

The AI Coach is an embedded enablement resource who helps client teams:

- Use GitHub Copilot effectively in VS Code and GitHub.com.
- Apply prompt patterns to real development work.
- Improve user stories, acceptance criteria, tests, refactoring, documentation, and release notes.
- Use Copilot safely with human review, source control, pull requests, tests, and security scans.
- Connect AI-assisted work to the client’s actual SDLC.
- Build internal champions so adoption continues after the coach leaves.

The AI Coach is not just a trainer. The coach works inside the client’s flow of work, observes friction, helps improve practices, and produces measurable enablement outcomes.
