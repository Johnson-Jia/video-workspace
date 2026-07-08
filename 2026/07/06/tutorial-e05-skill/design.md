# design.md — E05 段5 Skill 仓库（能力复用 + 两层架构降 Token）

## orientation

orientation: landscape
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏。两层架构卡片（公共 Skill / 项目级 Skill）+ RAG 向量库侧挂。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。4 region（标题 + 两层架构 + 降 Token 诀窍 + SkillHub）。

## color_direction

深蓝 hex_grid 底 + 公共层金（架构组）+ 项目级蓝（项目负责人）+ RAG 侧挂绿 + SkillHub 紫：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | hex_grid | 六边网格（基础设施结构感） |
| 标题 | `#FCD34D` | 金色 |
| 公共 Skill | `#FCD34D` | 金色（公司级/架构组） |
| 项目级 Skill | `#93C5FD` | 蓝色（项目专属） |
| RAG 向量库 | `#6EE7B7` | 绿色（按需检索） |
| SkillHub | `#C4B5FD` | 紫色（开源平台） |

## 视觉区域范式（1 场景）

- **region1 标题**（reveal 0，fade）：标题「Skill 仓库」+ 副标「能力复用 · 两层架构降 Token」
- **region2 两层架构**（reveal 4，left）：上层公共 Skill 3 卡（架构组维护）+ 下层项目级 Skill 3 卡（项目负责人）+ 中间箭头连接 + RAG 向量库侧挂
- **region3 降 Token 诀窍**（reveal 30，top）：金色卡「业务数据入 RAG · 项目级 Skill 只放规则+检索逻辑 · 保持极轻」
- **region4 SkillHub**（reveal 50，fade）：紫色卡「SkillHub · 讯飞出品 · Apache 协议 · 一条命令本地部署」

## bg_component

`hex_grid`

## visual_type

`tutorial_skill_repo`
