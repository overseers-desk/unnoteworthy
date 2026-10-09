# rotbit-xedit: verbatim profile

Cell: github-topics:markdown-editor (weight 1). Condition obeyed: rates only for repos with >=200 stars. The text is published in Chinese; quotes are the original, with no rendering added.

## Names as published
- Repository: "rotbit/xedit"; README heading: "xEdit"; site title: "xEdit · Markdown 公众号排版工具｜Markdown 公众号编辑器，AI 审核，一键发布"

## Pages read (all captured 2026-10-09)
- https://github.com/rotbit/xedit : HTTP 200
- https://api.github.com/repos/rotbit/xedit and .../releases (via gh) : success; no releases listed
- https://raw.githubusercontent.com/rotbit/xedit/main/README.md : HTTP 200
- https://xedit.me : HTTP 200 (landing page only; changelog, FAQ and Mac client pages not read)

## V01 Eligibility
README: "**Markdown 公众号排版工具 —— 左边写 Markdown，右边就是公众号里的样子，一键复制，样式不丢。**" Repository description: "Markdown 公众号排版工具：左边写 Markdown，右边实时预览，一键复制到微信公众号/知乎，样式全部内联不丢失。13 套主题、数学公式、图床、版本回滚、AI 内容审查，内置 MCP Server。"

## V02 Name as published
See "Names as published".

## V03 Name form
Silent

## V04 One thing or several
Site nav: "编辑器 主题 AI 审核 一键发布 Mac 版 更新日志 常见问题"; site: "获取 Mac 客户端". README: "在线体验", "部署教程", "MCP 接入", "飞书导入".

## V05 Whom the product sells to
README: "微信公众号后台的编辑器会丢掉 `<style>`、`class` 和伪元素，导致大多数「排版工具」粘贴过去就散架。" Site: "Markdown 微信公众号编辑器与排版工具"; theme tags such as "技术 · 深度长文", "职场 · 生活", "程序员 · 夜读", "女性 · 生活" (site).

## V06 Audience text outside the classes
Silent

## V07 What the page asks the buyer to do to get it
Site buttons: "开始写作", "获取 Mac 客户端"; "不用注册，打开就写；文章先存在这台设备，登录后自动同步到云端". README: "在线体验", "git clone https://github.com/rotbit/xedit.git", "打开 <http://localhost:3000> 即可。"

## V08 Product kind
Site: "Markdown 微信公众号编辑器与排版工具"; "网页版一键复制"; "Mac 客户端直接发送到公众号草稿箱". README: "仓库自带 `Dockerfile`"; "内置 MCP 服务端".

## V09 Reader only, or also editor
README: "双模编辑：类 Obsidian 的 Live Preview ... 或左右分栏对照，随时切换"; "CodeMirror 6 编辑器".

## V10 Platforms
Site: "获取 Mac 客户端"; "网页版" (web). README: "全部排版、预览、复制、导出功能都在浏览器里跑". README quick start: "brew install postgresql@17 ... （macOS 示例，其他平台装好 PostgreSQL 即可）".

## V11 Prerequisites
README (self-hosting): "前置依赖：**Node.js 20+**、**PostgreSQL 14+**。" README: "不配置 GitHub/Google OAuth 与 OSS 也能跑——登录用邮箱密码注册即可". README on WeChat login: "**需企业主体开放平台账号**".

## V12 Install and keep current
(a) README quick start: "npm install", "createdb xedit", "npx prisma migrate dev", "npm run dev"; "完整步骤见 **[部署教程](./docs/deployment.md)**，涵盖 Docker / Docker Compose、Dokploy 一键部署、域名与 HTTPS、生产环境 OAuth 配置和升级回滚". (b) Silent.

## V13 Markdown forms claimed
README: "**数学公式**：`$行内$` 与 `$$块级$$`，MathJax 渲染成 SVG 再复制"; "**外链转脚注**"; "脚注、行内公式，表格里回车和 Tab 都顺手" (site); "markdown-it" in the tech stack list. Diagrams, task lists: silent.

## V14 Whether files stay local
README: "不登录也能用：全部排版、预览、复制、导出功能都在浏览器里跑，文稿存本地。登录之后才有云端同步、版本历史和图床。"; "**本地优先**：断网照写，改动落本地镜像，联网自动补同步".

## V15 Network and data leaving
README: "登录之后才有云端同步、版本历史和图床。"; "图片上传经 `/api/upload` 中转，OSS AccessKey 不会下发到浏览器；用户填的 AI 平台 Key 经 AES-256-GCM 加密后入库"; "**飞书知识库导入**"; "AI 内容审查 ... 自带 Key，支持 Replicate / Kimi / GLM / DeepSeek".

## V16 Price and licence
Site: "免费"; "0 元 全部排版功能". Site: "会员现在全网最低价" appears only as sample text inside a demo. README: "[MIT](./LICENSE) © rotbit". Repository licence field: MIT.

## V17 Cost beyond the price
README: "`REPLICATE_API_TOKEN` ... 费用由站点账户承担"; "阿里云 OSS 图床"; "自带 Key".

## V18 Use at work
Silent

## V19 The unit a buyer takes
Silent

## V20 The surface the product sells on
Captured pages: code repository page; maker's own website (web app landing page).

## V21 Distribution channels named
Site: "获取 Mac 客户端"; "网页版". README: "Docker / Docker Compose、Dokploy 一键部署".

## V22 to V25 (shape dimensions)
Silent beyond the quotes under V07, V12, V16, V21. README: "每账号素材存储配额（MB），默认 10240（10GB）" (`DEFAULT_STORAGE_QUOTA_MB`).

## V26 Release cadence and timing
Silent

## V27 Last release and archived status
Repository: pushed_at "2026-10-09T08:16:32Z" (commit); archived: false; releases API returned none. Site nav: "更新日志" (not read).

## V28 Finding the way around a long document
README: "大纲面板"; "双向同步滚动"; "多级分类树". Site: "标题折叠".

## V29 Finding a word
README: "全局搜索" (article management).

## V30 Links, images and references to other files
README: "**外链转脚注**：公众号正文不允许外链，自动转成「文字[n]」+ 文末参考链接，可开关"; "**图床**：截图粘贴、文件拖入自动上传到你自己的阿里云 OSS 并就地插入".

## V31 Keeping up with a file edited elsewhere
README: "左边写 Markdown，右边实时预览" (preview follows the product's own editing). External changes: silent.

## V32 Appearance
README: "**13 套排版主题**"; "**6 套代码配色** + Mac 风格窗口装饰"; "**自定义 CSS**"; "手机预览模式". Site: "亮色 / 暗色两套界面".

## V33 Print, export, send on
README: "**导出**：Markdown / 独立 HTML / 打印版 PDF / 整篇长图 PNG"; "**一键复制**：公众号模式 ... 与知乎模式". Site: "也能复制到知乎，或导出 Markdown、HTML、PDF、长图、Word"; "点「发送到公众号」".

## V34 Help and what happens when it breaks
README: "欢迎 Issue 与 PR。"; links "部署教程", "MCP 接入". Site nav: "常见问题".

## V35 Who else uses it
Repository page (API): stargazers_count 205, forks_count 2.

## V36 AI-related claims
README: "**AI**: **公众号内容审查** ... 自带 Key，支持 Replicate / Kimi / GLM / DeepSeek"; "**MCP Server**：内置 MCP 服务端与自建 OAuth 2.1 授权，Claude Desktop、Cursor 等客户端授权后可直接列出、检索、新建、改写你的文章与图床". Site: "标题和正文原样使用你写的内容，不经 AI 改写"; "AI 内容审核 内测中".

## V37 Why the product exists
README: "微信公众号后台的编辑器会丢掉 `<style>`、`class` 和伪元素，导致大多数「排版工具」粘贴过去就散架。xEdit 在复制的那一刻把主题样式**逐条内联**到每个标签上".
