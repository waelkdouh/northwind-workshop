# Read-only cross-document probe for docs/product (writes nothing outside this probe directory).
$ErrorActionPreference = 'Stop'
$root = 'C:\demos\northwind-workshop\docs\product'
$reg = Import-Csv 'C:\demos\northwind-workshop\.copilot-tracking\reviews\probe-nw-product-docs\backlog-register.csv'
$regById = @{}; foreach ($r in $reg) { $regById[$r.ID] = $r }

# 1. Appendix A of traceability vs register
$tr = Get-Content -LiteralPath "$root\traceability.md" -Encoding UTF8
$inApp = $false; $appRows = 0; $appProblems = 0
$seen = @{}
foreach ($l in $tr) {
  if ($l -like '## Appendix A*') { $inApp = $true; continue }
  if ($inApp -and $l -match '^\| `([A-Z]{2}-[A-Z]{2}-\d{2,3})` \|') {
    $c = $l.Trim().Trim('|').Split('|') | ForEach-Object { $_.Trim() }
    $id = $c[0].Trim('`'); $appRows++; $seen[$id] = 1
    if (-not $regById.ContainsKey($id)) { Write-Output "APPX-UNKNOWN $id"; $appProblems++; continue }
    $r = $regById[$id]
    $relTxt = $c[5].Trim('`'); $relReg = $r.Release
    if ($relTxt -eq '-' -or $relTxt -like '-*') { $relTxt = '-' }
    if ($relTxt -ne $relReg) { Write-Output "APPX-REL $id doc=$relTxt reg=$relReg"; $appProblems++ }
    if ($c[4].Trim('`') -ne $r.Track) { Write-Output "APPX-TRACK $id"; $appProblems++ }
    if ($c[6] -notmatch ('^' + $r.Priority)) { Write-Output "APPX-PRIO $id doc=$($c[6]) reg=$($r.Priority)"; $appProblems++ }
    $regSrc = $r.Sources -split ', '
    $regBR = @($regSrc | Where-Object { $_ -match '^(BR|NFR)-' } | Sort-Object)
    $regOther = @($regSrc | Where-Object { $_ -match '^(C|SM|OQ)-' } | Sort-Object)
    $docBR = @(([regex]::Matches($c[7], '(BR|NFR)-\d{2}') | ForEach-Object { $_.Value }) | Sort-Object)
    $docOther = @(([regex]::Matches($c[8], '(C|SM|OQ)-\d{2}') | ForEach-Object { $_.Value }) | Sort-Object)
    if (($regBR -join ',') -ne ($docBR -join ',')) { Write-Output "APPX-COVERS $id doc=[$($docBR -join ',')] reg=[$($regBR -join ',')]"; $appProblems++ }
    if (($regOther -join ',') -ne ($docOther -join ',')) { Write-Output "APPX-OTHER $id doc=[$($docOther -join ',')] reg=[$($regOther -join ',')]"; $appProblems++ }
  }
}
Write-Output "APPENDIX rows=$appRows problems=$appProblems"
$missingApp = @($reg | Where-Object { $_.Type -in @('Story','Enabler') -and -not $seen.ContainsKey($_.ID) } | ForEach-Object { $_.ID })
Write-Output ("Stories/enablers in register missing from Appendix A: " + ($missingApp -join ', '))

# 2. Every ID of backlog-style form referenced in any product doc must exist in the register
$files = Get-ChildItem -Recurse -File $root -Filter *.md
$idRx = '\b(EP-(AZ|DN)-\d{2}|FT-(AZ|DN)-\d{2}|US-(AZ|DN)-\d{3}|EN-(AZ|DN)-\d{2})\b'
foreach ($f in $files) {
  $txt = Get-Content -LiteralPath $f.FullName -Raw -Encoding UTF8
  $ids = [regex]::Matches($txt, $idRx) | ForEach-Object { $_.Value } | Sort-Object -Unique
  $unknown = @($ids | Where-Object { -not $regById.ContainsKey($_) })
  $rel = $f.FullName.Replace($root + '\','')
  Write-Output ("{0,-34} work-item-IDs={1,3} unknown=[{2}]" -f $rel, $ids.Count, ($unknown -join ','))
}

# 3. Assumption and OPEN IDs: defined in README master register, and every file's used IDs exist there
$rd = Get-Content -LiteralPath "$root\README.md" -Encoding UTF8 -Raw
$aDef = @{}; foreach ($m in [regex]::Matches($rd, '(?m)^\| (A-\d{2}) \|')) { $aDef[$m.Groups[1].Value] = 1 }
$oDef = @{}; foreach ($m in [regex]::Matches($rd, '(?m)^\| (OPEN-\d{2}) \|')) { $oDef[$m.Groups[1].Value] = 1 }
Write-Output ("README defines A-: {0} ; OPEN-: {1}" -f $aDef.Count, $oDef.Count)
foreach ($f in $files) {
  $txt = Get-Content -LiteralPath $f.FullName -Raw -Encoding UTF8
  $aIds = [regex]::Matches($txt, '\bA-\d{2}\b') | ForEach-Object { $_.Value } | Sort-Object -Unique
  $oIds = [regex]::Matches($txt, '\bOPEN-\d{2}\b') | ForEach-Object { $_.Value } | Sort-Object -Unique
  $aBad = @($aIds | Where-Object { -not $aDef.ContainsKey($_) })
  $oBad = @($oIds | Where-Object { -not $oDef.ContainsKey($_) })
  $rel = $f.FullName.Replace($root + '\','')
  Write-Output ("{0,-34} A-used={1,2} notInReadme=[{2}]  OPEN-used={3,2} notInReadme=[{4}]" -f $rel, $aIds.Count, ($aBad -join ','), $oIds.Count, ($oBad -join ','))
}
$allA = @{}; $allO = @{}
foreach ($f in $files) { $txt = Get-Content -LiteralPath $f.FullName -Raw -Encoding UTF8; foreach ($m in [regex]::Matches($txt,'\bA-\d{2}\b')) { $allA[$m.Value]=1 }; foreach ($m in [regex]::Matches($txt,'\bOPEN-\d{2}\b')) { $allO[$m.Value]=1 } }
Write-Output ("A- defined but never used anywhere: " + (@($aDef.Keys | Where-Object { -not $allA.ContainsKey($_) } | Sort-Object) -join ','))
Write-Output ("OPEN- defined but never used anywhere: " + (@($oDef.Keys | Where-Object { -not $allO.ContainsKey($_) } | Sort-Object) -join ','))
