# 内容摘要

## 来源
- 数据源：`raw_trending.json`（python_requests + gh API 双源采集，15 个项目）
- 验证源：`gh api repos/{owner}/{repo}` 对 5 个入选项目逐一复核（star/fork/watcher/created/size/contributors）
- 日期：2026-07-09

## 核心主题
2026 年 7 月 9 日 GitHub Trending 涌现一批「让 AI 和创意软件更好用」的实用工具——从把 GIMP 改造成 PS 界面的设计师补丁、到让 AI 看视频的内容工具、到跨 6 个平台一键汇总的研究工具。本期主轴：**工具效率 + 跨领域**，破除连续 4 期的纯 AI-Agent 盘点同质化，普通人也能用上的实用工具集。

## 选题方向（topic_plan.json）
- **topic_type**: 工具/效率（topic-tool）—— 避开 AI-Agent 疲劳题材
- **angle**: 工具让你少做手工 / 普通人也能用上的跨领域工具集
- **跨领域分布**: 设计（PhotoGIMP）/ 视频（claude-video）/ 研究（last30days）/ 文档（OfficeCLI）/ 3D（autoremesher）—— 5 个不同领域

## 关键信息点
- **PhotoGIMP 反直觉**：开源 GIMP 3 装个补丁，界面/快捷键就变 Photoshop——让不想付费的设计师无缝切换。今日 +1125，总星 1.5 万，A 档设计师普通可用（补丁即生效）
- **claude-video 反直觉**：AI 助手原本只能看文字和图，这个工具让它能"看"任何视频——下载/抽帧/转写一步到位。今日 +951，A 档内容创作工具
- **last30days-skill 跨平台**：一个 agent skill 跨 Reddit/X/YouTube/HN/Polymarket/网页 6 个平台做研究汇总，约 5 万人收藏的老牌项目今日再涨。B 档半可用
- **autoremesher 3D 跨圈**：自动四边重网格工具，把杂乱三角面转成干净四边面——给做 3D/游戏/动画的开发者用。今日 +296，C 档开发者向
- **OfficeCLI 霸榜增量**：今日涨星榜首 +1717，但 07/08 已详细展开 → 仅提增量（总星破 1.1 万），不重复介绍功能

## 数据（gh API 校准，2026-07-09）
| 项目 | 总星 | 今日涨幅 | Fork | Star/Fork | 创建 | 受众 | 领域 |
|------|------|---------|------|-----------|------|------|------|
| Diolinux/PhotoGIMP | 15043 | +1125 | 595 | 25:1 | 2020-06 | A | 设计工具 |
| bradautomates/claude-video | 6069 | +951 | 723 | 8.4:1 | 2026-04 | A | 视频/内容工具 |
| mvanhorn/last30days-skill | 50765 | +352 | 4237 | 12:1 | 2026-01 | B | 研究工具 |
| huxingyi/autoremesher | 2020 | +296 | 153 | 13:1 | 2020-06 | C | 3D 工具 |
| iOfficeAI/OfficeCLI | 11879 | +1717 | 807 | 14.7:1 | 2026-03 | B | 文档/办公工具 |

## 真实性验证（authenticity_verification，gh API）
| 项目 | Star/Fork | Watcher | 账号年龄 | 判定 |
|------|-----------|---------|---------|------|
| PhotoGIMP | 25:1 | 134（0.9%）| 6 年 | ✅ 通过（老牌设计师社区项目） |
| claude-video | 8.4:1 | 36（0.6%）⚠ | 2.5 月 | ✅ 1 警告（size 76KB 但 README 19.5KB + 723 forks + 39 issues 证真实活跃，skill 包体积小属正常）|
| last30days-skill | 12:1 | 166（0.3%）⚠ | 5.5 月 | ✅ 1 警告（watcher% 偏低是 skill 类共性用完即走，5 万星 + 4237 forks + 96 issues 真实活跃，raw 的 stars_total=0 系采集缺失，gh 校准 50765）|
| autoremesher | 13:1 | 69（3.4%）| 6 年 | ✅ 通过（最健康，3D 专业工具）|
| OfficeCLI | 14.7:1 | 30（0.25%）⚠ | 3.8 月 | ✅ 1 警告（watcher% 偏低是 CLI 工具共性，14.7:1 star/fork + 20 issues 正常）|

**综合**：0 HARD，3 个 watcher% 警告（skill/CLI 类共性，配合 star/fork 正常 + 多 contributors + 真实活跃信号），全部保留。

## 排除项
- **永久排除列表命中 1 个**：ruvnet/RuView（WiFi 感知人体，虚假/不可实现），跳过不入选
- **合规风险排除 1 个**：asgeirtj/system_prompts_leaks（泄露他人系统提示，平台合规风险），⛔ 排除
- **低增量跳过 3 个**：prisma/prisma（+46 老牌 ORM 无新意）、argoproj/argo-cd（+29 K8s）、wonderwhy-er/DesktopCommanderMCP（+28）
- **agent 题材饱和跳过 2 个**：TencentCloud/TencentDB-Agent-Memory（agent 记忆）、obra/superpowers（agentic skills 框架，07/08 邻近题材已覆盖）
- **重复展开跳过 2 个**：addyosmani/agent-skills（07/08 已展开）、TencentCloud/CubeSandbox（07/08 已展开）、alibaba/zvec（07/07 已展开）

## 原始素材路径
- `raw_trending.json`（15 项目双源采集）
- `assets/avatars/`（5 入选项目 owner avatar 已预下载）
