# design.md — E04 段5 推进治理（培训100% / 周会 / 周报 / 考核引导）

## orientation

orientation: landscape
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏。推进治理四要点 + 嘴上结论。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。6 region（标题 + 4 要点 + 结论）。

## color_direction

深蓝 scan_grid 底 + 四要点同色系（蓝渐进）+ 金结论：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | scan_grid | 深蓝网格 |
| 要点①-④ | `#93C5FD` 渐深 | 蓝色系（治理递进） |
| 结论 | `#F87171`→`#FCD34D` | 红→金（警示→指引） |

## 视觉区域范式（1 场景）

- **region1 标题**（reveal 0，fade）：标题「推进治理」+ 副标「要推到位」
- **region2-5 四要点**（reveal 4/11/17/23，left）：4 行卡片（① 培训100%全覆盖 ② 周会同步 ③ 强制周报 ④ 考核引导循序渐进）
- **region6 结论**（reveal 28，top）：警示「治理不到位 → 赋能就停在嘴上」

## bg_component

`scan_grid`

## visual_type

`tutorial_gov`
