# design.md — E02 agent 段（原理④⑤ Agent + REACT）

## orientation

orientation: landscape
orientation_source: category_hint
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏。原理④⑤ 同框：上半 Agent 公式 + 下半 REACT 循环图。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。**1 场景 3 region**（scenes=1，避开 R-R-010）。

## style

教程科技风。上下分区：上方 Agent 公式卡（左），下方 REACT 循环图（横向流程 + 循环箭头）。

## color_direction

深蓝底 + 蓝绿语义色（Agent 蓝 / REACT 节点 蓝绿渐变）：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | `#0F172A` | 深蓝主底 |
| Agent 主色 | `#3B82F6` | 蓝（理性·Agent） |
| REACT 节点 | `#3B82F6` → `#10B981` | 蓝绿渐变（思考→行动→观察 循环） |
| Final | `#FBBF24` | 金色（最终答案·收束） |
| 注解/次要 | `#E0E7FF` | 蓝白 |

## immersion_mode

教程横屏 reveal — 1 场景。标题 → Agent 公式 → REACT 循环图，按 narration 锚点 reveal 同屏累积。

## 视觉区域范式（1 场景，~100s）

### 单场景：Agent + REACT（3 region 同屏累积）

- **region1 标题**（data-reveal=0）：原理编号「原理 ④ ⑤」+ 标题「Agent + REACT」fade-in
- **region2 Agent 公式卡**（data-reveal=10，dir=left）：公式「大模型 + 工具 = Agent」+ 注「先思考再行动靠系统提示词，不是训练」
- **region3 REACT 循环图**（data-reveal=35，dir=top）：4 节点（Thought 思考 → Action 行动 → Observation 观察 → 循环 ↺ → Final 答案）横向流程 + 循环箭头 fx-pulse 呼吸

## 动画策略

- region fade-in + 方向偏移（left 从 x:-40 / top 从 y:-40），500ms
- REACT 4 节点依次 reveal（35/40/45/50）
- 循环箭头 fx-pulse 呼吸（禁划过类）
- fx-pulse + fx-blink 静态点缀

## bg_component

`clean_slate`

## visual_type

`tutorial_agent_react`
