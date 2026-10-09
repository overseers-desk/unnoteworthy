# reor: verbatim profile

Cells: alternativeto:Typora; alternativeto:Obsidian (weight 2, AlternativeTo sampled stratum). Condition obeyed: eligibility re-checked on the product's own page; rates dated to the list.

## Names as published
- "Reor" (AlternativeTo page title "Reor: A self-organizing AI note-taking app that runs models locally"); README heading "Reor Project"; repository "reorproject/reor"

## How the AlternativeTo entry was found
Start URLs (.../typora/ and .../obsidian/?p=4) are list pages (entry link not captured). My first guess, https://alternativeto.net/software/reor/about/, was a different product (page title "Reor Calculator: Reor is a powerful calculator blended into", Windows scientific calculator) and was discarded. Web search "Reor AI personal knowledge management app alternativeto" returned https://alternativeto.net/software/reor-1/ (page title "Reor Alternatives"). I read https://alternativeto.net/software/reor-1/about/ through WebFetch (condensed rendering; curl gets 403); the description there matches the frame's list blurb.

## Pages read (all captured 2026-10-09)
- https://alternativeto.net/software/reor-1/about/ : read through WebFetch
- https://alternativeto.net/software/reor/about/ : read through WebFetch, a different product, not used
- https://github.com/reorproject/reor : HTTP 200
- https://api.github.com/repos/reorproject/reor and .../releases (via gh) : success
- https://raw.githubusercontent.com/reorproject/reor/main/README.md : HTTP 200
- https://www.reorproject.org (AlternativeTo website link, repository homepage field): UNREACHABLE. curl: "Could not resolve host: www.reorproject.org" (curl error 6). Also linked and not read: the docs pages.

## V01 Eligibility
Frame record of the AlternativeTo row: "Reor is an AI-powered desktop note-taking app: it automatically links related ideas, answers questions on your notes and provides semantic search. Everything is stored locally and you can edit your no[tes with an Obsidian-like markdown editor]." README: "Reor is an AI-powered desktop note-taking app: it automatically links related notes, answers questions on your notes and provides semantic search. Everything is stored locally and you can edit your notes with an Obsidian-like markdown editor."

## V02 Name as published
See "Names as published".

## V03 Name form
Silent

## V04 One thing or several
Silent

## V05 Whom the product sells to
Repository description: "Private & local AI personal knowledge management app for high entropy people." README: "We are always on the lookout for contributors keen on building the future of knowledge management."

## V06 Audience text outside the classes
Repository description: "for high entropy people".

## V07 What the page asks the buyer to do to get it
README: "Download from [reorproject.org](https://reorproject.org) or [releases](https://github.com/reorproject/reor/releases). Mac, Linux & Windows are all supported. 2. Install like a normal App." AlternativeTo: "winget install -e --id ReorProject.Reor".

## V08 Product kind
README: "AI-powered desktop note-taking app". Repository description: "personal knowledge management app".

## V09 Reader only, or also editor
README: "you can edit your notes with an Obsidian-like markdown editor"; "in editor mode, the human can toggle the sidebar to reveal related notes".

## V10 Platforms
README: "Mac, Linux & Windows are all supported." AlternativeTo: "Windows, Mac, Linux".

## V11 Prerequisites
README: "Reor interacts directly with Ollama which means you can download and run models locally right from inside Reor." README (building): "Make sure you have nodejs installed."

## V12 Install and keep current
(a) README: "Install like a normal App."; AlternativeTo: "winget install -e --id ReorProject.Reor"; "git clone https://github.com/reorproject/reor.git / npm install / npm run build". (b) Silent.

## V13 Markdown forms claimed
README: "Obsidian-like markdown editor"; "Note that if you have frontmatter in your markdown files it may not parse correctly."

## V14 Whether files stay local
README: "Everything is stored locally"; "Reor works within a single directory in the filesystem. You choose the directory on first boot."; "The hypothesis of the project is that AI tools for thought should run models locally _by default_."

## V15 Network and data leaving
README: "You can also connect to an OpenAI-compatible API like Oobabooga, Ollama or OpenAI itself!"; "Private & local AI personal knowledge management app" (repository description). Telemetry: silent.

## V16 Price and licence
README: "AGPL-3.0 license. See `LICENSE` for details." AlternativeTo: "Open Source" (AGPL-3.0), "Free product." Repository licence field: "GNU Affero General Public License v3.0". Price in README: silent.

## V17 Cost beyond the price
Silent

## V18 Use at work
Silent

## V19 The unit a buyer takes
README: "Download from reorproject.org or releases."

## V20 The surface the product sells on
Captured pages: AlternativeTo directory page; code repository page. The maker's site is unreachable.

## V21 Distribution channels named
README: "reorproject.org", "releases". AlternativeTo: winget command.

## V22 to V25 (shape dimensions)
Silent beyond the quotes under V07, V12, V16, V21.

## V26 Release cadence and timing
README: "Our team is shipping very quickly right now" (announcement).

## V27 Last release and archived status
Releases (API): "v-0.2.32 2025-04-05T18:33:39Z"; "v0.2.26 2024-10-30T23:20:08Z"; "v0.2.25 2024-10-22T19:41:14Z". Repository: pushed_at "2025-05-13T21:28:59Z" (commit); archived: true. AlternativeTo: "this page was last updated May 23, 2026."; "The GitHub repository section reads "Updated May 13, 2025 (Archived)."" The README still reads "We are now on Discord! Our team is shipping very quickly right now".

## V28 Finding the way around a long document
Silent

## V29 Finding a word
README: "Everything can be searched semantically."; "provides semantic search".

## V30 Links, images and references to other files
README: "it automatically links related notes"; "Related notes are connected automatically via vector similarity."

## V31 Keeping up with a file edited elsewhere
Silent

## V32 Appearance
Silent

## V33 Print, export, send on
Silent

## V34 Help and what happens when it breaks
README: "We are now on Discord!"; "Check out our issues page and the contributing guide".

## V35 Who else uses it
Repository page (API): stargazers_count 8544, forks_count 526. AlternativeTo: "33 likes".

## V36 AI-related claims
README: "AI-powered desktop note-taking app"; "LLM-powered Q&A does RAG on your corpus of notes."; "Every note you write is chunked and embedded into an internal vector database."; "Reor interacts directly with Ollama"; "connect to an OpenAI-compatible API". Repository topics: "ai", "llama", "ollama", "rag".

## V37 Why the product exists
README: "The hypothesis of the project is that AI tools for thought should run models locally _by default_."
