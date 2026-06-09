# 2026年6月第23周 GitHub 热门开源项目盘点

> 本周 GitHub 涨星总数超过 9.3 万，AI Agent 生态持续爆发——从 Agent 性能优化、设计语言到记忆引擎，一条完整的 Agent 开发链正在成形。同时，LLM Token 压缩器 headroom 以单周 +14,272 星登顶，成为本周最大黑马。

## 本周趋势速览

| 趋势 | 说明 |
|------|------|
| 最大赢家 | [headroom](https://github.com/chopratejas/headroom) 单周 +14,272 星，LLM Token 压缩赛道爆发 |
| 新面孔 | MoneyPrinterTurbo、taste-skill、oh-my-pi、impeccable 等 8 个项目首次进入周榜 |
| 持续热门 | headroom、ECC 连续 4 天日榜在线；trivy 稳定 4 天，安全扫描持续受关注 |
| 关键词 | Agent 生态、Token 压缩、AI 记忆、跨平台搜索 |

---

## 一、AI Agent 生态

Agent 开发不再只是"写个 Prompt"，围绕 Agent 的性能优化、设计美学、技能管理和前端交互，一整套工具链正在成熟。

### 1. [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)

**项目简介：** hermes-agent 是 NousResearch 推出的通用 AI Agent 框架，定位为"与你一起成长的 Agent"。它不仅是一个对话工具，更是一个可以持续学习、积累技能的智能体平台，支持多种大语言模型后端。

**核心亮点：**
- 支持多模型后端（Anthropic Claude、OpenAI 等），用户可按需切换
- 内置技能系统，Agent 可通过学习不断扩展能力边界
- 与 Claude Code、Codex、OpenClaw 等主流开发工具深度集成
- 活跃的开源社区，Open Issues 超过 19,000 个，反映生态高速迭代

**快速上手：**

```bash
pip install hermes-agent
hermes init
hermes chat
```

**适合人群：** AI Agent 开发者、自动化工作流搭建者

> Star: 186,521 | Fork: 32,086 | 协议: MIT | 语言: Python | 本周涨幅: +11,427 | 连续日榜: 3 天

### 2. [affaan-m/ECC](https://github.com/affaan-m/ECC)

**项目简介：** ECC 是一个面向 AI Agent 的性能优化系统，提供技能（Skills）、本能（Instincts）、记忆（Memory）、安全（Security）四大模块，为 Claude Code、Codex、Cursor 等编程 Agent 注入更强的工程能力。

**核心亮点：**
- 四维优化体系：技能扩展、行为本能、持久记忆、安全护栏
- 兼容多个主流 Agent 框架，零配置即可使用
- 社区贡献了大量预设技能包，覆盖代码审查、测试生成、文档编写等场景
- 总 Star 突破 21 万，是本周总星数最高的项目

**快速上手：**

```bash
# 在 Claude Code 中直接安装
claude skill add affaan-m/ECC
```

**适合人群：** Claude Code / Cursor 用户、AI 辅助编程爱好者

> Star: 210,176 | Fork: 32,233 | 协议: MIT | 语言: JavaScript | 本周涨幅: +10,207 | 连续日榜: 4 天

### 3. [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)

**项目简介：** taste-skill 解决了一个被忽视但极其关键的问题——AI 生成的代码和设计"缺乏品味"。它通过注入设计原则和审美规则，让 AI Agent 的输出从"能用"升级为"精致"。

**核心亮点：**
- 内置前端设计美学规则库，覆盖间距、配色、排版、动效等维度
- 拦截 AI 生成的"无聊、通用、平庸"输出，强制提升质量
- 适用于 Claude Code、Codex 等主流 Agent，Shell 脚本即安装
- 对 Vibe Coding 场景特别有效——让零设计基础的开发者也能产出专业级 UI

**快速上手：**

```bash
# 一键安装到 Claude Code
claude skill add Leonxlnx/taste-skill
```

**适合人群：** 前端开发者、Vibe Coding 爱好者

> Star: 37,543 | Fork: 2,681 | 协议: MIT | 语言: Shell | 本周涨幅: +6,385

### 4. [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi)

**项目简介：** oh-my-pi 是一个面向终端的 AI 编程 Agent，核心理念是"hash-anchored edits"——通过精确的哈希定位实现代码编辑，减少 AI 误改的风险。同时集成了 LSP、浏览器、子代理等能力。

**核心亮点：**
- Hash-anchored 编辑机制：AI 修改前精确定位代码行，避免误操作
- 内置 LSP 支持，代码补全和跳转体验接近 IDE
- 支持子代理（subagent）架构，复杂任务可自动拆分
- Rust + TypeScript 双语言架构，性能与可扩展性兼顾

**快速上手：**

```bash
npm install -g oh-my-pi
omp chat
```

**适合人群：** 偏好终端工作流的开发者、AI 辅助编程深度用户

> Star: 11,164 | Fork: 943 | 协议: MIT | 语言: TypeScript | 本周涨幅: +2,117

### 5. [revfactory/harness](https://github.com/revfactory/harness)

**项目简介：** harness 是一个"元技能"（meta-skill），它不是直接帮你写代码，而是帮你设计 Agent 团队。你描述一个领域的需求，它自动生成该领域的专业化 Agent 编队和对应的技能配置。

**核心亮点：**
- 输入领域描述，输出完整的 Agent 团队方案（角色定义 + 技能分配）
- 适用于 Claude Code 的 skill 体系，生成的配置可直接使用
- 支持多 Agent 协作编排，覆盖需求分析、代码实现、测试验证等环节
- "元技能"概念新颖——用 AI 来设计 AI 的组织架构

**快速上手：**

```bash
claude skill add revfactory/harness
/harness "构建一个电商系统的后端开发团队"
```

**适合人群：** Agent 架构师、Claude Code 高级用户

> Star: 6,478 | Fork: 881 | 协议: Apache-2.0 | 语言: HTML | 本周涨幅: +1,958

### 6. [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin)

**项目简介：** Compound Engineering 官方出品的工程化插件，为 Claude Code、Codex、Cursor 等工具注入系统化的工程实践——包括代码规范、审查流程、部署策略等。

**核心亮点：**
- 将企业级工程实践封装为可复用的 Agent 插件
- 支持多平台：Claude Code、Codex、Cursor 统一体验
- 内置 PRD 生成、代码审查、变更管理等工程流程模板
- 由 Compound 团队持续维护，更新频率高

**快速上手：**

```bash
npm install -g compound-engineering-plugin
compound init
```

**适合人群：** 追求工程化 AI 编程的团队和个人

> Star: 20,485 | Fork: 1,514 | 协议: MIT | 语言: TypeScript | 本周涨幅: +1,762

### 7. [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui)

**项目简介：** hermes-webui 为 hermes-agent 提供了网页端和移动端的图形界面，让用户无需命令行即可与 Agent 交互。支持对话历史、技能管理、多会话切换等功能。

**核心亮点：**
- 响应式设计，PC 和手机浏览器均可流畅使用
- 完整的对话管理：历史回溯、会话分类、上下文保持
- 与 hermes-agent 后端无缝对接，支持所有 Agent 能力
- Python + FastAPI 后端，部署简单

**快速上手：**

```bash
git clone https://github.com/nesquena/hermes-webui.git
cd hermes-webui
pip install -r requirements.txt
python app.py
```

**适合人群：** hermes-agent 用户、需要 Web 端管理 AI Agent 的团队

> Star: 13,924 | Fork: 1,712 | 协议: MIT | 语言: Python | 本周涨幅: +4,281 | 连续日榜: 2 天

---

## 二、AI 效率工具

从 Token 压缩到文件格式转换，从 AI 记忆到跨平台信息搜索，这组项目聚焦于"让 AI 用起来更高效"。

### 8. [chopratejas/headroom](https://github.com/chopratejas/headroom)

**项目简介：** headroom 是本周涨星最猛的项目（+14,272）。它解决了一个 AI 开发中的核心痛点：**LLM 的 Token 消耗太大**。headroom 可以将工具输出、日志文件、RAG 检索块等文本压缩 60-95%，压缩后的大语言模型回答质量几乎不受影响。

**核心亮点：**
- 三种使用方式：Python 库（pip install）、HTTP 代理服务器、MCP Server
- 压缩比高达 95%，实测对问答准确率影响小于 2%
- 支持 Claude Code、Cursor、LangChain 等主流 Agent 框架
- 对长日志分析、大文件摘要等场景效果显著，直接削减 API 成本

**快速上手：**

```python
from headroom import compress

compressed = compress("your long text here...", ratio=0.85)
# 原文 1000 token → 压缩后 150 token
```

或作为 MCP Server 使用：

```bash
pip install headroom
headroom serve --port 8080
```

**适合人群：** AI 应用开发者、RAG 系统搭建者、Token 成本敏感的团队

> Star: 17,434 | Fork: 1,110 | 协议: Apache-2.0 | 语言: Python | 本周涨幅: +14,272 | 连续日榜: 4 天

### 9. [microsoft/markitdown](https://github.com/microsoft/markitdown)

**项目简介：** 微软出品的文件格式转换工具，能将 Word、Excel、PowerPoint、PDF、HTML、图片等各类文件一键转为 Markdown 格式。对于需要将文档喂给大语言模型的场景，这是一个必备的前处理工具。

**核心亮点：**
- 支持几乎所有主流文件格式：.docx、.xlsx、.pptx、.pdf、.html、.png 等
- 转换结果保留标题层级、表格结构、列表格式等语义信息
- 微软官方维护，对 Office 文档的解析准确率极高
- CLI 和 Python API 双模式，可集成到任何自动化流程

**快速上手：**

```bash
pip install markitdown
markitdown document.pdf > output.md
```

Python API：

```python
from markitdown import MarkItDown

md = MarkItDown()
result = md.convert("presentation.pptx")
print(result.text_content)
```

**适合人群：** RAG 开发者、文档处理自动化工程师

> Star: 147,777 | Fork: 10,129 | 协议: MIT | 语言: Python | 本周涨幅: +13,359 | 连续日榜: 2 天

### 10. [supermemoryai/supermemory](https://github.com/supermemoryai/supermemory)

**项目简介：** supermemory 是一个面向 AI 应用的记忆引擎，提供高速、可扩展的 Memory API。它让 AI Agent 拥有"长期记忆"能力，不再每次对话都从零开始，而是能记住用户偏好、历史交互和领域知识。

**核心亮点：**
- Memory API 设计，支持增删改查和语义检索
- 基于 Cloudflare Workers + PostgreSQL 的分布式架构，响应极快
- 适用于个人知识管理、AI 助手、客服机器人等场景
- 提供完整的 Web UI，可视化管理和检索记忆条目

**快速上手：**

```bash
git clone https://github.com/supermemoryai/supermemory.git
cd supermemory
npm install && npm run dev
```

**适合人群：** AI Agent 开发者、需要为 AI 添加持久记忆能力的团队

> Star: 26,088 | Fork: 2,276 | 协议: MIT | 语言: TypeScript | 本周涨幅: +2,924 | 连续日榜: 2 天

### 11. [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook)

**项目简介：** open-notebook 是 Google NotebookLM 的开源替代方案，提供了更灵活的功能和完全的数据自主权。用户可以将文档、网页、音频等材料导入，由 AI 生成摘要、问答和学习笔记。

**核心亮点：**
- 支持多种输入源：PDF、网页 URL、音频文件、手动粘贴文本
- AI 驱动的摘要生成、问答对话、知识点提取
- 完全本地部署，数据不离开你的服务器
- TypeScript + React 技术栈，前端体验流畅

**快速上手：**

```bash
git clone https://github.com/lfnovo/open-notebook.git
cd open-notebook
npm install && npm run dev
```

**适合人群：** 知识工作者、学生、需要私有化 AI 学习工具的团队

> Star: 27,616 | Fork: 3,124 | 协议: MIT | 语言: TypeScript | 本周涨幅: +2,993 | 连续日榜: 3 天

### 12. [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill)

**项目简介：** last30days-skill 是一个 AI Agent 技能，能自动跨多个平台（Reddit、X/Twitter、YouTube、Hacker News、Polymarket 等）研究任何话题，并综合输出一份有据可查的摘要报告。

**核心亮点：**
- 单条命令即可启动跨平台研究，覆盖社交媒体、新闻、社区等 10+ 个信息源
- 输出结构化摘要，包含来源链接、关键观点、趋势分析
- 支持 Claude Code 技能体系，可作为 Agent 的研究能力模块
- 对"了解一个新领域"、"追踪行业动态"等场景非常实用

**快速上手：**

```bash
claude skill add mvanhorn/last30days-skill
/last30days "Rust 在嵌入式开发中的最新进展"
```

**适合人群：** 研究人员、产品经理、需要快速了解新领域的技术人

> Star: 32,372 | Fork: 2,680 | 协议: MIT | 语言: Python | 本周涨幅: +2,718 | 连续日榜: 3 天

### 13. [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)

**项目简介：** Agent-Reach 让 AI Agent 拥有"阅读全网"的能力——支持 Twitter、Reddit、YouTube、GitHub、B站、小红书等平台的搜索和内容提取，全部通过 CLI 完成，无需任何 API Key。

**核心亮点：**
- 零 API 费用：不依赖各平台的付费 API，直接爬取公开内容
- 国内平台支持：B站、小红书等中文平台一应俱全
- CLI 设计，可轻松集成到任何 Agent 工作流
- 支持 Claude Code、Cursor 等工具的 MCP 协议

**快速上手：**

```bash
pip install agent-reach
agent-reach search --platform xiaohongshu --query "Rust 入门"
agent-reach read --platform bilibili --url "https://bilibili.com/video/BVxxx"
```

**适合人群：** AI Agent 开发者、跨平台内容聚合器开发者

> Star: 23,420 | Fork: 1,978 | 协议: MIT | 语言: Python | 本周涨幅: +2,289 | 连续日榜: 2 天

---

## 三、AI 创意应用

### 14. [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo)

**项目简介：** MoneyPrinterTurbo 利用大语言模型一键生成高清短视频，从文案撰写到视频剪辑全自动完成。支持抖音、TikTok 等竖屏格式，适合批量生产信息流内容。

**核心亮点：**
- 一键生成：输入主题，自动完成文案 → 配音 → 素材匹配 → 视频合成
- 支持多种大语言模型后端，灵活切换
- 内置素材库和模板系统，开箱即用
- Python 技术栈，MoviePy 做视频处理，透明度高、可定制性强

**快速上手：**

```bash
pip install moneyprinterturbo
mpt --topic "GitHub 本周热门项目" --output video.mp4
```

**适合人群：** 自媒体运营者、内容创作者、批量视频生成需求方

> Star: 81,554 | Fork: 11,615 | 协议: MIT | 语言: Python | 本周涨幅: +7,992

### 15. [Open-LLM-VTuber/Open-LLM-VTuber](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber)

**项目简介：** Open-LLM-VTuber 让你在本地运行一个 Live2D 虚拟形象，通过语音与大语言模型实时对话。支持语音打断、多平台运行，数据完全本地化。

**核心亮点：**
- 完全离线运行：LLM、语音识别、语音合成、Live2D 渲染全部本地化
- 支持语音打断——对话中可以随时插话，体验自然
- 兼容 Ollama、LM Studio 等多种本地模型运行时
- Live2D 面部追踪与 LLM 回复同步，表情自然

**快速上手：**

```bash
git clone https://github.com/Open-LLM-VTuber/Open-LLM-VTuber.git
cd Open-LLM-VTuber
pip install -r requirements.txt
python main.py
```

**适合人群：** 虚拟主播爱好者、本地 AI 隐私倡导者、二次元技术玩家

> Star: 10,434 | Fork: 1,224 | 协议: NOASSERTION | 语言: Python | 本周涨幅: +2,388 | 连续日榜: 3 天

### 16. [pbakaus/impeccable](https://github.com/pbakaus/impeccable)

**项目简介：** impeccable 是一个为 AI Agent 设计的"设计语言"——它定义了一套规则和原则，让 AI 在生成界面时具备专业设计师的审美判断。不是给人类用的设计系统，而是教 AI "什么是好设计"。

**核心亮点：**
- 设计原则体系：涵盖间距、比例、色彩、动效等设计基础维度
- 可作为 Claude Code / Cursor 的技能插件安装
- 对 AI 生成的界面提供实时审美评估和改进建议
- 让不具备设计背景的开发者也能产出视觉质量上乘的产品

**快速上手：**

```bash
claude skill add pbakaus/impeccable
# 在生成界面时自动应用设计原则
```

**适合人群：** 前端开发者、Vibe Coding 用户、独立开发者

> Star: 35,840 | Fork: 1,954 | 协议: Apache-2.0 | 语言: JavaScript | 本周涨幅: +3,586

---

## 四、安全 & 开发工具

### 17. [aquasecurity/trivy](https://github.com/aquasecurity/trivy)

**项目简介：** trivy 是一款全面的安全扫描工具，用于检测容器镜像、Kubernetes 集群、代码仓库、云环境中的漏洞、配置错误和敏感信息泄露。CNCF 毕业项目，生产级稳定性。

**核心亮点：**
- 全栈扫描：容器、K8s、IaC、代码依赖、云配置一站覆盖
- SBOM（软件物料清单）生成，符合供应链安全合规要求
- Go 语言编写，扫描速度快，CI/CD 集成无缝
- 连续 4 天日榜在线，说明安全领域关注度持续走高

**快速上手：**

```bash
# 安装
brew install trivy  # macOS
# 或
apt-get install trivy  # Debian/Ubuntu

# 扫描容器镜像
trivy image nginx:latest

# 扫描代码仓库
trivy repo .
```

**适合人群：** DevOps 工程师、安全工程师、CI/CD 管线维护者

> Star: 36,135 | Fork: 459 | 协议: Apache-2.0 | 语言: Go | 本周涨幅: +844 | 连续日榜: 4 天

### 18. [dmtrKovalenko/fff](https://github.com/dmtrKovalenko/fff)

**项目简介：** fff 号称"最快且最精确的文件搜索工具包"，面向 AI Agent、Neovim、Rust 和 NodeJS 场景优化。用 Rust 编写，搜索速度比传统工具快一个数量级。

**核心亮点：**
- Rust 实现，搜索性能极高，适合大规模代码库
- 同时提供 Neovim 插件、NodeJS 绑定和 CLI 工具
- 精确匹配优先，减少 AI Agent 误读文件的风险
- 对 AI Agent 的文件定位场景做了专门优化

**快速上手：**

```bash
# CLI 使用
cargo install fff
fff search "TODO" --type rs

# Neovim 插件
use 'dmtrKovalenko/fff.nvim'
```

**适合人群：** Neovim 用户、AI Agent 开发者、大仓库维护者

> Star: 7,709 | Fork: 311 | 协议: MIT | 语言: Rust | 本周涨幅: +879

### 19. [openai/plugins](https://github.com/openai/plugins)

**项目简介：** OpenAI 官方的插件仓库，包含插件开发规范、示例代码和工具链。适合想要为 AI 助手开发自定义能力的开发者。

**核心亮点：**
- 官方维护，API 规范和开发指南最权威
- 包含多种类型的插件示例：搜索、代码执行、文件操作等
- 插件开发流程文档完善，从零到发布全链路覆盖
- 与 OpenAI 生态深度整合，插件可直接上架使用

**快速上手：**

```bash
git clone https://github.com/openai/plugins.git
cd plugins
# 按照文档创建你的第一个插件
```

**适合人群：** AI 插件开发者、OpenAI API 深度用户

> Star: 2,144 | Fork: 277 | 语言: JavaScript | 本周涨幅: +595 | 连续日榜: 2 天

---

## 本周总结

本周的 GitHub Trending 有三个值得关注的趋势：

**1. Agent 生态进入"基础设施"阶段。** ECC（性能优化）、taste-skill（审美）、impeccable（设计语言）、harness（团队编排）——Agent 开发不再是"写个 Prompt 跑起来"就行，而是在工程化、审美化、系统化方向全面演进。整个 Agent 工具链正在成形。

**2. Token 效率成为刚需。** headroom 单周 +14,272 星、连续 4 天日榜霸屏，说明大模型 Token 成本和上下文窗口限制是当前开发者最大的痛点之一。能在这个环节提供价值的工具，市场反馈极其迅速。

**3. 跨平台信息获取需求爆发。** Agent-Reach（零 API 费用全网搜索）和 last30days-skill（跨平台研究技能）的走红，反映出 AI Agent 对"实时、多源、结构化"信息的强烈渴求。

**最值得关注：** 如果只关注一个项目，推荐 [headroom](https://github.com/chopratejas/headroom)——LLM Token 压缩是当前 AI 应用的核心瓶颈，这个项目的实用性和增长势头都值得关注。

---

*数据来源：GitHub Trending Weekly（2026-06-02 至 2026-06-08），周涨幅以 GitHub Weekly 页面为准，连续上榜天数基于 GitHub Trending Daily 统计。*
