# design.md — E07 段3（权限 deny 关键：settings.json 终端演示）

## orientation

orientation: landscape
orientation_source: category_hint
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏。settings.json 终端窗口（deny 配置高亮 + AI 被拒动画）。E07 防偷改测试核心段——权限层硬性拦截。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。1 场景 6 region（避开 R-R-010 相邻同质误报）。标题 + 终端窗口（deny 配置逐行 reveal + AI 被拒动画）+ 铁律卡 + 金句，按 narration 锚点 reveal 同屏累积。

## style

终端窗口风（VSCode/Mac Terminal）。左侧终端窗口（标题栏红黄绿圆点 + settings.json + JSON 语法高亮 + deny 行金色高亮 + AI 尝试改测试被拒红色 X 动画），右侧铁律卡（框架强制 vs 提示词劝阻）。底部金句收束。

## color_direction

深底终端 + 三色语义（蓝=键名/路径 / 金=deny 高亮 / 红=被拒 X / 绿=铁律强制）：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | `#0F172A` | 深蓝主底（scan_grid 网格叠层） |
| 终端窗 | `#0a0a0a` | 终端深底（Mac Terminal 风） |
| 注释灰 | `#6B7280` | `// .claude/settings.json` 行 |
| 键名蓝 | `#60A5FA` | `permissions` / `deny` |
| 值白 | `#E0E7FF` | JSON 字符串值 |
| deny 高亮 | `#FBBF24` | deny 数组项（金色强调，关键） |
| 被拒红 | `#F87171` | AI 尝试改测试被拒 X |
| 铁律绿 | `#34D399` | 框架强制（不靠自觉） |
| 金句 | `#FBBF24` | 金色（绕不过权限层） |

## immersion_mode

教程横屏 reveal — 1 场景 + 多 region（标题+终端窗+铁律卡+金句）。region 按 data-reveal 时间点淡入 + 方向（标题 fade / 终端窗 top / deny 行逐行 stagger / 被拒 X 弹出 / 铁律卡 left / 金句 top）。

## 视觉区域范式（1 场景，~75s TTS）

### 单场景：权限 deny 硬拦截（6 region 同屏累积）

- **region1 标题**（data-reveal=0，dir=fade）：标题「settings.json · 权限 deny」+ 副「第二层防护 · 框架硬拦截」
- **region2 终端窗-头部**（data-reveal=5，dir=top）：终端窗口 reveal（标题栏红黄绿圆点 + settings.json）+ 头部注释 `// .claude/settings.json`
- **region3 deny 配置逐行**（data-reveal=12，dir=fade）：JSON reveal `permissions` 键 + `deny` 数组 + 3 条 deny 项（Write test 目录 / Edit test 目录 / Write 星 test.ts）逐行金色高亮
- **region4 AI 被拒动画**（data-reveal=32，dir=fade）：终端底部 AI 尝试 `Write test/foo.test.ts` → 红色 X「Permission denied」弹出
- **region5 铁律卡**（data-reveal=48，dir=left）：右侧卡「不靠 AI 自觉 · 靠框架强制」+ 对比（提示词劝阻 vs 权限硬拦截）
- **region6 金句**（data-reveal=62，dir=top）：金句「AI 再聪明 · 也绕不过权限层」

## 动画策略

- deny 配置逐行 reveal（data-reveal-dir=fade，每行 stagger 0.5s）
- AI 被拒 X 弹出（scale 0→1 + 红色闪烁，500ms）
- region fade-in + 方向偏移（left 从 x:-40 / top 从 y:-40 / fade 纯 opacity），500ms
- fx-pulse + fx-blink 静态点缀（禁划过类）

## bg_component

`scan_grid`（深蓝扫描网格，终端 HUD 感，与 E04 claudemd 同款保持合集一致）

## visual_type

`tutorial_deny_terminal`（终端窗口 + JSON deny 高亮 + AI 被拒动画 + 铁律卡布局）
