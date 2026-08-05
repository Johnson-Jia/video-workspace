# 内容摘要

## 来源
分类数据（GitHub Trending daily，2026-08-04，raw_trending.json 16 个项目，三源交叉验证 + gh API enrichment + avatar 已下载）

## 核心主题
8月4日 GitHub 日榜，本地大模型推理成最大看点：4G 显存就能跑 700 亿参数大模型；辅以开源 AI 语音工作室、Rust PDF 解析、终端 AI 编程 agent、antirez 新推理引擎，题材跨"本地推理+语音+文档+编程+项目管理"五方向。

## 关键信息点
- **airllm（lyogavin/airllm）**：单 4GB 显存 GPU 跑 70B（700亿参数）大模型推理，反直觉——打破"跑大模型要几十G显存"的常识。Jupyter Notebook 形式，浏览器/Colab 可跑。今日 +1085★，总 27K★。
- **ds4（antirez/ds4）**：大模型本地推理引擎，同时支持苹果 Metal、N卡 CUDA、A卡 ROCm 三大平台。作者 antirez 是 Redis 作者（知名开源 handle）。C 语言编写，总 20K★。
- **voicebox（jamiepine/voicebox）**：开源 AI 语音工作室，三大能力——声音克隆、语音听写、内容创作。桌面 GUI 应用，普通人可用。总 48K★（最高总星）。
- **pdf-inspector（firecrawl/pdf-inspector）**：Rust 编写的 PDF 解析库，做 PDF 检查、分类、文本提取，能智能识别扫描件 vs 文本件做路由。firecrawl 出品。今日 +1699★（今日涨幅第二）。
- **DeepSeek-Reasonix（esengine/DeepSeek-Reasonix）**：终端里的 AI 编程 agent，围绕前缀缓存（prefix-cache）稳定性设计，能常驻后台一直跑不崩。Go 编写。总 29K★。
- **kaneo（usekaneo/kaneo，连续霸榜）**：开源项目管理工具，只留你需要的、不臃肿，web app 可自部署。08-02/08-03 已介绍，今日快速带过增量。今日 +665★。

## 数据
| 项目 | 今日涨星 | 总星 | 语言 | 受众 |
|------|---------|------|------|------|
| firecrawl/pdf-inspector | +1699 | 8.2K | Rust | C 开发者向 |
| lyogavin/airllm | +1085 | 27.1K | Jupyter Notebook | A 浏览器即开 |
| esengine/DeepSeek-Reasonix | +883 | 29.9K | Go | B 半可用 |
| usekaneo/kaneo | +665 | 6.8K | TypeScript | A 普通可用 |
| antirez/ds4 | +384 | 20.3K | C | B 半可用 |
| jamiepine/voicebox | +412 | 48.6K | TypeScript | A 普通可用 |

## 原始素材路径
- `raw_trending.json`（16 个项目，已三源交叉验证 + gh API enrichment）
- `assets/avatars/{owner}.png`（avatar 已预下载）
