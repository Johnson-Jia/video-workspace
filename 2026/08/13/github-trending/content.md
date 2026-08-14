# content.md — 2026-08-13 GitHub Trending 数据源记录

## 数据来源

- 主数据源：`python .claude/commands/clipforge/scripts/github_trending.py --output-dir ... --date 2026-08-13 --since daily --yesterday workspace/2026/08/12/github-trending/raw_trending.json`
- 代理：172.21.0.102:7890（GitHub 直连失败，带代理抓取）
- 验证源：gh api（17/17 verified）
- 项目数：17（≥8 通过）
- 活跃度：14/17（82% ≥80% 通过）；3 个 >30 天未 push：shiyu-coder/Kronos(121d) / ZuodaoTech/everyone-can-use-english(44d) / smicallef/spiderfoot(121d)
- 与昨日重叠：4 重叠 / 13 新条目（非完全相同，通过）

## 池约束说明

### 1. 近 2 天 daily 已入选（禁选）
- 08-12：3b1b/manim / jaywcjlove/awesome-mac / practical-tutorials/project-based-learning / nvm-sh/nvm
- 08-11：PrimeIntellect-ai/prime-agent / semantica-agi/semantica
- 今日 raw 中命中：semantica-agi/semantica（禁选）

### 2. AI 项目上限（≤2）
今日 17 项目中 10 个 AI（gate 判定）。排除与昨日 ai-wind 重叠（orca/paperclip/agency-agents/ragflow 等虽跨频道不强制拦，但主动降重叠）。

剩余非 AI 候选筛选：
- ❌ NanmiCoder/MediaCrawler（社交平台爬虫，平台违规风险，Red Flags 零容忍剔除）
- ❌ shiyu-cacher/Kronos（金融基础模型，实际 AI；且金融敏感 + 121 天不活跃）
- ⚠️ 不选 NVIDIA-NeMo/Switchyard（desc 空，实际 NVIDIA AI 平台子项目）
- ⚠️ 不选 smicallef/spiderfoot（OSINT 灰色 + 121 天不活跃）
- ✅ cathrynlavery/diagram-design（+2855 当日爆点，图表模板）
- ✅ localsend/localsend（AirDrop 替代）
- ✅ ZuodaoTech/everyone-can-use-english（英语自学，44 天不活跃但 36K 大项目可入）

AI 新面孔（避开昨日 ai-wind）：
- ✅ hugohe3/ppt-master（AI 做 PPT，未选过）
- ✅ cactus-compute/needle（14MB 端侧模型，未选过）

### 3. 最终入选（5 项目，生活工具多元）

| 项目 | 类别 | 受众 | 总星 | 今日 | AI |
|------|------|------|------|------|----|
| cathrynlavery/diagram-design | 图表模板 | A | 10.5K | +2855 | 非 |
| localsend/localsend | 跨端传输 | A | 87.8K | +213 | 非 |
| ZuodaoTech/everyone-can-use-english | 英语自学 | A | 36.1K | +86 | 非 |
| hugohe3/ppt-master | AI 做 PPT | A | 45.6K | +476 | AI |
| cactus-compute/needle | 端侧小模型 | A | 4.2K | +315 | AI |

## 真实性核验（gh api）

| 项目 | owner 注册 | watchers | 星叉比 | 判定 |
|------|-----------|----------|--------|------|
| cathrynlavery/diagram-design | 2019-05 | 41 | 15.5:1 | ✅（watcher 偏低但模板类通性，owner 42 repos 真实） |
| localsend/localsend | 2022-12 | 330 | 18:1 | ✅（知名 AirDrop 替代，watcher 偏低是大项目通性） |
| ZuodaoTech/everyone-can-use-english | 2021-07 | 318 | 7.2:1 | ✅ |
| hugohe3/ppt-master | 2024-11 | 95 | 12.3:1 | ✅（watcher 偏低但 owner 5 repos 386 followers 真实） |
| cactus-compute/needle | 2025-01 | 32 | 13.9:1 | ✅ |

0 HARD 命中。

## 选题说明

本期主题"让生活变简单的开源工具"，5 方向多元（设计/传输/学习/办公/端侧 AI），全 A 档普通可用。与昨日 ai-wind（智能体工程化）+ 08-12 daily（老工具长青树）题材错开。
