# Read-only consistency probe for docs/product/backlog.md (section 11 register vs item blocks).
# Writes nothing outside this probe directory; prints findings to the console.
$ErrorActionPreference = 'Stop'
$blPath = 'C:\demos\northwind-workshop\docs\product\backlog.md'
$lines = Get-Content -LiteralPath $blPath -Encoding UTF8

# ---- 1. Register (section 11) ----
$regIdx = -1
for ($i = 0; $i -lt $lines.Count; $i++) { if ($lines[$i] -like '## 11. Machine-friendly register*') { $regIdx = $i; break } }
if ($regIdx -lt 0) { throw 'register heading not found' }
$reg = @{}
$regOrder = New-Object System.Collections.ArrayList
for ($i = $regIdx; $i -lt $lines.Count; $i++) {
  $l = $lines[$i]
  if ($l -match '^\| `([A-Z]{2}-[A-Z]{2}-\d{2,3})` \|') {
    $cells = $l.Trim().Trim('|').Split('|') | ForEach-Object { $_.Trim() }
    $row = [pscustomobject]@{
      ID = $cells[0].Trim('`'); Type = $cells[1]; Parent = $cells[2].Trim('`'); Title = $cells[3]
      Track = $cells[4].Trim('`'); Release = $cells[5].Trim('`'); Priority = $cells[6]; Sources = $cells[7]
    }
    if ($reg.ContainsKey($row.ID)) { Write-Output "DUP-REG $($row.ID)" }
    $reg[$row.ID] = $row
    [void]$regOrder.Add($row.ID)
  }
}
Write-Output ("REGISTER rows: {0}" -f $regOrder.Count)
$byTrack = $regOrder | ForEach-Object { $reg[$_] } | Group-Object Track | ForEach-Object { "{0}={1}" -f $_.Name, $_.Count }
Write-Output ("By track: " + ($byTrack -join ', '))
$byType = $regOrder | ForEach-Object { $reg[$_] } | Group-Object Type | ForEach-Object { "{0}={1}" -f $_.Name, $_.Count }
Write-Output ("By type: " + ($byType -join ', '))
$byRel = $regOrder | ForEach-Object { $reg[$_] } | Group-Object Track, Release | ForEach-Object { "{0}={1}" -f $_.Name, $_.Count }
Write-Output ("By track+release: " + ($byRel -join '; '))

# ---- 2. Register rule checks ----
foreach ($id in $regOrder) {
  $r = $reg[$id]
  $pfx = $id.Substring(0,2)
  $typeOk = @{ EP='Epic'; FT='Feature'; US='Story'; EN='Enabler' }[$pfx]
  if ($r.Type -ne $typeOk) { Write-Output "TYPE-MISMATCH $id type=$($r.Type)" }
  if ($r.Track -notin @('track-azure','track-dotnet')) { Write-Output "BAD-TRACK $id $($r.Track)" }
  $trackCode = $id.Substring(3,2)
  if ($r.Track -eq 'track-azure' -and $trackCode -ne 'AZ') { Write-Output "TRACK-CODE-MISMATCH $id $($r.Track)" }
  if ($r.Track -eq 'track-dotnet' -and $trackCode -ne 'DN') { Write-Output "TRACK-CODE-MISMATCH $id $($r.Track)" }
  if ($r.Release -ne '-') {
    if ($r.Release -notmatch '^(azure-r[1-3]|dotnet-r[1-4])$') { Write-Output "BAD-RELEASE $id $($r.Release)" }
    elseif (-not $r.Release.StartsWith($(if($r.Track -eq 'track-azure'){'azure'}else{'dotnet'}))) { Write-Output "RELEASE-TRACK-MISMATCH $id $($r.Track) $($r.Release)" }
  }
  if ($r.Priority -notin @('Must','Should','Could')) { Write-Output "BAD-PRIORITY $id $($r.Priority)" }
  if ($r.Parent -ne '-') {
    if (-not $reg.ContainsKey($r.Parent)) { Write-Output "PARENT-MISSING $id -> $($r.Parent)" }
    else {
      $p = $reg[$r.Parent]
      if ($p.Track -ne $r.Track) { Write-Output "PARENT-TRACK $id -> $($r.Parent)" }
      if ($p.Release -ne $r.Release) { Write-Output "PARENT-RELEASE $id ($($r.Release)) -> $($r.Parent) ($($p.Release))" }
    }
  } elseif ($pfx -ne 'EP') { Write-Output "NO-PARENT $id" }
  if ($r.Release -eq '-' -and $r.Priority -ne 'Must' -and $pfx -ne 'EP') { }
}
# Unplanned items must have unplanned parents
foreach ($id in $regOrder) { $r=$reg[$id]; if ($r.Release -eq '-' -and $r.Parent -ne '-' -and $reg.ContainsKey($r.Parent) -and $reg[$r.Parent].Release -ne '-') { Write-Output "UNPLANNED-CHILD-OF-PLANNED $id" } }
# Parent-child: each feature/enabler/story child's parent must be a feature (for EN/US) or epic (for FT)
foreach ($id in $regOrder) {
  $r=$reg[$id]; if ($r.Parent -eq '-') { continue }
  $pp = $reg[$r.Parent].ID.Substring(0,2)
  $cpfx = $id.Substring(0,2)
  if ($cpfx -eq 'FT' -and $pp -ne 'EP') { Write-Output "FT-PARENT-NOT-EP $id" }
  if ($cpfx -in @('US','EN') -and $pp -ne 'FT') { Write-Output "$cpfx-PARENT-NOT-FT $id -> $($r.Parent)" }
}

# ---- 3. Item blocks (sections 6 and 7) ----
$blocks = @{}
$curId = $null; $curLines = $null
$headRx = '^#{3,6} ((EP|FT|US|EN)-(AZ|DN)-\d{2,3})\b'
for ($i = 0; $i -lt $regIdx; $i++) {
  $l = $lines[$i]
  if ($l -match $headRx) {
    $curId = $Matches[1]; $curLines = New-Object System.Collections.ArrayList
    $blocks[$curId] = $curLines
  } elseif ($l -match '^#{1,3} ' ) {
    $curId = $null
  }
  if ($curId -and ($null -ne $curLines)) { [void]$curLines.Add($l) }
}
Write-Output ("ITEM BLOCKS found: {0}" -f $blocks.Count)
$missingBlock = $regOrder | Where-Object { -not $blocks.ContainsKey($_) }
Write-Output ("Register IDs with no item block: " + ($missingBlock -join ', '))
$extraBlock = $blocks.Keys | Where-Object { -not $reg.ContainsKey($_) }
Write-Output ("Item blocks with no register row: " + ($extraBlock -join ', '))

$report = @()
foreach ($id in $blocks.Keys) {
  $bl = $blocks[$id]; $txt = $bl -join "`n"
  $tagsLine = ($bl | Where-Object { $_ -match '^\* Tags:' } | Select-Object -First 1)
  $tagVals = @()
  if ($tagsLine) { $tagVals = ($tagsLine -replace '^\* Tags:\s*','').Split(',') | ForEach-Object { $_.Trim().Trim('`') } }
  $tTrack = @($tagVals | Where-Object { $_ -in @('track-azure','track-dotnet','track-power-platform') })
  $tRel = @($tagVals | Where-Object { $_ -match '^(azure|dotnet)-r\d$' })
  $other = @($tagVals | Where-Object { $_ -notin @('track-azure','track-dotnet','track-power-platform') -and $_ -notmatch '^(azure|dotnet)-r\d$' -and $_ -ne '' })
  $metaLine = ($bl | Where-Object { $_ -match '^\* Type:' } | Select-Object -First 1)
  $metaType = if ($metaLine -match 'Type:\s*(\w+)') { $Matches[1] } else { '?' }
  $metaPrio = if ($metaLine -match 'Priority:\s*(\w+)') { $Matches[1] } else { '?' }
  $metaParent = if ($metaLine -match 'Parent:\s*`([^`]+)`') { $Matches[1] } else { '-' }
  $srcLine = ($bl | Where-Object { $_ -match '^\* \(source:' } | Select-Object -First 1)
  $srcIds = @()
  if ($srcLine) { $srcIds = [regex]::Matches($srcLine, '(BR-\d{2}|NFR-\d{2}|C-\d{2}|CS-\d{2}|ES-\d{2}|SM-\d{2}|P-\d{2}|OQ-\d{2})') | ForEach-Object { $_.Value } | Sort-Object -Unique }
  $isStory = ($id.Substring(0,2) -in @('US','EN'))
  $hasStory = $txt -match '\*\*Story\.\*\*'
  $asA = $txt -match 'As an? '
  $iWant = $txt -match 'I want'
  $soThat = $txt -match 'so that'
  $crit = @($bl | Where-Object { $_ -match '^\d+\. ' })
  $critBad = @($crit | Where-Object { -not ($_ -match 'Given' -and $_ -match '\bWhen\b' -and $_ -match '\bThen\b') })
  $report += [pscustomobject]@{ ID=$id; Tags=($tagVals -join ' | '); TrackN=$tTrack.Count; RelN=$tRel.Count; Other=($other -join ','); Type=$metaType; Prio=$metaPrio; Parent=$metaParent; Src=($srcIds -join ','); IsStory=$isStory; Story=$hasStory; AsA=$asA; Want=$iWant; SoThat=$soThat; Crit=$crit.Count; CritBad=$critBad.Count; TagsLine=[bool]$tagsLine; SrcLine=[bool]$srcLine }
}

# ---- 4. Compare item blocks with register ----
foreach ($row in $report) {
  $id = $row.ID; $r = $reg[$id]
  if (-not $r) { continue }
  if (-not $row.TagsLine) { Write-Output "NO-TAGS-LINE $id" }
  if ($row.TrackN -ne 1) { Write-Output "TRACKTAG-COUNT $id = $($row.TrackN) [$($row.Tags)]" }
  if ($row.RelN -gt 1) { Write-Output "MULTI-RELEASE-TAG $id [$($row.Tags)]" }
  if ($row.Other) { Write-Output "OTHER-TAG $id [$($row.Other)]" }
  $expTags = @($r.Track)
  if ($r.Release -ne '-') { $expTags += $r.Release }
  $gotTags = @($row.Tags -split ' \| ')
  if (($expTags -join ',') -ne (($gotTags | Sort-Object) -join ',') -and ((@($expTags | Sort-Object) -join ',') -ne ((@($gotTags) | Sort-Object) -join ','))) { Write-Output "TAG-VS-REGISTER $id item=[$($row.Tags)] reg=[$($expTags -join ', ')]" }
  if ($row.Type -ne $r.Type) { Write-Output "TYPE-VS-REG $id item=$($row.Type) reg=$($r.Type)" }
  if ($row.Prio -ne $r.Priority) { Write-Output "PRIO-VS-REG $id item=$($row.Prio) reg=$($r.Priority)" }
  $regParent = $r.Parent
  if ($row.Parent -ne $regParent) { Write-Output "PARENT-VS-REG $id item=$($row.Parent) reg=$regParent" }
  $regSrc = @([regex]::Matches($r.Sources, '(BR-\d{2}|NFR-\d{2}|C-\d{2}|CS-\d{2}|ES-\d{2}|SM-\d{2}|P-\d{2}|OQ-\d{2})') | ForEach-Object { $_.Value } | Sort-Object -Unique)
  $a = ($row.Src -split ','); $b = $regSrc
  if (($a -join ',') -ne ($b -join ',')) { Write-Output "SRC-VS-REG $id item=[$($row.Src -join ',')] reg=[$($b -join ',')]" }
  if ($row.IsStory) {
    if (-not $row.Story) { Write-Output "NO-STORY-PARA $id" }
    if (-not ($row.AsA -and $row.Want -and $row.SoThat)) { Write-Output "STORY-FORM-MISSING $id asA=$($row.AsA) want=$($row.Want) soThat=$($row.SoThat)" }
    if ($row.Crit -eq 0) { Write-Output "NO-CRITERIA $id" }
    if ($row.CritBad -gt 0) { Write-Output "CRITERIA-NOT-GWT $id bad=$($row.CritBad) of $($row.Crit)" }
  }
  if (-not $row.SrcLine) { Write-Output "NO-SOURCE-LINE $id" }
}
Write-Output ("Items checked against register: {0}" -f $report.Count)
Write-Output ("Story/enabler count with GWT: " + ($report | Where-Object { $_.IsStory -and $_.Crit -gt 0 }).Count)
$report | Where-Object { $_.IsStory } | Select-Object ID,Crit,CritBad | Format-Table -AutoSize | Out-String -Width 200 | Write-Output
# Export full table for cross-checks
$report | Export-Csv -NoTypeInformation -Encoding UTF8 -LiteralPath 'C:\demos\northwind-workshop\.copilot-tracking\reviews\probe-nw-product-docs\backlog-items.csv'
$regOrder | ForEach-Object { $reg[$_] } | Export-Csv -NoTypeInformation -Encoding UTF8 -LiteralPath 'C:\demos\northwind-workshop\.copilot-tracking\reviews\probe-nw-product-docs\backlog-register.csv'
