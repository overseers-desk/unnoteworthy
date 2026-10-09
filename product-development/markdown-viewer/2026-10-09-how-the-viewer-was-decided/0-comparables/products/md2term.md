# md2term

Names as published: "md2term" (apt package name; Codeberg heading).
Cell obeyed: debian:apt-cache search markdown, named "Ubuntu 25.04 archive": no installs or recency figure drawn. Weight 1.

Pages read (all 2026-10-09):
- `apt-cache show md2term` run on the Ubuntu 25.04 (plucky) host | exit success; output quoted below (not an HTTP page)
- https://packages.ubuntu.com/plucky/md2term | HTTP 200 but the page is an error page: "two or more packages specified (md2term plucky)"; no package content (treated as unreachable for package content)
- https://packages.ubuntu.com/search?keywords=md2term&searchon=names&suite=plucky&section=all | HTTP 200; suite list on it names jammy, noble, questing, resolute, stonking and no plucky; no package content
- https://codeberg.org/blau_araujo/md2term | HTTP 200 (the Homepage field of the package)
- https://codeberg.org/blau_araujo/md2term/raw/branch/main/README.md | HTTP 200

## V02 Name as published

"Package: md2term" (apt-cache show md2term); "# md2term" (README).

## V03 Name form

"Description-en: Markdown parser for highlights and colors in terminal" (apt-cache); "Parser de markdown para destaques e cores do terminal." (README, Portuguese)

## V04 One thing or several

silent

## V05 Whom the product sells to

silent

## V06 Audience text outside the classes

"md2term was created to be a markdown parser for short texts (less than 30 lines) that could be used in terminal presentations (text slides) and, at the same time, able to be correctly visualized by other parsers on websites (GitHub, GitLab, etc). The script can also be used satisfactorily for viewing other markdown text, provided its limitations are observed."

## V07 What the page asks the buyer to do to get it

README (Portuguese): "Clone o repositório: git clone https://codeberg.org/blau_araujo/md2term ... execute o `make`: sudo make install". apt: "Filename: pool/universe/m/md2term/md2term_0.0.7-2_all.deb".

## V08 Product kind

"The script can also be used satisfactorily for viewing other markdown text" (apt-cache description); "O `md2term` foi criado para ser um parser de markdown" (README).

## V09 Reader only, or also editor

silent

## V10 Platforms

apt-cache: "Architecture: all"; "Origin: Ubuntu". README: "Dependências - Bash - [Pandoc](https://pandoc.org/)".

## V11 Prerequisites

apt-cache: "Depends: less, libhtml-parser-perl, pandoc". README: "## Dependências - Bash - [Pandoc]".

## V12 Install and keep current

apt-cache: "Version: 0.0.7-2", "Filename: pool/universe/m/md2term/md2term_0.0.7-2_all.deb". README: "Clone o repositório: git clone https://codeberg.org/blau_araujo/md2term / Entre no diretório `md2term` que foi criado e execute o `make`: sudo make install"; "Para desinstalar: sudo make uninstall".

## V13 Markdown forms claimed

README "Marcações válidas": "`**TEXTO**` ou `__TEXTO__` | NEGRITO", "`~~TEXTO~~` | RISCADO", "`[RÓTULO](URL)` | RÓTULO"; "capazes de serem visualizados corretamente por outros parsers em sites na web (GitHub, GitLab, etc)"; "é uma marcação válida do markdown GFM". "## Limitações - Não interpreta listas aninhadas (sub-itens) corretamente."

## V14 Whether files stay local

silent

## V15 Network and data leaving

silent

## V16 Price and licence

README: "Licença GPLv3+: GNU GPL versão 3 ou posterior ... Este é um software livre". Price: silent.

## V17 Cost beyond the price

silent

## V18 Use at work

silent

## V19 The unit a buyer takes

silent

## V20 The surface the product sells on

silent

## V21 Distribution channels named

apt-cache: "Section: universe/text", "Origin: Ubuntu", "Bugs: https://bugs.launchpad.net/ubuntu/+filebug", "Homepage: https://codeberg.org/blau_araujo/md2term"; README Codeberg clone address.

## V22 Shape dimension 1: how the buyer reaches the offering

README clone-and-make instructions (see V12); apt-cache package listing.

## V23 Shape dimension 2: whether anything is paid before it is reached

silent

## V24 Shape dimension 3: how the sale is taken

silent

## V25 Shape dimension 4: whether and how a place is held

silent

## V26 Release cadence and timing

silent

## V27 Last release and archived status

apt-cache: "Version: 0.0.7-2". README: "Copyright (C) 2022 Blau Araujo". Codeberg page: "32 commits", "1 branch", "2 tags". Archived banner: silent.

## V28 Finding the way around a long document

silent

## V29 Finding a word

silent

## V30 Links, images and references to other files

README: "Links são apenas representações visuais utilizando o rótulo da marcação (não a URL)."

## V31 Keeping up with a file edited elsewhere

silent

## V32 Appearance

README option: "-s ARQUIVO Esquema de cores alternativo."

## V33 Print, export, send on

silent

## V34 Help and what happens when it breaks

apt-cache: "Bugs: https://bugs.launchpad.net/ubuntu/+filebug". Codeberg page tabs "Issues 1", "Pull requests 1", "Wiki".

## V35 Who else uses it

Codeberg page: "Watch 2", "Star 4", "Fork ... 3".

## V36 AI-related claims

silent

## V37 Why the product exists

silent
