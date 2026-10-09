---
title: "Codebook v1: coding one comparable markdown product from its published text"
date: 2026-10-09
method: "SAGE Survey, the codebook frozen blind (`sage-S-survey.md` section 1, step 4): drafted before any frame or product page was seen, frozen before collection"
version: 1
status: "Frozen 2026-10-09. See the last section."
---

# What this manual is for

You are a coding clerk. You receive one profile: the verbatim text that one comparable product publishes about itself, on its own pages or on the listing it was drawn from, with the URL and capture date of every page and a list of the pages that could not be reached. From that profile you fill one row of the coded corpus by applying the variables below, in order, starting with eligibility.

The products in this corpus are applications, extensions or terminal programs a person installs or opens to read or write markdown files, on any platform, found through stores, package repositories and repository topic lists.

# Standing instructions

These hold for every variable. Where a variable's own rule seems to disagree with them, they win and you code "undecidable".

1. **Text only.** Code only words in the profile: page text, listing fields (title, subtitle, description, "what's new", compatibility, price, licence, version, date fields, category), README text and the text of a repository page's own fields (description, topics, licence field, release list, archived banner). Do not code from screenshots, images, videos, icons, or alt text, even where an image plainly shows a feature. Do not code from user reviews or comments on a listing: they are what buyers wrote, not what the product publishes. Do not open anything outside the profile.
2. **Silence is a value, not a fact.** Where the profile says nothing on a variable, code "not stated". "Not stated" means the product did not publish it in the captured pages. It never means the product lacks it.
3. **No inference in either direction.** Do not code a value because the product's kind, platform, licence, price, technology or other features make it likely. Do not withhold a value because it seems unlikely. A terminal program has not stated it is for terminal users; an open-source licence has not stated that business use is free; a store listing has not stated a platform unless its compatibility field names one.
4. **Every coded value carries its evidence.** For each value other than "not stated", record the quoted words (shortest span that carries the value) and the URL of the page they came from. A value with no quote is a coding error.
5. **A rule two coding clerks would apply differently has failed.** Every variable below has a decision rule and at least one worked hard case. The hard cases are written from imagination and describe no real product.
6. **Undecidable.** If you meet a case the rule cannot decide, code "undecidable" for that variable and write a note: the quote, the rule, and why the rule does not settle it. Never extend a rule, never pick the nearer value, never decide by analogy with a worked example that does not match. An "undecidable" is a finding about this manual and goes back to its owner.
7. **Unreachable pages.** If the profile lists a page as unreachable, you do not know what it said. Code from what was captured; the row's capture-gap field (below) carries the unreachable list so the analyst can see which "not stated" values sit beside a gap. Do not substitute any other source.
8. **Language.** Code text in whatever language it is published in. Quote the original; add an English rendering in the note. If you cannot read the language with confidence, code "undecidable" for each variable the text bears on.
9. **Several pages.** Multi-valued variables take the union of what all captured pages state. For a single-valued variable, the variable's own rule says what to do when pages disagree; where it does not, code "undecidable" and quote both.
10. **Status marks are provenance, not variables.** Store verification badges, "editor's choice" marks, awards, certifications and similar third-party standing marks are copied verbatim into the provenance field only. No variable codes them, and no value elsewhere is coded from them.
11. **Changing a frozen rule** takes a new version number, a date, and re-coding of every row already coded. A clerk does not change a rule; a clerk records an undecidable.

# Row record fields

These are recorded for every row, eligible or not. They are not variables and carry no decision rule beyond copying.

- **R1 Row identifier** as given in the profile.
- **R2 Source list and cell** as given in the profile.
- **R3 Captured pages:** each URL with its capture date.
- **R4 Capture gaps:** each unreachable URL with its error, as given in the profile.
- **R5 Status marks (provenance only):** verbatim text of any third-party standing mark, with URL. Empty if none.
- **R6 Notes:** every undecidable, conflict and translation note, keyed by variable number.

# Value conventions

- **Multi** means several values may be coded together; code every one that the rule admits.
- **Single** means exactly one value.
- **"Not stated"** and **"undecidable"** are available on every variable even where the value list does not repeat them. In a multi variable, "not stated" is coded only when no other value is coded.
- **Verbatim** fields hold quoted text exactly as published, including spelling and capitals, with URL.
- **Text naming** in a rule means the words appear in the profile, in any grammatical form (plural, verb form, abbreviation the same page expands, or the page's translation of the term).

# Part 1: eligibility, applied first

## V01 Eligibility (single)

Values: **eligible**; **ineligible: no captured text**; **ineligible: markdown not handled**; **ineligible: not a product**; **undecidable**.

Decision rule. Apply the three tests in order and stop at the first failure.

1. *Text test.* The profile contains at least one captured page published by the product, its maker, or the listing it was drawn from. If every page is unreachable or the captured pages hold no text about the product, code **ineligible: no captured text**.
2. *Markdown test.* The captured text states at least one of: (a) the product shows markdown rendered (words such as render, preview, display, view, read, open, together with "markdown", "md", ".md" or a named markdown flavour, in the same sentence or the same feature list item); or (b) the product edits or writes markdown, where "markdown", "md" or ".md" appears in the product's name, its tagline or subtitle, or the first paragraph of its description. A product whose only mention of markdown is an entry in a list of supported file types or languages, with no rendering or viewing claim, fails. A product that only converts markdown to another format and states no view of its own fails. Failure: code **ineligible: markdown not handled**.
3. *Product test.* The captured text presents something a person installs, adds or opens to use: an application, an extension or plug-in, a terminal program, a mobile application, a library or component, or a web service. A theme, a stylesheet, a template, a configuration file, a tutorial, an article or a list of other products fails, unless the same page states that it also reads or writes markdown itself. Failure: code **ineligible: not a product**.

If all three pass, code **eligible**. For an ineligible row, record R1 to R6 and V02, and stop.

Hard case A. An imagined listing for a note-taking application says "Write notes, plan projects, export to PDF, HTML and Markdown." Markdown appears only as an export format and is not in the name, tagline or first paragraph; nothing says it renders or opens markdown. Test 2 fails: **ineligible: markdown not handled**.

Hard case B. An imagined repository README for a command-line converter says "Turns .md files into PDF. Use --preview to see the rendered page in a window before writing." The preview sentence claims a rendered view of markdown. Test 2 passes on (a): **eligible**.

Hard case C. An imagined listing for a colour theme says "A calm dark theme for your markdown previewer." It is a theme and does not state that it reads markdown itself: **ineligible: not a product**.

# Part 2: what it is and who it is for

## V02 Name as published (verbatim)

Record the product's name exactly as it appears in the listing title, or, where there is no listing title, in the first heading of its own page. If the listing title adds a descriptive tail after a separator (a dash, colon or vertical bar), record the whole title verbatim and nothing else. "Not stated" only if no title or heading exists.

Hard case. An imagined store title reads "Penwick: Markdown Reader & Notes". Record "Penwick: Markdown Reader & Notes" whole. Do not split it; V03 reads its parts.

## V03 Name form (multi)

Answers "What is it called?" as the market answers it. Values:

- **markdown token in name**: the title contains "markdown", "md" as a separate word, or ".md".
- **function word in name**: the title contains view, viewer, read, reader, preview, edit, editor, write, writer, note, notes, doc, docs, pad, or the same words in the page's language.
- **maker name in title**: the title contains the maker's or publisher's name as shown in the listing's developer or publisher field or the page's footer.
- **none of the above**: none of the three applies.

Decision rule. Read V02 only. Match whole words, case-insensitively. A function word fused into a coined word ("Notewise", "Readly") counts only if it is separated by a space, hyphen, dot or capital letter boundary inside the word; "NoteWise" counts, "Notewise" does not.

Hard case. An imagined title "mdlark" has no space or separator, so "md" is not a separate word: **none of the above**. The title "MD Lark" would be **markdown token in name**.

## V04 One thing or several (single)

Answers "Is this one thing or several?". Values:

- **single program**: the captured text offers one program and names no other edition, companion program or component.
- **one program in editions**: the text names editions, tiers or versions of the same program (free and pro, lite and full, personal and team).
- **program and component**: the text offers the program and, separately, a library, component or package others can build into their own software.
- **family of programs**: the text names two or more distinct programs from the same maker offered alongside this one (on the same page or as a bundle).
- **component only**: the text offers only a library, component or package.

Decision rule. Code from what the captured pages offer, not from what the maker may sell elsewhere. A "see our other apps" link list with names counts as **family of programs** only if it appears on a captured page of this product. Where more than one value applies, code in this precedence: family of programs, program and component, one program in editions, single program.

Hard case. An imagined page offers "Reader Free" and "Reader Plus" and, at the foot, "Also by us: Sketchbook, Timer." Editions and a family both apply; precedence gives **family of programs**, and the note records the editions.

## V05 Whom the product sells to (multi)

Answers "Who is this for?". Values, exactly the buyer classes of this run, plus "not stated":

1. **Writers and authors**
2. **Bloggers and platform publishers**
3. **Students and academics**
4. **Developers and coders**
5. **Note-takers and personal knowledge managers**
6. **Teams, businesses and organisations**
7. **Terminal readers**
8. **Plain readers of received markdown files**
9. **Readers of what AI agents write**
10. **Application developers embedding a markdown view**

Decision rule.

- A class is coded only where the text contains an **audience phrase**: a noun or noun phrase naming people or organisations, used as the product's user, customer or audience ("for X", "X love it", "built for X", "if you are an X", "X can...", a plan or licence named for X).
- A feature is not an audience. Do not code a class from what the product does, supports, integrates with or runs on. Math rendering does not code academics; keyboard shortcuts in an editor's style do not code developers; running in a terminal does not code terminal readers; being a library does not code application developers.
- A purpose phrase without a person is not an audience: "for writing", "for note-taking", "for reading markdown" code nothing here; record them in V06.
- **Named audience nouns.** Code the class whose list contains the noun:
  1. writers, authors, novelists, journalists, copywriters, screenwriters, technical writers, documentation writers, editors (as people);
  2. bloggers, publishers of sites or blogs, site authors, content creators who publish posts;
  3. students, researchers, academics, scholars, scientists, teachers, lecturers, educators, faculty;
  4. developers, programmers, coders, software engineers, devs, maintainers, open-source contributors, hackers (as programmers);
  5. note-takers, people who keep notes, personal knowledge management or PKM users, "second brain" builders, journal keepers, Zettelkasten users;
  6. teams, companies, businesses, enterprises, organisations, departments, employers, and any plan or licence named Team, Business, Enterprise, Organisation or Site;
  7. terminal users, command-line users, CLI users, people who "live in" or "work in" the terminal or shell;
  8. readers (people who read and do not write markdown), recipients of markdown files, non-technical users or colleagues who are sent or receive markdown files;
  9. people who read output, files, responses or documents produced by AI, LLMs, chatbots, assistants or agents;
  10. developers or apps that embed, integrate or build a markdown view into their own application, site or program.
- **Generic nouns.** "You", "anyone", "everyone", "people", "users" code a class only when the same sentence attaches a qualifier from that class's list (for example "anyone who receives .md files" codes class 8; "users who live in the terminal" codes class 7). Otherwise they code nothing here and go to V06.
- **Class 4 against class 10.** "Developers" with a qualifier about embedding, integrating or building into their own app codes class 10 only. Code class 4 as well only if a separate audience phrase names developers without that qualifier.
- **Class 8 against class 9.** People reading what an AI produced code class 9; code class 8 as well only if a separate phrase names readers of received files without the AI qualifier.

Hard case A. An imagined README says "A tiny viewer for people who'd rather not install an editor just to read a README someone sent them." "People" with the qualifier "read a README someone sent them" names recipients who read: **Plain readers of received markdown files**.

Hard case B. An imagined listing says "Perfect for researchers and their teams. Supports LaTeX math and citations." "Researchers" codes **Students and academics**; "their teams" is an audience phrase with "teams": **Teams, businesses and organisations**. LaTeX and citations are features and add nothing.

Hard case C. An imagined extension page says "Preview the markdown your coding agent writes, as it writes it." There is no person noun; "your" refers to the reader, but no audience noun is named and "you" has no stated qualifier sentence. Code **not stated** here; record the sentence in V06 and V36.

Hard case D. An imagined pricing table has columns "Personal" and "Enterprise". "Enterprise" is a plan named for a class 6 noun: **Teams, businesses and organisations**. "Personal" names no class.

## V06 Audience text outside the classes (verbatim, multi)

Record verbatim every audience phrase or purpose phrase about who the product is for that did not code a class in V05: generic audiences without a qualifier ("for everyone", "anyone"), purpose phrases ("for reading markdown"), and nouns on no class list ("knowledge workers", "designers", "lawyers", "power users"). "Not stated" if none.

Hard case. "Built for knowledge workers." "Knowledge workers" is on no class list; it does not code class 5 or class 6. Record it here.

## V07 What the page asks the buyer to do to get it (multi)

Answers "What does 'sold' mean here?" by the acts the page invites. Values:

- **pay or buy** (buy, purchase, price button, checkout)
- **subscribe** (a recurring plan or "subscribe")
- **download a file** (download button or link for an installer, binary or archive)
- **install from a store** (get, install or add on a store or marketplace)
- **install by a package-manager command** (a command line that installs it)
- **clone or build from source** (a clone command, a build instruction)
- **open in a browser** (use it at a URL, no install)
- **add as a dependency** (an import or dependency line for developers)
- **create an account or sign in**
- **contact sales or request a quote**
- **star, follow or watch**
- **sponsor or donate**

Decision rule. Code an act when the captured text invites it: an imperative ("Download", "Buy now", "Star us"), a button or link label captured as text, or an instruction ("run ... to install"). Do not code an act that is merely possible on the hosting site (every repository can be starred; code **star, follow or watch** only if the text asks for it).

Hard case. An imagined README ends "If this saved you time, a star helps others find it." That is an invitation: **star, follow or watch**. A README with no such sentence on a repository page that shows a star count codes nothing for stars.

## V08 Product kind (multi)

Values: **desktop application**; **browser extension**; **editor extension** (an extension, plug-in or add-on to a text editor, code editor, IDE or note-taking application); **terminal program**; **mobile application**; **component** (a library, package, widget or module others build into software); **service** (used through a web page or hosted account, no install); **other kind** (an extension to another host, such as a file manager or an operating system's quick-preview facility; quote it).

Decision rule. Code what the text calls the product or the form it is offered in: "app for Mac" codes desktop application; "CLI", "command-line", "runs in your terminal" codes terminal program; "extension for [browser]" codes browser extension; "plug-in for [editor or notes app]" codes editor extension; "library", "crate", "package for your app", "component" codes component; "web app", "in your browser, nothing to install" codes service. A desktop operating system named as where the product is available ("for Windows", "on macOS") codes **desktop application** unless the same sentence names another kind. The store or marketplace a listing sits on counts as the text naming the kind only where its listing names the kind in a field (a category or type field that reads "Extension"); the identity of the store alone does not.

Hard case. An imagined page says "Available for Windows, macOS and Linux, and as a plug-in for your favourite editor." Code **desktop application** and **editor extension**.

## V09 Reader only, or also editor (single)

Answers "Can I write in it, or only read?". Values:

- **reader, stated read-only**: the text says it does not edit, is read-only, or is "only a viewer".
- **reader, editing not stated**: the text describes viewing, reading or previewing and says nothing of editing or writing.
- **editor with rendered view**: the text says it edits or writes markdown and also shows it rendered (side-by-side preview, live preview, WYSIWYG, rendered mode).
- **editor, rendered view not stated**: the text says it edits or writes markdown and says nothing of a rendered view.

Decision rule. The word "viewer" or "reader" in the name is not a statement that it does not edit; it codes **reader, editing not stated** unless other text says read-only. "Edit in your own editor" (it sends you elsewhere to edit) is not editing by this product. If any captured page states editing, the editor values win over the reader values.

Hard case. An imagined README says "Viewer only: open the file in your editor to make changes; this window follows along." "Viewer only" is an explicit read-only statement: **reader, stated read-only**.

## V10 Platforms (multi)

Answers "Will it run on my machine?" (first half). Values: **Windows**; **macOS**; **Linux** (any named distribution counts); **BSD**; **iOS**; **iPadOS**; **Android**; **ChromeOS**; **any desktop with a web browser** (stated as such); **inside a host program** (an extension stated to run in a named host, platform of the host not stated).

Decision rule. Code a platform when the text names it, including in a listing's compatibility or requirements field ("Requires macOS 13 or later" codes macOS). The store's identity alone codes nothing. "Cross-platform" with no platform named codes nothing here; quote it in R6. A downloadable file named for a platform (an ".exe", ".dmg", ".deb") codes the platform only if the text names the platform beside it; a file extension is not text naming a platform.

Hard case. An imagined release list shows "app-1.2.dmg, app-1.2.exe, app-1.2.AppImage" and nothing else. No platform is named in words: **not stated**, with a note quoting the file names. The same list with headings "macOS / Windows / Linux" codes all three.

## V11 Prerequisites (multi)

Answers "...and what do I need installed first?". Values:

- **none needed, stated** ("no dependencies", "nothing else to install", "single binary")
- **runtime or interpreter named** (a language runtime, framework or toolkit the buyer must install)
- **host program named** (the editor, browser or application it extends)
- **package manager named as required to install** (not merely offered)
- **build toolchain named** (a compiler or build tool the buyer must have)
- **minimum operating-system version named**

Decision rule. Code only what the text says is needed before the product will run or install. An install route offered among others (a package-manager line beside a download link) is a channel (V21), not a prerequisite. A runtime named only as what the product is written in ("built with X") is not stated as required.

Hard case. An imagined README says "Written in a scripting language; install its interpreter, then run the script." The interpreter is stated as required: **runtime or interpreter named**. A README that says only "Written in a scripting language" codes **not stated**.

## V12 Install and keep current (two fields, each multi)

Answers "How do I install it, and how do I keep it current?".

(a) Install method: **run an installer or open a package file**; **store install**; **package-manager command**; **copy or unpack a binary**; **build or run from source**; **host program's extension manager**; **open a URL**.

(b) Update method: **updates itself, stated**; **through the store**; **through the package manager**; **download the new version by hand, stated**; **no updates planned, stated**.

Decision rule. (a) codes the methods the text describes or instructs. (b) codes only an explicit statement about how new versions arrive. A store listing does not state that updates come through the store unless its text says so. A changelog is not an update method.

Hard case. An imagined page says "Install with your package manager; upgrade the same way." (a) **package-manager command**; (b) **through the package manager**. If it said only the first clause, (b) is **not stated**.

## V13 Markdown forms claimed (two fields)

Answers "Will it open my files? Which flavour, and what happens to the parts it does not understand?".

(a) Forms claimed (multi): **CommonMark**; **GitHub Flavored Markdown**; **other named flavour** (quote it: MultiMarkdown, Pandoc, a wiki dialect, a notebook or report dialect, and so on); **tables**; **task lists**; **footnotes**; **math**; **diagrams**; **syntax-highlighted code blocks**; **front matter**; **wiki-links**; **raw HTML**; **emoji shortcodes**; **callouts or admonitions**; **markdown named, no form named**.

(b) Unrecognised content (single): **shown as plain text, stated**; **dropped or hidden, stated**; **warned about, stated**; **not stated**.

Decision rule. (a) Code a form only where the text claims the product shows or edits it. These words code these forms and no others: checklists, checkboxes, to-do items code **task lists**; equations, formulas, LaTeX, TeX, KaTeX, MathJax code **math**; flowcharts, sequence diagrams, a named diagram language code **diagrams**; code highlighting, highlighted code code **syntax-highlighted code blocks**; YAML or TOML header, metadata block code **front matter**; double-bracket links code **wiki-links**; any other word for a form not on this list is quoted in R6 and codes nothing. "GFM" and "GitHub-style markdown" code GitHub Flavored Markdown; do not also code tables or task lists unless they are named separately. "Full markdown support" codes **markdown named, no form named**. A form named only as unsupported ("no footnotes yet") is not coded in (a); quote it in R6. (b) Code only a direct statement about content the product does not understand.

Hard case. An imagined feature list reads "Tables, checklists, LaTeX, flowcharts." "Checklists" are task lists; "LaTeX" is math; "flowcharts" are diagrams. Code **tables**, **task lists**, **math**, **diagrams**.

# Part 3: data, money and terms

## V14 Whether files stay local (single)

Values:

- **local, stated**: the text says files or content stay on the device, are not uploaded, or that it works on local files without a server.
- **local by default, optional upload stated**: as above, with an optional sync, share, cloud or AI feature that sends content away.
- **content leaves the device, stated**: the text says files or content are stored on or sent to a server as part of normal use.

Decision rule. Code only statements about the user's files or document content. Statements about telemetry go to V15. "Works offline" alone is not a statement about files staying local; it goes to V15. "Open files from your disk" describes where files come from, not that nothing leaves; it codes nothing here.

Hard case. An imagined page says "Your notes never leave your laptop unless you turn on sync." **Local by default, optional upload stated.**

## V15 Network and data leaving (multi)

Answers "Does it need the network, and does anything leave my machine?". Values: **works offline, stated**; **network required, stated**; **network used for named features only, stated** (quote the features); **no telemetry or tracking, stated**; **telemetry, analytics or crash reports sent, stated**; **account required, stated**.

Decision rule. Code each explicit statement. A privacy-policy link with no captured policy text codes nothing. A store's standard privacy label captured as text counts as the product's statement only where the listing presents it as the developer's declaration; quote it.

Hard case. An imagined listing's privacy label reads "Data not collected", declared by the developer. Code **no telemetry or tracking, stated**, with the quote.

## V16 Price and licence (three fields)

Answers "What does it cost?" and carries the licence.

(a) Price as published (verbatim, multi): every price with its currency, period and the unit it applies to, exactly as written. "Free" written as a price counts.

(b) Price shape (multi): **free**; **free with paid tier or features**; **one-time purchase**; **one-time purchase with paid upgrades**; **subscription**; **free trial, then paid**; **pay what you want**; **donation or sponsorship invited, use free**; **paid licence for a named use** (commercial, business or work use priced or sold separately while other use is free); **price on request** (the text asks the buyer to ask for a price).

(c) Licence (multi): **named open-source licence** (record the name verbatim); **source available, not open-source, stated**; **proprietary or end-user licence agreement, stated**; **public domain, stated**.

Decision rule. (b) is coded from the words of the page and the listing's price field. A store listing that shows "Free" with "In-app purchases" codes **free with paid tier or features**. A repository with no price text codes **not stated** for (a) and (b), not "free": silence on price is not a price. (c) codes the licence named in the text or in the repository's licence field captured as text; a licence file that was not captured codes nothing.

Hard case. An imagined README says "MIT licence. Free for personal use; a commercial licence is available." (a) "Free for personal use"; (b) **free** and **paid licence for a named use**, not **free with paid tier or features**, since what is paid for is a use, not a tier or a feature, and not **price on request**, since no request is mentioned; (c) "MIT licence". V18 carries the commercial-use statement.

## V17 Cost beyond the price (multi)

Answers "...and what does it cost me beyond the price to use it?". Values: **another product or subscription required, stated**; **own API key or service account required, stated**; **account with the maker required, stated**; **paid support or setup required, stated**; **no other cost, stated**.

Decision rule. Code only what the text states the buyer must have or pay to use the product or a named feature. Prerequisites that are free software are V11, not here, unless the text says they cost money.

Hard case. An imagined page says "AI summaries use your own key from your provider." **Own API key or service account required, stated.** The cost of that key is not stated and is not coded.

## V18 Use at work (multi)

Answers "Can I use it at work? Under what terms, and does my employer need a licence?". Values: **commercial or work use free, stated**; **commercial or work use needs a paid licence, stated**; **team, business or volume licence offered**; **work use restricted or forbidden, stated**.

Decision rule. Code only explicit statements about commercial, business, work or organisational use, or an offered licence for those buyers. Do not code from the licence name in V16(c): an open-source licence is not a statement that work use is free.

Hard case. An imagined listing says "Personal licence. Using it at your job? Grab a Business seat." Code **commercial or work use needs a paid licence, stated** and **team, business or volume licence offered**.

## V19 The unit a buyer takes (multi)

Answers "What am I getting one of?". Values: **a copy to download or install**; **a licence per person**; **a licence per device**; **a subscription per person**; **a licence or subscription per organisation, team or site**; **a package the system's package manager maintains**; **a component built into the buyer's software**; **an account on a service**; **support or a support contract**.

Decision rule. Code the unit the text names as what is sold, given or licensed. A "per user" price codes licence per person, or subscription per person where the price has a period. A free download with no licence unit named codes **a copy to download or install**. Where the text names no unit and offers no download, code **not stated**.

Hard case. An imagined page prices "$4 per month, use it on all your devices". Periodic, per buyer, not per device: **a subscription per person**. "All your devices" is a use term, not a per-device licence.

## V20 The surface the product sells on (multi)

Values: **application store listing**; **extension marketplace listing**; **package registry page**; **code repository page**; **release page**; **maker's own website**; **web store or checkout page**.

Decision rule. Code the kinds of captured page on which the product presents itself to a buyer, read from the captured URLs and the page's own text. This variable is coded from the capture record, so "not stated" applies only if no page was captured, which eligibility already excludes.

Hard case. A profile captured a repository page and a single-page site on the repository host's page service whose text is the maker's own pitch. The second is **maker's own website**: the page is the maker's, whatever host serves it. If its text is only the README rendered again, code undecidable and note it.

## V21 Distribution channels named (verbatim, multi)

Record verbatim the name of every place the captured text names as somewhere to get the product: each store, marketplace, package manager or registry, release page, download page, website. Record the count. "Not stated" if the text names no place.

Decision rule. Copy names, do not class them here; V22 classes them. A channel shown only as a badge image is not text and is not recorded. A channel named as planned ("coming soon to...") is recorded with "(planned)" after it.

Hard case. An imagined README says "Grab a build from Releases, or install via your distro's package manager." Record "Releases" and "your distro's package manager". The second names no particular package manager; record it as written.

## V22 Shape dimension 1: how the buyer reaches the offering (multi)

Values: **through an application store or marketplace**; **through a package repository or package manager**; **by downloading a release or binary from the maker**; **by cloning or downloading source and running or building it**; **by opening it in a browser**; **by adding it as a dependency**.

Decision rule. Class each entry of V21, and each route instructed in V12(a), into these values by the place's kind. Planned channels are not coded. This is the shape note's first dimension; the coding clerk does not compare it with the operator.

Hard case. "Download the zip of the repository and double-click run.sh." The zip is the source: **by cloning or downloading source and running or building it**, not a release download.

## V23 Shape dimension 2: whether anything is paid before it is reached (single)

Values: **nothing paid before use, stated**; **payment required before first use, stated**; **free trial, then payment**; **free use, payment for more**; **donation invited, not required**.

Decision rule. Code from V16(a) and (b) text and the page's own words only. "Free" stated as the price codes **nothing paid before use, stated**. Where the page states both a free tier and a paid tier, code **free use, payment for more**. No price text at all: **not stated**.

Hard case. An imagined listing shows "Free" in its price field and "Unlock Pro: $9.99" in its description. Code **free use, payment for more**.

## V24 Shape dimension 3: how the sale is taken (multi)

Values: **purchase through a store or marketplace**; **in-app purchase**; **checkout or licence key from the maker or a payment processor**; **subscription account with the maker**; **sponsorship or donation platform**; **contact sales**; **no sale taken, stated** (the text says it is free with nothing to buy).

Decision rule. Code the mechanism the text names or the buy link's labelled destination captured as text. "Buy a licence" with no mechanism named codes **not stated**, with a note. A free product with no statement that nothing is sold codes **not stated**, not **no sale taken**.

Hard case. An imagined README says "Free forever. If you'd like to support development, there's a sponsor link above." Code **no sale taken, stated** ("Free forever" says nothing is sold) and **sponsorship or donation platform**.

## V25 Shape dimension 4: whether and how a place is held (single)

Values: **capacity limit on buyers stated** (waitlist, invitation only, limited seats or places, closed beta); **per-licence use limit stated** (a number of devices, seats or installs per licence); **no limit, stated** (the text says copies, seats or devices are unlimited).

Decision rule. Code the limit the text states. "Use on all your devices" codes **no limit, stated**. A per-licence device count is a use limit, not a held place: code **per-licence use limit stated**. If both a capacity limit and a per-licence limit are stated, code **capacity limit on buyers stated** and note the other.

Hard case. An imagined page reads "Join the waitlist for the beta. Each licence covers three machines." Both apply; the rule codes **capacity limit on buyers stated** and notes the three-machine limit.

# Part 4: time and continuity

## V26 Release cadence and timing (single)

Answers "When? Does it matter when in the year I come looking, and does the product change on a cadence I should know about?". Values: **scheduled cadence stated** (quote: "monthly releases", "every quarter"); **frequent or continuous updates claimed, no schedule**; **feature-complete or no further releases planned, stated**; **seasonal or dated offer stated** (a sale, a launch price ending on a date, an academic-year offer).

Decision rule. Code an explicit statement. A changelog or release list with many dates is not a cadence statement and codes nothing here (V27 reads dates). Where two values apply, code the first in the list above and note the second.

Hard case. An imagined page says "Launch price until 31 March; we ship updates every two weeks." Both a cadence and a dated offer: precedence gives **scheduled cadence stated**, with the dated offer in the note.

## V27 Last release and archived status (two fields)

Answers "...will it still exist next year?" with V35.

(a) Last release date (single): the latest date the captured text gives for a release, version or listing update, written as published with its precision (day, month or year), and the field it came from. **Not stated** if no such date.

(b) Maintenance status (single): **archived, deprecated or unmaintained, stated** (including a repository host's archived banner captured as text); **actively maintained, stated**; **not stated**.

Decision rule. (a) Use release, version, "updated" and "last updated" fields and dated changelog entries. A last-commit date on a repository page counts only if captured as text and labelled as such; record it with "(commit)" so it is not read as a release. Take the latest date on any captured page. A copyright year in a footer is not a release date. (b) If any captured page states archived, deprecated or unmaintained, that value wins.

Hard case. An imagined repository page shows "Latest release v2.0, 2023-05-02" and "Last commit 2026-01-14". Code (a) "2023-05-02 (release)" and note "2026-01-14 (commit)"; the latest *release* date is the coded value, since the commit date is labelled "(commit)" and is not a release.

# Part 5: while reading and after

## V28 Finding the way around a long document (multi)

Values: **outline, contents or headings sidebar**; **jump to heading or section**; **folding of sections**; **minimap or overview strip**; **scroll position kept or synchronised**; **bookmarks**.

Decision rule. Code features the text names. "Table of contents" counts as outline whether shown in a sidebar or inserted in the document; note which.

Hard case. "Generate a TOC at the top of your document." That is an inserted contents list: code **outline, contents or headings sidebar** with the note "inserted".

## V29 Finding a word (multi)

Values: **search within the document**; **search across files or a folder**; **regular-expression search**; **find and replace**.

Decision rule. Code features the text names. "Search" with no scope named codes **search within the document** only if the sentence is about the open document; otherwise undecidable with a note.

Hard case. "Lightning-fast search." No scope is named and the sentence is not about the open document: **undecidable**, quoted.

## V30 Links, images and references to other files (multi)

Answers "What happens when I click a link, an image, or a reference to another file?". Values: **follows links to other markdown files inside the product**; **opens web links in the browser**; **shows local images**; **shows remote images**; **follows wiki-links or backlinks**; **resolves reference-style links**; **follows links to headings within the document**.

Decision rule. Code what the text says happens. "Supports links" or "supports images" with no behaviour stated codes nothing here and is noted; that is a claim about rendering, which V13 does not carry either.

Hard case. "Click a link to another note and it opens right here." **Follows links to other markdown files inside the product.**

## V31 Keeping up with a file edited elsewhere (single)

Values: **reloads when the file changes on disk, stated**; **preview updates as you type inside the product, stated**; **both stated**; **manual refresh, stated**.

Decision rule. "Live preview" in an editor means the preview follows the product's own editing: **preview updates as you type inside the product, stated**. Only a statement about changes made by another program or on disk codes the first value.

Hard case. "Live preview that follows your editor." The product is a viewer and the editor is another program: **reloads when the file changes on disk, stated**. If the text does not make clear whether "your editor" is another program, code undecidable.

## V32 Appearance (multi)

Values: **themes provided**; **light and dark modes**; **custom stylesheet**; **font or size choice**; **follows the system appearance, stated**.

Decision rule. Code named features. "Beautiful typography" is a description, not a choice offered to the buyer; it codes nothing.

Hard case. "Pick from five built-in looks or drop in your own CSS." **Themes provided** and **custom stylesheet**.

## V33 Print, export, send on (multi)

Values: **print**; **export to PDF**; **export to HTML**; **export to another named format** (quote it); **copy as rich text or HTML**; **share or send from the product**.

Decision rule. Code what the text says the product does. "Print to PDF" codes **print** and **export to PDF** only if the sentence presents PDF as a result the product produces; "print (use your system's save-as-PDF)" codes **print** only.

Hard case. "Export to anything Pandoc supports." Pandoc formats are not named one by one: code **export to another named format** with the quote, and do not list formats.

## V34 Help and what happens when it breaks (multi)

Values: **issue tracker**; **email or contact form**; **forum, chat or community**; **documentation or guide**; **paid or priority support**; **no support offered, stated**.

Decision rule. Code channels the text names or invites the buyer to use. A repository's issues tab that the text never mentions codes nothing.

Hard case. "Found a bug? Open an issue. Questions go to the discussion board." **Issue tracker** and **forum, chat or community**.

## V35 Who else uses it (multi)

Answers "Who else uses it?". Values: **user, download or install count claimed** (quote the number); **rating or review score shown on the listing** (quote it); **testimonials or quoted users**; **named customer organisations**; **press mentions quoted**.

Decision rule. Code what appears as text on the captured pages, including a listing's own rating or download field captured as text. Do not code counts shown only in images or badges. Third-party standing marks go to R5, not here.

Hard case. An imagined listing shows "4.7 ★ (212 ratings)" and "10K+ downloads" as text fields. Code **rating or review score shown on the listing** and **user, download or install count claimed**, both quoted.

## V36 AI-related claims (multi)

Values: **AI features in the product** (generation, summary, chat, rewriting, completion); **made for reading or editing AI output**; **works with AI agents or tools** (an integration, a protocol, an agent reading or writing through the product); **no AI, stated**; **made with AI, stated** (the maker says AI built or wrote the product).

Decision rule. Code only text that names AI, artificial intelligence, LLMs, language models, chatbots, assistants (in the AI sense) or agents (in the AI sense), or names a particular AI model or service. Quote every value.

Hard case. "Your assistant drafts, you polish." "Assistant" without any AI term may be a person: **undecidable** unless the same page says the assistant is AI.

## V37 Why the product exists (verbatim)

Record verbatim the first sentence, in reading order on the maker's own page, else on the listing, that gives a reason for making the product: a problem the maker had, a gap in other products, a motive ("I built this because...", "Existing tools were too heavy, so...", "Born out of...", a heading such as "Why" or "Motivation" and the first sentence under it). Record the URL. "Not stated" if no sentence gives a reason.

Decision rule. A tagline that says what the product is or does ("A fast markdown viewer") is not a reason. A sentence that says what the product is *not* only counts if it gives the reason in the same sentence.

Hard case. Under an imagined heading "Why?" the first sentence is "Because opening a whole IDE to read one file is silly." Record it whole, including "Because".

# Variable count

Thirty-seven variables, V01 to V37, plus the six row record fields R1 to R6, which are copied, not coded.

# Freeze

Version 1, frozen 2026-10-09, before any frame was drawn or any product page seen by its drafter. Any change to a rule above takes version 2 with its date, a line here saying what changed, and re-coding of every row coded under version 1.
