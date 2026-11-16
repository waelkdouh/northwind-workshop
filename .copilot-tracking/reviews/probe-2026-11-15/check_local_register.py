import re, datetime
from pathlib import Path
PROD = Path("/Users/waelkdouh/Demos/northwind-workshop/docs/product")
files = {"BRD": PROD/"business-requirements.md", "PRD": PROD/"product-requirements.md", "EXP": PROD/"experiments.md", "BACKLOG": PROD/"backlog.md", "TRACE": PROD/"traceability.md"}
for p in sorted((PROD/"releases").glob("*.md")):
    files["REL "+p.name] = p
ID = r"(?<![A-Za-z0-9-])((?:A|O|X|T|G|OQ)-\d+)(?![0-9])"
for dn, p in files.items():
    text = p.read_text(encoding="utf-8")
    defined = set()
    for ln in text.splitlines():
        if ln.startswith("|"):
            c = [x.strip().strip("`*") for x in ln.strip().strip("|").split("|")]
            if c and re.match(r"^(A|O|X|T|G|OQ)-\d+$", c[0]):
                defined.add(c[0])
    cited = set(re.findall(ID, text))
    missing = sorted(cited - defined, key=lambda s: (s.split('-')[0], int(s.split('-')[1])))
    print(f"{dn}: cited={len(cited)} defined_in_own_register={len(defined)} cited_not_in_own_register={missing}")
print()
for d in [6, 13, 20, 27]:
    dt = datetime.date(2027, 6, d)
    print("2027-06-%02d weekday:" % d, dt.strftime("%A"))
print("2027-06-30 weekday:", datetime.date(2027,6,30).strftime("%A"))
print("azure-r2 window end 31 Mar 2027 vs dotnet-r2 start 1 Mar 2027 (overlap days):", (datetime.date(2027,3,31)-datetime.date(2027,3,1)).days+1)
print("900/52 =", round(900/52,4), "| 1500/?; 9400 rows; 48+8=56 GB; 120+16=136 GB check:", 48+1*8, 120+2*8)
