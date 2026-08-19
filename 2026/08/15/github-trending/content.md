# 内容摘要

## 来源
分类数据（github trending daily，raw_trending.json 2026-08-15 采集：python_requests+gh_api，17 项目）+ gh api 实时核验

## 核心主题
换掉闭源/付费工具——视频剪辑与远程桌面两大日常付费场景的开源平替（OpenCut/rustdesk）打头阵，叠加 GitHub 官方规格驱动开发工具包 spec-kit 与给 AI 智能体用的浏览器 ego-lite，创作者+开发者双受众。

## 关键信息点
- OpenCut：开源视频剪辑工具，浏览器打开就能剪，83.1K★（+238 单日），A 档普通可用
- rustdesk：开源远程桌面，支持自托管，全平台客户端，120.6K★（+182 单日），A 档普通可用
- spec-kit：GitHub 官方出品，规格驱动开发（先写规格再让 AI 写码）工具包，128.5K★（+1147 单日，今日涨幅榜前列），B 档开发者向
- ego-lite：给 AI 智能体的浏览器自动化，可共享已登录浏览器状态、不打扰本人，10.3K★（+153 单日），B 档开发者向
- 选题主线「付费场景→开源平替」，双 A 档平替项目作双主角（合计总星约 20.4 万，hook 数字锚点）

## 数据
| 项目 | 语言 | 总星 | 单日 | 受众 |
|------|------|------|------|------|
| OpenCut-app/OpenCut | TypeScript | 83.1K | +238 | A |
| rustdesk/rustdesk | Rust | 120.6K | +182 | A |
| github/spec-kit | Python | 128.5K | +1147 | B |
| citrolabs/ego-lite | JavaScript | 10.3K | +153 | B |

AI 占比 2/4（spec-kit/ego-lite，≤2 上限内；避开昨日 ai-wind 已讲 5 个 AI 项目）。与近2天已选 9 项目零重复。

## 池约束说明（ToolJet 落选）
team-lead 原拟 5 项目含 ToolJet/ToolJet，但 gate `_is_ai_project` 实测判定其为 AI（raw 描述原文含 "ToolJet AI"/"AI agents" 命中 \bAI\b），5 选组合 ai_project_cap 必 HARD 失败（3>2）且无创意轨修复路径（描述保真门禁强制内嵌原文）。已上报 team-lead，按推荐去掉 ToolJet 做 4 项目。raw 中非禁选非 AI 替代仅 cursor/plugins（+69，C 档规范文档，Cursor 品牌名风险）与 deepseek-ai/awesome-deepseek-agent（描述为空，DeepSeek 品牌名），均不达标，不硬凑。gate 实测 4 项目组合：AI 2≤2 ✓ 总数 4≥4 ✓ 非AI 2≥2 ✓。

## 原始素材路径
D:/AI-Agent/video-clipforge/workspace/2026/08/15/github-trending/raw_trending.json
