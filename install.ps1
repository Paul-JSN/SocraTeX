$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$Source = Join-Path $ScriptDir ".claude\skills"
$Target = Join-Path $env:USERPROFILE ".claude\skills"

if (-not (Test-Path $Source)) {
    Write-Error "Skills directory not found at $Source"
    exit 1
}

Get-ChildItem -Path $Source -Directory | ForEach-Object {
    $name = $_.Name
    $dest = Join-Path $Target "socratex-$name"
    New-Item -ItemType Directory -Path $dest -Force | Out-Null
    Copy-Item (Join-Path $_.FullName "SKILL.md") -Destination $dest -Force
}

Write-Host "SocraTeX skills installed to $Target" -ForegroundColor Green
Write-Host ""
Write-Host "Available skills:"
Get-ChildItem -Path $Target -Directory -Filter "socratex-*" | ForEach-Object {
    $name = $_.Name
    Write-Host "  /$name"
}
Write-Host ""
Write-Host "Or use them without prefix when inside the SocraTeX project directory."
