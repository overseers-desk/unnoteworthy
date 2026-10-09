# Distributor notes: the transaction view

Written 2026-10-09 by the distributor clerk. Every count below was fetched on that date from the URL named in the note; raw responses were held in a scratch directory outside the run folder. The three questions are the method's: what is growing, what died, what buyers complain about. Nothing here asks what to build.

Two instrument facts hold for every note. Growth is stated as the source gives it, never as a share of the market, because no source here gives a denominator for "all markdown readers". Where an entry's 365-day count equals its 30-day or 90-day count, that is consistent with the entry first appearing in that window (or first being catalogued); the files do not say which, and I have not guessed.

---

## N1. Homebrew analytics, formulae and casks (2026-10-09)

Sources: https://formulae.brew.sh/api/analytics/install/{30d,90d,365d}.json (windows 2026-09-09, 2026-07-11, 2025-10-09, each to 2026-10-09); https://formulae.brew.sh/api/analytics/cask-install/{30d,90d,365d}.json; descriptions from https://formulae.brew.sh/api/formula.json and /api/cask.json. Selection: every formula and cask whose `desc` holds "markdown" (case-insensitive): 73 formulae and 48 casks. Growth = 30-day count divided by one twelfth of the 365-day count; 1.00 is flat. Counts are Homebrew's opt-in analytics from Homebrew users, not total installs.

Viewers and editors only (converters, linters, parsers, generators left in the raw pull, not shown). Columns: 30d / 90d / 365d / growth.

Formulae, terminal and preview readers:

| formula | 30d | 90d | 365d | growth | description as given |
|---|---|---|---|---|---|
| glow | 4145 | 19272 | 59634 | 0.83 | Render markdown on the CLI |
| grip | 345 | 667 | 5370 | 0.77 | GitHub Markdown previewer |
| mdcat | 683 | 2522 | 5360 | 1.53 | Show markdown documents on text terminals |
| mcat | 36 | 631 | 3125 | 0.14 | Terminal image, video, directory, and Markdown viewer |
| mdless | 50 | 316 | 2710 | 0.22 | Provides a formatted and highlighted view of Markdown files in Terminal |
| treemd | 54 | 329 | 2362 | 0.27 | TUI and CLI dual pane markdown viewer |
| mdfried | 84 | 258 | 2185 | 0.46 | Terminal markdown viewer |
| leaf-markdown-viewer | 431 | 1244 | 1244 | 4.16 | Terminal Markdown previewer with a GUI-like experience |
| mdv | 25 | 155 | 684 | 0.44 | Styled terminal markdown viewer |
| inlyne | 15 | 103 | 451 | 0.40 | GPU powered yet browserless tool to help you quickly view markdown files |
| md-tui | 73 | 181 | 421 | 2.08 | Markdown renderer in the terminal written in rust |
| mdserve | 11 | 43 | 371 | 0.36 | Fast markdown preview server with live reload and theme support |
| mandown | 4 | 18 | 202 | 0.24 | Man-page inspired Markdown viewer |

Casks, readers and editors (obsidian, qlmarkdown and the first dozen by 365d, then every cask whose description says viewer/previewer/reader):

| cask | 30d | 90d | 365d | growth | brew flags | description as given |
|---|---|---|---|---|---|---|
| obsidian | 11345 | 51034 | 194535 | 0.70 | | Knowledge base that works on top of a local folder of plain text Markdown files |
| qlmarkdown | 2087 | 8552 | 32911 | 0.76 | | Quick Look generator for Markdown files |
| mark-text | 23 | 4302 | 22164 | 0.01 | disabled | Markdown editor |
| macdown | 2 | 2311 | 17571 | 0.00 | disabled | Open-source Markdown editor |
| markedit | 1150 | 4810 | 17031 | 0.81 | | Markdown editor |
| typora | 605 | 2545 | 12014 | 0.60 | | Configurable document editor that supports Markdown |
| zettlr | 394 | 1629 | 6698 | 0.71 | | Open-source markdown editor |
| macdown-3000 | 498 | 1945 | 6325 | 0.94 | | Markdown editor with live preview and syntax highlighting |
| markdown-preview | 453 | 2618 | 2618 | 2.08 | | Markdown previewer with bundled Quick Look extension |
| marked-app | 45 | 218 | 1191 | 0.45 | | Previewer for Markdown, MultiMarkdown and other text markup languages |
| macmd-viewer | 96 | 319 | 627 | 1.84 | | Markdown viewer with QuickLook and Mermaid support |
| clearance | 12 | 62 | 328 | 0.44 | | Markdown viewer and editor |
| markviewer | 101 | 244 | 244 | 4.97 | | Minimal markdown editor |
| mdhero | 208 | 208 | 208 | 12.00 | | Markdown viewer and editor |
| markpad | 186 | 186 | 186 | 12.00 | | Markdown viewer and editor |
| telari | 14 | 14 | 14 | 12.00 | | Markdown reader built for typography |

Growing. Read from the counts, not inferred: the largest absolute 30-day counts in the whole pull are obsidian (11345), glow (4145), qlmarkdown (2087) and markedit (1150), all at growth 0.70 to 0.83, i.e. running at or below their twelve-month average. Growth above 1.5 among readers appears only on entries that are new in the window: leaf-markdown-viewer (365d = 90d = 1244), markdown-preview (365d = 90d = 2618), markviewer (365d = 90d = 244), mdhero, markpad and telari (365d = 90d = 30d), plus md-tui (2.08), macmd-viewer (1.84) and mdcat (1.53). Seven reader/viewer cask or formula entries (leaf-markdown-viewer, markdown-preview, markviewer, mdhero, markpad, telari, and treemd by its GitHub first release 2025-11-08) have a first appearance inside the last year. The mdcat formula now points at https://github.com/BIRSAx2/mdcat, not the original repository (see N5). The 12.00 growth figures are the arithmetic floor of an entry whose whole history is one window; they are not a rate.

Died. Brew itself marks 14 of 48 markdown casks `disabled: true` and 10 `deprecated: true` (flags overlap), and 1 of 73 formulae disabled and 4 deprecated. Disabled casks among viewers/editors: mark-text (365d 22164, 30d 23), macdown (365d 17571, 30d 2), pine, qlcommonmark, mindforger, panwriter, texts, uncolored, ttscoff-mmd-quicklook, eme, inkdown, foldingtext, shiba, haroopad. Deprecated formulae: ltex-ls, swagger2markup-cli, csvtomd (also disabled), peg-markdown. A brew `disabled` flag is Homebrew's act; mark-text's own repository is still releasing (N5), so the flag is not the product's death.

Complaints. Not carried by this source. It publishes counts only.

Designer against generator: a generator would read the table as "markdown tools are popular"; a designer reads that the biggest readers are flat to falling, and that the visible movement is a thin layer of new small viewers (seven entries) each at 14 to 2600 installs a year.

---

## N2. Flathub, the markdown search (2026-10-09)

Sources: `POST https://flathub.org/api/v2/search` with `{"query":"markdown"}` pages 1 to 3 (`totalHits` 48, all 48 read, 48 distinct app ids), and `GET https://flathub.org/api/v2/stats/<app_id>` for each (all 48 answered; history 2026-04-11 to 2026-10-07 for most, about 180 days). Installs last month is the search field `installs_last_month`. Growth here = last 30 days against the mean 30-day total of the earlier days in that history; it is not the 365-day measure N1 uses, because Flathub's history is six months.

Counted from the response: 48 hits, all `desktop-application`; 36 verified, 44 under a free licence. A hit is any app whose index text holds "markdown"; about a third are not markdown readers or editors (Jan, GPT4ALL, Cohesion, Simplenote, MindMate, Gai, Lorem, Typography, KonbuCase, Whisp, Kalba).

| app | last month | total | growth | summary |
|---|---|---|---|---|
| Apostrophe | 5267 | 249083 | 0.90 | Edit Markdown in style |
| MarkText | 3370 | 148193 | 1.05 | Next generation markdown editor |
| Text Pieces | 3101 | 85044 | 4.07 | Developer's scratchpad |
| Marknote | 2371 | 53316 | 0.60 | Write down your thoughts |
| ghostwriter | 1827 | 85446 | 1.16 | Distraction-free text editor for Markdown |
| Manuscript | 1763 | 9982 | 1.23 | Read and edit Markdown files (added 2026-03-25) |
| Folio | 1271 | 44873 | 1.34 | Beautiful markdown note-taking app |
| Jottr | 1185 | 4217 | 8.78 | Simple text and markdown editor (history from 2026-04-01) |
| QOwnNotes | 1109 | 75706 | 0.95 | Markdown note-taking |
| Cedilla | 718 | 5668 | 1.02 | Markdown Text Editor |
| Swifty Notes | 678 | 5748 | 0.75 | Native GTK markdown notes with preview and automation |
| Ferrite | 586 | 6489 | 0.94 | Write and preview markdown |
| Marker | 533 | 57659 | 1.01 | Powerful markdown editor for the GNOME desktop |
| ReText | 427 | 15442 | 1.21 | Simple text editor for Markdown and reStructuredText |
| Reinschrift | 422 | 2407 | 1.92 | Manage your todos in Markdown |
| ThiefMD | 297 | 21967 | 0.88 | The markdown editor worth stealing |
| Formiko | 194 | 8328 | 1.52 | reStructuredText and Markdown editor |

Growing. Manuscript, a viewer-and-editor first listed 2026-03-25 ("Read and edit Markdown files"), is at 1763 installs last month and 9982 total, growth 1.23. Jottr and Reinschrift show the highest rates but on baselines of 133 and 215 a month. Text Pieces' 4.07 is on a 30-day count of 3135 against a prior-month mean of 770, and I did not find its cause in these pages.

Died. Flathub publishes no "removed" list here; an app gone from the store would not appear in a search. What the pages show are `updated_at` dates: the oldest in the markdown set are 2Dtaskboard (2025-06-29) and Essentialist (2025-09-23); no app of the 48 has an `updated_at` more than two years before 2026-10-09. Marker's last update is 2026-04-10, ThiefMD's 2026-04-04, Norka's 2026-04-08. Marknote fell to 0.60 of its prior mean (2371 last month against a prior-month mean of 3999).

Complaints. Not carried by this source.

Not reached: `https://flathub.org/api/v2/stats` (no app id) answers HTTP 307 to `http://nginx-flathub.apps.openshift.gnome.org/api/v2/stats/`, a plain-http host I did not follow; the per-app route above answered instead, so the aggregate was not used.

Designer against generator: a generator would take Apostrophe at 5267 as the reader to copy; a designer notes it is a GNOME editor, and the one product on the list described as reading ("Read and edit Markdown files") is under a year old and already past 1700 a month.

---

## N3. VS Code Marketplace, first 100 for "markdown" by installs (2026-10-09)

Source: `POST https://marketplace.visualstudio.com/_apis/public/gallery/extensionquery`, headers and body exactly as in the run's frame brief (sortBy 4, flags 914, page 1, size 100). Response status 200; `TotalCount` 4720; 100 returned. Installs are the marketplace `install` statistic; rating counts are `ratingcount`.

Total installs across the 100: 297,098,688. The list is mostly not markdown tools: rank 1 is GitHub Copilot Chat (78,696,223), rank 2 Prettier (72,166,134), others are language support (Vue, R, LaTeX, Solidity). Markdown-specific entries, by installs:

| rank | extension | installs | ratings (avg) | last updated |
|---|---|---|---|---|
| 3 | Markdown All in One (yzhang) | 14,704,347 | 172 (4.69) | 2025-03-09 |
| 4 | markdownlint (DavidAnson) | 12,338,948 | 86 (4.52) | 2026-08-02 |
| 5 | Markdown Preview Enhanced (shd101wyy) | 10,429,484 | 145 (4.33) | 2026-10-09 |
| 10 | Markdown Preview Mermaid Support (bierner) | 5,379,736 | 60 (4.62) | 2026-05-21 |
| 13 | Markdown PDF (yzane) | 4,203,421 | 131 (4.35) | 2026-07-29 |
| 17 | Markdown Preview Github Styling (bierner) | 2,941,096 | 39 (4.54) | 2025-06-12 |
| 22 | Office Viewer (cweijan), "View word, excel, powerpoint files and using WYSIWYG editor for markdown" | 1,556,537 | 100 (4.31) | 2026-08-16 |
| 35 | GitHub Markdown Preview (bierner) | 801,711 | 21 (5.0) | 2026-06-02 |
| 37 | Preview (searKing) | 787,184 | 40 (3.2) | 2024-12-11 |
| 40 | Print (pdconsec), "Rendered Markdown, coloured code." | 740,400 | 55 (4.73) | 2025-07-27 |
| 42 | Auto-Open Markdown Preview (hnw) | 671,717 | 35 (3.97) | 2017-03-04 |
| 74 | Markdown Editor (zaaack) | 229,985 | 37 (4.51) | 2026-09-02 |
| 88 | Offline Markdown Preview (Bowlerr) | 171,391 | 2 (5.0) | 2026-07-12 |
| 91 | Instant Markdown (dbankier) | 164,280 | 39 (3.46) | 2021-05-11 |
| 95 | Typora (cweijan) | 148,967 | 14 (4.86) | 2025-04-28 |

Growing. The marketplace gives a cumulative install count and no history, so this source does not answer growth. The only dated signals are last-updated: Markdown Preview Enhanced was updated the day of the pull, and 68 of the 100 were updated within two years.

Died. 32 of the 100 have a last-updated before 2024-10-09 (more than two years). Among markdown ones: Auto-Open Markdown Preview (2017-03-04, 671,717 installs), Markdown Theme Kit (2017-04-04), Markdown Shortcuts (2019-11-10), Markdown+Math (2021-06-06), Instant Markdown (2021-05-11), MDX Preview (2021-11-28), Markdown Checkboxes (2022-11-03), Markdown Footnotes (2022-11-18), CS50-Flavored Markdown (2023-04-13), MDX (deprecated) (2022-08-08, the marketplace's own title). Markdown All in One, the most installed markdown-specific entry, was last updated 2025-03-09.

Complaints. Only the rating signal exists in this call: the lowest-rated markdown-specific entries with at least 30 ratings are Preview (searKing) 3.2 over 40 ratings and Instant Markdown 3.46 over 39. No review text was fetched.

Designer against generator: a generator reads 14.7 million installs as demand for a markdown viewer; a designer reads that this is the built-in preview plus helpers inside one editor, bought by people already in the editor, and that stale preview helpers still hold hundreds of thousands of installs.

---

## N4. PyPI, downloads over the last month (2026-10-09)

Source: `https://pypistats.org/api/packages/<name>/recent` (`last_month`), release dates from `https://pypi.org/pypi/<name>/json`. Downloads include mirrors and CI installs; I did not check whether the endpoint strips them.

| package | last month | last release | note |
|---|---|---|---|
| grip | 30,167 | 4.6.2, 2023-10-12 | GitHub repository last pushed 2024-07-10 |
| mdv | 2,510 | 1.7.5, 2023-10-02 | Terminal Markdown Viewer |
| frogmouth | 1,232 | 0.9.2, 2023-11-28 | A Markdown document viewer for the terminal |
| glow | 935 | (not examined) | PyPI name `glow`; I did not confirm it is the Charm tool |
| retext | 485 | 8.1.0, 2025-01-09 | Simple editor for Markdown and reStructuredText |
| formiko | 67 | 2.0.0, 2026-08-11 | |
| rich-cli | 22,138 | (not examined) | renders markdown among other things |
| markdown-viewer | 31 | | other viewers met by name search |
| mdviewer | 31 | | |
| mdterm | 17 | | |
| textual-markdown | 22 | | |

`mdless` and `markdown-preview`, `terminal-markdown-viewer`, `md-viewer`, `glow-md`: HTTP 404 (no such pypistats package). For scale only: `markdown` 90,911,256, `markdown-it-py` 448,478,871, `mistune` 60,924,850, `mkdocs` 13,132,209 are libraries and generators, not viewers.

Growing. This endpoint gives day/week/month, not a trend: grip's last_day 1433, last_week 8323 and last_month 30167 are consistent with a flat rate. Not answered beyond that.

Died. Three of the five named viewers have no release in over two years as of this date: grip (2023-10-12), frogmouth (2023-11-28), mdv (2023-10-02), and still download at 30,167, 1,232 and 2,510 a month.

Complaints. Not carried by this source.

Designer against generator: a generator treats 30,167 monthly downloads as a living product; a designer sees an unreleased-for-three-years tool installed by pipelines and habit, which says what people still reach for, not that it is liked.

---

## N5. GitHub repositories and releases (2026-10-09)

Source: `gh api repos/<owner>/<repo>` and `repos/<owner>/<repo>/releases?per_page=100`, paginated. Download counts are the sum of asset `download_count` across the stated releases and cover GitHub release assets only (not Homebrew, apt or store installs).

| repository | archived | last push | releases (newest) | releases in last 365d, their downloads |
|---|---|---|---|---|
| charmbracelet/glow | no | 2026-10-05 | 24 (v3.0.0, 2026-08-11) | 2, 285,591 |
| Textualize/frogmouth | no | 2024-08-01 | 8 (v0.9.1, 2023-11-02) | 0, 0 (assets: 0) |
| joeyespo/grip | no | 2024-07-10 | 0 releases; newest tag v4.6.1 | no releases |
| swsnr/mdcat | **yes** | 2026-06-19 | 64 (mdcat-2.7.1, 2024-12-14) | 0 |
| BIRSAx2/mdcat | no | 2026-10-01 | 15 (mdcat-2.18.0, 2026-10-01) | 15, 2,715 |
| marktext/marktext | no | 2026-10-09 | 56 (v0.21.1, 2026-10-08) | 20, 751,415 |
| Zettlr/Zettlr | no | 2026-10-06 | 181 (v4.8.0, 2026-09-18) | 17, 884,503 |
| laurent22/joplin | no | 2026-10-09 | 423 (v3.7.21, 2026-09-25) | 35, 3,530,285 |
| obsidianmd/obsidian-releases | no | 2026-10-09 | 173 (v1.14.4, 2026-10-05) | 12, 35,862,310 |
| typora/typora-issues | no | 2025-07-25 | 0 releases | no releases (issues repository) |
| MarkEdit-app/MarkEdit | no | 2026-10-09 | 95 (v1.36.0, 2026-09-23) | 15, 1,183,007 |
| sbarex/QLMarkdown | no | 2026-10-04 | 56 (1.5.7, 2026-10-02) | 9, 232,974 |
| MacDownApp/macdown | no | 2023-07-10 | 37 (v0.8.0d71, 2020-02-21) | 0 |
| clearance (prime-radiant-inc) | no | 2026-09-15 | 20 (v1.3.5, 2026-06-06) | 20, 28,632 |
| Skardyy/mcat | no | 2026-10-03 | 33 (v0.6.5, 2026-08-29) | 17, 13,174 |
| benjajaja/mdfried | no | 2026-10-08 | 61 (v0.22.7, 2026-10-08) | 41, 2,233 |
| henriklovhaug/md-tui | no | 2026-10-02 | 42 (v0.11.0, 2026-10-02) | 10, 2,497 |
| epistates/treemd | no | 2026-10-07 | 42 (v0.9.1, 2026-09-14); oldest 2025-11-08 | 42, 3,350 |
| Inlyne-Project/inlyne | no | 2026-08-06 | 18 (v0.5.3, 2026-08-06) | 4, 1,398 |
| ttscoff/mdless | no | 2026-06-25 | 88 (2.1.68, 2026-06-25) | 4, 0 (no assets) |
| axiros/terminal_markdown_viewer (mdv) | no | 2024-05-15 | 11 (1.6.3, 2016-12-08) | 0 |
| lukakerr/Pine | no | 2022-12-20 | 10 (0.1.0, 2019-09-30) | 0 |
| egoist/eme | no | 2022-12-10 | 16 (v0.15.1, 2020-07-23) | 0 |
| rhysd/Shiba | no | 2026-07-20 | 16 (v2.0.0-alpha.4, 2026-03-28) | 5, 743 |
| BoostIO/BoostNote-App | **yes** | 2026-03-17 | 53 (v0.23.1, 2021-11-29) | 0 (all-time 1,035,582 in one release; 2,859,669 across all) |

obsidian-releases and typora-issues returned no product source on the releases endpoint beyond what the table shows. `uranusjr/macdown` redirects to MacDownApp/macdown.

Growing. Cadence and download counts agree for marktext (v0.20.0 on 2026-10-02, 41,247 downloads on that release alone, v0.21.0 and v0.21.1 on 2026-10-08), MarkEdit (1,183,007 in the year), QLMarkdown (232,974), Zettlr (884,503) and glow (285,591 from two releases, v3.0.0 on 2026-08-11 at 94,334). Newly created viewers releasing weekly: mdfried (41 releases in the year, 2,233 downloads), treemd (42 releases in 11 months, 3,350), mcat (17, 13,174), clearance (20 releases since 2026-03-05, 28,632).

Died. Archived: swsnr/mdcat (its README: "This repository is no longer maintained. You can find a maintained fork at https://github.com/BIRSAx2/mdcat"), and BoostIO/BoostNote-App. Last release more than two years old at 2026-10-09: Textualize/frogmouth (2023-11-02), MacDownApp/macdown (2020-02-21, repository last pushed 2023-07-10), axiros/terminal_markdown_viewer (2016-12-08), Pine (2019-09-30), eme (2020-07-23), BoostNote-App (2021-11-29), grip (no releases; newest tag v4.6.1, last commit 2023-10-13 on master per the commits API, repository pushed 2024-07-10).

Complaints. Not carried here. typora-issues holds 1,097 open issues (repository count) and Zettlr 548, marktext 318, joplin 649; I read no issue text.

Designer against generator: a generator reads 35.8 million downloads of Obsidian releases as the market; a designer reads that the one dominant product is a notes workspace, and that the viewer-shaped repositories releasing this year (mdfried, treemd, md-tui, mcat, clearance) have download counts in the thousands to tens of thousands.

---

## N6. The Mac App Store (2026-10-09)

Source: `https://itunes.apple.com/search?term=markdown&entity=macSoftware&limit=200`. Status 200; `resultCount` 170 (limit 200 asked, 170 returned). 54 of the 170 carry any user rating. Prices are as the store gave them; "Free" includes free-with-in-app-purchase, which the search does not separate. 12 of the 170 have a current-version release date before 2024-10-09.

Ten most-rated:

| id | app | seller | ratings | average | price shown | current version released |
|---|---|---|---|---|---|---|
| 1225570693 | Ulysses: Writing App | Ulysses GmbH & Co. KG | 2130 | 4.58 | Free | 2026-10-06 |
| 1580431405 | HTML Editor | Intrepid Corporation LTD | 869 | 4.15 | Free | 2026-01-19 |
| 1527036273 | Taio - Markdown & Text Actions | 颖 钟 | 658 | 4.56 | Free | 2023-09-13 |
| 1494902837 | Markdown゜ | Teleprompter LLC | 484 | 4.55 | Free | 2026-09-30 |
| 1442727443 | Minimal \| Notes | Timeless LLC | 294 | 4.68 | Free | 2026-07-04 |
| 1534437697 | Flashtex: Study Flashcards | Mika Kruschel | 186 | 4.75 | Free | 2026-09-29 |
| 1183407767 | MWeb - Markdown Writing, Notes | 禄海 区 | 153 | 4.54 | Free | 2026-05-03 |
| 1507139439 | One Markdown | 禄海 区 | 148 | 4.61 | Free | 2026-05-03 |
| 6720708363 | Obsidian Web Clipper | Dynalist Inc. | 103 | 4.31 | Free | 2026-07-22 |
| 1496067471 | Quick Draft: Notes & Markdown | giddyapp, LLC | 102 | 4.65 | Free | 2025-03-22 |

Read.md (id 6760943472, Pavel Abin, 84 ratings, 4.96, first released 2026-03-25, current 2026-10-05) is the one entry in the top eleven described as a reader by name. Rating counts across the whole 170 are small: only 15 entries have 20 or more.

Growing. Dated by first release in the result: Read.md (2026-03-25), .Md Viewer (2026-03-23, 6 ratings), Marklens: Markdown Reader (2026-06-10), MarkFlow:Read Markdown files (2025-11-17), MD Flow - Markdown Reader (2026-04-21), Just a Markdown Viewer (2026-08-04), Quick Markdown Viewer (2026-04-07). Seven viewers-by-name first released within 19 months, none with more than 84 ratings.

Died. Current-version dates before 2024-10-09 on 12 entries, including Taio (2023-09-13, 658 ratings) and Copy Link in Markdown (2021-09-21). "Gone from a store" cannot be shown from one pull; I did not compare against an earlier listing.

Complaints. `https://itunes.apple.com/rss/customerreviews/id=<id>/sortBy=mostRecent/json` answered HTTP 200 for all five. Each returned up to 50 most recent reviews (the feed covers the United States store and the app as a whole, not only its Mac build). Low-star (1 or 2) reviews per feed: Ulysses 21 of 50 (mean 3.1, 2026-03-03 to 2026-10-04); HTML Editor 45 of 50 (mean 1.42, 2025-06-22 to 2026-09-05); Taio 12 of 50 (mean 3.8, back to 2022-04-15); Markdown゜ 27 of 45 (mean 2.4, 2020-06-13 to 2026-06-20); Minimal | Notes 9 of 50 (mean 4.04, 2023-05-23 to 2026-08-07). HTML Editor is not a markdown tool; the search returned it. Quoted:

- Ulysses, price and gate: "Deceptive Pricing: Shows in app purchases but that's not the case you can't use the app unless you start a 7 day trial which isn't long enough to evaluate something like this, or pay $39.99 a year." (2026-03-21). "Scam: It's not free. You have to pay $40 a month to type. It's not worth it" (2026-07-26). "A Paid App Disguised as Free: ... It is locked in 'read only' mode so you can only view their sales pitches while prompting you to either pick a free trial or pay to edit files." (2026-04-24).
- Ulysses, the format: "Ulysses is one of the most polished writing apps on macOS, yet it continues to use absolutely hideous, always-visible Markdown markup and refuses to give users the option to decide for themselves whether they want to see all those formatting symbols or not." (3 stars, 2026-08-12). "I'd never pay for subscription based. I own their one-time purchase version; which they no longer update." (2026-09-20).
- HTML Editor: "Forces the user to purchase a subscription upon first use." (2026-07-30). "Payment Required: Listed as a free app... if you want to do more than have it take up space on your device, you have to pay $2.99/WEEK!" (2026-05-22). "Went to subscription. Bye. This app used to be free but now they require a weekly subscription." (2026-04-03).
- Taio: "Despite having a roadmap on Trello the fact this app has no Z-E-R-O updates in 2 years means it's likely abandoned - you have been warned." (2026-07-12). "The lifetime purchase was a waste of money." (2024-05-28, after "the developer has lost interest").
- Markdown゜: "This thing doesn't work for editing. As soon as you get the cursor where you want it in a document and then hit a key with the keyboard, it moves the cursor to the end of the document." (2026-06-20). "Lost my document: I spent an hour writing a document and this app just lost it." (2023-06-28). "Still cannot open md files from Google Drive." (2020-06-21).
- Minimal | Notes: "not worth the subscription when something else is once off payment and just as good if not better" (2025-01-01). "Keeps Crashing and losing my work: I've had the trial for about an hour now and it's crashed, unsaved three times already." (2024-05-26).

What the five feeds hold: the largest low-star cluster in the Mac App Store pull is about price shown as free and then gated (Ulysses, HTML Editor, Minimal | Notes), the next is about edits not saving or the cursor jumping (Markdown゜), the next about a paid app left without updates (Taio, Ulysses). Reading a file without being asked to pay or sign up appears as a complaint only by its absence from these feeds; no review asks for a viewer.

Designer against generator: a generator would conclude people want a better markdown editor; a designer reads that the unhappy buyers on the store are unhappy about being charged before use and about edits that lose work, neither of which a free reader that never edits has to answer.

---

## N7. Cross-source reading and shape cautions (2026-10-09)

Compared on the operator's shape (venue-situation: reached by git clone only, nothing paid, no sale taken). Brew, Flathub, VS Code and the App Store count installs through stores that do dimension 1 and 3 differently from this operator; PyPI and GitHub releases are the sources closest to its shape, and both are download counts, not use. Every rate in N1 to N6 is therefore marked *differs* on dimensions 1 to 3 except the GitHub release counts in N5 and the free rows of N1 to N3.

What is growing, consolidated: reader-shaped entries that did not exist a year ago (N1 seven entries, N5 four repositories, N6 seven store entries); the established editors are flat or falling in Homebrew's window.

What died, consolidated: archived mdcat (N5), disabled brew casks mark-text and macdown (N1) against a MarkText repository that shipped v0.21.1 on 2026-10-08 (N5), grip, mdv and frogmouth unreleased for about three years while still downloaded (N4), and stale VS Code preview helpers (N3).

What buyers complain about: paying before use, a "free" listing that is a trial, subscription replacing one-time purchase, edits that lose or jump, and apps left unupdated (N6). The complaint data are for editors and writing apps on the store; none of the five feeds is for a read-only viewer.

---

## Not reached or limited

- Homebrew: no error. Counts are opt-in analytics; entries absent from an analytics file read as zero in my table, which may be a long-tail cut rather than zero installs.
- Flathub `/api/v2/stats` (aggregate): HTTP 307 to a plain-http host, not followed. Per-app stats answered for all 48. Flathub history is about 180 days, so no 365-day growth.
- VS Code Marketplace: answered; no install history exists in the response, so growth is not answered. No review text fetched.
- PyPI: one HTTP 429 (RATE LIMIT EXCEEDED) on `mkdocs`, retried after a pause and answered; 404 for `mdless`, `markdown-preview`, `terminal-markdown-viewer`, `md-viewer`, `glow-md`. The PyPI `glow` package was not examined to see whether it is the Charm tool.
- GitHub: `joeyespo/grip` and `typora/typora-issues` have no releases through the releases endpoint; no issue text read.
- Mac App Store: search returned 170 of 200 requested. Review feeds cap at the newest 50 per app, the US store only, and the app-wide feed is not Mac-only. "Gone from a store" not shown.
- Not asked of any source: what to build, and any single operator's business.
