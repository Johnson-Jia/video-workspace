# design.md — E02 介绍段（本集地图：思想转变 + 5 条原理）

## orientation

orientation: landscape
orientation_source: category_hint
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏。本集地图两栏（思想转变 | 5 原理）+ 结论行，一屏多区域 reveal。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。**1 场景 4 region**（scenes=1，避开 R-R-010 相邻同质误报）。标题 + 左栏 + 右栏 + 结论，按 narration 锚点 reveal 同屏累积。

## style

地图概览科技风。清晰、对称——两栏对比布局（思想转变 vs 5 原理）+ 底部结论行收束。教程重结构清晰。

## color_direction

深蓝底 + 双栏语义色（左金=思想转变 / 右蓝=原理）：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | `#0F172A` | 深蓝主底 |
| 左栏（思想转变） | `#FBBF24` | 金色（呼应钩子反常识冲击） |
| 右栏（5 原理） | `#3B82F6` | 蓝色（理性原理） |
| 结论 | `#10B981` | 绿色（= 精准交互，正向收束） |
| 蓝白 | `#E0E7FF` | 标题/次要 |

## immersion_mode

教程横屏 reveal — 1 场景 + tut-grid 两栏布局 + 结论行。region 按 data-reveal 时间点淡入 + 方向（左栏 left / 右栏 left / 结论 top）。

## 视觉区域范式（1 场景，~30s）

### 单场景：本集地图（4 region 同屏累积）

- **region1 标题**（data-reveal=0）：「这集讲什么」+ 副标题「思想转变 + 5 条 AI 原理」fade-in
- **region2 左栏**（data-reveal=5，dir=left）：「思想转变」金色栏头 + 两条要点（避开两个极端 / 拥抱+验证）
- **region3 右栏**（data-reveal=12，dir=left）：「5 条 AI 原理」蓝色栏头 + 五原理列表（token/上下文/Agent/REACT/精准）
- **region4 结论**（data-reveal=22，dir=top）：底部「思想转变 + 懂原理 = 精准交互」绿色结论行

## 动画策略

- region fade-in + 方向偏移（left 从 x:-40 / top 从 y:-40），500ms
- 双栏对称布局（水平均衡，禁偏右）
- fx-pulse + fx-blink 静态点缀（禁划过类）

## bg_component

`clean_slate`（单场景简洁底）

## visual_type

`tutorial_map`（本集结构地图）
