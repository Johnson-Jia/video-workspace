# design.md — E02 钩子段（反常识：AI 不是万能的）

## orientation

orientation: landscape
orientation_source: category_hint
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程类强制横屏（categories/tutorial.md orientation_hint=landscape）。反常识大字 + 副标题 + 转型起手 + 5 原理缩略，多区域同屏 reveal，竖屏装不下。s6_assemble 横屏分支依赖此字段。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16 教程横屏范式：单 phase + 多 region + data-reveal（不是竖屏 phase 切换）。反常识大字逐字 fade-in + 副标题 reveal + 转折区 + 5 原理缩略。区域 reveal 后同屏累积，不换屏。

## style

反常识冲击科技风。冷静、克制——一句反常识大字泼冷水，不靠花哨动画。黑底大字 + 轻量 fx-aura 静态光晕（禁划过类 fx）+ 副标题转折。教程重内容轻视觉。

## color_direction

深蓝底 + 反常识双色（金=冲击 / 蓝=转折理性）：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | `#0F172A` | 深蓝主底（沉稳，让大字跳出来） |
| 反常识冲击 | `#FBBF24` | 「AI 不是万能的」金色大字（泼冷水冲击） |
| 转折理性 | `#3B82F6` | 「能放大十倍」「转型起手」蓝色（理性指引） |
| 蓝白 | `#E0E7FF` | 副标题/次要文字 |
| 中性 | `#94A3B8` | 注释/分隔 |

> 强色控制：金/蓝严格分工——金=反常识冲击（打破预期），蓝=转折指引（给出路）。不混用。

## immersion_mode

教程横屏 reveal — 单 phase + 多 region。反常识大字 region 0s 在场（泼冷水）+ 副标题 region reveal（转折）+ 转折大字区 + 5 原理缩略 reveal。

## 视觉区域范式

### 场景 1：反常识揭示（~20s，大字 + 副标题）

- **反常识大字区**（data-reveal=0，场景开始即在）：「AI 不是万能的」金色大字（160px+）fade-in + 轻微 scale（克制不浮夸）
- **副标题区**（data-reveal=12）：蓝色副标题「但用对的人，能放大 10 倍」reveal opacity 0→1
- **fx-aura 静态光晕**：大字后方柔和金色光晕脉冲呼吸（禁 fx-scan/fx-beam 划过类）

### 场景 2：转型起手（~10s，转折收尾）

- **转折大字区**（data-reveal=0）：蓝色大字「转型起手 · 不是上工具」reveal + 副标题「先过这一关：思想转变 + 5 条原理」
- **5 原理缩略预告**（底部，data-reveal=5 依次）：五个胶囊小字「token 预测 / 上下文 1M / Agent / REACT / 精准指令」依次 reveal

## 动画策略

- **大字 fade-in**：opacity 0→1 + scale 1.04→1，600ms ease-out（克制）
- **副标题 reveal**：opacity 0→1，500ms
- **fx-aura 静态光晕**：脉冲呼吸（opacity 0.4→0.6 循环），**不划过不追线**
- **禁**：fx-scan/fx-stream/fx-beam 划过类、粒子过载、3D 翻转、强切换

## bg_component

`clean_slate`（反常识收敛简洁底，两个场景共用）

## visual_type 映射

- 场景 1：`contrarian_burst`（反常识大字冲击）
- 场景 2：`hook_transition`（转折收尾 + 5 原理预告）
