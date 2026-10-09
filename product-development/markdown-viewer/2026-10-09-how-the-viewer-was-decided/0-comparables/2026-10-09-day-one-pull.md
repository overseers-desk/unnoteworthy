---
title: "Day-one pull: what markdown viewers and editors say on their own pages"
date: 2026-10-09
method: "SAGE Adjudicate, the card set (`sage-A-adjudicate.md`): the day-one strike list is written from the owner's words and four market-side pulls"
status: "A convenience list, not a frame. Pages were chosen by the orchestrator from general knowledge of the category and from three published lists, read once by three Sonnet-tier agents, and quoted as the fetch tool rendered them. No rate computed here is a prevalence; the frame and the frozen codebook come after the owner returns the strike list."
---

# What was pulled

Three agents each enumerated one published list and read a set of product pages, quoting the audience each page names, the price or licence as stated, the feature claims, the distribution channels and any sentence on why the product exists. The instruction was to quote and not infer, to record an unreachable page as unreachable, and to write no files. Every page went through a summarising fetch tool, so quotes are that tool's rendering and not byte-exact; where an agent read raw text (GitHub READMEs through the API) it says so.

Pages read and readable: 37, counted as follows. Pull A, 12 of 13 (Logseq's page rendered only its title). Pull B, 10 of 13 (Haroopad unreachable on a certificate error; no page found for Buffer or Paper; GNOME Text Editor read but excluded from the count since its page names no markdown rendering). Pull C, 15 of 15.

Three published lists: AlternativeTo's Typora alternatives (221 entries, 12 shown, crowd-sourced, updated 2026-09-25); Flathub's search for "markdown" (48 hits, with installs last month per app); the GitHub topics `markdown-viewer` (1,008 repositories) and `markdown-editor` (2,690), top 20 by stars each. Snapcraft's search returned 100 entries with no counts and a probable cap.

---

## Pull A: paid, Mac and Windows products, and the AlternativeTo list

### AlternativeTo, Typora alternatives

URL read: https://alternativeto.net/software/typora/. The page names no operator beyond AlternativeTo itself, calls its lists "crowd-sourced" and shows "last updated Sep 25, 2026". It says "12 of 221 Typora alternatives". The extract returned 15 slots, two blank and one labelled "Ad".

| # | Entry | Likes shown |
|---|---|---|
| 1 | Joplin | 947 |
| 2 | Zettlr | 270 |
| 3 | (blank) | none |
| 4 | HelixNotes | 30 |
| 5 | Daino Notes (labelled "Ad") | none |
| 6 | Beaver Notes | 79 |
| 7 | SiYuan | 85 |
| 8 | (blank) | none |
| 9 | ghostwriter | 116 |
| 10 | MarkText | 122 |
| 11 | Trudido | 20 |
| 12 | Clearly Markdown | 22 |
| 13 | Marknote | 29 |
| 14 | Reor | 33 |
| 15 | Ferrite | 14 |

### Product pages

| Product | URLs read | Platforms named | Price or licence | Audience (quoted) | Feature claims | Distribution channels | Why it exists |
|---|---|---|---|---|---|---|---|
| Typora | https://typora.io/ | macOS, Windows (64 bit, 32 bit, ARM), Linux | "$ 14.99 (without tax)"; "15 days free trial / up to 3 devices" | "a seamless experience as both a reader and a writer"; "Take notes on math classes"; "root folder of your static blog"; testimonials from a book author and Charles McGuinness | Tables: "Quickest steps to resize tables in Markdown file: just mouse dragging." Outline: "Automatically see the Outline structure of your documents in outline panel." TOC via "[TOC]". Live preview: "Preview while you are typing." Links: "Set your the link targets towards a header, a markdown file, or an URL." Images: resize, drag and drop. Math: "Most MathJax extensions built-in". Diagrams: flowchart.js, Mermaid, sequence. Export: "Export to PDF with bookmarks", plus docx, LaTeX, Epub and others. Folding and find not mentioned. | Direct downloads only: dmg, Windows installers, .deb, apt repository, tarballs | Not stated as a sentence; paraphrased: focus on content by removing preview panes, mode switching and syntax symbols |
| Marked 2 | https://marked2app.com/ | "Marked 2 requires macOS 10.12 or later" | No price on the page. Free 7-day trial; buy via Paddle or Mac App Store. Notes Marked 3 is out at a discounted launch price | "Whether you're blogging, authoring a book, writing a report or editing a GitHub README file"; sections "Tools for authors", "Tools for coders", "Tools for bloggers", "Tools for business", "Tools for everyone" | Collapsible sections; automatic table of contents panel; updates "on every save in any editor"; search with wildcards and regular expressions; copy, validate and open links; refreshes embedded images; MathJax; PDF, Word, and self-contained HTML. Tables and diagrams not mentioned | Mac App Store; direct purchase via Paddle; free trial download | "a previewer for Markdown and other plain text markups" |
| iA Writer | https://ia.net/writer, https://ia.net/writer/pricing | Mac, Windows, iPad and iPhone | Mac $49.99, Windows $29.99, iPhone and iPad $49.99, all one-time ("One-Time ≠ Lifetime"). Free 7-day trial on Mac and Windows | "writers, whether they be students, professionals, or aspiring authors" (Time quote); "Markdown aficionados" (Forbes quote); "over two million writers"; "20% educational discount"; volume purchases | Focus Mode; Style Check; Authorship; "Switch to Preview to see it styled"; copy as HTML, export PDF or Word. Tables, outline, link following, images, math and diagrams not mentioned | Apple App Store (iPad and iPhone); direct download for Mac and Windows | Paraphrased: removes menus and buttons so writers can focus on writing first |
| Ulysses | https://ulysses.app/, https://ulysses.app/en/pricing/ | Macs, iPads, iPhones | "$39.99 per Year" or "$5.99 per Month" (US); "Free trial on all devices." | "made for people who love to write and write a lot"; "Be it college essays, blog posts, or the next Great American Novel"; "All Kinds of Writers Rely on Ulysses"; "Businesses and Organizations"; "Reduced pricing for students" | "a live preview built right in"; export to PDF, Word, ebooks, blog posts; grammar check in over 20 languages. Tables, outline, search, links, math and diagrams not mentioned | Mac App Store, App Store, Setapp; volume licensing outside the App Store | Paraphrased: powerful features in a focused, distraction-free environment |
| Bear | https://bear.app/ | Mac, iPhone, iPad | Free tier; Bear Pro "$2.99/month, or $29.99/year" after a 7-day trial | "Powerful tools to take notes, plan your week, write a book, or even build a wiki"; "Capture, write, and organize your life" | Tables; headings and folding; OCR search in photos and PDFs (Pro); links get rich previews; image resize and crop; export PDF and HTML. Live preview, math and diagrams not mentioned | Mac App Store, iOS App Store | "beautiful, powerfully simple Markdown note taking app" |
| Inkdrop | https://www.inkdrop.app/ | "macOS, Windows, Linux, iOS, Android" | "$9.98 / month"; "$8.31 / month", "$99.80 billed annually"; "30-day free trial"; licence type not stated | "an AI-native Markdown note app for developers"; "the daily thinking space of developers around the world since 2016"; "Join the doers' club" | Outline and code folding via plugins; "Mermaid diagrams"; "KaTeX rendering for inline and block equations"; fuzzy-finding via the command palette. Tables, live preview, links, images and export not mentioned | A "Download" page only; no store or package channel named | "AI handles the how. Write down your why in a clean Markdown space." |
| Caret | https://caret.io/ (https://caret.ink/ is a different product, a text expander, and was excluded) | "Mac, Windows and Linux" | "$29 licence"; no licence type named | None stated. Testimonial roles only: Writer, Developer, Designer, Freelance Writer, Editor at SitePoint; "If you write a lot of Markdown." | "Helps with tables, lists, html, fences, links, emphasis, etc."; sidebar to "view the headings in the current file"; "Enable preview"; Go To "quickly jump to a file, folder, heading or command"; context actions "visit links"; "Renders LaTeX math expressions inline". Images, diagrams and export not claimed | GitHub releases (Linux beta 4.0.0-rc23); the purchase link was a placeholder | Paraphrased: written from scratch to keep flexibility to add features |
| Obsidian | https://obsidian.md/, /pricing, /download | The home page names only Windows; the download page lists Windows, Mac, Linux, iOS, Android | Home: "Free without limits." Pricing: Sync $4 per user per month billed annually; Publish $8 per site per month billed annually; Catalyst $25 one-time; Commercial $50 per user per year, optional ("You are not _required_ to pay for a commercial license") | "The free and flexible app for your private thoughts."; "Invent your own personal Wikipedia."; "Work with your team on shared files"; students, faculty and nonprofit employees get 40% off | "Create connections between your notes", graph view; Canvas to "diagram"; images sync as files. Tables, folding, find, math and PDF or HTML export not mentioned | Windows .exe, Mac .dmg, Linux AppImage, Snap, Deb, Flatpak ("Community maintained", Flathub), iOS App Store, Google Play, APK, web clipper for Chrome, Safari, Firefox, Edge and others | "Sharpen your thinking." (tagline) |
| Zettlr | https://www.zettlr.com/, /download | Windows, macOS, Linux | "Free and Open Source software, supported by donations"; no named licence | "journal submission or book manuscript"; "Whether STEM, social sciences or humanities"; journalists; Zettelkasten users; university staff and students | Wiki-style links and graph view; LaTeX equations; Mermaid charts; Pandoc export profiles (Beamer, reveal.js, PowerPoint); a testimonial praises "powerful search"; WYSIWYG level is user-chosen. Tables, images and explicit PDF or HTML export not stated | Homebrew, WinGet, APT, Flatpak (FlatHub), Chocolatey, Pacman, direct deb, rpm, AppImage, dmg, exe, nightly builds | Paraphrased: a single privacy-respecting app from first notes to publication |
| Joplin | https://joplinapp.org/, /download/ | Windows, macOS, Linux, Android, iOS, plus a terminal app | No price on the page; "The app is open source" with no licence named; Joplin Cloud plans linked | "share your notes with your friends, family or colleagues"; PCMag quote: "Unlike some open-source tools, which are incredibly difficult to use, Joplin is surprisingly user friendly." | "Images, videos, PDFs and audio files are supported."; math and diagrams "directly from the app"; Rich Text or Markdown editors; publish by URL. Tables, outline, preview, search and export not mentioned | Windows, macOS, macOS M1, Linux, Google Play, App Store, portable app, terminal app, Android APK; web clipper for Chrome and Firefox | "Capture your thoughts and securely access them from any device." |
| Logseq | https://logseq.com/ | unreadable | unreadable | unreadable | unreadable | unreadable | Only the title "Logseq: A privacy-first, open-source knowledge base" rendered |
| Markdown Monster | https://markdownmonster.west-wind.com/, /purchase | Windows ("The Markdown Editor for Windows") | Evaluation free; Single User (v4) $99; Lifetime Single User $399; 5-user $399; 10-user $749; 25-user $1,899; Site $5,999. "All licenses are perpetual licenses that don't expire, valid for use with the major version they were purchased for" | Weblog authors on "WordPress, MetaWeblog, Jekyll, or Medium"; developers ("For Developers" section); "What our Users say" | "Sophisticated table editor"; document outline; "Live, synched Html preview"; Document Link Checker; image paste and drag and drop; MathML; Mermaid; PDF and HTML export. Folding and find not mentioned | Direct download; Chocolatey; WinGet | Not stated; closest: developers "wanted to make sure the editor is highly extensible" |
| Notable | https://notable.app/ | Windows, Linux, Mac; a web app and mobile apps in development (paraphrased) | No price or licence stated; "you can keep using the desktop app for free" | None named; usage phrases only ("Zen mode", "Todos can be used for task management") | "Split editor" to check how a note renders; "Fuzzy search is used when searching."; "Linking to other notes and attachments is supported."; "KaTeX expressions"; "Mermaid diagrams"; "Export your notes to Markdown, HTML or PDF." Tables and outline not mentioned | Windows NSIS installer; Linux AppImage, Deb, Pacman, Rpm, Snap; Mac Dmg | Tagline: "The Markdown-based note-taking app that doesn't suck." |

Pages linked but not fetched in this pull: Typora's purchase and feature anchors; Marked 2's help pages; Inkdrop's pricing section and download page; Ulysses' releases page; Joplin's plans page; Caret's docs; Notable's download site.

---

## Pull B: Linux and open-source desktop products, with the Flathub and Snapcraft lists

### Flathub, search "markdown"

The HTML page rendered "000 results" to a fetch, so the JSON API was used (POST https://flathub.org/api/v2/search, body {"query":"markdown"}): 48 hits. The count shown is installs in the last month.

| # | Entry | App ID | Installs last month |
|---|---|---|---|
| 1 | Marknote | org.kde.marknote | 2371 |
| 2 | ghostwriter | org.kde.ghostwriter | 1827 |
| 3 | Manuscript | io.gitlab.ilshat_apps.manuscript | 1763 |
| 4 | QOwnNotes | org.qownnotes.QOwnNotes | 1109 |
| 5 | Cedilla | dev.mariinkys.Cedilla | 718 |
| 6 | Swifty Notes | me.spaceinbox.swiftynotes | 678 |
| 7 | Tangent | io.github.suchnsuch.Tangent | 651 |
| 8 | Ferrite | io.github.olaproeis.Ferrite | 586 |
| 9 | Marker | com.github.fabiocolacio.marker | 533 |
| 10 | ReText | me.mitya57.ReText | 427 |
| 11 | KleverNotes | org.kde.klevernotes | 347 |
| 12 | ThiefMD | com.github.kmwallio.thiefmd | 297 |
| 13 | Norka | com.github.tenderowl.norka | 246 |
| 14 | Formiko | cz.zeropage.Formiko | 194 |
| 15 | ThemeGenerator | io.github.thiefmd.themegenerator | 143 |

### Snapcraft, search "markdown"

The search page rendered no results; the Snap Store API (https://api.snapcraft.io/v2/snaps/find?q=markdown) returned 100 results, probably a cap, with no install counts. First 15 in order: SnapDock - Markdown Workspace; markdown-editor; Markdown Viewditor; Markdown Hot Reload; MarkView; MarkdownMeister; markdown-viewer-premium; Markdown Editor (markdown-editor-viewer); Markdown Viewer; WeKan; ONLYOFFICE Desktop Editors; qownnotes; htmldoc; ghostwriter; Wave Terminal.

### Product pages

| Product | URLs read | Platforms named | Price or licence | Audience (quoted) | Feature claims | Distribution channels | Why it exists |
|---|---|---|---|---|---|---|---|
| MarkText | https://github.com/marktext/marktext | Linux, macOS (11+), Windows (10 and 11) | "MIT license" | not stated | "Realtime preview (WYSIWYG)"; "Math (KaTeX)"; "HTML and PDF export"; "Pasting images from the clipboard". Tables, folding, find, link following and diagrams not mentioned | GitHub releases, Homebrew Cask, Chocolatey, Winget, Linux instructions on the project site | Nearest sentence: "a simple and elegant open-source markdown editor that focused on speed and usability" |
| ghostwriter | https://github.com/KDE/ghostwriter (mirror) | Windows and Linux; a macOS installer is planned | "GNU GPL version 3" | "that next blog post, your school paper, or your NaNoWriMo novel" | "live HTML preview and export options" (via Pandoc, MultiMarkdown or cmark); cmark-gfm. Tables, folding, find, link following, images, diagrams and PDF not mentioned | KDE Gear and distro repos, Ubuntu PPA, Fedora Copr, KDE binary factory, source | "provides a relaxing, distraction-free writing environment" |
| ReText | https://github.com/retext-project/retext | No OS list; names Python 3.9+, PyQt6, "Debian-based systems" | "GNU GPL (v2+)" | not stated | Markdown, reStructuredText, Textile and AsciiDoc; optional "preview engine with JavaScript support". Nothing else on the list mentioned | PyPI, source | Nearest sentence: "a simple but powerful editor for markup languages" |
| Apostrophe | https://gitlab.gnome.org/World/apostrophe; https://world.pages.gitlab.gnome.org/apostrophe (the README URL failed to load) | Flathub linked; no OS list on the project page | "GNU GPLv3" on the project page; no licence on the site page | "A clean and intuitive Markdown editor designed for those of you who love a distraction-free writing environment" | "your document compiled in real time"; Ctrl+click popover preview of "links, images, footnotes, and equations"; export to PDF, ODT, Word and HTML via Pandoc. Tables, folding, find and diagrams not mentioned | Flathub, GitLab source | "A distraction free Markdown editor" |
| Remarkable | https://remarkableapp.github.io/, /linux.html | Linux; "The best markdown editor for Linux and Windows" | "You can download the Linux version for free (or donate if you wish)"; licence not stated | "software documentation writers and students taking notes" | "Live preview with synchronized scrolling"; MathJax; GitHub Flavoured Markdown (links and images); PDF and HTML export; PDF exports include a table of contents | Download page, GitHub, installers for Debian, Ubuntu, Fedora, SUSE and Arch | not stated |
| Haroopad | https://pad.haroopress.com/ | unreachable | unreachable | unreachable | unreachable | unreachable | Certificate name mismatch on both https and http |
| Abricotine | https://github.com/brrd/abricotine | "Windows (7 and +), Linux and OS X" | "GPL-3.0 license"; "Abricotine is discontinued" (archived August 2023) | not stated | "Markdown editor with inline preview"; manage and beautify tables; table of contents in a side pane; images and math previewed inline; "Search and replace"; export to HTML or any Pandoc format. Link following and diagrams not mentioned | Source on GitHub | Nearest: rendered markdown shown in the editing area instead of a separate pane |
| Formiko | https://github.com/ondratu/formiko | Linux (Flatpak, Debian-based), FreeBSD, NetBSD | "Free and open source"; licence not named | not stated; "a reStructuredText and MarkDown editor and live previewer" | "preview mode with auto scroll"; "linked file opening"; HTML output only; no PDF | Flathub, PyPI, apt, FreeBSD pkg, NetBSD pkgsrc, GitHub | not stated |
| PanWriter | https://panwriter.com/ | "macOS, Windows and Linux" | "free and open source software"; licence not named | "Distraction-free writing environment"; pandoc is "treasured" by "hackers" | CSS changes "reflected live" in a paginated preview; export to docx, EPUB, LaTeX, HTML, PDF, PowerPoint and ICML via pandoc; drag-and-drop import of .docx. Tables, find, link following, math and diagrams not mentioned | GitHub Releases, "Try online", source; needs a separate pandoc install | "users had to master the command-line, before they could tap into the power of pandoc" |
| Okular, markdown support | https://apps.kde.org/okular-md/ | Linux, plus Windows and macOS nightly builds | "GPL-2.0+" and "GFDL-1.3" | not stated | Reading Markdown only; no other feature named | AppStream stores (Discover), distro package manager, KDE CDN nightly installers | "Adds support for reading Markdown documents." |
| Marker | https://github.com/fabiocolacio/Marker; https://flathub.org/apps/com.github.fabiocolacio.marker | Linux ("a markdown editor for linux made with GTK+-3.0") | "GPL-3.0"; donations via PayPal | not stated | Table of contents (HTML and LaTeX conversion); tables via SciDown; "TeX math rendering with KaTeX or MathJax"; Mermaid; export to PDF, RTF, ODT and DOCX via pandoc. Live preview, find and link following not mentioned | Fedora, Flathub, AUR, Arch repo, Ubuntu PPA, Snap Store, GitHub tarballs, source | not stated |
| GNOME Text Editor | https://apps.gnome.org/TextEditor/ | Linux (keyword); Flathub | "GPL-3.0-or-later" | not stated | No mention of markdown or preview, so excluded from the count of pages | Flathub | "a simple text editor focused on a pleasing default experience" |

No page was reached for Buffer or Paper (GNOME notes apps); a web search surfaced Folio, "beautiful markdown note-taking app for GNOME", forked from Paper, not read.

---

## Pull C: terminal readers, browser and editor extensions, and the GitHub topic lists

Star counts are from the GitHub API on 2026-10-09. READMEs were read through the API, the first 4,500 to 7,000 characters each, so a claim past that point would be missing.

### GitHub topic `markdown-viewer`, 1,008 repositories, top 20 by stars

1. MacDownApp/macdown 9835 "Open source Markdown editor for macOS."
2. pd4d10/hashmd 4346 "Hackable Markdown Editor and Viewer (WIP)"
3. sbarex/QLMarkdown 3630 "macOS Quick Look extension for Markdown files."
4. Textualize/frogmouth 3307 "A Markdown browser for your terminal"
5. Ionaru/easy-markdown-editor 3086 "EasyMDE: A simple, beautiful, and embeddable JavaScript Markdown editor…"
6. d0c-s4vage/lookatme 2332 "An interactive, terminal-based markdown presenter"
7. hua1995116/react-resume-site 2312 (a markdown online résumé tool, Chinese)
8. RivoLink/leaf 2120 "Terminal Markdown previewer — GUI-like experience."
9. simov/markdown-viewer 1702 "Markdown Viewer / Browser Extension"
10. TooBug/wemark 1311 (a WeChat mini-program markdown rendering library)
11. k1LoW/mo 1070 "mo is a Markdown viewer that opens .md files in a browser."
12. vsch/idea-multimarkdown 810 "Markdown language support for IntelliJ IDEA."
13. goessner/mdmath 776 "LaTeX Math for Markdown inside of Visual Studio Code."
14. Houfeng/mditor 530 "[ M ] arkdown + E [ ditor ] = Mditor"
15. ThisIs-Developer/Markdown-Viewer 527 "A Markdown Editor That Lives in Your Browser, Desktop, and a Single URL…"
16. alexishida/Moji 493 "Open Markdown files like PDFs. A lightweight, clean desktop app for opening, reading, editing, and exporting Markdown files."
17. schuyler/macdown3000 487 "A modern, lightweight Markdown editor for macOS."
18. mohzy83/NppMarkdownPanel 453 "Lightweight Notepad++ plugin to preview Markdown files"
19. liyasthomas/marcdown 430 "Lightweight realtime markdown viewer and editor"
20. Linbreux/wikmd 424 "A file based wiki that uses markdown"

### GitHub topic `markdown-editor`, 2,690 repositories, top 20 by stars

1. foambubble/foam 17441 "A personal knowledge management and sharing system for VSCode"
2. pandao/editor.md 14318 "The open source embeddable online markdown editor (component)."
3. doocs/md 13409 (a WeChat public-account markdown editor, Chinese)
4. codexu/note-gen 12882 "Capture first. Organize later. A local-first Markdown app that turns scattered records into clear notes with AI."
5. Milkdown/milkdown 11980 "Plugin driven WYSIWYG markdown editor framework."
6. hackjutsu/Lepton 10340 "Democratizing Snippet Management (macOS/Win/Linux)"
7. MacDownApp/macdown 9835
8. genspark-ai/genoffice 9036 "Free, open-source AI Office suite… plus a `genoffice` CLI and agent skill so Claude Code, Codex and Cursor can create and edit real .docx/.xlsx/.pptx files locally…"
9. tw93/MiaoYan 8669 "Lightweight Markdown app to help you write great sentences."
10. dendronhq/dendron 7468 "The personal knowledge management (PKM) tool that grows as you do!"
11. taniarascia/takenote 7126 "A web-based notes app for developers."
12. purocean/yn 6766 "A highly extensible Markdown editor featuring version control, AI Copilot…"
13. kalcaddle/KodExplorer 6392 "A web based file manager, web IDE / browser based code editor"
14. gsantner/markor 6242 "Text editor - Notes & ToDo (for Android) - Markdown, todo.txt, plaintext, math…"
15. MarkEdit-app/MarkEdit 5804 "Just like TextEdit on Mac but dedicated to Markdown."
16. shd101wyy/markdown-preview-enhanced 4442 (the Atom extension)
17. inkeep/open-knowledge 4432 "Beautiful, AI-native markdown IDE and LLM wiki"
18. pd4d10/hashmd 4346
19. Moeditor/Moeditor 4100 "(discontinued) Your all-purpose markdown editor."
20. mdx-editor/editor 3691 "A rich text editor React component for markdown"

### Product pages

| Product | URLs read | Platforms named | Price or licence | Audience (quoted) | Feature claims | Distribution channels | Why it exists | Stars |
|---|---|---|---|---|---|---|---|---|
| Glow | https://github.com/charmbracelet/glow | "MacOS, Linux, Windows, FreeBSD and OpenBSD binaries"; "Android (with termux)"; terminal | "MIT" | "Glow is a terminal based markdown reader"; "Use it to discover markdown files, read documentation directly on the command line." | "Markdown files can be read with Glow's high-performance pager"; fetches README from GitHub, GitLab or HTTP. Tables, folding, find, images, math, diagrams, export not stated | Homebrew, MacPorts, pacman, xbps, Nix, FreeBSD pkg, Solus, Chocolatey, Scoop, Winget, Termux, Snap, apt and yum repositories, Debian, RPM and Alpine packages, go install, source | "Render markdown on the CLI, with _pizzazz_!" | 27634 |
| Frogmouth | https://github.com/Textualize/frogmouth | "Frogmouth runs on Linux, macOS, and Windows"; terminal | "MIT" (GitHub licence field) | not stated | "browser-like navigation stack, history, bookmarks, and table of contents"; "open `*.md` files locally or via a URL" | pipx, pip, Homebrew tap | "Frogmouth is a Markdown viewer / browser for your terminal" | 3307 |
| grip | https://github.com/joeyespo/grip | Linux, OS X, Windows; browser via a local server | "MIT" (GitHub licence field) | not stated; "Here's how others from the community are using Grip." | "Changes you make to the Readme will be instantly reflected in the browser without requiring a page refresh"; "export to a single HTML file, with all the styles and assets inlined"; relative URLs | pip, Homebrew | "Sometimes you just want to see the exact readme result before committing and pushing to GitHub." | 6837 |
| mdcat | https://github.com/swsnr/mdcat | Terminals: Windows 10 console, iTerm2, kitty, WezTerm, VSCode, Ghostty, Konsole | "Mozilla Public License, v. 2.0" | not stated | "shows links, and also images inline in supported terminals"; "jump marks for headings in iTerm2"; "Not supported: … Inline markup and text wrapping in table cells." | Release binaries, third-party packages, cargo, source. Banner: "This repository is no longer maintained"; fork at BIRSAx2/mdcat not read | "Fancy `cat` for Markdown (that is, CommonMark)" | 2412 |
| mdless | https://github.com/ttscoff/mdless | terminal; iTerm2 mentioned | "MIT" (GitHub licence field) | not stated | "Format tables"; "List headlines in document / Display single section of the document based on headlines"; "Inline image display"; "Built in pager functionality … `less` replacement for Markdown files" | gem, Homebrew | "I often use iTerm2 in visor mode, so `qlmanage -p` is annoying. I still wanted a way to view Markdown files quickly and without cruft." | 971 |
| Markdown Viewer (simov) | https://github.com/simov/markdown-viewer | Chrome, Firefox, Edge, Opera, Brave, Chromium, Vivaldi | "Free and Open Source"; "MIT" (GitHub field) | not stated | "GitHub Flavored Markdown (GFM)", "Full CommonMark support including GFM tables"; "Table of Contents (ToC)"; "Auto reload on file change"; "MathJax formulas"; "Mermaid diagrams"; "Remember scroll position" | browser extension stores | not stated | 1702 |
| Markdown Preview Enhanced | https://github.com/shd101wyy/vscode-markdown-preview-enhanced | VS Code; "VS Code for the Web" | "released under the University of Illinois/NCSA Open Source License"; sponsors | not stated | "automatic scroll sync, math typesetting, mermaid, PlantUML, WebSequenceDiagrams, pandoc, PDF export, code chunk, presentation writer"; "wikilinks, backlinks, tags and the graph" | VS Code Marketplace | no why-sentence | 2103 |
| Markdown Preview Plus | Chrome Web Store listing (ooso.net) | Chrome | Price not shown; open source per listing | not stated | "Converts and previews markdown files (.md, .markdown) to HTML(include TOC) right inside Chrome and support live reload"; GFM, HTML export, KaTeX, Mermaid | Chrome Web Store | not stated | not GitHub-hosted |
| Marp | https://marp.app/; https://github.com/marp-team/marp | VS Code extension, CLI; export uses Chrome or Chromium | no price or licence on marp.app; "MIT" (GitHub field) | "If you know how to write a document with Markdown, you already know how to write a Marp slide deck." | "Marp can convert Markdown into presentation-ready HTML, PDF and PowerPoint files directly!"; "image syntax, math typesetting, auto-scaling"; preview as you edit | VS Code Marketplace, npm, GitHub releases | "Marp is the ecosystem to write your presentation with plain Markdown." | 12611 |
| Mdview (c3er) | https://github.com/c3er/mdview | "Windows: Setup-exe, ZIP archive; Linux: AppImage package; macOS: DMG package" | "You can use and copy this tool under the conditions of the MIT license." | not stated | "A standalone application that renders and displays Markdown files. It does nothing else!"; GitHub Flavored Markdown | GitHub releases, winget, Scoop, AppImage, DMG | "No direct editing nor any fancy note taking features. It is not distributed as a browser extension nor does it fire up a web server - so no web browser is needed to see the rendered Markdown file." | 146 |
| MacDown | https://github.com/MacDownApp/macdown; https://macdown.uranusjr.com/ | OS X, macOS | "released under the MIT License" | not stated; the author's own use | "Highly customisable Markdown rendering. Syntax highlighting in fenced code blocks. Sophisticated auto-completion." | direct download, Homebrew Cask | "I like Mou. … I decided that instead of waiting for others to do something about this, I should act myself." | 9835 |
| HashMD | https://github.com/pd4d10/hashmd | not stated | "MIT" | not stated | not stated ("Working in progress") | not stated | not stated | 4346 |
| QLMarkdown | https://github.com/sbarex/QLMarkdown | "Mac OS" | "GPL-3.0" (GitHub field); donation link | "This application is not intended to be used as a standalone markdown file editor or viewer." | "a Quick Look extension for viewing Markdown files"; command-line converter to HTML; Mermaid and math listed | GitHub releases, Homebrew cask | not stated | 3630 |
| EasyMDE | https://github.com/Ionaru/easy-markdown-editor | browser (JavaScript component) | "MIT" (GitHub field) | "EasyMDE allows users who may be less experienced with Markdown to use familiar toolbar buttons and shortcuts." | "built-in auto saving and spell checking"; "the syntax is rendered while editing" | npm, unpkg and jsDelivr | "A drop-in JavaScript text area replacement for writing beautiful and understandable Markdown." | 3086 |
| Foam | https://github.com/foambubble/foam | VS Code | "Foam is free, open source" | "You can use Foam for organising your research, keeping re-discoverable notes, writing long-form content and, optionally, publishing it to the web." | "Link Preview and Navigation", "Navigation in Preview", "Backlinks Panel", "Graph Visualization", "Support for sections" | VS Code Marketplace | "Foam is a personal knowledge management and sharing system built on Visual Studio Code and GitHub." | 17441 |

Not read in this pull, the cap of five extras reached: pandao/editor.md, doocs/md, codexu/note-gen, Milkdown/milkdown. The Markdown Preview Enhanced docs site rendered only its title. The mdcat fork was not read, to avoid substituting a source.

---

## The limits of this pull, to carry into any count made from it

The list is a convenience list: nobody can re-open it and count it, so nothing here is a prevalence. Every quote passed through a summarising fetch tool except the GitHub READMEs, which were read raw but truncated. A page that names no audience is silent, which is a value and not a fact about whom it sells to. A product can address a buyer on a page not read here (a pricing page, a docs page), so every "n of 37" is a floor.
