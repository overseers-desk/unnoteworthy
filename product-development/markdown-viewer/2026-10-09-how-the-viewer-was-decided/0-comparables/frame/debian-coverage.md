# Coverage note: Debian-family package archive (`apt-cache search markdown`)

Frame file: `debian.tsv`. Strike-list rows admitting its buyers: developers and coders (RULED strike-list:developers-and-coders); terminal readers (RULED strike-list:terminal-readers).

## Provenance, which is not what the brief expected

- The brief asks for the distribution release from `/etc/os-release`. The search host (hostname `GPU-Workstation`, search run 2026-10-09 07:2x UTC) reports `PRETTY_NAME="Ubuntu 25.04"`, `VERSION_ID="25.04"`, codename plucky. The list is therefore **Ubuntu 25.04 (plucky) archive**, not Debian. Debian and Ubuntu share most source packages, but the Debian archive was not searched and its package set differs (Ubuntu's universe is a rebuild of Debian unstable at the time of the release, with its own changes).
- The package index was last refreshed on the search host on 2026-09-23 (modification time of `/var/lib/apt/lists`), not on 2026-10-09. Ubuntu 25.04 reached end of life in January 2026, so the index is of a release that no longer receives updates.
- Sources configured on the host: Ubuntu archive and security (main, universe, multiverse; amd64 and i386), plus third-party repositories (Dropbox, Google, NVIDIA container toolkit, Mozilla, git-core PPA, graphics-drivers PPA, an unnamed "Stable" and "nodistro" origin). Every package returned came from the Ubuntu archive except two (below).
- Two results are not archive packages: `typora` and `marktext` appear only because they are installed on the search host from locally installed `.deb` files (their only source in `apt-cache policy` is `/var/lib/dpkg/status`). They are recorded and marked out, as the list's membership depends on the host that ran it.

## The list

- **Who runs it.** Canonical and the Ubuntu community maintain the archive; `apt-cache search` is a substring/regex match of the term against package names and long descriptions, in the index on the searching machine. It has no ranking, no install count and no popularity figure; the TSV count column says so.
- **Entries held when opened.** 344 packages matched `markdown`. The archive index held more than that in total; its total was not counted.

## Who is structurally shut out

- Anyone who does not use an apt-based Linux distribution: Mac and Windows users, and Linux users on Fedora, Arch, Nix, Flatpak or Snap (a Flatpak-only editor is absent).
- Applications distributed by their own site or a third-party repository (the search returned nothing from the third-party repositories on the host).
- Packages absent from the Ubuntu 25.04 archive because they were never packaged, were removed, or arrived after the plucky freeze.
- Debian-only packages not in Ubuntu.
- Applications whose package description does not contain the word "markdown" (a note application described as "note taking" is found only if its long description says markdown).
- No install counts: popularity-contest and Ubuntu's installation figures were not consulted, so the list cannot weight a package by use.

## Steps from list size to frame size

1. `apt-cache search markdown`: 344 packages (name, description). All 344 are rows in `debian.tsv`; none dropped.
2. Eligibility (hand-applied from the package name and description, reason in the TSV): 10 in, 13 undecidable, 321 out.
   - out: 214 libraries, modules and language bindings (Perl, Python, Ruby, Go, Rust, Node, PHP, R, Haskell, Lua, OCaml and others, development and runtime library packages); 43 static-site or documentation generators, plugins and themes (including all `mkdocs-*` packages); 28 converters, parsers and processors (including `pandoc`, `cmark`, `discount`, `kramdown`, `lowdown`); 16 documentation packages; 5 linters and formatters; 5 services or applications whose description concerns no markdown file; 7 search hits whose description names no markdown reading or writing function (for instance `hyperfine`, `texlive-latex-extra`); 1 font; 2 locally installed packages (above).
   - in: `apostrophe`, `elpa-markdown-mode`, `formiko`, `geany-plugin-markdown`, `ghostwriter`, `glow`, `grip`, `markdownpart`, `marknote`, `retext`.
   - undecidable: `iotas`, `klevernotes`, `kookbook`, `md2term`, `lookatme`, `mdp`, `pampi`, `vim-vimwiki`, `vim-voom`, `elpa-olivetti`, `okular-extra-backends`, `vim-link-vim`, `minder`.
3. Package-class counting caution: the library and plugin ecosystem inflates the matched list, so 344 is a count of packages, not of applications. The out rows for `lib*`, `python3-*`, `ruby-*`, `golang-*`, `node-*`, `php-*`, `librust-*` and `r-cran-*` were assigned by package-name prefix and a reading of the description, not each individually opened.

## Census or sample

Census of the cell "packages in the Ubuntu 25.04 archive index of 2026-09-23 whose name or description matches 'markdown'". Nothing sampled. It is a census of one distribution's search, on one machine, and cannot stand for Debian.

## Not reached

The Debian archive itself (packages.debian.org, `apt-cache` against a Debian sources list) was not searched. No popularity data was fetched.
