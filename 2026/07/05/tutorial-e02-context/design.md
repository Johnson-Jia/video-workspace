# design.md — E02 原理③ 上下文 1M（约束原点）

## orientation

orientation: landscape
orientation_source: category_hint
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏（categories/tutorial.md orientation_hint=landscape）。上下文 = 1M token 约束原点，1 场景 3 region 同屏累积 reveal：原理编号 + 上下文桶（count-up 填充 0→100%）+ 最佳实践清单。s6_assemble 横屏分支依赖此字段。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。**1 场景 3 region**（scenes=1，避开 R-R-010 相邻同质）。标题 + 上下文桶 + 最佳实践清单，按 narration 锚点 reveal 同屏累积。

## style

原理约束揭示科技风。冷静、克制——上下文桶可视化（count-up 填充到 100% 撑爆）+ 四条最佳实践清单。教程重结构清晰、约束可视化。

## color_direction

深蓝底 + 三段语义色（蓝=原理 / 金=1M 大 / 红=撑爆警示 / 绿=实践落地）：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | `#0F172A` | 深蓝主底 |
| 原理编号/标题 | `#3B82F6` | 蓝色（理性原理） |
| 1M token / 桶大字 | `#FBBF24` | 金色（听着很大） |
| 撑爆警示 | `#EF4444` | 红色（撑爆 = 性能下降） |
| 实践清单 | `#10B981` | 绿色（最佳实践 = 正向落地） |
| 蓝白 | `#E0E7FF` | 次要文字 |

> 强色控制：蓝/金/红/绿严格分工——蓝=原理、金=1M 看着大、红=撑爆危险、绿=实践正向。count-up 填充过程金→红渐变（接近 100% 警示）。

## immersion_mode

教程横屏 reveal — 1 场景 + tut-grid 三区布局（标题 / 上下文桶 + 实践清单水平并列）+ count-up 桶填充。region 按 data-reveal 时间点淡入 + 方向（标题 fade / 桶 left / 实践 top）。

## 视觉区域范式（1 场景，~30s）

### 单场景：上下文约束全貌（3 region 同屏累积）

- **region1 标题**（data-reveal=0，fade）：「原理 ③」蓝色编号胶囊 + 标题「上下文 1M · 约束原点」
- **region2 上下文桶**（data-reveal=5，left）：桶形容器 + 「1M token」金色大字 + count-up 填充度 0→100%（data-count-to="100" data-count-at="7"）+ 「撑爆」红色标 + 三大撑爆源旁注（大代码库 / 长会话 / MCP 工具定义）
- **region3 最佳实践清单**（data-reveal=16，top）：四条实践胶囊（精简 CLAUDE.md / 按需 Skill / 干净会话 / CLI 优于 MCP）+ 金句「上下文是稀缺资源 · 每一段常驻内容都要挣一席之地」

## 动画策略

- region fade-in + 方向偏移（left 从 x:-40 / top 从 y:-40），500ms
- **count-up 桶填充**：data-count-to="100" data-count-at="7"（reveal 时间 5 + 2s 后触发），GSAP textContent tween 0→100 snap 整数，0.9s power2.out
- 上下文桶：纯 CSS 桶形容器（border + 圆角）+ 填充条高度同步数字（CSS 静态，count-up 只驱动数字，桶填充用 fx-pulse 呼吸暗示容量）
- fx-pulse + fx-blink 静态点缀（禁划过类 fx-scan/fx-beam）

## bg_component

`clean_slate`（原理约束收敛简洁底）

## visual_type

`principle_context_window`（原理③ 上下文桶 + 实践清单）
