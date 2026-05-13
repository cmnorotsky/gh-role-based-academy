<#
Repository inventory script (dry-run by default).
Usage: ./repo-inventory.ps1 -InputCsv samples/migration-data/sample-repo-inventory.csv -DryRun
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

# TODO: Connect to ADO or GitHub to enrich inventory.
$repos | Export-Csv -NoTypeInformation -Path "repo-inventory-output.csv"
