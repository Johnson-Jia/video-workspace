# 内容摘要

## 来源
GitHub Trending 日榜（raw_trending.json，github_trending.py 主榜 7 项 + 语言日榜扩池 30 项，2026-08-17 采集）+ gh api 实时核验

## 核心主题
8月17日 GitHub 日榜盘点：一个"不写代码"的免费 API 清单项目登顶（public-apis 46万星），叠加 AI 短视频生成、前端元框架、时序预测模型、命令行音视频工具五个方向。

## 关键信息点
- public-apis/public-apis：免费 API 大全清单，46.1万★ 总量 + 单日 1588（今日榜首）。反直觉核心：代码托管平台上星标最多的项目之一，主业是整理文档清单不写代码
- cordiverse/cordis：时空可组合的元框架（框架的框架），4.7K★ + 单日 720（对 4.7K 体量是爆发涨幅），TypeScript，Koishi 社区团队出品
- harry0703/MoneyPrinterTurbo：AI 大模型 + 自动化工作流一键生成高清短视频，10.4万★ + 单日 494（AI 项目 1/2）
- yt-dlp/yt-dlp：功能丰富的命令行音视频下载工具，18.4万★ + 单日 216，2020 年至今常青树（中性化：讲常青与工具能力，禁引导下载版权内容）
- google-research/timesfm：谷歌研究团队时序预测基础模型，27.8K★ + 单日 109（AI 项目 2/2；gate 加权制判非 AI，宽判定算 AI，按 AI 谨慎占用名额）

## 数据（gh api 实时核验 2026-08-17）
| 项目 | 总星 | 单日 | Fork | Watchers | 账龄 | 核验 |
|---|---|---|---|---|---|---|
| public-apis | 461,797 | +1588 | 51,012 | 4,669 | 2016 仓库 / 2019 org | 0 HARD 通过 |
| cordis | 4,761 | +720 | 257 | 22 | 2022 仓库 / 2023 org | 1 轻微警告（watchers 0.46%），知名社区框架，通过 |
| MoneyPrinterTurbo | 104,711 | +494 | 15,913 | 662 | 2024 仓库 / 2013 作者 | 0 HARD 通过 |
| timesfm | 27,807 | +109 | 2,708 | 185 | 2024 仓库 / google-research 官方 org | 0 HARD 通过 |
| yt-dlp | 184,902 | +216 | 15,925 | 912 | 2020 仓库 / 2021 org | 0 HARD 通过 |

## 池约束执行记录
- team-lead 已按 HARD gate 选定 5 项目（不增删换）；AI 加权制 1 个（MoneyPrinterTurbo；timesfm gate 判非 AI）≤2 ✓；非 AI ≥2 ✓；总数 5 ✓
- 近2天禁选（ego-lite/spec-kit/OpenCut/rustdesk）零命中 ✓；昨日 ai-wind 5 AI（cloudflare/computer、google/skills、hkuds/cli-anything、soup、ToolJet）零重叠 ✓
- 与 08-15 日榜 / 08-16 周榜入选项目零重复 ✓

## 原始素材路径
raw_trending.json（项目目录内）｜avatars: assets/avatars/{owner}.png（fetch_avatars.py 已回写）
