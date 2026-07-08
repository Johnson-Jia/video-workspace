# design.md — E03 段4 失败预案（止损线 / 回退 / 复盘 + 可止损金句）

## orientation

orientation: landscape
orientation_source: category_hint
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏。E03 立项实操段4：失败预案——止损线 / 回退 / 复盘 + 试点可止损金句。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。**1 场景 5 region**（scenes=1，避开 R-R-010 相邻同质误报）。标题 + 三兜底卡 + 金句，按 narration 锚点 reveal 同屏累积。

## style

教程风控对比风。深色底 + 三条兜底卡（红/橙/蓝语义）+ 绿色金句收束。布局：标题顶部 → 三卡横排（3 列等宽）→ 金句底部条。

## color_direction

深蓝底 + 多色语义（红=止损风险 / 橙=回退可控 / 蓝=复盘分析 / 绿=金句正向）：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | `#0F172A` | 深蓝主底 |
| 止损线（风险预警） | `#EF4444` | 红色（警示） |
| 回退（可控） | `#F59E0B` | 橙色（可控止损） |
| 复盘（分析） | `#3B82F6` | 蓝色（理性） |
| 金句（正向） | `#10B981` | 绿色（落地信心） |
| 蓝白 | `#E0E7FF` | 标题/次要 |

## immersion_mode

教程横屏 reveal — 1 场景 + 5 region（标题+三卡+金句）。region 按 data-reveal 时间点淡入 + 方向（标题 fade / 卡①left / 卡②top / 卡③left / 金句 fade）。

## 视觉区域范式（1 场景，~75s）

### 单场景：失败预案（5 region 同屏累积）

- **region1 标题**（data-reveal=0，dir=fade）：「失败预案 · 立项就想好退路」fade-in
- **region2 卡①止损线**（data-reveal=10，dir=left）：3 个月触发复盘（工具没装好/培训没到位/场景选错）
- **region3 卡②回退**（data-reveal=26，dir=top）：按月付费可停 + 范围可缩 + Git 可回退 · 沉没成本低
- **region4 卡③复盘**（data-reveal=42，dir=left）：方法错 vs 执行错 · 调整后再小范围试 · 不梭哈
- **region5 金句**（data-reveal=60，dir=fade）：「试点验证 + 可止损 · 老板才敢真投」绿色

## 动画策略

- region fade-in + 方向偏移（left 从 x:-40 / top 从 y:-40 / fade 纯 opacity），500ms
- 三卡横排等宽（grid 3 列），金句底部横条
- fx-pulse 多色静态光晕 + fx-blink 锚点（禁划过类）

## bg_component

`clean_slate`（单场景简洁底）

## visual_type

`tutorial_fail`（失败预案三卡 + 金句）
