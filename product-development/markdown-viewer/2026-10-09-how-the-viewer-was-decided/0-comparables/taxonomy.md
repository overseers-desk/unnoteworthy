---
title: "Taxonomy: every coded value, with its prevalence, by cell and overall"
date: 2026-10-09
method: "SAGE Survey section 1, step 7 (the activity taxonomy beside the numbered findings), under briefs/synthesis-clerk.md; read from 0-comparables/coded-corpus.tsv and the cell, drawn-by and weight columns of 0-comparables/frame/collection-list.tsv"
---

# Taxonomy of the coded comparables

This is the option set every card starts from, and the scarcity claims later are measured against exactly these tables. Findings that cite them are in `findings.md`.

**The standing caveat.** The corpus reads what products publish, and what is bought is not always printed; absence in the corpus is absence from publication, never absence from the market.

## How to read the tables

- **Coded comparables.** 449 rows were collected; 428 are eligible under V01 (table below), and only eligible rows carry values. 427 of them sit in at least one application cell; the 428th (shtmlview) sits only in the tcl-wiki cell, which is never pooled with application cells (frame review, forbidden comparison 9).
- **Weights.** The 69 eligible rows drawn by the AlternativeTo sampling rule carry weight 2 in every rate that includes them, so the pooled denominator is 496 for 427 rows, and each AlternativeTo cell's denominator counts sampled rows twice. No other cell has a weighted row.
- **Pooled columns.** ALL: every eligible row in an application cell, each counted once however many cells it sits in. SHAPE: the free sub-population that shares the operator's shape, as the shape note defines it: the GitHub-topic rows that state no payment (89) together with the free rows of the store and package cells (128), 13 rows in both, 204 in all. A row is free where V23 or V16(b) states a price and every stated value is free, free with a donation invited, or nothing paid before use; a row whose price is silent is not free. STORE-NS: the rows of the store and package cells (Flathub, Mac App Store, Snap, Ubuntu archive, Homebrew cask and formula, VS Code) that are not in SHAPE, 145. AlternativeTo-only rows are in ALL and in neither of the other two.
- **Cells.** FH Flathub (census of the search hits); MAS Mac App Store (census of 170 returned entries); SN Snap Store (the first 100 the search returns, ranking undisclosed); UA the Ubuntu 25.04 archive, apt-cache search markdown; HB-C and HB-F Homebrew casks and formulae; VS VS Code (head: the first 100 by installs); AT-T, AT-O, AT-M, AT-G the AlternativeTo lists anchored on Typora, Obsidian, Marked and Glow; GH-E, GH-V, GH-P, GH-R the GitHub topics markdown-editor, -viewer, -preview, -reader at 200 stars or more; ACC awesome-claude-code; TCL tcl-wiki-markdown with shtmlview's tklib membership. MAS-free and MAS-paid split the Mac App Store cell by the definitions above (52 and 82; none is silent on price). MAS-mac is the 43 Mac App Store rows whose V10 names macOS and names neither iOS nor iPadOS: a coded stand-in for the Mac-only listings, not the store's own device field, which this clerk did not open.
- **Entries.** Pooled columns give weighted count and percentage; cell columns give the count, and the fraction is that count over the denominator in the column header. GH-P, GH-R, ACC and TCL are too small for a rate: read their counts only. A multi-valued variable's values do not sum to the denominator. "Undecidable, no value coded" counts rows whose cell holds only an undecidable; a row with a coded value and an undecidable on a further point counts under its value.
- **Silent.** The line under each table counts the comparables that coded "not stated" on the variable, each counted once.
- **Comparisons the frame review forbids** are not made here or in the findings: store cells set against the operator on dimensions 1 to 3 without the mark; paid share across cells; popularity across cells; VS and SN against any census cell; GitHub-topic cells against store cells on age, activity, maintenance or recency; SN against FH; one AlternativeTo list against another, or an AlternativeTo list against a store on platform or price; one platform against another through the cell; the tcl-wiki cell with any application cell; any cell's count read as the number of markdown applications on its platform.
- **Parsing.** A cell's value is the text before its first bracket, brace, guillemet, "::", "@" or colon-and-space, read element by element (elements separated by semicolons or "||" outside quotes), with sub-fields split at "(a)", "(b)", "(c)"; each value is then matched to the codebook's value list. Clerks wrote cells in several layouts (bare values, values with single-letter tags such as "(p)", "a:" sub-field labels), and some cells carry shell-quoting debris (`'"'"'` for an apostrophe), which was cleaned before matching.

## V01 Eligibility

| value | rows |
|---|---|
| eligible | 428 |
| ineligible: markdown not handled | 13 |
| ineligible: no captured text | 2 |
| ineligible: not a product | 0 |
| undecidable | 6 |
| all collected | 449 |

The 6 undecidable rows (ia-presenter, kookbook, logseq, ufocus, wonderpen, writed) carry no values in any table below. Of the 21 rows not eligible, 5 are tcl-wiki components (caius, cmark, tclhoedown, tclsundown, tcllib-markdown-module: 5 of the cell's 6 rows), and 5 are sampled AlternativeTo rows.

## V03 Name form (multi)

| value | ALL (496) | SHAPE (204) | STORE-NS (145) | FH (25) | MAS (134) | SN (48) | UA (13) | HB-C (44) | HB-F (17) | VS (19) | AT-T (132) | AT-O (87) | AT-M (63) | AT-G (40) | GH-E (84) | GH-V (21) | GH-P (5) | GH-R (5) | ACC (2) | TCL (1) | MAS-free (52) | MAS-paid (82) | MAS-mac (43) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| markdown token in name | 216 (44%) | 85 (42%) | 89 (61%) | 0 | 118 | 13 | 2 | 5 | 3 | 10 | 36 | 23 | 22 | 11 | 25 | 8 | 2 | 1 | 0 | 0 | 44 | 74 | 40 |
| function word in name | 218 (44%) | 83 (41%) | 70 (48%) | 4 | 94 | 15 | 0 | 11 | 1 | 9 | 46 | 43 | 21 | 11 | 26 | 4 | 2 | 2 | 0 | 0 | 35 | 59 | 23 |
| maker name in title | 7 (1%) | 4 (2%) | 3 (2%) | 0 | 2 | 0 | 0 | 2 | 0 | 0 | 1 | 0 | 0 | 0 | 3 | 2 | 0 | 0 | 0 | 0 | 0 | 2 | 0 |
| none of the above | 194 (39%) | 83 (41%) | 45 (31%) | 20 | 5 | 28 | 11 | 29 | 14 | 5 | 70 | 34 | 34 | 25 | 43 | 11 | 2 | 2 | 2 | 1 | 3 | 2 | 2 |
| undecidable, no value coded | 7 (1%) | 3 (1%) | 0 (0%) | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 3 | 2 | 0 | 0 | 2 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |

Silent (not stated), each comparable counted once: ALL 0; SHAPE 0; STORE-NS 0; FH 0; MAS 0; SN 0; UA 0; HB-C 0; HB-F 0; VS 0; AT-T 0; AT-O 0; AT-M 0; AT-G 0; GH-E 0; GH-V 0; GH-P 0; GH-R 0; ACC 0; TCL 0; MAS-free 0; MAS-paid 0; MAS-mac 0.

## V04 One thing or several (single)

| value | ALL (496) | SHAPE (204) | STORE-NS (145) | FH (25) | MAS (134) | SN (48) | UA (13) | HB-C (44) | HB-F (17) | VS (19) | AT-T (132) | AT-O (87) | AT-M (63) | AT-G (40) | GH-E (84) | GH-V (21) | GH-P (5) | GH-R (5) | ACC (2) | TCL (1) | MAS-free (52) | MAS-paid (82) | MAS-mac (43) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| single program | 314 (63%) | 162 (79%) | 70 (48%) | 18 | 69 | 39 | 13 | 28 | 12 | 16 | 92 | 47 | 44 | 26 | 64 | 16 | 3 | 3 | 1 | 0 | 43 | 26 | 27 |
| one program in editions | 100 (20%) | 9 (4%) | 50 (34%) | 1 | 42 | 2 | 0 | 10 | 0 | 0 | 24 | 27 | 12 | 8 | 10 | 2 | 0 | 1 | 0 | 0 | 0 | 42 | 8 |
| program and component | 7 (1%) | 2 (1%) | 3 (2%) | 0 | 2 | 0 | 0 | 0 | 2 | 0 | 3 | 0 | 2 | 2 | 1 | 1 | 0 | 0 | 0 | 1 | 1 | 1 | 0 |
| family of programs | 40 (8%) | 18 (9%) | 13 (9%) | 5 | 14 | 6 | 0 | 2 | 0 | 3 | 7 | 7 | 0 | 0 | 5 | 0 | 0 | 0 | 1 | 0 | 5 | 9 | 5 |
| component only | 0 (0%) | 0 (0%) | 0 (0%) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| undecidable, no value coded | 36 (7%) | 14 (7%) | 9 (6%) | 1 | 8 | 1 | 0 | 4 | 3 | 0 | 6 | 6 | 5 | 4 | 4 | 2 | 2 | 1 | 0 | 0 | 4 | 4 | 3 |

Silent (not stated), each comparable counted once: ALL 0; SHAPE 0; STORE-NS 0; FH 0; MAS 0; SN 0; UA 0; HB-C 0; HB-F 0; VS 0; AT-T 0; AT-O 0; AT-M 0; AT-G 0; GH-E 0; GH-V 0; GH-P 0; GH-R 0; ACC 0; TCL 0; MAS-free 0; MAS-paid 0; MAS-mac 0.

Weakest variable of the second coding (9 cells the rule cannot decide, adjusted agreement 0.80): a bundled companion has no value, so the first coding recorded undecidable.

## V05 Whom the product sells to (multi)

| value | ALL (496) | SHAPE (204) | STORE-NS (145) | FH (25) | MAS (134) | SN (48) | UA (13) | HB-C (44) | HB-F (17) | VS (19) | AT-T (132) | AT-O (87) | AT-M (63) | AT-G (40) | GH-E (84) | GH-V (21) | GH-P (5) | GH-R (5) | ACC (2) | TCL (1) | MAS-free (52) | MAS-paid (82) | MAS-mac (43) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Writers and authors | 71 (14%) | 23 (11%) | 20 (14%) | 2 | 31 | 2 | 1 | 5 | 0 | 0 | 28 | 11 | 8 | 4 | 6 | 3 | 2 | 2 | 0 | 0 | 13 | 18 | 14 |
| Bloggers and platform publishers | 12 (2%) | 6 (3%) | 1 (1%) | 0 | 4 | 0 | 0 | 1 | 0 | 0 | 5 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 3 | 1 | 2 |
| Students and academics | 42 (8%) | 19 (9%) | 12 (8%) | 3 | 19 | 0 | 0 | 5 | 0 | 0 | 8 | 9 | 2 | 1 | 3 | 2 | 1 | 1 | 0 | 0 | 8 | 11 | 11 |
| Developers and coders | 64 (13%) | 28 (14%) | 18 (12%) | 3 | 29 | 5 | 1 | 6 | 1 | 1 | 18 | 6 | 2 | 1 | 7 | 3 | 2 | 2 | 1 | 1 | 15 | 14 | 14 |
| Note-takers and personal knowledge managers | 13 (3%) | 6 (3%) | 1 (1%) | 1 | 4 | 0 | 0 | 0 | 0 | 0 | 3 | 6 | 2 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 3 | 1 | 1 |
| Teams, businesses and organisations | 40 (8%) | 9 (4%) | 8 (6%) | 0 | 6 | 0 | 0 | 7 | 0 | 0 | 13 | 13 | 2 | 0 | 8 | 0 | 0 | 1 | 1 | 0 | 3 | 3 | 3 |
| Terminal readers | 2 (0%) | 1 (0%) | 1 (1%) | 0 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| Plain readers of received markdown files | 4 (1%) | 3 (1%) | 1 (1%) | 0 | 3 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 |
| Readers of what AI agents write | 12 (2%) | 4 (2%) | 8 (6%) | 1 | 6 | 3 | 0 | 3 | 1 | 0 | 2 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 4 | 0 |
| Application developers embedding a markdown view | 0 (0%) | 0 (0%) | 0 (0%) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| undecidable, no value coded | 3 (1%) | 1 (0%) | 2 (1%) | 0 | 2 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 |

Silent (not stated), each comparable counted once: ALL 348; SHAPE 150; STORE-NS 106; FH 19; MAS 86; SN 41; UA 12; HB-C 28; HB-F 14; VS 18; AT-T 91; AT-O 55; AT-M 52; AT-G 35; GH-E 63; GH-V 16; GH-P 3; GH-R 3; ACC 1; TCL 0; MAS-free 31; MAS-paid 55; MAS-mac 25.

No class is coded from a feature (codebook V05). The tcl-wiki row (shtmlview) is a component cell and is never pooled; it is shown, not added. Silent is the larger half of every column.

## V07 What the page asks the buyer to do (multi)

| value | ALL (496) | SHAPE (204) | STORE-NS (145) | FH (25) | MAS (134) | SN (48) | UA (13) | HB-C (44) | HB-F (17) | VS (19) | AT-T (132) | AT-O (87) | AT-M (63) | AT-G (40) | GH-E (84) | GH-V (21) | GH-P (5) | GH-R (5) | ACC (2) | TCL (1) | MAS-free (52) | MAS-paid (82) | MAS-mac (43) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| pay or buy | 86 (17%) | 1 (0%) | 55 (38%) | 1 | 47 | 1 | 0 | 10 | 0 | 0 | 35 | 8 | 18 | 9 | 2 | 0 | 0 | 0 | 0 | 0 | 1 | 46 | 14 |
| subscribe | 30 (6%) | 0 (0%) | 18 (12%) | 1 | 16 | 1 | 0 | 0 | 0 | 0 | 9 | 7 | 3 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 16 | 1 |
| download a file | 232 (47%) | 96 (47%) | 49 (34%) | 16 | 29 | 30 | 3 | 38 | 6 | 2 | 82 | 58 | 33 | 19 | 52 | 12 | 3 | 4 | 1 | 1 | 13 | 16 | 11 |
| install from a store | 151 (30%) | 73 (36%) | 41 (28%) | 22 | 55 | 16 | 4 | 7 | 0 | 13 | 47 | 27 | 14 | 8 | 13 | 3 | 1 | 2 | 0 | 0 | 22 | 33 | 21 |
| install by a package-manager command | 161 (32%) | 72 (35%) | 57 (39%) | 15 | 3 | 48 | 9 | 42 | 16 | 2 | 46 | 21 | 26 | 13 | 32 | 10 | 2 | 2 | 1 | 0 | 1 | 2 | 1 |
| clone or build from source | 105 (21%) | 71 (35%) | 13 (9%) | 13 | 4 | 16 | 6 | 5 | 9 | 2 | 23 | 14 | 11 | 7 | 43 | 13 | 4 | 4 | 1 | 0 | 4 | 0 | 0 |
| open in a browser | 48 (10%) | 21 (10%) | 8 (6%) | 0 | 7 | 3 | 0 | 4 | 0 | 0 | 18 | 5 | 8 | 6 | 17 | 2 | 1 | 0 | 0 | 0 | 2 | 5 | 1 |
| add as a dependency | 1 (0%) | 1 (0%) | 0 (0%) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| create an account or sign in | 23 (5%) | 4 (2%) | 3 (2%) | 0 | 3 | 1 | 0 | 0 | 0 | 0 | 7 | 14 | 2 | 2 | 3 | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 0 |
| contact sales or request a quote | 6 (1%) | 0 (0%) | 1 (1%) | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 3 | 1 | 0 | 3 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |
| star, follow or watch | 26 (5%) | 17 (8%) | 2 (1%) | 0 | 1 | 4 | 0 | 4 | 1 | 1 | 4 | 4 | 1 | 1 | 12 | 2 | 1 | 1 | 0 | 0 | 0 | 1 | 0 |
| sponsor or donate | 67 (14%) | 44 (22%) | 4 (3%) | 13 | 5 | 6 | 3 | 9 | 0 | 4 | 24 | 15 | 5 | 3 | 20 | 3 | 1 | 1 | 0 | 0 | 3 | 2 | 2 |
| undecidable, no value coded | 6 (1%) | 6 (3%) | 0 (0%) | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |

Silent (not stated), each comparable counted once: ALL 66; SHAPE 29; STORE-NS 25; FH 0; MAS 42; SN 0; UA 3; HB-C 0; HB-F 1; VS 3; AT-T 11; AT-O 6; AT-M 9; AT-G 8; GH-E 5; GH-V 1; GH-P 0; GH-R 0; ACC 0; TCL 0; MAS-free 21; MAS-paid 21; MAS-mac 16.

## V08 Product kind (multi)

| value | ALL (496) | SHAPE (204) | STORE-NS (145) | FH (25) | MAS (134) | SN (48) | UA (13) | HB-C (44) | HB-F (17) | VS (19) | AT-T (132) | AT-O (87) | AT-M (63) | AT-G (40) | GH-E (84) | GH-V (21) | GH-P (5) | GH-R (5) | ACC (2) | TCL (1) | MAS-free (52) | MAS-paid (82) | MAS-mac (43) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| desktop application | 364 (73%) | 139 (68%) | 116 (80%) | 25 | 126 | 42 | 6 | 42 | 0 | 0 | 107 | 67 | 47 | 26 | 52 | 10 | 4 | 3 | 2 | 0 | 49 | 77 | 42 |
| browser extension | 14 (3%) | 2 (1%) | 6 (4%) | 1 | 4 | 1 | 0 | 0 | 0 | 0 | 7 | 3 | 2 | 2 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 4 | 0 |
| editor extension | 32 (6%) | 27 (13%) | 3 (2%) | 0 | 0 | 0 | 2 | 0 | 0 | 18 | 2 | 2 | 2 | 0 | 7 | 3 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| terminal program | 41 (8%) | 18 (9%) | 19 (13%) | 3 | 4 | 6 | 4 | 3 | 15 | 1 | 4 | 5 | 2 | 0 | 5 | 6 | 0 | 0 | 0 | 0 | 2 | 2 | 1 |
| mobile application | 103 (21%) | 36 (18%) | 54 (37%) | 5 | 69 | 5 | 0 | 6 | 0 | 0 | 10 | 19 | 3 | 2 | 9 | 1 | 1 | 0 | 1 | 0 | 23 | 46 | 0 |
| component | 8 (2%) | 3 (1%) | 3 (2%) | 0 | 2 | 0 | 0 | 0 | 3 | 0 | 3 | 0 | 3 | 2 | 1 | 1 | 0 | 0 | 0 | 1 | 1 | 1 | 0 |
| service | 68 (14%) | 23 (11%) | 9 (6%) | 1 | 7 | 4 | 0 | 3 | 0 | 0 | 28 | 17 | 14 | 12 | 17 | 2 | 1 | 0 | 0 | 0 | 2 | 5 | 1 |
| other kind | 28 (6%) | 7 (3%) | 12 (8%) | 1 | 9 | 0 | 1 | 5 | 1 | 0 | 10 | 0 | 7 | 6 | 2 | 1 | 0 | 0 | 0 | 0 | 2 | 7 | 6 |
| undecidable, no value coded | 5 (1%) | 4 (2%) | 1 (1%) | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |

Silent (not stated), each comparable counted once: ALL 9; SHAPE 6; STORE-NS 1; FH 0; MAS 0; SN 1; UA 0; HB-C 0; HB-F 0; VS 0; AT-T 0; AT-O 0; AT-M 2; AT-G 2; GH-E 6; GH-V 1; GH-P 0; GH-R 0; ACC 0; TCL 0; MAS-free 0; MAS-paid 0; MAS-mac 0.

## V09 Reader only, or also editor (single)

| value | ALL (496) | SHAPE (204) | STORE-NS (145) | FH (25) | MAS (134) | SN (48) | UA (13) | HB-C (44) | HB-F (17) | VS (19) | AT-T (132) | AT-O (87) | AT-M (63) | AT-G (40) | GH-E (84) | GH-V (21) | GH-P (5) | GH-R (5) | ACC (2) | TCL (1) | MAS-free (52) | MAS-paid (82) | MAS-mac (43) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| reader, stated read-only | 22 (4%) | 7 (3%) | 12 (8%) | 0 | 16 | 2 | 0 | 2 | 0 | 0 | 5 | 0 | 2 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 6 | 10 | 4 |
| reader, editing not stated | 66 (13%) | 30 (15%) | 33 (23%) | 1 | 15 | 9 | 7 | 4 | 15 | 8 | 1 | 0 | 4 | 0 | 2 | 6 | 1 | 2 | 0 | 0 | 8 | 7 | 9 |
| editor with rendered view | 305 (61%) | 137 (67%) | 76 (52%) | 20 | 84 | 32 | 5 | 27 | 1 | 8 | 90 | 54 | 43 | 25 | 68 | 14 | 4 | 3 | 1 | 1 | 31 | 53 | 24 |
| editor, rendered view not stated | 93 (19%) | 26 (13%) | 22 (15%) | 4 | 15 | 5 | 1 | 9 | 1 | 3 | 32 | 31 | 10 | 10 | 14 | 0 | 0 | 0 | 0 | 0 | 4 | 11 | 4 |
| undecidable, no value coded | 6 (1%) | 3 (1%) | 1 (1%) | 0 | 3 | 0 | 0 | 1 | 0 | 0 | 2 | 0 | 2 | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 2 | 1 | 2 |

Silent (not stated), each comparable counted once: ALL 4; SHAPE 1; STORE-NS 1; FH 0; MAS 1; SN 0; UA 0; HB-C 1; HB-F 0; VS 0; AT-T 2; AT-O 2; AT-M 2; AT-G 2; GH-E 0; GH-V 0; GH-P 0; GH-R 0; ACC 0; TCL 0; MAS-free 1; MAS-paid 0; MAS-mac 0.

## V10 Platforms (multi)

| value | ALL (496) | SHAPE (204) | STORE-NS (145) | FH (25) | MAS (134) | SN (48) | UA (13) | HB-C (44) | HB-F (17) | VS (19) | AT-T (132) | AT-O (87) | AT-M (63) | AT-G (40) | GH-E (84) | GH-V (21) | GH-P (5) | GH-R (5) | ACC (2) | TCL (1) | MAS-free (52) | MAS-paid (82) | MAS-mac (43) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Windows | 174 (35%) | 70 (34%) | 26 (18%) | 12 | 6 | 31 | 4 | 20 | 5 | 3 | 62 | 47 | 26 | 14 | 39 | 10 | 4 | 3 | 1 | 0 | 2 | 4 | 2 |
| macOS | 341 (69%) | 120 (59%) | 123 (85%) | 13 | 131 | 22 | 6 | 44 | 16 | 1 | 90 | 63 | 49 | 27 | 42 | 9 | 3 | 2 | 1 | 0 | 50 | 81 | 43 |
| Linux | 186 (38%) | 81 (40%) | 50 (34%) | 25 | 5 | 47 | 11 | 20 | 17 | 2 | 58 | 35 | 27 | 14 | 36 | 7 | 2 | 2 | 2 | 0 | 1 | 4 | 1 |
| BSD | 13 (3%) | 7 (3%) | 4 (3%) | 3 | 0 | 4 | 4 | 1 | 5 | 0 | 3 | 1 | 4 | 1 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| iOS | 113 (23%) | 35 (17%) | 65 (45%) | 2 | 89 | 3 | 0 | 5 | 0 | 0 | 11 | 16 | 5 | 4 | 4 | 1 | 1 | 0 | 1 | 0 | 30 | 59 | 0 |
| iPadOS | 91 (18%) | 27 (13%) | 58 (40%) | 0 | 82 | 1 | 0 | 3 | 0 | 0 | 4 | 8 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 26 | 56 | 0 |
| Android | 40 (8%) | 13 (6%) | 14 (10%) | 3 | 8 | 5 | 0 | 3 | 1 | 0 | 7 | 15 | 0 | 0 | 10 | 2 | 1 | 0 | 1 | 0 | 1 | 7 | 0 |
| ChromeOS | 4 (1%) | 1 (0%) | 1 (1%) | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 2 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| any desktop with a web browser | 1 (0%) | 0 (0%) | 1 (1%) | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| inside a host program | 41 (8%) | 29 (14%) | 6 (4%) | 2 | 2 | 0 | 2 | 0 | 0 | 17 | 6 | 1 | 2 | 2 | 8 | 4 | 1 | 1 | 0 | 0 | 0 | 2 | 0 |
| undecidable, no value coded | 6 (1%) | 0 (0%) | 0 (0%) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

Silent (not stated), each comparable counted once: ALL 35; SHAPE 17; STORE-NS 0; FH 0; MAS 0; SN 0; UA 0; HB-C 0; HB-F 0; VS 0; AT-T 14; AT-O 10; AT-M 9; AT-G 9; GH-E 15; GH-V 5; GH-P 1; GH-R 1; ACC 0; TCL 1; MAS-free 0; MAS-paid 0; MAS-mac 0.

Platform is the list in most store cells (frame review, forbidden comparison 8): read MAS, FH, SN, UA and the Homebrew cells as what each list holds, never as one platform against another.

## V11 Prerequisites (multi)

| value | ALL (496) | SHAPE (204) | STORE-NS (145) | FH (25) | MAS (134) | SN (48) | UA (13) | HB-C (44) | HB-F (17) | VS (19) | AT-T (132) | AT-O (87) | AT-M (63) | AT-G (40) | GH-E (84) | GH-V (21) | GH-P (5) | GH-R (5) | ACC (2) | TCL (1) | MAS-free (52) | MAS-paid (82) | MAS-mac (43) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none needed, stated | 13 (3%) | 7 (3%) | 2 (1%) | 0 | 2 | 2 | 0 | 0 | 1 | 0 | 6 | 0 | 1 | 1 | 3 | 2 | 2 | 2 | 0 | 0 | 1 | 1 | 0 |
| runtime or interpreter named | 73 (15%) | 38 (19%) | 15 (10%) | 5 | 1 | 9 | 8 | 6 | 5 | 1 | 20 | 17 | 7 | 6 | 25 | 8 | 3 | 2 | 2 | 1 | 1 | 0 | 0 |
| host program named | 47 (9%) | 32 (16%) | 7 (5%) | 1 | 3 | 0 | 2 | 1 | 0 | 19 | 8 | 0 | 4 | 4 | 9 | 5 | 1 | 1 | 0 | 0 | 0 | 3 | 1 |
| package manager named as required to install | 14 (3%) | 10 (5%) | 4 (3%) | 0 | 1 | 4 | 0 | 0 | 0 | 0 | 2 | 1 | 2 | 1 | 9 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 0 |
| build toolchain named | 50 (10%) | 34 (17%) | 10 (7%) | 10 | 3 | 14 | 3 | 3 | 6 | 0 | 12 | 6 | 8 | 3 | 14 | 6 | 2 | 2 | 0 | 0 | 3 | 0 | 0 |
| minimum operating-system version named | 224 (45%) | 85 (42%) | 97 (67%) | 3 | 134 | 14 | 0 | 27 | 0 | 0 | 47 | 20 | 24 | 10 | 19 | 3 | 1 | 1 | 1 | 0 | 52 | 82 | 43 |
| undecidable, no value coded | 12 (2%) | 7 (3%) | 5 (3%) | 0 | 0 | 2 | 1 | 3 | 4 | 0 | 2 | 0 | 2 | 2 | 4 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

Silent (not stated), each comparable counted once: ALL 133; SHAPE 35; STORE-NS 18; FH 10; MAS 0; SN 20; UA 2; HB-C 8; HB-F 2; VS 0; AT-T 52; AT-O 50; AT-M 24; AT-G 16; GH-E 23; GH-V 4; GH-P 0; GH-R 1; ACC 0; TCL 0; MAS-free 0; MAS-paid 0; MAS-mac 0.

## V12(a) Install method (multi)

| value | ALL (496) | SHAPE (204) | STORE-NS (145) | FH (25) | MAS (134) | SN (48) | UA (13) | HB-C (44) | HB-F (17) | VS (19) | AT-T (132) | AT-O (87) | AT-M (63) | AT-G (40) | GH-E (84) | GH-V (21) | GH-P (5) | GH-R (5) | ACC (2) | TCL (1) | MAS-free (52) | MAS-paid (82) | MAS-mac (43) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| run an installer or open a package file | 105 (21%) | 46 (23%) | 15 (10%) | 4 | 6 | 17 | 0 | 13 | 2 | 1 | 36 | 25 | 16 | 5 | 29 | 4 | 1 | 2 | 1 | 0 | 5 | 1 | 2 |
| store install | 130 (26%) | 56 (27%) | 39 (27%) | 21 | 48 | 17 | 4 | 8 | 0 | 1 | 45 | 27 | 14 | 9 | 12 | 3 | 1 | 2 | 0 | 0 | 19 | 29 | 22 |
| package-manager command | 165 (33%) | 73 (36%) | 60 (41%) | 17 | 3 | 48 | 9 | 44 | 16 | 1 | 49 | 24 | 26 | 13 | 33 | 10 | 2 | 2 | 1 | 0 | 1 | 2 | 1 |
| copy or unpack a binary | 64 (13%) | 31 (15%) | 14 (10%) | 3 | 2 | 14 | 1 | 8 | 6 | 0 | 20 | 13 | 9 | 3 | 17 | 6 | 3 | 2 | 0 | 0 | 1 | 1 | 1 |
| build or run from source | 115 (23%) | 76 (37%) | 13 (9%) | 15 | 4 | 18 | 6 | 6 | 9 | 2 | 27 | 17 | 13 | 9 | 45 | 13 | 4 | 5 | 2 | 1 | 4 | 0 | 0 |
| host program's extension manager | 22 (4%) | 19 (9%) | 1 (1%) | 0 | 1 | 0 | 1 | 0 | 0 | 13 | 2 | 0 | 0 | 0 | 3 | 2 | 0 | 0 | 0 | 0 | 1 | 0 | 1 |
| open a URL | 37 (7%) | 17 (8%) | 5 (3%) | 0 | 5 | 3 | 0 | 2 | 0 | 0 | 13 | 5 | 5 | 5 | 13 | 2 | 1 | 0 | 0 | 0 | 2 | 3 | 1 |
| undecidable, no value coded | 7 (1%) | 5 (2%) | 0 (0%) | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 2 | 0 | 0 | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |

Silent (not stated), each comparable counted once: ALL 142; SHAPE 36; STORE-NS 55; FH 0; MAS 80; SN 0; UA 3; HB-C 0; HB-F 1; VS 3; AT-T 30; AT-O 32; AT-M 16; AT-G 12; GH-E 5; GH-V 1; GH-P 0; GH-R 0; ACC 0; TCL 0; MAS-free 29; MAS-paid 51; MAS-mac 21.

5 cells the rule cannot decide in the second coding (adjusted agreement 0.78): no value for container or server deployment.

## V12(b) Update method (multi)

| value | ALL (496) | SHAPE (204) | STORE-NS (145) | FH (25) | MAS (134) | SN (48) | UA (13) | HB-C (44) | HB-F (17) | VS (19) | AT-T (132) | AT-O (87) | AT-M (63) | AT-G (40) | GH-E (84) | GH-V (21) | GH-P (5) | GH-R (5) | ACC (2) | TCL (1) | MAS-free (52) | MAS-paid (82) | MAS-mac (43) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| updates itself, stated | 58 (12%) | 25 (12%) | 14 (10%) | 1 | 6 | 8 | 0 | 21 | 1 | 0 | 14 | 19 | 8 | 2 | 11 | 5 | 1 | 1 | 0 | 0 | 4 | 2 | 3 |
| through the store | 20 (4%) | 9 (4%) | 3 (2%) | 1 | 4 | 5 | 0 | 1 | 0 | 0 | 6 | 7 | 0 | 0 | 2 | 1 | 1 | 1 | 0 | 0 | 4 | 0 | 2 |
| through the package manager | 21 (4%) | 5 (2%) | 4 (3%) | 0 | 0 | 5 | 0 | 1 | 2 | 0 | 7 | 8 | 5 | 0 | 3 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| download the new version by hand, stated | 14 (3%) | 4 (2%) | 5 (3%) | 1 | 1 | 4 | 0 | 0 | 1 | 0 | 1 | 5 | 0 | 0 | 2 | 2 | 1 | 1 | 1 | 0 | 0 | 1 | 0 |
| no updates planned, stated | 1 (0%) | 0 (0%) | 1 (1%) | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| undecidable, no value coded | 4 (1%) | 3 (1%) | 0 (0%) | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |

Silent (not stated), each comparable counted once: ALL 410; SHAPE 168; STORE-NS 124; FH 21; MAS 126; SN 33; UA 13; HB-C 21; HB-F 13; VS 19; AT-T 110; AT-O 60; AT-M 54; AT-G 38; GH-E 68; GH-V 13; GH-P 3; GH-R 3; ACC 0; TCL 1; MAS-free 46; MAS-paid 80; MAS-mac 39.

## V13(a) Markdown forms claimed (multi)

| value | ALL (496) | SHAPE (204) | STORE-NS (145) | FH (25) | MAS (134) | SN (48) | UA (13) | HB-C (44) | HB-F (17) | VS (19) | AT-T (132) | AT-O (87) | AT-M (63) | AT-G (40) | GH-E (84) | GH-V (21) | GH-P (5) | GH-R (5) | ACC (2) | TCL (1) | MAS-free (52) | MAS-paid (82) | MAS-mac (43) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CommonMark | 36 (7%) | 17 (8%) | 11 (8%) | 2 | 12 | 2 | 1 | 4 | 1 | 1 | 12 | 3 | 7 | 6 | 6 | 5 | 3 | 1 | 0 | 0 | 5 | 7 | 6 |
| GitHub Flavored Markdown | 109 (22%) | 46 (23%) | 41 (28%) | 2 | 36 | 10 | 2 | 12 | 2 | 2 | 30 | 5 | 20 | 13 | 26 | 8 | 3 | 1 | 0 | 0 | 11 | 25 | 13 |
| other named flavour | 41 (8%) | 21 (10%) | 15 (10%) | 4 | 11 | 7 | 1 | 7 | 0 | 4 | 11 | 2 | 8 | 9 | 9 | 3 | 0 | 0 | 0 | 0 | 1 | 10 | 7 |
| tables | 215 (43%) | 76 (37%) | 72 (50%) | 4 | 87 | 16 | 1 | 13 | 5 | 3 | 48 | 37 | 28 | 11 | 25 | 8 | 4 | 3 | 1 | 0 | 34 | 53 | 25 |
| task lists | 134 (27%) | 61 (30%) | 43 (30%) | 5 | 55 | 12 | 1 | 7 | 4 | 4 | 19 | 19 | 13 | 3 | 19 | 7 | 2 | 2 | 0 | 0 | 26 | 29 | 15 |
| footnotes | 66 (13%) | 30 (15%) | 27 (19%) | 0 | 26 | 8 | 0 | 8 | 2 | 1 | 10 | 2 | 6 | 6 | 13 | 6 | 1 | 2 | 0 | 0 | 8 | 18 | 4 |
| math | 182 (37%) | 86 (42%) | 48 (33%) | 8 | 45 | 19 | 3 | 18 | 2 | 4 | 52 | 30 | 24 | 13 | 48 | 15 | 5 | 4 | 0 | 0 | 12 | 33 | 13 |
| diagrams | 167 (34%) | 75 (37%) | 51 (35%) | 5 | 54 | 16 | 0 | 15 | 4 | 5 | 35 | 23 | 20 | 6 | 36 | 12 | 5 | 4 | 1 | 0 | 20 | 34 | 15 |
| syntax-highlighted code blocks | 134 (27%) | 59 (29%) | 45 (31%) | 4 | 49 | 11 | 0 | 11 | 7 | 0 | 26 | 15 | 13 | 3 | 29 | 12 | 3 | 4 | 0 | 0 | 17 | 32 | 13 |
| front matter | 54 (11%) | 30 (15%) | 14 (10%) | 4 | 17 | 8 | 0 | 8 | 1 | 1 | 12 | 8 | 8 | 2 | 9 | 6 | 2 | 1 | 0 | 0 | 9 | 8 | 6 |
| wiki-links | 69 (14%) | 26 (13%) | 18 (12%) | 4 | 15 | 4 | 1 | 7 | 3 | 2 | 13 | 23 | 3 | 0 | 14 | 3 | 1 | 1 | 0 | 0 | 3 | 12 | 2 |
| raw HTML | 16 (3%) | 10 (5%) | 6 (4%) | 0 | 7 | 2 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 5 | 1 | 2 | 0 | 0 | 0 | 3 | 4 | 2 |
| emoji shortcodes | 8 (2%) | 5 (2%) | 1 (1%) | 0 | 2 | 1 | 0 | 0 | 0 | 0 | 2 | 1 | 3 | 0 | 3 | 3 | 1 | 2 | 0 | 0 | 2 | 0 | 1 |
| callouts or admonitions | 37 (7%) | 17 (8%) | 13 (9%) | 2 | 14 | 5 | 0 | 2 | 1 | 0 | 8 | 4 | 2 | 0 | 7 | 4 | 1 | 0 | 0 | 0 | 3 | 11 | 4 |
| markdown named, no form named | 131 (26%) | 38 (19%) | 35 (24%) | 8 | 21 | 12 | 7 | 9 | 5 | 7 | 48 | 35 | 18 | 18 | 13 | 2 | 0 | 1 | 1 | 1 | 5 | 16 | 5 |
| undecidable, no value coded | 1 (0%) | 1 (0%) | 0 (0%) | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 |

Silent (not stated), each comparable counted once: ALL 11; SHAPE 7; STORE-NS 4; FH 1; MAS 4; SN 3; UA 0; HB-C 0; HB-F 1; VS 1; AT-T 0; AT-O 0; AT-M 1; AT-G 0; GH-E 2; GH-V 1; GH-P 0; GH-R 0; ACC 0; TCL 0; MAS-free 2; MAS-paid 2; MAS-mac 2.

V13 is among the variables the second coding found weakest (8 cells the rule cannot decide; adjusted agreement 0.78). In particular whether "markdown named, no form named" may sit beside named forms is unsettled.

## V13(b) Unrecognised content (single)

| value | ALL (496) | SHAPE (204) | STORE-NS (145) | FH (25) | MAS (134) | SN (48) | UA (13) | HB-C (44) | HB-F (17) | VS (19) | AT-T (132) | AT-O (87) | AT-M (63) | AT-G (40) | GH-E (84) | GH-V (21) | GH-P (5) | GH-R (5) | ACC (2) | TCL (1) | MAS-free (52) | MAS-paid (82) | MAS-mac (43) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| shown as plain text, stated | 7 (1%) | 7 (3%) | 0 (0%) | 0 | 3 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 2 | 1 | 0 | 1 | 0 | 0 | 3 | 0 | 1 |
| dropped or hidden, stated | 0 (0%) | 0 (0%) | 0 (0%) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| warned about, stated | 1 (0%) | 0 (0%) | 1 (1%) | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| undecidable, no value coded | 5 (1%) | 3 (1%) | 2 (1%) | 0 | 2 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 2 |

Silent (not stated), each comparable counted once: ALL 483; SHAPE 194; STORE-NS 142; FH 25; MAS 129; SN 46; UA 13; HB-C 43; HB-F 17; VS 17; AT-T 132; AT-O 87; AT-M 63; AT-G 40; GH-E 81; GH-V 20; GH-P 5; GH-R 4; ACC 2; TCL 1; MAS-free 48; MAS-paid 81; MAS-mac 40.

## V14 Whether files stay local (single)

| value | ALL (496) | SHAPE (204) | STORE-NS (145) | FH (25) | MAS (134) | SN (48) | UA (13) | HB-C (44) | HB-F (17) | VS (19) | AT-T (132) | AT-O (87) | AT-M (63) | AT-G (40) | GH-E (84) | GH-V (21) | GH-P (5) | GH-R (5) | ACC (2) | TCL (1) | MAS-free (52) | MAS-paid (82) | MAS-mac (43) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| local, stated | 124 (25%) | 47 (23%) | 35 (24%) | 3 | 53 | 6 | 0 | 11 | 0 | 1 | 30 | 23 | 17 | 3 | 15 | 1 | 1 | 1 | 0 | 1 | 25 | 28 | 19 |
| local by default, optional upload stated | 101 (20%) | 35 (17%) | 25 (17%) | 5 | 30 | 6 | 0 | 6 | 0 | 2 | 24 | 37 | 5 | 2 | 17 | 2 | 2 | 1 | 1 | 0 | 9 | 21 | 2 |
| content leaves the device, stated | 13 (3%) | 2 (1%) | 9 (6%) | 1 | 8 | 1 | 1 | 1 | 1 | 0 | 1 | 4 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 7 | 0 |
| undecidable, no value coded | 31 (6%) | 7 (3%) | 8 (6%) | 0 | 11 | 1 | 0 | 1 | 0 | 0 | 10 | 8 | 8 | 8 | 1 | 0 | 1 | 0 | 0 | 0 | 3 | 8 | 0 |

Silent (not stated), each comparable counted once: ALL 227; SHAPE 113; STORE-NS 68; FH 16; MAS 32; SN 34; UA 12; HB-C 25; HB-F 16; VS 16; AT-T 67; AT-O 15; AT-M 32; AT-G 26; GH-E 50; GH-V 18; GH-P 1; GH-R 3; ACC 1; TCL 0; MAS-free 14; MAS-paid 18; MAS-mac 22.

5 cells the rule cannot decide in the second coding (sync to the user's own cloud fits no value); adjusted agreement 0.89.

## V15 Network and data leaving (multi)

| value | ALL (496) | SHAPE (204) | STORE-NS (145) | FH (25) | MAS (134) | SN (48) | UA (13) | HB-C (44) | HB-F (17) | VS (19) | AT-T (132) | AT-O (87) | AT-M (63) | AT-G (40) | GH-E (84) | GH-V (21) | GH-P (5) | GH-R (5) | ACC (2) | TCL (1) | MAS-free (52) | MAS-paid (82) | MAS-mac (43) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| works offline, stated | 151 (30%) | 58 (28%) | 46 (32%) | 8 | 54 | 17 | 1 | 11 | 0 | 2 | 40 | 33 | 22 | 7 | 21 | 5 | 1 | 2 | 0 | 0 | 20 | 34 | 16 |
| network required, stated | 2 (0%) | 1 (0%) | 1 (1%) | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| network used for named features only, stated | 110 (22%) | 45 (22%) | 28 (19%) | 2 | 35 | 8 | 1 | 13 | 1 | 2 | 19 | 28 | 12 | 3 | 21 | 6 | 3 | 3 | 1 | 0 | 13 | 22 | 6 |
| no telemetry or tracking, stated | 180 (36%) | 71 (35%) | 61 (42%) | 3 | 101 | 10 | 0 | 10 | 0 | 1 | 36 | 36 | 17 | 1 | 15 | 7 | 3 | 2 | 0 | 0 | 43 | 58 | 30 |
| telemetry, analytics or crash reports sent, stated | 54 (11%) | 17 (8%) | 19 (13%) | 0 | 25 | 1 | 0 | 7 | 0 | 1 | 11 | 14 | 3 | 2 | 5 | 0 | 0 | 1 | 1 | 0 | 9 | 16 | 7 |
| account required, stated | 8 (2%) | 0 (0%) | 2 (1%) | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 2 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 |
| undecidable, no value coded | 3 (1%) | 1 (0%) | 0 (0%) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

Silent (not stated), each comparable counted once: ALL 194; SHAPE 83; STORE-NS 53; FH 16; MAS 12; SN 25; UA 10; HB-C 19; HB-F 15; VS 14; AT-T 65; AT-O 22; AT-M 33; AT-G 31; GH-E 40; GH-V 10; GH-P 1; GH-R 2; ACC 1; TCL 1; MAS-free 4; MAS-paid 8; MAS-mac 8.

## V16(b) Price shape (multi)

| value | ALL (496) | SHAPE (204) | STORE-NS (145) | FH (25) | MAS (134) | SN (48) | UA (13) | HB-C (44) | HB-F (17) | VS (19) | AT-T (132) | AT-O (87) | AT-M (63) | AT-G (40) | GH-E (84) | GH-V (21) | GH-P (5) | GH-R (5) | ACC (2) | TCL (1) | MAS-free (52) | MAS-paid (82) | MAS-mac (43) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| free | 248 (50%) | 156 (76%) | 6 (4%) | 23 | 56 | 25 | 6 | 19 | 2 | 18 | 78 | 63 | 31 | 17 | 42 | 9 | 2 | 3 | 1 | 0 | 52 | 4 | 23 |
| free with paid tier or features | 99 (20%) | 0 (0%) | 58 (40%) | 1 | 53 | 2 | 0 | 3 | 0 | 0 | 27 | 21 | 13 | 8 | 4 | 0 | 0 | 1 | 1 | 0 | 0 | 53 | 8 |
| one-time purchase | 92 (19%) | 0 (0%) | 60 (41%) | 1 | 53 | 1 | 0 | 8 | 0 | 0 | 32 | 11 | 16 | 7 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 53 | 14 |
| one-time purchase with paid upgrades | 4 (1%) | 0 (0%) | 0 (0%) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| subscription | 53 (11%) | 0 (0%) | 30 (21%) | 2 | 25 | 3 | 0 | 3 | 0 | 0 | 15 | 17 | 4 | 1 | 2 | 0 | 0 | 1 | 1 | 0 | 0 | 25 | 1 |
| free trial, then paid | 49 (10%) | 0 (0%) | 30 (21%) | 1 | 24 | 2 | 0 | 7 | 0 | 0 | 20 | 5 | 11 | 7 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 24 | 7 |
| pay what you want | 0 (0%) | 0 (0%) | 0 (0%) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| donation or sponsorship invited, use free | 55 (11%) | 35 (17%) | 4 (3%) | 12 | 8 | 4 | 3 | 7 | 0 | 4 | 21 | 11 | 5 | 3 | 11 | 2 | 1 | 1 | 0 | 0 | 4 | 4 | 4 |
| paid licence for a named use | 5 (1%) | 0 (0%) | 1 (1%) | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| price on request | 3 (1%) | 0 (0%) | 1 (1%) | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 1 | 0 | 2 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |
| undecidable, no value coded | 16 (3%) | 1 (0%) | 13 (9%) | 0 | 9 | 1 | 1 | 3 | 0 | 0 | 3 | 0 | 4 | 4 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 9 | 4 |

Silent (not stated), each comparable counted once: ALL 97; SHAPE 46; STORE-NS 46; FH 0; MAS 0; SN 19; UA 6; HB-C 10; HB-F 15; VS 1; AT-T 6; AT-O 0; AT-M 5; AT-G 5; GH-E 36; GH-V 12; GH-P 3; GH-R 1; ACC 0; TCL 1; MAS-free 0; MAS-paid 0; MAS-mac 0.

No paid share is compared between any two cells (frame review, forbidden comparison 2). A repository with no price text is silent, not free.

## V16(c) Licence (multi)

| value | ALL (496) | SHAPE (204) | STORE-NS (145) | FH (25) | MAS (134) | SN (48) | UA (13) | HB-C (44) | HB-F (17) | VS (19) | AT-T (132) | AT-O (87) | AT-M (63) | AT-G (40) | GH-E (84) | GH-V (21) | GH-P (5) | GH-R (5) | ACC (2) | TCL (1) | MAS-free (52) | MAS-paid (82) | MAS-mac (43) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| named open-source licence | 240 (48%) | 137 (67%) | 41 (28%) | 23 | 5 | 36 | 11 | 23 | 16 | 11 | 64 | 44 | 24 | 13 | 78 | 21 | 5 | 5 | 2 | 1 | 4 | 1 | 1 |
| source available, not open-source, stated | 4 (1%) | 1 (0%) | 0 (0%) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| proprietary or end-user licence agreement, stated | 106 (21%) | 6 (3%) | 26 (18%) | 1 | 15 | 9 | 0 | 10 | 1 | 0 | 59 | 35 | 30 | 23 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 15 | 5 |
| public domain, stated | 1 (0%) | 1 (0%) | 0 (0%) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| undecidable, no value coded | 5 (1%) | 3 (1%) | 1 (1%) | 0 | 2 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 |

Silent (not stated), each comparable counted once: ALL 146; SHAPE 59; STORE-NS 77; FH 1; MAS 112; SN 3; UA 2; HB-C 11; HB-F 0; VS 7; AT-T 11; AT-O 6; AT-M 9; AT-G 4; GH-E 2; GH-V 0; GH-P 0; GH-R 0; ACC 0; TCL 0; MAS-free 46; MAS-paid 66; MAS-mac 37.

## V17 Cost beyond the price (multi)

| value | ALL (496) | SHAPE (204) | STORE-NS (145) | FH (25) | MAS (134) | SN (48) | UA (13) | HB-C (44) | HB-F (17) | VS (19) | AT-T (132) | AT-O (87) | AT-M (63) | AT-G (40) | GH-E (84) | GH-V (21) | GH-P (5) | GH-R (5) | ACC (2) | TCL (1) | MAS-free (52) | MAS-paid (82) | MAS-mac (43) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| another product or subscription required, stated | 17 (3%) | 5 (2%) | 2 (1%) | 3 | 1 | 1 | 0 | 1 | 0 | 0 | 5 | 8 | 0 | 0 | 3 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 |
| own API key or service account required, stated | 37 (7%) | 10 (5%) | 10 (7%) | 0 | 11 | 0 | 0 | 1 | 0 | 0 | 12 | 13 | 2 | 0 | 9 | 1 | 1 | 0 | 0 | 0 | 2 | 9 | 0 |
| account with the maker required, stated | 9 (2%) | 1 (0%) | 0 (0%) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 6 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| paid support or setup required, stated | 0 (0%) | 0 (0%) | 0 (0%) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| no other cost, stated | 19 (4%) | 11 (5%) | 2 (1%) | 1 | 8 | 2 | 0 | 2 | 0 | 0 | 8 | 2 | 5 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 2 | 4 |
| undecidable, no value coded | 4 (1%) | 4 (2%) | 0 (0%) | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 |

Silent (not stated), each comparable counted once: ALL 417; SHAPE 176; STORE-NS 131; FH 21; MAS 112; SN 45; UA 13; HB-C 41; HB-F 17; VS 19; AT-T 106; AT-O 61; AT-M 55; AT-G 39; GH-E 71; GH-V 20; GH-P 4; GH-R 5; ACC 1; TCL 1; MAS-free 42; MAS-paid 70; MAS-mac 39.

## V18 Use at work (multi)

| value | ALL (496) | SHAPE (204) | STORE-NS (145) | FH (25) | MAS (134) | SN (48) | UA (13) | HB-C (44) | HB-F (17) | VS (19) | AT-T (132) | AT-O (87) | AT-M (63) | AT-G (40) | GH-E (84) | GH-V (21) | GH-P (5) | GH-R (5) | ACC (2) | TCL (1) | MAS-free (52) | MAS-paid (82) | MAS-mac (43) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| commercial or work use free, stated | 6 (1%) | 2 (1%) | 2 (1%) | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 3 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| commercial or work use needs a paid licence, stated | 5 (1%) | 0 (0%) | 1 (1%) | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| team, business or volume licence offered | 14 (3%) | 0 (0%) | 4 (3%) | 0 | 1 | 0 | 0 | 3 | 0 | 0 | 7 | 4 | 2 | 0 | 4 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 |
| work use restricted or forbidden, stated | 4 (1%) | 0 (0%) | 0 (0%) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| undecidable, no value coded | 7 (1%) | 3 (1%) | 1 (1%) | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 2 | 1 | 1 | 3 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 |

Silent (not stated), each comparable counted once: ALL 466; SHAPE 199; STORE-NS 137; FH 24; MAS 131; SN 47; UA 13; HB-C 39; HB-F 17; VS 19; AT-T 124; AT-O 76; AT-M 60; AT-G 39; GH-E 75; GH-V 21; GH-P 5; GH-R 5; ACC 1; TCL 1; MAS-free 51; MAS-paid 80; MAS-mac 42.

## V19 The unit a buyer takes (multi)

| value | ALL (496) | SHAPE (204) | STORE-NS (145) | FH (25) | MAS (134) | SN (48) | UA (13) | HB-C (44) | HB-F (17) | VS (19) | AT-T (132) | AT-O (87) | AT-M (63) | AT-G (40) | GH-E (84) | GH-V (21) | GH-P (5) | GH-R (5) | ACC (2) | TCL (1) | MAS-free (52) | MAS-paid (82) | MAS-mac (43) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| a copy to download or install | 325 (66%) | 141 (69%) | 81 (56%) | 24 | 76 | 35 | 6 | 37 | 9 | 8 | 93 | 67 | 38 | 18 | 60 | 15 | 3 | 4 | 2 | 1 | 32 | 44 | 26 |
| a licence per person | 11 (2%) | 0 (0%) | 5 (3%) | 0 | 3 | 1 | 0 | 2 | 0 | 0 | 4 | 0 | 1 | 1 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |
| a licence per device | 4 (1%) | 1 (0%) | 1 (1%) | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 2 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| a subscription per person | 26 (5%) | 0 (0%) | 16 (11%) | 0 | 15 | 1 | 0 | 1 | 0 | 0 | 5 | 8 | 1 | 1 | 2 | 0 | 0 | 0 | 1 | 0 | 0 | 15 | 0 |
| a licence or subscription per organisation, team or site | 6 (1%) | 0 (0%) | 0 (0%) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 1 | 1 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| a package the system's package manager maintains | 108 (22%) | 52 (25%) | 44 (30%) | 13 | 0 | 40 | 12 | 25 | 16 | 0 | 24 | 14 | 13 | 8 | 14 | 8 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |
| a component built into the buyer's software | 3 (1%) | 2 (1%) | 1 (1%) | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| an account on a service | 19 (4%) | 0 (0%) | 3 (2%) | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 8 | 14 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| support or a support contract | 0 (0%) | 0 (0%) | 0 (0%) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| undecidable, no value coded | 6 (1%) | 0 (0%) | 4 (3%) | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 1 |

Silent (not stated), each comparable counted once: ALL 120; SHAPE 56; STORE-NS 34; FH 0; MAS 48; SN 3; UA 1; HB-C 2; HB-F 1; VS 11; AT-T 26; AT-O 12; AT-M 16; AT-G 14; GH-E 22; GH-V 4; GH-P 2; GH-R 1; ACC 0; TCL 0; MAS-free 20; MAS-paid 28; MAS-mac 16.

6 cells the rule cannot decide in the second coding (adjusted agreement 0.80): whether a store listing is a download offer is unsettled.

## V20 The surface the product sells on (multi)

| value | ALL (496) | SHAPE (204) | STORE-NS (145) | FH (25) | MAS (134) | SN (48) | UA (13) | HB-C (44) | HB-F (17) | VS (19) | AT-T (132) | AT-O (87) | AT-M (63) | AT-G (40) | GH-E (84) | GH-V (21) | GH-P (5) | GH-R (5) | ACC (2) | TCL (1) | MAS-free (52) | MAS-paid (82) | MAS-mac (43) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| application store listing | 212 (43%) | 93 (46%) | 101 (70%) | 25 | 134 | 42 | 5 | 5 | 1 | 0 | 37 | 21 | 15 | 10 | 7 | 1 | 0 | 0 | 0 | 0 | 52 | 82 | 43 |
| extension marketplace listing | 27 (5%) | 22 (11%) | 1 (1%) | 0 | 0 | 0 | 0 | 0 | 0 | 19 | 3 | 0 | 2 | 2 | 3 | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| package registry page | 71 (14%) | 28 (14%) | 43 (30%) | 6 | 2 | 10 | 11 | 42 | 16 | 0 | 20 | 4 | 10 | 8 | 10 | 6 | 1 | 1 | 0 | 0 | 0 | 2 | 1 |
| code repository page | 226 (46%) | 135 (66%) | 34 (23%) | 21 | 6 | 30 | 7 | 22 | 16 | 9 | 58 | 36 | 25 | 12 | 84 | 21 | 5 | 5 | 2 | 1 | 5 | 1 | 0 |
| release page | 49 (10%) | 30 (15%) | 6 (4%) | 4 | 2 | 7 | 1 | 4 | 3 | 1 | 13 | 10 | 7 | 0 | 23 | 5 | 0 | 0 | 1 | 0 | 2 | 0 | 0 |
| maker's own website | 298 (60%) | 102 (50%) | 77 (53%) | 17 | 81 | 23 | 6 | 32 | 2 | 2 | 104 | 75 | 48 | 28 | 44 | 10 | 3 | 4 | 1 | 0 | 26 | 55 | 25 |
| web store or checkout page | 10 (2%) | 0 (0%) | 5 (3%) | 0 | 1 | 1 | 0 | 4 | 0 | 0 | 5 | 2 | 3 | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| undecidable, no value coded | 8 (2%) | 0 (0%) | 0 (0%) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 2 | 4 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

Silent (not stated), each comparable counted once: ALL 0; SHAPE 0; STORE-NS 0; FH 0; MAS 0; SN 0; UA 0; HB-C 0; HB-F 0; VS 0; AT-T 0; AT-O 0; AT-M 0; AT-G 0; GH-E 0; GH-V 0; GH-P 0; GH-R 0; ACC 0; TCL 0; MAS-free 0; MAS-paid 0; MAS-mac 0.

## V22 Shape dimension 1: how the buyer reaches the offering (multi)

| value | ALL (496) | SHAPE (204) | STORE-NS (145) | FH (25) | MAS (134) | SN (48) | UA (13) | HB-C (44) | HB-F (17) | VS (19) | AT-T (132) | AT-O (87) | AT-M (63) | AT-G (40) | GH-E (84) | GH-V (21) | GH-P (5) | GH-R (5) | ACC (2) | TCL (1) | MAS-free (52) | MAS-paid (82) | MAS-mac (43) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| through an application store or marketplace | 204 (41%) | 89 (44%) | 74 (51%) | 24 | 79 | 36 | 5 | 10 | 1 | 11 | 54 | 33 | 19 | 13 | 17 | 5 | 1 | 2 | 0 | 0 | 28 | 51 | 30 |
| through a package repository or package manager | 172 (35%) | 78 (38%) | 60 (41%) | 17 | 3 | 45 | 13 | 42 | 16 | 1 | 52 | 22 | 29 | 16 | 36 | 11 | 2 | 2 | 0 | 0 | 1 | 2 | 1 |
| by downloading a release or binary from the maker | 211 (43%) | 84 (41%) | 41 (28%) | 13 | 17 | 33 | 2 | 36 | 7 | 1 | 78 | 57 | 32 | 16 | 47 | 13 | 4 | 4 | 2 | 0 | 7 | 10 | 7 |
| by cloning or downloading source and running or building it | 109 (22%) | 72 (35%) | 13 (9%) | 13 | 5 | 14 | 6 | 6 | 8 | 4 | 26 | 15 | 13 | 8 | 46 | 13 | 4 | 4 | 2 | 1 | 4 | 1 | 0 |
| by opening it in a browser | 49 (10%) | 21 (10%) | 7 (5%) | 0 | 6 | 3 | 0 | 3 | 0 | 0 | 18 | 7 | 8 | 6 | 17 | 2 | 1 | 0 | 0 | 0 | 2 | 4 | 1 |
| by adding it as a dependency | 1 (0%) | 1 (0%) | 0 (0%) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| undecidable, no value coded | 9 (2%) | 5 (2%) | 2 (1%) | 0 | 2 | 0 | 0 | 0 | 0 | 2 | 2 | 0 | 2 | 2 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 2 | 0 |

Silent (not stated), each comparable counted once: ALL 78; SHAPE 29; STORE-NS 25; FH 0; MAS 46; SN 0; UA 0; HB-C 0; HB-F 1; VS 3; AT-T 16; AT-O 16; AT-M 9; AT-G 6; GH-E 4; GH-V 1; GH-P 0; GH-R 0; ACC 0; TCL 0; MAS-free 21; MAS-paid 25; MAS-mac 12.

## V23 Shape dimension 2: whether anything is paid before it is reached (single)

| value | ALL (496) | SHAPE (204) | STORE-NS (145) | FH (25) | MAS (134) | SN (48) | UA (13) | HB-C (44) | HB-F (17) | VS (19) | AT-T (132) | AT-O (87) | AT-M (63) | AT-G (40) | GH-E (84) | GH-V (21) | GH-P (5) | GH-R (5) | ACC (2) | TCL (1) | MAS-free (52) | MAS-paid (82) | MAS-mac (43) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| nothing paid before use, stated | 222 (45%) | 150 (74%) | 1 (1%) | 21 | 51 | 21 | 6 | 17 | 1 | 18 | 70 | 54 | 28 | 15 | 39 | 9 | 2 | 3 | 1 | 0 | 50 | 1 | 21 |
| payment required before first use, stated | 32 (6%) | 0 (0%) | 22 (15%) | 0 | 20 | 0 | 0 | 2 | 0 | 0 | 11 | 4 | 7 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 20 | 7 |
| free trial, then payment | 25 (5%) | 0 (0%) | 14 (10%) | 1 | 9 | 2 | 0 | 6 | 0 | 0 | 13 | 3 | 8 | 7 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 9 | 6 |
| free use, payment for more | 95 (19%) | 0 (0%) | 55 (38%) | 1 | 48 | 2 | 0 | 5 | 0 | 0 | 24 | 24 | 8 | 4 | 5 | 0 | 0 | 1 | 1 | 0 | 0 | 48 | 6 |
| donation invited, not required | 5 (1%) | 3 (1%) | 0 (0%) | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 2 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| undecidable, no value coded | 12 (2%) | 3 (1%) | 5 (3%) | 1 | 5 | 1 | 0 | 2 | 0 | 0 | 3 | 2 | 3 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 1 | 4 | 3 |

Silent (not stated), each comparable counted once: ALL 105; SHAPE 48; STORE-NS 48; FH 1; MAS 0; SN 22; UA 7; HB-C 11; HB-F 16; VS 1; AT-T 9; AT-O 0; AT-M 9; AT-G 8; GH-E 36; GH-V 12; GH-P 3; GH-R 1; ACC 0; TCL 1; MAS-free 0; MAS-paid 0; MAS-mac 0.

MAS-free and MAS-paid are defined from V16(b) and V23 (see "How to read"), so they split this table by construction.

## V24 Shape dimension 3: how the sale is taken (multi)

| value | ALL (496) | SHAPE (204) | STORE-NS (145) | FH (25) | MAS (134) | SN (48) | UA (13) | HB-C (44) | HB-F (17) | VS (19) | AT-T (132) | AT-O (87) | AT-M (63) | AT-G (40) | GH-E (84) | GH-V (21) | GH-P (5) | GH-R (5) | ACC (2) | TCL (1) | MAS-free (52) | MAS-paid (82) | MAS-mac (43) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| purchase through a store or marketplace | 41 (8%) | 2 (1%) | 29 (20%) | 0 | 29 | 0 | 0 | 3 | 0 | 0 | 11 | 4 | 4 | 3 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 28 | 12 |
| in-app purchase | 64 (13%) | 0 (0%) | 56 (39%) | 0 | 55 | 1 | 0 | 2 | 0 | 0 | 8 | 6 | 4 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 55 | 10 |
| checkout or licence key from the maker or a payment processor | 27 (5%) | 0 (0%) | 12 (8%) | 0 | 7 | 1 | 0 | 7 | 0 | 0 | 17 | 1 | 10 | 6 | 2 | 0 | 0 | 1 | 0 | 0 | 0 | 7 | 4 |
| subscription account with the maker | 8 (2%) | 0 (0%) | 3 (2%) | 0 | 0 | 2 | 0 | 1 | 0 | 0 | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| sponsorship or donation platform | 56 (11%) | 35 (17%) | 2 (1%) | 9 | 4 | 4 | 3 | 6 | 0 | 4 | 20 | 12 | 5 | 4 | 17 | 3 | 1 | 1 | 0 | 0 | 3 | 1 | 2 |
| contact sales | 6 (1%) | 0 (0%) | 1 (1%) | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 3 | 1 | 0 | 3 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |
| no sale taken, stated | 73 (15%) | 51 (25%) | 0 (0%) | 5 | 14 | 8 | 0 | 11 | 0 | 4 | 19 | 20 | 9 | 2 | 16 | 6 | 1 | 1 | 0 | 0 | 14 | 0 | 8 |
| undecidable, no value coded | 0 (0%) | 0 (0%) | 0 (0%) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

Silent (not stated), each comparable counted once: ALL 266; SHAPE 132; STORE-NS 61; FH 12; MAS 45; SN 35; UA 10; HB-C 21; HB-F 17; VS 14; AT-T 68; AT-O 44; AT-M 35; AT-G 26; GH-E 52; GH-V 14; GH-P 4; GH-R 3; ACC 1; TCL 1; MAS-free 37; MAS-paid 8; MAS-mac 15.

## V25 Shape dimension 4: whether and how a place is held (single)

| value | ALL (496) | SHAPE (204) | STORE-NS (145) | FH (25) | MAS (134) | SN (48) | UA (13) | HB-C (44) | HB-F (17) | VS (19) | AT-T (132) | AT-O (87) | AT-M (63) | AT-G (40) | GH-E (84) | GH-V (21) | GH-P (5) | GH-R (5) | ACC (2) | TCL (1) | MAS-free (52) | MAS-paid (82) | MAS-mac (43) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| capacity limit on buyers stated | 6 (1%) | 0 (0%) | 2 (1%) | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 3 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| per-licence use limit stated | 31 (6%) | 1 (0%) | 21 (14%) | 0 | 15 | 1 | 0 | 6 | 0 | 0 | 9 | 3 | 6 | 3 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 15 | 10 |
| no limit, stated | 14 (3%) | 1 (0%) | 8 (6%) | 0 | 8 | 0 | 0 | 1 | 0 | 0 | 2 | 3 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 0 |
| undecidable, no value coded | 4 (1%) | 1 (0%) | 3 (2%) | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 |

Silent (not stated), each comparable counted once: ALL 441; SHAPE 201; STORE-NS 111; FH 24; MAS 108; SN 47; UA 13; HB-C 36; HB-F 17; VS 19; AT-T 118; AT-O 76; AT-M 57; AT-G 37; GH-E 80; GH-V 21; GH-P 5; GH-R 5; ACC 2; TCL 1; MAS-free 52; MAS-paid 56; MAS-mac 33.

## V26 Release cadence and timing (single)

| value | ALL (496) | SHAPE (204) | STORE-NS (145) | FH (25) | MAS (134) | SN (48) | UA (13) | HB-C (44) | HB-F (17) | VS (19) | AT-T (132) | AT-O (87) | AT-M (63) | AT-G (40) | GH-E (84) | GH-V (21) | GH-P (5) | GH-R (5) | ACC (2) | TCL (1) | MAS-free (52) | MAS-paid (82) | MAS-mac (43) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| scheduled cadence stated | 3 (1%) | 2 (1%) | 1 (1%) | 0 | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 |
| frequent or continuous updates claimed, no schedule | 12 (2%) | 2 (1%) | 4 (3%) | 1 | 4 | 1 | 0 | 0 | 0 | 0 | 4 | 6 | 2 | 0 | 2 | 0 | 0 | 1 | 0 | 0 | 0 | 4 | 2 |
| feature-complete or no further releases planned, stated | 7 (1%) | 4 (2%) | 2 (1%) | 0 | 0 | 1 | 0 | 1 | 2 | 1 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |
| seasonal or dated offer stated | 9 (2%) | 0 (0%) | 5 (3%) | 0 | 5 | 0 | 0 | 1 | 0 | 0 | 3 | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 2 |
| undecidable, no value coded | 4 (1%) | 2 (1%) | 0 (0%) | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 3 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

Silent (not stated), each comparable counted once: ALL 461; SHAPE 194; STORE-NS 133; FH 24; MAS 123; SN 45; UA 13; HB-C 40; HB-F 15; VS 18; AT-T 122; AT-O 78; AT-M 60; AT-G 39; GH-E 79; GH-V 20; GH-P 5; GH-R 4; ACC 1; TCL 1; MAS-free 51; MAS-paid 72; MAS-mac 39.

## V27(a) Last release date, by year as published (single)

The coded value is the latest release, version or listing-update date the captured text gives. "Relative" is a date published as "1 day ago", "4d ago" or "Today"; "month and day" is a date published without its year (most App Store version histories); a "commit date only" row gave a last-commit date and no release date. Capture was 2026-10-09.

| value | ALL (496) | SHAPE (204) | STORE-NS (145) | FH (25) | MAS (134) | SN (48) | UA (13) | HB-C (44) | HB-F (17) | VS (19) | AT-T (132) | AT-O (87) | AT-M (63) | AT-G (40) | GH-E (84) | GH-V (21) | GH-P (5) | GH-R (5) | ACC (2) | TCL (1) | MAS-free (52) | MAS-paid (82) | MAS-mac (43) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2026 | 167 (34%) | 68 (33%) | 43 (30%) | 14 | 31 | 38 | 5 | 14 | 2 | 9 | 42 | 48 | 13 | 2 | 16 | 3 | 1 | 2 | 1 | 0 | 15 | 16 | 12 |
| 2025 | 18 (4%) | 10 (5%) | 3 (2%) | 2 | 4 | 1 | 1 | 1 | 0 | 4 | 9 | 5 | 1 | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 2 | 2 | 4 |
| 2024 | 7 (1%) | 5 (2%) | 2 (1%) | 1 | 0 | 2 | 0 | 1 | 1 | 1 | 3 | 0 | 2 | 1 | 3 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 2021-2023 | 33 (7%) | 8 (4%) | 9 (6%) | 0 | 8 | 2 | 0 | 2 | 0 | 0 | 19 | 2 | 17 | 13 | 4 | 3 | 0 | 0 | 0 | 1 | 1 | 7 | 5 |
| 2020 or earlier | 22 (4%) | 9 (4%) | 5 (3%) | 0 | 2 | 2 | 0 | 3 | 1 | 2 | 11 | 0 | 10 | 9 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 1 |
| relative date (days to months before capture) | 30 (6%) | 15 (7%) | 13 (9%) | 7 | 19 | 2 | 1 | 0 | 0 | 0 | 4 | 2 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 6 | 13 | 2 |
| month and day, no year published | 79 (16%) | 33 (16%) | 36 (25%) | 1 | 55 | 0 | 0 | 3 | 2 | 0 | 8 | 6 | 4 | 0 | 11 | 3 | 0 | 0 | 0 | 0 | 21 | 34 | 15 |
| commit date only: 2026 | 4 (1%) | 1 (0%) | 0 (0%) | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 2 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| commit date only: 2025 | 2 (0%) | 0 (0%) | 0 (0%) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| commit date only: 2024 | 1 (0%) | 0 (0%) | 1 (1%) | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| commit date only: 2021-2023 | 2 (0%) | 2 (1%) | 0 (0%) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| commit date only: 2020 or earlier | 0 (0%) | 0 (0%) | 0 (0%) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| undecidable | 4 (1%) | 0 (0%) | 0 (0%) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| not stated (silent, each row once) | 127 (26%) | 53 (26%) | 33 (23%) | 0 | 15 | 0 | 5 | 20 | 10 | 3 | 31 | 16 | 15 | 11 | 38 | 10 | 4 | 3 | 1 | 0 | 7 | 8 | 4 |

Maintenance and recency are never set GitHub-topic cells against store cells (forbidden comparison 5: the star floor selects for age). AlternativeTo "last updated" dates are directory-page dates, and whether they are listing updates is one of the cases the second coding found the rule cannot decide (V27, 3 cells).

## V27(b) Maintenance status (single)

| value | ALL (496) | SHAPE (204) | STORE-NS (145) | FH (25) | MAS (134) | SN (48) | UA (13) | HB-C (44) | HB-F (17) | VS (19) | AT-T (132) | AT-O (87) | AT-M (63) | AT-G (40) | GH-E (84) | GH-V (21) | GH-P (5) | GH-R (5) | ACC (2) | TCL (1) | MAS-free (52) | MAS-paid (82) | MAS-mac (43) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| archived, deprecated or unmaintained, stated | 37 (7%) | 13 (6%) | 6 (4%) | 1 | 0 | 2 | 1 | 8 | 2 | 0 | 23 | 3 | 11 | 10 | 8 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 0 |
| actively maintained, stated | 12 (2%) | 9 (4%) | 3 (2%) | 3 | 1 | 1 | 1 | 2 | 1 | 0 | 6 | 1 | 3 | 0 | 6 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| undecidable, no value coded | 19 (4%) | 8 (4%) | 9 (6%) | 1 | 0 | 9 | 0 | 7 | 0 | 0 | 5 | 0 | 4 | 4 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

Silent (not stated), each comparable counted once: ALL 428; SHAPE 174; STORE-NS 127; FH 20; MAS 133; SN 36; UA 11; HB-C 27; HB-F 14; VS 19; AT-T 98; AT-O 83; AT-M 45; AT-G 26; GH-E 64; GH-V 19; GH-P 5; GH-R 4; ACC 1; TCL 1; MAS-free 52; MAS-paid 81; MAS-mac 42.

Maintenance and recency are never set GitHub-topic cells against store cells (forbidden comparison 5: the star floor selects for age).

## V28 Finding the way around a long document (multi)

| value | ALL (496) | SHAPE (204) | STORE-NS (145) | FH (25) | MAS (134) | SN (48) | UA (13) | HB-C (44) | HB-F (17) | VS (19) | AT-T (132) | AT-O (87) | AT-M (63) | AT-G (40) | GH-E (84) | GH-V (21) | GH-P (5) | GH-R (5) | ACC (2) | TCL (1) | MAS-free (52) | MAS-paid (82) | MAS-mac (43) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| outline, contents or headings sidebar | 158 (32%) | 70 (34%) | 58 (40%) | 8 | 63 | 13 | 2 | 15 | 4 | 5 | 45 | 12 | 17 | 7 | 32 | 11 | 3 | 4 | 0 | 0 | 17 | 46 | 14 |
| jump to heading or section | 69 (14%) | 20 (10%) | 34 (23%) | 2 | 35 | 4 | 1 | 7 | 4 | 0 | 17 | 4 | 9 | 3 | 10 | 5 | 2 | 3 | 0 | 0 | 8 | 27 | 8 |
| folding of sections | 28 (6%) | 12 (6%) | 9 (6%) | 2 | 7 | 3 | 0 | 3 | 1 | 0 | 5 | 8 | 0 | 0 | 10 | 1 | 1 | 0 | 0 | 0 | 2 | 5 | 2 |
| minimap or overview strip | 3 (1%) | 2 (1%) | 1 (1%) | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| scroll position kept or synchronised | 59 (12%) | 29 (14%) | 21 (14%) | 2 | 23 | 4 | 1 | 1 | 2 | 2 | 12 | 1 | 5 | 4 | 15 | 8 | 3 | 1 | 0 | 1 | 6 | 17 | 8 |
| bookmarks | 12 (2%) | 2 (1%) | 6 (4%) | 0 | 5 | 1 | 0 | 0 | 1 | 0 | 2 | 2 | 2 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 4 | 1 |
| undecidable, no value coded | 1 (0%) | 0 (0%) | 1 (1%) | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

Silent (not stated), each comparable counted once: ALL 296; SHAPE 117; STORE-NS 74; FH 15; MAS 62; SN 30; UA 10; HB-C 25; HB-F 10; VS 14; AT-T 78; AT-O 70; AT-M 42; AT-G 30; GH-E 43; GH-V 8; GH-P 0; GH-R 1; ACC 2; TCL 0; MAS-free 30; MAS-paid 32; MAS-mac 24.

## V29 Finding a word (multi)

| value | ALL (496) | SHAPE (204) | STORE-NS (145) | FH (25) | MAS (134) | SN (48) | UA (13) | HB-C (44) | HB-F (17) | VS (19) | AT-T (132) | AT-O (87) | AT-M (63) | AT-G (40) | GH-E (84) | GH-V (21) | GH-P (5) | GH-R (5) | ACC (2) | TCL (1) | MAS-free (52) | MAS-paid (82) | MAS-mac (43) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| search within the document | 94 (19%) | 37 (18%) | 31 (21%) | 1 | 41 | 7 | 0 | 6 | 3 | 2 | 18 | 15 | 13 | 1 | 11 | 5 | 2 | 2 | 1 | 0 | 14 | 27 | 11 |
| search across files or a folder | 100 (20%) | 32 (16%) | 26 (18%) | 5 | 32 | 6 | 0 | 1 | 1 | 1 | 20 | 31 | 10 | 2 | 14 | 4 | 1 | 0 | 1 | 0 | 9 | 23 | 5 |
| regular-expression search | 18 (4%) | 11 (5%) | 1 (1%) | 1 | 5 | 1 | 0 | 0 | 0 | 0 | 8 | 3 | 4 | 0 | 6 | 1 | 0 | 0 | 0 | 0 | 4 | 1 | 2 |
| find and replace | 66 (13%) | 37 (18%) | 14 (10%) | 3 | 21 | 4 | 0 | 3 | 0 | 0 | 19 | 8 | 8 | 1 | 23 | 4 | 2 | 2 | 0 | 0 | 8 | 13 | 2 |
| undecidable, no value coded | 70 (14%) | 24 (12%) | 17 (12%) | 7 | 13 | 9 | 1 | 11 | 1 | 2 | 19 | 28 | 2 | 2 | 9 | 1 | 1 | 1 | 0 | 0 | 7 | 6 | 3 |

Silent (not stated), each comparable counted once: ALL 241; SHAPE 107; STORE-NS 75; FH 12; MAS 52; SN 28; UA 12; HB-C 25; HB-F 12; VS 14; AT-T 74; AT-O 23; AT-M 41; AT-G 34; GH-E 45; GH-V 12; GH-P 1; GH-R 2; ACC 1; TCL 1; MAS-free 22; MAS-paid 30; MAS-mac 25.

"Search" with no scope named codes undecidable by rule, which is why the undecidable row is large.

## V30 Links, images and references to other files (multi)

| value | ALL (496) | SHAPE (204) | STORE-NS (145) | FH (25) | MAS (134) | SN (48) | UA (13) | HB-C (44) | HB-F (17) | VS (19) | AT-T (132) | AT-O (87) | AT-M (63) | AT-G (40) | GH-E (84) | GH-V (21) | GH-P (5) | GH-R (5) | ACC (2) | TCL (1) | MAS-free (52) | MAS-paid (82) | MAS-mac (43) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| follows links to other markdown files inside the product | 29 (6%) | 14 (7%) | 10 (7%) | 1 | 12 | 3 | 0 | 0 | 2 | 1 | 2 | 4 | 2 | 0 | 6 | 2 | 2 | 1 | 0 | 0 | 4 | 8 | 4 |
| opens web links in the browser | 17 (3%) | 7 (3%) | 6 (4%) | 1 | 5 | 4 | 0 | 0 | 0 | 0 | 1 | 2 | 3 | 0 | 2 | 2 | 1 | 1 | 0 | 0 | 1 | 4 | 0 |
| shows local images | 41 (8%) | 26 (13%) | 10 (7%) | 2 | 14 | 6 | 0 | 4 | 1 | 1 | 7 | 0 | 2 | 1 | 8 | 4 | 2 | 1 | 0 | 0 | 8 | 6 | 5 |
| shows remote images | 27 (5%) | 13 (6%) | 8 (6%) | 2 | 11 | 3 | 0 | 1 | 1 | 0 | 5 | 0 | 5 | 0 | 3 | 1 | 1 | 0 | 0 | 0 | 5 | 6 | 4 |
| follows wiki-links or backlinks | 49 (10%) | 13 (6%) | 15 (10%) | 4 | 13 | 3 | 0 | 1 | 1 | 1 | 13 | 18 | 3 | 0 | 8 | 0 | 0 | 0 | 0 | 0 | 1 | 12 | 1 |
| resolves reference-style links | 1 (0%) | 1 (0%) | 0 (0%) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| follows links to headings within the document | 17 (3%) | 6 (3%) | 7 (5%) | 0 | 5 | 2 | 0 | 2 | 2 | 0 | 2 | 0 | 5 | 1 | 3 | 1 | 0 | 0 | 0 | 0 | 1 | 4 | 1 |
| undecidable, no value coded | 6 (1%) | 3 (1%) | 2 (1%) | 1 | 1 | 0 | 1 | 2 | 0 | 0 | 1 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |

Silent (not stated), each comparable counted once: ALL 369; SHAPE 151; STORE-NS 104; FH 17; MAS 91; SN 34; UA 12; HB-C 36; HB-F 14; VS 17; AT-T 107; AT-O 68; AT-M 51; AT-G 38; GH-E 62; GH-V 15; GH-P 1; GH-R 3; ACC 2; TCL 1; MAS-free 38; MAS-paid 53; MAS-mac 32.

## V31 Keeping up with a file edited elsewhere (single)

| value | ALL (496) | SHAPE (204) | STORE-NS (145) | FH (25) | MAS (134) | SN (48) | UA (13) | HB-C (44) | HB-F (17) | VS (19) | AT-T (132) | AT-O (87) | AT-M (63) | AT-G (40) | GH-E (84) | GH-V (21) | GH-P (5) | GH-R (5) | ACC (2) | TCL (1) | MAS-free (52) | MAS-paid (82) | MAS-mac (43) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| reloads when the file changes on disk, stated | 56 (11%) | 23 (11%) | 22 (15%) | 2 | 20 | 7 | 1 | 7 | 7 | 1 | 13 | 10 | 9 | 1 | 4 | 5 | 1 | 1 | 0 | 0 | 11 | 9 | 13 |
| preview updates as you type inside the product, stated | 98 (20%) | 44 (22%) | 27 (19%) | 7 | 32 | 10 | 5 | 6 | 0 | 0 | 33 | 10 | 18 | 13 | 24 | 7 | 2 | 2 | 0 | 0 | 13 | 19 | 11 |
| both stated | 26 (5%) | 9 (4%) | 13 (9%) | 1 | 14 | 3 | 0 | 2 | 0 | 0 | 4 | 0 | 3 | 0 | 3 | 2 | 1 | 1 | 0 | 0 | 3 | 11 | 3 |
| manual refresh, stated | 2 (0%) | 1 (0%) | 1 (1%) | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| undecidable, no value coded | 21 (4%) | 17 (8%) | 2 (1%) | 0 | 2 | 1 | 0 | 0 | 0 | 6 | 0 | 0 | 2 | 2 | 8 | 1 | 1 | 0 | 0 | 0 | 0 | 2 | 0 |

Silent (not stated), each comparable counted once: ALL 294; SHAPE 110; STORE-NS 81; FH 15; MAS 66; SN 27; UA 6; HB-C 29; HB-F 9; VS 12; AT-T 82; AT-O 68; AT-M 31; AT-G 24; GH-E 45; GH-V 6; GH-P 0; GH-R 1; ACC 2; TCL 1; MAS-free 24; MAS-paid 42; MAS-mac 16.

## V32 Appearance (multi)

| value | ALL (496) | SHAPE (204) | STORE-NS (145) | FH (25) | MAS (134) | SN (48) | UA (13) | HB-C (44) | HB-F (17) | VS (19) | AT-T (132) | AT-O (87) | AT-M (63) | AT-G (40) | GH-E (84) | GH-V (21) | GH-P (5) | GH-R (5) | ACC (2) | TCL (1) | MAS-free (52) | MAS-paid (82) | MAS-mac (43) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| themes provided | 215 (43%) | 86 (42%) | 74 (51%) | 14 | 65 | 17 | 3 | 22 | 10 | 3 | 59 | 32 | 24 | 10 | 45 | 11 | 2 | 4 | 0 | 0 | 13 | 52 | 21 |
| light and dark modes | 170 (34%) | 76 (37%) | 49 (34%) | 8 | 63 | 19 | 3 | 11 | 3 | 2 | 41 | 33 | 21 | 7 | 27 | 13 | 5 | 4 | 1 | 0 | 26 | 37 | 21 |
| custom stylesheet | 65 (13%) | 30 (15%) | 19 (13%) | 6 | 11 | 9 | 2 | 13 | 2 | 3 | 18 | 7 | 12 | 11 | 16 | 3 | 1 | 1 | 0 | 0 | 1 | 10 | 6 |
| font or size choice | 104 (21%) | 46 (23%) | 32 (22%) | 5 | 45 | 5 | 1 | 8 | 0 | 0 | 23 | 17 | 14 | 4 | 21 | 6 | 3 | 3 | 0 | 0 | 17 | 28 | 9 |
| follows the system appearance, stated | 59 (12%) | 26 (13%) | 18 (12%) | 3 | 27 | 7 | 1 | 2 | 0 | 0 | 12 | 10 | 7 | 5 | 7 | 2 | 1 | 0 | 1 | 0 | 13 | 14 | 12 |
| undecidable, no value coded | 16 (3%) | 7 (3%) | 1 (1%) | 0 | 4 | 1 | 0 | 0 | 0 | 1 | 2 | 6 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 1 |

Silent (not stated), each comparable counted once: ALL 166; SHAPE 58; STORE-NS 47; FH 7; MAS 30; SN 16; UA 7; HB-C 14; HB-F 6; VS 12; AT-T 48; AT-O 31; AT-M 24; AT-G 19; GH-E 19; GH-V 4; GH-P 0; GH-R 1; ACC 1; TCL 1; MAS-free 13; MAS-paid 17; MAS-mac 8.

7 cells the rule cannot decide in the second coding (adjusted agreement 0.80): toggle labels and output themes are read two ways.

## V33 Print, export, send on (multi)

| value | ALL (496) | SHAPE (204) | STORE-NS (145) | FH (25) | MAS (134) | SN (48) | UA (13) | HB-C (44) | HB-F (17) | VS (19) | AT-T (132) | AT-O (87) | AT-M (63) | AT-G (40) | GH-E (84) | GH-V (21) | GH-P (5) | GH-R (5) | ACC (2) | TCL (1) | MAS-free (52) | MAS-paid (82) | MAS-mac (43) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| print | 79 (16%) | 30 (15%) | 32 (22%) | 3 | 37 | 7 | 0 | 6 | 1 | 1 | 19 | 11 | 13 | 2 | 11 | 5 | 4 | 2 | 0 | 0 | 13 | 24 | 13 |
| export to PDF | 196 (40%) | 78 (38%) | 59 (41%) | 10 | 72 | 14 | 2 | 15 | 2 | 2 | 63 | 32 | 30 | 17 | 34 | 8 | 4 | 3 | 0 | 0 | 25 | 47 | 18 |
| export to HTML | 152 (31%) | 59 (29%) | 52 (36%) | 8 | 48 | 12 | 5 | 16 | 3 | 3 | 52 | 16 | 25 | 19 | 34 | 9 | 2 | 2 | 0 | 0 | 11 | 37 | 15 |
| export to another named format | 145 (29%) | 56 (27%) | 51 (35%) | 7 | 50 | 15 | 3 | 15 | 3 | 1 | 44 | 17 | 16 | 14 | 28 | 5 | 3 | 3 | 0 | 0 | 13 | 37 | 11 |
| copy as rich text or HTML | 39 (8%) | 20 (10%) | 10 (7%) | 2 | 11 | 1 | 1 | 3 | 0 | 1 | 11 | 4 | 8 | 5 | 14 | 6 | 1 | 1 | 0 | 0 | 2 | 9 | 5 |
| share or send from the product | 81 (16%) | 24 (12%) | 27 (19%) | 2 | 33 | 5 | 0 | 4 | 0 | 1 | 23 | 18 | 12 | 6 | 10 | 2 | 1 | 0 | 0 | 0 | 11 | 22 | 3 |
| undecidable, no value coded | 2 (0%) | 0 (0%) | 2 (1%) | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 |

Silent (not stated), each comparable counted once: ALL 193; SHAPE 82; STORE-NS 54; FH 11; MAS 39; SN 20; UA 6; HB-C 18; HB-F 11; VS 12; AT-T 42; AT-O 35; AT-M 23; AT-G 15; GH-E 31; GH-V 7; GH-P 0; GH-R 1; ACC 2; TCL 1; MAS-free 20; MAS-paid 19; MAS-mac 17.

## V34 Help and what happens when it breaks (multi)

| value | ALL (496) | SHAPE (204) | STORE-NS (145) | FH (25) | MAS (134) | SN (48) | UA (13) | HB-C (44) | HB-F (17) | VS (19) | AT-T (132) | AT-O (87) | AT-M (63) | AT-G (40) | GH-E (84) | GH-V (21) | GH-P (5) | GH-R (5) | ACC (2) | TCL (1) | MAS-free (52) | MAS-paid (82) | MAS-mac (43) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| issue tracker | 138 (28%) | 87 (43%) | 21 (14%) | 24 | 6 | 30 | 11 | 14 | 5 | 6 | 38 | 25 | 12 | 7 | 43 | 10 | 2 | 4 | 0 | 0 | 4 | 2 | 0 |
| email or contact form | 129 (26%) | 40 (20%) | 48 (33%) | 3 | 58 | 12 | 1 | 9 | 0 | 1 | 34 | 22 | 15 | 10 | 10 | 1 | 0 | 1 | 0 | 0 | 22 | 36 | 16 |
| forum, chat or community | 80 (16%) | 27 (13%) | 12 (8%) | 7 | 5 | 5 | 2 | 8 | 1 | 1 | 29 | 32 | 7 | 4 | 21 | 3 | 1 | 3 | 1 | 1 | 0 | 5 | 0 |
| documentation or guide | 159 (32%) | 61 (30%) | 40 (28%) | 10 | 33 | 15 | 3 | 18 | 4 | 3 | 50 | 44 | 18 | 9 | 29 | 10 | 3 | 1 | 1 | 0 | 6 | 27 | 12 |
| paid or priority support | 5 (1%) | 0 (0%) | 3 (2%) | 0 | 2 | 0 | 0 | 1 | 0 | 0 | 2 | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 2 |
| no support offered, stated | 2 (0%) | 1 (0%) | 0 (0%) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |
| undecidable, no value coded | 5 (1%) | 0 (0%) | 5 (3%) | 0 | 4 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 1 |

Silent (not stated), each comparable counted once: ALL 157; SHAPE 62; STORE-NS 52; FH 0; MAS 52; SN 8; UA 2; HB-C 9; HB-F 9; VS 12; AT-T 34; AT-O 22; AT-M 25; AT-G 16; GH-E 23; GH-V 5; GH-P 0; GH-R 0; ACC 0; TCL 0; MAS-free 25; MAS-paid 27; MAS-mac 17.

## V35 Who else uses it (multi)

| value | ALL (496) | SHAPE (204) | STORE-NS (145) | FH (25) | MAS (134) | SN (48) | UA (13) | HB-C (44) | HB-F (17) | VS (19) | AT-T (132) | AT-O (87) | AT-M (63) | AT-G (40) | GH-E (84) | GH-V (21) | GH-P (5) | GH-R (5) | ACC (2) | TCL (1) | MAS-free (52) | MAS-paid (82) | MAS-mac (43) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| user, download or install count claimed | 116 (23%) | 66 (32%) | 38 (26%) | 23 | 3 | 12 | 8 | 40 | 16 | 19 | 33 | 12 | 15 | 10 | 18 | 6 | 1 | 2 | 1 | 0 | 1 | 2 | 2 |
| rating or review score shown on the listing | 47 (9%) | 15 (7%) | 26 (18%) | 2 | 34 | 0 | 1 | 0 | 0 | 4 | 8 | 3 | 5 | 2 | 0 | 1 | 0 | 1 | 0 | 0 | 9 | 25 | 1 |
| testimonials or quoted users | 15 (3%) | 1 (0%) | 6 (4%) | 0 | 2 | 1 | 0 | 5 | 0 | 0 | 5 | 2 | 5 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 2 |
| named customer organisations | 3 (1%) | 0 (0%) | 0 (0%) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |
| press mentions quoted | 9 (2%) | 3 (1%) | 4 (3%) | 2 | 1 | 1 | 0 | 3 | 0 | 0 | 1 | 4 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| undecidable, no value coded | 28 (6%) | 5 (2%) | 3 (2%) | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 13 | 12 | 0 | 0 | 5 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

Silent (not stated), each comparable counted once: ALL 310; SHAPE 121; STORE-NS 80; FH 1; MAS 97; SN 33; UA 5; HB-C 4; HB-F 1; VS 0; AT-T 82; AT-O 58; AT-M 45; AT-G 30; GH-E 60; GH-V 13; GH-P 4; GH-R 3; ACC 1; TCL 1; MAS-free 41; MAS-paid 56; MAS-mac 39.

Presence of a count or rating is coded; no figure from one instrument is set against another (forbidden comparison 3), and no Mac App Store rating figure enters any finding (zero for every Mac-only listing in the list).

## V36 AI-related claims (multi)

| value | ALL (496) | SHAPE (204) | STORE-NS (145) | FH (25) | MAS (134) | SN (48) | UA (13) | HB-C (44) | HB-F (17) | VS (19) | AT-T (132) | AT-O (87) | AT-M (63) | AT-G (40) | GH-E (84) | GH-V (21) | GH-P (5) | GH-R (5) | ACC (2) | TCL (1) | MAS-free (52) | MAS-paid (82) | MAS-mac (43) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AI features in the product | 91 (18%) | 29 (14%) | 23 (16%) | 4 | 24 | 9 | 0 | 6 | 0 | 0 | 27 | 28 | 3 | 0 | 19 | 0 | 0 | 0 | 2 | 0 | 7 | 17 | 5 |
| made for reading or editing AI output | 40 (8%) | 14 (7%) | 17 (12%) | 1 | 19 | 5 | 0 | 4 | 2 | 0 | 10 | 3 | 7 | 2 | 4 | 3 | 2 | 1 | 1 | 0 | 7 | 12 | 7 |
| works with AI agents or tools | 74 (15%) | 29 (14%) | 16 (11%) | 5 | 12 | 9 | 0 | 10 | 2 | 2 | 19 | 24 | 7 | 0 | 17 | 4 | 2 | 3 | 2 | 0 | 3 | 9 | 2 |
| no AI, stated | 9 (2%) | 1 (0%) | 0 (0%) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 4 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| made with AI, stated | 10 (2%) | 3 (1%) | 3 (2%) | 1 | 1 | 2 | 0 | 0 | 0 | 0 | 5 | 5 | 1 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| undecidable, no value coded | 23 (5%) | 10 (5%) | 6 (4%) | 1 | 9 | 3 | 0 | 1 | 0 | 0 | 4 | 5 | 4 | 2 | 4 | 1 | 0 | 1 | 0 | 0 | 5 | 4 | 2 |

Silent (not stated), each comparable counted once: ALL 314; SHAPE 142; STORE-NS 93; FH 18; MAS 78; SN 29; UA 13; HB-C 31; HB-F 15; VS 17; AT-T 85; AT-O 39; AT-M 46; AT-G 36; GH-E 54; GH-V 15; GH-P 2; GH-R 1; ACC 0; TCL 1; MAS-free 33; MAS-paid 45; MAS-mac 30.

## Verbatim fields: V06, V21, V37

These fields hold quoted text, not values from a list; the tables count rows that carry text, and the quotes are in the corpus.

### V06 Audience text outside the classes

| value | ALL (496) | SHAPE (204) | STORE-NS (145) | FH (25) | MAS (134) | SN (48) | UA (13) | HB-C (44) | HB-F (17) | VS (19) | AT-T (132) | AT-O (87) | AT-M (63) | AT-G (40) | GH-E (84) | GH-V (21) | GH-P (5) | GH-R (5) | ACC (2) | TCL (1) | MAS-free (52) | MAS-paid (82) | MAS-mac (43) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| carried | 293 (59%) | 122 (60%) | 87 (60%) | 17 | 93 | 26 | 6 | 29 | 10 | 6 | 78 | 54 | 30 | 17 | 46 | 11 | 4 | 4 | 1 | 0 | 36 | 57 | 30 |
| undecidable | 0 (0%) | 0 (0%) | 0 (0%) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| silent | 203 (41%) | 82 (40%) | 58 (40%) | 8 | 41 | 22 | 7 | 15 | 7 | 13 | 54 | 33 | 33 | 23 | 38 | 10 | 1 | 1 | 1 | 1 | 16 | 25 | 13 |

### V21 Distribution channels named

| value | ALL (496) | SHAPE (204) | STORE-NS (145) | FH (25) | MAS (134) | SN (48) | UA (13) | HB-C (44) | HB-F (17) | VS (19) | AT-T (132) | AT-O (87) | AT-M (63) | AT-G (40) | GH-E (84) | GH-V (21) | GH-P (5) | GH-R (5) | ACC (2) | TCL (1) | MAS-free (52) | MAS-paid (82) | MAS-mac (43) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| carried | 414 (83%) | 165 (81%) | 122 (84%) | 25 | 89 | 47 | 13 | 43 | 17 | 14 | 117 | 75 | 56 | 33 | 73 | 20 | 5 | 5 | 2 | 1 | 30 | 59 | 31 |
| undecidable | 1 (0%) | 1 (0%) | 0 (0%) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| silent | 81 (16%) | 38 (19%) | 23 (16%) | 0 | 45 | 1 | 0 | 1 | 0 | 5 | 15 | 12 | 7 | 7 | 10 | 1 | 0 | 0 | 0 | 0 | 22 | 23 | 12 |

### V37 Why the product exists

| value | ALL (496) | SHAPE (204) | STORE-NS (145) | FH (25) | MAS (134) | SN (48) | UA (13) | HB-C (44) | HB-F (17) | VS (19) | AT-T (132) | AT-O (87) | AT-M (63) | AT-G (40) | GH-E (84) | GH-V (21) | GH-P (5) | GH-R (5) | ACC (2) | TCL (1) | MAS-free (52) | MAS-paid (82) | MAS-mac (43) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| carried | 165 (33%) | 73 (36%) | 41 (28%) | 6 | 44 | 14 | 2 | 19 | 7 | 1 | 42 | 30 | 17 | 7 | 37 | 12 | 4 | 3 | 1 | 1 | 19 | 25 | 12 |
| undecidable | 6 (1%) | 3 (1%) | 1 (1%) | 0 | 2 | 0 | 0 | 1 | 0 | 0 | 2 | 0 | 2 | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 |
| silent | 325 (66%) | 128 (63%) | 103 (71%) | 19 | 88 | 34 | 11 | 24 | 10 | 18 | 88 | 57 | 44 | 31 | 46 | 9 | 1 | 2 | 1 | 0 | 32 | 56 | 31 |

Channels named per comparable (V21 count as coded, ALL, weighted; rows whose cell records no count are left out): 1: 106; 2: 108; 3: 79; 4: 35; 5: 24; 6: 13; 7: 5; 8: 4; 9: 4; 10: 1; 11: 1; 14: 2.

Rows of ALL (weighted) whose V21 text contains each of these names, case ignored (a name inside a longer name counts, so "App Store" includes "Mac App Store"; "apt" is matched as a substring and may over-count): GitHub 135; App Store 113; Releases 91; Homebrew 62; Snap 46; Flathub 25; AUR 25; Microsoft Store 18; apt 16; winget 14; Google Play 11; npm 11; Scoop 10; Chocolatey 8; Visual Studio Marketplace 8; cargo 6; pip 6; F-Droid 6; Chrome Web Store 5; Firefox 4; Setapp 3.

## V16(a) Price as published (verbatim)

Rows of ALL whose V16(a) holds a figure with a currency: 148 of 427 (unweighted). For the rows coded one-time purchase, the lowest non-zero dollar figure each publishes (unweighted, dollar figures only, so other currencies are left out): ALL 71 rows, lowest 0.99, quartiles 2.99 / 6.99 / 14.99, highest 79.00; MAS 49 rows, lowest 0.99, quartiles 2.99 / 4.99 / 9.99, highest 24.99. Subscription figures carry different periods (month, year) and are not summarised. No paid figure is compared between cells.
