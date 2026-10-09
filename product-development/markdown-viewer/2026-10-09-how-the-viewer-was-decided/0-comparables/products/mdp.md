# mdp

Names as published: "mdp" (Homebrew formula; apt package; README heading "mdp - A command-line based markdown presentation tool.").
Cells obeyed: debian:apt-cache search markdown (Ubuntu 25.04 archive; no installs or recency) and homebrew:formula (description-word census; installs as published, not users). Weight 1.

Pages read (all 2026-10-09):
- `apt-cache show mdp` run on the Ubuntu 25.04 (plucky) host | exit success; output quoted below (not an HTTP page)
- https://packages.ubuntu.com/plucky/mdp | HTTP 200 but an error page: "two or more packages specified (mdp plucky)"; no package content
- https://formulae.brew.sh/formula/mdp | HTTP 200
- https://github.com/visit1985/mdp | HTTP 200 (homepage in both listings; releases list not in the captured page text)
- https://raw.githubusercontent.com/visit1985/mdp/HEAD/README.md | HTTP 200
The two listings differ in capitalisation only: apt "command-line based Markdown presentation tool"; Homebrew "Command-line based markdown presentation tool"; GitHub "A command-line based markdown presentation tool."

## V02 Name as published

"mdp" (both listings).

## V03 Name form

"Package: mdp" (apt-cache). README: "## mdp - A command-line based markdown presentation tool."

## V04 One thing or several

silent

## V05 Whom the product sells to

silent

## V06 Audience text outside the classes

silent

## V07 What the page asks the buyer to do to get it

Homebrew: "Install command: brew install mdp". README: "$ git clone https://github.com/visit1985/mdp.git / $ cd mdp / $ make / $ make install / $ mdp sample.md"; "On Debian, you can use the existing [DEB package](https://tracker.debian.org/pkg/mdp-src), or run `apt-get install mdp`."

## V08 Product kind

"mdp is a command-line program that allows you to make elegant presentations from Markdown formatted files." (apt-cache description)

## V09 Reader only, or also editor

"It is as easy as write your presentation content in the text editor of your preference and launch the presentation from the command-line." (apt-cache description). Reading/editing inside the program: silent.

## V10 Platforms

apt-cache: "Architecture: amd64". Homebrew: "macOS on Apple Silicon golden gate ✅ tahoe ✅ sequoia ✅ sonoma ✅ Linux ARM64 ✅ x86_64 ✅". README: "on Raspbian (Raspberry Pi)", "on Fedora", "On Arch Linux", "on Cygwin", "On Debian", "On FreeBSD", "On MacOS", "On Slackware", "On Ubuntu".

## V11 Prerequisites

README: "mdp needs the ncursesw headers to compile." "on Raspbian (Raspberry Pi) you need `libncurses5-dev` and `libncursesw5-dev`"; "on Fedora you need `ncurses-devel` and `ncurses-c++-libs`"; "Most terminals support 256 colors only if the TERM variable is set correctly. To enjoy mdp's color fading feature: export TERM=xterm-256color". apt-cache: "Depends: libc6 (>= 2.4), libncursesw6 (>= 6), libtinfo6 (>= 6)".

## V12 Install and keep current

README: git clone / make / make install; "On Arch Linux, you can use the existing [package]"; "on Cygwin you can use the existing [package]"; "On Debian ... `apt-get install mdp`"; "On FreeBSD, you can use the port [misc/mdp]"; "On MacOS, use either the [Homebrew Formula] by running `brew install mdp` or ... MacPorts ... `sudo port install mdp`"; "On Slackware ... `sbopkg -i mdp`"; "On Ubuntu ... `apt-get install mdp`". apt-cache: "Version: 1.0.15-1". Homebrew: "stable ✅ 1.0.19".

## V13 Markdown forms claimed

README: "Supports basic markdown formatting: - line wide markup - headlines - code - quotes - unordered list - in-line markup - bold text - underlined text - code"; "Horizontal rulers are used as slide separator."; "Supports headers prefixed by @ symbol."

## V14 Whether files stay local

silent

## V15 Network and data leaving

silent

## V16 Price and licence

Homebrew: "License: GPL-3.0-or-later". GitHub page: "GPL-3.0 license".

## V17 Cost beyond the price

silent

## V18 Use at work

silent

## V19 The unit a buyer takes

silent

## V20 The surface the product sells on

silent

## V21 Distribution channels named

apt-cache: "Section: universe/misc", "Source: mdp-src", "Homepage: https://github.com/visit1985/mdp", "Origin: Ubuntu". Homebrew https://formulae.brew.sh/formula/mdp. README: Arch Linux package, Cygwin package, tracker.debian.org/pkg/mdp-src, launchpad.net/ubuntu/+source/mdp-src, freshports misc/mdp, brewformulas.org/Mdp, ports.macports.org/port/mdp/, slackbuilds.org/apps/mdp/.

## V22 Shape dimension 1: how the buyer reaches the offering

README install list above.

## V23 Shape dimension 2: whether anything is paid before it is reached

silent

## V24 Shape dimension 3: how the sale is taken

silent

## V25 Shape dimension 4: whether and how a place is held

silent

## V26 Release cadence and timing

silent

## V27 Last release and archived status

apt-cache: "Version: 1.0.15-1". Homebrew: "Current versions: stable ✅ 1.0.19 head ⚡️ HEAD". GitHub page: "Star5.3k", "Fork264". Release dates and archived banner: not present in the captured text.

## V28 Finding the way around a long document

README controls: "h, j, k, l, Arrow keys, Space, Enter, Backspace, Page Up, Page Down - next/previous slide"; "Home, g - go to first slide"; "End, G - go to last slide"; "1-9 - go to slide n".

## V29 Finding a word

silent

## V30 Links, images and references to other files

silent

## V31 Keeping up with a file edited elsewhere

README: "r - reload input file".

## V32 Appearance

README: "Colors, keybindings and list types are configurable as of now. Note that configuring colors only works in 8 color mode."

## V33 Print, export, send on

silent

## V34 Help and what happens when it breaks

silent

## V35 Who else uses it

Homebrew analytics: "Installs 20 / 122 / 308" (30 days / 90 days / 365 days); "Installs on Request 20 / 122 / 308". GitHub page: "Star5.3k".

## V36 AI-related claims

silent

## V37 Why the product exists

silent
