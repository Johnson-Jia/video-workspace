# design.md — E06 intro（这集讲什么 + 三堵墙预告）

## orientation

orientation: landscape
orientation_source: category_hint
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏。方法论段：单点用 AI 容易 / 端到端会撞三堵墙 / 本集路线图。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。1 场景 3 region（标题 + 三堵墙预告 + 路线图），按 narration 锚点 reveal。

## style

方法论引入。顶部标题「单点容易 端到端难」，中部三堵墙预告横排（分析不准/上下文断/偏差晚发现），底部路线图（为什么→SDD→六阶段→devflow）。

## color_direction

深蓝 dark_cipher 代码矩阵底 + 三堵墙蓝紫红 + 路线图金色：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | dark_cipher | 代码矩阵（规范驱动） |
| 标题 | `#E0E7FF` | 蓝白（主标） |
| 墙1 分析不准 | `#FCA5A5` | 浅红 |
| 墙2 上下文断 | `#C4B5FD` | 紫色 |
| 墙3 偏差晚发现 | `#93C5FD` | 蓝色 |
| 路线图 | `#FCD34D` | 金色（流程感） |

## immersion_mode

教程横屏 reveal — 1 场景 + 多 region。

## 视觉区域范式（1 场景，~36s TTS）

### 单场景：三堵墙预告 + 路线图（3 region 同屏累积）

- **region1 标题**（data-reveal=0，dir=fade）：标题「单点容易 · 端到端难」+ 副标「三堵墙 + 本集路线」
- **region2 三堵墙预告**（data-reveal=10，dir=left）：三墙横排（分析不准/上下文断/偏差晚发现），各列图标+一句话
- **region3 路线图**（data-reveal=24，dir=top）：金色路线节点（为什么闭环难 → SDD 规范驱动 → 六阶段流水线 → devflow 编排）

## 动画策略

- region fade-in + 方向偏移，500ms
- 三墙横排对称布局
- 路线图节点依次点亮
- fx-aura 静态光晕（金路线 / 三墙色；呼吸脉冲，禁划过类）

## bg_component

`dark_cipher`（代码矩阵，规范驱动结构感）

## visual_type

`tutorial_intro`（三堵墙预告 + 路线图）
