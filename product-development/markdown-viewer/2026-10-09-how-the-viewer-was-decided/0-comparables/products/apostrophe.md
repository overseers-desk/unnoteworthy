# Profile: apostrophe

Captured 2026-10-09. Cells: alternativeto:Typora; debian:apt-cache search markdown (Ubuntu 25.04 "plucky" archive); Flathub.

## Names as published
- "Apostrophe" (Flathub page heading; GitHub README heading; AlternativeTo)
- "Install Apostrophe on Linux | Flathub" (Flathub page title)
- apt: "Package: apostrophe" / "Description: Distraction free Markdown editor"

## URLs read
- https://alternativeto.net/software/typora/?p=3 (start URL, list page): direct fetch HTTP 403 (Cloudflare "Just a moment... Enable JavaScript and cookies to continue"); not read.
- Own AlternativeTo page, found by web search. Query: "Apostrophe alternativeto.net markdown editor"; result URL: https://alternativeto.net/software/apostrophe-1 . Read https://alternativeto.net/software/apostrophe-1/about/ through WebFetch (page text returned as an extract, HTTP status not reported; direct curl 403). AlternativeTo quotes below are the extract's quoted strings.
- http://archive.ubuntu.com/ubuntu/dists/plucky/universe/binary-amd64/Packages.xz : 200 (record "Package: apostrophe")
- http://archive.ubuntu.com/ubuntu/dists/plucky/universe/i18n/Translation-en.xz : 200 (long description)
- https://packages.ubuntu.com/plucky/apostrophe : 200, page body is an error: "two or more packages specified (apostrophe plucky)"; no product text.
- https://launchpad.net/ubuntu/plucky/+source/apostrophe : 200
- https://flathub.org/apps/org.gnome.gitlab.somas.Apostrophe : 200
- https://flathub.org/api/v2/appstream/org.gnome.gitlab.somas.Apostrophe : 200 (the listing's AppStream data)
- https://github.com/ApostropheEditor/Apostrophe : 200
- https://raw.githubusercontent.com/ApostropheEditor/Apostrophe/main/README.md : 200
- https://apps.gnome.org/Apostrophe/ : 200 (linked from Flathub as Project Website)

## Status marks (provenance only)
- apt long description: "Apostrophe is a GNOME Circle app." (Translation-en, plucky)
- Flathub page text beside the app name: "Free", "Medium Risk", "Desktop & Mobile", "3+ Age Rating". No verification badge text found beside the app.
- AlternativeTo extract: "Official Partner" appears only next to a different product's advertisement, not on Apostrophe's listing.

## V02 Name as published
"Apostrophe" (https://flathub.org/apps/org.gnome.gitlab.somas.Apostrophe); "Install Apostrophe on Linux | Flathub" (page title).

## V03 Name form
silent

## V04 One thing or several
silent

## V05 Whom the product sells to
silent

## V06 Audience text outside the classes
silent

## V07 What the page asks the buyer to do to get it
- Flathub buttons: "Install", "Donate", "Download" (https://flathub.org/apps/org.gnome.gitlab.somas.Apostrophe)
- "Fedora: `sudo dnf install apostrophe`" (README)
- "$ git clone https://gitlab.gnome.org/World/apostrophe/" ... "$ sudo ninja -C builddir install" (README)
- "If you want to help translating the project, please join us at Damned Lies" (README, https://raw.githubusercontent.com/ApostropheEditor/Apostrophe/main/README.md)

## V08 Product kind
- "Apostrophe is a [GTK+](https://www.gtk.org) based distraction free Markdown editor" (README)
- "Apostrophe is a GTK based distraction free Markdown editor." (apt long description)
- "Apostrophe is a simple GNU/Linux Markdown editor built with the GTK+ framework." (AlternativeTo extract)

## V09 Reader only, or also editor
- "Edit Markdown in style"; "Focus on your writing with a clean, distraction-free markdown editor."; "Live preview of what you write" (Flathub)
- "The preview lets you see a live rendered version of your document" (apps.gnome.org caption)

## V10 Platforms
- AlternativeTo extract: "Linux", "Flathub", "GNOME", "Linux Mobile"
- Flathub: "Desktop & Mobile"; "Available Architectures : x86_64 aarch64"
- apps.gnome.org keywords: "Linux"; AlternativeTo: "GNU/Linux"

## V11 Prerequisites
- README: "To build Apostrophe from source you need to have the following dependencies installed:" followed by "Build system: `meson ninja-build`", "Pandoc, the program used to convert Markdown to basically anything else: `pandoc`", "GTK3 and GLib development packages: `libgtk-3-dev libglib2.0-dev`", "Rendering the preview panel: `libwebkit2gtk`", "*optional:* pdftex module: `texlive texlive-latex-extra`", "*optional:* formula preview: `libjs-mathjax`"
- apt record: "Depends: dconf-gsettings-backend | gsettings-backend, python3:any, python3-pypandoc, python3-zombie-telnetlib, gir1.2-adw-1, gir1.2-glib-2.0, gir1.2-gtk-4.0, gir1.2-spelling-1, gir1.2-webkit-6.0"
- Flathub add-on: "TexLive Plugin  Allows to export to pdf and to show formulas in the inline preview"

## V12 Install and keep current
- "Install" ... "Also several unofficial builds are available: Nix(OS): `pkgs.apostrophe` ... Arch Linux (AUR) ... Fedora: `sudo dnf install apostrophe`" (README)
- "Building from Git" and "Building a flatpak package" sections (README)
- "Install the latest version from Flathub." (apps.gnome.org)
- Update method: silent

## V13 Markdown forms claimed
- "It uses pandoc as back-end for parsing Markdown" (README)
- "Inserting a table with the help of the toolbar" (apps.gnome.org screenshot caption)
- "Allows to export to pdf and to show formulas in the inline preview" (Flathub add-on)
- Unrecognised content: silent

## V14 Whether files stay local
silent

## V15 Network and data leaving
AppStream data, https://flathub.org/api/v2/appstream/org.gnome.gitlab.somas.Apostrophe: `"supports":[... {"type":"internet","value":"offline-only"}]` and `"recommends":[{"type":"internet","value":"always"}]`

## V16 Price and licence
- "Free" (Flathub); "Open Source ([GPL-3.0](https://choosealicense.com/licenses/gpl-3.0/)) and Free product." (AlternativeTo extract)
- "GPL-3.0 license" (GitHub licence field); `"project_license":"GPL-3.0+"` (AppStream)
- Flathub: "Donate"; AppStream `"donation":"https://www.paypal.me/manuelgenoves"`

## V17 Cost beyond the price
silent

## V18 Use at work
silent

## V19 The unit a buyer takes
silent

## V20 The surface the product sells on
silent

## V21 Distribution channels named
"Flathub"; "Nix(OS): `pkgs.apostrophe`"; "Arch Linux (AUR)"; "Fedora" (README); "Flathub" (apps.gnome.org)

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
- Flathub: "Changes in version 3.5  1 day ago" (read 2026-10-09)
- apps.gnome.org: "Latest version 3.4 released on 2025-09-30 00:00:00 UTC."
- Launchpad (plucky): "Current version: 3.2-2  Uploaded: 2025-01-13"
- AlternativeTo extract: "this page was last updated May 4, 2026."
- README: "currently developed and maintained by Manuel Genovés"

## V28 Finding the way around a long document
silent

## V29 Finding a word
silent

## V30 Links, images and references to other files
silent

## V31 Keeping up with a file edited elsewhere
"Live preview of what you write" (Flathub)

## V32 Appearance
"Dark, light and sepia themes" (Flathub, apps.gnome.org)

## V33 Print, export, send on
"Export to all kind of formats: PDF, Word/Libreoffice, LaTeX, or even HTML slideshows" (Flathub, apps.gnome.org)

## V34 Help and what happens when it breaks
- Flathub Links: "Report an Issue https://gitlab.gnome.org/World/apostrophe/-/issues"; "Help https://gitlab.gnome.org/World/apostrophe/"
- apps.gnome.org: "Contribute your ideas or report issues on the app's issue tracker."; "Visit the online help page for this app."

## V35 Who else uses it
- "5,273 Downloads/Month" (Flathub)
- AlternativeTo extract: "18 likes"; "4.7Excellent" from "3 ratings"
- GitHub repository page fields: "Stars 519", "Forks 46"

## V36 AI-related claims
silent

## V37 Why the product exists
silent
