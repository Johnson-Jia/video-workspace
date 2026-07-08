# design.md — E06 walls（三堵墙详解 + 各自解法标签）

## orientation

orientation: landscape
orientation_source: category_hint
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏。段1 三堵墙详解：分析不准 / 上下文断 / 偏差晚发现，各配解法标签（SDD / tasks / spec）。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。长场景（~75s）拆 4 region（标题 + 墙1 + 墙2 + 墙3 + 解法映射），按 narration 锚点 reveal。

## style

三堵墙纵排详解。每墙：图标 + 墙名 + 现象描述 + 解法标签胶囊。最后解法映射总结（三墙 → SDD/tasks/spec）。

## color_direction

深蓝 dark_cipher 底 + 三墙色（红/紫/蓝）+ 解法标签金：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | dark_cipher | 代码矩阵 |
| 墙1 分析不准 | `#FCA5A5` | 浅红 |
| 墙2 上下文断 | `#C4B5FD` | 紫色 |
| 墙3 偏差晚发现 | `#93C5FD` | 蓝色 |
| 解法标签 | `#FBBF24` | 金色 |

## immersion_mode

教程横屏 reveal — 1 场景 + 多 region。region 按 data-reveal 依次 reveal + 方向（标题 fade / 墙左滑入 / 解法 top）。

## 视觉区域范式（1 场景，~75s TTS）

### 单场景：三堵墙纵排详解 + 解法映射（5 region 同屏累积）

- **region1 标题**（data-reveal=0，dir=fade）：标题「三堵墙 · 闭环难点拆解」
- **region2 墙1 分析不准**（data-reveal=6，dir=left）：图标 + 墙名「分析不准」+ 现象「一句话需求理解偏 越写越歪」+ 解法标签「SDD 规范驱动」
- **region3 墙2 上下文断**（data-reveal=22，dir=left）：图标 + 墙名「上下文断」+ 现象「会话中断分析决策进度全丢」+ 解法标签「tasks 断点续传」
- **region4 墙3 偏差晚发现**（data-reveal=40，dir=left）：图标 + 墙名「偏差晚发现」+ 现象「代码写完才发现理解错 改代码代价大」+ 解法标签「spec 先行验证」
- **region5 解法映射收束**（data-reveal=58，dir=top）：三墙→三解法映射卡（分析不准→SDD / 上下文断→tasks / 偏差晚发现→spec）

## 动画策略

- region fade-in + 方向偏移，500ms
- 三墙纵排（移动端友好；横屏用紧凑卡纵列）
- 解法标签金色胶囊强调
- fx-aura 静态光晕（三墙色 + 金解法；呼吸脉冲，禁划过类）

## bg_component

`dark_cipher`（代码矩阵，规范驱动结构感）

## visual_type

`tutorial_walls`（三堵墙详解 + 解法映射）
