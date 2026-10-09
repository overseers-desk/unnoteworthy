# Decision review

The run's decision cards. Each card is a question, the ways the market answers it with a figure for each, the clerks' recommendation, and a line for the ruling. Rule from the sheet below, in the order set out under "The order of ruling" and not from the top of the table down, and open a card where a row raises a doubt. Where a card names another card, it names it by number.

## The ruling sheet

One row a card. *Your part* says what the row asks of you: confirm, rule, commission an observation, or nothing. *Recommended* reads withheld where no option is carried, and the margin column then gives the counts the card stands at. A negative margin means the largest count runs against the recommendation, which then rests on the other evidence its card names. *Rests on* says whether the recommendation stands on the market, on the business's own buyers, or on both, and is blank on a withheld row. *What is held* says whether the recommendation keeps or leaves a value the business already held. *Market-only reading* says where a fresh clerk landed who read the market alone, with neither the business's records nor the first clerk's work in hand (the card files call it the third derivation): agrees, differs, or declines, which means that clerk found nothing in the market to recommend on. *Ruled* says whether you have already ruled the question; where a card leaves your ruling, your ruling stands until you rule again. The clerks are the AI agents who read the survey and wrote the cards. A card's Joint line, where the order of ruling quotes one, is the line on that card saying which other cards it was decided with.

| card | your part | the question | recommended | margin, or the counts it stands at | rests on | what is held | market-only reading | ruled |
|---|---|---|---|---|---|---|---|---|
| 0 | confirm | Am I getting one program, or several things? | One program | 144 comparables (SHAPE 162/204 comparables; ALL 314/496 against SHAPE 18/204; ALL 40/496) | market | keeps it | agrees | open |
| 1 | rule | Who is this for? | Developers and coders | 5 comparables (SHAPE 28/204; ALL 64/496; rival register 15/121; search: platform words VS Code, GitHub and "Linux command line" in the suggestions; volume not searched against SHAPE 23/204 comparables address them; ALL 71/496; rival register 17/121 sections; search volume not searched) | market | nothing held | differs / declines | open |

## The order of ruling

Card 1 unlocks card 0. Card 0's own Joint line says so: "Decided with card 1." and gives one reading per buyer, so card 0 cannot be ruled before card 1 or beside it in a different direction. Card 1 also unlocks everything after the second gate: the seller's sentences are written one per ruled buyer, and the parameters those sentences contain are the cards of the full set, so no later card exists until card 1 is ruled.

Card 1 and card 0 collide on one buyer. Card 1's Joint line: "a ruling for developers or for embedding developers makes the modules a candidate second offering, and a ruling for AI-agent readers puts the operator's questlog beside this program." Card 0's Joint line answers each: "Under developers and coders: one program, with the modules named as where it comes from"; "Under application developers embedding a markdown view: the modules are the offering"; "Under readers of what AI agents write: a family with questlog becomes arguable (18/204), though neither member is known yet." So a ruling on card 1 for embedding developers reverses card 0's recommendation, and a ruling for AI-agent readers weakens it; the other eight buyers leave it standing.

Card 1 also collides with the surface question it names: "Decided with the surface question too: developers in SHAPE are reached by clone or source 72/204, release download 84/204 and package manager 78/204 (F10), which is where the seller's sentence above is delivered." The surface card is not in this set and cannot be ruled without the search-demand leg, which the run lacks this month; the owner rules card 1 knowing the surface it presumes is unruled.

## What passed through

2 cards. Every card offers at least two ways the market sells this, each with a figure. 1 recommendations keep a value the business already holds, 0 leave one. On 1 of the 2 the business held nothing, whatever the line reads. Keeping and leaving were asked for the same proof, a market-only reading by a fresh clerk who saw neither the business's records nor the first clerk's work. Of 2 such readings, 1 agree with the card, 1 split across the two halves of the question (Card 1: differs / declines). The measured-in lines mark a measured population as differing from this business's shape 7 times.

## Open cards

The recommended option and its runner-up in full; the other options by name and figure. The card file holds every option's source, capability and seller's sentence, and the corrections.

## Card 0 · Am I getting one program, or several things?

**Question:** Is this offered as one program, as a program with the parts it is built from offered beside it, as a free core with a paid tier, as one of a family of tools from the same maker, or as a part to build into my own program, and for whom?

**Options**

| option | figure | source | capability | sentence |
|---|---|---|---|---|
| One program | SHAPE 162/204 comparables; ALL 314/496 | taxonomy V04 "single program"; F26 | One Tcl script of 263 lines with two vendored modules, launched with one file path (capability note). Cost line: packaging pipeline adaptation (questlog's), and the repository's missing LICENSE, README, icon, desktop entry and release | In a direct email with the Homebrew tap link, to row 61 ("Developer; GTK framework development and training"; existing_relationship, star 4, response likelihood 54): "One program: install it, open a markdown file, read it. Nothing else to choose." Likely answer: "Fine; one install is what I want." Likely a try once packaged |
| A family of related tools from one maker | SHAPE 18/204; ALL 40/496 | taxonomy V04 "family of programs"; F26 | questlog, the operator's Claude Code session browser, runs on the same two modules and ships through the same release pipeline (capability note, sales record). Cost line: no website for software products exists to present a family | In a direct email, to row 277 ("Full-stack software engineer: 8+ years system design, frontend, backend; JavaScript/Python/AI agents"; known_of, star 2, response likelihood 35): "From the maker of questlog, which browses your Claude Code sessions: the same reader, for any markdown file your agent writes." Likely answer: "I had not heard of questlog; show me the one I need." A known_of contact may not answer; a family name carries little where neither member is known (questlog: 1 star) |

Other options, each with its figure: One program with its components offered beside it (SHAPE 2/204; ALL 7/496); One program in editions: a free core with a paid tier or add-on (SHAPE 9/204 editions, all free by SHAPE's definition; GitHub-topic cells 7/96 state a payment; ALL 100/496 editions and 99/496 free-with-paid-tier); A component only, built into the buyer's own program (SHAPE 0/204; ALL 0/496).

Undecidable on V04, counted once and in no option: SHAPE 14/204, ALL 36/496. Silent: 0 in every population (taxonomy V04). V04 is single-valued, so each comparable sits in one option and the options exclude one another; "program and component" is itself the market's joint of one program with a component.

**Recommended:** One program; margin: 144 comparables over A family of related tools from one maker; rests on: market; seen by: V04 in the SHAPE population, single-valued, so it saw every option in its own value; it leans toward one program, since a bundled companion has no V04 value (the 14/204 undecidable) and components were ruled ineligible in the frame's Tcl cell (5 of 6 rows), but moving every undecidable row to the runner-up leaves 162 against 32, so the lean cannot account for the lead; ALL agrees (314 against 100 weighted for editions, its runner-up), though ALL differs on reach, payment and sale.

**Third derivation:** `3-decisions/third-card-0.md`; agrees; One program, margin 144 comparables over a family of programs (SHAPE 162/204 against 18/204); runner-up in ALL is editions (314 against 100 weighted), kept as context. One program is deliverable by the capability record, so no cost line beside the landing.

**Ruled:** open

## Card 1 · Who is this for?

**Question:** Whose markdown files is this program for: who installs it, who would pay where anyone pays, and who opens their files in it?

**Options**

| option | figure | source | capability | sentence |
|---|---|---|---|---|
| Developers and coders | SHAPE 28/204; ALL 64/496; rival register 15/121; search: platform words VS Code, GitHub and "Linux command line" in the suggestions; volume not searched | F2 (V05); rival register R7, R21, R22, R29, R30, R31, R50, R52, R57, R62, R76, R84, R86, R116, R120; SD-1, SD-4, SD-5 | GFM pipe tables, fenced code, reference links across the document; relative markdown links open in place; `#anchor` scrolls by GitHub's slug rule; F5 keeps folds and scroll (capability note). Link call is `xdg-open`, Linux only; tested on Linux only. Cost line: packaging pipeline adaptation (questlog's) | In a direct email with the Homebrew tap and release links, to row 61 ("Developer; GTK framework development and training"; existing_relationship, star 4, response likelihood 54): "Read a README or a docs folder the way GitHub shows it, in a native window, without a browser and without sending the file anywhere: tables fit the window, anchors jump by GitHub's rule, relative links open in place." Likely answer: "On Linux, fine; is it in my distribution's packages or on Flathub, or do I install Tcl 9 myself?" Likely a try if a package exists |
| Writers and authors | SHAPE 23/204 comparables address them; ALL 71/496; rival register 17/121 sections; search volume not searched | F2 (V05), SHAPE and ALL columns; rival register, "Whom its pages address (V05)" lines, sections R21, R22, R29, R30, R31, R35, R50, R52, R57, R62, R84, R86, R89, R100, R114, R116, R120; SD-1 (no volume), SD-11 (the adjacent term "markdown editor" asks for editing, first page held by roundup publishers) | The program reads and does not edit; reload is the F5 key, not a watch; no export or print (capability note, "What it does not do"). Cost line: editing, file watching and export would each be built | In a direct email with the release link, to row 114 ("Software developer and technical writer, GNU/Linux focused, cryptographic systems interest"; prior_contact, star 4, response likelihood 29): "Keep writing in your own editor; open the file here and press F5 after each save to read it the way your reader will, folded by section, with the tables laid out to the window." Likely answer: "My editor already previews; does it reload by itself, and can it give me a PDF?" Both answers are no today, so most likely a polite decline |

Other options, each with its figure: Bloggers and platform publishers (SHAPE 6/204; ALL 12/496; rival register 2/121; search: no finding speaks to them; volume not searched); Students and academics (SHAPE 19/204; ALL 42/496; rival register 9/121; search: no finding speaks to them, the teaching-year season unread (SD-14); volume not searched); Note-takers and personal knowledge managers (SHAPE 6/204; ALL 13/496; rival register 2/121; search: "Markdown editor Obsidian" as a related search under the adjacent term only; volume not searched); Teams, businesses and organisations (SHAPE 9/204; ALL 40/496; rival register 4/121; search: no finding speaks to them; volume not searched); Terminal readers (SHAPE 1/204; ALL 2/496; rival register 1/121; search: "Is there a terminal markdown viewer?" asked under "markdown viewer", "Markdown viewer linux command line" a related search; volume not searched); Plain readers of received markdown files (SHAPE 3/204; ALL 4/496; rival register 2/121; search: "how to open md file" answered by products for a file in hand, with "App to open MD files" and "How to view md files with formatting" as related searches; "readers (not editors)" in a top result; volume not searched); Readers of what AI agents write (SHAPE 4/204; ALL 12/496; rival register 8/121 (9 counting R84, whose register line is clipped and which F3 names); search: no capture speaks to them; volume not searched); Application developers embedding a markdown view (SHAPE 0/204; ALL 0/496; rival register 0/121; search: no finding speaks to them; volume not searched); Developers and coders together with writers and authors (rival register 13/121 sections name both; the corpus findings give no co-occurrence count).

Silent on whom they sell to, counted once and in no option: SHAPE 150/204, ALL 348/496 (3/496 undecidable only); rival register 88/121 not stated, 1 undecidable (R12). Nine register lines are clipped in the register itself, so its counts are floors. Search volume is "not searched" for every option, since the rank database had no units this month (SD-1); no option is dropped for it.

**Recommended:** Developers and coders; margin: 5 comparables over Writers and authors; rests on: market (the operator's own record for this offering is zero by construction, sales record); seen by: V05 in the SHAPE population, which codes every buyer class from the page's own words and so sees both options; it leans against developers, since GitHub READMEs, the bulk of SHAPE, mostly name no audience (GH-E 63/84 silent) while writers' editors print an audience, so the lead survives the lean; thin: one row coded the other way leaves 27 against 24. Two readings would reverse it: in ALL, where the population differs on reach, payment and sale, writers lead by 7 weighted (71 against 64), and in the rival register writers lead 17 against 15, a tie; and the register's commonest stated posture is developers and writers together (13/121), which a co-occurrence count of V05 within SHAPE would test, the one observation that would carry the joint option instead.

**Third derivation:** `3-decisions/third-card-1.md`; differs, declines to recommend; withheld between Developers and writers together (11 of 86 reader rivals) and Readers of what AI agents write (8 of 86), 0 against 3 of 28 operator-shaped readers; it did not land on Developers and coders (13/86 with writers, 2 without). Capability not read by that clerk; the terminal-reader and team landings it suspects undeliverable are not the ones it withheld between.

**Ruled:** open

## Ruled cards

(no card is ruled yet)
