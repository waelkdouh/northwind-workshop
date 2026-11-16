import re
from collections import Counter
from pathlib import Path
P = Path("/Users/waelkdouh/Demos/northwind-workshop/docs/product")
files = {"BRD": P/"business-requirements.md", "PRD": P/"product-requirements.md", "EXP": P/"experiments.md", "BACKLOG": P/"backlog.md", "TRACE": P/"traceability.md", "REL-azure-r1": P/"releases/azure-r1.md", "REL-dotnet-r2": P/"releases/dotnet-r2.md"}
ACR = re.compile(r"(?<![A-Za-z`/\-])([A-Z][A-Za-z]?[A-Z]{1,5}[a-z]?s?)(?![A-Za-z0-9-])")
for name, p in files.items():
    text = p.read_text(encoding="utf-8")
    prose = []
    for ln in text.splitlines():
        s = ln.strip()
        if not s or s.startswith(("|", "#", "---", "```", "<!--", ">")) or s.startswith(("* `", "- `")):
            continue
        s = re.sub(r"`[^`]*`", " ", s)
        prose.append(s)
    sents = []
    for para in prose:
        for sent in re.split(r"(?<=[.!?])\s+", para):
            w = len(sent.split())
            if w >= 3:
                sents.append((w, sent))
    lens = [w for w,_ in sents]
    long = [s for w,s in sents if w > 30]
    avg = sum(lens)/len(lens) if lens else 0
    print(f"{name}: prose sentences={len(lens)} avg_words={avg:.1f} sentences_over_30_words={len(long)}")
    for s in long[:2]:
        print("   long:", s[:200])
    # acronyms in prose (not in code spans)
    acr = Counter(m.group(1) for m in ACR.finditer("\n".join(prose)))
    gloss = ""
    gm = re.search(r"^## (1[4-7])\. Glossary.*?(?=^## |\Z)", text, re.M|re.S)
    if gm: gloss = gm.group(0)
    undefined = [a for a in acr if a not in gloss and a not in ("I","A","The","This","Each","Not","If","No","Yes")]
    print("   acronyms in prose not in glossary:", sorted(undefined)[:40])
