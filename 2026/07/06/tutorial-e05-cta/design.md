# design.md — E05 CTA（收束 + E06 预告 + 合集引导）

## orientation

orientation: landscape
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏收尾。收束（基础设施深水区武器）+ E06 预告（闭环试点 OpenSpec+Superpowers）+ 合集引导 + 互动问题。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。3 region（收束 + E06 预告 + 合集/互动）。

## color_direction

深蓝 hex_grid 底 + 收束金 + E06 预告蓝 + 合集互动蓝白：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | hex_grid | 六边网格（基础设施结构感） |
| 收束 | `#FCD34D` | 金色（基础设施深水区） |
| E06 预告 | `#93C5FD` | 蓝色（闭环试点） |
| 合集/互动 | `#E0E7FF` | 蓝白（引导/互动） |

## 视觉区域范式（1 场景）

- **region1 收束**（reveal 0，fade）：「基础设施是大团队的深水区武器 · 小团队跳过不丢人 → 下一步 闭环试点」
- **region2 E06 预告**（reveal 8，top）：蓝色卡「E06 · 闭环试点 · OpenSpec + Superpowers · 需求到交付一条命令跑完」
- **region3 合集+互动**（reveal 16，fade）：「合集 12 集 · 点关注不走丢 · 评论区有教程仓库」+ 互动问题「你的团队，代码库到了需要图谱的规模吗？」

## bg_component

`hex_grid`

## visual_type

`tutorial_cta`
