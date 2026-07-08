# design.md — E04 CTA（E05 预告 + 合集引导）

## orientation

orientation: landscape
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏收尾。收束（三件事到位→基础设施）+ E05 预告 + 合集引导 + 互动问题。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。3 region（收束 + E05 预告 + 合集/互动）。

## color_direction

深蓝 scan_grid 底 + 收束蓝 + E05 预告金 + 合集互动蓝白：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | scan_grid | 深蓝网格 |
| 收束 | `#93C5FD` | 蓝色（三件事收束） |
| E05 预告 | `#FCD34D` | 金色（下集） |
| 合集/互动 | `#E0E7FF` | 蓝白（引导/互动） |

## 视觉区域范式（1 场景）

- **region1 收束**（reveal 0，fade）：「工具装好 + 规范沉淀 + 团队赋能到位 → 下一步 基础设施（装眼睛和记忆）」
- **region2 E05 预告**（reveal 8，top）：金色卡「下集 · 基础设施」（RAG + 代码知识图谱 + Skill 仓库）
- **region3 合集+互动**（reveal 16，fade）：「合集 12 集 · 点关注不走丢 · 评论区有教程仓库」+ 互动问题「你的团队，Claude Code 装上了吗？」

## bg_component

`scan_grid`

## visual_type

`tutorial_cta`
