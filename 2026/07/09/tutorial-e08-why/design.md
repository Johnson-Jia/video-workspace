# design.md — E08 why（为什么度量：不可度量=不可管理 + 放大与证伪两件事）

## orientation

orientation: landscape
orientation_source: category_hint
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏。为什么必须度量：感觉有用→预算没了 流程 + 不可度量=不可管理 金句 + 放大与证伪两件事。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。1 场景 4 region。标题（左对齐）+ 危险状态流程卡（感觉有用→预算没了）+ 金句卡（不可度量=不可管理）+ 两件事图标（放大/证伪）。布局 space-between 撑满画布。

## style

方法论警示风。标题左对齐 + 危险状态流程横排（红/金渐变警示）+ 金句居中大字 + 两件事图标卡（蓝=放大/绿=证伪）。

## color_direction

深底 + 三色（红=危险状态 / 金=警示金句 / 蓝=放大 / 绿=证伪）：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | `#0F172A` | 深蓝主底（hex_grid 网格叠层） |
| 危险状态 | `#F87171` | 红色（感觉有用→预算没了） |
| 金句警示 | `#FBBF24` | 金色（不可度量=不可管理） |
| 放大 | `#3B82F6` | 蓝色（从试点到全团队） |
| 证伪 | `#10B981` | 绿色（数据证伪） |

## immersion_mode

教程横屏 reveal — 1 场景 + 4 region（标题+危险状态流程+金句+两件事）。region 按 data-reveal 时间点淡入 + 方向。

## bg_component

`hex_grid`（深蓝六边形网格，与 E08 其他段做 bg 差异，避开 E07 dark_cipher）

## visual_type

`tutorial_why`（为什么度量：危险状态流程 + 金句 + 两件事图标布局）
