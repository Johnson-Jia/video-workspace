# design.md — E03 介绍段（Leader 主战场：战略启动 4 件事，前两件高亮）

## orientation

orientation: landscape
orientation_source: category_hint
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏。介绍：战略启动 4 件事（目标量化/路线图/组织保障/风险预案），本集讲前两件高亮。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。**1 场景 3 region**（scenes=1，避开 R-R-010）。标题 + 4 卡 grid（前两件高亮）+ 本集范围标注。

## style

介绍地图风。4 卡横排（2×2 或 4 列），前两件金边高亮（本集讲），后两件暗（下集预告）。

## color_direction

深蓝底 + 三色语义（金=本集高亮 / 蓝=导航战略 / 灰=下集预告）：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | `#0F172A` | 深蓝主底 |
| 本集高亮（前两件） | `#FBBF24` | 金色（强调本集） |
| 战略导航 | `#3B82F6` | 蓝色（战略主轴） |
| 下集预告（后两件） | `#94A3B8` | 灰色（暗淡） |
| 蓝白 | `#E0E7FF` | 标题/次要 |

## immersion_mode

教程横屏 reveal — 1 场景 + 多 region（标题+4 卡+范围标注）。region 按 data-reveal 时间点淡入 + 方向（标题 fade / 4 卡 left / 范围 fade）。

## 视觉区域范式（1 场景，~30s）

### 单场景：介绍（3 region 同屏累积）

- **region1 标题**（data-reveal=0，dir=fade）：「Leader 主战场 · 战略启动」+ 副「四件事齐备才叫启动」
- **region2 4 卡 grid**（data-reveal=6，dir=left）：4 卡（目标量化✓金 / 路线图✓金 / 组织保障·下集灰 / 风险预案·下集灰）
- **region3 本集范围**（data-reveal=18，dir=fade）：「这集拆前两件 · 目标量化 + 预算 ROI」

## 动画策略

- region fade-in + 方向偏移（left 从 x:-40 / fade 纯 opacity），500ms
- 4 卡前两件金边高亮 + 后两件灰暗
- fx-pulse + fx-blink 静态点缀（禁划过类）

## bg_component

`clean_slate`（单场景简洁底）

## visual_type

`tutorial_intro`（介绍地图布局）
