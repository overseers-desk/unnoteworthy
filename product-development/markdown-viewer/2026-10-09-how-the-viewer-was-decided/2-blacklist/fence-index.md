---
title: "The fence: what is closed to a deriving clerk, and what is open"
date: 2026-10-09
method: "SAGE Survey, the fence (`sage-S-survey.md` section 4), under the methodology's reading of 2026-09-19"
status: "Cut on day one. The offering has never been sold, so the fence holds no sales terms; it closes the code's own self-description, the maker's notes on why the program exists, the sibling products and the sibling runs."
---

# The fence

The fence closes opinion and leaves behaviour open.

**Closed** is any file that holds a value for a parameter of this offering that came from the maker rather than from the market: the program's own description of what it is and whom it serves, a note on why it was written, a design agreement, a sibling product's scope statement, a sibling run, or a document that reasons from any of those. What the maker thinks the market wants is a prior, neither support for a value nor a mark against it, and it reaches a card only through the priors clerk, last.

**Open** is what buyers and sellers did and what exists: what comparable products publish, what their stores count, what people type into a search engine, the operator's public repositories' traffic and release downloads, and the capability facts of the code and the operator's tooling, stated without a value for any parameter.

The test applied to every row: does this file state a value for a parameter of this offering, or a reason the offering exists, and did that come from the maker? Where a file mixes a fact of capability with such a statement, it is closed whole and its capability facts are carried into `1-competitions/capability-note.md` with their source, because a clerk cannot read half a file.

Paths are relative to this repository's root. Sibling repositories are named by the directory each occupies beside this one.

## 1. This repository

| Path | What it carries | Why closed |
|---|---|---|
| `viewer.tcl` | The program, with a header comment stating what it is, how it is launched and what each key does | The present practice: its feature set and its self-description are the maker's positions on the offering's parameters. The mechanisms are restated in the capability note |
| `vendor/streamdoc-1.3.tm`, `vendor/tkdown-2.1.tm` | The two upstream modules, whose header comments state the kinds of document they were written for | Mixed: the parse coverage is a capability fact, carried into the capability note; the statement of intended use is a prior on the buyer |
| The version-control history of the `main` branch | Seven commit messages narrating each feature and the reason it was added | An arm or clerk that can read history reads the fenced self-description; banned channel, as the method says of history |
| The `master` branch | A 2019 screenshot note-taking program under the same repository name, from which the placeholder name and the repository's GitHub description descend | The only source of the placeholder name's meaning; a prior on the name card and nothing else |
| `CLAUDE.md` | The vendoring rule | Open: it states no parameter |
| This run's own record from `3-decisions/` onward, and `README.md` of the run | Rulings, designs, verdicts, claims as they come to exist | Closed to this run's own deriving clerks, as in every run |

## 2. The session memory for this repository

The Claude Code memory directory kept for this repository holds two notes written on 2026-10-08 and 2026-10-09: one recording that the name is a placeholder, one recording why the viewer exists (that other viewers render tables badly), what it builds on, and a design agreement that the find bar and the table grid stay upstream. Both are closed: the first is a prior on the name, the second a stated purpose and a design decision. A clerk's brief lists its read order and these files are not in it; a memory file reaches a session only through its index, so the omission is the enforcement.

## 3. Sibling products of the same operator

| Path | What it carries | Why closed |
|---|---|---|
| `../questlog/` (the checkout beside this repository; GitHub overseers-desk/questlog) | A Claude Code session browser on the same modules, with a README stating its scope, its design principles, what it deliberately leaves out, its price (free) and its packaging | The operator's positions on a related product's parameters. Its packaging scripts are a capability fact, carried into the capability note; its GitHub record is carried into `1-competitions/sales-record.md` |
| `../teatotal/` (GitHub teatotal/teatotal) | The module repository: man pages, demos and README rows for streamdoc and tkdown, each naming the problem the module solves and the kind of document it was built for | Mixed: the modules' coverage is capability; the README rows and man pages state intended use and the audience the maker had in mind |
| The developer-contact roster of the operator's 2026-04-04 outreach campaign for another product, held in the owner's private records repository | A roster of 497 contacts with closeness scores, and the campaign's goal file and approach drafts | Open as a roster (the casting pool for judges and the prospects for the displacement offer); closed as copy: its goal file and drafts state how the operator sells software |

## 4. Sibling runs

| Path | Product |
|---|---|
| Every SAGE run in any other repository of the owner (two exist on 2026-10-09, both for a tourism operator) | Each run's evidence, cards, game record and definition | Closed whatever the product, readable only through the `forms/` each published. Their frames are venue lists and serve as no source list here |

## 5. The method repository's own test case

`../aesop/tests/12/01-Q-software-offering.md` states this product's category and that it has "no premises, no bookings and no local market". The second clause is a framing of the market written by the method's author before any evidence, so the file is closed to deriving clerks; whether the market is local is for the surface card to settle on evidence.

## 6. What is open

| Path | What it carries |
|---|---|
| `0-comparables/2026-10-09-day-one-pull.md` and every corpus file that follows it | What comparable products publish, quoted, and what three published lists count |
| `1-competitions/sales-record.md` | The operator's public repositories' traffic and release downloads, each beside the condition it was taken under |
| `1-competitions/capability-note.md` | What the code does, what it runs on, what the operator's tooling can ship, stated without a value for any parameter of this offering |
| `3-decisions/strike-list.md` | The day-one list as the owner returns it |
| `forms/` | The method's forms as this run copied them |
