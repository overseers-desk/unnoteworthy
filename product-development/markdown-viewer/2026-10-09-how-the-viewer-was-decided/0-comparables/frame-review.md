---
title: "Frame review: the adversarial read before collection"
date: 2026-10-09
method: "SAGE Survey section 1 step 5, under briefs/frame-reviewer.md; reads the shape note, the per-list TSVs and coverage notes, frame.tsv, frame-cells.md and merge-frame.py"
---

# Frame review

The frame as handed over: 1,531 comparables from 1,852 list rows, 509 with at least one cell marking them in. The frame as collection may use it, after the duplicate resolutions, the undecidable rule and the verdicts below: **1,502 comparables, 534 with an in-membership, 522 of them in a cell that passes, and 449 page sets to collect** (the 522 less the 73 that the AlternativeTo sampling rule leaves out).

A text generator reading these lists would count every row that says "markdown" and report prevalence across the union. A product designer has to know which lists stand for a place a buyer chooses from, which are shaped by a cap or a crowd, and which rates can be set against an operator who ships a free script by `git clone`. This review answers the second.

## 1. Verdicts per cell

Counts are comparables after the duplicate resolutions (section 3) and the undecidable rule (section 4). "Collect" is the number of comparables collected because of that cell's in-membership; a comparable in several cells is collected once.

| cell | list as built (in / out / undecidable) | after review (in / out) | collect | verdict | condition or reason |
|---|---|---|---|---|---|
| Flathub (search "markdown") | 25 / 17 / 6 | 27 / 21 | 27 | go | Census of the 48 search hits. Rates read "among Flathub apps the search returns for 'markdown'". Price is not stated by the list; licence is not price. Verification is provenance only (already so). |
| Mac App Store (search "markdown", macSoftware) | 133 / 26 / 11 | 135 / 35 | 135 | conditional | Census of the 170 returned entries, not of the store's markdown apps. (a) `userRatingCount` is not demand: all 55 Mac-only listings (`mt=12`) report 0, an instrument artefact, so no rating figure from this cell enters any finding. (b) 115 of 170 entries are iPhone/iPad or universal listings; the collector records `supportedDevices` and every rate is also given for the Mac-only listings. (c) Free and paid rows are reported separately (dimension 2). |
| Snap Store (search "markdown") | 50 / 40 / 10 | 52 / 47 | 52 | conditional | Exactly 100 results with no paging and an undisclosed ranking: neither a census nor a stated-rule sample. Rates are labelled "among the first 100 the Snap search returns, ranking undisclosed" and are never set against Flathub or any census cell. `prices={}` is recorded as "price not stated", never as free. No install figure exists, so no popularity statement. |
| alternativeto:Typora | 124 / 22 / 75 | 139 / 82 | 95 | conditional | Rule R1 struck (section 4); the AlternativeTo sampling rule (section 5) applies; R2 was applied by script on a blurb, so the collector applies the brief's eligibility sentence on the product's own page and records any reassignment. |
| alternativeto:Obsidian | 86 / 51 / 234 | 92 / 279 | 55 | conditional | As Typora. The 234 R3 rows are a note-taking and workspace population whose blurb is silent on Markdown; they resolve out (section 4), so this list stands for the note-taker buyer only through its 92. |
| alternativeto:Marked (entry for Marked) | 65 / 9 / 5 | 73 / 6 | 49 | conditional | As Typora. The slug is `/software/marked/`, recorded as the brief's list with the doubt the coverage note states. |
| alternativeto:Glow | 45 / 4 / 3 | 48 / 4 | 32 | conditional | As Typora. The page was last updated 2024-10-13; rates are dated to that list, not to 2026. |
| awesome-claude-code | 1 / 14 / 15 | 2 / 28 | 2 | conditional | Census of one curator's list of Claude Code tools, not of readers of agent output. The two in rows (Nimbalyst, FlyCrys) are collected; no rate is computed on a cell of 2. The coverage note's finding (no entry is a Markdown viewer for agent output) stands as a finding about the list. |
| chrome-web-store | 12 / 4 / 2 | 14 / 4 | 0 | no-go | The first ten results of two queries behind an unread continuation token: a search hit with no denominator (step 2). Its rows go to the declared convenience list. Two of its products are collected through other cells (md-reader, Markdown Here); their Chrome membership is provenance only. |
| debian:apt-cache search markdown | 10 / 321 / 13 | 14 / 330 | 14 | conditional | The list is the Ubuntu 25.04 (plucky) archive index of 2026-09-23 on one host, past end of life; the cell is renamed "Ubuntu 25.04 archive, apt-cache search markdown" in every finding. `typora` and `marktext` (local .deb on the host) are not archive members and count in no rate of this cell. No install or recency figure is drawn from it. |
| github-topics:markdown-editor | 67 / 41 / 37 | 85 / 60 | 85 | conditional | Census under the stated star floor (stars >= 200; 145 of 2,691 repositories). Rates read "among repositories with the topic and 200 stars or more" and never stand for the topic. No age or activity comparison against store cells (the floor favours old projects). |
| github-topics:markdown-viewer | 18 / 5 / 5 | 21 / 7 | 21 | conditional | As markdown-editor (28 of 1,009). |
| github-topics:markdown-preview | 5 / 0 / 0 | 5 / 0 | 5 | conditional | As markdown-editor (5 of 220). Too small for a rate; report counts only. |
| github-topics:markdown-reader | 4 / 0 / 1 | 5 / 0 | 5 | conditional | As markdown-editor (5 of 132). Too small for a rate; report counts only. |
| homebrew:cask | 43 / 1 / 4 | 45 / 2 | 45 | conditional | Census of casks whose description contains "markdown"; 2,649 casks carry no description and cannot be seen. Install figures are Homebrew's opt-out analytics, CI included; quote them as published, never as users. `typora` and `typora@dev` are one comparable. |
| homebrew:formula | 15 / 54 / 4 | 17 / 56 | 17 | conditional | As cask. The formula `marked` (a JavaScript parser) is not the Marked app and is split from it. |
| tcl-wiki-markdown | 5 / 2 / 6 | 5 / 8 | 5 | conditional | Admits a different buyer (developers embedding a view) under a different eligibility (a component built into a program). Never pooled with application cells. Census of a 2022 wiki page; report counts, not rates. |
| tcl-wiki-markdown; tklib | 1 / 0 / 0 | 1 / 0 | 1 | conditional | Not a cell: a merge-label artefact for shtmlview, which sits on the wiki page and in tklib. Fold into tcl-wiki-markdown with tklib as a second membership. |
| teatotal | 1 / 0 / 0 | named row | 0 | no-go | A one-entry cell from a shelf the coverage note could not attribute, whose sole entry (tkdown) is described as rendering chat and transcript bodies, which is the operator's own buyer row. The repository's standing instructions name teatotal as the upstream whose module releases the operator vendors, so tkdown is the operator's supply, not a comparable. It is collected as a named row outside the draw (step 5): coded, excluded from every numerator and denominator. |
| vscode | 13 / 64 / 23 | 20 / 80 | 20 | conditional | A top-N cut stated as a mechanical rule with the uncapped count beside it (first 100 by installs of 4,720): a sample of the head, declared as such. Rates describe the head only. VS Code's built-in preview, the strongest incumbent for this buyer, is not on the list; no finding may read the cell's prevalence as the market's. Installs include bundled and auto-installed extensions. |

No cell carries an eligibility or cell rule built on a status mark. Flathub verification and Snap publisher validation are kept as provenance and stay so; AlternativeTo's paid "Official Partner" placement was correctly kept out of the list. Nothing to strike.

## 2. Forbidden comparisons

The findings may not make these comparisons, because the list architecture is confounded with the dimension compared.

1. **Store cells against the operator on dimensions 1 to 3.** Every rate from Mac App Store, Flathub, Snap, Homebrew, the Ubuntu archive, VS Code and AlternativeTo is marked *differs* on reach, payment before reach and sale. The sub-population that shares the operator's shape is the GitHub-topic cells and the free rows of a cell that states price; at present only the Mac App Store states price (106 free of 133 as listed). Flathub, Snap, Homebrew and VS Code state none, so their "free rows" cannot be drawn until collection records price from the product's page.
2. **Paid share across cells.** Only the Mac App Store states a price; AlternativeTo states a licence line; Flathub states a licence; Snap states `{}`. No comparison of paid share between any two cells.
3. **Popularity across cells.** Homebrew installs (opt-out, CI-inflated), Flathub monthly installs, VS Code installs (bundles counted), GitHub stars, AlternativeTo likes and Chrome rounded users are six instruments. No figure from one is set against another, and Mac App Store rating counts are used nowhere (zero for every Mac-only listing).
4. **Head against whole.** VS Code (top 100 by installs) and Snap (first 100, undisclosed rank) against any census cell, on any prevalence.
5. **Starred against unstarred.** GitHub-topic cells (>= 200 stars) against store cells on age, activity, maintenance or release recency: the floor selects for age.
6. **Linux store against Linux store.** Snap against Flathub on any prevalence: one is a capped ranking, the other a census of hits.
7. **AlternativeTo list against AlternativeTo list.** Typora, Obsidian, Marked and Glow lists are anchored on four products whose kind and platform tilt their entries (editors, note-taking, Mac previewers, terminal tools). No comparison between them (for example "terminal readers' tools do X more than writers' tools"), and none between an AlternativeTo cell and a store on platform or price.
8. **Platform through the cell.** Mac App Store (Mac and iOS), Flathub, Snap and the Ubuntu archive (Linux), Homebrew (Mac and Linux command line): platform is the list. No finding states that one platform's products do something more than another's from cell rates.
9. **Embedding cell with application cells.** tcl-wiki-markdown (and shtmlview's tklib membership) is never pooled with or compared to an application cell.
10. **"Markdown apps on platform X".** Every store and package cell was drawn by the word "markdown" in a description or search index; products that do not say the word are absent. No cell's count is reported as the number of Markdown applications on its platform.
11. **Pooling without de-duplication.** A comparable in several cells counts once in any pooled rate and once in each cell's own rate; the AlternativeTo sampled stratum carries weight 2 in any rate that includes it (section 5).

## 3. Duplicate resolutions ordered

The merge joined on normalised name or shared identifier. It made false joins of different products, and left true duplicates apart. The collector applies these before collection; the counts in this review already do.

**Split (false joins: different products under one comparable).** Six comparables joined several rows of the *same* list; a list row with its own store identifier is its own product, so each is split by identifier:

- MarkView: AlternativeTo MarkView, and snaps `markdownviewer`, `markview`, `markview-reader` (four comparables).
- md Viewer: four Mac App Store ids 6811154913, 6806814038, 6752493034, 6760727738 (four).
- MDReader: Mac App Store ids 6795090587 and 1457039485 (two).
- Copy as Markdown: two Chrome listings (two). Solidity: two VS Code extensions (two). MDX: `silvenon.mdx` and `unifiedjs.vscode-mdx` (two).

Nine further rows were joined across lists by a shared short name and are split off:

- VS Code `cweijan.vscode-typora` from Typora (an extension, not Typora).
- VS Code `dionmunk.vscode-notes` and snap `notes` (notes-foss) from AlternativeTo "Notes (PFA)" (three products).
- VS Code `searKing.preview-vscode` from the Homebrew cask `markdown-preview`.
- VS Code `pdconsec.vscode-print` from AlternativeTo "Print(Notes)".
- VS Code `charliermarsh.ruff` (Python linter) from the Tcl wiki's ruff.
- Tcl wiki `cmark` (a Tcl wrapper) from the C library `cmark` in Homebrew and the Ubuntu archive.
- Homebrew formula `marked` (JavaScript parser) from the Marked app.
- Chrome "Markdown Reader" from Mac App Store "Markdown Reader ®" (Markora).

**Join (one product under several comparables).** Of the flagged pairs in `frame-cells.md`, these are real, judged from the list text (same name and the same described product); each becomes one comparable with several memberships:

Apostrophe + ApostropheEditor/Apostrophe; Bear + Bear: Markdown Notes; Caliu + Caliu - Markdown Notes; colamd + marswaveai/ColaMD; Edmund + I7T5/Edmund; Ferrite + OlaProeis/Ferrite; Folio (Flathub, Snap) + ToolStack Folio; leaf-markdown-viewer + RivoLink/leaf; Lockbook + Lockbook: Private Notes; MacDown + MacDownApp/macdown; MarkEdit + MarkEdit-app/MarkEdit; Markpad + sftwrdotdev/Markpad; mdhero + vaibhav-kakde-in/mdhero; mdSilo + mdSilo/mdSilo-app; miaoyan + tw93/MiaoYan; Monod + TailorDev/monod; MultiMarkdown Composer + MultiMarkdown Composer 4; MWeb + mweb-pro + MWeb - Markdown Writing, Notes; qlmarkdown + sbarex/QLMarkdown; ReText + retext-project/retext; SoloMD + zhitongblog/solomd; Tangent + Tangent Notes + suchnsuch/Tangent; texts + Texts.io; Typora + typora@dev; Ulysses + Ulysses: Writing App; Blank (Snap) + Blank - A new writing-experience; Marked + Marked 2 - Markdown Preview; Dendron + dendronhq/dendron; Foam + foambubble/foam; Joplin + joplin-arnatious (a repackaging of Joplin desktop).

Not flagged by the merge but real (repository name equals product name and the descriptions coincide): MindForger + dvorka/mindforger; MacDown 3000 + schuyler/macdown3000; lookatme (Ubuntu) + d0c-s4vage/lookatme; Marcdown + liyasthomas/marcdown; Tinta + oipoistar/tinta; OpenKnowledge + inkeep/open-knowledge; Pine Markdown Editor + lukakerr/Pine; Remarkable + jamiemcg/Remarkable; NoteKit + blackhole89/notekit; CuteMarkEd + cloose/CuteMarkEd; panwriter + mb21/panwriter; Marker + fabiocolacio/Marker; Quilter + lainsce/quilter; Rhyolite + lockedmutex/rhyolite; Inkwell Markdown Editor + 4worlds4w-svg/inkwell (same tagline); Chrome "Markdown Reader" + md-reader/md-reader (same tagline).

**Flagged but not real** (different products; leave apart): every "Markdown Viewer Editor / …", "Notes (PFA) / …", "markdown-preview / …", "python3-markdown / …" and "r-cran-markdown / …" pair (a generic word inside another name); Easy Markdown / Ionaru/easy-markdown-editor; Marknote / Shouheng88/MarkNote (KDE application against an Android app); MarkText / marktext/muya (the editor against its engine); MarkMyWords / Markdown Suite - MarkMyWords; MarkLens / Marklens; MarkDrop / MarkDrop - Markdown Converter; Markdown Edit / georgeOsdDev/markdown-edit; MDash / MDash: Markdown Notes Editor; Marko pair; Nodes App / Nodes - markdown by WERK 42 (the text does not settle it; leave apart); Paper (Snap) / Paper - Writing App; ZenWriter / ZenWriter Online; Markdown Writer / Writer for Markdown; Notion / Notion Electron; obsidian / Obsidian Web Clipper; Marked / Marked QL; Joplin / Joplin Terminal application (a different form of the same maker's product; collected as its own comparable); Markdown Preview Enhanced (VS Code) / shd101wyy/markdown-preview-enhanced (the Atom package). Pairs where both sides are out (libraries, `mkdocs-*`, `ruby-*`, `libghc-*` and the like) need no resolution: nothing is collected from them.

Net effect: 1,531 comparables, plus 19 from splits, less 48 from joins: 1,502.

## 4. Eligibility: rules struck, undecidable rows resolved

**R1 on AlternativeTo is struck.** It put out any entry whose blurb named Markdown and also a converter, linter, theme or snippet. A Markdown editor that mentions themes or export is still a Markdown editor. Of its 33 rows (20 products), 19 products are applications a buyer weighs: MarkText, Marker, Ferrite, MarkEdit, MWeb, Downright, Inkwell Markdown Editor, Yank Note, Versatil Markdown, MarkView and others. Replacement, applied: a row is out under the converter exclusion only where the blurb's own subject is the converter, linter, formatter, theme or snippet tool; otherwise R2 applies. Result: 19 products in; mdxport ("converts Markdown to … PDFs") stays out.

**The undecidable rule.** Undecidable rows came to 454: 317 on AlternativeTo and 137 elsewhere. The AlternativeTo ones cannot be settled by a second read, because the blurb is the whole text and it is silent. So one rule, applied to the list's own text (description, summary, or the text of a row joined to it), settles all of them. Two clerks would apply it alike:

> A row is **in** where the text says the product opens, reads, writes, edits, previews, renders or presents Markdown files or documents, or calls itself (in its description, not its name alone) a Markdown editor, viewer, reader, notebook, notes application or presenter. It is **out** where the text names Markdown only as formatting syntax, shortcuts or "support" inside a product not said to keep Markdown files, or does not name Markdown at all. For the tcl-wiki cell, "in" means a component a developer builds into a program to parse or render Markdown. A comparable is in if any of its memberships is in.

Resolved in (48 rows): Flathub Reinschrift, Essentialist; Snap SlidesWeft, Notesnook, Sticky Notes; Homebrew mdp, reveal-md, deckset, ia-presenter, tableflip; Ubuntu kookbook, md2term, mdp, pampi; Mac App Store Markdown to PDF Converter－Fast, Decoupage Markdown Studio; VS Code Office Viewer, Marp for VS Code, Print, Auto-Open Markdown Preview, Markmap, vscode-pandoc, XLSX, CSV, TSV & Markdown Editor; awesome-claude-code FlyCrys; Chrome Markdown Here, GitHub Markdown Printer (no-go cell); GitHub pd4d10/hashmd (both topic rows), d0c-s4vage/lookatme, Linbreux/wikmd (both topic rows), doocs/md, genspark-ai/genoffice, nimbalyst/nimbalyst, tianyaxiang/neurapress, growilabs/growi, shuaiplus/inkstone, tenngoxars/WeMD, Cveinnt/LetsMarkdown.com, junian/markdown-resume, terrylinooo/githuber-md, Gram-ax/gramax, jaywcjlove/wxmp, laogou717/md-wechat, markboard-io/markboard, georgeOsdDev/markdown-edit, rotbit/xedit, richardr1126/openreader.

Resolved out: every other undecidable row, including all 317 AlternativeTo R3 rows; on the tcl wiki CommonMark (a specification), jimsoldout (libsoldout not said to be Markdown), ruff, mkdoc, tmdoc (documentation packages) and mkdic (no description); the add-ons to VS Code's built-in preview (Mermaid, emoji, checkboxes, footnotes, front matter, math), which do not themselves open a file; the JSONL transcript viewers on awesome-claude-code, which read event streams, not Markdown files; backlog-md and boolean-maybe/tiki ("Markdown-native" and "Markdown-based" describe a task tool, not its documents).

**Out rows a buyer would weigh.** The rule keeps out some products a writer or note-taker plainly weighs, because no list text they sit on says Markdown: Ulysses (AlternativeTo and Mac App Store), Quilter (AlternativeTo and GitHub), Iotas (AlternativeTo and Ubuntu), and on the Obsidian list Notion-class workspaces. That is a finding about the lists, not about the products: their blurbs do not name the format. If the owner wants any of them placed, it enters as a named row outside the draw under step 5.

**R2 remains loose.** It admits a blurb that mentions Markdown in passing; "PHP Markdown" (a library) is in on the Marked and Glow lists. The condition on the AlternativeTo cells covers it: the collector applies the brief's eligibility sentence on the product's own page and records the reassignment, which changes the numerator, not the draw.

## 5. Sampling rule (AlternativeTo stratum)

Of the 522 comparables with an in-membership in a passing cell, 147 are in only through AlternativeTo cells. Their evidential weight is the lowest in the frame. They are entries a crowd linked to four anchor products. Eligibility was set by script from a blurb, and the list states no reach, no price beyond a licence line, and no count but likes; some are taken down (Monod). A census would spend 147 page sets, 28% of collection, on them. They are sampled; every comparable with any other in-membership stays a census.

> **Rule.** Take the comparables whose every in-membership is an AlternativeTo cell. Order them by the row number of their first in row in `alternativeto.tsv` (the file's order: the Typora, Obsidian, Marked and Glow lists in turn, each in the site's Rank order). Take positions 1, 3, 5, … : **74 of 147**. In any rate that includes this stratum, each sampled comparable carries weight 2.

The rule is systematic, not chosen, and it drops well-known entries with the rest (iA Writer is at position 4). That is the price of a mechanical draw. The 74, for the collector's check: HelixNotes; Reor; StackEdit; marka.md; novelWriter; Lumen AI; mdSilo; MarkFlowy; Notepack; Q - Collect Your Thoughts; Quiver; Document Node; Markdown Monster; CrabPad; Epsilon Notes; Typewrite; Rebel Notes; Markdown Edit; Writed; WordMark; Marxico; Notepad App; zerdo; MiniMark; Markie; Many Notes; Classeur; Write for Mac; TypeFire; Writage; (Un)colored; Theorylog; Markdown Buddy; PileMD; Citronote; Markdown Life; Booker; Zizeg; Pen and Quiet; nTilia; Ritemark; Markdown Writer; Markdific; MDash; Medita; Simplenote; FUTO Notes; NeverWrite; Zen Notes; Supernotes; Rook; Looksyk; FileOutliner; PocketMark; Note Shuttle; Intessika; Binderus; Jylos; OwnSync Note; Phasoric; Cabinet; Stik; Otterly; Lists & Notes; MarbleMD; NormNote; NoteCafe; Halzy; Moment Docs; Steno Notes; LightNote for Windows; Glance – Markdown Viewer; MarkMyWords; vmd.

No other cell is sampled. The Mac App Store's 122 store-only comparables stay a census, because that cell alone states price and so carries the free and paid strata that dimension 2 needs. The GitHub-topic cells stay a census because they are the sub-population that shares the operator's shape.

## 6. The four dimensions per cell

The shape note's dimensions are not all carried by the lists. The collector records them per comparable from the page set.

| cell | 1 reach | 2 paid before reach | 3 sale | 4 place held |
|---|---|---|---|---|
| GitHub topics | shared where the product is reached by clone or release download; record which | not stated: record from the page | not stated: record | shared |
| Mac App Store | differs (store) | stated per row (price) | differs where paid (store takes it) | shared |
| Flathub, Snap, Ubuntu archive, Homebrew, VS Code | differs (store or package manager) | not stated (licence or `{}` only): record from the product's page | not stated: record | shared |
| AlternativeTo | not stated (a directory, not a channel): record | licence line only: record price from the page | not stated: record | shared |
| awesome-claude-code, tcl-wiki | not stated: record | not stated: record | not stated: record | shared |

Until the page set fills a "not stated" cell, a rate turning on dimensions 1 to 3 is computed only on the Mac App Store's free and paid rows and the GitHub-topic cells, as the shape note requires.

## 7. The frame as collection may use it

| | count |
|---|---|
| comparables after duplicate resolution | 1,502 |
| with an in-membership after the undecidable rule and R1 | 534 |
| of which in only through the Chrome Web Store (no-go; to the convenience list) | 12 |
| with an in-membership in a passing cell | 522 |
| AlternativeTo-only stratum, 147, sampled to 74 | less 73 |
| **page sets collection runs on** | **449** |
| named row outside the draw (tkdown) | 1, not in any count above |

## Rows of the large TSVs read

`mac-app-store.tsv`: the header and first five rows (`head -6`), the last four (`tail -4`), all eleven undecidable rows (by grep), the rows for Markdown Reader ®, Easy Markdown and Markdown Pro (by grep), and grep counts of in rows (133), in rows with zero ratings (96), free in rows (106), Mac-only `mt=12` rows (55, every one with zero ratings). `snap.tsv`: all ten undecidable rows (by grep), the name and URL of the 50 in rows (grep, two columns), and the rows for Notes, Marker, MarkView, Folio and typora (by grep). Every row of both files was also parsed by script, together with the other lists, to re-run the merge for sections 3 to 7; those rows were counted, not read.
