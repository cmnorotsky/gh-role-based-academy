<#
ADO pipeline inventory script (dry-run by default).
Usage: ./ado-pipeline-inventory.ps1 -InputCsv samples/migration-data/sample-pipeline-inventory.csv -DryRun
#>
param(
  [string]$InputCsv,
  [switch]$DryRun
)

if (-not $InputCsv) { Write-Error "InputCsv is required"; exit 1 }

$pipelines = Import-Csv $InputCsv
if ($DryRun) {
  Write-Host "Dry run: loaded $($pipelines.Count) rows"
  exit 0
}

# TODO: Enrich pipeline data from ADO API.
$pipelines | Export-Csv -NoTypeInformation -Path "pipeline-inventory-output.csv"
