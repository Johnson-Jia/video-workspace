# 内容摘要

## 来源
分类数据（GitHub Trending daily，2026-08-05），`raw_trending.json` 18 个项目（python_requests + gh_api 双源交叉验证，cache_warning=false，活跃度达标）。avatar 已预下载至 `assets/avatars/`。

## 核心主题
8 月 5 日 GitHub 日榜：daily 回归多元——2 AI + 3 非 AI 跨 5 方向。主推 26 万星 superpowers（不是 AI 模型，是教 AI 干活的方法论框架，反直觉钩子核心），配 JS/TS 运行时 deno、CSS 框架 tailwindcss、企业 AI 安全 uber/ADR，PDF 智能分类库 pdf-inspector 因今日 top1 爆款一句带过增量。避开近 2 天 daily 已选项目，AI 深度交同日 ai-wind 专项承接。

## 选材决策（gate 真相驱动，AI≤2 + 单项目近 2 天禁连续 双新约束）
- **ai_project_cap（AI≤2）**：旧版选 superpowers/uber-ADR/livekit（3 个 AI，livekit topics 含 ai/agents）超 cap，本期去掉 livekit，留 superpowers+uber-ADR 共 2 AI，补 pdf-inspector/deno/tailwindcss 共 3 非 AI。
- **project_no_consecutive_repeat（近 2 天禁连续）**：08-04 daily 已选 airllm/ds4/voicebox/pdf-inspector/DeepSeek-Reasonix/kaneo，08-03 daily 已选 Agent-Reach/reverse-skill/TencentDB-Agent-Memory/build-your-own-x 等。本期 superpowers/deno/tailwindcss/uber-ADR 近 2 天均未选（全新鲜）；pdf-inspector 08-04 选过但今日 stars_today +2524 为 raw 第 1，进 top3 exempt 白名单，例外一句带过增量不展开。
- **排除敏感**：raw 涨幅第 2 的逆向/授权渗透测试项目（平台敏感零容忍剔除）。
- **audience_filter**：今日 raw 客观无 GUI 类 A 档（开发者基建/框架为主）。A 档 0、B 档 2（superpowers/deno）、C 档 3（pdf-inspector/tailwindcss/uber-ADR）。C 档超 1/3 引导值系客观构成，C 档文案措辞「给做 XX 的开发者」定调。

## 关键信息点
- superpowers：26 万星不是某个工具，而是把「AI 编程怎么干才靠谱」沉淀成可复用技能 + 方法论框架（subagent-driven development，子代理分工干开发流程）。反直觉主推：人教 AI 干活。
- deno：面向 JS/TS 的现代运行时，Node 之后的下一代基建，默认安全沙箱、原生 TS。
- tailwindcss：utility-first CSS 框架，前端快速搭界面的事实标准之一。
- uber/ADR：可观测 + 安全基准 + 威胁检测，Uber 生产环境盯着 AI agent 别乱来（企业 AI 安全）。
- pdf-inspector：Rust 写的 PDF 检查/分类/提取库，一眼识别扫描件 vs 文本件智能路由（今日 top1 涨星 +2524）。

## 数据（raw_trending.json，gh API 实时）
1. obra/superpowers | Shell | 266431★ (+777) | agentic skills 框架 + 软件开发方法论
2. denoland/deno | Rust | 108047★ (+27) | JS/TS 现代运行时
3. tailwindlabs/tailwindcss | TypeScript | 96445★ (+30) | utility-first CSS 框架
4. uber/ADR | Python | 656★ (+140) | 企业 AI agent 安全，Uber 部署
5. firecrawl/pdf-inspector | Rust | 9908★ (+2524) | Rust PDF 检查/分类/提取库（今日 top1 涨星）

## 原始素材路径
`raw_trending.json`、`assets/avatars/`
