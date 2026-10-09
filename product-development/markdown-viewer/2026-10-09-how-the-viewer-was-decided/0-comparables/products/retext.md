# retext: verbatim profile

Cells: alternativeto:Typora; alternativeto:Glow; debian:apt-cache search markdown (named "Ubuntu 25.04 archive"); Flathub; github-topics:markdown-editor (weight 1). Conditions obeyed: AlternativeTo: eligibility re-checked on own page, rates dated to the list; Ubuntu archive: no installs or recency drawn from it; Flathub: census of search hits, price not stated by the list; GitHub: rates only for repos with >=200 stars.

## Names as published
- "ReText" (README "Welcome to ReText!", Flathub, AlternativeTo page title "ReText: Simple text editor for Markdown and reStructuredText documents"); Ubuntu package "retext"; repository "retext-project/retext"

## How the AlternativeTo entry was found
Start URLs (.../typora/?p=4, .../glow/) are list pages (entry link not captured). I guessed the slug from the name and read https://alternativeto.net/software/retext/about/ through WebFetch (condensed rendering; curl gets 403); the page title names ReText.

## Pages read (all captured 2026-10-09)
- https://alternativeto.net/software/retext/about/ : read through WebFetch
- `apt-cache show retext` on the host (Ubuntu archive index; the identifier named in the collection list) : output read
- https://flathub.org/apps/me.mitya57.ReText : HTTP 200 (final URL https://flathub.org/en/apps/me.mitya57.ReText)
- https://flathub.org/api/v2/appstream/me.mitya57.ReText : HTTP 200
- https://github.com/retext-project/retext : HTTP 200
- https://api.github.com/repos/retext-project/retext and .../releases (via gh) : success
- https://raw.githubusercontent.com/retext-project/retext/master/README.md : HTTP 200
- Linked and not read: the wiki (https://github.com/retext-project/retext/wiki), PyPI, Transifex.

## V01 Eligibility
README: "ReText is a simple but powerful editor for markup languages. It is based on Markups module which supports Markdown, reStructuredText, Textile and AsciiDoc." Repository description: "ReText: Simple but powerful editor for Markdown and reStructuredText". Flathub: "Simple text editor for Markdown and reStructuredText". Ubuntu package: "Description-en: Simple text editor for Markdown and reStructuredText".

## V02 Name as published
See "Names as published".

## V03 Name form
Silent

## V04 One thing or several
Silent

## V05 Whom the product sells to
Silent

## V06 Audience text outside the classes
Silent

## V07 What the page asks the buyer to do to get it
README: "To install ReText, make sure that you have Python (3.9 or later) installed, and run `pip3 install ReText`." Flathub: "Install". 

## V08 Product kind
README: "ReText is a simple but powerful editor for markup languages." Ubuntu package: "It is written in Python using Qt libraries." Flathub: appstream type "desktop-application"; page "Desktop Only".

## V09 Reader only, or also editor
README: "a simple but powerful editor for markup languages". Flathub: "ReText is a text editor for plain text markup languages, such as Markdown and reStructuredText."

## V10 Platforms
Flathub: "Desktop Only". AlternativeTo (tool rendering): structured data lists "Mac, Windows, Linux, and BSD"; "Linux and BSD are officially supported". README: "ReText on Plasma 5 desktop" (image caption). Ubuntu: "Architecture: all".

## V11 Prerequisites
README: "Python (3.9 or later)"; "ReText requires PyQt6 and Markups (4.0 or later) to run."; "We also recommend having these packages installed: pyenchant — for spell checking support; chardet — for encoding detection support; PyQt6-WebEngine — a more powerful preview engine with JavaScript support". Ubuntu: "Depends: python3-docutils, python3-markdown, python3-markups (>= 4.0), python3-mdx-math, python3-pyqt6, python3-pygments, python3:any".

## V12 Install and keep current
(a) README: "run `pip3 install ReText`"; "create a virtual environment and install from there"; "manually download the tarball from PyPI or clone the repository, and then run `./retext.py`". Ubuntu archive package "retext_8.1.0-1_all.deb". Flathub package. (b) Silent.

## V13 Markdown forms claimed
README: "Markups module which supports Markdown, reStructuredText, Textile and AsciiDoc". Ubuntu: "Depends: ... python3-mdx-math". Release notes 8.1.0 (Flathub): "Added markdownHeaders setting for the highlighter."; "Pasted image URLs are now converted to image markup."

## V14 Whether files stay local
Silent

## V15 Network and data leaving
Silent

## V16 Price and licence
README: "licensed under GNU GPL (v2+) license". Flathub: "Free"; appstream project_license "GPL-2.0+". Repository licence field: "GNU General Public License v2.0". AlternativeTo: "Open Source and Free product." Ubuntu: price silent.

## V17 Cost beyond the price
Silent

## V18 Use at work
Silent

## V19 The unit a buyer takes
Flathub: "131 MiB Download". Ubuntu: "Size: 199884".

## V20 The surface the product sells on
Captured pages: AlternativeTo directory page; Flathub app page; Ubuntu archive index record; code repository page.

## V21 Distribution channels named
README: "PyPI"; "pip3 install ReText"; "clone the repository". Flathub: "Flathub". Ubuntu: "Origin: Ubuntu"; "Section: universe/editors".

## V22 to V25 (shape dimensions)
Silent beyond the quotes under V07, V12, V16, V21.

## V26 Release cadence and timing
Silent

## V27 Last release and archived status
Releases (API): "8.1.0 2025-01-09T18:55:56Z"; "8.0.2 2024-03-16T17:48:50Z"; "8.0.1 2023-05-28T18:24:37Z". Flathub: "Changes in version 8.1.0 almost 2 years ago". Repository: pushed_at "2026-09-24T11:18:47Z" (commit); archived: false. README: "ReText is Copyright 2011–2025". AlternativeTo: "this page was last updated Sep 9, 2022."

## V28 Finding the way around a long document
Flathub 8.1.0 notes: "Added F9 shortcut for showing/hiding directory tree dynamically."; "Flathub: synchronized scrolling". Outline: silent.

## V29 Finding a word
Silent

## V30 Links, images and references to other files
Flathub 8.1.0 notes: "WebEngine previewer now shows link on hover."; "Pasted image URLs are now converted to image markup."

## V31 Keeping up with a file edited elsewhere
Flathub: "It supports tabs, live text preview, synchronized scrolling and syntax highlighting." External changes: silent.

## V32 Appearance
Flathub 8.1.0 notes: "When the system theme is dark, Qt WebEngine now uses dark mode too."; "Preferences dialog now has links to open the selected stylesheet file".

## V33 Print, export, send on
Flathub: "ReText can export to HTML, ODT and PDF formats. It is also possible to write custom export extensions." Ubuntu: "Supported export formats: HTML, ODT, PDF."

## V34 Help and what happens when it breaks
README: "You can read more about ReText in the [wiki]."; "You can translate ReText into your language on [Transifex]." Flathub: "Report an Issue https://github.com/flathub/me.mitya57.ReText/issues". Ubuntu: "Bugs: https://bugs.launchpad.net/ubuntu/+filebug".

## V35 Who else uses it
Flathub: "427 Downloads/Month". Repository page (API): stargazers_count 2062, forks_count 212. AlternativeTo: "48 likes". Third-party mark (provenance): Flathub "Unverified"; "This community-provided package is not verified by, affiliated with, or supported by Dmitry Shachnev."

## V36 AI-related claims
Silent

## V37 Why the product exists
Silent
