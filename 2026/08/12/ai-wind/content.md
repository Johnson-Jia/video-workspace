# content.md — 2026-08-12 AI 风向标 数据源记录

## 数据来源

- 主数据源：`python .claude/commands/clipforge/scripts/ai_trending.py --output-dir ... --date 2026-08-12 --since daily --yesterday workspace/2026/08/10/ai-wind/raw_trending.json`
- 验证源：gh api 三源交叉验证（ai_trending + gh_api）
- 抓取时间：2026-08-11 UTC
- AI 项目数：13（≥5 硬下限通过）
- 活跃度：13/13 近期 pushed（100% ≥80%）
- 与昨日（08-10，上周一）重叠：6 重叠 / 7 新条目

## 池约束说明

### 1. 近2天 ai-wind 已入选（08-10 周一，上次发布）
- msitarzewski/agency-agents（已选）
- Comfy-Org/ComfyUI（已选）
- ZhuLinsen/daily_stock_analysis（已选）
- harveyai/harvey-labs（已选）

### 2. 与 daily 综合近两日重叠（仅警示，ai-wind 独立选）
- PrimeIntellect-ai/prime-agent（daily 08-11 已选）
- semantica-agi/semantica（daily 08-11 已选）
- vitali87/code-graph-rag（daily 08-10 已选）

### 3. 最终入选（智能体工程化主线）

| 项目 | 子方向 | 受众 | 总星 | 今日 |
|------|--------|------|------|------|
| stablyai/orca | Agent 工具（并行） | A 普通可用 | 42.7K | +875 |
| HKUDS/DeepTutor | Agent 工具（导师） | A 普通可用 | 34.7K | +812 |
| paperclipai/paperclip | Agent 管理 | A 普通可用 | 77.1K | +748 |
| addyosmani/agent-skills | Agent 技能 | B 半可用 | 86.2K | +578 |
| anthropics/skills | Agent 技能（官方） | C 开发者向 | 168.1K | +485 |

## 真实性核验（gh api）

| 项目 | created | watchers | 星叉比 | 判定 |
|------|---------|----------|--------|------|
| stablyai/orca | 2026-03 | 96 | 14.3:1 | ✅ |
| HKUDS/DeepTutor | 2025-12 | 174 | 7.9:1 | ✅ |
| paperclipai/paperclip | 2026-03 | 381 | 5.4:1 | ✅ |
| addyosmani/agent-skills | 2026-02 | 462 | 9.3:1 | ✅ |
| anthropics/skills | 2025-09 | 1103 | 8.4:1 | ✅ |

0 HARD 命中。

## 选题说明

今日 AI 榜 13 项目过滤后 7 个候选全在「智能体」子方向，反映 AI 开源从"炫技"到"工程化干活"的拐点。入选 5 项目覆盖 Agent 全栈（用→管→装技能），与同日 daily 综合榜（老工具长青树非 AI 多元）差异化。
