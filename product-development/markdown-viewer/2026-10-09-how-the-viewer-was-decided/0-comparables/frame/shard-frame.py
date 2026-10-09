#!/usr/bin/env python3
"""Draw the collection list from the merged frame under the frame review's verdicts, and cut it into shards.

Usage: shard-frame.py <frame-dir> <shard-size> <cell-spec>...
A cell-spec is  <cell-name>            every comparable the cell marks in (a census), or
                <cell-name>:every=<k>  every k-th such comparable in the cell's own row order (a systematic sample), or
                <cell-name>:undecidable  the cell's undecidable rows as well as its in rows.
Cell names match the cell column of frame.tsv by prefix. A comparable drawn by any passing cell is collected once.
Writes collection-list.tsv (slug, product, cells, identifiers, drawn-by) and shards.md (shard -> slugs).
"""
import csv, re, sys
from pathlib import Path

def slug(name):
    s = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    return s[:60] or "unnamed"

def main():
    d, size, specs = Path(sys.argv[1]), int(sys.argv[2]), sys.argv[3:]
    rows = list(csv.DictReader((d / "frame.tsv").open(newline=""), delimiter="\t"))
    drawn = {}  # slug -> row, drawn-by
    for spec in specs:
        name, _, opt = spec.partition(":")
        step = int(opt.split("=")[1]) if opt.startswith("every=") else 1
        want = ("in", "undecidable") if opt == "undecidable" else ("in",)
        members = []
        for r in rows:
            cells = [c.strip() for c in r["cells"].split(";")]
            eligs = dict(e.strip().rsplit("=", 1) for e in r["eligibility per cell"].split(";") if "=" in e)
            for c in cells:
                if c.startswith(name) and eligs.get(c, "").lower() in want:
                    members.append(r); break
        for i, r in enumerate(members):
            if i % step == 0:
                s = slug(r["product"])
                drawn.setdefault(s, (r, []))[1].append(spec)
        print(f"{spec}: {len(members)} members, {sum(1 for i in range(len(members)) if i % step == 0)} drawn")
    slugs = sorted(drawn)
    with (d / "collection-list.tsv").open("w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t"); w.writerow(["slug", "product", "cells", "identifiers", "drawn-by"])
        for s in slugs:
            r, by = drawn[s]; w.writerow([s, r["product"], r["cells"], r["identifiers"], "; ".join(by)])
    shards = [slugs[i:i + size] for i in range(0, len(slugs), size)]
    with (d / "shards.md").open("w") as fh:
        fh.write(f"# Collection shards\n\n{len(slugs)} comparables drawn under the frame review's verdicts, in {len(shards)} shards of up to {size} by sorted slug.\n\n")
        for n, sh in enumerate(shards, 1):
            fh.write(f"## shard-{n:02d}\n\n" + "\n".join(f"- {s}" for s in sh) + "\n\n")
    print(f"{len(slugs)} comparables in {len(shards)} shards")

if __name__ == "__main__":
    main()
