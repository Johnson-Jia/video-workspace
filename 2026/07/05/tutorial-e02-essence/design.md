# design.md — E02 原理①段（AI 到底是什么：弱/强 AI + 两流派 + 图灵测试）

## orientation

orientation: landscape
orientation_source: category_hint
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏。原理一：AI 本质——弱 AI vs 强 AI / 两大流派 / 图灵测试。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。**1 场景 4 region**（scenes=1，避开 R-R-010 相邻同质误报）。标题 + 弱/强对比 + 两流派 + 图灵测试，按 narration 锚点 reveal 同屏累积。

## style

原理科普对比风。清晰、对称——弱/强 AI 双列对比（左弱右强）+ 两流派横排（旧淘汰/新主流）+ 图灵测试收束。

## color_direction

深蓝底 + 三色语义（蓝=弱AI当前 / 紫=强AI理论 / 绿=主流神经网络 / 灰=已淘汰符号）：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | `#0F172A` | 深蓝主底 |
| 弱 AI（当前所有） | `#3B82F6` | 蓝色（当下主流） |
| 强 AI（AGI 理论） | `#A78BFA` | 紫色（未来/理论） |
| 神经网络（主流） | `#10B981` | 绿色（正向主流） |
| 符号推理（已淘汰） | `#94A3B8` | 灰色（过时） |
| 蓝白 | `#E0E7FF` | 标题/次要 |

## immersion_mode

教程横屏 reveal — 1 场景 + 多 region（标题+弱强对比+两流派+图灵测试）。region 按 data-reveal 时间点淡入 + 方向（标题 fade / 弱强 left / 流派 left / 图灵 top）。

## 视觉区域范式（1 场景，~80s）

### 单场景：原理①（4 region 同屏累积）

- **region1 标题**（data-reveal=0，dir=fade）：原理编号「原理 ①」+ 标题「AI 到底是什么」fade-in
- **region2 弱/强对比**（data-reveal=8，dir=left）：弱 AI（蓝，当前所有/特定任务）vs 强 AI（紫，AGI/理论）
- **region3 两流派**（data-reveal=28，dir=left）：符号推理（灰，已淘汰）/ 神经网络（绿，当前主流·大模型）
- **region4 图灵测试**（data-reveal=50，dir=top）：图灵测试 + 注解「通过≠真有智能，可能只是模仿」

## 动画策略

- region fade-in + 方向偏移（left 从 x:-40 / top 从 y:-40 / fade 纯 opacity），500ms
- 弱强对比纵向均衡布局
- fx-pulse + fx-blink 静态点缀（禁划过类）

## bg_component

`clean_slate`（单场景简洁底）

## visual_type

`tutorial_essence`（原理对比布局）
