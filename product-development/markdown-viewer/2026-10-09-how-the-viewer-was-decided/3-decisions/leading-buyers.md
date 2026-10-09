---
title: "The leading buyers' sentences, and the parameters they contain"
date: 2026-10-09
method: "SAGE Adjudicate, the card set (`sage-A-adjudicate.md`): a seller's sentence for each leading buyer on the buyer card, two sentences at most, said where the take-up is made; the parameters those sentences contain get cards, and a parameter in no sentence is design freedom by construction"
status: "Sentences and a parameter list. No parameter is given a value, an option ranking or a recommendation here; the cards do that. Written by the derivation clerk under `briefs/derivation-clerk-leading-buyers.md`."
---

# How to read this file

The leading buyers are the four the brief names from card 1: developers and coders (the recommendation), writers and authors (the runner-up), and the two between which the market-only reading in `3-decisions/third-card-1.md` withholds: developers and writers together as the documentation reader, and readers of what AI agents write. Card 0 (`3-decisions/third-card-0.md`) has one program for all four.

Each sentence is the one the market's own pages use to win that buyer, read from the reader rivals that name the buyer (rival register R1 to R86, "Whom its pages address") and from the findings. It is not a description of the program as it stands. Where a sentence promises something the program does not do today, the cost line from `1-competitions/capability-note.md` follows the sentence and travels with the parameter. A capability not yet built is a cost, not a bound.

`‹name›` marks where the offering's name goes. The owner calls the present name a placeholder (`3-decisions/questions.md`), and a deriving clerk carries no name for an offering not yet on sale.

The roster is the operator's 497-contact developer roster, dated 2026-04-04. A profile is named by its row number (its line in `roster.tsv`), the roster's own notes column, its star rating, response likelihood and warmth. The roster holds developers. For writers it holds no profile outside software documentation; the profile used there is the nearest one, and that fit is stated below.

The reader rivals naming each buyer, as tallied from the register sections:

- **Documentation reader.** 11 rivals name developers and writers together: R21, R22, R29, R30, R31, R50, R52, R57, R62, R84, R86. Nine of them are Mac App Store listings.
- **Readers of AI-agent output.** 8 rivals: R17, R20, R43, R44, R45, R48, R60, R73. Four are Mac App Store listings, two are on Homebrew (R17, R60) and two on the Snap Store (R20, R45).
- **Developers only.** 2 rivals: R7 and R76.
- **Writers only.** 1 rival: R35 (Marked).

Mac App Store listings name an audience far more often than pages in other cells (`third-card-1.md`: 16 of 31 App Store readers name one, against 8 of the other 55). So every per-buyer tally below leans toward what App Store listings print. Most of these rows also differ from the operator on shape dimensions 1 to 3.

# Developers and coders

**Sentence.** "‹name› is a free, open-source markdown reader for Linux, macOS and Windows that installs with one package command: open a README or any doc and it shows it as GitHub would, with a contents outline and find, redrawing each time you save. It never edits the file and never touches the network."

**Profile.** Row 17: "Linux/infrastructure engineer; Ubuntu mirror setup, domain configuration"; star rating 5, response likelihood 60, warmth existing_relationship.

**Likely answer.** He is warm, so he probably tries it if it really is one command away on his Ubuntu machines. On a server he reads a README in the terminal, where glow is the reader developers already install (59,634 Homebrew installs a year, N1). He reads one on GitHub itself when it is already pushed. So the window wins him only at a desktop. He may ask why not the editor's own preview (Markdown Preview Enhanced, 10,429,484 VS Code installs, N3).

**Cited.**
- **Whom it addresses.** Finding 2 (developers 28/204 in SHAPE, the leading named class there). Rival register R7 ("Document Reader for Developers") and R76 ("Designed for developers, CLI users, and AI-assisted workflows"). R31 ("Software Developers: Perfect for previewing README files") and R30 ("anyone who regularly opens README files or documentation"). R10, grip: "Render local readme files before sending off to GitHub"; "The styles and rendering come directly from GitHub".
- **Install route.** Finding 12 (package-manager command 73/204 in SHAPE, the largest install route there). D1 and N1 (the Homebrew formula top five are all terminal or preview readers: glow, grip, mdcat, mcat, mdless).
- **Free and open.** Findings 8 and 9 (SHAPE: free 156/204, a named open-source licence 137/204, no sale taken 51/204).
- **Platforms.** Finding 6. R9, glow (Linux, macOS, Windows, BSD). R76, leaf (macOS, Linux, Windows).
- **Rendering and features.** Finding 13 (GitHub Flavored Markdown 46/204). Finding 14 (outline 70/204). Finding 15. Finding 17 (reload on disk change 32/204). R76 ("Sidebar TOC", "Press / to search", "Auto-reload when the file changes on disk"). R10 (changes "instantly reflected").
- **Local and offline.** Finding 20.
- **Search demand.** SD-4 and SD-6 (the Linux results page is held by Unix StackExchange, Ask Ubuntu, ArchWiki and package listings, which are developer venues). SD-8 and SD-10 (browser tools that need no install).

**Cost lines that travel with this sentence.**
- **Package.** No package exists for this program. The sibling product's Debian package, RPM spec and Homebrew tap would be adapted to a program with no thread dependency and a different name. Being in a distribution's own archive is a further step the capability note does not cost.
- **Platforms.** The pipeline builds Linux x86_64 and arm64, macOS arm64 and Windows x86_64. It does not build for macOS Intel. Links call `xdg-open`, so a link with a URL scheme fails on macOS and Windows as the code stands. The maker has tested on Linux only.
- **"As GitHub would".** tkdown "is not a full CommonMark implementation". It leaves raw HTML, maths and diagrams outside its coverage, leaves footnote labels as written, and does not list task lists. Closing that gap is upstream work in a module the operator maintains.
- **"Redrawing each time you save".** The program does not watch the file; reload is F5.
- **"Open-source".** The repository has no LICENSE file.
- **Already in the program.** The outline (fold-all leaves the headings as a table of contents), find, read-only use and no network use.

# Writers and authors

**Sentence.** "Keep writing in the editor you like: ‹name›, a free reader for your Mac, sits beside it and shows your manuscript in whichever markdown flavour you write, as your readers will see it, in the style you pick, redrawing each time you save. When it's finished, print it or export it to PDF or HTML."

**Profile.** Row 486: "DITA Technical Committee, standards and technical documentation"; star rating 2, response likelihood 5, warmth known_of.

The fit is partial. The roster is a developer roster, and this is the one profile whose description names documentation work and not code. Rows 23 and 114 also name technical writing, but each beside development, so they belong to the documentation reader. The novelist, essayist and blogger whom the writer pages address (Typora, iA Writer, Ulysses, Marked on the strike list) have no row.

**Likely answer.** At this warmth and likelihood, probably no answer. If he does reply, his documents live in a documentation standard's own toolchain. He would ask whether the reader handles his markup and whether its PDF matches his publishing output, and judge it on the export. The one writers-only reader rival takes payment (Marked, one-time $14.99, R35). The writer's search page is an editor's page (SD-11). Both say a writer weighs this against the editor he already pays for, not against other readers.

**Cited.**
- **Whom it addresses.** Finding 2 (writers 71/496 in ALL, 23/204 in SHAPE). Strike list row "Writers and authors" (10 of 37 day-one pages; 6 of the 10 carry a price).
- **The sentence itself.** R35, Marked: "Marked 2 is a previewer (*not an editor*)"; "It updates live every time you save your document in your favorite text editor"; "9 preview styles built in"; "unlimited custom styles"; export "including HTML, PDF and Word"; "MultiMarkdown processing is provided for writers"; macOS only. R86, zerdo: "for authors who care about final output", PDF-first.
- **Feature findings.** Finding 4 (editors are four in five of ALL). Finding 13 (other named flavour 41/496). Finding 17. Finding 18 (themes 215/496, custom stylesheet 65/496). Finding 19 (PDF 196/496, HTML 152/496, print 79/496).
- **Platforms.** Finding 6, and taxonomy V05: the Mac App Store holds 31 of the 71 weighted rows naming writers, the largest share of any cell.
- **Search demand.** SD-9 and SD-11 (writer-facing publishers appear only on the "markdown editor" page). N6 (writers' store complaints are about being charged before use and about edits that lose work).

**Cost lines that travel with this sentence.**
- **"For your Mac".** A macOS arm64 image, `.app` and `.dmg` come from the sibling pipeline. Intel Macs are not covered, and scheme links fail on macOS (`xdg-open`).
- **"Whichever flavour you write".** tkdown is not full CommonMark, and no other flavour (MultiMarkdown, Discount) is in its stated coverage.
- **"In the style you pick".** Colours are fixed in the code, light. There are no themes.
- **"Redrawing each time you save".** There is no file watching.
- **"Print it or export it".** There is no print, export or copy of any kind.
- **"Free".** It holds for the operator, who has no means to take money. The writer market's readers take payment; that is the price parameter's business, not this sentence's.

# Developers and writers together: the documentation reader

**Sentence.** "For developers and technical writers who open READMEs and docs all day: ‹name› is a free reader, not an editor, that renders GitHub-flavoured markdown with its tables, diagrams and maths, gives you a contents outline and search, follows each save and exports to PDF, with nothing you open leaving your machine. Get it on the Mac App Store, or as a download for Windows and Linux."

**Profile.** Row 23: "Developer/technical writer; open source software discussion"; star rating 5, response likelihood 59, warmth existing_relationship.

**Likely answer.** He tries it. He points it first at his own READMEs and docs and checks the diagrams and tables. He compares it with GitHub's own rendering and with his editor's preview (N3). If he is on a Mac, he sets it against the Quick Look plug-in he may already have (QLMarkdown, 32,911 cask installs a year, N1). He keeps it if it renders his documents as faithfully as those do.

**Cited.**
- **Whom it addresses.** `third-card-1.md` (11 of 86 reader rivals, 9 of them Mac App Store). R30 ("Built for developers, technical writers, and anyone who regularly opens README files or documentation"; "This is a viewer, not an editor."). R57 ("Built for developers, writers, and anyone who keeps documentation in Markdown"; "intentionally read-only"). R52 ("Developers browsing project documentation / Writers reviewing Markdown drafts"; "Everything stays on your Mac, no cloud, no tracking"). R62 ("Built for people who live in markdown"; "Available for macOS, Windows & Linux"). R84 ("Developers reading READMEs and pull-request notes"; "Technical writers doing final-pass quality checks").
- **What these 11 claim.**

  | claim | rivals | of 11 |
  |---|---|---|
  | contents outline | R22, R30, R50, R52, R57, R62, R84 | 7 |
  | files stay local | R21, R22, R29, R50, R52, R84, R86 | 7 |
  | print or PDF | R21, R22, R30, R52, R62, R84, R86 | 7 |
  | diagrams | R21, R22, R50, R57, R62, R84 | 6 |
  | reload on disk change | R21, R22, R29, R50, R57, R62 | 6 |
  | maths | R21, R22, R50, R62, R84 | 5 |
  | search | R22, R30, R57, R62 (R52 undecidable) | 4 |

- **Price.** 5 state free only (R22, R29, R30, R31, R52). The other 6 name some payment.
- **Findings.** 4, 10, 13, 14, 15, 17, 19, 20.
- **Search demand.** SD-3 and SD-9 ("readers (not editors)" on the "markdown reader" page). SD-5 and SD-7 (store listings, GitHub and a Mac vendor roundup hold "md file viewer").

**Cost lines that travel with this sentence.**
- **"On the Mac App Store".** The operator has no store presence. The capability note costs a Flatpak manifest and a snapcraft recipe "from scratch" and names no Mac App Store route, so the cost of one is not recorded. That is an open cost, not a bar.
- **"A download for Windows and Linux".** The sibling pipeline's self-contained images for Windows x86_64 and Linux x86_64 and arm64 exist to be adapted. Scheme links fail on Windows and macOS (`xdg-open`).
- **"Diagrams and maths".** Both are outside tkdown's stated coverage.
- **"Follows each save".** There is no file watching.
- **"Exports to PDF".** There is no export.
- **Already in the program.** The outline, search (find), read-only use and nothing leaving the machine.

# Readers of what AI agents write

**Sentence.** "Your coding agent writes its plans and reports as markdown: keep ‹name› open beside it and read them rendered, diagrams and all, with an outline to jump through, refreshing the moment the agent rewrites the file. It is free to read and read-only, so it never fights the agent for the file, it is one `brew install` away, and nothing you open leaves your machine."

**Profile.** Row 277: "Full-stack software engineer: 8+ years system design, frontend, backend; JavaScript/Python/AI agents"; star rating 2, response likelihood 35, warmth known_of.

**Likely answer.** At this warmth he may not reply. If he does, he asks two things: does it refresh without a keypress, and why would he need a separate window when the editor his agent works in already previews the file? MacMD Viewer meets that objection in its own words: "people who already write in VS Code, Cursor or Obsidian and just want a fast, clean way to read the Markdown their AI agents ... keep [writing]" (R17). mdserve said the same sentence and is now archived (R60).

**Cited.**
- **Whom it addresses.** `third-card-1.md` (8 of 86 reader rivals; 3 of the 28 operator-shaped readers). R17 ("Read-only by design: you keep your editor for writing"; "live reload refreshes the preview the moment the file changes"). R60 ("built to give humans a live rendered view of the markdown that AI coding agents produce"; Homebrew formula; MIT). R43 ("the .md that AI assistants and coding agents produce"; "Your documents never leave your device."). R44 ("Reading costs nothing."). R48 ("You save your AI output as Markdown. Now you can actually read it."). R73 ("Free to read — forever."). R20 ("mhr never writes to the file it opens"). R45 ("files generated by AI agents").
- **What these 8 claim.**

  | claim | rivals | of 8 |
  |---|---|---|
  | contents outline | R17, R43, R44, R45, R48, R73 | 6 |
  | diagrams | R17, R43, R44, R45, R48, R60 | 6 |
  | reload on disk change | R17, R20, R45, R48, R60 | 5 |
  | files stay local | R17, R43, R44, R48, R73 | 5 |

  None of the 8 states folding.
- **Where these 8 are had.** Four are Mac App Store listings, two are on Homebrew and two on the Snap Store.
- **Findings.** 3 (12/496 name this buyer). 17. 20. 22 (made for AI output: 40/496 in ALL, 14/204 in SHAPE). 28.
- **Search demand.** SD-14 (every term's yearly mean rises steeply through 2025 and 2026). This is context and not a leg for the buyer: no term in the study names agents.

**Cost lines that travel with this sentence.**
- **"One `brew install` away".** The operator's Homebrew tap exists, and the sibling's formula would be adapted.
- **"Diagrams and all".** Diagrams are outside tkdown's stated coverage.
- **"Refreshing the moment the agent rewrites the file".** There is no file watching; reload is F5.
- **Already in the program.** The outline, read-only use, nothing leaving the machine, and "free".

# The parameters the sentences contain

Key to the sentence letters: **D** developers and coders, **W** writers and authors, **R** the documentation reader, **A** readers of what AI agents write.

"Differs by buyer" says whether the market evidence suggests the options or the recommendation would differ by buyer.
- No finding cross-tabulates a variable by V05 (whom the page addresses), so the per-buyer evidence is the reader-rival tallies above.
- Those tallies lean toward Mac App Store listings, and most of their rows differ from the operator on dimensions 1 to 3.
- Where a difference between buyers could be a difference between cells, the line says so and names the record that would separate the two.

"Search cards" says which of the four cards the method gives a search-demand leg (name, surface, unit, season) applies.

### 1. What is it called, and what do I type to find it?

- **Sentences:** D, W, R, A (the `‹name›` slot).
- **Differs by buyer:** not shown.
  - 8 of the 8 AI-output rivals and 9 of the 11 documentation-reader rivals carry a markdown token in the name (MarkRead, Read.md, MD Flow, Markdown Peek, Mdly).
  - The developers' largest readers carry none (glow, grip, R9 and R10).
  - The split follows the cell as much as the buyer: a markdown token appears in 118 of 134 Mac App Store names (finding 25) and in 25 of 84 GitHub editor-topic names (taxonomy V03). The record that would separate them is V03 by V05 within SHAPE.
- **Search cards:** name.
- **More than one way:**
  - Finding 25: function word 218/496, markdown token 216, none of the above 194, maker name 7.
  - SD-3 (viewer, reader, preview and editor used side by side).
  - SD-5 (the bare "markdown viewer" is crowded with same-word titles).
  - SD-9 ("reader" sometimes set against "editor").

### 2. Where do I get it, and who am I dealing with when I do?

- **Sentences:** D (a package command), R (the Mac App Store, or a download), A (Homebrew).
- **Differs by buyer:** suggested.
  - Documentation-reader rivals: 9 of 11 are Mac App Store listings.
  - AI-output rivals: 4 of 8 are on the App Store, 2 on Homebrew, 2 on the Snap Store.
  - Developers' readers lead the Homebrew formula list (D1, N1).
  - Writers' readers and editors are sold on stores and makers' sites (strike list; R35).
  - The App Store lean makes R's count partly a cell effect.
- **Search cards:** surface. It has no volume this month (SD-1), so the cluster's volume and the operator's share of it are the card's open fact.
- **More than one way:**
  - Finding 10 (V20: maker's own website 298/496, code repository 226, store listing 212, package registry 71, release page 49; in SHAPE the code repository leads at 135/204).
  - SD-5 to SD-10 (online tools, store listings, GitHub repositories, forums and package listings each hold first-page positions).
- **Cost:** no store presence; Flatpak and Snap recipes from scratch; a Mac App Store route not costed; GitHub releases and a Homebrew tap held; no software website.

### 3. What am I getting one of, and how does it get onto my machine and stay current?

This is one parameter in the sentences: the unit is the form the install takes. It covers both questions.md lines, "What am I getting one of?" and "How do I install it, and how do I keep it current?".

- **Sentences:** D (a package one command installs), R (a store install, or a downloaded copy), A (a Homebrew package).
- **Differs by buyer:** suggested, in step with parameter 2. The record that separates buyer from cell is V19 and V12(a) by V05.
- **Search cards:** unit, as the weaker evidence it is. The unit words in the captures are "download" ("MD file Viewer download", "Markdown viewer linux download", "MD viewer download") and "app" ("Markdown Viewer app", "App to open MD files").
- **More than one way:**
  - Finding 11: copy 325/496, system-maintained package 108, subscription per person 26; SHAPE: copy 141/204, package 52/204.
  - Finding 12: package-manager command 165/496, store install 130, build from source 115, installer 105, copy a binary 64; updates silent in 410/496.
- **Cost:** the packaging pipeline is to adapt; the repository has no installer or release today.

### 4. What does it cost?

- **Sentences:** D, W, R, A (each says free; A says "free to read").
- **Differs by buyer:** suggested.
  - Writers: the one writers-only reader charges (R35, one-time $14.99), and 6 of the 10 day-one writer pages carry a price.
  - Documentation reader: 5 of 11 state free only.
  - AI-output reader: 2 of 8 state free only. 4 sell a paid tier while saying reading is free (R17 one-time $19.99; R44, R48 and R73 with tiers). 2 are silent.
  - Developers: the leading readers are free or silent (R9, R10, R76).
  - All of these sit mostly in store rows that differ on dimension 2.
- **Search cards:** none. The method refuses search demand on the price card.
- **More than one way:**
  - Finding 8 (free 248/496, freemium 99, one-time purchase 92, donation invited 55, subscription 53, trial 49).
  - Findings 7 and 9.
  - N6 (the store's largest low-star cluster is a "free" listing gated after install).
- **Cost:** no payment mechanism of any kind exists. A paid option would need a store account, a checkout or licence-key path and a commercial licence text.

### 5. Can I use it at work, and can I read its source?

- **Sentences:** D ("open-source").
- **Differs by buyer:** not shown. Developers' readers state open-source licences (R9, R10, R60, R76 MIT). The App Store rows that dominate R and A are mostly silent on licence (V16(c) silent in 112 of 134 MAS rows), which is a cell effect. The record that would show it is V16(c) and V18 by V05.
- **Search cards:** none.
- **More than one way:**
  - Finding 8: V16(c) named open-source 240/496, proprietary 106, silent 146; V18 silent 466/496, with 14 offering a team licence, 6 stating work use free and 5 requiring a paid licence.
- **Cost:** the repository has no LICENSE file.

### 6. Will it run on my machine: which systems, and what do I need installed first?

- **Sentences:** D (Linux, macOS, Windows), W (Mac), R (Mac first, then Windows and Linux), A (implied by Homebrew).
- **Differs by buyer:** suggested, but confounded with cells.
  - Writers-only: R35 is macOS only.
  - Documentation reader: 9 of 11 are App Store listings, so macOS.
  - AI-output reader: macOS in 6 of 8, Linux in 3, Windows in 1.
  - Developers: glow and leaf name all three.
  - Finding 6 forbids reading platform through a cell. The record that would show it is V10 by V05 within SHAPE.
- **Search cards:** none of the four. SD-4 and SD-14 hold platform-qualified terms ("markdown viewer windows", "mac", "linux") as context.
- **More than one way:**
  - Finding 6: macOS 341/496, Linux 186, Windows 174; SHAPE 120, 81 and 70 of 204.
  - Finding 12, V11: minimum OS version 224/496, runtime named 73, none needed 13.
- **Cost:**
  - The program runs where Tcl 9 and Tk are installed; the pipeline's self-contained images remove that prerequisite for Linux x86_64 and arm64, macOS arm64 and Windows x86_64.
  - It does not build for macOS Intel.
  - `xdg-open` fails on macOS and Windows.
  - It has been tested on Linux only.

### 7. Will it open my files: which markdown, and what happens to the parts it does not understand?

- **Sentences:** D ("as GitHub would"), W ("whichever markdown flavour you write"), R (GitHub-flavoured, with tables, diagrams and maths), A ("diagrams and all").
- **Differs by buyer:** suggested.
  - Diagrams: 6 of 11 documentation-reader rivals and 6 of 8 AI-output rivals.
  - Maths: 5 of 11 and 4 of 8.
  - The writers-only rival names its own flavours (MultiMarkdown, Discount; R35).
  - The developers' README previewer promises GitHub's rendering (R10).
- **Search cards:** none. "Markdown Preview online with Mermaid" and "Markdown Preview Mermaid Support How to use" appear as related searches in the "markdown preview" capture, which is context.
- **More than one way:**
  - Finding 13: tables 215/496, maths 182, diagrams 167, GitHub Flavored Markdown 109, other named flavour 41, CommonMark 36; unrecognised content silent in 483/496.
- **Cost:** tkdown's coverage is as above. Raw HTML, maths and diagrams are outside it, footnote labels are left as written, and it is not full CommonMark. It is fixable upstream by the same hands.

### 8. Can I write in it, or only read?

- **Sentences:** D, W, R, A.
- **Differs by buyer:** suggested.
  - The writer market is an editor market: writers 71/496 in ALL, where four in five rows are editors (finding 4). The writer's search page asks for editing (SD-11).
  - The documentation-reader and AI-output rivals state read-only (R30, R57, R84; R17, R20, R43, R44, R48, R73).
- **Search cards:** none. SD-9 and SD-11 are context.
- **More than one way:**
  - Finding 4: editor with rendered view 305/496, editor with rendered view not stated 93, reader with editing not stated 66, reader stated read-only 22.

### 9. Does it keep up with a file I am editing elsewhere?

- **Sentences:** D, W, R, A.
- **Differs by buyer:** not shown. 5 of 8 AI-output rivals and 6 of 11 documentation-reader rivals state reload on disk change, and so do the writers-only R35 and the developer readers R10 and R76. The record that would show a difference is V31 by V05.
- **Search cards:** none. SD-13: "reload" surfaces on the trade side only.
- **More than one way:**
  - Finding 17: reloads on disk change 56/496, live preview of own typing 98, both 26, manual refresh 2, silent 294.
- **Cost:** the program does not watch the file; reload is F5, and it keeps folds and scroll.

### 10. How do I find my way around a long document?

- **Sentences:** D, R, A (a contents outline).
- **Differs by buyer:** not shown. 6 of 8 AI-output rivals and 7 of 11 documentation-reader rivals claim an outline. None of the 8 AI-output rivals states folding. The record is V28 by V05.
- **Search cards:** none. SD-13: "table of contents" and "fold" do not appear in buyer-side suggestions.
- **More than one way:**
  - Finding 14: outline 158/496, jump to heading 69, scroll kept 59, folding 28, bookmarks 12, silent 296.
- **Capability:** fold-all leaves the headings as a table of contents. There is no separate outline pane.

### 11. How do I find a word in it?

- **Sentences:** D ("find"), R ("search").
- **Differs by buyer:** not shown. 4 of 11 documentation-reader rivals and 5 of 8 AI-output rivals claim search. The record is V29 by V05.
- **Search cards:** none.
- **More than one way:**
  - Finding 15: within the document 94/496, across a folder 100, find and replace 66, regular expressions 18, undecidable 70.
- **Capability:** the find bar exists and reaches folded sections and table cells.

### 12. Does it need the network, and does anything leave my machine?

- **Sentences:** D ("never touches the network"), R and A ("nothing you open leaving your machine").
- **Differs by buyer:** not shown. 7 of 11 documentation-reader and 5 of 8 AI-output rivals state local. The App Store's privacy declaration inflates the stated rate in that cell (finding 20: 101 of the 180 no-telemetry rows are MAS rows).
- **Search cards:** none.
- **More than one way:**
  - Finding 20: local 124/496, local with optional upload 101, content leaves the device 13 (grip by default, R10), silent 227.
- **Capability:** the program uses no network; only a link hands off to `xdg-open`.

### 13. What does it look like, and can I change that?

- **Sentences:** W ("in the style you pick").
- **Differs by buyer:** not shown. The writers-only rival sells styles (R35: 9 built-in styles, custom styles), and reader rivals for every buyer claim light and dark. The record is V32 by V05.
- **Search cards:** none.
- **More than one way:**
  - Finding 18: themes 215/496, light and dark 170, font or size 104, custom stylesheet 65, follows the system 59.
- **Cost:** colours are fixed in the code, light; no themes.

### 14. Can I print it, export it, or send it on?

- **Sentences:** W (print, PDF, HTML), R (PDF).
- **Differs by buyer:** suggested for writers. Output is the writers-only rival's selling point (R35: HTML, PDF and Word), and the technical-author rival is PDF-first (R86). Export is also claimed by 7 of 11 documentation-reader and 6 of 8 AI-output rivals. The record is V33 by V05.
- **Search cards:** none.
- **More than one way:**
  - Finding 19: PDF 196/496, HTML 152, another format 145, share 81, print 79, copy as rich text 39, silent 193.
- **Cost:** no print, export or copy exists.

### 15. Is this one thing or several?

- **Sentences:** D, W, R, A. Each offers one program; a "Pro" edition or a sibling tool would change each sentence.
- **Differs by buyer:** not suggested. 14 of the 24 reader rivals that name any buyer name two or more for one program (`third-card-0.md`). The AI-output rivals that sell an edition still say reading is free (R44, R73).
- **Search cards:** none.
- **More than one way:**
  - Finding 26: single program 314/496, editions 100, family 40, program and component 7; SHAPE: 162, 9, 18 and 2 of 204.
  - This is card 0, already derived.

"Who is this for?" is the buyer card itself, which each sentence answers by whom it addresses; it is not listed again.

### The questions in `3-decisions/questions.md` that fall out

These are in no sentence, so each is design freedom by construction.

- **When? (season, and the product's cadence).** No sentence names a time. The season leg exists (SD-14: June peaks and December troughs for most terms), but no sentence carries it, so the season card has no parameter to rule.
- **What happens when I click a link, an image, or a reference to another file?** One documentation-reader rival claims following links to other markdown files (R21); no sentence carries it.
- **Where do I get help, and what happens when it breaks?** No sentence carries it.
- **Who else uses it, and will it still exist next year?** No sentence carries it.
- **What does "sold" mean here?** This is not a parameter of its own. It is answered by parameters 3 and 4, the take-up and its cost.
- **What is a small change?** The owner's scoping ruling for the Game, not a card, as questions.md says.

# Readings, text generator against product designer

- **Brief and standing block.** A generator would write four product descriptions; a designer writes what wins each buyer and puts a cost beside every promise the program cannot yet keep.
- **Method.** A generator would turn every feature into a card; a designer makes a card only of what changes a sentence, and leaves the rest open on purpose.
- **Findings and taxonomy.** A generator reads the commonest values as what buyers want; a designer reads which population each rate was measured in, and notes that no finding cuts any variable by buyer.
- **Rival register.** A generator would count every product that names a buyer; a designer sees that most of those that do are App Store listings, so the per-buyer tallies show what one store prints.
- **Search findings.** A generator would rank names by traffic; a designer notes there is no volume, only who holds each results page on one day in one place.
- **Distributor notes.** A generator reads millions of editor-preview installs as demand for a viewer; a designer reads that the developer already has a preview inside his editor, and the new readers are small.
- **Sales record and capability note.** A generator would read "no package, no watch, no export" as limits; a designer reads them as cost lines, the state of an unlaunched product.
- **Roster.** A generator would address the warmest contact; a designer addresses the contact whose own description matches the buyer, and says where none does.
