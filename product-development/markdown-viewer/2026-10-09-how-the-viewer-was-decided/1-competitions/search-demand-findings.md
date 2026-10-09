---
title: "What buyers type: search-demand findings for the markdown viewer"
date: 2026-10-09
method: "SAGE Survey section 2, 'What buyers type', run by the search-demand clerk; market side only, before the offering has a name or a page"
status: "Findings numbered SD-n; none decides anything alone. No volume exists in this study."
---

# Instruments and what was and was not read

- Rank database: no API units this month. Every term's volume column below reads "not searched". No volume, difficulty, density or intent label was pulled for any term.
- Located results-page captures, through the serpapi skill's `search` subcommand, 2026-10-09 about 07:20 to 07:21 UTC. Every capture reports: location requested "Austin, Texas, United States", location used "Austin,Texas,United States", google.com, language en, desktop. The location is my choice: the files open to me do not name the operator's national market. Ten organic results were asked for per term; "first page" below means those ten as returned. SerpApi's "total_results" (100 to 159) is an instrument figure, not a demand figure, and is not used.
- Relative interest over time (Google Trends): not made. The serpapi skill as documented offers flights, search, maps, reviews and hotels; its script has no Trends command (zero occurrences of "trends" in it). I did not call the API's Trends engine by hand, since the skill does not offer it. The season (step 3) is therefore unread; see SD-14.
- Read, in order: standing block, venue situation, survey section 2 "What buyers type", the day-one pull. Nothing else.

# Readings (one sentence each, text generator against product designer)

- Venue situation: a text generator would conclude the offering sells to the ten audiences listed; a product designer concludes there is nothing to take payment for and no place to hold, so search can only measure how many people find a free download, never revenue.
- Survey method: a text generator would fill the volume table with plausible numbers; a product designer writes "not searched" and names the gap, as the method says.
- Day-one pull: a text generator would take the 37 pages as the market's vocabulary; a product designer takes them as a convenience list whose words are seeds, not counts.

# Step 1: the term table

The buyer's own words from enquiries do not exist for this offering: no page, listing or installer is public, so there are no enquiries, booking free-text or meeting transcripts. The only buyer wording in this study is what Google's own suggestions show (people also ask, related searches), which is Google's rendering of searchers in aggregate, not enquiries.

Sources of the seeds: (a) comparables' own words in the day-one pull, e.g. "terminal based markdown reader" (Glow), "Markdown viewer / browser for your terminal" (Frogmouth), "a standalone application that renders and displays Markdown files" (Mdview), "a previewer for Markdown and other plain text markups" (Marked 2), "Reading Markdown only" (Okular), "Open Markdown files like PDFs" (Moji), "Markdown Viewer" and "Markdown Viewditor" and "Markdown Hot Reload" (Snap titles); (b) the operator's in-program words; (c) Google's expansions in the captures.

Volume column reads "not searched" for every row. Struck column: not computable without volume or an intent label; the modifiers in the phrase and the page the term already gets are noted instead.

| Term | Kind | Layer | Volume | Struck | Note from the capture |
|---|---|---|---|---|---|
| markdown viewer | trade | bare generic | not searched | n/a | captured |
| markdown reader | trade | bare generic | not searched | n/a | captured |
| markdown preview | trade | bare generic | not searched | n/a | captured |
| markdown previewer, markdown renderer, markdown browser | trade | bare generic | not searched | n/a | from comparables' self-descriptions; not captured |
| markdown editor | trade (adjacent) | bare generic | not searched | n/a | captured; asks for editing the viewer does not do (see SD-11) |
| md file viewer | buyer | bare generic | not searched | n/a | captured |
| how to open md file | buyer | proximity (see below) | not searched | n/a | captured |
| view md files with formatting; app to open MD files; can I open MD file in browser | buyer | proximity | not searched | n/a | related searches on "how to open md file"; not captured |
| markdown viewer linux | place (platform) | platform-qualified | not searched | n/a | captured |
| markdown viewer windows; markdown reader windows | place | platform-qualified | not searched | n/a | related searches; not captured |
| markdown viewer chrome / firefox / edge; md viewer vscode | place (host program) | platform-qualified | not searched | n/a | related searches; the viewer is none of these hosts, so these may ask for something the operator cannot be (extension). Not struck: no volume |
| markdown viewer github; markdown viewer app | place / trade | platform-qualified / bare | not searched | n/a | related searches |
| markdown viewer linux command line; terminal markdown viewer | place (terminal) | platform-qualified | not searched | n/a | related search / PAA "Is there a terminal markdown viewer?" |
| markdown viewer mac | place | platform-qualified | not searched | n/a | PAA "Is there a good markdown viewer for Mac?"; not captured |

Layer reading for software. The survey's proximity layer is "near me, closest"; no software term has that meaning. I took the nearest analogue to be the terms said from inside the moment of need, with a file already in hand ("how to open md file", "app to open MD files"). This is my reading, not the method's, and the layer is reported apart from the other two as required. Mac and Windows terms are platform-qualified terms the operator may not serve (the viewer's shipping platforms are not stated in the files open to me, except Tcl 9 with Tk install and a sibling release pipeline); whether they are struck is a question for the capability note, not for this study.

Internal term against buyer term:

| Operator's word | Buyer or trade word seen in the captures | Seen? |
|---|---|---|
| viewer | viewer, reader, preview, "md viewer"; "editor" also appears on viewer pages | yes, all four in use side by side (SD-3) |
| markdown viewer | md file viewer, "MD file Viewer app" | yes |
| markdown file viewer | md file viewer; "Markdown Document Viewer" (Microsoft store title) | yes |
| foldable sections, fold | no appearance in any people-also-ask or related search captured; "collapsible sections" appears only in Marked 2's own claims in the day-one pull | no buyer-side wording found; not tested by a capture |
| table of contents | "TOC" and "ToC" in comparables (simov, Markdown Preview Plus); not in suggestions | not in buyer-side suggestions |
| find -xdev | not in suggestions | not seen |
| reload | "live reload" (Markdown Preview Plus), "Auto reload on file change" (simov), "Markdown Hot Reload" (Snap title) on the trade side; not in suggestions | trade side only |

# Step 2: results-page captures

All: Austin, Texas, United States; 2026-10-09; one page. "Forum" and "video" noted where the result link was Reddit, Stack Overflow, Ask Ubuntu, Apple discussions or YouTube. Positions are as SerpApi numbered them, with forum and video entries included. Every one of the seven pages returned an AI overview block; the clerk did not read its text beyond the first sentence.

## markdown viewer

First page: online tool pages (codebeautify.org, elementor.com/tools, dillinger.io/markdown-viewer, markdowner.github.io), VS Code Marketplace (Markdown Preview Enhanced), GitHub repository (jojomondag/Markdown-Viewer), terminal previewer (leaf.rivolink.mg), two Reddit threads (positions 1 and 6, r/Markdown and r/vim). Operators hold most positions (tools and one extension store listing); forums hold two; no media site; no store page for a desktop app. A product answer wins, mostly browser-based online tools, with a forum thread in position 1.
People also ask, verbatim: "How to edit .MD files on Mac?"; "How to read a Markdown file in Windows?"; "Is there a terminal markdown viewer?"; "Is there a good markdown viewer for Mac?"
Related searches, verbatim: Markdown Viewer Windows; Markdown viewer GitHub; Markdown Viewer Chrome; Best Markdown viewer for Chrome; Markdown Viewer app; Reddit markdown viewer; Markdown Viewer Firefox; Chrome Markdown Viewer How to use.

## markdown viewer linux

First page: Unix StackExchange ("command line - Markdown Viewer", position 1), Snap Store (markdown-viewer-premium, 2), Reddit r/macapps (3; a Mac thread on a Linux query), markdown-viewer.com listicle "Markdown Reader Linux| 7 Best Tools You Need to Try Now!" (4), Ask Ubuntu "Console-based markdown reader" (5), ArchWiki Zettlr (6), Fedora Magazine "Applications for writing Markdown" (7), AUR markdown-reader (8). A forums-and-documentation page, with two package-repository listings (Snap, AUR); no operator's own site. How-to and discussion answers win; a product appears only as a package listing. A discussions-and-forums block was present.
People also ask: none returned.
Related searches, verbatim: Markdown viewer linux command line; Markdown viewer linux github; Free markdown viewer linux; Best markdown viewer linux; Markdown viewer linux download; Markdown viewer linux centos 7.

## md file viewer

First page: GitHub (simov/markdown-viewer, 1), Reddit r/vim (2) and r/MacOS (4), codebeautify.org (3), a GitHub "markdown-viewer-extension" page (5), Microsoft store page "Markdown Document Viewer" (6, zh-tw), SourceForge (7), macmdviewer.com blog "Best Markdown Viewer for Mac (2026): 16 Apps Compared" (8), Aspose online tool (9). Operators and stores hold the page with a vendor blog and two forum threads; a product answer wins.
People also ask: none returned.
Related searches, verbatim: Chrome Markdown Viewer; MD file Viewer app; Md file viewer extension VS Code; Best Markdown viewer for Chrome; Edge Markdown viewer; Markdown Viewer extension Firefox; Markdown viewer GitHub; MD file Viewer download.

## how to open md file

First page: Stack Overflow "View markdown files offline - github" (1), md-reader.github.io (2), Microsoft Store "Simple Markdown Viewer" (3), Google Workspace Marketplace "Markdown Viewer and Editor" (4), markdownguide.org Marked 2 page (5), mdview.io (6), Apple discussions "Markdown Viewer?" (7), a minimaxi.com-hosted "Open MD File in Browser" page (8). Mixed: one forum answer first, then operators' online readers and three store or marketplace listings, one reference site. Products win, with a how-to forum answer in position 1; no page on the first ten is a prose how-to article.
People also ask, verbatim: "What is a free Markdown viewer for Windows?"; "What does ``` do in Markdown?"; "How hard is it to learn Markdown?"; "Is there a good markdown viewer for Mac?"
Related searches, verbatim: How to view md files in VS Code; Can I open MD file in browser; Google Drive Markdown Viewer; How to view md files with formatting; App to open MD files; Markdown reader Windows; Markdown viewer and editor; Chrome Markdown Viewer. An inline videos block was present.

## markdown reader

First page: markdownguide.org/tools (1), Ask Ubuntu "What markdown readers (not editors) are available?" (2), simov GitHub extension (3), Reddit r/Markdown (4), mdedit.ai online viewer (5), editor.md (6), YouTube (7), Google Play "Read.md" (8). Reference site, forum, GitHub, an online tool, a Play Store app; a product answer wins narrowly, with the reference site and forums holding the top two. A discussions-and-forums block was present.
People also ask: none returned.
Related searches, verbatim: Markdown reader open source; Best markdown reader Windows; Best free Markdown editor; Markdown Viewer UWP; Best Markdown editor Windows free; Markdown reader free Windows; Ubuntu markdown reader; Best free Markdown editor Mac.

## markdown preview

First page: mdview.io (1), codebeautify.org (2), editor.md (3), Google Workspace Marketplace (4), codeinword.com tool (5), VS Code Marketplace "Markdown Pro" (6), YouTube (7), markdowner.github.io (8), cleanor.app (9). Almost wholly online tools and marketplace listings; a product answer wins; one video; no forum.
People also ask: none returned.
Related searches, verbatim: Markdown preview plugin; Markdown Preview online with Mermaid; Markdown Preview Mermaid Support How to use; Google Drive Markdown Viewer; MD viewer download; Markdown editor online; Markdown viewer and editor; Md viewer vscode.

## markdown editor (the adjacent term; see SD-11)

First page: Medium posts (1, 2), YouTube (3), Setapp review (4), IONOS (5), digitaltoolpad.com online editor (6), Google Play (7), Grammarist (8), LightPDF (9). Media and listicle sites hold it; an operator seat exists only as one online editor and one Play listing. Roundup articles win, not a product.
People also ask: none returned.
Related searches, verbatim: Markdown editor online; Markdown editor Windows; Markdown editor free; Markdown editor Obsidian; Markdown editor apps; Markdown editor with AI; Best free Markdown editor; Markdown editor open source.

# Step 3: the season

Not read. Relative interest for "markdown viewer" and "markdown editor", worldwide and one country, five years and twelve months: not made, because the serpapi skill offers no Trends access (see Instruments). No country was chosen for Trends. The calendars to hold the readings against, when the capture exists, are the teaching year (term starts and exam periods in the northern hemisphere) and the release cycles of the big editors; this clerk has no dates for either in the files open to it, so none are asserted.

# Step 4: the ceiling

From the venue situation: copies are unlimited, nothing is reserved or capped. There is no capacity ceiling for copies. The only ceiling is the maker's hours, which are unrecorded, so headroom in units cannot be stated and demand cannot be called above or below any ceiling.

# Findings

SD-1. No volume exists this month. The rank database has no units; every term's volume reads "not searched", no term is ranked by size, and no layer can be summed. Signal stops here: nothing below says how many people type any term.

SD-2. The buyer's own words from enquiries do not exist for this offering (nothing public; no enquiries). The only buyer-side wording is Google's people-also-ask and related-search text, which is Google's aggregate rendering, not enquiries. Signal stops: unattributed, undated, uncounted.

SD-3. Four nouns are used for the same thing on the same pages: viewer, reader, preview, editor. "Markdown reader" and "markdown viewer" results overlap (the simov extension is on both first pages); "Markdown viewer and editor" is a related search under both "markdown preview" and "how to open md file". Signal stops: one buyer, one place, one day; overlap of result pages is not overlap of intent.

SD-4. Platform words in Google's suggestions are mostly host programs and operating systems, not the terminal: Windows, Chrome, Firefox, Edge, VS Code, GitHub, Linux command line, Mac, UWP. "Is there a terminal markdown viewer?" is a people-also-ask under "markdown viewer". Signal stops: suggestions are ordered by Google, not ranked by size here.

SD-5. "markdown viewer": the first page is online tools, a VS Code extension, a GitHub repository, a terminal previewer and two Reddit threads; a product answer wins and the name is already used as a title by several pages (Markdown Viewer, markdown-viewer.com, simov/markdown-viewer, Markdown Viewer and Editor). The bare name is crowded by products with the same words. Signal stops: one buyer at Austin, Texas on 2026-10-09; a different location or day can differ.

SD-6. "markdown viewer linux": discussion and documentation win (Unix StackExchange, Ask Ubuntu, ArchWiki, Fedora Magazine, a Reddit thread from a Mac forum) and package listings (Snap, AUR) are the only products. This is the only captured term where no operator's own site is on the first page; the platform-qualified Linux layer is held by forums, wikis and package listings. Signal stops: one capture; no volume.

SD-7. "md file viewer": products, stores and GitHub win; a vendor roundup (macmdviewer.com) and two Reddit threads sit on the page. A store listing in Chinese (zh-tw) shows the location did not fix the store's language.

SD-8. "how to open md file": the page is answers to a file in hand, answered by products (online readers, store listings) with one Stack Overflow answer first, not by how-to articles. People also ask here asks for a Windows viewer, the meaning of ```, and the difficulty of learning Markdown: two of four questions are not about opening a file. Signal stops: PAA is Google's selection on one day.

SD-9. "markdown reader": reference and discussion sites hold the top two (markdownguide.org, Ask Ubuntu, whose title says "readers (not editors)"). A buyer who types "reader" is sometimes distinguishing from "editor".

SD-10. "markdown preview": the first page is almost wholly online tools and marketplace listings; no forum; no people-also-ask. The viewer would compete with browser tools that need no install. Signal stops: online tools are a free alternative that a buyer demonstrably finds; whether they prefer them is not shown.

SD-11. The adjacent term is "markdown editor". It was chosen for being the term every captured related search keeps returning to ("Best free Markdown editor" appears under "markdown reader"; "Markdown editor online" under "markdown preview"), and because the day-one pull's GitHub topic `markdown-editor` has 2,690 repositories against 1,008 for `markdown-viewer`; repository counts are supply, not demand. "Largest" is therefore unverified: no volume, no Trends. The first page is held by Medium, YouTube, Setapp, IONOS, Grammarist and LightPDF, which are media and roundup publishers, with an operator seat only for one online editor and a Play listing. Publishers rather than operators hold it, so on this capture it reads as a candidate page, not a candidate offering. It asks for editing, which the viewer does not do. Build-or-not question for the owner: is an editor in scope at all? Signal stops: one capture; the intent label that would settle it is missing.

SD-12. Every one of the seven pages carried an AI overview, and five of the seven showed no people-also-ask. What share of searchers click through is not measurable here. Signal stops: the capture shows the page, not behaviour.

SD-13. Operator words fold, table of contents, find and reload have no sign in the buyer-side suggestions captured. Silence on a page is a value, not a fact about the product: these words were not captured as terms, so their absence from the suggestions of seven pages says only that they did not surface there. Reload surfaces on the trade side (Hot Reload, live reload, auto reload).

SD-14. The season is unread. No Trends reading was made (the skill offers none), so there is no statement about the teaching year or editor release cycles. Interest, had it been read, would be relative and never money.

SD-15. There is no capacity ceiling for copies; the maker's hours are unrecorded. Demand above a ceiling cannot be separated from opportunity, because no ceiling is recorded.

SD-16. Where the signal stops, for the study as a whole: no volume exists this month; a capture is one buyer at one place on one day (Austin, Texas, 2026-10-09, desktop, English); interest is relative and never money, and none was read. Search says nothing about whether the operator can deliver, which is the capability leg's job.

# What the rank database would add when it has units again

Monthly volume per term, so the three layers can be summed apart; a difficulty score and competitive density to separate SD-5's crowded name from SD-6's open Linux page; intent labels to strike the terms that ask for editing, extensions or Mac and Windows apps; phrase-match and question expansions to test whether fold, table of contents, find and reload are searched at all; and an answer to whether "markdown editor" is in fact the largest adjacent term.
