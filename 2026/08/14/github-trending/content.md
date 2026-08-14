# content.md — 2026-08-14 GitHub Trending 数据源记录

## 数据来源

- 主数据源：`github_trending.py --date 2026-08-14 --since daily --yesterday workspace/2026/08/13/github-trending/raw_trending.json`
- 代理：172.21.0.102:7890
- 验证源：gh api（17/17 verified）
- 项目数：17（≥8 通过）
- 活跃度：14/17（82% ≥80%）
- 与昨日重叠：9 重叠 / 8 新条目

## 池约束说明（修正版）

### 关键认知修正
AI≤2 是**上限不是下限**。本期非 AI 池有 2 个合法开源安全工具（spiderfoot/holehe），中性化讲"自查/防御"可入（非 Red Flags 零容忍的 VPN/IPTV/破解类）。前次将 OSINT 工具笼统判"灰色剔除"过度保守——它们是 GitHub 长期存在的合法安全研究工具。

### 1. 近 2 天 daily 已入选（禁选）
- 08-13：cathrynlavery/diagram-design / localsend/localsend / ZuodaoTech/everyone-can-use-english / hugohe3/ppt-master / cactus-compute/needle
- 08-12：3b1b/manim / jaywcjlove/awesome-mac / practical-tutorials/project-based-learning / nvm-sh/nvm

### 2. AI 不连续重复原则
昨日 ai-wind（08-14）已讲：macro / needle / unsloth / ragflow / semantica。本期 daily 避开这 5 个，选 2 个新 AI（FluidVoice / modly），无连续两天重复。

### 3. 最终入选（4 项目，隐私自查 + 本地工具）

| 项目 | 类别 | 受众 | 总星 | 今日 | AI |
|------|------|------|------|------|----|
| smicallef/spiderfoot | 攻击面自查 | A | 20.7K | +278 | 非 |
| megadose/holehe | 邮箱痕迹自查 | B | 12.4K | +166 | 非 |
| altic-dev/FluidVoice | 离线语音听写 | A | 9.9K | +76 | AI |
| lightningpixel/modly | 本地图生 3D | A | 5.5K | +118 | AI |

非 AI 2 ≥ min_non_ai=2 ✅；AI 2 ≤ cap=2 ✅；总数 4 ≥ min_count=4 ✅

## 真实性核验（gh api）

| 项目 | owner 注册 | watchers | 星叉比 | 判定 |
|------|-----------|----------|--------|------|
| smicallef/spiderfoot | 2012-04 | 447 | 6.2:1 | ✅（OSINT 圈知名，14 年老号） |
| megadose/holehe | 2019-06 | 259 | 7.4:1 | ✅（经典工具，702 天不活跃但功能稳定） |
| altic-dev/FluidVoice | 2025-08 | 44 | 14.9:1 | ✅ |
| lightningpixel/modly | 2020-04 | 47 | 9.4:1 | ✅ |

0 HARD 命中。

## 选题说明

本期主题"守住隐私"——2 安全自查 + 2 本地不上传，4 项目都与"隐私/本地/自查"相关，主线连贯。AI 仅 2 个（上限），均本地不上传型，避开昨日 ai-wind 重复。安全工具中性化讲防御/自查（非攻击向），属合法安全科普。
