# content.md — 2026-08-12 GitHub Trending 数据源记录

## 数据来源

- 主数据源：`python .claude/commands/clipforge/scripts/github_trending.py --output-dir ... --date 2026-08-12 --since daily --yesterday workspace/2026/08/11/github-trending/raw_trending.json`
- 验证源：gh api 三源交叉验证（python_requests + gh_api）
- 抓取时间：2026-08-11T22:39:22 UTC
- 项目数：17（≥8 通过）
- 活跃度：17/17 近期 pushed（100% ≥80%）
- 与昨日重叠：6 重叠 / 11 新条目（非完全相同，通过）

## 池约束说明（双重过滤）

今日 17 项目经以下过滤：

### 1. 近 2 天禁选（同频道昨日/前日已入选）
- 昨日 08-11 入选：semantica / agency-agents / addyosmani-agent-skills / paperclip / prime-agent / vitali87-code-graph-rag
- 前日 08-10 入选：weathernext / t3code / vitali87-code-graph-rag / ComfyUI
- 今日 trending 中昨日已选 6 项目全部排除

### 2. AI 项目上限（≤2，ai-wind 已专项）
今日 17 项目中 13 个命中 AI 关键词（agent / llm / ai / transformers / tutor 等），包括：
- msitarzewski/agency-agents（AI agency）
- semantica-agi/semantica（Graph AI infrastructure）
- addyosmani/agent-skills（AI coding agents skills）
- ZhuLinsen/daily_stock_analysis（LLM 股票分析）
- vitali87/code-graph-rag（AI RAG）
- anthropics/skills（Agent skills）
- HKUDS/DeepTutor（AI tutor）
- stablyai/orca（Agent ADE）
- paperclipai/paperclip（Agent 管理）
- huggingface/transformers（ML 框架）
- harveyai/harvey-labs（Agent benchmark）
- calesthio/OpenMontage（Agentic video）
- PrimeIntellect-ai/prime-agent（RLM agent）

### 3. 最终入选（纯非 AI 多元池）

剩余 4 个纯非 AI 项目全部入选：

| 项目 | 类别 | 受众 | 总星 | 今日 |
|------|------|------|------|------|
| 3b1b/manim | 数学动画引擎 | A 普通可用 | 90.1K | +246 |
| jaywcjlove/awesome-mac | Mac 软件清单 | A 普通可用 | 110.4K | +334 |
| practical-tutorials/project-based-learning | 编程自学清单 | C 开发者向 | 278.4K | +394 |
| nvm-sh/nvm | Node 版本管理 | B 半可用 | 94.5K | +18 |

## 真实性核验（gh api）

| 项目 | owner 注册 | watchers | 星叉比 | 判定 |
|------|-----------|----------|--------|------|
| 3b1b/manim | 2015-03 | 946 | 12:1 | ✅ |
| jaywcjlove/awesome-mac | 2012-04 | 1526 | 13:1 | ✅ |
| practical-tutorials/project-based-learning | 2021-08 | 3459 | 7.8:1 | ✅ |
| nvm-sh/nvm | 2019-04 | 1081 | 9.1:1 | ✅ |

0 HARD 命中。practical-tutorials owner 只有 1 个公开仓库但有 5366 followers，账号活跃，判定通过。

## 选题说明

昨日（08-11）因 AI 池过重只入选 2 项目（prime-agent + semantica），今日回归非 AI 多元盘点 4 项目，符合 daily 与 ai-wind 差异化定位。
