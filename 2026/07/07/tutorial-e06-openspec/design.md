# design.md — E06 段4 OpenSpec 三概念四命令

## orientation

orientation: landscape
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏。三概念卡片（Spec/Change/Archive）+ 终端命令窗口（explore/propose/apply/archive 打字动画）+ 关键一条卡。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。4 region（标题 / 三概念 / 四命令终端 / 关键一条）。

## color_direction

深蓝 dark_cipher 底 + Spec 蓝（稳定）+ Change 紫（一次性）+ Archive 绿（存档）+ 终端命令青/金：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | dark_cipher | 代码矩阵 |
| 标题 | `#FCD34D` | 金色 |
| Spec 规格 | `#3B82F6` | 蓝色（稳定）|
| Change 变更 | `#A78BFA` | 紫色（一次性）|
| Archive 存档 | `#6EE7B7` | 绿色（归档）|
| 终端窗口底 | `#0a0a0a` | 深底（JetBrains Mono 等宽）|
| 终端命令 | `#60A5FA` | 青蓝（命令名）|
| 终端说明 | `#6EE7B7` | 绿（输出）|
| 关键一条 | `#FBBF24` | 金（specs 精简原则）|

## 视觉区域范式（1 场景）

- **region1 标题**（reveal 0，fade）：标题「OpenSpec」+ 副标「三概念 · 四命令 · SDD 落地工具」
- **region2 三概念**（reveal 8，left）：三卡（Spec 稳定/specs 目录 · Change 一次性/changes 目录 · Archive 存档）
- **region3 四命令终端**（reveal 32，left）：终端窗口（深底 + 红黄绿圆点 + JetBrains Mono）+ 四命令逐行打字（explore/propose/apply/archive）+ 每命令说明
- **region4 关键一条**（reveal 63，fade）：金卡「OpenSpec 自动读 specs 应用到代码 · specs 精简只放稳定规范 · 一次性变更放 changes」

## bg_component

`dark_cipher`
