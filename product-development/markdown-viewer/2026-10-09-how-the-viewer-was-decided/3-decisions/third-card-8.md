## Third derivation of Card 8

Derived 2026-10-09 by the third-derivation clerk under `briefs/third-derivation-clerk-cards.md`, from the market side alone. The read list and its limits are those stated at the head of `3-decisions/third-card-7.md`: the market files only, no sales record, no capability note, no other clerk's card. The coded corpus was not opened, so I made the exclusive counts from the rival register's sections, by script with the rows checked by eye. By-buyer figures are quoted from findings 31 to 49.

Reading: a text generator would list every form the comparables claim and promise them all. A product designer sees that the claims are what makers chose to print. The designer asks which claim, made as one sentence, separates the readers the operator stands among, and notes that almost nobody answers the second half of the buyer's question.

**Question:** Will it open my files: which markdown does it read, and what happens to the parts it does not understand?

The two halves are separate sentences on a comparable's page, and they get separate options and lines here, as 8a and 8b.

### The populations

As in card 7: ALL (496 weighted) and SHAPE (204) as value counts (taxonomy V13, finding 13, finding 40). Then the 86 reader rivals of the register, the 55 of them outside the Mac App Store, the 31 inside it, and the 28 operator-shaped readers of finding 28.

### 8a. Which markdown

Each reader rival is placed in one option by the forms its pages name (register, "Markdown forms claimed (V13)", sub-field a):

- a reader that names math or diagrams goes to the first option, whatever else it names;
- one that names any other form (GitHub Flavored Markdown, CommonMark, tables, task lists, footnotes, highlighted code, front matter, wiki-links, callouts) goes to the second;
- one that names only "markdown" goes to the third;
- one that names only a non-GitHub flavour goes to the fourth.

The register clips long lines. A clip can only hide a later value, so seven second-option rows might hold an unprinted math or diagram claim (R15, R20, R36, R37, R51, R85, R86). The figures read: reader rivals / outside the App Store / inside it / operator-shaped, then the value counts.

| option | figure | source | capability | sentence |
|---|---|---|---|---|
| GitHub-style markdown plus math or diagrams | 38/86; 21/55; 17/31; 12/28. Value counts: math ALL 182/496, SHAPE 86/204; diagrams ALL 167/496, SHAPE 75/204 | rival register R1 to R86; taxonomy V13(a); finding 13 | Not read. Every rival whose quoted line says how it renders these names a math typesetter or a diagram renderer: KaTeX, MathJax, Mermaid, mermaid.js, PlantUML or a Kroki server (e.g. R13, R21, R24, R70, R79). The shape note describes a Tk program and names none. **I suspect math and diagrams are the part of this option the operator cannot deliver as cheaply as the rest; the cost line belongs beside it.** | To a developer whose agent writes plans with Mermaid charts, on a release page beside MarkView ("KaTeX math", "Mermaid diagrams"): "Tables, task lists, highlighted code, maths and Mermaid diagrams, rendered as GitHub would." Likely answer: opens one of the agent's files and checks the diagram first |
| GitHub-style markdown, no math or diagrams | 27/86; 16/55; 11/31; 8/28. Value counts: tables ALL 215/496, SHAPE 76/204; GitHub Flavored Markdown 109 and 46; task lists 134 and 61; highlighted code 134 and 59 | rival register; taxonomy V13(a) | not read | To a developer reading a README before pushing, beside Markdown Hot Reload ("GitHub Flavored Markdown … tables … task lists … footnotes"): "Your README as GitHub shows it: tables, task lists, code." Likely answer: satisfied until a file holds a Mermaid block |
| "Markdown", no form named | 17/86; 15/55; 2/31; 7/28. Value count ALL 131/496 (finding 13 calls this the least firm figure), SHAPE 38/204 | rival register; taxonomy V13(a) | not read | As glow says it: "Markdown files can be read with Glow's high-performance pager." Likely answer: a terminal reader takes it on glow's name; a reader who must check a table cannot tell from the sentence |
| A named non-GitHub flavour only | 1/86 (ttscoff-mmd-quicklook, MultiMarkdown); 1/55; 0/31; 1/28. Value count, other named flavour: ALL 41/496, SHAPE 21/204 | rival register; taxonomy V13(a) | not read | "Reads MultiMarkdown." Likely answer: a MultiMarkdown writer is pleased; anyone else does not know what it means for their file |

Silent or undecidable on forms, counted once and in no figure above: 3/86; 2/55; 1/31; 0/28. ALL 11/496 silent.

Two install counts, each read inside a single cell, never across cells:

- **VS Code Marketplace (N3).** Among add-ons to the editor's built-in preview, each installed for one form, Markdown Preview Mermaid Support has 5,379,736 installs, Markdown Preview Github Styling 2,941,096 and GitHub Markdown Preview 801,711. The cell differs from the operator on dimensions 1 to 3.
- **Homebrew formulae (N1 and the register's counts, 365-day installs).** The five "markdown only" readers sum to 68,641 (glow 59,634 alone). The five math-or-diagrams readers sum to 9,844 and the five GitHub-style-only readers to 4,558. Glow alone makes the bare claim lead. The count follows the product, not its claim.

**Recommended:** GitHub-style markdown plus math or diagrams. Margin: 11 rows over GitHub-style markdown without them among the 86 readers (38 to 27), 5 outside the App Store (21 to 16) and 4 among the operator-shaped readers (12 to 8). Rests on: the market alone. Seen by: V13(a) as coded and quoted in the register, which sees both options in the same form, a list of forms on a page. It leans towards the runner-up, since seven runner-up rows are clipped where a math or diagram claim could hide. The lead survives one operator coded the other way in every population, and it is thin among the operator-shaped readers. It would be reversed by a blind second coding of the 20 operator-shaped rows in the two options that moved two or more of the twelve out of the first. The one buyer-side instrument that sees both, the VS Code add-on counts, puts the diagram add-on ahead of the GitHub-look add-on by 2,438,640 installs inside one editor.

**Measured in:** reader rivals, 38/86 against 27/86, mixed cells: dimensions 1 to 3 differ for the store and directory rows and are shared for the GitHub-topic and free release rows; dimension 4 is shared. Re-measured within the operator-shaped readers: 12/28 against 8/28, shared on dimensions 1 to 4. The markdown a product reads is not one of the four dimensions, so the ALL and SHAPE value counts stand as context.

### 8b. What happens to the parts it does not understand

| option | figure | source | capability | sentence |
|---|---|---|---|---|
| Shown as plain text, stated | ALL 7/496; SHAPE 7/204; STORE-NS 0/145; reader rivals 2/86 (learn-preview: "In some cases, custom …"; Offline Markdown Preview: "invalid Mermaid …"); operator-shaped 0/28 | taxonomy V13(b); finding 13; rival register | not read | To a reader of agent output: "Anything it cannot render stays on the page as the text you wrote, never dropped." Likely answer: nothing at first; it matters the day a file holds syntax the viewer lacks |
| Warned about, stated | ALL 1/496 (a Snap Store row); SHAPE 0/204; STORE-NS 1/145; reader rivals 0/86 | taxonomy V13(b) | not read | "It tells you when it meets something it cannot show." Likely answer: as above |
| Dropped or hidden, stated | 0 in every population | taxonomy V13(b) | not read | No seller says this, so no sentence is written for it |

Saying nothing is itself the commonest posture, and it is an option: the seller's sentence leaves the question unanswered. Its figure: ALL 483/496; SHAPE 194/204; STORE-NS 142/145; reader rivals 82/86, with two more clipped where the sub-field begins (MacMD Viewer, OnePreview); operator-shaped 28/28. Undecidable, counted once and in no figure: ALL 5, SHAPE 3.

**Recommended:** shown as plain text. Margin among the operators that state a posture: 6 rows over "warned about" in ALL (7 to 1) and 7 in SHAPE (7 to 0). With the silent counted in, saying nothing leads by 476 rows in ALL (483 to 7) and by 187 in SHAPE (194 to 7). The rule used across this clerk's cards is the same: rank among the operators that state a posture, and give the silent-counted margin beside it. Rests on: the market alone. Seen by: V13(b), which sees "plain text" and "warned" in the same form, a reassurance a seller prints. It cannot see "dropped or hidden" in the form that takes, because no seller prints that it loses content. So the line ranks plain text against a warning only and says nothing between plain text and dropping. The lead is thin: seven rows, every one of them in SHAPE (three App Store listings, two VS Code extensions, and GitHub editor, viewer and reader topic rows). It survives one operator coded the other way (6 to 2). No observation in the open files would reverse it. A buyer-side one would be a review or complaint about lost or hidden content in a reader; the five App Store review feeds read (N6) hold none, and none of them is a reader's.

**Measured in:** SHAPE, 7/204 against 0/204, dimensions 1 to 3 shared for its 89 GitHub-topic rows and differing for its 115 store-only rows; dimension 4 shared. ALL, 7/496 against 1/496, dimensions 1 to 3 differ. Not one of the four dimensions, so the rate stands.

### Landing by leading buyer

On 8a the evidence differs by buyer, and the findings by buyer say where.

- **Readers of what AI agents write: the first option, more firmly than the pool.** "Readers of AI output claim more forms than any other column, both in and out of the App Store" (finding 40): tables 11/12, diagrams 10/12, highlighted code 10/12, math 7/12. Inside the App Store diagrams are 5 of 6, against 43% of silent rows. Among the 8 AI-reader rivals, 7 are in the first option and 1 in the second, and that one (Markdown Hot Reload) is a clipped row. Margin over the second option: 6 of 8 rows.
- **Developers alone: no separate tier.** Their distinguishing form is highlighted code: 12/27 against writers alone 3/32 in ALL. Finding 40 says this "survives" inside AlternativeTo (6/13 against 0/22, on 8 and 12 products). Highlighted code sits in both of the first two options, so the tier is not separated by buyer. The developer's sentence names highlighted code. The SHAPE handfuls run the other way (4 of 9 against 3 of 4). The two developer-only reader rivals (Folio, leaf) are both in the first option.
- **Writers alone: the first option, by math.** Math is claimed by 14/32 writer-only rows against 10/27 developer-only rows, and by 13/22 against 5/13 inside AlternativeTo (finding 40). A named non-GitHub flavour is 4/32 against 1/27. The writer's sentence names maths, and may name MultiMarkdown. Only one writer-only reader rival exists (Marked, second option: GitHub Flavored Markdown and MultiMarkdown).
- **Developers and writers together (the documentation reader): same as the pool.** "Inside the App Store, no form separates the documentation reader from the silent rows" (finding 40), and the SHAPE gaps are the cell. Among the 11 documentation-reader rivals: 6 in the first option, 4 in the second, 1 undecidable.

On 8b no buyer lands differently. "V13(b) is silent in at least 97% of every column, and in all 35 leading-buyer rows in SHAPE" (finding 40). No buyer column carries a figure.

### Boundary tests

**Opposite.** Why not "markdown" with no form named, which is what glow says, and glow is the most-installed reader in its cell? Glow is a terminal pager, and within the Homebrew cell its lead is glow's own, not its claim's. Among the readers outside the App Store the bare claim stands at 15 to the first option's 21, and among the operator-shaped readers at 7 to 12. Why not GitHub-style without math or diagrams? It is the runner-up, and the line gives its margin.

**Further.** Beyond math and diagrams: wiki-links (ALL 69/496, mostly notes apps on the Obsidian list), front matter (54), callouts (37), other named flavours such as MultiMarkdown, MDX and Pandoc (41), raw HTML (16) and emoji shortcodes (8). Each is claimed by fewer than the forms in the landing. Front matter is the one that rises in SHAPE (30/204 against 14/145 in STORE-NS, finding 13).

**Joint.** Decided with card 13 (network). Some rivals render diagrams by sending their source to a server: ThisIs-Developer, "Diagram source can be sent to PlantUML, Kroki"; Print, "set up a local Kroki server". Readers that show remote images put them behind a switch: Folio, Markdown Peek, Marklet. A landing on math and diagrams together with "nothing leaves your machine" needs both rendered locally. Decided with card 15 (print and export): an export carries the same forms. Decided with card 14 (appearance): highlighted code brings code themes.

**Buyer.** No live buyer is held. A prediction against named rivals in one cell stands in. By N1's growth measure (30-day count against a twelfth of the 365-day count, computed from the register's counts where N1 does not print it), the Homebrew formula readers have these medians today: math or diagrams 0.46 (leaf 4.16, mdcat 1.53, mdfried 0.46, mdv 0.44, mdserve 0.36); GitHub-style only 0.40 (md-tui 2.08, ekphos 0.78, inlyne 0.40, mdless 0.22, reveal-md 0.05); "markdown" only 0.77 (glow 0.83, mdp 0.81, grip 0.77, mandown 0.24, mcat 0.14). The landing predicts that in the next 30-day window the first group's median stays at or above the second's. It says nothing about the bare group, which today leads both.

**Cost lines:** not read by this clerk; the holder of the capability record adds them beside these landings. Flagged for that holder: rendering math and diagrams. Every rival that names its method uses a math typesetter (KaTeX, MathJax) or a diagram renderer (Mermaid, PlantUML, Kroki), and the shape note names none for this offering.
