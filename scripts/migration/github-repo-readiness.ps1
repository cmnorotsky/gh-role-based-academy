<#
GitHub repo readiness scoring (dry-run by default).
Usage: ./github-repo-readiness.ps1 -InputCsv samples/migration-data/sample-repo-inventory.csv -DryRun
#>
param(
  [string]$InputCsv,
  [switch]$DryRun
)

if (-not $InputCsv) { Write-Error "InputCsv is required"; exit 1 }

$repos = Import-Csv $InputCsv
if ($DryRun) {
  Write-Host "Dry run: loaded $($repos.Count) rows"
  exit 0
}

# TODO: Compute readiness score based on repo size, branches, and pipelines.
$repos | Export-Csv -NoTypeInformation -Path "repo-readiness-output.csv"
