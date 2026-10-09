#!/usr/bin/env python3
"""Raw agreement between the first coding and the blind second coding, per variable.

Usage: agreement.py <coded-corpus.tsv> <second-coding.tsv> > second-coding.md
Rows are matched on the first column (the product slug); columns on their header names.
Prints a markdown table of agreement per variable over the matched rows, the overall raw agreement,
and every disagreement as slug, variable, first value, second value, for the corrections pass.
"""
import csv, sys

def read(p):
    with open(p, newline="") as fh:
        r = csv.DictReader(fh, delimiter="\t")
        return {row[r.fieldnames[0]].strip(): row for row in r}, r.fieldnames

def main():
    a, fa = read(sys.argv[1]); b, fb = read(sys.argv[2])
    common = sorted(set(a) & set(b)); cols = [c for c in fa if c in fb and c != fa[0] and c.lower() != "notes"]
    print(f"# Second coding: raw agreement\n\n{len(common)} profiles coded twice; {len(b) - len(common)} second-coded rows unmatched.\n")
    print("| variable | agree | of | rate |\n|---|---|---|---|")
    tot = agree = 0; dis = []
    for c in cols:
        n = sum(1 for s in common if a[s].get(c, "").strip().lower() == b[s].get(c, "").strip().lower())
        tot += len(common); agree += n
        print(f"| {c} | {n} | {len(common)} | {n/len(common):.2f} |" if common else f"| {c} | 0 | 0 | |")
        dis += [(s, c, a[s].get(c, ""), b[s].get(c, "")) for s in common if a[s].get(c, "").strip().lower() != b[s].get(c, "").strip().lower()]
    print(f"\nOverall raw agreement: {agree}/{tot} = {agree/tot:.3f}\n" if tot else "")
    print("## Disagreements\n\n| slug | variable | first | second |\n|---|---|---|---|")
    for s, c, x, y in dis:
        print(f"| {s} | {c} | {x[:60]} | {y[:60]} |")

if __name__ == "__main__":
    main()
