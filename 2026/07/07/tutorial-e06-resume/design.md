# design.md — E06 段6 断点续传（tasks 状态机）

## orientation

orientation: landscape
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏。tasks 状态机动画（[ ]→[in_progress]→[x] 依次切换）+ 断点续传演示 + 案例数据卡（12 Controller/211 API/15000 行/110 任务）。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。4 region（标题 / 状态机三态 / 断点续传演示 / 案例数据卡）。

## color_direction

深蓝 dark_cipher 底 + 状态机三色（待办灰蓝/进行中金/完成绿）+ 案例数据金：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | dark_cipher | 代码矩阵 |
| 标题 | `#FCD34D` | 金色 |
| 待办 [ ] | `#94A3B8` | 灰蓝（未启动）|
| 进行中 [in_progress] | `#FBBF24` | 金（活跃·脉冲）|
| 完成 [x] | `#6EE7B7` | 绿（达成·打勾）|
| 断点续传流程 | `#60A5FA` | 蓝（恢复路径）|
| 案例数据 | `#FBBF24` | 金（醒目数据）|

## 视觉区域范式（1 场景）

- **region1 标题**（reveal 0，fade）：标题「断点续传」+ 副标「tasks 状态机 · 中断了接着干」
- **region2 状态机三态**（reveal 5，left）：三状态卡片（[ ] 待办 / [in_progress] 进行中 / [x] 完成）+ 依次切换高亮 + 打勾动画（GSAP 控制）+ 状态机箭头流转
- **region3 断点续传演示**（reveal 22，left）：流程链（退出 → 重进 → 扫 [x] → 续行）+ devflow 恢复判定说明
- **region4 案例数据卡**（reveal 38，fade）：金边数据卡（12 Controller · 211 API · 15000 行 · 110 任务）+ 「跨周断点续传」标签

## bg_component

`dark_cipher`
