# Corrections after the blind second coding

Run folder 0-comparables. Inputs read: the standing block, codebook v1, the agreement file, the sample list, and for each sampled slug its profile and its rows in the coded corpus and the second coding. The agreement file compares each cell on its coded value alone (the text before the first bracketed quote or colon), so a listed difference can be a layout difference; every one of the 413 listed cells was read in full against the codebook and, where the rule needed it, against the profile.

## Counts by kind

| kind | cells |
|---|---|
| 1. Format, not coding (same value, other words, order, quote or count layout) | 266 |
| 2. Rule applied differently | 49 |
| 2a. of which first coding misapplied it: corrected in coded-corpus.tsv | 21 |
| 2b. of which second coding misapplied it: left as it stands | 28 |
| 3. Rule cannot decide: left as it stands, recorded as a codebook weakness | 98 |
| Listed disagreements | 413 |

Cells corrected in coded-corpus.tsv: 21. The file keeps 450 lines of 39 tab-separated columns and its row order; only the cells listed under "Corrections applied" were touched.

A cell is counted once, under the kind of its main difference. Where a corrected cell still carries a second, undecided point, the point is listed under weaknesses too (busymark V11, markdown-mate-writing-notes V32).

## Counts by variable

"Adjusted agreement" is (45 minus all cells that are not format) over 45: the agreement a reader gets once layout differences are discounted, with no credit for the corrections.

| variable | listed | 1 format | 2a corrected | 2b second in error | 3 cannot decide | adjusted agreement |
|---|---|---|---|---|---|---|
| V01 | 4 | 3 | 0 | 0 | 1 | 0.98 |
| V02 | 8 | 6 | 0 | 1 | 1 | 0.96 |
| V03 | 8 | 6 | 1 | 0 | 1 | 0.96 |
| V04 | 10 | 1 | 0 | 0 | 9 | 0.80 |
| V05 | 4 | 2 | 0 | 1 | 1 | 0.96 |
| V06 | 20 | 5 | 2 | 6 | 7 | 0.67 |
| V07 | 21 | 13 | 1 | 3 | 4 | 0.82 |
| V08 | 11 | 7 | 0 | 0 | 4 | 0.91 |
| V09 | 11 | 6 | 0 | 1 | 4 | 0.89 |
| V10 | 15 | 14 | 0 | 0 | 1 | 0.98 |
| V11 | 8 | 3 | 1 | 1 | 3 | 0.89 |
| V12 | 18 | 8 | 3 | 2 | 5 | 0.78 |
| V13 | 25 | 15 | 1 | 1 | 8 | 0.78 |
| V14 | 8 | 3 | 0 | 0 | 5 | 0.89 |
| V15 | 13 | 10 | 0 | 0 | 3 | 0.93 |
| V16 | 37 | 35 | 1 | 1 | 0 | 0.96 |
| V17 | 3 | 0 | 0 | 0 | 3 | 0.93 |
| V19 | 15 | 6 | 2 | 1 | 6 | 0.80 |
| V20 | 7 | 6 | 0 | 0 | 1 | 0.98 |
| V21 | 29 | 19 | 2 | 3 | 5 | 0.78 |
| V22 | 12 | 9 | 0 | 2 | 1 | 0.93 |
| V23 | 7 | 5 | 1 | 1 | 0 | 0.96 |
| V24 | 5 | 1 | 1 | 0 | 3 | 0.91 |
| V26 | 2 | 2 | 0 | 0 | 0 | 1.00 |
| V27 | 30 | 26 | 1 | 0 | 3 | 0.91 |
| V28 | 10 | 9 | 0 | 0 | 1 | 0.98 |
| V29 | 5 | 3 | 1 | 0 | 1 | 0.96 |
| V30 | 4 | 1 | 0 | 1 | 2 | 0.93 |
| V31 | 7 | 2 | 1 | 2 | 2 | 0.89 |
| V32 | 18 | 9 | 2 | 0 | 7 | 0.80 |
| V33 | 16 | 15 | 0 | 0 | 1 | 0.98 |
| V34 | 6 | 6 | 0 | 0 | 0 | 1.00 |
| V35 | 6 | 5 | 0 | 0 | 1 | 0.98 |
| V36 | 4 | 3 | 0 | 0 | 1 | 0.98 |
| V37 | 6 | 2 | 0 | 1 | 3 | 0.91 |
| all | 413 | 266 | 21 | 28 | 98 | |

Variables with no listed difference: V18, V25 (45 of 45).

Reading the raw table: the very low raw rates of V16 (0.18), V21 (0.36), V27 (0.33) and V13 (0.44) are mostly layout (how a price, a place list, a date or a quoted span was written); their adjusted agreement is high. The variables whose agreement a reader should weigh as weak are those with the most kind 3 cells, where the frozen instrument is the source of the difference: V04 (9), V13 (8), V06 (7), V32 (7), V19 (6), V12 (5), V14 (5), V21 (5), V07 (4), V08 (4), V09 (4), with V11, V15, V17, V24, V27, V37 (3 each) next. Second-coding quality, not the instrument, is the weak point on V06 (6 kind 2b cells), V07 (3) and V21 (3).

## Corrections applied (first coding, coded-corpus.tsv)

One line each: slug, variable, from, to, rule.

1. pixley-markdown, V03: "markdown token in name | function word in name (Reader; site name only)" to "markdown token in name". V03 reads V02 only; the listing title is "Pixley Markdown" and "Reader" belongs to the site name. (V02 of this row also carries the site names beside the listing title; V02 is not a listed difference and was not touched.)
2. busymark, V11: removed "package manager named as required to install" ("Don't have snapd? Get set up for snaps."). The snap line is one install route among several (a source build is also instructed), which V11 sends to V21, and it does not say snapd is required. The same line was left uncoded in linotes by the same clerk. The "none needed, stated" element is undecided (weakness).
3. ghostwriter, V12(a): added "store install" with the quote "Install" (Flathub). The same clerk coded that button as "install from a store" in V07; V12(a) codes the methods the text instructs.
4. markdown-to-pdf-converter-fast, V12(a): "not stated" to "store install" with the quote "Get" (listing button label). Same clerk coded it "install from a store" in V07.
5. marp-for-vs-code, V12(a): "undecidable" to "host program's extension manager", quote "Launch VS Code Quick Open (Ctrl+P), paste the following command, and press enter." The sentence is the host's extension install and the value names exactly that; the same sentence was coded this way in auto-open-markdown-preview by both clerks.
6. marp-for-vs-code, V07: "undecidable" to "install from a store" with the same quote (marketplace); "sponsor or donate" kept. V07 codes an instruction to install on a marketplace.
7. foldingtext, V13(a): added "task lists", quote "FoldingText does outlining, todo lists, and more". V13 rule: to-do items code task lists.
8. editor-markdown-notes, V31: "not stated" to "preview updates as you type inside the product, stated", quote "Simple Markdown writing with live preview" (listing). V31 rule: "live preview" in an editor (V09 is editor with rendered view in both codings).
9. minimark, V23: "not stated" to "nothing paid before use, stated", quote "Free product" (the same AlternativeTo line coded as price "free" in V16(a) and (b)). V23 rule: "Free" stated as the price.
10. vsch-idea-multimarkdown, V16(a): "released without needing a license" to "not stated". V16(a) records prices; a licence-need statement is not a price, and a repository with no price text codes "not stated" for (a) and (b). The quote is not carried to (c), which names a licence.
11. md-reader-md-reader, V27(b): "undecidable" to "archived, deprecated or unmaintained, stated", quote "This repository contains the old source code of Markdown Reader(2.x version) and is no longer maintained." (README). V27 rule: if any captured page states unmaintained, that value wins; the Chrome listing date stays in (a).
12. md-reader-md-reader, V24: added "checkout or licence key from the maker or a payment processor", quote "we receive necessary records from the payment provider, such as subscription status, order ID, product plan" (privacy page). V24 rule: code the mechanism the text names.
13. taio-markdown-text-actions, V29: "Full text search scope not named, not coded" to "undecidable", quote "Full text search" (listing). V29 rule: a search with no scope named, in a sentence not about the open document, is undecidable with a note, not omitted. The second coding also erred here (see 2b).
14. markdown-mate-writing-notes, V32: added "follows the system appearance, stated", quote "Support for system Light/Dark modes." The same clerk coded that sentence "light and dark modes" and coded the same kind of wording in marklens as following the system.
15. fastmd-fast-markdown-editor, V32: added "themes provided", quote "Light and Dark themes" (What's New 1.5). The same clerk coded "light and dark modes" from the same words and codes "built-in light and dark themes" as both in ghostwriter and mdserve.
16. growilabs-growi, V21: removed "npm (for plugins)" and "github (for plugins)", count 5 to 3. V21 records places to get the product; the sentence "You can find plugins from npm or github!" names places for plugins.
17. ownsync-note, V21: "Your browser / PWA (count 1)" to "not stated". V21 copies names the text gives; the profile records the section as silent, and the entry is a class of place, not a copied name.
18. linotes, V06: "A fast, private notes app for Linux."; "Designed for GNOME and Ubuntu, works on any modern desktop" to "not stated". V06 holds audience or purpose phrases about people; a platform and desktop names a place it runs, not an audience, and the same clerk did not record platform phrases in other rows.
19. deckset, V06: added "individuals", quote "One-time pricing for individuals and teams." (/buy/). V06 rule: generic audiences without a qualifier are recorded; "teams" had coded V05, "individuals" codes no class.
20. markdown-mate-writing-notes, V19: "not stated" to "a copy to download or install", quote "View in Mac App Store" (free, no licence unit named). V19 rule: a free download with no licence unit named; the same clerk coded the same text as an install act in V07.
21. marp-for-vs-code, V19: "not stated" to "a copy to download or install", quote "Launch VS Code Quick Open (Ctrl+P), paste the following command, and press enter." (free, no licence unit named). Same rule, and the corrected V07 above.

## Second-coding errors left as they stand (kind 2b)

One line each; the first coding was right under the rule, or the second coding broke the rule where the first did not.

- markdown-to-pdf-converter-fast V05: second coded "Bloggers and platform publishers" from "Social media creators exporting Markdown to image cards". The noun is on no class list ("content creators who publish posts" is the nearest); the rule says never pick the nearer value. First put it in V06. V06 of this slug follows (second omitted the phrase).
- notepad-app V09: second coded an editor value "from note-taking app alone" (its own note); no sentence says the product edits. First: "not stated".
- marp-for-vs-code V11: second dropped the browser requirement ("Exporting PDF, PPTX, and image formats requires to install any one of Google Chrome, ...") instead of coding undecidable; standing instruction 6. The gap is a weakness (V11 below).
- mdserve V12(b): second "not stated"; the README says "there will be no further releases, bug fixes, or security updates." which is an explicit statement about new versions.
- marklens-markdown-reader V07 and V12: second coded "clone or build from source" from the heading "Getting started" and "Download bundled web assets"; no clone or build instruction is quoted.
- read-md V22: second coded "by opening it in a browser"; V22 classes only V21 entries and V12(a) routes, and both are "not stated" in both codings.
- vsch-idea-multimarkdown V23: second coded "nothing paid before use" from "released without needing a license", which is not a price statement (second itself coded V16(a) "not stated").
- md-reader-md-reader V16(a): second quoted "Subscribe to the Pro plan to unlock more features" as a price; no price is in the captured text.
- simov-markdown-viewer V02: second recorded the README heading "Markdown Viewer / Browser Extension"; the Chrome Web Store listing title "Markdown Viewer" exists and V02 takes the listing title first.
- ownsync-note V19: second coded "an account on a service" from "login and license" (its own note: "coded loosely"); no unit is named as sold.
- ownsync-note V31 and scriptum-markdown-editor V31: second omitted "live preview" in an editor ("Full Markdown with live rich-text preview"; subtitle "Live preview, read on iPhone"); V31 rule: live preview in an editor is "preview updates as you type inside the product".
- obsidian V07: second omitted "install from a store" ("iOS App Store; Android Google Play" on the download page); xlsx-csv-tsv-markdown-editor V07: second omitted "download a file" ("VS Code Marketplace: Download Extension", a link label).
- markdown-pro V21 and V22: second omitted "App Store" (page title "Markdown Pro App - App Store"); it coded the same kind of title in markdown-to-pdf-converter-fast. V22 follows V21.
- toolstack-folio V21: second omitted "Desktop store" ("View in Desktop store"); vsch-idea-multimarkdown V21: second omitted "JetBrains Marketplace".
- qingmo-markdown-editor V37: second recorded two sentences, the first a tagline ("built for a smooth writing flow"); the rule takes the first sentence that gives a reason.
- growilabs-growi V06: second recorded a recruiting sentence ("We are looking for contributors ...") and missed the purpose phrase; foldingtext V06: second added "Not a note app. A productivity platform.", which is no audience or purpose phrase.
- neverwrite V06, qingmo-markdown-editor V06, taio-markdown-text-actions V06: second omitted a phrase that meets the rule ("people who need to handle workflows with multiple parallel agents"; "built for a smooth writing flow"; "A modern app for text processing").
- taio-markdown-text-actions V30: second coded "follows wiki-links or backlinks" from "Tags, wikilinks and backlinks", which names no behaviour (V30 rule: no behaviour stated codes nothing).
- growilabs-growi V13: second coded "emoji shortcodes" from "Emoji"; the rule codes a form only by its listed words and quotes any other word in R6. (Its "markdown named, no form named" is a weakness, below.) Also taio V29 (both codings erred; the first was corrected above).

## Codebook weaknesses (kind 3), for the synthesis clerk

Each is a case where two careful clerks read the frozen rule differently and the rule does not settle it. Nothing was changed; a change takes a new version, a date and a re-coding of everything coded. Cell counts in brackets.

- V01 eligibility (1): ufocus. Test 2(a) lists render, preview, display, view, read, open "such as", and "Markdown formatting is now applied automatically to files with the correct extension" and "MultiMarkdown: easily add headings ..." fit neither the verb list nor (b) (markdown not in name, subtitle or first paragraph). Needed: close the verb list or say whether apply/format counts, and say whether an editing claim in a feature list passes test 2. A single cell moves a row between the corpus and the discarded rows.
- V02/V03 (2): markrahq-markra. A store-less product has a site page title with a descriptive tail ("Markra | WYSIWYG Markdown editor with native AI") and a README heading ("Markra"). Needed: an order of sources (store title, page title, first heading). V03 inherits the choice.
- V04 (9): foldingtext, kite-markdown-editor, markdown-to-pdf-converter-fast, mdcat, mdserve, obsidian, richardr1126-openreader, scriptum-markdown-editor, simov-markdown-viewer. Three gaps: (a) one other named program (StoryWren, Web Clipper, mdpick): "family" needs "two or more distinct programs ... alongside this one" and does not say whether this program counts as one; (b) a bundled companion (Quick Look extension or viewer, a Claude Code plugin, a compute worker, a plug-in SDK) is neither a "component" (defined as a library built into others' software) nor an edition; "single program" excludes any companion; (c) "versions" in "editions, tiers or versions" does not say whether a release number, a legacy branch or a Mac and an iPhone build counts. Needed: a defined value for a bundled companion, a count rule for family, and a definition of version.
- V05 (1): md-reader-md-reader. "Anyone who reads README files, API documentation ..." is a generic noun with a reading qualifier; class 8 lists "recipients of markdown files" and "readers", and the hard case turns on "someone sent them". Needed: say whether a reading qualifier alone codes class 8.
- V06 (7): kite-markdown-editor, mandown, marp-for-vs-code, obsidian, read-md, texts-io, toolstack-folio. The boundary of a "purpose phrase" is open: a description of what the product does, a use-case list, a slogan and an AI-flavoured sentence (hard case C of V05) are recorded by one clerk and not the other. Needed: a test such as "for/built for/designed for plus a purpose or person" and a statement of whether use-case sentences count.
- V07 (4): qingmo-markdown-editor, scriptum-markdown-editor, taio-markdown-text-actions, richardr1126-openreader. Whether a store price line, an in-app purchase price or "pay once to use ..." is an invitation ("price button") or description, and whether "Develop locally" or a Docker or Vercel deploy route is "clone or build from source". Needed: say what a captured price line is, and add a value (or a rule) for self-hosted deployment.
- V08 (4): fastmd-fast-markdown-editor, joplin, marklens-markdown-reader, read-md. The rule gives an operating-system-to-kind clause for desktop systems only: iPhone, iPadOS and Android named leave "mobile application" without a rule (two clerks left it undecidable, two coded it); a bundled Quick Look extension (other kind) and a hosted sync service (Joplin Cloud, service) are named beside the product, and the rule does not say whether a companion form is a kind of the product. Needed: a mobile clause and a rule on bundled and add-on forms.
- V09 (4): ianks-octodown, markdown-to-pdf-converter-fast, pixley-markdown, steelnote-markdown-notes. "Edit your markdown like a boss with LiveReload" (whose editing?), a bare "Pro Editor" in release notes, a write-back to the file ("every change writes back") set against "read-only permissions", and "Tables, images and PDFs sit inline" as a rendered view. Needed: say whether the rendered-view words are a closed list, whether write-back is editing, and whether a name fragment states editing.
- V10 (1): ownsync-note. "Log in on any browser" against "any desktop with a web browser (stated as such)". Needed: say whether "any browser" is that statement.
- V11 (3): foldingtext, linotes, markdownmeister, with busymark and marp-for-vs-code. No value for software that must be installed but is neither runtime, host, package manager nor build tool (Rosetta 2, a browser for export); a runtime needed only to build (Node.js) is runtime or toolchain; a package manager that is the only install route ("Make sure snap support is enabled") is neither "merely offered" nor stated as required; "Packaged users do not need separate ..." is a partial none-needed. Needed: an "other software required" value and a rule for build-time and only-route cases.
- V12 (5): growilabs-growi, markrahq-markra, md-reader-md-reader, neverwrite, xlsx-csv-tsv-markdown-editor. No value for container or server deployment (docker-compose, Helm, on-premise); artifact names such as "portable", "AppImage", ".deb" with or without an instruction; "drag the extension into the browser"; a marketplace "Click Install" inside a host (store install or host's extension manager). Needed: a deployment value, a rule on artifact names (the V10 rule on file extensions has no V12 counterpart) and a store/host-manager tie-break.
- V13 (8): busymark, clearance, fastmd-fast-markdown-editor, ghostwriter, markdown-mate-writing-notes, mdcat, notepad-app, scriptum-markdown-editor. (i) Whether "markdown named, no form named" may be coded beside named forms and what claim triggers it (a product named a Markdown editor names markdown by its name); (ii) whether a documentation format such as Writerside is a flavour; (iii) "remain editable as source" against "shown as plain text, stated"; (iv) "cmark-gfm" against the rule for "GFM"; (v) "GitHub alerts" against "callouts or admonitions", given that the sentence "any other word for a form not on this list ... codes nothing" can be read two ways; (vi) "syntax highlighting" against the listed "code highlighting, highlighted code". Needed: an equivalence list for every form, exclusivity of the no-form value, and a closed-or-open statement for the (b) values.
- V14 (5): 0xgg-crossnote-app, foldingtext, scriptum-markdown-editor, steelnote-markdown-notes, taio-markdown-text-actions. Sync to the user's own cloud or git remote (iCloud, a git repository) is neither "optional upload" nor "content leaves" by the wording; "Your documents stay where you put them" may or may not be a statement of local storage; a bare "can be synchronized using iCloud" fits no value. Needed: a rule for the user's own account, and a value for sync stated with locality not stated.
- V15 (3): growilabs-growi, ownsync-note, simov-markdown-viewer. A feature that names a service or request ("RAG ... powered by OpenAI's Vector Store", sync "to your personal Google Drive", "make a GET request every second") implies network use but the rule codes only explicit statements, and the value says "only". Needed: say whether a named service or request is an explicit statement and whether "only" is required.
- V17 (3): busymark, read-md, scriptum-markdown-editor. A required Nextcloud server, a personal access token, an iCloud account: which of "another product or subscription" and "own API key or service account" they are, and whether a free-software server falls under the V11 exemption when its cost is not stated. Needed: separate values for a third-party account and a self-run server.
- V19 (6): fastmd-fast-markdown-editor, marklens-markdown-reader, qingmo-markdown-editor, taio-markdown-text-actions, ufocus, ianks-octodown. Whether a store listing that shows "Free" or a price offers "a download" when the text has no download or install invitation; and a language package manager (gem) against "the system's package manager". Needed: say whether a store listing is a download offer, and whether "package manager" is system-only.
- V20 (1): deckset. Whether a /buy/ page on the maker's site with prices and a quote address is a "web store or checkout page". Needed: a test for checkout (a purchase control captured as text).
- V21 and V22 (5 + 1): ghostwriter, joplin, kite-markdown-editor, marklens-markdown-reader, obsidian (V22 marklens follows). What is a "place": download-page operating-system labels (Windows, Mac), "Windows 10 portable download", the captured page's own URL, a mention of the maker's site, a source repository named as where the source lives. Needed: a definition of a place by what it is (a store, registry, release page or site that is named as where to get) and a rule on the page's own address.
- V24 (3): markdown-mate-writing-notes, marp-for-vs-code, simov-markdown-viewer. A bare "Donate" or "Sponsor" label names a mechanism but no platform; "Free" or "Free and Open Source" against the hard case "Free forever" for "no sale taken". Needed: whether a label alone codes the sponsorship value, and which free wordings say nothing is sold.
- V27 (3): markdown-pro, neverwrite, notepad-app. A directory entry's "last updated" (AlternativeTo) is or is not a "listing update". Needed: say which listings count.
- V28 (1): markdown-to-pdf-converter-fast. "Automatic PDF bookmarks" in the exported file against bookmarks for finding the way in a long document. Needed: scope of the variable (reading, or output as well).
- V29 (1): growilabs-growi. "Full-text search ... include the title of the uploaded file" is a scope statement or is not. Needed: what counts as naming a scope.
- V30 (2): busymark, clearance. "Local images can be selected from disk, pasted ..." and "manage remote-image permissions" (insertion, permission) against "shows"; "Follow Markdown links to local files or web URLs" (are the local files markdown files). Needed: a behaviour test and a link-target test.
- V31 (2): busymark, marp-for-vs-code. "Detect files changed outside BusyMark" (detect, not reload) and "preview the output as soon as you edit its Markdown" in a host editor (inside the product or not). Needed: whether detection is reload and whether an extension's host editing is "inside the product".
- V32 (7): foldingtext, linotes, md-reader-md-reader, minimark, notepad-app, qingmo-markdown-editor, xlsx-csv-tsv-markdown-editor. A toggle label "System", "interface zoom", "Adjust ... typography" (font or size choice?), "Dark Mode" alone, "themes" of a PDF export, a host editor's theme followed. Needed: the same kind of equivalence list as V13 and a scope (the product's interface or its output).
- V33 (1): qingmo-markdown-editor, "One-tap publishing" as "share or send from the product". V35 (1): linotes, repository stars, forks and watchers against the listed values. V36 (1): richardr1126-openreader, text-to-speech through OpenAI-compatible servers as "AI features in the product" or "works with AI agents or tools". Needed: a line for each.
- V37 (3): ghostwriter, neverwrite, obsidian. A reason that spans two sentences (benefit, then the wish to give back), and a benefit claim ("so you're never locked in"; "without giving up ownership") against a reason for making. Needed: say whether a benefit claim with a "so" or "without" is a reason, and how many sentences a reason may take.

## Other observations for the synthesis clerk

- The first coding's V07, V12, V19, V21 and V22 were not always derived from one another (V22 is defined as a classing of V21 and V12(a)); the corrections above restore the derivations where the first coding itself supplied the premise. The second coding shows the same drift (read-md V22, markdown-pro V22).
- The first coding coded "undecidable" on V04 where the second picked a value in seven of the nine V04 cells; in each the rule gives no value for a bundled companion, so that clerk applied standing instruction 6 as written.
- Not touched, because not listed: pixley-markdown V02 carries the site names beside the listing title (see correction 1).
