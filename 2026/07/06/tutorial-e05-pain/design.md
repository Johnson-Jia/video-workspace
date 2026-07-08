# design.md — E05 pain（三个痛点：不懂业务/看不见全貌/留不住能力）

## orientation

orientation: landscape
orientation_source: category_hint
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏。三痛点纵排卡片，每卡对应解法标签（RAG/图谱/Skill）。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。1 场景 2 region（标题 + 三卡纵排）。

## style

三卡片纵排（不懂业务/看不见全貌/留不住能力），每卡左图标 + 痛点名 + 一句话 + 右侧解法胶囊标签。底部结论金条。

## color_direction

深蓝 diamond_lattice 底 + 三痛点三色 + 解法标签金：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | diamond_lattice | 45°菱形网格（基础设施结构感） |
| 痛点1 不懂业务 | `#FCA5A5` | 浅红（幻觉） |
| 痛点2 看不见全貌 | `#C4B5FD` | 紫色（盲读） |
| 痛点3 留不住能力 | `#93C5FD` | 蓝色（流失） |
| 解法标签 | `#FCD34D` | 金色（RAG/图谱/Skill） |
| 结论 | `#FCD34D` | 金色 |

## 视觉区域范式（1 场景，~65s TTS）

- **region1 标题**（reveal 0，fade）：标题「为什么 AI 需要眼睛和记忆」+ 副标「三个痛点」
- **region2 三卡纵排**（reveal 4，left）：3 卡片（① 不懂业务 → RAG / ② 看不见全貌 → 代码图谱 / ③ 留不住能力 → Skill 仓库），reveal stagger
- **region3 结论金条**（reveal 50，top）：金色「四件套就是解决这三件事」

## bg_component

`diamond_lattice`（45°菱形网格，基础设施结构感）

## visual_type

`tutorial_pain`（三痛点 + 解法标签）
