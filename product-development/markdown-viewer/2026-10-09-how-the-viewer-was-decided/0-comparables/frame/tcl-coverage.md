# Coverage note: the Tcl wiki Markdown page, tklib and teatotal

Rows: `tcl.tsv`. Admits application developers embedding a markdown view (RULED strike-list:application-developers-embedding-a-markdown-view).

- **Who runs them.**
  - Tcler's Wiki, `https://wiki.tcl-lang.org/page/Markdown`: a community wiki any visitor can edit. The page was last updated 2022-03-12.
  - tklib: the Tcl/Tk community's Tk module library (`github.com/tcltk/tklib`).
  - teatotal: `github.com/teatotal/teatotal`, whose README calls it a public repository where anyone can put a Tcl module. Its README does not say who maintains it.
- **Opened.** 2026-10-09. Wiki page by curl (HTTP 200). tklib: GitHub contents and recursive git tree APIs for `modules/` (1858 tree entries, not truncated). teatotal: README on raw.githubusercontent.com.
- **Entries the lists held.**
  - Wiki page: 10 named entries under its "Tools" heading, plus 4 packages named in its "Description" list of uses (ruff, mkdoc::mkdoc, tmdoc::tmdoc, mkdic). The page states no count.
  - tklib: 36 modules in `modules/`.
  - teatotal: 15 modules in its README table.
- **Who is structurally shut out.** Developers working in other languages; Tcl packages the wiki page does not list; the wiki's editors' memory (a wiki lists what someone typed in); modules in tklib or teatotal whose README or man page does not mention Markdown. The Tcllib module index was not opened (not named in the brief), so only the wiki's one-line mention of its markdown module stands for it.
- **Steps from list size to frame size.**
  1. 14 wiki entries + 36 tklib modules + 15 teatotal modules = 65 entries.
  2. tklib: only shtmlview carries a Markdown reference (its man page: "basic support for rendering of HTML and Markdown"; no path in the 1858-entry tree contains the word "markdown"). Its description pages were not each opened, so the other 35 are excluded by name and tree path, not by reading their descriptions. shtmlview is also on the wiki page, so it is one row (list field "tcl-wiki-markdown; tklib").
  3. teatotal: the README descriptions of the 15 modules were read; only tkdown parses or renders Markdown. 1 row.
  4. Rows in the TSV: 15 (14 wiki entries, of which shtmlview doubles as the tklib entry, + tkdown). Eligible: 7 in, 6 undecidable, 2 out.
- **Census or sample.** Census of the wiki's Tools and Description lists; census of the teatotal README table; for tklib a census by name and path search, with the caveat in step 2.
- **Provenance.** teatotal's README is the only place the Tk Markdown renderer (tkdown) is described and its stated purpose is chat and transcript bodies. I could not verify from the pages I opened any relationship between the shelf and the operator, and I record none.
- **Counts kept.** Neither the wiki nor either repository gives a use or install count for these entries; the field names where the entry sits.
