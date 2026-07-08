# design.md — E05 段4（图谱工具 + 两条铁律：impact 终端演示，核心段）

## orientation

orientation: landscape
orientation_source: category_hint
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏。图谱工具 + 两条铁律：核心组件——impact 终端窗口（爆炸半径分析 + HIGH 风险脉冲）+ 两条铁律金边卡 + 实测数据。E04 install 终端组件范式延续。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。**1 场景 6 region**（scenes=1）。标题 + 三类工具卡 + impact 终端（命令打字 + 输出 fade + HIGH 脉冲）+ 两条铁律卡 + 实测数据，按 narration 锚点 reveal 同屏累积。

## style

impact 工具终端演示风。顶部三类工具卡（理解/变更/查询），中部终端窗口（深底 + 标题栏红黄绿 + 命令逐字打字 + 输出 fade-in + HIGH 红色脉冲），底部两条铁律金边卡 + 实测数据。

## color_direction

深蓝 hex_grid 底 + 终端深底 + 三色工具分类 + HIGH 红 + 金边铁律：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | hex_grid | 六边网格（基础设施结构感） |
| 终端窗 | `#0a0a0a` | 终端深底（macOS 风） |
| 命令蓝 | `#60A5FA` | 蓝（impact 命令） |
| 理解类 | `#3B82F6` | 蓝（context） |
| 变更类 | `#FBBF24` | 金（impact/detect_changes） |
| 查询类 | `#A78BFA` | 紫（Cypher） |
| HIGH 风险 | `#EF4444` | 红（爆炸半径警示） |
| 铁律金边 | `#FBBF24` | 金（两条铁律卡） |
| 蓝白 | `#E0E7FF` | 标题/次要 |

## immersion_mode

教程横屏 reveal — 1 场景 + 多 region（标题+三类工具+终端+铁律+数据）。region 按 data-reveal 时间点淡入 + 方向。

## 视觉区域范式（1 场景，~75s TTS）

### 单场景：图谱工具 + 铁律（6 region 同屏累积）

- **region1 标题**（data-reveal=0，dir=fade）：标题「图谱工具 · 十四件 + 两条铁律」+ 副「impact 算爆炸半径 · 改前必跑」
- **region2 三类工具卡**（data-reveal=4，dir=top）：三类横排——理解类（context 360 度视图）/ 变更类（impact 爆炸半径 + detect_changes）/ 查询类（自由 Cypher）
- **region3 终端-命令**（data-reveal=16，dir=top）：终端窗口 reveal + 命令打字 `$ impact --target UserService.validateToken` + `⚡ 爆炸半径分析中...`
- **region4 终端-输出+HIGH**（data-reveal=24，dir=fade）：输出 fade-in `d=1 直接调用者 12 处` + `d=2 间接影响 47 处` + `风险等级: HIGH ⚠` 红色脉冲
- **region5 两条铁律卡**（data-reveal=34，dir=left）：金边卡——铁律一「改前必跑 impact」/ 铁律二「提交前必跑 detect_changes」
- **region6 实测数据**（data-reveal=48，dir=top）：数据卡「累计排查 144 bug · 覆盖率 80%+」

## 动画策略

- 终端命令逐字打字（GSAP timeline + textContent snap，每字 50ms）
- 终端输出 fade-in（data-reveal 触发，500ms）
- HIGH 红色脉冲（box-shadow 同色系 red pulse，CSS animation 循环态）
- 铁律卡金边脉冲（border-color 微动，CSS animation 循环态）
- region fade-in + 方向偏移，500ms
- fx-pulse + fx-blink 静态点缀（禁划过类）

## bg_component

`hex_grid`（六边网格，基础设施结构感；E05 全集统一 bg）

## visual_type

`tutorial_impact_terminal`（终端窗口 + 三类工具卡 + 铁律金边卡布局）
