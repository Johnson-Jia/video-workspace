# design.md — E06 段3 SDD 三产物（spec/plan/tasks + 纠错左移，核心段）

## orientation

orientation: landscape
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏。左侧 SDD 三产物卡片（spec/plan/tasks）+ 右侧纠错左移对比图（核心视觉）。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。4 region（标题 / 三产物 / 左移对比 / bonus）。

## color_direction

深蓝 dark_cipher 底 + spec 蓝（WHAT）+ plan 紫（HOW）+ tasks 绿（DO）+ 左移对比 红→绿：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | dark_cipher | 代码矩阵（规范驱动质感）|
| 标题 | `#FCD34D` | 金色 |
| spec.md (WHAT) | `#3B82F6` | 蓝色（做什么）|
| plan.md (HOW) | `#A78BFA` | 紫色（怎么做）|
| tasks.md (DO) | `#6EE7B7` | 绿色（做到哪了）|
| 改代码（质量损失）| `#F87171` | 红色（晚发现代价大）|
| 改 Markdown（质量可控）| `#34D399` | 绿色（早发现代价小）|
| 质量提升金句 | `#FBBF24` | 金色（一个数量级）|

## 视觉区域范式（1 场景）

- **region1 标题**（reveal 0，fade）：标题「SDD 规范驱动开发」+ 副标「三层产物 · 纠错左移」
- **region2 三产物卡片**（reveal 9，left）：三卡纵排（spec.md WHAT / plan.md HOW / tasks.md DO）+ 每卡格式说明 + 回答问题
- **region3 纠错左移对比**（reveal 43，left，核心）：「改代码」红色质量损失 → 左移大箭头 → 「改 Markdown」绿色质量可控 + 金句「质量提升一个数量级」
- **region4 tasks bonus**（reveal 73，fade）：绿卡「tasks bonus · 断点续传」+ 引出下段

## bg_component

`dark_cipher`
