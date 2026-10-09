# Coverage note: AlternativeTo

Rows: `alternativeto.tsv`. Admits writers and authors (RULED strike-list:writers-and-authors), note-takers and personal knowledge managers (RULED strike-list:note-takers-and-personal-knowledge-managers) and terminal readers (RULED strike-list:terminal-readers). The four lists below stand for those three buyers; the list is not split by buyer.

- **Who runs it.** AlternativeTo, run by 27 Kilobyte AB, Stockholm (the page footer). Entries and "likes" are contributed and voted by its users; the site is free and shows paid "Official Partner" placements above the list (one, PrivacyNotes, appeared on every page; it is not a list row and is not in the TSV).
- **Opened.** 2026-10-09. A plain curl fetch of `https://alternativeto.net/software/<slug>/` returned HTTP 403 (5.5 KB) for all four slugs, so every page was read with the serialised-browsing ad-hoc dump (`browser-serialiser --dump`), paged with `?p=N`. Each list's pagination reads "12 of N alternatives" with 12 entries per page.
- **Slug for Marked 2.** `/software/marked-2/` and `/software/marked-app/` return the site's 404 page. `/software/marked/` is the entry for "Marked", described by the site as a "Native macOS tool for Markdown and markup previews with real-time updates, grammar and spelling checks, readability scoring, and export features". The page does not say "Marked 2"; I take this as the brief's list and record the doubt.
- **Entries each list claimed, and read.**

  | List | Page "last updated" (as printed) | Claimed | Pages | Read |
  | --- | --- | --- | --- | --- |
  | Typora alternatives | Sep 25, 2026 (page 1) | 221 | 19 | 221 |
  | Obsidian alternatives | Oct 4, 2026 | 371 | 31 | 371 |
  | Marked alternatives | Aug 18, 2026 | 79 | 7 | 79 |
  | Glow alternatives | Oct 13, 2024 | 52 | 5 | 52 |

  Every page of all four lists was read, so the read count equals the claim for each. 723 rows in all; the same product appears on several lists, so the distinct names number 544 (by exact name). Page 18 of the Typora list printed a last-updated date of Sep 18, 2026 where page 1 printed Sep 25, 2026; I record both and do not resolve it.
- **Who is structurally shut out.**
  - Anything not submitted to the site or not tagged as an alternative to the one product; the lists are what contributors linked to Typora, Obsidian, Marked or Glow, so they are comparables as the site's users see them, shaped by those four anchors.
  - Products that people use without comparing them (the built-in preview in an editor, a plain text viewer, `less`) unless a contributor linked them.
  - The Glow list was last updated in October 2024, two years before reading; its terminal readers are those someone added by then.
  - The Marked list is anchored on a paid macOS-only product, which tilts its entries toward Mac; Glow's tilts to terminal tools; Obsidian's to note-taking apps; Typora's to Markdown editors. The four lists are not interchangeable samples of one population.
- **Steps from list size to frame size.**
  1. 221 + 371 + 79 + 52 = 723 list entries claimed.
  2. 723 read, 0 skipped. Within a page the dump contained each entry block twice; duplicates on the same page were dropped by exact name and no entry was lost (per-list counts match the claims exactly).
  3. All 723 rows are written, with eligibility. By list (in / undecidable / out): Typora 124 / 75 / 22; Obsidian 86 / 234 / 51; Marked 65 / 5 / 9; Glow 45 / 3 / 4. Total 320 in, 317 undecidable, 86 out.
- **Census or sample.** Census of each of the four lists as the site pages them. The union of the four is not a census of the market; it is the set of products someone linked to those four anchors.
- **Eligibility rules applied (mechanical, on the site's description and application-type tags only; the rule id is in each row's reason).**
  - R1 out: the description names Markdown and also a converter, linter, theme or snippet function.
  - R2 in: the description names Markdown.
  - R3 undecidable: a notes, text-editing, writing, wiki, knowledge or terminal tool whose description does not mention Markdown, so the description cannot settle whether it reads or writes Markdown files.
  - R4 out: neither Markdown nor such a tool by description or type (to-do lists, calendars, mind maps and the like).
  Because R2 reads only the description, a product that handles Markdown but does not say so on its AlternativeTo blurb is R3, and a description that mentions Markdown only in passing is R2 in. The frame review should expect both errors; the rules were applied by script, not by reading each of the 723 rows.
- **Counts kept.** Rank on the list (the site's default "Rank" sort), page, the entry's like count where printed ("Like" with no number on the lower pages, recorded as printed), the count of alternatives the site lists for that entry, the license line, and any alert (for example "Discontinued"). The row URL is the list page the entry sat on; individual entry links were not captured.
