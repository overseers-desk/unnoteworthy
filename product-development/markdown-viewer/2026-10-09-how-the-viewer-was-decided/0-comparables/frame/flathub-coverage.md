# Coverage note: Flathub

- **Who runs it.** The Flathub project, the main repository of Flatpak apps for Linux. Read through `POST https://flathub.org/api/v2/search` with body `{"query":"markdown"}`, paged `page` 1 to 4, HTTP 200 each; then `GET https://flathub.org/api/v2/appstream/{app_id}` once per app, one-second pause between calls, 48 of 48 returned HTTP 200. Opened 2026-10-09.
- **Entries held when opened.** 48 hits (`totalHits` 48; pages of 21, 21 and 6; page 4 empty; 48 distinct app ids). All are `desktop-application`. This is the hit count for one search term, not the size of Flathub.
- **Strike-list rows admitted.** Plain readers of received markdown files (RULED strike-list:plain-readers-of-received-markdown-files), note-takers and personal knowledge managers (RULED strike-list:note-takers-and-personal-knowledge-managers), writers and authors (RULED strike-list:writers-and-authors), students and academics (RULED strike-list:students-and-academics).
- **Who is structurally shut out.**
  - Any maker not on Flathub (many Linux apps ship only as deb, rpm, AppImage, Snap or source).
  - Apps on Flathub whose name, keywords, summary or description does not carry "markdown" in what the search indexes. Search hits that are in the TSV but never mention markdown in their description (Jan, GPT4ALL, Lorem and others) show the search matches on more than the visible text, so I cannot say which fields it indexes.
  - Flathub carries only desktop apps and runtimes that a maker packaged; terminal-only tools are largely absent.
  - Mobile-first and web tools.
- **Steps from list size to frame size.**
  1. Flathub's catalogue, size not read.
  2. Search term "markdown": 48 hits.
  3. Eligibility applied to all 48 by reading the description, reason recorded: in 25, out 17, undecidable 6.
  4. Frame as it stands: 25 in plus 6 undecidable held for the frame review. Eligible 25 of 48.
- **Fields kept.** Id (page URL built as `https://flathub.org/apps/{app_id}`), name, summary, description, `installs_last_month`, `favorites_count`, licence, and the stated verification (`verification_verified`, method, login provider and name) as provenance only, per I6: no buyer evidence is held that buyers weigh it, so it is not a variable. Verified on the list: 36 of 48 (20 of the 25 in). Latest release date comes from the first entry of `releases` in the appstream record (as a date and version); present for all 48, none "not available".
- **Price.** Flathub's records state no price; `price_as_stated` says so. Licence is recorded (44 of 48 carry a free licence per the search facet), which is not the same as price.
- **Install counts.** `installs_last_month` is Flathub's own count of the last month as of 2026-10-09; it is present for all 48.
- **Census or sample.** Census of the search-term result set: all 48 hits paged to exhaustion, no cap, no draw, no sampling rule. Not a census of Flathub's markdown apps, for the reasons in the shut-out list.
