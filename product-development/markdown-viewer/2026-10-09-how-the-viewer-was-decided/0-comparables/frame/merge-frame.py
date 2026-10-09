#!/usr/bin/env python3
"""Fold the per-list frame TSVs into one frame.

Usage: merge-frame.py <frame-dir>
Reads every *.tsv in the directory except frame.tsv. A row is one list entry; a comparable
is one product, which may sit in several lists. Rows are joined into one comparable when
their normalised names match exactly or their identifiers share a host and path; a pair of
names where one contains the other is not joined but flagged for the frame reviewer.
Writes frame.tsv (one row per comparable: product, cells, identifiers, eligibility per cell,
descriptions per cell) and frame-cells.md (counts per cell, in/out/undecidable, and the
flagged possible duplicates). Nothing is dropped: an "out" row stays, marked out.
"""
import csv, re, sys, collections
from pathlib import Path

def norm(name):
    s = name.lower()
    s = re.sub(r"\(.*?\)", " ", s)
    s = re.sub(r"[^a-z0-9]+", " ", s).strip()
    s = re.sub(r"\b(app|application|the|for mac|for macos|for linux|for windows|markdown editor|markdown viewer|markdown)\b", " ", s)
    return re.sub(r"\s+", " ", s).strip()

def ident_key(ident):
    m = re.search(r"https?://([^/\s]+)(/[^\s?#]*)?", ident or "")
    if not m:
        return None
    host, path = m.group(1).lower(), (m.group(2) or "").rstrip("/").lower()
    host = host.replace("www.", "")
    if host == "github.com":
        path = "/".join(path.split("/")[:3])
    return host + path if path else host

def main():
    d = Path(sys.argv[1])
    rows = []
    for f in sorted(d.glob("*.tsv")):
        if f.name == "frame.tsv":
            continue
        with f.open(newline="") as fh:
            r = csv.DictReader(fh, delimiter="\t")
            for row in r:
                row = {k.strip().lower(): (v or "").strip() for k, v in row.items() if k}
                row["_file"] = f.stem
                rows.append(row)
    def get(row, *keys):
        for k in keys:
            for rk in row:
                if rk.startswith(k):
                    return row[rk]
        return ""
    comps = {}          # key -> comparable
    name_index = {}     # normalised name -> key
    ident_index = {}    # ident key -> key
    for row in rows:
        name = get(row, "entry", "name", "product")
        ident = get(row, "identifier", "url")
        cell = (get(row, "list") or row["_file"]) + (":" + get(row, "cell") if get(row, "cell") else "")
        nk, ik = norm(name), ident_key(ident)
        key = (ik and ident_index.get(ik)) or (nk and name_index.get(nk))
        if key is None:
            key = len(comps)
            comps[key] = {"product": name, "names": set(), "cells": [], "idents": set(), "elig": [], "desc": []}
        c = comps[key]
        c["names"].add(name)
        if nk: name_index.setdefault(nk, key)
        if ik: ident_index.setdefault(ik, key)
        c["cells"].append(cell)
        if ident: c["idents"].add(ident)
        c["elig"].append(f"{cell}={get(row, 'eligible') or '?'}")
        desc = get(row, "description", "summary")
        if desc: c["desc"].append(f"{cell}: {desc[:200]}")
    # flagged possible duplicates: one normalised name contained in another, different comparables
    keys = {norm(c["product"]): k for k, c in comps.items() if norm(c["product"])}
    flagged = []
    names = sorted(keys)
    for i, a in enumerate(names):
        for b in names[i+1:]:
            if len(a) >= 4 and (a in b.split() or (a in b and b.startswith(a + " "))):
                flagged.append((comps[keys[a]]["product"], comps[keys[b]]["product"]))
    out = d / "frame.tsv"
    with out.open("w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["product", "cells", "identifiers", "eligibility per cell", "descriptions per cell"])
        for c in comps.values():
            w.writerow([c["product"], "; ".join(c["cells"]), " ".join(sorted(c["idents"])), "; ".join(c["elig"]), " || ".join(c["desc"])])
    cells = collections.defaultdict(collections.Counter)
    for c in comps.values():
        for e in c["elig"]:
            cell, _, v = e.partition("=")
            cells[cell][v.lower()] += 1
    with (d / "frame-cells.md").open("w") as fh:
        fh.write("# The merged frame, by cell\n\nOne comparable is one product; a product in several lists sits in several cells. Counts are comparables per cell by the eligibility the list's builder gave.\n\n| cell | in | out | undecidable | other |\n|---|---|---|---|---|\n")
        for cell in sorted(cells):
            ct = cells[cell]
            other = sum(v for k, v in ct.items() if k not in ("in", "out", "undecidable"))
            fh.write(f"| {cell} | {ct.get('in',0)} | {ct.get('out',0)} | {ct.get('undecidable',0)} | {other} |\n")
        fh.write(f"\nComparables in the merged frame: {len(comps)}, from {len(rows)} list rows.\n")
        fh.write(f"\n## Possible duplicates not joined (one name inside another), for the reviewer\n\n")
        for a, b in flagged:
            fh.write(f"- {a} / {b}\n")
        if not flagged:
            fh.write("none\n")
    print(f"{len(rows)} rows -> {len(comps)} comparables; {len(flagged)} flagged pairs")

if __name__ == "__main__":
    main()
