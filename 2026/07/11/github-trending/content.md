# 内容摘要

## 来源
分类数据：GitHub Trending 2026-07-11 daily 模式（raw_trending.json，python_requests + gh API 双源交叉验证，19 项目，cache_warning=false）

## 核心主题
今日 GitHub Trending 换到开发者基石层：JS 运行时（bun）、网络互联（tailscale）、基础设施代码（terraform）、AI 编程配置（mattpocock/skills）、AI 终端控制（DesktopCommanderMCP）、前端框架（next.js）。这些是上层应用的地基——普通人触不到，但每天都在用它们造的东西。

## 关键信息点
- mattpocock/skills：TypeScript 教育界名人 Matt Pocock 把自己 .claude 目录的 AI 编程 skills 开源，今日涨星榜首 +1663，总 16.4 万星（mit 协议）
- wonderwhy-er/DesktopCommanderMCP：给 AI 助手装上终端控制 + 文件搜索 + 差异编辑能力的 MCP server，今日 +349，总 7253 星
- oven-sh/bun：Rust 写的 JS 运行时，运行时/打包/测试/包管理四合一，今日 +307，总 9.4 万星
- tailscale/tailscale：基于 WireGuard 的 VPN，号称最简单最安全的组网方式，今日 +183，总 3.3 万星
- vercel/next.js：React 框架事实标准，今日 +176，总 14 万星，9 年老牌仍在快速迭代
- hashicorp/terraform：基础设施即代码鼻祖，用配置文件管理云资源，今日 +168，总 4.9 万星，11 年老牌

## 数据（gh API 复核，2026-07-11）
| owner/repo | 今日涨星 | 总星 | forks | watchers | 创建 | 协议 |
|------------|---------|------|-------|----------|------|------|
| mattpocock/skills | +1663 | 164567 | 14161 | 958 | 2026-02 | MIT |
| wonderwhy-er/DesktopCommanderMCP | +349 | 7253 | 925 | 111 | 2024-12 | MIT |
| oven-sh/bun | +307 | 94196 | 4938 | 681 | 2021-04 | NOASSERTION |
| tailscale/tailscale | +183 | 33627 | 2910 | 266 | 2020-01 | BSD-3-Clause |
| vercel/next.js | +176 | 140688 | 31523 | 1669 | 2016-10 | MIT |
| hashicorp/terraform | +168 | 49151 | 10672 | 1282 | 2014-03 | NOASSERTION（BSL 1.1） |

## 真实性验证结论
6 项目全部 0 HARD 0 警告（watcher%/forks/star 比例均健康），全部保留。

## 排除记录
- addyosmani/agent-skills（+1114，07/08 已展开 + AI agent skills 题材饱和）
- obra/superpowers（+969，07/07 已展开）
- iOfficeAI/OfficeCLI（+1210，07/08+07/09 连续两期展开，严重疲劳）
- TencentCloud/TencentDB-Agent-Memory（+134，07/07 饱和）
- abseil/abseil-cpp、jbeder/yaml-cpp、catchorg/Catch2、chriskohlhoff/asio、zeux/meshoptimizer、grpc/grpc（C 档纯开发者库低增量）
- microsoft/TypeScript（+166，C 档语言实现，JS 生态已有 bun/next.js 代表，避免扎堆）
- davila7/claude-code-templates、google-labs-code/stitch-skills（与 mattpocock/skills 题材邻近，择一不重复）
- ruvnet/RuView（永久排除列表）

## 原始素材路径
- raw_trending.json：workspace/2026/07/11/github-trending/raw_trending.json
- gh API 复核数据：见 verification_notes（topic_plan.json）
