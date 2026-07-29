# 2026年7月第31周 GitHub 热门开源项目盘点

> AI 智能体（Agent）生态全面爆发，从统一网关、多 Agent 编排到代码智能体工具链，本周 GitHub 热榜被"Agent"主题强势占据——本周涨幅前 15 名累计涨星超 9.6 万，其中一本国产 AI Agent 开源书单周涨星 1.59 万登顶。

## 本周趋势速览

| 趋势 | 说明 |
|------|------|
| 最大赢家 | `bojieli/ai-agent-book` 单周涨星 +15,909，作为一本系统讲解 AI Agent 设计原理的中文开源书，登顶本周热榜 |
| 新面孔 | `stablyai/orca`（多 Agent 并行编排桌面端）、`diegosouzapw/OmniRoute`（统一 AI 网关）、`1jehuang/jcode`（Rust 极致省内存编码 Agent）等新项目集中上榜 |
| 持续热门 | `earendil-works/pi`（总 Star 7.8 万）、`mattpocock/skills`（总 Star 18.9 万）持续累积热度，本周再涨数千 Star |
| 核心主线 | AI 编码 Agent、Agent 编排平台、统一模型网关、代码知识图谱四条主线齐头并进 |

---

## 项目详细解读

### AI 智能体平台与基础设施

#### 1. [koala73/worldmonitor](https://github.com/koala73/worldmonitor)

**项目简介：** 一个实时全球情报看板，把新闻聚合、地缘政治监测、基础设施追踪整合到统一的态势感知界面中，借助 AI 对海量开源情报（OSINT）做实时提炼与可视化。

**核心亮点：**
- 把分散的新闻、舆情、基础设施状态等多源数据统一进一个看板，降低信息整合成本
- 面向态势感知（situational awareness）场景设计，类似 Palantir 风格的开源替代方案
- 基于 MCP 协议接入，可作为智能体的实时数据后端

**快速上手：** 仓库克隆后按 README 启动前端服务即可，TypeScript 技术栈，依赖标准 Node 工具链。

**适合人群：** 情报分析、舆情监测、智能体数据源集成方向的开发者。

> Star: 74,819 | Fork: 11,236 | 协议: NOASSERTION | 语言: TypeScript | 本周涨幅: +12,615

#### 2. [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute)

**项目简介：** 一个 MIT 协议的统一 AI 网关，用单一端点对接 290+ 模型供应商（其中 90+ 免费）、500+ 模型，支持主流大语言模型与编码 Agent 工具，具备配额感知的自动故障转移与令牌压缩能力。

**核心亮点：**
- 一个端点统一多家供应商，配额耗尽自动切换，免去多 Key 管理负担
- 内置 RTK + Caveman 压缩算法，官方称可节省 15%–95% 的 token 消耗
- 兼容主流编码 Agent CLI 与桌面端，支持 MCP / A2A 协议

**快速上手：** 作为 MIT 网关可本地或桌面 PWA 部署，按文档配置供应商 Key 即可统一调用。

**适合人群：** 需要频繁切换多家大语言模型供应商、关注 token 成本的开发者与团队。

> Star: 31,112 | Fork: 4,040 | 协议: MIT | 语言: TypeScript | 本周涨幅: +10,912

#### 3. [stablyai/orca](https://github.com/stablyai/orca)

**项目简介：** 一个面向"并行 Agent 舰队"的 Agent 开发环境（ADE），让你用自己的订阅同时运行多个编码 Agent，支持桌面、移动与 VPS 多端。

**核心亮点：**
- 把多个编码 Agent 编排成并行舰队，显著提升批量任务吞吐
- 跨端可用（桌面 / 移动 / VPS），并内置 worktrees 等工程化能力
- YC 支持项目，工程化完成度较高

**快速上手：** 下载桌面端或自部署 VPS 版本，绑定已有编码 Agent 订阅即可启动并行会话。

**适合人群：** 需要并行跑多个编码任务、提升 Agent 工程效率的重度用户。

> Star: 29,810 | Fork: 2,115 | 协议: MIT | 语言: TypeScript | 本周涨幅: +7,392

#### 4. [earendil-works/pi](https://github.com/earendil-works/pi)

**项目简介：** 一个 AI Agent 工具包，提供统一的 LLM API、Agent 循环、TUI 终端界面与编码 Agent CLI，是一套从底层 API 到上层编码 Agent 的完整工具链。

**核心亮点：**
- 统一 LLM API 抽象层，屏蔽不同模型供应商差异
- 自带 Agent 循环与终端 TUI，开箱即用的命令行编码体验
- 总 Star 已达 7.8 万，社区基础扎实

**快速上手：** 参照仓库 README 安装 CLI，配置模型 Key 后即可在终端调用编码 Agent。

**适合人群：** 偏好终端工作流、希望自建 Agent 工具链的开发者。

> Star: 78,151 | Fork: 9,622 | 协议: MIT | 语言: TypeScript | 本周涨幅: +5,389

### AI 学习与教育资源

#### 5. [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book)

**项目简介：** 《深入理解 AI Agent：设计原理与工程实践》（李博杰 著）的开源主仓库，包含全书正文、编译版 PDF 与按章配套代码，系统讲解智能体的设计原理与工程落地。

**核心亮点：**
- 覆盖 Agent 记忆、上下文工程、多模态、RAG、多智能体、强化学习等核心主题
- 正文与按章代码配套，理论与工程实践结合
- 中文原创、Apache-2.0 协议，对中文学习者极为友好

**快速上手：** 仓库内直接阅读 Markdown 正文或下载编译版 PDF，按章运行配套 Python 代码。

**适合人群：** 希望系统理解 AI Agent 原理与工程的开发者、研究者与学生。

> Star: 21,058 | Fork: 2,089 | 协议: Apache-2.0 | 语言: Python | 本周涨幅: +15,909

#### 6. [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch)

**项目简介：** 一个从零开始的 AI 工程教程，覆盖从机器学习、深度学习到智能体、MCP、强化学习的完整学习路径，口号是"Learn it. Build it. Ship it for others."。

**核心亮点：**
- 从基础到工程交付全链路覆盖，包含计算机视觉、NLP、生成式 AI 等方向
- 多语言示例（Python / Rust / TypeScript），不局限于单一技术栈
- 总 Star 超 4.3 万，是广受认可的系统化学习资源

**快速上手：** 按仓库章节顺序学习，每章配可运行代码，逐步构建并交付项目。

**适合人群：** 想从零系统转入 AI 工程方向的学习者。

> Star: 43,796 | Fork: 7,367 | 协议: MIT | 语言: Python | 本周涨幅: +4,317

#### 7. [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)

**项目简介：** 来自香港大学数据智能实验室（HKUDS）的终身个性化辅导系统，基于多智能体与 RAG 构建，提供深度研究（deep research）与交互式学习能力。

**核心亮点：**
- 面向"终身学习"场景的个性化辅导，强调长期记忆与因材施教
- 多智能体系统 + RAG 架构，支持深度研究式问答
- 提供 CLI 工具，便于集成到个人学习工作流

**快速上手：** 参照仓库文档安装 Python 依赖，配置模型后即可运行辅导 CLI。

**适合人群：** 教育技术研究者、希望自建个性化学习助手的学习者。

> Star: 30,119 | Fork: 3,965 | 协议: Apache-2.0 | 语言: Python | 本周涨幅: +2,199

### AI 编码与开发效率工具

#### 8. [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph)

**项目简介：** 一个本地优先（local-first）的代码智能图谱工具，为 MCP 与 CLI 构建代码库的持久化知识图谱，让 AI 编码工具"只读关键部分"，在代码审查与大型仓库工作流中显著缩减上下文。

**核心亮点：**
- 基于 tree-sitter 与 GraphRAG 构建增量代码知识图谱
- 本地优先，代码不出本机即可获得图谱化的智能检索
- 官方给出代码审查与大型仓库的上下文缩减基准数据

**快速上手：** 通过 MCP 接入主流 AI 编码工具，或直接使用其 CLI 对本地仓库建图。

**适合人群：** 在大型代码库中使用 AI 编码工具、苦于上下文爆炸的开发者。

> Star: 26,643 | Fork: 2,484 | 协议: MIT | 语言: Python | 本周涨幅: +6,006

#### 9. [1jehuang/jcode](https://github.com/1jehuang/jcode)

**项目简介：** 一个主打"极致省内存"的编码 Agent harness，用 Rust 实现，定位是当前内存效率最高的 Agent 运行框架之一。

**核心亮点：**
- Rust 实现，内存占用极低，适合资源受限环境长跑多 Agent
- 终端 TUI + 多模型适配，兼顾性能与可用性
- 面向编码 Agent 场景优化，强调 harness 层的工程效率

**快速上手：** 按仓库说明用 Cargo 构建运行，在终端配置模型后启动编码会话。

**适合人群：** 关注 Agent 运行时性能与资源开销、偏好 Rust 工具链的开发者。

> Star: 11,680 | Fork: 1,296 | 协议: MIT | 语言: Rust | 本周涨幅: +2,909

#### 10. [Nutlope/hallmark](https://github.com/Nutlope/hallmark)

**项目简介：** 一个面向主流 AI 编码工具（Claude Code、Cursor、Codex 等）的"反 AI 味设计 Skill"，目标是让 AI 生成的界面摆脱千篇一律的"AI slop"感，输出更有设计感的视觉。

**核心亮点：**
- 以 Skill 形式注入编码 Agent，约束生成结果的设计质量
- 直击"AI 生成的界面长得都一样"这一痛点
- 轻量、即插即用，适配多家主流编码工具

**快速上手：** 将 Skill 文件放入对应编码工具的 skills 目录，按 README 启用即可。

**适合人群：** 频繁用 AI 编码工具生成前端、对设计质量有要求的开发者。

> Star: 18,284 | Fork: 921 | 协议: MIT | 语言: CSS | 本周涨幅: +4,932

#### 11. [mattpocock/skills](https://github.com/mattpocock/skills)

**项目简介：** 知名 TypeScript 教育者 Matt Pocock 开源的"给真实工程师的 Skills"集合，直接来自他本人的 `.agents` 目录，是一批面向工程实践的 Agent Skill。

**核心亮点：**
- 来自一线工程师的真实 Skill 库，贴近实际工程场景而非演示玩具
- 总 Star 高达 18.9 万，是本周热度最高的 Skill 类资源之一
- 可直接复用到自己的 Agent 工作流

**快速上手：** 按需挑选 Skill 文件，复制到自己的 Agent 配置目录即可生效。

**适合人群：** 正在搭建 Agent 工作流、希望借鉴成熟 Skill 写法的工程师。

> Star: 189,713 | Fork: 16,293 | 协议: MIT | 语言: Shell | 本周涨幅: +12,238

#### 12. [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)

**项目简介：** 一个精选的 Claude Skills 资源清单（awesome list），汇集社区优秀的 Agent Skill、工具与工作流自动化方案，方便开发者快速选型与复用。

**核心亮点：**
- 分类整理 Skill 与工作流自动化资源，节省自行检索成本
- 覆盖多家编码工具生态，跨工具复用性强
- 总 Star 超 7 万，是 Skill 生态的权威索引之一

**快速上手：** 浏览 README 分类目录，按需跳转对应仓库获取 Skill。

**适合人群：** 希望快速发现、复用社区成熟 Skill 的智能体应用开发者。

> Star: 70,923 | Fork: 7,958 | 协议: N/A | 语言: Python | 本周涨幅: +2,820

### 实用开发工具

#### 13. [every-app/open-seo](https://github.com/every-app/open-seo)

**项目简介：** 一个对标商业 SEO 平台（Semrush、Ahrefs）的开源替代方案，提供关键词研究、外链分析、站点审计等核心 SEO 能力。

**核心亮点：**
- 把昂贵的商业 SEO 工具能力开源化，降低中小团队门槛
- 集成 Google Search Console MCP，可联动 AI 工作流
- 覆盖关键词、外链、站点审计三大 SEO 主场景

**快速上手：** 按 README 部署 TypeScript 服务，接入 Google Search Console 后即可开始分析。

**适合人群：** 独立开发者、内容站长、关注自然流量的中小团队。

> Star: 8,261 | Fork: 896 | 协议: MIT | 语言: TypeScript | 本周涨幅: +3,639

#### 14. [schollz/croc](https://github.com/schollz/croc)

**项目简介：** 一个经典且持续活跃的安全文件传输工具，让你轻松、安全地在两台电脑之间发送文件，基于 PAKE（密码认证密钥交换）实现端到端加密。

**核心亮点：**
- 端到端加密，无需复杂配置即可安全传文件
- 跨平台、支持断点续传与多文件，老牌项目至今仍持续维护
- 总 Star 3.8 万、Issue 仅 5 个，工程质量稳定

**快速上手：** 安装后执行 `croc send 文件名`，对方用 `croc <代码>` 即可接收。

**适合人群：** 需要在不同机器间安全、便捷传文件的运维与普通用户。

> Star: 38,679 | Fork: 1,541 | 协议: MIT | 语言: Go | 本周涨幅: +2,993

#### 15. [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad)

**项目简介：** 一组面向 CAD、机器人与硬件设计的 Agent Skill 集合，让智能体能够生成与操作 STEP、STL、URDF 等工程格式文件，把"文字到工程模型"的流程 Agent 化。

**核心亮点：**
- 覆盖 STEP / STL / GLB / URDF / SDF 等主流工程与机器人格式
- 面向机械工程与机器人学场景，结合 OpenCASCADE、build123d 等内核
- 把硬件设计流程接入 Agent 生态，拓展了 AI 编码的边界

**快速上手：** 将对应 Skill 装入支持 Skill 的编码工具，按 README 示例用自然语言生成 CAD 模型。

**适合人群：** 机械工程师、机器人开发者、硬件设计方向的技术人员。

> Star: 10,574 | Fork: 1,153 | 协议: MIT | 语言: JavaScript | 本周涨幅: +2,169

---

## 本周总结

本周 GitHub 热榜被 AI Agent 主题全面统治：从统一模型网关（OmniRoute）、多 Agent 并行编排（orca）、Agent 工具包（pi）到代码智能图谱（code-review-graph），一条完整的"Agent 工程化"技术栈正在成型，Agent 已经从单点实验走向可编排、可并行、可观测的基础设施。

学习资源同样亮眼：`bojieli/ai-agent-book` 单周涨星 1.59 万登顶，说明中文社区对"系统理解 Agent 原理"的需求旺盛；`rohitg00/ai-engineering-from-scratch` 与 `HKUDS/DeepTutor` 则分别覆盖了从零入门与个性化辅导两个学习场景。

**本周最值得关注的两个项目：**
- **`bojieli/ai-agent-book`** — 想系统掌握 Agent 设计原理的中文读者，这本开源书是当前最直接的入口。
- **`tirth8205/code-review-graph`** — 在大型代码库里用 AI 编码工具的开发者，这个本地优先的代码知识图谱能有效缓解上下文爆炸问题，工程价值突出。

---

> **数据来源说明：** 本文项目数据采集于 2026 年 7 月 27 日，源自 GitHub Trending Weekly 页面与 GitHub API。周涨幅（本周新增 Star）以 GitHub Weekly 页面为准，Star/Fork/Issues 等总量数据通过 GitHub API 实时获取，可能随时间略有变化。语言、协议等字段以仓库实际标注为准。
