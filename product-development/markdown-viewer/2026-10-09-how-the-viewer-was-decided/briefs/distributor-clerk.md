# Distributor clerk: the transaction view

Read `briefs/standing-brief-block.md` first, then `briefs/venue-situation.md`, then `/usr/local/src/aesop/pmf-sage/sage-S-survey.md` section 3. Nothing else in the repository is open to you.

For software, the intermediaries whose transactions cross the whole market publish their counts, so this channel is read rather than asked. Write `1-competitions/distributor-notes.md`, each note dated and sourced, answering the method's three questions, what is growing, what died, and what buyers complain about, from:

- **Homebrew analytics**: installs over 30, 90 and 365 days from https://formulae.brew.sh/api/analytics/install/{30d,90d,365d}.json and the cask equivalents under /api/analytics/cask-install/, for every formula and cask whose description holds "markdown" (catalogue at https://formulae.brew.sh/api/formula.json and /api/cask.json). Growth is the 30-day count against a twelfth of the 365-day count.
- **Flathub**: installs over the last month per app from `POST https://flathub.org/api/v2/search` with `{"query":"markdown"}`, and per-app stats where https://flathub.org/api/v2/stats or the app page gives a history.
- **The VS Code Marketplace**: install and rating counts for the first 100 results for "markdown" sorted by installs (the query body is in `briefs/frame-builder-c.md`, which you may read for that one block).
- **PyPI**: downloads over the last month from https://pypistats.org/api/packages/<name>/recent for grip, frogmouth, retext, formiko, mdv and any other markdown viewer or editor you meet.
- **GitHub**: for the repositories glow, frogmouth, grip, mdcat, marktext, zettlr, joplin, obsidian-releases, typora-issues and any with releases you meet, the release download counts and dates through `gh api repos/<owner>/<repo>/releases`, and whether the repository is archived.
- **The Mac App Store**: user rating counts and averages from `https://itunes.apple.com/search?term=markdown&entity=macSoftware&limit=200`, as the only complaint signal a store publishes without reviews text; and, for the five most-rated entries, the newest reviews through `https://itunes.apple.com/rss/customerreviews/id=<id>/sortBy=mostRecent/json` if that endpoint answers, quoting what buyers complain about.

Ask what is growing, what died (archived repositories, products whose last release is more than two years old, apps gone from a store), and what buyers complain about on the way home. Do not ask what to build. Where a source does not answer, say so with the error.

Your final message gives the notes by number with one line each, the counts delivered against what you expected, and what you could not reach.
