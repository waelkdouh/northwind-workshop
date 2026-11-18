# dotnet-r2 ledger (ado / waelconsulting / northwind-workshop)

Format: `[x] localId -> ADO id | parent ADO id | hyperlinks n/N`
Parent links: wit_work_item_link_write action=link linkType=parent. Hyperlinks: wit_work_item_write action=update, one batch of Hyperlink relation Adds per item.
Note: ADO normalises System.Tags to alphabetical order (`dotnet-r2; nw-workshop; track-dotnet`); the tag set equals the payload `tags` string.

[x] EPIC-202 -> 78 | none | hyperlinks 5/5
[x] FEAT-207 -> 79 | 78 | hyperlinks 4/4
[x] FEAT-208 -> 80 | 78 | hyperlinks 4/4
[x] FEAT-209 -> 81 | 78 | hyperlinks 4/4
[x] FEAT-210 -> 82 | 78 | hyperlinks 3/3
[x] FEAT-206 -> 83 | 78 | hyperlinks 3/3
[x] STORY-230 -> 84 | 83 | hyperlinks 5/5
[x] EN-11 -> 85 | 83 | hyperlinks 6/6
[x] STORY-239 -> 86 | 83 | hyperlinks 5/5
[x] STORY-240 -> 87 | 83 | hyperlinks 5/5
[x] STORY-234 -> 88 | 80 | hyperlinks 6/6
[x] STORY-231 -> 89 | 79 | hyperlinks 5/5
[x] STORY-233 -> 90 | 79 | hyperlinks 6/6
[x] STORY-232 -> 91 | 79 | hyperlinks 5/5
[x] STORY-235 -> 92 | 80 | hyperlinks 5/5
[x] STORY-237 -> 93 | 81 | hyperlinks 5/5
[x] STORY-238 -> 94 | 81 | hyperlinks 6/6
[x] STORY-242 -> 95 | 82 | hyperlinks 5/5
[x] STORY-241 -> 96 | 82 | hyperlinks 5/5
[x] STORY-243 -> 97 | 82 | hyperlinks 5/5
[x] STORY-236 -> 98 | 80 | hyperlinks 6/6

Total: 21/21 items, 103 hyperlinks (epic 5 + features 18 + stories 80).
Read-back (WIQL [System.Tags] CONTAINS 'dotnet-r2'): 21 items; types, `wael-01 ` titles, tags, parents, priority (all 1 except STORY-237 = 2, matching adoPriorityProposed) and System.HyperLinkCount verified for every item.
Incident: one parent-link call (FEAT-208 -> EPIC-202) returned TF401349 when issued concurrently with an update on the same item; retried once and succeeded (no duplicate).
