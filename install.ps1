$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$Source = Join-Path $ScriptDir "skills"
$Target = Join-Path $env:USERPROFILE ".claude\skills"

if (-not (Test-Path $Source)) {
    Write-Error "Skills directory not found at $Source"
    exit 1
}

# Copy each skill directory (SKILL.md + supporting files)
Get-ChildItem -Path $Source -Directory | ForEach-Object {
    $name = $_.Name
    # Skip _shared directory — handled separately
    if ($name -eq "_shared") { return }
    $dest = Join-Path $Target "socratex-$name"
    New-Item -ItemType Directory -Path $dest -Force | Out-Null
    Copy-Item (Join-Path $_.FullName "*") -Destination $dest -Recurse -Force
}

# Copy _shared resources
$SharedSource = Join-Path $Source "_shared"
if (Test-Path $SharedSource) {
    $SharedDest = Join-Path $Target "socratex-_shared"
    New-Item -ItemType Directory -Path $SharedDest -Force | Out-Null
    Copy-Item (Join-Path $SharedSource "*") -Destination $SharedDest -Recurse -Force
}

Write-Host "SocraTeX skills installed to $Target" -ForegroundColor Green
Write-Host ""
Write-Host "Available skills:"
Get-ChildItem -Path $Target -Directory -Filter "socratex-*" | ForEach-Object {
    $name = $_.Name -replace "^socratex-", ""
    if ($name -ne "_shared") {
        Write-Host "  /socratex-$name"
    }
}
Write-Host ""
Write-Host "Or use them without prefix when inside the SocraTeX project directory."
