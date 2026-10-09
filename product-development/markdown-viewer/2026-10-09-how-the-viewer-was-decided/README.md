# How the viewer was decided: a SAGE run

This folder is one SAGE run: the markdown viewer whose code sits at this repository's root, developed once. The run started on **9 October 2026** and runs under the methodology's reading dated **2026-09-19**. The offering has never been sold, so every stage reads a market the product has not yet entered, and its own record is empty by construction.

The method is in the aesop repository beside this one: `pmf-sage/sage-methodology.md`, with one document per phase (`sage-S-survey.md`, `sage-A-adjudicate.md`, `sage-G-game.md`, `sage-E-establish.md`) and `INVARIANTS.md` as the tie-breaker. The method holds what every run shares; this folder holds everything about this one product and this one market. Stage folders follow the numbering of the earlier run the method was extracted from, so each names its phase below.

**The owner's words, verbatim:** "the current name was a placeholder." and "not only if the product can be sold as is, but also what small changes can be made to make it sell."

**Where to start.** The owner rules from one page, `3-decisions/review.md`. Everything else is the evidence that page stands on.

## Where the run stands: the second owner gate

The Survey is complete, and the second gate is one ruling round of fifteen cards before the owner: the buyer card and every card its leading buyers' sentences call for. The first gate, the day-one strike list, came back unmarked on 9 October, so every buyer row is in and the striking happens on the buyer card.

**Card 1, who this is for, is withheld.** With options that exclude one another, developers and writers named together lead developers without writers 19 to 9 among the 204 free products shaped like the operator, but 12 of the 19 are free Mac App Store listings, whose pages print that pairing; outside them the two stand 7 to 6, and in the 89 GitHub repositories that reach buyers as this program does, 3 to 3. The market-only reading withholds between the same documentation reader and readers of what AI agents write. The observation that would carry it is take-up of a first release among the operator's roster, counted apart for the two kinds of profile.

**The leading buyers** are therefore three: the documentation reader, developers without writers, and readers of AI output. `3-decisions/leading-buyers.md` holds the seller's sentence for each and the fourteen parameters those sentences contain. Each became a card: card 0 (one program or several) and cards 2 to 14 (name, where it is had, what one takes up, cost, licence, systems, markdown, read or write, keeping up with a file, navigation, find, network, export). Each card recommends for the documentation reader, the one buyer both readings of card 1 name, and its Joint line says where the other two land. The season, link behaviour, help, longevity and appearance are in no leading sentence and stay design freedom.

**What the round shows**, in counts from the card check: 8 cards withheld (who it is for, name, where, unit, cost, markdown, keeping up, find), 2 recommendations that keep what the program already does (one program; nothing leaves the machine, said so), 4 that leave it (all three systems, an editor, a contents outline, PDF export), and the licence recommended with nothing held. The owner's question of what small changes would make it sell is answered card by card: the program as it stands is one option on each, and the changes are the others, each with its cost line. Card 3 cannot be ruled without search volume, which the rank database had no units to give this month, and cards 2 and 4 wait on it.

## The stages, and what each folder holds

### 0. Comparables (`0-comparables/`), Survey

`2026-10-09-day-one-pull.md`, the four market-side pulls behind the strike list (37 pages, three published lists, a convenience read). `shape-note.md`, the operator on the four dimensions, with dimension 4 not applicable to software. `codebook-v1.md`, 37 variables drafted blind and frozen before collection. `frame/`: eleven source-list cells with coverage notes (Homebrew formulae and casks with install analytics, the host's Ubuntu package archive, four GitHub topics at 200 stars or more, the Mac App Store search API with prices and rating counts, Flathub with monthly installs, the Snap Store, the VS Code Marketplace top 100 by installs, the Chrome Web Store, four AlternativeTo lists, the curated AI-tools list, the Tcl lists), merged by `merge-frame.py` into `frame.tsv` (1,531 comparables), corrected and sampled by the frame review into `collection-list.tsv` (449 page sets, with `frame-corrections.tsv` recording every split, join and resolution) and cut by `shard-frame.py` into fifteen shards. `frame-review.md`, the adversarial read: verdicts per cell, the forbidden comparisons, the undecidable rule, the sampling rule for the AlternativeTo-only group. `products/`, 449 verbatim profiles, one per comparable, each quoting what the product publishes on every codebook variable with URLs and dates. `coded/`, fifteen coded shards, concatenated by `concat-coded.py` into `coded-corpus.tsv` (449 rows, 428 eligible). `second-coding-sample.md` and `second-coding.tsv`, the blind re-code of every tenth slug; `second-coding.md`, raw agreement per variable from `agreement.py` (0.752 as written, mostly layout below that); `corrections.md`, the corrections pass (21 cells corrected, 98 rule weaknesses recorded). `findings.md`, findings F1 to F49, each citing variable, cell and count (F31 to F49 cross every parameter the cards rule with whom each page addresses, printed by `by-buyer.py`), with the three populations the cards use: ALL (496 weighted), SHAPE (204, the free rows shaped like the operator) and STORE-NS (145). `taxonomy.md`, every coded value's prevalence by cell and overall.

### 1. Competition and the operator's own record (`1-competitions/`), Survey

`rival-register.md`, 121 sections: every comparable coded as reading without editing, and the five largest-demand comparables of each cell that publishes a demand figure, with all-in costs, store counts by cell and the five demand signals (no enquiry and no meeting exist for this offering). `search-demand-findings.md`, SD-1 to SD-16 from seven located results-page captures: no volume this month, the name "markdown viewer" already a crowded title, the Linux page held by forums and package listings, and the season read from relative interest: a June peak, a December trough, and a steep five-year rise in every term; the raw Trends responses sit in `season/`. `distributor-notes.md`, N1 to N7: Homebrew, Flathub, Marketplace, PyPI and GitHub counts over their windows, what is growing (new readers, among them ones built for AI output), what died, and what Mac App Store reviews complain of. `sales-record.md`, this offering's empty record with its condition line and the sibling products' counts kept apart. `capability-note.md`, what exists with no value for any parameter.

### 2. The fence (`2-blacklist/`), Survey, conditional

`fence-index.md` closes opinion and leaves behaviour open: the program's self-description, the commit history, the old branch the placeholder name descends from, the session memory notes, the sibling products' scope statements, every sibling run, the method's own test case.

### 3. Decisions (`3-decisions/`), Adjudicate

`strike-list.md`, returned unmarked. `questions.md`, the parameters as questions with no values. `leading-buyers.md`, the seller's sentence for each leading buyer on card 1 and the parameters those sentences contain, which set the card set. `card-0-one-offer-or-several.md`, `card-1-who-it-is-for.md` and `card-2-name.md` to `card-14-export.md`, each with options, figures, legs, seller's sentences to roster profiles named by row and role, the recommended line for the documentation reader and the other leading buyers' landings on its Joint line, the measured-in line, cost lines, the four boundary tests, and the Priors, Held, Chip and Third derivation lines stamped by the priors clerk. `third-card-0.md` to `third-card-14.md`, the market-only derivations, one per card. `priors-pass.md`, what the closed files held for each card, by pass. `card-check.txt`, the output of the method's check. `integrator-fields.md`, which cards turn with the buyer ruling or wait on another card, and the collisions by Joint line. `review.md`, the owner's page, assembled by the method's tool.

### `briefs/`, `forms/`, `buyer-nouns.txt`

The briefs, one per clerk role, each opening with its read order and passing the launch check; `venue-situation.md` is the paragraph the launch check generates from the shape note and the unstruck rows. `forms/` is the method's forms as this run copied them. `buyer-nouns.txt` lists the words the strike list's rows use for buyers.

## Instruments and named gaps

The rank database (Semrush) had no API units for October 2026, so no term carries a volume, the surface card (card 3) cannot be ruled, and the search-demand findings say so on every line. The results-page capture instrument (SerpApi) was used for seven search-demand captures from one location, and from the same location for the collision check of each candidate name on card 2 and in its third derivation, and its relative-interest-over-time reading, reached through the skill's own request function since the skill has no command for it, read the season for ten terms worldwide and by country. Stores and package repositories publish install counts, so the distributor channel was read rather than asked. The Chrome Web Store has no denominator and is a no-go cell, which leaves the largest single viewer figure in the frame (an extension with 500,000 users) outside every rate. AlternativeTo refuses plain fetches; its pages were read through a serialising browser. Mac-only App Store listings publish no rating counts.

## The folder map

```
0-comparables/        the day-one pull, shape note, codebook, frame, profiles, coded corpus, findings, taxonomy
1-competitions/       rival register, search demand, distributor notes, the operator's record, the capability note
2-blacklist/          the fence: what is closed to a deriving clerk, and what is open
3-decisions/          the strike list, the questions, the leading buyers, the cards, their third derivations, the owner's page
briefs/               each clerk's brief, with the generated situation paragraph
forms/                the forms this run copied from the method
```
