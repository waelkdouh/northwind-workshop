# azure-r1 ledger (ado / waelconsulting / northwind-workshop)

Format: `[x] localId -> ADO id | parent ADO id | hyperlinks n/N`
Parent links: wit_work_item_link_write action=link linkType=parent. Hyperlinks: wit_work_item_write action=update, one batch of Hyperlink relation Adds per item.

[x] EPIC-101 -> 2 | none | hyperlinks 5/5
[x] EPIC-102 -> 1 | none | hyperlinks 5/5
[x] FEAT-101 -> 3 | 2 | hyperlinks 3/3
[x] FEAT-102 -> 5 | 2 | hyperlinks 3/3
[x] FEAT-103 -> 4 | 2 | hyperlinks 3/3
[x] FEAT-104 -> 7 | 1 | hyperlinks 4/4
[x] FEAT-105 -> 6 | 1 | hyperlinks 4/4
[x] EA-01 -> 11 | 3 | hyperlinks 5/5
[x] EA-11 -> 9 | 3 | hyperlinks 4/4
[x] STORY-101 -> 10 | 3 | hyperlinks 4/4
[x] STORY-104 -> 8 | 3 | hyperlinks 5/5
[x] STORY-105 -> 16 | 3 | hyperlinks 4/4
[x] EA-02 -> 12 | 5 | hyperlinks 4/4
[x] STORY-102 -> 13 | 5 | hyperlinks 4/4
[x] EA-03 -> 15 | 4 | hyperlinks 5/5
[x] STORY-103 -> 14 | 4 | hyperlinks 5/5
[x] EA-05 -> 20 | 7 | hyperlinks 5/5
[x] STORY-120 -> 18 | 7 | hyperlinks 6/6
[x] EA-09 -> 21 | 6 | hyperlinks 5/5
[x] STORY-121 -> 17 | 6 | hyperlinks 5/5
[x] STORY-122 -> 19 | 6 | hyperlinks 6/6

Totals: 21/21 items created, 19/19 parent links, 94/94 hyperlinks. Remaining: 0.
Read-back: WIQL Tags CONTAINS 'azure-r1' returned 21 items (ids 1-21); get_batch confirmed types, titles, parents, priority 1.
