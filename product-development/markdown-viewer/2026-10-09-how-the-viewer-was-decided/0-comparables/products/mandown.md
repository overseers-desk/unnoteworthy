# Profile: mandown

Slug: mandown. Cell: homebrew:formula. Weight 1. Cell condition obeyed: description-word census; installs as published, not users.

## Names as published

- Homebrew formula name "mandown"; description "Man-page inspired Markdown viewer"; README title "mandown - mdn"; repository "Titor8115/mandown"; the README says "executable's name changed to `mdn`"

## Pages read (all 2026-10-09)

- A https://formulae.brew.sh/formula/mandown : HTTP 200; also the API form https://formulae.brew.sh/api/formula/mandown.json : HTTP 200
- B https://github.com/Titor8115/mandown (the formula's homepage) : HTTP 200
- C https://raw.githubusercontent.com/Titor8115/mandown/master/README.md : HTTP 200
- D https://github.com/Titor8115/mandown/releases/latest (redirected to the tag page v1.0.5.2) : HTTP 200
- Unreachable: none.

Homebrew fields on A: "Install command: brew install mandown"; "Man-page inspired Markdown viewer"; "https://github.com/Titor8115/mandown"; "License: GPL-3.0-or-later"; "Current versions: stable 1.0.5.2"; "Revision: 2"; "Depends on: libconfig 1.8.2 Configuration file processing library; ncurses 6.6 Text-based UI library"; "Depends on when building from source: pkgconf"; bottle support listed for "macOS on Apple Silicon" (golden gate, tahoe, sequoia, sonoma), "macOS on Intel sonoma", "Linux ARM64", "Linux x86_64"; API analytics: install 30d 4, 90d 18, 365d 202; install_on_request 30d 4, 90d 18, 365d 202.
Fields on B: "man-page inspired Markdown viewer"; topics "c cli command-line console linux man man-page markdown ncurses ncurses-ui terminal tui"; "GPL-3.0 license"; "307 stars"; "5 watching"; "16 forks".

## V01 Eligibility

- A: "Man-page inspired Markdown viewer"
- C: "A man-page inspired Markdown pager written in C."

## V02 Name as published

- A: "mandown"; C: "mandown - mdn"

## V03 Name form

- A: "mandown"; C: "mandown - mdn"

## V04 One thing or several

- C: "Mandown can also be embedded in your own applications. To render a Markdown document in a C string: ... render_str(str, "md", "Test Title", NULL);"; "Static and shared libraries are available."

## V05 Whom the product sells to

- C: "Need to lookup things from README? Or from manual page? Or perhaps just want to install something cool..."

## V06 Audience text outside the classes

- C: "What is it: Need to lookup things from README? Or from manual page?"

## V07 What the page asks the buyer to do to get it

- A: "brew install mandown"
- C: "$ brew install mandown"; "$ git clone https://github.com/Titor8115/mandown.git $ cd mandown $ make install"; "Feel free to create an issue."

## V08 Product kind

- A: formula (package manager); C: "A man-page inspired Markdown pager written in C."; "$ mdn sample.md"; "Mandown can also be embedded in your own applications."

## V09 Reader only, or also editor

- C: "A man-page inspired Markdown pager"; "Move Up: Up, k ... Exit: q" (paging keys); editing: silent

## V10 Platforms

- A: bottle support for "macOS on Apple Silicon", "macOS on Intel", "Linux ARM64", "Linux x86_64" (Homebrew's list, with macOS release names)
- C: "Debian" install commands for dependencies

## V11 Prerequisites

- C: "Mandown requires libncurses(w), libxml2 and libconfig as compile-time dependencies. Make sure you have them installed before compiling."; "### Debian $ apt-get install libncursesw5-dev $ apt-get install libxml2-dev $ apt-get install libconfig-dev"
- A: "Depends on: libconfig ... ncurses"; "Depends on when building from source: pkgconf"

## V12 Install and keep current

- C: "### Homebrew $ brew install mandown The installed binary mdn would be at /usr/local/bin/"; "### Local $ git clone ... $ make install"; "To remove the binary ... make uninstall"
- Update method: silent

## V13 Markdown forms claimed

- C: "Current version is still being developed for some HTML tags. However, it should work on most Markdown documents."

## V14 Whether files stay local

- silent

## V15 Network and data leaving

- silent

## V16 Price and licence

- Price: silent
- Licence: A: "License: GPL-3.0-or-later"; B: "GPL-3.0 license"

## V17 Cost beyond the price

- silent

## V18 Use at work

- silent

## V19 The unit a buyer takes

- A: "a package the system's package manager maintains" is not worded; A: "Install command: brew install mandown" with bottles

## V20 The surface the product sells on

- A package registry page (Homebrew formula); B code repository page; D release page

## V21 Distribution channels named

- A, C: "Homebrew"; C: "git clone https://github.com/Titor8115/mandown.git"

## V22 Shape dimension 1: how the buyer reaches the offering

- C: "### Homebrew"; "### Local"

## V23 Shape dimension 2: whether anything is paid before it is reached

- silent

## V24 Shape dimension 3: how the sale is taken

- silent

## V25 Shape dimension 4: whether and how a place is held

- silent

## V26 Release cadence and timing

- silent

## V27 Last release and archived status

- D: "released this 01 Apr 18:37" (page datetime 2025-04-01) v1.0.5.2; A: "stable 1.0.5.2 Revision: 2"; archived status: silent

## V28 Finding the way around a long document

- C: "Page Up: Space, PgUp, b"; "Page Down: Bksp, PgDn, f"

## V29 Finding a word

- silent

## V30 Links, images and references to other files

- C: "Show href in hyperlink: Tab + Enter, or double click mouse 1"

## V31 Keeping up with a file edited elsewhere

- silent

## V32 Appearance

- C: "Added control schemes: mdn, vim, less (default since mdn isn't complete)"; "Config file location: ~/.config/mdn/mdnrc" (User Customization)

## V33 Print, export, send on

- silent

## V34 Help and what happens when it breaks

- C: "Feel free to create an issue."; "To read detailed usage, run `mdn -h`"

## V35 Who else uses it

- A: API install events 30d 4, 90d 18, 365d 202; install_on_request 30d 4, 90d 18, 365d 202 (Homebrew install analytics)
- B: "307 stars", "5 watching", "16 forks"

## V36 AI-related claims

- silent

## V37 Why the product exists

- C: "Need to lookup things from README? Or from manual page? Or perhaps just want to install something cool..."

## Disagreements between pages

- Dependencies: C "Mandown requires libncurses(w), libxml2 and libconfig as compile-time dependencies"; A lists "libconfig" and "ncurses" (and, for source builds, "pkgconf"), not libxml2.
- Name: A "mandown"; C "executable's name changed to `mdn`".

## Provenance (status marks)

- silent
