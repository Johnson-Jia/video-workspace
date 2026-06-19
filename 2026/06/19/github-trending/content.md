# 内容摘要

## 来源
分类数据（GitHub Trending，python_requests + gh_api 三源验证，2026-06-19 daily 模式）

## 核心主题
6 月 19 日 GitHub 杀入 6 个开源项目，覆盖 安卓隐私清理、本地翻译、API 调试、AI 代码智能、国产大模型、时间序列预测 六个方向。强钩子：codebase-memory-mcp 把 AI 看代码的输入砍掉 99%（今日单日涨星 +2308，榜单单日涨幅居首）。

## 关键信息点
- **钩子担当（反直觉 + 数字）**：DeusData/codebase-memory-mcp —— 把代码库索引成知识图谱，AI 查询省 99% token，今日 +2308 涨星居首
- **A 档普通人可用 ×3**（约占一半，满足受众筛选门禁）：
  - Universal-Debloater —— 免 root 清理安卓预装的 GUI（Rust 写，提升隐私/安全/续航）
  - LibreTranslate —— 开源翻译 API，可自托管离线，数据不外传
  - Kong/insomnia —— 开源 API 客户端 GUI，免费 Postman 替代品
- **B 档 ×2**：zai-org/GLM-5（智谱新模型，vibe coding→agentic）、google-research/timesfm（Google 时间序列预测模型）
- **受众配比**：A 档 3 个约占半、B 档 2 个、C 档 1 个（非纯库扎堆）

## 数据
- 数据源：raw_trending.json（17 项目，活跃度 94%，与昨日 7 重叠 10 新，Fresh 非缓存）
- 真实性验证：6/6 通过 gh API HARD（star/fork 比 9-23:1 正常、watcher 均>30、owner 账龄均>90 天、仓库体积充足，0 剔除补选）
- 选取项目（详见 content_ready.txt）：
  - DeusData/codebase-memory-mcp: 7.0K★ (+2308)
  - Universal-Debloater-Alliance/universal-android-debloater-next-generation: 7.9K★ (+247)
  - LibreTranslate/LibreTranslate: 15.0K★ (+83)
  - Kong/insomnia: 38.7K★ (+13)
  - zai-org/GLM-5: 4.1K★ (+286)
  - google-research/timesfm: 23.1K★ (+858)

## 原始素材路径
- `raw_trending.json` — 原始 trending 数据（含 description / avatar / topics / stars）
- `content_ready.txt` — 6 项目详细整理（中文忠实翻译 + 内嵌原文 description + avatar + 用途 + 受众分档）
- `assets/avatars/` — owner 头像（圆形裁剪，已下载）
