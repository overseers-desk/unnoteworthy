#!/usr/bin/env python3
"""Concatenate the coded shards into one corpus, one row per product, 37 variable columns.

Usage: concat-coded.py <comparables-dir>
Reads every coded/shard-*.tsv. A shard's separator is the tab, or "@@" or "|||" where a clerk wrote
one of those. Each header is mapped to its variable id by its leading V and two digits ("V16", "v16b",
"V16 price (a) shape (b) licence (c)"); a sub-field column (V12a, V12b) is folded into its variable's
cell as "(a) ...; (b) ...". Writes coded-corpus.tsv with columns slug, V01 to V37, notes, and reports
any shard whose columns could not be mapped and any slug coded twice (first row kept).
"""
import csv, re, sys
from pathlib import Path

VARS = [f"V{i:02d}" for i in range(1, 38)]

def split_line(line, sep):
    return line.rstrip("\n").split(sep)

def main():
    d = Path(sys.argv[1]); files = sorted((d / "coded").glob("shard-*.tsv"))
    out_rows, seen, problems = [], {}, []
    for f in files:
        lines = f.read_text(errors="replace").splitlines()
        if not lines: problems.append(f"{f.name}: empty"); continue
        sep = "\t" if "\t" in lines[0] else ("@@" if "@@" in lines[0] else ("|||" if "|||" in lines[0] else None))
        if sep is None: problems.append(f"{f.name}: no separator found in header"); continue
        if sep == "\t":
            with f.open(newline="") as fh:
                rows = list(csv.reader(fh, delimiter="\t"))
        else:
            rows = [split_line(l, sep) for l in lines]
        header = [h.strip() for h in rows[0]]
        keys = []
        for h in header:
            m = re.match(r"^[Vv](\d{2})\s*([a-z])?", h)
            if m: keys.append(("V" + m.group(1), m.group(2) or ""))
            elif h.lower().startswith("slug"): keys.append(("slug", ""))
            elif h.lower().startswith("note"): keys.append(("notes", ""))
            elif re.match(r"^[Rr]\d", h): keys.append(("notes", h.split()[0].upper()))   # a record column folds into notes
            else: keys.append((None, h))
        unmapped = [h for (k, _), h in zip(keys, header) if k is None]
        if unmapped: problems.append(f"{f.name}: unmapped columns {unmapped}")
        missing = [v for v in VARS if v not in {k for k, _ in keys}]
        if missing: problems.append(f"{f.name}: variables absent {missing}")
        for row in rows[1:]:
            if not row or not row[0].strip(): continue
            cells = {}
            for (k, sub), val in zip(keys, row):
                if k is None: continue
                val = val.strip()
                if sub and k == "notes":
                    if val: cells[k] = (cells.get(k, "") + ("; " if cells.get(k) else "") + f"{sub}: {val}").strip()
                elif sub:
                    cells[k] = (cells.get(k, "") + ("; " if cells.get(k) else "") + f"({sub}) {val}").strip()
                else:
                    cells[k] = (cells.get(k, "") + ("; " if cells.get(k) else "") + val).strip() if val else cells.get(k, "")
            slug = cells.get("slug", "").strip()
            if slug in seen: problems.append(f"{f.name}: {slug} already coded in {seen[slug]}"); continue
            seen[slug] = f.name
            out_rows.append([slug] + [cells.get(v, "") for v in VARS] + [cells.get("notes", "")])
    with (d / "coded-corpus.tsv").open("w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t"); w.writerow(["slug"] + VARS + ["notes"]); w.writerows(out_rows)
    for p in problems: print(p)
    print(f"{len(files)} shards, {len(out_rows)} rows, {1 + len(VARS) + 1} columns")

if __name__ == "__main__":
    main()
