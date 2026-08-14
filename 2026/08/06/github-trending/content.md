# 内容摘要

## 来源
GitHub Trending daily（2026-08-06）三源交叉验证：Python requests 抓取 + gh API enrichment（13/13 verified，92% 活跃）

## 核心主题
今日 GitHub 热门：AI agent 工具持续主导（cloudflare 让 agent 拥有计算机、TencentDB 团队记忆中枢），叠加 Rust PDF 解析与 React 框架的多元工具。AI≤2 硬约束下，2 个最热 AI + 2 个非 AI 工具/基建组合。

## 关键信息点（4 项目）

### 1. cloudflare/computer（钩子项目，rank1）
- "Give your agent a computer" — 给智能体一台电脑
- 让 AI 智能体拥有可操作的完整计算机环境
- TypeScript，今日 +796 ★，总 2.7K ★（新项目快速起量）
- 反直觉钩子：不是给 AI 模型，是给 AI 一台"电脑"

### 2. TencentCloud/TencentDB-Agent-Memory（今日最热）
- AI 智能体团队级记忆中枢（team-level memory hub for AI Agents）
- 把对话/文档/代码转成四种可复用记忆（Chat Memory/Skill/LLM-Wiki/Code-Graph）
- 跨智能体、跨框架共享与治理
- TypeScript，今日 +1891 ★（今日榜单最高），总 15K ★

### 3. firecrawl/pdf-inspector（非 AI，Rust 工具）
- 快速 Rust PDF 解析库（Fast Rust library for PDF inspection）
- 自动识别扫描版 vs 文本版 PDF，智能路由
- Rust，今日 +1583 ★，总 11K ★（连续两日高热度）

### 4. vercel/next.js（非 AI，前端框架）
- React 开发框架（The React Framework）
- 服务端渲染 + 静态生成通用方案
- JavaScript，今日 +144 ★，总 141K ★（常青框架）

## 数据
- 今日榜单 13 项目，92% 活跃（donnemartin/system-design-primer 138天未push 剔除）
- AI 项目占比高（约 9/13），ai_project_cap≤2 下精选 2 AI + 2 非 AI
- 今日 stars_today 前 3：TencentDB +1891 / pdf-inspector +1583 / superpowers +931

## 选材约束（已遵守）
- ai_project_cap：选 2 AI（computer + TencentDB）≤2 ✓
- project_no_consecutive_repeat：避 08-05 选过的 superpowers/uber-ADR/tailwindcss/deno；pdf-inspector 08-05 选过但今日 +1583 进前3豁免
- 题材多元：AI agent（computer/TencentDB）+ 文档工具（pdf-inspector）+ 前端基建（next.js）

## 原始素材路径
raw_trending.json（13 项目三源验证）
