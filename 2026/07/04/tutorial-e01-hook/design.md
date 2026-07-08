# design.md — E01 钩子段（数据飞升冲击）

## orientation

orientation: landscape
orientation_source: category_hint
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程类强制横屏（categories/tutorial.md orientation_hint=landscape）。B 站横屏播放，钩子段要同屏展示三个数据卡 + count-up + 注释行，竖屏装不下三卡并列。s6_assemble 横屏分支依赖此字段。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16 教程横屏范式：一屏多区域 + reveal（**不是竖屏 phase 切换**）。钩子段单 phase div + 三数据卡 region 同屏 grid + 按 narration 锚点依次 reveal + count-up。区域 reveal 后保持同屏累积，冲击递增不换屏。s6_assemble build_gsap 扫碎片 data-reveal 属性生成 reveal + count-up 动画。

## style

数据冲击科技风。钩子段要**干净 + 高信息密度 + 数据感强**（三数据卡同屏 + count-up + 注释行 + 悬念大字），不要花哨粒子抢数据注意力。count-up 动画 + 数字高亮是主角。

## color_direction

深蓝底 + 数据语义三色（金/蓝/绿，对应三数据，跟段 4 收官呼应）：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | `#0F172A` | 深蓝主底（沉稳专业，让数据色跳出来） |
| 主色 | `#1E3A8A` / `#3B82F6` | 蓝色主调（hero 标题/数据卡边框/悬念大字） |
| 数据①金 | `#FBBF24` | 人均代码产出 +104%（翻倍级，最强冲击色） |
| 数据②蓝 | `#3B82F6` | AI 代码占比 76.6%（AI 主题色） |
| 数据③绿 | `#10B981` | Bug 下降 -16.4pp（质量向好，绿色语义） |
| 蓝白 | `#E0E7FF` | 浅蓝白（注释行/次要文字） |
| 中性 | `#94A3B8` | 灰（注释「相关性非因果」/ 分隔） |

> 强色控制：金/蓝/绿三色**严格对应三数据**（+104% 金 / 76.6% 蓝 / -16.4pp 绿），不混用不互换。一屏多区域靠数据色区分语义，不靠强切换。三色跟段 4 收官数据卡呼应（合集视觉统一）。

## immersion_mode

教程横屏 reveal — 钩子段单 phase div + 三数据卡 region grid 同屏，按 data-reveal 时间点淡入 + count-up。悬念收尾用第二场景 hero 大字切换 reveal。

## 视觉区域范式（按内容自然组合）

### 场景 1：数据飞升冲击（~17s，一屏三数据卡 + 注释行）

- **三数据卡 grid**（横向并列，16:9 居中分布）：每卡含「数据值大字（count-up）+ 语义标签 + 色彩边框」
  - 左卡：`+104%` 金色大字（180px+，0→104 count-up 800ms）+ 标签「人均代码产出」+ 金色细边框
  - 中卡：`76.6%` 蓝色大字（180px+，0→76.6 count-up 800ms）+ 标签「AI 代码占比」+ 蓝色细边框
  - 右卡：`-16.4pp` 绿色大字（180px+，0→-16.4 count-up 800ms）+ 标签「Bug 下降」+ 绿色细边框
- **注释行**（三卡下方）：灰色小字「80+ 人团队 · 3 个月 · 206 仓库同比 · 相关性非因果」同屏淡入
- **reveal 节奏**：场景开始 0s reveal 左卡 +104%（冲击开场）→ 4s reveal 中卡 76.6%（冲击累积）→ 8s reveal 右卡 -16.4pp（三飞升齐现）→ 12s reveal 注释行（严谨口径收底）

### 场景 2：悬念收尾（~8s，hero 大字切换）

- **hero 大字区**：「怎么做到的？」主色蓝大字（200px+）fade-in + 蓝色下划线 width 0→100%
- **三数据卡缩小保留**（顶部或侧边小卡）— 不消失，作为「问题的背景」保持同屏
- **承接箭头**：右下角小箭头指向「下一段：方法论是什么」（蓝白）

## 动画策略

- **count-up**（核心冲击）：数字从 0 滚到目标值，800ms，缓动 ease-out（s6_assemble 按 data-reveal 触发）
- **reveal 淡入**：区域 opacity 0→1，500ms，按 narration 锚点同步
- **下划线 width**：hero 标题下划线 0→100%，600ms
- **克制原则**：无粒子光晕、无 3D 翻转、无强切换 — 数据本身就是主角，动画服务数据呈现

## bg_component

`scan_grid`（场景 1，数据卡科技网格底）/ `clean_slate`（场景 2，悬念收敛简洁底）

## visual_type 映射

- 场景 1：`data_burst`（三数据同屏 count-up 冲击）
- 场景 2：`hook_question`（悬念大字收尾）

## 与段 4 收官的视觉呼应

钩子段三数据卡（金/蓝/绿）与段 4 收官数据卡同色同布局——合集首尾呼应：钩子抛数据冲击开场，收官用同一组数据收尾验证。视觉记忆点统一。
