# Coverage note: Homebrew (formulae and casks)

Frame file: `homebrew.tsv`. Strike-list rows admitting its buyers: developers and coders (RULED strike-list:developers-and-coders); through the casks, the writers and note-takers on a Mac.

## The list

- **Who runs it.** Homebrew, the macOS/Linux package manager, publishes the catalogue (`https://formulae.brew.sh/api/formula.json`, `https://formulae.brew.sh/api/cask.json`) and its opt-out install analytics (`/api/analytics/install/{30d,90d,365d}.json`, `/api/analytics/cask-install/{30d,90d,365d}.json`).
- **Opened.** 2026-10-09 (UTC), all eight files returned HTTP 200. Analytics windows as the files state them: 30d = 2026-09-09 to 2026-10-09; 90d = 2026-07-11 to 2026-10-09; 365d = 2025-10-09 to 2026-10-09.
- **Entries held when opened.** formula.json 8,647 entries; cask.json 7,788 entries.
- **Provenance of the count.** Counts are Homebrew's own analytics as published, strings with thousands separators, kept as published. They count installs reported by users who have not turned analytics off, not users and not use. The formula analytics files carry `total_items` of 20,970 (30d) but list 17,318 items, so the published file itself omits some; "not listed" in the TSV means absent from the published items, not zero.

## Who is structurally shut out

- Anyone who gets software by another route: Linux distribution packages, Windows and Linux installers, the Mac App Store, direct download, `git clone`. Homebrew is a Mac (and Linux) command-line route and so over-represents people comfortable with a terminal.
- Applications not packaged in Homebrew's default taps (third-party taps are not in these files).
- Installs by users who disabled analytics, and installs from CI (counted in the analytics: a build farm installing `glow` counts as many installs).
- Casks with no description. 2,649 of 7,788 casks (34%) have a null `desc`, so a description search cannot see them. A markdown application whose cask carries no description is not in this frame whatever it is. Formulae: no null descriptions.
- Entries whose description does not use the word "markdown" (for instance "Markdown" spelled in another language, or an app described as "notes" or "text editor").

## Steps from list size to frame size

1. formulae in the catalogue: 8,647. Casks in the catalogue: 7,788.
2. Mechanical rule: description contains "markdown", case-insensitive substring, no other filter. Formulae: 73. Casks: 48. Total 121 rows in `homebrew.tsv`.
3. Eligibility (hand-applied per entry from the description alone, reason recorded in the TSV):
   - formulae: 15 in, 4 undecidable (`backlog-md`, `mdp`, `deck`, `reveal-md`), 54 out (parsers, converters, linters, formatters, static-site and documentation generators, language servers, task runners, a web server, a feed reader).
   - casks: 43 in, 4 undecidable (`deckset`, `ia-presenter`, `markdown-service-tools`, `tableflip`), 1 out (`ia-markdown-dictionary`, dictionary data).
   - total: 58 in, 8 undecidable, 55 out.
4. Notes on the in rows: `typora` and `typora@dev` are two casks of one product; both are rows because the list counts them separately. Quick Look plugins (`qlmarkdown`, `qlcommonmark`, `ttscoff-mmd-quicklook`, `markdown-preview`) are admitted as extensions a person installs to read markdown files. Cask rows not named in the cask decision table were marked "in" on the description alone ("Markdown editor", "Markdown viewer", and similar); a reviewer can re-check these against the `description` column.

## Census or sample

Census of the cell "Homebrew formulae and casks whose description contains 'markdown'", under the rule in step 2. Nothing was sampled or dropped between the list and the TSV. It is not a census of Homebrew's markdown software (see the null-description and wording gaps above) and not of the market.

## Not reached

Nothing returned an error. The install counts for the 16 window-cells marked "not listed" are not recoverable from the published files.
