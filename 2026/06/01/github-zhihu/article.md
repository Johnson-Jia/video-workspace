# 2026年6月第1周 GitHub 热门开源项目盘点

> 本周 GitHub 被 AI Agent 技能生态彻底刷屏了——榜单 19 个项目中近半数与 Claude Code、Cursor、Codex 的技能/插件直接相关。一个 20 万星的项目领跑全场，AI 正从"能写代码"进化到"有审美、有安全意识、能自我治理"。

## 本周趋势速览

| 趋势 | 说明 |
|------|------|
| 最大赢家 | [affaan-m/ECC](https://github.com/affaan-m/ECC) 以 200,591 星位居榜首，是本周涨星最多的 Agent 性能优化系统 |
| 新面孔 | [dograh-hq/dograh](https://github.com/dograh-hq/dograh)（开源语音 AI 平台）、[ogulcancelik/herdr](https://github.com/ogulcancelik/herdr)（终端 Agent 多路复用器）、[microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit)（Agent 治理工具包）均为本周首次上榜 |
| 持续热门 | [microsoft/markitdown](https://github.com/microsoft/markitdown)（134,941 星）和 [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo)（74,143 星）持续霸榜多周 |
| 核心主题 | AI Agent 技能生态集中爆发——技能市场、知识图谱、审美控制、安全技能全面开花 |

## 项目详细解读

### AI Agent 技能生态

本周的绝对主角。随着 Claude Code、Cursor、Codex 等 AI 编程工具开放技能/插件生态，围绕 Agent 能力增强的项目如雨后春笋般涌现。

#### 1. [affaan-m/ECC](https://github.com/affaan-m/ECC)

**项目简介：** ECC 是一个 Agent Harness 性能优化系统，覆盖技能（Skills）、本能（Instincts）、记忆（Memory）、安全（Security）四大模块。它不是一个单独的工具，而是为 AI 编程 Agent 提供了一套完整的性能调优框架，让 Agent 从"能用"变成"好用"。

**核心亮点：**
- **四维能力模型**：技能层定义 Agent 能做什么，本能层定义 Agent 该怎么思考，记忆层实现上下文持久化，安全层防止 Agent 越界操作——这四层构成了 Agent 的"操作系统"
- **跨平台兼容**：支持 Claude Code、Codex、OpenCode、Cursor 等主流 AI 编程工具，写一次配置到处运行
- **研究驱动开发**：内置 Research-First Development 模式，Agent 在动手写代码之前会先调研最佳实践，减少"拍脑袋"式的代码生成

**快速上手：** 通过 GitHub 克隆仓库后，按文档配置 `~/.claude/` 目录下的技能文件即可启用

**适合人群：** AI 编程工具重度用户、追求 Agent 输出质量的开发者

> Star: 200,591 | Fork: 30,780 | 协议: MIT | 语言: JavaScript | 创建: 2026-01-18

---

#### 2. [Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything)

**项目简介：** 把任意代码仓库变成可交互的知识图谱。不是静态的依赖关系图，而是真正可以探索、搜索、提问的活图谱——支持点击任意节点深入了解，也可以用自然语言问"这个模块做了什么"。

**核心亮点：**
- **全平台 AI 编程工具支持**：Claude Code、Codex、Cursor、Copilot、Gemini CLI 等均可用，不绑定单一工具
- **交互式知识图谱**：不是传统的树状结构，而是网状关系图谱，可以追踪函数调用链、数据流向、模块依赖
- **Vibe Coding 理念**：项目强调"教 > 展示"（Graphs that teach > graphs that impress），图谱设计以理解代码为目标，不是炫技

**快速上手：** `npx understand-anything` 或在 Claude Code 中通过技能安装

**适合人群：** 需要快速理解大型代码库的开发者、代码审查人员、技术文档工程师

> Star: 47,191 | Fork: 3,830 | 协议: MIT | 语言: TypeScript | 创建: 2026-03-15

---

#### 3. [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph)

**项目简介：** 与 Understand-Anything 互补的项目——它提供预索引的代码知识图谱，100% 本地运行。不需要把代码发送到云端，不需要额外的 API 调用，所有索引在本地构建和查询。

**核心亮点：**
- **100% 本地运行**：零数据泄露风险，适合处理私有仓库和敏感代码
- **省 token 省 API 调用**：预索引意味着 AI 编程工具不需要反复扫描整个代码库，大幅减少 token 消耗和工具调用次数
- **多工具支持**：Claude Code、Codex、Gemini、Cursor、OpenCode 等主流工具均支持

**快速上手：** 安装后在项目根目录运行 `codegraph index` 构建索引，AI 工具自动读取

**适合人群：** 注重代码隐私的开发者、使用私有仓库的团队、希望降低 AI 编程工具成本的团队

> Star: 35,336 | Fork: 2,186 | 协议: MIT | 语言: TypeScript | 创建: 2026-01-18

---

#### 4. [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)

**项目简介：** 一个让 AI 有"好品味"的技能文件。它不做任何功能性的事——它只做一件事：阻止 AI 生成无聊、泛泛、模板化的内容。如果你厌倦了 AI 每次都给你"模块化、可扩展、最佳实践"式的八股代码，这个项目值得一试。

**核心亮点：**
- **反 Sloppy 输出**：内置规则识别和拦截 AI 生成的"套路化"内容——通用配色方案、千篇一律的渐变、缺乏个性的布局
- **设计导向**：特别适用于前端开发和 UI 设计场景，让 AI 生成的界面不再是"能用但丑"
- **轻量级**：只是一个技能文件（Shell 脚本），不引入额外依赖，安装即用

**快速上手：** 将技能文件复制到 `~/.claude/skills/` 目录下即可生效

**适合人群：** 前端开发者、UI/UX 设计师、对 AI 生成内容的审美质量有要求的开发者

> Star: 29,890 | Fork: 2,217 | 协议: MIT | 语言: Shell | 创建: 2026-02-19

---

#### 5. [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills)

**项目简介：** 754 个结构化网络安全技能，专门为 AI Agent 设计。每个技能都映射到五大安全框架：MITRE ATT&CK、NIST CSF 2.0、MITRE ATLAS、D3FEND 和 NIST AI RMF。这不是一个"安全工具"，而是让 AI Agent 拥有安全专家的知识体系。

**核心亮点：**
- **754 个结构化技能**：覆盖 26 个安全领域，从渗透测试到恶意软件分析、从威胁狩猎到事件响应
- **五大框架映射**：每个技能都与业界标准安全框架对齐，确保覆盖全面且可审计
- **跨平台兼容**：支持 Claude Code、GitHub Copilot、Codex CLI、Cursor、Gemini CLI 等 20+ 平台

**快速上手：** 按文档指引将技能文件安装到对应 AI 工具的技能目录

**适合人群：** 安全工程师、DevSecOps 从业者、需要 AI 辅助安全审计的团队

> Star: 12,938 | Fork: 1,513 | 协议: Apache-2.0 | 语言: Python | 创建: 2026-02-25

---

### AI 内容与工具

#### 6. [microsoft/markitdown](https://github.com/microsoft/markitdown)

**项目简介：** 微软出品的文件转换工具，能把几乎任何文件格式转成 Markdown——PDF、Word、Excel、PowerPoint、图片、HTML、音频（转录文本）统统支持。在 RAG（检索增强生成）场景下，它是数据预处理的关键一环。

**核心亮点：**
- **广泛的格式支持**：Microsoft Office 全家桶（Word/Excel/PPT）、PDF、图片（OCR）、HTML、音频文件（Whisper 转录）等 20+ 格式
- **LLM 生态集成**：作为 AutoGen 扩展和 LangChain 文档加载器使用，无缝融入 RAG 管线
- **微软品质保障**：13 万星 + 780 个开放 Issues 说明社区活跃度极高，问题修复及时

**快速上手：** `pip install markitdown` → `markitdown input.pdf > output.md`

**适合人群：** RAG 应用开发者、知识管理工程师、需要批量处理文档的数据工程师

> Star: 134,941 | Fork: 9,228 | 协议: MIT | 语言: Python | 创建: 2024-11-13

---

#### 7. [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo)

**项目简介：** 一键生成高清短视频的 AI 工具。输入文案或主题，自动完成文案生成、素材匹配、配音、字幕、背景音乐全流程。名字叫"印钞机"，实际上做的是短视频生产自动化。

**核心亮点：**
- **全流程自动化**：从文案到成片，中间无需人工干预——AI 写文案 → AI 匹配视频素材 → AI 配音 → AI 加字幕 → AI 配乐
- **多平台适配**：支持抖音、TikTok、小红书等平台的视频尺寸和格式
- **Web UI + API 双模式**：提供可视化操作界面，也支持 API 调用批量生产

**快速上手：** `git clone` → `docker-compose up` → 浏览器访问 Web UI

**适合人群：** 短视频创作者、自媒体运营、需要批量生产视频内容的团队

> Star: 74,143 | Fork: 10,584 | 协议: MIT | 语言: Python | 创建: 2024-03-11

---

#### 8. [p-e-w/heretic](https://github.com/p-e-w/heretic)

**项目简介：** 全自动移除大语言模型审查限制的工具。基于 "Abliteration" 技术，通过修改模型的注意力机制来解除安全对齐，让模型在推理阶段不再自我审查。这是一个学术研究项目，涉及 AI 安全对齐的核心议题。

**核心亮点：**
- **全自动处理**：不需要手动修改模型权重，一键完成审查移除
- **Abliteration 技术**：通过调整模型拒绝方向上的注意力权重实现，不需要重新训练
- **学术透明**：项目明确标注研究用途，附带技术原理说明

**快速上手：** 按仓库 README 安装依赖，运行脚本处理目标模型

**适合人群：** AI 安全研究员、对齐技术研究者（请遵守当地法律法规）

> Star: 22,757 | Fork: 2,432 | 协议: AGPL-3.0 | 语言: Python | 创建: 2025-09-21

---

### 开发者基建

#### 9. [iii-hq/iii](https://github.com/iii-hq/iii)

**项目简介：** 用 Rust 编写的实时服务编排框架。不是传统的容器编排（那是 Kubernetes 的事），而是更贴近应用层的服务组合——实时编排、扩展和观测每一个服务。它想做的，是让"写一个微服务"和"编排十个微服务"一样简单。

**核心亮点：**
- **Rust 高性能**：利用 Rust 的零成本抽象和异步运行时，实现亚毫秒级的服务编排延迟
- **多语言支持**：虽然核心是 Rust，但服务端点支持 JavaScript、Python、TypeScript 等
- **实时可观测**：每个服务的状态、延迟、吞吐量实时可见，编排过程全程透明

**快速上手：** `cargo install iii` → 按 Quick Start 定义服务编排

**适合人群：** 后端架构师、微服务开发者、对服务编排性能有极致要求的团队

> Star: 17,372 | Fork: 1,140 | 语言: Rust | 创建: 2025-01-02

---

#### 10. [run-llama/liteparse](https://github.com/run-llama/liteparse)

**项目简介：** Llama 团队（没错，就是做 Llama 大模型的那个团队）出品的文档解析器。快速、轻量、开源，专注于 PDF 和 OCR 场景。它的定位是"给 AI 应用准备的文档解析前端"——在 RAG 管线中负责把非结构化文档变成结构化文本。

**核心亮点：**
- **Llama 团队出品**：背靠 Meta 级别的工程能力，质量和维护有保障
- **Rust 高性能**：文档解析是 CPU 密集型任务，Rust 的性能优势在这里充分体现
- **专注文档场景**：PDF 解析 + OCR，不做万金油，做精一个领域

**快速上手：** `pip install liteparse` 或 `cargo install liteparse`

**适合人群：** RAG 应用开发者、文档处理工程师、需要批量解析 PDF 的数据团队

> Star: 8,318 | Fork: 493 | 协议: Apache-2.0 | 语言: Rust | 创建: 2026-02-09

---

#### 11. [dograh-hq/dograh](https://github.com/dograh-hq/dograh)

**项目简介：** 开源语音 AI 平台，定位是 Vapi 和 Retell 的自托管替代方案。支持完全本地部署，自带可视化工作流构建器，覆盖语音到语音（Speech-to-Speech）和 LLM/STT/TTS 全链路。

**核心亮点：**
- **完全自托管**：数据不出服务器，支持 BYOK（Bring Your Own Key）模式，灵活选择语音模型供应商
- **可视化工作流构建器**：不需要写代码，拖拽式定义对话流程
- **MCP 原生 + 电话集成**：支持 Model Context Protocol，也支持 Asterisk 电话系统接入

**快速上手：** `docker compose up` 访问管理界面，配置语音模型和工作流

**适合人群：** 语音 AI 应用开发者、需要自托管语音方案的企业、客服系统搭建者

> Star: 3,981 | Fork: 797 | 协议: BSD-2-Clause | 语言: Python | 创建: 2025-09-09

---

#### 12. [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr)

**项目简介：** 终端里的 Agent 多路复用器。如果你同时用 Claude Code、Codex、Cursor 等多个 AI Agent，herdr 让你像用 tmux 管理多个终端窗口一样管理多个 Agent——一个界面统揽全局。

**核心亮点：**
- **Agent 多路复用**：同时运行多个 AI 编程 Agent，独立管理各自的工作目录和上下文
- **类 tmux 交互**：如果你会用 tmux，就会用 herdr——分屏、切换、同步操作一脉相承
- **Rust TUI**：流畅的终端界面，资源占用极低，适合在远程服务器上使用

**快速上手：** `cargo install herdr` → `herdr init` → 添加 Agent 配置

**适合人群：** 同时使用多个 AI 编程工具的开发者、远程开发场景、需要并行推进多个任务的工程师

> Star: 3,411 | Fork: 220 | 语言: Rust | 创建: 2026-03-27

---

### AI 学习与治理

#### 13. [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch)

**项目简介：** 从零学 AI 工程全栈的教程仓库。覆盖 Agent、计算机视觉、NLP、强化学习、MCP（Model Context Protocol）等核心方向。不是"调 API 调参教程"，而是从底层原理出发，自己实现每一个组件。

**核心亮点：**
- **全栈覆盖**：Agent、CV、NLP、RL、MCP、Transformers、Swarm Intelligence——一个仓库覆盖 AI 工程师需要的全部技能树
- **From Scratch 理念**：每个模块都从基本原理讲起，先手动实现，再用框架优化。不是"会用 PyTorch"，而是"理解为什么需要 PyTorch"
- **多语言实战**：Python 为主线，穿插 Rust 和 TypeScript 的生产级实现

**快速上手：** 克隆仓库，按目录结构从 01-fundamentals 开始学习

**适合人群：** 想系统学习 AI 工程的开发者、从后端转 AI 的工程师、有一定编程基础但缺乏 AI 理论的同学

> Star: 25,780 | Fork: 4,180 | 协议: MIT | 语言: Python | 创建: 2026-03-18

---

#### 14. [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit)

**项目简介：** 微软出品的 AI Agent 治理工具包。当 Agent 越来越自主、越来越强大时，谁来管它？这个工具包提供策略引擎、零信任身份、执行沙盒和可靠性工程——覆盖 OWASP Agentic Top 10 的全部 10 个风险点。

**核心亮点：**
- **OWASP Agentic Top 10 全覆盖**：10/10——从提示注入到权限越权，从数据泄露到供应链攻击，每个风险点都有对应的防护方案
- **零信任身份模型**：Agent 不默认信任任何人或系统，每次操作都需要验证权限
- **执行沙盒**：Agent 的所有文件操作、网络请求、API 调用都在沙盒中执行，可审计、可回滚

**快速上手：** `pip install agent-governance-toolkit` → 按文档配置策略和沙盒

**适合人群：** AI 安全工程师、企业 AI 治理团队、负责 AI 合规的技术管理者

> Star: 3,563 | Fork: 509 | 协议: MIT | 语言: Python | 创建: 2026-03-02

---

## 本周总结

本周 GitHub Trending 的核心信号非常清晰：**AI Agent 正在从"能写代码"进化到"有品味、有安全意识、能自我治理"**。

技能生态的爆发是最值得关注的趋势——ECC（20 万星）解决了 Agent 性能问题，taste-skill 解决了审美问题，Anthropic-Cybersecurity-Skills 解决了安全知识问题，Understand-Anything 和 codegraph 解决了代码理解问题。加上微软的 Agent 治理工具包兜底，Agent 的能力栈正在快速补全。

**最值得关注的项目**：
1. **[affaan-m/ECC](https://github.com/affaan-m/ECC)** — 20 万星不是偶然，它定义了 Agent 性能优化的标准范式
2. **[Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything)** — 代码知识图谱的交互体验令人印象深刻，对所有 AI 编程工具用户都有价值

---

*数据来源：GitHub Trending Weekly 页面（2026-06-01），通过 `github_trending.py` 脚本采集 + `gh api` 数据增强。周涨幅以 GitHub Weekly 页面为准。项目排名以 Weekly 页面为准。*
