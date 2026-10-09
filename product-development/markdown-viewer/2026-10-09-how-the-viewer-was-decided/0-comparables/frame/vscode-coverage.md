# Coverage note: the VS Code Marketplace

Rows: `vscode.tsv`. Admits developers and coders (RULED strike-list:developers-and-coders).

- **Who runs it.** Microsoft. The marketplace is the default extension source of Visual Studio Code.
- **Opened.** 2026-10-09, one POST to `https://marketplace.visualstudio.com/_apis/public/gallery/extensionquery` with the headers and body the brief gives (filterType 8 = Microsoft.VisualStudio.Code, filterType 10 = search text "markdown", pageSize 100, pageNumber 1, sortBy 4, sortOrder 0, flags 914). HTTP 200.
- **Entries the list held.** The response's `TotalCount` is 4720 for that query.
- **Who is structurally shut out.**
  - Anyone who gets extensions elsewhere: the Open VSX registry used by VSCodium and several VS Code forks, JetBrains and other editors' stores, Vim and Emacs packages.
  - Anyone who reads Markdown with VS Code's built-in preview, which ships in the editor and has no marketplace entry. The strongest incumbent for this buyer is not on the list.
  - Anything described on the marketplace without the word "markdown" in the searched fields.
  - The search is a text search, not a category filter, so it also admits entries that merely mention Markdown (the top 100 holds language servers, formatters, an AI assistant and a spell checker). The query counts mentions, not Markdown tools.
- **Steps from list size to frame size.**
  1. 4720 entries match "markdown" for VS Code.
  2. Sorted by installs descending (sortBy 4); the first 100 taken: pageNumber 1, pageSize 100. 100 entries read, 4620 not read.
  3. All 100 rows are in the TSV with eligibility recorded. Eligible: 13 in, 23 undecidable, 64 out. The 64 out and 23 undecidable stay in the file so the denominator can be re-counted.
- **Census or sample.** A sample, under the mechanical rule "top 100 by install count of the 4720". It is a top-N cut, not a random one: it holds the most-installed entries and none of the tail, so a rate computed on it describes the head of the list. Install counts are the marketplace's own and include extensions bundled or auto-installed by other products; the single largest (GitHub Copilot Chat, about 78.7 million) is out.
- **Counts kept per entry.** installs, rating count, average rating, last-updated date, as the API returned them. Short descriptions are the API's `shortDescription`, unedited (one carries question-mark characters where the source had symbols).
- **Eligibility.** Applied as the brief states. Add-ons that extend the built-in Markdown preview (Mermaid, emoji, checkboxes, footnotes, front matter) are kept as undecidable because the description cannot say whether a buyer installs them to read Markdown; extensions that only restyle the preview are out as themes. Reasons are per row.
