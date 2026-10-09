# sbarex-qlmarkdown: verbatim profile

Cells: github-topics:markdown-viewer; homebrew:cask (weight 1). Conditions obeyed: GitHub: rates only for repos with >=200 stars; Homebrew: description-word census, installs as published (opt-out analytics), not users.

## Names as published
- Repository "sbarex/QLMarkdown"; README heading "QLMarkdown"; Homebrew cask page: token "qlmarkdown", "Name: sbarex QLMarkdown"

## Pages read (all captured 2026-10-09)
- https://github.com/sbarex/QLMarkdown : HTTP 200
- https://api.github.com/repos/sbarex/QLMarkdown and .../releases (via gh) : success
- https://raw.githubusercontent.com/sbarex/QLMarkdown/main/README.md : HTTP 200
- https://formulae.brew.sh/cask/qlmarkdown : HTTP 200
- https://formulae.brew.sh/api/cask/qlmarkdown.json : HTTP 200
- No separate site: the repository homepage field is empty.

## V01 Eligibility
README: "QLMarkdown is a Mac OS application that provides: a Quick Look extension for viewing Markdown files; an experimental Shortcut extension for converting Markdown files to HTML; a command-line executable for converting Markdown files to HTML; a graphical interface for configuring Quick Look preview display settings." Cask: "Quick Look generator for Markdown files". Repository description: "macOS Quick Look extension for Markdown files."

## V02 Name as published
See "Names as published".

## V03 Name form
Silent

## V04 One thing or several
README (the list under V01): Quick Look extension, Shortcut extension, command-line executable, settings interface.

## V05 Whom the product sells to
Silent

## V06 Audience text outside the classes
Silent

## V07 What the page asks the buyer to do to get it
README: "You can download the last compiled release from [this link](https://github.com/sbarex/QLMarkdown/releases) or you can install with Homebrew: brew install --cask qlmarkdown"; "**You must launch the application at least once**."; "If you like this application and find it useful, buy me a coffee!" Cask: "brew install --cask qlmarkdown".

## V08 Product kind
README: "QLMarkdown is a Mac OS application"; "**This application is not intended to be used as a standalone markdown file editor or viewer.**"; "A `qlmarkdown_cli` command line interface (CLI) is available to perform batch conversion of markdown files."

## V09 Reader only, or also editor
README: "this application is not intended to be used as a standalone markdown file editor or viewer but only to set Quick Look preview formatting preferences."; "The window interface has an inline editor to test the settings with a markdown file. You can open a custom markdown file and export the edited source code."

## V10 Platforms
README: "QLMarkdown is a Mac OS application". Cask: "Requirements: macOS >= 12". README: "System Settings > General > Login Items & Extensions > Quick Look".

## V11 Prerequisites
Cask: "Requirements: macOS >= 12". README: "**You must launch the application at least once**. In this way the Quick Look extension will be discovered by the system". README on Math/Mermaid: "The Math and Diagram extensions requires some external javascript libraries."

## V12 Install and keep current
(a) README: "download the last compiled release"; "brew install --cask qlmarkdown"; "To uninstall the application, simply drag it to the trash."; build from source section. (b) Cask page: "Current version: 1.5.7 (auto-updates)".

## V13 Markdown forms claimed
README: "For maximum compatibility with the Markdown format, the `cmark-gfm` library is used."; extensions: "Definition list", "GitHub alert", "Emoji", "Hashtags", "Heads anchors", "Highlight", "Inline local images", "Subscript", "Superscript", "Math" (MathJax), "Mermaid", "MKDocs Admonition", "Syntax highlighting", "Wikilinks", "YAML header"; options "Footnotes", "Smart quotes". README: "The Quick Look extension can also preview rmarkdown files (`.rmd`, without evaluating `r` code), MDX files (`.mdx`, without JSX rendering), Cursor Rulers (`.mdc`), Quarto files (`.qmd`), Api Blueprint files (`.apib`) and textbundle packages. Also `.mermaid` files are rendered".

## V14 Whether files stay local
README: "**This application does not collect any information about your system or the files it processes.**"

## V15 Network and data leaving
README: "If enabled, the Math and Mermaid extensions can link the JS library source files via CDN, if you want you can embed the bundled code."; "You can choose to link the corresponding library from the web (internet connection required) via `cdn.jsdelivr.net`, or to embed the source code directly into the HTML output"; "The generated HTML code has a Content Security Policy (CSP) that prevent to execute any untrusted javascript code."; "the application and extension have a permission exception that only allows read access to the entire system."

## V16 Price and licence
README: price silent (donation button "buy me a coffee"). Repository licence field: "GNU General Public License v3.0". Cask page: no licence or price field.

## V17 Cost beyond the price
Silent

## V18 Use at work
Silent

## V19 The unit a buyer takes
Cask artifact: "QLMarkdown.app -> /Applications/QLMarkdown.app". README: "the last compiled release".

## V20 The surface the product sells on
Captured pages: code repository page; package registry page (Homebrew cask).

## V21 Distribution channels named
README: "this link (releases)"; "Homebrew". Cask: "Homebrew Cask".

## V22 to V25 (shape dimensions)
Silent beyond the quotes under V07, V12, V16, V21. README: "buy me a coffee" (donation link, https://www.buymeacoffee.com/sbarex).

## V26 Release cadence and timing
Silent

## V27 Last release and archived status
Releases (API): "1.5.7 2026-10-02T10:18:37Z"; "1.5.6 2026-09-30T14:34:05Z"; "1.5.5 2026-09-23T11:06:07Z". Cask: "Current version: 1.5.7". README: "Developed by SBAREX 2020 - 2026." Repository: pushed_at "2026-10-04T06:21:53Z" (commit); archived: false.

## V28 Finding the way around a long document
Silent

## V29 Finding a word
Silent

## V30 Links, images and references to other files
README: "Inline local images: embed the image files inside the formatted output (required for the Quick Look preview)"; "Wikilinks"; "Heads anchors: create anchors for the heads."

## V31 Keeping up with a file edited elsewhere
Silent

## V32 Appearance
README: "You can choose a CSS theme to render the Markdown file. The application is provided with a predefined theme derived from the GitHub style valid both for light and dark appearance."; "You can also use a style to extend the standard theme or to override it."; "`@media (prefers-color-scheme: dark)`"; "Render as source code".

## V33 Print, export, send on
README: "an experimental Shortcut extension for converting Markdown files to HTML"; "a command-line executable for converting Markdown files to HTML"; "You can open a custom markdown file and export the edited source code."

## V34 Help and what happens when it breaks
README: "## FAQ ... Q: The Quick Look preview do not works"; "**Please inform me of any other UTI associated to `.md` files.**"; "I am not primarily an application developer. There may be possible bugs in the code, be patient."; "Please note that this software is provided "as is", without any warranty of any kind."

## V35 Who else uses it
Cask page analytics (Homebrew opt-out, as published): "30 days 2,087; 90 days 8,552; 365 days 32,911" (API values 2087, 8552, 32911). Repository page (API): stargazers_count 3632, forks_count 110. README: "The precompiled app is notarized and signed" (provenance).

## V36 AI-related claims
README: "Cursor Rulers (`.mdc`)" is the only AI-adjacent text; no AI claim made.

## V37 Why the product exists
Silent
