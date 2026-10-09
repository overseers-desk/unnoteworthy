# Stik (slug stik)

Shard-13. Cell conditions: re-check eligibility on own page; rates dated to the list. Weight 2 (AlternativeTo sampling rule, position 123 of 147).
Name as published: "Stik" (README, site).

## How the product's own page was found

The start URL is an AlternativeTo list page only (entry link not captured). Web search "Stik notes app markdown Mac" (2026-10-09) returned raycast.com/0xMassi/stik, raw.githubusercontent.com/0xMassi/stik_app/main/README.md and alternativeto.net/software/stik. The frame's blurb for the row ("A keyboard-first note app for Mac. Press a shortcut, type your thought, close. Your note is saved as a plain markdown file in under 3 seconds. No account, no cloud, no setup.") was matched to this product; the repository's homepage field is https://www.stik.ink.

## Pages read (all 2026-10-09)

- https://alternativeto.net/software/obsidian/?p=24 : list page named in the collection list; not fetched
- https://alternativeto.net/software/stik/about : HTTP 403 (unreachable; no text)
- https://raw.githubusercontent.com/0xMassi/stik_app/main/README.md : HTTP 200
- https://api.github.com/repos/0xMassi/stik_app : HTTP 200; .../releases?per_page=3 : HTTP 200
- https://www.stik.ink : HTTP 200 (own site; includes a "Requirements & installation" link)
- Not read: stik.ink/download, /ideas, ROADMAP.md, CHANGELOG.md, the Raycast page

## V01 Eligibility

README: "Your note is saved as a plain markdown file." ; "Rich editor. Source-mode markdown with syntax highlighting, ==highlights==, [[wiki-links]], collapsible headings, image paste and drop, task lists, and editable tables."
Site title: "Stik: Free Quick-Capture Markdown Notes for Mac" ; "Save your thoughts as Markdown files"

## V02 Name as published

"Stik" (README heading; site); repository: "Instant thought capture for macOS. One shortcut, post-it appears, type, close." (description)

## V03 Name form

"Stik" ; "Instant thought capture for macOS." (README) ; "Capture quick notes on your Mac." (site)

## V04 One thing or several

README: "It installs as Stik Beta beside your stable copy" (beta builds)

## V05 Whom the product sells to

Site: "Built for keyboard warriors" ; "Unlike heavyweight note apps such as Notion, Obsidian, or Bear, Stik is designed for one thing: capturing fleeting thoughts before they disappear."

## V06 Audience text outside the classes

Site: "Built for keyboard warriors"

## V07 What the page asks the buyer to do to get it

README: "Grab the latest .dmg from stik.ink/download" ; "brew install --cask 0xMassi/stik/stik" ; "Download Stik for Mac". Site: "Download Stik for Mac" ; "Try it live"

## V08 Product kind

Site: "Stik is a free, open-source quick-capture note app for macOS." README Tech Stack: "Rust, Tauri 2.0"

## V09 Reader only, or also editor

README: "Rich editor. Source-mode markdown with syntax highlighting" ; "Type, close, done."

## V10 Platforms

README: "Instant thought capture for macOS." ; "Requires macOS 14+ (Sonoma)." Site: "Free · Apple Silicon · Intel Mac? · Requirements & installation"

## V11 Prerequisites

README: "On first launch, grant Accessibility permissions when prompted (needed for global shortcuts)." ; Build prerequisites: "macOS 14+ (Sonoma); Xcode Command Line Tools; Rust stable; Node.js 20+; Bun 1.4.1"

## V12 Install and keep current

README: "brew upgrade --cask stik" ; "From v0.3.3 onwards, Stik includes a built-in auto-updater that silently downloads new versions in the background. Updates apply on next app restart." ; "Beta builds ... Every push to develop produces a signed build, published under Releases as a prerelease."

## V13 Markdown forms claimed

README: "Source-mode markdown with syntax highlighting, ==highlights==, [[wiki-links]], collapsible headings, image paste and drop, task lists, and editable tables." ; "Notes are plain markdown files in ~/Documents/Stik/"

## V14 Whether files stay local

README: "Notes are plain markdown files in ~/Documents/Stik/ -- open them in any editor" ; "Settings stored locally in ~/.stik/" ; "Storage: Local filesystem (.md files), optional git sync"

## V15 Network and data leaving

README: "All AI runs on-device via Apple frameworks -- nothing is sent anywhere" ; "No account and no cloud service. Anonymous analytics are off by default and run only after you explicitly opt in; note content, titles, folders, and paths are never collected." Site: "On-device AI, zero cloud" ; "Video loads from YouTube when you press play."

## V16 Price and licence

Site: "Free and open source." ; "Free · Apple Silicon". Repository license field: "MIT".

## V17 Cost beyond the price

README: "No account and no cloud service."

## V18 Use at work

silent

## V19 The unit a buyer takes

silent

## V20 The surface the product sells on

Maker's own website https://www.stik.ink (download page); code repository page.

## V21 Distribution channels named

README: "stik.ink/download" ; "Homebrew" ; "the Releases page" ; "Raycast" is named in search results only, not in pages read.

## V22 Shape dimension 1: how the buyer reaches the offering

README: "Grab the latest .dmg from stik.ink/download" ; "Prefer GitHub? The same .dmg is on the Releases page." ; "brew install --cask 0xMassi/stik/stik"

## V23 Shape dimension 2: paid before reached

Site: "Free and open source."

## V24 Shape dimension 3: how the sale is taken

silent

## V25 Shape dimension 4: place held

silent

## V26 Release cadence and timing

GitHub API releases: v0.9.0 2026-09-08, beta-51 2026-09-08, beta-50 2026-09-06. README: "Every push to develop produces a signed build". No schedule stated.

## V27 Last release and archived status

GitHub API: latest listed release "v0.9.0" 2026-09-08; pushed_at 2026-10-05; archived false.

## V28 Finding the way around a long document

README: "collapsible headings" ; "Zen mode"

## V29 Finding a word

README: "Search everything from the command palette." Site: "Full-text search across all your notes with AI-powered semantic results."

## V30 Links, images and references

README: "[[wiki-links]], collapsible headings, image paste and drop"

## V31 Keeping up with a file edited elsewhere

silent

## V32 Appearance

README: "Themes. System, Light, Dark, or your own colors. Follows macOS appearance as it changes."

## V33 Print, export, send on

README: "Share. Copy a note as rich text, markdown, or an image. Push a folder to a git remote and Stik keeps it synced in the background."

## V34 Help and what happens when it breaks

README links: "Ideas Board", "Discord", "Roadmap", "Changelog"; "Please open an issue first to discuss what you'd like to change."

## V35 Who else uses it

Repository stargazers_count 266 (API field). README badges: "Downloads", "Stars" (counts in images).

## V36 AI-related claims

README: "On-device AI. Semantic search, folder suggestions, and note embeddings through Apple's NaturalLanguage framework. No cloud, no API keys, nothing sent anywhere." ; "Voice ... WhisperKit runs the model on the Neural Engine" ; repository topics "ai", "on-device-ai"

## V37 Why the product exists

README, "Why Stik?": "Every note app wants to be your second brain."
