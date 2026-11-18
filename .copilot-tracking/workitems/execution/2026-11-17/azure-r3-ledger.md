# azure-r3 ledger (ado / waelconsulting / northwind-workshop)

Format: `[x] localId -> ADO id | parent ADO id | hyperlinks n/N`
Parent links: wit_work_item_link_write action=link linkType=parent. Hyperlinks: wit_work_item_write action=update, one batch of Hyperlink relation Adds per item.

[x] EPIC-104 -> 44 | none | hyperlinks 5/5
[x] FEAT-114 -> 45 | 44 | hyperlinks 4/4
[x] FEAT-110 -> 43 | 44 | hyperlinks 3/3
[x] FEAT-111 -> 46 | 44 | hyperlinks 3/3
[x] FEAT-112 -> 42 | 44 | hyperlinks 3/3
[x] EA-16 -> 49 | 45 | hyperlinks 6/6
[x] EA-13 -> 48 | 43 | hyperlinks 5/5
[x] STORY-170 -> 47 | 43 | hyperlinks 5/5
[x] STORY-171 -> 50 | 43 | hyperlinks 5/5
[x] EA-14 -> 53 | 46 | hyperlinks 5/5
[x] STORY-172 -> 51 | 46 | hyperlinks 5/5
[x] STORY-173 -> 54 | 46 | hyperlinks 5/5
[x] STORY-174 -> 52 | 42 | hyperlinks 4/4

Applied 13/13 items; 12/12 parent links; 58/58 hyperlinks. Remaining 0.
Note: ids are not in operationOrder because creates within a tier ran in parallel; parent links were applied only after all items existed.
