# Formiko (slug formiko)

Shard-03. Cell conditions: re-check eligibility on own page; rates dated to the list (AlternativeTo Typora list) | cell named Ubuntu 25.04 archive; no installs or recency (apt) | census of search hits; price not stated (Flathub).
Name as published: "Formiko" (all pages); site title "Formiko — RST & Markdown editor".

## Pages read (all 2026-10-09)

- https://alternativeto.net/software/typora/?p=13 : list page; plain curl returns HTTP 403; read by headless browser dump (exit 0). Page text: "Typora alternatives page was last updated Sep 18, 2026".
- apt-cache show formiko : run on the collection host (Ubuntu 25.04, plucky archive index), 2026-10-09.
- https://flathub.org/apps/cz.zeropage.Formiko : HTTP 200 (final https://flathub.org/en/apps/cz.zeropage.Formiko)
- https://github.com/ondratu/formiko : linked from apt Homepage; read through https://api.github.com/repos/ondratu/formiko (200), .../readme (200), .../releases?per_page=5 (200). The github.com HTML page was not fetched.
- https://formiko.zeropage.cz : HTTP 200 (Project Website link on Flathub)

AlternativeTo entry, https://alternativeto.net/software/typora/?p=13: "Formiko 1 like  Formiko is reStructuredText and MarkDown editor and live previewer. It is written in Python with Gtk3, GtkSourceView and Webkit2.  Cost / License: Free, Open Source  Origin: Czechia, EU  Alerts: Discontinued  Platforms: Linux"

Status marks (provenance only): Flathub text "Free", "Medium Risk", "Desktop Only", "3+ Age Rating".

Where the pages disagree: AlternativeTo "Alerts: Discontinued" and "written in Python with Gtk3 ... Webkit2" against README "It is written in Python with Gtk4, GtkSourceView and WebKit" and a 2.0.0 release dated 2026-08-11 (API). apt "Version: 1.4.3-2.1" and "Homepage: https://github.com/ondratu/formiko" against Flathub "Changes in version 2.0.0".

## V01 Eligibility

README: "Formiko is a reStructuredText and MarkDown editor and live previewer." Flathub: "Formiko is a reStructuredText and Markdown editor and live previewer." apt: "reStructuredText and MarkDown editor and live previewer". Repository description: "reStructuredText editor and live previewer".

## V02 Name as published

"Formiko"

## V03 Name form

"Formiko"; "reStructuredText and Markdown editor" (Flathub summary); "RST & Markdown editor" (site)

## V04 One thing or several

silent

## V05 Whom the product sells to

Site: "A reStructuredText & Markdown editor with live preview — for writers, developers and documentation authors."

## V06 Audience text outside the classes

Site: "Everything you need to write great documentation."

## V07 What the page asks the buyer to do to get it

Site: "Install via Flatpak" ; "View on GitHub" ; "Other platforms" (buttons). README: "flatpak install flathub cz.zeropage.Formiko". README: "If you want to **donate** to the development, you can do so via the paypal link."

## V08 Product kind

silent beyond "editor and live previewer"

## V09 Reader only, or also editor

"reStructuredText and MarkDown editor and live previewer" (README, apt, AlternativeTo)

## V10 Platforms

Flathub: "Desktop Only" ; "Available Architectures: x86_64 aarch64". AlternativeTo: "Platforms Linux". README: sections "Flatpak", "Debian based", "NetBSD", "FreeBSD" (installation headings) ; NetBSD: "**Broken at this moment - the WebKit with GTK4 and the libspelling packages are not available at this moment**"

## V11 Prerequisites

README "Requirements:" list: "GTK 4", "WebKitGTK 6.x", "GtkSourceView 5.x", "gir files for all Gtk libraries" ; "Uses Docutils and m2r2 Markdown parser." (Flathub)

## V12 Install and keep current

README: "flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo" ; "flatpak install flathub cz.zeropage.Formiko" ; "flatpak run cz.zeropage.Formiko" ; Debian-based: apt of dependencies then the Python package installer with "--break-system-packages" ; "pkgin install ..." ; "pkg install ..." (BSD). Updates: silent.

## V13 Markdown forms claimed

README: "It uses Docutils and a MarkDown-to-reStructuredText converter." ; "MarkDown to reStructuredText converter (M2R2) - https://github.com/crossnox/m2r2" ; "Formiko registers additional directives that are available in both reStructuredText and MarkDown (via M2R2) documents." ; site: "First-class support for reStructuredText (Docutils) and Markdown via the M2R2 converter."

## V14 Whether files stay local

silent

## V15 Network and data leaving

silent

## V16 Price and licence

Flathub: "Free" label ; AlternativeTo: "Cost / License Free Open Source" ; README: donation link ("If you want to **donate** to the development"). Repository licence field via API: NOASSERTION. Price in Flathub text: silent. apt: silent.

## V17 Cost beyond the price

silent

## V18 Use at work

silent

## V19 The unit a buyer takes

silent

## V20 The surface the product sells on

AlternativeTo list page; Flathub application page; code repository page; maker's site formiko.zeropage.cz; apt archive index.

## V21 Distribution channels named

README: "Flatpak", "Debian based", "NetBSD", "FreeBSD"; "flathub"; site: "Install via Flatpak", "View on GitHub", "Other platforms".

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

Flathub: "Changes in version 2.0.0  about 2 months ago". API: latest release 2.0.0 published 2026-08-11T08:26:36Z; pushed_at 2026-10-07T08:35:27Z (commit); archived false. apt: "Version: 1.4.3-2.1". AlternativeTo: "Alerts: Discontinued".

## V28 Finding the way around a long document

silent

## V29 Finding a word

silent

## V30 Links, images and references to other files

README: "linked file opening" ; Flathub: "Linked file opening"

## V31 Keeping up with a file edited elsewhere

README: "preview mode with auto scroll" ; site: "See your rendered HTML output instantly as you type — no manual refresh needed."

## V32 Appearance

Site: "GtkSourceView-powered editor with full RST and Markdown syntax highlighting and theme support."

## V33 Print, export, send on

README: "Docutils HTML4, HTML5, S5/HTML slide show and PEP HTML writer" ; "json and html preview"

## V34 Help and what happens when it breaks

Flathub: "Report an Issue https://github.com/ondratu/formiko/issues" ; apt: "Bugs: https://bugs.launchpad.net/ubuntu/+filebug"

## V35 Who else uses it

AlternativeTo: "1 like". Flathub: "194Downloads/Month" (as published). API: stargazers_count 133.

## V36 AI-related claims

silent

## V37 Why the product exists

silent
