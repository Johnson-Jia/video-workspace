# design.md — E04 段3（CLAUDE.md 代码块：规范资产化）

## orientation

orientation: landscape
orientation_source: category_hint
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏。CLAUDE.md 文件窗口 + 代码块逐行 reveal（语法高亮）+ 资产化卡 + 金句。E04 新视觉组件——代码编辑器模拟。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。**1 场景 6 region**（scenes=1，避开 R-R-010 相邻同质误报）。标题 + 文件窗口（代码块逐行 reveal）+ 资产化卡 + 金句，按 narration 锚点 reveal 同屏累积。

## style

代码编辑器风。左侧文件窗口（标题栏 📄 CLAUDE.md + 代码块等宽字 + 语法高亮：注释灰/键蓝/值白），右侧资产化卡（人定规矩→AI 自动执行）。底部金句收束。

## color_direction

深底代码编辑器 + 三色语义（蓝=技术栈/命令 / 绿=测试/规范 / 金=金句资产化）：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | `#0F172A` | 深蓝主底（scan_grid 网格叠层） |
| 代码窗 | `#0a0a0a` | 代码编辑器深底（VSCode 风） |
| 注释灰 | `#6B7280` | `# 项目规范` 行 |
| 键名蓝 | `#60A5FA` | `- 技术栈` / `- 命名` |
| 值白 | `#E0E7FF` | `React + TypeScript + Vite` |
| 资产化 | `#34D399` | 绿色（人定规矩 AI 执行） |
| 金句 | `#FBBF24` | 金色（硬约束） |
| Git 共享 | `#A78BFA` | 紫色（提交进 Git 团队共享） |

## immersion_mode

教程横屏 reveal — 1 场景 + 多 region（标题+文件窗+资产化卡+金句）。region 按 data-reveal 时间点淡入 + 方向（标题 fade / 文件窗 top / 代码行逐行 stagger / 资产化卡 left / 金句 top）。

## 视觉区域范式（1 场景，~78s TTS）

### 单场景：CLAUDE.md 资产化（6 region 同屏累积）

- **region1 标题**（data-reveal=0，dir=fade）：标题「CLAUDE.md · 规范资产化」+ 副「项目根目录 · AI 每次自动读」
- **region2 文件窗-头部**（data-reveal=6，dir=top）：文件窗口 reveal（标题栏 📄 CLAUDE.md）+ 代码块头行 `# 项目规范`（注释灰）
- **region3 代码块-技术栈/命名**（data-reveal=14，dir=fade）：代码块 reveal `- 技术栈：React + TypeScript + Vite` + `- 命名：组件 PascalCase · 工具 camelCase`
- **region4 代码块-测试/提交**（data-reveal=30，dir=fade）：代码块 reveal `- 测试：改动必跑 npm test` + `- 提交：约定式 feat/fix/docs`
- **region5 资产化卡**（data-reveal=46，dir=left）：右侧卡「人定规矩 → AI 自动执行」+ Git 共享注「提交进 Git · 全团队共享 · 新人 AI 帮守规矩」
- **region6 金句**（data-reveal=60，dir=top）：金句「规范不是文档里落灰的字 · 是 AI 每次生成都遵守的硬约束」

## 动画策略

- 代码块逐行 reveal（data-reveal-dir=top，每行 stagger 0.4s）
- region fade-in + 方向偏移（left 从 x:-40 / top 从 y:-40 / fade 纯 opacity），500ms
- fx-pulse + fx-blink 静态点缀（禁划过类）

## bg_component

`scan_grid`（深蓝扫描网格，代码编辑器 HUD 感）

## visual_type

`tutorial_claudemd_codeblock`（文件窗口 + 代码块语法高亮 + 资产化卡布局）
