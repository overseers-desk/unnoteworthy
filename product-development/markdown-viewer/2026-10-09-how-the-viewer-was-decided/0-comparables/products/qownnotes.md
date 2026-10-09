# qownnotes: verbatim profile

Cells: alternativeto:Obsidian; Flathub; Snap Store (weight 1). Conditions obeyed: AlternativeTo: eligibility re-checked on own page, rates dated to the list; Flathub: census of search hits, price not stated by the list; Snap Store: undisclosed top-100, no rate against Flathub, an empty price map ({}) is not free. Price is recorded below only from the words of pages that state it.

## Names as published
- "QOwnNotes" (Flathub, Snap Store "qownnotes", site, README, AlternativeTo)

## How the AlternativeTo entry was found
Start URL https://alternativeto.net/software/obsidian/?p=2 is a list page (entry link not captured). Web search "QOwnNotes alternativeto.net" returned result URLs of the form https://alternativeto.net/software/qownnotes/?p=N, which name the entry's slug "qownnotes". The entry's page https://alternativeto.net/software/qownnotes/about/ was then read. Both AlternativeTo pages answer curl with HTTP 403; they were read through the WebFetch tool, which returns a model-condensed rendering, so the AlternativeTo quotes below are as that tool returned them.

## Pages read (all captured 2026-10-09)
- https://alternativeto.net/software/obsidian/?p=2 : curl HTTP 403; WebFetch returned the QOwnNotes row
- https://alternativeto.net/software/qownnotes/ : curl HTTP 403 (not read through another route)
- https://alternativeto.net/software/qownnotes/about/ : read through WebFetch
- https://flathub.org/apps/org.qownnotes.QOwnNotes : HTTP 200 (final URL https://flathub.org/en/apps/org.qownnotes.QOwnNotes)
- https://flathub.org/api/v2/appstream/org.qownnotes.QOwnNotes : HTTP 200
- https://snapcraft.io/qownnotes : HTTP 200
- https://api.snapcraft.io/v2/snaps/info/qownnotes?fields=... : HTTP 400 (not used)
- https://www.qownnotes.org/ : HTTP 200
- https://www.qownnotes.org/installation/ : HTTP 200 (page body listed install-method titles only)
- https://www.qownnotes.org/getting-started/ : HTTP 403
- https://www.qownnotes.org/contact/ : HTTP 404
- https://raw.githubusercontent.com/pbek/QOwnNotes/main/README.md : HTTP 200
- https://api.github.com/repos/pbek/QOwnNotes and .../releases : HTTP 200
- Linked and not read: ./PRIVACY.md, https://www.qownnotes.org/changelog.html

## V01 Eligibility
Frame record of the AlternativeTo row: "Plain text notepad with markdown support and todo list manager for Linux, Mac OS X and Windows, that works together with the notes application of ownCloud." Flathub: "Markdown note-taking". README: "QOwnNotes is the open source notepad with Markdown support and todo list manager for GNU/Linux, macOS and Windows". Site: "Free open source plain-text file markdown note-taking with Nextcloud / ownCloud integration".

## V02 Name as published
See "Names as published".

## V03 Name form
Silent

## V04 One thing or several
README: "QOwnNotes Web Companion browser extension"; "QOwnNotes Android"; "QOwnNotes Web App"; "QOwnNotes Tor Hidden Service"; "Nextcloud API App" (README link bar). Installation page menu: "QOwnNotes TUI", "QOwnNotes Android", "QOwnNotes Web App", "Command-line Snippet Manager".

## V05 Whom the product sells to
README: "If you like the concept of having notes accessible in plain text files, like it is done in the Nextcloud / ownCloud notes apps to gain a maximum of freedom then QOwnNotes is for you." Site: "Own your notes".

## V06 Audience text outside the classes
Silent

## V07 What the page asks the buyer to do to get it
Site: "Quick Start →". Snap Store: "sudo snap install qownnotes". Flathub: "Install". README: "Please visit [Installation](https://www.qownnotes.org/installation) for all the ways to install QOwnNotes."; "To get the most current features you can build the application from the source code. Download the latest source here"; "git clone https://github.com/pbek/QOwnNotes.git -b release --depth=1".

## V08 Product kind
Flathub: "desktop-application" (appstream type); page: "Desktop Only". Site: "Native application, optimized for speed and consuming little processor and memory resources." README: "written in C++ and optimized for low resource consumption (no CPU and memory-hungry Electron app)". Installation menu also names "QOwnNotes TUI - Your notes in the terminal".

## V09 Reader only, or also editor
README: "markdown highlighting of notes and a markdown preview"; "tabbing support for editing notes"; "Vim mode"; "distraction free mode, full-screen mode, typewriter mode".

## V10 Platforms
README: "for GNU/Linux, macOS and Windows". Flathub: "Desktop Only"; "Available Architectures: x86_64, aarch64". Snap description: "for GNU/Linux, macOS and Windows". AlternativeTo: "Mac, Windows, Linux, Flathub, PortableApps.com, Qt". Flathub description: "for GNU/Linux, Mac OS X and Windows". README: "For Android (default): QOwnNotes Android".

## V11 Prerequisites
README: "Minimum software requirements - A desktop operating system, that supports [Qt](https://www.qt.io) - Qt 5.5+ / Qt 6.0+ - gcc 4.8+" (under building). README: "that works together with Nextcloud Notes and ownCloud Notes" (sync is optional: Flathub "that (optionally) works together with the notes application of ownCloud or Nextcloud"). README: "To manage your todo lists in the web and on your mobile devices, you need to install the Tasks backend on Nextcloud or ownCloud."

## V12 Install and keep current
(a) Installation page menu: "Install on Ubuntu Linux, elementary OS and Linux Mint; Install on Microsoft Windows; Install on macOS; Install on Debian Linux; Install on openSUSE Linux; Install on Fedora Linux; Install as Snap; Install as Flatpak; Install as AppImage; Install via Nix; Install on Arch Linux; ... Install on FreeBSD; Building QOwnNotes". Snap Store: "sudo snap install qownnotes". README: build via "qmake / make -j4". (b) Installation page blog list: "Automatic updates in Windows and macOS" (title). Snap Store: "latest/stable", "latest/edge" channels.

## V13 Markdown forms claimed
README: "markdown highlighting of notes and a markdown preview - includes inline image previews, heading folding, and optional hiding of Markdown formatting syntax"; "optional wiki-style note links like `[[Note]]` with auto-completion, heading anchors, aliases, backlinks, and refactoring support"; "YAML front matter metadata" (Evernote import); Installation menu: "Markdown Cheatsheet"; "Markdown LSP". Blog titles: "Auto-format Markdown tables"; "Solve simple equations in the note editor". Task lists / math / diagrams: silent.

## V14 Whether files stay local
Site: "All notes are stored as plain-text markdown files on your computer, no "vendor lock-in". Use sync services like Nextcloud to sync notes across devices." README: "The notes are stored as plain text markdown files and are synced with Nextcloud's/ownCloud's file sync functionality."; "you can use your existing text or markdown files, no need for an import most of the time".

## V15 Network and data leaving
README: "built-in AI support with script integration for providers like OpenAI and Groq"; "includes a built-in MCP server so external AI agents can search and fetch notes securely"; "support for sharing notes on your Nextcloud / ownCloud server"; "older versions of your notes can be restored from your Nextcloud / ownCloud server". README footer: image "https://p.bekerle.com/piwik.php?idsite=3&rec=1" labelled "Matomo Stats". Installation menu FAQ title: "Why metrics?". README link: "[Privacy Policy](./PRIVACY.md)" (not read).

## V16 Price and licence
Flathub: "Free"; "open source (GPL)"; appstream project_license "GPL-2.0+". Snap Store: "License GPL-2.0" (the page shows no price field). AlternativeTo: "Licensing Open Source" and "Free product." (about page); "Free" and "Open Source (GPL-2.0)" (list page). GitHub licence field: "GNU General Public License v2.0". Site: "Free open source plain-text file markdown note-taking".

## V17 Cost beyond the price
README: "To manage your todo lists in the web and on your mobile devices, you need to install the Tasks backend on Nextcloud or ownCloud." No cost stated. Site menu: "Donate".

## V18 Use at work
Silent

## V19 The unit a buyer takes
Flathub: "26 MiB Download". Snap Store: "sudo snap install qownnotes". README: "Download the latest source here: QOwnNotes Source on GitHub as ZIP".

## V20 The surface the product sells on
Captured pages: AlternativeTo directory page, Flathub app page, Snap Store page, maker's own website (qownnotes.org), code repository page/README.

## V21 Distribution channels named
Installation page menu: "Install as Snap", "Install as Flatpak", "Install as AppImage", "Install via Nix", "Install on Ubuntu Linux, elementary OS and Linux Mint", "Install on Microsoft Windows", "Install on macOS", "Install on Debian Linux", "Install on openSUSE Linux", "Install on Fedora Linux", "Install on Arch Linux", "Install on Solus", "Install on KaOS Linux", "Install on CentOS Linux", "Install on Raspberry Pi OS", "Install on Gentoo Linux", "Install on Funtoo Linux", "Install on Void Linux", "Install on Slackware Linux", "Install on FreeBSD". README: "Packaging status" (repology badge); "Source Archive switched from TuxFamily to GitHub Releases" (blog title). AlternativeTo platforms: "Flathub", "PortableApps.com".

## V22 to V25 (shape dimensions)
Silent beyond the quotes under V07, V12, V16, V21. Site menu: "Donate" (page not read).

## V26 Release cadence and timing
Installation page blog title: "Happy 1000th release of QOwnNotes". Cadence statement: silent.

## V27 Last release and archived status
Flathub: "Changes in version 26.10.2 4 days ago". Snap Store: "latest/stable 26.10.3"; "Last updated Yesterday - latest/stable; 8 October 2026 - latest/edge". GitHub releases API: "v26.10.3 2026-10-08T18:46:27Z". Repository API: pushed_at "2026-10-09T07:20:09Z" (commit); archived: false. AlternativeTo about page: "this page was last updated Jun 2, 2025"; "GitHub section: Updated Oct 2, 2026".

## V28 Finding the way around a long document
README: "heading folding"; "linking of note headings" (blog title); "wiki-style note links ... heading anchors, aliases, backlinks"; "note tagging and note subfolders".

## V29 Finding a word
README: "sub-string searching of notes is possible and search results are highlighted in the notes". Installation menu: "Searching for notes".

## V30 Links, images and references to other files
README: "inline image previews"; "wiki-style note links like `[[Note]]`"; "linked files and attachments can be managed from the Navigation panel". Blog titles: "Open links in the note editor"; "Manage orphaned image files and attachments".

## V31 Keeping up with a file edited elsewhere
README: "external changes of note files are watched (notes or note list are reloaded)"; "differences between current note and externally changed note are shown in a dialog"; "markdown highlighting of notes and a markdown preview".

## V32 Appearance
README: "dark mode theme support, live theme switching, and custom color modes"; "support for freedesktop theme icons"; "toolbars are fully customizable"; "all panels can be placed wherever you want, they can even float or stack (fully dockable)".

## V33 Print, export, send on
README: "support for sharing notes on your Nextcloud / ownCloud server"; "Evernote ... and Joplin import". AlternativeTo tags include "pdf". Print and export: otherwise silent.

## V34 Help and what happens when it breaks
Site menu: "Ask question", "Ask for feature", "Report bug", "Telegram Channel", "Matrix/Element.io Room", "Gitter Chat", "IRC Channel", "Mastodon". Flathub: "Report an Issue https://github.com/pbek/QOwnNotes/issues". README: "report troubles on the [QOwnNotes issues page]"; link bar: "Documentation", "Issues". README disclaimer: "provided by THE PROVIDER "as is" and "with all faults.""

## V35 Who else uses it
Flathub: "1,109 Downloads/Month". AlternativeTo: "104 likes". GitHub API stargazers_count 5894. Installation page blog titles: "QOwnNotes reviewed in German magazine c't"; "QOwnNotes featured on LINUX Unplugged podcast and by Ubuntu". Third-party marks (provenance): Flathub appstream "flathub::verification::verified": true, method "website"; Snap Store "(Ownership verified) The publisher has verified that they own this domain. It does not guarantee the Snap is an official upload from the upstream project."

## V36 AI-related claims
README: "built-in AI support with script integration for providers like OpenAI and Groq"; "includes a built-in MCP server so external AI agents can search and fetch notes securely". GitHub topic list: "llm". Blog title: "AI support was added to QOwnNotes". Installation menu: "AI support".

## V37 Why the product exists
README: "You are able to write down your thoughts with QOwnNotes and edit or search for them later from your mobile device"; "If you like the concept of having notes accessible in plain text files ... to gain a maximum of freedom then QOwnNotes is for you." Site: "Own your notes. All notes are stored as plain-text markdown files on your computer, no "vendor lock-in"."
