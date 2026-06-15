# 2026年6月第24周 GitHub 热门开源项目盘点：AI agent skills 生态集体爆发

> 本周（6月8日-14日）GitHub Trending 周榜上，AI agent skills 类项目史无前例地占据了榜单半数席位——7 个技能项目集中涌入，从"让 AI 帮你做研究"到"给 AI 装上眼睛看全网"，skills 正在成为大模型应用层的标准载体。

## 本周趋势速览

| 趋势 | 说明 |
|------|------|
| 最大赢家 | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) 周 +12,053，登顶周榜冠军 |
| 本周主题 | AI agent skills 生态集体爆发：last30days / agent-skills / graphify / taste-skill / pm-skills / SkillSpector / Agent-Reach 七个项目同框 |
| 新面孔 | headroom（token 压缩）、graphify（代码知识图谱）、taste-skill（品味约束）等多个新项目首次上榜 |
| 持续热门 | markitdown 总星 15.3 万、PowerToys 总星 13.5 万、opencv 总星 8.9 万，老牌项目仍稳坐万星俱乐部 |
| 跨域补充 | apple/container（轻量 Linux 容器）、PowerToys（Windows 效率）、mattermost（协作平台）撑起非 AI 阵营 |

## 项目详细解读

### AI & Agent Skills 生态（本周主题）

#### 1. [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill)

**项目简介：** 一个 AI agent skill，能跨 Reddit、X（Twitter）、YouTube、Hacker News、Polymarket 以及通用 Web 调研任意主题，最后合成一份有来源依据的总结。本质上是一个"研究技能插件"，把"过去 30 天某话题在全网怎么讨论"变成 AI agent 可以一键调用的能力。

**核心亮点：**
- 覆盖六大信息源（Reddit/X/YouTube/HN/Polymarket/Web），输出带原始链接的 grounded summary，区别于纯生成式回答
- 以 skill 形式交付，可挂载到主流 AI 编程/agent 工具中复用，不需要自建爬虫
- 强调 recency（时效性）维度——这是大语言模型训练数据之后的"新鲜信息缺口"

**快速上手：** 项目用 Python 编写，以 skill 包形式安装；具体命令见仓库 README，通常是克隆后注册到 agent skill 目录即可调用。

**适合人群：** 需要做趋势调研、舆情追踪、热点总结的开发者和数据分析师。

> Star: 42,002 | Fork: 3,415 | 协议: MIT | 语言: Python | 本周涨幅: +12,053

---

#### 2. [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)

**项目简介：** 一组面向 AI 编程 agent 的"生产级工程技能"——把代码审查、重构、安全检查、性能优化等工程实践封装成 skill，让 agent 在写代码时遵循更专业的工程规范。作者在社区有长期的前端工程经验积累，项目走的是"工程化、可上生产"路线。

**核心亮点：**
- 覆盖 agent-skills / antigravity / claude-code / cursor 等多个主流 agent 运行时，跨工具复用
- 走 Shell 脚本路线，依赖少、易审计、易二次修改
- 6,440 个 fork 说明社区在它基础上派生了大量定制化技能

**快速上手：** 仓库以 Shell 脚本组织技能单元，克隆后按 README 指示把对应 skill 目录链接到 agent 配置路径即可。

**适合人群：** 重度使用 AI 编程工具、希望让 agent 更"懂工程规范"的开发者。

> Star: 59,470 | Fork: 6,440 | 协议: MIT | 语言: Shell | 本周涨幅: +10,445

---

#### 3. [safishamsi/graphify](https://github.com/safishamsi/graphify)

**项目简介：** 一个 AI 编程助手 skill（兼容 Claude Code、Codex、OpenCode、Cursor、Gemini CLI 等多种运行时），能把任意代码目录、SQL schema、R 脚本、shell 脚本、文档、论文甚至图像/视频，统一转成一张可查询的知识图谱——应用代码、数据库 schema、基础设施在同一张图里。

**核心亮点：**
- 基于 tree-sitter 解析 + Leiden 社区发现算法，把"代码即图"做成了 GraphRAG 的工程化实现
- 跨格式统一建模：代码、SQL、文档、图像视频进同一张图，查询时不再割裂
- 兼容六大主流 AI 编程工具，作为 skill 注入即用

**快速上手：** Python 实现，按 README 在目标目录执行索引命令生成图谱，再让 agent skill 查询。

**适合人群：** 维护大型代码库、需要"代码库级问答"的后端/平台工程师。

> Star: 67,149 | Fork: 6,803 | 协议: MIT | 语言: Python | 本周涨幅: +5,478

---

#### 4. [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)

**项目简介：** 一个给 AI agent"装上好品味"的 skill——核心目标是阻止 AI 生成"无聊、通用、像工厂流水线产物"的输出（项目原文称之为 generic slop）。它本质是一个"品味约束层"，在前端、设计、低代码场景下尤为常见。

**核心亮点：**
- 直接对 agent 输出做风格把关，缓解 AI 生成内容同质化的痛点
- 覆盖 claude / claude-code / codex / frontend / lowcode / nocode / vibecoding 多个场景
- 27 个 issues 说明项目活跃但稳定，社区反馈集中

**快速上手：** Shell 实现，按 skill 标准方式注册到 agent 后，在生成阶段自动介入约束。

**适合人群：** 做前端、设计、低代码生成的开发者，以及被"AI 风格千篇一律"困扰的创作者。

> Star: 43,687 | Fork: 3,054 | 协议: MIT | 语言: Shell | 本周涨幅: +7,591

---

#### 5. [phuryn/pm-skills](https://github.com/phuryn/pm-skills)

**项目简介：** 一个 PM（产品经理）技能市场，提供 100+ 个 agent skill、command 和 plugin，覆盖从需求发现、产品策略、执行、上线到增长的全产品生命周期。把产品经理的日常工作流变成了可被 AI agent 调用的能力集合。

**核心亮点：**
- 技能数量过百，是目前少见地"把非编程岗位的工作流 skill 化"的项目
- 覆盖 discovery → strategy → execution → launch → growth 完整链路
- 与 claude-code-marketplace / claude-code-plugins 生态对齐，可直接挂载

**快速上手：** 仓库按主题组织 skill 目录，按 README 把需要的技能子集注册到 agent 即可。

**适合人群：** 产品经理、增长运营，以及想用 agent 辅助产品工作的创业者。

> Star: 18,063 | Fork: 1,860 | 协议: MIT | 语言: - | 本周涨幅: +5,713

---

#### 6. [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector)

**项目简介：** 一个面向 AI agent skill 的安全扫描器——检测 skill 中的漏洞、恶意模式和安全隐患。随着 skills 生态爆发，"第三方 skill 是不是安全"成了刚需问题，NVIDIA 这一次直接给出了官方的安全审计工具。

**核心亮点：**
- 填补了"skill 供应链安全"空白：skills 可以执行代码、访问数据，安全扫描是刚需而非锦上添花
- 检测维度涵盖漏洞、恶意模式、安全风险三类
- Apache-2.0 协议，NVIDIA 官方背书，适合企业级引入

**快速上手：** Python 实现，按 README 对目标 skill 包执行扫描命令即可输出风险报告。

**适合人群：** 企业安全团队、agent 平台维护者，以及任何准备引入第三方 skill 的开发者。

> Star: 5,274 | Fork: 403 | 协议: Apache-2.0 | 语言: Python | 本周涨幅: +3,669

---

#### 7. [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)

**项目简介：** 让你的 AI agent"长出眼睛看全网"——一条 CLI 读取并搜索 Twitter、Reddit、YouTube、GitHub、Bilibili、小红书，零 API 费用。本质上是把分散在各平台的公开数据访问能力打包成 agent 可调用的统一接口。

**核心亮点：**
- 覆盖六大平台（含 Bilibili、小红书两个中文平台），对中文开发者友好
- 强调 zero API fees，走抓取/转录路线而非付费 API
- 同时提供 MCP 集成，可作为 agent 的标准数据源工具

**快速上手：** Python 实现，按 README 安装后通过 CLI 命令或 MCP 接入 agent 即可调用各平台数据。

**适合人群：** 做舆情监测、内容分析、跨平台数据聚合的开发者。

> Star: 28,738 | Fork: 2,355 | 协议: MIT | 语言: Python | 本周涨幅: +5,468

---

### AI 工具与效率

#### 8. [chopratejas/headroom](https://github.com/chopratejas/headroom)

**项目简介：** 在工具输出、日志、文件、RAG chunk 进入大语言模型之前，先把它们压缩掉——号称 60-95% 更少 token、相同答案。同时提供 library、proxy、MCP server 三种形态，是目前"上下文工程（context engineering）"赛道里工程化程度很高的一个项目。

**核心亮点：**
- 同时覆盖 library / proxy / MCP 三种接入方式，适配不同 agent 架构
- 兼容 anthropic / openai / langchain / claude-code / cursor 主流生态
- 60-95% 的 token 压缩率直接对应成本下降，对长上下文场景价值明显

**快速上手：** Python + TypeScript 双实现，可作库引入，也可起 proxy 拦截 agent 流量，或挂 MCP server。

**适合人群：** 重度使用 agent 调用、上下文成本敏感的团队，以及做 RAG 系统的工程师。

> Star: 27,567 | Fork: 1,869 | 协议: Apache-2.0 | 语言: Python | 本周涨幅: +10,653

---

#### 9. [microsoft/markitdown](https://github.com/microsoft/markitdown)

**项目简介：** 微软出品的 Python 工具，把各种文件和 Office 文档统一转成 Markdown。在 RAG/agent 时代，"把异构文档变成大模型能直接吃的 Markdown"几乎是每个知识库项目的第一步，markitdown 把这一步标准化了。

**核心亮点：**
- 总星 15.3 万，是本周榜单里"老而弥坚"的代表，持续被 RAG 项目当作数据预处理层
- 同时作为 autogen-extension 和 langchain 集成存在，无缝接入主流 agent 框架
- 覆盖 microsoft-office / pdf 等核心办公格式，企业场景刚需

**快速上手：** `pip install 'markitdown[all]'` 安装后，`markitdown input.docx > output.md` 即可完成转换。

**适合人群：** 搭建知识库、RAG 系统、文档问答系统的开发者和数据工程师。

> Star: 153,353 | Fork: 10,603 | 协议: MIT | 语言: Python | 本周涨幅: +6,280

---

#### 10. [lfnovo/open-notebook](https://github.com/lfnovo/open-notebook)

**项目简介：** Notebook LM 的开源实现，定位是"更灵活、功能更多"的开源替代。把"上传资料 → AI 帮你读、帮你总结、帮你生成播客式音频"这条流程做成了可自托管的开源产品。

**核心亮点：**
- TypeScript 实现，可自托管，数据不离开自有基础设施
- 覆盖 assistant / learning / note-taking / self-learning 多个学习场景
- MIT 协议 + 3,462 fork，社区二次开发活跃

**快速上手：** 按仓库 README 起本地服务（Node 环境），上传资料后即可使用问答/总结/生成功能。

**适合人群：** 注重数据隐私的研究者、学生，以及想自建"个人 AI 学习助手"的用户。

> Star: 30,526 | Fork: 3,462 | 协议: MIT | 语言: TypeScript | 本周涨幅: +3,468

---

### AI Agent 与计算机视觉

#### 11. [aaif-goose/goose](https://github.com/aaif-goose/goose)

**项目简介：** 一个开源、可扩展的 AI agent，定位"超越单纯的代码补全"——能安装、执行、编辑、测试代码，且支持任意大语言模型。Rust 实现，强调性能与可扩展性，是 agent 赛道里少见的 Rust 重型项目。

**核心亮点：**
- 覆盖 install / execute / edit / test 全流程，不只是补全代码片段
- model-agnostic（任意 LLM），不绑定单一模型供应商
- 支持 ACP（Agent Communication Protocol）和 MCP，可作为 agent 编排节点

**快速上手：** 按仓库 README 用 Rust 工具链或预编译二进制安装，配置模型后即可作为本地 agent 运行。

**适合人群：** 想要本地、可扩展、不锁定模型供应商的 AI 编程 agent 用户。

> Star: 49,375 | Fork: 5,214 | 协议: Apache-2.0 | 语言: Rust | 本周涨幅: +2,165

---

#### 12. [roboflow/supervision](https://github.com/roboflow/supervision)

**项目简介：** Roboflow 出品的可复用计算机视觉工具库——"我们替你写好那些反复要写的 CV 工具"。覆盖检测、分割、跟踪、标注格式转换、指标计算等 CV 工程里高频重复的活。

**核心亮点：**
- 一站式覆盖 classification / detection / segmentation / tracking / metrics
- 兼容 COCO / Pascal VOC / YOLO 主流数据格式，PyTorch / TensorFlow 双后端
- 提供 oriented bounding box 等进阶能力，工业级场景（如航拍、文档）直接可用

**快速上手：** `pip install supervision`，配合 YOLO/Detectron 等模型输出即可做后处理与可视化。

**适合人群：** 做 CV 应用、模型评测、数据流水线的算法与工程开发者。

> Star: 44,193 | Fork: 3,926 | 协议: MIT | 语言: Python | 本周涨幅: +3,315

---

#### 13. [opencv/opencv](https://github.com/opencv/opencv)

**项目简介：** 计算机视觉领域的开源基石——OpenCV 官方仓库，覆盖图像处理、几何变换、特征提取、相机标定、传统机器学习等 CV 经典能力，是几乎所有 CV 项目都绕不开的底层库。本周再次回到周榜，说明 CV 基础设施的需求依然稳定。

**核心亮点：**
- 总星 8.9 万 + fork 5.6 万，是本周榜单里"年龄最大、生态最厚"的项目（2012 年至今）
- C++ 核心 + 多语言绑定，跨平台、跨语言复用
- 与 deep-learning 生态（PyTorch/TF）互补：传统 CV 算子 + DL 推理可组合使用

**快速上手：** 各平台用包管理器安装（`apt install libopencv-dev` / `brew install opencv` / vcpkg），或从源码编译。

**适合人群：** 所有涉及图像/视频处理的开发者，从嵌入式到云端全覆盖。

> Star: 89,125 | Fork: 56,656 | 协议: Apache-2.0 | 语言: C++ | 本周涨幅: +1,227

---

### 非 AI 跨域基础设施

#### 14. [apple/container](https://github.com/apple/container)

**项目简介：** 苹果官方出品的容器工具——在 Mac 上用轻量级虚拟机创建并运行 Linux 容器，用 Swift 编写，针对 Apple silicon 优化。给 macOS 用户提供了一个"原生、轻量、苹果风格"的 Linux 容器方案。

**核心亮点：**
- 用轻量级 VM 跑 Linux 容器，兼顾隔离性与启动速度
- Swift 原生实现 + Apple silicon 优化，在 M 系列芯片上体验顺滑
- Apache-2.0 协议，苹果官方维护，长期可期待

**快速上手：** 按仓库 README 在 macOS 上安装（通常通过 Homebrew 或官方发布包），随后用类 Docker 命令拉起 Linux 容器。

**适合人群：** Mac 开发者、需要在 Apple silicon 上跑 Linux 容器环境的工程师。

> Star: 36,965 | Fork: 1,060 | 协议: Apache-2.0 | 语言: Swift | 本周涨幅: +10,021

---

## 本周总结

第24周（6月8日-14日）GitHub Trending 周榜最大的信号是：**AI agent skills 生态已经从"零散项目"进化到"成建制涌现"**——7 个 skills 项目同框上榜，覆盖调研（last30days）、工程化（agent-skills）、知识图谱（graphify）、品味约束（taste-skill）、产品经理（pm-skills）、安全审计（SkillSpector）、全网数据访问（Agent-Reach）七个不同切面，几乎构成了一个完整的"skill 供应链"。

如果只推荐两个最值得关注的：**[chopratejas/headroom](https://github.com/chopratejas/headroom)** 解决了 agent 跑起来最痛的 token 成本问题（周 +10,653、压缩率 60-95%），是基础设施级的刚需；**[NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector)** 则补上了 skills 生态最缺的安全审计环节——当 skill 可以执行代码、访问数据时，"用之前先扫一遍"会成为标配。

跨域方面，**[apple/container](https://github.com/apple/container)** 周 +10,021 表明 Mac 上的轻量 Linux 容器方案同样有强劲需求，是本周非 AI 阵营里最值得关注的项目。

---

**数据来源：** GitHub Trending Weekly 页面 + GitHub API（`gh api repos/{owner}/{repo}`），统计周期为 2026年6月8日-14日（第24周）。文中 Star/Fork/Issues/协议/语言字段均取自 GitHub API 实时返回值；周涨幅（weekly_stars）以 Weekly Trending 页面为准。所有项目描述基于仓库原始 `description` 字段翻译整理。
