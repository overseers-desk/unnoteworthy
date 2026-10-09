# Coverage note: Mac App Store

- **Who runs it.** Apple. Read through Apple's public iTunes Search API, `https://itunes.apple.com/search?term=markdown&entity=macSoftware&limit=200`, HTTP 200, opened 2026-10-09.
- **Entries held when opened.** 170 (`resultCount` 170; the `limit` was 200, so the response was not cut by the limit). This is the number of hits for the one search term, not the size of the store.
- **Strike-list rows admitted.** Writers and authors (RULED strike-list:writers-and-authors), note-takers and personal knowledge managers (RULED strike-list:note-takers-and-personal-knowledge-managers), plain readers of received markdown files (RULED strike-list:plain-readers-of-received-markdown-files).
- **Who is structurally shut out.**
  - Any maker who chose not to list on the Mac App Store: direct-download, Homebrew, GitHub-release and Setapp-only apps (a maker who sells outside the store is absent whatever the app is).
  - Any app that neither names itself nor describes itself with the word "markdown" in the fields the search term matches. An app that calls itself a "plain text editor" or "notes app" and handles `.md` files is absent.
  - Apps the search ranking did not return; Apple does not document how many hits one term can return or how it ranks, so the 170 is what this call returned, not a proven complete set of matches.
  - Free, source-only and clone-and-run tools such as the operator's own product, since the store carries only what a maker listed there.
- **Instrument quirk.** `entity=macSoftware` returned universal and iOS-and-iPadOS apps that also carry a Mac listing, and some entries are described for iPhone or iPad only. `supportedDevices` is kept in the `other_fields_kept` column. No entry was removed for being mobile-first; the eligibility test is the brief's (an application a person installs to read or write markdown files), applied to the description.
- **Steps from list size to frame size.**
  1. Apple's catalogue, size not stated by the API.
  2. Search term "markdown", entity macSoftware, limit 200: 170 entries returned. No de-duplication was needed (all 170 `trackId`s are distinct).
  3. Eligibility applied to every one of the 170 by reading its own description, with a reason recorded in the TSV: in 133, out 26, undecidable 11.
  4. Frame as it stands: 133 in, plus 11 undecidable held for the frame review (not decided by name). Eligible 133 of 170.
- **Of the 133 in**: 106 free and 27 paid, by `formattedPrice`. This is the free-row sub-population that shares the operator's shape on dimension 2, and every paid row differs from the operator on dimensions 2 and 3 (shape note).
- **Fields kept.** Name, seller, price and formatted price, rating count, average rating, release date, current-version date, description, URL and minimum OS are separate columns. Version, genres, bundle id, kind, languages, file size, content rating, current-version rating figures, supported devices, seller URL and currency are in the last column as key=value. Screenshot and artwork URLs, release notes, and the features and advisories arrays were dropped as not bearing on the frame; they remain in the API response, which can be re-opened.
- **Census or sample.** Census of the search-term result set: every one of the 170 returned entries is in the TSV, no draw, no cap reached, no mechanical sampling rule. It is a census of "what the Mac App Store's search for 'markdown' returns", and it is not a census of the Mac App Store's markdown apps, because the search term and ranking decide who appears. A reader should treat any prevalence read off it as a prevalence among store-listed apps that name markdown, as the store returned them on 2026-10-09.
- **Status marks.** None collected beyond store listing itself; ratings are kept as the list's own counts, not as a quality verdict (I6).
