# design.md — E04 段2（安装终端：curl install + 智谱 GLM 认证）

## orientation

orientation: landscape
orientation_source: category_hint
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏。安装 Claude Code 全流程：终端窗口 + 命令打字动画 + 智谱 GLM 认证配置。E04 新视觉组件——终端模拟。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。**1 场景 6 region**（scenes=1，避开 R-R-010 相邻同质误报）。标题 + 终端窗口（命令打字+输出）+ 认证卡 + 金句，按 narration 锚点 reveal 同屏累积。

## style

终端实操风。左侧终端窗口（深底 + 标题栏红黄绿圆点 + 等宽字命令逐字打字 + 绿色 ✓ 输出），右侧认证卡（智谱 GLM 国内直连）。底部金句收束。

## color_direction

深底 #0a0a0a 终端 + 三色语义（绿=命令成功 / 蓝=认证智谱 / 金=金句）：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | `#0F172A` | 深蓝主底（scan_grid 网格叠层） |
| 终端窗 | `#0a0a0a` | 终端深底（macOS 风） |
| 命令成功 | `#34D399` | 绿色（✓ installed / 连接成功） |
| 命令蓝 | `#60A5FA` | 蓝色（curl / export / claude 命令） |
| 认证（智谱） | `#A78BFA` | 紫色（GLM 国内直连） |
| 金句 | `#FBBF24` | 金色（一条路走通） |
| 蓝白 | `#E0E7FF` | 标题/次要 |

## immersion_mode

教程横屏 reveal — 1 场景 + 多 region（标题+终端窗+认证卡+金句）。region 按 data-reveal 时间点淡入 + 方向（标题 fade / 终端窗 top / 认证卡 left / 金句 top）。

## 视觉区域范式（1 场景，~75s TTS）

### 单场景：安装 + 认证（6 region 同屏累积）

- **region1 标题**（data-reveal=0，dir=fade）：标题「安装 Claude Code」+ 副「一行命令 · 终端原生 · 智谱直连」
- **region2 终端窗-安装**（data-reveal=5，dir=top）：终端窗口（标题栏红黄绿 + Terminal — bash）+ 命令1 打字 `curl -fsSL https://claude.ai/install.sh | bash` + 输出 `✓ Claude Code installed`
- **region3 认证卡**（data-reveal=16，dir=left）：认证卡「智谱 GLM · 国内直连」+ 副注「注册 → 创建 API Key」+ 免费额度练手
- **region4 终端窗-配置**（data-reveal=26，dir=fade）：终端命令2 打字 `export ANTHROPIC_BASE_URL=https://open.bigmodel.cn/api/anthropic` + 命令3 打字 `export ANTHROPIC_AUTH_TOKEN=你的Key`
- **region5 终端窗-启动**（data-reveal=42，dir=fade）：命令4 打字 `claude` + 输出框 `╭─ ✓ 已连接 GLM · 开始用 ╮`
- **region6 金句**（data-reveal=55，dir=top）：金句「只讲 GLM 一条路 · 一条路走通胜过十条路摆在面前」

## 动画策略

- 终端命令逐字打字（GSAP timeline + textContent snap，每字 50ms）
- 命令输出 fade-in（data-reveal 触发，500ms）
- region fade-in + 方向偏移（left 从 x:-40 / top 从 y:-40 / fade 纯 opacity），500ms
- fx-pulse + fx-blink 静态点缀（禁划过类）

## bg_component

`scan_grid`（深蓝扫描网格，终端 HUD 监控感）

## visual_type

`tutorial_install_terminal`（终端窗口 + 命令打字 + 认证卡布局）
