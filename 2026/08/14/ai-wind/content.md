# content.md — 2026-08-14 AI 风向标 数据源记录

## 数据来源

- 主数据源：`ai_trending.py --date 2026-08-14 --since daily --yesterday workspace/2026/08/12/ai-wind/raw_trending.json`
- 代理：172.21.0.102:7890
- 验证源：gh api（17/17 verified）
- AI 项目数：13（≥5 硬下限通过）
- 活跃度：12/13（92% ≥80%）；megadose/holehe 702 天不活跃
- 与昨日（08-12 周三）重叠：3 重叠 / 10 新条目

## 池约束说明

### 1. 近 2 天 ai-wind 已入选（禁选）
- 08-12 周三：stablyai/orca / HKUDS/DeepTutor / paperclipai/paperclip / addyosmani/agent-skills / anthropics/skills
- 08-10 周一：msitarzewski/agency-agents / Comfy-Org/ComfyUI / ZhuLinsen/daily_stock_analysis / harveyai/harvey-labs
- 今日 raw 命中：msitarzewski/agency-agents / anthropics/skills（均禁选）

### 2. 子方向筛选（跨 AI 子方向 ≥3）

今日 13 AI 项目，规避：
- 同方向重复：kepano/obsidian-skills（Agent 技能，与昨日 anthropics/skills 重复）
- 偏开发者中间件：NVIDIA-NeMo/Switchyard（LLM 路由）
- 昨日 daily 已覆盖"本地离线"主题：holaboss-ai/holaOS / Lightricks/LTX-2 / lightningpixel/modly / altic-dev/FluidVoice（方向重复，避免两榜同日撞）

入选 5 个跨子方向：
- macro-inc/macro（AI 工作区，+1239 当日最高）
- cactus-compute/needle（端侧小模型，+769 加速）
- unslothai/unsloth（本地大模型，71K 总星）
- infiniflow/ragflow（RAG 引擎，88K 总星）
- semantica-agi/semantica（图谱基建，+713 加速）

### 3. 最终入选（5 项目，跨 5 子方向）

| 项目 | 子方向 | 受众 | 总星 | 今日 |
|------|--------|------|------|------|
| macro-inc/macro | AI 工作区 | A | 2.6K | +1239 |
| cactus-compute/needle | 端侧小模型 | B | 4.9K | +769 |
| unslothai/unsloth | 本地大模型 | A | 71K | +328 |
| infiniflow/ragflow | RAG 引擎 | B | 88K | +465 |
| semantica-agi/semantica | 图谱基建 | C | 6.6K | +713 |

## 真实性核验（gh api）

| 项目 | created | watchers | 星叉比 | 判定 |
|------|---------|----------|--------|------|
| macro-inc/macro | 2025-11 | 44 | 9.4:1 | ✅ |
| cactus-compute/needle | 2026-02 | 33 | 14.8:1 | ✅ |
| unslothai/unsloth | 2023-11 | 369 | 11.1:1 | ✅ |
| infiniflow/ragflow | 2023-12 | 368 | 8.5:1 | ✅ |
| semantica-agi/semantica | 2025-06 | 42 | 9.5:1 | ✅ |

0 HARD 命中。

## 选题说明

本期主题"AI 落地基建"，跨 5 子方向（工作区/端侧/本地模型/RAG/图谱），覆盖 AI 应用全栈。与昨日 ai-wind（智能体工程化：用→管→装技能）+ 昨日 daily（本地离线 AI）题材错开。今日 daily 综合因非 AI 池枯竭跳过，ai-wind 正常承接 AI 内容。
