# design.md — E06 段5 六阶段流水线总览

## orientation

orientation: landscape
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏。六阶段流水线可视化（核心组件）：横向 6 节点（探索→规范→计划→TDD→验证→归档），每节点图标+阶段名+skill 名，连线渐进绘制，当前节点高亮 pulse-ring。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。4 region（标题 / 六阶段流水线 / 渐进式披露卡 / 收束金句）。

## color_direction

深蓝 dark_cipher 底 + 六阶段渐变冷→暖（同色系禁白端点）：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | dark_cipher | 代码矩阵 |
| 标题 | `#FCD34D` | 金色 |
| 阶段1 探索 | `#60A5FA` | 蓝（起手·冷）|
| 阶段2 规范 | `#A78BFA` | 紫 |
| 阶段3 计划 | `#3B82F6` | 深蓝 |
| 阶段4 TDD | `#6EE7B7` | 绿（执行·中性）|
| 阶段5 验证 | `#FBBF24` | 金 |
| 阶段6 归档 | `#FCA5A5` | 暖红（收束·暖）|
| 当前节点 ring | 同色系 glow | box-shadow 同色（禁白）|
| 渐进披露 | `#FCD34D` | 金（核心思想）|

## 视觉区域范式（1 场景）

- **region1 标题**（reveal 0，fade）：标题「六阶段流水线」+ 副标「OpenSpec + Superpowers · 需求到交付」
- **region2 六阶段流水线**（reveal 6，fade）：横向 6 节点（探索/规范/计划/TDD/验证/归档）+ 节点间连线 SVG（dashoffset 渐进）+ 每节点图标+阶段名+skill 名（brainstorming/openspec-propose/writing-plans/subagent-driven/verification/archive）+ 节点依次 scale 0→1 stagger
- **region3 渐进式披露卡**（reveal 30，left）：金卡「每阶段只读当前 Stage 文件 · 渐进式披露 · 省 token」+ 六阶段 stage 文件名小字
- **region4 收束**（reveal 56，fade）：金句「一条命令 · 串起六阶段 · 中断了还能接着干」（断点续传伏笔，承接下段）

## bg_component

`dark_cipher`
