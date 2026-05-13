# Value Measurement

Use these metrics to measure adoption, delivery flow, quality, and security outcomes. Avoid claiming ROI without financial data.

## Migration readiness
- Readiness score: $ready\% = (ready\ repos / total\ repos) * 100$
- Blocker count by wave

## Migration throughput
- Repos migrated per week
- Pipeline conversions per week

## Pipeline conversion success
- Success rate: $pipeline\ success\% = (successful\ runs / total\ runs) * 100$

## Build and deploy success
- Build success rate
- Deployment success rate

## GHAS alert reduction
- Reduction: $alert\ reduction\% = ((baseline - current) / baseline) * 100$

## Secret leak prevention
- Push protection blocks per week
- Secrets remediated within SLA

## Copilot adoption
- Adoption rate: $adoption\% = (active\ users / assigned\ licenses) * 100$

## Copilot engagement
- Engagement rate: $engaged\% = (engaged\ users / active\ users) * 100$

## Copilot suggestion acceptance
- Acceptance rate: $acceptance\% = (accepted\ lines / suggested\ lines) * 100$

## Pull request lifecycle changes
- PR cycle time
- Review turnaround time

## Developer satisfaction
- Survey score trend and qualitative feedback

## Lead time for changes
- $lead\ time = deployment\ time - commit\ time$

## Deployment frequency
- Deploys per week per service

## Change failure rate
- Failed deployments / total deployments

## MTTR
- $MTTR = sum(recovery\ time) / number\ of\ incidents$

## Example metrics table
| Metric | Definition | Data source | Review cadence |
|---|---|---|---|
| Adoption rate | Active users / assigned licenses | Copilot usage export | Monthly |
| PR cycle time | PR open to merge time | GitHub Insights | Weekly |
| CodeQL alerts closed | Alerts closed / total | Security Overview | Monthly |
| Pipeline success | Successful runs / total runs | Actions runs | Weekly |
