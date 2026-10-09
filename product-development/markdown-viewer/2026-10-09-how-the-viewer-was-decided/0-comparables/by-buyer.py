#!/usr/bin/env python3
"""Cross the variables the leading buyers' parameter list cites with V05.

Reads 0-comparables/coded-corpus.tsv and 0-comparables/frame/collection-list.tsv
(plain tab splitting; the files carry no quoting) and prints every table behind
the "Findings by buyer" section of findings.md.

Run from anywhere:  python3 -B by-buyer.py [--check]
--check prints the ALL column of each variable used, for comparison with taxonomy.md.

Reading a cell: the value of an element is its text before the first quote, bracket,
'::', '@' or ': ', after leading tags such as '(p)' are dropped; elements are split at
';', '||' and a single '|', sub-fields at '(a)' or 'a: '; every codebook value named in
that text is counted (so "Windows, macOS" counts both). An element that says
"undecidable" yields no value. This reads a few more coded values than taxonomy.md did
(finding 49 of findings.md); the V05 reconciliation table prints both readings.

Populations, weights and silence follow findings.md, "How the counts are made":
  ALL       every eligible row in an application cell, AlternativeTo-sampled rows weight 2
  SHAPE     GitHub-topic rows that state no payment, plus the free rows of the store and
            package cells; unweighted (no sampled row is in it)
  STORE-NS  store and package rows not in SHAPE (used only for the cell table)
A row is free where V23 or V16(b) states a price and every stated value is free,
donation invited, or nothing paid before use. Silent = "not stated", counted once per row.

Buyer columns (V05, as coded and corrected):
  D-only  names Developers and coders, not Writers and authors
  W-only  names Writers and authors, not Developers and coders
  D+W     names both
  AI      names Readers of what AI agents write (overlaps the three above where a row
          names both; the overlap is printed)
  other   names at least one class, none of developers, writers or AI readers
  silent  V05 not stated (each row once); 'undec' = V05 undecidable only
"""

import os
import re
import sys
from collections import OrderedDict, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
CORPUS = os.path.join(HERE, "coded-corpus.tsv")
FRAME = os.path.join(HERE, "frame", "collection-list.tsv")

# ---------------------------------------------------------------- value lists

VALUES = {
    "V03": ["markdown token in name", "function word in name", "maker name in title",
            "none of the above"],
    "V04": ["single program", "one program in editions", "program and component",
            "family of programs", "component only"],
    "V05": ["Writers and authors", "Bloggers and platform publishers",
            "Students and academics", "Developers and coders",
            "Note-takers and personal knowledge managers",
            "Teams, businesses and organisations", "Terminal readers",
            "Plain readers of received markdown files",
            "Readers of what AI agents write",
            "Application developers embedding a markdown view"],
    "V07": ["pay or buy", "subscribe", "download a file", "install from a store",
            "install by a package-manager command", "clone or build from source",
            "open in a browser", "add as a dependency", "create an account or sign in",
            "contact sales or request a quote", "star, follow or watch",
            "sponsor or donate"],
    "V09": ["reader, stated read-only", "reader, editing not stated",
            "editor with rendered view", "editor, rendered view not stated"],
    "V10": ["Windows", "macOS", "Linux", "BSD", "iOS", "iPadOS", "Android", "ChromeOS",
            "any desktop with a web browser", "inside a host program"],
    "V11": ["none needed, stated", "runtime or interpreter named", "host program named",
            "package manager named as required to install", "build toolchain named",
            "minimum operating-system version named"],
    "V12a": ["run an installer or open a package file", "store install",
             "package-manager command", "copy or unpack a binary",
             "build or run from source", "host program's extension manager",
             "open a URL"],
    "V12b": ["updates itself, stated", "through the store", "through the package manager",
             "download the new version by hand, stated", "no updates planned, stated"],
    "V13a": ["CommonMark", "GitHub Flavored Markdown", "other named flavour", "tables",
             "task lists", "footnotes", "math", "diagrams",
             "syntax-highlighted code blocks", "front matter", "wiki-links", "raw HTML",
             "emoji shortcodes", "callouts or admonitions",
             "markdown named, no form named"],
    "V13b": ["shown as plain text, stated", "dropped or hidden, stated",
             "warned about, stated"],
    "V14": ["local, stated", "local by default, optional upload stated",
            "content leaves the device, stated"],
    "V15": ["works offline, stated", "network required, stated",
            "network used for named features only, stated",
            "no telemetry or tracking, stated",
            "telemetry, analytics or crash reports sent, stated",
            "account required, stated"],
    "V16b": ["free", "free with paid tier or features", "one-time purchase",
             "one-time purchase with paid upgrades", "subscription",
             "free trial, then paid", "pay what you want",
             "donation or sponsorship invited, use free",
             "paid licence for a named use", "price on request"],
    "V16c": ["named open-source licence", "source available, not open-source, stated",
             "proprietary or end-user licence agreement, stated",
             "public domain, stated"],
    "V18": ["commercial or work use free, stated",
            "commercial or work use needs a paid licence, stated",
            "team, business or volume licence offered",
            "work use restricted or forbidden, stated"],
    "V19": ["a copy to download or install", "a licence per person",
            "a licence per device", "a subscription per person",
            "a licence or subscription per organisation, team or site",
            "a package the system's package manager maintains",
            "a component built into the buyer's software", "an account on a service",
            "support or a support contract"],
    "V20": ["application store listing", "extension marketplace listing",
            "package registry page", "code repository page", "release page",
            "maker's own website", "web store or checkout page"],
    "V22": ["through an application store or marketplace",
            "through a package repository or package manager",
            "by downloading a release or binary from the maker",
            "by cloning or downloading source and running or building it",
            "by opening it in a browser", "by adding it as a dependency"],
    "V23": ["nothing paid before use, stated", "payment required before first use, stated",
            "free trial, then payment", "free use, payment for more",
            "donation invited, not required"],
    "V24": ["purchase through a store or marketplace", "in-app purchase",
            "checkout or licence key from the maker or a payment processor",
            "subscription account with the maker", "sponsorship or donation platform",
            "contact sales", "no sale taken, stated"],
    "V28": ["outline, contents or headings sidebar", "jump to heading or section",
            "folding of sections", "minimap or overview strip",
            "scroll position kept or synchronised", "bookmarks"],
    "V29": ["search within the document", "search across files or a folder",
            "regular-expression search", "find and replace"],
    "V31": ["reloads when the file changes on disk, stated",
            "preview updates as you type inside the product, stated", "both stated",
            "manual refresh, stated"],
    "V32": ["themes provided", "light and dark modes", "custom stylesheet",
            "font or size choice", "follows the system appearance, stated"],
    "V33": ["print", "export to PDF", "export to HTML", "export to another named format",
            "copy as rich text or HTML", "share or send from the product"],
}

# Clerk wordings that name a listed value in other words (see the --aliases report).
OSL = ("named open-source licence")
ALIASES = {
    "V07": [("install from store", "install from a store")],
    "V24": [("checkout or licence key", "checkout or licence key from the maker or a "
             "payment processor")],
    "V16c": [("proprietary", "proprietary or end-user licence agreement, stated"),
             ("eula", "proprietary or end-user licence agreement, stated")]
            + [(k, OSL) for k in ("mit", "gpl", "agpl", "lgpl", "apache", "bsd", "mpl",
                                  "isc", "unlicense", "wtfpl", "zlib", "epl", "artistic",
                                  "gnu", "cc0", "mozilla public license")],
}

# variable -> (corpus column, sub-field letter or None)
COLUMN = {v: (v, None) for v in VALUES}
COLUMN.update({"V12a": ("V12", "a"), "V12b": ("V12", "b"), "V13a": ("V13", "a"),
               "V13b": ("V13", "b"), "V16b": ("V16", "b"), "V16c": ("V16", "c")})

# ---------------------------------------------------------------- parsing


def norm(s):
    s = s.lower().replace("‑", "-").replace("‐", "-")
    s = s.replace("’", "'")
    s = re.sub(r"[^a-z0-9']+", " ", s)
    words = [w.strip("'") for w in s.split()]
    return " ".join(w for w in words if w and w not in ("a", "an", "the"))


def clean(cell):
    c = cell.strip()
    if len(c) >= 2 and c[0] == '"' and c[-1] == '"':
        c = c[1:-1]
    c = c.replace("'\"'\"'", "'").replace('\\"', '"').replace('""', '"')
    return c


OPEN = {"(": ")", "[": "]", "{": "}", "«": "»", "“": "”"}
TAG = re.compile(r"^\s*[\(\[][A-Za-z0-9]{1,2}[\)\]]\s*")


def top_level_parts(c, split_pipe=True):
    """Split a cell into (subfield, element) pairs at top level: elements at ';', '||'
    and (unless split_pipe is False) a single '|'; sub-fields at '(a)', '(b)', '(c)' or
    'a: ', 'b: ', 'c: '. Text inside brackets or quotes is kept with its element.
    split_pipe=False reproduces the reading behind taxonomy.md, which did not treat a
    single '|' as a separator."""
    if not split_pipe:
        c = re.sub(r"(?<!\|)\|(?!\|)", "/", c)
    parts = []
    sub = None
    buf = []
    stack = []
    inq = False
    i = 0
    n = len(c)
    while i < n:
        ch = c[i]
        if not stack and not inq:
            m = re.match(r"\((a|b|c)\)", c[i:i + 3])
            if not m and (i == 0 or c[i - 1] in " ;|"):
                m = re.match(r"(a|b|c):\s", c[i:i + 3])
            if m:
                parts.append((sub, "".join(buf)))
                buf = []
                sub = m.group(1)
                i += len(m.group(0))
                continue
            if ch in ";|":
                parts.append((sub, "".join(buf)))
                buf = []
                i += 1
                continue
        if inq:
            if ch == '"':
                inq = False
        elif stack and ch == stack[-1]:
            stack.pop()
        elif ch in OPEN:
            stack.append(OPEN[ch])
        elif ch == '"':
            inq = True
        buf.append(ch)
        i += 1
    parts.append((sub, "".join(buf)))
    return parts


def prefix(el):
    """The value part of an element: text before its first quote, bracket, '::', '@'
    or ': ', after leading single-letter tags are dropped."""
    e = el
    while True:
        m = TAG.match(e)
        if not m:
            break
        e = e[m.end():]
    cut = len(e)
    for tok in ["«", "[", "{", "(", '"', "“", "::", "@", ": ", " - ", " — "]:
        k = e.find(tok)
        if k != -1 and k < cut:
            cut = k
    return e[:cut]


_vcache = {}


def matchers(var):
    if var not in _vcache:
        out = []
        for v in VALUES[var]:
            out.append((norm(v), v))
            core = re.sub(r",? stated$", "", v)
            if core != v and len(norm(core)) > 8:
                out.append((norm(core), v))
        out += [(norm(k), v) for k, v in ALIASES.get(var, [])]
        out = [o for o in out if o[0]]
        out.sort(key=lambda t: -len(t[0]))
        _vcache[var] = out
    return _vcache[var]


def parse(cell, var, split_pipe=True):
    """Return (set of values, status) where status is 'value', 'silent', 'undec' or
    'unparsed'."""
    col, sub = COLUMN[var]
    c = clean(cell)
    parts = top_level_parts(c, split_pipe)
    has_sub = any(s is not None for s, _ in parts)
    if has_sub and sub is not None:
        parts = [(s, e) for s, e in parts if s == sub]
    vals = set()
    text_all = " ".join(e for _, e in parts)
    for _, el in parts:
        p = " " + norm(prefix(el)) + " "
        if " undecidable " in p:
            continue  # "undecidable for iPadOS" names the point left open, not a value
        for key, v in matchers(var):
            k = " " + key + " "
            while k in p:
                vals.add(v)
                p = p.replace(k, " | ", 1)
    if vals:
        return vals, "value"
    t = norm(text_all)
    if "undecidable" in t:
        return vals, "undec"
    if "not stated" in t or "n s" == t or t == "" or "not coded" in t or "n c" in t:
        return vals, "silent"
    return vals, "unparsed"


# ---------------------------------------------------------------- the frame

CELL_CODE = OrderedDict([
    ("Flathub", "FH"), ("Mac App Store", "MAS"), ("Snap Store", "SN"),
    ("debian:apt-cache search markdown", "UA"), ("homebrew:cask", "HB-C"),
    ("homebrew:formula", "HB-F"), ("vscode", "VS"),
    ("alternativeto:Typora", "AT-T"), ("alternativeto:Obsidian", "AT-O"),
    ("alternativeto:Marked (AlternativeTo entry for Marked)", "AT-M"),
    ("alternativeto:Glow", "AT-G"),
    ("github-topics:markdown-editor", "GH-E"), ("github-topics:markdown-viewer", "GH-V"),
    ("github-topics:markdown-preview", "GH-P"), ("github-topics:markdown-reader", "GH-R"),
    ("awesome-claude-code", "ACC"),
])
STORE = {"FH", "MAS", "SN", "UA", "HB-C", "HB-F", "VS"}
GH = {"GH-E", "GH-V", "GH-P", "GH-R"}
AT = {"AT-T", "AT-O", "AT-M", "AT-G"}
WEIGHTED = {"ALL", "AT", "not-MAS"}  # populations that carry the AlternativeTo weight
FREE_VALUES = {"free", "donation or sponsorship invited, use free",
               "nothing paid before use, stated", "donation invited, not required"}


def read_tsv(path):
    with open(path, encoding="utf-8") as f:
        lines = f.read().split("\n")
    head = lines[0].split("\t")
    rows = []
    for ln in lines[1:]:
        if not ln.strip():
            continue
        rows.append(dict(zip(head, ln.split("\t"))))
    return rows


def load():
    corpus = {r["slug"]: r for r in read_tsv(CORPUS)}
    frame = {r["slug"]: r for r in read_tsv(FRAME)}
    rows = []
    for slug, r in corpus.items():
        f = frame[slug]
        elig = norm(prefix(clean(r["V01"]))) == "eligible"
        if not elig:
            continue
        cells = []
        for c in f["cells"].split(";"):
            c = c.strip()
            if c in CELL_CODE:
                cells.append(CELL_CODE[c])
        if not cells:
            continue  # tcl-wiki only, or the no-go Chrome cell only
        w = int(f["weight"])
        parsed = {var: parse(r[COLUMN[var][0]], var) for var in VALUES}
        v05_old = parse(r["V05"], "V05", split_pipe=False)
        price = set()
        for var in ("V16b", "V23"):
            price |= parsed[var][0]
        if not price:
            pstat = "silent"
        elif price <= FREE_VALUES:
            pstat = "free"
        else:
            pstat = "paid"
        gh = bool(set(cells) & GH)
        st = bool(set(cells) & STORE)
        shape = (gh and pstat != "paid") or (st and pstat == "free")
        rows.append({"slug": slug, "cells": cells, "w": w, "p": parsed, "price": pstat,
                     "SHAPE": shape, "STORE-NS": st and not shape, "ALL": True,
                     "MAS": "MAS" in cells, "MAS-free": "MAS" in cells and pstat == "free",
                     "AT": bool(set(cells) & AT), "not-MAS": "MAS" not in cells,
                     "V05-old": v05_old})
    return rows


# ---------------------------------------------------------------- buyers

D, W, A = "Developers and coders", "Writers and authors", "Readers of what AI agents write"
BUYERS = ["D-only", "W-only", "D+W", "AI", "other", "silent", "undec"]


def buyer_of(row):
    vals, st = row["p"]["V05"]
    out = set()
    if st == "silent":
        return {"silent"}
    if st != "value":
        return {"undec"} if st == "undec" else {"unparsed"}
    if D in vals and W in vals:
        out.add("D+W")
    elif D in vals:
        out.add("D-only")
    elif W in vals:
        out.add("W-only")
    if A in vals:
        out.add("AI")
    if not out:
        out.add("other")
    return out


# ---------------------------------------------------------------- printing


def wsum(rows, pop):
    return sum(r["w"] if pop in WEIGHTED else 1 for r in rows)


def fmt(n, base):
    if base < 10:
        return str(n)
    return "%d (%d%%)" % (n, round(100.0 * n / base)) if base else "0"


def table(title, rows, pop, var=None, derived=None):
    """var: a variable name; derived: (label list, function row -> set of labels)."""
    sel = [r for r in rows if r[pop]]
    groups = OrderedDict((b, [r for r in sel if b in buyer_of(r)]) for b in BUYERS)
    bases = OrderedDict((b, wsum(g, pop)) for b, g in groups.items())
    if derived:
        labels, fn = derived
    else:
        labels = VALUES[var]
        fn = None
    print("\n### %s, %s" % (title, POP_LABEL.get(pop, pop)))
    print("| value | " + " | ".join("%s (%d)" % (b, bases[b]) for b in BUYERS) + " |")
    print("|---|" + "---|" * len(BUYERS))

    def count(g, pred):
        return sum(r["w"] if pop in WEIGHTED else 1 for r in g if pred(r))

    for lab in labels:
        if fn:
            pred = (lambda L: lambda r: L in fn(r))(lab)
        else:
            pred = (lambda L: lambda r: L in r["p"][var][0])(lab)
        cells = [fmt(count(groups[b], pred), bases[b]) for b in BUYERS]
        if all(x.split()[0] == "0" for x in cells):
            continue
        print("| %s | %s |" % (lab, " | ".join(cells)))
    if not fn:
        for st, lab in (("undec", "undecidable, no value coded"), ("silent", "silent"),
                        ("unparsed", "unparsed")):
            pred = (lambda S: lambda r: r["p"][var][1] == S)(st)
            cells = [fmt(count(groups[b], pred), bases[b]) for b in BUYERS]
            if st == "unparsed" and all(x.split()[0] == "0" for x in cells):
                continue
            print("| %s | %s |" % (lab, " | ".join(cells)))


POP_LABEL = {"SHAPE": "SHAPE", "ALL": "ALL (weighted)",
             "MAS": "within the Mac App Store cell", "MAS-free": "within MAS-free",
             "AT": "within the AlternativeTo cells (weighted)",
             "not-MAS": "ALL rows outside the Mac App Store cell (weighted)"}

# The compact view: (population, buyer column) pairs set side by side for each value.
COMPACT = [("SHAPE", "D+W"), ("SHAPE", "silent"), ("MAS-free", "D+W"), ("MAS-free", "silent"),
           ("MAS", "D+W"), ("MAS", "silent"), ("not-MAS", "D+W"), ("not-MAS", "silent"),
           ("ALL", "D-only"), ("ALL", "W-only"), ("ALL", "D+W"), ("ALL", "AI"),
           ("ALL", "other"), ("ALL", "silent"),
           ("AT", "D-only"), ("AT", "W-only"), ("AT", "D+W"), ("AT", "other"), ("AT", "silent")]

def compact(var, rows, derived=None):
    """One line per value: count/base for each (population, buyer) pair in COMPACT."""
    labels, fn = derived if derived else (VALUES[var] + ["<silent>"], None)

    def has(r, lab):
        if fn:
            return lab in fn(r)
        if lab == "<silent>":
            return r["p"][var][1] == "silent"
        return lab in r["p"][var][0]

    heads = ["%s %s" % (POP_SHORT[p], b) for p, b in COMPACT]
    print("\n#### %s" % var)
    print("| value | " + " | ".join(heads) + " |")
    print("|---|" + "---|" * len(COMPACT))
    for lab in labels:
        cells = []
        for p, b in COMPACT:
            g = [r for r in rows if r[p] and b in buyer_of(r)]
            n = wsum([r for r in g if has(r, lab)], p)
            cells.append("%d/%d" % (n, wsum(g, p)))
        if all(c.startswith("0/") for c in cells):
            continue
        print("| %s | %s |" % (lab, " | ".join(cells)))


POP_SHORT = {"SHAPE": "SH", "MAS-free": "MASf", "MAS": "MAS", "not-MAS": "nonMAS",
             "ALL": "ALL", "AT": "AT"}

PARAMS = [
    ("1 Name", ["V03"]),
    ("2 Where", ["V20", "V22"]),
    ("3 Unit and install", ["V19", "V12a", "V12b"]),
    ("4 Cost", ["PRICE", "V16b", "V23", "V24", "V07"]),
    ("5 Work and source", ["V16c", "V18"]),
    ("6 Platforms and prerequisites", ["V10", "V11"]),
    ("7 Forms", ["V13a", "V13b"]),
    ("8 Write or read", ["V09"]),
    ("9 Keeping up", ["V31"]),
    ("10 Long document", ["V28"]),
    ("11 Finding a word", ["V29"]),
    ("12 Network", ["V14", "V15"]),
    ("13 Appearance", ["V32"]),
    ("14 Print and export", ["V33"]),
    ("15 One thing or several", ["V04"]),
]


def check(rows):
    for var in VALUES:
        tot = defaultdict(int)
        for r in rows:
            vals, st = r["p"][var]
            for v in vals:
                tot[v] += r["w"]
            if st != "value":
                tot["<" + st + ">"] += r["w"]
        print(var, dict(tot))


def main():
    rows = load()
    if "--check" in sys.argv:
        print("ALL rows", len(rows), "weighted", wsum(rows, "ALL"),
              "SHAPE", sum(r["SHAPE"] for r in rows),
              "STORE-NS", sum(r["STORE-NS"] for r in rows))
        check(rows)
        return
    # populations
    print("# Findings by buyer: the tables")
    for pop in ("SHAPE", "ALL", "STORE-NS", "MAS", "MAS-free", "not-MAS", "AT"):
        sel = [r for r in rows if r[pop]]
        print("- %s: %d rows, counted %d" % (pop, len(sel), wsum(sel, pop)))
    print("\nBuyer columns: D-only names developers and not writers; W-only names writers"
          " and not developers; D+W names both; AI names readers of AI-agent output (it"
          " may also sit in one of the first three); other names a class but none of"
          " those; silent is V05 not stated, each row once; undec is V05 undecidable only.")

    # co-occurrence of developers and writers
    print("\n## Developers and writers on V05")
    print("| population | both | developers only | writers only | neither, a class named |"
          " silent | undecidable only | total |")
    print("|---|---|---|---|---|---|---|---|")
    for pop in ("SHAPE", "ALL"):
        sel = [r for r in rows if r[pop]]
        def c(pred):
            return wsum([r for r in sel if pred(r)], pop)
        def has(r, x):
            return x in r["p"]["V05"][0]
        print("| %s | %d | %d | %d | %d | %d | %d | %d |" % (
            pop, c(lambda r: has(r, D) and has(r, W)), c(lambda r: has(r, D) and not has(r, W)),
            c(lambda r: has(r, W) and not has(r, D)),
            c(lambda r: r["p"]["V05"][1] == "value" and not has(r, D) and not has(r, W)),
            c(lambda r: r["p"]["V05"][1] == "silent"), c(lambda r: r["p"]["V05"][1] == "undec"),
            wsum(sel, pop)))

    # overlap of AI readers with the developer and writer columns
    print("\n## Readers of AI-agent output: rows also naming developers or writers")
    for pop in ("SHAPE", "ALL"):
        sel = [r for r in rows if r[pop] and A in r["p"]["V05"][0]]
        print("%s: %d AI rows; with D-only %d, W-only %d, D+W %d; slugs: %s" % (
            pop, wsum(sel, pop),
            wsum([r for r in sel if "D-only" in buyer_of(r)], pop),
            wsum([r for r in sel if "W-only" in buyer_of(r)], pop),
            wsum([r for r in sel if "D+W" in buyer_of(r)], pop),
            ", ".join(sorted(r["slug"] for r in sel))))

    # buyer by cell
    print("\n## Buyer columns by cell (rows; AlternativeTo cells weighted)")
    codes = list(CELL_CODE.values())
    print("| buyer | " + " | ".join(codes) + " | SHAPE | STORE-NS | ALL |")
    print("|---|" + "---|" * (len(codes) + 3))
    for b in BUYERS:
        g = [r for r in rows if b in buyer_of(r)]
        cells = []
        for code in codes:
            cells.append(str(sum(r["w"] for r in g if code in r["cells"])))
        print("| %s | %s | %d | %d | %d |" % (
            b, " | ".join(cells), wsum([r for r in g if r["SHAPE"]], "SHAPE"),
            wsum([r for r in g if r["STORE-NS"]], "STORE-NS"), wsum(g, "ALL")))
    # SHAPE by its two parts
    print("\n## Buyer columns in SHAPE, by its two parts (GitHub-topic rows; store-only rows)")
    print("| buyer | SHAPE | GitHub-topic | store-only | of which MAS-free |")
    print("|---|---|---|---|---|")
    for b in BUYERS:
        g = [r for r in rows if r["SHAPE"] and b in buyer_of(r)]
        ghn = len([r for r in g if set(r["cells"]) & GH])
        print("| %s | %d | %d | %d | %d |" % (b, len(g), ghn, len(g) - ghn,
                                              len([r for r in g if "MAS" in r["cells"]])))

    # the named rows in SHAPE for the small buyer columns
    print("\n## Rows in SHAPE per buyer column")
    for b in ("D-only", "W-only", "D+W", "AI"):
        g = sorted(r["slug"] + "[" + ",".join(r["cells"]) + "]"
                   for r in rows if r["SHAPE"] and b in buyer_of(r))
        print("- %s (%d): %s" % (b, len(g), "; ".join(g)))

    # reconciliation with finding 2 (taxonomy V05), which read a single '|' as text
    print("\n## V05 class totals in ALL (weighted): this reading against finding 2's")
    print("| class | this reading | single '|' not a separator | rows that differ |")
    print("|---|---|---|---|")
    for cls in VALUES["V05"]:
        new = [r for r in rows if cls in r["p"]["V05"][0]]
        old = [r for r in rows if cls in r["V05-old"][0]]
        diff = sorted(set(r["slug"] for r in new) ^ set(r["slug"] for r in old))
        print("| %s | %d | %d | %s |" % (cls, wsum(new, "ALL"), wsum(old, "ALL"),
                                        ", ".join(diff) or "none"))
    changed = [r for r in rows if r["p"]["V05"][0] != r["V05-old"][0]
               and buyer_of(r) != buyer_of(dict(r, p=dict(r["p"], V05=r["V05-old"])))]
    print("Rows whose buyer column changes between the two readings: %s" % (
        ", ".join(sorted(r["slug"] for r in changed)) or "none"))

    # products behind each weighted base
    print("\n## Products (unweighted rows) behind each buyer column")
    print("| buyer | ALL rows | ALL weighted | AT rows | AT weighted | MAS rows |")
    print("|---|---|---|---|---|---|")
    for b in BUYERS:
        g = [r for r in rows if b in buyer_of(r)]
        at = [r for r in g if r["AT"]]
        print("| %s | %d | %d | %d | %d | %d |" % (b, len(g), wsum(g, "ALL"), len(at),
                                                wsum(at, "AT"), len([r for r in g if r["MAS"]])))

    # the parameter tables
    def price_fn(r):
        return {r["price"]}
    print("\nEach variable is given in SHAPE and ALL, then within strata that separate a"
          " buyer from a cell: MAS-free (SHAPE's Mac App Store rows), MAS (the Mac App"
          " Store cell), not-MAS (ALL outside it, weighted) and AT (any AlternativeTo"
          " cell, weighted). A rate on a base under 10 is given as a count.")
    for title, vars_ in PARAMS:
        print("\n## Parameter %s" % title)
        for var in vars_:
            for pop in ("SHAPE", "ALL", "MAS-free", "MAS", "not-MAS", "AT"):
                if var == "PRICE":
                    table("price status (finding 7 rule)", rows, pop,
                          derived=(["free", "paid", "silent"], price_fn))
                else:
                    table(var, rows, pop, var=var)

    print("\n## Compact view: count/base per (population, buyer column)")
    print("SH = SHAPE, MASf = MAS-free, nonMAS = ALL outside the Mac App Store cell;"
          " <silent> = the variable not stated.")
    for title, vars_ in PARAMS:
        for var in vars_:
            if var == "PRICE":
                compact("price status", rows, derived=(["free", "paid", "silent"], price_fn))
            else:
                compact(var, rows)


if __name__ == "__main__":
    main()
