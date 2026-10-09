---
title: "Findings: numbered statements from the coded corpus"
date: 2026-10-09
method: "SAGE Survey section 1, step 7 (numbered findings), under briefs/synthesis-clerk.md; read from 0-comparables/coded-corpus.tsv, the cell, drawn-by and weight columns of 0-comparables/frame/collection-list.tsv, second-coding.md and corrections.md"
---

# Findings from the coded comparables

Every later document cites these by number ("finding 12") instead of restating them. Each finding cites coded data by variable, cell and count; the full value set behind each count is in `taxonomy.md`.

**The standing caveat.** The corpus reads what products publish, and what is bought is not always printed. Absence in the corpus is absence from publication, never absence from the market. Treat a surprising absence as a question for the distributor channel, not as an answer.

A text generator would read the most common values as what the market wants and stop there. A product designer reads them as what makers chose to print, and asks which rates come from a population shaped like the operator's: a free script reached by `git clone`, nothing paid, no sale taken, no place held.

## How the counts are made

- **Denominators.** 449 rows collected; 428 eligible (finding 1). Rates are over eligible rows. The 69 eligible rows drawn by the AlternativeTo sampling rule carry weight 2 wherever they are counted, so the pooled denominator is 496 for 427 rows, and each AlternativeTo cell's denominator counts sampled rows twice. A row in several cells counts once in a pooled rate and once in each cell's own rate.
- **Silence.** "Silent" means the row coded "not stated" on the variable. It is counted once per row, never per value. A row whose price is silent is not free.
- **Three pooled populations.** ALL: every eligible row in an application cell (427 rows, weighted 496). SHAPE: the free sub-population that shares the operator's shape, as the shape note defines it: the GitHub-topic rows that state no payment (89) together with the free rows of the store and package cells (128), 13 rows in both, 204 rows, none weighted. A row is free where V23 or V16(b) states a price and every stated value is "free", "donation invited" or "nothing paid before use". STORE-NS: the rows of the Flathub, Mac App Store, Snap, Ubuntu archive, Homebrew and VS Code cells that are not in SHAPE (145 rows). Of STORE-NS, 96 state a payment and 49 are silent on price; 82 of its 145 rows are paid Mac App Store rows.
- **Cells.** FH Flathub; MAS Mac App Store; SN Snap Store (the first 100 the search returns, ranking undisclosed); UA Ubuntu 25.04 archive, apt-cache search markdown; HB-C and HB-F Homebrew casks and formulae; VS VS Code (the first 100 by installs); AT-T, AT-O, AT-M, AT-G the AlternativeTo lists anchored on Typora, Obsidian, Marked and Glow; GH-E, GH-V, GH-P, GH-R the GitHub topics markdown-editor, -viewer, -preview and -reader at 200 stars or more; ACC awesome-claude-code; TCL tcl-wiki-markdown. GH-P, GH-R, ACC and TCL get counts, never rates. MAS-free (52) and MAS-paid (82) split the Mac App Store cell, as the frame review requires; no MAS row is silent on price.
- **Mac-only listings.** The frame review asks for MAS rates on the Mac-only listings too. This clerk could not open the store's device field. The taxonomy gives a coded stand-in instead, MAS-mac: the 43 MAS rows whose V10 names macOS and names neither iOS nor iPadOS.
- **Comparisons not made.** These follow the frame review, section 2. No paid share is compared between cells, and no popularity figure between instruments. VS and SN are not set against any census cell. GitHub-topic cells are not set against store cells on age, activity, maintenance or recency. SN is not set against FH. The AlternativeTo lists are not compared with each other, nor with a store on platform or price. No platform is compared with another through its cell, and TCL is never pooled. Where a finding gives SHAPE beside STORE-NS, it sets a sub-population defined by the operator's shape against the store rows that do not share it. That is the comparison the brief asks for, not a cell-against-cell one.
- **Instrument limits.** Some variables are weak by the second coding (findings 29 and 30). A finding resting on one names it.

## The cells against the operator's shape

The four dimensions are those of the shape note: D1 how the buyer reaches the offering, D2 whether anything is paid before it is reached, D3 how the sale is taken, D4 whether and how a place is held. "s" is shared with the operator, "d" differs.

| population or cell | rows (weighted) | D1 | D2 | D3 | D4 | basis |
|---|---|---|---|---|---|---|
| FH, MAS, SN, UA, HB-C, HB-F, VS | 25, 134, 48, 13, 44, 17, 19 | d | d | d | s | shape note and frame review: every store rate is marked differs on 1 to 3 |
| AT-T, AT-O, AT-M, AT-G | 132, 87, 63, 40 | d | d | d | s | frame review, forbidden comparison 1 |
| GH-E, GH-V, GH-P, GH-R | 84, 21, 5, 5 (96 pooled) | s | s | s | s | the shape note's sub-population. Coded: 79 of 96 state reach by clone or release download (V22). 7 of 96 state a payment (V23 free use with payment for more, or a trial) and 6 name a sale mechanism (V24). Those 7 are left out of SHAPE |
| ACC, TCL | 2, 1 | not marked | not marked | not marked | s | counts only, no rate |
| SHAPE | 204 | s for its 89 GitHub rows; d for its 115 store-only rows | s | s | s | the shape note's free rows. 2 of 204 name a store purchase in V24 (an anomaly left as coded) |
| STORE-NS | 145 | d | d | d | s | store rows that are paid or silent on price |
| ALL | 496 | d | d | d | s | pooled, mostly store and directory rows |

Dimension 4 is shared everywhere. 441 of 496 rows state no place held (V25, finding 27).

# Findings

## The corpus

**F1. The coded corpus holds 428 eligible comparables of 449 collected.** V01: 428 eligible, 13 "ineligible: markdown not handled", 2 "ineligible: no captured text", 6 undecidable (ia-presenter, kookbook, logseq, ufocus, wonderpen, writed). 427 eligible rows sit in application cells, weighted 496. The 428th, shtmlview, sits only in TCL, where 5 of the 6 collected rows were ineligible components. 5 of the 74 sampled AlternativeTo rows were not eligible. Measured in: all collected rows; no dimension.

## Whom the comparables address

**F2. Most comparables name no buyer class; where one is named, it is writers, developers, students or teams.** V05, ALL: 348/496 silent and 3/496 undecidable only, so 145/496 name at least one class. The silent are counted once. By class (a row may carry several):

| class | ALL /496 | SHAPE /204 | STORE-NS /145 |
|---|---|---|---|
| Writers and authors | 71 | 23 | 20 |
| Developers and coders | 64 | 28 | 18 |
| Students and academics | 42 | 19 | 12 |
| Teams, businesses and organisations | 40 | 9 | 8 |
| Note-takers and personal knowledge managers | 13 | 6 | 1 |
| Bloggers and platform publishers | 12 | 6 | 1 |
| Readers of what AI agents write | 12 | 4 | 8 |
| Plain readers of received markdown files | 4 | 3 | 1 |
| Terminal readers | 2 | 1 | 1 |
| Application developers embedding a markdown view | 0 | 0 | 0 |
| at least one class | 145 | 53 | 37 |
| silent | 348 | 150 | 106 |

By cell, rows naming at least one class: MAS 46/134 (MAS-free 20/52, MAS-paid 26/82), AT-T 41/132, AT-O 32/87, GH-E 21/84, HB-C 16/44, AT-M 11/63, SN 7/48, FH 6/25, AT-G 5/40, GH-V 5/21, HB-F 2/17, UA 1/13, VS 1/19. Text about audience that codes no class is carried in V06 by 293/496; V06 is the weakest variable of the second coding (adjusted agreement 0.67), so that count is soft. Measured in: ALL [d d d s]; SHAPE [s/d s s s]; STORE-NS [d d d s]. Audience is not one of the four dimensions.

**F3. The three buyer rows nearest the operator's reader are almost unaddressed in print.** These are terminal readers, plain readers of received files and readers of AI-agent output (V05 classes 7, 8, 9). Together they appear in 17/496 rows of ALL, 8/204 of SHAPE and 9/145 of STORE-NS. By cell: MAS 10/134, SN 4/48, HB-C 3/44, HB-F 2/17, FH 1/25, GH-V 1/21, GH-E 0/84; AT-T 2/132, AT-O 1/87, AT-M 1/63. The 12 rows naming readers of AI-agent output are inkdrop, macmd-viewer, markdown-format-preview, markdown-hot-reload, marko-markdown-viewer, markread-markdown-reader, markview-markview-reader, markviewer, md-flow-markdown-reader, mdserve, read-md and viewmd. The 6 naming terminal or plain readers are just-a-markdown-viewer, kite-markdown-editor, markdown-hot-reload, md-viewer-markdown, read-markdown-fast-light and rivolink-leaf. Class 10 (developers embedding a view) is coded in no row of any cell; the one eligible TCL row, shtmlview, codes Developers and coders. By the caveat, this is absence from publication; the strike list names sources outside the corpus for these buyers. Measured in: ALL [d d d s]; SHAPE [s/d s s s]; STORE-NS [d d d s].

## Reader only against editor

**F4. About one comparable in six is a reader; most of the rest are editors that show markdown rendered.** V09, ALL: "editor with rendered view" 305/496, "editor, rendered view not stated" 93/496, "reader, editing not stated" 66/496, "reader, stated read-only" 22/496, undecidable 6, silent 4. Readers (both reader values): 88/496 in ALL, 37/204 in SHAPE, 45/145 in STORE-NS. Editors: 163/204 in SHAPE, 98/145 in STORE-NS. Readers by cell: HB-F 15/17, UA 7/13, VS 8/19, GH-V 6/21, SN 11/48, MAS 31/134 (MAS-free 14/52, MAS-paid 17/82, MAS-mac 13/43), HB-C 6/44, AT-T 6/132, AT-M 6/63, GH-E 2/84, FH 1/25, AT-G 1/40, AT-O 0/87; GH-P 1, GH-R 2, ACC 1. The GitHub-topic counts follow from the topic names (GH-E is the editor topic), and the per-cell counts are not set against one another. Measured in: ALL [d d d s]; SHAPE [s/d s s s]; STORE-NS [d d d s]; cells as in the register.

## Kinds and platforms

**F5. Desktop applications dominate the kinds; editor extensions sit mostly in the shape-sharing population, mobile applications mostly in the store remainder.** V08, ALL: desktop application 364/496, mobile application 103, service 68, terminal program 41, editor extension 32, other kind 28 (Quick Look and similar hosts), browser extension 14, component 8; silent 9, undecidable 5. Rates that differ:

| kind | SHAPE /204 | STORE-NS /145 |
|---|---|---|
| editor extension | 27 | 3 |
| mobile application | 36 | 54 |
| service | 23 | 9 |
| terminal program | 18 | 19 |

Among the 88 reader rows (finding 4), 23 are terminal programs, 45 desktop applications, 12 editor extensions and 10 other kinds. V08 had 4 cells the rule cannot decide (finding 29); a mobile platform named without a desktop clause is the open case. Measured in: ALL [d d d s]; SHAPE [s/d s s s]; STORE-NS [d d d s].

**F6. Where a platform is named, it is macOS first, then Linux and Windows.** V10, ALL: macOS 341/496, Linux 186, Windows 174, iOS 113, iPadOS 91, inside a host program 41, Android 40, BSD 13, ChromeOS 4, any desktop with a web browser 1; silent 35, undecidable 6. In SHAPE: macOS 120/204, Linux 81/204, Windows 70/204, inside a host 29/204. In STORE-NS: macOS 123/145, Linux 50/145, Windows 26/145, iOS 65/145. Those STORE-NS rates mostly restate the list, since 82 of its 145 rows are paid Mac App Store rows. The frame review forbids reading platform through the cell: no store cell's rate here says one platform's products do more of anything, and no count is the number of markdown applications on a platform. Measured in: ALL [d d d s]; SHAPE [s/d s s s]; STORE-NS [d d d s].

## Price shapes and the free share

**F7. The free share, by cell (no cell is compared with another).** A row is free where it states a price and every stated price value is free. It is paid where V23 or V16(b) states any payment (paid up front, a trial, or free use with payment for more). It is silent where it states no price.

| cell | free | paid | silent on price |
|---|---|---|---|
| FH | 23/25 | 2 | 0 |
| MAS | 52/134 | 82 | 0 |
| SN | 24/48 | 4 | 20 |
| UA | 6/13 | 0 | 7 |
| HB-C | 19/44 | 13 | 12 |
| HB-F | 2/17 | 0 | 15 |
| VS | 18/19 | 0 | 1 |
| AT-T | 75/132 | 52 | 5 |
| AT-O | 56/87 | 31 | 0 |
| AT-M | 31/63 | 26 | 6 |
| AT-G | 17/40 | 17 | 6 |
| GH-E | 42/84 | 6 | 36 |
| GH-V | 9/21 | 0 | 12 |
| GH-P, GH-R, ACC (counts) | 2, 3, 1 | 0, 1, 1 | 3, 1, 0 |

In MAS, V23 codes "nothing paid before use" for 51/134, "free use, payment for more" 48, "payment required before first use" 20, "free trial, then payment" 9, "donation invited" 1 and undecidable 5. So the list's "Free" price for 106 of 133 includes many in-app purchase rows. Pooled over ALL: free 235/496, paid 161/496, silent 100/496. Measured in each cell [d d d s] except the GitHub-topic cells [s s s s]. This finding speaks to dimension 2, and every store and AlternativeTo cell is marked differs on it.

**F8. Free is the commonest price shape; among paid shapes, freemium and one-time purchase lead.** V16(b), ALL: free 248/496, free with paid tier or features 99, one-time purchase 92, donation or sponsorship invited 55, subscription 53, free trial then paid 49, paid licence for a named use 5, one-time purchase with paid upgrades 4, price on request 3, pay what you want 0; silent 97, undecidable 16. Prices (V16(a)): 71 one-time-purchase rows publish a dollar figure. Their lowest non-zero figures run from 0.99 to 79.00, with quartiles 2.99, 6.99 and 14.99; in MAS, 49 rows run from 0.99 to 24.99, quartiles 2.99, 4.99 and 9.99 (unweighted, dollars only). Licence (V16(c)): a named open-source licence 240/496, proprietary or EULA 106/496, silent 146/496. In SHAPE it is 137/204 open-source against 41/145 in STORE-NS. That is a licence rate, not a price rate. Use at work (V18) is silent in 466/496: 14 offer a team or business licence, 6 state that work use is free, 5 that it needs a paid licence, 4 that it is restricted. Cost beyond the price (V17) is silent in 417/496; 37 state that the buyer needs their own API key or service account. Measured in: ALL [d d d s]; SHAPE [s/d s s s]; STORE-NS [d d d s]. The price part speaks to dimension 2, on which ALL and STORE-NS differ.

**F9. Where a sale is taken it goes through the store; the shape-sharing population takes none and invites sponsorship and stars instead.** V24, ALL: in-app purchase 64/496, purchase through a store or marketplace 41, checkout or licence key from the maker 27, subscription account with the maker 8, contact sales 6, sponsorship or donation platform 56, no sale taken (stated) 73; silent 266. In STORE-NS: in-app 56/145, store purchase 29/145, checkout 12/145. In SHAPE: no sale taken 51/204, sponsorship 35/204, store purchase 2/204, and nothing else. V07 invitations that differ:

| invitation | SHAPE /204 | STORE-NS /145 |
|---|---|---|
| sponsor or donate | 44 | 4 |
| star, follow or watch | 17 | 2 |
| clone or build from source | 71 | 13 |
| download a file | 96 | 49 |
| pay or buy | 1 | 55 |

V24 had 3 cells the rule cannot decide (a bare "Donate" label; which "free" wordings say nothing is sold), and V07 had 4 (finding 29). Measured in: ALL [d d d s]; SHAPE [s/d s s s]; STORE-NS [d d d s]. This speaks to dimension 3, on which ALL and STORE-NS differ.

## Surfaces, reach and units

**F10. Comparables present themselves on the maker's site, a code repository and a store listing; the shape-sharing population is reached by repository and release.** V20, ALL: maker's own website 298/496, code repository page 226, application store listing 212, package registry page 71, release page 49, extension marketplace listing 27, web store or checkout page 10; undecidable 8. V22 (dimension 1), ALL: by downloading a release or binary 211/496, through a store or marketplace 204, through a package repository or manager 172, by cloning or downloading source 109, in a browser 49, as a dependency 1; silent 78, undecidable 9. Rates that differ:

| route (V22) | SHAPE /204 | STORE-NS /145 |
|---|---|---|
| clone or source | 72 | 13 |
| release download | 84 | 41 |
| store | 89 | 74 |
| package manager | 78 | 60 |

46 of the 134 MAS rows are silent on V22, because the listing names no channel in text. Of the 96 GitHub-topic rows, 79 state reach by clone or release. V21 and V22 had 5 and 1 cells the rule cannot decide ("what is a place"; finding 29). Measured in: ALL [d d d s]; SHAPE [s/d s s s]; STORE-NS [d d d s]. This speaks to dimension 1, on which ALL and STORE-NS differ, and on which SHAPE differs for its 115 store-only rows.

**F11. What a buyer takes is a copy, or a package the system maintains; per-person licences and subscriptions are few and sit outside the shape-sharing population.** V19, ALL: a copy to download or install 325/496, a package the system's package manager maintains 108, a subscription per person 26, an account on a service 19, a licence per person 11, a licence or subscription per organisation 6, a licence per device 4, a component built into the buyer's software 3, support 0; silent 120, undecidable 6. SHAPE: copy 141/204, package 52/204, and no licence, subscription or account unit. STORE-NS: copy 81/145, package 44/145, subscription per person 16/145. V19 is among the weak variables (6 cells the rule cannot decide, adjusted agreement 0.80; finding 29). Measured in: ALL [d d d s]; SHAPE [s/d s s s]; STORE-NS [d d d s]. The unit is how the sale is taken (dimension 3), on which ALL and STORE-NS differ.

**F12. Install and update routes: packages, stores and source builds; updates mostly unspoken.** V12(a), ALL: package-manager command 165/496, store install 130, build or run from source 115, run an installer 105, copy or unpack a binary 64, open a URL 37, host's extension manager 22; silent 142. In SHAPE, build or run from source is 76/204 against 13/145 in STORE-NS. V12(b) is silent in 410/496: updates itself 58, through the package manager 21, through the store 20, new version downloaded by hand 14, no updates planned 1. Prerequisites (V11), ALL: minimum operating-system version 224/496, runtime or interpreter 73, build toolchain 50, host program 47, package manager required 14, none needed (stated) 13; silent 133. A runtime or interpreter is named in 38/204 of SHAPE against 15/145 of STORE-NS; "none needed" in 7/204 against 2/145. V12(a) is weak (5 cells the rule cannot decide, adjusted agreement 0.78; no value for container deployment), and so is V11 (3 cells). Measured in: ALL [d d d s]; SHAPE [s/d s s s]; STORE-NS [d d d s]. The install route speaks to dimension 1, on which ALL and STORE-NS differ.

## Markdown forms claimed

**F13. Tables, math and diagrams are the forms most often claimed; a quarter claim markdown with no form named; almost none say what happens to content they do not understand.** V13(a), ALL, each over 496: tables 215 (43%), math 182 (37%), diagrams 167 (34%), task lists 134 (27%), syntax-highlighted code blocks 134 (27%), markdown named with no form 131 (26%), GitHub Flavored Markdown 109 (22%), wiki-links 69 (14%), footnotes 66 (13%), front matter 54 (11%), other named flavour 41 (8%), callouts or admonitions 37 (7%), CommonMark 36 (7%), raw HTML 16 (3%), emoji shortcodes 8 (2%); silent 11. Rates that differ:

| form | SHAPE /204 | STORE-NS /145 |
|---|---|---|
| math | 86 | 48 |
| tables | 76 | 72 |
| GitHub Flavored Markdown | 46 | 41 |
| front matter | 30 | 14 |

V13(b), unrecognised content, is silent in 483/496: "shown as plain text" 7, "warned about" 1, "dropped or hidden" 0, undecidable 5. V13 is among the weakest variables (8 cells the rule cannot decide, adjusted agreement 0.78). In particular, whether "markdown named, no form named" may sit beside named forms is unsettled, so its 131 is the least firm figure here. Measured in: ALL [d d d s]; SHAPE [s/d s s s]; STORE-NS [d d d s].

## The features the questions file asks about

**F14. Finding one's way around a long document: an outline is claimed by about a third; most say nothing.** V28, ALL: outline, contents or headings sidebar 158/496, jump to heading 69, scroll position kept or synchronised 59, folding 28, bookmarks 12, minimap 3; silent 296. In SHAPE, outline 70/204 and jump 20/204; in STORE-NS, outline 58/145 and jump 34/145. Among the 88 reader rows, 41 claim at least one of these and 34 an outline. Measured in: ALL [d d d s]; SHAPE [s/d s s s]; STORE-NS [d d d s].

**F15. Finding a word: claimed by about half, and often without a scope.** V29, ALL: search across files or a folder 100/496, search within the document 94, find and replace 66, regular-expression search 18; undecidable 70; silent 241. The 70 undecidable are mostly a bare "search" with no scope, which the rule sends to undecidable. Find and replace is 37/204 in SHAPE against 14/145 in STORE-NS. Among the 88 reader rows, 26 claim search, 22 of them within the document; none claims find and replace or regular expressions. Measured in: ALL [d d d s]; SHAPE [s/d s s s]; STORE-NS [d d d s].

**F16. Links and images: what happens on a click is stated by few.** V30, ALL: follows wiki-links or backlinks 49/496, shows local images 41, follows links to other markdown files inside the product 29, shows remote images 27, opens web links in the browser 17, follows links to headings 17, resolves reference-style links 1; undecidable 6; silent 369. Shows local images is 26/204 in SHAPE against 10/145 in STORE-NS. Among the 88 reader rows, 22 state some link or image behaviour. Measured in: ALL [d d d s]; SHAPE [s/d s s s]; STORE-NS [d d d s].

**F17. Keeping up with a file under edit elsewhere is stated by about one in six; live preview of the product's own typing by one in four.** V31, ALL: reloads when the file changes on disk 56/496, both stated 26, preview updates as you type 98, manual refresh 2; undecidable 21; silent 294. Reload on disk change, with or without live preview: 82/496 in ALL, 32/204 in SHAPE, 35/145 in STORE-NS. Among the 88 reader rows, 25 state reload on disk change. By cell, reload with or without live preview: MAS 34/134, AT-T 17/132, SN 10/48, AT-M 12/63, AT-O 10/87, HB-C 9/44, HB-F 7/17, GH-V 7/21, GH-E 7/84. V31 had 2 cells the rule cannot decide ("detect" against "reload"; host editing). Measured in: ALL [d d d s]; SHAPE [s/d s s s]; STORE-NS [d d d s]; cells as in the register.

**F18. Appearance is the most-claimed reading feature after markdown forms: themes in 43%, light and dark in a third.** V32, ALL: themes provided 215/496, light and dark modes 170, font or size choice 104, custom stylesheet 65, follows the system appearance 59; undecidable 16; silent 166. Among the 88 reader rows, 49 claim themes or light and dark. V32 is weak (7 cells the rule cannot decide, adjusted agreement 0.80): "Dark Mode" alone and output themes are read two ways. Measured in: ALL [d d d s]; SHAPE [s/d s s s]; STORE-NS [d d d s].

**F19. Export: PDF in 40%, HTML in 31%.** V33, ALL: export to PDF 196/496, export to HTML 152, export to another named format 145, share or send 81, print 79, copy as rich text 39; silent 193. Among the 88 reader rows, 35 claim print, PDF or HTML. SHAPE and STORE-NS differ little: PDF 78/204 against 59/145, HTML 59/204 against 52/145. Measured in: ALL [d d d s]; SHAPE [s/d s s s]; STORE-NS [d d d s].

## Whether files stay local

**F20. Under half state where files are kept; of those that do, nearly all say local.** V14, ALL: local (stated) 124/496, local by default with optional upload 101, content leaves the device 13; undecidable 31; silent 227. One of the two local values: 82/204 in SHAPE, 60/145 in STORE-NS; among the 88 reader rows, 29. Network (V15), ALL: no telemetry or tracking (stated) 180/496, works offline 151, network for named features only 110, telemetry sent 54, account required 8, network required 2; silent 194. Of the 180, 101 are MAS rows (101/134), where the coded text is the developer's privacy declaration on the listing. V14 is weak (5 cells the rule cannot decide, adjusted agreement 0.89): sync to the user's own cloud fits no value. Measured in: ALL [d d d s]; SHAPE [s/d s s s]; STORE-NS [d d d s].

## Release recency and archival

**F21. Recency, by cell only.** V27(a) gives the latest release date as published. The table counts rows whose date names the year 2026; separate columns count dates published as relative ("1 day ago", "Today") or as month and day with no year. Capture was 2026-10-09.

| cell | year 2026 | relative | month and day, no year | silent |
|---|---|---|---|---|
| FH | 14/25 | 7 | 1 | 0 |
| SN | 38/48 | 2 | 0 | 0 |
| MAS | 31/134 | 19 | 55 | 15 |
| HB-C | 14/44 | 0 | 3 | 20 |
| VS | 9/19 | 0 | 0 | 3 |
| AT-T | 42/132 | 4 | 8 | 31 |
| AT-O | 48/87 | 2 | 6 | 16 |
| AT-M | 13/63 | 1 | 4 | 15 |
| AT-G | 2/40 | 1 | 0 | 11 |
| GH-E | 16/84 | 1 | 11 | 38 |
| GH-V | 3/21 | 0 | 3 | 10 |

V27(b), archived, deprecated or unmaintained (stated): ALL 37/496; AT-T 23/132, AT-M 11/63, AT-G 10/40, GH-E 8/84, HB-C 8/44, AT-O 3/87, SN 2/48, HB-F 2/17, FH 1/25, UA 1/13, GH-V 1/21, MAS 0/134. Actively maintained is stated by 12/496. Cadence (V26) is silent in 461/496: 3 state a schedule, 12 frequent updates, 7 no further releases, 9 a dated offer, 4 undecidable. The GitHub-topic cells are never set against the store cells on any of this, because the star floor selects for age. The AlternativeTo "last updated" dates are directory-page dates; whether they count as listing updates is a case the rule cannot decide (V27, 3 cells). The Glow list itself dates from 2024-10-13. Measured in: each cell, marked as in the register.

## AI-related claims

**F22. Three in ten comparables make an AI claim; one in twelve says it is made for reading or editing AI output.** V36, ALL: AI features in the product 91/496, works with AI agents or tools 74, made for reading or editing AI output 40, made with AI 10, no AI (stated) 9; undecidable 23; silent 314. At least one of the four positive claims: 153/496 in ALL, 52/204 in SHAPE, 46/145 in STORE-NS. Made for AI output: 14/204 in SHAPE, 17/145 in STORE-NS. By cell, made for AI output: MAS 19/134, AT-T 10/132, AT-M 7/63, SN 5/48, HB-C 4/44, GH-E 4/84, GH-V 3/21, AT-O 3/87, HB-F 2/17, with 2 each in AT-G and GH-P and 1 each in FH, GH-R and ACC. Within MAS, any AI claim is 33/82 of MAS-paid and 14/52 of MAS-free. Among the 88 reader rows, 15 say they are made for AI output and 7 that they work with agents. Readers of AI output named as a buyer class (V05) are 12/496 (finding 3). Measured in: ALL [d d d s]; SHAPE [s/d s s s]; STORE-NS [d d d s]; MAS-free and MAS-paid [d d d s].

## Further parameters the codebook codes

**F23. Help: documentation, an issue tracker and email lead; the issue tracker belongs to the shape-sharing population.** V34, ALL: documentation or guide 159/496, issue tracker 138, email or contact form 129, forum or community 80, paid or priority support 5, no support offered (stated) 2; silent 157. Issue tracker: 87/204 in SHAPE against 21/145 in STORE-NS. Email or contact form: 40/204 against 48/145. Measured in: ALL [d d d s]; SHAPE [s/d s s s]; STORE-NS [d d d s].

**F24. Who else uses it: presence of a usage figure only.** V35, ALL: a download, install or user count is claimed in 116/496 rows, a rating shown in 47, testimonials in 15, press quotes in 9, named customers in 3; undecidable 28; silent 310. No figure is compared across instruments. No MAS rating figure enters any finding; the 34 MAS rows showing a rating carry the store's field. Measured in: ALL [d d d s].

**F25. Names: most carry "markdown" or a function word.** V03, ALL: function word in name 218/496, markdown token in name 216, none of the above 194, maker name 7; undecidable 7. MAS: markdown token 118/134. GH-E: none of the above 43/84. Measured in: ALL [d d d s]; MAS, GH-E as in the register.

**F26. Most are offered as one program; editions belong to the store remainder.** V04, ALL: single program 314/496, one program in editions 100, family of programs 40, program and component 7, component only 0; undecidable 36. Editions: 9/204 in SHAPE against 50/145 in STORE-NS. V04 is the weakest variable of the second coding (9 cells the rule cannot decide): a bundled companion has no value, which is why 36 rows are undecidable. Measured in: ALL [d d d s]; SHAPE [s/d s s s]; STORE-NS [d d d s].

**F27. A held place is almost never stated; where a limit is stated it is per licence.** V25 (dimension 4), ALL: silent 441/496; per-licence use limit 31, no limit (stated) 14, capacity limit on buyers 6 (waitlists, closed betas), undecidable 4. In SHAPE, 201/204 are silent; in STORE-NS, 21/145 state a per-licence limit. Measured in: ALL [d d d s]; SHAPE [s/d s s s]; STORE-NS [d d d s]. This speaks to dimension 4, on which every population is marked shared.

**F28. The rows shaped like the operator on dimensions 1 to 3 include 28 readers.** A row is shaped like the operator here when it states no payment (V16(b), V23), states reach by clone or release download (V22), and names no sale mechanism other than sponsorship or "no sale taken" (V24). 176 rows of ALL meet this (204 weighted). 28 of them are readers (V09): auto-open-markdown-preview, essentialist, flycrys, glow, inlyne, instant-markdown, k1low-mo, mandown, marge, markdown-hot-reload, markdown-view, markdowser, markview-markdownviewer, markview-markview-reader, md-tui, md2term, mdcat, mdfried, mdp, mdserv, mdserve, mud-mark-up-or-down, qlcommonmark, quick-markdown-viewer, rivolink-leaf, shiba, simov-markdown-viewer and ttscoff-mmd-quicklook. This is a row-level marking, shared on D1 to D4 for each row named, drawn across cells. It is a list to place, not a rate.

## The instrument

**F29. The second coding agreed on three quarters of cells as written. Once layout is set aside, the agreement a reader should weigh is weakest on V06, V12, V13, V21, V04, V19 and V32.** Raw agreement over the 45-profile sample: 1252/1665 cells, 0.752 (second-coding.md). The lowest raw rates were V16 at 0.18, V27 at 0.33, V21 at 0.36 and V13 at 0.44. The corrections pass read all 413 listed differences (corrections.md):

- 266 were layout, not coding.
- 21 were first-coding errors, corrected in the corpus.
- 28 were second-coding errors, left as they stand.
- 98 were cases the frozen rule cannot decide, recorded as codebook weaknesses.

Adjusted agreement (layout discounted, no credit for corrections) is lowest on V06 at 0.67, then V12, V13 and V21 at 0.78, then V04, V19 and V32 at 0.80. It is 1.00 on V18, V25, V26 and V34. The variables with the most undecidable-rule cells are V04 (9), V13 (8), V06 (7), V32 (7), V19 (6), V12, V14 and V21 (5 each), and V07, V08 and V09 (4 each). The raw lows on V16 and V27 are mostly layout; their adjusted agreement is 0.96 and 0.91. Findings 2 (its V06 count), 5, 9, 10, 11, 12, 13, 17, 18, 20, 21 and 26 rest on a weak variable and say so. Measured in: the 45-profile sample; no dimension.

**F30. The corrections reached only the sampled rows; the rule gaps reach every row.** The 21 corrections touched only the 45 sampled profiles. The 98 cells the rule cannot decide are 98/1665 (5.9%) of the cells compared. The same gaps exist in the 383 rows outside the sample, at a rate no one has measured, so a count on a weak variable carries that uncertainty everywhere. In the corpus as a whole, the gaps show as undecidable counts: V04 36/496, V14 31/496, V29 70/496 (mostly unscoped "search"), V35 28/496 and V36 23/496. The first coding drifted on derived variables too (V22 is a classing of V21 and V12(a)), and the corrections restored that derivation only in the sample. The corpus was written in several cell layouts: bare values, single-letter tags such as "(p)", "a:" sub-field labels, and shell-quoting debris (`'"'"'` in place of an apostrophe). The counts here are read with the brief's value rule, element by element, matched to the codebook's value lists. A re-count by another parser should agree on values but may differ by a row where a clerk wrote a value outside the list's words (for example "install from store" for "install from a store", which is counted). Measured in: all coded rows; no dimension.

# Index

F1 corpus size. F2 audience by class. F3 the operator's three buyer rows. F4 reader against editor. F5 kinds. F6 platforms. F7 free share by cell. F8 price shapes, prices, licence, work use. F9 sale mechanism and invitations. F10 surfaces and reach. F11 units. F12 install, update, prerequisites. F13 markdown forms. F14 long-document navigation. F15 search. F16 links and images. F17 following a file under edit. F18 appearance. F19 export. F20 files local, network. F21 recency and archival. F22 AI claims. F23 support. F24 usage figures. F25 names. F26 one program or several. F27 place held. F28 operator-shaped rows and their readers. F29 second-coding agreement. F30 reach of the corrections and the rule gaps.

# Findings by buyer

Written under `briefs/synthesis-clerk-by-buyer.md`. `3-decisions/leading-buyers.md` found that no finding above breaks a variable down by buyer. Under each of its fifteen parameters it named the variable to cross with V05 (whom the page addresses) to separate a difference between buyers from a difference between cells. Findings 31 to 49 are those cross-tabulations. They are counts over codebook v1 as coded and corrected, and no row was recoded. `0-comparables/by-buyer.py` reads the two TSV files and prints every table cited here, and the reader can rerun it.

A text generator would read a gap between two buyer columns as what each buyer wants. A product designer first asks whether the gap belongs to a cell. Buyers are named mostly on Mac App Store listings and AlternativeTo entries, and those cells print some things whoever the buyer is.

## How the by-buyer counts are made

- **Buyer columns (V05).**
  - **D-only:** names developers and coders, not writers and authors.
  - **W-only:** names writers and authors, not developers.
  - **D+W:** names both. This is the documentation reader of `leading-buyers.md`.
  - **AI:** names readers of what AI agents write. It overlaps the first three where a row names both, which happens in 3 rows: inkdrop is also D-only, and markviewer and viewmd are also D+W.
  - **other:** names at least one class but none of developers, writers or AI readers. Every other buyer class is pooled here.
  - **silent:** V05 "not stated", each row counted once.
  - **undecidable:** V05 undecidable and nothing else (3 rows), shown in the script's tables.
- **Populations, weights and silence.** These are as in "How the counts are made" above. SHAPE has 204 rows, unweighted. ALL has 427 rows, weighted 496. Silence on a variable is counted once per row. A rate is given on a base of ten or more; under ten, the count is given and the base is called a handful.
- **Cell strata.** The script also crosses each variable inside four strata:
  - MAS: the Mac App Store cell, 134 rows.
  - MAS-free: SHAPE's Mac App Store rows, 52.
  - not-MAS: ALL outside the Mac App Store, 293 rows weighted 362.
  - AT: any AlternativeTo cell, 129 rows weighted 198.

  A buyer difference **survives the cell** when it holds between buyer columns inside one stratum. It **is the cell** when it vanishes there. The dimension marks are MAS, not-MAS and AT [d d d s]; MAS-free [d s s s]; SHAPE [s/d s s s]; ALL [d d d s].
- **Comparisons not made.** The list under "How the counts are made" stands. In addition:
  - No buyer column in one stratum is set against a buyer column in another.
  - The four AlternativeTo lists are pooled as one stratum. They are never set against each other or against a store.
  - V10 is read by buyer only inside one stratum or one population, never as one platform's buyers against another's through the cell.
  - No rate is given on a base under ten.
  - TCL is not pooled. Its one eligible row, shtmlview, names developers but sits in no application cell, so it is in no column.
- **Products behind the weights.** In ALL the columns hold:
  - D-only: 22 products, weighted 27.
  - W-only: 22 products, weighted 32.
  - D+W: 36 products, weighted 39.
  - AI: 12 products, weighted 12.

  In AT, W-only's weighted 22 is 12 products, 10 of them sampled at weight 2. D-only's 13 is 8 products, 5 of them sampled at weight 2.
- **Reading.** This reading counts a few more coded values than `taxonomy.md` did (finding 49).
- **Weak variables** are named from findings 29 and 30 where a finding rests on one.

**F31. In SHAPE, only the rows naming developers and writers together reach a base of ten. Developers alone, writers alone and readers of AI output are each a handful.**
- V05, SHAPE (204): D-only 9, W-only 4, D+W 19, AI 4 (markviewer is also D+W), other 18, silent 150, undecidable only 1.
- V05, ALL (496 weighted): D-only 27, W-only 32, D+W 39, AI 12, other 38, silent 348, undecidable only 3.

Every SHAPE figure below for D-only, W-only and AI is therefore a count on a handful. Leaving out the one overlap, the leading buyers' SHAPE rows number 35. Measured in: SHAPE [s/d s s s]; ALL [d d d s].

**F32. Each leading buyer column sits mostly in one cell.**
- **D+W:** 24 of its 39 weighted ALL rows are Mac App Store listings. In SHAPE, 16 of its 19 rows are store-only rows. 12 of those are MAS-free, and the other 4 are on Snap, Flathub, the Ubuntu archive and Homebrew (dillinger, easyeditor, formiko, markviewer). Its 3 GitHub-topic rows are solomd, thisis-developer-markdown-viewer and vaibhav-kakde-in-mdhero.
- **W-only:** 22 of its 32 weighted ALL rows are in the AlternativeTo cells (12 products), and 7 are in MAS. Its 4 SHAPE rows are jottr (FH), markdown (MAS), laogou717-md-wechat (GH-E) and tizuio-tizumark-markdown-editor (GH-V, GH-E).
- **D-only:** 13 of its 27 weighted ALL rows are in AT (8 products), and 5 are in MAS. Its 9 SHAPE rows are 3 GitHub-topic rows and 6 store-only rows, 3 of those MAS-free.
- **AI:** 6 of its 12 rows are MAS listings. The other 6 are on Homebrew (inkdrop, macmd-viewer, markviewer, mdserve), the Snap Store (inkdrop, markdown-hot-reload, markview-markview-reader) and AlternativeTo (inkdrop, macmd-viewer). Its 4 SHAPE rows are 2 MAS-free, 1 Snap and 1 Homebrew cask. None is a GitHub-topic row.
- **Shared on all four dimensions:** of the 32 SHAPE rows that name developers or writers, 8 are GitHub-topic rows (D-only 3, W-only 2, D+W 3). Of the 150 silent SHAPE rows, 71 are.

Measured in: cells as in the register; SHAPE [s/d s s s].

**F33. Developers and writers are mostly named together, and naming them together is a Mac App Store habit.**

V05, by how many rows name developers and writers:

| population | both | developers only | writers only | neither, a class named | silent | undecidable only | total |
|---|---|---|---|---|---|---|---|
| SHAPE | 19 | 9 | 4 | 21 | 150 | 1 | 204 |
| ALL (weighted) | 39 | 27 | 32 | 47 | 348 | 3 | 496 |

- In SHAPE, a row that names developers also names writers in 19 of 28. A row that names writers also names developers in 19 of 23.
- In ALL, the same shares are 39 of 66 and 39 of 71.
- Inside MAS, 24 of the 36 rows naming either name both. Outside MAS, 15 of the 62 weighted rows naming either name both. Most of the rest are writers alone or developers alone on AlternativeTo.
- The documentation reader as a market phrase is therefore mostly what App Store listings print.

Measured in: SHAPE [s/d s s s]; ALL [d d d s]; MAS and not-MAS [d d d s].

**F34. Parameter 1, the name: the markdown token follows the cell, not the buyer.** V03, markdown token in name:

| | D+W | silent |
|---|---|---|
| ALL | 25/39 (64%) | 148/348 (43%) |
| inside MAS | 21/24 (88%) | 75/86 (87%) |
| outside MAS | 4/15 (27%) | 73/262 (28%) |
| SHAPE | 11/19 (58%) | 58/150 (39%) |
| MAS-free | 10/12 | 26/31 |

- 10 of D+W's 11 SHAPE rows with the token are MAS-free.
- Handfuls in SHAPE: D-only 6 of 9, W-only 2 of 4, AI 2 of 4.
- In ALL: D-only 10/27 (37%), W-only 14/32 (44%), AI 6/12, 5 of the 6 being its MAS rows.
- The one gap inside a stratum is developers alone in AT: 1/13 weighted carry the token, against W-only 8/22 and AT silent 36/135. That rests on 8 products.
- The difference between buyers does not survive the cell.

V03 is not a weak variable. Measured in: ALL, MAS, not-MAS [d d d s]; SHAPE [s/d s s s]; MAS-free [d s s s].

**F35. Parameter 2, where it is got: page surface and route differ by buyer only as the cells differ.**

V20, ALL, D+W against silent:
- Application store listing: 29/39 (74%) against 141/348 (41%).
- Code repository page: 8/39 (21%) against 175/348 (50%).

Every MAS row is a store listing. Outside MAS:
- Store listing: 5/15 (33%) against 55/262 (21%).
- Repository page: 8/15 (53%) against 169/262 (65%).

In SHAPE, D+W's repository page is 5/19 (26%) against 106/150 (71%), and its store listing is 15/19, 12 of them MAS-free.

V22 reach through a package repository or manager:

| | D+W | silent |
|---|---|---|
| ALL | 7/39 (18%) | 132/348 (38%) |
| outside MAS | 7/15 (47%) | 130/262 (50%) |

That gap is the cell.
- **AI:** package registry page 5/12 against 53/348 (15%), and reach by package manager 6/12. These are its Homebrew and Snap rows.
- **D-only against W-only:** reach by package manager is 10/27 (37%) against 6/32 (19%) in ALL. Inside AT it is 3/13 against 5/22, so it does not survive.
- **SHAPE handfuls:** D-only package manager 4, release download 4, clone 2 and store 3 of 9. W-only release 2, clone 2, store 1 and package manager 0 of 4. AI package manager 2, release 2 and store 1 of 4.

V22 is a classing of V21, a weak variable (adjusted agreement 0.78; finding 29). Measured in: ALL, MAS, not-MAS [d d d s]; SHAPE [s/d s s s]. This speaks to dimension 1.

**F36. Parameter 3, the unit and the install: writers alone are offered a store install more than developers alone, and that holds inside AlternativeTo. Developers alone lead on a package-manager command, but that lead does not hold there.**

V12(a), store install:

| | W-only | D+W | D-only | silent |
|---|---|---|---|---|
| ALL | 16/32 (50%) | 16/39 (41%) | 4/27 (15%) | 83/348 (24%) |
| inside AT | 12/22 (55%) | | 3/13 (23%) | 36/135 (27%) |
| inside MAS | | 11/24 (46%) | | 28/86 (33%) |

The AT figures rest on 12 and 8 products.

V12(a), package-manager command:

| | D-only | W-only | D+W | silent |
|---|---|---|---|---|
| ALL | 10/27 (37%) | 4/32 (12%) | 7/39 (18%) | 126/348 (36%) |
| inside AT | 3/13 | 3/22 | | |

- **SHAPE:** package-manager command D-only 4 of 9, W-only 0 of 4, D+W 6/19 (32%) against silent 56/150 (37%). Store install D+W 7/19 (37%, 5 of them MAS-free) against 42/150 (28%).
- **V19, a package the system maintains:** D-only 5/27, W-only 0/32, D+W 5/39, silent 91/348 (26%) in ALL. In SHAPE: D-only 3 of 9, W-only 0 of 4, D+W 5/19 (26%) against 41/150 (27%).
- **V12(b), how updates arrive, is silent nearly everywhere:** D+W 38/39, W-only 26/32, D-only 22/27, AI 7/12 and silent 286/348 in ALL; D+W 18/19 in SHAPE.

V12 (adjusted 0.78) and V19 (0.80) are weak variables. Measured in: ALL, AT, MAS [d d d s]; SHAPE [s/d s s s]. This speaks to dimensions 1 and 3.

**F37. Parameter 4, the cost: rows naming writers alone are paid more often than any other column, and the gap holds inside AlternativeTo, where most of them sit. In SHAPE every leading buyer column is free by construction.**

Paid, by the finding 7 rule:

| | W-only | AI | D+W | other | D-only | silent |
|---|---|---|---|---|---|---|
| ALL | 22/32 (69%) | 6/12 | 17/39 (44%) | 16/38 (42%) | 11/27 (41%) | 92/348 (26%) |
| inside AT | 16/22 (73%) | | 6/11 (55%) | 10/16 (62%) | 7/13 (54%) | 42/135 (31%) |

- **Inside MAS:** W-only 6 of 7 are paid, and D+W is 12/24 (50%) against 55/86 (64%) for silent rows.
- **V16(b), inside AT:** one-time purchase W-only 13/22 against D-only 4/13 and silent 17/135. Subscription 7/22 against 3/13 and 16/135.
- **AI:** 4 of its 6 MAS rows are paid. One-time purchase 5/12 and freemium 3/12 in ALL.
- **SHAPE:** D-only 8 of 9 free and 1 silent on price, W-only 3 of 4 and 1, D+W 18/19 and 1, AI 4 of 4. D+W states a price more often than the silent rows (18/19 against 111/150, 74%) only because 12 of its 19 rows are MAS-free listings, whose price field is always filled.
- **V24 and V07 in SHAPE:**
  - No sale taken: D-only 3 of 9, D+W 7/19 (37%), silent 34/150 (23%).
  - Sponsor or donate: D-only 4 of 9, W-only 0 of 4, D+W 4/19 (21%), silent 28/150 (19%).
  - Star: D-only 2 of 9.
- **V07 in ALL:** sponsor or donate D-only 6/27 (22%) against W-only 1/32.

V07 and V24 have cells the rule cannot decide (finding 29). Measured in: ALL, AT, MAS [d d d s]; SHAPE [s/d s s s]. This speaks to dimensions 2 and 3.

**F38. Parameter 5, licence and work use: the documentation reader's silence on licence comes from the App Store. Writers alone and developers alone state proprietary terms alike inside AlternativeTo. Work use is unstated for every buyer.**

V16(c), named open-source licence:

| | D+W | silent |
|---|---|---|
| ALL | 7/39 (18%) | 190/348 (55%) |
| outside MAS | 7/15 (47%) | 185/262 (71%) |
| SHAPE | 4/19 (21%) | 109/150 (73%) |
| MAS-free | 0/12 | 4/31 |

- D+W is silent on licence in 25/39, and 22 of those 25 are MAS rows. Inside MAS, licence silence is 22/24 for D+W and 71/86 for silent rows.
- The gap that remains outside MAS rests on 12 products.
- SHAPE handfuls: open-source D-only 6 of 9, W-only 3 of 4, AI 1 of 4.
- Proprietary: W-only 16/32 (50%) and D-only 10/27 (37%) in ALL. Inside AT they are 14/22 and 9/13, so the two do not separate.
- V18 is silent for D-only 23/27, W-only 29/32, D+W 39/39, AI 11/12 and silent rows 338/348. A team or business licence is offered by D-only 4/27, W-only 2/32 and other 8/38. In SHAPE, every leading-buyer row is silent on V18.

Measured in: ALL, not-MAS, AT [d d d s]; SHAPE [s/d s s s]; MAS-free [d s s s].

**F39. Parameter 6, platforms and prerequisites: the documentation reader's lean to macOS, and away from Windows and Linux, is the Mac App Store. Outside it, no buyer column differs from the silent rows.**

V10, D+W against silent:

| | macOS | Windows | Linux |
|---|---|---|---|
| SHAPE | 15/19 (79%) against 84/150 (56%) | 3/19 (16%) against 53/150 (35%) | 5/19 (26%) against 63/150 (42%) |
| outside MAS | 8/15 (53%) against 149/262 (57%) | 6/15 (40%) against 121/262 (46%) | 7/15 (47%) against 144/262 (55%) |

12 of D+W's 15 macOS rows in SHAPE are MAS-free.
- **SHAPE handfuls:** D-only macOS 7, Windows 4, Linux 4 of 9. W-only 3, 3 and 1 of 4. AI 3, 1 and 1 of 4.
- **Linux, D-only against W-only:** 10/27 (37%) against 7/32 (22%) in ALL; 4/13 against 4/22 inside AT. It does not survive.
- **AI:** iOS 6/12, all of them its MAS rows.
- **V11:**
  - Minimum operating-system version: D+W 32/39 (82%) against 144/348 (41%). Every MAS row states one (86/86 silent rows, 24/24 D+W), so this is the cell.
  - None needed, stated: D+W 4/39 against 7/348. 3 of the 4 are AlternativeTo rows (dillinger, zerdo). In SHAPE, 2/19 against 5/150.
  - Runtime or interpreter named in SHAPE: D-only 1, W-only 2 of 4, D+W 3/19 (16%) against 26/150 (17%).

V11 has cells the rule cannot decide (finding 29). Measured in: SHAPE [s/d s s s]; not-MAS, MAS, AT [d d d s]; MAS-free [d s s s].

**F40. Parameter 7, markdown forms: readers of AI output claim more forms than any other column, both in and out of the App Store. Inside the App Store, no form separates the documentation reader from the silent rows.**

AI against silent, in ALL and inside MAS:

| form | AI, ALL | silent, ALL | AI inside MAS | silent inside MAS |
|---|---|---|---|---|
| tables | 11/12 | 137/348 (39%) | 6 of 6 | 54/86 (63%) |
| diagrams | 10/12 | 115/348 (33%) | 5 of 6 | 37/86 (43%) |
| syntax-highlighted code blocks | 10/12 | 86/348 (25%) | 5 of 6 | 29/86 (34%) |
| GitHub Flavored Markdown | 8/12 | 75/348 (22%) | 3 of 6 | 22/86 (26%) |
| task lists | 8/12 | 94/348 (27%) | | |
| math | 7/12 | 130/348 (37%) | 4 of 6 | 34/86 (40%) |
| footnotes | 5/12 | 50/348 (14%) | | |

AI in SHAPE: tables 4, GFM 3, code blocks 3, task lists 3, diagrams 2 and math 2 of 4.

D+W against silent:

| form | SHAPE | inside MAS |
|---|---|---|
| tables | 9/19 (47%) against 55/150 (37%) | 17/24 against 54/86 |
| task lists | 9/19 (47%) against 44/150 (29%) | 10/24 against 38/86 |
| diagrams | 7/19 (37%) against 56/150 (37%) | 10/24 against 37/86 |
| math | 6/19 (32%) against 67/150 (45%) | 7/24 against 34/86 |
| GFM | 4/19 (21%) against 37/150 (25%) | |

The SHAPE gaps are the cell.

D-only against W-only:
- **Code blocks:** 12/27 (44%) against 3/32 (9%) in ALL, and 6/13 against 0/22 inside AT. This survives there, on 8 and 12 products. The SHAPE handfuls run the other way: D-only 4 of 9, W-only 3 of 4.
- **Math:** W-only 14/32 (44%) against D-only 10/27 (37%); 13/22 against 5/13 inside AT.
- **Other named flavour:** W-only 4/32 against D-only 1/27; 3/22 against 0/13 inside AT.

V13(b) is silent in at least 97% of every column, and in all 35 leading-buyer rows in SHAPE.

V13 is weak (adjusted 0.78, 8 cells the rule cannot decide), and "markdown named, no form named" is its least firm value. Measured in: ALL, MAS, AT [d d d s]; SHAPE [s/d s s s].

**F41. Parameter 8, reader or editor: the readers sit with the documentation reader and the AI reader, and that holds inside the App Store. A row naming writers alone or developers alone is an editor.**

V09, readers (both reader values), in ALL:

| | AI | D+W | D-only | W-only | other | silent |
|---|---|---|---|---|---|---|
| readers | 9/12 | 12/39 (31%) | 2/27 | 1/32 | 2/38 | 62/348 (18%) |

Reader, stated read-only: AI 8/12, D+W 7/39 (18%), silent 6/348 (2%).

| | D+W | silent |
|---|---|---|
| readers inside MAS | 9/24 (38%) | 15/86 (17%) |
| readers in SHAPE | 5/19 (26%) | 27/150 (18%) |
| readers in MAS-free | 5/12 | 7/31 |

- All 5 D+W readers in SHAPE are MAS-free rows.
- Inside MAS, AI is read-only in 5 of 6.
- SHAPE handfuls: AI read-only 2 of 4, D-only reader 1 of 9, W-only 0 of 4.
- Editors (either editor value): W-only 31/32, D-only 25/27.

V09 has 4 cells the rule cannot decide (finding 29). Measured in: ALL, MAS [d d d s]; SHAPE [s/d s s s]; MAS-free [d s s s].

**F42. Parameter 9, keeping up with a file edited elsewhere: reload on a change on disk is stated mostly by the AI reader's Homebrew and Snap rows, not its App Store rows. The documentation reader does not differ from other App Store rows.**

V31, reloads when the file changes on disk, alone or with live preview, in ALL: AI 6/12, D+W 9/39 (23%), W-only 6/32 (19%), D-only 3/27 (11%), silent 56/348 (16%).
- **AI:** 5 of its 6 rows outside MAS state reload (macmd-viewer, markdown-hot-reload, markview-markview-reader, markviewer, mdserve). Only 1 of its 6 MAS rows does (md-flow-markdown-reader), against 24/86 of silent MAS rows.
- **D+W:** 6/24 against 24/86 inside MAS. 5/19 (26%) against 24/150 (16%) in SHAPE, but 3/12 against 10/31 in MAS-free, so the SHAPE gap is the cell.
- **SHAPE handfuls:** AI 2 of 4, D-only 1 of 9, W-only 1 of 4.
- **Live preview of the product's own typing:** D+W 13/39, W-only 9/32, D-only 8/27, AI 0/12, silent 61/348 (18%).

V31 has 2 cells the rule cannot decide, and finding 17 already marks it. Measured in: ALL, MAS, not-MAS [d d d s]; SHAPE [s/d s s s]; MAS-free [d s s s].

**F43. Parameter 10, a long document: an outline is claimed most by the AI reader and the documentation reader. Inside the App Store the documentation reader's lead is nil. Outside it the lead is large, but rests on 8 products.**

V28, outline, in ALL: AI 9/12, D+W 22/39 (56%), D-only 9/27 (33%), W-only 8/32 (25%), other 7/38 (18%), silent 106/348 (30%).

| D+W against silent | outline |
|---|---|
| inside MAS | 11/24 (46%) against 40/86 (47%) |
| outside MAS | 11/15 (73%) against 66/262 (25%) |
| inside AT | 9/11 against 32/135 (24%); D-only 4/13, W-only 4/22 |
| SHAPE | 9/19 (47%) against 50/150 (33%) |
| MAS-free | 5/12 against 9/31 |

- AI claims an outline in 5 of its 6 MAS rows.
- SHAPE handfuls: AI 3 of 4, D-only 4 of 9, W-only 1 of 4.
- Folding of sections: AI 0/12, D+W 5/39, silent 20/348.

Measured in: ALL, MAS, not-MAS, AT [d d d s]; SHAPE [s/d s s s]; MAS-free [d s s s].

**F44. Parameter 11, finding a word: search within the document is claimed most by the AI reader, and that holds inside the App Store. Find and replace belongs to writers alone, and that holds inside AlternativeTo.**

V29, in ALL:

| | AI | D-only | D+W | W-only | silent |
|---|---|---|---|---|---|
| search within the document | 6/12 | 8/27 (30%) | 9/39 (23%) | 7/32 (22%) | 62/348 (18%) |
| find and replace | 0/12 | 5/27 (19%) | 2/39 (5%) | 10/32 (31%) | 41/348 (12%) |

- **Search within the document inside MAS:** AI 4 of 6 against 23/86 (27%); D+W 8/24.
- **Find and replace inside AT:** W-only 6/22 against D-only 3/13 and silent 9/135.
- **Regular-expression search:** W-only 5/32; every other column 2 or fewer.
- **SHAPE handfuls:** within the document D-only 3 of 9, W-only 2 of 4, AI 3 of 4, and D+W 4/19 (21%) against 24/150 (16%). Find and replace D-only 3 of 9, W-only 2 of 4, and D+W 2/19 against 25/150.
- **Weakness:** an unscoped "search" codes undecidable (finding 30). That is D-only 6/27 and D+W 4/39, so these counts are soft.

Measured in: ALL, MAS, AT [d d d s]; SHAPE [s/d s s s].

**F45. Parameter 12, network and files: every named buyer states that files stay local more often than the silent rows. Inside the App Store only the AI reader and the documentation reader keep that lead, and inside SHAPE's App Store rows neither does.**

V14, local (stated), in ALL: AI 7/12, W-only 15/32 (47%), D+W 16/39 (41%), other 12/38 (32%), D-only 7/27 (26%), silent 68/348 (20%).
- **Inside MAS:** D+W 12/24 (50%) against 29/86 (34%); AI 5 of 6; W-only 3 of 7.
- **Inside AT:** W-only 11/22 (50%), D-only 3/13, D+W 3/11, silent 21/135 (16%). V14 is silent in 10/63 weighted AT rows that name any class, against 70/135 of AT's silent rows. So in that cell, naming a buyer goes with saying where files are kept.
- **In SHAPE:** D+W 6/19 (32%) against 30/150 (20%), but 5/12 against 14/31 in MAS-free, so that is the cell.
- **SHAPE handfuls:** AI 3 of 4; D-only 2 of 9, plus 3 local with optional upload; W-only 1 of 4.
- **V15, no telemetry inside MAS:** D+W 20/24 against 63/86. That is the store's privacy declaration (finding 20).
- **V15, telemetry sent:** D+W 6/19 against 6/150 in SHAPE, and 4/12 against 4/31 in MAS-free. This survives the cell on 12 rows.

V14 is weak (adjusted 0.89, 5 cells; sync to the user's own cloud fits no value). Measured in: ALL, MAS, AT [d d d s]; SHAPE [s/d s s s]; MAS-free [d s s s].

**F46. Parameter 13, appearance: writers alone claim light and dark modes more than developers alone, and developers alone claim a custom stylesheet more. Both differences hold inside AlternativeTo, on 12 and 8 products.**

V32, in ALL and inside AT:

| | W-only | D-only | D+W | AI | silent |
|---|---|---|---|---|---|
| light and dark, ALL | 19/32 (59%) | 7/27 (26%) | 18/39 (46%) | 8/12 | 110/348 (32%) |
| light and dark, inside AT | 12/22 | 2/13 | | | 43/135 (32%) |
| custom stylesheet, ALL | 3/32 (9%) | 7/27 (26%) | 2/39 (5%) | | 48/348 (14%) |
| custom stylesheet, inside AT | 1/22 | 5/13 | | | 21/135 (16%) |

- Follows the system appearance: W-only 7/32, D-only 2/27, AI 5/12.
- Font or size choice: W-only 12/32 (38%) against D-only 4/27 (15%). Inside AT it is 5/22 against 2/13, too close to separate.
- Themes: 44% to 58% in every named column, 40% in silent rows.
- SHAPE handfuls: W-only themes 4 of 4 and font 3 of 4; D-only light and dark 3 of 9 and custom stylesheet 1 of 9.
- D+W custom stylesheet in SHAPE: 0/19 against 25/150 (17%). In MAS-free it is 0/12 against 1/31, so that is the cell.

V32 is weak (adjusted 0.80, 7 cells the rule cannot decide). Measured in: ALL, AT [d d d s]; SHAPE [s/d s s s]; MAS-free [d s s s].

**F47. Parameter 14, print and export: writers alone claim export to other formats and sending on more than any other column. The lead holds inside both the App Store and AlternativeTo. In SHAPE the writers are four rows, and the documentation reader's App Store rows claim export less than other App Store rows.**

V33, in ALL:

| | W-only | D-only | D+W | AI | silent |
|---|---|---|---|---|---|
| another named format | 21/32 (66%) | 12/27 (44%) | 11/39 (28%) | 1/12 | 98/348 (28%) |
| share or send | 13/32 (41%) | 5/27 | 5/39 | | 51/348 (15%) |
| HTML | 16/32 (50%) | | | | 99/348 (28%) |
| PDF | 17/32 (53%) | 13/27 (48%) | 18/39 (46%) | | 128/348 (37%) |

- **Inside AT:** another format W-only 14/22 against D-only 6/13 and silent 38/135. Share or send 11/22 against 0/13 and 22/135.
- **Inside MAS:** W-only 6 of 7 each for PDF, HTML and another format, against 47/86, 32/86 and 36/86 for silent rows.
- **Print:** AI 5/12, D+W 10/39 (26%), silent 49/348 (14%). Inside MAS, D+W 8/24 against 22/86.
- **SHAPE handfuls:** W-only another format 3 of 4, HTML 2, PDF 1 and copy as rich text 2; D-only PDF 5 of 9.
- **D+W in SHAPE:** PDF 8/19 (42%) against 57/150 (38%). Silent on V33 in 9/19, and in 8/12 in MAS-free against 8/31 of silent rows.

Measured in: ALL, MAS, AT [d d d s]; SHAPE [s/d s s s]; MAS-free [d s s s].

**F48. Parameter 15, one thing or several: none of the 35 leading-buyer rows in SHAPE is offered in editions. In ALL, editions are commoner where any buyer is named, and inside the App Store the documentation reader is offered in editions less often than other rows.**

V04, one program in editions, in ALL: W-only 10/32 (31%), D-only 7/27 (26%), D+W 9/39 (23%), AI 3/12, silent 62/348 (18%).
- **Inside MAS:** D+W 6/24 (25%) against 27/86 (31%); W-only 5 of 7.
- **Inside AT:** D-only 6/13, W-only 6/22, D+W 4/11, silent 30/135 (22%).
- **SHAPE:** single program D-only 8 of 9, W-only 4 of 4, D+W 18/19, AI 3 of 4 (one undecidable). Editions are 0 in all four columns, against 7/150 of silent rows.

V04 is the weakest variable (9 cells the rule cannot decide; 36 rows undecidable overall, 3 of the 12 AI rows). Measured in: ALL, MAS, AT [d d d s]; SHAPE [s/d s s s].

**F49. The instrument: this reading counts a few more coded values than `taxonomy.md`. The buyer columns move by one row.**

V05 in ALL counts these classes higher than finding 2:
- developers 66 (finding 2: 64)
- students 44 (42)
- note-takers 15 (13)

The cause is the reader, not the coding. Three AlternativeTo-sampled rows, each at weight 2, separated their V05 values with a single "|": phasoric, ownsync-note and pocketmark. The earlier count read that as text. Only phasoric changes buyer column, into developers alone.

The same layout, and values joined inside one element ("Windows, macOS"; "tables, task lists, footnotes"), raise this reading's ALL totals above the taxonomy's on other variables:
- V03 function word in name: 232 against 218 (+14). The cause of part of this surplus was not traced, because the earlier count's code is not open to this clerk.
- V13(a) task lists: +13.
- Math: +12.
- V10 Linux: +11.
- V13(a) diagrams: +10.
- V33 another named format: +10.

SHAPE moves by at most 5. Four counts come out lower: "markdown named, no form named" (127 against 131), host program's extension manager (21 against 22), the system package (107 against 108), and silence by one row on several variables. SHAPE (204), STORE-NS (145) and the price status are reproduced exactly: V16(b) free 248 and silent 97, and V23 identical.

So the by-buyer tables and findings 2 to 28 may disagree by these amounts. Neither reading recodes anything, and `by-buyer.py` prints both readings of V05. Measured in: all coded rows; no dimension.

## Index of the findings by buyer

- F31: bases by buyer.
- F32: the cells each buyer sits in.
- F33: developers and writers named together.
- F34: name.
- F35: surface and reach.
- F36: unit and install.
- F37: cost.
- F38: licence and work use.
- F39: platforms and prerequisites.
- F40: markdown forms.
- F41: reader or editor.
- F42: keeping up with a file.
- F43: long-document navigation.
- F44: search.
- F45: files local and network.
- F46: appearance.
- F47: print and export.
- F48: one program or several.
- F49: this reading against the taxonomy's.
