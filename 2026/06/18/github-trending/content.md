# 内容摘要

## 来源
分类数据（GitHub Trending，python_requests + gh_api 三源验证，2026-06-18 daily 模式）

## 核心主题
6 月 18 日 GitHub 涨星最猛的 6 个开源项目，覆盖 AI 代码智能、开发者技能、AI agent 全网抓取、安卓隐私工具、开源设计、项目管理六个方向。强钩子：codebase-memory-mcp 把 AI 看代码的输入砍掉 99%。

## 关键信息点
- **钩子担当（反直觉）**：codebase-memory-mcp —— 高性能代码智能 MCP，把代码库索引成知识图谱，AI 输入省 99% token、查询亚毫秒
- **涨幅王**：mattpocock/skills 单日 +1523 —— 资深工程师的 skills 集合（直接来自作者 .claude 目录）
- **涨幅第二**：Agent-Reach +1161 —— 给 AI agent 装眼睛看全网（Twitter/Reddit/YouTube/GitHub/B 站/小红书），一个 CLI 零 API 费
- **A 档普通人可用 ×3**：
  - Universal-Debloater —— 免 root 清理安卓预装的 GUI（Rust 写，提升隐私/安全/续航）
  - penpot —— 开源设计工具，设计与代码协作
  - plane —— 开源项目管理平台，任务/迭代/文档/分流
- **受众配比**：A 档 3 个约占半、B 档 2 个、C 档 1 个（满足受众筛选门禁，非纯库扎堆）

## 数据
- 数据源：raw_trending.json（20 项目，活跃度 90%，16 新条目不重复昨日）
- 真实性验证：6/6 通过 gh API HARD（star/fork 比 11–23:1、watcher 充足、owner 账号 ≥2.5 年、README 充足、0 剔除补选）
- 选取项目（详见 content_ready.txt）：
  - DeusData/codebase-memory-mcp: 5.4K★ (+371)
  - mattpocock/skills: 133.7K★ (+1523)
  - Panniantong/Agent-Reach: 33.3K★ (+1161)
  - Universal-Debloater-Alliance/universal-android-debloater-next-generation: 7.7K★ (+457)
  - penpot/penpot: 50.1K★ (+70)
  - makeplane/plane: 51.3K★ (+89)

## 原始素材路径
- `raw_trending.json` — 原始 trending 数据（含 description / avatar / topics / stars）
- `content_ready.txt` — 6 项目详细整理（中文忠实翻译 + 内嵌原文 description + avatar + 用途 + 受众分档）
- `assets/avatars/` — owner 头像（圆形裁剪，已下载 20 个）
