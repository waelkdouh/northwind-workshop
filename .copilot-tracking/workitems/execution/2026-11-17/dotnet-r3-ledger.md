# dotnet-r3 ledger (ado / waelconsulting / northwind-workshop)

Format: `[x] localId -> ADO id | parent ADO id | hyperlinks n/N`
Parent links: wit_work_item_link_write action=link linkType=parent. Hyperlinks: wit_work_item_write action=update, one batch of Hyperlink relation Adds per item.
Note: ADO normalises System.Tags to alphabetical order (`dotnet-r3; nw-workshop; track-dotnet`); the tag set equals the payload `tags` string.

[x] EPIC-203 -> 99 | none | hyperlinks 5/5
[x] FEAT-211 -> 103 | 99 | hyperlinks 3/3
[x] FEAT-212 -> 102 | 99 | hyperlinks 3/3
[x] FEAT-213 -> 100 | 99 | hyperlinks 4/4
[x] FEAT-214 -> 101 | 99 | hyperlinks 3/3
[x] EN-07 -> 105 | 103 | hyperlinks 4/4
[x] STORY-260 -> 111 | 103 | hyperlinks 5/5
[x] STORY-261 -> 106 | 102 | hyperlinks 5/5
[x] STORY-262 -> 104 | 102 | hyperlinks 5/5
[x] STORY-263 -> 109 | 100 | hyperlinks 5/5
[x] STORY-264 -> 110 | 100 | hyperlinks 5/5
[x] EN-14 -> 108 | 101 | hyperlinks 4/4
[x] STORY-265 -> 107 | 101 | hyperlinks 4/4

Total: 13/13 items, 55 hyperlinks (epic 5 + features 13 + stories 37).
