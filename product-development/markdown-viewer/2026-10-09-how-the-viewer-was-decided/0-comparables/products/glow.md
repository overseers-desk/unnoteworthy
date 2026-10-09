# Glow (slug glow)

Shard-03. Cell conditions: re-check eligibility on own page; rates dated to the list (AlternativeTo) | cell named Ubuntu 25.04 archive; no installs or recency | description-word census; installs as published, not users (Homebrew) | undisclosed top-100; no rate against Flathub; {} is not free (Snap).
Name as published: "Glow" (all pages); apt "glow"; Snap "glow".

## Pages read (all 2026-10-09)

- https://alternativeto.net/software/typora/?p=12 : list page; plain curl to AlternativeTo returns HTTP 403 ("Just a moment..."); read by headless browser dump (exit 0). Page text: "Typora alternatives page was last updated Aug 31, 2026".
- https://alternativeto.net/software/marked/?p=4 : same method (exit 0). Page text: "Marked alternatives page was last updated May 17, 2026".
- apt-cache show glow : run on the collection host (Ubuntu 25.04, plucky archive index), 2026-10-09.
- https://formulae.brew.sh/formula/glow : HTTP 200
- https://snapcraft.io/glow : HTTP 200
- https://github.com/charmbracelet/glow : linked from apt Homepage, Homebrew and Snap; read through https://api.github.com/repos/charmbracelet/glow (200), .../readme (200), .../releases?per_page=5 (200). The github.com HTML page was not fetched. charm.sh (linked from README and Snap as contact) was not read.

AlternativeTo entry, identical on both pages: "Glow 3 likes  Glow is a terminal based markdown reader designed from the ground up to bring out the beauty—and power—of the CLI.  52 Glow alternatives  Cost / License: Free, Open Source (MIT)  Platforms: Mac, Windows, Linux, BSD"

## V01 Eligibility

"Glow is a terminal based markdown reader designed from the ground up to bring out the beauty—and power—of the CLI." (README, AlternativeTo, Snap, apt) ; Homebrew: "Render markdown on the CLI"

## V02 Name as published

"Glow" (README heading, AlternativeTo, Homebrew page); Homebrew formula description: "Render markdown on the CLI"; apt Description-en: "Render Markdown on the command-line"

## V03 Name form

"Glow"; "Render markdown on the CLI, with _pizzazz_!" (README)

## V04 One thing or several

silent

## V05 Whom the product sells to

silent

## V06 Audience text outside the classes

"Use it to discover markdown files, read documentation directly on the command line." (README)

## V07 What the page asks the buyer to do to get it

README: "brew install glow" ; "sudo snap install glow" ; "sudo apt update && sudo apt install glow" ; "go install charm.land/glow/v3@latest" ; "git clone https://github.com/charmbracelet/glow.git". Homebrew: "Install command: brew install glow"

## V08 Product kind

README: "Glow is a terminal based markdown reader" ; "In addition to a TUI, Glow has a CLI for working with Markdown." ; apt: "Render Markdown on the command-line"

## V09 Reader only, or also editor

"Glow is a terminal based markdown reader" (README). Editing: "it in your favorite $EDITOR" (README, config section line as captured).

## V10 Platforms

README install sections: "# macOS or Linux", "# macOS (with MacPorts)", "# Arch Linux (btw)", "# Void Linux", "# Nix shell", "# FreeBSD", "choco install glow", "scoop install glow", "winget install charmbracelet.glow". AlternativeTo: "Platforms Mac Windows Linux BSD". Homebrew bottle table: "macOS on Apple Silicon: golden gate, tahoe, sequoia, sonoma; macOS on Intel: sonoma; Linux ARM64, x86_64".

## V11 Prerequisites

Homebrew: "Depends on when building from source: go 1.27.2"

## V12 Install and keep current

README: "### Package Manager" with "brew install glow", "sudo port install glow", "pacman -S glow", "xbps-install -S glow", "nix-shell -p glow --command glow", "pkg install glow", "eopkg install glow", "choco install glow", "scoop install glow", "winget install charmbracelet.glow", "sudo snap install glow", apt repo "https://repo.charm.sh/apt/", yum repo "https://repo.charm.sh/yum/", "go install charm.land/glow/v3@latest", build from clone. Updates: silent.

## V13 Markdown forms claimed

silent on flavours. README: "Markdown files can be read with Glow's high-performance pager." Styles via "Glamour".

## V14 Whether files stay local

silent

## V15 Network and data leaving

README: "glow github.com/charmbracelet/glow" ("Fetch README from GitHub / GitLab") ; "glow https://host.tld/file.md" ("Fetch markdown from HTTP"). Snap description: "stash markdown files to your own private collection so you can read them anywhere" (Snap text only).

## V16 Price and licence

Licence: "[MIT](https://github.com/charmbracelet/glow/raw/master/LICENSE)" (README); Homebrew "License: MIT"; Snap "License MIT"; AlternativeTo "Cost / License Free Open Source (MIT)". Price text on README, Snap, Homebrew, apt: silent.

## V17 Cost beyond the price

silent

## V18 Use at work

silent

## V19 The unit a buyer takes

Homebrew: package/formula. apt: package. Snap: snap.

## V20 The surface the product sells on

AlternativeTo list pages; package registry pages (Homebrew formula page, Snap Store page); code repository page; apt archive index.

## V21 Distribution channels named

README: "Homebrew" (`brew install glow`), "MacPorts", "Arch Linux", "Void Linux", "Nix", "FreeBSD", "Chocolatey" (`choco`), "Scoop", "WinGet", "snap", "apt" (repo.charm.sh), "yum", "go install", "Releases" ([releases]: https://github.com/charmbracelet/glow/releases)

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

Homebrew: "Current versions: stable 3.0.0". Snap: "latest/stable 2.1.1"; "Last updated 30 May 2025 - latest/stable". apt: "Version: 2.0.0-1". API: latest release v3.0.0 published 2026-08-11T18:09:45Z; pushed_at 2026-10-05T11:11:20Z (commit); archived false.

## V28 Finding the way around a long document

silent

## V29 Finding a word

silent

## V30 Links, images and references to other files

README: "Glow will find local markdown files in subdirectories or a local Git repository." ; "glow https://host.tld/file.md"

## V31 Keeping up with a file edited elsewhere

silent

## V32 Appearance

README: "You can choose a style with the `-s` flag. When no flag is provided `glow` tries to detect your terminal's current background color and automatically picks either the `dark` or the `light` style for you." ; "Alternatively you can also supply a custom JSON stylesheet: glow -s mystyle.json" ; config example "# style name or JSON path (default "auto")  style: "light""

## V33 Print, export, send on

README: "CLI output can be displayed in your preferred pager with the `-p` flag." ; "`-w` flag lets you set a maximum width at which the output will be wrapped"

## V34 Help and what happens when it breaks

README: "## Feedback  We'd love to hear your thoughts on this project. Feel free to drop us a note!  - Twitter - The Fediverse - Discord" ; "## Contributing  See contributing" ; apt: "Bugs: https://bugs.launchpad.net/ubuntu/+filebug"

## V35 Who else uses it

AlternativeTo: "3 likes". Homebrew analytics (as published): "Installs 4,142 | 19,244 | 59,535" for "30 days | 90 days | 365 days"; "Installs on Request 4,112 | 19,056 | 58,565". API: stargazers_count 27635.

## V36 AI-related claims

silent

## V37 Why the product exists

silent
