$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$Source = Join-Path $ScriptDir ".claude\commands"
$Target = Join-Path $env:USERPROFILE ".claude\commands\socratex"

if (-not (Test-Path $Source)) {
    Write-Error "Commands directory not found at $Source"
    exit 1
}

New-Item -ItemType Directory -Path $Target -Force | Out-Null
Copy-Item "$Source\*.md" -Destination $Target -Force

Write-Host "Socratex commands installed to $Target" -ForegroundColor Green
Write-Host ""
Write-Host "Available commands:"
Get-ChildItem "$Target\*.md" | ForEach-Object {
    $name = $_.BaseName
    Write-Host "  /socratex:$name"
}
Write-Host ""
Write-Host "Or use them without prefix when inside the socratex project directory."
