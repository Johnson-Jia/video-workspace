# design.md — E03 段1 目标量化（阶梯 10/20/50 + 目标前置）

## orientation

orientation: landscape
orientation_source: category_hint
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏。段1：目标量化——阶梯目标卡（1月 10-20% / 2月 20-30% / 3月 +50%）+ 注解 + 金句「目标前置」。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。**1 场景 4 region**（scenes=1，避开 R-R-010）。标题 + 阶梯卡 count-up + 注解 + 金句。

## style

目标阶梯进阶风。3 阶阶梯卡横排（递进色：蓝→青→金），数字 count-up 飞升，下方注解 + 金句收束。

## color_direction

深蓝底 + 三色进阶（蓝=适应期 1 月 / 青=扩展期 2 月 / 金=目标期 3 月）：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | `#0F172A` | 深蓝主底 |
| 1 月适应期 | `#3B82F6` | 蓝色（起步） |
| 2 月扩展期 | `#06B6D4` | 青色（进阶） |
| 3 月目标期 | `#FBBF24` | 金色（目标） |
| 金句（正向） | `#10B981` | 绿色（承诺） |
| 蓝白 | `#E0E7FF` | 标题/次要 |

## immersion_mode

教程横屏 reveal — 1 场景 + 多 region（标题+阶梯卡+注解+金句）。region 按 data-reveal 时间点淡入 + 方向（标题 fade / 阶梯卡 left / 注解 top / 金句 fade）。阶梯卡数字 count-up（data-count-to 10/20/50，data-count-at 略晚于 reveal）。

## 视觉区域范式（1 场景，~80s）

### 单场景：目标量化（4 region 同屏累积）

- **region1 标题**（data-reveal=0，dir=fade）：「目标量化 · 让提效可衡量」
- **region2 阶梯卡**（data-reveal=6，dir=left）：3 阶（1 月 10-20% 蓝 / 2 月 20-30% 青 / 3 月 +50% 金），数字 count-up
- **region3 注解**（data-reveal=38，dir=top）：「+50% 是启动承诺目标 · 实际靠度量」
- **region4 金句**（data-reveal=48，dir=fade）：「目标要前置 · 公开承诺」（绿）

## 动画策略

- region fade-in + 方向偏移（left 从 x:-40 / top 从 y:-40 / fade 纯 opacity），500ms
- 阶梯卡数字 count-up（data-count-to + data-count-at）
- fx-pulse + fx-blink 静态点缀（禁划过类）

## bg_component

`clean_slate`（单场景简洁底）

## visual_type

`tutorial_goal`（阶梯目标布局）
