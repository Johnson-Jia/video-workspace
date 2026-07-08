# design.md — E04 段4 五件套辨析（CLAUDE.md / Skill / MCP / RAG / Hooks）

## orientation

orientation: landscape
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏。五件套卡片（围绕 CLAUDE.md）+ 团队级提效结论。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。6 region（标题 + 5 卡 + 结论合并）。

## color_direction

深蓝 scan_grid 底 + 五件五色 + 金结论：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | scan_grid | 深蓝网格 |
| CLAUDE.md | `#FCD34D` | 金色（核心/规范） |
| Skill | `#93C5FD` | 蓝色（工作流） |
| MCP | `#C4B5FD` | 紫色（连接） |
| RAG | `#6EE7B7` | 绿色（知识/减幻觉） |
| Hooks | `#FCA5A5` | 浅红（钩子/防护） |
| 结论 | `#FCD34D` | 金色 |

## 视觉区域范式（1 场景）

- **region1 标题**（reveal 0，fade）：标题「五件套」+ 副标「围绕 CLAUDE.md」
- **region2 五卡**（reveal 4，left）：5 卡片（① CLAUDE.md / ② Skill / ③ MCP / ④ RAG / ⑤ Hooks），各列职责一句话
- **region3 结论**（reveal 30，top）：金色「团队级提效关键 · 个体再强 规范不沉淀就复制不开」

## bg_component

`scan_grid`

## visual_type

`tutorial_five`
