# design.md — E06 段2 试点设计（选谁 / 多大 / 成功标准 / 止损）

## orientation

orientation: landscape
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏。试点决策四象限卡片 + 四条成功标准 checklist + 止损金句。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。5 region（标题引言 / 选谁 / 多大 / 成功标准 / 止损金句）。

## color_direction

深蓝 dark_cipher 底（代码矩阵）+ 选谁蓝 + 多大紫 + 成功标准金（checklist）+ 止损绿（金句）：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | dark_cipher | 代码矩阵（换 E05 hex_grid 做合集差异）|
| 标题 | `#FCD34D` | 金色 |
| 选谁 | `#3B82F6` | 蓝色（团队选择）|
| 多大 | `#A78BFA` | 紫色（规模数据）|
| 成功标准 | `#FBBF24` | 金色（checklist 点亮）|
| 止损金句 | `#6EE7B7` | 绿色（数据说话）|

## 视觉区域范式（1 场景）

- **region1 标题引言**（reveal 0，fade）：标题「试点设计」+ 副标「选对团队 · 定清标准」+ 引言「闭环不是全员跑 · 先选对试点」
- **region2 选谁**（reveal 11，left）：蓝卡「选谁 · 意愿强团队 + 业务典型项目」+ 两个反例红叉（别选最忙 / 别选最边缘）
- **region3 多大**（reveal 28，top）：紫卡「多大」+ 4 数据格（1-2 团队 / 3-8 人 / 1-2 需求 / 4-8 周）
- **region4 成功标准**（reveal 45，left）：金卡「成功标准四条」+ checklist 逐条点亮（AI 代码占比 / 产出提升 / 质量不降 / 愿意继续用）
- **region5 止损金句**（reveal 65，fade）：绿卡「失败就止损 · 拿数据说话 · 成功有数据推广 · 失败有原因可查」

## bg_component

`dark_cipher`
