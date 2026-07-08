# design.md — E06 段8 devflow 一条命令（终端演示+三模式+规则覆盖）

## orientation

orientation: landscape
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏。devflow 终端窗口（深底 #0a0a0a + 红黄绿圆点 + JetBrains Mono）命令逐字打字 + Stage 1-6 依次执行输出 fade-in + 三模式卡片（标准/快速/迷你）+ 规则覆盖示意（rules/ 改写出口）。复用 openspec/sdd 段的终端组件样式。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。4 region（标题 / devflow 终端演示 / 三模式卡片 / 规则覆盖示意）。

## color_direction

深蓝 dark_cipher 底 + 终端深色窗口 + Stage/命令色（终端绿/金/蓝/紫）+ 三模式色（标准金/快速蓝/迷你绿）：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | dark_cipher | 代码矩阵 |
| 标题 | `#FCD34D` | 金色 |
| 终端窗口底 | `#0a0a0a` | 终端深底 |
| 命令 prompt | `#6EE7B7` | 绿（命令）|
| 命令文本 | `#FCD34D` | 金（用户输入）|
| Stage 输出 | `#60A5FA` | 蓝（执行）|
| Stage 完成 | `#6EE7B7` | 绿（done）|
| 标准模式 | `#FBBF24` | 金 |
| 快速模式 | `#60A5FA` | 蓝 |
| 迷你模式 | `#6EE7B7` | 绿 |
| 规则覆盖 | `#C4B5FD` | 紫（rules/）|

## 视觉区域范式（1 场景）

- **region1 标题**（reveal 0，fade）：标题「devflow 一条命令」+ 副标「编排型 skill · 串起六阶段」
- **region2 devflow 终端演示**（reveal 4，left）：终端窗口（标题栏 红黄绿圆点 + devflow）+ 命令 `/devflow --change add-feature` 打字 + Stage 1-6 依次执行输出 fade-in
- **region3 三模式卡片**（reveal 30，left）：三模式横排（标准 全六阶段 / 快速 精简头脑风暴 / 迷你 合并前三）+ 适用标签
- **region4 规则覆盖示意**（reveal 45，fade）：rules/ 目录覆盖示意（rules 改写 → 底层 skill 出口）+ 团队定制说明

## bg_component

`dark_cipher`
