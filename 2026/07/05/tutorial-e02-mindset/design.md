# design.md — E02 思想转变段（两个极端 + 拥抱验证）

## orientation

orientation: landscape
orientation_source: category_hint
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏。转型中最容易栽的两个坑（两个极端）+ 正确姿态收束。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。**1 场景 5 region**（scenes=1，避开 R-R-010 相邻同质误报）。标题 + 左卡 + 右卡 + 金句 + 转折，按 narration 锚点 reveal 同屏累积。

## style

思想转变对比风。清晰、对称——左右双卡红边框（两个极端的代价）+ 中部金句绿边框收束（拥抱+验证）+ 底部转折蓝（引出原理）。

## color_direction

深蓝底 + 三色语义（红=两个极端的代价 / 绿=正确姿态 / 蓝=引出原理）：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | `#0F172A` | 深蓝主底 |
| 左/右卡（两个极端） | `#EF4444` | 红色（错误姿态的代价） |
| 金句（拥抱+验证） | `#10B981` | 绿色（正确姿态，正向收束） |
| 转折（引出原理） | `#3B82F6` | 蓝色（理性原理） |
| 蓝白 | `#E0E7FF` | 标题/次要 |

## immersion_mode

教程横屏 reveal — 1 场景 + 多 region（标题+双卡+金句+转折）。region 按 data-reveal 时间点淡入 + 方向（标题 fade / 双卡 left / 金句 top / 转折 fade）。

## 视觉区域范式（1 场景，~90s）

### 单场景：思想转变（5 region 同屏累积）

- **region1 标题**（data-reveal=0，dir=fade）：「两个极端 · 都要避免」fade-in
- **region2 左卡**（data-reveal=6，dir=left）：「抗拒 AI」红边框 + 表现（觉得噱头/怕替代）+ 代价（被会用的人替代）
- **region3 右卡**（data-reveal=18，dir=left）：「盲目崇拜」红边框 + 表现（万能/全盘交付）+ 代价（产出不可控）
- **region4 金句**（data-reveal=32，dir=top）：「拥抱 + 验证」绿边框 + 「信任但验证」+ 「当资深实习生」
- **region5 转折**（data-reveal=50，dir=fade）：「光有态度不够 → 要懂原理」（引出后半段）

## 动画策略

- region fade-in + 方向偏移（left 从 x:-40 / top 从 y:-40 / fade 纯 opacity），500ms
- 左右双卡对称布局（水平均衡，禁偏右）
- fx-pulse + fx-blink 静态点缀（禁划过类）

## bg_component

`clean_slate`（单场景简洁底）

## visual_type

`tutorial_mindset`（思想转变对比布局）
