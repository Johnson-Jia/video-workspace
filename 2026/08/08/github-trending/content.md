# 内容摘要

## 来源
分类数据：github-trending daily（2026-08-08，raw_trending.json 17 项目），gh API 真实性验证 + README 调研

## 核心主题
2026-08-08 GitHub 热门盘点：以单日涨星最多的「会自进化的编码 agent」(prime-agent, +2271) 为数字锚钩子，搭配群体智能预测引擎 (MiroFish)、进程追根溯源 (witr)、开发环境一统 (mise)、自托管分布式基建 (celld)。AI ≤ 2，5 个方向互不重叠，与 8-7「多元基建回归」主动差异化。

## 关键信息点
- **prime-agent**（AI）：self-improving RLM agent，harness 能 `/refine` 自我精炼经验/技能（不改基础 prompt，可回滚），子 agent 并行，长任务不断片。单日 +2271（当日涨星第 1）
- **MiroFish**（AI）：群体智能预测引擎，多 agent 在数字沙盘里互动涌现「预测万物」，浏览器有在线 demo，70.5K 星，盛大背书
- **witr**（非 AI）：进程/端口/容器/文件追根溯源 CLI+TUI，一句命令追出「族谱」，19.7K 星
- **mise**（非 AI）：Rust 写的开发环境一统工具（运行时版本 + 环境变量 + 任务脚本），32K 星，知名维护者 jdx
- **celld**（非 AI）：deno 团队开源的自托管分布式 Durable Objects，把大厂云端状态化对象搬回自家服务器，+546

## 数据（核心指标）
| 项目 | 今日涨星 | 总星 | 语言 | 受众档 |
|------|---------|------|------|--------|
| PrimeIntellect-ai/prime-agent | +2271 | 6.4K | TypeScript | C |
| 666ghj/MiroFish | +126 | 70.5K | Python | A（demo） |
| pranshuparmar/witr | +308 | 19.7K | Go | B |
| jdx/mise | +130 | 32K | Rust | B |
| denoland/celld | +546 | 2.2K | Rust | C |

AI 占比：2/5（≤2 合规）。受众：A=1 / B=2 / C=2（受 raw 非 AI 偏基建工具限制，A 档取 MiroFish demo）。

## 差异化（对照 8-7）
- 8-7 hook「四个项目杀入榜单，一半不是 AI」→ 本期「单日涨两千七，这 AI 能自己进化」（数字锚 + 反直觉，完全换主题）
- 8-7 结尾「你会用上哪个」→ 本期「你最想试哪个」（动词轮换）
- 项目集 0 重复（guava/authentik 等 9 个近 2 天项目全规避）

## 原始素材路径
raw_trending.json / avatars: assets/avatars/

---
## 选材记录（移出 content_ready 避 description_fidelity gate 误判，泛化不用 owner/repo 格式）
- ⛔ 近2天禁选（项目重复 gate）：guava / authentik / cloudflare-computer / code-review-graph / loopx / pdf-inspector / tencentdb / next.js / superpowers
- ⚠️ 剔除：Legendary_OSINT（inactive 112 天，违反活跃度门禁）
- ⚠️ 弃选：grok2api（含 Grok/xAI 品牌）；agent-skills / mattpocock-skills / google-skills（AI 编码技能同质 + AI 超 cap）；swarm-forge / AutoGPT / semantica（AI 超 cap）
