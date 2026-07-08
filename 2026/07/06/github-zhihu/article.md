# 2026年7月第28周 GitHub 热门开源项目盘点（06月29日-07月06日）

> 本周 AI Agent 生态继续爆发，单周涨星破万的项目多达两个，AI 编码、视频生成、隐私通讯、安全渗透全线升温。

## 本周趋势速览

| 趋势 | 说明 |
|------|------|
| 最大赢家 | `msitarzewski/agency-agents` 单周涨 +10,637 星，累计 127,532 星，登顶本周涨幅榜 |
| AI 安全双雄 | `usestrix/strix`（AI 渗透测试，+10,338）与 `simplex-chat/simplex-chat`（无身份标识聊天，+3,572）共同折射出"AI 时代安全基建"被集中关注 |
| 新面孔密集 | `DeusData/codebase-memory-mcp`、`calesthio/OpenMontage`、`ogulcancelik/herdr`、`stablyai/orca` 等多个项目均为 2026 年初才创建的年轻仓库 |
| 持续热门 | `topoteretes/cognee`（Agent 记忆）、`logto-io/logto`（认证基础设施）连续数周维持在榜 |
| 主题集中 | 本周 15 个项目里 9 个直接与"AI Agent / 编码智能体"相关，AI 工具链成为绝对主线 |

---

## 项目详细解读

### AI & 智能体

#### 1. [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)

**项目简介：** 一套"开箱即用的 AI 代理团队"——把前端开发、社区运营、内容创作、风控审核等不同岗位的角色，封装成一个个带性格、流程和交付物的专业 Agent，让你像组建一个虚拟公司一样调度多个 AI 协作。

**核心亮点：**
- 角色化设计：每个 Agent 都是"带人格的专家"，比如前端向导、Reddit 社群忍者、创意注入器、现实校验器，分工明确而非通用聊天机器人
- 交付物导向：每个 Agent 不只回答问题，而是产出明确的工件（文案、设计稿、代码片段、审核报告）
- Shell 脚本驱动，门槛低、易扩展，方便集成进既有自动化流程

**快速上手：**

```bash
git clone https://github.com/msitarzewski/agency-agents
cd agency-agents
# 按 README 中的角色清单挑选 Agent，配合 Claude Code / Codex 等 CLI 工具调用
```

**适合人群：** 需要搭建 AI 自动化工作流的内容创作者、独立开发者、小型运营团队。

> Star: 127,532 | Fork: 20,711 | 协议: MIT | 语言: Shell | 本周涨幅: +10,637

---

#### 2. [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)

**项目简介：** 高性能代码智能 MCP 服务器，把整个代码仓库索引成持久化的知识图谱，让 AI 编码助手能够"记住"你的代码库——平均仓库毫秒级完成索引，支持 158 种语言，查询响应在亚毫秒级，号称减少 99% 的 token 消耗。

**核心亮点：**
- 持久化知识图谱：基于 tree-sitter 解析 + SQLite 存储，跨会话保留代码理解，避免每次都重新喂上下文
- 单一静态二进制 + 零依赖，部署门槛接近"下载即用"
- 兼容主流 AI 编码工具：Claude Code、Codex、Cursor、Gemini CLI、Windsurf、Aider、opencode 等都能直接接入

**快速上手：**

```bash
# 下载单文件二进制后
codebase-memory-mcp index /path/to/your/repo
# 在 Claude Code / Cursor 的 MCP 配置里挂载本服务即可
```

**适合人群：** 在大型代码库里使用 AI 编码助手的开发者，尤其是苦于"AI 总忘事"的团队。

> Star: 26,764 | Fork: 1,986 | 协议: MIT | 语言: C | 本周涨幅: +7,945

---

#### 3. [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage)

**项目简介：** 自称"全球首个开源的 Agentic 视频生产系统"——12 条流水线、52 个工具、500+ 个 Agent 技能，把 AI 编码助手变成一整套视频制作工作室，覆盖文案、配音、画面生成、剪辑、合成全链路。

**核心亮点：**
- Pipeline 化的视频生产：把"脚本 → 配音（ElevenLabs）→ 配图（Flux/Stable Diffusion）→ 剪辑（Remotion/FFmpeg）"串成 Agent 可调度的任务图
- 与主流编码 Agent 解耦：Claude、Cursor、Copilot、OpenAI 都能驱动
- 全开源（AGPL-3.0），可自托管，避免商业视频工具的订阅成本

**快速上手：**

```bash
git clone https://github.com/calesthio/OpenMontage
cd OpenMontage
# 配置 API Key（TTS / 图像生成）后，按 README 选择 pipeline 模板运行
```

**适合人群：** 需要批量生产短视频的创作者、做视频自动化的工程师、研究多模态 Agent 系统的研究者。

> Star: 33,700 | Fork: 3,862 | 协议: AGPL-3.0 | 语言: Python | 本周涨幅: +7,353

---

#### 4. [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire)

**项目简介：** "AI 时代的伯克希尔"——一个为 Claude Code / Codex 设计的价值投资研究框架，把巴菲特、芒格、段永平、李录四位投资大师的方法论，封装成多个并行协作的 Agent，对个股进行多角度、对抗式的基本面分析。同时支持 A 股与美股研究。

**核心亮点：**
- 多 Agent 对抗分析：不同 Agent 扮演不同大师视角，避免单一视角偏见
- 完整研究框架：从财报数据、行业对比、护城河评估到估值建模，流程结构化
- 多市场支持，含中文 A 股标的的研究链路

**适合人群：** 个人投资者、量化研究员、想用 LLM 做基本面研究的开发者。注意：本工具用于研究辅助，不构成投资建议。

> Star: 10,350 | Fork: 1,317 | 协议: MIT | 语言: Python | 本周涨幅: +5,038

---

#### 5. [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute)

**项目简介：** 一个免费 AI 网关——单端点接入 231+ 家模型供应商（其中 50+ 完全免费），让 Claude Code、Codex、Cursor、Cline、Copilot 等编码工具直接连到免费的 Claude / GPT / Gemini，并叠加 RTK+Caveman 压缩算法节省 15-95% 的 token。

**核心亮点：**
- 多供应商聚合 + 智能自动故障切换，单点失败不影响开发
- token 压缩：长上下文场景下显著降低调用成本
- 支持 MCP / A2A 协议、多模态 API，提供桌面端与 PWA

**适合人群：** 想白嫖大模型 API 的独立开发者、需要降低 AI 编码成本的团队。

> Star: 11,910 | Fork: 1,729 | 协议: MIT | 语言: TypeScript | 本周涨幅: +4,411

---

#### 6. [browser-use/video-use](https://github.com/browser-use/video-use)

**项目简介：** 来自 browser-use 团队的新作——用编码 Agent 来编辑视频。把视频剪辑操作抽象成可被代码 Agent 调用的工具链，让 AI 自己写代码完成剪切、拼接、加字幕、转码等视频处理任务。

**核心亮点：**
- 延续 browser-use"用 Agent 操作浏览器"的思路，这次把目标对准视频剪辑软件
- 编码 Agent 友好：把 FFmpeg / 视频工具的复杂命令封装成 Agent 可调用的原语
- 适合自动化批量视频处理、构建视频类 Agent 应用

**适合人群：** 构建视频自动化流水线的开发者、Agent 应用开发者、视频批量处理场景的工程师。

> Star: 15,049 | Fork: 1,779 | 协议: MIT | 语言: Python | 本周涨幅: +4,288

---

#### 7. [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis)

**项目简介：** LLM 驱动的多市场股票智能分析系统，整合多源行情数据、实时新闻、决策看板与自动推送，支持零成本定时运行。把"看盘 + 读新闻 + 出报告"这条分析师日常链路，用大模型自动化。

**核心亮点：**
- 多源数据聚合：行情 + 新闻 + 公告统一进入 LLM 分析管线
- 决策看板 + 自动推送（邮件/IM），定时运行成本几乎为零
- 多市场支持，社区活跃（47K+ Fork 反映了二次开发热度）

**适合人群：** 量化爱好者、个人投资者、研究 LLM 在金融分析场景落地的开发者。注意：本项目是分析工具，输出不构成投资建议。

> Star: 54,726 | Fork: 47,369 | 协议: MIT | 语言: Python | 本周涨幅: +3,806

---

#### 8. [alibaba/page-agent](https://github.com/alibaba/page-agent)

**项目简介：** 阿里开源的"网页内嵌 GUI Agent"——用自然语言控制网页界面。和通用浏览器 Agent 不同，它直接运行在页面上下文里，能更精准地操作 DOM、表单、按钮等页面元素。

**核心亮点：**
- In-page 设计：注入到目标页面中执行，比跨进程的浏览器 Agent 延迟更低、上下文更完整
- 自然语言驱动：用户描述意图，Agent 自动定位元素并执行操作
- 兼容 MCP 协议，可作为浏览器自动化链路的一环

**快速上手：** 项目提供 TypeScript SDK，可在前端项目或浏览器扩展中集成。

**适合人群：** 做 RPA / 网页自动化的工程师、研究 GUI Agent 的算法工程师、需要构建无障碍辅助工具的团队。

> Star: 23,948 | Fork: 2,062 | 协议: MIT | 语言: TypeScript | 本周涨幅: +3,151

---

#### 9. [topoteretes/cognee](https://github.com/topoteretes/cognee)

**项目简介：** 开源 AI 记忆平台——给 AI Agent 加上跨会话的长期记忆，底层是自托管的知识图谱引擎 + 向量数据库，让 Agent 不再"金鱼脑"。

**核心亮点：**
- 认知架构导向：把记忆建模成知识图谱（Graph RAG），而非简单向量检索
- 自托管：数据不出本地，隐私可控
- 兼容主流 Agent 框架，可作为记忆层插件接入

**适合人群：** 构建有状态 Agent 应用的开发者、研究长期记忆架构的研究者、对隐私敏感的 AI 应用团队。

> Star: 27,130 | Fork: 2,525 | 协议: Apache-2.0 | 语言: Python | 本周涨幅: +2,699

---

### 开发工具

#### 10. [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr)

**项目简介：** "活在终端里的 Agent 多路复用器"——用 Rust 写的终端工作区管理工具，可以同时跑多个编码 Agent（Claude Code、Codex 等），像 tmux 一样切换、编排，但专门为 Agent 协作优化。

**核心亮点：**
- Rust 实现，启动快、内存占用低
- 终端 UI 友好：多 Agent 并行工作不混乱，可可视化查看每个 Agent 的状态
- 工作区管理：每个项目一个独立 workspace，Agent 之间不互相干扰

**适合人群：** 重度使用编码 Agent 的开发者、终端控、需要并行调度多个 AI 编码任务的工程师。

> Star: 12,111 | Fork: 705 | 协议: NOASSERTION | 语言: Rust | 本周涨幅: +3,937

---

#### 11. [stablyai/orca](https://github.com/stablyai/orca)

**项目简介：** 面向"并行 Agent 舰队"的 ADE（Agent Development Environment）——用一个订阅调度任意编码 Agent 并行工作，桌面端 + 移动端均可用，YC 背景。

**核心亮点：**
- 并行 Agent 编排：在同一项目里同时跑多个 Agent 处理不同子任务
- 跨端可用：桌面 + 移动端，配合 worktrees、ghostty 等现代开发工具链
- 自带订阅管理思路，让"用自己的 API Key 调度多 Agent"成为默认模式

**适合人群：** 把编码 Agent 当生产力工具重度使用的开发者、Agent 工具链爱好者。

> Star: 12,399 | Fork: 837 | 协议: MIT | 语言: TypeScript | 本周涨幅: +3,783

---

#### 12. [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc)

**项目简介：** OpenAI 官方出品——在 Claude Code 里调用 Codex 来做代码评审或委派任务。让两家的编码 Agent 互相协作，发挥各自长处。

**核心亮点：**
- 官方背书，跨厂商 Agent 协作的早期范本
- 用法直接：在 Claude Code 里通过插件方式调起 Codex
- 适合"一个写代码一个评审"的双 Agent 工作流

**适合人群：** 同时使用 Claude Code 与 Codex 的开发者、追求代码评审自动化的团队。

> Star: 25,524 | Fork: 1,541 | 协议: Apache-2.0 | 语言: JavaScript | 本周涨幅: +3,405

---

#### 13. [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template)

**项目简介：** 一条命令用 AI 编码 Agent 克隆任意网站——基于 Next.js + React + Tailwind + shadcn-ui 的脚手架模板，配合 AI Agent 完成网站结构反推与前端代码生成。

**核心亮点：**
- 全套现代前端技术栈（Next.js / shadcn / Tailwind），克隆产物可直接二次开发
- Skills + 模板化设计，把"抓页面 → 分析结构 → 生成组件"流水线化
- 兼容主流编码 Agent（Claude Code、Cursor 等）

**适合人群：** 做前端开发的工程师、想快速搭建同类产品的独立开发者、学习现代前端技术栈的新人。

> Star: 25,861 | Fork: 3,637 | 协议: MIT | 语言: TypeScript | 本周涨幅: +3,246

---

### 安全 & 隐私

#### 14. [usestrix/strix](https://github.com/usestrix/strix)

**项目简介：** 开源 AI 渗透测试工具，用于发现并修复应用中的安全漏洞。把传统渗透测试流程交给 Agent 自动化执行，覆盖漏洞扫描、利用验证、修复建议全链路。

**核心亮点：**
- AI 驱动：Agent 自主规划测试路径，覆盖面比纯规则扫描更广
- 面向合法安全场景：Bug Bounty、CTF、红队演练、安全自查
- Apache-2.0 协议，社区贡献活跃（topics 涵盖 ethical-hacking / red-teaming / bug-bounty 等）

**快速上手：**

```bash
pip install -r requirements.txt
# 按README配置目标后运行Agent化扫描
```

**适合人群：** 安全工程师、Bug Bounty 猎人、CTF 选手、企业安全团队。⚠️ 仅用于授权范围内的安全测试。

> Star: 37,179 | Fork: 3,774 | 协议: Apache-2.0 | 语言: Python | 本周涨幅: +10,338

---

#### 15. [simplex-chat/simplex-chat](https://github.com/simplex-chat/simplex-chat)

**项目简介：** SimpleX——一个"不收集任何用户标识"的消息网络。和其他通讯软件不同，它不分配用户 ID，不依赖手机号 / 邮箱，联络关系完全由双方本地维护，从协议层做到 100% 隐私保护。提供 iOS、Android、桌面全平台客户端。

**核心亮点：**
- 协议层创新：无用户标识符 = 即使服务器被攻破也无法关联身份
- 双重加密（Double Ratchet），Haskell 实现的核心协议层经过长期审计
- 老牌项目（2019 年创建），稳定迭代多年，本周再迎涨星高峰

**适合人群：** 对通讯隐私有极高要求的用户、记者 / 研究者 / 隐私倡导者、研究去中心化通讯协议的开发者。

> Star: 17,924 | Fork: 1,055 | 协议: AGPL-3.0 | 语言: Haskell | 本周涨幅: +3,572

---

## 本周总结

把这一周的榜单摊开看，明显的信号是 **"AI Agent 正在变成新一代开发基础设施"**：

1. **AI 编码 Agent 的"工具链层"全面成型**——`codebase-memory-mcp`（记忆）、`herdr`（终端多路复用）、`orca`（并行调度）、`codex-plugin-cc`（跨厂商协作）、`OmniRoute`（网关）、`page-agent`（GUI 操作）几乎覆盖了一个 AI 编码 Agent 工作流的每个环节。开发者正在像 2010 年围绕 DevOps 工具链一样，围绕编码 Agent 重建一整套基础设施。
2. **垂直 Agent 应用爆发**——`agency-agents`（虚拟团队）、`OpenMontage`（视频生产）、`video-use`（视频剪辑）、`ai-berkshire`（投资研究）、`daily_stock_analysis`（股票分析）显示出 Agent 正在从"通用聊天"走向"交付物导向的专业角色"。
3. **安全与隐私同步升温**——`strix`（AI 渗透测试）和 `simplex-chat`（无标识通讯）的同时上榜，说明"AI 时代如何保护自己"正在成为公众议题。

**本周最值得关注：**

- **想体验 AI 编码 Agent 工具链**：首选 `DeusData/codebase-memory-mcp`，单二进制 + 跨工具兼容，接入门槛最低。
- **做内容 / 视频自动化**：`calesthio/OpenMontage` 是目前最完整的开源 Agentic 视频生产系统。
- **关注隐私基建**：`simplex-chat/simplex-chat` 是通讯隐私领域难得的协议级创新。

> 数据来源：GitHub Trending Weekly 页面（2026-07-06 抓取），周涨幅以 Weekly 页面为准，Star / Fork / Issue 数通过 GitHub API 复核。共盘点 15 个项目，覆盖 AI 智能体、开发工具、安全隐私三大方向。
