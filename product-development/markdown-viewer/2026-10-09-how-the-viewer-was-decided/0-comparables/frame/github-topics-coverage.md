# Coverage note: GitHub topics (markdown-viewer, markdown-editor, markdown-preview, markdown-reader)

Frame file: `github-topics.tsv`. Strike-list rows admitting its buyers: developers and coders (RULED strike-list:developers-and-coders); terminal readers (RULED strike-list:terminal-readers); application developers embedding a markdown view (RULED strike-list:application-developers-embedding-a-markdown-view).

## The list

- **Who runs it.** GitHub (Microsoft). A topic is a free-text label that a repository owner chooses to add; GitHub does not verify it. Search is `gh api 'search/repositories?q=topic:<topic>+stars:>=200&sort=stars&per_page=100'`, paged with `--paginate`, as the signed-in account `overseers-desk`, on 2026-10-09 (UTC, about 07:24).
- **The floor, the mechanical rule.** A repository enters the frame if it carries the topic and has 200 stars or more at the time of the query (`stars:>=200`). No other filter: archived repositories are kept (flagged in the count column), forks are whatever the search returned, no activity test.
- **Search reported `incomplete_results: false` for every query.**

## Topic totals, with and without the star floor

| topic | all repositories | with 200 stars or more | share kept |
|---|---|---|---|
| markdown-viewer | 1,009 | 28 | 2.8% |
| markdown-editor | 2,691 | 145 | 5.4% |
| markdown-preview | 220 | 5 | 2.3% |
| markdown-reader | 132 | 5 | 3.8% |
| total (rows) | 4,052 | 183 | 4.5% |

The 183 rows are 161 distinct repositories: 22 carry more than one of the four topics (for example `alexishida/Moji`, `vaibhav-kakde-in/mdhero`, `oipoistar/tinta` carry three or four). Each appears once per topic cell in the TSV, with the cell named.

## Who is structurally shut out

- Everything below 200 stars: 3,869 repositories with the four topics (95.5%). The floor is a popularity proxy, not a quality or eligibility test; it excludes a new tool with few stars exactly as it excludes an abandoned one, and favours old projects, which have had longer to accrue stars.
- Products that live on GitHub without these four topics (a repository tagged only `markdown`, `md`, `markdown-notes` or `note-taking` is not here). Other topic labels were not searched.
- Products whose source is not on GitHub (closed-source, GitLab, Codeberg, SourceForge).
- Stars are not use: a repository can be starred as a reference and never installed.
- Search sort is by stars, and the API returns at most 1,000 results per query; all four capped cells (floor applied) are far below that, so the cap did not bind. The unfloored totals were counted with `per_page=1` and not enumerated.

## Steps from list size to frame size

1. Repositories with each topic: 1,009 / 2,691 / 220 / 132 (table above).
2. Mechanical floor (200 stars or more): 28 / 145 / 5 / 5 = 183 rows (161 distinct repositories).
3. Eligibility (hand-applied from the repository name and description, reason in the TSV), on distinct repositories: 77 in, 40 undecidable, 44 out.
   - out: embeddable editor and preview components and libraries (React, Vue, Angular, Blazor, Django and Rails packages), converters, a theme, a pastebin client, file managers, a list of editors, repositories that are issue trackers or documentation.
   - undecidable: kept for the frame review where the description does not say whether a person opens markdown files with it (knowledge-management systems, wiki servers, WeChat typesetting editors whose hosted or installed form is unstated, plugins that add a feature to a markdown application, repositories described only by a pun or "Mirror of").
4. Per topic cell, rows by eligibility: markdown-viewer 18 in, 5 undecidable, 5 out; markdown-editor 67 in, 37 undecidable, 41 out; markdown-preview 5 in; markdown-reader 4 in, 1 undecidable.

## Census or sample

Each topic cell is a census of the repositories carrying the topic at 200 stars or more, under the floor. It is not a census of the topic and is not a sample of it: the star floor is a truncation, and the cell's prevalence figures are of the starred part only. The topics are an owner-chosen label, so the cell is also self-selected by repository owners.

## Not reached

Nothing returned an error. Repositories below the floor were not read. Release downloads, package-registry installs and live use of these repositories were not looked up (stars only).
