# shuaiplus/inkstone (slug shuaiplus-inkstone)

Shard-13. Cell condition: rates only for repos with >=200 stars.
Name as published: "Inkstone" (README heading).

## Pages read (all 2026-10-09)

- https://api.github.com/repos/shuaiplus/inkstone : HTTP 200 (repository fields)
- https://api.github.com/repos/shuaiplus/inkstone/readme : HTTP 200 (README text)
- https://api.github.com/repos/shuaiplus/inkstone/releases?per_page=3 : HTTP 200
- https://inkstone-demo.pages.dev/ : HTTP 200 (repository homepage field; script-rendered, 9 characters of text captured, no product text)
- Not read: README_ZH.md, CONTRIBUTING.md, LICENSE

## V01 Eligibility

README: "A self-hosted Markdown notebook for writing, organizing, syncing, and backing up personal knowledge." ; "Notes always remain plain Markdown text" ; Features, Writing: "CodeMirror 6 editor, ... per-group editor/split/preview layouts, synchronized scrolling, outline"

## V02 Name as published

"Inkstone" (README heading; logo alt "Inkstone project logo")

## V03 Name form

"Inkstone" ; "A self-hosted Markdown notebook"

## V04 One thing or several

silent

## V05 Whom the product sells to

README: "Every new account automatically receives two standard starter notes" ; "Public note links with optional access passwords and expiration dates" ; "owner-only update notifications" ; "regular members" (multi-account deployment)

## V06 Audience text outside the classes

"It is a complete self-hosted application. The deployer retains control of the database, attachments, and runtime environment." (README)

## V07 What the page asks the buyer to do to get it

README Deployment: "1. Fork the Inkstone repository to your GitHub account. 2. Open Cloudflare Workers & Pages. 3. Select Continue with GitHub, then choose your forked repository." ; "Demo" link.

## V08 Product kind

"Inkstone is a browser-based notebook that runs on Cloudflare Workers." ; "Installable PWA" (README)

## V09 Reader only, or also editor

"CodeMirror 6 editor" ; "per-group editor/split/preview layouts" (README)

## V10 Platforms

"browser-based notebook that runs on Cloudflare Workers" ; "Desktop and mobile layouts" ; "Installable PWA" (README)

## V11 Prerequisites

README: "Cloudflare D1", "Cloudflare R2 or Workers KV", "Workers KV OAUTH_KV", "SyncHub Durable Object", "CredentialVault Durable Object"; Deployment steps require a GitHub account and Cloudflare Workers & Pages; "Workers AI AI binding: Optional embedding generation for semantic search".

## V12 Install and keep current

README: "Existing databases are upgraded automatically through versioned, idempotent migrations. Keep a current backup before updating any self-hosted deployment. When a newer stable Inkstone release is available, the owner receives a focused reminder without interrupting regular members."

## V13 Markdown forms claimed

README: "GFM tables and task lists, footnotes, Obsidian-style comments, WikiLinks, embeds, block IDs, callouts, details blocks, tabs, math, Mermaid diagrams, PrismJS syntax highlighting, and Front Matter"

## V14 Whether files stay local

README: "Notes always remain plain Markdown text" ; Data storage table: "Cloudflare D1: Accounts, notes, folders, tags, settings, versions..." ; "Browser IndexedDB: Local cache and pending offline writes" ; "It is a complete self-hosted application. The deployer retains control of the database"

## V15 Network and data leaving

README: "offline app launch, browser-side cache, offline write queue" ; "private AI access" ; "Workers AI AI binding: Optional embedding generation for semantic search; unavailable deployments continue to use lexical search" ; "Remote backup targets support WebDAV and S3-compatible storage" ; "Login passwords, active sessions, share passwords, and backup-service credentials are not included in exports."

## V16 Price and licence

README link text: "LGPL-3.0-only". Repository license field (GitHub API): "NOASSERTION". Price: silent.

## V17 Cost beyond the price

README: requires Cloudflare resources (see V11); price of those: silent.

## V18 Use at work

silent

## V19 The unit a buyer takes

README: "Fork the Inkstone repository to your GitHub account."

## V20 The surface the product sells on

Code repository page (README); demo site.

## V21 Distribution channels named

README: "Fork the Inkstone repository to your GitHub account." ; "Cloudflare Workers & Pages" (https://dash.cloudflare.com/?to=/:account/workers-and-pages/create) ; "Demo" (https://inkstone-demo.pages.dev/)

## V22 Shape dimension 1: how the buyer reaches the offering

README Deployment steps 1 to 5 (fork, Cloudflare Workers & Pages, generated Workers URL); "The browser-only demo reuses the same note content"

## V23 Shape dimension 2: paid before reached

silent

## V24 Shape dimension 3: how the sale is taken

silent

## V25 Shape dimension 4: place held

silent

## V26 Release cadence and timing

GitHub API releases: v0.8.0 2026-09-14, v0.7.0 2026-08-31, v0.6.0 2026-08-10. No schedule stated.

## V27 Last release and archived status

GitHub API: latest release "v0.8.0" 2026-09-14; pushed_at 2026-10-07; archived false.

## V28 Finding the way around a long document

README: "outline" ; "synchronized scrolling" ; "focus mode" ; "typewriter mode"

## V29 Finding a word

README: "D1 FTS5 full-text search with Chinese indexing, filters, recent notes, command-palette navigation, and optional private semantic/hybrid search powered by Workers AI"

## V30 Links, images and references

README: "WikiLinks, embeds, block IDs" ; "bidirectional links" ; "Nested folders ... wiki links, backlinks, block references, note embeds, and a relationship graph" ; "Attachment and uploaded-avatar binaries"

## V31 Keeping up with a file edited elsewhere

README: "realtime notifications" ; "multi-device synchronization" ; "conflict copies"

## V32 Appearance

README: "dark/light themes, accent colors, Simplified Chinese, English"

## V33 Print, export, send on

README: "JSON and ZIP exports, directly readable Markdown, attachment export, and manual or scheduled WebDAV/S3 backups" ; "Public note links with optional access passwords and expiration dates"

## V34 Help and what happens when it breaks

README: "Contributing" link (CONTRIBUTING.md); repository issues not named in the README text.

## V35 Who else uses it

Repository stargazers_count 1071 (API field).

## V36 AI-related claims

README: "private AI access" ; "MCP: Private remote MCP, OAuth 2.1 with PKCE, revocable ink_... API keys, standard search/fetch, bounded reads, revision-safe writes, separate trash permission, and per-account grant management" ; "semantic/hybrid search powered by Workers AI". Repository topics: none naming AI.

## V37 Why the product exists

silent
