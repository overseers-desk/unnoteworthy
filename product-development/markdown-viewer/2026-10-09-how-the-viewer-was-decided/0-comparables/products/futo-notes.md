# FUTO Notes (slug futo-notes)

Shard-03. Weight 2 (AlternativeTo sampled stratum). Cell condition: re-check eligibility on own page; rates dated to the list.
Names as published: "FUTO Notes" (AlternativeTo, site); the site's blog records an earlier name: "FUTO Notes 1.3.1 — and the name goes back to FUTO Notes ... stonefruit is renamed back to FUTO Notes" and "the app briefly becomes Stonefruit" (llms.txt index).

## Pages read (all 2026-10-09)

- https://alternativeto.net/software/obsidian/?p=3 : list page; plain curl returns HTTP 403; read by headless browser dump (exit 0). Page text: "Obsidian alternatives page was last updated Oct 4, 2026".
- Finding the product's own page: web search "FUTO Notes app markdown notes" (WebSearch tool, 2026-10-09) returned https://notes.futo.tech/ among its results; that page is the one read below.
- https://notes.futo.tech/ : HTTP 200
- https://notes.futo.tech/llms.txt : HTTP 200
- https://notes.futo.tech/docs/faq.md : HTTP 200
- https://notes.futo.tech/docs/markdown.md : HTTP 200
- https://notes.futo.tech/docs/license.md : HTTP 200 (fetched; not quoted below beyond llms.txt and FAQ statements)
- https://notes.futo.tech/privacy.md : HTTP 200 (fetched; not quoted below beyond the FAQ and llms.txt statements)

AlternativeTo entry, https://alternativeto.net/software/obsidian/?p=3: "FUTO Notes 21 likes  Markdown notes stored as plain files, no database required, ensuring no lock-in. Works fully offline, has first-class self-hosted end-to-end encrypted sync, no ads, no analytics, no tracking, and maintains user privacy and transparency at all times.  Cost / License: Free, Source Available  Application type: Note-taking  Origin: United States  Platforms: Mac, Windows, Linux, Android, iPhone, ... +5"

## V01 Eligibility

Site: "FUTO Notes — private, local-first notes for every device" ; "Plain markdown you own, with end-to-end encrypted sync to a server you run". llms.txt: "FUTO Notes is a note-taking app built on plain markdown files."

## V02 Name as published

"FUTO Notes" (site title; AlternativeTo)

## V03 Name form

"FUTO Notes"

## V04 One thing or several

silent

## V05 Whom the product sells to

silent

## V06 Audience text outside the classes

Site: "Your notes belong to you" (site heading). FAQ: "Short answers to the questions people ask most about FUTO Notes."

## V07 What the page asks the buyer to do to get it

Site: "Download FUTO Notes" ; "Get FUTO Notes  Pick the build for your device, or switch platforms manually. Beta release". FAQ: "Are any FUTO Notes features behind a payment? No. Version 1.8.0 has no paid tier, no license key, and no in-app purchase, so every feature works as soon as you install it."

## V08 Product kind

Site: "Native on iOS and Android, with a real desktop app for Linux, macOS, and Windows." llms.txt: "The desktop app is built on Tauri (not a Chromium bundle)."

## V09 Reader only, or also editor

Site: "Markdown under the hood, but you never have to think about it." ; "the syntax melts away as you type, leaving plain text you own". FAQ: not separately stated.

## V10 Platforms

Site: "Linux · Android · iOS · macOS · Windows" ; "macOS 11 or later  Latest macOS build from GitLab releases." ; "Windows 10 and 11  Signed installer for current Windows devices." FAQ: "**iPhone and iPad** on iOS or iPadOS 18 or later" ; "**Android** 9 or later, from Google Play, F-Droid, Obtainium, or an APK" ; "**macOS** 11 or later, on Apple silicon and Intel" ; "**Windows**, 64-bit" ; "**Linux**, x86_64, from apt, dnf, or an AppImage"

## V11 Prerequisites

llms.txt: "Windows ... Signed x64 setup.exe, the WebView2 requirement, per-user install" (page index text). Site: "Requires the Obtainium app." ; "Requires the F-Droid app."

## V12 Install and keep current

Site: "Auto-updating sideload  Track our GitLab releases and update automatically with Obtainium." ; "Install and update through the FUTO F-Droid repo." ; "Download AppImage" ; apt and dnf command blocks ("sudo apt update && sudo apt install futo-notes" ; "sudo dnf install futo-notes"). FAQ: "How does FUTO Notes update? On macOS, Windows, and the Linux AppImage, the app updates itself when you click. Otherwise apt, dnf, or your app store updates it."

## V13 Markdown forms claimed

FAQ markdown page: "FUTO Notes saves every note as a plain `.md` file and supports CommonMark plus the GitHub extensions: tables, task lists, strikethrough, and bare URLs as links." Site: "Headings, **bold**, checklists, tables, [[wikilinks]], and fenced code" ; llms.txt: "Notes support markdown formatting, wikilinks, tags, checklists, and tables." Markdown page: "Code block ... optionally followed by a language" ; "Wikilink `[[Note title]]`" ; "Tag `#tag`"

## V14 Whether files stay local

Site: "No internet connection, works fully offline" ; "Plain markdown you own". FAQ: "Plain markdown. Each note is one `.md` file named after its title, and each folder in the app is a real folder on disk. There is no database, so any text editor can open your notes." ; "Your notes are files on your device, and search runs on the device too."

## V15 Network and data leaving

FAQ: "Does FUTO Notes collect telemetry? No. There is no analytics or usage tracking. With the default settings, the only request the app makes by itself is the desktop update check, which you can turn off. Crash reports are sent only when you press Send, or when you turn on sending them automatically." ; "Do I need an account to use FUTO Notes? No." ; "Does FUTO Notes work offline? Yes." llms.txt: "There is no analytics, advertising, or tracking." ; sync: "Every note and image is encrypted on your device with AES-256-GCM before upload, and the server stores only ciphertext."

## V16 Price and licence

FAQ: "Version 1.8.0 has no paid tier, no license key, and no in-app purchase". llms.txt: "The app is licensed under the FUTO Source First License 1.1-kb, which allows using it for any purpose. The server is licensed under the Source First License 1.1, which allows only non-commercial use. Both licenses allow modifying the code only for non-commercial purposes, and sharing copies only free of charge for non-commercial purposes. Neither is OSI-approved." FAQ: "The licenses are not OSI-approved: modifying and redistributing the code is limited to non-commercial purposes". AlternativeTo: "Cost / License Free, Source Available".

## V17 Cost beyond the price

FAQ: "Is there a FUTO sync service? Not today. To sync between devices, you run the sync server yourself." (optional sync)

## V18 Use at work

llms.txt: "The app is licensed under the FUTO Source First License 1.1-kb, which allows using it for any purpose." ; "The server is licensed under the Source First License 1.1, which allows only non-commercial use." Changelog index: "FUTO Notes 1.7.1 — 2026-08-31 — the licence now permits commercial use".

## V19 The unit a buyer takes

silent

## V20 The surface the product sells on

AlternativeTo list page; maker's own website notes.futo.tech; application store listings named in llms.txt (App Store, Google Play); release pages on gitlab.futo.org.

## V21 Distribution channels named

llms.txt "## Download": "App Store (iOS): https://apps.apple.com/us/app/futo-notes/id6758355468" ; "Google Play (Android): https://play.google.com/store/apps/details?id=com.futo.notes" ; "F-Droid (Android): https://app.futo.org/fdroid/repo" ; "Linux, macOS, Windows: https://notes.futo.tech/#download" ; "Latest release artifacts: https://gitlab.futo.org/futo-notes/futo-notes/-/releases/permalink/latest" ; site: "Obtainium", "GitLab releases", "apt", "dnf", "AppImage"

## V22 Shape dimension 1: how the buyer reaches the offering

silent

## V23 Shape dimension 2: whether anything is paid before it is reached

silent

## V24 Shape dimension 3: how the sale is taken

silent

## V25 Shape dimension 4: whether and how a place is held

silent

## V26 Release cadence and timing

silent

## V27 Last release and archived status

llms.txt changelog index: "FUTO Notes 1.8.0 ... 2026-09-17" ; FAQ: "Version 1.8.0". Site: "Beta release".

## V28 Finding the way around a long document

silent

## V29 Finding a word

FAQ: "Does FUTO Notes work offline? ... search runs on the device too." ; llms.txt page index: "Search: How on-device search matches and ranks notes, opening results in a new tab, and find in note" ; changelog 1.8.0: "find in note"

## V30 Links, images and references to other files

FAQ: "Notes, folders, `[[wikilinks]]`, tags, checklists, and tables carry over. Embeds, aliases, and plugins don't." ; Markdown page: "`[[wikilinks]]` show as links" ; "Image `![](image.png)`" ; llms.txt: "[[wikilink]] autocomplete, folder paths, broken links, links rewritten on rename"

## V31 Keeping up with a file edited elsewhere

Markdown page: "The editor formats it in place, hiding the syntax on every line except the one you're editing." (live formatting in the product's own editor). External-change statement: silent.

## V32 Appearance

llms.txt changelog: "a new colour palette and code-block syntax highlighting" (1.3.2); site: silent otherwise.

## V33 Print, export, send on

silent

## V34 Help and what happens when it breaks

FAQ: "How do I report a bug in FUTO Notes? In the app, open Settings → Send feedback. You can attach screenshots, and you don't need an account." ; llms.txt: "Docs", "FAQ", "Changelog"

## V35 Who else uses it

AlternativeTo: "21 likes". Site: none.

## V36 AI-related claims

llms.txt is a file titled for language-model readers: "Every page has a markdown twin, generated from the page at build time. Fetch the .md URL below, request the HTML page with `Accept: text/markdown`, or read llms-full.txt for the whole site in one file." No AI feature claim in the product text read.

## V37 Why the product exists

silent
