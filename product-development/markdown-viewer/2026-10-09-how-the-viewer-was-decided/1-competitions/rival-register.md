---
title: "Rival register: the incumbents to beat"
date: 2026-10-09
method: "SAGE Survey section 2, the rival register, written by the rival-register clerk under briefs/rival-register-clerk.md; sections are built from the 449 rows of the coded corpus (cells quoted as coded) and the frame lists' own counts"
status: "Register of rivals and the demand signals around them. It values no parameter of the offering and decides nothing alone."
---

# How the register was drawn

The offering is bound to no place, so the rivals are the comparables a buyer weighs when opening a markdown file on a platform the operator can ship to. The capability note names those platforms: Linux (x86_64 and arm64), macOS (arm64) and Windows (x86_64), through the sibling product's release pipeline and Homebrew tap.

**The rule.** A comparable is registered if either holds:

1. the coded corpus codes it as reading markdown files without editing them, since that is the operator's own kind: V01 is eligible and the V09 value (the text before the first bracket, brace, guillemet, "::", "@", quote or colon-and-space) is "reader, stated read-only" or "reader, editing not stated"; or
2. in a frame cell it is one of the five comparables with the largest published demand (installs, stars, likes or rating counts as that cell publishes them), among the cell's comparables that the corpus codes eligible.

A product in several cells is one section. Counts: 86 comparables meet the first test; 48 meet the second in at least one cell, of which 13 also meet the first and 35 meet only the second. **121 sections, R1 to R121**: R1 to R86 are the first-test products in alphabetical order, the rest the second-test-only products in alphabetical order.

**How the cells were read.**

- The corpus was parsed with the csv module (449 rows, 39 columns). Two layout facts of the corpus were met and handled: some cells begin with a shard marker such as "(e)" or "(r)", which is dropped before the value is read; and some cells open the quote with a plain double quote or a parenthesis, which ends the value as a bracket does. One row, kookbook, is coded "reader, editing not stated" but V01 undecidable; it is not registered.
- Cell membership is the "cells" column of `0-comparables/frame/collection-list.tsv`. A row's counts were taken from the per-list TSV row for the same entry (matched on the identifier, else the name; every membership matched).
- Demand is the figure the list publishes, per cell: Flathub installs last month; Mac App Store rating count; AlternativeTo likes; GitHub-topic stars; Homebrew 365-day installs (the 30- and 90-day counts are in each section); VS Code installs. Figures are never set against another cell's: the frame review forbids comparing popularity across lists (six different instruments).
- Cells that publish no demand figure, so draw no five: the Snap Store (the API returns no install, rating or download counts), the Ubuntu 25.04 archive (apt-cache gives none), awesome-claude-code (no counts in the list text), and the Tcl wiki lists (no counts on the page; its tklib membership holds one eligible comparable, shtmlview, which is a component). The Chrome Web Store cell is ruled no-go in the frame review (the first ten results of two queries); no comparable was drawn from it, and its two collected products (md-reader and Markdown Here) sit in other cells. The teatotal cell is the operator's own component and is excluded.
- Mac App Store caveat, from the frame review: Mac-only listings publish a rating count of 0, an instrument artefact, so a top five by rating count is a top five among listings that report any (the section says how many are non-zero). It is a ranking inside the cell and a lead on what a Mac buyer meets, not a popularity statement.
- AlternativeTo caveat: likes are a crowd's links to four anchor products (Typora, Obsidian, Marked, Glow), not installs; a listing showing "Like" with no number is read as no figure.
- The corpus cells are quoted as coded, with their own quote marks and source tags, clipped at a stated length where long ("[clipped]" marks the cut). Silence is recorded as "not stated"; it is not a fact about the product. Lines marked N1 to N6 point to sections of `1-competitions/distributor-notes.md`; lines in a section's "Further" clause come from those notes and are marked with the note number.
- "Platform the buyer must already hold" is read from the V10 cell, restricted to the operator's three platforms. "None of the three named" means V10 names none of them (a host program, a browser, a mobile system, or silence); it does not mean the product fails to run there.
- Sections were built from the corpus rows. The profile files under `0-comparables/products/` are the evidence behind those rows and are cited per section; they were opened only for spot checks (glow, mdcat, read-md, markdown-all-in-one, telari), so a cell the second coding corrected is read as it stands in the corpus.

# The rivals


## R1. Auto-Open Markdown Preview

Slug `auto-open-markdown-preview`; profile `0-comparables/products/auto-open-markdown-preview.md`. Registered because: coded as reading without editing (V09: reader, editing not stated). Cells: vscode.

- **Publishes about itself.**
  - Kind (V08): editor extension ("Extension for Visual Studio Code", marketplace.visualstudio.com)
  - Reader or editor (V09): reader, editing not stated ("This VS Code extension automatically shows Markdown preview whenever you open new Markdown file.", [clipped]
  - Platforms (V10): inside a host program ("Visual Studio Code", marketplace.visualstudio.com)
  - Markdown forms claimed (V13): markdown named, no form named ("Markdown", marketplace.visualstudio.com); (b) not stated
  - Features the questions ask about: V28 to V33 and V14 all not stated
- **Charges.** Free (marketplace.visualstudio.com price field); (b) free; (c) not stated
- **Buyer's all-in cost**, from the page text: price shape (V16b) free; beyond the price (V17): not stated; prerequisites (V11): host program named ("Extension for Visual Studio Code", marketplace.visualstudio.com); platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): none of the three named.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): vscode: installs=671717; ratings=35; average=3.97; lastUpdated=2017-03-04
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** 2017-03-04 (version 0.0.4, Marketplace Version History "Sat, 04 Mar 2017 07:15:33 GMT"; Changelog "version 0.0.4(2017/03/04)"; day precision); (b) not stated

## R2. bookmark.md

Slug `bookmark-md`; profile `0-comparables/products/bookmark-md.md`. Registered because: coded as reading without editing (V09: reader, editing not stated). Cells: Mac App Store.

- **Publishes about itself.**
  - Kind (V08): desktop application ("Only for Mac", apps.apple.com)
  - Reader or editor (V09): reader, editing not stated ("Bookmark is a simple, fast, and resilient Markdown viewer specifically designed for book in markdown.", apps.apple.com)
  - Platforms (V10): macOS ("Requires macOS 11.5 or later.", apps.apple.com)
  - Markdown forms claimed (V13): markdown named, no form named ("Bookmark introduces a new format for markdown books.", apps.apple.com); (b) not stated
  - Features the questions ask about: V28 to V33 and V14 all not stated
- **Charges.** Free (apps.apple.com price field); (b) free; (c) not stated
- **Buyer's all-in cost**, from the page text: price shape (V16b) free; beyond the price (V17): not stated; prerequisites (V11): minimum operating-system version named ("Requires macOS 11.5 or later.", apps.apple.com); platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): macOS.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): Mac App Store: userRatingCount=0; averageUserRating=0
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** 05/13/2025 ("Version 1.2 05/13/2025", Version History, apps.apple.com; day precision); (b) not stated

## R3. d0c-s4vage/lookatme

Slug `d0c-s4vage-lookatme`; profile `0-comparables/products/d0c-s4vage-lookatme.md`. Registered because: coded as reading without editing (V09: reader, editing not stated); and top five in github-topics:markdown-viewer by stars (5 of 21 eligible comparables with a figure; 2,332). Cells: github-topics:markdown-viewer.

- **Publishes about itself.**
  - Kind (V08): terminal program ["terminal-based markdown presentation tool" @readme]
  - Reader or editor (V09): reader, editing not stated ["Markdown rendering" @readme; "renders Markdown documents" @apt]
  - Platforms (V10): Linux ["Origin: Ubuntu" @apt]
  - Markdown forms claimed (V13): (a) front matter ["Styling and settings embedded within the Markdown YAML header" @docs] (b) not stated
  - Features the questions ask about: file changed elsewhere V31: undecidable ["Live (input file modification time watching) and manual reloading" @readme] | appearance V32: themes provided ["Themes" @docs; "--style [default|emacs|friendly|...]" @readme]; light and dark modes ["-t, --theme [dark|light]" @readme]
- **Charges.** (a) not stated (b) not stated (c) named open-source licence: "MIT License" [@api licence field]
- **Buyer's all-in cost**, from the page text: price shape (V16b) not stated; beyond the price (V17): not stated; prerequisites (V11): undecidable ["Depends: python3-click, python3-marshmallow, python3-mistune0, python3-pygments, python3-urwid, python3-yaml, python3:any" @apt]; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): Linux.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): github-topics:markdown-viewer: stars=2332; archived=false; last_push=2024-04-02
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** (a) 2023-03-14 (release, day, v3.0.0-rc5, @api releases) (b) not stated

## R4. ekphos

Slug `ekphos`; profile `0-comparables/products/ekphos.md`. Registered because: coded as reading without editing (V09: reader, editing not stated). Cells: homebrew:formula.

- **Publishes about itself.**
  - Kind (V08): terminal program ["terminal-based markdown research tool" @docs]
  - Reader or editor (V09): reader, editing not stated ["Three-panel layout - Sidebar, content view, and outline navigation" @docs]
  - Platforms (V10): macOS ["macOS on Apple Silicon golden gate ✅ tahoe ✅ sequoia ✅" @formula]; Linux ["Linux ARM64 ✅ x86_64 ✅" @formula]
  - Markdown forms claimed (V13): (a) wiki-links ["Wiki links - Obsidian-style [[note]] linking with autocomplete" @docs]; syntax-highlighted code blocks ["Syntax highlighting - 50+ languages supported in code blocks" @docs] (b) not [clipped]
  - Features the questions ask about: navigation V28: outline, contents or headings sidebar ["outline navigation" @docs] | find V29: search across files or a folder ["Fuzzy file search and full-text content search (Ctrl+k)" @docs] | appearance V32: themes provided ["Customizable themes - TOML-based theming with a live theme selector (Ctrl+t)" @docs]
- **Charges.** (a) not stated (b) not stated (c) named open-source licence: "License: MIT" [@formula]
- **Buyer's all-in cost**, from the page text: price shape (V16b) not stated; beyond the price (V17): not stated; prerequisites (V11): build toolchain named ["Requirements: Rust 1.70+" @docs; "Depends on when building from source: rust 1.99.0" @formula]; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): Linux, macOS.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): homebrew:formula: 30d=49; 90d=98; 365d=756
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** (a) not stated (b) not stated

## R5. Essentialist

Slug `essentialist`; profile `0-comparables/products/essentialist.md`. Registered because: coded as reading without editing (V09: reader, editing not stated). Cells: Flathub.

- **Publishes about itself.**
  - Kind (V08): desktop application ["Application for desktops (Windows, MacOS and Linux)" @readme]; mobile application ["and mobile (Android)" @readme]; terminal [clipped]
  - Reader or editor (V09): reader, editing not stated ["Essentialist supports a variety of Markdown features, including lists, tables, emojis, and basic text styling" @flathub]
  - Platforms (V10): Windows; macOS ["Essentialist is also available on Windows, MacOS, and Android." @flathub]; Android [same quote]; Linux ["Application for desktops [clipped]
  - Markdown forms claimed (V13): (a) tables ["lists, tables, emojis" @flathub]; math ["basic support for math rendering using standard LaTeX syntax" @readme] (b) not stated
  - Features the questions ask about: appearance V32: themes provided ["It includes a dark theme" @site] | files stay local V14: local, stated ["keeping your data right where it belongs: on your device" @flathub]
- **Charges.** (a) "Free" [@flathub label] (b) free (c) named open-source licence: "MIT License" [@api licence field]
- **Buyer's all-in cost**, from the page text: price shape (V16b) free; beyond the price (V17): not stated; prerequisites (V11): not stated; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): Linux, macOS, Windows.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): Flathub: installs_last_month=96; favorites_count=1
- **Whom its pages address (V05):** Students and academics ["This is a perfect workflow for students and anyone who takes notes" @flathub]; Note-takers and personal knowledge managers ["anyone who takes notes" @flathub]
- **Last release and maintenance (V27):** (a) 2025-10-10 (release, day, v0.3.22, @api releases) (b) not stated

## R6. FlyCrys

Slug `flycrys`; profile `0-comparables/products/flycrys.md`. Registered because: coded as reading without editing (V09: reader, stated read-only). Cells: awesome-claude-code.

- **Publishes about itself.**
  - Kind (V08): desktop application «Native Linux GUI for Claude Code agents. Rust + GTK4.» (repository description)
  - Reader or editor (V09): reader, stated read-only «It doesn't edit files.» (README)
  - Platforms (V10): Linux «Native Linux GUI»; Debian / Ubuntu, Fedora, Arch headings (README)
  - Markdown forms claimed (V13): tables «Streaming markdown rendering (tables, code blocks, lists, blockquotes)»; Markdown preview (README); (b) not stated
  - Features the questions ask about: find V29: search within document «In-view find bar (Ctrl+F)»; search across files or a folder «Search (filters across entire project)» (README) | appearance V32: follows the system appearance, stated «follows system theme»; light and dark modes «Light/dark theme toggle» (README)
- **Charges.** «Zero cost — no subscription, no API proxy, uses your own Claude Code CLI» (README); (b) free; (c) named open-source licence: MIT «MIT. See LICENSE.» (README)
- **Buyer's all-in cost**, from the page text: price shape (V16b) free; beyond the price (V17): another product or subscription required, stated «FlyCrys requires the Claude Code CLI» (README); prerequisites (V11): runtime or interpreter named «System deps: GTK4, VTE4, WebKitGTK 6.0, libsoup 3.0» (README, toolkits); platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): Linux.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): awesome-claude-code: section="Alternative Clients"; README line 288; no install or star count in the list text
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** 2026-06-18 (release v0.5.0, API); 2026-09-04 (commit) noted; (b) archived, deprecated or unmaintained, stated «No longer actively developed ... development has stopped» (README); repository field archived: false noted

## R7. Folio: Markdown+RST+Code+PDF

Slug `folio-markdown-rst-code-pdf`; profile `0-comparables/products/folio-markdown-rst-code-pdf.md`. Registered because: coded as reading without editing (V09: reader, editing not stated). Cells: Mac App Store.

- **Publishes about itself.**
  - Kind (V08): mobile application and desktop application «a quiet, native reader ... on iPhone, iPad, and Mac» (site); «a small, native reader» (listing)
  - Reader or editor (V09): reader, editing not stated «a small, native reader»; «Show Source reveals the document's own text» (listing)
  - Platforms (V10): iOS «Requires iOS 17.0 or later. iPhone»; iPadOS «Requires iPadOS 17.0 or later. iPad»; macOS «Requires macOS 14.0 or later. Mac» (listing)
  - Markdown forms claimed (V13): tables, task lists «Headings, lists, tables, task lists, blockquotes, code blocks, links, and images render» (listing); math «Equations in TeX notation render offline»; diagrams «embedded support for [clipped]
  - Features the questions ask about: navigation V28: outline, contents or headings sidebar; jump to heading or section «An outline jumps between headings» (listing) | find V29: search within document «Find highlights every match» (listing) | links and images V30: shows remote images «A single switch stops documents from loading images from the web» (listing) | appearance V32: light and dark modes «in light or dark»; font or size choice «serif or sans-serif type, and with text size, line spacing, and page width [clipped] | print and export V33: print «on Mac, Print» (Folio Plus); export to PDF «Export PDF»; share or send from the product «Share offers the source file or a PDF of [clipped] | files stay local V14: local, stated «Documents, bookmarks, and settings stay on your device.» (listing); «Your files stay on your device» (site)
- **Charges.** «Read complete text documents up to 10 KB for free, and view PDFs and images without limit» ; «Folio Plus Lifetime: a one-time purchase of $19.99 (USD); Folio Plus Yearly: an auto-renewing subscription of $9.99 (USD) per year» (listing); (b) free [clipped]
- **Buyer's all-in cost**, from the page text: price shape (V16b) free with paid tier or features, one-time purchase, subscription; beyond the price (V17): not stated; prerequisites (V11): minimum operating-system version named «Requires iOS 17, iPadOS 17, or macOS 14 or later» (listing); platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): macOS.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): Mac App Store: userRatingCount=0; averageUserRating=0
- **Whom its pages address (V05):** Developers and coders «Document Reader for Developers» (listing subtitle)
- **Last release and maintenance (V27):** «1.1 1d ago» (listing version history, captured 2026-10-09, relative); (b) not stated

## R8. geany-plugin-markdown

Slug `geany-plugin-markdown`; profile `0-comparables/products/geany-plugin-markdown.md`. Registered because: coded as reading without editing (V09: reader, editing not stated). Cells: debian:apt-cache search markdown.

- **Publishes about itself.**
  - Kind (V08): editor extension «markdown plugin for Geany» (apt)
  - Reader or editor (V09): reader, editing not stated «real-time preview of rendered Markdown» (apt, plugin page)
  - Platforms (V10): inside a host program «markdown plugin for Geany» (apt); apt «Architecture: amd64» names no operating system
  - Markdown forms claimed (V13): markdown named, no form named «rendered Markdown» (plugin page); «The preview is active by default for all documents with a Markdown filetype set.»; (b) not stated
  - Features the questions ask about: file changed elsewhere V31: preview updates as you type inside the product, stated «Updates the preview on-the-fly as you type, automatically.» (plugin page; typing is [clipped] | appearance V32: font or size choice «Allows simple customization of fonts and colours» (plugin page)
- **Charges.** not stated; (b) not stated; (c) named open-source licence: GNU General Public License, version 2 «The Markdown plugin is licensed under the GNU General Public License, version 2.»; BSD-style licence for the discount directory (plugin page); GPLv2 or [clipped]
- **Buyer's all-in cost**, from the page text: price shape (V16b) not stated; beyond the price (V17): not stated; prerequisites (V11): host program named «Depends: ... geany (>= 2.0)» (apt); runtime or interpreter named «GTK+ 3.0 or greater», «WebKitGTK+ API 4.0 or 4.1» (plugin page [clipped]; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): none of the three named.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): debian:apt-cache search markdown: not published by the list (no install count in apt-cache)
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** not stated; (b) not stated

## R9. Glow

Slug `glow`; profile `0-comparables/products/glow.md`. Registered because: coded as reading without editing (V09: reader, editing not stated); and top five in homebrew:formula by 365-day installs (1 of 17 eligible comparables with a figure; 59,634). Cells: alternativeto:Typora; alternativeto:Marked (AlternativeTo entry for Marked); debian:apt-cache search markdown; homebrew:formula; Snap Store.

- **Publishes about itself.**
  - Kind (V08): terminal program «Glow is a terminal based markdown reader»; «Glow has a CLI for working with Markdown» (README)
  - Reader or editor (V09): reader, editing not stated «Glow is a terminal based markdown reader» (README)
  - Platforms (V10): macOS «# macOS or Linux»; Linux; Windows «choco install glow», «winget install charmbracelet.glow»; BSD «# FreeBSD» (README); AlternativeTo [clipped]
  - Markdown forms claimed (V13): markdown named, no form named «Markdown files can be read with Glow's high-performance pager.» (README); (b) not stated
  - Features the questions ask about: appearance V32: light and dark modes «automatically picks either the dark or the light style for you» (README); custom stylesheet «supply a custom JSON [clipped]
- **Charges.** «Cost / License: Free, Open Source (MIT)» (AlternativeTo); price text on README, Snap, Homebrew, apt: none; (b) free; (c) named open-source licence: MIT «MIT» (README, Homebrew, Snap, AlternativeTo)
- **Buyer's all-in cost**, from the page text: price shape (V16b) free; beyond the price (V17): not stated; prerequisites (V11): build toolchain named «Depends on when building from source: go 1.27.2» (Homebrew); platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): Linux, macOS, Windows.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): alternativeto:Typora: rank=139; page=12; 3 likes; alternatives-listed-for-this-entry=52; license=Free Open Source (MIT) Platforms Mac Windows Linux BSD More about Glow Good alternative? Is [clipped] || alternativeto:Marked (AlternativeTo entry for Marked): rank=42; page=4; 3 likes; alternatives-listed-for-this-entry=not shown; license=Free Open Source (MIT) Platforms Mac Windows Linux BSD More about Glow Good alternative? [clipped] || debian:apt-cache search markdown: not published by the list (no install count in apt-cache) || homebrew:formula: 30d=4,145; 90d=19,272; 365d=59,634 || Snap Store: none given by API (find returns no install, rating or download counts).  Further: GitHub charmbracelet/glow: not archived; last push 2026-10-05; 24 releases, newest v3.0.0 2026-08-11; 2 releases in the last 365 days, 285,591 release-asset downloads (N5). Homebrew growth 0.83 (N1). PyPI 'glow' 935 last month, not confirmed to be this tool (N4).
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** 2026-08-11 (release v3.0.0, API); Homebrew stable 3.0.0; Snap «Last updated 30 May 2025» (older); 2026-10-05 (commit) noted; (b) not stated

## R10. grip

Slug `grip`; profile `0-comparables/products/grip.md`. Registered because: coded as reading without editing (V09: reader, editing not stated); and top five in homebrew:formula by 365-day installs (2 of 17 eligible comparables with a figure; 5,370). Cells: debian:apt-cache search markdown; homebrew:formula.

- **Publishes about itself.**
  - Kind (V08): terminal program «a command-line server application written in Python» (README, apt)
  - Reader or editor (V09): reader, editing not stated «Render local readme files before sending off to GitHub.» (README)
  - Platforms (V10): macOS «On OS X, you can also install with Homebrew»; Linux (Homebrew bottle table «Linux ARM64, x86_64»)
  - Markdown forms claimed (V13): markdown named, no form named «GitHub Markdown previewer» (Homebrew); «The styles and rendering come directly from GitHub» (README); (b) not stated
  - Features the questions ask about: file changed elsewhere V31: reloads when the file changes on disk, stated «Changes you make to the Readme will be instantly reflected in the browser without requiring [clipped] | print and export V33: export to HTML «export to a single HTML file, with all the styles and assets inlined: grip --export» (README) | files stay local V14: content leaves the device, stated «Privacy notice: by default all documents will be sent to GitHub (Microsoft).» (apt)
- **Charges.** not stated; (b) not stated; (c) named open-source licence: MIT «License: MIT» (Homebrew)
- **Buyer's all-in cost**, from the page text: price shape (V16b) not stated; beyond the price (V17): not stated; prerequisites (V11): runtime or interpreter named «Depends on: certifi 2026.7.22, python@3.14 3.14.8» (Homebrew); platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): Linux, macOS.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): debian:apt-cache search markdown: not published by the list (no install count in apt-cache) || homebrew:formula: 30d=345; 90d=667; 365d=5,370.  Further: PyPI 30,167 downloads last month, last release 4.6.2 on 2023-10-12 (N4). GitHub joeyespo/grip: not archived; no releases, newest tag v4.6.1; last push 2024-07-10 (N5). Homebrew growth 0.77 (N1).
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** 2024-07-10 (commit); releases list empty (API); Homebrew stable 4.6.2; (b) not stated

## R11. ianks/octodown

Slug `ianks-octodown`; profile `0-comparables/products/ianks-octodown.md`. Registered because: coded as reading without editing (V09: reader, editing not stated). Cells: github-topics:markdown-editor.

- **Publishes about itself.**
  - Kind (V08): terminal program [S1 "straight from your shell"; "from inside of a Terminal"]
  - Reader or editor (V09): reader, editing not stated [S1 "Github markdown previewing"]
  - Platforms (V10): macOS [S1 "Mac: brew install icu4c cmake pkg-config"]
  - Markdown forms claimed (V13): GitHub Flavored Markdown [S1 topic "github-flavored-markdown"; "the same markdown parsers and CSS as Github"]; (b) not stated
  - Features the questions ask about: file changed elsewhere V31: undecidable | appearance V32: themes provided [S1 "Multiple CSS styles. octodown --style atom README.md"] | print and export V33: export to HTML [S1 "octodown --raw --stdin > index.html"]
- **Charges.** not stated; (b) not stated; (c) named open-source licence: MIT license [S1 repository field]
- **Buyer's all-in cost**, from the page text: price shape (V16b) not stated; beyond the price (V17): not stated; prerequisites (V11): runtime or interpreter named [S1 "Requirements: Ruby >= 2.0"]; build toolchain named [S1 "Install icu4c and cmake"]; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): macOS.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): github-topics:markdown-editor: stars=690; archived=false; last_push=2023-03-01
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** 04 May 15:10 (no year; S2 release v1.8.0); (b) not stated

## R12. inlyne

Slug `inlyne`; profile `0-comparables/products/inlyne.md`. Registered because: coded as reading without editing (V09: reader, editing not stated). Cells: homebrew:formula.

- **Publishes about itself.**
  - Kind (V08): terminal program [S2 "Use inlyne --help to see all the command line options."]
  - Reader or editor (V09): reader, editing not stated [S1 "view markdown files"; S2 "allow you to make edits on the fly" refers to another program]
  - Platforms (V10): macOS [S1 bottles "macOS on Apple Silicon ... Intel"]; Linux [S1 "Linux ARM64 x86_64"]
  - Markdown forms claimed (V13): tables [S2 "Tables"]; task lists [S2 "Tasklists"]; syntax-highlighted code blocks [S2 "Code Blocks (with syntect highlighting)"]; raw HTML [S2 "Basic HTML Rendering"]; (b) not stated
  - Features the questions ask about: file changed elsewhere V31: reloads when the file changes on disk, stated [S2 "Live Code Change - Inlyne will monitor your markdown file for any write modifications [clipped]
- **Charges.** not stated; (b) not stated; (c) named open-source licence: MIT [S1 "License: MIT"; S2 "MIT license"]
- **Buyer's all-in cost**, from the page text: price shape (V16b) not stated; beyond the price (V17): not stated; prerequisites (V11): build toolchain named [S2 "cargo with a somewhat recent Rust toolchain; A C-compiler"] (for building from source); platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): Linux, macOS.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): homebrew:formula: 30d=15; 90d=103; 365d=451.  Further: GitHub Inlyne-Project/inlyne: not archived; last push 2026-08-06; newest release v0.5.3 2026-08-06; 4 releases in the last 365 days, 1,398 downloads (N5). Homebrew growth 0.40 (N1).
- **Whom its pages address (V05):** undecidable
- **Last release and maintenance (V27):** 06 Aug 09:42 (no year; S3 "released this 06 Aug 09:42 v0.5.3"); (b) not stated

## R13. Instant Markdown

Slug `instant-markdown`; profile `0-comparables/products/instant-markdown.md`. Registered because: coded as reading without editing (V09: reader, editing not stated). Cells: vscode.

- **Publishes about itself.**
  - Kind (V08): editor extension [S2 "vscode extension for instant markdown previews"]
  - Reader or editor (V09): reader, editing not stated [S2 "edit markdown documents in vscode and instantly preview it in your browser"]
  - Platforms (V10): macOS [S2 "Mac & Linux"]; Linux [S2]; Windows [S2 "Windows"]
  - Markdown forms claimed (V13): math [S2 "markdown-it-mathjax"]; diagrams [S2 "markdown-it-plantuml"]; task lists [S2 "markdown-it-task-lists"]; (b) not stated
  - Features the questions ask about: file changed elsewhere V31: undecidable
- **Charges.** Free [S1]; (b) free [S1 "Free"]; (c) named open-source licence: MIT [S1, S2 "MIT © David Bankier @dbankier"]
- **Buyer's all-in cost**, from the page text: price shape (V16b) free; beyond the price (V17): not stated; prerequisites (V11): host program named [S2 "vscode extension"]; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): Linux, macOS, Windows.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): vscode: installs=164280; ratings=39; average=3.46; lastUpdated=2021-05-11
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** not stated; (b) not stated

## R14. Just a Markdown Viewer

Slug `just-a-markdown-viewer`; profile `0-comparables/products/just-a-markdown-viewer.md`. Registered because: coded as reading without editing (V09: reader, stated read-only). Cells: Mac App Store.

- **Publishes about itself.**
  - Kind (V08): desktop application [S2 "A view-only markdown reader for macOS, iOS, and iPadOS."]; mobile application [S2 "iOS, and iPadOS"; "iPhone & iPad"]
  - Reader or editor (V09): reader, stated read-only [S2 "View only — renders markdown cleanly, with no editing by design"]
  - Platforms (V10): macOS [S2]; iOS [S2]; iPadOS [S2 "macOS, iOS, and iPadOS"]
  - Markdown forms claimed (V13): tables [S1 "tables"]; task lists [S1 "task lists"]; (b) not stated
  - Features the questions ask about: appearance V32: light and dark modes [S1 "Light mode, dark mode, or follow the system"]; follows the system appearance, stated [S1 "follow the system"] | files stay local V14: local, stated [S2 "No network access — files are read from disk and never leave your device"]
- **Charges.** Free [S1]; "Free · No ads · No in-app purchases" [S2]; (b) free [S1 "Free"]; (c) not stated
- **Buyer's all-in cost**, from the page text: price shape (V16b) free; beyond the price (V17): not stated; prerequisites (V11): minimum operating-system version named [S2 "Requires macOS 14 or later"]; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): macOS.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): Mac App Store: userRatingCount=1; averageUserRating=5
- **Whom its pages address (V05):** Plain readers of received markdown files [S1 "If you just want to READ markdown, this is the app."]
- **Last release and maintenance (V27):** August 4, 2026 (day; S2 "macOS 1.0 is live on the Mac App Store as of August 4, 2026."); (b) not stated

## R15. k1LoW/mo

Slug `k1low-mo`; profile `0-comparables/products/k1low-mo.md`. Registered because: coded as reading without editing (V09: reader, editing not stated). Cells: github-topics:markdown-viewer.

- **Publishes about itself.**
  - Kind (V08): terminal program [S1 "Live-reload on save (for files opened via CLI)"]
  - Reader or editor (V09): reader, editing not stated [S1 "mo is a Markdown viewer"]
  - Platforms (V10): not stated
  - Markdown forms claimed (V13): GitHub Flavored Markdown [S1 "GitHub-flavored Markdown"]; tables [S1 "tables"]; task lists [S1 "task lists"]; footnotes [S1 "footnotes"]; syntax-highlighted code blocks [S1 "Syntax highlighting [clipped]
  - Features the questions ask about: navigation V28: outline, contents or headings sidebar [S1 "Table of contents panel"] | find V29: search across files or a folder [S1 "Full-text search across file names and content"] | file changed elsewhere V31: reloads when the file changes on disk, stated [S1 "When you save a file, the browser automatically reflects the changes."] | appearance V32: light and dark modes [S1 "Dark / light theme"]; font or size choice [S1 "Content font size toggle (small / medium / large / extra large)"] | print and export V33: copy as rich text or HTML [S1 "Copy content (Markdown / Text / HTML)"]
- **Charges.** not stated; (b) not stated; (c) named open-source licence: MIT License [S1]; CC BY 4.0 for the logo only [S1 "Only logo license can be selected CC BY 4.0."]
- **Buyer's all-in cost**, from the page text: price shape (V16b) not stated; beyond the price (V17): not stated; prerequisites (V11): build toolchain named [S1 "Build: Requires Go and pnpm."] (for the build route); platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): none of the three named.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): github-topics:markdown-viewer: stars=1070; archived=false; last_push=2026-10-08
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** 28 Sep 12:18 (no year; S2 "released this 28 Sep 12:18 v1.6.9"); (b) not stated

## R16. learn-preview

Slug `learn-preview`; profile `0-comparables/products/learn-preview.md`. Registered because: coded as reading without editing (V09: reader, editing not stated). Cells: vscode.

- **Publishes about itself.**
  - Kind (V08): editor extension: [C] "In VS Code with Learn Preview installed"; [C] "This extension"
  - Reader or editor (V09): reader, editing not stated: [C] "The preview will open side-by-side."
  - Platforms (V10): inside a host program: [C] "In VS Code with Learn Preview installed"; [B] "Microsoft.VisualStudio.Code.Engine": "^1.86.0"
  - Markdown forms claimed (V13): CommonMark: [C] "all Markdown as supported by the CommonMark specification"; other named flavour: [C] "custom Markdown syntax for Learn"; (b) shown as plain text, stated: [C] "In some cases, custom [clipped]
  - Features the questions ask about: appearance V32: themes provided: [C] "light, dark and high contrast themes"; light and dark modes: [C] "light, dark and high contrast themes"
- **Charges.** [B] "Microsoft.VisualStudio.Services.Content.Pricing": "Free"; (b) free; (c) named open-source licence: [E] "MIT License"
- **Buyer's all-in cost**, from the page text: price shape (V16b) free; beyond the price (V17): not stated; prerequisites (V11): host program named: [B] "Microsoft.VisualStudio.Code.Engine": "^1.86.0"; runtime or interpreter named: [B] "ExtensionDependencies": [clipped]; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): none of the three named.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): vscode: installs=265340; ratings=3; average=3.33; lastUpdated=2026-08-13
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** "2026-08-13" (day; [B] "lastUpdated": "2026-08-13T01:49:13.887Z"); (b) not stated

## R17. MacMD Viewer

Slug `macmd-viewer`; profile `0-comparables/products/macmd-viewer.md`. Registered because: coded as reading without editing (V09: reader, stated read-only). Cells: alternativeto:Typora; alternativeto:Marked (AlternativeTo entry for Marked); homebrew:cask.

- **Publishes about itself.**
  - Kind (V08): desktop application: [B] "a native macOS app"; other kind: [B] "plus a QuickLook extension so you can preview files in Finder by pressing Space"
  - Reader or editor (V09): reader, stated read-only: [B] "not editing them."; [B] "Read-only by design: you keep your editor for writing, MacMD for reading."
  - Platforms (V10): macOS: [B] "macOS 14+, universal binary (Apple Silicon and Intel)."
  - Markdown forms claimed (V13): GitHub Flavored Markdown: [B] "it renders full GitHub-flavored Markdown"; diagrams: [B] "Mermaid diagrams"; tables: [B] "tables"; syntax-highlighted code blocks: [B] "syntax-highlighted code"; (b) [clipped]
  - Features the questions ask about: navigation V28: outline, contents or headings sidebar: [B] "A sidebar outline tracks your position as you scroll"; [D] "Table of contents sidebar" | file changed elsewhere V31: reloads when the file changes on disk, stated: [B] "live reload refreshes the preview the moment the file changes." | appearance V32: themes provided: [C] "12 document themes"; light and dark modes: [B] "Light and dark document themes" | print and export V33: export to PDF: [C] "Export to PDF" | files stay local V14: local, stated: [G] "Your Markdown files are read locally on your Mac and never leave your machine."
- **Charges.** [B] "$19.99 one-time — no subscription, no account required."; [D] "Single $19.99 one-time"; [D] "Family Pack $39.99 one-time, 3 keys"; [D] "Team & beyond $129 one-time, 10 keys"; [E] "No free trial."; (b) one-time purchase; (c) proprietary or [clipped]
- **Buyer's all-in cost**, from the page text: price shape (V16b) one-time purchase; beyond the price (V17): not stated; prerequisites (V11): minimum operating-system version named: [E] "macOS 14 (Sonoma) or later"; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): macOS; work use (V18): team, business or volume licence offered: [D] "Team & beyond $129 one-time, 10 keys"; [C] "Team Pack: $129 for 10 Macs".
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): alternativeto:Typora: rank=112; page=10; Like; alternatives-listed-for-this-entry=not shown; license=Paid Proprietary || alternativeto:Marked (AlternativeTo entry for Marked): rank=23; page=2; Like; alternatives-listed-for-this-entry=not shown; license=Paid Proprietary || homebrew:cask: 30d=96; 90d=319; 365d=627
- **Whom its pages address (V05):** Readers of what AI agents write: [B] "people who already write in VS Code, Cursor or Obsidian and just want a fast, clean way to read the Markdown their AI agents (Claude Code, Cursor, Copilot) keep [clipped]
- **Last release and maintenance (V27):** "October 3, 2026" (day; [F] "October 3, 2026 v1.6.4"); (b) actively maintained, stated: [B] "actively maintained"

## R18. mandown

Slug `mandown`; profile `0-comparables/products/mandown.md`. Registered because: coded as reading without editing (V09: reader, editing not stated). Cells: homebrew:formula.

- **Publishes about itself.**
  - Kind (V08): terminal program: [B] topics "cli command-line console ... terminal tui"; [C] "$ mdn sample.md"; component: [C] "Static and shared libraries are [clipped]
  - Reader or editor (V09): reader, editing not stated: [C] "A man-page inspired Markdown pager written in C."
  - Platforms (V10): macOS; Linux: [A] bottle support "macOS on Apple Silicon", "macOS on Intel sonoma", "Linux ARM64", "Linux x86_64"
  - Markdown forms claimed (V13): markdown named, no form named: [C] "it should work on most Markdown documents."; (b) not stated
  - Features the questions ask about: V28 to V33 and V14 all not stated
- **Charges.** not stated; (b) not stated; (c) named open-source licence: [A] "License: GPL-3.0-or-later"; [B] "GPL-3.0 license"
- **Buyer's all-in cost**, from the page text: price shape (V16b) not stated; beyond the price (V17): not stated; prerequisites (V11): runtime or interpreter named: [C] "Mandown requires libncurses(w), libxml2 and libconfig as compile-time dependencies."; build toolchain named: [A] [clipped]; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): Linux, macOS.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): homebrew:formula: 30d=4; 90d=18; 365d=202
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** "01 Apr 18:37" (v1.0.5.2 release, day; [D] "released this 01 Apr 18:37", page datetime 2025-04-01); (b) not stated

## R19. marge

Slug `marge`; profile `0-comparables/products/marge.md`. Registered because: coded as reading without editing (V09: reader, editing not stated). Cells: Snap Store.

- **Publishes about itself.**
  - Kind (V08): terminal program: [C] "Usage: marge [OPTIONS]... INPUT_FILE [OUTPUT_FILE]"; "command line arguments are subject to change"
  - Reader or editor (V09): reader, editing not stated: [C] "Converts a markdown INPUT_FILE to html and serves it with a web server."
  - Platforms (V10): macOS: [C] section heading "MacOS"; Linux: [A] "Ubuntu 16.04 or later?"
  - Markdown forms claimed (V13): markdown named, no form named: [C] "Converts a markdown file to html"; (b) not stated
  - Features the questions ask about: file changed elsewhere V31: reloads when the file changes on disk, stated: [C] "Watches the markdown file for changes and refreshes the html file" | print and export V33: export to HTML: [C] "Writes a standalone OUTPUT_FILE if requested."
- **Charges.** not stated; (b) not stated; (c) named open-source licence: [A] "License MIT"; [B] "MIT License"
- **Buyer's all-in cost**, from the page text: price shape (V16b) not stated; beyond the price (V17): not stated; prerequisites (V11): runtime or interpreter named: [C] "Install dependencies: sudo apt install inotify-tools pandoc busybox"; package manager named as required to [clipped]; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): Linux, macOS.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): Snap Store: none given by API (find returns no install, rating or download counts)
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** "4 December 2018" (day; [A] "Last updated 4 December 2018 - latest/stable"); (b) undecidable (see notes)

## R20. Markdown Hot Reload

Slug `markdown-hot-reload`; profile `0-comparables/products/markdown-hot-reload.md`. Registered because: coded as reading without editing (V09: reader, stated read-only). Cells: Snap Store.

- **Publishes about itself.**
  - Kind (V08): desktop application :: "Platform Linux only" [2]
  - Reader or editor (V09): reader, stated read-only :: "There is no editing surface, and mhr never writes to the file it opens." [1]
  - Platforms (V10): Linux :: "Linux is the only platform mhr is released on and used on." [3]
  - Markdown forms claimed (V13): GitHub Flavored Markdown :: "It renders GitHub Flavored Markdown" [1] || tables :: "tables" [1] || task lists :: "task lists" [1] || footnotes :: "footnotes" [1] || syntax-highlighted code blocks :: [clipped]
  - Features the questions ask about: navigation V28: scroll position kept or synchronised :: "Your scroll position stays where it was." [1] | links and images V30: opens web links in the browser :: "Clicking a link opens it in your default browser or mail client" [3] | file changed elsewhere V31: reloads when the file changes on disk, stated :: "re-renders it every time the file changes on disk" [1] | appearance V32: light and dark modes :: "the t key pins the theme to light or to dark" [3] || follows the system appearance, stated :: "The window follows [clipped]
- **Charges.** not stated || (b) not stated || (c) named open-source licence :: "License - MIT" [1] ; "MIT license" [3]
- **Buyer's all-in cost**, from the page text: price shape (V16b) not stated; beyond the price (V17): not stated; prerequisites (V11): runtime or interpreter named :: "WebKitGTK ... You install it yourself" (tarball and source routes) [2] || build toolchain named :: "it needs Rust [clipped]; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): Linux.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): Snap Store: none given by API (find returns no install, rating or download counts)
- **Whom its pages address (V05):** Plain readers of received markdown files :: "built for reading files you did not write, such as ... a README from a repository you just cloned" [1] || Readers of what AI agents write :: "a plan [clipped]
- **Last release and maintenance (V27):** 2026-09-16 (day), "Last updated - 16 September 2026" [1] || (b) not stated

## R21. Markdown Lens

Slug `markdown-lens`; profile `0-comparables/products/markdown-lens.md`. Registered because: coded as reading without editing (V09: reader, editing not stated). Cells: Mac App Store.

- **Publishes about itself.**
  - Kind (V08): desktop application :: "native Markdown viewer for macOS" [1]
  - Reader or editor (V09): reader, editing not stated :: "Preview your Markdown Files Beautifully." [2]
  - Platforms (V10): macOS :: "Requires macOS 12.4 or later." [1]
  - Markdown forms claimed (V13): GitHub Flavored Markdown :: "GitHub Flavored Markdown" [1] || tables :: "tables" [1] || task lists :: "task lists" [1] || math :: "Math equations with KaTeX" [1] || diagrams :: "Diagrams with [clipped]
  - Features the questions ask about: links and images V30: follows links to other markdown files inside the product :: "Click links to other Markdown files to open them in new windows" [1] | file changed elsewhere V31: reloads when the file changes on disk, stated :: "Live reload automatically refreshes when you edit in any external editor" [1] | appearance V32: light and dark modes :: "Light and dark mode support" [1] || follows the system appearance, stated :: "follows your system appearance" [1] | print and export V33: print :: "Print directly with accurate formatting" [1] || export to PDF :: "Export to PDF" [1] || export to HTML :: "Export to [clipped] | files stay local V14: local, stated :: "Your documents stay on your device" [1] ; "your files never leave your Mac" [2]
- **Charges.** "free to use with all features included" [1] ; "price": 0, "priceCurrency": "USD" ; "Support Development = $1.99" [1] ; "Actually Free" [2] || (b) free :: "free to use with all features included" [1] || donation or sponsorship invited, use free :: [clipped]
- **Buyer's all-in cost**, from the page text: price shape (V16b) free, donation or sponsorship invited, use free, one-time purchase; beyond the price (V17): not stated; prerequisites (V11): minimum operating-system version named :: "Requires macOS 12.4 or later." [1]; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): macOS.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): Mac App Store: userRatingCount=0; averageUserRating=0
- **Whom its pages address (V05):** Developers and coders :: "Perfect for developers" [1] || Writers and authors :: "writers" [1] || Students and academics :: "students" [1]
- **Last release and maintenance (V27):** 2026-09-17 (day), "Version 2.21 | Thu Sep 17 2026" [1] || (b) actively maintained, stated :: "Private & Actively Maintained" [2]

## R22. Markdown Peek

Slug `markdown-peek`; profile `0-comparables/products/markdown-peek.md`. Registered because: coded as reading without editing (V09: reader, stated read-only). Cells: Mac App Store.

- **Publishes about itself.**
  - Kind (V08): desktop application :: "Markdown viewer for macOS" [1]
  - Reader or editor (V09): reader, stated read-only :: "It is built for reading, not editing." ; "Markdown Peek does not edit or create files." [3]
  - Platforms (V10): macOS :: "Requires macOS 15.5 or later." [1]
  - Markdown forms claimed (V13): tables :: "tables" [3] || task lists :: "task lists" [3] || math :: "Inline math ... render as real formulas" [3] || diagrams :: "A mermaid code block becomes a flowchart" [3] || (b) not stated
  - Features the questions ask about: navigation V28: outline, contents or headings sidebar :: "the heading outline" [3] | find V29: search within document :: "Find with Command-F Every match lights up with a count of how many there are" [3] | links and images V30: shows remote images :: "Images from the web stay off until you choose to show them." [3] | file changed elsewhere V31: reloads when the file changes on disk, stated :: "open files reload on their own when they change on disk" [1] | appearance V32: light and dark modes :: "sharp in light mode and in a dark mode tuned for reading code" [2] | print and export V33: print :: "Print or save as PDF with ⌘P" [1]
- **Charges.** "Free to use." ; "Free on the Mac App Store" ; "price": 0, "priceCurrency": "USD" [1][2] || (b) free :: "Free to use." [1] || (c) not stated
- **Buyer's all-in cost**, from the page text: price shape (V16b) free; beyond the price (V17): no other cost, stated :: "No accounts, no setup, no cost." [3]; prerequisites (V11): minimum operating-system version named :: "Markdown Peek runs on macOS 15.5 and later." [2]; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): macOS.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): Mac App Store: userRatingCount=0; averageUserRating=0
- **Whom its pages address (V05):** Developers and coders :: "developers" [1][2] || Writers and authors :: "writers" [1][2] || Students and academics :: "students" [1][2] || Teams, businesses and organisations :: "Easy for IT, too" [1] [clipped]
- **Last release and maintenance (V27):** 2026-09-25 (day), version field "Version 1.8 | Fri Sep 25 2026" [1] || (b) not stated

## R23. Markdown Preview - Quick Look

Slug `markdown-preview-quick-look`; profile `0-comparables/products/markdown-preview-quick-look.md`. Registered because: coded as reading without editing (V09: reader, editing not stated). Cells: Mac App Store.

- **Publishes about itself.**
  - Kind (V08): other kind :: "Quick Look extension to preview Markdown files in Finder" [1] || desktop application :: "Mac / Requires macOS 12.0 or later." [1]
  - Reader or editor (V09): reader, editing not stated :: "You can also switch between preview and the original Markdown content." [1]
  - Platforms (V10): macOS :: "Requires macOS 12.0 or later." [1]
  - Markdown forms claimed (V13): math :: "Markdown with KaTex." [1] || diagrams :: "Markdown with Mermaid diagram." [1] || GitHub Flavored Markdown :: "GitHub Flavored Markdown Spec" [3] || other named flavour :: "MDX files (JSX [clipped]
  - Features the questions ask about: appearance V32: themes provided :: "Choose between a clean, modern look or a classic typeset style" [3]
- **Charges.** "a one-time purchase of $1.99 USD" ; "Actual price varies based on your region." [3] ; "price": 1.99, "priceCurrency": "USD" [1] || (b) one-time purchase :: "one-time purchase of $1.99 USD" [3] || (c) not stated
- **Buyer's all-in cost**, from the page text: price shape (V16b) one-time purchase; beyond the price (V17): not stated; prerequisites (V11): host program named :: "you will need to enable Quick Look extension in System Settings" [1] || minimum operating-system version named :: "Requires [clipped]; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): macOS.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): Mac App Store: userRatingCount=0; averageUserRating=0
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** 2026-10-08 (day), version field "Version 2.6 | Thu Oct 08 2026" [1] || (b) not stated

## R24. Markdown Preview Enhanced

Slug `markdown-preview-enhanced`; profile `0-comparables/products/markdown-preview-enhanced.md`. Registered because: coded as reading without editing (V09: reader, editing not stated); and top five in vscode by installs (2 of 19 eligible comparables with a figure; 10,429,484). Cells: vscode.

- **Publishes about itself.**
  - Kind (V08): editor extension :: "Extension for Visual Studio Code" [1]
  - Reader or editor (V09): reader, editing not stated :: "Markdown Preview Enhanced ported to vscode" [1]
  - Platforms (V10): inside a host program :: "Extension for Visual Studio Code" ; "VS Code · VS Code for the Web" [1]
  - Markdown forms claimed (V13): math :: "math typesetting" ; "Math (KaTeX/MathJax)" [1] || diagrams :: "mermaid, PlantUML, WebSequenceDiagrams" [1] || other named flavour :: "pandoc" [1] || wiki-links :: "wikilinks" [1] || (b) not [clipped]
  - Features the questions ask about: navigation V28: outline, contents or headings sidebar :: "esc Toggle sidebar TOC" [1] || scroll position kept or synchronised :: "automatic scroll sync" [1] | files stay local V14: local by default, optional upload stated :: "Markdown content — rendered locally; never leaves your machine." ; "Image upload (imgur, [clipped]
- **Charges.** "Free" in "10,429,939 installs | (145) | Free" [1] || (b) free :: "Free" [1] || donation or sponsorship invited, use free :: "supporting us on GitHub Sponsors, PayPal, or 微信支付 Wechat Pay" [1] || (c) named open-source licence :: "University of [clipped]
- **Buyer's all-in cost**, from the page text: price shape (V16b) free, donation or sponsorship invited, use free; beyond the price (V17): not stated; prerequisites (V11): host program named :: "Extension for Visual Studio Code" [1]; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): none of the three named.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): vscode: installs=10429484; ratings=145; average=4.33; lastUpdated=2026-10-09
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** 2026-10-09 (day), "LastUpdatedDateString: Fri, 09 Oct 2026" in listing data embedded in page [1] || (b) not stated

## R25. Markdown Reader - Ream

Slug `markdown-reader-ream`; profile `0-comparables/products/markdown-reader-ream.md`. Registered because: coded as reading without editing (V09: reader, stated read-only). Cells: Mac App Store.

- **Publishes about itself.**
  - Kind (V08): mobile application (\"Requires iOS 26.2 or later.\" P1); desktop application (\"Now available on Mac.\" P1)
  - Reader or editor (V09): reader, stated read-only (\"Markdown Reader is a view-only app\" P1; \"There's no editor.\" P1)
  - Platforms (V10): iOS; iPadOS; macOS (\"Requires iOS 26.2 or later.\" \"Requires iPadOS 26.2 or later.\" \"Requires macOS 26.2 or later.\" P1)
  - Markdown forms claimed (V13): syntax-highlighted code blocks (\"Syntax highlighting for 15 languages\" P1); tables (\"Optimized table rendering.\" P1); (b) not stated
  - Features the questions ask about: navigation V28: outline, contents or headings sidebar; jump to heading or section (\"Auto-generated table of contents with one-tap navigation\" P1) | appearance V32: themes provided (\"Multiple beautiful themes\"); light and dark modes (\"Dark mode support\"); font or size choice (\"Customizable fonts\"; [clipped] | files stay local V14: local, stated (\"your markdown files and content remain private and are not uploaded to any of our servers\" P3)
- **Charges.** \"3.99 USD\" (structured data \"price\": 3.99, \"priceCurrency\": \"USD\", P1; \"$3.99\" button P1); (b) undecidable; (c) not stated
- **Buyer's all-in cost**, from the page text: price shape (V16b) undecidable; beyond the price (V17): not stated; prerequisites (V11): minimum operating-system version named (\"Requires iOS 26.2 or later.\" P1); platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): macOS.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): Mac App Store: userRatingCount=1; averageUserRating=5
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** 2026-06-02 (day; version 1.4 date field, P1); (b) not stated

## R26. Markdown Sticky

Slug `markdown-sticky`; profile `0-comparables/products/markdown-sticky.md`. Registered because: coded as reading without editing (V09: reader, editing not stated). Cells: Mac App Store.

- **Publishes about itself.**
  - Kind (V08): desktop application (\"Requires macOS 15.5 or later.\" P1); mobile application (\"Requires iPadOS 18.5 or later.\" P1)
  - Reader or editor (V09): reader, editing not stated (\"Real-time Markdown preview\" P1)
  - Platforms (V10): iPadOS (\"Requires iPadOS 18.5 or later.\" P1); macOS (\"Requires macOS 15.5 or later.\" P1); iOS (\"iOS/iPadOS: inside the app's sandbox\" P3)
  - Markdown forms claimed (V13): markdown named, no form named (\"Real-time Markdown preview\" P1); (b) not stated
  - Features the questions ask about: files stay local V14: local, stated (\"The sticky-note data this app creates and edits is stored only inside the customer's device (local storage) and is not [clipped]
- **Charges.** \"0 USD\" (structured data \"price\": 0, \"priceCurrency\": \"USD\" P1); \"$1.99\" (in-app purchase \"Unlimited Windows\" P1); (b) free with paid tier or features (\"'hasInAppPurchases': True, 'isFree': True\" P1; \"This app offers in-app purchases [clipped]
- **Buyer's all-in cost**, from the page text: price shape (V16b) free with paid tier or features, \"This app offers in-app purchases for feature expansion.\" P3, English rendering); beyond the price (V17): not stated; prerequisites (V11): minimum operating-system version named (\"Requires macOS 15.5 or later.\" P1); platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): macOS.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): Mac App Store: userRatingCount=0; averageUserRating=0
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** not stated; (b) not stated

## R27. Markdown View

Slug `markdown-view`; profile `0-comparables/products/markdown-view.md`. Registered because: coded as reading without editing (V09: reader, editing not stated). Cells: Snap Store.

- **Publishes about itself.**
  - Kind (V08): terminal program (\"Command line tool to view a markdown file in your default web browser.\" P1)
  - Reader or editor (V09): reader, editing not stated (\"Command line tool to view a markdown file in your default web browser.\" P1)
  - Platforms (V10): Linux; macOS; Windows; BSD (\"Linux, macOS, Windows, and FreeBSD binaries are all published with every release.\" P4)
  - Markdown forms claimed (V13): GitHub Flavored Markdown; diagrams; tables; task lists (\"Supports GitHub Flavored Markdown, Mermaid diagrams, embedded images, and automatic theme detection.\"; \"Full support for tables, task [clipped]
  - Features the questions ask about: links and images V30: shows local images (\"Relative image paths are then resolved against the current working directory.\" P4) | appearance V32: light and dark modes; follows the system appearance, stated (\"Supports dark and light mode automatically\" P1; \"HTML output conforms to [clipped] | print and export V33: export to HTML (\"converts markdown files to styled HTML\"; \"Write to a temporary file or specify a custom output location\" P4)
- **Charges.** not stated; (b) not stated; (c) named open-source licence (\"License MIT\" P1; \"MIT license\" P3)
- **Buyer's all-in cost**, from the page text: price shape (V16b) not stated; beyond the price (V17): not stated; prerequisites (V11): not stated; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): Linux, macOS, Windows.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): Snap Store: none given by API (find returns no install, rating or download counts)
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** 23 August 2026 (day; snapcraft.io 'latest/edge' line, P1); latest/stable 1.8.0; GitHub release 1.9.0 'released this 21 Aug' (no year, P5); (b) not stated

## R28. Markdown Viewer

Slug `markdown-viewer`; profile `0-comparables/products/markdown-viewer.md`. Registered because: coded as reading without editing (V09: reader, editing not stated). Cells: Snap Store.

- **Publishes about itself.**
  - Kind (V08): desktop application (\"Desktop Markdown viewer for Linux, Windows, and macOS\" P1)
  - Reader or editor (V09): reader, editing not stated (\"Desktop Markdown viewer for Linux, Windows, and macOS\" P1)
  - Platforms (V10): Linux; Windows; macOS (\"Desktop Markdown viewer for Linux, Windows, and macOS\" P1)
  - Markdown forms claimed (V13): not stated; (b) not stated
  - Features the questions ask about: V28 to V33 and V14 all not stated
- **Charges.** not stated; (b) not stated; (c) not stated
- **Buyer's all-in cost**, from the page text: price shape (V16b) not stated; beyond the price (V17): not stated; prerequisites (V11): not stated; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): Linux, macOS, Windows.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): Snap Store: none given by API (find returns no install, rating or download counts)
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** 3 October 2026 (day; 'Last updated 3 October 2026 - latest/stable', version 1.1.0, P1); (b) not stated

## R29. Markdown Viewer - MD QuickView

Slug `markdown-viewer-md-quickview`; profile `0-comparables/products/markdown-viewer-md-quickview.md`. Registered because: coded as reading without editing (V09: reader, editing not stated). Cells: Mac App Store.

- **Publishes about itself.**
  - Kind (V08): other kind (\"A Mac Quick Look extension for previewing Markdown files in a GitHub-style layout.\" P2); desktop application (\"MD QuickView is a [clipped]
  - Reader or editor (V09): reader, editing not stated (\"MD QuickView is a Markdown viewer for Mac that lets you preview .md files with Quick Look.\" P1)
  - Platforms (V10): macOS (\"Requires macOS 14.0 or later.\" P1; \"macOS 12.0+\" P2)
  - Markdown forms claimed (V13): tables; task lists (\"readable rendering for tables, checklists, code blocks, and GitHub-style documents\" P2); (b) not stated
  - Features the questions ask about: file changed elsewhere V31: reloads when the file changes on disk, stated (\"the Quick Look preview now updates when an MD file is changed\" P1) | appearance V32: light and dark modes (\"When using your Mac in Dark Mode, the preview automatically switches to an eye-friendly dark theme.\" P2); follows [clipped] | files stay local V14: local, stated (\"Previews on Mac. It is not designed around sending documents to an AuraMark server.\" P2; \"This App does not collect or [clipped]
- **Charges.** \"Free\"; \"0 USD\" (\"price\": 0 P1); \"Pricing Free\" (P2); \"Yes, MD QuickView is free.\" (P2); (b) free (\"Is MD QuickView free? Yes, MD QuickView is free. It is available as a free download from the Mac App Store.\" P2); (c) not stated
- **Buyer's all-in cost**, from the page text: price shape (V16b) free; beyond the price (V17): not stated; prerequisites (V11): minimum operating-system version named (\"Requires macOS 14.0 or later.\" P1; \"Supported platform macOS 12.0 or later\" P2); platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): macOS.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): Mac App Store: userRatingCount=0; averageUserRating=0
- **Whom its pages address (V05):** Developers and coders (\"It is built for developers, writers, students, and anyone who often checks Markdown files on macOS.\" P1; \"Developers and engineers\" P2); Writers and authors (\"writers\" [clipped]
- **Last release and maintenance (V27):** 2026-09-17 (day; version 1.5.0 date field, P1); (b) not stated

## R30. Markdown Viewer - MD Reader

Slug `markdown-viewer-md-reader`; profile `0-comparables/products/markdown-viewer-md-reader.md`. Registered because: coded as reading without editing (V09: reader, stated read-only). Cells: Mac App Store.

- **Publishes about itself.**
  - Kind (V08): mobile application; desktop application (\"Requires iOS 17.0 or later.\" \"Requires macOS 14.0 or later.\" P1; \"A clean and simple free Markdown [clipped]
  - Reader or editor (V09): reader, stated read-only (\"This is a viewer, not an editor.\" P1)
  - Platforms (V10): iOS; iPadOS; macOS (\"Requires iOS 17.0 or later.\" \"Requires iPadOS 17.0 or later.\" \"Requires macOS 14.0 or later.\" P1)
  - Markdown forms claimed (V13): GitHub Flavored Markdown; tables; task lists (\"Renders GitHub Flavored Markdown — headings, tables, code blocks, task lists, blockquotes, links, and web images\" P1); (b) not stated
  - Features the questions ask about: navigation V28: outline, contents or headings sidebar (\"Table of contents — auto-generated from your headings ... (side panel on iPad, sheet on iPhone)\" [clipped] | find V29: search within the document (\"Search now highlights matches in the formatted view\" P1) | links and images V30: shows remote images (\"links, and web images\" P1) | file changed elsewhere V31: manual refresh, stated (\"Refresh — reload after editing in another app\" P1) | print and export V33: export to PDF (\"Export to PDF — share your document as a formatted, print-ready PDF\" P1)
- **Charges.** \"0 USD\" (\"price\": 0, \"priceCurrency\": \"USD\" P1); \"free Markdown viewer\" (P2); (b) free (\"A clean and simple free Markdown viewer for macOS.\" P2); (c) not stated
- **Buyer's all-in cost**, from the page text: price shape (V16b) free; beyond the price (V17): not stated; prerequisites (V11): minimum operating-system version named (\"Requires macOS 14.0 or later.\" P1); platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): macOS.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): Mac App Store: userRatingCount=0; averageUserRating=0
- **Whom its pages address (V05):** Developers and coders; Writers and authors (\"Built for developers, technical writers, and anyone who regularly opens README files or documentation\" P1)
- **Last release and maintenance (V27):** 2026-07-31 (day; version 1.0 date field, P1; version 1.1 undated); (b) not stated

## R31. Markdown Viewer Offline

Slug `markdown-viewer-offline`; profile `0-comparables/products/markdown-viewer-offline.md`. Registered because: coded as reading without editing (V09: reader, editing not stated). Cells: Mac App Store.

- **Publishes about itself.**
  - Kind (V08): desktop application (\"Markdown Viewer, a dedicated desktop application\" P1)
  - Reader or editor (V09): reader, editing not stated (\"Markdown Viewer is more than just a file reader\" P1)
  - Platforms (V10): macOS (\"Requires macOS 11.0 or later.\" P1)
  - Markdown forms claimed (V13): undecidable; (b) not stated
  - Features the questions ask about: V28 to V33 and V14 all not stated
- **Charges.** \"0 USD\" (\"price\": 0, \"priceCurrency\": \"USD\" P1); (b) free (\"'isFree': True\" P1); (c) not stated
- **Buyer's all-in cost**, from the page text: price shape (V16b) free; beyond the price (V17): not stated; prerequisites (V11): minimum operating-system version named (\"Requires macOS 11.0 or later.\" P1); platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): macOS.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): Mac App Store: userRatingCount=0; averageUserRating=0
- **Whom its pages address (V05):** Developers and coders (\"Software Developers: Perfect for previewing README files\"); Writers and authors; Bloggers and platform publishers (\"Writers and Bloggers\"); Students and academics [clipped]
- **Last release and maintenance (V27):** not stated; (b) not stated

## R32. markdown-viewer-premium

Slug `markdown-viewer-premium`; profile `0-comparables/products/markdown-viewer-premium.md`. Registered because: coded as reading without editing (V09: reader, editing not stated). Cells: Snap Store.

- **Publishes about itself.**
  - Kind (V08): desktop application (\"Install markdown-viewer-premium on your Linux distribution\" P1)
  - Reader or editor (V09): reader, editing not stated (\"A powerful and fast Markdown viewer with premium features.\" P1)
  - Platforms (V10): Linux (\"Install markdown-viewer-premium on your Linux distribution\" P1)
  - Markdown forms claimed (V13): not stated; (b) not stated
  - Features the questions ask about: V28 to V33 and V14 all not stated
- **Charges.** not stated; (b) not stated; (c) not stated
- **Buyer's all-in cost**, from the page text: price shape (V16b) not stated; beyond the price (V17): not stated; prerequisites (V11): not stated; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): Linux.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): Snap Store: none given by API (find returns no install, rating or download counts)
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** 27 March 2026 (day; 'Last updated 27 March 2026 - latest/stable', version 1.0.2, P1); (b) not stated

## R33. markdownpart

Slug `markdownpart`; profile `0-comparables/products/markdownpart.md`. Registered because: coded as reading without editing (V09: reader, editing not stated). Cells: debian:apt-cache search markdown.

- **Publishes about itself.**
  - Kind (V08): other kind (\"a small KDE KParts plugin to render Markdown documents in any application which uses the KPart system\" P1)
  - Reader or editor (V09): reader, editing not stated (\"a small KDE KParts plugin to render Markdown documents\" P1)
  - Platforms (V10): Linux (\"Origin: Ubuntu\"; \"500 archive.ubuntu.com plucky/universe amd64 Packages\" P1)
  - Markdown forms claimed (V13): markdown named, no form named (\"to render Markdown documents\" P1); (b) not stated
  - Features the questions ask about: V28 to V33 and V14 all not stated
- **Charges.** not stated; (b) not stated; (c) not stated
- **Buyer's all-in cost**, from the page text: price shape (V16b) not stated; beyond the price (V17): not stated; prerequisites (V11): runtime or interpreter named (\"Depends: kio6, libc6 (>= 2.14), libkf6configgui6 (>= 6.3.0), ... libqt6core6t64 (>= 6.8.2), ... libstdc++6 (>= 5)\" [clipped]; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): Linux.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): debian:apt-cache search markdown: not published by the list (no install count in apt-cache)
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** not stated; (b) not stated

## R34. markdowser

Slug `markdowser`; profile `0-comparables/products/markdowser.md`. Registered because: coded as reading without editing (V09: reader, editing not stated). Cells: Snap Store.

- **Publishes about itself.**
  - Kind (V08): desktop application (\"GitHub (Windows)\"; \"Snapcraft (Linux)\" P3)
  - Reader or editor (V09): reader, editing not stated (\"Markdowser is a web browser that renders Markdown instead of HTML.\" P3)
  - Platforms (V10): Windows; Linux (\"GitHub (Windows)\"; \"Chocolatey (Windows): `choco install Markdowser`\"; \"Snapcraft (Linux)\" P3)
  - Markdown forms claimed (V13): markdown named, no form named (\"Markdowser is a web browser that renders Markdown instead of HTML.\" P3); (b) not stated
  - Features the questions ask about: V28 to V33 and V14 all not stated
- **Charges.** not stated; (b) not stated; (c) named open-source licence (\"License MIT\" P1; \"MIT license\" P2)
- **Buyer's all-in cost**, from the page text: price shape (V16b) not stated; beyond the price (V17): not stated; prerequisites (V11): not stated; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): Linux, Windows.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): Snap Store: none given by API (find returns no install, rating or download counts)
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** 23 June 2024 (day; 'Last updated 23 June 2024 - latest/stable 23 June 2024 - latest/edge', version 0.2.0.0, P1); (b) undecidable

## R35. Marked

Slug `marked`; profile `0-comparables/products/marked.md`. Registered because: coded as reading without editing (V09: reader, stated read-only). Cells: alternativeto:Typora; alternativeto:Glow; homebrew:cask; Mac App Store.

- **Publishes about itself.**
  - Kind (V08): desktop application (\"Requires macOS 10.13 or later.\" P1)
  - Reader or editor (V09): reader, stated read-only (\"Marked 2 is a previewer (*not an editor*)\" P1)
  - Platforms (V10): macOS (\"Requires macOS 10.13 or later.\" P1)
  - Markdown forms claimed (V13): GitHub Flavored Markdown (\"Marked's built in GitHub Flavored Markdown processor\" P1); other named flavour (\"MultiMarkdown\"; \"the option to render using Discount\" P6); (b) not stated
  - Features the questions ask about: navigation V28: outline, contents or headings sidebar (\"automatically generates a table of contents using headlines in your document for easy navigation\" [clipped] | find V29: search within the document (\"Use typeahead search to rapidly jump to any section.\" P6) | file changed elsewhere V31: reloads when the file changes on disk, stated (\"It updates live every time you save your document in your favorite text editor\" P1) | appearance V32: themes provided (\"9 preview styles built in (including GitHub)\" P1); custom stylesheet (\"you can add unlimited custom styles of your [clipped] | print and export V33: export to PDF; export to HTML; export to another named format (\"documents (including HTML, PDF and Word)\" P6) | files stay local V14: local, stated (\"The application processes your Markdown files locally on your device. We do not collect, store, or transmit your document [clipped]
- **Charges.** \"13.99 USD\" (structured data P1); \"$14.99\" (\"remains available … for a one-time purchase of $14.99.\" P9); \"$1.99\" (in-app purchase \"Spelling and Grammar check\" P1); \"seven days\" trial (P6); (b) one-time purchase (\"one-time purchase of [clipped]
- **Buyer's all-in cost**, from the page text: price shape (V16b) one-time purchase, free trial, then paid; beyond the price (V17): not stated; prerequisites (V11): minimum operating-system version named (\"Requires macOS 10.13 or later.\" P1; \"Marked 2 requires macOS 10.12 or later\" P6; \"Requirements: macOS [clipped]; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): macOS.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): alternativeto:Typora: rank=41; page=4; 20 likes; alternatives-listed-for-this-entry=not shown; license=Paid Proprietary Origin United States Platforms Mac Google Chrome Safari Setapp Mozilla [clipped] || alternativeto:Glow: rank=9; page=1; 20 likes; alternatives-listed-for-this-entry=not shown; license=Paid Proprietary Origin United States Platforms Mac Google Chrome Safari Setapp Mozilla [clipped] || homebrew:cask: 30d=45; 90d=218; 365d=1,191 || Mac App Store: userRatingCount=0; averageUserRating=0
- **Whom its pages address (V05):** Writers and authors (\"MultiMarkdown processing is provided for writers\" P1; \"Smart tools for smart writers\"; \"Tools for authors\" P6)
- **Last release and maintenance (V27):** 2025-03-11 (day; version 2.6.46 date field, P1; Marked 3.2.18 undated); (b) not stated

## R36. Marked QL - Markdown Preview

Slug `marked-ql-markdown-preview`; profile `0-comparables/products/marked-ql-markdown-preview.md`. Registered because: coded as reading without editing (V09: reader, editing not stated). Cells: Mac App Store.

- **Publishes about itself.**
  - Kind (V08): other kind (\"Marked QL works on its own as a Quick Look extension for Markdown files.\" P2); desktop application (\"Requires macOS 13.0 or later.\" [clipped]
  - Reader or editor (V09): reader, editing not stated (\"Preview any Markdown file on your Mac with a press of the space bar.\" P1)
  - Platforms (V10): macOS (\"Requires macOS 13.0 or later.\" P1, P2)
  - Markdown forms claimed (V13): CommonMark; GitHub Flavored Markdown; other named flavour (\"Marked QL uses Apex, a unified Markdown processor that combines CommonMark, GitHub Flavored Markdown, MultiMarkdown, Kramdown, and [clipped]
  - Features the questions ask about: navigation V28: jump to heading or section (\"Jump between headings in longer documents without leaving the Quick Look preview.\" P2) | links and images V30: shows remote images (\"Embed remote http(s) images in Quick Look so CDN and wiki photos show in Spacebar previews\" P1); shows local images [clipped] | appearance V32: themes provided (\"Choose preview styles\" P2); custom stylesheet (\"optional custom CSS\" P2); follows the system appearance, stated [clipped]
- **Charges.** \"9.99 USD\" (structured data P1); \"$9.99 one-time\" (\"Paddle Direct download — $9.99 one-time, free trial available\" P2); (b) one-time purchase (\"$9.99 one-time purchase\" P2); free trial, then paid (\"free trial available\" P2); (c) not stated
- **Buyer's all-in cost**, from the page text: price shape (V16b) one-time purchase, free trial, then paid; beyond the price (V17): not stated; prerequisites (V11): minimum operating-system version named (\"Requires macOS 13.0 or later\" P2); platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): macOS.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): Mac App Store: userRatingCount=0; averageUserRating=0
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** 2026-10-07 (day; version 1.0.24 date field, P1); (b) not stated

## R37. MarkFlow:Read Markdown files

Slug `markflow-read-markdown-files`; profile `0-comparables/products/markflow-read-markdown-files.md`. Registered because: coded as reading without editing (V09: reader, editing not stated). Cells: Mac App Store.

- **Publishes about itself.**
  - Kind (V08): mobile application; desktop application (\"Requires iOS 13.0 or later.\" \"Requires macOS 10.15 or later.\" P1)
  - Reader or editor (V09): reader, editing not stated (\"MarkReader is a clean, fast Markdown reader\" P1)
  - Platforms (V10): iOS; iPadOS; macOS (\"Requires iOS 13.0 or later.\" \"Requires iPadOS 13.0 or later.\" \"Requires macOS 10.15 or later.\" P1)
  - Markdown forms claimed (V13): GitHub Flavored Markdown; tables; task lists (\"Full GitHub Flavored Markdown (GFM) — headings, bold, italic, strikethrough, blockquotes, tables, task lists, and more\" P1); footnotes (\"Footnotes [clipped]
  - Features the questions ask about: navigation V28: outline, contents or headings sidebar (\"Table of contents (TOC) / outline generated from headings\" P1); scroll position kept or [clipped] | find V29: search within the document (\"Search within the current document and jump between matches\" P1) | links and images V30: opens web links in the browser (\"Tap links in documents to open them directly in your browser.\" P1) | appearance V32: themes provided (\"6 beautiful new reading themes added, now 18 themes available\" P1); light and dark modes (\"Dark mode\" P1); font or [clipped] | files stay local V14: local, stated (\"All files are stored locally on your device in the app's secure storage. They are not uploaded to any cloud service or [clipped]
- **Charges.** \"0 USD\" (P1); \"$12.99\" (in-app purchase \"Lifetime Access\"); \"$19.99\" (\"Yearly Premium\"); \"$2.99\" (\"Monthly Premium\") (all P1); (b) free with paid tier or features (\"'hasInAppPurchases': True, 'isFree': True\" P1); subscription [clipped]
- **Buyer's all-in cost**, from the page text: price shape (V16b) free with paid tier or features, subscription, \"Added yearly subscription option\" P1); beyond the price (V17): not stated; prerequisites (V11): minimum operating-system version named (\"Requires iOS 13.0 or later.\" P1); platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): macOS.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): Mac App Store: userRatingCount=4; averageUserRating=4.5
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** 2026-04-27 (day; version 1.4.0 date field, P1); (b) not stated

## R38. Marklens: Markdown Reader

Slug `marklens-markdown-reader`; profile `0-comparables/products/marklens-markdown-reader.md`. Registered because: coded as reading without editing (V09: reader, stated read-only). Cells: Mac App Store.

- **Publishes about itself.**
  - Kind (V08): desktop application "Marklens is a fast, native Markdown viewer for macOS, iPadOS, and iPhone." [p1]; undecidable (mobile: iPadOS/iPhone named, rule [clipped]
  - Reader or editor (V09): reader, stated read-only "No editor, no library, no friction." [p1]
  - Platforms (V10): macOS "Requires macOS 14.0 or later." [p1]; iOS "Requires iOS 18.0 or later." [p1]; iPadOS "Requires iPadOS 18.0 or later." [p1]
  - Markdown forms claimed (V13): GitHub Flavored Markdown "GitHub-Flavored Markdown — tables, task lists, footnotes, strikethrough" [p1]; tables [p1]; task lists [p1]; footnotes [p1]; diagrams "Mermaid" [p2: renders correctly (GFM [clipped]
  - Features the questions ask about: find V29: undecidable | appearance V32: light and dark modes "Light and dark theme matching the system appearance" [p1]; follows the system appearance, stated [p1] | print and export V33: export to PDF "Export to PDF on every platform" [p1] | files stay local V14: local, stated "Marklens never uploads them anywhere." [p3]
- **Charges.** Free [p1]; (b) free; (c) named open-source licence: "MIT License" [p2]
- **Buyer's all-in cost**, from the page text: price shape (V16b) free; beyond the price (V17): not stated; prerequisites (V11): minimum operating-system version named "Requires macOS 14.0 or later." [p1]; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): macOS.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): Mac App Store: userRatingCount=2; averageUserRating=5
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** 1.0.3 Sep 6 (version history, p1; month and day, no year); (b) not stated

## R39. Marklet - Markdown Viewer

Slug `marklet-markdown-viewer`; profile `0-comparables/products/marklet-markdown-viewer.md`. Registered because: coded as reading without editing (V09: reader, stated read-only). Cells: Mac App Store.

- **Publishes about itself.**
  - Kind (V08): desktop application "Marklet for macOS" [p2]; "Only for Mac" [p1]
  - Reader or editor (V09): reader, stated read-only "Marklet is a native, read-only viewer" [p2]
  - Platforms (V10): macOS "Platform macOS" [p2]
  - Markdown forms claimed (V13): tables "Tables, task lists, strikethrough, links, images, and heading anchors" [p1]; task lists [p1]; (b) not stated
  - Features the questions ask about: find V29: search within the document "full find-in-page (⌘F)" [p1] | links and images V30: shows local images "local images render" [p2]; shows remote images "unless you enable Load Remote Images for the current document" [p2] | file changed elsewhere V31: reloads when the file changes on disk, stated "reload live when the file changes on disk" [p2] | appearance V32: light and dark modes "light and dark themes" [p1]; font or size choice "adjust text zoom" [p2] | print and export V33: print "Print directly with ⌘P" [p1]; export to PDF "turns any document into a clean, paginated PDF" [p1]; share or send from the product [clipped] | files stay local V14: local, stated "Your documents never leave your Mac." [p1]
- **Charges.** Free [p1]; (b) free; (c) not stated
- **Buyer's all-in cost**, from the page text: price shape (V16b) free; beyond the price (V17): not stated; prerequisites (V11): minimum operating-system version named "Requires macOS 26.0 or later." [p1]; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): macOS.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): Mac App Store: userRatingCount=0; averageUserRating=0
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** 1.1 Jul 29 (version history, p1; month and day, no year); (b) not stated

## R40. MarkLook - Markdown Reader

Slug `marklook-markdown-reader`; profile `0-comparables/products/marklook-markdown-reader.md`. Registered because: coded as reading without editing (V09: reader, stated read-only). Cells: Mac App Store.

- **Publishes about itself.**
  - Kind (V08): desktop application "Requires macOS 13.0 or later." [p1]; undecidable (mobile: iPhone/iPad named, rule covers desktop OS only)
  - Reader or editor (V09): reader, stated read-only "offers no editor" [p1]
  - Platforms (V10): iOS "Requires iOS 16.2 or later." [p1]; iPadOS "Requires iPadOS 16.2 or later." [p1]; macOS "Requires macOS 13.0 or later." [p1]
  - Markdown forms claimed (V13): syntax-highlighted code blocks "Code Highlighting: Supports 180+ programming languages" [p1]; math "Math Equations: Flawless support for LaTeX math" [p1]; diagrams "Supports Mermaid flowcharts and [clipped]
  - Features the questions ask about: navigation V28: outline, contents or headings sidebar "New table of contents for quick section navigation" [p1]; jump to heading or section "quick section [clipped] | find V29: search across files or a folder "with search by file name, path, or content" [p1]; search within the document "Find text within a document" [clipped] | links and images V30: shows local images "images in your text appear instantly" [p1]; opens web links in the browser "Links now open in your default browser." [clipped] | appearance V32: themes provided "built-in appearances (themes)" [p1]; light and dark modes "All built-in themes support Dark Mode." [p1]; custom stylesheet [clipped] | print and export V33: export to PDF "Export documents as PDF" [p1]; copy as rich text or HTML "copy them as styled HTML" [p1] | files stay local V14: undecidable
- **Charges.** Free · In‑App Purchases [p1]; "MarkLook完全版 $4.99" [p1]; "one-time purchase" [p1]; (b) free with paid tier or features; one-time purchase; (c) not stated
- **Buyer's all-in cost**, from the page text: price shape (V16b) free with paid tier or features, one-time purchase; beyond the price (V17): not stated; prerequisites (V11): minimum operating-system version named "Requires iOS 16.2 or later." [p1]; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): macOS.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): Mac App Store: userRatingCount=0; averageUserRating=0
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** 1.3.1 Aug 21 (version history, p1; month and day, no year); (b) not stated

## R41. Markmap

Slug `markmap`; profile `0-comparables/products/markmap.md`. Registered because: coded as reading without editing (V09: reader, editing not stated). Cells: vscode.

- **Publishes about itself.**
  - Kind (V08): editor extension "This extension integrates markmap into VSCode." [p1]
  - Reader or editor (V09): reader, editing not stated "Preview markdown files as markmap" [p1]
  - Platforms (V10): inside a host program "Visual Studio Code" [p1]
  - Markdown forms claimed (V13): markdown named, no form named "Preview markdown files as markmap" [p1]; (b) not stated
  - Features the questions ask about: file changed elsewhere V31: undecidable | appearance V32: custom stylesheet "Custom CSS Extra CSS to customize the style of markmap." [p1]
- **Charges.** Free [p1]; (b) free; (c) not stated
- **Buyer's all-in cost**, from the page text: price shape (V16b) free; beyond the price (V17): not stated; prerequisites (V11): host program named "This extension integrates markmap into VSCode." [p1]; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): none of the three named.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): vscode: installs=266661; ratings=30; average=5.00; lastUpdated=2026-09-14
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** Mon, 14 Sep 2026 13:29:21 GMT (version 0.2.12 lastUpdated, p1; day precision); (b) not stated

## R42. Marko Viewer

Slug `marko-viewer`; profile `0-comparables/products/marko-viewer.md`. Registered because: coded as reading without editing (V09: reader, stated read-only). Cells: Mac App Store.

- **Publishes about itself.**
  - Kind (V08): desktop application "A fast, beautiful Markdown viewer for macOS, iOS, and iPadOS." [p1]; undecidable (mobile: iOS/iPadOS named, rule covers desktop [clipped]
  - Reader or editor (V09): reader, stated read-only "A clean, read-only Markdown viewer." [p2]
  - Platforms (V10): macOS "Available on macOS" [p2]; iOS "iOS & iPadOS" [p2]; iPadOS [p2]
  - Markdown forms claimed (V13): front matter "YAML frontmatter support (title, tags, status)" [p1]; tables "headings, code blocks, tables, lists" [p2]; (b) not stated
  - Features the questions ask about: navigation V28: outline, contents or headings sidebar "Document outline" [p1]; jump to heading or section "tap-to-navigate headings" [p1] | find V29: search within the document "In-document search" [p1] | links and images V30: follows links to other markdown files inside the product "click a relative .md link and it opens in a new window" [p2] | appearance V32: light and dark modes "Follows system light/dark mode" [p1]; follows the system appearance, stated [p1]; font or size choice "Adjustable [clipped] | files stay local V14: local, stated "All Markdown files are read and rendered locally on your device. No data leaves the app." [p3]
- **Charges.** Free · In‑App Purchases [p1]; "Marko Viewer $4.99" [p1]; (b) free with paid tier or features; (c) not stated
- **Buyer's all-in cost**, from the page text: price shape (V16b) free with paid tier or features; beyond the price (V17): not stated; prerequisites (V11): minimum operating-system version named "Requires macOS 26.2 or later." [p1]; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): macOS.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): Mac App Store: userRatingCount=0; averageUserRating=0
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** 1.0.1 May 31 (version history, p1; month and day, no year); (b) not stated

## R43. Marko: Markdown Viewer

Slug `marko-markdown-viewer`; profile `0-comparables/products/marko-markdown-viewer.md`. Registered because: coded as reading without editing (V09: reader, stated read-only). Cells: Mac App Store.

- **Publishes about itself.**
  - Kind (V08): desktop application "The same app on iPhone, iPad, and Mac." [p1]; undecidable (mobile: iPhone/iPad named, rule covers desktop OS only)
  - Reader or editor (V09): reader, stated read-only "Marko is a reader, not an editor." [p1]
  - Platforms (V10): iOS "Requires iOS 18.0 or later." [p1]; iPadOS "Requires iPadOS 18.0 or later." [p1]; macOS "Requires macOS 14.0 or later." [p1]
  - Markdown forms claimed (V13): GitHub Flavored Markdown "All of GitHub Flavored Markdown" [p2]; tables "Tables and task lists" [p2]; task lists [p2]; footnotes "footnotes" [p2]; diagrams "Mermaid diagrams" [p2]; math "KaTeX math" [clipped]
  - Features the questions ask about: navigation V28: outline, contents or headings sidebar "Outline sidebar" [p2]; jump to heading or section "Jump to any heading." [p2] | find V29: search within the document "Find in page with a live match count." [p2] | appearance V32: light and dark modes "Light, Dark, and System themes." [p1]; follows the system appearance, stated "Light, Dark, and System" [p2]; font or [clipped] | print and export V33: print "Print or export a clean PDF." [p2]; export to PDF [p2] | files stay local V14: local, stated "Your documents never leave your device." [p1]
- **Charges.** Free [p1]; "Marko is free to use." [p2]; (b) free; (c) not stated
- **Buyer's all-in cost**, from the page text: price shape (V16b) free; beyond the price (V17): not stated; prerequisites (V11): minimum operating-system version named "Requires macOS 14 or iOS/iPadOS 18 or later." [p2]; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): macOS.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): Mac App Store: userRatingCount=0; averageUserRating=0
- **Whom its pages address (V05):** Readers of what AI agents write "built for the Markdown you didn't write by hand, too: the .md that AI assistants and coding agents produce" [p1]
- **Last release and maintenance (V27):** 2.0.1 14h ago (version history, p1; relative, no calendar date); "1.0 Sep 3"; (b) not stated

## R44. MarkRead - Markdown Reader

Slug `markread-markdown-reader`; profile `0-comparables/products/markread-markdown-reader.md`. Registered because: coded as reading without editing (V09: reader, stated read-only). Cells: Mac App Store.

- **Publishes about itself.**
  - Kind (V08): desktop application "MarkRead reads Markdown on a Mac and an iPhone." [p2]; undecidable (mobile: iPhone/iPad named, rule covers desktop OS only)
  - Reader or editor (V09): reader, stated read-only "Not an editor — the original never changes." [p2]
  - Platforms (V10): iOS "Requires iOS 17.0 or later." [p1]; iPadOS "Requires iPadOS 17.0 or later." [p1]; macOS "Requires macOS 14.0 or later." [p1]
  - Markdown forms claimed (V13): GitHub Flavored Markdown "GFM, LaTeX, diagrams, syntax highlighting" [p2]; tables "GFM tables" [p2]; task lists "Task lists" [p2]; footnotes "Footnotes" [p2]; math "LaTeX" [p2]; diagrams "Mermaid" [clipped]
  - Features the questions ask about: navigation V28: outline, contents or headings sidebar "Library and outline sit either side" [p2] | find V29: search within the document "tap the magnifying glass to search the document" [p1] | links and images V30: opens web links in the browser "links go out to your browser" [p2] | appearance V32: themes provided "Twenty-one themes" [p2]; light and dark modes "Bone light and dark follow the system." [p2]; follows the system [clipped] | print and export V33: print "Library, outline, search, print" [p2] | files stay local V14: local by default, optional upload stated "Files stay on the device; what syncs goes through your own iCloud private database." [p1]
- **Charges.** Free · In‑App Purchases [p1]; "Pro is $2.99 a month, $19.99 a year, or $48.99 outright." [p2]; "Reading costs nothing." [p2]; (b) free with paid tier or features; subscription; one-time purchase; (c) not stated
- **Buyer's all-in cost**, from the page text: price shape (V16b) free with paid tier or features, subscription, one-time purchase; beyond the price (V17): not stated; prerequisites (V11): minimum operating-system version named "RequiresmacOS 14 · iOS 17" [p2]; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): macOS.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): Mac App Store: userRatingCount=0; averageUserRating=0
- **Whom its pages address (V05):** Readers of what AI agents write "People who read AI-generated reports, technical docs, notes, and long-form Markdown" [p1]
- **Last release and maintenance (V27):** 1.0.3 Sep 29 (version history, p1; month and day, no year); (b) not stated

## R45. MarkView

Slug `markview-markview-reader`; profile `0-comparables/products/markview-markview-reader.md`. Registered because: coded as reading without editing (V09: reader, stated read-only). Cells: Snap Store.

- **Publishes about itself.**
  - Kind (V08): desktop application "An AI-native Markdown reader for Windows and Linux" [p2]
  - Reader or editor (V09): reader, stated read-only "MarkView is intentionally read-only and lightweight" [p2]
  - Platforms (V10): Windows "for Windows and Linux" [p2]; Linux [p2]
  - Markdown forms claimed (V13): GitHub Flavored Markdown "GFM — Tables, task lists, footnotes, strikethrough, autolinks." [p2]; tables [p2]; task lists [p2]; footnotes [p2]; math "KaTeX math" [p2]; diagrams "Mermaid diagrams" [p2]; [clipped]
  - Features the questions ask about: navigation V28: outline, contents or headings sidebar "Table of Contents — Auto-generated from headings with scroll spy." [p2] | find V29: search within the document "In-Document Search — Ctrl+F" [p2] | file changed elsewhere V31: reloads when the file changes on disk, stated "Auto-reloads when the file is modified externally." [p2] | appearance V32: light and dark modes "Light and dark themes" [p1]; font or size choice "adjustable font size" [p1]; follows the system appearance, stated [clipped] | print and export V33: print "Print — Clean print output (content only)." [p2]
- **Charges.** Free to use, fork, and modify. [p2]; "price=0.0 USD" [p1]; (b) free; (c) named open-source licence: "MIT" [p1]
- **Buyer's all-in cost**, from the page text: price shape (V16b) free; beyond the price (V17): not stated; prerequisites (V11): minimum operating-system version named "Ubuntu 24.04+, Debian 13+" [p2]; runtime or interpreter named "sudo apt install libwebkit2gtk-4.1-0" [p2]; [clipped]; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): Linux, Windows.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): Snap Store: none given by API (find returns no install, rating or download counts)
- **Whom its pages address (V05):** Readers of what AI agents write "Made for anyone who reads a lot of Markdown — files generated by AI agents, docs downloaded from GitHub, or your own notes." [p1]
- **Last release and maintenance (V27):** 16 April 2026 (snap latest/stable, p1; day precision); (b) archived, deprecated or unmaintained, stated "no longer under active development" [p2]

## R46. MarkView

Slug `markview-markdownviewer`; profile `0-comparables/products/markview-markdownviewer.md`. Registered because: coded as reading without editing (V09: reader, editing not stated). Cells: Snap Store.

- **Publishes about itself.**
  - Kind (V08): desktop application "Cross-platform Markdown viewer for opening local .md files from Windows, macOS, and Linux desktops" [p2]
  - Reader or editor (V09): reader, editing not stated "A simple tool to view Markdown files rendered in your browser." [p2]
  - Platforms (V10): Windows "Supports Windows, Linux, and macOS." [p2]; Linux [p2]; macOS [p2]
  - Markdown forms claimed (V13): syntax-highlighted code blocks "syntax-highlighted code blocks" [p1]; (b) not stated
  - Features the questions ask about: links and images V30: follows links to other markdown files inside the product "Opens links to other local Markdown files in the viewer" [p1] | appearance V32: themes provided "Includes 10 theme variations across light and dark modes" [p1]; light and dark modes [p1]; follows the system appearance, [clipped]
- **Charges.** price=0.0 USD [p1]; (b) free; (c) named open-source licence: "MIT" [p1]
- **Buyer's all-in cost**, from the page text: price shape (V16b) free; beyond the price (V17): not stated; prerequisites (V11): runtime or interpreter named "PowerShell 7 (pwsh)" [p2]; minimum operating-system version named "Windows 10 (version 2004/19041) or later" [p2]; [clipped]; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): Linux, macOS, Windows.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): Snap Store: none given by API (find returns no install, rating or download counts)
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** 14 August 2026 (snap latest/stable 1.4.0, p1; day precision); (b) not stated

## R47. mcat

Slug `mcat`; profile `0-comparables/products/mcat.md`. Registered because: coded as reading without editing (V09: reader, editing not stated); and top five in homebrew:formula by 365-day installs (4 of 17 eligible comparables with a figure; 3,125). Cells: homebrew:formula.

- **Publishes about itself.**
  - Kind (V08): terminal program "Terminal image, video, PDF, and Markdown viewer" [p2]
  - Reader or editor (V09): reader, editing not stated "Markdown Viewer is markdown with ANSI formatting" [p2]
  - Platforms (V10): macOS "Bottle (binary package) installation support provided for: macOS on Linux" [p1]; Linux [p1]
  - Markdown forms claimed (V13): markdown named, no form named "Markdown Viewer is markdown with ANSI formatting" [p2]; (b) not stated
  - Features the questions ask about: appearance V32: themes provided "-t monokai # With a different theme" [p2] | print and export V33: export to HTML "mcat f1.rs f2.rs -o html > index.html # Into HTML" [p2]; export to another named format "# Into image" [p2]
- **Charges.** not stated; (b) not stated; (c) named open-source licence: "MIT license" [p2]
- **Buyer's all-in cost**, from the page text: price shape (V16b) not stated; beyond the price (V17): not stated; prerequisites (V11): build toolchain named "Depends on when building from source: rust" [p1]; undecidable (Chromium, FFmpeg); platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): Linux, macOS.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): homebrew:formula: 30d=36; 90d=631; 365d=3,125.  Further: GitHub Skardyy/mcat: not archived; last push 2026-10-03; newest release v0.6.5 2026-08-29; 17 releases in the last 365 days, 13,174 downloads (N5). Homebrew growth 0.14 (N1).
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** not stated; (b) not stated

## R48. MD Flow - Markdown Reader

Slug `md-flow-markdown-reader`; profile `0-comparables/products/md-flow-markdown-reader.md`. Registered because: coded as reading without editing (V09: reader, stated read-only). Cells: Mac App Store.

- **Publishes about itself.**
  - Kind (V08): desktop application "MD Flow is a native app for Mac, iPhone, and iPad" [p2]; undecidable (mobile: iPhone/iPad named, rule covers desktop OS only)
  - Reader or editor (V09): reader, stated read-only "MD Flow is not a note-taking app, a PKM system, or a Markdown editor." [p1]
  - Platforms (V10): iOS "Requires iOS 17.0 or later." [p1]; iPadOS "Requires iPadOS 17.0 or later." [p1]; macOS "Requires macOS 14.0 or later." [p1]
  - Markdown forms claimed (V13): syntax-highlighted code blocks "syntax-highlighted code, tables, and Mermaid diagrams" [p1]; tables [p1]; diagrams [p1]; math "math, diagrams, callouts and tables all survive the page" [p2]; callouts [clipped]
  - Features the questions ask about: navigation V28: outline, contents or headings sidebar "Navigate long documents with a table of contents" [p1] | find V29: search across files or a folder "Search within the current folder" [p1] | links and images V30: follows links to other markdown files inside the product "A link to another .md file opens it right here" [p1]; follows links to headings [clipped] | file changed elsewhere V31: reloads when the file changes on disk, stated "edit a file somewhere else and MD Flow follows each save" [p1] | print and export V33: export to PDF "Export any document as a polished PDF, then share or save it" [p1]; share or send from the product "then share or save it" [clipped] | files stay local V14: local, stated "your content is never uploaded to browse or preview it." [p2]
- **Charges.** Free · In‑App Purchases [p1]; "$7.99one time — not per month, not per year" [p2]; "Small Support $1.99" "Medium Support $3.99" "Large Support $5.99" [p1]; (b) free with paid tier or features; one-time purchase; donation or sponsorship invited, use [clipped]
- **Buyer's all-in cost**, from the page text: price shape (V16b) free with paid tier or features, one-time purchase, donation or sponsorship invited, use free; beyond the price (V17): not stated; prerequisites (V11): minimum operating-system version named "Requires macOS 14.0 or later." [p1]; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): macOS.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): Mac App Store: userRatingCount=2; averageUserRating=3
- **Whom its pages address (V05):** Readers of what AI agents write "You save your AI output as Markdown. Now you can actually read it." [p2]
- **Last release and maintenance (V27):** 1.15 Oct 1 (version history, p1; month and day, no year); (b) not stated

## R49. md Viewer: Markdown & Mermaid

Slug `md-viewer-markdown-mermaid`; profile `0-comparables/products/md-viewer-markdown-mermaid.md`. Registered because: coded as reading without editing (V09: reader, editing not stated). Cells: Mac App Store.

- **Publishes about itself.**
  - Kind (V08): mobile application {"iPhone, iPad, Mac" @listing}; desktop application {"iPhone, iPad, Mac" @listing}; service {"Ouvrir le lecteur en ligne" [clipped]
  - Reader or editor (V09): reader, editing not stated {"md Viewer opens them as real documents" @listing}
  - Platforms (V10): iOS {"Requires iOS 26.4 or later. iPhone"}; iPadOS {"Requires iPadOS 26.4 or later. iPad"}; macOS {"Requires macOS 26.4 or later. Mac"} {listing}
  - Markdown forms claimed (V13): a: tables; diagrams; callouts or admonitions; wiki-links {"headings, tables, diagrams, maps and callouts"; "Mermaid diagrams (flowcharts, sequences, Gantt, mind maps) and maps"; "Callouts and [clipped]
  - Features the questions ask about: appearance V32: undecidable {"Dark mode and an interface in 5 languages." @listing: dark mode named alone; "Sombre, Console, Sépia et ..." [clipped] | print and export V33: export to PDF {"Export to PDF, Word and PowerPoint." @listing}; export to another named format {"Word and PowerPoint" @listing} | files stay local V14: local, stated {"No account, nothing uploaded: your documents stay on your devices." @listing}
- **Charges.** a: "Free"; "Free, no account." {listing}; b: free; c: not stated
- **Buyer's all-in cost**, from the page text: price shape (V16b) see V16; beyond the price (V17): undecidable {"The AI requires an Apple Intelligence-compatible device." @listing: a hardware requirement for a named feature; the values list only a [clipped]; prerequisites (V11): minimum operating-system version named {"Requires macOS 26.4 or later" @listing}; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): macOS.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): Mac App Store: userRatingCount=0; averageUserRating=0
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** a: "Sep 19" (day; version 1.2.1, year not published); b: not stated

## R50. md-reader/md-reader

Slug `md-reader-md-reader`; profile `0-comparables/products/md-reader-md-reader.md`. Registered because: coded as reading without editing (V09: reader, editing not stated); and top five in github-topics:markdown-reader by stars (3 of 5 eligible comparables with a figure; 475). Cells: chrome-web-store; github-topics:markdown-reader.

- **Publishes about itself.**
  - Kind (V08): browser extension {"Markdown Reader is a Markdown browser extension for Chrome, Microsoft Edge, and Firefox." @md-reader.github.io; category line [clipped]
  - Reader or editor (V09): reader, editing not stated {"primarily a Markdown viewer and reading extension ... edit the file in your favorite editor and preview changes in the [clipped]
  - Platforms (V10): inside a host program {"currently supports Google Chrome, Microsoft Edge, and Mozilla Firefox" @md-reader.github.io}
  - Markdown forms claimed (V13): a: tables; task lists; footnotes; math; diagrams; syntax-highlighted code blocks {"tables, task lists, footnotes, code blocks, Mermaid diagrams, KaTeX math formulas" @md-reader.github.io; [clipped]
  - Features the questions ask about: navigation V28: outline, contents or headings sidebar {"Sidebar TOC supports multi-level headings" @md-reader.github.io}; jump to heading or section [clipped] | file changed elsewhere V31: reloads when the file changes on disk, stated {"changes made in your editor can be reflected in the browser after the configured refresh [clipped] | appearance V32: themes provided {"Provide high-quality dark and light themes" @Chrome listing}; light and dark modes {"Switch between light and dark modes" [clipped] | files stay local V14: local, stated {"Local Markdown files are rendered in your browser and are not uploaded to Markdown Reader servers." @md-reader.github.io}
- **Charges.** a: not stated; b: free with paid tier or features {"the free version" and "Subscribe to the Pro plan to unlock more features" @md-reader.github.io}; subscription {"Subscribe to the Pro plan" @md-reader.github.io/pricing}; c: named open-source [clipped]
- **Buyer's all-in cost**, from the page text: price shape (V16b) see V16; beyond the price (V17): not stated; prerequisites (V11): host program named {"Markdown Reader is a Markdown browser extension for Chrome, Microsoft Edge, and Firefox." @md-reader.github.io}; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): none of the three named.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): chrome-web-store: users=100000 (store shows a rounded figure); rating=4.66; ratings=131; search rank "markdown viewer" #2, "markdown" #1 || github-topics:markdown-reader: stars=475; archived=false; last_push=2026-10-01
- **Whom its pages address (V05):** Writers and authors; Students and academics; Developers and coders; Teams, businesses and organisations {"useful for developers, technical writers, students, product teams, and anyone who reads [clipped]
- **Last release and maintenance (V27):** a: October 4, 2026 (day; Chrome listing "Updated"); b: archived, deprecated or unmaintained, stated {"This repository contains the old source code of Markdown Reader(2.x version) and is no longer maintained." @README, while Chrome listing shows "Version [clipped]

## R51. md-tui

Slug `md-tui`; profile `0-comparables/products/md-tui.md`. Registered because: coded as reading without editing (V09: reader, editing not stated). Cells: homebrew:formula.

- **Publishes about itself.**
  - Kind (V08): terminal program {"terminal-based application" @README; "Markdown renderer in the terminal written in rust" @Homebrew}; component {"It's possible to [clipped]
  - Reader or editor (V09): reader, editing not stated {"viewing and navigating Markdown files" @README; "e | Edit file in `$EDITOR`" is editing in another program}
  - Platforms (V10): macOS {"macOS on Apple Silicon" @formulae.brew.sh}; Linux {"Linux ARM64 ✅ x86_64 ✅" @formulae.brew.sh}
  - Markdown forms claimed (V13): a: syntax-highlighted code blocks {"code highlighting languages listed "Bash/sh, C/C++, CSS, ..."" @README}; undecidable for CriticMarkup {"MD-TUI renders CriticMarkup highlight/comment pairs without [clipped]
  - Features the questions ask about: navigation V28: undecidable {"Select. Open link, search, or toggle fold on selected ``" and "D | Enter select details mode. Cycle through `` blocks" [clipped] | find V29: search within the document {"f or / | Search"; "n or N | Jump to next or previous search result" @README} | appearance V32: themes provided {"Press `T` ... to choose a color theme. `Custom` ... `Match terminal` ... `Light`, `Dark`, `Warm light`, and `High [clipped]
- **Charges.** a: not stated; b: not stated; c: named open-source licence AGPL-3.0-or-later {"License: AGPL-3.0-or-later" @formulae.brew.sh; "AGPL-3.0 license" @github.com}
- **Buyer's all-in cost**, from the page text: price shape (V16b) see V16; beyond the price (V17): not stated; prerequisites (V11): undecidable {"### Requirements 1. A terminal 2. Nerd font" @README: a terminal and a font are neither runtime, host program, package manager, [clipped]; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): Linux, macOS.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): homebrew:formula: 30d=73; 90d=181; 365d=421.  Further: GitHub henriklovhaug/md-tui: not archived; newest release v0.11.0 2026-10-02; 10 releases in the last 365 days, 2,497 downloads (N5). Homebrew growth 2.08 (N1).
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** a: not stated ("Current versions: stable ✅ 0.11.0" carries no date); b: not stated

## R52. MD-Viewer

Slug `md-viewer-6752493034`; profile `0-comparables/products/md-viewer-6752493034.md`. Registered because: coded as reading without editing (V09: reader, editing not stated). Cells: Mac App Store.

- **Publishes about itself.**
  - Kind (V08): desktop application {"Built specifically for macOS, not a web wrapper" @listing}
  - Reader or editor (V09): reader, editing not stated {"when you just need to READ Markdown files" @listing}
  - Platforms (V10): macOS {"Requires macOS 10.13.0 or later. Mac" @listing}; Windows {"Beautiful Native Markdown Viewer for Mac & Windows" @md-viewer.com site title}
  - Markdown forms claimed (V13): a: syntax-highlighted code blocks {"Syntax Highlighting - Support for 100+ programming languages" @md-viewer.com}; b: not stated
  - Features the questions ask about: navigation V28: outline, contents or headings sidebar {"Table of Contents - Auto-generated navigation sidebar." @md-viewer.com} | find V29: undecidable {"Search - Find anything in your documents quickly." @md-viewer.com: "your documents" plural, scope not named, sentence not [clipped] | appearance V32: undecidable {"Dark Mode - Easy on the eyes with automatic theme persistence." @md-viewer.com: dark mode named alone; no light mode or [clipped] | print and export V33: export to PDF {"PDF Export - Export your markdown files with preserved formatting." @md-viewer.com} | files stay local V14: local, stated {"Everything stays on your Mac, no cloud, no tracking" @listing; "Your markdown files never leave your computer." [clipped]
- **Charges.** a: "Free" {listing; "MD Viewer Free / Free" @md-viewer.com}; b: free; c: not stated
- **Buyer's all-in cost**, from the page text: price shape (V16b) see V16; beyond the price (V17): not stated; prerequisites (V11): minimum operating-system version named {"Requires macOS 10.13.0 or later" @listing}; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): macOS, Windows.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): Mac App Store: userRatingCount=0; averageUserRating=0
- **Whom its pages address (V05):** Developers and coders; Writers and authors; Students and academics {"Perfect for: Developers browsing project documentation / Writers reviewing Markdown drafts / Students reading course materials" [clipped]
- **Last release and maintenance (V27):** a: "Jun 17" (day; "Version 1.2.1 Jun 17", year not published; listing version history); b: not stated

## R53. md2term

Slug `md2term`; profile `0-comparables/products/md2term.md`. Registered because: coded as reading without editing (V09: reader, editing not stated). Cells: debian:apt-cache search markdown.

- **Publishes about itself.**
  - Kind (V08): terminal program {"Markdown parser for highlights and colors in terminal" @apt-cache}
  - Reader or editor (V09): reader, editing not stated {"used satisfactorily for viewing other markdown text" @apt-cache}
  - Platforms (V10): Linux {"Origin: Ubuntu" @apt-cache}
  - Markdown forms claimed (V13): a: GitHub Flavored Markdown {"é uma marcação válida do markdown GFM" (en: is a valid GFM markdown mark-up) @README}; b: not stated
  - Features the questions ask about: V28 to V33 and V14 all not stated
- **Charges.** a: not stated; b: not stated; c: named open-source licence "GPLv3+: GNU GPL versão 3 ou posterior" (en: GPLv3+: GNU GPL version 3 or later) {@README; "Este é um software livre" (en: This is free software)}
- **Buyer's all-in cost**, from the page text: price shape (V16b) see V16; beyond the price (V17): not stated; prerequisites (V11): runtime or interpreter named {"Bash" under "Dependências"; "Depends: less, libhtml-parser-perl, pandoc" @README, apt-cache}; build toolchain named [clipped]; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): Linux.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): debian:apt-cache search markdown: not published by the list (no install count in apt-cache)
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** a: not stated ("Version: 0.0.7-2" carries no date; "Copyright (C) 2022 Blau Araujo" is not a release date); b: not stated

## R54. mdcat

Slug `mdcat`; profile `0-comparables/products/mdcat.md`. Registered because: coded as reading without editing (V09: reader, editing not stated); and top five in homebrew:formula by 365-day installs (3 of 17 eligible comparables with a figure; 5,360). Cells: homebrew:formula.

- **Publishes about itself.**
  - Kind (V08): terminal program {"Show markdown documents on text terminals" @formulae.brew.sh}
  - Reader or editor (V09): reader, editing not stated {"Show markdown documents on text terminals" @formulae.brew.sh}
  - Platforms (V10): macOS {"macOS on Apple Silicon" @formulae.brew.sh}; Linux {"Linux ARM64 ✅ x86_64 ✅" @formulae.brew.sh; "AUR (Arch Linux)", "Void Linux" @README}; [clipped]
  - Markdown forms claimed (V13): a: CommonMark; footnotes; tables; math; diagrams {"nicely renders all basic CommonMark syntax"; "renders footnotes and inline markup in table cells"; "renders inline and display math"; "renders [clipped]
  - Features the questions ask about: navigation V28: jump to heading or section {"adds jump marks for headings in [iTerm2] (jump forwards and backwards with ⇧⌘↓ and ⇧⌘↑)" @README} | file changed elsewhere V31: reloads when the file changes on disk, stated {"can watch a file and re-render it on every save with `--watch`, for a live preview while [clipped] | appearance V32: themes provided {"ships eight built-in colour themes" @README}; light and dark modes {"plus auto dark/light detection" @README}
- **Charges.** a: not stated; b: not stated; c: named open-source licence "MPL-2.0" {"License: MPL-2.0" @formulae.brew.sh}; "Apache 2.0 license" for some files {@README}
- **Buyer's all-in cost**, from the page text: price shape (V16b) see V16; beyond the price (V17): not stated; prerequisites (V11): undecidable {"mdcat requires that the terminal supports strikethrough formatting and [inline links][osc8]."; "Building requires `libcurl`."; [clipped]; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): Linux, macOS, Windows.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): homebrew:formula: 30d=683; 90d=2,522; 365d=5,360.  Further: GitHub swsnr/mdcat is archived (README: no longer maintained, points to a fork; last push 2026-06-19; newest release 2024-12-14). GitHub BIRSAx2/mdcat, which the Homebrew formula now points to: not archived; last push 2026-10-01; 15 releases in the last 365 days (mdcat-2.18.0, 2026-10-01), 2,715 downloads (N5). Homebrew growth 1.53 (N1).
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** a: not stated ("Current versions: stable ✅ 2.18.0" carries no date); b: actively maintained, stated {"Currently maintained by [BIRSAx2]" @README}

## R55. mdfried

Slug `mdfried`; profile `0-comparables/products/mdfried.md`. Registered because: coded as reading without editing (V09: reader, editing not stated). Cells: homebrew:formula.

- **Publishes about itself.**
  - Kind (V08): terminal program {"Terminal markdown viewer" @formulae.brew.sh}
  - Reader or editor (V09): reader, editing not stated {"a markdown viewer for the terminal" @README}
  - Platforms (V10): macOS {"binaries for Mac and Windows" @README; "macOS on Apple Silicon" @formulae.brew.sh}; Windows {"binaries for Mac and Windows" @README}; Linux [clipped]
  - Markdown forms claimed (V13): a: syntax-highlighted code blocks {"Syntax highlighting in codeblocks with [arborium]" @README}; diagrams {"Mermaid diagram rendering" @README}; b: not stated
  - Features the questions ask about: navigation V28: jump to heading or section {"Jump to headers in `#kebab-case`." @README} | find V29: undecidable {"Search" @README feature list: scope not named, sentence not about the open document} | links and images V30: follows links to other markdown files inside the product {"Can follow local `.md` links." @README}; follows links to headings within the [clipped] | appearance V32: themes provided {"Theme [configuration](#configuration) support"; "`mdfried --print-config` prints out a full example config with a full [clipped]
- **Charges.** a: not stated; b: not stated; c: named open-source licence "GPL-3.0-or-later" {"License: GPL-3.0-or-later" @formulae.brew.sh}
- **Buyer's all-in cost**, from the page text: price shape (V16b) see V16; beyond the price (V17): not stated; prerequisites (V11): undecidable {"Needs a chafa package with development headers, usually called something like `libchafa-dev`..."; "Homebrew: Depends on: chafa, [clipped]; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): Linux, macOS, Windows.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): homebrew:formula: 30d=84; 90d=258; 365d=2,185.  Further: GitHub benjajaja/mdfried: not archived; newest release v0.22.7 2026-10-08; 41 releases in the last 365 days, 2,233 downloads (N5). Homebrew growth 0.46 (N1).
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** a: not stated ("Current versions: stable ✅ 0.22.7"); b: not stated

## R56. mdless

Slug `mdless`; profile `0-comparables/products/mdless.md`. Registered because: coded as reading without editing (V09: reader, editing not stated); and top five in homebrew:formula by 365-day installs (5 of 17 eligible comparables with a figure; 2,710). Cells: homebrew:formula.

- **Publishes about itself.**
  - Kind (V08): terminal program {"a formatted and highlighted view of Markdown files in Terminal"; "`mdless` is a utility" @README}
  - Reader or editor (V09): reader, editing not stated {"provides a formatted and highlighted view of Markdown files in Terminal" @README}
  - Platforms (V10): macOS {"macOS on Apple Silicon golden gate ✅ tahoe ✅ sequoia ✅ sonoma ✅ macOS on Intel sonoma ✅" @formulae.brew.sh}; Linux {"Linux ARM64 ✅ x86_64 ✅" [clipped]
  - Markdown forms claimed (V13): a: footnotes; tables; wiki-links {"Display footnotes after each paragraph"; "Format tables"; "--[no-]wiki-links Highlight [[wiki links]]" @README}; b: not stated
  - Features the questions ask about: navigation V28: outline, contents or headings sidebar {"List headlines in document"; "-l, --list List headers in document and exit" @README, a listing not [clipped] | links and images V30: shows local images {"Inline image display (local, optionally remote)" @README}; shows remote images {same} | appearance V32: themes provided {"-t, --theme=THEME_NAME Specify an alternate color theme to load" @README}
- **Charges.** a: not stated; b: not stated; c: named open-source licence "MIT" {"License: MIT" @formulae.brew.sh}
- **Buyer's all-in cost**, from the page text: price shape (V16b) see V16; beyond the price (V17): not stated; prerequisites (V11): runtime or interpreter named {"Depends on: ruby 4.0.7" @formulae.brew.sh}; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): Linux, macOS.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): homebrew:formula: 30d=50; 90d=316; 365d=2,710.  Further: GitHub ttscoff/mdless: not archived; last push 2026-06-25; newest release 2.1.68 2026-06-25; 4 releases in the last 365 days, no assets (N5). Homebrew growth 0.22 (N1).
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** a: not stated ("Current versions: stable ✅ 2.1.68"); b: not stated

## R57. Mdly – Markdown Viewer

Slug `mdly-markdown-viewer`; profile `0-comparables/products/mdly-markdown-viewer.md`. Registered because: coded as reading without editing (V09: reader, stated read-only). Cells: Mac App Store.

- **Publishes about itself.**
  - Kind (V08): mobile application {"across iPhone, iPad, and Mac" @listing}; desktop application {same, Mac}
  - Reader or editor (V09): reader, stated read-only {"Mdly is intentionally read-only — no editing distractions." @listing}
  - Platforms (V10): iOS {"Requires iOS 18.0 or later. iPhone"}; iPadOS {"Requires iPadOS 18.0 or later."}; macOS {"Requires macOS 15.0 or later."} {listing}
  - Markdown forms claimed (V13): a: GitHub Flavored Markdown; tables; syntax-highlighted code blocks; diagrams; front matter {"Headings, lists, tables, blockquotes; Syntax-highlighted code blocks; GitHub-style Markdown rendering"; [clipped]
  - Features the questions ask about: navigation V28: outline, contents or headings sidebar {"Slide-up Table of Contents navigation" @listing; "目次自動生成" (en: automatic table of contents [clipped] | find V29: search across files or a folder {"Full-text search across files" @listing} | file changed elsewhere V31: reloads when the file changes on disk, stated {"リアルタイム監視：ファイルの変更を検知して自動的に表示を更新（Mac版）" (en: real-time monitoring: detects file changes and [clipped] | appearance V32: themes provided {"Dark and light themes" @listing}; light and dark modes {same}
- **Charges.** a: "$1.99" {listing}; b: undecidable ("$1.99" is a bare store price with no period or "one-time" wording); c: not stated
- **Buyer's all-in cost**, from the page text: price shape (V16b) see V16; beyond the price (V17): not stated; prerequisites (V11): minimum operating-system version named {"Requires iOS 18.0 or later" @listing; "必要環境: iOS 17.0以降（iPhone/iPad）、macOS 14.0以降（Mac）" (en: required: iOS [clipped]; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): macOS.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): Mac App Store: userRatingCount=1; averageUserRating=1
- **Whom its pages address (V05):** Developers and coders; Writers and authors {"Built for developers, writers, and anyone who keeps documentation in Markdown" @listing; "開発者、テクニカルライター、ドキュメント管理者など" (en: developers, technical writers, [clipped]
- **Last release and maintenance (V27):** a: "Apr 21" (day; version 1.6, year not published); b: not stated

## R58. mdp

Slug `mdp`; profile `0-comparables/products/mdp.md`. Registered because: coded as reading without editing (V09: reader, editing not stated). Cells: debian:apt-cache search markdown; homebrew:formula.

- **Publishes about itself.**
  - Kind (V08): terminal program {"mdp is a command-line program" @apt-cache}
  - Reader or editor (V09): reader, editing not stated {"write your presentation content in the text editor of your preference and launch the presentation from the command-line" [clipped]
  - Platforms (V10): macOS {"On MacOS" @README; "macOS on Apple Silicon" @formulae.brew.sh}; Linux {"Linux ARM64 ✅ x86_64 ✅" @formulae.brew.sh; "On Arch Linux", "on [clipped]
  - Markdown forms claimed (V13): a: markdown named, no form named {"Supports basic markdown formatting" @README}; b: not stated
  - Features the questions ask about: file changed elsewhere V31: manual refresh, stated {"r - reload input file" @README}
- **Charges.** a: not stated; b: not stated; c: named open-source licence "GPL-3.0-or-later" {"License: GPL-3.0-or-later" @formulae.brew.sh}
- **Buyer's all-in cost**, from the page text: price shape (V16b) see V16; beyond the price (V17): not stated; prerequisites (V11): undecidable {"mdp needs the ncursesw headers to compile."; "To enjoy mdp's color fading feature: export TERM=xterm-256color" @README: libraries and a [clipped]; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): Linux, macOS.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): debian:apt-cache search markdown: not published by the list (no install count in apt-cache) || homebrew:formula: 30d=21; 90d=124; 365d=310
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** a: not stated ("Version: 1.0.15-1", "stable ✅ 1.0.19" carry no date); b: not stated

## R59. mdserv

Slug `mdserv`; profile `0-comparables/products/mdserv.md`. Registered because: coded as reading without editing (V09: reader, editing not stated). Cells: Snap Store.

- **Publishes about itself.**
  - Kind (V08): desktop application {"Install mdserv on Linux" @snapcraft.io/mdserv}
  - Reader or editor (V09): reader, editing not stated {"Preview markdown files in web browser" @snapcraft.io/mdserv}
  - Platforms (V10): Linux {"Install mdserv on Linux"; "Arch Linux, CentOS, Debian, elementary OS, Fedora ..." @snapcraft.io/mdserv}
  - Markdown forms claimed (V13): a: markdown named, no form named {"Preview markdown files in web browser" @snapcraft.io/mdserv}; b: not stated
  - Features the questions ask about: appearance V32: undecidable {"Use CSS since version 1.2" @snapcraft.io/mdserv: does not say the buyer supplies the CSS}
- **Charges.** a: not stated; b: not stated; c: undecidable {"License CNRI-Python-GPL-Compatible" @snapcraft.io/mdserv: a named licence not stated to be open-source; the Gitee page says "License: Not specified"}
- **Buyer's all-in cost**, from the page text: price shape (V16b) see V16; beyond the price (V17): not stated; prerequisites (V11): package manager named as required to install {"Don't have snapd? Get set up for snaps." @snapcraft.io/mdserv}; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): Linux.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): Snap Store: none given by API (find returns no install, rating or download counts)
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** a: "2026-10-07" (day; Gitee "Last Updated"); the Snap page gives "Last updated 5 May 2018 - latest/stable"; b: undecidable {"This snap hasn't been updated in a while. It might be unmaintained and have stability or security issues." @snapcraft.io/mdserv: [clipped]

## R60. mdserve

Slug `mdserve`; profile `0-comparables/products/mdserve.md`. Registered because: coded as reading without editing (V09: reader, editing not stated). Cells: homebrew:formula.

- **Publishes about itself.**
  - Kind (V08): other kind {"Claude Code Plugin: mdserve includes a Claude Code plugin" @README}; undecidable for the main program ("Markdown preview server", [clipped]
  - Reader or editor (V09): reader, editing not stated {"Markdown preview server for AI coding agents." @README}
  - Platforms (V10): macOS {"### macOS (Homebrew)" @README}; Linux {"### Linux" @README}
  - Markdown forms claimed (V13): a: GitHub Flavored Markdown; tables; task lists; diagrams {"Full GFM support (tables, task lists, code blocks), Mermaid diagrams" @README}; b: not stated
  - Features the questions ask about: file changed elsewhere V31: reloads when the file changes on disk, stated {"Instant live reload. File changes appear in the browser immediately via WebSocket." @README} | appearance V32: themes provided {"Five built-in themes (light, dark, and Catppuccin variants)" @README}; light and dark modes {same}
- **Charges.** a: not stated; b: not stated; c: named open-source licence "MIT" {"License: MIT" @formulae.brew.sh; "The code stays available under the MIT license." @README}
- **Buyer's all-in cost**, from the page text: price shape (V16b) see V16; beyond the price (V17): not stated; prerequisites (V11): none needed, stated {"No runtime dependencies to manage." @README}; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): Linux, macOS.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): homebrew:formula: 30d=11; 90d=43; 365d=371
- **Whom its pages address (V05):** Readers of what AI agents write {"mdserve was built to give humans a live rendered view of the markdown that AI coding agents produce." @README}
- **Last release and maintenance (V27):** a: not stated ("(September 2026)" dates the archive notice; v1.1.0 has no date); b: archived, deprecated or unmaintained, stated {"This project is archived and no longer maintained (September 2026)." @README; "Public archive"; "[Archived] Markdown preview [clipped]

## R61. MDV

Slug `mdv`; profile `0-comparables/products/mdv.md`. Registered because: coded as reading without editing (V09: reader, editing not stated). Cells: alternativeto:Marked (AlternativeTo entry for Marked); homebrew:formula.

- **Publishes about itself.**
  - Kind (V08): desktop application {"the best Markdown viewer for Mac"; "Download MDV for macOS 13+"}; terminal program {"a command line tool called mdv that opens [clipped]
  - Reader or editor (V09): reader, editing not stated {(A) "It's like Preview... but for Markdown!" @mowglii.com/mdv/; (B) "a Python based Markdown viewer for the terminal" [clipped]
  - Platforms (V10): macOS {"Download MDV for macOS 13+" @mowglii.com/mdv/}; (B) macOS {"macOS on Apple Silicon ... macOS on Intel sonoma ✅" @formulae.brew.sh}; Linux [clipped]
  - Markdown forms claimed (V13): a: GitHub Flavored Markdown; front matter; math; diagrams {"Github-flavored Markdown rendering"; "YAML and TOML front matter blocks"; "Mermaid diagrams"; "KaTeX math expressions" @mowglii.com/mdv/}; [clipped]
  - Features the questions ask about: navigation V28: outline, contents or headings sidebar {"A Table of Contents sidebar" @mowglii.com/mdv/} | find V29: search within the document {"Document search" @mowglii.com/mdv/} | file changed elsewhere V31: reloads when the file changes on disk, stated {"A File Watcher which updates as you edit" @mowglii.com/mdv/}; (B) reloads when the file [clipped] | appearance V32: themes provided {"mdv ships with > 200 luminocity sorted themes" @README} | print and export V33: print {"Print to PDF or paper" @mowglii.com/mdv/}; export to PDF {same sentence}
- **Charges.** a: "Free product" {AlternativeTo extraction, unchecked: "Licensing Proprietary and Free product."}; b: free; c: proprietary or end-user licence agreement, stated {"Proprietary" extraction, unchecked}; (B) c: named open-source licence "BSD-3-Clause" [clipped]
- **Buyer's all-in cost**, from the page text: price shape (V16b) see V16; beyond the price (V17): not stated; prerequisites (V11): minimum operating-system version named {"Download MDV for macOS 13+" @mowglii.com/mdv/}; (B) runtime or interpreter named {"python == 2.7 or > 3.5" [clipped]; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): Linux, macOS.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): alternativeto:Marked (AlternativeTo entry for Marked): rank=77; page=7; Like; alternatives-listed-for-this-entry=not shown; license=Free Proprietary Origin United States Platforms Mac United States More about MDV Good [clipped] || homebrew:formula: 30d=25; 90d=155; 365d=684.  Further: PyPI mdv 2,510 downloads last month, last release 1.7.5 on 2023-10-02 (N4). GitHub axiros/terminal_markdown_viewer: not archived; last push 2024-05-15; newest release 1.6.3 on 2016-12-08 (N5). Homebrew growth 0.44 (N1).
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** a: "July 2016" (month; README dated entry "### July 2016: Sort of an excuse for the long long time w/o an update", product B; "Current versions: stable ✅ 1.7.5 Revision: 1" undated); product A none; b: not stated

## R62. Meva

Slug `meva`; profile `0-comparables/products/meva.md`. Registered because: coded as reading without editing (V09: reader, stated read-only). Cells: alternativeto:Typora; alternativeto:Marked (AlternativeTo entry for Marked); Mac App Store.

- **Publishes about itself.**
  - Kind (V08): desktop application {"Native macOS app" @listing; "Available for macOS, Windows & Linux" @usemeva.com}
  - Reader or editor (V09): reader, stated read-only {"Because you deserve a tool built specifically for reading, not editing." @usemeva.com}
  - Platforms (V10): macOS {"Requires macOS 10.13 or later. Mac" @listing}; Windows {"Available for macOS, Windows & Linux" @usemeva.com}; Linux {same}
  - Markdown forms claimed (V13): a: tables; math; diagrams; syntax-highlighted code blocks {"LaTeX math equations"; "Mermaid diagrams, tables, and more" @listing; "Syntax highlighting powered by Shiki" @usemeva.com}; b: not stated
  - Features the questions ask about: navigation V28: outline, contents or headings sidebar {"Collapsible Table of Contents sidebar" @listing}; jump to heading or section {"Click to jump" [clipped] | find V29: search within the document {"In-document search" @listing}; search across files or a folder {"Search everything ... Across all your files." [clipped] | file changed elsewhere V31: reloads when the file changes on disk, stated {"Live reload — edit in any editor, see changes instantly" @listing; "Meva detects file [clipped] | appearance V32: themes provided {"All 12 themes (Nord, Dracula, Tokyo Night, and more)" @listing}; light and dark modes {"1 light + 1 dark theme" @listing} | print and export V33: export to PDF {"Share as PDF or HTML" @usemeva.com}; export to HTML {same}; print {"Print / Export to PDF now works correctly." release [clipped] | files stay local V14: local, stated {"Your markdown files and documents remain entirely on your device and are never sent anywhere." @usemeva.com/privacy}
- **Charges.** a: "Free ... $0 forever"; "Pro ... $14.99 one-time"; "Free · In‑App Purchases" {usemeva.com; listing}; b: free with paid tier or features {"Free to use. Pro upgrade available"}; one-time purchase {"One-time purchase. No subscriptions."}; c: [clipped]
- **Buyer's all-in cost**, from the page text: price shape (V16b) see V16; beyond the price (V17): not stated; prerequisites (V11): minimum operating-system version named {"Requires macOS 10.13 or later" @listing}; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): Linux, macOS, Windows.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): alternativeto:Typora: rank=212; page=18; Like; alternatives-listed-for-this-entry=not shown; license=Freemium Proprietary Origin United States Platforms Mac Windows Linux United States + 3 [clipped] || alternativeto:Marked (AlternativeTo entry for Marked): rank=71; page=6; Like; alternatives-listed-for-this-entry=not shown; license=Freemium Proprietary Origin United States Platforms Mac Windows Linux United States + 3 More [clipped] || Mac App Store: userRatingCount=0; averageUserRating=0
- **Whom its pages address (V05):** Developers and coders; Students and academics; Writers and authors {"Built for people who live in markdown." with "Software Engineers", "Students & Researchers", "Technical Writers", "Data [clipped]
- **Last release and maintenance (V27):** a: "Apr 13" (day; version 1.3.0 in the listing, year not published); b: not stated

## R63. mohzy83/NppMarkdownPanel

Slug `mohzy83-nppmarkdownpanel`; profile `0-comparables/products/mohzy83-nppmarkdownpanel.md`. Registered because: coded as reading without editing (V09: reader, editing not stated). Cells: github-topics:markdown-viewer.

- **Publishes about itself.**
  - Kind (V08): editor extension [R: 'Lightweight Notepad++ plugin to preview Markdown files']
  - Reader or editor (V09): reader, editing not stated [R: 'lightweight plugin to preview markdown within Notepad++']
  - Platforms (V10): Windows [R: 'Note for Windows 7 users: WebView2 Edge is required']; inside a host program [R: 'Notepad++']
  - Markdown forms claimed (V13): callouts or admonitions [R: 'Text Callouts #141']; diagrams [R: 'Improved Mermaid Support #108']; markdown named, no form named [R: 'displaying rendered markdown HTML'] (b) not stated
  - Features the questions ask about: navigation V28: outline, contents or headings sidebar [R: 'Show Outline ... an outline of the document is displayed']; scroll position kept or synchronised [clipped] | links and images V30: shows local images [R: 'Fixed: Local relative path not working with img tag #84']; follows links to headings within the document [R: [clipped] | appearance V32: custom stylesheet [R: 'CSS File This allows you to select a CSS file']; undecidable (dark mode only) | print and export V33: export to PDF [R: 'Export to PDF']; export to HTML [R: 'can save rendered html to a file']; copy as rich text or HTML [R: 'Copies the [clipped]
- **Charges.** not stated (b) not stated (c) MIT license [R]
- **Buyer's all-in cost**, from the page text: price shape (V16b) not stated; beyond the price (V17): not stated; prerequisites (V11): host program named [R: 'Notepad++']; runtime or interpreter named [R: 'Prerequisites .NET 4.7.2 or higher'; 'WebView2 Edge (since 0.9.0) or an [clipped]; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): Windows.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): github-topics:markdown-viewer: stars=453; archived=false; last_push=2026-07-17
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** 2026-07-17 (release), day precision [R: 'Version 0.9.3 (released 2026-07-17)'] (b) not stated

## R64. Mud: Mark Up or Down

Slug `mud-mark-up-or-down`; profile `0-comparables/products/mud-mark-up-or-down.md`. Registered because: coded as reading without editing (V09: reader, editing not stated). Cells: Mac App Store.

- **Publishes about itself.**
  - Kind (V08): desktop application [B: 'A macOS app for viewing Markdown documents']; terminal program [A: 'excellent command-line tooling']
  - Reader or editor (V09): reader, editing not stated [A: 'A perfect Markdown viewer'; B: 'You just need a way to preview the Markdown you're writing']
  - Platforms (V10): macOS [A: 'Only for Mac'; 'Requires macOS 14.0 or later.']
  - Markdown forms claimed (V13): GitHub Flavored Markdown [A: 'GitHub-flavored']; syntax-highlighted code blocks [B]; front matter [B: 'Collapsible YAML frontmatter']; footnotes [B: 'Native popovers for footnotes']; diagrams [B: [clipped]
  - Features the questions ask about: navigation V28: outline, contents or headings sidebar [B: 'Table of contents — document outliner in sidebar']; folding of sections [B: 'Foldable [clipped] | find V29: undecidable | file changed elsewhere V31: reloads when the file changes on disk, stated [A: 'It automatically reloads the document when you save it'; B: 'Reload automatically every [clipped] | appearance V32: themes provided [B: 'Four color themes']; light and dark modes [B: 'Dark mode, Bright mode']; follows the system appearance, stated [B: [clipped] | print and export V33: print [B: 'Print and Open In Browser']; export to HTML [B: 'mud -u file.md # Render to HTML (mark-up view)']
- **Charges.** 'Free'; 'It's free and it's open source.' [A] (b) free (c) named open-source licence: 'MIT with Commons Clause' [B]
- **Buyer's all-in cost**, from the page text: price shape (V16b) free; beyond the price (V17): not stated; prerequisites (V11): minimum operating-system version named [A: 'Requires macOS 14.0 or later.']; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): macOS.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): Mac App Store: userRatingCount=0; averageUserRating=0
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** not stated

## R65. Offline Markdown Preview

Slug `offline-markdown-preview`; profile `0-comparables/products/offline-markdown-preview.md`. Registered because: coded as reading without editing (V09: reader, editing not stated). Cells: vscode.

- **Publishes about itself.**
  - Kind (V08): editor extension ("Visual Studio Code > Debuggers > Offline Markdown Preview"; "runs locally inside VS Code")
  - Reader or editor (V09): reader, editing not stated ("Markdown preview panel with live updates and editor/preview scroll sync.")
  - Platforms (V10): inside a host program ("runs locally inside VS Code")
  - Markdown forms claimed (V13): diagrams ("Mermaid diagrams") | math ("KaTeX math") | syntax-highlighted code blocks ("Prism syntax highlighting") ("Bundled rendering stack"); (b) shown as plain text, stated ("invalid Mermaid [clipped]
  - Features the questions ask about: navigation V28: outline, contents or headings sidebar ("Markdown outline TreeView") | jump to heading or section ("heading quick pick") | scroll position [clipped] | find V29: search within the document ("Cmd/Ctrl+F : open/focus preview search") | file changed elsewhere V31: undecidable ("Markdown preview panel with live updates"; text does not say what the updates follow) | print and export V33: export to HTML | export to PDF ("HTML export and PDF export from the preview workflow.") | files stay local V14: local, stated ("runs locally inside VS Code and the extension does not send your Markdown contents anywhere (no cloud, no telemetry).")
- **Charges.** 171,442 installs | ( 2 ) | Free | "Free : no paywalls; MIT-licensed."; (b) free; (c) named open-source licence ("License MIT License - see LICENSE .")
- **Buyer's all-in cost**, from the page text: price shape (V16b) free; beyond the price (V17): not stated; prerequisites (V11): host program named ("runs locally inside VS Code"); platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): none of the three named.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): vscode: installs=171391; ratings=2; average=5.00; lastUpdated=2026-07-12
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** Sun, 12 Jul 2026 15:53:57 GMT (day; version 0.4.0, page data); (b) not stated

## R66. OnePreview

Slug `onepreview`; profile `0-comparables/products/onepreview.md`. Registered because: coded as reading without editing (V09: reader, editing not stated). Cells: Mac App Store.

- **Publishes about itself.**
  - Kind (V08): other kind ("Finder Quick Look on macOS", site) | mobile application ("File viewer on iPhone and iPad", site)
  - Reader or editor (V09): reader, editing not stated ("Preview Markdown before opening an editor."; "switch between rendered Markdown and source")
  - Platforms (V10): iOS ("Requires iOS 17.0 or later") | iPadOS ("iPadOS 17.0") | macOS ("macOS 14.0 or later") (Compatibility)
  - Markdown forms claimed (V13): GitHub Flavored Markdown ("GitHub-style Markdown") | other named flavour ("MDX") | syntax-highlighted code blocks ("syntax highlighting") | diagrams ("Mermaid diagrams") | math ("KaTeX math"); (b) [clipped]
  - Features the questions ask about: appearance V32: undecidable ("Dark Interface", listed accessibility feature; names dark only, no light/dark pair, no choice stated) | files stay local V14: local, stated ("Processing is fast, local-first, and does not require an account."; "Documents opened in OnePreview are rendered locally on [clipped]
- **Charges.** Free (price line) | "Free app Available on the App Store."; (b) free; (c) not stated
- **Buyer's all-in cost**, from the page text: price shape (V16b) free; beyond the price (V17): not stated; prerequisites (V11): minimum operating-system version named ("Requires iOS 17.0 or later. ... macOS 14.0 or later."); platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): macOS.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): Mac App Store: userRatingCount=1; averageUserRating=5
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** 3d ago (relative date, no absolute date; "Version 1.4.2 3d ago"); other entries "Sep 7", "Sep 5", "Aug 19" without year; (b) not stated

## R67. pampi

Slug `pampi`; profile `0-comparables/products/pampi.md`. Registered because: coded as reading without editing (V09: reader, editing not stated). Cells: debian:apt-cache search markdown.

- **Publishes about itself.**
  - Kind (V08): desktop application (site section heading "GNU/Linux" under "Téléchargement et installation"; "PAMPI est un logiciel libre ... permettant de réaliser [clipped]
  - Reader or editor (V09): reader, editing not stated ("the Markdown file is displaied in the left side and on can view the result in the right side")
  - Platforms (V10): Linux (site section heading "GNU/Linux")
  - Markdown forms claimed (V13): math ("Maths can be authored with KaTeX."); (b) not stated
  - Features the questions ask about: print and export V33: export to HTML ("They are converted to web pages (HTML files) - one can view them with a browser - one can publish them online", apt-cache)
- **Charges.** PAMPI is a free software (apt-cache) | "PAMPI est un logiciel libre (licence GNU GPL 3)" (site); (b) undecidable ("free software" / "logiciel libre": text does not say whether free of charge or free as in freedom); (c) named open-source licence [clipped]
- **Buyer's all-in cost**, from the page text: price shape (V16b) undecidable; beyond the price (V17): not stated; prerequisites (V11): runtime or interpreter named ("Dépendances : Python 3 ... PyQt5 ... Pandoc un convertisseur de documents universel."; apt-cache "Depends: [clipped]; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): Linux.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): debian:apt-cache search markdown: not published by the list (no install count in apt-cache)
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** not stated; (b) not stated

## R68. Preview

Slug `preview`; profile `0-comparables/products/preview.md`. Registered because: coded as reading without editing (V09: reader, editing not stated); and top five in vscode by installs (5 of 19 eligible comparables with a figure; 787,184). Cells: vscode.

- **Publishes about itself.**
  - Kind (V08): editor extension ("Visual Studio Code > Programming Languages > Preview"; "An extension to preview ... in VSCode")
  - Reader or editor (V09): reader, editing not stated ("preview ... files ... while editing them in VSCode")
  - Platforms (V10): inside a host program ("in VSCode")
  - Markdown forms claimed (V13): markdown named, no form named ("A Previewer of Markdown, ReStructured Text, HTML, Jade, Pug, Mermaid files"); (b) not stated
  - Features the questions ask about: V28 to V33 and V14 all not stated
- **Charges.** 787,197 installs | ( 40 ) | Free; (b) free; (c) not stated
- **Buyer's all-in cost**, from the page text: price shape (V16b) free; beyond the price (V17): not stated; prerequisites (V11): host program named ("in VSCode"); platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): none of the three named.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): vscode: installs=787184; ratings=40; average=3.20; lastUpdated=2024-12-11
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** Wed, 11 Dec 2024 16:08:24 GMT (day; version 2.3.17, page data); (b) not stated

## R69. PreviewMarkdown

Slug `previewmarkdown`; profile `0-comparables/products/previewmarkdown.md`. Registered because: coded as reading without editing (V09: reader, editing not stated). Cells: Mac App Store.

- **Publishes about itself.**
  - Kind (V08): other kind ("Easy Markdown QuickLook previews and icon thumbnails."; "The app provides two app extensions: Markdown Previewer and Markdown [clipped]
  - Reader or editor (V09): reader, editing not stated ("select a Markdown file ... and press space - will pop up a rendered image of file", smittytone.net/previewmarkdown/)
  - Platforms (V10): macOS ("Only for Mac"; "Requires macOS 11.5 or later.")
  - Markdown forms claimed (V13): task lists ("[ ] [x] Checkboxes") | tables | front matter ("PreviewMarkdown will optionally preview YAML front matter") (listing feature list, site); (b) not stated
  - Features the questions ask about: appearance V32: font or size choice ("The base text size, from 10pt to 28pt. The primary text font and style.")
- **Charges.** $2.99 (price line); (b) undecidable ("$2.99" price line with no period, trial or tier text); (c) not stated
- **Buyer's all-in cost**, from the page text: price shape (V16b) undecidable; beyond the price (V17): not stated; prerequisites (V11): minimum operating-system version named ("Requires macOS 11.5 or later."); platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): macOS.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): Mac App Store: userRatingCount=0; averageUserRating=0
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** May 1 (year not published; "2.4.3 May 1", version history; "Latest Release: 2.4.3" site); (b) not stated

## R70. Print

Slug `print`; profile `0-comparables/products/print.md`. Registered because: coded as reading without editing (V09: reader, editing not stated). Cells: vscode.

- **Publishes about itself.**
  - Kind (V08): editor extension ("Visual Studio Code > Other > Print")
  - Reader or editor (V09): reader, editing not stated ("Print rendered Markdown."; editing happens in the host editor: "if you edit that file and stop making changes for three [clipped]
  - Platforms (V10): Windows | macOS | Linux ("Windows, Mac or Linux.") | inside a host program (VS Code)
  - Markdown forms claimed (V13): diagrams ("set up a local Kroki server and configure Print to use it", diagrams in hot preview); (b) not stated
  - Features the questions ask about: find V29: search within the document ("Hot preview also supports find-in-source.") | file changed elsewhere V31: undecidable ("if you edit that file and stop making changes for three seconds, the proview will update in the browser": edit is in the host [clipped] | print and export V33: print ("Print code. Print rendered Markdown."; "printing options like paper size, page orientation and margin size.")
- **Charges.** 740,428 installs | ( 55 ) | Free; (b) free; (c) not stated
- **Buyer's all-in cost**, from the page text: price shape (V16b) free; beyond the price (V17): not stated; prerequisites (V11): host program named ("VS Code can launch it"); platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): Linux, macOS, Windows.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): vscode: installs=740400; ratings=55; average=4.73; lastUpdated=2025-07-27
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** Sun, 27 Jul 2025 00:13:46 GMT (day; version 1.6.0, page data); (b) not stated

## R71. qlcommonmark

Slug `qlcommonmark`; profile `0-comparables/products/qlcommonmark.md`. Registered because: coded as reading without editing (V09: reader, editing not stated). Cells: homebrew:cask.

- **Publishes about itself.**
  - Kind (V08): other kind :: "QuickLook generator for beautifully rendering CommonMark documents on macOS" github.com
  - Reader or editor (V09): reader, editing not stated :: "QuickLook generator for CommonMark and Markdown files. It uses cmark to render the text" raw.githubusercontent.com
  - Platforms (V10): macOS :: "Requirements: macOS" formulae.brew.sh
  - Markdown forms claimed (V13): CommonMark :: "QuickLook generator for CommonMark and Markdown files" raw.githubusercontent.com; (b) not stated
  - Features the questions ask about: V28 to V33 and V14 all not stated
- **Charges.** not stated; (b) not stated; (c) named open-source licence :: MIT License (repository API field, spdx_id MIT) api.github.com
- **Buyer's all-in cost**, from the page text: price shape (V16b) not stated; beyond the price (V17): not stated; prerequisites (V11): not stated; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): macOS.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): homebrew:cask: 30d=not listed; 90d=7; 365d=98.  Further: Homebrew cask flagged disabled (N1).
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** 2017-07-23 (release v1.1, day) release list api.github.com; (b) archived, deprecated or unmaintained, stated :: "deprecated":true ; "qlcommonmark (disabled)" formulae.brew.sh

## R72. Quick Markdown Viewer

Slug `quick-markdown-viewer`; profile `0-comparables/products/quick-markdown-viewer.md`. Registered because: coded as reading without editing (V09: reader, editing not stated). Cells: Mac App Store.

- **Publishes about itself.**
  - Kind (V08): desktop application :: "for macOS, iPhone, and iPad" www.matthewpaulmoore.com ; undecidable (mobile application: iPhone/iPad named, rule has no [clipped]
  - Reader or editor (V09): reader, editing not stated :: "Read Markdown with native rendering" apps.apple.com
  - Platforms (V10): macOS :: "Requires macOS 13.0 or later." ; iOS :: "Requires iOS 16.0 or later." ; iPadOS :: "Requires iPadOS 16.0 or later." apps.apple.com
  - Markdown forms claimed (V13): tables ; diagrams :: "Render Mermaid diagrams natively" apps.apple.com; (b) not stated
  - Features the questions ask about: navigation V28: outline, contents or headings sidebar :: "Open a document outline" ; jump to heading or section :: "jump to headings" apps.apple.com | find V29: search within the document :: "Search the current document with Command-F" ; search across files or a folder :: "all open documents with [clipped] | links and images V30: shows remote images :: "View remote images and video links referenced in Markdown files." apps.apple.com | appearance V32: font or size choice :: "Adjust viewer font size for comfortable reading" apps.apple.com | print and export V33: print :: "Print the current document" apps.apple.com | files stay local V14: local, stated :: "Work entirely with files you choose from Finder or the Files app" www.matthewpaulmoore.com ; "local-first" apps.apple.com
- **Charges.** Free apps.apple.com; (b) free; (c) undecidable (see notes) :: "Free Markdown Viewer is also FOSS." www.matthewpaulmoore.com
- **Buyer's all-in cost**, from the page text: price shape (V16b) free; beyond the price (V17): not stated; prerequisites (V11): minimum operating-system version named :: "Requires macOS 13.0 or later." ; build toolchain named :: "full Xcode installed - `xcodebuild`, `swift`" ; [clipped]; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): macOS.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): Mac App Store: userRatingCount=1; averageUserRating=5
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** 1.7 Jun 15 (month and day, no year; version history) apps.apple.com; (b) not stated

## R73. Read.md

Slug `read-md`; profile `0-comparables/products/read-md.md`. Registered because: coded as reading without editing (V09: reader, stated read-only); and top five in Mac App Store by rating count (5 of 134 eligible comparables with a figure, 36 of them non-zero; 84). Cells: Mac App Store.

- **Publishes about itself.**
  - Kind (V08): desktop application :: "Native on Mac — instant, offline, built for macOS." read-md.app ; service :: "in your browser" read-md.app ; undecidable [clipped]
  - Reader or editor (V09): reader, stated read-only :: "Not an editor, not a note-taking app, not a vault system. A reader." apps.apple.com
  - Platforms (V10): iOS ; iPadOS ; macOS ; Android :: "Open any .md file on iPhone, iPad, Android, or Mac." read-md.app
  - Markdown forms claimed (V13): tables ; task lists ; syntax-highlighted code blocks :: "Syntax highlighting for 180+ programming languages" ; GitHub Flavored Markdown :: "GitHub Flavored Markdown fully supported" ; diagrams :: [clipped]
  - Features the questions ask about: navigation V28: outline, contents or headings sidebar :: "Auto-generated table of contents from your headings." ; scroll position kept or synchronised :: [clipped] | find V29: search within the document :: "Search within any document with match highlighting" apps.apple.com | appearance V32: light and dark modes :: "DARK AND LIGHT MODES" ; themes provided :: "Switch between dark and light themes" ; follows the system appearance, [clipped] | print and export V33: print :: "Share it, print it, archive it." ; export to PDF ; export to HTML ; export to another named format :: "real Word (.docx) file"; [clipped] | files stay local V14: local, stated :: "file contents are never uploaded, and reading works fully offline" apps.apple.com
- **Charges.** Free · In‑App Purchases ; "Read.md Pro Yearly $9.99" ; "Read.md Pro (Lifetime) $24.99" ; "Free to read — forever." apps.apple.com read-md.app; (b) free with paid tier or features ; one-time purchase :: "A one-time purchase" ; subscription :: "a [clipped]
- **Buyer's all-in cost**, from the page text: price shape (V16b) free with paid tier or features, one-time purchase, subscription, free trial, then paid; beyond the price (V17): own API key or service account required, stated :: "Sign in with a personal access token; your token stays on your device. (Read.md Pro)" [clipped]; prerequisites (V11): minimum operating-system version named :: "Requires iOS 15.0 or later." ; "Requires macOS 13.0 or later." apps.apple.com; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): macOS.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): Mac App Store: userRatingCount=84; averageUserRating=4.96429.  Further: Mac App Store: Pavel Abin, 84 ratings, average 4.96, first released 2026-03-25, current version 2026-10-05 (N6). The one entry in the store's top eleven described as a reader by name (N6).
- **Whom its pages address (V05):** Readers of what AI agents write :: "WHAT PEOPLE USE IT FOR: Reading AI-generated markdown exports." apps.apple.com
- **Last release and maintenance (V27):** 1.3.0 3d ago (relative, version history) apps.apple.com; (b) not stated

## R74. reveal-md

Slug `reveal-md`; profile `0-comparables/products/reveal-md.md`. Registered because: coded as reading without editing (V09: reader, editing not stated). Cells: homebrew:formula.

- **Publishes about itself.**
  - Kind (V08): undecidable (see notes) :: "reveal-md slides.md" raw.githubusercontent.com
  - Reader or editor (V09): reader, editing not stated :: "opens any Markdown file as a reveal.js presentation" raw.githubusercontent.com
  - Platforms (V10): macOS ; Linux :: "Bottle (binary package) installation support provided for: macOS on Apple Silicon ... Linux ARM64" formulae.brew.sh
  - Markdown forms claimed (V13): syntax-highlighted code blocks :: "Syntax highlighting" ; front matter :: "YAML Front matter" raw.githubusercontent.com; (b) not stated
  - Features the questions ask about: file changed elsewhere V31: reloads when the file changes on disk, stated :: "changes to markdown files will trigger the browser to reload" raw.githubusercontent.com | appearance V32: themes provided :: "Theme"; "Highlight Theme" ; custom stylesheet :: "Custom CSS" raw.githubusercontent.com | print and export V33: print :: "Print to PDF: reveal-md slides.md --print slides.pdf" ; export to PDF :: "The PDF is generated using Puppeteer." ; export to HTML [clipped]
- **Charges.** not stated; (b) not stated; (c) named open-source licence :: "License: MIT" formulae.brew.sh
- **Buyer's all-in cost**, from the page text: price shape (V16b) not stated; beyond the price (V17): not stated; prerequisites (V11): runtime or interpreter named :: dependency "node"; "You can use Docker to run this tool without needing Node.js installed on your machine." [clipped]; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): Linux, macOS.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): homebrew:formula: 30d=1; 90d=37; 365d=220
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** 2024-11-27 (release 6.1.4, day) releases API; (b) archived, deprecated or unmaintained, stated :: "reveal-md is no longer in active development." raw.githubusercontent.com

## R75. richardr1126/openreader

Slug `richardr1126-openreader`; profile `0-comparables/products/richardr1126-openreader.md`. Registered because: coded as reading without editing (V09: reader, editing not stated); and top five in github-topics:markdown-reader by stars (1 of 5 eligible comparables with a figure; 539). Cells: github-topics:markdown-reader.

- **Publishes about itself.**
  - Kind (V08): undecidable (see notes) :: "open-source, self-host-friendly text-to-speech document reader built with Next.js" raw.githubusercontent.com
  - Reader or editor (V09): reader, editing not stated :: "text-to-speech document reader" raw.githubusercontent.com
  - Platforms (V10): not stated
  - Markdown forms claimed (V13): markdown named, no form named :: "Five readable formats — synchronized EPUB, PDF, TXT, MD, and worker-converted DOCX" raw.githubusercontent.com; (b) not stated
  - Features the questions ask about: print and export V33: export to another named format :: "Audiobook export in M4B or MP3" raw.githubusercontent.com
- **Charges.** not stated; (b) not stated; (c) named open-source licence :: "MIT. See LICENSE." raw.githubusercontent.com
- **Buyer's all-in cost**, from the page text: price shape (V16b) not stated; beyond the price (V17): not stated; prerequisites (V11): not stated; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): none of the three named.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): github-topics:markdown-reader: stars=539; archived=false; last_push=2026-10-08
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** 2026-09-30 (release v5.1.0, day) releases API; (b) not stated

## R76. RivoLink/leaf

Slug `rivolink-leaf`; profile `0-comparables/products/rivolink-leaf.md`. Registered because: coded as reading without editing (V09: reader, editing not stated). Cells: github-topics:markdown-viewer; homebrew:formula; Snap Store.

- **Publishes about itself.**
  - Kind (V08): terminal program :: "A terminal-based Markdown previewer with a GUI-like experience." leaf.rivolink.mg
  - Reader or editor (V09): reader, editing not stated :: "Terminal Markdown previewer" raw.githubusercontent.com
  - Platforms (V10): macOS ; Linux ; Windows ; Android :: "leaf runs on macOS (Intel & Apple Silicon), Linux (x64 & ARM), Windows, and Android via Termux." [clipped]
  - Markdown forms claimed (V13): syntax-highlighted code blocks :: "syntax coloring for 40+ languages" ; tables :: "Markdown tables rendered with Unicode box-drawing borders" ; math :: "LaTeX math" ; diagrams :: "Mermaid diagrams" [clipped]
  - Features the questions ask about: navigation V28: outline, contents or headings sidebar :: "Sidebar TOC with heading hierarchy" ; jump to heading or section :: "jump with 1-9" ; scroll [clipped] | find V29: search within the document :: "Press / to search. Matches are highlighted with a counter." leaf.rivolink.mg | file changed elsewhere V31: reloads when the file changes on disk, stated :: "Auto-reload when the file changes on disk." leaf.rivolink.mg | appearance V32: themes provided :: "4 built-in themes: Arctic, Forest, Ocean, Solarized-Dark." leaf.rivolink.mg | print and export V33: export to another named format :: "leaf --inline plain README.md"; "leaf --inline ansi README.md" raw.githubusercontent.com
- **Charges.** not stated; (b) not stated; (c) named open-source licence :: "MIT License" raw.githubusercontent.com
- **Buyer's all-in cost**, from the page text: price shape (V16b) not stated; beyond the price (V17): not stated; prerequisites (V11): not stated; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): Linux, macOS, Windows.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): github-topics:markdown-viewer: stars=2121; archived=false; last_push=2026-09-28 || homebrew:formula: 30d=431; 90d=1,244; 365d=1,244 || Snap Store: none given by API (find returns no install, rating or download counts).  Further: Homebrew entry first appears inside the last year (365d count equals 90d count); growth 4.16 (N1).
- **Whom its pages address (V05):** Developers and coders :: "Designed for developers, CLI users, and AI-assisted workflows." ; Terminal readers :: "CLI users" leaf.rivolink.mg
- **Last release and maintenance (V27):** 2026-09-28 (release 1.28.3, day) releases API; (b) not stated

## R77. selimacerbas/mdkite.nvim

Slug `selimacerbas-mdkite-nvim`; profile `0-comparables/products/selimacerbas-mdkite-nvim.md`. Registered because: coded as reading without editing (V09: reader, editing not stated); and top five in github-topics:markdown-preview by stars (4 of 5 eligible comparables with a figure; 227). Cells: github-topics:markdown-preview.

- **Publishes about itself.**
  - Kind (V08): editor extension ["Live Markdown preview for Neovim" ; topic "neovim-plugin" | repo fields/readme]
  - Reader or editor (V09): reader, editing not stated ["Edit freely: the browser updates instantly as you type" (editing happens in Neovim) | readme]
  - Platforms (V10): macOS ["On macOS, string values are passed via `open -a <name>`." | readme] ; Windows [heading "WSL: browser doesn't open, or preview unreachable [clipped]
  - Markdown forms claimed (V13): tables ["headings, tables, code blocks, everything" | readme] ; syntax-highlighted code blocks [repo description "syntax highlighting"] ; math ["LaTeX math: inline `$...$` and display `$$...$$` [clipped]
  - Features the questions ask about: navigation V28: scroll position kept or synchronised ["Scroll sync: browser follows your cursor position with line-level precision" | readme] | links and images V30: shows local images ["Relative images work: `![](pic.png)` next to your `.md` file renders in the preview" | readme] | file changed elsewhere V31: undecidable ["auto_refresh = true, -- auto-update on buffer changes" (preview updates as you type inside Neovim) AND "Force refresh: [clipped] | appearance V32: light and dark modes ["Dark / Light theme toggle" | readme] ; custom stylesheet ["custom_css = \"\", -- CSS file layered over bundled [clipped] | print and export V33: export to another named format ["SVG export" (diagram overlay only) | readme] | files stay local V14: undecidable ["Local by default. The preview server binds to `127.0.0.1`." | readme Security]: sentence is about the preview server's [clipped]
- **Charges.** not stated; (b) not stated; (c) named open-source licence: MIT [repository license field | api.github.com/repos/selimacerbas/mdkite.nvim]
- **Buyer's all-in cost**, from the page text: price shape (V16b) not stated; beyond the price (V17): not stated; prerequisites (V11): none needed, stated ["No prereqs. No `npm install`." ; "Zero external dependencies: no npm, no Node.js, just Neovim + your browser" | readme] ; host [clipped]; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): macOS, Windows.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): github-topics:markdown-preview: stars=227; archived=false; last_push=2026-10-02
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** 2026-10-02 (release v2.1.0; day) [releases list]; (b) not stated

## R78. shd101wyy/markdown-preview-enhanced

Slug `shd101wyy-markdown-preview-enhanced`; profile `0-comparables/products/shd101wyy-markdown-preview-enhanced.md`. Registered because: coded as reading without editing (V09: reader, editing not stated). Cells: github-topics:markdown-editor.

- **Publishes about itself.**
  - Kind (V08): editor extension ["Markdown Preview Enhanced is an extension" | api.github.com/repos/shd101wyy/markdown-preview-enhanced/readme]
  - Reader or editor (V09): reader, editing not stated ["Toggle preview" ; "Sync preview / Sync source" | readme]
  - Platforms (V10): Windows ["The cmd key for Windows is ctrl." | api.github.com/repos/shd101wyy/markdown-preview-enhanced/readme] ; inside a host program [repo [clipped]
  - Markdown forms claimed (V13): math ["math typesetting" | api.github.com/repos/shd101wyy/markdown-preview-enhanced/readme] ; diagrams ["mermaid, PlantUML" | api.github.com/repos/shd101wyy/markdown-preview-enhanced/readme]; (b) not [clipped]
  - Features the questions ask about: navigation V28: outline, contents or headings sidebar ["esc: Toggle sidebar TOC" | readme] ; scroll position kept or synchronised ["automatic scroll sync" [clipped] | print and export V33: export to PDF ["PDF export" | readme]
- **Charges.** not stated; (b) not stated; (c) named open-source licence: University of Illinois/NCSA Open Source License ["released under the University of Illinois/NCSA Open Source License" | api.github.com/repos/shd101wyy/markdown-preview-enhanced/readme]
- **Buyer's all-in cost**, from the page text: price shape (V16b) not stated; beyond the price (V17): not stated; prerequisites (V11): host program named [repo description "extension for Atom editor"]; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): Windows.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): github-topics:markdown-editor: stars=4442; archived=false; last_push=2026-10-09
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** 2015-08-28 (release 0.3.7; day) [releases list]; (b) not stated

## R79. shiba

Slug `shiba`; profile `0-comparables/products/shiba.md`. Registered because: coded as reading without editing (V09: reader, editing not stated). Cells: homebrew:cask.

- **Publishes about itself.**
  - Kind (V08): terminal program ["Both CLI and GUI friendly" | README] ; desktop application ["installable desktop application" | README]
  - Reader or editor (V09): reader, editing not stated ["a simple Markdown browser to preview documents with your favorite text editor" | README]
  - Platforms (V10): macOS ["Requirements: macOS" | cask page] ; Windows [".msi file is a Windows installer" | docs/installation.md] ; Linux ["Cross platform; macOS, [clipped]
  - Markdown forms claimed (V13): GitHub Flavored Markdown ["GitHub-flavored Markdown support" | README] ; tables ["Table" | README] ; math ["Math expressions with Mathjax" | README] ; diagrams ["Diagrams with mermaid.js" | README]; [clipped]
  - Features the questions ask about: navigation V28: outline, contents or headings sidebar ["Sections outline in side navigation bar highlighting the current section" | README] ; jump to [clipped] | find V29: undecidable ["search text" in README keyboard-shortcuts list]: scope not named, sentence not about the open document | file changed elsewhere V31: reloads when the file changes on disk, stated ["Watch the files or directories and automatically update the preview efficiently using [clipped] | appearance V32: custom stylesheet ["Customizable with a YAML config file (color theme, keyboard shortcuts, custom CSS, ...)" | README]
- **Charges.** not stated; (b) not stated; (c) named open-source licence: MIT ["This software is distributed under the MIT license." | README ; license field "MIT"]
- **Buyer's all-in cost**, from the page text: price shape (V16b) not stated; beyond the price (V17): not stated; prerequisites (V11): runtime or interpreter named ["Install Rosetta 2 with softwareupdate --install-rosetta --agree-to-license." | cask page ; "On Linux, Shiba uses [clipped]; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): Linux, macOS, Windows.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): homebrew:cask: 30d=1; 90d=1; 365d=26.  Further: GitHub rhysd/Shiba: not archived; last push 2026-07-20; newest release v2.0.0-alpha.4 on 2026-03-28; 5 releases in the last 365 days, 743 downloads (N5). Homebrew cask flagged disabled (N1).
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** 2026-03-28 (release v2.0.0-alpha.4; day) [releases list]; (b) undecidable [cask page heading "shiba (disabled)"]: 'disabled' is not one of the rule's words (archived, deprecated, unmaintained) and the page gives no meaning for it

## R80. simov/markdown-viewer

Slug `simov-markdown-viewer`; profile `0-comparables/products/simov-markdown-viewer.md`. Registered because: coded as reading without editing (V09: reader, editing not stated). Cells: github-topics:markdown-viewer.

- **Publishes about itself.**
  - Kind (V08): browser extension ["Markdown Viewer / Browser Extension" | api.github.com/repos/simov/markdown-viewer/readme]
  - Reader or editor (V09): reader, editing not stated ["Raw and rendered markdown views" | api.github.com/repos/simov/markdown-viewer/readme]
  - Platforms (V10): inside a host program ["The following instructions applies for: Chrome, Edge, Opera, Brave, Chromium and Vivaldi." | [clipped]
  - Markdown forms claimed (V13): CommonMark ["Full CommonMark support"] ; GitHub Flavored Markdown ["GitHub Flavored Markdown (GFM)"] ; tables ["GFM tables"] ; task lists ["tasklists"] ; footnotes ["footnote"] ; math ["MathJax [clipped]
  - Features the questions ask about: navigation V28: outline, contents or headings sidebar ["Table of Contents (ToC)"] ; scroll position kept or synchronised ["Remember scroll position"] | file changed elsewhere V31: reloads when the file changes on disk, stated ["Auto reload on file change" (default off)] | appearance V32: themes provided ["30+ Themes (cleanrmd, GitHub)"] ; light and dark modes ["Dark Mode" | Chrome Web Store] ; undecidable for "Custom theme [clipped]
- **Charges.** Free and Open Source [README]; (b) free ["Free and Open Source"]; (c) named open-source licence: The MIT License (MIT) [README ; license field MIT]
- **Buyer's all-in cost**, from the page text: price shape (V16b) free; beyond the price (V17): not stated; prerequisites (V11): host program named ["Install: Chrome / Firefox / Edge / Opera / Brave / Chromium / Vivaldi" | api.github.com/repos/simov/markdown-viewer/readme]; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): none of the three named.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): github-topics:markdown-viewer: stars=1702; archived=false; last_push=2025-12-29
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** May 2, 2024 (Chrome Web Store 'Version 5.3 Updated May 2, 2024'; day); (b) not stated

## R81. telari

Slug `telari`; profile `0-comparables/products/telari.md`. Registered because: coded as reading without editing (V09: reader, editing not stated). Cells: homebrew:cask.

- **Publishes about itself.**
  - Kind (V08): desktop application [“Telari is a macOS Markdown reader built for typography” telari.app]
  - Reader or editor (V09): reader, editing not stated [“Telari is a local Markdown reader.” telari.app/privacy/]
  - Platforms (V10): macOS [“macOS 13+” telari.app]; iOS [“iOS / iPadOS versions are sold separately.” telari.app/pricing]; iPadOS [same]
  - Markdown forms claimed (V13): math [“TEX-grade math rendering” telari.app]; diagrams [“Mermaid diagrams” telari.app/pricing]; tables [“Tables are now three-rule (booktabs) tables” telari.app/changelog]; footnotes [“A little space [clipped]
  - Features the questions ask about: appearance V32: themes provided [“Eight ship with the app” telari.app/changelog v0.6.0]; font or size choice [“Curated font presets + deep settings” [clipped] | print and export V33: export to PDF [“Basic export to PDF or images” telari.app/pricing]; export to another named format [“images” same quote] | files stay local V14: local, stated [“Your documents never leave your Mac.” telari.app/privacy/]
- **Charges.** “Telari is free forever.”; “Free $0 Free forever”; “Pro licence $20 One-time purchase · 5 devices”; “one purchase, yours forever, updates for life” [telari.app/pricing]; “Telari is paid software — free during the public beta. The release version [clipped]
- **Buyer's all-in cost**, from the page text: price shape (V16b) free with paid tier or features, one-time purchase, free trial, then paid; beyond the price (V17): not stated; prerequisites (V11): minimum operating-system version named [“Requirements: macOS >= 13” formulae.brew.sh]; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): macOS.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): homebrew:cask: 30d=14; 90d=14; 365d=14
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** “October 4, 2026” (day; changelog heading “v0.6.2 October 4, 2026”); (b) not stated

## R82. Textualize/frogmouth

Slug `textualize-frogmouth`; profile `0-comparables/products/textualize-frogmouth.md`. Registered because: coded as reading without editing (V09: reader, editing not stated); and top five in github-topics:markdown-viewer by stars (4 of 21 eligible comparables with a figure; 3,307). Cells: github-topics:markdown-viewer.

- **Publishes about itself.**
  - Kind (V08): terminal program [“Frogmouth is a Markdown viewer / browser for your terminal” README]
  - Reader or editor (V09): reader, editing not stated [“Markdown viewer / browser” README]
  - Platforms (V10): Linux [“Frogmouth runs on Linux, macOS, and Windows.” README Compatibility]; macOS [same]; Windows [same]
  - Markdown forms claimed (V13): markdown named, no form named [“Frogmouth can open *.md files locally or via a URL.” README]; (b) not stated
  - Features the questions ask about: navigation V28: outline, contents or headings sidebar [“table of contents” README; inserted or sidebar not stated]; bookmarks [“bookmarks” README]
- **Charges.** not stated; (b) not stated; (c) named open-source licence: “MIT license” [github.com licence field and README header]
- **Buyer's all-in cost**, from the page text: price shape (V16b) not stated; beyond the price (V17): not stated; prerequisites (V11): runtime or interpreter named [“Frogmouth requires Python 3.8 or above.” README]; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): Linux, macOS, Windows.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): github-topics:markdown-viewer: stars=3307; archived=false; last_push=2024-08-01.  Further: PyPI frogmouth 1,232 downloads last month, last release 0.9.2 on 2023-11-28 (N4). GitHub Textualize/frogmouth: not archived; last push 2024-08-01; newest release v0.9.1 2023-11-02, none in the last 365 days (N5).
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** not stated; (b) not stated

## R83. ttscoff-mmd-quicklook

Slug `ttscoff-mmd-quicklook`; profile `0-comparables/products/ttscoff-mmd-quicklook.md`. Registered because: coded as reading without editing (V09: reader, editing not stated). Cells: homebrew:cask.

- **Publishes about itself.**
  - Kind (V08): other kind [“Quick Look plugin for viewing MultiMarkdown” formulae.brew.sh: extension to the macOS Quick Look facility]
  - Reader or editor (V09): reader, editing not stated [“Quick Look plugin for viewing MultiMarkdown” formulae.brew.sh]
  - Platforms (V10): macOS [“Requirements: macOS” formulae.brew.sh]
  - Markdown forms claimed (V13): other named flavour [“Quick Look plugin for viewing MultiMarkdown” formulae.brew.sh; “Improved QuickLook generator for MultiMarkdown files” github.com description]; (b) not stated
  - Features the questions ask about: appearance V32: themes provided [“Ready-made styles: A couple of default styles lifted from Marked.app. Swiss ... Upstanding Citizen” README]; custom [clipped]
- **Charges.** not stated; (b) not stated; (c) not stated
- **Buyer's all-in cost**, from the page text: price shape (V16b) not stated; beyond the price (V17): not stated; prerequisites (V11): host program named [“Quick Look plugin for viewing MultiMarkdown” formulae.brew.sh; the requirement is implied by “plugin”, no requirement sentence]; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): macOS.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): homebrew:cask: 30d=not listed; 90d=7; 365d=43.  Further: Homebrew cask flagged disabled (N1).
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** not stated [“Current version: 1.2”, no dates]; (b) undecidable [“ttscoff-mmd-quicklook (disabled)” formulae.brew.sh: “disabled” is not archived, deprecated or unmaintained and the rule gives no other word]

## R84. ViewMD

Slug `viewmd`; profile `0-comparables/products/viewmd.md`. Registered because: coded as reading without editing (V09: reader, stated read-only). Cells: Mac App Store.

- **Publishes about itself.**
  - Kind (V08): desktop application ("Requires macOS 13.0 or later. Mac", apps.apple.com); mobile application: undecidable (iPad named in "opens Markdown files on [clipped]
  - Reader or editor (V09): reader, stated read-only ("No editor mode.", apps.apple.com)
  - Platforms (V10): iPadOS ("Requires iPadOS 16.0 or later. iPad", apps.apple.com); macOS ("Requires macOS 13.0 or later. Mac", apps.apple.com)
  - Markdown forms claimed (V13): (a) diagrams ("Mermaid and GraphViz diagrams"); math ("KaTeX and MathJax equations"); syntax-highlighted code blocks ("Syntax-highlighted code blocks"); tables ("Tables, including wide and complex [clipped]
  - Features the questions ask about: navigation V28: outline, contents or headings sidebar ("Table of contents", apps.apple.com); jump to heading or section ("return from Table of Contents [clipped] | find V29: search within the document ("in-document search", apps.apple.com) | links and images V30: follows links to headings within the document ("Links to sections within a document now work", apps.apple.com); "working file links" [clipped] | appearance V32: themes provided ("Light, dark, sepia, Solarized, and high-contrast themes", apps.apple.com); light and dark modes (same quote) | print and export V33: export to PDF; export to HTML; print ("PDF and HTML export, plus printing via AirPrint", apps.apple.com) | files stay local V14: local, stated ("Everything runs locally on your iPad.", apps.apple.com)
- **Charges.** (a) "$5.99" (apps.apple.com, price field); "ViewMD is a one-time purchase." (b) one-time purchase (c) not stated
- **Buyer's all-in cost**, from the page text: price shape (V16b) one-time purchase; beyond the price (V17): not stated; prerequisites (V11): minimum operating-system version named ("Requires iPadOS 16.0 or later", "macOS 13.0 or later", apps.apple.com); platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): macOS.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): Mac App Store: userRatingCount=0; averageUserRating=0
- **Whom its pages address (V05):** Developers and coders ("Developers reading READMEs and pull-request notes on the go", apps.apple.com); Writers and authors ("Technical writers doing final-pass quality checks", apps.apple.com); [clipped]
- **Last release and maintenance (V27):** (a) "Jul 12" with version 1.31 (day and month; year not printed) (apps.apple.com, Version History) (b) not stated

## R85. vmd

Slug `vmd`; profile `0-comparables/products/vmd.md`. Registered because: coded as reading without editing (V09: reader, editing not stated). Cells: alternativeto:Marked (AlternativeTo entry for Marked).

- **Publishes about itself.**
  - Kind (V08): desktop application (AlternativeTo "Platforms: Mac, Windows, Linux, BSD, npm", alternativeto.net, alternativeto.net; "Cmd+F on OS X", github.com)
  - Reader or editor (V09): reader, editing not stated ("Preview markdown files in a separate window.", github.com)
  - Platforms (V10): Windows ("Windows"); macOS ("Mac"; "Cmd+F on OS X", github.com); Linux ("Linux"); BSD ("BSD") (alternativeto.net, AlternativeTo labels)
  - Markdown forms claimed (V13): (a) GitHub Flavored Markdown ("GitHub style: The markdown content is rendered as close to the way it's rendered on GitHub as possible.", github.com); task lists ("Checklists: Renders GitHub-style [clipped]
  - Features the questions ask about: navigation V28: jump to heading or section ("Navigate within linked sections in a document", github.com) | find V29: search within the document ("Search in page: Search within your markdown file and scroll to the results.", github.com) | links and images V30: follows links to other markdown files inside the product ("open relative links to other documents in the same window or in a new one [clipped] | file changed elsewhere V31: reloads when the file changes on disk, stated ("Local files opened in vmd are watched for changes and the viewer will automatically update [clipped] | appearance V32: themes provided ("Select different themes", github.com); custom stylesheet ("provide your own styles", github.com); font or size choice [clipped]
- **Charges.** (a) "Free product." (alternativeto.net); "Free" (alternativeto.net) (b) free (c) named open-source licence: "MIT" (github.com, License section and licence field)
- **Buyer's all-in cost**, from the page text: price shape (V16b) free; beyond the price (V17): not stated; prerequisites (V11): not stated ("$ npm install -g vmd", github.com, is the install line; npm is not stated as required); platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): Linux, macOS, Windows.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): alternativeto:Marked (AlternativeTo entry for Marked): rank=72; page=6; Like; alternatives-listed-for-this-entry=not shown; license=Free Open Source (MIT) Platforms Mac Windows Linux BSD npm Good alternative? Is vmd a good [clipped]
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** (a) "Apr 7, 2021" ("this page was last updated Apr 7, 2021.", alternativeto.net, listing update); AlternativeTo GitHub section "Updated Dec 18, 2019" is earlier (b) not stated

## R86. zerdo

Slug `zerdo`; profile `0-comparables/products/zerdo.md`. Registered because: coded as reading without editing (V09: reader, stated read-only). Cells: alternativeto:Typora.

- **Publishes about itself.**
  - Kind (V08): desktop application ("Zerdo is a desktop Markdown to PDF tool for Windows.", zerdo.swaswas.com)
  - Reader or editor (V09): reader, stated read-only ("Is Zerdo a Markdown editor? No.", zerdo.swaswas.com)
  - Platforms (V10): Windows ("Zerdo is currently available for Windows desktop systems.", zerdo.swaswas.com; "Windows 10 or later", github.com)
  - Markdown forms claimed (V13): (a) GitHub Flavored Markdown ("GitHub-style Markdown rendering", github.com); syntax-highlighted code blocks ("Syntax-highlighted code blocks", github.com); tables ("Clean tables and lists", [clipped]
  - Features the questions ask about: navigation V28: outline, contents or headings sidebar ("Automatic Table of Contents (TOC)", github.com; placed in the output, noted as inserted) | print and export V33: export to PDF ("Open a Markdown file. Export to PDF.", github.com; "PDF-first rendering focused on final output quality", zerdo.swaswas.com) | files stay local V14: local, stated ("All processing happens locally on your Windows system. No internet connection or cloud uploads required.", [clipped]
- **Charges.** (a) "Free to use, with optional licensed features"; "Early Supporter License ₹199 Available for the first 100 days. After that, the price will increase to ₹999."; "One time purchase (perpetual license) ranging between $2 and $10 + free version with [clipped]
- **Buyer's all-in cost**, from the page text: price shape (V16b) free with paid tier or features, one-time purchase; beyond the price (V17): not stated; prerequisites (V11): none needed, stated ("Zerdo works standalone without requiring LaTeX, Pandoc, or any additional dependencies.", zerdo.swaswas.com); minimum [clipped]; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): Windows.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): alternativeto:Typora: rank=111; page=10; Like; alternatives-listed-for-this-entry=not shown; license=Freemium Proprietary Origin India Platforms Windows Good alternative? Is zerdo a good [clipped]
- **Whom its pages address (V05):** Writers and authors ("Technical authors writing long Markdown documents"; "Writers who need emoji support in their PDFs"; "for authors who care about final output", zerdo.swaswas.com); Developers and [clipped]
- **Last release and maintenance (V27):** (a) "Jan 11, 2026" ("this page was last updated Jan 11, 2026.", alternativeto.net, listing update); "© 2026 Zerdo" is a copyright year (b) not stated

## R87. alexishida/Moji

Slug `alexishida-moji`; profile `0-comparables/products/alexishida-moji.md`. Registered because: top five in github-topics:markdown-reader by stars (2 of 5 eligible comparables with a figure; 493). Cells: github-topics:markdown-viewer; github-topics:markdown-editor; github-topics:markdown-reader.

- **Publishes about itself.**
  - Kind (V08): desktop application ("A lightweight, clean desktop app for opening, reading, editing, and exporting Markdown files.", raw.githubusercontent.com)
  - Reader or editor (V09): editor with rendered view ("Live preview: while editing, toggle a resizable split view ... to keep the rendered preview beside the source editor", [clipped]
  - Platforms (V10): Windows; macOS; Linux ("Official installers for Windows, macOS and Linux", alexishida.com)
  - Markdown forms claimed (V13): tables; task lists; footnotes; math ("LaTeX math via KaTeX"); diagrams ("renders as a responsive diagram, including flowcharts, sequence, Gantt, class, ER, state, and journey diagrams"); [clipped]
  - Features the questions ask about: navigation V28: outline, contents or headings sidebar ("Outline navigation: collapsible heading tree"); jump to heading or section ("clicking any heading [clipped] | find V29: search within the document ("top-bar search finds visible Markdown text"); find and replace ("replace-one/replace-all controls") [clipped] | links and images V30: opens web links in the browser ("external links opened in the OS browser"); shows local images ("images referenced relative to the document [clipped] | file changed elsewhere V31: preview updates as you type inside the product, stated ("Live preview: while editing ...", raw.githubusercontent.com) | appearance V32: light and dark modes ("dark/light toggle for rendered Markdown"); themes provided ("Markdown themes: dark/light toggle"); font or size [clipped] | print and export V33: export to HTML; export to PDF; export to another named format ("PNG") ("export the active document as HTML, PDF, or PNG", [clipped]
- **Charges.** Free · open source · no account; "Moji is free and distributed under the MIT license." (alexishida.com); (b) free; (c) named open-source licence: "MIT license" (alexishida.com); "MIT © Alex Ishida" (raw.githubusercontent.com)
- **Buyer's all-in cost**, from the page text: price shape (V16b) free; beyond the price (V17): not stated; prerequisites (V11): none needed, stated ("Windows and Linux install from the downloads above with no extra steps.", raw.githubusercontent.com); runtime or interpreter [clipped]; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): Linux, macOS, Windows.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): github-topics:markdown-viewer: stars=493; archived=false; last_push=2026-09-11 || github-topics:markdown-editor: stars=493; archived=false; last_push=2026-09-11 || github-topics:markdown-reader: stars=493; archived=false; last_push=2026-09-11
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** not stated; (b) not stated

## R88. Apostrophe

Slug `apostrophe`; profile `0-comparables/products/apostrophe.md`. Registered because: top five in Flathub by installs last month (1 of 25 eligible comparables with a figure; 5,267). Cells: alternativeto:Typora; debian:apt-cache search markdown; Flathub.

- **Publishes about itself.**
  - Kind (V08): desktop application ("Apostrophe is a simple GNU/Linux Markdown editor built with the GTK+ framework.", AlternativeTo extract; "GTK based distraction [clipped]
  - Reader or editor (V09): editor with rendered view ("Live preview of what you write", flathub.org; "The preview lets you see a live rendered version of your document", [clipped]
  - Platforms (V10): Linux ("GNU/Linux", AlternativeTo extract; "Linux", apps.gnome.org)
  - Markdown forms claimed (V13): tables ("Inserting a table with the help of the toolbar", apps.gnome.org caption); math ("show formulas in the inline preview", flathub.org add-on); (b) not stated
  - Features the questions ask about: file changed elsewhere V31: preview updates as you type inside the product, stated ("Live preview of what you write", flathub.org) | appearance V32: themes provided ("Dark, light and sepia themes", flathub.org); light and dark modes ("Dark, light and sepia themes") | print and export V33: export to PDF; export to another named format ("Export to all kind of formats: PDF, Word/Libreoffice, LaTeX, or even HTML slideshows") [clipped]
- **Charges.** Free (flathub.org); "Open Source (GPL-3.0) and Free product." (AlternativeTo extract); (b) free; donation or sponsorship invited, use free ("Donate", flathub.org; "donation":"www.paypal.me", flathub.org); (c) named open-source licence: "GPL-3.0 [clipped]
- **Buyer's all-in cost**, from the page text: price shape (V16b) free, donation or sponsorship invited, use free, "donation":"https://www.paypal.me/manuelgenoves", https://flathub.org/api/v2/appstream/org.; beyond the price (V17): not stated; prerequisites (V11): build toolchain named ("Build system: `meson ninja-build`", raw.githubusercontent.com); runtime or interpreter named ("Pandoc ... `pandoc`", "GTK3 [clipped]; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): Linux.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): alternativeto:Typora: rank=32; page=3; 18 likes; alternatives-listed-for-this-entry=24; license=Free Open Source (GPL-3.0) || debian:apt-cache search markdown: not published by the list (no install count in apt-cache) || Flathub: installs_last_month=5267; favorites_count=166.  Further: Flathub total 249,083, 5,267 last month, growth 0.90 (N2).
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** 1 day ago (Flathub, "Changes in version 3.5", relative, as read 2026-10-09); other dates seen: "2026-05-04" (AlternativeTo "this page was last updated May 4, 2026"), "2025-09-30" (version 3.4, apps.gnome.org); (b) actively maintained, stated ("currently [clipped]

## R89. Bear

Slug `bear`; profile `0-comparables/products/bear.md`. Registered because: top five in alternativeto:Obsidian by likes (4 of 30 eligible comparables with a figure; 102). Cells: alternativeto:Obsidian; Mac App Store.

- **Publishes about itself.**
  - Kind (V08): desktop application ("Only for Mac", apps.apple.com); mobile application ("Bear for iOS"; tabs "iPhone", "iPad", bear.app); browser extension [clipped]
  - Reader or editor (V09): editor with rendered view ("Bear is a beautiful, powerfully simple Markdown app to capture, write, and organize your life."; "Markdown hides for a [clipped]
  - Platforms (V10): macOS ("Requires macOS 12.4 or later.", apps.apple.com); iOS ("Bear for iOS", bear.app); iPadOS ("iPad", bear.app tab)
  - Markdown forms claimed (V13): tables ("tables"); wiki-links ("Use WikiLinks to connect notes"); task lists ("Add tasks to notes"); math ("Updated MathJax to version 4") (apps.apple.com); (b) not stated
  - Features the questions ask about: navigation V28: outline, contents or headings sidebar ("Info Panel now with Table of Contents and Backlinks", apps.apple.com; "Outline with focus", [clipped] | find V29: search across files or a folder ("Use Spotlight to search your notes from anywhere", apps.apple.com; "across all of them", bear.app); [clipped] | links and images V30: follows wiki-links or backlinks ("Use WikiLinks to connect notes"; "Table of Contents and Backlinks", apps.apple.com) | appearance V32: themes provided ("Pick from nearly 30 themes", apps.apple.com); light and dark modes ("in both Light and Dark Mode", apps.apple.com); font [clipped] | print and export V33: export to PDF; export to HTML; export to another named format ("TextBundle", "DocX", "ePub", "JPG", "RTF") ("Export to: TXT, Markdown, [clipped] | files stay local V14: content leaves the device, stated ("Your notes are between you and iCloud— we can't see anything", bear.app; "Sync notes between your [clipped]
- **Charges.** Free · In‑App Purchases (apps.apple.com); "Bear Pro $2.99" monthly and "Bear Pro $29.99" yearly (apps.apple.com); "A 7 day free trial, then $2.99 /month -15% $29.99 /year" (bear.app); "14-day free trial" (apps.apple.com); AlternativeTo extract: [clipped]
- **Buyer's all-in cost**, from the page text: price shape (V16b) free with paid tier or features, subscription, free trial, then paid; beyond the price (V17): not stated; prerequisites (V11): minimum operating-system version named ("Requires macOS 12.4 or later.", apps.apple.com); platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): macOS.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): alternativeto:Obsidian: rank=42; page=4; 102 likes; alternatives-listed-for-this-entry=321; license=Freemium Proprietary || Mac App Store: userRatingCount=0; averageUserRating=0
- **Whom its pages address (V05):** Writers and authors ("Bear is used by writers, lawyers, chefs, CEOs, teachers, doctors, engineers, students, parents.. you get the picture.", apps.apple.com); Students and academics (same sentence: [clipped]
- **Last release and maintenance (V27):** Sep 28, 2026 (AlternativeTo extract "App Store: Updated Sep 28, 2026"); App Store What's New "Version 3.0.1 Sep 28" shows no year; (b) not stated

## R90. codexu/note-gen

Slug `codexu-note-gen`; profile `0-comparables/products/codexu-note-gen.md`. Registered because: top five in github-topics:markdown-editor by stars (2 of 84 eligible comparables with a figure; 12,882). Cells: github-topics:markdown-editor.

- **Publishes about itself.**
  - Kind (V08): desktop application ["Windows | Beta", "macOS | Beta", "Linux | Beta" @readme]; mobile application ["Android | Alpha · ARM64", "iOS | Alpha" @readme]
  - Reader or editor (V09): editor with rendered view ["The editor supports: ... Markdown source mode and visual editing" @readme]
  - Platforms (V10): Windows; macOS; Linux; Android; iOS ["Windows · macOS · Linux · Android · iOS" @site]
  - Markdown forms claimed (V13): (a) tables, task lists, math, diagrams ["Tables, task lists, code blocks, math, diagrams, and document outlines" @readme] (b) not stated
  - Features the questions ask about: navigation V28: outline, contents or headings sidebar ["document outlines" @readme] | find V29: find and replace ["Search and replace" @readme]; search across files or a folder ["Search files" @readme] | print and export V33: print ["Export and printing tools" @readme] | files stay local V14: local by default, optional upload stated ["Stored locally by default" @site; "you can sync through services you already use. Supported [clipped]
- **Charges.** (a) "Free and open source" [@download]; "No subscription or account. All core features are free." [@site] (b) free; donation or sponsorship invited, use free ["Support the project through a donation or sponsorship" @business] (c) named open-source [clipped]
- **Buyer's all-in cost**, from the page text: price shape (V16b) free, donation or sponsorship invited, use free; beyond the price (V17): undecidable ["Configure an AI provider when you want to use AI features." @readme]; prerequisites (V11): not stated; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): Linux, macOS, Windows.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): github-topics:markdown-editor: stars=12882; archived=false; last_push=2026-10-08
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** (a) 2026-10-08 (release, day, note-gen-v0.38.1, @api releases) (b) actively maintained, stated ["Actively maintained" @download]

## R91. doocs/md

Slug `doocs-md`; profile `0-comparables/products/doocs-md.md`. Registered because: top five in github-topics:markdown-editor by stars (1 of 84 eligible comparables with a figure; 13,409). Cells: github-topics:markdown-editor.

- **Publishes about itself.**
  - Kind (V08): service ["Online Editor" @readme-en]; browser extension ["打包 Chrome 扩展", "打包 Firefox 扩展" @readme]; terminal program ["npm cli" @readme]; other kind [clipped]
  - Reader or editor (V09): editor with rendered view ["Instantly renders Markdown into WeChat-ready articles" @readme-en; "Local draft management with auto-save" @readme-en]
  - Platforms (V10): inside a host program ["打包 Chrome 扩展", "打包 Firefox 扩展", "打包 uTools 插件" @readme]
  - Markdown forms claimed (V13): (a) GitHub Flavored Markdown ["GFM alert blocks" @readme-en]; callouts or admonitions ["GFM alert blocks" @readme-en]; math ["math formulas (KaTeX)" @readme-en]; diagrams ["Mermaid diagrams, [clipped]
  - Features the questions ask about: appearance V32: themes provided ["Multiple code highlight themes", "Theme switching" @readme-en]; custom stylesheet ["customizable theme colors and CSS" [clipped]
- **Charges.** (a) not stated (b) not stated (c) named open-source licence: "Do What The F*ck You Want To Public License" (WTFPL) [@api licence field]
- **Buyer's all-in cost**, from the page text: price shape (V16b) not stated; beyond the price (V17): not stated; prerequisites (V11): not stated; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): none of the three named.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): github-topics:markdown-editor: stars=13409; archived=false; last_push=2026-10-09
- **Whom its pages address (V05):** Bloggers and platform publishers ["so content creators can spend their time writing rather than fixing layout" @readme-en]
- **Last release and maintenance (V27):** (a) 2025-10-17 (release, day, v2.1.0, @api releases) (b) not stated

## R92. genspark-ai/genoffice

Slug `genspark-ai-genoffice`; profile `0-comparables/products/genspark-ai-genoffice.md`. Registered because: top five in github-topics:markdown-editor by stars (4 of 84 eligible comparables with a figure; 9,042). Cells: github-topics:markdown-editor.

- **Publishes about itself.**
  - Kind (V08): desktop application «a desktop app for macOS, Windows, and Linux» (site); terminal program «a genoffice command line» (README)
  - Reader or editor (V09): editor with rendered view «Rendered, saved as plain Markdown — headings, lists, tables, images, code blocks and Mermaid diagrams in a Tiptap block [clipped]
  - Platforms (V10): macOS «macOS 11+»; Windows «Windows 10+»; Linux «Linux — Debian / Ubuntu» (README download table)
  - Markdown forms claimed (V13): tables; diagrams «headings, lists, tables, images, code blocks and Mermaid diagrams» (README); (b) not stated
  - Features the questions ask about: find V29: search across files or a folder «The home screen searches the names, folders and full text of your .docx, .xlsx, .pptx, PDF, Markdown and [clipped] | print and export V33: export to PDF «genoffice convert report.md --to pdf»; export to another named format «Markdown → Word export» (README) | files stay local V14: local by default, optional upload stated «Document editing is fully local — files never leave your machine to be opened, edited, saved or [clipped]
- **Charges.** «Free, for individuals and teams alike.» (README); «Free to download and use. AI features use Genspark credits or your own API key (BYOK).» (site); (b) free; (c) named open-source licence: Apache License 2.0 «free and open-source under the [clipped]
- **Buyer's all-in cost**, from the page text: price shape (V16b) free; beyond the price (V17): own API key or service account required, stated «AI features use Genspark credits or your own API key (BYOK)» (site); account with the maker [clipped]; prerequisites (V11): minimum operating-system version named «macOS 11+», «Windows 10+», «Ubuntu 22.04 or newer» (README); runtime or interpreter named «install the FUSE 2 [clipped]; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): Linux, macOS, Windows; work use (V18): commercial or work use free, stated «Free, for individuals and teams alike.» (README).
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): github-topics:markdown-editor: stars=9042; archived=false; last_push=2026-10-09
- **Whom its pages address (V05):** Teams, businesses and organisations «Free, for individuals and teams alike.» (README)
- **Last release and maintenance (V27):** 2026-10-08 (release v0.11.411, API); 2026-10-09 (commit) noted; (b) not stated

## R93. ghostwriter

Slug `ghostwriter`; profile `0-comparables/products/ghostwriter.md`. Registered because: top five in Flathub by installs last month (4 of 25 eligible comparables with a figure; 1,827); and top five in alternativeto:Glow by likes (3 of 27 eligible comparables with a figure; 116); and top five in alternativeto:Marked (AlternativeTo entry for Marked) by likes (3 of 32 eligible comparables with a figure; 116); and top five in alternativeto:Typora by likes (3 of 62 eligible comparables with a figure; 116). Cells: alternativeto:Typora; alternativeto:Marked (AlternativeTo entry for Marked); alternativeto:Glow; debian:apt-cache search markdown; Flathub; Snap Store.

- **Publishes about itself.**
  - Kind (V08): desktop application «Download for Windows ... Linux ... Mac» (site); «Desktop Only» (Flathub)
  - Reader or editor (V09): editor with rendered view «distraction-free text editor for Markdown featuring a live HTML preview as you type» (Flathub, Snap)
  - Platforms (V10): Windows «Windows 10 - available only as portable 64 bit»; Linux «Linux repos»; macOS «MacOS - build from source (community-supported)» (download [clipped]
  - Markdown forms claimed (V13): other named flavour «can integrate with Pandoc, MultiMarkdown, Discount, and cmark processors» (Flathub, Snap); math «MathJax: Use Pandoc to make beautiful equations in MathJax!» (site); (b) not [clipped]
  - Features the questions ask about: navigation V28: outline, contents or headings sidebar; jump to heading or section «sidebar provides an outline of the document that allows you to navigate [clipped] | file changed elsewhere V31: preview updates as you type inside the product, stated «live HTML preview as you type» (Flathub) | appearance V32: themes provided; light and dark modes «The built-in light and dark themes» (site) | print and export V33: export to another named format «Export to Multiple Formats: Pandoc, MultiMarkdown, commonmark» (site); copy as rich text or HTML «you can [clipped]
- **Charges.** «Free and Open Source» (site); Flathub label «Free»; AlternativeTo «Cost / License Free Open Source (GPL-3.0)»; (b) free; (c) named open-source licence: GNU General Public License v3.0 «distributed this software under the generous GNU General Public [clipped]
- **Buyer's all-in cost**, from the page text: price shape (V16b) free; beyond the price (V17): not stated; prerequisites (V11): not stated; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): Linux, macOS, Windows.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): alternativeto:Typora: rank=6; page=1; 116 likes; alternatives-listed-for-this-entry=159; license=Free Open Source (GPL-3.0) || alternativeto:Marked (AlternativeTo entry for Marked): rank=2; page=1; 116 likes; alternatives-listed-for-this-entry=159; license=Free Open Source (GPL-3.0) || alternativeto:Glow: rank=2; page=1; 116 likes; alternatives-listed-for-this-entry=159; license=Free Open Source (GPL-3.0) || debian:apt-cache search markdown: not published by the list (no install count in apt-cache) || Flathub: installs_last_month=1827; favorites_count=29 || Snap Store: none given by API (find returns no install, rating or download counts).  Further: Flathub total 85,446, growth 1.16 (N2).
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** 2026-07-03 (Snap «Last updated 3 July 2026», latest/stable 26.04.3); (b) not stated

## R94. Haroopad

Slug `haroopad`; profile `0-comparables/products/haroopad.md`. Registered because: top five in alternativeto:Glow by likes (5 of 27 eligible comparables with a figure; 68); and top five in alternativeto:Marked (AlternativeTo entry for Marked) by likes (5 of 32 eligible comparables with a figure; 68). Cells: alternativeto:Typora; alternativeto:Marked (AlternativeTo entry for Marked); alternativeto:Glow; homebrew:cask.

- **Publishes about itself.**
  - Kind (V08): desktop application [S4 "It runs on all three major operating systems—Windows, Mac OS X, and Linux."; S1 "Haroopad.app"]
  - Reader or editor (V09): editor, rendered view not stated [S1 "Markdown editor"; S4 "You can author ... documents"]
  - Platforms (V10): Windows [S4]; macOS [S4 "Mac OS X"; S1 "Requirements: macOS"]; Linux [S4]
  - Markdown forms claimed (V13): markdown named, no form named [S4 "markdown enabled document processor"]; (b) not stated
  - Features the questions ask about: V28 to V33 and V14 all not stated
- **Charges.** not stated; (b) not stated; (c) named open-source licence: GPL-3.0 [S4 "GPL-3.0 license" repository field; S2 "Open Source (GPL-3.0)"]
- **Buyer's all-in cost**, from the page text: price shape (V16b) not stated; beyond the price (V17): not stated; prerequisites (V11): undecidable; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): Linux, macOS, Windows.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): alternativeto:Typora: rank=47; page=4; 68 likes; alternatives-listed-for-this-entry=114; license=Free Open Source (GPL-3.0); alerts=Discontinued || alternativeto:Marked (AlternativeTo entry for Marked): rank=18; page=2; 68 likes; alternatives-listed-for-this-entry=not shown; license=Free Open Source (GPL-3.0); alerts=Discontinued || alternativeto:Glow: rank=10; page=1; 68 likes; alternatives-listed-for-this-entry=114; license=Free Open Source (GPL-3.0); alerts=Discontinued || homebrew:cask: 30d=1; 90d=3; 365d=17.  Further: Homebrew cask flagged disabled (N1).
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** not stated; (b) archived, deprecated or unmaintained, stated [S2 "Discontinued."; S1 "haroopad (disabled)"]

## R95. Joplin

Slug `joplin`; profile `0-comparables/products/joplin.md`. Registered because: top five in alternativeto:Obsidian by likes (1 of 30 eligible comparables with a figure; 947); and top five in alternativeto:Typora by likes (1 of 62 eligible comparables with a figure; 947). Cells: alternativeto:Typora; alternativeto:Obsidian; Snap Store.

- **Publishes about itself.**
  - Kind (V08): desktop application [S4 "available on Windows, macOS, Linux"]; mobile application [S4 "Android and iOS"]; terminal program [S4 "A terminal app is [clipped]
  - Reader or editor (V09): editor, rendered view not stated [S4 "multiple text editors (Rich Text or Markdown)"]
  - Platforms (V10): Windows [S4]; macOS [S4]; Linux [S4]; Android [S4]; iOS [S4 "The app is available on Windows, macOS, Linux, Android and iOS."]
  - Markdown forms claimed (V13): math [S4 "Create math expressions and diagrams directly from the app."]; diagrams [S4 same sentence]; (b) not stated
  - Features the questions ask about: appearance V32: themes provided [S4 "custom themes"] | print and export V33: share or send from the product [S4 "publish a note to the internet and share the URL with others"]
- **Charges.** Subscription ranging between $2 and $8 per month + free version with limited functionality. [S3] (Joplin Cloud); "A free, private note taking and to-do app!" [S1]; (b) free [S1 "A free, private note taking and to-do app!"]; subscription [S3 [clipped]
- **Buyer's all-in cost**, from the page text: price shape (V16b) free, subscription, free with paid tier or features; beyond the price (V17): not stated; prerequisites (V11): not stated; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): Linux, macOS, Windows.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): alternativeto:Typora: rank=1; page=1; 947 likes; alternatives-listed-for-this-entry=241; license=Freemium Open Source (AGPL-3.0) || alternativeto:Obsidian: rank=4; page=1; 947 likes; alternatives-listed-for-this-entry=241; license=Freemium Open Source (AGPL-3.0) || Snap Store: none given by API (find returns no install, rating or download counts) / none given by API (find returns no install, rating or download counts).  Further: GitHub laurent22/joplin: not archived; last push 2026-10-09; newest release v3.7.21 on 2026-09-25; 35 releases in the last 365 days, 3,530,285 downloads (N5).
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** 26 September 2026 (day; S1 "Last updated 26 September 2026 - latest/stable"); (b) archived, deprecated or unmaintained, stated [S2 "This snap hasn't been updated in a while. It might be unmaintained and have stability or security issues."] (second snap only)

## R96. MacDown

Slug `macdown`; profile `0-comparables/products/macdown.md`. Registered because: top five in github-topics:markdown-editor by stars (3 of 84 eligible comparables with a figure; 9,835); and top five in github-topics:markdown-viewer by stars (1 of 21 eligible comparables with a figure; 9,835); and top five in homebrew:cask by 365-day installs (4 of 44 eligible comparables with a figure; 17,571). Cells: alternativeto:Typora; alternativeto:Marked (AlternativeTo entry for Marked); github-topics:markdown-viewer; github-topics:markdown-editor; homebrew:cask.

- **Publishes about itself.**
  - Kind (V08): desktop application: [C] "The open source Markdown editor for macOS."
  - Reader or editor (V09): editor with rendered view: [C] "Highly customisable Markdown rendering."; [B] "Live Preview"
  - Platforms (V10): macOS: [C] "for macOS"
  - Markdown forms claimed (V13): syntax-highlighted code blocks: [C] "Syntax highlighting in fenced code blocks."; (b) not stated
  - Features the questions ask about: file changed elsewhere V31: preview updates as you type inside the product, stated: [B] "Live Preview" | appearance V32: themes provided: [E] "The following editor themes and CSS files are extracted from Mou"; light and dark modes: [B] "Dark Mode"
- **Charges.** [B] "Free"; [B] "Open Source and Free product."; (b) free; (c) named open-source licence: [C] "released under the MIT License"; [E] "MIT License"
- **Buyer's all-in cost**, from the page text: price shape (V16b) free; beyond the price (V17): not stated; prerequisites (V11): runtime or interpreter named: [A] "macdown is built for Intel macOS and requires Rosetta 2 on Apple Silicon."; build toolchain named: [E] "OS X SDK [clipped]; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): macOS.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): alternativeto:Typora: rank=51; page=5; 23 likes; alternatives-listed-for-this-entry=75; license=Free Open Source; alerts=Discontinued || alternativeto:Marked (AlternativeTo entry for Marked): rank=17; page=2; 23 likes; alternatives-listed-for-this-entry=75; license=Free Open Source; alerts=Discontinued || github-topics:markdown-viewer: stars=9835; archived=false; last_push=2023-07-10 || github-topics:markdown-editor: stars=9835; archived=false; last_push=2023-07-10 || homebrew:cask: 30d=2; 90d=2,311; 365d=17,571.  Further: Homebrew cask 'macdown' is flagged disabled; 30-day count 2 against 365-day 17,571 (N1). GitHub MacDownApp/macdown: not archived; last push 2023-07-10; newest release v0.8.0d71 on 2020-02-21, none in the last 365 days (N5).
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** "Jan 20, 2024" (day; [B] "this page was last updated Jan 20, 2024"; latest release [F] v0.7.3 "03 Jan", page datetime 2020-01-03); (b) archived, deprecated or unmaintained, stated: [B] "DiscontinuedThe latest version (0.7.3) is from January 2020"; [A] [clipped]

## R97. Manuscript

Slug `manuscript`; profile `0-comparables/products/manuscript.md`. Registered because: top five in Flathub by installs last month (5 of 25 eligible comparables with a figure; 1,763). Cells: Flathub.

- **Publishes about itself.**
  - Kind (V08): desktop application: [A] "Desktop & Mobile"; mobile application: [A] "Desktop & Mobile"; [C] "Adaptive — works on phones and tablets (GNOME Mobile, [clipped]
  - Reader or editor (V09): editor with rendered view: [A] "Three view modes: Read, Edit, and Split with live preview"
  - Platforms (V10): Linux: [A] tag "linux"; [C] "Dependencies (Fedora)", "(Debian/Ubuntu)"
  - Markdown forms claimed (V13): syntax-highlighted code blocks: [A] "Syntax-highlighted code blocks in 100+ languages"; tables: [A] "Tables rendered as a grid"; task lists: [A] "Task list checkboxes"; callouts or admonitions: [C] [clipped]
  - Features the questions ask about: navigation V28: outline, contents or headings sidebar: [C] "Outline panel — F9 toggles a sidebar with all document headings"; scroll position kept or [clipped] | find V29: find and replace: [C] "Find and Replace — Ctrl+H"; search: undecidable (see notes) | links and images V30: opens web links in the browser: [C] "Clickable links — open in default browser"; shows remote images: [C] "Remote images — ![alt](…) is [clipped] | file changed elsewhere V31: both stated: [A] "File watching with automatic reload"; [A] "Split with live preview" | appearance V32: follows the system appearance, stated: [A] "It follows your system theme automatically"; light and dark modes: [C] "follows system [clipped] | print and export V33: print: [C] "Rendered print — Ctrl+P prints the rendered markdown"; export to PDF: [C] "Export as PDF — File menu → Export as PDF… writes an [clipped]
- **Charges.** [A] "Free"; (b) free; (c) named open-source licence: [C] "GNU General Public License v3.0"; [B] "GNU General Public License v3.0 or later"
- **Buyer's all-in cost**, from the page text: price shape (V16b) free; beyond the price (V17): not stated; prerequisites (V11): build toolchain named: [C] "sudo dnf install gcc cargo gtk4-devel libadwaita-devel gtksourceview5-devel pango-devel oniguruma-devel" (source route); platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): Linux.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): Flathub: installs_last_month=1763; favorites_count=16.  Further: Flathub total 9,982, growth 1.23; first listed 2026-03-25, described there as 'Read and edit Markdown files' (N2).
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** "15 days ago" (relative, no calendar date; version 1.5.2, [A] "Changes in version 1.5.2 15 days ago"); (b) not stated

## R98. mark-text

Slug `mark-text`; profile `0-comparables/products/mark-text.md`. Registered because: top five in homebrew:cask by 365-day installs (3 of 44 eligible comparables with a figure; 22,164). Cells: homebrew:cask.

- **Publishes about itself.**
  - Kind (V08): desktop application: [C] "Available for Linux, macOS and Windows."
  - Reader or editor (V09): editor with rendered view: [E] "A true WYSIWYG editor — your Markdown transforms in place the moment you type."; [C] "Realtime preview (WYSIWYG)"
  - Platforms (V10): macOS; Windows; Linux: [C] "Available for Linux, macOS and Windows."
  - Markdown forms claimed (V13): CommonMark: [C] "Support CommonMark Spec"; GitHub Flavored Markdown: [C] "GitHub Flavored Markdown Spec"; other named flavour: [C] "selective support Pandoc markdown"; math: [C] "math expressions [clipped]
  - Features the questions ask about: file changed elsewhere V31: preview updates as you type inside the product, stated: [E] "your Markdown transforms in place the moment you type" | appearance V32: themes provided: [E] "33 built-in themes"; custom stylesheet: [E] "full custom CSS"; light and dark modes: [E] "Light & dark, instantly"; [clipped] | print and export V33: export to PDF: [C] "Output HTML and PDF files."; export to HTML: [C] "Output HTML and PDF files."
- **Charges.** [E] "Free & open source forever"; [E] "Free download"; [E] "One download. No account, no subscription."; (b) free; donation or sponsorship invited, use free: [E] "sponsorship keeps development going"; (c) named open-source licence: [E] "Released [clipped]
- **Buyer's all-in cost**, from the page text: price shape (V16b) free, donation or sponsorship invited, use free:; beyond the price (V17): not stated; prerequisites (V11): minimum operating-system version named: [C] "Requires macOS 11 (Big Sur) or later."; "Requires Windows 10 or 11."; [A] "Requirements: macOS >= 12"; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): Linux, macOS, Windows.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): homebrew:cask: 30d=23; 90d=4,302; 365d=22,164.  Further: Homebrew cask 'mark-text' is flagged disabled by Homebrew; 30-day count 23 against 365-day 22,164, growth 0.01 (N1). The product's own repository is still releasing (see marktext, N5: v0.21.1 on 2026-10-08).
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** "08 Oct 15:39" (v0.21.1 release, day; [D] "released this 08 Oct 15:39", page datetime 2026-10-08); (b) undecidable (see notes)

## R99. Markdown All in One

Slug `markdown-all-in-one`; profile `0-comparables/products/markdown-all-in-one.md`. Registered because: top five in vscode by installs (1 of 19 eligible comparables with a figure; 14,704,347). Cells: vscode.

- **Publishes about itself.**
  - Kind (V08): editor extension :: "Extension for Visual Studio Code" [1]
  - Reader or editor (V09): editor with rendered view :: "All you need to write Markdown (keyboard shortcuts, table of contents, auto preview and more)" [1]
  - Platforms (V10): inside a host program :: "Extension for Visual Studio Code" [1]
  - Markdown forms claimed (V13): tables :: "Table formatter" [1] || task lists :: "Task lists" [1] || math :: "Math" [1] || (b) not stated
  - Features the questions ask about: navigation V28: outline, contents or headings sidebar :: "Create Table of Contents ... to insert a new table of contents" [1] (inserted) | appearance V32: themes provided :: "Theme of the exported HTML" [1] (applies to exported HTML) | print and export V33: export to HTML :: "Markdown: Print current document to HTML" [1]
- **Charges.** "Free" in "14,704,681 installs | (172) | Free" [1] || (b) free :: "Free" [1] || donation or sponsorship invited, use free :: "Buy me a coffee" [1] || (c) named open-source licence :: "MIT license" [2]
- **Buyer's all-in cost**, from the page text: price shape (V16b) free, donation or sponsorship invited, use free; beyond the price (V17): not stated; prerequisites (V11): host program named :: "New to Visual Studio Code? Get it now." [1]; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): none of the three named.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): vscode: installs=14704347; ratings=172; average=4.69; lastUpdated=2025-03-09
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** 2025-03-09 (day), "LastUpdatedDateString: Sun, 09 Mar 2025" in listing data embedded in page [1] || (b) not stated

## R100. Markdown゜

Slug `markdown`; profile `0-comparables/products/markdown.md`. Registered because: top five in Mac App Store by rating count (2 of 134 eligible comparables with a figure, 36 of them non-zero; 484). Cells: Mac App Store.

- **Publishes about itself.**
  - Kind (V08): mobile application :: "for iPhone, iPad" [1] || desktop application :: "and Mac" [1]
  - Reader or editor (V09): editor with rendered view :: "watch headings, lists, tables, images and task lists render as you type" [1]
  - Platforms (V10): iOS :: "Requires iOS 15.0 or later." [1] || iPadOS :: "Requires iPadOS 15.0 or later." [1] || macOS :: "Requires macOS 12.0 or later." [1]
  - Markdown forms claimed (V13): tables :: "Tables render inline as you edit" [1] || task lists :: "Task lists with tappable checkmarks" [1] || syntax-highlighted code blocks :: "Pick your syntax highlighting theme" [1] || (b) not [clipped]
  - Features the questions ask about: find V29: find and replace :: "FIND AND REPLACE Search through a document and replace as you go." [1] || search within document :: same sentence [1] | file changed elsewhere V31: preview updates as you type inside the product, stated :: "Live preview beside your text on iPad and Mac" [1] | appearance V32: light and dark modes :: "Full light and dark mode support" [1] || themes provided :: "Pick your syntax highlighting theme" [1] || font or [clipped] | print and export V33: export to PDF :: "Export to PDF, HTML or raw Markdown" [1] || export to HTML :: same [1] || export to another named format :: "raw [clipped] | files stay local V14: local, stated :: "Your documents and exports stay on your device" [1]
- **Charges.** "price": 0, "priceCurrency": "USD" [1] || (b) free :: price 0 in the Offer field [1] || (c) not stated
- **Buyer's all-in cost**, from the page text: price shape (V16b) free; beyond the price (V17): not stated; prerequisites (V11): minimum operating-system version named :: "Requires iOS 15.0 or later." [1]; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): macOS.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): Mac App Store: userRatingCount=484; averageUserRating=4.55372.  Further: Mac App Store, 484 ratings, average 4.55, current version 2026-09-30 (N6). Of 45 recent reviews in the US feed, 27 are 1 or 2 stars (mean 2.4); quoted complaints concern edits (N6).
- **Whom its pages address (V05):** Writers and authors :: "writing documentation" [1] || Note-takers and personal knowledge managers :: "keeping a journal" ; "taking notes in a meeting" [1]
- **Last release and maintenance (V27):** 2026-09-30 (day), version field "Version 2.0.1 | Wed Sep 30 2026" [1] || (b) not stated

## R101. MarkEdit

Slug `markedit`; profile `0-comparables/products/markedit.md`. Registered because: top five in homebrew:cask by 365-day installs (5 of 44 eligible comparables with a figure; 17,031). Cells: alternativeto:Typora; github-topics:markdown-editor; homebrew:cask.

- **Publishes about itself.**
  - Kind (V08): desktop application (\"MarkEdit is a free and open-source Markdown editor, for macOS.\" P4)
  - Reader or editor (V09): editor, rendered view not stated (\"MarkEdit is a free and open-source Markdown editor, for macOS.\" P4)
  - Platforms (V10): macOS (\"Markdown editor, for macOS.\" P4)
  - Markdown forms claimed (V13): GitHub Flavored Markdown (\"MarkEdit strictly follows the [GFM specification]\" P4); (b) not stated
  - Features the questions ask about: navigation V28: folding of sections (\"Complex editing like multi-caret and code folding is built on\" P4) | appearance V32: custom stylesheet (\"Customization is built around CSS, JavaScript, and\" P4)
- **Charges.** \"free\" (\"MarkEdit is a free and open-source Markdown editor, for macOS.\" P4); (b) free (P4); (c) named open-source licence (\"MIT license\" P3; \"Open Source (MIT) and Free product.\" P2)
- **Buyer's all-in cost**, from the page text: price shape (V16b) free; beyond the price (V17): not stated; prerequisites (V11): minimum operating-system version named (\"Platform-macOS_26.0+\" P4; \"Requirements: macOS >= 15\" P6); platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): macOS.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): alternativeto:Typora: rank=42; page=4; 5 likes; alternatives-listed-for-this-entry=not shown; license=Free Open Source (MIT) || github-topics:markdown-editor: stars=5805; archived=false; last_push=2026-10-09 || homebrew:cask: 30d=1,150; 90d=4,810; 365d=17,031.  Further: GitHub MarkEdit-app/MarkEdit: not archived; last push 2026-10-09; newest release v1.36.0 2026-09-23; 15 releases in the last 365 days, 1,183,007 downloads (N5). Homebrew growth 0.81 (N1).
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** 23 Sep, no year (day and month; 'released this 23 Sep 02:47', v1.36.0, P5); (b) not stated

## R102. marknote

Slug `marknote`; profile `0-comparables/products/marknote.md`. Registered because: top five in Flathub by installs last month (3 of 25 eligible comparables with a figure; 2,371). Cells: debian:apt-cache search markdown; Flathub; Snap Store.

- **Publishes about itself.**
  - Kind (V08): desktop application "Other platforms: macOS | Windows" [p5]
  - Reader or editor (V09): editor, rendered view not stated "Source Mode for raw Markdown editing" [p5]
  - Platforms (V10): Linux "Install on Linux" [p5]; macOS "Other platforms: macOS" [p5]; Windows "Windows" [p5]
  - Markdown forms claimed (V13): task lists "lists, check boxes, images and more" [p4]; (b) not stated
  - Features the questions ask about: find V29: undecidable
- **Charges.** Free [p2]; "price=0.0 USD" [p1]; (b) free; donation or sponsorship invited, use free; (c) named open-source licence: "GPL-2.0-or-later" [p1]
- **Buyer's all-in cost**, from the page text: price shape (V16b) free, donation or sponsorship invited, use free; beyond the price (V17): not stated; prerequisites (V11): not stated; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): Linux, macOS, Windows.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): debian:apt-cache search markdown: not published by the list (no install count in apt-cache) || Flathub: installs_last_month=2371; favorites_count=43 || Snap Store: none given by API (find returns no install, rating or download counts).  Further: Flathub total 53,316, growth 0.60 (N2).
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** 2026-05-30 (1.6.0 release entry, p5; day precision); (b) not stated

## R103. MarkText

Slug `marktext`; profile `0-comparables/products/marktext.md`. Registered because: top five in Flathub by installs last month (2 of 25 eligible comparables with a figure; 3,370); and top five in alternativeto:Glow by likes (2 of 27 eligible comparables with a figure; 122); and top five in alternativeto:Marked (AlternativeTo entry for Marked) by likes (2 of 32 eligible comparables with a figure; 122); and top five in alternativeto:Typora by likes (2 of 62 eligible comparables with a figure; 122). Cells: alternativeto:Typora; alternativeto:Marked (AlternativeTo entry for Marked); alternativeto:Glow; Flathub; Snap Store.

- **Publishes about itself.**
  - Kind (V08): desktop application "Available for Linux, macOS and Windows." [p4]
  - Reader or editor (V09): editor with rendered view "Realtime preview" [p6]
  - Platforms (V10): Linux "Available for Linux, macOS and Windows." [p4]; macOS [p4]; Windows [p4]
  - Markdown forms claimed (V13): CommonMark "Support CommonMark Spec" [p4]; GitHub Flavored Markdown "GitHub Flavored Markdown Spec" [p4]; other named flavour "selective support Pandoc markdown" [p4]; math "math expressions (KaTeX)" [clipped]
  - Features the questions ask about: appearance V32: themes provided "33 built-in themes, light and dark." [p6]; light and dark modes [p6]; custom stylesheet "Every one is just CSS — fork a [clipped] | print and export V33: export to PDF "Output HTML and PDF files." [p4]; export to HTML [p4]
- **Charges.** Free & open source forever [p6]; "Free download" [p6]; "price=0.0 USD" [p1]; (b) free; (c) named open-source licence: "MIT." [p4]
- **Buyer's all-in cost**, from the page text: price shape (V16b) free; beyond the price (V17): not stated; prerequisites (V11): minimum operating-system version named "Requires macOS 11 (Big Sur) or later." [p4]; "Requires Windows 10 or 11." [p4]; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): Linux, macOS, Windows.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): alternativeto:Typora: rank=7; page=1; 122 likes; alternatives-listed-for-this-entry=141; license=Free Open Source (MIT) || alternativeto:Marked (AlternativeTo entry for Marked): rank=4; page=1; 122 likes; alternatives-listed-for-this-entry=141; license=Free Open Source (MIT) || alternativeto:Glow: rank=3; page=1; 122 likes; alternatives-listed-for-this-entry=141; license=Free Open Source (MIT) || Flathub: installs_last_month=3370; favorites_count=24 || Snap Store: none given by API (find returns no install, rating or download counts).  Further: GitHub marktext/marktext: not archived; last push 2026-10-09; newest release v0.21.1 2026-10-08; 20 releases in the last 365 days, 751,415 downloads (N5). Flathub total 148,193, growth 1.05 (N2). Homebrew cask marked disabled by Homebrew (see mark-text).
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** 3 months ago (Flathub, changes in version 0.19.0, p2; relative, no calendar date); p1 "9 August 2022"; (b) not stated

## R104. Marp for VS Code

Slug `marp-for-vs-code`; profile `0-comparables/products/marp-for-vs-code.md`. Registered because: top five in vscode by installs (4 of 19 eligible comparables with a figure; 871,866). Cells: vscode.

- **Publishes about itself.**
  - Kind (V08): editor extension "Marp for VS Code is an extension that allows you to edit and preview slide Markdown and custom theming within VS Code." [p2]
  - Reader or editor (V09): editor with rendered view "edit and preview slide Markdown" [p2]
  - Platforms (V10): inside a host program "within VS Code" [p2]
  - Markdown forms claimed (V13): front matter "when marp: true is written in a front-matter of Markdown document" [p1]; other named flavour "Marp Markdown" [p1]; (b) not stated
  - Features the questions ask about: navigation V28: outline, contents or headings sidebar "Outline view for each slide" [p1] | file changed elsewhere V31: undecidable | appearance V32: custom stylesheet "custom theme CSS for Marpit / Marp Core" [p1] | print and export V33: export to HTML "Export slide deck to HTML, PDF, PPTX, and image" [p1]; export to PDF [p1]; export to another named format "PPTX" [p1]
- **Charges.** Free [p1]; (b) free; donation or sponsorship invited, use free; (c) named open-source licence: "MIT License" [p1]
- **Buyer's all-in cost**, from the page text: price shape (V16b) free, donation or sponsorship invited, use free; beyond the price (V17): not stated; prerequisites (V11): host program named "Create slide deck written in Marp Markdown on VS Code." [p1]; undecidable (browser needed for export); platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): none of the three named.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): vscode: installs=871866; ratings=29; average=4.97; lastUpdated=2026-08-11
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** Tue, 11 Aug 2026 11:59:16 GMT (version 3.6.1 lastUpdated, p1; day precision); (b) not stated

## R105. MWeb

Slug `mweb`; profile `0-comparables/products/mweb.md`. Registered because: top five in Mac App Store by rating count (3 of 134 eligible comparables with a figure, 36 of them non-zero; 153). Cells: alternativeto:Typora; alternativeto:Marked (AlternativeTo entry for Marked); alternativeto:Glow; homebrew:cask; Mac App Store.

- **Publishes about itself.**
  - Kind (V08): desktop application [A: 'Mac Requires macOS 10.13 or later']; mobile application [A: 'iPhone Requires iOS 14.1 or later']
  - Reader or editor (V09): editor with rendered view [A: 'Markdown documents can be previewed and support Editor & Preview mode.']
  - Platforms (V10): iOS [A]; iPadOS [A]; macOS [A][H]
  - Markdown forms claimed (V13): CommonMark [A]; GitHub Flavored Markdown [A]; tables [A]; math [A: 'math formulas']; task lists [A]; footnotes [A] (b) not stated
  - Features the questions ask about: navigation V28: outline, contents or headings sidebar [A: 'view the outline'; 'supporting TOC'] (location not stated) | find V29: undecidable | appearance V32: themes provided [A: '11 light themes and 21 dark themes']; custom stylesheet [B: 'Custom Preview Style (CSS)']; font or size choice [A: [clipped] | print and export V33: export to PDF [A]; export to another named format [A: 'Epub or image']; export to HTML [E: 'export to PDF/HTML/RTF/DOCX'] | files stay local V14: local by default, optional upload stated [A: 'The Library follows the "local first" principle'; 'Complete cross-device synchronization [clipped]
- **Charges.** 'Free · In‑App Purchases'; 'MWeb for iPhone/iPad $14.99'; 'MWeb Yearly Subscription $9.99'; 'MWeb for Mac $24.99' [A]; 'MWeb Pro Lifetime Version for $34.99' [B]; 'One time purchase (perpetual license) that costs $10.' [E] (b) free with paid tier or [clipped]
- **Buyer's all-in cost**, from the page text: price shape (V16b) free with paid tier or features, one-time purchase, subscription; beyond the price (V17): not stated; prerequisites (V11): minimum operating-system version named [A: 'Mac Requires macOS 10.13 or later']; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): macOS.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): alternativeto:Typora: rank=70; page=6; 10 likes; alternatives-listed-for-this-entry=not shown; license=Paid Proprietary Origin China Platforms Mac China More about MWeb Good alternative? Is [clipped] || alternativeto:Marked (AlternativeTo entry for Marked): rank=41; page=4; 10 likes; alternatives-listed-for-this-entry=not shown; license=Paid Proprietary Origin China Platforms Mac China More about MWeb Good alternative? Is [clipped] || alternativeto:Glow: rank=23; page=2; 10 likes; alternatives-listed-for-this-entry=not shown; license=Paid Proprietary Origin China Platforms Mac China More about MWeb Good alternative? Is [clipped] || homebrew:cask: 30d=2; 90d=22; 365d=164 || Mac App Store: userRatingCount=153; averageUserRating=4.53594.  Further: Mac App Store, 153 ratings, average 4.54, current version 2026-05-03 (N6).
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** Apr 7, 2021 (listing updated), day precision [E: 'Updated: Apr 7, 2021'] (b) not stated

## R106. obsidian

Slug `obsidian`; profile `0-comparables/products/obsidian.md`. Registered because: top five in homebrew:cask by 365-day installs (1 of 44 eligible comparables with a figure; 194,535). Cells: homebrew:cask.

- **Publishes about itself.**
  - Kind (V08): desktop application ("Requirements: macOS >= 12"; "Obsidian.app"; "Get Obsidian for Windows")
  - Reader or editor (V09): not stated
  - Platforms (V10): macOS ("Requirements: macOS >= 12") | Windows ("Get Obsidian for Windows") | Linux ("Linux AppImage") | iOS ("iOS App Store") | Android ("Android [clipped]
  - Markdown forms claimed (V13): markdown named, no form named ("Obsidian stores your notes locally as plain text Markdown files.", obsidian.md); (b) not stated
  - Features the questions ask about: find V29: undecidable ("Graph and full text search", listed under Publish, obsidian.md/pricing) | appearance V32: themes provided ("thousands of plugins and themes", obsidian.md) | print and export V33: share or send from the product ("Publish instantly. Turn your notes into an online wiki", obsidian.md) | files stay local V14: local by default, optional upload stated ("Obsidian stores notes privately on your device" obsidian.md; "If you choose to use Obsidian [clipped]
- **Charges.** Free without limits. No sign-up required. No strings attached. (obsidian.md/pricing) | "Catalyst $25 USD One-time payment" | "Commercial $50 USD Per user, per year" | "Sync $4 USD Per user, per month, billed annually; $5 USD Per user, per month, [clipped]
- **Buyer's all-in cost**, from the page text: price shape (V16b) free, free with paid tier or features, subscription, one-time purchase, paid licence for a named use, see note); beyond the price (V17): not stated; prerequisites (V11): minimum operating-system version named ("Requirements: macOS >= 12", formulae.brew.sh/cask/obsidian); platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): Linux, macOS, Windows; work use (V18): commercial or work use free, stated ("Do I have to pay for commercial use? No. You are not required to pay for a commercial license", [clipped].
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): homebrew:cask: 30d=11,345; 90d=51,034; 365d=194,535.  Further: GitHub obsidianmd/obsidian-releases: not archived; newest release v1.14.4 on 2026-10-05; 12 releases in the last 365 days, 35,862,310 downloads (N5). Homebrew growth 0.70 (N1).
- **Whom its pages address (V05):** Teams, businesses and organisations ("if you are using Obsidian for work in an organization", obsidian.md/pricing)
- **Last release and maintenance (V27):** 2026-10-05 (day; "Last updated 2026-10-05", datetime attribute on obsidian.md/download); version 1.14.4 undated; (b) not stated

## R107. Office Viewer

Slug `office-viewer`; profile `0-comparables/products/office-viewer.md`. Registered because: top five in vscode by installs (3 of 19 eligible comparables with a figure; 1,556,537). Cells: vscode.

- **Publishes about itself.**
  - Kind (V08): editor extension ("Visual Studio Code > Visualization > Office Viewer"; "directly in VS Code")
  - Reader or editor (V09): editor with rendered view ("using WYSIWYG editor for markdown"; "preview and edit common office and design files directly in VS Code")
  - Platforms (V10): inside a host program ("directly in VS Code")
  - Markdown forms claimed (V13): markdown named, no form named ("Markdown: .md , .markdown"; "WYSIWYG editor for markdown"); (b) not stated
  - Features the questions ask about: print and export V33: export to PDF | export to HTML | export to another named format (DOCX) ("Right-click in the editor to export Markdown to PDF, DOCX, or [clipped]
- **Charges.** 1,556,659 installs | ( 100 ) | Free (marketplace field); (b) free; (c) not stated
- **Buyer's all-in cost**, from the page text: price shape (V16b) free; beyond the price (V17): not stated; prerequisites (V11): host program named ("directly in VS Code"); platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): none of the three named.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): vscode: installs=1556537; ratings=100; average=4.31; lastUpdated=2026-08-16
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** Sun, 16 Aug 2026 08:11:49 GMT (day; version 4.2.0, lastUpdated in page data); (b) not stated

## R108. One Markdown

Slug `one-markdown`; profile `0-comparables/products/one-markdown.md`. Registered because: top five in Mac App Store by rating count (4 of 134 eligible comparables with a figure, 36 of them non-zero; 148). Cells: Mac App Store.

- **Publishes about itself.**
  - Kind (V08): desktop application ("Requires macOS 10.13 or later.") | mobile application ("iPhone, iPad, Mac" device line; "Requires iOS 14.5 or later.") [clipped]
  - Reader or editor (V09): editor with rendered view ("a simple and fast editor"; "Markdown documents can be previewed and support Editor & Preview mode.")
  - Platforms (V10): iOS ("Requires iOS 14.5 or later.") | iPadOS ("iPadOS 14.5 or later") | macOS ("Requires macOS 10.13 or later.") (Compatibility field; visionOS also [clipped]
  - Markdown forms claimed (V13): CommonMark | GitHub Flavored Markdown | tables | task lists | footnotes | math ("math formulas") | diagrams ("mermaid and Echarts drawings can be previewed") ("Base on CommonMark syntax and GitHub [clipped]
  - Features the questions ask about: navigation V28: outline, contents or headings sidebar ("You can view the outline and word count of Markdown documents.") | appearance V32: themes provided ("11 light themes and 21 dark themes") | light and dark modes ("light themes and 21 dark themes") | font or size choice [clipped] | print and export V33: export to PDF ("The style for exporting to PDF can now be selected from the custom themes.", What is New)
- **Charges.** Free · In-App Purchases | "One Markdown for Mac $9.99" | "One Markdown Yearly Subscribe $3.99" | "One Markdown for iPhone/iPad $9.99" (listing); (b) free with paid tier or features ("Free · In-App Purchases") | one-time purchase ($9.99 in-app [clipped]
- **Buyer's all-in cost**, from the page text: price shape (V16b) free with paid tier or features, one-time purchase, subscription; beyond the price (V17): not stated; prerequisites (V11): minimum operating-system version named ("Requires iOS 14.5 or later. ... Requires macOS 10.13 or later."); platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): macOS.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): Mac App Store: userRatingCount=148; averageUserRating=4.60811.  Further: Mac App Store, 148 ratings, average 4.61, current version 2026-05-03 (N6).
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** May 3 (year not published; "1.6.7 May 3", newest version-history entry); dated entries "1.6.6 12/02/2025"; (b) not stated

## R109. pd4d10/hashmd

Slug `pd4d10-hashmd`; profile `0-comparables/products/pd4d10-hashmd.md`. Registered because: top five in github-topics:markdown-viewer by stars (2 of 21 eligible comparables with a figure; 4,346). Cells: github-topics:markdown-viewer; github-topics:markdown-editor.

- **Publishes about itself.**
  - Kind (V08): not stated
  - Reader or editor (V09): editor with rendered view ("Hackable Markdown Editor and Viewer (WIP)"; viewer of markdown read under eligibility test 2(a))
  - Platforms (V10): not stated
  - Markdown forms claimed (V13): not stated; (b) not stated
  - Features the questions ask about: V28 to V33 and V14 all not stated
- **Charges.** not stated; (b) not stated; (c) named open-source licence ("MIT license", repository licence field)
- **Buyer's all-in cost**, from the page text: price shape (V16b) not stated; beyond the price (V17): not stated; prerequisites (V11): not stated; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): none of the three named.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): github-topics:markdown-viewer: stars=4346; archived=false; last_push=2024-06-14 || github-topics:markdown-editor: stars=4346; archived=false; last_push=2024-06-14
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** not stated; (b) not stated

## R110. QOwnNotes

Slug `qownnotes`; profile `0-comparables/products/qownnotes.md`. Registered because: top five in alternativeto:Obsidian by likes (3 of 30 eligible comparables with a figure; 104). Cells: alternativeto:Obsidian; Flathub; Snap Store.

- **Publishes about itself.**
  - Kind (V08): desktop application :: "desktop-application"; "Native application" flathub.org www.qownnotes.org
  - Reader or editor (V09): editor with rendered view :: "markdown highlighting of notes and a markdown preview"; "tabbing support for editing notes" raw.githubusercontent.com
  - Platforms (V10): Linux :: "for GNU/Linux, macOS and Windows" ; macOS ; Windows ; BSD :: "Install on FreeBSD" raw.githubusercontent.com www.qownnotes.org
  - Markdown forms claimed (V13): wiki-links :: "optional wiki-style note links like `[[Note]]`" ; tables :: "Auto-format Markdown tables" (title) raw.githubusercontent.com www.qownnotes.org; (b) not stated
  - Features the questions ask about: navigation V28: folding of sections :: "heading folding" raw.githubusercontent.com | find V29: undecidable (see notes) :: "sub-string searching of notes is possible and search results are highlighted in the notes" [clipped] | links and images V30: follows wiki-links or backlinks :: "wiki-style note links like `[[Note]]` ... backlinks" raw.githubusercontent.com | file changed elsewhere V31: reloads when the file changes on disk, stated :: "external changes of note files are watched (notes or note list are reloaded)" [clipped] | appearance V32: themes provided :: "dark mode theme support, live theme switching, and custom color modes" ; light and dark modes :: "dark mode theme [clipped] | print and export V33: share or send from the product :: "support for sharing notes on your Nextcloud / ownCloud server" raw.githubusercontent.com | files stay local V14: local by default, optional upload stated :: "All notes are stored as plain-text markdown files on your computer"; "Use sync services like [clipped]
- **Charges.** Free flathub.org ; "Free product." alternativeto.net ; "Free open source plain-text file markdown note-taking" www.qownnotes.org; (b) free ; donation or sponsorship invited, use free :: "Donate" www.qownnotes.org; (c) named open-source licence :: [clipped]
- **Buyer's all-in cost**, from the page text: price shape (V16b) free, donation or sponsorship invited, use free; beyond the price (V17): another product or subscription required, stated :: "you need to install the Tasks backend on Nextcloud or ownCloud" raw.githubusercontent.com; prerequisites (V11): runtime or interpreter named :: "Qt 5.5+ / Qt 6.0+" (under building) ; build toolchain named :: "gcc 4.8+" (under building) raw.githubusercontent.com; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): Linux, macOS, Windows.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): alternativeto:Obsidian: rank=23; page=2; 104 likes; alternatives-listed-for-this-entry=333; license=Free Open Source (GPL-2.0) || Flathub: installs_last_month=1109; favorites_count=12 || Snap Store: none given by API (find returns no install, rating or download counts).  Further: Flathub total 75,706, growth 0.95 (N2).
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** 2026-10-08 (release v26.10.3, day) api.github.com; (b) not stated

## R111. sbarex/QLMarkdown

Slug `sbarex-qlmarkdown`; profile `0-comparables/products/sbarex-qlmarkdown.md`. Registered because: top five in github-topics:markdown-viewer by stars (3 of 21 eligible comparables with a figure; 3,631); and top five in homebrew:cask by 365-day installs (2 of 44 eligible comparables with a figure; 32,911). Cells: github-topics:markdown-viewer; homebrew:cask.

- **Publishes about itself.**
  - Kind (V08): desktop application :: "QLMarkdown is a Mac OS application" ; other kind :: "a Quick Look extension for viewing Markdown files" ; terminal program :: [clipped]
  - Reader or editor (V09): undecidable (see notes) :: "not intended to be used as a standalone markdown file editor or viewer" ; "The window interface has an inline editor to [clipped]
  - Platforms (V10): macOS :: "Requirements: macOS >= 12" formulae.brew.sh
  - Markdown forms claimed (V13): callouts or admonitions :: "GitHub alert", "MKDocs Admonition" ; math :: "Math" (MathJax) ; diagrams :: "Mermaid" ; syntax-highlighted code blocks :: "Syntax highlighting" ; wiki-links :: "Wikilinks" [clipped]
  - Features the questions ask about: links and images V30: shows local images :: "Inline local images: embed the image files inside the formatted output" raw.githubusercontent.com | appearance V32: themes provided :: "You can choose a CSS theme to render the Markdown file." ; custom stylesheet :: "You can also use a style to extend the [clipped] | print and export V33: export to HTML :: "a command-line executable for converting Markdown files to HTML" raw.githubusercontent.com
- **Charges.** not stated; (b) not stated; (c) named open-source licence :: "GNU General Public License v3.0" (repository licence field) github.com
- **Buyer's all-in cost**, from the page text: price shape (V16b) not stated; beyond the price (V17): not stated; prerequisites (V11): minimum operating-system version named :: "Requirements: macOS >= 12" formulae.brew.sh; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): macOS.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): github-topics:markdown-viewer: stars=3631; archived=false; last_push=2026-10-04 || homebrew:cask: 30d=2,087; 90d=8,552; 365d=32,911.  Further: GitHub sbarex/QLMarkdown: not archived; last push 2026-10-04; newest release 1.5.7 on 2026-10-02; 9 releases in the last 365 days, 232,974 downloads (N5). Homebrew growth 0.76 (N1).
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** 2026-10-02 (release 1.5.7, day) releases API; (b) not stated

## R112. Simplenote

Slug `simplenote`; profile `0-comparables/products/simplenote.md`. Registered because: top five in alternativeto:Obsidian by likes (2 of 30 eligible comparables with a figure; 612). Cells: alternativeto:Obsidian.

- **Publishes about itself.**
  - Kind (V08): desktop application ["the official Simplenote desktop app for Windows and Linux" | README] ; mobile application ["Get Simplenote now for iOS, [clipped]
  - Reader or editor (V09): editor with rendered view ["Write, preview, and publish your notes in Markdown format." | simplenote.com]
  - Platforms (V10): iOS ; Android ; macOS ["Mac"] ; Windows ; Linux [all: "Get Simplenote now for iOS, Android, Mac, Windows, Linux, or in your browser." | [clipped]
  - Markdown forms claimed (V13): markdown named, no form named ["Markdown support" | simplenote.com, Flathub]; (b) not stated
  - Features the questions ask about: find V29: undecidable ["quickly search for your content" (Flathub) ; "Add tags to find notes quickly with instant searching." (simplenote.com)]: [clipped] | print and export V33: share or send from the product ["you can share a note for collaboration or publish your notes online" | Flathub]
- **Charges.** Free [flathub.org/apps/com.simplenote.Simplenote] ; "It’s free: Apps, backups, syncing, sharing – it’s all completely free." [simplenote.com] ; "Free — the simplest way to keep notes" [simplenote.com]; (b) free; (c) named open-source licence: [clipped]
- **Buyer's all-in cost**, from the page text: price shape (V16b) free; beyond the price (V17): not stated; prerequisites (V11): not stated; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): Linux, macOS, Windows.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): alternativeto:Obsidian: rank=13; page=2; 612 likes; alternatives-listed-for-this-entry=199; license=Free Open Source (GPL-2.0); alerts=Discontinued
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** 2026-07-03 (release v2.27.2-md-editor-wysiwyg.1; day) [releases list]; (b) not stated

## R113. SiYuan

Slug `siyuan`; profile `0-comparables/products/siyuan.md`. Registered because: top five in alternativeto:Obsidian by likes (5 of 30 eligible comparables with a figure; 85); and top five in alternativeto:Typora by likes (5 of 62 eligible comparables with a figure; 85). Cells: alternativeto:Typora; alternativeto:Obsidian; Flathub.

- **Publishes about itself.**
  - Kind (V08): mobile application ["Android/iOS/HarmonyOS App" | raw.githubusercontent.com/siyuan-note/siyuan/HEAD/README.md] ; browser extension ["Chrome/Edge [clipped]
  - Reader or editor (V09): editor with rendered view ["Editor: Block-style, Markdown WYSIWYG" | raw.githubusercontent.com/siyuan-note/siyuan/HEAD/README.md]
  - Platforms (V10): Windows ["Available for Windows" | b3log.org/siyuan/en/] ; macOS ["desktop installation package on Windows or macOS" | README] ; Linux ["Tags: linux [clipped]
  - Markdown forms claimed (V13): markdown named, no form named ["Markdown WYSIWYG" | raw.githubusercontent.com/siyuan-note/siyuan/HEAD/README.md]; (b) not stated
  - Features the questions ask about: navigation V28: outline, contents or headings sidebar ["List outline" | README ; "document outline" | b3log.org/siyuan/en/] ; folding of sections [clipped] | find V29: undecidable ["The backlink panel supports filtering and searching"]: scope is the backlink panel, not named as document, files or folder | links and images V30: follows wiki-links or backlinks ["Block-level reference and two-way links" ; "Backlinks reflect bidirectional link value."] | print and export V33: export to PDF ["PDF, Word and HTML"] ; export to HTML [same] ; export to another named format ["Word" ; "Standard Markdown with assets"] [clipped] | files stay local V14: local by default, optional upload stated ["Data is stored entirely on the device under the control of the user. Even if there is no [clipped]
- **Charges.** Free [Flathub] ; "Most features are free, even for commercial use." [README] ; "Free: Local storage Completely free $0 Lifetime" ; "PRO Features One-time $64 Lifetime $96" ; "Subscription 8GB cloud $148 Lifetime $296" [clipped]
- **Buyer's all-in cost**, from the page text: price shape (V16b) free with paid tier or features, README], one-time purchase, subscription; beyond the price (V17): another product or subscription required, stated ["No storage included, Third-party service required" | b3log.org/siyuan/en/pricing.html]; prerequisites (V11): not stated; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): Linux, macOS, Windows; work use (V18): commercial or work use free, stated ["Most features are free, even for commercial use." | raw.githubusercontent.com/siyuan-note/siyuan/HEAD/README.md].
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): alternativeto:Typora: rank=5; page=1; 85 likes; alternatives-listed-for-this-entry=not shown; license=Freemium Open Source (AGPL-3.0) || alternativeto:Obsidian: rank=19; page=2; 85 likes; alternatives-listed-for-this-entry=not shown; license=Freemium Open Source (AGPL-3.0) || Flathub: installs_last_month=587; favorites_count=19
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** 2026-10-07 (release v3.8.7-alpha.6; day) [releases list]; (b) not stated

## R114. StackEdit

Slug `stackedit`; profile `0-comparables/products/stackedit.md`. Registered because: top five in alternativeto:Glow by likes (4 of 27 eligible comparables with a figure; 91); and top five in alternativeto:Marked (AlternativeTo entry for Marked) by likes (4 of 32 eligible comparables with a figure; 91); and top five in alternativeto:Typora by likes (4 of 62 eligible comparables with a figure; 91). Cells: alternativeto:Typora; alternativeto:Marked (AlternativeTo entry for Marked); alternativeto:Glow.

- **Publishes about itself.**
  - Kind (V08): service ["In-browser Markdown editor" | stackedit.io/] ; component ["Embed StackEdit in any website with stackedit.js" | [clipped]
  - Reader or editor (V09): editor with rendered view ["Rich Markdown editor" ; "Live preview with Scroll Sync" | stackedit.io/]
  - Platforms (V10): not stated
  - Markdown forms claimed (V13): other named flavour ["Markdown Extra" | stackedit.io/] ; GitHub Flavored Markdown ["GFM"] ; CommonMark ["CommonMark"] ; math ["LaTeX mathematical expressions"] ; diagrams ["UML diagrams"] (site: [clipped]
  - Features the questions ask about: navigation V28: scroll position kept or synchronised ["Scroll Sync feature accurately binds the scrollbars of the editor panel and the preview panel" | [clipped] | file changed elsewhere V31: preview updates as you type inside the product, stated ["Live preview with Scroll Sync" | stackedit.io/] | print and export V33: export to HTML ["upload in Markdown format, HTML" | stackedit.io/] ; share or send from the product ["publish them as blog posts to [clipped] | files stay local V14: undecidable ["Write offline!" ; "StackEdit can sync your files with Google Drive, Dropbox and GitHub." | stackedit.io/]: an optional sync [clipped]
- **Charges.** not stated; (b) not stated; (c) named open-source licence: Apache License ["Licensed under an Apache License" | site footer ; license field Apache-2.0]
- **Buyer's all-in cost**, from the page text: price shape (V16b) not stated; beyond the price (V17): not stated; prerequisites (V11): not stated; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): none of the three named.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): alternativeto:Typora: rank=14; page=2; 91 likes; alternatives-listed-for-this-entry=94; license=Free Open Source (Apache-2.0); alerts=Discontinued || alternativeto:Marked (AlternativeTo entry for Marked): rank=7; page=1; 91 likes; alternatives-listed-for-this-entry=94; license=Free Open Source (Apache-2.0); alerts=Discontinued || alternativeto:Glow: rank=4; page=1; 91 likes; alternatives-listed-for-this-entry=94; license=Free Open Source (Apache-2.0); alerts=Discontinued
- **Whom its pages address (V05):** Writers and authors ["Designed for web writers" | stackedit.io/]
- **Last release and maintenance (V27):** 2019-07-02 (release v5.14.0; day) [releases list]; (b) not stated

## R115. Taio - Markdown & Text Actions

Slug `taio-markdown-text-actions`; profile `0-comparables/products/taio-markdown-text-actions.md`. Registered because: top five in Mac App Store by rating count (1 of 134 eligible comparables with a figure, 36 of them non-zero; 658). Cells: Mac App Store.

- **Publishes about itself.**
  - Kind (V08): desktop application [“A modern app for text processing on iPhone, iPad, and Mac” apps.apple.com]; mobile application [same sentence, “app ... on [clipped]
  - Reader or editor (V09): editor, rendered view not stated [“a full-fledged Markdown editor” apps.apple.com]
  - Platforms (V10): iOS [“iPhone Requires iOS 15.0 or later” apps.apple.com]; iPadOS [“iPad Requires iPadOS 15.0 or later”]; macOS [“Mac Requires macOS 12.0 or later”]
  - Markdown forms claimed (V13): CommonMark [“supports `CommonMark` and `GitHub Flavored` standards” apps.apple.com]; GitHub Flavored Markdown [same]; math [“Math formulas and diagrams” apps.apple.com]; diagrams [same]; wiki-links [clipped]
  - Features the questions ask about: navigation V28: outline, contents or headings sidebar [“Outline view” apps.apple.com] | find V29: search within the document [“in-document search” apps.apple.com]; undecidable [“Full text search” apps.apple.com: no scope named, sentence [clipped] | appearance V32: themes provided [“Multiple color themes” apps.apple.com] | files stay local V14: undecidable [“Saved records can be synchronized across your iOS devices using iCloud” apps.apple.com: a sync mention with no statement that [clipped]
- **Charges.** “Free · In‑App Purchases”; “Taio Pro Monthly $1.49”; “Taio Pro Yearly $14.99”; “Taio Pro Lifetime $37.99” (other listed: $11.99 yearly, $29.99 and $46.99 lifetime, $10.49 yearly) [apps.apple.com]; “Basic Forever Free”; “Pro From $1.49 with free [clipped]
- **Buyer's all-in cost**, from the page text: price shape (V16b) free with paid tier or features, subscription, one-time purchase, “pay once”], free trial, then paid; beyond the price (V17): not stated; prerequisites (V11): minimum operating-system version named [“iPhone Requires iOS 15.0 or later. iPad Requires iPadOS 15.0 or later. ... Mac Requires macOS 12.0 or [clipped]; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): macOS.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): Mac App Store: userRatingCount=658; averageUserRating=4.56383.  Further: Mac App Store, 658 ratings, average 4.56, current version 2023-09-13 (N6). Reviews quoted in N6 say the app has had no update in two years.
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** “09/13/2023” (day; listing “Version 1.68.0 09/13/2023”); (b) not stated

## R116. ThisIs-Developer/Markdown-Viewer

Slug `thisis-developer-markdown-viewer`; profile `0-comparables/products/thisis-developer-markdown-viewer.md`. Registered because: top five in github-topics:markdown-preview by stars (1 of 5 eligible comparables with a figure; 527). Cells: github-topics:markdown-viewer; github-topics:markdown-editor; github-topics:markdown-preview.

- **Publishes about itself.**
  - Kind (V08): service [“the hosted web app” README]; desktop application [“the Neutralino desktop application” README]
  - Reader or editor (V09): editor with rendered view [“switch among Editor, Split view, and Preview” and “A local-first Markdown editor and viewer with live preview.” README]
  - Platforms (V10): not stated
  - Markdown forms claimed (V13): CommonMark [“CommonMark-style Markdown” README Highlights]; GitHub Flavored Markdown [“GitHub-Flavored Markdown (GFM)”]; tables [“tables”]; task lists [“task lists”]; footnotes [“footnotes”]; math [clipped]
  - Features the questions ask about: navigation V28: outline, contents or headings sidebar [“Document Outline ... a resizable right sidebar with collapsible heading branches” README]; jump to [clipped] | find V29: find and replace [“Find and Replace” markdownviewer.pages.dev]; search across files or a folder [“Search files” app page Explorer] | links and images V30: shows remote images [“External images, media, links, and map tiles / The referenced external host” README Local and Network Behavior] | file changed elsewhere V31: preview updates as you type inside the product, stated [“live preview” README] | appearance V32: light and dark modes [“remembered Light or Dark appearance” README] | print and export V33: print [“Browser Print/Save as PDF” README]; export to PDF [“a legacy raster PDF” README]; export to HTML [“standalone HTML” README]; export [clipped] | files stay local V14: local by default, optional upload stated [“Everyday editing stays on your device.” README; “Diagram source can be sent to PlantUML, Kroki, [clipped]
- **Charges.** not stated; (b) not stated; (c) named open-source licence: “Apache-2.0 license”; “Markdown Viewer is licensed under the Apache License 2.0.” [README]
- **Buyer's all-in cost**, from the page text: price shape (V16b) not stated; beyond the price (V17): own API key or service account required, stated [“optional PAT” for private repositories, README; feature-scoped, quote elided in profile]; prerequisites (V11): runtime or interpreter named [“python -m http.server 8080 ... Do not rely on file://” README Quick Start; local-server route only]; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): none of the three named.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): github-topics:markdown-viewer: stars=527; archived=false; last_push=2026-10-09 || github-topics:markdown-editor: stars=527; archived=false; last_push=2026-10-09 || github-topics:markdown-preview: stars=527; archived=false; last_push=2026-10-09
- **Whom its pages address (V05):** Developers and coders; Writers and authors; Students and academics [“an open source, local-first workspace for developers, writers, students, researchers, and anyone working with .md or .markdown [clipped]
- **Last release and maintenance (V27):** not stated [repository fields “985 Commits” carry no date]; (b) not stated

## R117. Tinta

Slug `tinta`; profile `0-comparables/products/tinta.md`. Registered because: top five in github-topics:markdown-preview by stars (5 of 5 eligible comparables with a figure; 205); and top five in github-topics:markdown-reader by stars (5 of 5 eligible comparables with a figure; 205). Cells: alternativeto:Typora; github-topics:markdown-viewer; github-topics:markdown-editor; github-topics:markdown-preview; github-topics:markdown-reader.

- **Publishes about itself.**
  - Kind (V08): desktop application [“Markdown and Mermaid viewer for Windows ... A single native executable” README]
  - Reader or editor (V09): editor with rendered view [“with an edit mode when you need it” README; “Press : to edit: your raw Markdown on the left with the rendered page [clipped]
  - Platforms (V10): Windows [“for Windows” README]
  - Markdown forms claimed (V13): CommonMark [“MD4C CommonMark+GFM” tinta.cc]; GitHub Flavored Markdown [same]; math [“Native LaTeX math - $inline$ and $$display$$ equations” README]; diagrams [“Native Mermaid diagrams” README]; [clipped]
  - Features the questions ask about: navigation V28: outline, contents or headings sidebar [“Table of contents - Press Tab to see document headings” README]; jump to heading or section [“click [clipped] | find V29: search within the document [“Find text with F or Ctrl+F” README]; find and replace [“Ctrl+H Find and replace (in edit mode)” README] | links and images V30: follows links to other markdown files inside the product [“Plain-text paths like docs/plan.md become real links: live targets open as tabs” [clipped] | file changed elsewhere V31: preview updates as you type inside the product, stated [“Edit mode Split view, live preview” tinta.cc] | appearance V32: themes provided [“10 beautiful themes” README]; light and dark modes [“5 light and 5 dark themes to choose from” README]; font or size [clipped] | print and export V33: print [“Ctrl+P Print / export to PDF” README]; export to PDF [“Export as HTML, DOCX, or PDF” README]; export to HTML [same]; export to [clipped]
- **Charges.** “Free, open source, MIT licensed.” [tinta.cc]; (b) free; (c) named open-source licence: “MIT licensed” [tinta.cc]; “MIT license” [github.com licence field]
- **Buyer's all-in cost**, from the page text: price shape (V16b) free; beyond the price (V17): not stated; prerequisites (V11): none needed, stated [“Zero dependencies tinta.exe No runtime, no frameworks: one executable.” tinta.cc]; build toolchain named [“Requires Windows [clipped]; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): Windows.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): alternativeto:Typora: rank=58; page=5; 3 likes; alternatives-listed-for-this-entry=not shown; license=Free Open Source (MIT) Origin Croatia EU Platforms Windows Croatia EU More about Tinta [clipped] || github-topics:markdown-viewer: stars=205; archived=false; last_push=2026-10-08 || github-topics:markdown-editor: stars=205; archived=false; last_push=2026-10-08 || github-topics:markdown-preview: stars=205; archived=false; last_push=2026-10-08 || github-topics:markdown-reader: stars=205; archived=false; last_push=2026-10-08
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** not stated [“226 Commits” repository field, no release date]; (b) not stated

## R118. tw93/MiaoYan

Slug `tw93-miaoyan`; profile `0-comparables/products/tw93-miaoyan.md`. Registered because: top five in github-topics:markdown-editor by stars (5 of 84 eligible comparables with a figure; 8,669). Cells: github-topics:markdown-editor; homebrew:cask.

- **Publishes about itself.**
  - Kind (V08): desktop application [“Lightweight Markdown note-taking app for macOS” README]; mobile application [“includes the iPhone and iPad app” README [clipped]
  - Reader or editor (V09): editor with rendered view [“split editor & preview” README; “Markdown editor” formulae.brew.sh]
  - Platforms (V10): macOS [“Requires macOS 12.0 or later.” miaoyan.app]
  - Markdown forms claimed (V13): wiki-links [“Wikilinks and backlinks” miaoyan.app]; math [“LaTeX” miaoyan.app]; diagrams [“Mermaid” miaoyan.app]; (b) not stated
  - Features the questions ask about: navigation V28: scroll position kept or synchronised [“60fps bidirectional scroll sync” miaoyan.app] | find V29: search across files or a folder [“miao search <query> # Search notes in terminal” README CLI] | file changed elsewhere V31: preview updates as you type inside the product, stated [“Split mode pairs real-time preview” miaoyan.app] | appearance V32: light and dark modes [“Dark mode, distraction-free writing” miaoyan.app] | files stay local V14: local, stated [“Your Markdown files stay in a folder you choose. MiaoYan does not collect note data” miaoyan.app; “It reads and writes the [clipped]
- **Charges.** “Mac App Store (paid, automatic updates, includes the iPhone and iPad app)” [README, no amount]; (b) undecidable [“paid” names no amount, period or shape, so no V16(b) value fits; price of the Homebrew and GitHub builds is silent]; (c) named [clipped]
- **Buyer's all-in cost**, from the page text: price shape (V16b) undecidable; beyond the price (V17): not stated; prerequisites (V11): minimum operating-system version named [“Requires macOS 12.0 or later.” miaoyan.app; “Requirements: macOS >= 12” formulae.brew.sh]; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): macOS.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): github-topics:markdown-editor: stars=8669; archived=false; last_push=2026-10-09 || homebrew:cask: 30d=86; 90d=482; 365d=1,971
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** not stated [“Current version: 4.5.0” no date]; (b) not stated

## R119. Typora

Slug `typora-typora`; profile `0-comparables/products/typora-typora.md`. Registered because: top five in alternativeto:Glow by likes (1 of 27 eligible comparables with a figure; 334); and top five in alternativeto:Marked (AlternativeTo entry for Marked) by likes (1 of 32 eligible comparables with a figure; 334). Cells: alternativeto:Marked (AlternativeTo entry for Marked); alternativeto:Glow; homebrew:cask; Snap Store.

- **Publishes about itself.**
  - Kind (V08): desktop application [“Typora is available on macOS, Windows, and Linux” store.typora.io]
  - Reader or editor (V09): editor with rendered view [“a seamless experience as both a reader and a writer” and “Live Preview Preview while you are typing.” typora.io]
  - Platforms (V10): macOS [“Typora is available on macOS, Windows, and Linux” store.typora.io]; Windows [same]; Linux [same]
  - Markdown forms claimed (V13): tables [“Tables” typora.io]; math [“Mathematics” typora.io]; diagrams [“Diagrams”, “Mermaid” typora.io]; task lists [“GFM task list supported.” typora.io]; GitHub Flavored Markdown [same phrase]; [clipped]
  - Features the questions ask about: navigation V28: outline, contents or headings sidebar [“Outline Panel” typora.io; “Table of Contents Type `[TOC]` to insert table of contents”, inserted]; [clipped] | links and images V30: follows links to headings within the document [“Set the href to headers, which will create a bookmark that allow you to jump to that [clipped] | file changed elsewhere V31: preview updates as you type inside the product, stated [“Live Preview Preview while you are typing.” typora.io] | appearance V32: custom stylesheet [“Customized Styles Use your own css code” typora.io] | print and export V33: export to PDF [“Export to PDF with bookmarks.” typora.io]; export to another named format [“docx, OpenOffice, LaTeX, MediaWiki, Epub” [clipped]
- **Charges.** “15 days free trial / up to 3 devices”; “$ 14.99 (without tax) x 1” [typora.io]; “Typora license is a one-time purchase, no subscription or renewal fee is required.” [store.typora.io]; (b) one-time purchase [same quote]; free trial, then paid [“15 [clipped]
- **Buyer's all-in cost**, from the page text: price shape (V16b) one-time purchase, free trial, then paid; beyond the price (V17): not stated; prerequisites (V11): minimum operating-system version named [“Requires Windows 10, 11.” typora.io]; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): Linux, macOS, Windows; work use (V18): undecidable [“We currently do not offer bulk license (one license code that can activate large amount of devices) ... you will need to buy multiple [clipped].
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): alternativeto:Marked (AlternativeTo entry for Marked): rank=1; page=1; 334 likes; alternatives-listed-for-this-entry=221; license=Paid Proprietary || alternativeto:Glow: rank=1; page=1; 334 likes; alternatives-listed-for-this-entry=221; license=Paid Proprietary || homebrew:cask: 30d=605; 90d=2,545; 365d=12,014 / 30d=2; 90d=12; 365d=79 || Snap Store: none given by API (find returns no install, rating or download counts).  Further: GitHub typora/typora-issues is an issues repository: no releases, last push 2025-07-25, 1,097 open issues (N5). Homebrew growth 0.60 (N1).
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** “1 August 2026” (day; snapcraft.io “Last updated 1 August 2026 - latest/stable”); (b) not stated

## R120. vaibhav-kakde-in/mdhero

Slug `vaibhav-kakde-in-mdhero`; profile `0-comparables/products/vaibhav-kakde-in-mdhero.md`. Registered because: top five in github-topics:markdown-preview by stars (3 of 5 eligible comparables with a figure; 252); and top five in github-topics:markdown-reader by stars (4 of 5 eligible comparables with a figure; 252). Cells: github-topics:markdown-viewer; github-topics:markdown-editor; github-topics:markdown-preview; github-topics:markdown-reader; homebrew:cask.

- **Publishes about itself.**
  - Kind (V08): desktop application ("A beautiful, native Markdown viewer and lightweight editor for macOS, Windows and Linux", github.com)
  - Reader or editor (V09): editor with rendered view ("Split puts the editor and a live preview side by side", mdhero.app; "Cmd+E flips any local file into edit mode", [clipped]
  - Platforms (V10): macOS ("macOS 12+ (Apple Silicon)", mdhero.app); Windows ("Windows 10+ (x64 or ARM64)", mdhero.app); Linux ("Linux (x64 or arm64)", github.com)
  - Markdown forms claimed (V13): (a) math ("KaTeX for equations", github.com); diagrams ("Mermaid for flowcharts", github.com); syntax-highlighted code blocks ("Syntax highlighting — 25+ languages via highlight.js", github.com); [clipped]
  - Features the questions ask about: navigation V28: outline, contents or headings sidebar ("Table of Contents — auto-generated sidebar with active heading tracking", github.com) | find V29: undecidable: "Search (Cmd+F) — with match highlighting" (github.com) names no scope and is not worded about the open document | file changed elsewhere V31: both stated ("File watching — edit in VS Code, see updates instantly in MDHero", github.com; "Split puts the editor and a live preview side [clipped] | appearance V32: themes provided ("light & dark themes", github.com); light and dark modes ("light & dark themes", github.com); font or size choice ("adjust [clipped] | print and export V33: print ("File › Print or Cmd/Ctrl+P opens the native print dialog", github.com); export to PDF ("Print/Export to PDF", github.com); copy as [clipped] | files stay local V14: local by default, optional upload stated ("Your files never leave your computer." github.com; optional: "Select a word or paragraph and [clipped]
- **Charges.** (a) "Free. Open source." (github.com); "free forever, MIT-licensed, ~8MB, runs entirely offline. No paid tier, no account, no upgrade nag." (mdhero.app) (b) free; donation or sponsorship invited, use free ("Sponsor this project", github.com) (c) [clipped]
- **Buyer's all-in cost**, from the page text: price shape (V16b) free, donation or sponsorship invited, use free; beyond the price (V17): not stated; prerequisites (V11): minimum operating-system version named ("Windows 10+", "macOS 12+", mdhero.app; "macOS >= 12", formulae.brew.sh); runtime or interpreter named ("Node [clipped]; platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): Linux, macOS, Windows.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): github-topics:markdown-viewer: stars=252; archived=false; last_push=2026-10-08 || github-topics:markdown-editor: stars=252; archived=false; last_push=2026-10-08 || github-topics:markdown-preview: stars=252; archived=false; last_push=2026-10-08 || github-topics:markdown-reader: stars=252; archived=false; last_push=2026-10-08 || homebrew:cask: 30d=208; 90d=208; 365d=208
- **Whom its pages address (V05):** Developers and coders ("Markdown is where developers, writers, and AI live today", github.com); Writers and authors (same quote); the sentence is about markdown's users, not worded as the product's [clipped]
- **Last release and maintenance (V27):** (a) not stated (version "v0.2.10" is given without a date, mdhero.app, formulae.brew.sh); (b) not stated

## R121. vorojar/md-preview

Slug `vorojar-md-preview`; profile `0-comparables/products/vorojar-md-preview.md`. Registered because: top five in github-topics:markdown-preview by stars (2 of 5 eligible comparables with a figure; 273). Cells: github-topics:markdown-viewer; github-topics:markdown-preview.

- **Publishes about itself.**
  - Kind (V08): desktop application ("built with Rust and the system WebView on desktop", github.com; Windows and Linux downloads); mobile application ("Android [clipped]
  - Reader or editor (V09): editor with rendered view ("Cmd/Ctrl+E switches to source mode; edits autosave", github.com; "Markdown previewer and quick editor", github.com)
  - Platforms (V10): Windows ("Windows MD-Preview-windows-x64.exe", download table, github.com); Linux ("Linux MD-Preview-linux-x64.tar.gz", github.com); Android [clipped]
  - Markdown forms claimed (V13): (a) CommonMark ("CommonMark plus GFM-style tables"); GitHub Flavored Markdown ("GFM-style tables", the abbreviation "GFM" used as a style); tables; task lists; front matter ("Readable YAML front [clipped]
  - Features the questions ask about: navigation V28: scroll position kept or synchronised ("Scroll continuity: Preview and source edit preserve normalized reading progress", github.com) | find V29: search within the document ("Find in preview: Cmd/Ctrl+F opens a compact search bar for the rendered document.", github.com) | links and images V30: follows links to other markdown files inside the product ("Relative or absolute links to existing Markdown and text files open or activate [clipped] | file changed elsewhere V31: reloads when the file changes on disk, stated ("External edits refresh the rendered document automatically.", github.com) | appearance V32: light and dark modes ("Dark mode: Follows the system color scheme across macOS, Windows, and Linux.", github.com); follows the system [clipped] | print and export V33: print ("Native print: Cmd/Ctrl+P opens the platform print dialog", github.com); export to PDF ("Print or export the rendered preview when [clipped] | files stay local V14: local, stated ("Your Markdown files stay on disk. Rendering happens locally.", github.com)
- **Charges.** (a) not stated (b) not stated (c) named open-source licence: "MIT" (github.com, License section and licence field)
- **Buyer's all-in cost**, from the page text: price shape (V16b) not stated; beyond the price (V17): not stated; prerequisites (V11): runtime or interpreter named ("Linux: Requires the system WebKitGTK runtime.", github.com); platform the buyer must already hold, among the operator's Linux, macOS and Windows (V10): Linux, macOS, Windows.
- **Demand signal** (frame list rows read 2026-10-09; counts as each list publishes them, never compared across lists): github-topics:markdown-viewer: stars=273; archived=false; last_push=2026-09-19 || github-topics:markdown-preview: stars=273; archived=false; last_push=2026-09-19
- **Whom its pages address (V05):** not stated
- **Last release and maintenance (V27):** (a) not stated (b) not stated

# The demand signals, in the method's five kinds

Reading, text generator against product designer: a generator would add the figures of one column to say how big the market is; a designer sees that each cell counts a different act (an install, a star, a like, a rating) on a different surface, and keeps them in their cells.

## D1. Which buyers already go where

Store counts by cell, from the frame lists (read 2026-10-09) and the distributor notes (all fetched 2026-10-09). The five largest per cell, as published, with the section of each:

| cell | figure | five largest, as the list publishes (section) |
|---|---|---|
| Flathub | installs last month | Apostrophe 5,267 (R88); MarkText 3,370 (R103); marknote 2,371 (R102); ghostwriter 1,827 (R93); Manuscript 1,763 (R97) |
| Mac App Store | rating count | Taio - Markdown & Text Actions 658 (R115); Markdown゜ 484 (R100); MWeb 153 (R105); One Markdown 148 (R108); Read.md 84 (R73) |
| alternativeto:Typora | likes | Joplin 947 (R95); MarkText 122 (R103); ghostwriter 116 (R93); StackEdit 91 (R114); SiYuan 85 (R113) |
| alternativeto:Obsidian | likes | Joplin 947 (R95); Simplenote 612 (R112); QOwnNotes 104 (R110); Bear 102 (R89); SiYuan 85 (R113) |
| alternativeto:Marked (AlternativeTo entry for Marked) | likes | Typora 334 (R119); MarkText 122 (R103); ghostwriter 116 (R93); StackEdit 91 (R114); Haroopad 68 (R94) |
| alternativeto:Glow | likes | Typora 334 (R119); MarkText 122 (R103); ghostwriter 116 (R93); StackEdit 91 (R114); Haroopad 68 (R94) |
| github-topics:markdown-editor | stars | doocs/md 13,409 (R91); codexu/note-gen 12,882 (R90); MacDown 9,835 (R96); genspark-ai/genoffice 9,042 (R92); tw93/MiaoYan 8,669 (R118) |
| github-topics:markdown-viewer | stars | MacDown 9,835 (R96); pd4d10/hashmd 4,346 (R109); sbarex/QLMarkdown 3,631 (R111); Textualize/frogmouth 3,307 (R82); d0c-s4vage/lookatme 2,332 (R3) |
| github-topics:markdown-preview | stars | ThisIs-Developer/Markdown-Viewer 527 (R116); vorojar/md-preview 273 (R121); vaibhav-kakde-in/mdhero 252 (R120); selimacerbas/mdkite.nvim 227 (R77); Tinta 205 (R117) |
| github-topics:markdown-reader | stars | richardr1126/openreader 539 (R75); alexishida/Moji 493 (R87); md-reader/md-reader 475 (R50); vaibhav-kakde-in/mdhero 252 (R120); Tinta 205 (R117) |
| homebrew:cask | 365-day installs | obsidian 194,535 (R106); sbarex/QLMarkdown 32,911 (R111); mark-text 22,164 (R98); MacDown 17,571 (R96); MarkEdit 17,031 (R101) |
| homebrew:formula | 365-day installs | Glow 59,634 (R9); grip 5,370 (R10); mdcat 5,360 (R54); mcat 3,125 (R47); mdless 2,710 (R56) |
| vscode | installs | Markdown All in One 14,704,347 (R99); Markdown Preview Enhanced 10,429,484 (R24); Office Viewer 1,556,537 (R107); Marp for VS Code 871,866 (R104); Preview 787,184 (R68) |

From the distributor notes, for the same cells and for sources that are not frame cells:

- Homebrew (N1): opt-in analytics, 365-day counts; among formulae glow is far ahead of the other terminal readers, and the casks lead with obsidian. The reader-shaped entries that are new inside the year (leaf-markdown-viewer, markdown-preview, markviewer, mdhero, markpad, telari) and the biggest names running at or below their twelve-month average are set out in N1; Homebrew marks mark-text and macdown disabled while their counts persist.
- Flathub (N2): 48 search hits, last-month installs from Apostrophe at 5,267 downward; the entry described as reading ("Read and edit Markdown files") is Manuscript, first listed 2026-03-25.
- VS Code Marketplace (N3): a top-100 cut of 4,720; the markdown-specific entries are mostly helpers to the built-in preview, and 32 of the 100 were last updated more than two years before 2026-10-09.
- Mac App Store (N6): 170 results, 54 with any rating; Read.md is the only entry in the top eleven described as a reader by name.
- PyPI (N4, not a frame cell): grip 30,167 downloads last month, rich-cli 22,138, mdv 2,510, frogmouth 1,232; grip, mdv and frogmouth have had no release in over two years.
- GitHub releases (N5, not a frame cell): release-asset downloads over the last 365 days are given per repository in the sections' "Further" clauses; the viewer-shaped repositories releasing this year are in the thousands to tens of thousands, Obsidian's 35.9 million being a notes workspace.
- No demand figure exists in the frame for the Snap Store, the Ubuntu archive, awesome-claude-code or the Tcl wiki lists; the register draws no five from them. The Chrome Web Store list does publish rounded users (Markdown Viewer 500,000; Markdown Reader 100,000; Markdown Here 100,000) and rating counts, but that cell is no-go in the frame review, so none of these is a section here.

Cross-source reading (N7): these counts differ from the operator's shape on reach, payment before reach and sale, except the GitHub release counts and the free rows of the first three; none says how many people use a reader.

## D2. What buyers pay all-in

One row per section. "Price shape" is V16(b), "price as published" V16(a) clipped, "beyond the price" V17, "prerequisite" the kind of V11, "platform held" the operator's platforms named in V10. The full cells are in each section. Nothing in the corpus states a price for the operator's own viewer; the operator charges nothing and has no mechanism to charge (capability note).

| section | product | price shape (V16b) | price as published (V16a) | beyond the price (V17) | prerequisite (V11) | platform held |
|---|---|---|---|---|---|---|
| R1 | Auto-Open Markdown Preview | free | Free (marketplace.visualstudio.com price field) | not stated | host program named | none of the three |
| R2 | bookmark.md | free | Free (apps.apple.com price field) | not stated | minimum operating-system version named | macOS |
| R3 | d0c-s4vage/lookatme | not stated | not stated | not stated | undecidable | Linux |
| R4 | ekphos | not stated | not stated | not stated | build toolchain named | Linux, macOS |
| R5 | Essentialist | free | "Free" [@flathub label] | not stated | not stated | Linux, macOS, Windows |
| R6 | FlyCrys | free | «Zero cost — no subscription, no API proxy, uses your own Claude Code CLI» (READ | another product or subscription required, stated | runtime or interpreter named | Linux |
| R7 | Folio: Markdown+RST+Code+PDF | free with paid tier or features, one-time purchase, subscription | «Read complete text documents up to 10 KB for free, and view PDFs and images wit | not stated | minimum operating-system version named | macOS |
| R8 | geany-plugin-markdown | not stated | not stated | not stated | host program named | none of the three |
| R9 | Glow | free | «Cost / License: Free, Open Source (MIT)» (AlternativeTo); price text on README, | not stated | build toolchain named | Linux, macOS, Windows |
| R10 | grip | not stated | not stated | not stated | runtime or interpreter named | Linux, macOS |
| R11 | ianks/octodown | not stated | not stated | not stated | runtime or interpreter named | macOS |
| R12 | inlyne | not stated | not stated | not stated | build toolchain named | Linux, macOS |
| R13 | Instant Markdown | free | Free [S1] | not stated | host program named | Linux, macOS, Windows |
| R14 | Just a Markdown Viewer | free | Free [S1]; "Free · No ads · No in-app purchases" [S2] | not stated | minimum operating-system version named | macOS |
| R15 | k1LoW/mo | not stated | not stated | not stated | build toolchain named | none of the three |
| R16 | learn-preview | free | [B] "Microsoft.VisualStudio.Services.Content.Pricing": "Free" | not stated | host program named: | none of the three |
| R17 | MacMD Viewer | one-time purchase | [B] "$19.99 one-time — no subscription, no account required."; [D] "Single $19.9 | not stated | minimum operating-system version named: | macOS |
| R18 | mandown | not stated | not stated | not stated | runtime or interpreter named: | Linux, macOS |
| R19 | marge | not stated | not stated | not stated | runtime or interpreter named: | Linux, macOS |
| R20 | Markdown Hot Reload | not stated | not stated // | not stated | runtime or interpreter named | Linux |
| R21 | Markdown Lens | free, donation or sponsorship invited, use free, one-time purchase | "free to use with all features included" [1] ; "price": 0, "priceCurrency": "USD | not stated | minimum operating-system version named | macOS |
| R22 | Markdown Peek | free | "Free to use." ; "Free on the Mac App Store" ; "price": 0, "priceCurrency": "USD | no other cost, stated | minimum operating-system version named | macOS |
| R23 | Markdown Preview - Quick Look | one-time purchase | "a one-time purchase of $1.99 USD" ; "Actual price varies based on your region." | not stated | host program named | macOS |
| R24 | Markdown Preview Enhanced | free, donation or sponsorship invited, use free | "Free" in "10,429,939 installs / (145) / Free" [1] // | not stated | host program named | none of the three |
| R25 | Markdown Reader - Ream | undecidable | \"3.99 USD\" (structured data \"price\": 3.99, \"priceCurrency\": \"USD\", P1; \ | not stated | minimum operating-system version named | macOS |
| R26 | Markdown Sticky | free with paid tier or features, \"This app offers in-app purchases fo | \"0 USD\" (structured data \"price\": 0, \"priceCurrency\": \"USD\" P1); \"$1.99 | not stated | minimum operating-system version named | macOS |
| R27 | Markdown View | not stated | not stated | not stated | not stated | Linux, macOS, Windows |
| R28 | Markdown Viewer | not stated | not stated | not stated | not stated | Linux, macOS, Windows |
| R29 | Markdown Viewer - MD QuickView | free | \"Free\"; \"0 USD\" (\"price\": 0 P1); \"Pricing Free\" (P2); \"Yes, MD QuickVie | not stated | minimum operating-system version named | macOS |
| R30 | Markdown Viewer - MD Reader | free | \"0 USD\" (\"price\": 0, \"priceCurrency\": \"USD\" P1); \"free Markdown viewer\ | not stated | minimum operating-system version named | macOS |
| R31 | Markdown Viewer Offline | free | \"0 USD\" (\"price\": 0, \"priceCurrency\": \"USD\" P1) | not stated | minimum operating-system version named | macOS |
| R32 | markdown-viewer-premium | not stated | not stated | not stated | not stated | Linux |
| R33 | markdownpart | not stated | not stated | not stated | runtime or interpreter named | Linux |
| R34 | markdowser | not stated | not stated | not stated | not stated | Linux, Windows |
| R35 | Marked | one-time purchase, free trial, then paid | \"13.99 USD\" (structured data P1); \"$14.99\" (\"remains available … for a one- | not stated | minimum operating-system version named | macOS |
| R36 | Marked QL - Markdown Preview | one-time purchase, free trial, then paid | \"9.99 USD\" (structured data P1); \"$9.99 one-time\" (\"Paddle Direct download  | not stated | minimum operating-system version named | macOS |
| R37 | MarkFlow:Read Markdown files | free with paid tier or features, subscription, \"Added yearly subscrip | \"0 USD\" (P1); \"$12.99\" (in-app purchase \"Lifetime Access\"); \"$19.99\" (\" | not stated | minimum operating-system version named | macOS |
| R38 | Marklens: Markdown Reader | free | Free [p1] | not stated | minimum operating-system version named | macOS |
| R39 | Marklet - Markdown Viewer | free | Free [p1] | not stated | minimum operating-system version named | macOS |
| R40 | MarkLook - Markdown Reader | free with paid tier or features, one-time purchase | Free · In‑App Purchases [p1]; "MarkLook完全版 $4.99" [p1]; "one-time purchase" [p1] | not stated | minimum operating-system version named | macOS |
| R41 | Markmap | free | Free [p1] | not stated | host program named | none of the three |
| R42 | Marko Viewer | free with paid tier or features | Free · In‑App Purchases [p1]; "Marko Viewer $4.99" [p1] | not stated | minimum operating-system version named | macOS |
| R43 | Marko: Markdown Viewer | free | Free [p1]; "Marko is free to use." [p2] | not stated | minimum operating-system version named | macOS |
| R44 | MarkRead - Markdown Reader | free with paid tier or features, subscription, one-time purchase | Free · In‑App Purchases [p1]; "Pro is $2.99 a month, $19.99 a year, or $48.99 ou | not stated | minimum operating-system version named | macOS |
| R45 | MarkView | free | Free to use, fork, and modify. [p2]; "price=0.0 USD" [p1] | not stated | minimum operating-system version named | Linux, Windows |
| R46 | MarkView | free | price=0.0 USD [p1] | not stated | runtime or interpreter named | Linux, macOS, Windows |
| R47 | mcat | not stated | not stated | not stated | build toolchain named | Linux, macOS |
| R48 | MD Flow - Markdown Reader | free with paid tier or features, one-time purchase, donation or sponso | Free · In‑App Purchases [p1]; "$7.99one time — not per month, not per year" [p2] | not stated | minimum operating-system version named | macOS |
| R49 | md Viewer: Markdown & Mermaid | see V16 | a: "Free"; "Free, no account." {listing}; b: free; c: not stated | undecidable {"The AI requires an Apple Intelligence-compatible [clipped] | minimum operating-system version named {"Requires macOS 26.4 | macOS |
| R50 | md-reader/md-reader | see V16 | a: not stated; b: free with paid tier or features {"the free version" and "Subsc | not stated | host program named {"Markdown Reader is a Markdown browser e | none of the three |
| R51 | md-tui | see V16 | a: not stated; b: not stated; c: named open-source licence AGPL-3.0-or-later {"L | not stated | undecidable {"### Requirements 1. A terminal 2. Nerd font" @ | Linux, macOS |
| R52 | MD-Viewer | see V16 | a: "Free" {listing; "MD Viewer Free / Free" @md-viewer.com}; b: free; c: not sta | not stated | minimum operating-system version named {"Requires macOS 10.1 | macOS, Windows |
| R53 | md2term | see V16 | a: not stated; b: not stated; c: named open-source licence "GPLv3+: GNU GPL vers | not stated | runtime or interpreter named {"Bash" under | Linux |
| R54 | mdcat | see V16 | a: not stated; b: not stated; c: named open-source licence "MPL-2.0" {"License:  | not stated | undecidable {"mdcat requires that the terminal supports stri | Linux, macOS, Windows |
| R55 | mdfried | see V16 | a: not stated; b: not stated; c: named open-source licence "GPL-3.0-or-later" {" | not stated | undecidable {"Needs a chafa package with development headers | Linux, macOS, Windows |
| R56 | mdless | see V16 | a: not stated; b: not stated; c: named open-source licence "MIT" {"License: MIT" | not stated | runtime or interpreter named {"Depends on: ruby 4.0.7" @form | Linux, macOS |
| R57 | Mdly – Markdown Viewer | see V16 | a: "$1.99" {listing}; b: undecidable ("$1.99" is a bare store price with no peri | not stated | minimum operating-system version named {"Requires iOS 18.0 o | macOS |
| R58 | mdp | see V16 | a: not stated; b: not stated; c: named open-source licence "GPL-3.0-or-later" {" | not stated | undecidable {"mdp needs the ncursesw headers to compile."; | Linux, macOS |
| R59 | mdserv | see V16 | a: not stated; b: not stated; c: undecidable {"License CNRI-Python-GPL-Compatibl | not stated | package manager named as required to install {"Don't have sn | Linux |
| R60 | mdserve | see V16 | a: not stated; b: not stated; c: named open-source licence "MIT" {"License: MIT" | not stated | none needed, stated {"No runtime dependencies to manage." @R | Linux, macOS |
| R61 | MDV | see V16 | a: "Free product" {AlternativeTo extraction, unchecked: "Licensing Proprietary a | not stated | minimum operating-system version named {"Download MDV for ma | Linux, macOS |
| R62 | Meva | see V16 | a: "Free ... $0 forever"; "Pro ... $14.99 one-time"; "Free · In‑App Purchases" [ | not stated | minimum operating-system version named {"Requires macOS 10.1 | Linux, macOS, Windows |
| R63 | mohzy83/NppMarkdownPanel | not stated | not stated | not stated | host program named | Windows |
| R64 | Mud: Mark Up or Down | free | 'Free'; 'It's free and it's open source.' [A] | not stated | minimum operating-system version named | macOS |
| R65 | Offline Markdown Preview | free | 171,442 installs / ( 2 ) / Free / "Free : no paywalls; MIT-licensed." | not stated | host program named | none of the three |
| R66 | OnePreview | free | Free (price line) / "Free app Available on the App Store." | not stated | minimum operating-system version named | macOS |
| R67 | pampi | undecidable | PAMPI is a free software (apt-cache) / "PAMPI est un logiciel libre (licence GNU | not stated | runtime or interpreter named | Linux |
| R68 | Preview | free | 787,197 installs / ( 40 ) / Free | not stated | host program named | none of the three |
| R69 | PreviewMarkdown | undecidable | $2.99 (price line) | not stated | minimum operating-system version named | macOS |
| R70 | Print | free | 740,428 installs / ( 55 ) / Free | not stated | host program named | Linux, macOS, Windows |
| R71 | qlcommonmark | not stated | not stated | not stated | not stated | macOS |
| R72 | Quick Markdown Viewer | free | Free apps.apple.com | not stated | minimum operating-system version named | macOS |
| R73 | Read.md | free with paid tier or features, one-time purchase, subscription, free | Free · In‑App Purchases ; "Read.md Pro Yearly $9.99" ; "Read.md Pro (Lifetime) $ | own API key or service account required, stated | minimum operating-system version named | macOS |
| R74 | reveal-md | not stated | not stated | not stated | runtime or interpreter named | Linux, macOS |
| R75 | richardr1126/openreader | not stated | not stated | not stated | not stated | none of the three |
| R76 | RivoLink/leaf | not stated | not stated | not stated | not stated | Linux, macOS, Windows |
| R77 | selimacerbas/mdkite.nvim | not stated | not stated | not stated | none needed, stated | macOS, Windows |
| R78 | shd101wyy/markdown-preview-enhanced | not stated | not stated | not stated | host program named | Windows |
| R79 | shiba | not stated | not stated | not stated | runtime or interpreter named | Linux, macOS, Windows |
| R80 | simov/markdown-viewer | free | Free and Open Source [README] | not stated | host program named | none of the three |
| R81 | telari | free with paid tier or features, one-time purchase, free trial, then p | “Telari is free forever.”; “Free $0 Free forever”; “Pro licence $20 One-time pur | not stated | minimum operating-system version named | macOS |
| R82 | Textualize/frogmouth | not stated | not stated | not stated | runtime or interpreter named | Linux, macOS, Windows |
| R83 | ttscoff-mmd-quicklook | not stated | not stated | not stated | host program named | macOS |
| R84 | ViewMD | one-time purchase | "$5.99" (apps.apple.com, price field); "ViewMD is a one-time purchase." | not stated | minimum operating-system version named | macOS |
| R85 | vmd | free | "Free product." (alternativeto.net); "Free" (alternativeto.net) | not stated | not stated | Linux, macOS, Windows |
| R86 | zerdo | free with paid tier or features, one-time purchase | "Free to use, with optional licensed features"; "Early Supporter License ₹199 [c | not stated | none needed, stated | Windows |
| R87 | alexishida/Moji | free | Free · open source · no account; "Moji is free and distributed under the MIT lic | not stated | none needed, stated | Linux, macOS, Windows |
| R88 | Apostrophe | free, donation or sponsorship invited, use free, "donation":"https://w | Free (flathub.org); "Open Source (GPL-3.0) and Free product." (AlternativeTo ext | not stated | build toolchain named | Linux |
| R89 | Bear | free with paid tier or features, subscription, free trial, then paid | Free · In‑App Purchases (apps.apple.com); "Bear Pro $2.99" monthly and "Bear Pro | not stated | minimum operating-system version named | macOS |
| R90 | codexu/note-gen | free, donation or sponsorship invited, use free | "Free and open source" [@download]; "No subscription or account. All core featur | undecidable ["Configure an AI provider when you want to use AI [clipped] | not stated | Linux, macOS, Windows |
| R91 | doocs/md | not stated | not stated | not stated | not stated | none of the three |
| R92 | genspark-ai/genoffice | free | «Free, for individuals and teams alike.» (README); «Free to download and use. AI | own API key or service account required, stated | minimum operating-system version named | Linux, macOS, Windows |
| R93 | ghostwriter | free | «Free and Open Source» (site); Flathub label «Free»; AlternativeTo «Cost / Licen | not stated | not stated | Linux, macOS, Windows |
| R94 | Haroopad | not stated | not stated | not stated | undecidable | Linux, macOS, Windows |
| R95 | Joplin | free, subscription, free with paid tier or features | Subscription ranging between $2 and $8 per month + free version with limited [cl | not stated | not stated | Linux, macOS, Windows |
| R96 | MacDown | free | [B] "Free"; [B] "Open Source and Free product." | not stated | runtime or interpreter named: | macOS |
| R97 | Manuscript | free | [A] "Free" | not stated | build toolchain named: | Linux |
| R98 | mark-text | free, donation or sponsorship invited, use free: | [E] "Free & open source forever"; [E] "Free download"; [E] "One download. No acc | not stated | minimum operating-system version named: | Linux, macOS, Windows |
| R99 | Markdown All in One | free, donation or sponsorship invited, use free | "Free" in "14,704,681 installs / (172) / Free" [1] // | not stated | host program named | none of the three |
| R100 | Markdown゜ | free | "price": 0, "priceCurrency": "USD" [1] // | not stated | minimum operating-system version named | macOS |
| R101 | MarkEdit | free | \"free\" (\"MarkEdit is a free and open-source Markdown editor, for macOS.\" P4) | not stated | minimum operating-system version named | macOS |
| R102 | marknote | free, donation or sponsorship invited, use free | Free [p2]; "price=0.0 USD" [p1] | not stated | not stated | Linux, macOS, Windows |
| R103 | MarkText | free | Free & open source forever [p6]; "Free download" [p6]; "price=0.0 USD" [p1] | not stated | minimum operating-system version named | Linux, macOS, Windows |
| R104 | Marp for VS Code | free, donation or sponsorship invited, use free | Free [p1] | not stated | host program named | none of the three |
| R105 | MWeb | free with paid tier or features, one-time purchase, subscription | 'Free · In‑App Purchases'; 'MWeb for iPhone/iPad $14.99'; 'MWeb Yearly Subscript | not stated | minimum operating-system version named | macOS |
| R106 | obsidian | free, free with paid tier or features, subscription, one-time purchase | Free without limits. No sign-up required. No strings attached. (obsidian.md/pric | not stated | minimum operating-system version named | Linux, macOS, Windows |
| R107 | Office Viewer | free | 1,556,659 installs / ( 100 ) / Free (marketplace field) | not stated | host program named | none of the three |
| R108 | One Markdown | free with paid tier or features, one-time purchase, subscription | Free · In-App Purchases / "One Markdown for Mac $9.99" / "One Markdown Yearly Su | not stated | minimum operating-system version named | macOS |
| R109 | pd4d10/hashmd | not stated | not stated | not stated | not stated | none of the three |
| R110 | QOwnNotes | free, donation or sponsorship invited, use free | Free flathub.org ; "Free product." alternativeto.net ; "Free open source plain-t | another product or subscription required, stated | runtime or interpreter named | Linux, macOS, Windows |
| R111 | sbarex/QLMarkdown | not stated | not stated | not stated | minimum operating-system version named | macOS |
| R112 | Simplenote | free | Free [flathub.org/apps/com.simplenote.Simplenote] ; "It’s free: Apps, backups, s | not stated | not stated | Linux, macOS, Windows |
| R113 | SiYuan | free with paid tier or features, README], one-time purchase, subscript | Free [Flathub] ; "Most features are free, even for commercial use." [README] ; " | another product or subscription required, stated ["No storage [clipped] | not stated | Linux, macOS, Windows |
| R114 | StackEdit | not stated | not stated | not stated | not stated | none of the three |
| R115 | Taio - Markdown & Text Actions | free with paid tier or features, subscription, one-time purchase, “pay | “Free · In‑App Purchases”; “Taio Pro Monthly $1.49”; “Taio Pro Yearly $14.99”; “ | not stated | minimum operating-system version named | macOS |
| R116 | ThisIs-Developer/Markdown-Viewer | not stated | not stated | own API key or service account required, stated [“optional PAT” for [clipped] | runtime or interpreter named | none of the three |
| R117 | Tinta | free | “Free, open source, MIT licensed.” [tinta.cc] | not stated | none needed, stated | Windows |
| R118 | tw93/MiaoYan | undecidable | “Mac App Store (paid, automatic updates, includes the iPhone and iPad app)” [REA | not stated | minimum operating-system version named | macOS |
| R119 | Typora | one-time purchase, free trial, then paid | “15 days free trial / up to 3 devices”; “$ 14.99 (without tax) x 1” [typora.io]; | not stated | minimum operating-system version named | Linux, macOS, Windows |
| R120 | vaibhav-kakde-in/mdhero | free, donation or sponsorship invited, use free | "Free. Open source." (github.com); "free forever, MIT-licensed, ~8MB, runs entir | not stated | minimum operating-system version named | Linux, macOS, Windows |
| R121 | vorojar/md-preview | not stated | not stated | not stated | runtime or interpreter named | Linux, macOS, Windows |

## D3. Live enquiries

None exist for this offering. Condition under which this count was taken: no surface, no name, no announcement. The offering has no page, listing, package, store entry or installer (capability note), the repository carries a placeholder name and a 2019 description of a different program, and nothing has been announced; so no buyer could enquire for it, and a count of zero enquiries is not a measure of zero demand. The record would hold, per enquiry, the date of enquiry, the date wanted, the party, the channel and the outcome; none is held, and no enquiry for something the operator did not offer is held either.

## D4. The meetings behind those signals

None. No meeting transcript or recorded conversation about this offering or its rivals is open to this register.

## D5. What buyers type

Read from `1-competitions/search-demand-findings.md`, cited by number and not restated. No volume exists (SD-1) and no enquiry wording (SD-2). The words a buyer uses: SD-3, SD-9. The platform words and the terminal: SD-4. What the first page already rewards, term by term: SD-5, SD-6, SD-7, SD-8, SD-10. The adjacent term: SD-11. The instrument limits: SD-12, SD-14 and SD-16. The operator's own words against the buyer's: SD-13. The ceiling: SD-15.

# Readings and limits

- Reading of the capability note and venue situation: a generator would register every markdown viewer on earth; a designer registers what a buyer on Linux, macOS or Windows weighs, and says in each section where V10 names none of the three.
- Reading of the corpus: a generator would count "viewer" in a name as a reader; the codebook does not, and neither does this register: the first test is V09 as coded, so products named "viewer" that are coded editors are registered only through a cell's top five, if at all.
- Not done: no web page was fetched and no version-control history read. Last-release and archived status are as the corpus coded them; where a distributor note adds a GitHub fact it is marked with its note number. A "not stated" under V27 means the captured pages gave no date, not that the product is unreleased.
