# Coverage note: Snap Store

- **Who runs it.** Canonical. Read through `https://api.snapcraft.io/v2/snaps/find?q=markdown` with header `Snap-Device-Series: 16`, HTTP 200, opened 2026-10-09. A second call to the same endpoint with `fields=` set to the permitted names (base, categories, channel, common-ids, confinement, contact, description, license, links, media, prices, private, publisher, revision, store-url, summary, title, type, version, website) returned the same 100 snaps with those fields.
- **Entries held when opened.** 100 results.
- **Is 100 a cap.** Probably, unconfirmed. The response is exactly 100, the API gives no total and no next-page marker, and `page`, `offset`, `size` and `limit` were each rejected with HTTP 400 ("Bad parameters"), so I could not page past 100 or ask for more. A search term as general as "markdown" returning exactly 100 is what a cap would look like, but I have no document that states a cap and no way to produce hit 101. The list's real hit count is unknown. Which hits the 100 are is decided by the store's ranking, so if 100 is a cap, the frame is the top 100 by an undisclosed ranking and not a census.
- **Strike-list rows admitted.** The same rows as Flathub: plain readers of received markdown files (RULED strike-list:plain-readers-of-received-markdown-files), note-takers and personal knowledge managers (RULED strike-list:note-takers-and-personal-knowledge-managers), writers and authors (RULED strike-list:writers-and-authors), students and academics (RULED strike-list:students-and-academics).
- **Who is structurally shut out.**
  - Any maker not on the Snap Store.
  - Snaps the search did not rank into the first 100, if 100 is a cap.
  - Snaps whose indexed text does not carry "markdown".
  - Hits are a mix: the store carries command-line tools, servers, libraries-as-snaps and non-markdown apps (a WhatsApp client, an HTTP API client, a static-site generator), so the list is not a list of markdown applications even in its top 100.
- **Counts.** The API returns no install count, rating count or download count for a snap. The list-counts column is therefore empty for all 100 rows and says so. `publisher.validation` as stated by the store (e.g. "unproven") is kept as provenance only (I6).
- **Price.** `prices` is an empty object for every snap read; kept as stated (`prices={}`). It does not say free.
- **Steps from list size to frame size.**
  1. Snap Store catalogue, size not read.
  2. Search term "markdown": 100 results (probable cap).
  3. Eligibility applied to all 100 by reading the description and summary, reason recorded: in 50, out 40, undecidable 10.
  4. Frame as it stands: 50 in plus 10 undecidable held for the frame review. Eligible 50 of 100.
- **Census or sample.** Cannot be declared a census. If 100 is a cap it is a truncated result set under the store's ranking, not a random or stated-rule sample, and the frame review should treat it as an unranked-by-us top-100 cut, not as a denominator for prevalence. If 100 is not a cap, it is a census of the search term's hits. Which of the two holds could not be established from the API.
- **Overlap.** The same applications appear on Flathub (QOwnNotes, ghostwriter, Marker, Marknote, Folio, Swifty Notes, MarkText, Inkdrop); the lists were not de-duplicated, because each list stands for a separate place buyers look.
