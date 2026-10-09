# selimacerbas/mdkite.nvim (slug selimacerbas-mdkite-nvim)

Shard-13. Cell condition: rates only for repos with >=200 stars; counts only, no rates.
Name as published: "mdkite.nvim" (README heading); repository selimacerbas/mdkite.nvim. Former names: "markdown-preview.nvim", "mermaid-playground.nvim".

## Pages read (all 2026-10-09)

- https://api.github.com/repos/selimacerbas/mdkite.nvim : HTTP 200 (repository fields: description, topics, license, archived, pushed_at, stars)
- https://api.github.com/repos/selimacerbas/mdkite.nvim/readme : HTTP 200 (README text; the repository page https://github.com/selimacerbas/mdkite.nvim was read through the API, not as HTML)
- https://api.github.com/repos/selimacerbas/mdkite.nvim/releases?per_page=3 : HTTP 200 (release list)
- Not read: SECURITY.md, CONTRIBUTING.md, kitehost.nvim

## V01 Eligibility

README: "Live **Markdown preview** for Neovim with first-class **Mermaid diagram** support." ; "Renders your entire `.md` file in the browser: headings, tables, code blocks, everything"
Repository description: "Live Markdown preview for Neovim with Mermaid diagrams, LaTeX math (KaTeX), scroll sync, and syntax highlighting. Pure Lua, zero npm dependencies."

## V02 Name as published

"mdkite.nvim" (README). "> Note: Before 2.0.0 this plugin was `markdown-preview.nvim`... Before that it was `mermaid-playground.nvim`, renamed and rewritten to support full Markdown preview alongside first-class Mermaid diagram support."

## V03 Name form

"mdkite.nvim" ; topics: "markdown-preview", "neovim-plugin", "nvim"

## V04 One thing or several

README: "Powered by `kitehost.nvim` (pure Lua HTTP server)" ; "Server dependency: kitehost.nvim, v2.0.0 or newer"

## V05 Whom the product sells to

silent

## V06 Audience text outside the classes

silent

## V07 What the page asks the buyer to do to get it

"Install (lazy.nvim)" with spec `"selimacerbas/mdkite.nvim"` ; "No prereqs. No `npm install`. Just install and go."

## V08 Product kind

"Live Markdown preview for Neovim" ; repository topics "neovim-plugin" ; "Zero external dependencies: no npm, no Node.js, just Neovim + your browser"

## V09 Reader only, or also editor

"Start preview: `:MdKite`" ; "Edit freely: the browser updates instantly as you type" (the editing is in Neovim; the product shows the preview)

## V10 Platforms

README: "On macOS, string values are passed via `open -a <name>`." ; Troubleshooting heading "WSL: browser doesn't open, or preview unreachable from Windows". Otherwise silent.

## V11 Prerequisites

"Neovim 0.10+" ; "kitehost.nvim v2.0.0 or newer" ; "Tree-sitter with the Markdown parser (recommended for mermaid block extraction)" ; "mermaid-rs-renderer (optional)" ; "Rendering requires internet access" (Security section).

## V12 Install and keep current

"Install (lazy.nvim)" (README). Upgrade section: "Upgrading from markdown-preview.nvim ... Through 2.x the former spec still installs it, since GitHub redirects the repository's former name".

## V13 Markdown forms claimed

"GitHub-flavored styling" ; "LaTeX math: inline `$...$` and display `$$...$$` rendered via KaTeX" ; "Browser-side libraries ... markdown-it: Markdown parser" ; "Raw HTML is rendered by default (GitHub-like)." ; "`.mmd` / `.mermaid` files are fully supported"

## V14 Whether files stay local

"Local by default. The preview server binds to `127.0.0.1`." (Security)

## V15 Network and data leaving

"Zero external dependencies: no npm, no Node.js, just Neovim + your browser" (Features list) and, in Security: "Browser libraries load from CDNs (jsdelivr/unpkg, see Dependencies). Rendering requires internet access" (both quoted; they sit in the same README). "Traffic is plain, unencrypted HTTP." (network binding note)

## V16 Price and licence

Repository license field: "MIT" (GitHub API). Price: silent.

## V17 Cost beyond the price

silent

## V18 Use at work

silent

## V19 The unit a buyer takes

silent

## V20 The surface the product sells on

Code repository page (README); no store.

## V21 Distribution channels named

"lazy.nvim" (install spec) ; GitHub repository `selimacerbas/mdkite.nvim` ; `cargo install mermaid-rs-renderer` (optional dependency)

## V22 Shape dimension 1: how the buyer reaches the offering

"Install (lazy.nvim)": `"selimacerbas/mdkite.nvim"`

## V23 Shape dimension 2: paid before reached

silent

## V24 Shape dimension 3: how the sale is taken

silent

## V25 Shape dimension 4: place held

silent

## V26 Release cadence and timing

GitHub API releases: v2.1.0 2026-10-02, v2.0.0 2026-10-02, v1.10.0 2026-07-07. No schedule stated. README: "All three are removed in 3.0.0."

## V27 Last release and archived status

GitHub API: latest release "v2.1.0" 2026-10-02; pushed_at 2026-10-02; archived false.

## V28 Finding the way around a long document

"Scroll sync: browser follows your cursor position with line-level precision"

## V29 Finding a word

silent

## V30 Links, images and references

"Relative images work: `![](pic.png)` next to your `.md` file renders in the preview" ; "Relative images are served from the previewed file's directory."

## V31 Keeping up with a file edited elsewhere

"Instant updates via Server-Sent Events (no polling)" ; "auto_refresh = true, -- auto-update on buffer changes" with events "InsertLeave", "TextChanged", "TextChangedI", "BufWritePost" ; "Force refresh: `:MdKite refresh`"

## V32 Appearance

"Dark / Light theme toggle with colored heading accents" ; "custom_css = "", -- CSS file layered over bundled styles"

## V33 Print, export, send on

"Mermaid diagrams ... (click to expand, zoom, pan, export)" ; "SVG export" (diagram overlay). Page export: silent.

## V34 Help and what happens when it breaks

README: "Troubleshooting" section (WSL); "PRs and ideas welcome: CONTRIBUTING.md ... SECURITY.md says how to report a vulnerability privately."

## V35 Who else uses it

Repository stargazers_count 227 (API field).

## V36 AI-related claims

silent

## V37 Why the product exists

"Before that it was `mermaid-playground.nvim`, renamed and rewritten to support full Markdown preview alongside first-class Mermaid diagram support." (README note; a history, not a stated motive)
