# design.md — E05 intro（基础设施四件套总览 + 谁该看谁该跳）

## orientation

orientation: landscape
orientation_source: category_hint
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏。四件套卡片总览 + 底部黄条「小团队可跳过」。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。1 场景 3 region（标题 + 四卡 + 黄条结论）。

## style

四件套卡片横排，各列职责一句话，底部黄条收束「小团队可跳过」。

## color_direction

深蓝 diamond_lattice 底 + 四件四色 + 金结论：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | diamond_lattice | 45°菱形网格（基础设施结构感） |
| RAG | `#6EE7B7` | 绿色（知识/业务） |
| 代码图谱 | `#93C5FD` | 蓝色（结构/全貌） |
| Skill 仓库 | `#FCD34D` | 金色（资产沉淀） |
| MCP 网关 | `#C4B5FD` | 紫色（连接/网关） |
| 结论 | `#FCD34D` | 金色（小团队可跳过） |

## 视觉区域范式（1 场景）

- **region1 标题**（reveal 0，fade）：标题「基础设施四件套」+ 副标「解决三件事」
- **region2 四卡**（reveal 5，left）：4 卡片（① RAG 业务知识 / ② 代码图谱 全貌 / ③ Skill 仓库 资产 / ④ MCP 网关 连接），各列职责
- **region3 黄条结论**（reveal 24，top）：金色「小团队可跳过 · CLAUDE.md + grep 就够」

## bg_component

`diamond_lattice`（45°菱形网格，基础设施结构感）

## visual_type

`tutorial_four`（四件套总览 + 跳过提示）
