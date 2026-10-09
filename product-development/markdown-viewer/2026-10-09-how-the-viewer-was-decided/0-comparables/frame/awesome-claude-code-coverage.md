# Coverage note: awesome-claude-code

Rows: `awesome-claude-code.tsv`. Admits readers of what AI agents write (RULED strike-list:readers-of-what-ai-agents-write).

- **Who runs it.** hesreallyhim on GitHub (`hesreallyhim/awesome-claude-code`), a hand-picked list; the README says additions are curated. GitHub's API showed 55,293 stars and a last push of 2026-10-09 at the time of reading.
- **Opened.** 2026-10-09, `https://raw.githubusercontent.com/hesreallyhim/awesome-claude-code/main/README.md` (HTTP 200, 208,562 bytes).
- **Entries the list held.** 217 entries of the form `- [name](url) ... - description`, counted from the "Start Here" heading to the end (every section, all parsed). The list states no count of its own.
- **Who is structurally shut out.** Anything its curator did not pick or that postdates the README; readers who use tools built for other agents (Codex, Cursor) unless the entry says so; closed-source or non-GitHub tools the curator does not link; the list covers Claude Code only.
- **Steps from list size to frame size.**
  1. 217 entries.
  2. A mechanical keyword pass on the description over viewing and reading verbs and the objects transcript, session, log, markdown, conversation, history (74 entries matched the object words alone) plus a second pass on preview, viewer, browse, render, display, reader, read (listing a few more).
  3. Hand review of every match against the brief's sentence ("views, reads, browses or renders transcripts, sessions, logs or markdown"). 30 entries judged to say so, or close enough to record with a reason, are in the TSV: 1 in, 15 undecidable, 14 out. The 187 others are not in the TSV.
- **Census or sample.** A census of the list under a reading rule applied by one clerk; the keyword pass is mechanical, the judgement after it is not, and a second reader could draw the line differently. The 187 unrecorded entries can be re-read from the README.
- **Finding.** The list holds no entry whose description says it is a Markdown viewer for a person to read agent output. The nearest are: FlyCrys (a Claude Code GUI with "markdown preview" as one feature), Nimbalyst (co-edit Markdown among other formats, rated in), MDXG Redline (read and comment on AI-written docs in a browser; format not stated), and a family of session and transcript viewers and replayers (claude-replay, Agent Workbench, seedeep, agents-observe, claude-esp, CC Harness). Those read JSONL transcripts or event streams, not Markdown files, so under the brief's eligibility rule (an application a person opens to read or write markdown files) they are undecidable for the frame review rather than in. The larger group of status, cost and usage monitors reads the same logs for numbers and is out.
- **Counts kept.** The README gives no install, user or star count in the entry text (it embeds badge images fetched from shields.io, not read); the field records the section and README line number instead.
