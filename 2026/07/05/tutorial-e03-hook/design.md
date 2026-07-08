# design.md — E03 钩子段（转型卡在预算：痛点 + 老板三问 + 立项全套）

## orientation

orientation: landscape
orientation_source: category_hint
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏。钩子：转型最大拦路虎是预算——痛点大字 + 老板三问 + 立项全套 4 胶囊。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。**1 场景 3 region**（scenes=1，避开 R-R-010）。痛点大字 + 老板三问 + 立项全套，按 narration 锚点 reveal 同屏累积。

## style

钩子痛点冲击风。中心大字砸出"卡在预算"，下方老板三问 + 立项全套 4 胶囊预告。

## color_direction

深蓝底 + 三色语义（红=痛点预算卡 / 金=老板三问警觉 / 蓝=立项全套指引）：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | `#0F172A` | 深蓝主底 |
| 痛点预算（卡住） | `#EF4444` | 红色（警示痛点） |
| 老板三问（警觉） | `#FBBF24` | 金色（追问） |
| 立项全套（指引） | `#3B82F6` | 蓝色（方案） |
| 蓝白 | `#E0E7FF` | 标题/次要 |

## immersion_mode

教程横屏 reveal — 1 场景 + 多 region（痛点大字+老板三问+立项全套）。region 按 data-reveal 时间点淡入 + 方向（痛点 fade / 三问 top / 全套 left）。

## 视觉区域范式（1 场景，~30s）

### 单场景：钩子（3 region 同屏累积）

- **region1 痛点大字**（data-reveal=0，dir=fade）：「转型卡在哪？」+ 副「不是技术 · 是预算」（红强调）
- **region2 老板三问**（data-reveal=8，dir=top）：3 问横排（要多少钱 / 多久回本 / 失败怎么办，金色警觉）
- **region3 立项全套**（data-reveal=18，dir=left）：4 胶囊（目标 / 成本 / ROI / 兜底，蓝指引）

## 动画策略

- region fade-in + 方向偏移（left 从 x:-40 / top 从 y:-40 / fade 纯 opacity），500ms
- fx-pulse + fx-blink 静态点缀（禁划过类）

## bg_component

`clean_slate`（单场景简洁底）

## visual_type

`tutorial_hook`（钩子痛点布局）
