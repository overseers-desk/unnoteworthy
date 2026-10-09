# rivolink-leaf: verbatim profile

Cells: github-topics:markdown-viewer; homebrew:formula; Snap Store (weight 1). Conditions obeyed: GitHub: rates only for repos with >=200 stars; Homebrew: description-word census, installs as published, not users; Snap: undisclosed top-100, no rate against Flathub, {} is not free (the Snap page states no price; none is recorded).

## Names as published
- Repository "RivoLink/leaf"; README/site: "leaf" (site title "leaf : Terminal Markdown previewer, GUI-like experience."); Homebrew formula "leaf-markdown-viewer" ("Formerly known as: leaf-md"); Snap Store: package name "leaf", title "Leaf Markdown Viewer"; npm "@rivolink/leaf"; crate "leaf-markdown-viewer"

## Pages read (all captured 2026-10-09)
- https://github.com/RivoLink/leaf : HTTP 200
- https://api.github.com/repos/RivoLink/leaf and .../releases (via gh) : success
- https://raw.githubusercontent.com/RivoLink/leaf/main/README.md : HTTP 200
- https://leaf.rivolink.mg : HTTP 200
- https://formulae.brew.sh/formula/leaf-markdown-viewer : HTTP 200
- https://formulae.brew.sh/api/formula/leaf-markdown-viewer.json : HTTP 200
- https://snapcraft.io/leaf : HTTP 200
- Linked and not read: npmjs.com, crates.io, scoop.sh, AUR pages, demo/README.md.

## V01 Eligibility
README: "Terminal Markdown previewer — GUI-like experience." Repository description: "Terminal Markdown previewer — GUI-like experience." Site: "leaf lets you read Markdown files directly in the terminal with a clean, focused interface." Homebrew: "Terminal Markdown previewer with a GUI-like experience".

## V02 Name as published
See "Names as published".

## V03 Name form
Silent

## V04 One thing or several
Silent

## V05 Whom the product sells to
Site: "Designed for developers, CLI users, and AI-assisted workflows."; "Built for developers" (Preview AI output; Read docs while coding; Explore Markdown projects).

## V06 Audience text outside the classes
Silent

## V07 What the page asks the buyer to do to get it
Site: "Get Started", "View Docs", "Install in seconds", "curl -fsSL https://leaf.rivolink.mg/install.sh | sh". README: "Install the latest published binary." Snap: "sudo snap install leaf --beta". Homebrew: "brew install leaf-markdown-viewer". README: "If you like leaf, consider giving the project a star ⭐".

## V08 Product kind
Site: "A terminal-based Markdown previewer with a GUI-like experience." README: "Inline Mode: Render Markdown directly to stdout without the interactive TUI". Repository topics: "terminal", "tui", "termux".

## V09 Reader only, or also editor
README: "Press Ctrl+E to open the current file in the configured editor." Site: "Editor integration: Press Ctrl+E to open in your editor." Editing in the product: silent.

## V10 Platforms
Site FAQ: "leaf runs on macOS (Intel & Apple Silicon), Linux (x64 & ARM), Windows, and Android via Termux." README: "macOS / Linux / Android / Termux"; "Windows". Homebrew: "Bottle (binary package) installation support provided for: macOS on Apple Silicon ... Linux".

## V11 Prerequisites
Silent (install commands only). README (shell completions): "Supports bash, zsh, fish, Nushell, and PowerShell."

## V12 Install and keep current
(a) README: install script (curl), PowerShell script (irm), "npm install -g @rivolink/leaf", "brew install leaf-markdown-viewer", "cargo install leaf-markdown-viewer", "scoop install leaf-markdown-viewer", "yay -S leaf-markdown-viewer"; Snap "sudo snap install leaf --beta". (b) README: "Update an existing installation to the latest published release."; "`leaf --update` downloads the matching published asset, verifies it against the published `checksums.txt` SHA256, and then installs it."; "npm update -g @rivolink/leaf"; "brew upgrade leaf-markdown-viewer"; "scoop update leaf-markdown-viewer". Site: "Secure Auto-update: One-command update with SHA256 verification."

## V13 Markdown forms claimed
Site: "Syntax highlighting: Beautiful code blocks with syntax coloring for 40+ languages."; "Table rendering: Markdown tables rendered with Unicode box-drawing borders"; "LaTeX math: Inline and block math formulas converted to Unicode symbols, no external renderer needed."; "Mermaid diagrams: Flowcharts, sequence diagrams, and pie charts rendered as ASCII art directly in the terminal."

## V14 Whether files stay local
Silent

## V15 Network and data leaving
README: "`leaf --update` downloads the matching published asset". Telemetry: silent.

## V16 Price and licence
README: "This project is licensed under the MIT License." Site FAQ: "Is open source? Yes, leaf is MIT licensed and hosted on GitHub." Homebrew: "License: MIT". Snap Store: "License MIT". Price: silent on all pages.

## V17 Cost beyond the price
Silent

## V18 Use at work
Silent

## V19 The unit a buyer takes
README: "Install the latest published binary."

## V20 The surface the product sells on
Captured pages: code repository page; maker's own website; package registry page (Homebrew); application store listing (Snap Store).

## V21 Distribution channels named
README/site: "curl install script", "npm", "Homebrew", "Cargo", "Scoop (Windows)", "ArchLinux (AUR)"; Snap Store "latest/beta" and "latest/edge" channels.

## V22 to V25 (shape dimensions)
Silent beyond the quotes under V07, V12, V16, V21.

## V26 Release cadence and timing
Silent

## V27 Last release and archived status
Releases (API): "1.28.3 2026-09-28T10:27:09Z"; "1.28.2 2026-09-14T04:39:32Z"; "1.28.1 2026-08-31T04:04:42Z". Homebrew: stable "1.28.3". Snap Store: "Last updated 29 September 2026 - latest/beta; 28 September 2026 - latest/edge"; "latest/beta 1.28.3". Repository: pushed_at "2026-09-28T10:22:52Z" (commit); archived: false. Site footer: "2026".

## V28 Finding the way around a long document
Site: "Table of contents: Sidebar TOC with heading hierarchy and active section tracking. Toggle with t, jump with 1-9."; "Watch mode: ... Scroll position is preserved."; "Keyboard navigation: Vim-like keybindings: j/k, d/u, g/G."

## V29 Finding a word
Site: "Full-text search: Press / to search. Matches are highlighted with a counter. Navigate with n/N."; "File picker: Fuzzy finder with Ctrl+P or directory browser with --picker."

## V30 Links, images and references to other files
README configuration: "hyper-link-prefix = "#"  # single character before link text". Images and other-file links: silent.

## V31 Keeping up with a file edited elsewhere
README: "# Watch mode: reloads automatically on save". Site: "Watch mode: Auto-reload when the file changes on disk. Scroll position is preserved. Toggle with -w flag or press w."

## V32 Appearance
Site: "Theme picker: 4 built-in themes: Arctic, Forest, Ocean, Solarized-Dark. Live preview with Shift+T."; README: "Custom Themes: Create a `.toml` file that inherits from a built-in theme and overrides specific colors"; "width = 80  # maximum content width".

## V33 Print, export, send on
README: "Render Markdown directly to stdout without the interactive TUI"; "leaf --inline plain README.md" (plain text), "leaf --inline ansi README.md"; "fzf --preview 'leaf --inline ansi {}'".

## V34 Help and what happens when it breaks
README: "Contributions are welcome. Feel free to open an issue or submit a pull request."; "See the CONTRIBUTING.md file for details." Site nav: "Documentation".

## V35 Who else uses it
Homebrew analytics (opt-out, as published): "leaf-markdown-viewer 30 days 430; 90 days 1243; 365 days 1243". Repository page (API): stargazers_count 2121, forks_count 109. Third-party mark (provenance): Snap Store "(Ownership verified) The publisher has verified that they own this domain."

## V36 AI-related claims
Site: "Designed for developers, CLI users, and AI-assisted workflows."; "Preview AI output: Pipe output from Claude, ChatGPT, or any AI tool directly into a beautiful preview. claude "explain Rust" | leaf"; "Stdin Support: Pipe output from any tool (claude, aichat, cat) directly into leaf." README: "claude "explain Rust lifetimes" | leaf".

## V37 Why the product exists
Site: "Previewing Markdown shouldn't mean switching to a browser or a heavy GUI app."; "Web viewers are overkill: For a quick preview, you don't need a full web application with login and setup."; "CLI tools lack interactivity: Existing terminal tools dump Markdown as plain text: no navigation, no search, no style."
