# reinschrift: verbatim profile

Cell: Flathub (weight 1). Condition obeyed: census of search hits; price not stated by the list (Flathub's own "Free" label is quoted as published).

## Names as published
- Flathub: "Reinschrift"; site title: "Reinschrift — your todo list is a Markdown file"; README: "Reinschrift"; repository "danst0/ReinschriftTodo"; GUI binary "reinschrift_todo"

## Pages read (all captured 2026-10-09)
- https://flathub.org/apps/me.dumke.Reinschrift : HTTP 200 (final URL https://flathub.org/en/apps/me.dumke.Reinschrift)
- https://flathub.org/api/v2/appstream/me.dumke.Reinschrift : HTTP 200
- https://reinschrift.dumke.me : HTTP 200
- https://github.com/danst0/ReinschriftTodo : HTTP 200
- https://api.github.com/repos/danst0/ReinschriftTodo and .../releases (via gh) : success
- https://raw.githubusercontent.com/danst0/ReinschriftTodo/main/README.md : HTTP 200

## V01 Eligibility
Flathub: "Manage your todos in Markdown"; "Your tasks remain a normal Markdown file – easy to back up, versionable via Git, and editable on any device with your favorite editor." Site: "Your todo list is just a text file."; "all reading and writing one Markdown file". README: "Manage your todos in plain Markdown — with a native GNOME desktop app, a CLI, and a web app."

## V02 Name as published
See "Names as published".

## V03 Name form
Silent

## V04 One thing or several
Site: "Reinschrift is a native GNOME app, a top-bar extension, a CLI and a self-hostable web app — all reading and writing one Markdown file."; "Four ways in, one file". README components table: "core/ Shared Rust library", "gui/ Native GNOME app", "cli/ Command-line interface", "webapp/ Flask web app (Docker, OIDC login, PWA)". Flathub: "Other apps by Dr. Daniel Dumke: Password Generator".

## V05 Whom the product sells to
Silent

## V06 Audience text outside the classes
Silent

## V07 What the page asks the buyer to do to get it
Site: "flatpak install flathub me.dumke.Reinschrift"; "yay -S reinschrift"; "docker pull ghcr.io/danst0/reinschrift-web"; "Take the desktop app, the top bar, the CLI — or host it yourself." Flathub: "Install".

## V08 Product kind
Flathub: appstream type desktop application; page "Desktop & Mobile". Site: "a native GNOME app, a top-bar extension, a CLI and a self-hostable web app"; "Web app · PWA".

## V09 Reader only, or also editor
Flathub: "reads changes live, writes directly back". Site: "all reading and writing one Markdown file". Reading of Markdown documents as such: silent.

## V10 Platforms
Site: "GNOME desktop: The recommended way on any Linux distribution."; "GNOME Shell extension ... GNOME 47–50."; "A compact mode makes it usable on Linux phones."; "Installable on your phone as a PWA". Flathub: "Desktop & Mobile"; tags in API: gnome, flatpak.

## V11 Prerequisites
README (build): "Requirements: Rust toolchain, GTK4 and libadwaita development libraries, cmake and clang (for Whisper voice input)." Site: "Pre-built image on GHCR ... OIDC, WebDAV and credentials via environment variables." Site: "AI assistance ... via your own Ollama".

## V12 Install and keep current
(a) Site/README: "flatpak install flathub me.dumke.Reinschrift"; "yay -S reinschrift" (Arch AUR); "docker pull ghcr.io/danst0/reinschrift-web"; "git clone …/ReinschriftTodo && ReinschriftTodo/extension/install.sh"; "cargo build --workspace --release". (b) Flathub: "Updates now arrive bundled, so you get fewer, larger updates" (release note 1.2.1). Site: "Pending review on extensions.gnome.org. Until then, install it from the repository".

## V13 Markdown forms claimed
Site: "Inspired by todo.txt, but living happily inside ordinary Markdown checklists — the kind every editor, forge and notes app already renders." README: "- [ ] Task title +project @context due:2026-01-20 rec:weekly ~note:"Additional details" ^ID123 / - [x] Completed task ✅ 2026-01-15". Other Markdown forms: silent.

## V14 Whether files stay local
README: "WebDAV/Nextcloud sync — or a plain local file"; "Plain text first — one Markdown file, no database, no lock-in". Site: "No database. No silo. No lock-in."; "AI assistance ... nothing leaves your machine."

## V15 Network and data leaving
Flathub: "The app syncs the file via Nextcloud/WebDAV, reads changes live, writes directly back". Site: "WebDAV / Nextcloud sync"; "Voice input: Local transcription via Whisper on the desktop, Web Speech API in the browser."; "push reminders and OIDC login" (web app).

## V16 Price and licence
Flathub: "Free"; appstream project_license "GPL-3.0-or-later". Site: "Free software · GNOME · plain text first"; "GPL-3.0-or-later". Repository licence field: "GNU General Public License v3.0".

## V17 Cost beyond the price
Silent

## V18 Use at work
Silent

## V19 The unit a buyer takes
Flathub: "10 MiB Download".

## V20 The surface the product sells on
Captured pages: Flathub app page; maker's own website; code repository page.

## V21 Distribution channels named
Site: "flatpak install flathub me.dumke.Reinschrift"; "Arch Linux: GUI and CLI from the AUR"; "docker pull ghcr.io/danst0/reinschrift-web" (GHCR); "extensions.gnome.org (pending review)" (planned).

## V22 to V25 (shape dimensions)
Silent beyond the quotes under V07, V12, V16, V21.

## V26 Release cadence and timing
Silent

## V27 Last release and archived status
Flathub: "Changes in version 1.2.1 about 7 hours ago". Releases (API): "v1.2.1 2026-10-09T06:06:09Z"; "v1.2.0 2026-09-29T11:24:44Z"; "v1.1.9 2026-09-29T10:21:19Z". Repository: pushed_at "2026-10-09T07:24:07Z" (commit); archived: false.

## V28 Finding the way around a long document
Silent

## V29 Finding a word
Site: "Search, filter, sort: Filter by time range (overdue, today, 7 or 30 days, no date) and by several projects or places at once". README: "Search, filtering, sorting — by project, context, or due date".

## V30 Links, images and references to other files
Silent

## V31 Keeping up with a file edited elsewhere
Flathub: "reads changes live". Site: "live reload when the file changes underneath"; "External edits are picked up live." README: "external changes are picked up live".

## V32 Appearance
Silent

## V33 Print, export, send on
Silent

## V34 Help and what happens when it breaks
Flathub: "Report an Issue https://github.com/danst0/ReinschriftTodo/issues"; "Contribute to the App". 

## V35 Who else uses it
Flathub: "422 Downloads/Month". Repository page (API): stargazers_count 20, forks_count 1. Third-party mark (provenance): Flathub appstream "flathub::verification::verified": true, method "website", website "dumke.me".

## V36 AI-related claims
Site: "AI assistance: Natural-language task parsing and semantic duplicate detection via your own Ollama — nothing leaves your machine." README: "AI task parsing — turn natural language into structured tasks via Ollama/LLM (optional)".

## V37 Why the product exists
Site: "No database. No silo. No lock-in." Flathub: "makes classic to-do lists in plain text suitable for everyday use – without proprietary silos. The format remains open, portable, and transparent."
