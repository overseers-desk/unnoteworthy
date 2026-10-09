# alexishida-moji

Source list and cell: github-topics:markdown-viewer; github-topics:markdown-editor; github-topics:markdown-reader. Condition: rates only for repos with >=200 stars (counts only, no rates).

## Names as published
- "Moji" (README heading); "Moji (文字)" (README "## Name"); site title "Moji — Open Markdown files like PDFs."

## URLs read (date 2026-10-09)
- https://github.com/alexishida/Moji : HTTP 200
- https://raw.githubusercontent.com/alexishida/Moji/main/README.md : HTTP 200 (master path also 200, identical text)
- https://alexishida.com/moji/ (repository homepage field) : HTTP 200
- Linked, not read: GitHub Releases downloads, CHANGELOG.md

## V02 Name as published
"Moji" (README first heading, https://raw.githubusercontent.com/alexishida/Moji/main/README.md) ; site title: "Moji — Open Markdown files like PDFs." (https://alexishida.com/moji/)

## V03 Name form
silent (see V02)

## V04 One thing or several
silent

## V05 Whom the product sells to
silent

## V06 Audience text outside the classes
"Built for reading Markdown." (https://alexishida.com/moji/) ; "Double-click a Markdown file and start reading." (site)

## V07 What the page asks the buyer to do to get it
README: "Download: Windows · macOS (DMG) · Linux (AppImage) · Linux (DEB)" ; "Drag Moji from the DMG into your Applications folder." Site: "View downloads", "View on GitHub", "Download .exe", "Download .dmg", "AppImage", ".deb", "View all releases", "Open repository", "Start opening Markdown like PDFs." README development section: "npm install / npm run dev".

## V08 Product kind
"A lightweight, clean desktop app for opening, reading, editing, and exporting Markdown files." (README) ; site: "a Markdown reader for your desktop"

## V09 Reader only, or also editor
"A lightweight, clean desktop app for opening, reading, editing, and exporting Markdown files." ; "Editor mode: CodeMirror 6 Markdown editor with line numbers, history, wrapping..." ; "Live preview: while editing, toggle a resizable split view from the top bar (or Ctrl+\) to keep the rendered preview beside the source editor." (README)

## V10 Platforms
"Official installers for Windows, macOS and Linux, published directly through GitHub Releases." (site) ; README download links: "Windows", "macOS (DMG)", "Linux (AppImage)", "Linux (DEB)" ; "macOS: universal (Apple Silicon + Intel) DMG and ZIP."

## V11 Prerequisites
"Windows and Linux install from the downloads above with no extra steps." (README, Installation) ; "Requirements: Node.js ^20.19.0 || >=22.12.0 (required by Vite 7 and electron-vite 5; packaging also needs require() of ES modules, unflagged since Node 22.12) ; npm" (README, under Requirements, next to the Development section) ; "macOS refuses to open Moji the first time ... Open Anyway" (README Installation, macOS)

## V12 Install and keep current
Install: README Installation (downloads; macOS steps 1-4 and "xattr -dr com.apple.quarantine /Applications/Moji.app"; development: "npm install / npm run dev / npm run build"). Update: "Update checks: installed Windows NSIS and Linux AppImage builds check GitHub Releases and link to the release page when a newer version is available, so you can choose the correct artifact." ; "Update from GitHub Releases by downloading a new DMG." ; "Update checks stay disabled on macOS." (README). Site: "NSIS installer for Windows x64 with automatic updates." ; "Universal DMG for Apple Silicon and Intel. Manual updates." ; "AppImage with automatic updates or a DEB package for manual installation."

## V13 Markdown forms claimed
"Open Markdown files: supports .md and .markdown" ; "Preview mode: sanitized Markdown rendering with heading anchors, outline navigation, tables, task lists, footnotes, definition lists, subscript/superscript, highlight/insert marks, emoji shortcodes, LaTeX math via KaTeX ($…$ and $$…$$), linkify, typographer, syntax-highlighted code, and copy buttons for code blocks." ; "every valid fenced mermaid block supported by bundled Mermaid renders as a responsive diagram, including flowcharts, sequence, Gantt, class, ER, state, and journey diagrams" ; "malformed Mermaid blocks remain readable code blocks." (README). Site: "Full Markdown" ; "Tables, tasks, footnotes, LaTeX, code highlighting, emoji and outline navigation."

## V14 Whether files stay local
silent. README: "Local images: images referenced relative to the document are served through an authorized moji-asset:// protocol, restricted to directories of documents you actually opened". Site: "Free · open source · no account".

## V15 Network and data leaving
Site: "Free · open source · no account". README: "dev:update: ... simulate an available 99.0.0 update without network access" ; "Security: sandboxed renderer, context isolation, nodeIntegration: false, DOMPurify sanitization, and external links opened in the OS browser." Update checks of GitHub Releases quoted in V12.

## V16 Price and licence
Price: "Free · open source · no account" ; "Moji is free and distributed under the MIT license." (https://alexishida.com/moji/). Licence: "MIT © Alex Ishida" (README); "MIT license" (repository page field).

## V17 Cost beyond the price
"Free · open source · no account" (site)

## V18 Use at work
silent

## V19 The unit a buyer takes
silent

## V20 The surface the product sells on
Captured: code repository page; raw README; maker's site https://alexishida.com/moji/ (own pitch text, distinct from README).

## V21 Distribution channels named
"GitHub Releases" ; "Releases" ; site: "published directly through GitHub Releases." ; "View all releases" ; "Open repository" (README, site)

## V22 Shape dimension 1
silent

## V23 Shape dimension 2
silent

## V24 Shape dimension 3
silent

## V25 Shape dimension 4
silent

## V26 Release cadence and timing
silent

## V27 Last release and archived status
"Current version: v1.0.7" (README). Site: "Latest version" (no number captured). No dated release or commit captured as text. Repository page text: "157 Commits". Maintenance statement: silent.

## V28 Finding the way around a long document
"Outline navigation: collapsible heading tree available in Preview and Editor modes. Preview uses scroll-spy; clicking any heading scrolls preview or moves editor cursor to its Markdown source." ; "heading anchors" ; "Scrolling either pane moves the other to the matching part of the document" ; "Click any rendered SVG or Markdown image to inspect it in a modal with zoom, drag navigation, a minimap" ; "Recent files" ; "Remembered app state" (README)

## V29 Finding a word
"Search and replace: top-bar search finds visible Markdown text even across inline formatting, distinguishes the active match, and shows the active/total occurrence count. Preview offers previous/next navigation; Editor separates navigation from replace-one/replace-all controls." (README)

## V30 Links, images and references to other files
"external links opened in the OS browser" ; "Local images: images referenced relative to the document are served through an authorized moji-asset:// protocol ... loaded lazily and cached in memory." ; "heading anchors" (README)

## V31 Keeping up with a file edited elsewhere
"Live preview: while editing, toggle a resizable split view ..." (README, quoted in V09)

## V32 Appearance
"Markdown themes: dark/light toggle for rendered Markdown. App chrome remains dark; exports always use the light theme." ; "Settings view: ... language, untitled-document recovery, preview typography, editor and preview font sizes, reading width" ; "font-size (Ctrl+Plus / Ctrl+Minus / Ctrl+0...)" (README)

## V33 Print, export, send on
"Export mode: export the active document as HTML, PDF, or PNG. PDF supports A4, Letter, Legal, portrait, and landscape" ; "individual PNG export" ; "Diagram exports: rendered Mermaid diagrams are embedded as self-contained SVG in HTML, PDF, and PNG exports." (README)

## V34 Help and what happens when it breaks
Site: "Explore the code, follow development, report issues or help shape Moji's next chapter." README Documentation lists ".ai-framework/RULES.md", "openspec/specs/", "docs/performance-budget.md" (developer files).

## V35 Who else uses it
Repository page fields: "Stars 493", "Watchers 1", "Forks 54" (https://github.com/alexishida/Moji)

## V36 AI-related claims
README "Documentation": ".ai-framework/RULES.md: project rules for AI-assisted changes." Repository file list includes names ".claude", ".codex/skills", "AGENTS.md", "CLAUDE.md". README: "document-translation" appears in the list of openspec specs. Nothing else names AI.

## V37 Why the product exists
"I built Moji because I wanted a Markdown file to open the way a PDF does: with a double-click, instantly readable, with clean typography and no setup." (https://alexishida.com/moji/, under "why I built Moji"; the first sentence there is "Opening Markdown should be as simple as opening a PDF.")

## Status marks (provenance only)
none. Repository topics: "codemirror cross-platform desktop-app electron markdown markdown-editor markdown-reader markdown-viewer mermaid open-source productivity react reader-writer typescript".
