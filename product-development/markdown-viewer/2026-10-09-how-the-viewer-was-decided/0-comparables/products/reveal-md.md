# reveal-md: verbatim profile

Cell: homebrew:formula (weight 1). Condition obeyed: description-word census; installs as published (opt-out analytics), not users.

## Names as published
- Formula page: "reveal-md"; README heading: "reveal-md"; repository "webpro/reveal-md"

## Pages read (all captured 2026-10-09)
- https://formulae.brew.sh/formula/reveal-md : HTTP 200
- https://formulae.brew.sh/api/formula/reveal-md.json : HTTP 200
- https://github.com/webpro/reveal-md : HTTP 200 (the formula's homepage link)
- https://api.github.com/repos/webpro/reveal-md and .../releases (via gh) : success
- https://raw.githubusercontent.com/webpro/reveal-md/main/README.md : HTTP 200 (about 14 KB; opening, installation, usage, live reload, print, static website and license passages read)

## V01 Eligibility
Formula page: "Get beautiful reveal.js presentations from your Markdown files". README: "reveal.js on steroids! Get beautiful reveal.js presentations from Markdown files." and "This starts a local server and opens any Markdown file as a reveal.js presentation in the default browser."

## V02 Name as published
See "Names as published".

## V03 Name form
Silent

## V04 One thing or several
README: "Scripts, Preprocessors and Plugins"; "Related Projects & Alternatives".

## V05 Whom the product sells to
Silent

## V06 Audience text outside the classes
Silent

## V07 What the page asks the buyer to do to get it
Formula page: "Install command: brew install reveal-md". README: "npm install -g reveal-md"; "reveal-md slides.md"; "docker run --rm -p 1948:1948 -v <path-to-your-slides>:/slides webpronl/reveal-md:latest".

## V08 Product kind
README: "This starts a local server and opens any Markdown file as a reveal.js presentation in the default browser."; command-line usage "reveal-md slides.md". Formula: dependency "node".

## V09 Reader only, or also editor
Silent as to editing. README: "Live Reload: Using `-w` option changes to markdown files will trigger the browser to reload".

## V10 Platforms
Formula page: "Bottle (binary package) installation support provided for: macOS on Apple Silicon ... Linux ARM64". README: "You can use Docker to run this tool without needing Node.js installed on your machine."

## V11 Prerequisites
Formula API: dependencies ["node"]. README: "npm install -g reveal-md"; "You can use Docker to run this tool without needing Node.js installed on your machine." README (print): "The PDF is generated using Puppeteer."

## V12 Install and keep current
(a) Formula: "brew install reveal-md"; README: "npm install -g reveal-md"; Docker image "webpronl/reveal-md:latest". (b) Silent.

## V13 Markdown forms claimed
README: "Markdown: The Markdown feature of reveal.js is awesome, and has an easy (and configurable) syntax to separate slides. Use three dashes surrounded by two blank lines"; "Syntax highlighting ```js"; "Highlight some lines"; "YAML Front matter"; "Speaker Notes"; "Note: speaker notes FTW!"

## V14 Whether files stay local
README: "This starts a local server". Statement about files: silent.

## V15 Network and data leaving
Silent

## V16 Price and licence
Formula page: "License: MIT". Repository licence field: "MIT License". Price: silent.

## V17 Cost beyond the price
Silent

## V18 Use at work
Silent

## V19 The unit a buyer takes
Formula: version "6.1.4" (API stable).

## V20 The surface the product sells on
Captured pages: package registry page (Homebrew formula); code repository page.

## V21 Distribution channels named
Formula: "Homebrew". README: "npm", "Docker" (webpronl/reveal-md).

## V22 to V25 (shape dimensions)
Silent beyond the quotes under V07, V12, V16, V21.

## V26 Release cadence and timing
README: "reveal-md is no longer in active development. No new features will be added. Pull requests for bug and documentation fixes will be considered. Occasional dependency upgrades and CVEs might happen."

## V27 Last release and archived status
Formula API: stable "6.1.4". Releases (API): "6.1.4 2024-11-27T04:40:57Z"; "6.1.3 2024-08-31T13:57:17Z"; "6.1.2 2024-05-20T06:43:32Z". Repository: pushed_at "2026-02-14T03:48:51Z" (commit); archived: true. README: "> [!WARNING] reveal-md is no longer in active development."

## V28 Finding the way around a long document
Silent

## V29 Finding a word
Silent

## V30 Links, images and references to other files
README (static website): "This should copy images along with the slides. Use `--static-dirs` to copy directories with other static assets".

## V31 Keeping up with a file edited elsewhere
README: "Live Reload: Using `-w` option changes to markdown files will trigger the browser to reload and thus display the changed presentation without the user having to reload the browser." (`reveal-md slides.md -w`)

## V32 Appearance
README: "Theme"; "Highlight Theme"; "Custom CSS"; "Custom Template".

## V33 Print, export, send on
README: "Print to PDF: reveal-md slides.md --print slides.pdf"; "The PDF is generated using Puppeteer."; "Static Website: This will export the provided Markdown file into a stand-alone HTML website including scripts and stylesheets."

## V34 Help and what happens when it breaks
README: "Pull requests for bug and documentation fixes will be considered."; "Thanks for using reveal-md! Please consider these Markdown-based alternatives: MkSlides (successor to reveal-md); Slidev".

## V35 Who else uses it
Formula page analytics (Homebrew opt-out, as published): API "30d 1; 90d 37; 365d 220". Repository page (API): stargazers_count 3912, forks_count 414.

## V36 AI-related claims
Silent

## V37 Why the product exists
Silent
